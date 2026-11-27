---
title: 東大理物 平成16年度 物理学 第2問：2状態単量体鎖状分子の統計力学と張力・長さ関係
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成16年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成16年度 物理学 第2問：2状態単量体鎖状分子の統計力学と張力・長さ関係

## 問題

図のように $N$ 個の単量体が連結された直線的な鎖状分子を考える。各単量体は図のように自由に変形し，長さ $a$ の状態 $\alpha$（エネルギー：$+\varepsilon$）か長さ $b$ の状態 $\beta$（エネルギー：$-\varepsilon$）のいずれかを，隣りあう単量体とは独立にとることができるとする。

<figure class="problem-figure" markdown>
![2状態単量体と鎖状分子の模式図](../../assets/figures/pastexam-todai-ributsu/H16_butsuri_2-p-light.svg#only-light)
![2状態単量体と鎖状分子の模式図](../../assets/figures/pastexam-todai-ributsu/H16_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">図1：単量体の状態 $\alpha$（長さ $a$，エネルギー $+\varepsilon$）と状態 $\beta$（長さ $b$，エネルギー $-\varepsilon$），および張力 $X$ のもとで長さ $L$ となった鎖状分子。</figcaption>
</figure>

鎖状分子が孤立した状態にあって，熱平衡に達している場合（ミクロカノニカル分布）を考える。
{: .problem-lead }

(1) $N_\alpha$ 個が $\alpha$，$N_\beta$ 個が $\beta$ の状態にいる場合を考える（$N = N_\alpha + N_\beta$）。鎖状分子の長さ $L$ とエネルギー $E_L$ を求めよ。また，この状態の熱力学的重率 $W(N_\alpha, N_\beta)$ を求め，鎖状分子のエントロピー $S$ が次のようになることを示せ。

$$
S = -k_B\left\{N_\alpha\log\frac{N_\alpha}{N} + N_\beta\log\frac{N_\beta}{N}\right\} \tag{1}
$$

ここで，$k_B$ はボルツマン定数である。Stirling の公式，$\log n! = n\log n - n$（$n \gg 1$）を用いてよい。また，$\log$ は自然対数とする。

つぎに，鎖状分子が温度 $T$ の熱浴に接していて，一定の温度状態におかれている場合（カノニカル分布）を考える。

(2) 熱浴の状態密度を $\Omega(E_B)$ とする。鎖状分子と熱浴からなる全系のエネルギーを $E_T$，状態 $l$ にある鎖状分子のエネルギーを $E_l$ とすれば（$E_T = E_B + E_l$），等重率の原理により，状態 $l$ の実現確率 $P(E_l)$ は，$l$ が指定された場合の微視的状態の数 $\Omega(E_T - E_l)\delta E$ に比例する。

$$
P(E_l) \propto \frac{\Omega(E_T - E_l)\delta E}{\Omega(E_T)\delta E} \tag{2}
$$

このことから，カノニカル分布では，状態 $l$ の実現確率 $P(E_l)$ は，$\exp(-E_l / k_B T)$ に比例することを示せ。ただし，熱浴は鎖状分子にくらべて十分大きいものとする。また，熱浴の温度が $T = (\partial S/\partial E)^{-1}|_{E = E_T}$ で表せることに留意せよ。

(3) 一つの単量体の分配関数 $Z_1$ を示し，さらに鎖状分子の分配関数 $Z_N$ を導け。

(4) 分配関数 $Z_N$ より，Helmholtz の自由エネルギー $F$，エントロピー $S$，系の内部エネルギー $E$ を求めよ。

(5) 比熱 $C$ を求め，温度の関数として図示せよ。ただし縦軸を $C/Nk_B$ とし，横軸を $k_B T/\varepsilon$ とせよ。

つぎに，鎖状分子を温度 $T$ の状態においたまま，一定の張力 $X$ で両端を引っぱり，長さ $L$ となった場合を考える。このとき，この系では，熱力学第一法則 $T\mathrm{d}S = \mathrm{d}E - X\mathrm{d}L$ が成立している。（$N$ 個の単量体からなる系を，非常に大きな $N_T$ 個からなる系の部分系と考えると，熱浴は $N_T - N$ 個からなる非常に大きな系と考えることができる。）

(6) 鎖状分子がエネルギー $E_L$ で長さ $L$ の状態にある確率 $p(E_L, L)$ は，熱浴を含む全系のエネルギーを $E_T$，長さを $L_T$ とすると，熱浴の状態密度 $\Omega(E_B) = \Omega(E_T - E_L, L_T - L)$ を用いて

$$
p(E_L, L) \propto \frac{\Omega(E_T - E_L, L_T - L)\delta E}{\Omega(E_T, L_T)\delta E} \tag{3}
$$

と書ける。$E_T, L_T$ に比べて $E_L, L$ が十分に微視的な量であることを利用して，

$$
p(E_L, L) \propto \exp\!\left\{\frac{1}{k_B T}(-E_L + XL)\right\} \tag{4}
$$

であることを示せ。

(7) 系の分配関数

$$
Y = \sum_{N_\alpha = 0}^{N} W(N_\alpha, N_\beta)\,p\bigl(E(N_\alpha, N_\beta), L(N_\alpha, N_\beta)\bigr) \tag{5}
$$

について，$N_\alpha$ に関する和を計算し，$N, T, X, a, b, +\varepsilon, -\varepsilon$ を用いて表せ。

(8) 分配関数より Gibbs の自由エネルギー $G$ を求め，そこから鎖状分子の長さ $L$ と張力 $X$ に関する関係式を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成16年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
巨大な熱浴とエネルギーや長さをやりとりする部分系の実現確率は，熱浴のエントロピーを部分系のエネルギーや長さの1次まで展開することでボルツマン因子として導くことができます。

各単量体が互いに独立に2状態をとるため，鎖状分子全体の分配関数は1単量体の分配関数の $N$ 乗になり，二項定理によってそのまま閉じた形でまとまります。自由エネルギーを温度や張力で偏微分することで，比熱や張力と長さの関係式を直接求めることができます。
</div>

### (1)

$N_\alpha$ 個の単量体が長さ $a$・エネルギー $+\varepsilon$ の状態 $\alpha$ をとり，$N_\beta$ 個の単量体が長さ $b$・エネルギー $-\varepsilon$ の状態 $\beta$ をとるので，鎖状分子の長さ $L$ とエネルギー $E_L$ は次式になります。

$$
L = N_\alpha a + N_\beta b, \qquad E_L = (N_\alpha - N_\beta)\varepsilon
$$

$N$ 個の単量体のうち状態 $\alpha$ をとる $N_\alpha$ 個を選ぶ場合の数が熱力学的重率 $W(N_\alpha, N_\beta)$ です。

$$
W(N_\alpha, N_\beta) = \frac{N!}{N_\alpha!\,N_\beta!}
$$

ボルツマンの関係式 $S = k_{\mathrm{B}}\log W(N_\alpha, N_\beta)$ にスターリングの公式 $\log n! \simeq n\log n - n$ と $N = N_\alpha + N_\beta$ を代入します。

$$
\begin{aligned}
S &= k_{\mathrm{B}}\bigl(\log N! - \log N_\alpha! - \log N_\beta!\bigr) \\
&= k_{\mathrm{B}}\bigl(N\log N - N - N_\alpha\log N_\alpha + N_\alpha - N_\beta\log N_\beta + N_\beta\bigr) \\
&= k_{\mathrm{B}}\bigl((N_\alpha + N_\beta)\log N - N_\alpha\log N_\alpha - N_\beta\log N_\beta\bigr) \\
&= -k_{\mathrm{B}}\left\{N_\alpha\log\frac{N_\alpha}{N} + N_\beta\log\frac{N_\beta}{N}\right\}
\end{aligned}
$$

これにより式 (1) が導かれます。求める $L, E_L, W(N_\alpha, N_\beta)$ は次式となります。

$$
\finalanswer{L = N_\alpha a + N_\beta b, \qquad E_L = (N_\alpha - N_\beta)\varepsilon, \qquad W(N_\alpha, N_\beta) = \frac{N!}{N_\alpha!\,N_\beta!}}
$$

### (2)

熱浴のエネルギーが $E_B$ であるときのエントロピーを $S_B(E_B) = k_{\mathrm{B}}\log\bigl(\Omega(E_B)\delta E\bigr)$ とおきます。すると $\Omega(E_B)\delta E = \exp\!\left(\dfrac{S_B(E_B)}{k_{\mathrm{B}}}\right)$ なので，式 (2) は次のように書き換えることができます。

$$
\begin{aligned}
P(E_l) &\propto \frac{\exp\!\left(\dfrac{S_B(E_T - E_l)}{k_{\mathrm{B}}}\right)}{\exp\!\left(\dfrac{S_B(E_T)}{k_{\mathrm{B}}}\right)} \\
&= \exp\!\left(\frac{S_B(E_T - E_l) - S_B(E_T)}{k_{\mathrm{B}}}\right)
\end{aligned}
$$

熱浴は鎖状分子に比べて十分大きく $E_l \ll E_T$ なので，$S_B(E_T - E_l)$ を $E_T$ のまわりで $E_l$ の1次までテイラー展開します。

$$
\begin{aligned}
S_B(E_T - E_l) - S_B(E_T) &\simeq -\left.\frac{\partial S_B}{\partial E}\right|_{E = E_T} E_l \\
&= -\frac{E_l}{T}
\end{aligned}
$$

ここで熱浴の温度の定義 $\left.\dfrac{\partial S_B}{\partial E}\right|_{E = E_T} = \dfrac{1}{T}$ を用いました。これを上の指数関数に代入すると，次式が得られます。

$$
P(E_l) \propto \exp\!\left(-\frac{E_l}{k_{\mathrm{B}}T}\right)
$$

### (3)

1つの単量体はエネルギー $+\varepsilon$ と $-\varepsilon$ の2状態をとるため，1つの単量体の分配関数 $Z_1$ は次式になります。

$$
\begin{aligned}
Z_1 &= e^{-\varepsilon/(k_{\mathrm{B}}T)} + e^{\varepsilon/(k_{\mathrm{B}}T)} \\
&= 2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

$N$ 個の単量体は互いに独立なので，鎖状分子全体の分配関数 $Z_N$ は $Z_1$ の $N$ 乗です。

$$
\begin{aligned}
Z_N &= Z_1^N \\
&= \left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\}^N
\end{aligned}
$$

したがって，$Z_1$ と $Z_N$ は次式となります。

$$
\finalanswer{Z_1 = 2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right), \qquad Z_N = \left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\}^N}
$$

