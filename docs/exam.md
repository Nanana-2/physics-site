---
title: 試験を作る
hide:
  - navigation
  - toc
---

# 試験を作る

好きな問題を8問まで選ぶと，定期試験の形の問題用紙と解答・解説の別冊を印刷できます。問題は，各問題のページの「試験に追加」からも選ぶことができます。

<div class="exam-builder" data-exam-builder data-index-url="../problem-index.json" markdown="0">
  <section class="toc-chapter">
    <h2 class="toc-chapter__head"><span class="toc-chapter__no">1</span><span class="toc-chapter__title">問題を選ぶ</span></h2>
    <div class="finder__subjects" data-exam-subjects role="group" aria-label="分野"></div>
    <div class="exam-builder__bar">
      <label class="exam-builder__select">章 <select data-exam-chapter></select></label>
      <span class="exam-builder__random">
        <span>この範囲からランダムに</span>
        <select data-exam-random-count aria-label="問題数"></select>
        <button type="button" class="exam-builder__chip" data-exam-random>問加える</button>
      </span>
    </div>
    <div class="exam-builder__list" data-exam-list></div>
  </section>

  <section class="toc-chapter">
    <h2 class="toc-chapter__head"><span class="toc-chapter__no">2</span><span class="toc-chapter__title">選んだ問題<span class="exam-builder__count" data-exam-count></span></span></h2>
    <div data-exam-chosen></div>
    <p class="exam-builder__empty" data-exam-empty>まだ問題が選ばれていません。上の一覧の「追加」か，各問題のページの「試験に追加」から選んでください。</p>
  </section>

  <section class="toc-chapter">
    <h2 class="toc-chapter__head"><span class="toc-chapter__no">3</span><span class="toc-chapter__title">試験の設定</span></h2>
    <label class="finder__search exam-builder__title">
      <span class="exam-builder__title-label">題名</span>
      <input type="text" data-exam-title maxlength="40" placeholder="物理学 試験問題" aria-label="題名">
    </label>
    <dl class="exam-builder__settings">
      <dt>大問番号</dt>
      <dd data-exam-option="num"><button type="button" data-value="mon">問題 1</button><button type="button" data-value="dai">第 1 問</button><button type="button" data-value="box" aria-label="四角数字"><span class="exam-builder__box">1</span></button></dd>
      <dt>用紙</dt>
      <dd data-exam-option="paper"><button type="button" data-value="A4">A4</button><button type="button" data-value="B5">B5</button></dd>
      <dt>形式</dt>
      <dd data-exam-option="book"><button type="button" data-value="0">プリント</button><button type="button" data-value="1">冊子（表紙つき）</button></dd>
      <dt>改ページ</dt>
      <dd data-exam-option="break"><button type="button" data-value="0">続けて組む</button><button type="button" data-value="1">1問ごと</button></dd>
    </dl>
  </section>

  <div class="exam-builder__actions">
    <a class="exam-builder__open" data-exam-open href="print/">印刷用のページを開く</a>
    <button type="button" class="exam-builder__chip" data-exam-share>この試験のリンクをコピー</button>
    <span class="exam-builder__status" data-exam-status role="status" aria-live="polite"></span>
  </div>
  <p class="exam-builder__note">冊子形式は，ページ数を4の倍数にそろえて印刷します。冊子の形に並べるには，プリンターや PDF ビューアーの小冊子印刷の設定を使ってください。</p>
  <noscript>このページを使うには，ブラウザのJavaScriptを有効にしてください。</noscript>
</div>
