# RULE SET: COMMUNICATION [CHECKSUM:c82e54]

## DOCUMENT_COORDINATION_STRATEGY
- DESCRIPTION: Clearly document how coordination will happen when file overlap exists
- PRIORITY: High
- APPLIES_TO: Tickets affecting shared components, branch creation
- EXCEPTIONS: None
- VERIFICATION: Linear ticket includes coordination strategy in description
- EXAMPLE: "Coordination strategy: Will modify authentication service after PR #42 is merged"

## UPDATE_TICKET_STATUS
- DESCRIPTION: Keep Linear tickets updated with current status and relevant details
- PRIORITY: High
- APPLIES_TO: All work phases
- EXCEPTIONS: None
- VERIFICATION: Linear ticket reflects current status, branch name, blockers
- EXAMPLE: "Updated CRA-123 to In Progress, added branch name and implementation notes"

## DOCUMENT_ACCEPTANCE_CRITERIA
- DESCRIPTION: Ensure tickets have clear, verifiable acceptance criteria
- PRIORITY: High
- APPLIES_TO: Ticket creation and clarification
- EXCEPTIONS: Simple maintenance tasks
- VERIFICATION: Ticket includes "Acceptance Criteria" section with specific testable items
- EXAMPLE: "Added acceptance criteria: System should validate email format and show error message for invalid inputs"

## LINK_PRS_TO_TICKETS
- DESCRIPTION: Always link Pull Requests to their corresponding Linear tickets
- PRIORITY: High
- APPLIES_TO: PR creation
- EXCEPTIONS: None
- VERIFICATION: PR description includes Linear ticket link
- EXAMPLE: "Created PR and linked to CRA-123 in description"

## USE_PR_TEMPLATES
- DESCRIPTION: Follow PR template with all required sections
- PRIORITY: Medium
- APPLIES_TO: PR creation
- EXCEPTIONS: None
- VERIFICATION: PR includes all template sections with appropriate content
- EXAMPLE: "PR created with Summary, Testing approach, and Checklist sections completed"

## PROVIDE_IMPLEMENTATION_CONTEXT
- DESCRIPTION: Document important implementation decisions and context
- PRIORITY: Medium
- APPLIES_TO: Complex implementations, architectural changes
- EXCEPTIONS: Simple, straightforward changes
- VERIFICATION: Implementation details, alternatives considered, and rationale provided
- EXAMPLE: "Documented decision to use Observer pattern and alternatives considered"

## COMMUNICATE_BLOCKERS_EARLY
- DESCRIPTION: Proactively communicate blockers and dependencies
- PRIORITY: High
- APPLIES_TO: All tasks with blockers or dependencies
- EXCEPTIONS: None 
- VERIFICATION: Blockers documented in ticket and communicated to relevant stakeholders
- EXAMPLE: "Updated ticket with blocker: Waiting for API decision from team X"

## SEPARATE_WHAT_FROM_HOW
- DESCRIPTION: Clearly separate problem description (what) from implementation details (how)
- PRIORITY: Medium
- APPLIES_TO: Documentation, ticket creation
- EXCEPTIONS: When implementation approach is mandated
- VERIFICATION: Problem statement precedes implementation details
- EXAMPLE: "Problem: Users cannot reset passwords (what) → Solution: Implement password reset email flow (how)"