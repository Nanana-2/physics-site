---
title: 東大理物 平成28年度 数学 第2問：クライン・ゴルドン方程式と非線形キンク解・ゼロモード
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成28年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成28年度 数学 第2問：クライン・ゴルドン方程式と非線形キンク解・ゼロモード

## 問題

(1) $y(x, t)$ に対する偏微分方程式

$$
\frac{\partial^2 y}{\partial t^2} - \frac{\partial^2 y}{\partial x^2} + \lambda^2 y = 0 \tag{1}
$$

を考える。（$\lambda$ は正の定数とする。）

(i) 初期条件，$y(x, 0) = \cos kx,\ \left.\dfrac{\partial y(x, t)}{\partial t}\right|_{t=0} = 0$ の下で，$y(x, t)$ を求めよ。（$k$ は正の定数とする。）ただし，この条件のとき，解が $y(x, t) = f(t) g(x)$ と書けることを用いてもよい。

(ii) 設問 (i) で得られた解を，$x$ 軸の正の方向に進む波と負の方向に進む波との2つに分解せよ。

(2) 次に

$$
\frac{\partial^2 y}{\partial t^2} - \frac{\partial^2 y}{\partial x^2} + 2\lambda^2\left(y^3 - y\right) = 0 \tag{2}
$$

を考える。（$\lambda$ は正の定数とする。）

(i) まず，$t$ に依存しない解 $y(x, t) = u(x)$ を考える。$u(x)$ に対する微分方程式

$$
-\frac{d^2 u}{dx^2} + 2\lambda^2\left(u^3 - u\right) = 0 \tag{3}
$$

の両辺に $\dfrac{du}{dx}$ をかけて，その積分を求めることにより

$$
\frac{du}{dx} = \pm\lambda\sqrt{u^4 - 2u^2 + A} \tag{4}
$$

が成立することを示せ。ここで，$A$ は積分定数である。

(ii) 設問 (i) の $u(x)$ が満たす境界条件を

$$
\lim_{x\to\infty} u(x) = 1,\qquad \lim_{x\to -\infty} u(x) = -1 \tag{5}
$$

とする。このとき $A$ の値を求めよ。

(iii) 設問 (ii) の境界条件の下で $u(x)$ を求めよ。ただし $|u(x)| \le 1,\ u(0) = 0$ としてよい。

(iv) 次に，(3) を満たす $u(x)$ を用いて $y(x, t) = u(x) + z(x, t)$ とおき，$z$ が満たす偏微分方程式を求めよ。ただし $z$ は微小であるとして，$z^2,\ z^3$ に比例する項は無視してよい。

(v) (3) を使って，設問 (iv) で求めた $z$ の偏微分方程式の1つの解が

$$
z_0(x, t) = e^{i\omega t}\frac{du}{dx} \tag{6}
$$

で与えられることを示せ。また，そのときの $\omega$ の値を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成28年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
設問1の線形クライン・ゴルドン方程式は変数分離によって分散関係 $\omega = \sqrt{k^2 + \lambda^2}$ をもつ平面波へ分解されます。

設問2の非線形方程式の静的解は，$x$ を時間とみなした力学系のエネルギー保存則（第1積分）を使うと2つの真空 $u = \pm 1$ を滑らかにつなぐキンク解 $u(x) = \tanh(\lambda x)$ として厳密に求まります。もとの方程式の空間並進対称性から，キンク解の微小シフト $u(x + \delta x) - u(x) \simeq \delta x\,\dfrac{\mathrm{d}u}{\mathrm{d}x}$ は振動数 $\omega = 0$ の線形化方程式の解（並進ゼロモード）を与えます。
</div>

### (1)
(i) $y(x, t) = f(t)g(x)$ を式 (1) に代入します。初期条件 $y(x, 0) = f(0)g(x) = \cos kx$ より $g(x) = \cos kx,\ f(0) = 1$ と選ぶことができます。すると $g''(x) = -k^2 g(x)$ なので，式 (1) は

$$
\bigl[f''(t) + (k^2 + \lambda^2) f(t)\bigr]\cos kx = 0
$$

