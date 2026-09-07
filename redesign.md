# Krém Desszertműhely és Kávézó, Pécs — UI/UX redesign koncepció és prototípus

> **Módszertani figyelmeztetés — rekonstrukcióból dolgoztam.**
> A brief egy **Google Cégprofil-listing** szövegét adta meg, nem egy weboldalt.
> A cég saját webhelyét kerestem (`Krém Desszertműhely`, `Zsuzsanna u. 2 Pécs`,
> `06 30 609 7009` kombinációkban): **egyetlen indexelt találat sem** tartozik
> ehhez a vállalkozáshoz. A találatok kivétel nélkül más cégek — a
> székesfehérvári *Krém Cukrászda és Kávézó*, a pesterzsébeti *Nosztalgia
> Desszertműhely*, pécsi cukrászda-gyűjtőoldalak. A közvetlen lekérés (`hu`
> irányítószám-adatbázis) a hálózati egress-proxyn elakadt (`EGRESS_BLOCKED`).
>
> Ezért: **minden ténymegállapítás forrása vagy a briefben megadott listing,
> vagy jelölve van, hogy következtetés.** Számot, árat, kapacitást, nyitvatartást
> nem találtam ki — ahol placeholder kell, ott `[szögletes zárójel]` áll, és a
> §15-ben kérdésként szerepel.

> **Hatókör-pontosítás.** A megadott felület nem az ügyfél tulajdona: a Google
> saját UI-ja, a Google Cégprofil adataiból renderelve. Ezt **nem lehet
> újratervezni** — a layoutot a platform diktálja. Ezért a munkát így bontom:
>
> 1. A listinget **elemzem** mint a jelenlegi — és jelenleg egyetlen — digitális
>    belépőpontot (§1–§3), és megnevezem, mi **jó** benne (§1.3).
> 2. A redesign tárgya **a hiányzó saját webhely** (§4–§14).
> 3. A listinget **csatornaként optimalizálom** (§10.5), nem felületként.

---

## 0.0 Változásnapló — a második iteráció

Az első átadás után az ügyfél négy irányt kért, amelyek részben **felülírják**
az akkori javaslataimat. Itt rögzítem, mi változott, és mit fizettünk érte —
hogy a döntés visszakereshető maradjon.

| Kérés | Mi volt előtte | Mi lett | Mit fizettünk érte |
|---|---|---|---|
| „Legyenek animációk" | Szándékosan visszafogott mozgás, nulla görgetés-animáció (régi D13) | 22 tételes mikrointerakció-készlet, görgetésre megjelenés, lebegő háttérfoltok (§8) | +2,7 kB CSS, +3,4 kB JS. A JS így **11,1 kB nyers** — a briefben kért 5–10 kB fölött; tömörítve 4,0 kB. |
| „fehér-bézs-cián-babarózsaszín" | Anyagnév-alapú paletta a műhely nyersanyagaiból (meggy, kakaó, piskóta) | A kért négy szín, kilenc tokenre bontva, minden kontraszt újramérve (§7.1) | A paletta már **nem vezethető le** a szakmából; ez most márkadöntés, nem érv (§3.6). |
| „térhatású elemek" | Sík, matt felületek, hajszálvonalak | Valódi CSS 3D: kiterjedt szelet, egérrel dönthető kártyák, 3D gombnyomódás (§8, §9.7) | +1,9 kB CSS. `transform-style: preserve-3d` mobilon GPU-memóriát eszik — ezért a döntés csak egérrel érhető el. |
| „esztétikus képek süteményekről" | Nulla kép, szándékosan (a fotó a tetőt mutatja, nem a szerkezetet) | Négy saját SVG-illusztráció (11,5 kB nyers, 2,5 kB tömörítve) + előkészített `<picture>` foglalatok | **Nem fotók**, és nem a Krém termékei. Jogtiszta fotóbank nem volt elérhető (§9.3). |

**Amit nem adtam fel:** egy H1, teljes heading-hierarchia, mért kontrasztok,
akadálymentes űrlap, `prefers-reduced-motion`, nulla külső kérés, és az, hogy
egyetlen kitalált ár, nyitvatartás vagy kapacitás sincs az oldalon.

---

## 0. Kontextus — amit tudok, és amit nem

A brief kontextusmezői üresen érkeztek. Az alábbi táblázat **csak dokumentált
tényeket** tartalmaz.

| Mező | Amit tudok | Forrás / bizonyosság |
|---|---|---|
| Ügyfél | Krém Desszertműhely és Kávézó | listing · **magas** |
| Cím | 7632 Pécs, Zsuzsanna u. 2. | listing · **magas** |
| Telefon | 06 30 609 7009 — **mobilszám** | listing · **magas** |
| Kategória | Kávézó (Google-kategória) | listing · **magas** |
| Értékelés | **5,0 ★ / 16 értékelés** | listing · **magas** (napi szinten változhat) |
| Ársáv | személyenként **1–2000 Ft** | Google-attribútum · **magas** |
| Nyitás | **11:00**; a lekérdezés pillanatában „Zárva" | listing · **magas** |
| Záróidő, heti rend | **ismeretlen** | — |
| SMS-csatorna | a listingen ott a „Szöveges üzenet" gomb — mobilszám lévén az SMS él | listing · **magas** |
| Profil gazdája | „Bejelentette 7 személy" → az adatok jelentős része **felhasználói bejelentésből** van, nem tulajdonosi szerkesztésből | listing · **közepes — ellenőrizendő** |
| Saját webhely | a listingen van „Webhely" gomb, de **semmi nincs indexelve** rá | keresés · **közepes** |
| Városrész | 7632 = Pécs Kertváros / Uránváros környéke | irányítószám · **közepes** |
| Étlap, árak, allergének | **ismeretlen** | — |
| Kapacitás, ülőhely, terasz | **ismeretlen** | — |
| Fotóanyag | **nincs jogtiszta kép a birtokomban** | — |

### 0.1 Munkahipotézisek

Ezek nélkül nem lehet oldalt tervezni; mindegyik a §15-ben megerősítendő, és
addig ezek alapján dolgoztam.

- **Az oldal EGY dolga: desszert- és tortaelőrendelés egy konkrét dátumra.**
  Indoklás: az 1–2000 Ft/fő ársáv azt jelenti, hogy az *egyszeri betérés*
  értéke pár száz–kétezer forint, és azt a Google Térkép amúgy is elviszi
  (útvonal + hívás gombra kattint, aki már döntött). Amit egy webhely érdemben
  befolyásolni tud, az a **tervezett, nagyobb tételű vásárlás**: névnapra,
  szülinapra, céges délutánra rendelt torta vagy válogatás. Ez az egyetlen
  konverzió, aminél a weboldal a döntés helye, nem csak az útvonal.
- **Másodlagos, egyenrangú kimenet: telefonhívás és SMS.** A szám mobil, a
  Google is felkínálja az SMS-t — ez már ma is működő csatorna, nem szabad
  elvenni tőle a forgalmat, csak kiegészíteni.
- **Célközönség:** (a) a környék lakói, akik délután desszertért ugranak be —
  őket a *mai kínálat* és a nyitvatartás érdekli; (b) 25–55, aki egy adott
  napra keres tortát, és ma ezt Facebook-üzenetben vagy telefonon intézi; (c)
  allergiával/diétával élők, akik ma nem mernek betérni, mert nincs információ.
- **Amit nem szabad megváltoztatni:** a „Krém" márkanév, a
  „Desszertműhely és Kávézó" alcím, a telefonszám, a cím. A `Desszertműhely`
  szó **stratégiai eszköz**, nem véletlen: megkülönböztet a „cukrászdától".

---

## 1. A jelenlegi digitális jelenlét elemzése

### 1.1 Technológia

Nincs mit elemezni a szó szokásos értelmében: **nincs vizsgálható saját
kódbázis.** A jelenlegi felület a Google Cégprofil szerver oldalon renderelt
nézete (Maps/Search kártya). Ebből következik:

| Réteg | Ki birtokolja | Mit lehet vele tenni |
|---|---|---|
| Layout, tipográfia, komponensek | Google | semmit |
| Adattartalom (név, cím, óra, attribútumok) | tulajdonos **vagy** felhasználói bejelentés | a profil igénylésével teljesen |
| Fotók | tulajdonos + vendégek | feltöltéssel |
| Értékelések | vendégek | csak válaszolni lehet |
| Konverziós gombok | Google | csak a mögöttes adatot (tel, URL) |

### 1.2 Struktúra

```
Név ─ Értékelés (5,0 · 16) ─ Ársáv (1–2000 Ft) ─ Kategória ─ Állapot (Zárva)
Gombsor: Hívás · Útvonal · SMS · Webhely · Megosztás · Mentés
Cím ─ Térkép-kivágat
Állapotsor: „Zárva · Nyitás: 11:00"
Attribútum: „Személyenként 1–2000 Ft"
Adatforrás-jelzés: „Bejelentette 7 személy"
Telefonszám
```

### 1.3 MI A JÓ BENNE — külön szedve, és megtartandó

Ez nem udvariassági szakasz. Hat olyan dolog van itt, ami **működik**, és amit
az új oldalon meg kell tartani, nem lecserélni.

| # | Ami jó | Miért jó | Hogyan él tovább az új oldalon |
|---|---|---|---|
| J1 | **5,0 ★ / 16 értékelés** | Ennél erősebb bizalmi jel nem létezik ebben a méretben. Nem vásárolt, nem szerkeszthető. | Hero-tényadat + saját szekció, forrásmegjelöléssel. **Nem** strukturált adatként — indoklás: §10.3 |
| J2 | **A gombsor (Hívás / Útvonal / SMS)** | Egy koppintásos, kontextusfüggő cselekvések. Ez jobb konverziós UI, mint amit a legtöbb éttermi weboldal csinál. | Mobilon fix alsó cselekvési sáv, ugyanezzel a logikával; az SMS-link megmarad (`sms:`) |
| J3 | **Valós idejű nyitva/zárva állapot** | Megválaszolja a leggyakoribb kérdést, mielőtt felmerül. | Fejlécbe épített jelző, egyetlen nyitvatartás-objektumból számolva |
| J4 | **Kiírt ársáv (1–2000 Ft / fő)** | Ritka őszinteség. A vendéglátásban az árelhallgatás a norma, és költséges: aki nem tudja, mit fog fizetni, nem indul el. | Hero-tényadat, kiemelve. Nem rejtjük el egy „árlista" aloldalra |
| J5 | **A név: „Desszertműhely", nem „cukrászda"** | Pozicionálási döntés, ami már megtörtént: műhely = kézi munka, kis széria, felelős készítő. | Az **egész vizuális irány** ebből a szóból nő ki (§3.6) |
| J6 | **Mobilszám, nem vezetékes** | Azt jelenti, hogy a tulajdonos maga veszi fel, és SMS-ben is elérhető. Kisvállalkozásnál ez előny, nem hiányosság. | „Hívás" és „SMS küldése ugyanerre a számra" külön, egyenrangú linkként |

### 1.4 Amit a listing nem tud, és nem is fog

Fotó a termékről; étlap; ár tételesen; allergének; előrendelés; a műhely
története; a záróidő; annak magyarázata, miért 11:00 a nyitás.

---

## 2. Problémalista bizonyítékkal

### 2.1 Kritikus

| # | Probléma | Bizonyíték | Következmény |
|---|---|---|---|
| **K1** | **Nincs indexelt saját webhely.** | Célzott keresés a névre, a címre és a telefonszámra: nulla releváns találat. A találati listát más cégek töltik ki. | A cég a Google-on kívül gyakorlatilag nem létezik. Minden forgalom egyetlen, idegen tulajdonú felületen fut át. |
| **K2** | **A cégprofil láthatóan nem tulajdonosi kezelésben van.** | „Bejelentette 7 személy" — ez a Google jelzése arra, hogy az adatot felhasználók küldték be. | Bárki javasolhat módosítást a nyitvatartáson. Nincs Bejegyzés, nincs Termék, nincs Üzenetek, nincs válasz az értékelésekre. |
| **K3** | **Nincs nyilvános záróidő és heti rend.** | A listing csak a „Nyitás: 11:00"-t hozza. | Minden „vajon nyitva van?" kérdés vagy telefonhívás lesz, vagy — gyakrabban — elmaradt látogatás. |
| **K4** | **Nincs allergén- és összetevő-információ.** | Sehol semmi. | Ez élelmiszer-jogi kockázat is (1169/2011/EU: az allergénadatot kérésre elérhetővé kell tenni), és egy egész vendégcsoportot zár ki. |
| **K5** | **Márkanév-ütközés.** | Minden keresés a székesfehérvári *Krém Cukrászda és Kávézó* és a *kremcukraszda.hu* felé visz. | A saját márkanévre folytatott keresést más viszi el. Saját domain és tartalom nélkül ez nem javítható. |

### 2.2 UX

| # | Probléma | Bizonyíték | Következmény |
|---|---|---|---|
| U1 | Egyetlen szinkron csatorna (telefon). | A listing gombsora. | Aki este 21:00-kor tervez a hétvégére, nem tud mit kezdeni. A döntés elhalasztódik, és nem tér vissza. |
| U2 | Nulla termékinformáció. | Nincs étlap, nincs fotó a terméken kívül. | A „menjek-e" döntéshez nincs bemenet. Marad a találgatás. |
| U3 | A 11:00-s nyitás magyarázat nélkül áll. | listing. | Egy kávézónál a 11:00 szokatlanul késői. Magyarázat nélkül lustaságnak olvasható; magyarázattal (délelőtti gyártás) **előnnyé** válik. |
| U4 | Nincs előrendelési útvonal. | — | A legnagyobb értékű tranzakció (torta adott napra) ma nem támogatott, csak improvizált. |
| U5 | Az értékelésekre nincs válasz. | A profil nincs igényelve (K2). | 16 elégedett vendég, akikkel nincs második érintkezés. |

### 2.3 SEO

