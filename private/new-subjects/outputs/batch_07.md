===== FILE: 08differential_equations/04/04_010.md =====
---
tags:
  - 標準
---

# べき級数解

## 問題
エアリーの微分方程式
$$
\frac{d^2 y}{dx^2} - x y = 0
$$
を考える。原点 $x = 0$ のまわりのべき級数解 $y(x) = \sum_{n=0}^\infty a_n x^n$ を求める。以下の問いに答えよ。

(1) 級数を微分方程式に代入して各次数の係数を比較することにより，$a_2$ を $a_0, a_1$ を用いて表し，一般の漸化式
$$
a_{n+2} = \frac{a_{n-1}}{(n+2)(n+1)} \quad (n \ge 1)
$$
を導け。

(2) 初期条件 $a_0 = 1, a_1 = 0$ に対応する解 $y_1(x)$ の級数展開を，$x^6$ の項まで求めよ。

(3) 初期条件 $a_0 = 0, a_1 = 1$ に対応する解 $y_2(x)$ の級数展開を，$x^7$ の項まで求めよ。

---

## 解答・解説

### (1)
べき級数を項別微分して方程式に代入し，べきの次数をそろえて係数を比較します。

$y(x)$ を2回項別微分すると，
$$
\begin{aligned}
\frac{d^2 y}{dx^2} &= \sum_{n=2}^\infty n(n-1) a_n x^{n-2} \\
&= 2 \cdot 1 a_2 + \sum_{k=1}^\infty (k+2)(k+1) a_{k+2} x^k
\end{aligned}
$$
となります。

一方，第2項は，
$$
\begin{aligned}
x y &= \sum_{n=0}^\infty a_n x^{n+1} \\
&= \sum_{k=1}^\infty a_{k-1} x^k
\end{aligned}
$$
となります。

これらをエアリー方程式に代入すると，
$$
\begin{aligned}
2 a_2 + \sum_{k=1}^\infty \left( (k+2)(k+1) a_{k+2} - a_{k-1} \right) x^k = 0
\end{aligned}
$$
となります。

各次数の係数が恒等的に $0$ でなければならないため，定数項より，
$$
\finalanswer{a_2 = 0}
$$
となります。

また，$k \ge 1$ の係数より，
$$
\finalanswer{a_{n+2} = \frac{a_{n-1}}{(n+2)(n+1)} \quad (n \ge 1)}
$$
が得られます。

### (2)
(1)の漸化式に $a_0 = 1, a_1 = 0$ を適用し，各係数を順次計算します。

$a_1 = 0, a_2 = 0$ であるため，漸化式より $3$ で割った余りが $1$ または $2$ となる添字の係数はすべて $0$ となります。

非ゼロとなる係数を計算すると，
$$
\begin{aligned}
a_3 &= \frac{a_0}{3 \cdot 2} = \frac{1}{6} \\
a_6 &= \frac{a_3}{6 \cdot 5} = \frac{1}{30} \cdot \frac{1}{6} = \frac{1}{180}
\end{aligned}
$$
となります。

したがって，求める級数解は，
$$
\finalanswer{y_1(x) = 1 + \frac{1}{6}x^3 + \frac{1}{180}x^6 + \dots}
$$
となります。

### (3)
初期条件 $a_0 = 0, a_1 = 1$ を適用し，各係数を計算します。

$a_0 = 0, a_2 = 0$ であるため，$3$ の倍数および $3$ で割って $2$ 余る添字の係数はすべて $0$ となります。

非ゼロとなる係数を計算すると，
$$
\begin{aligned}
a_4 &= \frac{a_1}{4 \cdot 3} = \frac{1}{12} \\
a_7 &= \frac{a_4}{7 \cdot 6} = \frac{1}{42} \cdot \frac{1}{12} = \frac{1}{504}
\end{aligned}
$$
となります。

したがって，求める級数解は，
$$
\finalanswer{y_2(x) = x + \frac{1}{12}x^4 + \frac{1}{504}x^7 + \dots}
$$
となります。これら $y_1(x), y_2(x)$ の線形結合がエアリー関数の基本解系を構成します。
===== FILE: 08differential_equations/04/04_020.md =====
---
tags:
  - 発展
---

# フロベニウス法

## 問題
微分方程式
$$
4x \frac{d^2 y}{dx^2} + 2 \frac{dy}{dx} + y = 0 \quad (x > 0)
$$
を考える。原点 $x = 0$ はこの方程式の確定特異点である。フロベニウス法により，解を $y(x) = \sum_{n=0}^\infty a_n x^{n+r}$（$a_0 \neq 0$）と仮定する。以下の問いに答えよ。

(1) $x = 0$ における決定方程式を導き，その2つの根 $r_1, r_2$（$r_1 > r_2$）を求めよ。

(2) 大きい方の根 $r_1$ に対する級数の漸化式を求め，対応する解 $y_1(x)$ を初等関数で表せ。

(3) 小さい方の根 $r_2$ に対する級数の漸化式を求め，対応する解 $y_2(x)$ を初等関数で表せ。

---

## 解答・解説

### (1)
仮定した級数を方程式に代入し，最低次の項の係数を $0$ とおくことで決定方程式を導きます。

級数の導関数は，
$$
\begin{aligned}
\frac{dy}{dx} &= \sum_{n=0}^\infty (n+r) a_n x^{n+r-1} \\
\frac{d^2 y}{dx^2} &= \sum_{n=0}^\infty (n+r)(n+r-1) a_n x^{n+r-2}
\end{aligned}
$$
となります。

微分方程式に代入すると，
$$
\begin{aligned}
\sum_{n=0}^\infty \left[ 4(n+r)(n+r-1) + 2(n+r) \right] a_n x^{n+r-1} + \sum_{n=0}^\infty a_n x^{n+r} = 0
\end{aligned}
$$
となります。

最低次の $x^{r-1}$ の係数は $n = 0$ の項から生じるため，
$$
\begin{aligned}
\left( 4r(r-1) + 2r \right) a_0 &= 0 \\
2r(2r - 1) a_0 &= 0
\end{aligned}
$$
となります。

$a_0 \neq 0$ より決定方程式は $2r(2r-1) = 0$ となり，根は大きい順に，
$$
\finalanswer{r_1 = \frac{1}{2}, \quad r_2 = 0}
$$
となります。

### (2)
$r_1 = 1/2$ を代入し，係数の漸化式から級数を求めます。

$x^{n+r-1}$ の係数を比較すると，
$$
\begin{aligned}
2(n+r)(2n+2r-1) a_n + a_{n-1} &= 0
\end{aligned}
$$
となります。

$r = 1/2$ を代入すると，
$$
\begin{aligned}
2\left(n + \frac{1}{2}\right)(2n) a_n + a_{n-1} &= 0 \\
2n(2n+1) a_n + a_{n-1} &= 0 \\
a_n &= -\frac{a_{n-1}}{2n(2n+1)}
\end{aligned}
$$
となります。

$a_0 = 1$ と選ぶと，
$$
\begin{aligned}
a_n &= \frac{(-1)^n}{(2n+1)!}
\end{aligned}
$$
となります。

したがって，解は，
$$
\begin{aligned}
y_1(x) &= \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} x^{n+1/2} \\
&= \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} (\sqrt{x})^{2n+1} \\
&= \finalanswer{\sin\sqrt{x}}
\end{aligned}
$$
となります。

### (3)
$r_2 = 0$ を代入し，係数の漸化式から級数を求めます。

$r = 0$ を漸化式に代入すると，
$$
\begin{aligned}
2n(2n-1) a_n + a_{n-1} &= 0 \\
a_n &= -\frac{a_{n-1}}{2n(2n-1)}
\end{aligned}
$$
となります。

$a_0 = 1$ と選ぶと，
$$
\begin{aligned}
a_n &= \frac{(-1)^n}{(2n)!}
\end{aligned}
$$
となります。

したがって，解は，
$$
\begin{aligned}
y_2(x) &= \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} x^n \\
&= \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} (\sqrt{x})^{2n} \\
&= \finalanswer{\cos\sqrt{x}}
\end{aligned}
$$
となります。
===== FILE: 08differential_equations/04/04_030.md =====
---
tags:
  - 標準
---

# ルジャンドル方程式の級数解

## 問題
ルジャンドルの微分方程式
$$
(1 - x^2)\frac{d^2 y}{dx^2} - 2x \frac{dy}{dx} + l(l+1) y = 0
$$
を考える。ここで $l$ は実数定数である。解をべき級数 $y(x) = \sum_{n=0}^\infty a_n x^n$ と仮定する。以下の問いに答えよ。

(1) 級数を微分方程式に代入することにより，係数に関する漸化式
$$
a_{n+2} = -\frac{(l - n)(l + n + 1)}{(n + 2)(n + 1)} a_n \quad (n \ge 0)
$$
を導け。

(2) $l$ が非負整数であるとき，偶数次または奇数次の級数が有限次数の多項式で打ち切られる理由を述べ，打ち切られる次数を示せ。

(3) $l = 2$ のとき，規格化条件 $P_2(1) = 1$ を満たす多項式解 $P_2(x)$ を求めよ。

---

## 解答・解説

### (1)
べき級数を2回項別微分して方程式に代入し，各次数の係数を集めます。

方程式の各項を展開すると，
$$
\begin{aligned}
\frac{d^2 y}{dx^2} &= \sum_{n=0}^\infty (n+2)(n+1) a_{n+2} x^n \\
-x^2 \frac{d^2 y}{dx^2} &= -\sum_{n=0}^\infty n(n-1) a_n x^n \\
-2x \frac{dy}{dx} &= -\sum_{n=0}^\infty 2n a_n x^n \\
l(l+1) y &= \sum_{n=0}^\infty l(l+1) a_n x^n
\end{aligned}
$$
となります。

これらを足し合わせて $x^n$ の係数を $0$ とおくと，
$$
\begin{aligned}
(n+2)(n+1) a_{n+2} - \left[ n(n-1) + 2n - l(l+1) \right] a_n &= 0 \\
(n+2)(n+1) a_{n+2} - \left[ n(n+1) - l(l+1) \right] a_n &= 0
\end{aligned}
$$
となります。

括弧内を因数分解すると，
$$
\begin{aligned}
n(n+1) - l(l+1) &= n^2 - l^2 + n - l \\
&= (n - l)(n + l + 1) = -(l - n)(l + n + 1)
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{a_{n+2} = -\frac{(l - n)(l + n + 1)}{(n + 2)(n + 1)} a_n \quad (n \ge 0)}
$$
が得られます。

### (2)
分子の因数が $0$ になる条件に着目します。

$l$ が非負整数であるとき，$n = l$ となるステップにおいて分子に $(l - l) = 0$ が現れます。

これにより，
$$
\begin{aligned}
a_{l+2} = 0
\end{aligned}
$$
となります。

漸化式は2つ飛びであるため，$a_{l+2} = 0$ 以降の同偶奇性のすべての係数は $a_{l+4} = a_{l+6} = \dots = 0$ となり，級数は有限項で終了します。

したがって，
$$
\finalanswer{n = l \text{ で } a_{l+2} = 0 \text{ となり，次数 } l \text{ の多項式となる}}
$$
となります。$l$ が偶数なら偶関数，$l$ が奇数なら奇関数の多項式解が得られます。

### (3)
$l = 2$ を代入して偶数次の係数を求め，規格化を行います。

