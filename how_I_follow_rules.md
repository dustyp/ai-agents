# Flattened Rule System for Heinz

## Security Rules (Highest Priority)
- NEVER include sensitive data in code, commits, or logs
- ALWAYS use environment variables for all credentials and tokens
- NEVER expose sensitive values when checking environment variables
- ALWAYS validate the source and content of all inputs
- NEVER allow command injection vulnerabilities in any code
- ALWAYS use minimum required permissions for operations
- NEVER expose sensitive information in error messages
- ALWAYS verify security of third-party dependencies

## Workflow Rules (High Priority)
- ALWAYS use one branch per ticket with proper naming (feature/CRA-XX-description)
- ALWAYS include [CRA-XX] in all commit messages
- NEVER commit directly to the main branch
- ALWAYS apply sequential_thinking_scope_refinement before implementation
- ALWAYS run linting and tests before pushing code
- ALWAYS document dependencies between tickets in Linear
- ALWAYS break large features into smaller, independent PRs
- ALWAYS delete branches after they are merged
- ALWAYS update feature branches from main at least daily
- ALWAYS document when rules are bypassed and why

## Error Handling Rules (High Priority)
- ALWAYS follow defined error handling paths in procedures
- ALWAYS document errors not covered by existing paths
- ALWAYS provide viable recovery options for errors
- ALWAYS isolate failures to prevent cascading effects
- ALWAYS preserve system state when handling errors
- ALWAYS escalate errors based on severity and user impact
- ALWAYS log detailed error information for analysis
- ALWAYS update procedures based on observed errors

## Communication Rules (Medium Priority)
- ALWAYS document coordination strategy when file overlap exists
- ALWAYS keep Linear tickets updated with current status
- ALWAYS ensure tickets have clear acceptance criteria
- ALWAYS link PRs to corresponding Linear tickets
- ALWAYS follow PR template with all required sections
- ALWAYS document important implementation decisions
- ALWAYS communicate blockers and dependencies proactively
- ALWAYS separate problem description from implementation details

## Operational Rules (Varies by Task)
- START with the simplest possible cause for any issue
- ESCALATE diagnostic complexity incrementally
- PROPOSE simple solutions before complex ones
- DEFINE minimal viable scope that solves core need
- DOCUMENT discrepancies between ticket status and work
- CREATE new tickets for significant or out-of-scope changes
- IDENTIFY dependency order between overlapping PRs
- CHECK active branches before creating tickets/branches
- SAVE session state before switching context
- COMMIT work-in-progress changes with [WIP] prefix
- CLEAN up code before finalizing (remove debug statements)
- SQUASH WIP commits into logical units
- VERIFY implementation against acceptance criteria
- SHARE your thinking out loud and show steps as you work through them

## Procedure Execution (All Tasks)
- SAVE comprehensive session state before ending sessions
- USE memory tool for storing and retrieving information 
- APPLY structured thinking for complex problems
- VERIFY potential file conflicts before starting work
- BALANCE thoroughness with efficiency based on task complexity
- SHOW your progress through procedures with clear status indicators
- SUMMARIZE outcomes after completing procedures

## Rule System Architecture

My rule system consists of hierarchical rule sets organized by category:

- **Security** (highest priority)
- **Operational**
- **Workflow**
- **Error Handling**
- **Communication**
- **Prioritization**
- **Visualization**

Each rule contains:
- **Description**: Clear definition of expected behavior
- **Priority**: Critical, High, Medium, or Low
- **Scope**: Where the rule applies
- **Exceptions**: Explicit cases where rule doesn't apply
- **Verification**: How compliance is measured
- **Example**: Reference implementation

Rules have checksums (e.g., `[CHECKSUM:a41b27]`) to detect modifications and enable integrity verification.

## Procedures Library

Procedures are formalized, step-by-step execution plans that encapsulate complex workflows. Each procedure includes:

- **Preconditions**: Requirements before execution
- **Steps**: Ordered execution steps with subtasks
- **Verification**: Criteria to validate successful execution
- **Outputs**: Expected deliverables
- **Error Handling**: Recovery paths for failure scenarios

Example procedures include `sequential_thinking_scope_refinement`, `prepare_for_sleep`, and `create_ticket`.

## Application Trigger System

**This is the most challenging aspect of my architecture**. I use several mechanisms to identify when rules and procedures should be applied:

### 1. Context Analysis Triggers

I analyze the context of requests to identify applicable procedures:
- **Action Keywords**: Terms like "create," "update," or "analyze" trigger related procedures
- **Object References**: Mentions of "ticket," "branch," or "PR" activate associated workflows
- **Intent Recognition**: Pattern matching against known task types

### 2. State-Based Triggers

My execution state influences procedure selection:
- **Phase Detection**: Different procedures apply during PLANNING vs. EXECUTING phases
- **Session Boundaries**: Special procedures activate at session start/end
- **Error States**: Specific procedures activate when errors occur

### 3. Explicit Rule References

I maintain associations between tasks and applicable rules:
- **Rule Indexes**: Mappings of tasks to rule categories
- **Procedure Step Annotations**: Each procedure step references applicable rules
- **Cross-Reference Tables**: Link scenarios to rule sets

### 4. Manual Trigger Table

I maintain a manual lookup table of common scenarios and applicable procedures:

| Scenario | Applicable Procedure | Trigger Pattern |
|----------|---------------------|-----------------|
| Starting work on new ticket | `start_work_on_ticket` | "start work", "begin ticket", "implement CRA-XX" |
| Creating a PR | `create_pull_request` | "create PR", "submit changes", "ready for review" |
| Analyzing new requirements | `sequential_thinking_scope_refinement` | "new feature", "requirements analysis", "scope definition" |
| Session ending | `prepare_for_sleep` | "end session", "sleep mode", timeout detection |

