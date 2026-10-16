#!/usr/bin/env python3
"""Generate the profile README SVG assets (light + dark) with no dependencies.

Run from anywhere:  python scripts/build_assets.py
Writes assets/*.svg (light) and assets/dark/*.svg (dark) next to this script's repo root.
Edit the CONTENT section to change any text.
"""
from __future__ import annotations

from html import escape
from textwrap import wrap as wrap_text
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEMES: dict[str, str] = {"light": "#000000", "dark": "#FFFFFF"}


def e(s: str) -> str:
    return escape(s, quote=False)


MONO = (
    '.mono { font-family: ui-monospace, "SFMono-Regular", "SF Mono", Menlo, '
    'Consolas, "Liberation Mono", monospace; }'
)
REDUCE = "@media (prefers-reduced-motion: reduce) { %s }"


def wrap(w: int, h: int, label: str, css: str, body: str, ink: str) -> str:
    root = (
        f":root {{ --bone:{ink}; --muted:{ink}; --dim:{ink}; --rule:{ink}; "
        f"--accent:{ink}; --ghost:{ink}; --ink:{ink}; }}"
    )
    return (
        f'<svg viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="{escape(label)}">\n  <style>\n    {root}\n    {MONO}\n'
        f"    {css}\n  </style>\n{body}\n</svg>\n"
    )


def t(x: float, y: float, s: str, size: float, fill: str = "bone", cls: str = "",
      ls: float | None = None, anchor: str | None = None) -> str:
    a = f' letter-spacing="{ls}"' if ls is not None else ""
    an = f' text-anchor="{anchor}"' if anchor else ""
    return (f'<text class="mono {cls}".strip() x="{x}" y="{y}" font-size="{size}" '
            f'fill="var(--{fill})"{a}{an}>{e(s)}</text>').replace('.strip()', '')


# ───────────────────────────── CONTENT ─────────────────────────────
NAME = "Aman Yadav"
GH_URL = "https://github.com/Mr-CodeGuru"
LI_URL = "https://linkedin.com/in/aman-yadav-codeguru"

PROJECTS: list[tuple[str, str, str]] = [
    ("ORCHESTRA",
     "A cloud-native, node-based platform for designing, running and deploying AI pipelines through a visual "
     "interface. Models, tools, data sources and processing steps connect as modular, reusable nodes, so complex "
     "workflows come together without extensive boilerplate. Built for both experimentation and production, it "
     "supports cloud execution and scalable orchestration, and any workflow can be exported as an API endpoint to "
     "plug into applications, automate tasks or run as a production service. The goal is one environment that "
     "carries an idea from rapid prototype to large-scale cloud execution, with flexibility and developer "
     "experience first.",
     "NODE-BASED WORKFLOWS · AI PIPELINES · CLOUD EXECUTION · API EXPORT"),
    ("LOOMIS",
     "A fully local, terminal-based code assistant in the spirit of Claude Code and Gemini CLI, but with no cloud "
     "dependency. A small language model served through llama.cpp answers questions over a codebase using "
     "retrieval-augmented generation: code is embedded with a code-specialised model into LanceDB, and hybrid "
     "vector and full-text search retrieves the relevant chunks from a corpus of roughly 70,000. A Rust CLI "
     "streams responses into the terminal, a Python sidecar handles embeddings, and a TUI front end is in "
     "development. Everything runs on-device and stays usable on modest hardware.",
     "RUST · PYTHON · LANCEDB · LLAMA.CPP · HYBRID RAG · LOCAL SLM"),
    ("CONDUIT",
     "A local-first MCP gateway that sits between AI agent clients such as Claude Desktop and Cursor and multiple "
     "backend MCP servers. It aggregates and namespaces their tools behind one endpoint, and applies masking, "
     "blocking and parameter-mutation rules, with Lua hooks for custom behavior, to everything passing through. "
     "Built as a Rust workspace with stdio and SSE transports and SQLite storage, it ships a SolidJS dashboard "
     "embedded in the binary, giving live session inspection and a REST observability API from a single local "
     "process.",
     "RUST · SOLIDJS · TYPESCRIPT · SQLITE · AXUM · MCP"),
    ("MARKITDOWN-RUST-PY",
     "A Rust-core reimplementation of MarkItDown, exposed to Python through PyO3. It converts documents such as "
     "CSV and HTML into clean Markdown with a small memory footprint and fast start-up, aimed at document "
     "ingestion pipelines that feed LLM and RAG workflows. It is built in phases: the CSV and HTML converters are "
     "in place and more formats are on the way, all behind a plain Python interface.",
     "RUST · PYO3 · PYTHON · MARKDOWN"),
    ("POSEFIT WEB",
     "A browser-based AI fitness coach that estimates body pose from the camera feed in real time. A Rust core "
     "compiled to WebAssembly works alongside MediaPipe to process pose landmarks, and a React interface turns "
     "them into live feedback while you exercise. It runs as a web app deployed on Vercel, so there is nothing "
     "to install and the analysis happens in the browser.",
     "RUST · WASM · MEDIAPIPE · REACT · VERCEL"),
    ("NOVELREAD",
     "A lightweight, mobile-friendly reading platform for discovering, organizing and reading digital books and "
     "documents through a clean interface tuned for mobile performance. Built with cloud integration in mind, it "
     "lets readers open their library on any device, synchronize progress and keep content organized without "
     "relying on local storage. The streamlined architecture favors fast loading and efficient resource use, so "
     "reading stays smooth even on devices with limited resources: simple, portable and accessible, with the "
     "reach of the cloud.",
     "MOBILE · CLOUD SYNC · LIGHTWEIGHT · READING"),
]