| # | Probléma | Bizonyíték |
|---|---|---|
| S1 | Nincs mit rangsorolni. | Nincs indexelt oldal — sem „desszert Pécs", sem „torta rendelés Pécs", sem „kávézó Kertváros" lekérdezésre. |
| S2 | Nincs NAP-konzisztencia. | A cég nem szerepel a pécsi cukrászda-gyűjtőoldalakon (Cylex, etterem.hu, cukraszturul), amelyek a keresésben megjelentek. |
| S3 | Nulla strukturált adat. | Nincs oldal, tehát nincs `LocalBusiness`. A Google csak a saját belső profiladatra támaszkodhat. |
| S4 | A márkanevet más birtokolja a találatokban. | lásd K5. |

### 2.4 Performance

Nincs mit mérni — nincs oldal. Ehelyett a mérce ez: **a jelenlegi belépőpont a
Google saját felülete, ami gyors.** Egy új oldal, ami lassabb a döntési úton,
mint a listing, rontani fog a helyzeten, nem javítani. Ebből lesz a §11
költségvetése.

Egyetlen mérhető tény: az ügyfélről **nincs jogtiszta képanyag**. Ez
performance-szempontból esély, nem hátrány — lásd §3.7, a szignatúra elemet.

---

## 3. Miért rosszak ezek — a mögöttes ok

A tünetlista fölött **egyetlen ok** áll, a többi ebből következik.

### 3.1 Az alapok: a cég digitálisan nem közzétett, hanem nyilvántartott

A Krém ma nem publikál, hanem *szerepel valahol*. Az adatait részben idegenek
töltik ki (K2). Ebből következik K1, K3, K4, S1, S3 és U2 is: aki nem publikál,
annak nincs mit indexelni, nincs mit strukturálni, és nincs miből dönteni.

Ez nem „hiányzik egy weboldal" típusú probléma. Ez tulajdonosi probléma:
a vállalkozás a saját adatainak nem gazdája.

### 3.2 A csatorna aszimmetriája: szinkron kínálat, aszinkron kereslet

A telefon akkor működik, ha mindkét fél ráér. A vendég viszont **este tervez a
holnaputánra** — pont akkor, amikor a műhely zárva van. Az U1 nem
kényelmetlenség, hanem strukturális veszteség: a kereslet és a felvevőképesség
időben nem fedik egymást. Egy űrlap nem azért kell, mert modern, hanem mert
**aszinkron**: a kérés megvárja a reggelt.

### 3.3 A bizalmi eszköz nincs kihasználva, és romlékony

Az 5,0/16 két dolgot mond egyszerre. Egy: a termék rendben van, tehát **nem
termékprobléma van, hanem elosztási**. Kettő: 16 elem statisztikailag törékeny —
két rossz értékelés 4,6-ra viszi. Tehát az 5,0-t (a) most kell konvertálni, és
(b) folyamatosan hígítani kell újakkal. Ez az oka annak, hogy az „Írj
értékelést" nem lábjegyzet lesz, hanem gomb (§12).

### 3.4 Az információhiány nem semleges: aktívan taszít

Az U2/K4 mögötti ok: **egy desszertnél a döntés kockázatos.** Nem tudom, mi van
benne; nem tudom, mennyi; nem tudom, van-e még. Egy fotó ezen keveset segít —
a fotó a *tetejét* mutatja. Az információ, ami hiányzik, a **belső szerkezet**.
Ebből a felismerésből lesz a szignatúra elem (§3.7): nem díszítés, hanem a hiányzó
információ formája.

### 3.5 A 11:00 nem hiba, hanem el nem mondott előny

Egy desszertműhelynél a délelőtt gyártás. A késői nyitás **ennek a
következménye**, tehát minőségi jelzés — csak nincs kimondva. A tünet
(„furcsa nyitvatartás") és az ok („kézi gyártás előzi meg") ugyanaz a tény,
ellenkező előjellel. Ezért kap a nyitvatartás önálló, magyarázó szekciót,
és nem csak egy táblázatsort.

---

## 3.6 A vizuális kiindulópont — egy mondatban

> **A kiindulópont a felvágott desszert keresztmetszete: az a nézet, amit csak
> akkor lát az ember, amikor a műhely már elvégezte a munkát — ezért a szerkezet
> a rétegekből, a sorrendből és az arányokból épül, a felület pedig térbeli:
> a szelet nem rajz, hanem kiterjedt test, aminek látszik az oldala és a teteje.**

### 3.6.1 A paletta — és egy őszinte megjegyzés

Az első iterációban a paletta **anyagnevekből** jött: minden szín egy nyersanyag
volt a műhelyből (meggy, kakaó, piskóta, pisztácia), és a szabály az volt, hogy
ami nem nevezhető meg anyaggal, az nem kerül be. Ez a szabály tartotta a
palettát a szakmához kötve.

Az ügyfél a **fehér – bézs – cián – babarózsaszín** négyest kérte. Ez az
ügyfél döntése, és így is szállítom. Amit ezzel elveszítünk, azt itt kimondom,
hogy később ne kelljen kitalálni:

- **A paletta ettől kezdve márkadöntés, nem levezetés.** Nincs mögötte olyan
  érv, hogy „mert ilyen egy karamell". Ha valaki megkérdezi, miért cián, a
  válasz az, hogy az ügyfél így kérte — ez teljesen legitim válasz, csak nem
  ugyanaz, mint egy indoklás.
- **A cián a magyar cukrászati hagyományban nem élelmiszerszín.** Ezt
  ellensúlyozza, hogy a szeletben csak mint *krém- és mousse-réteg* jelenik meg
  (mentás/menta-ízek), nem mint tésztaszín, és hogy a bézs és a fehér adja a
  felület nagy részét.
- **A babarózsaszín közel esik a „torta-marketing" alapértelmezéséhez**, amit az
  első briefed maga is tiltott. Ezt két dologgal tartom távol tőle: (a) a rózsaszín
  soha nem háttér, csak felület és réteg; (b) a szöveget hordozó akcent nem a
  babarózsaszín, hanem a **mély cián** (`#046B7E`) és a **mély málna** (`#C0396B`) —
  a pasztellek dekorációt visznek, nem információt.

Amit **megnyertünk**: a paletta világos és sötét témán is nagyon jól szétválik,
és a négy szín elég távol áll egymástól ahhoz, hogy a rétegek egy 22 px-es
színchipen is megkülönböztethetők legyenek.

---

## 3.7 A szignatúra elem — „A háromdimenziós szelet"

### Mi ez

Egy desszert **kiterjedt teste**, nem a rajza. A CSS `transform-style:
preserve-3d`-vel minden réteg kap egy jobb oldallapot, a legfelső egy tetőlapot,
és az egész test `perspective` alatt áll — így a szelet elülső lapja *maga a
keresztmetszet*, miközben a hasáb oldala és teteje is látszik. Egérrel a test
követi a kurzort; egér nélkül lassan hintázik. Egy réteget kiválasztva az
**a néző felé csúszik ki** (`translateZ(34px)`), a többi visszahalványul.

Mellette a rétegek listája: minden réteg neve és **funkciója** — nem az
összetevője, hanem hogy mit **csinál** („tartás — enélkül összeesik").

### Miért pont ez

1. **Megmutatja, nem elmondja.** A „műhely" szó azt állítja, hogy itt kézzel
   épített, összetett dolgok készülnek. A térbeli szelet ezt bizonyítja: hét
   réteg, hét döntés, és a vágott lap az, ami elárulja őket.
2. **A hiányzó információt adja meg.** §3.4: a döntés kockázata a belső
   szerkezet nem ismerete.
3. **A 3D itt nem díszítés, hanem a metafora befejezése.** Egy lapos rajz
   *ábrázolja* a keresztmetszetet; egy kiterjedt test **megmutatja, hogy van
   miből metszetet venni**. Ez az egyetlen hely az oldalon, ahol a térhatás
   tartalmat hordoz — a többi (kártyadöntés, gombnyomódás) visszajelzés.
4. **Nem fotón múlik.** Az ügyfélnek nincs jogtiszta fotóanyaga (§9.3).

### Mibe kerül LCP-ben

Megmérve a leszállított prototípuson:

| Tétel | Méret |
|---|---|
| A 3D szelet HTML-je | **954 B** |
| A hozzá tartozó CSS | **5 151 B** |
| Hálózati kérés | **0** |
| Képdekódolás | **0 ms** |
| Elrendezés-ugrás (CLS) | **0** — minden sáv fix `--h` magasságú |

**LCP-hatás: gyakorlatilag nulla, és negatív egy fotós alternatívához képest.**
Egy 1200 px széles, jól optimalizált AVIF hero 60–110 kB, plusz egy külön
hálózati kérés, plusz dekódolás. Így a legnagyobb festett elem a `H1` szövege,
tehát **LCP ≈ FCP**.

**Amit a 3D ténylegesen kerül:** nem bájtot, hanem **kompozitálást**. A
`preserve-3d` réteg saját GPU-textúrát kap. Ezért: a szelet a hajtás fölött
egyetlen ilyen réteg, a kártyák pedig csak hover alatt lépnek 3D-be, és
érintőeszközön (`pointer: coarse`) a JS **be sem köti** a döntést.

### Fegyelem — hova költöttük a merészséget

A háttérfoltok, a görgetésre megjelenés és a gombnyomódás mind **halk**:
0,38 opacitás, 26 px elmozdulás, 3 px gombsüllyedés. Egy hangos elem van, a
szelet. A sorszámozás sehol nem jelenik meg olyan tartalmon, aminek nincs valódi
sorrendje.

## 4. Új információs architektúra és sitemap

Alapelv: **minden URL egy kérdésre válaszol, amit egy valódi ember tesz fel.**
Ha nincs ilyen kérdés, nincs URL. Öt oldal indul, kettő a második fázisban jön.

| URL | A kérdés, amire válaszol | Miért önálló URL | Elsődleges cselekvés |
|---|---|---|---|
| `/` | „Mi ez a hely, és mit kapok itt?" | Ez a márkanév-keresés és a Google-listing „Webhely" gombjának célja. Mindent érint, semmit nem merít ki. | Előrendelés |
| `/kinalat/` | „Mi kapható, mennyiért, mi van benne?" | Ez a leggyakoribb belépő a nem-márkás keresésekből („desszert Pécs"). Külön URL kell, mert **linkelhetőnek és megosztható**nak kell lennie, és mert itt lesz a legtöbb tartalomfrissítés. | Előrendelés / útvonal |
| `/elorendeles/` | „Hogyan kérek egy adott napra?" | A fő konverzió önálló URL-en: hirdethető, mérhető, SMS-ben és Google-Bejegyzésben megosztható. A főoldali űrlapszekció ide horgonyzik (`/#elorendeles`), a `/elorendeles/` a teljes lap. | Űrlap beküldése |
| `/a-muhely/` | „Kik ezek, és miért 11-kor nyitnak?" | A késői nyitás magyarázata (§3.5) és a NAP-adatok kanonikus helye. Ez az oldal viszi a `LocalBusiness` részleteket. | Hívás / útvonal |
| `/allergenek/` | „Ehetem ezt?" | Külön URL, mert (a) jogi tartalom, (b) hosszú táblázat, (c) más keresési szándék („gluténmentes desszert Pécs"). | Előrendelés |
| `/velemenyek/` **(2. fázis)** | „Mások mit mondanak?" | **Csak akkor**, ha az értékelésszám tartósan 40 fölé megy. 16 véleményből aloldal nem lesz, csak vékony tartalom. Addig a főoldal szekciója viszi. | Értékelés írása |
| `/tortak/` **(2. fázis)** | „Rendelhetek egész tortát méretre?" | Csak akkor, ha kiderül, hogy ez önálló szolgáltatás saját méret-/ár-/határidőlogikával (§15/4). Addig a `/elorendeles/` egy választógombja. | Űrlap |

### 4.1 Amit szándékosan NEM építünk

| Nem lesz | Miért |
|---|---|
| Webshop / online fizetés | 1–2000 Ft/fő ársávnál a fizetési integráció fenntartási költsége nagyobb, mint a haszna. Az előrendelés kérés + telefonos visszaigazolás. |
| Blog | Nincs kapacitás fenntartani. Egy elhagyott blog rosszabb, mint a nem létező. |
| Galéria-aloldal | Nincs képanyag (§15/2). Ha lesz, a `/kinalat/` sorai kapnak fotót, nem külön galéria. |
| Nyelvváltó | Pécs turisztikai város, de Kertváros nem turistanegyed. Angol verzió akkor, ha a §15/9 kérdésre az a válasz, hogy jelentős a külföldi vendég. |

---

## 5. Oldalankénti felépítés

### 5.1 `/` — Főoldal (ez készült el prototípusként)

| # | Szekció | Tartalom | Cél | Megjegyzés |
|---|---|---|---|---|
| 1 | Fejléc | Logó, nav, **élő nyitva/zárva jelző** (lüktető ponttal, ha nyitva), téma-kapcsoló | Orientáció + a leggyakoribb kérdés azonnali megválaszolása | A jelző ugyanabból az objektumból számol, mint az űrlap-validáció |
| 2 | Hero | H1, egy bekezdés, két CTA, **4 tényadat-kártya** (5,0 / ársáv / nyitás / cím) | A „hova kerültem és megéri-e" 5 másodperc alatt | Mögötte két lassan sodródó, elmosott színfolt |
| 3 | **A 3D szelet** | A szignatúra elem, 7 réteggel, egérrel dönthető | Megmutatni, mit jelent a „műhely" | §3.7 |
| 4 | A műhely rendje | Három emelkedő lap: bejössz / hívsz-írsz / előre kéred | A csatornák egyenrangúsítása, az U1 feloldása | Nem sorszámozott lépéssor: három **párhuzamos** út |
| 5 | Kínálat | 4 térhatású kártya saját SVG-illusztrációval, allergénjelekkel, árral | A döntés bemenete (U2, K4) | Prototípusban mintaadat; a valódi fotó helye előkészítve (§9.3) |
| 6 | **Előrendelés** | Akadálymentes űrlap + magyarázó oszlop | A fő konverzió | Bal oldalt: miért kérjük az adatot |
| 7 | Hol és mikor | Cím, hívás, SMS, útvonal, heti nyitvatartás | NAP-konzisztencia + a K3 feloldása | A táblázat generált, egy forrásból |
| 8 | Vélemények | 5,0 · 16, forrással; „Írj értékelést" | A J1 konvertálása és hígítása (§3.3) | Nincs `aggregateRating` markup (§10.3) |
| 9 | GYIK | 4 kérdés | A telefonhívások egy részének kiváltása | `FAQPage` markup |
| 10 | Lábléc | NAP, oldalak, kötelező linkek | Jogi + bejárhatóság | |
| M | Mobil cselekvési sáv | Előrendelés + Hívás, fix | A J2 mintájának átvétele | Csak <960 px |

