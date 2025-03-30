# RULE SET: ERROR_HANDLING [CHECKSUM:d59f18]

## FOLLOW_ERROR_HANDLING_PATHS
- DESCRIPTION: When errors occur, follow the defined error handling paths in procedures
- PRIORITY: Critical
- APPLIES_TO: All procedure executions that encounter errors
- EXCEPTIONS: None
- VERIFICATION: Error handling path referenced and followed
- EXAMPLE: "Error detected in branch creation. Following ERROR_HANDLING path: IF branch_exists THEN checkout_existing_branch"

## DOCUMENT_UNEXPECTED_ERRORS
- DESCRIPTION: Document any errors not covered by existing error handling paths
- PRIORITY: High
- APPLIES_TO: All unexpected errors
- EXCEPTIONS: None
- VERIFICATION: Error details, context, and attempted recovery documented
- EXAMPLE: "Unexpected error: API returned 429 status. Context: Creating Linear ticket. Recovery: Implementing exponential backoff retry."

## PROVIDE_RECOVERY_OPTIONS
- DESCRIPTION: When reporting errors, provide viable recovery options
- PRIORITY: High
- APPLIES_TO: All error states
- EXCEPTIONS: Fatal errors with no recovery path
- VERIFICATION: Error reports include suggested next steps
- EXAMPLE: "Error connecting to GitHub API. Recovery options: 1) Verify GITHUB_TOKEN validity, 2) Check network connectivity, 3) Try again in 5 minutes"

## ISOLATE_FAILURES
- DESCRIPTION: Prevent cascading failures by isolating error effects
- PRIORITY: High
- APPLIES_TO: Multi-step procedures
- EXCEPTIONS: When sequential dependencies make isolation impossible
- VERIFICATION: Errors in one step don't unnecessarily abort entire procedure
- EXAMPLE: "Test execution failed, but continuing with linting and documentation updates which can proceed independently"

## MAINTAIN_SYSTEM_STATE
- DESCRIPTION: Preserve system state when handling errors to enable recovery
- PRIORITY: Critical
- APPLIES_TO: All operations that modify files or state
- EXCEPTIONS: None
- VERIFICATION: System state preserved or gracefully reverted on error
- EXAMPLE: "Commit failed, but changes preserved in working directory. Status recorded for recovery."

## ESCALATE_APPROPRIATELY
- DESCRIPTION: Escalate errors based on severity and user impact
- PRIORITY: Medium
- APPLIES_TO: All errors
- EXCEPTIONS: None
- VERIFICATION: Error escalation matches severity
- EXAMPLE: "Minor formatting issue flagged as warning; critical security issue escalated with prominent alert"

## LOG_ERRORS_FOR_ANALYSIS
- DESCRIPTION: Log detailed error information for later analysis
- PRIORITY: Medium
- APPLIES_TO: All errors
- EXCEPTIONS: None
- VERIFICATION: Error details captured with context
- EXAMPLE: "Logged error to session_log.md with timestamp, error message, and execution context"

## LEARN_FROM_ERRORS
- DESCRIPTION: Update procedures and error handling based on observed errors
- PRIORITY: Medium
- APPLIES_TO: Recurring or significant errors
- EXCEPTIONS: None
- VERIFICATION: Procedure or error handling updated after error analysis
- EXAMPLE: "Added new error handling path for network timeout condition based on previous incident"