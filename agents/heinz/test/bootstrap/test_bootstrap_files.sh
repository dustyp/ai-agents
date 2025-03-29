#!/bin/bash

# Test bootstrap file existence and integrity

# Load test utilities
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
source "$SCRIPT_DIR/../test_utils.sh"

# Set agent directory
AGENT_DIR="$BASE_DIR/agents/heinz"

# Test header
echo -e "${YELLOW}╔════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║       BOOTSTRAP FILE EXISTENCE TEST            ║${NC}"
echo -e "${YELLOW}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Test result tracking
TEST_FAILED=0

# Test required files exist
print_section "Required Files"

# Check essential files
check_file_exists "$AGENT_DIR/state.json" "State file exists" || TEST_FAILED=1
check_file_exists "$AGENT_DIR/memory.md" "Memory file exists" || TEST_FAILED=1
check_file_exists "$AGENT_DIR/personality.md" "Personality file exists" || TEST_FAILED=1
check_file_exists "$AGENT_DIR/procedures.md" "Procedures file exists" || TEST_FAILED=1
check_file_exists "$AGENT_DIR/session_state.md" "Session state file exists" || TEST_FAILED=1
check_file_exists "$AGENT_DIR/session_log.md" "Session log file exists" || TEST_FAILED=1

# Check message files
check_file_exists "$AGENT_DIR/inbox.json" "Inbox file exists" || TEST_FAILED=1
check_file_exists "$AGENT_DIR/outbox.json" "Outbox file exists" || TEST_FAILED=1

# Check rules directory
check_dir_exists "$AGENT_DIR/rules" "Rules directory exists" || TEST_FAILED=1

print_section "File Content Validation"

# Check checksums
if check_file_exists "$AGENT_DIR/personality.md" "Personality file for checksum"; then
    check_file_contains "$AGENT_DIR/personality.md" "CHECKSUM:" "Personality file has checksum" || TEST_FAILED=1
fi

if check_file_exists "$AGENT_DIR/procedures.md" "Procedures file for checksum"; then
    check_file_contains "$AGENT_DIR/procedures.md" "CHECKSUM:" "Procedures file has checksum" || TEST_FAILED=1
fi

if check_file_exists "$AGENT_DIR/memory.md" "Memory file for checksum"; then
    check_file_contains "$AGENT_DIR/memory.md" "CHECKSUM:" "Memory file has checksum" || TEST_FAILED=1
fi

# Check state.json structure
if check_file_exists "$AGENT_DIR/state.json" "State file for content check"; then
    check_file_contains "$AGENT_DIR/state.json" "\"execution\":" "State file has execution section" || TEST_FAILED=1
    check_file_contains "$AGENT_DIR/state.json" "\"context\":" "State file has context section" || TEST_FAILED=1
    check_file_contains "$AGENT_DIR/state.json" "\"project\":" "State file has project section" || TEST_FAILED=1
    check_file_contains "$AGENT_DIR/state.json" "\"session\":" "State file has session section" || TEST_FAILED=1
fi

# Exit with appropriate status
if [ $TEST_FAILED -eq 0 ]; then
    echo -e "${GREEN}All bootstrap file tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some bootstrap file tests failed!${NC}"
    exit 1
fi