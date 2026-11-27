---
title: 東大理物 平成21年度 数学 第1問：実対称行列の固有値とトレース不等式
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成21年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成21年度 数学 第1問：実対称行列の固有値とトレース不等式

## 問題

(1) 実変数 $\theta$ に依存する2行2列の実対称行列

$$
A = \frac{1}{4}\begin{pmatrix} \cos\theta + 3\sin\theta & -\sqrt{3}\cos\theta + \sqrt{3}\sin\theta \\ -\sqrt{3}\cos\theta + \sqrt{3}\sin\theta & 3\cos\theta + \sin\theta \end{pmatrix}
$$

に対し，次の問に答えよ。なお $\theta$ の範囲は $0 \le \theta \le \dfrac{\pi}{2}$ であるとする。

(i) 行列 $A$ の2つの固有値を求めよ。

(ii) $A$ の対角成分の和 $\mathrm{Tr}\,A$ の3乗 $(\mathrm{Tr}\,A)^3$ と $A^3$ の対角成分の和 $\mathrm{Tr}\,(A^3)$ の差を $\theta$ の関数として

$$
f(\theta) = (\mathrm{Tr}\,A)^3 - \mathrm{Tr}\,(A^3)
$$

と置くとき，$f(\theta)$ の最大値と最小値を求めよ。

(iii) $I$ を単位行列とするとき，$A$ の多項式から作られる行列

$$
B = A^4 - A^2 + A + (\cos^2\theta\sin^2\theta - 1)I
$$

が逆行列を持たないような $\theta$ の値を求めよ。

(iv) $B$ が逆行列 $B^{-1}$ を持つとき，$B^{-1}$ を行列 $A$ の1次式，すなわち係数 $a_1(\theta), a_0(\theta)$ を用いて $B^{-1} = a_1(\theta)A + a_0(\theta)I$ の形に表せ。

(2) $N$ 行 $N$ 列の実対称行列 $X$ の全ての固有値 $\lambda_i$（$i = 1, \dots, N$）が非負 $\lambda_i \ge 0$ であるとする。

(i) 任意の自然数 $n$ に対して不等式

$$
(\mathrm{Tr}\,X)^n \ge \mathrm{Tr}\,(X^n)
$$

が成り立つことを証明せよ。

(ii) 上の不等式で等号 $(\mathrm{Tr}\,X)^n = \mathrm{Tr}\,(X^n)$ が成立するのは，固有値 $\lambda_i$ がどのような場合に限られるか。ただし $n \ge 2$ とする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成21年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
実対称行列は直交行列で対角化することができ，トレースや行列式，多項式の固有値はいずれも元の行列の固有値だけで表すことができます。そのため，行列のべき乗を成分ごとに計算しなくても，固有値に関する代数計算へ置き換えることができます。

また2行2列の行列では，ケーリー・ハミルトンの定理によって2次以上のべき乗を1次式へ次数下げすることができます。これを用いると，高次の多項式で表された行列とその逆行列を $A$ の1次式で直接求めることができます。
</div>

### (1)

(i) $A$ のトレースと行列式を計算します。

$$
\begin{aligned}
\mathrm{Tr}\,A &= \frac{1}{4}\bigl((\cos\theta + 3\sin\theta) + (3\cos\theta + \sin\theta)\bigr) \\
&= \frac{1}{4}(4\cos\theta + 4\sin\theta) \\
&= \cos\theta + \sin\theta
\end{aligned}
$$

$$
\begin{aligned}
\det A &= \frac{1}{16}\Bigl((\cos\theta + 3\sin\theta)(3\cos\theta + \sin\theta) - (-\sqrt{3}\cos\theta + \sqrt{3}\sin\theta)^2\Bigr) \\
&= \frac{1}{16}\Bigl((3\cos^2\theta + 10\sin\theta\cos\theta + 3\sin^2\theta) - 3(\cos^2\theta - 2\sin\theta\cos\theta + \sin^2\theta)\Bigr) \\
&= \frac{1}{16}(16\sin\theta\cos\theta) \\
&= \sin\theta\cos\theta
\end{aligned}
$$

したがって，$A$ の固有方程式は次式になります。

$$
\begin{aligned}
\lambda^2 - (\mathrm{Tr}\,A)\lambda + \det A &= 0 \\
\lambda^2 - (\cos\theta + \sin\theta)\lambda + \sin\theta\cos\theta &= 0 \\
(\lambda - \cos\theta)(\lambda - \sin\theta) &= 0
\end{aligned}
$$

よって，$A$ の2つの固有値は次式となります。

$$
\finalanswer{\cos\theta, \quad \sin\theta}
$$

(ii) $A$ は実対称行列なので対角化することができ，$A$ の固有値を $\lambda_1 = \cos\theta$，$\lambda_2 = \sin\theta$ とすると，$\mathrm{Tr}\,A = \lambda_1 + \lambda_2$，$\mathrm{Tr}\,(A^3) = \lambda_1^3 + \lambda_2^3$ です。これを用いて $f(\theta)$ を変形します。

