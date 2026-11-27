---
title: 東大理物 平成13年度 数学 第2問：円形膜の波動方程式とベッセル関数
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 特殊関数・変分法
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成13年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成13年度 数学 第2問：円形膜の波動方程式とベッセル関数

## 問題

原点を中心とし，周辺を固定した半径 $a$ の薄い円形膜の振動を考えよう。平衡位置からの変位を $u$ とする。極座標を用い $u = u(r, \theta, t)$ とする時，円形膜の振動は波動方程式

$$
\frac{\partial^2 u}{\partial t^2} = \frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2}
$$

に従う（簡単のため方程式に現れる係数を $1$ とおいた）。以下の設問に答えよ。
{: .problem-lead }

(1) $n$ 次のベッセル関数 $J_n(x)$ は微分方程式

$$
\frac{\mathrm{d}^2 J_n(x)}{\mathrm{d}x^2} + \frac{1}{x}\frac{\mathrm{d}J_n(x)}{\mathrm{d}x} + \left(1 - \frac{n^2}{x^2}\right)J_n(x) = 0
$$

を満たす。$J_n(x)$ の $j$ 番目の零点を $\xi_{nj}$ とする時，次の直交関係

$$
\int_0^1 x J_n(\xi_{nj} x) J_n(\xi_{n\ell} x)\,\mathrm{d}x = 0, \qquad j \neq \ell
$$

が成り立つことを証明せよ。

(2) 境界条件 $u(a, \theta, t) = 0$ と初期条件 $u(r, \theta, 0) = F(r, \theta)$，$\left[\dfrac{\partial u(r, \theta, t)}{\partial t}\right]_{t=0} = 0$ を満たす波動方程式の解を変数分離の方法で求めよ。(1) で議論した直交関係を用いてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成13年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ベッセルの微分方程式に $x$ を掛けて自己随伴形 $\dfrac{\mathrm{d}}{\mathrm{d}x}\left(x y'\right) + \left(\xi^2 x - \dfrac{n^2}{x}\right)y = 0$ に直すと，異なる零点 $\xi_{nj}, \xi_{n\ell}$ に対応する2つの解の差から境界項だけが残る恒等式が得られ，直交関係が導かれます。

円形膜の波動方程式では，解を $u(r, \theta, t) = R(r)\Theta(\theta)T(t)$ と積の形に置くことで，角度方向は $2\pi$ 周期の三角関数，時間方向は初期速度 $0$ の余弦関数，動径方向はベッセル方程式へそれぞれ分離できます。原点での有界性と周辺 $r = a$ での固定条件から固有モードが定まり，初期変位 $F(r, \theta)$ との内積によって展開係数が決まります。
</div>

### (1)

$y_j(x) = J_n(\xi_{nj} x)$ および $y_\ell(x) = J_n(\xi_{n\ell} x)$ とおきます。ベッセルの微分方程式の変数を $z = \xi_{nj} x$ に変換すると，$\dfrac{\mathrm{d}}{\mathrm{d}z} = \dfrac{1}{\xi_{nj}}\dfrac{\mathrm{d}}{\mathrm{d}x}$ より次が成り立ちます。

$$
\begin{aligned}
\frac{1}{\xi_{nj}^2}\frac{\mathrm{d}^2 y_j}{\mathrm{d}x^2} + \frac{1}{\xi_{nj}^2 x}\frac{\mathrm{d}y_j}{\mathrm{d}x} + \left(1 - \frac{n^2}{\xi_{nj}^2 x^2}\right)y_j &= 0 \\
\frac{\mathrm{d}^2 y_j}{\mathrm{d}x^2} + \frac{1}{x}\frac{\mathrm{d}y_j}{\mathrm{d}x} + \left(\xi_{nj}^2 - \frac{n^2}{x^2}\right)y_j &= 0
\end{aligned}
$$

両辺に $x$ を掛けて，最初の2項を1つの微分にまとめます。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y_j}{\mathrm{d}x}\right) + \left(\xi_{nj}^2 x - \frac{n^2}{x}\right)y_j = 0
$$

$y_\ell(x)$ についても同じ方程式が成り立ちます。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y_\ell}{\mathrm{d}x}\right) + \left(\xi_{n\ell}^2 x - \frac{n^2}{x}\right)y_\ell = 0
$$

