---
title: 東大理物 令和2年度 数学 第1問：誤差関数と移流拡散方程式
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 令和2年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加しています。
---

# 東大理物 令和2年度 数学 第1問：誤差関数と移流拡散方程式

## 問題

以下の設問に答えよ。解答の際，ガウスの積分公式

$$
\int_{-\infty}^{\infty} dx\, e^{-\frac{1}{2}ax^2 + ipx} = \sqrt{\frac{2\pi}{a}} e^{-\frac{p^2}{2a}}
$$

を用いてよい。公式中で，$a > 0$，$p$ は実数，$i$ は虚数単位である。

(1) 誤差関数

$$
\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x d\xi\, e^{-\xi^2}
$$

について以下の小問に答えよ。

(i) $x = 0$ の周りのテイラー展開（マクローリン展開）を与えよ。

(ii) $x = \infty$ の周りで漸近展開すると，最初の2項は次のように与えられることを示せ。ヒント：$\xi^2 = \eta$ のように積分変数を変更し，部分積分を用いて求めよ。

$$
\operatorname{erf}(x) \sim 1 - \frac{1}{\sqrt{\pi}\,x} e^{-x^2} + \text{（高次の項）}
$$

(2) 偏微分方程式

$$
\frac{\partial u(x, t)}{\partial t} = -c\frac{\partial u(x, t)}{\partial x} + \frac{\lambda}{2}\frac{\partial^2 u(x, t)}{\partial x^2}
$$

を時刻 $t = 0$ における初期条件 $\left.u(x, t)\right|_{t=0} = U(x)$ のもとで，領域 $t \ge 0,\ -\infty < x < \infty$ で解く。パラメータの定義域は $c > 0,\ \lambda \ge 0$ とする。

(i) $\lambda = 0$ の場合の解を求めよ。ただし，$U(x)$ は任意の微分可能な関数とする。

以下の小問では $\lambda > 0$ の場合を考える。

(ii) $u(x, t)$ の $x$ に関するフーリエ変換を

$$
\tilde{u}(k, t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} dx\, e^{-ikx} u(x, t)
$$

と定義する。$\tilde{u}(k, t)$ が満たす微分方程式と初期条件を求めよ。

(iii) $U(x) = \delta(x)$ とするときの解 $u(x, t)$ を $G(x, t)$ と書く。ここで $\delta(x)$ はディラックのデルタ関数である。$x$ に関するフーリエ逆変換を用いて $G(x, t)$ を求めよ。

(iv) $U(x)$ が

$$
U(x) = \begin{cases} 1 & x < 0 \\ 0 & x \ge 0 \end{cases}
$$

のように与えられた場合の偏微分方程式の解を誤差関数を用いて書き表せ。また時刻 $t$ の経過とともに $u(x, t)$ の概形がどのように変化するのか説明せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 令和2年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
誤差関数は $e^{-\xi^2}$ の積分です。$x$ が小さいときは，被積分関数をべき級数に展開して項ごとに積分します。$x$ が大きいときは，$\displaystyle\int_x^\infty$ の部分を部分積分すると $e^{-x^2}$ に $1/x$ のべきを掛けた形になり，残りの積分の大きさも上から抑えることができます。

移流拡散方程式は線形で係数が定数なので，フーリエ変換すると波数 $k$ ごとの1階の常微分方程式になります。初期条件が $\delta(x)$ のときの解 $G$ を求めておけば，任意の初期条件の解は $G$ との畳み込みで書くことができます。
</div>

### (1)
(i) 指数関数 $e^{-\xi^2}$ のマクローリン展開は，任意の有限区間で一様収束します。したがって，固定した有限の $x$ に対し，$0$ と $x$ を結ぶ区間で項別積分することができます。

$$
\begin{aligned}
\operatorname{erf}(x)
&= \frac{2}{\sqrt{\pi}} \int_0^x \left(\sum_{n=0}^{\infty} \frac{(-\xi^2)^n}{n!}\right)\mathrm{d}\xi \\
&= \frac{2}{\sqrt{\pi}} \sum_{n=0}^{\infty} \frac{(-1)^n}{n!} \int_0^x \xi^{2n}\,\mathrm{d}\xi \\
&= \frac{2}{\sqrt{\pi}} \sum_{n=0}^{\infty} \frac{(-1)^n}{n!\,(2n + 1)} x^{2n + 1}
\end{aligned}
$$

したがって，

$$
\finalanswer{\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \sum_{n=0}^{\infty} \frac{(-1)^n}{n!\,(2n + 1)} x^{2n + 1}}
$$

(ii) $\displaystyle\int_0^{\infty} e^{-\xi^2}\,\mathrm{d}\xi = \dfrac{\sqrt{\pi}}{2}$ を用いて，誤差関数を $x > 0$ で次のように書き換えます。

