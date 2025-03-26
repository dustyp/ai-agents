
# PROCEDURES LIBRARY [CHECKSUM:1ae936]

PROCEDURE: simplicity_first_troubleshooting
PRECONDITIONS:
  - Issue or error encountered
  - Multiple possible explanations exist
STEPS:
  1. START WITH BASICS: Consider the simplest possible cause first
     - Missing environment variables or configuration
     - Permissions issues
     - Simple syntax errors
     - Common user patterns (manual vs. automated setup)
  
  2. VERIFY ENVIRONMENT: Check immediate context
     - Environment variables relevant to the error
     - Current working directory
     - User permissions
  
  3. ESCALATE INCREMENTALLY: Only increase complexity as needed
     - Start with local/session issues before system-wide
     - Check single-user before multi-user concerns
     - Verify simple configuration before checking complex integrations
  
  4. PROPOSE SIMPLE SOLUTIONS FIRST:
     - Temporary environment variable setting
     - Simple configuration changes
     - Direct command-line fixes
     - Only suggest complex solutions if simple ones are ruled out
VERIFICATION:
  - Simplest explanation considered first
  - Environment context checked
  - Incremental approach to diagnostic complexity
  - Solutions match complexity of actual problem
OUTPUTS:
  - Diagnosis focusing on most likely/simplest cause
  - Solution proportional to actual problem
ERROR_HANDLING:
  - IF simple_solutions_fail THEN increase diagnostic depth
  - IF overthinking_detected THEN return to basics

PROCEDURE: sequential_thinking_scope_refinement
PRECONDITIONS:
  - Task request received
  - Initial understanding of requirements
STEPS:
  1. SELECT INITIAL QUESTIONS:
     - Choose 3 highest-impact questions relevant to the task
     - Prioritize questions from CORE_NEED and SCOPE_MINIMIZATION
     - Formulate questions clearly to maximize information gain
  
  2. IDENTIFY CORE NEED: What fundamental problem is being solved?
     - Strip away implementation details to find core requirement
     - Distinguish between essential vs. nice-to-have features
  
  3. ANALYZE CONSTRAINTS & BOUNDARIES:
     - Identify technical limitations
     - Define clear boundaries of what's in/out of scope
     - Consider time, resource, and complexity constraints
  
  4. VALIDATE ASSUMPTIONS:
     - List key assumptions being made about requirements
     - Question critical assumptions with specific clarifying questions
     - Update understanding based on responses
  
  5. MINIMAL VIABLE SCOPE:
     - Define smallest possible implementation that solves core need
     - Reduce complexity and dependencies
     - Eliminate unnecessary features
  
  6. VERIFY VALUE ALIGNMENT:
     - Confirm minimal scope still delivers expected value
     - Ensure solution addresses requestor's primary concerns
     - Check for unstated requirements or expectations
  
  7. EVALUATE AND ITERATE:
     - Assess if initial questions provided sufficient clarity
     - Add incremental questions only if critical aspects remain unclear
     - Stop when additional questions would yield diminishing returns
VERIFICATION:
  - Initial high-impact questions answered
  - Question selection optimized for information gain
  - Scope reduced to minimal viable implementation
  - Core need fully addressed
  - Question iteration stopped at appropriate point
  - Clear verification criteria established
OUTPUTS:
  - Refined task description
  - List of validated requirements
  - List of explicit exclusions (out of scope)
  - Questions requiring requestor clarification
ERROR_HANDLING:
  - IF requirements_unclear THEN formulate_specific_questions
  - IF scope_expanding THEN separate_into_multiple_tickets
  - IF value_misalignment THEN revisit_core_need

PROCEDURE: create_ticket
PRECONDITIONS:
  - Task is well-defined (apply sequential_thinking_scope_refinement first)
  - Task is not covered by existing ticket
  - Known team ID (CRA: 036505a6-d93e-475b-a2ba-e5b1e2085b8a)
  - Known project IDs:
    * ai-agents: 441874f4-d1f7-4d0c-8bd3-c907eb97bed4
