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
    
    
    
graph_builder = StateGraph(State)

def chatbot(state: State):
    return  {"messages": [llm.invoke(state["messages"])]}
    
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

user_input = input("Enter a message: ")
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})

print("state[messages]==========>", state["messages"])
print("state[messages][-1]==========>", state["messages"][-1].content)


