from mcp.server.fastmcp import FastMCP
from codebase_tools import read_file_tool, write_file_tool, summarize_file_tool, search_code_tool, run_command_tool

mcp = FastMCP(
    name="Local codebase analyst mcp server",
)

# register codebase to the mcp server
mcp.add_tool(fn=read_file_tool, name="read_files")
mcp.add_tool(fn=write_file_tool, name="write_files")
mcp.add_tool(fn=summarize_file_tool, name="summarize_file_tool")
mcp.add_tool(fn=search_code_tool, name="search_code_tool")
mcp.add_tool(fn=run_command_tool, name="run_command_tool")


def main():
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()


