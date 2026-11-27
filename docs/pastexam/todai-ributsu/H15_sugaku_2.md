---
title: 東大理物 平成15年度 数学 第2問：球対称波動方程式の初期値問題とフーリエ変換
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 積分変換
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成15年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成15年度 数学 第2問：球対称波動方程式の初期値問題とフーリエ変換

## 問題

球対称の関数 $u(t, r)$ に対する波動方程式は，以下のように書くことができる：

$$
\frac{\partial^2 u}{\partial t^2} = c^2\left(\frac{\partial^2 u}{\partial r^2} + \frac{2}{r}\frac{\partial u}{\partial r}\right).
$$

ここで，$r$ は動径座標，$t$ は時間座標，$c$ は速度の次元の定数である。以下の問に答えよ。
{: .problem-lead }

(1) 上の偏微分方程式の一般解を求めよ。なおここで一般解とは2個の任意関数であらわされた解を指す。

(2) 初期条件，$t = 0$ で $u = e^{-r^2/(2r_0^2)}$，$\partial u/\partial t = 0$ の場合の $t > 0$ に対する解を求めよ。ただし，$r_0$ は波束の広がりをあらわす実定数である。

(3) 初期条件，$t = 0$ で $u = 0$，$\partial u/\partial t = e^{-r^2/(2r_0^2)}$ の場合の $t > 0$ に対する解を求めよ。

(4) (3) で求めた関数を，時間に対してフーリエ変換せよ。ただしここでフーリエ変換は，

$$
U(\omega, r) = \int_{-\infty}^{\infty} u(t, r)e^{i\omega t}\,\mathrm{d}t
$$

と定義する。

(5) $g(\omega) \equiv U(\omega, r = 0)$ は，$\omega$ の関数である。$g(\omega)$ が最大値となる $\omega$ の値を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成15年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
新しい従属変数 $w(t, r) = r u(t, r)$ を導入すると，球対称の3次元波動方程式は1次元の波動方程式と同じ形になります。これによりダランベールの一般解と初期値問題の公式をそのまま用いることができます。

得られたガウス型の球面波解に対して，時間に関するフーリエ変換を平方完成によるガウス積分で計算し，原点 $r \to 0$ での極限から周波数スペクトルの極値を求めます。
</div>

### (1)

関数 $w(t, r) = r u(t, r)$ を導入します。$w$ の $r$ に関する1階および2階偏微分を計算します。

$$
\frac{\partial w}{\partial r} = u + r\frac{\partial u}{\partial r}
$$

$$
\begin{aligned}
\frac{\partial^2 w}{\partial r^2} &= 2\frac{\partial u}{\partial r} + r\frac{\partial^2 u}{\partial r^2} \\
&= r\left(\frac{\partial^2 u}{\partial r^2} + \frac{2}{r}\frac{\partial u}{\partial r}\right)
\end{aligned}
$$

もとの波動方程式の両辺に $r$ を掛けると，$w(t, r)$ に関する1次元波動方程式が得られます。

$$
\frac{\partial^2 w}{\partial t^2} = c^2\frac{\partial^2 w}{\partial r^2}
$$

特性変数 $\xi = r - ct$，$\eta = r + ct$ を導入すると，$\dfrac{\partial^2 w}{\partial\xi\partial\eta} = 0$ となります。したがって，2つの2階微分可能な任意関数 $F, G$ を用いて一般解は $w(t, r) = F(r - ct) + G(r + ct)$ となります。$u = \dfrac{w}{r}$ より，求める一般解は次式となります。

$$
\finalanswer{u(t, r) = \frac{F(r - ct) + G(r + ct)}{r}}
$$

### (2)

$w(t, r) = r u(t, r)$ に対する $t = 0$ の初期条件は次式です。

$$
w(0, r) = r e^{-r^2/(2r_0^2)}, \qquad \left.\frac{\partial w}{\partial t}\right|_{t = 0} = 0
$$

また，$u(t, r) = \dfrac{w(t, r)}{r}$ が原点 $r = 0$ で発散しないためには，任意の時刻 $t$ で $w(t, 0) = 0$ を満たす必要があります。$w(0, r) = r e^{-r^2/(2r_0^2)}$ は $r$ の奇関数として全実数 $r \in (-\infty, \infty)$ に延長することができ，1次元波動方程式のダランベールの公式を当てはめます。

$$
w(t, r) = \frac{1}{2}\Bigl\{w(0, r - ct) + w(0, r + ct)\Bigr\}
$$

$r = 0$ を代入すると $w(0, -ct) + w(0, ct) = 0$ となり，境界条件 $w(t, 0) = 0$ を自動的に満たします。具体的に $w(0, s) = s e^{-s^2/(2r_0^2)}$ を代入して $r$ で割ると，求める解は次式となります。

$$
\finalanswer{u(t, r) = \frac{1}{2r}\left\{(r - ct)\exp\!\left(-\frac{(r - ct)^2}{2r_0^2}\right) + (r + ct)\exp\!\left(-\frac{(r + ct)^2}{2r_0^2}\right)\right\}}
$$

### (3)

$w(t, r) = r u(t, r)$ に対する $t = 0$ の初期条件は次式です。

$$
w(0, r) = 0, \qquad \left.\frac{\partial w}{\partial t}\right|_{t = 0} = r e^{-r^2/(2r_0^2)}
$$

$\left.\dfrac{\partial w}{\partial t}\right|_{t = 0}$ も $r$ の奇関数なので，ダランベールの公式により $w(t, 0) = 0$ を満たす解が次のように得られます。

