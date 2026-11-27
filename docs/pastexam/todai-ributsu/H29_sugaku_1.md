---
title: 東大理物 平成29年度 数学 第1問：ラプラス変換とたたみ込み積分方程式
tags:
  - 院試過去問
  - 東大理物
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成29年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成29年度 数学 第1問：ラプラス変換とたたみ込み積分方程式

## 問題

実数 $t \ge 0$ において定義されている関数 $f(t)$ に対するラプラス変換 $L[f(t)]$ は，複素数 $s$ を用いて積分

$$
L[f(t)] = F(s) = \int_0^{\infty} e^{-st} f(t)\,dt
$$

で定義される。また，$t \ge 0$ における $F(s)$ の逆ラプラス変換 $L^{-1}[F(s)] = f(t)$ は，$s$ に関する複素積分を用いて

$$
L^{-1}[F(s)] = f(t) = \frac{1}{2\pi i}\int_{\gamma - i\infty}^{\gamma + i\infty} e^{st} F(s)\,ds \tag{1}
$$

と表される。ここで式 (1) の積分路は，実部が $\gamma$ で虚軸に平行な直線であり，$\gamma$ は $F(s)$ のすべての特異点が積分路の左側になるように選ぶ。以下の設問に答えよ。

(1) 実数 $t \ge 0$ において定義されている以下の (i)〜(iii) の関数 $f(t)$ のラプラス変換 $F(s)$ を求めよ。また，ラプラス変換の積分が収束するための $s$ に対する条件を各々示せ。

(i) $f(t) = t$

(ii) $f(t) = \sin\omega t$（$\omega$ は正の実数）

(iii) $f(t) = \sqrt{t}\ (\ge 0)$

(2) ラプラス変換を用いて次の積分方程式の解 $f(t)$ を求める。

$$
f(t) = \sin t + \int_0^t \sin(t - t') f(t')\,dt' \qquad (t \ge 0) \tag{2}
$$

(i) 一般に関数 $f_1(t)$ と $f_2(t)$ のたたみ込みを $(f_1 * f_2)(t) = \displaystyle\int_0^t f_1(t - t') f_2(t')\,dt'$ と定義する。$f_1(t)$ と $f_2(t)$ の各々のラプラス変換を $F_1(s),\ F_2(s)$ とするとき，$(f_1 * f_2)(t)$ のラプラス変換は

$$
L[(f_1 * f_2)(t)] = F_1(s) F_2(s) \tag{3}
$$

となることを示せ。

(ii) 式 (3) を用いて式 (2) の両辺をラプラス変換し，$f(t)$ のラプラス変換 $F(s)$ を求めよ。

(iii) $f(t)$ を求めよ。

(3) $F(s) = \dfrac{s}{(s - 1)^2}$ の逆ラプラス変換 $f(t) = L^{-1}[F(s)]$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成29年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ラプラス変換すると，たたみ込みは変換した関数の積になります。そのため，たたみ込みを含む積分方程式 (2) は，変換した関数 $F(s)$ についての1次方程式になり，$F(s)$ を求めることができます。

$F(s)$ から $f(t)$ に戻す逆変換は，式 (1) の複素積分です。$t>0$ では $e^{st}$ が小さくなる左側の大きな半円で経路を閉じることができるので，逆変換は $e^{st}F(s)$ の極での留数の和として求まります。
</div>

### (1)
(i) $f(t) = t$ のとき，部分積分を用います。$\operatorname{Re} s > 0$ のとき $t \to \infty$ で $t e^{-st} \to 0,\ e^{-st} \to 0$ となり積分が収束します。$\operatorname{Re}s\le0$ では積分は収束しません。

$$
\begin{aligned}
F(s) &= \int_0^{\infty} t e^{-st}\,\mathrm{d}t \\
&= \left[-\frac{t}{s}e^{-st}\right]_0^{\infty} + \frac{1}{s}\int_0^{\infty} e^{-st}\,\mathrm{d}t \\
&= \frac{1}{s}\left[-\frac{1}{s}e^{-st}\right]_0^{\infty} \\
&= \frac{1}{s^2}
\end{aligned}
$$

したがって，

$$
\finalanswer{F(s) = \frac{1}{s^2} \qquad (\operatorname{Re} s > 0)}
$$

(ii) $f(t) = \sin\omega t = \dfrac{e^{i\omega t} - e^{-i\omega t}}{2i}$ とおきます。$\operatorname{Re} s > 0$ のとき $\operatorname{Re}(s \mp i\omega) = \operatorname{Re} s > 0$ なので積分が収束します。$\operatorname{Re}s\le0$ では積分は収束しません。

$$
\begin{aligned}
F(s) &= \frac{1}{2i}\int_0^{\infty} \left(e^{-(s - i\omega)t} - e^{-(s + i\omega)t}\right)\mathrm{d}t \\
&= \frac{1}{2i}\left(\frac{1}{s - i\omega} - \frac{1}{s + i\omega}\right) \\
&= \frac{1}{2i}\cdot\frac{2i\omega}{s^2 + \omega^2} \\
&= \frac{\omega}{s^2 + \omega^2}
\end{aligned}
$$

したがって，

$$
\finalanswer{F(s) = \frac{\omega}{s^2 + \omega^2} \qquad (\operatorname{Re} s > 0)}
$$

(iii) $f(t) = \sqrt{t}$ のとき，同様に収束条件は $\operatorname{Re} s > 0$ です。まず実数 $s>0$ に対して $st=u^2$ とおきます。$t=u^2/s$，$\mathrm{d}t=2u\,\mathrm{d}u/s$ なので，ガウス積分 $\displaystyle\int_0^{\infty} e^{-u^2}\,\mathrm{d}u = \dfrac{\sqrt{\pi}}{2}$ と部分積分を用います。

