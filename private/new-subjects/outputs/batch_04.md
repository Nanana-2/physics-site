===== FILE: 07linear_algebra/01/01_010.md =====
---
tags:
  - 基本
---

# 一次独立と基底

## 問題
$t$ を実数の定数とし，$\mathbb{R}^3$ の3つのベクトルを次のように定める。

$$
\boldsymbol{a}_1=\begin{pmatrix}1\\1\\0\end{pmatrix},\quad
\boldsymbol{a}_2=\begin{pmatrix}1\\0\\1\end{pmatrix},\quad
\boldsymbol{a}_3=\begin{pmatrix}0\\1\\t\end{pmatrix}
$$

以下の問いに答えよ。

(1) $\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3$ が一次独立になる $t$ の条件を求めよ。

(2) (1) の条件が満たされないとき，$\boldsymbol{a}_3$ を $\boldsymbol{a}_1$ と $\boldsymbol{a}_2$ の一次結合で表せ。

(3) $t=0$ のとき，$\boldsymbol{b}=(2,3,1)^{\mathrm{T}}$ を $\boldsymbol{b}=c_1\boldsymbol{a}_1+c_2\boldsymbol{a}_2+c_3\boldsymbol{a}_3$ と表す係数 $c_1,c_2,c_3$ を求めよ。

---

## 解答・解説

### (1)
3つのベクトルが一次独立であるとは，$c_1\boldsymbol{a}_1+c_2\boldsymbol{a}_2+c_3\boldsymbol{a}_3=\boldsymbol{0}$ を満たす係数が $c_1=c_2=c_3=0$ だけであることです。この式を成分ごとに書くと，次の連立方程式になります。

$$
\begin{aligned}
c_1+c_2&=0\\
c_1+c_3&=0\\
c_2+tc_3&=0
\end{aligned}
$$

1つ目と2つ目の式から $c_2=-c_1$，$c_3=-c_1$ です。これを3つ目の式 $c_2+tc_3=0$ に代入すると，

$$
\begin{aligned}
-c_1-tc_1&=0\\
(1+t)c_1&=0
\end{aligned}
$$

となります。$t\neq-1$ なら $c_1=0$ となり，$c_2=c_3=0$ も成り立ちます。$t=-1$ なら $c_1$ を0でない値にとれるので，一次独立ではありません。したがって，

$$
\finalanswer{t\neq-1}
$$

となります。$\mathbb{R}^3$ は3次元なので，一次独立な3つのベクトルはそのまま基底になります。この条件は，3つのベクトルが $\mathbb{R}^3$ の基底になる条件でもあります。

### (2)
$t=-1$ のとき，(1) の計算で $c_1=1$ とおくと，$c_2=-1$，$c_3=-1$ が解になります。

$$
\boldsymbol{a}_1-\boldsymbol{a}_2-\boldsymbol{a}_3=\boldsymbol{0}
$$

これを $\boldsymbol{a}_3$ について解くと，

$$
\finalanswer{\boldsymbol{a}_3=\boldsymbol{a}_1-\boldsymbol{a}_2}
$$

となります。成分で確かめると，

$$
\begin{aligned}
\boldsymbol{a}_1-\boldsymbol{a}_2&=\begin{pmatrix}1-1\\1-0\\0-1\end{pmatrix}\\
&=\begin{pmatrix}0\\1\\-1\end{pmatrix}
\end{aligned}
$$

であり，$t=-1$ のときの $\boldsymbol{a}_3$ と一致します。このとき3つのベクトルはすべて $\boldsymbol{a}_1,\boldsymbol{a}_2$ が張る平面の中にあるので，$\mathbb{R}^3$ 全体を張ることはできません。

### (3)
$t=0$ は (1) の条件を満たすので，3つのベクトルは基底であり，係数はただ1組に決まります。$\boldsymbol{b}=c_1\boldsymbol{a}_1+c_2\boldsymbol{a}_2+c_3\boldsymbol{a}_3$ を成分ごとに書くと，次の式になります。

$$
\begin{aligned}
c_1+c_2&=2\\
c_1+c_3&=3\\
c_2&=1
\end{aligned}
$$

3つ目の式から $c_2$ が決まり，それを1つ目の式に，さらに得られた $c_1$ を2つ目の式に代入します。

$$
\begin{aligned}
c_1&=2-c_2=1\\
c_3&=3-c_1=2
\end{aligned}
$$

したがって，

$$
\begin{aligned}
&\finalanswer{c_1=1}\\
&\finalanswer{c_2=1}\\
&\finalanswer{c_3=2}
\end{aligned}
$$

となります。係数の組 $(1,1,2)$ は，基底 $\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3$ に関する $\boldsymbol{b}$ の座標です。同じベクトルでも，基底を変えれば座標も変わります。

===== FILE: 07linear_algebra/01/01_020.md =====
---
tags:
  - 基本
---

# 部分空間と次元

## 問題
$\mathbb{R}^4$ のベクトル $\boldsymbol{x}=(x_1,x_2,x_3,x_4)^{\mathrm{T}}$ のうち，連立方程式

$$
\begin{aligned}
x_1+2x_2-x_3+x_4&=0\\
2x_1+4x_2-x_3+3x_4&=0
\end{aligned}
$$

を満たすもの全体を $W$，$x_1=x_2$ を満たすもの全体を $U$ とする。$W$ と $U$ はどちらも $\mathbb{R}^4$ の部分空間である。以下の問いに答えよ。

(1) $W$ の基底を1組求め，$W$ の次元を答えよ。

(2) $W\cap U$ の基底を1組求め，$W\cap U$ の次元を答えよ。

(3) $W+U=\{\boldsymbol{w}+\boldsymbol{u}\mid\boldsymbol{w}\in W,\ \boldsymbol{u}\in U\}$ の次元を求めよ。

---

## 解答・解説

### (1)
2つ目の式から1つ目の式の2倍を引いて，$x_1$ と $x_2$ を消去します。

$$
x_3+x_4=0
$$

この式と1つ目の式を使って，$x_1$ と $x_3$ を $x_2,x_4$ で表します。

$$
\begin{aligned}
x_3&=-x_4\\
x_1&=-2x_2+x_3-x_4\\
&=-2x_2-2x_4
\end{aligned}
$$

$x_2=s$，$x_4=r$ は自由に選べるので，解は次のように書けます。

$$
\boldsymbol{x}=s\begin{pmatrix}-2\\1\\0\\0\end{pmatrix}+r\begin{pmatrix}-2\\0\\-1\\1\end{pmatrix}
$$

2つのベクトルは第2成分と第4成分を見れば一次独立とわかります。したがって，

$$
\begin{aligned}
&\finalanswer{\boldsymbol{w}_1=(-2,1,0,0)^{\mathrm{T}},\quad\boldsymbol{w}_2=(-2,0,-1,1)^{\mathrm{T}}}\\
&\finalanswer{\dim W=2}
\end{aligned}
$$

となります。未知数が4個で，独立な方程式が2本なので，自由に選べる変数は $4-2=2$ 個です。

### (2)
$W$ のベクトルは $s\boldsymbol{w}_1+r\boldsymbol{w}_2$ と書けるので，その第1成分は $-2s-2r$，第2成分は $s$ です。これが $U$ に属する条件 $x_1=x_2$ を書くと，

$$
\begin{aligned}
-2s-2r&=s\\
3s&=-2r
\end{aligned}
$$

となります。$s=-2k$，$r=3k$ とおくと，この条件を満たすベクトルは次のようになります。

$$
\begin{aligned}
-2k\boldsymbol{w}_1+3k\boldsymbol{w}_2&=k\begin{pmatrix}4-6\\-2\\-3\\3\end{pmatrix}\\
&=k\begin{pmatrix}-2\\-2\\-3\\3\end{pmatrix}
\end{aligned}
$$

したがって，

$$
\begin{aligned}
&\finalanswer{\boldsymbol{v}=(-2,-2,-3,3)^{\mathrm{T}}}\\
&\finalanswer{\dim(W\cap U)=1}
\end{aligned}
$$

となります。$W$ に条件を1つ加えたので，次元が1つ下がっています。

### (3)
$U$ は1本の方程式 $x_1-x_2=0$ で定まるので，次元は $4-1=3$ です。部分空間の次元公式を使います。

$$
\begin{aligned}
\dim(W+U)&=\dim W+\dim U-\dim(W\cap U)\\
&=2+3-1
\end{aligned}
$$

したがって，

$$
\finalanswer{\dim(W+U)=4}
$$

となり，$W+U=\mathbb{R}^4$ です。$\boldsymbol{w}_1$ は第1成分と第2成分が異なるので $U$ に属しません。そのため $W+U$ は3次元の $U$ より真に大きく，4次元になることからも確かめられます。

===== FILE: 07linear_algebra/01/01_030.md =====
---
tags:
  - 基本
---

# 線形写像の表現行列

## 問題
定ベクトル $\boldsymbol{\omega}=(\omega_1,\omega_2,\omega_3)^{\mathrm{T}}$ を用いて，線形写像 $f:\mathbb{R}^3\to\mathbb{R}^3$ を $f(\boldsymbol{x})=\boldsymbol{\omega}\times\boldsymbol{x}$ で定める。標準基底 $\boldsymbol{e}_x,\boldsymbol{e}_y,\boldsymbol{e}_z$ に関する $f$ の表現行列を $A$ とする。すなわち，すべての $\boldsymbol{x}$ に対して $f(\boldsymbol{x})=A\boldsymbol{x}$ が成り立つ。$\omega=|\boldsymbol{\omega}|$ とし，$I$ を3次の単位行列とする。$\boldsymbol{\omega}\boldsymbol{\omega}^{\mathrm{T}}$ は $(i,j)$ 成分が $\omega_i\omega_j$ の3次正方行列である。以下の問いに答えよ。

(1) $A$ を求めよ。

