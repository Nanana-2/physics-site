---
title: 東大理物 平成30年度 数学 第2問：バーガース方程式とコール・ホップ変換
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成30年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成30年度 数学 第2問：バーガース方程式とコール・ホップ変換

## 問題

(1) 二変数関数 $u(t, x)$ が次の偏微分方程式

$$
\frac{\partial u}{\partial t} + \frac{\partial u}{\partial x} = 0
$$

を満たすとする。微分可能な関数 $f(x)$ を用いて

$$
u(t = 0, x) = f(x)
$$

と初期条件が与えられるとき，$t > 0$ での解 $u(t, x)$ を書け。

(2) 一変数関数 $u(x)$ が次の微分方程式

$$
u\frac{du}{dx} = \frac{d^2 u}{dx^2} \tag{1}
$$

を満たすとする。ただし，$u(x)$ は無限領域上で微分可能とする。

(i) 式 (1) を

$$
\frac{d}{dx} F = 0
$$

の形に表したときの $F$ を，$u$ と $\dfrac{du}{dx}$ を用いて書け。

(ii) 境界条件

$$
\begin{aligned}
\lim_{x\to -\infty} u(x) &= W \\
\lim_{x\to +\infty} u(x) &= -W \\
u(x = 0) &= 0
\end{aligned}
$$

を満たす解 $u(x)$ を求めよ。ここで，$W$ は正の定数である。

(3) 二変数関数 $u(t, x)$ が次の偏微分方程式

$$
\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = D\frac{\partial^2 u}{\partial x^2} \tag{2}
$$

を満たすとする。ここで，$D$ は正の定数である。この非線形方程式を線形方程式に帰着させて解く手順を考える。

(i) 次の偏微分方程式

$$
\frac{\partial s}{\partial t} = \frac{1}{2}\left(\frac{\partial s}{\partial x}\right)^2 + D\frac{\partial^2 s}{\partial x^2} \tag{3}
$$

を満たす関数 $s(t, x)$ によって

$$
u^*(t, x) = -\frac{\partial s(t, x)}{\partial x}
$$

と与えられる $u^*(t, x)$ は，式 (2) の解となることを示せ。

(ii) 関数 $\phi(t, x)$ が次の線形偏微分方程式

$$
\frac{\partial\phi}{\partial t} = D\frac{\partial^2\phi}{\partial x^2} \tag{4}
$$

を満たすとする。ある関数 $S(\phi)$ によって

$$
s^*(t, x) = S\bigl(\phi(t, x)\bigr)
$$

と与えられる $s^*(t, x)$ が式 (3) の解となるとき，$S(\phi)$ が満たす微分方程式を導け。さらに $S(\phi)$ を求めよ。

(iii) $\phi(t, x)$ は，次のように定義されるフーリエ変換によって

$$
\phi(t, x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \tilde{\phi}(t, k)\,e^{ikx}\,dk
$$

と表されるとする。ここで，$i$ は虚数単位を表す。$\tilde{\phi}(t, k)$ が満たす微分方程式を式 (4) から導け。さらに，関数 $g(k)$ を用いて

$$
\tilde{\phi}(t = 0, k) = g(k)
$$

と初期条件が与えられるとき，$t > 0$ での解 $\tilde{\phi}(t, k)$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成30年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
非線形移流項 $u\partial_x u$ と拡散項 $D\partial_x^2 u$ が釣り合うバーガース方程式は，そのままでは重ね合わせが効きませんが，ポテンシャル $s$ を導入して $u = -\partial_x s$ と書くと非線形項が $(\partial_x s)^2$ の形に整理されます。

さらに $s = 2D\ln\phi$ という対数変換（コール・ホップ変換）を施すと，$(\partial_x\phi)^2$ に比例する非線形項がちょうど打ち消し合って線形の拡散方程式へ変換され，フーリエ変換で一般解を厳密に構成することができます。
</div>

### (1)
特性変数 $\xi = x - t,\ \tau = t$ へ変数変換すると，$\dfrac{\partial}{\partial t} = \dfrac{\partial}{\partial\tau} - \dfrac{\partial}{\partial\xi}$，$\dfrac{\partial}{\partial x} = \dfrac{\partial}{\partial\xi}$ より偏微分方程式は $\dfrac{\partial u}{\partial\tau} = 0$ となります。よって $u$ は $\xi = x - t$ のみの関数であり，初期条件 $u(0, x) = f(x)$ より $u(t, x) = f(x - t)$ と決まります。したがって，

$$
\finalanswer{u(t, x) = f(x - t)}
$$

### (2)
(i) $u\dfrac{\mathrm{d}u}{\mathrm{d}x} = \dfrac{\mathrm{d}}{\mathrm{d}x}\left(\dfrac{1}{2}u^2\right)$ に注意すると，式 (1) は次のように変形されます。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{1}{2}u^2 - \frac{\mathrm{d}u}{\mathrm{d}x}\right) = 0
$$

