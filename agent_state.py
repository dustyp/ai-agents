#!/usr/bin/env python3
"""
Agent State Manager for AI Agents

This module handles saving and loading agent state, including:
- Current working project
- Recent memory and conversations
- Active tasks
- Emotional state
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
import sys

AGENTS_DIR = os.path.expanduser("~/_projects/ai-agents/agents")

def save_agent_state(agent_name, state_data):
    """
    Save agent's current state
    
    Args:
        agent_name: Name of the agent
        state_data: Dictionary of state information
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    state_path = os.path.join(agent_dir, "state.json")
    
    # Ensure agent directory exists
    if not os.path.exists(agent_dir):
        print(f"Error: Agent '{agent_name}' does not exist")
        return False
        
    # Add timestamp to state
    state_data["last_updated"] = int(time.time())
    
    try:
        with open(state_path, 'w') as f:
            json.dump(state_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving state: {e}")
        return False

def load_agent_state(agent_name):
    """
    Load agent's current state
    
    Args:
        agent_name: Name of the agent
        
    Returns:
        Dictionary of state information or empty dict if not found
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    state_path = os.path.join(agent_dir, "state.json")
    
    # Ensure agent directory exists
    if not os.path.exists(agent_dir):
        print(f"Error: Agent '{agent_name}' does not exist")
        return {}
        
    # Check if state file exists
    if not os.path.exists(state_path):
        print(f"No saved state found for {agent_name}")
        return {}
        
    try:
        with open(state_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading state: {e}")
        return {}

def update_memory(agent_name, new_memories):
    """
    Update agent's memory.md file with new memories
    
    Args:
        agent_name: Name of the agent
        new_memories: Dictionary of memory sections and content to add
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    memory_path = os.path.join(agent_dir, "memory.md")
    
    # Ensure agent directory exists
    if not os.path.exists(agent_dir):
        print(f"Error: Agent '{agent_name}' does not exist")
        return False
        
    # Read existing memory
    try:
        with open(memory_path, 'r') as f:
            memory_content = f.read()
    except:
        memory_content = f"# {agent_name.title()}'s Memory Database\n\n"
    
    # Update memory sections
    for section, content in new_memories.items():
        # Check if section exists
        section_header = f"## {section}"
        if section_header in memory_content:
            # Find the end of the section
            section_start = memory_content.find(section_header)
            next_section = memory_content.find("## ", section_start + len(section_header))
            if next_section == -1:
                # This is the last section, append to the end
                memory_content += f"\n- {content}"
            else:
                # Insert before the next section
                memory_content = (
                    memory_content[:next_section] + 
                    f"- {content}\n\n" + 
                    memory_content[next_section:]
                )
        else:
            # Add new section
            memory_content += f"\n## {section}\n- {content}\n"
    
    # Write updated memory
    try:
        with open(memory_path, 'w') as f:
            f.write(memory_content)
        return True
    except Exception as e:
        print(f"Error updating memory: {e}")
        return False

def get_unread_messages(agent_name):
    """
    Get unread messages from agent's inbox
    
    Args:
        agent_name: Name of the agent
        
    Returns:
        List of unread messages
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    inbox_path = os.path.join(agent_dir, "inbox.json")
    
    # Ensure agent directory exists
    if not os.path.exists(agent_dir):
        print(f"Error: Agent '{agent_name}' does not exist")
        return []
        
    # Check if inbox file exists
    if not os.path.exists(inbox_path):
        return []
        
    try:
        with open(inbox_path, 'r') as f:
            inbox = json.load(f)
        
        # Get unread messages
        unread = [m for m in inbox.get("messages", []) if not m.get("read", False)]
        return unread
    except Exception as e:
        print(f"Error getting unread messages: {e}")
        return []

def mark_messages_read(agent_name):
    """
    Mark all messages in agent's inbox as read
    
    Args:
        agent_name: Name of the agent
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    inbox_path = os.path.join(agent_dir, "inbox.json")
    
    # Ensure agent directory exists
    if not os.path.exists(agent_dir):
        print(f"Error: Agent '{agent_name}' does not exist")
        return False
        
    # Check if inbox file exists
    if not os.path.exists(inbox_path):
        return False
        
    try:
        with open(inbox_path, 'r') as f:
            inbox = json.load(f)
        
        # Mark all messages as read
        for m in inbox.get("messages", []):
            m["read"] = True
        
        # Write updated inbox
        with open(inbox_path, 'w') as f:
            json.dump(inbox, f, indent=2)
        
        return True
    except Exception as e:
        print(f"Error marking messages read: {e}")
        return False

def add_response(agent_name, response):
    """
    Add a response to agent's outbox
    
    Args:
        agent_name: Name of the agent
        response: Response content
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    outbox_path = os.path.join(agent_dir, "outbox.json")
    
    # Ensure agent directory exists
    if not os.path.exists(agent_dir):
        print(f"Error: Agent '{agent_name}' does not exist")
        return False
        
    # Create or update outbox
    if os.path.exists(outbox_path):
        try:
            with open(outbox_path, 'r') as f:
                outbox = json.load(f)
        except:
            outbox = {"messages": []}
    else:
        outbox = {"messages": []}
    
    # Add new response
    outbox["messages"].append({
        "timestamp": int(time.time()),
        "content": response,
        "read": False
    })
    
    # Save updated outbox
    try:
        with open(outbox_path, 'w') as f:
            json.dump(outbox, f, indent=2)
        return True
    except Exception as e:
        print(f"Error adding response: {e}")
        return False

def generate_state_prompt(agent_name):
    """
    Generate a comprehensive state prompt for the agent
    
    Args:
        agent_name: Name of the agent
        
    Returns:
        String with complete state information
    """
    # Load agent state
    state = load_agent_state(agent_name)
    
    # Get unread messages
    unread = get_unread_messages(agent_name)
    
    # Build state prompt
    prompt = f"# {agent_name.title()} State Initialization\n\n"
    
    # Add state information
    if state:
        prompt += "## Current State\n"
        prompt += f"- Last active: {datetime.fromtimestamp(state.get('last_updated', 0)).strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        # Add current project
        if "current_project" in state:
            prompt += f"- Current project: {state.get('current_project')}\n"
        
        # Add emotional state if available
        if "emotional_state" in state:
            prompt += f"- Emotional state: {state.get('emotional_state')}\n"
        
        # Add current tasks
        if "active_tasks" in state and state["active_tasks"]:
            prompt += "- Active tasks:\n"
            for task in state["active_tasks"]:
                prompt += f"  * {task}\n"
        
        # Add any other state information
        for key, value in state.items():
            if key not in ["last_updated", "current_project", "emotional_state", "active_tasks"]:
                prompt += f"- {key}: {value}\n"
    else:
        prompt += "## Current State\n"
        prompt += "- No previous state information available\n"
    
    # Add unread messages
    if unread:
        prompt += "\n## Unread Messages\n"
        for msg in unread:
            sender = msg.get("from", "Unknown")
            timestamp = datetime.fromtimestamp(msg.get("timestamp", 0)).strftime("%Y-%m-%d %H:%M:%S")
            subject = msg.get("subject", "No subject")
            message_type = msg.get("type", "general")
            content = msg.get("content", "")
            
            prompt += f"### Message from {sender} at {timestamp}\n"
            prompt += f"**Subject:** {subject}\n"
            prompt += f"**Type:** {message_type}\n"
            prompt += f"**Content:**\n{content}\n\n"
    
    return prompt

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent_state.py <command> [agent_name] [args]")
        print("Commands:")
        print("  generate-prompt <agent_name> - Generate state prompt for agent")
        print("  save-state <agent_name> - Save agent state")
        print("  mark-read <agent_name> - Mark all messages as read")
        return
    
    command = sys.argv[1]
    
    if command == "generate-prompt":
        if len(sys.argv) < 3:
            print("Error: Agent name required")
            return
        agent_name = sys.argv[2]
        prompt = generate_state_prompt(agent_name)
        print(prompt)
    
    elif command == "save-state":
        if len(sys.argv) < 3:
            print("Error: Agent name required")
            return
        agent_name = sys.argv[2]
        
        # Get state data from stdin
        try:
            state_data = json.loads(sys.stdin.read())
            success = save_agent_state(agent_name, state_data)
            if success:
                print(f"State saved for {agent_name}")
            else:
                print(f"Failed to save state for {agent_name}")
        except json.JSONDecodeError:
            print("Error: Invalid JSON state data")
    
    elif command == "mark-read":
        if len(sys.argv) < 3:
            print("Error: Agent name required")
            return
        agent_name = sys.argv[2]
        success = mark_messages_read(agent_name)
        if success:
            print(f"Marked all messages as read for {agent_name}")
        else:
            print(f"Failed to mark messages as read for {agent_name}")
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()