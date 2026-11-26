---
title: 東大理物 平成30年度 数学 第1問：特異値分解とムーア・ペンローズ擬似逆行列
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成30年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成30年度 数学 第1問：特異値分解とムーア・ペンローズ擬似逆行列

## 問題

2成分の行ベクトル $A = (a, b)$ について考える。ただし $a,\ b$ はゼロでない実数とする。また，以下では $T$ は行列の転置を表す。例えば，$A^T$ は $A$ を転置した列ベクトル $\begin{pmatrix} a \\ b \end{pmatrix}$ を表し，$A^T A$ は次のような2行2列の行列となる。

$$
A^T A = \begin{pmatrix} a^2 & ab \\ ab & b^2 \end{pmatrix}
$$

(1) $A^T A$ の全ての固有値と固有ベクトルを求めよ。

(2) 2成分の行ベクトル $B$ と2行2列の行列 $V$ を用いて $A = BV$ と分解する。ここで $B$ は，正の実数 $c$ を用いて $B = (c, 0)$ という形をとり，$V$ は実対称直交行列となるように選ぶ。$c$ と $V$ をそれぞれ $a,\ b$ を用いて表せ。

(3) $B\tilde{B} = 1$ を満たし，$\tilde{B}B$ が2行2列の実対称行列となるような列ベクトル $\tilde{B}$ を $c$ を用いて書け。

(4) $A\tilde{A} = 1$ を満たし，$\tilde{A}A$ が2行2列の実対称行列となるような列ベクトル $\tilde{A}$ は一意に定まる。$\tilde{A}$ を $\tilde{B}$ と $V$ を用いて書け。

つぎに，$n$ 成分の行ベクトル $A_n = (a_1, a_2, \dots, a_n)$ について考える。ただし $a_1, a_2, \dots, a_n$ はゼロでない実数であり，$n \ge 3$ とする。

(5) ゼロでない実数 $v$ に対して，$A_n X = v$ を満たす $n$ 成分の列ベクトル $X$ のうち，$\|X\|^2 = X^T X$ が最小となる $X = X_0$ を求めよ。また，このように求めた $X_0$ は，$v$ によらない列ベクトル $\tilde{A}_n$ を用いて $X_0 = v\tilde{A}_n$ と書ける。このとき，$A_n\tilde{A}_n = 1$ が成り立ち，$\tilde{A}_n A_n$ が実対称行列であることを示せ。

(6) 任意の行列 $M$ に対して，$M^T M$ のゼロでない固有値は，$M M^T$ の固有値となることを示せ。このことを用いて，$n$ 行 $n$ 列の行列 $A_n^T A_n$ の全ての固有値を求めよ。

(7) 一般には，重複する固有値を持つ行列は対角化可能であるとは限らない。$A_n^T A_n$ が対角化可能か否かを理由とともに述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成30年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
行列 $A$ は1行だけの行列なので，$A\boldsymbol{x}$ は $\boldsymbol{x}$ の $A$ の方向の成分だけで決まります。直交行列で座標を回して $A$ の方向を第1軸にそろえると，条件は第1成分だけにかかり，残りの成分は自由に選べることがわかります。

条件を満たす $\boldsymbol{x}$ の中でノルムが最小のものは，コーシー・シュワルツの不等式の等号条件から，$A$ の方向に平行なものになります。固有値が重なる対称行列でも，実対称行列は直交行列で対角化することができます。
</div>

### (1)
固有方程式 $\det(A^T A - \lambda I) = 0$ を解きます。

$$
\begin{aligned}
(a^2 - \lambda)(b^2 - \lambda) - a^2 b^2 &= 0 \\
\lambda^2 - (a^2 + b^2)\lambda &= 0 \\
\lambda\bigl(\lambda - (a^2 + b^2)\bigr) &= 0
\end{aligned}
$$

よって固有値は $\lambda_1 = a^2 + b^2$ と $\lambda_2 = 0$ です。それぞれの固有ベクトル $\boldsymbol{u} = \begin{pmatrix} x \\ y \end{pmatrix}$ を求めます。

