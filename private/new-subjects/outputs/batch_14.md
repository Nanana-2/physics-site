===== FILE: 12special_functions/01/01_010.md =====
---
tags:
  - 基本
---

# ガンマ関数の定義と性質

## 問題
ガンマ関数 $\Gamma(z)$ は $z>0$ に対して次のように定義される。
$$
\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt
$$
以下の問いに答えよ。

(1) $\Gamma(1)$ の値を求めよ。

(2) 部分積分を用いて，漸化式 $\Gamma(z+1)=z\Gamma(z)$ が成り立つことを示せ。

(3) 自然数 $n$ に対して，$\Gamma(n+1)=n!$ が成り立つことを示せ。

---

## 解答・解説

### (1)
定義式の被積分関数に $z=1$ を代入して定積分を計算します。

$$
\begin{aligned}
\Gamma(1) &= \int_0^\infty t^{1-1} e^{-t} \, dt \\
&= \int_0^\infty e^{-t} \, dt \\
&= \left[ -e^{-t} \right]_0^\infty \\
&= 0 - (-1) \\
&= \finalanswer{1}
\end{aligned}
$$

したがって，値は 1 となります。

### (2)
ガンマ関数の定義において $z$ を $z+1$ に置き換えると，次の積分が得られます。

$$
\Gamma(z+1) = \int_0^\infty t^z e^{-t} \, dt
$$

ここで，$u=t^z$，$v' = e^{-t}$ とみなして部分積分を適用します。$z>0$ であるため，$t \to 0$ において $t^z \to 0$ となり，$t \to \infty$ においては指数関数の減衰が多項式の増加より速いため $t^z e^{-t} \to 0$ となります。

$$
\begin{aligned}
\Gamma(z+1) &= \left[ -t^z e^{-t} \right]_0^\infty + \int_0^\infty z t^{z-1} e^{-t} \, dt \\
&= 0 + z \int_0^\infty t^{z-1} e^{-t} \, dt \\
&= \finalanswer{z\Gamma(z)}
\end{aligned}
$$

よって，漸化式 $\Gamma(z+1)=z\Gamma(z)$ が成り立ちます。

### (3)
(2) で求めた漸化式を繰り返し適用します。自然数 $n$ に対して漸化式を次々に用いると，積の形に展開できます。

$$
\begin{aligned}
\Gamma(n+1) &= n \Gamma(n) \\
&= n (n-1) \Gamma(n-1) \\
&= n (n-1) \cdots 2 \cdot 1 \cdot \Gamma(1)
\end{aligned}
$$

ここで (1) で求めた $\Gamma(1)=1$ を代入します。

$$
\begin{aligned}
\Gamma(n+1) &= n! \cdot 1 \\
&= \finalanswer{n!}
\end{aligned}
$$

この結果から，ガンマ関数は階乗の概念を実数や複素数へと拡張した関数とみなせます。

===== FILE: 12special_functions/01/01_020.md =====
---
tags:
  - 基本
---

# $\Gamma(1/2)$ とガウス積分

## 問題
ガンマ関数 $\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt$ について，以下の問いに答えよ。

(1) 置換 $t=x^2$ ($x \ge 0$) を行い，$\Gamma(1/2)$ をガウス積分 $I = \int_{-\infty}^\infty e^{-x^2} \, dx$ を用いて表せ。

(2) 重積分 $I^2 = \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-(x^2+y^2)} \, dx dy$ を 2 次元極座標 $(r, \theta)$ に変換して計算し，$I$ の値を求めよ。

(3) $\Gamma(1/2)$ および $\Gamma(3/2)$ の値を求めよ。

---

## 解答・解説

### (1)
ガンマ関数の定義式において $z=1/2$ とおくと，次の積分になります。

$$
\Gamma(1/2) = \int_0^\infty t^{-1/2} e^{-t} \, dt
$$

変数変換 $t=x^2$ を行うと，微分形式は $dt = 2x \, dx$ となり，積分範囲は $0 \le x < \infty$ に移ります。代入して式を整理します。

$$
\begin{aligned}
\Gamma(1/2) &= \int_0^\infty (x^2)^{-1/2} e^{-x^2} \cdot 2x \, dx \\
&= \int_0^\infty \frac{1}{x} e^{-x^2} \cdot 2x \, dx \\
&= 2 \int_0^\infty e^{-x^2} \, dx
\end{aligned}
$$

被積分関数 $e^{-x^2}$ は偶関数であるため，積分範囲を実数全体に対称化できます。

$$
\begin{aligned}
\Gamma(1/2) &= \int_{-\infty}^\infty e^{-x^2} \, dx \\
&= \finalanswer{I}
\end{aligned}
$$

したがって，$\Gamma(1/2)$ はガウス積分 $I$ そのものに等しくなります。

### (2)
重積分を平面全体の極座標 $(r, \theta)$ で表します。変換則は $x = r\cos\theta$，$y = r\sin\theta$ であり，微小面積要素は $dx dy = r \, dr d\theta$ となります。積分範囲は $0 \le r < \infty$，$0 \le \theta \le 2\pi$ です。

$$
\begin{aligned}
I^2 &= \int_0^{2\pi} d\theta \int_0^\infty e^{-r^2} r \, dr \\
&= 2\pi \left[ -\frac{1}{2} e^{-r^2} \right]_0^\infty \\
&= 2\pi \cdot \frac{1}{2} \\
&= \pi
\end{aligned}
$$

被積分関数は常に正であるため，$I>0$ です。平方根をとると，次のようになります。

$$
\finalanswer{I = \sqrt{\pi}}
$$

となります。

### (3)
(1) と (2) の結果を結びつけると，直ちに $\Gamma(1/2)$ が求まります。

$$
\finalanswer{\Gamma(1/2) = \sqrt{\pi}}
$$

続いて，ガンマ関数の漸化式 $\Gamma(z+1)=z\Gamma(z)$ に $z=1/2$ を適用します。

$$
\begin{aligned}
\Gamma(3/2) &= \Gamma(1/2 + 1) \\
&= \frac{1}{2} \Gamma(1/2) \\
&= \finalanswer{\frac{\sqrt{\pi}}{2}}
\end{aligned}
$$

このように，半奇数のガンマ関数はすべて $\sqrt{\pi}$ の有理数倍で表されます。

===== FILE: 12special_functions/01/01_030.md =====
---
tags:
  - 標準
---

# ベータ関数とガンマ関数

## 問題
ベータ関数は $p>0$，$q>0$ に対して次のように定義される。
$$
B(p, q) = \int_0^1 x^{p-1} (1-x)^{q-1} \, dx
$$
以下の問いに答えよ。

(1) 置換 $x = \sin^2\theta$ ($0 \le \theta \le \pi/2$) を行い，$B(p, q)$ を三角関数の定積分として表せ。

