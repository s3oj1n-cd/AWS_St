import json
import os
import time
from pathlib import Path

import requests

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json",
}

def request_json(url, params=None):
    for attempt in range(5):
        response = requests.get(url, headers=HEADERS, params=params, timeout=30)
        if response.status_code == 429:
            time.sleep(int(response.headers.get("Retry-After", "2")))
            continue
        response.raise_for_status()
        return response.json()
    raise RuntimeError(f"Notion API rate limit persisted: {url}")

def rich_text(items):
    return "".join(item.get("plain_text", "") for item in (items or []))

def inline_text(items):
    parts = []
    for item in items or []:
        text = item.get("plain_text", "")
        annotations = item.get("annotations", {})
        if annotations.get("code"):
            text = "`" + text + "`"
        if annotations.get("bold"):
            text = "**" + text + "**"
        if annotations.get("italic"):
            text = "*" + text + "*"
        if annotations.get("strikethrough"):
            text = "~~" + text + "~~"
        href = item.get("href")
        if href and text:
            text = f"[{text}]({href})"
        parts.append(text)
    return "".join(parts)

def get_blocks(block_id):
    results = []
    cursor = None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        data = request_json(f"{API_BASE}/blocks/{block_id}/children", params)
        results.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return results

def block_to_markdown(block, depth=0):
    kind = block.get("type", "")
    data = block.get(kind, {})
    text = inline_text(data.get("rich_text", []))
    prefix = "  " * min(depth, 8)

    if kind == "paragraph":
        return prefix + text if text else ""
    if kind.startswith("heading_"):
        level = int(kind[-1])
        return "#" * level + " " + text
    if kind == "bulleted_list_item":
        return prefix + "- " + text
    if kind == "numbered_list_item":
        return prefix + "1. " + text
    if kind == "to_do":
        return prefix + ("- [x] " if data.get("checked") else "- [ ] ") + text
    if kind == "quote":
        return "> " + text
    if kind == "callout":
        icon = data.get("icon", {})
        emoji = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
        return f"> {emoji} {text}".rstrip()
    if kind == "code":
        language = data.get("language", "")
        return f"```{language}\n{rich_text(data.get('rich_text', []))}\n```"
    if kind == "divider":
        return "---"
    if kind == "bookmark":
        url = data.get("url", "")
        return f"[{url}]({url})" if url else ""
    if kind == "embed":
        url = data.get("url", "")
        return f"[Embed]({url})" if url else ""
    if kind == "image":
        source = data.get("external", {}).get("url") or data.get("file", {}).get("url", "")
        caption = inline_text(data.get("caption", [])) or "Notion image"
        return f"![{caption}]({source})" if source else f"*[{caption}]*"
    if kind == "file":
        source = data.get("external", {}).get("url") or data.get("file", {}).get("url", "")
        name = inline_text(data.get("caption", [])) or "Attached file"
        return f"[{name}]({source})" if source else f"*{name}*"
    if kind == "child_page":
        return f"### {data.get('title', 'Untitled page')}"
    if kind == "table_of_contents":
        return ""
    if kind == "table":
        rows = get_blocks(block["id"])
        rendered = []
        for row in rows:
            cells = row.get("table_row", {}).get("cells", [])
            rendered.append("| " + " | ".join(inline_text(cell) for cell in cells) + " |")
        if rendered:
            count = len(rows[0].get("table_row", {}).get("cells", []))
            if count:
                rendered.insert(1, "| " + " | ".join(["---"] * count) + " |")
        return "\n".join(rendered)
    if kind == "child_database":
        return f"*Embedded database: {data.get('title', 'Untitled')}*"
    if kind == "equation":
        return "$$" + data.get("expression", "") + "$$"
    return ""

def render_block(block, depth=0):
    lines = []
    base = block_to_markdown(block, depth)
    if base:
        lines.append(base)
    if block.get("has_children") and block.get("type") not in ("table",):
        for child in get_blocks(block["id"]):
            child_text = render_block(child, depth + (1 if child.get("type") in ("bulleted_list_item", "numbered_list_item", "to_do") else 0))
            if child_text:
                lines.append(child_text)
    return "\n\n".join(lines)

def main():
    config = json.loads(Path("notion_pages.json").read_text(encoding="utf-8"))
    for page in config.get("pages", []):
        page_id = page["id"]
        meta = request_json(f"{API_BASE}/pages/{page_id}")
        title_parts = meta.get("properties", {}).get("title", {}).get("title", [])
        if not title_parts:
            for prop in meta.get("properties", {}).values():
                if prop.get("type") == "title":
                    title_parts = prop.get("title", [])
                    break
        title = rich_text(title_parts) or page.get("title", "Untitled")
        body = "\n\n".join(
            text for block in get_blocks(page_id)
            if (text := render_block(block))
        )
        output = Path(page["path"])
        output.parent.mkdir(parents=True, exist_ok=True)
        content = f"# {title}\n\n> Synced from Notion. Edit the source page in Notion; this file is generated.\n\n{body}\n"
        output.write_text(content, encoding="utf-8")
        print(f"Synced: {title} -> {output}")

if __name__ == "__main__":
    main()
