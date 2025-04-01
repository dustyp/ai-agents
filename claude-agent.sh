#!/bin/bash
# claude-agent.sh - A wrapper script to fully bootstrap agents with Claude

# Default values
AGENT_NAME="heinz"
PROMPT=""
INTERACTIVE="true"
NON_INTERACTIVE_OUTPUT_FILE="agent_response.txt"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -a|--agent)
            AGENT_NAME="$2"
            shift 2
            ;;
        --prompt)
            PROMPT="$2"
            shift 2
            ;;
        --non-interactive)
            INTERACTIVE="false"
            shift
            ;;
        --output)
            NON_INTERACTIVE_OUTPUT_FILE="$2"
            shift 2
            ;;
        *)
            # For any other argument, assume it's a prompt
            PROMPT="$1"
            shift
            ;;
    esac
done

# Construct the prompt
if [ -n "$PROMPT" ]; then
    FULL_PROMPT="CRITICAL STARTUP INSTRUCTIONS: You must follow the bootstrap instructions in CLAUDE.md. If you cannot find your memory tool module then when you are done with the other tasks go back and try to search for the knowledge graph in your memory tool to gain additional context. 

USER REQUEST: ${PROMPT}"
else
    FULL_PROMPT="CRITICAL STARTUP INSTRUCTIONS: You must follow the bootstrap instructions in CLAUDE.md. If you cannot find your memory tool module then when you are done with the other tasks go back and try to search for the knowledge graph in your memory tool to gain additional context"
fi

# Run Claude with the appropriate instructions
if [ "$INTERACTIVE" = "true" ]; then
    # Interactive mode - normal operation
    claude "$FULL_PROMPT"
else
    # Non-interactive mode - execute and exit
    echo "Running in non-interactive mode..."
    claude "$FULL_PROMPT" --no-confirmation > "$NON_INTERACTIVE_OUTPUT_FILE"
    echo "Agent response saved to $NON_INTERACTIVE_OUTPUT_FILE"
    # Exit immediately after completion
    exit 0
fi