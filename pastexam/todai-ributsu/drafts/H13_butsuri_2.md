---
title: 東大理物 平成13年度 物理学 第2問：1次元イジング模型の分配関数と自由エネルギー
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成13年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成13年度 物理学 第2問：1次元イジング模型の分配関数と自由エネルギー

## 問題

スピンが一次元格子上の各点にあり，格子点の数が $N$（$N$ は偶数）の模型を考察する。そのハミルトニアンは

$$
H = -J \sum_{i=1}^{N} \sigma_i \sigma_{i+1},
$$

とする。ここで周期的境界条件を課し，$\sigma_{N+1}$ は $\sigma_1$ を意味するものとし，かつ $\sigma_i$（$i = 1, 2, \dots, N$）は $\pm 1$ の値をとるものとする。この模型の各状態は $(\uparrow\downarrow\downarrow\uparrow\dots)$ のようなスピンの配置によってあらわされる。

(1) この模型の状態数は全部でいくつか。

(2) $J$ が正の場合と負の場合について基底状態のスピン配置を書け。

(3) 前問の場合，基底状態エネルギーとその縮重度を求めよ。

以下では $J$ が正の場合のみを考える。

(4) 第一励起状態のスピン配置を書け。そのエネルギーと縮重度をもとめよ。

(5) すべてのエネルギー固有値とその縮重度を求めよ。ただし二項係数

$$
{}_N C_M \equiv \frac{N!}{M!(N - M)!},
$$

を用いよ。

(6) 前問の結果を用いて，この系の分配関数を求めよ。ただし温度は $T$ とし，ボルツマン定数は $k_{\mathrm{B}}$ とする。必要に応じて

$$
(1 + x)^N = \sum_{M=0}^{N} {}_N C_M x^M,
$$

を使ってよい。

(7) $N$ が無限大の極限での1格子点当たりの自由エネルギーが

$$
-k_{\mathrm{B}}T \ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right]
$$

であらわされることを示せ。

(8) 前問の結果を用いて，1格子点当たりのエネルギーとエントロピーを求めよ。高温でのエントロピーの漸近的振る舞いを求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成13年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
スピン変数 $\sigma_i = \pm 1$ そのものではなく，隣り合うスピンの積 $\tau_i = \sigma_i\sigma_{i+1} \in \{+1, -1\}$ に注目すると，ハミルトニアンは反平行ボンドの個数 $M$ だけで表すことができます。

周期的境界条件 $\sigma_{N+1} = \sigma_1$ のもとでは全ボンドの積が $+1$ になるため，$M$ は偶数に限られます。この制約と二項定理を組み合わせることで，すべてのエネルギー準位の縮重度と有限 $N$ での分配関数を厳密に計算し，熱力学極限 $N \to \infty$ での自由エネルギーと熱力学量を導きます。
</div>

### (1)

各格子点 $i = 1, 2, \dots, N$ のスピン $\sigma_i$ は $+1$ と $-1$ の2通りの値を独立にとります。格子点の総数は $N$ なので，全状態数は次の通りです。

$$
\finalanswer{2^N}
$$

### (2)

各ボンドの積 $\sigma_i \sigma_{i+1}$ は $+1$ または $-1$ の値をとります。

$J > 0$ のときは，すべてのボンドで $\sigma_i \sigma_{i+1} = +1$ となるときエネルギーが最小になります。したがって，基底状態のスピン配置はすべてのスピンが同じ向きにそろった次の2通りです。

$$
\finalanswer{J > 0:\quad (\uparrow\uparrow\uparrow\cdots\uparrow), \quad (\downarrow\downarrow\downarrow\cdots\downarrow)}
$$

$J < 0$ のときは，すべてのボンドで $\sigma_i \sigma_{i+1} = -1$ となるときエネルギーが最小になります。格子点数 $N$ は偶数なので，$\sigma_{N+1} = \sigma_1$ を満たしながら隣り合うスピンをすべて反平行に並べることができます。したがって，基底状態のスピン配置は交互に並んだ次の2通りです。

$$
\finalanswer{J < 0:\quad (\uparrow\downarrow\uparrow\downarrow\cdots\uparrow\downarrow), \quad (\downarrow\uparrow\downarrow\uparrow\cdots\downarrow\uparrow)}
$$

### (3)

$J > 0$ のとき，全 $N$ 個のボンドで $\sigma_i\sigma_{i+1} = +1$ となるため，基底状態エネルギーは $E_0 = -NJ$ です。(2) より配置は2通りなので縮重度は $g_0 = 2$ です。

$J < 0$ のとき，全 $N$ 個のボンドで $\sigma_i\sigma_{i+1} = -1$ となるため，基底状態エネルギーは $E_0 = NJ$，すなわち $-N|J|$ です。(2) より配置は2通りなので縮重度は $g_0 = 2$ です。

$$
\finalanswer{E_0 = -N|J| = \begin{cases} -NJ & (J > 0) \\ NJ & (J < 0) \end{cases}, \qquad g_0 = 2}
$$

