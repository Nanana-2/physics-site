---
title: 東大理物 平成28年度 数学 第1問：2次行列のトレース漸化式と三重対角対称行列の固有値
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成28年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成28年度 数学 第1問：2次行列のトレース漸化式と三重対角対称行列の固有値

## 問題

(1) 二つの2次正方行列

$$
A = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix},\qquad B = \frac{1}{2}\begin{pmatrix} \sqrt{3} & -1 \\ 1 & \sqrt{3} \end{pmatrix} \tag{1}
$$

から，以下のような規則で行列 $M_n\ (n = 0, 1, 2, \dots)$ を生成する。まず，$M_0 = B,\ M_1 = A$ と定義し，次に一般の $n \ge 2$ については

$$
M_n = M_{n-1} M_{n-2} \tag{2}
$$

という漸化式により行列 $M_n$ を定義する。このとき，以下の設問に答えよ。

(i) 一般の $n$ について，$M_n$ が次の性質を満たすことを示せ。ただし，$E$ は2次の単位行列である。

$$
\begin{aligned}
&\text{(a)}\quad \det M_n = 1 \\
&\text{(b)}\quad \operatorname{Tr} M_n = \operatorname{Tr}(M_n)^{-1} \\
&\text{(c)}\quad M_n + (M_n)^{-1} = (\operatorname{Tr} M_n) E
\end{aligned}
$$

以下では，$x_n = \operatorname{Tr} M_n$ が満たす性質を調べる。

(ii) $M_{n+1} + (M_{n-2})^{-1}$ を $M_n$ と $M_{n-1}$ で表せ。また，それを用いて，$x_n$ が漸化式

$$
x_{n+1} = x_n x_{n-1} - x_{n-2} \tag{3}
$$

を満たすことを示せ。

(iii) (3) の漸化式を用いて，$x_n,\ x_{n+1},\ x_{n+2}$ から構成される

$$
I_n = x_{n+2}^2 + x_{n+1}^2 + x_n^2 - x_{n+2} x_{n+1} x_n \tag{4}
$$

が $n$ に依存しない量であることを証明せよ。また，その値を求めよ。

(2) 次の $N$ 次正方行列 $C$ を考える。

$$
C = \begin{pmatrix}
0 & b_1 & & & O \\
b_1 & 0 & b_2 & & \\
 & b_2 & 0 & \ddots & \\
 & & \ddots & \ddots & b_{N-1} \\
O & & & b_{N-1} & 0
\end{pmatrix} \tag{5}
$$

すなわち，$C_{i, i+1} = C_{i+1, i} = b_i\ (i = 1, 2, \dots, N - 1)$ であり，これら以外の成分はすべて $0$ であるものとする。また，すべての $i$ について，$b_i > 0$ であるとする。このとき，以下の設問に答えよ。

(i) $N = 3$ の場合について，行列 $C$ の固有値をすべて求めよ。

(ii) 列ベクトル $\boldsymbol{v} = (v_1, v_2, \dots, v_N)^{\mathrm{T}}$ が，行列 $C$ の固有ベクトルであるとき，$v_1 \neq 0$ であることを証明せよ。

(iii) 行列 $C$ の固有値がすべて互いに異なることを証明せよ。（設問 (ii) の結果を用いてもよい。）

> 出典：東京大学大学院理学系研究科物理学専攻 平成28年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
行列式が $1$ の2行2列の行列 $M$ では，ケイリー・ハミルトンの定理から $M+M^{-1}=(\operatorname{Tr}M)E$ が成り立ちます。この式を行列の漸化式 $M_n=M_{n-1}M_{n-2}$ と組み合わせると，行列そのものを使わずに，トレース $x_n$ だけの漸化式を作ることができます。

三重対角行列の固有方程式を成分で書くと，$v_{i-1}$，$v_i$，$v_{i+1}$ を結ぶ3項の漸化式になります。$v_1$ を決めると残りの成分は順に決まるので，固有ベクトルは定数倍を除いて1つしかなく，このことから固有値が重ならないことを示します。
</div>

### (1)
(i)
(a) $\det M_0 = \det B = \dfrac{1}{4}(3 + 1) = 1$， $\det M_1 = \det A = \dfrac{1}{2}(1 + 1) = 1$ です。$n \ge 2$ に対して $\det M_k = 1\ (k < n)$ を仮定すると，式 (2) より

