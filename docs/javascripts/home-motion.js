/* トップページの動き（ほかのページでは何もしない）
   1. 円筒：問題の図と問題文を3段の円筒に並べる。見出しの下で2周半ほど回ってから暗くなり，
      画面に止まった背景として残る。あとはスクロールに合わせてゆっくり回る。
   2. スクロールで現れる：見出し（丸が大きくなってから帯が伸びる），分野・難易度のカード（横から），
      文章（まとまりごとにフェード）。
   トップは背景が暗いので，サイトのダークモードの配色で表示する。 */
(function () {
  var ringEl = document.querySelector("[data-home-ring]");
  if (!ringEl) return;
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var body = document.body;

  /* ---------- ダークモードの配色に固定する（Material の切り替えが上書きしても戻す） ---------- */
  function forceDark() { if (body.getAttribute("data-md-color-scheme") !== "slate") body.setAttribute("data-md-color-scheme", "slate"); }
  forceDark();
  new MutationObserver(forceDark).observe(body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
  body.classList.add("home-motion");

  /* ---------- 円筒 ---------- */
  var N = 44, RINGS = 3, PER = 14, FIGS = 32;
  var base = ringEl.getAttribute("data-ring-base");
  var order = [];
  for (var i = 0; i < FIGS; i++) order.push(i);
  for (var k = 0; k < N - FIGS; k++) order.splice(2 + k * 3, 0, FIGS + k);  /* 図2枚ごとに問題文を1枚 */

  var stage = document.createElement("div");
  stage.className = "home-ring__stage";
  ringEl.appendChild(stage);
  var rings = [], geo = {};
  var search = document.querySelector(".home-hero .home-search");
  var centerStart = 0;

  function build() {
    stage.innerHTML = ""; rings.length = 0;
    var vw = innerWidth;
    /* 最初は検索窓の下に収まる大きさにする（高さ 3h + 2gap = 約 2.48w） */
    var sb = search ? search.getBoundingClientRect().bottom + scrollY : innerHeight * 0.55;
    var avail = innerHeight - sb - 36;
    var w = Math.max(64, Math.min(150, vw * 0.11, avail / 2.48)), h = w * 230 / 320, gap = h * 0.22;
    geo = { w: w, h: h, total: 3 * h + 2 * gap, r: (w * 1.08 * PER) / (2 * Math.PI) };
    for (var j = 0; j < RINGS; j++) {
      var ring = document.createElement("div"); ring.className = "home-ring__ring";
      var tiles = [];
      for (var i = 0; i < PER; i++) {
        var t = document.createElement("div"); t.className = "home-ring__tile";
        t.style.width = w + "px"; t.style.height = h + "px";
        t.style.marginLeft = -w / 2 + "px"; t.style.marginTop = -h / 2 + "px";
        var n = order[(j * PER + i) % order.length];
        t.style.backgroundImage = "url(" + base + (n < 10 ? "0" : "") + n + ".jpg)";
        var a0 = (360 / PER) * i + j * (180 / PER);
        t.style.transform = "rotateY(" + a0 + "deg) translateZ(" + geo.r + "px)";
        ring.appendChild(t); tiles.push({ el: t, a0: a0 });
      }
      stage.appendChild(ring);
      rings.push({ el: ring, tiles: tiles, dy: (j - 1) * (h + gap), cur: 0 });
    }
    centerStart = startCenter();
  }

  /* 円筒の中心の高さ：最初は検索窓のすぐ下，暗くなったあとは画面の真ん中 */

  function startCenter() {
    var b = search ? search.getBoundingClientRect().bottom + scrollY : innerHeight * 0.55;
    return b + 24 + geo.total / 2;
  }

  var SPIN = 900, T_SPIN = [4200, 4700, 5200], T_DIM = 1400;
  var t0 = null, dimStart = null;
  function easeOut(x) { return 1 - Math.pow(1 - x, 3); }
  function smooth(x) { return x * x * (3 - 2 * x); }
  if (reduce) dimStart = -1e9;
  addEventListener("scroll", function () { if (dimStart === null && scrollY > 40) dimStart = performance.now(); }, { passive: true });

  function frame(now) {
    if (t0 === null) t0 = now;
    var el = now - t0;
    if (dimStart === null && el > T_SPIN[2]) dimStart = now;
    var d = dimStart === null ? 0 : smooth(Math.min(1, (now - dimStart) / T_DIM));
    var bright = 1 - 0.74 * d;
    /* 中心：最初の位置（ページの上からの距離）から，画面の真ん中に止まる位置へ */
    var startY = centerStart - scrollY, endY = innerHeight * 0.5;
    var cy = startY + (endY - startY) * d;
    stage.style.transform = "translateY(" + cy + "px) scale(" + (1 + 0.3 * d).toFixed(3) + ")";
    ringEl.style.setProperty("--home-ring-veil", (0.6 + 0.25 * d).toFixed(3));

    var scrollAngle = scrollY * 0.05;
    rings.forEach(function (rg, j) {
      var spin = reduce ? 0 : -SPIN * (1 - easeOut(Math.min(1, el / T_SPIN[j])));
      var target = spin + scrollAngle;
      rg.cur += (target - rg.cur) * (dimStart === null ? 1 : 0.12 - j * 0.03);
      rg.el.style.transform = "translateY(" + rg.dy + "px) rotateX(-8deg) rotateY(" + -rg.cur + "deg)";
      rg.tiles.forEach(function (t) {
        var c = Math.cos((t.a0 - rg.cur) * Math.PI / 180);
        t.el.style.filter = "brightness(" + ((0.35 + 0.65 * (c + 1) / 2) * bright).toFixed(3) + ")";
        t.el.style.zIndex = Math.round(c * 100);
      });
    });
    requestAnimationFrame(frame);
  }
  build();
  addEventListener("resize", build);
  requestAnimationFrame(frame);

  /* ---------- スクロールで現れる ---------- */
  if (!("IntersectionObserver" in window) || reduce) return;
  var inner = document.querySelector(".md-content__inner");
  if (!inner) return;
  var targets = [];
  function add(el, cls, delay) {
    el.classList.add("hm", cls);
    if (delay) el.style.setProperty("--hm-delay", delay + "ms");
    targets.push(el);
  }

  /* 文章のまとまり：何者？の前半（区切り線の前）と後半，約束，更新履歴 */
  function wrap(nodes) {
    if (!nodes.length) return null;
    var box = document.createElement("div");
    nodes[0].parentNode.insertBefore(box, nodes[0]);
    nodes.forEach(function (n) { box.appendChild(n); });
    return box;
  }
  Array.prototype.forEach.call(inner.querySelectorAll("h2.books-head"), function (h) {
    if (h.textContent.indexOf("何者") < 0) return;
    var first = [], second = [], hr = false;
    for (var n = h.nextElementSibling; n && !n.matches("h2"); n = n.nextElementSibling) {
      if (n.matches("hr")) { hr = true; second.push(n); continue; }
      (hr ? second : first).push(n);
    }
    var b1 = wrap(first), b2 = wrap(second);
    if (b1) add(b1, "hm-fade");
    if (b2) add(b2, "hm-fade");
  });

  Array.prototype.forEach.call(inner.children, function (el) {
    if (el.matches("h1")) return;
    if (el.matches("h2.books-head")) { add(el, "hm-head"); return; }
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

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("is-shown");
      io.unobserve(e.target);
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.15 });
  targets.forEach(function (el) { io.observe(el); });
})();
