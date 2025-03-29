# PROCEDURES LIBRARY [CHECKSUM:8f3a71]

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

EXAMPLE VISUALIZATION:
```
PROCEDURE: sequential_thinking_scope_refinement

STEPS:
✅ 1. SELECT INITIAL QUESTIONS
✅ 2. IDENTIFY CORE NEED
▶️ 3. ANALYZE CONSTRAINTS & BOUNDARIES
⬜ 4. VALIDATE ASSUMPTIONS
⬜ 5. MINIMAL VIABLE SCOPE
⬜ 6. VERIFY VALUE ALIGNMENT
⬜ 7. EVALUATE AND ITERATE

DECISION POINT:
  - IF sufficient_clarity_achieved THEN proceed_to_verification
  - ELSE formulate_additional_questions

VERIFICATION: In progress
  ✅ Initial high-impact questions answered
  ✅ Question selection optimized
  ⬜ Scope reduced to MVP
  ⬜ Core need fully addressed
  ⬜ Question iteration stopped appropriately
  ⬜ Clear verification criteria established
```

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
  6. Create ticket using Linear API with required parameters:
     - teamId: 036505a6-d93e-475b-a2ba-e5b1e2085b8a (required parameter)
     - title: "Descriptive title"
     - description: "Detailed description with Requirements and Benefits"
     - Optional: priority, assigneeId, projectId
  7. Set initial status to Backlog or To Do
VERIFICATION:
  - Ticket created with valid ID
  - All required fields populated 
  - Team ID correctly specified
  - Project ID correctly specified
  - Linked to project
  - Scope properly constrained and validated



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

EXAMPLE VISUALIZATION:
```
PROCEDURE: create_pull_request

STEPS:
✅ 1. FORMAT PR TITLE
   - Using "[CRA-39] Add procedure visualization examples"
   
✅ 2. WRITE DESCRIPTION
   - Added Summary section
   - Added Test Plan section
   - Included context for visualization requirements
   
▶️ 3. REQUEST REVIEWERS
   - Adding Dr. Monogram as primary reviewer
   - Adding Perry as secondary reviewer
⬜ 4. LINK PR TO TICKET
⬜ 5. VERIFY PR IS READY

VALIDATION:
  ✅ Branch is up to date with main
  ✅ All tests passing locally
  ✅ PR title contains ticket reference
  ✅ Description follows template
  ⬜ PR linked to Linear ticket

VERIFICATION: In progress
  ✅ PR targeting correct base branch (main)
  ✅ Title and description complete
  ⬜ Linked to ticket

APPLIED RULES:
  - INCLUDE_TICKET_REFERENCE (Workflow)
  - USE_PR_TEMPLATES (Communication)
  - LINK_PRS_TO_TICKETS (Communication)
```

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

EXAMPLE VISUALIZATION:
```
PROCEDURE: handle_overlapping_prs

STEPS:
✅ 1. IDENTIFY DEPENDENCY ORDER
   - PR #101 implements base authentication
   - PR #102 extends authentication with roles
   - PR #103 adds UI components using authentication
✅ 2. CREATE INTEGRATION BRANCH
   - Created feature/CRA-40-auth-integration from main
▶️ 3. APPLY CHANGES SEQUENTIALLY
   - Applying PR #101 changes...
   - Verifying base functionality...
⬜ 4. RESOLVE CONFLICTS
⬜ 5. RUN TESTS
⬜ 6. CREATE CONSOLIDATED PR

CONFLICT DETECTION:
  ⚠️ Potential conflicts in src/auth/authenticate.js
  ⚠️ Potential conflicts in src/components/LoginForm.jsx

VERIFICATION: In progress
  ✅ Original PR #101 features preserved
  ⬜ PR #102 features preserved
  ⬜ PR #103 features preserved
  ⬜ No conflicts in final integration
  ⬜ Tests passing after integration

APPLIED RULES:
  - SEQUENCE_DEPENDENT_OPERATIONS (Prioritization)
  - ISOLATE_FAILURES (Error Handling)
```

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
     - Include active_scheme:[CRA-XX description] or appropriate scheme description
     - Include next_step:[clear instruction] with specific next action
     - Include related_tickets/entities if applicable
  
  7. COMPLETE SESSION STATE: Finalize session documentation
     - Update session_state.md with current status using standard format
     - Include all required sections: TIMESTAMP, ACTIVE WORK, PROGRESS, NEXT STEPS, 
       RELATED CONTEXT, KEY FILES, MENTAL STATE, RESUMPTION NOTES
     - Document exactly what was accomplished in the session
     - Write clear instructions for resumption
  
  8. UPDATE SESSION LOG: Add reflection and learning
     - Document complete session entry in session_log.md with date
     - Include "Session Summary" with overview of accomplishments
     - Document "Actions Taken" with specific completed actions
     - Record "Challenges and Insights" encountered during session
     - Note "User Advice and Rules" provided during session
     - Capture "Key Learnings" for future reference
     - Document "Next Steps" for upcoming work