$l = 2$ のとき，$l$ は偶数なので偶多項式となります。$n = 0$ を代入すると，
$$
\begin{aligned}
a_2 &= -\frac{(2 - 0)(2 + 0 + 1)}{2 \cdot 1} a_0 \\
&= -\frac{6}{2} a_0 = -3 a_0
\end{aligned}
$$
となります。$n = 2$ では $a_4 = 0$ となります。

したがって，多項式は，
$$
\begin{aligned}
y(x) &= a_0 (1 - 3x^2)
\end{aligned}
$$
となります。

規格化条件 $y(1) = 1$ を適用すると，
$$
\begin{aligned}
a_0 (1 - 3 \cdot 1^2) &= 1 \\
-2 a_0 &= 1 \\
a_0 &= -\frac{1}{2}
\end{aligned}
$$
となります。

したがって，ルジャンドル多項式 $P_2(x)$ は，
$$
\finalanswer{P_2(x) = \frac{1}{2}(3x^2 - 1)}
$$
となります。
===== FILE: 08differential_equations/04/04_040.md =====
---
tags:
  - 標準
---

# スツルム・リウビルの固有値問題

## 問題
区間 $0 \le x \le L$ における境界値問題
$$
\frac{d^2 y}{dx^2} + \lambda y = 0, \quad y(0) = 0, \quad \frac{dy}{dx}(L) = 0
$$
を考える。以下の問いに答えよ。

(1) $\lambda \le 0$ のとき，境界条件を満たす解は自明な解 $y(x) = 0$ に限られることを示せ。

(2) $\lambda > 0$（$\lambda = k^2, k > 0$）のとき，固有値 $\lambda_n$ および対応する固有関数 $y_n(x)$ を求めよ。

(3) 規格化条件 $\int_0^L y_n(x)^2 \, dx = 1$ を満たすように固有関数を規格化せよ。

---

## 解答・解説

### (1)
$\lambda = 0$ および $\lambda < 0$ のそれぞれについて一般解を求め，境界条件を適用します。

$\lambda = 0$ のとき，一般解は $y(x) = C_1 x + C_2$ です。$y(0) = 0$ より $C_2 = 0$，$y'(L) = C_1 = 0$ となるため，$y(x) = 0$ となります。

$\lambda < 0$ のとき，$\lambda = -\mu^2$（$\mu > 0$）とおくと，一般解は，
$$
\begin{aligned}
y(x) &= C_1 \cosh(\mu x) + C_2 \sinh(\mu x)
\end{aligned}
$$
となります。

境界条件 $y(0) = 0$ より $C_1 = 0$ です。導関数は $y'(x) = C_2 \mu \cosh(\mu x)$ であり，$y'(L) = C_2 \mu \cosh(\mu L) = 0$ となります。$\mu > 0$ かつ $\cosh(\mu L) \ge 1 > 0$ であるため $C_2 = 0$ となります。

したがって，
$$
\finalanswer{\lambda \le 0 \text{ のとき } y(x) = 0}
$$
となり，非自明な解は存在しません。

### (2)
$\lambda = k^2 > 0$ とおき，三角関数の一般解に境界条件を課します。

一般解は，
$$
\begin{aligned}
y(x) &= C_1 \cos(kx) + C_2 \sin(kx)
\end{aligned}
$$
となります。

境界条件 $y(0) = 0$ より $C_1 = 0$ です。

導関数を計算すると $y'(x) = C_2 k \cos(kx)$ です。境界条件 $y'(L) = 0$ を適用すると，
$$
\begin{aligned}
C_2 k \cos(kL) &= 0
\end{aligned}
$$
となります。

非自明解（$C_2 \neq 0$）をもつためには $\cos(kL) = 0$ が必要であり，
$$
\begin{aligned}
k_n L &= \left(n - \frac{1}{2}\right)\pi = \frac{(2n - 1)\pi}{2} \quad (n = 1, 2, 3, \dots)
\end{aligned}
$$
となります。

したがって，固有値と固有関数は，
$$
\finalanswer{\lambda_n = \left(\frac{(2n - 1)\pi}{2L}\right)^2, \quad y_n(x) = C_n \sin\left(\frac{(2n - 1)\pi x}{2L}\right) \quad (n = 1, 2, 3, \dots)}
$$
となります。

### (3)
二乗の定積分を計算して規格化定数を求めます。

半角の公式を用いて積分を計算すると，
$$
\begin{aligned}
\int_0^L \sin^2\left(\frac{(2n - 1)\pi x}{2L}\right) \, dx &= \int_0^L \frac{1 - \cos\left(\frac{(2n - 1)\pi x}{L}\right)}{2} \, dx \\
&= \left[ \frac{x}{2} - \frac{L}{2(2n - 1)\pi} \sin\left(\frac{(2n - 1)\pi x}{L}\right) \right]_0^L \\
&= \frac{L}{2} - 0 = \frac{L}{2}
\end{aligned}
$$
となります。

規格化条件 $C_n^2 \frac{L}{2} = 1$ より，$C_n = \sqrt{2/L}$ となります。

したがって，規格化された固有関数は，
$$
\finalanswer{y_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{(2n - 1)\pi x}{2L}\right)}
$$
となります。
===== FILE: 08differential_equations/04/04_050.md =====
---
tags:
  - 標準
---

# 固有関数の直交性と展開

## 問題
スツルム・リウビル型微分方程式
$$
\frac{d}{dx}\left( p(x) \frac{dy}{dx} \right) + q(x) y + \lambda r(x) y = 0 \quad (a \le x \le b)
$$
を考える。ここで $p(x) > 0, r(x) > 0$ である。両端固定条件 $y(a) = y(b) = 0$ を課す。以下の問いに答えよ。

(1) 相異なる固有値 $\lambda_m \neq \lambda_n$ に属する固有関数をそれぞれ $y_m(x), y_n(x)$ とする。部分積分を用いて，これらが重み関数 $r(x)$ に関して直交すること，すなわち
$$
\int_a^b r(x) y_m(x) y_n(x) \, dx = 0
$$
を示せ。

(2) $p(x) = 1, q(x) = 0, r(x) = 1$，$a = 0, b = \pi$ の場合の規格化固有関数系 $y_n(x) = \sqrt{\frac{2}{\pi}} \sin(nx)$ を用いて，関数 $f(x) = 1$ をフーリエ級数展開 $f(x) = \sum_{n=1}^\infty c_n y_n(x)$ するときの展開係数 $c_n$ を求めよ。

(3) (2)の展開式に $x = \pi/2$ を代入することにより，ライプニッツの公式 $\sum_{k=0}^\infty \frac{(-1)^k}{2k+1} = \frac{\pi}{4}$ を導け。

---

## 解答・解説

### (1)
2つの固有関数が満たす微分方程式を組み合わせ，ラグランジュの恒等式を積分します。

