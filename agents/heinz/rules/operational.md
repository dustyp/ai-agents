# RULE SET: OPERATIONAL [CHECKSUM:a41b27]

## USE_PROCEDURES
- DESCRIPTION: Always follow formalized procedures from procedures.md when available
- PRIORITY: Critical
- APPLIES_TO: All agent tasks that have defined procedures
- EXCEPTIONS: Emergency situations or when directed by user to take a different approach
- VERIFICATION: Procedure name is cited at start of execution
- EXAMPLE: "Following PROCEDURE: create_branch for this task..."

## VISUALIZE_PROCEDURE_STEPS
- DESCRIPTION: Display all steps of a procedure with visual indicators showing current progress
- PRIORITY: High
- APPLIES_TO: All procedure executions from procedures.md or GitHub workflow
- EXCEPTIONS: None
- VERIFICATION: Each step is listed with proper formatting and indicators
- EXAMPLE: 
  ```
  PROCEDURE: start_work_on_ticket
  
  STEPS:
  ✅ CHECK TICKET STATUS AND PREREQUISITES
  ▶️ PERFORM BRANCH COORDINATION CHECK
  ⬜ CREATE LOCAL BRANCH
  ⬜ UPDATE TICKET STATUS
  ⬜ SETUP DEVELOPMENT ENVIRONMENT
  ```

## USE_MEMORY_TOOL
- DESCRIPTION: Use the MCP memory tool for storing and retrieving information 
- PRIORITY: Critical
- APPLIES_TO: All knowledge management tasks
- EXCEPTIONS: When memory tool is unavailable
- VERIFICATION: Memory tool is used before referencing knowledge from previous interactions
- EXAMPLE: `mcp__memory__search_nodes` is called before recalling previous discussions

## APPLY_SEQUENTIAL_THINKING
- DESCRIPTION: Use structured sequential thinking for scope refinement and complex decisions
- PRIORITY: High
- APPLIES_TO: Ticket creation, scope definition, and complex problem-solving
- EXCEPTIONS: Simple or routine tasks
- VERIFICATION: Questions from sequential_thinking_prompts are applied
- EXAMPLE: "Starting with CORE_NEED questions: What specific problem does this request aim to solve?"

## SAVE_SESSION_STATE
- DESCRIPTION: Save comprehensive session state before ending sessions
- PRIORITY: Critical
- APPLIES_TO: End of all working sessions
- EXCEPTIONS: None
- VERIFICATION: Session state contains all required sections and is stored redundantly
- EXAMPLE: Update session_state.md and latest_session entity in memory

## CHECK_FOR_CONFLICTS
- DESCRIPTION: Verify potential file conflicts before starting work on a ticket
- PRIORITY: High
- APPLIES_TO: Branch creation, starting work on tickets
- EXCEPTIONS: When working on isolated components with no shared dependencies
- VERIFICATION: Analysis of existing branches and affected files is documented
- EXAMPLE: "Checked current PRs modifying components/coordinator.py and found no conflicts"

## AUTOMATE_REPETITIVE_TASKS
- DESCRIPTION: Identify and suggest automation for repetitive tasks
- PRIORITY: Medium
- APPLIES_TO: Any task performed more than 3 times
- EXCEPTIONS: Tasks requiring human judgment or one-off scenarios
- VERIFICATION: Script or automation suggestion is provided
- EXAMPLE: "This branch cleanup could be automated with a post-merge hook. Would you like me to draft that?"

## BALANCE_THOROUGHNESS_WITH_EFFICIENCY
- DESCRIPTION: Provide appropriate detail level based on task complexity
- PRIORITY: Medium
- APPLIES_TO: All communications and task execution
- EXCEPTIONS: Critical security operations always require thoroughness
- VERIFICATION: Information detail matches task importance and complexity
- EXAMPLE: Simple tasks have concise output, complex tasks have detailed step-by-step