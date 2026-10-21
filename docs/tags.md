---
title: 問題を探す
hide:
  - navigation
  - toc
---

# 問題を探す

<div class="finder" data-index-url="../problem-index.json">
  <label class="finder__search">
    <span class="finder__glass" aria-hidden="true"></span>
    <input type="search" data-finder-keyword placeholder="問題名・問題文から検索（例：角運動量，分配関数）" autocomplete="off" aria-label="キーワード">
  </label>

  <div class="finder__subjects" data-finder-subjects role="group" aria-label="分野">
    <button type="button" class="finder__subject is-on" data-subject="">すべて</button>
    <button type="button" class="finder__subject finder__subject--01mechanics" data-subject="01mechanics">力学</button>
    <button type="button" class="finder__subject finder__subject--02electromagnetism" data-subject="02electromagnetism">電磁気学</button>
    <button type="button" class="finder__subject finder__subject--03thermodynamics" data-subject="03thermodynamics">熱力学</button>
    <button type="button" class="finder__subject finder__subject--04quantum_mechanics" data-subject="04quantum_mechanics">量子力学</button>
    <button type="button" class="finder__subject finder__subject--05statistical_mechanics" data-subject="05statistical_mechanics">統計力学</button>
    <button type="button" class="finder__subject finder__subject--06solid_state" data-subject="06solid_state">物性物理学</button>
    <button type="button" class="finder__subject finder__subject--14calculus" data-subject="14calculus">微積分</button>
    <button type="button" class="finder__subject finder__subject--07linear_algebra" data-subject="07linear_algebra">線形代数</button>
    <button type="button" class="finder__subject finder__subject--08differential_equations" data-subject="08differential_equations">微分方程式</button>
    <button type="button" class="finder__subject finder__subject--09vector_analysis" data-subject="09vector_analysis">ベクトル解析</button>
    <button type="button" class="finder__subject finder__subject--10integral_transforms" data-subject="10integral_transforms">積分変換</button>
    <button type="button" class="finder__subject finder__subject--11complex_analysis" data-subject="11complex_analysis">複素関数</button>
    <button type="button" class="finder__subject finder__subject--12special_functions" data-subject="12special_functions">特殊関数・変分法</button>
    <button type="button" class="finder__subject finder__subject--13probability_statistics" data-subject="13probability_statistics">確率・統計</button>
  </div>

  <div class="finder__bar">
    <span class="finder__levels" data-finder-levels role="group" aria-label="難易度">
      <span class="finder__label">難易度</span>
      <button type="button" class="finder__level" data-level="基本" aria-label="基本">★</button>
      <button type="button" class="finder__level" data-level="標準" aria-label="標準">★★</button>
      <button type="button" class="finder__level" data-level="発展" aria-label="発展">★★★</button>
    </span>
    <span class="finder__count" data-finder-count aria-live="polite">読み込み中…</span>
  </div>

  <div data-finder-results></div>
  <noscript>この検索を使うには，ブラウザのJavaScriptを有効にしてください。</noscript>
</div>
