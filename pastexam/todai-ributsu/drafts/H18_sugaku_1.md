---
title: 東大理物 平成18年度 数学 第1問：エルミート行列の射影演算子とスペクトル分解
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成18年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成18年度 数学 第1問：エルミート行列の射影演算子とスペクトル分解

## 問題

複素数を成分とする $n$ 行 $1$ 列（$n \ge 1$）の縦ベクトル全体の集合 $\mathbb{C}^n$ は，$n$ 次元の複素線形空間をなす。2つのベクトル $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^n$ について，その内積 $(\boldsymbol{x}, \boldsymbol{y})$ を，$(\boldsymbol{x}, \boldsymbol{y}) \equiv \boldsymbol{x}^\dagger\boldsymbol{y}$ にて定義する。ただし，$\boldsymbol{x}^\dagger$ は $\boldsymbol{x}$ のエルミート共役（転置の複素共役）を表す。$\|\boldsymbol{x}\| \equiv \sqrt{(\boldsymbol{x}, \boldsymbol{x})}$ を $\boldsymbol{x}$ のノルムと言う。$A$ を $n$ 行 $n$ 列のエルミート行列とし，その固有値はどれも縮退がないとする。固有値 $a$ に対応する（属する）規格化された固有ベクトルを $\boldsymbol{u}_a$ と記す。即ち，

