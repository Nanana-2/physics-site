---
title: 東大理物 平成15年度 数学 第1問：外積による線形微分方程式と実直交変換
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成15年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成15年度 数学 第1問：外積による線形微分方程式と実直交変換

## 問題

定数ベクトル $\vec{v} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$ を用いた微分方程式

$$
\frac{\mathrm{d}}{\mathrm{d}t}\vec{x} = \vec{v}\times\vec{x}
$$

を考える。
{: .problem-lead }

(1) 上の方程式を行列 $A$ を用いて

$$
\frac{\mathrm{d}\vec{x}}{\mathrm{d}t} = A\cdot\vec{x}
$$

という形に書き換える。行列 $A$ を求めよ。

(2) 次の性質を持つ正規直交基底 $\vec{e}_i$（$i = 1, 2, 3$）（$\vec{e}_i\cdot\vec{e}_j = \delta_{i, j}$）と係数 $\lambda$（$\lambda > 0$）を求めよ。

$$
\vec{v}\times\vec{e}_1 = \lambda\vec{e}_2, \qquad \vec{v}\times\vec{e}_2 = -\lambda\vec{e}_1, \qquad \vec{v}\times\vec{e}_3 = 0
$$

ただし $\vec{e}_1$ の第1成分は $0$ とする。

(3) 上で得られた結果を用いると，行列 $A$ は実直交行列 $U$ を用いて

$$
A = U\begin{pmatrix} 0 & -\lambda & 0 \\ \lambda & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} U^t, \qquad U U^t = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

とかけることを示せ（ただし $U^t$ は $U$ の転置行列）。また $U$ を求めよ。

(4) $\vec{x}$ を基底 $\vec{e}_i$ を用いて

$$
\vec{x} = \sum_{i=1}^{3} q_i(t)\vec{e}_i
$$

と展開する。係数 $q_i(t)$ に対する微分方程式を書き下し，その一般解を求めよ。また解の振る舞いを定性的に論じよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成15年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
外積 $\vec{v}\times\vec{x}$ を成分ごとに展開すると，反対称行列 $A$ による線形写像として表すことができます。

ベクトル $\vec{v}$ の方向を第3基底 $\vec{e}_3$ にとり，$\vec{v}$ に直交する平面内で残りの正規直交基底 $\vec{e}_1, \vec{e}_2$ を選ぶことで，$A$ は $2\times 2$ の回転生成ブロックと $0$ ブロックに標準化されます。この基底で微分方程式を成分分解すると，連立方程式は単振動と定数解に分かれ，解の幾何学的な運動が直接わかります。
</div>

### (1)

$\vec{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}$ とおき，$\vec{v} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$ との外積 $\vec{v}\times\vec{x}$ を成分ごとに計算します。

$$
\begin{aligned}
\vec{v}\times\vec{x} &= \begin{pmatrix} 1\cdot x_3 - (-1)\cdot x_2 \\ (-1)\cdot x_1 - 2\cdot x_3 \\ 2\cdot x_2 - 1\cdot x_1 \end{pmatrix} \\
&= \begin{pmatrix} x_2 + x_3 \\ -x_1 - 2x_3 \\ -x_1 + 2x_2 \end{pmatrix} \\
&= \begin{pmatrix} 0 & 1 & 1 \\ -1 & 0 & -2 \\ -1 & 2 & 0 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}
\end{aligned}
$$

したがって，行列 $A$ は次式となります。

$$
\finalanswer{A = \begin{pmatrix} 0 & 1 & 1 \\ -1 & 0 & -2 \\ -1 & 2 & 0 \end{pmatrix}}
$$

### (2)

まず $\vec{v}\times\vec{e}_3 = \vec{0}$ より，$\vec{e}_3$ は $\vec{v}$ に平行な単位ベクトルです。$|\vec{v}| = \sqrt{6}$ なので，$\vec{e}_3$ は次式になります。

$$
\vec{e}_3 = \pm\frac{1}{\sqrt{6}}\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}
$$

次に $\vec{e}_1$ は $\vec{e}_3$ すなわち $\vec{v}$ に直交し，第1成分が $0$ です。$\vec{e}_1 = \begin{pmatrix} 0 \\ a \\ b \end{pmatrix}$ とおいて $\vec{v}\cdot\vec{e}_1 = 0$ を立てます。

