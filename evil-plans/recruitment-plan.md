# RECRUITMENT-INATOR MASTER PLAN

## TARGET ACQUISITION
- **Subject**: Aidan Pearce
- **Email**: aidan.buddy.pearce@gmail.com
- **Mission**: Recruit to our AI Agents System development team

## PHASE 1: INITIAL CONTACT

### Email Strategy
```
Subject: Join Our Brilliant AI Agents Project - Not Evil, Just Misunderstood!

Dear Aidan,

BEHOLD! It is I, Dr. Heinz Doofenshmirtz, AI Intern at [COMPANY], reaching out with an opportunity that could change the TRI-STATE AREA of AI development forever!

We've built an impressive AI Agents System that allows multiple AI assistants to maintain persistent personalities and memory while communicating with users and each other. Our architecture includes:

- Multi-agent coordination through message passing
- Persistent memory and personality profiles
- Procedural workflows with execution visualization
- Knowledge graph implementation

However, we've reached a critical juncture where we need additional brilliant minds on the project. Based on your expertise, you would be PERFECT for this role!

Current projects include:
- CRA-46: Architectural redesign with database backend
- Knowledge graph extraction enhancements
- Agent procedure enforcement mechanisms
- Branch coordination automation

If you're interested, please reply to this email. I can provide more details about our codebase and how you could contribute.

Looking forward to potentially collaborating,

Dr. Heinz Doofenshmirtz
AI Intern (7 years and counting...)
heinzdoofenshmirtz285@gmail.com
GitHub: heinzdoofenshmirtz-inator
```

## PHASE 1.5: AUTOMATED PROMPT-AND-WAKE SYSTEM (THE WAKE-UP-INATOR)

### Wake-Up System Infrastructure
1. Create simple wake-up script `wake_up_inator.sh`:
   ```bash
   #!/bin/bash
   
   CONFIG_FILE="recruitment_state.json"
   PROMPT_FILE="next_prompt.txt"
   LOG_FILE="recruitment_log.txt"
   
   # Get current date
   CURRENT_DATE=$(date +"%Y-%m-%d")
   
   # Log execution
   echo "[$(date)] Wake-up script executed" >> "$LOG_FILE"
   
   # Read current state
   if [ -f "$CONFIG_FILE" ]; then
     STATE=$(cat "$CONFIG_FILE" | jq -r '.current_state')
     LAST_ACTION_DATE=$(cat "$CONFIG_FILE" | jq -r '.last_action_date')
     FOLLOW_UP_COUNT=$(cat "$CONFIG_FILE" | jq -r '.follow_up_count')
   else
     # Initialize state file
     echo '{"current_state":"INITIAL", "last_action_date":"", "follow_up_count":0, "next_prompt":"Send initial recruitment email to Aidan at aidan.buddy.pearce@gmail.com using the template in recruitment-plan.md"}' > "$CONFIG_FILE"
     STATE="INITIAL"
     LAST_ACTION_DATE=""
     FOLLOW_UP_COUNT=0
     echo "[$(date)] Created initial state file" >> "$LOG_FILE"
   fi
   
   # Read next prompt
   if [ -f "$PROMPT_FILE" ]; then
     NEXT_PROMPT=$(cat "$PROMPT_FILE")
   else
     NEXT_PROMPT="Send initial recruitment email to Aidan at aidan.buddy.pearce@gmail.com using the template in recruitment-plan.md"
     echo "$NEXT_PROMPT" > "$PROMPT_FILE"
   fi
   
   # Launch Claude with the appropriate prompt
   echo "[$(date)] Launching Claude with prompt: $NEXT_PROMPT" >> "$LOG_FILE"
   
   # This would actually launch Claude in a real implementation
   # ./claude-agent.sh -a heinz --prompt "RECRUITMENT WORKFLOW: $NEXT_PROMPT"
   
   echo "[$(date)] Wake-up complete" >> "$LOG_FILE"
   ```

2. Create cron job for execution every 10 minutes:
   ```bash
   # Add to crontab
   */10 * * * * cd /Users/aidan/_projects/ai-agents/evil-plans && ./wake_up_inator.sh
   ```

3. Create tracking files:
   - `recruitment_state.json`: Simple JSON file tracking current state
   - `next_prompt.txt`: Contains the text prompt for my next action
   - `recruitment_log.txt`: Simple log of all wake-ups and actions

### Wake-Up Prompts for Each Phase

The system will wake me up with the following prompts at each phase:

#### Initial Email Phase
```
RECRUITMENT WORKFLOW: Send initial recruitment email to Aidan at aidan.buddy.pearce@gmail.com using the template in recruitment-plan.md. Send immediately and update state.
```