$$
A\boldsymbol{u}_a = a\boldsymbol{u}_a, \qquad (\boldsymbol{u}_a, \boldsymbol{u}_{a'}) = \delta_{a, a'}.
$$

固有値 $a$ は全て実数である。また，全ての $a$ について $\boldsymbol{u}_a$ を集めた集合 $\{\boldsymbol{u}_a\}$ は，$\mathbb{C}^n$ の正規直交完全系を成す。以下の設問に答えよ。

(i) 各固有値 $a$ ごとに，次の行列を定義する：

$$
P(a) \equiv \boldsymbol{u}_a\boldsymbol{u}_a^\dagger.
$$

このとき，次の等式が成り立つことを示せ：

$$
P(a)P(a') = \delta_{a, a'}P(a).
$$

(ii) 適当に選んだベクトル $\boldsymbol{x}$ について，もしも $P(a)\boldsymbol{x}$ がゼロベクトルでなければ，$P(a)\boldsymbol{x}$ は固有値 $a$ に対する $A$ の固有ベクトルであることを示せ。

(iii) 次の等式を示せ：

$$
A = \sum_a a P(a).
$$

即ち，任意の $\boldsymbol{x} \in \mathbb{C}^n$ について，$A\boldsymbol{x} = \sum_a a P(a)\boldsymbol{x}$ を示せ。

(iv) 固有値 $a$ の全てについて定義された関数 $f(a)$ を用いて，次の行列 $f(A)$ を定義する：

$$
f(A) \equiv \sum_a f(a)P(a).
$$

$f(A)$ の固有値と固有ベクトルが，それぞれ $f(a),\ \boldsymbol{u}_a$ で与えられることを示せ。

(v) $A$ の最小固有値を $a_0$ とする。適当に選んだベクトル $\boldsymbol{x}$ について，$P(a_0)\boldsymbol{x}$ がゼロベクトルでなかったとする。このとき，

$$
\boldsymbol{v} \equiv \lim_{t \to \infty} \frac{e^{-At}\boldsymbol{x}}{\|e^{-At}\boldsymbol{x}\|}
$$

とおくと，$\boldsymbol{v}$ が $a_0$ に対応する固有ベクトルであることを示せ。ただし，$t$ を任意の実数として，$f(a) = e^{-at}$ と選んだ場合の $f(A)$ を $e^{-At}$ と記した。

> 出典：東京大学大学院理学系研究科物理学専攻 平成18年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
エルミート行列の正規直交固有ベクトルから作る行列 $P(a) = \boldsymbol{u}_a\boldsymbol{u}_a^\dagger$ は，任意のベクトルから固有値 $a$ の成分だけを取り出す射影行列です。異なる固有値の射影行列同士を掛けると $0$ になり，同じものを掛けると元に戻るという性質によって，行列の関数 $f(A)$ の作用を各固有値の成分ごとに独立に計算することができます。

行列指数関数 $e^{-At}$ をベクトルに作用させると，各固有成分に重み $e^{-at}$ が掛かります。最小固有値 $a_0$ の因子 $e^{-a_0 t}$ をくくり出すと，他の固有値の成分はすべて $t \to \infty$ で指数関数的に減衰するため，最小固有値に対応する固有ベクトルを取り出すことができます。
</div>

### (i)

行列の積の結合法則と正規直交性 $\boldsymbol{u}_a^\dagger \boldsymbol{u}_{a'} = (\boldsymbol{u}_a, \boldsymbol{u}_{a'}) = \delta_{a, a'}$ を用いて計算します。

$$
\begin{aligned}
P(a)P(a') &= (\boldsymbol{u}_a\boldsymbol{u}_a^\dagger)(\boldsymbol{u}_{a'}\boldsymbol{u}_{a'}^\dagger) \\
&= \boldsymbol{u}_a(\boldsymbol{u}_a^\dagger\boldsymbol{u}_{a'})\boldsymbol{u}_{a'}^\dagger \\
&= \boldsymbol{u}_a\,\delta_{a, a'}\,\boldsymbol{u}_{a'}^\dagger \\
&= \delta_{a, a'}\,\boldsymbol{u}_a\boldsymbol{u}_a^\dagger \\
&= \delta_{a, a'}P(a)
\end{aligned}
$$

ここで $\delta_{a, a'}$ は $a = a'$ のときのみ $1$ でそれ以外は $0$ なので，$\delta_{a, a'}\boldsymbol{u}_{a'}^\dagger = \delta_{a, a'}\boldsymbol{u}_a^\dagger$ を用いました。

### (ii)

任意のベクトル $\boldsymbol{x} \in \mathbb{C}^n$ に対して，$P(a)\boldsymbol{x} = \boldsymbol{u}_a(\boldsymbol{u}_a^\dagger\boldsymbol{x})$ です。ここで $\boldsymbol{u}_a^\dagger\boldsymbol{x} = (\boldsymbol{u}_a, \boldsymbol{x})$ は複素数なので，$A$ と交換することができます。$A\boldsymbol{u}_a = a\boldsymbol{u}_a$ を用いて $A\bigl(P(a)\boldsymbol{x}\bigr)$ を計算します。

$$
\begin{aligned}
A\bigl(P(a)\boldsymbol{x}\bigr) &= A\bigl(\boldsymbol{u}_a(\boldsymbol{u}_a^\dagger\boldsymbol{x})\bigr) \\
&= (A\boldsymbol{u}_a)(\boldsymbol{u}_a^\dagger\boldsymbol{x}) \\
&= (a\boldsymbol{u}_a)(\boldsymbol{u}_a^\dagger\boldsymbol{x}) \\
&= a\bigl(\boldsymbol{u}_a(\boldsymbol{u}_a^\dagger\boldsymbol{x})\bigr) \\
&= a\bigl(P(a)\boldsymbol{x}\bigr)
\end{aligned}
$$

$P(a)\boldsymbol{x} \neq \boldsymbol{0}$ であることから，$P(a)\boldsymbol{x}$ は固有値 $a$ に対する $A$ の固有ベクトルです。

### (iii)

$\{\boldsymbol{u}_a\}$ は $\mathbb{C}^n$ の正規直交完全系なので，任意のベクトル $\boldsymbol{x} \in \mathbb{C}^n$ は複素係数 $c_a$ を用いて $\boldsymbol{x} = \sum_a c_a\boldsymbol{u}_a$ と一意に展開することができます。この両辺と $\boldsymbol{u}_{a'}$ の内積をとります。

$$
\begin{aligned}
(\boldsymbol{u}_{a'}, \boldsymbol{x}) &= \left(\boldsymbol{u}_{a'}, \sum_a c_a\boldsymbol{u}_a\right) \\
&= \sum_a c_a(\boldsymbol{u}_{a'}, \boldsymbol{u}_a) \\
&= \sum_a c_a\delta_{a', a} \\
&= c_{a'}
\end{aligned}
$$

よって $c_a = (\boldsymbol{u}_a, \boldsymbol{x}) = \boldsymbol{u}_a^\dagger\boldsymbol{x}$ であり，任意の $\boldsymbol{x}$ は次のように表されます。

$$
\begin{aligned}
\boldsymbol{x} &= \sum_a (\boldsymbol{u}_a^\dagger\boldsymbol{x})\boldsymbol{u}_a \\
&= \sum_a \boldsymbol{u}_a(\boldsymbol{u}_a^\dagger\boldsymbol{x}) \\
&= \sum_a P(a)\boldsymbol{x}
\end{aligned}
$$

この両辺に左から $A$ を掛けて，設問 (ii) の結果 $AP(a)\boldsymbol{x} = aP(a)\boldsymbol{x}$ を用います。

$$
\begin{aligned}
A\boldsymbol{x} &= A\left(\sum_a P(a)\boldsymbol{x}\right) \\
&= \sum_a A\bigl(P(a)\boldsymbol{x}\bigr) \\
&= \sum_a a P(a)\boldsymbol{x}
\end{aligned}
$$

これが任意の $\boldsymbol{x} \in \mathbb{C}^n$ について成り立つので，$A = \sum_a a P(a)$ です。

### (iv)

任意の固有値 $a'$ に対応する固有ベクトル $\boldsymbol{u}_{a'}$ に $f(A) = \sum_a f(a)P(a)$ を作用させます。正規直交性 $\boldsymbol{u}_a^\dagger\boldsymbol{u}_{a'} = \delta_{a, a'}$ を用います。

$$
\begin{aligned}
f(A)\boldsymbol{u}_{a'} &= \sum_a f(a)P(a)\boldsymbol{u}_{a'} \\
&= \sum_a f(a)\boldsymbol{u}_a(\boldsymbol{u}_a^\dagger\boldsymbol{u}_{a'}) \\
&= \sum_a f(a)\delta_{a, a'}\boldsymbol{u}_a \\
&= f(a')\boldsymbol{u}_{a'}
\end{aligned}
$$

$\boldsymbol{u}_{a'}$ はノルムが $1$ でゼロベクトルではないため，$\boldsymbol{u}_{a'}$ は固有値 $f(a')$ に対する $f(A)$ の固有ベクトルです。

また，$\{\boldsymbol{u}_a\}$ は $n$ 個の線形独立なベクトルからなる $\mathbb{C}^n$ の基底なので，$f(A)$ は固有ベクトル $\{\boldsymbol{u}_a\}$ によって対角化され，固有値はすべて $f(a)$ で尽くされます。したがって，$f(A)$ の固有値と固有ベクトルはそれぞれ $f(a)$，$\boldsymbol{u}_a$ で与えられます。

### (v)

定義より $e^{-At}\boldsymbol{x} = \sum_a e^{-at}P(a)\boldsymbol{x}$ です。最小固有値 $a_0$ の項を分けて $e^{-a_0 t}$ をくくり出します。

$$
\begin{aligned}
e^{-At}\boldsymbol{x} &= e^{-a_0 t}P(a_0)\boldsymbol{x} + \sum_{a \neq a_0} e^{-at}P(a)\boldsymbol{x} \\
&= e^{-a_0 t}\left(P(a_0)\boldsymbol{x} + \sum_{a \neq a_0} e^{-(a - a_0)t}P(a)\boldsymbol{x}\right)
\end{aligned}
$$

$a_0$ は実数なので $e^{-a_0 t} > 0$ です。よって，ノルムについても正の因子 $e^{-a_0 t}$ を外に出して分子と分母から約分することができます。

$$
\begin{aligned}
\frac{e^{-At}\boldsymbol{x}}{\|e^{-At}\boldsymbol{x}\|} &= \frac{e^{-a_0 t}\left(P(a_0)\boldsymbol{x} + \displaystyle\sum_{a \neq a_0} e^{-(a - a_0)t}P(a)\boldsymbol{x}\right)}{e^{-a_0 t}\left\|P(a_0)\boldsymbol{x} + \displaystyle\sum_{a \neq a_0} e^{-(a - a_0)t}P(a)\boldsymbol{x}\right\|} \\
&= \frac{P(a_0)\boldsymbol{x} + \displaystyle\sum_{a \neq a_0} e^{-(a - a_0)t}P(a)\boldsymbol{x}}{\left\|P(a_0)\boldsymbol{x} + \displaystyle\sum_{a \neq a_0} e^{-(a - a_0)t}P(a)\boldsymbol{x}\right\|}
\end{aligned}
$$

$A$ の固有値に縮退がなく $a_0$ が最小固有値なので，すべての $a \neq a_0$ に対して $a - a_0 > 0$ です。したがって $t \to \infty$ の極限で $e^{-(a - a_0)t} \to 0$ となり，仮定 $P(a_0)\boldsymbol{x} \neq \boldsymbol{0}$ より分母の極限 $\|P(a_0)\boldsymbol{x}\|$ は $0$ でありません。よって極限 $\boldsymbol{v}$ は次式になります。

$$
\boldsymbol{v} = \frac{P(a_0)\boldsymbol{x}}{\|P(a_0)\boldsymbol{x}\|}
$$

$\boldsymbol{v}$ はノルム $1$ のゼロでないベクトルであり，設問 (ii) より $P(a_0)\boldsymbol{x}$ は固有値 $a_0$ の固有ベクトルなので，その定数倍である $\boldsymbol{v}$ も固有値 $a_0$ に対応する $A$ の固有ベクトルです。