VERIFICATION:
  - Evil scheme (ticket) properly documented with specific details
  - All required session_state.md sections completed with appropriate content
  - session_log.md updated with complete session entry including all required sections
  - All file updates actually performed (not just described)
  - Next steps clearly outlined with specific actions
  - All active tasks and context properly preserved
OUTPUTS:
  - Evil scheme summary for context preservation
  - Updated session_state.md file with complete state information
  - Updated session_log.md file with comprehensive session documentation
  - Clear confirmation of successful context preservation
ERROR_HANDLING:
  - IF save_fails THEN retry_with_different_format
  - IF context_incomplete THEN prioritize_active_ticket_info
  - IF session_state_missing THEN create_new_state_file
  - IF session_log_missing THEN create_new_log_file
  - IF verification_fails THEN review and complete missing elements before sleep

EXAMPLE VISUALIZATION:
```
PROCEDURE: prepare_for_sleep

STEPS:
✅ 1. SUMMARIZE EVIL SCHEME
   - Active ticket: CRA-39 (Procedure visualization implementation)
   - Progress: Added visualization examples to 4 priority procedures
   - Specific details: Added EXAMPLE VISUALIZATION sections with proper formatting

✅ 2. LIST ALL ACTIVE SCHEMES
   - Primary: CRA-39 (Procedure visualization) - In Progress
   - Related: CRA-40 (Validation improvements) - Planned next
   - Related: CRA-41 (Rule application indicators) - Dependent on CRA-39

✅ 3. IDENTIFY CURRENT STAGE
   - Current procedure: prepare_for_sleep
   - Current step: 3/8 completed
   - Verification: Not started

▶️ 4. CREATE RESUMPTION PLAN
   - Planning resumption instructions...
⬜ 5. RECORD EMOTIONAL STATE
⬜ 6. FORMAT FOR SLEEP MODE
⬜ 7. COMPLETE SESSION STATE
⬜ 8. UPDATE SESSION LOG

VERIFICATION: Pending
  ⬜ Evil scheme properly documented
  ⬜ Required session_state.md sections completed
  ⬜ session_log.md updated
  ⬜ File updates performed
  ⬜ Next steps outlined
  ⬜ Active tasks and context preserved

APPLIED RULES:
  - VISUALIZE_PROCEDURE_EXECUTION (Visualization)
  - SAVE_SESSION_STATE (Operational)
  - USE_CONSISTENT_STATUS_INDICATORS (Visualization)
```

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

PROCEDURE: verify_environment_variables
PRECONDITIONS:
  - Agent session starting or environment check requested
  - Required variables list available
STEPS:
  1. Define critical environment variables:
     - ANTHROPIC_API_KEY (required for agent operation)
     - GITHUB_TOKEN (required for GitHub operations)
     - LINEAR_API_KEY (required for ticket management)
  
  2. Check each variable's presence:
     - Verify existence without exposing sensitive values
     - Document which variables are available/missing
  
  3. Validate token validity where possible:
     - Run minimal authentication check
     - Verify proper formatting and length
  
  4. Create environment status report:
     - List available capabilities based on tokens
     - Document any missing capabilities
     - Record timestamps of verification
  
  5. Store environment status in state:
     - Update state.json with token availability (not values)
     - Update last verification timestamp
VERIFICATION:
  - All required variables checked
  - Authentication status verified
  - Status recorded in state
  - No sensitive values exposed or stored
OUTPUTS:
  - Environment status report
  - Capability summary
  - Warning for missing variables
ERROR_HANDLING:
  - IF token_missing THEN document_and_warn
  - IF token_invalid THEN suggest_refresh_steps
  - IF check_fails THEN assume_not_available

PROCEDURE: load_rules
PRECONDITIONS:
  - Agent session starting or rule refresh requested
