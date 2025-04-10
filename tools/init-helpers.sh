#!/bin/bash
# Helper functions for agent initialization
# Created by Dr. Heinz Doofenshmirtz

# Function to check for untracked files during agent initialization
check_untracked_files() {
    echo "▶️ STEP 3: Checking for untracked files..."
    "$SCRIPT_DIR/../tools/untracked-files-monitor.sh"
}

# Export functions
export -f check_untracked_files