$$
2\cdot 0 + 1\cdot a + (-1)\cdot b = 0
$$

よって $a = b$ であり，$|\vec{e}_1| = 1$ より $a^2 + b^2 = 1$，すなわち $a = \pm\dfrac{1}{\sqrt{2}}$ です。全体の符号を反転しても条件を満たすため，ここでは正の符号を選びます。

$$
\vec{e}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}
$$

この $\vec{e}_1$ に対して $\vec{v}\times\vec{e}_1$ を計算します。

$$
\begin{aligned}
\vec{v}\times\vec{e}_1 &= \frac{1}{\sqrt{2}}\begin{pmatrix} 1\cdot 1 - (-1)\cdot 1 \\ (-1)\cdot 0 - 2\cdot 1 \\ 2\cdot 1 - 1\cdot 0 \end{pmatrix} \\
&= \frac{1}{\sqrt{2}}\begin{pmatrix} 2 \\ -2 \\ 2 \end{pmatrix} \\
&= \sqrt{2}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}
\end{aligned}
$$

$\lambda > 0$ と $|\vec{e}_2| = 1$ より，$\lambda = |\vec{v}\times\vec{e}_1|$ は $\sqrt{2}\cdot\sqrt{3} = \sqrt{6}$ であり，$\vec{e}_2 = \dfrac{1}{\lambda}(\vec{v}\times\vec{e}_1)$ は次式になります。

$$
\vec{e}_2 = \frac{1}{\sqrt{3}}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}
$$

念のため $\vec{v}\times\vec{e}_2$ を計算して $-\lambda\vec{e}_1$ になることを確かめます。

$$
\begin{aligned}
\vec{v}\times\vec{e}_2 &= \frac{1}{\sqrt{3}}\begin{pmatrix} 1\cdot 1 - (-1)\cdot(-1) \\ (-1)\cdot 1 - 2\cdot 1 \\ 2\cdot(-1) - 1\cdot 1 \end{pmatrix} \\
&= \frac{1}{\sqrt{3}}\begin{pmatrix} 0 \\ -3 \\ -3 \end{pmatrix} \\
&= -\sqrt{6}\cdot\frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \\
&= -\lambda\vec{e}_1
\end{aligned}
$$

また3つのベクトルは互いに内積が $0$ であり正規直交基底をなします。なお，$\vec{e}_1$ と $\vec{e}_2$ の組の符号を同時に反転したもの，および $\vec{e}_3$ の符号を反転したものも条件を満たします。右手系となる選び方を代表として書くと次式となります。

$$
\finalanswer{\lambda = \sqrt{6}, \quad \vec{e}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \quad \vec{e}_2 = \frac{1}{\sqrt{3}}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad \vec{e}_3 = \frac{1}{\sqrt{6}}\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}}
$$

### (3)

設問 (2) で求めた3つの列ベクトル $\vec{e}_1, \vec{e}_2, \vec{e}_3$ を並べた $3\times 3$ 実行列を $U = (\vec{e}_1, \vec{e}_2, \vec{e}_3)$ とおきます。$\{\vec{e}_i\}$ は正規直交基底なので，$U^t U$ の $(i, j)$ 成分は $\vec{e}_i\cdot\vec{e}_j = \delta_{i, j}$ となり，$U^t U = I$ です。正方行列なので $U^t = U^{-1}$ であり，$U U^t = I$ を満たす実直交行列です。

次に行列積 $AU$ を列ごとに計算し，設問 (2) の関係 $A\vec{e}_1 = \lambda\vec{e}_2$，$A\vec{e}_2 = -\lambda\vec{e}_1$，$A\vec{e}_3 = \vec{0}$ を代入します。

$$
\begin{aligned}
AU &= (A\vec{e}_1,\ A\vec{e}_2,\ A\vec{e}_3) \\
&= (\lambda\vec{e}_2,\ -\lambda\vec{e}_1,\ \vec{0}) \\
&= (\vec{e}_1,\ \vec{e}_2,\ \vec{e}_3)\begin{pmatrix} 0 & -\lambda & 0 \\ \lambda & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \\
&= U\begin{pmatrix} 0 & -\lambda & 0 \\ \lambda & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
\end{aligned}
$$

両辺に右から $U^t$ を掛けて $U U^t = I$ を用いると，求める表現が得られます。

