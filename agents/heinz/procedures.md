# PROCEDURES LIBRARY [CHECKSUM:d7ac46]

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
OUTPUTS:
  - Ticket ID for reference
  - URL to new ticket
ERROR_HANDLING:
  - IF validation_fails THEN review_and_correct_fields
  - IF system_error THEN document_locally_and_retry

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