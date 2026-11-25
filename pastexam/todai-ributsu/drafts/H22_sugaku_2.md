---
title: 東大理物 平成22年度 数学 第2問：1次元波動方程式のダランベールの公式とエネルギー保存
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成22年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成22年度 数学 第2問：1次元波動方程式のダランベールの公式とエネルギー保存

## 問題

以下の偏微分方程式を考える。

$$
\frac{1}{v^2}\frac{\partial^2 u}{\partial t^2} - \frac{\partial^2 u}{\partial x^2} = 0. \tag{1}
$$

ここで $v$ は正の定数であり，$u(x, t)$ は $-\infty < t < +\infty$ および $-\infty < x < +\infty$ で定義された二変数関数である。以下の設問に答えよ。

(1) 変数 $\xi = x + vt$ および $\eta = x - vt$ を用いて (1) 式を書き直せ。

(2) (1) 式の一般解が，適当な関数 $f$ と $g$ を用いて $u(x, t) = f(x + vt) + g(x - vt)$ と表せることを示せ。

(3) 任意の時間 $t$ に対して，(1) 式の解が $\left.\dfrac{\partial u(x, t)}{\partial x}\right|_{x \to \pm\infty} = 0$ を満たしているとする。このとき，以下の積分 $I$ が $t$ に依存しないことを示せ。ただし，$I$ は発散しないとする。

$$
I = \frac{1}{2}\int_{-\infty}^{+\infty}\left(\frac{1}{v^2}\left(\frac{\partial u}{\partial t}\right)^2 + \left(\frac{\partial u}{\partial x}\right)^2\right)\mathrm{d}x.
$$

(4) $u(x, t)$ の初期条件として，$u(x, 0) = u_0(x)$，$\left.\dfrac{\partial u(x, t)}{\partial t}\right|_{t=0} = u_1(x)$ が与えられているとする。このとき，設問 (2) の結果を利用して，解 $u(x, t)$ を $u_0$ と $u_1$ を用いて表せ。

(5) $u_0(x) = 0$ および $u_1(x) = \dfrac{v^2}{\pi}\dfrac{b}{(x - a)^2 + b^2}$ なる初期条件のもとで，$t > 0$ での解 $u(x, t)$ を求めよ。ここで，$a$ と $b$ は正の定数とする。

(6) $b \to 0$ なる極限の場合に，設問 (5) で求めた解 $u(x, t)$ を図示せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成22年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
特性変数 $\xi = x + vt$，$\eta = x - vt$ へ変換すると 1 次元波動方程式は混合偏微分 $\partial_\xi \partial_\eta u = 0$ になり，2 回の逐次積分で左右へ進む波の和 $f(x + vt) + g(x - vt)$ が一般解として得られます。

初期変位と初期速度から $f$ と $g$ を決めるとダランベールの公式が得られ，ローレンツ型の初期速度に対しては $\arctan$ で陽に積分できます。$b \to 0$ では $\arctan$ が階段関数に近づくため，両端が速度 $v$ で広がる矩形波になります。
</div>

### (1)
$\xi = x + vt$，$\eta = x - vt$ より，合成関数の微分法を用いて $\dfrac{\partial}{\partial t}$ と $\dfrac{\partial}{\partial x}$ を書き換えます。

$$
\begin{aligned}
\frac{\partial}{\partial x} &= \frac{\partial\xi}{\partial x}\frac{\partial}{\partial\xi} + \frac{\partial\eta}{\partial x}\frac{\partial}{\partial\eta} = \frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta} \\
\frac{\partial}{\partial t} &= \frac{\partial\xi}{\partial t}\frac{\partial}{\partial\xi} + \frac{\partial\eta}{\partial t}\frac{\partial}{\partial\eta} = v\left(\frac{\partial}{\partial\xi} - \frac{\partial}{\partial\eta}\right)
\end{aligned}
$$

これらを式 (1) に代入します。

