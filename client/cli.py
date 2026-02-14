
import os
import sys
import json
import asyncio

from dotenv import load_dotenv; load_dotenv()

from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

class CustomEncoder(json.JSONDecodeError):
    def default(self, o):
        if hasattr(0, 'content'):
            return {"type": o.__class__.__name__, "content": o.content}
        return super().default(o)


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_retries=3,
    api_key=os.getenv("GROQ_API_KEY")
)

if len(sys.argv) < 2:
    print("use python client-langchain-google-genai-bind-tools <path_to_server>")
    sys.exit(1)
server_script = sys.argv[1]

server_params = StdioServerParameters(
    command='python' if server_script.endswith('.py') else 'node',
    args=[server_script]
)

mcp_client = None
async def run_agent():
    global mcp_client
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            mcp_client = type("MCPClientHolder", (), {"session": session})
            tools = await load_mcp_tools(session)
            agent = create_agent(llm, tools)
            print("MCP client started, type 'quit' to exit.")

            while True:
                query = input("\nQuery: ").strip()
                if query.lower() == 'quit':
                    break

                response = await agent.ainvoke({
                    "messages": [HumanMessage(content=query)]
                })

                try:
                    formatted = json.dumps(response, indent=2, cls=CustomEncoder)
                except Exception as e:
                    formatted = str(response)

                print("\Response: ")
                print(formatted)
    return


if __name__ == "__main__":
    asyncio.run(run_agent())















