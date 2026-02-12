import os
from fastmcp.tools import tool
NOTE_DIR = "experiment/server/storage/notes"

@tool(
        name="write-file",
        description="Overwrite the content of a file.",
)
def write_file(filename: str, content: str) -> str:
    path = os.path.join(NOTE_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    return "File written successfully."