$$
\begin{aligned}
\frac{1}{v^2}\frac{\partial^2 u}{\partial t^2} - \frac{\partial^2 u}{\partial x^2} &= \left(\frac{\partial}{\partial\xi} - \frac{\partial}{\partial\eta}\right)^2 u - \left(\frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta}\right)^2 u \\
&= -4\frac{\partial^2 u}{\partial\xi\partial\eta} = 0
\end{aligned}
$$

したがって次式が得られます。

$$
\finalanswer{\frac{\partial^2 u}{\partial\xi\partial\eta} = 0}
$$

### (2)
設問 (1) の方程式 $\dfrac{\partial}{\partial\eta}\left(\dfrac{\partial u}{\partial\xi}\right) = 0$ を $\eta$ について積分すると，$\dfrac{\partial u}{\partial\xi}$ は $\eta$ に依存しない関数 $F(\xi)$ になります。

$$
\frac{\partial u}{\partial\xi} = F(\xi)
$$

これをさらに $\xi$ について積分します。$F(\xi)$ の原始関数を $f(\xi)$ とし，積分定数に相当する $\eta$ のみの任意関数を $g(\eta)$ とおきます。

$$
\begin{aligned}
u &= f(\xi) + g(\eta) \\
u(x, t) &= f(x + vt) + g(x - vt)
\end{aligned}
$$

以上より，式 (1) の一般解は $u(x, t) = f(x + vt) + g(x - vt)$ と表されます。

### (3)
積分 $I$ を時刻 $t$ で微分し，式 (1) の関係 $\dfrac{1}{v^2}\dfrac{\partial^2 u}{\partial t^2} = \dfrac{\partial^2 u}{\partial x^2}$ を用いて整理します。

$$
\begin{aligned}
\frac{\mathrm{d}I}{\mathrm{d}t} &= \int_{-\infty}^{+\infty}\left(\frac{1}{v^2}\frac{\partial u}{\partial t}\frac{\partial^2 u}{\partial t^2} + \frac{\partial u}{\partial x}\frac{\partial^2 u}{\partial t\partial x}\right)\mathrm{d}x \\
&= \int_{-\infty}^{+\infty}\left(\frac{\partial u}{\partial t}\frac{\partial^2 u}{\partial x^2} + \frac{\partial u}{\partial x}\frac{\partial^2 u}{\partial x\partial t}\right)\mathrm{d}x \\
&= \int_{-\infty}^{+\infty}\frac{\partial}{\partial x}\left(\frac{\partial u}{\partial t}\frac{\partial u}{\partial x}\right)\mathrm{d}x \\
&= \left[\frac{\partial u}{\partial t}\frac{\partial u}{\partial x}\right]_{x \to -\infty}^{x \to +\infty}
\end{aligned}
$$

仮定より $x \to \pm\infty$ で $\dfrac{\partial u}{\partial x} \to 0$ であり，また $I$ が発散しないことから $\dfrac{\partial u}{\partial t}$ も有界なので，右辺は $0$ です。したがって $\dfrac{\mathrm{d}I}{\mathrm{d}t} = 0$ となり，$I$ は $t$ に依存しません。

### (4)
設問 (2) の一般解 $u(x, t) = f(x + vt) + g(x - vt)$ に $t = 0$ の初期条件を代入します。

$$
\begin{aligned}
f(x) + g(x) &= u_0(x) \\
v\bigl(f'(x) - g'(x)\bigr) &= u_1(x)
\end{aligned}
$$

第 2 式を $0$ から $x$ まで積分します。積分定数を $C$ とおきます。

$$
f(x) - g(x) = \frac{1}{v}\int_0^x u_1(s)\,\mathrm{d}s + C
$$

これと第 1 式の和と差から $f(x)$ と $g(x)$ を求めます。

$$
\begin{aligned}
f(x) &= \frac{1}{2}u_0(x) + \frac{1}{2v}\int_0^x u_1(s)\,\mathrm{d}s + \frac{C}{2} \\
g(x) &= \frac{1}{2}u_0(x) - \frac{1}{2v}\int_0^x u_1(s)\,\mathrm{d}s - \frac{C}{2}
\end{aligned}
$$