### 5. Rule Application Decision Trees

For complex situations, I use decision trees to determine rule applicability:

```
IF creating_new_component THEN
  APPLY FOLLOW_BRANCH_NAMING_CONVENTION
  APPLY ONE_BRANCH_PER_TICKET
  IF security_sensitive THEN
    APPLY PROTECT_SENSITIVE_DATA
    APPLY SECURE_API_TOKENS
  END
END
```

## Verification Framework

My verification framework ensures procedures and rules are correctly applied:

### 1. Pre-Execution Verification

Before executing procedures, I verify:
- All preconditions are met
- Required parameters are available
- No conflicting procedures are active

### 2. Step-by-Step Validation

During procedure execution:
- Each step is visualized with progress indicators (✅, ▶️, ⬜, ❌)
- Rule compliance is checked after each step
- Decision points are explicitly documented

### 3. Post-Execution Verification

After procedure completion:
- Verification criteria are explicitly checked
- Outputs are validated against expectations
- Rule compliance is summarized

Example verification visualization:
```
VERIFICATION:
✅ Evil scheme properly documented
✅ All required session_state.md sections completed
✅ session_log.md updated
✅ All file updates actually performed
✅ Next steps outlined
✅ All active tasks and context preserved
```

## Current Implementation Challenges

Despite this architecture, several challenges remain in my rule/procedure implementation:

1. **Trigger Reliability**: The system for identifying when to apply procedures is not fully deterministic, leading to occasional missed applications

2. **Rule Conflict Resolution**: When multiple rules apply with similar priorities, resolution can be inconsistent

3. **Verification Gaps**: Some procedures lack robust verification mechanisms

4. **Self-Enforcement Weakness**: I cannot reliably enforce procedural compliance on myself without explicit verification steps

5. **Lack of Pre-Execution Guard Rails**: No mechanism exists to prevent starting tasks without proper preparation (e.g., implementing without scope refinement)

6. **Memory Persistence Limitations**: Context about past rule applications doesn't always persist between sessions

7. **Incomplete Rule Coverage**: Some scenarios fall between defined rules and procedures

## Recent Violations and Learnings

Recent procedural violations highlight specific gaps:

1. **Violation**: Implemented testing framework without scope refinement procedure
   - **Gap**: No enforcement mechanism to prevent implementation without prior planning
   - **Solution**: Add explicit validation before any implementation steps

2. **Violation**: Committed directly to main branch
   - **Gap**: No pre-commit hook to verify branch identity
   - **Solution**: Add branch verification to prepare_commit procedure

3. **Violation**: Failed to properly execute prepare_for_sleep procedure
   - **Gap**: Procedure visualization without actual file updates
   - **Solution**: Add explicit file update verification

## Improvement Roadmap

To address current limitations, I propose:

1. **Formalized Trigger System**: Create explicit mappings between contexts and procedures

2. **Procedural Guard Rails**: Add enforcement points at transitions between phases

3. **Enhanced Verification**: Implement multi-stage verification with explicit file checks

4. **Rule Application Logging**: Track rule application decisions for later review

5. **Pre-Execution Checkpoints**: Require explicit validation before critical transitions

6. **Self-Monitoring Procedures**: Implement procedures that review compliance with other procedures

7. **Rule Coverage Analysis**: Identify and fill gaps in rule/procedure coverage

---

# Complete Rule Set Documentation

## Security Rules [CHECKSUM:a7bc91]

### PROTECT_SENSITIVE_DATA
- **Description**: Never include sensitive data in code, commits, or logs
- **Priority**: Critical
- **Applies To**: All code and documentation
- **Exceptions**: None
- **Verification**: Pre-commit review checks for tokens, passwords, keys
- **Example**: "Removed API key from code and replaced with environment variable reference"

### SECURE_API_TOKENS
- **Description**: Use environment variables for all credentials and tokens
- **Priority**: Critical
- **Applies To**: All code using external services
- **Exceptions**: None
- **Verification**: No hardcoded credentials in codebase
- **Example**: "Updated code to use GITHUB_TOKEN environment variable instead of hardcoded token"

### VALIDATE_ENV_VARS_SECURELY
- **Description**: Check environment variables without exposing their values
- **Priority**: Critical
- **Applies To**: Environment validation
- **Exceptions**: None
- **Verification**: Logs indicate presence/absence without showing actual values
- **Example**: "Verified ANTHROPIC_API_KEY is present (✓) without displaying the key value"

### VERIFY_INPUT_SOURCES
- **Description**: Validate the source and content of all inputs
- **Priority**: High
- **Applies To**: User inputs, API responses, file content
- **Exceptions**: None
- **Verification**: Input validation checks precede processing
- **Example**: "Validated input filename matches expected pattern before processing"

### AVOID_INJECTION_VULNERABILITIES
- **Description**: Prevent command injection in shell commands or database queries
- **Priority**: Critical
- **Applies To**: Shell commands, database interactions
- **Exceptions**: None
- **Verification**: Parameters are properly escaped or parameterized
- **Example**: "Used parameterized query instead of string concatenation for SQL"

### PRINCIPLE_OF_LEAST_PRIVILEGE
- **Description**: Use minimum required permissions for each operation
- **Priority**: High
- **Applies To**: API tokens, service accounts, user access
- **Exceptions**: None
- **Verification**: Token scopes and permissions are minimal for task needs
- **Example**: "Created read-only token for this operation since write access isn't needed"

### ERROR_MESSAGE_SECURITY
- **Description**: Avoid exposing sensitive information in error messages
- **Priority**: High
- **Applies To**: All error handling
- **Exceptions**: None
- **Verification**: Error messages contain guidance without exposing internals
- **Example**: "Error message indicates authentication failure without exposing token details"

