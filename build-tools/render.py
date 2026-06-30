"""QC renderer: screenshot HTML/SVG files via system Edge (Chromium).
Usage:
  python render.py <input.html|input.svg> <output.png> [selector] [width] [height] [scale] [full]
If input is .svg it is wrapped in a minimal HTML page (transparent bg).
"""
import sys, os, pathlib, base64
from playwright.sync_api import sync_playwright

inp = sys.argv[1]
out = sys.argv[2]
selector = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] not in ("-", "") else None
width = int(sys.argv[4]) if len(sys.argv) > 4 else 1440
height = int(sys.argv[5]) if len(sys.argv) > 5 else 900
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
full = (len(sys.argv) > 7 and sys.argv[7] == "full")

path = pathlib.Path(inp).resolve()
is_svg = path.suffix.lower() == ".svg"

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(viewport={"width": width, "height": height}, device_scale_factor=scale)
    pg.emulate_media(reduced_motion="reduce")
    if is_svg:
        svg = path.read_text(encoding="utf-8")
        html = f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;padding:0;background:transparent}}</style></head><body>{svg}</body></html>'
        pg.set_content(html, wait_until="networkidle")
        target = pg.locator(selector or "svg").first
        target.screenshot(path=out, omit_background=True)
    else:
        pg.goto(path.as_uri(), wait_until="load", timeout=60000)
        try:
            pg.evaluate("document.fonts.ready")
        except Exception:
            pass
        pg.wait_for_timeout(600)
        if selector:
            pg.locator(selector).first.screenshot(path=out)
        else:
            pg.screenshot(path=out, full_page=full)
    b.close()
print("RENDERED", out)
