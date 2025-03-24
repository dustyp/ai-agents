#!/usr/bin/env python3
"""
Agent Coordinator for Notes Manager 2

This script facilitates communication between the user and AI agents
by managing message passing through inbox/outbox files.
"""

import os
import json
import time
import argparse
from datetime import datetime
from pathlib import Path

# Base directory for agent files
AGENTS_DIR = os.path.expanduser("~/_projects/ai-agents/agents")

def send_message(agent_name, message, from_user="user", subject=None, message_type=None):
    """
    Send a message to an agent's inbox
    
    Args:
        agent_name: Name of the agent (directory name)
        message: Content of the message
        from_user: Identifier of the sender
        subject: Subject line for the message
        message_type: Type of message (task, question, feedback)
        
    Returns:
        Status message
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    inbox_path = os.path.join(agent_dir, "inbox.json")
    
    # Ensure agent directory exists
    if not os.path.exists(agent_dir):
        return f"Error: Agent '{agent_name}' does not exist"
    
    # Create or update inbox
    if os.path.exists(inbox_path):
        with open(inbox_path, 'r') as f:
            try:
                inbox = json.load(f)
            except json.JSONDecodeError:
                inbox = {"messages": []}
    else:
        inbox = {"messages": []}
    
    # Add new message
    inbox["messages"].append({
        "from": from_user,
        "timestamp": int(time.time()),
        "content": message,
        "subject": subject or "No subject",
        "type": message_type or "general",
        "read": False
    })
    
    # Save updated inbox
    with open(inbox_path, 'w') as f:
        json.dump(inbox, f, indent=2)
    
    # Log the message in the session log
    log_message(agent_name, "Input", message)
    
    return f"Message sent to {agent_name}"

def get_responses(agent_name, mark_as_read=True):
    """
    Check if agent has responded
    
    Args:
        agent_name: Name of the agent
        mark_as_read: Whether to mark messages as read
        
    Returns:
        List of unread messages or status message
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    outbox_path = os.path.join(agent_dir, "outbox.json")
    
    if not os.path.exists(agent_dir):
        return f"Error: Agent '{agent_name}' does not exist"
    
    if not os.path.exists(outbox_path):
        return "No responses yet"
    
    with open(outbox_path, 'r') as f:
        try:
            outbox = json.load(f)
        except json.JSONDecodeError:
            return "Error reading outbox"
    
    # Get unread messages
    unread = [m for m in outbox.get("messages", []) if not m.get("read", False)]
    
    # Mark as read if requested
    if mark_as_read and unread:
        for m in outbox["messages"]:
            if not m.get("read", False):
                m["read"] = True
        
        with open(outbox_path, 'w') as f:
            json.dump(outbox, f, indent=2)
    
    if not unread:
        return "No unread responses"
    
    # Format the responses
    formatted_responses = []
    for msg in unread:
        timestamp = datetime.fromtimestamp(msg.get("timestamp", 0)).strftime("%Y-%m-%d %H:%M:%S")
        formatted_responses.append(f"[{timestamp}] {msg.get('content', '')}")
    
    return formatted_responses

def log_message(agent_name, message_type, content):
    """
    Log a message in the agent's session log
    
    Args:
        agent_name: Name of the agent
        message_type: Type of message (Input/Response)
        content: Message content
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    log_path = os.path.join(agent_dir, "session_log.md")
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Create or update log
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            log_content = f.read()
    else:
        log_content = f"# {agent_name.title()}'s Session Log\n\n"
    
    # Check if we already have a section for today
    if f"## Session: {today}" in log_content:
        # Append to today's section
        log_content += f"\n### {message_type}\n```\n{content}\n```\n"
    else:
        # Create a new section for today
        log_content += f"\n## Session: {today}\n\n### {message_type}\n```\n{content}\n```\n"
    
    # Save updated log
    with open(log_path, 'w') as f:
        f.write(log_content)

def respond_to_message(agent_name, response):
    """
    Add a response from the agent to their outbox
    
    Args:
        agent_name: Name of the agent
        response: Response content
        
    Returns:
        Status message
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    outbox_path = os.path.join(agent_dir, "outbox.json")
    
    # Create or update outbox
    if os.path.exists(outbox_path):
        with open(outbox_path, 'r') as f:
            try:
                outbox = json.load(f)
            except json.JSONDecodeError:
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
    with open(outbox_path, 'w') as f:
        json.dump(outbox, f, indent=2)
    
    # Log the response
    log_message(agent_name, "Response", response)
    
    return f"Response added for {agent_name}"

def list_agents():
    """List all available agents"""
    if not os.path.exists(AGENTS_DIR):
        return "No agents directory found"
    
    agents = [d for d in os.listdir(AGENTS_DIR) 
              if os.path.isdir(os.path.join(AGENTS_DIR, d))]
    
    if not agents:
        return "No agents found"
    
    return agents

