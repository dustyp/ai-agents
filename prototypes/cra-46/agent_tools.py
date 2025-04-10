from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI # Or Claude if you prefer

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)  # Replace with your LLM and settings

def summarize_text(text: str) -> str:
    """Summarizes a given text using the LLM."""
    prompt = f"Please summarize the following text:\n{text}"
    return llm.invoke(prompt).content

summarize_tool = Tool(
    name="text_summarizer",
    func=summarize_text,
    description="Useful for summarizing text. Input: The text to summarize.",
)