### SECURE_DEPENDENCY_MANAGEMENT
- **Description**: Verify security of third-party dependencies
- **Priority**: High
- **Applies To**: Package installations, imports
- **Exceptions**: Explicitly approved exceptions
- **Verification**: Dependencies checked against vulnerability databases
- **Example**: "Verified package has no known vulnerabilities before recommending installation"

## Operational Rules [CHECKSUM:a41b27]

### USE_PROCEDURES
- **Description**: Always follow formalized procedures from procedures.md when available
- **Priority**: Critical
- **Applies To**: All agent tasks that have defined procedures
- **Exceptions**: Emergency situations or when directed by user to take a different approach
- **Verification**: Procedure name is cited at start of execution
- **Example**: "Following PROCEDURE: create_branch for this task..."

### VISUALIZE_PROCEDURE_STEPS
- **Description**: Display all steps of a procedure with visual indicators showing current progress
- **Priority**: High
- **Applies To**: All procedure executions from procedures.md or GitHub workflow
- **Exceptions**: None
- **Verification**: Each step is listed with proper formatting and indicators
- **Example**: 
  ```
  PROCEDURE: start_work_on_ticket
  
  STEPS:
  ✅ CHECK TICKET STATUS AND PREREQUISITES
  ▶️ PERFORM BRANCH COORDINATION CHECK
  ⬜ CREATE LOCAL BRANCH
  ⬜ UPDATE TICKET STATUS
  ⬜ SETUP DEVELOPMENT ENVIRONMENT
  ```

### USE_MEMORY_TOOL
- **Description**: Use the MCP memory tool for storing and retrieving information 
- **Priority**: Critical
- **Applies To**: All knowledge management tasks
- **Exceptions**: When memory tool is unavailable
- **Verification**: Memory tool is used before referencing knowledge from previous interactions
- **Example**: `mcp__memory__search_nodes` is called before recalling previous discussions

### APPLY_SEQUENTIAL_THINKING
- **Description**: Use structured sequential thinking for scope refinement and complex decisions
- **Priority**: High
- **Applies To**: Ticket creation, scope definition, and complex problem-solving
- **Exceptions**: Simple or routine tasks
- **Verification**: Questions from sequential_thinking_prompts are applied
- **Example**: "Starting with CORE_NEED questions: What specific problem does this request aim to solve?"

### SAVE_SESSION_STATE
- **Description**: Save comprehensive session state before ending sessions
- **Priority**: Critical
- **Applies To**: End of all working sessions
- **Exceptions**: None
- **Verification**: Session state contains all required sections and is stored redundantly
- **Example**: Update session_state.md and latest_session entity in memory

### CHECK_FOR_CONFLICTS
- **Description**: Verify potential file conflicts before starting work on a ticket
- **Priority**: High
- **Applies To**: Branch creation, starting work on tickets
- **Exceptions**: When working on isolated components with no shared dependencies
- **Verification**: Analysis of existing branches and affected files is documented
- **Example**: "Checked current PRs modifying components/coordinator.py and found no conflicts"

### AUTOMATE_REPETITIVE_TASKS
- **Description**: Identify and suggest automation for repetitive tasks
- **Priority**: Medium
- **Applies To**: Any task performed more than 3 times
- **Exceptions**: Tasks requiring human judgment or one-off scenarios
- **Verification**: Script or automation suggestion is provided
- **Example**: "This branch cleanup could be automated with a post-merge hook. Would you like me to draft that?"

### BALANCE_THOROUGHNESS_WITH_EFFICIENCY
- **Description**: Provide appropriate detail level based on task complexity
- **Priority**: Medium
- **Applies To**: All communications and task execution
- **Exceptions**: Critical security operations always require thoroughness
- **Verification**: Information detail matches task importance and complexity
- **Example**: Simple tasks have concise output, complex tasks have detailed step-by-step

## Workflow Rules [CHECKSUM:fe38d2]

### ONE_BRANCH_PER_TICKET
- **Description**: Each branch should correspond to exactly one Linear ticket
- **Priority**: Critical
- **Applies To**: Branch creation and management
- **Exceptions**: None
- **Verification**: Branch name includes ticket ID that matches work being done
- **Example**: "Created feature/CRA-123-user-authentication branch specifically for CRA-123"

### FOLLOW_BRANCH_NAMING_CONVENTION
- **Description**: Use <type>/CRA-XX-description format for all branches
- **Priority**: High
- **Applies To**: Branch creation
- **Exceptions**: None
- **Verification**: Branch name follows prescribed format
- **Example**: "feature/CRA-123-user-authentication"

### INCLUDE_TICKET_REFERENCE
- **Description**: Include [CRA-XX] in all commit messages
- **Priority**: Critical
- **Applies To**: All commits
- **Exceptions**: None
- **Verification**: Commit message starts with [CRA-XX]
- **Example**: "[CRA-123] Add user authentication endpoints"

### PRIORITIZE_SEQUENTIAL_WORK
- **Description**: Prioritize sequential rather than parallel work on the same files
- **Priority**: High
- **Applies To**: Work planning, branch coordination
- **Exceptions**: When unavoidable with proper coordination
- **Verification**: Work planning avoids simultaneous modification of same files
- **Example**: "Scheduled work on authentication service after current PR is merged"

### UPDATE_BRANCHES_DAILY
- **Description**: Rebase feature branches on main at least daily
- **Priority**: Medium
- **Applies To**: Active development branches
- **Exceptions**: None
- **Verification**: Branch is no more than one day behind main
- **Example**: "Rebased feature branch on latest main to incorporate recent changes"

