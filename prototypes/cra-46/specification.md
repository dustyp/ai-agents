class Agent(BaseModel):
    """Represents an agent and all its associated data"""
    agent_id: str
    agent_name: str
    user_id: str  # Associate the agent with a specific user
    personality: str  # Description of agent's personality
    rules: List[str]  # List of rule IDs applicable to the agent
    phase: str = "idle"  # Current operational phase
    current_task_id: Optional[str] = None
    variables: Dict[str, Any] = Field(default_factory=dict) 

OK so we have an agent definition.....based on Heinz here are the things I think an agent needs.

* Name
* id
* user_id? Nope...that is some kind of relationship we need to think about
* personality 
* rules
* status
* session_state
* memory 
* tools 
    * Tool id
    * Tool identity (need to know how to secure tokens)
    * Tool RBAC (what this agent can do with this tool or not)[FUTURE FOR SURE]
