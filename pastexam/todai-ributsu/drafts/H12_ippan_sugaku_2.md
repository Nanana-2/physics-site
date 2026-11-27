---
title: 東大理物 平成12年度 一般教育科目 数学 第2問：実対称行列の対角化とユニタリ不変量
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 一般教育科目 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成12年度 一般教育科目 数学 第2問：実対称行列の対角化とユニタリ不変量

## 問題

(1) 行列

$$
\mathbf{A} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{pmatrix}
$$

の固有値と固有ベクトルを全て求めよ。ただし，固有ベクトルは正規化せよ。

(2) 次の行列

$$
\mathbf{X} = \begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] 0 & 0 & 1 \end{pmatrix}
$$

により，設問 (1) の行列 $\mathbf{A}$ を変換して得られる行列 $\mathbf{B} = \mathbf{X}\mathbf{A}\mathbf{X}^\dagger$ を考える。ただし $\mathbf{X}^\dagger$ は $\mathbf{X}$ のエルミート共役行列である。行列 $\mathbf{B}$ の固有値，固有ベクトルを示せ。ただし，固有ベクトルは正規化せよ。

(3) エルミート行列 $\mathbf{A} = (a_{ij})$（$i, j = 1, \dots, n$）の固有値を $\alpha_i$（$i = 1, \dots, n$）とする。それらに関して次の2つの量，

$$
F = \sum_{i=1}^{n} |\alpha_i|^2, \qquad G = \sum_{i,j=1}^{n} |a_{ij}|^2
$$

を考える。設問 (1) の $\mathbf{A}$ に対して $F$ と $G$ を求めよ。

(4) 設問 (3) の $F$ と $G$ の関係を，一般のエルミート行列 $\mathbf{A}$ に対して述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 一般教育科目 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
固有方程式 $\det(\lambda \mathbf{I} - \mathbf{A}) = 0$ を解いて $\mathbf{A}$ の固有値と正規化固有ベクトルを求めます。

(2) の変換行列 $\mathbf{X}$ は $\mathbf{X}\mathbf{X}^\dagger = \mathbf{I}$ を満たすユニタリ行列なので，$\mathbf{B} = \mathbf{X}\mathbf{A}\mathbf{X}^\dagger$ を具体的に展開しなくても，固有値は $\mathbf{A}$ と等しく，正規化固有ベクトルは $\mathbf{A}$ の固有ベクトルに $\mathbf{X}$ を左から掛けたものになります。(4) ではエルミート行列のユニタリ対角化とトレースの巡回不変性を用いて $\operatorname{Tr}(\mathbf{A}^\dagger\mathbf{A})$ を2通りに計算し，$F$ と $G$ の関係を導きます。
</div>

### (1)

固有方程式 $\det(\lambda \mathbf{I} - \mathbf{A}) = 0$ を展開します。

$$
\begin{aligned}
\det(\lambda \mathbf{I} - \mathbf{A}) &= \begin{vmatrix} \lambda & -1 & 0 \\ -1 & \lambda - 1 & -1 \\ 0 & -1 & \lambda \end{vmatrix} \\
&= \lambda\bigl[\lambda(\lambda - 1) - 1\bigr] - (-1)(-\lambda) \\
&= \lambda(\lambda^2 - \lambda - 1) - \lambda \\
&= \lambda(\lambda^2 - \lambda - 2) \\
&= \lambda(\lambda - 2)(\lambda + 1)
\end{aligned}
$$

よって固有値は $\lambda_1 = 2$，$\lambda_2 = 0$，$\lambda_3 = -1$ です。それぞれの固有ベクトル $\mathbf{u} = (x, y, z)^{\mathrm{T}}$ を $(\lambda \mathbf{I} - \mathbf{A})\mathbf{u} = \mathbf{0}$ から求め，大きさ $1$ に正規化します。

$\lambda_1 = 2$ のとき，連立方程式は次になります。

$$
\begin{aligned}
2x - y &= 0 \\
-x + y - z &= 0 \\
-y + 2z &= 0
\end{aligned}
$$

$x = 1$ とおくと $y = 2$，$z = 1$ です。大きさは $\sqrt{1^2 + 2^2 + 1^2} = \sqrt{6}$ なので，正規化固有ベクトルは $\mathbf{u}_1 = \dfrac{1}{\sqrt{6}}\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$ です。

$\lambda_2 = 0$ のとき，連立方程式は次になります。

$$
\begin{aligned}
-y &= 0 \\
-x - y - z &= 0 \\
-y &= 0
\end{aligned}
$$

よって $y = 0$，$z = -x$ です。$x = 1$ とおくと $(1, 0, -1)^{\mathrm{T}}$ となり，大きさ $\sqrt{2}$ で割ると正規化固有ベクトルは $\mathbf{u}_2 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$ です。

