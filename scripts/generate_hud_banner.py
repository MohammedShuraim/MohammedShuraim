"""HUD banner matching the 22MIS1157 profile chrome, with MohammedShuraim identity.

VISUAL.MAP morphs between a neural-node field and a </> code glyph.
Does not use anyone else's portrait or logo.
"""
from __future__ import annotations

import math
import os
import random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUM = 420
W, H = 1180, 610
MAP_W, MAP_H = 290, 350


def neural_field(n: int, w: int = MAP_W, h: int = MAP_H, seed: int = 7):
    rnd = random.Random(seed)
    pts = []
    rings = 6
    remaining = n
    for i in range(rings):
        count = max(8, remaining // (rings - i))
        remaining -= count
        r = 28 + i * 22
        for k in range(count):
            a = (2 * math.pi * k / count) + i * 0.35
            x = w / 2 + r * math.cos(a) + rnd.uniform(-3, 3)
            y = h / 2 + r * math.sin(a) * 1.15 + rnd.uniform(-3, 3)
            pts.append((x, y))
    rnd.shuffle(pts)
    return pts[:n]


def code_glyph(n: int, w: int = MAP_W, h: int = MAP_H):
    cx, cy = w / 2, h / 2
    pts = []
    part = n // 3
    for t in [i / max(part - 1, 1) for i in range(part)]:
        pts.append((cx - 50 - (1 - abs(t - 0.5) * 2) * 55, cy - 65 + t * 130))
    for t in [i / max(part - 1, 1) for i in range(part)]:
        pts.append((cx + 22 - t * 44, cy - 75 + t * 150))
    for t in [i / max(n - len(pts) - 1, 1) for i in range(n - len(pts))]:
        pts.append((cx + 50 + (1 - abs(t - 0.5) * 2) * 55, cy - 65 + t * 130))
    return pts[:n]


def write_banner(path: str, palette: dict):
    bg = palette["bg"]
    chrome = palette["chrome"]
    dots = palette["dots"]
    text = palette["text"]
    pill = palette["pill"]

    neural = neural_field(NUM)
    code = code_glyph(NUM)

    info = [
        ("Subject", "Mohammed Rashique Shuraim"),
        ("Role", "Applied AI Engineer"),
        ("Origin", "Chennai, India"),
        ("Education", "VIT Chennai · 22MIS1040"),
        ("Status", "Building + Learning + Shipping"),
        ("ToolChain", "Cursor, Git, Docker, AWS"),
        ("Core.Lang", "Python, TypeScript, JavaScript, SQL"),
        ("Core.Frontend", "Next.js, React, Vite"),
        ("Core.Backend", "FastAPI, Flask, AWS Lambda"),
        ("Core.AI", "RAG, Whisper, Groq, Gemini, Polly"),
        ("Core.Data", "PostgreSQL, pgvector, DynamoDB, S3"),
        ("Core.Infra", "Amplify, EC2, RDS, ECR, Terraform"),
        ("- Contact", ""),
        ("Grid.Mail", "mohammed.rashique2022@vitstudent.ac.in"),
        ("Grid.GitHub", "@MohammedShuraim"),
        ("Grid.LexCloud", "github.com/MohammedShuraim/LexCloud"),
        ("Grid.Sentellent", "github.com/MohammedShuraim/sentinel-ai"),
        ("Grid.Sarah", "github.com/MohammedShuraim/sarah-voice-assistant"),
    ]

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    out.append(f'<rect width="100%" height="100%" fill="{bg}"/>')
    out.append("<style>")
    out.append(".pulse { animation: p 2s infinite; }")
    out.append("@keyframes p { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }")
    out.append(f".corner-glow {{ stroke: {chrome}; stroke-width: 2; fill: none; }}")
    out.append("</style>")

    out.append(f'<rect x="10" y="10" width="1160" height="590" rx="12" fill="none" stroke="{chrome}" stroke-width="1.5" opacity="0.6"/>')
    out.append(f'<line x1="10" y1="42" x2="1170" y2="42" stroke="{chrome}" stroke-width="1" opacity="0.3"/>')
    out.append('<circle cx="32" cy="26" r="5" fill="#FF5F56"/>')
    out.append('<circle cx="48" cy="26" r="5" fill="#FFBD2E"/>')
    out.append('<circle cx="64" cy="26" r="5" fill="#27C93F"/>')
    out.append(f'<text x="590" y="30" fill="{text}" font-size="13" text-anchor="middle" opacity="0.8" font-family="Segoe UI, Helvetica, Arial, sans-serif">mohammed.rashique2022@vitstudent.ac.in — % ./profile.sh --live</text>')

    out.append(f'<rect x="45" y="65" width="330" height="420" fill="none" stroke="{chrome}" stroke-width="1" opacity="0.25"/>')
    out.append(f'<text x="58" y="85" fill="{text}" font-size="11" opacity="0.6" font-family="Segoe UI, Helvetica, Arial, sans-serif">VISUAL.MAP</text>')
    out.append('<path class="corner-glow" d="M38,85 V60 H63"/>')
    out.append('<path class="corner-glow" d="M382,85 V60 H357"/>')
    out.append('<path class="corner-glow" d="M38,465 V490 H63"/>')
    out.append('<path class="corner-glow" d="M382,465 V490 H357"/>')
    out.append(f'<text x="45" y="525" fill="{chrome}" font-size="12" opacity="0.8" font-family="Consolas, ui-monospace, monospace">► More about me &amp; projects below in README ↓</text>')

    ox, oy = 65, 100
    out.append(f'<g transform="translate({ox},{oy})">')
    keytimes = "0;0.42;0.50;0.92;1"
    for i in range(NUM):
        x1, y1 = neural[i]
        x2, y2 = code[i]
        cx = f"{x1:.1f};{x1:.1f};{x2:.1f};{x2:.1f};{x1:.1f}"
        cy = f"{y1:.1f};{y1:.1f};{y2:.1f};{y2:.1f};{y1:.1f}"
        out.append(f'<circle r="1.8" fill="{dots}">')
        out.append(f'  <animate attributeName="cx" values="{cx}" keyTimes="{keytimes}" dur="10s" repeatCount="indefinite"/>')
        out.append(f'  <animate attributeName="cy" values="{cy}" keyTimes="{keytimes}" dur="10s" repeatCount="indefinite"/>')
        out.append("</circle>")
    out.append("</g>")

    out.append('<g transform="translate(420, 85)" font-family="Consolas, ui-monospace, monospace">')
    out.append(f'<text x="0" y="0" fill="{chrome}" font-size="13" font-weight="bold">SYSTEM.INFO</text>')
    out.append('<g transform="translate(640, -10)">')
    out.append('<circle cx="5" cy="5" r="4" fill="#EF4444" class="pulse"/>')
    out.append('<text x="15" y="9" fill="#EF4444" font-size="12" font-weight="bold">LIVE</text>')
    out.append("</g>")
    out.append(f'<rect x="0" y="18" width="360" height="26" rx="4" fill="{pill}"/>')
    out.append('<text x="180" y="36" fill="white" font-size="12" text-anchor="middle" font-weight="bold">mohammed.rashique2022@vitstudent.ac.in</text>')

    y = 70
    for label, value in info:
        if label == "- Contact":
            out.append(f'<text x="0" y="{y}" fill="{text}" font-size="13" opacity="0.6">- Contact</text>')
            y += 24
            continue
        dots_s = "." * max(2, 58 - len(label) - min(len(value), 34))
        shown = value if len(value) <= 42 else value[:39] + "..."
        out.append(f'<text x="0" y="{y}" fill="{chrome}" font-size="13">{label}</text>')
        out.append(f'<text x="{len(label) * 8 + 6}" y="{y}" fill="{chrome}" font-size="13" opacity="0.3">{dots_s}</text>')
        out.append(f'<text x="720" y="{y}" fill="{text}" font-size="13" text-anchor="end">{shown}</text>')
        y += 22
    out.append("</g>")
    out.append("</svg>")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote {path}")


def main():
    write_banner(
        os.path.join(ROOT, "dark.svg"),
        {"dots": "#A78BFA", "chrome": "#22D3EE", "pill": "#7C3AED", "bg": "#0A101F", "text": "#94A3B8"},
    )
    write_banner(
        os.path.join(ROOT, "light.svg"),
        {"dots": "#7C3AED", "chrome": "#0891B2", "pill": "#7C3AED", "bg": "#FFFFFF", "text": "#475569"},
    )


if __name__ == "__main__":
    main()
