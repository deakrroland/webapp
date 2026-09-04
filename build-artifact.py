#!/usr/bin/env python3
"""index.html → artifact-változat (linkelhető, claude.ai Artifactként publikálható).

Az Artifact-futtató maga adja a <!doctype>, <html>, <head> és <body> burkot, ezért
a feltöltött fájl NEM tartalmazhatja őket. Ez a script egyetlen forrásból
(index.html) állítja elő a burok nélküli változatot, hogy a két verzió ne
csússzon szét kézi másolgatástól.

Amit kivesz:  <meta>, <link rel=canonical>  — a burok adja, vagy értelmetlen a
              beágyazott nézetben (og:, robots, theme-color).
Amit átír:    a <title>-t rövid névre. Az éles, keresőoptimalizált title a
              redesign.md §10.1-ben van, és az index.html-ben marad.
Minden más    — a design system, a JSON-LD gráf és a teljes script — változatlan.

Használat:  python3 build-artifact.py [kimeneti_fajl]
"""
import re, sys, pathlib

FORRAS = pathlib.Path(__file__).parent / "index.html"
KIMENET = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "papa-giorgio-artifact.html")

s = FORRAS.read_text(encoding="utf-8")

fej = s[s.index("<head>") + 6: s.index("</head>")]
test = s[s.index("<body>") + 6: s.rindex("</body>")]

# a <head>-ből csak az kell, ami a burkon belül is értelmes
fej = re.sub(r"[ \t]*<meta\b[^>]*>\n?", "", fej)
fej = re.sub(r"[ \t]*<link\b[^>]*>\n?", "", fej)
eles_title = re.search(r"<title>(.*?)</title>", fej, re.S)
if not eles_title:
    sys.exit("HIBA: nincs <title> az index.html-ben.")
fej = fej.replace(eles_title.group(0),
    "<title>Papa Giorgio Street Food</title>\n"
    "<!-- Az éles oldal keresőoptimalizált title-je ettől eltér, lásd redesign.md §10.1:\n"
    "     " + eles_title.group(1).strip() + " -->")

KIMENET.write_text((fej.strip() + "\n\n" + test.strip() + "\n"), encoding="utf-8")
print(f"{KIMENET}: {KIMENET.stat().st_size} bájt")
