"""Load every page; report console errors and failed (>=400) local requests; test mobile menu."""
import pathlib, glob
from playwright.sync_api import sync_playwright

WEB = pathlib.Path(r"D:\wajehawebsites\primevolt\website")
pages = sorted(glob.glob(str(WEB / "*.html")))

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    total_issues = 0
    for fp in pages:
        name = pathlib.Path(fp).name
        errors, failed = [], []
        pg = b.new_page()
        pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errors.append("PAGEERROR: " + str(e)))
        def on_resp(r):
            if r.status >= 400 and "fonts.g" not in r.url and "primevoltes.ca" not in r.url:
                failed.append("%s %s" % (r.status, r.url.split('/')[-1]))
        pg.on("response", on_resp)
        pg.goto(pathlib.Path(fp).as_uri(), wait_until="load", timeout=60000)
        pg.wait_for_timeout(700)
        # check internal links resolve to existing files
        hrefs = pg.eval_on_selector_all("a[href]", "els => els.map(e => e.getAttribute('href'))")
        broken = []
        for h in set(hrefs):
            if h and not h.startswith(("http", "tel:", "mailto:", "#")):
                target = (WEB / h.split('#')[0])
                if not target.exists():
                    broken.append(h)
        flag = "OK" if not (errors or failed or broken) else "ISSUES"
        if flag == "ISSUES":
            total_issues += 1
        print("[%s] %-14s console=%d failed=%d broken_links=%d" % (flag, name, len(errors), len(failed), len(broken)))
        for e in errors[:4]: print("     console:", e[:120])
        for f in failed[:6]: print("     failed :", f)
        for x in broken[:8]: print("     broken :", x)
        pg.close()

    # mobile menu interaction test
    pg = b.new_page(viewport={"width": 390, "height": 800})
    pg.goto((WEB / "index.html").as_uri(), wait_until="load")
    pg.wait_for_timeout(400)
    pg.click("#menuToggle")
    pg.wait_for_timeout(400)
    is_open = pg.eval_on_selector("#navLinks", "el => el.classList.contains('open')")
    pg.screenshot(path=str(pathlib.Path(r"D:\wajehawebsites\primevolt\build-tools\mobile-menu.png")))
    print("MOBILE MENU opens:", is_open)
    b.close()
    print("TOTAL PAGES WITH ISSUES:", total_issues)
