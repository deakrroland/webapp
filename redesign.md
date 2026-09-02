# Giovanni Pizzéria, Pécs — UI/UX redesign koncepció és prototípus

> **Módszertani figyelmeztetés — rekonstrukcióból dolgoztam.**
> A `https://hovamenjek.hu/pecs/giovanni-pizzeria`, a `https://giovannipecs.hu`, az
> `etterem.hu`, a `foodora.hu` és az `ittjartam.hu` közvetlen lekérése ebben a
> környezetben hálózati szinten tiltott (egress proxy: `EGRESS_BLOCKED`). Az
> elemzés a keresőben indexelt tartalomra és a briefben beillesztett listing-szövegre
> épül. Minden ténymegállapítás mellett jelzem a forrást és a bizonyosság szintjét.
> **Élesítés előtt a §15 ellenőrzőlistáját le kell futtatni az élő oldalon.**

> **Hatókör-korrekció (fontos, olvasd el).**
> A megadott URL nem az ügyfél saját oldala, hanem egy **aggregátor-listing**
> (hovamenjek.hu), amelynek tartalma láthatóan a Google Cégprofil adatait tükrözi
> (értékelés, „Zárva · Nyitás: 12:00", „Hívás / Útvonal / Webhely / Megosztás /
> Mentés" gombsor, attribútum-chipek). Egy nem birtokolt aggregátor-oldalt
> újratervezni nem szállítható munka: nincs hozzáférés a kódhoz, és a layoutot a
> platform diktálja. Ezért a brieffet így értelmezem, és így is szállítom:
>
> 1. **Elemzem a listinget** mint a jelenlegi digitális jelenlét *tényleges belépőpontját* (§1–3).
> 2. **A redesign tárgya az ügyfél saját webhelye, a `giovannipecs.hu`** (§4–14) — ez az,
>    amire a listing „Webhely" gombja mutat, és amit a listing forgalmát fogadva
>    konvertálnia kellene.
> 3. **A listinget mint csatornát optimalizálom** (§10.4 Local SEO), nem mint felületet.
>
> Ha az ügyfél tényleg a hovamenjek-listing átalakítását kérte, az egy másik,
> jóval szűkebb feladat (adatpontosítás + fotófeltöltés), és szólj — átírom.

---

## 0. Kontextus — amit tudok, és amit nem

A briefben a kontextusmezők üresen maradtak. Az alábbi táblázat **csak dokumentált
tényeket** tartalmaz; ami hiányzik, az a §15-ben kérdésként szerepel. Számot,
kapacitást, árat sehol nem találtam ki.

| Mező | Amit tudok | Forrás / bizonyosság |
|---|---|---|
| Ügyfél | Giovanni Pizzéria, Pécs, Nagy Imre út 43., 7632 (Kertváros) | listing + `giovannipecs.hu/elerhetoseg/` · **magas** |
| Telefon | (06 72) 446 000 | listing + cégadatbázisok · **magas** |
| Saját webhely | `giovannipecs.hu` — ismert URL-ek: `/`, `/etlap/`, `/itallap/`, `/elerhetoseg/` | keresőindex · **magas** |
| Konyha | pizza, roston sültek, levesek, salátáink | foodora + saját oldal szövege · **magas** |
| Csapolt | Staropramen, Stella Artois, Jägermeister | saját oldal szövege (idézett) · **közepes** |
| Szórakozás | biliárd, csocsó, darts, flipper | saját oldal szövege; `etterem.hu` biliárd+darts+TV-t erősít meg · **közepes** |
| Tér | terasz (nyáron), „kisebb összejövetelekre alkalmas"; a Google-attribútumok szerint **különterem** és **szabadtéri asztalok** | saját oldal + listing · **közepes** |
| Értékelés | Google 4,5 ★ / ~1 339–1 400 vélemény; foodora 4,7 ★ / 206 vélemény | listing + foodora · **közepes** (a szám naponta változik) |
| Ársáv | 2 000–6 000 Ft / fő | Google-attribútum · **közepes** |
| Nyitás | minden nap 12:00; zárás H–Cs 23:00, P–Szo 24:00, V 22:00 | nyitvatartás-aggregátorok · **alacsony — ellenőrizni kell** |
| Kiszállítás | foodora (két külön listing: „Giovanni Pizzéria" és „Giovanni étterem") | foodora · **közepes** |

**Munkahipotézisek** (a §15-ben megerősítendők, addig ezek alapján dolgoztam):

- **Az oldal EGY dolga: asztalfoglalás** (másodlagos, egyenrangú kimenet: telefonhívás).
  Indok: van terasz, különterem és játéksarok — ezek *helyhez kötött* értékek, amiket
  kiszállítással nem lehet monetizálni; a kiszállítást a foodora amúgy is elviszi,
  saját rendelési motort építeni ehhez a mérethez rossz ROI (§13).
- **Célközönség:** (a) kertvárosi családok és baráti társaságok 25–55, hétköznap
  este, „hova üljünk le enni, ahol a gyerek is elvan"; (b) 18–30, hétvégén, csocsó
  + csapolt sör; (c) csoportszervező, aki *egy* konkrét dolgot keres: „elfér-e 20 fő".
- **Amit nem szabad megváltoztatni:** a „Giovanni" márkanév, a telefonszám, a cím,
  és a már indexelt `/etlap/`, `/itallap/`, `/elerhetoseg/` URL-ek.

---

## 1. A jelenlegi állapot elemzése

### 1.1 Technológia

| Réteg | Megállapítás | Bizonyíték |
|---|---|---|
| Listing (hovamenjek.hu) | szerveroldali sablon Google-adatokból; a beillesztett szöveg pontosan a Google Cégprofil mezőstruktúráját követi | a brief szövege: értékelés → ársáv → kategória → állapot → akciógombok → attribútum-chipek → cím → térképhivatkozás |
| Saját webhely | **nagy valószínűséggel WordPress** | a címformátum `Elérhetőség – Giovanni Pizzéria` a WP alapértelmezett `–` elválasztója; a permalinkek záró perjeles, ékezet nélküli slugek (`/elerhetoseg/`, `/etlap/`, `/itallap/`) = WP „post name" struktúra · **inferencia, ellenőrizendő** |
| Struktúra | lapos, 4–5 oldalas brosúra: főoldal + Étlap + Itallap + Elérhetőség | keresőindex · **magas** |
| Mérhetőség | nincs adatom analitikáról, konverziókövetésről | **ismeretlen** |

### 1.2 A jelenlegi tartalom szerkezete (rekonstruált)

```
Listing:  név → 4,5★(1,4E) → ársáv → kategória → állapot(Zárva/Nyitás 12:00)
          → fotógaléria (pl. „Málnás Lávasüti") → [Hívás][Útvonal][Webhely][Megosztás][Mentés]
          → chipek: Szabadtéri asztalok · Különterem · Nagyszerű koktélok
          → cím → térkép → nyitvatartás → ársáv → telefon
Saját:    Főoldal (bemutatkozó bekezdés) → Étlap → Itallap → Elérhetőség
```

### 1.3 MI A JÓ BENNE — külön szedve, és amit megtartok

Ezeket **nem** dobom el, mert működnek:

| Ami jó | Miért jó | Mi lesz vele |
|---|---|---|
| **4,5 ★ / ~1 339 vélemény** | Ez a legértékesebb digitális eszközük. Egy pécsi kertvárosi pizzériánál az 1 300+ vélemény évekre visszamenő, hitelesíthetetlenül nagy bizalmi tőke. | **Felkerül a hajtás fölé, forrásmegjelöléssel, szövegként.** Nem schema-ban (§10.3 — okkal). |
| **Egy telefonszám, ami tényleg fel van véve** | Az étterem-szegmens konverzióinak nagy része továbbra is hívás. | Sticky mobil sávban, `tel:` linkkel, minden aloldalon. |
| **Világos, ékezetmentes, záró perjeles permalinkek** | SEO-szempontból korrekt, indexelt, működik. | **Megmarad**: `/etlap/`, `/itallap/`, `/elerhetoseg/` változatlan URL-en. |
| **Az étlap külön oldalon van** | Az étlap a legkeresettebb tartalom; saját URL-je indexelhető és linkelhető. | Megmarad, kap `Menu` schema-t és horgonyokat. |
| **Rövid, emberi hangú bemutatkozó szöveg** („Pécs Kertvárosában köszöntjük vendégeinket", biliárd, csocsó, darts, flipper, csapolt sörök) | Ez **konkrét és igaz** — pont az ellenkezője a szokásos „családias hangulat, kiváló minőség" vattának. | **A szövegvilág alapja marad.** A redesign nem írja felül, hanem előrehozza. |
| **Foodora-jelenlét (4,7 ★)** | Kiszállítás megoldva, nem kell saját rendszert építeni. | Kimenő link marad, de nem elsődleges CTA (§13). |
| **Egyértelmű, egyszavas menüpontok** | „Étlap", „Itallap", „Elérhetőség" — nulla kognitív teher. | Megmaradnak, kiegészülnek. |

### 1.4 Amit a listing tud, és a saját oldal nem mond el

A Google-attribútumok (**Különterem**, **Szabadtéri asztalok**, **Nagyszerű koktélok**)
és a saját oldal szövege (**csapolt sör, biliárd, csocsó, darts, flipper**) **két
különböző helyet írnak le**. Ez a legnagyobb egyedi tartalmi tartalék: a különterem
és a koktélok sehol nincsenek kifejtve a saját oldalon, pedig a különterem az egyetlen
olyan termék, amit *nem* lehet foodorán megvenni.

---

## 2. Problémalista bizonyítékkal

Súlyosság: **K** = kritikus (pénzt visz), **UX**, **SEO**, **PERF**.

| # | Súly | Probléma | Bizonyíték |
|---|---|---|---|
| P1 | **K** | Nincs asztalfoglalási útvonal. A Google-listing 5 akciógombja közül egy sem foglalás; a saját oldalon sincs nyoma. | listing gombsora: Hívás / Útvonal / Webhely / Megosztás / Mentés — nincs „Foglalás" |
| P2 | **K** | A **különterem** mint termék nem létezik digitálisan: nincs oldala, nincs kapacitása, nincs ára, nincs kérőűrlapja. | a `giovannipecs.hu` ismert URL-jei között nincs ilyen; a Google mégis attribútumként hozza |
| P3 | **K** | A nyitvatartás csak harmadik felek adatbázisában él megbízhatóan; a felhasználó az oldalon nem kap **most érvényes** választ arra, hogy nyitva van-e. | az aggregátorok eltérő zárásokat közölnek; a listing dinamikus („Zárva · Nyitás: 12:00"), a saját oldal statikus |
| P4 | **K** | Két külön foodora-listing („Giovanni Pizzéria" és „Giovanni étterem") ugyanarra a márkanévre — a vendég nem tudja, melyiket válassza. | foodora URL-ek: `/restaurant/z28z/...` és `/restaurant/xxsj/...` |
| P5 | UX | A tartalom brosúra-logikájú (Rólunk → Étlap → Elérhetőség), nem döntés-logikájú (Mikor? Hol ülünk? Mennyi? Hogyan foglalok?). | a 4 oldalas sitemap maga a bizonyíték |
| P6 | UX | A játéksarok (biliárd, csocsó, darts, flipper) egy felsoroló mondatban van elrejtve, pedig ez a fő megkülönböztető. | a bemutatkozó szöveg szerkezete |
| P7 | UX | Nincs allergén- és összetevő-információ, nincs vegetáriánus/gluténmentes szűrő az étlapon. | az `/etlap/` egyoldalas listaként indexelt |
| P8 | SEO | A `title` a WP alapértelmezése (`Oldalcím – Márkanév`) — nincs benne város, kategória, se differenciátor. | `Elérhetőség – Giovanni Pizzéria`, `Étlap – Giovanni Pizzéria` |
| P9 | SEO | Nincs (vagy nem teljes) `Restaurant` strukturált adat: nyitvatartás, menü, geo, akadálymentesség. | a listing a Google-profilból, nem az oldalról építkezik |
| P10 | SEO | Nincs helyi kulcsszóra épített landing („pizza rendelés Pécs Kertváros", „különterem Pécs 20 fő", „csocsó Pécs"). | a foodora `/city/pecs/area/kertvaros/52/cuisine/pizza` kategóriaoldala rangsorol e helyett |
| P11 | PERF | WordPress-alapon, téma + pluginok mellett tipikusan 1,5–3 MB-os főoldal, render-blokkoló CSS/JS. | inferencia a stackből — **méréssel igazolandó** (§15) |
| P12 | PERF | Az ételfotók nagy valószínűséggel méretezetlen JPEG-ek, `width`/`height` nélkül → CLS. | inferencia — **méréssel igazolandó** |
| P13 | UX/A11y | Nincs adat billentyűzet-navigációról, fókuszgyűrűkről, kontrasztról. | **méréssel igazolandó** |

---

## 3. Miért rosszak ezek — a mögöttes ok, nem a tünet

**Ok #1 — Az oldal a vendéglátóst írja le, nem a vendég döntését segíti.**
A P5, P6, P2 mind ugyanaz. A brosúra-struktúra abból a feltevésből él, hogy a vendég
„meg akar ismerni minket". Nem akar. Egy konkrét, szűk döntést hoz, adott
lelkiállapotban: *ma este hova üljünk le hatan úgy, hogy legyen terasz és ne kerüljön
20 ezerbe*. Minden szekció, ami nem ezt a döntést gyorsítja, súrlódás.

**Ok #2 — Az étterem digitálisan a saját közvetítőit erősíti, nem magát.**
A P1, P4, P10 közös gyökere: a foglalást a Google, a rendelést a foodora, a
véleményeket a hovamenjek/ittjartam birtokolja. Minden konverzió platformon
történik, jutalékkal és nulla vendégadattal. A saját oldalnak nem „szebbnek" kell
lennie — **birtokolnia kell legalább egy konverziót**, és a legvédhetőbb ez a
foglalás, mert a foodora ezt nem tudja elvenni.

**Ok #3 — A legdrágább termék láthatatlan.**
P2. A különterem az egyetlen olyan tétel, aminek magas a fajlagos árbevétele
(csoportos foglalás, előre tervezett, magas italfogyasztás), és az egyetlen, amit
kiszállítással nem lehet helyettesíteni. Digitálisan nem létezik. Ez nem
design-, hanem termékportfólió-hiba, amit designnal lehet javítani.

**Ok #4 — A „nyitva van-e" kérdés a legelső, és a legrosszabbul megválaszolt.**
P3. Egy étterem oldalán az első mikrokonverzió nem a hangulat, hanem az idő. Ha ezt
a választ a Google adja meg és nem az oldal, akkor a felhasználónak nincs oka
átjönni az oldalra. A statikus nyitvatartási táblázat nem válasz: fordítást
követel a felhasználótól („most 21:40 van, kedd, ez akkor még nyitva?").

**Ok #5 — A technológiai teher nem választás, hanem örökség.**
P11–P13. Egy 4 oldalas brosúra alá általános célú CMS-t rakni azt jelenti, hogy
minden látogató kifizeti egy blogmotor futásidejét. Nem a WordPress rossz — a
*méretezés* rossz.

---

## 4. Új információs architektúra és sitemap

Elv: **egy URL = egy vendégkérdés.** Nem tartalomtípus szerint bontok, hanem
döntési pont szerint.

```
/                          Főoldal — „nyitva vagytok, hol ülök, mit eszem, foglalok"
├─ /etlap/                 [MEGTARTOTT URL] Étlap — szűrhető, allergénnel
│   └─ /etlap/#pizzak      horgony, nem külön URL
├─ /itallap/               [MEGTARTOTT URL] Itallap — csapolt sörök, koktélok
├─ /asztalfoglalas/        Foglalás — az egyetlen űrlap teljes oldalon
├─ /kulonterem/            Különterem és rendezvény — a hiányzó termékoldal
├─ /jatekterem/            Biliárd, csocsó, darts, flipper — a differenciátor
├─ /elerhetoseg/           [MEGTARTOTT URL] Cím, nyitvatartás, megközelítés, parkolás
├─ /allergenek/            Allergéntáblázat
├─ /impresszum/            Kötelező
└─ /adatkezeles/           Kötelező (foglalási űrlap → GDPR)
```

**URL-enkénti indoklás:**

| URL | Miért van | Miért nem másképp |
|---|---|---|
| `/` | A listing „Webhely" gombjának landolása. Egyetlen dolga: állapot + foglalás. | Alternatíva: a `/` legyen az étlap. Elvetve — az étlapot linkelik és mentik, saját URL-t érdemel. |
| `/etlap/` | Már indexelt, már ez a legkeresettebb aloldal. | Alternatíva: kategóriánként külön URL (`/etlap/pizzak/`). Elvetve — ~4 kategóriánál ez vékony tartalmú oldalakat szülne, és megtörné a „végiggörgetem az egészet" mintát. Horgonyok elegek. |
| `/itallap/` | Már indexelt; a csapolt sör és a koktél külön keresési szándék. | Elvetve az `/etlap/`-ba olvasztás: külön indexelt URL-t megölni ok nélkül SEO-veszteség. |
| `/asztalfoglalas/` | A konverziónak saját, linkelhető, hirdethető, mérhető URL kell (Google Cégprofil „Foglalás" link, QR a asztalokon). | Alternatíva: csak modal a főoldalon. Elvetve — nem linkelhető, nem mérhető, nem oszthatóformában. |
| `/kulonterem/` | A legmagasabb értékű, jelenleg nem létező termék. Saját keresési szándék: „különterem Pécs", „céges vacsora Pécs". | Alternatíva: bekezdés az „Elérhetőség" alján. Elvetve — nem rangsorol, és nem lehet rá hirdetni. |
| `/jatekterem/` | Ez a márka egyedi eszköze. Külön szándék: „csocsó Pécs", „biliárd Pécs". | Alternatíva: hazai szekció a főoldalon. Részben megmarad: a főoldalon van kivonat, a mélytartalom itt. |
| `/allergenek/` | Jogszabályi elvárás + valós vendégkérdés; külön URL-en frissíthető anélkül, hogy az étlaphoz nyúlnánk. | Alternatíva: PDF. Elvetve — a PDF nem indexelhető jól, mobilon rossz, nem akadálymentes. |

**Amit szándékosan NEM építek meg:** saját rendelési/fizetési rendszer. Indok:
a foodora már működik 4,7 ★-gal; egy saját checkout fejlesztése, PCI-terhe és
karbantartása nincs arányban egy kertvárosi pizzéria volumenével. Ha ez mégis cél,
az külön projekt (§15).

---

## 5. Oldalankénti felépítés

### 5.1 Főoldal (`/`) — ez készül el prototípusként

| # | Szekció | Cél | Kulcselem | CTA |
|---|---|---|---|---|
| 0 | Skip-link + fejléc | navigáció, azonnali hívás | logó, 5 menüpont, `tel:` | „Asztalt foglalok" |
| 1 | Hajtás (hero) | „nyitva vagytok?" + „mi ez a hely?" | H1, **élő állapotjelző** (nyitva/zárva, óráig pontosan), 3 tényadat | 2 egyenrangú: Foglalás / Hívás |
| 2 | **Alaprajz** (szignatúra) | „hol fogok ülni?" | interaktív SVG zónatérkép, 4 zóna | zónaválasztás → űrlap előtöltése |
| 3 | Étlap-kivonat | „mit eszem, mennyiért?" | 4 kategória + ársáv | „Teljes étlap" → `/etlap/` |
| 4 | Csapolt és koktél | italkínálat, ami a listingben highlight | 3 nevesített csapolt tétel | „Itallap" → `/itallap/` |
| 5 | Játéksarok | differenciátor | 4 saját rajzú SVG ikon | „Mi van még" → `/jatekterem/` |
| 6 | Különterem | csoportos foglalás | kapacitás (placeholder), mire jó | „Ajánlatot kérek" → űrlap, tárgy előtöltve |
| 7 | Vélemények | bizalom | 4,5 ★ / 1 339, **forrásmegjelöléssel** | „Olvasd el a Google-on" |
| 8 | Foglalási űrlap | **a konverzió** | 6 mező, inline validáció | „Foglalás elküldése" |
| 9 | Gyakori kérdések | súrlódásoldás | 5 kérdés | — |
| 10 | Elérhetőség | hely + idő | cím, térképlink, nyitvatartási táblázat | „Útvonal" |
| 11 | Lábléc | jog, kapcsolat | impresszum, adatkezelés, közösségi | — |
| — | Mobil sticky sáv | mindig elérhető konverzió | „Hívás" + „Foglalás" | — |

### 5.2 `/etlap/`

| # | Szekció | Cél |
|---|---|---|
| 1 | H1 + rövid vezető | „Étlap — Giovanni Pizzéria, Pécs Kertváros" |
| 2 | Szűrősor (chip) | Mind / Pizzák / Roston sültek / Levesek / Saláták / Vegetáriánus |
| 3 | Kategórialisták | tételnév, rövid összetevő-sor, ár, allergénkód |
| 4 | Allergén-jelmagyarázat | link `/allergenek/`-re |
| 5 | Kiszállítás-sáv | foodora-link, egyértelműsítve, melyik listing |
| 6 | CTA | „Inkább itt eszünk → Foglalás" |

### 5.3 `/kulonterem/`

| # | Szekció | Cél |
|---|---|---|
| 1 | H1 + kapacitásadat | „Különterem Pécsen — [X] főig" *(placeholder)* |
| 2 | Mire jó | céges vacsora, ballagás, szülinap, klubest |
| 3 | Mi jár hozzá | asztalrend, projektor?, zene?, minimumfogyasztás? *(mind placeholder)* |
| 4 | Menüajánlatok | fix csomagok *(placeholder árakkal)* |
| 5 | Ajánlatkérő űrlap | dátum, létszám, alkalom, kapcsolat |
| 6 | GYIK | lemondás, előleg, saját torta |

### 5.4 `/jatekterem/`, `/itallap/`, `/elerhetoseg/`, `/allergenek/`
Egyszerű, egy-célú oldalak: H1 → tényleges tartalom → egy CTA. Nincs hero,
nincs karusszel.

---

## 6. Wireframe

### 6.1 Desktop (≥1024px)

```
┌───────────────────────────────────────────────────────────────────────────┐
│ [skip a tartalomra]                                                       │
├───────────────────────────────────────────────────────────────────────────┤
│ GIOVANNI   Étlap  Itallap  Játékterem  Különterem  Kapcsolat              │
│                                    (06 72) 446 000   [ Asztalt foglalok ] │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ● MOST NYITVA · zárás 23:00-kor          H1                              │
│  ┌──────────────────────────────┐   Pizza, csapolt sör és csocsó          │
│  │                              │   Pécs Kertvárosában.                   │
│  │   Nagy Imre út 43. óta       │                                         │
│  │   ugyanaz a cím.             │   Lead: 2 mondat, konkrét.              │
│  │                              │                                         │
│  │  [ Asztalt foglalok ]        │   ┌──────┬──────────┬─────────────┐     │
│  │  [ (06 72) 446 000 ]         │   │ 4,5★ │ 2–6 e Ft │ Nyitás 12:00│     │
│  └──────────────────────────────┘   │ 1339 │  / fő    │  minden nap │     │
│                                     └──────┴──────────┴─────────────┘     │
├───────────────────────────────────────────────────────────────────────────┤
│  SZIGNATÚRA — „Hol ülnél?"  (interaktív alaprajz, inline SVG)             │
│                                                                           │
│  ┌─────────────────────────────────────────────┐  ┌─────────────────────┐ │
│  │  ─ ─ ─ utca felőli oldal ─ ─ ─              │  │ TERASZ              │ │
│  │  ┌───────────┐  ┌────────────────────────┐  │  │ Utca felőli kiülős  │ │
│  │  │  TERASZ   │  │ BELSŐ TÉR              │  │  │ rész.               │ │
│  │  │ • • • •   │  │ ▭ ▭ ▭ ▭                │  │  │ [X] asztal (egyezt.)│ │
│  │  │ • • • •   │  │ ▭ ▭ ▭ ▭      ▂▂▂ pult  │  │  │                     │ │
│  │  └───────────┘  └────────────────────────┘  │  │ [ Ide foglalok ]    │ │
│  │        ┃ bejárat                            │  └─────────────────────┘ │
│  │  ┌───────────┐  ┌────────────────────────┐  │                          │
│  │  │ JÁTÉK-    │  │ KÜLÖNTEREM             │  │  (a jobb oldali panel a  │
│  │  │ SAROK     │  │ ○○○○○                  │  │   kijelölt zónához       │
│  │  │ ▭biliárd  │  │ ▭▭▭▭▭ hosszú asztal    │  │   frissül; a kiválasztás │
│  │  │ ⌗csocsó   │  │ ○○○○○                  │  │   előtölti az űrlapot)   │
│  │  │ ◎darts    │  └────────────────────────┘  │                          │
│  │  │ ⬡flipper  │                              │                          │
│  │  └───────────┘  ─ sematikus, nem méretarányos ─                        │
│  └─────────────────────────────────────────────┘                          │
├───────────────────────────────────────────────────────────────────────────┤
│  ÉTLAP-KIVONAT            ┌────────┐┌────────┐┌────────┐┌────────┐        │
│                           │ Pizzák ││ Roston ││ Levesek││Saláták │        │
│                           │ [ár]   ││ [ár]   ││ [ár]   ││ [ár]   │        │
│                           └────────┘└────────┘└────────┘└────────┘        │
│                                              [ Teljes étlap → ]           │
├───────────────────────────────────────────────────────────────────────────┤
│  SÖTÉT SÁV — CSAPOLVA        Staropramen · Stella Artois · Jägermeister    │
│                              + koktélok             [ Itallap → ]         │
├───────────────────────────────────────────────────────────────────────────┤
│  JÁTÉKSAROK   [ikon] Biliárd  [ikon] Csocsó  [ikon] Darts  [ikon] Flipper │
├───────────────────────────────────────────────────────────────────────────┤
│  KÜLÖNTEREM              │  VÉLEMÉNYEK                                     │
│  [X] főig, saját tér.    │  4,5 ★ — 1 339 vélemény a Google-on             │
│  [ Ajánlatot kérek ]     │  (forrás megjelölve, nem saját mérés)           │
├───────────────────────────────────────────────────────────────────────────┤
│  FOGLALÁS                                                                 │
│  ┌───────────────┬───────────────┐   Mit csinálunk az adataiddal:          │
│  │ Név*          │ Telefon*      │   csak visszaigazolunk, aztán töröljük. │
│  ├───────────────┼───────────────┤                                         │
│  │ Dátum*        │ Időpont*      │   [ Foglalás elküldése ]                │
│  ├───────────────┼───────────────┤   vagy hívj: (06 72) 446 000            │
│  │ Fő*           │ Hol ülnétek   │                                         │
│  ├───────────────┴───────────────┤                                         │
│  │ Megjegyzés                    │                                         │
│  └───────────────────────────────┘                                         │
├───────────────────────────────────────────────────────────────────────────┤
│  GYIK (5 db, ⌄ nyitható)        │  ELÉRHETŐSÉG + nyitvatartási táblázat    │
├───────────────────────────────────────────────────────────────────────────┤
│  Lábléc: cím · telefon · impresszum · adatkezelés · Facebook · foodora     │
└───────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Mobil (360–430px)

```
┌───────────────────────────┐
│ [skip]                    │
│ GIOVANNI            [☰]   │
├───────────────────────────┤
│ ● MOST NYITVA             │
│   zárás 23:00-kor         │
│                           │
│ Pizza, csapolt sör        │
│ és csocsó Pécs            │   ← H1, clamp() → ~34px
│ Kertvárosában.            │
│                           │
│ Lead, 2 mondat.           │
│                           │
│ ┌───────────────────────┐ │
│ │ 4,5 ★ · 1 339 vélem.  │ │
│ ├───────────────────────┤ │
│ │ 2 000–6 000 Ft / fő   │ │
│ ├───────────────────────┤ │
│ │ Nyitás 12:00, minden  │ │
│ │ nap                   │ │
│ └───────────────────────┘ │
├───────────────────────────┤
│ HOL ÜLNÉL?                │
│ ┌───────────────────────┐ │
│ │ ┌────────┐ ┌────────┐ │ │  ← ugyanaz az SVG,
│ │ │ TERASZ │ │ BELSŐ  │ │ │    változatlan viewBox,
│ │ │ • • •  │ │ ▭ ▭ ▭  │ │ │    arányosan kicsinyítve
│ │ └────────┘ └────────┘ │ │    (a rajz eleve 2×2)
│ │ ┌────────┐ ┌────────┐ │ │
│ │ │ JÁTÉK- │ │ KÜLÖN- │ │ │    Érintőcél 360px-en:
│ │ │ SAROK  │ │ TEREM  │ │ │    ~118×113 CSS px
│ │ └────────┘ └────────┘ │ │
│ └───────────────────────┘ │
│ ┌───────────────────────┐ │
│ │ TERASZ — leírás       │ │  ← a panel az ábra ALÁ
│ │ [ Ide foglalok ]      │ │    kerül, nem mellé
│ └───────────────────────┘ │
├───────────────────────────┤
│ ÉTLAP                     │
│ ┌───────────────────────┐ │
│ │ Pizzák          [ár]  │ │  ← 1 oszlop, nem
│ ├───────────────────────┤ │    vízszintes karusszel
│ │ Roston sültek   [ár]  │ │
│ ├───────────────────────┤ │
│ │ Levesek         [ár]  │ │
│ ├───────────────────────┤ │
│ │ Saláták         [ár]  │ │
│ └───────────────────────┘ │
│ [ Teljes étlap → ]        │
├───────────────────────────┤
│ CSAPOLVA (sötét sáv)      │
│ Staropramen               │
│ Stella Artois             │
│ Jägermeister              │
├───────────────────────────┤
│ JÁTÉKSAROK  2×2 rács      │
├───────────────────────────┤
│ KÜLÖNTEREM                │
├───────────────────────────┤
│ VÉLEMÉNYEK                │
├───────────────────────────┤
│ FOGLALÁS                  │
│ Név*                      │  ← 1 oszlop, 16px input
│ [_____________________]   │    (iOS zoom ellen)
│ Telefon*                  │
│ [_____________________]   │
│ Dátum*      Időpont*      │  ← ez a kettő maradhat
│ [_______]   [_________]   │    egy sorban
│ Fő*                       │
│ [_____________________]   │
│ Hol ülnétek?              │
│ [ Terasz          ▾ ]     │
│ [ Foglalás elküldése ]    │
├───────────────────────────┤
│ GYIK / ELÉRHETŐSÉG        │
│ Lábléc                    │
├───────────────────────────┤
│ ╔═══════════╦═══════════╗ │  ← sticky, csak akkor
│ ║  Hívás    ║  Foglalás ║ │    jelenik meg, ha a
│ ╚═══════════╩═══════════╝ │    hero elhagyta a nézetet
└───────────────────────────┘
```

---

## 7. Design system

### 7.0 A vizuális kiindulópont — egy mondatban

> **A lisztes rozsdamentes pult és a mellette álló, évek óta koptatott flipper- és
> csocsóasztal fém-üveg világa: hűvös acélszürkék, krétafehér lisztpor, és egyetlen
> meleg jel — a csapolt sör borostyánja.**

Ez a hely nem toszkán trattoria és nem „prémium gasztroélmény". Egy kertvárosi
pizzéria, ahol csapolt sör van és flipper. A vizuális rendszer ebből épül:
**munkaeszköz-esztétika, nem étterem-katalógus.**

**Amit ezért kizártam:**

| Elvetett irány | Miért nem |
|---|---|
| Krém háttér + magas kontrasztú serif + terrakotta accent | Ez az „olasz étterem" alapértelmezett AI-sablonja. Egy 2 000–6 000 Ft-os kertvárosi pizzériát fine-diningnak öltöztet — hazugság, és a vendég azonnal drágának olvassa. |
| Fekete + egy neon accent | Bár a játéksarok kísérti, ez sportbár-klisé, és a magyar szöveg (ő, ű) sötét alapon nagy méretben nehezen tördelhető olvashatóan. |
| Piros-fehér-zöld / kockás abrosz | A „Giovanni" név miatt kézenfekvő, ezért is elvetve: nulla megkülönböztetés a másik hat pécsi pizzériához képest. |
| Ételfotó-vezérelt hero | Nincs jogtiszta, jó minőségű saját fotókészletünk (a listing egyetlen említett fotója a „Málnás Lávasüti"). Stock-fotó pizzával azonnal lebukik. |

**Amit választottam:** világos alap (lisztpor), egyetlen sötét sáv az itallapnak
(este, pult), és **egy** meleg akcentus. A merészség egy helyre megy: az Alaprajzba.

### 7.1 Színtokenek

Alap: 9 tokenből álló skála. A kontrasztértékek WCAG 2.2 szerint számítva
(relatív luminancia, 8-bit sRGB).

| Token | Hex | Szerep | Kontraszt | Megfelelés |
|---|---|---|---|---|
| `--szen` | `#15181A` | fő szöveg világos alapon; sötét sáv háttere | **14,71 : 1** a `--liszt`-en; **17,19 : 1** a `--lap`-on | AAA |
| `--grafit` | `#23292C` | emelt felület a sötét sávban (kártya) | `--liszt` szöveg rajta **12,15 : 1** | AAA |
| `--acel` | `#56616A` | másodlagos szöveg, címkék világos alapon | **5,23 : 1** a `--liszt`-en; **6,11 : 1** a `--lap`-on | AA (normál), AAA (nagy) |
| `--acel-vil` | `#A9B2B8` | másodlagos szöveg sötét alapon | **8,28 : 1** a `--szen`-en; **6,84 : 1** a `--grafit`-on | AAA |
| `--liszt` | `#E7EAE7` | oldalháttér (hűvös krétaszürke, **nem** krém) | referencia-alap | — |
| `--lap` | `#FAFBFA` | kártya, űrlapmező, emelt felület | referencia-alap | — |
| `--vonal` | `#767F85` | input- és kártyakeret, elválasztó | **3,37 : 1** a `--liszt`-en; **3,93 : 1** a `--lap`-on | AA nem-szöveges UI (≥3:1) |
| `--parazs` | `#9C5406` | elsődleges CTA háttere, link világos alapon | fehér szöveg rajta **5,49 : 1**; szövegként a `--liszt`-en **4,70 : 1** | AA |
| `--parazs-vil` | `#F0A93C` | akcentus sötét alapon, fókuszgyűrű, kiemelés | **8,87 : 1** a `--szen`-en; **7,33 : 1** a `--grafit`-on | AAA |

**Állapotszínek** (szemantikusak, nem márkaszínek — mindig ikonnal/szöveggel
párosítva, sosem önmagukban hordoznak információt):

| Token | Hex | Szerep | Kontraszt a `--liszt`-en |
|---|---|---|---|
| `--nyitva` | `#14663F` | „Most nyitva" | **5,77 : 1** — AA |
| `--zarva` | `#96262B` | „Most zárva" | **6,64 : 1** — AA |

**Miért nem `--parazs` a zárt állapot is?** Mert akkor a CTA és a
figyelmeztetés ugyanúgy nézne ki. Az akcentus *mindig* és *csak* cselekvést jelent.

### 7.2 Típusskála

**Két variable betűcsalád, mindkettő teljes latin-ext lefedettséggel** (ő, ű valódi
kettős hosszú ékezettel, nem összeollózott glifával):

| Szerep | Család | Tengelyek | Miért ez |
|---|---|---|---|
| Display | **Bricolage Grotesque** | `wght 200–800`, `opsz 12–96`, `wdth 75–100` | Utcai tábla- és automata-feliratok logikájából épített grotesque: kissé szabálytalan, „csinált", nem semleges. Pontosan a koptatott flipper- és cégértipográfia regisztere. Az `opsz` tengely miatt nagy méretben szorosabbra, kis méretben nyitottabbra állítható. |
| Szöveg | **Source Sans 3** | `wght 200–900` | Kifejezetten képernyős folyószövegre tervezett humanista sans, magas x-magassággal és **valódi tabuláris számokkal** — ez az árlistánál és a nyitvatartási táblázatnál nem díszítés, hanem funkció. Latin-ext fedése teljes és jól hintelt 14–16px-en. |

**A display face minimális használati mérete: 24px / 1,5rem.**
Ez alatt a Bricolage jellegzetes vágásai (a `g` és az `ő` ékezetének viszonya, a
szűk belső terek) 1× DPR-en összemosódnak. 24px alatt **mindig** Source Sans 3.

**Elvetett alternatívák:**

| Alternatíva | Miért nem |
|---|---|
| Playfair Display + Inter | A default AI-páros. Ráadásul a Playfair vékony vonalvezetése kis méretben eltűnik, és a hangneme fine-dining. |
| Archivo / Archivo Expanded | Kiváló latin-ext, variable — de túl semleges, „agency-alapértelmezés". Nem hordoz karaktert. |
| Figtree szövegre | Jó, de nincs valódi tabuláris számkészlete, és a nyitvatartási táblázat emiatt ugrálna. |
| Egyetlen családdal megoldani | Olcsóbb lenne (egy woff2), de akkor a szignatúra-elem tipográfiai súlya elveszne. A két család együtt is elfér a KB-büdzsében (§11). |

```css
--t-display: clamp(2.25rem, 1.4rem + 3.6vw, 4.5rem);   /* H1 — 36 → 72px */
--t-h2:      clamp(1.75rem, 1.35rem + 1.8vw, 2.75rem); /* 28 → 44px */
--t-h3:      clamp(1.25rem, 1.13rem + 0.55vw, 1.5rem); /* 20 → 24px */
--t-lead:    clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); /* 17 → 20px */
--t-body:    1rem;      /* 16px — soha nem kisebb a folyószöveg */
--t-small:   0.875rem;  /* 14px — másodlagos, sosem kritikus infó */
--t-label:   0.75rem;   /* 12px — CSAK nagybetűs címke, 0.08em letter-spacing */
```

Sormagasság: display `1.02`, H2 `1.1`, folyószöveg `1.6`, mérőszám `1.15`.
Maximális sorhossz folyószövegen: `66ch`.

### 7.3 Térköz — 8px alapú

```css
--s-1: 4px;  --s-2: 8px;  --s-3: 16px; --s-4: 24px; --s-5: 32px;
--s-6: 48px; --s-7: 64px; --s-8: 96px; --s-9: 128px;
```
4px csak ikon-szöveg összetartozásra. Szekcióközi függőleges ritmus:
mobil `--s-7`, desktop `--s-8`. Kártya belső: `--s-4` mobil, `--s-5` desktop.
Minden érték a skáláról jön; egyedi pixelérték nem megengedett.

### 7.4 Elevation — 3 szint, szűken

| Szint | Érték | Mikor |
|---|---|---|
| `--e-0` | `0 0 0 1px var(--vonal-halvany)` | alapértelmezett: **hajszálvonal, nem árnyék**. Kártyák, mezők. |
| `--e-1` | `0 1px 2px rgb(21 24 26 / .07), 0 4px 12px -6px rgb(21 24 26 / .14)` | hover-állapot, kiválasztott zóna |
| `--e-2` | `0 -1px 0 var(--vonal-halvany), 0 -8px 24px -12px rgb(21 24 26 / .28)` | csak a mobil sticky sáv |

Indoklás: papíralapú szórólap-esztétika. Az árnyék drága (festési költség, és
vizuális zaj), a hajszálvonal ugyanazt a szeparációt adja. Árnyék csak akkor, ha
valami tényleg *lebeg* a tartalom fölött.

### 7.5 Egyéb tokenek

```css
--r-sm: 3px;   --r-md: 6px;   --r-lg: 10px;   --r-pill: 999px;
--fokusz: 3px solid var(--parazs-vil);  --fokusz-offset: 2px;
--tartalom-max: 1200px;  --szoveg-max: 66ch;
```
Kis lekerekítés (3–10px), mert a nagy radius „app-os"; ez nyomdai, nem app.

### 7.6 Komponenslista

| Komponens | Változatok | Állapotok |
|---|---|---|
| Gomb | elsődleges (tömör `--parazs`), másodlagos (keretes), szöveges | rest / hover / active / focus-visible / disabled / loading |
| Állapot-chip | nyitva / zárva | statikus + `aria-live="polite"` frissítés |
| Tényadat-kártya | 1–3 oszlop | — |
| **Zónakártya (Alaprajz)** | terasz / belső / különterem / játéksarok | rest / hover / **kiválasztott** / fókusz |
| Étlap-kategóriakártya | — | hover / fókusz |
| Ital-tétel (sötét sávon) | csapolt / koktél | — |
| Ikon (saját rajzú SVG) | biliárd, csocsó, darts, flipper | `currentColor`-t örököl |
| Űrlapmező | szöveg / tel / dátum / idő / szám / select / textarea | rest / fókusz / **hiba** / kitöltött |
| Hibaüzenet | inline, mező alatt | `role="alert"`, `aria-describedby` |
| Hibaösszegző | űrlap tetején | rejtett / látható, `tabindex="-1"`, küldéskor fókuszt kap |
| GYIK-tétel | `<details>` | nyitva / zárva |
| Nyitvatartási táblázat | — | „ma" sor kiemelve |
| Sticky mobil akciósáv | — | rejtett / látható |
| Skip-link | — | csak fókuszban látható |

### 7.7 A SZIGNATÚRA-ELEM — „Az Alaprajz"

**Mi ez.** A hajtás alatt egy **sematikus, interaktív SVG alaprajz**, amin a hely
négy zónája szerepel: **Terasz**, **Belső tér**, **Különterem**, **Játéksarok**. A
zónák kattinthatók/tabbal bejárhatók; a kiválasztás egyszerre (a) kinyit egy leíró
panelt, és (b) **előtölti a foglalási űrlap „Hol ülnétek?" mezőjét**. A játéksarokban
a biliárd-, csocsó-, darts- és flipperasztal a saját alakjával, méretarányosan jelenik
meg a többi asztal között.

**Miért pont ez.**

1. **Megmutatja, nem elmondja.** A „hangulatos terasz és különterem" mondat semmit
   nem közöl. Egy alaprajz, amin látszik, hogy a terasz kifelé néz, a különterem
   külön ajtón nyílik, és a csocsóasztal *fizikailag ott van az asztalok között* —
   az egyszerre válasz a „milyen hely ez?" és a „hova üljünk?" kérdésre.
2. **A hely tényleges döntését modellezi.** Egy asztaltársaság nem „éttermet" választ,
   hanem *helyet a helyen belül*: kint vagy bent, a gyerekekkel a játék mellé vagy a
   különterembe. Ezt eddig telefonon kellett megbeszélni.
3. **A márka saját világából jön**, nem designtrendből: a vendéglátós fejében
   *tényleg* alaprajz van (asztalkiosztás, foglalási rend). Ezt hoztam ki a
   pult mögül.
4. **Nem fotón múlik.** Nincs szükség fotósra, jogtiszta készletre, és nem avul el,
   ha átfestik a falat.
5. **Egyedi.** Nulla pécsi pizzéria csinál ilyet — ellenőrizhetően nincs is honnan
   másolni.

**Mibe kerül LCP-ben: gyakorlatilag nullába.**

- Inline `<svg>` elem, **nem** LCP-jelölt: az LCP-specifikáció szerint csak `<img>`,
  `<svg>`-n *belüli* `<image>`, `<video>` poszter, CSS `background-image` és
  blokkszintű szövegcsomó számít jelöltnek. A rajzolt `<path>`/`<rect>` nem.
  Az LCP-elem így a hero H1 szövegcsomója marad.
- **Hálózati költség: 0 kérés.** A markup a HTML-ben utazik: ~3,6 KB nyers, brotli
  után ~0,9–1,1 KB.
- **CLS: 0.** A `viewBox` + CSS `aspect-ratio` miatt a hely a first paintkor
  végleges; semmi nem tolódik el.
- **JS-költség: ~0,6 KB** (egy delegált `click`/`keydown` figyelő + osztálycsere).
  Az elem **JS nélkül is teljes értékű**: a zónák valódi `<a href="#foglalas">`
  hivatkozások leíró szöveggel, a panelek `<details>`-ként is működnek.
- Egyetlen valós költség: ~4 KB extra HTML a fő dokumentumban, ami a
  szerver-válaszidőhöz (TTFB) mérve mérhetetlen.

**Ami placeholder marad:** a valódi geometria és az asztalszámok. A prototípusban
szándékosan `[egyeztetendő]` jelöléssel szerepelnek — nem találtam ki asztalszámot.

**Elvetett szignatúra-alternatívák:**

| Alternatíva | Miért nem |
|---|---|
| Élő „kemence-hőmérő" a nyitásig visszaszámolva | Nem tudom, van-e kemencéjük és milyen — kitalált tény lett volna. |
| Animált pizza-összeállító (feltétválasztó) | Játék, de nem visz konverzió felé, és 15+ KB JS. |
| „Az est íve" — 12:00→24:00 idővonal hangulatokkal | Szép, de kitalált tartalom kellene hozzá óránként. |
| Nagy fotómozaik | Tiltott irány (fotófüggő), és nincs jogtiszta készlet. |

**Máshol a design csendes.** Egy akcentus, hajszálvonalak, árnyék alig, animáció
alig. A merészség teljes egészében az Alaprajzba megy.

---

## 8. Animációk és mikrointerakciók

Alapelv: minden mozgás **állapotváltozást magyaráz**, nem díszít. Az egész oldal
mozgáskészlete elfér három tokenben, és `prefers-reduced-motion: reduce` esetén
minden időzítés `0.01ms`-ra esik (a `transitionend` eseményekre épülő logika így is fut).

```css
--gyors: 120ms;  --alap: 200ms;  --lassu: 320ms;
--gorbe: cubic-bezier(.2,.7,.3,1);   /* gyors indulás, lágy megállás */
```

| Elem | Interakció | Változás | Időzítés | Miért |
|---|---|---|---|---|
| Gomb (elsődleges) | hover | háttér −6% világosság | `120ms` `--gorbe` | azonnali visszajelzés, nem játék |
| Gomb | active | `translateY(1px)` | `60ms` linear | fizikai megnyomás-érzet |
| Bármi fókuszálható | `:focus-visible` | 3px `--parazs-vil` gyűrű, 2px offset | **0ms** | a fókusz sosem animált — késleltetve nem látszik, hova ugrott |
| Zónakártya (Alaprajz) | hover | kitöltés opacitás .06 → .14 | `120ms` | „ez kattintható" |
| Zónakártya | kiválasztás | 2px keret + panel csere | `200ms` | az állapotváltás olvasható legyen |
| Zónapanel | csere | opacitás 0→1 + `translateY(6px→0)` | `200ms` `--gorbe` | jelzi, hogy *új* tartalom jött, nem a régi módosult |
| Állapot-chip pont | folyamatos | opacitás 1 → .45 → 1 | `2400ms` végtelen | „élő adat" jelzés. **Reduced motion esetén kikapcsol** — az információt a szöveg hordozza |
| Sticky mobil sáv | hero elhagyása | `translateY(100%→0)` | `320ms` `--gorbe` | ne takarja a herót, de utána mindig kéznél legyen |
| Űrlapmező | hiba megjelenése | keret- és `box-shadow`-szín vált, a hibaszöveg **animáció nélkül** jelenik meg | `200ms` (csak a keret) | A szöveg magasságának animálása (`max-height`) reflow-t okoz, és ütközik a „csak `transform`/`opacity`" szabállyal. A keretszín-váltás elég visszajelzés. |
| Küldés gomb | küldés alatt | `disabled`, opacitás .45, felirat → „Küldés…" | azonnali | Dupla beküldés megelőzése; a felhasználó látja, hogy történik valami. |
| Űrlapmező | hiba javítása | keret vissza alapra | `200ms` | pozitív megerősítés |
| GYIK `<details>` | nyitás | natív; `content-visibility` nélkül | natív | nem éri meg egyedi animációt írni rá |
| Belső horgonyugrás | kattintás | `scroll-behavior: smooth` | natív, reduced-motion esetén `auto` | kontextusőrzés |
| Étlapkártya | hover | hajszálvonal `--vonal` → `--szen` | `120ms` | minimális, hogy ne vonja el a figyelmet a CTA-ról |

Ami **nincs**: scroll-triggerelt beúszás, parallax, számláló-animáció, hero-videó,
betűnkénti szövegfelfedés. Mind lassít, mind bosszant másodjára, és egyikük sem
segít eldönteni, hogy hova üljünk le vacsorázni.

---

## 9. Frontend-megvalósítás

### 9.1 Stack

**Javaslat: Astro statikus build → GitLab → Netlify, Formspree űrlap-végponttal.**
Ez a stúdió meglévő eszközkészlete; nincs benne semmi, amit külön be kellene vezetni
vagy karbantartani.

| Réteg | Választás | Indoklás | Elvetett alternatíva |
|---|---|---|---|
| Renderelés | **Astro** statikus build | 9 oldal, ritkán változó tartalom. Nulla futásidejű PHP, nulla adatbázis. Az étlap komponensbe és `Menu` schemába is egy adatforrásból generálódik. | **WordPress megtartása**: ismerős a tulajdonosnak, de minden látogató kifizeti a futásidőt (§3, Ok #5). Ha a szerkeszthetőség kritikus → §15/19. **Sima HTML+CSS**: 9 oldalnál a fejléc/lábléc duplikálódna. |
| Verziókezelés | **GitLab**, privát repó (`giovanni-web`) | Ügyfelenként külön repó; a Netlify erről deploy-ol. | — |
| Hosting / deploy | **Netlify**, GitLab-ról auto-deploy | Ingyenes SSL, CDN, és **branch-enkénti preview URL** — az ügyfél éles domain előtt ezen látja az oldalt. | **FTP/kézi feltöltés**: nincs verzió, nincs preview, nincs visszaállítás. |
| JS | vanilla, **4 976 B** (mért) | Ennyi funkcióhoz (állapotóra, zónaválasztás, validáció, menü) a keretrendszer tiszta veszteség. | **React/Vue**: +40 KB minimum, semmiért. |
| CSS | egyetlen kézzel írt lap, custom property-kkel | A design system 30 tokenből áll, ehhez nem kell utility-keretrendszer. | **Tailwind**: build-lánc és osztálynév-zaj egy 9 oldalas oldalért. |
| Animáció | **nincs könyvtár** | A teljes mozgáskészlet 3 CSS-tokenből elfér (§8). | **AOS / GSAP**: scroll-animációkhoz való, itt nincs egy sem — és a Lighthouse-célt (§11) rontaná. |
| Tartalom | JSON az étlaphoz, Markdown a szövegoldalakhoz | Az étlap adat, nem szöveg: egy JSON-ból generálódik a HTML **és** a `Menu` schema — nem lehet elcsúszni egymástól. | **Kézi HTML-szerkesztés**: az étlap és a schema garantáltan szétcsúszik. |
| Űrlap | **Formspree** végpont → e-mail az étterem címére | Nincs backend, nincs adattárolás, beépített spamszűrés, és az étterem bármikor átállíthatja a fogadó e-mail-címet. GDPR: csak továbbít, nem tárol tartósan. | **Cloudflare Worker / saját serverless**: több karbantartás, több hozzáférés, ugyanaz az eredmény. **`mailto:`**: mobilon a felhasználók fele elakad. |
| Foglalás | **a saját űrlap**, nem foglalómotor | Az étterem foglalása nem időpontfoglalás: létszám + zóna + időpont, fix slothossz nélkül, és telefonos visszaigazolással zárul. | **Cal.com**: fix hosszú slotokra tervezett időpontfoglaló (konzultáció, fodrász). Egy asztaltársaságra ráerőltetve fals kapacitást ígér, amit az étterem nem tud tartani. Akkor jön szóba, ha az ügyfél tényleg slot-alapú foglalást akar (→ §15/5). |

**Ha a foglalás volumene később indokolja** (napi 20+ online foglalás), a következő lépés
Supabase-tábla + visszaigazoló e-mail, nem egy dobozos foglalórendszer — de ez a
2. fázisban még biztosan felesleges.

### 9.2 Fontkezelés

- **Önhosztolt woff2**, saját domainről. Google Fonts CDN-ről betölteni ma
  (a) egy extra kapcsolat, (b) adatvédelmi kockázat EU-ban.
- **Subsetting**: `latin` + `latin-ext` **csak** (unicode-range-dzsel két fájlra
  bontva, hogy az ékezetes blokk külön töltődjön). A magyar `ő`/`ű` a `latin-ext`
  blokkban van — ezt kihagyni a leggyakoribb hiba, aminek eredménye a
  fallback-glifás „ő".
- **Variable fájlok**, statikus vágatok helyett: Source Sans 3 VF ~38 KB,
  Bricolage Grotesque VF ~34 KB (`wght` tengelyre szűkítve, `wdth`/`opsz`
  instanceolva a buildben, ha nem használjuk dinamikusan).
- `font-display: swap` + `<link rel="preload" as="font" crossorigin>` **csak a
  szövegcsaládra**. A display face nem preloadolódik: a H1 fallbackkel is
  olvasható, és így nem versenyez az LCP-ért.
- `size-adjust` / `ascent-override` a fallback stacken (`@font-face` fallback
  metrikamásolattal), hogy a betűcsere ne okozzon elrendezés-ugrást (CLS).

```css
@font-face{font-family:"Source Sans 3";src:url(/f/ss3.woff2)format("woff2-variations");
  font-weight:200 900;font-display:swap;unicode-range:U+0000-00FF,U+0131,U+0152-0153,...}
@font-face{font-family:"Source Sans 3";src:url(/f/ss3-ext.woff2)format("woff2-variations");
  font-weight:200 900;font-display:swap;unicode-range:U+0100-024F,U+0259,U+1E00-1EFF,...}
```

### 9.3 Képek

- Formátum: **AVIF** elsődleges, WebP fallback, `<picture>`-rel.
- Minden `<img>`-en kötelező `width`, `height`, `alt` (dekoratívnál `alt=""`).
- `loading="lazy"` + `decoding="async"` mindenen, ami a hajtás alatt van;
  a hajtás fölötti kép (ha lesz) `fetchpriority="high"`, `loading="eager"`.
- `srcset` 3 lépcsőben (480 / 960 / 1440 px).
- Ételfotó **csak saját, friss felvételből**. Stock nincs. Amíg nincs fotó, a
  szekció fotó nélkül is teljes értékű (ezért nem építettem fotófüggő layoutot).
- Az ikonok mind inline SVG-k, `currentColor`-ral — nincs ikonfont, nincs sprite-kérés.

### 9.4 Cache

| Erőforrás | Fejléc |
|---|---|
| HTML | `Cache-Control: public, max-age=0, must-revalidate` + `ETag` |
| CSS/JS (hasholt fájlnév) | `public, max-age=31536000, immutable` |
| Fontok | `public, max-age=31536000, immutable` |
| Képek (hasholt) | `public, max-age=31536000, immutable` |
| Űrlap-végpont | `no-store` |

A kritikus CSS (~7 KB) **inline** a `<head>`-ben, a maradék elhalasztva
(`media="print" onload="this.media='all'"` mintával, `<noscript>` fallbackkel).

### 9.5 Űrlap

- Natív HTML-validáció **alapnak** (`required`, `type="tel"`, `min`, `max`,
  `pattern`), és JS-réteg *fölé*, ami:
  - `novalidate`-tel átveszi a hibamegjelenítést, hogy magyar, konkrét
    üzenetet adjon (a böngésző saját szövege lokalizált, de generikus);
  - **`blur`-kor validál először, utána `input`-ra újraértékel** — nem
    kiabál gépelés közben;
  - küldéskor **hibaösszegzőt** épít az űrlap tetején (GOV.UK-minta): felsorolja,
    hány mező hibás, mindegyikhez horgonylinkkel, és a fókuszt az összegzőre viszi.
    Így a képernyőolvasó és a nagyítót használó felhasználó egyszerre látja az összes
    hibát, nem csak az elsőt (WCAG G139).
- **Dupla beküldés ellen**: a küldés gomb a beküldés idejére `disabled`, a felirata
  „Küldés…", és csak a szerverválasz után áll vissza. Enélkül a lassú hálózaton
  türelmetlen felhasználó két foglalást küld.
- Minden mezőnek valódi `<label for>`; a placeholder soha nem címke.
- Hiba: `aria-invalid="true"` + `aria-describedby` a hibaszövegre,
  a hibaszöveg `role="alert"`.
- Az űrlap **JS nélkül is elküldhető** (`method="post"` a végpontra).
- Spam: rejtett honeypot mező + időbélyeg-ellenőrzés a szerveren.
  **CAPTCHA nincs** — akadálymentességi és konverziós költsége nagyobb, mint a haszna
  ezen a volumenen.
- GDPR: egy mondat az űrlap mellett arról, mit csinálunk az adattal, + link az
  adatkezelési tájékoztatóra. Marketing-hozzájárulás **külön, opcionális** jelölő.

---

## 10. SEO-specifikáció

### 10.1 Title / meta minta

| Oldal | `<title>` (≤ 60 kar.) | `meta description` (≤ 155 kar.) |
|---|---|---|
| `/` | `Giovanni Pizzéria Pécs – Nagy Imre út 43. | Asztalfoglalás` | `Pizza, roston sültek, csapolt sör és csocsó Pécs Kertvárosában. Terasz, különterem, játéksarok. Nyitás minden nap 12:00. Foglalj asztalt online.` |
| `/etlap/` | `Étlap – Giovanni Pizzéria, Pécs Kertváros` | `Pizzák, roston sültek, levesek és saláták árakkal. Allergéninformáció minden tételnél. Helyben és kiszállítással.` |
| `/itallap/` | `Itallap – csapolt sörök és koktélok | Giovanni Pécs` | `Staropramen és Stella Artois csapolva, Jägermeister, koktélok. A teljes itallap árakkal.` |
| `/asztalfoglalas/` | `Asztalfoglalás – Giovanni Pizzéria Pécs` | `Foglalj asztalt teraszra, a belső térbe vagy a különterembe. Visszaigazolás telefonon.` |
| `/kulonterem/` | `Különterem Pécsen [X] főig – Giovanni Pizzéria` | `Céges vacsora, ballagás, szülinap Pécs Kertvárosában. Saját különterem, fix menüajánlatok. Kérj ajánlatot.` |
| `/jatekterem/` | `Biliárd, csocsó, darts, flipper – Giovanni Pécs` | `Játéksarok a pizzéria mellett: biliárd, csocsóasztal, darts, flipper. Csapolt sör mellé.` |

Elv: **a márkanév hátul, a differenciátor elöl**, kivéve a főoldalt. Ne ismételjük
a WP-alapértelmezést (P8).

### 10.2 Heading-hierarchia (főoldal)

```
H1  Pizza, csapolt sör és csocsó Pécs Kertvárosában   (pontosan egy H1)
├ H2  Hol ülnél?                    (Alaprajz)
│  └ H3  Terasz / Belső tér / Különterem / Játéksarok   (a panelekben)
├ H2  Étlap
│  └ H3  Pizzák / Roston sültek / Levesek / Saláták
├ H2  Csapolva és koktélok
├ H2  Játéksarok
│  └ H3  Biliárd / Csocsó / Darts / Flipper
├ H2  Különterem
├ H2  Mit mondanak a vendégek
├ H2  Asztalfoglalás
├ H2  Gyakori kérdések
│  └ H3  (kérdésenként)
└ H2  Elérhetőség és nyitvatartás
```
Szint kihagyása nincs. A lábléc navigációs címei `H2`-k, vizuálisan kicsik.

### 10.3 Strukturált adat — teljes gráf

Egyetlen `<script type="application/ld+json">`, `@graph` szerkezetben,
`@id`-kkal összekötve:

| `@type` | `@id` | Mit tartalmaz |
|---|---|---|
| `WebSite` | `#website` | `name`, `url`, `inLanguage: hu-HU`, `publisher` → `#restaurant` |
| `WebPage` | `#webpage` | `isPartOf` → `#website`, `about` → `#restaurant`, `primaryImageOfPage`, `breadcrumb` |
| `Restaurant` | `#restaurant` | `name`, `image`, `telephone`, `url`, `priceRange`, `servesCuisine: ["Pizza","Olasz","Magyar"]`, `currenciesAccepted: HUF`, `paymentAccepted`, `address` → `PostalAddress`, `geo` → `GeoCoordinates`, `openingHoursSpecification` (7 nap), `acceptsReservations: true`, `hasMenu` → `#menu`, `amenityFeature` → `LocationFeatureSpecification[]`, `potentialAction` → `ReserveAction`, `sameAs` (Facebook, foodora, Google) |
| `Menu` | `#menu` | `hasMenuSection` → `MenuSection[]` (Pizzák, Roston sültek, Levesek, Saláták), azon belül `MenuItem` + `offers.price` |
| `BreadcrumbList` | `#breadcrumb` | `Főoldal` (a főoldalon 1 elem) |
| `FAQPage` | `#faq` | 5 `Question`/`Answer` |
| `ImageObject` | `#logo` | logó, `width`/`height` |

**`amenityFeature` tételek** (a `LocationFeatureSpecification` `name` + `value`
párokkal, mert ezek a Google-attribútumok gépi megfelelői):
`Szabadtéri asztalok`, `Különterem`, `Terasz`, `Biliárd`, `Csocsó`, `Darts`,
`Flipper`, `Kártyás fizetés`, `Akadálymentes bejárat *(ellenőrizendő)*`.

**Amit szándékosan NEM teszek bele: `aggregateRating`.**
A 4,5 ★ / 1 339 vélemény a Google Cégprofilból származik. A saját oldalon
sajátként megjelölt `aggregateRating` **önkiszolgáló értékelés-jelölés**, amit a
Google strukturált adat irányelvei tiltanak a saját entitásra, és amiért kézi
büntetés jár. A számot **szövegként, forrásmegjelöléssel** jelenítjük meg —
ugyanaz a bizalmi hatás, nulla kockázat.
*(Ha később valódi, oldalon gyűjtött vendégértékelés lesz `Review` elemekkel,
az újratárgyalható.)*

### 10.4 Local SEO — a listing mint csatorna

| Teendő | Miért |
|---|---|
| Google Cégprofil: **„Foglalás" link** beállítása → `/asztalfoglalas/` | Ezzel lesz a listingnek olyan gombja, ami a saját oldalra visz konverzióval (P1). |
| Cégprofil: **Étlap-link** → `/etlap/`, **Attribútumok** kiegészítése (biliárd, csocsó, darts, flipper) | A Google ma nem tudja a legfontosabb differenciátort. |
| **NAP-konzisztencia** (Név / Cím / Telefon) minden aggregátoron: hovamenjek, etterem.hu, nyitva.hu, cylex, firmania, gastro.hu, ittjartam | A név ma háromféleképp szerepel: „Giovanni", „Giovanni Pizzéria", „Giovanni étterem". Ez hígítja az entitást. |
| **A két foodora-listing tisztázása** (összevonás vagy egyértelmű elnevezés) | P4 — közvetlen rendelésvesztés. |
| Cím: `Nagy Imre út 43.` — az aggregátorokon `Nagy Imre Utca 43` is szerepel | Következetlen cím → gyengébb helyi jelzés. |
| Heti fotófeltöltés a Cégprofilra | A listing fotógalériája ma szinte üres („Málnás Lávasüti"). |
| `sameAs` a schema-ban minden hiteles profilra | Entitás-összekötés. |

**Amit nem csinálunk:** kulcsszóhalmozás („pizza Pécs, pizza rendelés Pécs, pizzéria
Pécs…"), városonkénti álodalak, vélemény-kérés jutalomért.

---

## 11. Performance-célok

Mérési alap: **Moto G Power-osztályú eszköz, lassú 4G (400 kbps down, 400 ms RTT)**,
Lighthouse mobil profil; és mezei CrUX (75. percentilis).

| Metrika | Cél | Jelenlegi (becsült, WP-alapon) |
|---|---|---|
| **LCP** | **≤ 1,6 s** lab, ≤ 2,0 s CrUX p75 | 3,5–6 s *(mérendő)* |
| **CLS** | **≤ 0,02** | ismeretlen, fontcsere+képek miatt vsz. > 0,1 |
| **INP** | **≤ 120 ms** (cél: ≤ 200 ms határ jóval alatta) | ismeretlen |
| **TTFB** | ≤ 200 ms (statikus, CDN) | 400–900 ms |
| **FCP** | ≤ 1,0 s | — |
| **TBT** | ≤ 80 ms | — |

**KB-büdzsé, első betöltés (tömörítve, hálózaton):**

| Erőforrás | Büdzsé |
|---|---|
| HTML (kritikus CSS inline-nal, JSON-LD-vel, az Alaprajz SVG-vel) | **≤ 18 KB** br |
| Elhalasztott CSS | ≤ 6 KB br |
| JS (összesen) | **≤ 5 KB** — a prototípus tömörítetlenül **4 976 B** |
| Font: Source Sans 3 VF (latin) | ≤ 26 KB |
| Font: Source Sans 3 VF (latin-ext) | ≤ 12 KB |
| Font: Bricolage Grotesque VF (latin+ext, `wght` tengelyre szűkítve) | ≤ 30 KB |
| Kép a hajtás fölött | **0** (szándékosan nincs) |
| Hajtás alatti képek (lazy, AVIF) | ≤ 45 KB / kép |
| **Első nézet, hajtás fölött összesen** | **≤ 95 KB** |
| Teljes főoldal, minden lusta erőforrással | ≤ 320 KB |

**Kérésszám a hajtás fölött: 4** (HTML, 2 font, 1 JS). Nincs harmadik felű kérés
az első nézetben — analitika `defer`-rel, a `load` után.

**Hogyan tartjuk:** a hero szándékosan **szöveges** (nincs hero-kép), így az LCP
egy szövegcsomó, ami a fallback fonttal azonnal fest, és `size-adjust`-tal nem ugrik
a csere. Ez az egyetlen legnagyobb hozamú döntés az egész projektben.

---

## 12. CRO — konverziós elemek

Az oldal EGY dolga: **asztalfoglalás**. Minden alábbi elem ezt szolgálja vagy
akadályt bont el előle.

| # | Elem | Hol | Miért működik |
|---|---|---|---|
| 1 | **Élő nyitva/zárva chip zárási idővel** | hero, első sor | Az első kérdésre válaszol, és az egyetlen valós ok, amiért a Google-ról átjön valaki. Ha „zárva", akkor is konverzió: „nyitás 12:00" + „foglalj mára" — nem elveszett látogató, hanem eltolt konverzió. |
| 2 | **Két egyenrangú CTA: Foglalás / Hívás** | hero | A vendéglátásban a hívás valós konverzió, nem kudarc. Elrejteni a telefonszámot a foglalás javára = elvesztett foglalás. Egyenrangúak, nem versenyeznek. |
| 3 | **Alaprajz mint választó** | 2. szekció | Zérus kognitív költséggel kvalifikálja a foglalást: a látogató kimondja magának, mit akar (terasz / különterem), és ezzel elköteleződik. A kiválasztás előtölti az űrlapot → megkezdett folyamat, amit nehezebb elhagyni. |
| 4 | **Ársáv a hajtás fölött (2 000–6 000 Ft/fő)** | tényadat-kártya | Az ár elrejtése súrlódás. Kimondva kiszűri a rossz illeszkedésű látogatót, és a maradéknál eltünteti a legnagyobb belső ellenvetést. |
| 5 | **4,5 ★ / 1 339 vélemény, forrásmegjelöléssel** | tényadat + külön szekció | A darabszám itt fontosabb, mint az átlag: 1 339 vélemény ellenőrizhetetlenül nagy szám egy kertvárosi helynél. A forrás megnevezése (Google) növeli a hitelt, nem csökkenti. |
| 6 | **Rövid, 6 mezős űrlap** | 8. szekció | Minden extra mező mérhetően csökkenti a kitöltést. Csak az kerül bele, ami nélkül nem lehet asztalt lefoglalni: név, telefon, dátum, idő, létszám, zóna. E-mail **nem kötelező**. |
| 7 | **Inline validáció `blur`-re, nem gépelés közben** | űrlap | A gépelés közbeni pirosítás büntetésként hat és növeli az elhagyást; a `blur`-validáció ugyanazt a hibát fogja el, negatív érzelem nélkül. |
| 8 | **„vagy hívj: (06 72) 446 000" a küldés gomb alatt** | űrlap | Kiút azoknak, akik megakadnak. Az űrlapot elhagyók egy része így is konvertál. |
| 9 | **Adatkezelési mikroszöveg az űrlapnál** | űrlap | „Csak visszaigazolunk, aztán töröljük." — a magyar felhasználó legnagyobb űrlapfélelme, hogy hírlevelet kap. Egy mondat oldja. |
| 10 | **Sticky mobil sáv (Hívás / Foglalás)** | mobil, hero után | Mobilon a látogatók többsége az oldal közepén dönt. Ne kelljen visszagörgetni. |
| 11 | **Különterem-blokk saját CTA-val** | 6. szekció | A legmagasabb kosárértékű szegmens külön útvonalat kap, mert más a szándéka (ajánlatkérés, nem foglalás). |
| 12 | **GYIK a foglalás után** | 9. szekció | Az itt maradt kifogásokat (parkolás, gyerekek, kutya, saját torta, kártyás fizetés) *az űrlap után* oldjuk fel, hogy a kifogások ne előzzék meg a döntést. |
| 13 | **Nyitvatartási táblázat kiemelt „ma" sorral** | 10. szekció | Csökkenti a „mikor mehetek?" miatti visszalépést a Google-hoz. |
| 14 | **Egyetlen akcentusszín, csak cselekvésre** | mindenütt | Ha minden kiemelt, semmi sem az. A `--parazs` kizárólag kattintható dolgokon jelenik meg — az oldal így „megtanítja", hova kell nyúlni. |

---

## 13. Design-döntések összefoglaló táblázata

| # | Döntés | Alternatíva | Miért nem az alternatíva |
|---|---|---|---|
| D1 | A redesign tárgya a saját oldal, a listing csak csatorna | A hovamenjek-listing „újratervezése" | Nincs hozzá hozzáférés; a layoutot a platform adja. |
| D2 | Az oldal egy dolga: asztalfoglalás | Online rendelés/fizetés | A foodora ezt már megoldja 4,7 ★-gal; saját checkout ROI-ja negatív ezen a méreten. |
| D3 | Szöveges hero, hero-kép nélkül | Nagy ételfotó a hajtásban | Nincs jogtiszta, jó fotókészlet; és a hero-kép a legdrágább LCP-tétel. |
| D4 | Szignatúra: interaktív SVG alaprajz | Fotómozaik / kemence-animáció / pizza-építő | Fotófüggő vagy kitalált tényre épülne; az alaprajz konverziót visz és 0 LCP. |
| D5 | Hűvös krétaszürke alap, egy borostyán akcentus | Krém + serif + terrakotta | Fine-dining regisztert hazudna egy 2–6 e Ft-os helyre; ráadásul tiltott irány. |
| D6 | Bricolage Grotesque + Source Sans 3 | Playfair + Inter; egy család | Az első a default AI-páros; az egy család esetén elvész a szignatúra súlya. |
| D7 | Astro statikus build, Netlify-on | WordPress megtartása | Minden látogató kifizeti a CMS futásidejét (§3 Ok #5). *Feltételes — §15.* |
| D8 | Hajszálvonal-alapú elevation, alig árnyék | Kártyás, árnyékos „app"-look | Nyomdai/szórólap-regiszter; kevesebb festési költség. |
| D9 | `aggregateRating` nincs a schema-ban | Csillagok kiírása rich snippetért | Önkiszolgáló értékelés-jelölés, Google-irányelvbe ütközik. |
| D10 | Meglévő URL-ek megtartása (`/etlap/`, `/itallap/`, `/elerhetoseg/`) | Új, „szebb" URL-struktúra | Indexelt oldalakat átirányítani ok nélkül nettó veszteség. |
| D11 | Külön `/kulonterem/` és `/jatekterem/` oldal | Minden a főoldalon | Külön keresési szándék, külön hirdethető landing, külön mérhető. |
| D12 | Telefonszám végig egyenrangú a foglalással | „Digitális-first", telefon elrejtve | Vendéglátásban a hívás valós, gyakran domináns konverzió. |
| D13 | Nincs CAPTCHA | reCAPTCHA / hCaptcha | Akadálymentességi és konverziós költsége meghaladja a spam kárát ezen a volumenen. Honeypot + időbélyeg elég. |
| D14 | Nincs cookie-alapú analitika az első nézetben | GA4 azonnal | Cookie-banner = az első interakció egy elutasítás. Szerveroldali/cookieless mérés, `load` után. |
| D15 | Az étlap adatból (JSON) generálódik | Kézi HTML | A schema és a látható étlap különben szétcsúszik. |
| D16 | Zöld/piros állapotszín ikonnal és szöveggel párosítva | Csak színnel jelzett állapot | Színvakság; a szín sosem lehet egyedüli információhordozó. |

---

## 14. Bevezetési ütemterv

| Fázis | Tartalom | Kimenet | Előfeltétel |
|---|---|---|---|
| **0. Audit és adatgyűjtés** | Élő mérés (Lighthouse, CrUX), a §15 kérdéslista lefuttatása az ügyféllel, meglévő URL-ek és forgalmi adatok kinyerése, fotóleltár | mérési alapvonal + kitöltött tényadatlap | ügyfél-hozzáférés az analitikához és a Cégprofilhoz |
| **1. Gyors nyereségek — a saját oldal érintése nélkül** | Google Cégprofil: foglalás-link, étlap-link, attribútumok, fotók; NAP-konzisztencia az aggregátorokon; a két foodora-listing rendezése | mérhető listing-forgalom-emelkedés 2–3 héten belül | 0. fázis |
| **2. Alap: főoldal + foglalás** | A jelen prototípus véglegesítése valós adatokkal, Alaprajz valós geometriával, űrlap-végpont, analitika | élő `/` és `/asztalfoglalas/` | valós asztalkiosztás, nyitvatartás, foglalási folyamat |
| **3. Tartalmi oldalak** | `/etlap/` JSON-ból, `/itallap/`, `/allergenek/`, `/elerhetoseg/` | teljes étlap + allergén | árlista, allergénadatok |
| **4. Bevételi oldalak** | `/kulonterem/` (kapacitás, csomagok, ajánlatkérő), `/jatekterem/` | két új landing | kapacitás, csomagárak, fotók |
| **5. Fotó és tartalom** | Fotózás (terek, 8–10 étel, játéksarok), szövegek véglegesítése | képkészlet, AVIF-pipeline | fotós, egy zárva töltött délelőtt |
| **6. Mérés és finomítás** | Konverziókövetés, a foglalási űrlap elhagyási pontjai, GYIK bővítése valós kérdésekből | havi riport | 2. fázis óta eltelt ≥ 4 hét |

Fázis 1 és 2 párhuzamosítható; 1 azonnali hozamot ad, amíg 2 készül.

---

## 15. Nyitott kérdések — ehhez ügyfél-input kell

**Blokkoló (enélkül nem élesíthető):**

1. **Pontos nyitvatartás minden napra**, ünnepnapi eltérésekkel. *(Az aggregátorok
   ellentmondanak; a prototípus élő állapotjelzője ezt az adatot használja.)*
2. **A konyha záró időpontja** — eltér-e a hely zárásától? (A vendég ezt kérdezi 22:15-kor.)
3. **Asztalkiosztás és férőhely zónánként**: terasz / belső / különterem / játéksarok
   asztal- és fő-szám. *(Az Alaprajz szignatúra-elem ezen áll vagy bukik.)*
4. **Különterem**: hány főig, van-e külön ajtó, minimumfogyasztás, előleg,
   lemondási feltétel, fix menücsomagok és áraik.
5. **Fogadtok-e egyáltalán asztalfoglalást?** Ha igen: telefonon, e-mailben, vagy
   mindkettőn? Ki és mikor igazolja vissza? *(Az egész oldal fő konverziója ez.)*
6. **Étlap + itallap tételek, aktuális árakkal**, és **allergénadatok** tételenként.
7. **A két foodora-listing** („Giovanni Pizzéria" és „Giovanni étterem") — ugyanaz a
   konyha? Melyik az elsődleges? Összevonható?

**Erős hatású (a tartalom minőségét dönti el):**

8. Mióta működik a hely, ugyanazon a címen, ugyanazzal a tulajdonossal? *(Számot
   nem találtam ki — pedig egy „1998 óta" a legerősebb bizalmi elem lenne.)*
9. Van-e ebédmenü? Meddig, mennyiért?
10. A játéksarok tényleg működik? Biliárd, csocsó, darts, flipper — melyik van *ma*
    a helyszínen, és fizetős-e?
11. „Nagyszerű koktélok" — a Google-attribútum szerint van koktélkínálat, a saját
    oldalon csak csapolt sör szerepel. Melyik igaz?
12. Kutya bemehet? Gyerekszék, pelenkázó? Akadálymentes bejárat és mosdó?
13. Parkolás: van saját parkoló? Fizetős zóna? Melyik buszjárat áll a legközelebb?
14. Kártyás fizetés, SZÉP-kártya elfogadás (melyik zseb)?
15. Van-e saját fotókészlet, és jogtiszta-e? Ha nincs: mikor fotózható a hely?

**Technikai / hozzáférési:**

16. Ki fér hozzá a `giovannipecs.hu` tárhelyéhez, domainjéhez, és a Google Cégprofilhoz?
17. Tényleg WordPress? Milyen téma, milyen pluginok, ki karbantartja? *(Ettől függ,
    hogy D7 statikus generálás lehet-e, vagy a WP-t kell optimalizálni.)*
18. Van-e ma analitika, és **mennyi a jelenlegi forgalom**? Enélkül a redesign
    hatását nem lehet bizonyítani.
19. Szerkeszthetőségi elvárás: ki fogja frissíteni az árakat, és milyen felületen?
20. Van-e márkakönyv, logó vektorosan? **A briefben nem szerepelt, mit tilos
    megváltoztatni** — én a márkanevet, a telefonszámot, a címet és a meglévő
    URL-eket vettem érinthetetlennek. Megerősítendő.

---

## 16. Az anyag leggyengébb pontja — őszintén

**A leggyengébb pont: az egész stratégia egy nem ellenőrzött feltevésen áll — hogy
a Giovanni fogad asztalfoglalást, és hogy a különterem valóban létező, eladható
termék.**

Ha kiderül, hogy nem fogadnak foglalást (sok kertvárosi pizzéria nem: „gyere és
ülj le"), akkor az oldal „EGY dolga" hibás, és az Alaprajz-szignatúra egy olyan
folyamat elé épített kapu, ami nem létezik. Ebben az esetben a helyes fókusz a
*kiszállítás* és a *„most nyitva, gyere"* lenne, és a szignatúra-elemnek is más
kimenete kellene legyen. Ezt a kockázatot a §15/5. kérdés zárja le, és amíg nincs
válasz, minden §12-es CRO-állítás feltételes.

Két további gyengeség, kisebb súllyal:

- **Az elemzés rekonstrukció.** A hálózati blokk miatt nem láttam sem a listing,
  sem a saját oldal valódi DOM-ját, se egyetlen Lighthouse-mérést. A §2 P11–P13
  performance- és akadálymentességi állításai stack-alapú inferenciák, nem mérések.
  Bizonyíték nélkül ezeket **állításként kezelni hiba lenne** — a 0. fázis első
  napján mérni kell.
- **A prototípus szövegei tényszegények.** Mivel nem találtam ki számot, a
  legmeggyőzőbb mondatok (mióta működnek, hány főig megy a különterem, mennyibe
  kerül egy pizza) placeholderként állnak. Egy tényadatokkal feltöltött verzió
  érezhetően erősebb lesz, mint ami most a `index.html`-ben látszik — az anyag
  jelenlegi meggyőző ereje ezért alulmutatja a végleges potenciált.

---

### Források

Rekonstrukció alapjául szolgáló, indexelt tartalom:
[hovamenjek.hu listing](https://hovamenjek.hu/pecs/giovanni-pizzeria) ·
[giovannipecs.hu](https://giovannipecs.hu/) ·
[giovannipecs.hu/etlap/](https://giovannipecs.hu/etlap/) ·
[giovannipecs.hu/itallap/](https://giovannipecs.hu/itallap/) ·
[giovannipecs.hu/elerhetoseg/](https://giovannipecs.hu/elerhetoseg/) ·
[etterem.hu/giovanni](https://etterem.hu/giovanni) ·
[foodora – Giovanni Pizzéria](https://www.foodora.hu/restaurant/z28z/giovanni-pizzeria) ·
[foodora – Giovanni étterem](https://www.foodora.hu/restaurant/xxsj/giovanni-etterem) ·
[ittjartam.hu vélemények](https://www.ittjartam.hu/pecs/ettermek/giovanni-pizzeria-pecs/) ·
[nyitvatartas24.hu](https://www.nyitvatartas24.hu/uzlet/P%C3%A9cs-Giovanni%20Pizz%C3%A9ria-38465F.html) ·
[nyitva.hu](https://nyitva.hu/p%C3%A9cs/giovanni-pizz%C3%A9ria-81019) ·
[yably.hu](https://yably.hu/%C3%A9rt%C3%A9kel%C3%A9sek/pecs/giovanni-pizzeria-nagy-imre-utca-43)
