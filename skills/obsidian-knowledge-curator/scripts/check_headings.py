#!/usr/bin/env python3
"""Check the curator's default hierarchical heading numbers, without writes."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?)[ \t]*|[ \t]*)$")
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})[^\r\n]*$")
NUMBER = re.compile(r"^(\d+(?:\.\d+)*)(\.?)[ \t]+\S")


def strip_comments(line: str, active: str | None) -> tuple[str, str | None]:
    result: list[str] = []
    position = 0
    while position < len(line):
        if active:
            end_marker = "-->" if active == "html" else "%%"
            end = line.find(end_marker, position)
            if end < 0:
                return "".join(result), active
            position = end + len(end_marker)
            active = None
            continue
        starts = [
            (idx, kind, marker)
            for marker, kind in (("<!--", "html"), ("%%", "obsidian"))
            if (idx := line.find(marker, position)) >= 0
        ]
        if not starts:
            result.append(line[position:])
            break
        idx, active, marker = min(starts)
        result.append(line[position:idx])
        position = idx + len(marker)
    return "".join(result), active


def inspect(text: str) -> list[str]:
    lines = text.splitlines()
    errors: list[str] = []
    start = 0
    if lines and lines[0].strip() == "---":
        end = next(
            (i for i in range(1, len(lines)) if lines[i].strip() in {"---", "..."}),
            None,
        )
        if end is None:
            return ["YAML frontmatter 未闭合，无法可靠检查标题"]
        start = end + 1

    counts = [0] * 7
    title_count = 0
    fence_marker: str | None = None
    fence_length = 0
    in_math = False
    comment: str | None = None
    for line_no, raw in enumerate(lines[start:], start + 1):
        if fence_marker is not None:
            close = re.compile(
                r"^ {0,3}" + re.escape(fence_marker) + "{" + str(fence_length) + r",}[ \t]*$"
            )
            if close.match(raw):
                fence_marker = None
            continue

        line, comment = strip_comments(raw, comment)
        if in_math:
            if line.count("$$") % 2:
                in_math = False
            continue
        fence = FENCE.match(line)
        if fence:
            fence_marker = fence.group(1)[0]
            fence_length = len(fence.group(1))
            continue
        if line.strip().startswith("$$"):
            if line.count("$$") % 2:
                in_math = True
            continue

        match = HEADING.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2) or ""
        if level == 1:
            title_count += 1
            if title_count > 1:
                errors.append(f"第 {line_no} 行：存在多个一级标题")
            continue
        if level > 3:
            errors.append(f"第 {line_no} 行：默认最多使用两层编号标题（1. 和 1.1）")
            continue
        if title_count == 0:
            errors.append(f"第 {line_no} 行：标题出现在一级标题之前")
        if level > 2 and counts[level - 1] == 0:
            errors.append(f"第 {line_no} 行：{level} 级标题缺少上一级标题")
        counts[level] += 1
        for lower in range(level + 1, 7):
            counts[lower] = 0
        expected = ".".join(str(counts[i]) for i in range(2, level + 1))
        number = NUMBER.match(title)
        suffix = "." if level == 2 else ""
        if number is None or number.group(1) != expected or number.group(2) != suffix:
            errors.append(f"第 {line_no} 行：{level} 级标题应以 {expected + suffix} 加空格开头")

    if title_count == 0:
        errors.append("缺少一级标题")
    if fence_marker is not None:
        errors.append("代码块未闭合，无法可靠检查后续标题")
    if in_math:
        errors.append("块公式可能未闭合，无法可靠检查后续标题")
    if comment is not None:
        errors.append("注释可能未闭合，无法可靠检查后续标题")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="只读检查默认标题：一级为标题，最多两层编号 1. 和 1.1。"
    )
    parser.add_argument("note", type=Path, help="需要检查的 Markdown 笔记")
    args = parser.parse_args()
    try:
        text = args.note.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"读取失败：{exc}", file=sys.stderr)
        return 2
    errors = inspect(text)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("标题层级与默认编号通过检查；请另外检查链接锚点及实际渲染。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