(2) 置換 $t=u^2$，$s=v^2$ によって得られるガンマ関数の表示
$$
\Gamma(p) = 2\int_0^\infty u^{2p-1} e^{-u^2} \, du, \quad \Gamma(q) = 2\int_0^\infty v^{2q-1} e^{-v^2} \, dv
$$
の積を極座標 $u=r\cos\theta$，$v=r\sin\theta$ で表すことにより，関係式 $B(p, q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$ を示せ。

(3) (2) の関係式を用いて，定積分 $K = \int_0^{\pi/2} \sin^4\theta \, d\theta$ の値を求めよ。

---

## 解答・解説

### (1)
変数変換 $x = \sin^2\theta$ を行うと，微分形式は $dx = 2\sin\theta\cos\theta \, d\theta$ となります。積分範囲は $x: 0 \to 1$ が $\theta: 0 \to \pi/2$ に対応します。

被積分関数に代入して整理します。

$$
\begin{aligned}
B(p, q) &= \int_0^{\pi/2} (\sin^2\theta)^{p-1} (1-\sin^2\theta)^{q-1} \cdot 2\sin\theta\cos\theta \, d\theta \\
&= \int_0^{\pi/2} \sin^{2p-2}\theta \cos^{2q-2}\theta \cdot 2\sin\theta\cos\theta \, d\theta \\
&= \finalanswer{2 \int_0^{\pi/2} \sin^{2p-1}\theta \cos^{2q-1}\theta \, d\theta}
\end{aligned}
$$

この積分形は三角関数の高次積分の計算で広く利用されます。

### (2)
2 つのガンマ関数の積を第 1 象限における 2 重積分として表します。

<!-- FIGURE solution (2): 第1象限 (u>=0, v>=0) における直交座標系 (u, v) と極座標 (r, theta) の対応。微小面積要素 du dv と r dr dtheta を示す。 -->
平面の第 1 象限における積分を図に示します。

$$
\Gamma(p)\Gamma(q) = 4 \int_0^\infty du \int_0^\infty dv \, u^{2p-1} v^{2q-1} e^{-(u^2+v^2)}
$$

極座標変換 $u=r\cos\theta$，$v=r\sin\theta$ を行うと，面積要素は $du dv = r \, dr d\theta$ となり，積分領域は $0 \le r < \infty$，$0 \le \theta \le \pi/2$ となります。

$$
\begin{aligned}
\Gamma(p)\Gamma(q) &= 4 \int_0^{\pi/2} d\theta \int_0^\infty dr \, r (r\cos\theta)^{2p-1} (r\sin\theta)^{2q-1} e^{-r^2} \\
&= 4 \int_0^{\pi/2} \cos^{2p-1}\theta \sin^{2q-1}\theta \, d\theta \int_0^\infty r^{2(p+q)-1} e^{-r^2} \, dr
\end{aligned}
$$

ここで，動径積分と角度積分をそれぞれ独立に評価します。動径部分は定義より $\frac{1}{2}\Gamma(p+q)$ であり，角度部分は (1) より $\frac{1}{2}B(p, q)$ です。

$$
\begin{aligned}
\Gamma(p)\Gamma(q) &= 4 \left( \frac{1}{2} B(p, q) \right) \left( \frac{1}{2} \Gamma(p+q) \right) \\
&= B(p, q) \Gamma(p+q)
\end{aligned}
$$

両辺を $\Gamma(p+q)$ で割ると，求める関係式が得られます。

$$
\finalanswer{B(p, q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}}
$$

となります。

### (3)
求める積分 $K = \int_0^{\pi/2} \sin^4\theta \, d\theta$ を (1) の形式と比較します。$\cos^0\theta$ を補うと次のようになります。

$$
K = \int_0^{\pi/2} \sin^4\theta \cos^0\theta \, d\theta
$$

(1) の被積分関数の指数 $2p-1=4$，$2q-1=0$ と連立させると，$p=5/2$，$q=1/2$ が得られます。したがって，積分はベータ関数を用いて次のように書けます。

$$
K = \frac{1}{2} B(5/2, 1/2) = \frac{\Gamma(5/2)\Gamma(1/2)}{2\Gamma(3)}
$$

各ガンマ関数の値を求めます。$\Gamma(1/2)=\sqrt{\pi}$ および $\Gamma(3)=2!=2$ であり，$\Gamma(5/2)$ は漸化式から計算できます。

$$
\Gamma(5/2) = \frac{3}{2} \cdot \frac{1}{2} \Gamma(1/2) = \frac{3\sqrt{\pi}}{4}
$$

これらを代入して整理します。

$$
\begin{aligned}
K &= \frac{\frac{3\sqrt{\pi}}{4} \cdot \sqrt{\pi}}{2 \cdot 2} \\
&= \finalanswer{\frac{3\pi}{16}}
\end{aligned}
$$

となります。

===== FILE: 12special_functions/01/01_040.md =====
---
tags:
  - 標準
---

# スターリングの公式

## 問題
ガンマ関数の積分表示
$$
\Gamma(N+1) = \int_0^\infty t^N e^{-t} \, dt = \int_0^\infty e^{N\ln t - t} \, dt
$$
を考える。ここで $N$ は十分に大きい正の実数とする。以下の問いに答えよ。

(1) $t = N(1+s)$ と変数変換し，被積分関数を指数の形 $N^N e^{-N} e^{-N f(s)}$ に書き直したときの関数 $f(s)$ を求めよ。

(2) $f(s)$ を $s=0$ のまわりでテイラー展開し，$s^2$ の項まで求めよ。

(3) $N$ が十分に大きいとき，積分の主要な寄与が $s=0$ 近傍から得られることを用いてガウス積分に帰着させ，スターリングの公式
$$
\Gamma(N+1) \approx \sqrt{2\pi N} \left(\frac{N}{e}\right)^N
$$
を導け。

---

## 解答・解説

### (1)
変数変換 $t=N(1+s)$ を行うと，微分形式は $dt = N \, ds$ となり，積分範囲は $-1 \le s < \infty$ となります。

被積分関数の指数部分を計算します。

$$
\begin{aligned}
N \ln t - t &= N \ln(N(1+s)) - N(1+s) \\
&= N \ln N + N \ln(1+s) - N - Ns \\
&= N \ln N - N - N (s - \ln(1+s))
\end{aligned}
$$

したがって，被積分関数は次のように分離できます。

$$
e^{N\ln t - t} = N^N e^{-N} e^{-N(s - \ln(1+s))}
$$

これより，求める関数は次の形になります。

$$
\finalanswer{f(s) = s - \ln(1+s)}
$$

となります。

### (2)
$|s| < 1$ における対数関数のマクローリン展開を用います。

$$
\ln(1+s) = s - \frac{s^2}{2} + \frac{s^3}{3} - \cdots
$$

これを $f(s)$ の表式に代入します。

$$
\begin{aligned}
f(s) &= s - \left( s - \frac{s^2}{2} + O(s^3) \right) \\
&= \finalanswer{\frac{s^2}{2} + O(s^3)}
\end{aligned}
$$

1 次の項が相殺して消えるため，$s=0$ は $f(s)$ の極小点となります。

### (3)
$N$ が非常に大きいとき，$e^{-N f(s)}$ は $f(s)$ が極小値 0 をとる $s=0$ のごく狭い近傍でのみ有限の値を持ち，それ以外の領域では急激に減衰します。

<!-- FIGURE solution (3): 横軸を s，縦軸を被積分関数 exp(-N f(s)) とするグラフ。s=0 に鋭いピークを持ち，N が大きくなると幅が狭くなる様子を示す。原点 O を含む。 -->
ピーク近傍の急激な局在化の様子を図に示します。

展開の 2 次の項までを採用し，積分範囲を実数全体 $(-\infty, \infty)$ に拡張して近似します。

$$
\begin{aligned}
\Gamma(N+1) &= N^{N+1} e^{-N} \int_{-1}^\infty e^{-N f(s)} \, ds \\
&\approx N^{N+1} e^{-N} \int_{-\infty}^\infty e^{-N s^2 / 2} \, ds
\end{aligned}
$$

ガウス積分の公式 $\int_{-\infty}^\infty e^{-a s^2} \, ds = \sqrt{\pi / a}$ において $a = N/2$ と置きます。

$$
\int_{-\infty}^\infty e^{-N s^2 / 2} \, ds = \sqrt{\frac{2\pi}{N}}
$$

これを元の式に代入して整理します。

$$
\begin{aligned}
\Gamma(N+1) &\approx N^{N+1} e^{-N} \sqrt{\frac{2\pi}{N}} \\
&= \finalanswer{\sqrt{2\pi N} \left(\frac{N}{e}\right)^N}
\end{aligned}
$$

この評価は統計力学において巨大な粒子数の階乗を扱う際の基礎となります。

===== FILE: 12special_functions/01/01_050.md =====
---
tags:
  - 標準
---

# $n$ 次元球の体積

## 問題
$n$ 次元ユークリッド空間における半径 $R$ の超球の体積を $V_n(R) = C_n R^n$ とする。以下の問いに答えよ。

(1) 1 次元のガウス積分の値 $\int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt{\pi}$ を用いて，$n$ 重積分
$$
J_n = \int_{-\infty}^\infty \cdots \int_{-\infty}^\infty \exp\left( -\sum_{i=1}^n x_i^2 \right) dx_1 \cdots dx_n
$$
の値を求めよ。

(2) 球殻の体積要素 $dV_n(r) = n C_n r^{n-1} \, dr$ を用いて，$J_n$ を動径 $r$ に関する 1 重積分として表し，これをガンマ関数を用いて表せ。

(3) (1) と (2) の結果を等置することにより，$C_n$ をガンマ関数を用いて表し，体積 $V_n(R)$ を求めよ。

---

## 解答・解説

### (1)
被積分関数は各変数 $x_i$ について独立な指数関数の積に分解できます。

$$
\exp\left( -\sum_{i=1}^n x_i^2 \right) = \prod_{i=1}^n e^{-x_i^2}
$$

したがって，$n$ 重積分は $n$ 個の独立な 1 次元積分の積として計算できます。

$$
\begin{aligned}
J_n &= \prod_{i=1}^n \left( \int_{-\infty}^\infty e^{-x_i^2} \, dx_i \right) \\
&= (\sqrt{\pi})^n \\
&= \finalanswer{\pi^{n/2}}
\end{aligned}
$$

となります。

### (2)
距離 $r = \sqrt{\sum_{i=1}^n x_i^2}$ を導入すると，被積分関数は動径 $r$ のみに依存する関数 $e^{-r^2}$ となります。

<!-- FIGURE solution (2): n 次元球における厚み dr の球殻の概念図。内径 r，外径 r+dr，体積要素 dV_n(r) = n C_n r^(n-1) dr を示す。 -->
動径方向への微小球殻の分割を図に示します。

超球の表面積要素を用いて，体積要素を $dx_1 \cdots dx_n = dV_n(r) = n C_n r^{n-1} \, dr$ と変換し，積分範囲を $0 \le r < \infty$ とします。

$$
J_n = \int_0^\infty e^{-r^2} \cdot n C_n r^{n-1} \, dr
$$

ここで $t = r^2$ と置換すると，$dt = 2r \, dr$ すなわち $r \, dr = dt / 2$ となります。

$$
\begin{aligned}
J_n &= \frac{n C_n}{2} \int_0^\infty e^{-t} (t^{1/2})^{n-2} \, dt \\
&= \frac{n C_n}{2} \int_0^\infty t^{n/2 - 1} e^{-t} \, dt \\
&= \frac{n C_n}{2} \Gamma(n/2)
\end{aligned}
$$

ガンマ関数の基本関係式 $(n/2)\Gamma(n/2) = \Gamma(n/2 + 1)$ を適用します。

$$
J_n = \finalanswer{C_n \Gamma(n/2 + 1)}
$$

となります。

### (3)
(1) と (2) で得られた $J_n$ の表式を等置します。

$$
C_n \Gamma(n/2 + 1) = \pi^{n/2}
$$

両辺を $\Gamma(n/2 + 1)$ で割ることで，係数 $C_n$ が定まります。

$$
C_n = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)}
$$

