"""Editorial particle portrait for MohammedShuraim — applied AI theme.

Ink / brass / signal-cyan. Converts the GitHub portrait into dithered
dots, then composes an SVG identity plate (not a toy terminal window).
"""
from __future__ import annotations

import os
import random

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO = os.path.join(ROOT, "data", "github-avatar.png")
PW, PH = 248, 300


def dither(path: str, invert: bool) -> list[list[int]]:
    img = Image.open(path).convert("RGB")
    w, h = img.size
    side = min(w, h)
    img = img.crop(((w - side) // 2, 0, (w - side) // 2 + side, side))
    img = img.resize((PW, PH), Image.Resampling.LANCZOS)
    img = ImageOps.grayscale(img)
    img = ImageOps.autocontrast(img, cutoff=2)
    img = ImageEnhance.Contrast(img).enhance(1.55)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=120))
    if invert:
        img = ImageOps.invert(img)
    pixels = img.load()
    grid = [[0] * PW for _ in range(PH)]
    err = [[0.0] * PW for _ in range(PH)]
    for y in range(PH):
        for x in range(PW):
            old = pixels[x, y] + err[y][x]
            new = 255 if old > 128 else 0
            grid[y][x] = 1 if new == 0 else 0
            quant = old - new
            if x + 1 < PW:
                err[y][x + 1] += quant * 7 / 16
            if y + 1 < PH and x > 0:
                err[y + 1][x - 1] += quant * 3 / 16
            if y + 1 < PH:
                err[y + 1][x] += quant * 5 / 16
            if y + 1 < PH and x + 1 < PW:
                err[y + 1][x + 1] += quant * 1 / 16
    return grid


def write_svg(grid: list[list[int]], path: str, dark: bool) -> None:
    bg = "#070A12" if dark else "#F4F0E8"
    ink = "#E8ECF4" if dark else "#14110C"
    muted = "#8B93A7" if dark else "#5C564C"
    brass = "#D4AF6A"
    cyan = "#38D8F0" if dark else "#0E7490"
    dot = cyan if dark else "#1F2933"
    W, H = 1180, 420

    rnd = random.Random(11)
    bands: dict[int, list[str]] = {i: [] for i in range(72)}
    for y in range(PH):
        run = -1
        for x in range(PW + 1):
            on = x < PW and grid[y][x] == 1
            if on and run == -1:
                run = x
            if (not on) and run != -1:
                bands[rnd.randint(0, 71)].append(f"M{run} {y}h{x - run}")
                run = -1

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect width="100%" height="100%" fill="{bg}"/>',
        f'<rect x="36" y="28" width="1108" height="364" fill="none" stroke="{brass}" stroke-opacity="0.35"/>',
        f'<path d="M36 48h16M36 28v20M1144 48h-16M1144 28v20M36 372h16M36 392v-20M1144 372h-16M1144 392v-20" fill="none" stroke="{cyan}" stroke-width="1.6"/>',
        f'<text x="72" y="64" fill="{muted}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="12" letter-spacing="4">APPLIED AI ENGINEER</text>',
        f'<g transform="translate(72,86)">',
        f'<rect x="-8" y="-8" width="{PW + 16}" height="{PH + 16}" fill="none" stroke="{brass}" stroke-opacity="0.45"/>',
    ]
    for idx, segs in bands.items():
        if not segs:
            continue
        delay = (idx % 12) * 0.12
        lines.append(
            f'<path fill="none" stroke="{dot}" stroke-width="1.35" d="{" ".join(segs)}">'
            f'<animate attributeName="opacity" values="0.35;1;0.35" dur="3.6s" begin="{delay:.2f}s" repeatCount="indefinite"/>'
            f"</path>"
        )
    lines += [
        "</g>",
        f'<text x="380" y="150" fill="{ink}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="34" font-weight="700">Mohammed Rashique Shuraim</text>',
        f'<rect x="380" y="168" width="64" height="2" fill="{brass}"/>',
        f'<text x="380" y="206" fill="{muted}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="16">I ship AI as product systems — retrieval, voice, and agents that stay faithful to source data.</text>',
        f'<text x="380" y="242" fill="{cyan}" font-family="Consolas, ui-monospace, monospace" font-size="13">RAG grounded in documents   ·   Whisper in / Polly out   ·   AWS production</text>',
        f'<text x="380" y="278" fill="{muted}" font-family="Consolas, ui-monospace, monospace" font-size="13">LexCloud · Sentellent AI · Sarah</text>',
        f'<text x="380" y="330" fill="{muted}" font-family="Consolas, ui-monospace, monospace" font-size="12">VIT Chennai  ·  22MIS1040  ·  Chennai</text>',
        "</svg>",
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("wrote", path)


def main() -> None:
    write_svg(dither(PHOTO, invert=True), os.path.join(ROOT, "dark.svg"), True)
    write_svg(dither(PHOTO, invert=False), os.path.join(ROOT, "light.svg"), False)


if __name__ == "__main__":
    main()