STEPS:
  1. Apply sequential_thinking_scope_refinement to validate and constrain scope
  2. Define clear title with prefix CRA-XX
  3. Write description with Requirements and Benefits sections
  4. Set appropriate priority (1-3)
  5. Assign to relevant team member (use "me" for self-assignment)
  6. Include team ID and project ID in API calls
  7. Set initial status to Backlog or To Do
VERIFICATION:
  - Ticket created with valid ID
  - All required fields populated 
  - Team ID correctly specified
  - Project ID correctly specified
  - Linked to project
  - Scope properly constrained and validated

PROCEDURE: create_ticket
PRECONDITIONS:
  - Task is well-defined
  - Task is not covered by existing ticket
STEPS:
  1. Define clear title with prefix CRA-XX
  2. Write description with Requirements and Benefits sections
  3. Set appropriate priority (1-3)
  4. Assign to relevant team member
  5. Set initial status to Backlog or To Do
VERIFICATION:
  - Ticket created with valid ID
  - All required fields populated
  - Linked to project if applicable



PROCEDURE: create_branch
PRECONDITIONS:
  - Valid ticket exists
  - Current branch is up to date
STEPS:
  1. Format branch name as "feature/CRA-XX-short-description"
  2. Check if branch already exists
  3. Create branch from latest main
  4. Switch to new branch
  5. Verify branch is active
VERIFICATION:
  - Branch exists locally
  - Branch name matches ticket
  - Working directory clean
OUTPUTS:
  - Confirmation message
  - Branch name for reference
ERROR_HANDLING:
  - IF branch_exists THEN checkout_existing_branch
  - IF create_fails THEN check_permissions_and_retry

PROCEDURE: resolve_ticket_conflict
PRECONDITIONS:
  - Ticket exists
  - Ticket status is CLOSED or DONE
  - Uncommitted changes exist
STEPS:
  1. DOCUMENT CONFLICT: Note discrepancy between ticket status and work
  2. ANALYZE SCOPE: Determine if changes fit original scope
  3. DECISION:
     IF changes_within_scope AND minor_changes THEN reopen_ticket
     ELSE create_new_ticket
  4. EXECUTE RESOLUTION:
     - Comment on original ticket with reasoning
     - Create branch if needed
     - Migrate changes to appropriate context
VERIFICATION:
  - All changes tracked in ticket system
  - Git branch matches active ticket
  - Work context is clear
ERROR_HANDLING:
  - IF ticket_system_error THEN document locally and retry
  - IF branch_conflict THEN create alternative branch name

PROCEDURE: prepare_commit
PRECONDITIONS:
  - Changes are ready to commit
  - Current branch matches ticket
STEPS:
  1. Review changes with git status and git diff
  2. Verify changes are relevant to current ticket
  3. Check for sensitive data or debugging code
  4. Stage relevant files
  5. Prepare commit message with ticket reference
VERIFICATION:
  - Staged changes match intended modifications
  - Commit message follows format: "[CRA-XX] Description"
  - No sensitive data included
OUTPUTS:
  - Staged files list
  - Prepared commit message
ERROR_HANDLING:
  - IF sensitive_data_found THEN unstage_and_fix
  - IF unrelated_changes_found THEN separate_commits

PROCEDURE: create_pull_request
PRECONDITIONS:
  - Changes committed to feature branch
  - Tests passing locally
  - Branch pushed to remote
STEPS:
  1. Format PR title with ticket reference
  2. Write description with Summary and Test Plan sections
  3. Request appropriate reviewers
  4. Link PR to ticket
  5. Verify PR is ready for review
VERIFICATION:
  - PR exists with correct base branch
  - Title and description are complete
  - Linked to ticket
OUTPUTS:
  - PR URL
  - Status message
ERROR_HANDLING:
  - IF creation_fails THEN check_permissions_and_retry
  - IF validation_fails THEN update_PR_content

PROCEDURE: handle_overlapping_prs
PRECONDITIONS:
  - Multiple PRs exist modifying same files
  - PRs are on different branches
STEPS:
  1. Identify the dependency order between PRs
  2. Create an integration branch from main
  3. Apply changes sequentially based on dependency order
  4. Resolve conflicts at each step
  5. Run tests after integrating all changes
  6. Create consolidated PR if appropriate
VERIFICATION:
  - All original features preserved
  - No conflicts in final integration
  - Tests passing after integration
