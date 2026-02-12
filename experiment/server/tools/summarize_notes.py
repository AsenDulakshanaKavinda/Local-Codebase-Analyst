import os
from fastmcp.tools import tool

@tool(
        name="summarize-note",
        description="Summarize a give content.",
)
def summarize_note(content: str) -> str:
    return {
        "role": "assistant",
        "content": f"Summarize the following:\n\n{content}"
    }