したがって，$F$ は定数倍および定数項の任意性を除いて次のように与えられます。

$$
\finalanswer{F = \frac{1}{2}u^2 - \frac{\mathrm{d}u}{\mathrm{d}x}}
$$

(ii) (i) より $\dfrac{1}{2}u^2 - \dfrac{\mathrm{d}u}{\mathrm{d}x} = C$（$C$ は定数）です。$x \to \pm\infty$ で $u(x) \to \mp W$ かつ $\dfrac{\mathrm{d}u}{\mathrm{d}x} \to 0$ なので，$C = \dfrac{1}{2}W^2$ と決まります。

$$
\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{2}\left(u^2 - W^2\right)
$$

$-W < u < W$ で変数分離して部分分数分解により積分します。

$$
\begin{aligned}
\frac{\mathrm{d}u}{u^2 - W^2} &= \frac{1}{2}\mathrm{d}x \\
\frac{1}{2W}\left(\frac{1}{u - W} - \frac{1}{u + W}\right)\mathrm{d}u &= \frac{1}{2}\mathrm{d}x \\
\frac{1}{2W}\ln\frac{W - u}{W + u} &= \frac{x}{2} + C_0
\end{aligned}
$$

境界条件 $u(0) = 0$ を代入すると $C_0 = 0$ です。よって

$$
\frac{W - u}{W + u} = e^{Wx}
\implies W - u = (W + u)e^{Wx}
\implies u(x) = W\frac{1 - e^{Wx}}{1 + e^{Wx}} = -W\tanh\left(\frac{Wx}{2}\right)
$$

となります（$x \to \pm\infty$ で $\mp W$ に収束することも満たします）。したがって，

$$
\finalanswer{u(x) = -W\tanh\left(\frac{Wx}{2}\right)}
$$

### (3)
(i) 式 (3) の両辺を $x$ で偏微分します。

$$
\frac{\partial}{\partial t}\left(\frac{\partial s}{\partial x}\right)
= \frac{\partial s}{\partial x}\frac{\partial^2 s}{\partial x^2} + D\frac{\partial^2}{\partial x^2}\left(\frac{\partial s}{\partial x}\right)
$$

両辺に $-1$ を掛けて $u^*(t, x) = -\dfrac{\partial s(t, x)}{\partial x}$ を代入します。

$$
\frac{\partial u^*}{\partial t} = -u^*\frac{\partial u^*}{\partial x} + D\frac{\partial^2 u^*}{\partial x^2}
\implies \frac{\partial u^*}{\partial t} + u^*\frac{\partial u^*}{\partial x} = D\frac{\partial^2 u^*}{\partial x^2}
$$

よって $u^*(t, x)$ は式 (2) の解となります。

(ii) $s^*(t, x) = S(\phi(t, x))$ の各偏微分を合成関数の微分則で計算します。

