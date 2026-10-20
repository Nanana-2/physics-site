// 問題ページ：小問ごとの解答を折りたたむ。「解答・解説」の帯の右に「すべて表示／すべて隠す」。
// 開いておくか閉じておくかの好みはブラウザに保存する（初期値は閉じる）。
(() => {
  const KEY = "answers-open";
  const setup = () => {
    const toggles = [...document.querySelectorAll("[data-answer-toggle]")];
    if (!toggles.length) return;
    let preferOpen = false;
    try { preferOpen = localStorage.getItem(KEY) === "1"; } catch (e) {}

    const set = (button, open) => {
      const answer = button.nextElementSibling;
      answer.classList.toggle("is-closed", !open);
      button.setAttribute("aria-expanded", String(open));
      button.textContent = open ? "解答を隠す" : "解答を見る";
    };
    toggles.forEach((button) => {
      button.hidden = false;
      set(button, preferOpen);
      button.addEventListener("click", () => set(button, button.getAttribute("aria-expanded") !== "true"));
    });

    const heading = document.querySelector("h2.solution-heading");
    if (heading && !heading.querySelector(".answer-all")) {
      const all = document.createElement("button");
      all.type = "button";
      all.className = "answer-all";
      const label = () => (all.textContent = preferOpen ? "すべて隠す" : "すべて表示");
      label();
      all.addEventListener("click", () => {
        preferOpen = !preferOpen;
        try { localStorage.setItem(KEY, preferOpen ? "1" : "0"); } catch (e) {}
        toggles.forEach((button) => set(button, preferOpen));
        label();
      });
      heading.append(all);
    }
    // 目次などで解答の見出しへ飛んできたら，その解答は開く
    const openFromHash = () => {
      const target = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
      const button = target && target.nextElementSibling;
      if (button && button.matches("[data-answer-toggle]")) set(button, true);
    };
    window.addEventListener("hashchange", openFromHash);
    openFromHash();
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
})();

// 補足（details.rigor-note）：開け閉めを，解答と同じくなめらかに伸び縮みさせる
(() => {
  const EASE = "cubic-bezier(.25, .8, .25, 1)";
  const setup = () => {
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    document.querySelectorAll("details.rigor-note").forEach((note) => {
      const summary = note.querySelector("summary");
      const body = note.querySelector(".rigor-note__body");
      if (!summary || !body || reduce) return;
      let anim = null;
      summary.addEventListener("click", (e) => {
        e.preventDefault();
        if (anim) anim.cancel();
        const opening = !note.open;
        if (opening) note.open = true;
        const full = body.scrollHeight;
        const from = opening ? 0 : full, to = opening ? full : 0;
        body.style.overflow = "hidden";
        anim = body.animate(
          [{ height: from + "px", opacity: opening ? 0 : 1 }, { height: to + "px", opacity: opening ? 1 : 0 }],
          { duration: 450, easing: EASE }
        );
        anim.onfinish = () => {
          if (!opening) note.open = false;
          body.style.overflow = ""; anim = null;
        };
      });
    });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
})();