STACK: list[tuple[str, str]] = [
    ("LANGUAGES", "Rust · Python · TypeScript · HTML · JavaScript · Shell · WebAssembly"),
    ("AI / ML", "Small language models · GGUF · llama.cpp · hybrid RAG · MediaPipe"),
    ("SYSTEMS", "Tokio · Axum · PyO3 · WebAssembly · JSON-RPC · MCP"),
    ("WEB", "React · SolidJS · Next.js · Tailwind"),
    ("DATA", "SQLite · LanceDB · PostgreSQL"),
    ("TOOLING", "Git · Docker · uv · Vercel"),
]

SECTIONS = [("01", "WHOAMI", "whoami"), ("02", "SYSTEM MAP", "system-map"),
            ("03", "PROJECTS", "projects"), ("04", "TELEMETRY", "telemetry"),
            ("05", "THE ROUTE", "the-route"), ("06", "STACK", "stack")]
# ───────────────────────────────────────────────────────────────────


def header(ink: str) -> str:
    css = """
    .draw { stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: draw 1.4s cubic-bezier(.6,0,.2,1) forwards; }
    @keyframes draw { to { stroke-dashoffset: 0; } }
    .rise { opacity: 0; animation: rise .9s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from { opacity:0;transform:translateY(12px); } to { opacity:1;transform:translateY(0); } }
    .fade { opacity: 0; animation: fade .7s ease forwards; }
    @keyframes fade { to { opacity: 1; } }
    .a1{animation-delay:.2s} .a2{animation-delay:.5s} .a3{animation-delay:.9s} .a4{animation-delay:1.2s} .a5{animation-delay:1.4s} .a6{animation-delay:1.7s}
    """ + REDUCE % ".draw,.rise,.fade { animation: none; } .draw{stroke-dashoffset:0} .rise,.fade{opacity:1}"
    chain = ["RUST & PYTHON", "LOCAL-FIRST AI", "OFFLINE SYSTEMS"]
    x, parts = 48.0, []
    for i, s in enumerate(chain):
        parts.append(t(x, 374, s, 11.5, "muted", ls=3))
        x += len(s) * 9.9 + 30
        if i < len(chain) - 1:
            parts.append(t(x - 14, 374, "·", 11.5, "accent"))
            x += 16
    body = f"""
  <line class="draw a1" x1="48" y1="58" x2="952" y2="58" stroke="var(--rule)" stroke-width="1"/>
  <g class="fade a1">
    {t(48, 44, "PORTFOLIO — INDEX Nº 001", 11, "muted", ls=3.5)}
    {t(952, 44, "GUJARAT, IN — 23.0° N", 11, "muted", ls=3.5, anchor="end")}
  </g>
  <g class="rise a2">{t(46, 176, NAME, 72, "bone", ls=-2)}</g>
  <g class="fade a3">{t(48, 214, "AI/ML Engineer — Gujarat, India.", 19, "muted")}</g>
  <g class="fade a4">
    {t(48, 274, "focus  ▸", 12.5, "dim", ls=1)}
    {t(128, 274, "local-first AI · Rust & Python systems · terminal interfaces · offline agents", 12.5, "accent", ls=1)}
  </g>
  <g class="fade a5">{t(48, 300, "builds AI that runs on the hardware people already own", 12.5, "dim", ls=1)}</g>
  <line class="draw a5" x1="48" y1="342" x2="952" y2="342" stroke="var(--rule)" stroke-width="1"/>
  <g class="fade a6">
    {''.join(parts)}
    {t(952, 374, "SYSTEMS · AI · TOOLING", 11.5, "muted", ls=3, anchor="end")}
  </g>"""
    return wrap(1000, 400, f"{NAME} — AI/ML Engineer", css, body, ink)


