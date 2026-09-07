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
> akkor lát az ember, amikor a műhely már elvégezte a munkát — ezért a paletta
> nem absztrakt márkaszínekből, hanem a rétegek anyagaiból (tejszín, piskóta,
> égetett cukor, kakaó, meggy, pisztácia) áll, a szerkezet pedig a műhely
> szóhasználatát követi: rétegek, sorrend, arány.**

Amit ez konkrétan kizár: nincs „elegáns cukrászda" aranyszín; nincs pasztell
rózsaszín, mert az a torta-marketing alapértelmezése; nincs fotótapéta-hero,
mert nincs jogtiszta fotó, és mert a fotó úgyis csak a tetejét mutatja.

Amit előír: minden szín megnevezhető egy **anyaggal**, amit a műhelyben
használnak. Ha egy szín nem nevezhető meg így, nem kerül a rendszerbe.

---

## 3.7 A szignatúra elem — „A keresztmetszet"

### Mi ez

Egy desszert **vágott felülete**: egymásra rakott vízszintes rétegsávok,
mindegyik a saját anyagtextúrájával (a piskóta morzsás, a mousse sima szemcsés,
a glazúr fényes és túlcsordul az oldalán, a ropogós alap rácsos). Mellette a
rétegek listája: minden réteg neve és **funkciója** — nem az összetevője, hanem
hogy mit **csinál** („tartás — enélkül összeesik", „savas ellenpont a
mousse-nak"). Egy réteget kiválasztva az kicsúszik a szeletből, a többi
visszahalványul.

### Miért pont ez

1. **Megmutatja, nem elmondja.** A „műhely" szó azt állítja, hogy itt kézzel
   épített, összetett dolgok készülnek. Ezt egy fotó nem tudja bizonyítani —
   a fotó a tetőt mutatja. A keresztmetszet a *munkát* mutatja: hét réteg, hét
   döntés.
2. **A hiányzó információt adja meg.** §3.4: a döntés kockázata a belső
   szerkezet nem ismerete. A keresztmetszet pont ezt oldja fel, és mellékesen
   megoldja az allergéninformáció megjelenítését is (K4): a rétegsorban látszik,
   hol van tej, tojás, dióféle.
3. **Rendszer, nem trükk.** Ugyanez a rajz jelenik meg 34 px széles
   miniatűrként a kínálatlista minden során. Így fotó nélkül is minden tételnek
   **saját vizuális identitása** van, és a lista végigpásztázható.
4. **Nem fotón múlik.** Az ügyfélnek ma nincs fotóanyaga. Ez a megoldás
   *fotófüggetlen*, és akkor is működik, ha soha nem lesz fotós.
5. **A paletta belőle jön.** A rétegszínek és a felület-/szövegszínek ugyanabból
   a hét anyagból származnak — a szignatúra elem és a design system nem két
   dolog.

### Mibe kerül LCP-ben

Megmértem a leszállított prototípuson:

| Tétel | Méret |
|---|---|
| A keresztmetszet HTML-je | **3 946 B** |
| A hozzá tartozó CSS | **4 973 B** |
| Hálózati kérés | **0** |
| Képdekódolás | **0 ms** |
| Elrendezés-ugrás (CLS) | **0** — minden sáv fix `--h` magasságú |

**LCP-hatás: gyakorlatilag nulla, és negatív egy fotós alternatívához képest.**
Egy 1200 px széles, jól optimalizált AVIF hero 60–110 kB, plusz egy külön
hálózati kérés, plusz dekódolás — az lenne az LCP-elem. Így a legnagyobb
festett elem a `H1` szövege vagy a keresztmetszet DOM-ja, tehát
**LCP ≈ FCP**, és a font érkezésén kívül semmi nem tolja.

### Fegyelem máshol

Ez az egy hely a merész. Minden más csendes: hajszálvékony elválasztók,
matt felületek, 3–12 px sugarak, semmi üvegeffekt, semmi gradiens a szöveg
mögött, semmi nagybetűs „01/02/03". A sorszámozás csak ott jelenik meg, ahol
valódi sorrend van — a rétegek listája alulról fölfelé építési sorrend, de ott
sem számot használunk, hanem a rétegek vizuális egymásra következését.

---

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
| 1 | Fejléc | Logó, nav, **élő nyitva/zárva jelző**, téma-kapcsoló | Orientáció + a leggyakoribb kérdés azonnali megválaszolása | A jelző ugyanabból az objektumból számol, mint az űrlap-validáció |
| 2 | Hero | H1, egy bekezdés, két CTA, **4 tényadat** (5,0 / ársáv / nyitás / cím) | A „hova kerültem és megéri-e" 5 másodperc alatt | Nincs kép. A tények forrásmegjelöléssel |
| 3 | **Keresztmetszet** | A szignatúra elem, 7 réteggel | Megmutatni, mit jelent a „műhely" | §3.7 |
| 4 | A műhely rendje | Három út: bejössz / hívsz-írsz / előre kéred | A csatornák egyenrangúsítása, az U1 feloldása | Nem sorszámozott lépéssor: három **párhuzamos** út |
| 5 | Kínálat | 4 tétel mini keresztmetszettel, allergénjelekkel, árral | A döntés bemenete (U2, K4) | Prototípusban mintaadat |
| 6 | **Előrendelés** | Akadálymentes űrlap + magyarázó oszlop | A fő konverzió | Bal oldalt: miért kérjük az adatot |
| 7 | Hol és mikor | Cím, hívás, SMS, útvonal, heti nyitvatartás | NAP-konzisztencia + a K3 feloldása | A táblázat generált, egy forrásból |
| 8 | Vélemények | 5,0 · 16, forrással; „Írj értékelést" | A J1 konvertálása és hígítása (§3.3) | Nincs `aggregateRating` markup (§10.3) |
| 9 | GYIK | 4 kérdés | A telefonhívások egy részének kiváltása | `FAQPage` markup |
| 10 | Lábléc | NAP, oldalak, kötelező linkek | Jogi + bejárhatóság | |
| M | Mobil cselekvési sáv | Előrendelés + Hívás, fix | A J2 mintájának átvétele | Csak <900 px |

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

### 6.1 Főoldal — desktop (≥1100 px, tartalomsáv 1160 px)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ [Ugrás a tartalomra]  ← csak fókusszal látható, a bal felső sarokban          │
├──────────────────────────────────────────────────────────────────────────────┤
│ Krém  desszertműhely & kávézó   Kínálat Előrendelés A műhely Hol             │
│                                    ( ● Most nyitva · 18:00-ig )  [☀][▭][☾]   │  ← ragadós, 64 px
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Krém Desszertműhely és Kávézó —      ┌───────────────────────────────────┐  │
│  Pécs, Zsuzsanna utca                 │ [a nap desszertje]        (MINTA) │  │
│  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ H1 (Fraunces) │                                   │  │
│                                       │ ┌────────┐  ■ Tükörglazúr         │  │
│  Tizenhat Google-értékelés, egy sem   │ │▓▓▓▓▓▓▓▓│    lezár, és eltakarja │  │
│  kevesebb ötnél. Tizenegykor          │ │████████│  ■ Gyümölcszselé       │  │
│  nyitunk. Egy kávé és egy desszert    │ │▒▒▒▒▒▒▒▒│    savas ellenpont     │  │
│  személyenként 2000 Ft alatt kijön.   │ │░░░░░░░░│  ■ Csokoládémousse     │  │
│                                       │ │▓▓▓▓▓▓▓▓│    a tömeg             │  │
│  ┌───────────────────┐ ┌────────────┐ │ │▚▚▚▚▚▚▚▚│  ■ …                   │  │
│  │Desszertet rendelnék│ │06 30 609 …│ │ └────────┘  (7 réteg)             │  │
│  └───────────────────┘ └────────────┘ │  ▔▔▔▔▔▔▔▔▔ SZIGNATÚRA             │  │
│  ─────────────────────────────────    │ Ez a rajz mutatja meg, mit jelent │  │
│  ÉRTÉKELÉS  ÁRSÁV     NYITÁS   CÍM    │ a „műhely" szó…                   │  │
│  5,0        1–2000 Ft 11:00  Zsuzs. 2 └───────────────────────────────────┘  │
│  16 érték.  /fő       zárás?  7632                                           │
├──────────────────────────────────────────────────────────────────────────────┤
│  A MŰHELY RENDJE ────────────────────────────────────────────────────────    │
│  Három út vezet ide, és nem egyforma sürgős mind a három                      │
│                                                                              │
│  ─────────────────      ─────────────────      ─────────────────             │
│  11:00-tól              Bármikor               Előre                          │
│  Bejössz                Hívsz vagy írsz        Kitöltöd az űrlapot            │
│  Zsuzsanna u. 2…        06 30 609 7009, SMS…   Konkrét napra…                 │
├──────────────────────────────────────────────────────────────────────────────┤
│  KÍNÁLAT ────────────────────────────────────────────────────────────────    │
│  Minden tétel a saját keresztmetszetét hozza                                  │
│  ──────────────────────────────────────────────────────────────────────      │
│  ▤  [csokoládés szeletes desszert]                                    [ár]   │
│     Hat réteg: glazúr, zselé, mousse, krém, piskóta, ropogós alap             │
│     (tojás)(tej)(glutén)(diófélék)                                            │
│  ──────────────────────────────────────────────────────────────────────      │
│  ▤  [pisztáciás desszert]                                             [ár]   │
│  … (4 sor)                                                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│  ELŐRENDELÉS  (eltérő felület-tónus, teljes szélességű sáv)                   │
│                                                                              │
│  Mondd meg, mikorra és      ┌─ Mit szeretnél? * ──────────────────────────┐  │
│  mennyit                    │ (o)Szeletes  (o)Egész torta  (o)Válogatás   │  │
│                             │ (o)Egyéb                                     │  │
│  Ez egy kérés, nem          ├─ Hány adag? * ───────────────────────────────┤  │
│  visszaigazolt rendelés…    │ [                                          ] │  │
│                             ├─ Mikorra kell? * ────────────────────────────┤  │
│  – Miért van benne az       │ [ 2026-09-20                             📅] │  │
│    átvétel órája?           ├─ Átvétel körülbelül * ───────────────────────┤  │
│  – Miért kérünk telefont?   │ [ 14:30                                  🕐] │  │
│  – Miért van allergia-mező? │ … allergia / név* / telefon* / e-mail        │  │
│                             │ [x] Tudomásul veszem… *                      │  │
│                             │ ┌──────────────────┐                         │  │
│                             │ │ Kérés elküldése  │                         │  │
│                             │ └──────────────────┘                         │  │
│                             └──────────────────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────────┤
│  HOL ÉS MIKOR ───────────────────────────────────────────────────────────    │
│  Zsuzsanna utca 2., Pécs                                                      │
│  Krém Desszertműhely és Kávézó   │  Nyitvatartás                              │
│  Zsuzsanna u. 2., 7632 Pécs      │  Hétfő      11:00 – 18:00   ← MA kiemelve  │
│  → Hívás  → SMS  → Útvonal       │  Kedd       11:00 – 18:00                  │
├──────────────────────────────────────────────────────────────────────────────┤
│  AMIT MÁSOK MONDANAK ────────────────────────────────────────────────────    │
│  Tizenhat értékelés, mind ötcsillagos                                         │
│  5,0  16 értékelés   ★★★★★     │  [3 kiemelt vélemény helye]                 │
│  Forrás: Google Cégprofil…      │                                            │
│  [Írj te is értékelést]         │                                            │
│                                                                              │
│  Gyakori kérdések                                                             │
│  ▸ Mikor van nyitva?              ▸ Lehet előre rendelni?                     │
├──────────────────────────────────────────────────────────────────────────────┤
│  LÁBLÉC   NAP-adatok │ Oldalak │ Kötelező (adatkezelés, impresszum, allergén) │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Főoldal — mobil (375–430 px)

```
┌───────────────────────────────┐
│ Krém              [☀][▭][☾]   │ ← ragadós; a nav és az állapotjelző elrejtve
├───────────────────────────────┤
│ Krém                          │
│ Desszertműhely                │
│ és Kávézó —                   │
│ Pécs,                         │  ← H1 36 px, az accent rész színnel
│ Zsuzsanna utca                │
│                               │
│ Tizenhat Google-értékelés,    │
│ egy sem kevesebb ötnél…       │
│                               │
│ ÉRTÉKELÉS      ÁRSÁV          │  ← a tények 2 oszlopban
│ 5,0            1–2000 Ft      │
│ NYITÁS         CÍM            │
│ 11:00          Zsuzsanna u. 2 │
├───────────────────────────────┤
│ ┌───────────────────────────┐ │
│ │[a nap desszertje] (MINTA) │ │
│ │ ┌───────────┐             │ │  ← a tömb max 240 px széles,
│ │ │▓▓▓▓▓▓▓▓▓▓▓│             │ │    hogy szeletnek látsszon
│ │ │███████████│             │ │
│ │ │▒▒▒▒▒▒▒▒▒▒▒│             │ │
│ │ └───────────┘             │ │
│ │ ■ Tükörglazúr             │ │  ← a rétegek listája ALÁ kerül,
│ │   lezár, és eltakarja…    │ │    minden sor 48 px magas gomb
│ │ ■ Gyümölcszselé           │ │
│ │ … (7 sor)                 │ │
│ │ Ez a rajz mutatja meg…    │ │
│ └───────────────────────────┘ │
├───────────────────────────────┤
│ A MŰHELY RENDJE ──────────    │
│ Három út vezet ide…           │
│ │ 11:00-tól                   │  ← egymás alatt, bal oldali
│ │ Bejössz                     │    függőleges vonallal
│ │ Zsuzsanna u. 2…             │
│ │ Bármikor                    │
│ │ Hívsz vagy írsz             │
│ │ Előre                       │
├───────────────────────────────┤
│ KÍNÁLAT ──────────────────    │
│ ▤ [csokoládés desszert] [ár]  │  ← 34 px mini + szöveg + ár
│   Hat réteg: glazúr…          │
│   (tojás)(tej)(glutén)        │
│ ───────────────────────────   │
├───────────────────────────────┤
│ ELŐRENDELÉS                   │
│ Mondd meg, mikorra…           │
│ Mit szeretnél? *              │
│ ┌───────────┐ ┌─────────────┐ │  ← 2 oszlopos választórács,
│ │(o)Szeletes│ │(o)Egész torta│ │    minden cél ≥52 px
│ └───────────┘ └─────────────┘ │
│ Hány adag? *                  │
│ [                           ] │  ← input 48 px, 16 px betű
│ ⓘ Add meg, hány adagot kérsz. │  ← hiba a mező ALATT
│ …                             │
│ [ Kérés elküldése ]           │
├───────────────────────────────┤
│ HOL ÉS MIKOR / VÉLEMÉNYEK /   │
│ GYIK / LÁBLÉC (egy oszlop)    │
├───────────────────────────────┤
│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│  ← 84 px üres hely a fix sávnak
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

A tokenek **anyagnevek**, nem szerepnevek: ez tartja meg a §3.6 fegyelmét.
A szerepleképezés külön réteg (`--hatter`, `--szoveg`, `--akcent`…), így a
paletta cserélhető anélkül, hogy komponenst kellene átírni.

| # | Token | Világos | Sötét | Anyag | Szerep |
|---|---|---|---|---|---|
| 1 | `--tejszin` | `#FBF7F1` | `#FBF7F1` | tejszín, papír | világos háttér / sötét szöveg |
| 2 | `--piskota` | `#EADFCB` | — | piskóta | világos emelt felület |
| 3 | `--kakao` | `#241A14` | `#241A14` | étcsokoládé | világos szöveg / sötét háttér |
| 4 | `--ganache` | — | `#3B2A20` | ganache | sötét emelt felület |
| 5 | `--fust` | `#6B6055` | `#B7A899` | füstölt karamell | másodlagos szöveg |
| 6 | `--meggy` | `#8E1D30` | `#E08A7E` | meggy | **akcent, CTA, hiba** |
| 7 | `--karamell` | `#9A5B15` | `#DDA45C` | égetett cukor | jelölés, placeholder, csillag |
| 8 | `--pisztacia` | `#4E6B3C` | `#9FBE85` | pisztácia | „nyitva", pozitív állapot |
| 9 | `--vonal` | `#8F7D63` | `#A08260` | kréta a táblán | vezérlőelem-keret |

**Mért WCAG-kontrasztok** (relatív luminancia szerint számolva, nem becsülve):

| Pár | Világos | Sötét | Követelmény | Státusz |
|---|---|---|---|---|
| törzsszöveg a háttéren | **15,96:1** | **15,96:1** | 4,5:1 | AAA |
| másodlagos szöveg a háttéren | **5,74:1** | **7,36:1** | 4,5:1 | AA / AAA |
| akcent szöveg a háttéren | **8,31:1** | **6,57:1** | 4,5:1 | AAA / AA |
| CTA-felirat a gombon | **8,31:1** | **6,57:1** | 4,5:1 | AAA / AA |
| „nyitva" jelző a háttéren | **5,63:1** | **8,26:1** | 4,5:1 | AA / AAA |
| jelölő (`.ph`) a háttéren | **5,07:1** | **7,74:1** | 4,5:1 | AA / AAA |
| vezérlőkeret a háttéren | **3,73:1** | **4,75:1** | 3:1 (1.4.11) | ✓ |
| vezérlőkeret az emelt felületen | **3,01:1** | **3,81:1** | 3:1 | ✓ |
| szöveg az emelt felületen | **12,91:1** | **12,79:1** | 4,5:1 | AAA |

**A sötét téma nem inverz.** Az akcent nem a `#8E1D30` invertálva lenne, hanem
`#E08A7E` — ez a meggy tejszínbe keverve, nem rózsaszín. A cél az volt, hogy
a márkaszín *anyagi értelemben* is helyes maradjon: sötét felületen a meggy
nem sötétebb lesz, hanem hígabb. A `--karamell` és a `--pisztacia` ugyanígy
világosodik, nem telítettebb lesz.

**Miért nem `prefers-color-scheme` duplikáció?** A tokenek `light-dark()`-kal
vannak írva, minden deklaráció előtt egy sima fallback-értékkel:

```css
--hatter:#FBF7F1;                          /* régi böngésző: mindig világos */
--hatter:light-dark(#FBF7F1,#241A14);      /* modern: a color-scheme dönt */
```

*Alternatíva, amit nem választottam:* a teljes tokenkészlet megismétlése
`@media (prefers-color-scheme:dark)` és `[data-theme="dark"]` alatt. Az működik
mindenhol, de kétszer 30 sor duplikáció, és minden jövőbeli tokenmódosítást
két helyen kell elvégezni — pont ez az a hiba, amitől a design systemek
szétcsúsznak. Az ára: 2023 előtti böngészőben nincs sötét téma. Ezt vállalom,
mert az elrendezés és a kontraszt ott is hibátlan.

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

### 7.4 Elevation

Matt műhely, nem üveg. Négy szint, és a **sötét témán nem árnyékkal, hanem
felület-világosodással** dolgozik, mert sötét háttéren az árnyék nem látszik:

| Szint | Világos | Sötét | Hol |
|---|---|---|---|
| `--e-0` | nincs | nincs | szekciók, listasorok — csak hajszálvonal |
| `--e-1` | `0 1px 2px rgba(36,26,20,.06)` | `0 1px 0 rgba(251,247,241,.06)` | kártya, kapcsoló |
| `--e-2` | `0 2px 4px -2px …, 0 10px 24px -14px …` | `0 2px 12px -6px rgba(0,0,0,.6)` | a keresztmetszet-tömb, elsődleges gomb hoverben |
| `--e-3` | `0 8px 16px -8px …, 0 24px 56px -28px …` | `0 12px 40px -12px rgba(0,0,0,.7)` | (fenntartva modálisnak, jelenleg nem használt) |

Sugarak: `3 / 6 / 12 / 999 px`. Kicsi sugarak — egy műhely pontos, nem buborékos.
Kivétel a jelölő chipek (`999px`), mert ott a pirula-forma önálló jelentést hordoz.

### 7.5 Komponenslista

| Komponens | Állapotok | Megjegyzés |
|---|---|---|
| Gomb (fő / mellék) | alap, hover, active, fókusz, letiltott | min. 48 px magas, `aria-disabled` nem csak `opacity` |
| Nyitva/zárva jelző | nyitva (telt pont) / zárva (üres karika) | **nem csak szín**: a pont formája is különbözik |
| Téma-kapcsoló | 3 állapot, `aria-pressed` | világos / rendszer / sötét |
| **Keresztmetszet** | alap, hover, kiválasztott, csökkentett mozgás | a szignatúra; 7 anyagtextúra |
| Mini keresztmetszet | statikus | `aria-hidden`, csak vizuális azonosító |
| Kínálatsor | alap | mini + név + rétegsor + jelek + ár |
| Jelölő chip | allergén (borostyán) / mentes (zöld) / semleges | szín + szöveg, sosem csak szín |
| Űrlapmező | alap, hover, fókusz, hibás, letiltott | hiba: 2 px keret + halvány háttér + ikon + szöveg |
| Választócsoport | alap, kiválasztott, fókusz | `:has(input:checked)`, min. 52 px |
| Hibaösszegző | rejtett / látható | fókuszt kap, ugróhivatkozásokkal |
| Sikerpanel | rejtett / látható | fókuszt kap, összefoglalja a beküldött adatot |
| Nyitvatartás-táblázat | alap, „ma" kiemelve | egy adatforrásból generált |
| GYIK | zárt / nyitott | `<details name="gyik">` — natív, JS nélkül is működik |
| Mobil cselekvési sáv | — | fix, `safe-area-inset-bottom` |
| Placeholder-jelölés (`.ph`) | — | **terméktervezési eszköz**: szaggatott aláhúzás + borostyán szín; élesítéskor egyetlen `grep`-pel megtalálható |

---

## 8. Animációk és mikrointerakciók

Alapelv: **minden animációnak oksági viszonyt kell kifejeznie.** Ami csak szép,
az kimarad. Globális tokenek: `--idom: 180ms`, belépés `220ms`, kilépés `140ms`
(a kilépés mindig gyorsabb — ettől érzi az ember reszponzívnak),
`--gorbe: cubic-bezier(.2,.7,.3,1)`.

| # | Elem | Interakció | Mi történik | Időzítés | Miért |
|---|---|---|---|---|---|
| A1 | Keresztmetszet-réteg | hover / fókusz | a sáv `translateX(12px)`-szel kicsúszik, a többi `saturate .55 / opacity .6`-ra halványul, a kicsúszó él árnyékot kap | 180 ms, `--gorbe` | A kihúzás fizikai metafora: a réteget *kiveszik* a szeletből. Ez az egyetlen hely, ahol a mozgás információt hordoz, nem kíséretet ad. |
| A2 | Keresztmetszet-réteg | kattintás / Enter | ugyanaz, de rögzül; `aria-pressed="true"` | 180 ms | Érintőn nincs hover — kattintással kell rögzíthetőnek lennie. |
| A3 | Keresztmetszet | **`prefers-reduced-motion`** | nincs eltolás; helyette 2 px belső körvonal | 0 ms | Az információ (melyik réteg) megmarad, a mozgás nem. Nem „letiltjuk az animációt", hanem **más csatornán adjuk ugyanazt**. |
| A4 | Elsődleges gomb | hover | háttér 8%-kal sötétebb (világos) / világosabb (sötét) + `--e-1` → `--e-2` | 180 ms | Emelkedés = megnyomható. `active`-ban az árnyék eltűnik: lenyomódik. |
| A5 | Gomb / link | fókusz | 2 px accent gyűrű + 4 px háttérszínű külső gyűrű | azonnali | A kettős gyűrű bármilyen felületen látszik. Fókusznál nincs késleltetés — a billentyűzetes navigációt a lassulás elrontja. |
| A6 | Navigációs link | hover | háttér `--felulet-halk` | 180 ms | |
| A7 | Téma-kapcsoló | kattintás | az aktív pirula háttere és árnyéka átvált; a `<meta name="theme-color">` is frissül | 180 ms | A böngésző UI-sávja együtt vált a lappal, különben villan. |
| A8 | Nyitva/zárva jelző | percenkénti újraszámítás | szöveg + pontforma vált | nincs átmenet | Állapotváltásnál az animáció félrevezető: nem a felhasználó okozta. |
| A9 | Űrlapmező | `blur` (nem gépelés közben) | keret accentre vált, hibaszöveg megjelenik alatta | 180 ms keret, szöveg azonnal | Gépelés közbeni validálás bünteti a felhasználót azért, mert még nem fejezte be. |
| A10 | Hibás űrlapmező | `input` | ha már hibás volt, gépelés közben azonnal újraértékel | azonnali | Javításkor viszont *azonnali* visszajelzés kell — az irány itt megfordul. |
| A11 | Hibaösszegző | küldés hibával | megjelenik, fókuszt kap, a lista elemei a mezőkre ugranak | nincs átmenet | Fókuszmozgatás animációval késleltetve zavaró képernyőolvasóval. |
| A12 | Sikerpanel | sikeres küldés | megjelenik, fókuszt kap, a gomb letiltódik és „Elküldve" lesz | nincs átmenet | Dupla küldés megelőzése. |
| A13 | GYIK | nyitás | a `summary` nyila 45° → 225° fordul | 180 ms | A nyíl iránya az állapotot jelzi, a fordulás a változást. |
| A14 | Oldalon belüli link | kattintás | `scroll-behavior: smooth` | böngészőalapú | `prefers-reduced-motion` esetén `auto` — a hosszú görgetés mozgásérzékenyeknél rosszullétet okoz. |
| A15 | Fejléc | görgetés | **semmi** | — | Nincs elrejtés-visszahozás, nincs zsugorodás. Egy ragadós fejléc, ami mozog, elveszi a figyelmet a tartalomtól, és a fix elem magasságának változása CLS-t okozhat. |

**Amit szándékosan nem csinálunk:** görgetésre megjelenő („scroll reveal")
szekciók, parallax, számláló-animáció az 5,0-n, betöltéskori „fade in".
Ezek mind késleltetik a tartalmat azért, hogy a fejlesztő megmutassa, tud
animálni. Egy nyitvatartást kereső embernek ez ellenség.

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

### 9.3 Képek

Ma **nincs kép** az oldalon, és ez nem kényszer, hanem eredmény (§3.7).
Amikor lesz fotóanyag (§15/2), a szabályok:

| Szabály | Konkrétan |
|---|---|
| Formátum | AVIF `<source>`, WebP fallback, JPEG utolsó lépcsőben |
| Méretek | `srcset` 400 / 800 / 1200 px, `sizes` a tényleges rácsból |
| Helyfoglalás | `width`+`height` **vagy** `aspect-ratio` minden `<img>`-en — kötelező, CLS miatt |
| Betöltés | a hajtás alattiak `loading="lazy" decoding="async"` |
| A hero | **továbbra sem kap fotót.** A fotók a kínálatsorokba és az `/a-muhely/` oldalra kerülnek |
| `alt` | leíró, nem kulcsszóhalmozó. Dekoratív képnél `alt=""` |

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
nem a fejlesztő gépe. A mérce a §2.4-ben rögzített: nem lehet lassabb a
döntési úton, mint a Google-listing, amit leváltunk.

| Metrika | Cél | Küszöb, ami fölött hiba | Mivel érjük el |
|---|---|---|---|
| **LCP** | **≤ 1,3 s** | 2,5 s | Nincs hero-kép; az LCP-elem a `H1` szövege. Kritikus CSS inline, betűk preloaddal. |
| **FCP** | ≤ 0,9 s | 1,8 s | Egyetlen HTML-kérés, blokkoló külső CSS nélkül. |
| **CLS** | **≤ 0,02** | 0,1 | Minden sáv fix magasságú; metrikára illesztett fallback-betű; a hibaszövegek üresen 0 magasak, de a DOM-ban vannak; nincs késve érkező banner. |
| **INP** | **≤ 120 ms** | 200 ms | 3,3 kB JS, nincs keretrendszer, nincs hydration. A legdrágább kezelő az űrlap-validáció: egy mező, szinkron. |
| **TBT** | ≤ 50 ms | 200 ms | Nincs harmadik feles szkript. |

### 11.1 Bájtköltségvetés (élesített változat, brotli után)

| Erőforrás | Költségvetés | A prototípusban mért |
|---|---|---|
| HTML (fontok nélkül) | **≤ 22 kB** | 21,0 kB gzip ✓ |
| CSS (inline, kritikus) | ≤ 9 kB | 8,3 kB gzip ✓ |
| JS | **≤ 4 kB** | 3,3 kB gzip ✓ (nyers 8,7 kB) |
| Betűk (2 × woff2) | ≤ 55 kB | 51,8 kB ✓ |
| Képek az első nézetben | **0 kB** | 0 ✓ |
| **Első betöltés összesen** | **≤ 90 kB** | **~81 kB** ✓ |
| Kérésszám az első nézethez | ≤ 3 | 3 (HTML + 2 betű) |

A prototípus `index.html`-je 145 kB, mert a betűk base64-gyel benne vannak
(§9.2). Élesben ez szétválik, és a betűk egy évig cache-elődnek — a **második**
oldalletöltés így ~22 kB.

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

### 12.1 Mit mérünk

| Esemény | Hogyan |
|---|---|
| `elorendeles_bekuldve` | űrlap-siker, a „mit" értékkel dimenzióként |
| `telefon_koppintas` | `tel:` link kattintás |
| `sms_koppintas` | `sms:` link kattintás |
| `utvonal_koppintas` | Google Térkép link |
| `ertekeles_koppintas` | „Írj értékelést" |
| `keresztmetszet_hasznalat` | legalább egy réteg kiválasztva — ez méri, hogy a szignatúra elem *működik-e*, vagy csak dísz |

Az utolsó tétel önvizsgálat: ha három hónap alatt a látogatók kevesebb mint
10%-a nyúl hozzá, a keresztmetszet interaktív rétege felesleges, és statikus
illusztrációra kell egyszerűsíteni.

---

## 13. A fontos design-döntések, alternatívával együtt

| # | Döntés | Alternatíva | Miért nem az alternatíva |
|---|---|---|---|
| D1 | A redesign tárgya a hiányzó saját webhely, nem a listing | A Google-profil „átalakítása" | A listing layoutja nem birtokolt és nem szerkeszthető. Amit ott lehet, az adatpontosítás — az a §10.5, nem redesign. |
| D2 | **Keresztmetszet** mint szignatúra | Nagyméretű termékfotó-hero | Nincs jogtiszta fotó; a fotó a tetőt mutatja, nem a szerkezetet; és 60–110 kB + egy kérés + dekódolás LCP-költség. |
| D3 | A paletta anyagnevekből | Absztrakt márkaszínek (pl. „primary/secondary") | Anyagnév-kényszer nélkül a paletta 3 iteráció alatt elcsúszik a szakmától. Ha egy szín nem nevezhető meg a műhely anyagával, nem kerül be. |
| D4 | Meggy akcentnek | Rózsaszín (torta-alapértelmezés) / arany (elegancia) | A rózsaszín az esküvő-/torta-marketing közhelye; az arany 1–2000 Ft/fő ársávnál hazugság. A meggy egy magyar cukrászati **alapanyag**, nem hangulat. |
| D5 | Fraunces + Commissioner | Playfair + Inter | A brief tiltja, és jogosan: nem mond semmit a szakmáról. Lásd a §7.2 alternatívatáblázatát. |
| D6 | `light-dark()` a témákhoz | Teljes tokenkészlet duplikálva `@media` + `[data-theme]` alatt | 60 sor duplikáció, két helyen karbantartandó. Ára: régi böngészőben nincs sötét téma — de az elrendezés és a kontraszt ott is hibátlan. |
| D7 | Sötét téma = hígított akcent, nem invertált | Színek matematikai invertálása | Az invertálás a meggyet zölddé tenné. Az anyagi logika (meggy tejszínben) ad helyes és felismerhető sötét palettát. |
| D8 | Az oldal egy dolga: **előrendelés** | Asztalfoglalás / webshop | Foglalás: ismeretlen, van-e ülőhely (§15/7), és 1–2000 Ft/fő ársávnál a foglalás túlzás. Webshop: a fizetési integráció fenntartása többe kerül, mint a haszna. |
| D9 | Az SMS önálló, megnevezett csatorna | Csak telefonszám | A mobilszám (J6) miatt az SMS **ma is működik**; nulla fejlesztési költséggel nyit egy aszinkron utat. |
| D10 | Nincs `aggregateRating` markup | A 5,0 markupolása a rich resultért | Saját oldalon a saját értékelés „self-serving": nem jogosult, és manuális intézkedést kockáztat. Az érték láthatóan ott van — csak nem markupolva. |
| D11 | Statikus HTML + 11ty | WordPress | Hatoldalas, ritkán változó oldalhoz plugin-karbantartás és 300–800 kB alapteher. |
| D12 | Placeholderek **láthatóan jelölve** (`.ph`) | Kitalált mintaszöveg vagy lorem ipsum | Kitalált ár/nyitvatartás élesben átcsúszhat. A szaggatott borostyán aláhúzás egyszerre olvasható a designban és `grep`-elhető a kódban. |
| D13 | Nincs görgetés-animáció, nincs parallax | „Modern" scroll-reveal | Késlelteti a tartalmat azért, hogy a fejlesztő mutasson valamit. Egy nyitvatartást kereső embernek ez ellenség. |
| D14 | Egyetlen `NYITVATARTAS` adatforrás négy felhasználással | Külön beírt óraértékek a táblázatban, a jelzőben, a validációban és a schemában | A négy hely előbb-utóbb szétcsúszik, és a schema mond mást, mint az oldal. |
| D15 | Nincs süti-banner | Analitika sütivel | Süti nélküli mérés (Plausible / szervernapló) elegendő, és a banner az első interakció elrablása. |
| D16 | A hero nem sorszámoz („01/02/03") | Számozott „hogyan működik" lépéssor | A három út (bejössz / hívsz / előre kéred) **párhuzamos**, nem sorrend. Számozni azt, aminek nincs sorrendje, hazugság. |

---

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
| `index.html` | 145 216 B (ebből 69 128 B a két base64 betű) |
| HTML betűk nélkül | 76 094 B · **21 018 B gzip** |
| CSS | 29 779 B · **8 255 B gzip** |
| JS (2 blokk: téma-bootstrap + fő) | nyers 11 270 B · komment nélkül 8 700 B · **3 297 B gzip** |
| JSON-LD | 3 885 B |
| Szignatúra elem (HTML + CSS) | 3 946 + 4 973 B |
| Külső kérés | **0** |
| Kép | **0** |

**Ellenőrzött viselkedés** (fejetlen Chromium, 320 / 375 / 390 / 768 / 1440 px,
világos és sötét, `prefers-reduced-motion: reduce`):

- vízszintes görgetés: **nincs**, egyik szélességen sem;
- címke nélküli űrlapmező: **0**; hozzáférhető név nélküli gomb/link: **0**;
- első `Tab`: „Ugrás a tartalomra";
- `role="alert"` hibamezők üresen 0 magasak, de a DOM-ban maradnak;
- csökkentett mozgásnál a rétegkiemelés `transform: none`, körvonallal helyettesítve;
- konzolhiba: **nincs**;
- az űrlap-validáció végigmérve: üres küldés → 7 hiba + összegző; 09:00-s átvétel
  → „Aznap 11:00 és 18:00 között vagyunk nyitva"; mai dátum → „Legalább 2 nappal
  előbb…"; helyes kitöltés → sikerpanel + a gomb letiltása.

---

## 17. Őszintén: mi ennek az anyagnak a leggyengébb pontja

**Az, hogy az ügyfélről hat adatot tudok, és arra épül tizenhét oldalnyi terv.**

Konkrétan:

1. **A központi stratégiai döntés — hogy az oldal EGY dolga az előrendelés —
   egy hipotézis, nem tudás.** Levezettem az ársávból, a mobilszámból és a
   „műhely" szóból, de nem beszéltem az ügyféllel. Ha kiderül, hogy nincs
   előrendelés, vagy hogy a bevétel 90%-a a betérő kávézó vendég, akkor a §5
   oldalfelépítése és a §12 CRO-tábla fele újraírandó. **Ez a legnagyobb
   egyedi kockázat az anyagban.**

2. **A kínálat teljes egészében placeholder.** Egy desszertoldal, aminek nincs
   étlapja, a felét sem tudja annak, amire képes. A `/kinalat/` — a
   legértékesebb oldal — nem létezik, csak a sablonja.

3. **A szignatúra elem egy általam kitalált mintadesszertet mutat.** A hét
   réteg valós cukrászati komponens, de **nem biztos, hogy a Krém ilyet
   csinál.** Ha kiderül, hogy főleg egyszerű, kétrétegű süteményeket készítenek,
   a keresztmetszet mint alapötlet nem dől meg, de sokkal szerényebb lesz —
   és akkor jogos a kérdés, elbírja-e egyedül a hero-t.

4. **A „Bejelentette 7 személy" értelmezése következtetés** (§15/17). Erre
   építettem a K2-t és az egész §10.5 sürgősségét. Közepes bizonyosságú.

5. **Az öt teljes oldalból egy készült el.** A `/kinalat/`, `/elorendeles/`,
   `/a-muhely/` és `/allergenek/` szekciótáblaként létezik, kódként nem. Az
   ütemterv ezt fázisokra bontja, de a leszállított kód a főoldal.

6. **A `light-dark()` döntés (D6) modern böngészőt feltételez.** Vállalható,
   de ha kiderül, hogy a látogatók jelentős része régi Androidon böngészik,
   ez a duplikáció-mentesség rossz csere volt, és vissza kell írni a
   `@media`-blokkokat.

7. **Nem beszéltem egyetlen vendéggel sem.** A célközönség-leírás (§0.1)
   irodai következtetés. Öt beszélgetés a pult mellett többet érne, mint ez
   az egész dokumentum §12-es fejezete.

Amit ezzel szemben **nem** tartok gyengének: a design system számai mérve
vannak, nem becsülve; a prototípus akadálymentességét gépi ellenőrzéssel
átnéztem; és sehol nincs kitalált ár, nyitvatartás vagy kapacitás — ami nem
tudott, az jelölve van.