$$
\begin{aligned}
f(\theta) &= (\lambda_1 + \lambda_2)^3 - (\lambda_1^3 + \lambda_2^3) \\
&= 3\lambda_1\lambda_2(\lambda_1 + \lambda_2) \\
&= 3\sin\theta\cos\theta(\cos\theta + \sin\theta)
\end{aligned}
$$

$t = \cos\theta + \sin\theta$ とおきます。合成公式より $t = \sqrt{2}\sin\!\left(\theta + \dfrac{\pi}{4}\right)$ であり，$0 \le \theta \le \dfrac{\pi}{2}$ より $\dfrac{\pi}{4} \le \theta + \dfrac{\pi}{4} \le \dfrac{3\pi}{4}$ なので，$t$ の値域は $1 \le t \le \sqrt{2}$ です。また $t^2 = 1 + 2\sin\theta\cos\theta$ より $\sin\theta\cos\theta = \dfrac{t^2 - 1}{2}$ なので，$f(\theta)$ は $t$ の関数 $g(t)$ として次のように書くことができます。

$$
\begin{aligned}
g(t) &= 3\cdot\frac{t^2 - 1}{2}\cdot t \\
&= \frac{3}{2}(t^3 - t)
\end{aligned}
$$

微分すると $g'(t) = \dfrac{3}{2}(3t^2 - 1)$ であり，$1 \le t \le \sqrt{2}$ の範囲では $g'(t) > 0$ です。よって $g(t)$ は単調増加します。最小値は $t = 1$，すなわち $\theta = 0, \dfrac{\pi}{2}$ のときの $g(1) = 0$ です。最大値は $t = \sqrt{2}$，すなわち $\theta = \dfrac{\pi}{4}$ のときの次式になります。

$$
\begin{aligned}
g(\sqrt{2}) &= \frac{3}{2}\bigl(2\sqrt{2} - \sqrt{2}\bigr) \\
&= \frac{3\sqrt{2}}{2}
\end{aligned}
$$

したがって，$f(\theta)$ の最大値は $\dfrac{3\sqrt{2}}{2}$，最小値は $0$ です。

$$
\finalanswer{f_{\max} = \frac{3\sqrt{2}}{2}, \qquad f_{\min} = 0}
$$

(iii) $A$ は直交行列 $U$ により $U^{-1}AU = \operatorname{diag}(\cos\theta, \sin\theta)$ と対角化されます。このとき $A^2$ は $U^{-1}A^2 U = \operatorname{diag}(\cos^2\theta, \sin^2\theta)$ となります。$\cos^2\theta + \sin^2\theta = 1$ を用いると，$A^2$ の固有値 $\mu = \cos^2\theta, \sin^2\theta$ はいずれも次の2次方程式を満たします。

$$
\begin{aligned}
(\mu - \cos^2\theta)(\mu - \sin^2\theta) &= 0 \\
\mu^2 - (\cos^2\theta + \sin^2\theta)\mu + \cos^2\theta\sin^2\theta &= 0 \\
\mu^2 - \mu + \cos^2\theta\sin^2\theta &= 0
\end{aligned}
$$

よって対角成分がすべて $0$ となるため，行列として次式が成り立ちます。

$$
A^4 - A^2 + \cos^2\theta\sin^2\theta\,I = O
$$

これを $B$ の定義式に代入します。

$$
\begin{aligned}
B &= \bigl(A^4 - A^2 + \cos^2\theta\sin^2\theta\,I\bigr) + A - I \\
&= A - I
\end{aligned}
$$

よって $B$ の固有値は $\cos\theta - 1$ と $\sin\theta - 1$ であり，$\det B = (\cos\theta - 1)(\sin\theta - 1)$ です。$B$ が逆行列を持たない条件は $\det B = 0$，すなわち $\cos\theta = 1$ または $\sin\theta = 1$ です。$0 \le \theta \le \dfrac{\pi}{2}$ の範囲で解くと，$\theta = 0, \dfrac{\pi}{2}$ となります。

$$
\finalanswer{\theta = 0, \ \frac{\pi}{2}}
$$

(iv) (i) より，ケーリー・ハミルトンの定理から次式が成り立ちます。

$$
A^2 - (\cos\theta + \sin\theta)A + \sin\theta\cos\theta\,I = O
$$

(iii) で得た $B = A - I$ をくくり出すために，左辺を $A - I$ で割ります。

$$
\begin{aligned}
(A - I)\bigl(A + (1 - \cos\theta - \sin\theta)I\bigr) &= A^2 - (\cos\theta + \sin\theta)A + (\cos\theta + \sin\theta - 1)I \\
&= (\cos\theta + \sin\theta - 1 - \sin\theta\cos\theta)I \\
&= -(1 - \cos\theta)(1 - \sin\theta)I
\end{aligned}
$$

