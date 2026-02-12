
import os
from pathlib import Path


async def write_file_tool(filepath: Path, content) -> str:
    """ 
    Write content to a file.

    Args:
        filepath: path of the file to write
        content: text to write into the file
    Returns:
        success or error message
    """
    if not filepath:
        return "[WRITE_FILE_ERROR]: filepath missing or empty."

    try:
        with open(file=filepath, mode="W", encoding="utf-8") as file:
            await file.write(content)

        return f"Success: wrote to '{filepath}'."
    
    except Exception as e:
        return f"Error while writing file: {str(e)}"