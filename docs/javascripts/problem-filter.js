(() => {
  const PAGE_SIZE = 40;

  const normalize = (value) =>
    String(value || "")
      .normalize("NFKC")
      .toLocaleLowerCase("ja")
      .replace(/\s+/g, " ")
      .trim();

  const escapeHtml = (value) =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  const setupProblemFinder = async (finder) => {
    if (finder.dataset.ready === "true") return;
    finder.dataset.ready = "true";

    const keyword = finder.querySelector("[data-problem-keyword]");
    const subject = finder.querySelector("[data-problem-subject]");
    const chapter = finder.querySelector("[data-problem-chapter]");
    const difficulty = finder.querySelector("[data-problem-difficulty]");
    const reset = finder.querySelector("[data-problem-reset]");
    const status = finder.querySelector("[data-problem-status]");
    const results = finder.querySelector("[data-problem-results]");
    const more = finder.querySelector("[data-problem-more]");

    let problems = [];
    let filtered = [];
    let visibleCount = PAGE_SIZE;

    const option = (value, label) => {
      const element = document.createElement("option");
      element.value = value;
      element.textContent = label;
      return element;
    };

    const populateSubjects = () => {
      const subjects = new Map();
      problems.forEach((problem) => {
        if (!subjects.has(problem.subjectSlug)) {
          subjects.set(problem.subjectSlug, problem.subject);
        }
      });
      subjects.forEach((label, value) => subject.append(option(value, label)));
    };

    const populateChapters = () => {
      const selected = subject.value;
      const current = chapter.value;
      const chapters = new Map();

      problems
        .filter((problem) => !selected || problem.subjectSlug === selected)
        .forEach((problem) => {
          const value = `${problem.subjectSlug}/${problem.chapterSlug}`;
          const label = selected
            ? problem.chapter
            : `${problem.subject}｜${problem.chapter}`;
          if (!chapters.has(value)) chapters.set(value, label);
        });

      chapter.replaceChildren(option("", "すべての章"));
      chapters.forEach((label, value) => chapter.append(option(value, label)));
      chapter.value = chapters.has(current) ? current : "";
    };

    const render = () => {
      const shown = filtered.slice(0, visibleCount);
      status.textContent = `${filtered.length}問が見つかりました`;

      if (!shown.length) {
        results.innerHTML = '<p class="problem-finder__empty">条件に合う問題がありません。検索語や絞り込み条件を変えてみてください。</p>';
        more.hidden = true;
        return;
      }

      results.innerHTML = shown
        .map((problem) => {
          const href = new URL(`../${problem.url}`, window.location.href).href;
          return `
            <article class="problem-result">
              <div class="problem-result__body">
                <a class="problem-result__title" href="${escapeHtml(href)}">${escapeHtml(problem.title)}</a>
                <p class="problem-result__meta">
                  <span>${escapeHtml(problem.subject)}</span>
                  <span aria-hidden="true">›</span>
                  <span>${escapeHtml(problem.chapter)}</span>
                  <span class="problem-result__number">${escapeHtml(problem.number || "")}</span>
                </p>
              </div>
              <span class="problem-result__difficulty" data-difficulty="${escapeHtml(problem.difficulty)}">${escapeHtml(problem.difficulty)}</span>
            </article>`;
        })
        .join("");

      more.hidden = visibleCount >= filtered.length;
      more.textContent = `続きを表示（残り${filtered.length - visibleCount}問）`;
    };

    const filter = () => {
      const query = normalize(keyword.value);
      const words = query.split(" ").filter(Boolean);
      const selectedChapter = chapter.value;

      filtered = problems.filter((problem) => {
        if (subject.value && problem.subjectSlug !== subject.value) return false;
        if (
          selectedChapter &&
          `${problem.subjectSlug}/${problem.chapterSlug}` !== selectedChapter
        ) return false;
        if (difficulty.value && problem.difficulty !== difficulty.value) return false;

        const haystack = normalize(
          `${problem.title} ${problem.subject} ${problem.chapter} ${problem.searchText}`
        );
        return words.every((word) => haystack.includes(word));
      });

      visibleCount = PAGE_SIZE;
      render();
    };

    try {
      const indexUrl = new URL(finder.dataset.indexUrl, window.location.href);
      const response = await fetch(indexUrl);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      problems = data.problems || [];

      populateSubjects();
      const params = new URLSearchParams(window.location.search);
      const requestedSubject = params.get("subject") || "";
      const requestedDifficulty = params.get("difficulty") || "";
      if ([...subject.options].some((item) => item.value === requestedSubject)) {
        subject.value = requestedSubject;
      }
      if ([...difficulty.options].some((item) => item.value === requestedDifficulty)) {
        difficulty.value = requestedDifficulty;
      }
      keyword.value = params.get("keyword") || "";
      populateChapters();
      filter();

      keyword.addEventListener("input", filter);
      subject.addEventListener("change", () => {
        populateChapters();
        filter();
      });
      chapter.addEventListener("change", filter);
      difficulty.addEventListener("change", filter);
      reset.addEventListener("click", () => {
        keyword.value = "";
        subject.value = "";
        difficulty.value = "";
        populateChapters();
        filter();
        keyword.focus();
      });
      more.addEventListener("click", () => {
        visibleCount += PAGE_SIZE;
        render();
      });
    } catch (error) {
      console.error("Problem index could not be loaded:", error);
      status.textContent = "問題一覧を読み込めませんでした。ページを再読み込みしてください。";
    }
  };

  const redirectDifficultyTags = () => {
    document.querySelectorAll('a.md-tag[href*="tag-index/"]').forEach((link) => {
      const difficulty = link.textContent.trim();
      if (!["基本", "標準", "発展"].includes(difficulty)) return;

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
    document.querySelectorAll(".problem-finder").forEach(setupProblemFinder);
  };

  if (typeof document$ !== "undefined") {
    document$.subscribe(initialize);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }
})();
