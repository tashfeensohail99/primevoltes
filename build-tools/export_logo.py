"""Export PrimeVolt logo assets as transparent PNGs at high resolution."""
import pathlib
from playwright.sync_api import sync_playwright

SRC = pathlib.Path(r"D:\wajehawebsites\primevolt\build-tools\logo-final.html").resolve().as_uri()
OUT = pathlib.Path(r"D:\wajehawebsites\primevolt\brand")
OUT.mkdir(parents=True, exist_ok=True)

# (selector, filename, device_scale_factor)
ASSETS = [
    ("#mark",            "primevolt-mark.png",            6),
    ("#markMonoNavy",    "primevolt-mark-mono.png",       6),
    ("#horizontal",      "primevolt-logo-horizontal.png", 5),
    ("#horizontalWhite", "primevolt-logo-white.png",      5),
    ("#stacked",         "primevolt-logo-stacked.png",    5),
    ("#monoNavy",        "primevolt-logo-mono.png",       5),
]

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    for sel, name, dsf in ASSETS:
        pg = b.new_page(viewport={"width": 1400, "height": 700}, device_scale_factor=dsf)
        pg.goto(SRC, wait_until="load", timeout=60000)
        try: pg.evaluate("document.fonts.ready")
        except Exception: pass
        pg.wait_for_timeout(500)
        pg.locator(sel).screenshot(path=str(OUT / name), omit_background=True)
        pg.close()
        print("EXPORTED", name)
    b.close()
print("ALL DONE")
