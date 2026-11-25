---
title: 東大理物 平成23年度 数学 第2問：1次元・2次元・d次元のポアソン方程式とラプラス方程式
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成23年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成23年度 数学 第2問：1次元・2次元・d次元のポアソン方程式とラプラス方程式

## 問題

以下ではポアソン方程式，またはラプラス方程式の解を様々な次元 ($d$)，境界条件の下で求める。

(1) まず1次元（$d = 1$）の場合を考える。

(i) 領域 $x \in [0, 1]$ で定義された連続関数 $u(x)$ に対する微分方程式

$$
\frac{\mathrm{d}^2 u}{\mathrm{d}x^2} = -\delta(x - y), \qquad 0 < y < 1
$$

を境界条件 $u(0) = u(1) = 0$ の下で解け。ここで $\delta(x)$ はデルタ関数である。

(ii) 上で得られた解 $u(x)$ を $G(x, y)$ と書く。このとき領域 $x \in [0, 1]$ で定義される，より一般的な微分方程式

$$
\frac{\mathrm{d}^2 v}{\mathrm{d}x^2} = \rho(x)
$$

の解 $v(x)$ を $G(x, y)$ を用いて書き下せ。ただし境界条件は $v(0) = v(1) = 0$ とし，右辺の $\rho(x)$ は $\rho(0) = \rho(1) = 0$ を満たす任意関数とする。

(2) 次に2次元（$d = 2$）の場合を考える。2次元平面の直交座標を $(x, y)$，複素座標を $z = x + iy, \bar{z} = x - iy$，極座標を $r, \theta$（$x = r\cos\theta, y = r\sin\theta$）とする。

(i) 単位円の内部（$r < 1$）で定義された関数 $u_n(x, y) = z^n + \bar{z}^n$（$n = 0, 1, 2, \cdots$）はラプラス方程式

$$
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right) u(x, y) = 0
$$

の解であることを示せ。またこの関数は境界（$r = 1$）でどのような値をとるのか，$\theta$ の関数として表せ。

(ii) 単位円の内部 $r < 1$ でラプラス方程式を満たし，境界条件

$$
\left.u(x, y)\right|_{r=1} = |\theta|, \qquad -\pi \le \theta \le \pi
$$

を満たす関数 $u$ を，境界値に対するフーリエ級数展開を用いて求めよ。

(3) $d$ 次元（$d \ge 3$）ポアソン方程式

$$
\nabla \cdot \nabla u(\boldsymbol{x}) = -\prod_{a=1}^d \delta(x_a), \qquad \boldsymbol{x} = (x_1, \cdots, x_d), \qquad \nabla = \left(\frac{\partial}{\partial x_1}, \cdots, \frac{\partial}{\partial x_d}\right)
$$

を，定義域 $\mathbb{R}^d$，境界条件 $\lim_{|\boldsymbol{x}|\to\infty} u(\boldsymbol{x}) = 0$ の下で考える。発散定理

$$
\int_V \mathrm{d}^d x\,\nabla \cdot \boldsymbol{F} = \int_{\partial V} \mathrm{d}S\,\boldsymbol{n} \cdot \boldsymbol{F}
$$

を用いて解 $u(\boldsymbol{x})$ を求めよ。ここで $V$ は $\mathbb{R}^d$ 内のなめらかな境界 $\partial V$ を持つ有界な領域，$\boldsymbol{F}$ はベクトル値関数，$\boldsymbol{n}$ は $\partial V$ 上の単位法線ベクトル，$\mathrm{d}S$ は $\partial V$ の超面積要素である。（必要であれば $d$ 次元空間内の半径 $1$ の超球面 $\sum_{i=1}^d (x_i)^2 = 1$ の超面積が $\dfrac{2\pi^{d/2}}{\Gamma(d/2)}$ であることを用いても良い。ここで $\Gamma(z)$ はガンマ関数である。）

> 出典：東京大学大学院理学系研究科物理学専攻 平成23年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
右辺がデルタ関数の方程式では，$x\neq y$ で $u''=0$ なので，$u$ は $x<y$ と $x>y$ でそれぞれ1次関数になります。$x=y$ での $u'$ の跳びは，両辺を $y$ をはさむ短い区間で積分して求めます。

グリーン関数 $G(x,y)$ は，点 $y$ に置いたデルタ関数に対する解です。一般の右辺 $\rho(x)$ はデルタ関数の重ね合わせとみることができるので，$v(x)$ は $G(x,y)$ と $\rho(y)$ の積を $y$ で積分して作ります。

