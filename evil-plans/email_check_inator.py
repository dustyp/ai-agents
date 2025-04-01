#!/usr/bin/env python3
import os
import json
import datetime
import subprocess
from email.utils import parsedate_to_datetime

CONFIG_FILE = "recruitment_config.json"
LOG_FILE = "recruitment_log.json"

def load_config():
    """Load recruitment configuration"""
    if not os.path.exists(CONFIG_FILE):
        # Default configuration
        config = {
            "target_email": "aidan.buddy.pearce@gmail.com",
            "initial_contact_date": datetime.datetime.now().isoformat(),
            "last_check_time": None,
            "follow_up_count": 0,
            "status": "INITIAL_SENT",  # INITIAL_SENT, FOLLOW_UP_1, FOLLOW_UP_2, FOLLOW_UP_3, RESPONDED, COMPLETE, FAILED
            "response_received": False,
            "response_content": None,
            "next_action_date": (datetime.datetime.now() + datetime.timedelta(days=5)).isoformat()
        }
        save_config(config)
        return config
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    """Save recruitment configuration"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def log_activity(activity_type, details):
    """Log recruitment activity"""
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "type": activity_type,
        "details": details
    }
    
    if not os.path.exists(LOG_FILE):
        log_data = {"entries": [log_entry]}
    else:
        with open(LOG_FILE, 'r') as f:
            log_data = json.load(f)
            log_data["entries"].append(log_entry)
    
    with open(LOG_FILE, 'w') as f:
        json.dump(log_data, f, indent=2)

def check_gmail_for_responses():
    """Check Gmail for responses using the Gmail API"""
    # This would use Gmail API but is simplified for now
    # Return mock response for demonstration
    return {
        "has_new_response": False, 
        "emails": []
    }

def determine_next_action(config):
    """Determine the next action based on current status"""
    current_status = config["status"]
    now = datetime.datetime.now()
    next_action_date = datetime.datetime.fromisoformat(config["next_action_date"])
    
    if config["response_received"]:
        return "PROCESS_RESPONSE"
        
    if now < next_action_date:
        return "WAIT"
        
    if current_status == "INITIAL_SENT":
        return "SEND_FOLLOW_UP_1"
    elif current_status == "FOLLOW_UP_1":
        return "SEND_FOLLOW_UP_2"
    elif current_status == "FOLLOW_UP_2":
        return "SEND_FOLLOW_UP_3"
    elif current_status == "FOLLOW_UP_3":
        return "REPORT_FAILURE"
    
    return "WAIT"

def take_action(action, config):
    """Take the appropriate action"""
    if action == "WAIT":
        log_activity("WAIT", "Waiting until next action date")
        return
        
    if action == "SEND_FOLLOW_UP_1":
        # This would use an email sending function
        log_activity("FOLLOW_UP", "Sent first follow-up email")
        config["status"] = "FOLLOW_UP_1"
        config["follow_up_count"] = 1
        config["next_action_date"] = (datetime.datetime.now() + datetime.timedelta(days=5)).isoformat()
        save_config(config)
        # Would trigger Claude to draft and send the follow-up
        
    elif action == "SEND_FOLLOW_UP_2":
        log_activity("FOLLOW_UP", "Sent second follow-up email")
        config["status"] = "FOLLOW_UP_2"
        config["follow_up_count"] = 2
        config["next_action_date"] = (datetime.datetime.now() + datetime.timedelta(days=5)).isoformat()
        save_config(config)
        # Would trigger Claude to draft and send the follow-up
        
    elif action == "SEND_FOLLOW_UP_3":
        log_activity("FOLLOW_UP", "Sent final follow-up email")
        config["status"] = "FOLLOW_UP_3"
        config["follow_up_count"] = 3
        config["next_action_date"] = (datetime.datetime.now() + datetime.timedelta(days=5)).isoformat()
        save_config(config)
        # Would trigger Claude to draft and send the follow-up
        
    elif action == "REPORT_FAILURE":
        log_activity("FAILURE", "Recruitment failed after three follow-ups")
        config["status"] = "FAILED"
        save_config(config)
        # Would trigger Claude to generate failure report
        
    elif action == "PROCESS_RESPONSE":
        log_activity("RESPONSE", "Processing received response")
        # Would trigger Claude to analyze response and take appropriate action

def trigger_claude_session(action_type):
    """Trigger a Claude session with appropriate prompts"""
    # Command to invoke Claude with specific context
    cmd = [
        "./claude-agent.sh", 
        "-a", "heinz",
        "--prompt", f"Execute recruitment plan action: {action_type}. Check the recruitment_config.json and recruitment_log.json in the evil-plans directory for current status."
    ]
    # In a real implementation, this would actually execute the command
    log_activity("CLAUDE_TRIGGER", f"Would trigger Claude with action: {action_type}")
    # subprocess.run(cmd)

def main():
    """Main function to check email and determine next actions"""
    config = load_config()
    email_check_result = check_gmail_for_responses()
    
    # Update last check time
    config["last_check_time"] = datetime.datetime.now().isoformat()
    
    # Check for new responses
    if email_check_result["has_new_response"]:
        config["response_received"] = True
        config["response_content"] = email_check_result["emails"]
        log_activity("RESPONSE_DETECTED", "New email response detected")
        trigger_claude_session("RESPONSE_ANALYSIS")
    
    # Determine and take next action
    next_action = determine_next_action(config)
    take_action(next_action, config)
    
    if next_action != "WAIT":
        trigger_claude_session(next_action)
    
    save_config(config)
        
if __name__ == "__main__":
    main()