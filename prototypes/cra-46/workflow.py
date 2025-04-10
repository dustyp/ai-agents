from langgraph.graph import StateGraph, END
from typing import List, Dict, TypedDict, Optional
from agent_state import AgentState
from agent_tools import summarize_tool
import json


def decide_next_step(state: AgentState) -> str:
    """Decides what to do next based on the agent's state."""
    print(f"[decide_next_step] State: {json.dumps(state, indent=2)}")
    if state.get("agent_response") is None:
        print("[decide_next_step] Returning: process_input")
        return "process_input"
    else:
        print("[decide_next_step] Returning: respond_to_user")
        return "respond_to_user"

def process_user_input(state: AgentState) -> Dict:
    """Processes the user input using the summarizer tool."""
    print(f"[process_user_input] Input state: {state.model_dump_json(indent=2)}")
    
    response = summarize_tool.func(state.user_input)
    print(f"[process_user_input] Response: {response}")
    
    # Return a dict for LangGraph compatibility
    return {
        "user_input": state.user_input,
        "agent_response": response,
        "conversation_history": state.conversation_history
    }

def respond_to_user(state: AgentState) -> AgentState:
    """Simple user response to return"""
    print(f"[respond_to_user] State: {json.dumps(state, indent=2)}")
    # Just return the state as is
    return state


# 1. Define a new graph
builder = StateGraph(AgentState)

# 2. Define the nodes
builder.add_node("process_input", process_user_input)  # process_input
builder.add_node("respond_to_user", respond_to_user)

# 3. Define the edges
builder.add_edge("process_input", "respond_to_user")

# Add conditional edge from respond_to_user based on the decide_next_step function
builder.add_conditional_edges(
    "respond_to_user",  # source node
    decide_next_step,   # routing function
    {
        "process_input": "process_input",
        "respond_to_user": END,
    }
)

# 4. Set the entrypoint
builder.set_entry_point("process_input")

# 5. Compile
graph = builder.compile()

# Function to print the graph structure
def print_graph_structure():
    """Print a text representation of the graph structure."""
    print("\n===== GRAPH STRUCTURE =====")
    print("Nodes:")
    for node in builder.nodes:
        print(f"  - {node}")
    
    print("\nEdges:")
    for edge in builder.edges:
        # Assuming edges are stored as (source, target) tuples in the set
        print(f"  - {edge[0]} -> {edge[1]}")
    
    print("===========================\n")