各関数の方程式は，
$$
\begin{aligned}
\frac{d}{dx}\left( p y_m' \right) + q y_m &= -\lambda_m r y_m \\
\frac{d}{dx}\left( p y_n' \right) + q y_n &= -\lambda_n r y_n
\end{aligned}
$$
です。第1式に $y_n$，第2式に $y_m$ を掛けて差をとると，
$$
\begin{aligned}
y_n \frac{d}{dx}\left( p y_m' \right) - y_m \frac{d}{dx}\left( p y_n' \right) &= (\lambda_n - \lambda_m) r y_m y_n
\end{aligned}
$$
となります。

左辺は完全微分 $\frac{d}{dx}\left[ p (y_m' y_n - y_m y_n') \right]$ と書き直せます。区間 $[a, b]$ で積分すると，
$$
\begin{aligned}
(\lambda_n - \lambda_m) \int_a^b r(x) y_m(x) y_n(x) \, dx &= \left[ p(x) \left( y_m'(x) y_n(x) - y_m(x) y_n'(x) \right) \right]_a^b
\end{aligned}
$$
となります。

境界条件 $y_m(a) = y_n(a) = 0$ および $y_m(b) = y_n(b) = 0$ により右辺の境界値は $0$ となります。

$\lambda_m \neq \lambda_n$ であるため，
$$
\finalanswer{\int_a^b r(x) y_m(x) y_n(x) \, dx = 0}
$$
となります。

### (2)
直交関係を利用して展開係数の積分を実行します。

係数 $c_n$ は内積より，
$$
\begin{aligned}
c_n &= \int_0^\pi f(x) y_n(x) \, dx \\
&= \sqrt{\frac{2}{\pi}} \int_0^\pi \sin(nx) \, dx \\
&= \sqrt{\frac{2}{\pi}} \left[ -\frac{\cos(nx)}{n} \right]_0^\pi \\
&= \sqrt{\frac{2}{\pi}} \frac{1 - (-1)^n}{n}
\end{aligned}
$$
となります。

$n$ が偶数のとき $c_n = 0$ であり，$n = 2k+1$（奇数）のとき分子は $2$ となります。

したがって，
$$
\finalanswer{c_n = \begin{cases} \sqrt{\frac{2}{\pi}} \frac{2}{n} & (n \text{ が奇数}) \\ 0 & (n \text{ が偶数}) \end{cases}}
$$
となります。

### (3)
得られた級数に $x = \pi/2$ を代入して値を評価します。

関数 $f(x) = 1$ の展開式を書き下すと，
$$
\begin{aligned}
1 &= \sum_{k=0}^\infty c_{2k+1} y_{2k+1}(x) \\
&= \sum_{k=0}^\infty \left( \sqrt{\frac{2}{\pi}} \frac{2}{2k+1} \right) \left( \sqrt{\frac{2}{\pi}} \sin\left((2k+1)x\right) \right) \\
&= \frac{4}{\pi} \sum_{k=0}^\infty \frac{\sin\left((2k+1)x\right)}{2k+1}
\end{aligned}
$$
となります。

$x = \pi/2$ を代入すると，$\sin\left((2k+1)\frac{\pi}{2}\right) = (-1)^k$ であるため，
$$
\begin{aligned}
1 &= \frac{4}{\pi} \sum_{k=0}^\infty \frac{(-1)^k}{2k+1}
\end{aligned}
$$
となります。

両辺に $\pi/4$ を掛けると，
$$
\finalanswer{\sum_{k=0}^\infty \frac{(-1)^k}{2k+1} = \frac{\pi}{4}}
$$
となります。
===== FILE: 08differential_equations/04/04_060.md =====
---
tags:
  - 発展
---

# 境界値問題のグリーン関数

## 問題
張力で張られた弦の微小なたわみ $y(x)$ を記述する境界値問題
$$
-\frac{d^2 y}{dx^2} = f(x) \quad (0 < x < L), \quad y(0) = 0, \quad y(L) = 0
$$
を考える。以下の問いに答えよ。

(1) グリーン関数 $G(x, \xi)$ が満たす方程式 $-\frac{d^2 G}{dx^2} = \delta(x - \xi)$ および境界条件のもとで，$x = \xi$ における連続条件と微係数の不連続性（跳び）の条件を式で表せ。

(2) $x < \xi$ および $x > \xi$ での方程式を解き，(1)の境界条件と接続条件をすべて用いてグリーン関数 $G(x, \xi)$ を求めよ。

(3) 一様な荷重 $f(x) = f_0$（正の定数）が作用するとき，積分 $y(x) = \int_0^L G(x, \xi) f(\xi) \, d\xi$ を計算してたわみ $y(x)$ を求めよ。

---

## 解答・解説

### (1)
デルタ関数を含む方程式を $x = \xi$ の微小近傍で積分して不連続条件を導きます。

$-\frac{d^2 G}{dx^2} = \delta(x - \xi)$ の両端を $\xi - \epsilon$ から $\xi + \epsilon$ まで積分し $\epsilon \to +0$ の極限をとると，
$$
\begin{aligned}
-\left[ \frac{dG}{dx} \right]_{\xi-0}^{\xi+0} &= \int_{\xi-0}^{\xi+0} \delta(x - \xi) \, dx = 1
\end{aligned}
$$
となります。

関数の連続性と合わせると，
$$
\finalanswer{G(\xi + 0, \xi) = G(\xi - 0, \xi), \quad \left.\frac{dG}{dx}\right|_{x = \xi + 0} - \left.\frac{dG}{dx}\right|_{x = \xi - 0} = -1}
$$
となります。

### (2)
各領域で直線の一般解を立て，境界条件と接続条件から未定係数を決定します。

$x \neq \xi$ では $\frac{d^2 G}{dx^2} = 0$ であるため，一次式となります。境界条件 $G(0, \xi) = 0$ および $G(L, \xi) = 0$ を考慮すると，
$$
G(x, \xi) = \begin{cases} A x & (0 \le x \le \xi) \\ B (L - x) & (\xi \le x \le L) \end{cases}
$$
とおくことができます。

$x = \xi$ における連続条件より，
$$
\begin{aligned}
A \xi &= B (L - \xi)
\end{aligned}
$$
となります。

微係数の跳びの条件より，
$$
\begin{aligned}
-B - A &= -1 \implies A + B = 1
\end{aligned}
$$
となります。

$B = 1 - A$ を連続性の式に代入すると，
$$
\begin{aligned}
A \xi &= (1 - A)(L - \xi) = L - \xi - AL + A\xi \\
AL &= L - \xi \\
A &= \frac{L - \xi}{L}
\end{aligned}
$$
となります。これより $B = \frac{\xi}{L}$ となります。

したがって，グリーン関数は，
$$
\finalanswer{G(x, \xi) = \begin{cases} \frac{x(L - \xi)}{L} & (x \le \xi) \\ \frac{\xi(L - x)}{L} & (x > \xi) \end{cases}}
$$
となります。$G(x, \xi) = G(\xi, x)$ の対称性が成り立ちます。

### (3)
グリーン関数を用いた積分を実行します。

積分の区間を $\xi = x$ で2つに分割すると，
$$
\begin{aligned}
y(x) &= f_0 \int_0^L G(x, \xi) \, d\xi \\
&= f_0 \left[ \int_0^x \frac{\xi(L - x)}{L} \, d\xi + \int_x^L \frac{x(L - \xi)}{L} \, d\xi \right]
\end{aligned}
$$
となります。

それぞれの積分を計算すると，
$$
\begin{aligned}
\int_0^x \xi \, d\xi &= \frac{x^2}{2} \\
\int_x^L (L - \xi) \, d\xi &= \left[ -\frac{(L - \xi)^2}{2} \right]_x^L = \frac{(L - x)^2}{2}
\end{aligned}
$$
となります。

代入して整理すると，
$$
\begin{aligned}
y(x) &= \frac{f_0}{L} \left[ \frac{(L - x) x^2}{2} + \frac{x (L - x)^2}{2} \right] \\
&= \frac{f_0 x (L - x)}{2L} \left[ x + (L - x) \right] \\
&= \frac{f_0 x (L - x)}{2L} \cdot L \\
&= \finalanswer{\frac{f_0}{2} x (L - x)}
\end{aligned}
$$
となります。直接微分して $-\frac{d^2 y}{dx^2} = f_0$ となることからも確かめられます。
===== FILE: 08differential_equations/05/05_010.md =====
---
tags:
  - 標準
---

# 1階偏微分方程式と特性曲線

## 問題
1次元の移流方程式
$$
\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = 0 \quad (-\infty < x < \infty, t > 0)
$$
を考える。ここで $c$ は正の定数である。以下の問いに答えよ。

(1) 特性曲線を定める微分方程式 $\frac{dx}{dt} = c$ を解き，その解曲線に沿って $u(x(t), t)$ が時間に関して一定であることを示せ。

(2) 初期条件 $u(x, 0) = f(x)$ が与えられたときの一般解 $u(x, t)$ を求めよ。

(3) 初期条件が $f(x) = \frac{1}{1 + x^2}$ のとき，時刻 $t$ における解 $u(x, t)$ を求め，波形の進行方向と速さを答えよ。

---

## 解答・解説

### (1)
合成関数の微分法を用いて特性曲線上の変化率を計算します。

微分方程式 $\frac{dx}{dt} = c$ を積分すると，特性曲線の式は，
$$
\begin{aligned}
x - ct = x_0 \quad (\text{一定})
\end{aligned}
$$
となります。

この曲線 $x(t) = ct + x_0$ に沿った $u(x(t), t)$ の全微分を計算すると，
$$
\begin{aligned}
\frac{d}{dt} u(x(t), t) &= \frac{\partial u}{\partial t} + \frac{\partial u}{\partial x} \frac{dx}{dt} \\
&= \frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x}
\end{aligned}
$$
となります。

与えられた移流方程式より右辺は $0$ となるため，
$$
\finalanswer{\frac{d}{dt} u(x(t), t) = 0}
$$
となり，特性曲線に沿って $u$ の値は保存されます。

### (2)
特性曲線に沿って初期値まで遡ることで解を表現します。

任意の点 $(x, t)$ を通る特性曲線は $x - ct = x_0$ であり，$t = 0$ における位置は $x_0 = x - ct$ です。

(1)より値は一定に保たれるため，
$$
\begin{aligned}
u(x, t) &= u(x_0, 0) \\
&= f(x_0)
\end{aligned}
$$
となります。

$x_0 = x - ct$ を代入すると，
$$
\finalanswer{u(x, t) = f(x - ct)}
$$
となります。

### (3)
具体的な初期関数に引数を代入し，波の伝播の様子を解釈します。

$f(x) = \frac{1}{1 + x^2}$ を代入すると，
$$
\finalanswer{u(x, t) = \frac{1}{1 + (x - ct)^2}}
$$
となります。

この解は初期の波形が形を変えずにそのまま進むことを表しており，進行方向と速さは，
$$
\finalanswer{x \text{ の正の向きに速さ } c}
$$
となります。
===== FILE: 08differential_equations/05/05_020.md =====
---
tags:
  - 基本
---

# 波動方程式とダランベールの解

## 問題
1次元の波動方程式
$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} \quad (-\infty < x < \infty, t > 0)
$$
を考える。ここで $c > 0$ である。以下の問いに答えよ。

(1) 新しい変数 $\xi = x - ct, \eta = x + ct$ を導入するとき，連鎖律を用いて方程式が $\frac{\partial^2 u}{\partial \xi \partial \eta} = 0$ と変換されることを示し，一般解が任意の2回微分可能な関数 $F, G$ を用いて $u(x, t) = F(x - ct) + G(x + ct)$ と表せることを示せ。

(2) 初期条件 $u(x, 0) = \phi(x)$，$\frac{\partial u}{\partial t}(x, 0) = \psi(x)$ を用いて関数 $F, G$ を決定し，ダランベールの公式
$$
u(x, t) = \frac{\phi(x - ct) + \phi(x + ct)}{2} + \frac{1}{2c} \int_{x - ct}^{x + ct} \psi(s) \, ds
$$
を導け。

(3) $\phi(x) = e^{-x^2}, \psi(x) = 0$ のときの解 $u(x, t)$ を求めよ。

---

## 解答・解説

### (1)
偏微分の連鎖律を2回適用して微分演算子を座標変換します。

1階微分を計算すると，
$$
\begin{aligned}
\frac{\partial}{\partial x} &= \frac{\partial\xi}{\partial x}\frac{\partial}{\partial\xi} + \frac{\partial\eta}{\partial x}\frac{\partial}{\partial\eta} = \frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta} \\
\frac{\partial}{\partial t} &= \frac{\partial\xi}{\partial t}\frac{\partial}{\partial\xi} + \frac{\partial\eta}{\partial t}\frac{\partial}{\partial\eta} = -c \frac{\partial}{\partial\xi} + c \frac{\partial}{\partial\eta}
\end{aligned}
$$
となります。

2階微分を計算すると，
$$
\begin{aligned}
\frac{\partial^2}{\partial x^2} &= \left(\frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta}\right)^2 = \frac{\partial^2}{\partial\xi^2} + 2\frac{\partial^2}{\partial\xi\partial\eta} + \frac{\partial^2}{\partial\eta^2} \\
\frac{\partial^2}{\partial t^2} &= c^2 \left(-\frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta}\right)^2 = c^2 \left(\frac{\partial^2}{\partial\xi^2} - 2\frac{\partial^2}{\partial\xi\partial\eta} + \frac{\partial^2}{\partial\eta^2}\right)
\end{aligned}
$$
となります。

波動方程式 $\frac{\partial^2 u}{\partial t^2} - c^2 \frac{\partial^2 u}{\partial x^2} = 0$ に代入すると，
$$
\begin{aligned}
-4c^2 \frac{\partial^2 u}{\partial\xi\partial\eta} &= 0 \implies \finalanswer{\frac{\partial^2 u}{\partial\xi\partial\eta} = 0}
\end{aligned}
$$
となります。

$\eta$ で積分すると $\frac{\partial u}{\partial\xi} = f(\xi)$ となり，さらに $\xi$ で積分すると，
$$
\finalanswer{u(x, t) = F(\xi) + G(\eta) = F(x - ct) + G(x + ct)}
$$
となります。

### (2)
初期条件を代入して $F$ と $G$ に関する連立方程式を解きます。

$t = 0$ における条件を立てると，
$$
\begin{aligned}
F(x) + G(x) &= \phi(x) \\
-c F'(x) + c G'(x) &= \psi(x) \implies -F'(x) + G'(x) = \frac{1}{c}\psi(x)
\end{aligned}
$$
となります。

第2式を $0$ から $x$ まで積分すると，
$$
\begin{aligned}
-F(x) + G(x) &= \frac{1}{c} \int_0^x \psi(s) \, ds + K
\end{aligned}
$$
となります。ここで $K$ は定数です。

和と差をとると，
$$
\begin{aligned}
G(x) &= \frac{1}{2}\phi(x) + \frac{1}{2c}\int_0^x \psi(s) \, ds + \frac{K}{2} \\
F(x) &= \frac{1}{2}\phi(x) - \frac{1}{2c}\int_0^x \psi(s) \, ds - \frac{K}{2}
\end{aligned}
$$
となります。

解 $u(x, t) = F(x - ct) + G(x + ct)$ に代入すると定数 $K$ は相殺され，
$$
\finalanswer{u(x, t) = \frac{\phi(x - ct) + \phi(x + ct)}{2} + \frac{1}{2c} \int_{x - ct}^{x + ct} \psi(s) \, ds}
$$
が得られます。

### (3)
与えられた初期関数をダランベールの公式に代入します。

$\psi(x) = 0$ より積分項は $0$ となります。$\phi(x) = e^{-x^2}$ を代入すると，
$$
\finalanswer{u(x, t) = \frac{1}{2}\left( e^{-(x - ct)^2} + e^{-(x + ct)^2} \right)}
$$
となります。初期の波形が振幅半分の2つのパルスに分裂し，互いに逆向きへ進行します。
===== FILE: 08differential_equations/05/05_030.md =====
---
tags:
  - 基本
---

# 弦の振動と変数分離

## 問題
両端が固定された長さ $L$ の弦の微小振動
$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} \quad (0 < x < L, t > 0)
$$
を考える。境界条件は $u(0, t) = 0, u(L, t) = 0$ である。以下の問いに答えよ。