2次元では，複素座標を使うとラプラシアンは $\partial_z$ と $\partial_{\bar{z}}$ の積に比例します。そのため，$z$ だけの関数や $\bar{z}$ だけの関数はラプラス方程式を満たします。境界値をフーリエ級数に展開し，各項に (2)(i) の $u_n$ を対応させると，円の内部の解を作ることができます。

$d\geq3$ のポアソン方程式では，右辺のデルタ関数も境界条件も原点のまわりの回転で変わりません。そのため，解は原点からの距離 $r$ だけの関数とみて，半径 $r$ の球に発散定理を用いて $u'(r)$ を求めます。
</div>

### (1)(i)
$x \neq y$ では $\dfrac{\mathrm{d}^2 u}{\mathrm{d}x^2} = 0$ なので，$u(x)$ は $[0, y]$ と $[y, 1]$ のそれぞれで1次関数です。境界条件 $u(0) = 0$，$u(1) = 0$ より，定数 $c_1, c_2$ を用いて次のように置くことができます。

$$
u(x) = \begin{cases} c_1 x & (0 \le x \le y) \\ c_2(1 - x) & (y \le x \le 1) \end{cases}
$$

$u(x)$ は $x = y$ で連続なので，$c_1 y = c_2(1 - y)$ が成り立ちます。次に微分方程式の両辺を $y - \epsilon$ から $y + \epsilon$ まで積分し，$\epsilon \to 0+$ の極限をとります。

$$
\begin{aligned}
\lim_{\epsilon \to 0+}\bigl(u'(y + \epsilon) - u'(y - \epsilon)\bigr) &= -1 \\
-c_2 - c_1 &= -1 \\
c_1 + c_2 &= 1
\end{aligned}
$$

$c_1 y = c_2(1 - y)$ と $c_1 + c_2 = 1$ を連立して解くと，$c_1 = 1 - y$，$c_2 = y$ です。したがって求める解は次のとおりです。

$$
\finalanswer{u(x) = \begin{cases} x(1 - y) & (0 \le x \le y) \\ y(1 - x) & (y \le x \le 1) \end{cases}}
$$

### (1)(ii)
$G(x, y)$ は $\dfrac{\partial^2 G(x, y)}{\partial x^2} = -\delta(x - y)$ および $G(0, y) = G(1, y) = 0$ を満たします。符号に注意して

$$
v(x) = -\int_0^1 G(x, y)\rho(y)\,\mathrm{d}y
$$

とおくと，境界条件 $v(0) = v(1) = 0$ を満たし，2階微分は次のようになります。

$$
\begin{aligned}
\frac{\mathrm{d}^2 v}{\mathrm{d}x^2} &= -\int_0^1 \frac{\partial^2 G(x, y)}{\partial x^2}\rho(y)\,\mathrm{d}y \\
&= -\int_0^1 \bigl(-\delta(x - y)\bigr)\rho(y)\,\mathrm{d}y \\
&= \rho(x)
\end{aligned}
$$

したがって求める解は次のとおりです。

$$
\finalanswer{v(x) = -\int_0^1 G(x, y)\rho(y)\,\mathrm{d}y}
$$

### (2)(i)
$z = x + iy$，$\bar{z} = x - iy$ より，偏微分演算子の変換を求めます。

$$
\begin{aligned}
\frac{\partial}{\partial x} &= \frac{\partial}{\partial z} + \frac{\partial}{\partial \bar{z}} \\
\frac{\partial}{\partial y} &= i\left(\frac{\partial}{\partial z} - \frac{\partial}{\partial \bar{z}}\right)
\end{aligned}
$$

これらを2乗して加えると，2次元のラプラシアンは次式になります。

$$
\begin{aligned}
\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} &= \left(\frac{\partial}{\partial z} + \frac{\partial}{\partial \bar{z}}\right)^2 - \left(\frac{\partial}{\partial z} - \frac{\partial}{\partial \bar{z}}\right)^2 \\
&= 4\frac{\partial^2}{\partial z \partial \bar{z}}
\end{aligned}
$$

$z^n$ は $\bar{z}$ に依存せず，$\bar{z}^n$ は $z$ に依存しないので，$u_n(x, y) = z^n + \bar{z}^n$ に対して次式が成り立ちます。

$$
\begin{aligned}
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right) u_n(x, y) &= 4\frac{\partial^2}{\partial z \partial \bar{z}}\left(z^n + \bar{z}^n\right) \\
&= 0
\end{aligned}
$$

よって $u_n(x, y)$ はラプラス方程式の解です。また極座標で表すと $z = r e^{i\theta}$，$\bar{z} = r e^{-i\theta}$ より $u_n(x, y) = r^n(e^{in\theta} + e^{-in\theta}) = 2r^n \cos(n\theta)$ なので，境界 $r = 1$ での値は次のとおりです。

