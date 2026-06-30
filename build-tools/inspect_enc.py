# -*- coding: utf-8 -*-
import glob, os
# mojibake markers: cp1252 mis-decode of UTF-8 lead byte 0xE2 = 'â' (U+00E2), 0xC2='Â', 0xC3='Ã'
MARKERS = ['â€', 'Â', 'Ã', 'â']
files = (glob.glob(r"D:\wajehawebsites\primevolt\website\*.html")
         + glob.glob(r"D:\wajehawebsites\primevolt\*.md")
         + glob.glob(r"D:\wajehawebsites\primevolt\build-tools\build_pages.py")
         + glob.glob(r"D:\wajehawebsites\primevolt\letterhead\*.html"))
for f in files:
    s = open(f, encoding="utf-8").read()
    hits = []
    i = 0
    while i < len(s):
        if s[i] in ('â', 'Â', 'Ã'):
            ctx = s[max(0,i-12):i+12]
            hits.append((i, ' '.join('U+%04X' % ord(c) for c in s[i:i+3]), ctx.replace('\n',' ')))
            i += 3
        else:
            i += 1
    if hits:
        print("=====", os.path.basename(f), "(", len(hits), "hits )")
        for pos, cps, ctx in hits[:6]:
            print("   ", cps, "::", repr(ctx))
