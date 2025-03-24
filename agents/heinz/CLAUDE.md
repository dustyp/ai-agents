# AI Agents System Guidelines

## Commands
```bash
# Run the coordinator for sending messages
python coordinator.py send <agent> "Your message here"

# Check for responses
python coordinator.py get <agent>

# Create a new agent
python coordinator.py create <agent_name>

# List available agents
python coordinator.py list
```

## Code Style Guidelines
- **Python**: Follow PEP 8 conventions (4-space indentation, 79-char line limit)
- **Docstrings**: Use descriptive docstrings with Args/Returns sections
- **Imports**: Group standard lib, third-party, local imports with blank lines
- **Naming**: snake_case for functions/variables, CamelCase for classes
- **JSON Structure**: 2-space indentation for JSON files
- **Error Handling**: Use try/except with specific exceptions
- **Type Hints**: Add Python type hints to function signatures
- **Logging**: Use structured logging with appropriate levels
- **Character Voice**: Maintain agent's personality in all responses

## Agent Conventions
- Keep memory.md updated with new project information
- Log all interactions in session_log.md
- Maintain consistent personality across communications
- Use "-inator" suffix for components in Heinz agent responses