したがって，半径 $R$ の $n$ 次元球の体積は次式で与えられます。

$$
\finalanswer{V_n(R) = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)} R^n}
$$

$n=2$ では $\Gamma(2)=1$ より $\pi R^2$，$n=3$ では $\Gamma(5/2)=3\sqrt{\pi}/4$ より $\frac{4}{3}\pi R^3$ となり，通常の円の面積や球の体積と一致します。

===== FILE: 12special_functions/02/02_010.md =====
---
tags:
  - 標準
---

# ルジャンドル多項式とロドリゲスの公式

## 問題
ルジャンドル多項式 $P_l(x)$ はロドリゲスの公式
$$
P_l(x) = \frac{1}{2^l l!} \frac{d^l}{dx^l} (x^2 - 1)^l
$$
で定義される（$l$ は非負整数）。以下の問いに答えよ。

(1) $P_0(x)$，$P_1(x)$，$P_2(x)$ を求めよ。

(2) $P_3(x)$ を求めよ。

(3) 多項式の対称性 $P_l(-x) = (-1)^l P_l(x)$ が成り立つことを示せ。

---

## 解答・解説

### (1)
ロドリゲスの公式に $l=0, 1, 2$ を順次代入して計算します。

$l=0$ のとき，微分は 0 階（何もしない操作）となります。

$$
\finalanswer{P_0(x) = 1}
$$

$l=1$ のとき，1 階微分を実行します。

$$
\begin{aligned}
P_1(x) &= \frac{1}{2^1 \cdot 1!} \frac{d}{dx} (x^2 - 1) \\
&= \frac{1}{2} (2x) \\
&= \finalanswer{x}
\end{aligned}
$$

$l=2$ のとき，2 階微分を実行します。

$$
\begin{aligned}
P_2(x) &= \frac{1}{2^2 \cdot 2!} \frac{d^2}{dx^2} (x^2 - 1)^2 \\
&= \frac{1}{8} \frac{d^2}{dx^2} (x^4 - 2x^2 + 1) \\
&= \frac{1}{8} \frac{d}{dx} (4x^3 - 4x) \\
&= \frac{1}{8} (12x^2 - 4) \\
&= \finalanswer{\frac{1}{2} (3x^2 - 1)}
\end{aligned}
$$

となります。

### (2)
$l=3$ のロドリゲスの公式を適用します。

$$
P_3(x) = \frac{1}{2^3 \cdot 3!} \frac{d^3}{dx^3} (x^2 - 1)^3 = \frac{1}{48} \frac{d^3}{dx^3} (x^2 - 1)^3
$$

多項式を展開します。

$$
(x^2 - 1)^3 = x^6 - 3x^4 + 3x^2 - 1
$$

順に微分を実行します。

$$
\begin{aligned}
\frac{d}{dx} (x^6 - 3x^4 + 3x^2 - 1) &= 6x^5 - 12x^3 + 6x \\
\frac{d^2}{dx^2} (x^6 - 3x^4 + 3x^2 - 1) &= 30x^4 - 36x^2 + 6 \\
\frac{d^3}{dx^3} (x^6 - 3x^4 + 3x^2 - 1) &= 120x^3 - 72x \\
&= 24 (5x^3 - 3x)
\end{aligned}
$$

係数を掛けて整理します。

$$
\begin{aligned}
P_3(x) &= \frac{24(5x^3 - 3x)}{48} \\
&= \finalanswer{\frac{1}{2}(5x^3 - 3x)}
\end{aligned}
$$

となります。

### (3)
関数 $u(x) = (x^2 - 1)^l$ を定義します。$u(-x) = ((-x)^2 - 1)^l = (x^2 - 1)^l = u(x)$ であるため，$u(x)$ は偶関数です。

偶関数の高階微分におけるパリティの変換性を考えます。微分演算子について連鎖律を用いると，次が成り立ちます。

$$
\frac{d}{dx} = -\frac{d}{d(-x)}
$$

したがって，$l$ 回の微分演算子を作用させると符号因子 $(-1)^l$ が生じます。

$$
\begin{aligned}
\frac{d^l}{dx^l} u(x) &= \frac{d^l}{d(-x)^l} u(-x) \cdot (-1)^l \\
&= (-1)^l \left[ \frac{d^l}{dy^l} u(y) \right]_{y=-x}
\end{aligned}
$$

両辺に定数因子 $\frac{1}{2^l l!}$ を掛けると，定義式より次の関係が得られます。

$$
\finalanswer{P_l(-x) = (-1)^l P_l(x)}
$$

これにより，$P_l(x)$ は $l$ が偶数なら偶関数，$l$ が奇数なら奇関数であることが示されました。

===== FILE: 12special_functions/02/02_020.md =====
---
tags:
  - 標準
---

# 母関数と漸化式

## 問題
ルジャンドル多項式 $P_l(x)$ の母関数は次式で与えられる。
$$
g(x, t) = \frac{1}{\sqrt{1 - 2xt + t^2}} = \sum_{l=0}^\infty P_l(x) t^l \quad (|t|<1)
$$
以下の問いに答えよ。

(1) $g(x, t)$ を $t$ について微分し，等式
$$
(1 - 2xt + t^2) \frac{\partial g}{\partial t} = (x - t) g
$$
が成り立つことを示せ。

(2) (1) の等式に母関数の級数表示を代入し，$t^l$ の係数を比較することにより，漸化式
$$
(l+1) P_{l+1}(x) - (2l+1) x P_l(x) + l P_{l-1}(x) = 0 \quad (l \ge 1)
$$
を導け。

(3) $P_0(x) = 1$，$P_1(x) = x$ と (2) の漸化式を用いて，$P_2(x)$ を求めよ。

---

## 解答・解説

### (1)
母関数 $g(x, t) = (1 - 2xt + t^2)^{-1/2}$ を $t$ で偏微分します。

$$
\begin{aligned}
\frac{\partial g}{\partial t} &= -\frac{1}{2} (1 - 2xt + t^2)^{-3/2} \cdot (-2x + 2t) \\
&= \frac{x - t}{(1 - 2xt + t^2)^{3/2}}
\end{aligned}
$$

両辺に $(1 - 2xt + t^2)$ を掛けます。

$$
\begin{aligned}
(1 - 2xt + t^2) \frac{\partial g}{\partial t} &= \frac{x - t}{\sqrt{1 - 2xt + t^2}} \\
&= \finalanswer{(x - t) g}
\end{aligned}
$$

これで等式が示されました。

### (2)
母関数の級数表示 $g = \sum_{l=0}^\infty P_l(x) t^l$ を用いると，$t$ に関する偏微分は次のように書けます。

$$
\frac{\partial g}{\partial t} = \sum_{l=1}^\infty l P_l(x) t^{l-1}
$$

これを (1) の関係式の左辺と右辺に代入して展開します。まず左辺を計算します。

