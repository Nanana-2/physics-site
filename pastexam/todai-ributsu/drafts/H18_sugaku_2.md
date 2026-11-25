---
title: 東大理物 平成18年度 数学 第2問：変分法・ベルトラミの恒等式と最小回転面
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成18年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成18年度 数学 第2問：変分法・ベルトラミの恒等式と最小回転面

## 問題

以下の積分を考える。

$$
S = \int_{x_0}^{x_1} F\bigl(y(x), y'(x)\bigr)\,\mathrm{d}x. \tag{1}
$$

ここで，$y'(x) \equiv \mathrm{d}y(x)/\mathrm{d}x$ である。また，$F(y, y')$ および $y(x)$ は，いずれの変数についても何回でも微分可能な連続かつ一価な関数とする。さらに，曲線 $y = y(x)$ の端点は，$y(x_0) = y_0,\ y(x_1) = y_1$ のように固定されているものとする。以下の設問に答えよ。

(i) 積分 $S$ が曲線 $y = y(x)$ の変化に対して極値をとるための十分条件となる微分方程式を，関数 $y(x)$ の微小変分 $\delta y(x)$ を考える事で導出せよ。

(ii) 設問 (i) で求めた微分方程式は，

$$
F - y'\frac{\partial F}{\partial y'} = C,
$$

に変形できることを示せ。ここで，$C$ は定数である。

(iii) 曲線 $y = y(x)$ の両端点が $x_1 > x_0 > 0,\ y_1 > 0,\ y_0 > 0$ を満たすとする。この曲線を $x$ 軸のまわりに $360^\circ$ 回転して得られる回転面を考え，その表面積を (1) 式の形の積分を用いて表せ。

(iv) 設問 (iii) で得られた表面積を最小にする曲線 $y = y(x)$ が満たす微分方程式を導け。

(v) 設問 (iv) で得られた微分方程式を解き，曲線 $y(x)$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成18年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
端点を固定した微小変分 $\delta y(x)$ に対して積分の1次変分 $\delta S$ を計算し，部分積分で $\delta y'(x)$ の微分を隣の因子へ移すと，変分法の基本補題からオイラー・ラグランジュ方程式を導くことができます。

