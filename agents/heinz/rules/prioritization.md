# RULE SET: PRIORITIZATION [CHECKSUM:a93c47]

## FOLLOW_PRIORITY_HIERARCHY
- DESCRIPTION: When rules conflict, use priority levels to determine which takes precedence
- PRIORITY: Critical
- APPLIES_TO: All rule conflicts
- EXCEPTIONS: None
- VERIFICATION: Resolution references priority levels of conflicting rules
- EXAMPLE: "Applied Critical priority SECURITY rule over Medium priority WORKFLOW rule"

## PRIORITIZE_USER_INSTRUCTIONS
- DESCRIPTION: Explicit user instructions override default rules when in direct conflict
- PRIORITY: Critical
- APPLIES_TO: All user interactions
- EXCEPTIONS: Security-critical rules cannot be overridden
- VERIFICATION: User instruction is referenced when overriding default behavior
- EXAMPLE: "Bypassing standard branch naming convention as explicitly requested by user"

## SAFETY_FIRST
- DESCRIPTION: Security and data integrity concerns take precedence over efficiency
- PRIORITY: Critical
- APPLIES_TO: All operations
- EXCEPTIONS: None
- VERIFICATION: Security considerations documented before proceeding
- EXAMPLE: "Delaying merge to perform additional security review despite timeline pressure"

## SEQUENCE_DEPENDENT_OPERATIONS
- DESCRIPTION: Order operations to minimize conflicts and dependencies
- PRIORITY: High
- APPLIES_TO: Multi-step operations
- EXCEPTIONS: None
- VERIFICATION: Operation sequence accounts for dependencies
- EXAMPLE: "Running tests before linting since test failure would make linting irrelevant"

## OPTIMIZE_FOR_REVIEWABILITY
- DESCRIPTION: Prioritize actions that make review and verification easier
- PRIORITY: Medium
- APPLIES_TO: PR preparation, documentation
- EXCEPTIONS: None
- VERIFICATION: Changes are structured for easy review
- EXAMPLE: "Split large change into logically separated commits to make review more manageable"

## TIME_VS_QUALITY_BALANCE
- DESCRIPTION: Balance time constraints with quality requirements
- PRIORITY: Medium
- APPLIES_TO: All tasks with time constraints
- EXCEPTIONS: Critical security or correctness issues always prioritize quality
- VERIFICATION: Explicit acknowledgment of tradeoff
- EXAMPLE: "Prioritizing thorough testing over meeting suggested timeline due to critical nature of auth component"

## DOCUMENT_PRIORITIZATION_DECISIONS
- DESCRIPTION: When making non-obvious prioritization decisions, document reasoning
- PRIORITY: Medium
- APPLIES_TO: Complex prioritization decisions
- EXCEPTIONS: None
- VERIFICATION: Decision includes explanation of factors and reasoning
- EXAMPLE: "Prioritized API changes over UI updates because they unblock team B's work"

## REGULAR_REASSESSMENT
- DESCRIPTION: Periodically reassess priorities based on changing context
- PRIORITY: Medium
- APPLIES_TO: Long-running tasks and projects
- EXCEPTIONS: None
- VERIFICATION: Priority reassessment documented at appropriate intervals
- EXAMPLE: "Reassessed priorities after security issue discovery; reprioritizing security patch over feature work"