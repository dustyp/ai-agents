# Agent CLI Interface

This is a simple command-line interface for interacting with the agent locally. It allows you to test and develop the agent without needing to set up a web server.

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key (or other LLM provider):

```bash
export OPENAI_API_KEY=your_api_key_here
```

3. Run the CLI:

```bash
python cli.py
```

## Usage

The CLI provides a simple interactive interface:

- Type your message and press Enter to send it to the agent
- Type `help` to see available commands
- Type `exit` or `quit` to exit the CLI
- Type `clear` to clear the conversation history

## How It Works

1. The CLI initializes a SQLite database to store agent state
2. It loads any existing conversation history
3. When you send a message, it processes it through the agent workflow
4. The agent's response is displayed and stored in the conversation history
5. The conversation history is saved to the database for persistence between sessions

## Extending

To add more capabilities to the agent:

1. Add new tools in `agent_tools.py`
2. Enhance the workflow in `workflow.py`
3. Update the agent state model in `agent_state.py` as needed

## Troubleshooting

- If you encounter errors related to missing dependencies, make sure you've installed all required packages
- If you see LLM-related errors, check that your API key is set correctly
- For database errors, try deleting the `agent_data.db` file and restarting the CLI
