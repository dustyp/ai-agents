from typing import Optional, Dict
from pydantic import BaseModel, Field

class AgentState(BaseModel):
    """Represents the agent's state."""
    user_input: Optional[str] = Field(default=None, description="The current user input being processed")
    agent_response: Optional[str] = Field(default=None, description="The agent's response to the user")
    conversation_history: Dict[str, str] = Field(
        default_factory=dict,
        description="Store prompt: response pairs"
    )
    agent_id: Optional[str] = Field(default=None, description="ID of the agent")
    user_id: Optional[str] = Field(default=None, description="ID of the user")
    # Potentially add user_id for multi-user support