def section(num: str, name: str, slug: str, ink: str) -> str:
    css = """
    .draw { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 900; stroke-dashoffset: 900; animation: d 1.3s cubic-bezier(.6,0,.2,1) .2s forwards; }
    @keyframes d { to { stroke-dashoffset: 0; } }
    .f { opacity: 0; animation: f .8s ease .1s forwards; }
    @keyframes f { to { opacity: 1; } }
    """ + REDUCE % ".draw,.f { animation: none; } .draw { stroke-dashoffset: 0; } .f { opacity: 1; }"
    right = f"~/{num}-{slug}"
    x1 = 128 + len(name) * 14.4 + 30
    x2 = 952 - len(right) * 8.6 - 24
    body = f"""  <g class="f">
    {t(48, 68, num, 52, "ghost")}
    {t(128, 58, name, 14, "accent", ls=6)}
    {t(952, 58, right, 11, "muted", ls=2, anchor="end")}
  </g>
  <line class="draw" x1="{x1:.0f}" y1="53" x2="{x2:.0f}" y2="53"/>"""
    return wrap(1000, 92, f"Section {num} — {name}", css, body, ink)


def whoami(ink: str) -> str:
    css = """
    .rise { opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from { opacity:0;transform:translateY(8px); } to { opacity:1;transform:translateY(0); } }
    .a1{animation-delay:.1s} .a2{animation-delay:.2s} .a3{animation-delay:.35s} .a4{animation-delay:.5s} .a5{animation-delay:.65s} .a6{animation-delay:.8s}
    """ + REDUCE % ".rise { animation: none; opacity: 1; }"
    body = f"""
  {t(48, 32, "I build AI systems that run where people already are: offline, lightweight and private.", 16, cls="rise a1")}
  {t(48, 60, "Rust cores, Python orchestration, small language models, and thin interfaces on top.", 16, cls="rise a2")}
  {t(48, 88, "drawn to software that runs offline on modest hardware. small binaries, low memory, no cloud.", 15, "muted", cls="rise a3")}
  <line class="rise a4" x1="48" y1="116" x2="952" y2="116" stroke="var(--rule)" stroke-width="1" opacity=".5"/>
  {t(48, 148, "FOCUS", 11, "muted", cls="rise a4", ls=2.5)}
  {t(154, 148, "Local-first AI · Rust & Python systems · Offline agents · Terminal UI", 15, cls="rise a4")}
  {t(48, 182, "BUILDING", 11, "muted", cls="rise a5", ls=2.5)}
  {t(154, 182, "Agents · workflow platforms · RAG tooling · browser & mobile apps", 15, "accent", cls="rise a5")}
  {t(48, 216, "PRINCIPLE", 11, "muted", cls="rise a6", ls=2.5)}
  {t(154, 216, "local-first by default, cloud as an optional upgrade", 15, cls="rise a6")}"""
    return wrap(1000, 236, "whoami — focus, building, principle", css, body, ink)


def edge(cx: float, cy: float, w: float, h: float, tx: float, ty: float) -> tuple[float, float]:
    """Point where the ray from a box centre toward (tx, ty) leaves the box."""
    dx, dy = tx - cx, ty - cy
    k = min((w / 2) / abs(dx) if dx else float("inf"), (h / 2) / abs(dy) if dy else float("inf"))
    return cx + dx * k, cy + dy * k


