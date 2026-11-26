---
title: 東大理物 平成27年度 数学 第1問：第2種チェビシェフ多項式とスツルム・リウヴィル固有値問題
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成27年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成27年度 数学 第1問：第2種チェビシェフ多項式とスツルム・リウヴィル固有値問題

## 問題

(1) $n$ 次の正方行列 $A$ に対して，変数 $x$ に対する方程式

$$
\det(xE - A) = 0 \tag{1}
$$

を特性方程式，左辺を特性多項式と呼ぶ。ただし，$E$ は単位行列である。以下では $n = 2$ の場合を考える。

(i) 特性方程式を，$\operatorname{Tr} A,\ \det A$ を用いて表せ。

(ii) 特性多項式において $x$ に行列 $A$ を代入して得られる行列はゼロ行列であり，このため $A^N$（ただし，$N = 2, 3, \dots$）は $A$ のより低い冪の線形結合で表される。このことを用いて，$\det A = 1$ の場合には，

$$
U_N(\xi) - 2\xi U_{N-1}(\xi) + U_{N-2}(\xi) = 0 \tag{2}
$$

という漸化式を満たす関数列 $U_N(\xi)$ により，$A^N$ が

$$
A^N = U_{N-1}(\xi) A - U_{N-2}(\xi) E \tag{3}
$$

のように表されることを示せ。ここで $\xi = \dfrac{1}{2}\operatorname{Tr} A$ である。

(2) 次に，$a \le x \le b$ で

$$
\mathcal{L}u(x) \equiv \frac{d}{dx}\left[p(x)\frac{du(x)}{dx}\right] \tag{4}
$$

により定義された2階微分演算子 $\mathcal{L}$ を考える。ここで，$p(x)$ は $x$ の実関数であり，$p(a) = p(b) = 0$ を満たすものとする。このとき，

$$
\int_a^b v^*(x)\mathcal{L}u(x)\,dx = \int_a^b u(x)\bigl(\mathcal{L}v(x)\bigr)^*\,dx \tag{5}
$$

が成り立つことを示せ。ただし $u(x)$ と $v(x)$ は $x$ の複素関数である。

(3) 式 (4) で定義された演算子 $\mathcal{L}$ に対して，2階微分方程式

$$
\mathcal{L}u(x) = \lambda w(x) u(x) \tag{6}
$$

を考える。ただし，$w(x)$ は $x$ の実関数であり，$a < x < b$ において正の値をとる。この微分方程式が成立すれば，$\lambda$ は実数であることを示せ。

また，$\lambda = \lambda_1$ に対する微分方程式 (6) の解を $u_1(x)$，$\lambda = \lambda_2$ に対する解を $u_2(x)$ としたときに，$\lambda_1 \neq \lambda_2$ であれば

$$
\int_a^b u_1(x) u_2^*(x) w(x)\,dx = 0 \tag{7}
$$

であることを示せ。

(4) 上記の設問1における $U_N(x)$ は，$-1 \le x \le 1$ において

$$
(1 - x^2)\frac{d^2}{dx^2}U_N(x) - 3x\frac{d}{dx}U_N(x) + N(N + 2)U_N(x) = 0 \tag{8}
$$

という微分方程式を満たすことが知られている。この微分方程式が，式 (4) において $p(x)$ を適当に選んだ $\mathcal{L}$ により与えられる方程式 (6) の形になることを示せ。さらに，$M \neq N$ に対して

$$
\int_{-1}^{1} U_M(x) U_N(x) (1 - x^2)^{1/2}\,dx \tag{9}
$$

を，解答の筋道を示した上で求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成27年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ケイリー・ハミルトンの定理を使うと，$A^2$ は $A$ と $I$ の1次結合で書くことができます。そのため，$A^N$ も $A$ と $I$ の1次結合になり，その係数は $N$ についての漸化式を満たします。

微分方程式 $\mathcal{L}u=\lambda u$ の2つの解 $u_1$，$u_2$ について，$u_2\mathcal{L}u_1-u_1\mathcal{L}u_2$ を区間で積分すると，部分積分で境界項だけが残ります。境界項が $0$ になると，$(\lambda_1-\lambda_2)$ と重み付きの積分の積が $0$ になるので，固有値が異なる解は直交します。
</div>

