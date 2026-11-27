---
title: 東大理物 平成16年度 数学 第1問：多項式空間の線形写像の表現行列・固有値と反復合成
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成16年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成16年度 数学 第1問：多項式空間の線形写像の表現行列・固有値と反復合成

## 問題

変数 $x$ についての2次以下の次数の多項式のなす線形空間を $V$ とする。

線形写像 $F : V \longrightarrow V$ を以下のように定める。

$$
\text{任意の } p(x) \in V \text{ に対して} \qquad F\bigl(p(x)\bigr) = p(ax + b).
$$

ここで $a, b$ は定数で，$a \neq 1$ とする。以下の問に答えよ。

(1) $F(x^2 + x + 1)$ を求めよ。

(2) $V$ の基底を $e_0(x) = 1,\ e_1(x) = x,\ e_2(x) = x^2$ と選ぶ。このとき $F$ の表現行列 $M$，すなわち

$$
\bigl(F(e_0(x)), F(e_1(x)), F(e_2(x))\bigr) = \bigl(e_0(x), e_1(x), e_2(x)\bigr)M
$$

となる行列 $M$ を求めよ。

(3) 線形写像 $F$ の固有値，固有ベクトルを求めよ。

(4) 任意の自然数 $k$ について，$F$ を $e_1(x)$ に $k$ 回作用させて得られる $V$ の元を求めよ。

(5) 任意の自然数 $k$ について，$F$ を $e_2(x)$ に $k$ 回作用させて得られる $V$ の元を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成16年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
多項式の基底 $\{1, x, x^2\}$ に対する写像 $F$ の像を計算すると，表現行列 $M$ は上三角行列になります。上三角行列の固有値は対角成分にそのまま現れるため，$a \neq 1$ の条件のもとで固有値と固有ベクトルを直接求めることができます。

$e_1(x)$ や $e_2(x)$ を $F$ の固有ベクトルの線形結合で表すと，$F$ を $k$ 回作用させる操作が各固有ベクトルの係数を固有値の $k$ 乗倍するだけの計算になります。これにより，任意の自然数 $k$ に対する反復合成の結果をそのまま書き出すことができます。
</div>

### (1)

定義 $F(p(x)) = p(ax + b)$ に $p(x) = x^2 + x + 1$ を代入して展開します。

$$
\begin{aligned}
F(x^2 + x + 1) &= (ax + b)^2 + (ax + b) + 1 \\
&= a^2 x^2 + 2abx + b^2 + ax + b + 1 \\
&= a^2 x^2 + (2ab + a)x + (b^2 + b + 1)
\end{aligned}
$$

したがって，求める多項式は次式となります。

$$
\finalanswer{F(x^2 + x + 1) = a^2 x^2 + (2ab + a)x + (b^2 + b + 1)}
$$

### (2)

各基底 $e_0(x) = 1$，$e_1(x) = x$，$e_2(x) = x^2$ に $F$ を作用させます。

$$
\begin{aligned}
F(e_0(x)) &= 1 \\
&= 1\cdot e_0(x) + 0\cdot e_1(x) + 0\cdot e_2(x)
\end{aligned}
$$

$$
\begin{aligned}
F(e_1(x)) &= ax + b \\
&= b\cdot e_0(x) + a\cdot e_1(x) + 0\cdot e_2(x)
\end{aligned}
$$

$$
\begin{aligned}
F(e_2(x)) &= (ax + b)^2 \\
&= b^2\cdot e_0(x) + 2ab\cdot e_1(x) + a^2\cdot e_2(x)
\end{aligned}
$$

各式の係数を縦に並べることで，表現行列 $M$ が得られます。

$$
\finalanswer{M = \begin{pmatrix} 1 & b & b^2 \\ 0 & a & 2ab \\ 0 & 0 & a^2 \end{pmatrix}}
$$

### (3)

表現行列 $M$ は上三角行列なので，固有多項式は対角成分の積になります。

$$
\det(M - \lambda I) = (1 - \lambda)(a - \lambda)(a^2 - \lambda)
$$

固有方程式 $\det(M - \lambda I) = 0$ より，固有値は $\lambda = 1, a, a^2$ です。$a \neq 1$ なので $c = \dfrac{b}{a - 1}$ を定義し，次の3つの多項式を考えます。

$$
p_0(x) = 1, \qquad p_1(x) = x + \frac{b}{a - 1}, \qquad p_2(x) = \left(x + \frac{b}{a - 1}\right)^2
$$

それぞれに $F$ を作用させて確かめます。まず $p_0(x)$ については $F\bigl(p_0(x)\bigr) = 1 = p_0(x)$ です。次に $p_1(x)$ と $p_2(x)$ を計算します。

