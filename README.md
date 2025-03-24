# AI Agents System

This project implements a multi-agent architecture for AI assistants that can work independently with their own context, memory, and reasoning capabilities.

## Overview

The AI Agents system allows you to create and interact with AI characters that have:
- Persistent memory and personality
- Independent LLM sessions
- Message-based communication
- Session logging and context management
- Specialized expertise and character traits

## Directory Structure

```
~/_projects/ai-agents/
├── agents/                  # Individual agent directories
│   └── heinz/               # Dr. Heinz Doofenshmirtz agent
│       ├── personality.md   # Character definition
│       ├── memory.md        # Persistent memory
│       ├── inbox.json       # Messages sent to the agent
│       ├── outbox.json      # Responses from the agent
│       ├── session_log.md   # Log of interactions
│       └── prompt_template.md # Template for LLM prompting
└── coordinator.py           # Message passing system
```

## Usage

### Sending Messages to Agents

```bash
python coordinator.py send heinz "Could you review this knowledge graph implementation?"
# With subject and type
python coordinator.py send heinz "Review attached schema" --subject "Knowledge Graph Review" --type "task"
```

### Getting Agent Responses

```bash
python coordinator.py get heinz
# Keep messages marked as unread
python coordinator.py get heinz --keep-unread
```

### Creating New Agents

```bash
python coordinator.py create david
```

### Responding as an Agent (for development)

```bash
python coordinator.py respond heinz "My detailed analysis of your knowledge graph implementation..."
```

### Listing Available Agents

```bash
python coordinator.py list
```

### Bootstrapping an Agent

The bootstrap script initializes an agent with system context, tools information, and project details:

```bash
./bootstrap_agent.sh heinz
```

This sends a sequence of initialization messages to the agent's inbox to prepare it for a session.

## Agent Workflow

1. **Message Delivery**: Messages are delivered to an agent's inbox
2. **Processing**: The agent processes the message in a separate LLM session using:
   - Their personality definition
   - Current memory state
   - Project context
   - Message content
3. **Response**: Agent writes response to their outbox
4. **Memory Update**: Agent updates their memory with new information
5. **Logging**: All interactions are logged in the session_log.md file

## Integration with Notes Manager 2

Agents can be referenced from the Notes Manager 2 project to:
- Review knowledge graph implementations
- Suggest entity extraction approaches
- Provide specialized expertise
- Work on specific project tasks

## Running an Agent Session

To run a session with an agent:

1. Open a Claude-Code or similar LLM session
2. Load the agent's personality, memory, and context
3. Process messages from their inbox
4. Generate responses to their outbox
5. Update their memory and session log

## Example Agent: Dr. Heinz Doofenshmirtz

Dr. Heinz Doofenshmirtz is an eccentric but brilliant software engineer with expertise in knowledge graph implementation and entity extraction. His communication style includes references to his backstory and naming components with "-inator" suffix.

## Development & Contribution

Please follow our [GitHub Workflow](./github-workflow.md) guidelines when contributing to this project. Our workflow is based on:

- Linear ticket integration
- Feature branch development
- Clean, focused commits
- Code reviews before merging
- Continuous integration testing

## Acknowledgments

- Inspired by multi-agent AI architectures
- Character concepts based on popular media
- Built with Claude Code and Python
