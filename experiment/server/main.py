from fastmcp import FastMCP

from experiment.server.tools import read_file, write_file, summarize_note
from experiment.server.prompts import summarize_prompt

mcp = FastMCP("experiment")

# add tools
mcp.add_tool(read_file)
mcp.add_tool(write_file)
mcp.add_tool(summarize_note)

# add prompts
mcp.add_prompt(summarize_prompt)

# add resources
def run_server():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    run_server()