### (4)

ヘルムホルツの自由エネルギー $F$ は $F = -k_{\mathrm{B}}T\log Z_N$ から求めます。

$$
F = -Nk_{\mathrm{B}}T\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\}
$$

エントロピー $S$ は $S = -\dfrac{\partial F}{\partial T}$ から計算します。

$$
\begin{aligned}
S &= -\frac{\partial}{\partial T}\left[-Nk_{\mathrm{B}}T\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\}\right] \\
&= Nk_{\mathrm{B}}\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\} + Nk_{\mathrm{B}}T\cdot\frac{\sinh\!\left(\dfrac{\varepsilon}{k_{\mathrm{B}}T}\right)}{\cosh\!\left(\dfrac{\varepsilon}{k_{\mathrm{B}}T}\right)}\left(-\frac{\varepsilon}{k_{\mathrm{B}}T^2}\right) \\
&= Nk_{\mathrm{B}}\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\} - \frac{N\varepsilon}{T}\tanh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

内部エネルギー $E$ は $E = F + TS$ から求めます。

$$
\begin{aligned}
E &= -Nk_{\mathrm{B}}T\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\} + Nk_{\mathrm{B}}T\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\} - N\varepsilon\tanh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right) \\
&= -N\varepsilon\tanh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

したがって，$F, S, E$ は次式となります。

