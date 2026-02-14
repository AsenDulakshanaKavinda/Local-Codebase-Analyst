from pathlib import Path
from typing import Any


WORKSPACE = Path("../workspace")



def search_code_tool(query: str, file_pattern: str) -> str:
    """
    Search for text inside source files.

    Args:
        query: text to search
        file_pattern: file fileter 

    Returns:
        list of marches with file path and line numbers
    """

    if not query:
        return "[SEARCH_ERROR] Empty query."

    if not file_pattern:
        return "[SEARCH_ERROR] Empty file_pattern."

    results = []

    for file in WORKSPACE.rglob(file_pattern):
        try:
            with open(file=file, mode="r", encoding="utf-8") as f:
                for i, line in enumerate(f, start=1):
                    if query.lower() in line.lower():
                        results.append(f"{file}:{i} -> {line.strip()}")
        except Exception as e:
            return f"[SEARCH_ERROR] error reading file {file}: {str(e)}."
    
    if not results:
        return "No match found."
    
    return "\n".join(results[:50]) # limit the outptus
        