(2) 合成写像 $f\circ f$ の表現行列 $A^2$ を，$\boldsymbol{\omega}\boldsymbol{\omega}^{\mathrm{T}}$，$\omega$，$I$ で表せ。

(3) $A^3$ を $A$ と $\omega$ で表せ。

---

## 解答・解説

### (1)
表現行列の第 $j$ 列は，第 $j$ の基底ベクトルの像です。$f(\boldsymbol{e}_x)=A\boldsymbol{e}_x$ は $A$ の第1列に等しいからです。外積を成分で計算すると，

$$
\begin{aligned}
\boldsymbol{\omega}\times\boldsymbol{e}_x&=(0,\ \omega_3,\ -\omega_2)^{\mathrm{T}}\\
\boldsymbol{\omega}\times\boldsymbol{e}_y&=(-\omega_3,\ 0,\ \omega_1)^{\mathrm{T}}\\
\boldsymbol{\omega}\times\boldsymbol{e}_z&=(\omega_2,\ -\omega_1,\ 0)^{\mathrm{T}}
\end{aligned}
$$

となります。これらを順に列として並べると，

$$
\finalanswer{A=\begin{pmatrix}0&-\omega_3&\omega_2\\\omega_3&0&-\omega_1\\-\omega_2&\omega_1&0\end{pmatrix}}
$$

となります。$A$ は $A^{\mathrm{T}}=-A$ を満たす交代行列です。剛体の各点の速度 $\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{r}$ は，この行列を位置ベクトルに掛けて得られます。

### (2)
合成写像の表現行列は表現行列の積なので，$f(f(\boldsymbol{x}))=A^2\boldsymbol{x}$ です。ベクトル三重積の公式 $\boldsymbol{a}\times(\boldsymbol{b}\times\boldsymbol{c})=\boldsymbol{b}(\boldsymbol{a}\cdot\boldsymbol{c})-\boldsymbol{c}(\boldsymbol{a}\cdot\boldsymbol{b})$ を使います。$\boldsymbol{\omega}(\boldsymbol{\omega}\cdot\boldsymbol{x})=\boldsymbol{\omega}\boldsymbol{\omega}^{\mathrm{T}}\boldsymbol{x}$ に注意すると，

$$
\begin{aligned}
f(f(\boldsymbol{x}))&=\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{x})\\
&=\boldsymbol{\omega}(\boldsymbol{\omega}\cdot\boldsymbol{x})-\omega^2\boldsymbol{x}\\
&=\left(\boldsymbol{\omega}\boldsymbol{\omega}^{\mathrm{T}}-\omega^2I\right)\boldsymbol{x}
\end{aligned}
$$

となります。これがすべての $\boldsymbol{x}$ について成り立つので，

$$
\finalanswer{A^2=\boldsymbol{\omega}\boldsymbol{\omega}^{\mathrm{T}}-\omega^2I}
$$

となります。(1) の $A$ を直接2乗すると，たとえば $(1,1)$ 成分は $-\omega_2^{\,2}-\omega_3^{\,2}$ です。これは右辺の $(1,1)$ 成分 $\omega_1^{\,2}-\omega^2$ と一致します。剛体の回転では，$\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$ は回転軸に向かう向心加速度を表します。

### (3)
(2) の結果に左から $A$ を掛けます。$A\boldsymbol{\omega}=\boldsymbol{\omega}\times\boldsymbol{\omega}=\boldsymbol{0}$ なので，第1項は消えます。

$$
\begin{aligned}
A^3&=A\boldsymbol{\omega}\boldsymbol{\omega}^{\mathrm{T}}-\omega^2A\\
&=(A\boldsymbol{\omega})\boldsymbol{\omega}^{\mathrm{T}}-\omega^2A
\end{aligned}
$$

したがって，

$$
\finalanswer{A^3=-\omega^2A}
$$

となります。これより，$A$ の高次のべきはすべて $A$ か $A^2$ の定数倍になります。この性質を使うと，$A$ の指数関数として回転行列を有限個の項で書き表せます。

===== FILE: 07linear_algebra/01/01_040.md =====
---
tags:
  - 標準
---

# 核と像，次元定理

## 問題
線形写像 $f:\mathbb{R}^4\to\mathbb{R}^3$ を $f(\boldsymbol{x})=A\boldsymbol{x}$ で定める。ここで

$$
A=\begin{pmatrix}1&2&0&1\\2&4&1&4\\1&2&1&3\end{pmatrix}
$$

である。核を $\operatorname{Ker}f=\{\boldsymbol{x}\in\mathbb{R}^4\mid f(\boldsymbol{x})=\boldsymbol{0}\}$，像を $\operatorname{Im}f=\{f(\boldsymbol{x})\mid\boldsymbol{x}\in\mathbb{R}^4\}$ とする。以下の問いに答えよ。

(1) $\operatorname{Ker}f$ の基底を1組求めよ。

(2) $\operatorname{Im}f$ の基底を1組求めよ。

(3) $\boldsymbol{b}=(b_1,b_2,b_3)^{\mathrm{T}}$ が $\operatorname{Im}f$ に属するための $b_1,b_2,b_3$ の条件を求めよ。

---

## 解答・解説

### (1)
行基本変形をしても $A\boldsymbol{x}=\boldsymbol{0}$ の解は変わらないので，$A$ を簡単な形に変形します。第2行から第1行の2倍を，第3行から第1行を引き，さらに第3行から第2行を引きます。

$$
\begin{pmatrix}1&2&0&1\\2&4&1&4\\1&2&1&3\end{pmatrix}
\to
\begin{pmatrix}1&2&0&1\\0&0&1&2\\0&0&1&2\end{pmatrix}
\to
\begin{pmatrix}1&2&0&1\\0&0&1&2\\0&0&0&0\end{pmatrix}
$$

残った2本の式から，$x_1$ と $x_3$ を $x_2=s$，$x_4=r$ で表します。

$$
\begin{aligned}
x_1&=-2s-r\\
x_3&=-2r
\end{aligned}
$$

したがって，解は $s(-2,1,0,0)^{\mathrm{T}}+r(-1,0,-2,1)^{\mathrm{T}}$ と書けて，

$$
\finalanswer{\boldsymbol{k}_1=(-2,1,0,0)^{\mathrm{T}},\quad\boldsymbol{k}_2=(-1,0,-2,1)^{\mathrm{T}}}
$$

となります。$\dim\operatorname{Ker}f=2$ です。

### (2)
$A$ の列を $\boldsymbol{a}_1,\ldots,\boldsymbol{a}_4$ とすると，$f(\boldsymbol{x})=x_1\boldsymbol{a}_1+\cdots+x_4\boldsymbol{a}_4$ です。そのため像は4つの列が張る空間です。(1) の核のベクトルは列の間の一次関係を与えます。

$$
\begin{aligned}
A\boldsymbol{k}_1=\boldsymbol{0}\quad&\Longrightarrow\quad\boldsymbol{a}_2=2\boldsymbol{a}_1\\
A\boldsymbol{k}_2=\boldsymbol{0}\quad&\Longrightarrow\quad\boldsymbol{a}_4=\boldsymbol{a}_1+2\boldsymbol{a}_3
\end{aligned}
$$

$\boldsymbol{a}_2$ と $\boldsymbol{a}_4$ は $\boldsymbol{a}_1,\boldsymbol{a}_3$ で表せます。$\boldsymbol{a}_1$ と $\boldsymbol{a}_3$ は比例しないので一次独立です。したがって，

$$
\finalanswer{\boldsymbol{a}_1=(1,2,1)^{\mathrm{T}},\quad\boldsymbol{a}_3=(0,1,1)^{\mathrm{T}}}
$$

となります。$\dim\operatorname{Im}f=2$ で，これは $A$ の階数に等しくなります。(1) と合わせると次の関係が成り立ちます。

$$
\dim\operatorname{Ker}f+\dim\operatorname{Im}f=2+2=4
$$

これは定義域 $\mathbb{R}^4$ の次元で，次元定理と一致します。

### (3)
$\boldsymbol{b}$ が像に属するのは，$\boldsymbol{b}=p\boldsymbol{a}_1+q\boldsymbol{a}_3$ と書けるときです。成分ごとに書くと，

$$
\begin{aligned}
b_1&=p\\
b_2&=2p+q\\
b_3&=p+q
\end{aligned}
$$

となります。2つ目の式から1つ目の式を引くと $b_2-b_1=p+q$ で，これは3つ目の式の右辺と同じです。$p,q$ を消去すると，

$$
\finalanswer{b_1-b_2+b_3=0}
$$

となります。像は $\mathbb{R}^3$ の中で原点を通る平面で，$(1,-1,1)^{\mathrm{T}}$ はその法線ベクトルです。連立方程式 $A\boldsymbol{x}=\boldsymbol{b}$ が解をもつのは，$\boldsymbol{b}$ がこの条件を満たすときに限られます。

===== FILE: 07linear_algebra/01/01_050.md =====
---
tags:
  - 標準
---

# 基底変換と表現行列の変化

## 問題
$\mathbb{R}^2$ の線形写像 $f(\boldsymbol{x})=A\boldsymbol{x}$ を考える。$A$ は標準基底に関する表現行列である。$\mathbb{R}^2$ の別の基底 $\boldsymbol{u}_1,\boldsymbol{u}_2$ をとり，これらを列に並べた行列を $P=(\boldsymbol{u}_1\ \boldsymbol{u}_2)$ とする。基底 $\boldsymbol{u}_1,\boldsymbol{u}_2$ に関する $f$ の表現行列 $B=(b_{ij})$ を

$$
f(\boldsymbol{u}_j)=b_{1j}\boldsymbol{u}_1+b_{2j}\boldsymbol{u}_2\quad(j=1,2)
$$

で定義する。$I$ を2次の単位行列とする。以下の問いに答えよ。

(1) $B=P^{-1}AP$ となることを示せ。

