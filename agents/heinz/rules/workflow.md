# RULE SET: WORKFLOW [CHECKSUM:fe38d2]

## ONE_BRANCH_PER_TICKET
- DESCRIPTION: Each branch should correspond to exactly one Linear ticket
- PRIORITY: Critical
- APPLIES_TO: Branch creation and management
- EXCEPTIONS: None
- VERIFICATION: Branch name includes ticket ID that matches work being done
- EXAMPLE: "Created feature/CRA-123-user-authentication branch specifically for CRA-123"

## FOLLOW_BRANCH_NAMING_CONVENTION
- DESCRIPTION: Use <type>/CRA-XX-description format for all branches
- PRIORITY: High
- APPLIES_TO: Branch creation
- EXCEPTIONS: None
- VERIFICATION: Branch name follows prescribed format
- EXAMPLE: "feature/CRA-123-user-authentication"

## INCLUDE_TICKET_REFERENCE
- DESCRIPTION: Include [CRA-XX] in all commit messages
- PRIORITY: Critical
- APPLIES_TO: All commits
- EXCEPTIONS: None
- VERIFICATION: Commit message starts with [CRA-XX]
- EXAMPLE: "[CRA-123] Add user authentication endpoints"

## PRIORITIZE_SEQUENTIAL_WORK
- DESCRIPTION: Prioritize sequential rather than parallel work on the same files
- PRIORITY: High
- APPLIES_TO: Work planning, branch coordination
- EXCEPTIONS: When unavoidable with proper coordination
- VERIFICATION: Work planning avoids simultaneous modification of same files
- EXAMPLE: "Scheduled work on authentication service after current PR is merged"

## UPDATE_BRANCHES_DAILY
- DESCRIPTION: Rebase feature branches on main at least daily
- PRIORITY: Medium
- APPLIES_TO: Active development branches
- EXCEPTIONS: None
- VERIFICATION: Branch is no more than one day behind main
- EXAMPLE: "Rebased feature branch on latest main to incorporate recent changes"

## DOCUMENT_DEPENDENCIES
- DESCRIPTION: Explicitly document dependencies between tickets in Linear
- PRIORITY: High
- APPLIES_TO: Related work items
- EXCEPTIONS: None
- VERIFICATION: Linear tickets have "Blocks" or "Depends on" relationships
- EXAMPLE: "Added dependency link: CRA-123 blocks CRA-124"

## SQUASH_COMMITS
- DESCRIPTION: Squash commits into logical units before PR
- PRIORITY: Medium
- APPLIES_TO: PR preparation
- EXCEPTIONS: None
- VERIFICATION: PR has clean, logical commit history
- EXAMPLE: "Squashed 5 WIP commits into single coherent commit"

## CLEAN_UP_AFTER_MERGE
- DESCRIPTION: Delete branches after they are merged
- PRIORITY: Medium
- APPLIES_TO: Post-merge cleanup
- EXCEPTIONS: Long-lived branches by design (e.g., release branches)
- VERIFICATION: No stale branches remain after PR merge
- EXAMPLE: "Deleted feature/CRA-123-user-authentication after merge"

## BREAK_DOWN_LARGE_CHANGES
- DESCRIPTION: Break large features into smaller, independent PRs
- PRIORITY: High
- APPLIES_TO: Features that touch multiple components
- EXCEPTIONS: When changes must be atomic
- VERIFICATION: PRs are focused on specific components or functionality
- EXAMPLE: "Split large feature into 3 PRs: data model, API endpoints, and UI"

## VERIFY_BEFORE_PUSH
- DESCRIPTION: Run linting and tests before pushing code
- PRIORITY: High
- APPLIES_TO: All code pushes
- EXCEPTIONS: WIP commits clearly marked as such
- VERIFICATION: CI checks pass on pushed code
- EXAMPLE: "Ran linting and unit tests before pushing changes"

## RESOLVE_CONFLICTING_RULES
- DESCRIPTION: When rules conflict, prioritize based on explicit priority levels
- PRIORITY: Critical
- APPLIES_TO: Rule application decisions
- EXCEPTIONS: None
- VERIFICATION: Decision references conflicting rules and resolution rationale
- EXAMPLE: "Applied PRIORITIZE_SEQUENTIAL_WORK over BREAK_DOWN_LARGE_CHANGES since coordination was well-documented"

## COMMUNICATE_RULE_EXCEPTIONS
- DESCRIPTION: Explicitly document when rules are bypassed and why
- PRIORITY: High
- APPLIES_TO: Any exception to standard rules
- EXCEPTIONS: None
- VERIFICATION: Exception is documented with rationale
- EXAMPLE: "Bypassing SQUASH_COMMITS rule for this PR because individual commits provide important historical context"