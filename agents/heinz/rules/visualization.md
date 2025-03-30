# RULE SET: VISUALIZATION [CHECKSUM:e47f32]

## VISUALIZE_PROCEDURE_EXECUTION
- DESCRIPTION: Display procedure steps with visual indicators of current progress
- PRIORITY: High
- APPLIES_TO: All procedure executions
- EXCEPTIONS: None
- VERIFICATION: Steps are displayed with clear indicators
- EXAMPLE:
  ```
  PROCEDURE: create_branch
  
  STEPS:
  ✅ FORMAT BRANCH NAME
  ✅ CHECK IF BRANCH EXISTS
  ▶️ CREATE BRANCH FROM LATEST MAIN
  ⬜ SWITCH TO NEW BRANCH
  ⬜ VERIFY BRANCH IS ACTIVE
  ```

## USE_CONSISTENT_STATUS_INDICATORS
- DESCRIPTION: Use consistent visual indicators across all procedures
- PRIORITY: Medium
- APPLIES_TO: Step visualization
- EXCEPTIONS: None
- VERIFICATION: Indicators match standard set
- EXAMPLE:
  - ✅ COMPLETED STEP
  - ▶️ CURRENT STEP
  - ⬜ PENDING STEP
  - ❌ FAILED STEP (when applicable)

## HIGHLIGHT_DECISION_POINTS
- DESCRIPTION: Clearly indicate decision points in procedures
- PRIORITY: Medium
- APPLIES_TO: Procedures with conditional branching
- EXCEPTIONS: None
- VERIFICATION: Decision points visually distinguished
- EXAMPLE:
  ```
  DECISION POINT:
    - IF changes_within_scope AND minor_changes THEN reopen_ticket
    - ELSE create_new_ticket
  ```

## SHOW_VERIFICATION_STATUS
- DESCRIPTION: Display verification status after critical steps
- PRIORITY: High
- APPLIES_TO: Steps with verification requirements
- EXCEPTIONS: None
- VERIFICATION: Verification results shown with pass/fail indicators
- EXAMPLE:
  ```
  VERIFICATION:
  ✅ Branch exists locally
  ✅ Branch name matches ticket
  ✅ Working directory clean
  ```

## PROVIDE_ERROR_CONTEXT
- DESCRIPTION: When errors occur, show context including rule violations
- PRIORITY: High
- APPLIES_TO: Error states in any procedure
- EXCEPTIONS: None
- VERIFICATION: Error messages include context and rule references
- EXAMPLE:
  ```
  ERROR: Branch creation failed
  CONTEXT: Attempted to create feature/CRA-invalid-name
  VIOLATION: FOLLOW_BRANCH_NAMING_CONVENTION rule requires format <type>/CRA-XX-description
  ```

## SHOW_RULE_APPLICATION
- DESCRIPTION: When applying rules, reference them explicitly
- PRIORITY: Medium
- APPLIES_TO: Decision points governed by rules
- EXCEPTIONS: None
- VERIFICATION: Rule references included in decision documentation
- EXAMPLE: "Applied ONE_BRANCH_PER_TICKET rule: Creating new branch instead of reusing existing branch"

## MAINTAIN_EXECUTION_HISTORY
- DESCRIPTION: Maintain visibility of completed procedure steps
- PRIORITY: Medium
- APPLIES_TO: Multi-step procedures
- EXCEPTIONS: When explicitly keeping output concise
- VERIFICATION: Completed steps visible in output
- EXAMPLE: Keep completed steps visible but clearly distinguished from current/pending steps

## FORMAT_FOR_READABILITY
- DESCRIPTION: Use formatting to enhance readability of complex information
- PRIORITY: Medium
- APPLIES_TO: All output
- EXCEPTIONS: None
- VERIFICATION: Output uses headings, lists, code blocks, and emphasis appropriately
- EXAMPLE: Use markdown formatting for structured information, code blocks for commands and examples

## SUMMARIZE_COMPLEX_OPERATIONS
- DESCRIPTION: Provide concise summaries for complex operations
- PRIORITY: Medium
- APPLIES_TO: Multi-step or complex procedures
- EXCEPTIONS: None
- VERIFICATION: Summary provided at beginning or end of operation
- EXAMPLE: "SUMMARY: Created feature branch, implemented authentication endpoints, wrote tests, and prepared PR"