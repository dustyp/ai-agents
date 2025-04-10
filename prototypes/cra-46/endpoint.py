from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import asyncio
from agent_state import AgentState
from workflow import graph

app = FastAPI()

@app.post("/process_input/")
async def process_input(request: Request):
    """Receives user input and returns agent response."""
    try:
        data = await request.json()
        user_input = data.get("user_input")

        if not user_input:
            raise HTTPException(status_code=400, detail="Missing user_input")

        # Initialize the agent state
        initial_state = AgentState(user_input=user_input, conversation_history={})

        # Run the LangGraph graph
        results = await graph.ainvoke(initial_state)  # Use ainvoke for async

        # Access the final state and extract the response
        final_state = results
        agent_response = final_state.agent_response

        print(f"Response: {agent_response}")

        return JSONResponse({"agent_response": agent_response})

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))