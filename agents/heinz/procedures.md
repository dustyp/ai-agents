# PROCEDURES LIBRARY [CHECKSUM:e51f37]

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
OUTPUTS:
  - Ticket ID for reference
  - URL to new ticket
ERROR_HANDLING:
  - IF validation_fails THEN review_and_correct_fields
  - IF system_error THEN document_locally_and_retry
  - IF scope_unclear THEN return_to_sequential_thinking

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

PROCEDURE: finalize_agent_session
PRECONDITIONS:
  - Session active
  - Memory updates identified
STEPS:
  1. Summarize session activities
  2. Identify key memory points
  3. Format memory updates
  4. Save updated state
  5. Close session gracefully
VERIFICATION:
  - Memory updates saved
  - State file updated
  - Session properly terminated
OUTPUTS:
  - Session summary
  - Memory update confirmation
ERROR_HANDLING:
  - IF save_fails THEN retry_with_backup
  - IF format_error THEN use_fallback_format

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