### (4)

ボンド変数 $\tau_i = \sigma_i\sigma_{i+1} \in \{+1, -1\}$ を導入します。周期的境界条件 $\sigma_{N+1} = \sigma_1$ より，全ボンドの積は次の恒等式を満たします。

$$
\begin{aligned}
\prod_{i=1}^{N} \tau_i &= \prod_{i=1}^{N} \sigma_i \sigma_{i+1} \\
&= \prod_{i=1}^{N} \sigma_i^2 \\
&= 1
\end{aligned}
$$

したがって，$\tau_i = -1$ となる反平行ボンドの個数 $M$ は必ず偶数になります。

$J > 0$ のとき，基底状態は $M = 0$ であり，エネルギーが次に低い第1励起状態は $M = 2$ の状態です。これは円環上に2か所の磁壁があり，ある連続した区間のスピンだけが反転した配置，すなわち $(\uparrow\cdots\uparrow\downarrow\cdots\downarrow\uparrow\cdots\uparrow)$ および全体の向きを反転した $(\downarrow\cdots\downarrow\uparrow\cdots\uparrow\downarrow\cdots\downarrow)$ の形の配置です。

このとき平行ボンドが $N - 2$ 個，反平行ボンドが $2$ 個なので，エネルギー $E_1$ は次のようになります。

$$
\begin{aligned}
E_1 &= -J(N - 2) + 2J \\
&= -(N - 4)J
\end{aligned}
$$

縮重度 $g_1$ を求めます。$N$ 個のボンドから反平行にする2か所を選ぶ方法は ${}_N C_2 = \dfrac{N(N - 1)}{2}$ 通りです。反平行ボンドの位置を決めると，$\sigma_1$ の向きを $\uparrow$ か $\downarrow$ の2通りから選んだ時点で残りのスピン $\sigma_2, \dots, \sigma_N$ がすべて一意に定まります。よって縮重度は $g_1 = 2\,{}_N C_2 = N(N - 1)$ です。

したがって，第1励起状態は連続する一部の区間のみスピンが反転した配置であり，エネルギーと縮重度は次の通りです。

$$
\finalanswer{E_1 = -(N - 4)J, \qquad g_1 = N(N - 1)}
$$

### (5)

反平行ボンドの個数 $M$ は，(4) で示した通り偶数であり，$N$ が偶数なので $M = 0, 2, 4, \dots, N$ の値をとります。反平行ボンドが $M$ 個，平行ボンドが $N - M$ 個あるときのエネルギー固有値 $E_M$ は次の通りです。

$$
\begin{aligned}
E_M &= -J(N - M) + JM \\
&= -(N - 2M)J
\end{aligned}
$$

縮重度 $g_M$ を求めます。$N$ 個のボンドから $\tau_i = -1$ とする $M$ 個を選ぶ方法は ${}_N C_M$ 通りです。選んだ $M$ 個が偶数個なので $\prod_{i=1}^{N}\tau_i = 1$ が成り立ち，$\sigma_1 \in \{+1, -1\}$ の2通りを決めると $\sigma_2 = \tau_1\sigma_1$，$\sigma_3 = \tau_2\sigma_2$，$\dots$ と順に定まり，$\sigma_{N+1} = \sigma_1$ も自動的に満たされます。したがって，各偶数 $M$ に対する縮重度は $g_M = 2\,{}_N C_M$ です。

$$
\finalanswer{E_M = -(N - 2M)J, \qquad g_M = 2\,{}_N C_M \qquad (M = 0, 2, 4, \dots, N)}
$$

### (6)

$K = \dfrac{J}{k_{\mathrm{B}}T}$ とおき，偶数 $M$ を $M = 2k$（$k = 0, 1, \dots, N/2$）と書きます。(5) のエネルギー固有値と縮重度を用いて，分配関数 $Z$ を計算します。

$$
\begin{aligned}
Z &= \sum_{k=0}^{N/2} 2\,{}_N C_{2k} \exp\bigl((N - 4k)K\bigr) \\
&= 2e^{NK} \sum_{k=0}^{N/2} {}_N C_{2k} \left(e^{-2K}\right)^{2k}
\end{aligned}
$$

二項展開 $(1 + x)^N = \sum_{M=0}^{N} {}_N C_M x^M$ と $(1 - x)^N = \sum_{M=0}^{N} (-1)^M {}_N C_M x^M$ を足して $2$ で割ると，偶数次の項だけを取り出す恒等式が得られます。

$$
\sum_{k=0}^{N/2} {}_N C_{2k} x^{2k} = \frac{(1 + x)^N + (1 - x)^N}{2}
$$

これに $x = e^{-2K}$ を代入して $Z$ を計算します。

$$
\begin{aligned}
Z &= e^{NK}\left[\left(1 + e^{-2K}\right)^N + \left(1 - e^{-2K}\right)^N\right] \\
&= \left(e^K + e^{-K}\right)^N + \left(e^K - e^{-K}\right)^N \\
&= (2\cosh K)^N + (2\sinh K)^N
\end{aligned}
$$

