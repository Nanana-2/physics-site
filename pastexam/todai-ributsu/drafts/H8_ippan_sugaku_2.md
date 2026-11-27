---
title: 東大理物 平成8年度 一般教育科目 数学 第2問：3行2列実行列の特異値分解
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 一般教育科目 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成8年度 一般教育科目 数学 第2問：3行2列実行列の特異値分解

## 問題

3行2列の実行列 $A$ を

$$
A = U \Lambda V^T \qquad \text{(1)}
$$

のように分解することを考える。ただし，添字 $T$ は転置行列を表し，$U$，$\Lambda$，$V$ はそれぞれ3行2列，2行2列，2行2列の実行列で，

$$
V^T V = V V^T = U^T U = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

と

$$
\Lambda = \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}
$$

および $\lambda_1 \ge \lambda_2 \ge 0$ を仮定する。
{: .problem-lead }

(a) (1) 式のように分解ができたとして，行列 $A^T A$ のすべての固有値とそれに対応する固有ベクトルとを，$U$，$\Lambda$，$V$，$\lambda_1$，$\lambda_2$ を用いて表せ。必要なら単位ベクトル

$$
\vec{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

を用いてよい。

(b)

$$
A = \begin{pmatrix}
\dfrac{3 + \sqrt{2}}{2} & \dfrac{3 - \sqrt{2}}{2} \\[8pt]
\dfrac{3 - \sqrt{2}}{2} & \dfrac{3 + \sqrt{2}}{2} \\[8pt]
\dfrac{3\sqrt{2}}{2} & \dfrac{3\sqrt{2}}{2}
\end{pmatrix}
$$

のとき，$A^T A$ の固有値および長さ $1$ の固有ベクトルをすべて求めよ。ただし，各固有ベクトルの第1要素は非負とする。

(c) 前問で与えられた行列 $A$ に対して，(1) 式を満たす $U$，$\Lambda$，$V$ を求めよ。ただし，$V$ の第1行の各要素は非負とする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 一般教育科目 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
長方形行列 $A$ に対する特異値分解 $A = U\Lambda V^T$ を構成する問題です。積 $A^T A$ を作ると $U^T U = I_2$ により $U$ が消去され，対称行列 $A^T A = V\Lambda^2 V^T$ の直交対角化から特異値 $\lambda_1, \lambda_2$ と右特異ベクトルを並べた行列 $V$ が決まります。最後に $A V = U\Lambda$ を用いて $U = A V \Lambda^{-1}$ を計算すれば分解が完了します。
</div>

### (a)

式 (1) の $A = U \Lambda V^T$ と仮定 $U^T U = I_2$，$\Lambda^T = \Lambda$ を用いて $A^T A$ を計算します。

$$
\begin{aligned}
A^T A &= (U \Lambda V^T)^T (U \Lambda V^T) \\
&= V \Lambda^T (U^T U) \Lambda V^T \\
&= V \Lambda^2 V^T
\end{aligned}
$$

ここで $\Lambda^2 = \begin{pmatrix} \lambda_1^2 & 0 \\ 0 & \lambda_2^2 \end{pmatrix}$ です。この式の右から $V^T V = I_2$ を満たす直交行列 $V$ および単位ベクトル $\vec{e}_1, \vec{e}_2$ を順に作用させます。

$$
\begin{aligned}
(A^T A)(V\vec{e}_1) &= V \Lambda^2 (V^T V)\vec{e}_1 \\
&= V \Lambda^2 \vec{e}_1 \\
&= \lambda_1^2 (V\vec{e}_1)
\end{aligned}
$$

$$
\begin{aligned}
(A^T A)(V\vec{e}_2) &= V \Lambda^2 (V^T V)\vec{e}_2 \\
&= V \Lambda^2 \vec{e}_2 \\
&= \lambda_2^2 (V\vec{e}_2)
\end{aligned}
$$

$V$ は直交行列なので $V\vec{e}_1$ と $V\vec{e}_2$ は互いに直交する長さ $1$ のゼロでないベクトルです。したがって $A^T A$ の固有値は $\lambda_1^2$ および $\lambda_2^2$ であり，対応する固有ベクトルは $0$ でない任意の実数 $c_1, c_2$ に対して $c_1 V\vec{e}_1$ および $c_2 V\vec{e}_2$ です。なお $\lambda_1 = \lambda_2$ のときは $A^T A = \lambda_1^2 I_2$ となるため，$V\vec{e}_1$ と $V\vec{e}_2$ のゼロでない任意の線形結合も固有ベクトルになります。

$$
\finalanswer{(\lambda_1^2,\ c_1 V\vec{e}_1),\qquad (\lambda_2^2,\ c_2 V\vec{e}_2)\quad (c_1, c_2 \neq 0)}
$$

### (b)

与えられた行列 $A$ に対して $A^T A$ の各成分を計算します。

$$
\begin{aligned}
(A^T A)_{11} &= \left(\frac{3 + \sqrt{2}}{2}\right)^2 + \left(\frac{3 - \sqrt{2}}{2}\right)^2 + \left(\frac{3\sqrt{2}}{2}\right)^2 \\
&= \frac{(11 + 6\sqrt{2}) + (11 - 6\sqrt{2}) + 18}{4} \\
&= 10
\end{aligned}
$$

$$
\begin{aligned}
(A^T A)_{12} &= 2\cdot\frac{3 + \sqrt{2}}{2}\cdot\frac{3 - \sqrt{2}}{2} + \left(\frac{3\sqrt{2}}{2}\right)^2 \\
&= \frac{2(9 - 2) + 18}{4} \\
&= 8
\end{aligned}
$$

対称性より $(A^T A)_{22} = 10$，$(A^T A)_{21} = 8$ なので，

$$
A^T A = \begin{pmatrix} 10 & 8 \\ 8 & 10 \end{pmatrix}
$$

となります。固有方程式 $\det(A^T A - \mu I_2) = 0$ を解きます。

$$
\begin{aligned}
(10 - \mu)^2 - 64 &= 0 \\
(10 - \mu - 8)(10 - \mu + 8) &= 0 \\
(2 - \mu)(18 - \mu) &= 0
\end{aligned}
$$

よって固有値は大きい順に $\mu_1 = 18$，$\mu_2 = 2$ です。

次に各固有値に対応する第1要素が非負で長さ $1$ の固有ベクトルを求めます。

$\mu_1 = 18$ のとき $(A^T A - 18 I_2)\vec{v} = \vec{0}$ は $-8v_1 + 8v_2 = 0$ すなわち $v_1 = v_2$ となるため，長さ $1$ で第1要素が非負の固有ベクトルは

$$
\vec{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

です。$\mu_2 = 2$ のとき $(A^T A - 2 I_2)\vec{v} = \vec{0}$ は $8v_1 + 8v_2 = 0$ すなわち $v_2 = -v_1$ となるため，長さ $1$ で第1要素が非負の固有ベクトルは

$$
\vec{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

です。

$$
\finalanswer{\mu_1 = 18,\ \vec{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix},\qquad \mu_2 = 2,\ \vec{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}}
$$

### (c)

(a) の結果と仮定 $\lambda_1 \ge \lambda_2 \ge 0$ より，特異値は (b) の固有値の正の平方根として決まります。

$$
\lambda_1 = \sqrt{18} = 3\sqrt{2}, \qquad \lambda_2 = \sqrt{2}
$$

したがって対角行列 $\Lambda$ は次の通りです。

$$
\Lambda = \begin{pmatrix} 3\sqrt{2} & 0 \\ 0 & \sqrt{2} \end{pmatrix}
$$

行列 $V$ の第1列と第2列はそれぞれ $V\vec{e}_1$，$V\vec{e}_2$ であり，$A^T A$ の固有値 $\lambda_1^2 = 18$，$\lambda_2^2 = 2$ に対応する長さ $1$ の固有ベクトルです。$V$ の第1行の各要素が非負であるという条件より，(b) で求めた $\vec{v}_1, \vec{v}_2$ をそのまま並べた行列が $V$ になります。

$$
V = (\vec{v}_1, \vec{v}_2) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

実際，$V^T V = I_2$ および $V V^T = I_2$ を満たします。

最後に $U$ を求めます。$A = U\Lambda V^T$ の右から $V$ を掛けると $A V = U\Lambda$ であり，$\lambda_1, \lambda_2 > 0$ より $\Lambda$ は正則なので $U = A V \Lambda^{-1}$ と一意に定まります。すなわち $U$ の第1列 $\vec{u}_1$ と第2列 $\vec{u}_2$ はそれぞれ $\vec{u}_1 = \dfrac{1}{\lambda_1} A\vec{v}_1$，$\vec{u}_2 = \dfrac{1}{\lambda_2} A\vec{v}_2$ で与えられます。まず $A\vec{v}_1$ と $A\vec{v}_2$ を計算します。

$$
A\vec{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}
\dfrac{3 + \sqrt{2}}{2} + \dfrac{3 - \sqrt{2}}{2} \\[8pt]
\dfrac{3 - \sqrt{2}}{2} + \dfrac{3 + \sqrt{2}}{2} \\[8pt]
\dfrac{3\sqrt{2}}{2} + \dfrac{3\sqrt{2}}{2}
\end{pmatrix}
= \frac{1}{\sqrt{2}}\begin{pmatrix} 3 \\ 3 \\ 3\sqrt{2} \end{pmatrix}
$$

$$
A\vec{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}
\dfrac{3 + \sqrt{2}}{2} - \dfrac{3 - \sqrt{2}}{2} \\[8pt]
\dfrac{3 - \sqrt{2}}{2} - \dfrac{3 + \sqrt{2}}{2} \\[8pt]
\dfrac{3\sqrt{2}}{2} - \dfrac{3\sqrt{2}}{2}
\end{pmatrix}
= \frac{1}{\sqrt{2}}\begin{pmatrix} \sqrt{2} \\ -\sqrt{2} \\ 0 \end{pmatrix}
= \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}
$$

これらをそれぞれ $\lambda_1 = 3\sqrt{2}$，$\lambda_2 = \sqrt{2}$ で割ります。

$$
\vec{u}_1 = \frac{1}{3\sqrt{2}}\cdot\frac{1}{\sqrt{2}}\begin{pmatrix} 3 \\ 3 \\ 3\sqrt{2} \end{pmatrix} = \begin{pmatrix} \dfrac{1}{2} \\[6pt] \dfrac{1}{2} \\[6pt] \dfrac{1}{\sqrt{2}} \end{pmatrix}, \qquad
\vec{u}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} = \begin{pmatrix} \dfrac{1}{\sqrt{2}} \\[6pt] -\dfrac{1}{\sqrt{2}} \\[6pt] 0 \end{pmatrix}
$$

ここで $|\vec{u}_1|^2 = 1$，$|\vec{u}_2|^2 = 1$，$\vec{u}_1 \cdot \vec{u}_2 = 0$ となり，確かに $U^T U = I_2$ を満たします。以上より $U, \Lambda, V$ が求まりました。

$$
\finalanswer{U = \begin{pmatrix} \dfrac{1}{2} & \dfrac{1}{\sqrt{2}} \\[8pt] \dfrac{1}{2} & -\dfrac{1}{\sqrt{2}} \\[8pt] \dfrac{1}{\sqrt{2}} & 0 \end{pmatrix},\qquad \Lambda = \begin{pmatrix} 3\sqrt{2} & 0 \\ 0 & \sqrt{2} \end{pmatrix},\qquad V = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}}
$$
