---
title: 東大理物 平成9年度 一般教育科目 数学 第2問：上半平面の測地線方程式
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 一般教育科目 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成9年度 一般教育科目 数学 第2問：上半平面の測地線方程式

## 問題

2次元 $(x, y)$ 平面の上半面（$-\infty < x < \infty,\ y > 0$）における，なめらかな曲線を考える。曲線は，実数パラメータ $s$ によって $(x(s), y(s))$ と表され，次の微分方程式を満たすものとする。

$$
\left.
\begin{aligned}
y x'' - 2 x' y' &= 0 \\
y y'' + x'^2 - y'^2 &= 0
\end{aligned}
\right\} \qquad \text{(1)}
$$

ただし，関数 $x(s)$ は2階微分可能で，$x' = \mathrm{d}x/\mathrm{d}s$，$x'' = \mathrm{d}^2x/\mathrm{d}s^2$ および $x'^2 = (\mathrm{d}x/\mathrm{d}s)^2$ である。関数 $y(s)$ についても同様である。以下の設問に答えよ。
{: .problem-lead }

(a) 新しい変数

$$
X = \frac{x'}{y}, \qquad Y = \frac{y'}{y} \qquad \text{(2)}
$$

を導入して，変数 $X(s)$ と $Y(s)$ の満たすべき方程式を求めよ。さらに，次の関係

$$
X^2 + Y^2 = C \qquad \text{(3)}
$$

が成り立つことを示せ。ただし，$C$ は定数である。

(b) 方程式 (1) を満たす $(x(s), y(s))$ はどのような曲線群を表すか。$X = 0$ と $X \neq 0$ の場合に分けて，それぞれについて求めよ。ただし，$C = 1$ としてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 一般教育科目 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2階の連立非線形微分方程式に対して $X = x'/y$，$Y = y'/y$ とおくと，$X, Y$ の1階連立微分方程式へと次数を下げることができます。保存量 $X^2 + Y^2 = C$ を導いたのち，$X = 0$ の場合と $X \neq 0$ の場合に分けて積分すれば，$x$ 軸に直交する半直線群と $x$ 軸上に中心をもつ上半円群というポアンカレ上半平面の測地線が得られます。
</div>

### (a)

定義式 $X = \dfrac{x'}{y}$ と $Y = \dfrac{y'}{y}$ をそれぞれパラメータ $s$ で微分します。

$$
\begin{aligned}
X' &= \frac{x'' y - x' y'}{y^2} \\
&= \frac{y x'' - 2 x' y' + x' y'}{y^2}
\end{aligned}
$$

ここで式 (1) の第1式 $y x'' - 2 x' y' = 0$ を用いると，次式が得られます。

$$
\begin{aligned}
X' &= \frac{x' y'}{y^2} \\
&= X Y
\end{aligned}
$$

同様に $Y$ を $s$ で微分します。

$$
\begin{aligned}
Y' &= \frac{y'' y - y'^2}{y^2} \\
&= \frac{y y'' + x'^2 - y'^2 - x'^2}{y^2}
\end{aligned}
$$

式 (1) の第2式 $y y'' + x'^2 - y'^2 = 0$ を用いると，次式となります。

$$
\begin{aligned}
Y' &= -\frac{x'^2}{y^2} \\
&= -X^2
\end{aligned}
$$

次に $X^2 + Y^2$ を $s$ で微分し，いま得られた方程式を代入します。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}s}(X^2 + Y^2) &= 2 X X' + 2 Y Y' \\
&= 2 X (X Y) + 2 Y (-X^2) \\
&= 2 X^2 Y - 2 X^2 Y \\
&= 0
\end{aligned}
$$

導関数が恒等的に $0$ であるため，$X^2 + Y^2$ は $s$ によらない定数 $C$ に等しくなり，式 (3) の $X^2 + Y^2 = C$ が成り立ちます。

$$
\finalanswer{X' = XY,\qquad Y' = -X^2}
$$

### (b)

$C = 1$ のとき $X^2 + Y^2 = 1$ が成り立ちます。なお，方程式 $X' = XY$ は線形なので，ある点で $X = 0$ ならば解の一意性よりすべての $s$ で $X(s) \equiv 0$ となり，逆に $X \neq 0$ ならばすべての $s$ で $X(s)$ の符号は一定に保たれます。したがって，$X = 0$ と $X \neq 0$ に完全に場合分けできます。

