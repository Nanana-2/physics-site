// 問題を印刷する：選んだ問題（8問まで）をブラウザに保存する（登録不要・この端末だけ）。
// 問題ページでは「印刷に追加」ボタンを，問題を印刷するページ（exam.md）では問題の選択と設定を受け持つ。
// 印刷用のページ（exam/print/）には，選んだ問題と設定を URL で渡す。
(() => {
  const KEY = "exam-problems";
  const SETTINGS = "exam-settings";
  const MAX = 8;
  const ID = /^[0-9a-z_]+\/[0-9a-z_]+\/[0-9a-z_]+$/;
  const read = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch (e) { return fallback; } };
  const write = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) {} };
  const chosen = () => read(KEY, []).filter((id) => ID.test(id)).slice(0, MAX);

  // 問題ページ：「印刷に追加」ボタン
  const setupButton = () => {
    const button = document.querySelector("[data-exam-toggle]");
    const m = location.pathname.match(/([0-9a-z_]+\/[0-9a-z_]+\/[0-9a-z_]+)\/(index\.html)?$/);
    if (!button || !m) return;
    const id = m[1];
    const render = (note) => {
      const list = chosen();
      const on = list.includes(id);
      button.classList.toggle("is-on", on);
      button.setAttribute("aria-pressed", String(on));
      button.textContent = note || (on ? `印刷に追加済み（${list.length}/${MAX}）` : "印刷に追加");
    };
    button.hidden = false;
    render();
    button.addEventListener("click", () => {
      const list = chosen();
      if (list.includes(id)) write(KEY, list.filter((x) => x !== id));
      else if (list.length >= MAX) { render(`選ぶことができるのは${MAX}問までです`); setTimeout(() => render(), 2500); return; }
      else write(KEY, [...list, id]);
      render();
    });
  };

  // 問題を印刷するページ
  const setupBuilder = async () => {
    const root = document.querySelector("[data-exam-builder]");
    if (!root) return;
    const $ = (sel) => root.querySelector(sel);
    const index = (await (await fetch(root.dataset.indexUrl)).json()).problems;
    const idOf = (p) => p.url.replace(/\/$/, "");
    const byId = new Map(index.map((p) => [idOf(p), p]));
    const base = new URL(".", location.href);
    const site = new URL("../", base);
    const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
    const label = (p) => `${Number(p.chapterSlug) || p.chapterSlug}-${Number(p.number.split("_")[1]) / 10}`;
    const LEVELS = { "基本": 1, "標準": 2, "発展": 3 };
    const stars = (p) => { const n = LEVELS[p.difficulty] || 0; return `<span class="toc-row__stars" aria-label="難易度 ${n}/3"><span class="on">${"★".repeat(n)}</span><span class="off">${"☆".repeat(3 - n)}</span></span>`; };

    // URL に問題や設定があれば，それを読み込む（共有されたリンク）
    const params = new URLSearchParams(location.search);
    const settings = Object.assign({ title: "", num: "mon", paper: "A4", book: "0", break: "0" }, read(SETTINGS, {}));
    if (params.get("p")) write(KEY, params.get("p").split(",").filter((id) => ID.test(id) && byId.has(id)).slice(0, MAX));
    ["title", "num", "paper", "book", "break"].forEach((k) => { if (params.has(k)) settings[k] = params.get(k); });
    write(SETTINGS, settings);

    const query = () => {
      const q = new URLSearchParams({ p: chosen().join(","), title: settings.title || "物理学 問題", num: settings.num, paper: settings.paper, book: settings.book, break: settings.break });
      return `?${q.toString()}`;
    };
    let timer;
    const status = (text) => { clearTimeout(timer); $("[data-exam-status]").textContent = text; timer = setTimeout(() => { $("[data-exam-status]").textContent = ""; }, 2500); };

    // 分野のタブと章の選択。その範囲の問題を一覧にし，行の「追加」で選ぶ
    const subjects = [...new Map(index.map((p) => [p.subjectSlug, p.subject])).entries()];
    let subject = subjects[0][0];
    // 章と難易度はチェックで複数選ぶ。分野を替えると章はすべて選んだ状態に戻す
    const chapterBox = $("[data-exam-chapters]");
    const levelBox = $("[data-exam-levels]");
    const tabs = $("[data-exam-subjects]");
    let chapters = new Set();
    const levels = new Set(Object.keys(LEVELS));
    tabs.innerHTML = subjects.map(([slug, name]) => `<button type="button" class="finder__subject finder__subject--${slug}" data-subject="${slug}">${esc(name)}</button>`).join("");
    const markChapters = () => {
      const all = chapterBox.querySelectorAll("[data-chapter]");
      all.forEach((b) => { const on = chapters.has(b.dataset.chapter); b.classList.toggle("is-on", on); b.setAttribute("aria-pressed", String(on)); });
      const every = chapters.size === all.length;
      const allButton = chapterBox.querySelector("[data-chapter-all]");
      allButton.classList.toggle("is-on", every);
      allButton.setAttribute("aria-pressed", String(every));
    };
    const fillChapters = () => {
      tabs.querySelectorAll("button").forEach((b) => b.classList.toggle("is-on", b.dataset.subject === subject));
      const list = [...new Map(index.filter((p) => p.subjectSlug === subject).map((p) => [p.chapterSlug, p.chapter])).entries()];
      chapters = new Set(list.map(([slug]) => slug));
      chapterBox.innerHTML = '<button type="button" class="exam-builder__chip exam-builder__check" data-chapter-all>すべて</button>'
        + list.map(([slug, name]) => `<button type="button" class="exam-builder__chip exam-builder__check" data-chapter="${slug}">${esc(name)}</button>`).join("");
      markChapters();
    };
    const inRange = () => index.filter((p) => p.subjectSlug === subject && chapters.has(p.chapterSlug) && levels.has(p.difficulty));
    const renderList = () => {
      const list = chosen();
      const full = list.length >= MAX;
      const rows = inRange();
      $("[data-exam-list]").innerHTML = rows.length ? rows.map((p) => {
        const id = idOf(p);
        const on = list.includes(id);
        return `<div class="toc-row exam-builder__row${on ? " is-on" : ""}"><span class="toc-row__num">${label(p)}</span>`
          + `<a class="toc-row__title" href="${new URL(p.url, site)}">${esc(p.title)}</a>${stars(p)}`
          + `<button type="button" class="exam-builder__add" data-toggle="${id}"${!on && full ? " disabled" : ""}>${on ? "✓ 追加済み" : "＋ 追加"}</button></div>`;
      }).join("") : '<p class="exam-builder__empty">章と難易度を選ぶと，ここに問題が並びます。</p>';
    };
    $("[data-exam-list]").addEventListener("click", (e) => {
      const b = e.target.closest("[data-toggle]");
      if (!b) return;
      const id = b.dataset.toggle;
      const list = chosen();
      write(KEY, list.includes(id) ? list.filter((x) => x !== id) : [...list, id].slice(0, MAX));
      renderChosen();
    });
    tabs.addEventListener("click", (e) => {
      const b = e.target.closest("[data-subject]");
      if (!b) return;
      subject = b.dataset.subject;
      fillChapters();
      renderList();
    });
    chapterBox.addEventListener("click", (e) => {
      const b = e.target.closest("button");
      if (!b) return;
      if (b.dataset.chapterAll !== undefined) {
        const all = [...chapterBox.querySelectorAll("[data-chapter]")].map((x) => x.dataset.chapter);
        chapters = new Set(chapters.size === all.length ? [] : all);
      } else if (chapters.has(b.dataset.chapter)) chapters.delete(b.dataset.chapter);
      else chapters.add(b.dataset.chapter);
      markChapters();
      renderList();
    });
    levelBox.addEventListener("click", (e) => {
      const b = e.target.closest("[data-level]");
      if (!b) return;
      if (levels.has(b.dataset.level)) levels.delete(b.dataset.level);
      else levels.add(b.dataset.level);
      b.classList.toggle("is-on", levels.has(b.dataset.level));
      b.setAttribute("aria-pressed", String(levels.has(b.dataset.level)));
      renderList();
    });

    // 範囲からランダムに選ぶ（すでに選んだ問題は除き，上限を超えない）。選んだ問題は問題番号の順に加える
    const countSel = $("[data-exam-random-count]");
    countSel.innerHTML = Array.from({ length: MAX }, (_, i) => i + 1).map((n) => `<option value="${n}"${n === 3 ? " selected" : ""}>${n}</option>`).join("");
    $("[data-exam-random]").addEventListener("click", () => {
      const list = chosen();
      const room = MAX - list.length;
      if (room <= 0) { status(`すでに${MAX}問選んでいます`); return; }
      const pool = inRange().map(idOf).filter((id) => !list.includes(id));
      for (let i = pool.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [pool[i], pool[j]] = [pool[j], pool[i]]; }
      const order = new Map(index.map((p, i) => [idOf(p), i]));
      const add = pool.slice(0, Math.min(Number(countSel.value), room)).sort((a, b) => order.get(a) - order.get(b));
      write(KEY, [...list, ...add]);
      renderChosen();
      status(add.length ? `${add.length}問を加えました` : "選んだ章と難易度に加えられる問題がありません");
    });

    // 選んだ問題の一覧（並べ替え・外す）
    const renderChosen = () => {
      const list = chosen();
      $("[data-exam-count]").textContent = `${list.length} / ${MAX}`;
      $("[data-exam-empty]").hidden = list.length > 0;
      $("[data-exam-clear]").hidden = !list.length;
      $("[data-exam-chosen]").innerHTML = list.map((id, i) => {
        const p = byId.get(id);
        return `<div class="toc-row exam-builder__row"><span class="toc-row__num">${i + 1}</span>`
          + `<span class="exam-builder__text"><a class="toc-row__title" href="${new URL(`${id}/`, site)}">${p ? esc(p.title) : id}</a><span class="exam-builder__meta">${p ? `${esc(p.subject)}・${esc(p.chapter)}` : ""}</span></span>`
          + `<span class="exam-builder__ops"><button type="button" data-up="${i}" aria-label="上へ"${i ? "" : " disabled"}>↑</button>`
          + `<button type="button" data-down="${i}" aria-label="下へ"${i < list.length - 1 ? "" : " disabled"}>↓</button>`
          + `<button type="button" data-remove="${i}" aria-label="外す">×</button></span></div>`;
      }).join("");
      const open = $("[data-exam-open]");
      open.href = `print/${query()}`;
      open.classList.toggle("is-disabled", !list.length);
      renderList();
    };
    $("[data-exam-chosen]").addEventListener("click", (e) => {
      const b = e.target.closest("button");
      if (!b) return;
      const list = chosen();
      const i = Number(b.dataset.up ?? b.dataset.down ?? b.dataset.remove);
      if (b.dataset.remove !== undefined) list.splice(i, 1);
      else { const j = b.dataset.up !== undefined ? i - 1 : i + 1; [list[i], list[j]] = [list[j], list[i]]; }
      write(KEY, list);
      renderChosen();
    });

    $("[data-exam-clear]").addEventListener("click", () => {
      write(KEY, []);
      renderChosen();
    });

    // 印刷の設定
    const title = $("[data-exam-title]");
    title.value = settings.title;
    title.addEventListener("input", () => { settings.title = title.value.trim(); write(SETTINGS, settings); renderChosen(); });
    root.querySelectorAll("[data-exam-option]").forEach((group) => {
      const key = group.dataset.examOption;
      const mark = () => group.querySelectorAll("button").forEach((b) => { b.classList.toggle("is-on", b.dataset.value === settings[key]); b.setAttribute("aria-pressed", String(b.dataset.value === settings[key])); });
      group.addEventListener("click", (e) => {
        const b = e.target.closest("button");
        if (!b) return;
        settings[key] = b.dataset.value;
        write(SETTINGS, settings);
        mark();
        renderChosen();
      });
      mark();
    });

    $("[data-exam-open]").addEventListener("click", (e) => { if (!chosen().length) { e.preventDefault(); status("問題を選んでください"); } });
    $("[data-exam-share]").addEventListener("click", async () => {
      if (!chosen().length) { status("問題を選んでください"); return; }
      try { await navigator.clipboard.writeText(new URL(query(), base).href); status("リンクをコピーしました"); } catch (e) { status("コピーできませんでした"); }
    });

    const first = byId.get(chosen()[0]);
    if (first) subject = first.subjectSlug;
    fillChapters();
    renderChosen();
  };

  const setup = () => { setupButton(); setupBuilder(); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
})();
