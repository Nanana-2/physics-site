---
title: 東大理物 平成20年度 物理学 第2問：3状態独立分子系の統計力学とゆらぎ応答関係
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成20年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成20年度 物理学 第2問：3状態独立分子系の統計力学とゆらぎ応答関係

## 問題

ある分子 $N$ 個からなる系を考える。それぞれの分子は3つの状態をとる。そのうちの2つの状態のエネルギーは縮退しており，そのエネルギーの値を $0$ とする。残りの1つの状態のエネルギーを $\varepsilon$ とする。それぞれの分子は互いに独立とする。この系が温度 $T$ の熱平衡状態にあると仮定して以下の設問に答えよ。

(1) この系の内部エネルギーを求めよ。

(2) この系のエントロピーを求めよ。また，$\varepsilon > 0$，$\varepsilon = 0$，$\varepsilon < 0$ のそれぞれの場合について，$T = 0$ でのエントロピーを求め，それらの値が異なる理由を説明せよ。

エネルギーが $\varepsilon$ の状態にある分子の数を $N_\varepsilon$ とする。以下の設問で必要ならば，二項分布の公式

$$
(x + y)^N = \sum_{m=0}^{N} {}_N C_m x^{N-m} y^m
$$

を利用してもよい。
{: .problem-lead }

(3) 熱平衡状態での $N_\varepsilon$ の分布関数 $P(N_\varepsilon)$ を求めよ。

(4) 熱平衡状態での $N_\varepsilon$ の平均値 $\langle N_\varepsilon \rangle$ を求めよ。次に，ある温度 $T = T_1$ において，$\langle N_\varepsilon \rangle$ が $\varepsilon$ によってどのように変化するかについて考える。特に，$\varepsilon$ が $\pm\infty$ に近づく場合の振る舞いや $\varepsilon = 0$ 付近の様子に注意して，$\langle N_\varepsilon \rangle$ を $\varepsilon$ の関数として概形を図示せよ。また，温度が $T = 2T_1$ の場合の $\langle N_\varepsilon \rangle$ の概形も合わせて図示せよ。

(5) 熱平衡状態における $N_\varepsilon$ の分散 $\langle N_\varepsilon^2 \rangle - \langle N_\varepsilon \rangle^2$ を求めよ。

(6) $\langle N_\varepsilon \rangle$ の $\varepsilon$ に対する応答関数

$$
\chi = \frac{\partial\langle N_\varepsilon \rangle}{\partial\varepsilon}
$$

を求めよ。また，$\chi$ を $\langle N_\varepsilon^2 \rangle - \langle N_\varepsilon \rangle^2$ を用いて表せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成20年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
$N$ 個の分子が互いに独立なため，系全体の分配関数は1分子の分配関数の $N$ 乗になります。そのため，内部エネルギーやエントロピーなどの熱力学量はすべて1分子の分配関数の対数微分から求めることができます。

各分子がエネルギー $\varepsilon$ の状態にいるかどうかは独立な2通りの選択なので，その状態にいる分子数は二項展開で数えます。二項展開の公式をパラメータで微分すると，平均値や分散だけでなく，エネルギー $\varepsilon$ を変化させたときの応答関数と分散の比例関係も直接導くことができます。
</div>

### (1)

ボルツマン定数を $k_{\mathrm{B}}$ とし，$\beta = \dfrac{1}{k_{\mathrm{B}}T}$ とおきます。1個の分子はエネルギー $0$ の状態を2つ，エネルギー $\varepsilon$ の状態を1つとるので，1分子の分配関数 $Z_1$ は次式になります。

$$
\begin{aligned}
Z_1 &= 2e^{-\beta\cdot 0} + e^{-\beta\varepsilon} \\
&= 2 + e^{-\beta\varepsilon}
\end{aligned}
$$

$N$ 個の分子は互いに独立なので，系全体の分配関数 $Z$ は $Z_1$ の $N$ 乗です。

$$
\begin{aligned}
Z &= Z_1^N \\
&= \bigl(2 + e^{-\beta\varepsilon}\bigr)^N
\end{aligned}
$$

内部エネルギー $U$ は $U = -\dfrac{\partial\ln Z}{\partial\beta}$ から計算します。

$$
\begin{aligned}
U &= -\frac{\partial}{\partial\beta}\Bigl(N\ln\bigl(2 + e^{-\beta\varepsilon}\bigr)\Bigr) \\
&= -N\frac{-\varepsilon e^{-\beta\varepsilon}}{2 + e^{-\beta\varepsilon}} \\
&= \frac{N\varepsilon e^{-\beta\varepsilon}}{2 + e^{-\beta\varepsilon}} \\
&= \frac{N\varepsilon}{2e^{\beta\varepsilon} + 1}
\end{aligned}
$$