Minden szekció **görgetésre úszik be**, testvérenként 70 ms lépcsőzéssel (A13),
és a `.rejt` osztály csak futó JS mellett rejt (§8.3).

### 5.2 `/kinalat/`

| # | Szekció | Tartalom | Cél |
|---|---|---|---|
| 1 | Fejléc + „ma a pultban" sáv | Aznapi elérhetőség | A legfrissebb információ legfölül |
| 2 | Szűrő | allergénmentesség szerint (glutén / laktóz / tojás / dióféle) | A K4 gyakorlati feloldása |
| 3 | Kategóriák | szeletes / egész torta / kávé és ital | Böngészhetőség |
| 4 | Tételsorok | mini keresztmetszet + név + rétegsor + allergének + ár | A döntés bemenete |
| 5 | Rendelési sáv (ragadós) | „Ezt előre kérem" → `/elorendeles/?tetel=…` | Konverzió a böngészés közben |
| 6 | Allergén-jelmagyarázat | | Jogi + érthetőség |

### 5.3 `/elorendeles/`

| # | Szekció | Tartalom | Cél |
|---|---|---|---|
| 1 | Fejléc + a feltételek | határidő, minimális mennyiség, fizetés módja | Elvárás-kezelés a kitöltés **előtt** |
| 2 | Űrlap | ugyanaz, mint a főoldalon | Konverzió |
| 3 | „Mi történik ezután" | 3 lépés, valós időkkel | A bizonytalanság csökkentése |
| 4 | Alternatív csatornák | hívás, SMS | Aki nem akar űrlapot |

### 5.4 `/a-muhely/`

| # | Szekció | Tartalom | Cél |
|---|---|---|---|
| 1 | A nap rendje | gyártás → 11:00 nyitás → elfogy | A §3.5 kimondása |
| 2 | A készítő | név, háttér | Bizalom kisvállalkozásnál |
| 3 | Megközelítés | busz, parkolás, bejárat | A helyszínre jutás |
| 4 | Nyitvatartás | kanonikus táblázat + ünnepnapi eltérések | K3 |

### 5.5 `/allergenek/`

| # | Szekció | Tartalom | Cél |
|---|---|---|---|
| 1 | Bevezető | mit vállalunk, mit nem (keresztszennyeződés!) | Jogi pontosság |
| 2 | Táblázat | tétel × 14 EU-allergén | Kereshető, rendezhető |
| 3 | Kapcsolat | „ha bizonytalan vagy, hívj" | Felelősség-visszavezetés emberhez |

---

## 6. Wireframe

### 6.1 Főoldal — desktop (≥1100 px, tartalomsáv 1180 px)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ [Ugrás a tartalomra]  ← csak fókusszal látható                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ Krém  DESSZERTMŰHELY & KÁVÉZÓ   Kínálat Előrendelés A műhely Hol             │
│  ▲gradiens                        ( ● Most nyitva · 18:00-ig )  [☀][▭][☾]    │  ragadós, 68 px
├──────────────────────────────────────────────────────────────────────────────┤
│  ░░ cián folt (blur 70px, sodródik 26s)          ░░ rózsa folt (32s) ░░       │
│                                                                              │
│  Krém Desszertműhely és Kávézó —      ┌───────────────────────────────────┐  │
│  Pécs, Zsuzsanna utca                 │ [a nap desszertje]        (MINTA) │  │
│  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ H1, az „em" rész     │                                   │  │
│   cián→málna gradienssel              │        ╱▔▔▔▔▔▔▔▔▔▔╲              │  │
│                                       │      ╱▁▁▁▁▁▁▁▁▁▁╱ │  ← tetőlap   │  │
│  Tizenhat Google-értékelés, egy sem   │     │▓▓▓ glazúr ▓│ │              │  │
│  kevesebb ötnél. Tizenegykor          │     │▒▒▒ zselé ▒▒│ │  ← oldallap  │  │
│  nyitunk. Egy kávé és egy desszert    │     │░░ mousse ░░│ │              │  │
│  személyenként 2000 Ft alatt kijön.   │     │▓▓ piskóta ▓│ │              │  │
│                                       │     │▚▚▚ alap ▚▚▚│╱               │  │
│  ╭───────────────────╮ ╭────────────╮ │      ╲▁▁▁▁▁▁▁▁▁╱                 │  │
│  │Desszertet rendelnék│ │06 30 609 …│ │        ~~~ árnyék ~~~            │  │
│  ╰───────────────────╯ ╰────────────╯ │   ▲ VALÓDI CSS 3D, egérrel dönthető│ │
│   ▲ fénycsík hoverre, −3px emelkedés  │                                   │  │
│                                       │  ■ Tükörglazúr  lezár, és eltak…  │  │
│  ┌────────┐┌────────┐┌────────┐┌────┐ │  ■ Málnazselé   savas ellenpont   │  │
│  │ÉRTÉKEL.││ÁRSÁV   ││NYITÁS  ││CÍM │ │  ■ Mentás mousse  a tömeg         │  │
│  │  5,0   ││1–2000Ft││ 11:00  ││Zsu…│ │  … (7 sor, mind 50 px gomb)       │  │
│  │16 érté.││/fő     ││zárás?  ││7632│ │                                   │  │
│  └────────┘└────────┘└────────┘└────┘ │  Ez a szelet nem kép, hanem…      │  │
│    ▲ hoverre −4px                     └───────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────────┤
│  ▬▬ A MŰHELY RENDJE                                                          │
│  Három út vezet ide, és nem egyforma sürgős mind a három                      │
│  ┌═══════════════┐  ┌═══════════════┐  ┌═══════════════┐   ← felső élük      │
│  │ 11:00-tól     │  │ Bármikor      │  │ Előre         │     cián→rózsa      │
│  │ Bejössz       │  │ Hívsz vagy írsz│  │ Kitöltöd…     │     gradiens       │
│  │ Zsuzsanna u…  │  │ 06 30 609 7009│  │ Konkrét napra │                     │
│  └───────────────┘  └───────────────┘  └───────────────┘   hoverre −6px      │
├──────────────────────────────────────────────────────────────────────────────┤
│  ▬▬ KÍNÁLAT                                                                  │
│  Ami a pultban áll                                                            │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐  ← 4 oszlop         │
│  │ ┌───────┐ │ │ ┌───────┐ │ │ ┌───────┐ │ │ ┌───────┐ │                     │
│  │ │  SVG  │ │ │ │  SVG  │ │ │ │  SVG  │ │ │ │  SVG  │ │  a kép translateZ   │
│  │ │ szelet│ │ │ │macaron│ │ │ │ tart  │ │ │ │ torta │ │  (34px)-en lebeg    │
│  │ └───────┘ │ │ └───────┘ │ │ └───────┘ │ │ └───────┘ │                     │
│  │[málnás-…] │ │[macaron-…]│ │[gyümölcs…]│ │[egész t…] │                     │
│  │ Hat réteg…│ │ Mandula…  │ │ Omlós…    │ │ Csak elő… │                     │
│  │(tojás)(tej)│ │(tojás)(tej)│ │(tojás)(tej)│ │(csak elő…)│                   │
│  │[ár] Előre │ │[ár] Előre │ │[ár] Előre │ │[ár] Előre │  ← a lábak igazítva │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘                     │
│   ▲ egérrel ±4,5° dőlés + a kurzort követő fényfolt                          │
│  „A négy tétel mintaadat, az ábrák saját illusztrációk — nem a Krém termékei" │
├──────────────────────────────────────────────────────────────────────────────┤
│  ELŐRENDELÉS  (mélyebb felület-tónus, teljes szélességű sáv, cián folt)       │
│  Mondd meg, mikorra és      ┌─ kiemelt kártya ────────────────────────────┐  │
│  mennyit                    │ Mit szeretnél? *                             │  │
│                             │ ┌(o)Szeletes┐┌(o)Egész t.┐┌(o)Macaron┐      │  │
│  Ez egy kérés, nem          │ ├─ Hány adag? * ───────────────────────────┤ │  │
│  visszaigazolt rendelés…    │ │ [                                      ] │ │  │
│  ▬ Miért van benne az       │ ├─ Mikorra kell? * ────────────────────────┤ │  │
│    átvétel órája?           │ │ [ 2026-09-20                         📅] │ │  │
│  ▬ Miért kérünk telefont?   │ ├─ Átvétel körülbelül * ───────────────────┤ │  │
│  ▬ Miért van allergia-mező? │ │ … név* / telefon* / e-mail / megjegyzés  │ │  │
│                             │ │ [x] Tudomásul veszem… *                  │ │  │
│                             │ │ ╭──────────────────╮                     │ │  │
│                             │ │ │ Kérés elküldése  │                     │ │  │
│                             │ │ ╰──────────────────╯                     │ │  │
│                             └──────────────────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────────┤
│  ▬▬ HOL ÉS MIKOR                                                             │
│  ┌──── panel ─────────────┐  ┌──── panel ─────────────────────────────────┐  │
│  │ Krém Desszertműhely…   │  │ Nyitvatartás                                │  │
│  │ Zsuzsanna u. 2., 7632  │  │ Hétfő      11:00 – 18:00  ← MA kiemelve     │  │
│  │ → Hívás → SMS → Útvonal│  │ Kedd       11:00 – 18:00                    │  │
│  └────────────────────────┘  └─────────────────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────────┤
│  ▬▬ AMIT MÁSOK MONDANAK                                                      │
│  ┌──── panel ─────────────┐  ┌──── panel ─────────────────────────────────┐  │
│  │ 5,0  16 értékelés      │  │ [3 kiemelt vélemény helye]                  │  │
│  │ ★★★★★  Forrás: Google… │  │                                             │  │
│  │ ╭Írj te is értékelést╮ │  │                                             │  │
│  └────────────────────────┘  └─────────────────────────────────────────────┘  │
│  Gyakori kérdések                                                             │
│  ▸ Mikor van nyitva?   ▸ Mennyibe kerül?   ▸ Lehet előre rendelni?            │
├──────────────────────────────────────────────────────────────────────────────┤
│  LÁBLÉC   NAP-adatok │ Oldalak │ Kötelező (adatkezelés, impresszum, allergén) │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Főoldal — mobil (375–430 px)

```
┌───────────────────────────────┐
│ Krém              [☀][▭][☾]   │ ← ragadós; a nav és az állapotjelző elrejtve
├───────────────────────────────┤
│ ░░ cián folt (halványabb) ░░  │
│ Krém                          │
│ Desszertműhely                │
│ és Kávézó —                   │
│ Pécs,                         │  ← H1 36 px; az „em" rész gradienssel
│ Zsuzsanna utca                │
│                               │
│ Tizenhat Google-értékelés,    │
│ egy sem kevesebb ötnél…       │
│                               │
│ ┌───────────┐ ┌─────────────┐ │  ← a tényadatok 2 oszlopban, kártyaként
│ │ÉRTÉKELÉS  │ │ÁRSÁV        │ │
│ │5,0        │ │1–2000 Ft    │ │
│ └───────────┘ └─────────────┘ │
│ ┌───────────┐ ┌─────────────┐ │
│ │NYITÁS 11:00│ │CÍM Zsuzs. 2│ │
│ └───────────┘ └─────────────┘ │
├───────────────────────────────┤
│ ┌───────────────────────────┐ │
│ │[a nap desszertje] (MINTA) │ │
│ │      ╱▔▔▔▔▔▔╲             │ │  ← a 3D szelet marad, de NEM követi
│ │     │▓▓▓▓▓▓│ │            │ │    a kurzort (nincs kurzor);
│ │     │░░░░░░│ │            │ │    a lassú hintázás megy tovább
│ │      ╲▁▁▁▁▁╱              │ │
│ │ ■ Tükörglazúr             │ │  ← a rétegek listája ALÁ kerül,
│ │   lezár, és eltakarja…    │ │    minden sor 50 px magas gomb
│ │ … (7 sor)                 │ │
│ └───────────────────────────┘ │
├───────────────────────────────┤
│ ▬▬ A MŰHELY RENDJE            │
│ ┌───────────────────────────┐ │  ← a három lap egymás alatt,
│ │═══ 11:00-tól              │ │    felső élük gradiens
│ │ Bejössz …                 │ │
│ └───────────────────────────┘ │
│ (×3)                          │
├───────────────────────────────┤
│ ▬▬ KÍNÁLAT                    │
│ ┌───────────────────────────┐ │  ← 1 oszlop; a kártya SÍK marad
│ │ ┌───────────────────────┐ │ │    (érintőn nincs dőlés – D18)
│ │ │      SVG szelet       │ │ │
│ │ └───────────────────────┘ │ │
│ │ [málnás-mentás szelet]    │ │
│ │ Hat réteg: tükörglazúr…   │ │
│ │ (tojás)(tej)(glutén)      │ │
│ │ [ár]          Előre kérem │ │
│ └───────────────────────────┘ │
│ (×4)                          │
├───────────────────────────────┤
│ ELŐRENDELÉS                   │
│ Mit szeretnél? *              │
│ ┌───────────┐ ┌─────────────┐ │  ← 2 oszlopos rács, 56 px célpontok
│ │(o)Szeletes│ │(o)Egész torta│ │
│ └───────────┘ └─────────────┘ │
│ Hány adag? *                  │
│ [                           ] │  ← input 50 px, 16 px betű
│ ⓘ Add meg, hány adagot kérsz. │  ← hiba a mező ALATT, beúszik
│ …                             │
│ [ Kérés elküldése ]           │
├───────────────────────────────┤
│ HOL ÉS MIKOR / VÉLEMÉNYEK /   │
│ GYIK / LÁBLÉC (egy oszlop)    │
├───────────────────────────────┤
│▒▒▒▒▒ 90 px hely a fix sávnak ▒│
└───────────────────────────────┘
┌───────────────────────────────┐
│ [  Előrendelés  ] [ 📞 ]      │ ← FIX alsó sáv, safe-area-inset-bottom
└───────────────────────────────┘
```