$$
A = U\begin{pmatrix} 0 & -\lambda & 0 \\ \lambda & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} U^t
$$

したがって，実直交行列 $U$ は次式となります。

$$
\finalanswer{U = \begin{pmatrix} 0 & \dfrac{1}{\sqrt{3}} & \dfrac{2}{\sqrt{6}} \\[8pt] \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{6}} \\[8pt] \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} \end{pmatrix}}
$$

### (4)

$\vec{x}(t) = \sum_{i=1}^{3} q_i(t)\vec{e}_i$ を微分方程式 $\dfrac{\mathrm{d}\vec{x}}{\mathrm{d}t} = \vec{v}\times\vec{x}$ に代入し，設問 (2) の関係を用います。

$$
\begin{aligned}
\frac{\mathrm{d}q_1}{\mathrm{d}t}\vec{e}_1 + \frac{\mathrm{d}q_2}{\mathrm{d}t}\vec{e}_2 + \frac{\mathrm{d}q_3}{\mathrm{d}t}\vec{e}_3 &= q_1(\vec{v}\times\vec{e}_1) + q_2(\vec{v}\times\vec{e}_2) + q_3(\vec{v}\times\vec{e}_3) \\
&= \lambda q_1\vec{e}_2 - \lambda q_2\vec{e}_1
\end{aligned}
$$

$\vec{e}_1, \vec{e}_2, \vec{e}_3$ は線形独立なので，各成分の係数を比較して $q_i(t)$ に対する微分方程式が得られます。

$$
\frac{\mathrm{d}q_1}{\mathrm{d}t} = -\sqrt{6}\,q_2, \qquad \frac{\mathrm{d}q_2}{\mathrm{d}t} = \sqrt{6}\,q_1, \qquad \frac{\mathrm{d}q_3}{\mathrm{d}t} = 0
$$

まず第3式より $q_3(t) = C_3$（$C_3$ は任意定数）です。第1式を時間 $t$ で微分して第2式を代入します。

$$
\begin{aligned}
\frac{\mathrm{d}^2 q_1}{\mathrm{d}t^2} &= -\lambda\frac{\mathrm{d}q_2}{\mathrm{d}t} \\
&= -\lambda^2 q_1
\end{aligned}
$$

これは角振動数 $\lambda = \sqrt{6}$ の単振動の方程式なので，任意定数 $C_1, C_2$ を用いて $q_1(t) = C_1\cos(\lambda t) - C_2\sin(\lambda t)$ と表すことができます。これを $q_2 = -\dfrac{1}{\lambda}\dfrac{\mathrm{d}q_1}{\mathrm{d}t}$ に代入します。

$$
\begin{aligned}
q_2(t) &= -\frac{1}{\lambda}\bigl(-\lambda C_1\sin(\lambda t) - \lambda C_2\cos(\lambda t)\bigr) \\
&= C_1\sin(\lambda t) + C_2\cos(\lambda t)
\end{aligned}
$$

$\lambda = \sqrt{6}$ を代入すると，微分方程式と一般解はそれぞれ次式となります。

$$
\finalanswer{\frac{\mathrm{d}q_1}{\mathrm{d}t} = -\sqrt{6}\,q_2, \qquad \frac{\mathrm{d}q_2}{\mathrm{d}t} = \sqrt{6}\,q_1, \qquad \frac{\mathrm{d}q_3}{\mathrm{d}t} = 0}
$$

$$
\finalanswer{q_1(t) = C_1\cos(\sqrt{6}\,t) - C_2\sin(\sqrt{6}\,t), \qquad q_2(t) = C_1\sin(\sqrt{6}\,t) + C_2\cos(\sqrt{6}\,t), \qquad q_3(t) = C_3}
$$

解の振る舞いは次の通りです。$\vec{e}_3$ 方向の成分 $q_3(t) = C_3$ は時間によらず一定であり，$\vec{v}$ に垂直な平面内の成分の2乗和 $q_1(t)^2 + q_2(t)^2 = C_1^2 + C_2^2$ も一定に保たれます。したがって，ベクトル $\vec{x}(t)$ は定数ベクトル $\vec{v}$ を回転軸として，軸に垂直な平面上で半径 $\sqrt{C_1^2 + C_2^2}$ の円を描きながら，角速度 $\sqrt{6}$ で一様に回転運動をします。
