// 試験問題の印刷ページ：URL の設定に従って問題ページから問題と解答を取り出し，試験問題の体裁でページに割り付ける。
// 例：?p=01mechanics/03/03_050,02electromagnetism/01/01_010&title=物理学 期末試験&num=mon&paper=A4&break=0&book=0
// 設定は試験を作るページ（docs/exam.md と docs/javascripts/exam.js）が作る。
(() => {
  const SITE = "https://nanana-2.github.io/physics-site/";
  const MAX = 5;
  const PAPER = { A4: [210, 297], B5: [182, 257] }; // B5 は日本の B5（JIS）
  const q = new URLSearchParams(location.search);
  const ids = (q.get("p") || "").split(",").filter((id) => /^[0-9a-z_]+\/[0-9a-z_]+\/[0-9a-z_]+$/.test(id)).slice(0, MAX);
  const opt = {
    title: (q.get("title") || "物理学 試験問題").replace(/[<>&"]/g, ""),
    num: ["box", "dai", "mon"].includes(q.get("num")) ? q.get("num") : "mon",
    paper: q.get("paper") === "B5" ? "B5" : "A4",
    breakEach: q.get("break") === "1",
    book: q.get("book") === "1",
  };
  const label = (i) => opt.num === "box" ? `<span class="q-head__box">${i}</span>` : opt.num === "dai" ? `第 ${i} 問` : `問題 ${i}`;

  // 答えは黄色の下地ではなく枠で囲む。数式の中の日本語は本文と同じフォントにする
  window.MathJax = {
    tex: { inlineMath: [["\\(", "\\)"]], displayMath: [["\\[", "\\]"]], macros: { finalanswer: ["\\boxed{#1}", 1] } },
    svg: { fontCache: "global", mtextInheritFont: true },
    startup: { typeset: false },
  };

  const el = (html) => { const t = document.createElement("template"); t.innerHTML = html.trim(); return [...t.content.children]; };
  const status = (text) => { document.querySelector("[data-status]").textContent = text; };

  // 問題ページの HTML から，問題・考え方・解答を取り出す
  const extract = (doc, url) => {
    doc.querySelectorAll('img[src*="#only-dark"]').forEach((img) => img.remove());
    doc.querySelectorAll("img").forEach((img) => { img.src = new URL(img.getAttribute("src"), url).href; });
    // 数式の前後の半角スペースは消し，間隔は CSS でそろえる
    doc.querySelectorAll("span.arithmatex").forEach((m) => {
      [m.previousSibling, m.nextSibling].forEach((t, k) => {
        if (t && t.nodeType === 3) t.textContent = k ? t.textContent.replace(/^ +/, "") : t.textContent.replace(/ +$/, "");
      });
    });
    const parts = [...doc.querySelectorAll("h3.solution-part")].map((h) => {
      let a = h.nextElementSibling;
      while (a && !a.classList.contains("answer")) a = a.nextElementSibling;
      return { head: h.textContent.trim(), body: a ? [...a.querySelector(".answer__inner").children] : [] };
    });
    const notes = [...doc.querySelectorAll(".rigor-note__body")].map((n) => el(`<aside>補足：${n.innerHTML}</aside>`)[0]);
    return {
      title: doc.querySelector("h1.problem-title")?.textContent.trim() || "",
      problem: [...(doc.querySelector(".problem-box__body")?.children || [])],
      approach: [...(doc.querySelector(".approach")?.children || [])],
      parts,
      notes,
    };
  };

  // 流し込む要素の列。keep は次の要素と同じページに置く，page は新しいページから始める
  const blocks = (items) => {
    const prob = [], ans = [];
    items.forEach((it, i) => {
      prob.push({ node: el(`<h2 class="q-head">${label(i + 1)}</h2>`)[0], keep: true, page: i > 0 && opt.breakEach });
      it.problem.forEach((n) => prob.push({ node: n }));
      ans.push({ node: el(`<h2 class="q-head">${label(i + 1)}<span>${it.title}</span></h2>`)[0], keep: true });
      if (it.approach.length) {
        ans.push({ node: el('<p class="a-label">考え方</p>')[0], keep: true });
        it.approach.forEach((n) => ans.push({ node: n }));
      }
      it.parts.forEach((p) => {
        ans.push({ node: el(`<h3 class="a-part">${p.head}</h3>`)[0], keep: true });
        p.body.forEach((n) => ans.push({ node: n }));
      });
      it.notes.forEach((n) => ans.push({ node: n }));
      ans.push({ node: el(`<p class="a-source">出典：${SITE}${it.id}/</p>`)[0] });
    });
    return { prob, ans };
  };

  const newPage = (site) => {
    const [page] = el(`<section class="page"><div class="page__body"></div><footer class="page__foot"><span class="page__no"></span>${site ? `<span class="page__site">大学物理の問題集　${SITE}</span>` : ""}</footer></section>`);
    document.getElementById("pages").append(page);
    return page;
  };
  const fits = (body) => body.scrollHeight <= body.clientHeight + 1;

  // 要素を順にページへ入れ，はみ出したら次のページへ送る
  const paginate = (list, site, first) => {
    const pages = [];
    let page = first || newPage(site);
    pages.push(page);
    list.forEach((b, i) => {
      let body = page.querySelector(".page__body");
      if (b.page && body.children.length) { page = newPage(site); pages.push(page); body = page.querySelector(".page__body"); }
      body.append(b.node);
      if (fits(body) || body.children.length === 1) return;
      // 見出しが下端に取り残されないよう，直前の keep の要素も一緒に送る
      const move = [b.node];
      let prev = b.node.previousElementSibling, j = i - 1;
      while (prev && list[j] && list[j].keep && body.children.length > move.length + 1) { move.unshift(prev); prev = prev.previousElementSibling; j--; }
      page = newPage(site); pages.push(page);
      page.querySelector(".page__body").append(...move);
    });
    return pages;
  };

  const padTo4 = (pages, site) => { while (pages.length % 4) pages.push(newPage(site)); };
  const cover = (sub) => {
    const page = newPage(false);
    page.querySelector(".page__body").append(...el(`<div class="cover"><h1 class="exam-title">${opt.title}</h1><p class="cover__sub">${sub}</p></div>`));
    return page;
  };
  const number = (pages) => pages.forEach((p, i) => { p.querySelector(".page__no").textContent = i + 1; });

  // スマホなど画面が用紙より狭いときは，画面の上だけ縮めて見せる（印刷には影響しない）
  const fitScreen = () => {
    const pages = document.getElementById("pages");
    const page = pages.querySelector(".page");
    if (!page) return;
    pages.style.zoom = "";
    const scale = Math.min(1, (document.documentElement.clientWidth - 16) / page.offsetWidth);
    if (scale < 1) pages.style.zoom = scale;
  };

  const build = async () => {
    document.querySelector("[data-back]").href = `../${location.search}`;
    if (!ids.length) { status(""); document.getElementById("pages").innerHTML = '<p class="message">問題が選ばれていません。試験を作るページで問題を選んでください。</p>'; return; }
    const [w, h] = PAPER[opt.paper];
    document.documentElement.style.setProperty("--paper-w", `${w}mm`);
    document.documentElement.style.setProperty("--paper-h", `${h}mm`);
    document.getElementById("paper").textContent = `@page { size: ${w}mm ${h}mm; margin: 0; }`;
    document.title = `${opt.title}｜大学物理の問題集`;

    const base = new URL("../../", location.href);
    const items = await Promise.all(ids.map(async (id) => {
      const url = new URL(`${id}/`, base);
      const res = await fetch(url);
      if (!res.ok) throw new Error(id);
      return { id, ...extract(new DOMParser().parseFromString(await res.text(), "text/html"), url) };
    }));
    const { prob, ans } = blocks(items);

    // 数式を組み，フォントと図を読み込んでから大きさを測る
    const flow = document.getElementById("flow");
    flow.append(...prob.map((b) => b.node), ...ans.map((b) => b.node));
    while (!(window.MathJax && MathJax.typesetPromise)) await new Promise((r) => setTimeout(r, 50));
    await MathJax.startup.promise;
    await MathJax.typesetPromise([flow]);
    await document.fonts.ready;
    await Promise.all([...flow.querySelectorAll("img")].map((img) => img.complete ? 0 : new Promise((r) => { img.onload = img.onerror = r; })));

    if (opt.book) {
      // 冊子：問題と解答・解説に表紙をつけ，それぞれ 4 の倍数のページにそろえる
      const c1 = cover("問題");
      const p1 = paginate(prob, false);
      number(p1);
      padTo4([c1, ...p1], false);
      const c2 = cover("解答・解説");
      const p2 = paginate(ans, true);
      number(p2);
      padTo4([c2, ...p2], true);
    } else {
      const first = newPage(false);
      first.querySelector(".page__body").append(...el(`<h1 class="exam-title">${opt.title}</h1>`));
      const p1 = paginate(prob, false, first);
      const p2 = paginate([{ node: el('<h1 class="exam-title">解答・解説</h1>')[0], keep: true }, ...ans], true);
      number([...p1, ...p2]);
    }
    flow.remove();
    const total = document.querySelectorAll(".page").length;
    status(`${opt.paper}・${total} ページ`);
    const button = document.querySelector("[data-print]");
    button.disabled = false;
    button.addEventListener("click", () => window.print());
    fitScreen();
    window.addEventListener("resize", fitScreen);
    document.body.dataset.ready = "1";
  };
  build().catch(() => status("問題を読み込めませんでした。時間をおいて開き直してください。"));
})();