1本目の式に $y_\ell$ を掛け，2本目の式に $y_j$ を掛けて辺々を引きます。

$$
\begin{aligned}
(\xi_{nj}^2 - \xi_{n\ell}^2)x y_j y_\ell &= y_j\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y_\ell}{\mathrm{d}x}\right) - y_\ell\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y_j}{\mathrm{d}x}\right) \\
&= \frac{\mathrm{d}}{\mathrm{d}x}\left[x\left(y_j\frac{\mathrm{d}y_\ell}{\mathrm{d}x} - y_\ell\frac{\mathrm{d}y_j}{\mathrm{d}x}\right)\right]
\end{aligned}
$$

両辺を $x = 0$ から $x = 1$ まで積分します。

$$
(\xi_{nj}^2 - \xi_{n\ell}^2)\int_0^1 x y_j(x) y_\ell(x)\,\mathrm{d}x = \left[x\left(y_j(x)\frac{\mathrm{d}y_\ell(x)}{\mathrm{d}x} - y_\ell(x)\frac{\mathrm{d}y_j(x)}{\mathrm{d}x}\right)\right]_0^1
$$

右辺の境界値を調べます。$x = 1$ では $\xi_{nj}, \xi_{n\ell}$ が $J_n$ の零点なので $y_j(1) = 0$ かつ $y_\ell(1) = 0$ です。また $x = 0$ では非負整数 $n$ に対して $J_n$ と $J_n'$ が有限なので，$x$ を掛けた項は $x \to 0$ で $0$ になります。よって右辺は $0$ です。

$j \neq \ell$ のとき $\xi_{nj} \neq \xi_{n\ell}$ かつ $\xi_{nj}, \xi_{n\ell} > 0$ なので $\xi_{nj}^2 - \xi_{n\ell}^2 \neq 0$ です。両辺を $\xi_{nj}^2 - \xi_{n\ell}^2$ で割ると，直交関係が得られます。

$$
\int_0^1 x J_n(\xi_{nj} x) J_n(\xi_{n\ell} x)\,\mathrm{d}x = 0 \qquad (j \neq \ell)
$$

### (2)

変数分離形 $u(r, \theta, t) = R(r)\Theta(\theta)T(t)$ を波動方程式に代入し，両辺を $R\Theta T$ で割ります。