def ecosystem(ink: str) -> str:
    css = """
    .node { fill: none; stroke: var(--rule); stroke-width: 1; }
    .wire { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 500; stroke-dashoffset: 500; animation: draw 1.6s cubic-bezier(.6,0,.2,1) forwards; }
    @keyframes draw { to { stroke-dashoffset: 0; } }
    .w1{animation-delay:.2s}.w2{animation-delay:.32s}.w3{animation-delay:.44s}.w4{animation-delay:.56s}.w5{animation-delay:.68s}.w6{animation-delay:.8s}
    .flow { stroke: var(--muted); stroke-width: 1; opacity: .2; stroke-dasharray: 3 9; animation: march 1.4s linear infinite; }
    @keyframes march { to { stroke-dashoffset: -12; } }
    .pop { opacity: 0; animation: pop .7s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes pop { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
    .p0{animation-delay:.1s}.p1{animation-delay:.9s}.p2{animation-delay:1.0s}.p3{animation-delay:1.1s}.p4{animation-delay:1.2s}.p5{animation-delay:1.3s}.p6{animation-delay:1.4s}.p10{animation-delay:1.9s}
    .core { animation: breathe 3.2s ease-in-out infinite; }
    @keyframes breathe { 0%,100%{opacity:1} 50%{opacity:.55} }
    """ + REDUCE % ".wire,.flow,.pop,.core { animation: none; } .wire{stroke-dashoffset:0} .pop{opacity:1} .flow{opacity:.1}"
    W, H = 210, 54
    # (name, sub, x, y, cluster label, label_below)
    nodes = [
        ("loomis", "Rust · LanceDB · llama.cpp", 50, 95, "LOCAL AI", False),
        ("conduit", "Rust · SolidJS · MCP", 740, 95, "AGENT TOOLING", False),
        ("markitdown-rust-py", "Rust core · PyO3", 50, 351, "RUST ↔ PYTHON", False),
        ("posefit web", "Rust→WASM · MediaPipe", 740, 351, "BROWSER AI", False),
        ("orchestra", "AI pipelines · cloud", 395, 78, "CLOUD WORKFLOWS", False),
        ("novelread", "Mobile · cloud sync", 395, 395, "MOBILE READING", True),
    ]
    cx, cy, cw, ch = 405, 222, 190, 56
    lines_w, lines_f = [], []
    for i, n in enumerate(nodes):
        ncx, ncy = n[2] + W / 2, n[3] + H / 2
        ax, ay = edge(500, 250, cw, ch, ncx, ncy)
        bx, by = edge(ncx, ncy, W, H, 500, 250)
        d = f'x1="{ax:.0f}" y1="{ay:.0f}" x2="{bx:.0f}" y2="{by:.0f}"'
        lines_w.append(f'<line class="wire w{i+1}" {d}/>')
        lines_f.append(f'<line class="flow" {d}/>')
    pops = []
    for i, (nm, sub, x, y, lab, below) in enumerate(nodes):
        mx = x + W / 2
        ly = y + H + 22 if below else y - 14
        pops.append(
            f'<g class="pop p{i+1}"><rect class="node" x="{x}" y="{y}" width="{W}" height="{H}" rx="2"/>'
            f'{t(mx, y+23, nm, 12, ls=1, anchor="middle")}{t(mx, y+42, sub, 9, "muted", ls=1, anchor="middle")}</g>'
            f'{t(mx, ly, lab, 10, "accent", cls="pop p10", ls=3, anchor="middle")}'
        )
    body = f"""
  <line x1="48" y1="40" x2="952" y2="40" stroke="var(--rule)"/>
  {t(48, 28, "SYSTEM MAP — RUST CORE, THIN SHELLS", 11, "muted", ls=3.5)}
  {t(952, 28, "FIG. 01", 11, "muted", ls=3.5, anchor="end")}
  <g>{''.join(lines_w)}</g>
  <g>{''.join(lines_f)}</g>
  <g class="pop p0 core">
    <rect class="node" x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="2"/>
    {t(500, 246, "AMAN.SYS", 13, ls=2, anchor="middle")}
    {t(500, 264, "rust core · python glue · thin ui", 8.5, "muted", ls=0.5, anchor="middle")}
  </g>
  {''.join(pops)}"""
    return wrap(1000, 500, "System map: local-first AI projects around one build pipeline", css, body, ink)


def projects(ink: str) -> str:
    css = """
    .row { opacity:0; animation:reveal .55s cubic-bezier(.2,.7,.2,1) forwards; }
    .rule { stroke:var(--ink); stroke-width:1; }
    .title { fill:var(--ink); font-size:17px; font-weight:700; letter-spacing:.8px; }
    .copy { fill:var(--ink); font-size:12px; }
    .meta { fill:var(--ink); font-size:11px; letter-spacing:.4px; }
    @keyframes reveal { from { opacity:0; } to { opacity:1; } }
    .r1{animation-delay:.05s}.r2{animation-delay:.10s}.r3{animation-delay:.15s}.r4{animation-delay:.20s}.r5{animation-delay:.25s}.r6{animation-delay:.30s}
    """ + REDUCE % ".row { animation:none; opacity:1; }"
    rows, y = [], 20
    for i, (title, para, tags) in enumerate(PROJECTS):
        lines = wrap_text(para, 130)
        copy = "".join(f'<text class="copy" x="48" y="{49 + 19*j}">{e(ln)}</text>' for j, ln in enumerate(lines))
        meta_y = 49 + 19 * (len(lines) - 1) + 26
        rule_y = meta_y + 18
        rows.append(
            f'<g class="row r{i+1}" transform="translate(0 {y})">'
            f'<text class="title" x="48" y="24">{i+1:02d} / {e(title)}</text>{copy}'
            f'<text class="meta" x="48" y="{meta_y}">{e(tags)}</text>'
            f'<line class="rule" x1="48" y1="{rule_y}" x2="952" y2="{rule_y}"/></g>'
        )
        y += rule_y + 26
    body = f'  <g class="mono">{"".join(rows)}</g>'
    return wrap(1000, y, f"{len(PROJECTS)} projects by " + NAME, css, body, ink)


