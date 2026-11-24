---
title: 東大理物 平成29年度 数学 第2問：外積行列とロドリゲスの回転公式
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成29年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成29年度 数学 第2問：外積行列とロドリゲスの回転公式

## 問題

3次元実ベクトル空間について，以下の設問に答えよ。ただし，$\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ を単位ベクトル，すなわち $\displaystyle\sum_{i=1}^{3} a_i^2 = 1$ を満たす3次元ベクトルとする。

(1) $\vec{x}$ を任意の3次元ベクトルとするとき，外積 $\vec{a}\times\vec{x}$ は行列 $J(\vec{a})$ を用いて $\vec{a}\times\vec{x} = J(\vec{a})\vec{x}$ と書くことができる。行列 $J(\vec{a})$ を求めよ。

(2) 行列 $J(\vec{a})$ の固有値をすべて求めよ。

(3) $P(\vec{a}) = -J(\vec{a})^2$ と定義する。以下の (i)〜(iii) の等式を示せ。

(i) $P(\vec{a})\vec{a} = \vec{0}$

(ii) $\vec{a}$ と直交するすべてのベクトル $\vec{b}$ に対して $P(\vec{a})\vec{b} = \vec{b}$

(iii) $P(\vec{a})^2 = P(\vec{a})$

(4) $\theta$ を任意の実数とする行列 $\exp(\theta J(\vec{a}))$ は，次のように展開することができる。

$$
\exp(\theta J(\vec{a})) = f_1(\theta)I + f_2(\theta)P(\vec{a}) + f_3(\theta)J(\vec{a})P(\vec{a})
$$

ここで $I$ は単位行列であり，$f_i(\theta)\ (i = 1, 2, 3)$ は $\vec{a}$ によらない $\theta$ の関数である。$f_1(\theta),\ f_2(\theta),\ f_3(\theta)$ を求めよ。ただし，行列の指数関数は $\exp(\theta J(\vec{a})) = \displaystyle\sum_{n=0}^{\infty}\dfrac{\theta^n}{n!}J(\vec{a})^n$ と定義される。

(5) $\vec{a}$ と直交する単位ベクトルの一つを $\vec{b}$ とし，$\vec{c}$ を $\vec{c} = \vec{a}\times\vec{b}$ と定義すると，$\vec{a}, \vec{b}, \vec{c}$ は正規直交基底となる。行列 $\exp(\theta J(\vec{a}))$ と $\vec{a}, \vec{b}, \vec{c}$ それぞれとの積を $\vec{a}, \vec{b}, \vec{c}$ の線形和で表し，この行列が $\vec{a}$ を軸とした角度 $\theta$ の回転を表すことを示せ。

(6) $\vec{b}, \vec{c}$ を設問5で与えたベクトルとする。任意の実数 $\theta, \varphi$ に対して，実数 $\chi$ と単位ベクトル $\vec{e}$ を選ぶことにより

$$
\exp(\theta J(\vec{a}))\exp(\varphi J(\vec{b}))\exp(-\theta J(\vec{a})) = \exp(\chi J(\vec{e}))
$$

と書くことができる。$\vec{e}$ を $\vec{a}, \vec{b}, \vec{c}$ の線形和で表し，$\chi$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成29年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
単位ベクトル $\vec{a}$ との外積を表す反対称行列 $J(\vec{a})$ は，$P(\vec{a}) = -J(\vec{a})^2$ が $\vec{a}$ に直交する平面への射影行列となるため，$J^3 = -J$ という簡潔な最小多項式を満たします。

これにより無限級数 $\exp(\theta J(\vec{a}))$ は有限個の行列 $I,\ P(\vec{a}),\ J(\vec{a})$ の線形結合（ロドリゲスの回転公式）へ閉じ，さらに回転の相似変換は回転軸ベクトル自身を回転させる操作にほかならないことが幾何学的にも代数的にも直接導かれます。
</div>

### (1)
$\vec{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}$ とおくと，外積 $\vec{a}\times\vec{x}$ の各成分は

$$
\vec{a}\times\vec{x} = \begin{pmatrix} a_2 x_3 - a_3 x_2 \\ a_3 x_1 - a_1 x_3 \\ a_1 x_2 - a_2 x_1 \end{pmatrix}
= \begin{pmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}
$$

となります。したがって，

