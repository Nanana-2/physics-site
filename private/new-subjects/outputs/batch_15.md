===== FILE: 12special_functions/04/04_010.md =====
---
tags:
  - 基本
---

# オイラー・ラグランジュ方程式

## 問題
両端点を $(x_1, y_1)$ および $(x_2, y_2)$ に固定した滑らかな曲線 $y(x)$ に対する汎関数
$$
I[y] = \int_{x_1}^{x_2} f(x, y(x), y'(x)) \, dx
$$
を考える。ここで $y'(x) = dy/dx$ であり，$f(x, y, y')$ は各引数について連続微分可能とする。以下の問いに答えよ。

(1) 両端点で $0$ となる任意の微小変分 $\eta(x)$（$\eta(x_1) = \eta(x_2) = 0$）と微小パラメータ $\epsilon$ を用いて $y(x) + \epsilon \eta(x)$ を考えたとき，$I[y + \epsilon \eta]$ を $\epsilon$ について展開して1次の変分 $\delta I$ を求めよ。

(2) $\delta I = 0$ が任意の $\eta(x)$ に対して成り立つ条件から，関数 $y(x)$ が満たすべき微分方程式（オイラー・ラグランジュ方程式）を導け。

---

## 解答・解説

### (1)
変形した曲線 $Y(x) = y(x) + \epsilon \eta(x)$ を汎関数に代入すると，積分はパラメータ $\epsilon$ の関数とみなせます。

$$
I(\epsilon) = \int_{x_1}^{x_2} f(x, y(x) + \epsilon \eta(x), y'(x) + \epsilon \eta'(x)) \, dx
$$

ここで $I(\epsilon)$ を $\epsilon = 0$ のまわりでテイラー展開します。1次の変分 $\delta I$ は微係数を用いて $\delta I = \left. \frac{dI}{d\epsilon} \right|_{\epsilon=0} \epsilon$ と定義されます。積分記号下で $\epsilon$ について微分すると，多変数関数の合成微分の規則より次のようになります。