def telemetry(ink: str) -> str:
    css = """
    .bar { transform: scaleX(0); animation: grow 1.2s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes grow { to { transform: scaleX(1); } }
    .g1{transform-origin:48px 0;animation-delay:.25s}.g2{transform-origin:48px 0;animation-delay:.38s}.g3{transform-origin:48px 0;animation-delay:.51s}
    .g4{transform-origin:48px 0;animation-delay:.64s}.g5{transform-origin:48px 0;animation-delay:.77s}.g6{transform-origin:48px 0;animation-delay:.90s}.g7{transform-origin:48px 0;animation-delay:1.03s}
    .spark { stroke-dasharray: 700; stroke-dashoffset: 700; animation: draw 2.2s cubic-bezier(.6,0,.2,1) .5s forwards; }
    @keyframes draw { to { stroke-dashoffset: 0; } }
    .dot { opacity: 0; animation: fade .4s ease forwards; }
    .d1{animation-delay:1.0s}.d2{animation-delay:1.3s}.d3{animation-delay:1.6s}.d4{animation-delay:1.9s}.d5{animation-delay:2.2s}.d6{animation-delay:2.5s}
    @keyframes fade { to { opacity: 1; } }
    .rise { opacity: 0; animation: rise .8s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
    .n1{animation-delay:.5s}.n2{animation-delay:.7s}.n3{animation-delay:.9s}.n4{animation-delay:1.1s}
    .ping { animation: ping 2.2s ease-out infinite; transform-origin: 622px 105px; }
    @keyframes ping { 0%{transform:scale(.4);opacity:.9} 80%,100%{transform:scale(2.8);opacity:0} }
    """ + REDUCE % (
        ".bar,.spark,.dot,.rise,.ping { animation: none; } "
        ".bar{transform:scaleX(1)} .spark{stroke-dashoffset:0} .dot,.rise{opacity:1} .ping{opacity:0}"
    )
    body = f"""
  <line x1="48" y1="40" x2="952" y2="40" stroke="var(--rule)"/>
  {t(48, 28, "TELEMETRY — WHAT THE HANDS ARE DOING", 11, "muted", ls=3.5)}
  {t(952, 28, "FIG. 02", 11, "muted", ls=3.5, anchor="end")}
  <line x1="360" y1="64" x2="360" y2="296" stroke="var(--rule)" opacity=".4"/>
  <line x1="688" y1="64" x2="688" y2="296" stroke="var(--rule)" opacity=".4"/>

  <!-- language bars: rust 78, python 53, ts 36, html 28, js 17, shell 8, wasm 3 -->
  {t(48, 76, "LANGUAGE DISTRIBUTION · EST.", 10, "dim", ls=2.5)}
  <g class="mono" font-size="11">
    {t(48, 102, "rust", 11)}         <rect class="bar g1" x="48" y="110" width="230" height="5" fill="var(--accent)"/>{t(288, 117, "35%", 10, "muted")}
    {t(48, 131, "python", 11)}       <rect class="bar g2" x="48" y="139" width="158" height="5" fill="var(--bone)"/>{t(216, 146, "24%", 10, "muted")}
    {t(48, 160, "typescript", 11)}   <rect class="bar g3" x="48" y="168" width="105" height="5" fill="var(--bone)"/>{t(163, 175, "16%", 10, "muted")}
    {t(48, 189, "html", 11)}         <rect class="bar g4" x="48" y="197" width="85"  height="5" fill="var(--bone)"/>{t(143, 204, "13%", 10, "muted")}
    {t(48, 218, "javascript", 11)}   <rect class="bar g5" x="48" y="226" width="52"  height="5" fill="var(--bone)"/>{t(110, 233, "8%", 10, "muted")}
    {t(48, 247, "shell", 11)}        <rect class="bar g6" x="48" y="255" width="24"  height="5" fill="var(--bone)"/>{t(82, 262, "3%", 10, "muted")}
    {t(48, 276, "wasm", 11)}         <rect class="bar g7" x="48" y="284" width="12"  height="5" fill="var(--bone)"/>{t(70, 291, "1%", 10, "muted")}
  </g>

  <!-- shipping velocity -->
  {t(392, 76, "SHIPPING VELOCITY · 2023 → 2026", 10, "dim", ls=2.5)}
  <g>
    <line x1="392" y1="252" x2="656" y2="252" stroke="var(--rule)"/>
    <polyline class="spark" points="392,245 440,235 488,212 536,178 584,136 622,105 656,84" stroke="var(--accent)" stroke-width="1.5" fill="none"/>
    <circle class="dot d1" cx="440" cy="235" r="2.5" fill="var(--bone)"/>
    <circle class="dot d2" cx="488" cy="212" r="2.5" fill="var(--bone)"/>
    <circle class="dot d3" cx="536" cy="178" r="2.5" fill="var(--bone)"/>
    <circle class="dot d4" cx="584" cy="136" r="2.5" fill="var(--bone)"/>
    <circle class="ping" cx="622" cy="105" r="4" stroke="var(--accent)" fill="none"/>
    <circle class="dot d5" cx="622" cy="105" r="3" fill="var(--accent)"/>
    {t(392, 272, "'23", 9.5, "dim", ls=1.5)}
    {t(475, 272, "'24", 9.5, "dim", ls=1.5)}
    {t(560, 272, "'25", 9.5, "dim", ls=1.5)}
    {t(640, 272, "'26", 9.5, "dim", ls=1.5)}
    <g class="dot d6">
      {t(392, 300, "trend — accelerating", 10, "accent", ls=1.5)}
    </g>
  </g>

  <!-- profile counters -->
  <g>
    <g class="rise n1">
      {t(720, 118, "60", 44)}
      {t(790, 112, "REPOSITORIES", 10, "muted", ls=2.5)}
    </g>
    <g class="rise n2">
      {t(720, 178, "17", 44)}
      {t(790, 172, "PROJECTS DOCUMENTED", 10, "muted", ls=2.5)}
    </g>
    <g class="rise n3">
      {t(720, 238, "3", 44)}
      {t(790, 232, "OPEN SOURCE", 10, "muted", ls=2.5)}
    </g>
    <g class="rise n4">
      {t(718, 298, "∞", 44, "accent")}
      {t(790, 292, "INFINITE IDEAS MORE", 10, "muted", ls=2.5)}
    </g>
  </g>"""
    return wrap(1000, 330, "Telemetry: language distribution, shipping velocity 2023 to 2026, counters — 60 repositories, 17 projects, 3 open source", css, body, ink)


