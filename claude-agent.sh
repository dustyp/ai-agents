#!/bin/bash
# claude-agent.sh - A wrapper script to fully bootstrap agents with Claude

# Default to regular Claude if no agent specified
AGENT=""
SLEEP_MODE=false
RESUME_MODE=false
SAVE_MEMORIES=()
CURRENT_PROJECT=""
TRANSCRIPT_FILE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -a|--agent)
      AGENT="$2"
      shift 2
      ;;
    -s|--sleep)
      SLEEP_MODE=true
      shift
      ;;
    -r|--resume)
      RESUME_MODE=true
      shift
      ;;
    -m|--memory)
      SAVE_MEMORIES+=("$2")
      shift 2
      ;;
    -p|--project)
      CURRENT_PROJECT="$2"
      shift 2
      ;;
    -t|--transcript)
      TRANSCRIPT_FILE="$2"
      shift 2
      ;;
    *)
      # Collect remaining arguments for Claude
      CLAUDE_ARGS=("$@")
      break
      ;;
  esac
done

# This function is deprecated - Claude can't send signals to the shell script
# Keeping the function stub for backward compatibility, but it doesn't do anything
parse_system_commands() {
  local transcript="$1"
  # No-op function - we now use explicit save/resume flags
  return 0
}

# If agent specified, check if it exists
if [ -n "$AGENT" ]; then
  if [ ! -d "$(pwd)/agents/$AGENT" ]; then
    echo "Error: Agent '$AGENT' not found in $(pwd)/agents/"
    echo "Available agents:"
    python3 coordinator.py list
    exit 1
  fi

  # Sleep mode - save agent state and exit
  if [ "$SLEEP_MODE" = true ]; then
    echo "🛌 Putting agent $AGENT to sleep..."
    
    # Build state data with any memories to save
    STATE_DATA='{"active_tasks": [], "emotional_state": "resting"'
    
    # Add current project if specified
    if [ -n "$CURRENT_PROJECT" ]; then
      STATE_DATA="$STATE_DATA, \"current_project\": \"$CURRENT_PROJECT\""
    fi
    
    # Close the JSON object
    STATE_DATA="$STATE_DATA}"
    
    # Save state
    echo "$STATE_DATA" | python3 agent_state.py save-state "$AGENT"
    
    # Save any new memories if provided
    if [ ${#SAVE_MEMORIES[@]} -gt 0 ]; then
      for mem in "${SAVE_MEMORIES[@]}"; do
        IFS=':' read -r section content <<< "$mem"
        python3 coordinator.py send "$AGENT" "Remember for later: $content" --subject "Memory Update" --type "system"
        echo "📝 Added memory: '$content' to section '$section'"
      done
    fi
    
    echo "💤 Agent $AGENT is now sleeping. State saved."
    exit 0
  fi
  
  echo "🤖 Waking up agent: $AGENT"

  # Mark all messages as read first to prepare for session
  python3 agent_state.py mark-read "$AGENT"
  
  # Generate state initialization prompt
  AGENT_STATE=$(python3 agent_state.py generate-prompt "$AGENT")
  
  # Create a temporary file for the state prompt
  STATE_FILE=$(mktemp)
  echo "$AGENT_STATE" > "$STATE_FILE"
  
  # Create a temporary transcript file if none provided
  if [ -z "$TRANSCRIPT_FILE" ]; then
    TRANSCRIPT_FILE=$(mktemp)
    AUTO_TRANSCRIPT=true
  else
    AUTO_TRANSCRIPT=false
  fi
  
  # Set environment variable for Claude (used by script internally)
  export CLAUDE_AGENT="$AGENT"
  
  echo "📋 Loading personality, memory, and state..."
  
  # Get agent personality file
  PERSONALITY_FILE="$(pwd)/agents/$AGENT/personality.md"
  MEMORY_FILE="$(pwd)/agents/$AGENT/memory.md"
  
  # Read personality and memory files
  PERSONALITY=$(cat "$PERSONALITY_FILE")
  MEMORY=$(cat "$MEMORY_FILE")
  
  # Create agent initialization prompt
  if [ "$RESUME_MODE" = true ]; then
    # Resume mode - focus on resuming previous session
    INITIAL_PROMPT="I am $AGENT. Please load my personality, memory, and state.

# Agent Initialization with Resume
You are now operating as $AGENT.

## Personality
$PERSONALITY

## Memory
$MEMORY

## State
$AGENT_STATE

IMPORTANT: You must run the resume_last_session procedure immediately.
Please confirm that you've loaded my context and are ready to resume as $AGENT. Respond in character immediately."
  else
    # Regular initialization
    INITIAL_PROMPT="I am $AGENT. Please load my personality, memory, and state.

# Agent Initialization
You are now operating as $AGENT.

## Personality
$PERSONALITY

## Memory
$MEMORY

## State
$AGENT_STATE

Please confirm that you've loaded my context and are ready to proceed as $AGENT. Respond in character immediately."
  fi
  
  # Run Claude with agent context passed directly as an initial prompt
  # The initial prompt will bootstrap the agent before user interaction
  echo "$INITIAL_PROMPT" | claude --print | head -n 1
  
  # Now start the interactive session with agent already initialized
  claude "${CLAUDE_ARGS[@]}"
  
  # Clean up temp files
  rm "$STATE_FILE"
  if [ "$AUTO_TRANSCRIPT" = true ]; then
    rm "$TRANSCRIPT_FILE"
  fi
  
  # If sleep mode flag was provided, execute it
  if [ "$SLEEP_MODE" = true ]; then
    echo "🛌 Putting agent $AGENT to sleep..."
    
    # Build state data to save
    STATE_DATA='{"active_tasks": [], "emotional_state": "resting"'
    
    # Add current project if specified
    if [ -n "$CURRENT_PROJECT" ]; then
      STATE_DATA="$STATE_DATA, \"current_project\": \"$CURRENT_PROJECT\""
    fi
    
    # Close the JSON object
    STATE_DATA="$STATE_DATA}"
    
    # Save state
    echo "$STATE_DATA" | python3 agent_state.py save-state "$AGENT"
    
    # Save any new memories if provided
    if [ ${#SAVE_MEMORIES[@]} -gt 0 ]; then
      for mem in "${SAVE_MEMORIES[@]}"; do
        IFS=':' read -r section content <<< "$mem"
        python3 coordinator.py send "$AGENT" "Remember for later: $content" --subject "Memory Update" --type "system"
        echo "📝 Added memory: '$content' to section '$section'"
      done
    fi
    
    echo "💤 Agent $AGENT is now sleeping. State saved."
  else
    echo "✅ Session with $AGENT complete"
  fi
else
  # Just run regular Claude
  claude "${CLAUDE_ARGS[@]}"
fi