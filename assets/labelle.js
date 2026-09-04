(function(){
/* ══════════════════════════════════════════════════════════════════════════
   PROTOTÍPUS-VISELKEDÉS — nulla külső függőség.
   1) téma  2) mobil fiók  3) dózisskála  4) űrlap  5) lépcsőzött megjelenés
   6) mai nap kiemelése a nyitvatartásban
   ══════════════════════════════════════════════════════════════════════════ */
'use strict';
const $ = (s, k = document) => k.querySelector(s);
const $$ = (s, k = document) => [...k.querySelectorAll(s)];
document.documentElement.classList.add('js');

/* ── 1. TÉMA — 3 állapot: auto / világos / sötét ───────────────────────── */
const temaGombok = $$('[data-tema-valto]');
const temaFest = t => {
  if (t === 'auto') delete document.documentElement.dataset.tema;
  else document.documentElement.dataset.tema = t;
  temaGombok.forEach(g =>
    g.setAttribute('aria-pressed', String(g.dataset.temaValto === t)));
};
let aktivTema = 'auto';
try { aktivTema = localStorage.getItem('lb-tema') || 'auto'; } catch (e) {}
temaFest(aktivTema);
temaGombok.forEach(g => g.addEventListener('click', () => {
  const t = g.dataset.temaValto;
  temaFest(t);
  try { t === 'auto' ? localStorage.removeItem('lb-tema')
                     : localStorage.setItem('lb-tema', t); } catch (e) {}
}));

/* ── 1b. AKTUÁLIS OLDAL JELÖLÉSE A NAVIGÁCIÓBAN ───────────────────────── */
const ittVagyok = document.body.dataset.oldal;
if (ittVagyok) $$(`nav a[data-oldal="${ittVagyok}"]`).forEach(a => {
  a.setAttribute('aria-current', 'page');
});

/* ── 2. MOBIL FIÓK ────────────────────────────────────────────────────── */
const fiok = $('#fiok'), scrim = $('#scrim'), menugomb = $('#menugomb');
if (fiok && scrim && menugomb) {
let elozoFokusz = null;
const fiokNyit = () => {
  elozoFokusz = document.activeElement;
  fiok.hidden = scrim.hidden = false;
  requestAnimationFrame(() => { fiok.classList.add('nyit'); scrim.classList.add('nyit'); });
  menugomb.setAttribute('aria-expanded', 'true');
  document.body.style.overflow = 'hidden';
  $('#fiokzar').focus();
};
const fiokZar = () => {
  fiok.classList.remove('nyit'); scrim.classList.remove('nyit');
  menugomb.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
  setTimeout(() => { fiok.hidden = scrim.hidden = true; }, 180);
  elozoFokusz?.focus();
};
menugomb.addEventListener('click', fiokNyit);
$('#fiokzar').addEventListener('click', fiokZar);
scrim.addEventListener('click', fiokZar);
fiok.addEventListener('click', e => { if (e.target.closest('a')) fiokZar(); });
document.addEventListener('keydown', e => {
  if (e.key !== 'Escape' || fiok.hidden) return;
  fiokZar();
});
/* Fókuszcsapda: a fiók nyitva tartja a Tab-kört. */
fiok.addEventListener('keydown', e => {
  if (e.key !== 'Tab') return;
  const f = $$('a[href],button:not([disabled])', fiok);
  const elso = f[0], utolso = f[f.length - 1];
  if (e.shiftKey && document.activeElement === elso) { utolso.focus(); e.preventDefault(); }
  else if (!e.shiftKey && document.activeElement === utolso) { elso.focus(); e.preventDefault(); }
});

}

/* ── 3. DÓZISSKÁLA ────────────────────────────────────────────────────── */
const X0 = 13.4, MM_PER_ML = 17.2;      /* 0 ml pozíciója / 1 ml hossza mm-ben */
const csuszka = $('#ml');
if (csuszka) {
const hu1 = n => n.toFixed(1).replace('.', ',');
const skalaFrissit = () => {
  const ml = +csuszka.value;
  const hossz = ml * MM_PER_ML;
  $('#toltet').setAttribute('width', hossz.toFixed(2));
  $('#dugattyu').setAttribute('x', (X0 + hossz).toFixed(2));
  $('#rud').setAttribute('d', `M${(X0 + hossz + 1.8).toFixed(2)} 26H73.4`);
  $('#ml-ertek').textContent = hu1(ml);
  $('#ml-csepp').textContent = Math.round(ml * 20);
  $('#ml-gramm').textContent = hu1(ml) + ' g';
  $('#ml-kanal').textContent = hu1(5 / ml) + ' adag';
  csuszka.setAttribute('aria-valuetext', hu1(ml) + ' milliliter');
};
csuszka.addEventListener('input', skalaFrissit);
skalaFrissit();
}

/* ── 4. ŰRLAP — validáció blur-on, összegző küldéskor ─────────────────── */
const urlap = $('#urlap'), osszegzo = $('#osszegzo'), lista = $('#osszegzo-lista');
if (urlap) {
$('#ts').value = Date.now();

const SZABALY = {
  nev: v => v.trim().length >= 2 ||
    'Írd be a neved — legalább 2 karakter.',
  telefon: v => /^[+\d][\d\s()/-]{8,}$/.test(v.trim()) ||
    'A telefonszám legalább 9 számjegy legyen — például 06 30 123 4567.',
  email: v => v.trim() === '' || /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v.trim()) ||
    'Az e-mail cím hiányos — például nev@pelda.hu.',
  hozzajarulas: (v, el) => el.checked ||
    'A válaszadáshoz a hozzájárulásod kell — pipáld ki a jelölőnégyzetet.'
};
const mezoDoboz = el => el.closest('[data-mezo]');
const hibaKiir = (el, uzenet) => {
  const doboz = mezoDoboz(el);
  const szoveg = $('.hibaszoveg span', doboz);
  if (uzenet) {
    doboz.dataset.hibas = 'true';
    szoveg.textContent = uzenet;
    el.setAttribute('aria-invalid', 'true');
  } else {
    doboz.dataset.hibas = 'false';
    szoveg.textContent = '';
    el.removeAttribute('aria-invalid');
  }
  return !uzenet;
};
const ellenoriz = el => {
  const sz = SZABALY[el.name];
  if (!sz) return true;
  const eredmeny = sz(el.value, el);
  return hibaKiir(el, eredmeny === true ? '' : eredmeny);
};
Object.keys(SZABALY).forEach(nev => {
  const el = urlap.elements[nev];
  el.addEventListener('blur', () => ellenoriz(el));
  el.addEventListener('input', () => {
    if (mezoDoboz(el).dataset.hibas === 'true') ellenoriz(el);
  });
});

urlap.addEventListener('submit', e => {
  const rosszak = Object.keys(SZABALY)
    .map(n => urlap.elements[n]).filter(el => !ellenoriz(el));

  if (rosszak.length) {
    e.preventDefault();
    lista.innerHTML = rosszak.map(el => {
      const cimke = $(`label[for="${el.id}"]`, mezoDoboz(el)).textContent
        .replace(/\s*\*\s*$/, '').trim();
      return `<li><a href="#${el.id}">${cimke}</a></li>`;
    }).join('');
    osszegzo.dataset.lathato = 'true';
    osszegzo.focus();
    rosszak[0].focus();
    return;
  }
  osszegzo.dataset.lathato = 'false';

  /* A prototípus nem küld hálózati kérést: itt csak a sikerállapotot mutatja.
     Élesben ez a sor törlendő — a form POST-ol a /idopont végpontra. */
  e.preventDefault();
  const gomb = $('#kuld');
  gomb.setAttribute('aria-disabled', 'true');
  gomb.innerHTML = '<span class="porgo" aria-hidden="true"></span><span>Küldés…</span>';
  setTimeout(() => {
    const vissza = $('#visszajelzes');
    vissza.textContent = 'Köszönjük, megkaptuk a kérésed. ' +
      '[X] órán belül visszajelzünk időpontjavaslattal. ' +
      '(Prototípus: valódi küldés nem történt.)';
    vissza.dataset.lathato = 'true';
    gomb.removeAttribute('aria-disabled');
    gomb.innerHTML = '<span>Időpontot kérek</span>';
  }, 700);
});

}

/* ── 5. LÉPCSŐZÖTT MEGJELENÉS ─────────────────────────────────────────── */
if ('IntersectionObserver' in window) {
  const figy = new IntersectionObserver((be, o) => {
    be.forEach(b => {
      if (!b.isIntersecting) return;
      b.target.classList.add('latszik');
      o.unobserve(b.target);
    });
  }, { rootMargin: '0px 0px -12% 0px' });
  $$('.lepcso').forEach(el => figy.observe(el));
} else {
  $$('.lepcso').forEach(el => el.classList.add('latszik'));
}

/* ── 5b. UGRÓSÁV — az éppen látott szakasz jelölése ────────────────────────
   A ui-ux-pro-max Navigation/Active State szabálya: a jelenlegi hely legyen
   vizuálisan jelölve. Az aloldalak hosszúak; horgonysáv nélkül a látogató
   elveszti a fonalat. */
const ugroLinkek = $$('.ugrosav a');
if (ugroLinkek.length && 'IntersectionObserver' in window) {
  const celok = ugroLinkek
    .map(a => ({ a, el: $(a.getAttribute('href')) }))
    .filter(x => x.el);
  const lathato = new Set();
  const jelol = () => {
    const elso = celok.find(x => lathato.has(x.el));
    celok.forEach(x => x.a.setAttribute('aria-current',
      String(!!elso && x === elso)));
  };
  const figy2 = new IntersectionObserver(be => {
    be.forEach(b => b.isIntersecting ? lathato.add(b.target)
                                     : lathato.delete(b.target));
    jelol();
  }, { rootMargin: '-25% 0px -60% 0px' });
  celok.forEach(x => figy2.observe(x.el));
}

/* ── 6. NYITVATARTÁS — a mai nap kiemelése ────────────────────────────────
   NYITVA: null = nincs dokumentált adat. Kitöltve így néz ki:
     const NYITVA = { 1:['09:00','16:00'], …, 0:null };
   Ilyenkor az állapotjelző valós nyitva/zárva állapotot mutat. */
const NYITVA = null;
const ma = new Date().getDay();
$(`#nyitva li[data-nap="${ma}"]`)?.classList.add('ma');
if ($('#allapot')) {
if (NYITVA) {
  const p = NYITVA[ma];
  const most = new Date().getHours() * 60 + new Date().getMinutes();
  const perc = s => +s.slice(0, 2) * 60 + +s.slice(3);
  const nyitva = p && most >= perc(p[0]) && most < perc(p[1]);
  $('#allapot').dataset.allapot = nyitva ? 'nyitva' : 'zarva';
  $('#allapot-szoveg').textContent = nyitva
    ? `Most nyitva — zárás ${p[1]}`
    : 'Most zárva — az online időpontkérés bármikor működik';
}
}
})();
