#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
BASE_DIR="$( cd "$SCRIPT_DIR" && cd ../../.. && pwd )"

# Function to check if a file exists
check_file_exists() {
    local file_path="$1"
    local message="$2"
    
    if [ -f "$file_path" ]; then
        echo -e "${GREEN}✓ $message${NC}"
        return 0
    else
        echo -e "${RED}✗ $message${NC}"
        echo -e "  File not found: $file_path"
        return 1
    fi
}

# Function to check if a directory exists
check_dir_exists() {
    local dir_path="$1"
    local message="$2"
    
    if [ -d "$dir_path" ]; then
        echo -e "${GREEN}✓ $message${NC}"
        return 0
    else
        echo -e "${RED}✗ $message${NC}"
        echo -e "  Directory not found: $dir_path"
        return 1
    fi
}

# Function to check if file contains a pattern
check_file_contains() {
    local file_path="$1"
    local pattern="$2"
    local message="$3"
    
    if grep -q "$pattern" "$file_path"; then
        echo -e "${GREEN}✓ $message${NC}"
        return 0
    else
        echo -e "${RED}✗ $message${NC}"
        echo -e "  Pattern not found in file: $pattern"
        return 1
    fi
}

# Function to check if a checksum is valid
check_checksum() {
    local file_path="$1"
    local expected_checksum="$2"
    local message="$3"
    
    # Extract checksum from file
    local actual_checksum=$(grep -oE '\[CHECKSUM:[a-f0-9]+\]' "$file_path" | cut -d':' -f2 | tr -d '[]')
    
    if [ "$actual_checksum" = "$expected_checksum" ]; then
        echo -e "${GREEN}✓ $message${NC}"
        return 0
    else
        echo -e "${RED}✗ $message${NC}"
        echo -e "  Expected: $expected_checksum"
        echo -e "  Actual:   $actual_checksum"
        return 1
    fi
}

# Mock the agent bootstrap process
mock_bootstrap() {
    local agent_name="$1"
    local temp_dir="$SCRIPT_DIR/temp"
    
    # Create temporary directory
    mkdir -p "$temp_dir/$agent_name"
    
    # Create mock agent files
    echo "# Mock state.json" > "$temp_dir/$agent_name/state.json"
    echo "# Mock memory.md" > "$temp_dir/$agent_name/memory.md"
    echo "# Mock personality.md" > "$temp_dir/$agent_name/personality.md"
    echo "# Mock procedures.md [CHECKSUM:1234ab]" > "$temp_dir/$agent_name/procedures.md"
    
    echo "$temp_dir/$agent_name"
}

# Clean up mock environment
cleanup_mock() {
    local mock_dir="$1"
    
    if [ -d "$mock_dir" ]; then
        rm -rf "$mock_dir"
    fi
}

# Section header for test output
print_section() {
    local title="$1"
    echo -e "${BLUE}===== $title =====${NC}"
}

# Assert that a condition is true
assert() {
    local condition="$1"
    local message="$2"
    
    if eval "$condition"; then
        echo -e "${GREEN}✓ $message${NC}"
        return 0
    else
        echo -e "${RED}✗ $message${NC}"
        return 1
    fi
}

# Assert that two values are equal
assert_equals() {
    local expected="$1"
    local actual="$2"
    local message="$3"
    
    if [ "$expected" = "$actual" ]; then
        echo -e "${GREEN}✓ $message${NC}"
        return 0
    else
        echo -e "${RED}✗ $message${NC}"
        echo -e "  Expected: $expected"
        echo -e "  Actual:   $actual"
        return 1
    fi
}