(() => {
  const copyText = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }

    const input = document.createElement("textarea");
    input.value = text;
    input.setAttribute("readonly", "");
    input.style.position = "fixed";
    input.style.opacity = "0";
    document.body.append(input);
    input.select();
    const copied = document.execCommand("copy");
    input.remove();
    if (!copied) throw new Error("Copy failed");
  };

  const setupShare = (share) => {
    if (share.dataset.ready === "true") return;
    share.dataset.ready = "true";

    const pageUrl = new URL(window.location.href);
    pageUrl.hash = "";
    const url = pageUrl.href;
    const title = share.dataset.shareTitle || document.title;
    const encodedUrl = encodeURIComponent(url);
    const encodedTitle = encodeURIComponent(title);

    share.querySelector("[data-share-x]").href =
      "https://twitter.com/intent/tweet?text=" + encodedTitle + "&url=" + encodedUrl;
    share.querySelector("[data-share-facebook]").href =
      "https://www.facebook.com/sharer/sharer.php?u=" + encodedUrl;
    share.querySelector("[data-share-line]").href =
      "https://social-plugins.line.me/lineit/share?url=" + encodedUrl;

    const copy = share.querySelector("[data-share-copy]");
    const label = share.querySelector("[data-share-copy-label]");
    const status = share.querySelector("[data-share-status]");
    let resetTimer;

    copy.addEventListener("click", async () => {
      window.clearTimeout(resetTimer);
      try {
        await copyText(url);
        label.textContent = "コピーしました";
        status.textContent = "ページのURLをコピーしました。";
      } catch (error) {
        console.error("Could not copy page URL:", error);
        label.textContent = "コピーできませんでした";
        status.textContent = "ブラウザのアドレス欄からURLをコピーしてください。";
      }

      resetTimer = window.setTimeout(() => {
        label.textContent = "リンクをコピー";
        status.textContent = "";
      }, 2500);
    });
  };

  const initialize = () => {
    document.querySelectorAll("[data-page-share]").forEach(setupShare);
  };

  if (typeof document$ !== "undefined") {
    document$.subscribe(initialize);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }
})();
