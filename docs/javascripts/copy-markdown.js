// 「Markdownでコピー」：問題と解答を Markdown のままクリップボードへ（AI に質問するときなどに）
(() => {
  const setup = () => {
    const button = document.querySelector("[data-copy-markdown]");
    const source = document.getElementById("page-markdown");
    if (!button || !source || !navigator.clipboard) return;
    const label = button.querySelector("[data-copy-label]");
    button.hidden = false;
    button.setAttribute("aria-label", "Markdownでコピー");
    button.addEventListener("click", async () => {
      const text = source.textContent.replace(/<\\\//g, "</") + `\n\n出典：${location.href}\n`;
      try {
        await navigator.clipboard.writeText(text);
        label.textContent = "コピーしました";
      } catch (e) {
        label.textContent = "失敗しました";
      }
      // 結果を読めるように，2秒間は開いたままにする
      button.classList.add("is-copied");
      setTimeout(() => { label.textContent = "Markdownでコピー"; button.classList.remove("is-copied"); }, 2000);
    });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
})();