def github_stats(ink: str) -> str:
    css = """
    .panel,.rule,.bar { fill:none; stroke:var(--rule); stroke-width:1; }
    .fill { fill:var(--bone); }
    .grow { transform:scaleX(0); transform-origin:left; animation:grow .8s cubic-bezier(.2,.7,.2,1) forwards; }
    .g2{animation-delay:.1s}.g3{animation-delay:.2s}.g4{animation-delay:.3s}.g5{animation-delay:.4s}.g6{animation-delay:.5s}.g7{animation-delay:.6s}
    @keyframes grow { to { transform:scaleX(1); } }
    """ + REDUCE % ".grow { animation:none; transform:scaleX(1); }"
    body = f"""
  <rect class="panel" x="24" y="20" width="456" height="270" rx="2"/>
  <rect class="panel" x="520" y="20" width="456" height="270" rx="2"/>

  <g class="mono">
    {t(52, 58, "GITHUB STATS", 15, ls=2)}
    <line class="rule" x1="52" y1="72" x2="452" y2="72"/>
    {t(52, 110, "TOTAL REPOSITORIES", 11, ls=1)}{t(436, 110, "60", 13, anchor="end")}
    {t(52, 146, "PROJECTS DOCUMENTED", 11, ls=1)}{t(436, 146, "17", 13, anchor="end")}
    {t(52, 182, "OPEN SOURCE", 11, ls=1)}{t(436, 182, "3", 13, anchor="end")}
    {t(52, 218, "SYSTEM SPECIALTY", 11, ls=1)}{t(436, 218, "LOCAL-FIRST AI", 13, anchor="end")}
    {t(52, 254, "CURRENT STATUS", 11, ls=1)}{t(436, 254, "BUILDING", 13, anchor="end")}

    {t(548, 58, "LANGUAGES BY REPOSITORY", 15, ls=2)}
    <line class="rule" x1="548" y1="72" x2="948" y2="72"/>
    {t(548, 98, "RUST", 10)}<rect class="bar" x="660" y="89" width="270" height="10"/><rect class="fill grow" x="660" y="89" width="270" height="10"/>
    {t(548, 125, "PYTHON", 10)}<rect class="bar" x="660" y="116" width="270" height="10"/><rect class="fill grow g2" x="660" y="116" width="183" height="10"/>
    {t(548, 152, "TYPESCRIPT", 10)}<rect class="bar" x="660" y="143" width="270" height="10"/><rect class="fill grow g3" x="660" y="143" width="125" height="10"/>
    {t(548, 179, "HTML", 10)}<rect class="bar" x="660" y="170" width="270" height="10"/><rect class="fill grow g4" x="660" y="170" width="97" height="10"/>
    {t(548, 206, "JAVASCRIPT", 10)}<rect class="bar" x="660" y="197" width="270" height="10"/><rect class="fill grow g5" x="660" y="197" width="59" height="10"/>
    {t(548, 233, "SHELL", 10)}<rect class="bar" x="660" y="224" width="270" height="10"/><rect class="fill grow g6" x="660" y="224" width="28" height="10"/>
    {t(548, 260, "WASM", 10)}<rect class="bar" x="660" y="251" width="270" height="10"/><rect class="fill grow g7" x="660" y="251" width="12" height="10"/>
  </g>"""
    return wrap(1000, 310, "GitHub statistics and repository languages", css, body, ink)


