import asyncio
import json
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from abc import ABC, abstractmethod
from enum import Enum

# Define Enums for Memory Types and State Phases
class MemoryType(Enum):
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    PROCEDURAL = "procedural"

class AgentStatePhase(Enum):
    IDLE = "idle"
    WORKING = "working"
    SLEEPING = "sleeping"
    ERROR = "error"

# Agent State (Pydantic-like for now)
class DatabaseAgentState:
    """Simplified agent state class for demonstration."""
    def __init__(self, agent_id: str, user_id: str, data: Dict[str, Any]):
        self.agent_id = agent_id
        self.user_id = user_id
        self.data = data # General agent state
        
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.data)
    
    @classmethod
    def from_json(cls, agent_id: str, user_id: str, json_str: str) -> 'DatabaseAgentState':
        """Create from JSON string."""
        return cls(agent_id, user_id, json.loads(json_str))

# Define Pydantic models for TaskState, SessionState, and AgentState
from pydantic import BaseModel, Field
class TaskState(BaseModel):
    task_id: str
    description: str
    status: str  # e.g., "to_do", "in_progress", "completed"
    dependencies: List[str] = Field(default_factory=list)
    assigned_resources: List[str] = Field(default_factory=list) # List of agent_ids working on the task
    relevance_score: float = 0.0

class SessionState(BaseModel):
    session_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    active_task_id: Optional[str] = None
    recent_activities: List[str] = Field(default_factory=list) # Keep track of the last few actions
    agent_phase: AgentStatePhase = AgentStatePhase.IDLE

class AgentContext(BaseModel):
    agent_id: str
    agent_name: str
    user_id: str  # Associate the agent with a specific user
    personality: str  # Description of agent's personality
    rules: List[str] # List of rule IDs applicable to the agent
    state: Dict[str, Any] = Field(default_factory=dict)

#Memory Entry
class MemoryEntry(BaseModel):
    memory_id: str
    user_id: str # User associated with the memory
    agent_id: str # Agent associated with the memory
    memory_type: MemoryType
    content: str
    relevance_score: float = 0.0  # Initial relevance score

#Procedure
class Procedure(BaseModel):
    procedure_id: str
    name: str
    description: str
    steps: List[str]
    complexity: str
    rules: List[str] = Field(default_factory=list)  # List of rule IDs applicable to the procedure

class DatabaseInterface(ABC):
    """Abstract base class for database interfaces."""
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the database connection and create schemas if needed."""
        pass
    
    # Agent Context CRUD
    @abstractmethod
    async def store_agent_context(self, agent_context: AgentContext) -> None:
        """Store agent context in the database."""
        pass

    @abstractmethod
    async def get_agent_context(self, agent_id: str, user_id: str) -> Optional[AgentContext]:
        """Retrieve agent context from the database."""
        pass
        
    # Agent State CRUD
    @abstractmethod
    async def store_agent_state(self, agent_id: str, user_id: str, state_data: Dict[str, Any]) -> None:
        """Store agent state in the database."""
        pass
    
    @abstractmethod
    async def get_agent_state(self, agent_id: str, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve agent state from the database."""
        pass
    
    # Memory CRUD
    @abstractmethod
    async def store_memory(self, memory: MemoryEntry) -> None:
        """Store memory in the database."""
        pass

    @abstractmethod
    async def get_memory(self, memory_id: str, user_id: str, agent_id: str) -> Optional[MemoryEntry]:
         """Retrieve a memory from the database."""
         pass
    
    @abstractmethod
    async def search_memories(self, user_id: str, agent_id: str, query: str, memory_type: Optional[MemoryType] = None, limit: int = 10) -> List[MemoryEntry]:
        """Search memories based on a query and other criteria."""
        pass
    
    # Procedures CRUD
    @abstractmethod
    async def store_procedure(self, procedure: Procedure) -> None:
        """Store a procedure in the database."""
        pass
    
    @abstractmethod
    async def get_procedure(self, procedure_id: str) -> Optional[Procedure]:
        """Retrieve a procedure from the database."""
        pass
    
    @abstractmethod
    async def list_procedures(self) -> List[str]:
        """List all available procedure IDs."""
        pass

    # Rules CRUD (Simple - Expand Later if Needed)
    @abstractmethod
    async def store_rule(self, rule_id: str, rule_text: str) -> None:
        """Store a rule in the database."""
        pass
    
    @abstractmethod
    async def get_rule(self, rule_id: str) -> Optional[str]:
        """Retrieve a rule from the database."""
        pass
    
    @abstractmethod
    async def close(self) -> None:
        """Close the database connection."""
        pass

