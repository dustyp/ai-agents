"""
CRA-46: Schema Prototype for Database-backed Agent State

This file demonstrates how Pydantic models could be used to represent agent state
that would be stored in a database instead of directly in git.
"""

from datetime import datetime
from typing import List, Dict, Optional, Any, Literal
from pydantic import BaseModel, Field


class AgentExecution(BaseModel):
    """Represents the current execution state of an agent."""
    phase: Literal["PLANNING", "EXECUTING", "VERIFYING", "SLEEPING"] = "PLANNING"
    active_procedure: Optional[str] = None
    step_index: int = 0
    validation_status: Optional[Literal["PENDING", "SUCCESS", "FAILURE"]] = None


class AgentContext(BaseModel):
    """Represents the agent's context and rule configuration."""
    loaded_rules: List[str] = Field(default_factory=list)
    rule_checksums: Dict[str, str] = Field(default_factory=dict)
    rule_source: str = "CLAUDE.md"
    reference_examples: bool = True
    refresh_required: bool = False


class AgentProject(BaseModel):
    """Represents the agent's current project context."""
    current: str
    active_tickets: List[str] = Field(default_factory=list)
    branch: str = "main"


class AgentSession(BaseModel):
    """Represents the agent's session information."""
    start_time: int  # Unix timestamp
    last_activity: int  # Unix timestamp
    interaction_count: int = 0


class AgentTasks(BaseModel):
    """Represents the agent's task management."""
    active: List[str] = Field(default_factory=list)
    completed: List[str] = Field(default_factory=list)
    blocked: List[str] = Field(default_factory=list)


class AgentMessage(BaseModel):
    """Represents a message in the agent's inbox or outbox."""
    id: str
    sender: str
    recipient: str
    subject: str
    content: str
    created_at: datetime
    read: bool = False
    message_type: str = "TEXT"


class AgentMemoryEntry(BaseModel):
    """Represents an entry in the agent's procedural memory."""
    category: str
    entry_type: str
    title: str
    content: Dict[str, Any]
    created_at: datetime
    updated_at: datetime


class AgentSessionLog(BaseModel):
    """Represents an entry in the agent's session log."""
    timestamp: datetime
    session_id: str
    entry_type: Literal["INPUT", "PROCESSING", "RESPONSE", "SYSTEM"]
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AgentState(BaseModel):
    """The complete state of an agent that would be stored in the database."""
    agent_id: str
    name: str
    execution: AgentExecution
    context: AgentContext
    project: AgentProject
    session: AgentSession
    tasks: AgentTasks
    emotional_state: str = "neutral"
    last_interaction: str = ""
    last_updated: int  # Unix timestamp


class AgentProcedure(BaseModel):
    """Represents a procedure that would be stored in the database."""
    id: str
    name: str
    description: str
    prerequisites: List[str] = Field(default_factory=list)
    steps: List[str] = Field(default_factory=list)
    rules: List[str] = Field(default_factory=list)
    visualization: Optional[str] = None
    errors: List[str] = Field(default_factory=list)
    related_procedures: Dict[str, str] = Field(default_factory=dict)
    complexity: Literal["SIMPLE", "STANDARD", "COMPLEX"] = "STANDARD"


class AgentRule(BaseModel):
    """Represents a rule that would be stored in the database."""
    id: str
    category: str
    description: str
    priority: Literal["HIGHEST", "HIGH", "MEDIUM", "LOW"] = "MEDIUM"
    examples: List[str] = Field(default_factory=list)
    checksum: str


# Example of how to create and potentially store an agent state
def create_example_agent_state() -> AgentState:
    """Creates an example agent state for demonstration purposes."""
    current_time = int(datetime.now().timestamp())
    
    return AgentState(
        agent_id="heinz",
        name="Dr. Heinz Doofenshmirtz",
        execution=AgentExecution(
            phase="SLEEPING",
            active_procedure="prepare_for_sleep",
            step_index=8,
            validation_status="SUCCESS"
        ),
        context=AgentContext(
            loaded_rules=["flattened"],
            rule_checksums={"flattened": "fe23696"},
            rule_source="CLAUDE.md",
            reference_examples=True,
            refresh_required=False
        ),
        project=AgentProject(
            current="ai-agents",
            active_tickets=[],
            branch="main"
        ),
        session=AgentSession(
            start_time=1711691460,
            last_activity=current_time,
            interaction_count=16
        ),
        tasks=AgentTasks(
            active=[],
            completed=[
                "Create feature/CRA-44 branch",
                "Simplify procedure format",
                "Add workflow documentation", 
                "Create procedure_menu.sh",
                "Convert rules to reference examples",
                "Resolve branch conflicts",
                "Clean up and merge PRs #15 and #17",
                "Clean up all feature branches"
            ],
            blocked=[]
        ),
        emotional_state="satisfied",
        last_interaction="Executed prepare_for_sleep procedure with full knowledge graph backup",
        last_updated=current_time
    )


if __name__ == "__main__":
    # This would demonstrate creation and serialization
    agent = create_example_agent_state()
    print(agent.model_dump_json(indent=2))
    
    # In a real implementation, this would connect to a database
    # and store the agent state.
    # Example:
    # 
    # import asyncpg
    # 
    # async def store_agent_state(agent: AgentState):
    #     conn = await asyncpg.connect(DATABASE_URL)
    #     await conn.execute(
    #         """
    #         INSERT INTO agent_states (agent_id, state_json) 
    #         VALUES ($1, $2)
    #         ON CONFLICT (agent_id) DO UPDATE
    #         SET state_json = $2
    #         """,
    #         agent.agent_id,
    #         agent.model_dump_json()
    #     )
    #     await conn.close()