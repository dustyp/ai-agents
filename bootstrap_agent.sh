#!/bin/bash
# bootstrap_agent.sh
# This script sends initialization messages to bootstrap an agent's memory and tools

# Check if an agent name was provided
if [ $# -eq 0 ]
then
    echo "Error: No agent name provided."
    echo "Usage: ./bootstrap_agent.sh <agent_name>"
    exit 1
fi

AGENT_NAME=$1
COORDINATOR="./coordinator.py"

# Check if agent exists
if ! python $COORDINATOR list | grep -q "$AGENT_NAME"; then
    echo "Error: Agent '$AGENT_NAME' does not exist."
    echo "Available agents:"
    python $COORDINATOR list
    exit 1
fi

echo "====================================="
echo "Bootstrapping agent: $AGENT_NAME"
echo "====================================="

# Send system context message
echo "Sending system context..."
python $COORDINATOR send $AGENT_NAME "I'm initializing your session. Please load your personality, memory, and tools." --type "system" --subject "Initialization"

# Send tools info message
echo "Sending tools information..."
python $COORDINATOR send $AGENT_NAME "You have access to the following tools: file search, memory recall, web search." --type "system" --subject "Tools"

# Send project context
echo "Sending project context..."
python $COORDINATOR send $AGENT_NAME "You are working on the AI Agents project, which manages autonomous AI agents with individual personalities and memories." --type "system" --subject "Project Context"

# Prompt agent to acknowledge initialization
echo "Sending activation message..."
python $COORDINATOR send $AGENT_NAME "Initialization complete. Please confirm that you're ready to begin working." --type "system" --subject "Activation"

echo "====================================="
echo "Bootstrap complete for $AGENT_NAME"
echo "====================================="
echo "To check for agent responses, run:"
echo "python $COORDINATOR get $AGENT_NAME"
echo "====================================="