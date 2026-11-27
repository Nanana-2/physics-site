---
title: 東大理物 平成17年度 数学 第2問：フォッカー・プランク方程式のガウス解と定常分布への緩和
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成17年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成17年度 数学 第2問：フォッカー・プランク方程式のガウス解と定常分布への緩和

## 問題

$f(x, t)$ についての偏微分方程式

$$
\frac{\partial f}{\partial t} = \frac{\partial}{\partial x}(xf) + D\frac{\partial^2 f}{\partial x^2}
$$

を考える。$f$ および $\partial f/\partial x$ は，$x \to \pm\infty$ に対して十分速やかに $0$ に収束する。また，$D$ は正の定数とする。

(1) $x$ についての $f$ の定積分

$$
I = \int_{-\infty}^{\infty} f(x, t)\,\mathrm{d}x
$$

が保存されること，すなわち $\mathrm{d}I/\mathrm{d}t = 0$ であることを示せ。

(2) 原点 $x = 0$ を中心とするガウス分布関数

$$
g(x, \sigma) = \frac{1}{\sqrt{2\pi}\sigma}e^{-x^2/(2\sigma^2)} \qquad (\sigma\text{ は正の定数})
$$

が，はじめの偏微分方程式の定常解（すなわち，$\partial f/\partial t = 0$）であるとき，$\sigma$ はどう表せるか。

(3) 中心 $X(t)$，標準偏差 $\sigma(t)$（$X$ および $\sigma$ は $t$ の関数）のガウス分布関数

$$
f(x, t) = g\bigl(x - X(t), \sigma(t)\bigr)
$$

が，はじめの偏微分方程式の解になるために，$X(t)$ および $\sigma(t)$ の満たすべき常微分方程式を求めよ。

(4) はじめの偏微分方程式を，初期条件 $f(x, 0) = \delta(x - 1)$ のもとで解き，$t \to \infty$ において設問 (2) で求めた定常解に近づくことを示せ。（デルタ関数 $\delta(x - 1)$ は，$g(x - 1, \sigma)$ の $\sigma \to 0$ の極限であることを考慮せよ。）

> 出典：東京大学大学院理学系研究科物理学専攻 平成17年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
偏微分方程式の右辺は $\dfrac{\partial}{\partial x}\left(xf + D\dfrac{\partial f}{\partial x}\right)$ という全微分の形にまとまります。そのため $x$ について全空間で積分すると境界項だけになり，遠方での減衰条件から総積分 $I$ の保存をすぐ確かめることができます。

時間とともに中心 $X(t)$ と幅 $\sigma(t)$ が変化するガウス分布を方程式へ代入すると，両辺が $f(x, t)$ に $u = x - X(t)$ の2次多項式を掛けた形になります。すべての $u$ について係数を比較することで，偏微分方程式が $X(t)$ と $\sigma(t)$ の常微分方程式へ分解されます。
</div>

### (1)

積分 $I = \int_{-\infty}^{\infty} f(x, t)\,\mathrm{d}x$ を $t$ で微分し，与えられた偏微分方程式を代入します。右辺は $x$ に関する1階導関数の形にまとめることができます。

$$
\begin{aligned}
\frac{\mathrm{d}I}{\mathrm{d}t} &= \int_{-\infty}^{\infty} \frac{\partial f}{\partial t}\,\mathrm{d}x \\
&= \int_{-\infty}^{\infty} \frac{\partial}{\partial x}\left(xf + D\frac{\partial f}{\partial x}\right)\mathrm{d}x \\
&= \left[xf + D\frac{\partial f}{\partial x}\right]_{-\infty}^{\infty}
\end{aligned}
$$

仮定より $f$ および $\dfrac{\partial f}{\partial x}$ は $x \to \pm\infty$ で十分速やかに $0$ に収束するため，$xf \to 0$ かつ $\dfrac{\partial f}{\partial x} \to 0$ となります。したがって $\dfrac{\mathrm{d}I}{\mathrm{d}t} = 0$ であり，$I$ は保存されます。

