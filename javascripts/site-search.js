// ヘッダーの検索：入力すると問題の候補（番号・タイトル・分野と章・★）を出し，最後に「すべての結果を見る」を置く
(() => {
  const MAX = 8;
  const LEVELS = { 基本: 1, 標準: 2, 発展: 3 };
  const normalize = (value) => String(value || "").normalize("NFKC").toLocaleLowerCase("ja").replace(/\s+/g, " ").trim();
  const escapeHtml = (value) =>
    String(value).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[c]));

  const setup = (form) => {
    const input = form.querySelector(".site-search__input");
    const box = form.querySelector(".site-search__results");
    let problems = null;
    let active = -1;

    const load = async () => {
      if (problems) return problems;
      const response = await fetch(new URL(form.dataset.indexUrl, window.location.href));
      const data = (await response.json()).problems || [];
      const position = {};
      data.forEach((p) => {
        const key = `${p.subjectSlug}/${p.chapterSlug}`;
        position[key] = (position[key] || 0) + 1;
        p.label = `${parseInt(p.chapter, 10)}-${position[key]}`;
        p.chapterName = p.chapter.replace(/^\d+\.\s*/, "");
        p.titleKey = normalize(p.title);
        p.haystack = normalize(`${p.title} ${p.subject} ${p.chapter} ${p.searchText}`);
      });
      problems = data;
      return problems;
    };

    const items = () => [...box.querySelectorAll(".site-search__item")];
    const highlight = (index) => {
      const list = items();
      active = list.length ? (index + list.length) % list.length : -1;
      list.forEach((item, i) => item.classList.toggle("is-active", i === active));
    };
    const close = () => { box.hidden = true; active = -1; };

    const render = async () => {
      const query = normalize(input.value);
      if (!query) { close(); return; }
      const words = query.split(" ");
      const data = await load();
      const hits = data.filter((p) => words.every((w) => p.haystack.includes(w)));
      // 問題名に当たったものを先に
      hits.sort((a, b) => Number(words.every((w) => b.titleKey.includes(w))) - Number(words.every((w) => a.titleKey.includes(w))));
      const finder = new URL(form.action, window.location.href);
      finder.searchParams.set("keyword", input.value.trim());
      box.innerHTML =
        hits.slice(0, MAX).map((p) => {
          const level = LEVELS[p.difficulty] || 0;
          const href = new URL(form.dataset.indexUrl.replace(/problem-index\.json$/, "") + p.url, window.location.href).href;
          return `<a class="site-search__item" role="option" href="${escapeHtml(href)}"><span class="site-search__num">${p.label}</span><span class="site-search__text"><span class="site-search__title">${escapeHtml(p.title)}</span><span class="site-search__where">${escapeHtml(p.subject)} › ${escapeHtml(p.chapterName)}</span></span><span class="site-search__stars"><span class="on">${"★".repeat(level)}</span><span class="off">${"☆".repeat(3 - level)}</span></span></a>`;
        }).join("") +
        (hits.length
          ? `<a class="site-search__item site-search__all" role="option" href="${escapeHtml(finder.href)}">すべての結果を見る（${hits.length}問） →</a>`
          : '<p class="site-search__empty">見つかりませんでした</p>');
      box.hidden = false;
      active = -1;
    };

    input.addEventListener("input", render);
    input.addEventListener("focus", () => { load(); if (input.value) render(); });
    input.addEventListener("keydown", (event) => {
      if (box.hidden) return;
      if (event.key === "ArrowDown") { event.preventDefault(); highlight(active + 1); }
      else if (event.key === "ArrowUp") { event.preventDefault(); highlight(active - 1); }
      else if (event.key === "Escape") { close(); }
      else if (event.key === "Enter" && active >= 0) { event.preventDefault(); items()[active].click(); }
    });
    document.addEventListener("click", (event) => { if (!form.contains(event.target)) close(); });
  };

  const initialize = () => document.querySelectorAll("[data-site-search]").forEach((form) => {
    if (form.dataset.ready) return;
    form.dataset.ready = "true";
    setup(form);
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initialize);
  else initialize();
})();