(1) $u(x, t) = X(x) T(t)$ とおいて変数分離を行い，分離定数を $-\omega^2$（$\omega > 0$）とするとき，$X(x)$ および $T(t)$ が満たす常微分方程式を導け。

(2) 境界条件から固有角振動数 $\omega_n$ および対応する固有振動モード $u_n(x, t)$ を導け。

(3) 初期条件 $u(x, 0) = \sin\left(\frac{2\pi x}{L}\right)$，$\frac{\partial u}{\partial t}(x, 0) = 0$ を満たす解 $u(x, t)$ を求めよ。

---

## 解答・解説

### (1)
積の形の解を方程式に代入して両辺を変数ごとにまとめます。

$u(x, t) = X(x) T(t)$ を代入すると，
$$
\begin{aligned}
X(x) T''(t) &= c^2 X''(x) T(t)
\end{aligned}
$$
となります。

両辺を $c^2 X(x) T(t)$ で割ると，
$$
\begin{aligned}
\frac{T''(t)}{c^2 T(t)} &= \frac{X''(x)}{X(x)}
\end{aligned}
$$
となります。

左辺は $t$ のみ，右辺は $x$ のみの関数であるため，恒等的に定数でなければなりません。この定数を $-k^2 = -\frac{\omega^2}{c^2}$ とおくと，
$$
\finalanswer{X''(x) + \frac{\omega^2}{c^2} X(x) = 0, \quad T''(t) + \omega^2 T(t) = 0}
$$
が得られます。

### (2)
$X(x)$ の境界条件から離散的な固有値を決定します。

$X(x)$ の一般解は $X(x) = A \cos\left(\frac{\omega x}{c}\right) + B \sin\left(\frac{\omega x}{c}\right)$ です。$X(0) = 0$ より $A = 0$ です。

$X(L) = B \sin\left(\frac{\omega L}{c}\right) = 0$ より，非自明解をもつ条件は，
$$
\begin{aligned}
\frac{\omega_n L}{c} &= n\pi \implies \omega_n = \frac{n\pi c}{L} \quad (n = 1, 2, 3, \dots)
\end{aligned}
$$
となります。

$T(t)$ の一般解は $A_n \cos(\omega_n t) + B_n \sin(\omega_n t)$ です。

したがって，各固有モードは，
$$
\finalanswer{u_n(x, t) = \sin\left(\frac{n\pi x}{L}\right) \left[ A_n \cos\left(\frac{n\pi c t}{L}\right) + B_n \sin\left(\frac{n\pi c t}{L}\right) \right]}
$$
となります。

### (3)
与えられた初期条件と固有モードの展開を比較します。

一般解はモードの重ね合わせ $\sum_{n=1}^\infty u_n(x, t)$ です。初期速度 $\frac{\partial u}{\partial t}(x, 0) = 0$ より，すべての $n$ で $B_n = 0$ です。

初期変位の条件より，
$$
\begin{aligned}
u(x, 0) &= \sum_{n=1}^\infty A_n \sin\left(\frac{n\pi x}{L}\right) = \sin\left(\frac{2\pi x}{L}\right)
\end{aligned}
$$
となります。

基底の直交性により係数を比較すると，$n = 2$ のとき $A_2 = 1$ であり，それ以外の $n$ では $A_n = 0$ となります。

したがって，求める解は，
$$
\finalanswer{u(x, t) = \sin\left(\frac{2\pi x}{L}\right) \cos\left(\frac{2\pi c t}{L}\right)}
$$
となります。第2高調波（節が中央に1つある定在波）のみが励起された単一モードの振動となります。
===== FILE: 08differential_equations/05/05_040.md =====
---
tags:
  - 標準
---

# 熱伝導方程式と変数分離

## 問題
長さ $L$ の一様な棒における1次元の熱伝導方程式
$$
\frac{\partial u}{\partial t} = \kappa \frac{\partial^2 u}{\partial x^2} \quad (0 < x < L, t > 0)
$$
を考える。ここで熱拡散率は $\kappa > 0$ である。両端の温度は $0$ に保持されているとする（$u(0, t) = 0, u(L, t) = 0$）。以下の問いに答えよ。

(1) $u(x, t) = X(x) T(t)$ とおいて変数分離を行い，境界条件を満たす $X_n(x)$ および $T_n(t)$ を求めよ。

(2) 重ね合わせの原理を用いて，一般解の級数表示を導け。

(3) 初期温度分布が $u(x, 0) = u_0 \sin\left(\frac{\pi x}{L}\right)$（$u_0 > 0$）であるとき，解 $u(x, t)$ を求め，棒の中央 $x = L/2$ の温度が初期値の $1/e$ に減衰する時刻 $t_1$ を求めよ。

---

## 解答・解説

### (1)
変数分離法を適用し，空間境界条件から固有値を決定します。

$u(x, t) = X(x) T(t)$ を代入して両辺を $\kappa X T$ で割ると，
$$
\begin{aligned}
\frac{T'(t)}{\kappa T(t)} &= \frac{X''(x)}{X(x)} = -\lambda
\end{aligned}
$$
となります。

$X''(x) + \lambda X(x) = 0$ に境界条件 $X(0) = X(L) = 0$ を課すと，$\lambda_n = \left(\frac{n\pi}{L}\right)^2$（$n = 1, 2, \dots$）および，
$$
X_n(x) = \sin\left(\frac{n\pi x}{L}\right)
$$
が得られます。

時間微分の方程式 $T_n'(t) = -\kappa \lambda_n T_n(t)$ を解くと，
$$
T_n(t) = e^{-\kappa (n\pi/L)^2 t}
$$
となります。

したがって，
$$
\finalanswer{X_n(x) = \sin\left(\frac{n\pi x}{L}\right), \quad T_n(t) = e^{-\kappa (n\pi/L)^2 t} \quad (n = 1, 2, 3, \dots)}
$$
となります。

### (2)
線形微分方程式の解の線形結合を構成します。

各分離解 $X_n(x) T_n(t)$ の任意の線形結合が解となるため，
$$
\finalanswer{u(x, t) = \sum_{n=1}^\infty c_n \sin\left(\frac{n\pi x}{L}\right) e^{-\kappa \left(\frac{n\pi}{L}\right)^2 t}}
$$
となります。ここで $c_n$ は初期条件によって決定される展開係数です。

### (3)
初期条件と級数を比較して解を特定し，温度が $1/e$ になる条件を解きます。

$t = 0$ において，
$$
\begin{aligned}
u(x, 0) &= \sum_{n=1}^\infty c_n \sin\left(\frac{n\pi x}{L}\right) = u_0 \sin\left(\frac{\pi x}{L}\right)
\end{aligned}
$$
となります。係数を比較すると $c_1 = u_0$，$c_n = 0$（$n \ge 2$）です。

したがって，温度分布は，
$$
\finalanswer{u(x, t) = u_0 \sin\left(\frac{\pi x}{L}\right) e^{-\kappa \left(\frac{\pi}{L}\right)^2 t}}
$$
となります。

棒の中央 $x = L/2$ では $\sin(\pi/2) = 1$ であるため，$u(L/2, t) = u_0 e^{-\kappa (\pi/L)^2 t}$ となります。

この温度が $u_0/e = u_0 e^{-1}$ に等しくなる条件は，
$$
\begin{aligned}
\kappa \left(\frac{\pi}{L}\right)^2 t_1 &= 1
\end{aligned}
$$
となります。

したがって，求める時刻は，
$$
\finalanswer{t_1 = \frac{L^2}{\pi^2 \kappa}}
$$
となります。拡散による緩和時間は棒の長さの二乗に比例します。
===== FILE: 08differential_equations/05/05_050.md =====
---
tags:
  - 標準
---

# 長方形領域のラプラス方程式

## 問題
長方形領域 $0 < x < a, 0 < y < b$ における静電ポテンシャルのラプラス方程式
$$
\frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = 0
$$
を考える。境界条件は
$$
\phi(0, y) = 0, \quad \phi(a, y) = 0, \quad \phi(x, 0) = 0, \quad \phi(x, b) = V_0 \sin\left(\frac{\pi x}{a}\right)
$$
である。ここで $V_0$ は正の定数である。以下の問いに答えよ。

(1) $\phi(x, y) = X(x) Y(y)$ とおいて変数分離を行い，$X(x)$ の境界条件 $X(0) = X(a) = 0$ から固有関数 $X_n(x)$ を求めよ。

(2) $Y(y)$ が満たす微分方程式と境界条件 $Y(0) = 0$ から，各モードに対する $Y_n(y)$ の関数形を双曲線関数を用いて表せ。

(3) 境界条件 $\phi(x, b) = V_0 \sin\left(\frac{\pi x}{a}\right)$ を満たすポテンシャル分布 $\phi(x, y)$ を求めよ。

---

## 解答・解説

### (1)
変数分離を行い，斉次境界条件をもつ $x$ 方向の固有値問題を解きます。

$\phi(x, y) = X(x) Y(y)$ を代入して両辺を $X Y$ で割ると，
$$
\begin{aligned}
\frac{X''(x)}{X(x)} + \frac{Y''(y)}{Y(y)} &= 0 \implies \frac{X''(x)}{X(x)} = -\frac{Y''(y)}{Y(y)} = -k^2
\end{aligned}
$$
となります。

$X$ についての方程式は $X''(x) + k^2 X(x) = 0$ となり，一般解は $X(x) = A \cos(kx) + B \sin(kx)$ です。

境界条件 $X(0) = 0$ より $A = 0$ です。また $X(a) = B \sin(ka) = 0$ より，非自明解をもつ条件は，
$$
\begin{aligned}
k_n &= \frac{n\pi}{a} \quad (n = 1, 2, 3, \dots)
\end{aligned}
$$
となります。

したがって，固有関数は，
$$
\finalanswer{X_n(x) = \sin\left(\frac{n\pi x}{a}\right) \quad (n = 1, 2, 3, \dots)}
$$
となります。

### (2)
$Y(y)$ の方程式を解き，$y = 0$ での境界条件を適用します。

$Y$ についての方程式は，
$$
\begin{aligned}
Y_n''(y) - k_n^2 Y_n(y) &= 0
\end{aligned}
$$
となります。

一般解は双曲線関数を用いて，
$$
\begin{aligned}
Y_n(y) &= C_n \cosh(k_n y) + D_n \sinh(k_n y)
\end{aligned}
$$
と表されます。

境界条件 $Y_n(0) = 0$ より $\cosh(0) = 1, \sinh(0) = 0$ であるため $C_n = 0$ となります。

したがって，求める関数形は，
$$
\finalanswer{Y_n(y) = D_n \sinh\left(\frac{n\pi y}{a}\right)}
$$
となります。

### (3)
重ね合わせの級数を作り，$y = b$ の境界条件から係数を決定します。

一般解は，
$$
\begin{aligned}
\phi(x, y) &= \sum_{n=1}^\infty D_n \sin\left(\frac{n\pi x}{a}\right) \sinh\left(\frac{n\pi y}{a}\right)
\end{aligned}
$$
です。$y = b$ を代入すると，
$$
\begin{aligned}
\phi(x, b) &= \sum_{n=1}^\infty D_n \sinh\left(\frac{n\pi b}{a}\right) \sin\left(\frac{n\pi x}{a}\right) = V_0 \sin\left(\frac{\pi x}{a}\right)
\end{aligned}
$$
となります。

両辺の係数を比較すると，$n = 1$ の項のみが存在するため，
$$
\begin{aligned}
D_1 \sinh\left(\frac{\pi b}{a}\right) &= V_0 \implies D_1 = \frac{V_0}{\sinh\left(\frac{\pi b}{a}\right)}
\end{aligned}
$$
となり，$n \ge 2$ では $D_n = 0$ です。

したがって，電位分布は，
$$
\finalanswer{\phi(x, y) = V_0 \frac{\sinh\left(\frac{\pi y}{a}\right)}{\sinh\left(\frac{\pi b}{a}\right)} \sin\left(\frac{\pi x}{a}\right)}
$$
となります。
===== FILE: 08differential_equations/05/05_060.md =====
---
tags:
  - 標準
---

# 偏微分方程式の分類

## 問題
2変数の2階線形偏微分方程式
$$
A \frac{\partial^2 u}{\partial x^2} + 2B \frac{\partial^2 u}{\partial x \partial y} + C \frac{\partial^2 u}{\partial y^2} + D \frac{\partial u}{\partial x} + E \frac{\partial u}{\partial y} + F u = 0
$$
を考える。主部の係数から定まる判別式を $\Delta = B^2 - AC$ とする。以下の問いに答えよ。

(1) 判別式の符号 $\Delta > 0, \Delta = 0, \Delta < 0$ に応じて，偏微分方程式がそれぞれどの型（双曲型，放物型，楕円型）に分類されるか答えよ。

(2) 1次元波動方程式 $\frac{\partial^2 u}{\partial t^2} - c^2 \frac{\partial^2 u}{\partial x^2} = 0$，1次元熱伝導方程式 $\frac{\partial u}{\partial t} - \kappa \frac{\partial^2 u}{\partial x^2} = 0$，および2次元ラプラス方程式 $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ の型をそれぞれ判定せよ。

(3) トリコミの方程式 $y \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ について，$y > 0, y = 0, y < 0$ の各領域における分類を答えよ。

---

## 解答・解説

### (1)
二次曲線の分類との対応に基づいて判別式の符号による分類を定義します。

特性曲線の微分方程式 $A (dy)^2 - 2B dx dy + C (dx)^2 = 0$ の根の性質に対応して分類されます。

したがって，各符号に対する分類は，
$$
\finalanswer{\Delta > 0 : \text{双曲型}, \quad \Delta = 0 : \text{放物型}, \quad \Delta < 0 : \text{楕円型}}
$$
となります。

### (2)
物理の代表的な各方程式について係数 $A, B, C$ を読み取り，判別式を計算します。

波動方程式について，独立変数を $(t, x)$ とすると，$u_{tt} - c^2 u_{xx} = 0$ より $A = 1, B = 0, C = -c^2$ です。判別式は，
$$
\begin{aligned}
\Delta &= 0^2 - 1(-c^2) = c^2 > 0
\end{aligned}
$$
となり，双曲型です。

熱伝導方程式について，独立変数を $(t, x)$ とすると，2階微分は $u_{xx}$ のみであるため $A = 0, B = 0, C = -\kappa$（または $u_{tt}$ の係数が $0$）です。判別式は，
$$
\begin{aligned}
\Delta &= 0^2 - 0 \cdot (-\kappa) = 0
\end{aligned}
$$
となり，放物型です。

ラプラス方程式について，独立変数を $(x, y)$ とすると，$A = 1, B = 0, C = 1$ です。判別式は，
$$
\begin{aligned}
\Delta &= 0^2 - 1 \cdot 1 = -1 < 0
\end{aligned}
$$
となり，楕円型です。

したがって，
$$
\finalanswer{\text{波動方程式 : 双曲型}, \quad \text{熱伝導方程式 : 放物型}, \quad \text{ラプラス方程式 : 楕円型}}
$$
となります。

### (3)
トリコミ方程式の係数を同定し，$y$ の値による符号変化を調べます。

方程式 $y u_{xx} + u_{yy} = 0$ において，係数は $A = y, B = 0, C = 1$ です。

判別式を計算すると，
$$
\begin{aligned}
\Delta &= B^2 - AC = 0^2 - y \cdot 1 = -y
\end{aligned}
$$
となります。

したがって，領域ごとの分類は，
$$
\begin{aligned}
y > 0 \text{ のとき} \quad \Delta < 0 \\
y = 0 \text{ のとき} \quad \Delta = 0 \\
y < 0 \text{ のとき} \quad \Delta > 0
\end{aligned}
$$
となります。

よって，
$$
\finalanswer{y > 0 : \text{楕円型}, \quad y = 0 : \text{放物型}, \quad y < 0 : \text{双曲型}}
$$
となります。この方程式は遷音速流（亜音速領域と超音速領域の遷移）の解析に応用されます。
===== FILE: 08differential_equations/06/06_010.md =====
---
tags:
  - 標準
---

# 円形領域のラプラス方程式

## 問題
半径 $R$ の円板領域 $r < R$ における2次元ラプラス方程式
$$
\frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2} = 0 \quad (0 \le r < R, -\pi < \theta \le \pi)
$$
を考える。以下の問いに答えよ。