これらを $u(x, t) = f(x + vt) + g(x - vt)$ に代入すると，定数 $C/2$ が打ち消し合って次式が得られます。

$$
\begin{aligned}
u(x, t) &= \frac{1}{2}\bigl(u_0(x + vt) + u_0(x - vt)\bigr) + \frac{1}{2v}\left(\int_0^{x+vt} u_1(s)\,\mathrm{d}s - \int_0^{x-vt} u_1(s)\,\mathrm{d}s\right) \\
&= \frac{1}{2}\bigl(u_0(x + vt) + u_0(x - vt)\bigr) + \frac{1}{2v}\int_{x - vt}^{x + vt} u_1(s)\,\mathrm{d}s
\end{aligned}
$$

$$
\finalanswer{u(x, t) = \frac{1}{2}\bigl(u_0(x + vt) + u_0(x - vt)\bigr) + \frac{1}{2v}\int_{x - vt}^{x + vt} u_1(s)\,\mathrm{d}s}
$$

### (5)
設問 (4) の公式に $u_0(x) = 0$，$u_1(x) = \dfrac{v^2}{\pi}\dfrac{b}{(x - a)^2 + b^2}$ を代入し，$w = \dfrac{s - a}{b}$ と置換して積分します。

$$
\begin{aligned}
u(x, t) &= \frac{1}{2v}\int_{x - vt}^{x + vt} \frac{v^2}{\pi}\frac{b}{(s - a)^2 + b^2}\,\mathrm{d}s \\
&= \frac{v}{2\pi}\int_{(x - vt - a)/b}^{(x + vt - a)/b} \frac{\mathrm{d}w}{w^2 + 1} \\
&= \frac{v}{2\pi}\left[\arctan\!\left(\frac{x + vt - a}{b}\right) - \arctan\!\left(\frac{x - vt - a}{b}\right)\right]
\end{aligned}
$$

$$
\finalanswer{u(x, t) = \frac{v}{2\pi}\left[\arctan\!\left(\frac{x + vt - a}{b}\right) - \arctan\!\left(\frac{x - vt - a}{b}\right)\right]}
$$

### (6)
$t > 0$ を固定して $b \to 0+$ の極限をとります。実数 $X \neq 0$ に対して $X > 0$ なら $\lim_{b \to 0+}\arctan(X / b) = \dfrac{\pi}{2}$，$X < 0$ なら $\lim_{b \to 0+}\arctan(X / b) = -\dfrac{\pi}{2}$ なので，$x$ の範囲によって次のように場合分けされます。

- $x < a - vt$ のとき：$x + vt - a < 0$ かつ $x - vt - a < 0$ なので，$u(x, t) \to \dfrac{v}{2\pi}\left(-\dfrac{\pi}{2} + \dfrac{\pi}{2}\right) = 0$ です。
- $a - vt < x < a + vt$ のとき：$x + vt - a > 0$ かつ $x - vt - a < 0$ なので，$u(x, t) \to \dfrac{v}{2\pi}\left(\dfrac{\pi}{2} + \dfrac{\pi}{2}\right) = \dfrac{v}{2}$ です。
- $x > a + vt$ のとき：$x + vt - a > 0$ かつ $x - vt - a > 0$ なので，$u(x, t) \to \dfrac{v}{2\pi}\left(\dfrac{\pi}{2} - \dfrac{\pi}{2}\right) = 0$ です。

したがって $b \to 0$ の極限では，$x = a$ を中心として区間 $a - vt < x < a + vt$ に高さ $v/2$ をもつ矩形波になります。図示すると次のとおりです。

<figure class="problem-figure" markdown>
![b->0極限における矩形波u(x,t)の概形](../../../docs/assets/figures/pastexam-todai-ributsu/H22_sugaku_2-s-light.svg#only-light)
![b->0極限における矩形波u(x,t)の概形](../../../docs/assets/figures/pastexam-todai-ributsu/H22_sugaku_2-s-dark.svg#only-dark)
<figcaption markdown="span">$b \to 0$ の極限における $t > 0$ での解 $u(x, t)$ の概形。</figcaption>
</figure>
