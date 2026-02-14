from pathlib import Path
from typing import Any

IGNORE_DIRS = {".venv", "node_modules", "__pycache__"}
MAX_RESULTS = 50

def search_code_tool(directory:str, query: str, file_pattern: str) -> str:
    """
    Search for text inside source files.

    Args:
        directory: root folder to search
        query: text to search
        file_pattern: file fileter (only the extention eg:- py, go, rust, js)

    Returns:
        list of marches with file path and line numbers
    """
    root = Path(directory)
    if not root.exists():
        return f"[SEARCH_ERROR] Directory not found: {directory}"

    if not query:
        return "[SEARCH_ERROR] Empty query."

    if not file_pattern:
        return "[SEARCH_ERROR] Empty file_pattern."

    results = []
    file_pattern = f"*.{file_pattern}"

    for file in root.rglob(file_pattern):
        if any(part in IGNORE_DIRS for part in file.parts):
            continue

        try:
            with open(file=file, mode="r", encoding="utf-8") as f:
                for i, line in enumerate(f, start=1):
                    if query.lower() in line.lower().strip():
                        results.append(f"{file}:{i} -> {line.strip()}")
                    
                    if len(results) >= MAX_RESULTS:
                        return "\n".join(results)

        except Exception as e:
            continue
    
    if not results:
        return "No match found."
    
    return "\n".join(results[:50]) # limit the outptus
        


