# Váradi Ferenc Üveges (pecsiuveges.hu) — UI/UX redesign koncepció és prototípus

> ### Módszertani figyelmeztetés: rekonstrukcióból dolgoztam
>
> A `www.pecsiuveges.hu` közvetlen lekérése ebben a környezetben hálózati szinten
> tiltott (egress proxy: `Host not in allowlist: www.pecsiuveges.hu`, HTTP 403).
> Ugyanígy blokkolt minden aggregátor-oldal (`uzleti.hu`, `cylex.hu`, `daibau.hu`,
> `bonumventus.hu`, `yoys.hu`). **A HTML forrását tehát nem láttam.**
>
> Amiből dolgoztam:
> 1. **A briefbe beillesztett oldalszöveg** — ez a legerősebb forrás, mert szó
>    szerinti, és önmagában is diagnosztizálható (lásd §2.1: a karakterkódolási hiba
>    magából a beillesztett szövegből bizonyítható).
> 2. **A Google Cégprofil kivonata** (a briefben szintén szó szerint).
> 3. **Keresőindex-találatok**: `daibau.hu/varadi_ferenc_ev`, `varadi-uveges.uzleti.hu`,
>    `xn--pcs-bma.cylex.hu`, `szakkatalogus.hu`, `yoys.hu`, valamint az indexelt
>    oldalcím: `Pécsi Üveges - képkeretezés, üveg, üvegezés, tükör ...`
>
> Minden ténymegállapítás mellett jelölöm a **bizonyosság szintjét**. Ahol a
> forrás csak a HTML lenne, ott nem állítok, hanem **ellenőrzendőként** jelölöm
> (§15.2). Számot, árat, kapacitást **sehol nem találtam ki** — a placeholderek
> `[szögletes zárójelben]` állnak.

---

## 0. Kontextus — amit tudok, és amit nem

A brief kontextusmezői üresen érkeztek. Az alábbi táblázat **kizárólag dokumentált
tényeket** tartalmaz.

| Mező | Amit tudok | Forrás / bizonyosság |
|---|---|---|
| Ügyfél | Váradi Ferenc egyéni vállalkozó üveges + Váradiné Czike Éva | oldalszöveg · **magas** |
| Telephely | 7632 Pécs, Nagy Imre út 29. (Kertváros) | oldalszöveg + Google + 5 katalógus · **magas** |
| Vezetékes | 72 / 321 316 | oldalszöveg + Yoys + Cylex · **magas** |
| Mobil | 06 30 267 6709 | Google Cégprofil + oldalszöveg · **magas** |
| E-mail | varadi@freemail.hu | oldalszöveg · **magas** |
| Nyitvatartás | H–P 9:00–17:00; rendkívüli esetben non-stop hívható | oldalszöveg + Google · **magas** |
| Google-értékelés | 4,7 · 66 vélemény | Google Cégprofil · **magas** |
| Google-kategória | „Üveg- és tükörbolt" | Google Cégprofil · **magas** |
| Működés kezdete | „2000-ben nyitotta pécsi üvegműhelyét" | daibau.hu profil · **közepes** (nem az ügyfél saját közlése) |
| Bővítés | „Pécsett Kertvárosban **megnyitottuk**… képkeretezési kínálattal kibővített" | oldalszöveg · **magas** (de az időpont ismeretlen — §15) |
| Bővebb szolgáltatáskör | üvegterasz, üvegkorlát, télikert, üvegtető | daibau.hu · **közepes** — a saját oldalon **nem szerepel** |
| Biztosítós kárrendezés | vélemény szerint „órákon belül árajánlat, 48 órán belül beépítés, 2 nap alatt kész" | katalógus-vélemény · **közepes**, egyetlen vásárlói leírás |
| Vidéki kiszállás | vállal, és a kiszállási költség megosztható több megrendelő között | oldalszöveg · **magas** |
| Ár, kapacitás, garancia, átfutás | **nincs adat** | — → §15 |

**Az oldal EGY dolga.** A briefben ez a mező üres volt, ezért levezetem, nem
kitalálom: a jelenlegi oldalon egyetlen cselekvésre szólít fel — „**Hívjon –
jövünk – segítünk!**" —, és minden más információ ezt támasztja alá. A Google
Cégprofil elsődleges gombja szintén a HÍVÁS. Az oldal egy dolga tehát:
**telefonhívás vagy méretadatokkal kitöltött ajánlatkérés kiváltása.**
Nem webshop, nem katalógus, nem márkaépítés.

**Amit nem szabad megváltoztatni.** A brief ezt is üresen hagyta. Amit én
*javaslok* érinthetetlennek — mert értéket hordoz, és §15-ben megerősítendő:
a `pecsiuveges.hu` domain, a „Váradi Ferenc Üveges" cégnév, a két név
együttes szerepeltetése, és a vidéki költségmegosztás ajánlata szó szerint.

---

## 0.1 A vizuális kiindulópont — egy mondatban

> **A vizuális rendszer alapja a 4 mm-es float üveg élének zöldje** — az a szín,
> amit egy üvegtábla *csak a vágott élén* mutat meg, egyébként láthatatlan —,
> mellette a paszpartúkarton krémje és a gitt szürkéje: vagyis pontosan az a
> három anyag, amit ez a műhely nap mint nap a kezében tart.

Ez nem hangulat, hanem anyagi tény: a float üveg vas-oxid-tartalma miatt élből
nézve zöld. Az üveges ezt ismeri, a laikus meglepődik rajta — ezért jó
márkaalap: **igaz, konkrét, és a szakmán kívül senki nem használja.**

---

## 1. A jelenlegi oldal elemzése

### 1.1 Technológia és szerkezet

| Jellemző | Megállapítás | Bizonyosság |
|---|---|---|
| Protokoll | `http://` — az indexelt kanonikus URL nem HTTPS | **magas** (keresőindex) |
| Karakterkódolás | Latin-2 / Windows-1250 tartalom hibás deklarációval kiszolgálva | **magas** — bizonyítás §2.1 |
| Oldalak száma | Gyakorlatilag **egy** hosszú főoldal | **közepes-magas** (a beillesztett szöveg teljesnek látszik, a keresőben más aloldal nem jött elő) |
| Szerkezet | Bekezdésfolyam, felsorolás-szerű sortörésekkel, hierarchia nélkül | **magas** (a szöveg szerkezetéből) |
| Tartalmi duplikáció | A „Pécsett Kertvárosban megnyitottuk…" blokk **kétszer**, csaknem szó szerint | **magas** — a beillesztett szövegben látható |
| Kép/média | Ismeretlen; a szövegben egyetlen képre utaló elem sincs | **alacsony** → §15.2 |
| Űrlap | Nincs. Az egyetlen konverziós út a telefon és egy `freemail.hu` cím | **magas** |
| Strukturált adat | Nem valószínű, hogy van (a kor és a stílus alapján) | **alacsony** → §15.2 |

### 1.2 MI A JÓ BENNE — külön szedve, és ezt meg is tartom

Ez nem udvariassági szakasz. Nyolc olyan dolog van ezen az oldalon, amit a pécsi
versenytársak nagy része **nem** tud felmutatni, és amit egy „modern" újratervezés
tipikusan kidob. Egyiket sem dobom ki.