したがって，内部エネルギーは次式となります。

$$
\finalanswer{U = \frac{N\varepsilon}{2e^{\varepsilon/(k_{\mathrm{B}}T)} + 1}}
$$

### (2)

ヘルムホルツの自由エネルギーは 

$$
\begin{aligned}
F &= -k_{\mathrm{B}}T\ln Z \\
&= -Nk_{\mathrm{B}}T\ln\bigl(2 + e^{-\beta\varepsilon}\bigr)
\end{aligned}
$$

です。エントロピー $S$ は $F = U - TS$ すなわち $S = \dfrac{U - F}{T}$ から求めます。

$$
\begin{aligned}
S &= \frac{U}{T} - \frac{F}{T} \\
&= \frac{N\varepsilon}{T\bigl(2e^{\beta\varepsilon} + 1\bigr)} + Nk_{\mathrm{B}}\ln\bigl(2 + e^{-\beta\varepsilon}\bigr)
\end{aligned}
$$

したがって，この系のエントロピーは次式となります。

$$
\finalanswer{S = Nk_{\mathrm{B}}\ln\!\left(2 + e^{-\varepsilon/(k_{\mathrm{B}}T)}\right) + \frac{N\varepsilon}{T\bigl(2e^{\varepsilon/(k_{\mathrm{B}}T)} + 1\bigr)}}
$$

次に $\varepsilon$ の符号ごとに $T \to 0$，すなわち $\beta \to \infty$ の極限を求めます。

まず $\varepsilon > 0$ のとき，$\beta\varepsilon \to +\infty$ なので $e^{-\beta\varepsilon} \to 0$，かつ $\beta\varepsilon e^{-\beta\varepsilon} \to 0$ です。よって次式が得られます。

$$
\begin{aligned}
\lim_{T \to 0} S &= Nk_{\mathrm{B}}\ln(2 + 0) + 0 \\
&= Nk_{\mathrm{B}}\ln 2
\end{aligned}
$$

次に $\varepsilon = 0$ のとき，温度によらず $e^{-\beta\varepsilon} = 1$ です。

$$
\begin{aligned}
S &= Nk_{\mathrm{B}}\ln(2 + 1) + 0 \\
&= Nk_{\mathrm{B}}\ln 3
\end{aligned}
$$

最後に $\varepsilon < 0$ のとき，$-\beta\varepsilon \to +\infty$ なので，$\ln(2 + e^{-\beta\varepsilon}) = -\beta\varepsilon + \ln(1 + 2e^{\beta\varepsilon})$ と変形します。

$$
\begin{aligned}
S &= Nk_{\mathrm{B}}\bigl(-\beta\varepsilon + \ln(1 + 2e^{\beta\varepsilon})\bigr) + Nk_{\mathrm{B}}\frac{\beta\varepsilon}{2e^{\beta\varepsilon} + 1} \\
&= Nk_{\mathrm{B}}\ln(1 + 2e^{\beta\varepsilon}) - Nk_{\mathrm{B}}\frac{2\beta\varepsilon e^{\beta\varepsilon}}{2e^{\beta\varepsilon} + 1}
\end{aligned}
$$

$T \to 0$ で $e^{\beta\varepsilon} \to 0$ かつ $\beta\varepsilon e^{\beta\varepsilon} \to 0$ なので，$\displaystyle \lim_{T \to 0} S = 0$ です。

$$
\finalanswer{\varepsilon > 0:\ S = Nk_{\mathrm{B}}\ln 2, \qquad \varepsilon = 0:\ S = Nk_{\mathrm{B}}\ln 3, \qquad \varepsilon < 0:\ S = 0}
$$

値が異なる理由は，各分子の基底状態の縮退度の違いにあります。$T = 0$ では各分子はエネルギーが最も低い基底状態のみをとり，系全体の基底状態の微視的状態数 $W_0$ に対して $S = k_{\mathrm{B}}\ln W_0$ となります。$\varepsilon > 0$ ではエネルギー $0$ の2状態が基底状態となるため $W_0 = 2^N$，$\varepsilon = 0$ では3状態すべてが基底状態となるため $W_0 = 3^N$，$\varepsilon < 0$ ではエネルギー $\varepsilon$ の1状態のみが基底状態となるため $W_0 = 1$ となり，それぞれ $Nk_{\mathrm{B}}\ln 2$，$Nk_{\mathrm{B}}\ln 3$，$0$ を与えます。

### (3)