$B$ が逆行列を持つとき $(1 - \cos\theta)(1 - \sin\theta) \neq 0$ なので，両辺を $-(1 - \cos\theta)(1 - \sin\theta)$ で割ります。

$$
\begin{aligned}
B^{-1} &= -\frac{1}{(1 - \cos\theta)(1 - \sin\theta)}\bigl(A + (1 - \cos\theta - \sin\theta)I\bigr) \\
&= -\frac{1}{(1 - \cos\theta)(1 - \sin\theta)}A + \frac{\cos\theta + \sin\theta - 1}{(1 - \cos\theta)(1 - \sin\theta)}I
\end{aligned}
$$

したがって，$B^{-1}$ は次式となります。

$$
\finalanswer{B^{-1} = -\frac{1}{(1 - \cos\theta)(1 - \sin\theta)}A + \frac{\cos\theta + \sin\theta - 1}{(1 - \cos\theta)(1 - \sin\theta)}I}
$$

### (2)

(i) $X$ は $N$ 行 $N$ 列の実対称行列なので，実直交行列 $P$ を選んで対角化することができます。

$$
P^{-1}XP = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_N)
$$

両辺を $n$ 乗すると $P^{-1}X^n P = \operatorname{diag}(\lambda_1^n, \lambda_2^n, \dots, \lambda_N^n)$ です。トレースの相似不変性より，次式が成り立ちます。

$$
\mathrm{Tr}\,X = \sum_{i=1}^{N} \lambda_i, \qquad \mathrm{Tr}\,(X^n) = \sum_{i=1}^{N} \lambda_i^n
$$

したがって，示すべき不等式は非負実数 $\lambda_1, \dots, \lambda_N \ge 0$ に対する

$$
\left(\sum_{i=1}^{N} \lambda_i\right)^n \ge \sum_{i=1}^{N} \lambda_i^n
$$

です。これを自然数 $n$ に関する数学的帰納法で示します。

$n = 1$ のときは両辺ともに $\displaystyle \sum_{i=1}^{N} \lambda_i$ なので等号で成り立ちます。ある自然数 $k \ge 1$ で $\displaystyle \left(\sum_{i=1}^{N} \lambda_i\right)^k \ge \sum_{i=1}^{N} \lambda_i^k$ が成り立つと仮定します。$\displaystyle \sum_{i=1}^{N}\lambda_i \ge 0$ なので，両辺に $\displaystyle \sum_{j=1}^{N}\lambda_j$ を掛けても不等号の向きは変わりません。

$$
\begin{aligned}
\left(\sum_{i=1}^{N} \lambda_i\right)^{k+1} &\ge \left(\sum_{i=1}^{N} \lambda_i^k\right)\left(\sum_{j=1}^{N} \lambda_j\right) \\
&= \sum_{i=1}^{N} \lambda_i^{k+1} + \sum_{i \neq j} \lambda_i^k \lambda_j
\end{aligned}
$$

すべての $i, j$ で $\lambda_i \ge 0$ なので，$\displaystyle \sum_{i \neq j} \lambda_i^k \lambda_j \ge 0$ です。よって次式が成り立ちます。

$$
\left(\sum_{i=1}^{N} \lambda_i\right)^{k+1} \ge \sum_{i=1}^{N} \lambda_i^{k+1}
$$

以上より，すべての自然数 $n$ に対して $(\mathrm{Tr}\,X)^n \ge \mathrm{Tr}\,(X^n)$ が成り立ちます。

(ii) $n \ge 2$ とします。(i) の帰納法で用いた式を $k = 1$ から $n - 1$ まで順にたどると，等号が成り立つための必要十分条件は，すべての $k = 1, \dots, n - 1$ について非負の交差項の和 $\displaystyle \sum_{i \neq j} \lambda_i^k \lambda_j$ が $0$ になることです。

$\lambda_i\ge0$ より，次の和の各項は非負です。

$$
\sum_{i\ne j}\lambda_i^k\lambda_j
$$

したがって，和が $0$ になる条件は，各項がすべて $0$ になることです。

$$
\lambda_i^k\lambda_j=0\quad(i\ne j)
$$

$k\ge1$ なので，この条件は各 $i\ne j$ で $\lambda_i=0$ または $\lambda_j=0$ となることと同値です。

すなわち，正の固有値が2個以上存在してはなりません。逆に，0でない固有値が高々1個であれば，すべての交差項が $0$ となって等号 $(\mathrm{Tr}\,X)^n = \mathrm{Tr}\,(X^n)$ が成り立ちます。

したがって，すべての固有値が $0$ の場合と，正の固有値が1個だけの場合に限り，等号が成立します。


$$
\finalanswer{\operatorname{rank}X\le1}
$$