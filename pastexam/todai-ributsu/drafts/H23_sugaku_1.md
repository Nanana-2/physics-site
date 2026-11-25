---
title: 東大理物 平成23年度 数学 第1問：反交換関係を満たす複素行列とパウリ行列表現
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成23年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成23年度 数学 第1問：反交換関係を満たす複素行列とパウリ行列表現

## 問題

$A, B$ は $n$ 行 $n$ 列の複素行列であり，$A^2 = B^2 = E$，$AB + BA = O$ を満たすものとする。ただし，$E$ は単位行列，$O$ は全ての成分が $0$ に等しい零行列である。また，行列 $C, D$ をそれぞれ $C = -iAB$，$D = A + iB$ によって定義する。$i$ は虚数単位である。このとき，以下の設問に答えよ。

(1) 行列 $A$ の固有値の取り得る値を全て求めよ。

(2) $C^2 = E$ となること，また $BC + CB = CA + AC = O$ となることを示せ。

(3) $D^2 = O$ かつ $D \neq O$ となることを示せ。

(4) 設問 (3) の結果により，$D\boldsymbol{r} \neq \boldsymbol{0}$（ただし $\boldsymbol{0}$ は零ベクトル）となる縦ベクトル $\boldsymbol{r}$ が存在する。ここで $\boldsymbol{p} = D\boldsymbol{r}$ によりベクトル $\boldsymbol{p}$ を定義すると，$\boldsymbol{p} \neq \boldsymbol{0}$ かつ $D\boldsymbol{p} = D^2\boldsymbol{r} = \boldsymbol{0}$ をみたす。また $\boldsymbol{p}$ を用いて，ベクトル $\boldsymbol{q}$ を，$\boldsymbol{q} = \dfrac{1}{2}(A - iB)\boldsymbol{p}$ によって定義する。

(i) ベクトル $\boldsymbol{p}, \boldsymbol{q}$ は，ともに行列 $C$ の固有ベクトルになっていることを示し，それぞれの固有値を求めよ。

(ii) ベクトル $\boldsymbol{p}, \boldsymbol{q}$ は互いに線型独立であることを証明せよ。

(5) 以下では $n = 2$ とし，設問 (4) で定義した $\boldsymbol{p}, \boldsymbol{q}$ が 2 次元縦ベクトルとなる場合を考える。

(i) $\boldsymbol{p}, \boldsymbol{q}$ を並べて作った 2 次元正方行列 $P = (\boldsymbol{p}\ \boldsymbol{q})$ は正則であることを，設問 (4) の結果を用いることによって示せ。

(ii) 行列 $P^{-1} C P$ を計算せよ。

(iii) 行列 $P^{-1}(A \pm iB)P$ を計算することによって，$P^{-1} A P$ および $P^{-1} B P$ を求めよ。

(6) $n = 2$ のとき，行列 $A, B, C$ の具体形を一組与えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成23年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
関係式 $A^2 = B^2 = E$ と $AB + BA = O$ から，$A, B, C = -iAB$ は互いに反交換し 2 乗が $E$ になる 3 つ組を作ります。また $D = A + iB$ が零でないのに $D^2 = O$ になる性質から，$D\boldsymbol{p} = \boldsymbol{0}$ を満たす零でないベクトル $\boldsymbol{p}$ が存在します。

この $\boldsymbol{p}$ と $\boldsymbol{q} = \dfrac{1}{2}(A - iB)\boldsymbol{p}$ は行列 $C$ の異なる固有値に属する固有ベクトルになるため，$n = 2$ では両者を並べた行列 $P$ が正則となり，相似変換 $P^{-1}(\cdot)P$ によって $A, B, C$ の行列成分が一意に定まります。
</div>

### (1)
行列 $A$ の固有値を $\lambda$，対応する固有ベクトルを $\boldsymbol{v} \neq \boldsymbol{0}$ とします。$A\boldsymbol{v} = \lambda\boldsymbol{v}$ の両辺に左から $A$ を掛け，$A^2 = E$ を用います。

$$
\begin{aligned}
A^2 \boldsymbol{v} &= \lambda A\boldsymbol{v} \\
\boldsymbol{v} &= \lambda^2 \boldsymbol{v} \\
(\lambda^2 - 1)\boldsymbol{v} &= \boldsymbol{0}
\end{aligned}
$$

$\boldsymbol{v} \neq \boldsymbol{0}$ なので $\lambda^2 = 1$，すなわち $\lambda = 1$ または $\lambda = -1$ です。

