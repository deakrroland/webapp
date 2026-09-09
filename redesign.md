# Diana Vendéglő, Pécs — UI/UX redesign koncepció és működő prototípus

> **Módszertani figyelmeztetés — rekonstrukcióból dolgoztam.**
> A `dianavendeglo.hu`, az `etterem.hu`, a `foodora.hu`, a `wolt.com`, a `menuzz.hu`
> és az `ittjartam.hu` közvetlen lekérése ebben a környezetben hálózati szinten
> tiltott (egress proxy: `EGRESS_BLOCKED`). Az elemzés a keresőben **indexelt**
> tartalomra, a SERP-ben látható `<title>`-ekre és URL-ekre, a briefben beillesztett
> Google-listingre, valamint a pécsi sajtó (pecsaktual.hu, pecsma.hu) és a
> katalógusoldalak (hovamenjek.hu, utazzitthon.hu, vendeglatasinfo.hu) indexelt
> szövegére épül.
>
> Minden ténymegállapítás mellett jelölöm a bizonyosság szintjét:
> **[T]** = több forrásból megerősített tény · **[V]** = valószínű, ellenőrizendő ·
> **[P]** = placeholder, ügyfél-input kell hozzá.
>
> Amit **nem** tudtam mérni: Core Web Vitals, HTML-forrás, CSS, képméretek,
> HTTPS-konfiguráció, meglévő JSON-LD. Ezekről a 2. és 11. fejezetben külön
> jelzem, hogy mit kell megmérni élesítés előtt. **Egyetlen számot sem találtam ki.**

---

## Kontextus — amit a briefből és a kutatásból tudok

A brief kontextus-mezői üresen érkeztek, ezért nem töltöttem ki őket találgatással.
Amit dokumentáltan tudok az ügyfélről:

| Mező | Érték | Forrás / bizonyosság |
|---|---|---|
| Cég | Diana Vendéglő, 7632 Pécs, Diana tér 10. | Google-listing, saját domain [T] |
| Nyitás | **1982. május 1.** | pecsaktual.hu / pecsma.hu [T] |
| Vezetés | Racskó Gábor 2003 óta vezeti, 1994-ben került ide pincérként | pecsaktual.hu [T] |
| Konyha | magyaros, házias; helyi kistermelők friss alapanyagai | saját oldal indexelt szövege [T] |
| Kapacitás | **130 fő** vendéglő, **45 fő** leválasztható különterem, **120 fő** kerthelyiség | utazzitthon.hu, hovamenjek.hu [T] |
| Nyári konyha | vaslapon, grillen, parázson, bográcsban, vendégek előtt | utazzitthon.hu [T] |
| Zene | egész évben esti élőzene; rendszeres **szombat esti retro élőzenés** program, à la carte fogyasztással | hovamenjek.hu [T] |
| Napi menü | egy hétre előre publikált heti menü | saját oldal [T] |
| Nyitvatartás | H–Cs 11–22, P–Szo 11–23, V 11–22 | nyitva.hu + saját oldal [T] |
| Elérhetőség | (06 72) 438 176 · dvendeglo@gmail.com | saját oldal [T] |
| Fizetés | bankkártya, SZÉP-kártya | etterem.hu listing [T] |
| Kiszállítás | Wolt és Foodora | platform-listingek [T] |
| Google | 4,2 ★ / 910 értékelés · 2000–6000 Ft/fő · „Bejelentette 84 személy" | brief [T] |
| Attribútumok | kedvezményes ételek, különterem, vegán lehetőségek | Google-listing [T] |
| Rendezvénytípusok | lakodalom, bál, ballagás, szalagavató, diplomaosztó, céges | hovamenjek.hu, saját oldal [T] |
| Versenytársak | nincs megadva | **[P]** |
| Célközönség pontos profilja | nincs megadva | **[P]** |
| Az oldal EGY dolga | nincs megadva → **feltételezésem: rendezvény-ajánlatkérés**, indoklás a 12. fejezetben | **[P]** |
| Amit nem szabad megváltoztatni | nincs megadva → **a „Diana Vendéglő" nevet és a Diana-alakot érintetlenül hagytam** | **[P]** |

A hiányzó mezők a 15. fejezetben, kérdés-formában szerepelnek.

---

## 1. A jelenlegi oldal elemzése

### 1.1 Technológia

| Megállapítás | Bizonyíték | Szint |
|---|---|---|
| WordPress | Minden indexelt URL a `dianavendeglo.hu/**wp/**…` alkönyvtár alatt van (`/wp/`, `/wp/etel/`, `/wp/ital/`, `/wp/napi-menu/`, `/wp/rendezvenyek/`, `/wp/ajanlatok-aktualitasok/`) — ez a klasszikus „WordPress a `/wp/` mappába telepítve, a gyökér nem lett átirányítva" minta | [T] |
| Klasszikus többoldalas struktúra, nem SPA | Minden menüpont önálló, indexelt URL | [T] |
| Nincs nyelvi verzió | Csak magyar URL-ek és címek indexeltek | [V] |
| Sablonos, nem egyedi téma | A SERP-címek automatikusan generált mintája (lásd 2.3) sablon-viselkedésre utal | [V] |
| Kép- és teljesítményjellemzők | **nem mérhető** ebben a környezetben | — |

### 1.2 Struktúra (a valós, indexelt sitemap)

```
dianavendeglo.hu/wp/                        Főoldal
dianavendeglo.hu/wp/etel/                   Étel
dianavendeglo.hu/wp/ital/                   Ital
dianavendeglo.hu/wp/napi-menu/              Napi menü
dianavendeglo.hu/wp/rendezvenyek/           Rendezvények
dianavendeglo.hu/wp/ajanlatok-aktualitasok/ Ajánlatok, aktualitások
```

A Google Cégprofil ezen felül két külön deep linket hirdet: **„Menü · dianavendeglo.hu"**
és **„Asztal foglalása · dianavendeglo.hu"**.

### 1.3 MI A JÓ BENNE — külön szedve, és ezt mind megtartom

Ez nem udvariassági fejezet. Öt olyan dolog van a jelenlegi oldalon, amit egy
redesign könnyen kidobna, pedig ezek tartják el az egészet.

1. **Saját domain, nem Facebook-oldal.** 2026-ban is meglepően sok pécsi vendéglő
   csak Facebookon él. A Diana indexelhető, linkelhető, mérhető. **Megtartva.**