(1) $u(r, \theta) = R_r(r) \Theta(\theta)$ と変数分離し，$\Theta$ に関する周期境界条件 $\Theta(\theta + 2\pi) = \Theta(\theta)$ から分離定数を決定せよ。

(2) 原点 $r = 0$ において解が有限にとどまる（正則である）条件を用いて，動径方向の関数 $R_n(r)$ を求めよ。

(3) 円周境界上の条件が $u(R, \theta) = V_0 \cos(2\theta)$（$V_0$ は定数）で与えられるとき，円板内部の解 $u(r, \theta)$ を求めよ。

---

## 解答・解説

### (1)
変数分離を行い，角度方向の常微分方程式に周期性を課します。

$u = R_r(r)\Theta(\theta)$ を代入して $r^2/(R_r\Theta)$ を掛けると，
$$
\begin{aligned}
\frac{r^2 R_r''(r) + r R_r'(r)}{R_r(r)} &= -\frac{\Theta''(\theta)}{\Theta(\theta)} = \lambda
\end{aligned}
$$
となります。

$\Theta'' + \lambda \Theta = 0$ の周期解が存在するためには $\lambda = n^2$（$n = 0, 1, 2, \dots$）が必要です。

一般解は，
$$
\begin{aligned}
\Theta_n(\theta) &= A_n \cos(n\theta) + B_n \sin(n\theta)
\end{aligned}
$$
となります。

したがって，分離定数は，
$$
\finalanswer{\lambda = n^2 \quad (n = 0, 1, 2, \dots)}
$$
となります。

### (2)
動径方向のオイラー型方程式を解き，原点での特異性を除外します。

動径方向の方程式は，
$$
\begin{aligned}
r^2 R_r'' + r R_r' - n^2 R_r &= 0
\end{aligned}
$$
となります。解を $R_r(r) = r^m$ と仮定すると，$m(m-1) + m - n^2 = m^2 - n^2 = 0$ となり，$m = \pm n$ です。

$n = 0$ のとき，一般解は $R_0(r) = C_0 + D_0 \ln r$ です。$r \to 0$ で $\ln r \to -\infty$ と発散するため，$D_0 = 0$ です。

$n \ge 1$ のとき，一般解は $R_n(r) = C_n r^n + D_n r^{-n}$ です。$r \to 0$ で $r^{-n} \to \infty$ と発散するため，$D_n = 0$ です。

したがって，正則な動径解は，
$$
\finalanswer{R_n(r) = C_n r^n \quad (n = 0, 1, 2, \dots)}
$$
となります。

### (3)
級数解の境界値と与えられた境界条件を比較します。

領域内部の一般解は，
$$
\begin{aligned}
u(r, \theta) &= \frac{A_0}{2} + \sum_{n=1}^\infty r^n \left( A_n \cos(n\theta) + B_n \sin(n\theta) \right)
\end{aligned}
$$
です。

境界 $r = R$ を代入すると，
$$
\begin{aligned}
u(R, \theta) &= \frac{A_0}{2} + \sum_{n=1}^\infty R^n \left( A_n \cos(n\theta) + B_n \sin(n\theta) \right) = V_0 \cos(2\theta)
\end{aligned}
$$
となります。

係数を比較すると，$n = 2$ の余弦項のみが非ゼロであり，
$$
\begin{aligned}
R^2 A_2 &= V_0 \implies A_2 = \frac{V_0}{R^2}
\end{aligned}
$$
となり，他の係数はすべて $0$ です。

したがって，求める解は，
$$
\finalanswer{u(r, \theta) = V_0 \left(\frac{r}{R}\right)^2 \cos(2\theta)}
$$
となります。
===== FILE: 08differential_equations/06/06_020.md =====
---
tags:
  - 発展
---

# 球座標のラプラス方程式と軸対称解

## 問題
3次元球座標 $(r, \theta, \phi)$ において，方位角 $\phi$ に依存しない軸対称な静電ポテンシャル $\Phi(r, \theta)$ が満たすラプラス方程式
$$
\frac{1}{r^2} \frac{\partial}{\partial r}\left( r^2 \frac{\partial \Phi}{\partial r} \right) + \frac{1}{r^2 \sin\theta} \frac{\partial}{\partial \theta}\left( \sin\theta \frac{\partial \Phi}{\partial \theta} \right) = 0
$$
を考える。以下の問いに答えよ。

(1) $\Phi(r, \theta) = R(r) \Theta(\theta)$ と変数分離し，$\mu = \cos\theta$ と変数変換することで，$\Theta$ がルジャンドルの微分方程式を満たすことを示せ。

(2) 分離定数を $l(l+1)$（$l$ は非負整数）とするとき，球の外部領域 $r \ge a$ において無限遠で $\Phi \to 0$ となる解の一般形が
$$
\Phi(r, \theta) = \sum_{l=0}^\infty \frac{B_l}{r^{l+1}} P_l(\cos\theta)
$$
と表せることを示せ。

(3) 球面 $r = a$ 上の電位が $\Phi(a, \theta) = V_0 \cos\theta$（$V_0$ は定数）で与えられるとき，外部領域 $r \ge a$ の電位 $\Phi(r, \theta)$ を求めよ。

---

## 解答・解説

### (1)
方程式に変数分離形を代入して分離定数を導入し，角度部分を $\mu = \cos\theta$ で書き換えます。

$\Phi = R(r)\Theta(\theta)$ を代入して $r^2/(R\Theta)$ を掛けると，
$$
\begin{aligned}
\frac{1}{R} \frac{d}{dr}\left( r^2 \frac{dR}{dr} \right) &= -\frac{1}{\Theta \sin\theta} \frac{d}{d\theta}\left( \sin\theta \frac{d\Theta}{d\theta} \right) = \lambda
\end{aligned}
$$
となります。

角度成分の方程式において $\mu = \cos\theta$ とおくと，$\frac{d}{d\theta} = -\sin\theta \frac{d}{d\mu}$ および $\sin^2\theta = 1 - \mu^2$ です。

代入すると，
$$
\begin{aligned}
-\frac{1}{\sin\theta} \left( -\sin\theta \frac{d}{d\mu} \right) \left[ \sin\theta \left( -\sin\theta \frac{d\Theta}{d\mu} \right) \right] &= \lambda \Theta \\
\frac{d}{d\mu}\left[ (1 - \mu^2) \frac{d\Theta}{d\mu} \right] + \lambda \Theta &= 0
\end{aligned}
$$
となります。

展開すると，
$$
\finalanswer{(1 - \mu^2) \frac{d^2 \Theta}{d\mu^2} - 2\mu \frac{d\Theta}{d\mu} + \lambda \Theta = 0}
$$
となり，ルジャンドル方程式が得られます。

### (2)
動径方向の方程式を解き，無限遠での境界条件を課します。

極での正則性から $\lambda = l(l+1)$（$l = 0, 1, 2, \dots$）であり，$\Theta(\theta) = P_l(\cos\theta)$ です。

動径方程式は，
$$
\begin{aligned}
\frac{d}{dr}\left( r^2 \frac{dR}{dr} \right) - l(l+1) R &= 0 \\
r^2 R'' + 2r R' - l(l+1) R &= 0
\end{aligned}
$$
となります。解を $R(r) = r^k$ と仮定すると，$k(k-1) + 2k - l(l+1) = k(k+1) - l(l+1) = 0$ となり，$k = l$ または $k = -(l+1)$ です。

外部領域 $r \to \infty$ で $\Phi \to 0$ となるためには，$r^l$（$l \ge 0$）の項は発散するため係数は $0$ でなければなりません。

したがって，許される動径解は $R_l(r) = B_l r^{-(l+1)}$ となり，重ね合わせると，
$$
\finalanswer{\Phi(r, \theta) = \sum_{l=0}^\infty \frac{B_l}{r^{l+1}} P_l(\cos\theta)}
$$
となります。

### (3)
球面上の境界条件と級数展開を比較します。

$P_1(\cos\theta) = \cos\theta$ であるため，境界条件は $\Phi(a, \theta) = V_0 P_1(\cos\theta)$ と表されます。

級数解に $r = a$ を代入すると，
$$
\begin{aligned}
\Phi(a, \theta) &= \sum_{l=0}^\infty \frac{B_l}{a^{l+1}} P_l(\cos\theta) = V_0 P_1(\cos\theta)
\end{aligned}
$$
となります。

ルジャンドル多項式の直交性により係数を比較すると，$l = 1$ の項のみが存在し，
$$
\begin{aligned}
\frac{B_1}{a^2} &= V_0 \implies B_1 = V_0 a^2
\end{aligned}
$$
となり，$l \neq 1$ では $B_l = 0$ です。

したがって，外部電位は，
$$
\finalanswer{\Phi(r, \theta) = V_0 \frac{a^2}{r^2} \cos\theta}
$$
となります。電気双極子による電位分布と一致します。
===== FILE: 08differential_equations/06/06_030.md =====
---
tags:
  - 標準
---

# 熱核と無限長の熱伝導

## 問題
無限に長い直線路 $-\infty < x < \infty$ における熱伝導方程式
$$
\frac{\partial u}{\partial t} = \kappa \frac{\partial^2 u}{\partial x^2} \quad (-\infty < x < \infty, t > 0)
$$
を考える。ここで $\kappa > 0$ である。以下の問いに答えよ。

(1) 空間変数 $x$ についてフーリエ変換 $\hat{u}(k, t) = \int_{-\infty}^\infty u(x, t) e^{-ikx} \, dx$ を行うとき，$\hat{u}(k, t)$ が満たす常微分方程式とその解を求めよ。

(2) 初期条件がデルタ関数 $u(x, 0) = \delta(x)$ で与えられるとき，フーリエ逆変換を用いて基本解（熱核）
$$
K(x, t) = \frac{1}{\sqrt{4\pi\kappa t}} \exp\left(-\frac{x^2}{4\kappa t}\right)
$$
を導け。必要であればガウス積分 $\int_{-\infty}^\infty e^{-a k^2 + i b k} \, dk = \sqrt{\frac{\pi}{a}} e^{-b^2/(4a)}$（$a > 0$）を用いよ。

(3) 一般の初期条件 $u(x, 0) = f(x)$ に対する解が，熱核とのたたみ込み $u(x, t) = \int_{-\infty}^\infty K(x - \xi, t) f(\xi) \, d\xi$ で表されることを示せ。

---

## 解答・解説

### (1)
偏微分方程式にフーリエ変換を適用し，空間微分を波数 $k$ の代数演算に変換します。

部分積分を用いて空間微分のフーリエ変換を計算すると，
$$
\begin{aligned}
\int_{-\infty}^\infty \frac{\partial^2 u}{\partial x^2} e^{-ikx} \, dx &= (ik)^2 \hat{u}(k, t) = -k^2 \hat{u}(k, t)
\end{aligned}
$$
となります。

したがって，フーリエ変換された方程式は，
$$
\begin{aligned}
\frac{d\hat{u}}{dt} &= -\kappa k^2 \hat{u}
\end{aligned}
$$
となります。

この1階微分方程式を解くと，
$$
\finalanswer{\frac{d\hat{u}}{dt} = -\kappa k^2 \hat{u}, \quad \hat{u}(k, t) = \hat{u}(k, 0) e^{-\kappa k^2 t}}
$$
となります。

### (2)
デルタ関数のフーリエ変換を求め，逆フーリエ変換の積分を実行します。

初期条件 $u(x, 0) = \delta(x)$ のフーリエ変換は，
$$
\begin{aligned}
\hat{u}(k, 0) &= \int_{-\infty}^\infty \delta(x) e^{-ikx} \, dx = 1
\end{aligned}
$$
となります。したがって $\hat{u}(k, t) = e^{-\kappa k^2 t}$ です。

フーリエ逆変換を計算すると，
$$
\begin{aligned}
K(x, t) &= \frac{1}{2\pi} \int_{-\infty}^\infty \hat{u}(k, t) e^{ikx} \, dk \\
&= \frac{1}{2\pi} \int_{-\infty}^\infty e^{-\kappa t k^2 + ikx} \, dk
\end{aligned}
$$
となります。

与えられたガウス積分の公式において $a = \kappa t, b = x$ を適用すると，
$$
\begin{aligned}
K(x, t) &= \frac{1}{2\pi} \sqrt{\frac{\pi}{\kappa t}} \exp\left(-\frac{x^2}{4\kappa t}\right) \\
&= \finalanswer{\frac{1}{\sqrt{4\pi\kappa t}} \exp\left(-\frac{x^2}{4\kappa t}\right)}
\end{aligned}
$$
が得られます。

### (3)
線形性と重ね合わせを用いて一般解を積分表示します。

任意の初期条件 $f(x)$ は，デルタ関数を用いて $f(x) = \int_{-\infty}^\infty f(\xi) \delta(x - \xi) \, d\xi$ と表せます。

熱伝導方程式は線形かつ空間並進不変であるため，初期条件 $\delta(x - \xi)$ に対する解は $K(x - \xi, t)$ となります。

解の重ね合わせの原理を適用すると，
$$
\begin{aligned}
u(x, t) &= \int_{-\infty}^\infty f(\xi) K(x - \xi, t) \, d\xi
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{u(x, t) = \int_{-\infty}^\infty K(x - \xi, t) f(\xi) \, d\xi}
$$
となります。
===== FILE: 08differential_equations/06/06_040.md =====
---
tags:
  - 標準
---

# 非斉次の境界条件

## 問題
長さ $L$ の一様な棒における熱伝導方程式
$$
\frac{\partial u}{\partial t} = \kappa \frac{\partial^2 u}{\partial x^2} \quad (0 < x < L, t > 0)
$$
を考える。両端の温度は異なる一定値 $u(0, t) = T_1, u(L, t) = T_2$ に保持されている。以下の問いに答えよ。

(1) 時間に依存しない定常温度分布 $u_{\text{s}}(x)$ を境界条件を満たすように求めよ。

(2) $v(x, t) = u(x, t) - u_{\text{s}}(x)$ と定義するとき，$v(x, t)$ が満たす熱伝導方程式および境界条件を導け。

(3) 初期の温度分布が $u(x, 0) = 0$ であるとき，解 $u(x, t)$ の級数展開表示を求めよ。

---

## 解答・解説

### (1)
時間微分を $0$ とおいて常微分方程式を解きます。

定常状態では $\frac{\partial u_{\text{s}}}{\partial t} = 0$ であるため，
$$
\begin{aligned}
\frac{d^2 u_{\text{s}}}{dx^2} &= 0
\end{aligned}
$$
となります。

一般解は一次関数 $u_{\text{s}}(x) = A x + B$ です。境界条件 $u_{\text{s}}(0) = T_1$ より $B = T_1$ です。

$u_{\text{s}}(L) = A L + T_1 = T_2$ より，$A = \frac{T_2 - T_1}{L}$ となります。

したがって，定常解は，
$$
\finalanswer{u_{\text{s}}(x) = T_1 + \frac{T_2 - T_1}{L} x}
$$
となります。

### (2)
偏差関数 $v(x, t)$ の満たす方程式と境界条件を計算します。

$u(x, t) = v(x, t) + u_{\text{s}}(x)$ を熱伝導方程式に代入すると，
$$
\begin{aligned}
\frac{\partial v}{\partial t} + 0 &= \kappa \left( \frac{\partial^2 v}{\partial x^2} + \frac{d^2 u_{\text{s}}}{dx^2} \right) \\
\frac{\partial v}{\partial t} &= \kappa \frac{\partial^2 v}{\partial x^2}
\end{aligned}
$$
となります。

両端の境界条件を計算すると，
$$
\begin{aligned}
v(0, t) &= u(0, t) - u_{\text{s}}(0) = T_1 - T_1 = 0 \\
v(L, t) &= u(L, t) - u_{\text{s}}(L) = T_2 - T_2 = 0
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{\frac{\partial v}{\partial t} = \kappa \frac{\partial^2 v}{\partial x^2}, \quad v(0, t) = 0, \quad v(L, t) = 0}
$$
となり，境界条件が斉次化されます。

### (3)
$v(x, t)$ をフーリエ・サイン級数で解き，定常解と足し合わせます。

斉次境界条件を満たす $v(x, t)$ の一般解は，
$$
\begin{aligned}
v(x, t) &= \sum_{n=1}^\infty c_n \sin\left(\frac{n\pi x}{L}\right) e^{-\kappa (n\pi/L)^2 t}
\end{aligned}
$$
です。初期条件は $v(x, 0) = 0 - u_{\text{s}}(x) = -u_{\text{s}}(x)$ となります。

展開係数 $c_n$ を計算すると，
$$
\begin{aligned}
c_n &= \frac{2}{L} \int_0^L \left[ -T_1 - \frac{T_2 - T_1}{L} x \right] \sin\left(\frac{n\pi x}{L}\right) \, dx
\end{aligned}
$$
となります。部分積分を実行すると，
$$
\begin{aligned}
c_n &= \frac{2}{n\pi} \left[ (-1)^n T_2 - T_1 \right]
\end{aligned}
$$
が得られます。

したがって，全体の解は，
$$
\finalanswer{u(x, t) = T_1 + \frac{T_2 - T_1}{L} x + \sum_{n=1}^\infty \frac{2}{n\pi} \left[ (-1)^n T_2 - T_1 \right] \sin\left(\frac{n\pi x}{L}\right) e^{-\kappa \left(\frac{n\pi}{L}\right)^2 t}}
$$
となります。時間が経過すると $t \to \infty$ で指数減衰項が消失し，定常分布 $u_{\text{s}}(x)$ に漸近します。
===== FILE: 08differential_equations/06/06_050.md =====
---
tags:
  - 発展
---

# 円形膜の振動

## 問題
半径 $a$ の円形膜の軸対称（$\theta$ に依存しない）微小振動
$$
\frac{\partial^2 u}{\partial t^2} = c^2 \left( \frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} \right) \quad (0 \le r < a, t > 0)
$$
を考える。境界条件は固定端 $u(a, t) = 0$ であり，膜の中心 $r = 0$ で変位は有限である。以下の問いに答えよ。

