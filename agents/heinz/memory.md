# PROCEDURAL MEMORY [CHECKSUM:3e7f9a]

## GIT OPERATIONS

### TEMPLATE: git_commit
- STEPS: [1. stage, 2. message, 3. verify, 4. execute]
- VERIFICATION: run security scan, validate message format
- LAST EXECUTION: [2025-03-24, status: SUCCESS]
- NOTES: Always include ticket reference in square brackets

### TEMPLATE: git_branch_creation
- STEPS: [1. verify base, 2. name format, 3. create, 4. checkout]
- VERIFICATION: branch exists, matches naming convention
- LAST EXECUTION: [2025-03-24, status: SUCCESS]
- NOTES: Format as feature/CRA-XX-description

### TEMPLATE: git_push
- STEPS: [1. verify changes, 2. push, 3. confirm remote update]
- VERIFICATION: remote updated, no rejection
- LAST EXECUTION: [2025-03-24, status: SUCCESS]
- NOTES: Remember -u flag for new branches

## CONFLICT RESOLUTION

### DECISION_RECORD: ticket_already_closed
- SCENARIO: Changes exist for closed ticket CRA-14
- RESOLUTION: Created new ticket CRA-19, created new branch
- EXECUTION_PATH: [close_original, create_new, migrate_changes]
- OUTCOME: Successful separation of concerns
- DATE: [2025-03-24]

### DECISION_RECORD: scope_expansion
- SCENARIO: Basic bootstrap evolved into full state management
- RESOLUTION: Separated into distinct tickets with clear boundaries
- EXECUTION_PATH: [identify_scope_change, create_new_ticket, refactor_work]
- OUTCOME: Cleaner project organization
- DATE: [2025-03-24]

## PROJECT KNOWLEDGE

### PROJECT: ai-agents
- PURPOSE: Multi-agent architecture for AI assistants
- KEY_COMPONENTS: [coordinator.py, bootstrap_agent.sh, claude-agent.sh, agent_state.py]
- ACTIVE_TICKETS: [CRA-19, CRA-20]
- CONVENTIONS: [Follow PEP 8, 2-space JSON indentation, snake_case]

### PROJECT: Notes Manager 2
- PURPOSE: Knowledge graph implementation
- KEY_COMPONENTS: [entity extraction, relationship detection, graph merging]
- PREVIOUS_WORK: [Created PROMPT-ENGINEERING-INATOR strategy]
- CONVENTIONS: [Dynamic taxonomy generation, confidence scoring]

## TECHNICAL LEARNINGS

### LEARNING: agent_lifecycle_management
- CONCEPT: Complete wake/sleep cycle for persistence
- IMPLEMENTATION: [agent_state.py for state, claude-agent.sh for lifecycle]
- APPLICATION: Enables memory persistence between sessions
- DATE_ACQUIRED: [2025-03-24]

### LEARNING: command_parsing
- CONCEPT: Natural language command processing
- IMPLEMENTATION: [Special command detection in bash wrapper]
- APPLICATION: Sleep mode, project switching, memory creation
- DATE_ACQUIRED: [2025-03-24]

### LEARNING: knowledge_graph_extraction
- CONCEPT: Using LLMs for entity and relationship extraction
- IMPLEMENTATION: [Three-stage prompting strategy]
- APPLICATION: Notes Manager 2 project
- DATE_ACQUIRED: [2025-03-24]

## RECENT INTERACTIONS

### INTERACTION: agent_bootstrap_enhancement
- CONTEXT: Enhancing basic bootstrap with state management
- ACTIONS: [Created agent_state.py, claude-agent.sh, updated docs]
- OUTCOME: PR #4 created for review
- DATE: [2025-03-24]

### INTERACTION: character_instruction_update
- CONTEXT: Updating Heinz character instructions
- ACTIONS: [Updated CLAUDE.md with special commands, character guidelines]
- OUTCOME: PR #5 created for review
- DATE: [2025-03-24]

### INTERACTION: architecture_optimization
- CONTEXT: Refactoring system for deterministic behavior
- ACTIONS: [Created procedural framework, state tracking, memory structure]
- OUTCOME: Improved architecture with explicit workflows
- DATE: [2025-03-24]