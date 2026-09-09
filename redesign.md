# Gömböc Pizzéria, Pécs — UI/UX redesign koncepció és működő prototípus

> **Módszertani figyelmeztetés — rekonstrukcióból dolgoztam.**
> A `gombocpizzeria.hu` és minden nagyobb magyar vendéglátós aggregátor
> (etterem.hu, pizza-etterem.hu, pecsma.hu, nyitva.hu, menuzz.hu, foodyas.com)
> **egress-blokkolt** ebben a környezetben: közvetlen HTTP-lekérés egyikről sem
> jött létre. Az alábbi anyag a **kereső által indexelt tartalomból** rekonstruált
> tényeken alapul, plusz a feladatkiírásban átadott Google Business Profile-kivonaton.
>
> Ez a dokumentum minden állításnál megnevezi a forrását. Amit nem tudtam
> visszaigazolni, az **`ÜGYFÉL-ADAT SZÜKSÉGES`** jelölést kap — sem itt, sem a
> prototípusban nincs kitalált szám. A §1.1 (technológia) a leggyengébben
> alátámasztott szakasz; lásd §16.

---

## 0. Kontextus — amit tudok, és amit nem

A briefben a kontextus-mezők üresen maradtak. Nem töltöm ki őket találgatással;
az alábbi táblázat szétválasztja a **dokumentált** és a **hiányzó** oldalt.

### 0.1 Dokumentált tények

| Tény | Érték | Forrás |
|---|---|---|
| Név, cím | Gömböc Pizzéria, 7632 Pécs, Nagy Imre út 70. | Google Business Profile (brief), nyitva.hu |
| Telefon | 06 30 899 9303 (új szám) | gombocpizzeria.hu címsora, menuzz |
| Korábbi telefon | +36 72 440 456 | aggregátor-listing |
| E-mail | gombocpizzeria@gmail.com | keresőben indexelt kapcsolati adat |
| Alapítás | **1983**, családi vállalkozásként, a jelenlegi vezető szüleitől | pecsma.hu „Ezért szeretik Kertvárost" |
| Jelenlegi vezető | Fauszt Gábor, **2010 óta** | pecsma.hu |
| Nyitvatartás | V 11–21, H 10:30–21, K–P 10:30–22, Szo 11–22 | nyitva.hu, GBP |
| Kínálat | helyben, **kemencében sütött pizza**, frissensültek, lepények, hamburger, gyros, koktélok, csapolt és üveges sör | etterem.hu / gastro.hu leírás |
| Terek | kerthelyiség (nyári kiülős), kulturált belső tér, **különterem** | gastro.hu, GBP attribútum |
| Attribútumok | kutyabarát, ingyenes parkolás, kedvezményes ételek, nagyszerű koktélok | gastro.hu, GBP |
| Heti menü | 11:00–13:00 vagy a készlet erejéig; **A menü 2 990 Ft**, **B menü 2 690 Ft**, **napi leves 900 Ft**, csomagolás **200 Ft/adag** | menuzz.hu listing |
| Értékelés | 4,6 ★ / ~1 300 értékelés | GBP (brief) |
| Átlagköltés | 4 000–6 000 Ft / fő | GBP (brief) |
| Foglalási jelzés | „Bejelentette 130 személy" | GBP (brief) |

### 0.2 Amit NEM tudok — és ezért nincs az anyagban

Célközönség-kutatás, versenytárs-audit, teljes étlap tételes árakkal, különterem
kapacitása, kiszállítás léte, kártyaelfogadás, SZÉP-kártya, a jelenlegi oldal
forgalmi adatai, arculati kötöttségek. Mind a §15-ben, kérdés formájában.

### 0.3 Az oldal EGY dolga — ez nem találgatás