### (1)
(i) $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$ とおくと，$\operatorname{Tr} A = a_{11} + a_{22},\ \det A = a_{11}a_{22} - a_{12}a_{21}$ なので，

$$
\begin{aligned}
\det(xE - A) &= (x - a_{11})(x - a_{22}) - a_{12}a_{21} \\
&= x^2 - (a_{11} + a_{22})x + (a_{11}a_{22} - a_{12}a_{21}) \\
 &= x^2 - (\operatorname{Tr} A)x + \det A \\
&= 0
\end{aligned}
$$

したがって，

$$
\finalanswer{x^2 - (\operatorname{Tr} A)x + \det A = 0}
$$

(ii) $\det A = 1$ と $\operatorname{Tr} A = 2\xi$ より，ケイリー・ハミルトンの定理は

$$
A^2 - 2\xi A + E = O \implies A^2 = 2\xi A - E
$$

となります。初期条件を $U_0(\xi) = 1,\ U_1(\xi) = 2\xi$ とおき，漸化式 (2) $U_N(\xi) = 2\xi U_{N-1}(\xi) - U_{N-2}(\xi)\ (N \ge 2)$ によって関数列 $U_N(\xi)$ を定めます。

$N = 2$ のとき $A^2 = 2\xi A - E = U_1(\xi)A - U_0(\xi)E$ となり，式 (3) が成り立ちます。

ある $N \ge 2$ に対して式 (3) が成り立つと仮定すると，$N + 1$ に対しては

$$
\begin{aligned}
A^{N+1} &= A^N A \\
&= \bigl(U_{N-1}(\xi)A - U_{N-2}(\xi)E\bigr)A \\
&= U_{N-1}(\xi)A^2 - U_{N-2}(\xi)A \\
&= U_{N-1}(\xi)(2\xi A - E) - U_{N-2}(\xi)A \\
&= \bigl(2\xi U_{N-1}(\xi) - U_{N-2}(\xi)\bigr)A - U_{N-1}(\xi)E \\
&= U_N(\xi)A - U_{N-1}(\xi)E
\end{aligned}
$$

となり，$N + 1$ でも式 (3) が成り立ちます。よって数学的帰納法によりすべての $N \ge 2$ に対して式 (3) が成り立ちます。

### (2)
以下では $u,v$ と1階導関数が端点まで有限で，部分積分ができる関数を考えます。式 (4) を左辺に代入して部分積分を2回行います。$p(x)$ は実関数であり，$p(a)=p(b)=0$ と端点での有限性から境界項は $0$ になります。

$$
\begin{aligned}
\int_a^b v^*(x)\mathcal{L}u(x)\,\mathrm{d}x
&= \int_a^b v^*(x)\frac{\mathrm{d}}{\mathrm{d}x}\left[p(x)\frac{\mathrm{d}u(x)}{\mathrm{d}x}\right]\mathrm{d}x \\
&= \left[v^*(x)p(x)\frac{\mathrm{d}u(x)}{\mathrm{d}x}\right]_a^b - \int_a^b \frac{\mathrm{d}v^*(x)}{\mathrm{d}x}p(x)\frac{\mathrm{d}u(x)}{\mathrm{d}x}\,\mathrm{d}x \\
&= -\left[p(x)\frac{\mathrm{d}v^*(x)}{\mathrm{d}x}u(x)\right]_a^b + \int_a^b u(x)\frac{\mathrm{d}}{\mathrm{d}x}\left[p(x)\frac{\mathrm{d}v^*(x)}{\mathrm{d}x}\right]\mathrm{d}x \\
&= \int_a^b u(x)\bigl(\mathcal{L}v(x)\bigr)^*\,\mathrm{d}x
\end{aligned}
$$

よって式 (5) が成り立ちます。

### (3)
まず，$\lambda$ が実数であることを示します。恒等的に $0$ でない解 $u(x)$ に対して，式 (5) で $v(x) = u(x)$ とおき，式 (6) を代入します。ここで $w(x)$ は実関数です。

$$
\begin{aligned}
\int_a^b u^*(x)\mathcal{L}u(x)\,\mathrm{d}x &= \lambda\int_a^b |u(x)|^2 w(x)\,\mathrm{d}x \\
\int_a^b u(x)\bigl(\mathcal{L}u(x)\bigr)^*\,\mathrm{d}x &= \lambda^*\int_a^b |u(x)|^2 w(x)\,\mathrm{d}x
\end{aligned}
$$

