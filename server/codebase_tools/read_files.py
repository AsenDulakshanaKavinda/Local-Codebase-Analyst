
import os
from pathlib import Path


async def read_file_tool(filepath: Path) -> str:
    """ 
    Read the given file and return its content

    Args:
        filepath: path to the file
    Returns:
        content of the file or the error message
    """
    if not filepath:
        return "[READ_FILE_ERROR]: filepath missing or empty."

    if not filepath.exists():
        return f"[READ_FILE_ERROR]: file '{filepath}' does not exist."
    
    if not filepath.is_file():
        return f"[READ_FILE_ERROR]: '{filepath}' is not a file."

    try:
        with open(file=filepath, mode="r", encoding="utf-8") as file:
            content = await file.read()
            return content
    except Exception as e:
        return f"[READ_FILE_ERROR]: while reading file: {str(e)}"