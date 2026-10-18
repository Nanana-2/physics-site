window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
    macros: {
      finalanswer: ['\\class{fa}{\\boldsymbol{#1}}', 1]
    }
  },
  startup: {
    // 答えだけの数式は式全体に，導出の最後が答えの式は答えの部分だけに黄色を敷く
    pageReady: () => MathJax.startup.defaultPageReady().then(() => {
      document.querySelectorAll('mjx-container[display="true"]').forEach((box) => {
        const answers = box.querySelectorAll('.fa');
        if (!answers.length) return;
        const inAnswers = [...answers].reduce((n, a) => n + a.querySelectorAll('mjx-c').length, 0);
        if (inAnswers === box.querySelectorAll('mjx-c').length) box.classList.add('fa-whole');
      });
    })
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
