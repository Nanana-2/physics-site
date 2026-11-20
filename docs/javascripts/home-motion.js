/* トップページの動き（ほかのページでは何もしない）
   1. 円筒：問題の図と問題文を円筒に並べ，暗くした背景として画面に止めて置く。
      何もしていないときもゆっくり回り，スクロールするとその分だけ余計に回る。
   2. スクロールで現れる：見出し（左から順に現れる），分野・難易度のカード（横から），
      文章（まとまりごとにフェード）。
   3. 節の組み立て：見出しとその中身を1つの節にまとめる。PC では見出しを左の列，中身を右の列に置く。
   円筒の上（見出し・検索窓・分野と難易度のカード）はダークモードの配色で表示する。
   「このサイトについて」から下は無地の面に載せ，円筒の上へせり上がるようにする。
   この面はライトモードとダークモードの切り替えに従う。 */
(function () {
  var ringEl = document.querySelector("[data-home-ring]");
  if (!ringEl) return;
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var body = document.body;

  body.classList.add("home-motion");

  /* ---------- 円筒の上の部分と，無地の面に分ける ---------- */
  var hero = document.querySelector(".home-hero");
  if (hero) hero.setAttribute("data-md-color-scheme", "slate");
  var inner = document.querySelector(".md-content__inner");
  var dark = null, sheet = null;
  if (inner) {
    var kids = Array.prototype.slice.call(inner.children), cut = -1;
    kids.forEach(function (el, i) { if (cut < 0 && el.matches("h2#about")) cut = i; });
    var top = kids.filter(function (el, i) { return (cut < 0 || i < cut) && !el.matches("h1"); });
    var rest = cut < 0 ? [] : kids.slice(cut);
    if (top.length) {
      dark = document.createElement("div"); dark.className = "home-dark";
      inner.insertBefore(dark, top[0]); top.forEach(function (el) { dark.appendChild(el); });
    }
    if (rest.length) {
      sheet = document.createElement("div"); sheet.className = "home-sheet";
      inner.insertBefore(sheet, rest[0]); rest.forEach(function (el) { sheet.appendChild(el); });
    }
  }

  /* ---------- 円筒 ---------- */
  var N = 44, PER = 14, FIGS = 32;
  var base = ringEl.getAttribute("data-ring-base");
  var order = [];
  for (var i = 0; i < FIGS; i++) order.push(i);
  for (var k = 0; k < N - FIGS; k++) order.splice(2 + k * 3, 0, FIGS + k);  /* 図2枚ごとに問題文を1枚 */

  var stage = document.createElement("div");
  stage.className = "home-ring__stage";
  ringEl.appendChild(stage);
  var rings = [];

  /* 回し方：何もしていないときの回転は CSS のアニメーション（.home-ring__spin）に任せる。
     スクリプトはスクロールした分の回転だけを受け持ち，動きが収まったら描き直しを止める。
     タイルの明るさは一様にし，裏を向いたタイルは描かない（1コマごとの計算をなくすため） */
  function build() {
    stage.innerHTML = ""; rings.length = 0;
    var vw = innerWidth;
    var w = Math.max(64, Math.min(130, vw * 0.1)), h = w * 230 / 320, gap = h * 0.22;
    var r = (w * 1.08 * PER) / (2 * Math.PI);
    /* 円筒の左右の端が画面の外に出る大きさにする。scale() で拡大すると画像が粗く描かれるので，
       タイルの大きさ・半径・奥行き（perspective）をそろえて S 倍にする（見え方は拡大と同じ） */
    var S = Math.max(1.3, 1.15 * vw / (2 * r));
    w *= S; h *= S; gap *= S; r *= S;
    ringEl.style.perspective = (1500 * S).toFixed(0) + "px";
    /* 上下の端も画面の外に出る段数にする */
    var RINGS = Math.max(6, Math.ceil(innerHeight / (h + gap)) + 3);
    for (var j = 0; j < RINGS; j++) {
      var ring = document.createElement("div"); ring.className = "home-ring__ring";
      var spin = document.createElement("div"); spin.className = "home-ring__spin";
      for (var i = 0; i < PER; i++) {
        var t = document.createElement("div"); t.className = "home-ring__tile";
        t.style.width = w + "px"; t.style.height = h + "px";
        t.style.marginLeft = -w / 2 + "px"; t.style.marginTop = -h / 2 + "px";
        var n = order[(j * PER + i) % order.length];
        t.style.backgroundImage = "url(" + base + (n < 10 ? "0" : "") + n + ".webp)";
        var a0 = (360 / PER) * i + j * (180 / PER);
        t.style.transform = "rotateY(" + a0 + "deg) translateZ(" + r + "px)";
        spin.appendChild(t);
      }
      ring.appendChild(spin);
      stage.appendChild(ring);
      rings.push({ el: ring, dy: (j - (RINGS - 1) / 2) * (h + gap), k: 0.12 - 0.07 * j / (RINGS - 1), cur: target() });
    }
    rings.forEach(draw);
  }

  /* スクロールした分の回転（下の段ほど遅れてついてくる） */
  function target() { return scrollY * 0.05; }
  function draw(rg) { rg.el.style.transform = "translateY(" + rg.dy + "px) rotateX(-8deg) rotateY(" + (-rg.cur).toFixed(2) + "deg)"; }
  var running = false;
  function frame() {
    var goal = target(), moving = false;
    rings.forEach(function (rg) {
      rg.cur += (goal - rg.cur) * (reduce ? 1 : rg.k);
      if (Math.abs(goal - rg.cur) > 0.02) moving = true; else rg.cur = goal;
      draw(rg);
    });
    if (moving) requestAnimationFrame(frame); else running = false;
  }
  function kick() { if (!running) { running = true; requestAnimationFrame(frame); } }
  addEventListener("scroll", kick, { passive: true });
  addEventListener("resize", build);
  build();

  /* 画像を読み終えてから円筒を出す（遅い回線で1枚ずつ出てくるのを避ける。最大2.5秒待つ）。
     透明度で出すと立体の表示が崩れるので，暗い状態から明るさを上げて出す（CSS の .is-ready） */
  var ready = false;
  function onReady() { if (ready) return; ready = true; ringEl.classList.add("is-ready"); }
  (function preload() {
    var left = N;
    function one() { if (--left === 0) onReady(); }
    for (var i = 0; i < N; i++) {
      var im = new Image(); im.onload = im.onerror = one;
      im.src = base + (i < 10 ? "0" : "") + i + ".webp";
    }
    setTimeout(onReady, 2500);
  })();

  /* ---------- スクロールで現れる ---------- */
  if (!("IntersectionObserver" in window) || reduce) return;
  if (!inner) return;
  var targets = [];
  function add(el, cls, delay) {
    el.classList.add("hm", cls);
    if (delay) el.style.setProperty("--hm-delay", delay + "ms");
    targets.push(el);
  }

  /* 文章のまとまり：このサイトについての前半（区切り線の前）と後半，約束，更新履歴 */
  function wrap(nodes) {
    if (!nodes.length) return null;
    var box = document.createElement("div");
    nodes[0].parentNode.insertBefore(box, nodes[0]);
    nodes.forEach(function (n) { box.appendChild(n); });
    return box;
  }
  Array.prototype.forEach.call(inner.querySelectorAll("h2#about"), function (h) {
    var first = [], second = [], hr = false;
    for (var n = h.nextElementSibling; n && !n.matches("h2"); n = n.nextElementSibling) {
      if (n.matches("hr")) { hr = true; second.push(n); continue; }
      (hr ? second : first).push(n);
    }
    var b1 = wrap(first), b2 = wrap(second);
    if (b1) add(b1, "hm-fade");
    if (b2) add(b2, "hm-fade");
  });

  /* カードのまとまり：物理は左から，物理数学は右から，難易度と印刷は下から入る */
  function group(nodes, dir) {
    var box = wrap(nodes.filter(Boolean));
    if (box) { box.classList.add("hm-slide", "hm-slide--" + dir); add(box, "hm-slide"); }
  }
  if (dark) {
    var subs = dark.querySelectorAll(":scope > h3.home-subhead");
    Array.prototype.forEach.call(subs, function (h3, i) {
      var nodes = [h3];
      for (var n = h3.nextElementSibling; n && !n.matches("h2, h3"); n = n.nextElementSibling) nodes.push(n);
      group(nodes, i === 0 ? "left" : "right");
    });
    /* 難易度と印刷は別の節なので，まとまりも分ける */
    group([dark.querySelector(":scope > .home-levels")], "up");
    group([dark.querySelector(":scope > .home-tiles--single")], "up");
  }

  var blocks = [];
  [dark, sheet].forEach(function (box) { if (box) blocks = blocks.concat(Array.prototype.slice.call(box.children)); });
  blocks.forEach(function (el) {
    if (el.matches("h1")) return;
    if (el.matches("h2.home-head")) { add(el, "hm-head"); return; }
    if (el.matches(".home-tiles")) {
      Array.prototype.forEach.call(el.children, function (card, i) {
        add(card, (i % 2 === 0 || el.matches(".home-tiles--single")) ? "hm-left" : "hm-right", Math.floor(i / 2) * 70);
      });
      return;
    }
    if (el.matches(".home-levels")) {
      Array.prototype.forEach.call(el.children, function (card, i) { add(card, "hm-left", i * 110); });
      return;
    }
    if (el.classList.contains("hm")) return;
    add(el, "hm-fade");
  });
  document.querySelectorAll(".md-content .page-share, .md-content .owner").forEach(function (el) { add(el, "hm-fade"); });

  /* 節の組み立て：見出しと，次の見出しまでの中身を section.home-sec にまとめる */
  [dark, sheet].forEach(function (box) {
    if (!box) return;
    Array.prototype.forEach.call(box.querySelectorAll(":scope > h2.home-head"), function (h) {
      var sec = document.createElement("section"), main = document.createElement("div");
      sec.className = "home-sec"; main.className = "home-sec__body";
      box.insertBefore(sec, h);
      for (var n = h.nextElementSibling; n && !n.matches("h2"); ) { var nx = n.nextElementSibling; main.appendChild(n); n = nx; }
      sec.appendChild(h); sec.appendChild(main);
    });
  });

  /* 見出しは最初ほとんど切り取られていて面積がないので，少しでも入ったら出す */
  var heads = [];
  targets = targets.filter(function (el) { if (el.classList.contains("hm-head")) { heads.push(el); return false; } return true; });
  if (sheet) { sheet.classList.add("hm", "hm-sheet"); heads.push(sheet); }
  var ioHead = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("is-shown");
      ioHead.unobserve(e.target);
    });
  }, { rootMargin: "0px 0px -12% 0px", threshold: 0 });


  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("is-shown");
      io.unobserve(e.target);
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.15 });
  function observeAll() {
    heads.forEach(function (el) { ioHead.observe(el); });
    targets.forEach(function (el) { io.observe(el); });
  }
  /* 円筒は最初から背景として置くので，見出しとカードはすぐに出し始める */
  observeAll();
})();
