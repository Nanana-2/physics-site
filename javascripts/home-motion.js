/* トップページの背景と節の組み立て（ほかのページでは何もしない）
   1. 背景の帯：問題の図と問題文を横一列に並べた帯を何段か重ね，暗くして画面に止めて置く。
      帯は CSS のアニメーションでゆっくり横に流れる。スクロールや操作には反応しない。
   2. 節の組み立て：見出しとその中身を1つの節にまとめる。PC では見出しを左の列，中身を右の列に置く。
   帯の上（見出し・分野と難易度のカード）はダークモードの配色で表示する。
   「何のサイト？」から下は無地の面に載せる。この面はライトモードとダークモードの切り替えに従う。 */
(function () {
  var ringEl = document.querySelector("[data-home-ring]");
  if (!ringEl) return;
  var body = document.body;

  body.classList.add("home-motion");

  /* ---------- 帯の上の部分と，無地の面に分ける ---------- */
  var hero = document.querySelector(".home-hero");
  if (hero) hero.setAttribute("data-md-color-scheme", "slate");
  var inner = document.querySelector(".md-content__inner");
  /* 「何のサイト？」から下は無地の面にする。ただし .home-band（問題を探す・問題用紙・参考文献一覧の入口）では面を切り，
     帯をもう一度見せる。darks と sheets はそれぞれのまとまりの一覧 */
  var darks = [], sheets = [];
  if (inner) {
    var kids = Array.prototype.slice.call(inner.children), onSheet = false, box = null, kind = "";
    kids.forEach(function (el) {
      if (el.matches("h1")) return;
      if (el.matches("h2#about")) onSheet = true;
      var k = (onSheet && !el.matches(".home-band")) ? "sheet" : "dark";
      if (!box || k !== kind) {
        box = document.createElement("div"); box.className = k === "sheet" ? "home-sheet" : "home-dark"; kind = k;
        inner.insertBefore(box, el);
        (k === "sheet" ? sheets : darks).push(box);
      }
      box.appendChild(el);
    });
    if (sheets.length) sheets[sheets.length - 1].classList.add("home-sheet--last");

    /* 節の組み立て：見出しと，次の見出しまでの中身を section.home-sec にまとめる */
    darks.concat(sheets).forEach(function (box) {
      Array.prototype.forEach.call(box.querySelectorAll(":scope > h2.home-head"), function (h) {
        var sec = document.createElement("section"), main = document.createElement("div");
        sec.className = "home-sec"; main.className = "home-sec__body";
        box.insertBefore(sec, h);
        for (var n = h.nextElementSibling; n && !n.matches("h2"); ) { var nx = n.nextElementSibling; main.appendChild(n); n = nx; }
        sec.appendChild(h); sec.appendChild(main);
      });
    });
  }

  /* ---------- 背景の帯 ---------- */
  var N = 44, FIGS = 32;
  var base = ringEl.getAttribute("data-ring-base");
  var order = [];
  for (var i = 0; i < FIGS; i++) order.push(i);
  for (var k = 0; k < N - FIGS; k++) order.splice(2 + k * 3, 0, FIGS + k);  /* 図2枚ごとに問題文を1枚 */
  function src(n) { return base + (n < 10 ? "0" : "") + n + ".webp"; }

  var stage = document.createElement("div");
  stage.className = "home-ring__stage";
  ringEl.appendChild(stage);

  /* 1段は同じ並びを2回続けたもので，CSS で並び1回分だけ左へ動かしてから最初に戻す（継ぎ目が見えない）。
     段ごとに並びの始まりを半枚ずらし，円筒を切り開いたように見せる。
     スマホのアドレスバーの出し入れで高さが変わっても組み直さないよう，横幅が変わったときだけ組み直す */
  var builtWidth = 0, used = {};
  function build() {
    var vw = innerWidth;
    if (vw === builtWidth) return;
    builtWidth = vw;
    stage.innerHTML = ""; used = {};
    var w = vw < 600 ? 120 : 170, h = w * 460 / 640, gap = Math.round(w * 0.08);
    var per = Math.ceil(vw / (w + gap)) + 1;
    var rows = Math.ceil(Math.max(innerHeight, screen.height || 0) / (h + gap)) + 1;
    for (var j = 0; j < rows; j++) {
      var row = document.createElement("div"); row.className = "home-ring__row";
      row.style.top = (j * (h + gap) - h / 2) + "px";
      row.style.marginLeft = -((j % 2) * (w + gap) / 2) + "px";
      row.style.setProperty("--hr-shift", -(per * (w + gap)) + "px");
      row.style.animationDuration = (per * 9) + "s";
      for (var rep = 0; rep < 2; rep++) {
        for (var i = 0; i < per; i++) {
          var t = document.createElement("div"); t.className = "home-ring__tile";
          t.style.width = w + "px"; t.style.height = h + "px"; t.style.marginRight = gap + "px";
          var n = order[(j * per + i) % order.length];
          used[n] = true;
          t.style.backgroundImage = "url(" + src(n) + ")";
          row.appendChild(t);
        }
      }
      stage.appendChild(row);
    }
  }
  addEventListener("resize", build);
  build();

  /* 使う画像を読み終えてから帯を出す（遅い回線で1枚ずつ出てくるのを避ける。最大2.5秒待つ） */
  var ready = false;
  function onReady() { if (ready) return; ready = true; ringEl.classList.add("is-ready"); }
  (function preload() {
    var list = Object.keys(used), left = list.length;
    function one() { if (--left === 0) onReady(); }
    list.forEach(function (n) { var im = new Image(); im.onload = im.onerror = one; im.src = src(+n); });
    setTimeout(onReady, 2500);
  })();
})();
