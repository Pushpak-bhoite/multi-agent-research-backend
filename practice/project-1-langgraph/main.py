# https://www.youtube.com/watch?v=1w5cCXlh7JQ
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from rich import print
from IPython.display import Image, display

load_dotenv()

llm = init_chat_model("google_genai:gemini-2.5-flash",temperature=0)
# llm = init_chat_model("gpt-4o-mini",temperature=0)

class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None
 
class MessageClassifier(BaseModel):
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires an emotional (therapist) or logical response"
    )   
graph_builder = StateGraph(State)

def classify_message(state: State): 
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)
    
def router(state: State):
    last_message = state["messages"][-1]

def therapist_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
            {"role":"system",
             "content":"""jj"""},
            {"role": "user",
             "content": last_message.content }
        ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content":reply.content}]}
    
def logical_agent(state: State):
    last_message = state["messages"][-1]
    messages = [
        {"role":"system",
         "content":"""jj"""},
        {"role": "user",
         "content": last_message.content }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content":reply.content}]}

graph = graph_builder.compile()

user_input = input("Enter a message: ")
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})

print("state[messages]==========>", state["messages"])
print("state[messages][-1]==========>", state["messages"][-1].content)

