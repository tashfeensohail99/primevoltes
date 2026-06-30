# -*- coding: utf-8 -*-
"""Single source of truth for the PrimeVolt tower+bolt emblem (open + tile variants)."""

TOWER = ('<path d="M40 100 L55 38"/><path d="M80 100 L65 38"/>'
         '<path d="M55 38 L60 24 L65 38"/><path d="M60 38 L60 24"/>'
         '<path d="M31 70 H89"/><path d="M37 56 H83"/><path d="M43 44 H77"/>'
         '<path d="M45 96 L74 80 M75 96 L46 80 M48 78 L72 66 M73 78 L49 66 M51 64 L69 54 M70 64 L52 54"/>')
BOLT = 'M67 30 L49 66 H60 L54 98 L77 58 H64 L73 30 Z'
BOLT_TILE = 'M67 33 L50 67 H60 L55 97 L77 60 H64 L72 33 Z'

def defs(uid):
    return ('<linearGradient id="%sA" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#E0382F"/><stop offset="1" stop-color="#F58233"/></linearGradient>'
            '<linearGradient id="%sB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFD23F"/><stop offset="1" stop-color="#F5A100"/></linearGradient>') % (uid, uid)

def open_emblem(uid, tower="#16335A", horizon="#0C2747", size=None):
    """Open tower+bolt+sunrise emblem. Use light tower on dark backgrounds."""
    wh = ('width="%d" height="%d" ' % (size, size)) if size else ''
    return ('<svg %sviewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs>' % wh + defs(uid) + '</defs>'
      '<path d="M18 100 A42 42 0 0 1 102 100 Z" fill="url(#%sA)"/>' % uid +
      '<g stroke="#E0382F" stroke-width="2.4" stroke-linecap="round" opacity=".8"><line x1="60" y1="40" x2="60" y2="30"/><line x1="34" y1="52" x2="27" y2="46"/><line x1="86" y1="52" x2="93" y2="46"/></g>'
      '<line x1="12" y1="100" x2="108" y2="100" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>' % horizon +
      '<g stroke="%s" stroke-width="2.5" stroke-linecap="round" fill="none">%s</g>' % (tower, TOWER) +
      '<path d="%s" fill="url(#%sB)" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/></svg>' % (BOLT, uid))

def tile_emblem(uid, size=None, navy="#15406B,#0D2C4D,#081B30"):
    wh = ('width="%d" height="%d" ' % (size, size)) if size else ''
    n0, n1, n2 = navy.split(',')
    return ('<svg %sviewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs>' % wh +
      '<linearGradient id="%sN" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset=".55" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>' % (uid, n0, n1, n2) +
      defs(uid) + '<clipPath id="%sC"><rect x="6" y="6" width="108" height="108" rx="28"/></clipPath></defs>' % uid +
      '<rect x="6" y="6" width="108" height="108" rx="28" fill="url(#%sN)"/>' % uid +
      '<g clip-path="url(#%sC)">' % uid +
      '<path d="M22 102 A38 38 0 0 1 98 102 Z" fill="url(#%sA)" opacity=".95"/>' % uid +
      '<g stroke="#BFE0FF" stroke-width="2.4" stroke-linecap="round" fill="none" opacity=".92">'
      '<path d="M42 102 L56 44"/><path d="M78 102 L64 44"/><path d="M56 44 L60 31 L64 44"/>'
      '<path d="M34 72 H86"/><path d="M40 59 H80"/><path d="M46 48 H74"/>'
      '<path d="M47 98 L73 83 M74 98 L48 83 M50 81 L70 69 M71 81 L51 69"/></g>'
      '<path d="%s" fill="url(#%sB)"/></g></svg>' % (BOLT_TILE, uid))

def tile_mono(uid, size=None):
    wh = ('width="%d" height="%d" ' % (size, size)) if size else ''
    return ('<svg %sviewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' % wh +
      '<rect x="6" y="6" width="108" height="108" rx="28" fill="#0C2747"/>'
      '<clipPath id="%sC"><rect x="6" y="6" width="108" height="108" rx="28"/></clipPath>' % uid +
      '<g clip-path="url(#%sC)" stroke="#fff" stroke-width="2.4" stroke-linecap="round" fill="none" opacity=".9">'
      '<path d="M42 102 L56 44"/><path d="M78 102 L64 44"/><path d="M56 44 L60 31 L64 44"/>'
      '<path d="M34 72 H86"/><path d="M40 59 H80"/><path d="M46 48 H74"/></g>' % uid +
      '<path d="%s" fill="#fff"/></svg>' % BOLT_TILE)