(2) 次の場合に $B$ を求めよ。

$$
A=\begin{pmatrix}2&1\\1&2\end{pmatrix},\quad
\boldsymbol{u}_1=\begin{pmatrix}1\\0\end{pmatrix},\quad
\boldsymbol{u}_2=\begin{pmatrix}1\\1\end{pmatrix}
$$

(3) 一般の $A$ と $P$ について，任意の数 $\lambda$ に対して $\det(B-\lambda I)=\det(A-\lambda I)$ となることを示せ。

---

## 解答・解説

### (1)
$B$ の第 $j$ 列を $\boldsymbol{b}_j=(b_{1j},b_{2j})^{\mathrm{T}}$ とします。定義の右辺は $P$ の列の一次結合なので，$P\boldsymbol{b}_j$ と書けます。行列の積 $AP$ の第 $j$ 列は $A\boldsymbol{u}_j=f(\boldsymbol{u}_j)$ なので，

$$
\begin{aligned}
AP&=\begin{pmatrix}f(\boldsymbol{u}_1)&f(\boldsymbol{u}_2)\end{pmatrix}\\
&=\begin{pmatrix}P\boldsymbol{b}_1&P\boldsymbol{b}_2\end{pmatrix}\\
&=PB
\end{aligned}
$$

となります。$P$ の列は基底なので一次独立で，$P$ は正則です。両辺に左から $P^{-1}$ を掛けると，

$$
\finalanswer{B=P^{-1}AP}
$$

となります。ベクトル $\boldsymbol{x}$ の新しい基底での座標を $\boldsymbol{x}'$ とすると $\boldsymbol{x}=P\boldsymbol{x}'$ です。$P^{-1}AP$ は，座標を標準基底に直し，$A$ を掛け，新しい基底の座標に戻す操作を表します。

### (2)
$P$ とその逆行列は次のとおりです。

$$
P=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
P^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}
$$

先に $AP$ を計算し，左から $P^{-1}$ を掛けます。

$$
\begin{aligned}
AP&=\begin{pmatrix}2&3\\1&3\end{pmatrix}\\
P^{-1}AP&=\begin{pmatrix}2-1&3-3\\1&3\end{pmatrix}
\end{aligned}
$$

したがって，

$$
\finalanswer{B=\begin{pmatrix}1&0\\1&3\end{pmatrix}}
$$

となります。定義からも確かめます。$f(\boldsymbol{u}_1)=(2,1)^{\mathrm{T}}=\boldsymbol{u}_1+\boldsymbol{u}_2$ と $f(\boldsymbol{u}_2)=(3,3)^{\mathrm{T}}=3\boldsymbol{u}_2$ の係数は，$B$ の第1列と第2列に一致します。

### (3)
$I=P^{-1}P$ を使うと，$B-\lambda I$ を $P^{-1}$ と $P$ ではさんだ形に書けます。

$$
\begin{aligned}
B-\lambda I&=P^{-1}AP-\lambda P^{-1}P\\
&=P^{-1}(A-\lambda I)P
\end{aligned}
$$

行列式は積を積に移し，$\det P^{-1}\det P=\det I=1$ です。したがって，

$$
\begin{aligned}
\det(B-\lambda I)&=\det P^{-1}\det(A-\lambda I)\det P\\
&=\finalanswer{\det(A-\lambda I)}
\end{aligned}
$$

となります。固有多項式が同じなので，固有値，トレース，行列式は基底の選び方によりません。(2) でも，トレースは $A$ と $B$ のどちらも4，行列式はどちらも3です。

===== FILE: 07linear_algebra/01/01_060.md =====
---
tags:
  - 標準
---

# 多項式空間の線形写像

## 問題
実数係数で次数が3以下の $x$ の多項式全体を $V$ とし，基底 $1,x,x^2,x^3$ をとる。多項式 $p(x)=c_0+c_1x+c_2x^2+c_3x^3$ を列ベクトル $(c_0,c_1,c_2,c_3)^{\mathrm{T}}$ で表す。線形写像 $g:V\to V$ の表現行列とは，$p$ の列ベクトルに掛けると $g(p)$ の列ベクトルを与える4次正方行列である。$a$ を実数の定数，$I$ を4次の単位行列とする。以下の問いに答えよ。

(1) 微分 $\mathcal{D}:p(x)\mapsto p'(x)$ の表現行列 $D$ を求めよ。

(2) 平行移動 $\mathcal{T}_a:p(x)\mapsto p(x+a)$ の表現行列 $T_a$ を求めよ。

(3) 次式が成り立つことを示せ。

$$
T_a=I+aD+\frac{a^2}{2!}D^2+\frac{a^3}{3!}D^3
$$

---

## 解答・解説

### (1)
表現行列の第 $j$ 列は，第 $j$ の基底の像の列ベクトルです。各基底を微分すると，

$$
\begin{aligned}
\mathcal{D}(1)&=0\\
\mathcal{D}(x)&=1\\
\mathcal{D}(x^2)&=2x\\
\mathcal{D}(x^3)&=3x^2
\end{aligned}
$$

となります。これらの係数を列として並べると，

