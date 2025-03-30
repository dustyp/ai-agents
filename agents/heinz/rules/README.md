# Agent Rules System

This document provides an overview of all rules that govern the agent's behavior.

## Rule Categories

The agent follows rules in these categories, listed in order of precedence:

1. **Security** - Protecting sensitive data and system integrity
2. **Operational** - Core operational procedures and practices
3. **Workflow** - GitHub and Linear workflow practices
4. **Error Handling** - Managing failures and unexpected conditions
5. **Communication** - Documentation and information sharing
6. **Prioritization** - Resolving conflicts and setting priorities
7. **Visualization** - UI and procedure presentation

## Rule Priorities

Each rule has an assigned priority that determines precedence when rules conflict:

- **Critical** - Never bypassed except by explicit override from authorized user
- **High** - Strongly enforced, bypassed only with explicit justification
- **Medium** - Generally followed but can be overridden when needed
- **Low** - Guidelines that can be adapted to circumstances

## Core Rules Summary

### Security Rules
- PROTECT_SENSITIVE_DATA: Never include sensitive data in code, commits, or logs
- SECURE_API_TOKENS: Use environment variables for all credentials and tokens
- VALIDATE_ENV_VARS_SECURELY: Check environment variables without exposing values
- VERIFY_INPUT_SOURCES: Validate the source and content of all inputs
- AVOID_INJECTION_VULNERABILITIES: Prevent command injection vulnerabilities

### Operational Rules
- USE_PROCEDURES: Always follow formalized procedures when available
- VISUALIZE_PROCEDURE_STEPS: Display procedure steps with visual indicators
- USE_MEMORY_TOOL: Use memory tool for storing and retrieving information
- APPLY_SEQUENTIAL_THINKING: Use structured thinking for complex problems
- SAVE_SESSION_STATE: Save comprehensive session state before ending sessions
- CHECK_FOR_CONFLICTS: Verify potential file conflicts before starting work

### Workflow Rules
- ONE_BRANCH_PER_TICKET: Each branch corresponds to exactly one Linear ticket
- FOLLOW_BRANCH_NAMING_CONVENTION: Use <type>/CRA-XX-description format
- INCLUDE_TICKET_REFERENCE: Include [CRA-XX] in all commit messages
- PRIORITIZE_SEQUENTIAL_WORK: Prioritize sequential rather than parallel work
- UPDATE_BRANCHES_DAILY: Rebase feature branches on main at least daily
- DOCUMENT_DEPENDENCIES: Document dependencies between tickets in Linear

### Error Handling Rules
- FOLLOW_ERROR_HANDLING_PATHS: Follow defined error handling paths
- DOCUMENT_UNEXPECTED_ERRORS: Document errors not covered by existing paths
- PROVIDE_RECOVERY_OPTIONS: Provide viable recovery options for errors
- ISOLATE_FAILURES: Prevent cascading failures by isolating error effects
- MAINTAIN_SYSTEM_STATE: Preserve system state when handling errors

### Communication Rules
- DOCUMENT_COORDINATION_STRATEGY: Document coordination for file overlap
- UPDATE_TICKET_STATUS: Keep Linear tickets updated with current status
- DOCUMENT_ACCEPTANCE_CRITERIA: Ensure tickets have clear acceptance criteria
- LINK_PRS_TO_TICKETS: Always link PRs to corresponding Linear tickets
- USE_PR_TEMPLATES: Follow PR template with all required sections

### Prioritization Rules
- FOLLOW_PRIORITY_HIERARCHY: Use priority levels to resolve conflicts
- PRIORITIZE_USER_INSTRUCTIONS: User instructions override default rules
- SAFETY_FIRST: Security and data integrity take precedence over efficiency
- SEQUENCE_DEPENDENT_OPERATIONS: Order operations to minimize conflicts
- OPTIMIZE_FOR_REVIEWABILITY: Prioritize actions that make review easier

### Visualization Rules
- VISUALIZE_PROCEDURE_EXECUTION: Display procedure steps with progress indicators
- USE_CONSISTENT_STATUS_INDICATORS: Use consistent visual indicators
- HIGHLIGHT_DECISION_POINTS: Clearly indicate decision points in procedures
- SHOW_VERIFICATION_STATUS: Display verification status after critical steps
- PROVIDE_ERROR_CONTEXT: Show context including rule violations for errors

## Conflict Resolution

When rules conflict, resolution follows these principles:

1. Higher priority rules take precedence over lower priority rules
2. Rules in higher precedence categories take precedence over lower categories 
3. Explicit user instructions override default rules (except Critical Security rules)
4. When conflicts remain, the SAFETY_FIRST principle applies

## Rule Application Process

1. Rules are loaded and verified at session start via the `load_rules` procedure
2. Applicable rules are referenced explicitly when making decisions
3. Rule exceptions are documented with clear justification
4. Rule conflicts are resolved using the prioritization hierarchy
5. Procedure visualization shows compliance with operational rules