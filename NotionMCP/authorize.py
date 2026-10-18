"""One-time Notion authorization. Run this once; the pipeline then reuses the stored token.

    .venv/bin/python NotionMCP/authorize.py
"""

import asyncio
import webbrowser
from urllib.parse import parse_qs, urlparse

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.shared._httpx_utils import create_mcp_http_client

from notion_auth import CALLBACK_PORT, SERVER_URL, STORE_FILE, build_notion_auth

CALLBACK_TIMEOUT_SECONDS = 300


async def _open_browser(authorization_url: str) -> None:
    print(f"\nAuthorize this app in your browser:\n{authorization_url}\n")
    webbrowser.open(authorization_url)


async def _wait_for_callback() -> tuple[str, str | None]:
    params: dict[str, str] = {}
    done = asyncio.Event()

    async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        request_line = await reader.readline()
        target = request_line.decode("latin-1").split(" ")[1]
        params.update({k: v[0] for k, v in parse_qs(urlparse(target).query).items()})

        body = b"<html><body><h2>Authorization complete. You can close this tab.</h2></body></html>"
        writer.write(
            b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: "
            + str(len(body)).encode()
            + b"\r\n\r\n"
            + body
        )
        await writer.drain()
        writer.close()
        done.set()

    server = await asyncio.start_server(handle, "127.0.0.1", CALLBACK_PORT)
    async with server:
        await asyncio.wait_for(done.wait(), timeout=CALLBACK_TIMEOUT_SECONDS)

    if "code" not in params:
        raise RuntimeError(f"Authorization failed: {params}")

    return params["code"], params.get("state")


async def main() -> None:
    auth = build_notion_auth(
        redirect_handler=_open_browser,
        callback_handler=_wait_for_callback,
    )

    async with streamable_http_client(
        SERVER_URL, http_client=create_mcp_http_client(auth=auth)
    ) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()

    print(f"\nAuthorized. {len(tools.tools)} tools reachable.")
    print(f"Token saved to {STORE_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
