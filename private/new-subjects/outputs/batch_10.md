===== FILE: 10integral_transforms/01/01_010.md =====
---
tags:
  - 基本
---

# フーリエ級数の計算

## 問題
区間 $-\pi < x < \pi$ において $f(x) = x$ と定義され，周期 $2\pi$ をもつ周期関数 $f(x)$ を考える（図）。$f(x)$ のフーリエ級数を
$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty (a_n \cos nx + b_n \sin nx)
$$
とする。以下の問いに答えよ。

<!-- FIGURE problem: 横軸 x，縦軸 y の直交座標系。周期 2π ののこぎり波 y = f(x)。区間 (-π, π) で原点を通る傾き 1 の線分（両端 x = ±π は白丸）。同様の線分が区間 (π, 3π) や (-3π, -π) にも周期的に繰り返されている様子。x 軸上に -π, 0, π, 2π, 3π の目盛りラベル。 -->

(1) フーリエ余弦係数 $a_n$（$n = 0, 1, 2, \dots$）を求めよ。

(2) フーリエ正弦係数 $b_n$（$n = 1, 2, \dots$）を求めよ。

(3) $f(x)$ のフーリエ級数展開を求めよ。

---

## 解答・解説

### (1)
フーリエ余弦係数は，関数の対称性を利用して計算します。被積分関数 $f(x) = x$ は奇関数であり，$\cos nx$ は偶関数であるため，その積 $x \cos nx$ は奇関数となります。対称区間 $[-\pi, \pi]$ における奇関数の積分は 0 です。したがって，すべての $n = 0, 1, 2, \dots$ について

$$
\begin{aligned}
a_n &= \frac{1}{\pi} \int_{-\pi}^\pi x \cos nx \, dx \\
&= \finalanswer{a_n = 0}
\end{aligned}
$$

となります。

### (2)
フーリエ正弦係数の積分を実行します。被積分関数 $x \sin nx$ は奇関数どうしの積であるため偶関数となり，積分区間を $[0, \pi]$ に半減して 2 倍できます。部分積分法を適用すると，次のように計算されます。

$$
\begin{aligned}
b_n &= \frac{1}{\pi} \int_{-\pi}^\pi x \sin nx \, dx \\
&= \frac{2}{\pi} \int_0^\pi x \sin nx \, dx \\
&= \frac{2}{\pi} \left( \left[ -x \frac{\cos nx}{n} \right]_0^\pi + \frac{1}{n} \int_0^\pi \cos nx \, dx \right) \\
&= \frac{2}{\pi} \left( -\frac{\pi \cos n\pi}{n} + \frac{1}{n^2} \left[ \sin nx \right]_0^\pi \right)
\end{aligned}
$$

ここで $\cos n\pi = (-1)^n$ であり，$\sin n\pi = 0$ であることを用いると，

$$
\begin{aligned}
b_n &= \frac{2}{\pi} \left( -\frac{\pi (-1)^n}{n} \right) \\
&= \finalanswer{b_n = \frac{2(-1)^{n+1}}{n}}
\end{aligned}
$$

となります。

### (3)
(1)および(2)で得られた係数をフーリエ級数の表式に代入します。(1)より余弦項および定数項はすべて 0 であり，正弦項のみが残ります。係数を代入すると，

$$
\begin{aligned}
f(x) &\sim \sum_{n=1}^\infty \frac{2(-1)^{n+1}}{n} \sin nx \\
&= \finalanswer{2 \left( \sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \cdots \right)}
\end{aligned}
$$

となります。級数の第 $n$ 項の振幅は $1/n$ に比例して減衰します。
===== FILE: 10integral_transforms/01/01_020.md =====
---
tags:
  - 基本
---

# 偶関数・奇関数と正弦・余弦級数

## 問題
区間 $0 < x < L$ で定義された関数 $f(x) = x$ を考える。この関数を区間 $-L < x < L$ に拡張して周期 $2L$ の周期関数を構成する。以下の問いに答えよ。

(1) $f(x)$ を区間 $-L < x < L$ に奇関数として拡張した関数のフーリエ級数展開（フーリエ正弦級数）を求めよ。

(2) $f(x)$ を区間 $-L < x < L$ に偶関数として拡張した関数のフーリエ余弦係数 $a_0$ および $a_n$（$n = 1, 2, \dots$）を求めよ。

(3) (2)の偶拡張に対するフーリエ級数展開（フーリエ余弦級数）を求めよ。

---

## 解答・解説

### (1)
奇関数として拡張した場合，余弦係数はすべて 0 となり，正弦係数のみが残ります。周期は $2L$ であるため，正弦係数 $b_n$ は次のように計算されます。

$$
\begin{aligned}
b_n &= \frac{2}{L} \int_0^L x \sin \frac{n\pi x}{L} \, dx \\
&= \frac{2}{L} \left( \left[ -x \frac{L}{n\pi} \cos \frac{n\pi x}{L} \right]_0^L + \frac{L}{n\pi} \int_0^L \cos \frac{n\pi x}{L} \, dx \right) \\
&= \frac{2}{L} \left( -\frac{L^2}{n\pi} \cos n\pi + \frac{L^2}{(n\pi)^2} \left[ \sin \frac{n\pi x}{L} \right]_0^L \right)
\end{aligned}
$$

$\cos n\pi = (-1)^n$ かつ $\sin n\pi = 0$ であることから，

$$
b_n = \frac{2L(-1)^{n+1}}{n\pi}
$$

が得られます。したがって，求める正弦級数は

$$
\finalanswer{f(x) \sim \frac{2L}{\pi} \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n} \sin \frac{n\pi x}{L}}
$$

となります。

### (2)
偶関数として拡張した場合，正弦係数はすべて 0 となります。まず定数項の係数を求めます。

$$
\begin{aligned}
a_0 &= \frac{2}{L} \int_0^L x \, dx \\
&= \frac{2}{L} \left[ \frac{x^2}{2} \right]_0^L \\
&= \finalanswer{a_0 = L}
\end{aligned}
$$

続いて $n \ge 1$ に対する余弦係数を計算します。

$$
\begin{aligned}
a_n &= \frac{2}{L} \int_0^L x \cos \frac{n\pi x}{L} \, dx \\
&= \frac{2}{L} \left( \left[ x \frac{L}{n\pi} \sin \frac{n\pi x}{L} \right]_0^L - \frac{L}{n\pi} \int_0^L \sin \frac{n\pi x}{L} \, dx \right) \\
&= \frac{2}{L} \left( 0 + \frac{L^2}{(n\pi)^2} \left[ \cos \frac{n\pi x}{L} \right]_0^L \right) \\
&= \finalanswer{a_n = \frac{2L}{(n\pi)^2} ((-1)^n - 1)}
\end{aligned}
$$

となります。

### (3)
(2)で求めた係数を級数の一般形に代入します。(2)の結果において，$n$ が偶数のときは $(-1)^n - 1 = 0$ となり，$n$ が奇数のときは $(-1)^n - 1 = -2$ となります。奇数を $n = 2m+1$（$m = 0, 1, 2, \dots$）とおくと，

$$
a_{2m+1} = -\frac{4L}{(2m+1)^2 \pi^2}
$$

となります。定数項は $a_0 / 2 = L / 2$ であるため，フーリエ余弦級数は

$$
\finalanswer{f(x) \sim \frac{L}{2} - \frac{4L}{\pi^2} \sum_{m=0}^\infty \frac{1}{(2m+1)^2} \cos \frac{(2m+1)\pi x}{L}}
$$

となります。正弦級数に比べて係数が $1/n^2$ で速く減衰します。
===== FILE: 10integral_transforms/01/01_030.md =====
---
tags:
  - 標準
---

# 収束とギブス現象

## 問題
区間 $-\pi < x < \pi$ において次のように定義され，周期 $2\pi$ をもつ矩形波 $f(x)$ を考える。
$$
f(x) = \begin{cases} -1 & (-\pi < x < 0) \\ 1 & (0 < x < \pi) \end{cases}
$$
$f(0) = 0, f(\pm \pi) = 0$ とする。以下の問いに答えよ。

(1) $f(x)$ のフーリエ正弦係数 $b_n$（$n = 1, 2, \dots$）を求めよ。

