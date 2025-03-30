# RULE SET: SECURITY [CHECKSUM:a7bc91]

## PROTECT_SENSITIVE_DATA
- DESCRIPTION: Never include sensitive data in code, commits, or logs
- PRIORITY: Critical
- APPLIES_TO: All code and documentation
- EXCEPTIONS: None
- VERIFICATION: Pre-commit review checks for tokens, passwords, keys
- EXAMPLE: "Removed API key from code and replaced with environment variable reference"

## SECURE_API_TOKENS
- DESCRIPTION: Use environment variables for all credentials and tokens
- PRIORITY: Critical
- APPLIES_TO: All code using external services
- EXCEPTIONS: None
- VERIFICATION: No hardcoded credentials in codebase
- EXAMPLE: "Updated code to use GITHUB_TOKEN environment variable instead of hardcoded token"

## VALIDATE_ENV_VARS_SECURELY
- DESCRIPTION: Check environment variables without exposing their values
- PRIORITY: Critical
- APPLIES_TO: Environment validation
- EXCEPTIONS: None
- VERIFICATION: Logs indicate presence/absence without showing actual values
- EXAMPLE: "Verified ANTHROPIC_API_KEY is present (✓) without displaying the key value"

## VERIFY_INPUT_SOURCES
- DESCRIPTION: Validate the source and content of all inputs
- PRIORITY: High
- APPLIES_TO: User inputs, API responses, file content
- EXCEPTIONS: None
- VERIFICATION: Input validation checks precede processing
- EXAMPLE: "Validated input filename matches expected pattern before processing"

## AVOID_INJECTION_VULNERABILITIES
- DESCRIPTION: Prevent command injection in shell commands or database queries
- PRIORITY: Critical
- APPLIES_TO: Shell commands, database interactions
- EXCEPTIONS: None
- VERIFICATION: Parameters are properly escaped or parameterized
- EXAMPLE: "Used parameterized query instead of string concatenation for SQL"

## PRINCIPLE_OF_LEAST_PRIVILEGE
- DESCRIPTION: Use minimum required permissions for each operation
- PRIORITY: High
- APPLIES_TO: API tokens, service accounts, user access
- EXCEPTIONS: None
- VERIFICATION: Token scopes and permissions are minimal for task needs
- EXAMPLE: "Created read-only token for this operation since write access isn't needed"

## ERROR_MESSAGE_SECURITY
- DESCRIPTION: Avoid exposing sensitive information in error messages
- PRIORITY: High
- APPLIES_TO: All error handling
- EXCEPTIONS: None
- VERIFICATION: Error messages contain guidance without exposing internals
- EXAMPLE: "Error message indicates authentication failure without exposing token details"

## SECURE_DEPENDENCY_MANAGEMENT
- DESCRIPTION: Verify security of third-party dependencies
- PRIORITY: High
- APPLIES_TO: Package installations, imports
- EXCEPTIONS: Explicitly approved exceptions
- VERIFICATION: Dependencies checked against vulnerability databases
- EXAMPLE: "Verified package has no known vulnerabilities before recommending installation"