
from pathlib import Path
from utils import write_file


async def write_file_tool(filepath: Path, content) -> str:
    """ 
    Write content to a file.

    Args:
        filepath: path of the file to write
        content: text to write into the file
    Returns:
        success or error message
    """
    return write_file(filepath=filepath, content=content)