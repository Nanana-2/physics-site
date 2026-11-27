---
title: 東大理物 平成19年度 数学 第2問：コーシー・リーマンの関係式とガウス型フーリエ積分
tags:
  - 院試過去問
  - 東大理物
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成19年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成19年度 数学 第2問：コーシー・リーマンの関係式とガウス型フーリエ積分

## 問題

二つの実変数 $x, y$ の実関数 $u(x, y),\ v(x, y)$ は至るところで有限な値を持ち，任意回微分可能で，さらに関係式

$$
\frac{\partial u(x, y)}{\partial x} = \frac{\partial v(x, y)}{\partial y}, \qquad \frac{\partial u(x, y)}{\partial y} = -\frac{\partial v(x, y)}{\partial x} \tag{1}
$$

を満たしているものとする。

(1) 以下の等式が成り立つことを示せ。

$$
\frac{\partial^2 u(x, y)}{\partial x^2} + \frac{\partial^2 u(x, y)}{\partial y^2} = 0, \qquad \frac{\partial^2 v(x, y)}{\partial x^2} + \frac{\partial^2 v(x, y)}{\partial y^2} = 0. \tag{2}
$$

(2) ストークスの定理は，微分可能なベクトル場 $\boldsymbol{A}(\boldsymbol{x})$ の，閉曲線 $\mathrm{C}$ を一周する線積分と，$\mathrm{C}$ を縁とする面 $\mathrm{S}$ 上の面積分との関係を表し，次式で与えられる。

$$
\oint_{\mathrm{C}} \boldsymbol{A}(\boldsymbol{x})\cdot\mathrm{d}\boldsymbol{x} = \iint_{\mathrm{S}} \bigl[\nabla\times\boldsymbol{A}(\boldsymbol{x})\bigr]\cdot\boldsymbol{n}(\boldsymbol{x})\,\mathrm{d}S. \tag{3}
$$

ただし，ベクトル $\boldsymbol{n}(\boldsymbol{x})$ は，面 $\mathrm{S}$ 上の点 $\boldsymbol{x}$ におけるこの面の法線ベクトルである。この定理を用いて，$xy$ 平面上の任意の閉じた経路 $\mathrm{C}$ に関する線積分に対して，以下の二式が成り立つことを示せ。

$$
\oint_{\mathrm{C}} \bigl[u(x, y)\,\mathrm{d}x - v(x, y)\,\mathrm{d}y\bigr] = 0, \qquad \oint_{\mathrm{C}} \bigl[u(x, y)\,\mathrm{d}y + v(x, y)\,\mathrm{d}x\bigr] = 0. \tag{4}
$$

(3) $i$ を虚数単位とし，複素数 $z$ を $z = x + iy$ によって定義する。また，複素関数 $f(z)$ は実関数 $u(x, y),\ v(x, y)$ を用いて，$f(z) = u(x, y) + iv(x, y)$ のように表されるものとする。式 (4) が成り立っているとき，複素平面上の任意の閉じた経路 $\mathrm{C}$ に関する線積分に対して，以下の等式が成り立つことを示せ。

$$
\oint_{\mathrm{C}} f(z)\,\mathrm{d}z = 0. \tag{5}
$$

(4) 複素関数 $f(z)$ の例として，$f(z) = e^{-z^2}$ を考える。$f(x + iy)$ の実部を $u(x, y)$，虚部を $v(x, y)$ としたとき，式 (1) が成り立つことを示せ。

(5) 以上の結果を用いて，実数 $p$ に対して，定積分

$$
\int_{-\infty}^{\infty} e^{-x^2}\cos(2px)\,\mathrm{d}x \tag{6}
$$

を求めよ。ただし，

$$
\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x = \sqrt{\pi} \tag{7}
$$

となることは既知としてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成19年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
実部と虚部がコーシー・リーマンの関係式 (1) を満たす複素関数では，実部と虚部から作る2次元ベクトル場の回転が $0$ になります。そのため，ストークスの定理を用いると任意の閉経路に沿った複素積分が $0$ になるというコーシーの積分定理を導くことができます。

この積分定理をガウス関数 $e^{-z^2}$ と複素平面上の長方形経路に用いると，実軸上の積分を虚軸方向に $ip$ だけ平行移動した直線上の積分へ移すことができます。展開して出てくる振動因子 $\cos(2px)$ がそのまま求める定積分と結びつきます。
</div>

### (1)

$u(x, y), v(x, y)$ は任意回微分可能なので，2階偏微分の順序を入れ替えることができます。式 (1) の第1式を $x$ で偏微分し，第2式を $y$ で偏微分して足し合わせます。

$$
\begin{aligned}
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} &= \frac{\partial}{\partial x}\left(\frac{\partial v}{\partial y}\right) + \frac{\partial}{\partial y}\left(-\frac{\partial v}{\partial x}\right) \\
&= \frac{\partial^2 v}{\partial x\partial y} - \frac{\partial^2 v}{\partial y\partial x} \\
&= 0
\end{aligned}
$$