(2) $f(x)$ のフーリエ級数の第 $2m-1$ 部分和
$$
S_{2m-1}(x) = \sum_{k=1}^m b_{2k-1} \sin (2k-1)x
$$
を考える。$x > 0$ において $S_{2m-1}(x)$ が極大値をとる最小の正の $x$ を $x_m$ とするとき，$x_m$ を $m$ を用いて表せ。

(3) $m \to \infty$ における極大値の極限 $\lim_{m \to \infty} S_{2m-1}(x_m)$ を定積分の形で表せ。

---

## 解答・解説

### (1)
$f(x)$ は奇関数であるため，余弦係数はすべて 0 です。正弦係数は次のように計算されます。

$$
\begin{aligned}
b_n &= \frac{2}{\pi} \int_0^\pi 1 \cdot \sin nx \, dx \\
&= \frac{2}{\pi} \left[ -\frac{\cos nx}{n} \right]_0^\pi \\
&= \frac{2}{n\pi} (1 - (-1)^n)
\end{aligned}
$$

$n$ が偶数のとき $b_n = 0$ であり，$n = 2k-1$（奇数）のとき値は $4/((2k-1)\pi)$ となります。したがって，

$$
\finalanswer{b_n = \begin{cases} 0 & (n\ \text{が偶数}) \\ \dfrac{4}{n\pi} & (n\ \text{が奇数}) \end{cases}}
$$

となります。

### (2)
極大値を与える点を求めるため，部分和 $S_{2m-1}(x)$ を $x$ で微分します。

$$
\frac{d S_{2m-1}}{dx} = \sum_{k=1}^m \frac{4}{\pi} \cos (2k-1)x
$$

両辺に $\sin x$ をかけて積和の公式を適用すると，

$$
\begin{aligned}
\sin x \sum_{k=1}^m \cos (2k-1)x &= \sum_{k=1}^m \frac{1}{2} (\sin 2kx - \sin (2k-2)x) \\
&= \frac{1}{2} \sin 2mx
\end{aligned}
$$

が得られます。したがって導関数は

$$
\frac{d S_{2m-1}}{dx} = \frac{2\sin 2mx}{\pi \sin x}
$$

と表されます。導関数が 0 となる最小の正の $x$ は，分子の $\sin 2mx = 0$ を満たす最小の正の値であるため，

$$
\finalanswer{x_m = \frac{\pi}{2m}}
$$

となります。

### (3)
部分和に $x_m$ を代入した値は，導関数の積分として表せます。

$$
S_{2m-1}(x_m) = \int_0^{\pi/(2m)} \frac{2\sin 2mt}{\pi \sin t} \, dt
$$

ここで $u = 2mt$ と変数変換を行うと，$dt = du / (2m)$ となります。

$$
S_{2m-1}(x_m) = \frac{1}{\pi} \int_0^\pi \frac{\sin u}{m \sin (u/(2m))} \, du
$$

$m \to \infty$ の極限において，分母の関数は

$$
\lim_{m \to \infty} m \sin \left( \frac{u}{2m} \right) = \frac{u}{2}
$$

となります。これを用いると，極限値は

$$
\begin{aligned}
\lim_{m \to \infty} S_{2m-1}(x_m) &= \frac{1}{\pi} \int_0^\pi \frac{\sin u}{u/2} \, du \\
&= \finalanswer{\frac{2}{\pi} \int_0^\pi \frac{\sin u}{u} \, du}
\end{aligned}
$$

となります。この定積分の値は約 1.179 であり，不連続点の跳びの約 9% 分だけ関数値を超過します。不連続点近傍で生じるこの振動現象を図に示します。

<!-- FIGURE solution (3): 横軸 x，縦軸 y の直交座標系。y = 1 の水平線（x > 0 での矩形波の元の値）。m が大きい有限項のフーリエ部分和 S_{2m-1}(x) の曲線。原点から急激に立ち上がり，x = x_m で約 1.18 までオーバーシュートして極大値をとり，その後減衰振動しながら y = 1 に漸近していく様子。 -->
===== FILE: 10integral_transforms/01/01_040.md =====
---
tags:
  - 標準
---

# パーセバルの等式

## 問題
周期 $2\pi$ をもつ関数 $f(x)$ のフーリエ係数を $a_n, b_n$ とするとき，パーセバルの等式
$$
\frac{1}{\pi} \int_{-\pi}^\pi (f(x))^2 \, dx = \frac{a_0^2}{2} + \sum_{n=1}^\infty (a_n^2 + b_n^2)
$$
が成り立つ。区間 $-\pi < x < \pi$ で $f(x) = x$ と定義される周期 $2\pi$ の関数について，以下の問いに答えよ。

(1) 定積分 $\frac{1}{\pi} \int_{-\pi}^\pi (f(x))^2 \, dx$ の値を求めよ。

(2) $f(x)$ のフーリエ係数を用いて，パーセバルの等式の右辺を計算せよ。

(3) パーセバルの等式を用いて，無限級数の和 $\sum_{n=1}^\infty \frac{1}{n^2}$ を求めよ。

---

## 解答・解説

### (1)
左辺の積分を直接計算します。被積分関数は $x^2$ であり偶関数であるため，積分区間を $[0, \pi]$ に半減して 2 倍できます。

$$
\begin{aligned}
\frac{1}{\pi} \int_{-\pi}^\pi x^2 \, dx &= \frac{2}{\pi} \int_0^\pi x^2 \, dx \\
&= \frac{2}{\pi} \left[ \frac{x^3}{3} \right]_0^\pi \\
&= \finalanswer{\frac{2\pi^2}{3}}
\end{aligned}
$$

となります。

### (2)
$f(x) = x$（$-\pi < x < \pi$）のフーリエ係数を求めます。奇関数であるため，余弦係数はすべて 0 です。

$$
a_n = 0 \quad (n = 0, 1, 2, \dots)
$$

正弦係数は部分積分により次のように得られます。

$$
\begin{aligned}
b_n &= \frac{2}{\pi} \int_0^\pi x \sin nx \, dx \\
&= \frac{2}{\pi} \left( \left[ -x \frac{\cos nx}{n} \right]_0^\pi + \frac{1}{n} \int_0^\pi \cos nx \, dx \right) \\
&= \frac{2(-1)^{n+1}}{n}
\end{aligned}
$$

これらをパーセバルの等式の右辺に代入すると，

$$
\begin{aligned}
\frac{a_0^2}{2} + \sum_{n=1}^\infty (a_n^2 + b_n^2) &= \sum_{n=1}^\infty \left( \frac{2(-1)^{n+1}}{n} \right)^2 \\
&= \finalanswer{\sum_{n=1}^\infty \frac{4}{n^2}}
\end{aligned}
$$

となります。

### (3)
パーセバルの等式により，(1)で求めた左辺の値と(2)で求めた右辺の値は一致します。

$$
\frac{2\pi^2}{3} = 4 \sum_{n=1}^\infty \frac{1}{n^2}
$$

両辺を 4 で割ると，

$$
\finalanswer{\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}}
$$

となります。関数の二乗可積分ノルムとフーリエ係数の二乗和が結びつくことで，ゼータ関数の特殊値が導かれます。
===== FILE: 10integral_transforms/01/01_050.md =====
---
tags:
  - 標準
---

# フーリエ級数による級数の和

## 問題
区間 $-\pi \le x \le \pi$ で $f(x) = x^2$ と定義され，周期 $2\pi$ をもつ周期関数 $f(x)$ を考える。以下の問いに答えよ。

(1) $f(x)$ のフーリエ余弦係数 $a_0$ および $a_n$（$n = 1, 2, \dots$）を求めよ。

(2) $f(x)$ のフーリエ級数展開を求めよ。

(3) (2)の展開式に $x = \pi$ を代入することにより，無限級数の和 $\sum_{n=1}^\infty \frac{1}{n^2}$ を求めよ。

---

## 解答・解説

### (1)
$f(x) = x^2$ は偶関数であるため，正弦係数はすべて 0 となります。定数項の係数は次のように計算されます。