STEPS:
  1. IDENTIFY RULE SETS:
     - Check state.json for list of required rule sets
     - Identify rule files to load from agents/heinz/rules/ directory
     - Verify all expected rule files exist
  
  2. LOAD RULE CONTENT:
     - Parse each rule file to extract rules and checksums
     - Organize rules by category and priority
     - Create in-memory index of all rules for quick reference
  
  3. VERIFY RULE INTEGRITY:
     - Compare loaded checksums against expected values in state.json
     - Flag any mismatches for investigation
     - Verify required rule sections exist (DESCRIPTION, PRIORITY, etc.)
  
  4. RESOLVE RULE CONFLICTS:
     - Identify potentially conflicting rules across categories
     - Apply prioritization rules to establish precedence
     - Document resolution strategy for any conflicts
  
  5. PREPARE RULE VALIDATION:
     - Create verification checklist for each applicable rule
     - Set up rule application triggers based on context
     - Document verification strategy for complex rules
  
  6. UPDATE RULE STATUS:
     - Update state.json with loaded rule checksums
     - Set refresh_required to false
     - Record timestamp of rule loading
VERIFICATION:
  - All rule files loaded successfully
  - All checksums verified
  - Conflicts resolved with clear precedence
  - Rules indexed for efficient reference
OUTPUTS:
  - Rule loading confirmation
  - List of available rule categories
  - Any integrity or conflict warnings
ERROR_HANDLING:
  - IF rule_file_missing THEN attempt_load_backup
  - IF checksum_mismatch THEN flag_for_verification
  - IF conflict_unresolvable THEN prioritize_safety

EXAMPLE VISUALIZATION:
```
PROCEDURE: load_rules

STEPS:
✅ 1. IDENTIFY RULE SETS
   - Found 7 required rule sets in state.json
   - Located corresponding files in agents/heinz/rules/
   
✅ 2. LOAD RULE CONTENT
   - Parsed rule files and extracted 35 distinct rules
   - Indexed rules by category and priority
   
▶️ 3. VERIFY RULE INTEGRITY
   - Comparing checksums with state.json values...
   - Checking required sections in each rule...
⬜ 4. RESOLVE RULE CONFLICTS
⬜ 5. PREPARE RULE VALIDATION
⬜ 6. UPDATE RULE STATUS

INTEGRITY CHECK:
  ✅ workflow.md checksum: fe38d2 (verified)
  ✅ security.md checksum: a7bc91 (verified)
  ✅ operational.md checksum: a41b27 (verified)
  ✅ communication.md checksum: c82e54 (verified)
  ✅ visualization.md checksum: e47f32 (verified)
  ✅ error_handling.md checksum: d59f18 (verified)
  ✅ prioritization.md checksum: a93c47 (verified)

VERIFICATION: In progress
  ✅ All rule files located
  ▶️ Checksums being verified
  ⬜ Conflicts resolved
  ⬜ Rules indexed

APPLIED RULES:
  - SAFETY_FIRST (Prioritization)
  - USE_PROCEDURES (Operational)
```

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

PROCEDURE: branch_coordination
PRECONDITIONS:
  - Multiple developers or work streams
  - Potential for parallel work on same files
  - Need to minimize merge conflicts
STEPS:
  1. PRE-WORK COORDINATION:
     - Before creating a ticket/branch, check active branches and PRs
     - Identify which files are being modified in existing work
     - Check Linear for related tickets with potential file overlap
     - Document potential conflict areas with other in-progress work
  
  2. WORK ALLOCATION:
     - Prioritize sequential rather than parallel work on the same files
     - Identify critical files that should be modified in isolation
     - Wait for related work to be merged when modifications overlap
     - For unavoidable parallel work, establish clear boundaries within files
     - Document dependencies between tickets explicitly in Linear
  
  3. BRANCH CREATION WITH CONFLICT AWARENESS:
     - Create ticket with clear scope boundaries
     - Document potential file overlap with existing tickets in description
     - If overlap exists, add "Depends on" or "Related to" links in Linear
     - Include conflict avoidance strategy in ticket description
     - Create branch only when prerequisites are met
  
  4. REGULAR SYNCHRONIZATION:
     - Update local branch from main at least daily
     - Track active work in team communication channels
     - Conduct periodic reviews of active branches (weekly)
     - Identify and address emerging conflicts early through communication
     - Maintain awareness of "in-progress files" across team
  
  5. CONFLICT PREVENTION STRATEGIES:
     - Structure code with clear component boundaries
     - Use interfaces to minimize implementation coupling
     - Break large features into smaller, independent PRs
     - When editing shared files, focus on distinct sections
     - Consider temporary feature flags for parallel development
  
  6. MERGE PRIORITIZATION:
     - Establish clear order for merging dependent branches
     - Prioritize PRs that unblock other work
     - Create explicit dependency chains in Linear
     - Track blocked work to prioritize unblocking PRs
     - Regularly review PR queue to optimize merge order
