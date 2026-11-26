---
title: 東大理物 平成14年度 物理学 第2問：荷電鎖状分子のエントロピー弾性と一様電場下の伸び
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成14年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成14年度 物理学 第2問：荷電鎖状分子のエントロピー弾性と一様電場下の伸び

## 問題

図のように，矢印で表される要素 $N$ 個が $x$ 方向に繋がった鎖状分子を考える。各要素はそれぞれ長さ $b$ で，矢印の先端に電荷 $Q$（$> 0$）をもつ。各要素は，矢印が $+x$ 方向に向くか，$-x$ 方向に向くかの二つの状態のみ取りうるものとする。これを，$i$ 番目要素の状態変数 $\mu_i$ を導入し，$\mu_i = +1$ または $-1$ で表す。1番目要素の矢印の始点が点 O（$x = 0$）に固定されていて，大きさ $E$ の電場（$E \ge 0$）が $+x$ の向きにかけられているものとする。また，この鎖状分子は温度 $T$ の熱浴に接しているものとする。

電荷は外部電場 $E$ とだけ相互作用し，電荷間の相互作用は無視できるものとする。また，$x$ と垂直方向への分子の広がりは無視できるものとし，ボルツマン定数を $k_{\mathrm{B}}$ として，以下の問に，解答に至る道筋を添えて答えよ。
{: .problem-lead }

