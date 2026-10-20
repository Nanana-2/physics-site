// スマホの分野タブ（横スクロール）：今いる分野を見える位置へ，続きがある側の端をぼかす，初回だけ少し覗かせる
document.addEventListener("DOMContentLoaded", () => {
  const list = document.querySelector(".md-tabs__list");
  if (!list || list.scrollWidth <= list.clientWidth) return;

  const updateEdges = () => {
    list.classList.toggle("has-more-left", list.scrollLeft > 4);
    list.classList.toggle("has-more-right", list.scrollLeft + list.clientWidth < list.scrollWidth - 4);
  };
  list.addEventListener("scroll", updateEdges, { passive: true });

  const active = list.querySelector(".md-tabs__item--active");
  if (active) {
    list.style.scrollBehavior = "auto";
    list.scrollLeft = active.offsetLeft - (list.clientWidth - active.offsetWidth) / 2;
    list.style.scrollBehavior = "";
  }
  updateEdges();

  let seen = false;
  try { seen = localStorage.getItem("tabs-peek") === "1"; } catch (e) {}
  if (seen || list.scrollLeft > 4 || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  setTimeout(() => {
    list.scrollLeft = 60;
    setTimeout(() => { list.scrollLeft = 0; }, 700);
  }, 600);
  try { localStorage.setItem("tabs-peek", "1"); } catch (e) {}
});

// 「物理数学」のタブ：ページへ移らず，タブのバーの下に分野の一覧を開く
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".md-tabs__menu-toggle");
  const tabs = document.querySelector(".md-tabs");
  if (!toggle || !tabs) return;
  const menu = document.getElementById(toggle.getAttribute("aria-controls"));
  if (!menu) return;
  // タブのリストは横スクロールで切れるので，一覧はバーの直後へ移す
  tabs.after(menu);

  const setOpen = (open) => {
    toggle.setAttribute("aria-expanded", String(open));
    toggle.closest(".md-tabs__item").classList.toggle("md-tabs__item--open", open);
    if (open) {
      menu.hidden = false;
      requestAnimationFrame(() => menu.classList.add("is-open"));
    } else {
      menu.classList.remove("is-open");
      const done = () => { if (!menu.classList.contains("is-open")) menu.hidden = true; };
      if (matchMedia("(prefers-reduced-motion: reduce)").matches) done();
      else menu.addEventListener("transitionend", done, { once: true });
      setTimeout(done, 300);
    }
  };
  toggle.addEventListener("click", (e) => {
    e.stopPropagation();
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });
  document.addEventListener("click", (e) => {
    if (toggle.getAttribute("aria-expanded") === "true" && !menu.contains(e.target)) setOpen(false);
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") { setOpen(false); toggle.focus(); }
  });
});
