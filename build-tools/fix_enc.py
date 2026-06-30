# -*- coding: utf-8 -*-
"""Reverse the UTF-8 -> cp1252 -> UTF-8 double-encoding (mojibake) and strip the BOM
introduced by a PowerShell Get-Content/Set-Content round-trip."""
import glob, os, codecs

ROOT = r"D:\wajehawebsites\primevolt"

def reverse_mojibake(s):
    """Undo .NET cp1252 mis-decode of UTF-8 bytes."""
    out = bytearray()
    for ch in s:
        try:
            out += ch.encode("cp1252")
        except UnicodeEncodeError:
            o = ord(ch)
            if o <= 0xFF:        # C1 control: .NET mapped undefined byte b -> U+00bb
                out.append(o)
            else:
                raise
    return out.decode("utf-8")

pats = ["*.html", "*.py", "*.md", "*.xml", "*.txt", "*.toml", "*.css", "*.js"]
subs = ["", "website", r"website\assets\css", r"website\assets\js", "build-tools", "letterhead", "website-plan"]
files = []
for sub in subs:
    base = os.path.join(ROOT, sub) if sub else ROOT
    for p in pats:
        files += glob.glob(os.path.join(base, p))
files = sorted(set(files))

fixed_n = 0
for f in files:
    if os.path.basename(f) in ("fix_enc.py", "inspect_enc.py"):
        continue
    raw = open(f, "rb").read()
    had_bom = raw.startswith(codecs.BOM_UTF8)
    if had_bom:
        raw = raw[3:]
    s = raw.decode("utf-8")
    changed = had_bom
    if ("â" in s) or ("Â" in s) or ("Ã" in s):
        try:
            s = reverse_mojibake(s)
            changed = True
        except Exception as e:
            print("SKIP (cannot reverse):", os.path.basename(f), "->", e)
            continue
    if changed:
        with open(f, "w", encoding="utf-8", newline="") as out:
            out.write(s)
        fixed_n += 1
        tag = "FIXED+BOM" if "â" not in raw.decode("utf-8", "ignore") else "FIXED"
        print(tag, os.path.relpath(f, ROOT))

print("TOTAL CLEANED:", fixed_n)
