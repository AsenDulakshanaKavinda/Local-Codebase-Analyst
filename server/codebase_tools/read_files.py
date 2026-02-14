
from pathlib import Path
from utils import read_file, log



async def read_file_tool(filepath: Path) -> str:
    """ 
    Read the given file and return its content

    Args:
        filepath: path to the file
    Returns:
        content of the file or the error message
    """
    return read_file(filepath=filepath)