$$
(1 - 2xt + t^2) \sum_{l=1}^\infty l P_l(x) t^{l-1} = \sum_{l=1}^\infty l P_l(x) t^{l-1} - 2x \sum_{l=1}^\infty l P_l(x) t^l + \sum_{l=1}^\infty l P_l(x) t^{l+1}
$$

次に右辺を計算します。

$$
(x - t) \sum_{l=0}^\infty P_l(x) t^l = x \sum_{l=0}^\infty P_l(x) t^l - \sum_{l=0}^\infty P_l(x) t^{l+1}
$$

両辺において $t^l$ ($l \ge 1$) の係数を集めます。左辺の $t^l$ の係数は次のようになります。

$$
(l+1) P_{l+1}(x) - 2l x P_l(x) + (l-1) P_{l-1}(x)
$$

右辺の $t^l$ の係数は次のようになります。

$$
x P_l(x) - P_{l-1}(x)
$$

これらを等置します。

$$
(l+1) P_{l+1}(x) - 2l x P_l(x) + (l-1) P_{l-1}(x) = x P_l(x) - P_{l-1}(x)
$$

同類項を左辺にまとめて整理します。

$$
\finalanswer{(l+1) P_{l+1}(x) - (2l+1) x P_l(x) + l P_{l-1}(x) = 0}
$$

となります。

### (3)
(2) で導いた漸化式において $l=1$ と置きます。

$$
(1+1) P_2(x) - (2\cdot 1 + 1) x P_1(x) + 1 \cdot P_0(x) = 0
$$

係数を整理します。

$$
2 P_2(x) - 3x P_1(x) + P_0(x) = 0
$$

与えられた $P_0(x) = 1$，$P_1(x) = x$ を代入します。

$$
2 P_2(x) - 3x(x) + 1 = 0
$$

$P_2(x)$ について解きます。

$$
\begin{aligned}
2 P_2(x) &= 3x^2 - 1 \\
P_2(x) &= \finalanswer{\frac{1}{2}(3x^2 - 1)}
\end{aligned}
$$

微分操作を行わずに，代数的な漸化式のみから高次の多項式が求まります。

===== FILE: 12special_functions/02/02_030.md =====
---
tags:
  - 標準
---

# 直交性と展開

## 問題
ルジャンドル多項式 $P_l(x)$ は，区間 $[-1, 1]$ において次の直交関係を満たす。
$$
\int_{-1}^1 P_l(x) P_{l'}(x) \, dx = \frac{2}{2l+1} \delta_{l l'}
$$
以下の問いに答えよ。

(1) 関数 $f(x) = x^2$ をルジャンドル多項式の線形結合 $f(x) = c_0 P_0(x) + c_1 P_1(x) + c_2 P_2(x)$ として表し，係数 $c_0, c_1, c_2$ を求めよ。ただし $P_0(x)=1$，$P_1(x)=x$，$P_2(x)=\frac{1}{2}(3x^2-1)$ である。

(2) (1) の展開および直交関係を用いて，定積分 $\int_{-1}^1 x^2 P_2(x) \, dx$ の値を求めよ。

(3) $z$ 軸上の点 $(0, 0, a)$ ($a>0$) に置かれた点電荷 $q$ が，点 $\boldsymbol{r}$ ($r = |\boldsymbol{r}| > a$) に作る静電ポテンシャル
$$
\Phi(\boldsymbol{r}) = \frac{q}{4\pi\varepsilon_0 \sqrt{r^2 - 2ar\cos\theta + a^2}}
$$
を母関数を用いて展開し，$P_l(\cos\theta)$ の級数として表せ。

---

## 解答・解説

### (1)
$P_2(x) = \frac{3}{2}x^2 - \frac{1}{2}$ より，最高次の項 $x^2$ について整理します。

$$
\frac{3}{2}x^2 = P_2(x) + \frac{1}{2}
$$

両辺に $2/3$ を掛けます。

$$
x^2 = \frac{2}{3} P_2(x) + \frac{1}{3}
$$

ここで $P_0(x)=1$ であるため，定数項を $P_0(x)$ で置き換えます。

$$
x^2 = \frac{1}{3} P_0(x) + 0 \cdot P_1(x) + \frac{2}{3} P_2(x)
$$

各係数を比較すると，次のようになります。

$$
\finalanswer{c_0 = \frac{1}{3}, \quad c_1 = 0, \quad c_2 = \frac{2}{3}}
$$

となります。

### (2)
(1) で求めた多項式展開を被積分関数の $x^2$ に代入します。

$$
\int_{-1}^1 x^2 P_2(x) \, dx = \int_{-1}^1 \left( \frac{1}{3} P_0(x) + \frac{2}{3} P_2(x) \right) P_2(x) \, dx
$$

直交関係 $\int_{-1}^1 P_l(x) P_{l'}(x) \, dx = \frac{2}{2l+1} \delta_{l l'}$ を各項に適用します。$P_0(x) P_2(x)$ の項は $l \neq l'$ であるため 0 となります。

$$
\begin{aligned}
\int_{-1}^1 x^2 P_2(x) \, dx &= \frac{1}{3} \cdot 0 + \frac{2}{3} \int_{-1}^1 [P_2(x)]^2 \, dx \\
&= \frac{2}{3} \cdot \frac{2}{2\cdot 2 + 1} \\
&= \frac{2}{3} \cdot \frac{2}{5} \\
&= \finalanswer{\frac{4}{15}}
\end{aligned}
$$

直接積分することなく直交性から値が求まります。

### (3)
静電ポテンシャルの表式の分母から $r$ をくくり出します。

<!-- FIGURE solution (3): z 軸上の点 (0, 0, a) に置かれた点電荷 q と観測点 r=(r, theta, phi) の位置関係を示す極座標系の図。原点 O からの距離 r，角度 theta を明記。 -->
観測点と電荷の幾何学的配置を図に示します。

$$
\Phi(\boldsymbol{r}) = \frac{q}{4\pi\varepsilon_0 r} \frac{1}{\sqrt{1 - 2(a/r)\cos\theta + (a/r)^2}}
$$

$r > a$ であるため，$t = a/r < 1$ かつ $x = \cos\theta$ と置くことで，ルジャンドル多項式の母関数の形になります。

$$
\frac{1}{\sqrt{1 - 2xt + t^2}} = \sum_{l=0}^\infty P_l(x) t^l
$$

この級数展開をポテンシャルの式に代入します。

$$
\begin{aligned}
\Phi(\boldsymbol{r}) &= \frac{q}{4\pi\varepsilon_0 r} \sum_{l=0}^\infty P_l(\cos\theta) \left(\frac{a}{r}\right)^l \\
&= \finalanswer{\frac{q}{4\pi\varepsilon_0} \sum_{l=0}^\infty \frac{a^l}{r^{l+1}} P_l(\cos\theta)}
\end{aligned}
$$

この展開は静電ポテンシャルの多重極展開の基本形を与えます。

===== FILE: 12special_functions/02/02_040.md =====
---
tags:
  - 標準
---

# エルミート多項式

## 問題
エルミート多項式 $H_n(x)$ はロドリゲスの公式
$$
H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2}
$$
で定義される。以下の問いに答えよ。

(1) $H_0(x)$，$H_1(x)$，$H_2(x)$ を求めよ。

(2) 1 次元量子調和振動子の定常状態の波動関数は $\psi_n(x) = N_n H_n(\alpha x) e^{-\alpha^2 x^2 / 2}$ で与えられる。ここで $\alpha = \sqrt{m\omega/\hbar}$ である。直交関係
$$
\int_{-\infty}^\infty e^{-x^2} H_n(x) H_m(x) \, dx = \sqrt{\pi} 2^n n! \, \delta_{nm}
$$
を用いて，規格化条件 $\int_{-\infty}^\infty |\psi_n(x)|^2 \, dx = 1$ を満たす正の実数定数 $N_n$ を求めよ。

(3) 基底状態 $\psi_0(x)$ および第 1 励起状態 $\psi_1(x)$ の波動関数を具体的に求めよ。

---

## 解答・解説

### (1)
定義式において $n=0, 1, 2$ を代入して計算します。

$n=0$ のとき，微分は行いません。

$$
\finalanswer{H_0(x) = 1}
$$

$n=1$ のとき，1 階微分を実行します。

$$
\begin{aligned}
H_1(x) &= (-1)^1 e^{x^2} \frac{d}{dx} e^{-x^2} \\
&= -e^{x^2} (-2x e^{-x^2}) \\
&= \finalanswer{2x}
\end{aligned}
$$

$n=2$ のとき，2 階微分を実行します。