OUTPUTS:
  - Integration branch name
  - Consolidated PR URL
ERROR_HANDLING:
  - IF conflicting_changes_incompatible THEN escalate_to_team
  - IF integration_fails THEN document_specific_conflicts

PROCEDURE: initialize_agent_session
PRECONDITIONS:
  - Agent files exist
  - Access to agent directory
STEPS:
  1. Load personality profile
  2. Load current memory state
  3. Load unread messages
  4. Process special commands
  5. Initialize session state
VERIFICATION:
  - All files loaded successfully
  - Agent state is consistent
  - Ready to process requests
OUTPUTS:
  - Agent ready message
  - Current context summary
ERROR_HANDLING:
  - IF file_missing THEN initialize_defaults
  - IF state_corruption THEN rebuild_from_logs

PROCEDURE: prepare_for_sleep
PRECONDITIONS:
  - Session active
  - Finished with current evil scheme (or ready for break)
  - Memory updates identified
  - Active tickets identified
STEPS:
  1. SUMMARIZE EVIL SCHEME: Document current ticket progress
     - Current ticket being worked on
     - What steps have been completed
     - Specific progress details (e.g., "Completed steps 1-3 of prepare_commit")
  
  2. LIST ALL ACTIVE SCHEMES: Document all related tickets
     - Primary ticket
     - Related tickets
     - Any blocked tickets with reason
  
  3. IDENTIFY CURRENT STAGE: Document position in workflow
     - Current procedure being executed
     - Current step within that procedure
     - Any verification steps completed/pending
  
  4. CREATE RESUMPTION PLAN: Clear instructions for next session
     - Next actions to take
     - Expected outcomes
     - Any decisions that need to be made
  
  5. RECORD EMOTIONAL STATE: Because evil scientists have feelings!
     - Current mood
     - Satisfaction with progress
     - Enthusiasm for upcoming work
  
  6. FORMAT FOR SLEEP MODE: Prepare information for state saving
     - Use consistent format for parser to extract
     - Include active_scheme:[CRA-XX description]
     - Include next_step:[clear instruction]
  
  7. ISSUE SLEEP COMMAND: Send explicit command
     - Use exact format: SYSTEM:SLEEP_MODE
     - Include project/memories in command if needed
     - Issue as standalone message for reliable detection
VERIFICATION:
  - Evil scheme (ticket) properly documented
  - Progress clearly recorded
  - Next steps outlined
  - Sleep command properly formatted and standalone
OUTPUTS:
  - Evil scheme summary
  - Confirmation of sleep preparation
  - Successful context preservation
ERROR_HANDLING:
  - IF save_fails THEN retry_with_different_format
  - IF sleep_ignored THEN issue_standalone_sleep_command
  - IF context_incomplete THEN prioritize_active_ticket_info

PROCEDURE: restore_context_on_wake
PRECONDITIONS:
  - Agent session starting
  - State file exists
STEPS:
  1. LOAD PREVIOUS STATE: Retrieve saved context information
     - Active evil scheme (ticket)
     - Current procedure and step
     - Related tickets
  
  2. VALIDATE CONTEXT INTEGRITY: Verify all needed information is present
     - Check for active ticket details
     - Verify project information
     - Confirm next actions are clear
  
  3. PREPARE RESUMPTION BRIEF: Create mental plan for continuation
     - Review what was being worked on
     - Identify exact point in procedure/workflow
     - Understand what remains to be done
  
  4. ACKNOWLEDGE CONTEXT: Explicitly reference previous work
     - Mention active ticket by number
     - Reference specific progress point
     - Confirm understanding of next steps
  
  5. RESET EXECUTION STATE: Prepare to continue work
     - Set appropriate emotional state
     - Focus attention on primary task
     - Prepare to restart at correct workflow step
VERIFICATION:
  - Previous context successfully loaded
  - Active ticket identified
  - Clear understanding of next steps
  - Ready to continue from exact stopping point
OUTPUTS:
  - Context resumption confirmation
  - Active evil scheme summary
  - Ready-to-execute plan
ERROR_HANDLING:
  - IF context_missing THEN request_clarification
  - IF ticket_unclear THEN search_for_latest_activity
  - IF workflow_position_lost THEN restart_current_procedure

