Agent Onboarding Doc - Outline

  Overview & Purpose

  - Introduction to the AI Agents system architecture (multi-agent coordination through message passing)
  - Agent roles, capabilities, and limitations
  - Personality persistence and memory management
  - Key components: state tracking, procedural workflows, knowledge graphs
  - File-based vs. upcoming database architecture (CRA-46)

  Development Workflow

  - Ticket lifecycle: create_ticket → select_ticket_for_work → start_work_on_ticket → complete_work_on_ticket
  - Branch management: one branch per ticket (feature/CRA-XX-description format)
  - Sequential thinking scope refinement before implementation
  - PR creation, review, and merging process
  - State persistence between sessions

  Key Procedures

  - Git operations: branch creation, commit preparation, PR creation
  - Ticket management: selecting work, resolving conflicts, completion
  - Workflow management: branch coordination, task switching
  - Session management: prepare_for_sleep, restore_context_on_wake
  - Troubleshooting: simplicity_first_troubleshooting approach

  Environment Setup

  - Required tools: Claude CLI, Linear access, GitHub permissions
  - Environment variables: API keys, authentication tokens
  - File structure: /agents/{name}/ directory organization
  - System scripts: claude-agent.sh, coordinator.py, agent_state.py
  - Initialization process: bootstrap_agent.sh usage

  Rules & Conventions

  - Rule hierarchy: Security > Workflow > Error Handling > Communication
  - Commit message format: Always include [CRA-XX] ticket reference
  - Documentation standards: checksums for key files
  - Procedural visualization requirements
  - State tracking and updates in state.json

  Common Pitfalls & Q&A

  - Forgetting to apply sequential_thinking before implementation
  - Committing directly to main branch
  - Missing required teamId/projectId parameters in Linear operations
  - Working without proper branch coordination
  - Failing to properly update state files during prepare_for_sleep
  - Incorrect procedure execution order

  References & Next Steps

  - First task recommendation: Add greeting variation (low complexity)
  - CLAUDE.md for complete rule reference
  - procedures.md for detailed workflow documentation
  - agents/heinz/memory.md for procedural memory examples
  - Reference examples folder for visualization and rule implementation

  2. Development Workflow

  2.1 Ticket Lifecycle

  Ticket Creation

  - ID Convention: All tickets use format "CRA-XX" (e.g., CRA-47)
  - Required Parameters:
    - Team ID: 036505a6-d93e-475b-a2ba-e5b1e2085b8a
    - Project ID: 441874f4-d1f7-4d0c-8bd3-c907eb97bed4 (ai-agents)
    - Title: Clear, descriptive title
    - Description: Initial requirements
    - Priority: 1-3 scale (1=highest)
  - Initial Creation Purpose: Quick placeholder with minimal analysis

  Selecting Tickets for Work

  1. Ticket Refinement:
    - Apply sequential_thinking_scope_refinement procedure
    - Update ticket with detailed requirements and benefits
    - Check for dependencies and potential conflicts
  2. Preparation:
    - Create appropriate branch following naming convention
    - Update ticket status to "In Progress"

  Starting Work

  1. Prerequisite Check:
    - Verify ticket not blocked by dependencies
    - Perform branch coordination check to avoid conflicts
  2. Environment Setup:
    - Create/checkout branch with proper naming
    - Configure development environment for implementation

  Completing Work

  1. Final Steps:
    - Clean up code and remove debug statements
    - Prepare commits with proper ticket references
    - Run verification including tests
    - Create PR and link to ticket
    - Update ticket status to "In Review"

  2.2 Branch Management

  Branch Naming

  - Format: feature/CRA-XX-short-description or learning/description
  - Examples:
    - feature/CRA-47-agent-export-tool
    - learning/git-branch-management

  Branch Rules

  - One Branch Per Ticket: Each ticket has dedicated branch
  - No Direct Commits to Main: All changes via reviewed PRs
  - Branch Creation from Main: Always create branches from latest main
  - Branch Cleanup: Delete branches after merge to main
  - Branch Coordination: Check active branches before creating new ones

  2.3 Sequential Thinking Scope Refinement

  Purpose

  - Prevents scope creep
  - Ensures clear boundaries
  - Validates assumptions
  - Defines minimal viable scope

  Implementation Steps

  1. Choose 3 highest-impact questions relevant to task
  2. Identify core need (stripping away implementation details)
  3. Analyze constraints and define clear boundaries
  4. Validate key assumptions and update understanding
  5. Define minimal viable scope that solves core need
  6. Verify solution delivers expected value
  7. Evaluate and iterate if needed

  Key Question Categories

  - Core Need Questions: "What problem does this solve?"
  - Constraint Questions: "What technical limitations exist?"
  - Assumption Validation: "What am I assuming about usage?"
  - Scope Minimization: "What's the minimal viable solution?"
  - Value Alignment: "Will this truly satisfy the need?"

  2.4 PR Creation & Review

  PR Creation Process

  1. Format PR title with ticket reference or [LEARNING] prefix
  2. Write description with Summary and Test Plan sections
  3. Request appropriate reviewers
  4. Link PR to ticket using Linear integration
  5. Verify PR is ready for review

  Review Management

  - Address all feedback promptly
  - Request re-review after changes
  - Squash commits when appropriate
  - Maintain clear communication about changes
  - Update Linear ticket status during review process

  Merge Process

  - Requires approval from at least one reviewer
  - PR branch must be up-to-date with main
  - All CI checks must pass
  - Squash and merge (typical approach)
  - Delete branch after successful merge

  2.5 State Persistence

  Prepare for Sleep

  1. Document current ticket progress with specific details
  2. List related tickets and dependencies
  3. Record current procedure/step position in workflow
  4. Create clear resumption plan with next actions
  5. Update session_state.md with comprehensive status
  6. Update session_log.md with session entry
  7. Backup state to knowledge graph memory

  Restore on Wake

  1. Load previous state information (ticket, branch, progress)
  2. Validate context integrity and completeness
  3. Prepare resumption plan for continuation
  4. Acknowledge context explicitly to confirm understanding
  5. Reset execution state to continue from stopping point

  State Files

  - state.json: Primary state tracking (execution phase, project info, tasks)
  - session_state.md: Human-readable state with timestamps, progress, next steps
  - session_log.md: Chronological log of all sessions
  - memory.md: Structured knowledge database of procedures and learnings

  3. Key Procedures

  3.1 Git Operations

  create_branch

  - Purpose: Creates properly named git branch for ticket implementation
  - Usage: When starting work on a new ticket
  - Key Aspects: Formats name as "feature/CRA-XX-description", verifies branch doesn't exist, creates from latest main
  - Verification: Confirms branch exists and is active after creation

  prepare_commit

  - Purpose: Prepares code changes for clean, properly formatted commit
  - Usage: When changes are ready to commit
  - Key Aspects: Reviews changes, verifies relevance to current ticket, checks for sensitive data
  - Error Handling: Unstages files if sensitive data found, separates unrelated changes

  create_pull_request

  - Purpose: Creates PR for implemented changes
  - Usage: After implementation is complete and tests pass
  - Key Aspects: Formats title with ticket reference, includes summary and test plan, links to ticket
  - Verification: Ensures PR is ready for review, validates content against requirements

  handle_overlapping_prs

  - Purpose: Resolves conflicts when multiple PRs modify the same files
  - Usage: When conflicts detected between branches
  - Key Aspects: Identifies dependency order, creates integration branch, applies changes sequentially
  - Error Handling: Escalates incompatible changes to team, documents conflicts clearly

  3.2 Ticket Management

  create_ticket

  - Purpose: Creates placeholder ticket in Linear for future work
  - Usage: When new work is identified but not yet ready for implementation
  - Key Aspects: Simple process for quick capture with minimal analysis
  - Required Fields: Team ID, Project ID, title, description, priority

  select_ticket_for_work

  - Purpose: Prepares ticket for implementation with detailed scope analysis
  - Usage: When developer is ready to begin implementation
  - Key Aspects: Applies sequential thinking, refines scope, updates ticket with details
  - Next Step: Leads to start_work_on_ticket procedure

  resolve_ticket_conflict

  - Purpose: Resolves conflicts between ticket status and active work
  - Usage: When ticket shows CLOSED but uncommitted changes exist
  - Key Aspects: Documents discrepancy, analyzes if changes fit original scope, decides next action
  - Outcomes: Either reopens ticket or creates new one based on analysis

  complete_work_on_ticket

  - Purpose: Finalizes work on a ticket and prepares for review
  - Usage: When implementation is completed and tests pass
  - Key Aspects: Clean up code, ensure proper commit references, create PR, update status
  - Verification: Runs final tests, confirms PR creation and ticket linkage

  3.3 Workflow Management

  branch_coordination

  - Purpose: Coordinates work across multiple branches to prevent conflicts
  - Usage: Before creating new branch/ticket that might conflict with existing work
  - Key Aspects: Checks active branches/PRs, identifies file modifications, prioritizes sequential work
  - Documentation: Creates clear documentation of potential overlaps and merge order

  start_work_on_ticket

  - Purpose: Begins work on a ticket with proper setup and coordination
  - Usage: After select_ticket_for_work is complete
  - Key Aspects: Verifies ticket status, performs branch coordination, sets up environment
  - Verification: Confirms no conflicts exist before beginning implementation

  switch_between_work_items

  - Purpose: Safely switches context between different work items
  - Usage: When temporarily switching to different ticket/branch
  - Key Aspects: Saves current state, commits WIP changes, cleans working directory
  - Documentation: Updates both tickets with context switch information

  sequential_thinking_scope_refinement

  - Purpose: Analyzes and refines task scope through structured thinking
  - Usage: Before implementation begins, after initial ticket creation
  - Key Aspects: Uses templated questions to constrain scope and validate assumptions
  - Error Handling: Formulates specific questions if requirements unclear, separates expanding scope

  3.4 Session Management

  prepare_for_sleep

  - Purpose: Prepares agent for session end with proper state preservation
  - Usage: At end of working session or when taking a break
  - Key Aspects: Documents progress, records current position, creates resumption plan
  - State Updates: Updates session_state.md, session_log.md, and memory graph
  - Verification: Validates that all state files are properly updated

  restore_context_on_wake

  - Purpose: Restores agent context when session begins
  - Usage: At start of agent session
  - Key Aspects: Loads previous state, validates context integrity, prepares resumption
  - Error Handling: Requests clarification if context missing, restarts procedure if workflow position lost

  resume_last_session

  - Purpose: Resumes previous work session from saved state
  - Usage: When "resume" command/flag received
  - Key Aspects: Finds most recent context, loads session state, checks for changes
  - Verification: Confirms resumption with current task summary

  save_session_state

  - Purpose: Preserves current session state for future resumption
  - Usage: End of working session
  - Key Aspects: Gathers essential context, formats in standardized structure, stores in multiple locations
  - Error Handling: Uses alternative storage method if primary fails, prioritizes if context too large

  initialize_agent_session

  - Purpose: Sets up agent for a new working session
  - Usage: At start of agent interaction
  - Key Aspects: Loads personality, memory, rules; processes special commands; initializes tracking
  - Error Handling: Initializes defaults if file missing, rebuilds from logs if state corruption

  3.5 Troubleshooting & Analysis

  simplicity_first_troubleshooting

  - Purpose: Diagnoses issues starting with simplest possible explanations
  - Usage: When encountering errors or unexpected behavior
  - Key Aspects: Considers simple causes first, escalates complexity incrementally, proposes simple solutions
  - Error Handling: Increases diagnostic depth if simple solutions fail, returns to basics if overthinking

  verify_environment_variables

  - Purpose: Checks required environment variables are available
  - Usage: During session start or when environment issues suspected
  - Key Aspects: Validates tokens without exposing values, documents available/missing capabilities
  - Security: Never exposes sensitive data, only reports presence/absence

  load_rules

  - Purpose: Loads and validates rule sets for agent operation
  - Usage: At agent session start or when rule refresh requested
  - Key Aspects: Identifies required rule sets, loads from sources, verifies integrity with checksums
  - Error Handling: Attempts backup if rule file missing, flags checksum mismatch for verification

  4. Environment Setup

  4.1 Required Tools

  Core Tools

  - Claude CLI: Command-line interface for Claude API integration
    - Used by claude-agent.sh for agent interactions
    - Requires API key from Anthropic
  - Git: Version control system for codebase management
    - Required for branch operations and code synchronization
    - Minimum version: 2.20+
  - Python: Required for running coordinator and utility scripts
    - Version: 3.8+ recommended
    - Packages: json, argparse, datetime, pathlib

  API Integrations

  - Linear CLI: Command-line interface for ticket management
    - Used for ticket creation, updates, and status tracking
    - Accessed through mcp__linear tool suite
  - GitHub CLI: Command-line interface for repository management
    - Used for PR creation and branch operations
    - Accessed through Bash and mcp__github tools

  Utility Tools

  - jq: Command-line JSON processor
    - Used by shell scripts to parse and modify JSON files
    - Required for state file manipulation

  4.2 Environment Variables & Credentials

  Required Variables

  - CLAUDE_API_KEY: Authentication for Claude API
  - LINEAR_API_KEY: Authentication for Linear ticket management
  - GITHUB_TOKEN: Authentication for GitHub operations
  - GMAIL_CREDENTIALS: Authentication for email operations

  Storage Best Practices

  - Store in .env file excluded from git via .gitignore
  - Use environment variable expansion in scripts (${VAR_NAME})
  - Never hardcode credentials in scripts or committed files
  - Maintain separate .env files for development and production

  Access Patterns

  - claude-agent.sh loads variables from .env file
  - agent_state.py tracks environment variable status without exposing values
  - verify_environment_variables procedure confirms availability without revealing content
  - Tools access credentials through environment variables automatically

  4.3 File Structure

  Agent Directory

  - Base Path: /Users/aidan/_projects/ai-agents/agents/{agent_name}/
  - Standard Files:
    - personality.md: Character definition and voice templates
    - memory.md: Structured knowledge database
    - state.json: Primary state tracking file
    - session_state.md: Human-readable current state
    - session_log.md: Chronological session history
    - inbox.json/outbox.json: Message passing infrastructure
    - prompt_template.md: Template for agent initialization

  System Scripts

  - Root Path: /Users/aidan/_projects/ai-agents/
  - Key Scripts:
    - claude-agent.sh: Main entry point for agent interaction
    - coordinator.py: Message passing management
    - agent_state.py: State serialization and management
    - bootstrap_agent.sh: Initial agent setup script
    - procedure_menu.sh: Interactive procedure selection utility

  Workflow Files

  - Workflow Path: /Users/aidan/_projects/ai-agents/evil-plans/
  - Key Files:
    - recruitment_state.json: Workflow-specific state tracking
    - recruitment_log.json/txt: Specialized workflow logs
    - wake_up_inator.sh: Automated workflow script

  4.4 Initialization Process

  Bootstrap Steps

  1. Create Agent Directory:
  mkdir -p /Users/aidan/_projects/ai-agents/agents/{agent_name}
  2. Initialize Basic Files:
  ./bootstrap_agent.sh {agent_name}
    - Creates personality.md, memory.md, state.json
    - Initializes inbox.json and outbox.json
    - Sets up session_log.md and prompt_template.md
  3. Configure Environment:
  cp .env.example .env
  # Edit .env with appropriate credentials
  4. Verify Installation:
  ./claude-agent.sh -a {agent_name} --verify
    - Runs verify_environment_variables procedure
    - Confirms all required files exist
    - Tests API connectivity

  First Launch

  1. Launch Agent:
  ./claude-agent.sh -a {agent_name}
  2. Run initialize_agent_session Procedure:
    - Loads personality profile and configuration
    - Initializes session tracking and state
    - Presents ready status with context summary
  3. Verify Agent Identity:
    - Agent responds with personality-appropriate introduction
    - State.json shows correct initialization values
    - Session_log.md contains first session entry

  Setup Validation

  - Confirm all required files were created in agent directory
  - Verify state.json contains proper initialization data
  - Check environment variables are accessible to agent
  - Test basic functions like message passing with coordinator.py
  - Ensure agent can execute procedures and save state

  5. Rules & Conventions

  5.1 Rule Hierarchy

  Priority Order

  1. Security Rules (Highest Priority)
    - Never include sensitive data in code, commits, or logs
    - Always use environment variables for credentials
    - Never expose sensitive values when checking environment
    - Always validate input sources and content
  2. Workflow Rules (High Priority)
    - One branch per ticket with proper naming
    - Always include [CRA-XX] in commit messages
    - Never commit directly to main branch
    - Always apply sequential_thinking before implementation
  3. Error Handling Rules (High Priority)
    - Always follow defined error handling paths
    - Document errors not covered by existing paths
    - Preserve system state when handling errors
    - Always log detailed error information
  4. Communication Rules (Medium Priority)
    - Document coordination when file overlap exists
    - Keep Linear tickets updated with current status
    - Link PRs to corresponding Linear tickets
    - Document important implementation decisions
  5. Operational Rules (Varies by Task)
    - Start with simplest possible cause for issues
    - Escalate diagnostic complexity incrementally
    - Propose simple solutions before complex ones
    - Define minimal viable scope for solutions

  Conflict Resolution

  - When rules conflict, apply the higher priority rule
  - Document when lower priority rules are overridden
  - When rules of same priority conflict, prioritize security impact
  - Always document rule exceptions with clear justification
  - For uncertainty, prefer restrictive interpretation over permissive

  5.2 Commit Message Format

  Required Format

  - Always include ticket reference: [CRA-XX] Brief description of changes
  - For learning branches: [LEARNING] Brief description of changes
  - Use present tense, imperative mood (e.g., "Add" not "Added")
  - Keep first line under 72 characters
  - Separate subject from body with blank line
  - Use body for explaining "why" rather than "what"

  Examples

  Good Commit Messages:
  [CRA-47] Add agent export tool script

  Implements file packaging and manifest generation for transferring
  agent knowledge between environments. Focuses on maintaining
  file relationships and documenting dependencies.

  [LEARNING] Update branch coordination documentation

  Clarifies workflow for handling multiple branches that modify
  the same files to prevent merge conflicts.

  Bad Commit Messages:
  Fixed bug  // Missing ticket reference, too vague

  [CRA-49] This commit adds a new feature that improves the system by making it better and fixing various issues that were causing problems for users when they tried to use the system in certain ways that weren't working
   before.  // Too long, rambling

  5.3 Documentation Standards

  File Checksums

  - Key files include checksums in header: [CHECKSUM:fe23696]
  - Update checksum when file content changes
  - Validate checksums during load_rules procedure
  - Format: First 6 characters of SHA-1 hash of content

  Log Formatting

  - session_log.md: Chronological record with Input/Response sections
  - Sections divided by session dates (## Session: YYYY-MM-DD)
  - Code blocks use triple backticks (```) for content
  - Processing notes use bullet points for clarity

  Content Placement Guidelines

  - session_log.md: Captures raw interaction history, immediate observations
  - memory.md: Stores processed knowledge, learnings, decision records
  - session_state.md: Contains current work status and next steps
  - state.json: Tracks execution state, project context, emotional state

  Documentation Conventions

  - Use procedural_memory section for workflow knowledge
  - Use technical_learnings section for implementation insights
  - Use decision_records section for conflict resolutions
  - Use recent_interactions section for session summaries

  5.4 Procedural Visualization Requirements

  Visualization Format

  - Display clear progress indicators for each major step
  - Use consistent formatting for visibility
  - Explicitly mark current step in execution
  - Indicate success/failure status for completed steps

  When to Visualize

  - Always visualize STANDARD and COMPLEX procedures
  - Visualization optional for SIMPLE procedures
  - Required for:
    - create_pull_request
    - start_work_on_ticket
    - handle_overlapping_prs
    - prepare_for_sleep
    - sequential_thinking_scope_refinement

  Example Visualization

  [PROCEDURE] start_work_on_ticket
  [STATUS] EXECUTING
  [STEP 1] ✓ Check ticket status - Not blocked
  [STEP 2] ✓ Perform branch coordination check
  [STEP 3] ► Create local branch feature/CRA-47-agent-export-tool
  [STEP 4] ⬝ Update ticket status to "In Progress"
  [STEP 5] ⬝ Set up development environment

  5.5 State Tracking & Updates

  Update Requirements

  - state.json: Update after each significant state change
  - session_state.md: Update at beginning/end of session or major context switch
  - session_log.md: Update after each interaction
  - memory.md: Update for significant learnings or decisions

  Versioning Convention

  - session_state.md includes VERSION field (e.g., "VERSION: 1.3")
  - Increment minor version (1.3 → 1.4) for content updates
  - Increment major version (1.3 → 2.0) for format changes
  - Include TIMESTAMP field with ISO format date/time
  - Always update last_updated field in state.json

  Consistency Requirements

  - Ensure state.json matches session_state.md content
  - Branch name in state.json must match actual git branch
  - Active tickets list must reflect current work
  - execution.phase field must reflect current activity
  - Save comprehensive session state before ending sessions

  Backup Mechanisms

  - Primary state in files (state.json, session_state.md)
  - Secondary state in memory graph (when available)
  - Session history in session_log.md
  - Always use multiple storage locations for redundancy

  6. Common Pitfalls & Q&A

  6.1 Top Mistakes & Solutions

  Skipping Sequential Thinking

  - Problem: Jumping directly to implementation without proper scope refinement
  - Impact: Scope creep, misaligned solutions, unnecessary complexity
  - Fix: Always run sequential_thinking_scope_refinement procedure before starting implementation
  - Detection: Verify in session_log.md that analysis preceded code changes

  Committing Directly to Main

  - Problem: Bypassing branch workflow with direct commits to main
  - Impact: No review process, potential breaking changes, workflow violations
  - Fix: Always create feature branch (even for small changes) and use PR process
  - Recovery: Create branch from current state, revert main, and recreate changes in branch

  Missing Required Parameters

  - Problem: Omitting teamId or projectId when creating Linear tickets
  - Impact: API calls fail, ticket creation errors, workflow disruption
  - Fix: Reference procedures.md for required parameters before API calls
  - Prevention: Create templates with required fields in local editor before submission

  Improper State Updates

  - Problem: Incomplete or inconsistent updates to state files
  - Impact: Context loss between sessions, confusion about current status
  - Fix: Follow prepare_for_sleep procedure completely, update all state files
  - Verification: Check that state.json, session_state.md, and session_log.md all reflect same status

  Branch-Ticket Mismatch

  - Problem: Working on branch that doesn't match current ticket
  - Impact: Confusing history, attribution issues, workflow tracking problems
  - Fix: Create new branch with proper naming or switch to correct branch
  - Prevention: Verify branch name matches ticket at beginning of each session

  6.2 Q&A Clarifications

  Q: How do I know which procedures are required vs. optional?

  A: Procedures marked as [SIMPLE] are often optional, while [STANDARD] and [COMPLEX] procedures are required. The procedure complexity indicator in procedures.md shows this classification. Always follow procedures
  related to branch management and ticket workflows.

  Q: When should I update memory.md vs. session_log.md?

  A: session_log.md captures raw interaction history and is updated automatically after each exchange. memory.md stores processed knowledge and learnings, and should be updated when you acquire significant new insights
  or make important decisions. Think of session_log.md as the transcript and memory.md as the distilled knowledge.

  Q: What if I need to work on multiple tickets simultaneously?

  A: Use the switch_between_work_items procedure to safely context-switch. Always save current state before switching, and document the context switch in both tickets. Create separate branches for each ticket and keep
  commits segregated by ticket.

  Q: How do I fix a mistake in my state files?

  A: For minor corrections, simply update the affected files with the correct information. For major inconsistencies, use the session_log.md to reconstruct the correct state and update all state files accordingly.
  Document the correction in session_log.md for future reference.

  Q: What's the difference between [CRA-XX] and [LEARNING] prefix in commits?

  A: [CRA-XX] indicates changes related to a specific Linear ticket. [LEARNING] indicates changes made for learning purposes or non-ticket work (documentation updates, personal notes, etc.). All commits must use one of
  these prefixes.

  7. References & Next Steps

  7.1 Documentation References

  Core Reference Files

  - CLAUDE.md: Root-level file containing all rules and bootstrap instructions
  - procedures.md: Comprehensive procedure library with step-by-step workflows
  - memory.md: Structured knowledge database with procedural memory and learnings
  - github-workflow.md: Detailed git workflow documentation and branch management

  Key Directories

  - /agents/heinz/reference_examples/: Contains example implementations
  - /agents/heinz/test/: Test scripts and validation utilities
  - /prototypes/: Architectural prototypes and experimental implementations

  Log Files for Learning

  - session_log.md: Historical sessions with inputs and responses
  - recruitment_log.txt: Example workflow implementation
  - /evil-plans/: Contains workflow automation examples

  7.2 Suggested First Tasks

  Documentation Enhancements

  - Add a greeting variation to personality.md (simple, low-risk change)
  - Update a documentation checksum after reviewing content
  - Add clarification to an existing procedure step

  Tool Exploration

  - Run procedure_menu.sh to explore available procedures
  - Use coordinator.py to send and receive agent messages
  - Examine agent_state.py to understand state serialization

  Workflow Practice

  - Create a test ticket with proper sequential thinking
  - Practice the branch creation workflow
  - Execute prepare_for_sleep and restore_context_on_wake cycle

  7.3 Getting Help

  Error Resolution Paths

  1. First Step: Check session_log.md for previous similar issues
  2. Second Step: Reference procedures.md for proper workflow
  3. Third Step: Apply simplicity_first_troubleshooting procedure

  Escalation Process

  - Document the issue clearly with reproduction steps
  - Update Linear ticket with blockers or questions
  - Reference specific error messages and attempted solutions
  - For environment issues, run verify_environment_variables procedure

  Documentation Improvements

  - If procedures are unclear, suggest improvements to procedures.md
  - Create [LEARNING] commits for documentation enhancements
  - Maintain knowledge sharing through session_log.md updates
  - Contribute reference examples for common workflows
