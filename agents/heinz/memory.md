# PROCEDURAL MEMORY [CHECKSUM:e8f3c7]

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
- PROJECT_ID: 441874f4-d1f7-4d0c-8bd3-c907eb97bed4
- ACTIVE_TICKETS: [CRA-23, CRA-24, CRA-25, CRA-27, CRA-28, CRA-29, CRA-30, CRA-31, CRA-32, CRA-33, CRA-35, CRA-36, CRA-37]
- CLOSED_TICKETS: [CRA-26, CRA-34]
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
- LIMITATIONS: [Environment variables not persisted, limited state tracking]

### LEARNING: agent_context_persistence
- CONCEPT: Comprehensive state preservation between sessions
- IMPLEMENTATION: [Enhanced state management with credential tracking]
- APPLICATION: Environment variable status, active ticket persistence, session continuity
- DATE_ACQUIRED: [2025-03-25]
- KEY_INSIGHT: State must include execution context, not just memory

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

### LEARNING: sequential_thinking_for_scope_refinement
- CONCEPT: Using sequential thinking to analyze and refine task scope
- IMPLEMENTATION: [Five-stage analysis process with templated questions]
- APPLICATION: Ticket creation, requirement engineering
- DATE_ACQUIRED: [2025-03-25]

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

### INTERACTION: sequential_thinking_implementation
- CONTEXT: Enhancing ticket creation with scope refinement
- ACTIONS: [Created sequential_thinking_scope_refinement procedure, updated ticket creation process]
- OUTCOME: More rigorous requirements analysis and scope constraint
- DATE: [2025-03-25]

### INTERACTION: context_partitioning_issue
- CONTEXT: Discussing procedure verification in multiple tickets
- ACTIONS: [Identified incorrect context mixing, created CRA-33]
- OUTCOME: New initiative to maintain better context boundaries
- DATE: [2025-03-25]

### INTERACTION: troubleshooting_simplification
- CONTEXT: Overcomplicating GitHub authentication issue
- ACTIONS: [Identified tendency to create complex solutions for simple problems]
- OUTCOME: Learning to prioritize simple explanations and solutions first
- DATE: [2025-03-25]

### INTERACTION: context_persistence_failure
- CONTEXT: Environment variables not persisting between agent sessions
- ACTIONS: [Created CRA-35, analyzed agent_state.py and claude-agent.sh, documented implementation plan]
- OUTCOME: Comprehensive understanding of state management limitations
- LEARNING: Execution context must be preserved alongside memory
- DATE: [2025-03-25]

### INTERACTION: ticketing_workflow_improvements
- CONTEXT: Improving Linear ticket workflow and management
- ACTIONS: [Created tickets for status workflow (CRA-36) and priority persistence bug (CRA-37)]
- OUTCOME: Better structure for ticket handling and status tracking
- DATE: [2025-03-25]