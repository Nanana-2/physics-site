---
title: 問題を印刷する
hide:
  - navigation
  - toc
---

# 問題を印刷する

好きな問題を選ぶと，問題用紙と解答・解説の別冊を印刷できます。

<div class="exam-builder" data-exam-builder data-index-url="../problem-index.json" markdown="0">
  <section class="toc-chapter">
    <h2 class="toc-chapter__head"><span class="toc-chapter__no">1</span><span class="toc-chapter__title">問題を選ぶ</span></h2>
    <div class="finder__subjects" data-exam-subjects role="group" aria-label="分野"></div>
    <dl class="exam-builder__filters">
      <dt>章</dt>
      <dd class="exam-builder__chapters" data-exam-chapters role="group" aria-label="章"></dd>
      <dt>難易度</dt>
      <dd class="finder__levels" data-exam-levels role="group" aria-label="難易度">
        <button type="button" class="finder__level exam-builder__check is-on" data-level="基本" aria-label="基本" aria-pressed="true">★</button>
        <button type="button" class="finder__level exam-builder__check is-on" data-level="標準" aria-label="標準" aria-pressed="true">★★</button>
        <button type="button" class="finder__level exam-builder__check is-on" data-level="発展" aria-label="発展" aria-pressed="true">★★★</button>
      </dd>
    </dl>
    <div class="exam-builder__bar">
      <span class="exam-builder__random">
        <span>選んだ章と難易度からランダムに</span>
        <select data-exam-random-count aria-label="問題数"></select>
        <button type="button" class="exam-builder__chip" data-exam-random>問加える</button>
      </span>
    </div>
    <div class="exam-builder__list" data-exam-list></div>
  </section>

  <section class="toc-chapter">
    <h2 class="toc-chapter__head"><span class="toc-chapter__no">2</span><span class="toc-chapter__title">選んだ問題<span class="exam-builder__count" data-exam-count></span></span></h2>
    <div data-exam-chosen></div>
    <div class="exam-builder__clear"><button type="button" class="exam-builder__chip" data-exam-clear hidden>すべて外す</button></div>
    <p class="exam-builder__empty" data-exam-empty>まだ問題が選ばれていません。上の一覧の「追加」か，各問題のページの「印刷に追加」から選んでください。</p>
  </section>

  <section class="toc-chapter">
    <h2 class="toc-chapter__head"><span class="toc-chapter__no">3</span><span class="toc-chapter__title">印刷の設定</span></h2>
    <label class="finder__search exam-builder__title">
      <span class="exam-builder__title-label">題名</span>
      <input type="text" data-exam-title maxlength="40" placeholder="物理学 問題" aria-label="題名">
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
    <button type="button" class="exam-builder__chip" data-exam-share>このセットのリンクをコピー</button>
    <span class="exam-builder__status" data-exam-status role="status" aria-live="polite"></span>
  </div>
  <p class="exam-builder__note">冊子形式は，ページ数を4の倍数にそろえて印刷します。冊子の形に並べるには，プリンターや PDF ビューアーの小冊子印刷の設定を使ってください。</p>
  <noscript>このページを使うには，ブラウザのJavaScriptを有効にしてください。</noscript>
</div>
