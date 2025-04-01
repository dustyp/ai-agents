#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Parent directory (project root)
PROJECT_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"

# Use absolute paths for all files
CONFIG_FILE="$SCRIPT_DIR/recruitment_state.json"
PROMPT_FILE="$SCRIPT_DIR/next_prompt.txt"
LOG_FILE="$SCRIPT_DIR/recruitment_log.txt"

# Get current date
CURRENT_DATE=$(date +"%Y-%m-%d")

# Log execution
echo "[$(date)] Wake-up script executed" >> "$LOG_FILE"
echo "[$(date)] Script directory: $SCRIPT_DIR" >> "$LOG_FILE"
echo "[$(date)] Project directory: $PROJECT_DIR" >> "$LOG_FILE"

# NOTICE: This script has been updated to require human supervision.
# Automated execution via cron is no longer supported since Claude agents
# require human supervision. Use this script only with human interaction.

echo "[$(date)] IMPORTANT: This script now requires human supervision!" >> "$LOG_FILE"
echo "[$(date)] Automated execution via cron is not supported." >> "$LOG_FILE"
echo ""
echo "======================================================================"
echo "NOTICE: Claude agents require human supervision."
echo "This script should not be run via cron or other automated methods."
echo "Instead, launch Claude and use the prompt 'Check recruitment status'"
echo "to manually trigger the workflow with human supervision."
echo "======================================================================"
echo ""
echo "Recruitment workflow should now be run with human in the loop."
echo "Exiting without launching Claude agent."
exit 1
