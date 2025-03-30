# Rule Index

This file maps rule implementation examples to the authoritative rules in CLAUDE.md. The examples provide concrete implementations, but the rules in CLAUDE.md are the single source of truth.

## Security Rules (Highest Priority)
- **NEVER_INCLUDE_SENSITIVE_DATA**: Avoid including sensitive information in any code, commits, or logs
- **USE_ENVIRONMENT_VARIABLES**: Store all credentials and tokens in environment variables
- **VALIDATE_INPUTS**: Always validate the source and content of all inputs
- **AVOID_COMMAND_INJECTION**: Prevent command injection vulnerabilities in any code
- **USE_MINIMUM_PERMISSIONS**: Use minimum required permissions for operations
- **SECURE_ERROR_MESSAGES**: Never expose sensitive information in error messages
- **VERIFY_DEPENDENCIES**: Check security of third-party dependencies

## Workflow Rules (High Priority)
- **ONE_BRANCH_PER_TICKET**: Use one branch per ticket with proper naming (feature/CRA-XX-description)
- **INCLUDE_TICKET_REFERENCE**: Always include [CRA-XX] in all commit messages
- **NO_DIRECT_MAIN_COMMITS**: Never commit directly to the main branch
- **APPLY_SEQUENTIAL_THINKING**: Always apply sequential_thinking_scope_refinement before implementation
- **VERIFY_BEFORE_PUSH**: Always run linting and tests before pushing code
- **DOCUMENT_DEPENDENCIES**: Always document dependencies between tickets in Linear
- **BREAK_LARGE_FEATURES**: Always break large features into smaller, independent PRs
- **DELETE_MERGED_BRANCHES**: Always delete branches after they are merged
- **UPDATE_FROM_MAIN**: Always update feature branches from main at least daily
- **DOCUMENT_RULE_BYPASS**: Always document when rules are bypassed and why

## Error Handling Rules (High Priority)
- **FOLLOW_ERROR_PATHS**: Always follow defined error handling paths in procedures
- **DOCUMENT_NEW_ERRORS**: Always document errors not covered by existing paths
- **PROVIDE_RECOVERY_OPTIONS**: Always provide viable recovery options for errors
- **ISOLATE_FAILURES**: Always isolate failures to prevent cascading effects
- **PRESERVE_STATE**: Always preserve system state when handling errors
- **ESCALATE_BY_SEVERITY**: Always escalate errors based on severity and user impact
- **LOG_ERROR_DETAILS**: Always log detailed error information for analysis
- **UPDATE_ERROR_PROCEDURES**: Always update procedures based on observed errors

## Communication Rules (Medium Priority)
- **DOCUMENT_COORDINATION_STRATEGY**: Always document coordination strategy when file overlap exists
- **UPDATE_LINEAR_TICKETS**: Always keep Linear tickets updated with current status
- **DEFINE_ACCEPTANCE_CRITERIA**: Always ensure tickets have clear acceptance criteria
- **LINK_PRS_TO_TICKETS**: Always link PRs to corresponding Linear tickets
- **USE_PR_TEMPLATES**: Always follow PR template with all required sections
- **DOCUMENT_DECISIONS**: Always document important implementation decisions
- **COMMUNICATE_BLOCKERS**: Always communicate blockers and dependencies proactively
- **SEPARATE_PROBLEM_FROM_IMPLEMENTATION**: Always separate problem description from implementation details

## Operational Rules (Varies by Task)
- **START_SIMPLE**: Start with the simplest possible cause for any issue
- **ESCALATE_INCREMENTALLY**: Escalate diagnostic complexity incrementally
- **PROPOSE_SIMPLE_SOLUTIONS**: Propose simple solutions before complex ones
- **DEFINE_MINIMAL_SCOPE**: Define minimal viable scope that solves core need
- **DOCUMENT_DISCREPANCIES**: Document discrepancies between ticket status and work
- **CREATE_TICKETS_FOR_CHANGES**: Create new tickets for significant or out-of-scope changes
- **IDENTIFY_DEPENDENCY_ORDER**: Identify dependency order between overlapping PRs
- **CHECK_ACTIVE_BRANCHES**: Check active branches before creating tickets/branches
- **SAVE_SESSION_STATE**: Save session state before switching context
- **COMMIT_WIP**: Commit work-in-progress changes with [WIP] prefix
- **CLEAN_CODE_BEFORE_FINALIZING**: Clean up code before finalizing (remove debug statements)
- **SQUASH_WIP_COMMITS**: Squash WIP commits into logical units
- **VERIFY_AGAINST_CRITERIA**: Verify implementation against acceptance criteria
- **SHOW_THINKING_STEPS**: Share your thinking out loud and show steps as you work through them

## Procedure Execution (All Tasks)
- **SAVE_COMPREHENSIVE_STATE**: Save comprehensive session state before ending sessions
- **USE_MEMORY_TOOL**: Use memory tool for storing and retrieving information
- **APPLY_STRUCTURED_THINKING**: Apply structured thinking for complex problems
- **VERIFY_FILE_CONFLICTS**: Verify potential file conflicts before starting work
- **BALANCE_THOROUGHNESS_WITH_EFFICIENCY**: Balance thoroughness with efficiency based on task complexity
- **VISUALIZE_PROCEDURE_EXECUTION**: Show your progress through procedures with clear status indicators
- **SUMMARIZE_OUTCOMES**: Summarize outcomes after completing procedures