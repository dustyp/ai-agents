# CRA-46 Architecture Prototypes

This directory contains early prototypes for the architectural redesign of the AI Agents system, focusing on separating state from code with a database backend.

## Overview

These prototypes demonstrate the core concepts for CRA-46, providing working examples of:

1. Pydantic data models for structured agent state
2. Database interfaces for PostgreSQL and SQLite
3. LangGraph orchestration for agent workflows

## Contents

- `schema_prototype.py`: Pydantic models for agent state, procedures, and rules
- `database_prototype.py`: Database abstraction for storing and retrieving agent data
- `orchestration_prototype.py`: LangGraph-based workflow orchestration

## Key Concepts

### Data Modeling with Pydantic

The schema prototype demonstrates how to:
- Define structured data models for all agent components
- Validate data at runtime
- Serialize/deserialize to JSON for database storage
- Create type-safe interfaces for agent state manipulation

### Database Abstraction

The database prototype demonstrates:
- Abstract interface supporting multiple backends
- Implementation for PostgreSQL (production) and SQLite (development)
- Proper schema creation with JSON support
- Connection pooling and efficient database operations
- Factory pattern for database creation

### Agent Orchestration with LangGraph

The orchestration prototype demonstrates:
- State graph for agent workflow
- Transitions between planning, executing, verifying, and sleeping phases
- Integration with LLM for complex reasoning
- Preservation of agent state between operations
- Procedure execution with verification

## Getting Started

These prototypes require Python 3.9+ and can be installed with:

```bash
pip install pydantic langchain langgraph asyncpg aiosqlite
```

For running locally, SQLite provides the simplest option. For production, PostgreSQL is recommended.

## Development Roadmap

1. Phase 1: Implement basic state storage in database (these prototypes)
2. Phase 2: Migrate procedures and rules to database
3. Phase 3: Create full Python orchestration layer
4. Phase 4: Add monitoring, optimization, and advanced features

## Design Decisions

- **PostgreSQL with JSONB**: Chosen for production for its combination of structure and flexibility
- **SQLite for Development**: Simplifies local testing without external dependencies
- **Langgraph for Orchestration**: Provides explicit state management for agent workflows
- **Pydantic for Schema**: Enforces type safety while supporting complex nested structures

## Notes

These prototypes are illustrative examples to demonstrate the architectural approach. They are not production-ready and omit error handling, authentication, and other important aspects that would be included in the final implementation.