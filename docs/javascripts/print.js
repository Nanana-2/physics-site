// 印刷：ダークモードで見ていても，紙にはライトモードの色と図で印刷する。印刷が終わったら元に戻す。
(() => {
  let saved = null;
  window.addEventListener("beforeprint", () => {
    saved = document.body.getAttribute("data-md-color-scheme");
    if (saved && saved !== "default") document.body.setAttribute("data-md-color-scheme", "default");
  });
  window.addEventListener("afterprint", () => {
    if (saved) document.body.setAttribute("data-md-color-scheme", saved);
    saved = null;
  });
})();