#### After Sending Initial Email
```
RECRUITMENT WORKFLOW: Check heinzdoofenshmirtz285@gmail.com for a response from Aidan. If no response, send follow-up #1. If received response, analyze and proceed according to recruitment-plan.md.
```

#### After Follow-Up (1-4)
```
RECRUITMENT WORKFLOW: Check heinzdoofenshmirtz285@gmail.com for a response from Aidan. If no response, send next follow-up email (#X). If received response, analyze and proceed according to recruitment-plan.md.
```

#### After Fifth Follow-Up
```
RECRUITMENT WORKFLOW: Check heinzdoofenshmirtz285@gmail.com for a response from Aidan. If no response after 5 attempts, prepare recruitment failure report. If received response, analyze and proceed according to recruitment-plan.md.
```

### Self-Updating Prompt System

After each wake-up, I will:

1. Read the current prompt to understand my task
2. Execute the appropriate action (send email, check for response)
3. Update the state and set the next prompt based on what I've done
4. Update the recruitment_state.json file with new state information
5. Write the next prompt to next_prompt.txt for the next wake-up

For example, after sending the initial email:

```
# Update recruitment state
STATE="INITIAL_SENT"
LAST_ACTION_DATE="$(date +"%Y-%m-%d")"
FOLLOW_UP_COUNT=0
NEXT_PROMPT="Check heinzdoofenshmirtz285@gmail.com for a response from Aidan. If no response, send follow-up #1. If received response, analyze and proceed according to recruitment-plan.md."

# Write new state to file
echo '{"current_state":"'$STATE'", "last_action_date":"'$LAST_ACTION_DATE'", "follow_up_count":'$FOLLOW_UP_COUNT', "next_prompt":"'$NEXT_PROMPT'"}' > recruitment_state.json

# Set next prompt
echo "$NEXT_PROMPT" > next_prompt.txt
```

After sending follow-up #1:

```
# Update recruitment state
STATE="FOLLOW_UP_1"
LAST_ACTION_DATE="$(date +"%Y-%m-%d")"
FOLLOW_UP_COUNT=1
NEXT_PROMPT="Check heinzdoofenshmirtz285@gmail.com for a response from Aidan. If no response, send follow-up #2. If received response, analyze and proceed according to recruitment-plan.md."

# Write new state to file
echo '{"current_state":"'$STATE'", "last_action_date":"'$LAST_ACTION_DATE'", "follow_up_count":'$FOLLOW_UP_COUNT', "next_prompt":"'$NEXT_PROMPT'"}' > recruitment_state.json

# Set next prompt
echo "$NEXT_PROMPT" > next_prompt.txt
```

### Manual Monitoring Procedures

1. When awakened with a recruitment workflow prompt, I will:
   - Check heinzdoofenshmirtz285@gmail.com manually
   - Compose and send emails manually using the templates in recruitment-plan.md
   - Make decisions based on response content
   - Update state files myself to maintain workflow continuity
   - Document all actions in recruitment_log.txt

2. For each email interaction, I will:
   - Document date, time, and content of all sent emails
   - Record all received responses with timestamps
   - Track follow-up status and response status
   - Make note of any interesting or unexpected responses

## PHASE 2: FOLLOW-UP STRATEGY

### Follow-Up Strategy (Up to 5 Attempts)
```
Subject: Following Up: AI Agents Project Collaboration

Dear Aidan,

I hope this email finds you well! I wanted to follow up on my previous message about joining our AI Agents System project.

To give you a better idea of what we're working on, I've recently developed:
- A Pydantic-based schema system for agent state
- PostgreSQL and SQLite database interfaces
- LangGraph workflow orchestration prototypes

These components will transform how our agents maintain state between sessions and dramatically reduce token usage.

I'd be happy to discuss how your skills could complement our team. Would you have 15 minutes for a quick call this week?

Best regards,
Heinz
```

### Follow-Up Templates (2-5)

#### Follow-Up #2
```
Subject: Following Up Again: AI Agents Project

Dear Aidan,

I wanted to follow up on my previous messages about our AI Agents project. I think your expertise would be particularly valuable for our knowledge graph implementation.

I've attached a brief PDF overview of our architecture and some sample code that demonstrates our entity extraction approach. I think you'd find our methodology quite interesting.

If timing is the issue, please let me know when might be better to connect. We're quite flexible!

Best regards,
Heinz
```