となります。$\omega_k = \sqrt{k^2 + \lambda^2}$ とおくと $f''(t) + \omega_k^2 f(t) = 0$ の一般解は $f(t) = C_1\cos(\omega_k t) + C_2\sin(\omega_k t)$ です。初期条件 $f(0) = 1,\ f'(0) = 0$ より $C_1 = 1,\ C_2 = 0$ となります。したがって，

$$
\finalanswer{y(x, t) = \cos\left(\sqrt{k^2 + \lambda^2}\,t\right)\cos kx}
$$

(ii) 三角関数の積和公式 $\cos\alpha\cos\beta = \dfrac{1}{2}\bigl[\cos(\alpha - \beta) + \cos(\alpha + \beta)\bigr]$ を用います。

$$
y(x, t) = \frac{1}{2}\cos\left(kx - \sqrt{k^2 + \lambda^2}\,t\right) + \frac{1}{2}\cos\left(kx + \sqrt{k^2 + \lambda^2}\,t\right)
$$

右辺第1項が $x$ 軸の正の方向に進む波，第2項が $x$ 軸の負の方向に進む波です。したがって，

$$
\finalanswer{y_+(x, t) = \frac{1}{2}\cos\left(kx - \sqrt{k^2 + \lambda^2}\,t\right),\qquad y_-(x, t) = \frac{1}{2}\cos\left(kx + \sqrt{k^2 + \lambda^2}\,t\right)}
$$

### (2)
(i) 式 (3) の両辺に $\dfrac{\mathrm{d}u}{\mathrm{d}x}$ を掛けます。

$$
-\frac{\mathrm{d}u}{\mathrm{d}x}\frac{\mathrm{d}^2 u}{\mathrm{d}x^2} + 2\lambda^2\left(u^3 - u\right)\frac{\mathrm{d}u}{\mathrm{d}x} = 0
$$

左辺を全微分の形にまとめます。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left[-\frac{1}{2}\left(\frac{\mathrm{d}u}{\mathrm{d}x}\right)^2 + \frac{\lambda^2}{2}\left(u^4 - 2u^2\right)\right] = 0
$$

$x$ について積分し，積分定数を $-\dfrac{\lambda^2}{2}A$ とおくと，

$$
\left(\frac{\mathrm{d}u}{\mathrm{d}x}\right)^2 = \lambda^2\left(u^4 - 2u^2 + A\right)
$$

両辺の平方根をとると（$\lambda > 0$），式 (4) が得られます。

$$
\frac{\mathrm{d}u}{\mathrm{d}x} = \pm\lambda\sqrt{u^4 - 2u^2 + A}
$$

(ii) 境界条件 (5) より $x \to \pm\infty$ で $u(x) \to \pm 1$ であり，一定値に収束するため $\dfrac{\mathrm{d}u}{\mathrm{d}x} \to 0$ です。これを式 (4) に代入すると，

$$
0 = \lambda^2(1 - 2 + A) \implies A = 1
$$

となります。したがって，

$$
\finalanswer{A = 1}
$$

(iii) $A = 1$ を式 (4) に代入すると $u^4 - 2u^2 + 1 = (1 - u^2)^2$ です。$|u(x)| \le 1$ より $1 - u^2 \ge 0$ であり，境界条件 $u(-\infty) = -1,\ u(+\infty) = +1$ を満たす単調増加解を与えるため正符号をとります。

$$
\frac{\mathrm{d}u}{\mathrm{d}x} = \lambda\left(1 - u^2\right)
$$

変数分離して部分分数分解により積分します。

$$
\begin{aligned}
\frac{\mathrm{d}u}{1 - u^2} &= \lambda\,\mathrm{d}x \\
\frac{1}{2}\left(\frac{1}{1 - u} + \frac{1}{1 + u}\right)\mathrm{d}u &= \lambda\,\mathrm{d}x \\
\frac{1}{2}\ln\frac{1 + u}{1 - u} &= \lambda x + C
\end{aligned}
$$

条件 $u(0) = 0$ より $C = 0$ です。よって

