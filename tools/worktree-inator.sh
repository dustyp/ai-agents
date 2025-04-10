#!/bin/bash
# WORKTREE-INATOR: A tool for managing git worktrees for the AI Agents project
# Created by Dr. Heinz Doofenshmirtz

set -e  # Exit on any error

# Configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$SCRIPT_DIR/.."
WORKTREE_DIR="$REPO_ROOT/worktrees"
SHARED_VENV_DIR="$REPO_ROOT/shared_venv"

# Create directories if they don't exist
mkdir -p "$WORKTREE_DIR"
mkdir -p "$SHARED_VENV_DIR"
DEFAULT_BRANCH="main"
BOLD=$(tput bold)
NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)
BLUE=$(tput setaf 4)

# Help message
show_help() {
    echo "${BOLD}WORKTREE-INATOR${NORMAL} - Git Worktree Management Tool"
    echo
    echo "Usage: $0 [command] [options]"
    echo
    echo "Worktree Commands:"
    echo "  ${BOLD}setup${NORMAL} <ticket-id> [description]  Create a new worktree for a ticket"
    echo "  ${BOLD}list${NORMAL}                            List all worktrees"
    echo "  ${BOLD}cleanup${NORMAL} <path>                   Remove a worktree"
    echo "  ${BOLD}prune${NORMAL}                           Clean up stale worktree metadata"
    echo
    echo "Python Virtual Environment Commands:"
    echo "  ${BOLD}venv-setup${NORMAL}                      Create or update shared Python virtual environment"
    echo "  ${BOLD}venv-info${NORMAL}                       Display information about the shared venv"
    echo
    echo "Other Commands:"
    echo "  ${BOLD}help${NORMAL}                            Show this help message"
    echo
    echo "Examples:"
    echo "  $0 setup CRA-50 database-implementation"
    echo "  $0 list"
    echo "  $0 cleanup worktrees/CRA-50"
    echo "  $0 venv-setup"
    echo "  $0 venv-info"
    echo
}

# Create a new worktree
setup_worktree() {
    if [ -z "$1" ]; then
        echo "${RED}Error: Ticket ID is required${NORMAL}"
        show_help
        exit 1
    fi

    TICKET_ID=$1
    DESCRIPTION=${2:-"implementation"}
    BRANCH_NAME="feature/${TICKET_ID}-${DESCRIPTION}"
    WORKTREE_PATH="${WORKTREE_DIR}/${TICKET_ID}"

    echo "${BOLD}${BLUE}BEHOLD! The WORKTREE-CREATION-INATOR is now in action!${NORMAL}"
    echo "${YELLOW}▶️ STEP 1: Checking if branch exists...${NORMAL}"
    
    if git show-ref --verify --quiet refs/heads/${BRANCH_NAME}; then
        echo "Branch ${BRANCH_NAME} already exists."
        BRANCH_EXISTS=true
    elif git show-ref --verify --quiet refs/remotes/origin/${BRANCH_NAME}; then
        echo "Branch ${BRANCH_NAME} exists on remote."
        BRANCH_EXISTS=true
    else
        echo "Branch ${BRANCH_NAME} does not exist yet."
        BRANCH_EXISTS=false
    fi

    echo "${YELLOW}▶️ STEP 2: Creating worktree at ${WORKTREE_PATH}...${NORMAL}"
    
    if [ "$BRANCH_EXISTS" = true ]; then
        git worktree add "${WORKTREE_PATH}" "${BRANCH_NAME}"
    else
        git worktree add -b "${BRANCH_NAME}" "${WORKTREE_PATH}"
    fi

    echo "${YELLOW}▶️ STEP 3: Verifying worktree creation...${NORMAL}"
    git worktree list

    echo "${YELLOW}▶️ STEP 4: Setting up development environment...${NORMAL}"
    echo "Worktree for ${TICKET_ID} created successfully at ${WORKTREE_PATH}"
    
    # Check if Python files exist in the worktree
    PYTHON_FILES=$(find "${WORKTREE_PATH}" -name "*.py" -type f | wc -l)
    
    echo
    echo "${GREEN}✅ SUCCESS! To begin working, run:${NORMAL}"
    echo "cd ${WORKTREE_PATH}"
    
    # If Python files found, suggest setting up the venv
    if [ "$PYTHON_FILES" -gt 0 ]; then
        echo
        echo "${YELLOW}Python files detected! For Python development:${NORMAL}"
        echo "1. Set up shared venv: ${BOLD}$0 venv-setup${NORMAL}"
        echo "2. Activate the venv:  ${BOLD}source ${SHARED_VENV_DIR}/bin/activate${NORMAL}"
    fi
}

# List all worktrees
list_worktrees() {
    echo "${BOLD}${BLUE}BEHOLD! The WORKTREE-LISTING-INATOR is now in action!${NORMAL}"
    echo
    git worktree list
    echo
    echo "${YELLOW}Want more details? Try:${NORMAL}"
    echo "git worktree list --verbose"
}

