#!/usr/bin/env python3
"""
Simple test script to check LangGraph functionality.
"""

print("Testing LangGraph imports...")

try:
    from langgraph.graph import StateGraph, END
    print("✓ Successfully imported StateGraph and END from langgraph.graph")
except ImportError as e:
    print(f"✗ Error importing from langgraph.graph: {e}")

try:
    from typing import TypedDict, Optional, Dict
    
    # Define a simple state type
    class SimpleState(TypedDict, total=False):
        count: int
        message: str
    
    # Define a simple function
    def increment(state: SimpleState) -> SimpleState:
        return {"count": state.get("count", 0) + 1, "message": state.get("message", "")}
    
    # Create a simple graph
    builder = StateGraph(SimpleState)
    builder.add_node("increment", increment)
    builder.set_entry_point("increment")
    builder.add_edge("increment", END)
    
    # Compile the graph
    graph = builder.compile()
    
    print("✓ Successfully created and compiled a simple LangGraph")
    
    # Print the graph structure
    print("\nGraph Structure:")
    print(f"  Nodes: {list(builder.nodes.keys())}")
    print(f"  Entry Point: {builder._entry_point}")
    
except Exception as e:
    print(f"✗ Error creating LangGraph: {e}")

print("\nLangGraph test completed.")
