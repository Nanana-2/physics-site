---
title: 東大理物 平成10年度 一般教育科目 数学 第1問：ジョルダン標準形・行列のべき乗と線形漸化式の収束条件
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 一般教育科目 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成10年度 一般教育科目 数学 第1問：ジョルダン標準形・行列のべき乗と線形漸化式の収束条件

## 問題

3行3列の実行列

$$
A = \begin{pmatrix}
a + 1 & 0 & 0 \\
0 & a + 1 & -1 \\
-1 & 1 & a - 1
\end{pmatrix}
$$

について以下の設問に答えよ。
{: .problem-lead }

(a) $A\vec{e}_1 = \lambda_1\vec{e}_1$，$A\vec{e}_2 = \lambda_2\vec{e}_2$，$A\vec{e}_3 = \vec{e}_2 + \lambda_2\vec{e}_3$ を満たす実数値 $\lambda_1$，$\lambda_2$ および $\mathbb{R}^3$ の単位ベクトル $\vec{e}_1$，$\vec{e}_2$，$\vec{e}_3$ を求めよ。ただし $\vec{e}_1$，$\vec{e}_2$，$\vec{e}_3$ の第2成分は正とする。

(b) $A^n\vec{e}_1$，$A^n\vec{e}_2$，$A^n\vec{e}_3$ を $\vec{e}_1$，$\vec{e}_2$，$\vec{e}_3$ の一次結合で表せ。

(c) $\vec{r}$，$\vec{d}$ を $\mathbb{R}^3$ のベクトルとする。このときベクトル列 $\vec{r}_0$，$\vec{r}_1$，$\vec{r}_2$，$\dots$ を $\vec{r}_0 = \vec{r}$，$\vec{r}_{n+1} = A\vec{r}_n + \vec{d}$（$n = 0, 1, 2, \dots$）によって定める。ベクトル列の極限 $\lim_{n \to \infty}\vec{r}_n$ が任意の $\vec{r}$，$\vec{d}$ について常に存在するような $a$ の範囲を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 一般教育科目 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
行列 $A$ の固有多項式を求めて重複固有値を特定し，固有ベクトル $\vec{e}_1, \vec{e}_2$ および広義固有ベクトル $\vec{e}_3$ からなるジョルダン基底を構成します。

続いて (b) でジョルダン基底に対する $A^n$ の作用を数学的帰納法で求め，(c) では漸化式の一般項をこの基底で展開することで，任意の初期ベクトル $\vec{r}$ と定数ベクトル $\vec{d}$ に対して極限が存在するためのスペクトル半径条件 $|\lambda_1| < 1, |\lambda_2| < 1$ を導出します。
</div>

### (a)

まず $A$ の固有値を求めるため，固有多項式 $\det(A - \lambda I)$ を計算します。第1行について余因子展開を行います。

$$
\begin{aligned}
\det(A - \lambda I) &= \begin{vmatrix}
a + 1 - \lambda & 0 & 0 \\
0 & a + 1 - \lambda & -1 \\
-1 & 1 & a - 1 - \lambda
\end{vmatrix} \\
&= (a + 1 - \lambda)\bigl((a + 1 - \lambda)(a - 1 - \lambda) + 1\bigr) \\
&= (a + 1 - \lambda)\bigl((a - \lambda)^2 - 1 + 1\bigr) \\
&= (a + 1 - \lambda)(a - \lambda)^2
\end{aligned}
$$

したがって固有値は重複度 $1$ の $a + 1$ と重複度 $2$ の $a$ です。条件 $A\vec{e}_3 = \vec{e}_2 + \lambda_2\vec{e}_3$ より $(A - \lambda_2 I)\vec{e}_3 = \vec{e}_2 \neq \vec{0}$ かつ $(A - \lambda_2 I)^2\vec{e}_3 = \vec{0}$ が成り立つため，$\lambda_2$ は重複度 $2$ の固有値でなければなりません。よって $\lambda_1 = a + 1$，$\lambda_2 = a$ と一意に定まります。

次に各単位ベクトルを求めます。

まず $\vec{e}_1$ について，$(A - (a + 1)I)\vec{e}_1 = \vec{0}$ を書き下します。