エネルギー $\varepsilon$ の状態にある分子が $N_\varepsilon$ 個，エネルギー $0$ の状態にある分子が $N - N_\varepsilon$ 個である微視的状態の選び方を数えます。どの $N_\varepsilon$ 個の分子がエネルギー $\varepsilon$ の状態をとるかの選び方は ${}_N C_{N_\varepsilon}$ 通りです。エネルギー $0$ の状態をとる残りの $N - N_\varepsilon$ 個の分子はそれぞれ縮退した2状態のどちらかを独立に選ぶことができるので，その選び方は $2^{N - N_\varepsilon}$ 通りです。

このような各微視的状態のエネルギーは $N_\varepsilon \varepsilon$ なので，ボルツマン因子は $e^{-\beta\varepsilon N_\varepsilon}$ です。これを分配関数 $Z = (2 + e^{-\beta\varepsilon})^N$ で割ることで，確率分布 $P(N_\varepsilon)$ が得られます。

$$
\begin{aligned}
P(N_\varepsilon) &= \frac{{}_N C_{N_\varepsilon}\, 2^{N - N_\varepsilon} e^{-\beta\varepsilon N_\varepsilon}}{Z} \\
&= {}_N C_{N_\varepsilon}\,\frac{2^{N - N_\varepsilon} e^{-\beta\varepsilon N_\varepsilon}}{\bigl(2 + e^{-\beta\varepsilon}\bigr)^N}
\end{aligned}
$$

したがって，分布関数 $P(N_\varepsilon)$ は次式となります。

$$
\finalanswer{P(N_\varepsilon) = {}_N C_{N_\varepsilon}\,\frac{2^{N - N_\varepsilon} e^{-\varepsilon N_\varepsilon / (k_{\mathrm{B}}T)}}{\bigl(2 + e^{-\varepsilon / (k_{\mathrm{B}}T)}\bigr)^N}}
$$

### (4)

二項分布の公式 $\displaystyle (x + y)^N = \sum_{m=0}^{N} {}_N C_m x^{N-m} y^m$ の両辺を $y$ で微分し，さらに $y$ を掛けます。

$$
\begin{aligned}
N(x + y)^{N-1} &= \sum_{m=0}^{N} m\,{}_N C_m x^{N-m} y^{m-1} \\
Ny(x + y)^{N-1} &= \sum_{m=0}^{N} m\,{}_N C_m x^{N-m} y^m
\end{aligned}
$$

ここで $x = 2$，$y = e^{-\beta\varepsilon}$ とおき，両辺を $Z = (2 + e^{-\beta\varepsilon})^N$ で割ります。

$$
\begin{aligned}
\langle N_\varepsilon \rangle &= \sum_{m=0}^{N} m\,P(m) \\
&= \frac{N e^{-\beta\varepsilon}(2 + e^{-\beta\varepsilon})^{N-1}}{(2 + e^{-\beta\varepsilon})^N} \\
&= \frac{N e^{-\beta\varepsilon}}{2 + e^{-\beta\varepsilon}} \\
&= \frac{N}{2e^{\beta\varepsilon} + 1}
\end{aligned}
$$

したがって，平均値 $\langle N_\varepsilon \rangle$ は次式となります。

$$
\finalanswer{\langle N_\varepsilon \rangle = \frac{N}{2e^{\varepsilon/(k_{\mathrm{B}}T)} + 1}}
$$

$\langle N_\varepsilon \rangle$ の $\varepsilon$ に対する振る舞いを調べます。

- $\varepsilon \to -\infty$ のとき，$e^{\beta\varepsilon} \to 0$ なので $\langle N_\varepsilon \rangle \to N$ に近づきます。
- $\varepsilon \to +\infty$ のとき，$e^{\beta\varepsilon} \to +\infty$ なので $\langle N_\varepsilon \rangle \to 0$ に近づきます。
- $\varepsilon = 0$ のとき，温度 $T$ によらず $\langle N_\varepsilon \rangle = \dfrac{N}{3}$ を通ります。
- $\varepsilon$ について単調減少であり，$\varepsilon = 0$ での傾きは $-\dfrac{2N}{9k_{\mathrm{B}}T}$ です。

温度を $T = 2T_1$ に上げると，$\varepsilon = 0$ での値 $\dfrac{N}{3}$ と $\varepsilon \to \pm\infty$ での漸近値は変わりませんが，変数 $\dfrac{\varepsilon}{k_{\mathrm{B}}T}$ が半分になるため，グラフは横方向に2倍に引き伸ばされ，変化が緩やかになります。$\varepsilon < 0$ では $T = 2T_1$ の方が小さく，$\varepsilon > 0$ では $T = 2T_1$ の方が大きくなります。概形は次の図のようになります。