さらに，$1$ と $-1$ がともに実際に固有値となることを確かめます。$B^2 = E$ より $B$ は正則なので $B\boldsymbol{v} \neq \boldsymbol{0}$ です。$AB = -BA$ を用いて $A(B\boldsymbol{v})$ を計算します。

$$
\begin{aligned}
A(B\boldsymbol{v}) &= -BA\boldsymbol{v} \\
&= -\lambda(B\boldsymbol{v})
\end{aligned}
$$

よって $\lambda$ が固有値ならば $-\lambda$ も固有値であり，$A$ の固有値の取り得る値は $1$ と $-1$ の両方です。

$$
\finalanswer{\lambda = 1,\; -1}
$$

### (2)
$C = -iAB$ および $AB = -BA$，$A^2 = B^2 = E$ を用いて $C^2$，$BC + CB$，$CA + AC$ を順に計算します。

$$
\begin{aligned}
C^2 &= (-iAB)(-iAB) \\
&= -A(BA)B \\
&= -A(-AB)B \\
&= A^2 B^2 \\
&= E
\end{aligned}
$$

$$
\begin{aligned}
BC + CB &= B(-iAB) + (-iAB)B \\
&= -i(BA)B - iA B^2 \\
&= -i(-AB)B - iAE \\
&= iA B^2 - iA \\
&= iA - iA \\
&= O
\end{aligned}
$$

$$
\begin{aligned}
CA + AC &= (-iAB)A + A(-iAB) \\
&= -iA(BA) - iA^2 B \\
&= -iA(-AB) - iEB \\
&= iA^2 B - iB \\
&= iB - iB \\
&= O
\end{aligned}
$$

以上より，$C^2 = E$ および $BC + CB = CA + AC = O$ が成り立ちます。

### (3)
$D = A + iB$ の 2 乗を展開します。

$$
\begin{aligned}
D^2 &= (A + iB)(A + iB) \\
&= A^2 + i(AB + BA) - B^2 \\
&= E + O - E \\
&= O
\end{aligned}
$$

次に $D \neq O$ であることを背理法で示します。仮に $D = O$ であるとすると，$A = -iB$ が成り立ちます。両辺を 2 乗すると次式になります。

$$
\begin{aligned}
A^2 &= (-iB)^2 \\
E &= -B^2 \\
E &= -E
\end{aligned}
$$

これは矛盾するので，$D \neq O$ です。

### (4)(i)
$D\boldsymbol{p} = (A + iB)\boldsymbol{p} = \boldsymbol{0}$ より $A\boldsymbol{p} = -iB\boldsymbol{p}$ です。まず $C\boldsymbol{p}$ を計算します。

$$
\begin{aligned}
C\boldsymbol{p} &= -iAB\boldsymbol{p} \\
&= A(-iB\boldsymbol{p}) \\
&= A(A\boldsymbol{p}) \\
&= A^2\boldsymbol{p} \\
&= \boldsymbol{p}
\end{aligned}
$$

$\boldsymbol{p} \neq \boldsymbol{0}$ なので，$\boldsymbol{p}$ は $C$ の固有値 $1$ に属する固有ベクトルです。

次に $\boldsymbol{q} = \dfrac{1}{2}(A - iB)\boldsymbol{p}$ について，$-iB\boldsymbol{p} = A\boldsymbol{p}$ を用いると $\boldsymbol{q} = \dfrac{1}{2}(A\boldsymbol{p} + A\boldsymbol{p}) = A\boldsymbol{p}$ となります。$A^2 = E$ より $A$ は正則であり $\boldsymbol{p} \neq \boldsymbol{0}$ なので，$\boldsymbol{q} = A\boldsymbol{p} \neq \boldsymbol{0}$ です。設問 (2) の $CA = -AC$，$CB = -BC$ を用いて $C\boldsymbol{q}$ を計算します。

$$
\begin{aligned}
C\boldsymbol{q} &= \frac{1}{2}C(A - iB)\boldsymbol{p} \\
&= -\frac{1}{2}(A - iB)C\boldsymbol{p} \\
&= -\frac{1}{2}(A - iB)\boldsymbol{p} \\
&= -\boldsymbol{q}
\end{aligned}
$$

よって $\boldsymbol{q}$ は $C$ の固有値 $-1$ に属する固有ベクトルです。

$$
\finalanswer{C\boldsymbol{p} = \boldsymbol{p}, \qquad C\boldsymbol{q} = -\boldsymbol{q}}
$$