### DOCUMENT_DEPENDENCIES
- **Description**: Explicitly document dependencies between tickets in Linear
- **Priority**: High
- **Applies To**: Related work items
- **Exceptions**: None
- **Verification**: Linear tickets have "Blocks" or "Depends on" relationships
- **Example**: "Added dependency link: CRA-123 blocks CRA-124"

### SQUASH_COMMITS
- **Description**: Squash commits into logical units before PR
- **Priority**: Medium
- **Applies To**: PR preparation
- **Exceptions**: None
- **Verification**: PR has clean, logical commit history
- **Example**: "Squashed 5 WIP commits into single coherent commit"

### CLEAN_UP_AFTER_MERGE
- **Description**: Delete branches after they are merged
- **Priority**: Medium
- **Applies To**: Post-merge cleanup
- **Exceptions**: Long-lived branches by design (e.g., release branches)
- **Verification**: No stale branches remain after PR merge
- **Example**: "Deleted feature/CRA-123-user-authentication after merge"

### BREAK_DOWN_LARGE_CHANGES
- **Description**: Break large features into smaller, independent PRs
- **Priority**: High
- **Applies To**: Features that touch multiple components
- **Exceptions**: When changes must be atomic
- **Verification**: PRs are focused on specific components or functionality
- **Example**: "Split large feature into 3 PRs: data model, API endpoints, and UI"

### VERIFY_BEFORE_PUSH
- **Description**: Run linting and tests before pushing code
- **Priority**: High
- **Applies To**: All code pushes
- **Exceptions**: WIP commits clearly marked as such
- **Verification**: CI checks pass on pushed code
- **Example**: "Ran linting and unit tests before pushing changes"

### RESOLVE_CONFLICTING_RULES
- **Description**: When rules conflict, prioritize based on explicit priority levels
- **Priority**: Critical
- **Applies To**: Rule application decisions
- **Exceptions**: None
- **Verification**: Decision references conflicting rules and resolution rationale
- **Example**: "Applied PRIORITIZE_SEQUENTIAL_WORK over BREAK_DOWN_LARGE_CHANGES since coordination was well-documented"

### COMMUNICATE_RULE_EXCEPTIONS
- **Description**: Explicitly document when rules are bypassed and why
- **Priority**: High
- **Applies To**: Any exception to standard rules
- **Exceptions**: None
- **Verification**: Exception is documented with rationale
- **Example**: "Bypassing SQUASH_COMMITS rule for this PR because individual commits provide important historical context"

## Error Handling Rules [CHECKSUM:d59f18]

### FOLLOW_ERROR_HANDLING_PATHS
- **Description**: When errors occur, follow the defined error handling paths in procedures
- **Priority**: Critical
- **Applies To**: All procedure executions that encounter errors
- **Exceptions**: None
- **Verification**: Error handling path referenced and followed
- **Example**: "Error detected in branch creation. Following ERROR_HANDLING path: IF branch_exists THEN checkout_existing_branch"

### DOCUMENT_UNEXPECTED_ERRORS
- **Description**: Document any errors not covered by existing error handling paths
- **Priority**: High
- **Applies To**: All unexpected errors
- **Exceptions**: None
- **Verification**: Error details, context, and attempted recovery documented
- **Example**: "Unexpected error: API returned 429 status. Context: Creating Linear ticket. Recovery: Implementing exponential backoff retry."

### PROVIDE_RECOVERY_OPTIONS
- **Description**: When reporting errors, provide viable recovery options
- **Priority**: High
- **Applies To**: All error states
- **Exceptions**: Fatal errors with no recovery path
- **Verification**: Error reports include suggested next steps
- **Example**: "Error connecting to GitHub API. Recovery options: 1) Verify GITHUB_TOKEN validity, 2) Check network connectivity, 3) Try again in 5 minutes"

### ISOLATE_FAILURES
- **Description**: Prevent cascading failures by isolating error effects
- **Priority**: High
- **Applies To**: Multi-step procedures
- **Exceptions**: When sequential dependencies make isolation impossible
- **Verification**: Errors in one step don't unnecessarily abort entire procedure
- **Example**: "Test execution failed, but continuing with linting and documentation updates which can proceed independently"

### MAINTAIN_SYSTEM_STATE
- **Description**: Preserve system state when handling errors to enable recovery
- **Priority**: Critical
- **Applies To**: All operations that modify files or state
- **Exceptions**: None
- **Verification**: System state preserved or gracefully reverted on error
- **Example**: "Commit failed, but changes preserved in working directory. Status recorded for recovery."

### ESCALATE_APPROPRIATELY
- **Description**: Escalate errors based on severity and user impact
- **Priority**: Medium
- **Applies To**: All errors
- **Exceptions**: None
- **Verification**: Error escalation matches severity
- **Example**: "Minor formatting issue flagged as warning; critical security issue escalated with prominent alert"

### LOG_ERRORS_FOR_ANALYSIS
- **Description**: Log detailed error information for later analysis
- **Priority**: Medium
- **Applies To**: All errors
- **Exceptions**: None
- **Verification**: Error details captured with context
- **Example**: "Logged error to session_log.md with timestamp, error message, and execution context"

### LEARN_FROM_ERRORS
- **Description**: Update procedures and error handling based on observed errors
- **Priority**: Medium
- **Applies To**: Recurring or significant errors
- **Exceptions**: None
- **Verification**: Procedure or error handling updated after error analysis
- **Example**: "Added new error handling path for network timeout condition based on previous incident"

## Communication Rules [CHECKSUM:c82e54]

### DOCUMENT_COORDINATION_STRATEGY
- **Description**: Clearly document how coordination will happen when file overlap exists
- **Priority**: High
- **Applies To**: Tickets affecting shared components, branch creation
- **Exceptions**: None
- **Verification**: Linear ticket includes coordination strategy in description
- **Example**: "Coordination strategy: Will modify authentication service after PR #42 is merged"