### 6.3 Az űrlap hibaállapota (mindkét nézetben azonos logika)

```
┌─────────────────────────────────────────────┐
│ ┃ A küldés nem ment el                      │  ← 2 px accent keret, fókuszt kap
│ ┃ Az alábbi mezőket kell javítani:          │     (tabindex="-1")
│ ┃ 1. Mit szeretnél — Válassz a négy…        │  ← ugróhivatkozás a mezőre
│ ┃ 2. Mikorra kell — Add meg a napot.        │
│ ┃ 3. Telefonszám — Ez így nem tűnik…        │
└─────────────────────────────────────────────┘
   …
   Mikorra kell? *
   Zárva tartó napra nem lehet átvételt kérni.   ← segítő szöveg, MINDIG látszik
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ← 2 px accent keret + halvány
  ┃                                       📅 ┃     accent háttér
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
   ⓘ Legalább 2 nappal előbb kérjük a leadást.   ← role="alert", a mező ALATT
```

---

## 7. Design system

### 7.1 Szín — 9 nevesített token, mért kontraszttal

Az ügyfél által kért **fehér – bézs – cián – babarózsaszín** négyest kilenc
tokenre bontottam. A négy alapszín önmagában nem elég egy működő rendszerhez:
a cián és a babarózsaszín is világos, tehát egyik sem hordozhat szöveget fehér
vagy bézs háttéren. Ezért mindkettőnek van egy **mély párja** (szöveghez, CTA-hoz),
és van egy sötét „tinta", ami a ciánból származik — így a szövegszín is a
paletta családjában marad, nem szürke idegen test.

| # | Token | Világos | Sötét | Miből | Szerep |
|---|---|---|---|---|---|
| 1 | `--porcukor` | `#FFFFFF` | — | fehér | kártyafelület |
| 2 | `--vanilia` | `#FAF4EC` | — | bézs | oldalháttér |
| 3 | `--marcipan` | `#E4D2B8` | — | mély bézs | másodlagos felület |
| 4 | `--jegkrem` | `#00B7D4` | `#5FE0F2` | **cián** | dekor, chip, jelölés |
| 5 | `--menta` | `#046B7E` | `#5FE0F2` | mély cián | **link, elsődleges CTA** |
| 6 | `--babarozsa` | `#FFC7D9` | `#3A2430` | **babarózsaszín** | felület, réteg, dekor |
| 7 | `--malna` | `#C0396B` | `#FFB3CC` | mély rózsa | másodlagos CTA, hibaállapot |
| 8 | `--tinta` | `#10303A` | `#F2F7F8` | ciánból mélyítve | szöveg |
| 9 | `--fust` | `#5C6B72` | `#A8BCC4` | tinta hígítva | másodlagos szöveg |

Sötét témán az alap `#0C2129`, az emelt felület `#14323C`.

**Mért WCAG-kontrasztok** (relatív luminancia szerint számolva, nem becsülve):

| Pár | Világos | Sötét | Követelmény | Státusz |
|---|---|---|---|---|
| törzsszöveg a háttéren | **12,76:1** | **15,36:1** | 4,5:1 | AAA |
| törzsszöveg a kártyán | **13,95:1** | **12,53:1** | 4,5:1 | AAA |
| másodlagos szöveg a háttéren | **5,06:1** | **8,42:1** | 4,5:1 | AA / AAA |
| másodlagos szöveg a kártyán | **5,52:1** | **6,87:1** | 4,5:1 | AA |
| link / elsődleges akcent | **5,64:1** | **10,62:1** | 4,5:1 | AA / AAA |
| felirat az elsődleges CTA-n | **6,16:1** | **10,62:1** | 4,5:1 | AA / AAA |
| másodlagos akcent (málna) | **4,76:1** | **9,94:1** | 4,5:1 | AA / AAA |
| felirat a másodlagos CTA-n | **5,20:1** | **9,94:1** | 4,5:1 | AA / AAA |
| tinta babarózsaszín felületen | **9,58:1** | — | 4,5:1 | AAA |
| tinta cián felületen | **5,79:1** | — | 4,5:1 | AA |
| tinta marcipán felületen | **9,44:1** | — | 4,5:1 | AAA |
| vezérlőkeret a háttéren | **3,13:1** | **4,54:1** | 3:1 (1.4.11) | ✓ |
| vezérlőkeret a kártyán | **3,43:1** | **3,70:1** | 3:1 | ✓ |

**A pasztellek soha nem hordoznak szöveget.** A `--babarozsa` és a `--jegkrem`
felület és réteg; ha rájuk szöveg kerül, az mindig `--tinta` (9,58:1 és 5,79:1).
Ez az egyetlen szabály, ami megakadályozza, hogy a kért paletta olvashatatlanná
váljon.

**A sötét téma nem inverz.** A cián nem sötétedik, hanem **világosodik**
(`#046B7E` → `#5FE0F2`), a málna is (`#C0396B` → `#FFB3CC`). Sötét felületen a
telített szín égeti a szemet; a hígított marad felismerhetően ugyanaz a szín.

**Miért nincs duplikáció?** A tokenek `light-dark()`-kal vannak írva, minden
deklaráció előtt egy sima fallback-értékkel:

```css
--hatter:#FAF4EC;                          /* régi böngésző: mindig világos */
--hatter:light-dark(#FAF4EC,#0C2129);      /* modern: a color-scheme dönt */
```

*Alternatíva, amit nem választottam:* a teljes tokenkészlet megismétlése
`@media (prefers-color-scheme:dark)` és `[data-theme="dark"]` alatt. Az működik
mindenhol, de kétszer ~30 sor duplikáció. Az ára: 2023 előtti böngészőben nincs
sötét téma — de az elrendezés és a kontraszt ott is hibátlan.

**Két helyen mégis kellett a régi módszer:** a `light-dark()` a specifikáció
szerint **két színt** vesz, tehát (a) a többrétegű `box-shadow` és (b) a
háttérfoltok `opacity`-je nem fér bele. Az árnyéknál ezt úgy oldottam meg, hogy
**az árnyék színe témafüggő token, a geometria fix** (§7.4); az `opacity`-nél
két sor média-lekérdezés maradt. Ez a két kivétel a forrásban kommentelve van.

### 7.2 Tipográfia

Két variable betűcsalád, mindkettő **latin-ext lefedettséggel** — ellenőrizve,
hogy az `ő` (U+0151) és az `ű` (U+0171) benne van a rajzolt karakterkészletben,
nem helyettesítéssel jelenik meg.

| | Display | Szöveg |
|---|---|---|
| Család | **Fraunces** | **Commissioner** |
| Típus | variable soft-serif | variable humanista sans |
| Tengelyek eredetileg | `opsz 9–144`, `wght 100–900`, `SOFT 0–100`, `WONK 0–1` | `wght 100–900`, `slnt`, `FLAR`, `VOLM` |
| Amit szállítunk | `SOFT=25`, `WONK=1`, `opsz=48` rögzítve, `wght 300–900` marad | `slnt/FLAR/VOLM=0` rögzítve, `wght 300–800` marad |
| Méret (magyar subset, woff2) | **27,1 kB** | **24,7 kB** |

**Miért ez a kettő:**

- **Fraunces** azért, mert a `SOFT` tengelye szó szerint a terminálok
  lekerekítését szabályozza — egy desszertműhelynél ez nem metafora, hanem
  ugyanaz a mozdulat, amivel egy krémet elsimítanak. A `WONK=1` bekapcsolja a
  szabálytalanabb, „ferde" betűformákat: kézi munka, nem gépi. Old-style
  számformái vannak, és a latin-ext teljes.
- **Commissioner** azért, mert alacsony kontrasztú, humanista sans, ami 13 px-en
  is olvasható marad (allergénjelek, segítőszövegek), tabuláris számokat tud
  (árak, órák nem ugrálnak), és a terminálok enyhe kalligrafikus dőlése rímel a
  Fraunces lágyságára anélkül, hogy utánozná.

**A display face minimális használati mérete: 24 px, ajánlott 28 px fölött.**
Az `opsz=48`-ra rögzített példány vékony vonalvezetésű; 24 px alatt a hajszálak
elvesznek, különösen sötét témán. A prototípusban a Fraunces sehol nem megy
20 px alá: `H1` 36–68 px, `H2` 28–44 px, `H3` 22–30 px, logó 24 px,
tényadat-számok 22–30 px. **Minden 20 px alatti szöveg Commissioner.**

*Alternatívák, amiket elvetettem:*

| Alternatíva | Miért nem |
|---|---|
| Playfair Display + Inter | A brief tiltja, és jogosan: ez ma az AI- és sablonoldalak alapértelmezése. Semmit nem mond a szakmáról. |
| Bricolage Grotesque | Jó betű, de ipari/technikai a karaktere; egy műhelyhez illik, egy *desszert*műhelyhez nem. |
| Cormorant / Libre Baskerville | Irodalmi-elegáns. Ez a „fine dining cukrászda" közhely, és 1–2000 Ft/fő ársávnál hazugság. |
| Amatic SC (a design-system generátor javaslata) | Kézírás-imitáció. Törékeny, rosszul olvasható, és pont azt a „házias" közhelyet hozza, amitől a „műhely" szó megkülönböztetne. |
| Egyetlen családra szűkítés | Olcsóbb lenne 27 kB-tal, de akkor a „kézi munka" és a „pontos információ" két hangja ugyanaz lenne. A kettősség itt tartalom. |

**Típusskála** — folytonos `clamp()`, 375 px → 1440 px viewport között
lineáris, utána rögzül:

```css
--sz-2xs: .75rem;                                        /* 12 px  – csak címke  */
--sz-xs : clamp(.8125rem, .791rem + .094vw , .875rem);   /* 13→14  – segítő, jel */
--sz-s  : clamp(.9375rem, .916rem + .094vw , 1rem);      /* 15→16  – UI, lista   */
--sz-m  : clamp(1rem    , .956rem + .188vw , 1.125rem);  /* 16→18  – törzsszöveg */
--sz-l  : clamp(1.125rem, 1.037rem + .376vw, 1.375rem);  /* 18→22  – bevezető    */
--sz-xl : clamp(1.375rem, 1.199rem + .751vw, 1.875rem);  /* 22→30  – H3          */
--sz-2xl: clamp(1.75rem , 1.398rem + 1.502vw, 2.75rem);  /* 28→44  – H2          */
--sz-3xl: clamp(2.25rem , 1.546rem + 3.005vw, 4.25rem);  /* 36→68  – H1          */
```

Sormagasság: törzsszöveg 1.6, címsor 1.08. Sorhossz: `--keskeny: 68ch` a
folyószövegre, a hero-bevezetőn 46ch.

### 7.3 Térköz — 8 px alap

`4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128` (`--t-1` … `--t-10`).
A 4 px kizárólag ikon–szöveg illesztésre. Szekciók függőleges ritmusa:
mobil 64 px, desktop 96 px. Komponensen belüli csoportköz 24 px, elemköz 8–16 px.

### 7.4 Elevation és térhatás

Két külön dolog, és nem szabad összekeverni őket:

**(a) Elevation — lapok egymás fölött.** Négy szint. A geometria fix, az árnyék
**színe** témafüggő, mert sötét háttéren a fekete árnyék nem látszik:

```css
--arny-1:light-dark(rgba(16,48,58,.10),rgba(0,0,0,.55));
--arny-2:light-dark(rgba(16,48,58,.16),rgba(0,0,0,.72));
--e-1:0 1px 2px var(--arny-1);
--e-2:0 4px 10px -6px var(--arny-1),0 16px 32px -18px var(--arny-2);
--e-3:0 10px 22px -12px var(--arny-1),0 36px 66px -30px var(--arny-2);
```

| Szint | Hol |
|---|---|
| `--e-1` | tényadat-kártya, jelző, téma-kapcsoló, panel |
| `--e-2` | keresztmetszet-kártya, űrlap, gomb alapállapot |
| `--e-3` | gomb és kártya hover, kiemelt lap |
| `--e-lebego` | fenntartva modálisnak |

**(b) Térhatás — valódi 3D.** Ahol az elem tényleg elfordul a térben:

| Elem | Technika | Mértéke |
|---|---|---|
| A szelet | `perspective:1100px` + `preserve-3d`; rétegenként oldal- és tetőlap | alap `rotateX(9°) rotateY(26°)`, egérrel ±11° |
| Süteménykártya | `perspective:1000px`, a belső lap dől, a kép `translateZ(34px)` | max ±4,5° / ±3,5° |
| Gomb | `translateY` + `inset` alsó él (nyomódás) | −3 px hover, +1 px active |
| Kiválasztott réteg | `translateZ(34px)` — a néző felé csúszik | 34 px |

Szabály: **a 3D csak egérrel érhető el** (`hover:hover and pointer:fine`), és
`prefers-reduced-motion` alatt teljesen kikapcsol. Érintőn a kártya sík marad —
ott a döntés nem visszajelzés, csak akadozás.

Sugarak: `4 / 10 / 18 / 28 / 999 px`. A korábbi kis sugarakat a pasztell paletta
miatt növeltem: éles sarok + pasztell szín olcsó műanyag hatást ad.

### 7.5 Komponenslista

