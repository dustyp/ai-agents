# Procedure Execution Visualization Example

This document demonstrates the proper visualization of procedure execution following the VISUALIZE_PROCEDURE_EXECUTION rule.

## Example: prepare_for_sleep Procedure

When executing the prepare_for_sleep procedure, the visualization should look like this at different stages:

### Starting the Procedure

```
PROCEDURE: prepare_for_sleep

STEPS:
▶️ 1. SUMMARIZE EVIL SCHEME: Document current ticket progress
⬜ 2. LIST ALL ACTIVE SCHEMES: Document all related tickets
⬜ 3. IDENTIFY CURRENT STAGE: Document position in workflow
⬜ 4. CREATE RESUMPTION PLAN: Clear instructions for next session
⬜ 5. RECORD EMOTIONAL STATE: Because evil scientists have feelings!
⬜ 6. FORMAT FOR SLEEP MODE: Prepare information for state saving
⬜ 7. COMPLETE SESSION STATE: Finalize session documentation
⬜ 8. UPDATE SESSION LOG: Add reflection and learning
⬜ 9. UPDATE KNOWLEDGE GRAPH: Backup to memory tool

VERIFICATION: Pending
```

### Mid-Procedure (After Step 4)

```
PROCEDURE: prepare_for_sleep

STEPS:
✅ 1. SUMMARIZE EVIL SCHEME: Document current ticket progress
✅ 2. LIST ALL ACTIVE SCHEMES: Document all related tickets
✅ 3. IDENTIFY CURRENT STAGE: Document position in workflow
✅ 4. CREATE RESUMPTION PLAN: Clear instructions for next session
▶️ 5. RECORD EMOTIONAL STATE: Because evil scientists have feelings!
⬜ 6. FORMAT FOR SLEEP MODE: Prepare information for state saving
⬜ 7. COMPLETE SESSION STATE: Finalize session documentation
⬜ 8. UPDATE SESSION LOG: Add reflection and learning
⬜ 9. UPDATE KNOWLEDGE GRAPH: Backup to memory tool

VERIFICATION: Pending
```

### Verification Phase (After All Steps)

```
PROCEDURE: prepare_for_sleep

STEPS:
✅ 1. SUMMARIZE EVIL SCHEME: Document current ticket progress
✅ 2. LIST ALL ACTIVE SCHEMES: Document all related tickets
✅ 3. IDENTIFY CURRENT STAGE: Document position in workflow
✅ 4. CREATE RESUMPTION PLAN: Clear instructions for next session
✅ 5. RECORD EMOTIONAL STATE: Because evil scientists have feelings!
✅ 6. FORMAT FOR SLEEP MODE: Prepare information for state saving
✅ 7. COMPLETE SESSION STATE: Finalize session documentation
✅ 8. UPDATE SESSION LOG: Add reflection and learning
✅ 9. UPDATE KNOWLEDGE GRAPH: Backup to memory tool

VERIFICATION:
▶️ Checking verification criteria...
⬜ Evil scheme properly documented with specific details
⬜ All required session_state.md sections completed
⬜ session_log.md updated with complete session entry
⬜ All file updates actually performed
⬜ Next steps clearly outlined
⬜ All active tasks and context properly preserved
⬜ Knowledge graph memory backup completed
```

### Completion Confirmation

```
PROCEDURE: prepare_for_sleep

STEPS:
✅ 1. SUMMARIZE EVIL SCHEME: Document current ticket progress
✅ 2. LIST ALL ACTIVE SCHEMES: Document all related tickets
✅ 3. IDENTIFY CURRENT STAGE: Document position in workflow
✅ 4. CREATE RESUMPTION PLAN: Clear instructions for next session
✅ 5. RECORD EMOTIONAL STATE: Because evil scientists have feelings!
✅ 6. FORMAT FOR SLEEP MODE: Prepare information for state saving
✅ 7. COMPLETE SESSION STATE: Finalize session documentation
✅ 8. UPDATE SESSION LOG: Add reflection and learning
✅ 9. UPDATE KNOWLEDGE GRAPH: Backup to memory tool

VERIFICATION:
✅ Evil scheme properly documented with specific details
✅ All required session_state.md sections completed
✅ session_log.md updated with complete session entry
✅ All file updates actually performed
✅ Next steps clearly outlined
✅ All active tasks and context properly preserved
✅ Knowledge graph memory backup completed

RESULT: Procedure successfully completed ✅
NEXT: Delivering Heinz's theatrical farewell
```

## Guidelines for Procedure Visualization

1. Always display all steps at the beginning of the procedure
2. Use consistent indicators:
   - ▶️ Current step being executed
   - ✅ Completed step
   - ⬜ Pending step
   - ❌ Failed step (when applicable)
3. Update the visualization after each step completion
4. Include verification section at the end
5. Show clear completion confirmation when done
6. Indicate next actions after procedure completion