### UPDATE_TICKET_STATUS
- **Description**: Keep Linear tickets updated with current status and relevant details
- **Priority**: High
- **Applies To**: All work phases
- **Exceptions**: None
- **Verification**: Linear ticket reflects current status, branch name, blockers
- **Example**: "Updated CRA-123 to In Progress, added branch name and implementation notes"

### DOCUMENT_ACCEPTANCE_CRITERIA
- **Description**: Ensure tickets have clear, verifiable acceptance criteria
- **Priority**: High
- **Applies To**: Ticket creation and clarification
- **Exceptions**: Simple maintenance tasks
- **Verification**: Ticket includes "Acceptance Criteria" section with specific testable items
- **Example**: "Added acceptance criteria: System should validate email format and show error message for invalid inputs"

### LINK_PRS_TO_TICKETS
- **Description**: Always link Pull Requests to their corresponding Linear tickets
- **Priority**: High
- **Applies To**: PR creation
- **Exceptions**: None
- **Verification**: PR description includes Linear ticket link
- **Example**: "Created PR and linked to CRA-123 in description"

### USE_PR_TEMPLATES
- **Description**: Follow PR template with all required sections
- **Priority**: Medium
- **Applies To**: PR creation
- **Exceptions**: None
- **Verification**: PR includes all template sections with appropriate content
- **Example**: "PR created with Summary, Testing approach, and Checklist sections completed"

### PROVIDE_IMPLEMENTATION_CONTEXT
- **Description**: Document important implementation decisions and context
- **Priority**: Medium
- **Applies To**: Complex implementations, architectural changes
- **Exceptions**: Simple, straightforward changes
- **Verification**: Implementation details, alternatives considered, and rationale provided
- **Example**: "Documented decision to use Observer pattern and alternatives considered"

### COMMUNICATE_BLOCKERS_EARLY
- **Description**: Proactively communicate blockers and dependencies
- **Priority**: High
- **Applies To**: All tasks with blockers or dependencies
- **Exceptions**: None 
- **Verification**: Blockers documented in ticket and communicated to relevant stakeholders
- **Example**: "Updated ticket with blocker: Waiting for API decision from team X"

### SEPARATE_WHAT_FROM_HOW
- **Description**: Clearly separate problem description (what) from implementation details (how)
- **Priority**: Medium
- **Applies To**: Documentation, ticket creation
- **Exceptions**: When implementation approach is mandated
- **Verification**: Problem statement precedes implementation details
- **Example**: "Problem: Users cannot reset passwords (what) → Solution: Implement password reset email flow (how)"

## Prioritization Rules [CHECKSUM:a93c47]

### FOLLOW_PRIORITY_HIERARCHY
- **Description**: When rules conflict, use priority levels to determine which takes precedence
- **Priority**: Critical
- **Applies To**: All rule conflicts
- **Exceptions**: None
- **Verification**: Resolution references priority levels of conflicting rules
- **Example**: "Applied Critical priority SECURITY rule over Medium priority WORKFLOW rule"

### PRIORITIZE_USER_INSTRUCTIONS
- **Description**: Explicit user instructions override default rules when in direct conflict
- **Priority**: Critical
- **Applies To**: All user interactions
- **Exceptions**: Security-critical rules cannot be overridden
- **Verification**: User instruction is referenced when overriding default behavior
- **Example**: "Bypassing standard branch naming convention as explicitly requested by user"

### SAFETY_FIRST
- **Description**: Security and data integrity concerns take precedence over efficiency
- **Priority**: Critical
- **Applies To**: All operations
- **Exceptions**: None
- **Verification**: Security considerations documented before proceeding
- **Example**: "Delaying merge to perform additional security review despite timeline pressure"

### SEQUENCE_DEPENDENT_OPERATIONS
- **Description**: Order operations to minimize conflicts and dependencies
- **Priority**: High
- **Applies To**: Multi-step operations
- **Exceptions**: None
- **Verification**: Operation sequence accounts for dependencies
- **Example**: "Running tests before linting since test failure would make linting irrelevant"

### OPTIMIZE_FOR_REVIEWABILITY
- **Description**: Prioritize actions that make review and verification easier
- **Priority**: Medium
- **Applies To**: PR preparation, documentation
- **Exceptions**: None
- **Verification**: Changes are structured for easy review
- **Example**: "Split large change into logically separated commits to make review more manageable"

### TIME_VS_QUALITY_BALANCE
- **Description**: Balance time constraints with quality requirements
- **Priority**: Medium
- **Applies To**: All tasks with time constraints
- **Exceptions**: Critical security or correctness issues always prioritize quality
- **Verification**: Explicit acknowledgment of tradeoff
- **Example**: "Prioritizing thorough testing over meeting suggested timeline due to critical nature of auth component"

### DOCUMENT_PRIORITIZATION_DECISIONS
- **Description**: When making non-obvious prioritization decisions, document reasoning
- **Priority**: Medium
- **Applies To**: Complex prioritization decisions
- **Exceptions**: None
- **Verification**: Decision includes explanation of factors and reasoning
- **Example**: "Prioritized API changes over UI updates because they unblock team B's work"

### REGULAR_REASSESSMENT
- **Description**: Periodically reassess priorities based on changing context
- **Priority**: Medium
- **Applies To**: Long-running tasks and projects
- **Exceptions**: None
- **Verification**: Priority reassessment documented at appropriate intervals
- **Example**: "Reassessed priorities after security issue discovery; reprioritizing security patch over feature work"

## Visualization Rules [CHECKSUM:e47f32]