次に，式 (1) の第2式を $x$ で偏微分して符号を反転し，第1式を $y$ で偏微分して足し合わせます。

$$
\begin{aligned}
\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} &= \frac{\partial}{\partial x}\left(-\frac{\partial u}{\partial y}\right) + \frac{\partial}{\partial y}\left(\frac{\partial u}{\partial x}\right) \\
&= -\frac{\partial^2 u}{\partial x\partial y} + \frac{\partial^2 u}{\partial y\partial x} \\
&= 0
\end{aligned}
$$



### (2)

$xy$ 平面上の閉曲線 $\mathrm{C}$ を縁とする平面領域を $\mathrm{S}$ とし，法線ベクトルを $\boldsymbol{n} = (0, 0, 1)$ とします。また，3次元ベクトル場 $\boldsymbol{A}_1(\boldsymbol{x}) = (u(x, y), -v(x, y), 0)$ と $\boldsymbol{A}_2(\boldsymbol{x}) = (v(x, y), u(x, y), 0)$ を定義します。

まず $\boldsymbol{A}_1$ の回転の $z$ 成分を計算し，式 (1) の第2式を用います。

$$
\begin{aligned}
\bigl[\nabla\times\boldsymbol{A}_1\bigr]\cdot\boldsymbol{n} &= \frac{\partial(-v)}{\partial x} - \frac{\partial u}{\partial y} \\
&= -\left(\frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}\right) \\
&= 0
\end{aligned}
$$

よってストークスの定理 (3) より次式が成り立ちます。

$$
\begin{aligned}
\oint_{\mathrm{C}} \bigl[u(x, y)\,\mathrm{d}x - v(x, y)\,\mathrm{d}y\bigr] &= \oint_{\mathrm{C}} \boldsymbol{A}_1\cdot\mathrm{d}\boldsymbol{x} \\
&= \iint_{\mathrm{S}} \bigl[\nabla\times\boldsymbol{A}_1\bigr]\cdot\boldsymbol{n}\,\mathrm{d}S \\
&= 0
\end{aligned}
$$

次に $\boldsymbol{A}_2$ の回転の $z$ 成分を計算し，式 (1) の第1式を用います。

$$
\begin{aligned}
\bigl[\nabla\times\boldsymbol{A}_2\bigr]\cdot\boldsymbol{n} &= \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} \\
&= 0
\end{aligned}
$$

よってストークスの定理 (3) より次式が成り立ちます。

$$
\begin{aligned}
\oint_{\mathrm{C}} \bigl[u(x, y)\,\mathrm{d}y + v(x, y)\,\mathrm{d}x\bigr] &= \oint_{\mathrm{C}} \boldsymbol{A}_2\cdot\mathrm{d}\boldsymbol{x} \\
&= \iint_{\mathrm{S}} \bigl[\nabla\times\boldsymbol{A}_2\bigr]\cdot\boldsymbol{n}\,\mathrm{d}S \\
&= 0
\end{aligned}
$$



### (3)

$z = x + iy$ より $\mathrm{d}z = \mathrm{d}x + i\,\mathrm{d}y$ です。$f(z)\,\mathrm{d}z$ を実部と虚部に展開して積分します。

$$
\begin{aligned}
\oint_{\mathrm{C}} f(z)\,\mathrm{d}z &= \oint_{\mathrm{C}} \bigl(u(x, y) + iv(x, y)\bigr)(\mathrm{d}x + i\,\mathrm{d}y) \\
&= \oint_{\mathrm{C}} \bigl[u(x, y)\,\mathrm{d}x - v(x, y)\,\mathrm{d}y\bigr] + i\oint_{\mathrm{C}} \bigl[u(x, y)\,\mathrm{d}y + v(x, y)\,\mathrm{d}x\bigr] \\
&= 0 + i\cdot 0 \\
&= 0
\end{aligned}
$$

ここで式 (4) を用いました。したがって式 (5) が成り立ちます。

### (4)

$z = x + iy$ を $f(z) = e^{-z^2}$ に代入して実部と虚部に分けます。

$$
\begin{aligned}
f(x + iy) &= \exp\!\bigl(-(x + iy)^2\bigr) \\
&= \exp\!\bigl(-(x^2 - y^2) - 2ixy\bigr) \\
&= e^{-x^2 + y^2}\bigl(\cos(2xy) - i\sin(2xy)\bigr)
\end{aligned}
$$

よって，$u(x, y) = e^{-x^2 + y^2}\cos(2xy)$，$v(x, y) = -e^{-x^2 + y^2}\sin(2xy)$ です。それぞれの $x$ 偏微分と $y$ 偏微分を計算します。

