# La' Belle orvos-esztétikai klinika, Szekszárd — UI/UX redesign koncepció és prototípus

> **Módszertani figyelmeztetés — rekonstrukcióból dolgoztam.**
> A klinika Google Cégprofilja jelez „Webhely" gombot, de a hálózati egress ebben a
> munkakörnyezetben blokkolja a facebook.com, a szepsegturul.eu és az egeszsegturul.eu
> domaineket, a webhely URL-jét pedig egyik indexelt forrás sem adta vissza.
> **Az éles oldal HTML-jét nem láttam.** Az 1. fejezet ezért nem „a jelenlegi weboldal
> kódelemzése", hanem **a jelenlegi digitális jelenlét elemzése** az alábbi forrásokból:
>
> | # | Forrás | Mit igazol |
> |---|--------|-----------|
> | F1 | Instagram-profil képernyőkép, `@labelle_orvosesztetika`, 2026-09-04 | bio, 516 bejegyzés, 1499 követő, 184 követés, kiemelt storyk címei |
> | F2 | Instagram-rács képernyőkép (2. oldal) | 18 poszt tartalma: kezelések, akciók, szabadságközlemények |
> | F3 | Klinika belső fotó | anyaghasználat: márvány, kefélt acél, körlámpa, szürke velúr |
> | F4 | Google Cégprofil kivonat | 5,0 ★ / 52 értékelés, „Kozmetikai vállalat", zárás 16:00, 06 30 719 1991 |
> | F5 | Indexelt találatok (Facebook-poszt címek, katalógusok) | „Dr. Imre Laura fogorvos, szájsebész, esztétikai orvos"; e-mail; „orvos-esztétika, orvosi kozmetika, sminktetoválás" |
>
> Minden **[szögletes zárójeles]** érték a dokumentumban és a prototípusban
> **placeholder**: nincs róla dokumentált adatom. Nem találtam ki számot. A kitöltendő
> listát a **15. fejezet** tartalmazza.

---

## 0. Kontextus — amit tudok, és amit nem

### 0.1 A brief kitöltése a dokumentált tényekből

| Brief-mező | Kitöltve | Forrás / státusz |
|---|---|---|
| **Ügyfél** | La' Belle orvos-esztétikai klinika, Szekszárd, Csalogány u. 2, 7100. Tulajdonos-kezelőorvos: **Dr. Imre Laura**, fogorvos, szájsebész, esztétikai orvos. Önmeghatározás: „Tolna vármegye első orvos-esztétikai klinikája." | F1, F5 |
| **Piac és verseny** | Tolna vármegyében nincs második orvos-esztétikai klinika (saját állítás, F1). A valós versenytárs nem helyi: **Pécs és Budapest** klinikái (50–140 km), illetve a **helyi kozmetikusok**, akik orvosi képesítés nélkül adnak hasonló hangzású kezeléseket. → Lásd 0.3. | részben rekonstruált |
| **Célközönség** | Lásd 0.2. Rekonstrukció az IG-tartalomból, nem ügyféladat. | rekonstruált |
| **Az oldal EGY dolga** | **Időpontkérés** — a DM-ből webes űrlapba terelni. Indoklás: 0.4. | levezetett |
| **Amit tudok és nincs az oldalon** | Dr. Imre Laura hármas képesítése; 5,0 ★ / 52 értékelés; „vármegye első" pozíció; a két külön telefonszám (esztétika / fogászat); a klinika saját tere | F1, F4, F5, F2 |
| **Amit NEM szabad megváltoztatni** | **A brief ezt üresen hagyta.** Feltételezésem: a `La' Belle` névalak, az `LB` monogram-logó és a `labelle_orvosesztetika` kézjegy marad. Ezt a 15. fejezetben visszakérdezem. | **NYITOTT** |

### 0.2 Célközönség — rekonstrukció, nem kutatás

Az IG-tartalom három elkülönülő csoportot rajzol ki (F1, F2):

| Csoport | Jel a tartalomban | Milyen lelkiállapotban érkezik |
|---|---|---|
| **A. Első injektálás előtt álló nő, kb. 25–40** | ajak-posztok, „Lips" kiemelt story, Teoxane Baby Glow | **Szégyenkezve és félve.** Két félelme van: „fáj-e" és „meg fog látszani, hogy csináltattam". Nem árat keres először, hanem engedélyt. |
| **B. Visszatérő bőrkezelés-vásárló, kb. 30–55** | carbon peeling, Hydra Beauty, CALECIM, ZO Skin Health | **Kalkulálva.** Sorozatban gondolkodik, ár-érték arányt néz, terméknevet keres a Google-ben. |
| **C. Férfi, kb. 30–50** | hajvonal előtte/utána poszt, PRP-vérvételes poszt, arckezelés férfi pácienssel | **Diszkréten.** Nem akar „szépészetibe" járni. Az „orvosi", „klinika", „szájsebész" szavak neki nyitnak ajtót, a „szépülj" szó bezárja. |

**Ez a három csoport három különböző első mondatot igényel** — a főoldal felépítése (5. fejezet) ezért nem egy hosszú „rólunk", hanem egy háromfelé ágazó belépő.

### 0.3 A verseny — mitől néznek ki mind egyformán

Az orvos-esztétikai szegmens magyar weboldalai egy jól felismerhető sablont követnek:
rózsaszín-arany vagy türkiz-fehér paletta, Playfair/Cormorant fejlécek, stock-fotó
modell hunyt szemmel, „Fedezd fel a benned rejlő szépséget" típusú vezérszöveg,
kezeléslista árak nélkül, űrlap „Kérjen visszahívást" gombbal.

**Ez a sablon pont azt mossa el, ami a La' Belle egyetlen védhető előnye: hogy itt orvos
kezel.** Egy kozmetikus és egy szájsebész weboldala ma megkülönböztethetetlen. Ez a
redesign kiindulópontja — nem a szépítés, hanem a **differenciálás visszaállítása**.

### 0.4 Miért az időpontkérés az oldal EGY dolga