$\lambda_3 = -1$ のとき，連立方程式は次になります。

$$
\begin{aligned}
-x - y &= 0 \\
-x - 2y - z &= 0 \\
-y - z &= 0
\end{aligned}
$$

よって $y = -x$，$z = x$ です。$x = 1$ とおくと $(1, -1, 1)^{\mathrm{T}}$ となり，大きさ $\sqrt{3}$ で割ると正規化固有ベクトルは $\mathbf{u}_3 = \dfrac{1}{\sqrt{3}}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$ です。

以上より，固有値と正規化固有ベクトルは次の通りです。なお，各固有ベクトルには絶対値 $1$ の位相因子，実ベクトルの場合は符号 $\pm 1$ の任意性があります。

$$
\finalanswer{\lambda_1 = 2:\ \mathbf{u}_1 = \frac{1}{\sqrt{6}}\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}, \qquad \lambda_2 = 0:\ \mathbf{u}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \qquad \lambda_3 = -1:\ \mathbf{u}_3 = \frac{1}{\sqrt{3}}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}}
$$

### (2)

行列 $\mathbf{X}$ は実対称行列であり，$\mathbf{X}^\dagger = \mathbf{X}$ です。積 $\mathbf{X}^\dagger\mathbf{X}$ を計算します。

$$
\begin{aligned}
\mathbf{X}^\dagger\mathbf{X} &= \begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] 0 & 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\
&= \mathbf{I}
\end{aligned}
$$

よって $\mathbf{X}$ はユニタリ行列です。(1) の固有値方程式 $\mathbf{A}\mathbf{u}_k = \lambda_k \mathbf{u}_k$ の左から $\mathbf{X}$ を掛け，$\mathbf{X}^\dagger\mathbf{X} = \mathbf{I}$ を挿入します。

$$
\begin{aligned}
\mathbf{X}\mathbf{A}\mathbf{u}_k &= \lambda_k \mathbf{X}\mathbf{u}_k \\
(\mathbf{X}\mathbf{A}\mathbf{X}^\dagger)(\mathbf{X}\mathbf{u}_k) &= \lambda_k (\mathbf{X}\mathbf{u}_k) \\
\mathbf{B}(\mathbf{X}\mathbf{u}_k) &= \lambda_k (\mathbf{X}\mathbf{u}_k)
\end{aligned}
$$

したがって，$\mathbf{B}$ の固有値は $\mathbf{A}$ と同じ $\lambda_1 = 2$，$\lambda_2 = 0$，$\lambda_3 = -1$ であり，対応する固有ベクトルは $\mathbf{v}_k = \mathbf{X}\mathbf{u}_k$ です。さらに $\mathbf{X}$ はユニタリなので，ノルムも保たれて自動的に正規化されています。

$$
\begin{aligned}
\|\mathbf{v}_k\|^2 &= \mathbf{u}_k^\dagger \mathbf{X}^\dagger\mathbf{X}\mathbf{u}_k \\
&= \|\mathbf{u}_k\|^2 \\
&= 1
\end{aligned}
$$

各 $\mathbf{v}_k = \mathbf{X}\mathbf{u}_k$ を計算します。

$$
\begin{aligned}
\mathbf{v}_1 &= \frac{1}{\sqrt{6}}\begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \\
&= \frac{1}{\sqrt{6}}\begin{pmatrix} \dfrac{3}{\sqrt{2}} \\[1.2ex] -\dfrac{1}{\sqrt{2}} \\[1.2ex] 1 \end{pmatrix} \\
&= \frac{1}{2\sqrt{3}}\begin{pmatrix} 3 \\ -1 \\ \sqrt{2} \end{pmatrix}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{v}_2 &= \frac{1}{\sqrt{2}}\begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \\
&= \frac{1}{\sqrt{2}}\begin{pmatrix} \dfrac{1}{\sqrt{2}} \\[1.2ex] \dfrac{1}{\sqrt{2}} \\[1.2ex] -1 \end{pmatrix} \\
&= \frac{1}{2}\begin{pmatrix} 1 \\ 1 \\ -\sqrt{2} \end{pmatrix}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{v}_3 &= \frac{1}{\sqrt{3}}\begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} & 0 \\[1.2ex] 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \\
&= \frac{1}{\sqrt{3}}\begin{pmatrix} 0 \\ \sqrt{2} \\ 1 \end{pmatrix}
\end{aligned}
$$

したがって，$\mathbf{B}$ の固有値と正規化固有ベクトルは次の通りです。