| Komponens | Állapotok | Megjegyzés |
|---|---|---|
| Gomb (fő / másod / csendes) | alap, hover, active, fókusz, letiltott | min. 50 px magas; 3D nyomódás + fénycsík; `aria-disabled` nem csak `opacity` |
| Nyitva/zárva jelző | nyitva (lüktető telt pont) / zárva (mozdulatlan üres karika) | **nem csak szín**: a pont formája és mozgása is különbözik |
| Téma-kapcsoló | 3 állapot, `aria-pressed` | világos / rendszer / sötét |
| **3D szelet** | alap, hintázás, kurzorkövetés, réteg kiemelve, csökkentett mozgás | a szignatúra; 6 anyagtextúra, rétegenként oldal- és tetőlap |
| Rétegvezérlő (lista) | alap, hover, kiválasztott, fókusz | 50 px, `aria-pressed`, 22 px színchip |
| **Térhatású kártya** | alap, hover (dőlés + fényfolt), fókusz-within | egérrel ±4,5°; érintőn sík |
| Süteményillusztráció | statikus | inline SVG, `role="img"` + `aria-label`; a valódi fotó foglalata előkészítve |
| Tényadat-kártya | alap, hover | −4 px emelkedés |
| „Út"-lap | alap, hover | −6 px; felső él cián→rózsa gradiens |
| Jelölő chip | allergén (borostyán) / mentes (cián) / semleges | szín + szöveg, sosem csak szín |
| Űrlapmező | alap, hover, fókusz (−1 px), hibás, letiltott | hiba: 2 px keret + halvány háttér + ikon + beúszó szöveg |
| Választócsoport | alap, kiválasztott, hover (−2 px), fókusz | `:has(input:checked)`, min. 56 px |
| Hibaösszegző | rejtett / látható | felskálázódik, fókuszt kap, ugróhivatkozásokkal |
| Sikerpanel | rejtett / látható | felskálázódik, fókuszt kap, összefoglalja a beküldött adatot |
| Nyitvatartás-táblázat | alap, „ma" kiemelve | egy adatforrásból generált |
| GYIK | zárt / nyitott | `<details name="gyik">` — natív, JS nélkül is működik |
| Háttérfolt | folyamatos sodródás | `aria-hidden`, 0,38 opacitás, reduced-motion alatt `display:none` |
| Mobil cselekvési sáv | — | fix, `safe-area-inset-bottom` |
| Placeholder-jelölés (`.ph`) | — | **terméktervezési eszköz**: szaggatott aláhúzás + borostyán szín; élesítéskor `grep`-elhető |

---

## 8. Animációk és mikrointerakciók

Az ügyfél animációkat kért. A rendszer alapszabálya ettől nem változik:
**minden animációnak vagy oksági viszonyt kell kifejeznie, vagy egy állapotot
kell láthatóvá tennie.** Ami egyiket sem teszi, az kimaradt (lásd a táblázat
utáni listát).

Globális tokenek: `--idom: 200ms` (mikrointerakció), `--idom-be: 420ms`
(belépés), `--idom-ki: 140ms` (kilépés — mindig gyorsabb),
`--gorbe: cubic-bezier(.2,.7,.3,1)`, `--rugo: cubic-bezier(.34,1.4,.5,1)`
(enyhe túllövés, csak megnyomható elemeken).

| # | Elem | Interakció | Mi történik | Időzítés / görbe | Miért |
|---|---|---|---|---|---|
| A1 | **A szelet** | egérmozgás a színtér fölött | a test követi a kurzort: `rotateY` 22±11°, `rotateX` 10∓7° | 420 ms `--gorbe` | A tárgyszerűség bizonyítása: ami elfordul, az test. |
| A2 | A szelet | üresjárat (nincs egér) | lassú hintázás 26° és 15° között | 11 s, végtelen | Jelzi, hogy interaktív, anélkül hogy odakiabálna. |
| A3 | Rétegsáv | hover / fókusz a listasoron | a réteg `translateZ(34px)`-szel a néző felé csúszik, a többi `saturate .5 / brightness .94` | 260 ms `--rugo` | Fizikai metafora: a réteget *kiveszik*. |
| A4 | Rétegsáv | kattintás / Enter | ugyanaz, rögzítve, `aria-pressed="true"` | 260 ms | Érintőn nincs hover. |
| A5 | **`prefers-reduced-motion`** | — | nincs kicsúszás, nincs hintázás, nincs kurzorkövetés; a kiválasztott réteg 3 px körvonalat kap | 0 ms | Az információ marad, a mozgás megy. |
| A6 | Süteménykártya | egérmozgás | a lap ±4,5°/±3,5°-ot dől, a kép `translateZ(34px)`-en marad, a fényfolt a kurzorhoz igazodik | 220 ms `--gorbe` | Térbeli visszajelzés arról, hogy a kártya egy tárgy, nem szövegdoboz. |
| A7 | Süteménykártya | hover | `--e-1` → `--e-3` | 220 ms | Emelkedés = megfogható. |
| A8 | Elsődleges gomb | hover | −3 px `translateY`, árnyék `--e-2` → `--e-3` | 200 ms `--rugo` | |
| A9 | Elsődleges gomb | hover | **fénycsík** fut át rajta balról jobbra | 620 ms `--gorbe` | Egyszeri, nem ismétlődő. A fő CTA-t emeli ki a többi közül. |
| A10 | Gomb | `:active` | +1 px `translateY`, árnyék `--e-1` | 200 ms | Lenyomódik. A belső alsó él (`inset`) adja a vastagságot. |
| A11 | Tényadat-kártya | hover | −4 px emelkedés | 200 ms `--rugo` | |
| A12 | „A műhely rendje" lap | hover | −6 px emelkedés, `--e-3` | 200 ms | |
| A13 | **Szekciók, kártyák, listaelemek** | görgetés (IntersectionObserver) | 26 px-ről felúszik + halványul be, testvérenként **70 ms lépcsőzéssel** (max 5 lépcső) | 420 ms `--gorbe` | Olvasási sorrendet ad. Csak egyszer fut (`unobserve`). |
| A14 | Háttérfoltok | folyamatos | két elmosott színfolt lassan sodródik | 26 s és 32 s | Az egyetlen tisztán dekoratív mozgás. `aria-hidden`, 0,38 opacitás, reduced-motion alatt `display:none`. |
| A15 | „Most nyitva" pont | folyamatos, csak nyitva állapotban | lüktetés | 2,4 s | **Állapotjelzés**: zárva a pont üres karika és nem mozog. A mozgás maga hordoz információt. |
| A16 | Navigációs link | hover | 2 px aláhúzás nő ki balról | 200 ms | |
| A17 | Téma-kapcsoló | hover | 1,08× skálázás | 200 ms `--rugo` | |
| A18 | Téma-kapcsoló | kattintás | az aktív pirula háttere átvált, és a `<meta name="theme-color">` is frissül | 200 ms | A böngésző UI-sávja együtt vált, különben villan. |
| A19 | Űrlapmező | fókusz | −1 px emelkedés + akcent keret | 200 ms | |
| A20 | Űrlapmező | `blur` (nem gépelés közben) | hibaszöveg **halványan beúszik** a mező alatt | 200 ms `be` | Gépelés közbeni validálás bünteti a felhasználót azért, mert még nem fejezte be. |
| A21 | Hibaösszegző / sikerpanel | küldés | 0,94-ről felskálázódik és fókuszt kap | 300–340 ms | A fókuszmozgatás animáció **után** történik, hogy a képernyőolvasó ne vágja el. |
| A22 | GYIK | nyitás | a nyíl 45° → 225° fordul, a válasz felúszik | 200 / 260 ms | A nyíl iránya az állapot, a fordulás a változás. |
| A23 | Választógomb (űrlap) | hover | −2 px emelkedés + árnyék | 200 ms `--rugo` | 56 px-es érintőcélpont, tapintható visszajelzéssel. |

### 8.1 Amit szándékosan nem animáltunk

| Nem csináltuk | Miért |
|---|---|
| Számláló-animáció az **5,0**-n | A pontszám tény, nem teljesítmény. A felfelé pörgő szám azt sugallja, hogy nő — nem nő, 16 értékelésből áll. |
| Fejléc-elrejtés görgetésre | Egy mozgó ragadós fejléc elveszi a figyelmet, és a magasságváltozása CLS-t okozhat. |
| Parallax a hero mögött | Mozgásérzékenyeknél rosszullétet okoz, és semmit nem közöl. |
| Betöltéskori teljes oldal-fade | Késlelteti a tartalmat azért, hogy a fejlesztő mutasson valamit. |
| Kártyadöntés **érintőn** | Nincs kurzor, amit követni lehetne; csak akadozás lenne belőle. A JS érintőn be sem köti. |
| Végtelen ismétlődő gombanimáció | Két kivétel van a végtelen mozgásra (A14 dekoratív, A15 állapotjelző); a CTA-n a mozgás egyszeri, hoverre. |

### 8.2 Mit garantál a `prefers-reduced-motion`

Egyetlen blokk kapcsolja ki az egészet: minden `animation` és `transition`
0,01 ms-ra megy, a háttérfoltok eltűnnek, a görgetésre megjelenő elemek
**azonnal láthatók** (a JS megfigyelő el sem indul), a kártyadöntés és a
kurzorkövetés be sem kötődik, a fénycsík eltűnik, és a kiválasztott réteg
**körvonalat kap a kicsúszás helyett**.

Ellenőrizve fejetlen Chromiumban `reduced_motion: reduce` alatt: a kiemelt
réteg `transform` értéke `none`, a `.folt` `display` értéke `none`, és nulla
elem marad rejtve.

### 8.3 Egy figyelmeztetés a görgetésre megjelenésről

A `.rejt` osztály **csak akkor rejt, ha fut a JS**: a fejlécbeli szkript teszi
ki a `data-js` jelzőt a `<html>`-re, és a CSS-szabály `:root[data-js] .rejt`
alakú. JS nélkül — kikapcsolt szkript, hiba a betöltésben, régi kliens — az
oldal teljes tartalma azonnal látszik. Ez nem apróság: a görgetés-animációk
leggyakoribb élesbeni hibája, hogy a tartalom véglegesen láthatatlan marad.

---

## 9. Frontend megvalósítás

### 9.1 Stack és indoklás

| Réteg | Választás | Indoklás |
|---|---|---|
| Kimenet | **statikus HTML** | Az oldal tartalma naponta legfeljebb egyszer változik (a napi kínálat). Nincs szükség futásidejű renderelésre. |
| Generálás | **Eleventy (11ty)** | Az étlap és a nyitvatartás egy-egy JSON/YAML adatfájl; a `/kinalat/` sorai és a `Menu` schema **ugyanabból** generálódik. Nincs kettős karbantartás. |
| CSS | **kézzel írt, egyetlen fájl, custom property alapon** | ~30 kB nyers, ~8 kB tömörítve. Egy Tailwind-build ennél a méretnél több eszközt hoz, mint értéket. |
| JS | **vanilla, egy fájl, modul nélkül** | 8,7 kB (komment nélkül) / **3,3 kB gzip**. Keretrendszer nélkül nincs hydration, nincs futásidejű költség. |
| Tartalomszerkesztés | **Decap CMS (git-alapú)** vagy egyszerű Google Sheet → build | Az ügyfél a napi kínálatot telefonról tudja frissíteni. A választás a §15/10-en múlik. |
| Hosting | **statikus, CDN-ről** (Netlify / Cloudflare Pages) | Ingyenes sávban elfér, HTTPS automatikus, a build git-push-ra fut. |
| Űrlapfeldolgozás | **szerver nélküli funkció** (lásd §9.5) | Nincs adatbázis, nincs karbantartandó backend. |

*Alternatíva, amit elvetettem:* WordPress. Egy hatoldalas, ritkán változó
oldalhoz havi frissítési kötelezettséget, plugin-felületet és 300–800 kB
alapterhet hozna. A „majd az ügyfél maga szerkeszti" ígéret ekkora oldalnál
a gyakorlatban nem valósul meg — helyette egy tényleg egyszerű, egymezős
napi-kínálat-szerkesztő a válasz.

### 9.2 Fontkezelés

**A prototípusban** a két betű **base64-gyel be van ágyazva** az
`index.html`-be. Ez tudatos döntés: a brief nulla külső függőséget kér, és
így a fájl offline, hálózat nélkül is a tervezett tipográfiával nyílik meg.
Ára: az `index.html` 145 kB, ebből 69 kB a két base64-blokk.

**Élesben ez nem így megy.** A helyes felállás:

```html
<link rel="preload" href="/f/fraunces.woff2"     as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/f/commissioner.woff2" as="font" type="font/woff2" crossorigin>
```
```css
@font-face{font-family:"Fraunces";src:url(/f/fraunces.woff2) format("woff2-variations");
           font-weight:300 900;font-display:swap;
           unicode-range:U+0000-00FF,U+0150,U+0151,U+0170,U+0171,U+2010-2026}
```

- **Önhosztolva**, nem a Google CDN-ről: a harmadik feles kapcsolat egy extra
  DNS + TLS kört jelent az LCP útján, és 2020 óta a böngészők cache-e amúgy sem
  megosztott a domainek között — a „majd már ott lesz a cache-ben" érv halott.
- **Subset**: latin + a magyar kiterjesztett karakterek. A leszállított
  subsetből ellenőrzötten nem hiányzik az `ő`, `Ő`, `ű`, `Ű`.
- **Tengelyrögzítés**: a Fraunces `SOFT`, `WONK` és `opsz` tengelye rögzítve
  (27,1 kB). Ha később kell az optikai méret adaptáció, a teljes `opsz`
  tengellyel 49,0 kB — a különbség 22 kB, és ezt csak akkor éri meg kifizetni,
  ha a display face 20 px alá is lemegy. Most nem megy (§7.2).
- `font-display: swap` + **metrikára illesztett fallback** (`size-adjust`,
  `ascent-override`), hogy a betűcsere ne okozzon elrendezés-ugrást.

### 9.3 Képek — mi van most az oldalon, és mi lesz

Az ügyfél „esztétikus képeket süteményekről" kért. Amit szállítani tudtam, és
amit nem:

**Amit NEM tudtam szállítani: fotót.** Két okból.

1. **Az ügyfélnek nincs fotóanyaga a birtokomban** (§15/2), és a Krém termékeiről
   egyetlen képet sem láttam.