$$
\frac{T''(t)}{T(t)} = \frac{R''(r)}{R(r)} + \frac{1}{r}\frac{R'(r)}{R(r)} + \frac{1}{r^2}\frac{\Theta''(\theta)}{\Theta(\theta)}
$$

左辺は $t$ のみ，右辺は $r, \theta$ のみの関数なので，両辺は定数になります。振動解を与える分離定数を $-\omega^2$（$\omega > 0$）とおきます。

まず時間部分の方程式は $T''(t) + \omega^2 T(t) = 0$ です。初期条件 $T'(0) = 0$ より，定数倍を除いて次になります。

$$
T(t) = \cos(\omega t)
$$

空間部分に $r^2$ を掛けて整理します。

$$
r^2\frac{R''(r)}{R(r)} + r\frac{R'(r)}{R(r)} + \omega^2 r^2 = -\frac{\Theta''(\theta)}{\Theta(\theta)}
$$

左辺は $r$ のみ，右辺は $\theta$ のみの関数なので，両辺を定数 $\lambda$ とおきます。$\Theta(\theta)$ は $2\pi$ の周期をもつ一価関数なので，$\Theta''(\theta) + \lambda\Theta(\theta) = 0$ が恒等的に $0$ でない周期解をもつためには $\lambda = n^2$（$n = 0, 1, 2, \dots$）が必要です。

- $n = 0$ のとき：定数関数 $\Theta_0(\theta) = 1$。
- $n \ge 1$ のとき：$\Theta_n(\theta) = A_n\cos(n\theta) + B_n\sin(n\theta)$。

次に動径部分の方程式を書きます。

$$
\frac{\mathrm{d}^2 R}{\mathrm{d}r^2} + \frac{1}{r}\frac{\mathrm{d}R}{\mathrm{d}r} + \left(\omega^2 - \frac{n^2}{r^2}\right)R = 0
$$

$\tilde{r} = \omega r$ と置換すると $n$ 次のベッセルの微分方程式になります。$r = 0$ で有限となる解は第1種ベッセル関数 $J_n(\omega r)$ だけです。境界条件 $u(a, \theta, t) = 0$ より $J_n(\omega a) = 0$ となるため，$\omega a$ は $J_n$ の正の零点 $\xi_{nj}$（$j = 1, 2, \dots$）に一致します。したがって，角振動数は $\omega_{nj} = \dfrac{\xi_{nj}}{a}$ です。

以上を重ね合わせた一般解は次の形になります。

$$
u(r, \theta, t) = \sum_{j=1}^{\infty} A_{0j} J_0\left(\frac{\xi_{0j} r}{a}\right)\cos\left(\frac{\xi_{0j} t}{a}\right) + \sum_{n=1}^{\infty}\sum_{j=1}^{\infty} \bigl[A_{nj}\cos(n\theta) + B_{nj}\sin(n\theta)\bigr] J_n\left(\frac{\xi_{nj} r}{a}\right)\cos\left(\frac{\xi_{nj} t}{a}\right)
$$

次に，展開係数 $A_{0j}, A_{nj}, B_{nj}$ を決めるため，規格化積分 $I_{nj} = \int_0^1 x \bigl[J_n(\xi_{nj} x)\bigr]^2\,\mathrm{d}x$ を求めます。(1) の自己随伴方程式の両辺に $2x y_j'(x)$ を掛けます。

$$
\begin{aligned}
2x y_j'\frac{\mathrm{d}}{\mathrm{d}x}(x y_j') + 2\left(\xi_{nj}^2 x^2 - n^2\right)y_j y_j' &= 0 \\
\frac{\mathrm{d}}{\mathrm{d}x}\left[(x y_j')^2 + \left(\xi_{nj}^2 x^2 - n^2\right)y_j^2\right] - 2\xi_{nj}^2 x y_j^2 &= 0
\end{aligned}
$$

両辺を $x = 0$ から $x = 1$ まで積分します。

$$
2\xi_{nj}^2 \int_0^1 x \bigl[y_j(x)\bigr]^2\,\mathrm{d}x = \left[\bigl(x y_j'(x)\bigr)^2 + \left(\xi_{nj}^2 x^2 - n^2\right)\bigl(y_j(x)\bigr)^2\right]_0^1
$$

$x = 1$ では $J_n(\xi_{nj}) = 0$ より $y_j(1) = 0$ であり，$y_j'(1) = \xi_{nj} J_n'(\xi_{nj})$ です。また $x = 0$ では $x y_j'(x) \to 0$ であり，$n = 0$ のとき $n^2 = 0$，$n \ge 1$ のとき $J_n(0) = 0$ なので下端の寄与は $0$ です。したがって次が得られます。

$$
\begin{aligned}
2\xi_{nj}^2 \int_0^1 x \bigl[J_n(\xi_{nj} x)\bigr]^2\,\mathrm{d}x &= \xi_{nj}^2 \bigl[J_n'(\xi_{nj})\bigr]^2 \\
\int_0^1 x \bigl[J_n(\xi_{nj} x)\bigr]^2\,\mathrm{d}x &= \frac{1}{2}\bigl[J_n'(\xi_{nj})\bigr]^2
\end{aligned}
$$

$r = ax$ と置換すると，(1) の直交関係と合わせて次が成り立ちます。

$$
\int_0^a r J_n\left(\frac{\xi_{nj} r}{a}\right) J_n\left(\frac{\xi_{n\ell} r}{a}\right)\mathrm{d}r = \frac{a^2}{2}\bigl[J_n'(\xi_{nj})\bigr]^2 \delta_{j\ell}
$$

初期条件 $u(r, \theta, 0) = F(r, \theta)$ に上式を当てはめます。

$$
F(r, \theta) = \sum_{j=1}^{\infty} A_{0j} J_0\left(\frac{\xi_{0j} r}{a}\right) + \sum_{n=1}^{\infty}\sum_{j=1}^{\infty} \bigl[A_{nj}\cos(n\theta) + B_{nj}\sin(n\theta)\bigr] J_n\left(\frac{\xi_{nj} r}{a}\right)
$$

両辺に $r J_0\left(\dfrac{\xi_{0j} r}{a}\right)$ を掛けて $r \in [0, a]$，$\theta \in [0, 2\pi]$ で積分すると，$\int_0^{2\pi}\mathrm{d}\theta = 2\pi$ より次になります。

$$
\int_0^{2\pi}\mathrm{d}\theta \int_0^a r F(r, \theta) J_0\left(\frac{\xi_{0j} r}{a}\right)\mathrm{d}r = 2\pi \cdot \frac{a^2}{2}\bigl[J_0'(\xi_{0j})\bigr]^2 A_{0j}
$$

同様に $n \ge 1$ について $r J_n\left(\dfrac{\xi_{nj} r}{a}\right)\cos(n\theta)$ および $r J_n\left(\dfrac{\xi_{nj} r}{a}\right)\sin(n\theta)$ を掛けて積分すると，$\int_0^{2\pi}\cos^2(n\theta)\,\mathrm{d}\theta = \pi$，$\int_0^{2\pi}\sin^2(n\theta)\,\mathrm{d}\theta = \pi$ より次になります。

$$
\begin{aligned}
\int_0^{2\pi}\mathrm{d}\theta \int_0^a r F(r, \theta) J_n\left(\frac{\xi_{nj} r}{a}\right)\cos(n\theta)\,\mathrm{d}r &= \pi \cdot \frac{a^2}{2}\bigl[J_n'(\xi_{nj})\bigr]^2 A_{nj} \\
\int_0^{2\pi}\mathrm{d}\theta \int_0^a r F(r, \theta) J_n\left(\frac{\xi_{nj} r}{a}\right)\sin(n\theta)\,\mathrm{d}r &= \pi \cdot \frac{a^2}{2}\bigl[J_n'(\xi_{nj})\bigr]^2 B_{nj}
\end{aligned}
$$

以上より，求める解は次の通りです。

$$
\finalanswer{u(r, \theta, t) = \sum_{j=1}^{\infty} A_{0j} J_0\left(\frac{\xi_{0j} r}{a}\right)\cos\left(\frac{\xi_{0j} t}{a}\right) + \sum_{n=1}^{\infty}\sum_{j=1}^{\infty} \bigl[A_{nj}\cos(n\theta) + B_{nj}\sin(n\theta)\bigr] J_n\left(\frac{\xi_{nj} r}{a}\right)\cos\left(\frac{\xi_{nj} t}{a}\right)}
$$

ただし各展開係数は次で与えられます。

$$
\finalanswer{A_{0j} = \frac{1}{\pi a^2 \bigl[J_0'(\xi_{0j})\bigr]^2}\int_0^{2\pi}\mathrm{d}\theta \int_0^a r F(r, \theta) J_0\left(\frac{\xi_{0j} r}{a}\right)\mathrm{d}r}
$$

$$
\finalanswer{A_{nj} = \frac{2}{\pi a^2 \bigl[J_n'(\xi_{nj})\bigr]^2}\int_0^{2\pi}\mathrm{d}\theta \int_0^a r F(r, \theta) J_n\left(\frac{\xi_{nj} r}{a}\right)\cos(n\theta)\,\mathrm{d}r \qquad (n \ge 1)}
$$

$$
\finalanswer{B_{nj} = \frac{2}{\pi a^2 \bigl[J_n'(\xi_{nj})\bigr]^2}\int_0^{2\pi}\mathrm{d}\theta \int_0^a r F(r, \theta) J_n\left(\frac{\xi_{nj} r}{a}\right)\sin(n\theta)\,\mathrm{d}r \qquad (n \ge 1)}
$$

<aside class="rigor-note" markdown>
分離定数に $\omega^2 \le 0$ をとる場合を確かめます。$\omega = 0$ のときは動径方程式が $r^2 R'' + r R' - n^2 R = 0$ となり，$r = 0$ で有限な解は $R(r) \propto r^n$ なので，境界条件 $R(a) = 0$ を満たすのは恒等的に $0$ の解だけです。また $\omega^2 < 0$ のときは $R(r)$ が変形ベッセル関数 $I_n(|\omega|r)$ となり，$r > 0$ で正の零点をもたないため $R(a) = 0$ を満たす恒等的に $0$ でない解は存在しません。なお，漸化式 $J_n'(x) = \dfrac{n}{x}J_n(x) - J_{n+1}(x)$ に $x = \xi_{nj}$ を代入すると $J_n'(\xi_{nj}) = -J_{n+1}(\xi_{nj})$ となるため，展開係数の分母は $\bigl[J_{n+1}(\xi_{nj})\bigr]^2$ と書くこともできます。
</aside>