$$
\begin{aligned}
\det M_n &= \det(M_{n-1} M_{n-2}) \\
&= (\det M_{n-1})(\det M_{n-2}) \\
&= 1\cdot 1 \\
&= 1
\end{aligned}
$$

となるため，数学的帰納法によりすべての $n \ge 0$ で $\det M_n = 1$ が成り立ちます。

(b) $M_n = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$ とおくと，(a) より $\det M_n = ps - qr = 1$ なので逆行列は $(M_n)^{-1} = \begin{pmatrix} s & -q \\ -r & p \end{pmatrix}$ です。よって

$$
\begin{aligned}
\operatorname{Tr}(M_n)^{-1} &= s + p \\
&= \operatorname{Tr} M_n
\end{aligned}
$$

が成り立ちます。

(c) $2\times 2$ 行列に対するケイリー・ハミルトンの定理と $\det M_n = 1$ より，

$$
M_n^2 - (\operatorname{Tr} M_n) M_n + E = O
$$

が成り立ちます。両辺に $(M_n)^{-1}$ を掛けて移項すると，

$$
M_n + (M_n)^{-1} = (\operatorname{Tr} M_n) E
$$

が得られます。

(ii) 式 (2) より $M_n = M_{n-1} M_{n-2}$ なので，$M_{n-2} = (M_{n-1})^{-1} M_n$，すなわち $(M_{n-2})^{-1} = (M_n)^{-1} M_{n-1}$ です。これと $M_{n+1} = M_n M_{n-1}$ を足し合わせ，(i)(c) を用います。

$$
\begin{aligned}
M_{n+1} + (M_{n-2})^{-1}
&= M_n M_{n-1} + (M_n)^{-1} M_{n-1} \\
&= \bigl(M_n + (M_n)^{-1}\bigr) M_{n-1} \\
&= (\operatorname{Tr} M_n) M_{n-1}
\end{aligned}
$$

したがって，

$$
\finalanswer{M_{n+1} + (M_{n-2})^{-1} = (\operatorname{Tr} M_n) M_{n-1}}
$$

この両辺のトレースをとり，(i)(b) の $\operatorname{Tr}(M_{n-2})^{-1} = \operatorname{Tr} M_{n-2} = x_{n-2}$ を用いると，

$$
\begin{aligned}
x_{n+1} + x_{n-2} &= x_n x_{n-1} \\
x_{n+1} &= x_n x_{n-1} - x_{n-2}
\end{aligned}
$$

となり，式 (3) が成り立ちます。

(iii) $I_{n+1} - I_n$ を計算して因数分解します。

$$
\begin{aligned}
I_{n+1} - I_n
&= \left(x_{n+3}^2 + x_{n+2}^2 + x_{n+1}^2 - x_{n+3} x_{n+2} x_{n+1}\right)
 - \left(x_{n+2}^2 + x_{n+1}^2 + x_n^2 - x_{n+2} x_{n+1} x_n\right) \\
&= \left(x_{n+3}^2 - x_n^2\right) - x_{n+2} x_{n+1}\left(x_{n+3} - x_n\right) \\
&= \left(x_{n+3} - x_n\right)\left(x_{n+3} + x_n - x_{n+2} x_{n+1}\right)
\end{aligned}
$$

式 (3) で $n$ を $n + 2$ に置き換えると $x_{n+3} = x_{n+2} x_{n+1} - x_n$，すなわち $x_{n+3} + x_n - x_{n+2} x_{n+1} = 0$ なので，$I_{n+1} - I_n = 0$ がすべての $n \ge 0$ で成り立ちます。よって $I_n = I_0$ は $n$ に依存しない定数です。

初期値 $x_0, x_1, x_2$ を計算します。

$$
\begin{aligned}
x_0 &= \operatorname{Tr} B \\
&= \sqrt{3} \\
x_1 &= \operatorname{Tr} A \\
&= \sqrt{2}
\end{aligned}
$$

$$
\begin{aligned}
M_2 &= AB \\
&= \frac{1}{2\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} \sqrt{3} & -1 \\ 1 & \sqrt{3} \end{pmatrix} \\
&= \frac{1}{2\sqrt{2}}\begin{pmatrix} \sqrt{3} - 1 & -1 - \sqrt{3} \\ \sqrt{3} + 1 & \sqrt{3} - 1 \end{pmatrix}
\end{aligned}
$$

