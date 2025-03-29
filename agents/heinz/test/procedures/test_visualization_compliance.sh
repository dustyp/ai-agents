#!/bin/bash

# Test procedure visualization compliance

# Load test utilities
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source "$SCRIPT_DIR/../test_utils.sh"

# Set procedures file path
PROCEDURES_FILE="$BASE_DIR/agents/heinz/procedures.md"

# Test header
echo -e "${YELLOW}╔════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║      PROCEDURE VISUALIZATION TEST              ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Test result tracking
TEST_FAILED=0

# Verify procedures file exists
if ! check_file_exists "$PROCEDURES_FILE" "Procedures file exists"; then
    echo -e "${RED}Cannot continue - procedures file doesn't exist!${NC}"
    exit 1
fi

# List of procedures that should have visualization
VISUALIZATION_REQUIRED=(
    "sequential_thinking_scope_refinement"
    "branch_coordination"
    "handle_overlapping_prs"
    "prepare_for_sleep"
    "load_rules"
    "create_pull_request"
    "start_work_on_ticket"
)

print_section "Procedure Visualization Compliance"

# Function to check if a procedure has visualization
check_procedure_visualization() {
    local procedure_name="$1"
    local found=0
    
    # Look for the procedure and check if it has example visualization
    awk -v proc="PROCEDURE: $procedure_name" '
        $0 ~ proc {found=1}
        found && $0 ~ /EXAMPLE VISUALIZATION/ {visualized=1; exit}
        /^PROCEDURE:/ && found {found=0}
        END {exit !(found && visualized)}
    ' "$PROCEDURES_FILE"
    
    local result=$?
    
    if [ $result -eq 0 ]; then
        echo -e "${GREEN}✓ $procedure_name has visualization example${NC}"
        return 0
    else
        echo -e "${RED}✗ $procedure_name is missing visualization example${NC}"
        return 1
    fi
}

# Check each required procedure
for procedure in "${VISUALIZATION_REQUIRED[@]}"; do
    check_procedure_visualization "$procedure" || TEST_FAILED=1
done

print_section "Visualization Formatting Compliance"

# Check if visualizations use the correct status indicators
check_file_contains "$PROCEDURES_FILE" "✅" "Uses completed step indicator (✅)" || TEST_FAILED=1
check_file_contains "$PROCEDURES_FILE" "▶️" "Uses current step indicator (▶️)" || TEST_FAILED=1
check_file_contains "$PROCEDURES_FILE" "⬜" "Uses pending step indicator (⬜)" || TEST_FAILED=1

# Check if visualizations include decision points
check_file_contains "$PROCEDURES_FILE" "DECISION POINT:" "Includes decision points" || TEST_FAILED=1

# Check if visualizations include verification status
check_file_contains "$PROCEDURES_FILE" "VERIFICATION:" "Includes verification status" || TEST_FAILED=1

# Check if visualizations reference applied rules
check_file_contains "$PROCEDURES_FILE" "APPLIED RULES:" "References applied rules" || TEST_FAILED=1

# Exit with appropriate status
if [ $TEST_FAILED -eq 0 ]; then
    echo -e "${GREEN}All procedure visualization tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some procedure visualization tests failed!${NC}"
    exit 1
fi