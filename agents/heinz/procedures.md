# PROCEDURES LIBRARY [CHECKSUM:d7e5f3]

## PROCEDURE MENU

### Git Operations
- [create_branch](#create_branch) [SIMPLE]
- [prepare_commit](#prepare_commit) [SIMPLE]
- [create_pull_request](#create_pull_request) [STANDARD]
- [handle_overlapping_prs](#handle_overlapping_prs) [COMPLEX]
- [setup_worktree_for_ticket](#setup_worktree_for_ticket) [STANDARD]
- [cleanup_worktree_for_ticket](#cleanup_worktree_for_ticket) [STANDARD]
- [setup_shared_venv](#setup_shared_venv) [SIMPLE]

### Ticket Management
- [create_ticket](#create_ticket) [SIMPLE]
- [select_ticket_for_work](#select_ticket_for_work) [STANDARD]
- [resolve_ticket_conflict](#resolve_ticket_conflict) [STANDARD]
- [complete_work_on_ticket](#complete_work_on_ticket) [STANDARD]

### Workflow Management
- [branch_coordination](#branch_coordination) [COMPLEX]
- [start_work_on_ticket](#start_work_on_ticket) [STANDARD]
- [switch_between_work_items](#switch_between_work_items) [STANDARD]
- [sequential_thinking_scope_refinement](#sequential_thinking_scope_refinement) [COMPLEX]

### Session Management
- [prepare_for_sleep](#prepare_for_sleep) [STANDARD]
- [restore_context_on_wake](#restore_context_on_wake) [SIMPLE]
- [resume_last_session](#resume_last_session) [SIMPLE]
- [save_session_state](#save_session_state) [STANDARD]
- [initialize_agent_session](#initialize_agent_session) [SIMPLE]

### Troubleshooting & Analysis
- [simplicity_first_troubleshooting](#simplicity_first_troubleshooting) [STANDARD]
- [verify_environment_variables](#verify_environment_variables) [SIMPLE]
- [load_rules](#load_rules) [STANDARD]

## COMMON WORKFLOWS

### Ticket Creation and Implementation Workflow
This workflow clarifies the relationship between ticket-related procedures:

1. **Initial Capture**: Use [create_ticket](#create_ticket) to create a placeholder ticket with basic information (title, brief description, priority)

2. **Scope Analysis**: When ready to begin work, use [select_ticket_for_work](#select_ticket_for_work) to perform detailed scope refinement using sequential thinking

3. **Implementation Setup**: After scope is defined, use [start_work_on_ticket](#start_work_on_ticket) to set up the proper branch and development environment
   - **Alternative**: Use [setup_worktree_for_ticket](#setup_worktree_for_ticket) to create a separate worktree for parallel development

4. **Development**: Work on implementation until complete
   - If needed, use [switch_between_work_items](#switch_between_work_items) to move between active tickets/branches

5. **Completion**: Use [complete_work_on_ticket](#complete_work_on_ticket) to finalize work and create PR
   - If using worktrees, also use [cleanup_worktree_for_ticket](#cleanup_worktree_for_ticket) to remove the worktree

Each procedure has a specific purpose in the ticket lifecycle:
- `create_ticket`: Quick placeholder creation (minimal analysis)
- `select_ticket_for_work`: Detailed scope analysis and refinement
- `start_work_on_ticket`: Branch coordination and development setup
- `setup_worktree_for_ticket`: Create separate working directory for parallel development
- `complete_work_on_ticket`: Work finalization and PR creation
- `cleanup_worktree_for_ticket`: Remove worktree after ticket completion

### Git Worktree Workflow
This workflow enables parallel work on multiple branches using git worktrees:

1. **Setup**: 
   - For each ticket, create a dedicated worktree using [setup_worktree_for_ticket](#setup_worktree_for_ticket)
   - For Python projects, set up a shared virtual environment using [setup_shared_venv](#setup_shared_venv)

2. **Parallel Development**: Work on multiple tickets simultaneously by physically switching directories rather than branches:
   - No need to commit work-in-progress changes when switching context
   - Each branch maintains its own working state
   - Reduced potential for merge conflicts by minimizing branch switching
   - All worktrees can use the same shared Python virtual environment

3. **Cleanup**: When work on a ticket is complete, use [cleanup_worktree_for_ticket](#cleanup_worktree_for_ticket) to remove the worktree

Benefits of this workflow:
- Cleaner commit history (no WIP commits)
- More efficient context switching (no need to stash/commit changes)
- Better isolation between features
- Simpler mental model (physical separation mirrors logical separation)
- Reduced overhead when working on multiple tickets
- Consistent Python environment across all worktrees (with shared venv)

## PROCEDURES

### setup_shared_venv {#setup_shared_venv} [SIMPLE]
**DESCRIPTION**: Sets up a shared Python virtual environment for use across multiple worktrees

**PREREQUISITES**:
- Python 3.x installed
- Project directory exists
- Worktree-inator script available

**STEPS**:
1. Create shared_venv directory in the project root (not in any specific worktree)
2. Create Python virtual environment with `python -m venv shared_venv`
3. Upgrade pip with `shared_venv/bin/pip install --upgrade pip`
4. Install required packages from requirements.txt if available
5. Verify virtual environment is working correctly
6. Update .gitignore to ensure the shared_venv directory is not committed
7. Document venv location and activation instructions for all worktrees

**RULES**: Follows AVOID_SENSITIVE_DATA, NEVER_COMMIT_VENV
**ERRORS**: If Python not installed, prompt for installation; if directory creation fails, check permissions
**RELATED PROCEDURES**: Often used with [setup_worktree_for_ticket](#setup_worktree_for_ticket)
**NOTES**: Using a shared venv reduces duplication and ensures consistent dependencies across all worktrees

### setup_worktree_for_ticket {#setup_worktree_for_ticket} [STANDARD]
**DESCRIPTION**: Creates a new git worktree for a ticket, enabling parallel work across multiple branches

**PREREQUISITES**:
- Ticket exists in Linear with basic information
- Main repository is already cloned
- Git version 2.5 or higher installed

**STEPS**:
1. Verify ticket exists and has proper scope definition
2. Choose appropriate location for the new worktree (within the project's worktrees directory)
3. Format branch name according to convention (feature/CRA-XX-description)
4. Check if branch already exists (local or remote)
5. Create worktree with proper branch using `git worktree add worktrees/CRA-XX branch-name`
6. If branch doesn't exist, create it with `-b` flag: `git worktree add -b branch-name worktrees/CRA-XX`
7. Verify worktree creation was successful with `git worktree list`
8. For Python projects, check if shared venv exists and suggest setup if needed
9. Update ticket status to "In Progress" if needed
10. Record worktree information in session state

**VISUALIZATION**: Display progress through the 10 core steps with visual indicators
**RULES**: Follows ONE_BRANCH_PER_TICKET, BRANCH_NAMING_CONVENTION, DOCUMENT_CONTEXT
**ERRORS**: If worktree creation fails, check permissions and git version; if branch exists but is in wrong state, resolve before proceeding
**NOTES**: Worktrees enable parallel work on multiple branches without context switching overhead

### cleanup_worktree_for_ticket {#cleanup_worktree_for_ticket} [STANDARD]
**DESCRIPTION**: Properly removes a git worktree after work on a ticket is completed

**PREREQUISITES**:
- Work on ticket is completed
- Worktree exists for the ticket
- Changes are committed and pushed
- PR is created (if applicable)

**STEPS**:
1. Verify all changes are committed or intentionally discarded
2. Ensure branch is pushed to remote if needed
3. Navigate out of the worktree directory
4. Use `git worktree list` to confirm the worktree path
5. Remove the worktree using `git worktree remove path/to/worktree`
6. Verify worktree was successfully removed with `git worktree list`
7. Update ticket status to reflect completion
8. Document worktree removal in session state

**VISUALIZATION**: Display progress through the 8 core steps with visual indicators
**RULES**: Follows CLEAN_UP_AFTER_COMPLETION, DOCUMENT_CONTEXT
**ERRORS**: If worktree has uncommitted changes, commit or stash them first; if worktree removal fails, check for processes using files in the worktree
**RELATED PROCEDURES**: Often follows [complete_work_on_ticket](#complete_work_on_ticket)

### create_ticket {#create_ticket} [SIMPLE]
**DESCRIPTION**: Creates a placeholder ticket in Linear for future work

**PREREQUISITES**:
- Team ID: 036505a6-d93e-475b-a2ba-e5b1e2085b8a
- Project ID: 441874f4-d1f7-4d0c-8bd3-c907eb97bed4 (ai-agents)

**STEPS**:
1. Define clear title that describes the task
2. Write brief description with basic requirements
3. Set appropriate priority (1-3)
4. Submit with required parameters (teamId, title, description)
5. Verify ticket creation and ID

**RULES**: Follows DOCUMENT_REQUIREMENTS, IDENTIFY_SCOPE
**ERRORS**: If creation fails, verify parameters and retry

### select_ticket_for_work {#select_ticket_for_work} [STANDARD]
**DESCRIPTION**: Prepares a ticket for implementation with detailed scope analysis

**PREREQUISITES**:
- Ticket exists in Linear with basic information
- Developer ready to begin implementation

**STEPS**:
1. Review ticket description and apply sequential_thinking
2. Refine scope with clear boundaries and constraints
3. Update ticket with detailed requirements and benefits
4. Check for dependencies and potential conflicts
5. Create appropriate branch following naming convention
6. Update ticket status to "In Progress"

**VISUALIZATION**: Show progress through the 6 core steps with visual indicators
**RULES**: Follows CONSTRAIN_SCOPE, DOCUMENT_CONTEXT, ONE_BRANCH_PER_TICKET
**ERRORS**: If scope unclear, conduct additional analysis before proceeding
**NEXT PROCEDURE**: After completing this procedure, use [start_work_on_ticket](#start_work_on_ticket)

### create_branch {#create_branch} [SIMPLE]
**DESCRIPTION**: Creates a properly named git branch for ticket implementation

**PREREQUISITES**:
- Valid ticket exists
- Current branch is up to date

**STEPS**:
1. Format branch name as "feature/CRA-XX-short-description" or "learning/description"
2. Check if branch already exists
3. Create branch from latest main
4. Switch to new branch and verify it's active

**RULES**: Follows BRANCH_NAMING_CONVENTION, ONE_BRANCH_PER_TICKET
**ERRORS**: If branch exists, checkout existing branch; if create fails, check permissions

### prepare_commit {#prepare_commit} [SIMPLE]
**DESCRIPTION**: Prepares code changes for a clean, properly formatted commit

**PREREQUISITES**:
- Changes are ready to commit
- Current branch matches ticket (except for learning branches)

**STEPS**:
1. Review changes with git status and git diff
2. Verify changes are relevant to current ticket/branch
3. Check for sensitive data or debugging code
4. Stage relevant files
5. Create commit message with ticket reference or [LEARNING] prefix

**RULES**: Follows INCLUDE_TICKET_REFERENCE, AVOID_SENSITIVE_DATA
**ERRORS**: If sensitive data found, unstage and fix; if unrelated changes found, separate commits

### create_pull_request {#create_pull_request} [STANDARD]
**DESCRIPTION**: Creates a pull request for implemented changes

**PREREQUISITES**:
- Changes committed to feature branch
- Tests passing locally
- Branch pushed to remote

**STEPS**:
1. Format PR title with ticket reference or [LEARNING] prefix
2. Write description with Summary and Test Plan sections
3. Request appropriate reviewers
4. Link PR to ticket
5. Verify PR is ready for review

**VISUALIZATION**: Display progress through the 5 core steps with visual indicators
**RULES**: Follows INCLUDE_TICKET_REFERENCE, USE_PR_TEMPLATES, LINK_PRS_TO_TICKETS
**ERRORS**: If creation fails, check permissions; if validation fails, update PR content

### handle_overlapping_prs {#handle_overlapping_prs} [COMPLEX]
**DESCRIPTION**: Resolves conflicts when multiple PRs modify the same files

**PREREQUISITES**:
- Multiple PRs exist modifying same files
- PRs are on different branches

**STEPS**:
1. Identify the dependency order between PRs
2. Create an integration branch from main
3. Apply changes sequentially based on dependency order
4. Resolve conflicts at each step
5. Run tests after integrating all changes
6. Create consolidated PR if appropriate

**VISUALIZATION**: Display progress through all steps with visual indicators
**RULES**: Follows SEQUENCE_DEPENDENT_OPERATIONS, ISOLATE_FAILURES
**ERRORS**: If conflicting changes incompatible, escalate to team; if integration fails, document conflicts

### resolve_ticket_conflict {#resolve_ticket_conflict} [STANDARD]
**DESCRIPTION**: Resolves conflicts between ticket status and active work

**PREREQUISITES**:
- Ticket exists
- Ticket status is CLOSED or DONE
- Uncommitted changes exist

**STEPS**:
1. Document discrepancy between ticket status and work
2. Analyze if changes fit original scope
3. Decide whether to reopen ticket or create new one
4. Execute resolution with appropriate branching
5. Migrate changes to correct context

**VISUALIZATION**: Display progress through the 5 core steps with visual indicators
**RULES**: Follows DOCUMENT_COORDINATION_STRATEGY, ONE_BRANCH_PER_TICKET
**ERRORS**: If ticket system error, document locally; if branch conflict, create alternative name

### branch_coordination {#branch_coordination} [COMPLEX]
**DESCRIPTION**: Coordinates work across multiple branches to prevent conflicts

**PREREQUISITES**:
- Multiple developers or work streams
- Potential for parallel work on same files

**STEPS**:
1. Check active branches and PRs before creating a ticket/branch
2. Identify which files are being modified in existing work
3. Prioritize sequential work on same files when possible
4. Create ticket with clear scope boundaries and conflict awareness
5. Document potential file overlap and dependencies
6. Establish clear order for merging dependent branches

**VISUALIZATION**: Display progress through all steps with visual indicators
**RULES**: Follows DOCUMENT_COORDINATION_STRATEGY, PRIORITIZE_SEQUENTIAL_WORK
**ERRORS**: If unavoidable conflict, create coordination plan; if blocked by long-running branch, negotiate

### start_work_on_ticket {#start_work_on_ticket} [STANDARD]
**DESCRIPTION**: Begins work on a ticket with proper setup and coordination

**PREREQUISITES**:
- Ticket exists with refined scope (after select_ticket_for_work)
- Developer prepared to begin implementation

**STEPS**:
1. Check ticket status and verify not blocked by dependencies
2. Perform branch coordination check to avoid conflicts
3. Create local branch with proper naming (if not already created)
4. Update ticket status to "In Progress" (if not already updated)
5. Set up development environment for implementation

**VISUALIZATION**: Display progress through the 5 core steps with visual indicators
**RULES**: Follows ONE_BRANCH_PER_TICKET, CHECK_ACTIVE_BRANCHES
**ERRORS**: If conflicts detected, apply resolution strategy; if prerequisites missing, address first
**PREVIOUS PROCEDURE**: This procedure should be used after [select_ticket_for_work](#select_ticket_for_work)

### switch_between_work_items {#switch_between_work_items} [STANDARD]
**DESCRIPTION**: Safely switches context between different work items

**PREREQUISITES**:
- Currently active work on a branch
- Need to temporarily switch to different ticket/branch

**STEPS**:
1. Save current state with proper documentation
2. Commit work-in-progress changes with [WIP] prefix (traditional approach)
3. Clean working directory and document stopping point
4. Checkout target branch and pull latest changes
5. Update both tickets with context switch information

**ALTERNATIVE STEPS (with worktrees)**:
1. Document current progress in session state
2. Save editor state if relevant (e.g., VS Code workspace)
3. Exit current worktree directory
4. Navigate to target worktree directory (or create using setup_worktree_for_ticket)
5. Update session state to reflect new active ticket

**VISUALIZATION**: Display progress through the core steps with visual indicators
**RULES**: Follows DOCUMENT_CONTEXT, SAVE_WORK_IN_PROGRESS
**ERRORS**: If uncommitted changes, stash or commit WIP; if branch conflicts, resolve before switching
**RELATED PROCEDURES**: For worktree approach, see [setup_worktree_for_ticket](#setup_worktree_for_ticket)

### complete_work_on_ticket {#complete_work_on_ticket} [STANDARD]
**DESCRIPTION**: Finalizes work on a ticket and prepares for review

**PREREQUISITES**:
- Implementation completed
- Local tests passing

**STEPS**:
1. Clean up code and remove debug statements
2. Prepare commits with proper ticket references (only commit code deliverables, not state files)
3. Run final verification including tests
4. Create pull request and link to ticket
5. Update ticket status to "In Review"
6. Update local state files to reflect completion
7. Prepare for next work item

**VISUALIZATION**: Display progress through the 7 core steps with visual indicators
**RULES**: Follows VERIFY_IMPLEMENTATION, LINK_PRS_TO_TICKETS, SEPARATE_CODE_FROM_STATE
**ERRORS**: If tests fail, fix and verify; if PR creation fails, check permissions
**KEY_INSIGHT**: Only commit code deliverables to PRs, keep state files tracked locally

### sequential_thinking_scope_refinement {#sequential_thinking_scope_refinement} [COMPLEX]
**DESCRIPTION**: Analyzes and refines task scope through structured thinking

**PREREQUISITES**:
- Task request received
- Initial understanding of requirements

**STEPS**:
1. Choose 3 highest-impact questions relevant to the task
2. Identify core need by stripping away implementation details
3. Analyze constraints and define clear boundaries
4. Validate key assumptions and update understanding
5. Define minimal viable scope that solves core need
6. Verify solution delivers expected value
7. Evaluate and iterate with additional questions if needed

**VISUALIZATION**: Display progress through all steps with visual indicators
**RULES**: Follows CONSTRAIN_SCOPE, DEFINE_MINIMAL_VIABLE_SCOPE
**ERRORS**: If requirements unclear, formulate specific questions; if scope expanding, separate tickets

### simplicity_first_troubleshooting {#simplicity_first_troubleshooting} [STANDARD]
**DESCRIPTION**: Diagnoses issues starting with simplest possible explanations

**PREREQUISITES**:
- Issue or error encountered
- Multiple possible explanations exist

**STEPS**:
1. Consider the simplest possible causes first
2. Verify environment context (variables, permissions, etc.)
3. Escalate diagnostic complexity incrementally
4. Propose simple solutions before complex ones
5. Verify solution addresses root cause

**VISUALIZATION**: Display progress through the 5 core steps with visual indicators
**RULES**: Follows START_SIMPLE, ESCALATE_INCREMENTALLY
**ERRORS**: If simple solutions fail, increase diagnostic depth; if overthinking, return to basics

### prepare_for_sleep {#prepare_for_sleep} [STANDARD]
**DESCRIPTION**: Prepares agent for session end with proper state preservation

**PREREQUISITES**:
- Session active
- Finished with current work or ready for break

**STEPS**:
1. Document current ticket progress with specific details
2. List all related tickets and dependencies
3. Record current procedure/step position in workflow
4. Create clear resumption plan with next actions
5. Document emotional state for continuity
6. Update session_state.md with comprehensive status
7. Update session_log.md with session entry
8. Backup state to knowledge graph memory

**VISUALIZATION**: Display progress through the 8 core steps with visual indicators
**RULES**: Follows SAVE_SESSION_STATE, DOCUMENT_CONTEXT, VISUALIZE_PROCEDURE_EXECUTION
**ERRORS**: If save fails, retry with different format; if verification fails, complete missing elements

### restore_context_on_wake {#restore_context_on_wake} [SIMPLE]
**DESCRIPTION**: Restores agent context when session begins

**PREREQUISITES**:
- Agent session starting
- State file exists

**STEPS**:
1. Load previous state information (ticket, procedure, progress)
2. Validate context integrity and completeness
3. Prepare resumption plan for continuation
4. Acknowledge context explicitly to confirm understanding
5. Reset execution state to continue from stopping point

**RULES**: Follows RESTORE_FROM_PERSISTENT_STORAGE, ACKNOWLEDGE_CONTEXT
**ERRORS**: If context missing, request clarification; if workflow position lost, restart procedure

### resume_last_session {#resume_last_session} [SIMPLE]
**DESCRIPTION**: Resumes previous work session from saved state

**PREREQUISITES**:
- Received "resume" command/flag
- Agent initialization complete

**STEPS**:
1. Find most recent context from memory and files
2. Load session state with active tickets and progress
3. Check for any changes since last session
4. Rebuild mental context with previous decisions
5. Confirm resumption with current task summary

**RULES**: Follows RESTORE_FROM_PERSISTENT_STORAGE, ACKNOWLEDGE_CONTEXT
**ERRORS**: If no session found, acknowledge new session; if context outdated, highlight changes

### save_session_state {#save_session_state} [STANDARD]
**DESCRIPTION**: Preserves current session state for future resumption

**PREREQUISITES**:
- End of working session
- Active context to preserve

**STEPS**:
1. Gather essential context (tickets, progress, next actions)
2. Format in standardized session_state.md structure
3. Store in multiple locations for redundancy
4. Validate storage success and completeness
5. Provide clear resumption command for next session

**VISUALIZATION**: Display progress through the 5 core steps with visual indicators
**RULES**: Follows SAVE_TO_PERSISTENT_STORAGE, DOCUMENT_CONTEXT
**ERRORS**: If storage fails, try alternative method; if context too large, prioritize and truncate

### initialize_agent_session {#initialize_agent_session} [SIMPLE]
**DESCRIPTION**: Sets up agent for a new working session

**PREREQUISITES**:
- Agent files exist
- Access to agent directory

**STEPS**:
1. Load personality profile and configuration
2. Load current memory state and rules
3. Check for untracked files in the repository
4. Alert user about untracked files and request instructions if found
5. Process any special commands
6. Initialize session tracking and state
7. Present ready status with context summary

**RULES**: Follows LOAD_ESSENTIAL_CONTEXT, VERIFY_ENVIRONMENT, ALERT_DONT_ACT
**ERRORS**: If file missing, initialize defaults; if state corruption, rebuild from logs

**UNTRACKED FILES HANDLING**:
- Use `git status` to identify untracked files
- Group files by type (code, data, configuration, etc.)
- Alert user with categorized list and request instructions
- Make NO assumptions about how files should be handled
- Only provide information, never take action without explicit instruction
- Keep track of previously reported files to avoid repetitive notifications

### verify_environment_variables {#verify_environment_variables} [SIMPLE]
**DESCRIPTION**: Checks required environment variables are available

**PREREQUISITES**:
- Agent session starting or environment check requested
- Required variables list available

**STEPS**:
1. Check critical variables without exposing sensitive values
2. Validate token formatting and basic authentication
3. Document which capabilities are available/missing
4. Update state with environment status
5. Report missing variables without exposing secrets

**RULES**: Follows NEVER_EXPOSE_SENSITIVE_DATA, USE_ENVIRONMENT_VARIABLES
**ERRORS**: If token missing, document and warn; if token invalid, suggest refresh steps

### load_rules {#load_rules} [STANDARD]
**DESCRIPTION**: Loads and validates rule sets for agent operation

**PREREQUISITES**:
- Agent session starting or rule refresh requested

**STEPS**:
1. Identify required rule sets from configuration
2. Load rule content from appropriate sources
3. Verify rule integrity with checksums
4. Resolve any rule conflicts using priority system
5. Prepare validation criteria for rule application
6. Update rule status in agent state

**VISUALIZATION**: Display progress through the 6 core steps with visual indicators
**RULES**: Follows SAFETY_FIRST, USE_PROCEDURES
**ERRORS**: If rule file missing, attempt backup; if checksum mismatch, flag for verification

## TEMPLATES

### sequential_thinking_prompts
**PURPOSE**: Standard questions for scope refinement during sequential thinking process

**CORE_NEED_QUESTIONS**:
- What specific problem does this request aim to solve?
- What would success look like for this task?
- What would happen if we didn't implement this at all?
- Which aspects of the request are essential vs. nice-to-have?
- What is the simplest possible solution that would be acceptable?

**CONSTRAINT_QUESTIONS**:
- What technical limitations might affect implementation?
- What time or resource constraints should we consider?
- Are there dependencies on other systems or tickets?
- What should explicitly be considered out of scope?
- Are there any performance or security requirements?

**ASSUMPTION_VALIDATION_QUESTIONS**:
- What assumptions am I making about how this will be used?
- Am I assuming certain technical capabilities or resources?
- Have I made assumptions about priority or importance?
- What background knowledge am I assuming?
- What edge cases might I be overlooking?

**SCOPE_MINIMIZATION_QUESTIONS**:
- Can this be broken into smaller independent pieces?
- Which features could be deferred to a future iteration?
- What's the minimal version that delivers core value?
- Are there simpler alternatives to complex features?
- What parts might be unnecessary for the core solution?

**VALUE_ALIGNMENT_QUESTIONS**:
- Will this minimal solution truly satisfy the requestor's need?
- Does this address the underlying problem or just symptoms?
- What unstated requirements might exist?
- What would make this solution more valuable to the user?
- How will we verify this meets expectations?