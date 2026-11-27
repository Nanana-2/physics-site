---
title: 東大理物 平成22年度 物理学 第2問：2状態単量体からなる鎖状分子の統計力学
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成22年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して解答にグラフを追加しています。
---

# 東大理物 平成22年度 物理学 第2問：2状態単量体からなる鎖状分子の統計力学

## 問題

図のように $N$ 個の単量体が連結された直線的な鎖状分子を考える。各単量体は図のように自由に変形し，長さ $a$ の状態 $\alpha$ か長さ $b$ の状態 $\beta$ のいずれかを，隣りあう単量体とは独立にとることができる。ただし，$a > b$ とする。また，各単量体の2つの状態 $\alpha, \beta$ が持つエネルギーは，$f$ を定数として，それぞれ $-fa, -fb$ であるとする。すなわち，鎖状分子の全長を $L$ とすると，全エネルギーは $E = -fL$ となる。ただし，設問6以外では $f > 0$ とする。

<figure class="problem-figure" markdown>
![長さaの状態alphaと長さbの状態betaからなる鎖状分子](../../assets/figures/pastexam-todai-ributsu/H22_butsuri_2-p-light.svg#only-light)
![長さaの状態alphaと長さbの状態betaからなる鎖状分子](../../assets/figures/pastexam-todai-ributsu/H22_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">長さ $a$ の状態 $\alpha$ と長さ $b$ の状態 $\beta$ をとる単量体が連結した鎖状分子。</figcaption>
</figure>

(1) 鎖状分子が，与えられた全エネルギーについてのミクロカノニカル分布に従う状態にあると考える。状態 $\alpha$ をとる単量体が $N_\alpha$ 個，状態 $\beta$ をとる単量体が $N_\beta$ 個とする。ただし，$N_\alpha + N_\beta = N$ である。このとき，鎖状分子のエントロピー $S$ をボルツマン定数 $k_{\mathrm{B}}$ および $N_\alpha, N_\beta$ を用いて表せ。

以下では，単量体の個数 $N$ が大きい極限を考える。単量体1個あたりの物理量は，この極限で一定値に収束する。これ以降の設問に対しては，$N$ によらない形で答えること。

(2) 設問1と同じミクロカノニカル分布について，単量体1個あたりのエネルギー $\epsilon = E / N$ の関数として，単量体1個あたりのエントロピー $s = S / N$ を求め，グラフの概形を図示せよ。なお，大きな整数 $M \gg 1$ に対して成立する Stirling の公式 $\log M! \sim M\log M - M$ を用いてもよい。ここで $\log x$ は $x$ の自然対数を意味する。

以下では，鎖状分子が温度 $T$ の熱平衡状態にあるとする。

(3) 絶対零度および温度無限大それぞれの場合について，鎖状分子の単量体1個あたりのエントロピー $s$ を求めよ。

(4) 温度 $T$ を与えたとき，鎖状分子の単量体1個あたりの長さは $T$ の関数 $l(T)$ となる。温度の上昇とともに，鎖状分子の長さは増大するか減少するか，その物理的理由とともに答えよ。また，$l(T = 0)$ と $l(T = \infty)$ の値を求めよ。

(5) この系の，温度 $T$ における単量体1個あたりの熱容量を $c(T)$ とする。積分

$$
\int_0^{\infty} \frac{c(T)}{T}\,\mathrm{d}T
$$

の値を求めよ。

(6) 単量体の2つの状態 $\alpha, \beta$ の持つエネルギーが等しい，すなわち $f = 0$ のとき，鎖状分子の単量体1個あたりの長さを求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成22年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して解答にグラフを追加しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
各単量体は隣と独立に2つの状態をとるので，$N_\alpha$ を決めると，状態の数は $N$ 個から $N_\alpha$ 個を選ぶ組合せの数になります。$N$ が大きいときは，スターリングの公式で階乗の対数を近似し，単量体1個あたりの量に書き直します。

温度 $T$ の熱平衡でも，単量体は互いに独立です。そのため，1個の単量体の2つの状態のボルツマン因子から確率を作り，長さやエントロピーをその確率で表します。

熱容量とエントロピーは $\mathrm{d}s=\dfrac{c}{T}\,\mathrm{d}T$ で結びついています。この関係から，$\dfrac{c(T)}{T}$ の積分は $T=0$ と $T=\infty$ のエントロピーの差として求めます。
</div>

### (1)
$N = N_\alpha + N_\beta$ 個の単量体のうち $N_\alpha$ 個が状態 $\alpha$，残り $N_\beta$ 個が状態 $\beta$ をとる微視的状態の数 $W$ は二項係数 $\dfrac{(N_\alpha + N_\beta)!}{N_\alpha! N_\beta!}$ です。ボルツマンの公式 $S = k_{\mathrm{B}}\log W$ より，エントロピー $S$ は次のとおりです。

$$
\finalanswer{S = k_{\mathrm{B}}\log\frac{(N_\alpha + N_\beta)!}{N_\alpha! N_\beta!}}
$$

### (2)
$p \equiv \dfrac{N_\alpha}{N}$ とおくと，$\dfrac{N_\beta}{N} = 1 - p$ であり，$0 \le p \le 1$ です。単量体1個あたりのエネルギー $\epsilon$ は

$$
\begin{aligned}
\epsilon &= \frac{-f(N_\alpha a + N_\beta b)}{N} \\
&= -f\bigl(p a + (1 - p) b\bigr) \\
&= -fb - f(a - b)p
\end{aligned}
$$

なので，$p$ と $1 - p$ は $\epsilon$ を用いて次のように表されます。ここで $-fa \le \epsilon \le -fb$ です。

$$
p = \frac{-\epsilon - fb}{f(a - b)}, \qquad 1 - p = \frac{\epsilon + fa}{f(a - b)}
$$

スターリングの公式 $\log M! \sim M\log M - M$ を設問1の式に用いて $s = S / N$ を計算します。

$$
\begin{aligned}
S &\simeq k_{\mathrm{B}}\bigl[(N\log N - N) - (N_\alpha\log N_\alpha - N_\alpha) - (N_\beta\log N_\beta - N_\beta)\bigr] \\
&= k_{\mathrm{B}}\left[-N_\alpha\log\frac{N_\alpha}{N} - N_\beta\log\frac{N_\beta}{N}\right] \\
s &= -k_{\mathrm{B}}\bigl[p\log p + (1 - p)\log(1 - p)\bigr]
\end{aligned}
$$

$p$ と $1 - p$ を代入すると，次式が得られます。

$$
s(\epsilon) = -k_{\mathrm{B}}\left[\frac{-\epsilon - fb}{f(a - b)}\log\frac{-\epsilon - fb}{f(a - b)} + \frac{\epsilon + fa}{f(a - b)}\log\frac{\epsilon + fa}{f(a - b)}\right] \qquad (-fa \le \epsilon \le -fb)
$$

式の両端では $0\log0=0$ を極限の意味で用います。$s(\epsilon)$ は $\epsilon = -fa$ と $\epsilon = -fb$ で $0$ となり，中点 $\epsilon = -\dfrac{f(a + b)}{2}$ に関して対称で，中点で最大値 $k_{\mathrm{B}}\log 2$ をとる上に凸の曲線です。両端での傾きは発散します。グラフの概形は次の図のとおりです。

<figure class="problem-figure" markdown>
![単量体1個あたりのエントロピーs(epsilon)のグラフ](../../assets/figures/pastexam-todai-ributsu/H22_butsuri_2-s-light.svg#only-light)
![単量体1個あたりのエントロピーs(epsilon)のグラフ](../../assets/figures/pastexam-todai-ributsu/H22_butsuri_2-s-dark.svg#only-dark)
<figcaption markdown="span">単量体1個あたりのエントロピー $s(\epsilon)$ の概形。$\epsilon = -\dfrac{f(a+b)}{2}$ で最大値 $k_{\mathrm{B}}\log 2$ をとる。</figcaption>
</figure>

$$
\finalanswer{s(\epsilon) = -k_{\mathrm{B}}\left[\frac{-\epsilon - fb}{f(a - b)}\log\frac{-\epsilon - fb}{f(a - b)} + \frac{\epsilon + fa}{f(a - b)}\log\frac{\epsilon + fa}{f(a - b)}\right] \qquad (-fa \le \epsilon \le -fb)}
$$

### (3)
カノニカル分布において，各単量体が状態 $\alpha$ をとる確率 $p_\alpha$ と状態 $\beta$ をとる確率 $p_\beta$ は $\beta_{\mathrm{th}} = \dfrac{1}{k_{\mathrm{B}} T}$ を用いて

$$
p_\alpha = \frac{e^{\beta_{\mathrm{th}} f a}}{e^{\beta_{\mathrm{th}} f a} + e^{\beta_{\mathrm{th}} f b}}, \qquad p_\beta = \frac{e^{\beta_{\mathrm{th}} f b}}{e^{\beta_{\mathrm{th}} f a} + e^{\beta_{\mathrm{th}} f b}}
$$

です。$f > 0$，$a > b$ より $-fa < -fb$ なので，絶対零度 $T \to 0$ ではすべての単量体が最低エネルギーの状態 $\alpha$ をとり，$p_\alpha \to 1$，$p_\beta \to 0$ となって $s = 0$ です。

温度無限大 $T \to \infty$ では $\beta_{\mathrm{th}} \to 0$ より2つの状態が等確率 $p_\alpha = p_\beta = 1/2$ で現れ，$s = k_{\mathrm{B}}\log 2$ となります。

$$
\finalanswer{s(T = 0) = 0, \qquad s(T = \infty) = k_{\mathrm{B}}\log 2}
$$

### (4)
単量体1個あたりの長さの期待値 $l(T)$ を計算します。

$$
\begin{aligned}
l(T) &= a p_\alpha + b p_\beta \\
&= \frac{a e^{\frac{fa}{k_{\mathrm{B}} T}} + b e^{\frac{fb}{k_{\mathrm{B}} T}}}{e^{\frac{fa}{k_{\mathrm{B}} T}} + e^{\frac{fb}{k_{\mathrm{B}} T}}} \\
&= \frac{a + b e^{-\frac{f(a - b)}{k_{\mathrm{B}} T}}}{1 + e^{-\frac{f(a - b)}{k_{\mathrm{B}} T}}} \\
&= b + \frac{a - b}{1 + e^{-\frac{f(a - b)}{k_{\mathrm{B}} T}}}
\end{aligned}
$$

温度 $T$ が上昇すると，$e^{-f(a-b)/(k_{\mathrm{B}} T)}$ は単調に増加します。したがって，$l(T)$ は温度の上昇とともに減少します。

低温では，ほとんどの単量体がエネルギーの低い長い状態 $\alpha$ をとります。温度が上がると，2つの状態が混ざるほうがエントロピーが大きくなるので，エネルギーの高い短い状態 $\beta$ をとる単量体が増えます。そのため，鎖全体の長さは短くなります。

極限の値は $T \to 0$ で $e^{-f(a-b)/(k_{\mathrm{B}} T)} \to 0$ より $l(T = 0) = a$，$T \to \infty$ で $e^{-f(a-b)/(k_{\mathrm{B}} T)} \to 1$ より $l(T = \infty) = \dfrac{a + b}{2}$ です。

$$
\finalanswer{l(T = 0) = a, \qquad l(T = \infty) = \frac{a + b}{2}}
$$

### (5)
熱容量とエントロピーの関係式 $\dfrac{\mathrm{d}s}{\mathrm{d}T} = \dfrac{c(T)}{T}$ を用いて積分を計算し，設問3の結果を代入します。

$$
\begin{aligned}
\int_0^{\infty} \frac{c(T)}{T}\,\mathrm{d}T &= \int_0^{\infty} \frac{\mathrm{d}s}{\mathrm{d}T}\,\mathrm{d}T \\
&= s(T = \infty) - s(T = 0) \\
&= k_{\mathrm{B}}\log 2 - 0 \\
&= k_{\mathrm{B}}\log 2
\end{aligned}
$$

$$
\finalanswer{\int_0^{\infty} \frac{c(T)}{T}\,\mathrm{d}T = k_{\mathrm{B}}\log 2}
$$

### (6)
$f = 0$ のとき，状態 $\alpha$ と状態 $\beta$ のエネルギーはともに $0$ で等しいため，任意の温度 $T > 0$ で両者の出現確率は等しく $p_\alpha = p_\beta = 1/2$ となります。よって単量体1個あたりの長さは次のとおりです。

$$
\begin{aligned}
l &= \frac{1}{2}a + \frac{1}{2}b \\
&= \frac{a + b}{2}
\end{aligned}
$$

$$
\finalanswer{\frac{a + b}{2}}
$$