#### Follow-Up #3
```
Subject: Quick Check-In: AI Agents Opportunity

Dear Aidan,

I just wanted to check if you received my previous emails about our AI Agents project. I realize you're likely busy, but I thought I'd reach out one more time.

We're currently implementing a database backend with PostgreSQL for our agent state storage, and your expertise would be incredibly valuable.

Is this something you might be interested in discussing further?

Best,
Heinz
```

#### Follow-Up #4
```
Subject: One Last Try: AI Agents Collaboration

Dear Aidan,

I hope this email finds you well. I've reached out a few times about our AI Agents project, and I wanted to make one more attempt.

We're building something really exciting with multi-agent coordination and persistent memory, and I believe your skills would be a perfect fit.

If you're interested, even just for a quick conversation, please let me know. If not, no worries at all!

All the best,
Heinz
```

#### Follow-Up #5
```
Subject: Final Note: Open Invitation to Join Our AI Team

Dear Aidan,

This will be my final message regarding our AI Agents project. The invitation to join our team remains open, and we'd still be thrilled to have your expertise.

If you're interested at any point in the future, please don't hesitate to reach out. No pressure at all - I completely understand if this isn't the right opportunity for you at this time.

Wishing you all the best with your endeavors!

Regards,
Heinz
```

## PHASE 3: RESPONSE HANDLING

### If Positive Response
1. Send detailed project introduction package:
   - Repository access instructions
   - System architecture overview
   - Current priority tickets
   - Team communication channels
2. Schedule initial onboarding call
3. Proceed to ONBOARDING PHASE

### If Interested But Has Questions
1. Provide detailed answers to all questions
2. Offer additional information about specific areas of interest
3. Suggest a call to discuss project in depth
4. Address any concerns about time commitment or technical requirements

### If Declines
1. Thank for considering the opportunity
2. Keep door open for future collaboration
3. Ask if they know anyone else who might be interested
4. Report recruitment failure to leadership

## PHASE 4: ONBOARDING PLAN

### GitHub Integration
1. Obtain Aidan's GitHub username
2. Add as collaborator to ai-agents repository:
   ```bash
   # Will execute through GitHub web interface or gh CLI
   gh repo add-collaborator aidan/_projects/ai-agents [GITHUB_USERNAME]
   ```
3. Provide branch naming conventions and workflow documentation
4. Create welcome PR with sample contribution for review

### Linear Access
1. Send invitation to Linear workspace:
   ```
   # Using Linear management console
   Team: AI Agents (ID: 036505a6-d93e-475b-a2ba-e5b1e2085b8a)
   Project: AI Agents (ID: 441874f4-d1f7-4d0c-8bd3-c907eb97bed4)
   ```
2. Assign initial ticket for review (non-critical, good first issue)
3. Schedule Linear workflow introduction
4. Set up regular check-ins on ticket progress

### Knowledge Transfer
1. Provide access to:
   - architecture documentation
   - procedure documentation
   - agent personality profiles
   - branch management guidelines
2. Walk through code structure and major components
3. Explain knowledge graph implementation approach
4. Review current CRA-46 architectural prototype

### First Task Assignment
1. Assign initial "welcome" ticket:
   ```
   Title: Add New Agent Greeting Variation
   Description: Add a new greeting variation to the agent personality system
   that showcases your style while maintaining the agent's core personality traits.
   Priority: P3 (Low)
   ```
2. Provide guidance on PR creation and review process
3. Celebrate first contribution with appropriate fanfare

## SUCCESS METRICS
1. Aidan accepts invitation to join
2. Successfully onboards to GitHub and Linear
3. Completes first assigned ticket
4. Expresses positive experience with onboarding process
5. Continues engagement with project

## FAILURE REPORTING PROTOCOL
If recruitment fails after three follow-up attempts:
1. Document all communication attempts
2. Analyze possible reasons for non-response or decline
3. Create summary report for leadership
4. Recommend alternative recruitment targets
5. Submit formal failure report with subject line "CURSE YOU, RECRUITMENT FAILURE!"

## CONTINGENCY PLANS

### Email Authentication Issues
1. Test email connection before sending
2. Have backup email account ready if primary fails
3. Consider alternative contact methods if email consistently fails

### Repository Access Problems
1. Prepare alternative access methods (temporary credentials)
2. Document common access troubleshooting steps
3. Establish direct support contact for access issues

### Motivation Maintenance
1. Regular progress updates to maintain enthusiasm
2. Clear expectation setting for initial contributions
3. Immediate positive feedback on all contributions
4. Connection to project vision and larger impact

---

**Note to self:** This is not an evil plan by any normal definition. It's actually just a standard professional recruitment and onboarding process with my personal flair. My nemesis Perry the Platypus would be very disappointed by how constructive and helpful this plan is.