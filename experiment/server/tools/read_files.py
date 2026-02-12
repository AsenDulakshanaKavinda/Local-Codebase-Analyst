import os
from fastmcp.tools import tool

NOTE_DIR = "experiment/server/storage/notes"

@tool(
        name="read-file",
        description="Read the content of a file.",
)
def read_file(filename: str) -> str:
    """ Read a note from storage """
    path = os.path.join(NOTE_DIR, filename)
    with open(path, 'r') as f:
        return f.read()