被積分関数 $F(y, y')$ が独立変数 $x$ を陽に含まないときは，2階のオイラー・ラグランジュ方程式を1階の保存量の式へ積分することができます。回転面の表面積も $x$ を陽に含まない汎関数なので，この1階微分方程式を変数分離で解いて曲線を求めることができます。
</div>

### (i)

端点が固定されているので，微小変分 $\delta y(x)$ は境界条件 $\delta y(x_0) = \delta y(x_1) = 0$ を満たします。$y(x)$ を $y(x) + \delta y(x)$ に変えたときの $S$ の1次変分 $\delta S$ を計算します。$\delta y'(x) = \dfrac{\mathrm{d}}{\mathrm{d}x}\delta y(x)$ を用いて第2項を部分積分します。

$$
\begin{aligned}
\delta S &= \int_{x_0}^{x_1} \left(\frac{\partial F}{\partial y}\delta y + \frac{\partial F}{\partial y'}\delta y'\right)\mathrm{d}x \\
&= \int_{x_0}^{x_1} \frac{\partial F}{\partial y}\delta y\,\mathrm{d}x + \left[\frac{\partial F}{\partial y'}\delta y\right]_{x_0}^{x_1} - \int_{x_0}^{x_1} \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right)\delta y\,\mathrm{d}x \\
&= \int_{x_0}^{x_1} \left\{\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right)\right\}\delta y(x)\,\mathrm{d}x
\end{aligned}
$$

ここで境界条件 $\delta y(x_0) = \delta y(x_1) = 0$ より境界項が $0$ になります。任意の微小変分 $\delta y(x)$ に対して停留条件 $\delta S = 0$ が成り立つためには，変分法の基本補題より被積分関数の中括弧内が恒等的に $0$ でなければなりません。

$$
\finalanswer{\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right) = 0}
$$

### (ii)

$F - y'\dfrac{\partial F}{\partial y'}$ を $x$ で全微分します。$F(y, y')$ は $x$ を陽に含まないため，$\dfrac{\mathrm{d}F}{\mathrm{d}x} = \dfrac{\partial F}{\partial y}y' + \dfrac{\partial F}{\partial y'}y''$ です。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}x}\left(F - y'\frac{\partial F}{\partial y'}\right) &= \left(\frac{\partial F}{\partial y}y' + \frac{\partial F}{\partial y'}y''\right) - y''\frac{\partial F}{\partial y'} - y'\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right) \\
&= y'\left\{\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right)\right\}
\end{aligned}
$$

設問 (i) のオイラー・ラグランジュ方程式より右辺の中括弧内は $0$ なので，次式が成り立ちます。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left(F - y'\frac{\partial F}{\partial y'}\right) = 0
$$

したがって，$x$ によらない定数 $C$ を用いて $F - y'\dfrac{\partial F}{\partial y'} = C$ と変形することができます。

### (iii)

曲線 $y = y(x)$ 上の微小弧長 $\mathrm{d}s$ は $\mathrm{d}s = \sqrt{(\mathrm{d}x)^2 + (\mathrm{d}y)^2} = \sqrt{1 + y'(x)^2}\,\mathrm{d}x$ です。この微小線分を $x$ 軸のまわりに $360^\circ$ 回転してできる帯の半径は $y(x)$ なので，その微小表面積 $\mathrm{d}S$ は $2\pi y(x)\,\mathrm{d}s$ です。

これを $x_0$ から $x_1$ まで積分すると，回転面の表面積 $S$ は式 (1) の形で次のように表されます。

$$
\finalanswer{S = 2\pi\int_{x_0}^{x_1} y(x)\sqrt{1 + y'(x)^2}\,\mathrm{d}x}
$$

### (iv)

設問 (iii) より被積分関数は $F(y, y') = 2\pi y\sqrt{1 + y'^2}$ です。$y'$ による偏微分を計算します。

$$
\frac{\partial F}{\partial y'} = \frac{2\pi y y'}{\sqrt{1 + y'^2}}
$$

これらを設問 (ii) の関係式 $F - y'\dfrac{\partial F}{\partial y'} = C$ に代入します。

$$
\begin{aligned}
2\pi y\sqrt{1 + y'^2} - y'\cdot\frac{2\pi y y'}{\sqrt{1 + y'^2}} &= C \\
2\pi y\frac{(1 + y'^2) - y'^2}{\sqrt{1 + y'^2}} &= C \\
\frac{2\pi y}{\sqrt{1 + y'^2}} &= C
\end{aligned}
$$

$c = \dfrac{C}{2\pi}$ とおきます。$y > 0$ より $c > 0$ です。両辺を2乗して $y'$ について整理します。

$$
\begin{aligned}
\frac{y^2}{1 + y'^2} &= c^2 \\
1 + y'^2 &= \frac{y^2}{c^2} \\
\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2 &= \frac{y^2}{c^2} - 1
\end{aligned}
$$

したがって，求める曲線が満たす微分方程式は正の定数 $c$ を用いて次式となります。

$$
\finalanswer{\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2 = \frac{y^2}{c^2} - 1}
$$

### (v)

設問 (iv) の微分方程式を変数分離して解きます。

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = \pm\frac{\sqrt{y^2 - c^2}}{c}
$$

$y = c\cosh t$ と置換します。$\mathrm{d}y = c\sinh t\,\mathrm{d}t$ であり，$\sqrt{y^2 - c^2} = c|\sinh t|$ です。$t$ の符号の取り方で $\pm$ を含めることができるため，次式になります。

$$
\begin{aligned}
\frac{c\sinh t\,\mathrm{d}t}{c\sinh t} &= \pm\frac{\mathrm{d}x}{c} \\
\mathrm{d}t &= \pm\frac{\mathrm{d}x}{c}
\end{aligned}
$$

両辺を積分すると，積分定数 $b$ を用いて $t = \pm\dfrac{x - b}{c}$ が得られます。$\cosh$ は偶関数なので $\pm$ の符号によらず同じ関数になります。

$$
y(x) = c\cosh\!\left(\frac{x - b}{c}\right)
$$

したがって，求める曲線は積分定数 $c > 0$ および $b$ を用いて次式となります。定数 $c, b$ は端点条件 $y(x_0) = y_0$，$y(x_1) = y_1$ から定まります。

$$
\finalanswer{y(x) = c\cosh\!\left(\frac{x - b}{c}\right)}
$$
