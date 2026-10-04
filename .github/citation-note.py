"""Add the citation note to a copy of the legacy site (stand-in for the generator).

Used by pages.yml until the generator exists. Renders docs/STABLE-REFERENCES.md
to versions.html in the frame of the legacy pages, adds a nav entry and a note
above the navigation to every page. Fails loudly if the legacy markup no longer
matches.

Usage: citation-note.py SITE_DIR NOTICE_MD
"""
import pathlib
import re
import sys

import markdown

NOTE = (
    '<div class="alert alert-info" role="alert" '
    'style="margin:0;border:5px solid #000;border-radius:0;font-size:16px">'
    "This is a <strong>dynamic, live zoo</strong>. The <strong>citable state</strong> "
    "for the <strong>SIMPAR 2014</strong> and <strong>JOSER 2016</strong> surveys "
    "<strong>lies on corlab</strong>, in <strong>pinned states that do not "
    'change</strong>. <a href="./versions.html"><strong>Where to find it, and why '
    "it stays stable</strong></a></div>"
)
NAV_ENTRY = '<li><a href="./versions.html">Versions</a></li>'
CONTRIBUTE_LI = re.compile(r'<li[^>]*>\s*<a href="\./contribute\.html">Contribute</a>\s*</li>')
# the legacy navbar is fixed to the top and would cover the note
NAVBAR = re.compile(r'<nav class="navbar navbar-inverse navbar-fixed-top"')
NO_BODY_PADDING = "<style>body{padding-top:0 !important}</style>"


def sub_once(pattern, repl, text, what, name):
    new, n = pattern.subn(repl, text, count=1)
    if n != 1:
        sys.exit(f"{name}: {what} not found")
    return new


def main(site_dir, notice_md):
    site = pathlib.Path(site_dir)
    index = (site / "index.html").read_text(encoding="utf-8")

    nav = re.search(r"<body>(.*?</nav>)", index, re.S)
    if not nav:
        sys.exit("index.html: navbar not found")
    body = markdown.markdown(
        pathlib.Path(notice_md).read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code"],
    ).replace("<table>", '<table class="table table-striped">')
    (site / "versions.html").write_text(
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<link rel="icon" href="images/favicon.png">\n'
        "<title>Versions - Robotics DSL Zoo</title>\n"
        '<link href="dist/css/bootstrap.min.css" rel="stylesheet">\n'
        '<link rel="stylesheet" type="text/css" href="dist/css/custom.css">\n'
        "</head>\n<body>" + nav.group(1) + '\n<div class="container">\n'
        '<div class="starter-template">\n' + body + "\n</div>\n</div>\n"
        '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n'
        '<script src="dist/js/bootstrap.min.js"></script>\n</body>\n</html>\n',
        encoding="utf-8",
    )

    pages = sorted(site.glob("*.html"))
    for page in pages:
        text = page.read_text(encoding="utf-8")
        text = sub_once(CONTRIBUTE_LI, lambda m: m.group(0) + NAV_ENTRY, text, "nav entry", page.name)
        text = sub_once(NAVBAR, lambda m: NOTE + m.group(0).replace("fixed-top", "static-top"), text, "fixed navbar", page.name)
        text = sub_once(re.compile(r"</head>"), lambda m: NO_BODY_PADDING + m.group(0), text, "</head>", page.name)
        page.write_text(text, encoding="utf-8")
    print(f"note added to {len(pages)} pages")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