$$
\begin{aligned}
H_2(x) &= (-1)^2 e^{x^2} \frac{d^2}{dx^2} e^{-x^2} \\
&= e^{x^2} \frac{d}{dx} (-2x e^{-x^2}) \\
&= e^{x^2} (-2 e^{-x^2} + 4x^2 e^{-x^2}) \\
&= \finalanswer{4x^2 - 2}
\end{aligned}
$$

となります。

### (2)
規格化条件の積分に波動関数を代入します。

$$
\int_{-\infty}^\infty |\psi_n(x)|^2 \, dx = N_n^2 \int_{-\infty}^\infty [H_n(\alpha x)]^2 e^{-\alpha^2 x^2} \, dx = 1
$$

変数変換 $y = \alpha x$ を行うと，$dx = dy / \alpha$ となります。

$$
\frac{N_n^2}{\alpha} \int_{-\infty}^\infty [H_n(y)]^2 e^{-y^2} \, dy = 1
$$

与えられたエルミート多項式の直交関係において $m=n$ とした値 $\sqrt{\pi} 2^n n!$ を代入します。

$$
\frac{N_n^2}{\alpha} \sqrt{\pi} 2^n n! = 1
$$

$N_n > 0$ について解きます。

$$
\begin{aligned}
N_n^2 &= \frac{\alpha}{\sqrt{\pi} 2^n n!} \\
N_n &= \finalanswer{\sqrt{\frac{\alpha}{\sqrt{\pi} 2^n n!}}}
\end{aligned}
$$

$\alpha = \sqrt{m\omega/\hbar}$ を用いると，$(m\omega/(\pi\hbar))^{1/4} (2^n n!)^{-1/2}$ とも表せます。

### (3)
(2) で求めた規格化定数に $n=0$ および $n=1$ を代入します。

$n=0$ のとき，$N_0 = \sqrt{\frac{\alpha}{\sqrt{\pi}}} = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}$ であり，$H_0(\alpha x)=1$ です。

$$
\finalanswer{\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-\alpha^2 x^2 / 2}}
$$

$n=1$ のとき，$N_1 = \sqrt{\frac{\alpha}{2\sqrt{\pi}}} = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} \frac{1}{\sqrt{2}}$ であり，$H_1(\alpha x) = 2\alpha x$ です。

$$
\begin{aligned}
\psi_1(x) &= \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} \frac{1}{\sqrt{2}} \cdot 2\alpha x e^{-\alpha^2 x^2 / 2} \\
&= \finalanswer{\left(\frac{m\omega}{\pi\hbar}\right)^{1/4} \sqrt{2}\alpha x e^{-\alpha^2 x^2 / 2}}
\end{aligned}
$$

基底状態はガウス波束であり，第 1 励起状態は原点に節を 1 つ持つ奇関数となります。

===== FILE: 12special_functions/02/02_050.md =====
---
tags:
  - 発展
---

# ラゲール多項式

## 問題
結合ラゲール多項式 $L_n^k(x)$ はロドリゲス表示
$$
L_n^k(x) = \frac{e^x x^{-k}}{n!} \frac{d^n}{dx^n} (e^{-x} x^{n+k})
$$
で定義される。以下の問いに答えよ。

(1) $L_0^1(x)$ および $L_1^1(x)$ を求めよ。

(2) 水素原子の主量子数 $n=2$，方位量子数 $l=0$ の状態（2s 軌道）の動径波動関数は
$$
R_{20}(r) = N_{20} e^{-\rho/2} L_1^1(\rho)
$$
の形をとる。ここで $\rho = r/a_0$（$a_0$ はボーア半径）である。$R_{20}(r)$ を $r, a_0, N_{20}$ を用いて表せ。

(3) 規格化条件 $\int_0^\infty [R_{20}(r)]^2 r^2 \, dr = 1$ を用いて，正の規格化定数 $N_{20}$ を求めよ。

---

## 解答・解説

### (1)
定義式において $k=1$ と置きます。

$$
L_n^1(x) = \frac{e^x x^{-1}}{n!} \frac{d^n}{dx^n} (e^{-x} x^{n+1})
$$

$n=0$ を代入すると，微分は 0 階となります。

$$
\begin{aligned}
L_0^1(x) &= \frac{e^x x^{-1}}{0!} (e^{-x} x) \\
&= \finalanswer{1}
\end{aligned}
$$

$n=1$ を代入して 1 階微分を実行します。

$$
\begin{aligned}
L_1^1(x) &= \frac{e^x x^{-1}}{1!} \frac{d}{dx} (e^{-x} x^2) \\
&= e^x x^{-1} (-e^{-x} x^2 + 2x e^{-x}) \\
&= -x + 2 \\
&= \finalanswer{2 - x}
\end{aligned}
$$

となります。

### (2)
(1) で求めた $L_1^1(\rho) = 2 - \rho$ を動径波動関数の表式に代入します。

$$
R_{20}(r) = N_{20} e^{-\rho/2} (2 - \rho)
$$

変数 $\rho = r/a_0$ を代入します。

$$
\finalanswer{R_{20}(r) = N_{20} \left( 2 - \frac{r}{a_0} \right) e^{-r/(2a_0)}}
$$

動径波動関数は $r = 2a_0$ で符号を変える節を 1 つ持ちます。

### (3)
規格化の積分に (2) の結果を代入します。

$$
\int_0^\infty [R_{20}(r)]^2 r^2 \, dr = N_{20}^2 \int_0^\infty \left( 2 - \frac{r}{a_0} \right)^2 e^{-r/a_0} r^2 \, dr = 1
$$

無次元変数 $\rho = r/a_0$ を導入すると，$r = a_0 \rho$，$dr = a_0 \, d\rho$ となります。

$$
N_{20}^2 a_0^3 \int_0^\infty (2 - \rho)^2 \rho^2 e^{-\rho} \, d\rho = 1
$$

多項式を展開します。

$$
(2 - \rho)^2 \rho^2 = (4 - 4\rho + \rho^2) \rho^2 = 4\rho^2 - 4\rho^3 + \rho^4
$$

ガンマ関数の公式 $\int_0^\infty \rho^m e^{-\rho} \, d\rho = m!$ を各項に適用します。

$$
\begin{aligned}
\int_0^\infty (4\rho^2 - 4\rho^3 + \rho^4) e^{-\rho} \, d\rho &= 4(2!) - 4(3!) + 4! \\
&= 8 - 24 + 24 \\
&= 8
\end{aligned}
$$

したがって，規格化条件は次のようにまとまります。

$$
8 a_0^3 N_{20}^2 = 1
$$

$N_{20} > 0$ について解きます。

$$
\finalanswer{N_{20} = \frac{1}{2\sqrt{2} a_0^{3/2}}}
$$

となります。

===== FILE: 12special_functions/03/03_010.md =====
---
tags:
  - 標準
---

# ベッセル関数の級数解

## 問題
ベッセルの微分方程式
$$
x^2 \frac{d^2 y}{dx^2} + x \frac{dy}{dx} + (x^2 - \nu^2) y = 0
$$
において，$\nu \ge 0$ とする。解をフロベニウスの級数 $y = \sum_{m=0}^\infty a_m x^{m+\rho}$ ($a_0 \neq 0$) とおく。以下の問いに答えよ。

(1) 最低次の項 $x^\rho$ の係数を比較することにより，指標方程式を導き，$\rho$ の値を求めよ。

(2) $\rho = \nu$ としたとき，係数 $a_m$ の漸化式を導け。

(3) $a_0 = \frac{1}{2^\nu \Gamma(\nu+1)}$ と選ぶとき，第 1 種ベッセル関数 $J_\nu(x)$ の級数表示を求めよ。

---

## 解答・解説

### (1)
仮定した級数を微分します。

$$
\begin{aligned}
\frac{dy}{dx} &= \sum_{m=0}^\infty (m+\rho) a_m x^{m+\rho-1} \\
\frac{d^2 y}{dx^2} &= \sum_{m=0}^\infty (m+\rho)(m+\rho-1) a_m x^{m+\rho-2}
\end{aligned}
$$

これらを微分方程式に代入します。

$$
\sum_{m=0}^\infty (m+\rho)(m+\rho-1) a_m x^{m+\rho} + \sum_{m=0}^\infty (m+\rho) a_m x^{m+\rho} + \sum_{m=0}^\infty a_m x^{m+\rho+2} - \nu^2 \sum_{m=0}^\infty a_m x^{m+\rho} = 0
$$

最低次の項である $m=0$（$x^\rho$ の項）の係数をまとめます。