$$
\begin{aligned}
F\bigl(p_1(x)\bigr) &= ax + b + \frac{b}{a - 1} \\
&= ax + \frac{ab}{a - 1} \\
&= a\left(x + \frac{b}{a - 1}\right) \\
&= a\,p_1(x)
\end{aligned}
$$

$$
\begin{aligned}
F\bigl(p_2(x)\bigr) &= \left(ax + b + \frac{b}{a - 1}\right)^2 \\
&= a^2\left(x + \frac{b}{a - 1}\right)^2 \\
&= a^2 p_2(x)
\end{aligned}
$$

$p_0(x), p_1(x), p_2(x)$ は次数がそれぞれ $0, 1, 2$ なので，任意の $a \neq 1$ に対して線形独立な3つの固有ベクトルになります。固有値の重複の有無で場合分けすると，固有値と固有ベクトルは次のようになります。ただし $c_0, c_1, c_2$ はゼロベクトルにならない任意の定数です。

$a \neq 0$ かつ $a \neq -1$ のとき，$1, a, a^2$ は互いに異なる3つの固有値であり，各固有ベクトルはそれぞれ $c_0$，$c_1\left(x + \dfrac{b}{a - 1}\right)$，$c_2\left(x + \dfrac{b}{a - 1}\right)^2$ です。

$a = -1$ のとき，固有値は $1$ と $-1$ です。固有値 $1$ の固有ベクトルは $c_0 + c_2\left(x - \dfrac{b}{2}\right)^2$，固有値 $-1$ の固有ベクトルは $c_1\left(x - \dfrac{b}{2}\right)$ です。

$a = 0$ のとき，固有値は $1$ と $0$ です。固有値 $1$ の固有ベクトルは $c_0$，固有値 $0$ の固有ベクトルは $c_1(x - b) + c_2(x - b)^2$ です。

### (4)

設問3で導入した固有ベクトル $p_0(x) = 1$，$p_1(x) = x + \dfrac{b}{a - 1}$ を用いて $e_1(x) = x$ を表します。

$$
e_1(x) = p_1(x) - \frac{b}{a - 1}p_0(x)
$$

$F^k(p_0) = 1^k p_0 = p_0$ および $F^k(p_1) = a^k p_1$ を用いて，$F$ を $k$ 回作用させます。

$$
\begin{aligned}
F^k\bigl(e_1(x)\bigr) &= F^k\bigl(p_1(x)\bigr) - \frac{b}{a - 1}F^k\bigl(p_0(x)\bigr) \\
&= a^k\left(x + \frac{b}{a - 1}\right) - \frac{b}{a - 1} \\
&= a^k x + \frac{a^k - 1}{a - 1}b
\end{aligned}
$$

この式は $a = 0$（$k \ge 1$）のときも $F^k(e_1(x)) = b$ として成り立ちます。したがって，求める $V$ の元は次式となります。

$$
\finalanswer{F^k\bigl(e_1(x)\bigr) = a^k x + \frac{a^k - 1}{a - 1}b}
$$

### (5)

$e_2(x) = x^2 = \left(p_1(x) - \dfrac{b}{a - 1}p_0(x)\right)^2$ を固有ベクトル $p_0, p_1, p_2$ の線形結合に展開します。

$$
e_2(x) = p_2(x) - \frac{2b}{a - 1}p_1(x) + \frac{b^2}{(a - 1)^2}p_0(x)
$$

$F^k(p_0) = p_0$，$F^k(p_1) = a^k p_1$，$F^k(p_2) = a^{2k}p_2$ を用いて $F$ を $k$ 回作用させます。

$$
\begin{aligned}
F^k\bigl(e_2(x)\bigr) &= a^{2k}p_2(x) - \frac{2b}{a - 1}a^k p_1(x) + \frac{b^2}{(a - 1)^2}p_0(x) \\
&= a^{2k}\left(x + \frac{b}{a - 1}\right)^2 - \frac{2b}{a - 1}a^k\left(x + \frac{b}{a - 1}\right) + \frac{b^2}{(a - 1)^2} \\
&= \left\{a^k\left(x + \frac{b}{a - 1}\right) - \frac{b}{a - 1}\right\}^2 \\
&= \left(a^k x + \frac{a^k - 1}{a - 1}b\right)^2 \\
&= a^{2k}x^2 + 2a^k\frac{a^k - 1}{a - 1}bx + \left(\frac{a^k - 1}{a - 1}\right)^2 b^2
\end{aligned}
$$

したがって，求める $V$ の元は次式となります。

$$
\finalanswer{F^k\bigl(e_2(x)\bigr) = \left(a^k x + \frac{a^k - 1}{a - 1}b\right)^2 = a^{2k}x^2 + 2a^k\frac{a^k - 1}{a - 1}bx + \left(\frac{a^k - 1}{a - 1}\right)^2 b^2}
$$
