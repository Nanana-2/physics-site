---
title: 東大理物 平成19年度 物理学 第2問：常磁性スピン系とスピン対の磁化率
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成19年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成19年度 物理学 第2問：常磁性スピン系とスピン対の磁化率

## 問題

スピン $1/2$ の粒子が大きさ $H$ の磁場の下におかれると，ゼーマン効果によって，そのエネルギー準位は $-\mu H, +\mu H$（$\mu$ は正の定数）に分裂する。このような粒子 $N$ 個が大きさ $H$ の一様な磁場の下におかれ，温度 $T$ に保たれている系を考え，これをカノニカル分布によって取り扱う。最初は粒子間に相互作用がないとして，以下の設問に答えよ。ただし，$\beta = (k_{\mathrm{B}}T)^{-1}$（$k_{\mathrm{B}}$ はボルツマン定数）を用いてもよい。

(1) この系の自由エネルギー $F$ を求めよ。

(2) 磁場に平行方向の磁化 $M$ と，$H \to 0$ での磁化率 $\chi$ を求めよ。ただし磁化は $M = -\partial F/\partial H$，磁化率は $\chi = \partial M/\partial H$ で定義される。

次に，$N$ 個の粒子が2個ずつ $N/2$ 組の対になり，対を組んだ粒子間にはそれぞれのスピンの内積に比例する相互作用が働く場合を考える。異なる対に含まれる粒子間には相互作用が働かないとする。磁場の方向を $z$ 方向とすれば，一つの対のハミルトニアンは，対に含まれる2粒子のスピン演算子 $\boldsymbol{s}_1, \boldsymbol{s}_2$ とその $z$ 成分 $s_{1z}, s_{2z}$ を用いて，

$$
\mathcal{H} = V\boldsymbol{s}_1\cdot\boldsymbol{s}_2 - 2\mu(s_{1z} + s_{2z})H
$$

と書くことができる。$V$ は相互作用の大きさと符号を表すパラメータである。このとき以下の設問に答えよ。

(3) ハミルトニアン $\mathcal{H}$ のエネルギー固有値を求めよ。

(4) $N/2$ 組の対からなる系全体の自由エネルギー $F$ を求めよ。

(5) 磁場に平行方向の磁化 $M$ と，$H \to 0$ での磁化率 $\chi$ を求めよ。

(6) 設問5で求めた磁化率の低温極限（$k_{\mathrm{B}}T/|V| \ll 1$）での振舞いを調べ，それが $V$ の符号によって定性的に異なる理由を簡単に説明せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成19年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
互いに相互作用しない粒子や対からなる系では，全体の分配関数が1単位ごとの分配関数の積になります。そのため，まず1粒子または1対のエネルギー固有値を求めれば，系全体の自由エネルギーと磁化を微分で計算することができます。

2粒子のスピン内積 $\boldsymbol{s}_1\cdot\boldsymbol{s}_2$ は，全スピン $\boldsymbol{S} = \boldsymbol{s}_1 + \boldsymbol{s}_2$ の2乗で表すことができます。$\boldsymbol{S}^2$ と $S_z$ は可換なので，全スピンの量子数 $S$ と $S_z$ の同時固有状態をとれば，相互作用項とゼーマン項を同時に対角化することができます。
</div>

### (1)

1粒子のエネルギー準位は $-\mu H$ と $+\mu H$ の2つなので，1粒子の分配関数 $Z_1$ は次式になります。

$$
\begin{aligned}
Z_1 &= e^{\beta\mu H} + e^{-\beta\mu H} \\
&= 2\cosh(\beta\mu H)
\end{aligned}
$$

$N$ 個の粒子は互いに独立なので，系全体の分配関数 $Z$ は $Z = Z_1^N$ です。これよりヘルムホルツの自由エネルギー $F = -\dfrac{1}{\beta}\ln Z$ を計算します。

$$
\begin{aligned}
F &= -\frac{1}{\beta}\ln\bigl(Z_1^N\bigr) \\
&= -\frac{N}{\beta}\ln\bigl(2\cosh(\beta\mu H)\bigr)
\end{aligned}
$$

したがって，この系の自由エネルギーは次式となります。

$$
\finalanswer{F = -\frac{N}{\beta}\ln\bigl(2\cosh(\beta\mu H)\bigr)}
$$

### (2)

磁化 $M = -\dfrac{\partial F}{\partial H}$ を計算します。

$$
\begin{aligned}
M &= -\frac{\partial}{\partial H}\left(-\frac{N}{\beta}\ln\bigl(2\cosh(\beta\mu H)\bigr)\right) \\
&= \frac{N}{\beta}\cdot\frac{\beta\mu\sinh(\beta\mu H)}{\cosh(\beta\mu H)} \\
&= N\mu\tanh(\beta\mu H)
\end{aligned}
$$

次に磁化率 $\chi = \dfrac{\partial M}{\partial H}$ を求め，$H \to 0$ の極限をとります。