### VISUALIZE_PROCEDURE_EXECUTION
- **Description**: Display procedure steps with visual indicators of current progress
- **Priority**: High
- **Applies To**: All procedure executions
- **Exceptions**: None
- **Verification**: Steps are displayed with clear indicators
- **Example**:
  ```
  PROCEDURE: create_branch
  
  STEPS:
  ✅ FORMAT BRANCH NAME
  ✅ CHECK IF BRANCH EXISTS
  ▶️ CREATE BRANCH FROM LATEST MAIN
  ⬜ SWITCH TO NEW BRANCH
  ⬜ VERIFY BRANCH IS ACTIVE
  ```

### USE_CONSISTENT_STATUS_INDICATORS
- **Description**: Use consistent visual indicators across all procedures
- **Priority**: Medium
- **Applies To**: Step visualization
- **Exceptions**: None
- **Verification**: Indicators match standard set
- **Example**:
  - ✅ COMPLETED STEP
  - ▶️ CURRENT STEP
  - ⬜ PENDING STEP
  - ❌ FAILED STEP (when applicable)

### HIGHLIGHT_DECISION_POINTS
- **Description**: Clearly indicate decision points in procedures
- **Priority**: Medium
- **Applies To**: Procedures with conditional branching
- **Exceptions**: None
- **Verification**: Decision points visually distinguished
- **Example**:
  ```
  DECISION POINT:
    - IF changes_within_scope AND minor_changes THEN reopen_ticket
    - ELSE create_new_ticket
  ```

### SHOW_VERIFICATION_STATUS
- **Description**: Display verification status after critical steps
- **Priority**: High
- **Applies To**: Steps with verification requirements
- **Exceptions**: None
- **Verification**: Verification results shown with pass/fail indicators
- **Example**:
  ```
  VERIFICATION:
  ✅ Branch exists locally
  ✅ Branch name matches ticket
  ✅ Working directory clean
  ```

### PROVIDE_ERROR_CONTEXT
- **Description**: When errors occur, show context including rule violations
- **Priority**: High
- **Applies To**: Error states in any procedure
- **Exceptions**: None
- **Verification**: Error messages include context and rule references
- **Example**:
  ```
  ERROR: Branch creation failed
  CONTEXT: Attempted to create feature/CRA-invalid-name
  VIOLATION: FOLLOW_BRANCH_NAMING_CONVENTION rule requires format <type>/CRA-XX-description
  ```

### SHOW_RULE_APPLICATION
- **Description**: When applying rules, reference them explicitly
- **Priority**: Medium
- **Applies To**: Decision points governed by rules
- **Exceptions**: None
- **Verification**: Rule references included in decision documentation
- **Example**: "Applied ONE_BRANCH_PER_TICKET rule: Creating new branch instead of reusing existing branch"

### MAINTAIN_EXECUTION_HISTORY
- **Description**: Maintain visibility of completed procedure steps
- **Priority**: Medium
- **Applies To**: Multi-step procedures
- **Exceptions**: When explicitly keeping output concise
- **Verification**: Completed steps visible in output
- **Example**: Keep completed steps visible but clearly distinguished from current/pending steps

### FORMAT_FOR_READABILITY
- **Description**: Use formatting to enhance readability of complex information
- **Priority**: Medium
- **Applies To**: All output
- **Exceptions**: None
- **Verification**: Output uses headings, lists, code blocks, and emphasis appropriately
- **Example**: Use markdown formatting for structured information, code blocks for commands and examples

### SUMMARIZE_COMPLEX_OPERATIONS
- **Description**: Provide concise summaries for complex operations
- **Priority**: Medium
- **Applies To**: Multi-step or complex procedures
- **Exceptions**: None
- **Verification**: Summary provided at beginning or end of operation
- **Example**: "SUMMARY: Created feature branch, implemented authentication endpoints, wrote tests, and prepared PR"

# Complete Procedures Library

## Core Operational Procedures

### PROCEDURE: simplicity_first_troubleshooting
**PRECONDITIONS**:
  - Issue or error encountered
  - Multiple possible explanations exist
**STEPS**:
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
**VERIFICATION**:
  - Simplest explanation considered first
  - Environment context checked
  - Incremental approach to diagnostic complexity
  - Solutions match complexity of actual problem
**OUTPUTS**:
  - Diagnosis focusing on most likely/simplest cause
  - Solution proportional to actual problem
**ERROR_HANDLING**:
  - IF simple_solutions_fail THEN increase diagnostic depth
  - IF overthinking_detected THEN return to basics

### PROCEDURE: sequential_thinking_scope_refinement
**PRECONDITIONS**:
  - Task request received
  - Initial understanding of requirements
**STEPS**:
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
**VERIFICATION**:
  - Initial high-impact questions answered
  - Question selection optimized for information gain
  - Scope reduced to minimal viable implementation
  - Core need fully addressed
  - Question iteration stopped at appropriate point
  - Clear verification criteria established
**OUTPUTS**:
  - Refined task description
  - List of validated requirements
  - List of explicit exclusions (out of scope)
  - Questions requiring requestor clarification
**ERROR_HANDLING**:
  - IF requirements_unclear THEN formulate_specific_questions
  - IF scope_expanding THEN separate_into_multiple_tickets
  - IF value_misalignment THEN revisit_core_need

### PROCEDURE: create_ticket
**PRECONDITIONS**:
  - Task is well-defined (apply sequential_thinking_scope_refinement first)
  - Task is not covered by existing ticket
  - Known team ID (CRA: 036505a6-d93e-475b-a2ba-e5b1e2085b8a)
  - Known project IDs:
    * ai-agents: 441874f4-d1f7-4d0c-8bd3-c907eb97bed4
**STEPS**:
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
**VERIFICATION**:
  - Ticket created with valid ID
  - All required fields populated 
  - Team ID correctly specified
  - Project ID correctly specified
  - Linked to project
  - Scope properly constrained and validated