- $\lambda_1 = a^2 + b^2$ のとき： $-b^2 x + ab y = 0 bx = ay$ より，$\boldsymbol{u}_1 = k_1\begin{pmatrix} a \\ b \end{pmatrix}$（$k_1 \neq 0$）。
- $\lambda_2 = 0$ のとき： $a^2 x + ab y = 0 ax + by = 0$ より，$\boldsymbol{u}_2 = k_2\begin{pmatrix} -b \\ a \end{pmatrix}$（$k_2 \neq 0$）。

したがって，固有値と固有ベクトルはそれぞれ

$$
\finalanswer{\lambda_1 = a^2 + b^2,\ \boldsymbol{u}_1 = k_1\begin{pmatrix} a \\ b \end{pmatrix};\qquad \lambda_2 = 0,\ \boldsymbol{u}_2 = k_2\begin{pmatrix} -b \\ a \end{pmatrix} \quad (k_1, k_2 \neq 0)}
$$

### (2)
$V$ が実直交行列で $VV^T=I$ を満たすので， $A A^T = B V V^T B^T = B B^T$ より $a^2 + b^2 = c^2$ です。$c > 0$ より $c = \sqrt{a^2 + b^2}$ となります。

$V = \begin{pmatrix} v_{11} & v_{12} \\ v_{21} & v_{22} \end{pmatrix}$ とおくと， $A = BV = (c v_{11}, c v_{12}) = (a, b)$ より，

$$
v_{11} = \frac{a}{\sqrt{a^2 + b^2}},\qquad v_{12} = \frac{b}{\sqrt{a^2 + b^2}}
$$

です。さらに $V$ が実対称なので $v_{21}=v_{12}$ です。また直交行列なので，第1行と第2行の内積が $0$ となる必要があります。

$$
\begin{aligned}
v_{11} v_{21} + v_{12} v_{22} &= \frac{ab}{a^2 + b^2} + \frac{b}{\sqrt{a^2 + b^2}} v_{22} \\
&= 0
\end{aligned}
$$

$b \neq 0$ より $v_{22} = -\dfrac{a}{\sqrt{a^2 + b^2}}$ が一意に定まります。$v_{21}^2+v_{22}^2=1$ も満たします。したがって，

$$
\finalanswer{c = \sqrt{a^2 + b^2},\qquad V = \frac{1}{\sqrt{a^2 + b^2}}\begin{pmatrix} a & b \\ b & -a \end{pmatrix}}
$$

### (3)
$\tilde{B} = \begin{pmatrix} x \\ y \end{pmatrix}$ とおきます。条件 $B\tilde{B} = cx = 1$ より $x = \dfrac{1}{c}$ です。

$$
\begin{aligned}
\tilde{B}B &= \begin{pmatrix} 1/c \\ y \end{pmatrix}(c, 0) \\
&= \begin{pmatrix} 1 & 0 \\ cy & 0 \end{pmatrix}
\end{aligned}
$$

これが実対称行列となる条件は $cy = 0$，すなわち $y = 0$ です。したがって，

$$
\finalanswer{\tilde{B} = \begin{pmatrix} 1/c \\ 0 \end{pmatrix}}
$$

### (4)
$\tilde A=V^T\tilde B$ とおきます。$V$ は実対称なので，$V^T\tilde B=V\tilde B$ です。$VV^T=I$ を使って条件を確認します。

$$
\begin{aligned}
A\tilde{A} &= (BV)(V^T\tilde{B}) \\
&= B\tilde{B} \\
&= 1
\end{aligned}
$$

$$
\begin{aligned}
(\tilde{A}A)^T &= (V^T \tilde{B} B V)^T \\
&= V^T (\tilde{B}B)^T V \\
&= V^T (\tilde{B}B) V \\
&= \tilde{A}A
\end{aligned}
$$

よって $\tilde{A} = V^T\tilde{B} = V\tilde{B}$ は両方の条件を満たします。一意性よりこれが求める $\tilde{A}$ です。したがって，

$$
\finalanswer{\tilde{A} = V^T\tilde{B} = V\tilde{B}}
$$

### (5)
コーシー・シュワルツの不等式より，$A_n X = v$ を満たす任意の列ベクトル $X$ に対して次式が成り立ちます。