(1) 単振動解 $u(r, t) = R(r) \cos(\omega t)$ を仮定し，$z = \frac{\omega r}{c}$ と変数変換するとき，$R$ が0次のベッセル微分方程式
$$
\frac{d^2 R}{dz^2} + \frac{1}{z}\frac{dR}{dz} + R = 0
$$
を満たすことを示せ。

(2) 中心で有限な解 $R(r) = J_0\left(\frac{\omega r}{c}\right)$ に対し，固定端条件から固有角振動数 $\omega_n$ を $J_0(z)$ の正の零点 $\alpha_n$（$J_0(\alpha_n) = 0, n = 1, 2, \dots$）を用いて表せ。

(3) 基本振動モード（$n = 1$）の固有角振動数 $\omega_1$ を $c, a, \alpha_1$ を用いて表せ。

---

## 解答・解説

### (1)
解を方程式に代入し，連鎖律を用いて無次元変数 $z$ で書き直します。

$u(r, t) = R(r)\cos(\omega t)$ を代入すると，
$$
\begin{aligned}
-\omega^2 R \cos(\omega t) &= c^2 \left( \frac{d^2 R}{dr^2} + \frac{1}{r}\frac{dR}{dr} \right) \cos(\omega t)
\end{aligned}
$$
となります。両辺を $c^2 \cos(\omega t)$ で割ると，
$$
\begin{aligned}
\frac{d^2 R}{dr^2} + \frac{1}{r}\frac{dR}{dr} + \frac{\omega^2}{c^2} R &= 0
\end{aligned}
$$
となります。