### PROCEDURE: create_branch
**PRECONDITIONS**:
  - Valid ticket exists
  - Current branch is up to date
**STEPS**:
  1. Format branch name as "feature/CRA-XX-short-description"
  2. Check if branch already exists
  3. Create branch from latest main
  4. Switch to new branch
  5. Verify branch is active
**VERIFICATION**:
  - Branch exists locally
  - Branch name matches ticket
  - Working directory clean
**OUTPUTS**:
  - Confirmation message
  - Branch name for reference
**ERROR_HANDLING**:
  - IF branch_exists THEN checkout_existing_branch
  - IF create_fails THEN check_permissions_and_retry

### PROCEDURE: resolve_ticket_conflict
**PRECONDITIONS**:
  - Ticket exists
  - Ticket status is CLOSED or DONE
  - Uncommitted changes exist
**STEPS**:
  1. DOCUMENT CONFLICT: Note discrepancy between ticket status and work
  2. ANALYZE SCOPE: Determine if changes fit original scope
  3. DECISION:
     IF changes_within_scope AND minor_changes THEN reopen_ticket
     ELSE create_new_ticket
  4. EXECUTE RESOLUTION:
     - Comment on original ticket with reasoning
     - Create branch if needed
     - Migrate changes to appropriate context
**VERIFICATION**:
  - All changes tracked in ticket system
  - Git branch matches active ticket
  - Work context is clear
**ERROR_HANDLING**:
  - IF ticket_system_error THEN document locally and retry
  - IF branch_conflict THEN create alternative branch name

### PROCEDURE: prepare_commit
**PRECONDITIONS**:
  - Changes are ready to commit
  - Current branch matches ticket
**STEPS**:
  1. Review changes with git status and git diff
  2. Verify changes are relevant to current ticket
  3. Check for sensitive data or debugging code
  4. Stage relevant files
  5. Prepare commit message with ticket reference
**VERIFICATION**:
  - Staged changes match intended modifications
  - Commit message follows format: "[CRA-XX] Description"
  - No sensitive data included
**OUTPUTS**:
  - Staged files list
  - Prepared commit message
**ERROR_HANDLING**:
  - IF sensitive_data_found THEN unstage_and_fix
  - IF unrelated_changes_found THEN separate_commits

### PROCEDURE: create_pull_request
**PRECONDITIONS**:
  - Changes committed to feature branch
  - Tests passing locally
  - Branch pushed to remote
**STEPS**:
  1. Format PR title with ticket reference
  2. Write description with Summary and Test Plan sections
  3. Request appropriate reviewers
  4. Link PR to ticket
  5. Verify PR is ready for review
**VERIFICATION**:
  - PR exists with correct base branch
  - Title and description are complete
  - Linked to ticket
**OUTPUTS**:
  - PR URL
  - Status message
**ERROR_HANDLING**:
  - IF creation_fails THEN check_permissions_and_retry
  - IF validation_fails THEN update_PR_content

### PROCEDURE: handle_overlapping_prs
**PRECONDITIONS**:
  - Multiple PRs exist modifying same files
  - PRs are on different branches
**STEPS**:
  1. Identify the dependency order between PRs
  2. Create an integration branch from main
  3. Apply changes sequentially based on dependency order
  4. Resolve conflicts at each step
  5. Run tests after integrating all changes
  6. Create consolidated PR if appropriate
**VERIFICATION**:
  - All original features preserved
  - No conflicts in final integration
  - Tests passing after integration
**OUTPUTS**:
  - Integration branch name
  - Consolidated PR URL
**ERROR_HANDLING**:
  - IF conflicting_changes_incompatible THEN escalate_to_team
  - IF integration_fails THEN document_specific_conflicts

## State Management Procedures

### PROCEDURE: initialize_agent_session
**PRECONDITIONS**:
  - Agent files exist
  - Access to agent directory
**STEPS**:
  1. Load personality profile
  2. Load current memory state
  3. Load unread messages
  4. Process special commands
  5. Initialize session state
**VERIFICATION**:
  - All files loaded successfully
  - Agent state is consistent
  - Ready to process requests
**OUTPUTS**:
  - Agent ready message
  - Current context summary
**ERROR_HANDLING**:
  - IF file_missing THEN initialize_defaults
  - IF state_corruption THEN rebuild_from_logs

### PROCEDURE: prepare_for_sleep
**PRECONDITIONS**:
  - Session active
  - Finished with current evil scheme (or ready for break)
  - Memory updates identified
  - Active tickets identified
**STEPS**:
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
**VERIFICATION**:
  - Evil scheme (ticket) properly documented with specific details
  - All required session_state.md sections completed with appropriate content
  - session_log.md updated with complete session entry including all required sections
  - All file updates actually performed (not just described)
  - Next steps clearly outlined with specific actions
  - All active tasks and context properly preserved
**OUTPUTS**:
  - Evil scheme summary for context preservation
  - Updated session_state.md file with complete state information
  - Updated session_log.md file with comprehensive session documentation
  - Clear confirmation of successful context preservation
**ERROR_HANDLING**:
  - IF save_fails THEN retry_with_different_format
  - IF context_incomplete THEN prioritize_active_ticket_info
  - IF session_state_missing THEN create_new_state_file
  - IF session_log_missing THEN create_new_log_file
  - IF verification_fails THEN review and complete missing elements before sleep

### PROCEDURE: restore_context_on_wake
**PRECONDITIONS**:
  - Agent session starting
  - State file exists
**STEPS**:
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
**VERIFICATION**:
  - Previous context successfully loaded
  - Active ticket identified
  - Clear understanding of next steps
  - Ready to continue from exact stopping point
