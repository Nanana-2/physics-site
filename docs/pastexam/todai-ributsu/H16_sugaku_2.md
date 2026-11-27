---
title: 東大理物 平成16年度 数学 第2問：1次元熱伝導方程式のフーリエ変換解法と誤差関数
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 積分変換
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成16年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成16年度 数学 第2問：1次元熱伝導方程式のフーリエ変換解法と誤差関数

## 問題

(1) $u_k(x, t) = e^{ikx + i\omega t}$ とおく。$u = u_k(x, t)$ が，次の偏微分方程式

$$
\frac{\partial u}{\partial t} = a^2\frac{\partial^2 u}{\partial x^2}
$$

を満たすように $\omega$ を定めよ。ただし，$a$ を正の定数，$x$ および $t$ は実数とする。

(2) (1) で得られた $u_k(x, t)$ を用いて，上の偏微分方程式の解を

$$
u(x, t) = \int_{-\infty}^{\infty} A_k u_k(x, t)\,\mathrm{d}k
$$

とおく。与えられた関数 $f(x)$ に対し，初期条件 $u(x, 0) = f(x)$ をみたすように $A_k$ を $f(x)$ を用いて表わせ。ただし，$k$ についての積分は実行しなくてよい。

(3) $\displaystyle\int_{-\infty}^{\infty} e^{iky} e^{-a^2 k^2 t}\,\mathrm{d}k$ を求めよ。ただし，$y$ は定数で，$t > 0$ とする。

(4) (3) の結果を用いて (2) の $k$ についての積分を実行し，初期値問題の解 $u(x, t)$ を求めよ。

(5) $f(x)$ が次のように与えられているとする。

$$
f(x) = \begin{cases} U & \text{if } |x| \le L \\ 0 & \text{if } |x| > L \end{cases}
$$

ただし，$U$ と $L(>0)$ は定数とする。このとき，$u(x, t)$ を $\operatorname{erf}(z)$ を用いて表わせ。ここで，すべての実数 $z$ について

$$
\operatorname{erf}(z) = \frac{2}{\sqrt{\pi}}\int_{0}^{z} e^{-y^2}\,\mathrm{d}y
$$

と定義する。

> 出典：東京大学大学院理学系研究科物理学専攻 平成16年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
1次元熱伝導方程式は定数係数の線形偏微分方程式なので，空間方向にフーリエ変換を行うと各波数 $k$ の成分が互いに独立な1階常微分方程式に分かれます。それぞれの波数成分は $e^{-a^2 k^2 t}$ で時間減衰します。

この減衰因子をフーリエ逆変換で実空間へ戻すとガウス型の熱核が得られ，任意の初期分布 $f(x)$ に対する解を畳み込み積分として表すことができます。初期分布が区間 $[-L, L]$ で定数のときは，ガウス積分を誤差関数 $\operatorname{erf}(z)$ の差として書くことができます。
</div>

### (1)

$u_k(x, t) = e^{ikx + i\omega t}$ の各偏微分を計算します。

$$
\frac{\partial u_k}{\partial t} = i\omega e^{ikx + i\omega t}, \qquad \frac{\partial^2 u_k}{\partial x^2} = -k^2 e^{ikx + i\omega t}
$$

これらを偏微分方程式 $\dfrac{\partial u}{\partial t} = a^2\dfrac{\partial^2 u}{\partial x^2}$ に代入し，$e^{ikx + i\omega t} \neq 0$ で割ります。

$$
i\omega = -a^2 k^2
$$

両辺を $i$ で割ると，$\omega = i a^2 k^2$ となります。

$$
\finalanswer{\omega = i a^2 k^2}
$$

### (2)

設問 (1) より $u_k(x, t) = e^{ikx - a^2 k^2 t}$ なので，$t = 0$ を代入すると初期条件は次式になります。

$$
\int_{-\infty}^{\infty} A_k e^{ikx}\,\mathrm{d}k = f(x)
$$

フーリエ変換の反転公式を用いると，$A_k$ は $f(x)$ を用いて次のように表されます。

$$
\finalanswer{A_k = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(\xi)e^{-ik\xi}\,\mathrm{d}\xi}
$$

### (3)

被積分関数の指数部分を $k$ について平方完成します。

$$
\begin{aligned}
iky - a^2 k^2 t &= -a^2 t\left(k^2 - \frac{iy}{a^2 t}k\right) \\
&= -a^2 t\left(k - \frac{iy}{2a^2 t}\right)^2 - \frac{y^2}{4a^2 t}
\end{aligned}
$$

これを積分に代入します。$t > 0$，$a > 0$ なので，ガウス積分において積分路を実軸から虚軸方向に平行移動しても値は変わりません。

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{iky} e^{-a^2 k^2 t}\,\mathrm{d}k &= \exp\!\left(-\frac{y^2}{4a^2 t}\right)\int_{-\infty}^{\infty} \exp\!\left\{-a^2 t\left(k - \frac{iy}{2a^2 t}\right)^2\right\}\mathrm{d}k \\
&= \exp\!\left(-\frac{y^2}{4a^2 t}\right)\int_{-\infty}^{\infty} e^{-a^2 t k^2}\,\mathrm{d}k \\
&= \frac{\sqrt{\pi}}{a\sqrt{t}}\exp\!\left(-\frac{y^2}{4a^2 t}\right)
\end{aligned}
$$

