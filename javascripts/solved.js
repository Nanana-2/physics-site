// 「解いた」印：問題ページのボタンで付け外しし，ブラウザに保存する（登録不要・この端末だけ）。
// 一覧・サイドバー・検索結果・前後の問題の行に ✓ を付け，トップの分野タイルに「解いた数」を出す。
(() => {
  const KEY = "solved-problems";
  const read = () => { try { return new Set(JSON.parse(localStorage.getItem(KEY) || "[]")); } catch (e) { return new Set(); } };
  const write = (set) => { try { localStorage.setItem(KEY, JSON.stringify([...set])); } catch (e) {} };
  const path = (href) => new URL(href, location.href).pathname.replace(/index\.html$/, "");
  const ROWS = ".side-chapter__link, a.toc-row, a.page-nav__side, .site-search__item";

  const mark = () => {
    const solved = read();
    document.querySelectorAll(ROWS).forEach((a) => a.classList.toggle("is-solved", solved.has(path(a.href))));
    document.querySelectorAll("a.home-tile").forEach((tile) => {
      const base = path(tile.href);
      const done = [...solved].filter((p) => p.startsWith(base)).length;
      const count = tile.querySelector(".home-tile__count");
      if (!count) return;
      count.dataset.total = count.dataset.total || count.textContent;
      count.textContent = done ? `${done} / ${count.dataset.total} 解いた` : count.dataset.total;
      count.classList.toggle("has-solved", done > 0);
    });
  };

  const setup = () => {
    const button = document.querySelector("[data-solved-toggle]");
    if (button) {
      const here = path(location.href);
      const label = button.querySelector("[data-solved-label]");
      const render = () => {
        const on = read().has(here);
        button.classList.toggle("is-on", on);
        button.setAttribute("aria-pressed", String(on));
        label.textContent = on ? "解いた！" : "解いたら押す";
      };
      button.hidden = false;
      render();
      button.addEventListener("click", () => {
        const solved = read();
        solved.has(here) ? solved.delete(here) : solved.add(here);
        write(solved);
        render();
        mark();
      });
    }
    mark();
    // 検索結果など，あとから描かれる行にも付ける
    new MutationObserver(() => mark()).observe(document.body, { childList: true, subtree: true });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
})();