$$
\begin{aligned}
\frac{\partial s^*}{\partial t} &= S'(\phi)\frac{\partial\phi}{\partial t} \\
\frac{\partial s^*}{\partial x} &= S'(\phi)\frac{\partial\phi}{\partial x} \\
\frac{\partial^2 s^*}{\partial x^2} &= S''(\phi)\left(\frac{\partial\phi}{\partial x}\right)^2 + S'(\phi)\frac{\partial^2\phi}{\partial x^2}
\end{aligned}
$$

これらを式 (3) に代入し，式 (4) の $\dfrac{\partial\phi}{\partial t} = D\dfrac{\partial^2\phi}{\partial x^2}$ を用います。

$$
\begin{aligned}
D S'(\phi)\frac{\partial^2\phi}{\partial x^2}
&= \frac{1}{2}\bigl(S'(\phi)\bigr)^2\left(\frac{\partial\phi}{\partial x}\right)^2 + D S''(\phi)\left(\frac{\partial\phi}{\partial x}\right)^2 + D S'(\phi)\frac{\partial^2\phi}{\partial x^2} \\
\left[D S''(\phi) + \frac{1}{2}\bigl(S'(\phi)\bigr)^2\right]\left(\frac{\partial\phi}{\partial x}\right)^2 &= 0
\end{aligned}
$$

任意の解 $\phi(t, x)$ に対して成り立つためには，$S(\phi)$ が次の常微分方程式を満たす必要があります。

$$
D S''(\phi) + \frac{1}{2}\bigl(S'(\phi)\bigr)^2 = 0
$$

$S'(\phi) \neq 0$ として $p(\phi) = S'(\phi)$ とおくと，$\dfrac{p'}{p^2} = -\dfrac{1}{2D}$ となります。両辺を $\phi$ で積分します。

$$
-\frac{1}{p(\phi)} = -\frac{\phi + C_1}{2D} \implies S'(\phi) = \frac{2D}{\phi + C_1}
$$

もう一度積分すると，$S(\phi) = 2D\ln|\phi + C_1| + C_2$（$C_1,\ C_2$ は積分定数；また $S'(\phi) \equiv 0$ に対応する定数解 $S(\phi) = C_2$ もあります）となります。したがって（$C_1,\ C_2$ は任意の定数），

$$
\finalanswer{D\frac{\mathrm{d}^2 S}{\mathrm{d}\phi^2} + \frac{1}{2}\left(\frac{\mathrm{d}S}{\mathrm{d}\phi}\right)^2 = 0,\qquad S(\phi) = 2D\ln|\phi + C_1| + C_2}
$$

(iii) フーリエ変換の表式を式 (4) に代入し，積分記号下で微分します。

$$
\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\left(\frac{\partial\tilde{\phi}(t, k)}{\partial t} + Dk^2\tilde{\phi}(t, k)\right)e^{ikx}\,\mathrm{d}k = 0
$$

フーリエ変換の一意性より，$\tilde{\phi}(t, k)$ が満たす微分方程式は次のとおりです。

$$
\frac{\partial\tilde{\phi}(t, k)}{\partial t} = -Dk^2\tilde{\phi}(t, k)
$$

初期条件 $\tilde{\phi}(0, k) = g(k)$ のもとで $t$ について解くと，$\tilde{\phi}(t, k) = g(k) e^{-Dk^2 t}$ となります。したがって，

$$
\finalanswer{\frac{\partial\tilde{\phi}(t, k)}{\partial t} = -Dk^2\tilde{\phi}(t, k),\qquad \tilde{\phi}(t, k) = g(k)\,e^{-Dk^2 t}}
$$

<aside class="rigor-note" markdown>
式 (2) は粘性バーガース（Burgers）方程式，式 (3) は KPZ（Kardar–Parisi–Zhang）方程式のノイズのない形，そして問3(i)(ii)の組み合わせ $u = -2D\dfrac{\partial_x\phi}{\phi}$ はコール・ホップ（Cole–Hopf）変換と呼ばれます。問2(ii)で求めた $u(x) = -W\tanh(Wx/2)$ は，非線形による波形の切り立ちと拡散による平滑化が釣り合った定常衝撃波解です。
</aside>
