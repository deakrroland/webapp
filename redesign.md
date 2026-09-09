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
> **Frissítés — az ügyfél képernyőképeket küldött a valódi oldalról.**
> Ezek alapján a következők ténnyé váltak vagy megváltoztak: a **valódi menüszerkezet**
> (9 menüpont, köztük három, amit a kereső nem indexelt), az **arculati színek**
> (a logó sötétzöld + arany), a **valódi étlap árakkal**, és egy új **kritikus
> hiba**: az étlap képfájlokban van. Ahol egy korábbi megállapításom megdőlt,
> ott ezt külön jelölöm: **[JAVÍTVA]**.
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
| Stáb | Racskó Gábor üzletvezető · Horváth Csaba üzletvezető-helyettes · Pécsi Norbert konyhafőnök | étlap lábléce [T] |
| Arculat | logó: **sötétzöld + arany**, „1982" évszámmal, D-monogram, „DIANA VENDÉGLŐ" felirat | képernyőkép [T] |
| Étlap | főételek 4900–5500 Ft; pizza **15:00-tól** 1800–3800 Ft; desszert 1600–1800 Ft; saláta 400–1000 Ft; köret 900–1200 Ft | étlap [T] |
| Árpolitika | „Áraink forintban értetendők és az ÁFÁ-t tartalmazzák." · „Az étteremben **nem számítunk fel szervízdíjat**." | étlap [T] |
| Csomagolás | doboz 100 Ft/db · pizzadoboz 200 Ft/db · alumínium tálca 500 Ft/db | étlap [T] |
| Egyesület | **Diana Vendéglő SE** — saját sportegyesület | menüpont [T] |
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

### 1.2 Struktúra — a valódi menü **[JAVÍTVA]**

A képernyőkép szerint a mobil menü **kilenc** pontból áll, nem hatból. Három
olyan oldal van benne, amit a kereső nem adott vissza:

```
Főoldal
Miért szeretik a „Dianát"          ← nem volt indexelve a keresésemben
Napi menü
Ajánlatok, aktualitások
Étel
Ital
Esküvői menü                        ← nem volt indexelve
Rendezvények
Diana Vendéglő SE                   ← nem volt indexelve (sportegyesület)
```

**Ez önmagában megállapítás:** kilenc oldalból három nem jött vissza a
keresőből. Ez vagy indexelési probléma (`noindex`, gyenge belső linkelés,
hiányzó sitemap), vagy a tartalom annyira vékony, hogy a Google nem tartja
érdemesnek megjeleníteni. **Ellenőrizendő a Search Console-ban** — ez a
0. fázis egyik konkrét feladata.

A navigáció **kilenc egyenrangú pontja** külön UX-probléma is: nincs hierarchia,
a „Diana Vendéglő SE" ugyanakkora súlyt kap, mint a „Napi menü".

A Google Cégprofil ezen felül két külön deep linket hirdet: **„Menü · dianavendeglo.hu"**
és **„Asztal foglalása · dianavendeglo.hu"**.

### 1.2b Arculat — ami eddig hiányzott az elemzésből

A logó: **sötétzöld körben arany „D"-monogram**, fölötte az **1982** évszám,
alatta „DIANA VENDÉGLŐ". A menülapok fejlécében ugyanez, arany vonallal
elválasztva, a lap hátterében halványzöld óriás-monogram vízjelként.

Ez **kész, működő és következetes arculat** — és az évszám benne van a logóban.
A redesign paletta ebből indul ki (7.0), nem külső hangulattáblából.

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
| **K6** | **AZ ÉTLAP KÉPFÁJLOKBAN VAN.** Az „Étel" oldal egy képnézegetőt (lightbox) nyit meg: nagyítás, teljes képernyő, megosztás, bezárás gombokkal. A menülapok **exportált képek**, nem HTML. | képernyőkép | **[T]** |
| **K7** | **A képes étlap mögött vízjel fut.** A halványzöld óriás-monogram az árak és az ételnevek alatt húzódik, ami rontja a kontrasztot és a kis kijelzős olvashatóságot. | képernyőkép | **[T]** |
| **K8** | **A Google Cégprofil „Menü" linkje képekre mutat.** A Google nem tud belőle menü-rich resultot építeni, mert nincs szövege. | K6 következménye | [V] |