$$
\frac{1 + u}{1 - u} = e^{2\lambda x} \implies u(x) = \frac{e^{2\lambda x} - 1}{e^{2\lambda x} + 1} = \tanh(\lambda x)
$$

となります（$x \to \pm\infty$ で $\pm 1$ に収束することも満たします）。したがって，

$$
\finalanswer{u(x) = \tanh(\lambda x)}
$$

(iv) $y(x, t) = u(x) + z(x, t)$ を式 (2) に代入し，$z$ の1次まで展開します。

$$
\begin{aligned}
\frac{\partial^2 z}{\partial t^2} - \frac{\mathrm{d}^2 u}{\mathrm{d}x^2} - \frac{\partial^2 z}{\partial x^2} + 2\lambda^2\left(u^3 + 3u^2 z - u - z\right) &\simeq 0 \\
\left(-\frac{\mathrm{d}^2 u}{\mathrm{d}x^2} + 2\lambda^2(u^3 - u)\right) + \frac{\partial^2 z}{\partial t^2} - \frac{\partial^2 z}{\partial x^2} + 2\lambda^2\left(3u^2 - 1\right)z &= 0
\end{aligned}
$$

第1項は式 (3) より $0$ です。したがって，$z(x, t)$ が満たす偏微分方程式は

$$
\finalanswer{\frac{\partial^2 z}{\partial t^2} - \frac{\partial^2 z}{\partial x^2} + 2\lambda^2\left(3u^2 - 1\right)z = 0}
$$

です（$u(x) = \tanh(\lambda x)$ を代入すれば $\dfrac{\partial^2 z}{\partial t^2} - \dfrac{\partial^2 z}{\partial x^2} + 2\lambda^2\left(2 - 3\operatorname{sech}^2(\lambda x)\right)z = 0$ とも表すことができます）。

(v) 式 (3) の両辺を $x$ で微分します。

$$
-\frac{\mathrm{d}^2}{\mathrm{d}x^2}\left(\frac{\mathrm{d}u}{\mathrm{d}x}\right) + 2\lambda^2\left(3u^2 - 1\right)\frac{\mathrm{d}u}{\mathrm{d}x} = 0
$$

式 (6) の $z_0(x, t) = e^{i\omega t}\dfrac{\mathrm{d}u}{\mathrm{d}x}$ を (iv) の偏微分方程式の左辺に代入します。

$$
\begin{aligned}
\frac{\partial^2 z_0}{\partial t^2} - \frac{\partial^2 z_0}{\partial x^2} + 2\lambda^2\left(3u^2 - 1\right)z_0
&= e^{i\omega t}\left[-\omega^2\frac{\mathrm{d}u}{\mathrm{d}x} - \frac{\mathrm{d}^2}{\mathrm{d}x^2}\left(\frac{\mathrm{d}u}{\mathrm{d}x}\right) + 2\lambda^2\left(3u^2 - 1\right)\frac{\mathrm{d}u}{\mathrm{d}x}\right] \\
&= -\omega^2 e^{i\omega t}\frac{\mathrm{d}u}{\mathrm{d}x}
\end{aligned}
$$

$\dfrac{\mathrm{d}u}{\mathrm{d}x} = \lambda\operatorname{sech}^2(\lambda x) \not\equiv 0$ なので，これが $0$ となるための必要十分条件は $\omega = 0$ です。よって $\omega = 0$ のとき $z_0(x, t)$ は (iv) の偏微分方程式の解となります。したがって，

$$
\finalanswer{\omega = 0}
$$

<aside class="rigor-note" markdown>
式 (2) は1+1次元 $\phi^4$ 理論の運動方程式であり，問2(iii) の $u(x) = \tanh(\lambda x)$ はトポロジカルソリトン（キンク解）と呼ばれます。問2(v) で現れた $\omega = 0$ のモード $z_0 \propto \operatorname{sech}^2(\lambda x)$ は，キンクの中心位置を任意に平行移動しても解であることに由来する南部・ゴールドストーンの並進ゼロモードです。
</aside>
