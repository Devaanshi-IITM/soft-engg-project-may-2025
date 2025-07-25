from app.core.db.postgres import SessionLocal
from app.core.db.mongo import db as mongo_db
from app.core.db.redis import redis_client as redis
import logging
import os

# LangChain/LangGraph imports
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.tools import tool, Tool
from langgraph.graph import StateGraph, END

from langchain_groq import ChatGroq

from groq import Groq, APIError

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_mongo_db():
    try:
        yield mongo_db
    finally:
        # No explicit close needed for motor, but can be used if needed
        pass

def get_redis():
    try:
        yield redis
    finally:
        # No explicit close needed for aioredis, but can be used if needed
        pass

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

def add_reminder(reason: str, date: str, time: Optional[str] = None) -> str:
    """
    Adds a new reminder to the system.
    Parses natural language date and time into a structured format for storage.
    """
    
    ########################################################
    #########  Insert Reminder function here ############### 
    #########################################################

    return f"Reminder '{reason}' set successfully for {date} and time {time}"

# Declaring list of tools
tools = [add_reminder]
# tool_executor = ToolExecutor(tools)
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
    print("=====================")
    # print(messages)
    # print(response)
    print(response.tool_calls[0])
    print("=====================")
    return {"messages": [response], "tool_calls": response.tool_calls, "agent_outcome": response}

def call_tool(state: AgentState):
    """
    Executes the tool chosen by the LLM and updates the state.
    """
    tool_name = state["tool_calls"][0]["name"] # Assuming one tool call for simplicity
    tool_args = state["tool_calls"][0]["args"]
    print("=====================")
    print(tool_name)
    print(tool_args)
    print(state['tool_calls'][0])
    print("=====================")
    
    return {
        "messages": [
            ToolMessage(
                content=add_reminder(reason=tool_args['reason'], date=tool_args['date'], time=tool_args['time']),
                tool_call_id = state['tool_calls'][0]['id']
            )
        ]
    }

def should_continue(state: AgentState) -> str:
    """
    Determines whether the graph should continue to the tool node or end.
    """
    if state["tool_calls"]:
        print("Intend_to_set_reminder activated")
        return "Intend_to_set_reminder" # Go to tool node if LLM wants to call a tool
    else:
        return "end" # End the graph if LLM provides a direct answer (no tool call)


# Flow
workflow = StateGraph(AgentState)
# Add nodes
workflow.add_node("llm", call_llm)
workflow.add_node("run_tool", call_tool)

# Set entry point
workflow.set_entry_point("llm")

workflow.add_conditional_edges(
    "llm", # From LLM node
    should_continue, # Conditional logic
    {
        "Intend_to_set_reminder": "run_tool",
        "end": END
    }
)

# After tool execution, always end the graph for this simplified flow
workflow.add_edge("run_tool", END)
agent_app = workflow.compile()

