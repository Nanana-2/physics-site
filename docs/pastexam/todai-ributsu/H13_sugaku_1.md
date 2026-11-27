---
title: 東大理物 平成13年度 数学 第1問：4次元空間の部分空間と共通部分の次元
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成13年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成13年度 数学 第1問：4次元空間の部分空間と共通部分の次元

## 問題

4次元ユークリッド空間の部分空間 $V_1, V_2$ を

$$
V_1 \equiv \bigl\{\text{条件 } x_1 - x_2 + 2x_3 - x_4 = 0 \text{ と } x_1 + 2x_2 - x_3 = 0 \text{ を共に満足するベクトル } \vec{x} = (x_1, x_2, x_3, x_4) \text{ の集合}\bigr\}
$$

$$
V_2 \equiv \bigl\{\text{条件 } 2x_1 + x_2 + 2x_3 - 2x_4 = 0 \text{ と } 3x_1 + 2x_3 - x_4 = 0 \text{ を共に満足するベクトル } \vec{x} = (x_1, x_2, x_3, x_4) \text{ の集合}\bigr\}
$$

とする。
{: .problem-lead }

(1) $V_1, V_2$ はそれぞれ何次元の空間か？

(2) $V_1$ と $V_2$ に共通に含まれるベクトルを求めよ。

(3) 空間 $V_1 \cap V_2$ は何次元か？

> 出典：東京大学大学院理学系研究科物理学専攻 平成13年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
斉次連立1次方程式 $A\vec{x} = \vec{0}$ の解空間の次元は，未知数の個数から係数行列の階数 $\operatorname{rank} A$ を引いた値に等しくなります。

$V_1$ と $V_2$ はそれぞれ2本の線形方程式で定まる解空間であり，$V_1 \cap V_2$ は4本の方程式をすべて連立した解空間です。係数行列に行基本変形を行って階数と一般解を求めます。
</div>

### (1)

$V_1$ を定める2本の方程式の係数行列を $A_1$ とします。

$$
A_1 = \begin{pmatrix} 1 & -1 & 2 & -1 \\ 1 & 2 & -1 & 0 \end{pmatrix}
$$

第2行から第1行を引きます。

$$
\begin{pmatrix} 1 & -1 & 2 & -1 \\ 1 & 2 & -1 & 0 \end{pmatrix} \to \begin{pmatrix} 1 & -1 & 2 & -1 \\ 0 & 3 & -3 & 1 \end{pmatrix}
$$

2つの行は1次独立なので $\operatorname{rank} A_1 = 2$ です。よって $V_1$ の次元は次になります。

$$
\begin{aligned}
\dim V_1 &= 4 - \operatorname{rank} A_1 \\
&= 4 - 2 \\
&= 2
\end{aligned}
$$

同様に，$V_2$ を定める2本の方程式の係数行列を $A_2$ とします。

$$
A_2 = \begin{pmatrix} 2 & 1 & 2 & -2 \\ 3 & 0 & 2 & -1 \end{pmatrix}
$$

第1列と第2列の小行列式は $2 \cdot 0 - 1 \cdot 3 = -3 \neq 0$ なので，2つの行は1次独立であり $\operatorname{rank} A_2 = 2$ です。よって $V_2$ の次元も次になります。

$$
\begin{aligned}
\dim V_2 &= 4 - \operatorname{rank} A_2 \\
&= 4 - 2 \\
&= 2
\end{aligned}
$$

したがって，$V_1$ と $V_2$ の次元はいずれも $2$ です。

$$
\finalanswer{\dim V_1 = 2, \qquad \dim V_2 = 2}
$$

### (2)

$V_1 \cap V_2$ に属するベクトル $\vec{x} = (x_1, x_2, x_3, x_4)$ は，次の4本の方程式をすべて満たします。

$$
\begin{aligned}
x_1 - x_2 + 2x_3 - x_4 &= 0 \\
x_1 + 2x_2 - x_3 &= 0 \\
2x_1 + x_2 + 2x_3 - 2x_4 &= 0 \\
3x_1 + 2x_3 - x_4 &= 0
\end{aligned}
$$

この連立方程式の係数行列 $A$ に行基本変形を行います。まず第2行から第1行を引き，第3行から第1行の2倍を引き，第4行から第1行の3倍を引きます。

$$
A = \begin{pmatrix} 1 & -1 & 2 & -1 \\ 1 & 2 & -1 & 0 \\ 2 & 1 & 2 & -2 \\ 3 & 0 & 2 & -1 \end{pmatrix} \to \begin{pmatrix} 1 & -1 & 2 & -1 \\ 0 & 3 & -3 & 1 \\ 0 & 3 & -2 & 0 \\ 0 & 3 & -4 & 2 \end{pmatrix}
$$

続いて第3行から第2行を引き，第4行から第2行を引きます。

$$
\begin{pmatrix} 1 & -1 & 2 & -1 \\ 0 & 3 & -3 & 1 \\ 0 & 3 & -2 & 0 \\ 0 & 3 & -4 & 2 \end{pmatrix} \to \begin{pmatrix} 1 & -1 & 2 & -1 \\ 0 & 3 & -3 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & -1 & 1 \end{pmatrix}
$$

最後に第4行に第3行を足します。

$$
\begin{pmatrix} 1 & -1 & 2 & -1 \\ 0 & 3 & -3 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & -1 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & -1 & 2 & -1 \\ 0 & 3 & -3 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

これにより，もとの連立方程式は次の3本と同値になります。

$$
\begin{aligned}
x_1 - x_2 + 2x_3 - x_4 &= 0 \\
3x_2 - 3x_3 + x_4 &= 0 \\
x_3 - x_4 &= 0
\end{aligned}
$$

自由変数を $x_4 = 3t$（$t$ は任意の実数）とおきます。3本目の式より $x_3 = x_4$ なので，$x_3 = 3t$ です。これを2本目の式に代入します。

$$
\begin{aligned}
3x_2 &= 3x_3 - x_4 \\
&= 9t - 3t \\
&= 6t
\end{aligned}
$$

よって $x_2 = 2t$ です。これらを1本目の式に代入して $x_1$ を求めます。

$$
\begin{aligned}
x_1 &= x_2 - 2x_3 + x_4 \\
&= 2t - 6t + 3t \\
&= -t
\end{aligned}
$$

したがって，$V_1$ と $V_2$ に共通に含まれるベクトルは次の通りです。

$$
\finalanswer{\vec{x} = t(-1, 2, 3, 3) \qquad (t \in \mathbb{R})}
$$

### (3)

(2) で求めた係数行列 $A$ の行階段形には零でない行が3本あるため，$\operatorname{rank} A = 3$ です。あるいは (2) の一般解が1つの独立な基底ベクトル $(-1, 2, 3, 3)$ の実数倍全体であることから，$V_1 \cap V_2$ の次元は次になります。

$$
\begin{aligned}
\dim(V_1 \cap V_2) &= 4 - \operatorname{rank} A \\
&= 4 - 3 \\
&= 1
\end{aligned}
$$

$$
\finalanswer{\dim(V_1 \cap V_2) = 1}
$$