### (2)

定常解では $\dfrac{\partial g}{\partial t} = 0$ なので，次式が成り立ちます。

$$
\frac{\partial}{\partial x}\left(xg + D\frac{\partial g}{\partial x}\right) = 0
$$

まず $g(x, \sigma) = \dfrac{1}{\sqrt{2\pi}\sigma}e^{-x^2/(2\sigma^2)}$ の1階導関数を計算します。

$$
\frac{\partial g}{\partial x} = -\frac{x}{\sigma^2}g
$$

これを用いて $xg + D\dfrac{\partial g}{\partial x}$ を計算します。

$$
\begin{aligned}
xg + D\frac{\partial g}{\partial x} &= xg - \frac{D}{\sigma^2}xg \\
&= \left(1 - \frac{D}{\sigma^2}\right)xg
\end{aligned}
$$

さらに $x$ で微分します。

$$
\begin{aligned}
\frac{\partial}{\partial x}\left\{\left(1 - \frac{D}{\sigma^2}\right)xg\right\} &= \left(1 - \frac{D}{\sigma^2}\right)\left(g + x\frac{\partial g}{\partial x}\right) \\
&= \left(1 - \frac{D}{\sigma^2}\right)\left(1 - \frac{x^2}{\sigma^2}\right)g
\end{aligned}
$$

定常解の条件よりこれがすべての $x$ に対して $0$ にならなければならないため，$1 - \dfrac{D}{\sigma^2} = 0$ が必要です。$\sigma > 0$ より $\sigma = \sqrt{D}$ となります。

$$
\finalanswer{\sigma = \sqrt{D}}
$$

### (3)

$u = x - X(t)$ とおくと，$f(x, t) = \dfrac{1}{\sqrt{2\pi}\sigma(t)}\exp\!\left(-\dfrac{u^2}{2\sigma(t)^2}\right)$ です。$\dot{X} = \dfrac{\mathrm{d}X}{\mathrm{d}t}$，$\dot{\sigma} = \dfrac{\mathrm{d}\sigma}{\mathrm{d}t}$ として，左辺の $\dfrac{\partial f}{\partial t}$ を計算します。

$$
\begin{aligned}
\frac{\partial f}{\partial t} &= \left(-\frac{\dot{\sigma}}{\sigma} + \frac{u\dot{X}}{\sigma^2} + \frac{u^2\dot{\sigma}}{\sigma^3}\right)f
\end{aligned}
$$

次に右辺の各項を計算します。$\dfrac{\partial f}{\partial x} = -\dfrac{u}{\sigma^2}f$，および $x = u + X$ を用います。

$$
\begin{aligned}
\frac{\partial}{\partial x}(xf) &= f + x\frac{\partial f}{\partial x} \\
&= \left(1 - \frac{(u + X)u}{\sigma^2}\right)f \\
&= \left(1 - \frac{X}{\sigma^2}u - \frac{1}{\sigma^2}u^2\right)f
\end{aligned}
$$

$$
\begin{aligned}
D\frac{\partial^2 f}{\partial x^2} &= D\frac{\partial}{\partial x}\left(-\frac{u}{\sigma^2}f\right) \\
&= D\left(-\frac{1}{\sigma^2} + \frac{u^2}{\sigma^4}\right)f
\end{aligned}
$$

右辺の2項を足し合わせます。

$$
\frac{\partial}{\partial x}(xf) + D\frac{\partial^2 f}{\partial x^2} = \left\{\left(1 - \frac{D}{\sigma^2}\right) - \frac{X}{\sigma^2}u + \left(-\frac{1}{\sigma^2} + \frac{D}{\sigma^4}\right)u^2\right\}f
$$

$f(x, t) > 0$ なので，偏微分方程式がすべての $u$ について成り立つためには，左辺と右辺の $u^0, u^1, u^2$ の係数がそれぞれ一致しなければなりません。

