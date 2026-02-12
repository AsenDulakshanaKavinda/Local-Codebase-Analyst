from mcp.server.fastmcp import FastMCP
from codebase_tools import read_file_tool, write_file_tool

mcp = FastMCP(
    name="Local codebase analyst mcp server",
)

# register codebase to the mcp server
mcp.add_tool(fn=read_file_tool, name="read_files")
mcp.add_tool(fn=write_file_tool, name="write_files")


def main():
    print("done")
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