# Clean up a worktree
cleanup_worktree() {
    if [ -z "$1" ]; then
        echo "${RED}Error: Worktree path is required${NORMAL}"
        show_help
        exit 1
    fi

    WORKTREE_PATH="$1"

    echo "${BOLD}${BLUE}BEHOLD! The WORKTREE-CLEANUP-INATOR is now in action!${NORMAL}"
    echo "${YELLOW}▶️ STEP 1: Verifying worktree exists...${NORMAL}"
    
    if ! git worktree list | grep -q "${WORKTREE_PATH}"; then
        echo "${RED}Error: Worktree not found at ${WORKTREE_PATH}${NORMAL}"
        exit 1
    fi

    echo "${YELLOW}▶️ STEP 2: Checking for uncommitted changes...${NORMAL}"
    if [ -d "${WORKTREE_PATH}" ]; then
        pushd "${WORKTREE_PATH}" > /dev/null
        if ! git diff-index --quiet HEAD --; then
            echo "${RED}Warning: There are uncommitted changes in the worktree.${NORMAL}"
            echo "Please commit or stash them before removing the worktree."
            exit 1
        fi
        popd > /dev/null
    fi

    echo "${YELLOW}▶️ STEP 3: Removing worktree...${NORMAL}"
    git worktree remove "${WORKTREE_PATH}"

    echo "${YELLOW}▶️ STEP 4: Verifying removal...${NORMAL}"
    git worktree list

    echo "${GREEN}✅ SUCCESS! Worktree at ${WORKTREE_PATH} has been removed.${NORMAL}"
}

# Prune stale worktree metadata
prune_worktrees() {
    echo "${BOLD}${BLUE}BEHOLD! The WORKTREE-PRUNING-INATOR is now in action!${NORMAL}"
    echo "${YELLOW}▶️ STEP 1: Pruning stale worktree metadata...${NORMAL}"
    git worktree prune -v
    echo "${GREEN}✅ SUCCESS! Stale worktree information has been pruned.${NORMAL}"
}

# Create or update the shared Python virtual environment
setup_venv() {
    echo "${BOLD}${BLUE}BEHOLD! The VENV-CREATION-INATOR is now in action!${NORMAL}"
    
    # Check if Python is installed
    if ! command -v python3 &> /dev/null; then
        echo "${RED}Error: Python 3 is not installed. Please install Python 3 to continue.${NORMAL}"
        exit 1
    fi
    
    echo "${YELLOW}▶️ STEP 1: Setting up shared Python virtual environment...${NORMAL}"
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "$SHARED_VENV_DIR/bin" ]; then
        echo "Creating new virtual environment in $SHARED_VENV_DIR"
        python3 -m venv "$SHARED_VENV_DIR"
    else
        echo "Using existing virtual environment in $SHARED_VENV_DIR"
    fi
    
    echo "${YELLOW}▶️ STEP 2: Upgrading pip...${NORMAL}"
    "$SHARED_VENV_DIR/bin/pip" install --upgrade pip
    
    # Install requirements if a requirements file exists
    if [ -f "$REPO_ROOT/requirements.txt" ]; then
        echo "${YELLOW}▶️ STEP 3: Installing requirements...${NORMAL}"
        "$SHARED_VENV_DIR/bin/pip" install -r "$REPO_ROOT/requirements.txt"
    fi
    
    echo "${GREEN}✅ SUCCESS! Shared Python virtual environment is ready.${NORMAL}"
    echo
    echo "${YELLOW}To activate the virtual environment in any worktree, run:${NORMAL}"
    echo "source $SHARED_VENV_DIR/bin/activate"
}

# Show venv information
venv_info() {
    echo "${BOLD}${BLUE}BEHOLD! The VENV-INFO-INATOR is now in action!${NORMAL}"
    
    if [ ! -d "$SHARED_VENV_DIR/bin" ]; then
        echo "${YELLOW}No shared virtual environment found. Create one with:${NORMAL}"
        echo "$0 venv-setup"
        return
    fi
    
    echo "${YELLOW}▶️ Shared venv location: ${NORMAL}$SHARED_VENV_DIR"
    echo "${YELLOW}▶️ Python version: ${NORMAL}$($SHARED_VENV_DIR/bin/python --version 2>&1)"
    echo "${YELLOW}▶️ Pip version: ${NORMAL}$($SHARED_VENV_DIR/bin/pip --version 2>&1)"
    
    echo "${YELLOW}▶️ Installed packages:${NORMAL}"
    $SHARED_VENV_DIR/bin/pip list
    
    echo
    echo "${YELLOW}To activate the virtual environment in any worktree, run:${NORMAL}"
    echo "source $SHARED_VENV_DIR/bin/activate"
}

# Main command processing
case "$1" in
    setup)
        shift
        setup_worktree "$@"
        ;;
    list)
        list_worktrees
        ;;
    cleanup)
        shift
        cleanup_worktree "$@"
        ;;
    prune)
        prune_worktrees
        ;;
    venv-setup)
        setup_venv
        ;;
    venv-info)
        venv_info
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