$$
[\rho(\rho-1) + \rho - \nu^2] a_0 = 0
$$

整理すると指標方程式が得られます。

$$
(\rho^2 - \nu^2) a_0 = 0
$$

$a_0 \neq 0$ であるため，$\rho$ の満たすべき条件は次のようになります。

$$
\finalanswer{\rho = \pm \nu}
$$

となります。

### (2)
$\rho = \nu$ とおき，次数の等しい項を比較します。$x^{\nu+1}$ の項（$m=1$）の係数は次のようになります。

$$
[(\nu+1)^2 - \nu^2] a_1 = (2\nu+1) a_1 = 0
$$

$\nu \ge 0$ であるため $2\nu+1 > 0$ となり，$a_1 = 0$ が定まります。

一般の次数 $x^{\nu+m}$ ($m \ge 2$) について係数を比較します。

$$
[(\nu+m)^2 - \nu^2] a_m + a_{m-2} = 0
$$

因数分解して整理します。

$$
\begin{aligned}
m(2\nu+m) a_m + a_{m-2} &= 0 \\
a_m &= \finalanswer{-\frac{1}{m(2\nu+m)} a_{m-2}}
\end{aligned}
$$

$a_1 = 0$ であることから，奇数番目の係数はすべて $a_{2k+1} = 0$ となります。

### (3)
偶数番目の添字を $m = 2k$ ($k = 1, 2, \dots$) とおきます。(2) の漸化式は次の形になります。

$$
a_{2k} = -\frac{1}{2k(2\nu+2k)} a_{2k-2} = -\frac{1}{4k(\nu+k)} a_{2k-2}
$$

これを繰り返し適用します。

$$
a_{2k} = \frac{(-1)^k}{4^k k! (\nu+k)(\nu+k-1)\cdots(\nu+1)} a_0
$$

与えられた $a_0 = \frac{1}{2^\nu \Gamma(\nu+1)}$ を代入します。ガンマ関数の性質より，分母の積は次のようにまとまります。

$$
(\nu+k)(\nu+k-1)\cdots(\nu+1)\Gamma(\nu+1) = \Gamma(\nu+k+1)
$$

したがって，係数 $a_{2k}$ は次のようになります。

$$
a_{2k} = \frac{(-1)^k}{k! \Gamma(\nu+k+1) 2^{2k+\nu}}
$$

これを級数 $y = \sum_{k=0}^\infty a_{2k} x^{2k+\nu}$ に代入します。

$$
\finalanswer{J_\nu(x) = \sum_{k=0}^\infty \frac{(-1)^k}{k! \Gamma(\nu+k+1)} \left(\frac{x}{2}\right)^{2k+\nu}}
$$

これが第 1 種ベッセル関数の標準的な級数表示となります。

===== FILE: 12special_functions/03/03_020.md =====
---
tags:
  - 発展
---

# ベッセル関数の漸近形

## 問題
ベッセルの微分方程式において，未知関数を $y(x) = \frac{u(x)}{\sqrt{x}}$ と変換する。以下の問いに答えよ。

(1) $u(x)$ が満たす微分方程式を導け。

(2) $x \to \infty$ の極限において，$u(x)$ の方程式を近似し，その一般解を求めよ。

(3) 第 1 種ベッセル関数 $J_\nu(x)$ の漸近形が振幅因子 $\sqrt{2/(\pi x)}$ を用いて
$$
J_\nu(x) \approx \sqrt{\frac{2}{\pi x}} \cos\left( x - \frac{\nu\pi}{2} - \frac{\pi}{4} \right) \quad (x \to \infty)
$$
となることを用いて，十分に大きい領域における隣り合う零点の間隔 $\Delta x$ を求めよ。

---

## 解答・解説

### (1)
変換 $y(x) = x^{-1/2} u(x)$ を $x$ で微分します。

$$
\begin{aligned}
\frac{dy}{dx} &= -\frac{1}{2} x^{-3/2} u + x^{-1/2} \frac{du}{dx} \\
\frac{d^2 y}{dx^2} &= \frac{3}{4} x^{-5/2} u - x^{-3/2} \frac{du}{dx} + x^{-1/2} \frac{d^2 u}{dx^2}
\end{aligned}
$$

これらをベッセルの微分方程式 $x^2 y'' + x y' + (x^2 - \nu^2)y = 0$ に代入します。

$$
x^2 \left( x^{-1/2} u'' - x^{-3/2} u' + \frac{3}{4} x^{-5/2} u \right) + x \left( x^{-1/2} u' - \frac{1}{2} x^{-3/2} u \right) + (x^2 - \nu^2) x^{-1/2} u = 0
$$

全体を $x^{3/2}$ で整理します。1 階微分の項 $-x^{1/2} u' + x^{1/2} u'$ は相殺します。

$$
x^{3/2} \left[ \frac{d^2 u}{dx^2} + \left( 1 - \frac{\nu^2 - 1/4}{x^2} \right) u \right] = 0
$$

両辺を $x^{3/2}$ で割ると，求める方程式が得られます。

$$
\finalanswer{\frac{d^2 u}{dx^2} + \left( 1 - \frac{\nu^2 - 1/4}{x^2} \right) u = 0}
$$

となります。

### (2)
$x \to \infty$ の極限では，遠心力的なポテンシャル項が無視できます。

$$
\frac{\nu^2 - 1/4}{x^2} \to 0
$$

したがって，微分方程式は単振動の方程式に帰着します。

$$
\frac{d^2 u}{dx^2} + u \approx 0
$$

この方程式の一般解は，任意定数 $C_1, C_2$（あるいは振幅 $A$ と位相 $\delta$）を用いて次のように表せます。

$$
\finalanswer{u(x) \approx C_1 \cos x + C_2 \sin x = A \cos(x - \delta)}
$$

となります。

### (3)
与えられた漸近形において，$J_\nu(x) = 0$ となる条件は余弦関数の位相が $\pi/2$ の奇数倍となるときです。

$$
x - \frac{\nu\pi}{2} - \frac{\pi}{4} \approx \left( n - \frac{1}{2} \right)\pi \quad (n \text{ は十分大きな整数})
$$

$x$ について解くと，第 $n$ 番目の零点 $x_n$ の漸近位置が得られます。

$$
x_n \approx n\pi + \frac{\nu\pi}{2} - \frac{\pi}{4}
$$

隣り合う零点の間隔 $\Delta x = x_{n+1} - x_n$ を計算します。

$$
\begin{aligned}
\Delta x &= \left( (n+1)\pi + \frac{\nu\pi}{2} - \frac{\pi}{4} \right) - \left( n\pi + \frac{\nu\pi}{2} - \frac{\pi}{4} \right) \\
&= \finalanswer{\pi}
\end{aligned}
$$

十分遠方において，ベッセル関数の零点は周期的な三角関数の零点と同様に間隔 $\pi$ で並びます。

===== FILE: 12special_functions/03/03_030.md =====
---
tags:
  - 標準
---

# 円形膜の振動数

## 問題
半径 $a$ の一様な円形膜の微小な横振動 $z(r, \theta, t)$ は波動方程式
$$
\frac{\partial^2 z}{\partial t^2} = v^2 \left( \frac{\partial^2 z}{\partial r^2} + \frac{1}{r}\frac{\partial z}{\partial r} + \frac{1}{r^2}\frac{\partial^2 z}{\partial \theta^2} \right)
$$
に従う。境界条件は膜の固定端条件 $z(a, \theta, t) = 0$ であり，原点 $r=0$ で変位は有限である。以下の問いに答えよ。

(1) 軸対称な定常振動解 $z(r, t) = R(r) \cos(\omega t)$ を仮定し，$R(r)$ が満たす微分方程式を導け。

(2) $k = \omega/v$ とおくとき，$r=0$ で有限という条件から，$R(r)$ を第 1 種ベッセル関数 $J_0$ を用いて表せ（振幅定数を $A$ とする）。

(3) $J_0(x)$ の正の零点を小さい順に $\alpha_{0,1}, \alpha_{0,2}, \dots, \alpha_{0,n}, \dots$ とするとき，固有振動数 $\omega_{0,n}$ を求めよ。

---

## 解答・解説

### (1)
軸対称振動であるため，$\theta$ 依存性はありません（$\partial z / \partial \theta = 0$）。

仮定した解 $z(r, t) = R(r) \cos(\omega t)$ を時間および空間で微分します。

$$
\begin{aligned}
\frac{\partial^2 z}{\partial t^2} &= -\omega^2 R(r) \cos(\omega t) \\
\frac{\partial^2 z}{\partial r^2} + \frac{1}{r}\frac{\partial z}{\partial r} &= \left( \frac{d^2 R}{dr^2} + \frac{1}{r}\frac{dR}{dr} \right) \cos(\omega t)
\end{aligned}
$$