$$
\finalanswer{D=\begin{pmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\\0&0&0&0\end{pmatrix}}
$$

となります。微分は次数を1つ下げるので，$D$ は対角成分のすぐ上だけに成分をもちます。4回微分すると3次以下の多項式はすべて0になるので，$D^4=O$ です。

### (2)
各基底を $x+a$ に置き換えて展開し，$1,x,x^2,x^3$ の係数を読み取ります。

$$
\begin{aligned}
\mathcal{T}_a(1)&=1\\
\mathcal{T}_a(x)&=a+x\\
\mathcal{T}_a(x^2)&=a^2+2ax+x^2\\
\mathcal{T}_a(x^3)&=a^3+3a^2x+3ax^2+x^3
\end{aligned}
$$

これらの係数を列として並べると，

$$
\finalanswer{T_a=\begin{pmatrix}1&a&a^2&a^3\\0&1&2a&3a^2\\0&0&1&3a\\0&0&0&1\end{pmatrix}}
$$

となります。各列には二項係数が並んでいます。

### (3)
(1) の $D$ から $D^2$ と $D^3$ を計算します。$D^2$ は2回の微分，$D^3$ は3回の微分を表すので，基底の像から直接求められます。$\mathcal{D}^2(x^2)=2$，$\mathcal{D}^2(x^3)=6x$，$\mathcal{D}^3(x^3)=6$ なので，

$$
\begin{aligned}
D^2&=\begin{pmatrix}0&0&2&0\\0&0&0&6\\0&0&0&0\\0&0&0&0\end{pmatrix}\\
D^3&=\begin{pmatrix}0&0&0&6\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
\end{aligned}
$$

となります。右辺の各成分を足し合わせます。$aD$ は対角のすぐ上に $a,2a,3a$ を与え，$a^2D^2/2$ はその1つ上に $a^2,3a^2$ を，$a^3D^3/6$ は右上の角に $a^3$ を与えます。

$$
I+aD+\frac{a^2}{2}D^2+\frac{a^3}{6}D^3=\begin{pmatrix}1&a&a^2&a^3\\0&1&2a&3a^2\\0&0&1&3a\\0&0&0&1\end{pmatrix}
$$

これは (2) の $T_a$ と一致するので，

$$
\finalanswer{T_a=I+aD+\frac{a^2}{2!}D^2+\frac{a^3}{3!}D^3}
$$

が成り立ちます。これは $p(x+a)$ のテイラー展開を行列で書いたもので，$D^4=O$ のため有限個の項で終わります。右辺は $e^{aD}$ にあたり，微分演算子が平行移動を生み出すことを表しています。

===== FILE: 07linear_algebra/02/02_010.md =====
---
tags:
  - 基本
---

# 行列式の性質

## 問題
行列式の基本変形を用いて，次の行列式を計算する。以下の問いに答えよ。

(1) 次の行列式を求めよ。

$$
\begin{vmatrix}1&1&1&1\\1&2&2&2\\1&2&3&3\\1&2&3&4\end{vmatrix}
$$

(2) $x$ を変数として，次の行列式を因数分解した形で求めよ。

$$
\begin{vmatrix}x&1&1&1\\1&x&1&1\\1&1&x&1\\1&1&1&x\end{vmatrix}
$$

(3) $n\ge2$ とする。対角成分がすべて $x$ で，それ以外の成分がすべて1である $n$ 次正方行列の行列式を求めよ。

---

## 解答・解説

### (1)
行列式は，ある行に別の行の定数倍を加えても変わりません。また，三角行列の行列式は対角成分の積です。そこで，第4行から第3行を引き，次に第3行から第2行を，最後に第2行から第1行を引きます。この順に行うと，引く側の行はどれもまだ変形されていない元の行です。

$$
\begin{vmatrix}1&1&1&1\\1&2&2&2\\1&2&3&3\\1&2&3&4\end{vmatrix}
=\begin{vmatrix}1&1&1&1\\0&1&1&1\\0&0&1&1\\0&0&0&1\end{vmatrix}
$$

右辺は上三角行列で，対角成分はすべて1です。したがって，

$$
\finalanswer{\begin{vmatrix}1&1&1&1\\1&2&2&2\\1&2&3&3\\1&2&3&4\end{vmatrix}=1}
$$

となります。

### (2)
行列式は転置しても変わらないので，列についても行と同じ性質が成り立ちます。第2列から第4列までを第1列に加えると，第1列はすべて $x+3$ になります。そこから共通因子 $x+3$ をくくり出します。

$$
\begin{vmatrix}x&1&1&1\\1&x&1&1\\1&1&x&1\\1&1&1&x\end{vmatrix}
=(x+3)\begin{vmatrix}1&1&1&1\\1&x&1&1\\1&1&x&1\\1&1&1&x\end{vmatrix}
$$

次に，第2行から第4行のそれぞれから第1行を引くと，上三角行列になります。

$$
\begin{vmatrix}1&1&1&1\\1&x&1&1\\1&1&x&1\\1&1&1&x\end{vmatrix}
=\begin{vmatrix}1&1&1&1\\0&x-1&0&0\\0&0&x-1&0\\0&0&0&x-1\end{vmatrix}
$$

対角成分の積をとると，

$$
\finalanswer{\begin{vmatrix}x&1&1&1\\1&x&1&1\\1&1&x&1\\1&1&1&x\end{vmatrix}=(x+3)(x-1)^3}
$$

となります。$x=1$ ではすべての行が等しく，$x=-3$ では各行の和が0になるので，どちらの場合も行列式が0になることと一致します。

### (3)
(2) と同じ手順を $n$ 次で行います。第2列から第 $n$ 列までを第1列に加えると，第1列はすべて $x+n-1$ になります。それをくくり出してから，第2行以降のそれぞれから第1行を引くと，対角成分が $1,x-1,\ldots,x-1$ の上三角行列になります。$x-1$ は $n-1$ 個並ぶので，

$$
\finalanswer{\det=(x+n-1)(x-1)^{n-1}}
$$

となります。$n=2$ では $(x+1)(x-1)=x^2-1$ で，2次の行列式を直接計算した値と一致します。この行列は $(x-1)I$ にすべての成分が1の行列を加えたものです。その固有値は $x+n-1$ が1つと $x-1$ が $n-1$ 個で，行列式はそれらの積になっています。

===== FILE: 07linear_algebra/02/02_020.md =====
---
tags:
  - 基本
---

# 余因子展開と逆行列

## 問題
$n$ 次正方行列 $A=(a_{ij})$ の $(i,j)$ 余因子を $\Delta_{ij}=(-1)^{i+j}M_{ij}$ とする。$M_{ij}$ は，$A$ から第 $i$ 行と第 $j$ 列を除いてできる $n-1$ 次の行列式である。$(i,j)$ 成分が $\Delta_{ji}$ である行列を余因子行列とよび，$\tilde{A}$ と書く。$I$ を単位行列とする。以下の問いに答えよ。

(1) $A\tilde{A}=(\det A)I$ となることを示せ。

(2) 次の行列 $A$ の余因子行列 $\tilde{A}$ を求めよ。

$$
A=\begin{pmatrix}1&2&0\\0&1&1\\1&0&1\end{pmatrix}
$$

(3) (2) の $A$ の逆行列 $A^{-1}$ を求めよ。

---

## 解答・解説

### (1)
$A\tilde{A}$ の $(i,j)$ 成分は，$\tilde{A}$ の $(k,j)$ 成分が $\Delta_{jk}$ であることから，次のように書けます。

$$
(A\tilde{A})_{ij}=\sum_{k=1}^{n}a_{ik}\Delta_{jk}
$$

$i=j$ のとき，これは第 $i$ 行についての余因子展開そのもので，$\det A$ に等しくなります。$i\neq j$ のときは，$A$ の第 $j$ 行を第 $i$ 行で置き換えた行列 $A'$ を考えます。$A'$ の第 $j$ 行の余因子は第 $j$ 行を含まないので，$A$ の $\Delta_{jk}$ と同じです。そのため上の和は $\det A'$ を第 $j$ 行で展開したものになります。$A'$ は等しい2つの行をもつので，その行列式は0です。まとめると，

$$
\sum_{k=1}^{n}a_{ik}\Delta_{jk}=\delta_{ij}\det A
$$

となります。$\delta_{ij}$ は $i=j$ で1，$i\neq j$ で0の記号です。したがって，

$$
\finalanswer{A\tilde{A}=(\det A)I}
$$

が成り立ちます。$\det A\neq0$ なら，$\tilde{A}/\det A$ が $A$ の逆行列になります。

### (2)
各成分の小行列式を計算し，符号 $(-1)^{i+j}$ を付けます。第1行の余因子は次のとおりです。

$$
\begin{aligned}
\Delta_{11}&=+\begin{vmatrix}1&1\\0&1\end{vmatrix}=1\\
\Delta_{12}&=-\begin{vmatrix}0&1\\1&1\end{vmatrix}=1\\
\Delta_{13}&=+\begin{vmatrix}0&1\\1&0\end{vmatrix}=-1
\end{aligned}
$$

第2行と第3行も同じように計算します。

$$
\begin{aligned}
\Delta_{21}&=-\begin{vmatrix}2&0\\0&1\end{vmatrix}=-2\\
\Delta_{22}&=+\begin{vmatrix}1&0\\1&1\end{vmatrix}=1\\
\Delta_{23}&=-\begin{vmatrix}1&2\\1&0\end{vmatrix}=2\\
\Delta_{31}&=+\begin{vmatrix}2&0\\1&1\end{vmatrix}=2\\
\Delta_{32}&=-\begin{vmatrix}1&0\\0&1\end{vmatrix}=-1\\
\Delta_{33}&=+\begin{vmatrix}1&2\\0&1\end{vmatrix}=1
\end{aligned}
$$

余因子行列の $(i,j)$ 成分は $\Delta_{ji}$ なので，余因子を転置して並べます。したがって，

$$
\finalanswer{\tilde{A}=\begin{pmatrix}1&-2&2\\1&1&-1\\-1&2&1\end{pmatrix}}
$$

となります。

### (3)
$\det A$ を第1行で余因子展開すると，(2) の余因子を使って次のように求まります。

$$
\begin{aligned}
\det A&=1\cdot\Delta_{11}+2\cdot\Delta_{12}+0\cdot\Delta_{13}\\
&=1+2=3
\end{aligned}
$$

(1) から $A^{-1}=\tilde{A}/\det A$ です。したがって，

$$
\finalanswer{A^{-1}=\frac{1}{3}\begin{pmatrix}1&-2&2\\1&1&-1\\-1&2&1\end{pmatrix}}
$$

となります。$A\tilde{A}$ を計算すると，対角成分はすべて3，それ以外は0になり，(1) の関係と一致します。

===== FILE: 07linear_algebra/02/02_030.md =====
---
tags:
  - 基本
---

# クラメルの公式

## 問題
$n$ 次正方行列 $A$ は $\det A\neq0$ を満たすとし，連立一次方程式 $A\boldsymbol{x}=\boldsymbol{b}$ を考える。$A$ の第 $i$ 列を $\boldsymbol{b}$ で置き換えた行列を $A_i$ とする。$A$ の $(i,j)$ 余因子を $\Delta_{ij}$ とし，$(i,j)$ 成分が $\Delta_{ji}$ である余因子行列 $\tilde{A}$ を用いた逆行列の表示 $A^{-1}=\tilde{A}/\det A$ を用いてよい。以下の問いに答えよ。

(1) 解の第 $i$ 成分が $x_i=\det A_i/\det A$ となることを示せ。

(2) (1) の結果を用いて，次の連立方程式を解け。

$$
\begin{aligned}
x+y+z&=6\\
x+2y+3z&=14\\
x+4y+9z&=36
\end{aligned}
$$

---

## 解答・解説

### (1)
$\det A\neq0$ なので解は $\boldsymbol{x}=A^{-1}\boldsymbol{b}$ です。逆行列の表示を使い，第 $i$ 成分を書き出します。$\tilde{A}$ の $(i,k)$ 成分は $\Delta_{ki}$ です。

$$
\begin{aligned}
x_i&=\frac{1}{\det A}\left(\tilde{A}\boldsymbol{b}\right)_i\\
&=\frac{1}{\det A}\sum_{k=1}^{n}b_k\Delta_{ki}
\end{aligned}
$$

右辺の和は，$A_i$ の行列式を第 $i$ 列で余因子展開したものです。$A_i$ の第 $i$ 列の成分は $b_k$ で，第 $i$ 列の余因子は第 $i$ 列を含まないので $A$ の $\Delta_{ki}$ と同じだからです。したがって，

$$
\finalanswer{x_i=\frac{\det A_i}{\det A}}
$$

となります。これをクラメルの公式とよびます。

### (2)
係数行列は $A=\begin{pmatrix}1&1&1\\1&2&3\\1&4&9\end{pmatrix}$ です。第2行と第3行から第1行を引いてから，第1列で展開します。

$$
\begin{aligned}
\det A&=\begin{vmatrix}1&1&1\\0&1&2\\0&3&8\end{vmatrix}\\
&=1\cdot8-2\cdot3=2
\end{aligned}
$$

次に，第1列，第2列，第3列をそれぞれ $(6,14,36)^{\mathrm{T}}$ で置き換えた行列式を，第1行で展開します。

$$
\begin{aligned}
\det A_1&=\begin{vmatrix}6&1&1\\14&2&3\\36&4&9\end{vmatrix}\\
&=6(18-12)-(126-108)+(56-72)\\
&=36-18-16=2
\end{aligned}
$$

$$
\begin{aligned}
\det A_2&=\begin{vmatrix}1&6&1\\1&14&3\\1&36&9\end{vmatrix}\\
&=(126-108)-6(9-3)+(36-14)\\
&=18-36+22=4
\end{aligned}
$$

$$
\begin{aligned}
\det A_3&=\begin{vmatrix}1&1&6\\1&2&14\\1&4&36\end{vmatrix}\\
&=(72-56)-(36-14)+6(4-2)\\
&=16-22+12=6
\end{aligned}
$$

これらを (1) の式に代入します。したがって，

$$
\begin{aligned}
&\finalanswer{x=\frac{2}{2}=1}\\
&\finalanswer{y=\frac{4}{2}=2}\\
&\finalanswer{z=\frac{6}{2}=3}
\end{aligned}
$$

となります。3つ目の式に代入すると $1+8+27=36$ となり，満たされています。この係数行列は，2-6 で扱うヴァンデルモンドの行列を転置したものです。

===== FILE: 07linear_algebra/02/02_040.md =====
---
tags:
  - 標準
---

# 階数と解の存在

## 問題
$a,b$ を実数の定数として，$x,y,z$ についての連立一次方程式

$$
\begin{aligned}
x+y+z&=1\\
x+2y+3z&=2\\
x+3y+az&=b
\end{aligned}
$$

を考える。係数行列を $A$，拡大係数行列を $(A\mid\boldsymbol{b})$ とする。以下の問いに答えよ。

(1) $A$ の階数を求めよ。

(2) 解が存在しないための $a,b$ の条件を求めよ。

(3) 解が無数に存在するときの一般解を求めよ。

---

## 解答・解説

### (1)
拡大係数行列に行基本変形を行います。第2行と第3行から第1行を引き，さらに第3行から第2行の2倍を引きます。

$$
\left(\begin{array}{ccc|c}1&1&1&1\\1&2&3&2\\1&3&a&b\end{array}\right)
\to
\left(\begin{array}{ccc|c}1&1&1&1\\0&1&2&1\\0&2&a-1&b-1\end{array}\right)
\to
\left(\begin{array}{ccc|c}1&1&1&1\\0&1&2&1\\0&0&a-5&b-3\end{array}\right)
$$

縦線の左側が $A$ を変形したものです。第3行の左側が0でないのは $a\neq5$ のときです。したがって，

$$
\begin{aligned}
&\finalanswer{\operatorname{rank}A=3\quad(a\neq5)}\\
&\finalanswer{\operatorname{rank}A=2\quad(a=5)}
\end{aligned}
$$

となります。

### (2)
連立方程式が解をもつのは，$\operatorname{rank}A=\operatorname{rank}(A\mid\boldsymbol{b})$ のときです。$a\neq5$ のときは，どちらの階数も3になるので，解はただ1つ存在します。$a=5$ のときは，(1) の変形の第3行が次の式を表します。

$$
0=b-3
$$

$b\neq3$ ならこの式は成り立たず，$\operatorname{rank}(A\mid\boldsymbol{b})=3$ が $\operatorname{rank}A=2$ より大きくなります。したがって，

$$
\finalanswer{a=5,\ b\neq3}
$$

となります。このとき，3つ目の式の左辺は1つ目と2つ目の式の左辺の一次結合になりますが，右辺はそれと矛盾します。

### (3)
解が無数にあるのは，$a=5$，$b=3$ で2つの階数がどちらも2のときです。残る2本の式は次のとおりです。

$$
\begin{aligned}
x+y+z&=1\\
y+2z&=1
\end{aligned}
$$

$z=t$ を任意の実数とし，2つ目の式，1つ目の式の順に解きます。

$$
\begin{aligned}
y&=1-2t\\
x&=1-y-z\\
&=t
\end{aligned}
$$

したがって，

$$
\finalanswer{\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}0\\1\\0\end{pmatrix}+t\begin{pmatrix}1\\-2\\1\end{pmatrix}}
$$