$$
\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & -1 \\
-1 & 1 & -2
\end{pmatrix}
\begin{pmatrix} x \\ y \\ z \end{pmatrix}
= \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

これより $z = 0$ および $x = y$ が得られます。単位ベクトルかつ第2成分 $y > 0$ の条件より，$\vec{e}_1 = \dfrac{1}{\sqrt{2}}(1, 1, 0)^T$ です。

次に $\vec{e}_2$ について，$(A - aI)\vec{e}_2 = \vec{0}$ を書き下します。

$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & -1 \\
-1 & 1 & -1
\end{pmatrix}
\begin{pmatrix} x \\ y \\ z \end{pmatrix}
= \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

これより $x = 0$ および $y = z$ が得られます。単位ベクトルかつ第2成分 $y > 0$ の条件より，$\vec{e}_2 = \dfrac{1}{\sqrt{2}}(0, 1, 1)^T$ です。

最後に $\vec{e}_3$ について，$(A - aI)\vec{e}_3 = \vec{e}_2$ を書き下します。

$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & -1 \\
-1 & 1 & -1
\end{pmatrix}
\begin{pmatrix} x \\ y \\ z \end{pmatrix}
= \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}
$$

第1行より $x = 0$，第2・第3行より $y - z = \dfrac{1}{\sqrt{2}}$ が得られます。そこで実数 $t$ を用いて

$$
\begin{aligned}
y &= t + \frac{1}{2\sqrt{2}} \\
z &= t - \frac{1}{2\sqrt{2}}
\end{aligned}
$$

とおき，単位ベクトルの条件 $x^2 + y^2 + z^2 = 1$ を用います。

$$
\begin{aligned}
\left(t + \frac{1}{2\sqrt{2}}\right)^2 + \left(t - \frac{1}{2\sqrt{2}}\right)^2 &= 1 \\
2t^2 + \frac{1}{4} &= 1 \\
t^2 &= \frac{3}{8}
\end{aligned}
$$

したがって $t = \pm\dfrac{\sqrt{6}}{4}$ です。ここで $t = -\dfrac{\sqrt{6}}{4}$ のときは第2成分が $y = \dfrac{-\sqrt{6} + \sqrt{2}}{4} < 0$ となり不適です。$t = +\dfrac{\sqrt{6}}{4}$ のとき第2成分が $y = \dfrac{\sqrt{6} + \sqrt{2}}{4} > 0$ を満たし，$z = \dfrac{\sqrt{6} - \sqrt{2}}{4}$ と一意に定まります。

$$
\finalanswer{\lambda_1 = a + 1,\quad \lambda_2 = a,\quad \vec{e}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix},\quad \vec{e}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix},\quad \vec{e}_3 = \frac{1}{4}\begin{pmatrix} 0 \\ \sqrt{6} + \sqrt{2} \\ \sqrt{6} - \sqrt{2} \end{pmatrix}}
$$

### (b)

固有ベクトル $\vec{e}_1, \vec{e}_2$ に対しては，繰り返し $A$ を掛けることで次式が得られます。

$$
\begin{aligned}
A^n\vec{e}_1 &= (a + 1)^n\vec{e}_1 \\
A^n\vec{e}_2 &= a^n\vec{e}_2
\end{aligned}
$$

次に $A^n\vec{e}_3$ について，すべての正の整数 $n$ に対して

$$
A^n\vec{e}_3 = n a^{n-1}\vec{e}_2 + a^n\vec{e}_3
$$

が成り立つことを数学的帰納法で示します。なお $n = 0$ のときは $0\cdot a^{-1} = 0$ とみなすことで $A^0\vec{e}_3 = \vec{e}_3$ にも一致します。

まず $n = 1$ のとき，(a) の関係より $A\vec{e}_3 = \vec{e}_2 + a\vec{e}_3$ であり成立します。

次に $n = k$（$k \ge 1$）で成り立つと仮定すると，$n = k + 1$ のときは次のように計算されます。

$$
\begin{aligned}
A^{k+1}\vec{e}_3 &= A\left(k a^{k-1}\vec{e}_2 + a^k\vec{e}_3\right) \\
&= k a^{k-1}(a\vec{e}_2) + a^k(\vec{e}_2 + a\vec{e}_3) \\
&= (k + 1)a^k\vec{e}_2 + a^{k+1}\vec{e}_3
\end{aligned}
$$