### 2.2 UX

| # | Probléma | Bizonyíték | Szint |
|---|---|---|---|
| U1 | **A vendég legfontosabb kérdésére — „most nyitva vagytok?" — az oldal nem válaszol azonnal.** A nyitvatartás katalógusoldalakon van jól kiemelve, nem a sajátján. | A nyitvatartást a nyitva.hu és az etterem.hu SERP-snippetje adja vissza, nem a `dianavendeglo.hu` | [V] |
| U2 | **A 130 / 45 / 120 fős kapacitás nincs a döntési pontnál.** Ez a rendezvényszervező *egyetlen* kizáró kritériuma, mégis csak katalógusoldalakon olvasható jól. | a számok az utazzitthon.hu és hovamenjek.hu szövegében jelennek meg, nem a saját oldal SERP-snippetjeiben | [V] |
| U3 | **Az „Ajánlatok, aktualitások" oldal örök karbantartási adósság.** Az ilyen oldal 3 hét után elavul, és elavultan rosszabb, mint ha nem lenne. | oldalcím önmagában | [T] |
| U4 | **Étel és Ital két külön oldal.** Senki nem keres „ital"-ra; „étlap"-ra keres. Két kattintás egy döntéshez. | két külön indexelt URL | [T] |
| U5 | **[JAVÍTVA]** Van „Miért szeretik a »Dianát«" oldal — tehát a történet valószínűleg *szerepel* az oldalon. A probléma más: **ez az oldal nem jött vissza a keresőben**, és a főoldalon a képernyőkép alapján nem kap kiemelt helyet. A 43 év tehát megvan írva, csak nem dolgozik. | menüpont létezik, de nincs indexelve | [T] / [V] |
| U7 | **Kilenc egyenrangú menüpont, hierarchia nélkül.** A „Diana Vendéglő SE" ugyanolyan súlyú, mint a „Napi menü". A mobil menü egy képernyőt kitöltő, tagolatlan lista. | képernyőkép | **[T]** |
| U8 | **Az étlap két külön oldalon (Étel / Ital) és képként.** Az étel és az ital külön menüpont, és mindkettő képnézegető. Egy döntéshez két kattintás és egy lightbox. | képernyőkép | **[T]** |
| U6 | **A szombat esti retro élőzene nincs a főoldalon.** Ez heti visszatérő esemény és önálló látogatási ok. | a program a hovamenjek.hu-n van kiemelve | [V] |

### 2.3 SEO

