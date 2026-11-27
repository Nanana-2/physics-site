---
title: 東大理物 平成10年度 物理学 第3問：反強磁性ハイゼンベルク2スピン系・4スピン系の固有状態と帯磁率
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成10年度 物理学 第3問：反強磁性ハイゼンベルク2スピン系・4スピン系の固有状態と帯磁率

## 問題

(1) 大きさ $\dfrac{1}{2}$ のスピン2個が，次のハミルトニアンで相互作用している系を考える。

$$
\mathcal{H} = J\vec{S}_1\cdot\vec{S}_2
$$

以下 $J > 0$ とする。固有値と固有状態を求めよ。

<figure class="problem-figure" markdown>
![反強磁性相互作用する2スピン系](../../assets/figures/pastexam-todai-ributsu/H10_butsuri_3-p1-light.svg#only-light){ loading=lazy }
![反強磁性相互作用する2スピン系](../../assets/figures/pastexam-todai-ributsu/H10_butsuri_3-p1-dark.svg#only-dark){ loading=lazy }
</figure>

(2) このスピン系に $z$ 方向の磁場 $H$ がかかるとハミルトニアンは

$$
\mathcal{H} = J\vec{S}_1\cdot\vec{S}_2 - g\mu_{\mathrm{B}}H\,(S_1^z + S_2^z)
$$

と書くことができる。ここで $\mu_{\mathrm{B}}$ はボーア磁子，$g$ は電子の $g$-因子で $g = 2$ である。この系が温度 $T$ の熱浴と接して熱平衡にあるとき，その分配関数を計算せよ。

(3) 温度 $T$ における磁気モーメントの平均値

$$
M = g\mu_{\mathrm{B}}\langle S_1^z + S_2^z \rangle
$$

を計算し，磁化率 $\chi = \lim_{H \to 0} M/H$ の温度依存性の様子を図示せよ。特に，$k_{\mathrm{B}}T \gg J$，$k_{\mathrm{B}}T \ll J$ での漸近形を求めよ。

(4) 正方形の頂点に4個の大きさ $\dfrac{1}{2}$ のスピンがあって，隣り合ったスピンと相互作用している。このときのハミルトニアンが

$$
\mathcal{H} = J(\vec{S}_1 + \vec{S}_3)\cdot(\vec{S}_2 + \vec{S}_4)
$$

と書けることに注目して，すべての固有状態のスピン量子数とエネルギー固有値を求めよ。

<figure class="problem-figure" markdown>
![正方形の頂点に配置された4スピン系](../../assets/figures/pastexam-todai-ributsu/H10_butsuri_3-p2-light.svg#only-light){ loading=lazy }
![正方形の頂点に配置された4スピン系](../../assets/figures/pastexam-todai-ributsu/H10_butsuri_3-p2-dark.svg#only-dark){ loading=lazy }
</figure>

(5) 上の4個のスピン系の低温での磁化率の漸近形，高温での磁化率の漸近形はどうなるか。理由をつけて答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
反強磁性ハイゼンベルク模型の有限スピン系を，合成スピンの角運動量合成則によって厳密対角化します。前半の2スピン系では1重項基底状態と3重項励起状態のエネルギーギャップ $J$ が低温での指数関数的抑制を生み，高温では独立スピンのキュリーの法則に近づくことから，$\chi(T)$ が有限温度で極大をもつことを示します。

後半の正方形4スピン系では対角頂点のスピン和 $\vec{S}_A = \vec{S}_1 + \vec{S}_3$，$\vec{S}_B = \vec{S}_2 + \vec{S}_4$ を導入して全16状態を分類し，低温と高温の磁化率の漸近形をエネルギー準位構造から導出します。
</div>

### (1)

問題文の表記に従い $\hbar = 1$ の無次元スピン演算子を用いて，合成スピン $\vec{S} = \vec{S}_1 + \vec{S}_2$ を導入します。$\vec{S}^2 = \vec{S}_1^2 + \vec{S}_2^2 + 2\vec{S}_1\cdot\vec{S}_2$ より，ハミルトニアンは次のように書き換えられます。

$$
\mathcal{H} = \frac{J}{2}\left(\vec{S}^2 - \vec{S}_1^2 - \vec{S}_2^2\right)
$$

各スピンの大きさは $S_1 = \dfrac{1}{2}$，$S_2 = \dfrac{1}{2}$ なので，$\vec{S}_1^2$ と $\vec{S}_2^2$ の固有値はともに $\dfrac{3}{4}$ です。合成スピン量子数 $S$ は $S = 0$ の1重項と $S = 1$ の3重項の2通りをとり，$\vec{S}^2$ の固有値は $S(S + 1)$ です。

各スピンの $z$ 成分固有状態を $|\uparrow\rangle$（$S^z = +\dfrac{1}{2}$），$|\downarrow\rangle$（$S^z = -\dfrac{1}{2}$）として，固有値 $E_S$ と対応する固有状態 $|S, S^z\rangle$ を求めます。

まず $S = 0$ のスピン1重項基底状態では，エネルギー固有値は

$$
\begin{aligned}
E_0 &= \frac{J}{2}\left(0 - \frac{3}{4} - \frac{3}{4}\right) \\
&= -\frac{3}{4}J
\end{aligned}
$$

であり，固有状態は次の1状態です。

$$
|0, 0\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\bigr)
$$

次に $S = 1$ のスピン3重項励起状態では，エネルギー固有値は

$$
\begin{aligned}
E_1 &= \frac{J}{2}\left(2 - \frac{3}{4} - \frac{3}{4}\right) \\
&= +\frac{1}{4}J
\end{aligned}
$$

であり，3重に縮退した固有状態は次の3通りです。

$$
\begin{aligned}
|1, +1\rangle &= |\uparrow\uparrow\rangle \\
|1, 0\rangle &= \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle\bigr) \\
|1, -1\rangle &= |\downarrow\downarrow\rangle
\end{aligned}
$$

$$
\finalanswer{\begin{aligned}
E_0 &= -\frac{3}{4}J, & |0, 0\rangle &= \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\bigr) \\
E_1 &= +\frac{1}{4}J, & |1, \pm 1\rangle &= |\uparrow\uparrow\rangle,\,|\downarrow\downarrow\rangle,\quad |1, 0\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle\bigr)
\end{aligned}}
$$

