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