$$
\finalanswer{F = -Nk_{\mathrm{B}}T\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\}, \quad S = Nk_{\mathrm{B}}\log\!\left\{2\cosh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\} - \frac{N\varepsilon}{T}\tanh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right), \quad E = -N\varepsilon\tanh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)}
$$

### (5)

設問4で求めた内部エネルギー $E$ を温度 $T$ で微分して比熱 $C = \dfrac{\partial E}{\partial T}$ を求めます。

$$
\begin{aligned}
C &= \frac{\partial}{\partial T}\left\{-N\varepsilon\tanh\!\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)\right\} \\
&= -N\varepsilon\cdot\frac{1}{\cosh^2\!\left(\dfrac{\varepsilon}{k_{\mathrm{B}}T}\right)}\left(-\frac{\varepsilon}{k_{\mathrm{B}}T^2}\right) \\
&= Nk_{\mathrm{B}}\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)^2\frac{1}{\cosh^2\!\left(\dfrac{\varepsilon}{k_{\mathrm{B}}T}\right)}
\end{aligned}
$$

したがって，比熱 $C$ は次式となります。

$$
\finalanswer{C = Nk_{\mathrm{B}}\left(\frac{\varepsilon}{k_{\mathrm{B}}T}\right)^2\frac{1}{\cosh^2\!\left(\dfrac{\varepsilon}{k_{\mathrm{B}}T}\right)}}
$$

