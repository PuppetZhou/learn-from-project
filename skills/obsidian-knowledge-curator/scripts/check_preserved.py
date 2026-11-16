#!/usr/bin/env python3
"""Heuristically compare protected Markdown fragments in two note versions.

The comparison is read-only and never prints fragment contents. It is not a
Markdown parser, scientific correctness check, or Obsidian link resolver.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys


KINDS = (
    ("frontmatter", "YAML 属性"),
    ("fenced_code", "围栏代码块"),
    ("inline_code", "行内代码"),
    ("block_math", "块公式"),
    ("inline_math", "行内公式"),
    ("wikilink", "双链与嵌入"),
)

FENCE_OPEN = re.compile(r"^ {0,3}(\x60{3,}|~{3,})[^\r\n]*$")
INLINE_CODE = re.compile(
    r"(?<!\x60)(\x60+)(?!\x60)(.+?)(?<!\x60)\1(?!\x60)", re.DOTALL
)
BLOCK_MATH = re.compile(r"(?<!\\)\$\$.*?(?<!\\)\$\$", re.DOTALL)
INLINE_MATH = re.compile(
    r"(?<![\\$])\$(?!\$)(?:\\.|[^$\n\\])+(?<!\\)\$(?!\$)"
)
WIKILINK = re.compile(r"!?\[\[[^\]\n]+\]\]")


def hide(value: str) -> str:
    return "".join("\n" if char == "\n" else " " for char in value)


def collect(text: str) -> tuple[dict[str, Counter], list[str]]:
    parts = {key: Counter() for key, _ in KINDS}
    warnings: list[str] = []
    lines = text.splitlines(keepends=True)
    visible: list[str] = []
    i = 0

    if lines and lines[0].strip() == "---":
        end = next(
            (j for j in range(1, len(lines)) if lines[j].strip() in {"---", "..."}),
            None,
        )
        if end is None:
            warnings.append("YAML frontmatter 可能没有闭合")
        else:
            frontmatter = "".join(lines[: end + 1])
            parts["frontmatter"][frontmatter] += 1
            visible.append(hide(frontmatter))
            i = end + 1

    while i < len(lines):
        match = FENCE_OPEN.match(lines[i].rstrip("\r\n"))
        if not match:
            visible.append(lines[i])
            i += 1
            continue

        marker = match.group(1)
        close = re.compile(r"^ {0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}[ \t]*$")
        end = i + 1
        while end < len(lines) and not close.match(lines[end].rstrip("\r\n")):
            end += 1
        if end == len(lines):
            warnings.append("围栏代码块可能没有闭合")
        else:
            end += 1
        block = "".join(lines[i:end])
        parts["fenced_code"][block] += 1
        visible.append(hide(block))
        i = end

    remainder = "".join(visible)
    for key, pattern in (
        ("inline_code", INLINE_CODE),
        ("block_math", BLOCK_MATH),
        ("inline_math", INLINE_MATH),
        ("wikilink", WIKILINK),
    ):
        def capture(match: re.Match[str]) -> str:
            fragment = match.group(0)
            parts[key][fragment] += 1
            return hide(fragment)

        remainder = pattern.sub(capture, remainder)
    return parts, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="只读比较原稿和整理稿中的常见公式、代码、双链及 YAML；不输出正文。"
    )
    parser.add_argument("before", type=Path, help="修改前的原稿")
    parser.add_argument("after", type=Path, help="修改后的候选稿")
    args = parser.parse_args()
    try:
        before = args.before.read_text(encoding="utf-8")
        after = args.after.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"读取失败：{exc}", file=sys.stderr)
        return 2

    old_parts, old_warnings = collect(before)
    new_parts, new_warnings = collect(after)
    missing_total = 0
    for key, label in KINDS:
        missing = sum((old_parts[key] - new_parts[key]).values())
        added = sum((new_parts[key] - old_parts[key]).values())
        missing_total += missing
        print(f"{label}：原稿片段缺失或改变 {missing}，新增 {added}")
    for label, warnings in (("原稿", old_warnings), ("整理稿", new_warnings)):
        for warning in warnings:
            print(f"提示：{label}{warning}，需要人工检查。")
    print("本工具是启发式比较；不验证普通 Markdown 链接、锚点解析、渲染和科学语义。")
    if missing_total:
        print("请核对差异；如为用户要求的改动，应记录为预期变化。")
        return 1
    print("未发现已识别原片段缺失；仍需人工复核。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
