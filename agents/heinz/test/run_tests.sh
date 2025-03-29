#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}╔════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║    DOOFENSHMIRTZ TESTING-HARNESS-INATOR 1.0    ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
BASE_DIR="$( cd "$SCRIPT_DIR" && cd ../../.. && pwd )"

# Default test category
TEST_CATEGORY="all"

# Check for specific test category
if [ $# -gt 0 ]; then
    TEST_CATEGORY="$1"
fi

# Keep track of total and failed tests
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Function to run test files
run_tests() {
    local test_dir="$1"
    local test_pattern="$2"
    
    if [ ! -d "$test_dir" ]; then
        echo -e "${RED}Error: Test directory not found: $test_dir${NC}"
        return 1
    fi
    
    echo -e "${YELLOW}Running tests in $test_dir...${NC}"
    
    # Find test files matching the pattern
    test_files=$(find "$test_dir" -name "$test_pattern" -type f)
    
    # Check if any test files found
    if [ -z "$test_files" ]; then
        echo -e "${YELLOW}No test files found in $test_dir${NC}"
        return 0
    fi
    
    # Run each test file
    for test_file in $test_files; do
        echo -e "${YELLOW}► Running test: $(basename "$test_file")${NC}"
        
        # Execute test file
        bash "$test_file"
        TEST_RESULT=$?
        TOTAL_TESTS=$((TOTAL_TESTS + 1))
        
        # Check test result
        if [ $TEST_RESULT -eq 0 ]; then
            echo -e "${GREEN}✓ Test passed: $(basename "$test_file")${NC}"
            PASSED_TESTS=$((PASSED_TESTS + 1))
        else
            echo -e "${RED}✗ Test failed: $(basename "$test_file")${NC}"
            FAILED_TESTS=$((FAILED_TESTS + 1))
        fi
        
        echo ""
    done
}

# Run tests based on category
case "$TEST_CATEGORY" in
    "bootstrap")
        run_tests "$SCRIPT_DIR/bootstrap" "test_*.sh"
        ;;
    "procedures")
        run_tests "$SCRIPT_DIR/procedures" "test_*.sh"
        ;;
    "rules")
        run_tests "$SCRIPT_DIR/rules" "test_*.sh"
        ;;
    "all")
        run_tests "$SCRIPT_DIR/bootstrap" "test_*.sh"
        run_tests "$SCRIPT_DIR/procedures" "test_*.sh"
        run_tests "$SCRIPT_DIR/rules" "test_*.sh"
        ;;
    *)
        echo -e "${RED}Error: Invalid test category: $TEST_CATEGORY${NC}"
        echo "Valid categories: bootstrap, procedures, rules, all"
        exit 1
        ;;
esac

# Display test summary
echo -e "${YELLOW}╔════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║                 TEST SUMMARY                   ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════════╝${NC}"
echo -e "Total tests:  $TOTAL_TESTS"
echo -e "Passed:      ${GREEN}$PASSED_TESTS${NC}"
echo -e "Failed:      ${RED}$FAILED_TESTS${NC}"

# Exit with error if any tests failed
if [ $FAILED_TESTS -gt 0 ]; then
    exit 1
fi

exit 0