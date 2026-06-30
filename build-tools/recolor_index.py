# -*- coding: utf-8 -*-
"""Swap the old tile emblems for the new tower+bolt emblem and recolour accent-blues to green in index.html (and og-cover)."""
import re, emblem

BLUEMAP = {
    "#2E7DF6": "#1FA85C", "#1E63D6": "#178A49", "#2563EB": "#178A49", "#1E54CC": "#127A47",
    "#2160E6": "#178A49", "#1C6DD0": "#178A49", "#46B4F5": "#34D17E", "#3FB0F4": "#34D17E",
    "#56CCF2": "#34D17E", "#9FE0FF": "#A7E9C6", "#7DD3FC": "#A7E9C6", "#A5E3FF": "#A7E9C6",
    "#7FB0E0": "#7FC9A6", "#6FA6D8": "#7FC9A6", "#6CA5DA": "#7FC9A6", "#79A6D6": "#7FC9A6",
    "#4E83BF": "#3E9E72", "#5B8FC0": "#3E9E72", "#3E7AB8": "#3E9E72", "#5E8BBE": "#3E9E72",
    "#8FC0E8": "#A7E9C6", "#2E5C8A": "#1E7A52", "#2D6CB5": "#1E8A55",
    "rgba(46,125,246": "rgba(31,168,92", "rgba(70,180,245": "rgba(52,209,126",
}

EMBLEM_RE = re.compile(r'<svg class="emblem".*?</svg>', re.S)

def process(path, emblem_ids, foot_attr=None):
    s = open(path, encoding="utf-8").read()
    news = []
    for i, uid in enumerate(emblem_ids):
        extra = ' width="40" height="40"' if (foot_attr and i == 1) else ''
        news.append(emblem.tile_emblem(uid).replace('<svg ', '<svg class="emblem"%s ' % extra, 1))
    n_found = len(EMBLEM_RE.findall(s))
    def repl(m):
        return news.pop(0) if news else m.group(0)
    s = EMBLEM_RE.sub(repl, s)
    for a, b in BLUEMAP.items():
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8", newline="").write(s)
    print("%-22s emblems matched=%d replaced=%d" % (path.split('\\')[-1], n_found, len(emblem_ids)))

process(r"D:\wajehawebsites\primevolt\website\index.html", ["ih", "if"], foot_attr=True)