$$
\begin{aligned}
v^2 &= \left(A_n X\right)^2 \\
&= \left(\sum_{i=1}^{n} a_i X_i\right)^2 \le \left(\sum_{i=1}^{n} a_i^2\right)\left(\sum_{i=1}^{n} X_i^2\right) \\
&= \left(A_n A_n^T\right)\|X\|^2
\end{aligned}
$$

よって $\|X\|^2 \ge \dfrac{v^2}{\sum_{i=1}^{n} a_i^2}$ であり，等号が成り立つのは $X$ が $A_n^T$ の実数倍 $X_0 = k A_n^T$ となるときに限ります。条件 $A_n X_0 = k\left(\sum_{i=1}^{n} a_i^2\right) = v$ より $k = \dfrac{v}{\sum_{i=1}^{n} a_i^2}$ なので，

$$
\begin{aligned}
X_0 &= \frac{v}{\sum_{i=1}^{n} a_i^2} A_n^T \\
&= v\tilde{A}_n
\end{aligned}
$$

となります。ここで，$\tilde{A}_n$ は次のようにおきました。

$$
\tilde{A}_n = \frac{1}{\sum_{i=1}^{n} a_i^2} A_n^T
$$

この $\tilde{A}_n$ について2つの性質を確認します。

$$
\begin{aligned}
A_n\tilde{A}_n &= \frac{A_n A_n^T}{\sum_{i=1}^{n} a_i^2} \\
&= \frac{\sum_{i=1}^{n} a_i^2}{\sum_{i=1}^{n} a_i^2} \\
&= 1
\end{aligned}
$$

$$
\begin{aligned}
\left(\tilde{A}_n A_n\right)^T &= \left(\frac{A_n^T A_n}{\sum_{i=1}^{n} a_i^2}\right)^T \\
&= \frac{A_n^T (A_n^T)^T}{\sum_{i=1}^{n} a_i^2} \\
&= \frac{A_n^T A_n}{\sum_{i=1}^{n} a_i^2} \\
&= \tilde{A}_n A_n
\end{aligned}
$$

よって $A_n\tilde{A}_n = 1$ が成り立ち，$\tilde{A}_n A_n$ は実対称行列です。したがって，

$$
\finalanswer{X_0 = \frac{v}{\sum_{i=1}^{n} a_i^2}\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}}
$$

### (6)
$\lambda \neq 0$ を $M^T M$ の固有値，対応する固有ベクトルを $\boldsymbol{u} \neq \mathbf{0}$ とします。固有方程式は $M^TM\boldsymbol u=\lambda\boldsymbol u$ です。もし $M\boldsymbol{u} = \mathbf{0}$ ならば $\lambda\boldsymbol{u} = M^T(M\boldsymbol{u}) = \mathbf{0}$ となり $\lambda \neq 0,\ \boldsymbol{u} \neq \mathbf{0}$ に矛盾するため，$M\boldsymbol{u} \neq \mathbf{0}$ です。

もとの固有方程式に左から $M$ を掛けると，

$$
\begin{aligned}
(M M^T)(M\boldsymbol{u}) &= M(M^T M\boldsymbol{u}) \\
&= \lambda(M\boldsymbol{u})
\end{aligned}
$$

となるため，$\lambda$ は $M M^T$ の固有値であり，$M\boldsymbol u$ が対応する固有ベクトルです。

$M=A_n$ とすると，$A_nA_n^T$ は成分が $\sum_{i=1}^na_i^2$ の $1\times1$ 行列です。$A_n^TA_n$ の固有ベクトル $A_n^T$ に対応する固有値は $\sum_{i=1}^na_i^2$ です。階数が1の実対称行列なので，残りの $n-1$ 個の固有値はすべて $0$ になります。したがって，

$$
\finalanswer{\lambda_1=\sum_{i=1}^n a_i^2,\qquad\lambda_j=0\quad(j=2,\ldots,n)}
$$

### (7)
$A_n^TA_n$ の転置を計算すると，

$$
\begin{aligned}
(A_n^TA_n)^T&=A_n^T(A_n^T)^T\\
&=A_n^TA_n
\end{aligned}
$$

なので，実対称行列です。実対称行列は，固有値が重なる場合でも直交行列で対角化することができます。したがって $A_n^TA_n$ は対角化可能です。