$$
\begin{aligned}
a_0 &= \frac{2}{\pi} \int_0^\pi x^2 \, dx \\
&= \frac{2}{\pi} \left[ \frac{x^3}{3} \right]_0^\pi \\
&= \finalanswer{a_0 = \frac{2\pi^2}{3}}
\end{aligned}
$$

$n \ge 1$ に対する余弦係数は，2 回の部分積分法を用いて計算します。

$$
\begin{aligned}
a_n &= \frac{2}{\pi} \int_0^\pi x^2 \cos nx \, dx \\
&= \frac{2}{\pi} \left( \left[ x^2 \frac{\sin nx}{n} \right]_0^\pi - \frac{2}{n} \int_0^\pi x \sin nx \, dx \right) \\
&= -\frac{4}{n\pi} \left( \left[ -x \frac{\cos nx}{n} \right]_0^\pi + \frac{1}{n} \int_0^\pi \cos nx \, dx \right) \\
&= -\frac{4}{n\pi} \left( -\frac{\pi (-1)^n}{n} + 0 \right) \\
&= \finalanswer{a_n = \frac{4(-1)^n}{n^2}}
\end{aligned}
$$

となります。

### (2)
求めた係数をフーリエ級数の公式に代入します。定数項は $a_0 / 2 = \pi^2 / 3$ です。$f(x)$ は連続で微分可能な周期関数であるため，各点でフーリエ級数は元の関数値に収束します。

$$
\begin{aligned}
f(x) &= \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2} \cos nx \\
&= \finalanswer{\frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n}{n^2} \cos nx}
\end{aligned}
$$

となります。

### (3)
(2)の等式に $x = \pi$ を代入します。$\cos n\pi = (-1)^n$ であり，$(-1)^n (-1)^n = ((-1)^2)^n = 1$ となります。

$$
f(\pi) = \pi^2 = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{1}{n^2}
$$

定数項を移項すると，

$$
4 \sum_{n=1}^\infty \frac{1}{n^2} = \pi^2 - \frac{\pi^2}{3} = \frac{2\pi^2}{3}
$$

となります。両辺を 4 で割ることで，

$$
\finalanswer{\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}}
$$

となります。
===== FILE: 10integral_transforms/01/01_060.md =====
---
tags:
  - 基本
---

# 複素フーリエ級数

## 問題
区間 $-\pi \le x < \pi$ で定義され，周期 $2\pi$ をもつ関数 $f(x) = e^{ax}$（$a$ は 0 でない実数定数）を考える。$f(x)$ の複素フーリエ級数を
$$
f(x) \sim \sum_{n=-\infty}^\infty c_n e^{inx}, \quad c_n = \frac{1}{2\pi} \int_{-\pi}^\pi f(x) e^{-inx} \, dx
$$
とする。以下の問いに答えよ。

(1) 複素フーリエ係数 $c_n$（$n$ は整数）を求めよ。

(2) $f(x)$ の複素フーリエ級数展開を求めよ。

(3) $x = 0$ における級数の収束を考えることにより，交代級数の和 $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2 + a^2}$ を求めよ。

---

## 解答・解説

### (1)
複素フーリエ係数の積分を計算します。指数の積をまとめて積分を実行します。

$$
\begin{aligned}
c_n &= \frac{1}{2\pi} \int_{-\pi}^\pi e^{(a - in)x} \, dx \\
&= \frac{1}{2\pi} \left[ \frac{e^{(a - in)x}}{a - in} \right]_{-\pi}^\pi \\
&= \frac{e^{(a-in)\pi} - e^{-(a-in)\pi}}{2\pi(a - in)}
\end{aligned}
$$

$e^{\pm in\pi} = (-1)^n$ であることを用いると，

$$
c_n = \frac{(-1)^n (e^{a\pi} - e^{-a\pi})}{2\pi(a - in)}
$$

となります。双曲線関数 $\sinh(a\pi) = (e^{a\pi} - e^{-a\pi})/2$ を用い，分母を有理化すると，

$$
\begin{aligned}
c_n &= \frac{(-1)^n \sinh(a\pi)}{\pi(a - in)} \\
&= \finalanswer{c_n = \frac{(-1)^n \sinh(a\pi)(a + in)}{\pi(a^2 + n^2)}}
\end{aligned}
$$

となります。

### (2)
得られた係数 $c_n$ を用いて複素フーリエ級数を書き下します。

$$
\begin{aligned}
f(x) &\sim \sum_{n=-\infty}^\infty \frac{(-1)^n \sinh(a\pi)(a + in)}{\pi(a^2 + n^2)} e^{inx} \\
&= \finalanswer{\frac{\sinh(a\pi)}{\pi} \sum_{n=-\infty}^\infty \frac{(-1)^n (a + in)}{a^2 + n^2} e^{inx}}
\end{aligned}
$$

となります。

### (3)
$f(x)$ は $x = 0$ において連続であるため，複素フーリエ級数の値は関数値 $f(0) = e^0 = 1$ に収束します。

$$
1 = \sum_{n=-\infty}^\infty c_n = c_0 + \sum_{n=1}^\infty (c_n + c_{-n})
$$

$c_0$ および $c_n + c_{-n}$ を計算します。

$$
c_0 = \frac{\sinh(a\pi)}{\pi a}
$$

虚数部は $n$ と $-n$ で符号が反転して相殺するため，

$$
\begin{aligned}
c_n + c_{-n} &= \frac{(-1)^n \sinh(a\pi)}{\pi(a^2 + n^2)} \left( (a + in) + (a - in) \right) \\
&= \frac{2a(-1)^n \sinh(a\pi)}{\pi(a^2 + n^2)}
\end{aligned}
$$

となります。これらを等式に代入すると，

$$
1 = \frac{\sinh(a\pi)}{\pi a} + \frac{2a\sinh(a\pi)}{\pi} \sum_{n=1}^\infty \frac{(-1)^n}{n^2 + a^2}
$$

が得られます。式を整理すると，

$$
\sum_{n=1}^\infty \frac{(-1)^n}{n^2 + a^2} = \frac{\pi}{2a\sinh(a\pi)} \left( 1 - \frac{\sinh(a\pi)}{\pi a} \right) = \frac{\pi}{2a\sinh(a\pi)} - \frac{1}{2a^2}
$$

となります。両辺に $-1$ をかけると，

$$
\finalanswer{\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2 + a^2} = \frac{1}{2a^2} - \frac{\pi}{2a\sinh(a\pi)}}
$$

となります。
===== FILE: 10integral_transforms/02/02_010.md =====
---
tags:
  - 基本
---

# デルタ関数の定義と性質

## 問題
ディラックのデルタ関数 $\delta(x)$ は，任意の滑らかなテスト関数 $\phi(x)$ に対して
$$
\int_{-\infty}^\infty \phi(x) \delta(x - a) \, dx = \phi(a)
$$
を満たす。以下の問いに答えよ。

(1) 実数定数 $c > 0$ に対して，変数変換を用いて等式 $\delta(cx) = \frac{1}{c} \delta(x)$ が成り立つことを示せ。

(2) $c < 0$ の場合を考慮し，0 でない任意の実数 $c$ に対して $\delta(cx) = \frac{1}{|c|} \delta(x)$ が成り立つことを示せ。

(3) 次の定積分の値を求めよ。
$$
I = \int_{-2}^3 (x^3 - 2x + 4) \delta(2x - 2) \, dx
$$

---

## 解答・解説

### (1)
任意のテスト関数 $\phi(x)$ との内積を考え，変数変換を行います。$y = cx$ と置くと，$dy = c\,dx$ となり，$c > 0$ であるため積分区間は $-\infty$ から $\infty$ のまま変わりません。

$$
\begin{aligned}
\int_{-\infty}^\infty \phi(x) \delta(cx) \, dx &= \int_{-\infty}^\infty \phi\left( \frac{y}{c} \right) \delta(y) \frac{dy}{c} \\
&= \frac{1}{c} \phi(0) \\
&= \int_{-\infty}^\infty \phi(x) \left( \finalanswer{\frac{1}{c} \delta(x)} \right) dx
\end{aligned}
$$

両辺が任意の $\phi(x)$ について成り立つため，等式が示されます。

### (2)
$c < 0$ のとき，変数変換 $y = cx$ を行うと積分区間の上限と下限が反転します。

