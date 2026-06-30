"""Export the letterhead to print-ready A4 PDFs: a sample-letter version and a blank template."""
import pathlib
from playwright.sync_api import sync_playwright

SRC = pathlib.Path(r"D:\wajehawebsites\primevolt\letterhead\primevolt-letterhead.html").resolve().as_uri()
OUT = pathlib.Path(r"D:\wajehawebsites\primevolt\letterhead")

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")

    # 1) Sample letter PDF
    pg = b.new_page()
    pg.goto(SRC, wait_until="networkidle")
    pg.wait_for_timeout(500)
    pg.emulate_media(media="print")
    pg.pdf(path=str(OUT / "PrimeVolt-Letterhead-Sample.pdf"),
           width="210mm", height="297mm", print_background=True,
           margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    print("PDF: sample")

    # 2) Blank template PDF (clear body content, drop the sample flag)
    pg2 = b.new_page()
    pg2.goto(SRC, wait_until="networkidle")
    pg2.wait_for_timeout(400)
    pg2.evaluate("""() => {
        const body = document.querySelector('.body');
        if (body) body.innerHTML = '';
    }""")
    pg2.emulate_media(media="print")
    pg2.pdf(path=str(OUT / "PrimeVolt-Letterhead-Blank.pdf"),
            width="210mm", height="297mm", print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    print("PDF: blank")

    b.close()
print("LETTERHEAD PDFs DONE")