### (4)(ii)
複素数 $c_1, c_2$ に対して $c_1\boldsymbol{p} + c_2\boldsymbol{q} = \boldsymbol{0}$ と仮定します。両辺に左から $C$ を掛け，設問 (4)(i) の結果 $C\boldsymbol{p} = \boldsymbol{p}$，$C\boldsymbol{q} = -\boldsymbol{q}$ を用います。

$$
\begin{aligned}
c_1\boldsymbol{p} + c_2\boldsymbol{q} &= \boldsymbol{0} \\
c_1\boldsymbol{p} - c_2\boldsymbol{q} &= \boldsymbol{0}
\end{aligned}
$$

2 式の和と差をとると $2c_1\boldsymbol{p} = \boldsymbol{0}$，$2c_2\boldsymbol{q} = \boldsymbol{0}$ が得られます。$\boldsymbol{p} \neq \boldsymbol{0}$，$\boldsymbol{q} \neq \boldsymbol{0}$ なので $c_1 = c_2 = 0$ です。したがって $\boldsymbol{p}, \boldsymbol{q}$ は互いに線型独立です。

### (5)(i)
$n = 2$ のとき，$\boldsymbol{p}, \boldsymbol{q}$ は設問 (4)(ii) より互いに線型独立な 2 次元縦ベクトルです。2 次元正方行列 $P = (\boldsymbol{p}\ \boldsymbol{q})$ の列ベクトルが線型独立なので，$\operatorname{rank} P = 2$ であり $P$ は正則です。

### (5)(ii)
設問 (4)(i) より $CP$ は次のように計算されます。

$$
\begin{aligned}
CP &= (C\boldsymbol{p}\quad C\boldsymbol{q}) \\
&= (\boldsymbol{p}\quad -\boldsymbol{q}) \\
&= (\boldsymbol{p}\quad \boldsymbol{q})\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \\
&= P\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\end{aligned}
$$

両辺に左から $P^{-1}$ を掛けると次式が得られます。

$$
\finalanswer{P^{-1} C P = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}}
$$

### (5)(iii)
まず $(A + iB)$ を $\boldsymbol{p}$ と $\boldsymbol{q}$ に作用させます。$(A + iB)\boldsymbol{p} = D\boldsymbol{p} = \boldsymbol{0}$ です。$\boldsymbol{q}$ への作用は次のように計算します。

$$
\begin{aligned}
(A + iB)\boldsymbol{q} &= \frac{1}{2}(A + iB)(A - iB)\boldsymbol{p} \\
&= \frac{1}{2}\bigl(A^2 + B^2 - i(AB - BA)\bigr)\boldsymbol{p} \\
&= \frac{1}{2}\bigl(2E - 2iAB\bigr)\boldsymbol{p} \\
&= (E + C)\boldsymbol{p} \\
&= 2\boldsymbol{p}
\end{aligned}
$$

よって $(A + iB)P = (\boldsymbol{0}\quad 2\boldsymbol{p}) = P\begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$ となり，次式が得られます。

$$
P^{-1}(A + iB)P = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}
$$

次に $(A - iB)$ を $\boldsymbol{p}$ と $\boldsymbol{q}$ に作用させます。定義より $(A - iB)\boldsymbol{p} = 2\boldsymbol{q}$ です。また $(A - iB)^2 = A^2 - i(AB + BA) - B^2 = O$ なので，

$$
\begin{aligned}
(A - iB)\boldsymbol{q} &= \frac{1}{2}(A - iB)^2 \boldsymbol{p} \\
&= \boldsymbol{0}
\end{aligned}
$$

です。よって $(A - iB)P = (2\boldsymbol{q}\quad \boldsymbol{0}) = P\begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix}$ となり，次式が得られます。

$$
P^{-1}(A - iB)P = \begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix}
$$

これら 2 式の和と差から $P^{-1} A P$ と $P^{-1} B P$ を求めます。

$$
\begin{aligned}
P^{-1} A P &= \frac{1}{2}\left[P^{-1}(A + iB)P + P^{-1}(A - iB)P\right] \\
&= \frac{1}{2}\left[\begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix}\right] \\
&= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
\end{aligned}
$$

$$
\begin{aligned}
P^{-1} B P &= \frac{1}{2i}\left[P^{-1}(A + iB)P - P^{-1}(A - iB)P\right] \\
&= \frac{1}{2i}\left[\begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix}\right] \\
&= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\end{aligned}
$$

$$
\finalanswer{P^{-1} A P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad P^{-1} B P = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}}
$$

### (6)
設問 (5) で得られた行列そのものをとると，$A^2 = B^2 = E$，$AB + BA = O$，$C = -iAB$ をすべて満たします。

$$
\finalanswer{A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad C = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}}
$$