したがってすべての正の整数 $n$ で成立します。

$$
\finalanswer{A^n\vec{e}_1 = (a + 1)^n\vec{e}_1,\qquad A^n\vec{e}_2 = a^n\vec{e}_2,\qquad A^n\vec{e}_3 = n a^{n-1}\vec{e}_2 + a^n\vec{e}_3}
$$

### (c)

$\vec{e}_1, \vec{e}_2, \vec{e}_3$ の行列式を計算すると $\det(\vec{e}_1, \vec{e}_2, \vec{e}_3) = -\dfrac{1}{2} \neq 0$ であるため，$\{\vec{e}_1, \vec{e}_2, \vec{e}_3\}$ は $\mathbb{R}^3$ の基底をなします。

漸化式 $\vec{r}_{n+1} = A\vec{r}_n + \vec{d}$ を繰り返し用いると，任意の $n \ge 1$ に対して次式が得られます。

$$
\vec{r}_n = A^n\vec{r} + \sum_{k=0}^{n-1} A^k\vec{d}
$$

任意の $\vec{r}, \vec{d} \in \mathbb{R}^3$ を基底 $\{\vec{e}_1, \vec{e}_2, \vec{e}_3\}$ で展開します。

$$
\begin{aligned}
\vec{r} &= \alpha_1\vec{e}_1 + \alpha_2\vec{e}_2 + \alpha_3\vec{e}_3 \\
\vec{d} &= \beta_1\vec{e}_1 + \beta_2\vec{e}_2 + \beta_3\vec{e}_3
\end{aligned}
$$

(b) の結果を代入すると，$\vec{r}_n = c_1(n)\vec{e}_1 + c_2(n)\vec{e}_2 + c_3(n)\vec{e}_3$ の各成分は次のようになります。

$$
\begin{aligned}
c_1(n) &= \alpha_1(a + 1)^n + \beta_1\sum_{k=0}^{n-1}(a + 1)^k \\
c_2(n) &= \alpha_2 a^n + \alpha_3 n a^{n-1} + \beta_2\sum_{k=0}^{n-1} a^k + \beta_3\sum_{k=1}^{n-1} k a^{k-1} \\
c_3(n) &= \alpha_3 a^n + \beta_3\sum_{k=0}^{n-1} a^k
\end{aligned}
$$

$\lim_{n \to \infty}\vec{r}_n$ が存在するための必要十分条件は，$c_1(n), c_2(n), c_3(n)$ のすべてが有限値に収束することです。

まず必要条件を求めます。$\vec{r} = \vec{0}$，$\vec{d} = \vec{e}_1$（$\beta_1 = 1$）を選んだとき，$c_1(n) = \sum_{k=0}^{n-1}(a + 1)^k$ が収束するためには等比級数の収束条件より $|a + 1| < 1$ が必要です。同様に $\vec{r} = \vec{0}$，$\vec{d} = \vec{e}_2$（$\beta_2 = 1$）を選んだとき，$c_2(n) = \sum_{k=0}^{n-1} a^k$ が収束するためには $|a| < 1$ が必要です。

両不等式を連立して解きます。

$$
\begin{aligned}
|a + 1| < 1 &\iff -2 < a < 0 \\
|a| < 1 &\iff -1 < a < 1
\end{aligned}
$$

共通部分は $-1 < a < 0$ です。

逆に $-1 < a < 0$ が成り立つとき，$|a + 1| < 1$ かつ $|a| < 1$ であるため，以下がすべて有限値に収束します。

- $(a + 1)^n \to 0$，$a^n \to 0$，$n a^{n-1} \to 0$
- $\sum_{k=0}^{n-1}(a + 1)^k \to -\dfrac{1}{a}$
- $\sum_{k=0}^{n-1} a^k \to \dfrac{1}{1 - a}$
- $\sum_{k=1}^{n-1} k a^{k-1} \to \dfrac{1}{(1 - a)^2}$

したがって任意の $\vec{r}, \vec{d} \in \mathbb{R}^3$ に対して $\lim_{n \to \infty}\vec{r}_n$ は常に存在し，その極限値は $(I - A)^{-1}\vec{d}$ に一致します。

$$
\finalanswer{-1 < a < 0}
$$
