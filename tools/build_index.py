#!/usr/bin/env python3
"""Regenerate the writeup index table in README.md from post frontmatter.

No third-party dependencies — the frontmatter subset used here (scalars and
simple inline lists) is parsed directly, so this runs anywhere Python 3 does.

Usage:
    python3 tools/build_index.py           # rewrite README.md in place
    python3 tools/build_index.py --check    # exit 1 if README.md is out of date
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WRITEUPS = ROOT / "writeups"
README = ROOT / "README.md"

START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"

DIFFICULTY_ORDER = {"easy": 0, "medium": 1, "hard": 2, "insane": 3}


def parse_frontmatter(text: str) -> dict[str, object]:
    """Pull the leading --- fenced YAML block into a dict.

    Handles `key: value` and `key: [a, b, c]`. Quotes are stripped. Anything
    more exotic is left as a raw string, which is fine for an index table.
    """
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}

    data: dict[str, object] = {}
    for line in match.group(1).splitlines():
        line = line.split(" #")[0].rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        raw = raw.strip()

        if raw.startswith("[") and raw.endswith("]"):
            items = [i.strip().strip("\"'") for i in raw[1:-1].split(",")]
            data[key] = [i for i in items if i]
        else:
            data[key] = raw.strip("\"'")
    return data


def collect() -> list[dict[str, object]]:
    posts = []
    for path in sorted(WRITEUPS.glob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not meta:
            print(f"  skipping {path.name}: no frontmatter", file=sys.stderr)
            continue
        if str(meta.get("status", "")).lower() == "draft":
            continue
        meta["_path"] = path.relative_to(ROOT).as_posix()
        posts.append(meta)
    return posts


def render(posts: list[dict[str, object]]) -> str:
    if not posts:
        return "\n_No published writeups yet._\n"

    posts.sort(key=lambda p: str(p.get("date", "")), reverse=True)

    rows = [
        "| Date | Target | Platform | OS | Difficulty | Tags |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for p in posts:
        tags = p.get("tags") or []
        tag_str = ", ".join(f"`{t}`" for t in tags) if isinstance(tags, list) else str(tags)
        title = p.get("title") or p.get("target") or pathlib.Path(str(p["_path"])).stem
        rows.append(
            f"| {p.get('date', '')} "
            f"| [{title}]({p['_path']}) "
            f"| {p.get('platform', '')} "
            f"| {p.get('os', '')} "
            f"| {p.get('difficulty', '')} "
            f"| {tag_str} |"
        )

    count = len(posts)
    noun = "writeup" if count == 1 else "writeups"
    return "\n" + "\n".join(rows) + f"\n\n_{count} published {noun}._\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify without writing")
    args = parser.parse_args()

    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        print(f"error: README.md is missing the {START} / {END} markers", file=sys.stderr)
        return 2

    before, _, rest = readme.partition(START)
    _, _, after = rest.partition(END)
    updated = before + START + render(collect()) + END + after

    if updated == readme:
        print("index is up to date")
        return 0

    if args.check:
        print("index is out of date — run: python3 tools/build_index.py", file=sys.stderr)
        return 1

    README.write_text(updated, encoding="utf-8")
    print("index updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
