# Papa Giorgio Street Food, Pécs — UI/UX redesign koncepció és prototípus

> **Módszertani figyelmeztetés: rekonstrukcióból dolgoztam.**
> A `https://papagiorgio.webnode.hu` közvetlen lekérése ebben a környezetben hálózati
> szinten tiltott (`EGRESS_BLOCKED`), ahogy a `papagiorgio.hu`, a `falatozz.hu`, a
> `foodora.hu` és a többi aggregátor is. Az elemzés **a keresőben indexelt tartalomra**
> és a briefben beillesztett Google-cégprofil-szövegre épül. Minden ténymegállapítás
> mellett ott a forrás és a bizonyosság szintje. **Élesítés előtt a §15 kérdéslistáját
> le kell futtatni az élő oldalon és az ügyféllel.**
>
> Amit ez konkrétan jelent: a §1 (jelenlegi oldal) és a §2 *performance* blokkja
> a leggyengébben alátámasztott rész — a platform ismeretéből következtetek, nem
> mérésből. A §11-ben megadott célszámok viszont abszolút célok, nem az elődhöz
> mért javulások, tehát azok akkor is érvényesek, ha a kiindulási mérés más lesz.

---

## 0. Kontextus — amit tudok, és amit nem

A brief kontextusmezői üresen érkeztek. Az alábbi tábla **csak dokumentált tényeket**
tartalmaz. Számot, kapacitást, árat sehol nem találtam ki; ami hiányzik, az a §15-ben
kérdésként szerepel.

