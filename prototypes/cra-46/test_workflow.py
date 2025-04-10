#!/usr/bin/env python3
"""
Test script for visualizing and testing the LangGraph workflow.
This script allows you to:
1. Visualize the workflow graph
2. Run a test message through the workflow
3. See detailed tracing of the execution
"""

import asyncio
import json
from workflow import builder, graph, print_graph_structure, AgentStateDict
from agent_state import AgentState

async def test_workflow():
    """Test the workflow with a sample message."""
    print("\n===== TESTING WORKFLOW =====")
    
    # Create a test state using Pydantic model
    test_state = AgentState(
        user_input="Tell me about the weather today",
        agent_response=None,
        conversation_history={}
    )
    
    print(f"Initial state: {test_state.model_dump_json(indent=2)}")
    
    # Run the workflow
    print("\nRunning workflow...")
    result = await graph.ainvoke(test_state.model_dump())
    
    print(f"\nFinal result: {json.dumps(result, indent=2)}")
    
    return result

def visualize_graph():
    """Attempt to visualize the graph if the required libraries are available."""
    print("Graph visualization is not available in current langgraph version.")
    print("Using text-based graph structure instead:")
    print_graph_structure()

async def main():
    """Main function to run the test script."""
    print("LangGraph Workflow Test and Visualization")
    print("----------------------------------------")
    
    # Print graph structure
    print_graph_structure()
    
    # Try to visualize the graph
    visualize_graph()
    
    # Test the workflow
    await test_workflow()
    
    print("\nTest completed!")

if __name__ == "__main__":
    asyncio.run(main())