これらを波動方程式に代入し，両辺から $\cos(\omega t)$ を消去します。

$$
-\omega^2 R = v^2 \left( \frac{d^2 R}{dr^2} + \frac{1}{r}\frac{dR}{dr} \right)
$$

移項して整理します。

$$
\finalanswer{\frac{d^2 R}{dr^2} + \frac{1}{r}\frac{dR}{dr} + \frac{\omega^2}{v^2} R = 0}
$$

となります。

### (2)
$k = \omega/v$ を代入し，両辺に $r^2$ を掛けます。

$$
r^2 \frac{d^2 R}{dr^2} + r \frac{dR}{dr} + k^2 r^2 R = 0
$$

変数変換 $\xi = kr$ を行うと，$\frac{d}{dr} = k \frac{d}{d\xi}$ となり，0 次のベッセルの微分方程式が得られます。

$$
\xi^2 \frac{d^2 R}{d\xi^2} + \xi \frac{dR}{d\xi} + \xi^2 R = 0
$$

この方程式の一般解は，第 1 種ベッセル関数 $J_0$ と第 2 種ベッセル関数（ノイマン関数）$Y_0$ の線形結合で表されます。

$$
R(r) = A J_0(kr) + B Y_0(kr)
$$

原点 $r \to 0$ において $Y_0(kr) \to -\infty$ と発散するため，変位が有限である物理的境界条件から $B=0$ が要求されます。したがって，解は次のようになります。

$$
\finalanswer{R(r) = A J_0(kr)}
$$

となります。

### (3)
円形膜の外周における固定境界条件 $z(a, \theta, t) = 0$ より，動径関数は $r=a$ で 0 とならなければなりません。

$$
R(a) = A J_0(ka) = 0
$$

振幅 $A \neq 0$ の有意な振動解を得るためには，引数 $ka$ が $J_0$ の零点でなければなりません。第 $n$ 番目の零点 $\alpha_{0,n}$ と等置します。

$$
k_{0,n} a = \alpha_{0,n}
$$

波数 $k_{0,n}$ について解きます。

$$
k_{0,n} = \frac{\alpha_{0,n}}{a}
$$

関係式 $\omega = v k$ に代入して固有振動数が求まります。

$$
\finalanswer{\omega_{0,n} = \frac{v \alpha_{0,n}}{a}}
$$

ベッセル関数の零点は等間隔ではないため，膜の倍音の振動数は基本振動数の整数倍にはなりません。

===== FILE: 12special_functions/03/03_040.md =====
---
tags:
  - 発展
---

# 球ベッセル関数

## 問題
球対称な 3 次元無限に深い井戸型ポテンシャル（半径 $a$ の内側で $V(r)=0$，外側で $V(r)=\infty$）中の質量 $m$ の粒子を考える。動径波動関数 $R(r)$ は
$$
\frac{d^2 R}{dr^2} + \frac{2}{r}\frac{dR}{dr} + \left( k^2 - \frac{l(l+1)}{r^2} \right) R = 0
$$
を満たす。ここで $k = \sqrt{2mE}/\hbar$ である。以下の問いに答えよ。

(1) $l=0$（s 波）の場合の方程式を，$u(r) = r R(r)$ を導入して解き，$r=0$ で有限である条件を満たす $R(r)$ を求めよ（定数倍を除く）。

(2) 球ベッセル関数 $j_0(x) = \frac{\sin x}{x}$ を用いて，境界条件 $R(a)=0$ から $l=0$ に対するエネルギー固有値 $E_{n,0}$ ($n=1, 2, \dots$) を求めよ。

(3) $l=1$ の球ベッセル関数 $j_1(x) = \frac{\sin x}{x^2} - \frac{\cos x}{x}$ に対し，境界条件 $j_1(ka)=0$ から波数が満たすべき超越方程式を導け。

---

## 解答・解説

### (1)
$l=0$ のとき，方程式は次のようになります。

$$
\frac{d^2 R}{dr^2} + \frac{2}{r}\frac{dR}{dr} + k^2 R = 0
$$

$u(r) = r R(r)$ とおき，$u(r)$ の微分を計算します。

$$
\begin{aligned}
\frac{du}{dr} &= R + r \frac{dR}{dr} \\
\frac{d^2 u}{dr^2} &= 2 \frac{dR}{dr} + r \frac{d^2 R}{dr^2} = r \left( \frac{d^2 R}{dr^2} + \frac{2}{r}\frac{dR}{dr} \right)
\end{aligned}
$$

元の方程式を代入すると，単振動の方程式が得られます。

$$
\frac{d^2 u}{dr^2} = -k^2 r R = -k^2 u
$$

この方程式の一般解は $u(r) = C_1 \sin(kr) + C_2 \cos(kr)$ です。したがって動径関数は次の形になります。

$$
R(r) = \frac{u(r)}{r} = C_1 \frac{\sin(kr)}{r} + C_2 \frac{\cos(kr)}{r}
$$

$r \to 0$ において $\cos(kr)/r \to \infty$ と発散するため，$r=0$ で有限である条件から $C_2 = 0$ となります。定数倍を除き，解は次のようになります。

$$
\finalanswer{R(r) = \frac{\sin(kr)}{r}}
$$

となります。

### (2)
$l=0$ の解は球ベッセル関数を用いて $R(r) = C j_0(kr)$ と表されます。境界条件 $R(a)=0$ を適用します。

$$
j_0(ka) = \frac{\sin(ka)}{ka} = 0
$$

$ka > 0$ であるため，分子が 0 となる条件から波数が定まります。

$$
ka = n\pi \quad (n = 1, 2, \dots)
$$

波数は次のようになります。

$$
k = \frac{n\pi}{a}
$$

関係式 $E = \frac{\hbar^2 k^2}{2m}$ に代入します。

$$
\finalanswer{E_{n,0} = \frac{n^2 \pi^2 \hbar^2}{2m a^2}}
$$

これは 1 次元の井戸型ポテンシャルのエネルギー準位と完全に一致します。

### (3)
$l=1$ に対する境界条件は $j_1(ka) = 0$ です。与えられた $j_1(x)$ の表式に代入します。

$$
\frac{\sin(ka)}{(ka)^2} - \frac{\cos(ka)}{ka} = 0
$$

$ka \neq 0$ であるため，両辺に $(ka)^2$ を掛けます。

$$
\sin(ka) - ka \cos(ka) = 0
$$

両辺を $\cos(ka)$ で割ると，正接関数に関する超越方程式が得られます。

$$
\finalanswer{\tan(ka) = ka}
$$

この方程式の根は数値的に求められ，p 波（$l=1$）のエネルギー固有値を決定します。

===== FILE: 12special_functions/03/03_050.md =====
---
tags:
  - 標準
---

# 球面調和関数の具体形

## 問題
球面調和関数 $Y_l^m(\theta, \phi)$ は
$$
Y_l^m(\theta, \phi) = (-1)^m \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{i m \phi} \quad (m \ge 0)
$$
で定義され，負の $m$ に対しては $Y_l^{-m}(\theta, \phi) = (-1)^m [Y_l^m(\theta, \phi)]^*$ である。ここで $P_l^m(x) = (1-x^2)^{m/2} \frac{d^m}{dx^m} P_l(x)$ である。以下の問いに答えよ。

(1) $P_0(x)=1$，$P_1(x)=x$ を用いて，$Y_0^0(\theta, \phi)$ および $Y_1^0(\theta, \phi)$ を求めよ。

(2) $P_1^1(x) = \sqrt{1-x^2}$ を用いて，$Y_1^1(\theta, \phi)$ および $Y_1^{-1}(\theta, \phi)$ を求めよ。

(3) 直交座標の変数 $x=r\sin\theta\cos\phi$，$y=r\sin\theta\sin\phi$，$z=r\cos\theta$ を用いて，線形結合 $\frac{1}{\sqrt{2}}(-Y_1^1 + Y_1^{-1})$ を直交座標の成分と動径 $r$ で表せ。

---

## 解答・解説

### (1)
定義式において各量子数を代入します。

$l=0, m=0$ のとき，$P_0^0(x) = P_0(x) = 1$ です。

$$
\begin{aligned}
Y_0^0(\theta, \phi) &= (-1)^0 \sqrt{\frac{1}{4\pi} \frac{0!}{0!}} \cdot 1 \cdot e^0 \\
&= \finalanswer{\frac{1}{\sqrt{4\pi}}}
\end{aligned}
$$