となります。自由な変数の数は，未知数の数3から階数2を引いた1です。一般解は，1つの特解 $(0,1,0)^{\mathrm{T}}$ に，$A\boldsymbol{x}=\boldsymbol{0}$ の解全体を加えたものになっています。

===== FILE: 07linear_algebra/02/02_050.md =====
---
tags:
  - 標準
---

# ブロック行列の行列式

## 問題
$A$ を $m$ 次の正則行列，$D$ を $n$ 次正方行列，$B$ を $m\times n$ 行列，$C$ を $n\times m$ 行列とし，$m+n$ 次の正方行列

$$
M=\begin{pmatrix}A&B\\C&D\end{pmatrix}
$$

を考える。$I_m,I_n$ は $m$ 次と $n$ 次の単位行列，$O$ は零行列である。対角ブロックが正方行列であるブロック三角行列の行列式は，対角ブロックの行列式の積に等しいことを用いてよい。以下の問いに答えよ。

(1) 次式を満たす $n\times m$ 行列 $X$ と $n$ 次正方行列 $S$ を求めよ。

$$
M=\begin{pmatrix}I_m&O\\X&I_n\end{pmatrix}\begin{pmatrix}A&B\\O&S\end{pmatrix}
$$

(2) $\det M$ を $A,B,C,D$ で表せ。

(3) $m=n$ とし，数 $a,b,c,d$ を用いて $A=aI_n$，$B=bI_n$，$C=cI_n$，$D=dI_n$ とする。$a\neq0$ のとき，$\det M$ を求めよ。

---

## 解答・解説

### (1)
右辺の積をブロックごとに計算します。ブロックの大きさがそろっているので，ふつうの行列の積と同じ規則で計算できます。

$$
\begin{pmatrix}I_m&O\\X&I_n\end{pmatrix}\begin{pmatrix}A&B\\O&S\end{pmatrix}
=\begin{pmatrix}A&B\\XA&XB+S\end{pmatrix}
$$

これを $M$ と比べると，左下のブロックから $XA=C$，右下のブロックから $XB+S=D$ が得られます。$A$ は正則なので，1つ目の式に右から $A^{-1}$ を掛けて $X$ が決まり，それを2つ目の式に代入して $S$ が決まります。したがって，

$$
\begin{aligned}
&\finalanswer{X=CA^{-1}}\\
&\finalanswer{S=D-CA^{-1}B}
\end{aligned}
$$

となります。$S$ を，$M$ における $A$ のシューア補行列とよびます。

### (2)
(1) の分解の両辺の行列式をとります。左の因子は対角ブロックが単位行列のブロック三角行列なので，行列式は1です。右の因子は対角ブロックが $A$ と $S$ のブロック三角行列です。

$$
\begin{aligned}
\det M&=\det I_m\det I_n\cdot\det A\det S\\
&=\det A\det S
\end{aligned}
$$

(1) の $S$ を代入すると，

$$
\finalanswer{\det M=\det A\,\det\left(D-CA^{-1}B\right)}
$$

となります。$m=n=1$ では $\det M=a(d-cb/a)=ad-bc$ となり，2次の行列式と一致します。

### (3)
$A^{-1}=I_n/a$ なので，シューア補行列は単位行列の定数倍になります。

$$
\begin{aligned}
S&=dI_n-\frac{cb}{a}I_n\\
&=\frac{ad-bc}{a}I_n
\end{aligned}
$$

$n$ 次の行列 $kI_n$ の行列式は $k^n$ です。(2) の式に代入すると，

$$
\begin{aligned}
\det M&=a^n\left(\frac{ad-bc}{a}\right)^n\\
&=\finalanswer{(ad-bc)^n}
\end{aligned}
$$

となります。両辺は $a,b,c,d$ の多項式なので，この等式は $a=0$ でも成り立ちます。

===== FILE: 07linear_algebra/02/02_060.md =====
---
tags:
  - 標準
---

# ヴァンデルモンドの行列式

## 問題
数 $x_1,\ldots,x_n$ に対して，$n$ 次の行列式

$$
V_n(x_1,\ldots,x_n)=\begin{vmatrix}1&x_1&x_1^2&\cdots&x_1^{n-1}\\1&x_2&x_2^2&\cdots&x_2^{n-1}\\\vdots&\vdots&\vdots&&\vdots\\1&x_n&x_n^2&\cdots&x_n^{n-1}\end{vmatrix}
$$

を考える。$V_1(x_1)=1$ とする。以下の問いに答えよ。

(1) $V_3(x_1,x_2,x_3)$ を因数分解した形で求めよ。

(2) $n\ge2$ のとき，第 $k$ 列から第 $k-1$ 列の $x_1$ 倍を引く操作を考えて，次式を示せ。

$$
V_n(x_1,\ldots,x_n)=\prod_{j=2}^{n}(x_j-x_1)\cdot V_{n-1}(x_2,\ldots,x_n)
$$

(3) $V_n(x_1,\ldots,x_n)$ を $x_j-x_i$ の積で表せ。

---

## 解答・解説

### (1)
第2行と第3行から第1行を引き，第1列に1つだけ残った1で展開します。

$$
\begin{aligned}
V_3&=\begin{vmatrix}1&x_1&x_1^2\\0&x_2-x_1&x_2^2-x_1^2\\0&x_3-x_1&x_3^2-x_1^2\end{vmatrix}\\
&=\begin{vmatrix}x_2-x_1&x_2^2-x_1^2\\x_3-x_1&x_3^2-x_1^2\end{vmatrix}
\end{aligned}
$$

各行から $x_2-x_1$ と $x_3-x_1$ をくくり出し，残った2次の行列式を計算します。

$$
\begin{aligned}
V_3&=(x_2-x_1)(x_3-x_1)\begin{vmatrix}1&x_2+x_1\\1&x_3+x_1\end{vmatrix}\\
&=(x_2-x_1)(x_3-x_1)(x_3-x_2)
\end{aligned}
$$

したがって，

$$
\finalanswer{V_3=(x_2-x_1)(x_3-x_1)(x_3-x_2)}
$$

となります。

### (2)
$k=n,n-1,\ldots,2$ の順に，第 $k$ 列から第 $k-1$ 列の $x_1$ 倍を引きます。右の列から順に行うので，引く側の第 $k-1$ 列は元のままです。この操作で行列式は変わらず，第 $i$ 行第 $k$ 列の成分は次のようになります。

$$
\begin{aligned}
x_i^{k-1}-x_1x_i^{k-2}&=x_i^{k-2}(x_i-x_1)
\end{aligned}
$$

第1行は $i=1$ なので $(1,0,\ldots,0)$ になります。第1行で展開すると，第2行から第 $n$ 行，第2列から第 $n$ 列でできる $n-1$ 次の行列式が残ります。その第 $i$ 行からは共通因子 $x_i-x_1$ をくくり出せます。