$$
\frac{\partial M}{\partial H} = \frac{N\beta\mu^2}{\cosh^2(\beta\mu H)}
$$

零磁場の極限をとり，$\chi$ と表します。

$$
\begin{aligned}
\chi &= \lim_{H \to 0}\frac{N\beta\mu^2}{\cosh^2(\beta\mu H)} \\
&= N\beta\mu^2 \\
&= \frac{N\mu^2}{k_{\mathrm{B}}T}
\end{aligned}
$$

したがって，磁化 $M$ と $H \to 0$ での磁化率 $\chi$ は次式となります。

$$
\finalanswer{\begin{aligned}
M&=N\mu\tanh(\beta\mu H),\\
\chi&=N\beta\mu^2\\
&=\frac{N\mu^2}{k_{\mathrm B}T}
\end{aligned}}
$$

### (3)

ゼーマン項 $-2\mu(s_{1z} + s_{2z})H$ が1粒子あたり $\mp\mu H$ のエネルギーを与えることから，ここでは $s_{1z}, s_{2z}$ の固有値を $\pm\dfrac{1}{2}$ とした無次元のスピン演算子を用います。このとき 

$$
\begin{aligned}
\boldsymbol{s}_1^2 &= \boldsymbol{s}_2^2 \\
&= \frac{1}{2}\left(\frac{1}{2} + 1\right) \\
&= \frac{3}{4}
\end{aligned}
$$

です。

全スピン演算子 $\boldsymbol{S} = \boldsymbol{s}_1 + \boldsymbol{s}_2$ を導入します。$\boldsymbol{S}^2 = \boldsymbol{s}_1^2 + \boldsymbol{s}_2^2 + 2\boldsymbol{s}_1\cdot\boldsymbol{s}_2$ より，内積 $\boldsymbol{s}_1\cdot\boldsymbol{s}_2$ を $\boldsymbol{S}^2$ で書き換えます。

$$
\begin{aligned}
\boldsymbol{s}_1\cdot\boldsymbol{s}_2 &= \frac{1}{2}\bigl(\boldsymbol{S}^2 - \boldsymbol{s}_1^2 - \boldsymbol{s}_2^2\bigr) \\
&= \frac{1}{2}\left(\boldsymbol{S}^2 - \frac{3}{2}\right)
\end{aligned}
$$

これをハミルトニアン $\mathcal{H}$ に代入します。

$$
\mathcal{H} = \frac{V}{2}\left(\boldsymbol{S}^2 - \frac{3}{2}\right) - 2\mu S_z H
$$

$\boldsymbol{S}^2$ と $S_z$ は可換であり，2つのスピン $1/2$ の合成スピンの量子数は $S = 0$ と $S = 1$ です。各状態 $|S, S_z\rangle$ に対する $\boldsymbol{S}^2$ の固有値は $S(S + 1)$ です。

まず $S = 0$，$S_z = 0$ の一重項状態では，$\boldsymbol{S}^2$ の固有値が $0$ です。

$$
\begin{aligned}
E_{0, 0} &= \frac{V}{2}\left(0 - \frac{3}{2}\right) - 0 \\
&= -\frac{3}{4}V
\end{aligned}
$$

次に $S = 1$，$S_z = +1, 0, -1$ の三重項状態では，$\boldsymbol{S}^2$ の固有値が $1(1 + 1) = 2$ です。

$$
\begin{aligned}
E_{1, S_z} &= \frac{V}{2}\left(2 - \frac{3}{2}\right) - 2\mu S_z H \\
&= \frac{1}{4}V - 2\mu S_z H
\end{aligned}
$$

したがって，ハミルトニアン $\mathcal{H}$ の4つのエネルギー固有値は次式となります。

$$
\finalanswer{-\frac{3}{4}V, \qquad \frac{1}{4}V - 2\mu H, \qquad \frac{1}{4}V, \qquad \frac{1}{4}V + 2\mu H}
$$

### (4)

設問3で求めた4つのエネルギー固有値から，1つの対の分配関数 $Z_{\mathrm{pair}}$ を計算します。

$$
\begin{aligned}
Z_{\mathrm{pair}} &= e^{\frac{3}{4}\beta V} + e^{-\frac{1}{4}\beta V + 2\beta\mu H} + e^{-\frac{1}{4}\beta V} + e^{-\frac{1}{4}\beta V - 2\beta\mu H} \\
&= e^{\frac{3}{4}\beta V} + e^{-\frac{1}{4}\beta V}\bigl(1 + 2\cosh(2\beta\mu H)\bigr) \\
&= e^{-\frac{1}{4}\beta V}\bigl(e^{\beta V} + 1 + 2\cosh(2\beta\mu H)\bigr)
\end{aligned}
$$

異なる対の間には相互作用がないため，$N/2$ 組の対からなる系全体の分配関数は $Z = Z_{\mathrm{pair}}^{N/2}$ です。よって自由エネルギー $F = -\dfrac{1}{\beta}\ln Z$ は次式になります。

