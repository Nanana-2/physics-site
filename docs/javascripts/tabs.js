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

// 「物理数学」のタブ：ページへ移らず，タブの下に分野の一覧を縦に開く。
// マウスのある端末では触れた時点で開き，離れると閉じる。スマホなどはタップで開閉する。
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".md-tabs__menu-toggle");
  const tabs = document.querySelector(".md-tabs");
  if (!toggle || !tabs) return;
  const item = toggle.closest(".md-tabs__item");
  const menu = document.getElementById(toggle.getAttribute("aria-controls"));
  if (!menu) return;
  // タブのリストは横スクロールで切れるので，一覧はバーの直後へ移し，位置はタブに合わせる
  tabs.after(menu);
  const header = tabs.closest(".md-header") || tabs.parentElement;
  const place = () => {
    const r = item.getBoundingClientRect(), h = header.getBoundingClientRect();
    const left = Math.max(8, Math.min(r.left - h.left, h.width - menu.offsetWidth - 8));
    menu.style.left = left + "px";
    menu.style.minWidth = r.width + "px";
  };
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const isOpen = () => toggle.getAttribute("aria-expanded") === "true";
  const setOpen = (open) => {
    if (open === isOpen()) return;
    toggle.setAttribute("aria-expanded", String(open));
    item.classList.toggle("md-tabs__item--open", open);
    if (open) {
      menu.hidden = false;
      place();
      requestAnimationFrame(() => menu.classList.add("is-open"));
    } else {
      menu.classList.remove("is-open");
      const done = () => { if (!isOpen()) menu.hidden = true; };
      if (reduce) done(); else setTimeout(done, 220);
    }
  };
  toggle.addEventListener("click", (e) => { e.stopPropagation(); setOpen(!isOpen()); });
  document.addEventListener("click", (e) => { if (isOpen() && !menu.contains(e.target)) setOpen(false); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && isOpen()) { setOpen(false); toggle.focus(); } });
  addEventListener("resize", () => { if (isOpen()) place(); });
  tabs.querySelector(".md-tabs__list")?.addEventListener("scroll", () => { if (isOpen()) place(); }, { passive: true });

  const hover = matchMedia("(hover: hover) and (pointer: fine)");
  let timer;
  const enter = () => { if (!hover.matches) return; clearTimeout(timer); setOpen(true); };
  const leave = () => { if (!hover.matches) return; clearTimeout(timer); timer = setTimeout(() => setOpen(false), 180); };
  for (const el of [item, menu]) { el.addEventListener("mouseenter", enter); el.addEventListener("mouseleave", leave); }
  menu.addEventListener("focusout", (e) => { if (!menu.contains(e.relatedTarget) && e.relatedTarget !== toggle) setOpen(false); });
});