$$
\begin{aligned}
V_n&=\begin{vmatrix}x_2-x_1&(x_2-x_1)x_2&\cdots&(x_2-x_1)x_2^{n-2}\\\vdots&\vdots&&\vdots\\x_n-x_1&(x_n-x_1)x_n&\cdots&(x_n-x_1)x_n^{n-2}\end{vmatrix}\\
&=\prod_{j=2}^{n}(x_j-x_1)\begin{vmatrix}1&x_2&\cdots&x_2^{n-2}\\\vdots&\vdots&&\vdots\\1&x_n&\cdots&x_n^{n-2}\end{vmatrix}
\end{aligned}
$$

最後の行列式は $V_{n-1}(x_2,\ldots,x_n)$ です。したがって，

$$
\finalanswer{V_n(x_1,\ldots,x_n)=\prod_{j=2}^{n}(x_j-x_1)\cdot V_{n-1}(x_2,\ldots,x_n)}
$$

が成り立ちます。

### (3)
(2) の漸化式を使って，$n$ についての数学的帰納法で示します。$n=1$ では積が空なので1とみなし，$V_1=1$ と一致します。$n-1$ 個の変数について，$V_{n-1}(x_2,\ldots,x_n)$ が $2\le i<j\le n$ のすべての組についての $x_j-x_i$ の積に等しいと仮定します。(2) の式に代入すると，

$$
\begin{aligned}
V_n&=\prod_{j=2}^{n}(x_j-x_1)\prod_{2\le i<j\le n}(x_j-x_i)\\
&=\prod_{1\le i<j\le n}(x_j-x_i)
\end{aligned}
$$

となり，$n$ 個の変数でも成り立ちます。したがって，

$$
\finalanswer{V_n(x_1,\ldots,x_n)=\prod_{1\le i<j\le n}(x_j-x_i)}
$$

となります。$n=3$ では (1) の結果と一致します。$V_n\neq0$ となるのは $x_1,\ldots,x_n$ がすべて異なるときです。そのため，異なる $n$ 点を通る $n-1$ 次以下の多項式はただ1つに決まります。

===== FILE: 07linear_algebra/03/03_010.md =====
---
tags:
  - 基本
---

# 固有値と固有ベクトル

## 問題
正方行列 $A$ に対して，$A\boldsymbol{v}=\lambda\boldsymbol{v}$ を満たす数 $\lambda$ と $\boldsymbol{v}\neq\boldsymbol{0}$ を，それぞれ $A$ の固有値と固有ベクトルという。$I$ を単位行列とする。以下の問いに答えよ。

(1) 次の行列 $A$ の固有値と固有ベクトルを求めよ。

$$
A=\begin{pmatrix}4&1\\2&3\end{pmatrix}
$$

(2) 次の行列 $K$ の固有値を求めよ。

$$
K=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}
$$

(3) (2) の各固有値に対する $K$ の固有ベクトルを求めよ。

---

## 解答・解説

### (1)
$(A-\lambda I)\boldsymbol{v}=\boldsymbol{0}$ が $\boldsymbol{0}$ でない解をもつ条件は $\det(A-\lambda I)=0$ です。これを計算すると，

$$
\begin{aligned}
\det(A-\lambda I)&=(4-\lambda)(3-\lambda)-2\\
&=\lambda^2-7\lambda+10\\
&=(\lambda-2)(\lambda-5)
\end{aligned}
$$

となり，固有値は2と5です。$\lambda=5$ では $(A-5I)\boldsymbol{v}=\boldsymbol{0}$ の第1行から $-v_1+v_2=0$ が，$\lambda=2$ では $(A-2I)\boldsymbol{v}=\boldsymbol{0}$ の第1行から $2v_1+v_2=0$ が得られます。したがって，$c$ を0でない任意の数として，

$$
\begin{aligned}
&\finalanswer{\lambda=5,\quad\boldsymbol{v}=c\begin{pmatrix}1\\1\end{pmatrix}}\\
&\finalanswer{\lambda=2,\quad\boldsymbol{v}=c\begin{pmatrix}1\\-2\end{pmatrix}}
\end{aligned}
$$

となります。たとえば $A(1,-2)^{\mathrm{T}}=(2,-4)^{\mathrm{T}}$ で，これは確かに $(1,-2)^{\mathrm{T}}$ の2倍です。

### (2)
$\det(K-\lambda I)$ を第1行で展開します。第1行の成分は $2-\lambda$，$-1$，0 です。

$$
\begin{aligned}
\det(K-\lambda I)&=(2-\lambda)\begin{vmatrix}2-\lambda&-1\\-1&2-\lambda\end{vmatrix}+\begin{vmatrix}-1&-1\\0&2-\lambda\end{vmatrix}\\
&=(2-\lambda)\left[(2-\lambda)^2-1\right]-(2-\lambda)\\
&=(2-\lambda)\left[(2-\lambda)^2-2\right]
\end{aligned}
$$

これが0になるのは $2-\lambda=0$ または $2-\lambda=\pm\sqrt{2}$ のときです。したがって，

$$
\finalanswer{\lambda=2-\sqrt{2},\ 2,\ 2+\sqrt{2}}
$$

となります。

### (3)
各固有値について $(K-\lambda I)\boldsymbol{v}=\boldsymbol{0}$ を解きます。$\lambda=2$ では，第1行から $v_2=0$，第2行から $v_1+v_3=0$ です。$\lambda=2\mp\sqrt{2}$ では，第1行と第3行がそれぞれ次の式を与えます。

$$
\begin{aligned}
\pm\sqrt{2}\,v_1-v_2&=0\\
-v_2\pm\sqrt{2}\,v_3&=0
\end{aligned}
$$

複号は $\lambda=2-\sqrt{2}$ のとき上の符号です。どちらの場合も $v_1=v_3$，$v_2=\pm\sqrt{2}\,v_1$ となり，第2行も満たされます。したがって，$c$ を0でない任意の数として，

$$
\begin{aligned}
&\finalanswer{\lambda=2-\sqrt{2},\quad\boldsymbol{v}=c\begin{pmatrix}1\\\sqrt{2}\\1\end{pmatrix}}\\
&\finalanswer{\lambda=2,\quad\boldsymbol{v}=c\begin{pmatrix}1\\0\\-1\end{pmatrix}}\\
&\finalanswer{\lambda=2+\sqrt{2},\quad\boldsymbol{v}=c\begin{pmatrix}1\\-\sqrt{2}\\1\end{pmatrix}}
\end{aligned}
$$

となります。$K$ は，両端を壁につないだ3つの等しい質点がばねでつながった系の運動方程式に現れる行列です。固有ベクトルは基準振動の振動の形を表し，最も低い固有値では3つの質点が同じ向きに動きます。$K$ は対称行列なので，3つの固有ベクトルは互いに直交しています。

===== FILE: 07linear_algebra/03/03_020.md =====
---
tags:
  - 標準
---

# 対角化可能の条件

## 問題
$a$ を実数の定数とし，行列

$$
A=\begin{pmatrix}1&1&0\\0&2&0\\a&1&2\end{pmatrix}
$$

を考える。$I$ を3次の単位行列とする。固有値の重複度とは，固有多項式 $\det(A-\lambda I)$ の根としての重複度である。以下の問いに答えよ。

(1) $A$ の固有値と，それぞれの重複度を求めよ。

(2) 固有空間の次元を考えて，$A$ が対角化可能となる $a$ の値を求めよ。

(3) (2) の $a$ について，$P^{-1}AP$ が対角行列となる正則行列 $P$ を1つ求め，その対角行列を求めよ。

---

## 解答・解説

### (1)
$A-\lambda I$ の第2行は対角成分の $2-\lambda$ だけが0でないので，第2行で展開します。

$$
\begin{aligned}
\det(A-\lambda I)&=(2-\lambda)\begin{vmatrix}1-\lambda&0\\a&2-\lambda\end{vmatrix}\\
&=(1-\lambda)(2-\lambda)^2
\end{aligned}
$$

したがって，

$$
\begin{aligned}
&\finalanswer{\lambda=1\quad\text{multiplicity}\ 1}\\
&\finalanswer{\lambda=2\quad\text{multiplicity}\ 2}
\end{aligned}
$$

となります。固有値は1が重複度1，2が重複度2で，$a$ によりません。

### (2)
3次の行列が対角化可能であるのは，一次独立な固有ベクトルが3本とれるときです。各固有値の固有空間の次元は1以上で重複度以下なので，その条件は，重複度2の固有値2の固有空間が2次元になることです。固有空間の次元は $3-\operatorname{rank}(A-2I)$ です。

$$
A-2I=\begin{pmatrix}-1&1&0\\0&0&0\\a&1&0\end{pmatrix}
$$

0でない2つの行 $(-1,1,0)$ と $(a,1,0)$ が比例するとき，階数は1になります。比例する条件は次のとおりです。

$$
\begin{aligned}
(-1)\cdot1-1\cdot a&=0\\
a&=-1
\end{aligned}
$$

$a\neq-1$ では階数が2で固有空間は1次元となり，固有ベクトルが2本しかとれません。したがって，

$$
\finalanswer{a=-1}
$$

となります。$a\neq-1$ のとき $A$ は対角化できず，3-4 で扱うジョルダン標準形になります。

### (3)
$a=-1$ として，各固有値の固有ベクトルを求めます。$\lambda=2$ では，$A-2I$ の0でない行から $-v_1+v_2=0$ だけが条件になり，$v_3$ は自由です。$\lambda=1$ では，次の行列の各行が条件を与えます。

$$
A-I=\begin{pmatrix}0&1&0\\0&1&0\\-1&1&1\end{pmatrix}
$$

第1行から $v_2=0$，第3行から $v_3=v_1$ です。固有ベクトルは次のように選べます。

$$
\begin{aligned}
\lambda=1&:\quad(1,0,1)^{\mathrm{T}}\\
\lambda=2&:\quad(1,1,0)^{\mathrm{T}},\ (0,0,1)^{\mathrm{T}}
\end{aligned}
$$

これらを列に並べると $\det P=1$ となるので，$P$ は正則です。したがって，