- $u^1$ の係数より $\dfrac{\dot{X}}{\sigma^2} = -\dfrac{X}{\sigma^2}$，すなわち $\dfrac{\mathrm{d}X}{\mathrm{d}t} = -X$ です。
- $u^0$ の係数より $-\dfrac{\dot{\sigma}}{\sigma} = 1 - \dfrac{D}{\sigma^2}$，すなわち $\dfrac{\mathrm{d}\sigma}{\mathrm{d}t} = \dfrac{D}{\sigma} - \sigma$ です。
- $u^2$ の係数より $\dfrac{\dot{\sigma}}{\sigma^3} = -\dfrac{1}{\sigma^2} + \dfrac{D}{\sigma^4}$ となり，両辺に $\sigma^3$ を掛けると $\dfrac{\mathrm{d}\sigma}{\mathrm{d}t} = \dfrac{D}{\sigma} - \sigma$ となって $u^0$ の条件と一致します。

したがって，$X(t)$ と $\sigma(t)$ の満たすべき常微分方程式は次式となります。

$$
\finalanswer{\frac{\mathrm{d}X}{\mathrm{d}t} = -X, \qquad \frac{\mathrm{d}\sigma}{\mathrm{d}t} = \frac{D}{\sigma} - \sigma}
$$

### (4)

初期条件 $f(x, 0) = \delta(x - 1)$ は $g(x - 1, \sigma)$ の $\sigma \to 0$ の極限なので，$t = 0$ における $X(t)$ と $\sigma(t)$ の初期値は $X(0) = 1$，$\sigma(0) = 0$ です。

まず $\dfrac{\mathrm{d}X}{\mathrm{d}t} = -X$ を $X(0) = 1$ のもとで解くと，$X(t) = e^{-t}$ が得られます。

次に $v(t) = \sigma(t)^2$ とおきます。設問 (3) の第2式の両辺に $2\sigma$ を掛けます。

$$
2\sigma\frac{\mathrm{d}\sigma}{\mathrm{d}t} = 2D - 2\sigma^2
$$

$\dfrac{\mathrm{d}v}{\mathrm{d}t} = 2\sigma\dfrac{\mathrm{d}\sigma}{\mathrm{d}t}$ を用いて整理すると，$v(t)$ に関する1階線形常微分方程式が得られます。

$$
\frac{\mathrm{d}v}{\mathrm{d}t} + 2v = 2D
$$

両辺に $e^{2t}$ を掛けます。

$$
\frac{\mathrm{d}}{\mathrm{d}t}\bigl(e^{2t}v(t)\bigr) = 2D e^{2t}
$$

両辺を $0$ から $t$ まで積分します。

$$
e^{2t}v(t) - v(0) = D\bigl(e^{2t} - 1\bigr)
$$

初期条件 $v(0) = \sigma(0)^2 = 0$ を代入し，両辺に $e^{-2t}$ を掛けます。

$$
v(t) = D\bigl(1 - e^{-2t}\bigr)
$$

$\sigma(t) > 0$（$t > 0$）なので，$\sigma(t) = \sqrt{D(1 - e^{-2t})}$ です。これらを $f(x, t) = g\bigl(x - X(t), \sigma(t)\bigr)$ に代入すると，求める解は次式となります。

$$
\finalanswer{f(x, t) = \frac{1}{\sqrt{2\pi D(1 - e^{-2t})}}\exp\!\left(-\frac{(x - e^{-t})^2}{2D(1 - e^{-2t})}\right)}
$$

$t \to \infty$ の極限では $X(t) = e^{-t} \to 0$ かつ $\sigma(t) = \sqrt{D(1 - e^{-2t})} \to \sqrt{D}$ となります。したがって，解 $f(x, t)$ は $t \to \infty$ において次のようになります。

$$
\begin{aligned}
\lim_{t \to \infty} f(x, t) &= \frac{1}{\sqrt{2\pi D}}e^{-x^2/(2D)} \\
&= g\bigl(x, \sqrt{D}\bigr)
\end{aligned}
$$

このように，$f(x, t)$ は設問 (2) で求めた定常解に近づきます。