Ma a foglalás útja a bio szerint: hívás `0630 719 1991`, vagy Instagram-DM
(„esztétikai időpont miatt üzenetben keressetek" — F2). Mindkettő szinkron csatorna.
A dokumentált szabadságközlemények (`08.10–21.`, `2026.07.29–08.03.` — F2) azt mutatják,
hogy az elérhetőség szakaszos, a kereslet viszont nem az.

Egy webes időpontkérő űrlap az egyetlen elem, ami **aszinkron** — éjjel 11-kor, munka
közben, szabadság alatt is fogad érdeklődést. Minden más oldalelem ennek az űrlapnak
a bizalmi előkészítése.

---

## 1. A jelenlegi állapot elemzése

### 1.1 „Technológia és struktúra"

A jelenlegi jelenlét gyakorlatilag **három third-party profil**, saját domain-tartalom nélkül:

| Csatorna | Szerep ma | Kontroll |
|---|---|---|
| Instagram `@labelle_orvosesztetika` | **fő tartalomtár** — 516 poszt, kezelésbemutatás, árak, akciók, elérhetőség | nulla (algoritmus, formátum, indexelés) |
| Facebook-oldal | duplikátum + megosztásfelület | nulla |
| Google Cégprofil | **fő belépő** — 5,0 ★ / 52 értékelés, térkép, hívás gomb | részleges |
| „Webhely" (URL ismeretlen) | ismeretlen tartalom | ismeretlen |

**Az információs architektúra ma nem az oldalon van, hanem a kiemelt storykban.**
Ez öt „menüpont" (F1): `2025 árak` · `Szolgáltatások` · `Szőrtelenítés` · `Lips` ·
`ZO Skin Health`. Ez fontos: **ezt a felhasználók keresletéhez igazította valaki.**
Nem eldobni kell, hanem sitemappé emelni (4. fejezet).

### 1.2 MI A JÓ BENNE — külön szedve, megtartandó

Ezeket **nem** dobom el, mert működnek:

| # | Ami jó | Miért jó | Mi lesz vele |
|---|---|---|---|
| J1 | **„Tolna vármegye első orvos-esztétikai klinikája"** | Egy mondatban ad kategóriát, területet és elsőbbséget. Ellenőrizhető, nem marketingvatta. | **Szó szerint marad**, a H1 alá emelve. |
| J2 | **Dr. Imre Laura arca és neve a tartalomban** | Az orvos-esztétikában a bizalom személyhez kötődik, nem márkához. 516 posztban ott van. | Külön `/dr-imre-laura/` oldal + a főoldalon név és képesítés a hajtás felett. |
| J3 | **Valódi előtte/utána anyagok** (hajvonal, ajak, dekoltázs — F2) | Ez a szakma egyetlen hiteles bizonyítéka. | Marad, de **jogi és GDPR-keretbe téve** (10.5). |
| J4 | **5,0 ★ / 52 értékelés** (F4) | 52 értékelés egy 30 ezres városban erős minta. | Számként a hajtás felett, `AggregateRating` schemával. |
| J5 | **A kiemelt storyk mint IA** | A felhasználók keresletéből nőtt ki: ár, szolgáltatás, szőrtelenítés, ajak, termék. | 1:1 megfeleltetés a sitemapben (4.2). |
| J6 | **Két külön telefonszám** (esztétika `0630 719 1991` / fogászat `0674 512 222` — F2) | Operatív valóság, nem hiba. A páciens ma is eltéved köztük. | Explicit, címkézett kettős kontaktblokk. |
| J7 | **Szabadságközlemények** | Őszinte elérhetőség-kommunikáció. Ritka és bizalomépítő. | Egy `Elérhetőség` sáv az oldalon, egy szerkeszthető mezőből. |
| J8 | **A klinika saját tere** (F3): hideg szürke márvány, kefélt acél, fehér falak, **körlámpa**, meleg szürke velúr | Már ma is konzisztens, drága és nem rózsaszín. | **Ez lesz a vizuális kiindulópont** (7.0). |
| J9 | **Konkrét márkanevek** a tartalomban: Teoxane, ZO Skin Health, CALECIM | Ezekre valós keresés fut. Márkakeresés = magas vásárlási szándék. | Külön aloldalak, a márkanév a `<title>`-ben. |

### 1.3 Ami hiányzik a rendszerből (nem hiba, hanem üres hely)

- Nincs indexelhető szöveg a kezelésekről. Az Instagram-poszt képére írt szöveg a
  Google számára nem létezik.
- Nincs ár semmilyen kereshető formában. A `2025 árak` egy **story-kiemelés**, azaz
  képsorozat: nem másolható, nem kereshető, nem linkelhető, és a neve évszámot tartalmaz,
  tehát 2026-ban már önmagát cáfolja.
- Nincs kiírt nyitvatartás a Google-ön kívül.
- Nincs egyetlen olyan felület sem, ahol a páciens **kérdés nélkül** végigmehetne a
  döntésen: *mi ez → nekem jó-e → mi történik → mennyi idő a regenerálódás → mennyibe
  kerül → mikor mehetek*.

---

## 2. Problémalista bizonyítékkal

### 2.1 Kritikus (bevételt közvetlenül visz el)

| # | Probléma | Bizonyíték | Hatás |
|---|---|---|---|
| K1 | **A foglalás mindkét útja szinkron.** Csak telefon vagy DM. | F1 bio: `0630/7191991`; F2: „esztétikai időpont miatt üzenetben keressetek" | A munkaidőn kívüli és a „még csak nézelődöm" fázisú érdeklődő elveszik. Ez az orvos-esztétikában a forgalom nagyobbik fele: a döntés estére és hétvégére esik. |
| K2 | **Az árinformáció képbe van zárva, és lejárt évszámot visel.** | F1: `2025 árak` kiemelt story | 2026-ban a legelső bizalmi jelzés az, hogy az árlista elavult. Az árkérdés a DM-be tolódik, ami az orvos idejét viszi. |
| K3 | **A legerősebb bizalmi eszköz sehol nem szerepel kereshető szövegben:** hogy a kezelőorvos **fogorvos és szájsebész**. | F5 (Facebook-poszt címe), F1 bio (nem tartalmazza) | Az arc alsó harmadának anatómiája — ajak, áll, nasolabialis — szájsebészi kompetencia. Ez az egyetlen érv, amit egy kozmetikus nem tud lemásolni, és éppen ez hiányzik. |
| K4 | **Nincs saját domain-tartalom a pénzt hozó keresésekre.** | „orvos esztétika Szekszárd", „ajakfeltöltés Szekszárd", „lézeres szőrtelenítés Szekszárd" — egyik találati listában sem jött vissza La' Belle-oldal | A vásárlási szándékú keresés versenytárshoz vagy pécsi/budapesti klinikához megy. |
| K5 | **A platformkockázat 100%.** 516 poszt és 1499 követő olyan felületen, amit nem a klinika birtokol. | F1 | Egy fiókzárolás nullázza a teljes marketingvagyont. |

### 2.2 UX

| # | Probléma | Bizonyíték | Hatás |
|---|---|---|---|
| U1 | **Nincs lineáris döntési út.** A rács idővonal szerint rendez, nem szándék szerint. | F1, F2 rácsnézet | A B-csoport (kalkuláló) nem tud összehasonlítani, a C-csoport (férfi) nem talál magának szánt tartalmat. |
| U2 | **A szöveg képen van.** Akció, szabadság, árak mind grafikaként. | F2: „ÓRIÁSI ZO SKIN HEALTH KOZMETIKUM AKCIÓ" képposzt | Képernyőolvasóval néma, nem másolható, nem fordítható, nem kereshető, mobil zoomon töredezik. |
| U3 | **A nyitvatartás nincs kiírva.** Csak a Google „Zárás: 16:00" sora. | F4 | „Ma még odaérek?" — megválaszolatlan kérdés a hívás előtt. |
| U4 | **Az elérhetőség szakaszos, de nem előrejelezhető.** Két különböző szabadságposzt. | F2 | A páciens nem tudja, érdemes-e most írni. |
| U5 | **A két telefonszám összekeveredik.** | F2: „fogászati időpont miatt: 0674 512 222 / esztétikai időpont miatt üzenetben" | Rossz számra futó hívás mindkét rendelést terheli. |
| U6 | **A „modell" hívások és a „betelt" válaszok ugyanabban a folyamban vannak, mint a szolgáltatás.** | F2: „Már nincs hely modellkedésre, betelt." | Az árérzékeny érdeklődőt olyan ajánlat vonzza be, ami rendszerint már nem elérhető. |

### 2.3 SEO

| # | Probléma | Bizonyíték |
|---|---|---|
| S1 | Nincs `MedicalClinic` / `LocalBusiness` strukturált adat saját domainen. | keresési találatokban nem jelenik meg rich result |
| S2 | Nincs kezelésenkénti landing URL, így nincs mire rangsorolni. | 4 különböző lekérdezés, nulla saját találat |
| S3 | A kategorizálás a Google Cégprofilban **„Kozmetikai vállalat"** (F4) — nem `Medical clinic` / `Skin care clinic`. | F4 | Ez a besorolás **maga a pozicionálási hiba, adatszinten**: a klinikát a kozmetikusok közé sorolja a helyi találatokban. |
| S4 | Márkakeresések (`ZO Skin Health Szekszárd`, `Teoxane Szekszárd`, `CALECIM`) kihasználatlanok. | F1, F2 |
| S5 | Nincs `hu-HU` nyelvi és földrajzi jelzés saját domainen, nincs NAP-konzisztencia auditálva. | — |

### 2.4 Performance

Az éles oldal nem mérhető, ezért itt **a redesignra vonatkozó kockázatot** rögzítem:

| # | Kockázat | Miért kritikus itt |
|---|---|---|
| P1 | Instagram-beágyazó szkript (`embed.js`) | ~1,2 MB harmadik féltől, saját fő szálat blokkoló futással. Egy 6 posztos beágyazás önmagában megbukik minden Core Web Vitals-célon. **Tiltott a specifikációban** (9.6). |
| P2 | Előtte/utána galéria kezeletlen JPEG-ekkel | Ez a szakma legnehezebb tartalma. AVIF + `srcset` + `loading="lazy"` + fix `aspect-ratio` nélkül LCP és CLS egyszerre borul. |
| P3 | Betűtípus-villanás | Két betűcsalád, ékezetes magyar szöveg. `font-display:swap` és latin+latin-ext subset nélkül FOIT vagy nagy elrendezés-ugrás. |

---

## 3. Miért rosszak ezek — a mögöttes ok, nem a tünet

Négy ok, minden fenti tünet ezekre vezethető vissza.

### 3.1 A csatorna formátuma felülírta az üzenetet

Az Instagram **idő szerint rendez és képet jutalmaz**. Egy olyan szolgáltatás, amelynek
a lényege *az orvosi képesítés, a dozírozás és a kockázatkezelés* — vagyis végig szöveges,
sorrendhez kötött információ — ebben a formátumban nem tud megjelenni. Ezért került az
árlista *képbe*, a szabadság *posztba*, a képesítés pedig *sehova*.

**A tünet nem az, hogy hiányzik egy weboldal. Az ok az, hogy a szolgáltatás legfontosabb
tulajdonságai nem férnek bele a jelenlegi médium formátumába.**

### 3.2 Kategóriatévesztés a láncolat minden pontján

A Google szerint „Kozmetikai vállalat" (F4). Az IG-esztétika a szépségipar konvencióit
követi. A weboldal — ha van — vélhetően szintén. Közben a szolgáltató **fogorvos és
szájsebész** (F5).

Ez nem finomhangolási kérdés. **Az orvos-esztétika vásárlásakor a páciens kockázatot
vásárol le, nem szépséget vásárol meg.** Aki „kozmetikai vállalatot" lát, az árat
hasonlít össze. Aki klinikát lát, az kompetenciát hasonlít össze. A La' Belle az első
összehasonlításban nem tud nyerni (a kozmetikus mindig olcsóbb), a másodikban pedig
Tolna vármegyében nincs kihívója.

### 3.3 A bizonyíték és a döntés külön helyen van

Az IG-en ott a bizonyíték (előtte/utána, 5,0 ★, 516 poszt). A döntés helye viszont egy
DM-ablak, ahol a páciensnek **kérdeznie kell** — vagyis szégyenkeznie. Az orvos-esztétika
első vásárlása előtti fő gát nem az ár, hanem az, hogy a páciens nem tudja, mit kérdezzen,
és nem akarja elárulni, hogy nem tudja.

**Egy jó oldal itt azt csinálja, hogy megválaszolja a ki nem mondott kérdést, mielőtt
kérdezni kellene.**

### 3.4 Egyetlen ponton sincs aszinkron kapacitás

Az orvos maga kezel, maga válaszol DM-ben, maga megy szabadságra. Minden csatorna az ő
idejét fogyasztja. Egy weboldal itt nem marketingeszköz, hanem **kapacitáseszköz**:
minden kérdés, amit az oldal megválaszol, egy DM, amit nem kell megválaszolni.

Ezért lesz a 12. fejezetben a fő KPI nem a látogatószám, hanem a
**„beérkező időpontkérés / megválaszolt DM" arány**.

---

## 4. Új információs architektúra és sitemap

### 4.1 A rendezőelv

Nem szolgáltatáslista, hanem **döntési szakasz**. Három belépő, amit a 0.2 három
célcsoportja diktál, és egy közös kimenet.

```
                 ┌─────────────────────────────┐
                 │   /  főoldal                │
                 │   „mi ez és ki csinálja"    │
                 └──────────────┬──────────────┘
        ┌───────────────┬───────┴────────┬─────────────────┐
        ▼               ▼                ▼                 ▼
  /kezelesek/      /arak/         /dr-imre-laura/     /eredmenyek/
  „mit lehet"      „mennyi"       „ki csinálja"       „mit hozott"
        │               │                │                 │
        └───────────────┴───────┬────────┴─────────────────┘
                                ▼
                          /idopont/   ← az oldal EGY dolga
```

### 4.2 Sitemap URL-enkénti indoklással

| URL | Cél | Miért ezen az URL-en | Kiemelt storynak megfelel? |
|---|---|---|---|
| `/` | Belépő, orientáció, gyors foglalás | — | — |
| `/kezelesek/` | Hub, a teljes kínálat egy nézetben, szűrhető | A `Szolgáltatások` story szöveges, kereshető megfelelője | ✅ `Szolgáltatások` |
| `/kezelesek/ajakfeltoltes/` | Legkeresettebb önálló kezelés | „ajakfeltöltés Szekszárd" — önálló keresési szándék, önálló URL-t érdemel. Itt él a **szignatúra elem** (7.6). | ✅ `Lips` |
| `/kezelesek/arcfeltoltes/` | Hyaluronsavas arcváz-kezelések (áll, járomcsont, nasolabialis) | Külön szándék az ajaktól; itt indokolható a szájsebészi kompetencia | — |
| `/kezelesek/rancfeltoltes/` | Mimikai ráncok kezelése | **Jogi megjegyzés (10.6): márkanév nem használható.** URL-ben és címben sem. | — |
| `/kezelesek/biostimulacio/` | Mezoterápia, skin booster, kollagénindukció | Gyűjtő, mert ezek a páciens fejében egy döntés | — |
| `/kezelesek/prp/` | Saját vérplazmás kezelés (arc és hajas fejbőr) | F2: vérvételes poszt + hajvonal előtte/utána. **A C-célcsoport belépője.** | — |
| `/kezelesek/carbon-peeling/` | Lézeres carbon peeling | F2: akciós poszt nevesíti | — |
| `/kezelesek/hydra-beauty/` | Hidrodermabráziós arckezelés | F2: akciós poszt nevesíti | — |
| `/kezelesek/calecim/` | CALECIM professional kezelés | F2: akciós poszt nevesíti. Márkakeresés. | — |
| `/kezelesek/lezeres-szortelenites/` | Lézeres szőrtelenítés | Külön kiemelt story van rá → önálló kereslet, önálló URL | ✅ `Szőrtelenítés` |
| `/kezelesek/sminktetovalas/` | Sminktetoválás | F5: katalógus nevesíti | — |
| `/kezelesek/orvosi-kozmetika/` | Orvosi kozmetika | F5 | — |
| `/arak/` | **Teljes, dátumozott árlista egy oldalon** | A `2025 árak` story pótlása: kereshető, linkelhető, egy helyen frissíthető, évszám nélküli URL-lel | ✅ `2025 árak` |
| `/dr-imre-laura/` | Az orvos: képesítés, továbbképzések, kamarai adatok | K3 orvoslása. Saját URL kell, mert a személy külön keresési entitás. | — |
| `/a-klinika/` | A hely, felszerelés, megközelítés, parkolás, akadálymentesség | F3 anyaghasználata itt él; a „hova jövök" szorongás oldása | — |
| `/eredmenyek/` | Előtte/utána galéria, hozzájárulási és jogi kerettel | J3 + 10.5 | — |
| `/zo-skin-health/` | Forgalmazott termékcsalád | J9, márkakeresés, kiskereskedelmi bevétel | ✅ `ZO Skin He...` |
| `/idopont/` | **Az űrlap** | Önálló URL kell, hogy DM-ben, Google-profilban, storyban linkelhető legyen | — |
| `/gyik/` | Fájdalom, downtime, kockázat, ellenjavallat, lemondás | A ki nem mondott kérdések helye (3.3). `FAQPage` schema. | — |
| `/kapcsolat/` | NAP, két telefonszám, nyitvatartás, térkép | U3, U5 | — |
| `/adatkezelesi-tajekoztato/`, `/impresszum/` | Jogi kötelező | Egészségügyi szolgáltató: kötelező | — |

**Amit szándékosan NEM veszek fel az 1. fázisba:** blog / tudástár. Indoklás: tartalom-
karbantartási kötelezettséget jelent, amire nincs dokumentált kapacitás, és üresen álló
blog rosszabb, mint a hiánya. A 14. fejezetben a 3. fázisba kerül.

### 4.3 Navigáció

- **Desktop:** vízszintes sáv — `Kezelések` (megaменü a 4.2 listával) · `Árak` ·
  `Dr. Imre Laura` · `Eredmények` · `Kapcsolat` + kiemelt `Időpontkérés` gomb.
- **Mobil:** ugyanez fiókban (drawer), **plusz egy fix alsó sáv két gombbal: `Hívás` és
  `Időpontkérés`**. A `Hívás` azért marad elsőnek, mert a mai működő csatorna, és nem
  szabad egy szokást erőszakkal átterelni.
- A `Kezelések` megamenü **nem** rejti el az árat: minden tétel mellett `-tól` ár áll
  (placeholder), mert az árkérdés az első kattintás előtt van, nem utána.

---

## 5. Oldalankénti felépítés

### 5.1 Főoldal `/` — szekciótábla

| # | Szekció | Tartalom | Cél | Bizonyíték/forrás |
|---|---|---|---|---|
| 1 | Fejléc | logó, navigáció, téma-kapcsoló, `Időpontkérés` | orientáció | — |
| 2 | **Hero** | H1: `Orvos-esztétika Szekszárdon, szájsebészi kézzel.` Alcím: „Tolna vármegye első orvos-esztétikai klinikája. Kezelőorvos: Dr. Imre Laura fogorvos, szájsebész, esztétikai orvos." 2 CTA: `Időpontkérés` (elsődleges), `Árak megnézése` (másodlagos). | J1 + K3 egyben, az első képernyőn | F1, F5 |
| 3 | **Tényszalag** | 4 tétel: `5,0 ★ · 52 értékelés` · `Tolna vármegye első klinikája` · `[X] éve a szakmában` · `Csalogány u. 2., Szekszárd` | bizonyíték a hajtás alatt közvetlenül | F4, F1, [placeholder] |
| 4 | **Három belépő** | „Először jönnék" / „Bőrkezelésre járok" / „Férfiaknak" — három kártya, három külön útvonallal | 0.2 három célcsoportja | rekonstruált |
| 5 | **Kezelések** | 8–10 kezelés kártyaként, `-tól` árral, csoportosítva: *injektálás · bőrkezelés · készülékes* | U1 orvoslása | F1, F2 |
| 6 | **SZIGNATÚRA: „Az egy milliliter"** | Életnagyságú, bankkártyával kalibrálható dózisskála (7.6) | A dozírozás fogalmának megmutatása | koncepció |
| 7 | **Az orvos** | Portré, képesítés-lista, egy bekezdés első személyben, link `/dr-imre-laura/` | K3, J2 | F5 |
| 8 | **Eredmények** | 3 előtte/utána pár, hozzájárulási címkével, link a galériára | J3 | F2 |
| 9 | **A folyamat** | 4 lépés: `konzultáció → terv és ár → kezelés → kontroll` | a ki nem mondott kérdés (3.3) | koncepció |
| 10 | **Elérhetőség sáv** | nyitvatartás + „mostani elérhetőség" szerkeszthető mező (szabadság) | U3, U4, J7 | F2, F4 |
| 11 | **Vélemények** | 5,0 ★ / 52, 2–3 idézet | J4 | F4 + [placeholder idézetek] |
| 12 | **Időpontkérő űrlap** | 6 mező, inline validáció | az oldal EGY dolga | — |
| 13 | **GYIK-kivonat** | 5 kérdés, `<details>` | — | — |
| 14 | Lábléc | NAP, két telefonszám címkézve, jogi linkek, IG/FB | U5, J6 | F2 |

### 5.2 A többi oldal váza (rövidítve)

| Oldal | Kötelező szekciók sorrendben |
|---|---|
| `/kezelesek/{név}/` | H1 kezelésnév + hely · mire jó · **kinek nem ajánlott** · mi történik a székben · érzés/fájdalom · downtime idővonal · tartósság · **ár** · GYIK · időpontkérés · kapcsolódó kezelés |
| `/arak/` | H1 + **frissítés dátuma** · kategóriánkénti táblázat · mit tartalmaz az ár · fizetés módja · lemondási feltétel · CTA |
| `/dr-imre-laura/` | portré · végzettségek évszámmal · továbbképzések · kamarai/nyilvántartási szám · szakmai hitvallás · CTA |
| `/eredmenyek/` | jogi keret elöl · szűrő kezelésre · páronkénti kártya (kezelés, dózis, eltelt idő) · CTA |
| `/idopont/` | űrlap · mi történik a küldés után · válaszidő · telefonos alternatíva |
| `/gyik/` | témacsoportok · `<details>` · `FAQPage` schema |

### 5.3 A prototípusban ténylegesen megépült oldalak

| Fájl | URL élesben | Mit demonstrál |
|---|---|---|
| `index.html` | `/` | teljes főoldal + a szignatúra elem |
| `arak/index.html` | `/arak/` | a `2025 árak` story kiváltása: kereshető, linkelhető, dátumozott árlista ugrósávval és feltételekkel |
| `kezelesek/ajakfeltoltes/index.html` | `/kezelesek/ajakfeltoltes/` | a kezelésoldal-sablon: mire jó / mire nem / kinek nem ajánlott / mi történik / **gyógyulási idővonal** / mennyiség / ár / GYIK |
| `assets/labelle.css` | `/assets/…` | a design system egyetlen forrásból, mindhárom oldalon |
| `assets/labelle.js` | `/assets/…` | az öt viselkedés, oldalanként önmagát kikapcsolva, ha az elem nincs ott |

A többi URL a 4.2-es sitemapből a 2. és 3. fázisban épül, ugyanezzel a
sablonnal.

**A „kinek nem ajánlott" szekció szándékos.** Ez az egyetlen elem, ami egy kozmetikus
oldalán soha nincs ott, és amitől orvosinak érződik az egész. Konverziót nem csökkent:
kockázatérzetet csökkent.

---

## 6. Wireframe

### 6.1 Főoldal — desktop (≥1024px, 12 oszlop, 1200px max)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ [LB] La' Belle    Kezelések▾  Árak  Dr. Imre Laura  Eredmények  Kapcsolat    │
│                                              [◐ téma]  [ Időpontkérés → ]    │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ORVOS-ESZTÉTIKA SZEKSZÁRDON,                    ┌────────────────────────┐  │
│   SZÁJSEBÉSZI KÉZZEL.                             │                        │  │
│   ──────────────────────────                      │   A klinika belső      │  │
│   Tolna vármegye első orvos-esztétikai            │   tere — márvány,      │  │
│   klinikája. Kezelőorvos: Dr. Imre Laura          │   körlámpa, acél       │  │
│   fogorvos, szájsebész, esztétikai orvos.         │   (F3, AVIF, 3:2)      │  │
│                                                   │                        │  │
│   [ Időpontkérés → ]   [ Árak megnézése ]         └────────────────────────┘  │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│  5,0 ★ / 52 értékelés │ Vármegye első │ [X] éve │ Csalogány u. 2., Szekszárd │
├──────────────────────────────────────────────────────────────────────────────┤
│   HONNAN INDULSZ?                                                            │
│   ┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐       │
│   │ Először jönnék     │ │ Bőrkezelésre járok │ │ Férfiaknak         │       │
│   │ Mit érdemes tudni  │ │ Sorozatok, termék  │ │ Diszkrét, orvosi   │       │
│   │ az első alkalom →  │ │ ZO Skin Health   → │ │ PRP, hajkezelés  → │       │
│   └────────────────────┘ └────────────────────┘ └────────────────────┘       │
├──────────────────────────────────────────────────────────────────────────────┤
│   KEZELÉSEK                                       [ mind a 12 kezelés → ]    │
│   ── injektálás ──────────────────────────────────────────────────────────   │
│   ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐    │
│   │ Ajakfeltöltés │ │ Arcfeltöltés  │ │ Ráncfeltöltés │ │ Biostimuláció │    │
│   │ 0,5–1 ml      │ │ áll, járomcs. │ │ mimikai ráncok│ │ mezoterápia   │    │
│   │ [ár]-tól      │ │ [ár]-tól      │ │ [ár]-tól      │ │ [ár]-tól      │    │
│   └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘    │
│   ── bőrkezelés ──────────────────────────────────────────────────────────   │
│   ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐    │
│   │ Carbon peeling│ │ Hydra Beauty  │ │ CALECIM       │ │ PRP           │    │
│   └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘    │
├──────────────────────────────────────────────────────────────────────────────┤
│ ╔══════════════════════ SZIGNATÚRA ═══════════════════════════════════════╗  │
│ ║  AZ EGY MILLILITER                                                      ║  │
│ ║  ┌───────────────────────────────────────────┐   0,8 ml                 ║  │
│ ║  │ ┌ ─ ─ bankkártya kerete (85,6 mm) ─ ─ ┐   │   ────────               ║  │
│ ║  │ │  ╭──────────────────────────────╮   │   │   ≈ 16 csepp            ║  │
│ ║  │ │  │████████████░░░░░░░░░░░░░│▮▮▮ │   │   │   ≈ 1/6 kávéskanál      ║  │
│ ║  │ │  ╰──┬────┬────┬────┬────┬───────╯   │   │                          ║  │
│ ║  │ │    0,2  0,5  1,0  1,5  2,0 ml       │   │   A különbség a          ║  │
│ ║  │ └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘   │   természetes és a       ║  │
│ ║  └───────────────────────────────────────────┘   feltűnő között          ║  │
│ ║  [◀━━━━━━━━●━━━━━━━━▶]  csúszka                  gyakran fél milliliter. ║  │
│ ║  Tartsd a bankkártyád a szaggatott kerethez — ha illeszkedik,            ║  │
│ ║  a fecskendő is életnagyságú a képernyődön.                             ║  │
│ ╚═════════════════════════════════════════════════════════════════════════╝  │
├──────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐   DR. IMRE LAURA                                           │
│  │              │   fogorvos · szájsebész · esztétikai orvos                 │
│  │   portré     │   „[első személyű bekezdés — ügyfélszöveg kell]"           │
│  │   4:5 AVIF   │   • [végzettség, év]  • [szakvizsga, év]  • [nyilv. szám]  │
│  └──────────────┘   [ Az orvosról részletesen → ]                            │
├──────────────────────────────────────────────────────────────────────────────┤
│   EREDMÉNYEK          ┌────────┬────────┐ ┌────────┬────────┐  … [galéria →] │
│   hozzájárulással     │ előtte │ utána  │ │ előtte │ utána  │                │
│                       └────────┴────────┘ └────────┴────────┘                │
├──────────────────────────────────────────────────────────────────────────────┤
│   A FOLYAMAT   ①konzultáció → ②terv és ár → ③kezelés → ④kontroll             │
├──────────────────────────────────────────────────────────────────────────────┤
│   ELÉRHETŐSÉG   H–P [ó]–[ó] · Szo [ó] · V zárva   ● Most: [állapotmező]      │
│                 esztétika 0630 719 1991 · fogászat 0674 512 222              │
├──────────────────────────────────────────────────────────────────────────────┤
│   IDŐPONTKÉRÉS                                    │  MIT KAPSZ VISSZA        │
│   Név* [_______]      Telefon* [_______]          │  • [X] órán belül válasz │
│   E-mail [_______]    Kezelés  [ ▾ ]              │  • időpontjavaslat       │
│   Mikor jó? [ ▾ ]                                 │  • nem kötelez semmire   │
│   Üzenet [__________________________]             │                          │
│   ☐ Adatkezelési tájékoztatót elolvastam*         │  Inkább telefonálnál?    │
│   [ Időpontot kérek → ]                           │  0630 719 1991           │
├──────────────────────────────────────────────────────────────────────────────┤
│   GYIK ▸ Fáj? ▸ Meglátszik? ▸ Meddig tart? ▸ Kinek nem ajánlott? ▸ Lemondás  │
├──────────────────────────────────────────────────────────────────────────────┤
│  La' Belle · Csalogány u. 2., 7100 Szekszárd · esztétika: 0630 719 1991      │
│  fogászat: 0674 512 222 · Instagram · Facebook · Adatkezelés · Impresszum    │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Főoldal — mobil (375px, 1 oszlop, 20px gutter)

```
┌───────────────────────────────┐
│ [LB] La' Belle    [◐] [☰]     │  fejléc 56px, sticky
├───────────────────────────────┤
│                               │
│ ORVOS-ESZTÉTIKA               │  H1 clamp → 30px @375
│ SZEKSZÁRDON,                  │
│ SZÁJSEBÉSZI KÉZZEL.           │
│                               │
│ Tolna vármegye első orvos-    │
│ esztétikai klinikája.         │
│ Kezelőorvos: Dr. Imre Laura   │
│ fogorvos, szájsebész,         │
│ esztétikai orvos.             │
│                               │
│ [   Időpontkérés →        ]   │  56px magas, teljes szélesség
│ [   Árak megnézése        ]   │
│                               │
│ ┌───────────────────────────┐ │
│ │ klinikakép 3:2, AVIF      │ │  a hero KÉP a szöveg ALATT:
│ │ fetchpriority=high        │ │  az LCP a H1 legyen, ne a kép
│ └───────────────────────────┘ │
├───────────────────────────────┤
│ 5,0 ★ · 52 értékelés          │  2×2 rács
│ Vármegye első klinikája       │
│ [X] éve a szakmában           │
│ Csalogány u. 2.               │
├───────────────────────────────┤
│ HONNAN INDULSZ?               │
│ ┌───────────────────────────┐ │  egymás alatt,
│ │ Először jönnék         →  │ │  nem vízszintes scroll
│ └───────────────────────────┘ │  (gesture-conflicts)
│ ┌───────────────────────────┐ │
│ │ Bőrkezelésre járok     →  │ │
│ └───────────────────────────┘ │
│ ┌───────────────────────────┐ │
│ │ Férfiaknak             →  │ │
│ └───────────────────────────┘ │
├───────────────────────────────┤
│ KEZELÉSEK                     │
│ ── injektálás ──              │
│ ┌───────────┐ ┌───────────┐   │  2 oszlop 375px-en is elfér
│ │Ajakfelt.  │ │Arcfelt.   │   │  (min 150px kártya)
│ │[ár]-tól   │ │[ár]-tól   │   │
│ └───────────┘ └───────────┘   │
│ …                             │
├───────────────────────────────┤
│ AZ EGY MILLILITER             │  SZIGNATÚRA
│ ┌───────────────────────────┐ │
│ │┌ ─ kártya kerete ─ ─ ─ ┐  │ │  a kártyakeret 375px-en
│ ││ ╭────────────────╮    │  │ │  vízszintesen elfér
│ ││ │███████░░░░░│▮▮▮ │    │  │ │  (85,6 mm ≈ 323 CSS px)
│ ││ ╰─┬───┬───┬───┬──╯    │  │ │
│ ││  0,2 0,5 1,0 2,0      │  │ │
│ │└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘  │ │
│ └───────────────────────────┘ │
│         0,8 ml                │  a kiírás a rajz ALÁ kerül
│    ≈16 csepp · ≈1/6 kanál     │
│ [◀━━━━●━━━━▶]  56px csúszka   │
├───────────────────────────────┤
│ DR. IMRE LAURA                │
│ ┌───────────────────────────┐ │
│ │ portré 4:5                │ │
│ └───────────────────────────┘ │
│ fogorvos · szájsebész ·       │
│ esztétikai orvos              │
│ [ Az orvosról →  ]            │
├───────────────────────────────┤
│ EREDMÉNYEK                    │
│ ┌─────────┬─────────┐         │
│ │ előtte  │ utána   │         │
│ └─────────┴─────────┘         │
│ (függőlegesen görgetve, nem   │
│  vízszintes karusszelben)     │
├───────────────────────────────┤
│ A FOLYAMAT                    │
│ ① konzultáció                 │  függőleges lista,
│ ② terv és ár                  │  bal oldali vonallal
│ ③ kezelés                     │
│ ④ kontroll                    │
├───────────────────────────────┤
│ ELÉRHETŐSÉG                   │
│ H–P [ó]–[ó]                   │
│ ● Most: [állapotmező]         │
├───────────────────────────────┤
│ IDŐPONTKÉRÉS                  │
│ Név*                          │  egy oszlop, 48px mezők,
│ [_______________________]     │  16px betűméret (iOS zoom ellen)
│ Telefon*                      │
│ [_______________________]     │  inputmode=tel
│ …                             │
│ [ Időpontot kérek →       ]   │
├───────────────────────────────┤
│ GYIK ▸ ▸ ▸                    │
├───────────────────────────────┤
│ lábléc                        │
│                               │
│ (80px alsó padding a fix      │
│  sáv miatt)                   │
├───────────────────────────────┤
│ [ 📞 Hívás ]  [ Időpontkérés ]│  FIX ALSÓ SÁV
│ safe-area-inset-bottom        │  56px + safe area
└───────────────────────────────┘
```

### 6.3 Kezelésoldal — mobil váz

```
┌───────────────────────────────┐
│ ‹ Kezelések                   │  vissza, nem hamburger
├───────────────────────────────┤
│ AJAKFELTÖLTÉS                 │  H1
│ Szekszárd · [ár]-tól · 30 perc│
├───────────────────────────────┤
│ MIRE JÓ                       │
│ MIRE NEM                      │  ⟵ a kulcselem
│ KINEK NEM AJÁNLOTT            │
├───────────────────────────────┤
│ MI TÖRTÉNIK                   │
│ ├ érkezés és konzultáció      │
│ ├ érzéstelenítés              │
│ ├ injektálás                  │
│ └ hűtés, tájékoztató          │
├───────────────────────────────┤
│ GYÓGYULÁSI IDŐVONAL           │
│ 0ó ──── 24ó ──── 3nap ─── 2hét│
│ [▮▮▮▮▮▮▮░░░░░░░░░░░░░░░░░░░]  │
│ „mikor mehetek vissza"        │
├───────────────────────────────┤
│ [ Időpontot kérek → ]         │  sticky a szekció alján
└───────────────────────────────┘
```

---

## 7. Design system

### 7.0 A vizuális kiindulópont — egy mondat

> **A kiindulópont a klinika saját kezelőterének anyaga (F3): hideg szürke márvány és
> kefélt acél, amit egyetlen meleg fényforrás, a mennyezeti körlámpa világít be — tehát
> hideg kő plusz egy meleg lámpafény-tónus, semmi más.**

Ebből következik minden döntés:

- a paletta **hideg semleges alap + egyetlen meleg akcentus** (nem rózsaszín, nem türkiz,
  nem arany);
- a **kör** mint az egyetlen visszatérő geometriai motívum (körlámpa, fecskendő
  keresztmetszete, gomb-fókuszgyűrű) — de dísztelenül, nem dekorációként;
- a sötét mód nem „sötét UI-téma", hanem **a kezelő éjjel: minden kihűl, csak a lámpa
  marad meleg** — ezért a sötét módban az akcentus melegebbé és világosabbá válik, nem
  hidegebbé.

**Amit ez kizár** (és amit a brief is tiltott): Playfair+Inter, 01/02/03 számozás valódi
sorrend nélkül, fekete alap egyetlen neon akcentussal, gradiens a hero szöveg mögött,
stock-fotó ikonok. Ezek egyike sincs a rendszerben.

### 7.1 Színtokenek — 9 nevesített token, WCAG-számokkal

A számok saját méréséből (WCAG 2.1 relatív luminancia, `scratchpad/k.py`).

| # | Token | Világos | Sötét | Szerep |
|---|---|---|---|---|
| 1 | `--marvany` | `#F6F5F2` | `#15181B` | oldal háttere (a padló) |
| 2 | `--lap` | `#FFFFFF` | `#1E2227` | kártya, űrlap, felület |
| 3 | `--grafit` | `#1C2024` | `#E8E7E3` | elsődleges szöveg (az LB logó tónusa) |
| 4 | `--halk` | `#5A626B` | `#A3A9B0` | másodlagos szöveg |
| 5 | `--lampafeny` | `#8A5A28` | `#E0A868` | **az egyetlen akcentus** — a körlámpa melege |
| 6 | `--lampafeny-halk` | `#F3EBE0` | `#2A2119` | akcentus-tónusú felület |
| 7 | `--acel` | `#DEDBD4` | `#333A41` | hajszálvonal, elválasztó (dekoratív) |
| 8 | `--mezsgye` | `#8C8A83` | `#6A727A` | **űrlapmező- és komponenskeret** (állapotot hordoz) |
| 9 | `--hiba` | `#A62A1F` | `#FF9C8A` | hibaállapot |

**Kontrasztmátrix (mért):**

| Pár | Világos | Sötét | Követelmény | ✓ |
|---|---|---|---|---|
| `--grafit` / `--marvany` | **15,03:1** | **14,40:1** | 4,5 (AA szöveg) | ✓ AAA |
| `--grafit` / `--lap` | **16,39:1** | **12,92:1** | 4,5 | ✓ AAA |
| `--halk` / `--marvany` | **5,68:1** | **7,52:1** | 4,5 | ✓ AA |
| `--halk` / `--lap` | **6,19:1** | **6,75:1** | 4,5 | ✓ AA |
| `--halk` / `--lampafeny-halk` | **5,24:1** | **6,66:1** | 4,5 | ✓ AA |
| `--lampafeny` / `--marvany` | **5,39:1** | **8,46:1** | 4,5 | ✓ AA |
| `--lampafeny` / `--lap` | **5,88:1** | **7,59:1** | 4,5 | ✓ AA |
| gombszöveg / `--lampafeny` gombháttér | **5,88:1** (fehér) | **8,46:1** (`#15181B`) | 4,5 | ✓ AA |
| `--mezsgye` / `--marvany` | **3,17:1** | **3,65:1** | 3,0 (nem-szöveg UI) | ✓ AA |
| `--mezsgye` / `--lap` | **3,45:1** | **3,27:1** | 3,0 | ✓ AA |
| `--hiba` / `--lap` | **7,07:1** | **7,90:1** | 4,5 | ✓ AA |
| `--hiba` / `--marvany` | **6,48:1** | — | 4,5 | ✓ AA |
| `--grafit` / `--lampafeny-halk` | **13,87:1** | **12,76:1** | 4,5 | ✓ AAA |

**Alternatíva, amit elvetettem:** a `ui-ux-pro-max --design-system` gépi javaslata
`#0891B2` orvosi türkiz + `#16A34A` egészségzöld volt. Elvetve két okból: (a) a brief
kifejezetten tiltja a „zöld, ha egészség" reflexet; (b) a türkiz-zöld az *állami/rendelői*
egészségügy kódja, a La' Belle viszont magánklinika prémium anyaghasználattal (F3) — a
türkiz itt lefelé pozicionál. A skill többi rétegét (a11y-szabálykészlet, touch-target
és állapotkontraszt-előírások) viszont teljes egészében beépítettem.

### 7.2 Tipográfia

**Két variable betűcsalád, mindkettő teljes latin-ext lefedettséggel — az `ő` és `ű`
valódi kettős hegyes ékezettel, nem umlauttal helyettesítve.**

| Szerep | Család | Tengelyek | Miért ez |
|---|---|---|---|
| **Display** | **Source Serif 4** | `wght 200–900`, `opsz 8–60` | Tranzicionális szerif optikai méret-tengellyel. Az „orvosi szakirodalom", nem az „esküvői meghívó" regisztere. Adobe közép-európai ékezetrajza a legmegbízhatóbb a szabadon elérhető szerifek közül — a `ő`/`ű` nem összeolvadt, hanem két különálló vessző. Az `opsz` tengely miatt kis méretben is használható, nem esik szét, mint a magas kontrasztú didone-ok. |
| **Szöveg** | **Schibsted Grotesk** | `wght 400–900` | Hírolvasásra tervezett groteszk: szűk, de nyitott rajzolatú, jól bírja a hosszú magyar összetett szavakat („orvos-esztétikai", „szőrtelenítés"). Semleges, de nem arctalan. |

**Miért nem a tiltott páros:** a Playfair Display magas kontrasztú didone → vékony
vonalai kis méretben eltűnnek, és a szépségipar teljes egészében ezt használja, tehát
pont a differenciálást akadályozza. Az Inter szándékosan neutrális UI-betű — weboldal
törzsszövegében jellegtelen.

**A display face minimális használati mérete: 18px.** Alatta az `opsz` tengely már nem
kompenzálja a vékony összekötő vonalakat ékezetes magyar szövegben; 18px alatt kizárólag
a Schibsted Grotesk használható. Az `opsz` a méretre van kötve
(`font-optical-sizing: auto`).

**Típusskála — `clamp()`, 375px→1440px között folytonos:**

| Token | Érték | 375px | 1440px |
|---|---|---|---|
| `--t-display` | `clamp(1.875rem, 1.1rem + 3.3vw, 4rem)` | 30px | 64px |
| `--t-h2` | `clamp(1.5rem, 1.1rem + 1.7vw, 2.5rem)` | 24px | 40px |
| `--t-h3` | `clamp(1.1875rem, 1.05rem + .58vw, 1.625rem)` | 19px | 26px |
| `--t-lead` | `clamp(1.0625rem, 1rem + .33vw, 1.25rem)` | 17px | 20px |
| `--t-body` | `1rem` | 16px | 16px |
| `--t-small` | `.875rem` | 14px | 14px |
| `--t-micro` | `.75rem` | 12px | 12px |

Sormagasság: display `1.05`, h2 `1.15`, törzsszöveg `1.6`, `--t-small` `1.5`.
Sorhossz: `max-width: 66ch` minden folyószövegen.
Számok: `font-variant-numeric: tabular-nums` az árakon, a ml-értéken és a csillagos
értékelésen — hogy a szignatúra elem csúszkáján ne ugráljon a szám szélessége.

### 7.3 Térköz — 8px-alap

`--s-1:4px` · `--s-2:8px` · `--s-3:12px` · `--s-4:16px` · `--s-5:24px` · `--s-6:32px` ·
`--s-7:48px` · `--s-8:64px` · `--s-9:96px`

Szekcióritmus: mobilon `--s-7`, ≥768px `--s-8`, ≥1200px `--s-9`.
Gutter: 375px→`--s-5`, 768px→`--s-6`, ≥1200px→`--s-7`.
Konténer: `max-width: 1200px`.

### 7.4 Elevation — 4 szint, kőfelület-logika

Márványon a tárgy nem lebeg, hanem **árnyékot vet és tükröződik**. Ezért az elevation
kettős: lágy elterülő árnyék + 1px felső fénybelső árnyék.

| Szint | Használat | Világos | Sötét |
|---|---|---|---|
| `--e-0` | alapfelület | `none` | `none` |
| `--e-1` | kártya | `0 1px 2px rgba(28,32,36,.05), 0 2px 8px rgba(28,32,36,.04)` | `0 1px 2px rgba(0,0,0,.5)` |
| `--e-2` | kiemelt kártya, hover | `0 2px 4px rgba(28,32,36,.06), 0 8px 24px rgba(28,32,36,.07)` | `0 2px 4px rgba(0,0,0,.5), 0 8px 24px rgba(0,0,0,.4)` |
| `--e-3` | fiók, fix alsó sáv | `0 -2px 16px rgba(28,32,36,.09)` | `0 -2px 16px rgba(0,0,0,.55)` |

Sötét módban az árnyék önmagában nem látszik, ezért ott a felületelválasztás a
**világosságkülönbség** (`--lap` `#1E2227` vs `--marvany` `#15181B`) plusz `--acel`
hajszálvonal. Ez az `elevation-consistent` és a `border-and-divider-visibility` szabály
együtt.

Lekerekítés: `--r-1:4px` (címke, chip) · `--r-2:8px` (mező, gomb) · `--r-3:14px` (kártya)
· `--r-teljes:999px` (csak kör alakú elemeken).

### 7.5 Komponenslista

| Komponens | Állapotok | Megjegyzés |
|---|---|---|
| `Gomb / elsődleges` | alap, hover, focus-visible, active, disabled, loading | 48px magas (mobil 56px), `--lampafeny` háttér |
| `Gomb / másodlagos` | ua. | `--mezsgye` keret, átlátszó háttér |
| `Gomb / szöveges` | ua. | aláhúzás hoveren, nem csak szín |
| `Link` | alap, hover, visited, focus-visible | mindig aláhúzott folyószövegben |
| `Kezeléskártya` | alap, hover, focus-within | teljes felület kattintható, de a link a címben van |
| `Belépőkártya` (3 db) | alap, hover, focus | — |
| `Tényszalag-elem` | statikus | tabular-nums |
| `Űrlapmező` | alap, focus, hiba, kitöltött, disabled | látható címke, `aria-describedby` |
| `Jelölőnégyzet` | alap, focus, hiba | 24px vizuális, 44px tapintható |
| `Kiválasztó (select)` | natív | natív, nem custom — `system-controls` |
| `Csúszka (range)` | alap, focus, aktív hüvelyk | a szignatúra elem vezérlője, 28px hüvelyk / 44px tapintható |
| `Akkordeon` (`<details>`) | zárt, nyitott, focus | natív elem |
| `Előtte/utána pár` | statikus | fix `aspect-ratio`, hozzájárulási címke |
| `Idővonal` | statikus | gyógyulási idő |
| `Elérhetőség-jelző` | nyitva / zárva / szabadság | szín + ikon + szöveg (`color-not-only`) |
| `Téma-kapcsoló` | auto / világos / sötét | 3 állapot, `aria-pressed` csoport |
| `Fix alsó sáv` (mobil) | — | safe-area-inset |
| `Skip-link` | rejtett / fókuszban | első fókuszálható elem |
| `Toast` (űrlap-visszajelzés) | siker, hiba | `role="status"` / `role="alert"` |
| `Morzsa` | statikus | az utolsó elem nem link, `aria-current="page"` |
| `Ugrósáv` (horgonysáv) | alap, hover, **aktív** | ragadós a fejléc alatt; az aktív szakaszt `IntersectionObserver` jelöli `aria-current="true"`-val |
| `Ártáblázat` | hover soronként | saját `overflow-x` konténer, `tabular-nums`, jobbra zárt ár |
| `Gyógyulási idővonal` | statikus | a sáv hossza = idő, tónusa = láthatóság; minden fokozat szövegben is |
| `Állítás/korlát dobozpár` | statikus | akcentus = állítás, halk tónus = korlát |
| `Tényszalag-chip` (`.tenysor`) | statikus | aloldali fejléc alatti kulcsadatok |

### 7.6 SZIGNATÚRA ELEM — „Az egy milliliter"

**Mi ez.** Egy életnagyságú, a felhasználó saját bankkártyájával kalibrálható
dózisskála. A rajz egy 1 ml-es fecskendőhenger metszete beosztásokkal, mögötte egy
szaggatott téglalap, ami pontosan **85,6 × 53,98 mm** — az ISO/IEC 7810 ID-1 szabvány,
azaz minden bankkártya mérete. A csúszkával 0,2 és 2,0 ml között lehet állítani a
töltetet; a kiírás tabuláris számmal mutatja a ml-t, mellette **≈ csepp** (1 ml ≈ 20
csepp) és **≈ kávéskanál-tört** (1 ml = 1/5 kávéskanál) átváltással.

**Miért pont ez.**

1. **A szolgáltatás lényegét mutatja meg, nem elmondja.** Az orvos-esztétika és a
   kozmetikus között az a különbség, hogy az egyik **milliliterben dozíroz**. Ezt le
   lehetne írni („precíz, orvosi dozírozás") — az semmit nem jelent. Megmutatni annyit
   jelent, hogy a látogató a saját kezével állítja be a mennyiséget, és megdöbben, milyen
   kevés.
2. **A célközönség legerősebb félelmét oldja.** Az A-csoport (0.2) fő félelme nem a
   fájdalom, hanem a „meg fog látszani". Az 1 ml életnagyságban nevetségesen kicsi.
   Ez az egyetlen érv, amit szöveggel nem lehet átadni.
3. **Nem fotón múlik.** Tiszta SVG + CSS. Nincs modell, nincs stock, nincs
   előtte/utána — tehát nem esik a 10.5 jogi és GDPR-terhe alá sem.
4. **A klinika saját anyagából jön.** A fecskendő beosztása a szakma saját mértékegysége,
   ahogy a körlámpa a saját fénye. Nem kitalált metafora.
5. **Kalibrálható, tehát igaz.** A CSS `mm` egység csak névleges (1mm = 96/25.4 px),
   valós képernyőn eltér. Ezt nem elrejtem, hanem **a felhasználóra bízom**: a
   bankkártya-keret adja a hitelesítést. Ez egyben a legmemorizálhatóbb mozzanat — valaki
   tényleg oda fogja tartani a kártyáját.

**Mibe kerül LCP-ben: nullába.**

| Tétel | Költség |
|---|---|
| Elhelyezés | a hajtás alatt, a 6. szekcióban — nem LCP-jelölt |
| Súly | inline SVG ≈ 2,3 KB nyers / ≈ 0,9 KB brotli után |
| Hálózat | 0 kérés (inline) |
| JS | ≈ 0,7 KB (csúszka-eseménykezelő + `requestAnimationFrame` nélkül, egyszerű attribútum-írás) |
| CLS | 0 — a doboz `aspect-ratio`-val van kitöltve, a szám `tabular-nums` és fix szélességű dobozban van |
| INP | csak `transform`/`width` a kitöltésen — a csúszka `input` eseménye alatt egyetlen SVG-attribútum és egy `textContent` írás, mérésem szerint <1ms |

**Fegyelem máshol.** A merészség ide van elköltve. Az oldal többi része szándékosan
csendes: egy akcentusszín, két betűcsalád, négy elevation-szint, nulla dekoratív
animáció, nulla háttérgradiens, nulla parallax.

---

## 8. Animációk és mikrointerakciók

Alapelv: minden animáció ok-okozatot fejez ki. Ami dísz, az nincs benne.
Globális tokenek: `--gyors:120ms` · `--alap:180ms` · `--lassu:260ms` ·
`--be: cubic-bezier(.2,.8,.3,1)` (ease-out) · `--ki: cubic-bezier(.4,0,1,1)` (ease-in).

| Elem | Interakció | Változó tulajdonság | Időzítés | Miért |
|---|---|---|---|---|
| Elsődleges gomb | hover | `background-color`, `box-shadow` | 120ms `--be` | azonnali visszajelzés, nem elrendezésmozgató |
| Elsődleges gomb | active | `transform: scale(.98)` | 90ms | `scale-feedback`; nem tolja el a környezetet |
| Bármely fókuszálható | `:focus-visible` | `outline` | **0ms** | a fókuszgyűrű animálása lassítja a billentyűs navigációt |
| Kezeléskártya | hover | `box-shadow` `--e-1`→`--e-2`, `transform: translateY(-2px)` | 180ms `--be` | emelkedés = kattintható |
| Kezeléskártya | leave | ua. vissza | **120ms** | kilépés ≈ 66% a belépésből (`exit-faster-than-enter`) |
| Kártyarács | első megjelenés | `opacity 0→1`, `translateY 8px→0` | 260ms, **40ms lépcső**, max 8 elem | `stagger-sequence`; `IntersectionObserver`, egyszer fut |
| Szignatúra csúszka | `input` | SVG `width` attribútum + `textContent` | **0ms (követés)** | `gesture-feedback`: a kitöltésnek az ujjat kell követnie, nem utána érkeznie |
| Szignatúra kitöltés | csúszka elengedése után | — | — | nincs „beugrás": az érték már ott van |
| Mobil fiók (drawer) | nyitás | `transform: translateX(100%→0)`, scrim `opacity` | 260ms `--be` | `modal-motion`, irányhelyes |
| Mobil fiók | zárás | ua. | **180ms `--ki`** | gyorsabb kilépés |
| Akkordeon `<details>` | nyitás | `grid-template-rows 0fr→1fr` | 200ms `--be` | magasság-animáció reflow nélkül |
| Űrlapmező | fókusz | `border-color`, `box-shadow` (gyűrű) | 120ms | — |
| Űrlapmező | hiba megjelenése | `opacity 0→1` a hibaszövegen | 180ms | **nincs rázás/shake**: szorongó közönségnél az agresszív visszajelzés árt |
| Küldés gomb | folyamatban | tárcsa forgása | 800ms/kör, lineáris | folyamatos állapot, nem UI-átmenet — itt a `linear` helyes |
| Toast | be / ki | `opacity` + `translateY(8px)` | 200ms / 140ms | `role=status`, nem lop fókuszt |
| Elérhetőség-jelző pont | folyamatos | **nincs pulzálás** | — | szándékos: a pulzáló pont sürgősséget hazudik |
| Téma-kapcsoló | váltás | `color`/`background` átmenet a `:root`-on | 180ms | de a **kép és az SVG nem** animál, hogy ne villogjon |

**`prefers-reduced-motion: reduce` esetén:** minden `transition-duration` és
`animation-duration` `0.01ms`; a lépcsőzött megjelenés kimarad (az elemek eleve
láthatók); a fiók azonnal jelenik meg; a csúszka követése változatlan (az nem animáció,
hanem közvetlen visszajelzés); a küldés-tárcsa statikus szöveggé válik („Küldés…").

---

## 9. Frontend-megvalósítás

### 9.1 Stack és indoklás

| Réteg | Választás | Miért ez | Mit vetettem el és miért |
|---|---|---|---|
| Renderelés | **Statikus HTML generálás** (Astro vagy Eleventy) | ~20 oldal, napi frissítés nélkül. A `/arak/` és az „elérhetőség" mező szerkesztése kell csak. | **Next.js/React SPA:** kliensoldali JS-t és hidratálást hozna 20 statikus oldalra — nettó veszteség. **WordPress:** egészségügyi adatot érintő űrlaphoz plugin-függő biztonsági felület; havi karbantartási teher, amire nincs kapacitás. |
| Tartalom | **Markdown + fájlalapú CMS** (Decap/Sveltia) vagy Git-alapú szerkesztő | Az orvosnak két dolgot kell tudnia szerkeszteni: árlista és „most elérhető vagyok-e". Ehhez nem kell adatbázis. | **Fejetlen CMS SaaS:** havi díj és külső függés egy 20 oldalas site-hoz. |
| CSS | **Natív CSS custom property + `@layer` + konténer-lekérdezés** | Nulla build-függés a stílusban, a design system 1:1 tokenként él a `:root`-ban. | **Tailwind:** a tokenek a markupba kerülnének, a design system elveszne mint önálló artefaktum. |
| JS | **Vanilla, `type="module"`, progresszív** | A funkciók: téma-kapcsoló, mobil fiók, űrlap-validáció, csúszka, lépcsőzött megjelenés. Ez összesen <6 KB. | **Bármely keretrendszer:** 40–120 KB alapdíj öt apró viselkedésért. |
| Űrlap-backend | **Szerveroldali végpont saját domainen** + rate limit + honeypot + időbélyeg-ellenőrzés | **Egészségügyi kontextusban a beérkező adat különleges adat lehet.** Harmadik feles űrlapszolgáltatóhoz (Formspree, Netlify Forms) küldeni adatfeldolgozói szerződés nélkül kockázat. | **reCAPTCHA:** külső szkript + adattovábbítás; helyette honeypot + időzítés + rate limit. |
| Hosztolás | **CDN-es statikus tárhely**, magyar/EU régió, HTTP/2 vagy /3, brotli | LCP a szekszárdi és pécsi mobilhálózaton dől el | — |

### 9.1b A prototípus fájlszerkezete — és egy konkrét korlát

```
index.html                         →  /
arak/index.html                    →  /arak/
kezelesek/ajakfeltoltes/index.html →  /kezelesek/ajakfeltoltes/
assets/labelle.css                 →  a teljes design system, egy forrásból
assets/labelle.js                  →  a viselkedés, egy forrásból
```

Három oldalnál a CSS beágyazása már triplikáció lenne, ezért a design system
külön fájlba került. Ez egyben a 9.4-es cache-táblázat feltételezéseit is
teljesíti (a HTML revalidál, az eszközök egy évig állnak).

**Konkrét korlát, amit tudni kell:** a JS **nem** `type="module"`, hanem
klasszikus `<script defer>`. Oka: a `file://` protokoll alól a modulbetöltés
CORS-hibára fut minden Chromium-alapú böngészőben, a prototípusnak viszont
dupla kattintásra is működnie kell. Éles környezetben (HTTP) a modul is jó,
és `type="module"`-lal a `defer` viselkedés alapból megvan.

A belső hivatkozások relatívak (`../index.html`), hogy a prototípus fájlból
is bejárható legyen. Éles környezetben ezek tiszta URL-ekre íródnak át
(`/`, `/arak/`, `/kezelesek/ajakfeltoltes/`) — ez a statikus generátor dolga,
nem kézi munka.

### 9.2 Betűkezelés

```
/f/source-serif-4.woff2      variable, wght 200–900, opsz 8–60, subset: latin + latin-ext
/f/schibsted-grotesk.woff2   variable, wght 400–900,           subset: latin + latin-ext
```

- **Subset kötelezően `latin` + `latin-ext`.** A puszta `latin` subsetből hiányzik az
  `ő` és az `ű` — ez a magyar oldalak leggyakoribb betűhibája: a böngésző ilyenkor
  fallback betűből pótolja a két karaktert, ami szemmel láthatóan más rajzolatú.
- Önhosztolt, saját domainről. Nincs `fonts.googleapis.com` hívás: külön DNS + TCP +
  TLS kör, és harmadik felű adattovábbítás.
- `font-display: swap`, `size-adjust` a fallback stackhez az elrendezés-ugrás ellen.
- `<link rel="preload" as="font" type="font/woff2" crossorigin>` **csak a két variable
  fájlra** — több preload rontana.
- Fallback stack: `"Source Serif 4", "Iowan Old Style", Georgia, "Times New Roman", serif`
  és `"Schibsted Grotesk", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`.

### 9.3 Képek

| Tartalom | Formátum | Méretek | Betöltés |
|---|---|---|---|
| Hero (klinikatér, F3) | AVIF + WebP fallback, `<picture>` | 640 / 960 / 1440 / 1920 | `fetchpriority="high"`, **nem** lazy |
| Orvosportré | AVIF/WebP, 4:5 | 400 / 800 | `loading="lazy"` |
| Előtte/utána | AVIF/WebP, azonos vágás és **azonos megvilágítás** | 600 / 1200 | `loading="lazy"`, `decoding="async"` |
| Kezeléskártya-illusztráció | **inline SVG, nem fotó** | — | — |

Minden `<img>`-en kötelező a `width`/`height` vagy a CSS `aspect-ratio` — ez a CLS
egyetlen valódi forrása ezen az oldalon.

**Előtte/utána külön szabály:** azonos objektív, azonos távolság, azonos fényviszony,
azonos arckifejezés. Ha ez nem teljesül, a kép nem bizonyíték, hanem gyanús. Ez tartalmi
előírás, nem technikai.

### 9.4 Cache

| Erőforrás | `Cache-Control` |
|---|---|
| HTML | `public, max-age=0, must-revalidate` |
| `/f/*.woff2` | `public, max-age=31536000, immutable` |
| `/assets/*.[hash].css|js` | `public, max-age=31536000, immutable` |
| Képek hash-elt néven | `public, max-age=31536000, immutable` |
| `/idopont` végpont | `no-store` |

### 9.5 Űrlap

- Metódus: `POST`, `application/x-www-form-urlencoded`, **JS nélkül is működik** (a
  szerver visszaküld egy megerősítő oldalt). A JS csak rárétegzi az inline validációt.
- Mezők: `név*`, `telefon*`, `e-mail`, `kezelés` (select), `mikor jó` (select),
  `üzenet`, `hozzájárulás*` (checkbox).
- `autocomplete="name" | "tel" | "email"`, `inputmode="tel"`, `type="tel"` — hogy mobilon
  a helyes billentyűzet jöjjön.
- **Validáció `blur`-on, nem billentyűleütésre** (`inline-validation`). Küldés után a
  fókusz az első hibás mezőre ugrik (`focus-management`), és a hibalista `role="alert"`
  régióban jelenik meg (`aria-live-errors`).
- Hibaszöveg **okot és megoldást** tartalmaz: nem „Érvénytelen", hanem „A telefonszám
  legalább 9 számjegy legyen — pl. 06 30 123 4567."
- **Nem kér diagnózist, kórtörténetet, fotót.** Ez tudatos: minél kevesebb egészségügyi
  adat kerül az űrlapba, annál kisebb az adatvédelmi felület. A kórtörténet a
  konzultációra való.
- Spamvédelem: rejtett honeypot mező + „gyorsabban küldve, mint 3 mp" szűrő + szerveroldali
  rate limit IP-nként. Nincs CAPTCHA.

### 9.6 Tiltólista a megvalósításban

- ❌ Instagram/Facebook beágyazó szkript (P1). Helyette: statikus kép-rács saját
  kiszolgálásból + link a profilra.
- ❌ Google Fonts CDN.
- ❌ Chat-widget, cookie-consent SaaS harmadik felű szkripttel (a saját, sütimentes
  megvalósítás elég, mert az oldal alapból nem tesz le mérési sütit).
- ❌ Karusszel bármelyik szekcióban (`gesture-conflicts`, és rejtett tartalom).
- ❌ Automatikusan induló videó.

---

## 10. SEO-specifikáció

### 10.1 `title` és `meta description` minták

| Oldal | `<title>` (≤60 kar.) | `<meta description>` (≤155 kar.) |
|---|---|---|
| `/` | `Orvos-esztétika Szekszárdon – La' Belle klinika` | `Tolna vármegye első orvos-esztétikai klinikája. Kezelőorvos: Dr. Imre Laura fogorvos, szájsebész, esztétikai orvos. Csalogány u. 2. Időpontkérés online.` |
| `/kezelesek/ajakfeltoltes/` | `Ajakfeltöltés Szekszárd – La' Belle klinika` | `Hyaluronsavas ajakfeltöltés orvosi kézben, Szekszárdon. Mennyi az 1 ml, mennyi ideig tart, mikor múlik a duzzanat. Ár: [ár]-tól. Időpontkérés.` |
| `/kezelesek/lezeres-szortelenites/` | `Lézeres szőrtelenítés Szekszárd – La' Belle` | `Lézeres szőrtelenítés Szekszárdon, orvos-esztétikai klinikán. Testtájankénti árak, kezelésszám, felkészülés. [ár]-tól.` |
| `/arak/` | `Árak – La' Belle orvos-esztétikai klinika` | `A La' Belle teljes árlistája kezelésenként. Frissítve: [dátum]. Szekszárd, Csalogány u. 2.` |
| `/dr-imre-laura/` | `Dr. Imre Laura – fogorvos, szájsebész, esztétikai orvos` | `Dr. Imre Laura, a szekszárdi La' Belle orvos-esztétikai klinika alapítója. Végzettségek, szakvizsga, továbbképzések.` |

Minden `title` mintája: **`{szándék} {város} – {márka}`**. A várost minden kezelésoldal
címe tartalmazza: a helyi keresés a teljes szándékforgalom ezen a piacon.

### 10.2 Heading-hierarchia (főoldal)

```
h1  Orvos-esztétika Szekszárdon, szájsebészi kézzel.
├ h2  Honnan indulsz?
│  ├ h3 Először jönnék
│  ├ h3 Bőrkezelésre járok
│  └ h3 Férfiaknak
├ h2  Kezelések
│  ├ h3 Injektálásos kezelések
│  │   └ h4 Ajakfeltöltés / Arcfeltöltés / Ráncfeltöltés / Biostimuláció
│  ├ h3 Bőrkezelések
│  └ h3 Készülékes kezelések
├ h2  Az egy milliliter
├ h2  Dr. Imre Laura
├ h2  Eredmények
├ h2  A folyamat a konzultációtól a kontrollig
├ h2  Elérhetőség és nyitvatartás
├ h2  Amit a pácienseink mondanak
├ h2  Időpontkérés
└ h2  Gyakori kérdések
   └ h3 (kérdésenként)
```

Egy `h1`, nincs szintugrás, a vizuális méret és a szint elválik (a `--t-h3` méretet
CSS-osztály adja, nem a taggel érjük el).

### 10.3 Strukturált adat — teljes gráf

Egyetlen `<script type="application/ld+json">`, `@graph` szerkezetben:

| `@type` | `@id` | Mit visz |
|---|---|---|
| `MedicalClinic` (+`LocalBusiness`) | `#klinika` | név, `medicalSpecialty: PlasticSurgery`/`Dermatology`, cím, `geo`, telefon, `openingHoursSpecification`, `priceRange`, `sameAs` (IG, FB, Google) |
| `Physician` | `#orvos` | Dr. Imre Laura, `medicalSpecialty`, `worksFor: #klinika` |
| `AggregateRating` | beágyazva `#klinika`-ba | `5.0` / `52` (F4) — **csak ha a Google-forrás megjelölhető** (10.4) |
| `PostalAddress` | `#cim` | Csalogány u. 2., 7100 Szekszárd, HU |
| `GeoCoordinates` | `#geo` | `[szélesség]`, `[hosszúság]` — placeholder |
| `WebSite` | `#site` | `inLanguage: hu-HU` |
| `WebPage` | `#lap` | `isPartOf: #site`, `about: #klinika` |
| `BreadcrumbList` | `#morzsa` | — |
| `MedicalProcedure` × kezelés | `#kezeles-{slug}` | `name`, `procedureType: NoninvasiveProcedure`, `bodyLocation`, `howPerformed`, `preparation`, `followup` |
| `Offer` × kezelés | `#ar-{slug}` | `price` (placeholder), `priceCurrency: HUF`, `availability` |
| `FAQPage` | `#gyik` | csak a valóban látható kérdésekkel |
| `Organization` | — | a lábléc NAP-jával, `logo` |

**Fontos korlát:** az `AggregateRating` saját oldalon való közlése a Google
irányelvei szerint csak akkor jogszerű, ha az értékelés az oldal saját gyűjtése,
nem másolt Google-adat. **Ezért a prototípusban az 5,0 ★ vizuálisan megjelenik forrás-
megjelöléssel („Google-értékelés"), de `AggregateRating` schemaként csak akkor élesíthető,
ha a klinika saját véleménygyűjtést indít.** Ez a 15. fejezet egyik kérdése.

### 10.4 Local SEO

1. **A Google Cégprofil kategóriája `Kozmetikai vállalat`-ról átállítandó**
   (elsődleges: `Bőrgyógyászati klinika` vagy `Orvosi klinika`; másodlagos: `Kozmetikai
   vállalat`, `Lézeres szőrtelenítő`). Ez **egyetlen kattintás, és a 2.3/S3 szerint a
   legnagyobb hozamú SEO-lépés az egész projektben.**
2. NAP-konzisztencia: pontosan `La' Belle orvos-esztétikai klinika` /
   `7100 Szekszárd, Csalogány u. 2.` / `+36 30 719 1991` — betűre azonosan a weboldalon,
   a Google-profilban, a Facebookon és minden katalógusban (szepsegturul.eu,
   egeszsegturul.eu, cylex.hu, aranyoldalak).
3. A weboldal a Cégprofil „Webhely" mezőjében a **`/`-re**, a „Foglalás" mezőjében a
   **`/idopont/`-ra** mutasson.
4. Google Business-bejegyzések: a szabadságközlemények (F2) ide is menjenek ki, ne csak
   IG-re — a Google-profil a legtöbbek első érintkezési pontja.
5. `hreflang` nem kell (egynyelvű), de `<html lang="hu">` és `og:locale=hu_HU` igen.
6. Beágyazott térkép **iframe nélkül**: statikus térképkép + link. Az iframe harmadik
   felű szkript és sütikockázat.

### 10.5 Előtte/utána képek — jogi és GDPR-keret

Ez nem SEO, de itt a helye, mert a tartalomstratégia része. **Nem jogi tanács, hanem
ellenőrizendő pontok listája:**

- Az arcképmás **egészségügyi kontextusban különleges adat** (GDPR 9. cikk). Külön,
  írásbeli, célhoz kötött, visszavonható hozzájárulás kell — a kezeléshez adott
  beleegyezés **nem** fedi le a marketingcélú közzétételt.
- A hozzájárulásnak ki kell terjednie a felületre (weboldal, IG, FB) és a
  visszavonhatóságra. Visszavonás esetén a képet minden felületről törölni kell.
- Az egészségügyi szolgáltatók reklámjára a Grtv. (2008. évi XLVIII. tv.) és a
  96/2003. (VII. 15.) Korm. rendelet is vonatkozik. **Ügyvédi ellenőrzés kell** arra,
  hogy az eredményközlés nem minősül-e megtévesztő gyógyhatás-állításnak.
- Ajánlott a képek mellett kötelező kísérőszöveg: *„Egyedi eredmény, a páciens írásos
  hozzájárulásával. Az eredmény személyenként eltérhet."*

### 10.6 Készítménynevek — konkrét megkötés

A **vényköteles készítmények neve a lakosságnak szóló reklámban nem használható**
(Gyftv., 2005. évi XCV. tv.). A botulinum toxint tartalmazó készítmények vénykötelesek.
Ezért:

- ❌ márkanév a `title`-ben, `h1`-ben, URL-ben, alt-szövegben, IG-poszt szövegében;
- ✅ `Ráncfeltöltés` / `Mimikai ráncok kezelése` mint szolgáltatásnév;
- ✅ a hatóanyag megnevezése a konzultáción, nem a hirdetésben.

**Ez SEO-veszteség** (a márkanévre nagy a keresés), és ezt vállalni kell. Az URL ezért
`/kezelesek/rancfeltoltes/`.

---

## 11. Performance-célok

Mérési alap: **mobil, 4× CPU-lassítás, Slow 4G**, Lighthouse + valós CrUX.
A célok a **75. percentilisre** vonatkoznak.

| Metrika | Cél | Miért ez a szám | Hogyan érjük el |
|---|---|---|---|
| **LCP** | **≤ 1,8 s** | A „jó" küszöb 2,5 s; egy statikus oldalnál ez nem teljesítmény, hanem alapszint. Az LCP-jelölt a **H1 szöveg**, nem a hero kép. | kritikus CSS inline (≤14 KB), betű `preload` + `swap`, hero kép `fetchpriority=high`, nulla renderelést blokkoló JS |
| **CLS** | **≤ 0,02** | 0,1 a küszöb, de ezen az oldalon nincs hirdetés és beágyazás, tehát 0 közeli reális | minden `<img>`-en `width`/`height`, `size-adjust`-olt fallback betű, a szignatúra elem `aspect-ratio`-s doboza, fix magasságú fejléc |
| **INP** | **≤ 120 ms** | 200 ms a küszöb; a legnehezebb interakció a csúszka | a csúszka `input`-kezelője két attribútumot ír; nincs elrendezés-olvasás; passzív eseményfigyelők |
| **TTFB** | ≤ 200 ms | statikus fájl CDN-ről | EU-régiós CDN, HTTP/3 |
| **FCP** | ≤ 1,2 s | — | — |

**Súlybüdzsé (főoldal, brotli után, kompresszált):**

| Erőforrás | Büdzsé | Megjegyzés |
|---|---|---|
| HTML (kritikus CSS-sel) | **≤ 18 KB** | a prototípusban a CSS már külön fájl; élesben a hajtás feletti rész inline-olandó |
| CSS (megosztott, `assets/labelle.css`) | ≤ 8 KB | 42 KB nyers, brotli után ennek töredéke; oldalak közt cache-elt |
| JS (összes, `assets/labelle.js`) | **≤ 6 KB** | 10,0 KB nyers / **~3,4 KB gzip**, hét viselkedés, nulla függőség |
| Betűk (2 × variable woff2, latin+latin-ext) | ≤ 70 KB | ez a legnagyobb tétel — indokolt |
| Hero kép AVIF | ≤ 45 KB | 1440px szélességnél |
| Egyéb képek (lusta) | nem számít az elsődleges terhelésbe | |
| **Első terhelés összesen** | **≤ 140 KB** | |

**Harmadik felű kérés a főoldalon: 0.** Ez a legfontosabb szám az egész táblázatban.

---

## 12. CRO — konverziós elemek

Konverzió = **elküldött időpontkérés**. Másodlagos = **hívás**.

| # | Elem | Hol | Miért működik |
|---|---|---|---|
| C1 | A H1 nevesíti a képesítést („szájsebészi kézzel") | hero | A kockázatérzetet oldja, nem vágyat kelt. Ez a **kategóriaváltás** (3.2) egyetlen mondatban: a látogató nem kozmetikust néz. |
| C2 | `5,0 ★ · 52 értékelés` a hajtás alatt közvetlenül | tényszalag | Társas bizonyíték az árinformáció **előtt**. Az 52-es szám kisvárosi kontextusban nagy — ki kell írni a darabszámot, a csillag önmagában értéktelen. |
| C3 | Három belépőkártya | 4. szekció | Önszelekció. A látogató saját magát sorolja be, ezzel elköteleződik a további olvasásra (foot-in-the-door). |
| C4 | Ár a kezeléskártyán, `-tól` alakban | kezelésrács | Az árelrejtés az orvos-esztétikában a legnagyobb kilépési ok. A `-tól` megtartja a konzultáció szerepét, de leveszi a „biztos drága" gyanút. |
| C5 | **Szignatúra: „Az egy milliliter"** | 6. szekció | A vásárlás előtti fő félelmet („meg fog látszani") oldja, méghozzá saját kezű interakcióval. Aki hozzáér, tovább marad. |
| C6 | „Kinek nem ajánlott" szekció | kezelésoldal | Ellentmondásos, de bizonyítottan bizalomnövelő: aki visszautasít, azt hisszük el. Egyben előszűri az alkalmatlan érdeklődőt, ami az orvos idejét spórolja. |
| C7 | Gyógyulási idővonal | kezelésoldal | A ki nem mondott kérdés: „mikor mehetek vissza dolgozni". Ez sokszor fontosabb az árnál. |
| C8 | „Mit kapsz vissza" doboz az űrlap mellett | űrlap | Kockázatmentesítés a küldés pillanatában: válaszidő, nem kötelez semmire. Az űrlap melletti szöveg mérhetően emeli a kitöltést. |
| C9 | Hozzájárulás-checkbox **magyarázó szöveggel**, nem jogi paragrafussal | űrlap | A jogi szöveg falak elé állítja a szorongó felhasználót. Egy mondat + link jobb. |
| C10 | Fix alsó sáv mobilon: `Hívás` + `Időpontkérés` | mobil, globális | A mobilforgalom nem az űrlapig görget. Két hüvelykujj-távolságú gomb bármely pontról. |
| C11 | Elérhetőség-jelző valós állapottal (nyitva / zárva / szabadság) | 10. szekció + lábléc | Megszünteti a „hiába írok" bizonytalanságot (U4). Őszinte „most szabadságon vagyok" **jobban** konvertál, mint a hallgatás — mert megmondja, mikor érdemes visszatérni. |
| C12 | Két telefonszám címkézve | lábléc, kapcsolat | U5. Egy rossz számra futó hívás elveszett páciens. |
| C13 | A `/arak/` oldalon **frissítés dátuma** | árak | K2 közvetlen orvoslása. A dátum jelenléte önmagában bizalmi jelzés. |

**Amit szándékosan NEM teszek bele:** visszaszámláló, „még 2 hely maradt", felugró
kedvezményablak, kilépési szándék popup. Egy egészségügyi szolgáltatónál a
sürgetéstechnika a kompetenciaérzetet rombolja — pontosan azt, amire az egész
pozicionálás épül.

---

## 13. Design-döntések összefoglaló táblázata

| # | Döntés | Alternatíva | Miért nem az alternatívát |
|---|---|---|---|
| D1 | Vizuális kiindulópont: a saját kezelőtér anyaga (márvány, acél, körlámpa) | „luxus szépségszalon" arany-rózsaszín; vagy „orvosi" türkiz-fehér | Mindkettő kategóriaklisé. Az egyik lefelé (kozmetikus), a másik oldalra (állami rendelő) pozicionál. A saját tér már ma is drágább képet mutat, mint bármelyik sablon. |
| D2 | Egyetlen meleg akcentus (`#8A5A28` / `#E0A868`) hideg semlegesen | a gépi javaslat `#0891B2` türkiz + `#16A34A` zöld | Brief-tiltás („zöld, ha egészség") + a türkiz az állami egészségügy kódja |
| D3 | Source Serif 4 + Schibsted Grotesk | Playfair Display + Inter | Brief-tiltás; ezen felül a Playfair vékony vonalai kis méretben eltűnnek, és a teljes szépségipar ezt használja |
| D4 | Sötét mód: az akcentus **melegebb és világosabb** lesz | akcentus egyszerű invertálása | Az invertált akcentus hideggé válna, és megtörné a koncepciót („a lámpa marad meleg"). Az invertálás emellett kontraszthibát is szül. |
| D5 | Szignatúra: életnagyságú, kalibrálható dózisskála | before/after slider (a szakma szokásos „merész" eleme) | A before/after slider (a) fotófüggő, (b) GDPR- és reklámjogi terhet visel (10.5), (c) minden versenytárs oldalán ott van, tehát nem megjegyezhető |
| D6 | Ár `-tól` alakban a kártyán | ár teljes elrejtése konzultációig | Az árelrejtés az első számú kilépési ok. A `-tól` kompromisszum: informál, de nem ígér. |
| D7 | „Kinek nem ajánlott" szekció minden kezelésnél | csak előnyök | A visszautasítás hitelesíti az állítást; egyben előszűr |
| D8 | Fix alsó sáv mobilon `Hívás`-sal az első helyen | csak `Időpontkérés` | A telefon a ma működő csatorna (F1). Egy szokást nem szabad erőszakkal kivenni, csak alternatívát mellé tenni. |
| D9 | Nulla harmadik felű szkript, IG-beágyazás helyett statikus rács + link | hivatalos IG-beágyazás | ~1,2 MB és a Core Web Vitals bukása egyetlen szekcióért |
| D10 | Statikus generálás, saját űrlap-végpont | WordPress; vagy külső űrlapszolgáltató | Egészségügyi kontextusban a beérkező adat különleges adat lehet — külső feldolgozóhoz csak szerződéssel |
| D11 | Egy kezelés = egy URL | egyetlen hosszú „szolgáltatásaink" oldal | Kezelésenként külön keresési szándék és külön ár; egy oldalon nincs mire rangsorolni |
| D12 | A kiemelt storyk 1:1 leképezése sitemapre | „szakmailag logikus" saját csoportosítás | A storyk sorrendjét a valós kereslet alakította ki — ez ingyen kapott felhasználókutatás (J5) |
| D13 | Nincs pulzáló „élő" pont az elérhetőség-jelzőn | pulzáló pont, mint a legtöbb oldalon | Sürgősséget hazudik, és `prefers-reduced-motion` alatt úgyis kikapcsol — akkor viszont információt veszít |
| D14 | Nincs karusszel sehol | eredmény- és véleménykarusszel | Rejtett tartalom + gesztusütközés mobilon |
| D15 | Az LCP-jelölt a H1 szöveg, a hero kép mobilon a szöveg **alatt** van | képes hero felül, szöveggel ráírva | Szövegre írt kép: kontrasztkockázat, LCP-terhelés, és mobilon a felső 100vh-ból kiszorul a lényeg |
| D16 | Márkanév-tiltás a ráncfeltöltésnél, vállalt SEO-veszteséggel | a keresett márkanév használata | Gyftv. — vényköteles készítmény nem reklámozható a lakosságnak (10.6) |
| D17 | Az `/arak/` **katalógus-táblázat**, kategóriánként | 3 sávos „csomagkártya" a legnépszerűbbet kiemelve (a `ui-ux-pro-max` landing-domain `Pricing Page + CTA` mintája) | Az a minta SaaS-előfizetésre való: ott a felhasználó *csomagot választ*. A klinikán a páciens nem csomagot választ, hanem **egy kezelést keres és megnézi az árát**. A csomagkártya itt hamis választást kényszerítene, és eltakarná a 40+ tételes valóságot. A táblázat viszont Ctrl+F-elhető, oszlopba állítja a számokat és nyomtatható. |
| D18 | Ugrósáv (horgonysáv) ragadósan a fejléc alatt, `IntersectionObserver`-es aktív állapottal | oldalsó tartalomjegyzék; vagy semmi | A skill `Navigation / Active State` szabálya: a jelenlegi hely legyen jelölve. Oldalsó TOC mobilon eltűnne — az ugrósáv mindkét nézetben ugyanaz a komponens, +0,4 KB JS. |
| D19 | **Gyógyulási idővonal** a kezelésoldalon, nem szövegbekezdés | „a duzzanat 2–3 nap alatt lemegy" mondat a folyószövegben | A „mikor mehetek vissza dolgozni" gyakran fontosabb az árnál (12/C7). Sávként az idő és a láthatóság *egyszerre* leolvasható; szövegben nem. Tiszta CSS, nulla JS, nulla kép. |
| D20 | Az akcentusszín az **állítást** jelöli, a halk tónus a **korlátot** | pipa és X ugyanabban az akcentusban | Ha a „mire jó" és a „mire nem" listája azonos színű, a szín elveszti a jelentését. A forma (pipa/X) és a tónus együtt hordozza — a szín soha nem egyedüli hordozó. |
| D21 | A design system külön `assets/labelle.css`-be | oldalanként beágyazott `<style>` | Három oldalnál a beágyazás triplikáció, és a tokenek szétcsúsznának. Éles környezetben a kritikus CSS ebből emelhető ki inline-ba (11. fejezet). |

---

## 14. Bevezetési ütemterv

| Fázis | Tartalom | Feltétel a start előtt | Becsült idő |
|---|---|---|---|
| **0. Azonnali, kód nélkül** | Google Cégprofil kategória átállítása (`Kozmetikai vállalat` → orvosi kategória); NAP egységesítése minden katalógusban; a `2025 árak` story átnevezése `Árak`-ra | semmi | 1 nap |
| **1. Alap** | Domain, tárhely, design system implementálás, `/`, `/kezelesek/` hub, `/arak/`, `/dr-imre-laura/`, `/kapcsolat/`, `/idopont/` + űrlap-végpont, jogi oldalak, schema-gráf | árlista, orvos-adatok, nyitvatartás, GDPR-tájékoztató (15. fejezet) | 2–3 hét |
| **2. Kezelésoldalak** | 12 kezelésoldal a 5.2 sablonnal, kezelésenkénti GYIK, `MedicalProcedure` schema | kezelésenkénti szakmai szöveg az orvostól | 2 hét |
| **3. Bizonyíték** | `/eredmenyek/` galéria, `/a-klinika/`, `/zo-skin-health/`, saját véleménygyűjtés indítása (10.3) | **ügyvédi ellenőrzés + páciens-hozzájárulási minta** | 1–2 hét |
| **4. Mérés és finomítás** | valós CrUX-adat, űrlap-elhagyás mérése, A/B a hero H1-en | 4–6 hét éles forgalom | folyamatos |
| **5. Opcionális** | `/tudastar/`, online naptáras foglalás (nem csak kérés), hírlevél | eldöntendő, van-e rá kapacitás | — |

**A 3. fázis nem indulhat a jogi ellenőrzés előtt.** Ez az egyetlen kemény függőség a
tervben.

---

## 15. Nyitott kérdések — ehhez ügyfél-input kell

Csoportosítva aszerint, hogy melyik fázist blokkolja.

### 15.1 Az 1. fázist blokkolja

1. **Mi a jelenlegi weboldal URL-je**, és mi van rajta? (A Google „Webhely" gombot jelez;
   a domaint nem sikerült azonosítani. Új domain kell, vagy meglévőt költöztetünk?)
2. **A teljes, aktuális árlista** kezelésenként. A prototípusban minden ár placeholder.
   Az IG-akciós poszt (F2) `128.500 Ft → 90.000 Ft` értékei akciósak és lejártak — nem
   használom listaárként.
3. **Pontos nyitvatartás** minden napra. A Google csak a „zárás 16:00"-t adja.
4. **Dr. Imre Laura hivatalos adatai:** diploma (intézmény, év), szájsebész szakvizsga
   (év), esztétikai orvosi képzés (hol, mikor), **működési nyilvántartási szám**,
   kamarai tagság. Ezek nélkül a `/dr-imre-laura/` oldal csak állítás.
5. **Hány éve működik a klinika**, és hány éve praktizál az orvos? (A tényszalag
   `[X] éve` mezője.)
6. **A klinika hivatalos neve, székhelye, adószáma, ÁNTSZ/NNK működési engedélyének
   száma** — impresszumhoz és a `MedicalClinic` schemához.
7. **Ki válaszol az űrlapokra, és milyen válaszidőt vállalunk?** A „Mit kapsz vissza"
   doboz (C8) konkrét szám nélkül nem működik.
8. **Hova menjen az űrlap:** e-mail (`laura.imre.5@gmail.com` — **ez nem alkalmas
   egészségügyi kontextusú megkeresésre**, saját domainű postafiók kell), vagy
   praxiskezelő rendszer?
9. **GDPR adatkezelési tájékoztató** — van-e, ki készítette, mikor frissült?
10. **Melyik a végleges kezeléslista?** A 4.2-es 12 tétel az IG-tartalomból rekonstruált.
    Van-e olyan, ami nincs benne, vagy olyan, amit már nem csinál?
11. **A logó vektoros formátumban**, és hogy pontosan `La' Belle` vagy `La'Belle` az
    írásmód. (Az IG bio és a Google-találat eltér.) — **a brief „amit nem szabad
    megváltoztatni" mezője üres volt, ezt itt kérdezem vissza.**

### 15.2 A 2. fázist blokkolja

12. Kezelésenként: **átlagos időtartam, érzés/fájdalom leírása, downtime**, tartósság,
    ajánlott kezelésszám. Ezt csak az orvos tudja megadni, és nem szabad kitalálni.
13. **Kinek nem ajánlott** — kezelésenkénti ellenjavallati lista (D7). Szakmai tartalom.
14. Az „Az egy milliliter" szekció szövege — a *„a különbség a természetes és a feltűnő
    között gyakran fél milliliter"* mondat **szakmai jóváhagyást igényel**. Ha az orvos
    nem vállalja, semlegesebb változat kell.
15. Használ-e a klinika lézeres szőrtelenítéshez konkrét, nevesíthető készüléket?
    (A F2-es fotón látszik egy eszköz, de nem azonosítható.) A készüléknév erős
    keresési horgony.

### 15.3 A 3. fázist blokkolja

16. **Ügyvédi állásfoglalás** az előtte/utána képek közléséről és a hozzájárulási
    mintáról (10.5).
17. Van-e írásos hozzájárulás a **már közzétett** IG-képekhez? Ha nincs, azok
    átemelése a weboldalra nem javasolt.
18. Indul-e **saját véleménygyűjtés**? Enélkül az `AggregateRating` schema nem
    élesíthető (10.3), csak a vizuális 5,0 ★ marad forrásmegjelöléssel.
19. A F2-es közös fotó egy külföldi kollégával (a felirat alapján `Dr. Zach A…`,
    háttérben `CU… ZAG…`) — **nem azonosítottam**, ezért nem is állítok róla semmit.
    Ha ez egy külföldi továbbképzés, az a `/dr-imre-laura/` oldal erős tartalma.

### 15.4 Üzleti döntés

20. **Időpontkérés vagy valódi online foglalás?** A kérés kevesebb kockázat, de marad
    egy kézi lépés. A naptáras foglaláshoz vezetett szabad kapacitás kell.
21. Akarunk-e **kiskereskedelmi webshopot** a ZO Skin Health termékekre, vagy marad a
    „bolti" bemutatás? (Ez külön projekt, külön jogi felület.)
22. A **„modell" akciók** (F2) beépüljenek-e az oldalba egy `/modell/` oldalként, vagy
    maradjanak IG-exkluzívnak? (Előny: olcsó lead. Hátrány: árlehorgonyzás lefelé.)

---

## 16. Az anyag leggyengébb pontja — őszintén

**A leggyengébb pont az, hogy a bemeneti adat egy Instagram-profil képernyőképe.**

Konkrétan:

1. **Nem láttam a jelenlegi weboldalt.** A 2. fejezet „Kritikus" sora — hogy nincs
   indexelhető saját tartalom — abból következtetett állítás, hogy négy különböző,
   vásárlási szándékú lekérdezésre egyetlen La' Belle-találat sem jött vissza. Ez erős
   jel, de nem bizonyíték. Ha kiderül, hogy van egy működő, indexelt oldal, a 2. fejezet
   egy részét újra kell írni. **A 15.1/1. kérdés ezért az első.**

2. **A célközönség-szegmentálás (0.2) rekonstrukció, nem kutatás.** Három csoportot
   vezettem le abból, hogy milyen posztok vannak a rácson. Ez lehet, hogy pontosan
   megfelel a valóságnak, és lehet, hogy a klinika forgalmának 70%-a valójában egyetlen
   szegmensből jön, amiről az IG nem árulkodik. **A teljes 4. szekció (a három
   belépőkártya) ezen a bizonytalan alapon áll.** Egy 20 perces beszélgetés az orvossal
   megerősítené vagy megdöntené — és ez a legolcsóbb validáció az egész projektben.

3. **Nulla valós ár van a dokumentumban.** Az árstratégia (C4: `-tól` árak a kártyán)
   elvben helyes, de az, hogy a **konkrét** számok hogyan hatnak, csak akkor derül ki,
   ha látjuk őket. Ha az árszint jelentősen a pécsi klinikák felett van, a `-tól` ár
   kiírása ronthat is a konverzión — akkor előbb kell jönnie a kompetencia-érvnek.

4. **A szignatúra elem szövege szakmailag nincs jóváhagyva.** A „fél milliliter"
   megfogalmazás (15.2/14.) az én állításom a szakma általános gyakorlatáról, nem a
   La' Belle protokollja. A vizuális megoldás a jóváhagyástól függetlenül áll, de a
   kísérőmondat nem élesíthető orvosi ellenőrzés nélkül.

5. **A jogi fejezetek (10.5, 10.6) ellenőrzésre szánt listák, nem jogi tanács.** A
   megkötések irányát biztosra veszem, de a pontos alkalmazást ügyvédnek kell megnéznie.
   Ha a márkanév-tiltásban tévedek, a 3. fejezet SEO-lemondása (D16) fölöslegesen vitt
   el forgalmat.

6. **A prototípus egyfájlos, önhosztolt betűk nélkül.** A `index.html` a rendszerbetűkre
   esik vissza, ha nincs telepítve a Source Serif 4 / Schibsted Grotesk. A tipográfiai
   döntés (7.2) tehát a prototípusban **nem látszik teljes valójában** — ezt a fájl
   fejlécének megjegyzése is kimondja. Az élesítés első lépése a két woff2 subsetelése.

### 16.1 Ami a második körben (aloldalak) romlott vagy nem oldódott meg

7. **A kezelésoldal szerkezete kész, a tartalma nem.** Az `/kezelesek/ajakfeltoltes/`
   oldalon a komponensek élesek (idővonal, dobozpár, lépéslista, GYIK, schema),
   de a **szakmai szöveg minden pontján placeholder áll**: javallat,
   ellenjavallat, fájdalom, downtime, tartósság. Ezt szándékosan nem töltöttem
   ki — orvosi állítást kitalálni ennél a szolgáltatásnál nem apró hiba, hanem
   a legsúlyosabb, amit egy ilyen oldalon el lehet követni. **Következmény:
   az oldal jelen állapotában nem élesíthető, csak bemutatható.**

8. **A gyógyulási idővonal fokozatai (0–2 óra … 2 hét) az én becsléseim
   a szakma általános gyakorlatáról.** A komponens működik, a beosztás
   szemléltető. Ha az orvos más ütemet ad meg, a sávok és a `datetime`
   attribútumok is átírandók — nem csak a szöveg.

9. **Az árlista 40+ tétele rekonstruált kezeléslista.** Az IG-tartalomból és
   a katalógusokból következtettem rá, hogy mit csinál a klinika, és ebből
   képeztem az egységeket (0,5 ml / 1 ml / 1 alkalom / 4 alkalom / testtáj).
   Elképzelhető, hogy a klinika máshogy tagolja az árait — pl. testtájankénti
   bérletekkel vagy csomagokkal, amikről nincs adatom. **A táblázat
   szerkezete könnyen átrendezhető, de az egységek megválasztása feltevés.**

10. **Az ugrósáv aktív állapota `IntersectionObserver`-rel dolgozik, nem a
    görgetési pozícióval.** Rövid szakaszoknál (pl. `#mennyiseg`) ez pontatlan
    lehet: ha két szakasz egyszerre látszik, az elsőt jelöli. Ez tudatos
    egyszerűsítés a JS-büdzsé miatt; ha zavaró, egy pontosabb megoldás
    ~0,6 KB-tal többe kerül.

11. **A `web-artifacts-builder` skillt nem használtam, és ezt vállalom.**
    A most telepített új skill React + Tailwind + shadcn/ui alapú, összetett
    claude.ai-artifactekre való, és a saját leírása is kimondja, hogy nem
    egyszerű, egyfájlos HTML-hez készült. Ez a projekt viszont éppen arra
    épül, hogy **nulla külső függőség, nulla harmadik felű kérés és ≤6 KB JS**
    legyen (11. fejezet) — egy React+Tailwind réteg ennek a specifikációnak
    mindhárom pontját megsértené egy 20 oldalas statikus klinikaoldalon.
    A `ui-ux-pro-max` skillt viszont ténylegesen lekérdeztem, és a
    D17–D20 döntések ebből származnak — a `Pricing Page` mintáját is
    megnéztem, és **indoklással elvetettem**, nem figyelmen kívül hagytam.

**Amit ebből érdemes elvinni:** a stratégiai váz (kategóriaváltás kozmetikusból
klinikába, aszinkron kapacitás, kezelésenkénti URL) még akkor is áll, ha a fenti hat
pont mindegyikében tévedek részben. A **számok és a szövegek** viszont nem élesíthetők
a 15. fejezet kitöltése nélkül.
