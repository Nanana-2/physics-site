---
title: 試験を作る
hide:
  - navigation
  - toc
---

# 試験を作る

好きな問題を5問まで選ぶと，定期試験の形の問題用紙と解答・解説の別冊を印刷できます。問題は，各問題のページの「試験に追加」からも選ぶことができます。

<div class="exam-builder" data-exam-builder data-index-url="../problem-index.json" markdown="0">
  <section class="exam-builder__section">
    <h2>選んだ問題 <span class="exam-builder__count" data-exam-count></span></h2>
    <ol class="exam-builder__chosen" data-exam-chosen></ol>
    <p class="exam-builder__empty" data-exam-empty>まだ問題が選ばれていません。</p>
  </section>

  <section class="exam-builder__section">
    <h2>問題を加える</h2>
    <div class="exam-builder__row">
      <label>分野 <select data-exam-subject></select></label>
      <label>章 <select data-exam-chapter></select></label>
    </div>
    <div class="exam-builder__row">
      <label>ランダムに <select data-exam-random-count></select> 問</label>
      <button type="button" class="exam-builder__button" data-exam-random>この範囲から選ぶ</button>
    </div>
    <ul class="exam-builder__list" data-exam-list></ul>
  </section>

  <section class="exam-builder__section">
    <h2>試験の設定</h2>
    <div class="exam-builder__row">
      <label class="exam-builder__title">題名 <input type="text" data-exam-title maxlength="40" placeholder="物理学 試験問題"></label>
    </div>
    <div class="exam-builder__row" role="radiogroup" aria-label="大問番号">
      <span class="exam-builder__label">大問番号</span>
      <label><input type="radio" name="exam-num" value="mon"> 問題 1</label>
      <label><input type="radio" name="exam-num" value="dai"> 第 1 問</label>
      <label><input type="radio" name="exam-num" value="box"> <span class="exam-builder__box">1</span></label>
    </div>
    <div class="exam-builder__row" role="radiogroup" aria-label="用紙">
      <span class="exam-builder__label">用紙</span>
      <label><input type="radio" name="exam-paper" value="A4"> A4</label>
      <label><input type="radio" name="exam-paper" value="B5"> B5</label>
    </div>
    <div class="exam-builder__row" role="radiogroup" aria-label="形式">
      <span class="exam-builder__label">形式</span>
      <label><input type="radio" name="exam-book" value="0"> プリント</label>
      <label><input type="radio" name="exam-book" value="1"> 冊子（表紙つき）</label>
    </div>
    <div class="exam-builder__row">
      <label><input type="checkbox" data-exam-break> 1問ごとに改ページする</label>
    </div>
  </section>

  <div class="exam-builder__actions">
    <a class="exam-builder__open" data-exam-open href="print/">印刷用のページを開く</a>
    <button type="button" class="exam-builder__button" data-exam-share>この試験のリンクをコピー</button>
    <span class="exam-builder__status" data-exam-status role="status" aria-live="polite"></span>
  </div>
  <p class="exam-builder__note">冊子形式は，ページ数を4の倍数にそろえて印刷します。冊子の形に並べるには，プリンターや PDF ビューアーの小冊子印刷の設定を使ってください。</p>
  <noscript>このページを使うには，ブラウザのJavaScriptを有効にしてください。</noscript>
</div>
