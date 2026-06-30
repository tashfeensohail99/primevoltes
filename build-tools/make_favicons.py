"""Render favicon.svg at high-res (transparent) then produce icon sizes + .ico."""
import pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BRAND = pathlib.Path(r"D:\wajehawebsites\primevolt\brand")
svg = (BRAND / "favicon.svg").read_text(encoding="utf-8")
html = f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:transparent}} svg{{width:512px;height:512px}}</style></head><body>{svg}</body></html>'

big = BRAND / "favicon-512.png"
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(device_scale_factor=1, viewport={"width": 512, "height": 512})
    pg.set_content(html, wait_until="networkidle")
    pg.locator("svg").screenshot(path=str(big), omit_background=True)
    b.close()

src = Image.open(big).convert("RGBA")
for size in (16, 32, 48, 64, 180, 192, 512):
    img = src.resize((size, size), Image.LANCZOS)
    if size == 180:
        img.save(BRAND / "apple-touch-icon.png")
    elif size == 192:
        img.save(BRAND / "favicon-192.png")
    elif size == 512:
        img.save(BRAND / "favicon-512.png")
    else:
        img.save(BRAND / f"favicon-{size}.png")
# multi-resolution .ico
ico_sizes = [(16,16),(32,32),(48,48),(64,64)]
src.save(BRAND / "favicon.ico", sizes=ico_sizes)
print("FAVICONS DONE")