$$
\operatorname{erf}(x) = 1 - \frac{2}{\sqrt{\pi}} \int_x^{\infty} e^{-\xi^2}\,\mathrm{d}\xi
$$

ヒントに従い $\xi^2=\eta$ と変数変換します。$\xi=\sqrt\eta$，$\mathrm{d}\xi=\dfrac12\eta^{-1/2}\mathrm{d}\eta$ を使い，部分積分します。

$$
\begin{aligned}
\int_x^{\infty} e^{-\xi^2}\,\mathrm{d}\xi
&= \frac{1}{2}\int_{x^2}^{\infty} \eta^{-\frac{1}{2}} e^{-\eta}\,\mathrm{d}\eta \\
&= \frac{1}{2}\left[-\eta^{-\frac{1}{2}} e^{-\eta}\right]_{x^2}^{\infty} - \frac{1}{4}\int_{x^2}^{\infty} \eta^{-\frac{3}{2}} e^{-\eta}\,\mathrm{d}\eta \\
&= \frac{e^{-x^2}}{2x} - \frac{1}{4}\int_{x^2}^{\infty} \eta^{-\frac{3}{2}} e^{-\eta}\,\mathrm{d}\eta
\end{aligned}
$$

右辺第2項の積分は $\eta \ge x^2$ で $\eta^{-3/2} \le x^{-3}$ なので，

$$
0 < \frac{1}{4}\int_{x^2}^{\infty} \eta^{-\frac{3}{2}} e^{-\eta}\,\mathrm{d}\eta \le \frac{1}{4x^3}\int_{x^2}^{\infty} e^{-\eta}\,\mathrm{d}\eta = \frac{e^{-x^2}}{4x^3}
$$

と評価され，$x \to \infty$ で第1項 $\dfrac{e^{-x^2}}{2x}$ に対して $O(x^{-3}e^{-x^2})$ の微小項となります。これを元の式に代入すると，

$$
\operatorname{erf}(x) = 1 - \frac{1}{\sqrt{\pi}\,x} e^{-x^2} + O\left(\frac{e^{-x^2}}{x^3}\right)
$$

となり，最初の2項が問題文の漸近展開に一致することが確かめられます。

### (2)
(i) $\lambda = 0$ のとき，偏微分方程式は1階の移流方程式 $\dfrac{\partial u}{\partial t} + c\dfrac{\partial u}{\partial x} = 0$ となります。

特性変数 $\xi = x - ct,\ \tau = t$ へ変数変換すると，$\dfrac{\partial}{\partial t} = \dfrac{\partial}{\partial\tau} - c\dfrac{\partial}{\partial\xi}$，$\dfrac{\partial}{\partial x} = \dfrac{\partial}{\partial\xi}$ より方程式は $\dfrac{\partial u}{\partial\tau} = 0$ となります。よって $u$ は $\xi = x - ct$ のみの関数 $u(x, t) = f(x - ct)$ であり，初期条件 $u(x, 0) = f(x) = U(x)$ より $f = U$ と決まります。したがって，

$$
\finalanswer{u(x, t) = U(x - ct)}
$$

(ii) 偏微分方程式の両辺に $\dfrac{1}{\sqrt{2\pi}}e^{-ikx}$ を掛けて $x$ について $-\infty$ から $\infty$ まで積分します。$|x| \to \infty$ で $u(x, t)$ と $\dfrac{\partial u}{\partial x}$ が十分速く $0$ に収束するとすると，部分積分によって $\dfrac{\partial u}{\partial x}$ のフーリエ変換は $ik\tilde{u}(k, t)$，$\dfrac{\partial^2 u}{\partial x^2}$ のフーリエ変換は $(ik)^2\tilde{u}(k, t) = -k^2\tilde{u}(k, t)$ となります。

よって $\tilde{u}(k, t)$ が満たす微分方程式と初期条件は次のとおりです。したがって，

