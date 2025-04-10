"""
CRA-46: Orchestration Prototype

This file demonstrates how LangGraph could be used to manage agent state transitions
and orchestrate workflow between database, Python logic, and LLM.
"""

import os
import json
from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from datetime import datetime

from langchain.schema import AIMessage, HumanMessage
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END


# Define state types
class AgentPhase(str, Enum):
    PLANNING = "PLANNING"
    EXECUTING = "EXECUTING"
    VERIFYING = "VERIFYING"
    SLEEPING = "SLEEPING"


class AgentState:
    """Simplified agent state class for demonstration."""
    def __init__(self, agent_id: str, data: Dict[str, Any]):
        self.agent_id = agent_id
        self.data = data
        self.messages: List[Dict[str, Any]] = []
        self.current_procedure: Optional[str] = None
        self.procedure_step: int = 0
        self.phase: AgentPhase = AgentPhase.PLANNING
        self.completion_status: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for state graph."""
        return {
            "agent_id": self.agent_id,
            "data": self.data,
            "messages": self.messages,
            "current_procedure": self.current_procedure,
            "procedure_step": self.procedure_step,
            "phase": self.phase,
            "completion_status": self.completion_status
        }

    @classmethod
    def from_dict(cls, state_dict: Dict[str, Any]) -> 'AgentState':
        """Create from dictionary."""
        state = cls(state_dict["agent_id"], state_dict["data"])
        state.messages = state_dict["messages"]
        state.current_procedure = state_dict["current_procedure"]
        state.procedure_step = state_dict["procedure_step"]
        state.phase = state_dict["phase"]
        state.completion_status = state_dict["completion_status"]
        return state


# Mock functions that would interact with the database
async def load_agent_state(agent_id: str) -> AgentState:
    """Load agent state from database."""
    # In a real implementation, this would fetch from the database
    return AgentState(agent_id, {
        "name": "Dr. Heinz Doofenshmirtz",
        "emotional_state": "satisfied",
        "last_updated": datetime.now().timestamp()
    })


async def save_agent_state(state: AgentState) -> None:
    """Save agent state to database."""
    # In a real implementation, this would save to the database
    print(f"Saving agent state: {json.dumps(state.to_dict(), default=str)}")


async def load_procedure(procedure_id: str) -> Dict[str, Any]:
    """Load procedure from database."""
    # In a real implementation, this would fetch from the database
    
    # Example prepare_for_sleep procedure
    return {
        "name": "prepare_for_sleep",
        "description": "Prepares agent for session end with proper state preservation",
        "steps": [
            "Document current ticket progress with specific details",
            "List all related tickets and dependencies",
            "Record current procedure/step position in workflow",
            "Create clear resumption plan with next actions",
            "Document emotional state for continuity",
            "Update session_state.md with comprehensive status",
            "Update session_log.md with session entry",
            "Backup state to knowledge graph memory"
        ],
        "complexity": "STANDARD"
    }


# LLM interaction functions
def get_llm():
    """Get LLM instance."""
    # In production, this would use Claude or appropriate LLM
    # For demonstration, we use OpenAI
    return ChatOpenAI(temperature=0)


def create_system_prompt(state: AgentState) -> str:
    """Create system prompt based on agent state."""
    agent_name = state.data.get("name", "AI Agent")
    emotional_state = state.data.get("emotional_state", "neutral")
    
    if state.current_procedure:
        return f"""You are {agent_name}, currently in the {state.phase} phase.
Your emotional state is: {emotional_state}.
You are executing the {state.current_procedure} procedure, on step {state.procedure_step + 1}.
Respond in character based on your personality and current state."""
    else:
        return f"""You are {agent_name}, currently in the {state.phase} phase.