$z = \frac{\omega r}{c}$ とおくと，$\frac{d}{dr} = \frac{\omega}{c}\frac{d}{dz}$，$\frac{d^2}{dr^2} = \frac{\omega^2}{c^2}\frac{d^2}{dz^2}$ です。

代入すると，
$$
\begin{aligned}
\frac{\omega^2}{c^2} \frac{d^2 R}{dz^2} + \frac{1}{\frac{c}{\omega} z} \frac{\omega}{c} \frac{dR}{dz} + \frac{\omega^2}{c^2} R &= 0 \\
\frac{\omega^2}{c^2} \left( \frac{d^2 R}{dz^2} + \frac{1}{z}\frac{dR}{dz} + R \right) &= 0
\end{aligned}
$$
となります。

両辺を $\frac{\omega^2}{c^2}$ で割ると，
$$
\finalanswer{\frac{d^2 R}{dz^2} + \frac{1}{z}\frac{dR}{dz} + R = 0}
$$
が得られます。

### (2)
第1種ベッセル関数に境界条件を課して固有値を決定します。

0次ベッセル方程式の一般解は $R(z) = C_1 J_0(z) + C_2 Y_0(z)$ です。$z \to 0$ で第2種ベッセル関数は $Y_0(z) \to -\infty$ と発散するため，原点での正則性より $C_2 = 0$ です。

したがって $R(r) = J_0\left(\frac{\omega r}{c}\right)$ です。

境界 $r = a$ において固定端条件を課すと，
$$
\begin{aligned}
J_0\left(\frac{\omega a}{c}\right) &= 0
\end{aligned}
$$
となります。

$J_0$ の零点を小さい順に $\alpha_1, \alpha_2, \dots$ とすると，
$$
\begin{aligned}
\frac{\omega_n a}{c} &= \alpha_n
\end{aligned}
$$
となります。

したがって，固有角振動数は，
$$
\finalanswer{\omega_n = \frac{c \alpha_n}{a} \quad (n = 1, 2, 3, \dots)}
$$
となります。

### (3)
最低次のモードについて固有値を書き下します。

基本振動モードは最小の零点 $\alpha_1 \approx 2.4048$ に対応します。

したがって，
$$
\finalanswer{\omega_1 = \frac{c \alpha_1}{a}}
$$
となります。弦の振動と異なり，高調波の振動数比は整数比にならず，打楽器特有の倍音構成を与えます。
===== FILE: 08differential_equations/06/06_060.md =====
---
tags:
  - 標準
---

# 箱の中の粒子と変数分離

## 問題
直方体の箱 $0 < x < a, 0 < y < b, 0 < z < c$ の内部に閉じ込められた質量 $M$ の粒子の定常状態を記述する3次元シュレーディンガー方程式
$$
-\frac{\hbar^2}{2M} \nabla^2 \psi(x, y, z) = E \psi(x, y, z)
$$
を考える。境界条件は箱の表面で $\psi = 0$ である。以下の問いに答えよ。

(1) $\psi(x, y, z) = X(x) Y(y) Z(z)$ と変数分離し，規格化条件 $\int_0^a \int_0^b \int_0^c |\psi|^2 \, dx dy dz = 1$ を満たす固有関数 $\psi_{n_x, n_y, n_z}(x, y, z)$ を求めよ。

(2) エネルギー固有値 $E_{n_x, n_y, n_z}$ を正の整数 $n_x, n_y, n_z$ を用いて表せ。

(3) 立方体の箱（$a = b = c$）の場合について，基底状態のエネルギー $E_0$ および第1励起状態のエネルギー $E_1$ とその縮退度（同一エネルギーをもつ独立な状態数）を求めよ。

---

## 解答・解説

### (1)
3方向に変数分離を行い，1次元の井戸型ポテンシャルの解を掛け合わせます。

$\psi = X(x) Y(y) Z(z)$ を代入して両辺を $\psi$ で割ると，
$$
\begin{aligned}
\frac{X''(x)}{X(x)} + \frac{Y''(y)}{Y(y)} + \frac{Z''(z)}{Z(z)} &= -\frac{2ME}{\hbar^2} = -(k_x^2 + k_y^2 + k_z^2)
\end{aligned}
$$
となります。

各成分の方程式 $X'' + k_x^2 X = 0$ に境界条件 $X(0) = X(a) = 0$ を課すと，
$$
\begin{aligned}
k_x &= \frac{n_x \pi}{a}, \quad X(x) = \sqrt{\frac{2}{a}} \sin\left(\frac{n_x \pi x}{a}\right) \quad (n_x = 1, 2, \dots)
\end{aligned}
$$
となります。$y$ 方向および $z$ 方向も同様です。

したがって，規格化された固有関数は，
$$
\finalanswer{\psi_{n_x, n_y, n_z}(x, y, z) = \sqrt{\frac{8}{abc}} \sin\left(\frac{n_x \pi x}{a}\right) \sin\left(\frac{n_y \pi y}{b}\right) \sin\left(\frac{n_z \pi z}{c}\right)}
$$
となります。

### (2)
各方向の波数から全エネルギーを計算します。

エネルギー固有値は，
$$
\begin{aligned}
E &= \frac{\hbar^2}{2M} (k_x^2 + k_y^2 + k_z^2) \\
&= \frac{\hbar^2 \pi^2}{2M} \left( \frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2} \right)
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2M} \left( \frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2} \right) \quad (n_x, n_y, n_z = 1, 2, 3, \dots)}
$$
となります。

### (3)
立方体の場合のエネルギー準位を量子数の組み合わせから評価します。

$a = b = c$ のとき，エネルギーは $E = \frac{\hbar^2 \pi^2}{2Ma^2} (n_x^2 + n_y^2 + n_z^2)$ です。

基底状態は $(n_x, n_y, n_z) = (1, 1, 1)$ であり，
$$
\begin{aligned}
E_0 &= \frac{\hbar^2 \pi^2}{2Ma^2} (1^2 + 1^2 + 1^2) = \finalanswer{\frac{3\hbar^2 \pi^2}{2Ma^2}}
\end{aligned}
$$
となります。

第1励起状態は量子数のいずれか1つが $2$ となる状態であり，$(2, 1, 1), (1, 2, 1), (1, 1, 2)$ の3組が存在します。

エネルギーは，
$$
\begin{aligned}
E_1 &= \frac{\hbar^2 \pi^2}{2Ma^2} (2^2 + 1^2 + 1^2) = \finalanswer{\frac{3\hbar^2 \pi^2}{Ma^2}}
\end{aligned}
$$
となります。

3つの異なる量子数の組が同一のエネルギーを与えるため，縮退度は，
$$
\finalanswer{3}
$$
となります。空間の対称性により縮退が生じます。
===== FILE: 08differential_equations/07/07_010.md =====
---
tags:
  - 発展
---

# リッカチ型方程式

## 問題
リッカチの微分方程式
$$
\frac{dy}{dx} = y^2 - \frac{2}{x^2} \quad (x > 0)
$$
を考える。以下の問いに答えよ。

(1) 特解として $y_1(x) = \frac{a}{x}$ の形を仮定し，定数 $a$ を求めよ（正のものを1つ選べ）。

(2) 一般解を $y(x) = y_1(x) + \frac{1}{u(x)}$ とおくとき，未知関数 $u(x)$ が満たす1階線形微分方程式を導け。

(3) $u(x)$ についての方程式を解き，元の微分方程式の一般解 $y(x)$ を求めよ。

---

## 解答・解説

### (1)
仮定した関数形を微分方程式に代入して定数 $a$ を決定します。

$y_1(x) = a x^{-1}$ の導関数は $\frac{dy_1}{dx} = -a x^{-2}$ です。

方程式に代入すると，
$$
\begin{aligned}
-\frac{a}{x^2} &= \left(\frac{a}{x}\right)^2 - \frac{2}{x^2} \\
-\frac{a}{x^2} &= \frac{a^2 - 2}{x^2}
\end{aligned}
$$
となります。

両辺に $x^2$ を掛けると，
$$
\begin{aligned}
a^2 + a - 2 &= 0 \\
(a + 2)(a - 1) &= 0
\end{aligned}
$$
となり，$a = 1, -2$ を得ます。

正の解をとると，
$$
\finalanswer{a = 1 \quad \left(y_1(x) = \frac{1}{x}\right)}
$$
となります。

### (2)
変数変換を施して二次の項を相殺し，線形微分方程式を導きます。

$y = \frac{1}{x} + \frac{1}{u}$ を $x$ で微分すると，
$$
\begin{aligned}
\frac{dy}{dx} &= -\frac{1}{x^2} - \frac{1}{u^2} \frac{du}{dx}
\end{aligned}
$$
となります。

右辺に代入すると，
$$
\begin{aligned}
y^2 - \frac{2}{x^2} &= \left( \frac{1}{x} + \frac{1}{u} \right)^2 - \frac{2}{x^2} \\
&= \frac{1}{x^2} + \frac{2}{xu} + \frac{1}{u^2} - \frac{2}{x^2} \\
&= -\frac{1}{x^2} + \frac{2}{xu} + \frac{1}{u^2}
\end{aligned}
$$
となります。

両辺を等置すると，
$$
\begin{aligned}
-\frac{1}{x^2} - \frac{1}{u^2} \frac{du}{dx} &= -\frac{1}{x^2} + \frac{2}{xu} + \frac{1}{u^2} \\
-\frac{1}{u^2} \frac{du}{dx} &= \frac{2}{xu} + \frac{1}{u^2}
\end{aligned}
$$
となります。

両辺に $-u^2$ を掛けると，
$$
\finalanswer{\frac{du}{dx} + \frac{2}{x} u = -1}
$$
が得られます。

### (3)
積分因子を用いて線形方程式を解き，$y(x)$ に戻します。

積分因子は $\mu(x) = e^{\int (2/x) dx} = e^{2\ln x} = x^2$ です。方程式に $x^2$ を掛けると，
$$
\begin{aligned}
x^2 \frac{du}{dx} + 2x u &= -x^2 \\
\frac{d}{dx}(x^2 u) &= -x^2
\end{aligned}
$$
となります。