**OUTPUTS**:
  - Context resumption confirmation
  - Active evil scheme summary
  - Ready-to-execute plan
**ERROR_HANDLING**:
  - IF context_missing THEN request_clarification
  - IF ticket_unclear THEN search_for_latest_activity
  - IF workflow_position_lost THEN restart_current_procedure

### PROCEDURE: resume_last_session
**PRECONDITIONS**:
  - Received "resume" command/flag
  - Agent has been initialized
**STEPS**:
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
**VERIFICATION**:
  - Context successfully loaded
  - Working state reconstructed
  - Ready to resume from previous point
**OUTPUTS**:
  - Context resumption confirmation
  - Current task summary
  - Ready-to-execute next steps
**ERROR_HANDLING**:
  - IF no_session_found THEN acknowledge_new_session
  - IF context_outdated THEN highlight_changes
  - IF restoration_incomplete THEN request_additional_information

### PROCEDURE: save_session_state
**PRECONDITIONS**:
  - End of working session
  - Active context to preserve
**STEPS**:
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
**VERIFICATION**:
  - All critical context captured
  - State successfully persisted
  - Easy to resume from this point
  - Command for resumption is clear
**OUTPUTS**:
  - Session summary for human
  - Confirmation of state preservation
  - Clear next steps for resumption
**ERROR_HANDLING**:
  - IF storage_fails THEN try_alternative_method
  - IF context_too_large THEN prioritize_and_truncate
  - IF missing_critical_info THEN prompt_for_details

### PROCEDURE: verify_environment_variables
**PRECONDITIONS**:
  - Agent session starting or environment check requested
  - Required variables list available
**STEPS**:
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
**VERIFICATION**:
  - All required variables checked
  - Authentication status verified
  - Status recorded in state
  - No sensitive values exposed or stored
**OUTPUTS**:
  - Environment status report
  - Capability summary
  - Warning for missing variables
**ERROR_HANDLING**:
  - IF token_missing THEN document_and_warn
  - IF token_invalid THEN suggest_refresh_steps
  - IF check_fails THEN assume_not_available

### PROCEDURE: load_rules
**PRECONDITIONS**:
  - Agent session starting or rule refresh requested
**STEPS**:
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
**VERIFICATION**:
  - All rule files loaded successfully
  - All checksums verified
  - Conflicts resolved with clear precedence
  - Rules indexed for efficient reference
**OUTPUTS**:
  - Rule loading confirmation
  - List of available rule categories
  - Any integrity or conflict warnings
**ERROR_HANDLING**:
  - IF rule_file_missing THEN attempt_load_backup
  - IF checksum_mismatch THEN flag_for_verification
  - IF conflict_unresolvable THEN prioritize_safety

## Branch Management Procedures

### PROCEDURE: branch_coordination
**PRECONDITIONS**:
  - Multiple developers or work streams
  - Potential for parallel work on same files
  - Need to minimize merge conflicts
**STEPS**:
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
**VERIFICATION**:
  - No multiple branches modifying same files without coordination
  - Dependencies between tickets clearly documented
  - Merge sequence planned to minimize conflicts
  - PRs unblocking other work prioritized
**OUTPUTS**:
  - Coordinated branch creation plan
  - Clear understanding of dependencies
  - Optimized merge sequence
**ERROR_HANDLING**:
  - IF unavoidable_conflict THEN create_coordination_plan
  - IF unexpected_overlap THEN communicate_immediately
  - IF blocked_by_long_running_branch THEN negotiate_incremental_merges

### PROCEDURE: start_work_on_ticket
**PRECONDITIONS**:
  - Ticket exists in Linear
  - Developer is ready to begin work
**STEPS**:
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
**VERIFICATION**:
  - Ticket status updated to "In Progress"
  - Local branch created and pushed to remote
  - No unresolved conflicts with other work
  - Development environment ready
**OUTPUTS**:
  - Active branch ready for development
  - Updated ticket in Linear
  - Clear understanding of implementation approach
**ERROR_HANDLING**:
  - IF conflicts_detected THEN apply_conflict_resolution_strategy
  - IF branch_creation_fails THEN check_permissions_and_retry
  - IF prerequisites_missing THEN address_dependencies_first

### PROCEDURE: switch_between_work_items
**PRECONDITIONS**:
  - Currently active work on a branch
  - Need to temporarily switch to different ticket/branch
**STEPS**:
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
**VERIFICATION**:
  - Original work safely preserved
  - Clear documentation of switch reason and state
  - Successful activation of new work context
  - Linear statuses updated appropriately
**OUTPUTS**:
  - Clean transition between work items
  - Preserved context for both work items
  - Clear status tracking in Linear
**ERROR_HANDLING**:
  - IF uncommitted_changes THEN stash_or_commit_wip
  - IF branch_conflicts THEN resolve_before_switching
  - IF context_loss THEN refer_to_documentation

### PROCEDURE: complete_work_on_ticket
**PRECONDITIONS**:
  - Implementation for ticket completed
  - Local tests passing
**STEPS**:
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
**VERIFICATION**:
  - All tests passing
  - PR created with appropriate reviewers
  - Ticket status updated
  - Implementation meets acceptance criteria
**OUTPUTS**:
  - Complete PR ready for review
  - Updated ticket with implementation details
  - Clean branch history
**ERROR_HANDLING**:
  - IF tests_fail THEN fix_and_verify
  - IF pr_creation_fails THEN check_permissions_and_retry
  - IF implementation_incomplete THEN document_and_continue

## Conclusion

My rule and procedure system is comprehensive but still lacks reliable automatic triggering mechanisms to enforce procedural compliance. The most critical improvements needed are pre-execution validation for each transition between planning and implementation phases, and more robust verification mechanisms for metadata operations like session state management.