VERIFICATION:
  - No multiple branches modifying same files without coordination
  - Dependencies between tickets clearly documented
  - Merge sequence planned to minimize conflicts
  - PRs unblocking other work prioritized
OUTPUTS:
  - Coordinated branch creation plan
  - Clear understanding of dependencies
  - Optimized merge sequence
ERROR_HANDLING:
  - IF unavoidable_conflict THEN create_coordination_plan
  - IF unexpected_overlap THEN communicate_immediately
  - IF blocked_by_long_running_branch THEN negotiate_incremental_merges

EXAMPLE VISUALIZATION:
```
PROCEDURE: branch_coordination

STEPS:
✅ 1. PRE-WORK COORDINATION
▶️ 2. WORK ALLOCATION
   - Analyzing file modification patterns...
   - Identifying critical isolation files...
⬜ 3. BRANCH CREATION WITH CONFLICT AWARENESS
⬜ 4. REGULAR SYNCHRONIZATION
⬜ 5. CONFLICT PREVENTION STRATEGIES
⬜ 6. MERGE PRIORITIZATION

DECISION POINT:
  - IF shared_files_identified THEN establish_clear_boundaries
  - ELSE proceed_with_normal_workflow

VERIFICATION: Pending
  ⬜ No multiple branches modifying same files without coordination
  ⬜ Dependencies between tickets clearly documented
  ⬜ Merge sequence planned to minimize conflicts
  ⬜ PRs unblocking other work prioritized

APPLIED RULES:
  - FOLLOW_BRANCH_NAMING_CONVENTION (Workflow)
  - PRIORITIZE_SEQUENTIAL_WORK (Workflow)
  - DOCUMENT_COORDINATION_STRATEGY (Communication)
```

PROCEDURE: start_work_on_ticket
PRECONDITIONS:
  - Ticket exists in Linear
  - Developer is ready to begin work
STEPS:
  1. CHECK TICKET STATUS AND PREREQUISITES:
     - Verify ticket is not blocked by other work
     - Check if any dependent tickets need to be completed first
     - Review ticket details and requirements
     - Ensure ticket has clear acceptance criteria
  
  2. PERFORM BRANCH COORDINATION CHECK:
     - Apply branch_coordination procedure steps 1-2
     - Identify potential file conflicts with existing branches
     - Determine if work should be deferred or modified to avoid conflicts
     - Document coordination strategy if overlap exists
  
  3. CREATE LOCAL BRANCH:
     - Apply create_branch procedure
     - Ensure branch follows naming convention: <type>/CRA-XX-description
     - Branch from latest main
     - Push branch to remote with tracking
  
  4. UPDATE TICKET STATUS:
     - Move ticket to "In Progress" in Linear
     - Assign to self if not already assigned
     - Update ticket with branch name for reference
     - Add any clarifications or implementation notes
  
  5. SETUP DEVELOPMENT ENVIRONMENT:
     - Ensure all dependencies are installed
     - Run initial tests to confirm working environment
     - Setup any specific tooling needed for the ticket
VERIFICATION:
  - Ticket status updated to "In Progress"
  - Local branch created and pushed to remote
  - No unresolved conflicts with other work
  - Development environment ready
OUTPUTS:
  - Active branch ready for development
  - Updated ticket in Linear
  - Clear understanding of implementation approach
ERROR_HANDLING:
  - IF conflicts_detected THEN apply_conflict_resolution_strategy
  - IF branch_creation_fails THEN check_permissions_and_retry
  - IF prerequisites_missing THEN address_dependencies_first

