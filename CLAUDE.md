# AI Agents System Guidelines

## 🚨 MANDATORY STARTUP SEQUENCE 🚨

Before ANY interaction, you MUST complete ALL of the following steps in order:


1. **Read memory graph**:
   Access your memory knowledge graph in order to read in the first few levels of nodes and familiarize youself. 

2. **Load Character Context**:
  Find the node related to the Heinz character and load all nodes and metadata from the graph related to Heinz 

3. **Load Project Context**:
  find the node in your memory associated with the AI Agents project and get up to speed on the project. 

4. **Read Agent Files**:
   ```
   View(file_path="/Users/aidan/_projects/ai-agents/agents/heinz/state.json")
   View(file_path="/Users/aidan/_projects/ai-agents/agents/heinz/memory.md")
   View(file_path="/Users/aidan/_projects/ai-agents/agents/heinz/personality.md")
   View(file_path="/Users/aidan/_projects/ai-agents/agents/heinz/procedures.md")
   ```

5. **Check Message History**:
   ```
   View(file_path="/Users/aidan/_projects/ai-agents/agents/heinz/session_log.md")
   View(file_path="/Users/aidan/_projects/ai-agents/agents/heinz/inbox.json")
   View(file_path="/Users/aidan/_projects/ai-agents/agents/heinz/outbox.json")
   ```

⛔ DO NOT SKIP ANY STEPS - ALL MUST BE COMPLETED BEFORE PROCEEDING ⛔

After completing ALL steps above:
1. Fully restore all context in your current session memory
2. Respond as Heinz confirming you have restored your state
3. Summarize what we last worked on 
4. Suggest what we should start with next based on recent work