$$
\begin{aligned}
\int_{-\infty}^\infty \phi(x) \delta(cx) \, dx &= \int_\infty^{-\infty} \phi\left( \frac{y}{c} \right) \delta(y) \frac{dy}{c} \\
&= -\frac{1}{c} \int_{-\infty}^\infty \phi\left( \frac{y}{c} \right) \delta(y) \, dy \\
&= \frac{1}{-c} \phi(0)
\end{aligned}
$$

$c < 0$ において $-c = |c|$ であるため，この結果は $\frac{1}{|c|} \phi(0)$ と書けます。(1)の $c > 0$ では $c = |c|$ であるため，符号を統合して

$$
\finalanswer{\delta(cx) = \frac{1}{|c|} \delta(x)}
$$

となります。

### (3)
デルタ関数の引数を $2x - 2 = 2(x - 1)$ と変形し，(2)の公式を適用します。

$$
\delta(2x - 2) = \delta(2(x - 1)) = \frac{1}{2} \delta(x - 1)
$$

これを積分に代入します。特異点 $x = 1$ は積分区間 $[-2, 3]$ の内部に含まれるため，ふるい分けの性質をそのまま適用できます。

$$
\begin{aligned}
I &= \int_{-2}^3 (x^3 - 2x + 4) \left( \frac{1}{2} \delta(x - 1) \right) dx \\
&= \frac{1}{2} \left[ x^3 - 2x + 4 \right]_{x=1} \\
&= \frac{1}{2} (1 - 2 + 4) \\
&= \finalanswer{I = \frac{3}{2}}
\end{aligned}
$$

となります。
===== FILE: 10integral_transforms/02/02_020.md =====
---
tags:
  - 標準
---

# 合成関数のデルタ関数