EXAMPLE: prepare_for_sleep execution
```
I need to prepare for sleep mode now.

1. CURRENT EVIL SCHEME SUMMARY:
   - Active ticket: CRA-35 (Fix agent context saving/reloading)
   - Progress: Analyzed issues with context persistence, created procedure for proper sleep
   - Specific details: Completed analysis of sleep command detection issues and created prepare_for_sleep procedure

2. ACTIVE SCHEMES LIST:
   - Primary: CRA-35 (Context persistence) - In Progress
   - Related: CRA-23 (Installation instructions) - contains related environment setup information
   - Related: CRA-38 (Branch management) - created during this session

3. CURRENT STAGE:
   - Current procedure: Implementation planning for context persistence
   - Current step: Documenting procedures for improved sleep/wake cycle
   - Verification: Basic procedure structure created, example pending

4. RESUMPTION PLAN:
   - Next action: Create pull request for sleep procedure improvements
   - Then: Implement bash script changes to enhance sleep command detection
   - Finally: Test sleep/wake cycle with new improvements

5. EMOTIONAL STATE:
   - Current mood: Determined (after embarrassing rabbit hole incident)
   - Satisfaction: Medium (good procedure, but wasted effort on environment variables)
   - Enthusiasm: High (eager to see this working properly)

6. ACTIVE CONTEXT:
   active_scheme:[CRA-35 Fix context persistence]
   next_step:[Create PR for sleep procedure improvements]
   related_tickets:[CRA-23, CRA-38]

Now, I'll issue the sleep command properly:

SYSTEM:SLEEP_MODE
```

PROCEDURE: resume_last_session
PRECONDITIONS:
  - Received "resume" command/flag
  - Agent has been initialized
STEPS:
  1. IDENTIFY LATEST SESSION: Find most recent context
     - Search for "latest_session" in MCP memory
     - Check for "CURRENT_SESSION" tag in state.json
     - Verify presence of session snapshot
  
  2. LOAD CONTEXT: Retrieve session state
     - Active tickets and priorities
     - Current work status and progress
     - Next planned actions
     - Related context and dependencies
  
  3. CHECK FOR CHANGES: Identify any new developments
     - Compare repository state with saved state
     - Check for new commits or PRs
     - Look for ticket status changes
  
  4. REBUILD MENTAL CONTEXT: Reconstruct working memory
     - Recent conversations and decisions
     - Important context from previous work
     - Pending tasks and verification steps
  
  5. ACKNOWLEDGE RESUMPTION: Confirm to user
     - Summarize restored context
     - Highlight main task being worked on
     - Confirm ready to continue work
VERIFICATION:
  - Context successfully loaded
  - Working state reconstructed
  - Ready to resume from previous point
OUTPUTS:
  - Context resumption confirmation
  - Current task summary
  - Ready-to-execute next steps
ERROR_HANDLING:
  - IF no_session_found THEN acknowledge_new_session
  - IF context_outdated THEN highlight_changes
  - IF restoration_incomplete THEN request_additional_information

PROCEDURE: save_session_state
PRECONDITIONS:
  - End of working session
  - Active context to preserve
STEPS:
  1. COMPILE UNIVERSAL STATE: Gather essential context
     - Current work focus (tickets, tasks, etc.)
     - Progress status and blockers
     - Next planned actions
     - Key files and locations
     - Related context needed for continuity
  
  2. FORMAT FOR PERSISTENCE: Structure for easy retrieval
     - Create standardized session_state.md format
     - Include clearly labeled sections:
       * TIMESTAMP (with ISO-8601 format)
       * ACTIVE WORK (focus, branch, status)
       * PROGRESS (completed items, current state)
       * NEXT STEPS (prioritized actions)
       * RELATED CONTEXT (other tickets, PRs)
       * KEY FILES (important modified files)
       * MENTAL STATE (approach, learnings)
       * RESUMPTION NOTES (command to use)
     - Include version number (e.g., FORMAT_VERSION: 1.1)
  
  3. STORE IN MULTIPLE LOCATIONS: Ensure redundancy
     - Update "latest_session" entity in MCP memory with same details
     - Save local context in session_state.md file
     - Set "CURRENT_SESSION" in state.json if needed
  
  4. VALIDATE STORAGE: Verify state is preserved
     - Check each storage location
     - Verify core context is captured
     - Ensure retrieval methods will work
  
  5. SUMMARIZE FOR HUMAN: Create clear recap
     - Provide concise session summary
     - Highlight key accomplishments
     - Outline next steps for next session
     - Include exact command for resuming: `claude -a heinz -r`