$$
\begin{aligned}
&\finalanswer{P=\begin{pmatrix}1&1&0\\0&1&0\\1&0&1\end{pmatrix}}\\
&\finalanswer{P^{-1}AP=\begin{pmatrix}1&0&0\\0&2&0\\0&0&2\end{pmatrix}}
\end{aligned}
$$

となります。たとえば $A(1,0,1)^{\mathrm{T}}=(1,0,1)^{\mathrm{T}}$ です。対角行列の成分の並びは，$P$ の列に並べた固有ベクトルの順に対応します。

===== FILE: 07linear_algebra/03/03_030.md =====
---
tags:
  - 標準
---

# ケイリー・ハミルトンの定理

## 問題
$I$ を2次の単位行列，$O$ を2次の零行列とする。以下の問いに答えよ。

(1) 2次正方行列 $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ について，次式を示せ。

$$
A^2-(a+d)A+(ad-bc)I=O
$$

(2) 次の行列 $A$ について，0以上の整数 $n$ に対して $A^n$ を $A$ と $I$ の一次結合で表せ。

$$
A=\begin{pmatrix}3&1\\-2&0\end{pmatrix}
$$

(3) (2) の $A$ について，$A^{-1}$ を $A$ と $I$ の一次結合で表せ。

---

## 解答・解説

### (1)
$A^2$ と $(a+d)A$ を成分で計算します。

$$
\begin{aligned}
A^2&=\begin{pmatrix}a^2+bc&ab+bd\\ac+cd&bc+d^2\end{pmatrix}\\
(a+d)A&=\begin{pmatrix}a^2+ad&ab+bd\\ac+cd&ad+d^2\end{pmatrix}
\end{aligned}
$$

2つの差をとると，非対角成分は打ち消し合い，対角成分は $bc-ad$ だけが残ります。

$$
A^2-(a+d)A=-(ad-bc)I
$$

したがって，

$$
\finalanswer{A^2-(a+d)A+(ad-bc)I=O}
$$

が成り立ちます。左辺は，固有多項式 $\varphi(\lambda)=\det(\lambda I-A)=\lambda^2-(a+d)\lambda+(ad-bc)$ の $\lambda$ を $A$ に置き換えたものです。これが2次のケイリー・ハミルトンの定理です。

### (2)
トレースは3，行列式は2なので，(1) から $\varphi(A)=O$ です。ここで $\varphi(x)=x^2-3x+2=(x-1)(x-2)$ です。$x^n$ を $\varphi(x)$ で割った商を $q(x)$，余りを $p_nx+r_n$ とします。

$$
x^n=q(x)\varphi(x)+p_nx+r_n
$$

この式に $x=1$ と $x=2$ を代入すると，$\varphi(1)=\varphi(2)=0$ なので余りの係数が決まります。

$$
\begin{aligned}
1&=p_n+r_n\\
2^n&=2p_n+r_n
\end{aligned}
$$

これを解くと $p_n=2^n-1$，$r_n=2-2^n$ です。多項式の等式の $x$ を $A$ に置き換えても等式は成り立ち，$\varphi(A)=O$ なので商の項は消えます。したがって，

$$
\finalanswer{A^n=(2^n-1)A-(2^n-2)I}
$$

となります。$n=2$ では $A^2=3A-2I$ となり，(1) の関係と一致します。$n$ が大きくても，計算するのは2つの係数だけです。

### (3)
$\varphi(A)=O$ を，$A$ を左にくくり出した形に書き直します。

$$
\begin{aligned}
A^2-3A&=-2I\\
A(3I-A)&=2I
\end{aligned}
$$

両辺を2で割ると，$A$ に掛けて $I$ になる行列が得られます。したがって，

$$
\finalanswer{A^{-1}=\frac{3}{2}I-\frac{1}{2}A}
$$

となります。成分で書くと $A^{-1}=\begin{pmatrix}0&-1/2\\1&3/2\end{pmatrix}$ です。これは (2) の式に $n=-1$ を代入した $(1/2-1)A-(1/2-2)I$ と一致します。

===== FILE: 07linear_algebra/03/03_040.md =====
---
tags:
  - 発展
---

# ジョルダン標準形

## 問題
$I$ を単位行列，$O$ を零行列とする。次の行列 $A$，$B$ を考える。

$$
A=\begin{pmatrix}3&1\\-1&1\end{pmatrix},\quad
B=\begin{pmatrix}3&1&0\\-1&1&0\\1&1&2\end{pmatrix}
$$

以下の問いに答えよ。

(1) $P^{-1}AP$ がジョルダン標準形になる正則行列 $P$ を1つ求め，そのジョルダン標準形 $J$ を求めよ。

(2) 0以上の整数 $n$ に対して $A^n$ を求めよ。

(3) $Q^{-1}BQ$ がジョルダン標準形になる正則行列 $Q$ を1つ求め，そのジョルダン標準形 $J'$ を求めよ。

---

## 解答・解説

### (1)
固有多項式を計算すると，

$$
\begin{aligned}
\det(A-\lambda I)&=(3-\lambda)(1-\lambda)+1\\
&=(\lambda-2)^2
\end{aligned}
$$

となり，固有値は重複度2の2だけです。$N=A-2I$ とおくと，$N\neq O$ なので固有空間は1次元で，$A$ は対角化できません。ケイリー・ハミルトンの定理から $N^2=O$ です。

$$
N=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}
$$

求める $P=(\boldsymbol{p}_1\ \boldsymbol{p}_2)$ は $A\boldsymbol{p}_1=2\boldsymbol{p}_1$ と $A\boldsymbol{p}_2=\boldsymbol{p}_1+2\boldsymbol{p}_2$ を満たせばよく，これは $N\boldsymbol{p}_2=\boldsymbol{p}_1$，$N\boldsymbol{p}_1=\boldsymbol{0}$ と同じです。$N$ の核に入らない $\boldsymbol{p}_2=(1,0)^{\mathrm{T}}$ を選び，$\boldsymbol{p}_1=N\boldsymbol{p}_2=(1,-1)^{\mathrm{T}}$ とします。$N^2=O$ なので，$N\boldsymbol{p}_1=\boldsymbol{0}$ も成り立ちます。したがって，

$$
\begin{aligned}
&\finalanswer{P=\begin{pmatrix}1&1\\-1&0\end{pmatrix}}\\
&\finalanswer{J=\begin{pmatrix}2&1\\0&2\end{pmatrix}}
\end{aligned}
$$

となります。$AP$ と $PJ$ はどちらも $\begin{pmatrix}2&3\\-2&-1\end{pmatrix}$ になり，$AP=PJ$ が確かめられます。

### (2)
$A=2I+N$ と書けます。$2I$ と $N$ は交換するので二項定理が使え，$N^2=O$ から2次以上の項は消えます。

$$
\begin{aligned}
A^n&=(2I+N)^n\\
&=2^nI+n\,2^{n-1}N
\end{aligned}
$$

$N$ の成分を代入すると，

$$
\finalanswer{A^n=2^{n-1}\begin{pmatrix}n+2&n\\-n&2-n\end{pmatrix}}
$$

となります。$n=0$ では $I$，$n=1$ では $A$ と一致します。$PJ^nP^{-1}$ を計算しても同じ結果になります。そこでは $J^n$ の右上の成分 $n\,2^{n-1}$ が，対角化できる場合にはない $n$ に比例する因子を生みます。

### (3)
$B-\lambda I$ の第3列は $(2-\lambda)$ だけが0でないので，第3列で展開します。

$$
\begin{aligned}
\det(B-\lambda I)&=(2-\lambda)\begin{vmatrix}3-\lambda&1\\-1&1-\lambda\end{vmatrix}\\
&=(2-\lambda)^3
\end{aligned}
$$

固有値は重複度3の2です。$N'=B-2I$ を調べます。

$$
N'=\begin{pmatrix}1&1&0\\-1&-1&0\\1&1&0\end{pmatrix}
$$

$N'$ の階数は1なので，固有空間は2次元です。ジョルダン細胞1つにつき固有ベクトルが1本あるので，細胞は2つで，その大きさは2と1です。$N'$ の列はすべて $(1,-1,1)^{\mathrm{T}}$ に比例し，$N'(1,-1,1)^{\mathrm{T}}=\boldsymbol{0}$ なので，$N'^2=O$ です。(1) と同じように，$N'$ の核に入らない $\boldsymbol{q}_2=(1,0,0)^{\mathrm{T}}$ を選び，$\boldsymbol{q}_1=N'\boldsymbol{q}_2=(1,-1,1)^{\mathrm{T}}$ とします。もう1本の固有ベクトルとして，$\boldsymbol{q}_1$ と独立な $\boldsymbol{q}_3=(0,0,1)^{\mathrm{T}}$ をとります。したがって，

$$
\begin{aligned}
&\finalanswer{Q=\begin{pmatrix}1&1&0\\-1&0&0\\1&0&1\end{pmatrix}}\\
&\finalanswer{J'=\begin{pmatrix}2&1&0\\0&2&0\\0&0&2\end{pmatrix}}
\end{aligned}
$$

となります。$\det Q=1$ なので，$Q$ は正則です。$B\boldsymbol{q}_2=(3,-1,1)^{\mathrm{T}}=\boldsymbol{q}_1+2\boldsymbol{q}_2$ となり，$J'$ の第2列と一致します。

===== FILE: 07linear_algebra/03/03_050.md =====
---
tags:
  - 標準
---

# 行列の累乗と漸化式

## 問題
フィボナッチ数列を $F_0=0$，$F_1=1$，$F_{n+2}=F_{n+1}+F_n$ で定める。$\boldsymbol{x}_n=(F_{n+1},F_n)^{\mathrm{T}}$ とおくと，ある2次正方行列 $A$ を用いて $\boldsymbol{x}_{n+1}=A\boldsymbol{x}_n$ と書ける。以下の問いに答えよ。

(1) $A$ の固有値と固有ベクトルを求めよ。

(2) $F_n$ を $n$ の式で表せ。

(3) $\displaystyle\lim_{n\to\infty}\frac{F_{n+1}}{F_n}$ を求めよ。

---

## 解答・解説

### (1)
漸化式から $\boldsymbol{x}_{n+1}$ の成分を $\boldsymbol{x}_n$ の成分で表すと，$A$ が決まります。

$$
\begin{aligned}
\begin{pmatrix}F_{n+2}\\F_{n+1}\end{pmatrix}&=\begin{pmatrix}F_{n+1}+F_n\\F_{n+1}\end{pmatrix}\\
&=\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}F_{n+1}\\F_n\end{pmatrix}
\end{aligned}
$$