$$
\finalanswer{\lambda_1 = 2:\ \mathbf{v}_1 = \frac{1}{2\sqrt{3}}\begin{pmatrix} 3 \\ -1 \\ \sqrt{2} \end{pmatrix}, \qquad \lambda_2 = 0:\ \mathbf{v}_2 = \frac{1}{2}\begin{pmatrix} 1 \\ 1 \\ -\sqrt{2} \end{pmatrix}, \qquad \lambda_3 = -1:\ \mathbf{v}_3 = \frac{1}{\sqrt{3}}\begin{pmatrix} 0 \\ \sqrt{2} \\ 1 \end{pmatrix}}
$$

### (3)

(1) の行列 $\mathbf{A}$ の固有値は $\alpha_1 = 2$，$\alpha_2 = 0$，$\alpha_3 = -1$ です。$F$ を計算します。

$$
\begin{aligned}
F &= \sum_{i=1}^{3} |\alpha_i|^2 \\
&= 2^2 + 0^2 + (-1)^2 \\
&= 5
\end{aligned}
$$

次に $\mathbf{A}$ の成分のうち $0$ でないものは $a_{12}, a_{21}, a_{22}, a_{23}, a_{32}$ の5個で，値はいずれも $1$ です。$G$ を計算します。

$$
\begin{aligned}
G &= \sum_{i,j=1}^{3} |a_{ij}|^2 \\
&= 1^2 + 1^2 + 1^2 + 1^2 + 1^2 \\
&= 5
\end{aligned}
$$

$$
\finalanswer{F = 5, \qquad G = 5}
$$

### (4)

一般のエルミート行列 $\mathbf{A}$ に対して，常に $F = G$ が成り立ちます。これを示します。

まず $\operatorname{Tr}(\mathbf{A}^\dagger\mathbf{A})$ を成分で展開します。$(\mathbf{A}^\dagger)_{ij} = a_{ji}^*$ を用います。

$$
\begin{aligned}
\operatorname{Tr}(\mathbf{A}^\dagger\mathbf{A}) &= \sum_{i=1}^{n} (\mathbf{A}^\dagger\mathbf{A})_{ii} \\
&= \sum_{i=1}^{n}\sum_{j=1}^{n} (\mathbf{A}^\dagger)_{ij} a_{ji} \\
&= \sum_{i=1}^{n}\sum_{j=1}^{n} a_{ji}^* a_{ji} \\
&= \sum_{i,j=1}^{n} |a_{ji}|^2 \\
&= G
\end{aligned}
$$

一方，$\mathbf{A}$ はエルミート行列なので，あるユニタリ行列 $\mathbf{U}$（$\mathbf{U}^\dagger\mathbf{U} = \mathbf{I}$）によって対角行列 $\mathbf{D} = \operatorname{diag}(\alpha_1, \dots, \alpha_n)$ に対角化されます。すなわち $\mathbf{A} = \mathbf{U}\mathbf{D}\mathbf{U}^\dagger$ です。エルミート共役は $\mathbf{A}^\dagger = \mathbf{U}\mathbf{D}^\dagger\mathbf{U}^\dagger$ となります。トレースの巡回不変性 $\operatorname{Tr}(\mathbf{P}\mathbf{Q}) = \operatorname{Tr}(\mathbf{Q}\mathbf{P})$ を用いて $\operatorname{Tr}(\mathbf{A}^\dagger\mathbf{A})$ を計算します。

$$
\begin{aligned}
\operatorname{Tr}(\mathbf{A}^\dagger\mathbf{A}) &= \operatorname{Tr}(\mathbf{U}\mathbf{D}^\dagger\mathbf{U}^\dagger\mathbf{U}\mathbf{D}\mathbf{U}^\dagger) \\
&= \operatorname{Tr}(\mathbf{U}\mathbf{D}^\dagger\mathbf{D}\mathbf{U}^\dagger) \\
&= \operatorname{Tr}(\mathbf{D}^\dagger\mathbf{D}\mathbf{U}^\dagger\mathbf{U}) \\
&= \operatorname{Tr}(\mathbf{D}^\dagger\mathbf{D}) \\
&= \sum_{i=1}^{n} |\alpha_i|^2 \\
&= F
\end{aligned}
$$

以上2つの結果から，一般のエルミート行列 $\mathbf{A}$ に対して $F = G$ が成り立ちます。

$$
\finalanswer{F = G}
$$

<aside class="rigor-note" markdown>
(4) の証明では $\mathbf{A}$ がユニタリ対角化できる性質だけを使ったため，$F = G$ はエルミート行列に限らず任意の正規行列（$\mathbf{A}^\dagger\mathbf{A} = \mathbf{A}\mathbf{A}^\dagger$）に対しても成り立ちます。また (2) の $\mathbf{B} = \mathbf{X}\mathbf{A}\mathbf{X}^\dagger$ でも，$\sum_{i,j}|b_{ij}|^2 = \operatorname{Tr}(\mathbf{B}^\dagger\mathbf{B}) = \operatorname{Tr}(\mathbf{A}^\dagger\mathbf{A}) = 5$ と値が保たれます。
</aside>