**Asztalfoglalás (és a vele egyenrangú telefonhívás).** Nem a briefből, hanem
bizonyítékból: a GBP-n „Bejelentette 130 személy" fut, a „Különterem" attribútum
aktív, a jelenlegi oldal maga is a hívásra terel („Foglalás vagy érdeklődés esetén
várják a hívásaidat"), és nincs online rendelési rendszer, amire terelni lehetne.
A másodlagos cél a **heti menü** napi elérése — ez a visszatérő, hétköznap déli
forgalom motorja.

---

## 1. A jelenlegi állapot elemzése

### 1.1 Technológia

Közvetlen lekérés nem jött létre, így ez a szakasz **indexelt jelekből** olvasható
ki, és élesítés előtt egy valódi audit kell hozzá.

| Jel | Amit indexelt nyomból látni | Következtetés |
|---|---|---|
| URL-szerkezet | `/etlap-3/`, `/kapcsolat/`, `/heti-menu-hirek/` | WordPress. Az `etlap-3` a WP automatikus slug-ütközés-feloldása: legalább kétszer újralétrehozott oldal, kézi rendrakás nélkül |
| Protokoll | az indexelt linkek `http://` sémával jönnek | **HTTPS hiányzik vagy nincs kikényszerítve** — kritikus |
| Címsor-tartalom | „Új telefonszámunk: +36-30/899-9303" a *`<title>`-ben* | a telefonszám a sablon site-tagline mezőjébe került, tehát **minden aloldal title-jében** ott van |
| Oldalcím | „Gömböc Pizzéria – Várunk változatos ételeinkkel" | generikus tagline, se hely, se kategória, se USP |
| Aloldalak | Étlap, Kapcsolat, Heti menü / Hírek | 3–4 oldalas, klasszikus kisvállalkozói WP-struktúra |

**Amit ebből biztosan lehet állítani:** a title-taxonómia elromlott, és az URL-ek
karbantartatlanok. Amit nem: a sablon neve, a plugin-lista, a hoszting, a
Core Web Vitals valós mérése. Ehhez hozzáférés kell (§15).

### 1.2 A jelenlegi tartalom szerkezete (rekonstruált)

```
/                  Főoldal — „Várunk változatos ételeinkkel" + kínálat-bekezdés
/etlap-3/          Étlap
/heti-menu-hirek/  Heti menü és hírek egy oldalon összekeverve
/kapcsolat/        Cím, telefon, e-mail
```

### 1.3 MI A JÓ BENNE — külön szedve, és amit megtartok

Ez a rész nem udvariasság. Egy 1983 óta működő helynél a régi megoldások egy része
azért él még, mert **működik**, és eldobni őket kár lenne.

| Ami jó | Miért jó | Sorsa a redesignban |
|---|---|---|
| **A telefonszám a legelső helyen** | A tényleges konverziós csatorna. A tulaj tudja, hogy a foglalás telefonon jön | **Megtartva és erősítve**: fejlécben állandó CTA, mobilon fix alsó sávban. Nem tolom le űrlap javára |
| **Heti menü mint önálló oldal** | A visszatérő déli forgalom pontosan ezt keresi | **Megtartva**, de kiemelve a „Hírek"-ből: külön URL, a főoldalon árakkal |
| **Rövid, 3–4 oldalas szerkezet** | Egy pizzéria nem igényel többet; könnyen karbantartható | **Megtartva.** Nem építek 12 oldalas site-ot azért, hogy „gazdagabb" legyen |
| **Egyszerű, díszítetlen szöveg** | Nincs marketinges vatta, nincs stock-fotós hangulatszöveg | **Megtartva** — a hangnem alapja |
| **A kínálat őszinte felsorolása** (pizza, frissensült, lepény, hamburger, gyros, koktél) | Pontosan leírja, mi ez a hely: nem koncepció-étterem, hanem kertvárosi melegkonyha | **Megtartva szó szerint**, ez lett a §5 „Amit sütünk" szekció gerince |
| **A domain** | `gombocpizzeria.hu` — rövid, pontos, beírható | Változatlan |

### 1.4 Amit a listing tud, és a saját oldal nem mond el

Ez a legdrágább hiány. A Google-találat **többet mond az étteremről, mint az
étterem saját oldala**:

- 4,6 ★ / ~1 300 értékelés — az oldalon nem szerepel
- 1983 óta, családi kézben, 2010 óta Fauszt Gábor vezeti — az oldalon nem szerepel
- Különterem, kerthelyiség, kutyabarát, ingyenes parkolás — az oldalon nem szerepel
- 4 000–6 000 Ft/fő árszint — az oldalon nem szerepel
- Heti menü árai (2 990 / 2 690 / 900 Ft) — csak harmadik fél listingjében

A saját oldal jelenleg **gyengébb eladó, mint a róla szóló találatok**.

---

## 2. Problémalista bizonyítékkal

### 2.1 Kritikus

| # | Probléma | Bizonyíték |
|---|---|---|
| K1 | **Nincs (kikényszerített) HTTPS** | minden indexelt belső link `http://` sémájú |
| K2 | **A telefonszám a site-title-ben van** | indexelt `<title>`: „Heti menü - Hírek - Új telefonszámunk: +36-30/899-9303 - Gömböc Pizzéria" |
| K3 | **Nincs foglalási felület** | a felhasználó a telefonon kívül semmit nem tud kezdeményezni; a GBP szerint 130-an mégis foglaltak |
| K4 | **Az árak nincsenek a saját oldalon** | a heti menü árai csak a menuzz.hu-n érhetők el |
| K5 | **Nincs strukturált adat** | a találat nem hozza a nyitvatartást, értékelést, menüt |

### 2.2 UX

| # | Probléma | Bizonyíték |
|---|---|---|
| U1 | „Heti menü / Hírek" **egy oldalon** | az URL maga: `/heti-menu-hirek/` — két külön szándék egy dokumentumban |
| U2 | A „ma mi a menü?" kérdésre **nincs válasz a főoldalon** | a főoldal tagline-ja: „Várunk változatos ételeinkkel" |
| U3 | **Nyitvatartás nem derül ki azonnal**; „nyitva vagyunk-e most?" nem megválaszolt | a nyitvatartás csak aggregátorokon konzisztens |
| U4 | `/etlap-3/` — **beszélő URL helyett gépi ütközésfeloldás** | maga a slug |
| U5 | A **különterem** és a **kerthelyiség** — a két legerősebb differenciáló — nincs kifejtve | GBP-attribútumként létezik, oldalon nem |
| U6 | **Nincs társadalmi bizonyíték** | 1 300 értékelés sehol az oldalon |

### 2.3 SEO

| # | Probléma | Bizonyíték |
|---|---|---|
| S1 | Title-sablon elromlott (K2) | minden aloldal title-je hordozza a telefonszámot |
| S2 | **Nincs helymegjelölés a title-ben** | „Gömböc Pizzéria – Várunk változatos ételeinkkel" — se Pécs, se Kertváros, se pizzéria mint kategória |
| S3 | Nincs `Restaurant` / `Menu` / `OpeningHoursSpecification` JSON-LD | rich result nem jelenik meg a találatban |
| S4 | Cím-inkonzisztencia a weben: **Nagy Imre út 70.** vs. **68.** | nyitva.hu és GBP: 70; több aggregátor: 68 — a NAP-konzisztencia (Name/Address/Phone) sérül, ami local rankinget ront |
| S5 | Kettős telefonszám a weben (72/440-456 és 30/899-9303) | ugyanaz a NAP-probléma |

### 2.4 Performance

Valós mérés nélkül (nincs hozzáférés) csak **strukturális kockázatokat** állítok:

| # | Kockázat | Alapja |
|---|---|---|
| P1 | WP-sablon + plugin-halmozódás → 1,5–3 MB-os főoldal | a kategória tipikus profilja; **mérés kell** |
| P2 | Nem méretezett, nem modern formátumú képek → LCP-romlás | ugyanaz |
| P3 | HTTP-n futó oldal → nincs HTTP/2, nincs modern cache-viselkedés | K1 következménye |

> Ezt a szakaszt szándékosan nem hígítom kitalált számokkal. A §11 **célszámokat**
> ad, nem jelenlegi mérést.

---

## 3. Miért rosszak ezek — a mögöttes ok, nem a tünet

Öt tünet, három tényleges ok.

**3.1 Az oldal *létezésnek* készült, nem *munkának*.**
A `/etlap-3/` slug, a title-be írt telefonszám és a „Várunk változatos ételeinkkel"
tagline mind ugyanazt mutatja: valaki egyszer feltette az oldalt, aztán csak
*hozzáírt*. A telefonszám a tagline-mezőbe került, mert ott a leggyorsabb volt
kiírni — nem mert oda való. Ez nem hanyagság: ez a **CMS rossz affordanciája**
találkozva egy olyan üzemeltetővel, akinek a pizzasütés a munkája. A redesign
feladata nem „szebb oldal", hanem **olyan szerkezet, amit karbantartás nélkül sem
lehet elrontani**.

**3.2 Az oldal az étteremről beszél, a vendég viszont döntést hoz.**
„Várunk változatos ételeinkkel" — ez a *hely* nézőpontja. A vendég három kérdéssel
érkezik: *nyitva vagytok most? mi a mai menü, és mennyi? tudok asztalt kapni ma
estére?* Ezek egyikére sem válaszol az oldal. A GBP mind a háromra válaszol —
ezért nyeri meg a Google-találat a saját oldal ellen. A hiány nem tartalmi, hanem
**nézőpontbeli**.

**3.3 A hely legerősebb tényei kívül rekedtek, mert nem „weboldalas" tények.**
1983, negyven év, egy család, kemence, kerthelyiség, különterem, 1 300 értékelés.
Ezek nem fértek be, mert a kisvállalkozói WP-sablon **hero-kép + három hasáb +
kapcsolat** sémája nem kínál helyet nekik. Az információs architektúra tehát nem
azért hiányos, mert kevés a tartalom, hanem mert a **sablon szabta meg a
tartalmat**, nem fordítva.

Ezért a §4-ben nem oldalakat rendezek át: **azt a három kérdést teszem az oldal
tetejére, amivel a vendég érkezik.**

---

## 4. Új információs architektúra és sitemap

Elv: **4 URL, mindegyik egy keresési szándékra**. Nem építek több oldalt, mint
amennyit egy pizzéria karbantartani tud (§1.3).

| URL | Keresési szándék | Miért önálló URL |
|---|---|---|
| `/` | „gömböc pizzéria" / „pizza pécs kertváros" — márka és felfedezés | Ez a landolás. Minden fenti kérdésre (nyitva? menü? asztal?) itt jön válasz, továbbkattintás nélkül. A foglalás is itt zárul |
| `/etlap/` | „gömböc étlap", „pizza árak pécs" | A leggyakoribb *tranzakciós előtti* keresés. Beszélő slug az `/etlap-3/` helyett, **301 a régiről**. Külön URL, mert megosztható és `Menu` schemával indexelhető |
| `/heti-menu/` | „napi menü pécs kertváros", „heti menü pécs" | **Ez a legnagyobb nyeremény.** Heti frissítésű, ismétlődő szándék, saját közönséggel. Külön URL kell, mert a tartalma hetente cserélődik, és mert a „Hírek"-től el kell választani (U1). A régi `/heti-menu-hirek/` **301** ide |
| `/kulonterem/` | „különterem pécs", „céges ebéd pécs", „ballagás hely" | Magas értékű, alacsony volumenű, **erős szándékú** keresés. Ma nulla tartalommal versenyzik. Külön URL, mert saját lekérdezéskört szolgál, és mert a foglalási űrlapon van külön ága |

**Ami szándékosan NEM lesz külön oldal:**

| Elvetett URL | Miért nem |
|---|---|
| `/rolunk/` | A történet (1983, család) a főoldalon bizonyíték, nem külön olvasmány. Külön oldalon senki nem olvassa el |
| `/galeria/` | Fotó-oldal karbantartás nélkül azonnal elavul; a §7.7 szignatúra-eleme épp azért nem fotóra épül |
| `/hirek/` | A „Hírek" a Facebook dolga. Az oldalnak nem kell blogmotort üzemeltetnie |
| `/kapcsolat/` | **Ezt megszüntetem**, és a főoldal záró szekciójába olvasztom (cím + telefon + űrlap + nyitvatartás). Egy 4 URL-es site-on a kapcsolat külön kattintás = felesleges lépés a konverzió előtt. **301** a `/` `#foglalas` horgonyra |

---

## 5. Oldalankénti felépítés

### 5.1 Főoldal (`/`) — **ez készült el prototípusként** (`index.html`)

| # | Szekció | Tartalom | Miért itt |
|---|---|---|---|
| 1 | Fejléc | Szóvédjegy + „PÉCS 1983", nav, téma-váltó, telefon-CTA | Az 1983 a szóvédjegy mellett = a differenciáló az első pixeltől |
| 2 | Hero | H1, vezető bekezdés, 2 CTA, **A Kemence** (§7.7), bizonyítéksor (1983 / 4,6 / 2 690 Ft) | A három érkező kérdés közül kettőre (nyitva? mennyi?) itt jön válasz |
| 3 | Heti menü | A 2 990 / B 2 690 / leves 900, sáv 11–13, csomagolás 200 Ft | A visszatérő déli forgalom motorja; **ár a hajtás alatt közvetlenül** |
| 4 | Amit sütünk | 6 tétel: kemencés pizza, frissensültek, lepény, hamburger, gyros, koktél/sör | Az 1.3 szerint megtartott, működő szöveg — szerkezetbe rendezve |
| 5 | Nyitvatartás | Teljes heti táblázat, mai nap kiemelve, élő állapot | U3 közvetlen megoldása |
| 6 | Terek | Kerthelyiség / Különterem | U5: a két differenciáló először kap felületet |
| 7 | Asztalfoglalás | Űrlap + telefon egyenrangúan | K3; az oldal EGY dolga |
| 8 | Lábléc | NAP-adatok gépi és emberi olvasásra | S4/S5 konzisztencia-horgony |

### 5.2 `/etlap/`

| # | Szekció | Tartalom |
|---|---|---|
| 1 | Fejléc + H1 „Étlap" | változatlan navigáció |
| 2 | Ugró-navigáció | Pizzák / Frissensültek / Lepények / Hamburger / Gyros / Italok — sticky, mobilon vízszintesen görgethető |
| 3 | Kategóriablokkok | tétel + rövid összetevősor + ár, `tabular-nums` oszlopban |
| 4 | Allergén- és méret-lábjegyzet | `ÜGYFÉL-ADAT SZÜKSÉGES` |
| 5 | Záró CTA | „Asztalt foglalok" + telefon |

### 5.3 `/heti-menu/`

| # | Szekció | Tartalom |
|---|---|---|
| 1 | H1 + a hét dátumtartománya | gépileg generált, hogy sose látszódjon elavultnak |
| 2 | Napi bontás H–P | A menü / B menü / leves, mai nap kiemelve |
| 3 | Árblokk | 2 990 / 2 690 / 900 / csomagolás 200 |
| 4 | „Hogyan viszem el" | sáv 11–13, telefonos előjelzés |

### 5.4 `/kulonterem/`

| # | Szekció | Tartalom |
|---|---|---|
| 1 | H1 + kapacitás | `ÜGYFÉL-ADAT SZÜKSÉGES` — fő létszám |
| 2 | Alkalmak | céges ebéd, ballagás, születésnap, keresztelő |
| 3 | Feltételek | minimális fogyasztás, előfoglalás, kizárólagosság — `ÜGYFÉL-ADAT SZÜKSÉGES` |
| 4 | Ugyanaz a foglalási űrlap, „Különterem-igény" előre kiválasztva |

---

## 6. Wireframe

### 6.1 Desktop (≥1024px)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Gömböc │PÉCS│   Heti menü  Amit sütünk  Nyitvatartás  Különterem  ( ☀ ) │
│         │1983│                                    [ 06 30 899 9303 ]     │  sticky, 68px
├──────────────────────────────────────────────────────────────────────────┤
│                                            ╭──────────────────────────╮  │
│ — PÉCS-KERTVÁROS, NAGY IMRE ÚT 70          │        ▄▄▄▄▄▄▄▄          │  │
│                                            │     ▄▀          ▀▄   ║   │  │
│ A kemence *reggel óta* megy.               │   ▄▀   ┌────────┐  ▀▄ ║   │  │
│ Mint 1983 óta minden nap.                  │  │     │▓▓▓▓▓▓▓▓│     │║   │  │
│                                            │  │     │ ◉◉◉◉◉  │     │    │  │
│ Családi pizzéria a kertvárosi              │  └─────┴────────┴─────┘    │  │
│ buszmegálló mellett. Helyben,              │  ══════════════════════    │  │
│ kemencében sült pizza, ...                 │    ║                ║      │  │
│                                            ╰──────────────────────────╯  │
│ [ Asztalt foglalok ] [ Mi a mai menü? ]      ( ● Most nyitva — 22:00 )   │
│ ──────────────────────────────────────       Nem dísz: a parázs a valós  │
│ 1983          4,6            2 690 Ft        nyitvatartásból izzik.      │
│ Óta a N.I.úton  1300 értékelés  B menü                                   │
├──────────────────────────────────────────────────────────────────────────┤
│ — HÉTKÖZNAP DÉLBEN                                                       │
│ Heti menü 11:00-tól 13:00-ig, vagy amíg a készlet tart                   │
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐                    │
│ │ A menü        │ │ B menü        │ │ Napi leves    │                    │
│ │ 2 990 Ft      │ │ 2 690 Ft      │ │ 900 Ft        │                    │
│ └───────────────┘ └───────────────┘ └───────────────┘                    │
│ Elviteli csomagolás 200 Ft/adag. …[ÜGYFÉL-ADAT SZÜKSÉGES]                │
├──────────────────────────────────────────────────────────────────────────┤
│ — AMIT A KEMENCÉBŐL ÉS A KONYHÁBÓL KIVESZÜNK                             │
│ ─────────────────  ─────────────────  ─────────────────                  │
│ ◭ Kemencés pizza   ◗ Frissensültek    ⬭ Lepények                         │
│ ─────────────────  ─────────────────  ─────────────────                  │
│ ⬒ Hamburger        ⌇ Gyros            Y Koktélok, sör                    │
├──────────────────────────────────────────────────────────────────────────┤
│ — MIKOR MEGYÜNK                     │ NAP           NYITVA               │
│ Hétfőn és vasárnap 21:00-kor        │ ─────────────────────────          │
│ zárunk, egyébként 22:00-kor         │ Hétfő         10:30 – 21:00        │
│                                     │ Kedd          10:30 – 22:00        │
│ A konyha zárás előtt kb. 30 perccel │▌Szerda        10:30 – 22:00  ← ma  │
│ vesz fel utolsó rendelést. …        │ Csütörtök     10:30 – 22:00        │
│ ( ● Most nyitva — 22:00-kor zárunk )│ …                                  │
├──────────────────────────────────────────────────────────────────────────┤
│ — AHOL LEÜLTÖK                                                           │
│ ┌────────────────────────────┐  ┌────────────────────────────┐           │
│ │ Kerthelyiség               │  │ Különterem                 │           │
│ │ …                          │  │ … [ÜGYFÉL-ADAT SZÜKSÉGES]  │           │
│ │ [Nyáron][Kutyabarát][Park] │  │ [Előfoglalással][Zárt tér] │           │
│ └────────────────────────────┘  └────────────────────────────┘           │
├──────────────────────────────────────────────────────────────────────────┤
│ — ASZTALFOGLALÁS               │ ┌ Név ────────┐ ┌ Telefonszám ────────┐ │
│ Szóljatok előre, és lesz asztal│ └─────────────┘ └─────────────────────┘ │
│                                │ ┌ Dátum ──────┐ ┌ Időpont ────────────┐ │
│ TELEFON  06 30 899 9303        │ └─────────────┘ └─────────────────────┘ │
│ E-MAIL   gombocpizzeria@…      │ ┌ Hányan ─────┐ ┌ Milyen alkalom? ▾ ──┐ │
│ CÍM      7632 Pécs, N.I. út 70 │ └─────────────┘ └─────────────────────┘ │
│                                │ ┌ Megjegyzés ───────────────────────── ┐│
│                                │ └──────────────────────────────────────┘│
│                                │ [ Foglalás elküldése ] [ Inkább telefon]│
├──────────────────────────────────────────────────────────────────────────┤
│ Gömböc Pizzéria     │ Elérhetőség        │ Az oldalon                     │
│ Kemencés pizzéria…  │ 7632 Pécs, …       │ Heti menü / Étlap / …          │
└──────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Mobil (360–430px)

```
┌────────────────────────────┐
│ Gömböc│1983  (☀) [ 📞 ]    │ sticky 68px  (a telefon ikonos, a szám a sávban)
├────────────────────────────┤
│ — PÉCS-KERTVÁROS,          │
│   NAGY IMRE ÚT 70          │
│                            │
│ A kemence *reggel          │  H1: clamp() alsó vége, 2,4rem
│ óta* megy. Mint            │
│ 1983 óta minden            │
│ nap.                       │
│                            │
│ Családi pizzéria a         │
│ kertvárosi buszmegálló     │
│ mellett. …                 │
│                            │
│ [ Asztalt foglalok      ]  │  teljes szélesség, 48px
│ [ Mi a mai menü?        ]  │
│                            │
│ ╭────────────────────────╮ │  A Kemence a szöveg ALATT:
│ │      ▄▄▄▄▄▄▄▄▄▄        │ │  mobilon a válasz előbb jön,
│ │   ▄▀  ┌──────┐  ▀▄  ║  │ │  mint a kép
│ │  │    │▓▓▓▓▓▓│    │  ║  │ │
│ │  └────┴──────┴────┘     │ │
│ │  ═══════════════════    │ │
│ ╰────────────────────────╯ │
│ ( ● Most nyitva — 22:00 )  │
│ Nem dísz: a parázs a valós │
│ nyitvatartásból izzik.     │
│                            │
│ ───────────────────────    │
│ 1983    4,6     2 690 Ft   │  wrap-elő flex
├────────────────────────────┤
│ — HÉTKÖZNAP DÉLBEN         │
│ Heti menü 11:00-tól …      │
│ ┌────────────────────────┐ │  1 hasáb
│ │ A menü   2 990 Ft      │ │
│ └────────────────────────┘ │
│ ┌────────────────────────┐ │
│ │ B menü   2 690 Ft      │ │
│ └────────────────────────┘ │
│ ┌────────────────────────┐ │
│ │ Napi leves   900 Ft    │ │
│ └────────────────────────┘ │
├────────────────────────────┤
│ ── ◭ Kemencés pizza        │  1 hasáb 620px alatt,
│ ── ◗ Frissensültek         │  2 hasáb 620–960px között
│ ── ⬭ Lepények              │
│ …                          │
├────────────────────────────┤
│ Nyitvatartás — táblázat    │  a szöveg és a táblázat
│ egymás alatt               │  egymás alá kerül
├────────────────────────────┤
│ Kerthelyiség (kártya)      │
│ Különterem (kártya)        │
├────────────────────────────┤
│ Asztalfoglalás             │
│ ┌ Név ───────────────────┐ │  a mezők 560px alatt
│ └────────────────────────┘ │  egy hasábba állnak
│ ┌ Telefonszám ───────────┐ │
│ └────────────────────────┘ │
│ …                          │
│ [ Foglalás elküldése    ]  │
├────────────────────────────┤
│ Lábléc, 1 hasáb            │
├────────────────────────────┤
│ [ Asztalfoglalás ][ Hívás ]│ ← FIX alsó sáv, safe-area-inset,
└────────────────────────────┘   a body 84px alsó paddinggel
```

---

## 7. Design system

### 7.0 A vizuális kiindulópont — egy mondatban

> **A kemence maga: a samott-tégla okkerje, a parázs narancsa, a fahamu szürkéje
> és a kormos boltív — vagyis annak a négy anyagnak a színe, amit ebben a
> konyhában tényleg megfognak, nem az „olasz pizzéria" jelmeztára.**

Ebből következik minden lenti döntés: a paletta a parázs–hamu tengelyen mozog,
a szignatúra-elem maga a kemence, a sötét mód pedig nem „invertált világos", hanem
**a kemence este** — amikor a nyílás a legvilágosabb pont a helyiségben.

**Amit ez kizár, és miért:** nem használok piros-fehér-zöld olasz kódot (nem
olasz hely: gyros és hamburger is van az étlapon), nem használok fekete hátteret
egyetlen neonzöld akcenttel (§7.8), és nem építek fotóra (§7.7).

### 7.1 Színtokenek

Kilenc nevesített token. A kontrasztarányokat WCAG 2.1 relatív luminancia szerint
számoltam; minden szövegszín **AA fölött**, a UI-kontúrok **3:1 fölött**.

**Világos mód** (alap: `--liszt` #FAF6EF, emelt felület: `--tepsi` #FFFDF8)

| Token | Hex | Szerep | Kontraszt `--liszt`-en | WCAG |
|---|---|---|---|---|
| `--liszt` | `#FAF6EF` | alap háttér | — | — |
| `--tepsi` | `#FFFDF8` | emelt felület (kártya, űrlap-szakasz) | — | — |
| `--korom` | `#1F1A14` | elsődleges szöveg | **16,03:1** | AAA |
| `--hamu` | `#6A6156` | másodlagos szöveg | **5,64:1** | AA |
| `--tegla` | `#8C3A1B` | márka, címsor-accent, árak | **7,12:1** | AAA |
| `--parazs` | `#B24A11` | CTA, fókuszgyűrű, hibaállapot | **5,02:1** | AA |
| `--lomb` | `#3D6B3F` | „nyitva" állapot, sikeres foglalás | **5,78:1** | AA |
| `--vonal` | `#E3D9C9` | dekoratív elválasztó (nem hordoz információt) | 1,30:1 | n/a |
| `--vonal-eros` | `#8A7F6D` | űrlapkeret, UI-kontúr | **3,65:1** | AA (non-text) |

`--on-parazs` `#FFFFFF` a CTA feliratára: **5,41:1** a `--parazs` gombon.
`--parazs-feny` `#F0842F` **kizárólag dekoráció** (a parázs izzása), sosem hordoz
szöveget vagy önálló jelentést.

**Sötét mód** — nem inverzió: deszaturált, világosabb tonális variánsok
(alap `#14110D`, felület `#1E1A15`)

| Token | Hex | Kontraszt alapon | WCAG |
|---|---|---|---|
| `--korom` | `#F2EAE0` | **15,79:1** | AAA |
| `--hamu` | `#A79C8D` | **6,98:1** | AA |
| `--tegla` | `#E8A07A` | **8,73:1** | AAA |
| `--parazs` | `#F0842F` | **7,21:1** | AAA |
| `--lomb` | `#8FBE8B` | **8,88:1** | AAA |
| `--vonal-eros` | `#7A6E5E` | 3,48:1 felületen | AA (non-text) |
| `--on-parazs` | `#14110D` | **7,21:1** a CTA-n | AAA |

**A három téma-állapot kezelése** (ez a leggyakoribb hiba a dark mode-nál):
a felhasználónak nem két, hanem **három** állapota van. A teljes világos palettát a
csupasz `:root` deklarálja; a `@media (prefers-color-scheme: dark)` blokk
`:root:not([data-theme="light"])` védőszelektorral **csak felülír**; és
`:root[data-theme="dark"]` újra felülír, hogy a kézi váltó mindkét irányban
nyerjen. Így a **nem stampelt (rendszerkövető) állapot** is helyesen rajzol —
egyetlen szín sincs, aminek az egyetlen definíciója media query-ben ülne.

### 7.2 Típusskála

**Két variable betűcsalád, mindkettő teljes latin-ext lefedettséggel (ő, ű
működik).**

| Szerep | Betű | Tengelyek | Miért ez |
|---|---|---|---|
| Display | **Fraunces** | `opsz 9–144`, `wght 400–800`, `SOFT`, `WONK` | Egy 1970-es–80-as évekbeli, meleg, enyhén esetlen antikva. Pontosan az az évtized, amiben a Gömböc elindult (1983), és a `SOFT`/`WONK` tengelyekkel **hangolható**, mennyire különc — nem „elegáns étterem", hanem *régi, karakteres, kézzel csinált*. Optikai méret-tengelye van, tehát nagy méretben tud feszes lenni |
| Szöveg / UI | **Figtree** | `wght 400–700` | Meleg, kissé lekerekített groteszk, magas x-magassággal; hosszú ékezetes magyar szövegben (ő, ű dupla ékezet) is szellős marad. Semleges, de **nem hideg** — nem viszi el a figyelmet a Frauncestől |

**A Fraunces minimális használati mérete: 20px.** A `WONK` tengely bekapcsolt
állapotban (`WONK 1`) az `a`, `g`, `y` betűkön szándékosan „félrecsúszott"
részleteket ad; ez 20px alatt zajjá mosódik és rontja az olvashatóságot. Ezért a
Fraunces **csak** H1/H2/H3, ár-számok és a szóvédjegy szerepét viszi — minden
16px alatti elem (címkék, sugó-szövegek, lábjegyzet) Figtree.

**Amit elvetettem:** Playfair Display + Inter (a brief kifejezetten tiltja, és
jogosan: ez ma az „AI-generált étteremoldal" alapértelmezése); Lora + Source Sans
(korrekt, de karaktertelen); és a skill-adatbázis saját ajánlása, a **Playfair
Display SC + Karla** — ugyanaz a csapda, csak kiskapitálisban.

```css
--sz-mikro:  clamp(.75rem,  .72rem  + .15vw, .82rem);   /* címke, lábjegyzet   */
--sz-kis:    clamp(.875rem, .85rem  + .18vw, .95rem);   /* UI, sugó, táblázat  */
--sz-alap:   clamp(1rem,    .97rem  + .22vw, 1.12rem);  /* folyószöveg         */
--sz-vezeto: clamp(1.12rem, 1.04rem + .4vw,  1.35rem);  /* hero vezető         */
--sz-h3:     clamp(1.25rem, 1.14rem + .55vw, 1.6rem);
--sz-h2:     clamp(1.6rem,  1.35rem + 1.2vw, 2.5rem);
--sz-h1:     clamp(2.4rem,  1.7rem   + 3.2vw, 4.6rem);
```

A folyószöveg alsó vége **16px** — mobilon ez alatt az iOS automatikus
nagyítást indít űrlapmezőn. Sorhossz: `max-width: 46ch` a hero vezetőn,
`56ch` a szakaszfejeken.

### 7.3 Térköz — 8px alapú

```
--t1  4px    ikon–szöveg finomhangolás
--t2  8px    alapegység: gomb belső, címke–mező
--t3 16px    bekezdésköz, kártya-belső kis oldal
--t4 24px    rács-hézag, kártya-belső
--t5 32px    kártya-belső nagy, blokkok között
--t6 48px    szakaszfej és tartalom között
--t7 64px    hasábköz desktopon
--t8 96px    szakaszok közötti függőleges ritmus
--t9 128px   tartalék a legnagyobb töréspontra
```

Sugár: `--r-s 4px` (címke), `--r-m 10px` (gomb, mező), `--r-l 18px` (kártya).
Három érték, nem egy — a §7.6 szerint a sugár **szerepet jelöl**, nem díszít.

### 7.4 Elevation — 3 szint, szűken

| Szint | Érték (világos) | Hol |
|---|---|---|
| 1 | `0 1px 2px rgba(31,26,20,.06)` | alig — finom elválasztás |
| 2 | `0 4px 14px -4px rgba(31,26,20,.14)` | **elsődleges CTA nyugalmi állapot** |
| 3 | `0 18px 40px -18px rgba(31,26,20,.34)` | elsődleges CTA hover |

Sötét módban ugyanez a három szint fekete alapon, magasabb alfával
(.5 / .6 / .85) — sötét háttéren a világos árnyék nem működik.
**A kártyák nem kapnak árnyékot**, csak keretet: az árnyék itt kizárólag azt jelöli,
ami *megnyomható*. Ez az `elevation-consistent` és a „nem minden kártya" szabály.

### 7.5 Egyéb tokenek

```
--ki  cubic-bezier(.22,.61,.36,1)     belépés (ease-out)
--be  cubic-bezier(.55,.06,.68,.19)   kilépés (ease-in)
--ido-gyors  150ms   --ido-alap 240ms   --ido-lassu 380ms
```

### 7.6 Komponenslista

| Komponens | Változatok | Állapotok |
|---|---|---|
| Gomb | `gomb-fo` (parázs), `gomb-mas` (kontúr), `gomb-ikon` (44px kör) | rest / hover / **focus-visible (3px parázs gyűrű, 3px offset)** / active (scale .975) |
| Fejléc | sticky, 68px, `backdrop-filter: blur(12px)` | görgetve / tetején |
| Fő navigáció | 940px felett látszik | rest / hover (alávonás `scaleX` 0→1) / focus |
| Bizonyítéksor | 3 tétel, `tabular-nums` | — |
| **A Kemence** | inline SVG | `zarva` / `nyitva` / `utolso` |
| Állapot-chip | pont + szöveg | zárva (hamu) / nyitva (lomb) / utolsó óra (parázs) |
| Ár-kártya | keret, sugár `--r-l` | rest / hover (−3px, kontúr erősödik) |
| Kínálat-tétel | SVG ikon 30px + cím + leírás | statikus |
| Nyitvatartás-táblázat | `tabular-nums`, mai sor kiemelve parázs-jelzőrúddal | — |
| Tér-kártya | cím + szöveg + címkesor | statikus |
| Űrlapmező | text / tel / date / time / number / select / textarea | rest / hover / focus / **hibás (parázs keret + 3px halo + ikonos üzenet)** |
| Hibaösszegző | `role="alert"`, horgony-linkek a mezőkre | rejtett / látható |
| Siker-panel | `role="status"`, lomb keret | rejtett / látható |
| Mobil akciósáv | 2 gomb, `env(safe-area-inset-bottom)` | 940px alatt |
| Téma-váltó | nap/hold ikon, `aria-pressed` | világos / sötét |

**Ikonok:** kézzel rajzolt, egységes SVG-készlet — 30px, `stroke-width 1.6`,
`stroke-linecap/linejoin: round`, `currentColor`. **Nulla emoji, nulla
ikon-könyvtár, nulla raszter.** Összesen ~1,4 KB inline.

### 7.7 A SZIGNATÚRA-ELEM — „A Kemence"

**Mi:** a kemence keresztmetszete inline SVG-ben, a hero jobb hasábjában — kupola,
samott-téglasorok, kémény, sütőlap, szájnyílás. A nyílásban **parázságy**, ami a
**valós nyitvatartásból** izzik:

| Állapot | Vizuális | Szöveg |
|---|---|---|
| `zarva` | parázs `opacity .12`, fénykör kikapcsol — hamuszürke | „Most zárva — nyitás csütörtök 10:30-kor." |
| `nyitva` | teli izzás + 4,2s-os `lelegzes` skálázás + 3 felszálló szikra | „Most nyitva — ma 22:00-kor zárunk." |
| `utolso` (zárás előtt ≤60 perc) | parázs `opacity .55` — láthatóan halványul | „Zárás 22:00-kor — utolsó rendelés kb. 21:30-ig." |

**Miért pont ez.** A brief azt kérte, hogy az elem **mutassa meg** a szolgáltatás
lényegét, ne elmondja. Egy kemencés pizzéria lényege bináris és fizikai: **a tűz
vagy ég, vagy nem.** Ha ég, van pizza; ha nem, nincs. Ez az elem tehát nem
illusztráció, hanem **állapotjelző** — ugyanaz az információ, amit a nyitvatartás
hordoz, de a hely saját anyagában elmondva. Ezért nem díszít, hanem dolgozik: a
vendég három érkező kérdése közül az elsőre (*nyitva vagytok most?*) ez válaszol,
a hajtás fölött, olvasás nélkül. És mert nem fotó, **nem avul el**: nem kell
újrafotózni, ha átfestik a termet.

Az elem alá odaírtam, hogy nem dísz — a „szín ne legyen az egyetlen jelhordozó"
szabály miatt az izzás mellett **mindig ott a szöveges állapot is** (`role="status"`).

**Mibe kerül LCP-ben: gyakorlatilag nullába, mérhetően 0 bájt hálózaton.**
Az elem ~2,6 KB inline SVG-jelölés a HTML-ben, tehát a dokumentummal együtt
érkezik: **nulla extra kérés, nulla extra RTT**. Az LCP-elem így nem ez, hanem a
H1 szövege. A `radialGradient` + `clipPath` egyetlen kompozit réteg, a
`lelegzes` animáció csak `opacity`-t és `transform`-ot mozgat, tehát nem okoz
layoutot és nem számít bele a CLS-be. **Reduced-motion alatt az animáció leáll,
az állapot marad** — az információ megmarad, csak a mozgás tűnik el.

**Az alternatívák és miért nem azok:**

| Alternatíva | Miért nem |
|---|---|
| Nagy hero-fotó a kemencéből | Fotón múlna (a brief tiltja), 200–400 KB LCP-teher, és nincs jogtiszta Gömböc-fotóm |
| Tésztagombóc → pizza morph görgetésre | Szép, de **semmit nem mond a vendégnek**, amit ne tudna. Dekoráció |
| Élő „hány asztal szabad" kijelző | Ehhez foglalási rendszer és fegyelmezett napi karbantartás kell — a §3.1 szerint pont ez az, ami itt nem fog megtörténni |
| Interaktív térkép | Third-party JS, cookie, LCP-teher, és a Google Maps ezt jobban csinálja |

### 7.8 Amit a vizuális irányból tudatosan kizártam

| Tiltott / kockázatos minta | Mi lett helyette |
|---|---|
| Playfair Display + Inter | Fraunces + Figtree (§7.2) |
| 01 / 02 / 03 számozás | Nincs számozás: az oldalon egyetlen valódi sorrend sincs. Ahol sorrend van (nyitvatartás), ott **napnév** áll |
| Fekete háttér + egy neon akcent | Sötét mód = `#14110D` meleg korom, és **három** szemantikus szín (tégla, parázs, lomb) |
| Gradiens a hero-szöveg mögött | A hero háttere sík `--liszt`. Az egyetlen gradiens az egész oldalon a parázs `radialGradient`-je, ott, ahol fizikailag indokolt |
| Stock-fotó vagy emoji ikonként | Kézzel rajzolt, egységes SVG-készlet (§7.6) |
| „Étteremhez piros" automatizmus | A paletta a *kemence* anyagaiból jön, nem a kategóriából. A `--tegla` és a `--parazs` égetett agyag- és parázsszín, nem pizzareklám-piros |

---

## 8. Animációk és mikrointerakciók

Elv: **minden animáció ok-okozatot fejez ki**, a globális időzítés-tokenekből
dolgozik (§7.5), és `transform`/`opacity`-t mozgat — semmi szélesség, magasság
vagy pozíció, tehát nincs reflow és nincs CLS.

| Elem | Interakció | Mozgás | Időzítés / easing |
|---|---|---|---|
| **Parázságy** (szignatúra) | oldal betöltve, nyitva állapot | `opacity .85→1`, `scaleY 1→1.06` | 4 200 ms, `--ki`, végtelen alternálva |
| **Szikrák** ×3 | ugyanaz | `translateY 0→−46px`, `opacity 0→.9→0` | 3 600 ms lineáris, 0 / 1,2 / 2,4 s késleltetéssel |
| **Parázs-állapotváltás** | nyitva → utolsó óra → zárva | `opacity` átmenet | 380 ms `--ki` |
| Elsődleges CTA | hover | háttér `--parazs`→`--tegla`, árnyék 2→3 | 150 ms `--ki` |
| Bármely gomb | aktív (lenyomás) | `scale(.975)` | 150 ms `--ki` |
| Fő navigáció | hover / fókusz | alávonás `scaleX 0→1`, balról | 240 ms `--ki` |
| Ár-kártya | hover | `translateY(−3px)`, keret `--vonal`→`--vonal-eros` | 240 ms `--ki` |
| Szakaszok | görgetéskor belépnek | `opacity 0→1`, `translateY 18px→0` | 380 ms `--ki`, 45 ms lépcsőzéssel |
| Űrlapmező | fókusz | 3px parázs fókuszgyűrű | 150 ms |
| Űrlapmező | blur-validáció hibával | keret `--parazs` + 3px halo, ikonos üzenet megjelenik | 150 ms. **Nincs rázás** — a rázás vesztibuláris zavart okozhat |
| Siker-panel | sikeres beküldés | `felfele`: `opacity 0→1`, `translateY 12px→0` | 380 ms `--ki` |
| Téma-váltó | kattintás | ikoncsere + a teljes felület tokenátmenete | 240 ms |
| Skip-link | fókusz | `top −100px→16px` | 150 ms `--ki` |

**Két szabály, amit végig betartottam:**

1. **Az oldal nyugalmi állapotban teljes.** A belépő animáció **csak** azokra az
   elemekre kerül fel, amelyek betöltéskor a viewport alatt vannak — JS teszi rájuk
   az `opacity: 0`-t, nem a CSS. Ha a JS nem fut le, minden látszik. Egyetlen
   olvasandó tartalom sincs `opacity: 0`-ban parkoltatva egy observerre várva.
2. **`prefers-reduced-motion: reduce` esetén** minden `animation-duration` és
   `transition-duration` 0,001 ms-ra esik, a parázs lélegzése leáll, a szikrák
   `display: none`, a `scroll-behavior` `auto` lesz. **Az információ nem vész el:**
   a parázs statikus izzása és a szöveges állapot ugyanúgy ott van.

---

## 9. Frontend-megvalósítás

### 9.1 Stack

| Réteg | Választás | Indoklás | Alternatíva, és miért nem |
|---|---|---|---|
| Kimenet | **Statikus HTML + CSS, ~4,5 KB vanilla JS** | 4 URL, hetente egy tartalomfrissítés. Nincs olyan igény, amit build-lánc kiszolgálna | Next.js / Astro: karbantartási felület egy olyan üzemeltetőnek, akinek nincs frontend-embere. §3.1 |
| Szerkesztés | **WordPress megtartva, saját sablonnal** (blokk-téma) | Az ügyfél már ismeri, és a heti menüt magának kell tudnia frissíteni. A WP nem az ellenség — a *sablon* volt az | Headless CMS: új felület, új tanulási görbe, nulla haszon 4 oldalon |
| CSS | Egyetlen fájl, custom property-k, `@layer` nélkül | Ekkora felületen a réteges kaszkád több szabályt hoz, mint amennyit megold | Tailwind: build-lánc egy 4 oldalas site-ért |
| JS | Vanilla, IIFE, ES5-kompatibilis szintaxis | Nulla függőség, nulla parse-költség | Alpine.js (~15 KB): többe kerülne, mint a teljes saját logika |
| Hoszting | Bármi HTTPS-sel és HTTP/2-vel | K1 megoldása az első lépés | — |

**A prototípus JS-e (`index.html`) pontosan öt dolgot csinál:** téma-váltás
(`localStorage`, `try/catch`-ben), nyitvatartás-táblázat renderelése egy
adatforrásból, a kemence állapotának számítása percenként, a hajtás alatti
szakaszok belépő animációja, és az űrlap validációja. **Egyetlen külső JS
függőség sincs.**

### 9.2 Fontkezelés

**A prototípusban** a két variable font a Google Fonts CSS-éről jön
(`display=swap`, `preconnect` mindkét hosztra) — hogy a fájl dupla kattintással
megnyíljon, telepítés nélkül.

**Élesben ez nem így lesz.** Termelésben:

```
/fonts/fraunces-latin-ext.woff2   (variable, opsz+wght, latin + latin-ext subset)
/fonts/figtree-latin-ext.woff2    (variable, wght, latin + latin-ext subset)
```

- `unicode-range` szerint kettévágva latin / latin-ext, hogy az ő és ű ne
  kényszerítsen teljes készletet
- `font-display: swap`, és `<link rel="preload" as="font" crossorigin>` **csak a
  Figtree-re** — az a hajtás fölötti folyószöveg; a Fraunces H1-je swap-pel is
  elfogadható, és a preload-halmozás pont az LCP-t rontja
- fallback-lánc valódi metrikákkal: `"Fraunces", "Iowan Old Style", Georgia, serif`
  és `"Figtree", "Segoe UI", system-ui, sans-serif`
- becsült méret: 2 × ~28 KB subsetelve

### 9.3 Képek

A főoldal **egyetlen képet sem tölt be** — ez tudatos: a szignatúra-elem SVG
(§7.7), az ikonok SVG-k. Ahol az `/etlap/` és a `/kulonterem/` később fotót kap:

- AVIF + WebP `<picture>`-ben, JPEG fallback
- `srcset` 480/960/1440w, `sizes` a rácshoz
- **kötelező `width`/`height`** vagy `aspect-ratio` — CLS-védelem
- hajtás alatt `loading="lazy"` és `decoding="async"`
- **Fotó nélkül is teljes az oldal.** Ha az ügyfél nem szállít fotót, semmi nem
  törik el — ez a §7.7 döntésének a másodlagos haszna

### 9.4 Cache

| Erőforrás | Fejléc |
|---|---|
| HTML | `Cache-Control: public, max-age=0, must-revalidate` + `ETag` |
| CSS / JS (hash-elt fájlnév) | `public, max-age=31536000, immutable` |
| Fontok | `public, max-age=31536000, immutable` |
| Képek (hash-elt) | `public, max-age=31536000, immutable` |
| Egyéb | Brotli, HTTP/2, HSTS `max-age=31536000; includeSubDomains` |

A heti menü hetente változik, de a HTML `must-revalidate`-tel jön: a látogató
sosem lát múlt heti menüt gyorsítótárból.

### 9.5 Űrlap

Az akadálymentes foglalási űrlap a prototípusban működik:

- **Látható `<label>` minden mezőn** — nincs placeholder-only címke
- `type="tel"`, `type="date"`, `type="time"`, `type="number"` + `inputmode` — mobilon
  a helyes billentyűzet jön fel; `autocomplete="name"`, `autocomplete="tel"`
- **`novalidate`**, és a validáció **blur-re** fut, nem billentyűleütésre —
  gépelés közben nem hibázik rá az emberre
- A hibaüzenet **a mező alatt**, ikonnal + szöveggel (nem csak színnel),
  `aria-invalid` + `aria-describedby`
- Beküldéskor **hibaösszegző `role="alert"`-tel**, horgony-linkekkel a mezőkre,
  és a fókusz az első hibás mezőre ugrik
- **Az időpont a nyitvatartáshoz validál** — ugyanabból a `NYITVA` tömbből, amiből
  a táblázat és a kemence állapota. Ha valaki szerdán 22:30-at ír be:
  *„Szerdán 10:30 és 21:30 között tudunk asztalt adni — akkor még sül a rendelés
  zárásig."* Ez a validáció nem formai, hanem **üzemi**: a konyha zárás előtt
  30 perccel vesz fel utolsó rendelést
- Siker esetén `role="status"` panel, ami visszaolvassa a foglalás adatait, és
  **megmondja, hogy prototípusban nem ment el sehová** — nem hazudik visszaigazolást
- Élesben: szerveroldali validáció, honeypot + időbélyeg-ellenőrzés spam ellen
  (nem CAPTCHA — az akadálymentességi teher), e-mail a `gombocpizzeria@gmail.com`-ra

---

## 10. SEO-specifikáció

### 10.1 Title / meta minta

Sablon: `{Oldal} | Gömböc Pizzéria — Pécs, Kertváros`
(a telefonszám **kikerül** a globális tagline-ból — K2/S1)

| URL | `<title>` (≤60 karakter) | `<meta name="description">` (≤155) |
|---|---|---|
| `/` | `Gömböc Pizzéria — Pécs, Kertváros` | `Kemencében sült pizza, frissensültek és heti menü Pécs-Kertvárosban, 1983 óta. Nagy Imre út 70. Asztalfoglalás: 06 30 899 9303.` |
| `/etlap/` | `Étlap és árak \| Gömböc Pizzéria, Pécs` | `Kemencés pizzák, frissensültek, lepények, hamburger és gyros árakkal. Pécs, Nagy Imre út 70.` |
| `/heti-menu/` | `Heti menü \| Gömböc Pizzéria, Pécs-Kertváros` | `A menü 2 990 Ft, B menü 2 690 Ft, napi leves 900 Ft. Hétköznap 11:00–13:00, vagy amíg a készlet tart. Elvitelre is.` |
| `/kulonterem/` | `Különterem és kerthelyiség \| Gömböc Pizzéria` | `Zárt különterem céges ebédre, ballagásra, születésnapra Pécs-Kertvárosban, kerthelyiséggel. Előfoglalás: 06 30 899 9303.` |

### 10.2 Heading-hierarchia (főoldal)

```
h1  A kemence reggel óta megy. Mint 1983 óta minden nap.
├─ h2  Heti menü 11:00-tól 13:00-ig, vagy amíg a készlet tart
│   ├─ h3  A menü
│   ├─ h3  B menü
│   └─ h3  Napi leves önmagában
├─ h2  Pizza a kemencéből, mellette az, amit egy kertvárosi konyha tud
│   └─ h3 ×6  Kemencés pizza / Frissensültek / Lepények / Hamburger / Gyros / Koktélok…
├─ h2  Hétfőn és vasárnap 21:00-kor zárunk, egyébként 22:00-kor
├─ h2  Kerthelyiség nyáron, különterem egész évben
│   ├─ h3  Kerthelyiség
│   └─ h3  Különterem
├─ h2  Szóljatok előre, és lesz asztal
│   └─ h3  Megvan, elküldtük        (siker-panel)
└─ h2  Gömböc Pizzéria              (lábléc)
    ├─ h2  Elérhetőség
    └─ h2  Az oldalon
```

Egy H1, nincs kihagyott szint. A szemöldök-szövegek (`— HÉTKÖZNAP DÉLBEN`)
**`<p class="szemold">`**, nem álcímsorok — ez a leggyakoribb heading-hiba.

### 10.3 Strukturált adat — teljes gráf

A prototípusban egyetlen `@graph` fut, négy csomóponttal:

| `@type` | `@id` | Mit visz |
|---|---|---|
| `Restaurant` | `#etterem` | `name`, `url`, `telephone`, `email`, `address` (PostalAddress), `servesCuisine`, `priceRange` „4000–6000 Ft", `currenciesAccepted`, `foundingDate` **1983**, `openingHoursSpecification` (4 blokk), `amenityFeature` ×4 (kerthelyiség, különterem, kutyabarát, ingyenes parkolás), `acceptsReservations`, `hasMenu`, `aggregateRating` 4,6 / 1300 |
| `Menu` | `#heti-menu` | `hasMenuSection` → `MenuItem` ×3 `Offer`-rel (2990 / 2690 / 900 HUF) |
| `WebSite` | `#website` | `inLanguage: hu-HU`, `publisher` → `#etterem` |
| `WebPage` | `#fooldal` | `isPartOf` → `#website`, `about` → `#etterem` |

Aloldalakon bővül: `/etlap/` teljes `Menu` gráffal `MenuSection`-önként,
`/kulonterem/` `Service` + `BreadcrumbList`.

> **Figyelmeztetés az `aggregateRating`-re:** a Google szabályzata szerint saját
> oldalon megjelenített értékelés-összesítést **az oldalon látható módon is**
> közölni kell, és nem szabad harmadik fél (Google) értékelését sajátként
> feltüntetni. A prototípusban a 4,6 / 1 300 forrásmegjelöléssel („1300
> Google-értékelés") látszik. **Élesítés előtt ezt jogi/szabályzati szempontból
> validálni kell** — ez az anyag egyik nyitott kockázata (§15).

### 10.4 Local SEO — a listing mint csatorna

Ezen a piacon a **GBP a fő felület, a weboldal a bizonyíték mögötte.** Teendők
fontossági sorrendben:

1. **NAP-konzisztencia rendezése (S4/S5).** A weben két cím (Nagy Imre út **70.**
   vs **68.**) és két telefonszám kering. Ki kell választani a hivatalosat, és
   minden felületen (GBP, etterem.hu, pizza-etterem.hu, nyitva.hu, cylex, foodyas,
   Facebook, saját oldal, `schema.org/PostalAddress`) egységesíteni. Ez a
   **legolcsóbb és leghatásosabb** local ranking-lépés.
2. **A saját oldal legyen a NAP forrása**: a lábléc gépi és emberi olvasásra
   ugyanazt az adatot viszi, és a JSON-LD-vel egyezik.
3. GBP-poszt hetente a heti menüről, link a `/heti-menu/`-re.
4. Az étlap a saját oldalon legyen indexelhető szöveg, ne PDF és ne kép.
5. `hreflang` nem kell; `inLanguage: hu-HU` elég.

---

## 11. Performance-célok

Konkrét számok, 4G / Moto G4-osztályú mobilon, mezei látogatásnál:

| Metrika | Cél | Hogyan tartható |
|---|---|---|
| **LCP** | **< 1,2 s** (jó: < 2,5 s) | Az LCP-elem a H1 **szövege**. Nincs hero-kép, nincs képre váró render. A CSS inline a `<head>`-ben |
| **CLS** | **< 0,02** (jó: < 0,1) | Nulla kép a főoldalon; a fontok `swap`-pel, metrikailag közeli fallbackkel; minden animáció `transform`/`opacity` |
| **INP** | **< 100 ms** (jó: < 200 ms) | ~4,5 KB JS, nincs framework, nincs hydration. A legnehezebb művelet a táblázat egyszeri renderelése |
| **TTFB** | < 300 ms | statikus HTML, HTTP/2, Brotli |
| HTML (Brotli után) | **< 14 KB** | egy RTT-be fér |
| CSS | inline, < 12 KB | egyetlen fájl, nincs keretrendszer |
| JS | **< 5 KB** | a prototípusban ~4,5 KB tömörítetlenül |
| Font | 2 × ~28 KB | subsetelt variable woff2 |
| **Teljes főoldal-súly** | **< 90 KB** első betöltésre | a fenti összeg |
| Kérések száma | **≤ 5** | HTML + 2 font + favicon (+ 1 CSS, ha nem inline) |
| Lighthouse Performance | ≥ 98 | — |
| Lighthouse Accessibility | **100** | a §7.1 kontrasztok, fókuszgyűrűk, skip-link, ARIA |

Összevetésül: a kategória tipikus WP-főoldala 1,5–3 MB és 60–120 kérés.
A **< 90 KB / ≤ 5 kérés** nem optimista becslés, hanem annak a következménye,
hogy nincs hero-fotó és nincs keretrendszer.

---

## 12. CRO — konverziós elemek

| Elem | Hol | Miért működik |
|---|---|---|
| **Telefonszám a fejlécben, minden nézetben** | sticky fejléc | Ezen a piacon a telefon a valódi csatorna (§0.3). A vendég ötven százaléka nem akar űrlapot kitölteni, hanem szólni akar. Nem szabad az űrlap kedvéért elrejteni |
| **Fix alsó akciósáv mobilon** | < 940px, `safe-area-inset` | Mobilon a hüvelykujj-zóna alul van. Az „Asztalfoglalás / Hívás" pár a görgetés bármely pontján egy koppintásra van — ez a legnagyobb egyetlen konverziós tétel mobilon |
| **A Kemence + állapot-chip** | hero | Megválaszolja a *„nyitva vagytok most?"* kérdést kattintás nélkül. Ha zárva vagyunk, ezt őszintén megmondja — **a hamis „nyitva" több foglalást öl meg, mint amennyit hoz**, mert bizalmat veszít |
| **Ár a hajtás alatt közvetlenül** (2 990 / 2 690 / 900) | heti menü szekció | Az ár a legerősebb kvalifikáló. Aki elrejti, drágábbnak látszik. A 4 000–6 000 Ft-os GBP-sáv mellé a 2 690 Ft-os menü **lefelé nyitja** a közönséget |
| **Bizonyítéksor (1983 / 4,6 / 2 690 Ft)** | hero alja | Három különböző kifogásra válaszol egy sorban: *megbízható? jó? megfizethető?* A negyven év a legnehezebben másolható előny a piacon |
| **A „ma" sor kiemelése a nyitvatartásban** | nyitvatartás | Csökkenti a keresési munkát — a látogató a saját napját keresi, nem a hetet |
| **A telefon az űrlap mellett, nem alatta** | foglalás | Nem verseng, hanem választást ad. „Inkább telefonálok" gomb közvetlenül a beküldés mellett: aki elakad az űrlapon, nem távozik, hanem hív |
| **Nyitvatartás-alapú időpont-validáció** | űrlap | Megelőzi a hibás foglalást a beérkezés *előtt*. Egy visszautasított foglalás rosszabb élmény, mint egy azonnali, magyarázó hibaüzenet |
| **Sikerpanel a foglalás visszaolvasásával** | űrlap | Csökkenti a beküldés utáni bizonytalanságot, és tartalmazza a telefonszámot arra az esetre, ha mégis sürgős |
| **Különterem külön kártyán + külön űrlapágon** | terek / űrlap | A legmagasabb kosárértékű vendég (céges ebéd, ballagás) külön útvonalat kap. Ma nulla felülete van |

---

## 13. Design-döntések összefoglaló táblázata

| # | Döntés | Miért | Az elvetett alternatíva, és miért nem az |
|---|---|---|---|
| 1 | Vizuális kiindulópont: **a kemence anyagai** | Az ügyfél saját, dokumentált világából jön („helyben, kemencében sütött") | „Olasz pizzéria" jelmeztár: nem olasz hely, gyros és hamburger is van az étlapon |
| 2 | Paletta: samott / parázs / hamu / lomb | A kiindulóponttal koherens, és a `--parazs` egyszerre CTA és fizikai jelentés | Étterem = piros automatizmus: kategória-alapú, nem hely-alapú, és megkülönböztethetetlen |
| 3 | **Fraunces + Figtree** | 1983-as kor-rezonancia + hangolható különcség; mindkettő variable, latin-ext | Playfair + Inter (tiltott, és mai alapértelmezés); Playfair SC + Karla (a skill ajánlása — ugyanaz a csapda) |
| 4 | Szignatúra: **A Kemence élő állapotjelzőként** | Megmutatja a lényeget (a tűz ég vagy nem), nem elmondja; nem fotón múlik; 0 hálózati bájt | Hero-fotó (LCP-teher, jogtisztaság); tésztagombóc-morph (dekoráció); élő asztalfoglaltság (nem lesz karbantartva) |
| 5 | **Nincs kép a főoldalon** | LCP < 1,2 s, CLS < 0,02, és fotó nélkül sem törik el semmi | Galéria: karbantartás nélkül azonnal elavul |
| 6 | **4 URL**, `/kapcsolat/` megszüntetve | Karbantarthatóság; a kapcsolat a konverzió helye, nem külön lépés | 8–12 oldalas „teljes" site: az üzemeltető nem fogja karbantartani (§3.1) |
| 7 | **A heti menü kiemelése a „Hírek"-ből** | Két külön szándék, két külön URL; heti frissítésű, visszatérő közönség | Együtt hagyás: a jelenlegi `/heti-menu-hirek/` mindkettőt rontja |
| 8 | **A telefon egyenrangú az űrlappal** | Ez a piac valódi csatornája; az űrlap nem helyettesíti | „Csak űrlap" (modernebbnek látszik, kevesebbet konvertál) |
| 9 | Elevation csak megnyomható elemeken | Az árnyék jelentést hordoz, nem díszít | Egységes árnyék minden kártyán: ellaposítja a hierarchiát |
| 10 | **Három téma-állapot** kezelése (light / dark / rendszerkövető) | A rendszerkövető állapot a leggyakoribb, és a legtöbb megvalósítás pont ezt rontja el | Csak `prefers-color-scheme`: a kézi váltó nem tud felülbírálni |
| 11 | Belépő animáció **csak a hajtás alatti** elemekre, JS-ből | Az oldal nyugalmi állapotban teljes; JS nélkül is minden látszik | CSS-ből `opacity: 0` + observer: JS-hiba esetén üres oldal |
| 12 | **Nincs 01/02/03 számozás** | Az oldalon nincs valódi sorrend | Számozás mint dísz: hamis szerkezeti információ |
| 13 | Egy adatforrás a nyitvatartásra (`NYITVA` tömb) | A táblázat, a kemence állapota és az űrlap-validáció **nem tud szétcsúszni** | Három helyen leírt nyitvatartás: garantáltan elavul valamelyik |
| 14 | **WordPress megtartva** saját sablonnal | Az ügyfél ismeri, és magának kell frissítenie a heti menüt | Statikus generátor: build-lánc, amit nincs ki üzemeltessen |
| 15 | Ikonok: kézzel rajzolt SVG-készlet | Egységes vonalvastagság, `currentColor`, témakövető, ~1,4 KB | Ikon-könyvtár (fölösleges kB); emoji (platformfüggő, nem tokenezhető) |

---

## 14. Bevezetési ütemterv

| Fázis | Tartalom | Feltétel | Becsült ráfordítás |
|---|---|---|---|
| **0. Azonnali, a redesign előtt** | HTTPS + HSTS bekapcsolása és kikényszerítése (K1); a telefonszám kivétele a site-title-ből (K2); NAP-konzisztencia rendezése minden listingen (S4/S5) | hoszting- és GBP-hozzáférés | 0,5 nap |
| **1. Tartalmi feltárás** | Teljes étlap tételes árakkal, különterem-kapacitás és feltételek, kiszállítás/fizetés tisztázása, adatkezelési tájékoztató, fotók (opcionális) | **ügyfél-input, §15** | ügyfélfüggő |
| **2. Design system + főoldal** | A jelen anyag tokenjei WP blokk-témába; a főoldal élesítése a prototípus alapján | 1. fázis lezárva | 3–4 nap |
| **3. Aloldalak** | `/etlap/`, `/heti-menu/`, `/kulonterem/` + 301-ek a régi URL-ekről | 2. fázis | 2–3 nap |
| **4. Heti menü munkafolyamat** | Egyszerű szerkesztőfelület a heti menüre, hogy karbantartás nélkül se avuljon el; GBP-poszt sablon | 3. fázis | 1 nap |
| **5. Mérés és élesítés** | Lighthouse + valós CWV, schema-validáció, űrlap-végpont, akadálymentességi átnézés (billentyűzet, képernyőolvasó, reduced-motion) | 4. fázis | 1 nap |
| **6. Utánkövetés, 4 hét** | GBP-forgalom, foglalások száma, heti menü oldalletöltések | élesítés után | — |

**301-térkép:**
`/etlap-3/ → /etlap/` · `/heti-menu-hirek/ → /heti-menu/` · `/kapcsolat/ → /#foglalas`
· minden `http://` → `https://`

---

## 15. Nyitott kérdések — ehhez ügyfél-input kell

**Blokkoló (enélkül nem élesíthető):**

1. **A cím: Nagy Imre út 70. vagy 68.?** A weben mindkettő fut. A prototípus a
   70-est használja (GBP + nyitva.hu), de ezt meg kell erősíteni.
2. **A telefonszám: a 06 30 899 9303 az egyetlen érvényes?** A +36 72 440 456 még
   több listingen él.
3. **Teljes étlap tételes árakkal.** A prototípus csak a heti menü árait hozza,
   mert csak azok dokumentáltak.
4. **A heti menü árai ma is 2 990 / 2 690 / 900 Ft?** A forrás egy aggregátor-listing,
   dátum nélkül.
5. **Adatkezelési tájékoztató** — az űrlap enélkül nem mehet élesbe.
6. **Hová menjen a foglalási űrlap?** E-mail, és ha igen, ki nézi munkaidőben?
7. **Az `aggregateRating` megjelenítése a saját oldalon** — a 4,6 / 1 300 a Google
   adata; szabályzati validáció kell (§10.3).

**Fontos (a tartalmat érinti):**

8. **Különterem: hány fő?** Van-e minimális fogyasztás, előfoglalási feltétel?
9. **Kerthelyiség: hány fő, mettől meddig üzemel?**
10. **Van-e kiszállítás?** Ha igen: milyen körzet, milyen díj, milyen platform?
11. **Fizetés:** kártya, SZÉP-kártya, utalvány?
12. **A heti menü napi fogásai** — hogyan és ki frissíti hetente?
13. **A „Kedvezményes ételek" GBP-attribútum** mit takar konkrétan?
14. **Van-e jogtiszta fotó** a kemencéről, a kerthelyiségről, a különteremről?
    (Nem blokkoló — az oldal fotó nélkül is teljes, §9.3.)

**Stratégiai (a brief üresen hagyott mezői):**

15. **Célközönség:** kik jönnek ma? Kertvárosi családok, környékbeli munkahelyek
    déli forgalma, esti baráti társaságok — melyik a legfontosabb?
16. **Verseny:** kiket tekint a Gömböc versenytársnak Kertvárosban?
17. **Van-e arculati kötöttség?** Logó, betűtípus, szín, amihez ragaszkodni kell?
    A prototípus **szöveges szóvédjegyet** használ, mert a meglévő logót nem láttam.
18. **Az oldal jelenlegi forgalma és forrásmegoszlása** (GA / GSC hozzáférés).

---

## 16. Az anyag leggyengébb pontja — őszintén

**A §1.1, a technológiai elemzés.** Nem tudtam lekérni a `gombocpizzeria.hu`-t:
minden hozzáférési kísérlet egress-blokkba futott. Amit a jelenlegi oldal
technológiájáról állítok, azt **indexelt URL-ekből és title-ökből** olvastam ki.
A „WordPress" következtetés az `/etlap-3/` slug-ütközésen és a
`/heti-menu-hirek/` szerkezeten áll — ez valószínű, de nem bizonyított. A `http://`
séma az indexelt linkekben erős jel, de az sem kizárt, hogy azóta bekapcsolták a
HTTPS-t, és csak az index régi. **A §2.4 performance-szakaszban ezért nincs
egyetlen valós mérési szám sem** — csak strukturális kockázatok és a §11
célszámai. Egy fél napos, hozzáféréssel végzett audit ezt a szakaszt teljesen
átírhatja, és elvben megdöntheti a §9.1 stack-döntését is (ha például kiderül,
hogy nem WordPress fut rajta).

**A második leggyengébb pont: az étlap.** A prototípus mindössze három árat
mutat — a heti menüét —, mert csak ezek dokumentáltak. Egy pizzéria főoldalán ez
kevés: a látogató pizzaárat keres. Ezt szándékosan nem pótoltam kitalált
számokkal, de emiatt a §5.2 `/etlap/` oldala **jelenleg specifikáció, nem
tartalom.**

**A harmadik: a célközönség-állítások.** A §12 CRO-táblázatában olyan
viselkedési feltevések vannak („a vendég fele nem akar űrlapot kitölteni"),
amelyek a kategóriára általánosan igazak, de **erre a helyre nincsenek mérve.**
Az élesítés utáni négy hét (§14/6) az első alkalom, amikor ezek ellenőrizhetők.

---

### Források

A dokumentum a következő, keresővel indexelt forrásokból rekonstruált tényekre épül:

- [Gömböc Pizzéria — hivatalos oldal (indexelt)](http://gombocpizzeria.hu/) · [Étlap](http://gombocpizzeria.hu/etlap-3/) · [Heti menü / Hírek](http://gombocpizzeria.hu/heti-menu-hirek/) · [Kapcsolat](http://gombocpizzeria.hu/kapcsolat/)
- [pecsma.hu — „Ezért szeretik Kertvárost – Gömböc Pizzéria"](https://www.pecsma.hu/ezert-szeretik-kulvarost-gomboc-pizzeria/) (1983, család, Fauszt Gábor 2010 óta)
- [etterem.hu — Gömböc](https://etterem.hu/gomboc) · [gastro.hu](https://gastro.hu/helyek/gomboc-pizzeria) (kínálat, kerthelyiség, kutyabarát)
- [nyitva.hu](https://nyitva.hu/p%C3%A9cs/g%C3%B6mb%C3%B6c-pizz%C3%A9ria-146842) (nyitvatartás, cím)
- [menuzz.hu](https://menuzz.hu/etterem/gomboc-pizzeria-napi-menu-pecs-heti-menu-pecs/) (heti menü árai, 11:00–13:00 sáv, csomagolás)
- [pizza-etterem.hu](https://www.pizza-etterem.hu/pizzeria/gomboc-pizzeria-pecs) · [foodyas.com](https://www.foodyas.com/HU/P%C3%A9cs/448235732030698/G%C3%B6mb%C3%B6c-Pizz%C3%A9ria) · [cylex](https://xn--pcs-bma.cylex.hu/ceg-info/g%C3%B6mb%C3%B6c-pizz%C3%A9ria-979278.html)
- Google Business Profile-kivonat a feladatkiírásból (4,6 ★ / 1,3 E, 4 000–6 000 Ft, különterem, koktélok, „Bejelentette 130 személy")