$$
\finalanswer{J(\vec{a}) = \begin{pmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{pmatrix}}
$$

### (2)
固有方程式 $\det(J(\vec{a}) - \lambda I) = 0$ を展開し，$a_1^2 + a_2^2 + a_3^2 = 1$ を用います。

$$
\begin{aligned}
\det\begin{pmatrix} -\lambda & -a_3 & a_2 \\ a_3 & -\lambda & -a_1 \\ -a_2 & a_1 & -\lambda \end{pmatrix}
&= -\lambda^3 - a_1 a_2 a_3 + a_1 a_2 a_3 - a_2^2\lambda - a_1^2\lambda - a_3^2\lambda \\
&= -\lambda\left(\lambda^2 + a_1^2 + a_2^2 + a_3^2\right) \\
&= -\lambda\left(\lambda^2 + 1\right) = 0
\end{aligned}
$$

よって固有値は $0,\ i,\ -i$ です。したがって，

$$
\finalanswer{\lambda = 0,\ i,\ -i}
$$

### (3)
任意の3次元ベクトル $\vec{x}$ に対して，ベクトル三重積の公式と $|\vec{a}|^2 = 1$ を用いて $P(\vec{a})\vec{x}$ を計算します。

$$
P(\vec{a})\vec{x} = -J(\vec{a})^2\vec{x} = -\vec{a}\times(\vec{a}\times\vec{x}) = -\left[(\vec{a}\cdot\vec{x})\vec{a} - (\vec{a}\cdot\vec{a})\vec{x}\right] = \vec{x} - (\vec{a}\cdot\vec{x})\vec{a}
$$

(i) $\vec{x} = \vec{a}$ を代入すると，$|\vec{a}|^2 = 1$ より

$$
P(\vec{a})\vec{a} = \vec{a} - (\vec{a}\cdot\vec{a})\vec{a} = \vec{a} - \vec{a} = \vec{0}
$$

が成り立ちます。

(ii) $\vec{a}\cdot\vec{b} = 0$ を満たす任意のベクトル $\vec{b}$ を代入すると，

$$
P(\vec{a})\vec{b} = \vec{b} - (\vec{a}\cdot\vec{b})\vec{a} = \vec{b}
$$

が成り立ちます。

(iii) 任意のベクトル $\vec{x}$ に対し，(i) と上の関係を用いて $P(\vec{a})^2\vec{x}$ を計算します。

$$
\begin{aligned}
P(\vec{a})^2\vec{x}
&= P(\vec{a})\bigl[\vec{x} - (\vec{a}\cdot\vec{x})\vec{a}\bigr] \\
&= P(\vec{a})\vec{x} - (\vec{a}\cdot\vec{x}) P(\vec{a})\vec{a} \\
&= P(\vec{a})\vec{x}
\end{aligned}
$$

任意の $\vec{x}$ に対して成り立つので，$P(\vec{a})^2 = P(\vec{a})$ です。

### (4)
略記として $J = J(\vec{a}),\ P = P(\vec{a})$ とおきます。定義より $J^2 = -P$ です。また任意の $\vec{x}$ に対し $J(\vec{a})P(\vec{a})\vec{x} = \vec{a}\times\bigl(\vec{x} - (\vec{a}\cdot\vec{x})\vec{a}\bigr) = \vec{a}\times\vec{x} = J(\vec{a})\vec{x}$ なので，$JP = J$ が成り立ちます。

さらに問3(iii)の $P^2 = P$ と $J^2 = -P$ より，

$$
J^3 = J(-P) = -JP = -J,\qquad J^4 = (-P)^2 = P^2 = P
$$

となるため，帰納的に任意の整数 $k \ge 1$ に対して次式が成り立ちます。

$$
J^{2k} = (-1)^k P,\qquad J^{2k - 1} = (-1)^{k - 1} JP
$$

これを指数関数の級数展開に代入し，偶数次（$n = 2k$）と奇数次（$n = 2k - 1$）に分けてまとめます。

$$
\begin{aligned}
\exp(\theta J)
&= I + \sum_{k=1}^{\infty}\frac{\theta^{2k}}{(2k)!}(-1)^k P + \sum_{k=1}^{\infty}\frac{\theta^{2k-1}}{(2k-1)!}(-1)^{k-1} JP \\
&= I + \left(\sum_{k=0}^{\infty}\frac{(-1)^k \theta^{2k}}{(2k)!} - 1\right) P + \left(\sum_{k=1}^{\infty}\frac{(-1)^{k-1}\theta^{2k-1}}{(2k-1)!}\right) JP \\
&= I + (\cos\theta - 1) P + (\sin\theta) JP
\end{aligned}
$$

したがって，

$$
\finalanswer{f_1(\theta) = 1,\qquad f_2(\theta) = \cos\theta - 1,\qquad f_3(\theta) = \sin\theta}
$$

### (5)
$R = \exp(\theta J(\vec{a})) = I + (\cos\theta - 1)P(\vec{a}) + \sin\theta\,J(\vec{a})P(\vec{a})$ とおきます。問3の (i), (ii) および $\vec{a}\times\vec{b} = \vec{c},\ \vec{a}\times\vec{c} = -\vec{b}$ を用いて各基底への作用を計算します。

- $\vec{a}$ への作用：$P(\vec{a})\vec{a} = \vec{0}$ より，
  $$
  R\vec{a} = \vec{a}
  $$
- $\vec{b}$ への作用：$P(\vec{a})\vec{b} = \vec{b}$，$J(\vec{a})\vec{b} = \vec{a}\times\vec{b} = \vec{c}$ より，
  $$
  R\vec{b} = \vec{b} + (\cos\theta - 1)\vec{b} + \sin\theta\,\vec{c} = \cos\theta\,\vec{b} + \sin\theta\,\vec{c}
  $$
- $\vec{c}$ への作用：$\vec{c} \perp \vec{a}$ なので $P(\vec{a})\vec{c} = \vec{c}$，$J(\vec{a})\vec{c} = \vec{a}\times\vec{c} = -\vec{b}$ より，
  $$
  R\vec{c} = \vec{c} + (\cos\theta - 1)\vec{c} + \sin\theta(-\vec{b}) = -\sin\theta\,\vec{b} + \cos\theta\,\vec{c}
  $$

よって $R$ は $\vec{a}$ 方向を不変に保ち，$\vec{a}$ に直交する右手系平面（基底 $\vec{b}, \vec{c}$）内でベクトルを角度 $\theta$ だけ回転させるため，$\vec{a}$ を軸とした角度 $\theta$ の回転を表します。

### (6)
$R = \exp(\theta J(\vec{a}))$ とおくと $R^{-1} = \exp(-\theta J(\vec{a}))$ です。問5より $R$ は3次元回転行列（$\det R = 1,\ R^{\mathrm{T}}R = I$）なので，任意の2つのベクトル $\vec{u}, \vec{v}$ に対して外積を保ちます（$R(\vec{u}\times\vec{v}) = (R\vec{u})\times(R\vec{v})$）。

したがって任意のベクトル $\vec{x}$ に対して次式が成り立ちます。

$$
\begin{aligned}
\left(R J(\vec{b}) R^{-1}\right)\vec{x}
&= R\left(\vec{b}\times(R^{-1}\vec{x})\right) \\
&= (R\vec{b})\times(R R^{-1}\vec{x}) \\
&= (R\vec{b})\times\vec{x} = J(R\vec{b})\vec{x}
\end{aligned}
$$

よって $R J(\vec{b}) R^{-1} = J(R\vec{b})$ であり，任意の非負整数 $n$ に対して $R J(\vec{b})^n R^{-1} = J(R\vec{b})^n$ です。これを指数関数の級数展開に用います。

$$
\begin{aligned}
R\exp(\varphi J(\vec{b})) R^{-1}
&= \sum_{n=0}^{\infty}\frac{\varphi^n}{n!} R J(\vec{b})^n R^{-1} \\
&= \sum_{n=0}^{\infty}\frac{\varphi^n}{n!} J(R\vec{b})^n = \exp\bigl(\varphi J(R\vec{b})\bigr)
\end{aligned}
$$

問5より $R\vec{b} = \cos\theta\,\vec{b} + \sin\theta\,\vec{c}$ は単位ベクトルです。よって $\vec{e} = \cos\theta\,\vec{b} + \sin\theta\,\vec{c}$，$\chi = \varphi$ と選べます（また符号を同時に反転した $\vec{e} = -(\cos\theta\,\vec{b} + \sin\theta\,\vec{c}),\ \chi = -\varphi$ も同じく成り立ちます）。したがって，

$$
\finalanswer{\vec{e} = \cos\theta\,\vec{b} + \sin\theta\,\vec{c},\qquad \chi = \varphi}
$$

<aside class="rigor-note" markdown>
問4の公式 $\exp(\theta J(\vec{a})) = I + (\cos\theta - 1)P(\vec{a}) + \sin\theta\,J(\vec{a}) = I + \sin\theta\,J(\vec{a}) + (1 - \cos\theta)J(\vec{a})^2$ はロドリゲス（Rodrigues）の回転公式と呼ばれ，3次元回転群 $\mathrm{SO}(3)$ のリー代数 $\mathfrak{so}(3)$ からの指数写像を陽に与える基本公式です。
</aside>