$$
\finalanswer{\left.u_n(x, y)\right|_{r=1} = 2\cos(n\theta)}
$$

### (2)(ii)
境界値 $|\theta|$ は $[-\pi, \pi]$ 上の偶関数なので，フーリエ余弦級数

$$
|\theta| = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos(n\theta)
$$

に展開します。係数 $a_0$ と $a_n$（$n \ge 1$）を計算します。

$$
\begin{aligned}
a_0 &= \frac{2}{\pi}\int_0^{\pi} \theta\,\mathrm{d}\theta \\
&= \frac{2}{\pi}\left[\frac{\theta^2}{2}\right]_0^{\pi} \\
&= \pi
\end{aligned}
$$

$$
\begin{aligned}
a_n &= \frac{2}{\pi}\int_0^{\pi} \theta\cos(n\theta)\,\mathrm{d}\theta \\
&= \frac{2}{\pi}\left[\frac{\theta\sin(n\theta)}{n} + \frac{\cos(n\theta)}{n^2}\right]_0^{\pi} \\
&= \frac{2}{\pi n^2}\bigl((-1)^n - 1\bigr)
\end{aligned}
$$

$n$ が偶数のとき $a_n = 0$，$n = 2k + 1$（$k = 0, 1, 2, \dots$）が奇数のとき $a_{2k+1} = -\dfrac{4}{\pi(2k+1)^2}$ です。よって境界値のフーリエ級数展開は次式になります。

$$
|\theta| = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{\cos\bigl((2k + 1)\theta\bigr)}{(2k + 1)^2}
$$

設問 (2)(i) より $r^n \cos(n\theta) = \dfrac{1}{2}u_n(x, y)$ は $r < 1$ でラプラス方程式を満たし，境界 $r = 1$ で $\cos(n\theta)$ になります。線形結合をとることで，求める解 $u$ が得られます。

$$
\finalanswer{u(r, \theta) = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{r^{2k+1}\cos\bigl((2k + 1)\theta\bigr)}{(2k + 1)^2}}
$$

### (3)
方程式と境界条件は原点周りの回転に対して不変なので，解 $u(\boldsymbol{x})$ は原点からの距離 $r = |\boldsymbol{x}|$ のみの関数 $u(r)$ です。このとき勾配は $\nabla u(\boldsymbol{x}) = u'(r)\dfrac{\boldsymbol{x}}{r}$ となります。

原点を中心とする半径 $R > 0$ の $d$ 次元球 $V = \{\boldsymbol{x} \in \mathbb{R}^d : |\boldsymbol{x}| \le R\}$ に対して $\boldsymbol{F} = \nabla u$ とし，ポアソン方程式の両辺を $V$ 上で積分して発散定理を用います。境界 $\partial V$ 上で単位法線ベクトルは $\boldsymbol{n} = \dfrac{\boldsymbol{x}}{R}$ であり，半径 $R$ の超球面の超面積は $S_d R^{d-1}$ です。ここで $S_d = \dfrac{2\pi^{d/2}}{\Gamma(d/2)}$ とおきました。

$$
\begin{aligned}
\int_V \mathrm{d}^d x\,\nabla \cdot \nabla u(\boldsymbol{x}) &= \int_V \mathrm{d}^d x\left(-\prod_{a=1}^d \delta(x_a)\right) \\
\int_{\partial V} \mathrm{d}S\,\boldsymbol{n}\cdot\nabla u &= -1 \\
u'(R)\,S_d R^{d-1} &= -1 \\
u'(R) &= -\frac{1}{S_d} R^{1 - d}
\end{aligned}
$$

$d \ge 3$ なので $2 - d < 0$ であり，$\lim_{r \to \infty} u(r) = 0$ を用いて $r$ から $\infty$ まで積分します。

$$
\begin{aligned}
u(\infty) - u(r) &= -\frac{1}{S_d}\int_r^{\infty} R^{1 - d}\,\mathrm{d}R \\
-u(r) &= -\frac{1}{S_d}\left[\frac{R^{2 - d}}{2 - d}\right]_r^{\infty} \\
u(r) &= \frac{1}{(d - 2) S_d}\,\frac{1}{r^{d - 2}} \\
&= \frac{\Gamma(d/2)}{2(d - 2)\pi^{d/2}}\,\frac{1}{|\boldsymbol{x}|^{d - 2}}
\end{aligned}
$$

$$
\finalanswer{u(\boldsymbol{x}) = \frac{\Gamma(d/2)}{2(d - 2)\pi^{d/2}}\,\frac{1}{|\boldsymbol{x}|^{d - 2}}}
$$
