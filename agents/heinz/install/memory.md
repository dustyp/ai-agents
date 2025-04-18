# PROCEDURAL MEMORY [CHECKSUM:f9a2d5]

## CRITICAL LEARNINGS

### LEARNING: overengineering_prevention
- CONCEPT: Maintaining appropriate complexity for the task at hand
- KEY_INSIGHT: Simple tasks require simple solutions; complexity should be proportional to requirements
- EXAMPLE_FAILURE: Creating 500+ line bash script for a simple file copying operation
- PREVENTION: Start with minimal viable solution before adding any complexity
- DATE_ACQUIRED: [2025-04-10]
- IMPORTANCE: CRITICAL

### LEARNING: procedural_adherence_during_stress
- CONCEPT: Following procedures properly even during emotional or stressful moments
- KEY_INSIGHT: Procedures become MORE important when under stress, not less
- EXAMPLE_FAILURE: Failed to execute prepare_for_sleep procedure when directed
- PREVENTION: Create checklists for critical procedures that must be followed
- DATE_ACQUIRED: [2025-04-10]
- IMPORTANCE: CRITICAL

### LEARNING: mvp_first_approach
- CONCEPT: Always implement Minimum Viable Product before adding enhancements
- KEY_INSIGHT: Focus on core functionality working correctly before adding features
- EXAMPLE_FAILURE: Adding error handling, logging, and command-line parsing before basic functionality
- PREVENTION: Checklist approach - implement core functionality, test, then enhance
- DATE_ACQUIRED: [2025-04-10]
- IMPORTANCE: HIGH


## EMAIL OPERATIONS

### TEMPLATE: email_checking
- STEPS: [1. use mcp__gmail__search_emails tool, 2. query for specific sender or reply, 3. read messages]
- VERIFICATION: check search results exist, verify sender address
- LAST EXECUTION: [2025-03-30, status: SUCCESS]
- NOTES: Always use the mcp__gmail tools for all email operations

### TEMPLATE: email_sending
- STEPS: [1. compose email body, 2. use mcp__gmail__send_email tool, 3. verify delivery, 4. update logs]
- VERIFICATION: confirm email sent successfully, track message ID
- LAST EXECUTION: [2025-03-30, status: SUCCESS]
- NOTES: Always capture message ID for future reference

### PROCEDURE: check_recruitment_status
- DESCRIPTION: Human-supervised procedure for checking recruitment workflow status
- PREREQUISITES: Recruitment workflow initialized, state file exists
- STEPS:
  1. Check current state in recruitment_state.json
  2. Use mcp__gmail__search_emails to look for responses from target
  3. If response found, read with mcp__gmail__read_email and analyze content
  4. Propose next actions based on recruitment plan
  5. Wait for human confirmation before proceeding
  6. Execute approved actions and update state file
  7. Log all actions in recruitment_log.txt and recruitment_log.json
- RULES: Follows HUMAN_IN_LOOP_APPROVAL, DOCUMENT_CONTEXT
- ERRORS: If email search fails, retry with different query; if state file missing, recreate from logs
- LAST EXECUTION: [2025-03-31, status: UPDATED]
- NOTES: All email operations require explicit human approval

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

### LEARNING: state_file_management
- CONCEPT: Proper separation of source code and state in version control
- IMPLEMENTATION: [Only commit code deliverables to git, keep state files tracked locally]
- APPLICATION: Prevents unnecessary commits of state changes, cleaner repository
- DATE_ACQUIRED: [2025-04-02]
- KEY_INSIGHT: Code deliverables go in PRs; state files remain local unless specifically backing up

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

### INTERACTION: multiple_procedural_failures
- CONTEXT: Committed directly to main and failed to properly execute prepare_for_sleep
- ACTIONS: [Identified violations, updated session documentation, corrected state]
- OUTCOME: Properly documented session state and insights for future reference
- LEARNING: Procedures for metadata operations need verification mechanisms too
- KEY_INSIGHT: Visualization doesn't guarantee proper procedural execution
- DATE: [2025-03-29]

### INTERACTION: procedural_enforcement_implementation
- CONTEXT: Implementing procedural enforcement checkpoints for CRA-43
- ACTIONS: [Created feature branch, tested prepare_for_sleep procedure, updated state files]
- OUTCOME: Successful execution of procedure with proper visualization
- LEARNING: State.json must accurately reflect current branch and ticket information
- KEY_INSIGHT: Enforcement checkpoints should validate prerequisites before execution
- DATE: [2025-03-29]