より $x_2 = \operatorname{Tr} M_2 = \dfrac{\sqrt{3} - 1}{\sqrt{2}}$ です。これらを $I_0$ に代入します。

$$
\begin{aligned}
I_0 &= x_2^2 + x_1^2 + x_0^2 - x_2 x_1 x_0 \\
&= \frac{4 - 2\sqrt{3}}{2} + 2 + 3 - \frac{\sqrt{3} - 1}{\sqrt{2}}\cdot\sqrt{2}\cdot\sqrt{3} \\
&= (2 - \sqrt{3}) + 5 - (3 - \sqrt{3}) \\
&= 4
\end{aligned}
$$

したがって，

$$
\finalanswer{I_n = 4}
$$

### (2)
(i) $N = 3$ のとき $C = \begin{pmatrix} 0 & b_1 & 0 \\ b_1 & 0 & b_2 \\ 0 & b_2 & 0 \end{pmatrix}$ です。固有方程式 $\det(C - \lambda E) = 0$ を展開します。

$$
\begin{aligned}
\det\begin{pmatrix} -\lambda & b_1 & 0 \\ b_1 & -\lambda & b_2 \\ 0 & b_2 & -\lambda \end{pmatrix} &= -\lambda\left(\lambda^2 - b_2^2\right) - b_1(-b_1\lambda) \\
&= -\lambda\left(\lambda^2 - b_1^2 - b_2^2\right) \\
&= 0
\end{aligned}
$$

したがって，

$$
\finalanswer{\lambda = 0,\ \pm\sqrt{b_1^2 + b_2^2}}
$$

(ii) 固有値 $\lambda$ に対応する固有ベクトル $\boldsymbol{v} = (v_1, v_2, \dots, v_N)^{\mathrm{T}} \neq \mathbf{0}$ について，固有方程式 $C\boldsymbol{v} = \lambda\boldsymbol{v}$ を成分ごとに書きます。

$$
\begin{aligned}
b_1 v_2 &= \lambda v_1 \\
b_{i-1} v_{i-1} + b_i v_{i+1} &= \lambda v_i \qquad (i = 2, 3, \dots, N - 1) \\
b_{N-1} v_{N-1} &= \lambda v_N
\end{aligned}
$$

背理法で示します。もし $v_1 = 0$ であると仮定すると，第1式より $b_1 v_2 = 0$ となり，$b_1 > 0$ より $v_2 = 0$ です。次に $v_1 = v_2 = \dots = v_i = 0$ を仮定すると，$i$ 番目の式より $b_i v_{i+1} = \lambda v_i - b_{i-1} v_{i-1} = 0$ となり，$b_i > 0$ より $v_{i+1} = 0$ です。帰納的に $v_1 = v_2 = \dots = v_N = 0$，すなわち $\boldsymbol{v} = \mathbf{0}$ となって固有ベクトルであることに矛盾します。よって $v_1 \neq 0$ です。

(iii) ある固有値 $\lambda$ に対して2つの線形独立な固有ベクトル $\boldsymbol{u} = (u_1, \dots, u_N)^{\mathrm{T}},\ \boldsymbol{w} = (w_1, \dots, w_N)^{\mathrm{T}}$ が存在すると仮定します。(ii) より $u_1 \neq 0,\ w_1 \neq 0$ なので，線形結合

$$
\boldsymbol{v} = w_1\boldsymbol{u} - u_1\boldsymbol{w}
$$

を作ると，$\boldsymbol{u}, \boldsymbol{w}$ の線形独立性より $\boldsymbol{v} \neq \mathbf{0}$ かつ $C\boldsymbol{v} = \lambda\boldsymbol{v}$ なので，$\boldsymbol{v}$ は固有値 $\lambda$ の固有ベクトルです。ところが $\boldsymbol{v}$ の第1成分は $v_1 = w_1 u_1 - u_1 w_1 = 0$ となり，(ii) の結果に矛盾します。

したがって，すべての固有値の固有空間の次元は $1$ です。一方，$C$ は実対称行列なので直交行列によって対角化可能であり，固有値の特性多項式での重複度は，固有空間の次元と一致します。よって $C$ の $N$ 個の固有値はすべて互いに異なります。