両辺の差をとると，

$$
(\lambda - \lambda^*)\int_a^b |u(x)|^2 w(x)\,\mathrm{d}x = 0
$$

となります。$a < x < b$ で $w(x) > 0$ かつ $u(x) \not\equiv 0$ なので $\displaystyle\int_a^b |u(x)|^2 w(x)\,\mathrm{d}x > 0$ です。よって $\lambda = \lambda^*$，すなわち $\lambda$ は実数です。

次に，直交性を示します。式 (5) で $u = u_1,\ v = u_2$ とおき，$\lambda_2^* = \lambda_2$ を用います。

$$
\begin{aligned}
\int_a^b u_2^*(x)\mathcal{L}u_1(x)\,\mathrm{d}x &= \lambda_1\int_a^b u_1(x) u_2^*(x) w(x)\,\mathrm{d}x \\
\int_a^b u_1(x)\bigl(\mathcal{L}u_2(x)\bigr)^*\,\mathrm{d}x &= \lambda_2\int_a^b u_1(x) u_2^*(x) w(x)\,\mathrm{d}x
\end{aligned}
$$

両辺の差をとると，

$$
(\lambda_1 - \lambda_2)\int_a^b u_1(x) u_2^*(x) w(x)\,\mathrm{d}x = 0
$$

となります。$\lambda_1 \neq \lambda_2$ より式 (7) $\displaystyle\int_a^b u_1(x) u_2^*(x) w(x)\,\mathrm{d}x = 0$ が成り立ちます。

### (4)
式 (8) の両辺に $(1 - x^2)^{1/2}$ を掛けます。

$$
(1 - x^2)^{3/2}\frac{\mathrm{d}^2 U_N}{\mathrm{d}x^2} - 3x(1 - x^2)^{1/2}\frac{\mathrm{d}U_N}{\mathrm{d}x} + N(N + 2)(1 - x^2)^{1/2} U_N = 0
$$

ここで $\dfrac{\mathrm{d}}{\mathrm{d}x}\bigl[(1 - x^2)^{3/2}\bigr] = -3x(1 - x^2)^{1/2}$ なので，最初の2項は1つの微分にまとまります。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left[(1 - x^2)^{3/2}\frac{\mathrm{d}U_N(x)}{\mathrm{d}x}\right] = -N(N + 2)(1 - x^2)^{1/2} U_N(x)
$$

したがって，区間 $[a, b] = [-1, 1]$ において

$$
p(x) = (1 - x^2)^{3/2},\qquad w(x) = (1 - x^2)^{1/2},\qquad \lambda_N = -N(N + 2)
$$

と選べば，式 (8) は方程式 (6) $\mathcal{L}U_N(x) = \lambda_N w(x) U_N(x)$ の形になります。このとき $p(-1) = p(1) = 0$ かつ $-1 < x < 1$ で $w(x) > 0$ を満たします。

非負整数 $M \neq N$ に対して $\lambda_M - \lambda_N = -(M - N)(M + N + 2) \neq 0$ なので，設問3の式 (7) および $U_N(x)$ が実関数であることから，積分 (9) は $0$ となります。したがって，

$$
\finalanswer{\int_{-1}^{1} U_M(x) U_N(x) (1 - x^2)^{1/2}\,\mathrm{d}x = 0 \qquad (M \neq N)}
$$

<aside class="rigor-note" markdown>
漸化式 (2) と初期条件 $U_0(\xi) = 1,\ U_1(\xi) = 2\xi$ で定義される多項式 $U_N(\xi)$ は第2種チェビシェフ多項式と呼ばれ，$\xi = \cos\theta$ とおくと $U_N(\cos\theta) = \dfrac{\sin\bigl((N + 1)\theta\bigr)}{\sin\theta}$ と表されます。積分 (9) で $x = \cos\theta$ と変数変換すれば $\displaystyle\int_0^\pi \sin\bigl((M + 1)\theta\bigr)\sin\bigl((N + 1)\theta\bigr)\,\mathrm{d}\theta = \dfrac{\pi}{2}\delta_{MN}$ となり，$M \neq N$ で $0$ になることも直接確かめることができます。
</aside>
