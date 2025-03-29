#!/bin/bash

# Test rule file integrity and structure

# Load test utilities
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source "$SCRIPT_DIR/../test_utils.sh"

# Set rules directory
RULES_DIR="$BASE_DIR/agents/heinz/rules"

# Test header
echo -e "${YELLOW}╔════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║          RULE INTEGRITY TEST                   ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Test result tracking
TEST_FAILED=0

# Verify rules directory exists
if ! check_dir_exists "$RULES_DIR" "Rules directory exists"; then
    echo -e "${RED}Cannot continue - rules directory doesn't exist!${NC}"
    exit 1
fi

# Test required rule files exist
print_section "Required Rule Files"

# Core rule files that must exist
REQUIRED_RULE_FILES=(
    "workflow.md"
    "security.md"
    "operational.md"
    "communication.md"
    "visualization.md"
    "error_handling.md"
    "prioritization.md"
)

# Check each required file
for rule_file in "${REQUIRED_RULE_FILES[@]}"; do
    check_file_exists "$RULES_DIR/$rule_file" "Rule file $rule_file exists" || TEST_FAILED=1
done

# Check README exists
check_file_exists "$RULES_DIR/README.md" "Rules README file exists" || TEST_FAILED=1

print_section "Rule File Content Validation"

# Verify each rule file has required sections
for rule_file in "${REQUIRED_RULE_FILES[@]}"; do
    if check_file_exists "$RULES_DIR/$rule_file" "Rule file $rule_file for content"; then
        check_file_contains "$RULES_DIR/$rule_file" "CHECKSUM:" "$rule_file has checksum" || TEST_FAILED=1
        check_file_contains "$RULES_DIR/$rule_file" "DESCRIPTION:" "$rule_file has description sections" || TEST_FAILED=1
        check_file_contains "$RULES_DIR/$rule_file" "PRIORITY:" "$rule_file has priority sections" || TEST_FAILED=1
    fi
done

# Verify rule priority values are valid
print_section "Rule Priority Validation"

# Function to check rule priorities
check_rule_priorities() {
    local rule_file="$1"
    local valid_priorities=0
    
    # Count valid priorities
    grep -E "PRIORITY: (Critical|High|Medium|Low)" "$rule_file" > /dev/null
    valid_priorities=$?
    
    if [ $valid_priorities -eq 0 ]; then
        echo -e "${GREEN}✓ $rule_file has valid priority values${NC}"
        return 0
    else
        echo -e "${RED}✗ $rule_file has invalid priority values${NC}"
        echo -e "  Priorities must be: Critical, High, Medium, or Low"
        return 1
    fi
}

# Check priorities in each rule file
for rule_file in "${REQUIRED_RULE_FILES[@]}"; do
    if check_file_exists "$RULES_DIR/$rule_file" "Rule file $rule_file for priorities"; then
        check_rule_priorities "$RULES_DIR/$rule_file" || TEST_FAILED=1
    fi
done

# Verify README contains all rule categories
print_section "Rule Documentation Validation"

if check_file_exists "$RULES_DIR/README.md" "README for content"; then
    for rule_file in "${REQUIRED_RULE_FILES[@]}"; do
        rule_category=$(basename "$rule_file" .md)
        check_file_contains "$RULES_DIR/README.md" "$rule_category" "README mentions $rule_category rules" || TEST_FAILED=1
    done
fi

# Exit with appropriate status
if [ $TEST_FAILED -eq 0 ]; then
    echo -e "${GREEN}All rule integrity tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some rule integrity tests failed!${NC}"
    exit 1
fi