$$
\begin{aligned}
F(s) &= \int_0^{\infty} \sqrt{t}\,e^{-st}\,\mathrm{d}t \\
&= \frac{2}{s^{3/2}}\int_0^{\infty} u^2 e^{-u^2}\,\mathrm{d}u \\
&= \frac{2}{s^{3/2}}\left(\left[-\frac{u}{2}e^{-u^2}\right]_0^{\infty} + \frac{1}{2}\int_0^{\infty} e^{-u^2}\,\mathrm{d}u\right) \\
&= \frac{1}{s^{3/2}}\cdot\frac{\sqrt{\pi}}{2} \\
&= \frac{\sqrt{\pi}}{2 s^{3/2}}
\end{aligned}
$$

解析接続により $\operatorname{Re} s > 0$ の複素数 $s$ に対しても同じ表式が成り立ちます。$s^{3/2}$ は実数 $s>0$ で正となる主値分枝を使います。したがって，

$$
\finalanswer{F(s) = \frac{\sqrt{\pi}}{2 s^{3/2}} \qquad (\operatorname{Re} s > 0)}
$$

### (2)
(i) たたみ込みのラプラス変換を書き，領域 $0 \le t' \le t < \infty$ における二重積分の順序を交換します。

$$
\begin{aligned}
L[(f_1 * f_2)(t)]
&= \int_0^{\infty} e^{-st}\left(\int_0^t f_1(t - t') f_2(t')\,\mathrm{d}t'\right)\mathrm{d}t \\
&= \int_0^{\infty} f_2(t')\left(\int_{t'}^{\infty} e^{-st} f_1(t - t')\,\mathrm{d}t\right)\mathrm{d}t'
\end{aligned}
$$

内側の積分で $u=t-t'$ とおきます。$\mathrm{d}t=\mathrm{d}u$ であり，$t=t'$ は $u=0$ に対応します。

$$
\begin{aligned}
L[(f_1 * f_2)(t)]
&= \int_0^{\infty} f_2(t') e^{-st'}\left(\int_0^{\infty} e^{-su} f_1(u)\,\mathrm{d}u\right)\mathrm{d}t' \\
&= \left(\int_0^{\infty} e^{-su} f_1(u)\,\mathrm{d}u\right)\left(\int_0^{\infty} e^{-st'} f_2(t')\,\mathrm{d}t'\right) \\
&= F_1(s) F_2(s)
\end{aligned}
$$

よって式 (3) が成り立ちます。

(ii) 式 (2) の右辺第2項は $\sin t$ と $f(t)$ のたたみ込みです。問1(ii) に $\omega=1$ を代入すると $L[\sin t] = \dfrac{1}{s^2 + 1}$ なので，式 (2) の両辺をラプラス変換して式 (3) を用います。

$$
\begin{aligned}
F(s) &= \frac{1}{s^2 + 1} + \frac{1}{s^2 + 1} F(s) \\
\left(1 - \frac{1}{s^2 + 1}\right) F(s) &= \frac{1}{s^2 + 1} \\
\frac{s^2}{s^2 + 1} F(s) &= \frac{1}{s^2 + 1} \\
F(s) &= \frac{1}{s^2}
\end{aligned}
$$

したがって，

$$
\finalanswer{F(s) = \frac{1}{s^2}}
$$

(iii) 問1(i) の結果 $L[t] = \dfrac{1}{s^2}$ とラプラス変換の一意性より，$f(t) = t$ です。したがって，

$$
\finalanswer{f(t) = t}
$$

### (3)
$F(s) = \dfrac{s}{(s - 1)^2}$ の特異点は $s = 1$ の2位の極のみなので，$\gamma > 1$ と選びます。

$t > 0$ のとき，直線 $s = \gamma + iy\ (-R \le y \le R)$ とその左側の半径 $R$ の半円弧 $C_R$ からなる反時計回りの閉経路を考えます。半円弧 $C_R$ 上では $\operatorname{Re} s = \gamma + R\cos\theta \le \gamma$ かつ $|F(s)| = \mathcal{O}(R^{-1})$ なので，ジョルダンの補題より $R \to \infty$ で $C_R$ 上の積分は $0$ に収束します。

よって留数定理により，$f(t)$ は $s = 1$ における $e^{st} F(s)$ の留数に等しくなります。

$$
\begin{aligned}
f(t) &= \operatorname{Res}_{s = 1}\left[\frac{s e^{st}}{(s - 1)^2}\right] \\
&= \lim_{s \to 1}\frac{\mathrm{d}}{\mathrm{d}s}\left(s e^{st}\right) \\
&= \lim_{s \to 1}\left(e^{st} + st e^{st}\right) \\
&= (1 + t)e^t
\end{aligned}
$$

$t=0$ では右側極限から $f(0)=1$ です。したがって，

$$
\finalanswer{f(t) = (1 + t)e^t}
$$

<aside class="rigor-note" markdown>
問2の解を元の積分方程式へ代入すると，

$$
\begin{aligned}
\sin t+\int_0^t\sin(t-t')t'\,\mathrm{d}t'
&=\sin t+\left[t'\cos(t-t')\right]_0^t-\int_0^t\cos(t-t')\,\mathrm{d}t'\\
&=\sin t+t-\sin t\\
&=t
\end{aligned}
$$

となり，等式が成り立ちます。
</aside>