#PostgreSQL Implementation of the Adapted Database Interface
class PostgreSQLInterface(DatabaseInterface):
    """PostgreSQL implementation of the database interface."""

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.pool = None

    async def initialize(self) -> None:
        """Initialize the PostgreSQL connection pool and create schemas."""
        import asyncpg

        self.pool = await asyncpg.create_pool(self.connection_string)

        async with self.pool.acquire() as conn:
            # Create agent_context table
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS agent_context (
                    agent_id TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    agent_name TEXT NOT NULL,
                    personality TEXT,
                    rules TEXT[],
                    state_json JSONB,
                    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    PRIMARY KEY (agent_id, user_id)
                )
            ''')

            # Create agent_state table
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS agent_state (
                    agent_id TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    state_json JSONB NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    PRIMARY KEY (agent_id, user_id)
                )
            ''')

            # Create memory table
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS memory (
                    memory_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    agent_id TEXT NOT NULL,
                    memory_type TEXT NOT NULL,
                    content TEXT NOT NULL,
                    relevance_score REAL NOT NULL DEFAULT 0.0,
                    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
                )
            ''')

            # Create procedures table
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS procedures (
                    procedure_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    steps TEXT[],
                    complexity TEXT,
                    rules TEXT[],
                    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
                )
            ''')

            # Create rules table
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS rules (
                    rule_id TEXT PRIMARY KEY,
                    rule_text TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
                )
            ''')

            # Add update trigger for updated_at
            await conn.execute('''
                CREATE OR REPLACE FUNCTION update_timestamp()
                RETURNS TRIGGER AS $$
                BEGIN
                    NEW.updated_at = NOW();
                    RETURN NEW;
                END;
                $$ LANGUAGE plpgsql;
            ''')

            # Create triggers if they don't exist
            for table in ['agent_context', 'agent_state', 'memory', 'procedures', 'rules']:
                trigger_name = f"update_{table}_timestamp"

                # Check if trigger exists
                trigger_exists = await conn.fetchval(
                    "SELECT EXISTS(SELECT 1 FROM pg_trigger WHERE tgname = $1)",
                    trigger_name
                )

                if not trigger_exists:
                    await conn.execute(f'''
                        CREATE TRIGGER {trigger_name}
                        BEFORE UPDATE ON {table}
                        FOR EACH ROW
                        EXECUTE FUNCTION update_timestamp()
                    ''')

    async def store_agent_context(self, agent_context: AgentContext) -> None:
        """Store agent context in PostgreSQL."""
        async with self.pool.acquire() as conn:
            await conn.execute(
                '''
                INSERT INTO agent_context (agent_id, user_id, agent_name, personality, rules, state_json)
                VALUES ($1, $2, $3, $4, $5, $6::jsonb)
                ON CONFLICT (agent_id, user_id) DO UPDATE
                SET agent_name = $3,
                    personality = $4,
                    rules = $5,
                    state_json = $6::jsonb,
                    updated_at = NOW()
                ''',
                agent_context.agent_id,
                agent_context.user_id,
                agent_context.agent_name,
                agent_context.personality,
                agent_context.rules,
                agent_context.state.json() if isinstance(agent_context.state, BaseModel) else json.dumps(agent_context.state)
            )

    async def get_agent_context(self, agent_id: str, user_id: str) -> Optional[AgentContext]:
        """Retrieve agent context from PostgreSQL."""
        async with self.pool.acquire() as conn:
            result = await conn.fetchrow(
                '''
                SELECT agent_name, personality, rules, state_json
                FROM agent_context
                WHERE agent_id = $1 AND user_id = $2
                ''',
                agent_id,
                user_id
            )

            if result is None:
                return None

            return AgentContext(
                agent_id=agent_id,
                user_id=user_id,
                agent_name=result['agent_name'],
                personality=result['personality'],
                rules=result['rules'],
                state=json.loads(result['state_json'])
            )

    async def store_agent_state(self, agent_id: str, user_id: str, state_data: Dict[str, Any]) -> None:
        """Store agent state in PostgreSQL."""
        async with self.pool.acquire() as conn:
            await conn.execute(
                '''
                INSERT INTO agent_state (agent_id, user_id, state_json)
                VALUES ($1, $2, $3::jsonb)
                ON CONFLICT (agent_id, user_id) DO UPDATE
                SET state_json = $3::jsonb,
                    updated_at = NOW()
                ''',
                agent_id,
                user_id,
                json.dumps(state_data)
            )

    async def get_agent_state(self, agent_id: str, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve agent state from PostgreSQL."""
        async with self.pool.acquire() as conn:
            result = await conn.fetchrow(
                '''
                SELECT state_json
                FROM agent_state
                WHERE agent_id = $1 AND user_id = $2
                ''',
                agent_id,
                user_id
            )

            if result is None:
                return None

            return json.loads(result['state_json'])

    async def store_memory(self, memory: MemoryEntry) -> None:
        """Store memory in PostgreSQL."""
        async with self.pool.acquire() as conn:
            await conn.execute(
                '''
                INSERT INTO memory (memory_id, user_id, agent_id, memory_type, content, relevance_score)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (memory_id) DO UPDATE
                SET user_id = $2,
                    agent_id = $3,
                    memory_type = $4,
                    content = $5,
                    relevance_score = $6,
                    updated_at = NOW()
                ''',
                memory.memory_id,
                memory.user_id,
                memory.agent_id,
                memory.memory_type.value,
                memory.content,
                memory.relevance_score
            )

    async def get_memory(self, memory_id: str, user_id: str, agent_id: str) -> Optional[MemoryEntry]:
        """Retrieve a memory from PostgreSQL."""
        async with self.pool.acquire() as conn:
            result = await conn.fetchrow(
                '''
                SELECT user_id, agent_id, memory_type, content, relevance_score
                FROM memory
                WHERE memory_id = $1 AND user_id = $2 AND agent_id = $3
                ''',
                memory_id,
                user_id,
                agent_id
            )

            if result is None:
                return None

            return MemoryEntry(
                memory_id=memory_id,
                user_id=result['user_id'],
                agent_id=result['agent_id'],
                memory_type=MemoryType(result['memory_type']),
                content=result['content'],
                relevance_score=result['relevance_score']
            )

    async def search_memories(self, user_id: str, agent_id: str, query: str, memory_type: Optional[MemoryType] = None, limit: int = 10) -> List[MemoryEntry]:
        """Search memories based on a query and other criteria."""
        async with self.pool.acquire() as conn:
            # Construct the query
            base_query = '''
                SELECT memory_id, user_id, agent_id, memory_type, content, relevance_score
                FROM memory
                WHERE user_id = $1 AND agent_id = $2
            '''
            conditions = []
            values = [user_id, agent_id]

            if query:
                conditions.append("content ILIKE $3")  # ILIKE for case-insensitive search
                values.append(f"%{query}%")
            if memory_type:
                conditions.append("memory_type = $4")
                values.append(memory_type.value)

            if conditions:
                base_query += " AND " + " AND ".join(conditions)

            base_query += " ORDER BY relevance_score DESC, updated_at DESC LIMIT $" + str(len(values) + 1)
            values.append(limit)

            # Execute the query
            results = await conn.fetch(base_query, *values)

            # Convert results to MemoryEntry objects
            memories = [
                MemoryEntry(
                    memory_id=row['memory_id'],
                    user_id=row['user_id'],
                    agent_id=row['agent_id'],
                    memory_type=MemoryType(row['memory_type']),
                    content=row['content'],
                    relevance_score=row['relevance_score']
                )
                for row in results
            ]

            return memories

    async def store_procedure(self, procedure: Procedure) -> None:
        """Store a procedure in PostgreSQL."""
        async with self.pool.acquire() as conn:
            await conn.execute(
                '''
                INSERT INTO procedures (procedure_id, name, description, steps, complexity, rules)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (procedure_id) DO UPDATE
                SET name = $2,
                    description = $3,
                    steps = $4,
                    complexity = $5,
                    rules = $6,
                    updated_at = NOW()
                ''',
                procedure.procedure_id,
                procedure.name,
                procedure.description,
                procedure.steps,
                procedure.complexity,
                procedure.rules
            )

    async def get_procedure(self, procedure_id: str) -> Optional[Procedure]:
        """Retrieve a procedure from PostgreSQL."""
        async with self.pool.acquire() as conn:
            result = await conn.fetchrow(
                '''
                SELECT name, description, steps, complexity, rules
                FROM procedures
                WHERE procedure_id = $1
                ''',
                procedure_id
            )

            if result is None:
                return None

            return Procedure(
                procedure_id=procedure_id,
                name=result['name'],
                description=result['description'],
                steps=result['steps'],
                complexity=result['complexity'],
                rules=result['rules']
            )

    async def list_procedures(self) -> List[str]:
        """List all available procedure IDs from PostgreSQL."""
        async with self.pool.acquire() as conn:
            results = await conn.fetch(
                '''
                SELECT procedure_id
                FROM procedures
                ORDER BY procedure_id
                '''
            )

            return [row['procedure_id'] for row in results]

    async def store_rule(self, rule_id: str, rule_text: str) -> None:
        """Store a rule in PostgreSQL."""
        async with self.pool.acquire() as conn:
            await conn.execute(
                '''
                INSERT INTO rules (rule_id, rule_text)
                VALUES ($1, $2)
                ON CONFLICT (rule_id) DO UPDATE
                SET rule_text = $2,
                    updated_at = NOW()
                ''',
                rule_id,
                rule_text
            )

    async def get_rule(self, rule_id: str) -> Optional[str]:
        """Retrieve a rule from PostgreSQL."""
        async with self.pool.acquire() as conn:
            result = await conn.fetchrow(
                '''
                SELECT rule_text
                FROM rules
                WHERE rule_id = $1
                ''',
                rule_id
            )

            if result is None:
                return None

            return result['rule_text']

    async def close(self) -> None:
        """Close the PostgreSQL connection pool."""
        if self.pool:
            await self.pool.close()

# SQLite Implementation of the Adapted Database Interface
class SQLiteInterface(DatabaseInterface):
    """SQLite implementation of the database interface."""

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.db = None

    async def initialize(self) -> None:
        """Initialize the SQLite connection and create schemas."""
        import aiosqlite

        self.db = await aiosqlite.connect(self.db_path)

        # Enable JSON support
        await self.db.execute("PRAGMA journal_mode=WAL")

        # Create agent_context table
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS agent_context (
                agent_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                agent_name TEXT NOT NULL,
                personality TEXT,
                rules TEXT,
                state_json TEXT,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (agent_id, user_id)
            )
        ''')

        # Create agent_state table
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS agent_state (
                agent_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                state_json TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (agent_id, user_id)
            )
        ''')

        # Create memory table
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                memory_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                agent_id TEXT NOT NULL,
                memory_type TEXT NOT NULL,
                content TEXT NOT NULL,
                relevance_score REAL NOT NULL DEFAULT 0.0,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create procedures table
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS procedures (
                procedure_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                steps TEXT,
                complexity TEXT,
                rules TEXT,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create rules table
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS rules (
                rule_id TEXT PRIMARY KEY,
                rule_text TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create triggers for updated_at
        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS update_agent_context_timestamp
            AFTER UPDATE ON agent_context
            BEGIN
                UPDATE agent_context SET updated_at = CURRENT_TIMESTAMP
                WHERE agent_id = NEW.agent_id AND user_id = NEW.user_id;
            END;
        ''')

        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS update_agent_state_timestamp
            AFTER UPDATE ON agent_state
            BEGIN
                UPDATE agent_state SET updated_at = CURRENT_TIMESTAMP
                WHERE agent_id = NEW.agent_id AND user_id = NEW.user_id;
            END;
        ''')

        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS update_memory_timestamp
            AFTER UPDATE ON memory
            BEGIN
                UPDATE memory SET updated_at = CURRENT_TIMESTAMP
                WHERE memory_id = NEW.memory_id;
            END;
        ''')

        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS update_procedures_timestamp
            AFTER UPDATE ON procedures
            BEGIN
                UPDATE procedures SET updated_at = CURRENT_TIMESTAMP
                WHERE procedure_id = NEW.procedure_id;
            END;
        ''')

        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS update_rules_timestamp
            AFTER UPDATE ON rules
            BEGIN
                UPDATE rules SET updated_at = CURRENT_TIMESTAMP
                WHERE rule_id = NEW.rule_id;
            END;
        ''')

        await self.db.commit()

    async def store_agent_context(self, agent_context: AgentContext) -> None:
        """Store agent context in SQLite."""
        await self.db.execute(
            '''
            INSERT INTO agent_context (agent_id, user_id, agent_name, personality, rules, state_json)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT (agent_id, user_id) DO UPDATE
            SET agent_name = ?,
                personality = ?,
                rules = ?,
                state_json = ?
            ''',
            (
                agent_context.agent_id,
                agent_context.user_id,
                agent_context.agent_name,
                agent_context.personality,
                ",".join(agent_context.rules),
                agent_context.state.json() if isinstance(agent_context.state, BaseModel) else json.dumps(agent_context.state),
                agent_context.agent_name,
                agent_context.personality,
                ",".join(agent_context.rules),
                agent_context.state.json() if isinstance(agent_context.state, BaseModel) else json.dumps(agent_context.state)
            )
        )
        await self.db.commit()

    async def get_agent_context(self, agent_id: str, user_id: str) -> Optional[AgentContext]:
        """Retrieve agent context from SQLite."""
        cursor = await self.db.execute(
            '''
            SELECT agent_name, personality, rules, state_json
            FROM agent_context
            WHERE agent_id = ? AND user_id = ?
            ''',
            (agent_id, user_id)
        )
        result = await cursor.fetchone()

        if result is None:
            return None

        agent_name, personality, rules, state_json = result
        rules_list = rules.split(",") if rules else []

        return AgentContext(
            agent_id=agent_id,
            user_id=user_id,
            agent_name=agent_name,
            personality=personality,
            rules=rules_list,
            state=json.loads(state_json)
        )

    async def store_agent_state(self, agent_id: str, user_id: str, state_data: Dict[str, Any]) -> None:
        """Store agent state in SQLite."""
        await self.db.execute(
            '''
            INSERT INTO agent_state (agent_id, user_id, state_json)
            VALUES (?, ?, ?)
            ON CONFLICT (agent_id, user_id) DO UPDATE
            SET state_json = ?
            ''',
            (agent_id, user_id, json.dumps(state_data), json.dumps(state_data))
        )
        await self.db.commit()

    async def get_agent_state(self, agent_id: str, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve agent state from SQLite."""
        cursor = await self.db.execute(
            '''
            SELECT state_json
            FROM agent_state
            WHERE agent_id = ? AND user_id = ?
            ''',
            (agent_id, user_id)
        )
        result = await cursor.fetchone()

        if result is None:
            return None

        return json.loads(result[0])

    async def store_memory(self, memory: MemoryEntry) -> None:
        """Store memory in SQLite."""
        await self.db.execute(
            '''
            INSERT INTO memory (memory_id, user_id, agent_id, memory_type, content, relevance_score)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT (memory_id) DO UPDATE
            SET user_id = ?,
                agent_id = ?,
                memory_type = ?,
                content = ?,
                relevance_score = ?
            ''',
            (
                memory.memory_id,
                memory.user_id,
                memory.agent_id,
                memory.memory_type.value,
                memory.content,
                memory.relevance_score,
                memory.user_id,
                memory.agent_id,
                memory.memory_type.value,
                memory.content,
                memory.relevance_score
            )
        )
        await self.db.commit()

    async def get_memory(self, memory_id: str, user_id: str, agent_id: str) -> Optional[MemoryEntry]:
        """Retrieve a memory from SQLite."""
        cursor = await self.db.execute(
            '''
            SELECT user_id, agent_id, memory_type, content, relevance_score
            FROM memory
            WHERE memory_id = ? AND user_id = ? AND agent_id = ?
            ''',
            (memory_id, user_id, agent_id)
        )
        result = await cursor.fetchone()

        if result is None:
            return None

        user_id, agent_id, memory_type, content, relevance_score = result

        return MemoryEntry(
            memory_id=memory_id,
            user_id=user_id,
            agent_id=agent_id,
            memory_type=MemoryType(memory_type),
            content=content,
            relevance_score=relevance_score
        )

    async def search_memories(self, user_id: str, agent_id: str, query: str, memory_type: Optional[MemoryType] = None, limit: int = 10) -> List[MemoryEntry]:
        """Search memories based on a query and other criteria."""
        async with self.db.execute('''
            SELECT *
            FROM memory
            WHERE user_id = ?
            AND agent_id = ?
            AND (? IS NULL OR memory_type = ?)
            AND content LIKE ?
            ORDER BY relevance_score DESC
            LIMIT ?
        ''', (user_id, agent_id, memory_type.value if memory_type else None,
              memory_type.value if memory_type else None, f"%{query}%", limit)):
            rows = await self.db.fetchall()
            memories = []
            for row in rows:
                memory = MemoryEntry(
                    memory_id=row[0],
                    user_id=row[1],
                    agent_id=row[2],
                    memory_type=MemoryType(row[3]),
                    content=row[4],
                    relevance_score=row[5],
                )
                memories.append(memory)
            return memories

    async def store_procedure(self, procedure: Procedure) -> None:
        """Store a procedure in SQLite."""
        await self.db.execute(
            '''
            INSERT INTO procedures (procedure_id, name, description, steps, complexity, rules)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT (procedure_id) DO UPDATE
            SET name = ?,
                description = ?,
                steps = ?,
                complexity = ?,
                rules = ?
            ''',
            (
                procedure.procedure_id,
                procedure.name,
                procedure.description,
                ",".join(procedure.steps),
                procedure.complexity,
                ",".join(procedure.rules),
                procedure.name,
                procedure.description,
                ",".join(procedure.steps),
                procedure.complexity,
                ",".join(procedure.rules)
            )
        )
        await self.db.commit()

    async def get_procedure(self, procedure_id: str) -> Optional[Procedure]:
        """Retrieve a procedure from SQLite."""
        cursor = await self.db.execute(
            '''
            SELECT name, description, steps, complexity, rules
            FROM procedures
            WHERE procedure_id = ?
            ''',
            (procedure_id,)
        )
        result = await cursor.fetchone()

        if result is None:
            return None

        name, description, steps, complexity, rules = result
        steps_list = steps.split(",") if steps else []
        rules_list = rules.split(",") if rules else []

        return Procedure(
            procedure_id=procedure_id,
            name=name,
            description=description,
            steps=steps_list,
            complexity=complexity,
            rules=rules_list
        )

    async def list_procedures(self) -> List[str]:
        """List all available procedure IDs from SQLite."""
        cursor = await self.db.execute(
            '''
            SELECT procedure_id
            FROM procedures
            ORDER BY procedure_id
            '''
        )
        results = await cursor.fetchall()

        return [row[0] for row in results]

    async def store_rule(self, rule_id: str, rule_text: str) -> None:
        """Store a rule in SQLite."""
        await self.db.execute(
            '''
            INSERT INTO rules (rule_id, rule_text)
            VALUES (?, ?)
            ON CONFLICT (rule_id) DO UPDATE
            SET rule_text = ?
            ''',
            (rule_id, rule_text, rule_text)
        )
        await self.db.commit()

    async def get_rule(self, rule_id: str) -> Optional[str]:
        """Retrieve a rule from SQLite."""
        cursor = await self.db.execute(
            '''
            SELECT rule_text
            FROM rules
            WHERE rule_id = ?
            ''',
            (rule_id,)
        )
        result = await cursor.fetchone()

        if result is None:
            return None

        return result[0]

    async def close(self) -> None:
        """Close the SQLite connection."""
        if self.db:
            await self.db.close()

class DatabaseFactory:
    """Factory for creating database interfaces."""
    
    @staticmethod
    def create_interface(db_type: str, connection_info: Union[str, Dict[str, Any]]) -> DatabaseInterface:
        """Create a database interface based on the specified type."""
        if db_type == "postgresql":
            if isinstance(connection_info, dict):
                # Convert dict to connection string
                conn_str = " ".join(f"{k}={v}" for k, v in connection_info.items())
                return PostgreSQLInterface(conn_str)
            else:
                return PostgreSQLInterface(connection_info)
        elif db_type == "sqlite":
            if isinstance(connection_info, dict):
                return SQLiteInterface(connection_info['path'])
            else:
                return SQLiteInterface(connection_info)