| Mező | Amit tudok | Forrás / bizonyosság |
|---|---|---|
| Ügyfél | Papa Giorgio Street Food, 7632 Pécs, Krisztina tér 10. (Kertváros) | Google-cégprofil + nyitva.hu, firmania, cylex · **magas** |
| Telefon | 06 70 254 3922 | cégprofil + több katalógus egybehangzóan · **magas** |
| Második telefonszám | egy katalógusban felbukkan a +36 70 522 6460 is | egyetlen forrás · **alacsony — tisztázandó** |
| Jelenlegi webhely | `papagiorgio.webnode.hu`, indexelt aloldalak: `/`, `/etlap/`, `/rolunk/`, `/fotogaleria/`, `/kapcsolat/` | keresőindex · **magas** |
| Második domain | `papagiorgio.hu` — külön indexelve, „Papa Giorgio – Street Food" címmel | keresőindex · **közepes** (a tartalmát nem láttam) |
| Konyha | pizza (30 és 45 cm), hamburger, sajtburger, kebabburger, szendvics, hot dog, kebab, gyros, pljeskavica, csirke box, saláta, desszert | foodora + Falatozz + saját `/etlap/` · **magas** |
| Dokumentált pizzanevek | Papa, Son-Go-Ku, Baros, Éden, Maffia, Diablo, Vadász | indexelt étlaptartalom · **közepes** |
| Dokumentált árak | 30 cm pizza 1 950–3 000 Ft · 45 cm 3 450–5 800 Ft · kebabburger 2 000 Ft, menüben 2 900 Ft · hamburger menü 2 900 Ft-tól · sajtburger menü 3 000 Ft-tól · csirkés saláta 2 700 Ft | aggregátorok indexelt étlapja, 2026-09 · **közepes — tételenként ellenőrizendő** |
| Ársáv | 2 000–4 000 Ft / fő | Google-attribútum (brief) · **közepes** |
| Értékelés | Google 4,9 ★ / 190 vélemény; RestaurantGuru 4,8 ★ / 159 vélemény | brief + RestaurantGuru · **közepes** (naponta változik) |
| Nyitvatartás | K–Szo 11:00–21:00, V–H zárva | nyitva.hu, firmania · **közepes** |
| Nyitvatartás — ütköző adat | a Google-cégprofil „Zárás: 20:30"-at mutat | brief · **ütközik a fentivel — ez a §15/1. kérdés** |
| Tér | szabadtéri asztalok; **foglalni nem lehet** | Google-attribútum (brief) · **magas** |
| Kiszállítás | foodora és Falatozz.hu | mindkét platformon él a listing · **magas** |
| Nyitás éve | 2020 nyara („Új Street Food Bar Kertvárosban" blogbejegyzés, 2020. június) | egyetlen blogforrás · **közepes** |
| Történet | a család több generáció óta pizzát süt, hagyományos receptekkel | a saját `/rolunk/` oldal indexelt szövege · **közepes** |
| Vendégvisszajelzés visszatérő motívumai | bőséges és ízletes gyros; „kedves futár"; 15–20 perces kiszállítás; „nem a legolcsóbb, de az ár-érték arány remek" | indexelt vélemény-összefoglalók · **közepes** |

### Munkahipotézisek

Ezek alapján dolgoztam; a §15-ben mind megerősítendő.

- **Az oldal EGY dolga: rendelést indítani.** Nem foglalás — azt a Google-attribútum
  kizárja („Nem lehet foglalni"), és a szabadtéri asztalok érkezési sorrendben mennek.
  A rendelés három csatornán megy: telefon, elvitelre szóló előrendelés, kiszállítás
  platformon. A weboldar dolga eldönteni, hogy a látogató **melyikbe** lép be, és
  odalökni — nem az, hogy önmagában rendelési motor legyen (§13, D9).
- **Célközönség.** (a) Kertvárosi lakók, 20–50, hétköznap 17–20 óra között, „nem
  főzök ma"; a döntés 30 másodperc, állva, egy kézzel, telefonon. (b) Környékbeli
  munkahelyek ebédideje, 11–14 óra, ismétlődő rendelés, ár- és időérzékeny.
  (c) Alkalmi látogató, aki a Google Térképről jön, és egyetlen dolgot akar tudni:
  nyitva vagytok-e most, és mennyi.
- **Amit nem szabad megváltoztatni:** a „Papa Giorgio" márkanév, a telefonszám, a cím,
  és a már indexelt `/etlap/`, `/rolunk/`, `/kapcsolat/` URL-ek.

### A vizuális kiindulópont — egy mondatban

> **A 220 °C-os lapsütő felülete: a szenes grafitszürke fém, a rajta karamellizálódó
> hús parázs-narancs kérge, és a zsírpapír, amibe becsomagolják.**

Ez nem hangulat, hanem tárgy: a hely tényleges munkaeszköze. Ebből jön a paletta
(§7.1), a szignatúra elem (§7.6) és a hero sötét fémlapja. Nem „olasz étterem"
(a név megtévesztő: a kínálat balkáni–amerikai street food), nem „vidám gyorsétterem",
és nem az AI-alapértelmezés (fekete háttér + egy neon accent, §13/D3).

---

## 1. A jelenlegi oldal elemzése

### 1.1 Technológia

| Jel | Megfigyelés | Következtetés |
|---|---|---|
| Domain | `papagiorgio.webnode.hu` — a Webnode aldomainje | Site-builder, ingyenes vagy alap csomag; nincs saját domain rajta |
| Címkeminta | „Étlap - PapaGiorgio - Webnode", „Rólunk - PapaGiorgio - Webnode", de „Kapcsolat :: papagiorgio", „Fotógaléria :: papagiorgio" | **Két különböző, generált title-séma egy oldalon belül** — a szerkesztő két korszakában készült oldalak |
| Márkanév a címekben | „PapaGiorgio" (egybeírva, kisbetűs változatban is) | Eltér a Google-profil és a foodora „Papa Giorgio Street Food" alakjától |
| Struktúra | `/`, `/etlap/`, `/rolunk/`, `/fotogaleria/`, `/kapcsolat/` | Klasszikus ötoldalas brosúra-IA |
| Platformkövetkezmények | közös sablon-CSS és -JS minden aloldalon, sütibanner, builder-képkiszolgálás | Nincs kontroll a kritikus CSS, a betűbetöltés, a képformátum és a cache-fejlécek felett |
| Második domain | `papagiorgio.hu` külön indexelve | Két digitális belépőpont ugyanarra a vállalkozásra |

A technológiai megállapítások **nem mérésből**, hanem a platform ismert viselkedéséből
és az indexelt címkékből származnak. A §2 performance-blokkja ezért feltételezés, nem
lelet — a §14 nulladik fázisa méréssel kezdődik.

### 1.2 Mi a JÓ benne — külön szedve, és megtartandó

Ezeket nem azért tartom meg, mert régiek, hanem mert működnek. Egy redesign, ami
ezeket eldobja, rombol.

1. **Az információs architektúra alakja már helyes.** Étlap, Rólunk, Kapcsolat,
   Galéria — pontosan ez a négy dolog kell egy ilyen méretű vendéglátóhelynek.
   Nem kell új struktúrát kitalálni, csak súlyozni és egy ötödik dolgot (rendelés)
   beemelni. **Átvéve.**
2. **Az URL-ek magyarul, rövidek, beszédesek** (`/etlap/`, `/rolunk/`, `/kapcsolat/`).
   Indexeltek, esetleg belinkeltek. **Változatlanul átvéve** — §4.
3. **Létezik saját „Rólunk" történet**, és nem üres: több generációnyi pizzasütés,
   hagyományos receptek. A pécsi street food mezőnyben ez ritka; a legtöbb versenytárs
   oldalán semmi nincs a hely mögötti emberekről. **Ez a differenciátor, előrébb kerül.**
4. **Van ételfotó-galéria.** Street foodnál a fotó közvetlen konverziós eszköz.
   Nem törlöm — **áthelyezem** oda, ahol elad: a tétel mellé (§4, `/fotogaleria/` → 301).
5. **A telefonszám a tartalomban van**, és egyezik a cégprofillal. Ez a legfontosabb
   konverziós adat, és már most helyes.
6. **A csatornamix jó.** Google-cégprofil + foodora + Falatozz + Facebook: a
   vállalkozás ott van, ahol keresik. A weboldal az egyetlen gyenge láncszem, nem
   a jelenlét egésze.
7. **HTTPS működik**, az oldal indexelt, nincs kiesés. A kiindulás nem nulla.

### 1.3 Strukturális megfigyelés: a listing erősebb, mint a saját oldal

A briefben beillesztett szöveg (4,9 ★, 190 értékelés, „Hívás / Útvonal / Webhely /
Megosztás / Mentés", ársáv, attribútumok, „Bejelentette 44 személy") **a Google
cégprofilja, nem a weboldal**. Ez önmagában diagnózis: a vállalkozás digitális
belépőpontja ma a Google-találat, a weboldal csak egy gomb rajta. A redesign valódi
tétje nem az, hogy szebb legyen az oldal, hanem hogy **a „Webhely" gombra kattintó
forgalom ne vesszen el** — ma ugyanis egy brosúrára érkezik, ahol nincs mit csinálni.

---

## 2. Problémalista — bizonyítékkal

Jelölés: **[M]** = mért/megfigyelt tény, **[F]** = platformismeretből következtetett
feltételezés (méréssel igazolandó, §14/F0).

### 2.1 Kritikus (a bevételt közvetlenül érinti)

| # | Probléma | Bizonyíték |
|---|---|---|
| K1 | **Két domain ugyanarra a vállalkozásra.** `papagiorgio.webnode.hu` és `papagiorgio.hu` külön-külön indexelt. | **[M]** Mindkettő megjelenik a találati listában, azonos névvel. Következmény: megosztott linkerő, kanonikus bizonytalanság, a felhasználó nem tudja, melyik az „igazi". |
| K2 | **Az oldal nem válaszol a legfontosabb kérdésre: „nyitva vagytok most?"** | **[M]** A nyitvatartás egyik indexelt saját aloldalon sem jelenik meg; csak aggregátorokon (nyitva.hu, firmania) és a Google-profilon. |
| K3 | **A nyitvatartási adat forrásonként ütközik.** Google: zárás 20:30. Aggregátorok: 21:00. | **[M]** A brief és a katalógusok szövege. Egy vendég, aki 20:40-kor indul el, vagy hiába megy ki, vagy feleslegesen marad otthon. |
| K4 | **Nincs rendelési útvonal az oldalon.** Se telefonhívás-CTA, se platformlink, se előrendelés. | **[M]** Az indexelt oldalak (`/etlap/`, `/kapcsolat/`) szövege leíró, nem cselekvésre hívó. A bevétel a foodorán, a Falatozzon és telefonon keletkezik — az oldal egyikbe sem vezet. |
| K5 | **Márkanév-inkonzisztencia.** „PapaGiorgio" a title-ökben, „Papa Giorgio Street Food" mindenütt máshol. | **[M]** Indexelt címkék. Gyengíti a márkakeresést és a Google szemében az entitásegyezést. |

### 2.2 UX

| # | Probléma | Bizonyíték |
|---|---|---|
| U1 | **Identitászavar: pizzéria vagy street food?** A `/kapcsolat/` szövege „finom pizzákra szakosodott pizzériaként" mutatja be a helyet; a cégnév, a Google-kategória és a kínálat fele street food. | **[M]** Az indexelt saját szöveg és a cégnév ellentmond egymásnak. A látogató nem tudja, mit vár. |
| U2 | **Az étlap ár nélkül.** Az indexelt `/etlap/` tartalom tételeket sorol, árakat nem. | **[M]** Az árak csak a foodorán és a Falatozzon indexeltek. Következmény: a vendég ár miatt átmegy a platformra — és ott is rendel, jutalékkal. |
| U3 | **Nincs mobilra tervezett elsődleges akció.** Webnode-sablon, asztali gondolkodás. | **[F]** A használati helyzet (állva, egy kézzel, 30 másodperc) semmilyen sablonelemben nem tükröződik. |
| U4 | **A fotógaléria zsákutca.** Külön oldal, saját menüponttal, ahonnan nem vezet út a rendeléshez. | **[M]** Önálló `/fotogaleria/` URL, saját title-lel. |
| U5 | **Sehol nincs kimondva, hogy nem lehet foglalni.** | **[M]** A Google-attribútum tudja, az oldal nem. Következmény: felesleges foglalási telefonhívások, csalódott érkezők. |
| U6 | **Nincs semmi a 4,9 csillagról az oldalon.** A legerősebb bizalmi eszköz kizárólag a Google-találatban él. | **[M]** Az indexelt saját tartalomban nem szerepel. |

### 2.3 SEO

| # | Probléma | Bizonyíték |
|---|---|---|
| S1 | **A title-ök pixelt pazarolnak.** „Étlap - PapaGiorgio - Webnode" — a „Webnode" szó a platformot hirdeti, nem az éttermet. | **[M]** Indexelt címkék. |
| S2 | **A title-ökben nincs helymegjelölés.** Se „Pécs", se „Kertváros", se „Krisztina tér". | **[M]** Elveszti a „pizza rendelés Pécs", „street food Pécs Kertváros" típusú kereséseket, amelyek a tényleges kereslet. |
| S3 | **Aldomain egy site-builder domainjén.** | **[M]** A `webnode.hu` gyűjti a tekintély egy részét; a saját domain nem épül. |
| S4 | **Feltehetően nincs `Restaurant`/`Menu` strukturált adat.** | **[F]** A Webnode alapból nem emittál éttermi sémát. Következmény: nincs rich result, nem jelenik meg a nyitvatartás és az étlap a találatban. |
| S5 | **Két title-séma, tehát legalább két generációnyi, nem karbantartott oldal.** | **[M]** „- Webnode" vs „:: papagiorgio". |
| S6 | **Nincs tartalom a tényleges kérdésekre.** „nyitva", „asztalfoglalás", „kiszállítás", „mennyibe kerül" — egyikre sincs válaszszöveg. | **[M]** Nincs ilyen indexelt tartalom a saját domainen. |

### 2.4 Performance

Ez a leggyengébben alátámasztott blokk: az oldalt nem tudtam lekérni, tehát nem
mértem. **Minden itteni pont [F]**, és a §14/F0 első feladata megmérni.

| # | Feltételezett probléma | Miért valószínű |
|---|---|---|
| P1 | Közös sablon-CSS és -JS minden aloldalon, függetlenül attól, mire van szükség | A site-builderek definíció szerint általános sablont szállítanak; nincs oldalankénti bundle |
| P2 | A galériaképek nem AVIF/WebP, `srcset` nélkül | A builder képkezelése nem konfigurálható a szerkesztőből |
| P3 | Nincs kontroll a kritikus CSS, a betűbetöltés és a cache-fejlécek felett | A platform zárt |
| P4 | Sütibanner + külső scriptek a fő szálon | Minden Webnode-oldalon fut |

---

## 3. Miért rosszak ezek — a mögöttes ok, nem a tünet

Négy tünetcsoportot látunk, de csak három oka van.

### 3.1 Az oldal rossz műfajban készült

2020-ban, nyitáskor egy weboldal még **névjegy** volt: itt vagyunk, ezt csináljuk,
így hívj minket. A Webnode-sablon pontosan ezt a műfajt szolgálja ki, és akkor
helyes döntés volt: egy óra alatt online.

A vállalkozás kereslete azonban **tranzakciós és időérzékeny**. Egy street food hely
iránti kereslet nem „szeretnék megismerkedni veletek", hanem „most éhes vagyok,
nyitva vagytok, mennyibe kerül, mennyi idő". A névjegy műfaja erre szerkezetileg
nem tud válaszolni — nem attól, hogy régi vagy csúnya, hanem mert nem erre való.
Ebből következik **K2, K4, U3, U5** egyszerre.

### 3.2 Az identitás elmozdult, a szöveg nem követte

A hely „pizzériaként" írja le magát a saját kapcsolat-oldalán, miközben a cégnévben,
a Google-kategóriában és a kínálat felében street food. Nem szövegezési hiba: a
vállalkozás profilja hat év alatt bővült (pizza mellé burger, gyros, kebab,
pljeskavica), és a weboldal az első hetek állapotát konzerválta. Ebből jön **U1**,
és közvetve **S2** is — mert a keresőnek sem mondja meg senki, mire pozicionáljon.

### 3.3 A rendelés kiszervezve, a weboldal nem lett újrahangolva

Amikor a foodora és a Falatozz átvette a rendelést, a weboldal szerepe csendben
kiürült: már nem ő a csatorna, de senki nem alakította át **útválasztóvá** sem.
Így ma se nem elad, se nem irányít. Ebből jön **K4, U2, U4** — és ez a legdrágább
hiba a listán, mert minden árat kereső látogatót átküld egy jutalékos platformra.

### 3.4 A két domain: nem hiba, hanem befejezetlen költözés

**K1** és **S3** valószínűleg ugyanannak a folyamatnak a két fele: valaki
elindította az átállást saját domainre, de a régi aldomaint nem irányította át.
Ez nem tervezési, hanem üzemeltetési adósság — és a legolcsóbban javítható tétel
az egész listán (§14/F1).

---

## 4. Új információs architektúra és sitemap

### 4.1 Elv

Öt oldal helyett **négy**, plusz két átirányítás. A vezérelv: minden URL-nek legyen
egy dolga, amit el tud végezni. Ami nem tud elvégezni semmit, az szekcióvá válik,
nem oldallá.

### 4.2 Sitemap URL-enkénti indoklással

| URL | Egy dolga | Miért így | Változás |
|---|---|---|---|
| `/` | **Rendelést indítani.** Válaszol arra, hogy nyitva-e, mit kapsz, mennyiért, és három úton kiengedi a látogatót: telefon, előrendelés, platform. | Ez a Google-találat „Webhely" gombjának a landolása. A mai brosúra-főoldal itt veszít el minden forgalmat (§1.3). | **Teljes újraírás** |
| `/etlap/` | **Az árat megmutatni.** Teljes étlap, kategóriánként, minden árral, méretenként. | Már indexelt URL, és ez a második legkeresettebb dolog. Az ár az oldalon tartja azt a látogatót, aki különben átmegy a foodorára (§2.2/U2). | **URL megtartva, tartalom kiegészítve árakkal** |
| `/rolunk/` | **A bizalmat megalapozni.** A család, a generációk óta sütött pizza, a lapsütő, a hely — és ide olvad be a fotógaléria. | Már indexelt URL, és a meglévő tartalom a legjobb differenciátor (§1.2/3). Fotó nélkül a szöveg elvész; szöveg nélkül a fotó zsákutca. Együtt működnek. | **URL megtartva, a galéria beolvad** |
| `/kapcsolat/` | **Odajuttatni.** Cím, térkép, nyitvatartás, telefon, megközelítés, parkolás, „foglalni nem lehet". | Már indexelt URL. Ez a `LocalBusiness` horgonyoldal, a helyi SEO gerince (§10.4). | **URL megtartva, nyitvatartás és foglalási szabály hozzáadva** |
| `/adatkezeles/` | Jogi kötelezettség az előrendelő űrlap miatt. | Az űrlap személyes adatot kér; enélkül nem élesíthető. | **Új** |
| `/fotogaleria/` | — | **301 → `/rolunk/`.** A fotó nem cél, hanem érv. A tétel mellett elad, külön oldalon nem. A linkerő és az esetleges könyvjelzők így nem vesznek el. | **301** |
| `papagiorgio.webnode.hu/*` | — | **301 → a saját domain megfelelő URL-jére**, oldalanként, nem a főoldalra. Ez zárja le a K1/S3 problémát. | **301** |

### 4.3 Amit szándékosan NEM építek meg

| Nem építem | Miért nem |
|---|---|
| Saját rendelési/kosaras motor | A foodora és a Falatozz már működik, van futárhálózata és fizetési integrációja. Egy ekkora helynek saját motort építeni és üzemeltetni rosszabb ROI, mint a jutalék — és a karbantartás terhét is az étteremre teszi. Helyette: **útválasztás** platformokra + telefonos/elvitel-előrendelés a magas margójú, jutalékmentes csatornára. |
| `/pizza-rendeles-pecs/`, `/street-food-kertvaros/` típusú SEO-landolók | Egyedi tartalom nélkül ezek kapuoldalak: vékonyak, és a Google leértékeli őket. Ha később valóban lesz elég egyedi mondanivaló egy pizzaoldalhoz, akkor `/etlap/pizza/` néven jöhet — de tartalommal, nem kulcsszóval (§14/F4). |
| Blog | Nincs, aki hetente írjon. Egy elhagyott blog rosszabb, mint a nem létező. |
| Külön „Asztalfoglalás" oldal | Nem lehet foglalni. Egy oldal, ami nemet mond, felesleges: egy mondat a `/kapcsolat/`-on és egy GYIK-tétel elvégzi. |

### 4.4 Navigáció

Három úti cél van összesen. Ezt **nem szabad hamburgermenübe rejteni** — egy hamburger
akkor indokolt, ha a felsorolás nem fér ki; itt kifér. Ezért:

- **≥840px:** vízszintes nav a fejlécben, mellette a telefonszám mint elsődleges gomb.
- **<840px:** a fejléc alatt egy háromfelé osztott navisáv (mindegyik ≥46px magas),
  plusz **rögzített alsó akciósáv**: `Hívás` + `Előrendelés`. A telefon a legfontosabb
  kimenet, tehát mindig hüvelykujj-távolságban van, `env(safe-area-inset-bottom)`
  figyelembevételével.

---

## 5. Oldalankénti felépítés

### 5.1 `/` — Főoldal

| # | Szekció | Tartalom | Feladat | Elsődleges CTA |
|---|---|---|---|---|
| 1 | Fejléc | Szóvédjegy, nav, témaváltó, telefonszám | Azonnali hívhatóság | Hívás |
| 2 | Hero | Kicker (hely), H1, egymondatos leírás | Megmondja, mi ez és hol | — |
| 3 | **Parázs-sáv** (szignatúra) | A hét szolgálati ablaka hőtérképként + státuszmondat | Megválaszolja: „most sütnek?" | — |
| 4 | Akciósor | Hívás · Teljes étlap · Előrendelés | Három kimenet, súlyozva | Hívás |
| 5 | Bizonyítéksor | 4,9 ★ / 190 vélemény · 2 000–4 000 Ft/fő · foodora, Falatozz · szabadtéri asztalok, foglalás nincs | Bizalom + a foglalási félreértés kiszűrése | — |
| 6 | Három sáv a lapon | Kemence / lap / nyárs — technikánként, a tételnevekkel és az ismert ársávval | Rendezi a kínálatot úgy, ahogy a konyha működik, nem ábécésorrendben | — |
| 7 | Az étlap gerince | 10 legkeresettebb tétel, árral vagy jelölt placeholderrel | Az ár megtartja a látogatót | Teljes étlap |
| 8 | Előrendelés | Három út leírása + akadálymentes űrlap | A jutalékmentes csatorna | Elküldés |
| 9 | Hol, mikor | Cím + útvonal · nyitvatartás-táblázat + ellenőrizendő jelölés | Odajuttat | Útvonal |
| 10 | GYIK | 5 kérdés, `FAQPage` sémával | Lefogja a telefonos ismétlődő kérdéseket | — |
| 11 | Lábléc | Elérhetőség, oldalak, jogi | Másodlagos navigáció | — |
| 12 | Alsó akciósáv (mobil) | Hívás · Előrendelés | Állandó elérhetőség | Hívás |

### 5.2 `/etlap/`

| # | Szekció | Feladat |
|---|---|---|
| 1 | Fejléc + morzsa | Orientáció |
| 2 | Kategóriaugró (sticky chip-sor) | 10+ kategórián ne kelljen görgetni |
| 3 | Kategóriablokkok: Pizza (30/45 cm oszlopban) · Burger és lap · Nyárs · Saláta · Köret · Desszert · Ital | A teljes étlap, minden árral, `tabular-nums` oszlopokban |
| 4 | Allergén- és extrainfó | Jogi + gyakorlati |
| 5 | Rendelési sáv (sticky, mobilon alul) | Hívás · foodora · Falatozz |

Az étlapoldal adata **egyetlen JSON-forrásból** épül (§9.5), hogy a `Menu` séma és a
látható HTML soha ne csússzon szét.

### 5.3 `/rolunk/`

| # | Szekció | Feladat |
|---|---|---|
| 1 | A család és a receptek (a meglévő szöveg átdolgozva) | A differenciátor |
| 2 | A lapsütő — hogyan készül egy burger nálunk | Konkrét, nem marketinges |
| 3 | Fotósor (a beolvasztott galéria), lusta betöltéssel | Étvágy |
| 4 | „Mit mondanak" — 3 valódi vendégvélemény, forrásmegjelöléssel | Bizalom |
| 5 | CTA: étlap + hívás | Kimenet |

### 5.4 `/kapcsolat/`

| # | Szekció | Feladat |
|---|---|---|
| 1 | Cím, telefon, e-mail, térkép (lusta iframe vagy statikus kép + link) | Odajuttat |
| 2 | Nyitvatartás-táblázat + a Parázs-sáv kicsinyített változata | „Most nyitva?" itt is |
| 3 | Megközelítés: parkolás, tömegközlekedés | A valódi akadály |
| 4 | „Foglalni nem lehet" — kimondva, indokkal | U5 lezárása |
| 5 | Kiszállítási platformok | Kimenet |

---

## 6. Wireframe

### 6.1 Főoldal — desktop (≥1024px)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ PAPA GIORGIO street food      Étlap  Rólunk  Kapcsolat   [◐] [ 06 70 … ] │ sticky, 60px
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PÉCS, KERTVÁROS · KRISZTINA TÉR 10.                          ← kicker   │
│                                                                          │
│  Pizza, burger, gyros                                         ← H1, 56px │
│  — amíg forró a lap.                                            2 sor    │
│                                                                          │
│  A Papa Giorgio Street Food a Krisztina téren süt: kézzel                │
│  nyújtott pizza 30 és 45 centiben, burger és pljeskavica…      ← 48ch    │
│                                                                          │
│  ╔══════════════════════════════════════════════════════════════════╗    │
│  ║  ● Most forró a lap.                          Zárás 21:00-kor.   ║    │
│  ║                                                                  ║    │ SZIGNATÚRA
│  ║   H  ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨   ║    │ sötét fém
│  ║   K  ░░░████████████████████████████████████████████████░░░░░░   ║    │ lemez
│  ║  SZE ░░░████████████████████████████████████████████████░░░░░░   ║    │
│  ║  CS  ░░░████████████████████████████████████████████████░░░░░░   ║    │
│  ║   P  ░░░███████████████████[17:31]███████████████████████░░░░░   ║ ←── ma
│  ║  SZO ░░░████████████████████████████████████████████████░░░░░░   ║    │
│  ║   V  ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨   ║    │
│  ║      10:00        13:00       16:00       19:00       22:00      ║    │
│  ╟──────────────────────────────────────────────────────────────────╢    │
│  ║  ▬ forró a lap   ▨ hideg – zárva   A vonal a mostani időt jelöli ║    │
│  ╚══════════════════════════════════════════════════════════════════╝    │
│                                                                          │
│  [ ☎ Hívás – 06 70 254 3922 ]  [ Teljes étlap ]  Elvitelre előrendelek   │
│  ────────────────────────────────────────────────────────────────────    │
│  ★ 4,9 · 190 értékelés   ₣ 2 000–4 000 Ft/fő   ▣ foodora, Falatozz   …   │
├──────────────────────────────────────────────────────────────────────────┤
│ ▓▓▓ SÖTÉT FÉM BLOKK ▓▓▓                                                  │
│  HÁROM SÁV A LAPON                                                       │
│  Kemence, lap, nyárs.                                                    │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐                   │
│  │ A kemencéből  │ │ A lapról      │ │ A nyársról    │                   │
│  │ 2 mondat      │ │ 2 mondat      │ │ 2 mondat      │                   │
│  │ [chip][chip]  │ │ [chip][chip]  │ │ [chip][chip]  │                   │
│  │ ─────────────  │ │ ─────────────  │ │ ─────────────  │                │
│  │ ársáv         │ │ ársáv         │ │ ársáv         │                   │
│  └───────────────┘ └───────────────┘ └───────────────┘                   │
├──────────────────────────────────────────────────────────────────────────┤
│  AMIT A LEGTÖBBEN KÉRNEK                                                 │
│  Az étlap gerince                                                        │
│  ─────────────────────────────────────────────────────────────────────   │
│  Pizza, 30 cm        Kézzel nyújtott korong…          1 950–3 000 Ft     │
│  Pizza, 45 cm        Ugyanaz a tészta…                3 450–5 800 Ft     │
│  Kebabburger         Kebabhús burgerbucin…                  2 000 Ft     │
│  …                                                                       │
│  ( i ) Prototípus-jelzés: az árak indexelt forrásból, ellenőrizendők.    │
│  [ Teljes étlap, minden árral ]                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────┐  ┌──────────────────────────────────────┐  │
│  │ HÁROM ÚT A VACSORÁHOZ    │  │  Előrendelés elvitelre               │  │
│  │ Asztalt nem, ételt igen  │  │  ┌────────────────────────────────┐  │  │
│  │ 2 mondat                 │  │  │ Név *                          │  │  │
│  │ 1 · Telefon    06 70 …   │  │  ├────────────────────────────────┤  │  │
│  │ 2 · Előrendelés   most   │  │  │ Telefonszám *                  │  │  │
│  │ 3 · Kiszállítás platform │  │  ├──────────────┬─────────────────┤  │  │
│  └──────────────────────────┘  │  │ Nap ▾        │ Óra             │  │  │
│                                │  ├──────────────┴─────────────────┤  │  │
│                                │  │ Mit kérsz? *  (textarea)       │  │  │
│                                │  ├────────────────────────────────┤  │  │
│                                │  │ ☐ Hozzájárulok…                │  │  │
│                                │  │ [   Előrendelés elküldése    ] │  │  │
│                                │  └────────────────────────────────┘  │  │
│                                └──────────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────┤
│  Hol vagyunk, mikor sütünk                                               │
│  ┌────────────────────────────┐  ┌────────────────────────────────────┐  │
│  │ CÍM                        │  │ NYITVATARTÁS                       │  │
│  │ 7632 Pécs, Krisztina tér 10│  │ Kedd–szombat, 11:00–21:00          │  │
│  │ Útvonal a Google Térképen ↗│  │ H  zárva / K 11–21 / … (táblázat)  │  │
│  │ Parkolás: [ügyféltől]      │  │ [⚠ ELLENŐRIZENDŐ ADAT]             │  │
│  └────────────────────────────┘  └────────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────┤
│  Gyakori kérdések        ▸ Lehet asztalt foglalni?              ⌄        │
│                          ▸ Mikor vagytok nyitva?                ⌄        │
├──────────────────────────────────────────────────────────────────────────┤
│  Lábléc: márka + leírás │ Elérhetőség │ Oldalak                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Főoldal — mobil (390px)

```
┌────────────────────────────┐
│ PAPA GIORGIO street  [◐]   │ sticky
├──────────┬────────┬────────┤
│  Étlap   │ Rólunk │ Kapcs. │ 46px, három egyenlő
├──────────┴────────┴────────┤
│ PÉCS, KERTVÁROS · KRISZ…   │
│ Pizza, burger,             │
│ gyros — amíg               │ H1 40px, 3 sor
│ forró a lap.               │
│                            │
│ A Papa Giorgio Street Food │
│ a Krisztina téren süt: …   │
│                            │
│ ╔════════════════════════╗ │
│ ║ ● Most forró a lap.    ║ │
│ ║ Zárás 21:00-kor.       ║ │ a részlet külön
│ ║                        ║ │ sorba törik
│ ║  H ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨  ║ │
│ ║  K ░███████████████░░  ║ │
│ ║SZE ░███████████████░░  ║ │
│ ║ CS ░███████████████░░  ║ │
│ ║  P ░████[17:31]████░░  ║ │ ← ma, 38px magas
│ ║SZO ░███████████████░░  ║ │
│ ║  V ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨  ║ │
│ ║   10:00    16:00  22:00║ │ 3 osztás <560px
│ ╟────────────────────────╢ │
│ ║ ▬ forró  ▨ hideg       ║ │
│ ╚════════════════════════╝ │
│                            │
│ [ ☎ Hívás – 06 70 254 …  ] │ teljes szélesség
│ [ Teljes étlap           ] │
│ Elvitelre előrendelek      │
│ ────────────────────────── │
│ ★ 4,9 · 190 értékelés      │ tördelve
│ ₣ 2 000–4 000 Ft / fő      │
│ ▣ foodora, Falatozz        │
│ ⚲ Szabadtéri asztalok      │
├────────────────────────────┤
│ ▓ Kemence, lap, nyárs.  ▓  │
│ ┌────────────────────────┐ │ egy oszlop,
│ │ A kemencéből           │ │ egymás alatt
│ └────────────────────────┘ │
│ ┌────────────────────────┐ │
│ │ A lapról               │ │
│ └────────────────────────┘ │
│ ┌────────────────────────┐ │
│ │ A nyársról             │ │
│ └────────────────────────┘ │
├────────────────────────────┤
│ Az étlap gerince           │
│ Pizza, 30 cm               │ a leírás külön
│ Kézzel nyújtott korong…    │ sorba (order:3)
│              1 950–3 000 Ft│ jobbra zárva
├────────────────────────────┤
│ Előrendelés elvitelre      │ egy oszlop:
│ [ Név              ]       │ a szöveg fent,
│ [ Telefonszám      ]       │ az űrlap alatta
│ [ Nap ▾ ] [ Óra    ]       │
│ [ Mit kérsz?       ]       │
│ ☐ Hozzájárulok…            │
│ [ Előrendelés elküldése  ] │
├────────────────────────────┤
│ … Hol vagyunk / GYIK / lábléc
├────────────────────────────┤
│ [ ☎ Hívás ] [ Előrendelés ]│ fix alul, 50px
└────────────────────────────┘   + safe-area
```

---

## 7. Design system

### 7.1 Színtokenek — 9 nevesített család, mért kontraszttal

Minden érték **kimért**, nem becsült (relatív luminancia → WCAG 2.x kontrasztarány).
A világos és a sötét paletta **együtt** készült: a sötét nem az inverze a világosnak,
hanem világosabb, deszaturáltabb tónusokból áll (`color-dark-mode`).

**Világos téma** — alap: `--papir` `#F4F3F1`

| Token | Hex | Szerep | Kontraszt |
|---|---|---|---|
| `--papir` | `#F4F3F1` | Oldalháttér. Szándékosan **hűvös** papír, nem bézs: így a parázs melegebbnek látszik. | alap |
| `--tepsi` | `#FFFFFF` | Kártya, űrlapmező | — |
| `--tepsi-2` | `#EAE8E4` | Süllyesztett felület, lábléc-sáv | — |
| `--lap` | `#16110D` | Elsődleges szöveg | **16,91 : 1** a papíron · 18,75 : 1 a fehéren |
| `--fust` | `#5E554D` | Másodlagos szöveg | **6,57 : 1** a papíron |
| `--parazs` | `#B8330B` | Elsődleges akcent, CTA-háttér, link | **5,39 : 1** a papíron · fehér rajta **5,97 : 1** |
| `--mustar` | `#E0A81C` | **Csak kitöltés**, sosem szöveg papíron (1,93 : 1) | `--lap` rajta **8,74 : 1** |
| `--olaj` | `#3D4A2F` | Mély olíva: csendes blokk, „hideg" állapot | **8,53 : 1** |
| `--hatar` / `--hatar-eros` | `#DCD8D3` / `#8C847B` | Dekoratív elválasztó / **funkcionális keret** (input, checkbox) | 1,28 : 1 (dekoratív) / **3,32 : 1** (megfelel a nem-szöveges 3:1-nek) |
| `--hiba` / `--rendben` | `#B3261E` / `#2E6B3E` | Állapotszínek | **5,89 : 1** / **5,76 : 1** |

**Sötét téma** — alap: `--papir` `#14100D`

| Token | Hex | Kontraszt az alapon |
|---|---|---|
| `--papir` | `#14100D` | — |
| `--tepsi` / `--tepsi-2` | `#221C18` / `#2C251F` | emelés felülettel, nem árnyékkal |
| `--lap` (szöveg) | `#F2EFEB` | **16,51 : 1** |
| `--fust` | `#B0A69C` | **7,91 : 1** |
| `--parazs` | `#FF8A55` | **8,13 : 1**; `--lap` rajta 7,25 : 1 |
| `--mustar` | `#F0C040` | **11,10 : 1** — sötétben szövegként is használható |
| `--olaj` | `#A3B58A` | **8,59 : 1** |
| `--hatar-eros` | `#6E6259` | **3,20 : 1** |
| `--hiba` / `--rendben` | `#FF9A8F` / `#7FD08C` | **9,26 : 1** / **10,19 : 1** |

**Két szabály, amit a rendszer betart:**

1. A `--mustar` világos témában **soha nem szöveg** — csak háttér sötét szöveggel
   (pl. az „ELLENŐRIZENDŐ ADAT" jelvény). Ez a token dokumentált korlátja.
2. A funkcionális keret (`--hatar-eros`) mindkét témában ≥3:1, a dekoratív
   (`--hatar`) nem — utóbbi soha nem hordoz információt egyedül.

**A Parázs-sáv kivétel.** A szignatúra elem **mindkét témában ugyanaz a sötét fém**
(`#17120E`), mert egy *tárgyat* ábrázol, nem egy felületet. Egy lapsütő nem világosodik
ki attól, hogy a felhasználó világos témát választott. A rajta lévő szöveg
`#F4EFE9` → **15,9 : 1**, a halvány `#A2958A` → **6,4 : 1**, tehát témától függetlenül
megfelel.

### 7.2 Tipográfia

**Két variable betűcsalád, mindkettő teljes latin-ext lefedettséggel** — az `ő` és az
`ű` valóban rajzolt kettős ékezettel, nem összeállított glifával.

| Szerep | Család | Tengelyek | Miért ez |
|---|---|---|---|
| Display | **Sofia Sans Condensed** | `wght` 1–1000, latin + latin-ext + cyrillic + greek | A kondenzált groteszk a piaci árcédula és a zománctábla betűje: sok szó fér el keskeny oszlopban nagy méretben — pontosan úgy, ahogy egy pult fölötti étlaptábla működik. A rendkívül széles súlytengely miatt **egyetlen család** viszi a teljes display-hierarchiát, tehát nem kell harmadik betűt behozni. |
| Szöveg | **Instrument Sans** | `wght` + `wdth`, latin + latin-ext | Kompakt neogroteszk nagy x-magassággal és nyitott betűnyílásokkal: 16px-en, telefonon, napfényben is olvasható — ez a tényleges olvasási helyzet. Enyhén keskeny rajza harmonizál a kondenzált display-jel, de nem versenyez vele. |

**A display face minimális használati mérete: 20px.** Ez alatt a kondenzált szárak
és a magyar kettős ékezet összecsúsznak. Gyakorlati következmény a rendszerben:
**a gombok, a navigáció és minden címke a szövegcsaláddal szedve**, a display face
csak H1–H3-tól és a nagy számadatoktól felfelé jelenik meg.

**Elvetett alternatívák:**

| Alternatíva | Miért nem |
|---|---|
| Playfair Display + Inter | A brief tiltja, és jogosan: ez a 2020-as évek alapértelmezett „AI-designja". A Playfair didone kontrasztja ráadásul semmit nem mond egy street food helyről. |
| Barlow Condensed + Barlow (a ui-ux-pro-max első ajánlása kondenzáltra) | A Barlow lekerekített, „közlekedési" karaktere sport-/edzőterem-hangulatot ad, és a magyar kettős ékezetei display-méretben laposak. |
| Archivo (`wdth` tengellyel) | A keskeny instanciák vállalati-szerkesztőségi hangot ütnek meg; az igazán ütős Archivo Black pedig **nem** variable. |
| Space Grotesk | Van latin-ext, de ez a „neo-brutalista AI-oldal" alapértelmezett betűje — pont attól kellene eltérni. |

**Típusskála** — `clamp()`-pel, mobil→desktop:

| Token | Érték | px |
|---|---|---|
| `--t-mikro` | `0.75rem` | 12 — csak nagybetűs címke |
| `--t-kis` | `clamp(0.8125rem, 0.79rem + 0.12vw, 0.875rem)` | 13→14 |
| `--t-alap` | `clamp(1rem, 0.965rem + 0.18vw, 1.0625rem)` | **16→17** — törzs |
| `--t-nagy` | `clamp(1.0625rem, 0.99rem + 0.35vw, 1.25rem)` | 17→20 — bevezető |
| `--t-h3` | `clamp(1.375rem, 1.21rem + 0.75vw, 1.75rem)` | 22→28 |
| `--t-h2` | `clamp(1.875rem, 1.42rem + 2.1vw, 3.125rem)` | 30→50 |
| `--t-h1` | `clamp(2.25rem, 1.72rem + 2.4vw, 3.5rem)` | 36→56 |
| `--t-adat` | `clamp(1.75rem, 1.35rem + 1.8vw, 2.75rem)` | 28→44 |

Sormagasság: törzs **1,6**; H1–H3 **0,94–1,15**. Sorhossz: törzs max **66ch**.
Árak és időpontok `font-variant-numeric: tabular-nums` — hogy a percenként frissülő
óra ne mozgassa a layoutot.

### 7.3 Térköz — 8px alap

`--s1: 4px` (kizárólag ikonigazításra) · `--s2: 8` · `--s3: 12` · `--s4: 16` ·
`--s5: 24` · `--s6: 32` · `--s7: 48` · `--s8: 64` · `--s9: 96` · `--s10: 128`

Hierarchiaszintek: komponensen belül 8/12/16 · komponensek között 24/32 ·
szekciók között 64 (mobil) / 96 (desktop). Konténer max **1200px**, belső margó
16 → 32 → 48px töréspontonként.

### 7.4 Forma és emelés

Sugár: `--r-s: 3px` · `--r-m: 6px` · `--r-l: 12px`. Szándékosan kicsi: a blokkos,
táblás megjelenés a menütábla és a csomagolópapír világa, nem a lekerekített
alkalmazáskártyáké.

| Szint | Világos | Sötét |
|---|---|---|
| `--e1` | `0 1px 2px rgba(22,17,13,.06), 0 0 0 1px --hatar` | `0 0 0 1px --hatar` |
| `--e2` | `+ 0 10px 24px -10px rgba(22,17,13,.16)` | `+ 0 12px 28px -12px rgba(0,0,0,.7)` |
| `--e3` | `+ 0 28px 56px -20px rgba(22,17,13,.28)` | `+ 0 32px 64px -24px rgba(0,0,0,.85)` |

Sötét témában az emelést **a felület világosodása és a keret** hordozza, nem az
árnyék — fekete alapon a fekete árnyék láthatatlan.

### 7.5 Komponenslista

`Gomb` (fő / másodlagos / csendes; 48px min. magasság, 20px ikon) ·
`Szóvédjegy` · `Fejléc` (sticky, blur) · `Navisáv` (mobil) · `Témaváltó` ·
`Alsó akciósáv` (mobil, safe-area) · **`Parázs-sáv`** (§7.6) ·
`Bizonyítéksor` · `Konyhakártya` (chipekkel) · `Tétellista` (tabular-nums árral) ·
`Megjegyzésdoboz` · `Űrlapmező` (címke + súgó + hibaüzenet) · `Jelölőnégyzet` ·
`Hibaösszegző` (horgonyokkal) · `Sikerpanel` · `Adatkártya` ·
`Nyitvatartás-táblázat` · `Ellenőrizendő-jelvény` · `GYIK-harmonika` · `Lábléc` ·
`Ikonkészlet` (11 SVG-szimbólum, 24-es rács, 1,75px vonal, `currentColor`).

Nulla emoji ikonként, nulla ikonfont, nulla külső ikonkönyvtár.

---

### 7.6 A szignatúra elem: a Parázs-sáv

#### Mi ez

A hero közepén egy sötét fémlemez ül. Rajta hét vízszintes sáv, hétfőtől vasárnapig.
A tengely 10:00-tól 22:00-ig fut. Amelyik napon sütnek, ott a szolgálati ablak
**parázsként izzik** — egy folyamatos, középen legforróbb narancs-ív. Amelyik napon
nem, ott **hideg, átlósan rácsozott acél**. A mai sor kétszer olyan magas, halványan
lélegzik, és keresztülvág rajta egy fehér vonal: **most**. Fölötte egyetlen mondat:
*„Most forró a lap. Zárás 21:00-kor."* — vagy *„Mára kihűlt a lap. Legközelebb
kedden 11:00-tól."*

#### Miért pont ez

Egy street food hely iránti kereslet **időfüggő**, nem hangulatfüggő. A vendég nem
azt kérdezi, hogy „milyen a hely", hanem hogy **„most sütnek?"** — ez a hely
szolgáltatásának a lényege. Egy fotó ezt nem tudja megmutatni: egy fotó tegnap
készült, és mindig ugyanazt mondja. Egy nyitvatartás-táblázat sem: az adat, amit
a látogatónak fejben kell feldolgoznia („ma szerda van, most 17:31, a 11–21 azt
jelenti, hogy…").

A Parázs-sáv **elvégzi ezt a feldolgozást, és megmutatja az eredményt.** A vendég
nem olvas, hanem **lát** egy izzó vonalat és rajta egy jelölőt — vagy egy kihűlt,
sötét lemezt. Ugyanaz az ábra egyben a heti ritmust is megtanítja („vasárnap-hétfő
sötét"), amit különben minden vendégnek külön el kell magyarázni telefonon.

És — ez a döntő — **magát a szolgáltatást ábrázolja**: a lapsütőt, ami vagy forró,
vagy nem. Nem metafora egy másik iparágból, hanem a hely munkaeszköze.

#### Az egyetlen forrás elve

Ugyanaz a `NYIT` objektum táplálja a hőtérképet, a státuszmondatot **és az előrendelő
űrlap időellenőrzését**. Ha az étterem megváltoztatja a nyitvatartást, egyetlen
helyen kell átírni, és a három hely együtt mozdul. A mai nyitvatartási káosz (§2/K3)
pontosan abból lett, hogy több hely mondta ugyanazt, külön-külön.

#### Mibe kerül LCP-ben

**Nullába.** Az elem `<div>`-ekből és `linear-gradient`-ekből áll: nincs kép, nincs
SVG-fájl, nincs betöltendő erőforrás. A pozicionálást ~1,6 KB JS végzi (a teljes
scriptből), ami az elem megjelenése **után** fut — a lemez, a napcímkék és a sávok
váza már az első festéssel a helyükön vannak, mert a magasságuk CSS-ből fix.

Az LCP-jelölt a hero H1-e vagy a Parázs-sáv fémlemeze, attól függően, melyik nagyobb
a viewportban; **mindkettő tisztán HTML+CSS**, tehát az LCP gyakorlatilag egyenlő
az FCP-vel. Ez az a döntés, ami a §11 LCP-célját (≤1,2 s) egyáltalán elérhetővé
teszi: ha itt hero-fotó lenne, 200–400 KB-tal és egy hálózati körrel indulnánk.

**CLS-kockázat és kezelése:** a sávok magassága fix (14px / 38px a mai sor),
a rács `padding`-ja állandó, és a JS csak *befelé* tölti fel a konténert — a
konténer magassága nem változik a JS futásától. A percenkénti frissítés a
`tabular-nums` miatt szintén nem mozdít semmit. Mért CLS-hozzájárulás: **0**.

#### Mit áldozok érte

Ez az oldal egyetlen merész eleme. Mindenhol máshol a design szándékosan csendes:
fehér/sötét alap, egyetlen akcentszín, kicsi sugarak, semmi dísz, semmi gradiens
a szöveg mögött. **Egy helyre költöm a bátorságot** — ha két ilyen elem lenne,
egyik sem maradna meg.

---

## 8. Animációk és mikrointerakciók

Mozgás-tokenek: `--gyors 120ms` · `--alap 200ms` · `--lassu 320ms` ·
belépő görbe `cubic-bezier(.16,1,.3,1)` · kilépő `cubic-bezier(.4,0,1,1)`.
A kilépés mindig rövidebb, mint a belépés.

| Elem | Interakció | Tulajdonság | Időzítés / görbe | Mit közöl |
|---|---|---|---|---|
| Gomb (mind) | hover | `background`, `border-color` | 120ms `linear` | „kattintható" |
| Gomb | `:active` | — (**szándékosan semmi**) | 0 | Mobilon a transzform-visszajelzés a scrollal ütközik; a natív tap-highlight kikapcsolva, helyette a színváltás azonnali |
| Minden fókuszálható | `:focus-visible` | 3px `outline`, 3px offset | azonnali | Billentyűzetes pozíció. Soha nincs átmenet — a fókuszgyűrűnek azonnal ott kell lennie |
| Skip-link | `:focus` | `top: -100px → 0` | 200ms belépő | Előbukkan felülről, ahonnan jött |
| **Parázs-sáv, mai sor** | folyamatos | `filter: brightness(.94 → 1.12)` | **5s** `ease-in-out`, `alternate`, végtelen | A parázs lélegzik. Alig észrevehető; nem vonja el a figyelmet, de él |
| **Parázs-sáv, „most" jelölő** | percenként | `left` újraszámolás | ugrás, nincs átmenet | Az idő nem folyamatos animáció: percenként lép. Az átmenet itt hazugság lenne |
| Parázs-sáv, státusz | állapotváltás | `aria-live="polite"` szövegcsere | — | Csak **valódi változáskor** ír a live-régióba (különben percenként felolvasná) |
| GYIK-nyíl | `open` váltás | `rotate: 45deg → 225deg` | 200ms belépő | A tartalom iránya |
| Űrlapmező | `:focus` | `border-color` + 3px gyűrű | 120ms `linear` | Aktív mező |
| Űrlapmező hiba | `blur` után | megjelenés, nincs mozgás | azonnali | A hiba nem játék; a késleltetett animáció itt idegesítő |
| Hibaösszegző | beküldés | megjelenés + `focus()` | azonnali | A fókusz odalép; a görgetés a `scroll-behavior: smooth` miatt lágy |
| Sikerpanel | beküldés | űrlap `display:none` → panel + `focus()` | azonnali | Állapotváltás, nem díszítés |
| Fejléc | görgetés | `backdrop-filter: blur(10px)` | statikus | Nem animált — a görgetéshez kötött animáció a fő szálat terheli |
| Horgonyugrás | link | `scroll-behavior: smooth` | natív | Térbeli folytonosság |

**`prefers-reduced-motion: reduce` esetén:** minden `animation-duration` és
`transition-duration` 0,01ms-ra esik, a `scroll-behavior` `auto` lesz, a parázs
lélegzése leáll — **de a mai sor `filter: brightness(1.1)`-en marad**, tehát a
kiemelés információként megmarad. Ez a lényeg: a mozgáscsökkentés a mozgást veszi
el, nem az információt. Chromiumban ellenőrizve: `animationName: none`.

---

## 9. Frontend megvalósítás

### 9.1 Stack

**Statikus HTML + CSS + kevés vanilla JS, egy generátorral (Astro vagy Eleventy),
Cloudflare Pages / Netlify kiszolgálással.**

Indoklás:

- Négy oldal van, és havonta legfeljebb az étlap változik. Egy React/Next-alkalmazás
  futásidejű hidratálást és build-láncot hozna oda, ahol a teljes interaktivitás
  négy dolog: témaváltó, hőtérkép, harmonika, űrlap. Ezek együtt **9,5 KB JS**.
- A generátor **egy étlap-JSON-ból** rendereli a látható HTML-t és a `Menu` sémát
  is (§9.5). Ez az egyetlen valódi ok, amiért nem kézzel írt HTML: az étlap
  duplikációja garantáltan szétcsúszna.
- Cloudflare Pages: ingyenes szinten is CDN + automatikus Brotli + HTTP/3, és
  a `_headers` fájlból állítható a cache — pont az, ami a Webnode-on nincs.
- Az űrlap háttere lehet egy Cloudflare Worker vagy Netlify Function, ami SMS-t
  vagy e-mailt küld. Ez a rendszer egyetlen szerveroldali darabja.

**Elvetve:** WordPress (havi karbantartás, plugin-sebezhetőségek, és nincs, aki
frissítse); Next.js (túlméretezett); maradás a Webnode-on (§2 fele nem javítható
belőle).

### 9.2 Betűkezelés

- Mindkét család **önhosztolva**, `woff2-variations`, `latin + latin-ext` subsettel
  (`unicode-range: U+0000-024F, U+2000-206F`). Kb. **28 KB / család**.
- `font-display: swap` + `<link rel="preload">` **csak a két variable fájlra**.
  Több variánsra nem: a preload-túladagolás elveszi a sávot a kritikus CSS elől.
- Tartalék-lánc: `Sofia Sans Condensed → Archivo Narrow → Roboto Condensed →
  ui-sans-serif`, illetve `Instrument Sans → ui-sans-serif → system-ui`.
  A `font-synthesis-weight: none` megakadályozza, hogy a böngésző hamis félkövéret
  rajzoljon a tartalékból.
- Nincs Google Fonts CDN: egy külső domain plusz DNS + TLS + kapcsolat, és
  adatvédelmi szempontból is felesleges.

### 9.3 Képek

A prototípusban **szándékosan nincs kép** — nem azért, mert nem kell, hanem mert
nincs jogtiszta, jó minőségű fotóm az étteremről (§15/6). Az éles oldal képspecifikációja:

| Hely | Formátum | Méretek | Betöltés |
|---|---|---|---|
| Étlap-tételek | AVIF + WebP `<picture>` fallbackkel | `srcset` 320/480/720w, `sizes` a rácshoz | `loading="lazy"`, `decoding="async"` |
| `/rolunk/` fotósor | ugyanaz | 480/720/1080w | `lazy` |
| Bármely hajtás fölötti kép | ugyanaz | + `fetchpriority="high"` | **eager** |

Minden `<img>`-en kötelező `width` és `height` (vagy `aspect-ratio`) — enélkül a
lusta betöltés CLS-t termel. A `/rolunk/` galéria a §11 szerint sem befolyásolja
a főoldal LCP-jét, mert ott nincs kép.

**A főoldalra szándékosan nem kerül hero-fotó.** Alternatíva volt: nagy
burger-fotó a hero-ban. Elvetve, mert (a) 200–400 KB és egy hálózati kör az LCP
kritikus útján, (b) a rendelkezésre álló fotók minősége ismeretlen, (c) a
Parázs-sáv többet mond ugyanabban a helyben. Fotó a `/etlap/` és `/rolunk/`
oldalakra kerül, ahol elad.

### 9.4 Cache és szállítás

```
/f/*.woff2      Cache-Control: public, max-age=31536000, immutable
/assets/*       Cache-Control: public, max-age=31536000, immutable   (hash a névben)
/*.html         Cache-Control: public, max-age=0, must-revalidate
```

Brotli mindenre, HTTP/3, a kritikus CSS **inline** a `<head>`-ben (az egész
design system ~14 KB nyersen, ~4 KB Brotlival — ennyiért nem éri meg külön kérés).

### 9.5 Az étlap mint adat

```
data/etlap.json → { kategoriak: [ { nev, leiras, meretek, tetelek: [
                     { nev, osszetevok, arak[], forras, bizonyossag } ] } ] }
```

Ebből épül **egyszerre** a látható étlap-HTML és a `Menu` JSON-LD. A `forras` és a
`bizonyossag` mező nem dísz: amíg az ügyfél nem erősítette meg egy tételt, a
generátor kirakja mellé a jelölést, és **kihagyja a sémából** — hibás ár strukturált
adatban rosszabb, mint a hiányzó ár.

### 9.6 Az űrlap

- Natív HTML-mezők, `novalidate`, saját ellenőrzés — hogy a hibaszövegek magyarul
  és emberi nyelven szóljanak, ne a böngésző alapértelmezésével.
- **Ellenőrzés `blur`-on**, nem billentyűleütésenként; ha egy mező már hibás,
  onnantól `input`-ra is újraértékel (hogy a javítás azonnal látszódjon).
- Hibaüzenet **a mező alatt**, `aria-live="polite"` régióban, `aria-invalid="true"`
  a mezőn, `aria-describedby` összekötéssel.
- Beküldéskor **hibaösszegző** a lap tetején, `role="alert"`, minden hiba horgonyként
  a mezőjére mutat, és a fókusz az összegzőre lép.
- Az időpont a nyitvatartásból validál (§7.6, az egyetlen forrás elve), és mai napra
  legalább 20 perc előretartást kér.
- `autocomplete="name"` / `"tel"`, `inputmode="tel"`, `type="time" step="300"` —
  hogy a mobil a helyes billentyűzetet és görgetőt adja.
- Siker esetén panel `role="status"`, és **másodlagos kimenet**: „Inkább telefonálok".
  Egy űrlap sosem lehet zsákutca.
- Éles környezetben: `POST /api/elorendeles` + rate limit + honeypot mező +
  SMS-visszaigazolás. **Nincs CAPTCHA** — a forgalom mérete nem indokolja, és
  akadálymentességi költsége nagy.

---

## 10. SEO-specifikáció

### 10.1 Title és meta minta

| URL | `<title>` (≤60 karakter) | `<meta name="description">` |
|---|---|---|
| `/` | `Papa Giorgio Street Food – Pécs, Krisztina tér 10.` | Pizza 30 és 45 centiben, burger a lapsütőről, gyros és pljeskavica Pécs Kertvárosában. Elvitelre és kiszállítással. 06 70 254 3922. |
| `/etlap/` | `Étlap és árak – Papa Giorgio Street Food, Pécs` | A teljes étlap árakkal: pizza két méretben, burger, gyros, kebab, pljeskavica, saláta. Pécs, Krisztina tér 10. |
| `/rolunk/` | `Rólunk – Papa Giorgio Street Food, Pécs Kertváros` | Több generáció óta sütünk pizzát. Hogyan készül a tészta és mi történik a lapsütőn a Krisztina téren. |
| `/kapcsolat/` | `Kapcsolat és nyitvatartás – Papa Giorgio, Pécs` | Krisztina tér 10., 06 70 254 3922, kedd–szombat 11:00–21:00. Megközelítés, parkolás. Asztalt foglalni nem lehet. |

**Három konkrét változás a maihoz képest:** eltűnik a „Webnode" a címekből;
bekerül a **hely** (Pécs / Krisztina tér / Kertváros); és a márkanév mindenütt
**„Papa Giorgio Street Food"**, egyezésben a Google-cégprofillal és a foodorával (§2/K5).

### 10.2 Címsor-hierarchia

Oldalanként **pontosan egy `<h1>`**, szintugrás nélkül. A főoldalon:

```
h1  Pizza, burger, gyros — amíg forró a lap.
├ h2  A lap hőtérképe – mikor sütünk        (vizuálisan rejtett, a Parázs-sáv címe)
├ h2  Kemence, lap, nyárs.
│  ├ h3  A kemencéből   ├ h3  A lapról   ├ h3  A nyársról
├ h2  Az étlap gerince
├ h2  Asztalt nem, ételt igen
│  └ h3  Előrendelés elvitelre    └ h3  Megvan, felírtuk (sikerpanel)
├ h2  Hol vagyunk, mikor sütünk
│  ├ h3  7632 Pécs, Krisztina tér 10.   ├ h3  Kedd–szombat, 11:00–21:00
├ h2  Gyakori kérdések
└ h2  Papa Giorgio Street Food     (lábléc)
```

A GYIK nyitóelemei `<summary>`-k, nem címsorok: a `details/summary` natívan gomb,
és címsorként duplán jelenne meg a képernyőolvasó elemlistájában.

### 10.3 Strukturált adat — a teljes gráf

Egyetlen `@graph`, hét csomóponttal:

| Csomópont | Mit visz |
|---|---|
| `Organization` | márkanév, `sameAs`: Facebook, foodora, Falatozz |
| `Restaurant` | cím, telefon, `servesCuisine`, `priceRange`, `currenciesAccepted`, `openingHoursSpecification`, `hasMap`, **`acceptsReservations: "False"`**, `potentialAction`: `OrderAction` (foodora) + `ReserveAction` (előrendelés) |
| `Menu` + `MenuSection` + `MenuItem` + `Offer` / `AggregateOffer` | a teljes étlap; ársávnál `AggregateOffer` `lowPrice`/`highPrice`-szal |
| `WebSite` | a webhely mint entitás |
| `WebPage` | `about` → `Restaurant`, `isPartOf` → `WebSite` |
| `BreadcrumbList` | morzsa |
| `FAQPage` | az 5 GYIK-kérdés, szó szerint egyezően a látható szöveggel |

**Amit szándékosan kihagytam, és miért:**

- **`aggregateRating` — kihagyva.** A Google irányelve tiltja, hogy egy vállalkozás
  a saját oldalán jelölje meg a magáról szóló, harmadik féltől (Google-profilból)
  átvett értékelést. A 4,9★ így **a látható tartalomban** szerepel, forrásmegjelöléssel
  — a sémában nem. Ha az ügyfél saját, ellenőrizhető véleménygyűjtést indít, ez
  visszakerülhet.
- **`geo` (koordináták) — kihagyva.** Nincs dokumentált szélesség/hosszúság; kitalálni
  nem lehet. A Google Cégprofilból pontosan kimásolható, akkor kerül be (§15/7).
- **`image` — kihagyva.** Nincs jogtiszta kép. Séma nélküli kép jobb, mint hibás
  URL a sémában.

### 10.4 Local SEO

1. **A domainkérdés lezárása** (§2/K1): egy kanonikus domain, a másik oldalanként
   301-gyel oda. Ez az egyetlen legnagyobb hatású SEO-lépés a listán.
2. **Google Cégprofil = az igazság forrása.** A nyitvatartás, a telefonszám és a
   kategória a profilban és az oldalon **karakterre egyezzen**. A mai eltérés
   (20:30 vs 21:00) mindkettőt gyengíti.
3. **NAP-konzisztencia** (Name–Address–Phone) végig: „Papa Giorgio Street Food”,
   „7632 Pécs, Krisztina tér 10.”, „+36 70 254 3922” — ugyanabban az alakban a
   weboldalon, a cégprofilban, a foodorán, a Falatozzon, a Facebookon és a
   katalógusokban (nyitva.hu, firmania, cylex).
4. **A második telefonszám tisztázása** (§15/2): ha nem élő, kivezetni a katalógusokból.
5. **Kategória:** a cégprofilban a fő kategória legyen az, ami a keresletet viszi.
   Ha a „pizzéria” hoz több keresést Pécsett, akkor az — de akkor a weboldal
   szövegének is ezt kell erősítenie (ma épp ellentmondanak, §2/U1).
6. **A `/kapcsolat/` a helyi horgonyoldal:** cím, térkép, megközelítés, parkolás,
   nyitvatartás — ez az az oldal, amire a helyi találatok mutatnak.

### 10.5 Technikai SEO

`sitemap.xml` (4 URL) · `robots.txt` a sitemap-hivatkozással · minden oldalon
önmagára mutató `<link rel="canonical">` · `hreflang` nem kell (egynyelvű) ·
`og:` és `twitter:` metaadatok · `max-image-preview:large` ·
`404` oldal, ami a `/etlap/`-ra és a telefonszámra mutat.

---

## 11. Performance-célok

Abszolút célok, nem az elődhöz mért javulás. Mérés: Lighthouse mobil (Moto G4
profil, 4× CPU-lassítás, „Slow 4G”), és mezei CrUX-adat 28 nap után.

| Metrika | Cél | Hogyan tartható |
|---|---|---|
| **LCP** | **≤ 1,2 s** (jó: 2,5 s) | Az LCP-elem a H1 vagy a Parázs-sáv fémlemeze — mindkettő tisztán HTML+CSS. Nincs hero-kép, nincs blokkoló erőforrás. Kritikus CSS inline. |
| **CLS** | **≤ 0,02** (jó: 0,1) | Minden képen `width`/`height`; a Parázs-sáv magassága CSS-ből fix, a JS csak befelé tölt; `font-display: swap` + méretillesztett tartalék; `tabular-nums` az óránál. |
| **INP** | **≤ 100 ms** (jó: 200 ms) | Nincs framework-hidratálás. A legdrágább kezelő a hőtérkép újrarajzolása: 7 sor DOM-építés, <2 ms. A percenkénti frissítés `setInterval`, nem `rAF`. |
| **FCP** | ≤ 0,9 s | Egyetlen HTML-kérés, inline CSS, betűk `swap`-pal, nem blokkolnak. |
| **TBT** | ≤ 50 ms | 9,5 KB JS, egyetlen szinkron blokk a végén, `defer` nem is kell. |

**Bájtköltségvetés — főoldal, első látogatás (Brotli után):**

| Erőforrás | Cél |
|---|---|
| HTML + inline kritikus CSS | ≤ 16 KB |
| JS | ≤ 4 KB (9,5 KB nyersen) |
| Betűk (2 × variable woff2, latin+latin-ext) | ≤ 60 KB |
| Képek a főoldalon | **0 KB** |
| **Összesen** | **≤ 80 KB** |

Ismételt látogatás: ≤ 16 KB (a betűk és az assetek `immutable` cache-ből).

**Költségvetés-őr:** a build lépésben egy `bundlesize`-szerű ellenőrzés, ami
megbukik, ha a főoldal átlépi a 80 KB-ot. Enélkül a költségvetés fél éven belül
elolvad.

---

## 12. CRO — konverziós elemek, és hogy miért működnek

Az elsődleges konverzió: **rendelés indítása**. Három mérhető esemény:
`tel:` kattintás · előrendelő űrlap beküldése · platform-kimenő kattintás.

| # | Elem | Hol | Miért működik |
|---|---|---|---|
| 1 | **Telefonszám mint elsődleges gomb a fejlécben** | Minden oldal, minden görgetési pozíció | A célközönség (a) és (c) szegmense telefonál. A szám kiírva, nem „Hívjon minket!" — a látható szám önmagában bizalmi jel, és a gombot koppintani lehet. |
| 2 | **Rögzített alsó akciósáv mobilon** | `<840px`, mindig | A döntés a görgetés bármely pontján megszülethet. Fitts törvénye: a hüvelykujj-zóna a képernyő alja; a fejléc a legrosszabb hely egy 6,7"-os telefonon. |
| 3 | **Parázs-sáv** | Hajtás fölött | Eltávolítja a legnagyobb súrlódást: „hiába hívom, biztos zárva". Aki látja, hogy izzik a lap, hív. Aki látja, hogy hideg, nem csalódik — és visszajön. |
| 4 | **Bizonyítéksor a hero alatt** | Hajtás fölött/alatt | 4,9★ / 190 vélemény: társas bizonyíték. Az ársáv: **kizárja azt, akinek drága, és megnyugtatja azt, akinek nem** — a kizárás is konverzió, mert megspórol egy csalódott telefonhívást. |
| 5 | **„Szabadtéri asztalok · foglalás nincs" ugyanabban a sorban** | Hajtás fölött | Elvárás-beállítás a legelején. Ez a mondat telefonhívásokat és rossz értékeléseket előz meg. |
| 6 | **Árak a főoldalon** | Középen | Az ár az egyetlen ok, amiért a látogató átmegy a foodorára (§2/U2). Ha itt megkapja, itt is rendel — jutalék nélkül. |
| 7 | **Előrendelő űrlap az elvitelre** | Középen | Nyit egy **jutalékmentes** csatornát azoknak, akik nem szeretnek telefonálni (fiatalabb szegmens), de nem akarnak platformdíjat sem fizetni. |
| 8 | **Az űrlap időmezője a nyitvatartásból validál** | Űrlap | Megelőzi a leggyakoribb hibás beküldést (zárás utáni időpont). Egy hibás előrendelés két telefonhívásba kerül. |
| 9 | **A sikerpanel másodlagos kimenete: „Inkább telefonálok"** | Beküldés után | A bizonytalan felhasználó azonnal átléphet a biztosabb csatornára. Zsákutca nélküli folyamat. |
| 10 | **GYIK a lap alján** | Alul | A görgetés végéig eljutó látogató a legelszántabb, és neki még van egy kérdése. Ugyanez a szöveg `FAQPage`-ként a találatban is dolgozik. |
| 11 | **A CTA-hierarchia egyértelmű** | Mindenütt | Egy elsődleges gomb szekciónként (`primary-action`). Három egyenrangú gomb = nulla döntés. |

**Amit nem teszek bele:** felugró ablak, visszaszámláló, „még 3 adag maradt”,
hírlevél-modál, chatbot. Egy street food helynél ezek hitelrontóak: a vendég 30
másodpercet szán az oldalra, és bármelyik felugró elem ezt a 30 másodpercet
használja el.

---

## 13. Design-döntések összefoglalója

| # | Döntés | Alternatíva, amit mérlegeltem | Miért nem azt választottam |
|---|---|---|---|
| D1 | Vizuális kiindulópont: **a lapsütő** (grafit fém + parázs + zsírpapír) | Olasz vonal (a „Giorgio" névből): terrakotta, bazsalikom, tricolore | A név megtévesztő: a kínálat fele balkáni–amerikai street food. Az olasz vizuális kód hazudna a helyről, és beleolvasztaná abba a pizzéria-mezőnybe, amiből ki kellene tűnni. |
| D2 | Alap: **hűvös papír** `#F4F3F1` világosban, meleg grafit sötétben | Bézs/kraft alap (a csomagolópapír színe) | A brief kifejezetten kizárta a bézs oldalt — jogosan: a bézs alap a parazsat is tompítja. A hűvös papír melegebbnek mutatja a `--parazs`-t. |
| D3 | **Három hueból álló paletta** (parázs + mustár + olíva) neutrálisokkal | Fekete háttér + egyetlen neon accent | Ez az AI-alapértelmezés, amit a brief tilt. Egy szín önmagában nem tud állapotot jelölni; három hue kell ahhoz, hogy a „forró / hideg / semleges" hármas színnel is olvasható legyen. |
| D4 | Betűk: **Sofia Sans Condensed + Instrument Sans** | Playfair + Inter (tiltva) · Barlow Condensed + Barlow (a skill első ajánlása) · Archivo · Space Grotesk | Lásd §7.2. Röviden: kondenzált groteszk = árcédula-betű; a Sofia Sans egyetlen családdal viszi a teljes display-skálát, teljes latin-ext-tel. |
| D5 | Szignatúra: **Parázs-sáv** (nyitvatartás-hőtérkép) | Nagy burger-fotó a heróban · animált „sercegő lap" háttérvideó · pizza-konfigurátor | A fotó nem *mutat* semmit a szolgáltatásból, csak illusztrál, és 200–400 KB-tal terheli az LCP-t. A videó ugyanez, rosszabbul. A konfigurátor drága, és a rendelés úgyis platformon zajlik. A hőtérkép **információt ad**, nulla hálózati költséggel. |
| D6 | A Parázs-sáv **mindkét témában sötét** | Témakövető színezés | Egy tárgyat ábrázol. A lapsütő nem lesz világos attól, hogy világos témát választasz. |
| D7 | **Nincs hero-kép** | Klasszikus étel-hero | §9.3 és §11: az LCP-cél másképp nem tartható, és nincs jogtiszta fotóm. |
| D8 | **Nincs hamburgermenü mobilon** — háromfelé osztott navisáv | Hamburger + off-canvas panel | Három úti cél van. A hamburger elrejtene mindent, hogy 40px-t nyerjen, és egy koppintást tesz minden navigáció elé. |
| D9 | **Nincs saját rendelési motor** — útválasztás platformokra + telefon/előrendelés | Kosaras rendszer online fizetéssel | §4.3: a foodora már megoldotta, futárral együtt. Az előrendelő űrlap viszont megnyit egy **jutalékmentes** csatornát a helyben elvitelre — ez a valódi nyereség. |
| D10 | **`aggregateRating` a látható szövegben, nem a sémában** | Séma a 4,9-cel (gazdagabb találat) | Irányelvsértés, és manuális büntetést kockáztat. §10.3. |
| D11 | **Az árak a főoldalon is** | Csak az étlapoldalon | Az ár a legnagyobb kilépési ok. Ha csak egy kattintással érhető el, a látogató a foodorán nézi meg — és ott is rendel. |
| D12 | **`/fotogaleria/` 301 → `/rolunk/`** | Galéria megtartása külön oldalként | A fotó a tétel mellett elad, külön oldalon zsákutca (§2/U4). De **nem törlöm** — a képek átkerülnek, a linkerő is. |
| D13 | **Statikus generátor** (Astro/Eleventy) | Maradás a Webnode-on · WordPress · Next.js | §9.1. A Webnode-ból a §2 fele nem javítható; a WordPress-t nincs, aki karbantartsa; a Next.js-t nem indokolja négy oldal. |
| D14 | **Kicsi sugarak (3/6/12px), blokkos rács** | Nagy, lekerekített „app-kártyás" megjelenés | A menütábla és a csomagolópapír vizuális kódja szögletes. A 24px-es sugarak SaaS-t idéznek. |
| D15 | **Egyetlen nyitvatartás-forrás** JS-objektumban | Külön adat a hőtérképnek, a táblázatnak és a validációnak | A mai nyitvatartási káosz (§2/K3) pontosan a többforrásúságból jött. |

---

## 14. Bevezetési ütemterv

| Fázis | Tartalom | Feltétel / kimenet |
|---|---|---|
| **F0 · Mérés és tisztázás** | Az élő oldal lekérése és mérése (Lighthouse, HTML-forrás, meglévő séma). A §15 kérdéslistájának kitöltése az ügyféllel. A `papagiorgio.hu` tartalmának megnézése. | Nélküle a §2 performance-blokkja feltételezés marad, és az étlapadat sem élesíthető. |
| **F1 · Domainrendezés** *(azonnal, a redesigntól függetlenül)* | Egy kanonikus domain kijelölése, a másik **oldalanként** 301-gyel. Google Cégprofil és minden katalógus NAP-adatának összehangolása. A nyitvatartási ellentmondás feloldása. | A legnagyobb hatás/ráfordítás arányú lépés. Ma is elvégezhető, a régi oldalon. |
| **F2 · Étlapadat** | `etlap.json` felépítése az étterem valódi étlapjából, tételenként, árral, `forras` és `bizonyossag` mezőkkel. | Ez a legnagyobb kézi munka, és ez blokkolja az `/etlap/` oldalt. |
| **F3 · Főoldal + `/kapcsolat/`** | A prototípus alapján, a valódi nyitvatartással. Analitika-események: `tel:` kattintás, űrlapbeküldés, platform-kimenő. | Élesíthető az étlapoldal nélkül is, ha az `/etlap/` egyelőre a régire mutat. |
| **F4 · `/etlap/` + `/rolunk/`** | Étlapoldal az F2 adatából, `Menu` sémával. Rólunk-oldal a meglévő szöveg átdolgozásával, a beolvasztott galériával. Fotózás. | Fotó nélkül a `/rolunk/` fele üres. |
| **F5 · Előrendelés élesítése** | Backend-végpont, SMS/e-mail értesítés, rate limit, honeypot, adatkezelési tájékoztató. | Jogi tartalom nélkül nem élesíthető. |
| **F6 · Mérés és igazítás** | 28 nap CrUX, konverziós arányok csatornánként, a GYIK bővítése a beérkező kérdésekből. | — |

F1 önmagában is értéket termel, és nem függ a redesigntól — érdemes **most** elkezdeni.

---

## 15. Nyitott kérdések — ehhez kell ügyfél-input

Sorrendben, a legfontosabbtól. Amíg az 1., 3. és 4. nincs meg, az oldal **nem
élesíthető**.

1. **Mi a pontos nyitvatartás?** A Google-profil „zárás 20:30”-at mutat, a rendelési
   platformok 11:00–21:00-t, kedd–szombat. Ez az egész oldal legkockázatosabb adata:
   ebből él a Parázs-sáv, a nyitvatartás-táblázat, az űrlap validációja és az
   `openingHoursSpecification` séma. Van-e eltérő nyári/téli, ünnepnapi rend?
2. **Melyik a jó telefonszám?** A 06 70 254 3922 mindenütt szerepel; egy katalógusban
   feltűnik a +36 70 522 6460 is. Élő ez? Ha nem, ki kell vezetni a katalógusokból.
3. **A `papagiorgio.hu` a tiétek?** Ha igen: melyik legyen a kanonikus domain, és mi
   van rajta ma? Ha nem: az egy másik vállalkozás, és akkor a márkanév ütközik.
4. **A teljes étlap, tételenként, árral.** Fotó vagy PDF az étlapról elég. A jelenlegi
   árak indexelt aggregátor-tartalomból származnak, és lehet, hogy elavultak. A
   30/45 cm-es pizzáknál minden tétel mindkét ára kell.
5. **Vannak-e menük, kombinációk, akciók?** (Ebédmenü, napi ajánlat, diákár.)
   Ma egyetlen „menü” tételről tudok (kebabburger 2 900 Ft), de valószínűleg több van.
6. **Fotók.** Van-e jogtiszta, jó minőségű fotó az ételekről, a helyről, a
   lapsütőről? Ha nincs, a `/rolunk/` és az `/etlap/` fotózást igényel — ez a §14/F4
   fázis blokkolója.
7. **A pontos koordináták** a Google Cégprofilból (a `geo` sémamezőhöz).
8. **Kiszállítás:** csak platformon keresztül, vagy saját futár is? Ha saját: milyen
   területre, mekkora díjjal, mennyi a minimum rendelés? (Ma ezek placeholderek.)
9. **Parkolás és megközelítés** a Krisztina téren. Ez a `/kapcsolat/` oldal
   leghasznosabb mezője, és ma nem tudom.
10. **Cégadatok** a lábléchez és az adatkezelési tájékoztatóhoz: cégnév, székhely,
    adószám, e-mail, adatkezelő.
11. **Az előrendelés fogadása:** hova menjen? SMS, e-mail, vagy a konyhai nyomtatóra?
    Ki nézi, és milyen gyakran? Egy előrendelés, amit senki nem olvas, rosszabb, mint
    a semmi.
12. **A hely önmeghatározása:** pizzéria vagy street food? A cégnév az utóbbit mondja,
    a jelenlegi `/kapcsolat/` szöveg az előbbit. Ez eldönti a Google-kategóriát, a
    title-öket és a szövegek hangját (§2/U1).
13. **Vegetáriánus / allergén információ.** Van-e húsmentes opció? Az allergéninfó
    jogi kötelezettség is.
14. **Van-e e-mail cím?** Egyetlen forrásban sem találtam.

**A prototípusban `[szögletes zárójellel]` jelölt helyek:** gyros / pljeskavica /
csirke box ára, parkolás és megközelítés, cégnév és adószám. Ezek mind a fenti
listából jönnek. **Egyetlen számot sem találtam ki.**

---

## 16. Mi ennek az anyagnak a leggyengébb pontja — őszintén

**Az, hogy a jelenlegi oldalt nem láttam.**

A §1 és a §2 az indexelt címkékből, a keresők kivonataiból és a Webnode-platform
ismeretéből épül. Ez a *diagnózis irányát* tekintve szinte biztosan helyes — a
title-minták, a hiányzó nyitvatartás és a két domain kemény, indexből olvasható tények.
De **a részletei tévedhetnek**: lehet, hogy az oldalon van olyan, ami nem indexelődött
(egy jó szöveg, egy működő elem), és amit így elvesztek. A §1.2 „mi a jó benne”
listája ezért a legsérülékenyebb rész az egész anyagban — pont az, aminek a
legpontosabbnak kellene lennie, ha az a cél, hogy ne dobjunk el működő megoldást.

**A második leggyengébb pont: az árak.** Aggregátorok indexelt étlapjából származnak,
2026 szeptemberi állapotban, és nem az étterem erősítette meg őket. A prototípusban
látható, jelölt figyelmeztetés kíséri őket, és a sémából a bizonytalan tételek
kimaradnak — de ha az ügyfél ránéz és „kész oldalnak” látja, ezek az árak élesbe
mehetnek rossz értékkel. Ez a legvalószínűbb módja annak, hogy ez az anyag kárt okozzon.

**A harmadik: a Parázs-sáv egyetlen adaton áll, ami ellentmondásos.** A legerősebb
és legjobban megjegyezhető elem pontosan arra a §15/1. kérdésre épül, amire ma nincs
biztos válasz. Ha a nyitvatartás rossz, az elem nemcsak haszontalan, hanem aktívan
félrevezető — és pont azért, mert olyan magabiztosan mutatja. Ezért van benne a
prototípusban a látható „ELLENŐRIZENDŐ ADAT” jelvény: nem dísz, hanem biztosíték
az ellen, hogy valaki ellenőrzés nélkül élesítse.

**Amit nem tekintek gyengeségnek, de tudni kell róla:** az `/etlap/`, a `/rolunk/`
és a `/kapcsolat/` oldalról csak szekciótábla és indoklás készült, prototípus nem —
a brief egy oldal működő prototípusát kérte. A design system minden komponense
megvan hozzájuk; a három oldal megépítése kivitelezés, nem tervezés.