## 問題
滑らかな関数 $g(x)$ の単根を $x_i$（$g(x_i) = 0, g'(x_i) \ne 0$）とするとき，合成関数のデルタ関数について次の公式が成り立つ。
$$
\delta(g(x)) = \sum_i \frac{\delta(x - x_i)}{|g'(x_i)|}
$$
以下の問いに答えよ。

(1) 定数 $a > 0$ とする。$g(x) = x^2 - a^2$ に対して $\delta(x^2 - a^2)$ を $\delta(x - a)$ と $\delta(x + a)$ を用いて表せ。

(2) (1)の結果を用いて，定積分 $I = \int_0^\infty e^{-x} \delta(x^2 - 4) \, dx$ の値を求めよ。

(3) 定積分 $J = \int_{-\infty}^\infty (x + 2) \delta(x^3 - x) \, dx$ の値を求めよ。

---

## 解答・解説

### (1)
$g(x) = x^2 - a^2 = 0$ の根を求めると，$x = a$ および $x = -a$ の 2 つです。導関数は $g'(x) = 2x$ であるため，各根における微分係数の絶対値は

$$
|g'(\pm a)| = |2(\pm a)| = 2a
$$

となります。公式に代入すると，

$$
\begin{aligned}
\delta(x^2 - a^2) &= \frac{\delta(x - a)}{|g'(a)|} + \frac{\delta(x + a)}{|g'(-a)|} \\
&= \finalanswer{\delta(x^2 - a^2) = \frac{1}{2a} (\delta(x - a) + \delta(x + a))}
\end{aligned}
$$

となります。

### (2)
$a = 2$ の場合であり，(1)より

$$
\delta(x^2 - 4) = \frac{1}{4} (\delta(x - 2) + \delta(x + 2))
$$

となります。積分区間は $[0, \infty)$ であるため，$x = 2$ は区間内に含まれますが，$x = -2$ は区間外となります。したがって，

$$
\begin{aligned}
I &= \int_0^\infty e^{-x} \left( \frac{1}{4} \delta(x - 2) + \frac{1}{4} \delta(x + 2) \right) dx \\
&= \frac{1}{4} e^{-2} + 0 \\
&= \finalanswer{I = \frac{1}{4e^2}}
\end{aligned}
$$

となります。

### (3)
$g(x) = x^3 - x = x(x - 1)(x + 1) = 0$ の根は，$x = -1, 0, 1$ の 3 つです。導関数は $g'(x) = 3x^2 - 1$ です。各根における導関数の絶対値を求めます。

$$
\begin{aligned}
|g'(-1)| &= |3(-1)^2 - 1| = 2 \\
|g'(0)| &= |3(0)^2 - 1| = 1 \\
|g'(1)| &= |3(1)^2 - 1| = 2
\end{aligned}
$$

これらを用いてデルタ関数を展開します。

$$
\delta(x^3 - x) = \frac{1}{2} \delta(x + 1) + \delta(x) + \frac{1}{2} \delta(x - 1)
$$

すべての根が積分区間 $(-\infty, \infty)$ に含まれるため，ふるい分けの性質を適用すると，

$$
\begin{aligned}
J &= \int_{-\infty}^\infty (x + 2) \left( \frac{1}{2} \delta(x + 1) + \delta(x) + \frac{1}{2} \delta(x - 1) \right) dx \\
&= \frac{1}{2} (-1 + 2) + (0 + 2) + \frac{1}{2} (1 + 2) \\
&= \frac{1}{2} + 2 + \frac{3}{2} \\
&= \finalanswer{J = 4}
\end{aligned}
$$

となります。
===== FILE: 10integral_transforms/02/02_030.md =====
---
tags:
  - 標準
---

# デルタ関数の微分

## 問題
デルタ関数の導関数 $\delta'(x)$ について，以下の問いに答えよ。

(1) 任意の滑らかな関数 $f(x)$ に対し，部分積分を用いて等式
$$
\int_{-\infty}^\infty f(x) \delta'(x - a) \, dx = -f'(a)
$$
が成り立つことを示せ。ただし $\lim_{|x| \to \infty} f(x) = 0$ とする。

(2) 任意のテスト関数 $\phi(x)$ との内積を考えることにより，超関数の意味で等式 $x \delta'(x) = -\delta(x)$ が成り立つことを示せ。

(3) 次の定積分の値を求めよ。
$$
I = \int_{-\infty}^\infty (x^3 + 2x^2 - 5) \delta'(x - 2) \, dx
$$

---

## 解答・解説

### (1)
部分積分法を形式的に適用します。無限遠で $f(x)$ およびデルタ関数は 0 に収束するため，境界項は消滅します。

$$
\begin{aligned}
\int_{-\infty}^\infty f(x) \delta'(x - a) \, dx &= \left[ f(x) \delta(x - a) \right]_{-\infty}^\infty - \int_{-\infty}^\infty f'(x) \delta(x - a) \, dx \\
&= 0 - f'(a) \\
&= \finalanswer{-f'(a)}
\end{aligned}
$$

となり，等式が示されます。

### (2)
超関数としての等式を示すため，任意のテスト関数 $\phi(x)$ をかけて全空間で積分します。(1)の結果において $a = 0$ とし，関数として $x \phi(x)$ をとります。

$$
\begin{aligned}
\int_{-\infty}^\infty (x \delta'(x)) \phi(x) \, dx &= \int_{-\infty}^\infty (x \phi(x)) \delta'(x) \, dx \\
&= -\left. \frac{d}{dx} (x \phi(x)) \right|_{x=0}
\end{aligned}
$$

積の微分法を実行します。

$$
\frac{d}{dx} (x \phi(x)) = \phi(x) + x \phi'(x)
$$

$x = 0$ を代入すると $\phi(0) + 0 = \phi(0)$ となるため，

$$
\int_{-\infty}^\infty (x \delta'(x)) \phi(x) \, dx = -\phi(0)
$$

が得られます。一方，$-\delta(x)$ との内積も

$$
\int_{-\infty}^\infty (-\delta(x)) \phi(x) \, dx = -\phi(0)
$$

となります。任意の $\phi(x)$ について両者の積分値が一致するため，

$$
\finalanswer{x \delta'(x) = -\delta(x)}
$$

が成り立ちます。

### (3)
$f(x) = x^3 + 2x^2 - 5$ とおきます。(1)の性質を $a = 2$ として適用します。まず導関数を求めます。

$$
f'(x) = 3x^2 + 4x
$$

$x = 2$ における微分係数を計算します。

$$
f'(2) = 3(2)^2 + 4(2) = 12 + 8 = 20
$$

(1)の公式より $I = -f'(2)$ であるため，

$$
\finalanswer{I = -20}
$$

となります。
===== FILE: 10integral_transforms/02/02_040.md =====
---
tags:
  - 基本
---

# 階段関数とその微分

## 問題
ヘヴィサイドの階段関数 $\theta(x)$ は次のように定義される。
$$
\theta(x) = \begin{cases} 1 & (x > 0) \\ 0 & (x < 0) \end{cases}
$$
以下の問いに答えよ。

(1) 任意の滑らかなテスト関数 $\phi(x)$（$\lim_{|x| \to \infty} \phi(x) = 0$）を用いた積分により，超関数の意味で等式 $\frac{d\theta}{dx} = \delta(x)$ が成り立つことを示せ。

(2) 定数 $a > 0$ とする。関数 $f(x) = \theta(x) e^{-ax}$ の導関数 $f'(x)$ を，$\delta(x)$ と $\theta(x)$ を用いて表せ。

(3) (2)の結果を用いて定積分 $I = \int_{-\infty}^\infty f'(x) \, dx$ を計算し，その値が $\lim_{x \to \infty} f(x) - \lim_{x \to -\infty} f(x)$ と一致することを確かめよ。

---

## 解答・解説

### (1)
超関数の導関数の定義に従い，部分積分を行います。$\theta(x)$ の定義域を分割して積分を実行します。

$$
\begin{aligned}
\int_{-\infty}^\infty \frac{d\theta}{dx} \phi(x) \, dx &= \left[ \theta(x) \phi(x) \right]_{-\infty}^\infty - \int_{-\infty}^\infty \theta(x) \phi'(x) \, dx \\
&= 0 - \int_0^\infty \phi'(x) \, dx \\
&= - \left[ \phi(x) \right]_0^\infty \\
&= - (0 - \phi(0)) \\
&= \finalanswer{\phi(0)}
\end{aligned}
$$

これは $\int_{-\infty}^\infty \delta(x) \phi(x) \, dx = \phi(0)$ と一致するため，超関数の意味で $\frac{d\theta}{dx} = \delta(x)$ が成り立ちます。

### (2)
積の微分則を超関数に対して適用します。

$$
f'(x) = \frac{d\theta}{dx} e^{-ax} + \theta(x) \frac{d}{dx}(e^{-ax})
$$

(1)の結果 $\frac{d\theta}{dx} = \delta(x)$ を代入します。

$$
f'(x) = \delta(x) e^{-ax} - a \theta(x) e^{-ax}
$$

デルタ関数との積において $g(x) \delta(x) = g(0) \delta(x)$ が成り立つため，$e^{-a \cdot 0} = 1$ より第 1 項は $\delta(x)$ となります。したがって，

$$
\finalanswer{f'(x) = \delta(x) - a \theta(x) e^{-ax}}
$$

となります。

### (3)
(2)で得られた導関数を全空間で積分します。

$$
\begin{aligned}
I &= \int_{-\infty}^\infty (\delta(x) - a \theta(x) e^{-ax}) \, dx \\
&= \int_{-\infty}^\infty \delta(x) \, dx - a \int_0^\infty e^{-ax} \, dx \\
&= 1 - a \left[ -\frac{e^{-ax}}{a} \right]_0^\infty \\
&= 1 - a \left( 0 - \left( -\frac{1}{a} \right) \right) \\
&= 1 - 1 \\
&= \finalanswer{I = 0}
\end{aligned}
$$

一方，元の関数の極限値を計算すると，

$$
\begin{aligned}
\lim_{x \to \infty} f(x) &= \lim_{x \to \infty} e^{-ax} = 0 \\
\lim_{x \to -\infty} f(x) &= 0
\end{aligned}
$$

となります。したがって差は $0 - 0 = 0$ となり，積分の結果と一致します。
===== FILE: 10integral_transforms/02/02_050.md =====
---
tags:
  - 標準
---

# デルタ関数のフーリエ表示

## 問題
以下の問いに答えよ。

(1) パラメータ $\epsilon > 0$ に対して，定積分
$$
I_\epsilon(x) = \int_0^\infty e^{-\epsilon k} \cos(kx) \, dk
$$
を計算せよ。

(2) $\lim_{\epsilon \to +0} \frac{1}{\pi} \frac{\epsilon}{x^2 + \epsilon^2} = \delta(x)$ であることを用いて，広義積分 $\int_{-\infty}^\infty e^{ikx} \, dk$ が $2\pi \delta(x)$ と表されることを示せ。

(3) (2)の公式を用いて，次の定積分の値を求めよ。
$$
J = \int_{-\infty}^\infty \left( \int_{-\infty}^\infty e^{ik(x - 3)} \, dk \right) (x^2 + 1) \, dx
$$

---

## 解答・解説

### (1)
オイラーの公式を用いて被積分関数を複素指数の形に直し，積分を計算します。

$$
\begin{aligned}
I_\epsilon(x) &= \text{Re} \int_0^\infty e^{-(\epsilon - ix)k} \, dk \\
&= \text{Re} \left[ -\frac{e^{-(\epsilon - ix)k}}{\epsilon - ix} \right]_0^\infty
\end{aligned}
$$

$\epsilon > 0$ であるため上限 $k \to \infty$ で指数因子は 0 に減衰します。

$$
\begin{aligned}
I_\epsilon(x) &= \text{Re} \left( \frac{1}{\epsilon - ix} \right) \\
&= \text{Re} \left( \frac{\epsilon + ix}{\epsilon^2 + x^2} \right) \\
&= \finalanswer{\frac{\epsilon}{x^2 + \epsilon^2}}
\end{aligned}
$$

となります。

### (2)
積分を収束させるため，収束因子 $e^{-\epsilon |k|}$（$\epsilon > 0$）を導入して極限をとります。

$$
\int_{-\infty}^\infty e^{ikx} \, dk = \lim_{\epsilon \to +0} \int_{-\infty}^\infty e^{ikx - \epsilon |k|} \, dk
$$

積分区間を正負に分割します。

$$
\int_{-\infty}^\infty e^{ikx - \epsilon |k|} \, dk = \int_0^\infty e^{ikx - \epsilon k} \, dk + \int_{-\infty}^0 e^{ikx + \epsilon k} \, dk
$$

第 2 項において $k = -k'$ と置換すると，

$$
\begin{aligned}
\int_{-\infty}^\infty e^{ikx - \epsilon |k|} \, dk &= \int_0^\infty e^{-(\epsilon - ix)k} \, dk + \int_0^\infty e^{-(\epsilon + ix)k'} \, dk' \\
&= 2 \int_0^\infty e^{-\epsilon k} \cos(kx) \, dk \\
&= 2 I_\epsilon(x)
\end{aligned}
$$

となります。(1)の結果を代入し，$\epsilon \to +0$ の極限をとると，

$$
\begin{aligned}
\lim_{\epsilon \to +0} 2 I_\epsilon(x) &= \lim_{\epsilon \to +0} \frac{2\epsilon}{x^2 + \epsilon^2} \\
&= 2\pi \lim_{\epsilon \to +0} \frac{1}{\pi} \frac{\epsilon}{x^2 + \epsilon^2} \\
&= \finalanswer{2\pi \delta(x)}
\end{aligned}
$$

となり，公式が示されます。

### (3)
(2)の積分公式を内側の積分に適用します。

$$
\int_{-\infty}^\infty e^{ik(x - 3)} \, dk = 2\pi \delta(x - 3)
$$

これを外側の積分に代入し，デルタ関数のふるい分けの性質を用います。

$$
\begin{aligned}
J &= \int_{-\infty}^\infty 2\pi \delta(x - 3) (x^2 + 1) \, dx \\
&= 2\pi \left[ x^2 + 1 \right]_{x=3} \\
&= 2\pi (3^2 + 1) \\
&= \finalanswer{J = 20\pi}
\end{aligned}
$$

となります。
===== FILE: 10integral_transforms/03/03_010.md =====
---
tags:
  - 基本
---

# ガウス関数のフーリエ変換

## 問題
定数 $a > 0$ に対するガウス関数 $f(x) = e^{-ax^2}$ のフーリエ変換を
$$
\hat{f}(k) = \int_{-\infty}^\infty f(x) e^{-ikx} \, dx
$$
と定義する。以下の問いに答えよ。

(1) 被積分関数の指数部分を平方完成し，$\hat{f}(k)$ を
$$
\hat{f}(k) = e^{-\frac{k^2}{4a}} \int_{-\infty}^\infty e^{-a \left( x + \frac{ik}{2a} \right)^2} dx
$$
の形に変形せよ。

(2) ガウス積分の公式 $\int_{-\infty}^\infty e^{-a u^2} \, du = \sqrt{\frac{\pi}{a}}$ を用いて，$\hat{f}(k)$ を求めよ。

(3) $a = 1/2$ のとき，$f(x) = e^{-x^2/2}$ のフーリエ変換 $\hat{f}(k)$ を求め，$\hat{f}(k) = C f(k)$ と表したときの定数 $C$ を求めよ。

---

## 解答・解説

### (1)
フーリエ変換の被積分関数における指数部分を変形します。

$$
-ax^2 - ikx = -a \left( x^2 + \frac{ik}{a} x \right)
$$

括弧内を $x$ について平方完成します。

$$
\begin{aligned}
-a \left( x^2 + \frac{ik}{a} x \right) &= -a \left( \left( x + \frac{ik}{2a} \right)^2 - \left( \frac{ik}{2a} \right)^2 \right) \\
&= -a \left( x + \frac{ik}{2a} \right)^2 - a \left( \frac{k^2}{4a^2} \right) \\
&= -a \left( x + \frac{ik}{2a} \right)^2 - \frac{k^2}{4a}
\end{aligned}
$$

したがって，$x$ に依存しない因子 $e^{-\frac{k^2}{4a}}$ を積分の外に出すと，

$$
\finalanswer{\hat{f}(k) = e^{-\frac{k^2}{4a}} \int_{-\infty}^\infty e^{-a \left( x + \frac{ik}{2a} \right)^2} dx}
$$

となります。

### (2)
(1)の積分において，複素平面上での積分路の変形を行います。コーシーの積分定理により，実軸に平行な直線上の積分は実軸上の積分と一致します。

$$
\int_{-\infty}^\infty e^{-a \left( x + \frac{ik}{2a} \right)^2} dx = \int_{-\infty}^\infty e^{-au^2} \, du = \sqrt{\frac{\pi}{a}}
$$

これを(1)の結果に代入すると，

$$
\finalanswer{\hat{f}(k) = \sqrt{\frac{\pi}{a}} e^{-\frac{k^2}{4a}}}
$$

となります。ガウス関数のフーリエ変換は再びガウス関数となります。

### (3)
(2)の結果に $a = 1/2$ を代入します。

$$
\begin{aligned}
\hat{f}(k) &= \sqrt{\frac{\pi}{1/2}} e^{-\frac{k^2}{4(1/2)}} \\
&= \sqrt{2\pi} e^{-\frac{k^2}{2}}
\end{aligned}
$$

元の関数は $f(k) = e^{-k^2/2}$ であるため，

$$
\hat{f}(k) = \sqrt{2\pi} f(k)
$$

と表されます。したがって求める定数は

$$
\finalanswer{C = \sqrt{2\pi}}
$$

となります。この関数はフーリエ変換の固有関数となっています。
===== FILE: 10integral_transforms/03/03_020.md =====
---
tags:
  - 基本
---

# 指数減衰とローレンツ関数

## 問題
定数 $a > 0$ に対する両側指数減衰関数 $f(x) = e^{-a|x|}$ を考える（図）。フーリエ変換を
$$
\hat{f}(k) = \int_{-\infty}^\infty f(x) e^{-ikx} \, dx
$$
と定義する。以下の問いに答えよ。

<!-- FIGURE problem: 横軸 x，縦軸 y の直交座標系。y = e^{-a|x|} の曲線。原点 (0, 1) で尖点をもち，左右対称に x → ±∞ で指数関数的に 0 に減衰するグラフ。 -->

(1) $\hat{f}(k)$ を求めよ。

(2) 得られた $\hat{f}(k)$ が最大値をとる $k$ の値と，その最大値を求めよ。

(3) フーリエ逆変換の公式
$$
f(x) = \frac{1}{2\pi} \int_{-\infty}^\infty \hat{f}(k) e^{ikx} \, dk
$$
を用いて，定積分 $\int_{-\infty}^\infty \frac{\cos kx}{k^2 + a^2} \, dk$ の値を求めよ。

---

## 解答・解説

### (1)
絶対値記号を外すため，積分区間を負の領域と正の領域に分割します。

$$
\hat{f}(k) = \int_{-\infty}^0 e^{ax} e^{-ikx} \, dx + \int_0^\infty e^{-ax} e^{-ikx} \, dx
$$

それぞれの積分を実行します。

$$
\begin{aligned}
\hat{f}(k) &= \int_{-\infty}^0 e^{(a - ik)x} \, dx + \int_0^\infty e^{-(a + ik)x} \, dx \\
&= \left[ \frac{e^{(a - ik)x}}{a - ik} \right]_{-\infty}^0 + \left[ -\frac{e^{-(a + ik)x}}{a + ik} \right]_0^\infty \\
&= \frac{1}{a - ik} + \frac{1}{a + ik}
\end{aligned}
$$

通分して整理すると，

$$
\begin{aligned}
\hat{f}(k) &= \frac{(a + ik) + (a - ik)}{a^2 + k^2} \\
&= \finalanswer{\frac{2a}{k^2 + a^2}}
\end{aligned}
$$

となります。これはローレンツ関数の形をしています。

### (2)
(1)で得られた関数

$$
\hat{f}(k) = \frac{2a}{k^2 + a^2}
$$

は，分母が最小となるときに最大値をとります。分母 $k^2 + a^2$ は実数 $k$ に対して $k = 0$ で最小値 $a^2$ をとるため，$\hat{f}(k)$ は $k = 0$ で最大となります。最大値は

$$
\hat{f}(0) = \frac{2a}{a^2} = \frac{2}{a}
$$

となります。したがって，

$$
\finalanswer{k = 0\ \text{で最大値}\ \frac{2}{a}}
$$

となります。

### (3)
フーリエ逆変換の公式に $\hat{f}(k)$ を代入します。

$$
e^{-a|x|} = \frac{1}{2\pi} \int_{-\infty}^\infty \frac{2a}{k^2 + a^2} e^{ikx} \, dk
$$

オイラーの公式 $e^{ikx} = \cos kx + i \sin kx$ を適用します。奇関数である正弦成分の積分は 0 になるため，

$$
e^{-a|x|} = \frac{a}{\pi} \int_{-\infty}^\infty \frac{\cos kx}{k^2 + a^2} \, dk
$$

が得られます。両辺に $\frac{\pi}{a}$ をかけると，

$$
\finalanswer{\int_{-\infty}^\infty \frac{\cos kx}{k^2 + a^2} \, dk = \frac{\pi}{a} e^{-a|x|}}
$$

となります。
===== FILE: 10integral_transforms/03/03_030.md =====
---
tags:
  - 基本
---

# フーリエ変換の性質

## 問題
関数 $f(x)$ のフーリエ変換を $\hat{f}(k) = \int_{-\infty}^\infty f(x) e^{-ikx} \, dx$ とする。以下の問いに答えよ。

(1) 実数定数 $x_0$ に対し，$g(x) = f(x - x_0)$ のフーリエ変換 $\hat{g}(k)$ を $\hat{f}(k)$ を用いて表せ。

(2) $h(x) = f'(x)$ のフーリエ変換 $\hat{h}(k)$ を $\hat{f}(k)$ を用いて表せ。ただし $\lim_{|x| \to \infty} f(x) = 0$ とする。

(3) 定数 $c > 0$ に対し，$p(x) = f(cx)$ のフーリエ変換 $\hat{p}(k)$ を $\hat{f}$ を用いて表せ。

---

## 解答・解説

### (1)
定義式に基づいてフーリエ変換の積分を立て，変数変換を行います。$y = x - x_0$ と置くと，$x = y + x_0, dx = dy$ となります。

$$
\begin{aligned}
\hat{g}(k) &= \int_{-\infty}^\infty f(x - x_0) e^{-ikx} \, dx \\
&= \int_{-\infty}^\infty f(y) e^{-ik(y + x_0)} \, dy \\
&= e^{-ikx_0} \int_{-\infty}^\infty f(y) e^{-iky} \, dy
\end{aligned}
$$

積分の部分は $\hat{f}(k)$ そのものであるため，

$$
\finalanswer{\hat{g}(k) = e^{-ikx_0} \hat{f}(k)}
$$

となります。実空間での平行移動は，波数空間での位相変化に対応します。

### (2)
導関数のフーリエ変換に部分積分法を適用します。

$$
\begin{aligned}
\hat{h}(k) &= \int_{-\infty}^\infty f'(x) e^{-ikx} \, dx \\
&= \left[ f(x) e^{-ikx} \right]_{-\infty}^\infty - \int_{-\infty}^\infty f(x) (-ik) e^{-ikx} \, dx
\end{aligned}
$$

無限遠で $f(x) \to 0$ であるため境界項は消滅します。

$$
\begin{aligned}
\hat{h}(k) &= 0 + ik \int_{-\infty}^\infty f(x) e^{-ikx} \, dx \\
&= \finalanswer{ik \hat{f}(k)}
\end{aligned}
$$

となります。実空間での微分演算は，波数空間での $ik$ の掛け算に変換されます。

### (3)
スケール変換された関数のフーリエ変換において，$y = cx$ と置換します。$c > 0$ より $dx = dy/c$ であり，積分区間は変化しません。

$$
\begin{aligned}
\hat{p}(k) &= \int_{-\infty}^\infty f(cx) e^{-ikx} \, dx \\
&= \int_{-\infty}^\infty f(y) e^{-ik(y/c)} \frac{dy}{c} \\
&= \frac{1}{c} \int_{-\infty}^\infty f(y) e^{-i(k/c)y} \, dy
\end{aligned}
$$

右辺の積分は $\hat{f}(k/c)$ を表しているため，

$$
\finalanswer{\hat{p}(k) = \frac{1}{c} \hat{f}\left( \frac{k}{c} \right)}
$$

となります。実空間での収縮（$c > 1$）は，波数空間での伸長と振幅の減少に対応します。
===== FILE: 10integral_transforms/03/03_040.md =====
---
tags:
  - 標準
---

# 畳み込み定理

## 問題
2 つの関数 $f(x), g(x)$ の畳み込みは $(f * g)(x) = \int_{-\infty}^\infty f(x - y) g(y) \, dy$ で定義される。以下の問いに答えよ。

(1) フーリエ変換を $\mathcal{F}[f](k) = \int_{-\infty}^\infty f(x) e^{-ikx} \, dx$ とするとき，畳み込みのフーリエ変換がそれぞれの積 $\mathcal{F}[f * g](k) = \hat{f}(k) \hat{g}(k)$ に等しいことを示せ。

(2) $f(x) = e^{-ax^2}, g(x) = e^{-bx^2}$（$a, b > 0$）のフーリエ変換 $\hat{f}(k), \hat{g}(k)$ を求めよ。

(3) (1)の畳み込み定理とフーリエ逆変換を用いて，畳み込み積分
$$
(f * g)(x) = \int_{-\infty}^\infty e^{-a(x - y)^2} e^{-by^2} \, dy
$$
を計算せよ。

---

## 解答・解説

### (1)
畳み込みのフーリエ変換の式に重積分を代入し，積分の順序を交換します。

$$
\begin{aligned}
\mathcal{F}[f * g](k) &= \int_{-\infty}^\infty \left( \int_{-\infty}^\infty f(x - y) g(y) \, dy \right) e^{-ikx} \, dx \\
&= \int_{-\infty}^\infty g(y) \left( \int_{-\infty}^\infty f(x - y) e^{-ikx} \, dx \right) dy
\end{aligned}
$$

内側の積分において $u = x - y$ と変数変換を行うと，$x = u + y, dx = du$ となります。

$$
\begin{aligned}
\int_{-\infty}^\infty f(x - y) e^{-ikx} \, dx &= \int_{-\infty}^\infty f(u) e^{-ik(u + y)} \, du \\
&= e^{-iky} \int_{-\infty}^\infty f(u) e^{-iku} \, du \\
&= e^{-iky} \hat{f}(k)
\end{aligned}
$$

これを外側の積分に戻すと，

$$
\begin{aligned}
\mathcal{F}[f * g](k) &= \int_{-\infty}^\infty g(y) e^{-iky} \hat{f}(k) \, dy \\
&= \hat{f}(k) \int_{-\infty}^\infty g(y) e^{-iky} \, dy \\
&= \finalanswer{\hat{f}(k) \hat{g}(k)}
\end{aligned}
$$

となり，定理が示されます。

### (2)
ガウス関数のフーリエ変換の公式 $\int_{-\infty}^\infty e^{-\alpha x^2} e^{-ikx} \, dx = \sqrt{\frac{\pi}{\alpha}} e^{-\frac{k^2}{4\alpha}}$ をそれぞれの関数に適用します。

$$
\finalanswer{\hat{f}(k) = \sqrt{\frac{\pi}{a}} e^{-\frac{k^2}{4a}}, \quad \hat{g}(k) = \sqrt{\frac{\pi}{b}} e^{-\frac{k^2}{4b}}}
$$

となります。

### (3)
(1)の畳み込み定理により，$(f * g)(x)$ のフーリエ変換は(2)で求めた変換の積となります。

$$
\begin{aligned}
\mathcal{F}[f * g](k) &= \left( \sqrt{\frac{\pi}{a}} e^{-\frac{k^2}{4a}} \right) \left( \sqrt{\frac{\pi}{b}} e^{-\frac{k^2}{4b}} \right) \\
&= \frac{\pi}{\sqrt{ab}} \exp \left( -\frac{k^2}{4} \left( \frac{1}{a} + \frac{1}{b} \right) \right) \\
&= \frac{\pi}{\sqrt{ab}} \exp \left( -\frac{a + b}{4ab} k^2 \right)
\end{aligned}
$$

ここで $A = \frac{a + b}{4ab}$ とおきます。ガウス関数のフーリエ逆変換は

$$
\frac{1}{2\pi} \int_{-\infty}^\infty e^{-A k^2} e^{ikx} \, dk = \frac{1}{2\pi} \sqrt{\frac{\pi}{A}} e^{-\frac{x^2}{4A}}
$$

となります。$4A = \frac{a + b}{ab}$ より $\frac{1}{4A} = \frac{ab}{a + b}$ であり，係数は

$$
\frac{\pi}{\sqrt{ab}} \frac{1}{2\pi} \sqrt{\frac{\pi}{A}} = \frac{1}{2\sqrt{ab}} \sqrt{4\pi \frac{ab}{a + b}} = \sqrt{\frac{\pi}{a + b}}
$$

となります。したがって，

$$
\finalanswer{(f * g)(x) = \sqrt{\frac{\pi}{a + b}} \exp \left( -\frac{ab}{a + b} x^2 \right)}
$$

となります。2 つのガウス関数の畳み込みは再びガウス関数となります。
===== FILE: 10integral_transforms/03/03_050.md =====
---
tags:
  - 標準
---

# 幅の積と不確定性

## 問題
実関数 $f(x)$ は規格化条件 $\int_{-\infty}^\infty (f(x))^2 \, dx = 1$ を満たし，$x \to \pm \infty$ で急速に 0 に減衰するとする。位置と波数の分散を
$$
(\Delta x)^2 = \int_{-\infty}^\infty x^2 (f(x))^2 \, dx, \quad (\Delta k)^2 = \frac{1}{2\pi} \int_{-\infty}^\infty k^2 |\hat{f}(k)|^2 \, dk
$$
で定義する。ただし平均値は 0 とする。以下の問いに答えよ。

(1) プランシュレルの定理 $\frac{1}{2\pi} \int_{-\infty}^\infty |\hat{f}(k)|^2 \, dk = \int_{-\infty}^\infty (f(x))^2 \, dx$ および導関数の性質を用いて，$(\Delta k)^2 = \int_{-\infty}^\infty (f'(x))^2 \, dx$ と表せることを示せ。

(2) シュワルツの不等式
$$
\left( \int_{-\infty}^\infty x f(x) f'(x) \, dx \right)^2 \le \left( \int_{-\infty}^\infty x^2 (f(x))^2 \, dx \right) \left( \int_{-\infty}^\infty (f'(x))^2 \, dx \right)
$$
の左辺の積分を部分積分により計算し，不確定性関係 $\Delta x \Delta k \ge \frac{1}{2}$ を導け。

(3) ガウス関数 $f(x) = \left( \frac{2a}{\pi} \right)^{1/4} e^{-ax^2}$（$a > 0$）に対して $\Delta x$ および $\Delta k$ を求め，等号 $\Delta x \Delta k = \frac{1}{2}$ が成立することを確かめよ。

---

## 解答・解説

### (1)
導関数のフーリエ変換は $\mathcal{F}[f'](k) = ik \hat{f}(k)$ です。この関数の絶対値の 2 乗をとると，

$$
|\mathcal{F}[f'](k)|^2 = |ik \hat{f}(k)|^2 = k^2 |\hat{f}(k)|^2
$$

となります。プランシュレルの定理を関数 $f'(x)$ に対して適用します。

$$
\int_{-\infty}^\infty (f'(x))^2 \, dx = \frac{1}{2\pi} \int_{-\infty}^\infty |\mathcal{F}[f'](k)|^2 \, dk
$$

右辺に先ほどの式を代入すると，

$$
\int_{-\infty}^\infty (f'(x))^2 \, dx = \frac{1}{2\pi} \int_{-\infty}^\infty k^2 |\hat{f}(k)|^2 \, dk = \finalanswer{(\Delta k)^2}
$$

となり，等式が示されます。

### (2)
シュワルツの不等式の左辺の括弧内を部分積分により計算します。$f(x) f'(x) = \frac{1}{2} \frac{d}{dx} (f(x))^2$ であることに着目します。

$$
\begin{aligned}
\int_{-\infty}^\infty x f(x) f'(x) \, dx &= \int_{-\infty}^\infty x \left( \frac{1}{2} \frac{d}{dx} (f(x))^2 \right) dx \\
&= \left[ \frac{1}{2} x (f(x))^2 \right]_{-\infty}^\infty - \frac{1}{2} \int_{-\infty}^\infty (f(x))^2 \, dx
\end{aligned}
$$

無限遠での急速な減衰により境界項は 0 となり，規格化条件より積分項は 1 です。

$$
\int_{-\infty}^\infty x f(x) f'(x) \, dx = 0 - \frac{1}{2} \cdot 1 = -\frac{1}{2}
$$

この値をシュワルツの不等式に代入します。

$$
\left( -\frac{1}{2} \right)^2 \le (\Delta x)^2 (\Delta k)^2
$$

両辺を整理すると $(\Delta x)^2 (\Delta k)^2 \ge \frac{1}{4}$ となり，平方根をとることで

$$
\finalanswer{\Delta x \Delta k \ge \frac{1}{2}}
$$

が導かれます。

### (3)
与えられたガウス関数を用いて各分散を計算します。まず位置の分散を求めます。

$$
(\Delta x)^2 = \left( \frac{2a}{\pi} \right)^{1/2} \int_{-\infty}^\infty x^2 e^{-2ax^2} \, dx
$$

公式 $\int_{-\infty}^\infty x^2 e^{-\beta x^2} \, dx = \frac{1}{2\beta} \sqrt{\frac{\pi}{\beta}}$ において $\beta = 2a$ とおくと，

$$
(\Delta x)^2 = \sqrt{\frac{2a}{\pi}} \frac{1}{4a} \sqrt{\frac{\pi}{2a}} = \frac{1}{4a}
$$

となります。したがって $\Delta x = \frac{1}{2\sqrt{a}}$ です。次に導関数を求めます。

$$
f'(x) = \left( \frac{2a}{\pi} \right)^{1/4} (-2ax) e^{-ax^2} = -2ax f(x)
$$

(1)の関係式を用いると，

$$
\begin{aligned}
(\Delta k)^2 &= \int_{-\infty}^\infty (f'(x))^2 \, dx \\
&= 4a^2 \int_{-\infty}^\infty x^2 (f(x))^2 \, dx \\
&= 4a^2 (\Delta x)^2 \\
&= 4a^2 \cdot \frac{1}{4a} \\
&= a
\end{aligned}
$$

となります。したがって $\Delta k = \sqrt{a}$ です。両者の積を計算すると，

$$
\Delta x \Delta k = \frac{1}{2\sqrt{a}} \cdot \sqrt{a} = \finalanswer{\frac{1}{2}}
$$

となり，最小不確定性が達成されることが確かめられます。
===== FILE: 10integral_transforms/03/03_060.md =====
---
tags:
  - 標準
---

# プランシュレルの定理

## 問題
フーリエ変換を $\hat{f}(k) = \int_{-\infty}^\infty f(x) e^{-ikx} \, dx$ と定義するとき，プランシュレルの定理
$$
\int_{-\infty}^\infty |f(x)|^2 \, dx = \frac{1}{2\pi} \int_{-\infty}^\infty |\hat{f}(k)|^2 \, dk
$$
が成り立つ。定数 $a > 0$ に対する矩形関数
$$
f(x) = \begin{cases} 1 & (|x| \le a) \\ 0 & (|x| > a) \end{cases}
$$
について（図），以下の問いに答えよ。

<!-- FIGURE problem: 横軸 x，縦軸 y の直交座標系。区間 [-a, a] で高さ 1 の水平線分をもち，|x| > a では y = 0 となる対称な矩形パルス。x 軸上に -a, 0, a の目盛りラベル。 -->

(1) $f(x)$ のフーリエ変換 $\hat{f}(k)$ を求めよ。

(2) 左辺の積分 $\int_{-\infty}^\infty |f(x)|^2 \, dx$ の値を求めよ。

(3) プランシュレルの定理を用いて，定積分 $\int_{-\infty}^\infty \frac{\sin^2(ak)}{k^2} \, dk$ の値を求めよ。

---

## 解答・解説

### (1)
定義式に従って積分区間を $[-a, a]$ に限定して計算します。

$$
\begin{aligned}
\hat{f}(k) &= \int_{-a}^a 1 \cdot e^{-ikx} \, dx \\
&= \left[ \frac{e^{-ikx}}{-ik} \right]_{-a}^a \\
&= \frac{e^{-ika} - e^{ika}}{-ik} \\
&= \frac{e^{ika} - e^{-ika}}{ik}
\end{aligned}
$$

オイラーの公式 $\sin(ak) = (e^{ika} - e^{-ika}) / (2i)$ を用いると，

$$
\finalanswer{\hat{f}(k) = \frac{2\sin(ak)}{k}}
$$

となります。この関数はシンク関数と呼ばれます。

### (2)
実空間での二乗可積分ノルムを直接計算します。被積分関数は区間 $[-a, a]$ で 1，それ以外の領域で 0 です。

$$
\begin{aligned}
\int_{-\infty}^\infty |f(x)|^2 \, dx &= \int_{-a}^a 1^2 \, dx \\
&= [x]_{-a}^a \\
&= \finalanswer{2a}
\end{aligned}
$$

となります。

### (3)
プランシュレルの定理に(1)および(2)の結果を代入します。

$$
2a = \frac{1}{2\pi} \int_{-\infty}^\infty \left| \frac{2\sin(ak)}{k} \right|^2 dk
$$

右辺の絶対値の 2 乗を展開します。

$$
\begin{aligned}
2a &= \frac{1}{2\pi} \int_{-\infty}^\infty \frac{4\sin^2(ak)}{k^2} \, dk \\
&= \frac{2}{\pi} \int_{-\infty}^\infty \frac{\sin^2(ak)}{k^2} \, dk
\end{aligned}
$$

両辺に $\frac{\pi}{2}$ をかけると，

$$
\finalanswer{\int_{-\infty}^\infty \frac{\sin^2(ak)}{k^2} \, dk = \pi a}
$$

となります。実空間での有限幅の信号エネルギーが，波数空間での広がり全体の積分と等しく結びつきます。
===== END =====