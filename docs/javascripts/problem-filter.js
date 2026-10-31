// 「問題を探す」ページ：キーワード・分野・難易度で絞り込み，結果を章ごとの見出しの下に並べる
(() => {
  const LEVELS = { 基本: 1, 標準: 2, 発展: 3 };

  const normalize = (value) =>
    String(value || "")
      .normalize("NFKC")
      .toLocaleLowerCase("ja")
      .replace(/\s+/g, " ")
      .trim();

  const escapeHtml = (value) =>
    String(value).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[c]));

  const escapeRegExp = (value) => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

  const stars = (level) =>
    `<span class="toc-row__stars" aria-label="難易度 ${level}/3"><span class="on">${"★".repeat(level)}</span><span class="off">${"☆".repeat(3 - level)}</span></span>`;

  // 問題文のうちキーワードが当たった辺りを1行だけ抜き出し，その語に黄色の下地を敷く（数式は「…」で省く）
  const snippet = (problem, words) => {
    if (!words.length) return "";
    const text = problem.plainText;
    const at = normalize(text).indexOf(words[0]);
    if (at < 0) return "";
    const start = Math.max(0, at - 18);
    const part = escapeHtml(text.slice(start, at + words[0].length + 30));
    const pattern = new RegExp(`(${words.map((w) => escapeRegExp(escapeHtml(w))).join("|")})`, "gi");
    return `<span class="finder__snippet">${start > 0 ? "…" : ""}${part.replace(pattern, "<mark>$1</mark>")}…</span>`;
  };

  const setupFinder = async (finder) => {
    if (finder.dataset.ready === "true") return;
    finder.dataset.ready = "true";

    const keyword = finder.querySelector("[data-finder-keyword]");
    const subjects = finder.querySelector("[data-finder-subjects]");
    const levels = finder.querySelector("[data-finder-levels]");
    const count = finder.querySelector("[data-finder-count]");
    const results = finder.querySelector("[data-finder-results]");
    const state = { subject: "", level: "" };
    let problems = [];

    const render = () => {
      const words = normalize(keyword.value).split(" ").filter(Boolean);
      const hits = problems.filter(
        (p) =>
          (!state.subject || p.subjectSlug === state.subject) &&
          (!state.level || p.difficulty === state.level) &&
          words.every((w) => p.haystack.includes(w))
      );
      count.textContent = `${hits.length}問`;
      if (!hits.length) {
        results.innerHTML = '<p class="finder__empty">条件に合う問題がありません。</p>';
        return;
      }

      let html = "";
      let group = "";
      hits.forEach((p) => {
        const key = `${p.subjectSlug}/${p.chapterSlug}`;
        if (key !== group) {
          if (group) html += "</section>";
          group = key;
          const subjectLabel = state.subject ? "" : `<span class="finder__subject-label">${escapeHtml(p.subject)}</span>`;
          html += `<section class="toc-chapter"><h2 class="toc-chapter__head"><span class="toc-chapter__no">${p.chapterNumber}</span><span class="toc-chapter__title">${subjectLabel}${escapeHtml(p.chapterName)}</span></h2>`;
        }
        const href = new URL(`../${p.url}`, window.location.href).href;
        html += `<a class="toc-row finder__row" href="${escapeHtml(href)}"><span class="toc-row__num">${p.label}</span><span class="finder__text"><span class="toc-row__title">${p.number.endsWith("_900") ? "章末：" : ""}${escapeHtml(p.title)}</span>${snippet(p, words)}</span>${stars(LEVELS[p.difficulty] || 0)}</a>`;
      });
      results.innerHTML = `${html}</section>`;
    };

    const select = (group, selector, attribute, value) => {
      group.querySelectorAll(selector).forEach((button) => button.classList.toggle("is-on", button.dataset[attribute] === value));
    };

    try {
      const response = await fetch(new URL(finder.dataset.indexUrl, window.location.href));
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      problems = (await response.json()).problems || [];

      // 章の中で何問目か（1-1, 1-2, …）を，索引の並び順から付ける
      const position = {};
      problems.forEach((p) => {
        const key = `${p.subjectSlug}/${p.chapterSlug}`;
        position[key] = (position[key] || 0) + 1;
        p.chapterNumber = parseInt(p.chapter, 10);
        p.chapterName = p.chapter.replace(/^\d+\.\s*/, "");
        p.label = `${p.chapterNumber}-${position[key]}`;
        p.plainText = p.searchText.replace(/\$[^$]*\$/g, "…").replace(/\s+/g, " ");
        p.haystack = normalize(`${p.title} ${p.subject} ${p.chapter} ${p.searchText}`);
      });

      // ?keyword= / ?subject= / ?difficulty= で条件を引き継ぐ（右上の検索や難易度タグから来たとき）
      const params = new URLSearchParams(window.location.search);
      keyword.value = params.get("keyword") || "";
      if (subjects.querySelector(`[data-subject="${params.get("subject")}"]`)) state.subject = params.get("subject");
      if (params.get("difficulty") in LEVELS) state.level = params.get("difficulty");
      select(subjects, "[data-subject]", "subject", state.subject);
      select(levels, "[data-level]", "level", state.level);
      render();

      keyword.addEventListener("input", render);
      subjects.addEventListener("click", (event) => {
        const button = event.target.closest("[data-subject]");
        if (!button) return;
        state.subject = button.dataset.subject;
        select(subjects, "[data-subject]", "subject", state.subject);
        render();
      });
      levels.addEventListener("click", (event) => {
        const button = event.target.closest("[data-level]");
        if (!button) return;
        state.level = state.level === button.dataset.level ? "" : button.dataset.level;
        select(levels, "[data-level]", "level", state.level);
        render();
      });
    } catch (error) {
      console.error("Problem index could not be loaded:", error);
      count.textContent = "問題一覧を読み込めませんでした。ページを再読み込みしてください。";
    }
  };

  const redirectDifficultyTags = () => {
    document.querySelectorAll('a.md-tag[href*="tag-index/"]').forEach((link) => {
      const difficulty = link.textContent.trim();
      if (!(difficulty in LEVELS)) return;
      const destination = new URL(link.href);
      destination.pathname = destination.pathname.replace(/tag-index\/?$/, "tags/");
      destination.hash = "";
      destination.search = "";
      destination.searchParams.set("difficulty", difficulty);
      link.href = destination.href;
    });
  };

  const initialize = () => {
    redirectDifficultyTags();
    document.querySelectorAll(".finder").forEach(setupFinder);
  };

  if (typeof document$ !== "undefined") {
    document$.subscribe(initialize);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }
})();