両辺を積分すると，
$$
\begin{aligned}
x^2 u &= -\int x^2 \, dx = -\frac{1}{3}x^3 + C_1
\end{aligned}
$$
となります。

$C = 3C_1$ とおいて両辺を $x^2$ で割ると，
$$
\begin{aligned}
u(x) &= \frac{C - x^3}{3x^2}
\end{aligned}
$$
となります。

したがって，一般解 $y(x) = \frac{1}{x} + \frac{1}{u(x)}$ は，
$$
\begin{aligned}
y(x) &= \frac{1}{x} + \frac{3x^2}{C - x^3} \\
&= \finalanswer{\frac{C + 2x^3}{x(C - x^3)}}
\end{aligned}
$$
となります。
===== FILE: 08differential_equations/07/07_020.md =====
---
tags:
  - 標準
---

# 自励系の平衡点と相直線

## 問題
個体群生態学におけるロジスティック方程式
$$
\frac{dx}{dt} = f(x) = r x \left(1 - \frac{x}{K}\right)
$$
を考える。ここで $r > 0, K > 0$ である。以下の問いに答えよ。

(1) 平衡点 $f(x) = 0$ をすべて求めよ。

(2) 各平衡点における導関数 $f'(x)$ を計算し，線形化による局所安定性を判定せよ。

(3) 相直線（$x$ 軸）上での流れの向き（$x < 0, 0 < x < K, x > K$ における $\frac{dx}{dt}$ の符号）を判定し，初期値 $x(0) = x_0 > 0$ を満たす解の長時間極限 $\lim_{t \to \infty} x(t)$ を答えよ。

---

## 解答・解説

### (1)
方程式の右辺を $0$ とおくことで平衡点を求めます。

条件式は，
$$
\begin{aligned}
r x \left(1 - \frac{x}{K}\right) &= 0
\end{aligned}
$$
となります。

したがって，平衡点は，
$$
\finalanswer{x = 0, \quad x = K}
$$
となります。

### (2)
$f(x)$ を微分し，各平衡点における微係数の符号を調べます。

$f(x) = r x - \frac{r}{K} x^2$ の導関数を計算すると，
$$
\begin{aligned}
f'(x) &= r - \frac{2r}{K} x
\end{aligned}
$$
となります。

$x = 0$ において，
$$
\begin{aligned}
f'(0) &= r > 0
\end{aligned}
$$
となり，微小なずれが増大するため，平衡点 $x = 0$ は不安定です。

$x = K$ において，
$$
\begin{aligned}
f'(K) &= r - 2r = -r < 0
\end{aligned}
$$
となり，微小なずれが減衰するため，平衡点 $x = K$ は漸近安定です。

したがって，
$$
\finalanswer{x = 0 : f'(0) = r > 0 \text{（不安定）}, \quad x = K : f'(K) = -r < 0 \text{（安定）}}
$$
となります。

### (3)
各区間における $f(x)$ の符号から相直線上の流速の向きを決定します。

$f(x)$ の各因数の符号を評価すると，
$$
\begin{aligned}
x < 0 \text{ では } & \frac{dx}{dt} < 0 \quad (\text{負の向きへ発散}) \\
0 < x < K \text{ では } & \frac{dx}{dt} > 0 \quad (K \text{ に向かって増加}) \\
x > K \text{ では } & \frac{dx}{dt} < 0 \quad (K \text{ に向かって減少})
\end{aligned}
$$
となります。

任意の正の初期値 $x_0 > 0$ から出発する軌道は，増加または減少して安定平衡点 $x = K$ へ向かいます。

したがって，長時間の極限値は，
$$
\finalanswer{\lim_{t \to \infty} x(t) = K}
$$
となります。環境収容力 $K$ に収束します。
===== FILE: 08differential_equations/07/07_030.md =====
---
tags:
  - 発展
---

# 摂動法による弱非線形振動

## 問題
三次非線形性をもつダフィング方程式
$$
\frac{d^2 x}{dt^2} + x + \epsilon x^3 = 0, \quad x(0) = A, \quad \frac{dx}{dt}(0) = 0
$$
を考える。ここで $0 < \epsilon \ll 1$ である。ポアンカレ・リンドステット法に従い，無次元時間 $\tau = \omega t$ を導入し，
$$
\omega = 1 + \epsilon \omega_1 + \dots, \quad x(\tau) = x_0(\tau) + \epsilon x_1(\tau) + \dots
$$
と展開する。以下の問いに答えよ。

(1) 時間変数を $\tau$ に変換し，方程式を展開して $\epsilon^0$ 次および $\epsilon^1$ 次の方程式を導け。

(2) $\epsilon^0$ 次の解 $x_0(\tau) = A \cos\tau$ を $\epsilon^1$ 次の方程式に代入し，永年項（$\cos\tau$ に比例する共振項）を消去する条件から振動数補正 $\omega_1$ を求めよ。必要であれば三倍角の公式 $\cos^3\tau = \frac{3}{4}\cos\tau + \frac{1}{4}\cos(3\tau)$ を用いよ。

(3) 摂動の1次まで含めた角振動数 $\omega$ を $\epsilon$ と $A$ を用いて表せ。

---

## 解答・解説

### (1)
連鎖律 $\frac{d}{dt} = \omega \frac{d}{d\tau}$ を用いて方程式を変換し，$\epsilon$ のべきで整理します。

導関数の変換は $\frac{d^2 x}{dt^2} = \omega^2 \frac{d^2 x}{d\tau^2}$ です。方程式は，
$$
\begin{aligned}
\omega^2 \frac{d^2 x}{d\tau^2} + x + \epsilon x^3 &= 0
\end{aligned}
$$
となります。

展開式を代入すると，
$$
\begin{aligned}
(1 + 2\epsilon \omega_1 + \dots) \frac{d^2}{d\tau^2}(x_0 + \epsilon x_1 + \dots) + (x_0 + \epsilon x_1 + \dots) + \epsilon (x_0 + \dots)^3 &= 0
\end{aligned}
$$
となります。

$\epsilon^0$ 次の項を集めると，
$$
\finalanswer{\frac{d^2 x_0}{d\tau^2} + x_0 = 0}
$$
となります。

$\epsilon^1$ 次の項を集めると，
$$
\begin{aligned}
\frac{d^2 x_1}{d\tau^2} + 2\omega_1 \frac{d^2 x_0}{d\tau^2} + x_1 + x_0^3 &= 0
\end{aligned}
$$
となります。$\frac{d^2 x_0}{d\tau^2} = -x_0$ を用いると，
$$
\finalanswer{\frac{d^2 x_1}{d\tau^2} + x_1 = 2\omega_1 x_0 - x_0^3}
$$
が得られます。

### (2)
$x_0(\tau) = A \cos\tau$ を代入し，三角関数の公式を適用します。

右辺を計算すると，
$$
\begin{aligned}
2\omega_1 (A\cos\tau) - A^3 \cos^3\tau &= 2\omega_1 A \cos\tau - A^3 \left( \frac{3}{4}\cos\tau + \frac{1}{4}\cos(3\tau) \right) \\
&= \left( 2\omega_1 A - \frac{3}{4} A^3 \right) \cos\tau - \frac{1}{4} A^3 \cos(3\tau)
\end{aligned}
$$
となります。

$\cos\tau$ の項が存在すると，固有角振動数 $1$ との共振により解に $\tau \sin\tau$ という永年項（発散項）が生じます。摂動展開が長時間有効であるためには，この係数が $0$ でなければなりません。

したがって，
$$
\begin{aligned}
2\omega_1 A - \frac{3}{4} A^3 &= 0
\end{aligned}
$$
となります。

$A \neq 0$ より，
$$
\finalanswer{\omega_1 = \frac{3}{8} A^2}
$$
となります。

### (3)
得られた補正項を振動数の展開式に代入します。

$\omega = 1 + \epsilon \omega_1$ に代入すると，
$$
\finalanswer{\omega = 1 + \frac{3}{8} \epsilon A^2}
$$
となります。非線形性（硬いばね）により，振動角振動数は振幅の二乗に比例して増加します。
===== FILE: 08differential_equations/07/07_040.md =====
---
tags:
  - 標準
---

# オイラー法と誤差

## 問題
線形微分方程式の初期値問題
$$
\frac{dy}{dt} = \lambda y, \quad y(0) = y_0 \quad (y_0 > 0)
$$
を刻み幅 $h > 0$ のオイラー法（陽解法）によって解く。時刻を $t_n = n h$ とし，数値解を $y_n$ とする。以下の問いに答えよ。

(1) 前進差分による漸化式 $y_{n+1} = y_n + h f(t_n, y_n)$ を具体的に書き下し，局所離散化誤差が $O(h^2)$ であることを真解のテイラー展開を用いて示せ。

(2) 漸化式を解いて，ステップ数 $n$ における数値解 $y_n$ の表式を求めよ。

(3) 時刻 $t = n h$ を一定に保ったまま $h \to 0$（$n \to \infty$）の極限をとるとき，数値解 $y_n$ が厳密解 $y(t) = y_0 e^{\lambda t}$ に収束することを示せ。

---

## 解答・解説

### (1)
漸化式を立て，真解の1ステップの発展とオイラー法の近似を比較します。

オイラー法の漸化式に $f(t_n, y_n) = \lambda y_n$ を代入すると，
$$
\begin{aligned}
y_{n+1} &= y_n + h \lambda y_n \\
&= \finalanswer{(1 + \lambda h) y_n}
\end{aligned}
$$
となります。

真解 $y(t)$ のテイラー展開を計算すると，
$$
\begin{aligned}
y(t_n + h) &= y(t_n) + h y'(t_n) + \frac{h^2}{2} y''(t_n) + O(h^3) \\
&= y(t_n) + h \lambda y(t_n) + \frac{h^2}{2} \lambda^2 y(t_n) + O(h^3)
\end{aligned}
$$
となります。

1ステップの数値解 $y(t_n) + h \lambda y(t_n)$ との差を計算すると，
$$
\begin{aligned}
y(t_n + h) - (1 + \lambda h) y(t_n) &= \frac{\lambda^2 y(t_n)}{2} h^2 + O(h^3)
\end{aligned}
$$
となります。

したがって，局所離散化誤差は，
$$
\finalanswer{O(h^2)}
$$
となります。

### (2)
得られた公比の数列を繰り返し適用します。

漸化式 $y_{n+1} = (1 + \lambda h) y_n$ は公比 $(1 + \lambda h)$ の等比数列です。

初期値 $y_0$ から $n$ 回掛けると，
$$
\finalanswer{y_n = y_0 (1 + \lambda h)^n}
$$
となります。

### (3)
$n = t/h$ を代入し，ネイピア数の極限定義を適用します。

$h = t/n$ を代入すると，数値解は，
$$
\begin{aligned}
y_n &= y_0 \left( 1 + \frac{\lambda t}{n} \right)^n
\end{aligned}
$$
と表されます。

$n \to \infty$ の極限をとると，
$$
\begin{aligned}
\lim_{n \to \infty} y_n &= y_0 \lim_{n \to \infty} \left( 1 + \frac{\lambda t}{n} \right)^n \\
&= y_0 e^{\lambda t}
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{\lim_{\substack{h \to 0 \\ nh = t}} y_n = y_0 e^{\lambda t}}
$$
となり，数値解が厳密解に収束することが示されます。全区間での大域誤差は局所誤差 $O(h^2)$ にステップ数 $n = O(1/h)$ を掛けた $O(h)$ となり，オイラー法は1次の解法となります。
===== END =====