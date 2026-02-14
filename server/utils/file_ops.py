from pathlib import Path

def read_file(filepath: Path) -> str:
    """ 
    Read the given file and return its content

    Args:
        filepath: path to the file
    Returns:
        content of the file or the error message
    """
    if not filepath:
        return "[FILE_OPS_ERROR]: filepath missing or empty."

    if not filepath.exists():
        return f"[FILE_OPS_ERROR]: file '{filepath}' does not exist."
    
    if not filepath.is_file():
        return f"[FILE_OPS_ERROR]: '{filepath}' is not a file."

    try:
        with open(file=filepath, mode="r", encoding="utf-8") as file:
            content = file.read()
            return content
    except Exception as e:
        return f"[FILE_OPS_ERROR]: while reading file: {str(e)}"
    
def write_file(filepath: Path, content:str) -> str:
    """ 
    Write content to a file.

    Args:
        filepath: path of the file to write
        content: text to write into the file
    Returns:
        success or error message
    """
    if not filepath:
        return "[FILE_OPS_ERROR]: filepath missing or empty."
    
    if not content:
        return "[FILE_OPS_ERROR]: content is missing."

    try:
        with open(file=filepath, mode="W", encoding="utf-8") as file:
            file.write(content)

        return f"Success: wrote to '{filepath}'."
    
    except Exception as e:
        return f"[FILE_OPS_ERROR] while writing file: {str(e)}"