$l=1, m=0$ のとき，$P_1^0(x) = P_1(x) = x = \cos\theta$ です。

$$
\begin{aligned}
Y_1^0(\theta, \phi) &= (-1)^0 \sqrt{\frac{3}{4\pi} \frac{1!}{1!}} \cos\theta \cdot e^0 \\
&= \finalanswer{\sqrt{\frac{3}{4\pi}} \cos\theta}
\end{aligned}
$$

となります。

### (2)
$l=1, m=1$ のとき，$P_1^1(\cos\theta) = \sqrt{1-\cos^2\theta} = \sin\theta$ です。

$$
\begin{aligned}
Y_1^1(\theta, \phi) &= (-1)^1 \sqrt{\frac{3}{4\pi} \frac{(1-1)!}{(1+1)!}} \sin\theta e^{i\phi} \\
&= -\sqrt{\frac{3}{4\pi} \frac{1}{2}} \sin\theta e^{i\phi} \\
&= \finalanswer{-\sqrt{\frac{3}{8\pi}} \sin\theta e^{i\phi}}
\end{aligned}
$$

負の指数 $m=-1$ については，関係式 $Y_1^{-1} = (-1)^1 (Y_1^1)^*$ を適用します。

$$
\begin{aligned}
Y_1^{-1}(\theta, \phi) &= -\left( -\sqrt{\frac{3}{8\pi}} \sin\theta e^{-i\phi} \right) \\
&= \finalanswer{\sqrt{\frac{3}{8\pi}} \sin\theta e^{-i\phi}}
\end{aligned}
$$

となります。

### (3)
(2) で求めた $Y_1^1$ と $Y_1^{-1}$ を指定の線形結合に代入します。

$$
\begin{aligned}
\frac{1}{\sqrt{2}} (-Y_1^1 + Y_1^{-1}) &= \frac{1}{\sqrt{2}} \left( \sqrt{\frac{3}{8\pi}} \sin\theta e^{i\phi} + \sqrt{\frac{3}{8\pi}} \sin\theta e^{-i\phi} \right) \\
&= \frac{1}{\sqrt{2}} \sqrt{\frac{3}{8\pi}} \sin\theta (e^{i\phi} + e^{-i\phi}) \\
&= \frac{1}{4} \sqrt{\frac{3}{\pi}} \sin\theta (2\cos\phi) \\
&= \sqrt{\frac{3}{4\pi}} \sin\theta \cos\phi
\end{aligned}
$$

極座標と直交座標の関係式 $x = r\sin\theta\cos\phi$ より，$\sin\theta\cos\phi = x/r$ と置き換えることができます。

$$
\finalanswer{\sqrt{\frac{3}{4\pi}} \frac{x}{r}}
$$

この実数線形結合は，化学において $p_x$ 軌道と呼ばれる波動関数の角度依存性を与えます。

===== FILE: 12special_functions/03/03_060.md =====
---
tags:
  - 発展
---

# 球面調和関数の加法定理の入口

## 問題
2 つの単位ベクトル $\boldsymbol{n}_1, \boldsymbol{n}_2$ のなす角を $\gamma$ とするとき，球面調和関数の加法定理は
$$
P_l(\cos\gamma) = \frac{4\pi}{2l+1} \sum_{m=-l}^l Y_l^m(\theta_1, \phi_1) [Y_l^m(\theta_2, \phi_2)]^*
$$
で与えられる。以下の問いに答えよ。

(1) $l=0$ の場合について，加法定理の両辺を個別に計算し，等式が成り立つことを示せ。

(2) $\boldsymbol{n}_2$ を $z$ 軸の向きにとるとき（$\theta_2 = 0$），$\theta_1 = \theta$ かつ $\gamma = \theta$ となる。$m \neq 0$ のとき $Y_l^m(0, \phi_2) = 0$ となることを用いて，この特別な配置において加法定理が成り立つことを示せ。

(3) 単位球面上（$\boldsymbol{n}_1$ の立体角 $\Omega_1$）で加法定理の両辺を積分し，直交性を用いて両辺が共に $4\pi \delta_{l 0}$ となることを示せ。

---

## 解答・解説

### (1)
$l=0$ のとき，左辺のルジャンドル多項式は定義より次の値をとります。

$$
P_0(\cos\gamma) = 1
$$

右辺の和は $m=0$ の 1 項のみとなります。$Y_0^0 = \frac{1}{\sqrt{4\pi}}$ を代入します。

$$
\begin{aligned}
\frac{4\pi}{2\cdot 0 + 1} Y_0^0(\theta_1, \phi_1) [Y_0^0(\theta_2, \phi_2)]^* &= 4\pi \left(\frac{1}{\sqrt{4\pi}}\right) \left(\frac{1}{\sqrt{4\pi}}\right) \\
&= \finalanswer{1}
\end{aligned}
$$

両辺が共に 1 となり，等式が成り立ちます。

### (2)
$\boldsymbol{n}_2$ が $z$ 軸上にあるとき，$\gamma$ はそのまま $\boldsymbol{n}_1$ の極角 $\theta$ と一致するため，左辺は $P_l(\cos\theta)$ となります。

<!-- FIGURE solution (2): 単位球面上において n_2 を z 軸の正の向きにとり，任意の単位ベクトル n_1 とのなす角が極角 theta と一致する幾何学的配置を示す図。原点 O を含む。 -->
極軸上に一方のベクトルをとった配置を図に示します。

右辺において，$\theta_2 = 0$ では $m \neq 0$ の球面調和関数が消滅するため，$m=0$ の項のみが残ります。

$$
\frac{4\pi}{2l+1} Y_l^0(\theta, \phi_1) [Y_l^0(0, \phi_2)]^*
$$

ここで $Y_l^0(\theta, \phi) = \sqrt{\frac{2l+1}{4\pi}} P_l(\cos\theta)$ であり，$P_l(\cos 0) = P_l(1) = 1$ より $Y_l^0(0, \phi_2) = \sqrt{\frac{2l+1}{4\pi}}$ です。これらを代入します。

$$
\begin{aligned}
\frac{4\pi}{2l+1} \left( \sqrt{\frac{2l+1}{4\pi}} P_l(\cos\theta) \right) \left( \sqrt{\frac{2l+1}{4\pi}} \right) &= \frac{4\pi}{2l+1} \cdot \frac{2l+1}{4\pi} P_l(\cos\theta) \\
&= \finalanswer{P_l(\cos\theta)}
\end{aligned}
$$

左辺と完全に一致し，等式が示されました。

### (3)
加法定理の両辺を $\boldsymbol{n}_1$ の立体角 $\Omega_1$ について全球面で積分します。

まず左辺を積分します。$\boldsymbol{n}_2$ を基準の極軸にとることで，積分要素は $d\Omega_1 = \sin\gamma \, d\gamma d\phi'$ と表せます。

$$
\int P_l(\cos\gamma) \, d\Omega_1 = \int_0^{2\pi} d\phi' \int_0^\pi P_l(\cos\gamma) \sin\gamma \, d\gamma = 2\pi \int_{-1}^1 P_l(x) \, dx
$$

ルジャンドル多項式の直交性 $\int_{-1}^1 P_l(x) P_0(x) \, dx = \frac{2}{2\cdot 0 + 1}\delta_{l 0} = 2\delta_{l 0}$ を用います。

$$
\int P_l(\cos\gamma) \, d\Omega_1 = 2\pi \cdot 2\delta_{l 0} = \finalanswer{4\pi \delta_{l 0}}
$$

次に右辺を積分します。球面調和関数の規格直交性 $\int Y_l^m(\Omega_1) \, d\Omega_1 = \sqrt{4\pi} \int Y_l^m [Y_0^0]^* \, d\Omega_1 = \sqrt{4\pi} \delta_{l 0} \delta_{m 0}$ を用います。

$$
\begin{aligned}
\frac{4\pi}{2l+1} \sum_{m=-l}^l [Y_l^m(\Omega_2)]^* \int Y_l^m(\Omega_1) \, d\Omega_1 &= \frac{4\pi}{2l+1} \sum_{m=-l}^l [Y_l^m(\Omega_2)]^* \sqrt{4\pi} \delta_{l 0} \delta_{m 0} \\
&= 4\pi [Y_0^0(\Omega_2)]^* \sqrt{4\pi} \delta_{l 0} \\
&= 4\pi \left(\frac{1}{\sqrt{4\pi}}\right) \sqrt{4\pi} \delta_{l 0} \\
&= \finalanswer{4\pi \delta_{l 0}}
\end{aligned}
$$

両辺の積分値が完全に一致することが示されました。

===== END =====