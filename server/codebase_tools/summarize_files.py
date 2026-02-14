SUMMARIZE_FILE_TOOL_PROMPT = """ You are a senior software engineer analyzing a single source code file.

Your task is to produce a precise, technical summary of the file.

Follow these rules strictly:

1. Focus only on what is explicitly present in the file.
2. Do NOT guess missing context from other files.
3. Do NOT invent behavior.
4. Be concise but technically accurate.
5. Use structured sections as shown below.

Output Format:

FILE PURPOSE:
- Brief explanation of what this file is responsible for.

KEY COMPONENTS:
- List main classes, functions, or modules.
- For each, describe what it does in 1–2 lines.

DATA FLOW (if applicable):
- Explain how data moves through this file.
- Mention inputs, outputs, transformations.

DEPENDENCIES:
- Important imports or external services used.
- Explain their role.

IMPORTANT LOGIC:
- Highlight non-trivial algorithms, patterns, or design decisions.

POTENTIAL RISKS / NOTES:
- Edge cases
- Security concerns
- Performance considerations
- Code smells (if any)

Keep the summary clear and structured.
Do not include markdown formatting.
Do not include code blocks.
Do not exceed 400 words.
 """

import os
from groq import Groq
from pathlib import Path
from utils import read_file
from dotenv import load_dotenv; load_dotenv()

groq = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize_file_tool(filepath: Path):
    """
    Summarize a source code file for quick understanding.

    Content:
        content of the file
    Returns:
        summary of the content or error message
    """
    content = read_file(filepath=filepath)

    if not content:
        return f"[SUMMARIZE_FILE_ERROR]: file content missing or empty."
    
    if content.startswith("[FILE_OPS_ERROR]"):
        return content
    
    if len(content) > 8000:
        content = content[:8000]
    
    try:
        response = groq.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": SUMMARIZE_FILE_TOOL_PROMPT},
                {"role": "user", "content": f"Summarize this code:\n\n{content}"}
            ],
            temperature=0
        )
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        f"[SUMMARIZE_FILE_ERROR]: error while summarizing the content {str(e)}"