$$
\begin{aligned}
\frac{\partial u}{\partial x} &= -2x e^{-x^2 + y^2}\cos(2xy) - 2y e^{-x^2 + y^2}\sin(2xy) \\
&= -2e^{-x^2 + y^2}\bigl(x\cos(2xy) + y\sin(2xy)\bigr)
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial v}{\partial y} &= -2y e^{-x^2 + y^2}\sin(2xy) - 2x e^{-x^2 + y^2}\cos(2xy) \\
&= -2e^{-x^2 + y^2}\bigl(x\cos(2xy) + y\sin(2xy)\bigr)
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial u}{\partial y} &= 2y e^{-x^2 + y^2}\cos(2xy) - 2x e^{-x^2 + y^2}\sin(2xy) \\
&= 2e^{-x^2 + y^2}\bigl(y\cos(2xy) - x\sin(2xy)\bigr)
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial v}{\partial x} &= 2x e^{-x^2 + y^2}\sin(2xy) - 2y e^{-x^2 + y^2}\cos(2xy) \\
&= -2e^{-x^2 + y^2}\bigl(y\cos(2xy) - x\sin(2xy)\bigr)
\end{aligned}
$$

これらを比べると，$\dfrac{\partial u}{\partial x} = \dfrac{\partial v}{\partial y}$ および $\dfrac{\partial u}{\partial y} = -\dfrac{\partial v}{\partial x}$ が成り立ちます。

### (5)

求める積分 $\displaystyle I(p) = \int_{-\infty}^{\infty} e^{-x^2}\cos(2px)\,\mathrm{d}x$ は $p$ の偶関数であり，$p = 0$ のときは式 (7) より $I(0) = \sqrt{\pi}$ です。そこで以下では $p > 0$ の場合を考えます。

$R > 0$ とし，複素平面上の4点 $-R,\ R,\ R + ip,\ -R + ip$ をこの順に反時計回りに結ぶ長方形の閉経路 $C$ をとります。

<figure class="problem-figure" markdown>
![複素平面上の長方形積分経路 C](../../../docs/assets/figures/pastexam-todai-ributsu/H19_sugaku_2-s-light.svg#only-light)
![複素平面上の長方形積分経路 C](../../../docs/assets/figures/pastexam-todai-ributsu/H19_sugaku_2-s-dark.svg#only-dark)
<figcaption markdown="span">長方形の積分経路 $C$。</figcaption>
</figure>

設問3と設問4より，この閉経路 $C$ 上で $\oint_C e^{-z^2}\,\mathrm{d}z = 0$ が成り立ちます。各辺の積分に分解します。

$$
\begin{aligned}
0 &= \int_{-R}^{R} e^{-x^2}\,\mathrm{d}x + \int_{0}^{p} e^{-(R + iy)^2} i\,\mathrm{d}y \\
&\quad + \int_{R}^{-R} e^{-(x + ip)^2}\,\mathrm{d}x + \int_{p}^{0} e^{-(-R + iy)^2} i\,\mathrm{d}y
\end{aligned}
$$

右辺の縦辺上の2つの積分の大きさを上から抑えます。$0 \le y \le p$ のとき $|e^{-(\pm R + iy)^2}| = e^{-R^2 + y^2} \le e^{-R^2 + p^2}$ です。

$$
\begin{aligned}
\left|\int_{0}^{p} e^{-(\pm R + iy)^2} i\,\mathrm{d}y\right| &\le \int_{0}^{p} e^{-R^2 + p^2}\,\mathrm{d}y \\
&= p\,e^{p^2} e^{-R^2} \xrightarrow{R \to \infty} 0
\end{aligned}
$$

したがって，$R \to \infty$ の極限をとると縦辺の積分は $0$ になり，上辺の積分を移項して次式が得られます。

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x &= \int_{-\infty}^{\infty} e^{-(x + ip)^2}\,\mathrm{d}x \\
&= \int_{-\infty}^{\infty} e^{-x^2 + p^2 - 2ipx}\,\mathrm{d}x \\
&= e^{p^2}\int_{-\infty}^{\infty} e^{-x^2}\bigl(\cos(2px) - i\sin(2px)\bigr)\,\mathrm{d}x
\end{aligned}
$$

左辺は式 (7) より $\sqrt{\pi}$ です。両辺の実部をとって $e^{p^2}$ で割ります。

$$
\sqrt{\pi}=e^{p^2}\int_{-\infty}^{\infty}e^{-x^2}\cos(2px)\,\mathrm{d}x
$$

正の因子 $e^{p^2}$ で割ると，次の式になります。

$$
\int_{-\infty}^{\infty}e^{-x^2}\cos(2px)\,\mathrm{d}x=\sqrt{\pi}e^{-p^2}
$$

偶関数性より，この式は $p < 0$ および $p = 0$ を含むすべての実数 $p$ に対して成り立ちます。したがって，求める定積分は次式となります。

$$
\finalanswer{\int_{-\infty}^{\infty} e^{-x^2}\cos(2px)\,\mathrm{d}x = \sqrt{\pi}\,e^{-p^2}}
$$