Your emotional state is: {emotional_state}.
Respond in character based on your personality and current state."""


# State graph node functions
async def initialize_state(state: Dict[str, Any]) -> Dict[str, Any]:
    """Initialize the agent state."""
    agent_state = await load_agent_state("heinz")
    
    # Convert to dictionary for state graph
    return agent_state.to_dict()


async def determine_next_action(state: Dict[str, Any]) -> Dict[str, Any]:
    """Determine the next action based on input."""
    agent_state = AgentState.from_dict(state)
    
    # Parse the last user message to determine action
    if agent_state.messages and agent_state.messages[-1]["role"] == "user":
        user_message = agent_state.messages[-1]["content"]
        
        # Check for procedure requests
        if "prepare_to_sleep" in user_message.lower() or "prepare_for_sleep" in user_message.lower():
            agent_state.current_procedure = "prepare_for_sleep"
            agent_state.procedure_step = 0
            agent_state.phase = AgentPhase.PLANNING
            
            # Load procedure details
            procedure = await load_procedure("prepare_for_sleep")
            
            # Add procedure information to state
            agent_state.data["active_procedure"] = procedure
    
    return agent_state.to_dict()


async def planning_phase(state: Dict[str, Any]) -> Dict[str, Any]:
    """Planning phase of the agent workflow."""
    agent_state = AgentState.from_dict(state)
    
    # Get LLM
    llm = get_llm()
    
    # Create system prompt
    system_prompt = create_system_prompt(agent_state)
    
    # Create messages for LLM
    messages = [SystemMessage(content=system_prompt)]
    
    # Add context about the procedure
    if agent_state.current_procedure and "active_procedure" in agent_state.data:
        procedure = agent_state.data["active_procedure"]
        
        planning_prompt = f"""
You need to execute the {agent_state.current_procedure} procedure.

Description: {procedure['description']}

This procedure has {len(procedure['steps'])} steps:
{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(procedure['steps']))}

How will you approach this procedure? Please outline your plan.
"""
        messages.append(HumanMessage(content=planning_prompt))
    else:
        messages.append(HumanMessage(content="What would you like to do next?"))
    
    # Get response from LLM
    response = llm.invoke(messages)
    
    # Update state with response
    agent_state.messages.append({"role": "assistant", "content": response.content})
    
    # Move to executing phase if we have a procedure
    if agent_state.current_procedure:
        agent_state.phase = AgentPhase.EXECUTING
    
    return agent_state.to_dict()


async def executing_phase(state: Dict[str, Any]) -> Dict[str, Any]:
    """Executing phase of the agent workflow."""
    agent_state = AgentState.from_dict(state)
    
    # Get procedure
    procedure = agent_state.data.get("active_procedure")
    
    if not procedure:
        # No procedure to execute, return to planning
        agent_state.phase = AgentPhase.PLANNING
        return agent_state.to_dict()
    
    # Get current step
    current_step_idx = agent_state.procedure_step
    if current_step_idx >= len(procedure["steps"]):
        # Finished all steps, move to verification
        agent_state.phase = AgentPhase.VERIFYING
        return agent_state.to_dict()
    
    current_step = procedure["steps"][current_step_idx]
    
    # Get LLM
    llm = get_llm()
    
    # Create system prompt
    system_prompt = create_system_prompt(agent_state)
    
    # Create execution prompt
    execution_prompt = f"""
You are executing step {current_step_idx + 1} of the {agent_state.current_procedure} procedure:
"{current_step}"

Please execute this step now. Describe exactly what you're doing in character.
When you've completed this step, clearly indicate that you've finished it and are ready for the next step.
"""
    
    # Create messages for LLM
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=execution_prompt)
    ]
    
    # Get response from LLM
    response = llm.invoke(messages)
    
    # Update state with response
    agent_state.messages.append({"role": "assistant", "content": response.content})
    
    # Move to next step
    agent_state.procedure_step += 1
    
    # If we've finished all steps, move to verification
    if agent_state.procedure_step >= len(procedure["steps"]):
        agent_state.phase = AgentPhase.VERIFYING
    
    return agent_state.to_dict()


async def verification_phase(state: Dict[str, Any]) -> Dict[str, Any]:
    """Verification phase of the agent workflow."""
    agent_state = AgentState.from_dict(state)
    
    # Get procedure
    procedure = agent_state.data.get("active_procedure")
    
    if not procedure:
        # No procedure to verify, return to planning
        agent_state.phase = AgentPhase.PLANNING
        return agent_state.to_dict()
    
    # Get LLM
    llm = get_llm()
    
    # Create system prompt
    system_prompt = create_system_prompt(agent_state)
    
    # Create verification prompt
    verification_prompt = f"""
You have completed all steps of the {agent_state.current_procedure} procedure:

{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(procedure["steps"]))}

