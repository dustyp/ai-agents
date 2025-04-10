#!/bin/bash
# VENV-CLEANUP-INATOR: A tool for cleaning up incorrectly committed Python venv directories
# Created by Dr. Heinz Doofenshmirtz

set -e  # Exit on any error

# Configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$SCRIPT_DIR/.."
BOLD=$(tput bold)
NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)
BLUE=$(tput setaf 4)

# Help message
show_help() {
    echo "${BOLD}VENV-CLEANUP-INATOR${NORMAL} - Python Virtual Environment Cleanup Tool"
    echo
    echo "Usage: $0 [command] [options]"
    echo
    echo "Commands:"
    echo "  ${BOLD}find${NORMAL}                       Find venv directories that are tracked by git"
    echo "  ${BOLD}remove${NORMAL} <path>              Remove a venv directory from git tracking"
    echo "  ${BOLD}remove-all${NORMAL}                 Remove all venv directories from git tracking"
    echo "  ${BOLD}help${NORMAL}                       Show this help message"
    echo
    echo "Examples:"
    echo "  $0 find"
    echo "  $0 remove worktrees/CRA-46/venv"
    echo
}

# Find venv directories that are tracked by git
find_venvs() {
    echo "${BOLD}${BLUE}BEHOLD! The VENV-FINDER-INATOR is now in action!${NORMAL}"
    echo "${YELLOW}▶️ STEP 1: Searching for tracked venv directories...${NORMAL}"
    
    # Find potential venv directories
    POTENTIAL_VENVS=$(find "$REPO_ROOT" -path "*/venv" -type d -o -path "*/.venv" -type d)
    TRACKED_VENVS=()
    
    # Check if they are tracked by git
    for venv_dir in $POTENTIAL_VENVS; do
        # Get a sample file from the venv
        SAMPLE_FILE=$(find "$venv_dir" -type f -name "*.py" | head -n 1)
        if [ -n "$SAMPLE_FILE" ]; then
            if git ls-files --error-unmatch "$SAMPLE_FILE" &> /dev/null; then
                TRACKED_VENVS+=("$venv_dir")
            fi
        fi
    done
    
    if [ ${#TRACKED_VENVS[@]} -eq 0 ]; then
        echo "${GREEN}No tracked venv directories found. All is well!${NORMAL}"
        return 0
    fi
    
    echo "${YELLOW}▶️ Found ${#TRACKED_VENVS[@]} tracked venv directories:${NORMAL}"
    for venv_dir in "${TRACKED_VENVS[@]}"; do
        echo "  - $venv_dir"
    done
    
    echo
    echo "${YELLOW}To remove these directories from git tracking, run:${NORMAL}"
    echo "$0 remove-all"
    echo
    echo "${YELLOW}Or to remove a specific directory:${NORMAL}"
    echo "$0 remove <path>"
}

# Remove a venv directory from git tracking
remove_venv() {
    if [ -z "$1" ]; then
        echo "${RED}Error: Path to venv directory is required${NORMAL}"
        show_help
        exit 1
    fi
    
    VENV_PATH="$1"
    REL_PATH=$(realpath --relative-to="$REPO_ROOT" "$VENV_PATH" 2>/dev/null || echo "$VENV_PATH")
    
    echo "${BOLD}${BLUE}BEHOLD! The VENV-REMOVAL-INATOR is now in action!${NORMAL}"
    echo "${YELLOW}▶️ STEP 1: Checking if $REL_PATH exists and is tracked...${NORMAL}"
    
    if [ ! -d "$VENV_PATH" ]; then
        echo "${RED}Error: Directory $REL_PATH does not exist${NORMAL}"
        exit 1
    fi
    
    # Check if any files in the venv directory are tracked
    TRACKED_FILES=$(git ls-files "$VENV_PATH")
    if [ -z "$TRACKED_FILES" ]; then
        echo "${YELLOW}No tracked files found in $REL_PATH. Nothing to do.${NORMAL}"
        return 0
    fi
    
    echo "${YELLOW}▶️ STEP 2: Removing $REL_PATH from git tracking...${NORMAL}"
    git rm -r --cached "$VENV_PATH"
    
    echo "${YELLOW}▶️ STEP 3: Verifying removal...${NORMAL}"
    if [ -z "$(git ls-files "$VENV_PATH")" ]; then
        echo "${GREEN}✅ SUCCESS! $REL_PATH has been removed from git tracking.${NORMAL}"
        echo "${YELLOW}NOTE: The directory still exists locally but will not be committed.${NORMAL}"
        echo "${YELLOW}You should now commit this change.${NORMAL}"
    else
        echo "${RED}Error: Failed to remove $REL_PATH from git tracking${NORMAL}"
        exit 1
    fi
}

# Remove all venv directories from git tracking
remove_all_venvs() {
    echo "${BOLD}${BLUE}BEHOLD! The VENV-MASS-REMOVAL-INATOR is now in action!${NORMAL}"
    echo "${YELLOW}▶️ STEP 1: Searching for tracked venv directories...${NORMAL}"
    
    # Find potential venv directories
    POTENTIAL_VENVS=$(find "$REPO_ROOT" -path "*/venv" -type d -o -path "*/.venv" -type d)
    TRACKED_VENVS=()
    
    # Check if they are tracked by git
    for venv_dir in $POTENTIAL_VENVS; do
        # Get a sample file from the venv
        SAMPLE_FILE=$(find "$venv_dir" -type f -name "*.py" | head -n 1)
        if [ -n "$SAMPLE_FILE" ]; then
            if git ls-files --error-unmatch "$SAMPLE_FILE" &> /dev/null; then
                TRACKED_VENVS+=("$venv_dir")
            fi
        fi
    done
    
    if [ ${#TRACKED_VENVS[@]} -eq 0 ]; then
        echo "${GREEN}No tracked venv directories found. All is well!${NORMAL}"
        return 0
    fi
    
    echo "${YELLOW}▶️ STEP 2: Removing ${#TRACKED_VENVS[@]} venv directories from git tracking...${NORMAL}"
    for venv_dir in "${TRACKED_VENVS[@]}"; do
        REL_PATH=$(realpath --relative-to="$REPO_ROOT" "$venv_dir")
        echo "  - Removing $REL_PATH..."
        git rm -r --cached "$venv_dir" > /dev/null 2>&1
    done
    
    echo "${YELLOW}▶️ STEP 3: Verifying removal...${NORMAL}"
    STILL_TRACKED=0
    for venv_dir in "${TRACKED_VENVS[@]}"; do
        if [ -n "$(git ls-files "$venv_dir")" ]; then
            STILL_TRACKED=$((STILL_TRACKED + 1))
        fi
    done
    
    if [ $STILL_TRACKED -eq 0 ]; then
        echo "${GREEN}✅ SUCCESS! All venv directories have been removed from git tracking.${NORMAL}"
        echo "${YELLOW}NOTE: The directories still exist locally but will not be committed.${NORMAL}"
        echo "${YELLOW}You should now commit this change.${NORMAL}"
    else
        echo "${RED}Error: Failed to remove $STILL_TRACKED venv directories from git tracking${NORMAL}"
        exit 1
    fi
}

# Main command processing
case "$1" in
    find)
        find_venvs
        ;;
    remove)
        shift
        remove_venv "$@"
        ;;
    remove-all)
        remove_all_venvs
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        show_help
        exit 1
        ;;
esac

exit 0