#General
from datetime import datetime
import operator
import tempfile
import logging
import shutil
import os

# LangChain/LangGraph imports
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool, Tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langchain_groq import ChatGroq

# Api lib
from typing import TypedDict, Annotated, Sequence, Optional, List
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from groq import Groq, APIError
import dateparser

os.environ["GROQ_API_KEY"] = "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"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(
    title       = "API",
    description = "This application can be used to convert Audio to Text and to set llm powered reminders",
    version     = "1.0.0",
)

groq_client = Groq()
llm = ChatGroq(model="llama3-8b-8192", temperature=0) # Using Llama 3 8B model



def extract_text(filecontent):
    """Loads the ASR model when the FastAPI application starts up."""
    logger.info(f"Passing audio content to wisper model")
    try:
        filename = filecontent.filename
        print(filename)
        print(type(filecontent))
        print(filecontent)
        data     = filecontent.read()
        print(type(data))
        transcription = groq_client.audio.transcriptions.create(
            file=(filename, data),
            model="whisper-large-v3",
            response_format="verbose_json",
            ).text.strip()
        
        logger.info("Text extracted successfully.")
        return transcription
    except Exception as e:
        logger.error(f"Failed to extract text: {e}")
        raise RuntimeError(f"{e}")


@app.get("/health")
def health_check():
    """
    Checks the health of the application and model.
    """
    return {"status": "healthy"}

@app.post("/transcribe-audio")
async def transcribe_audio(audio_file: UploadFile = File(...)):

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

####### LLM Powered Reminder ######

class AddReminderInput(BaseModel):
    reason: str         = Field(description="The reason or description of the reminder.")
    date  : str         = Field(description="The date for the reminder (e.g., '2023-10-27', 'tomorrow', 'next Monday').")
    time: Optional[str] = Field(None, description="The specific time for the reminder (e.g., '10:00 AM', '15:30', 'noon'). Use 24-hour format if possible.")

@tool(args_schema=AddReminderInput)
def add_reminder(reason: str, date: str, time: Optional[str] = None) -> str:
    """
    Adds a new reminder to the system.
    Parses natural language date and time into a structured format for storage.
    """
    print(reason, date, time)
    print("Insert reminder function here")
    parsed_date = dateparser.parse(date)
    parsed_time = None
    if time:
        # Try to parse time, potentially combining with date if needed for full datetime object
        parsed_time_obj = dateparser.parse(time, settings={'RELATIVE_BASE': parsed_date})
        if parsed_time_obj:
            parsed_time = parsed_time_obj.strftime("%H:%M") # Format to HH:MM

    if not parsed_date:
        return f"Could not parse the date '{date}'. Please provide a clearer date."
    return f"Reminder '{reason}' set successfully for {parsed_date.strftime('%Y-%m-%d')}{' at ' + parsed_time if parsed_time else ''}."

# Declaring list of tools
tools = [add_reminder]
tool_executor = ToolExecutor(tools)
llm_with_tools = llm.bind_tools(tools)


# Define Agent state
class AgentState(TypedDict):
    """
    Represents the state of our agent.
    - messages: A list of messages depicting the conversation history.
    - tool_calls: Contains information about tools the LLM wants to call.
    - tool_response: The output received after executing a tool.
    - agent_outcome: The final message from the agent if no tool call happens or after tool execution.
    """
    messages     : Annotated[Sequence[BaseMessage], operator.add]
    tool_calls   : Optional[List[dict]]
    tool_response: Optional[str]
    agent_outcome: Optional[AIMessage] # Final direct response from LLM, or after tool execution

# Define the chat prompt
system_message = """You are a helpful and efficient AI assistant specializing in managing reminders.
Your primary goal is to determine if the user's request is to set a reminder.

If the user wants to set a reminder:
- Use the 'add_reminder' tool.
- Extract the 'reason', 'date', and optionally 'time' from the user's input.
- Be intelligent about parsing natural language dates and times (e.g., 'tomorrow', 'next week', '3 PM', 'noon', 'end of day').
- If a specific time is not mentioned, you should try to infer it if contextually relevant (e.g., 'morning' -> '9 AM') or leave it as None if no time context is provided.
- If any crucial information (like the reason or a clear date) is missing for a reminder, you MUST ask clarifying questions before attempting to call the tool. For example, if they say 'Remind me to do something', ask 'What should I remind you to do and when?'.

If the user's request is NOT about setting a reminder (e.g., general questions, greetings):
- Respond directly and helpfully to their query without attempting to use any tools.

Be concise and get straight to the point.
"""
prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    MessagesPlaceholder(variable_name="messages"),
])

# Chain the prompt with the LLM
agent_runnable = prompt | llm_with_tools


# Node to call the LLM
def call_llm(state: AgentState):
    """
    Invokes the LLM with the current conversation history and updates the state.
    """
    messages = state["messages"]
    response = agent_runnable.invoke({"messages": messages})
    return {"messages": [response], "tool_calls": response.tool_calls, "agent_outcome": response}

def call_tool(state: AgentState):
    """
    Executes the tool chosen by the LLM and updates the state.
    """
    tool_name = state["tool_calls"][0]["name"] # Assuming one tool call for simplicity
    tool_args = state["tool_calls"][0]["args"]

    tool_output = tool_executor.invoke(state["tool_calls"][0])
    return {"messages": [ToolMessage(content=str(tool_output), tool_call_id=state["tool_calls"][0]["id"])], "tool_response": tool_output}

def should_continue(state: AgentState) -> str:
    """
    Determines whether the graph should continue to the tool node or end.
    """
    if state["tool_calls"]:
        return "Intend_to_set_reminder" # Go to tool node if LLM wants to call a tool
    else:
        return "end" # End the graph if LLM provides a direct answer (no tool call)


# Flow
workflow = StateGraph(AgentState)
# Add nodes
workflow.add_node("llm", call_llm)
workflow.add_node("tool", call_tool)

# Set entry point
workflow.set_entry_point("llm")

workflow.add_conditional_edges(
    "llm", # From LLM node
    should_continue, # Conditional logic
    {
        "Intend_to_set_reminder": "tool",
        "end": END
    }
)

# After tool execution, always end the graph for this simplified flow
workflow.add_edge("tool", END)
agent_app = workflow.compile()

class UserInput(BaseModel):
    text: str = Field(..., example="Remind me to call mom tomorrow at 3 PM about her doctor's appointment.")

class AIResponse(BaseModel):
    response: str
    reminders_list: Optional[List[dict]] = None

@app.post("/chat/", response_model=AIResponse, summary="Interact with the Reminder Agent")
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

    # except Exception as e:
    #     print(f"Error during agent invocation: {e}")
    #     return AIResponse(response=f"An error occurred: {str(e)}")