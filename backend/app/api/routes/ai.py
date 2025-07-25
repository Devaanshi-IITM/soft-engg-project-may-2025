#General
from datetime import datetime
import operator
import tempfile
import logging
import shutil
import os

# FastAPI imports
from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse

# LangChain/LangGraph imports
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.tools import tool, Tool
from langgraph.graph import StateGraph, END

from langchain_groq import ChatGroq

from groq import Groq, APIError
import dateparser

from app.models.requests.content import ContentCreate, ContentRead
from app.models.requests.ai import UserInput, AIResponse
from app.api.deps import AgentState, agent_app, extract_text, add_reminder, call_llm, call_tool, should_continue

os.environ["GROQ_API_KEY"] = "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"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

groq_client = Groq()
llm = ChatGroq(model="llama3-8b-8192", temperature=0) # Using Llama 3 8B model


router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/transcribe-audio")
async def transcribe_audio(audio_file: UploadFile):

    if not audio_file.filename:
        raise HTTPException(status_code=400, detail="No audio file uploaded.")

    temp_audio_path = None

    try:
        temp_file_suffix = "." + audio_file.filename.split(".")[-1] if "." in audio_file.filename else ".tmp"
        with tempfile.NamedTemporaryFile(delete=False, suffix=temp_file_suffix) as temp_audio_file:
            shutil.copyfileobj(audio_file.file, temp_audio_file)
            temp_audio_path = temp_audio_file.name
        
        logging.info(f"Audio file saved temporarily at: {temp_audio_path}")

        # Transcribe the audio using Groq's Whisper model
        # We need to open the temporary file in binary read mode.
        with open(temp_audio_path, "rb") as file_to_transcribe:
            logging.info("Sending audio to Groq Whisper model...")
            transcription = groq_client.audio.transcriptions.create(
                file=file_to_transcribe,
                model="whisper-large-v3",  # Groq's Whisper model
                response_format="verbose_json" # You can also try "srt" or "vtt" for structured output
            )
        
        transcribed_text = transcription.text
        logging.info("Transcription successful.")
        
        return JSONResponse(status_code=200, content={"transcribed_text": transcribed_text})

    except APIError as e:
        # Catch specific Groq API errors
        logging.error(f"Groq API Error: {e}")
        error_detail = f"Groq API error: {e.response.status_code} - {e.response.text}" if e.response else str(e)
        raise HTTPException(
            status_code=e.response.status_code if e.response else 500,
            detail=f"Groq API transcription failed: {error_detail}"
        )
    except Exception as e:
        # Catch any other unexpected errors
        logging.exception("An unexpected error occurred during transcription.")
        raise HTTPException(
            status_code=500,
            detail=f"An internal server error occurred: {e}"
        )
    finally:
        # Ensure the temporary file is deleted, even if an error occurred
        if temp_audio_path and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
            logging.info(f"Temporary file deleted: {temp_audio_path}")


@router.post("/chat", response_model=AIResponse)
async def chat_with_agent(user_input: UserInput):
    """
    Sends a user query to the AI agent and receives a response.
    The agent will either set a reminder or respond directly.
    """
    # try:
    # Initial state setup: we start with the user's message
    initial_state = {"messages": [HumanMessage(content=user_input.text)]}

    # Invoke the LangGraph application asynchronously
    # The recursion_limit is a safeguard to prevent infinite loops in more complex graphs
    result = await agent_app.ainvoke(initial_state, {"recursion_limit": 50})

    # Determine the final message to return
    final_response_content = ""
    # The 'messages' list in the final state contains all interactions
    # The last message is usually the most relevant for the final user response
    if result and result.get("messages"):
        last_message = result["messages"][-1]
        if isinstance(last_message, ToolMessage):
            final_response_content = f"Reminder operation successful: {last_message.content}"
        elif isinstance(last_message, AIMessage):
            final_response_content = last_message.content
        else: # Fallback for other message types
            final_response_content = str(last_message.content)
    else:
        final_response_content = "An unexpected error occurred or no response was generated."


    return AIResponse(response=final_response_content)