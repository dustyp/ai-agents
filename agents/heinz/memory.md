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

### TEMPLATE: git_branch_cleanup
- STEPS: [1. analyze branches, 2. identify merged branches, 3. delete local, 4. delete remote]
- VERIFICATION: branches removed both locally and remotely
- LAST EXECUTION: [2025-03-26, status: SUCCESS]
- NOTES: Use git branch -d for merged, git branch -D for unmerged but obsolete

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

### DECISION_RECORD: branch_cleanup
- SCENARIO: Multiple stale branches creating confusion in repository
- RESOLUTION: Analyzed and deleted all branches with work in main or superseded
- EXECUTION_PATH: [analyze_branches, identify_merged, remove_superseded, document_actions]
- OUTCOME: Clean repository with only main branch remaining
- DATE: [2025-03-26]

## PROJECT KNOWLEDGE

### PROJECT: ai-agents
- PURPOSE: Multi-agent architecture for AI assistants
- KEY_COMPONENTS: [coordinator.py, bootstrap_agent.sh, claude-agent.sh, agent_state.py]
- PROJECT_ID: 441874f4-d1f7-4d0c-8bd3-c907eb97bed4
- ACTIVE_TICKETS: [CRA-23, CRA-24, CRA-25, CRA-27, CRA-28, CRA-29, CRA-30, CRA-31, CRA-32, CRA-33, CRA-36, CRA-37]
- CLOSED_TICKETS: [CRA-14, CRA-19, CRA-20, CRA-21, CRA-22, CRA-26, CRA-34, CRA-35]
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

### LEARNING: git_branch_management
- CONCEPT: Structured approach to managing git branches
- IMPLEMENTATION: [Analysis, categorization, and cleanup process]
- APPLICATION: Repository organization and maintenance
- DATE_ACQUIRED: [2025-03-26]
- KEY_INSIGHT: Regular branch cleanup prevents repository bloat and confusion

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

### INTERACTION: context_persistence_implementation
- CONTEXT: Implementing agent context persistence across sessions
- ACTIONS: [Created standardized procedures for saving/restoring context, updated session_state.md format]
- OUTCOME: Successful implementation of context persistence mechanism
- DATE: [2025-03-26]

### INTERACTION: git_branch_cleanup
- CONTEXT: Repository organization and branch cleanup
- ACTIONS: [Analyzed branch status, deleted merged/superseded branches, documented process]
- OUTCOME: Clean repository with only main branch remaining
- LEARNING: Importance of regular branch maintenance and proper branch naming
- DATE: [2025-03-26]

### INTERACTION: repository_structure_analysis
- CONTEXT: Understanding git branch relationships and PR workflow
- ACTIONS: [Analyzed commit history, tracked branch relationships, identified merge patterns]
- OUTCOME: Clear understanding of PR workflow and branch management needs
- LEARNING: Branch divergence can cause confusion without proper tracking
- DATE: [2025-03-26]

### INTERACTION: procedure_visualization_implementation
- CONTEXT: Adding visual indicators to procedure execution
- ACTIONS: [Added visualization examples to 7 key procedures, updated documentation]
- OUTCOME: Standardized visualization format for procedure execution
- LEARNING: Visual progress indicators improve procedure execution clarity
- DATE: [2025-03-29]

### INTERACTION: procedural_violation_detection
- CONTEXT: Attempted implementation of testing harness without proper scope refinement
- ACTIONS: [Created testing framework, identified procedural violation, canceled ticket]
- OUTCOME: Canceled PR #12, created new ticket for procedural compliance enforcement
- LEARNING: Procedural definition is insufficient without enforcement mechanisms
- KEY_INSIGHT: Start-of-task validation needed to prevent procedural violations
- DATE: [2025-03-29]

