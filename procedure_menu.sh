#!/bin/bash

# procedure_menu.sh - Display the procedure menu from procedures.md

PROCEDURES_FILE="/Users/aidan/_projects/ai-agents/agents/heinz/procedures.md"

# Extract and display the procedure menu section
echo "====================================="
echo "HEINZ PROCEDURE MENU"
echo "====================================="
echo

# Use awk to extract the procedure menu section
awk '/^## PROCEDURE MENU$/,/^## PROCEDURES$/' "$PROCEDURES_FILE" | grep -v "^## " | grep -v "^$"

echo 
echo "====================================="
echo "To execute a procedure, use the syntax:"
echo "procedure <procedure_name>"
echo 
echo "Example: procedure create_ticket"
echo "====================================="