固有多項式は $\det(A-\lambda I)=\lambda^2-\lambda-1$ で，その根を $\phi$ と $\psi$ とします。固有ベクトルは，$(A-\lambda I)\boldsymbol{v}=\boldsymbol{0}$ の第2行 $v_1-\lambda v_2=0$ から $(\lambda,1)^{\mathrm{T}}$ と選べます。したがって，

$$
\begin{aligned}
&\finalanswer{\phi=\frac{1+\sqrt{5}}{2},\quad\boldsymbol{v}_1=\begin{pmatrix}\phi\\1\end{pmatrix}}\\
&\finalanswer{\psi=\frac{1-\sqrt{5}}{2},\quad\boldsymbol{v}_2=\begin{pmatrix}\psi\\1\end{pmatrix}}
\end{aligned}
$$

となります。根と係数の関係から，$\phi+\psi=1$，$\phi-\psi=\sqrt{5}$ です。

### (2)
$\boldsymbol{x}_n=A^n\boldsymbol{x}_0$ で，固有ベクトルには $A^n\boldsymbol{v}_i=\lambda_i^{\,n}\boldsymbol{v}_i$ が成り立ちます。そこで，初期値 $\boldsymbol{x}_0=(1,0)^{\mathrm{T}}$ を固有ベクトルで展開します。$\boldsymbol{x}_0=c_1\boldsymbol{v}_1+c_2\boldsymbol{v}_2$ の成分を比べると，

$$
\begin{aligned}
c_1\phi+c_2\psi&=1\\
c_1+c_2&=0
\end{aligned}
$$

となり，$c_1(\phi-\psi)=1$ から $c_1=1/\sqrt{5}$，$c_2=-1/\sqrt{5}$ です。各成分に $A^n$ を掛けると，

$$
\boldsymbol{x}_n=\frac{1}{\sqrt{5}}\left(\phi^n\boldsymbol{v}_1-\psi^n\boldsymbol{v}_2\right)
$$

となります。$\boldsymbol{x}_n$ の第2成分が $F_n$ です。したがって，

$$
\finalanswer{F_n=\frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n\right]}
$$

となります。$n=1$ では $(\phi-\psi)/\sqrt{5}=1$，$n=2$ では $(\phi+\psi)(\phi-\psi)/\sqrt{5}=1$ で，漸化式の値と一致します。

### (3)
(2) の式で比をとり，分子と分母を $\phi^n$ で割ります。

$$
\frac{F_{n+1}}{F_n}=\frac{\phi-\psi\,(\psi/\phi)^n}{1-(\psi/\phi)^n}
$$

$|\psi|\approx0.618$，$\phi\approx1.618$ なので，$|\psi/\phi|<1$ で $(\psi/\phi)^n\to0$ です。したがって，

$$
\finalanswer{\lim_{n\to\infty}\frac{F_{n+1}}{F_n}=\frac{1+\sqrt{5}}{2}}
$$

となり，極限は黄金比です。$n$ が大きくなると，絶対値の大きい固有値 $\phi$ の成分だけが残り，$\boldsymbol{x}_n$ は固有ベクトル $\boldsymbol{v}_1$ の向きに近づきます。$|\psi^n/\sqrt{5}|<1/2$ なので，$F_n$ は $\phi^n/\sqrt{5}$ に最も近い整数でもあります。

===== FILE: 07linear_algebra/03/03_060.md =====
---
tags:
  - 標準
---

# 行列の指数関数

## 問題
正方行列 $A$ と実数 $t$ に対して，行列の指数関数を

$$
e^{At}=\sum_{k=0}^{\infty}\frac{t^k}{k!}A^k
$$

で定義する。$A^0=I$ は単位行列であり，この級数は項別に微分してよい。以下の問いに答えよ。

(1) $\omega>0$ を定数とし，次の行列 $A$ について $e^{At}$ を求めよ。

$$
A=\begin{pmatrix}0&1\\-\omega^2&0\end{pmatrix}
$$

(2) 一般の正方行列 $A$ と定ベクトル $\boldsymbol{X}_0$ について，$\boldsymbol{X}(t)=e^{At}\boldsymbol{X}_0$ が $\mathrm{d}\boldsymbol{X}/\mathrm{d}t=A\boldsymbol{X}$ と $\boldsymbol{X}(0)=\boldsymbol{X}_0$ を満たすことを示せ。

(3) 質量 $m$ の質点が，ばね定数 $k$ のばねにつながれて直線上を運動する。位置を $x(t)$，速度を $v(t)$ とし，$\omega=\sqrt{k/m}$ とする。$x(0)=x_0$，$v(0)=v_0$ のとき，$x(t)$ を求めよ。

---

## 解答・解説

### (1)
級数を計算するために，$A$ のべきの規則を調べます。$A$ を2乗すると単位行列の定数倍になります。

$$
\begin{aligned}
A^2&=\begin{pmatrix}0\cdot0+1\cdot(-\omega^2)&0\cdot1+1\cdot0\\-\omega^2\cdot0+0\cdot(-\omega^2)&-\omega^2\cdot1+0\cdot0\end{pmatrix}\\
&=-\omega^2I
\end{aligned}
$$

したがって，偶数乗と奇数乗はそれぞれ次のようになります。

$$
\begin{aligned}
A^{2j}&=(-1)^j\omega^{2j}I\\
A^{2j+1}&=(-1)^j\omega^{2j}A
\end{aligned}
$$

級数を偶数番目の項と奇数番目の項に分けると，それぞれ余弦と正弦のテイラー級数になります。

$$
\begin{aligned}
e^{At}&=\sum_{j=0}^{\infty}\frac{(-1)^j(\omega t)^{2j}}{(2j)!}I+\frac{1}{\omega}\sum_{j=0}^{\infty}\frac{(-1)^j(\omega t)^{2j+1}}{(2j+1)!}A\\
&=\cos\omega t\,I+\frac{\sin\omega t}{\omega}A
\end{aligned}
$$

成分で書くと，

$$
\finalanswer{e^{At}=\begin{pmatrix}\cos\omega t&\dfrac{\sin\omega t}{\omega}\\-\omega\sin\omega t&\cos\omega t\end{pmatrix}}
$$

となります。$t=0$ では単位行列になります。

### (2)
定義の級数を項別に $t$ で微分します。$k=0$ の項は定数なので消え，残りの項から $A$ を1つくくり出します。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t}e^{At}&=\sum_{k=1}^{\infty}\frac{kt^{k-1}}{k!}A^k\\
&=A\sum_{k=1}^{\infty}\frac{t^{k-1}}{(k-1)!}A^{k-1}\\
&=Ae^{At}
\end{aligned}
$$

$\boldsymbol{X}_0$ は定ベクトルなので，$\boldsymbol{X}(t)$ の微分はこの式に右から $\boldsymbol{X}_0$ を掛けたものです。したがって，

$$
\begin{aligned}
&\finalanswer{\frac{\mathrm{d}\boldsymbol{X}}{\mathrm{d}t}=Ae^{At}\boldsymbol{X}_0=A\boldsymbol{X}}\\
&\finalanswer{\boldsymbol{X}(0)=I\boldsymbol{X}_0=\boldsymbol{X}_0}
\end{aligned}
$$

となります。行列の指数関数は，1変数の $e^{at}$ と同じ役割を連立一次微分方程式で果たします。

### (3)
運動方程式 $m\,\mathrm{d}v/\mathrm{d}t=-kx$ と $\mathrm{d}x/\mathrm{d}t=v$ を，$\boldsymbol{X}=(x,v)^{\mathrm{T}}$ についての1階の方程式にまとめます。

$$
\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix}x\\v\end{pmatrix}=\begin{pmatrix}0&1\\-\omega^2&0\end{pmatrix}\begin{pmatrix}x\\v\end{pmatrix}
$$

係数行列は (1) の $A$ です。(2) から，解は (1) の $e^{At}$ を $\boldsymbol{X}_0=(x_0,v_0)^{\mathrm{T}}$ に掛けたものです。その第1成分をとると，

$$
\finalanswer{x(t)=x_0\cos\omega t+\frac{v_0}{\omega}\sin\omega t}
$$

となります。第2成分は $v(t)=-\omega x_0\sin\omega t+v_0\cos\omega t$ です。$x^2+v^2/\omega^2$ は時間によらないので，$(x,v)$ 平面での軌道は楕円になります。その様子を図に示します。

<!-- FIGURE solution (3): 横軸 位置 x，縦軸 速度 v，原点 O。原点を中心とし，x 方向の半径 a，v 方向の半径 ωa の楕円を実線で描く（a = √(x0² + v0²/ω²)）。楕円の上の1点に黒丸を置いて (x0, v0) とラベルする。楕円上に時計回りの矢印を2〜3個付けて運動の向きを示す（v > 0 の上半分では x が増える向き）。横軸に a と −a，縦軸に ωa と −ωa の目盛りを付ける。 -->

$\det e^{At}=\cos^2\omega t+\sin^2\omega t=1$ なので，$e^{At}$ による写像は $(x,v)$ 平面の面積を変えません。

===== END =====