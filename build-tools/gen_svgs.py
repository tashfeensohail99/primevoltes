# -*- coding: utf-8 -*-
"""Write standalone master SVGs for the new emblem."""
import pathlib, emblem
B = pathlib.Path(r"D:\wajehawebsites\primevolt\brand")

def doc(svg):  # add role/label for a standalone file
    return svg.replace('aria-hidden="true"', 'role="img" aria-label="PrimeVolt Energy Systems"', 1)

(B / "primevolt-mark.svg").write_text(doc(emblem.tile_emblem("pv", size=120)), encoding="utf-8")
(B / "favicon.svg").write_text(doc(emblem.tile_emblem("fv", size=64)), encoding="utf-8")
(B / "primevolt-emblem-open.svg").write_text(doc(emblem.open_emblem("op", size=120)), encoding="utf-8")
print("SVGs written: primevolt-mark.svg, favicon.svg, primevolt-emblem-open.svg")