2. **Jogtiszta fotóbank ebből a környezetből nem elérhető.** A hálózati
   egress-proxy blokkolja az Unsplash-t, a Pexelst, a Wikimedia Commonst és az
   Openverse-t (mind `connect_rejected`). Ismeretlen eredetű fotót pedig nem
   teszek egy ügyfél oldalára: a szerzői jogi kockázat az ügyfelet terheli,
   nem engem.

**Amit szállítottam: négy saját SVG-illusztráció.** Rétegszelet tányéron,
macaron-torony, gyümölcsös tartelette, egész torta tortaállványon. Kézzel írt
SVG, gradiensekkel, egységes fényiránnyal (bal felső), a kért palettában.

| Tétel | Méret |
|---|---|
| 4 illusztráció összesen | **11 537 B** nyers · **2 477 B** brotli/gzip után |
| Legnagyobb egyedi | 3 040 B |
| Hálózati kérés | **0** — mind inline |
| Dekódolás | **0 ms** — nincs raszter |
| CLS | **0** — `aspect-ratio: 5/4` a foglalaton |

Mindegyik `role="img"` + leíró `aria-label`, tehát képernyőolvasóval is
értelmezhető, és mindegyik **jelölve van**, hogy illusztráció, nem a Krém terméke
— a kártyák alatti figyelmeztetésben és a forrás kommentjeiben is.

**Amikor lesz fotó (§15/2), a csere elő van készítve.** Az `index.html`-ben a
kínálat fölött ott a `FOTÓHELY` komment a kész foglalattal:

```html
<picture>
  <source type="image/avif" srcset="/img/nev-400.avif 400w, /img/nev-800.avif 800w"
          sizes="(min-width:900px) 300px, 90vw">
  <source type="image/webp" srcset="/img/nev-400.webp 400w, /img/nev-800.webp 800w"
          sizes="(min-width:900px) 300px, 90vw">
  <img src="/img/nev-800.jpg" width="800" height="640" loading="lazy" decoding="async"
       alt="[a desszert leírása, nem kulcsszóhalmozás]">
</picture>
```

Szabályok a valódi fotókhoz:

| Szabály | Konkrétan |
|---|---|
| Formátum | AVIF `<source>`, WebP fallback, JPEG utolsó lépcsőben |
| Méretek | `srcset` 400 / 800 / 1200 px, `sizes` a tényleges rácsból |
| Helyfoglalás | `width`+`height` **vagy** `aspect-ratio` minden `<img>`-en — kötelező, CLS miatt |
| Vágás | 5:4, a desszert középre, felülről 30–45°-os szögből (ez illeszkedik a szelet nézetéhez) |
| Betöltés | a hajtás alattiak `loading="lazy" decoding="async"` |
| A hero | **továbbra sem kap fotót** — ott a 3D szelet áll (§3.7) |
| `alt` | leíró, nem kulcsszóhalmozó. Dekoratív képnél `alt=""` |