def timeline(ink: str) -> str:
    css = """
    .axis { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 1110; stroke-dashoffset: 1110; animation: draw 2.4s cubic-bezier(.6,0,.2,1) forwards; }
    @keyframes draw { to { stroke-dashoffset: 0; } }
    .m { opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
    .m1{animation-delay:.4s}.m2{animation-delay:1.0s}.m3{animation-delay:1.6s}.m4{animation-delay:2.0s}.m5{animation-delay:2.4s}
    .pulse { animation: pulse 2.6s ease-in-out infinite; }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.35} }
    .ring { animation: ring 2.6s ease-out infinite; transform-origin: 960px 125px; }
    @keyframes ring { 0%{transform:scale(.4);opacity:.8} 80%,100%{transform:scale(3);opacity:0} }
    """ + REDUCE % ".axis,.m,.pulse,.ring { animation: none; } .axis{stroke-dashoffset:0} .m{opacity:1} .ring{opacity:0}"

    def mark(x: int, up: bool, yr: str, label: str, cls: str, now: bool = False) -> str:
        if up:
            stem, ty, ly = (x, 121, 96), 74, 90
        else:
            stem, ty, ly = (x, 129, 154), 172, 188
        dot = (f'<circle class="ring" cx="{x}" cy="125" r="4" stroke="var(--accent)" fill="none"/>'
               f'<circle class="pulse" cx="{x}" cy="125" r="4.5" fill="var(--accent)"/>') if now \
            else f'<circle cx="{x}" cy="125" r="4" fill="var(--bone)"/>'
        return (f'<g class="m {cls}">{dot}<line x1="{x}" y1="{stem[1]}" x2="{x}" y2="{stem[2]}" stroke="var(--rule)"/>'
                f'{t(x, ty, yr, 11, "accent", ls=2, anchor="middle")}'
                f'{t(x, ly, label, 10.5, ls=1, anchor="middle")}</g>')
    body = f"""
  <line x1="48" y1="40" x2="1152" y2="40" stroke="var(--rule)"/>
  {t(48, 28, "THE ROUTE SO FAR", 11, "muted", ls=3.5)}
  {t(1152, 28, "FIG. 03", 11, "muted", ls=3.5, anchor="end")}
  <line class="axis" x1="48" y1="125" x2="1158" y2="125"/>
  {mark(110, True, "2023", "B.Tech CE (AI) · UVPCE", "m1")}
  {mark(370, False, "JUL 2026", "Python AI/ML · Kody Technolab", "m2")}
  {mark(640, True, "2026", "Loomis · Conduit · PoseFit Web", "m3")}
  {mark(960, False, "NOW", "3rd yr · CGPA 8.7+ · building", "m4", now=True)}
  <g class="m m5"><circle cx="1152" cy="125" r="3" fill="var(--dim)"/>
    {t(1152, 105, "2027 →", 10, "dim", ls=2, anchor="end")}
    {t(1152, 150, "the next build", 13, "dim", anchor="end")}</g>"""
    return wrap(1200, 220, "Timeline: 2023 B.Tech, July 2026 Kody Technolab, 2026 projects, now, 2027 graduation", css, body, ink)


def experience(ink: str) -> str:
    css = """
    .rise { opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from { opacity:0;transform:translateY(8px); } to { opacity:1;transform:translateY(0); } }
    .a1{animation-delay:.15s} .a2{animation-delay:.35s}
    """ + REDUCE % ".rise { animation: none; opacity: 1; }"
    body = f"""
  <line x1="120" y1="10" x2="120" y2="176" stroke="var(--rule)" stroke-width="1" opacity=".4"/>
  <g class="rise a1">
    {t(48, 42, "2026 –", 12, "accent", ls=2)}
    {t(136, 42, "Kody Technolab Ltd · Python AI/ML · Ahmedabad", 15)}
    {t(136, 68, "joined 14 July 2026 through college placement", 14, "muted")}
  </g>
  <g class="rise a2">
    {t(48, 130, "2023 –", 12, "accent", ls=2)}
    {t(136, 130, "U. V. Patel College of Engineering, Ganpat University · B.Tech", 15)}
    {t(136, 156, "Computer Engineering · AI specialization · graduating 2027 · CGPA 8.7+", 14, "muted")}
  </g>"""
    return wrap(1000, 186, "Experience — Kody Technolab Ltd, Ganpat University", css, body, ink)


