#!/usr/bin/env python3
"""
Simple CLI interface for interacting with an agent locally.
This allows for testing and development without needing to set up a web server.
"""

import asyncio
import os
import sys
import uuid
import json
from datetime import datetime
from typing import Dict, Any, Optional

# Import our agent components
from agent_state import AgentState
from agent_tools import summarize_tool
from workflow import builder, AgentStateDict, graph, print_graph_structure
from database_prototype import DatabaseFactory, SQLiteInterface

# Configure the database
DB_PATH = "agent_data.db"  # Local SQLite database file

class AgentCLI:
    """Command-line interface for interacting with the agent."""
    
    def __init__(self):
        """Initialize the agent CLI."""
        self.agent_id = "cli-agent"
        self.user_id = "local-user"
        self.db = None
        self.workflow = graph  # Use the compiled graph from workflow.py
        self.conversation_history = {}
        self.debug_mode = True
        
    async def initialize(self):
        """Initialize the agent CLI."""
        # Initialize database
        self.db = DatabaseFactory.create_interface("sqlite", DB_PATH)
        await self.db.initialize()
        
        # Try to load existing agent state
        state_data = await self.db.get_agent_state(self.agent_id, self.user_id)
        
        # If no agent state exists, create a new one
        if not state_data:
            state_data = {
                "conversation_history": {}
            }
        
        # Create initial state using Pydantic model
        self.state = AgentState(
            agent_id=self.agent_id,
            user_id=self.user_id,
            conversation_history=state_data.get("conversation_history", {}),
        )
        
        print(f"Agent initialized. Conversation history has {len(self.state.conversation_history)} entries.")
        print("Type 'exit' to quit, 'help' for commands.")
        
    async def process_message(self, message: str) -> str:
        """Process a user message through the agent workflow."""
        # Update state with new message
        self.state.user_input = message
        self.state.agent_response = None
        
        if self.debug_mode:
            print(f"\nProcessing message: {message}")
            print(f"Initial state: {self.state.model_dump_json(indent=2)}")
        
        # Run the workflow
        try:
            # Convert to dict for LangGraph compatibility
            result = await self.workflow.ainvoke(self.state.model_dump())
            
            if self.debug_mode:
                print("\nWorkflow execution completed.")
                print(f"Final state: {json.dumps(result, indent=2)}")
            
            # Update conversation history if we got a response
            if result.get("agent_response"):
                self.state.conversation_history[message] = result["agent_response"]
                self.state.agent_response = result["agent_response"]
                
                # Save updated state to database
                await self.db.store_agent_state(
                    self.agent_id,
                    self.user_id,
                    self.state.model_dump()
                )
                
                return self.state.agent_response
            else:
                return "I processed your message but don't have a specific response."
                
        except Exception as e:
            print(f"Error processing message: {str(e)}")
            return f"Sorry, I encountered an error: {str(e)}"
    
    async def run(self):
        """Run the agent CLI in an interactive loop."""
        await self.initialize()
        
        while True:
            # Get user input
            user_input = input("\nYou: ")
            
            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting agent CLI...")
                break
            
            # Check for help command
            if user_input.lower() == "help":
                print("\nAvailable commands:")
                print("  help - Show this help message")
                print("  exit/quit - Exit the CLI")
                print("  clear - Clear the conversation history")
                print("  debug - Toggle detailed debug output")
                print("  graph - Show the workflow graph structure")
                print("  Any other input will be sent to the agent")
                continue
            
            # Check for clear command
            if user_input.lower() == "clear":
                self.conversation_history = {}
                await self.db.store_agent_state(
                    self.agent_id, 
                    self.user_id, 
                    {"conversation_history": self.conversation_history}
                )
                print("Conversation history cleared.")
                continue
                
            # Check for debug command
            if user_input.lower() == "debug":
                self.debug_mode = not self.debug_mode
                print(f"Debug mode {'enabled' if self.debug_mode else 'disabled'}.")
                continue
                
            # Check for graph command
            if user_input.lower() == "graph":
                print_graph_structure()
                continue
            
            # Process the message
            print("\nProcessing...")
            response = await self.process_message(user_input)
            print(f"\nAgent: {response}")
    
    async def close(self):
        """Close the agent CLI and clean up resources."""
        if self.db:
            await self.db.close()


async def main():
    """Main function to run the agent CLI."""
    cli = AgentCLI()
    try:
        await cli.run()
    finally:
        await cli.close()


if __name__ == "__main__":
    asyncio.run(main())
