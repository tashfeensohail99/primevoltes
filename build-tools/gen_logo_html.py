# -*- coding: utf-8 -*-
"""Generate logo-final.html (asset sheet) from the shared emblem definitions."""
import pathlib, emblem

WM = '<div class="wm"><span class="p">PRIME</span><span class="v">VOLT</span></div><div class="tag">ENERGY&nbsp;SYSTEMS</div>'

def asset(id_, cls, inner):
    return '<div class="asset %s" id="%s">%s</div>' % (cls, id_, inner)

# emblem instances (unique gradient id per svg)
mark        = emblem.tile_emblem("m1", size=240)
markmono    = emblem.tile_mono("m2", size=240)
open_navy   = emblem.open_emblem("h1", tower="#16335A", horizon="#0C2747", size=104)
open_light  = emblem.open_emblem("h2", tower="#CFE6FF", horizon="#9FC2E0", size=104)
open_stack  = emblem.open_emblem("s1", tower="#16335A", horizon="#0C2747", size=96)
mono_mark   = emblem.tile_mono("mn", size=104)

html = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<style>
 *{box-sizing:border-box}
 body{margin:0;font-family:'Sora',sans-serif;background:transparent}
 .asset{display:inline-block;background:transparent;padding:24px}
 .wm{font-weight:800;letter-spacing:-1.2px;line-height:.96;white-space:nowrap}
 .tag{font-weight:600;letter-spacing:.42em;line-height:1}
 .lockup{display:flex;align-items:center;gap:20px}
 .lockup.big .wm{font-size:54px}.lockup.big .tag{font-size:14.5px;margin-top:9px}
 .stack{display:flex;flex-direction:column;align-items:center;gap:16px}
 .stack .wm{font-size:46px;text-align:center}.stack .tag{font-size:12.5px;margin-top:8px;text-align:center}
 .lighttheme .wm .p{color:#0C2747}.lighttheme .wm .v{color:#1FA85C}.lighttheme .tag{color:#5B7185}
 .dark .wm .p{color:#fff}.dark .wm .v{color:#2ED47A}.dark .tag{color:#90A8BE}
 .monoNavy .wm .p,.monoNavy .wm .v{color:#0C2747}.monoNavy .tag{color:#0C2747}
</style></head><body>
""" + \
asset("mark","", mark) + \
asset("markMonoNavy","", markmono) + \
asset("horizontal","lighttheme", '<div class="lockup big">' + open_navy + '<div>' + WM + '</div></div>') + \
asset("horizontalWhite","dark", '<div class="lockup big">' + open_light + '<div>' + WM + '</div></div>') + \
asset("stacked","lighttheme", '<div class="stack">' + open_stack + '<div>' + WM + '</div></div>') + \
asset("monoNavy","monoNavy", '<div class="lockup big">' + mono_mark + '<div>' + WM + '</div></div>') + \
"</body></html>"

out = pathlib.Path(r"D:\wajehawebsites\primevolt\build-tools\logo-final.html")
out.write_text(html, encoding="utf-8")
print("WROTE", out)