### (2)

磁場中のハミルトニアンは $\mathcal{H} = J\vec{S}_1\cdot\vec{S}_2 - 2\mu_{\mathrm{B}}H S^z$（$g = 2$，$S^z = S_1^z + S_2^z$）です。$\vec{S}_1\cdot\vec{S}_2$ と $S^z$ は互いに可換であるため，(1) で求めた4つの固有状態 $|S, S^z\rangle$ がそのまま磁場中の固有状態になります。各状態のエネルギー固有値は次の通りです。

- $|0, 0\rangle$：$E = -\dfrac{3}{4}J$
- $|1, +1\rangle$：$E = \dfrac{1}{4}J - 2\mu_{\mathrm{B}}H$
- $|1, 0\rangle$：$E = \dfrac{1}{4}J$
- $|1, -1\rangle$：$E = \dfrac{1}{4}J + 2\mu_{\mathrm{B}}H$

逆温度 $\beta = \dfrac{1}{k_{\mathrm{B}}T}$ を用いて分配関数 $Z = \operatorname{Tr}(e^{-\beta\mathcal{H}})$ を計算します。

$$
\begin{aligned}
Z &= e^{3\beta J/4} + e^{-\beta J/4 + 2\beta\mu_{\mathrm{B}}H} + e^{-\beta J/4} + e^{-\beta J/4 - 2\beta\mu_{\mathrm{B}}H} \\
&= e^{3\beta J/4} + e^{-\beta J/4}\bigl(1 + 2\cosh(2\beta\mu_{\mathrm{B}}H)\bigr)
\end{aligned}
$$