$$
\begin{aligned}
\left. \frac{dI}{d\epsilon} \right|_{\epsilon=0}
&= \int_{x_1}^{x_2} \left[ \frac{\partial f}{\partial y} \frac{\partial Y}{\partial \epsilon} + \frac{\partial f}{\partial y'} \frac{\partial Y'}{\partial \epsilon} \right]_{\epsilon=0} dx \\
&= \int_{x_1}^{x_2} \left( \frac{\partial f}{\partial y} \eta(x) + \frac{\partial f}{\partial y'} \eta'(x) \right) dx
\end{aligned}
$$

微小変化 $\delta y(x) = \epsilon \eta(x)$ および $\delta y'(x) = \epsilon \eta'(x)$ を用いて表すと，1次の変分は次の式で与えられます。

$$
\finalanswer{\delta I = \int_{x_1}^{x_2} \left( \frac{\partial f}{\partial y} \delta y + \frac{\partial f}{\partial y'} \delta y' \right) dx}
$$

となります。

### (2)
(1) で得られた変分の第2項に対して部分積分を実行します。境界条件 $\eta(x_1) = \eta(x_2) = 0$ を適用すると，端点での境界項は消去されます。

$$
\begin{aligned}
\int_{x_1}^{x_2} \frac{\partial f}{\partial y'} \eta'(x) \, dx
&= \left[ \frac{\partial f}{\partial y'} \eta(x) \right]_{x_1}^{x_2} - \int_{x_1}^{x_2} \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) \eta(x) \, dx \\
&= - \int_{x_1}^{x_2} \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) \eta(x) \, dx
\end{aligned}
$$

この結果を $\delta I$ の式に代入して整理します。

$$
\delta I = \epsilon \int_{x_1}^{x_2} \left[ \frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) \right] \eta(x) \, dx
$$

汎関数が停留値をとるためには，端点で $0$ となる任意の滑らかな関数 $\eta(x)$ に対して $\delta I = 0$ が成立しなければなりません。変分法の基本補題を適用すると，被積分関数の大括弧内が区間内のすべての $x$ で常に $0$ でなければならないことが導かれます。

したがって，求める微分方程式は次のようになります。

$$
\finalanswer{\frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) = 0}
$$

となります。この方程式はオイラー・ラグランジュ方程式と呼ばれ，物理学における最小作用の原理や幾何学的な最短線問題の基礎となります。

===== FILE: 12special_functions/04/04_020.md =====
---
tags:
  - 基本
---

# 平面上の最短経路

## 問題
$xy$ 平面上の相異なる2点 $(x_1, y_1)$ と $(x_2, y_2)$（$x_1 < x_2$）を結ぶ滑らかな曲線 $y(x)$ を考える。曲線の線素は $ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + (y')^2} \, dx$ で与えられる。以下の問いに答えよ。

(1) 弧長を表す汎関数 $L[y] = \int_{x_1}^{x_2} \sqrt{1 + (y')^2} \, dx$ に対するオイラー・ラグランジュ方程式を立てよ。

(2) (1) の微分方程式を解き，2点を結ぶ弧長を最小にする曲線が直線であることを示せ。

---

## 解答・解説

### (1)
被積分関数を $f(x, y, y') = \sqrt{1 + (y')^2}$ とおきます。この関数は $x$ および $y$ を陽に含まないため，各偏導関数は次のようになります。

$$
\frac{\partial f}{\partial y} = 0
$$

また，$y'$ について偏微分を計算すると次のようになります。

$$
\frac{\partial f}{\partial y'} = \frac{y'}{\sqrt{1 + (y')^2}}
$$

オイラー・ラグランジュ方程式 $\frac{\partial f}{\partial y} - \frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) = 0$ に代入すると，求める微分方程式は次の形になります。

$$
\finalanswer{\frac{d}{dx} \left( \frac{y'}{\sqrt{1 + (y')^2}} \right) = 0}
$$

となります。

### (2)
(1) で得られた微分方程式を $x$ について積分します。

$$
\frac{y'}{\sqrt{1 + (y')^2}} = C \quad (C \text{ は定数})
$$

被積分関数の分母は常に正の実数であるため，定数 $C$ は $|C| < 1$ を満たします。両辺を2乗して $y'$ について解きます。

$$
\begin{aligned}
(y')^2 &= C^2 (1 + (y')^2) \\
(1 - C^2)(y')^2 &= C^2 \\
y' &= \pm \frac{C}{\sqrt{1 - C^2}}
\end{aligned}
$$

右辺は定数であるため，これを改めて定数 $m$ とおきます。

$$
\frac{dy}{dx} = m
$$

この微分方程式を積分すると，任意定数 $c$ を用いて次の一般解が得られます。

$$
y(x) = m x + c
$$

曲線が2点 $(x_1, y_1)$ および $(x_2, y_2)$ を通過するという境界条件を代入します。

$$
\begin{aligned}
y_1 &= m x_1 + c \\
y_2 &= m x_2 + c
\end{aligned}
$$

辺々の差をとると $m(x_2 - x_1) = y_2 - y_1$ となり，$x_1 \neq x_2$ より傾き $m$ が求まります。

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

これを $c = y_1 - m x_1$ とともに代入すると，曲線の方程式は次のように決定されます。

$$
\finalanswer{y(x) = \frac{y_2 - y_1}{x_2 - x_1}(x - x_1) + y_1}
$$

となります。これは2点を通る直線の方程式そのものであり，平面上の最短経路が直線であることが示されました。

===== FILE: 12special_functions/04/04_030.md =====
---
tags:
  - 標準
---

# 最速降下線

## 問題
鉛直下向きに $y$ 軸，水平方向に $x$ 軸をとる。原点 $(0,0)$ から点 $(x_1, y_1)$（$x_1 > 0, y_1 > 0$）まで，一様な重力加速度 $g$ のもとで初速度 $0$ で摩擦なく滑り落ちる質点の所要時間を最小にする滑らかな曲線 $y(x)$ を求める（図）。

<!-- FIGURE problem: 座標軸は水平右向きにx軸，鉛直下向きにy軸。原点O(0,0)と第1象限の点P(x_1, y_1)を結ぶ滑らかな曲線。点Pの位置に破線で垂線をおろし座標値を明示。重力加速度gが下向きの矢印で示されている。 -->

以下の問いに答えよ。

(1) 力学的エネルギー保存則から質点の速さ $v$ を $y$ の式で表し，降下に要する全時間 $T$ を $y$ と $y' = dy/dx$ を用いた定積分として表せ。

(2) 被積分関数が $x$ を陽に含まないときに成立する第1積分（ベルトラミの等式）を用いて，曲線が満たす微分方程式が正の定数 $a$ を用いて $y [1 + (y')^2] = 2a$ と表されることを示せ。

(3) パラメータ $\theta$ を用いて $y = a(1 - \cos\theta)$ と置換することにより，$x$ を $\theta$ と $a$ を用いて表せ。ただし $\theta = 0$ で $x = 0$ とする。

---

## 解答・解説

### (1)
質点は原点 $(0,0)$ において初速度 $0$ で運動を開始します。深さ $y$ まで降下したときの運動エネルギーと位置エネルギーの和は保存されるため，次が成り立ちます。

$$
\frac{1}{2}m v^2 - m g y = 0
$$

したがって，速さ $v$ は次のように求まります。

$$
v = \sqrt{2gy}
$$

微小弧長は $ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + (y')^2} \, dx$ です。微小時間 $dt = ds/v$ を原点から終点まで積分することにより，全所要時間 $T$ は次のように表されます。

$$
\finalanswer{T = \int_0^{x_1} \sqrt{\frac{1 + (y')^2}{2gy}} \, dx}
$$

となります。

### (2)
汎関数の被積分関数を $f(y, y') = \sqrt{\frac{1 + (y')^2}{2gy}}$ とおきます。被積分関数が変数 $x$ を陽に含まない場合，オイラー・ラグランジュ方程式からベルトラミの等式（エネルギー保存型第1積分）が成り立ちます。

$$
f - y' \frac{\partial f}{\partial y'} = C \quad (C \text{ は正の定数})
$$

$f$ の $y'$ に関する偏導関数を計算します。

$$
\frac{\partial f}{\partial y'} = \frac{y'}{\sqrt{2gy} \sqrt{1 + (y')^2}}
$$

これをベルトラミの等式に代入して通分します。

$$
\begin{aligned}
f - y' \frac{\partial f}{\partial y'}
&= \frac{1 + (y')^2}{\sqrt{2gy}\sqrt{1 + (y')^2}} - \frac{(y')^2}{\sqrt{2gy}\sqrt{1 + (y')^2}} \\
&= \frac{1}{\sqrt{2gy}\sqrt{1 + (y')^2}} \\
&= C
\end{aligned}
$$

両辺を2乗して逆数をとります。

$$
2gy [1 + (y')^2] = \frac{1}{C^2}
$$

ここで $a = \frac{1}{4gC^2}$ と定義すると，右辺は $4ga$ と書き換えられます。両辺を $2g$ で割ることにより，次の関係式が得られます。

$$
\finalanswer{y [1 + (y')^2] = 2a}
$$

となります。

### (3)
(2) で得られた式を $y'$ について解きます。質点は下向きに進むため $y' \ge 0$ とすると次のようになります。

$$
y' = \sqrt{\frac{2a - y}{y}}
$$

$y = a(1 - \cos\theta)$ とおくと，三角関数の半角の公式より根号内は次のように変形できます。

$$
\begin{aligned}
\frac{2a - y}{y}
&= \frac{2a - a(1 - \cos\theta)}{a(1 - \cos\theta)} \\
&= \frac{1 + \cos\theta}{1 - \cos\theta} \\
&= \frac{2\cos^2(\theta/2)}{2\sin^2(\theta/2)} \\
&= \cot^2\left(\frac{\theta}{2}\right)
\end{aligned}
$$

したがって，$y' = \frac{dy}{dx} = \cot(\theta/2)$ となります。一方，$y$ の微分は $dy = a \sin\theta \, d\theta$ です。これを $dx = \frac{dy}{y'}$ に代入します。

$$
\begin{aligned}
dx &= \frac{a \sin\theta}{\cot(\theta/2)} \, d\theta \\
&= \frac{2a \sin(\theta/2)\cos(\theta/2)}{\cos(\theta/2)/\sin(\theta/2)} \, d\theta \\
&= 2a \sin^2\left(\frac{\theta}{2}\right) d\theta \\
&= a (1 - \cos\theta) \, d\theta
\end{aligned}
$$

この式を $\theta = 0$ で $x = 0$ という初期条件のもとで積分します。

$$
\begin{aligned}
x(\theta) &= a \int_0^\theta (1 - \cos\phi) \, d\phi \\
&= a (\theta - \sin\theta)
\end{aligned}
$$

したがって，求める関係式は次のようになります。

$$
\finalanswer{x(\theta) = a(\theta - \sin\theta)}
$$

となります。これは半径 $a$ の円が直線上を滑らずに転がるときに円周上の点が描くサイクロイド曲線を表しています。

===== FILE: 12special_functions/04/04_040.md =====
---
tags:
  - 標準
---

# 懸垂線

## 問題
密度が一様で伸び縮みしない長さ $L$ のひもが，鉛直面内の同一高度にある2点 $(-a, h)$ と $(a, h)$ に固定されている（$2a < L$）。重力加速度を $g$ とする（図）。

<!-- FIGURE problem: 水平方向にx軸，鉛直上向きにy軸。x = -a と x = a の高さhにある2つの固定点。その2点を結ぶ左右対称に垂れ下がったなめらかな曲線。最下点はx = 0でy_0。 -->

以下の問いに答えよ。

(1) ひもの線密度を $\rho$ とするとき，ひもの全質量 $M = \rho L$ に対する重力による位置エネルギー $U[y]$，およびひもの全長 $L[y]$ を曲線 $y(x)$ と $y' = dy/dx$ の積分として表せ。

(2) ラグランジュの未定乗数を $\lambda$ とし，拘束条件を組み込んだ汎関数の被積分関数を $F(y, y') = (\rho g y - \lambda)\sqrt{1 + (y')^2}$ とおく。ベルトラミの等式を用いて，この系に対する第1積分を導け。

(3) 境界条件の対称性 $y(-x) = y(x)$ を用いて微分方程式を解き，曲線の形状が双曲線余弦関数を用いて $y(x) = c \cosh(x/c) + y_0$（$c, y_0$ は定数）と表されることを示せ。

---

## 解答・解説

### (1)
微小線素は $ds = \sqrt{1 + (y')^2} \, dx$ で表されます。微小部分の質量は $dm = \rho \, ds$ であり，高さ $y$ における重力による位置エネルギーは $dU = dm \, gy = \rho g y \, ds$ です。

したがって，ひもの全長 $L[y]$ および位置エネルギー $U[y]$ は区間 $[-a, a]$ での積分として次のように表されます。

$$
\finalanswer{L[y] = \int_{-a}^a \sqrt{1 + (y')^2} \, dx}
$$

$$
\finalanswer{U[y] = \int_{-a}^a \rho g y \sqrt{1 + (y')^2} \, dx}
$$

となります。

### (2)
長さ $L$ を一定に保つ拘束条件のもとで位置エネルギー $U[y]$ を最小化するため，ラグランジュの未定乗数 $\lambda$ を導入して汎関数 $J[y] = U[y] - \lambda L[y]$ を停留させます。被積分関数は次のようになります。

$$
F(y, y') = (\rho g y - \lambda)\sqrt{1 + (y')^2}
$$

$F$ は独立変数 $x$ を陽に含まないため，ベルトラミの等式が成り立ちます。

$$
F - y' \frac{\partial F}{\partial y'} = C \quad (C \text{ は定数})
$$

$F$ の $y'$ に関する偏導関数を計算します。

$$
\frac{\partial F}{\partial y'} = (\rho g y - \lambda) \frac{y'}{\sqrt{1 + (y')^2}}
$$

これを等式に代入して整理します。

$$
\begin{aligned}
F - y' \frac{\partial F}{\partial y'}
&= (\rho g y - \lambda)\sqrt{1 + (y')^2} - (\rho g y - \lambda) \frac{(y')^2}{\sqrt{1 + (y')^2}} \\
&= \frac{\rho g y - \lambda}{\sqrt{1 + (y')^2}} \\
&= C
\end{aligned}
$$

したがって，求める第1積分は次のようになります。

$$
\finalanswer{\frac{\rho g y - \lambda}{\sqrt{1 + (y')^2}} = C}
$$

となります。

### (3)
(2) で得られた式を定数 $c = \frac{C}{\rho g}$ および $y_0 = \frac{\lambda}{\rho g}$ を用いて書き直します。

$$
\frac{y - y_0}{\sqrt{1 + (y')^2}} = c
$$

この式を $y'$ について解きます。

$$
\frac{dy}{dx} = \sqrt{\left(\frac{y - y_0}{c}\right)^2 - 1}
$$

変数分離形にして積分を実行します。

$$
\int \frac{dy}{\sqrt{(y - y_0)^2 - c^2}} = \int \frac{dx}{c}
$$

左辺の積分に対して $y - y_0 = c \cosh u$ と置換すると，$dy = c \sinh u \, du$ および $\sqrt{(y - y_0)^2 - c^2} = c \sinh u$ となるため，左辺は $u$ となります。

$$
u = \operatorname{arcosh}\left(\frac{y - y_0}{c}\right) = \frac{x - x_0}{c}
$$

ここで $x_0$ は積分定数です。境界条件 $y(-a) = y(a) = h$ より，曲線の形状は $x = 0$ に関して対称でなければなりません。したがって $x = 0$ で傾きが $y'(0) = 0$ となることから $x_0 = 0$ が定まります。

両辺の逆関数をとると，求める曲線の形状が得られます。

$$
\finalanswer{y(x) = c \cosh\left(\frac{x}{c}\right) + y_0}
$$

となります。この曲線はカテナリー（懸垂線）と呼ばれ，電線や吊り橋のケーブルの自然な垂れ下がり形状を記述します。

===== FILE: 12special_functions/04/04_050.md =====
---
tags:
  - 標準
---

# 等周問題とラグランジュの未定乗数

## 問題
$x$ 軸上の2点 $(-a, 0)$ と $(a, 0)$（$a > 0$）を結ぶ滑らかな曲線 $y(x) \ge 0$（境界条件 $y(-a) = y(a) = 0$）を考える。曲線の長さが一定値 $L$（$L > 2a$）であるとき，曲線と $x$ 軸で囲まれる領域の面積 $S = \int_{-a}^a y \, dx$ を最大にする問題を考える。以下の問いに答えよ。

(1) 弧長一定の拘束条件のもとで未定乗数 $\lambda$ を導入した汎関数 $J[y] = \int_{-a}^a [y + \lambda \sqrt{1 + (y')^2}] \, dx$ に対するオイラー・ラグランジュ方程式の第1積分を導け。

(2) (1) の微分方程式を解き，面積を最大にする曲線 $y(x)$ が円弧 $(x - x_0)^2 + (y - y_0)^2 = R^2$ の一部となることを示せ。

---

## 解答・解説

### (1)
汎関数の被積分関数を $f(y, y') = y + \lambda \sqrt{1 + (y')^2}$ とおきます。この関数は $x$ を陽に含まないため，ベルトラミの等式より次の量が定数 $C$ として保存されます。

$$
f - y' \frac{\partial f}{\partial y'} = C
$$

被積分関数の $y'$ に関する偏導関数を計算します。

$$
\frac{\partial f}{\partial y'} = \frac{\lambda y'}{\sqrt{1 + (y')^2}}
$$

これをベルトラミの等式に代入して計算します。

$$
\begin{aligned}
f - y' \frac{\partial f}{\partial y'}
&= y + \lambda \sqrt{1 + (y')^2} - \frac{\lambda (y')^2}{\sqrt{1 + (y')^2}} \\
&= y + \frac{\lambda [1 + (y')^2] - \lambda (y')^2}{\sqrt{1 + (y')^2}} \\
&= y + \frac{\lambda}{\sqrt{1 + (y')^2}} \\
&= C
\end{aligned}
$$

したがって，求める第1積分は次のようになります。

$$
\finalanswer{y + \frac{\lambda}{\sqrt{1 + (y')^2}} = C}
$$

となります。

### (2)
(1) で得られた式を $y'$ について解きます。

$$
\begin{aligned}
\frac{\lambda}{\sqrt{1 + (y')^2}} &= C - y \\
\frac{\lambda^2}{(C - y)^2} &= 1 + (y')^2 \\
(y')^2 &= \frac{\lambda^2 - (C - y)^2}{(C - y)^2}
\end{aligned}
$$

両辺の平方根をとると次の微分方程式が得られます。

$$
\frac{dy}{dx} = \frac{\sqrt{\lambda^2 - (y - C)^2}}{C - y}
$$

変数分離形にして両辺を積分します。

$$
\int \frac{C - y}{\sqrt{\lambda^2 - (y - C)^2}} \, dy = \int dx
$$

左辺の被積分関数の分子は根号内の関数の導関数の $-1/2$ 倍であるため，直ちに積分できます。

$$
\sqrt{\lambda^2 - (y - C)^2} = x - x_0
$$

ここで $x_0$ は積分定数です。両辺を2乗して移項します。

$$
(x - x_0)^2 + (y - C)^2 = \lambda^2
$$

境界条件 $y(-a) = y(a) = 0$ より曲線は $x = 0$ に関して対称でなければならないため，$x_0 = 0$ が定まります。また $y_0 = C$，$R = |\lambda|$ とおくと，曲線の方程式は次のように表されます。

$$
\finalanswer{x^2 + (y - y_0)^2 = R^2}
$$

となります。これは中心 $(0, y_0)$，半径 $R$ の円の方程式であり，囲まれる面積を最大にする曲線が円弧であることが示されました。

===== FILE: 12special_functions/04/04_060.md =====
---
tags:
  - 発展
---

# 場の汎関数微分

## 問題
1次元空間 $x$（$x_1 \le x \le x_2$）と時間 $t$（$t_1 \le t \le t_2$）における実スカラー場 $\phi(x,t)$ の作用積分が，ラグランジアン密度 $\mathcal{L}$ を用いて次式で与えられている。
$$
S[\phi] = \int_{t_1}^{t_2} dt \int_{x_1}^{x_2} dx \, \mathcal{L}\left(\phi, \frac{\partial \phi}{\partial t}, \frac{\partial \phi}{\partial x}\right)
$$
領域の境界上で $0$ となる任意の微小変分 $\delta \phi(x,t)$ を考える。以下の問いに答えよ。

(1) 作用の変分 $\delta S$ を計算し，ハミルトンの原理 $\delta S = 0$ から場 $\phi(x,t)$ に対するオイラー・ラグランジュ方程式を導け。

(2) 線密度 $\rho$ と張力 $T$ をもつ弦の微小振動を表すラグランジアン密度が
$$
\mathcal{L} = \frac{1}{2}\rho \left(\frac{\partial \phi}{\partial t}\right)^2 - \frac{1}{2}T \left(\frac{\partial \phi}{\partial x}\right)^2
$$
で与えられるとき，(1) の方程式を用いて場 $\phi$ が満たす運動方程式（波動方程式）を求めよ。また波の位相速度 $v$ を $\rho$ と $T$ で表せ。

---

## 解答・解説

### (1)
微小変分 $\delta \phi(x,t)$ に伴うラグランジアン密度 $\mathcal{L}$ の変化を，1次の変分まで計算します。記号の簡略化のため $\phi_t = \frac{\partial \phi}{\partial t}$，$\phi_x = \frac{\partial \phi}{\partial x}$ と表記します。

$$
\delta S = \int_{t_1}^{t_2} dt \int_{x_1}^{x_2} dx \left( \frac{\partial \mathcal{L}}{\partial \phi} \delta \phi + \frac{\partial \mathcal{L}}{\partial \phi_t} \delta \phi_t + \frac{\partial \mathcal{L}}{\partial \phi_x} \delta \phi_x \right)
$$

第2項および第3項に対してそれぞれ時間および空間について部分積分を行います。微小変分は境界上で $\delta \phi = 0$ を満たすため，境界項はすべて消失します。

$$
\begin{aligned}
\int_{t_1}^{t_2} \frac{\partial \mathcal{L}}{\partial \phi_t} \frac{\partial(\delta \phi)}{\partial t} \, dt
&= \left[ \frac{\partial \mathcal{L}}{\partial \phi_t} \delta \phi \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \frac{\partial}{\partial t}\left(\frac{\partial \mathcal{L}}{\partial \phi_t}\right) \delta \phi \, dt \\
&= - \int_{t_1}^{t_2} \frac{\partial}{\partial t}\left(\frac{\partial \mathcal{L}}{\partial \phi_t}\right) \delta \phi \, dt
\end{aligned}
$$

同様に空間微分についても次が成り立ちます。

$$
\int_{x_1}^{x_2} \frac{\partial \mathcal{L}}{\partial \phi_x} \frac{\partial(\delta \phi)}{\partial x} \, dx = - \int_{x_1}^{x_2} \frac{\partial}{\partial x}\left(\frac{\partial \mathcal{L}}{\partial \phi_x}\right) \delta \phi \, dx
$$

これらを $\delta S$ に代入して整理します。

$$
\delta S = \int_{t_1}^{t_2} dt \int_{x_1}^{x_2} dx \left[ \frac{\partial \mathcal{L}}{\partial \phi} - \frac{\partial}{\partial t}\left(\frac{\partial \mathcal{L}}{\partial (\partial \phi / \partial t)}\right) - \frac{\partial}{\partial x}\left(\frac{\partial \mathcal{L}}{\partial (\partial \phi / \partial x)}\right) \right] \delta \phi
$$

任意の変分 $\delta \phi$ に対して $\delta S = 0$ が成り立つことから，場に対するオイラー・ラグランジュ方程式が得られます。

$$
\finalanswer{\frac{\partial \mathcal{L}}{\partial \phi} - \frac{\partial}{\partial t}\left(\frac{\partial \mathcal{L}}{\partial (\partial \phi / \partial t)}\right) - \frac{\partial}{\partial x}\left(\frac{\partial \mathcal{L}}{\partial (\partial \phi / \partial x)}\right) = 0}
$$

となります。

### (2)
与えられたラグランジアン密度 $\mathcal{L} = \frac{1}{2}\rho \left(\frac{\partial \phi}{\partial t}\right)^2 - \frac{1}{2}T \left(\frac{\partial \phi}{\partial x}\right)^2$ に対し，各偏導関数を計算します。

$$
\begin{aligned}
\frac{\partial \mathcal{L}}{\partial \phi} &= 0 \\
\frac{\partial \mathcal{L}}{\partial (\partial \phi / \partial t)} &= \rho \frac{\partial \phi}{\partial t} \\
\frac{\partial \mathcal{L}}{\partial (\partial \phi / \partial x)} &= -T \frac{\partial \phi}{\partial x}
\end{aligned}
$$

これらを (1) のオイラー・ラグランジュ方程式に代入します。

$$
0 - \frac{\partial}{\partial t}\left( \rho \frac{\partial \phi}{\partial t} \right) - \frac{\partial}{\partial x}\left( -T \frac{\partial \phi}{\partial x} \right) = 0
$$

線密度 $\rho$ と張力 $T$ が一様定数である場合，時間微分と空間微分を実行して整理します。

$$
-\rho \frac{\partial^2 \phi}{\partial t^2} + T \frac{\partial^2 \phi}{\partial x^2} = 0
$$

両辺を $\rho$ で割ると，標準的な波動方程式の形が得られます。

$$
\finalanswer{\frac{\partial^2 \phi}{\partial t^2} - \frac{T}{\rho} \frac{\partial^2 \phi}{\partial x^2} = 0}
$$

この方程式を一般の波動方程式 $\frac{\partial^2 \phi}{\partial t^2} - v^2 \frac{\partial^2 \phi}{\partial x^2} = 0$ と比較することにより，波の位相速度 $v$ は次のように求まります。

$$
\finalanswer{v = \sqrt{\frac{T}{\rho}}}
$$

となります。

===== FILE: 12special_functions/04/04_070.md =====
---
tags:
  - 発展
---

# レイリー・リッツ法

## 問題
区間 $[0, 1]$ における微分方程式 $-y''(x) = \lambda y(x)$，境界条件 $y(0) = y(1) = 0$ で定義される固有値問題を考える。厳密な最小固有値は $\lambda_1 = \pi^2 \approx 9.8696$ である。以下の問いに答えよ。

(1) 境界条件を満たす関数 $y(x)$ に対するレイリー商
$$
R[y] = \frac{\int_0^1 (y'(x))^2 \, dx}{\int_0^1 (y(x))^2 \, dx}
$$
を考える。境界条件を満たす最も単純な多項式の試行関数 $y(x) = x(1 - x)$ を用いて，レイリー商の値 $\lambda_{\mathrm{app}}$ を計算せよ。

(2) 一般に正規直交固有関数系 $\{u_n(x)\}$（$-u_n'' = \lambda_n u_n$，$\int_0^1 u_m u_n dx = \delta_{mn}$，$\lambda_1 < \lambda_2 < \dots$）が存在するとき，境界条件を満たす任意の関数 $y(x)$ に対するレイリー商が常に最小固有値の上限を与えること（$R[y] \ge \lambda_1$）を示せ。

---

## 解答・解説

### (1)
試行関数 $y(x) = x(1 - x) = x - x^2$ の導関数は $y'(x) = 1 - 2x$ です。

まず分子の積分を計算します。

$$
\begin{aligned}
\int_0^1 (y'(x))^2 \, dx
&= \int_0^1 (1 - 2x)^2 \, dx \\
&= \int_0^1 (1 - 4x + 4x^2) \, dx \\
&= \left[ x - 2x^2 + \frac{4}{3}x^3 \right]_0^1 \\
&= 1 - 2 + \frac{4}{3} \\
&= \frac{1}{3}
\end{aligned}
$$

次に分母の積分を計算します。

$$
\begin{aligned}
\int_0^1 (y(x))^2 \, dx
&= \int_0^1 x^2 (1 - x)^2 \, dx \\
&= \int_0^1 (x^2 - 2x^3 + x^4) \, dx \\
&= \left[ \frac{1}{3}x^3 - \frac{1}{2}x^4 + \frac{1}{5}x^5 \right]_0^1 \\
&= \frac{1}{3} - \frac{1}{2} + \frac{1}{5} \\
&= \frac{10 - 15 + 6}{30} \\
&= \frac{1}{30}
\end{aligned}
$$

これらをレイリー商の定義に代入します。

$$
R[y] = \frac{1/3}{1/30} = 10
$$

したがって，近似固有値は次のようになります。

$$
\finalanswer{\lambda_{\mathrm{app}} = 10}
$$

となります。厳密解 $\pi^2 \approx 9.8696$ に対する相対誤差は約 $1.3\%$ であり，極めて高い精度で近似できていることがわかります。

### (2)
境界条件を満たす任意の関数 $y(x)$ を正規直交固有関数系 $\{u_n(x)\}$ で展開します。

$$
y(x) = \sum_{n=1}^\infty c_n u_n(x) \quad \left( c_n = \int_0^1 y(x) u_n(x) \, dx \right)
$$

分母の積分を直交性 $\int_0^1 u_m u_n \, dx = \delta_{mn}$ を用いて展開します。

$$
\int_0^1 (y(x))^2 \, dx = \sum_{m,n=1}^\infty c_m c_n \int_0^1 u_m(x) u_n(x) \, dx = \sum_{n=1}^\infty c_n^2
$$

分子の積分に対して部分積分を実行すると，境界条件 $y(0) = y(1) = 0$ より境界項が消え，固有値方程式 $-u_n'' = \lambda_n u_n$ が適用できます。

$$
\begin{aligned}
\int_0^1 (y'(x))^2 \, dx
&= [y(x) y'(x)]_0^1 - \int_0^1 y(x) y''(x) \, dx \\
&= \int_0^1 \left( \sum_{m=1}^\infty c_m u_m(x) \right) \left( \sum_{n=1}^\infty c_n \lambda_n u_n(x) \right) dx \\
&= \sum_{n=1}^\infty \lambda_n c_n^2
\end{aligned}
$$

固有値の大小関係 $\lambda_1 < \lambda_2 \le \dots$ より，すべての $n$ に対して $\lambda_n \ge \lambda_1$ が成り立ちます。

$$
\sum_{n=1}^\infty \lambda_n c_n^2 \ge \lambda_1 \sum_{n=1}^\infty c_n^2
$$

両辺を正の実数である $\sum_{n=1}^\infty c_n^2$ で割ると，次の不等式が得られます。

$$
\finalanswer{R[y] \ge \lambda_1}
$$

となります。等号は試行関数が基底状態の固有関数 $u_1(x)$ に厳密に一致するときに限り成立します。

===== FILE: 12special_functions/05/05_010.md =====
---
tags:
  - 基本
---

# 誤差関数

## 問題
誤差関数 $\operatorname{erf}(x)$ および相補誤差関数 $\operatorname{erfc}(x)$ は次式で定義される。
$$
\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} \, dt, \quad \operatorname{erfc}(x) = 1 - \operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_x^\infty e^{-t^2} \, dt
$$
ガウス積分の公式 $\int_{-\infty}^\infty e^{-t^2} \, dt = \sqrt{\pi}$ を用いて，以下の問いに答えよ。

(1) 極限値 $\lim_{x \to \infty} \operatorname{erf}(x)$ を求めよ。また $\operatorname{erf}(-x) = -\operatorname{erf}(x)$（奇関数）であることを示せ。

(2) $x > 0$ において被積分関数を $e^{-t^2} = -\frac{1}{2t} \frac{d}{dt}(e^{-t^2})$ と変形し，部分積分を2回繰り返すことにより，相補誤差関数の $x \to \infty$ における漸近展開の主要な2項（$1/x$ および $1/x^3$ の項）を求めよ。

---

## 解答・解説

### (1)
被積分関数 $e^{-t^2}$ は偶関数であるため，全区間でのガウス積分より半無限区間での積分値は次のように計算されます。

$$
\int_0^\infty e^{-t^2} \, dt = \frac{1}{2} \int_{-\infty}^\infty e^{-t^2} \, dt = \frac{\sqrt{\pi}}{2}
$$

定義式において $x \to \infty$ の極限をとると次のようになります。

$$
\lim_{x \to \infty} \operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^\infty e^{-t^2} \, dt = \frac{2}{\sqrt{\pi}} \frac{\sqrt{\pi}}{2} = 1
$$

したがって，求める極限値は次の値になります。

$$
\finalanswer{\lim_{x \to \infty} \operatorname{erf}(x) = 1}
$$

次に，$\operatorname{erf}(-x)$ の定義式において変数変換 $t = -u$（$dt = -du$）を行います。

$$
\begin{aligned}
\operatorname{erf}(-x)
&= \frac{2}{\sqrt{\pi}} \int_0^{-x} e^{-t^2} \, dt \\
&= \frac{2}{\sqrt{\pi}} \int_0^x e^{-(-u)^2} (-du) \\
&= - \frac{2}{\sqrt{\pi}} \int_0^x e^{-u^2} \, du \\
&= - \operatorname{erf}(x)
\end{aligned}
$$

したがって，奇関数の関係式が得られます。

$$
\finalanswer{\operatorname{erf}(-x) = -\operatorname{erf}(x)}
$$

となります。

### (2)
相補誤差関数の積分に対して部分積分を実行します。

$$
\begin{aligned}
\int_x^\infty e^{-t^2} \, dt
&= \int_x^\infty \left( -\frac{1}{2t} \right) \frac{d}{dt}\left(e^{-t^2}\right) dt \\
&= \left[ -\frac{e^{-t^2}}{2t} \right]_x^\infty - \int_x^\infty \frac{e^{-t^2}}{2t^2} \, dt \\
&= \frac{e^{-x^2}}{2x} - \int_x^\infty \frac{e^{-t^2}}{2t^2} \, dt
\end{aligned}
$$

残った積分項に対して再び同様の部分積分を行います。

$$
\begin{aligned}
\int_x^\infty \frac{e^{-t^2}}{2t^2} \, dt
&= \int_x^\infty \left( -\frac{1}{4t^3} \right) \frac{d}{dt}\left(e^{-t^2}\right) dt \\
&= \left[ -\frac{e^{-t^2}}{4t^3} \right]_x^\infty - \int_x^\infty \frac{3e^{-t^2}}{4t^4} \, dt \\
&= \frac{e^{-x^2}}{4x^3} - \int_x^\infty \frac{3e^{-t^2}}{4t^4} \, dt
\end{aligned}
$$

これらをまとめると，積分の漸近展開は次のようになります。

$$
\int_x^\infty e^{-t^2} \, dt = \frac{e^{-x^2}}{2x} - \frac{e^{-x^2}}{4x^3} + O\left( \frac{e^{-x^2}}{x^5} \right)
$$

係数 $\frac{2}{\sqrt{\pi}}$ を掛けることにより，相補誤差関数の漸近展開が得られます。

$$
\finalanswer{\operatorname{erfc}(x) = \frac{e^{-x^2}}{\sqrt{\pi}} \left( \frac{1}{x} - \frac{1}{2x^3} \right) + O\left( \frac{e^{-x^2}}{x^5} \right)}
$$

となります。この展開は $x$ が大きい領域での熱伝導方程式の解や統計力学の確率計算で頻繁に利用されます。

===== FILE: 12special_functions/05/05_020.md =====
---
tags:
  - 標準
---

# エルミート多項式の母関数

## 問題
エルミート多項式 $H_n(x)$ の母関数は次式で定義される。
$$
G(x, t) = e^{2xt - t^2} = \sum_{n=0}^\infty \frac{H_n(x)}{n!} t^n
$$
以下の問いに答えよ。

(1) 母関数 $G(x, t)$ を $t$ について偏微分し，両辺の $t^n$ の係数を比較することにより，エルミート多項式の3項間漸化式
$$
H_{n+1}(x) - 2x H_n(x) + 2n H_{n-1}(x) = 0 \quad (n \ge 1)
$$
を導け。

(2) 母関数 $G(x, t)$ を $x$ について偏微分し，両辺の $t^n$ の係数を比較することにより，導関数に関する関係式
$$
H_n'(x) = 2n H_{n-1}(x) \quad (n \ge 1)
$$
を導け。

---

## 解答・解説

### (1)
母関数 $G(x, t) = e^{2xt - t^2}$ を変数 $t$ について偏微分します。

$$
\frac{\partial G}{\partial t} = (2x - 2t) e^{2xt - t^2} = (2x - 2t) G(x, t)
$$

この等式に母関数の級数表示を代入します。

$$
\sum_{n=0}^\infty \frac{H_n(x)}{n!} n t^{n-1} = (2x - 2t) \sum_{n=0}^\infty \frac{H_n(x)}{n!} t^n
$$

左辺のインデックスをずらし，右辺を展開して整理します。

$$
\sum_{n=0}^\infty \frac{H_{n+1}(x)}{n!} t^n = 2x \sum_{n=0}^\infty \frac{H_n(x)}{n!} t^n - 2 \sum_{n=0}^\infty \frac{H_n(x)}{n!} t^{n+1}
$$

右辺第2項の和の添字を $m = n + 1$ と置き直して $t^n$ の形にそろえます。

$$
\sum_{n=0}^\infty \frac{H_{n+1}(x)}{n!} t^n = \sum_{n=0}^\infty \frac{2x H_n(x)}{n!} t^n - \sum_{n=1}^\infty \frac{2 H_{n-1}(x)}{(n-1)!} t^n
$$

$n \ge 1$ における $t^n$ の係数を両辺で比較します。

$$
\frac{H_{n+1}(x)}{n!} = \frac{2x H_n(x)}{n!} - \frac{2 H_{n-1}(x)}{(n-1)!}
$$

両辺に $n!$ を掛けます。$\frac{n!}{(n-1)!} = n$ であることに注意して移項すると，求める漸化式が得られます。

$$
\finalanswer{H_{n+1}(x) - 2x H_n(x) + 2n H_{n-1}(x) = 0}
$$

となります。

### (2)
母関数 $G(x, t)$ を変数 $x$ について偏微分します。

$$
\frac{\partial G}{\partial x} = 2t e^{2xt - t^2} = 2t G(x, t)
$$

この式の両辺に母関数の級数表示を代入します。

$$
\sum_{n=0}^\infty \frac{H_n'(x)}{n!} t^n = 2t \sum_{n=0}^\infty \frac{H_n(x)}{n!} t^n = \sum_{n=0}^\infty \frac{2 H_n(x)}{n!} t^{n+1}
$$

右辺の和の添字をずらして $t^n$ のベキで表します。

$$
\sum_{n=0}^\infty \frac{H_n'(x)}{n!} t^n = \sum_{n=1}^\infty \frac{2 H_{n-1}(x)}{(n-1)!} t^n
$$

$n \ge 1$ について両辺の $t^n$ の係数を比較します。

$$
\frac{H_n'(x)}{n!} = \frac{2 H_{n-1}(x)}{(n-1)!}
$$

両辺に $n!$ を掛けると，導関数の関係式が得られます。

$$
\finalanswer{H_n'(x) = 2n H_{n-1}(x)}
$$

となります。この関係式と (1) の漸化式を組み合わせることで，量子調和振動子のシュレーディンガー方程式が導出されます。

===== FILE: 12special_functions/05/05_030.md =====
---
tags:
  - 標準
---

# エルミート関数の直交性と規格化

## 問題
1次元調和振動子の固有関数を構成するエルミート多項式 $H_n(x)$ の直交関係と規格化を考える。母関数は $G(x, t) = e^{2xt - t^2} = \sum_{n=0}^\infty \frac{H_n(x)}{n!} t^n$ である。以下の問いに答えよ。

(1) 母関数の積に重み関数 $e^{-x^2}$ を掛けた積分
$$
I(t, s) = \int_{-\infty}^\infty G(x, t) G(x, s) e^{-x^2} \, dx
$$
をガウス積分の公式を用いて計算せよ。

(2) $I(t, s)$ の結果を $t$ と $s$ のベキ級数に展開して係数を比較することにより，直交関係
$$
\int_{-\infty}^\infty H_m(x) H_n(x) e^{-x^2} \, dx = \sqrt{\pi} 2^n n! \, \delta_{mn}
$$
を示せ。さらに，規格化条件 $\int_{-\infty}^\infty |\psi_n(x)|^2 \, dx = 1$ を満たす調和振動子の波動関数 $\psi_n(x) = N_n H_n(x) e^{-x^2/2}$ の正の規格化定数 $N_n$ を求めよ。

---

## 解答・解説

### (1)
母関数の積と重み関数の積の指数部分をまとめます。

$$
(2xt - t^2) + (2xs - s^2) - x^2 = - x^2 + 2(t + s)x - (t^2 + s^2)
$$

$x$ について平方完成を行います。

$$
\begin{aligned}
- x^2 + 2(t + s)x - (t^2 + s^2)
&= - [x - (t + s)]^2 + (t + s)^2 - (t^2 + s^2) \\
&= - [x - (t + s)]^2 + 2ts
\end{aligned}
$$

したがって，積分は次のように変形されます。

$$
I(t, s) = e^{2ts} \int_{-\infty}^\infty e^{-[x - (t + s)]^2} \, dx
$$

ガウス積分の公式 $\int_{-\infty}^\infty e^{-u^2} \, du = \sqrt{\pi}$ を適用すると，求める積分値が得られます。

$$
\finalanswer{I(t, s) = \sqrt{\pi} e^{2ts}}
$$

となります。

### (2)
(1) で得られた結果を指数関数のマクローリン展開を用いて展開します。

$$
I(t, s) = \sqrt{\pi} \sum_{n=0}^\infty \frac{(2ts)^n}{n!} = \sum_{n=0}^\infty \frac{\sqrt{\pi} 2^n}{n!} t^n s^n
$$

一方，定義式から母関数の級数表示を代入して項別積分を行うと次のようになります。

$$
I(t, s) = \sum_{m=0}^\infty \sum_{n=0}^\infty \frac{t^m s^n}{m! n!} \int_{-\infty}^\infty H_m(x) H_n(x) e^{-x^2} \, dx
$$

両辺の $t^m s^n$ の係数を比較します。$m \neq n$ の項は存在しないため，積分値は $0$ となります。$m = n$ のとき，係数を比較すると次が成り立ちます。

$$
\frac{1}{(n!)^2} \int_{-\infty}^\infty [H_n(x)]^2 e^{-x^2} \, dx = \frac{\sqrt{\pi} 2^n}{n!}
$$

両辺に $(n!)^2$ を掛けることにより，直交関係が得られます。

$$
\finalanswer{\int_{-\infty}^\infty H_m(x) H_n(x) e^{-x^2} \, dx = \sqrt{\pi} 2^n n! \, \delta_{mn}}
$$

次に波動関数の規格化条件を計算します。

$$
\begin{aligned}
\int_{-\infty}^\infty |\psi_n(x)|^2 \, dx
&= N_n^2 \int_{-\infty}^\infty [H_n(x)]^2 e^{-x^2} \, dx \\
&= N_n^2 \sqrt{\pi} 2^n n! = 1
\end{aligned}
$$

$N_n > 0$ より，規格化定数は次のように求まります。

$$
\finalanswer{N_n = \frac{1}{\sqrt{\sqrt{\pi} 2^n n!}} = \pi^{-1/4} (2^n n!)^{-1/2}}
$$

となります。

===== FILE: 12special_functions/05/05_040.md =====
---
tags:
  - 発展
---

# ルジャンドル陪関数

## 問題
ルジャンドル多項式 $P_l(x)$ は次のルジャンドルの微分方程式を満たす。
$$
(1 - x^2) \frac{d^2 P_l}{dx^2} - 2x \frac{dP_l}{dx} + l(l + 1) P_l = 0 \quad (l \text{ は非負整数})
$$
ルジャンドル陪関数 $P_l^m(x)$（$0 \le m \le l$）は $P_l(x)$ を用いて次式で定義される。
$$
P_l^m(x) = (1 - x^2)^{m/2} \frac{d^m P_l(x)}{dx^m}
$$
以下の問いに答えよ。

(1) 関数 $u(x) = \frac{d^m P_l(x)}{dx^m}$ が満たす微分方程式を導くことにより，ルジャンドル陪関数 $P_l^m(x)$ が陪微分方程式
$$
(1 - x^2) \frac{d^2 y}{dx^2} - 2x \frac{dy}{dx} + \left[ l(l + 1) - \frac{m^2}{1 - x^2} \right] y = 0
$$
を満たすことを示せ。

(2) $l = 2$ のルジャンドル多項式 $P_2(x) = \frac{1}{2}(3x^2 - 1)$ を用いて，$P_2^1(x)$ および $P_2^2(x)$ を求めよ。

---

## 解答・解説

### (1)
ルジャンドルの微分方程式の両辺をライプニッツの公式を用いて $x$ について $m$ 回微分します。

$$
\begin{aligned}
\frac{d^m}{dx^m}\left[ (1 - x^2) P_l'' \right] &= (1 - x^2) u'' - 2mx u' - m(m - 1) u \\
\frac{d^m}{dx^m}\left[ - 2x P_l' \right] &= - 2x u' - 2m u \\
\frac{d^m}{dx^m}\left[ l(l + 1) P_l \right] &= l(l + 1) u
\end{aligned}
$$

これらを足し合わせると，$u(x)$ が満たす微分方程式が得られます。

$$
(1 - x^2) u'' - 2(m + 1)x u' + [l(l + 1) - m(m + 1)] u = 0
$$

ここで $y(x) = (1 - x^2)^{m/2} u(x)$ より $u(x) = (1 - x^2)^{-m/2} y(x)$ です。この導関数を計算して微分方程式に代入し，整理します。

$$
\begin{aligned}
u' &= (1 - x^2)^{-m/2} \left[ y' + \frac{mx}{1 - x^2} y \right] \\
u'' &= (1 - x^2)^{-m/2} \left[ y'' + \frac{2mx}{1 - x^2} y' + \left( \frac{m}{1 - x^2} + \frac{m(m + 2)x^2}{(1 - x^2)^2} \right) y \right]
\end{aligned}
$$

これらを $u$ の方程式に代入して $(1 - x^2)^{-m/2}$ で割ると，一次の微分の項の係数は次のようになります。

$$
(1 - x^2)\frac{2mx}{1 - x^2} - 2(m + 1)x = 2mx - 2mx - 2x = - 2x
$$

同様に $y$ の係数をまとめると $l(l+1) - \frac{m^2}{1-x^2}$ となります。したがって，陪微分方程式が得られます。

$$
\finalanswer{(1 - x^2) \frac{d^2 y}{dx^2} - 2x \frac{dy}{dx} + \left[ l(l + 1) - \frac{m^2}{1 - x^2} \right] y = 0}
$$

となります。

### (2)
$P_2(x) = \frac{1}{2}(3x^2 - 1)$ を順次微分します。

$$
\begin{aligned}
\frac{dP_2}{dx} &= 3x \\
\frac{d^2 P_2}{dx^2} &= 3
\end{aligned}
$$

定義式 $P_l^m(x) = (1 - x^2)^{m/2} \frac{d^m P_l}{dx^m}$ に $l = 2, m = 1$ を代入します。

$$
\finalanswer{P_2^1(x) = 3x \sqrt{1 - x^2}}
$$

次に $l = 2, m = 2$ を代入します。$(1 - x^2)^{2/2} = 1 - x^2$ より次のようになります。

$$
\finalanswer{P_2^2(x) = 3(1 - x^2)}
$$

となります。これらは水素原子の電子軌道や重力ポテンシャルの多重極展開で現れる角運動量 $l=2$（d軌道）の角度分布の基本成分です。

===== FILE: 12special_functions/05/05_050.md =====
---
tags:
  - 標準
---

# 球面調和関数の直交性

## 問題
球面座標 $(\theta, \phi)$（$0 \le \theta \le \pi, 0 \le \phi < 2\pi$）における球面調和関数 $Y_l^m(\theta, \phi)$ は次式で定義される。
$$
Y_l^m(\theta, \phi) = C_{lm} P_l^m(\cos\theta) e^{im\phi} \quad (l \ge 0, -l \le m \le l)
$$
ここで $C_{lm}$ は正の実数規格化定数であり，$P_l^m(x)$ はルジャンドル陪関数である。ルジャンドル陪関数の直交関係
$$
\int_{-1}^1 P_l^m(x) P_{l'}^m(x) \, dx = \frac{2}{2l + 1} \frac{(l + m)!}{(l - m)!} \delta_{ll'}
$$
が成り立つものとして，以下の問いに答えよ。

(1) 方位角方向の積分 $\int_0^{2\pi} e^{-im'\phi} e^{im\phi} \, d\phi$ を計算し，$m = m'$ および $m \neq m'$ の場合について値を求めよ。

(2) 全立体角に関する正規直交化条件
$$
\int_0^{2\pi} d\phi \int_0^\pi d\theta \, \sin\theta \, [Y_{l'}^{m'}(\theta, \phi)]^* Y_l^m(\theta, \phi) = \delta_{ll'} \delta_{mm'}
$$
を満たす規格化定数 $C_{lm}$ を求めよ。

---

## 解答・解説

### (1)
方位角 $\phi$ に関する積分を計算します。

$$
I_\phi = \int_0^{2\pi} e^{i(m - m')\phi} \, d\phi
$$

$m = m'$ の場合，被積分関数は $e^0 = 1$ となります。

$$
I_\phi = \int_0^{2\pi} 1 \, d\phi = 2\pi
$$

$m \neq m'$ の場合，指数関数を積分します。

$$
\begin{aligned}
I_\phi &= \left[ \frac{e^{i(m - m')\phi}}{i(m - m')} \right]_0^{2\pi} \\
&= \frac{e^{i 2\pi(m - m')} - 1}{i(m - m')}
\end{aligned}
$$

$m$ と $m'$ は整数であるため $m - m'$ も整数であり，$e^{i 2\pi(m - m')} = 1$ が成り立ちます。したがって分子が $0$ になります。クロネッカーのデルタを用いると，結果は次のようにまとまります。

$$
\finalanswer{\int_0^{2\pi} e^{-im'\phi} e^{im\phi} \, d\phi = 2\pi \delta_{mm'}}
$$

となります。

### (2)
立体角要素は $d\Omega = \sin\theta \, d\theta \, d\phi$ です。正規直交化積分の式に球面調和関数の定義を代入します。

$$
\int d\Omega \, [Y_{l'}^{m'}]^* Y_l^m = C_{l'm'} C_{lm} \left( \int_0^{2\pi} e^{i(m - m')\phi} \, d\phi \right) \left( \int_0^\pi P_{l'}^{m'}(\cos\theta) P_l^m(\cos\theta) \sin\theta \, d\theta \right)
$$

(1) の結果を代入すると $m \neq m'$ の寄与は消滅し，$m = m'$ の項のみが残ります。さらに $\theta$ の積分において変数変換 $x = \cos\theta$（$dx = -\sin\theta \, d\theta$）を行います。積分範囲は $\theta: 0 \to \pi$ が $x: 1 \to -1$ に移ります。

$$
\int_0^\pi P_{l'}^m(\cos\theta) P_l^m(\cos\theta) \sin\theta \, d\theta = \int_{-1}^1 P_{l'}^m(x) P_l^m(x) \, dx
$$

与えられたルジャンドル陪関数の直交関係の式を代入します。

$$
\int d\Omega \, [Y_{l'}^{m'}]^* Y_l^m = C_{lm}^2 \cdot 2\pi \delta_{mm'} \cdot \frac{2}{2l + 1} \frac{(l + m)!}{(l - m)!} \delta_{ll'}
$$

正規直交条件 $\int d\Omega \, [Y_{l'}^{m'}]^* Y_l^m = \delta_{ll'} \delta_{mm'}$ と比較します。

$$
C_{lm}^2 \frac{4\pi}{2l + 1} \frac{(l + m)!}{(l - m)!} = 1
$$

$C_{lm} > 0$ であるため，規格化定数は次のように求まります。

$$
\finalanswer{C_{lm} = \sqrt{\frac{2l + 1}{4\pi} \frac{(l - m)!}{(l + m)!}}}
$$

となります。

===== FILE: 12special_functions/05/05_060.md =====
---
tags:
  - 発展
---

# ベッセル関数の母関数と漸化式

## 問題
整数次数 $n$ の第1種ベッセル関数 $J_n(x)$ の母関数は次式で定義される。
$$
G(x, t) = \exp\left[ \frac{x}{2}\left(t - \frac{1}{t}\right) \right] = \sum_{n=-\infty}^\infty J_n(x) t^n
$$
以下の問いに答えよ。

(1) 母関数 $G(x, t)$ を $t$ について偏微分し，両辺の $t^n$ の係数を比較することにより，漸化式
$$
J_{n-1}(x) + J_{n+1}(x) = \frac{2n}{x} J_n(x)
$$
を導け。

(2) 母関数 $G(x, t)$ を $x$ について偏微分することにより，導関数に関する関係式
$$
J_{n-1}(x) - J_{n+1}(x) = 2 J_n'(x)
$$
を導け。また(1)と(2)の結果から，$x J_n'(x)$ を $J_n(x)$ と $J_{n+1}(x)$ で表せ。

---

## 解答・解説

### (1)
母関数 $G(x, t) = \exp\left[ \frac{x}{2}\left(t - \frac{1}{t}\right) \right]$ を $t$ について偏微分します。

$$
\frac{\partial G}{\partial t} = \frac{x}{2}\left(1 + \frac{1}{t^2}\right) G(x, t)
$$

この等式に母関数の級数表示を代入します。

$$
\sum_{n=-\infty}^\infty n J_n(x) t^{n-1} = \frac{x}{2}\left(1 + \frac{1}{t^2}\right) \sum_{n=-\infty}^\infty J_n(x) t^n
$$

右辺を展開してまとめます。

$$
\sum_{n=-\infty}^\infty n J_n(x) t^{n-1} = \frac{x}{2} \sum_{n=-\infty}^\infty J_n(x) t^n + \frac{x}{2} \sum_{n=-\infty}^\infty J_n(x) t^{n-2}
$$

両辺の和の添字を調整して $t^{n-1}$ の係数をそろえます。

$$
\sum_{n=-\infty}^\infty n J_n(x) t^{n-1} = \frac{x}{2} \sum_{n=-\infty}^\infty J_{n-1}(x) t^{n-1} + \frac{x}{2} \sum_{n=-\infty}^\infty J_{n+1}(x) t^{n-1}
$$

両辺の $t^{n-1}$ の係数を比較します。

$$
n J_n(x) = \frac{x}{2} [J_{n-1}(x) + J_{n+1}(x)]
$$

両辺に $\frac{2}{x}$ を掛けると，求める漸化式が得られます。

$$
\finalanswer{J_{n-1}(x) + J_{n+1}(x) = \frac{2n}{x} J_n(x)}
$$

となります。

### (2)
母関数 $G(x, t)$ を変数 $x$ について偏微分します。

$$
\frac{\partial G}{\partial x} = \frac{1}{2}\left(t - \frac{1}{t}\right) G(x, t)
$$

この式の両辺に母関数の級数表示を代入します。

$$
\sum_{n=-\infty}^\infty J_n'(x) t^n = \frac{1}{2} \sum_{n=-\infty}^\infty J_n(x) t^{n+1} - \frac{1}{2} \sum_{n=-\infty}^\infty J_n(x) t^{n-1}
$$

右辺の添字をずらして $t^n$ のベキにそろえます。

$$
\sum_{n=-\infty}^\infty J_n'(x) t^n = \frac{1}{2} \sum_{n=-\infty}^\infty J_{n-1}(x) t^n - \frac{1}{2} \sum_{n=-\infty}^\infty J_{n+1}(x) t^n
$$

両辺の $t^n$ の係数を比較します。

$$
J_n'(x) = \frac{1}{2}[J_{n-1}(x) - J_{n+1}(x)]
$$

両辺を2倍することにより，導関数の関係式が得られます。

$$
\finalanswer{J_{n-1}(x) - J_{n+1}(x) = 2 J_n'(x)}
$$

(1) の漸化式からこの関係式を辺々引きます。

$$
\begin{aligned}
[J_{n-1}(x) + J_{n+1}(x)] - [J_{n-1}(x) - J_{n+1}(x)] &= \frac{2n}{x} J_n(x) - 2 J_n'(x) \\
2 J_{n+1}(x) &= \frac{2n}{x} J_n(x) - 2 J_n'(x)
\end{aligned}
$$

両辺を2で割って移項し，全体に $x$ を掛けると求める関係式が得られます。

$$
\finalanswer{x J_n'(x) = n J_n(x) - x J_{n+1}(x)}
$$

となります。

===== FILE: 12special_functions/05/05_070.md =====
---
tags:
  - 基本
---

# ハミルトンの原理と運動方程式

## 問題
質量 $m$ の質点が1次元ポテンシャル $V(x)$ のもとで運動している。時刻 $t_1$ から $t_2$ までの作用積分 $S[x]$ は，ラグランジアン $L(x, \dot{x}) = \frac{1}{2}m\dot{x}^2 - V(x)$ を用いて次式で定義される。
$$
S[x] = \int_{t_1}^{t_2} L(x(t), \dot{x}(t)) \, dt
$$
ここで $\dot{x} = dx/dt$ である。以下の問いに答えよ。

(1) 両端点で $0$ となる微小変分 $\delta x(t)$（$\delta x(t_1) = \delta x(t_2) = 0$）に対する作用の変分 $\delta S$ を $\delta x$ および $\delta \dot{x} = \frac{d}{dt}(\delta x)$ の積分として表せ。

(2) 部分積分を用いて $\delta S$ を $\delta x(t)$ のみを含む積分の形に変形し，ハミルトンの原理 $\delta S = 0$ からニュートンの運動方程式 $m\ddot{x} = -\frac{dV}{dx}$ を導け。

---

## 解答・解説

### (1)
作用積分 $S[x]$ において，経路を $x(t) \to x(t) + \delta x(t)$ と微小変化させたときの1次の変分を計算します。合成関数の微分法則より次が成り立ちます。

$$
\delta S = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial x} \delta x + \frac{\partial L}{\partial \dot{x}} \delta \dot{x} \right) dt
$$

ラグランジアン $L = \frac{1}{2}m\dot{x}^2 - V(x)$ の各偏導関数を計算します。

$$
\begin{aligned}
\frac{\partial L}{\partial x} &= - \frac{dV}{dx} \\
\frac{\partial L}{\partial \dot{x}} &= m\dot{x}
\end{aligned}
$$

これらを代入すると，変分 $\delta S$ は次のように表されます。

$$
\finalanswer{\delta S = \int_{t_1}^{t_2} \left( - \frac{dV}{dx} \delta x + m\dot{x} \delta \dot{x} \right) dt}
$$

となります。

### (2)
(1) で得られた式の第2項に対して，$\delta \dot{x} = \frac{d}{dt}(\delta x)$ であることを用いて時間 $t$ について部分積分を実行します。

$$
\begin{aligned}
\int_{t_1}^{t_2} m\dot{x} \frac{d}{dt}(\delta x) \, dt
&= [m\dot{x} \delta x]_{t_1}^{t_2} - \int_{t_1}^{t_2} \frac{d}{dt}(m\dot{x}) \delta x \, dt \\
&= [m\dot{x} \delta x]_{t_1}^{t_2} - \int_{t_1}^{t_2} m\ddot{x} \delta x \, dt
\end{aligned}
$$

端点固定条件 $\delta x(t_1) = \delta x(t_2) = 0$ により，境界項は消去されます。

$$
[m\dot{x} \delta x]_{t_1}^{t_2} = 0
$$

したがって，変分 $\delta S$ は次のようにまとまります。

$$
\delta S = \int_{t_1}^{t_2} \left( - m\ddot{x} - \frac{dV}{dx} \right) \delta x(t) \, dt
$$

ハミルトンの原理 $\delta S = 0$ は，端点で $0$ となる任意の変分 $\delta x(t)$ に対して成立しなければなりません。変分法の基本補題により，被積分関数の括弧内が常に $0$ でなければなりません。

$$
- m\ddot{x} - \frac{dV}{dx} = 0
$$

移項することにより，ニュートンの運動方程式が得られます。

$$
\finalanswer{m\ddot{x} = - \frac{dV}{dx}}
$$

となります。

===== FILE: 12special_functions/05/05_080.md =====
---
tags:
  - 基本
---

# フェルマーの原理と屈折の法則

## 問題
$xy$ 平面において，$y > 0$ の領域は屈折率 $n_1$（光速 $v_1 = c/n_1$）の媒質1，$y < 0$ の領域は屈折率 $n_2$（光速 $v_2 = c/n_2$）の媒質2で満たされている。光が媒質1内の点 $A(0, h_1)$（$h_1 > 0$）から境界面上の点 $P(x, 0)$ を通過して媒質2内の点 $B(d, -h_2)$（$d > 0, h_2 > 0$）へ進む（図）。

<!-- FIGURE problem: 横軸に境界を表すx軸，縦軸にy軸。y > 0の領域に点A(0, h_1)，y < 0の領域に点B(d, -h_2)。境界面上の点P(x, 0)を経由して点Aから点Bへ結ばれる折れ線光線。法線とのなす角として入射角theta_1と屈折角theta_2を明示。 -->

以下の問いに答えよ。

(1) 光が点 $A$ から点 $P$ を経由して点 $B$ に達するまでの所要時間 $T(x)$ を求めよ。

(2) フェルマーの原理（所要時間が停留値をとる条件 $dT/dx = 0$）から，境界面の法線に対する入射角 $\theta_1$ および屈折角 $\theta_2$ の間にスネルの法則 $n_1 \sin\theta_1 = n_2 \sin\theta_2$ が成り立つことを示せ。

---

## 解答・解説

### (1)
点 $A(0, h_1)$ から境界面上の点 $P(x, 0)$ までの幾何学的距離 $L_1$ は，三平方の定理より次のようになります。

$$
L_1 = \sqrt{x^2 + h_1^2}
$$

媒質1内での光速は $v_1$ であるため，この区間の伝播時間は $t_1 = L_1 / v_1$ です。同様に，点 $P(x, 0)$ から点 $B(d, -h_2)$ までの距離 $L_2$ は次のようになります。

$$
L_2 = \sqrt{(d - x)^2 + h_2^2}
$$

媒質2内での光速は $v_2$ であるため，この区間の伝播時間は $t_2 = L_2 / v_2$ です。全所要時間 $T(x) = t_1 + t_2$ は次のように表されます。

$$
\finalanswer{T(x) = \frac{\sqrt{x^2 + h_1^2}}{v_1} + \frac{\sqrt{(d - x)^2 + h_2^2}}{v_2}}
$$

となります。

### (2)
フェルマーの原理に従い，所要時間 $T(x)$ を媒介変数の位置 $x$ について微分して停留条件 $\frac{dT}{dx} = 0$ を課します。

$$
\frac{dT}{dx} = \frac{1}{v_1} \frac{x}{\sqrt{x^2 + h_1^2}} - \frac{1}{v_2} \frac{d - x}{\sqrt{(d - x)^2 + h_2^2}} = 0
$$

境界面の法線（$y$ 軸に平行な直線）と光線の幾何学的配置を考えます。直角三角形の辺の比より，入射角 $\theta_1$ および屈折角 $\theta_2$ の正弦は次のように表されます。

$$
\begin{aligned}
\sin\theta_1 &= \frac{x}{\sqrt{x^2 + h_1^2}} \\
\sin\theta_2 &= \frac{d - x}{\sqrt{(d - x)^2 + h_2^2}}
\end{aligned}
$$

これらを微分係数の式に代入します。

$$
\frac{\sin\theta_1}{v_1} - \frac{\sin\theta_2}{v_2} = 0
$$

光速と屈折率の関係 $v_1 = c/n_1$ および $v_2 = c/n_2$ を代入します。

$$
\frac{n_1 \sin\theta_1}{c} = \frac{n_2 \sin\theta_2}{c}
$$

両辺に真空中の光速 $c$ を掛けることにより，スネルの法則が得られます。

$$
\finalanswer{n_1 \sin\theta_1 = n_2 \sin\theta_2}
$$

となります。幾何光学の基本法則が変分原理から直接導かれます。

===== FILE: 12special_functions/05/05_090.md =====
---
tags:
  - 標準
---

# 変分法による水素原子の基底状態

## 問題
原子単位系（$\hbar = m_e = e = 4\pi\varepsilon_0 = 1$）における水素原子のハミルトニアンは
$$
H = - \frac{1}{2}\nabla^2 - \frac{1}{r}
$$
で与えられる。球対称なガウス型試行関数 $\psi(r) = e^{-\alpha r^2}$（$\alpha > 0$）を用いて基底状態エネルギーの上限値を評価する。必要に応じて次の定積分の公式を用いてよい。
$$
\int_0^\infty r^2 e^{-2\alpha r^2} \, dr = \frac{\sqrt{\pi}}{4(2\alpha)^{3/2}}, \quad \int_0^\infty r^4 e^{-2\alpha r^2} \, dr = \frac{3\sqrt{\pi}}{8(2\alpha)^{5/2}}, \quad \int_0^\infty r e^{-2\alpha r^2} \, dr = \frac{1}{4\alpha}
$$
以下の問いに答えよ。

(1) エネルギー期待値 $E(\alpha) = \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle}$ を計算し，パラメータ $\alpha$ の関数として表せ。

(2) $E(\alpha)$ を最小にするパラメータの最適値 $\alpha_{\mathrm{opt}}$，およびそのときのエネルギー期待値の最小値 $E_{\mathrm{min}}$ を求めよ。

---

## 解答・解説

### (1)
全空間における体積要素は球座標で $d^3\boldsymbol{r} = 4\pi r^2 \, dr$ です。まず分母の規格化積分を計算します。

$$
\langle \psi | \psi \rangle = 4\pi \int_0^\infty r^2 e^{-2\alpha r^2} \, dr = 4\pi \frac{\sqrt{\pi}}{4(2\alpha)^{3/2}} = \left(\frac{\pi}{2\alpha}\right)^{3/2}
$$

次に運動エネルギー期待値を計算します。部分積分により勾配ベクトルの内積の積分に変換できます。$\nabla \psi = \frac{d\psi}{dr} \frac{\boldsymbol{r}}{r} = -2\alpha \boldsymbol{r} e^{-\alpha r^2}$ であるため次が成り立ちます。

$$
\begin{aligned}
\langle \psi | - \frac{1}{2}\nabla^2 | \psi \rangle
&= \frac{1}{2} \int |\nabla \psi|^2 \, d^3\boldsymbol{r} \\
&= \frac{1}{2} \int_0^\infty (4\alpha^2 r^2 e^{-2\alpha r^2}) \cdot 4\pi r^2 \, dr \\
&= 8\pi \alpha^2 \int_0^\infty r^4 e^{-2\alpha r^2} \, dr \\
&= 8\pi \alpha^2 \frac{3\sqrt{\pi}}{8(2\alpha)^{5/2}} \\
&= \frac{3}{2}\alpha \left(\frac{\pi}{2\alpha}\right)^{3/2}
\end{aligned}
$$

したがって，運動エネルギーの比率は $\frac{\langle T \rangle}{\langle \psi | \psi \rangle} = \frac{3}{2}\alpha$ となります。

続いてクーロンポテンシャルエネルギー期待値を計算します。

$$
\begin{aligned}
\langle \psi | - \frac{1}{r} | \psi \rangle
&= - 4\pi \int_0^\infty r e^{-2\alpha r^2} \, dr \\
&= - 4\pi \frac{1}{4\alpha} \\
&= - \frac{\pi}{\alpha}
\end{aligned}
$$

分母の積分で割って整理します。

$$
\frac{\langle V \rangle}{\langle \psi | \psi \rangle} = \frac{-\pi/\alpha}{(\pi/(2\alpha))^{3/2}} = - \frac{\pi}{\alpha} \frac{(2\alpha)^{3/2}}{\pi^{3/2}} = - 2 \sqrt{\frac{2\alpha}{\pi}}
$$

これらを足し合わせることにより，エネルギー期待値が得られます。

$$
\finalanswer{E(\alpha) = \frac{3}{2}\alpha - 2\sqrt{\frac{2\alpha}{\pi}}}
$$

となります。

### (2)
$E(\alpha)$ をパラメータ $\alpha$ で微分して極小値を求めます。

$$
\frac{dE}{d\alpha} = \frac{3}{2} - 2\sqrt{\frac{2}{\pi}} \frac{1}{2\sqrt{\alpha}} = \frac{3}{2} - \sqrt{\frac{2}{\pi\alpha}}
$$

停留条件 $\frac{dE}{d\alpha} = 0$ を解きます。

$$
\begin{aligned}
\sqrt{\frac{2}{\pi\alpha}} &= \frac{3}{2} \\
\frac{2}{\pi\alpha} &= \frac{9}{4}
\end{aligned}
$$

したがって，最適値は次のように決定されます。

$$
\finalanswer{\alpha_{\mathrm{opt}} = \frac{8}{9\pi}}
$$

この $\alpha_{\mathrm{opt}}$ を $E(\alpha)$ の式に代入します。

$$
\begin{aligned}
E_{\mathrm{min}}
&= \frac{3}{2}\left(\frac{8}{9\pi}\right) - 2\sqrt{\frac{2}{\pi} \frac{8}{9\pi}} \\
&= \frac{4}{3\pi} - 2 \cdot \frac{4}{3\pi} \\
&= - \frac{4}{3\pi}
\end{aligned}
$$

したがって，エネルギーの最小値は次のようになります。

$$
\finalanswer{E_{\mathrm{min}} = - \frac{4}{3\pi}}
$$

となります。数値はおよそ $-0.4244$ であり，厳密な基底状態エネルギー $-0.5$ に対する良い上限値を与えています。

===== FILE: 12special_functions/05/05_100.md =====
---
tags:
  - 発展
---

# 端点が動く変分問題

## 問題
汎関数 $I[y] = \int_{x_1}^{x_2} f(x, y, y') \, dx$ において，左端点 $(x_1, y_1)$ は固定されているが，右端点 $(x_2, y_2)$ は与えられた曲線 $y = g(x)$ 上を自由に動けるものとする（図）。

<!-- FIGURE problem: 平面上の曲線y(x)。始点(x_1, y_1)は固定点として黒丸で表示。終点は右上がりの境界曲線y = g(x)と交わっており，その交点(x_2, y_2)が曲線に沿って移動可能であることを示す矢印がある。 -->

以下の問いに答えよ。

(1) 右端点の微小変位 $(\delta x_2, \delta y_2)$ が拘束条件 $\delta y_2 = g'(x_2) \delta x_2$ を満たすとき，オイラー・ラグランジュ方程式が満たされているもとでの変分 $\delta I$ を計算し，右端点で満たされるべき横断条件（transversality condition）を導け。

(2) 原点 $(0, 0)$ から直線 $g(x) = -x + 2$ までの最短経路（$f = \sqrt{1 + (y')^2}$）を求める問題に (1) の横断条件を適用せよ。最適経路が直線 $y = g(x)$ と直交することを示し，最短距離 $d$ を求めよ。

---

## 解答・解説

### (1)
端点 $x_2$ が $\delta x_2$ だけ変化し，関数形が $y(x) \to y(x) + \delta y(x)$ と変化したときの汎関数の全変分を計算します。積分の端点の変動公式より次が成り立ちます。

$$
\delta I = \int_{x_1}^{x_2} \left[ \frac{\partial f}{\partial y} - \frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) \right] \delta y \, dx + \left[ \frac{\partial f}{\partial y'} \delta y \right]_{x_1}^{x_2} + f(x_2, y(x_2), y'(x_2)) \delta x_2
$$

オイラー・ラグランジュ方程式が満たされているとき，積分項は消失します。また左端点は固定されているため $x_1$ での変位は $0$ です。

右端点における全変位 $\delta y_2$ と内部の関数形の変分 $\delta y(x_2)$ の間には，テイラー展開の1次の関係より次の幾何学的関係が成り立ちます。

$$
\delta y_2 = \delta y(x_2) + y'(x_2) \delta x_2
$$

したがって，$\delta y(x_2) = \delta y_2 - y'(x_2) \delta x_2$ と表せます。右端点が曲線 $y = g(x)$ 上を動くことから，$\delta y_2 = g'(x_2) \delta x_2$ を代入します。

$$
\delta y(x_2) = [g'(x_2) - y'(x_2)] \delta x_2
$$

これを端点項に代入して整理します。

$$
\begin{aligned}
\delta I &= \frac{\partial f}{\partial y'}(x_2) [g'(x_2) - y'(x_2)] \delta x_2 + f(x_2) \delta x_2 \\
&= \left[ f + (g' - y') \frac{\partial f}{\partial y'} \right]_{x = x_2} \delta x_2
\end{aligned}
$$

任意の $\delta x_2$ に対して $\delta I = 0$ となることから，求める横断条件が得られます。

$$
\finalanswer{\left[ f + (g' - y') \frac{\partial f}{\partial y'} \right]_{x = x_2} = 0}
$$

となります。

### (2)
最短経路問題では $f = \sqrt{1 + (y')^2}$ であり，オイラー・ラグランジュ方程式より最適経路は直線 $y(x) = m x$（原点を通る）です。

偏導関数 $\frac{\partial f}{\partial y'} = \frac{y'}{\sqrt{1 + (y')^2}}$ を (1) の横断条件に代入します。

$$
\sqrt{1 + (y')^2} + (g' - y') \frac{y'}{\sqrt{1 + (y')^2}} = 0
$$

両辺に $\sqrt{1 + (y')^2}$ を掛けます。

$$
\begin{aligned}
1 + (y')^2 + (g' - y')y' &= 0 \\
1 + g'(x_2) y'(x_2) &= 0
\end{aligned}
$$

したがって，交点において次の直交条件が成り立ちます。

$$
\finalanswer{y'(x_2) g'(x_2) = -1}
$$

直線 $g(x) = -x + 2$ の傾きは $g' = -1$ です。したがって直交条件より最適経路の傾きは $m = y' = 1$ と決定されます。

直線 $y = x$ と直線 $y = -x + 2$ の交点を連立させて求めます。

$$
x = -x + 2 \implies 2x = 2 \implies x_2 = 1, \quad y_2 = 1
$$

原点 $(0,0)$ から交点 $(1,1)$ までの線分長が最短距離となります。

$$
d = \sqrt{1^2 + 1^2} = \sqrt{2}
$$

したがって，最短距離は次のようになります。

$$
\finalanswer{d = \sqrt{2}}
$$

となります。

===== FILE: 12special_functions/05/05_110.md =====
---
tags:
  - 発展
---

# 2階導関数を含む汎関数

## 問題
曲率や曲げ変形を記述するため，2階導関数 $y''(x)$ を含む汎関数
$$
I[y] = \int_0^L f(x, y(x), y'(x), y''(x)) \, dx
$$
を考える。以下の問いに答えよ。

(1) 両端 $x = 0, L$ において固定端境界条件 $\delta y = 0$ かつ $\delta y' = 0$ が課されているとき，変分 $\delta I = 0$ から停留関数 $y(x)$ が満たすオイラー・ポアソン方程式
$$
\frac{\partial f}{\partial y} - \frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) + \frac{d^2}{dx^2}\left(\frac{\partial f}{\partial y''}\right) = 0
$$
を導け。

(2) 曲げ剛性 $E I_z$ をもつ長さ $L$ の弾性ばりが一様荷重 $q$ を受けるとき，全エネルギー汎関数は
$$
U[y] = \int_0^L \left[ \frac{1}{2} E I_z (y'')^2 - q y \right] dx
$$
で与えられる。(1) の方程式を用いてばりのたわみ $y(x)$ が満たす微分方程式を導け。また両端固定条件 $y(0) = y'(0) = 0, y(L) = y'(L) = 0$ のもとで中央 $x = L/2$ におけるたわみ $y(L/2)$ を求めよ。

---

## 解答・解説

### (1)
変分 $\delta y(x)$ を与えたときの汎関数の1次の変分を計算します。

$$
\delta I = \int_0^L \left( \frac{\partial f}{\partial y} \delta y + \frac{\partial f}{\partial y'} \delta y' + \frac{\partial f}{\partial y''} \delta y'' \right) dx
$$

第2項に対して部分積分を1回，第3項に対して部分積分を2回実行します。

$$
\int_0^L \frac{\partial f}{\partial y'} \delta y' \, dx = \left[ \frac{\partial f}{\partial y'} \delta y \right]_0^L - \int_0^L \frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) \delta y \, dx
$$

$$
\begin{aligned}
\int_0^L \frac{\partial f}{\partial y''} \delta y'' \, dx
&= \left[ \frac{\partial f}{\partial y''} \delta y' \right]_0^L - \int_0^L \frac{d}{dx}\left(\frac{\partial f}{\partial y''}\right) \delta y' \, dx \\
&= \left[ \frac{\partial f}{\partial y''} \delta y' \right]_0^L - \left[ \frac{d}{dx}\left(\frac{\partial f}{\partial y''}\right) \delta y \right]_0^L + \int_0^L \frac{d^2}{dx^2}\left(\frac{\partial f}{\partial y''}\right) \delta y \, dx
\end{aligned}
$$

両端で $\delta y = 0$ および $\delta y' = 0$ であるため，すべての境界項は $0$ になります。

したがって，変分 $\delta I$ は次のようにまとまります。

$$
\delta I = \int_0^L \left[ \frac{\partial f}{\partial y} - \frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) + \frac{d^2}{dx^2}\left(\frac{\partial f}{\partial y''}\right) \right] \delta y \, dx
$$

任意の変分 $\delta y$ に対して $\delta I = 0$ が成り立つことから，オイラー・ポアソン方程式が得られます。

$$
\finalanswer{\frac{\partial f}{\partial y} - \frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) + \frac{d^2}{dx^2}\left(\frac{\partial f}{\partial y''}\right) = 0}
$$

となります。

### (2)
$f(x, y, y', y'') = \frac{1}{2} E I_z (y'')^2 - q y$ に対し，各導関数を計算します。

$$
\frac{\partial f}{\partial y} = - q, \quad \frac{\partial f}{\partial y'} = 0, \quad \frac{\partial f}{\partial y''} = E I_z y''
$$

これらを (1) の方程式に代入します。

$$
- q + \frac{d^2}{dx^2}(E I_z y'') = 0
$$

曲げ剛性 $E I_z$ は一定であるため，たわみの微分方程式が得られます。

$$
\finalanswer{E I_z \frac{d^4 y}{dx^4} = q}
$$

両辺を $x$ について4回積分します。

$$
y(x) = \frac{q}{24 E I_z} x^4 + C_3 x^3 + C_2 x^2 + C_1 x + C_0
$$

境界条件 $y(0) = 0$ および $y'(0) = 0$ より，$C_0 = 0, C_1 = 0$ と定まります。したがって $y(x) = \frac{q}{24 E I_z} x^2 (x^2 + A x + B)$ と置けます。$x = L$ での境界条件を適用します。

$$
\begin{aligned}
y(L) &= 0 \implies L^2 + A L + B = 0 \\
y'(L) &= 0 \implies 4L^2 + 3A L + 2B = 0
\end{aligned}
$$

連立方程式を解くと $A = -2L, B = L^2$ が得られます。したがって，たわみ曲線は次のように決定されます。

$$
y(x) = \frac{q}{24 E I_z} x^2 (L - x)^2
$$

中央 $x = L/2$ を代入します。

$$
y(L/2) = \frac{q}{24 E I_z} \left(\frac{L}{2}\right)^2 \left(\frac{L}{2}\right)^2 = \frac{q}{24 E I_z} \frac{L^4}{16}
$$

分母を計算すると $24 \times 16 = 384$ となります。したがって，中央のたわみは次のようになります。

$$
\finalanswer{y(L/2) = \frac{q L^4}{384 E I_z}}
$$

となります。

===== FILE: 12special_functions/05/05_120.md =====
---
tags:
  - 発展
---

# 固有値問題の変分による特徴づけ

## 問題
エルミート演算子 $\hat{A}$ の固有値問題を考える。固有値 $\lambda_n$ と正規直交固有状態 $|u_n\rangle$（$n = 1, 2, \dots$）は $\hat{A}|u_n\rangle = \lambda_n |u_n\rangle$ および $\langle u_m | u_n \rangle = \delta_{mn}$ を満たし，固有値は昇順 $\lambda_1 \le \lambda_2 \le \lambda_3 \le \dots$ に並んでいるものとする。以下の問いに答えよ。

(1) 任意の規格化された状態 $|\psi\rangle$（$\langle \psi | \psi \rangle = 1$）に対し，期待値 $\langle \hat{A} \rangle = \langle \psi | \hat{A} | \psi \rangle$ が不等式 $\langle \hat{A} \rangle \ge \lambda_1$ を満たすことを示せ。

(2) 基底状態 $|u_1\rangle$ と直交する規格化された状態（$\langle u_1 | \psi \rangle = 0, \langle \psi | \psi \rangle = 1$）の空間において，期待値 $\langle \hat{A} \rangle$ の最小値が第1励起状態の固有値 $\lambda_2$ に一致することを示せ。また，規格化拘束条件のもとで未定乗数 $\lambda$ を用いた停留条件から固有値方程式 $\hat{A}|\psi\rangle = \lambda |\psi\rangle$ を導け。

---

## 解答・解説

### (1)
任意の規格化された状態 $|\psi\rangle$ を完全系をなす固有状態 $\{|u_n\rangle\}$ で展開します。

$$
|\psi\rangle = \sum_{n=1}^\infty c_n |u_n\rangle \quad (c_n = \langle u_n | \psi \rangle)
$$

規格化条件 $\langle \psi | \psi \rangle = 1$ を展開係数で表します。

$$
\langle \psi | \psi \rangle = \sum_{m,n=1}^\infty c_m^* c_n \langle u_m | u_n \rangle = \sum_{n=1}^\infty |c_n|^2 = 1
$$

この展開を用いて期待値 $\langle \hat{A} \rangle$ を計算します。

$$
\begin{aligned}
\langle \psi | \hat{A} | \psi \rangle
&= \sum_{m,n=1}^\infty c_m^* c_n \langle u_m | \hat{A} | u_n \rangle \\
&= \sum_{m,n=1}^\infty c_m^* c_n \lambda_n \delta_{mn} \\
&= \sum_{n=1}^\infty \lambda_n |c_n|^2
\end{aligned}
$$

すべての $n$ に対して $\lambda_n \ge \lambda_1$ であるため，次の不等式が成り立ちます。

$$
\sum_{n=1}^\infty \lambda_n |c_n|^2 \ge \lambda_1 \sum_{n=1}^\infty |c_n|^2 = \lambda_1
$$

したがって，求める不等式が得られます。

$$
\finalanswer{\langle \psi | \hat{A} | \psi \rangle \ge \lambda_1}
$$

となります。等号成立は状態 $|\psi\rangle$ が固有値 $\lambda_1$ に属する固有空間にある場合に限られます。

### (2)
基底状態との直交条件 $\langle u_1 | \psi \rangle = 0$ より，展開係数の初項は $c_1 = 0$ となります。規格化条件は $\sum_{n=2}^\infty |c_n|^2 = 1$ となります。

この直交部分空間における期待値を評価します。

$$
\langle \psi | \hat{A} | \psi \rangle = \sum_{n=2}^\infty \lambda_n |c_n|^2 \ge \lambda_2 \sum_{n=2}^\infty |c_n|^2 = \lambda_2
$$

ここで $|\psi\rangle = |u_2\rangle$（$c_2 = 1$，$n \ge 3$ で $c_n = 0$）と選ぶと期待値は厳密に $\lambda_2$ に一致します。したがって，最小値は $\lambda_2$ となります。

$$
\finalanswer{\min_{\langle u_1 | \psi \rangle = 0, \langle \psi | \psi \rangle = 1} \langle \psi | \hat{A} | \psi \rangle = \lambda_2}
$$

次に，拘束条件 $\langle \psi | \psi \rangle = 1$ のもとで期待値 $\langle \psi | \hat{A} | \psi \rangle$ を停留させるため，ラグランジュの未定乗数 $\lambda$ を導入して汎関数を定義します。

$$
J[|\psi\rangle, \langle\psi|] = \langle \psi | \hat{A} | \psi \rangle - \lambda (\langle \psi | \psi \rangle - 1)
$$

ブラ $\langle\psi|$ の独立な微小変分 $\langle\delta \psi|$ に対する変分を計算します。

$$
\delta J = \langle \delta \psi | (\hat{A} |\psi\rangle - \lambda |\psi\rangle) = 0
$$

任意の $\langle\delta \psi|$ に対してこの式が成り立つことから，固有値方程式が導かれます。

$$
\finalanswer{\hat{A}|\psi\rangle = \lambda |\psi\rangle}
$$

となります。未定乗数 $\lambda$ 自身が物理的な固有値に対応します。

===== END =====