$$
\begin{aligned}
w(t, r) &= \frac{1}{2c}\int_{r - ct}^{r + ct} s\exp\!\left(-\frac{s^2}{2r_0^2}\right)\mathrm{d}s \\
&= \frac{1}{2c}\left[-r_0^2\exp\!\left(-\frac{s^2}{2r_0^2}\right)\right]_{r - ct}^{r + ct} \\
&= \frac{r_0^2}{2c}\left\{\exp\!\left(-\frac{(r - ct)^2}{2r_0^2}\right) - \exp\!\left(-\frac{(r + ct)^2}{2r_0^2}\right)\right\}
\end{aligned}
$$

両辺を $r$ で割ると，求める解は次式となります。

$$
\finalanswer{u(t, r) = \frac{r_0^2}{2cr}\left\{\exp\!\left(-\frac{(r - ct)^2}{2r_0^2}\right) - \exp\!\left(-\frac{(r + ct)^2}{2r_0^2}\right)\right\}}
$$

### (4)

設問 (3) で得た解の表式は全実数 $t \in (-\infty, \infty)$ にわたって波動方程式を満たします。これをフーリエ変換の定義式に代入します。

$$
U(\omega, r) = \frac{r_0^2}{2cr}\left\{\int_{-\infty}^{\infty} \exp\!\left(-\frac{(ct - r)^2}{2r_0^2}\right)e^{i\omega t}\,\mathrm{d}t - \int_{-\infty}^{\infty} \exp\!\left(-\frac{(ct + r)^2}{2r_0^2}\right)e^{i\omega t}\,\mathrm{d}t\right\}
$$

まず第1の積分 $I_+(r)$ について $\xi = ct - r$ と置換します。$t = \dfrac{\xi + r}{c}$，$\mathrm{d}t = \dfrac{\mathrm{d}\xi}{c}$ です。

$$
\begin{aligned}
I_+(r) &= \frac{1}{c}e^{i\omega r/c}\int_{-\infty}^{\infty} \exp\!\left(-\frac{\xi^2}{2r_0^2} + i\frac{\omega}{c}\xi\right)\mathrm{d}\xi \\
&= \frac{1}{c}e^{i\omega r/c}\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right)\int_{-\infty}^{\infty} \exp\!\left\{-\frac{1}{2r_0^2}\left(\xi - i\frac{r_0^2\omega}{c}\right)^2\right\}\mathrm{d}\xi \\
&= \frac{\sqrt{2\pi}\,r_0}{c}e^{i\omega r/c}\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right)
\end{aligned}
$$

第2の積分 $I_-(r)$ は $r$ を $-r$ に置き換えたものなので，次式になります。

$$
I_-(r) = \frac{\sqrt{2\pi}\,r_0}{c}e^{-i\omega r/c}\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right)
$$

両者の差をとり，$e^{i\omega r/c} - e^{-i\omega r/c} = 2i\sin\!\left(\dfrac{\omega r}{c}\right)$ を用います。

$$
\begin{aligned}
U(\omega, r) &= \frac{r_0^2}{2cr}\cdot\frac{\sqrt{2\pi}\,r_0}{c}\bigl(e^{i\omega r/c} - e^{-i\omega r/c}\bigr)\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right) \\
&= i\frac{\sqrt{2\pi}\,r_0^3}{c^2 r}\sin\!\left(\frac{\omega r}{c}\right)\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right)
\end{aligned}
$$

したがって，フーリエ変換 $U(\omega, r)$ は次式となります。

$$
\finalanswer{U(\omega, r) = i\frac{\sqrt{2\pi}\,r_0^3}{c^2 r}\sin\!\left(\frac{\omega r}{c}\right)\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right)}
$$

### (5)

設問 (4) の $U(\omega, r)$ で $r \to 0$ の極限をとります。$\lim_{r \to 0}\dfrac{1}{r}\sin\!\left(\dfrac{\omega r}{c}\right) = \dfrac{\omega}{c}$ を用います。

$$
\begin{aligned}
g(\omega) &= \lim_{r \to 0} U(\omega, r) \\
&= i\frac{\sqrt{2\pi}\,r_0^3}{c^3}\,\omega\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right)
\end{aligned}
$$

$u(t, 0)$ は $t$ の実奇関数なので，$g(\omega)$ は純虚数になります。虚部 $h(\omega) = \dfrac{g(\omega)}{i}$ を $\omega$ で微分します。

$$
\frac{\mathrm{d}h}{\mathrm{d}\omega} = \frac{\sqrt{2\pi}\,r_0^3}{c^3}\left(1 - \frac{r_0^2\omega^2}{c^2}\right)\exp\!\left(-\frac{r_0^2\omega^2}{2c^2}\right)
$$

$\dfrac{\mathrm{d}h}{\mathrm{d}\omega} = 0$ より $\omega = \pm\dfrac{c}{r_0}$ です。増減を調べると，虚部 $h(\omega)$ は $\omega = \dfrac{c}{r_0}$ で最大値，$\omega = -\dfrac{c}{r_0}$ で最小値をとります。また振幅 $|g(\omega)| = |h(\omega)|$ は $\omega = \pm\dfrac{c}{r_0}$ で最大値をとります。

したがって，虚部 $\operatorname{Im} g(\omega)$ が最大となる $\omega$ は次式となります。なお絶対値 $|g(\omega)|$ が最大となるのは $\omega = \pm\dfrac{c}{r_0}$ です。

$$
\finalanswer{\omega = \frac{c}{r_0}}
$$