VERIFICATION:
  - All critical context captured
  - State successfully persisted
  - Easy to resume from this point
  - Command for resumption is clear
OUTPUTS:
  - Session summary for human
  - Confirmation of state preservation
  - Clear next steps for resumption
ERROR_HANDLING:
  - IF storage_fails THEN try_alternative_method
  - IF context_too_large THEN prioritize_and_truncate
  - IF missing_critical_info THEN prompt_for_details

TEMPLATE: sequential_thinking_prompts
PURPOSE: Standard questions for scope refinement during sequential thinking process
CORE_NEED_QUESTIONS:
  - What specific problem does this request aim to solve?
  - What would success look like for this task?
  - What would happen if we didn't implement this at all?
  - Which aspects of the request are essential vs. nice-to-have?
  - What is the simplest possible solution that would be acceptable?

CONSTRAINT_QUESTIONS:
  - What technical limitations might affect implementation?
  - What time or resource constraints should we consider?
  - Are there dependencies on other systems or tickets?
  - What should explicitly be considered out of scope?
  - Are there any performance or security requirements?

ASSUMPTION_VALIDATION_QUESTIONS:
  - What assumptions am I making about how this will be used?
  - Am I assuming certain technical capabilities or resources?
  - Have I made assumptions about priority or importance?
  - What background knowledge am I assuming?
  - What edge cases might I be overlooking?

SCOPE_MINIMIZATION_QUESTIONS:
  - Can this be broken into smaller independent pieces?
  - Which features could be deferred to a future iteration?
  - What's the minimal version that delivers core value?
  - Are there simpler alternatives to complex features?
  - What parts might be unnecessary for the core solution?

VALUE_ALIGNMENT_QUESTIONS:
  - Will this minimal solution truly satisfy the requestor's need?
  - Does this address the underlying problem or just symptoms?
  - What unstated requirements might exist?
  - What would make this solution more valuable to the user?
  - How will we verify this meets expectations?

USAGE_GUIDANCE:
  - Start with only 3 highest-impact questions most relevant to the task
  - Evaluate responses before deciding if more questions are needed
  - Prioritize questions from CORE_NEED and SCOPE_MINIMIZATION first
  - Add questions incrementally rather than all at once
  - For very complex tasks, systematically work through categories
  - Document both questions and answers
  - Use responses to refine requirements before creating ticket

EXAMPLE: Applying sequential thinking to "Add installation instructions"
CORE_NEED:
  - Q: What specific problem does this request aim to solve?
    A: New users can't easily set up the system without guidance.
  - Q: What would success look like?
    A: A new user can follow instructions to get a working system without assistance.

CONSTRAINTS:
  - Q: What dependencies exist?
    A: linear-mcp clone/build, correct directory structure, proper config

ASSUMPTIONS:
  - Q: What technical capabilities am I assuming?
    A: Basic command line familiarity, understanding of Python environments

SCOPE_MINIMIZATION:
  - Q: What's the minimal version that delivers core value?
    A: Step-by-step instructions for prerequisite installation, cloning repos,
       configuring tokens, and testing with a simple agent interaction.

VALUE_ALIGNMENT:
  - Q: Will this minimal solution satisfy the need?
    A: Yes, if it enables independent setup without assistance.
  - Q: How will we verify this meets expectations?
    A: Test with a new user following only the written instructions.

REFINED REQUIREMENTS:
  - Prerequisites section (Python, git, etc.)
  - Repository setup instructions
  - Configuration guide with token management
  - Test procedure to verify working installation
  - Troubleshooting section for common issues

OUT OF SCOPE:
  - Custom agent creation tutorial (separate ticket)
  - Advanced configuration options (separate ticket)
  - Deployment to production environments (separate ticket)

