#!/bin/bash
# UNTRACKED-FILES-MONITOR-INATOR: A tool for detecting and alerting about untracked files
# Created by Dr. Heinz Doofenshmirtz

set -e  # Exit on any error

# Configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$SCRIPT_DIR/.."
STORAGE_FILE="$REPO_ROOT/.untracked_files_history.txt"
BOLD=$(tput bold)
NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)
BLUE=$(tput setaf 4)

# Get untracked files
get_untracked_files() {
    cd "$REPO_ROOT"
    git status --porcelain | grep "^??" | cut -c4-
}

# Categorize a file by type
categorize_file() {
    local file="$1"
    local ext="${file##*.}"
    
    case "$ext" in
        py|js|ts|jsx|tsx|java|rb|go|rs|c|cpp|h|hpp)
            echo "CODE"
            ;;
        json|yml|yaml|toml|ini|xml|conf|config)
            echo "CONFIG"
            ;;
        md|txt|rst|adoc|log)
            echo "DOCUMENTATION"
            ;;
        csv|tsv|xls|xlsx|ods|db|sqlite|sql)
            echo "DATA"
            ;;
        png|jpg|jpeg|gif|svg|webp|ico|bmp)
            echo "IMAGE"
            ;;
        sh|bash|zsh|bat|cmd|ps1)
            echo "SCRIPT"
            ;;
        *)
            # Special cases for files without extensions
            if [[ "$file" == *"README"* ]] || [[ "$file" == *"LICENSE"* ]]; then
                echo "DOCUMENTATION"
            elif [[ "$file" == ".env"* ]] || [[ "$file" == ".git"* ]]; then
                echo "CONFIG"
            else
                echo "OTHER"
            fi
            ;;
    esac
}

# Load previously reported files
load_history() {
    if [ -f "$STORAGE_FILE" ]; then
        cat "$STORAGE_FILE"
    else
        echo ""
    fi
}

# Save reported files
save_history() {
    local files="$1"
    echo "$files" > "$STORAGE_FILE"
}

# Check if file was previously reported
is_new_file() {
    local file="$1"
    local history=$(load_history)
    
    if grep -q "^$file$" <<< "$history"; then
        return 1  # File was previously reported
    else
        return 0  # File is new
    fi
}

# Filter for new files only
filter_new_files() {
    local files="$1"
    local new_files=""
    
    for file in $files; do
        if is_new_file "$file"; then
            new_files="$new_files $file"
        fi
    done
    
    echo "$new_files"
}

# Update history with new files
update_history() {
    local current_files="$1"
    local history=$(load_history)
    local new_history="$history"
    
    # Add new files to history
    for file in $current_files; do
        if ! grep -q "^$file$" <<< "$new_history"; then
            new_history="${new_history}${file}
"
        fi
    done
    
    save_history "$new_history"
}

# Main function to display untracked files
display_untracked_files() {
    local show_all=${1:-false}
    
    cd "$REPO_ROOT"
    
    echo "${BOLD}${BLUE}BEHOLD! The UNTRACKED-FILES-DETECTOR-INATOR is now in action!${NORMAL}"
    echo
    
    local untracked_files=$(get_untracked_files)
    
    if [ -z "$untracked_files" ]; then
        echo "${GREEN}No untracked files found in the repository.${NORMAL}"
        echo
        return 0
    fi
    
    # If not showing all, filter for new files only
    if [ "$show_all" = false ]; then
        local new_files=$(filter_new_files "$untracked_files")
        if [ -z "$new_files" ]; then
            echo "${GREEN}No new untracked files found (previously reported files are being skipped).${NORMAL}"
            echo "${YELLOW}Use --all flag to see all untracked files.${NORMAL}"
            echo
            return 0
        fi
        untracked_files="$new_files"
    fi
    
    echo "${YELLOW}${BOLD}ALERT! Untracked files detected:${NORMAL}"
    echo
    
    # Sort and display files by category
    echo "${BOLD}CODE FILES:${NORMAL}"
    for file in $untracked_files; do
        if [ "$(categorize_file "$file")" = "CODE" ]; then
            echo "  - $file"
        fi
    done
    echo
    
    echo "${BOLD}CONFIG FILES:${NORMAL}"
    for file in $untracked_files; do
        if [ "$(categorize_file "$file")" = "CONFIG" ]; then
            echo "  - $file"
        fi
    done
    echo
    
    echo "${BOLD}DOCUMENTATION FILES:${NORMAL}"
    for file in $untracked_files; do
        if [ "$(categorize_file "$file")" = "DOCUMENTATION" ]; then
            echo "  - $file"
        fi
    done
    echo
    
    echo "${BOLD}DATA FILES:${NORMAL}"
    for file in $untracked_files; do
        if [ "$(categorize_file "$file")" = "DATA" ]; then
            echo "  - $file"
        fi
    done
    echo
    
    echo "${BOLD}SCRIPT FILES:${NORMAL}"
    for file in $untracked_files; do
        if [ "$(categorize_file "$file")" = "SCRIPT" ]; then
            echo "  - $file"
        fi
    done
    echo
    
    echo "${BOLD}IMAGE FILES:${NORMAL}"
    for file in $untracked_files; do
        if [ "$(categorize_file "$file")" = "IMAGE" ]; then
            echo "  - $file"
        fi
    done
    echo
    
    echo "${BOLD}OTHER FILES:${NORMAL}"
    for file in $untracked_files; do
        if [ "$(categorize_file "$file")" = "OTHER" ]; then
            echo "  - $file"
        fi
    done
    echo
    
    # Update history with current files
    update_history "$untracked_files"
    
    # Provide suggestions
    echo "${BOLD}Suggestions for handling untracked files:${NORMAL}"
    echo "1. Add specific files to the current branch: ${YELLOW}git add [file1] [file2]${NORMAL}"
    echo "2. Add to .gitignore if they should never be tracked: ${YELLOW}echo \"[pattern]\" >> .gitignore${NORMAL}"
    echo "3. Use worktrees to separate work on different branches: ${YELLOW}./tools/worktree-inator.sh setup [ticket]${NORMAL}"
    echo "4. Create a new branch for these files: ${YELLOW}git checkout -b feature/new-branch-name${NORMAL}"
    echo
    echo "${RED}IMPORTANT: I will not take any action on these files without your explicit instructions.${NORMAL}"
    echo
}

# Parse arguments
show_all=false

if [ "$1" = "--all" ]; then
    show_all=true
fi

display_untracked_files "$show_all"

exit 0