$$
\finalanswer{Z = e^{3J/(4k_{\mathrm{B}}T)} + e^{-J/(4k_{\mathrm{B}}T)}\left\{1 + 2\cosh\left(\frac{2\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)\right\}}
$$

### (3)

磁気モーメントの平均値 $M$ は分配関数 $Z$ から $M = \dfrac{1}{\beta}\dfrac{\partial\ln Z}{\partial H}$ によって計算します。

$$
\begin{aligned}
M &= \frac{1}{\beta Z}\frac{\partial Z}{\partial H} \\
&= \frac{4\mu_{\mathrm{B}} e^{-\beta J/4}\sinh(2\beta\mu_{\mathrm{B}}H)}{e^{3\beta J/4} + e^{-\beta J/4}\bigl(1 + 2\cosh(2\beta\mu_{\mathrm{B}}H)\bigr)} \\
&= \frac{4\mu_{\mathrm{B}}\sinh(2\beta\mu_{\mathrm{B}}H)}{e^{\beta J} + 1 + 2\cosh(2\beta\mu_{\mathrm{B}}H)}
\end{aligned}
$$

次に磁化率 $\chi = \lim_{H \to 0}\dfrac{M}{H}$ を求めます。$H \to 0$ で $\sinh(2\beta\mu_{\mathrm{B}}H) \approx 2\beta\mu_{\mathrm{B}}H$，$\cosh(2\beta\mu_{\mathrm{B}}H) \to 1$ となるため，次式が得られます。

$$
\begin{aligned}
\chi &= \frac{8\beta\mu_{\mathrm{B}}^2}{e^{\beta J} + 3} \\
&= \frac{8\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T\left(e^{J/(k_{\mathrm{B}}T)} + 3\right)}
\end{aligned}
$$

高温極限と低温極限での漸近形を評価します。

まず高温極限 $k_{\mathrm{B}}T \gg J$ では $e^{J/(k_{\mathrm{B}}T)} \to 1$ より，独立な2個のスピン $\dfrac{1}{2}$ のキュリーの法則に一致します。

$$
\chi \simeq \frac{2\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}
$$

次に低温極限 $k_{\mathrm{B}}T \ll J$ では $e^{J/(k_{\mathrm{B}}T)} \gg 3$ より，1重項と3重項の間のスピンギャップ $J$ を反映した熱活性化型の振る舞いを示し，$T \to 0$ で指数関数的に $0$ へ減衰します。

$$
\chi \simeq \frac{8\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}e^{-J/(k_{\mathrm{B}}T)}
$$

$\chi(T)$ は $T \to 0$ と $T \to \infty$ の双方で $0$ に近づく正の関数であり，途中の有限温度で1つの極大をもちます。$\dfrac{\mathrm{d}\chi}{\mathrm{d}T} = 0$ を解くと $(x - 1)e^x = 3$（$x = \dfrac{J}{k_{\mathrm{B}}T}$）より $x \approx 1.60$，すなわち $k_{\mathrm{B}}T/J \approx 0.624$ で最大値 $\chi_{\max} \approx 1.61\dfrac{\mu_{\mathrm{B}}^2}{J}$ をとります。温度依存性のグラフは次の通りです。

![反強磁性2スピン系の磁化率の温度依存性](../../assets/figures/pastexam-todai-ributsu/H10_butsuri_3-s-light.svg#only-light){ loading=lazy }
![反強磁性2スピン系の磁化率の温度依存性](../../assets/figures/pastexam-todai-ributsu/H10_butsuri_3-s-dark.svg#only-dark){ loading=lazy }

$$
\finalanswer{M = \frac{4\mu_{\mathrm{B}}\sinh\left(\dfrac{2\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)}{e^{J/(k_{\mathrm{B}}T)} + 1 + 2\cosh\left(\dfrac{2\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)},\qquad \chi = \frac{8\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T\left(e^{J/(k_{\mathrm{B}}T)} + 3\right)},\qquad \chi \simeq \begin{cases}\dfrac{2\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T} & (k_{\mathrm{B}}T \gg J) \\[10pt] \dfrac{8\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}e^{-J/(k_{\mathrm{B}}T)} & (k_{\mathrm{B}}T \ll J)\end{cases}}
$$

### (4)

対角に位置するスピンの和 $\vec{S}_A = \vec{S}_1 + \vec{S}_3$，$\vec{S}_B = \vec{S}_2 + \vec{S}_4$，および系全体の合成スピン $\vec{S} = \vec{S}_A + \vec{S}_B$ を導入します。ハミルトニアンは次のように表されます。

$$
\begin{aligned}
\mathcal{H} &= J\vec{S}_A\cdot\vec{S}_B \\
&= \frac{J}{2}\left(\vec{S}^2 - \vec{S}_A^2 - \vec{S}_B^2\right)
\end{aligned}
$$

$\vec{S}^2$，$\vec{S}_A^2$，$\vec{S}_B^2$，$S^z$ は互いに可換であるため，固有状態は量子数 $(S_A, S_B, S, S^z)$ で完全に指定されます。$S_A$ と $S_B$ はそれぞれ大きさ $\dfrac{1}{2}$ のスピン2個の合成なので $0$ または $1$ をとり，合成スピン $S$ は $|S_A - S_B| \le S \le S_A + S_B$ を満たします。エネルギー固有値は

$$
E(S_A, S_B, S) = \frac{J}{2}\bigl(S(S + 1) - S_A(S_A + 1) - S_B(S_B + 1)\bigr)
$$

です。すべての組み合わせ（合計 $2^4 = 16$ 状態）を次の表にまとめます。

| $S_A$ | $S_B$ | 全スピン $S$ | $S^z$ の状態数 $2S + 1$ | エネルギー固有値 $E$ |
| :---: | :---: | :---: | :---: | :---: |
| $1$ | $1$ | $0$ | $1$ | $-2J$ |
| $1$ | $1$ | $1$ | $3$ | $-J$ |
| $0$ | $0$ | $0$ | $1$ | $0$ |
| $1$ | $0$ | $1$ | $3$ | $0$ |
| $0$ | $1$ | $1$ | $3$ | $0$ |
| $1$ | $1$ | $2$ | $5$ | $+J$ |

状態数の合計は $1 + 3 + 1 + 3 + 3 + 5 = 16$ となり，すべての固有状態が尽くされています。

$$
\finalanswer{\begin{aligned}
(S_A, S_B, S) &= (1, 1, 0): & E &= -2J \\
(S_A, S_B, S) &= (1, 1, 1): & E &= -J \\
(S_A, S_B, S) &= (0, 0, 0),\, (1, 0, 1),\, (0, 1, 1): & E &= 0 \\
(S_A, S_B, S) &= (1, 1, 2): & E &= +J
\end{aligned}}
$$

### (5)

4個のスピン系に $z$ 方向の磁場 $H$ を印加したときのハミルトニアンは $\mathcal{H} = J\vec{S}_A\cdot\vec{S}_B - 2\mu_{\mathrm{B}}H S^z$ であり，分配関数 $Z_4$ は (4) の結果を用いて厳密に表されます。

$$
Z_4 = e^{2\beta J} + e^{\beta J}\bigl(1 + 2\cosh(2\beta\mu_{\mathrm{B}}H)\bigr) + 1 + 2\bigl(1 + 2\cosh(2\beta\mu_{\mathrm{B}}H)\bigr) + e^{-\beta J}\bigl(1 + 2\cosh(2\beta\mu_{\mathrm{B}}H) + 2\cosh(4\beta\mu_{\mathrm{B}}H)\bigr)
$$

一般のスピン系において，ゼロ磁場磁化率 $\chi_4$ は $H = 0$ での熱平均 $\langle (S^z)^2 \rangle_0$ を用いて

$$
\chi_4 = \frac{(2\mu_{\mathrm{B}})^2}{k_{\mathrm{B}}T}\langle (S^z)^2 \rangle_0
$$

と表されます。各全スピン多重項 $S$ の $(S^z)^2$ の和は $\sum_{m=-S}^{S} m^2 = \dfrac{1}{3}S(S + 1)(2S + 1)$ なので，$S = 0$ で $0$，$S = 1$ で $2$，$S = 2$ で $10$ となります。したがって $\chi_4$ の厳密表式は次の通りです。

$$
\chi_4 = \frac{4\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}\cdot\frac{2e^{\beta J} + 4 + 10e^{-\beta J}}{e^{2\beta J} + 3e^{\beta J} + 7 + 5e^{-\beta J}}
$$

これより低温極限および高温極限の漸近形を求めます。

まず低温極限 $k_{\mathrm{B}}T \ll J$ を考えます。分母では非磁性の1重項基底状態（$E = -2J$，$S = 0$）のボルツマン因子 $e^{2\beta J}$ が他の項に比べて圧倒的に大きくなります。一方，分子では基底状態からのエネルギーギャップが最小の $\Delta = J$ である第1励起状態（$E = -J$，$S = 1$ の3重項）の寄与 $2e^{\beta J}$ が他の励起準位に比べて圧倒的に大きく，より高い準位（$E = 0, +J$）はさらに指数関数的に抑制されます。したがって漸近形は2スピン系と同じ形になります。

$$
\begin{aligned}
\chi_4 &\simeq \frac{4\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}\cdot\frac{2e^{\beta J}}{e^{2\beta J}} \\
&= \frac{8\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}e^{-J/(k_{\mathrm{B}}T)}
\end{aligned}
$$

次に高温極限 $k_{\mathrm{B}}T \gg J$ を考えます。熱エネルギー $k_{\mathrm{B}}T$ が相互作用 $J$ に比べて十分大きいため，4個の大きさ $\dfrac{1}{2}$ のスピンが相互作用を失って互いに独立な常磁性スピンとして振る舞います。上の厳密式で $\beta J \to 0$ とすると，分母は $1 + 3 + 7 + 5 = 16$，分子の和は $2 + 4 + 10 = 16$ となり，1個の自由スピン $\dfrac{1}{2}$ のキュリー磁化率 $\dfrac{\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}$ の4倍に一致します。

$$
\begin{aligned}
\chi_4 &\simeq \frac{4\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}\cdot\frac{16}{16} \\
&= \frac{4\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}
\end{aligned}
$$

$$
\finalanswer{\chi_4 \simeq \begin{cases}\dfrac{8\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}e^{-J/(k_{\mathrm{B}}T)} & (k_{\mathrm{B}}T \ll J) \\[10pt] \dfrac{4\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T} & (k_{\mathrm{B}}T \gg J)\end{cases}}
$$