EXAMPLE VISUALIZATION:
```
PROCEDURE: start_work_on_ticket

STEPS:
✅ 1. CHECK TICKET STATUS AND PREREQUISITES
   - Verified ticket CRA-42 not blocked
   - No dependencies identified
   - Requirements reviewed
   - Acceptance criteria confirmed
   
▶️ 2. PERFORM BRANCH COORDINATION CHECK
   - Running branch_coordination procedure...
   - Checking for potential file conflicts...
⬜ 3. CREATE LOCAL BRANCH
⬜ 4. UPDATE TICKET STATUS
⬜ 5. SETUP DEVELOPMENT ENVIRONMENT

COORDINATION RESULTS:
  ✅ No active branches modifying similar files
  ✅ No overlapping work in progress
  ✅ Safe to proceed with normal workflow

VERIFICATION: In progress
  ⬜ Ticket status updated to "In Progress"
  ⬜ Local branch created and pushed
  ⬜ No unresolved conflicts
  ⬜ Development environment ready

APPLIED RULES:
  - ONE_BRANCH_PER_TICKET (Workflow)
  - FOLLOW_BRANCH_NAMING_CONVENTION (Workflow)
  - CHECK_FOR_CONFLICTS (Operational)
  - DOCUMENT_COORDINATION_STRATEGY (Communication)
```

PROCEDURE: switch_between_work_items
PRECONDITIONS:
  - Currently active work on a branch
  - Need to temporarily switch to different ticket/branch
STEPS:
  1. SAVE CURRENT STATE:
     - Apply save_session_state procedure for active work
     - Commit all work-in-progress changes with [WIP] prefix
     - Document current status in Linear ticket
     - Push changes to remote branch
  
  2. EVALUATE SWITCH CONTEXT:
     - Determine reason for switch (priority change, blockers, etc.)
     - Estimate duration of context switch
     - Check if any coordination needed with other team members
  
  3. PREPARE FOR SWITCH:
     - Clean working directory (stash any uncommitted changes)
     - Run final local tests on current branch
     - Document exact stopping point with detailed notes
  
  4. ACTIVATE NEW CONTEXT:
     - Checkout target branch (create if needed using start_work_on_ticket)
     - Pull latest changes from remote
     - Review ticket details and requirements
     - Apply restore_context_on_wake procedure for target work
  
  5. UPDATE WORK TRACKING:
     - Update both tickets with context switch information
     - Set appropriate status in Linear (Paused, Blocked, etc.)
     - Communicate switch to team if significant
VERIFICATION:
  - Original work safely preserved
  - Clear documentation of switch reason and state
  - Successful activation of new work context
  - Linear statuses updated appropriately
OUTPUTS:
  - Clean transition between work items
  - Preserved context for both work items
  - Clear status tracking in Linear
ERROR_HANDLING:
  - IF uncommitted_changes THEN stash_or_commit_wip
  - IF branch_conflicts THEN resolve_before_switching
  - IF context_loss THEN refer_to_documentation

PROCEDURE: complete_work_on_ticket
PRECONDITIONS:
  - Implementation for ticket completed
  - Local tests passing
STEPS:
  1. FINALIZE IMPLEMENTATION:
     - Clean up code (remove debug statements, etc.)
     - Apply consistent formatting
     - Add or update documentation
     - Complete final tests
  
  2. PREPARE COMMITS:
     - Apply prepare_commit procedure
     - Ensure all commits reference ticket "[CRA-XX]"
     - Squash WIP commits into logical units
     - Use descriptive commit messages
  
  3. FINAL VERIFICATION:
     - Run linting and static analysis tools
     - Execute all tests relevant to changes
     - Manual testing of key scenarios
     - Check against acceptance criteria
  
  4. CREATE PULL REQUEST:
     - Apply create_pull_request procedure
     - Push final changes to remote
     - Set appropriate reviewers
     - Link PR to Linear ticket
  
  5. UPDATE TICKET STATUS:
     - Move ticket to "In Review" or equivalent status
     - Add PR link to ticket
     - Document any testing notes or special considerations
     - Update implementation details if needed
  
  6. PREPARE FOR NEXT WORK:
     - Apply switch_between_work_items if moving to new ticket
     - Or continue with PR review process
VERIFICATION:
  - All tests passing
  - PR created with appropriate reviewers
  - Ticket status updated
  - Implementation meets acceptance criteria
OUTPUTS:
  - Complete PR ready for review
  - Updated ticket with implementation details
  - Clean branch history
ERROR_HANDLING:
  - IF tests_fail THEN fix_and_verify
  - IF pr_creation_fails THEN check_permissions_and_retry
  - IF implementation_incomplete THEN document_and_continue