2. **Külön Napi menü oldal, egy hétre előre feltöltve.** [T] Ez az oldal
   *forgalmi motorja*: heti visszatérő keresés („napi menü Pécs"), heti friss
   tartalom, heti ok a visszatérésre. A legtöbb vendéglő ezt nem csinálja meg,
   vagy csak Facebook-posztban. **Megtartva, és a főoldalra is felhozva.**
3. **A tartalmi felosztás pontosan úgy tagol, ahogy a vendég dönt.**
   „Mit eszem" (Étel) / „mit iszom" (Ital) / „mennyiért ma" (Napi menü) /
   „hol tartsam a ballagást" (Rendezvények). Ez helyes információs modell,
   nem a szervezeti ábra leképezése. **Megtartva** — csak az Étel+Ital kettőt
   vonom össze (indoklás: 4.2).
4. **A Google Cégprofil rendben van karbantartva.** Nyitvatartás, árszint,
   attribútumok, 910 értékelés 4,2 átlaggal, és a profil *vissza is linkel*
   a menüre és a foglalásra. Ez a helyi SEO nehezebbik fele, és kész van.
   **Megtartva, és a weboldal adataival szinkronba hozva.**
5. **WordPress.** Nem hibás választás egy vendéglőnek: a heti menüt a személyzet
   fejlesztő nélkül tudja frissíteni. Egy Next.js-re költöztetés a heti
   menüfrissítést fejlesztői feladattá tenné — pontosan azt rontaná el, ami ma
   működik. **Megtartva** (indoklás: 9.1).

Ezen felül a *tartalom* alapanyaga is megvan: kapacitásszámok, kistermelői
beszerzés, 1982-es alapítás, szombati retro élőzene. Ezek dokumentált tények —
a redesign nagyrészt nem újat ír, hanem **előreveszi, ami el van temetve**.

---

## 2. Problémalista bizonyítékkal

### 2.1 Kritikus

| # | Probléma | Bizonyíték | Szint |
|---|---|---|---|
| K1 | **Minden URL a `/wp/` alatt van.** A gyökér (`dianavendeglo.hu/`) nem a főoldalt szolgálja ki, vagy nem 301-el rá. | Az összes indexelt URL `/wp/`-vel kezdődik | [T] |
| K2 | **A `/wp/` szegmens elárulja a CMS-t és a telepítési útvonalat**, ami felesleges támadási felület-információ, és minden megosztott link 4 karakterrel zajosabb. | ugyanaz | [T] |
| K3 | **Nincs online foglalás, csak telefon.** A Google „Asztal foglalása" linkje a saját oldalra mutat, de az indexelt oldalstruktúrában nincs foglalási aloldal. | Nincs `/asztalfoglalas` vagy `/foglalas` indexelt URL | [V] |
| K4 | **Nincs önálló rendezvény-ajánlatkérő út.** Egyetlen `/rendezvenyek/` oldal fedi a lakodalmat, ballagást, céges vacsorát — pedig ezek külön keresések és külön döntési logikák. | egy URL, hat rendezvénytípus | [T] |
| K5 | **Nincs strukturált adat.** Nem tudom lekérni, de a SERP-ben nem jelenik meg sem menü-, sem étterem-rich result. | SERP-megfigyelés | [V] |

### 2.2 UX

| # | Probléma | Bizonyíték | Szint |
|---|---|---|---|
| U1 | **A vendég legfontosabb kérdésére — „most nyitva vagytok?" — az oldal nem válaszol azonnal.** A nyitvatartás katalógusoldalakon van jól kiemelve, nem a sajátján. | A nyitvatartást a nyitva.hu és az etterem.hu SERP-snippetje adja vissza, nem a `dianavendeglo.hu` | [V] |
| U2 | **A 130 / 45 / 120 fős kapacitás nincs a döntési pontnál.** Ez a rendezvényszervező *egyetlen* kizáró kritériuma, mégis csak katalógusoldalakon olvasható jól. | a számok az utazzitthon.hu és hovamenjek.hu szövegében jelennek meg, nem a saját oldal SERP-snippetjeiben | [V] |
| U3 | **Az „Ajánlatok, aktualitások" oldal örök karbantartási adósság.** Az ilyen oldal 3 hét után elavul, és elavultan rosszabb, mint ha nem lenne. | oldalcím önmagában | [T] |
| U4 | **Étel és Ital két külön oldal.** Senki nem keres „ital"-ra; „étlap"-ra keres. Két kattintás egy döntéshez. | két külön indexelt URL | [T] |
| U5 | **A 43 éves történet nincs sehol az oldalon.** Az 1982-es nyitás, a napi élőzene, a „csak asztalfoglalással lehetett bejutni" korszak — mindezt a *sajtó* írta meg, nem a vendéglő. | a történet forrása pecsaktual.hu / pecsma.hu | [T] |
| U6 | **A szombat esti retro élőzene nincs a főoldalon.** Ez heti visszatérő esemény és önálló látogatási ok. | a program a hovamenjek.hu-n van kiemelve | [V] |

### 2.3 SEO

| # | Probléma | Bizonyíték | Szint |
|---|---|---|---|
| S1 | **A `<title>`-ök duplikálják a márkanevet, és kulcsszóhalmozásba futnak.** Ténylegesen indexelt címek:<br>`Főoldal - Diana Vendéglő Diana Vendéglő házias ízvilág`<br>`Napi menü - Diana Vendéglő Diana Vendéglő napi menü`<br>`Étel - Diana Vendéglő Diana Vendéglő ételei`<br>`Ital - Diana Vendéglő Diana Vendéglő italok`<br>`Rendezvények - Diana Vendéglő Diana Vendéglő rendezvények` | SERP | **[T]** |
| S2 | **A főoldal címe a „Főoldal" szóval kezdődik.** A `<title>` első ~30 karaktere a legértékesebb hely a teljes weboldalon; itt egy olyan szó áll, amire soha senki nem keres. | SERP | [T] |
| S3 | **Egyetlen címben sincs benne, hogy „Pécs".** Egy lokális vendéglőnek ez a legfontosabb kulcsszava. | SERP | [T] |
| S4 | **Az oldal a saját tényeire nem rangsorol.** A „130 fős", „45 fős különterem", „1982" kifejezésekre katalógus- és sajtóoldalak jönnek elő, nem a `dianavendeglo.hu`. | keresési eredmények | [T] |
| S5 | **`/wp/` a kanonikus útvonalban** — minden belső link és minden backlink egy technikai szegmensen keresztül megy. | URL-struktúra | [T] |

### 2.4 Performance

**Nem mértem, tehát nem állítok semmit.** Amit a struktúrából valószínűsítek,
és amit élesítés előtt **meg kell mérni** (Lighthouse + CrUX + WebPageTest,
4G-throttling, Moto G4 profil):

| # | Feltételezés | Miért valószínű | Szint |
|---|---|---|---|
| P1 | Optimalizálatlan, teljes méretben feltöltött ételfotók | tipikus WP-vendéglő minta; nincs bizonyítékom | [V] |
| P2 | Sablon + több plugin CSS/JS-e a kritikus útvonalon | ugyanaz | [V] |
| P3 | Nincs `width`/`height` a képeken → CLS | ugyanaz | [V] |

Ezek **[V]** szintű feltételezések. Az audit első lépése a mérés, nem a javítás.

---

## 3. Miért rosszak ezek — a mögöttes ok, nem a tünet

**A `/wp/` nem elgépelés, hanem egy telepítési döntés, amit soha nem javítottak ki.**
A tünet egy útvonal-szegmens; a mögöttes ok az, hogy az oldal **egyszer elkészült,
és azóta üzemel, nem fejlődik**. Ugyanez az ok termeli a duplikált címeket
(a sablon alapbeállítása maradt) és az elavuló „Ajánlatok" oldalt.

**A duplikált `<title>`-ök nem SEO-hiba, hanem a márkahang hiányának lenyomata.**
A `Diana Vendéglő Diana Vendéglő házias ízvilág` azért állhat elő, mert valaki
kitöltött egy „SEO-cím" és egy „alcím" mezőt anélkül, hogy bárki elolvasta volna,
mi jön ki belőle a keresőben. Senki nem nézte meg a saját oldalát vendégként.

**A legsúlyosabb probléma nem technikai: a Diana a saját történetét kiszervezte.**
A 130 fős terem, a 45 fős leválasztható különterem, a 120 fős kerthelyiség, a
bográcsban és vaslapon főzés, az 1982. május 1-i nyitás, a napi élőzenés
nyolcvanas évek — **ezt mind más oldalak írták meg**. Ez azt jelenti, hogy a
vendéglő legerősebb bizonyítékai fölött nincs kontrollja: nem tudja frissíteni,
nem tudja kiemelni, nem tud rá konvertálni, és a keresőben más domain kapja értük
a forgalmat. Egy 43 éves intézmény esetében ez nem elmaradt tartalomírás, hanem
**elveszített vagyon**.

**Az „egy oldal minden rendezvénynek" azért rossz, mert a rendezvényszervező nem
rendezvényt keres, hanem a sajátját.** Aki ballagásra keres helyet, annak a
lakodalmi szöveg zaj; aki lakodalmat szervez, annak a ballagási menü zaj. Egy
közös oldal *mindkettőnek* rosszabb, mint két rövidebb. A mögöttes ok itt egy
gyakori tervezői tévedés: **a struktúrát a kínálat, nem a szándék szerint szabták.**

**A „nyitva vagytok most?" kérdés azért kritikus, mert ez a mobilos vendég
tényleges belépési kérdése.** Egy vendéglő oldalát nem böngészik, hanem
*megkérdezik*. Ha az oldal erre nem válaszol 1 másodpercen belül, a vendég
visszalép a Google-listingre — és onnantól a Google birtokolja a vendéget.

---

## 4. Új információs architektúra és sitemap

### 4.1 A vezérelv

Az IA nem az étterem felépítését képezi le, hanem a **négy tényleges belépési
szándékot**:

1. „Most nyitva? Mennyiért? Hol?" → gyors tények
2. „Mi a mai menü?" → napi menü
3. „Elfér nálatok 80 fő ballagásra?" → rendezvény
4. „Milyen hely ez egyáltalán?" → a Diana története

### 4.2 Sitemap URL-enként indokolva

```
/                                   Főoldal
├── /napi-menu/                     Heti/napi menü            ← MEGTARTOTT URL
├── /etlap/                         Teljes étlap (étel + ital)
├── /rendezvenyek/                  Rendezvény-hub
│   ├── /rendezvenyek/eskuvo/
│   ├── /rendezvenyek/ballagas/
│   └── /rendezvenyek/ceges/
├── /asztalfoglalas/                Foglalás
├── /a-diana/                       1982 óta — a történet
├── /kapcsolat/                     Cím, parkolás, megközelítés
└── /ajanlatok/                     Aktuális ajánlatok
```

| URL | Miért pont ez | Alternatíva, amit elvetettem |
|---|---|---|
| `/` a `/wp/` helyett | A `/wp/` semmit nem ad a vendégnek, és minden meglévő backlinket egy technikai szegmensen vezet át. Költözés + **301 minden `/wp/*` → `/*`**, a régi útvonalak élnek tovább átirányításként. | „Hagyjuk, működik." — működik, de minden jövőbeli linket is rontani fog, és a javítás költsége az idővel nő, nem csökken. |
| `/napi-menu/` **változatlanul** | Ez az egyetlen URL, aminek bizonyíthatóan van visszatérő keresési kereslete és belső értéke. Nem nyúlok hozzá; csak a `/wp/` esik le róla. | `/heti-menu/` — pontosabb lenne, de eldobná a meglévő indexelést egy szinonimáért. Nem éri meg. |
| `/etlap/` (Étel + Ital összevonva) | Senki nem keres „ital"-ra egy vendéglő kapcsán; „étlap"-ra keres. Egy oldal, `#levesek`, `#foetelek`, `#italok` horgonyokkal. 301: `/wp/etel/` és `/wp/ital/` → `/etlap/`. | Két oldal megtartása — két gyengébb oldal egy erős helyett, és két kattintás egy döntéshez. |
| `/rendezvenyek/` + 3 aloldal | Külön keresési szándék, külön kapacitáslogika, külön bizonyíték. A hub megtartja a meglévő URL erejét, az aloldalak viszik a hosszú farkat („ballagás helyszín Pécs"). | Egyetlen hosszú oldal — olcsóbb, de minden célközönségnek 70%-ban irreleváns. |
| `/asztalfoglalas/` | A Google Cégprofil **már most is hirdet egy foglalási linket**. Ha van rá hirdetett belépési pont, kell hozzá landolóoldal. | Modális ablak URL nélkül — nem linkelhető a Cégprofilból, nem mérhető, nem osztható meg. |
| `/a-diana/` | Az 1982-es történet ma más domainen hoz forgalmat. Ez a lap veszi vissza. A `/rolunk/` helyett azért `/a-diana/`, mert a helyiek így hívják: „a Diana". | `/rolunk/` — semleges, de kicseréli a márkanevet egy általános szóra. |
| `/kapcsolat/` | Parkolás, buszjárat, megközelítés Kertvárosban — ez valódi, döntés előtti kérdés, nem lábléc-tartalom. | Csak lábléc — a parkolási info így soha nem rangsorol semmire. |
| `/ajanlatok/` | Rövidebb, mint az `ajanlatok-aktualitasok`, és **fegyelmet kényszerít**: az „aktualitások" szó teszi lehetővé, hogy elavuljon. Ha nincs aktuális ajánlat, az oldal a heti menüre irányít. | Törlés — az akciók valós forgalmat hoznak; a probléma a karbantartás, nem az oldal. |

---

## 5. Oldalankénti felépítés

### 5.1 Főoldal

| # | Szekció | Feladat | Tartalom forrása |
|---|---|---|---|
| 1 | Fejléc | navigáció + telefon + téma-kapcsoló | — |
| 2 | Hero + **Napív** (szignatúra) | „nyitva vagyunk / most ez van" 1 mp alatt | nyitvatartás [T] |
| 3 | Ma a Dianában | napi menü kiemelés + ár | menü [P] |
| 4 | Mit főzünk | kistermelő, vaslap/parázs/bogrács, vegán | [T] |
| 5 | Rendezvények | 130 / 45 / 120 fő, vizuális kapacitás | [T] |
| 6 | Szombat este | retro élőzene | [T] |
| 7 | 1982 óta | rövid történet + link a `/a-diana/`-ra | [T] |
| 8 | Vendégek | 4,2 ★ / 910 értékelés | [T] |
| 9 | Gyakorlati tudnivalók | nyitvatartás-táblázat, fizetés, kiszállítás | [T] |
| 10 | Asztalfoglalás | űrlap inline validációval | — |
| 11 | Lábléc | NAP-adatok, térkép, jogi | [T] |

### 5.2 A többi oldal

| Oldal | Szekciók sorrendben |
|---|---|
| `/napi-menu/` | Mai menü kiemelve → a hét többi napja → ár és időablak → „hozom / viszem / kiszállítás" → foglalás |
| `/etlap/` | Ugrósáv (`#levesek` `#foetelek` `#vegan` `#italok`) → kategóriák → allergén-jelzés → ár |
| `/rendezvenyek/` | Kapacitás-vizualizáció → három típus kártyája → hogyan zajlik → ajánlatkérő űrlap |
| `/rendezvenyek/{tipus}/` | A típus egy mondatban → mire fér el hány fő → menüsor-példa **[P]** → mikorra kell foglalni **[P]** → ajánlatkérés |
| `/asztalfoglalas/` | Űrlap elsőként, magyarázat utána → „nagy létszám? hívj" → telefon |
| `/a-diana/` | 1982 → a nyolcvanas évek → 2003, Racskó Gábor → ma → mi maradt ugyanaz |
| `/kapcsolat/` | Térkép → cím → parkolás **[P]** → tömegközlekedés **[P]** → telefon, e-mail → nyitvatartás |

---

## 6. Wireframe

### 6.1 Desktop (≥1024px)

```
┌───────────────────────────────────────────────────────────────────────┐
│ [Diana Vendéglő]   Étlap  Napi menü  Rendezvények  A Diana  Kapcsolat │
│  Pécs · Kertváros · 1982              ☀/☾   (06 72) 438 176  [Foglalás]│
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   Kertváros vendéglője                     ●  NYITVA                  │
│   1982 óta.                                   Zárás: 22:00            │
│                                                                       │
│   Házias magyar konyha, helyi kistermelők                             │
│   alapanyagaiból. 130 fős terem, 45 fős                               │
│   különterem, 120 fős kerthelyiség.                                   │
│                                                                       │
│   [ Asztalt foglalok ]   [ Mai menü ]                                 │
│                                                                       │
│   ── SZIGNATÚRA: A DIANA NAPJA ───────────────────────────────────    │
│                        ╭──────────────────────╮                       │
│               ╭────────╯          ▲           ╰────────╮              │
│          ╭────╯                  most                  ╰────╮         │
│      11:00      13:00       15:00      17:00      19:00     22:00     │
│      └─ napi menü ─┘└──────── à la carte ────────┘└─ élőzene ┘        │
│                                                                       │
├───────────────────────────────────────────────────────────────────────┤
│  MA A DIANÁBAN — kedd                                                 │
│  ┌─────────────────────────┬─────────────────────────┐                │
│  │ A menü                  │ B menü                  │   [Teljes hét] │
│  │ [leves] · [főétel]      │ [leves] · [főétel]      │                │
│  │ [ár] Ft                 │ [ár] Ft                 │                │
│  └─────────────────────────┴─────────────────────────┘                │
├───────────────────────────────────────────────────────────────────────┤
│  MIT FŐZÜNK                                                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐                  │
│  │kistermelő│ │ vaslap,  │ │  vegán   │ │  SZÉP-   │                  │
│  │  alap-   │ │ parázs,  │ │lehetőségek││ kártya,  │                  │
│  │  anyag   │ │  bogrács │ │          │ │bankkártya│                  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘                  │
├───────────────────────────────────────────────────────────────────────┤
│  RENDEZVÉNYEK                                                         │
│   ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪  130 fő — nagyterem                        │
│   ▪▪▪▪▪▪▪▪▪                   45 fő — különterem (leválasztható)      │
│   ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪      120 fő — kerthelyiség (nyáron)          │
│  [Esküvő] [Ballagás] [Céges]                    [Ajánlatot kérek]     │
├───────────────────────────────────────────────────────────────────────┤
│  SZOMBAT ESTE  │  1982 ÓTA           │  VENDÉGEK: 4,2 ★ / 910         │
├───────────────────────────────────────────────────────────────────────┤
│  ASZTALFOGLALÁS            │  NYITVATARTÁS   H–Cs 11–22               │
│  [név] [telefon]           │                 P–Szo 11–23              │
│  [dátum] [idő] [fő]        │                 V    11–22               │
│  [megjegyzés]              │  Pécs, Diana tér 10.                     │
│  [ Foglalás elküldése ]    │  (06 72) 438 176                         │
├───────────────────────────────────────────────────────────────────────┤
│  Lábléc: NAP · Wolt · Foodora · adatkezelés                           │
└───────────────────────────────────────────────────────────────────────┘
```

### 6.2 Mobil (375px)

```
┌───────────────────────────┐
│ Diana Vendéglő      ☀ ☰   │
├───────────────────────────┤
│ ● NYITVA · zárás 22:00    │  ← ragadós állapotsáv
├───────────────────────────┤
│                           │
│  Kertváros                │
│  vendéglője               │
│  1982 óta.                │
│                           │
│  Házias magyar konyha,    │
│  helyi kistermelők        │
│  alapanyagaiból.          │
│                           │
│  ╭──────────────────╮     │  ← Napív, mobilon
│  │   ▲ most 13:40   │        alacsonyabb ívvel
│  ╰──────────────────╯     │
│  11:00 ··········· 22:00  │
│  napi menü 14:30-ig       │
│                           │
│  [  Asztalt foglalok  ]   │
│  [  Mai menü          ]   │
├───────────────────────────┤
│ MA A DIANÁBAN — kedd      │
│ ┌───────────────────────┐ │
│ │ A menü                │ │
│ │ [leves] · [főétel]    │ │
│ │ [ár] Ft               │ │
│ └───────────────────────┘ │
│ ┌───────────────────────┐ │
│ │ B menü …              │ │
│ └───────────────────────┘ │
│ → Teljes hét              │
├───────────────────────────┤
│ MIT FŐZÜNK                │
│ ┌───────────┐ ┌─────────┐ │  ← 2 oszlop
│ │kistermelő │ │ vaslap  │ │
│ └───────────┘ └─────────┘ │
│ ┌───────────┐ ┌─────────┐ │
│ │  vegán    │ │  SZÉP   │ │
│ └───────────┘ └─────────┘ │
├───────────────────────────┤
│ RENDEZVÉNYEK              │
│ ▪▪▪▪▪▪▪▪▪▪▪▪▪ 130 nagyterem│
│ ▪▪▪▪▪         45 különterem│
│ ▪▪▪▪▪▪▪▪▪▪▪   120 kert     │
│ [Ajánlatot kérek]         │
├───────────────────────────┤
│ SZOMBAT ESTE · retro      │
├───────────────────────────┤
│ 1982 ÓTA →                │
├───────────────────────────┤
│ 4,2 ★ · 910 értékelés     │
├───────────────────────────┤
│ ASZTALFOGLALÁS            │
│ [név]                     │
│ [telefon]                 │
│ [dátum] [idő]             │
│ [fő]                      │
│ [megjegyzés]              │
│ [ Foglalás elküldése ]    │
├───────────────────────────┤
│ Nyitvatartás / cím / NAP  │
├───────────────────────────┤
│ [ Hívás ]   [ Foglalás ]  │  ← fix alsó sáv,
└───────────────────────────┘     safe-area-padding
```

**Mobil-döntés:** a fix alsó sávban **két** akció van, nem több. A „Hívás" azért
marad az első helyen, mert a Google-listing tanúsága szerint a Dianát ma is
telefonon érik el, és 20:30-kor egy telefonhívás gyorsabb, mint bármilyen űrlap.

---

## 7. Design system

### 7.0 A vizuális kiindulópont — egy mondatban

> **A kiindulópont a Diana nyári kerthelyiségének parazsa: a meszelt fal meleg
> törtfehérje, a pörköltpaprika mélyvörösse, a vaslap alatt izzó parázs
> narancsa és a kertvárosi fák tompa zöldje — négy szín, ami fizikailag ott van
> az udvarban, amikor a szakács a bogrács mellett áll.**

Ez a paletta forrása. Nem hangulattábla, hanem egy **dokumentált tény**
(„vaslapon, grillen, parázson és bográcsban készítik az ételt a vendégek előtt")
lefordítása színre. Nem esik bele a „fekete háttér + egy neon accent" mintába,
mert a Dianában nincs semmi neon; és nem lesz belőle „étterem = piros" klisé sem,
mert a vörös itt **másodhegedűs**: az alaphangot a meszelt fal és a füst adja.

### 7.1 Színtokenek — 8 nevesített token, mért kontraszttal

A kontrasztértékeket WCAG 2.1 relatív luminancia szerint számoltam
(`(L1+0.05)/(L2+0.05)`), nem becsültem.

**Világos mód**

| Token | Hex | Szerep | Kontraszt |
|---|---|---|---|
| `--lap` | `#F6F1E8` | oldalháttér (meszelt fal) | alap |
| `--abrosz` | `#FFFDF8` | kártya-, űrlapfelület | 1,11 : 1 a `--lap`-hoz (szándékos: elválasztás vonallal, nem világossággal) |
| `--tinta` | `#1F1710` | elsődleges szöveg | **15,71 : 1** a `--lap`-on · 17,38 : 1 az `--abrosz`-on — AAA |
| `--fust` | `#6A5F52` | másodlagos szöveg | **5,54 : 1** · 6,13 : 1 — AA |
| `--paprika` | `#A32C1C` | elsődleges akció, márkaszín | **6,36 : 1** · 7,04 : 1 — AA; fehér **rajta 7,16 : 1** |
| `--parazs` | `#B04E17` | szignatúra-kiemelés, fókuszgyűrű | **4,73 : 1** · 5,23 : 1 — AA; fehér rajta 5,32 : 1 |
| `--liget` | `#3C5A3A` | „nyitva" / sikeres állapot | **6,87 : 1** · 7,61 : 1 — AA |
| `--vonal` | `#93856B` | űrlapkeret, aktív határ | **3,21 : 1** a `--lap`-on — WCAG 1.4.11 ✓ |
| `--vonal-halk` | `#E2D9C8` | *csak dekoratív* elválasztó | 1,24 : 1 — soha nem hordoz információt |
| `--hiba` | `#A31B12` | hibaüzenet | **6,86 : 1** — AA |

**Sötét mód** — nem invertálás, hanem külön hangolt tónusok (a paprika és a
parázs deszaturálva és világosítva, ahogy a Material és a HIG is előírja):

| Token | Hex | Kontraszt a `--lap`-on (`#14110F`) |
|---|---|---|
| `--lap` | `#14110F` | alap (meleg sötét, nem `#000` — az esti terem, nem a világűr) |
| `--abrosz` | `#1E1A17` | 1,09 : 1 |
| `--tinta` | `#F2EAE0` | **15,78 : 1** · 14,50 : 1 az `--abrosz`-on — AAA |
| `--fust` | `#A99B8C` | **6,94 : 1** · 6,38 : 1 — AA |
| `--paprika` | `#F08A72` | **7,69 : 1**; sötét szöveg rajta 7,69 : 1 |
| `--parazs` | `#E6A05A` | **8,54 : 1** |
| `--liget` | `#93B683` | **8,29 : 1** |
| `--vonal` | `#77695D` | **3,55 : 1** — 1.4.11 ✓ |
| `--vonal-halk` | `#332C27` | 1,37 : 1 — dekoratív |
| `--hiba` | `#FFA898` | **10,12 : 1** |

**Alternatíva, amit elvetettem:** a ui-ux-pro-max `--design-system` futása
`#DC2626` + `#F87171` + `#FEF2F2` „appetizing red" palettát javasolt. Elvetettem:
a `#DC2626` a Tailwind `red-600` alapértéke, ma minden második étteremoldal ezt
használja, és a `#FEF2F2` rózsaszínes háttér a Diana meszelt-fal világától
idegen. A saját paletta ugyanazt a funkciót látja el (étvágy, meleg), de a
vendéglő fizikai környezetéből származik.

### 7.2 Tipográfia

**Két variable betűcsalád, mindkettő teljes `latin-ext` lefedettséggel** —
az `ő` és az `ű` valódi, tervezett glif, nem fallback-összeollózás.

| Szerep | Betűcsalád | Tengelyek | Miért ez |
|---|---|---|---|
| Display + UI | **Bricolage Grotesque** | `opsz`, `wdth`, `wght` | Táblafestett, cégérszerű groteszk, enyhén szabálytalan írásjelekkel. A `wdth` tengely miatt a nagy címsorok szorosra húzhatók — pontosan úgy, ahogy egy 1982-es zománctábla feliratát a rendelkezésre álló helyre szorították. Nem „elegáns étterem", hanem **vendéglő**. |
| Folyószöveg | **Source Serif 4** | `opsz`, `wght` | Adobe-forrású, kifogástalan magyar ékezetes rajzolattal, valódi optikai méret-tengellyel: 17px-en melegen, könyvszerűen olvas. Egy étlapot serifben olvasunk, nem UI-fontban. |

**A display face minimális használati mérete: 28px**, ha `wdth < 100` vagy
`opsz > 24` (a szűkített változat 24px alatt összecsukja az `ő` két vesszőjét).
28px alatt a Bricolage-t **csak `wdth: 100`, `wght: 500–600` beállítással**
használom, kizárólag UI-címkékre és gombokra (14–16px).

**Alternatíva, amit elvetettem:** Playfair Display + Inter — a brief kifejezetten
tiltja, és jogosan: ez ma az AI-generált oldalak alapértelmezése. A ui-ux-pro-max
Playfair Display SC + Karla javaslatát is elvetettem ugyanezért (a Playfair SC
kiskapitálisai ráadásul magyar szövegben a hosszú ékezeteket felül levágják).
Elvetettem továbbá a Fraunces-t: szép, de ma a „specialty coffee 2021" arca, és
egy 1982-es kertvárosi vendéglőhöz kölcsönzött nosztalgia lenne, nem a sajátja.

**Skála** — `clamp()`, 320px → 1440px között folytonos:

```css
--sz-cim:    clamp(2.5rem,  1.6rem + 4.5vw,  5rem);     /* 40 → 80px  */
--sz-h2:     clamp(1.75rem, 1.35rem + 2vw,   2.75rem);  /* 28 → 44px  */
--sz-h3:     clamp(1.25rem, 1.1rem + 0.75vw, 1.625rem); /* 20 → 26px  */
--sz-nagy:   clamp(1.125rem, 1.05rem + 0.4vw, 1.3125rem);/* 18 → 21px */
--sz-alap:   1.0625rem;                                 /* 17px fix   */
--sz-kicsi:  0.9375rem;                                 /* 15px       */
--sz-apro:   0.8125rem;                                 /* 13px       */
```

A folyószöveg **fix 17px**, nem `vw`-alapú: a `vw`-skálázott törzsszöveg
elveszi a felhasználótól a böngésző-zoom kontrollját. Sormagasság 1,65 a
törzsszövegen, 1,08 a display címsorokon. Sorhossz 62–68 karakter (`max-width: 62ch`).

### 7.3 Spacing — 8px alap

```
--t1: 4px    --t2: 8px    --t3: 12px   --t4: 16px   --t5: 24px
--t6: 32px   --t7: 48px   --t8: 64px   --t9: 96px   --t10: 128px
```

Szekcióköz: `--t8` mobilon, `--t9` tableten, `--t10` desktopon.
Kártya-belső: `--t5`. Űrlapmező-köz: `--t4`. Címke→mező: `--t2`.

### 7.4 Elevation

Nem árnyékkal rétegzek, hanem **vonallal és tónussal** — ez a meszelt fal
logikája, és sötét módban is működik, ahol az árnyék láthatatlan.

| Szint | Világos | Sötét | Használat |
|---|---|---|---|
| 0 | `--lap`, nincs keret | `--lap` | oldalháttér |
| 1 | `--abrosz` + 1px `--vonal-halk` | `--abrosz` + 1px `--vonal-halk` | kártya |
| 2 | 1. szint + `0 1px 2px rgb(31 23 16 / .06)` | 1. szint + `--abrosz` világosítva 4%-kal | kiemelt kártya, űrlap |
| 3 | 2. szint + `0 8px 24px rgb(31 23 16 / .10)` | `#262019` + 1px `--vonal` | ragadós fejléc, mobil menü |
| 4 | 3. szint + 50% `rgb(31 23 16 / .5)` scrim | ugyanaz | modális, mobil navigáció |

### 7.5 Komponenslista

`Fejléc` · `Mobilnavigáció (sheet)` · `Témakapcsoló (3 állás: rendszer/világos/sötét)` ·
`Napív (szignatúra)` · `Állapotjelvény (nyitva/zárva)` · `Elsődleges gomb` ·
`Másodlagos gomb` · `Szöveges link-gomb` · `Menükártya` · `Ténykártya` ·
`Kapacitássáv` · `Idézetblokk` · `Értékelés-összegző` · `Nyitvatartás-táblázat` ·
`Űrlapmező (szöveg / tel / dátum / idő / szám / textarea)` · `Hibaüzenet` ·
`Sikerüzenet (aria-live)` · `Fix mobil akciósáv` · `Lábléc` · `Skip-link`

---

## 8. Animációk és mikrointerakciók

Minden animáció `transform` és `opacity` — nulla layout-reflow, nulla CLS.
Globális tokenek: `--ki: cubic-bezier(.16,1,.3,1)` (belépés),
`--be: cubic-bezier(.4,0,1,1)` (kilépés).

| Elem | Interakció | Időzítés / easing | Miért |
|---|---|---|---|
| Napív marker | oldalbetöltés | 900ms `--ki`, 200ms késleltetés, `stroke-dashoffset` + `translate` | Megmutatja, hogy az ív **egy nap**, és hol tartunk benne. Ez a szignatúra teljes érvelése. |
| Napív szegmens | hover / fókusz | 180ms `--ki`, `opacity .55→1` | melyik sáv aktív |
| Állapotjelvény pont | folyamatos | 2,4s `ease-in-out` alternate, `opacity .55↔1` | „élő" adat, nem statikus felirat |
| Szekciók | scroll-belépés | 420ms `--ki`, `translateY(14px)→0` + fade, IntersectionObserver, **egyszer** | olvasási ritmus; nem ismétlődik, hogy ne legyen zaklató |
| Menükártya / ténykártya | rácsban belépés | 60ms stagger elemenként, max 6 elem | csoport-összetartozás |
| Gomb | hover | 160ms, `translateY(-1px)` + háttér-tónus | tapintható visszajelzés |
| Gomb | aktív (lenyomás) | 90ms, `scale(.985)` | a kilépés gyorsabb, mint a belépés |
| Kapacitássáv | belépés | 700ms `--ki`, `scaleX(0→1)` origin left, stagger 90ms | a három tér **méretét** mutatja, nem mondja |
| Űrlapmező | fókusz | 140ms, `box-shadow` fókuszgyűrű | láthatóság |
| Űrlapmező | hiba `blur`-nél | 200ms, keretszín + üzenet `opacity 0→1`, **nem** rázás | a rázás pánikot közöl; a hiba nem katasztrófa |
| Sikerüzenet | küldés után | 260ms fade + `translateY(8px)→0`, `role="status"` | képernyőolvasónak is |
| Mobil menü | nyitás | 260ms `--ki`, `translateY(-8px)` + fade; zárás 170ms `--be` | térbeli folytonosság a hamburger-gombtól |
| Témakapcsoló | váltás | 220ms `ease` a háttéren és a szövegszínen | a hirtelen villanás fárasztó éjjel |

**`prefers-reduced-motion: reduce` esetén:** minden `transition` és `animation`
`0.01ms`-re esik, a scroll-belépés kikapcsol (a tartalom azonnal `opacity: 1`),
a Napív markere **animálás nélkül, a végállapotban** jelenik meg — az információ
nem vész el, csak a mozgás. Az állapotjelvény pulzálása leáll.

---

## 9. Frontend megvalósítás

### 9.1 Stack és indoklás

**Marad WordPress**, egyedi blokk-témával (classic theme, nem full-site editing),
`/wp/`-ből a gyökérbe költöztetve.

*Miért nem Next.js / Astro:* mert a Diana legértékesebb működő szokása a **heti
menü feltöltése**. Bármilyen statikus generátor ezt vagy build-lépéssé, vagy egy
headless CMS második belépési pontjává tenné. Az a redesign, ami a heti
menüfrissítést megnehezíti, a vendéglő legjobb tulajdonságát rontja el —
függetlenül attól, hogy hány ponttal jobb Lighthouse-t hoz.

*Miért nem a meglévő sablon átszínezése:* mert a `<title>`-problémát (S1–S3) és a
`/wp/` útvonalat sablonszinten nem lehet megbízhatóan javítani, és mert a
szignatúra elem inline SVG-t igényel a template-ben.

| Réteg | Választás | Alternatíva, amit elvetettem |
|---|---|---|
| CMS | WordPress, egyedi téma | Astro + headless WP — plusz réteg, plusz hibaforrás, semmi haszon egy 8 oldalas oldalon |
| CSS | kézi CSS, custom property-k, `@layer`, container query-k | Tailwind — build-lépést hoz be egy olyan csapatba, ahol nincs build-lépés |
| JS | vanilla, ~6 KB, nulla függőség | Alpine.js (~15 KB) — háromszoros költség öt viselkedésért |
| Foglalás | saját `POST` + e-mail + naptár-ICS **[P]** | külső foglalórendszer — havi díj, márkaidegen felület; ha van már ilyen, azt integrálom |
| Analitika | Plausible vagy szerveroldali | GA4 — cookie-banner, ami elveszi a hero felét mobilon |

### 9.2 Fontkezelés

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?
  family=Bricolage+Grotesque:opsz,wdth,wght@10..48,75..100,300..800
  &family=Source+Serif+4:opsz,wght@8..60,300..600
  &display=swap">
```

- A Google Fonts `css2` végpontja `unicode-range`-alapú subsetet szolgál ki: a
  `latin-ext` blokk **automatikusan** letöltődik, amint az oldalon `ő`/`ű`
  szerepel. Nem kell külön kérni — **azt kell ellenőrizni, hogy a család
  egyáltalán tartalmaz-e latin-ext lefedettséget.** Mindkét választott család
  tartalmaz.
- `display=swap`, és a fallback stackre `size-adjust`/`ascent-override` van
  állítva, hogy a swap ne okozzon CLS-t.
- **Élesben:** a két variable WOFF2 önhosztolva (`/betuk/`), **a latin és a
  latin-ext subsetfájllal együtt**, `preload`-dal, `font-display: swap`. Ez
  levesz két DNS-feloldást és egy harmadik felet a kritikus útvonalról. Ha csak
  a latin subsetet töltjük fel — ez a leggyakoribb önhosztolási hiba —, az
  `ő` és az `ű` fallback-fontból fog jönni. A prototípusban Google Fontsról
  érkezik, hogy egyetlen fájlban, azonnal megnyithatóan működjön.

### 9.3 Képek

A prototípus **szándékosan fotómentes** (indoklás: 10.4 / szignatúra). Élesben:

- AVIF + WebP + JPEG `<picture>`-rel, `srcset` 480/800/1200/1600w.
- Kötelező `width`/`height` vagy `aspect-ratio` minden képen → CLS 0.
- A hero fölött **nincs** kép; az első kép `loading="eager"`, `fetchpriority="high"`
  csak akkor, ha az LCP-elem lenne — jelenleg nem az.
- Minden további kép `loading="lazy"` + `decoding="async"`.
- **Fontos:** a ma használt ételfotók minőségét látatlanban nem minősítem.
  Ha nincs profi anyag, előbb a fotózás, aztán a képgaléria (13. fejezet, 3. fázis).

### 9.4 Cache

| Erőforrás | Fejléc |
|---|---|
| HTML | `Cache-Control: public, max-age=0, s-maxage=300, stale-while-revalidate=86400` |
| CSS/JS (hasheltnév) | `public, max-age=31536000, immutable` |
| Betűk (önhosztolt) | `public, max-age=31536000, immutable` |
| Képek | `public, max-age=2592000` |
| `/napi-menu/` | `s-maxage=600` — hetente változik, de a hét közbeni javítás gyorsan menjen ki |

Ezen felül: Brotli, HTTP/2, `Link: rel=preload` a két betűre, és a
`/wp/*` → `/*` **301** (nem 302) minden régi útvonalra.

### 9.5 Űrlap

- Natív HTML5 típusok: `type="tel"` (`inputmode="tel"`), `type="date"`,
  `type="time"`, `type="number"`, hogy mobilon a helyes billentyűzet nyíljon.
- `autocomplete="name"`, `"tel"` — rendszerszintű kitöltés.
- **Validáció `blur`-nél, nem billentyűleütésnél**; a hiba a mező *alatt*
  jelenik meg, `aria-describedby`-jal összekötve, `role="alert"`-tel.
- Küldés után: az első hibás mezőre ugrik a fókusz; több hiba esetén összegző
  a lista tetején, horgony-linkekkel.
- **Az űrlap ismeri a nyitvatartást**: 11:00 előtti vagy zárás utáni időpontot
  nem fogad el, és megmondja, meddig lehet asztalt foglalni azon a napon.
- **45 fő fölött** az űrlap átirányít a rendezvény-ajánlatkérésre — mert 45 fő
  fölött már a különtermet vagy a nagytermet foglalja, ami más folyamat.
- Honeypot mező + időbélyeg-ellenőrzés spam ellen; **nincs CAPTCHA** (a reCAPTCHA
  ~250 KB harmadik fél JS-e, és a legrosszabb konverziós elem, amit egy
  vendéglői foglalásra tehetünk).

---

## 10. SEO-specifikáció

### 10.1 Title / meta minta

| Oldal | `<title>` (≤60 kar.) | `<meta name="description">` (≤155 kar.) |
|---|---|---|
| `/` | `Diana Vendéglő Pécs — házias magyar konyha 1982 óta` | `Kertváros vendéglője a Diana téren. Napi menü, magyaros ételek helyi alapanyagból, 130 fős terem, 45 fős különterem, 120 fős kert. Foglalás: (06 72) 438 176.` |
| `/napi-menu/` | `Napi menü — Diana Vendéglő, Pécs Kertváros` | `A Diana Vendéglő heti menüje egy hétre előre, helyi kistermelők alapanyagaiból. Pécs, Diana tér 10.` |
| `/etlap/` | `Étlap és itallap — Diana Vendéglő, Pécs` | `Magyaros, házias ételek, vegán lehetőségek, italok. Diana Vendéglő, Pécs, Diana tér 10.` |
| `/rendezvenyek/` | `Rendezvényhelyszín Pécsen — Diana Vendéglő` | `130 fős nagyterem, 45 fős leválasztható különterem, 120 fős kerthelyiség. Lakodalom, ballagás, céges rendezvény Pécs Kertvárosban.` |
| `/rendezvenyek/ballagas/` | `Ballagási ebéd Pécsen — Diana Vendéglő` | `Ballagás, szalagavató, diplomaosztó a Diana Vendéglőben. 45 fős különterem vagy 130 fős nagyterem, egyedi menüsor.` |
| `/a-diana/` | `A Diana 1982 óta — Pécs Kertváros vendéglője` | `1982. május 1-jén nyitottunk. Akkor csak asztalfoglalással lehetett bejutni. Azóta is minden nap főzünk.` |

**A minta szabálya:** `[amit keresnek] — [márka], [város]`. A márkanév a
*végén* van, nem az elején, mert a 60 karakterből az elsők a legértékesebbek,
és aki „Diana Vendéglő"-re keres, úgyis megtalálja. Ez a jelenlegi
`Főoldal - Diana Vendéglő Diana Vendéglő …` minta pontos ellentéte.

### 10.2 Heading-hierarchia (főoldal)

```
h1  Kertváros vendéglője 1982 óta
├── h2  A Diana napja                     (szignatúra, nyitvatartás)
├── h2  Ma a Dianában
│   ├── h3  A menü
│   └── h3  B menü
├── h2  Mit főzünk
│   ├── h3  Helyi kistermelők alapanyagai
│   ├── h3  Vaslapon, parázson, bográcsban
│   ├── h3  Vegán lehetőségek
│   └── h3  SZÉP-kártya és bankkártya
├── h2  Rendezvények
│   ├── h3  130 fős nagyterem
│   ├── h3  45 fős különterem
│   └── h3  120 fős kerthelyiség
├── h2  Szombat este: retro élőzene
├── h2  1982 óta ugyanitt
├── h2  Amit a vendégeink mondanak
├── h2  Nyitvatartás és megközelítés
└── h2  Asztalfoglalás
```

Egy `h1`, nincs szintugrás, a `h3`-ak mindig `h2` alatt.

### 10.3 Teljes schema-lista (JSON-LD gráf)

Egyetlen `@graph`, `@id`-kkel összekötve:

| Típus | Mit ír le | Kulcsmezők |
|---|---|---|
| `Restaurant` | a vendéglő | `name`, `@id`, `url`, `telephone`, `email`, `priceRange: "2000–6000 Ft"`, `servesCuisine: "Magyar"`, `foundingDate: "1982-05-01"`, `paymentAccepted`, `currenciesAccepted: "HUF"`, `maximumAttendeeCapacity: 130`, `smokingAllowed: false` **[V]** |
| `PostalAddress` | cím | `streetAddress: "Diana tér 10."`, `addressLocality: "Pécs"`, `postalCode: "7632"`, `addressCountry: "HU"` |
| `GeoCoordinates` | koordináta | **[P]** — pontos lat/lng ügyféltől vagy geokódolásból |
| `OpeningHoursSpecification` ×3 | H–Cs / P–Szo / V | `dayOfWeek`, `opens`, `closes` |
| `AggregateRating` | Google-értékelés | `ratingValue: 4.2`, `reviewCount: 910` — **csak akkor tehető ki, ha az értékelések a saját oldalon is meg vannak jelenítve**, különben a Google policy-sértés |
| `Menu` + `hasMenuSection` + `MenuItem` | étlap | a tényleges tételek **[P]** |
| `Offer` | napi menü ára | **[P]** |
| `Place` ×3 | nagyterem / különterem / kerthelyiség | `maximumAttendeeCapacity: 130 / 45 / 120` — így a kapacitás gépi olvasható |
| `Event` | szombat esti retro élőzene | `eventSchedule: Schedule` heti ismétléssel — **[P]**: pontos kezdés kell |
| `ReserveAction` | foglalás | `target`, `EntryPoint` — ez az, amit a Google Cégprofil „Asztal foglalása" gombja használ |
| `BreadcrumbList` | morzsa | aloldalakon |
| `WebSite` + `WebPage` | oldal | `inLanguage: "hu-HU"` |
| `ImageObject` | logó, fotók | **[P]** |

### 10.4 Local SEO

1. **NAP-konzisztencia**: a `Diana tér 10.` írásmódnak minden platformon
   egyeznie kell. A jelenlegi listingekben `Diana tér`, `Diána tér` és
   `Diana Tér` is előfordul — ez a helyi rangsorolás egyik legolcsóbban
   javítható hibája. **[T]**
2. **Telefonszám egységesen** `+36 72 438 176` formátumban, `tel:+3672438176` linkkel.
3. **Google Cégprofil**: menü-link a `/napi-menu/`-re, foglalási link az
   `/asztalfoglalas/`-ra, „Termékek" közé a rendezvénycsomagok.
4. **Kertváros mint kulcsszó.** A sajtó „Kertváros ikonikus étterme"-ként
   emlegeti; ez földrajzi long tail, amire ma senki nem optimalizál.
5. **Citation-tisztítás**: nyitva.hu, etterem.hu, vendeglatasinfo.hu,
   legjobbettermek.hu, cylex, uzleti.hu, programturizmus — mind él, mind
   ellenőrizendő nyitvatartásra és névre.
6. **Értékeléskezelés**: 910 értékelés 4,2 átlaggal jó alap; a 3★ alattiakra
   adott válasz a helyi rangsor egyik mért tényezője.

---

## 11. Performance-célok

Mobil, 4G (150 ms RTT, 1,6 Mbps), Moto G4-osztályú CPU, hideg cache:

| Metrika | Cél | Prototípusban |
|---|---|---|
| LCP | **< 1,8 s** (jó: 2,5 s) | a hero `h1` — szöveg, nem kép |
| CLS | **< 0,03** (jó: 0,1) | 0, ha a `size-adjust` fallback helyes |
| INP | **< 150 ms** (jó: 200 ms) | nincs blokkoló JS |
| TTFB | < 400 ms | szerveroldali cache-től függ |
| FCP | < 1,2 s | kritikus CSS inline |
| HTML (tömörítve) | < 25 KB | **16,3 KB** gzip (a teljes egyfájlos prototípus, CSS-sel és JS-sel együtt) |
| CSS | < 18 KB tömörítve | a HTML-be ágyazva, lásd fent |
| **JS** | **< 8 KB tömörítve** | **11,0 KB nyers / 4,0 KB gzip.** A brief 5–10 KB-os korlátját tömörítve tartja; nyersen 1 KB-tal fölötte van, mert a kommenteket bennhagytam, hogy a kód átadható legyen. Minifikálva ~6 KB nyers. |
| Betűk | 2 fájl, < 90 KB együtt | `latin` + `latin-ext` subset |
| Első oldal összes bájt | **< 180 KB** kép nélkül, **< 420 KB** hero-fotóval |
| Lighthouse Performance | ≥ 95 mobilon | |
| Lighthouse Accessibility | **100** | |

**A jelenlegi oldal számait nem tudom megadni** — nem mértem. Az első fázis
első feladata a baseline-mérés, hogy a redesign hatása mérhető legyen.

---

## 12. CRO — konverziós elemek

**Az oldal EGY dolga a briefből hiányzik.** A rendelkezésre álló tények alapján a
javaslatom: **a rendezvény-ajánlatkérés** legyen az elsődleges konverzió, és az
asztalfoglalás a másodlagos. Indoklás: az asztalfoglalás bevétele
2000–6000 Ft/fő; egy 80 fős ballagási ebéd egyetlen kérésben nagyságrenddel
nagyobb értéket hoz, és a kapacitás (130 / 45 / 120) az a tulajdonság, amivel a
Diana ténylegesen kiemelkedik a pécsi mezőnyből. Ez **feltételezés**, az ügyfél
felülírhatja (15. fejezet, Q1).

| Elem | Hol | Miért működik |
|---|---|---|
| **Élő nyitva/zárva állapot** | fejléc + hero | A mobilos vendég első kérdésére válaszol, mielőtt feltenné. Csökkenti a visszalépést a Google-listingre — és a listingre visszalépő vendéget a Google, nem a Diana birtokolja. |
| **Napív (szignatúra)** | hero | Egyetlen ábrán mutatja meg, hogy *mikor mi van*: menüidő, à la carte, élőzene. A „mikor menjek?" kérdést döntéssé alakítja. |
| **Kapacitás-vizualizáció** | rendezvény-blokk | A 130/45/120 nem szám, hanem **méret** lesz. A rendezvényszervező egyetlen kizáró kritériumát azonnal ellenőrizhetővé teszi — a kizárás gyorsítása is konverzió. |
| **„Ma a Dianában" menü ár mellett** | 3. szekció | Az árat *előre* megadni bizalmi jelzés; az árat elrejteni a leggyakoribb ok, amiért egy vendég továbbáll. |
| **Telefon minden képernyőn** | fejléc + fix mobil sáv | Egy 43 éves vendéglő vendégköre telefonál. Az űrlap nem helyettesíti, kiegészíti. |
| **45 fő fölött automatikus átterelés** | foglalóűrlap | Megakadályozza, hogy nagy csoport rossz csatornán érkezzen — és így ne vesszen el. |
| **4,2 ★ / 910 értékelés, szám szerint** | vélemények | A 910 itt fontosabb, mint a 4,2: a mennyiség hitelesíti az átlagot. Egy 4,8-as átlag 12 értékeléssel gyengébb bizonyíték. |
| **1982. május 1.** | történet-blokk | Konkrét dátum, nem „több évtizedes múlt". A pontos dátum ellenőrizhető, tehát hihető. |
| **„Helyi kistermelők"** | mit főzünk | Dokumentált saját állítás, nem marketingfordulat. |
| **SZÉP-kártya kiírva** | gyakorlati blokk | Céges ebéd és rendezvény esetén ez gyakran kizáró kérdés. |

---

## 13. A fontos design-döntések összefoglaló táblázata

| # | Döntés | Miért | Alternatíva, amit elvetettem |
|---|---|---|---|
| 1 | **Marad a WordPress** | a heti menüfrissítés fejlesztő nélkül működik ma — ez a legjobb meglévő szokás | Astro/Next.js: jobb Lighthouse, de eltöri a heti menüt |
| 2 | **`/wp/` → gyökér, 301-ekkel** | minden URL és backlink tisztul; a javítás költsége az idővel nő | változatlanul hagyni |
| 3 | **Étel + Ital → `/etlap/`** | egy döntés, egy oldal; „étlap"-ra keresnek, nem „ital"-ra | két oldal megtartása |
| 4 | **Rendezvények → hub + 3 aloldal** | külön szándék, külön long tail | egyetlen hosszú oldal |
| 5 | **Szignatúra: Napív, nem fotó** | nincs jogtiszta fotóm, és egy fotó nem *mutatja meg* a napi ritmust; az ív igen | hero-fotó a teraszról |
| 6 | **Paletta a parázsból és a meszelt falból** | a vendéglő fizikai világából, nem a „restaurant = red" kliséből | ui-ux-pro-max `#DC2626` javaslata: Tailwind-alapérték, mindenhol ott van |
| 7 | **Bricolage Grotesque + Source Serif 4** | cégérszerű display + valódi magyar ékezetek olvasható serifben | Playfair+Inter (tiltott, AI-alapértelmezés), Playfair SC (levágja a hosszú ékezeteket), Fraunces (kölcsönzött nosztalgia) |
| 8 | **Elevation vonallal, nem árnyékkal** | sötét módban is működik; illik a meszelt fal logikájához | Material-árnyékskála: sötét módban láthatatlan |
| 9 | **Fotómentes prototípus** | a koncepció ne fotó minőségén álljon vagy bukjon; élesben jön a fotózás | stock-fotók: hazugság egy 43 éves valódi helyről |
| 10 | **Az űrlap ismeri a nyitvatartást** | a hiba megelőzése olcsóbb, mint a hibaüzenet | szabad időpont-beírás, hibaüzenettel |
| 11 | **45 fő fölött átterelés** | más folyamat, más ember válaszol rá | egy űrlap mindenre |
| 12 | **Nincs CAPTCHA** | ~250 KB harmadik fél JS a legérzékenyebb konverziós ponton | reCAPTCHA v2/v3 |
| 13 | **Nincs cookie-banner az MVP-ben** | szerveroldali/cookie-mentes analitikával nem kell — mobilon a banner elveszi a hero felét | GA4 + banner |
| 14 | **Három állású témakapcsoló** | a „rendszer" alapállás tiszteletben tartja az OS-beállítást; a kézi váltás felülírja | csak `prefers-color-scheme`, kapcsoló nélkül |
| 15 | **A telefonszám végig látszik** | a tényleges vendégkör telefonál | „modern" megoldás: csak űrlap |

---

## 14. Bevezetési ütemterv

| Fázis | Tartalom | Kimenet | Becsült idő **[P]** |
|---|---|---|---|
| **0. Mérés** | Lighthouse + CrUX baseline, teljes URL-lista, backlink-export, Search Console adatok, a jelenlegi étlap és árak begyűjtése | mérési riport, tartalomleltár | 1 hét |
| **1. Technikai alap** | `/wp/` → gyökér, 301-térkép, HTTPS + HSTS ellenőrzés, `<title>`/meta újraírás mind a 6 meglévő oldalon, JSON-LD alapgráf | **ez önmagában, redesign nélkül is javítja a rangsorolást** | 1–2 hét |
| **2. Főoldal** | design system implementálása, Napív, foglalóűrlap, sötét mód | új főoldal élesben | 2–3 hét |
| **3. Aloldalak** | `/napi-menu/`, `/etlap/`, `/rendezvenyek/` + 3 aloldal, `/a-diana/`, `/kapcsolat/` | teljes oldal | 3–4 hét |
| **4. Tartalom** | profi fotózás (terem, különterem, kert, parázs), a 1982-es történet megírása, rendezvény-menüsorok | képanyag és szövegek | párhuzamos, 2–4 hét |
| **5. Local SEO** | NAP-egységesítés minden citationben, Cégprofil frissítés, értékelés-válasz folyamat | konzisztens jelenlét | 1 hét + folyamatos |
| **6. Mérés újra** | ugyanaz, mint a 0. fázis | előtte/utána riport | 1 hét, élesítés után 4 héttel |

**Az 1. fázis a legjobb megtérülésű**, és nem függ a redesigntól. Ha az ügyfél
csak egyetlen fázist rendel meg, ez legyen az.

---

## 15. Nyitott kérdések — ehhez ügyfél-input kell

Az alábbiak nélkül az anyag **nem élesíthető**. Egyiket sem találtam ki.

**Üzleti**
- **Q1.** Mi az oldal EGY dolga: rendezvény-ajánlatkérés, asztalfoglalás vagy
  napimenü-forgalom? A teljes CRO-logika (12. fejezet) ezen áll.
- **Q2.** Melyik hoz ma több bevételt: à la carte, napi menü vagy rendezvény?
- **Q3.** Kik a valódi versenytársak Pécsen, és melyiktől veszítenek ügyfelet?
- **Q4.** Van bármi, amihez nem szabad hozzányúlni? (logó, a Diana-alak, szlogen,
  meglévő nyomdai arculat)

**Tartalom és számok — minden **[P]** ide tartozik**
- **Q5.** A napi menü ára és időablaka (meddig kérhető).
- **Q6.** A teljes étlap tételekkel és árakkal, allergénjelöléssel.
- **Q7.** Rendezvény-menüsorok és irányárak fejenként.
- **Q8.** Mennyivel előre kell foglalni rendezvényt? Van-e minimum létszám?
- **Q9.** A szombat esti retro élőzene pontos kezdése; van-e belépő?
- **Q10.** Parkolás: hány hely, ingyenes-e? Melyik busszal érhető el?
- **Q11.** Van-e akadálymentes bejárat és mosdó? (valódi vendégkérdés)
- **Q12.** Vegán/gluténmentes: hány tétel, állandó vagy kérésre?
- **Q13.** Terasz/kerthelyiség szezonja: mettől meddig üzemel?
- **Q14.** Az 1982 óta eltelt idő mérföldkövei — a sajtócikkeken túl mi az,
  amit a vendéglő maga akar elmondani?
- **Q15.** Van-e jogtiszta fotóanyag, vagy fotózni kell?

**Technikai**
- **Q16.** Kié a domain és a tárhely? Van-e hozzáférés?
- **Q17.** Van-e ma bármilyen foglalási vagy CRM-rendszer (akár Excel)?
- **Q18.** Ki tölti fel hetente a menüt, és milyen eszközzel? (a szerkesztői
  felületet hozzá kell tervezni)
- **Q19.** A Wolt/Foodora linkek maradnak, vagy saját rendelés a cél?
- **Q20.** A Google Cégprofilhoz van-e hozzáférés?

---

## 16. Az anyag leggyengébb pontja — őszintén

**A prototípus egyetlen valódi ára sincs benne, és ez nem apró hiány.**

Egy vendéglő weboldalán az ár nem díszítés, hanem a fő tartalom. A menükártyák,
az étlap-szekció és a rendezvénycsomagok mind `[ár] Ft` placeholderrel állnak,
mert a `dianavendeglo.hu`, a Wolt és a Foodora lekérése blokkolt volt, és nem
voltam hajlandó számot kitalálni. Ennek az a következménye, hogy **a főoldal
tipográfiai ritmusa árakkal ki lesz próbálva először élesben**: nem tudom, hogy
egy 12 szavas ételnév és egy négyjegyű ár hogyan tördelődik 375px-en, amíg nem
látom a valódi étlapot. Ez a legvalószínűbb hely, ahol a design szét fog esni.

Két további gyenge pont, sorrendben:

**Második: a performance-fejezet egy oldalról szól, amit nem mértem.** A 11.
fejezet célszámai védhetők, de a „mennyivel lesz jobb" kérdésre nincs válaszom,
mert nincs baseline. A `/wp/` és a `<title>`-ek **[T]** szintű bizonyítékok — a
képméretekről és a plugin-terhelésről szóló minden mondatom **[V]**, azaz
mintaillesztés. Ha valaki ezt tényként idézi az ügyfélnek, tévedni fog.

**Harmadik: a szignatúra elem kockázata a mérés.** A Napív azt feltételezi, hogy
a „mikor menjek?" valódi kérdés a Diana vendégeinél. Ez logikus, de nem mért. Ha
kiderül, hogy a látogatók 80%-a a napi menüért jön és a nyitvatartás nem kérdés,
akkor az ív egy szép, drága dekoráció marad, és a helyére a heti menü kellene.
Ezt az élesítés utáni első hónap eseménykövetése dönti el — nem én.

---

## Melléklet: a szignatúra elem — „A Diana napja"

**Mi ez.** Egy inline SVG ív a hero alatt, ami a vendéglő egy napját rajzolja ki
11:00-tól zárásig. Az ív három sávra van osztva — **napi menü**, **à la carte**,
**esti élőzene** —, és egy jelölő mutatja, hogy a látogató *most* hol áll ebben a
napban. Szombaton a harmadik sáv 23:00-ig nyúlik, és „retro élőzene" feliratot kap.

**Miért pont ez.**
1. **A szolgáltatás lényegét mutatja meg, nem mondja el.** A Diana nem egy
   étlap, hanem egy **napi ritmus**: 1982 óta minden nap ugyanaz az ív. Ezt egy
   fotó nem tudja megmutatni, egy bekezdés pedig elmondaná — ami gyengébb.
2. **Egyszerre válaszol a három leggyakoribb kérdésre**: nyitva vagytok?
   meddig? mikor van élőzene?
3. **Nem fotón múlik.** Nincs szükség jogtiszta képanyagra ahhoz, hogy az oldal
   megjegyezhető legyen — ez a brief kifejezett elvárása volt.
4. **A vendéglő saját világából jön.** Nem absztrakt grafika: a nyitvatartás
   maga, amit ma egy táblázatban közölnek.
5. **Élő adat.** A látogató saját órájából számol; nem lehet elavult.

**Mibe kerül LCP-ben.**

| Tétel | Költség |
|---|---|
| Inline SVG jelölés | ~1,7 KB nyers, ~700 B Brotli után |
| CSS (ív, sávok, jelölő) | ~0,9 KB nyers |
| JS (pozíciószámítás) | ~1,1 KB nyers, ~500 B tömörítve |
| Hálózati kérés | **0** — teljes egészében a HTML-ben van |
| Betűtöltés | **0** — a feliratok a már betöltött UI-fontot használják |
| **Hatás az LCP-re** | **≈ 0 ms.** Az LCP-elem a hero `h1` szövege, ami az ív előtt fest. Az ív a HTML-t ~2,5 KB-tal növeli, ami 1,6 Mbps-en ~13 ms letöltés és ~1 ms parse. |
| Hatás a CLS-re | **0** — az SVG-nek fix `viewBox`-a és `aspect-ratio`-ja van, a jelölő `transform`-mal mozog |
| Hatás az INP-re | **0** — a számítás egyszer fut betöltéskor, `requestAnimationFrame`-ben |

**Amiért kockázatos:** ha a nyitvatartás valaha eltér a beállítottól (ünnepnap,
zárva tartás), az ív **magabiztosan hazudik**. Ezért az élesített változatban a
nyitvatartás és az ünnepnapi kivételek a CMS-ből jönnek, egyetlen forrásból,
ahonnan a JSON-LD `OpeningHoursSpecification` is táplálkozik. Két helyen
karbantartott nyitvatartás előbb-utóbb szétcsúszik.

---

## Források

Rekonstrukcióhoz használt, indexelt források:
`dianavendeglo.hu` SERP-adatai (címek, URL-ek) · `pecsaktual.hu` ·
`pecsma.hu` · `utazzitthon.hu` · `hovamenjek.hu` · `nyitva.hu` ·
`etterem.hu` · `vendeglatasinfo.hu` · `legjobbettermek.hu` ·
`wolt.com` és `foodora.hu` listing-metaadatok · Google Cégprofil (brief).
