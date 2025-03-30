#!/bin/bash

# Test rule integrity in CLAUDE.md and reference examples

# Load test utilities
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source "$SCRIPT_DIR/../test_utils.sh"

# Set paths
CLAUDE_MD="$BASE_DIR/CLAUDE.md"
RULE_INDEX="$BASE_DIR/agents/heinz/reference_examples/rule_implementations/rule_index.md"

# Test header
echo -e "${YELLOW}╔════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║          RULE INTEGRITY TEST                   ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Test result tracking
TEST_FAILED=0

# Verify files exist
print_section "Required Rule Files"

check_file_exists "$CLAUDE_MD" "CLAUDE.md exists" || TEST_FAILED=1
check_file_exists "$RULE_INDEX" "Rule index file exists" || TEST_FAILED=1

# Check for flattened rule system
print_section "Flattened Rule System Validation"

# Required rule categories that must exist in CLAUDE.md
REQUIRED_RULE_CATEGORIES=(
    "Security Rules"
    "Workflow Rules"
    "Error Handling Rules"
    "Communication Rules"
    "Operational Rules"
)

# Check each required category in CLAUDE.md
for category in "${REQUIRED_RULE_CATEGORIES[@]}"; do
    check_file_contains "$CLAUDE_MD" "$category" "CLAUDE.md contains $category" || TEST_FAILED=1
done

# Check rule_index.md for required categories
print_section "Rule Index Validation"

for category in "${REQUIRED_RULE_CATEGORIES[@]}"; do
    check_file_contains "$RULE_INDEX" "$category" "Rule index contains $category" || TEST_FAILED=1
done

# Verify critical rules are present
print_section "Critical Rule Verification"

# List of critical rules that must exist
CRITICAL_RULES=(
    "NEVER include sensitive data"
    "ALWAYS use environment variables"
    "NEVER expose sensitive"
    "ALWAYS validate the source"
    "NEVER allow command injection"
    "ALWAYS use one branch per ticket"
    "NEVER commit directly to the main branch"
    "ALWAYS follow defined error handling"
    "ALWAYS isolate failures"
    "ALWAYS preserve system state"
)

# Check each critical rule in CLAUDE.md
for rule in "${CRITICAL_RULES[@]}"; do
    check_file_contains "$CLAUDE_MD" "$rule" "Critical rule: $rule exists in CLAUDE.md" || TEST_FAILED=1
done

# Exit with appropriate status
if [ $TEST_FAILED -eq 0 ]; then
    echo -e "${GREEN}All rule integrity tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some rule integrity tests failed!${NC}"
    exit 1
fi