<figure class="problem-figure" markdown>
![平均分子数のエネルギー依存性の概形](../../../docs/assets/figures/pastexam-todai-ributsu/H20_butsuri_2-s-light.svg#only-light)
![平均分子数のエネルギー依存性の概形](../../../docs/assets/figures/pastexam-todai-ributsu/H20_butsuri_2-s-dark.svg#only-dark)
<figcaption markdown="span">$\langle N_\varepsilon \rangle$ の $\varepsilon$ 依存性の概形（実線：$T = T_1$，破線：$T = 2T_1$）。</figcaption>
</figure>

### (5)

設問4で得た恒等式 $\displaystyle \sum_{m=0}^{N} m\,{}_N C_m x^{N-m} y^m = Ny(x + y)^{N-1}$ の両辺を再び $y$ で微分し，さらに $y$ を掛けます。

$$
\begin{aligned}
\sum_{m=0}^{N} m^2\,{}_N C_m x^{N-m} y^m &= y\frac{\partial}{\partial y}\Bigl(Ny(x + y)^{N-1}\Bigr) \\
&= Ny(x + y)^{N-1} + N(N - 1)y^2(x + y)^{N-2}
\end{aligned}
$$

$x = 2$，$y = e^{-\beta\varepsilon}$ を代入し，両辺を $Z = (x + y)^N$ で割ると，$\langle N_\varepsilon^2 \rangle$ が得られます。

$$
\begin{aligned}
\langle N_\varepsilon^2 \rangle &= \frac{Ny}{x + y} + \frac{N(N - 1)y^2}{(x + y)^2} \\
&= \frac{Ny(x + y) + N^2 y^2 - Ny^2}{(x + y)^2} \\
&= \frac{Nxy}{(x + y)^2} + \left(\frac{Ny}{x + y}\right)^2
\end{aligned}
$$

第2項は $\langle N_\varepsilon \rangle^2$ に等しいので，分散 $\langle N_\varepsilon^2 \rangle - \langle N_\varepsilon \rangle^2$ は次式になります。

$$
\begin{aligned}
\langle N_\varepsilon^2 \rangle - \langle N_\varepsilon \rangle^2 &= \frac{Nxy}{(x + y)^2} \\
&= \frac{2N e^{-\beta\varepsilon}}{\bigl(2 + e^{-\beta\varepsilon}\bigr)^2} \\
&= \frac{2N e^{\beta\varepsilon}}{\bigl(2e^{\beta\varepsilon} + 1\bigr)^2}
\end{aligned}
$$

したがって，分散は次式となります。

$$
\finalanswer{\langle N_\varepsilon^2 \rangle - \langle N_\varepsilon \rangle^2 = \frac{2N e^{\varepsilon/(k_{\mathrm{B}}T)}}{\bigl(2e^{\varepsilon/(k_{\mathrm{B}}T)} + 1\bigr)^2}}
$$

### (6)

設問4で求めた $\langle N_\varepsilon \rangle = \dfrac{N}{2e^{\beta\varepsilon} + 1}$ を $\varepsilon$ で偏微分します。

$$
\begin{aligned}
\chi &= \frac{\partial}{\partial\varepsilon}\left(\frac{N}{2e^{\beta\varepsilon} + 1}\right) \\
&= -\frac{N \cdot 2\beta e^{\beta\varepsilon}}{\bigl(2e^{\beta\varepsilon} + 1\bigr)^2} \\
&= -\frac{2N e^{\beta\varepsilon}}{k_{\mathrm{B}}T\bigl(2e^{\beta\varepsilon} + 1\bigr)^2}
\end{aligned}
$$

これを設問5の分散 $\langle N_\varepsilon^2 \rangle - \langle N_\varepsilon \rangle^2 = \dfrac{2N e^{\beta\varepsilon}}{(2e^{\beta\varepsilon} + 1)^2}$ と比較すると，次の関係が得られます。

$$
\chi = -\frac{1}{k_{\mathrm{B}}T}\bigl(\langle N_\varepsilon^2 \rangle - \langle N_\varepsilon \rangle^2\bigr)
$$

したがって，応答関数 $\chi$ と分散を用いた表式は次式となります。

$$
\finalanswer{\begin{aligned}
\chi&=-\frac{2Ne^{\varepsilon/(k_{\mathrm B}T)}}{k_{\mathrm B}T\bigl(2e^{\varepsilon/(k_{\mathrm B}T)}+1\bigr)^2}\\
&=-\frac{1}{k_{\mathrm B}T}\bigl(\langle N_\varepsilon^2\rangle-\langle N_\varepsilon\rangle^2\bigr)
\end{aligned}}
$$
