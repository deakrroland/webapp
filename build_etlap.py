#!/usr/bin/env python3
"""Az étlap-oldal generálása az etlap.json-ból.

Egy adatforrás elve (redesign.md §13/13): az árak egyetlen helyen, az
etlap.json-ban élnek; innen készül a statikus, indexelhető HTML és a
JSON-LD Menu gráf is. A design system CSS-ét az index.html-ből olvassuk,
hogy a két oldal ne tudjon szétcsúszni.
"""
import json, html, re

adat = json.load(open('etlap.json', encoding='utf-8'))
fo = open('index.html', encoding='utf-8').read()

FEJ = fo[fo.index('<link rel="preconnect"'):fo.index('<style>')]
CSS = fo[fo.index('<style>') + 7:fo.index('</style>')]
FEJLEC = fo[fo.index('<header class="fejlec">'):fo.index('</header>') + 9]
LABLEC = fo[fo.index('<footer class="lablec">'):fo.index('</footer>') + 10]
MOBILSAV = fo[fo.index('<nav class="mobilsav"'):fo.index('</nav>', fo.index('<nav class="mobilsav"')) + 6]
TEMA_JS = fo[fo.index('  /* ---------- 1. Téma ----------'):fo.index('  /* ---------- 2. Nyitvatartás')]

e = lambda t: html.escape(str(t), quote=False)
ft = lambda n: format(n, ',').replace(',', ' ')          # keskeny szóköz ezresenként


def tetel_html(t, oszlopok):
    sor = []
    if t.get('sorszam'):
        sor.append('<span class="sorsz" aria-hidden="true">%d</span>' % t['sorszam'])
    sor.append('<h3>%s</h3>' % e(t['nev']))
    if t.get('hazi'):
        sor.append('<span class="bado">A ház sajátja</span>')
    if t.get('kemence'):
        sor.append('<span class="bado">Kemencéből</span>')
    arak = ''.join('<span>%s</span>' % ft(a) for a in t['arak'])
    # hiányzó ár-oszlop kitöltése, hogy a rács ne csússzon el
    arak = '<span aria-hidden="true"></span>' * (oszlopok - len(t['arak'])) + arak
    leiras = '<p class="tetel-leiras">%s</p>' % e(t['leiras']) if t.get('leiras') else ''
    return ('<li class="tetel"><div class="tetel-nev">%s</div>%s'
            '<p class="tetel-ar"><span class="rejtett">Ár:</span>%s</p></li>'
            % (''.join(sor), leiras, arak))


def kategoria_html(k):
    osz = len(k.get('arfej', [1]))
    fejsor = ''
    if k.get('arfej'):
        fejsor = ('<p class="ar-fejsor" aria-hidden="true">%s</p>'
                  % ''.join('<span>%s</span>' % e(a) for a in k['arfej']))
    megj = '<p class="kat-megj">%s</p>' % e(k['megjegyzes']) if k.get('megjegyzes') else ''
    return ('<section class="kat" id="%s" aria-labelledby="%s-cim">'
            '<div class="kat-fej"><h2 id="%s-cim">%s</h2>'
            '<span class="kat-en">%s</span></div>%s%s'
            '<ul class="tetelek">%s</ul></section>'
            % (k['id'], k['id'], k['id'], e(k['nev']), e(k['en']), megj, fejsor,
               ''.join(tetel_html(t, osz) for t in k['tetelek'])))


etel = [k for k in adat['kategoriak'] if not k.get('italok')]
ital = [k for k in adat['kategoriak'] if k.get('italok')]

ugro = ''.join('<a href="#%s">%s</a>' % (k['id'], e(k['nev'])) for k in adat['kategoriak'])

# --- JSON-LD: teljes Menu gráf az adatforrásból ---
def ld_tetel(t, k):
    o = {'@type': 'MenuItem', 'name': t['nev']}
    if t.get('leiras'):
        o['description'] = t['leiras']
    arfej = k.get('arfej')
    o['offers'] = [
        {'@type': 'Offer', 'price': str(a), 'priceCurrency': 'HUF',
         **({'name': arfej[i]} if arfej and i < len(arfej) else {})}
        for i, a in enumerate(t['arak'])
    ]
    return o

