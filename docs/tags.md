# 全問題一覧

収録されている問題を、分野・章・難易度・キーワードから絞り込めます。
キーワードは問題名だけでなく、問題文の内容も検索します。

<div class="problem-finder" data-index-url="../problem-index.json">
  <div class="problem-finder__controls">
    <label class="problem-finder__keyword">
      <span>キーワード</span>
      <input type="search" data-problem-keyword placeholder="例：角運動量、分配関数" autocomplete="off">
    </label>

    <label>
      <span>分野</span>
      <select data-problem-subject>
        <option value="">すべての分野</option>
      </select>
    </label>

    <label>
      <span>章</span>
      <select data-problem-chapter>
        <option value="">すべての章</option>
      </select>
    </label>

    <label>
      <span>難易度</span>
      <select data-problem-difficulty>
        <option value="">すべての難易度</option>
        <option value="基本">基本</option>
        <option value="標準">標準</option>
        <option value="発展">発展</option>
      </select>
    </label>

    <button type="button" class="problem-finder__reset" data-problem-reset>条件をリセット</button>
  </div>

  <p class="problem-finder__status" data-problem-status aria-live="polite">問題一覧を読み込んでいます。</p>
  <div class="problem-finder__results" data-problem-results></div>
  <button type="button" class="problem-finder__more" data-problem-more hidden>続きを表示</button>

  <noscript>この絞り込み機能を使うには、ブラウザのJavaScriptを有効にしてください。</noscript>
</div>