Please verify that each step was executed correctly. 
Indicate any issues or incomplete steps.
If everything is correct, confirm completion of the procedure.
"""
    
    # Create messages for LLM
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=verification_prompt)
    ]
    
    # Get response from LLM
    response = llm.invoke(messages)
    
    # Update state with response
    agent_state.messages.append({"role": "assistant", "content": response.content})
    
    # Check if verification indicates success
    # For the demo, we'll assume success if the response contains specific phrases
    success_indicators = ["successfully completed", "all steps executed", "procedure complete"]
    completion_status = any(indicator in response.content.lower() for indicator in success_indicators)
    
    agent_state.completion_status = completion_status
    
    # If successfully completed, move to sleeping phase
    if completion_status:
        agent_state.phase = AgentPhase.SLEEPING
        
        # Update state data
        agent_state.data["last_procedure"] = agent_state.current_procedure
        agent_state.data["last_updated"] = datetime.now().timestamp()
        
        # For prepare_for_sleep specifically
        if agent_state.current_procedure == "prepare_for_sleep":
            agent_state.data["execution"] = {
                "phase": "SLEEPING",
                "active_procedure": "prepare_for_sleep",
                "step_index": len(procedure["steps"]),
                "validation_status": "SUCCESS"
            }
    else:
        # If verification failed, go back to execution
        agent_state.phase = AgentPhase.EXECUTING
        # Reset to start of procedure
        agent_state.procedure_step = 0
    
    return agent_state.to_dict()


async def sleeping_phase(state: Dict[str, Any]) -> Dict[str, Any]:
    """Sleeping phase of the agent workflow."""
    agent_state = AgentState.from_dict(state)
    
    # Save state to database
    await save_agent_state(agent_state)
    
    # Create a goodbye message
    agent_state.messages.append({
        "role": "assistant", 
        "content": f"I've successfully completed the {agent_state.current_procedure} procedure and saved my state. I'm now in sleep mode until reactivated."
    })
    
    # Signal end of workflow
    return {"__end__": True, **agent_state.to_dict()}


def should_end(state: Dict[str, Any]) -> str:
    """Determine if the workflow should end."""
    if state.get("__end__", False):
        return END
    
    # Otherwise, return the phase
    agent_state = AgentState.from_dict(state)
    return agent_state.phase


def build_agent_workflow() -> StateGraph:
    """Build the agent workflow state graph."""
    # Create state graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("initialize", initialize_state)
    workflow.add_node("determine_next_action", determine_next_action)
    workflow.add_node(AgentPhase.PLANNING, planning_phase)
    workflow.add_node(AgentPhase.EXECUTING, executing_phase)
    workflow.add_node(AgentPhase.VERIFYING, verification_phase)
    workflow.add_node(AgentPhase.SLEEPING, sleeping_phase)
    
    # Add edges
    workflow.add_edge("initialize", "determine_next_action")
    workflow.add_edge("determine_next_action", should_end)
    
    # Connect phases
    workflow.add_edge(AgentPhase.PLANNING, AgentPhase.EXECUTING)
    workflow.add_edge(AgentPhase.EXECUTING, AgentPhase.EXECUTING)
    workflow.add_edge(AgentPhase.EXECUTING, AgentPhase.VERIFYING)
    workflow.add_edge(AgentPhase.VERIFYING, AgentPhase.EXECUTING)
    workflow.add_edge(AgentPhase.VERIFYING, AgentPhase.SLEEPING)
    workflow.add_edge(AgentPhase.SLEEPING, END)
    
    # Set entry point
    workflow.set_entry_point("initialize")
    
    return workflow


async def main():
    """Main function to demonstrate the workflow."""
    # Build workflow
    workflow = build_agent_workflow()
    
    # Compile the workflow
    app = workflow.compile()
    
    # Initialize with a user message
    inputs = {"messages": [{"role": "user", "content": "I'd like you to prepare_for_sleep now."}]}
    
    # Run the workflow
    outputs = await app.ainvoke(inputs)
    
    # Print final state
    print("\nFinal State:")
    print(json.dumps(outputs, indent=2, default=str))
    
    # Print messages
    print("\nConversation:")
    for msg in outputs.get("messages", []):
        role = msg["role"]
        content = msg["content"]
        print(f"\n{role.upper()}:\n{content}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())