したがって，分配関数は次の通りです。

$$
\finalanswer{Z = \left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right]^N + \left[2\sinh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right]^N}
$$

### (7)

1格子点当たりの自由エネルギー $f_N = -\dfrac{k_{\mathrm{B}}T}{N}\ln Z$ を計算します。(6) の結果から $(2\cosh K)^N$ をくくり出します。

$$
\begin{aligned}
f_N &= -\frac{k_{\mathrm{B}}T}{N}\ln\left\{(2\cosh K)^N\left[1 + (\tanh K)^N\right]\right\} \\
&= -k_{\mathrm{B}}T\ln(2\cosh K) - \frac{k_{\mathrm{B}}T}{N}\ln\left[1 + (\tanh K)^N\right]
\end{aligned}
$$

$J > 0$ および $T > 0$ より $K = \dfrac{J}{k_{\mathrm{B}}T} > 0$ であり，$0 < \tanh K < 1$ が成り立ちます。したがって $N \to \infty$ の極限で $(\tanh K)^N \to 0$ となり，第2項は $0$ に収束します。よって，1格子点当たりの自由エネルギー $f = \lim_{N \to \infty} f_N$ は次の式で与えられます。

$$
f = -k_{\mathrm{B}}T \ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right]
$$

### (8)

1格子点当たりのエントロピー $s$ は $s = -\dfrac{\partial f}{\partial T}$ から求めます。

$$
\begin{aligned}
s &= -\frac{\partial}{\partial T}\left\{-k_{\mathrm{B}}T\ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right]\right\} \\
&= k_{\mathrm{B}}\ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right] + k_{\mathrm{B}}T \cdot \frac{\sinh\left(\dfrac{J}{k_{\mathrm{B}}T}\right)}{\cosh\left(\dfrac{J}{k_{\mathrm{B}}T}\right)} \cdot \left(-\frac{J}{k_{\mathrm{B}}T^2}\right) \\
&= k_{\mathrm{B}}\ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right] - \frac{J}{T}\tanh\left(\frac{J}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

1格子点当たりのエネルギー $u$ は熱力学関係 $u = f + Ts$ から求めます。

$$
\begin{aligned}
u &= -k_{\mathrm{B}}T\ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right] + T\left\{k_{\mathrm{B}}\ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right] - \frac{J}{T}\tanh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right\} \\
&= -J\tanh\left(\frac{J}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

次に，高温極限 $k_{\mathrm{B}}T \gg J$，すなわち $K = \dfrac{J}{k_{\mathrm{B}}T} \ll 1$ でのエントロピーの漸近的振る舞いを求めます。$\cosh K = 1 + \dfrac{1}{2}K^2 + O(K^4)$ および $\tanh K = K + O(K^3)$ を用いて展開します。

$$
\begin{aligned}
\ln(2\cosh K) &= \ln 2 + \ln\left(1 + \frac{1}{2}K^2 + O(K^4)\right) \\
&= \ln 2 + \frac{1}{2}K^2 + O(K^4)
\end{aligned}
$$

また $K\tanh K = K^2 + O(K^4)$ です。これらを $s = k_{\mathrm{B}}\bigl[\ln(2\cosh K) - K\tanh K\bigr]$ に代入します。

$$
\begin{aligned}
s &= k_{\mathrm{B}}\left[\ln 2 + \frac{1}{2}K^2 - K^2 + O(K^4)\right] \\
&= k_{\mathrm{B}}\left[\ln 2 - \frac{1}{2}\left(\frac{J}{k_{\mathrm{B}}T}\right)^2 + O\left(\left(\frac{J}{k_{\mathrm{B}}T}\right)^4\right)\right]
\end{aligned}
$$

したがって，1格子点当たりのエネルギー，エントロピー，および高温でのエントロピーの漸近的振る舞いは次の通りです。

$$
\finalanswer{u = -J\tanh\left(\frac{J}{k_{\mathrm{B}}T}\right), \qquad s = k_{\mathrm{B}}\ln\left[2\cosh\left(\frac{J}{k_{\mathrm{B}}T}\right)\right] - \frac{J}{T}\tanh\left(\frac{J}{k_{\mathrm{B}}T}\right)}
$$

$$
\finalanswer{s \approx k_{\mathrm{B}}\ln 2 - \frac{J^2}{2k_{\mathrm{B}}T^2} \qquad (k_{\mathrm{B}}T \gg J)}
$$

<aside class="rigor-note" markdown>
(5) の縮重度の総和は $\sum_{k=0}^{N/2} 2\,{}_N C_{2k} = 2 \cdot 2^{N-1} = 2^N$ となり，(1) の全状態数と一致します。また (8) のエントロピーは，$T \to \infty$ で各スピンが完全に無秩序になった値 $k_{\mathrm{B}}\ln 2$ に $T^{-2}$ の速さで近づき，$T \to 0^+$ では $\ln(2\cosh K) - K\tanh K \approx 2K e^{-2K} \to 0$ となって $0$ に収束します。
</aside>