<figure class="problem-figure" markdown>
![一様電場中の1次元荷電鎖状分子の模式図](../../../docs/assets/figures/pastexam-todai-ributsu/H14_butsuri_2-p-light.svg#only-light)
![一様電場中の1次元荷電鎖状分子の模式図](../../../docs/assets/figures/pastexam-todai-ributsu/H14_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">図1：始点 O に固定された1次元荷電鎖状分子と $+x$ 方向の電場 $E \ge 0$。</figcaption>
</figure>

(1) まず，$E = 0$ の場合を考える。

(a) 分子の端点の位置 $x_N$ の関数としてこの分子のエントロピー $S$ を求めよ。ただし，$L = bN$ とし，$N, x_N/b \gg 1$ であるとして，必要であれば Stirling の公式，すなわち，$x \gg 1$ のとき

$$
\log x! \sim x\log x - x + \cdots
$$

を用いよ。

(b) 端点位置を $x_N$ に保つために，この端点に加えなければならない力 $X$ と $x_N$ との関係を導け。

(c) $N \gg x_N/b$（$\gg 1$）の場合，$X$ と $x_N$ との関係式は近似的にどのように与えられるか。$x_N$ を外力 $X$ に対する分子の伸びとみたとき，この分子はどのような弾性体と言えるか。

(2) 次に，$E > 0$ の場合を考える。

(a) $E$ が与えられたもとでのこの鎖状分子の分配関数 $Z_N$ を，変数 $A \equiv bQE/(k_{\mathrm{B}}T)$ を用いて表せ。

(b) $i$ 番目要素の $\mu_i$ の平均値 $\langle\mu_i\rangle$ を求めよ。

(c) この鎖状分子の長さの平均値 $\langle x_N \rangle$ について，電場が十分小さい極限，$NA \ll 1$，での表式を求めよ。$\langle x_N \rangle$ を外力の総和 $NQE$ に対する分子の伸びとみたとき，前問 (1)(c) との関連を論ぜよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成14年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半の $E = 0$ の場合，内部エネルギーは配置によらず $0$ なので，鎖状分子の弾性は状態数の対数であるエントロピーのみから生じます。端点位置 $x_N$ を指定した状態数をスターリングの公式で評価し，自由エネルギーの微分から張力と伸びの関係を導きます。

後半の $E > 0$ の場合，$i$ 番目の電荷の位置は $1$ 番目から $i$ 番目までの要素の向き $\mu_j$ の和で決まるため，各 $\mu_j$ は自分より先端側にあるすべての電荷を動かすことになります。このことに注意してエネルギーを $\mu_j$ ごとに整理すると分配関数が各要素の積に分離し，弱電場極限の伸びを端点張力の場合と直接比べることができます。
</div>

### (1)

#### (a)

$N$ 個の要素のうち，$\mu_i = +1$ であるものの個数を $N_+$，$\mu_i = -1$ であるものの個数を $N_-$ とおきます。総数と端点位置 $x_N$ より次の関係が成り立ちます。

$$
N_+ + N_- = N, \qquad b(N_+ - N_-) = x_N
$$

$L = bN$ を用いて $N_+, N_-$ を解きます。

$$
N_+ = \frac{N}{2}\left(1 + \frac{x_N}{L}\right), \qquad N_- = \frac{N}{2}\left(1 - \frac{x_N}{L}\right)
$$

この端点位置を実現する配置の総数は $W = \dfrac{N!}{N_+!\,N_-!}$ です。スターリングの公式 $\log n! \simeq n\log n - n$ を用いてエントロピー $S = k_{\mathrm{B}}\log W$ を計算します。

$$
\begin{aligned}
S &= k_{\mathrm{B}}\bigl(\log N! - \log N_+! - \log N_-!\bigr) \\
&\simeq k_{\mathrm{B}}\bigl(N\log N - N - N_+\log N_+ + N_+ - N_-\log N_- + N_-\bigr) \\
&= -k_{\mathrm{B}}\left(N_+\log\frac{N_+}{N} + N_-\log\frac{N_-}{N}\right)
\end{aligned}
$$

ここに $\dfrac{N_\pm}{N} = \dfrac{1}{2}\left(1 \pm \dfrac{x_N}{L}\right)$ を代入します。

$$
\begin{aligned}
S &= -k_{\mathrm{B}}\frac{N}{2}\left\{\left(1 + \frac{x_N}{L}\right)\log\!\left(\frac{1 + x_N/L}{2}\right) + \left(1 - \frac{x_N}{L}\right)\log\!\left(\frac{1 - x_N/L}{2}\right)\right\} \\
&= N k_{\mathrm{B}}\log 2 - \frac{N k_{\mathrm{B}}}{2}\left\{\left(1 + \frac{x_N}{L}\right)\log\!\left(1 + \frac{x_N}{L}\right) + \left(1 - \frac{x_N}{L}\right)\log\!\left(1 - \frac{x_N}{L}\right)\right\}
\end{aligned}
$$

$$
\finalanswer{S(x_N) = N k_{\mathrm{B}}\log 2 - \frac{N k_{\mathrm{B}}}{2}\left\{\left(1 + \frac{x_N}{L}\right)\log\!\left(1 + \frac{x_N}{L}\right) + \left(1 - \frac{x_N}{L}\right)\log\!\left(1 - \frac{x_N}{L}\right)\right\}}
$$

#### (b)

$E = 0$ のとき系の内部エネルギーは $U = 0$ なので，ヘルムホルツの自由エネルギーは $F(T, x_N) = -T S(x_N)$ です。端点位置を $x_N$ に保つために端点に加える力 $X$ は $X = \left(\dfrac{\partial F}{\partial x_N}\right)_T = -T\dfrac{\partial S}{\partial x_N}$ から求めます。

$$
\begin{aligned}
X &= -T\frac{\partial S}{\partial x_N} \\
&= \frac{N k_{\mathrm{B}}T}{2}\left\{\frac{1}{L}\log\!\left(1 + \frac{x_N}{L}\right) + \frac{1}{L} - \frac{1}{L}\log\!\left(1 - \frac{x_N}{L}\right) - \frac{1}{L}\right\} \\
&= \frac{k_{\mathrm{B}}T}{2b}\log\!\left(\frac{1 + x_N/L}{1 - x_N/L}\right)
\end{aligned}
$$

ここで $N/L = 1/b$ を用いました。したがって，$X$ と $x_N$ の関係は次式となります。

$$
\finalanswer{X = \frac{k_{\mathrm{B}}T}{2b}\log\!\left(\frac{1 + x_N/L}{1 - x_N/L}\right)}
$$

#### (c)

$N \gg x_N/b$ すなわち $\dfrac{x_N}{L} \ll 1$ のとき，$\log(1 \pm y) \simeq \pm y$ の近似を用います。

$$
\begin{aligned}
X &\simeq \frac{k_{\mathrm{B}}T}{2b}\left(\frac{x_N}{L} - \left(-\frac{x_N}{L}\right)\right) \\
&= \frac{k_{\mathrm{B}}T}{bL}x_N \\
&= \frac{k_{\mathrm{B}}T}{Nb^2}x_N
\end{aligned}
$$

$$
\finalanswer{X \simeq \frac{k_{\mathrm{B}}T}{Nb^2}x_N}
$$

力 $X$ は伸び $x_N$ に比例するためフックの法則に従う線形弾性体であり，そのばね定数 $k = \dfrac{k_{\mathrm{B}}T}{Nb^2}$ は絶対温度 $T$ に比例して大きくなります。このような弾性はエネルギーではなくエントロピーの減少に由来するため，この分子を**エントロピー弾性体**といいます。

### (2)

#### (a)

$i$ 番目の要素の先端にある電荷 $Q$ の座標は $x_i = b\sum_{j=1}^{i} \mu_j$ です。一様電場 $E$ のもとでの全静電ポテンシャルエネルギー $U$ を計算し，和の順序を入れ替えます。

$$
\begin{aligned}
U &= -\sum_{i=1}^{N} Q E x_i \\
&= -b Q E \sum_{i=1}^{N}\sum_{j=1}^{i} \mu_j \\
&= -b Q E \sum_{j=1}^{N}\sum_{i=j}^{N} \mu_j \\
&= -b Q E \sum_{j=1}^{N} (N - j + 1)\mu_j
\end{aligned}
$$

$A \equiv \dfrac{bQE}{k_{\mathrm{B}}T}$ を用いると $-\dfrac{U}{k_{\mathrm{B}}T} = A\sum_{j=1}^{N} (N - j + 1)\mu_j$ となります。各 $\mu_j = \pm 1$ が独立なので，分配関数 $Z_N$ は積に分離されます。

$$
\begin{aligned}
Z_N &= \sum_{\mu_1 = \pm 1} \cdots \sum_{\mu_N = \pm 1} \exp\!\left\{A\sum_{j=1}^{N}(N - j + 1)\mu_j\right\} \\
&= \prod_{j=1}^{N} \left(e^{(N - j + 1)A} + e^{-(N - j + 1)A}\right) \\
&= \prod_{j=1}^{N} 2\cosh\!\bigl((N - j + 1)A\bigr)
\end{aligned}
$$

$k = N - j + 1$ とおき直すと，$Z_N$ は次式となります。

$$
\finalanswer{Z_N = 2^N \prod_{k=1}^{N} \cosh(kA)}
$$

#### (b)

各要素 $\mu_i$ は互いに独立であり，$\mu_i$ に関するボルツマン因子は $\exp\!\bigl((N - i + 1)A\mu_i\bigr)$ です。したがって平均値 $\langle\mu_i\rangle$ は次式になります。

$$
\begin{aligned}
\langle\mu_i\rangle &= \frac{e^{(N - i + 1)A} - e^{-(N - i + 1)A}}{e^{(N - i + 1)A} + e^{-(N - i + 1)A}} \\
&= \tanh\!\bigl((N - i + 1)A\bigr)
\end{aligned}
$$

$$
\finalanswer{\langle\mu_i\rangle = \tanh\!\bigl((N - i + 1)A\bigr)}
$$

#### (c)

鎖状分子の長さの平均値 $\langle x_N \rangle = b\sum_{i=1}^{N} \langle\mu_i\rangle$ に小問 (b) の結果を代入し，$k = N - i + 1$ とおき直します。

$$
\langle x_N \rangle = b\sum_{k=1}^{N} \tanh(kA)
$$

$NA \ll 1$ の極限ではすべての $k$（$1 \le k \le N$）に対して $kA \ll 1$ なので，$\tanh(kA) \simeq kA$ と近似します。

$$
\begin{aligned}
\langle x_N \rangle &\simeq bA\sum_{k=1}^{N} k \\
&= \frac{N(N + 1)}{2}bA \\
&= \frac{N(N + 1)b^2 QE}{2k_{\mathrm{B}}T}
\end{aligned}
$$

$N \gg 1$ では $N + 1 \simeq N$ なので，外力の総和 $F_{\mathrm{tot}} = NQE$ を用いて次のように書くことができます。

$$
\finalanswer{\langle x_N \rangle \simeq \frac{N(N + 1)}{2}bA \simeq \frac{Nb^2}{2k_{\mathrm{B}}T}(NQE)}
$$

設問 (1)(c) の結果を伸びについて解くと $x_N \simeq \dfrac{Nb^2}{k_{\mathrm{B}}T}X$ となります。外力の総和 $NQE$ を端点張力 $X$ に対応させて比べると，一様電場のもとでの伸び $\langle x_N \rangle$ は端点に同じ大きさの力 $X = NQE$ を加えた場合のちょうど半分になっています。これは，端点に力 $X$ を加えたときはすべての要素に一様に張力 $X$ がはたらくのに対し，一様電場では $i$ 番目の要素より先端側にある $N - i + 1$ 個の電荷からの力 $(N - i + 1)QE$ だけが $i$ 番目の要素にはたらき，分子全体で平均した張力が $\dfrac{1}{2}NQE$ になるためです。