| # | Ami jó | Miért érték | Mi lesz vele az új oldalon |
|---|---|---|---|
| J1 | **Telefon-központú, egyértelmű felszólítás**: „Hívjon – jövünk – segítünk!" | A konverziós mechanika eleve helyes. Törött ablaknál senki nem tölt ki 9 mezős űrlapot. | Megmarad, sőt: `tel:` link, ragadós hívógomb, és a nyitvatartásból számolt élő állapot. §12 |
| J2 | **Névvel vállalt szolgáltatás**: „Váradi Ferenc és Váradiné, Czike Éva" | Ritka. A konkurencia többsége arctalan „Kft." — egy magánlakásba beengedett iparosnál a név bizalmi tőke. | A „Kik jövünk" szekció alapja, kiemelt helyen. §5 |
| J3 | **A vidéki költségmegosztás ajánlata** | Konkrét, szokatlan, számszerűsíthető kereskedelmi feltétel, amit sehol máshol nem láttam a pécsi mezőnyben. Ez egy valódi USP. | Önálló URL (`/videk/`) + a főoldalon szó szerint idézve. §4 |
| J4 | **Non-stop elérhetőség rendkívüli esetben**, kimondva | A legmagasabb szándékú keresés (betört kirakat éjjel) pont ezt keresi. | A `/uvegtores/` sürgősségi útvonal magja. §4 |
| J5 | **Rendkívül konkrét szakmai szókincs**: drótüveg, fazettázott, katedrál jellegű, paszpartú, polikarbonát, 1000 °C kandallóüveg, élcsiszolás, tükörfűtés | Ez long-tail SEO-arany. A generikus versenytárs-oldalak („minőségi üvegezés Pécsett") ezekre nem rangsorolnak. | **Minden egyes kifejezés megmarad**, de saját szekcióba/URL-re osztva, hogy legyen mire rangsorolni. §4, §10 |
| J5b | **Konkrét üvegeredetek**: cseh, lengyel, német, olasz, török katedrálüvegek | Választékot bizonyít elbeszélés helyett. | Megmarad, táblázatos formában. §5 |
| J6 | **Pontos cím és nyitvatartás az oldalon** | Local SEO alap, sok kisvállalkozói oldalról hiányzik. | Megmarad + `LocalBusiness` JSON-LD + `OpeningHoursSpecification`. §10 |
| J7 | **A domain maga: `pecsiuveges.hu`** | Pontos egyezés a „pécsi üveges" keresésre, régi domain, meglévő linkprofillal. | **Nem cserélni.** Migráció nélkül, ugyanazon a domainen. §14 |
| J8 | **Két üzletág egy helyen** (üvegezés + képkeretezés) | Valódi kereszt-értékesítés: aki tükröt vág, keretet is rendel. | Nem összemosom, hanem két egyenrangú belépőként kezelem. §4 |

### 1.3 Amit a jelenlegi oldal **jól csinál technikailag** — és ezt sem dobom el

Egy 2000-es évek eleji, statikus, kép nélküli HTML-oldal **valószínűleg gyors**.
Nem fogok kitalált teljesítményproblémát a szemére vetni. A baj nem a
sebessége, hanem az, hogy **használhatatlan**. A redesign kockázata épp az, hogy
egy React-es „modernizálás" elrontja azt, ami eddig jó volt: a súlytalanságot.
Ezért lett a stack az, ami (§9).

---

## 2. Problémalista — bizonyítékkal

### 2.1 KRITIKUS

**K1 — Törött karakterkódolás. Ez a legsúlyosabb hiba az oldalon.**

*Bizonyíték (szó szerint a beillesztett oldalszövegből):*

```
hõszigetelõ üvegkészítés      → helyesen: hőszigetelő
szakszerû kivitelezés         → helyesen: szakszerű
Rövid határidõk!              → helyesen: határidők
Mûanyag üvegekkel             → helyesen: Műanyag
Hõálló kerámia                → helyesen: Hőálló
erõsségünk                    → helyesen: erősségünk
hétfõtõl - péntekig           → helyesen: hétfőtől – péntekig
```

Ez a Windows-1250 (Latin-2) bájtok ISO-8859-1/2-ként való értelmezésének
klasszikus tünete: az `ő` (0xF5) `õ`-ként, az `ű` (0xFB) `û`-ként jelenik meg.
Vagyis a `<meta charset>` hiányzik vagy hibás, illetve a szerver rossz
`Content-Type` fejlécet küld.

*Következmény, és ezért kritikus:* a magyar üvegesszakma **legfontosabb
keresőkifejezései pont ezt a két betűt tartalmazzák**:
`hőszigetelő üveg`, `edzett üveg` (ez rendben), `hőálló kandallóüveg`,
`biztonsági üveg egyedi méretre`, `üvegezés rövid határidővel`.
A `hõszigetelõ` string **nem egyezik** a `hőszigetelő` lekérdezéssel. Az oldal
tehát a saját fő témájára nem rangsorolhat. Ez nem esztétikai hiba: ez az
egyetlen olyan defektus, amely önmagában megsemmisíti az organikus forgalmat.

**K2 — Nincs HTTPS.** Az indexelt kanonikus URL `http://www.pecsiuveges.hu/`.
A Chrome „Nem biztonságos" jelzést tesz a címsorba. Egy iparos oldalán, ahová
azért érkezik valaki, hogy beengedje a lakásába, ez a lehető legrosszabb első
benyomás. *(Bizonyosság: magas — keresőindex.)*

**K3 — Nincs semmilyen űrlap.** Az egyetlen digitális kapcsolatfelvételi mód egy
`freemail.hu` cím. Következmény: (a) a 17:00 után érkező látogató nem tud
nyomot hagyni; (b) nem lehet **fotót és méretet** küldeni, pedig egy üveges
árajánlatnak pont ez a két bemenete; (c) az ingyenes levelezőfiók spam-mappába
kerülhet, és rontja a szakmai megítélést.

**K4 — Telefonszám-inkonzisztencia magán az oldalon.** Ugyanaz a mobilszám két
formában szerepel: `Rádió telefon: 30 2676 709`, illetve a Google-profilban
`06 30 267 6709`. A `Rádió telefon` megnevezés 2026-ban értelmezhetetlen a
célközönség fiatalabb felének. NAP-konzisztencia (Name–Address–Phone) hiánya
közvetlenül rontja a local rangsorolást.

**K5 — Nincs egyetlen mérhető állítás sem.** Sem évszám, sem darabszám, sem
átfutási idő, sem garancia. Pedig van mivel: 4,7 csillag 66 értékelésből, és
egy 2000 óta működő műhely. Ezek az adatok **léteznek, csak nincsenek az
oldalon.**

### 2.2 UX

| # | Probléma | Bizonyíték |
|---|---|---|
| U1 | **Szövegfal, hierarchia nélkül.** ~450 szó folyamatos bekezdésekben, alcímek és vizuális tagolás nélkül. | A beillesztett szöveg szerkezete |
| U2 | **Szó szerinti duplikáció.** A „Pécsett Kertvárosban megnyitottuk…" + „Lakások, családi házak…" + „A folyamatban lévő munka után…" + „Egyedi erősségünk a képkeretezés…" blokk **kétszer** szerepel. | A beillesztett szövegben mindkét példány megtalálható |
| U3 | **Elgépelés a fő ígéretben.** „Az üvegezési, képkeretezési **problámáit** megoldjuk!" — továbbá „egyéb **mozaikképe** háttérrel" (a második előfordulásban). | Szó szerint |
| U4 | **A látogató három különböző okból érkezik, az oldal egyiket sem szolgálja ki elsőként.** (1) Betört valami, most azonnal. (2) Tervezett munka: tükörfal, hőszigetelő csere. (3) Képkeretezés. Az oldal mindhármat egyetlen, sorrend nélküli szövegtömbbe önti. | Szerkezeti elemzés |
| U5 | **Nincs folyamat-információ.** Nem derül ki, mi történik a hívás után: mikor jön ki, mennyibe kerül a felmérés, mennyi az átfutás. Ez a laikus vevő első három kérdése. | Hiány |
| U6 | **Nincs egyetlen referenciamunka sem.** Az üvegezés és a képkeretezés is **vizuális** szakma. | Hiány |
| U7 | **Mobilra nagy valószínűséggel nem alkalmas.** A Google Cégprofilon keresztül érkező forgalom túlnyomó része mobil. | **közepes** — a HTML hiányában viewport-metára nem esküszöm meg → §15.2 |
| U8 | **A képkeretezés — a saját maga által deklarált „egyedi erősség" — nem kap önálló felületet.** Egy bekezdésben van elrejtve az üvegezés közé, kétszer. | Szerkezeti |
| U9 | **Az üvegterasz, üvegkorlát, télikert, üvegtető hiányzik a saját oldalról**, miközben a daibau-profil szerint csinálja. Ezek a legmagasabb kosárértékű munkák. | daibau.hu vs. oldalszöveg összevetése · **közepes** |

### 2.3 SEO

| # | Probléma | Bizonyíték / következmény |
|---|---|---|
| S1 | A törött `ő`/`ű` miatt a fő kulcsszavak nem egyeznek. | §2.1 K1 |
| S2 | **Egy URL ~14 különböző szolgáltatásra.** Hőszigetelő üveg, drótüveg, edzett üveg, tükörfal, tükörfűtés, plexi, polikarbonát, kandallóüveg, képkeretezés, paszpartú… mind ugyanazon a címen. Egy oldal egy fő szándékra tud rangsorolni. | Szerkezeti |
| S3 | Az indexelt cím `Pécsi Üveges - képkeretezés, üveg, üvegezés, tükör ...` — vesszős kulcsszólista, a látható részben **város nélkül**, felhívás nélkül. | Keresőtalálat |
| S4 | Nincs strukturált adat → nincs esély rich resultra, és a Google nem kapja meg gépi formában a nyitvatartást, a szolgáltatásokat, a földrajzi hatókört. | **közepes** → §15.2 |
| S5 | **A 4,7 / 66 értékelés forgalmi értéke kiaknázatlan.** Ez a legerősebb meglévő eszköze, és a saját oldalán nyoma sincs. | Google-profil vs. oldalszöveg |
| S6 | Nincs vidéki/agglomerációs landing, pedig kimondottan vállal vidéki munkát — így a „üveges Pécsvárad", „üveges Kozármisleny" típusú keresésekre nincs mit felmutatni. | Oldalszöveg + a daibau `pecsvarad_7720` aloldalának léte |

### 2.4 Teljesítmény

**Nem állítok teljesítményproblémát, mert nem mértem, és a HTML-t sem láttam.**
A prior az, hogy egy kép nélküli statikus oldal **gyors**. A jelen anyag
teljesítmény-fejezete (§11) ezért nem javításról szól, hanem **megőrzésről**: a
cél az, hogy az új, jóval gazdagabb oldal *ne legyen lassabb* a réginél.
Egyetlen kockázati megállapítás van, ami a HTML nélkül is igaz:

| # | Kockázat | Indok |
|---|---|---|
| P1 | HTTP → nincs HTTP/2, nincs multiplexelés, nincs modern gyorsítótár-alku. | K2 következménye |
| P2 | Ha bekerülnek a hiányzó referenciafotók (márpedig kellenek, U6), az a mostani „gyors, mert üres" állapotot azonnal elviszi — ha nincs mellette képstratégia. | §9.3 |

---

## 3. Miért rosszak ezek — a mögöttes ok, nem a tünet

A tünetlista fenti 20 pontja **négy okra** vezethető vissza. Ha csak a tüneteket
javítjuk, három éven belül ugyanide jutunk.

### O1 — Ez nem weboldal, hanem egy szórólap HTML-be másolva

*Bizonyíték:* a szó szerinti duplikáció (U2). Egy szórólapon a hajtás két
oldalán **szándékosan** ismétlődik az ajánlat, mert az olvasó bármelyik oldalról
kezdheti. Weben ez értelmetlen — és pontosan így néz ki: a szöveg úgy áll,
ahogy egy A5-ös lapon állt.

*Következmény:* a tartalom **nem navigálható**, mert soha nem is arra készült.
Nincs benne belépőpont, nincs benne sorrend, nincs benne cselekvési pont —
mert a szórólapon a cselekvési pont maga a papír, amit a hűtőre tesznek.

*Ezért:* a megoldás nem „szebb tipográfia", hanem **az információ újratagolása
a látogató szándéka szerint** (§4).

### O2 — A tartalom sorrendje a szolgáltató fejében lévő sorrend, nem a vevőé

Az oldal így halad: ki vagyok → mit nyitottam → milyen üvegeim vannak (14 fajta)
→ mikor vagyok nyitva → mi van vészhelyzetben. A vevő fejében ez a sorrend:
**„most törött be" / „mennyibe kerül" / „megbízható-e" / „mikor jön".**

*Ezért:* a főoldal első képernyője nem bemutatkozás lesz, hanem **három ajtó a
látogató három állapotához** (§5.1).

### O3 — A karakterkódolási hiba nem hiba, hanem tünet: az oldalt évek óta senki nem nyitotta meg szerkesztésre

A `õ`/`û` akkor keletkezik, amikor egy Win-1250-es szerkesztőből mentett fájl
kerül ki deklaráció nélkül. Ez az **első** mentéskor keletkezik, és utána soha
nem javítható „véletlenül". Hogy máig ott van a `problámáit` elgépeléssel együtt,
az azt jelenti: **nincs olyan folyamat, amiben bárki ránéz erre az oldalra.**

*Ezért:* a szállítmány része egy olyan technikai alap, amit **az ügyfél maga is
tud szerkeszteni** anélkül, hogy elronthatná a kódolást (§9.1), és egy
karbantartási ritmus (§14, F4).

### O4 — A bizalom kizárólag a fizikai jelenlétből származik, digitálisan nulla

Az ügyfélnek **4,7 csillagja van 66 értékelésből** — ez a pécsi üveges mezőnyben
kiemelkedő. Ez a bizalom a Google Térképen áll, és ott is marad: a saját oldal
egyetlen bizonyítékot sem hoz át belőle. Aki a Cégprofilról a „WEBHELY" gombra
kattint, **rosszabb élménybe** érkezik, mint ahonnan jött — a listing modernebb,
mint a célpont.

*Ezért:* a redesign egyik fő feladata a **bizonyítékáthordás**: a
Cégprofil-értékelés, a nevesített személyek, a 2000 óta tartó működés és a
konkrét szakmai szókincs láthatóvá tétele az első képernyőn (§12).

---

## 4. Új információs architektúra és sitemap

### 4.1 A rendezőelv

Nem szolgáltatás szerint tagolok, hanem **a látogató érkezési állapota szerint**,
és csak a második szinten megyek át szolgáltatásra. Három állapot van (O2):

| Állapot | Lelkiállapot | Mennyi ideje van | Mit kell látnia 3 mp alatt |
|---|---|---|---|
| **A — Baj van** | stresszes, sürget, gyakran biztosítós ügy | ~10 mp | telefonszám, „most hívható-e", „mikor jön ki" |
| **B — Tervez** | mérlegel, összehasonlít, árat keres | 2–5 perc | mit tud, milyen üvegek, hogyan zajlik, mennyi idő |
| **C — Keretez** | vizuális, ízlés-döntés, nem sürgős | 3–10 perc | keretválaszték, paszpartú, példák, hogyan viszem be |

### 4.2 Sitemap URL-enkénti indoklással

```
/                                  Főoldal — a három ajtó + a „tábla" + bizonyíték
│
├── /uvegtores/                    (A) Sürgősségi: törés, kárelhárítás, non-stop
│   └── /uvegtores/biztositas/     (A) Biztosítós kárrendezés lépésről lépésre
│
├── /uvegezes/                     (B) Üvegezés — gyűjtő
│   ├── /uvegezes/hoszigetelo-uveg/
│   ├── /uvegezes/biztonsagi-uveg/
│   ├── /uvegezes/kirakat/
│   ├── /uvegezes/dísz-es-katedral-uveg/   → /uvegezes/disz-es-katedral-uveg/
│   └── /uvegezes/erkely-es-elcsiszolas/
│
├── /tukor/                        (B) Tükör — önálló üzletág, önálló keresés
│   ├── /tukor/tukorfal/
│   └── /tukor/kulonleges-tukrok/
│
├── /kepkeretezes/                 (C) Képkeretezés — a második egyenrangú üzletág
│   └── /kepkeretezes/paszpartu/
│
├── /muanyag-es-hoallo/            (B) Plexi, polikarbonát, kandallóüveg
├── /videk/                        (B) Vidéki kiszállás + a költségmegosztás
├── /arajanlat/                    Ajánlatkérő űrlap (mérettel, fotóval)
├── /rolunk/                       Váradi Ferenc és Váradiné Czike Éva, 2000 óta
└── /kapcsolat/                    Cím, nyitvatartás, térkép, parkolás
```

### 4.3 Miért pont ezek az URL-ek

| URL | Indok | Alternatíva, amit elvetettem, és miért |
|---|---|---|
| `/` | A Cégprofilról érkező forgalom itt landol; három ajtót kell nyitnia, nem elmesélnie a céget. | *Egyoldalas (one-page) megtartása:* elvetve — S2 miatt 14 szolgáltatás nem fér egy rangsorolható URL-be. |
| `/uvegtores/` | A legmagasabb szándékú keresés („betört ablak Pécs", „üveges azonnal"). Külön URL kell, mert külön hirdetési célpont és külön schema (`EmergencyService`-szerű `availableChannel`). | *`/kapcsolat/#surgos` horgony:* elvetve — horgonyra nem lehet hirdetni és nem rangsorol önállóan. |
| `/uvegtores/biztositas/` | A biztosítós ügyintézés a legfélelmetesebb rész a laikusnak, és **dokumentált erősség** (48 órás beépítés). Külön oldal, mert külön keresés: „biztosító fizeti az ablakot". | *A sürgősségi oldal egy szekciója:* elvetve — hosszú, folyamatábrás tartalom, elnyomná a hívásra ösztönzést. |
| `/uvegezes/*` | A meglévő szakmai szókincs (J5) csak akkor ér valamit, ha van hova rangsorolnia. Öt aloldal = öt kulcsszócsoport. | *Egy nagy `/szolgaltatasok/` oldal:* elvetve — ez a jelenlegi hiba nagyobb betűvel. |
| `/tukor/` **nem** `/uvegezes/tukor/` | A tükör önálló vásárlói szándék („tükör méretre vágás Pécs", „aerobik tükörfal"), és a Google-kategória is „Üveg- **és tükörbolt**". Nem alárendelt. | *Alárendelés az üvegezésnek:* elvetve — mélyebb URL, gyengébb belső linkerő, rosszabb címezhetőség. |
| `/kepkeretezes/` | Az ügyfél maga nevezi „egyedi erősségünknek". Jelenleg egy bekezdés. Ez a második üzletág, saját közönséggel (C állapot), saját szezonnal. | *Beolvasztás a főoldalba:* elvetve — U8. |
| `/kepkeretezes/paszpartu/` | A „paszpartú" önálló, alacsony versenyű, magas szándékú kifejezés. Aki ezt keresi, tudja mit akar. | — |
| `/muanyag-es-hoallo/` | A plexi/polikarbonát/kandallóüveg nem „üveg" a vevő fejében, más keresési nyelv. A kandallóüveg erősen szezonális (őszi csúcs). | *Szétbontás három URL-re:* elvetve — jelenleg nincs elég tartalom három oldalhoz; ez §14 F3 fázisban újranyitható. |
| `/videk/` | J3, a költségmegosztás. Emellett ez a horgony a környékbeli településnevekhez (Kozármisleny, Pécsvárad, Szentlőrinc, Bogád – §15-ben megerősítendő hatókör). | *Csak a főoldalon említve:* elvetve — S6. |
| `/arajanlat/` | Önálló URL kell, mert (a) hirdetési célpont, (b) köszönőoldal-mérés, (c) minden aloldalról ide mutat a másodlagos CTA. | *Csak modális űrlap:* elvetve — nem megosztható, nem mérhető, nem működik JS nélkül. |
| `/rolunk/` | O4: a bizalom áthordása. Két nevesített ember, 2000 óta. | — |
| `/kapcsolat/` | NAP-konzisztencia egyetlen kanonikus helyen, ahonnan minden katalógus másolható. | — |

**Ami tudatosan NINCS benne:** blog, hírek, galéria-aloldal, „Miért minket
válasszon" oldal, árlista-oldal. Indoklás: egy kétfős műhelynél a nem
karbantartott blog kárt okoz (O3 megismétlődik), a galéria pedig a
szolgáltatásoldalakon belül a helyén van, ahol konvertál is. Árlista-oldal csak
akkor, ha valódi árak vannak (§15 Q3) — kitalált árat nem teszek ki.

### 4.4 Navigáció

Fő navigáció, öt elem (a `bottom-nav-limit` és `overflow-menu` elv szerint a
kognitív terhelés miatt 5 a plafon):

`Üvegezés · Tükör · Képkeretezés · Vidékre is · Kapcsolat`
mellette elkülönítve: **`Hívás: 06 30 267 6709`** (elsődleges, jelzőszínű).

Az `/uvegtores/` **nem** a főmenüben van, hanem a fejléc alatti, mindig látható
**állapotsávban**: „Most nyitva 17:00-ig · Törés esetén non-stop: 06 30 267 6709".
Indok: aki bajban van, nem menüt olvas, hanem a legkontrasztosabb elemre néz.

---

## 5. Oldalankénti felépítés

### 5.1 Főoldal (`/`) — ez készül el prototípusként

| # | Szekció | Cél | Fő tartalom | CTA |
|---|---|---|---|---|
| 1 | Állapotsáv | Azonnali elérhetőség | Élő nyitva/zárva állapot a H–P 9–17-ből számolva + non-stop szám | `tel:` |
| 2 | Fejléc | Navigáció | Logó (szöveges), 5 menüpont, téma-váltó, hívógomb | `tel:` |
| 3 | **Hero + „A tábla"** | A szolgáltatás lényegének megmutatása | H1, egy mondatos ígéret, és a **méretre húzható üvegtábla** (§ Szignatúra) | Méret átvitele az űrlapba |
| 4 | Három ajtó | A látogató szétválogatása (O2) | Baj van / Tervezek / Keretezek — három kártya, mindegyik konkrét első lépéssel | 3 különböző |
| 5 | Bizonyíték-sáv | O4: bizalomáthordás | 4,7 ★ / 66 vélemény (Google-ra mutatva), 2000 óta, Nagy Imre út 29., non-stop | Google-profil |
| 6 | Mit csinálunk | J5 megőrzése rangsorolható formában | Üvegezés / Tükör / Képkeretezés / Műanyag és hőálló — 4 blokk, mindegyikben a valódi szakmai felsorolás | aloldalak |
| 7 | Hogyan zajlik | U5 | 4 lépés: hívás → helyszíni felmérés azonnali áregyeztetéssel → gyártás → beépítés | `/arajanlat/` |
| 8 | Vidékre is | J3 szó szerint | A költségmegosztás ajánlata, idézetként | `/videk/` |
| 9 | Kik jövünk | J2 | Váradi Ferenc és Váradiné Czike Éva; fotóhely fenntartva | `/rolunk/` |
| 10 | Ajánlatkérés | K3 megoldása | Akadálymentes űrlap, a táblából jövő mérettel előtöltve | küldés |
| 11 | Kapcsolat + nyitvatartás | J6 | Cím, két szám, e-mail, nyitvatartási táblázat, térképhely | útvonalterv |
| 12 | Lábléc | NAP-kanonizálás | Egységes NAP, sitemap-linkek, adatkezelés | — |

### 5.2 A többi oldal sablonjai

| Oldaltípus | Szekciósor |
|---|---|
| **Sürgősségi** (`/uvegtores/`) | Hívósáv → Mit tegyen most (3 pont: biztonság, fotó, méret) → Mit csinálunk mi → Biztosítós ügy → Rövid GYIK → Hívás |
| **Szolgáltatás-gyűjtő** (`/uvegezes/`, `/tukor/`) | H1 + egymondatos definíció → aloldal-kártyák → mikor melyiket → munkafolyamat → ajánlatkérés |
| **Szolgáltatás-levél** (`/uvegezes/hoszigetelo-uveg/`) | H1 → mire jó, laikusul → műszaki táblázat (vastagság, felépítés, mit old meg) → tipikus esetek → mit kell megadnia → ajánlatkérés |
| **Képkeretezés** | H1 → mit hozhat be → keret- és paszpartúválaszték → példahely (fotó) → átfutás → ajánlatkérés |
| **Vidék** | H1 → a költségmegosztás ajánlata → hogyan szervezze meg a szomszédokkal → hatókör-lista → hívás |
| **Rólunk** | H1 → két ember, névvel → 2000 óta → a műhely → értékelések → hívás |
| **Kapcsolat** | H1 → NAP-blokk → nyitvatartás-táblázat → térkép → megközelítés/parkolás → űrlap |

---

## 6. Wireframe-leírás (ASCII)

### 6.1 Desktop, ≥1024px — főoldal első két képernyője

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ ● Most nyitva · 17:00-ig      Törés esetén non-stop: 06 30 267 6709      [☀/☾]│ ← állapotsáv, 36px
├──────────────────────────────────────────────────────────────────────────────┤
│  VÁRADI FERENC          Üvegezés  Tükör  Képkeretezés  Vidékre is  Kapcsolat │
│  ÜVEGES · Pécs, Kertváros                              [  HÍVÁS: 30 267 6709 ]│ ← fejléc, ragadós
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌───────────────────────────────┐   ┌──────────────────────────────────┐   │
│   │                               │   │  ↕ 400 mm                        │   │
│   │  Üveg, méretre vágva.         │   │   ┌────────────────────────┐▲    │   │
│   │  Pécsett, 2000 óta.           │   │   │                        ││    │   │
│   │  ────────────────────         │   │   │   A TÁBLA              ││    │   │
│   │  Ablak, kirakat, tükör,       │   │   │   (húzható üvegtábla,  ││    │   │
│   │  hőszigetelő üveg és          │   │   │    zöld vágott éllel,  ││    │   │
│   │  képkeretezés. Helyszíni      │   │   │    fénycsíkkal)        ││    │   │
│   │  felmérés, azonnali           │   │   │                        ││    │   │
│   │  áregyeztetéssel.             │   │   └────────────────────────┘▼◄──┐│   │
│   │                               │   │   ◄────── 600 mm ──────►    ↖húzd│   │
│   │  [ Ajánlatot kérek ]  [Hívás] │   │  ├┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┤ mérce │   │
│   │                               │   │  600 × 400 mm  → [Átveszem]      │   │
│   └───────────────────────────────┘   └──────────────────────────────────┘   │
│    max 34rem szövegoszlop              a tábla: max 520×420, arányt tart     │
├──────────────────────────────────────────────────────────────────────────────┤
│  ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐      │
│  │ [!] BAJ VAN        │  │ [▭] TERVEZEK       │  │ [◱] KERETEZEK      │      │
│  │ Betört, repedt,    │  │ Hőszigetelő csere, │  │ Kép, gobelin,      │      │
│  │ kiesett.           │  │ tükörfal, kirakat. │  │ festmény, tükör.   │      │
│  │ → Hívás most       │  │ → Ajánlatot kérek  │  │ → Keretválaszték   │      │
│  └────────────────────┘  └────────────────────┘  └────────────────────┘      │
├──────────────────────────────────────────────────────────────────────────────┤
│   ★ 4,7 / 66 vélemény (Google)  │  2000 óta  │  Nagy Imre út 29.  │  Non-stop │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Mobil, 375px — ugyanaz a tartalom, más sorrend

```
┌──────────────────────────┐
│ ● Nyitva · 17:00-ig  [☾] │  36px, ragadós
├──────────────────────────┤
│ VÁRADI FERENC ÜVEGES  [≡]│  56px
├──────────────────────────┤
│                          │
│  Üveg, méretre vágva.    │  H1, clamp 36→60px
│  Pécsett, 2000 óta.      │
│                          │
│  Ablak, kirakat, tükör,  │  17px, max 60ch
│  hőszigetelő üveg és     │
│  képkeretezés.           │
│                          │
│  ┌────────────────────┐  │  ← A TÁBLA mobilon
│  │  ↕300              │  │    a szöveg ALATT,
│  │ ┌────────────┐▲    │  │    de a hajtás
│  │ │            ││    │  │    felett még
│  │ │  üvegtábla ││    │  │    belóg (affordancia)
│  │ │            ││    │  │
│  │ └────────────┘▼    │  │
│  │ ◄──── 450 ────►    │  │
│  │ 450 × 300 mm       │  │
│  │ [ Átveszem ]       │  │
│  └────────────────────┘  │
│                          │
│  ┌────────────────────┐  │
│  │ [!] BAJ VAN        │  │  egymás alatt,
│  │ Betört, repedt.    │  │  nem vízszintes
│  │ → Hívás most       │  │  görgetés
│  └────────────────────┘  │
│  ┌────────────────────┐  │
│  │ [▭] TERVEZEK       │  │
│  └────────────────────┘  │
│  ┌────────────────────┐  │
│  │ [◱] KERETEZEK      │  │
│  └────────────────────┘  │
│                          │
│  ★ 4,7 · 66 vélemény     │  a bizonyítéksáv
│  2000 óta · Kertváros    │  2 sorba tördel
│                          │
│         ⋮ (görgetés)     │
├──────────────────────────┤
│ [ 📞 HÍVÁS ] [ AJÁNLAT ] │  ← ragadós alsó sáv,
└──────────────────────────┘    56px, safe-area-inset
```

**Mobil-döntés, amit külön indokolok:** a hero-szöveg a tábla **fölé** kerül,
mert a H1-nek kell az LCP-elemnek lennie, és mert egy stresszes látogatónál a
szöveg + a hívógomb fontosabb, mint az interakció. A tábla teteje viszont még
belóg a hajtás fölé, hogy legyen affordanciája („van itt még valami").
Az alsó ragadós sáv **két** gombot tart, nem egyet: a hívás (A állapot) és az
ajánlatkérés (B/C állapot) nem ugyanaz a szándék.

### 6.3 Az ajánlatkérő űrlap wireframe-je (mindkét méret)

```
┌─ Ajánlatkérés ──────────────────────────────────────────┐
│                                                          │
│  Miben segíthetünk? *                                    │
│  ( ) Törés, sürgős   ( ) Üvegezés   ( ) Tükör            │
│  ( ) Képkeretezés    ( ) Egyéb                           │
│                                                          │
│  Név *                          Telefonszám *            │
│  ┌───────────────────────┐      ┌──────────────────────┐ │
│  │                       │      │ 06 30 …              │ │
│  └───────────────────────┘      └──────────────────────┘ │
│  ↳ hiba ide, a mező ALÁ, role="alert"                    │
│                                                          │
│  Méret (mm)          Hol van? (irányítószám)             │
│  ┌─────┐ × ┌─────┐   ┌──────────────────────┐            │
│  │ 600 │   │ 400 │   │ 7632                 │            │
│  └─────┘   └─────┘   └──────────────────────┘            │
│  ↳ „A táblából átvéve" — ha onnan jött                   │
│                                                          │
│  Leírás                                                  │
│  ┌────────────────────────────────────────────────────┐  │
│  │                                                    │  │
│  └────────────────────────────────────────────────────┘  │
│  Ha tud, írja meg az üveg vastagságát és a keret          │
│  anyagát — így pontosabb árat tudunk mondani.             │
│                                                          │
│  [ Elküldöm ]      Vagy hívjon: 06 30 267 6709           │
│                                                          │
│  ┌── aria-live="polite" ─────────────────────────────┐   │
│  │ Összefoglaló hibalista / sikerüzenet ide           │   │
│  └────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

---

## 7. Design system

### 7.1 Színtokenek

Kilenc nevesített token. Mindegyik egy **konkrét anyaghoz** kötődik a műhelyből,
nem hangulathoz. A kontrasztértékeket kiszámoltam (WCAG 2.x relatív luminancia),
nem becsültem.

| Token | Név | Light | Dark | Mire való |
|---|---|---|---|---|
| `--el` | **élzöld** — a float üveg vágott élének színe | `#14544C` | `#6FC0B2` | elsődleges: gombok, linkek, fókusz |
| `--el-mely` | **mélység** — egymásra rakott üvegtáblák | `#0B2E2A` | `#071110` | sötét felületek, lábléc, hover |
| `--el-tint` | **üvegtónus** — egyetlen tábla átnézetben | `#CFE3DE` | `#16332E` | kiemelt blokkok, idézetek |
| `--paszpartu` | **paszpartúkarton** | `#F2EEE4` | `#0C1513` | oldalháttér |
| `--papir` | **papír** — a keretbe kerülő lap | `#FCFAF5` | `#13201D` | kártya, űrlap, felület |
| `--tinta` | **tinta** | `#15201E` | `#E9E6DC` | szövegtörzs |
| `--gitt` | **gitt** — az ablakgitt meleg szürkéje | `#55605C` | `#9DA8A3` | másodlagos szöveg, ikon |
| `--gitt-vonal` | **gittvonal** | `#8C8474` | `#63776F` | űrlapmező-keret, elválasztó |
| `--jelzo` | **jelzőszalag** — a frissen beépített üvegre ragasztott figyelmeztető szalag | `#A33512` | `#F5804F` | **kizárólag** sürgősség |

#### Kontrasztarányok — kiszámolva

**Light mód** (háttér `#F2EEE4`, felület `#FCFAF5`):

| Előtér | Háttéren | Arány | Szint |
|---|---|---|---|
| `--tinta` `#15201E` | `--papir` `#FCFAF5` | **16,01 : 1** | AAA |
| `--tinta` `#15201E` | `--paszpartu` `#F2EEE4` | **14,42 : 1** | AAA |
| `--gitt` `#55605C` | `--papir` `#FCFAF5` | **6,26 : 1** | AAA (normál szöveg) |
| `--gitt` `#55605C` | `--paszpartu` `#F2EEE4` | **5,64 : 1** | AA+ |
| `--el` `#14544C` | `--papir` `#FCFAF5` | **8,38 : 1** | AAA |
| `--el` `#14544C` | `--el-tint` `#CFE3DE` | **6,53 : 1** | AAA |
| `--jelzo` `#A33512` | `--papir` `#FCFAF5` | **6,55 : 1** | AAA |
| `#FFFFFF` | `--el` `#14544C` | **8,74 : 1** | AAA |
| `#FFFFFF` | `--jelzo` `#A33512` | **6,83 : 1** | AAA |
| `--gitt-vonal` `#8C8474` | `--papir` `#FCFAF5` | **3,55 : 1** | AA (UI-komponens, ≥3:1) |
| `--el` fókuszgyűrű | `--papir` | **8,38 : 1** | ≫3:1 |

**Dark mód** (háttér `#0C1513`, felület `#13201D`):

| Előtér | Háttéren | Arány | Szint |
|---|---|---|---|
| `--tinta` `#E9E6DC` | `--paszpartu` `#0C1513` | **14,85 : 1** | AAA |
| `--tinta` `#E9E6DC` | `--papir` `#13201D` | **13,43 : 1** | AAA |
| `--gitt` `#9DA8A3` | `--paszpartu` `#0C1513` | **7,56 : 1** | AAA |
| `--gitt` `#9DA8A3` | `--papir` `#13201D` | **6,84 : 1** | AAA |
| `--el` `#6FC0B2` | `--paszpartu` `#0C1513` | **8,71 : 1** | AAA |
| `--jelzo` `#F5804F` | `--paszpartu` `#0C1513` | **7,14 : 1** | AAA |
| `#0C1513` | `--el` `#6FC0B2` | **8,71 : 1** | AAA (sötét szöveg világos gombon) |
| `--gitt-vonal` `#63776F` | `--papir` `#13201D` | **3,51 : 1** | AA (UI-komponens) |

**Döntés, amit külön indoklok:** dark módban a gombfelirat **nem fehér**, hanem
`--paszpartu` (`#0C1513`) a világosított élzöldön. A fehér szöveg világos
telített felületen kápráztat, és a `color-dark-mode` elv szerint sötét módban
nem invertálni kell, hanem tónusváltozatot használni.

### 7.2 Tipográfia

**Két variable betűcsalád, mindkettő teljes latin-ext lefedettséggel** — az
`ő` (U+0151) és `ű` (U+0171) mindkettőben megvan, ez volt a kizáró feltétel
(K1 után ez nem elhanyagolható részlet).

| Szerep | Család | Tengelyek | Licenc | Miért ez |
|---|---|---|---|---|
| Display, címsor, számok | **Archivo** | `wght 100–900`, `wdth 62–125` | OFL | Grotesque, amit eredetileg **nagyméretű, nyomtatott és táblás megjelenítésre** terveztek — ugyanaz a műfaj, mint egy műhely cégtáblája vagy egy kirakatra festett felirat. A `wdth` tengely miatt **egyetlen fájlból** kapok keskenyített feliratot a mércéhez és normál szélességet a címsorhoz — nincs második letöltés. Latin-ext teljes. |
| Szövegtörzs | **Source Serif 4** | `wght 200–900`, `opsz 8–60` | OFL | Talpas törzs, mert (a) hosszabb magyarázó szövegnél kevésbé fárasztó, (b) egy 2000 óta működő családi műhelynél „levélpapír"-hangot ad, nem startupot, (c) az `opsz` tengely miatt a 17px-es törzs és a 13px-es képaláírás **külön optikai rajzot** kap ugyanabból a fájlból. Adobe, kifogástalan latin-ext. |

**A display face minimális használati mérete.** Az Archivo `wdth < 85`
beállításban a magyar kettős ékezet (`ő`, `ű`) fölött a két vonás összezár:

- `wdth 100` (normál): **14px-től** használható.
- `wdth 88` (címsor-keskenyítés): **24px-től**.
- `wdth 75` (mérce, számok): **13px-től, de csak verzálban és számokkal** —
  ékezetes kisbetűt ilyen szélességben nem szedek.
- `wdth < 70`: **nem használom.** Nincs olyan méret, ahol a magyar ékezet
  biztonságos.

Ez nem elméleti óvatosság: pont az `ő`/`ű` az a két karakter, amivel ennek az
oldalnak eddig baja volt (K1). Nem szeretném tipográfiával megismételni azt,
amit a kódolás elrontott.

**Típusskála `clamp()`-pel** (360px → 1440px között folyamatos):

```css
--t-xs:   clamp(0.8125rem, 0.79rem + 0.11vw, 0.875rem);   /* 13 → 14 */
--t-sm:   clamp(0.875rem,  0.85rem + 0.12vw, 0.9375rem);  /* 14 → 15 */
--t-base: clamp(1rem,      0.96rem + 0.20vw, 1.125rem);   /* 16 → 18 */
--t-md:   clamp(1.125rem,  1.06rem + 0.31vw, 1.3125rem);  /* 18 → 21 */
--t-lg:   clamp(1.375rem,  1.25rem + 0.63vw, 1.75rem);    /* 22 → 28 */
--t-xl:   clamp(1.75rem,   1.50rem + 1.25vw, 2.5rem);     /* 28 → 40 */
--t-2xl:  clamp(2.25rem,   1.75rem + 2.50vw, 3.75rem);    /* 36 → 60 */
```

Sormagasság: törzs `1.6`, címsor `1.08`, mérce `1`. Sorhossz: `max-width: 62ch`
törzsre, `18ch` H1-re.

### 7.3 Térköz — 8px-alap

```css
--s1: 4px;   --s2: 8px;   --s3: 12px;  --s4: 16px;  --s5: 24px;
--s6: 32px;  --s7: 48px;  --s8: 64px;  --s9: 96px;  --s10: 128px;
```

Szekcióritmus: mobil `--s8` (64px), desktop `--s9`/`--s10`. Kártyabelső `--s5`.
Űrlapmezők közötti függőleges térköz `--s4`, csoportok között `--s6`.
Érintőcélpontok között minimum `--s2` (8px), méret minimum **48×48px**.

### 7.4 Elevation — üveglogika, nem árnyéklogika

Ez a rendszer egyik tudatos eltérése a szokásos „elevation = shadow" mintától.
Üvegnél a mélységet nem az árnyék jelzi, hanem **az él, ahol a fény megtörik**.

| Szint | Light | Dark | Hol |
|---|---|---|---|
| `e0` | nincs keret, `--paszpartu` háttér | ugyanaz | oldalalap |
| `e1` | `1px solid --gitt-vonal/40%` + `0 1px 2px rgb(21 32 30 / .06)` | `1px solid --gitt-vonal/50%` + **felső 1px élfény** `inset 0 1px 0 rgb(255 255 255 / .06)` | kártya, űrlap |
| `e2` | `0 6px 20px -12px rgb(21 32 30 / .22)` | felület egy fokkal világosabb (`#1A2926`) + élfény | ragadós fejléc, alsó sáv |
| `e3` | `0 24px 48px -24px rgb(21 32 30 / .30)` | `#1A2926` + erősebb élfény + scrim `rgb(0 0 0 / .55)` | mobil menü |

**Indoklás:** sötét módban az árnyék fizikailag láthatatlan (fekete a feketén).
A `border-and-divider-visibility` elv szerint a mélységet ott a **felület
világossága + egy 1px-es felső élfény** hordozza — ez pont az, amit egy
üvegtábla tetején lát az ember, amikor fény éri. A metafora és az akadálymentesség
itt ugyanazt kívánja.

### 7.5 Komponenslista

| Komponens | Állapotok | Megjegyzés |
|---|---|---|
| `Gomb / elsődleges` | rest, hover, active, focus-visible, disabled | 48px magas, `--el` háttér |
| `Gomb / jelző` | ugyanaz | csak hívásra és sürgősségre, oldalanként **egyszer** |
| `Gomb / másodlagos` | ugyanaz | keretes, átlátszó háttér |
| `Hívólink` | + `:visited` semleges | `tel:` séma, `aria-label`-lel kimondva a számot |
| `Állapotsáv` | nyitva / zárva / mindjárt zár | szín **és** szöveg **és** pont-ikon (nem csak szín) |
| `Ajtókártya` (A/B/C) | rest, hover, focus-within | teljes felület kattintható, de a link a címben van |
| `Bizonyítéksáv` | — | 4 elem, mobilon 2×2 |
| `Szolgáltatásblokk` | — | ikon + cím + valódi szakmai felsorolás |
| `Lépéslista` | — | számozott, mert **valódi sorrend** (§ tiltólista: számozás csak itt) |
| `Idézetblokk` | — | `--el-tint` háttér, bal oldali `--el` él |
| **`A tábla`** | rest, drag, focus, reduced-motion | §Szignatúra |
| `Mérce` | — | Archivo `wdth 75`, `tnum` |
| `Űrlapmező` | rest, focus, hiba, kitöltött, tiltott | címke **fölötte**, hiba **alatta** |
| `Rádiócsoport` | — | `fieldset`+`legend` |
| `Hibaösszefoglaló` | — | `role="alert"`, horgonyokkal a mezőkre |
| `Nyitvatartás-táblázat` | mai nap kiemelve | `<table>`, nem div |
| `Téma-váltó` | világos / sötét / rendszer | 3 állás, `aria-pressed` |
| `Mobil menü` | zárva / nyitva | `<dialog>`-szerű, fókuszcsapda, `Esc` |
| `Ragadós alsó sáv` | — | csak mobil, `env(safe-area-inset-bottom)` |

---

## 7.6 A szignatúra elem — „A tábla"

### 7.6.1 Mi ez

A hero jobb oldalán egy **valódi méretre húzható üvegtábla**. A jobb alsó
sarkában fogantyú; húzásra a tábla mérete változik, a két oldalán futó **mérce**
élőben írja ki a méretet **milliméterben**. A tábla:

- **átlátszó** — átlátszik rajta a mögötte lévő háttér,
- **csak az élén zöld** — pontosan úgy, ahogy a float üveg,
- és lassan végigfut rajta **egy fénycsík**, mert egy üvegtáblát a valóságban is
  csak a rajta megcsillanó fényről vesz észre az ember.

Alatta egy sor: **„600 × 400 mm"** és egy gomb: **„Átveszem az ajánlatkérésbe"**.

### 7.6.2 Miért pont ez

A brief azt kérte, hogy az elem **mutassa meg** a szolgáltatás lényegét, ne
elmondja. Ennek a műhelynek — mindkét üzletágának — egyetlen közös lényege van:
**minden darab a megrendelő saját méretére készül.** Nincs raktári termék, nincs
szabvány. Az ablakbetét, a kirakat, a tükörfal, a paszpartú és a keret: mind
egyedi méret, milliméterben.

Ezt eddig az oldal így mondta el: *„méretre vágva"*, *„egyedi méretre"*,
*„méretre vágott"* — háromszor, szövegben. A tábla ehelyett **a látogató kezébe
adja a mérőszalagot**. Aki egyszer meghúzta a sarkát, az megértette a
szolgáltatást, és — ez a lényeg — **már meg is adta az első adatot az
ajánlatkéréshez.** A szignatúra elem és a konverziós elem ugyanaz az elem.

A második réteg — hogy a tábla átlátszó és csak az éle látszik — az üvegezés
szakmai igazsága: **ha jól van beépítve, nem látja.** Ezt sem kell leírni, mert
a látogató a saját szemével tapasztalja: mozgatja, és közben szinte nincs is ott.

### 7.6.3 Miért nem fotón múlik

Nincs egyetlen jogtiszta fotóm sem erről a műhelyről (§15 Q1), és egy stock-fotós
üvegtábla pont az ellenkezőjét bizonyítaná annak, amit ez a vállalkozás elad
(hogy ez itt egy konkrét ember konkrét munkája). A tábla **négy `div` és néhány
CSS-gradiens** — nem kell hozzá se fotós, se jogdíj, se ügyfélvárakozás. Az első
naptól élesíthető.

### 7.6.4 Mibe kerül LCP-ben

Őszinte válasz, három részre bontva:

| Tétel | Költség | Magyarázat |
|---|---|---|
| **LCP-elem** | **0 ms** | Az LCP-jelölt a hero **H1-e** marad. A tábla háttere `linear-gradient` — a CSS-gradiens **nem LCP-jelölt** a specifikáció szerint, a benne lévő szövegek pedig kicsik. A tábla tehát nem versenyez az LCP-ért, és nem is halasztja el: ugyanabban a festési körben rajzolódik ki. |
| **Hálózat** | **0 byte extra** | Nincs kép, nincs betűtípus-extra, nincs könyvtár. |
| **JS** | **~1,6 KB** (nem tömörítve, a teljes JS-ből) | Pointer-események + `requestAnimationFrame`-mel csoportosított DOM-írás. `defer`-rel töltve, nem blokkolja a festést. |
| **CLS** | **0** | A tábla konténerének fix `aspect-ratio` és `min-height` van; a méretváltozás **kizárólag `transform: scale()` és a konténeren belüli `width/height`**, ami saját `contain: layout` blokkban van — a dokumentumfolyam nem mozdul. |
| **INP** | cél **< 100 ms** | A húzás során csak `transform` és két `textContent` frissül; nincs elrendezés-olvasás a hurokban. |
| **Kockázat** | mobil hüvelykujj | A fogantyú 48×48px tapintófelületet kap (a látható rész kisebb), `touch-action: none` csak a fogantyún. |

### 7.6.5 Akadálymentesség — enélkül nem szignatúra, hanem gimmick

- A fogantyú **fókuszálható** (`tabindex="0"`), `role="slider"`-szerű
  szemantikával: `aria-label="Tábla mérete, nyílbillentyűkkel állítható"`,
  `aria-valuetext="600 × 400 milliméter"`.
- **Nyílbillentyűk**: ±10 mm, `Shift`+nyíl ±100 mm, `Home`/`End` a szélső értékek.
- A méret **szám formájában is** ott van két `<output>` elemben, felolvasható.
- Aki nem tud vagy nem akar húzni, az ugyanazt a két számot **beírhatja az
  űrlapon** — a tábla nem az egyetlen út.
- `prefers-reduced-motion: reduce` esetén a **fénycsík megáll** (a húzás marad).

---

## 8. Animációk és mikrointerakciók

Alapelv: **minden animáció ok-okozatot fejez ki.** Egyetlen díszítő mozgás sincs
a rendszerben. Globális tokenek:

```css
--gyors:  120ms;  --alap: 200ms;  --lassu: 320ms;
--be:  cubic-bezier(.16,.84,.44,1);    /* ease-out, belépés */
--ki:  cubic-bezier(.55,.06,.68,.19);  /* ease-in, kilépés */
```

| # | Elem | Interakció | Mit fejez ki | Tulajdonság | Időzítés |
|---|---|---|---|---|---|
| A1 | **A tábla fénycsíkja** | automatikus, 7 s-onként | „ez itt üveg" — a valóságban is a csillanás árulja el | `transform: translateX()` + `opacity` | 2400 ms `linear`, 7 s szünet |
| A2 | **A tábla húzása** | pointer / nyílbillentyű | közvetlen fizikai megfelelés | `width`/`height` `contain: layout` blokkban | **0 ms** (követi az ujjat) |
| A3 | **A mérce számai** | húzás közben | visszajelzés | `textContent`, `tnum` | 0 ms, rAF-hoz igazítva |
| A4 | **„Átveszem" gomb** | kattintás | a méret **átment** az űrlapba | a mérőszám 320 ms alatt az űrlapmezőhöz „úszik", majd a mező kerete 2× felvillan | 320 ms `--be` + 2×160 ms |
| A5 | Ajtókártya (A/B/C) | hover / focus | „ez kattintható" | `translateY(-2px)` + `border-color` | 200 ms `--be` |
| A6 | Elsődleges gomb | `:active` | tapintási visszajelzés | `scale(.97)` | 120 ms |
| A7 | Szekció belépés | görgetés (IntersectionObserver) | „új gondolat kezdődik" | `opacity 0→1`, `translateY(12px→0)` | 320 ms `--be`, **elemenként 40 ms késleltetés**, maximum 4 elem |
| A8 | Állapotpont (nyitva/zárva) | betöltés + percenként | „élő adat, nem statikus felirat" | `opacity` lüktetés 2 s | csak nyitva állapotban |
| A9 | Téma-váltás | kattintás | „ugyanaz az oldal, más fény" | `background-color`, `color`, `border-color` | 200 ms — **csak az első 200 ms-ban**, utána kikapcsol, hogy a görgetés ne legyen ragacsos |
| A10 | Űrlaphiba | `blur` után | „ezt a mezőt nézd meg" | `border-color` + a hibaszöveg `height 0→auto` helyett `grid-template-rows 0fr→1fr` | 200 ms `--be` |
| A11 | Űrlap-siker | küldés után | „megkaptuk" | pipa-SVG `stroke-dashoffset` rajzolódik | 400 ms |
| A12 | Mobil menü | kattintás | térbeli folytonosság a `≡` gombtól | `translateY(-8px)+opacity` + scrim `opacity` | be 200 ms `--be`, **ki 130 ms** `--ki` (~65%) |
| A13 | Ragadós fejléc | görgetés > 80px | „elváltál a lap tetejétől" | `box-shadow` + `backdrop-filter` | 200 ms |
| A14 | Fókuszgyűrű | `:focus-visible` | — | **nincs animáció**, azonnal | 0 ms |

**`prefers-reduced-motion: reduce` esetén:** A1 megáll (a tábla marad, csak nem
csillan), A4 azonnali (a mérőszám ugrik), A5/A6/A7/A12 `transform`-jai kikapcsolnak,
`opacity`-átmenet marad 120 ms-ban, A8 lüktetés megáll (a pont marad), A11 pipa
azonnal kirajzolva. **A2 és A3 soha nem kapcsol ki** — az a funkció, nem animáció.
A14 amúgy sem animált.

---

## 9. Frontend-megvalósítás

### 9.1 Stack

**Statikus HTML + CSS + egy kis vanilla JS, build-lépéssel, de framework nélkül.**
Konkrétan: **Eleventy (11ty)** sablonok → statikus HTML, kiszolgálás CDN-ről
(Cloudflare Pages / Netlify), az űrlap egy szerver nélküli végponton keresztül.

**Indoklás:**

1. **A jelenlegi oldal legnagyobb erénye a súlytalansága** (§1.3). Egy
   React/Next.js redesign 90–200 KB JS-t hoz oda, ahol jelenleg ~0 van. Az
   üzleti tartalom **11 statikus oldal**, ami havonta legfeljebb egyszer változik.
2. **O3 a valódi kockázat**: az oldal azért romlott el, mert senki nem nyúlt
   hozzá. Egy olyan stack kell, ami **öt év múlva is buildel**. Egy 11ty +
   Markdown projekt igen; egy 2026-os Next.js-projekt 2031-ben függőségi
   pokol.
3. **A karakterkódolás soha többé**: a build minden fájlt UTF-8-ban olvas és ír,
   a kiszolgáló `Content-Type: text/html; charset=utf-8` fejlécet küld, és a
   CI-ban egy 5 soros ellenőrzés elbukik, ha `õ` vagy `û` bekerül a forrásba.
   **Ez a K1 strukturális megoldása, nem a tünet javítása.**
4. Az ügyfél szerkeszthetősége: a szolgáltatásoldalak Markdownban, a NAP-adatok
   **egyetlen `adatok.json`-ban**, ahonnan a lábléc, a JSON-LD, a
   nyitvatartás-táblázat és az állapotsáv egyaránt táplálkozik — így K4
   (telefonszám-inkonzisztencia) fizikailag nem tud újra előfordulni.

**Alternatívák, amiket elvetettem:**

| Alternatíva | Miért nem |
|---|---|
| **WordPress** | A magyar kisvállalkozói alapértelmezés. Elvetve: karbantartatlan WP a legjobb módja annak, hogy 2 éven belül feltört oldal legyen belőle — pontosan az O3 mintázat, csak nagyobb kárral. Egy kétfős műhelynek nincs, aki frissítse. |
| **Next.js / Astro islands** | Túlméretezett. 11 statikus oldalhoz nem kell hidratálás. Az Astro reális második hely lenne, de a 11ty kevesebb mozgó alkatrész. |
| **Kizárólag kézzel írt HTML, build nélkül** | Csábító (nulla függőség), de 11 oldalon a fejléc/lábléc/NAP duplikálódna — és pont a duplikáció okozta az eredeti bajt (U2). |
| **Oldalkészítő (Wix/Webnode)** | Elvetve: nem kontrollálható a JSON-LD, a betűtöltés és a CLS, és a `pecsiuveges.hu` régi linkprofilját kockáztató migráció. |

### 9.2 Betűkezelés

```
/f/archivo-var.latin-ext.woff2       ~28 KB   (wght+wdth, subset: latin + latin-ext)
/f/sourceserif4-var.latin-ext.woff2  ~34 KB   (wght+opsz, subset: latin + latin-ext)
```

- **Önhosztolás**, nem Google Fonts CDN. Indok: egy külső kapcsolat (`preconnect`
  + DNS + TLS) mobilhálózaton 150–300 ms, és a Google Fonts amúgy sem oszt meg
  gyorsítótárat domainek között 2020 óta. Nincs mit nyerni rajta.
- **Subset**: `U+0000-00FF, U+0100-017F, U+02C7, U+02D8-02DB, U+2010-2015,
  U+2018-201E, U+20AC, U+2212` — vagyis latin + latin-ext + a magyar
  idézőjelek (`„ "`) + gondolatjel + euró. Az `ő`/`ű` benne van. Cirill,
  görög, vietnámi **kivéve** — ez felezi a fájlméretet.
- `font-display: swap` — a törzsön elfogadható a FOUT. **Fallback-metrikák
  igazítva** (`size-adjust`, `ascent-override`), hogy a csere ne okozzon CLS-t:

```css
@font-face{font-family:"Archivo Fallback";src:local("Arial");
  size-adjust:97%;ascent-override:92%;descent-override:24%;line-gap-override:0%}
```

- `<link rel="preload" as="font" type="font/woff2" crossorigin>` **csak a
  két variable fájlra** — semmi másra (a `font-preload` túlhasználat elv).
- **A prototípus szándékosan nem tölt le betűt.** Rendszerbetűkkel fut
  (`system-ui`, `Georgia`), és a fenti `@font-face` blokk kommentben van benne.
  Így a demó offline is azonos, és az „azonnal megnyitható" követelmény teljesül.

### 9.3 Képek

Fotó jelenleg **nincs** (§15 Q1). A prototípus **helyet tart** nekik, nem tölt ki
stockkal. Éles specifikáció:

- Formátum: **AVIF** elsődleges, **WebP** fallback, `<picture>`-rel.
- `srcset` 4 lépcsőben: 480 / 768 / 1200 / 1800 px, `sizes` a tényleges
  elrendezés szerint.
- **Minden `<img>`-en kötelező `width` + `height`** → CLS 0. A prototípusban
  ezt `aspect-ratio` box helyettesíti.
- A hajtás alatt `loading="lazy" decoding="async"`. A hajtás fölött **nincs**
  lazy (ott amúgy sincs kép — a hero szöveg + a tábla).
- Költségvetés: **oldalanként legfeljebb 250 KB kép összesen**.
- Amit fotózni kell: a műhely bejárata, a keretminta-fal, egy beépítés közbeni
  kép, egy elkészült tükörfal, és **a két ember** (J2 miatt ez a legfontosabb).

### 9.4 Gyorsítótár

| Erőforrás | Fejléc |
|---|---|
| HTML | `Cache-Control: public, max-age=0, s-maxage=600, stale-while-revalidate=86400` |
| CSS/JS (hash-elt névvel) | `public, max-age=31536000, immutable` |
| WOFF2 (hash-elt) | `public, max-age=31536000, immutable` |
| Képek (hash-elt) | `public, max-age=31536000, immutable` |
| Mindenhol | `Content-Type: …; charset=utf-8` — **K1 ellen szerveroldalról is** |

Továbbá: HTTPS + HSTS (K2), `301` a `http://` és a `www` nélküli változatról a
kanonikusra, HTTP/2 vagy /3.

### 9.5 Az űrlap

- **Progresszív**: sima `<form method="post" action="/arajanlat/koszonjuk/">`,
  ami **JS nélkül is elküldhető**. A JS csak inline validációt és `fetch`-es
  küldést ad hozzá.
- Végpont: szerver nélküli függvény (Cloudflare Worker / Netlify Function), ami
  **e-mailt küld egy saját domainnevű postafiókba** (`ajanlat@pecsiuveges.hu`) —
  nem `freemail.hu`-ra (K3). SPF + DKIM + DMARC beállítva.
- **Mézesbödön** (`honeypot`) mező + időbélyeg-ellenőrzés spam ellen. Nem CAPTCHA:
  egy 66 értékeléses helyi üvegesnél a CAPTCHA több valódi ajánlatkérést öl meg,
  mint amennyi spamot kiszűr, és akadálymentességi kockázat.
- Fotófeltöltés: `<input type="file" accept="image/*" capture="environment">` —
  mobilon azonnal a kamerát nyitja. **Ez az egyik legnagyobb gyakorlati nyereség**:
  egy törött ablakról készült fotó + egy méret gyakran elég a pontos árhoz.
- Adatkezelés: a beküldött adat célja, megőrzési ideje és jogalapja a mező
  mellett egy sorban, nem külön oldalon elrejtve.

---

## 10. SEO-specifikáció

### 10.1 Title és meta minták

Minta: `{Szolgáltatás} {Város} – {Konkrét megkülönböztető} | Váradi Ferenc Üveges`
Maximum ~60 karakter a levágás előtt, a **város a látható részben** (S3 javítása).

| URL | `<title>` | `<meta name="description">` |
|---|---|---|
| `/` | `Üveges Pécs – üvegezés, tükör, képkeretezés \| Váradi Ferenc` | `Ablak, kirakat, hőszigetelő üveg, tükör méretre vágva és képkeretezés Pécsett, Kertvárosban. Helyszíni felmérés azonnali áregyeztetéssel. Hívjon: 06 30 267 6709.` |
| `/uvegtores/` | `Betört ablak, kirakat? Üveges Pécsett – non-stop hívható` | `Törés, kiesett üveg, kirakatkár Pécsett és környékén. Rendkívüli esetben non-stop elérhető. Ideiglenes lezárás, felmérés, csere.` |
| `/uvegezes/hoszigetelo-uveg/` | `Hőszigetelő üveg csere Pécs – méretre gyártva \| Váradi Üveges` | `Hőszigetelő üvegezés és üvegcsere Pécsett: felmérés, méretre gyártás, beépítés. Fa, műanyag és fém nyílászáróhoz egyaránt.` |
| `/tukor/tukorfal/` | `Tükörfal készítés Pécs – aerobik és edzőtermi tükör` | `Élcsiszolt, fazettázott tükörfalak sportoláshoz és testmozgáshoz, méretre. Beépítés, tükörcsempézés, tükörfűtés Pécsett.` |
| `/kepkeretezes/` | `Képkeretezés Pécs – nagy keretválaszték, paszpartú` | `Kép, gobelin, festmény keretezése Pécsett, Kertvárosban. Nagy keretválaszték, paszpartú és mozaikkép-háttér. Gyors, szakszerű munka.` |
| `/videk/` | `Üveges vidékre is – megosztott kiszállási költség \| Pécs` | `Vidéki üvegezést is vállalunk. Ha a szomszédokkal vagy a rokonsággal egyeztet, a kiszállási költség megoszlik a megrendelők között.` |

**Ami a jelenlegi címhez képest változik:** eltűnik a vesszős kulcsszólista, és
minden cím egyetlen szándékot céloz. A `Pécs` minden címben szerepel — a
jelenlegi indexelt címben (`Pécsi Üveges - képkeretezés, üveg, üvegezés, tükör ...`)
a város csak a márkanév részeként van benne, a szolgáltatáshoz nem kötve.

### 10.2 Heading-hierarchia (főoldal)

```
h1  Üveg, méretre vágva. Pécsett, 2000 óta.        ← EGYETLEN h1
├── h2  Miben segíthetünk?                          (három ajtó)
│   ├── h3  Betört, repedt, kiesett
│   ├── h3  Tervezett munka
│   └── h3  Képkeretezés
├── h2  Amit csinálunk
│   ├── h3  Üvegezés
│   ├── h3  Tükör
│   ├── h3  Képkeretezés
│   └── h3  Műanyag és hőálló üvegek
├── h2  Hogyan zajlik
├── h2  Vidékre is kimegyünk
├── h2  Kik jövünk
├── h2  Kérjen ajánlatot
│   └── h3  (fieldset legendák nem headingek)
└── h2  Elérhetőség és nyitvatartás
    ├── h3  Cím és telefon
    └── h3  Nyitvatartás
```

Szintugrás nincs. A bizonyítéksáv és az állapotsáv **szándékosan nem kap
headinget** — nem tartalomszakaszok, hanem kiegészítő adatok (`role="note"` /
`aria-label`).

### 10.3 Strukturált adat — a teljes JSON-LD gráf

Egyetlen `@graph` a főoldalon, egymásra hivatkozó `@id`-kkal:

| Típus | `@id` | Miért kell |
|---|---|---|
| `WebSite` | `#website` | `name`, `inLanguage: hu-HU`, `publisher` |
| `WebPage` | `#webpage` | oldalanként, `breadcrumb`, `primaryImageOfPage` |
| `BreadcrumbList` | `#breadcrumb` | aloldalakon; a főoldalon elhagyva |
| `LocalBusiness` + `HomeAndConstructionBusiness` | `#uzlet` | **a gráf magja** — lásd alább |
| `Person` (Váradi Ferenc) | `#varadiferenc` | `founder` / `employee`; J2 gépi megfelelője |
| `Person` (Váradiné Czike Éva) | `#czikeeva` | `employee` |
| `PostalAddress` | `#cim` | Nagy Imre út 29., 7632 Pécs, HU |
| `GeoCoordinates` | `#geo` | **§15 Q6 — pontos koordináta megerősítendő**, nem találom ki |
| `OpeningHoursSpecification` ×2 | — | (1) `Mo–Fr 09:00–17:00`; (2) a non-stop sürgősségi elérhetőség **nem** nyitvatartás, hanem `ContactPoint` |
| `ContactPoint` ×2 | `#telefon`, `#surgos` | `contactType: "customer service"` ill. `"emergency"`, `availableLanguage: hu`, `hoursAvailable` |
| `Service` ×6 | `#szolg-uvegezes` stb. | üvegezés, tükör, képkeretezés, hőszigetelő, biztonsági üveg, műanyag/hőálló |
| `OfferCatalog` | `#kinalat` | a `Service`-eket fogja össze, `itemListElement`-tel |
| `GeoCircle` / `areaServed` | `#hatokor` | Pécs + a vállalt vidéki hatókör (**§15 Q4: hány km?**) |
| `FAQPage` | `#gyik` | a `/uvegtores/` és a szolgáltatásoldalak GYIK-jei; a főoldalon nem |
| `ImageObject` | `#logo` | ha lesz logó (§15 Q2) |

**A `LocalBusiness` magja (kivonat):**

```json
{
  "@type": ["LocalBusiness","HomeAndConstructionBusiness"],
  "@id": "https://www.pecsiuveges.hu/#uzlet",
  "name": "Váradi Ferenc Üveges",
  "url": "https://www.pecsiuveges.hu/",
  "telephone": "+36302676709",
  "email": "ajanlat@pecsiuveges.hu",
  "address": {"@id":"…#cim"},
  "openingHoursSpecification": [{
    "@type":"OpeningHoursSpecification",
    "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens":"09:00","closes":"17:00"
  }],
  "priceRange": "[MEGERŐSÍTENDŐ — §15 Q3]",
  "foundingDate": "[MEGERŐSÍTENDŐ — a daibau szerint 2000, §15 Q5]"
}
```

**Amit tudatosan KIHAGYOK a gráfból, és ezt indoklom:**

> **`aggregateRating` — nem kerül bele.** Kézenfekvő lenne kiírni a 4,7 / 66-ot
> strukturált adatként, hiszen ez a legerősebb bizonyíték. A Google
> keresési-értékelés irányelve viszont a `LocalBusiness` és `Organization`
> típusnál **tiltja az önmagáról szóló (self-serving) értékelés jelölését** —
> vagyis azt, hogy a vállalkozás a saját oldalán a saját magáról szóló
> értékelést jelölje. Ennek kockázata kézi büntetés a strukturált adatra, ami
> **több kárt okoz, mint amennyi hasznot a csillag hozna.**
>
> *Amit helyette csinálok:* az értékelés **vizuálisan** ott van az első
> képernyőn, és **hivatkozásként a Google Cégprofilra mutat**, ahol ellenőrizhető.
> A csillagok a találati listában a Cégprofilon keresztül amúgy is megjelennek —
> ott, ahol jogszerűen a helyük van.
>
> *(Bizonyosság: a szabály léte magas; a pontos megfogalmazás változhat —
> élesítés előtt a Google aktuális „Review snippet" dokumentációja ellenőrizendő.)*

### 10.4 Local SEO

**A legnagyobb egyszeri nyereség itt van, nem a saját oldalon.** A 66 értékelés
és a 4,7 csillag már megvan; a Cégprofil kihasználatlan.

| # | Teendő | Miért |
|---|---|---|
| L1 | **NAP-kanonizálás.** Egyetlen írásmód mindenhol: `Váradi Ferenc Üveges` / `7632 Pécs, Nagy Imre út 29.` / `+36 30 267 6709` és `+36 72 321 316`. A „Rádió telefon" megnevezés törlendő. | K4. A local rangsorolás a citációk egyezésén áll. |
| L2 | Frissítés a talált katalógusokban: `uzleti.hu`, `cylex.hu`, `yoys.hu`, `szakkatalogus.hu`, `daibau.hu`, `joszaki.hu`, `bonumventus.hu` | ugyanaz |
| L3 | **Cégprofil-szolgáltatások feltöltése** a valódi szakmai szókinccsel (drótüveg, fazettázott tükör, paszpartú, kandallóüveg…) | J5 — a Cégprofil szolgáltatáslistája is rangsorolási jel |
| L4 | **Fotók a Cégprofilra**, havi ütemben | a fotózott profilok mérhetően több útvonaltervet kapnak |
| L5 | **Kérdések és válaszok** feltöltése a profilra: „Kijönnek felmérni?", „Biztosítós kárt intéznek?", „Vidékre is jönnek?" | ezek a valós kérdések, és a válaszok a profilon jelennek meg |
| L6 | **Értékeléskérés folyamattá tétele**: minden befejezett munka után egy rövid link | 66-ról feljebb; a friss értékelések súlyozottak |
| L7 | `/videk/` + településnév-említések a valódi hatókörben (§15 Q4) | S6 |
| L8 | A weboldal → Cégprofil és Cégprofil → weboldal **kölcsönös** hivatkozása, UTM-mel a mérhetőségért | a forgalmi forrás jelenleg nem mérhető |

**Amit NEM javaslok:** külön landing oldal minden környékbeli településre
(„üveges Kozármisleny", „üveges Bogád" …) ugyanazzal a szöveggel. Ez doorway-oldal,
a Google bünteti, és egy kétfős műhely nem tudja valódi tartalommal feltölteni.
Egyetlen, tisztességes `/videk/` oldal a valós hatókörrel többet ér.

---

## 11. Teljesítménycélok

Mérési feltétel: **Moto G4-osztályú mobil, 4G lassítás (Lighthouse mobil profil)**,
hidegindítás, `/` és `/uvegezes/hoszigetelo-uveg/` mérve.

| Metrika | Cél | Küszöb, ami alatt hibának tekintem | Hogyan érem el |
|---|---|---|---|
| **LCP** | **≤ 1,2 s** | 2,0 s | Az LCP-elem a hero **H1 szövege**. Nincs hero kép, nincs render-blokkoló külső CSS, a kritikus CSS inline. Betű `swap` + metrikaigazított fallback. |
| **CLS** | **≤ 0,02** | 0,05 | Minden képnek `width`/`height`; a tábla `contain: layout`; a betűcsere metrikaigazított; az állapotsáv fix magasságú (nem tolja le a fejlécet, amikor betölt az élő adat). |
| **INP** | **≤ 120 ms** | 200 ms | A húzás rAF-fal csoportosított, nincs layout-olvasás a hurokban; nincs harmadik féltől származó szkript. |
| **TTFB** | ≤ 200 ms | 600 ms | statikus fájl CDN-ről, `s-maxage` |
| **FCP** | ≤ 0,9 s | — | inline kritikus CSS |
| **TBT** | ≤ 50 ms | 200 ms | a teljes JS `defer`, nincs framework |

**Byte-költségvetés oldalanként (tömörítve):**

| Erőforrás | Költségvetés | Megjegyzés |
|---|---|---|
| HTML | **≤ 16 KB** | benne az inline kritikus CSS és a JSON-LD |
| CSS (külső, hash-elt) | ≤ 12 KB | a hajtás alatti rész |
| JS | **≤ 8 KB** | a teljes oldal minden interakciója |
| Betűk | ≤ 62 KB | 2 × variable woff2, latin+latin-ext subset |
| Képek | ≤ 250 KB | ha lesznek (§15 Q1) |
| **Összes, első betöltés** | **≤ 350 KB** | fotókkal együtt |
| **Harmadik fél** | **0 byte** | nincs analitika-tag, nincs betűtípus-CDN, nincs chat-widget, nincs cookie-banner (mert nincs mit bejelenteni) |

**A prototípus MÉRT számai** (nem becslés — a fájlon lefuttatva):

| Tétel | Érték |
|---|---|
| Letöltendő külső erőforrás | **0 db** (nincs kép, betű, könyvtár, tag) |
| JS kód, kommentek nélkül | **9,68 KB** — a brief ≤10 KB-os keretén belül |
| JS forrás, kommentekkel együtt | 13,2 KB — a kommentek élesben nem kerülnek ki |
| JS gzip | **3,88 KB** — ennyi megy át a hálózaton |
| Teljes HTML gzip (CSS + JSON-LD + JS együtt) | **24,1 KB** |
| Vízszintes görgetés 375 / 768 / 1024 / 1280 px-en | nincs (mérve) |
| Konzolhiba / JS-kivétel | nincs (mérve) |
| Valódi kontraszthiba light + dark módban | **0** (a renderelt színekből számolva, alfa-kompozitálással) |

*A méréseket headless Chromiumban futtattam a kész fájlon; a kontrasztaudit a
tényleges számított színeket olvassa vissza a DOM-ból, nem a tervezett értékeket.*

**Mérési ritmus:** havi Lighthouse + a Search Console Core Web Vitals riportja.
Ha három hónapig zöld, negyedévesre ritkítható.

---

## 12. CRO — konverziós elemek

Kiindulás: **a jelenlegi oldalon egy konverziós elem van** (egy telefonszám
szövegként), és az is csak 9 és 17 óra között működik.

| # | Elem | Hol | Miért működik — a mögöttes mechanizmus |
|---|---|---|---|
| C1 | **Élő nyitvatartási állapot** („Most nyitva · 17:00-ig" / „Zárva · nyitás P 9:00") | állapotsáv, minden oldalon | A telefonálás előtti legnagyobb súrlódás a bizonytalanság, hogy *felveszi-e valaki*. A statikus „H–P 9–17" felirat ezt nem oldja fel — a látogatónak fejben kell számolnia. A kiszámolt állapot **átveszi ezt a munkát**. Zárás után nem tiltja a hívást, hanem átirányítja a figyelmet az űrlapra és a non-stop számra. |
| C2 | **`tel:` hívógomb, jelzőszínnel, oldalanként egyszer** | fejléc + mobil alsó sáv | Egy elsődleges CTA per képernyő (`primary-action`). Ha minden gomb kiabál, egyik sem hallatszik. A jelzőszín itt **kizárólag** a sürgősséget jelenti — így megőrzi a jelzésértékét. |
| C3 | **A tábla → „Átveszem" gomb** | hero | Elköteleződési lépcső (foot-in-the-door): a látogató **már megadott egy adatot**, mielőtt űrlapot látott volna. A megkezdett feladatot nehezebb elhagyni, mint egy üres űrlapot elkezdeni. Ez a szignatúra elem és a konverzió találkozása. |
| C4 | **Három ajtó (A/B/C)** | hajtás alatt közvetlenül | A látogató nem „üvegest keres", hanem **egy konkrét bajt akar megoldani**. Aki magára ismer az egyik kártyában, az elköteleződik az útvonal mellett. Ez a §3/O2 közvetlen javítása. |
| C5 | **4,7 ★ / 66 vélemény, a Google-profilra mutatva** | bizonyítéksáv, első képernyő alja | Társas bizonyíték, **ellenőrizhető forrással**. Az ellenőrizhetőség itt fontosabb, mint a szám: egy kattintással látja, hogy nem az oldal állítja magáról. |
| C6 | **Névvel vállalt szolgáltatás** (két ember, fotóval) | „Kik jövünk" | A lakásba beengedett iparosnál a fő kockázat érzelmi, nem anyagi. Az arc és a név ezt csökkenti. J2 kiaknázása. |
| C7 | **„Hogyan zajlik" négy lépés** | a szolgáltatások után | Bizonytalanság-csökkentés (U5). Aki tudja, mi következik, hamarabb indítja el. A negyedik lépés kimondja azt is, ami **nem** történik: „a felmérés nem kötelezettség". |
| C8 | **Méret + fotó az űrlapon** | ajánlatkérés | Az üvegesnek pont ez a két bemenet kell az árhoz. Ha megkapja, **azonnal** tud árat mondani — ez pedig a dokumentált erősség („órákon belül árajánlat"). A gyors válasz maga a konverziós tényező. |
| C9 | **A vidéki költségmegosztás, szó szerint idézve** | önálló szekció | Konkrét pénzügyi ajánlat, ami **az ügyfél saját szavaival** van megfogalmazva. Az ilyen mondat hihetőbb, mint bármilyen újraírt marketingváltozat. Ezért nem írom át. |
| C10 | **Sürgősségi útvonal a nyitvatartáson kívül** | állapotsáv + `/uvegtores/` | 17:00 után a legmagasabb szándékú látogató érkezik (most történt a baj). Jelenleg pont ekkor van a legkevesebb kapaszkodója. |
| C11 | **Ragadós alsó sáv mobilon, két gombbal** | mobil | A hívás (A) és az ajánlatkérés (B/C) nem ugyanaz a szándék; egy gomb az egyik felét elveszíti. 56px magas, `safe-area-inset` figyelembe véve. |
| C12 | **Nulla akadály**: nincs cookie-banner, nincs chat-widget, nincs hírlevél-popup | mindenhol | Minden megszakítás konverziót visz. Mivel nincs harmadik féltől származó szkript, **nincs is mit bejelenteni** — ez egyszerre jogi és konverziós előny. |

**Mérés (harmadik fél nélkül):** a `tel:` kattintás, az „Átveszem" gomb és az
űrlapküldés egy saját, cookie nélküli végpontra küld eseményt (Cloudflare Web
Analytics vagy egy 1 KB-os saját beacon). Nincs személyes adat, nincs profilozás.

---

## 13. Minden fontos design-döntés — összefoglaló táblázat

Minden sorban ott az **alternatíva**, amit elvetettem, és hogy miért.

| # | Döntés | Miért ez | Az alternatíva, amit elvetettem | Miért nem az |
|---|---|---|---|---|
| D1 | **Vizuális alap: a float üveg élének zöldje + paszpartúkarton + gitt** | Anyagi tény a műhelyből; a szakmán kívül senki nem használja; igaz és ellenőrizhető | „Bizalmi kék", ami minden iparos-oldal alapértelmezése | Megkülönböztethetetlen. A pécsi mezőny (`pecsiuvegmester.hu`, `uvegker.hu`, `ÜVEGKOVÁCS`) pontosan ebben a sávban mozog. |
| D2 | **A jelzőszín a beépített üvegre ragasztott figyelmeztető szalag narancsa, és csak sürgősségre** | A szín jelentése a szakmából jön, nem a design-divatból; és mert egyetlen helyen használom, megőrzi a jelzésértékét | Neonzöld/cinóber akcent fekete alapon | A brief kifejezetten tiltja, és okkal: ez a 2024–26-os alapértelmezett AI-esztétika. Egy 2000 óta működő üvegesműhelyhez nincs köze. |
| D3 | **Archivo + Source Serif 4** | Két variable család, teljes latin-ext (`ő`, `ű`); a `wdth` tengely egy fájlból ad cégtábla-feliratot és mércét; az `opsz` tengely külön optikai rajzot ad a 17px-es törzsnek és a 13px-es képaláírásnak | Playfair Display + Inter | A brief tiltja, és jogosan: ez a legelnyűttebb páros. Ráadásul a Playfair vékony vonásai 16px alatt a magyar ékezeteknél összeesnek. |
| D3b | ugyanaz | — | Amatic SC + Cabin (a design-system-generátor javaslata „craft/handmade" kulcsszavakra) | **A generátor javaslatát elvetettem.** Az Amatic SC kézírásos display face, ami (a) 20px alatt olvashatatlan, (b) latin-ext lefedettsége nem megbízható a magyar kettős ékezetre, (c) „kézműves kávézó" konnotációt hoz egy olyan szakmához, ahol a milliméteres pontosság az érték. |
| D4 | **Talpas szövegtörzs** | Egy 2000 óta működő családi műhelyhez levélpapír-hang illik; hosszabb magyarázó szövegnél kevésbé fárasztó | Sans törzs mindenhol | Semlegesebb, de a display-től nem különül el; a két grotesque egymás mellett „elmosódik" |
| D5 | **Elevation = üvegél, nem árnyék** (sötét módban felület-világosság + 1px élfény) | Sötétben az árnyék fizikailag láthatatlan; a metafora és az akadálymentesség itt ugyanazt kívánja | Ugyanaz az árnyékskála mindkét módban | Sötét módban a kártyák elolvadnak a háttérben; ez a leggyakoribb dark-mode hiba |
| D6 | **Szignatúra: méretre húzható üvegtábla** | Megmutatja mindkét üzletág közös lényegét (minden darab egyedi méret), közben adatot gyűjt az ajánlatkéréshez | Törésanimáció a heroban („kattints, és reped az üveg") | Látványos, de a **problémát** mutatja, nem a szolgáltatást; egy stresszes látogatónál ízléstelen; és semmilyen adatot nem gyűjt |
| D6b | ugyanaz | — | Előtte/utána képcsúszka | Fotófüggő (nincs fotó), és a legelcsépeltebb iparos-oldal elem |
| D7 | **Az IA a látogató állapota szerint tagol, nem szolgáltatás szerint** | A látogató nem „üvegest keres", hanem egy bajt akar megoldani (§3/O2) | Klasszikus szolgáltatás-menü a főoldalon | Ez a jelenlegi hiba, csak rendezettebben. A szolgáltatás-tagolás a második szinten megvan. |
| D8 | **11ty statikus generálás, framework nélkül** | Megőrzi a régi oldal egyetlen erényét (súlytalanság), és **öt év múlva is buildel** | WordPress / Next.js | WP: karbantartás nélkül biztonsági kockázat — pont az O3 mintázat. Next: túlméretezett 11 statikus oldalhoz. |
| D9 | **Nincs `aggregateRating` a JSON-LD-ben** | A Google tiltja az önmagáról szóló értékelés jelölését `LocalBusiness`-nél; a kézi büntetés kockázata nagyobb a nyereségnél | Kiírni a 4,7 / 66-ot strukturált adatként | Rövid távon csillag a találatban, hosszú távon kockázat. A csillag a Cégprofilon keresztül amúgy is megjelenik. |
| D10 | **A vidéki költségmegosztás szó szerint idézve** | Az ügyfél saját mondata hihetőbb, mint bármely újraírt változat; ez valódi USP (J3) | Marketinges újrafogalmazás („Rugalmas kiszállási feltételek") | Elveszne a konkrétum, ami az egészet érdekessé teszi |
| D11 | **Nincs cookie-banner, nincs chat-widget, nincs analitika-tag** | Nincs harmadik féltől származó szkript → nincs mit bejelenteni; minden megszakítás konverziót visz | GA4 + cookie-banner | 45+ KB JS, egy megszakítás a legfontosabb pillanatban, és jogi felület a semmiért |
| D12 | **A prototípus nem tölt le betűt, és nem tesz bele fotót** | Offline is azonos, azonnal megnyitható, és nem hazudik fotóval, ami nem az ügyfélé | Google Fonts + stock-fotók a demóhoz | A stock-fotó pont azt rombolja, amit ez a vállalkozás elad; a betű-CDN pedig külső függőség |
| D13 | **Számozás csak a „Hogyan zajlik" lépéseinél** | Ott valódi sorrend van | 01 / 02 / 03 a szolgáltatásoknál | A brief tiltja, és jogosan: hamis sorrendet sugall ott, ahol nincs |
| D14 | **Kézzel rajzolt inline SVG ikonok, egységes 1,5px vonással** | Egy vonalvastagság, egy sarokrádiusz, téma-követő `currentColor` | Emoji ikonok / ikonkészlet-CDN | Az emoji platformfüggő és nem tokenizálható; a CDN külső függőség |
| D15 | **A sürgősségi útvonal nincs a főmenüben, hanem az állapotsávban** | Aki bajban van, nem menüt olvas, hanem a legkontrasztosabb elemre néz | Hatodik menüpont: „Vészhelyzet" | Felhígítja az ötelemű menüt, és pont a legrosszabb pillanatban kényszerít keresésre |
| D16 | **Mobilon a hero szöveg a tábla fölött** | Az LCP-elemnek a H1-nek kell lennie; stresszes látogatónál a szöveg + hívógomb fontosabb az interakciónál | Tábla legfelül, „wow-hatás" | Az LCP-t egy interaktív elemre bízni kockázat, és a sürgős látogatót elveszítjük |
| D17 | **Két gomb a mobil alsó sávban** | A hívás (A állapot) és az ajánlatkérés (B/C) különböző szándék | Egy nagy hívógomb | A látogatók egyharmadát (képkeretezés, tervezett munka) rossz útra tereli |

---

## 14. Bevezetési ütemterv

Fázisokra bontva, mindegyik önmagában is értéket ad — ha bármelyik után leáll a
projekt, az addigi állapot jobb, mint a mai.

### F0 — Vérzéscsillapítás (0–3 nap, a redesigntól függetlenül)

**Ez a legjobb megtérülésű munka az egész anyagban, és nem kell hozzá új oldal.**

| Teendő | Miért most |
|---|---|
| `<meta charset="utf-8">` + szerveroldali `Content-Type` javítása a **meglévő** oldalon, és a szöveg újramentése UTF-8-ban | K1 — a fő kulcsszavak azonnal egyeznek |
| HTTPS-tanúsítvány + `301` átirányítás | K2 — megszűnik a „Nem biztonságos" jelzés |
| `<meta name="viewport">` ellenőrzése/pótlása | U7 |
| A telefonszámok `tel:` linkké alakítása | mobilon egy kattintás |
| Az elgépelések javítása (`problámáit`, `mozaikképe`) és a duplikált blokk törlése | U2, U3 |
| Google Cégprofil: szolgáltatáslista + fotók + Q&A feltöltése | L3–L5 — a forgalom nagyobb része itt jár |

### F1 — Az új főoldal (2–3 hét)

Design system, prototípus élesítése, a tábla, az űrlap végponttal, JSON-LD,
`/kapcsolat/`, `/rolunk/`. A régi tartalom megmarad egy `/regi/` archívumban,
amíg a szolgáltatásoldalak el nem készülnek — hogy egyetlen kulcsszó se essen ki.

### F2 — Szolgáltatásoldalak (3–5 hét)

`/uvegtores/`, `/uvegezes/*` (5 db), `/tukor/*` (3 db), `/kepkeretezes/*` (2 db),
`/muanyag-es-hoallo/`, `/videk/`. Belső linkhálózat, `BreadcrumbList`, GYIK-ek.
**Itt kerül vissza a helyére a J5 szakmai szókincs.** A `/regi/` archívum
lezárása, `301`-ekkel.

### F3 — Bizonyíték (párhuzamosan, az ügyféltől függ)

Fotózás (§15 Q1): a két ember, a műhely, a keretminta-fal, 4–6 referenciamunka.
Amíg nincs fotó, a helyek fenntartva maradnak — **nem töltjük ki stockkal.**
Ide tartozik a `/uvegtores/biztositas/` folyamatábra is, ha a dokumentált
48 órás átfutás megerősíthető (§15 Q7).

### F4 — Karbantartási ritmus (folyamatos) — ez a legfontosabb fázis

O3 azt mondja: az oldal nem attól romlott el, hogy rossz volt, hanem hogy senki
nem nézett rá. Ezért a szállítmány része:

- **Negyedéves 30 perces ellenőrzőlista** (linkek, nyitvatartás, telefonszám,
  Search Console hibák, Core Web Vitals).
- **CI-ellenőrzés**, ami elbukik, ha `õ` vagy `û` bekerül a forrásba (K1 soha többé).
- **Havi Cégprofil-fotó** — egy telefonos kép egy elkészült munkáról.
- Egy oldalankénti „utoljára ellenőrizve" dátum a build-idejéből, ami láthatóvá
  teszi az elavulást.

---

## 15. Nyitott kérdések — ehhez ügyfél-input kell

### 15.1 Amit meg kell kérdezni, mielőtt ez élesíthető

| # | Kérdés | Mi múlik rajta |
|---|---|---|
| **Q1** | Van fotó a műhelyről, a két emberről, elkészült munkákról? Lehet újat készíteni? | U6, C6, F3. A prototípusban 6 fenntartott képhely van. **Enélkül a bizalomépítés fele hiányzik.** |
| **Q2** | Van logó, cégtábla, bármilyen meglévő arculati elem, amit meg kell tartani? | A brief „nem változtatható" mezője üres maradt. A prototípus szöveges logót használ. |
| **Q3** | Mondható-e bármilyen ár- vagy ártartomány? Kirakatüveg m²-ár, keretezés kiindulóár, kiszállási díj Pécsen belül? | C7, C8, a `priceRange` a JSON-LD-ben, és egy esetleges `/arak/` oldal. **Árat nem találtam ki sehol.** |
| **Q4** | Meddig megy ki vidékre? Konkrét településnevek vagy km-sugár? | `/videk/`, `areaServed`, L7, S6 |
| **Q5** | Tényleg 2000-ben nyílt a műhely? (Ezt a daibau-profil állítja, nem az ügyfél.) | A H1-ben és a JSON-LD `foundingDate`-jében szerepel. **Ha nem igaz, azonnal ki kell venni.** |
| **Q6** | Pontos koordináta a bejárathoz (nem a háztömb közepéhez)? | `GeoCoordinates`, útvonalterv |
| **Q7** | A „órákon belül árajánlat, 48 órán belül beépítés" vállalható általános ígéretként, vagy egyetlen szerencsés eset volt? | C8, `/uvegtores/biztositas/`. **Vállalhatatlan ígéretet nem teszek ki.** |
| **Q8** | Tényleg csinál üvegteraszt, üvegkorlátot, télikertet, üvegtetőt? (daibau) Ha igen, miért nincs a saját oldalán? | U9. Ezek a legmagasabb kosárértékű munkák — ha igen, saját oldalt érdemelnek. |
| **Q9** | Melyik a fontosabb üzletág ma: üvegezés vagy képkeretezés? Van-e szezonalitás? | A főoldali sorrend és a hirdetési költés |
| **Q10** | Milyen kapacitás van? Hány munkát tud egy héten? | Ha szűk, a „gyors kiszállás" ígéret visszaüt. Ez befolyásolja, mennyire toljuk a sürgősségi útvonalat. |
| **Q11** | Lehet saját domainnevű e-mail (`ajanlat@pecsiuveges.hu`)? | K3, kézbesíthetőség, szakmai megítélés |
| **Q12** | Ki fogja frissíteni az oldalt, és milyen gyakran? | F4. Ha a válasz „senki", akkor a stack-döntés (D8) még fontosabb, és a tartalmat még statikusabbra kell tervezni. |
| **Q13** | Van cégjegyzék-/nyilvántartási szám, adószám, amit a láblécre kell tenni? | Jogi kötelezettség és bizalmi jel |
| **Q14** | Van meglévő Google Analytics / Search Console hozzáférés? Mekkora ma a forgalom? | A mérés nulláról indul-e, és van-e viszonyítási alap |

### 15.2 Amit **le kell ellenőrizni az élő oldalon**, mert a HTML-t nem láttam

| # | Ellenőrzendő | Ha kiderül, hogy… |
|---|---|---|
| V1 | Van-e `<meta name="viewport">`? | …van, akkor U7 törlendő a hibalistáról |
| V2 | Van-e bármilyen kép az oldalon, és mekkora? | …van, akkor §2.4 P2 újraértékelendő |
| V3 | Van-e már valamilyen strukturált adat? | …van, akkor S4 törlendő |
| V4 | Mi a tényleges `<title>` és `<meta description>`? | S3 pontosítása |
| V5 | Vannak-e aloldalak, amiket a keresőindex nem hozott elő? | …vannak, akkor a §4 sitemap `301`-térképe bővül |
| V6 | Mekkora a valódi LCP/CLS a mai oldalon? | Viszonyítási alap a §11 célokhoz |
| V7 | Ki a domain- és tárhely-tulajdonos, van-e hozzáférés? | F0 egyáltalán elvégezhető-e |

---

## 16. Mi ennek az anyagnak a leggyengébb pontja

Őszintén, sorrendben:

**1. Nem láttam a HTML-t.** Ez a legsúlyosabb korlát. A karakterkódolási hibát
(K1) a beillesztett szövegből bizonyítani tudom, és a HTTPS hiányát is látom a
keresőindexből — de a viewport, a strukturált adat, a képek és a tényleges
teljesítmény ügyében **feltételezésekkel dolgoztam, és ezt mindenhol jelöltem**
(§15.2). Ha kiderül, hogy az oldal reszponzív, a hibalistám egy pontja elesik.
Ettől a stratégia nem dől meg, de a diagnózis pontossága sérül.

**2. Nincs egyetlen valódi fotó sem, és ez nem kozmetikai hiány.** Az üvegezés és
a képkeretezés is **vizuális szakma**, és a bizalom fele a munka látványán múlik.
A prototípus szándékosan fenntartott helyeket mutat, nem stockot — ez tisztességes,
de a demó ettől **soványabb, mint amilyen az éles oldal lesz.** Ha az ügyfél
holnap küld 20 telefonos fotót a műhelyből, ez az anyag azonnal 30%-kal erősebb.

**3. Nincs egyetlen ár sem, és emiatt a legfontosabb vevői kérdés
megválaszolatlan marad.** A laikus első kérdése: „mennyibe kerül egy ablaküveg?"
Kitalált számot nem írok le, tehát ez a kérdés **nyitva marad az anyag végéig**
(Q3). Egy ártartomány — akár csak „kirakatüveg m²-ára [x]-től" — mérhetően
javítaná a konverziót, és nélküle a §12 CRO-fejezet egy lábon áll.

**4. A 2000-es évszám a H1-ben egy harmadik fél állításán nyugszik.** A
`daibau.hu` profilja írja, nem az ügyfél. Beleírtam, mert erős, de **ha nem igaz,
azonnal ki kell venni** (Q5). Egy hamis évszám a főcímben pont azt a bizalmat
rombolja, amit építeni akar.

**5. A tábla (a szignatúra elem) egy fogadás.** Azt feltételezi, hogy a látogató
kíváncsi, és megpróbálja meghúzni. Ha nem — mert sürgős a baja, mert mobilon
nem veszi észre a fogantyút, mert nem szokott hozzá —, akkor a hero fele
dekoráció marad, és a C3 konverziós elem nem működik. **Ezt mérni kell**, nem
hinni: ha az „Átveszem" gomb 8 hét után a látogatók 3%-a alatt marad, a táblát
statikus, feliratozott illusztrációra kell cserélni, és a méretbekérést az
űrlapba visszatolni. Az elemet úgy építettem, hogy ez a csere **egy szekció
cseréje** legyen, ne az egész hero újratervezése.

**6. A verseny elemzése hiányos.** A pécsi mezőnyt (`pecsiuvegmester.hu`,
`uvegker.hu`, ÜVEGKOVÁCS, Üveges Gyorsszolgálat) a keresőtalálatok szintjén
azonosítottam, de az oldalaikat **nem tudtam megnyitni** — ugyanaz az egress-tiltás.
A „mitől néznek ki mind egyformán" állításom (D1) ezért **hipotézis**, nem
megfigyelés. Élesítés előtt fél óra manuális átnézés kell.

---

## Források

Az anyag a következő, indexelt forrásokra épül (közvetlen lekérés nélkül):

- `http://www.pecsiuveges.hu/` — indexelt oldalcím és a briefbe illesztett teljes oldalszöveg
- Google Cégprofil kivonata (a briefben szó szerint): 4,7 · 66 vélemény, „Üveg- és tükörbolt", nyitvatartás, `06 30 267 6709`
- [daibau.hu — Váradi Ferenc EV](https://www.daibau.hu/varadi_ferenc_ev) — 2000-es alapítás, üvegterasz/üvegkorlát/télikert/üvegtető
- [varadi-uveges.uzleti.hu](https://varadi-uveges.uzleti.hu/) — szolgáltatáslista, elérhetőségek
- [Cylex — Váradi Ferenc Üveges Vállalkozó](https://xn--pcs-bma.cylex.hu/ceg-info/v%C3%A1radi-ferenc-%C3%BCveges-v%C3%A1llalkoz%C3%B3-676585.html)
- [Yoys — Üveg- és tükörbolt, Pécs](https://www.yoys.hu/phone-36-72321316-%C3%BCveg--%C3%A9s-t%C3%BCk%C3%B6rbolt-P%C3%A9cs-HU36071.html) — vezetékes szám, nyitvatartás
- [szakkatalogus.hu — Váradi Ferenc, kertvárosi üveges](https://www.szakkatalogus.hu/infok/V%C3%A1radi_Ferenc_kertv%C3%A1rosi_%C3%BCveges-513408)
- [bonumventus.hu](https://bonumventus.hu/12225274097285326723/) — vásárlói visszajelzések
- Versenytársként azonosítva: [pecsiuvegmester.hu](https://pecsiuvegmester.hu/), [uvegker.hu](https://uvegker.hu/), [uveg-kovacs-pecs.uzleti.hu](https://uveg-kovacs-pecs.uzleti.hu/), [joszaki.hu/szakemberek/uveges/pecs](https://joszaki.hu/szakemberek/uveges/pecs)

---

**Kapcsolódó fájl:** `index.html` — a főoldal működő, egyfájlos prototípusa.