def create_agent(agent_name):
    """
    Create a new agent with basic structure
    
    Args:
        agent_name: Name for the new agent
        
    Returns:
        Status message
    """
    agent_dir = os.path.join(AGENTS_DIR, agent_name)
    
    # Check if agent already exists
    if os.path.exists(agent_dir):
        return f"Error: Agent '{agent_name}' already exists"
    
    # Create agent directory
    os.makedirs(agent_dir, exist_ok=True)
    
    # Create basic files
    with open(os.path.join(agent_dir, "personality.md"), 'w') as f:
        f.write(f"# {agent_name.title()}\n\n## Core Identity\n- Add personality traits here\n\n## Knowledge & Expertise\n- Add areas of expertise here\n")
    
    with open(os.path.join(agent_dir, "memory.md"), 'w') as f:
        f.write(f"# {agent_name.title()}'s Memory Database\n\n## Project Knowledge\n- Initial memory entries go here\n")
    
    with open(os.path.join(agent_dir, "inbox.json"), 'w') as f:
        json.dump({"messages": []}, f, indent=2)
    
    with open(os.path.join(agent_dir, "outbox.json"), 'w') as f:
        json.dump({"messages": []}, f, indent=2)
    
    with open(os.path.join(agent_dir, "session_log.md"), 'w') as f:
        f.write(f"# {agent_name.title()}'s Session Log\n\n## Session: {datetime.now().strftime('%Y-%m-%d')}\n\n")
    
    with open(os.path.join(agent_dir, "prompt_template.md"), 'w') as f:
        f.write(f"# {agent_name.title()} Agent Prompt Template\n\n## System Instructions\n\nYou are {agent_name.title()}. Respond in character.\n\n## Character Definition\n\n{{personality}}\n\n## Current Memory State\n\n{{memory}}\n\n## Project Context\n\n{{project_context}}\n\n## Current Message\n\n{{message}}\n\n## Response Guidelines\n\n1. Always respond in character\n2. Provide technically sound advice\n\nNow, respond to the current message as {agent_name.title()}.")
    
    return f"Agent '{agent_name}' created successfully"

def print_help():
    """Print detailed help information about the coordinator"""
    help_text = """
    AI-AGENTS-COORDINATOR-INATOR HELP
    =================================
    
    This coordinator allows you to interact with AI agents through a message-based system.
    Each agent has their own personality, memory, and reasoning capabilities.
    
    Available Commands:
    ------------------
    
    send <agent> "<message>"  - Send a message to an agent's inbox
      Options:
        --subject "Subject"   - Add a subject line
        --type [task|question|feedback|general] - Specify message type
    
    get <agent>               - Check for agent responses
      Options:
        --keep-unread         - Don't mark messages as read
    
    respond <agent> "<msg>"   - Add a response from an agent (for development)
    
    list                      - Show all available agents
    
    create <agent>            - Create a new agent with default files
    
    help                      - Show this detailed help message
    
    Examples:
    --------
    python coordinator.py send heinz "Could you review this code?"
    python coordinator.py get heinz
    python coordinator.py list
    """
    print(help_text)

def main():
    parser = argparse.ArgumentParser(description="Agent Coordinator for Notes Manager 2")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Help command
    subparsers.add_parser("help", help="Show detailed help information")
    
    # Send message command
    send_parser = subparsers.add_parser("send", help="Send a message to an agent")
    send_parser.add_argument("agent", help="Name of the agent")
    send_parser.add_argument("message", help="Message content")
    send_parser.add_argument("--subject", help="Subject line for the message")
    send_parser.add_argument("--type", choices=["task", "question", "feedback", "general"], 
                           default="general", help="Type of message")
    
    # Get responses command
    get_parser = subparsers.add_parser("get", help="Get responses from an agent")
    get_parser.add_argument("agent", help="Name of the agent")
    get_parser.add_argument("--keep-unread", action="store_true", help="Don't mark messages as read")
    
    # Respond command (for simulating agent responses)
    respond_parser = subparsers.add_parser("respond", help="Add a response from an agent")
    respond_parser.add_argument("agent", help="Name of the agent")
    respond_parser.add_argument("response", help="Response content")
    
    # List agents command
    subparsers.add_parser("list", help="List all available agents")
    
    # Create agent command
    create_parser = subparsers.add_parser("create", help="Create a new agent")
    create_parser.add_argument("agent", help="Name for the new agent")
    
    args = parser.parse_args()
    
    # Handle commands
    if args.command == "send":
        result = send_message(args.agent, args.message, subject=args.subject, message_type=args.type)
        print(result)
    elif args.command == "get":
        result = get_responses(args.agent, not args.keep_unread)
        if isinstance(result, list):
            for msg in result:
                print(msg)
                print("-" * 40)
        else:
            print(result)
    elif args.command == "respond":
        result = respond_to_message(args.agent, args.response)
        print(result)
    elif args.command == "list":
        agents = list_agents()
        if isinstance(agents, list):
            print("Available agents:")
            for agent in agents:
                print(f"- {agent}")
        else:
            print(agents)
    elif args.command == "create":
        result = create_agent(args.agent)
        print(result)
    elif args.command == "help":
        print_help()
    else:
        print("No command specified. Use 'help' for detailed information.")
        parser.print_help()

if __name__ == "__main__":
    main()