まず $X = 0$ の場合を考えます。$X = \dfrac{x'}{y}$ が $0$ であり $y > 0$ なので $x' = 0$ なので，実定数 $x_0$ を用いて

$$
x(s) = x_0
$$

となります。また $X^2 + Y^2 = 1$ より $Y = \pm 1$ であり，$\dfrac{y'}{y} = \pm 1$ を積分すると正の定数 $y_0 > 0$ を用いて

$$
y(s) = y_0 e^{\pm s}
$$

が得られます。$s$ が実数全体を動くとき $y(s)$ は $0 < y < \infty$ のすべての値をとるため，曲線 $(x(s), y(s))$ は $x$ 軸に垂直な上半面の半直線

$$
x = x_0, \qquad y > 0
$$

を表します。

次に $X \neq 0$ の場合を考えます。$X' = XY$ の両辺を $X$ で割ると，定義 $Y = \dfrac{y'}{y}$ を用いて次式が成り立ちます。

$$
\frac{X'}{X} = \frac{y'}{y}
$$

両辺を $s$ で積分すると，$\ln|X| = \ln y + \text{const.}$ となるため，正の定数 $R > 0$ を用いて

$$
X = \pm \frac{y}{R}
$$

となります。ここで複号は $X$ の符号に対応して一定です。$X^2 + Y^2 = 1$ より $X^2 \le 1$ なので $0 < y \le R$ であり，

$$
Y^2 = 1 - \frac{y^2}{R^2}
$$

が成り立ちます。また $x' = \pm \dfrac{y^2}{R}$ より $x(s)$ は単調であり，$Y' = -\dfrac{y^2}{R^2} < 0$ より $Y(s)$ は狭義単調減少します。

曲線の方程式を求めるため，$Y \neq 0$ の区間で $\dfrac{\mathrm{d}x}{\mathrm{d}y}$ を計算します。

$$
\begin{aligned}
\frac{\mathrm{d}x}{\mathrm{d}y} &= \frac{x'}{y'} \\
&= \frac{X}{Y}
\end{aligned}
$$

一方で，微分方程式 $X' = XY$ と $Y' = -X^2$ から $x' = yX$ と $y' = yY$ に注目すると，直接に $(x, y)$ の関係を導くこともできます。実際，$X = \pm\dfrac{y}{R}$ より $y = \pm R X$ であり，これを $s$ で微分すると

$$
\begin{aligned}
y' &= \pm R X' \\
&= \pm R X Y \\
&= y Y
\end{aligned}
$$

が恒等的に満たされます。同様に符号 $\sigma \in \{+1, -1\}$ を用いて $X = \sigma \dfrac{y}{R}$ とおくと

$$
\begin{aligned}
x' &= y X \\
&= \sigma R X^2 \\
&= -\sigma R Y'
\end{aligned}
$$

が得られます。これを $s$ で積分すると，実定数 $x_0$ を用いて

$$
x(s) - x_0 = -\sigma R Y(s)
$$

となります。これと $y(s) = \sigma R X(s)$ の2乗和をとれば，$X^2 + Y^2 = 1$ より次式が得られます。

$$
\begin{aligned}
(x - x_0)^2 + y^2 &= R^2(Y^2 + X^2) \\
&= R^2
\end{aligned}
$$

パラメータ表示も明示的に求まります。$Y' = -(1 - Y^2)$ を解くと，積分定数 $s_0$ を用いて $Y(s) = -\tanh(s - s_0)$ となり，$X(s) = \sigma\operatorname{sech}(s - s_0)$ なので

$$
x(s) = x_0 + \sigma R\tanh(s - s_0), \qquad y(s) = R\operatorname{sech}(s - s_0)
$$

となります。$s$ が $-\infty < s < \infty$ を動くとき $\tanh(s - s_0)$ は $(-1, 1)$ 全体を，$\operatorname{sech}(s - s_0)$ は $(0, 1]$ を動くため，曲線 $(x(s), y(s))$ は $x$ 軸上の点 $(x_0, 0)$ を中心とし半径 $R > 0$ をもつ上半円

$$
(x - x_0)^2 + y^2 = R^2, \qquad y > 0
$$

全体を描きます。

<div class="rigor-note" markdown>
この微分方程式 (1) は，上半平面 $y > 0$ にリーマン計量 $\mathrm{d}\ell^2 = \dfrac{\mathrm{d}x^2 + \mathrm{d}y^2}{y^2}$ を入れた双曲幾何学のポアンカレ上半平面モデルにおける測地線方程式であり，条件 $X^2 + Y^2 = 1$ はパラメータ $s$ が双曲弧長であることを表します。
</div>

$$
\finalanswer{X = 0:\ x = x_0\ (y > 0),\qquad X \neq 0:\ (x - x_0)^2 + y^2 = R^2\ (y > 0,\ R > 0)}
$$
