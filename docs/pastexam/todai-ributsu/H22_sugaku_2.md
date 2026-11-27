---
title: 東大理物 平成22年度 数学 第2問：1次元波動方程式のダランベールの公式とエネルギー保存
tags:
  - 院試過去問
  - 東大理物
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
変数を $\xi=x+vt$，$\eta=x-vt$ に変えると，左へ進む波と右へ進む波を別々の変数で表すことができます。そのため，波動方程式は $\xi$ と $\eta$ で1回ずつ微分した形になり，順に積分して一般解を作ることができます。

$I$ が $t$ によらないことは，$\dfrac{\mathrm{d}I}{\mathrm{d}t}$ を計算して示します。時間の2階微分を波動方程式で空間の2階微分に置き換えると，被積分関数は $x$ についての全微分になり，$x\to\pm\infty$ での値だけが残ります。

初期条件は，$t=0$ での $u$ と $\dfrac{\partial u}{\partial t}$ の2つです。この2つから $f$ と $g$ の和と，微分の差がわかるので，連立して $f$ と $g$ を求めます。初期速度はローレンツ型なので，その積分は $\arctan$ で書くことができます。
</div>

### (1)
$\xi = x + vt$，$\eta = x - vt$ より，合成関数の微分法を用いて $\dfrac{\partial}{\partial t}$ と $\dfrac{\partial}{\partial x}$ を書き換えます。

$$
\begin{aligned}
\frac{\partial}{\partial x} &= \frac{\partial\xi}{\partial x}\frac{\partial}{\partial\xi} + \frac{\partial\eta}{\partial x}\frac{\partial}{\partial\eta} \\
&= \frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta} \\
\frac{\partial}{\partial t} &= \frac{\partial\xi}{\partial t}\frac{\partial}{\partial\xi} + \frac{\partial\eta}{\partial t}\frac{\partial}{\partial\eta} \\
&= v\left(\frac{\partial}{\partial\xi} - \frac{\partial}{\partial\eta}\right)
\end{aligned}
$$

これらを式 (1) に代入します。

$$
\begin{aligned}
\frac{1}{v^2}\frac{\partial^2 u}{\partial t^2} - \frac{\partial^2 u}{\partial x^2} &= \left(\frac{\partial}{\partial\xi} - \frac{\partial}{\partial\eta}\right)^2 u - \left(\frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta}\right)^2 u \\
&= -4\frac{\partial^2 u}{\partial\xi\partial\eta} \\
&= 0
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



### (3)
設問(2)の一般解を用い，$F=f'$，$G=g'$ とおきます。時間微分と空間微分は次のとおりです。

$$
\begin{aligned}
\frac1v\frac{\partial u}{\partial t}&=F(x+vt)-G(x-vt),\\
\frac{\partial u}{\partial x}&=F(x+vt)+G(x-vt)
\end{aligned}
$$

2乗して加えると交差項が消えます。

$$
\frac12\left[\frac1{v^2}\left(\frac{\partial u}{\partial t}\right)^2
+\left(\frac{\partial u}{\partial x}\right)^2\right]
=F(x+vt)^2+G(x-vt)^2
$$

したがって，それぞれの積分で変数を平行移動すると，次のようになります。

$$
\begin{aligned}
I(t)&=\int_{-\infty}^{\infty}F(x+vt)^2\,\mathrm{d}x
+\int_{-\infty}^{\infty}G(x-vt)^2\,\mathrm{d}x\\
&=\int_{-\infty}^{\infty}F(\xi)^2\,\mathrm{d}\xi
+\int_{-\infty}^{\infty}G(\eta)^2\,\mathrm{d}\eta\\
&=I(0)
\end{aligned}
$$

仮定より積分は有限であり，右辺は $t$ に依存しません。

### (4)
設問 (2) の一般解 $u(x, t) = f(x + vt) + g(x - vt)$ に $t = 0$ の初期条件を代入します。

$$
\begin{aligned}
f(x) + g(x) &= u_0(x) \\
v\bigl(f'(x) - g'(x)\bigr) &= u_1(x)
\end{aligned}
$$

第2式を $0$ から $x$ まで積分します。積分定数を $C$ とおきます。

$$
f(x) - g(x) = \frac{1}{v}\int_0^x u_1(s)\,\mathrm{d}s + C
$$

これと第1式の和と差から $f(x)$ と $g(x)$ を求めます。

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
$t > 0$ を固定して $b \to 0+$ の極限をとります。実数 $X \neq 0$ に対して $X > 0$ なら $\displaystyle \lim_{b \to 0+}\arctan(X / b) = \dfrac{\pi}{2}$，$X < 0$ なら $\displaystyle \lim_{b \to 0+}\arctan(X / b) = -\dfrac{\pi}{2}$ なので，$x$ の範囲によって次のように場合分けされます。

$x<a-vt$ では，2つの逆正接はいずれも $-\pi/2$ に近づきます。$a-vt<x<a+vt$ ではそれぞれ $\pi/2$，$-\pi/2$ に近づき，$x>a+vt$ ではいずれも $\pi/2$ に近づきます。波面 $x=a\pm vt$ では一方の逆正接の引数が $0$ です。したがって，点ごとの極限は次のとおりです。

$$
\lim_{b\to0+}u(x,t)=\begin{cases}
0 &(x<a-vt\ \text{or}\ x>a+vt),\\
\dfrac v4 &(x=a\pm vt),\\
\dfrac v2 &(a-vt<x<a+vt)
\end{cases}
$$

したがって $b \to 0$ の極限では，$x = a$ を中心として区間 $a - vt < x < a + vt$ に高さ $v/2$ をもつ矩形波になります。図示すると次のとおりです。

<figure class="problem-figure" markdown>
![b->0極限における矩形波u(x,t)の概形](../../assets/figures/pastexam-todai-ributsu/H22_sugaku_2-s-light.svg#only-light)
![b->0極限における矩形波u(x,t)の概形](../../assets/figures/pastexam-todai-ributsu/H22_sugaku_2-s-dark.svg#only-dark)
<figcaption markdown="span">$b \to 0$ の極限における $t > 0$ での解 $u(x, t)$ の概形。</figcaption>
</figure>