ld = {
    '@context': 'https://schema.org',
    '@graph': [
        {'@type': 'Menu', '@id': 'https://gombocpizzeria.hu/etlap/#menu',
         'name': 'Gömböc Pizzéria étlap', 'inLanguage': 'hu-HU',
         'hasMenuSection': [
             {'@type': 'MenuSection', 'name': k['nev'],
              'hasMenuItem': [ld_tetel(t, k) for t in k['tetelek']]}
             for k in adat['kategoriak']]},
        {'@type': 'Restaurant', '@id': 'https://gombocpizzeria.hu/#etterem',
         'name': 'Gömböc Pizzéria', 'telephone': '+36-30-899-9303',
         'address': {'@type': 'PostalAddress', 'streetAddress': 'Nagy Imre út 70.',
                     'addressLocality': 'Pécs', 'postalCode': '7632', 'addressCountry': 'HU'},
         'hasMenu': {'@id': 'https://gombocpizzeria.hu/etlap/#menu'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Főoldal',
             'item': 'https://gombocpizzeria.hu/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Étlap',
             'item': 'https://gombocpizzeria.hu/etlap/'}]}]
}

legolcsobb = min(t['arak'][0] for k in adat['kategoriak'] if k['id'] == 'pizzak'
                 for t in k['tetelek'])

EXTRA_CSS = """
/* ---------- Étlap-oldal ---------- */
.etlap-hero{padding-block:var(--t7) var(--t5)}
.etlap-hero h1{font-size:clamp(2.2rem,1.6rem + 2.4vw,3.6rem);margin-block:var(--t3) var(--t3)}
.etlap-hero p{color:var(--hamu);max-width:56ch}
.ugrosav{position:sticky;top:68px;z-index:30;
  background:color-mix(in srgb,var(--liszt) 92%,transparent);backdrop-filter:blur(12px);
  border-block:1px solid var(--vonal)}
.ugrosav .burok{display:flex;gap:var(--t1);overflow-x:auto;scrollbar-width:thin;
  padding-block:var(--t2);scroll-snap-type:x proximity}
.ugrosav a{flex:none;scroll-snap-align:start;text-decoration:none;white-space:nowrap;
  font-size:var(--sz-kis);font-weight:500;color:var(--hamu);
  padding:var(--t2) var(--t3);border-radius:var(--r-m);
  transition:background var(--ido-gyors) var(--ki),color var(--ido-gyors) var(--ki)}
.ugrosav a:hover{background:color-mix(in srgb,var(--korom) 6%,transparent);color:var(--korom)}
.ugrosav a[aria-current="true"]{background:var(--parazs);color:var(--on-parazs);font-weight:600}
.etlap-torzs{padding-block:var(--t6) var(--t8);display:grid;gap:var(--t8)}
.etlap-blokk{display:grid;gap:var(--t7)}
.blokkfej{font-family:var(--f-display);font-size:var(--sz-h2);font-weight:600;
  padding-bottom:var(--t3);border-bottom:2px solid var(--korom);letter-spacing:-.015em}
.kat{scroll-margin-top:140px}
.kat-fej{display:flex;align-items:baseline;gap:var(--t3);flex-wrap:wrap;
  margin-bottom:var(--t3)}
.kat-fej h2{font-size:var(--sz-h3);font-weight:600}
.kat-en{font-size:var(--sz-mikro);letter-spacing:.14em;text-transform:uppercase;
  color:var(--hamu)}
.kat-megj{font-size:var(--sz-kis);color:var(--hamu);margin-bottom:var(--t3)}
.ar-fejsor{display:flex;justify-content:flex-end;gap:var(--t4);
  font-size:var(--sz-mikro);letter-spacing:.1em;text-transform:uppercase;
  color:var(--hamu);padding-bottom:var(--t2);border-bottom:1px solid var(--vonal)}
.ar-fejsor span{width:76px;text-align:right}
.tetel{display:grid;grid-template-columns:1fr auto;gap:0 var(--t4);
  padding-block:var(--t3);border-bottom:1px solid var(--vonal);align-items:baseline}
.tetel:hover{background:color-mix(in srgb,var(--tegla) 4%,transparent)}
.tetel-nev{display:flex;align-items:baseline;gap:var(--t2);flex-wrap:wrap}
.tetel-nev h3{font-family:var(--f-szoveg);font-size:var(--sz-alap);font-weight:600;
  line-height:1.35}
.sorsz{font-size:var(--sz-mikro);color:var(--hamu);font-variant-numeric:tabular-nums;
  min-width:1.6em}
.bado{font-size:var(--sz-mikro);font-weight:600;color:var(--tegla);
  background:color-mix(in srgb,var(--tegla) 12%,transparent);
  padding:2px 7px;border-radius:var(--r-s)}
.tetel-leiras{grid-column:1;font-size:var(--sz-kis);color:var(--hamu);margin-top:2px;
  max-width:62ch}
.tetel-ar{grid-column:2;grid-row:1/3;display:flex;gap:var(--t4);
  font-variant-numeric:tabular-nums;font-weight:600;white-space:nowrap}
.tetel-ar span{width:76px;text-align:right}
.tetel-ar span:last-child::after{content:" Ft";font-weight:400;color:var(--hamu)}
@media(max-width:560px){
  .ar-fejsor span,.tetel-ar span{width:62px}
  .tetel-ar{gap:var(--t3)}
}
.etlap-zaro{background:var(--tepsi);border-block:1px solid var(--vonal);
  padding-block:var(--t7)}
.etlap-zaro h2{font-size:var(--sz-h2);font-weight:600;margin-bottom:var(--t3)}
.labjegyzetek{display:grid;gap:var(--t2);margin-top:var(--t5);
  font-size:var(--sz-kis);color:var(--hamu)}
.labjegyzetek li{padding-left:var(--t3);border-left:2px solid var(--vonal)}
"""