| # | Probléma | Bizonyíték | Szint |
|---|---|---|---|
| S1 | **A `<title>`-ök duplikálják a márkanevet, és kulcsszóhalmozásba futnak.** Ténylegesen indexelt címek:<br>`Főoldal - Diana Vendéglő Diana Vendéglő házias ízvilág`<br>`Napi menü - Diana Vendéglő Diana Vendéglő napi menü`<br>`Étel - Diana Vendéglő Diana Vendéglő ételei`<br>`Ital - Diana Vendéglő Diana Vendéglő italok`<br>`Rendezvények - Diana Vendéglő Diana Vendéglő rendezvények` | SERP | **[T]** |
| S2 | **A főoldal címe a „Főoldal" szóval kezdődik.** A `<title>` első ~30 karaktere a legértékesebb hely a teljes weboldalon; itt egy olyan szó áll, amire soha senki nem keres. | SERP | [T] |
| S3 | **Egyetlen címben sincs benne, hogy „Pécs".** Egy lokális vendéglőnek ez a legfontosabb kulcsszava. | SERP | [T] |
| S4 | **Az oldal a saját tényeire nem rangsorol.** A „130 fős", „45 fős különterem", „1982" kifejezésekre katalógus- és sajtóoldalak jönnek elő, nem a `dianavendeglo.hu`. | keresési eredmények | [T] |
| S5 | **`/wp/` a kanonikus útvonalban** — minden belső link és minden backlink egy technikai szegmensen keresztül megy. | URL-struktúra | [T] |
| **S6** | **Az étlap teljes szövege — ~200 tétel, ~350 ár — nulla indexelhető szó.** Ez a weboldal legnagyobb tartalmi vagyona, és a Google számára nem létezik. | K6 | **[T]** |
| **S7** | **Kilencből három oldal nincs indexelve** („Miért szeretik a »Dianát«", „Esküvői menü", „Diana Vendéglő SE"). Az „Esküvői menü" különösen fáj: ez a legértékesebb kereskedelmi kulcsszó, ami a vendéglőnek van. | menü vs. keresési eredmények | [T] / [V] |
| **S8** | **Árellentmondás a Google-profil és az étlap között.** A Cégprofil 2000–6000 Ft/fő sávot hirdet; az étlapon a főételek 4900–5500 Ft, a pizza 3800 Ft. Egy főétel + egy ital reálisan a sáv tetején vagy fölötte van. Ez rossz elvárást állít, és a Google-ből érkező vendég a számlánál csalódik. | Cégprofil vs. étlap | **[T]** |

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

**A képként feltöltött étlap a legdrágább hiba az oldalon — és nem esztétikai.**
Amit egy képfájl elveszít:

| Elveszik | Következmény |
|---|---|
| Kereshetőség | Aki „sörben sült csülök Pécs"-re keres, soha nem talál rá a Dianára — pedig van neki, `Sörben sült sertéscsülök „Dianásan”`, 4900 Ft. |
| Kijelölhetőség | A vendég nem tud árat kimásolni, ételnevet elküldeni. |
| Képernyőolvasó | Vak vagy gyengénlátó vendégnek az étlap **nem létezik**. Egy `alt` szöveg 200 tételre nem megoldás. |
| Nagyítás | Aki 200%-ra nagyít, elmosódott képet kap, nem nagyobb betűt. |
| Fordítás | A böngésző-fordító nem éri el — külföldi vendégnek nulla. |
| Strukturált adat | Nem építhető `Menu` schema, tehát nincs menü-rich result a Google-ben. |
| Frissítés | Egy ár módosítása = új kép exportálása és feltöltése. Ezért avulnak el a képes étlapok. |

A mögöttes ok itt is ugyanaz, mint a `/wp/`-nél: **a nyomdai anyagot tették fel
webre**, ahelyett hogy a webre készült volna tartalom. A menülap PDF-nek és
nyomtatásnak jó — weboldalnak nem az.

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
├── /etlap/                         Teljes étlap — SZÖVEGKÉNT (étel + ital)
├── /rendezvenyek/                  Rendezvény-hub
│   ├── /rendezvenyek/eskuvo/       ← a meglévő „Esküvői menü" ide költözik
│   ├── /rendezvenyek/ballagas/
│   └── /rendezvenyek/ceges/
├── /asztalfoglalas/                Foglalás
├── /a-diana/                       1982 óta — a történet
│                                     ← a meglévő „Miért szeretik a »Dianát«" ide
├── /kapcsolat/                     Cím, parkolás, megközelítés
├── /ajanlatok/                     Aktuális ajánlatok
└── /diana-se/                      Diana Vendéglő SE          ← megmarad, de a láblécbe
```

**Kilenc menüpontból öt marad a főnavigációban.** Az „Esküvői menü" a
rendezvény-ághoz kerül (ott keresik), a „Miért szeretik a »Dianát«" beolvad az
`/a-diana/`-ba, a „Diana Vendéglő SE" a láblécbe megy. Nem törlöm egyiket sem —
átsorolom őket oda, ahol a keresési szándékkal találkoznak.

| URL | Miért pont ez | Alternatíva, amit elvetettem |
|---|---|---|
| `/` a `/wp/` helyett | A `/wp/` semmit nem ad a vendégnek, és minden meglévő backlinket egy technikai szegmensen vezet át. Költözés + **301 minden `/wp/*` → `/*`**, a régi útvonalak élnek tovább átirányításként. | „Hagyjuk, működik." — működik, de minden jövőbeli linket is rontani fog, és a javítás költsége az idővel nő, nem csökken. |
| `/napi-menu/` **változatlanul** | Ez az egyetlen URL, aminek bizonyíthatóan van visszatérő keresési kereslete és belső értéke. Nem nyúlok hozzá; csak a `/wp/` esik le róla. | `/heti-menu/` — pontosabb lenne, de eldobná a meglévő indexelést egy szinonimáért. Nem éri meg. |
| `/etlap/` (Étel + Ital összevonva) | Senki nem keres „ital"-ra egy vendéglő kapcsán; „étlap"-ra keres. Egy oldal, `#levesek`, `#foetelek`, `#pizza`, `#italok` horgonyokkal. **A tételek HTML-szövegként, nem képként** — ez a redesign legnagyobb egyedi nyeresége (K6). 301: `/wp/etel/` és `/wp/ital/` → `/etlap/`. | Két oldal megtartása; illetve a képes étlap megtartása „mert így néz ki a nyomtatott" — a nyomtatott lap PDF-ként letölthető marad, de nem az lesz az oldal. |
| `/rendezvenyek/eskuvo/` a külön „Esküvői menü" helyett | Az esküvő rendezvény; aki esküvői helyszínt keres, a kapacitást és a menüsort együtt akarja látni. Az önálló „Esküvői menü" oldal ma nincs is indexelve. 301: `/wp/eskuvoi-menu/` → ide. | Önálló `/eskuvoi-menu/` megtartása — megőrizné a mai állapotot, ami bizonyíthatóan nem rangsorol. |
| `/diana-se/` a láblécbe | A sportegyesület valódi közösségi tény, és megtartandó — de nem étterem-választási szempont, tehát nem főnavigációs elem. | Törlés (elveszne egy valódi helyi kötődés) vagy főmenüben tartás (elveszi a helyet a foglalástól). |
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
| 3 | Ma a Dianában | napi menü kiemelés + ár | menü ára [P] |
| 4 | Az étlapról | 5 valódi főétel valódi árral, kategória-ársávok, „pizza 15:00-tól" | étlap [T] |
| 5 | Mit főzünk | kistermelő, vaslap/parázs/bogrács, **nincs szervizdíj**, SZÉP | [T] |
| 6 | Rendezvények | 130 / 45 / 120 fő, vizuális kapacitás | [T] |
| 7 | Szombat este | retro élőzene | [T] |
| 8 | 1982 óta | rövid történet + **a stáb névvel** + Diana Vendéglő SE | [T] |
| 9 | Vendégek | 4,2 ★ / 910 értékelés | [T] |
| 10 | Gyakorlati tudnivalók | nyitvatartás-táblázat, fizetés, kiszállítás | [T] |
| 11 | Asztalfoglalás | űrlap inline validációval | — |
| 12 | Lábléc | NAP-adatok, térkép, Diana SE, jogi | [T] |

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
│      └─── konyha ───┘└─ pizza is, 15:00-tól ─┘└─── este, élőzene ──┘  │
│                                                                       │
├───────────────────────────────────────────────────────────────────────┤
│  MA A DIANÁBAN — kedd                                                 │
│  ┌─────────────────────────┬─────────────────────────┐                │
│  │ A menü                  │ B menü                  │   [Teljes hét] │
│  │ [leves] · [főétel]      │ [leves] · [főétel]      │                │
│  │ [ár] Ft                 │ [ár] Ft                 │                │
│  └─────────────────────────┴─────────────────────────┘                │
├───────────────────────────────────────────────────────────────────────┤
│  AZ ÉTLAPRÓL — valódi tételek, valódi árak, HTML-szövegként           │
│  Sörben sült sertéscsülök „Dianásan"                        4 900 Ft  │
│    steak burgonyával, szalonnás savanyú káposztával                   │
│  Vörösboros marha pörkölt kapros-túrós galuskával           5 400 Ft  │
│  Vaslapos csirkemell sült zöldséggel                        4 900 Ft  │
│  Békacomb rántva házi steak burgonyával                     5 200 Ft  │
│  ──────────────────────────────────────────────────────────────────   │
│  Pizza 15:00-tól │ Desszertek   │ Saláták      │ Köretek              │
│  1 800–3 800 Ft  │ 1 600–1 800  │ 400–1 000    │ 900–1 200            │
│                                              [A teljes étlap →]       │
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
│  │   ▲ most 13:40   │        ritkább óracímkékkel
│  ╰──────────────────╯     │
│  11:00 ··········· 22:00  │
│  konyha · pizza 15:00-tól │
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
│ AZ ÉTLAPRÓL               │
│ Sörben sült sertéscsülök  │
│ „Dianásan"      4 900 Ft  │
│ steak burgonyával,        │
│ szalonnás savanyú kápo... │
│ ───────────────────────── │
│ Vörösboros marha pörkölt  │
│                 5 400 Ft  │
│ ───────────────────────── │
│ Pizza 15:00-tól           │
│ 1 800 – 3 800 Ft          │
│ → A teljes étlap          │
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

> **A kiindulópont a Diana saját étlapja: a menülap krémszínű papírja, a fejlécet
> lezáró arany vonal, és a logó sötétzöld körbe zárt arany monogramja az 1982-es
> évszámmal — három szín, amit a vendég minden egyes látogatáskor a kezében tart.**

Ez a paletta forrása. **[JAVÍTVA]** — az első változatban a nyári kerthelyiség
parazsából indultam ki (meszelt fehér, pörköltpaprika-vörös, parázs-narancs),
mert nem láttam a vendéglő arculatát. Amint a logó és a menülap előkerült,
kidobtam: **volt egy kész, következetes, 1982 óta épített arculat, és én egy
másikat találtam ki mellé.** A vörös paletta szép volt, de idegen. A meglévő
arculat felülírja a tervezői ötletet — ez a legfontosabb szabály egy 43 éves
márkánál.

A zöld–arany páros ráadásul **jobb is**, mint amit kitaláltam volna:
- a zöld a Kertvároshoz és a kerthelyiséghez is köt, nem csak a logóhoz;
- az arany a menülap vonalából jön, tehát az ár és a kiemelés természetes színe;
- és nem esik bele az „étterem = piros" klisébe, amit a brief is tilt.

Amit a kerthelyiség parazsából megtartottam: a **krémszínű, meleg alap**
(`#F4F1E7`), ami a menülap papírja — nem hideg fehér, nem szürke.

### 7.1 Színtokenek — 8 nevesített token, mért kontraszttal

A kontrasztértékeket WCAG 2.1 relatív luminancia szerint számoltam
(`(L1+0.05)/(L2+0.05)`), nem becsültem.

**Világos mód**

| Token | Hex | Szerep | Kontraszt |
|---|---|---|---|
| `--lap` | `#F4F1E7` | oldalháttér (a menülap papírja) | alap |
| `--abrosz` | `#FFFDF7` | kártya-, űrlapfelület | 1,10 : 1 a `--lap`-hoz (szándékos: elválasztás vonallal, nem világossággal) |
| `--tinta` | `#1B211A` | elsődleges szöveg (zöldre hangolt feketésbarna, nem semleges szürke) | **14,53 : 1** a `--lap`-on · 16,14 : 1 az `--abrosz`-on — AAA |
| `--fust` | `#5C6357` | másodlagos szöveg | **5,50 : 1** · 6,11 : 1 — AA |
| `--kert` | `#2C6B31` | **a logó zöldje** — elsődleges akció, márkaszín | **5,71 : 1** · 6,34 : 1 — AA; fehér **rajta 6,45 : 1** |
| `--arany` | `#856512` | **a menülap arany vonala** — kiemelés, ár, fókuszgyűrű | **4,80 : 1** · 5,34 : 1 — AA; fehér rajta 5,43 : 1 |
| `--este` | `#2A3326` | a nap utolsó szakasza a Napíven, harmadik sáv | **11,61 : 1** — AAA |
| `--vonal` | `#8A8770` | űrlapkeret, aktív határ | **3,21 : 1** a `--lap`-on — WCAG 1.4.11 ✓ |
| `--vonal-halk` | `#E0DCC8` | *csak dekoratív* elválasztó | 1,22 : 1 — soha nem hordoz információt |
| `--hiba` | `#A31B12` | hibaüzenet | **6,82 : 1** — AA |

**Sötét mód** — nem invertálás: a zöld és az arany világosítva és deszaturálva,
az alap pedig **zöldre hangolt sötét** (`#12150F`), nem `#000`:

| Token | Hex | Kontraszt a `--lap`-on (`#12150F`) |
|---|---|---|
| `--lap` | `#12150F` | alap |
| `--abrosz` | `#1B1F18` | 1,09 : 1 |
| `--tinta` | `#EDEBDE` | **15,39 : 1** · 13,97 : 1 az `--abrosz`-on — AAA |
| `--fust` | `#A0A692` | **7,34 : 1** · 6,66 : 1 — AA |
| `--kert` | `#86C08A` | **8,70 : 1**; sötét szöveg rajta 8,70 : 1 |
| `--arany` | `#D9B255` | **9,17 : 1**; sötét szöveg rajta 9,17 : 1 |
| `--este` | `#C9D6BC` | **12,13 : 1** |
| `--vonal` | `#787E6D` | **4,39 : 1** — 1.4.11 ✓ |
| `--vonal-halk` | `#2C3128` | 1,38 : 1 — dekoratív |
| `--hiba` | `#FFA898` | **9,92 : 1** |

**Alternatíva, amit elvetettem:** (1) a ui-ux-pro-max `--design-system` futása
`#DC2626` + `#F87171` + `#FEF2F2` „appetizing red" palettát javasolt — a `#DC2626`
a Tailwind `red-600` alapértéke, ma minden második étteremoldal ezt használja.
(2) A saját, első paprikavörös–parázs palettámat is elvetettem, amint láttam a
logót: **egy kész arculat mellé nem tervezünk másodikat.**

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
| `Menu` + `hasMenuSection` + `MenuItem` + `Offer` | étlap | **Megvan.** A prototípus JSON-LD-je 6 szekciót és 18 tételt tartalmaz valódi árral (`priceCurrency: "HUF"`), a pizzáknál `availabilityStarts: "15:00"`. Élesben mind a ~200 tétel. **Ez az a rich result, amit ma a képes étlap miatt nem lehet megkapni.** |
| `Offer` | napi menü ára | **[P]** — az egyetlen ár, ami még hiányzik |
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
| **Napív (szignatúra)** | hero | Egyetlen ábrán mutatja meg, hogy *mikor mi van*: konyha, pizza 15:00-tól, esti élőzene. A „mikor menjek?" kérdést döntéssé alakítja — és a pizza kezdési ideje az étlapról származó, dokumentált tény. |
| **Kapacitás-vizualizáció** | rendezvény-blokk | A 130/45/120 nem szám, hanem **méret** lesz. A rendezvényszervező egyetlen kizáró kritériumát azonnal ellenőrizhetővé teszi — a kizárás gyorsítása is konverzió. |
| **„Ma a Dianában" menü ár mellett** | 3. szekció | Az árat *előre* megadni bizalmi jelzés; az árat elrejteni a leggyakoribb ok, amiért egy vendég továbbáll. |
| **Telefon minden képernyőn** | fejléc + fix mobil sáv | Egy 43 éves vendéglő vendégköre telefonál. Az űrlap nem helyettesíti, kiegészíti. |
| **45 fő fölött automatikus átterelés** | foglalóűrlap | Megakadályozza, hogy nagy csoport rossz csatornán érkezzen — és így ne vesszen el. |
| **4,2 ★ / 910 értékelés, szám szerint** | vélemények | A 910 itt fontosabb, mint a 4,2: a mennyiség hitelesíti az átlagot. Egy 4,8-as átlag 12 értékeléssel gyengébb bizonyíték. |
| **1982. május 1.** | történet-blokk | Konkrét dátum, nem „több évtizedes múlt". A pontos dátum ellenőrizhető, tehát hihető. |
| **Valódi árak HTML-ben, a főoldalon** | étlap-szekció | Ma az árat egy képfájl őrzi, amit a kereső nem lát és a vendég nem tud kimásolni. Az ár kiírása a bizalom legolcsóbb formája — és a „mennyibe kerül?" az a kérdés, ami miatt a legtöbben továbbállnak. |
| **„Nem számítunk fel szervizdíjat"** | mit főzünk + étlap-fej | Ez a vendéglő saját, kiírt mondata az étlapon, és pontosan azt a szorongást oldja fel, amit a rejtett tételek okoznak. A számla kiszámíthatósága konverziós érv. |
| **A stáb névvel** | 1982-blokk | Racskó Gábor, Horváth Csaba, Pécsi Norbert. Egy 43 éves vendéglőnél a folytonosságot emberek testesítik meg, nem évszámok. Név + pozíció ellenőrizhető, tehát hiteles. |
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
| 6 | **Paletta a meglévő logóból: sötétzöld + arany + menülap-krém** | van kész, következetes arculat 1982 óta — mellé nem tervezünk másodikat | (a) ui-ux-pro-max `#DC2626`: Tailwind-alapérték; (b) a saját, első paprikavörös palettám: szép volt, de a valódi arculat láttán idegen — kidobtam |
| 6b | **Az étlap HTML-szövegként, nem képként** | a képes étlap egyszerre SEO-, akadálymentességi- és karbantartási hiba (K6). A nyomtatott lap PDF-ként letölthető marad. | A képek megtartása „mert így néz ki a nyomtatott" — ez a nyomdai anyagot teszi meg weboldalnak |
| 6c | **Kilenc menüpontból öt a főnavigációban** | az „Esküvői menü" a rendezvényekhez, a történet az `/a-diana/`-ba, a Diana SE a láblécbe — egyik sem törlődik, mindegyik oda kerül, ahol keresik | Mind a kilenc megtartása: hierarchia nélküli lista, amiben a foglalás elvész |
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
| **1. Technikai alap** | `/wp/` → gyökér, 301-térkép, HTTPS + HSTS ellenőrzés, `<title>`/meta újraírás mind a **9** meglévő oldalon, a nem indexelt három oldal kivizsgálása a Search Console-ban, JSON-LD alapgráf | **ez önmagában, redesign nélkül is javítja a rangsorolást** | 1–2 hét |
| **1b. Étlap-digitalizálás** | a ~200 tétel és ~350 ár átgépelése a képekről strukturált adatba (CMS-mező vagy CSV → `Menu` schema), a nyomtatott lap PDF-ként megmarad letöltésre | **a legnagyobb egyszeri tartalmi nyereség az egész projektben** | 1 hét, egyszeri adatrögzítés |
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
- **Q6.** ~~A teljes étlap tételekkel és árakkal~~ — **részben megvan** a küldött
  képekről (főételek, pizzák, desszertek, saláták, köretek). Ami még kell:
  a levesek, előételek, a teljes itallap, és **hogy melyik tétel vegán/vegetáriánus
  és melyik tartalmaz mely allergént** (ma az étlap csak annyit ír: „érdeklődjön
  munkatársainknál" — ez 2026-ban webre kevés).
- **Q6b.** **Melyik az igaz ár-sáv?** A Google Cégprofil 2000–6000 Ft/fő sávot
  hirdet, az étlap főételei 4900–5500 Ft. Egy főétel + ital reálisan a sáv
  tetején vagy fölötte van. A Cégprofilt kell javítani, vagy a sáv a napi menüre
  értendő? (S8)
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

**Az új képernyőképekből fakadó kérdések**
- **Q21.** Miért nincs indexelve a „Miért szeretik a »Dianát«", az „Esküvői menü"
  és a „Diana Vendéglő SE" oldal? (`noindex`? gyenge belső linkelés? hiányzó
  sitemap?) — Search Console-hozzáférés kell hozzá.
- **Q22.** Az étlap képek forrásfájlja megvan-e szerkeszthető formában (InDesign,
  Word, Canva)? Ha igen, a digitalizálás nem gépelés, hanem export.
- **Q23.** Mi az „Esküvői menü" oldal tényleges tartalma? Vannak-e fix csomagok
  és irányárak?
- **Q24.** A „Diana Vendéglő SE" aktív egyesület? Van-e saját mérkőzés- vagy
  eseménynaptár, amit az oldal megjeleníthetne?
- **Q25.** A napi menü ára és időablaka — **ez maradt az egyetlen ár, ami hiányzik.**

**Technikai**
- **Q16.** Kié a domain és a tárhely? Van-e hozzáférés?
- **Q17.** Van-e ma bármilyen foglalási vagy CRM-rendszer (akár Excel)?
- **Q18.** Ki tölti fel hetente a menüt, és milyen eszközzel? (a szerkesztői
  felületet hozzá kell tervezni)
- **Q19.** A Wolt/Foodora linkek maradnak, vagy saját rendelés a cél?
- **Q20.** A Google Cégprofilhoz van-e hozzáférés?

---

## 16. Az anyag leggyengébb pontja — őszintén

**Az első változat leggyengébb pontja az volt, hogy nem voltak árak. Ez megoldódott
— és közben kiderült, hogy ennél nagyobb baj is volt: rossz színt terveztem.**

Az első paletta paprikavörös és parázs-narancs volt, egy „a kerthelyiség parazsából
indulunk ki" indoklással, ami jól hangzott, és teljesen mellément: a Dianának
**1982 óta van sötétzöld–arany arculata**, benne az évszámmal. Ezt nem a
módszertan hibája okozta, hanem az, hogy a hálózati blokk miatt nem láttam a
logót, és a hiányt **ötlettel töltöttem ki ahelyett, hogy megkérdeztem volna.**
A tanulság a következő ügyfélre is áll: **az arculat nem az a mező, amit a
tervező tölt ki, ha üres.** Ha egy adat hiányzik, azt kérdésként kell felírni,
nem kreatív döntésként lezárni.

Ami **most** a leggyengébb:

**Első: a napi menü ára még mindig hiányzik** — és a napi menü az oldal
forgalmi motorja. Az étlap árai megvannak, tehát a tipográfiai ritmus valódi
számokon van kipróbálva (4 900 Ft, 5 400 Ft — a leghosszabb ételnév 62 karakter,
375px-en két sorba tördel, ellenőriztem). A napi menünél viszont még mindig
`[ár]` áll, és épp az az ár, amiért a legtöbben az oldalra jönnek.

**Második: a ~200 tételes étlapot nem gépeltem át.** A prototípusban 5 főétel és
a JSON-LD-ben 18 tétel szerepel valódi árral — a többi az 1b fázis munkája. Ez
nem tervezési, hanem adatrögzítési feladat, de amíg nincs kész, az `/etlap/`
oldal ígéret, nem tény. **A projekt legnagyobb hozamú része a legkevésbé
látványos része**, és nálam is ez maradt utoljára.

**Harmadik: a performance-fejezet továbbra is egy oldalról szól, amit nem
mértem.** A `/wp/`, a duplikált címek és a képes étlap **[T]** szintű
bizonyítékok. A képméretekről és a plugin-terhelésről szóló minden mondatom
**[V]** — mintaillesztés. A képes étlap miatt viszont most már majdnem biztos,
hogy a képsúly probléma: egy lightboxban ~20 nagy felbontású menülap fekszik.
Ez mérendő, nem állítandó.


---

## Melléklet: a szignatúra elem — „A Diana napja"

**Mi ez.** Egy inline SVG ív a hero alatt, ami a vendéglő egy napját rajzolja ki
11:00-tól zárásig. Az ív három sávra van osztva — **konyha**, **pizza is
(15:00-tól)**, **este / élőzene** —, és egy jelölő mutatja, hogy a látogató *most*
hol áll ebben a napban. Szombaton a harmadik sáv 23:00-ig nyúlik.

**A középső sáv határa dokumentált tény:** az étlapon szó szerint ez áll:
`PIZZÁINK (15:00-tól)`. Ez az egyetlen olyan időpont a vendéglő napjában, amit
maga az étlap rögzít — és pontosan ezt teszi az ív láthatóvá. A napi menü és a
zene kezdése egyelőre `[egyeztetendő]`, és a prototípusban is így van jelölve.

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
