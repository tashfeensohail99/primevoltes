# -*- coding: utf-8 -*-
"""Render the website plan markdown into a branded A4 PDF."""
import pathlib, markdown
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(r"D:\wajehawebsites\primevolt")
md = (ROOT / "website-plan" / "PrimeVolt-Website-Plan.md").read_text(encoding="utf-8")
# drop the first H1 (we render a custom cover instead)
lines = md.splitlines()
if lines and lines[0].startswith("# "):
    lines = lines[1:]
body_html = markdown.markdown("\n".join(lines), extensions=["tables", "fenced_code", "sane_lists", "attr_list"])

EMBLEM = ('<svg width="78" height="78" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">'
  '<defs><linearGradient id="cA" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#E0382F"/><stop offset="1" stop-color="#F58233"/></linearGradient>'
  '<linearGradient id="cB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFD23F"/><stop offset="1" stop-color="#F5A100"/></linearGradient></defs>'
  '<path d="M18 100 A42 42 0 0 1 102 100 Z" fill="url(#cA)"/>'
  '<g stroke="#E0382F" stroke-width="2.4" stroke-linecap="round" opacity=".8"><line x1="60" y1="40" x2="60" y2="30"/><line x1="34" y1="52" x2="27" y2="46"/><line x1="86" y1="52" x2="93" y2="46"/></g>'
  '<line x1="12" y1="100" x2="108" y2="100" stroke="#9FC2E0" stroke-width="2.6" stroke-linecap="round"/>'
  '<g stroke="#CFE6FF" stroke-width="2.5" stroke-linecap="round" fill="none"><path d="M40 100 L55 38"/><path d="M80 100 L65 38"/><path d="M55 38 L60 24 L65 38"/><path d="M60 38 L60 24"/><path d="M31 70 H89"/><path d="M37 56 H83"/><path d="M43 44 H77"/><path d="M45 96 L74 80 M75 96 L46 80 M48 78 L72 66 M73 78 L49 66 M51 64 L69 54 M70 64 L52 54"/></g>'
  '<path d="M67 30 L49 66 H60 L54 98 L77 58 H64 L73 30 Z" fill="url(#cB)" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/></svg>')

html = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
 :root{--navy:#0C2747;--blue:#1FA85C;--gold:#F59E0B;--slate:#5B7185;--line:#E5ECF3;--mist:#F4F7FB}
 *{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
 body{margin:0;font-family:'Inter',sans-serif;color:#27384a;font-size:10.6pt;line-height:1.62}
 @page{size:A4;margin:20mm 18mm}
 @page:first{margin:0}
 h1,h2,h3,h4{font-family:'Sora',sans-serif;color:var(--navy);line-height:1.2}
 h2{font-size:16pt;margin:22pt 0 8pt;padding-bottom:6pt;border-bottom:2px solid var(--line)}
 h3{font-size:12pt;margin:16pt 0 5pt;color:#123a63}
 p{margin:0 0 8pt}
 a{color:var(--blue);text-decoration:none}
 strong{color:var(--navy)}
 table{width:100%;border-collapse:collapse;margin:10pt 0;font-size:9.2pt}
 th{background:var(--navy);color:#fff;text-align:left;padding:7pt 9pt;font-family:'Sora';font-weight:600;font-size:8.6pt}
 td{padding:7pt 9pt;border-bottom:1px solid var(--line);vertical-align:top}
 tr:nth-child(even) td{background:var(--mist)}
 ul,ol{margin:0 0 8pt;padding-left:18pt}
 li{margin-bottom:3pt}
 code{background:var(--mist);border:1px solid var(--line);border-radius:4px;padding:1px 5px;font-size:9pt;color:#123a63}
 pre{background:#0C2747;color:#cfe0f0;border-radius:8px;padding:12pt 14pt;overflow:auto;font-size:8.6pt;line-height:1.5}
 pre code{background:none;border:none;color:#cfe0f0;padding:0}
 blockquote{margin:10pt 0;padding:10pt 14pt;background:var(--mist);border-left:4px solid var(--blue);border-radius:0 8px 8px 0;color:var(--navy)}
 hr{border:none;border-top:1px solid var(--line);margin:16pt 0}
 .cover{height:297mm;background:linear-gradient(150deg,#15406B,#0D2C4D 55%,#07182C);color:#fff;padding:42mm 30mm;display:flex;flex-direction:column;page-break-after:always;position:relative;overflow:hidden}
 .cover .glow{position:absolute;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(31,168,92,.42),transparent 62%);top:-200px;right:-160px}
 .cover .brand{display:flex;align-items:center;gap:16px;position:relative;z-index:2}
 .cover .wm{font-family:'Sora';font-weight:800;font-size:26pt;letter-spacing:-.5px}
 .cover .wm .v{color:#2ED47A}
 .cover .tag{font-family:'Sora';font-weight:600;font-size:8pt;letter-spacing:6px;color:#90a8be;margin-top:3px}
 .cover .mid{margin-top:auto;margin-bottom:auto;position:relative;z-index:2}
 .cover .kicker{font-family:'Sora';font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#FFD774;font-size:10pt;margin-bottom:14px}
 .cover h1{color:#fff;font-size:34pt;line-height:1.1;max-width:150mm;margin:0 0 16px}
 .cover .sub{color:#b9cee2;font-size:12pt;max-width:140mm}
 .cover .meta{position:relative;z-index:2;border-top:1px solid rgba(255,255,255,.18);padding-top:16px;display:flex;justify-content:space-between;color:#a9c2da;font-size:9pt}
 .cover .meta b{color:#fff;font-family:'Sora'}
</style></head><body>
<div class="cover"><div class="glow"></div>
  <div class="brand">__EMBLEM__<div><div class="wm">PRIME<span class="v">VOLT</span></div><div class="tag">ENERGY&nbsp;SYSTEMS</div></div></div>
  <div class="mid"><div class="kicker">Complete Website Plan &amp; Blueprint</div>
    <h1>A premium web presence for PrimeVolt Energy Systems</h1>
    <div class="sub">Brand, letterhead, a full premium website and an SEO &amp; content strategy &mdash; aligned to the business plan and the Canada&nbsp;C11 entrepreneur application.</div></div>
  <div class="meta"><div>Prepared for <b>Rana Muhammad Zahid Hafeez</b><br>PrimeVolt Energy Systems Limited &middot; Ontario Corp. No. 1001613569</div>
    <div style="text-align:right"><b>www.primevoltes.ca</b><br>info@primevoltes.ca &middot; +1 (437) 559-2990</div></div>
</div>
__BODY__
</body></html>""".replace("__EMBLEM__", EMBLEM).replace("__BODY__", body_html)

out_html = ROOT / "website-plan" / "_plan_render.html"
out_html.write_text(html, encoding="utf-8")

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page()
    pg.goto(out_html.resolve().as_uri(), wait_until="load", timeout=60000)
    try: pg.evaluate("document.fonts.ready")
    except Exception: pass
    pg.wait_for_timeout(600)
    pg.emulate_media(media="print")
    pg.pdf(path=str(ROOT / "website-plan" / "PrimeVolt-Website-Plan.pdf"),
           format="A4", print_background=True,
           display_header_footer=True,
           header_template='<div></div>',
           footer_template='<div style="width:100%;font-size:7pt;color:#90a8be;font-family:sans-serif;padding:0 14mm;display:flex;justify-content:space-between"><span>PrimeVolt Energy Systems &mdash; Website Plan</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>',
           margin={"top": "16mm", "bottom": "16mm", "left": "0", "right": "0"})
    b.close()
out_html.unlink(missing_ok=True)
print("PLAN PDF DONE")