JS = """
(function(){
  "use strict";
  var gyoker=document.documentElement, valto=document.getElementById("temavalto");
__TEMA__
  /* Ugrósáv: az éppen olvasott kategória jelölése */
  var linkek=[].slice.call(document.querySelectorAll(".ugrosav a"));
  var terkep={};
  linkek.forEach(function(a){ terkep[a.getAttribute("href").slice(1)]=a; });
  if("IntersectionObserver" in window){
    var figy=new IntersectionObserver(function(be){
      be.forEach(function(b){
        if(!b.isIntersecting) return;
        linkek.forEach(function(a){ a.removeAttribute("aria-current"); });
        var a=terkep[b.target.id];
        if(a){ a.setAttribute("aria-current","true");
               a.scrollIntoView({block:"nearest",inline:"nearest"}); }
      });
    },{rootMargin:"-140px 0px -70% 0px"});
    [].forEach.call(document.querySelectorAll(".kat"),function(k){ figy.observe(k); });
  }
  document.getElementById("ev").textContent=new Date().getFullYear();
})();
""".replace('__TEMA__', TEMA_JS.replace('/* ---------- 1. Téma ---------- */', ''))

oldal = """<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Étlap és árak — Gömböc Pizzéria, Pécs</title>
<meta name="description" content="A Gömböc Pizzéria teljes étlapja árakkal: kemencés pizzák {legolcsobb} Ft-tól, frissensültek, tálak, saláták, italok. Pécs, Nagy Imre út 70.">
<link rel="canonical" href="https://gombocpizzeria.hu/etlap/">
<meta name="theme-color" content="#FAF6EF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#14110D" media="(prefers-color-scheme: dark)">
{FEJ}<style>{CSS}{EXTRA}</style>
</head>
<body>
<a class="atugras" href="#fo">Ugrás a tartalomra</a>
{FEJLEC}
<main id="fo">
  <section class="hero etlap-hero">
    <div class="burok">
      <p class="szemold">Pécs-Kertváros, Nagy Imre út 70</p>
      <h1>Étlap</h1>
      <p>Kemencés pizza {legolcsobb} Ft-tól, frissensültek, tálak társaságnak,
         saláták és a teljes itallap. Féladag rendelése esetén az ár 70%-át
         számítjuk fel; az árak tartalmazzák az áfát.</p>
    </div>
  </section>

  <nav class="ugrosav" aria-label="Ugrás étlap-kategóriára">
    <div class="burok">{UGRO}</div>
  </nav>

  <div class="burok etlap-torzs">
    <div class="etlap-blokk">
      <h2 class="blokkfej">Ételek</h2>
      {ETEL}
    </div>
    <div class="etlap-blokk">
      <h2 class="blokkfej">Italok</h2>
      {ITAL}
    </div>
  </div>

  <section class="etlap-zaro">
    <div class="burok">
      <h2>Asztalt foglalnátok?</h2>
      <p style="color:var(--hamu);max-width:56ch">A foglalás a főoldalon vagy
         telefonon megy. Elvitelre is minden rendelhető; a heti menü hétköznap
         11:00 és 13:00 között tart, vagy amíg a készlet enged.</p>
      <p style="display:flex;flex-wrap:wrap;gap:var(--t3);margin-top:var(--t5)">
        <a class="gomb gomb-fo" href="index.html#foglalas">Asztalt foglalok</a>
        <a class="gomb gomb-mas" href="tel:+36308999303">06 30 899 9303</a>
      </p>
      <ul class="labjegyzetek">{LABJ}</ul>
    </div>
  </section>
</main>
{LABLEC}
{MOBILSAV}
<script type="application/ld+json">
{LD}
</script>
<script>{JS}</script>
</body>
</html>
""".format(
    FEJ=FEJ, CSS=CSS, EXTRA=EXTRA_CSS, FEJLEC=FEJLEC.replace(
        '<a href="#heti-menu">Heti menü</a>', '<a href="index.html#heti-menu">Heti menü</a>')
        .replace('<a href="#kinalat">Amit sütünk</a>', '<a href="etlap.html" aria-current="page">Étlap</a>')
        .replace('<a href="#nyitvatartas">Nyitvatartás</a>', '<a href="index.html#nyitvatartas">Nyitvatartás</a>')
        .replace('<a href="#terek">Különterem</a>', '<a href="index.html#terek">Különterem</a>')
        .replace('<a href="#foglalas">Asztalfoglalás</a>', '<a href="index.html#foglalas">Asztalfoglalás</a>')
        .replace('<a class="jel" href="#fo">', '<a class="jel" href="index.html">'),
    UGRO=ugro,
    ETEL=''.join(kategoria_html(k) for k in etel),
    ITAL=''.join(kategoria_html(k) for k in ital),
    LABJ=''.join('<li>%s</li>' % e(x) for x in adat['labjegyzetek']),
    LABLEC=LABLEC.replace('<a href="#heti-menu">Heti menü</a>', '<a href="index.html#heti-menu">Heti menü</a>')
        .replace('<a href="#kinalat">Amit sütünk</a>', '<a href="etlap.html">Étlap</a>')
        .replace('<a href="#nyitvatartas">Nyitvatartás</a>', '<a href="index.html#nyitvatartas">Nyitvatartás</a>')
        .replace('<a href="#foglalas">Asztalfoglalás</a>', '<a href="index.html#foglalas">Asztalfoglalás</a>'),
    MOBILSAV=MOBILSAV.replace('href="#foglalas"', 'href="index.html#foglalas"'),
    LD=json.dumps(ld, ensure_ascii=False, indent=1),
    JS=JS, legolcsobb=ft(legolcsobb))

open('etlap.html', 'w', encoding='utf-8').write(oldal)
print('etlap.html kész — %d bájt, %d tétel' %
      (len(oldal), sum(len(k['tetelek']) for k in adat['kategoriak'])))
