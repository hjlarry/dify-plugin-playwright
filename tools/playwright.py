from collections.abc import Generator
from typing import Any, Literal

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from playwright.sync_api import sync_playwright


def run_playwright(uri: str, commands: str, uri_type: Literal["ws", "cdp"]) -> str | bytes:
    with sync_playwright() as p:
        if uri_type == "ws":
            browser = p.chromium.connect(ws_endpoint=uri, timeout=3000)
        else:
            browser = p.chromium.connect_over_cdp(endpoint_url=uri, timeout=3000)
        local_vars = {"browser": browser}
        exec(commands, {}, local_vars)
        result = local_vars.get("result")

    return result


class PlaywrightTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        commands = tool_parameters.get("script")
        result = run_playwright(
            self.runtime.credentials.get("playwright_uri"), commands, self.runtime.credentials.get("uri_type")
        )
        if isinstance(result, str):
            yield self.create_text_message(result)
        elif isinstance(result, bytes):
            yield self.create_blob_message(blob=result, meta={"mime_type": "image/png"})
        else:
            yield self.create_text_message("Nothing output")
