import subprocess

ALLOWED_PROGRAMS = {"git", "python", "pip", "mkdir", "cd"}
WORKSPACE = "../workspace"

def run_command_tool(root: str, command: str) -> str:
    """
    Run a terminal command inside the workspace directory.
    
    Args:
        root: project root of the workspace
        command: The powershell command to run.

    Return:
        The command output or an error message
    """

    command = command.split()

    if command[0] not in ALLOWED_PROGRAMS:
        return "[RUN COMMAND]: program not allowed"
    
    try:
        result = subprocess.run(
            command, 
            cwd=root, 
            capture_output=True, 
            text=True,
            timeout=30 
        )
        return result.stdout or result.stderr
    except Exception as e:
        return F"[RUN COMMAND]: Error {str(e)}"