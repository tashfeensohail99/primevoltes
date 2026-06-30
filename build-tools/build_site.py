# -*- coding: utf-8 -*-
"""Builds the inner pages of the PrimeVolt site with shared header/footer chrome.
Outputs plain static HTML (no runtime build needed by the user)."""
import pathlib, emblem
WEB = pathlib.Path(r"D:\wajehawebsites\primevolt\website")

NAV = [("index.html","Home"),("about.html","About"),("services.html","Services"),
       ("industry.html","Industry"),("careers.html","Careers"),("insights.html","Insights"),("contact.html","Contact")]

ARROW = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9Z"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7L22 6"/></svg>'
GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 0 20 15.3 15.3 0 0 1 0-20Z"/></svg>'

EMBLEM_HEAD = emblem.tile_emblem("hd").replace('<svg ', '<svg class="emblem" ', 1)
EMBLEM_FOOT = emblem.tile_emblem("ft").replace('<svg ', '<svg class="emblem" width="40" height="40" ', 1)

def header(active):
    links = ""
    for href, label in NAV:
        cls = ' class="active"' if href == active else ''
        links += '<li><a href="%s"%s>%s</a></li>' % (href, cls, label)
    return ('<header class="site-header" id="siteHeader"><div class="container nav">'
      '<a class="brand" href="index.html" aria-label="PrimeVolt Energy Systems — home">' + EMBLEM_HEAD +
      '<span><span class="wm"><span class="p">PRIME</span><span class="v">VOLT</span></span>'
      '<span class="tag" style="display:block">ENERGY&nbsp;SYSTEMS</span></span></a>'
      '<nav aria-label="Primary"><ul class="nav-links" id="navLinks">' + links + '</ul></nav>'
      '<div class="nav-cta"><a class="nav-phone" href="tel:+14375592990">' + PHONE + '+1 (437) 559-2990</a>'
      '<a class="btn btn-primary" href="contact.html">Get in touch</a>'
      '<button class="menu-toggle" id="menuToggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>'
      '</div></div></header>')

def head(title, desc, canonical, keywords=""):
    return ('<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
      '<title>' + title + '</title><meta name="description" content="' + desc + '">' +
      ('<meta name="keywords" content="' + keywords + '">' if keywords else '') +
      '<link rel="canonical" href="' + canonical + '">'
      '<meta property="og:type" content="website"><meta property="og:title" content="' + title + '">'
      '<meta property="og:description" content="' + desc + '"><meta property="og:url" content="' + canonical + '">'
      '<meta property="og:image" content="https://www.primevoltes.ca/assets/img/og-cover.png"><meta name="twitter:card" content="summary_large_image">'
      '<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml"><link rel="alternate icon" href="assets/img/favicon.ico"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">'
      '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      '<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
      '<link rel="stylesheet" href="assets/css/style.css"><script>document.documentElement.classList.add(\'js\')</script></head>')

def page_hero(crumb, title, sub):
    return ('<section class="page-hero"><div class="hero-glow"></div>'
      '<svg class="hero-bg" viewBox="0 0 1440 500" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="opacity:.6">'
      '<g stroke="#34D17E" stroke-opacity=".12" stroke-width="1"><line x1="0" y1="80" x2="1440" y2="200"/><line x1="0" y1="300" x2="1440" y2="160"/><line x1="0" y1="420" x2="1440" y2="500"/></g></svg>'
      '<div class="container"><div class="crumb reveal"><a href="index.html">Home</a> &nbsp;/&nbsp; ' + crumb + '</div>'
      '<h1 class="reveal">' + title + '</h1><p class="reveal d1">' + sub + '</p></div></section>')

CTA = ('<section class="section section--tight"><div class="container"><div class="cta-band reveal"><div class="ctaglow"></div>'
  '<div style="position:relative;z-index:2"><span class="eyebrow" style="color:var(--gold-soft)">Let\'s build what\'s next</span>'
  '<h2>Ready to strengthen your next transmission or grid project?</h2>'
  '<p>Talk to PrimeVolt about technical support, maintenance coordination, documentation or modernization assistance — and put two decades of transmission expertise to work.</p>'
  '<div class="cta-actions"><a class="btn btn-gold" href="contact.html">Request a Consultation</a>'
  '<a class="btn btn-light" href="tel:+14375592990">' + PHONE + '+1 (437) 559-2990</a></div></div></div></div></section>')

FOOTER = ('<footer class="site-footer"><div class="container"><div class="footer-top">'
  '<div class="footer-brand"><div class="brand">'
  + EMBLEM_FOOT +
  '<span class="wm" style="font-size:1.3rem;font-family:Sora;font-weight:800;color:#fff">PRIME<span class="v" style="color:var(--cyan)">VOLT</span></span></div>'
  '<p>An Ontario-based power-infrastructure firm specializing in high-voltage transmission support, grid maintenance coordination, and modernization services.</p></div>'
  '<div class="footer"><h4>Company</h4><ul><li><a href="about.html">About &amp; Founder</a></li><li><a href="services.html">Services</a></li><li><a href="industry.html">Industry &amp; Market</a></li><li><a href="careers.html">Careers</a></li><li><a href="insights.html">Insights</a></li></ul></div>'
  '<div class="footer"><h4>Services</h4><ul><li><a href="services.html">Transmission Support</a></li><li><a href="services.html">Grid Maintenance</a></li><li><a href="services.html">Smart-Grid Modernization</a></li><li><a href="services.html">Tender &amp; BOQ</a></li></ul></div>'
  '<div class="footer"><h4>Contact</h4><ul class="footer-contact">'
  '<li>' + PIN + '<span>Greater Toronto Area,<br>Ontario, Canada</span></li>'
  '<li>' + PHONE + '<a href="tel:+14375592990">+1 (437) 559-2990</a></li>'
  '<li>' + MAIL + '<a href="mailto:info@primevoltes.ca">info@primevoltes.ca</a></li></ul></div></div>'
  '<div class="footer-bottom"><div>&copy; <span data-year>2026</span> PrimeVolt Energy Systems Limited &middot; Ontario Corporation No. 1001613569 &middot; <a href="privacy.html" style="color:#9fb6cc">Privacy</a></div>'
  '<div class="socials">'
  '<a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg></a>'
  '<a href="mailto:info@primevoltes.ca" aria-label="Email">' + MAIL + '</a></div></div></div></footer>')

SCRIPT = '<script src="assets/js/main.js"></script>'

def write(fn, active, head_html, body):
    html = '<!doctype html>\n<html lang="en">\n' + head_html + '\n<body>\n' + header(active) + '\n<main>\n' + body + '\n</main>\n' + FOOTER + '\n' + SCRIPT + '\n</body>\n</html>\n'
    (WEB / fn).write_text(html, encoding="utf-8")
    print("BUILT", fn, len(html), "bytes")

# ----- bring in page bodies -----
import build_pages
build_pages.build(globals())
import build_articles
build_articles.build(globals())