無次元変数 $x = \dfrac{\varepsilon}{k_{\mathrm{B}}T}$ を用いると $\dfrac{C}{Nk_{\mathrm{B}}} = \dfrac{x^2}{\cosh^2 x}$ です。$t = \dfrac{k_{\mathrm{B}}T}{\varepsilon} = \dfrac{1}{x}$ の関数として調べると，低温 $t \to 0$ では $4x^2 e^{-2x} \to 0$ と急激に $0$ へ近づき，高温 $t \to \infty$ では $x^2 = \dfrac{1}{t^2} \to 0$ と減衰します。極大は $\dfrac{\mathrm{d}}{\mathrm{d}x}\left(\dfrac{x}{\cosh x}\right) = 0$ すなわち $x\tanh x = 1$（$x \simeq 1.20$，$t \simeq 0.83$）のときに現れ，最大値は約 $0.44$ です。概形は次の図のようになります。

<figure class="problem-figure" markdown>
![比熱の温度依存性](../../assets/figures/pastexam-todai-ributsu/H16_butsuri_2-s-light.svg#only-light)
![比熱の温度依存性](../../assets/figures/pastexam-todai-ributsu/H16_butsuri_2-s-dark.svg#only-dark)
<figcaption markdown="span">比熱 $C/(Nk_{\mathrm{B}})$ の無次元温度 $k_{\mathrm{B}}T/\varepsilon$ 依存性。</figcaption>
</figure>

### (6)

熱浴のエントロピーを $S_B(E_B, L_B) = k_{\mathrm{B}}\log\bigl(\Omega(E_B, L_B)\delta E\bigr)$ とおくと，式 (3) は次式になります。

$$
p(E_L, L) \propto \exp\!\left(\frac{S_B(E_T - E_L, L_T - L) - S_B(E_T, L_T)}{k_{\mathrm{B}}}\right)
$$

熱浴に対する熱力学第一法則 $T\,\mathrm{d}S_B = \mathrm{d}E_B - X\,\mathrm{d}L_B$ より，$\mathrm{d}S_B = \dfrac{1}{T}\,\mathrm{d}E_B - \dfrac{X}{T}\,\mathrm{d}L_B$ です。したがって，熱浴のエントロピーの偏微分は次式になります。

$$
\left(\frac{\partial S_B}{\partial E_B}\right)_{L_B} = \frac{1}{T}, \qquad \left(\frac{\partial S_B}{\partial L_B}\right)_{E_B} = -\frac{X}{T}
$$

$E_L \ll E_T$ かつ $L \ll L_T$ なので，$S_B(E_T - E_L, L_T - L)$ を1次までテイラー展開します。

$$
\begin{aligned}
S_B(E_T - E_L, L_T - L) - S_B(E_T, L_T) &\simeq -\frac{\partial S_B}{\partial E_B}E_L - \frac{\partial S_B}{\partial L_B}L \\
&= -\frac{E_L}{T} + \frac{XL}{T} \\
&= \frac{1}{T}(-E_L + XL)
\end{aligned}
$$

これを上の指数関数に代入すると，式 (4) が得られます。

$$
p(E_L, L) \propto \exp\!\left\{\frac{1}{k_{\mathrm{B}}T}(-E_L + XL)\right\}
$$

### (7)

設問1の $W(N_\alpha, N_\beta) = \dfrac{N!}{N_\alpha!\,N_\beta!}$，$E(N_\alpha, N_\beta) = (N_\alpha - N_\beta)\varepsilon$，$L(N_\alpha, N_\beta) = N_\alpha a + N_\beta b$（$N_\beta = N - N_\alpha$），および設問6の重み因子を式 (5) に代入します。

$$
\begin{aligned}
Y &= \sum_{N_\alpha = 0}^{N} \frac{N!}{N_\alpha!(N - N_\alpha)!}\exp\!\left\{\frac{1}{k_{\mathrm{B}}T}\Bigl(-(N_\alpha - N_\beta)\varepsilon + X(N_\alpha a + N_\beta b)\Bigr)\right\} \\
&= \sum_{N_\alpha = 0}^{N} {}_N C_{N_\alpha} \exp\!\left(\frac{-\varepsilon + Xa}{k_{\mathrm{B}}T}N_\alpha\right)\exp\!\left(\frac{+\varepsilon + Xb}{k_{\mathrm{B}}T}(N - N_\alpha)\right) \\
&= \sum_{N_\alpha = 0}^{N} {}_N C_{N_\alpha} \left\{\exp\!\left(\frac{-\varepsilon + Xa}{k_{\mathrm{B}}T}\right)\right\}^{N_\alpha}\left\{\exp\!\left(\frac{+\varepsilon + Xb}{k_{\mathrm{B}}T}\right)\right\}^{N - N_\alpha}
\end{aligned}
$$

二項定理を用いて和をまとめると，分配関数 $Y$ は次式となります。

$$
\finalanswer{Y = \left\{\exp\!\left(\frac{Xa - \varepsilon}{k_{\mathrm{B}}T}\right) + \exp\!\left(\frac{Xb + \varepsilon}{k_{\mathrm{B}}T}\right)\right\}^N}
$$

### (8)

ギブスの自由エネルギー $G$ は $G = -k_{\mathrm{B}}T\log Y$ です。

$$
G = -Nk_{\mathrm{B}}T\log\!\left\{\exp\!\left(\frac{Xa - \varepsilon}{k_{\mathrm{B}}T}\right) + \exp\!\left(\frac{Xb + \varepsilon}{k_{\mathrm{B}}T}\right)\right\}
$$

熱力学第一法則 $T\,\mathrm{d}S = \mathrm{d}E - X\,\mathrm{d}L$ より，ギブスの自由エネルギー $G = E - TS - XL$ の全微分は $\mathrm{d}G = -S\,\mathrm{d}T - L\,\mathrm{d}X$ となります。したがって，鎖状分子の平均の長さ $L$ は $L = -\left(\dfrac{\partial G}{\partial X}\right)_T$ から求めることができます。

$$
\begin{aligned}
L &= -\left(\frac{\partial G}{\partial X}\right)_T \\
&= Nk_{\mathrm{B}}T\frac{\dfrac{a}{k_{\mathrm{B}}T}\exp\!\left(\dfrac{Xa - \varepsilon}{k_{\mathrm{B}}T}\right) + \dfrac{b}{k_{\mathrm{B}}T}\exp\!\left(\dfrac{Xb + \varepsilon}{k_{\mathrm{B}}T}\right)}{\exp\!\left(\dfrac{Xa - \varepsilon}{k_{\mathrm{B}}T}\right) + \exp\!\left(\dfrac{Xb + \varepsilon}{k_{\mathrm{B}}T}\right)} \\
&= N\frac{a\exp\!\left(\dfrac{Xa - \varepsilon}{k_{\mathrm{B}}T}\right) + b\exp\!\left(\dfrac{Xb + \varepsilon}{k_{\mathrm{B}}T}\right)}{\exp\!\left(\dfrac{Xa - \varepsilon}{k_{\mathrm{B}}T}\right) + \exp\!\left(\dfrac{Xb + \varepsilon}{k_{\mathrm{B}}T}\right)}
\end{aligned}
$$

分子と分母に $\exp\!\left(-\dfrac{X(a + b)}{2k_{\mathrm{B}}T}\right)$ を掛けて双曲線正接でまとめることもできます。

$$
L = N\frac{a + b}{2} + N\frac{a - b}{2}\tanh\!\left(\frac{X(a - b) - 2\varepsilon}{2k_{\mathrm{B}}T}\right)
$$

したがって，ギブスの自由エネルギー $G$ と長さ $L$・張力 $X$ の関係式は次式となります。

$$
\finalanswer{G = -Nk_{\mathrm{B}}T\log\!\left\{e^{(Xa - \varepsilon)/(k_{\mathrm{B}}T)} + e^{(Xb + \varepsilon)/(k_{\mathrm{B}}T)}\right\}, \qquad L = N\frac{a + b}{2} + N\frac{a - b}{2}\tanh\!\left(\frac{X(a - b) - 2\varepsilon}{2k_{\mathrm{B}}T}\right)}
$$
