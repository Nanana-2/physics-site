// 試験を作る：選んだ問題（5問まで）をブラウザに保存する（登録不要・この端末だけ）。
// 問題ページでは「試験に追加」ボタンを，試験を作るページ（exam.md）では問題の選択と設定を受け持つ。
// 印刷用のページ（exam/print/）には，選んだ問題と設定を URL で渡す。
(() => {
  const KEY = "exam-problems";
  const SETTINGS = "exam-settings";
  const MAX = 5;
  const ID = /^[0-9a-z_]+\/[0-9a-z_]+\/[0-9a-z_]+$/;
  const read = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch (e) { return fallback; } };
  const write = (key, value) => { try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) {} };
  const chosen = () => read(KEY, []).filter((id) => ID.test(id)).slice(0, MAX);

  // 問題ページ：「試験に追加」ボタン
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
      button.textContent = note || (on ? `試験に追加済み（${list.length}/${MAX}）` : "試験に追加");
    };
    button.hidden = false;
    render();
    button.addEventListener("click", () => {
      const list = chosen();
      if (list.includes(id)) write(KEY, list.filter((x) => x !== id));
      else if (list.length >= MAX) { render(`試験に入れられるのは${MAX}問までです`); setTimeout(() => render(), 2500); return; }
      else write(KEY, [...list, id]);
      render();
    });
  };

  // 試験を作るページ
  const setupBuilder = async () => {
    const root = document.querySelector("[data-exam-builder]");
    if (!root) return;
    const $ = (s) => root.querySelector(s);
    const index = (await (await fetch(root.dataset.indexUrl)).json()).problems;
    const byId = new Map(index.map((p) => [p.url.replace(/\/$/, ""), p]));
    const base = new URL(".", location.href);

    // URL に問題や設定があれば，それを読み込む（共有されたリンク）
    const params = new URLSearchParams(location.search);
    const settings = Object.assign({ title: "", num: "mon", paper: "A4", book: "0", break: "0" }, read(SETTINGS, {}));
    if (params.get("p")) write(KEY, params.get("p").split(",").filter((id) => ID.test(id) && byId.has(id)).slice(0, MAX));
    ["title", "num", "paper", "book", "break"].forEach((k) => { if (params.has(k)) settings[k] = params.get(k); });
    write(SETTINGS, settings);

    const query = () => {
      const q = new URLSearchParams({ p: chosen().join(","), title: settings.title || "物理学 試験問題", num: settings.num, paper: settings.paper, book: settings.book, break: settings.break });
      return `?${q.toString()}`;
    };
    const status = (text) => { $("[data-exam-status]").textContent = text; if (text) setTimeout(() => { $("[data-exam-status]").textContent = ""; }, 2500); };

    // 選んだ問題の一覧（並べ替え・外す）
    const renderChosen = () => {
      const list = chosen();
      $("[data-exam-count]").textContent = `${list.length} / ${MAX}`;
      $("[data-exam-empty]").hidden = list.length > 0;
      $("[data-exam-chosen]").innerHTML = list.map((id, i) => {
        const p = byId.get(id);
        return `<li><a href="${new URL(`${id}/`, new URL("../", base))}">${p ? p.title : id}</a><span class="exam-builder__meta">${p ? `${p.subject}・${p.chapter}` : ""}</span>`
          + `<span class="exam-builder__ops"><button type="button" data-up="${i}" aria-label="上へ"${i ? "" : " disabled"}>↑</button>`
          + `<button type="button" data-down="${i}" aria-label="下へ"${i < list.length - 1 ? "" : " disabled"}>↓</button>`
          + `<button type="button" data-remove="${i}">外す</button></span></li>`;
      }).join("");
      const open = $("[data-exam-open]");
      open.href = `print/${query()}`;
      open.classList.toggle("is-disabled", !list.length);
      renderList();
    };
    $("[data-exam-chosen]").addEventListener("click", (e) => {
      const list = chosen();
      const b = e.target.closest("button");
      if (!b) return;
      const i = Number(b.dataset.up ?? b.dataset.down ?? b.dataset.remove);
      if (b.dataset.remove !== undefined) list.splice(i, 1);
      else { const j = b.dataset.up !== undefined ? i - 1 : i + 1; [list[i], list[j]] = [list[j], list[i]]; }
      write(KEY, list);
      renderChosen();
    });

    // 分野と章の選択，その範囲の問題の一覧（チェックで追加・外す）
    const subjects = [...new Map(index.map((p) => [p.subjectSlug, p.subject])).entries()];
    const subjectSel = $("[data-exam-subject]"), chapterSel = $("[data-exam-chapter]");
    subjectSel.innerHTML = subjects.map(([slug, name]) => `<option value="${slug}">${name}</option>`).join("");
    const fillChapters = () => {
      const chapters = [...new Map(index.filter((p) => p.subjectSlug === subjectSel.value).map((p) => [p.chapterSlug, p.chapter])).entries()];
      chapterSel.innerHTML = '<option value="">すべての章</option>' + chapters.map(([slug, name]) => `<option value="${slug}">${name}</option>`).join("");
    };
    const inRange = () => index.filter((p) => p.subjectSlug === subjectSel.value && (!chapterSel.value || p.chapterSlug === chapterSel.value));
    const renderList = () => {
      const list = chosen();
      const full = list.length >= MAX;
      $("[data-exam-list]").innerHTML = inRange().map((p) => {
        const id = p.url.replace(/\/$/, "");
        const on = list.includes(id);
        return `<li><label><input type="checkbox" value="${id}"${on ? " checked" : ""}${!on && full ? " disabled" : ""}> ${p.title}</label><span class="exam-builder__meta">${p.chapter}・${p.difficulty}</span></li>`;
      }).join("");
    };
    $("[data-exam-list]").addEventListener("change", (e) => {
      const id = e.target.value;
      const list = chosen().filter((x) => x !== id);
      if (e.target.checked) list.push(id);
      write(KEY, list.slice(0, MAX));
      renderChosen();
    });
    subjectSel.addEventListener("change", () => { fillChapters(); renderList(); });
    chapterSel.addEventListener("change", renderList);

    // 範囲からランダムに選ぶ（すでに選んだ問題は除き，5問を超えない）
    const countSel = $("[data-exam-random-count]");
    countSel.innerHTML = [1, 2, 3, 4, 5].map((n) => `<option value="${n}"${n === 3 ? " selected" : ""}>${n}</option>`).join("");
    $("[data-exam-random]").addEventListener("click", () => {
      const list = chosen();
      const room = MAX - list.length;
      if (room <= 0) { status(`すでに${MAX}問選んでいます`); return; }
      const pool = inRange().map((p) => p.url.replace(/\/$/, "")).filter((id) => !list.includes(id));
      for (let i = pool.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [pool[i], pool[j]] = [pool[j], pool[i]]; }
      const add = pool.slice(0, Math.min(Number(countSel.value), room));
      write(KEY, [...list, ...add]);
      renderChosen();
      status(add.length ? `${add.length}問を加えました` : "この範囲に加えられる問題がありません");
    });

    // 試験の設定
    const title = $("[data-exam-title]");
    title.value = settings.title;
    title.addEventListener("input", () => { settings.title = title.value.trim(); write(SETTINGS, settings); renderChosen(); });
    [["exam-num", "num"], ["exam-paper", "paper"], ["exam-book", "book"]].forEach(([name, key]) => {
      root.querySelectorAll(`input[name="${name}"]`).forEach((r) => {
        r.checked = r.value === settings[key];
        r.addEventListener("change", () => { settings[key] = r.value; write(SETTINGS, settings); renderChosen(); });
      });
    });
    const brk = $("[data-exam-break]");
    brk.checked = settings.break === "1";
    brk.addEventListener("change", () => { settings.break = brk.checked ? "1" : "0"; write(SETTINGS, settings); renderChosen(); });

    $("[data-exam-open]").addEventListener("click", (e) => { if (!chosen().length) { e.preventDefault(); status("問題を選んでください"); } });
    $("[data-exam-share]").addEventListener("click", async () => {
      if (!chosen().length) { status("問題を選んでください"); return; }
      try { await navigator.clipboard.writeText(new URL(query(), base).href); status("リンクをコピーしました"); } catch (e) { status("コピーできませんでした"); }
    });

    const first = byId.get(chosen()[0]);
    if (first) subjectSel.value = first.subjectSlug;
    fillChapters();
    renderChosen();
  };

  const setup = () => { setupButton(); setupBuilder(); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
})();