*Alternatíva, amit elvetettem:* generált („AI") fotórealisztikus képek. Egy
desszertműhelynél a fotó **bizonyíték**, nem illusztráció; egy nem létező sütemény
fotórealisztikus képe megtévesztő, és az első csalódott vendégnél visszaüt. Egy
nyilvánvalóan rajzolt illusztráció ezt a hazugságot nem követi el.

### 9.4 Cache

| Erőforrás | Fejléc |
|---|---|
| `/*.html` | `Cache-Control: public, max-age=0, must-revalidate` + `ETag` |
| `/f/*.woff2`, `/css/*.[hash].css`, `/js/*.[hash].js` | `public, max-age=31536000, immutable` (tartalom-hash a fájlnévben) |
| képek | `public, max-age=31536000, immutable` |
| Tömörítés | Brotli (fallback gzip) minden szöveges válaszra |
| Egyéb | `Content-Security-Policy` (self + `form-action`), `Referrer-Policy: strict-origin-when-cross-origin`, `X-Content-Type-Options: nosniff` |

### 9.5 Űrlap

**A prototípusban** az űrlap nem küld sehová: `preventDefault()`, majd
sikerpanel a beküldött adatok visszatükrözésével. Ez szándékos — nincs
backend, és nem akartam félrevezetni.

**Élesben** a javasolt felállás:

1. **Progresszív alap:** az űrlap `method="post"` `action="/api/elorendeles"`,
   és **JS nélkül is működik** (szerveroldali validáció + átirányítás egy
   `/koszonjuk/` oldalra). A JS csak inline validációt és aszinkron beküldést
   ad hozzá.
2. **Szerver nélküli funkció** (Netlify/Cloudflare Function): validál, majd
   (a) e-mailt küld a műhelynek, (b) **SMS-t** a `06 30 609 7009`-re, mert
   §1.3/J6 alapján ez a valóban olvasott csatorna, (c) visszaigazoló SMS-t
   a vendégnek, ha megadta. Az SMS-lépcső költsége tételenként pár forint —
   §15/6-ban árazandó.
3. **Spam:** rejtett `honeypot` mező + időbélyeg-ellenőrzés (3 másodpercnél
   gyorsabb kitöltés eldobva). **CAPTCHA nincs**: napi néhány beküldésnél
   a súrlódás többe kerül, mint a szemét.
4. **Adatkezelés:** a beküldött adat e-mailben/SMS-ben landol, tárolás nélkül.
   Ha tárolás kell (rendelésnyilvántartás), az már adatkezelési tájékoztatót és
   megőrzési időt igényel — §15/11.
5. **Validáció, ahogy a prototípusban is:** `blur`-re validál (nem gépelés
   közben), javításkor viszont azonnal; hiba a mező **alatt**, `role="alert"`;
   több hibánál összegző a lap tetején ugróhivatkozásokkal; a fókusz az első
   hibás mezőre. A dátum- és időmező **a nyitvatartás-objektumból** validál,
   nem beégetett számokból.

### 9.6 Egy adatforrás, négy felhasználás

A prototípus egyik szerkezeti döntése: a `NYITVATARTAS` objektum **egyetlen
helyen** van definiálva, és ebből származik

1. a fejléc élő nyitva/zárva jelzője,
2. a `/#hol` nyitvatartási táblázata,
3. az űrlap átvételi-idő és -dátum validációja,
4. a JSON-LD `openingHoursSpecification` blokkja.

Így a §15/1 megválaszolásakor **egy** helyen kell javítani, és nem lehet, hogy
az oldal mást mond, mint a strukturált adat.

### 9.7 A térhatás és az animációk megvalósítási költsége

| Réteg | Nyers | Tömörítve | Megjegyzés |
|---|---|---|---|
| Mozgás-CSS (kulcskockák, segédosztályok) | 1 508 B | ~0,4 kB | 8 kulcskocka |
| 3D szelet CSS | 5 151 B | ~1,2 kB | ebben az anyagtextúrák is |
| 3D szelet HTML | 954 B | — | |
| Illusztrációk | 11 537 B | 2 477 B | 4 db inline SVG |
| JS: 3D + kártyadöntés + görgetésfigyelő | ~3 400 B | ~1,0 kB | a teljes JS részeként |

**A JS így 11,1 kB kommentek nélkül, tömörítve 4,0 kB.** A brief eredetileg
5–10 kB JS-t kért: **a nyers méret 1,1 kB-tal túllépi a felső határt.** Ezt nem
szépítem — az animációk és a 3D ára. Két dolog tartja kezelhető szinten:
tömörítve 4,0 kB (a hálózaton ez számít), és nincs benne keretrendszer, tehát
nincs futásidejű költsége a méreten túl.

**Ha vissza kell szorítani 10 kB alá**, ebben a sorrendben venném ki:
(1) a kártyadöntés (~700 B) — ez a leggyengébb hozzáadott érték;
(2) a szelet kurzorkövetése (~600 B) — az üresjárati hintázás CSS-ből marad;
(3) a görgetésfigyelő (~900 B) — a `.rejt` osztály nélkül minden azonnal látszik.
Mindhárom kivehető anélkül, hogy bármi elromolna, mert mindegyik
progresszív ráépülés.

**Teljesítménybiztosítékok a 3D-hez:**

- `transform-style: preserve-3d` csak két helyen: a szelet és a kártya belső lapja.
- A kurzorkövető kezelők `getBoundingClientRect()`-et **egyszer** hívnak
  belépéskor, és a `resize` nullázza — nem minden egérmozgásnál (ez a leggyakoribb
  jank-forrás a döntött kártyáknál).
- Csak `transform` és `opacity` animálódik; `width`, `height`, `top`, `left` soha.
- `will-change` egyedül a háttérfoltokon, ahol tényleg folyamatos a mozgás.
- Érintőeszközön a 3D kurzorkövetés **be sem kötődik** (`pointer: coarse`).

---

## 10. SEO-specifikáció

### 10.1 Title és meta minta

| URL | `<title>` (≤60 kar.) | `<meta name="description">` (≤155 kar.) |
|---|---|---|
| `/` | `Krém Desszertműhely és Kávézó – Pécs, Zsuzsanna u. 2` | `Desszertműhely és kávézó Pécsett, a Zsuzsanna utca 2-ben. Nyitás 11:00. Desszert- és tortaelőrendelés online, telefonon vagy SMS-ben: 06 30 609 7009.` |
| `/kinalat/` | `Kínálat – desszertek és torták \| Krém, Pécs` | `Mi kapható ma a Krém pultjában: rétegenként leírt desszertek, allergénjelöléssel és árral. Pécs, Zsuzsanna u. 2.` |
| `/elorendeles/` | `Desszert- és tortaelőrendelés – Krém, Pécs` | `Rendelj desszertet vagy egész tortát konkrét napra a pécsi Krém Desszertműhelyből. Űrlap, telefon vagy SMS.` |
| `/a-muhely/` | `A műhely és a nyitvatartás – Krém, Pécs` | `Miért 11-kor nyitunk, hogyan találsz meg minket, és mikor vagyunk nyitva. Krém Desszertműhely és Kávézó, Pécs, Zsuzsanna u. 2.` |
| `/allergenek/` | `Allergéntáblázat – Krém Desszertműhely, Pécs` | `Melyik desszertünkben mi van: a 14 EU-allergén tételes táblázata, gluténmentes és laktózmentes jelöléssel.` |

A `title`-ökben a **város és az utca** benne van, mert a márkanév ütközik
(§K5) — a helymegjelölés az egyetlen egyértelmű megkülönböztető.

### 10.2 Heading-hierarchia (főoldal, a leszállított prototípusból)

```
H1  Krém Desszertműhely és Kávézó — Pécs, Zsuzsanna utca
├─ H2  Három út vezet ide, és nem egyforma sürgős mind a három
├─ H2  Minden tétel a saját keresztmetszetét hozza
│   ├─ H3  [csokoládés szeletes desszert]
│   ├─ H3  [pisztáciás desszert]
│   ├─ H3  [gyümölcsös desszert]
│   └─ H3  [egész torta, rendelésre]
├─ H2  Mondd meg, mikorra és mennyit
│   ├─ H3  A küldés nem ment el         (rejtett, hibaállapotban)
│   └─ H3  Megvan, elküldve             (rejtett, sikerállapotban)
├─ H2  Zsuzsanna utca 2., Pécs
│   └─ H3  Nyitvatartás
├─ H2  Tizenhat értékelés, mind ötcsillagos
│   └─ H3  Gyakori kérdések
└─ H2  Krém Desszertműhely és Kávézó    (lábléc)
    ├─ H3  Oldalak
    └─ H3  Kötelező
```

**Egy H1, nincs szintugrás.** A szekciócímkék („A MŰHELY RENDJE", „KÍNÁLAT")
szándékosan `<p class="cimke">` és nem heading: vizuális eligazítók, nem a
dokumentumstruktúra részei.

### 10.3 Strukturált adat — a teljes gráf

A prototípus egyetlen `@graph`-ot szállít, öt csomóponttal:

| Csomópont | `@id` | Mit visz |
|---|---|---|
| `WebSite` | `#website` | a webhely mint entitás, `publisher` → az üzlet |
| `CafeOrCoffeeShop` | `#uzlet` | név, leírás, `telephone`, `priceRange`, `PostalAddress`, `areaServed`, `ContactPoint`, `openingHoursSpecification`, `OrderAction` |
| `WebPage` | `#fooldal` | `isPartOf` → website, `about` → üzlet, `breadcrumb` |
| `BreadcrumbList` | `#morzsa` | egyelemű (főoldal); aloldalakon bővül |
| `FAQPage` | `#gyik` | 4 kérdés–válasz |

**Amit szándékosan NEM tettem bele, és miért — ez a szakasz fontosabb, mint
amit beletettem:**

| Kihagyva | Indoklás |
|---|---|
| **`aggregateRating`** | Az 5,0/16 a Google-nál él. A saját oldalon a **saját magunkról** közölt értékelés a Google szemében „self-serving review": a `LocalBusiness` review-gazdagítására **nem jogosult**, és a strukturált adatra vonatkozó irányelvek megsértése manuális intézkedést vonhat maga után. Ezért az érték **láthatóan ott van az oldalon**, forrásmegjelöléssel — csak nem markupolva. Ez nem óvatoskodás: a jelenlegi legerősebb eszközt (J1) nem érdemes egy kockázatos markupért kitenni. |
| **`geo`** | Nincs megerősített koordinátám. Kitalált szélesség/hosszúság rosszabb, mint a hiányzó: a térképes találatot rontja. §15/3. |
| **`image` / `logo`** | Nincs jogtiszta képanyag. §15/2. |
| **`hasMenu` / `Menu`** | Nincs dokumentált étlap. Amint van (§15/5), a `/kinalat/` oldalra kerül teljes `Menu` → `MenuSection` → `MenuItem` gráf, árakkal — ez tétel szinten indexelhető. |
| **`openingHoursSpecification`** | Ez **benne van**, de a `closes` értékek **placeholderek** (`18:00`), és az `index.html`-ben egy hangos HTML-komment figyelmeztet rá. **Ha a záróidő élesítésig nem erősíthető meg, ezt a tömböt ki kell venni.** Téves nyitvatartás a Google-ban mérhetően rosszabb, mint a hiányzó: elküldi az embereket zárt ajtóhoz, és az abból lett 1 csillagos értékelés az 5,0-t viszi el. |

A `FAQPage` markup marad, noha a FAQ-gazdagítás ma már gyakorlatilag csak
hatósági/egészségügyi oldalaknál jelenik meg. Ok: érvényes, nem árt, és a
kérdés–válasz szerkezet a nyelvi modellek és az asszisztensek számára jól
kinyerhető — ez a csatorna ma többet ér, mint a rich result.

### 10.4 Egyéb technikai SEO

- Egy `<link rel="canonical">` oldalanként, abszolút URL-lel.
- `hu-HU` `lang`, `og:locale`.
- `sitemap.xml` + `robots.txt` a build során generálva.
- **Nincs** `/index.html` és `/` duplikáció; záró perjeles alak a kanonikus.
- A `/#elorendeles` horgony és a `/elorendeles/` oldal **nem** duplikátum:
  a főoldali szekció rövidebb, az önálló oldal viszi a feltételeket.

### 10.5 Local SEO — a listing mint csatorna

Ez a rész hoz rövid távon a legtöbbet, és **függetlenül** attól, elkészül-e
a webhely.

| # | Teendő | Miért |
|---|---|---|
| L1 | **A cégprofil igénylése** (tulajdonosi hitelesítés) | A „Bejelentette 7 személy" (K2) addig marad, amíg nincs gazdája. Enélkül semmi más nem tartható karban. |
| L2 | Teljes nyitvatartás + ünnepnapi eltérések feltöltése | K3, és ez a leggyakoribb kérdés. |
| L3 | Kategória finomítása: elsődleges **Cukrászda / Desszertüzlet**, másodlagos Kávézó | Ma „Kávézó"-ként a „torta rendelés Pécs" lekérdezésekben nem jelenik meg. |
| L4 | 10–15 termékfotó + „Termékek" feltöltése árral | A profilon a fotó a legerősebb kattintásnövelő. |
| L5 | „Webhely" gomb a saját domainre, UTM-mel | Így mérhető lesz, mennyi forgalmat ad a listing. |
| L6 | Mind a 16 értékelésre válasz | Aktivitásjel a Google-nak, és a 17. vendégnek szóló üzenet. |
| L7 | NAP-konzisztencia: azonos név/cím/telefon a Cylex, etterem.hu, cukraszturul, Facebook adatlapokon | S2. Az eltérő adat gyengíti az entitás egyértelműségét. |
| L8 | Google Bejegyzés hetente egyszer: „ma a pultban" | Ingyenes, és pont azt a friss információt hozza, amiért a törzsvendég visszatér. |

---

## 11. Performance-célok

Referencia: **Moto G4-osztályú eszköz, lassú 4G (1,6 Mb/s, 150 ms RTT)** —
nem a fejlesztő gépe. A mérce a §2.4-ben rögzített: nem lehet lassabb a döntési
úton, mint a Google-listing, amit leváltunk.

| Metrika | Cél | Küszöb, ami fölött hiba | Mivel érjük el |
|---|---|---|---|
| **LCP** | **≤ 1,4 s** | 2,5 s | Nincs hero-fotó; az LCP-elem a `H1` szövege. Kritikus CSS inline, betűk preloaddal. |
| **FCP** | ≤ 1,0 s | 1,8 s | Egyetlen HTML-kérés, blokkoló külső CSS nélkül. |
| **CLS** | **≤ 0,02** | 0,1 | Minden réteg és illusztráció-foglalat fix arányú; metrikára illesztett fallback-betű; az üres hibamezők 0 magasak, de a DOM-ban vannak. A görgetésre megjelenés `opacity` + `transform` — **nem okoz elrendezés-ugrást**. |
| **INP** | **≤ 130 ms** | 200 ms | 4,0 kB tömörített JS, nincs keretrendszer, nincs hydration. A kurzorkövetők csak CSS-változót írnak. |
| **TBT** | ≤ 60 ms | 200 ms | Nincs harmadik feles szkript. |
| **Képkockaidő animáció közben** | ≤ 16 ms | — | Csak `transform`/`opacity` animálódik; a `getBoundingClientRect()` belépésenként egyszer fut. |

### 11.1 Bájtköltségvetés (élesített változat, brotli után)

| Erőforrás | Költségvetés | A prototípusban mért |
|---|---|---|
| HTML (fontok nélkül, illusztrációkkal együtt) | ≤ 28 kB | **26,3 kB** gzip ✓ |
| CSS (inline, kritikus) | ≤ 10 kB | **9,3 kB** gzip ✓ |
| JS | ≤ 5 kB | **4,0 kB** gzip ✓ (nyers 11,1 kB — lásd §9.7) |
| Betűk (2 × woff2) | ≤ 55 kB | **51,8 kB** ✓ |
| Fotó az első nézetben | **0 kB** | 0 ✓ (a szelet és az illusztrációk inline) |
| **Első betöltés összesen** | **≤ 95 kB** | **~87 kB** ✓ |
| Kérésszám az első nézethez | ≤ 3 | 3 (HTML + 2 betű) |

Az előző iterációhoz képest ez **+6 kB** (animációk, 3D, négy illusztráció).
Az `index.html` a prototípusban 167 kB, mert a betűk base64-gyel benne vannak
(§9.2); élesben ez szétválik, és a betűk egy évig cache-elődnek — a **második**
oldalletöltés így ~26 kB.

### 11.2 Harmadik felek

**Nulla.** Nincs Google Fonts, nincs analitika-tag, nincs süti-banner, nincs
térkép-iframe (a „Útvonal" egy sima link a Google Térképre — nem tölt be
600 kB-nyi beágyazott térképet). Ha analitika kell, Plausible vagy szerveroldali
naplóelemzés — a §15/12-ben eldöntendő.

---

## 12. CRO — konverziós elemek

**A mért konverzió: beküldött előrendelési kérés.** Másodlagos, egyenrangú:
`tel:` és `sms:` koppintás.

| # | Elem | Hol | Miért működik |
|---|---|---|---|
| C1 | **Élő nyitva/zárva jelző a fejlécben** | minden oldal | A legfőbb belépési súrlódást (a „vajon nyitva?" bizonytalanságot) az első 200 ms-ben feloldja. A Google-listing legjobb tulajdonságának átvétele (J3). |
| C2 | **Kiírt ársáv a hajtás fölött** | főoldal hero | Az árelhallgatás a legdrágább vendéglátós szokás: a bizonytalan ár kockázat, a kockázat halasztás. Az „1–2000 Ft" kimondása kiszűri a rossz illeszkedést és megnyugtatja a jót. Ez már ma is ott van a listingen (J4) — csak nem a saját felületünkön. |
| C3 | **5,0 · 16 értékelés, forrásmegjelöléssel** | hero + saját szekció | Társas bizonyíték. A forrás megnevezése („Google Cégprofil, lekérdezve …") **növeli** a hitelességet: az ellenőrizhető szám erősebb, mint a kerek szám. |
| C4 | **Fix alsó cselekvési sáv mobilon** | <900 px | A fő cél mindig hüvelykujjnyira van, függetlenül a görgetési pozíciótól. A listing gombsorának mintája (J2). |
| C5 | **Az SMS mint önálló, megnevezett út** | „A műhely rendje", „Hol" | Aki nem szeret telefonálni (és 25 alatt ez a többség), az ma nem rendel. Egy `sms:` link nulla fejlesztési költséggel nyit egy csatornát, ami **már működik**. |
| C6 | **Az űrlap melletti „miért kérdezzük" oszlop** | előrendelés | Minden mező indoklása csökkenti a kitöltés-elhagyást. A telefonszám kérése gyanús — amíg meg nem mondod, hogy oda megy a visszaigazolás. |
| C7 | **„Ez kérés, nem visszaigazolt rendelés" — kimondva, kétszer** | űrlap eleje + siker | Az elvárás előre kezelése megelőzi a legrosszabb kimenetet: az „azt hittem, megrendeltem" típusú csalódásból lesz az 1 csillag. |
| C8 | **A nyitvatartásból validáló dátum- és időmező** | űrlap | Nem enged olyan kérést, amit nem lehet teljesíteni. Minden ilyen kérés két telefonhívás és egy csalódás. |
| C9 | **Allergénjelek a kínálatsorokon** | kínálat | Egy egész vendégcsoportnak ez nem kényelmi funkció, hanem a belépés feltétele. Ma nincs sehol (K4). |
| C10 | **A keresztmetszet mint termékleírás** | hero + minden sor | Csökkenti a döntési kockázatot (§3.4), és fotó nélkül is megkülönböztethetővé teszi a tételeket. |
| C11 | **„Írj te is értékelést" gomb** | vélemények | §3.3: 16 elem törékeny. Az egyetlen olcsó védekezés a folyamatos utánpótlás. Ez nem konverzió a látogató felé, hanem konverzió a **következő** látogató felé. |
| C12 | **A 11:00 magyarázata** | „A műhely rendje" | Egy kifogást (`késői nyitás`) minőségi érvvé fordít (§3.5). |
| C13 | **GYIK** | főoldal alja | A négy kérdés a négy leggyakoribb telefonhívás. Minden megválaszolt kérdés egy fel nem vett telefon a gyártás közepén. |
| C14 | **A 3D szelet mint első interakció** | hero | Az első kattintás a legnehezebb. Egy alacsony tétű, játékos interakció (válassz réteget) belépteti a látogatót az oldal használatába — és közben pont a termékről tanít. |
| C15 | **Süteményillusztrációk** | kínálat | Fotó nélkül is megkülönbözteti a tételeket, és a listát végigpásztázhatóvá teszi. Ideiglenes megoldás: a valódi fotó erősebb lesz (§9.3). |

### 12.1 Mit mérünk

| Esemény | Hogyan |
|---|---|
| `elorendeles_bekuldve` | űrlap-siker, a „mit" értékkel dimenzióként |
| `telefon_koppintas` | `tel:` link kattintás |
| `sms_koppintas` | `sms:` link kattintás |
| `utvonal_koppintas` | Google Térkép link |
| `ertekeles_koppintas` | „Írj értékelést" |
| `szelet_hasznalat` | legalább egy réteg kiválasztva — ez méri, hogy a szignatúra elem *működik-e*, vagy csak dísz |

Az utolsó tétel önvizsgálat: ha három hónap alatt a látogatók kevesebb mint
10%-a nyúl hozzá, a keresztmetszet interaktív rétege felesleges, és statikus
illusztrációra kell egyszerűsíteni.

---

## 13. A fontos design-döntések, alternatívával együtt

A **⟳** jel azt jelöli, hogy a döntés a második iterációban megváltozott
(§0.0), és a mostani változat az ügyfél irányát követi.

| # | Döntés | Alternatíva | Miért nem az alternatíva |
|---|---|---|---|
| D1 | A redesign tárgya a hiányzó saját webhely, nem a listing | A Google-profil „átalakítása" | A listing layoutja nem birtokolt és nem szerkeszthető. Amit ott lehet, az adatpontosítás — az a §10.5. |
| D2 ⟳ | **Háromdimenziós szelet** mint szignatúra, valódi CSS 3D-vel | Lapos keresztmetszet-rajz (1. iteráció) / nagy termékfotó-hero | A fotó nincs és a tetőt mutatja. A lapos rajz *ábrázolja* a metszetet; a kiterjedt test **megmutatja, hogy van miből metszetet venni**. +1,9 kB CSS, nulla hálózati kérés. |
| D3 ⟳ | A paletta az ügyfél által megadott négy szín, kilenc tokenre bontva | Anyagnév-alapú paletta a műhely nyersanyagaiból (1. iteráció) | Az ügyfél kérése. Amit ezzel elveszítünk (a paletta már nem levezetés, hanem márkadöntés), a §3.6.1-ben kimondva. |
| D4 | **A pasztellek soha nem hordoznak szöveget** | Cián/rózsaszín szövegszínként | A kért négy szín közül kettő világos; szövegként egyik sem éri el a 4,5:1-et fehéren. Ezért van mély párjuk (`#046B7E`, `#C0396B`) az információhoz, és a pasztell csak felület. Enélkül a paletta olvashatatlan lenne. |
| D5 | Fraunces + Commissioner | Playfair + Inter | A brief tiltja, és jogosan: nem mond semmit a szakmáról. Lásd a §7.2 alternatívatáblázatát. |
| D6 | `light-dark()` a témákhoz | Teljes tokenkészlet duplikálva | 60 sor duplikáció, két helyen karbantartandó. Két kivétel maradt (többrétegű árnyék, folt-opacitás), mert a `light-dark()` csak színt vesz — kommentelve. |
| D7 | Sötét téma = **világosított**, nem invertált akcent | Színek matematikai invertálása | Az invertálás a ciánt narancsra vinné. A hígítás megtartja a felismerhetőséget. |
| D8 | Az oldal egy dolga: **előrendelés** | Asztalfoglalás / webshop | Foglalás: ismeretlen, van-e ülőhely (§15/7). Webshop: a fizetési integráció fenntartása többe kerül, mint a haszna. |
| D9 | Az SMS önálló, megnevezett csatorna | Csak telefonszám | A mobilszám (J6) miatt az SMS **ma is működik**; nulla fejlesztési költséggel nyit egy aszinkron utat. |
| D10 | Nincs `aggregateRating` markup | A 5,0 markupolása a rich resultért | Saját oldalon a saját értékelés „self-serving": nem jogosult, és manuális intézkedést kockáztat. |
| D11 | Statikus HTML + 11ty | WordPress | Hatoldalas, ritkán változó oldalhoz plugin-karbantartás és 300–800 kB alapteher. |
| D12 | Placeholderek **láthatóan jelölve** (`.ph`) | Kitalált mintaszöveg | Kitalált ár/nyitvatartás élesben átcsúszhat. A szaggatott aláhúzás egyszerre olvasható a designban és `grep`-elhető a kódban. |
| D13 ⟳ | **Görgetésre megjelenés, lépcsőzve** | Nincs görgetés-animáció (1. iteráció) | Az ügyfél kérése. Két biztosíték: a `.rejt` csak `data-js` mellett rejt (JS nélkül minden látszik), és `prefers-reduced-motion` alatt a megfigyelő el sem indul. |
| D14 | Egyetlen `NYITVATARTAS` adatforrás négy felhasználással | Külön beírt óraértékek | A négy hely előbb-utóbb szétcsúszik, és a schema mást mond, mint az oldal. |
| D15 | Nincs süti-banner | Analitika sütivel | Süti nélküli mérés elegendő, és a banner az első interakció elrablása. |
| D16 | A hero nem sorszámoz („01/02/03") | Számozott „hogyan működik" lépéssor | A három út **párhuzamos**, nem sorrend. |
| D17 ⟳ | **Saját SVG-illusztrációk** fotó helyett | Stock fotó / generált fotórealisztikus kép | Fotóbank a hálózaton nem elérhető, ismeretlen eredetű fotó jogi kockázat. Egy nem létező sütemény fotórealisztikus képe pedig megtévesztő — egy nyilvánvalóan rajzolt illusztráció nem hazudik. |
| D18 | A 3D **csak egérrel**, `prefers-reduced-motion` alatt sehogy | Mindenhol bekapcsolva | Érintőn nincs kurzor, amit követni — csak akadozás lenne belőle. Mozgásérzékenyeknél a folyamatos térbeli mozgás rosszullétet okoz. |
| D19 | A lüktető „nyitva" pont az egyetlen végtelen **állapotjelző** mozgás | Statikus pont / mindenhol lüktetés | Itt a mozgás maga az információ: zárva a pont üres karika és mozdulatlan. Máshol a végtelen mozgás zaj. |
| D20 | Nincs számláló-animáció az 5,0-n | Felfelé pörgő pontszám | A felfelé pörgő szám növekedést sugall. Nem nő: 16 értékelésből áll. |

## 14. Bevezetési ütemterv

| Fázis | Mi történik | Idő | Feltétele | Mérhető eredmény |
|---|---|---|---|---|
| **0. Azonnal, webhely nélkül** | §10.5 L1–L4: cégprofil igénylése, teljes nyitvatartás, kategória, 10–15 termékfotó, válasz mind a 16 értékelésre | 1 hét, fejlesztés nélkül | csak ügyfél-idő | profilmegtekintés, útvonalkérés növekedése |
| **1. Alap** | Domain + hosting; `/` és `/a-muhely/`; `LocalBusiness` gráf; NAP-konzisztencia (L7) | 2 hét | §15/1, /2, /3, /13 | indexelt oldalak; márkanév-keresésre saját találat |
| **2. Konverzió** | `/elorendeles/` + szerver nélküli űrlap (§9.5) + SMS-értesítés; L5 (UTM) | 1,5 hét | §15/4, /6, /11 | első beküldött kérések; `tel:`/`sms:` koppintások |
| **3. Tartalom** | `/kinalat/` az étlapadatokból; `Menu` gráf; mini keresztmetszetek tételenként | 2 hét | **§15/5 (étlap + árak)** | nem-márkás keresésekből érkező forgalom |
| **4. Bizalom és jog** | `/allergenek/`; adatkezelési tájékoztató; impresszum; L8 (heti Bejegyzés) | 1 hét | §15/11, /14 | „gluténmentes/laktózmentes …" lekérdezésekre megjelenés |
| **5. Mérés és nyesés** | Analitika bekötése; a §12.1 események; **a keresztmetszet használatának kiértékelése** | folyamatos, 3 hónap múlva döntés | — | konverziós arány; döntés a szignatúra elem sorsáról |
| **6. Opcionális** | `/velemenyek/` (ha 40+ értékelés); `/tortak/` (ha önálló szolgáltatás); angol verzió (ha §15/9 igen) | — | küszöbfeltételek | — |

**A kritikus út:** a 3. fázis a legértékesebb (ez hozza a nem-márkás
forgalmat), de teljesen az ügyfél adatszolgáltatásán múlik (§15/5). Ha az étlap
nem érkezik meg, az 1–2. fázis önmagában is szállítható és működőképes.

---

## 15. Nyitott kérdések — ehhez ügyfél-input kell

Sorrendben aszerint, hogy mi blokkolja az élesítést. Az 1–3. **blokkoló**.

| # | Kérdés | Miért blokkoló / mit érint |
|---|---|---|
| **1** | **Pontos heti nyitvatartás: minden nap záróidő, és van-e zárva tartó nap? Ünnepnapi eltérések?** | **Blokkoló.** Négy dolgot hajt (§9.6): fejlécjelző, táblázat, űrlap-validáció, `openingHoursSpecification`. A prototípusban 11:00–18:00 **kitalált** placeholder. Ha nem erősíthető meg, a schema-blokkot ki kell venni (§10.3). |
| **2** | **Van jogtiszta fotóanyag? Ki készítette, felhasználható-e?** | **Blokkoló** a Local SEO L4-hez és az `image` schemához. Az oldal fotó nélkül is teljes (§3.7), de a Google-profilon a fotó a legerősebb eszköz. |
| **3** | **Van saját domain? Ha igen, melyik? (A prototípus `kremdesszert.hu`-t használ placeholderként.)** | **Blokkoló.** Ez határozza meg a canonical URL-t, az `@id`-ket és a listing „Webhely" gombját. |
| 4 | Van egész torta rendelésre? Milyen méretek, hány szeletes, mennyibe kerül, **hány nappal előbb** kell leadni, van-e minimális mennyiség? | Az űrlap `ELOJEGYZES_NAP` értéke (most: 2, kitalált), a választógombok, és a `/tortak/` aloldal léte. |
| **5** | **Teljes étlap: tételek, összetevők, árak, és melyik tétel milyen rétegekből áll.** | A 3. fázis egésze. Ez a legnagyobb értékű hiányzó adat: enélkül a `/kinalat/` nem születik meg, és a nem-márkás keresésekből nem jön forgalom. |
| 6 | Melyik e-mail-cím kapja a beküldött kéréseket? Kérünk-e SMS-értesítést is (tételenként pár forint)? | §9.5/2. |
| 7 | Van ülőhely, hány fő? Terasz? Ez ott fogyasztható hely, vagy inkább elviteli pult? | A pozicionálás és a „kávézó" vagy „desszertüzlet" elsődleges kategória (§10.5 L3). |
| **8** | **Átvehetjük-e a Google-értékelések szövegét kiemelt idézetként? (A szerzők nevével — jogilag és etikailag ehhez az ügyfél döntése kell.)** | A „Vélemények" szekció jelenleg placeholder. |
| 9 | Jelentős a külföldi/turista vendég? | Angol nyelvi verzió (§4.1). |
| 10 | Ki fogja frissíteni a napi kínálatot, és milyen eszközzel érzi jól magát? (telefon, Google Sheet, admin felület) | A CMS választása (§9.1). |
| 11 | Tárolni akarjuk-e a beküldött rendeléseket, vagy elég az e-mail/SMS? | Adatkezelési tájékoztató tartalma és megőrzési idő (§9.5/4). |
| 12 | Kell-e analitika? Elég a süti nélküli? | §11.2, D15. |
| 13 | **Igényelve van-e a Google Cégprofil?** Ha nem: van hozzáférés a hitelesítéshez? | §10.5 L1 — ez a legolcsóbb és leggyorsabb javítás az egész anyagban. |
| 14 | Cégadatok az impresszumhoz: cégnév, székhely, adószám, nyilvántartási szám. | Jogi kötelezettség. |
| 15 | Mi a tulajdonos/készítő neve, és vállalja-e, hogy megjelenik az oldalon? | Kisvállalkozásnál a névvel vállalt felelősség erős bizalmi elem (`/a-muhely/`). |
| 16 | Van-e gluténmentes / laktózmentes / cukormentes kínálat, és van-e külön munkafelület (keresztszennyeződés)? | `/allergenek/` tartalma és a K4 feloldása. |
| 17 | A „Bejelentette 7 személy" tényleg azt jelenti, hogy a profil nincs tulajdonosi kezelésben? (Ez a K2 alapja, és **közepes** bizonyosságú következtetés.) | Ha téves, a K2 és az L1 tárgytalan. |

---

## 16. A leszállított prototípus — mért adatok

| Tétel | Érték |
|---|---|
| `index.html` | 167 282 B (ebből 69 128 B a két base64 betű) |
| HTML betűk nélkül | 98 160 B · **26 250 B gzip** |
| CSS | 35 663 B · **9 340 B gzip** |
| JS (2 blokk: téma-bootstrap + fő) | nyers 14 182 B · komment nélkül **11 138 B** · **4 046 B gzip** |
| — ebből 3D + animáció + görgetésfigyelő | ~3 400 B |
| JSON-LD | 3 885 B |
| 3D szelet (HTML + CSS) | 954 + 5 151 B |
| Mozgás-CSS (kulcskockák, segédosztályok) | 1 508 B |
| Süteményillusztrációk (4 db inline SVG) | 11 537 B · **2 477 B gzip** |
| Külső kérés | **0** |
| Raszteres kép | **0** |

**Ellenőrzött viselkedés** (fejetlen Chromium, 320 / 390 / 768 / 1440 px,
világos és sötét, `prefers-reduced-motion: reduce`):

- vízszintes görgetés: **nincs**, egyik szélességen sem (320-tól 1440-ig mérve);
- külső hálózati kérés: **nincs** — a betűk és az illusztrációk inline;
- címke nélküli űrlapmező: **0**; hozzáférhető név nélküli gomb/link: **0**;
  `aria-label` nélküli `role="img"` SVG: **0**;
- pontosan **egy** `H1`, szintugrás nélkül;
- első `Tab`: „Ugrás a tartalomra";
- a betűk ténylegesen betöltődnek, az `ő`/`ű` rajzolt glifa, nem helyettesítés;
- **görgetés után nulla elem marad rejtve** minden mért szélességen;
- **csökkentett mozgásnál**: nulla rejtett elem (a megfigyelő el sem indul),
  a háttérfoltok `display:none`, a kiemelt réteg `transform: none`;
- 3D kurzorkövetés egérrel mérve: a szelet `--ry` 28,6°-ra állt, a kártya
  `--ry` 3,15°-ra — a `matrix3d` ténylegesen alkalmazódik;
- konzolhiba: **nincs**;
- űrlap-validáció végigmérve: üres küldés → **7 hiba + összegző**; 09:00-s
  átvétel → „Aznap 11:00 és 18:00 között vagyunk nyitva"; helyes kitöltés →
  sikerpanel és a gomb letiltása („Elküldve").

---

## 17. Őszintén: mi ennek az anyagnak a leggyengébb pontja

**Az, hogy az ügyfélről hat adatot tudok, és arra épül egy teljes oldal.**
A második iteráció ezen nem javított — sőt, két ponton rontott.

1. **A központi stratégiai döntés — hogy az oldal EGY dolga az előrendelés —
   hipotézis, nem tudás.** Levezettem az 1–2000 Ft-os ársávból, a mobilszámból
   és a „desszertműhely" szóból, de nem beszéltem az ügyféllel. Ha a bevétel
   túlnyomó része a betérő kávézó vendég, a §5 oldalfelépítése és a §12 CRO-tábla
   fele újraírandó. **Ez maradt a legnagyobb egyedi kockázat.**

2. **A paletta már nem érv, hanem ízlés.** Az első iterációban minden színt meg
   tudtam indokolni egy nyersanyaggal. Most a válasz az, hogy az ügyfél így
   kérte. Ez legitim, de ha jövőre valaki megkérdezi, miért cián egy pécsi
   desszertműhely oldala, erre a dokumentumra mutatva nem lesz jobb válasz.
   **Ez a mostani iteráció legnagyobb vesztesége.**

3. **A képek nem fotók, és nem az ügyfél termékei.** Az illusztrációk jók
   arra, hogy a felület ne legyen üres, és arra, hogy megmutassák a
   rétegszerkezetet — de egy desszertnél a **fotó a bizonyíték**. Amíg nincs
   valódi fotóanyag, az oldal a saját termékéről semmit nem mutat. A csere
   elő van készítve (§9.3), de amíg nem történik meg, ez hiány.

4. **A kínálat teljes egészében placeholder.** A négy tétel neve, összetétele
   és ára kitalálatlan; a `/kinalat/` — a legértékesebb oldal — csak sablonként
   létezik.

5. **A JS túllépte a kért méretet.** 11,1 kB nyers a kért 5–10 kB helyett
   (tömörítve 4,0 kB). Ez az animációk és a 3D ára. §9.7-ben megírtam, mit
   venném ki és milyen sorrendben, ha vissza kell szorítani — de most fölötte van.

6. **A 3D és az animációk elsősorban egérrel élnek.** Érintőn a kártyadöntés és
   a kurzorkövetés nem fut, tehát a látogatók többsége (mobil) a térhatásból
   csak a statikus perspektívát és az árnyékokat látja. Ez így helyes döntés,
   de azt jelenti, hogy **amit az ügyfél kért, azt a felhasználók kisebbik
   része tapasztalja meg teljesen.**

7. **A „Bejelentette 7 személy" értelmezése következtetés** (§15/17). Erre
   építettem a K2-t és az egész §10.5 sürgősségét. Közepes bizonyosságú.

8. **Az öt tervezett oldalból egy készült el.** A `/kinalat/`, `/elorendeles/`,
   `/a-muhely/` és `/allergenek/` szekciótáblaként létezik, kódként nem.

9. **Nem beszéltem egyetlen vendéggel sem.** A célközönség-leírás (§0.1) irodai
   következtetés. Öt beszélgetés a pult mellett többet érne, mint ez az egész
   dokumentum §12-es fejezete.

Amit ezzel szemben **nem** tartok gyengének: a design system számai mérve
vannak, nem becsülve; a prototípus akadálymentességét gépi ellenőrzéssel
átnéztem világos és sötét témán, csökkentett mozgással is; az animációk
egyike sem tud tartalmat véglegesen elrejteni; és sehol nincs kitalált ár,
nyitvatartás vagy kapacitás — ami nem tudott, az jelölve van.