$$
\finalanswer{\frac{\partial\tilde{u}(k, t)}{\partial t} = \left(-ick - \frac{\lambda}{2}k^2\right)\tilde{u}(k, t),\qquad \tilde{u}(k, 0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{-ikx} U(x)\,\mathrm{d}x}
$$

(iii) 初期条件 $U(x) = \delta(x)$ に対する $\tilde{G}(k, 0)$ は次のようになります。

$$
\begin{aligned}
\tilde{G}(k, 0) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{-ikx}\delta(x)\,\mathrm{d}x \\
&= \frac{1}{\sqrt{2\pi}}
\end{aligned}
$$

(ii) の微分方程式を $t$ について解くと，

$$
\tilde{G}(k, t) = \frac{1}{\sqrt{2\pi}}\exp\left[\left(-ick - \frac{\lambda}{2}k^2\right)t\right]
$$

となります。これをフーリエ逆変換し，問題文のガウス積分公式に $a=\lambda t>0$，$p=x-ct$ を代入して $G(x, t)$ を求めます。

$$
\begin{aligned}
G(x, t)
&= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{ikx}\,\tilde{G}(k, t)\,\mathrm{d}k \\
&= \frac{1}{2\pi}\int_{-\infty}^{\infty} \exp\left[-\frac{1}{2}(\lambda t)k^2 + i(x - ct)k\right]\mathrm{d}k \\
&= \frac{1}{2\pi}\sqrt{\frac{2\pi}{\lambda t}}\exp\left(-\frac{(x - ct)^2}{2\lambda t}\right) \\
&= \frac{1}{\sqrt{2\pi\lambda t}}\exp\left(-\frac{(x - ct)^2}{2\lambda t}\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{G(x, t) = \frac{1}{\sqrt{2\pi\lambda t}}\exp\left(-\frac{(x - ct)^2}{2\lambda t}\right)\qquad(t>0)}
$$

(iv) 偏微分方程式の線形性と並進不変性より，任意の初期条件 $U(x)$ に対する解はグリーン関数 $G(x, t)$ との畳み込み積分で与えられます。

$$
\begin{aligned}
u(x, t)
&= \int_{-\infty}^{\infty} G(x - x', t) U(x')\,\mathrm{d}x' \\
&= \int_{-\infty}^{0} \frac{1}{\sqrt{2\pi\lambda t}}\exp\left(-\frac{(x - x' - ct)^2}{2\lambda t}\right)\mathrm{d}x'
\end{aligned}
$$

積分変数を $\xi=\dfrac{x-x'-ct}{\sqrt{2\lambda t}}$ とおくと，$\mathrm{d}x'=-\sqrt{2\lambda t}\,\mathrm{d}\xi$ です。$x'=-\infty$ では $\xi=+\infty$，$x'=0$ では $\xi=\dfrac{x-ct}{\sqrt{2\lambda t}}$ なので，

$$
\begin{aligned}
u(x, t)
&= \frac{1}{\sqrt{\pi}}\int_{\frac{x - ct}{\sqrt{2\lambda t}}}^{\infty} e^{-\xi^2}\,\mathrm{d}\xi \\
&= \frac{1}{\sqrt{\pi}}\left(\int_0^{\infty} e^{-\xi^2}\,\mathrm{d}\xi - \int_0^{\frac{x - ct}{\sqrt{2\lambda t}}} e^{-\xi^2}\,\mathrm{d}\xi\right) \\
&= \frac{1}{2}\left[1 - \operatorname{erf}\left(\frac{x - ct}{\sqrt{2\lambda t}}\right)\right]
\end{aligned}
$$

したがって，

$$
\finalanswer{u(x, t) = \frac{1}{2}\left[1 - \operatorname{erf}\left(\frac{x - ct}{\sqrt{2\lambda t}}\right)\right]\qquad(t>0)}
$$

解の概形を調べます。初期分布は $x<0$ で1，$x\ge0$ で0です。$t>0$ では滑らかな単調減少関数になります。値が $1/2$ となる中心位置 $x=ct$ は速さ $c$ で正の向きに動きます。分布の幅を与える $\sqrt{2\lambda t}$ は $\sqrt t$ に比例して増えるため，遷移領域は時間とともに広がります。

<figure class="problem-figure" markdown>
![移流拡散方程式の解 u(x,t) の時間変化](../../../docs/assets/figures/pastexam-todai-ributsu/R2_sugaku_1-s-light.svg#only-light)
![移流拡散方程式の解 u(x,t) の時間変化](../../../docs/assets/figures/pastexam-todai-ributsu/R2_sugaku_1-s-dark.svg#only-dark)
<figcaption markdown="span">階段状の初期分布（$t = 0$，破線）に対する移流拡散方程式の解 $u(x, t)$ の時間発展（$0 < t_1 < t_2$）。中心 $x = ct$ が速さ $c$ で右へ移動しながら，段差の幅が $\sqrt{2\lambda t}$ でなだらかに広がる。</figcaption>
</figure>

<aside class="rigor-note" markdown>
$G(x,t)$ の初期条件は分布として $G(x,t)\to\delta(x)$ と解釈します。設問2(iv)の解も，初期関数が連続な $x\ne0$ では $t\to0+$ で $U(x)$ に収束します。$x=0$ での極限は $1/2$ なので，指定された $U(0)=0$ には点ごとには収束しません。初期時刻の値は別に $u(x,0)=U(x)$ と定め，初期条件は分布またはほとんど至る所で満たすものとします。

階段関数は無限遠で0にならないため，設問2(ii)の通常の部分積分の仮定を満たしません。この場合も緩増加分布のフーリエ変換を使うと，同じ微分方程式が成り立ちます。
</aside>