したがって，求める積分は次式となります。

$$
\finalanswer{\int_{-\infty}^{\infty} e^{iky} e^{-a^2 k^2 t}\,\mathrm{d}k = \frac{\sqrt{\pi}}{a\sqrt{t}}\exp\!\left(-\frac{y^2}{4a^2 t}\right)}
$$

### (4)

設問 (2) で得た $A_k$ を $u(x, t) = \int_{-\infty}^{\infty} A_k e^{ikx - a^2 k^2 t}\,\mathrm{d}k$ に代入し，$k$ と $\xi$ の積分順序を入れ替えます。

$$
\begin{aligned}
u(x, t) &= \int_{-\infty}^{\infty} \left(\frac{1}{2\pi}\int_{-\infty}^{\infty} f(\xi)e^{-ik\xi}\,\mathrm{d}\xi\right) e^{ikx - a^2 k^2 t}\,\mathrm{d}k \\
&= \frac{1}{2\pi}\int_{-\infty}^{\infty} f(\xi)\left(\int_{-\infty}^{\infty} e^{ik(x - \xi)} e^{-a^2 k^2 t}\,\mathrm{d}k\right)\mathrm{d}\xi
\end{aligned}
$$

括弧内の $k$ に関する積分に設問 (3) の結果で $y = x - \xi$ としたものを代入します。

$$
\begin{aligned}
u(x, t) &= \frac{1}{2\pi}\int_{-\infty}^{\infty} f(\xi)\cdot\frac{\sqrt{\pi}}{a\sqrt{t}}\exp\!\left(-\frac{(x - \xi)^2}{4a^2 t}\right)\mathrm{d}\xi \\
&= \frac{1}{2a\sqrt{\pi t}}\int_{-\infty}^{\infty} f(\xi)\exp\!\left(-\frac{(x - \xi)^2}{4a^2 t}\right)\mathrm{d}\xi
\end{aligned}
$$

したがって，初期値問題の解は次式となります。

$$
\finalanswer{u(x, t) = \frac{1}{2a\sqrt{\pi t}}\int_{-\infty}^{\infty} f(\xi)\exp\!\left(-\frac{(x - \xi)^2}{4a^2 t}\right)\mathrm{d}\xi}
$$

### (5)

与えられた $f(\xi)$ を設問 (4) の解に代入すると，積分範囲は $[-L, L]$ になります。

$$
u(x, t) = \frac{U}{2a\sqrt{\pi t}}\int_{-L}^{L} \exp\!\left(-\frac{(\xi - x)^2}{4a^2 t}\right)\mathrm{d}\xi
$$

$y = \dfrac{\xi - x}{2a\sqrt{t}}$ と置換します。$\mathrm{d}\xi = 2a\sqrt{t}\,\mathrm{d}y$ であり，$\xi = -L$ で $y = \dfrac{-L - x}{2a\sqrt{t}} = -\dfrac{x + L}{2a\sqrt{t}}$，$\xi = L$ で $y = \dfrac{L - x}{2a\sqrt{t}}$ となります。

$$
\begin{aligned}
u(x, t) &= \frac{U}{\sqrt{\pi}}\int_{-(x + L)/(2a\sqrt{t})}^{(L - x)/(2a\sqrt{t})} e^{-y^2}\,\mathrm{d}y \\
&= \frac{U}{2}\left\{\frac{2}{\sqrt{\pi}}\int_{0}^{(L - x)/(2a\sqrt{t})} e^{-y^2}\,\mathrm{d}y - \frac{2}{\sqrt{\pi}}\int_{0}^{-(x + L)/(2a\sqrt{t})} e^{-y^2}\,\mathrm{d}y\right\} \\
&= \frac{U}{2}\left\{\operatorname{erf}\!\left(\frac{L - x}{2a\sqrt{t}}\right) - \operatorname{erf}\!\left(-\frac{x + L}{2a\sqrt{t}}\right)\right\}
\end{aligned}
$$

被積分関数 $e^{-y^2}$ は偶関数なので $\operatorname{erf}(-z) = -\operatorname{erf}(z)$ が成り立ちます。これを用いて整理します。

$$
\begin{aligned}
u(x, t) &= \frac{U}{2}\left\{\operatorname{erf}\!\left(\frac{L - x}{2a\sqrt{t}}\right) + \operatorname{erf}\!\left(\frac{x + L}{2a\sqrt{t}}\right)\right\} \\
&= \frac{U}{2}\left\{\operatorname{erf}\!\left(\frac{x + L}{2a\sqrt{t}}\right) - \operatorname{erf}\!\left(\frac{x - L}{2a\sqrt{t}}\right)\right\}
\end{aligned}
$$

したがって，$u(x, t)$ は次式となります。

$$
\finalanswer{u(x, t) = \frac{U}{2}\left\{\operatorname{erf}\!\left(\frac{x + L}{2a\sqrt{t}}\right) - \operatorname{erf}\!\left(\frac{x - L}{2a\sqrt{t}}\right)\right\}}
$$