def stack(ink: str) -> str:
    css = """
    .rise { opacity: 0; animation: rise .6s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from { opacity:0;transform:translateY(6px); } to { opacity:1;transform:translateY(0); } }
    .a1{animation-delay:.1s} .a2{animation-delay:.2s} .a3{animation-delay:.3s} .a4{animation-delay:.4s} .a5{animation-delay:.5s} .a6{animation-delay:.6s}
    """ + REDUCE % ".rise { animation: none; opacity: 1; }"
    rows = "".join(
        f'{t(48, 32 + 32*i, k, 12, "muted", cls=f"rise a{i+1}", ls=2)}'
        f'{t(154, 32 + 32*i, v, 15, cls=f"rise a{i+1}")}\n  '
        for i, (k, v) in enumerate(STACK))
    body = (f'  <line x1="138" y1="8" x2="138" y2="{32*len(STACK)+2}" stroke="var(--rule)" stroke-width="1" opacity=".4"/>\n  {rows}')
    return wrap(1000, 32 * len(STACK) + 10, "Stack — " + ", ".join(k.lower() for k, _ in STACK), css, body, ink)


def footer(ink: str) -> str:
    css = """
    .draw { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: d 1.6s cubic-bezier(.6,0,.2,1) forwards; }
    @keyframes d { to { stroke-dashoffset: 0; } }
    .dot { animation: p 2.4s ease-in-out infinite; }
    .ring { animation: r 2.4s ease-out infinite; transform-origin: 60px 64px; }
    @keyframes p { 0%,100%{opacity:1} 50%{opacity:.35} }
    @keyframes r { 0%{transform:scale(.4);opacity:.8} 80%,100%{transform:scale(2.6);opacity:0} }
    """ + REDUCE % ".draw,.dot,.ring{animation:none} .draw{stroke-dashoffset:0} .ring{opacity:0}"
    body = f"""
  <line class="draw" x1="48" y1="24" x2="952" y2="24"/>
  <circle class="ring" cx="60" cy="64" r="5" stroke="var(--accent)" stroke-width="1" fill="none"/>
  <circle class="dot" cx="60" cy="64" r="4" fill="var(--accent)"/>
  {t(82, 62, "STATUS — BUILDING", 12, ls=3)}
  {t(82, 82, "probably compiling something in Rust", 11, "muted", ls=2)}
  {t(952, 66, "github.com/Mr-CodeGuru  ·  Gujarat, IN  ·  © 2026", 15, "muted", anchor="end")}"""
    return wrap(1000, 110, "Status: building. Gujarat, India.", css, body, ink)


def badge(label: str, ink: str) -> str:
    w, h = 120, 28  # same box for every badge
    body = (f'  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="2" stroke="var(--rule)" fill="none"/>\n'
            f'  {t(w/2 + 1.25, 18, label, 11, ls=2.5, anchor="middle")}')
    return wrap(w, h, label, "", body, ink).replace("<svg ", f'<svg width="{w}" height="{h}" ', 1)


def build() -> None:
    files: dict[str, callable] = {
        "header-v1": header,
        "whoami": whoami,
        "ecosystem": ecosystem,
        "projects": projects,
        "telemetry": telemetry,
        "github-stats": github_stats,
        "timeline": timeline,
        "experience": experience,
        "stack": stack,
        "footer": footer,
        "badge-github": lambda i: badge("GITHUB", i),
        "badge-linkedin": lambda i: badge("LINKEDIN", i),
    }
    for num, name, slug in SECTIONS:
        files[f"s{num}"] = (lambda n, nm, sl: lambda i: section(n, nm, sl, i))(num, name, slug)
    for theme, ink in THEMES.items():
        out = ROOT / "assets" / ("dark" if theme == "dark" else "")
        out.mkdir(parents=True, exist_ok=True)
        for stem, fn in files.items():
            (out / f"{stem}.svg").write_text(fn(ink), encoding="utf-8", newline="\n")
    print(f"wrote {len(files) * len(THEMES)} SVGs under {ROOT / 'assets'}")


if __name__ == "__main__":
    build()
