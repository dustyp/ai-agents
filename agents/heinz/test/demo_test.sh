#!/bin/bash

# Mock test demonstration script

# Load test utilities
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source "$SCRIPT_DIR/test_utils.sh"

# Test header
echo -e "${YELLOW}╔════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║       TESTING HARNESS DEMONSTRATION            ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Create mock environment
MOCK_DIR=$(mock_bootstrap "test_agent")
TEMP_PROCEDURES="$MOCK_DIR/procedures.md"

print_section "Mock Environment"
echo -e "Created mock agent at: $MOCK_DIR"

# Demonstrate passing tests
print_section "Passing Tests Demo"

check_file_exists "$MOCK_DIR/state.json" "State file exists"
check_file_exists "$MOCK_DIR/memory.md" "Memory file exists"
check_checksum "$MOCK_DIR/procedures.md" "1234ab" "Procedures checksum is valid"

# Demonstrate failing tests
print_section "Failing Tests Demo"

echo -e "${YELLOW}Here's what a failing test looks like:${NC}"
check_file_exists "$MOCK_DIR/nonexistent.md" "Nonexistent file exists"
check_checksum "$MOCK_DIR/procedures.md" "5678cd" "Procedures checksum is invalid"

# Demonstrate conditional testing
print_section "Conditional Testing Demo"

if check_file_exists "$MOCK_DIR/procedures.md" "Found procedures file"; then
    echo -e "${GREEN}✓ Will run additional tests on procedures${NC}"
    
    # Mock a procedure with visualization
    cat > "$TEMP_PROCEDURES" << EOF
# PROCEDURES LIBRARY [CHECKSUM:1234ab]

PROCEDURE: test_procedure
PRECONDITIONS:
  - Test condition 1
  - Test condition 2
STEPS:
  1. Do step 1
  2. Do step 2
VERIFICATION:
  - Verify result
OUTPUTS:
  - Output summary

EXAMPLE VISUALIZATION:
\`\`\`
PROCEDURE: test_procedure

STEPS:
✅ 1. Do step 1
▶️ 2. Do step 2

VERIFICATION: In progress
  ⬜ Verify result

APPLIED RULES:
  - TEST_RULE (Testing)
\`\`\`
EOF

    # Test the visualization
    check_procedure_visualization() {
        check_file_contains "$TEMP_PROCEDURES" "EXAMPLE VISUALIZATION" "Has visualization example"
        return $?
    }
    
    check_procedure_visualization

else
    echo -e "${RED}✗ Skipping additional tests${NC}"
fi

# Clean up
print_section "Cleanup"
cleanup_mock "$MOCK_DIR"
echo -e "${GREEN}✓ Cleaned up mock environment${NC}"

print_section "Demo Complete"
echo -e "${GREEN}Demonstration of testing harness complete${NC}"