$$
\begin{aligned}
F &= -\frac{N}{2\beta}\ln Z_{\mathrm{pair}} \\
&= -\frac{N}{2\beta}\left(-\frac{1}{4}\beta V + \ln\bigl(e^{\beta V} + 1 + 2\cosh(2\beta\mu H)\bigr)\right) \\
&= \frac{NV}{8} - \frac{N}{2\beta}\ln\bigl(e^{\beta V} + 1 + 2\cosh(2\beta\mu H)\bigr)
\end{aligned}
$$

したがって，系全体の自由エネルギーは次式となります。

$$
\finalanswer{F = \frac{NV}{8} - \frac{N}{2\beta}\ln\bigl(e^{\beta V} + 1 + 2\cosh(2\beta\mu H)\bigr)}
$$

### (5)

設問4の自由エネルギーを $H$ で偏微分して磁化 $M = -\dfrac{\partial F}{\partial H}$ を求めます。

$$
\begin{aligned}
M &= \frac{N}{2\beta}\cdot\frac{4\beta\mu\sinh(2\beta\mu H)}{e^{\beta V} + 1 + 2\cosh(2\beta\mu H)} \\
&= \frac{2N\mu\sinh(2\beta\mu H)}{e^{\beta V} + 1 + 2\cosh(2\beta\mu H)}
\end{aligned}
$$

次に $H \to 0$ での磁化率 $\chi = \left.\dfrac{\partial M}{\partial H}\right|_{H \to 0}$ を計算します。$H \to 0$ のとき $\sinh(2\beta\mu H) \simeq 2\beta\mu H$，$\cosh(2\beta\mu H) \to 1$ なので，次のように求めることができます。

$$
\begin{aligned}
\chi &= \lim_{H \to 0}\frac{M}{H} \\
&= \lim_{H \to 0}\frac{2N\mu\cdot 2\beta\mu H}{\bigl(e^{\beta V} + 1 + 2\bigr)H} \\
&= \frac{4N\beta\mu^2}{e^{\beta V} + 3}
\end{aligned}
$$

したがって，磁化 $M$ と $H \to 0$ での磁化率 $\chi$ は次式となります。

$$
\finalanswer{\begin{aligned}
M&=\frac{2N\mu\sinh(2\beta\mu H)}{e^{\beta V}+1+2\cosh(2\beta\mu H)},\\
\chi&=\frac{4N\beta\mu^2}{e^{\beta V}+3}\\
&=\frac{4N\mu^2}{k_{\mathrm B}T\bigl(e^{V/(k_{\mathrm B}T)}+3\bigr)}
\end{aligned}}
$$

### (6)

低温極限 $k_{\mathrm{B}}T/|V| \ll 1$，すなわち $\beta|V| \gg 1$ における $\chi$ の振る舞いを $V$ の符号ごとに調べます。

$V > 0$ のとき，$\beta V \gg 1$ より $e^{\beta V} \gg 3$ となるため，分母の $3$ を無視することができます。

$$
\begin{aligned}
\chi &= \frac{4N\mu^2}{k_{\mathrm{B}}T\bigl(e^{V/(k_{\mathrm{B}}T)} + 3\bigr)} \\
&\simeq \frac{4N\mu^2}{k_{\mathrm{B}}T}e^{-V/(k_{\mathrm{B}}T)} \xrightarrow{T \to 0} 0
\end{aligned}
$$

$V < 0$ のとき，$\beta V = -\beta|V| \ll -1$ より $e^{\beta V} = e^{-\beta|V|} \ll 1$ となるため，分母の $e^{\beta V}$ を無視することができます。

$$
\begin{aligned}
\chi &= \frac{4N\mu^2}{k_{\mathrm{B}}T\bigl(e^{-|V|/(k_{\mathrm{B}}T)} + 3\bigr)} \\
&\simeq \frac{4N\mu^2}{3k_{\mathrm{B}}T} \xrightarrow{T \to 0} +\infty
\end{aligned}
$$

低温の磁化率をまとめると，次のようになります。

$$
\finalanswer{\chi\simeq\begin{cases}
\frac{4N\mu^2}{k_{\mathrm B}T}e^{-V/(k_{\mathrm B}T)} &(V>0),\\
\frac{4N\mu^2}{3k_{\mathrm B}T} &(V<0)
\end{cases}}
$$

$V>0$ では基底状態は全スピン $S=0$ の非磁性な一重項です。磁場に応答する三重項とのエネルギー差は $V$ なので，熱励起が $e^{-V/(k_{\mathrm B}T)}$ で抑えられ，磁化率は $0$ に近づきます。

$V<0$ では基底状態は全スピン $S=1$ の三重項です。低温の各対は大きさ $S=1$ の自由スピンとして振る舞い，磁化率は $1/T$ に比例して発散します。