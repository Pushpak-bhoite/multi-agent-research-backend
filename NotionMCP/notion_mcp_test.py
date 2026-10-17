import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.shared._httpx_utils import create_mcp_http_client

from notion_auth import SERVER_URL, build_notion_auth


async def main():
    http_client = create_mcp_http_client(auth=build_notion_auth())

    async with streamable_http_client(SERVER_URL, http_client=http_client) as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            print(f"\n{len(tools.tools)} Notion MCP tools:\n")

            for tool in tools.tools:
                print(f"Name: {tool.name}")
                print(f"Description: {(tool.description or '')[:200]}")
                print("-" * 50)


if __name__ == "__main__":
    asyncio.run(main())