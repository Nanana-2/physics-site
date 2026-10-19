===== FILE: 11complex_analysis/01/01_010.md =====
---
tags:
  - 基本
---

# 極形式とド・モアブルの定理

## 問題
複素数 $w = -1 + \sqrt{3}i$ について考える（図）。以下の問いに答えよ。

<!-- FIGURE problem: 複素平面（横軸を実軸 Re z，縦軸を虚軸 Im z とし，原点 O を明記）。点 w = -1 + \sqrt{3}i を第2象限にプロットし，原点からの線分と実軸の正の向きとのなす角 \theta を図示する。 -->

(1) 複素数 $w$ の絶対値 $r = |w|$ および偏角 $\theta = \arg w$（$0 \le \theta < 2\pi$）を求めよ。

(2) 方程式 $z^3 = w$ を満たす複素数 $z$ をすべて極形式 $z = R(\cos\phi + i\sin\phi)$（$R > 0$，$0 \le \phi < 2\pi$）で表せ。

(3) (2)で求めた3つの解を複素平面上の点としたとき，これらを頂点とする三角形の面積 $S$ を求めよ。

---

## 解答・解説

### (1)
複素数 $w = x + iy$（$x, y$ は実数）の絶対値は $r = \sqrt{x^2 + y^2}$ で定義されます。実部 $x = -1$ と虚部 $y = \sqrt{3}$ を代入すると，

$$
\begin{aligned}
r &= \sqrt{(-1)^2 + (\sqrt{3})^2} \\
&= \sqrt{1 + 3} \\
&= \finalanswer{r = 2}
\end{aligned}
$$

となります。

偏角 $\theta$ は $\cos\theta = x/r = -1/2$ かつ $\sin\theta = y/r = \sqrt{3}/2$ を満たします。$0 \le \theta < 2\pi$ の範囲でこれらを満たす角を求めると，

$$
\finalanswer{\theta = \frac{2\pi}{3}}
$$

となります。

### (2)
求める複素数を極形式 $z = R(\cos\phi + i\sin\phi)$（$R > 0$）とおきます。ド・モアブルの定理を適用すると，

$$
z^3 = R^3 (\cos 3\phi + i\sin 3\phi)
$$

となります。(1)の結果より $w = 2(\cos(2\pi/3) + i\sin(2\pi/3))$ であるため，方程式 $z^3 = w$ の両辺の絶対値と偏角を比較します。絶対値について，

$$
R^3 = 2
$$

が成り立ち，$R$ は正の実数であることから，

$$
R = 2^{1/3}
$$

となります。

偏角については，整数 $k$ を用いて，

$$
3\phi = \frac{2\pi}{3} + 2k\pi
$$

と表せます。両辺を $3$ で割ると，

$$
\phi = \frac{2\pi}{9} + \frac{2k\pi}{3}
$$

となります。$0 \le \phi < 2\pi$ の範囲に入る解を得るため $k = 0, 1, 2$ を代入すると，

$$
\begin{aligned}
\phi_0 &= \frac{2\pi}{9} \\
\phi_1 &= \frac{8\pi}{9} \\
\phi_2 &= \frac{14\pi}{9}
\end{aligned}
$$

が得られます。したがって，求める解は，

$$
\finalanswer{z = 2^{1/3}\left(\cos\frac{2\pi}{9} + i\sin\frac{2\pi}{9}\right),\quad 2^{1/3}\left(\cos\frac{8\pi}{9} + i\sin\frac{8\pi}{9}\right),\quad 2^{1/3}\left(\cos\frac{14\pi}{9} + i\sin\frac{14\pi}{9}\right)}
$$

となります。

### (3)
(2)で求めた3つの解は，複素平面上において原点を中心とする半径 $R = 2^{1/3}$ の同一円周上に位置し，偏角がそれぞれ $2\pi/3$ ずつ離れています。したがって，これら3点を頂点とする図形は正三角形となります。

正三角形の外接円の半径を $R$ とすると，1辺の長さ $a$ は余弦定理より，

$$
\begin{aligned}
a^2 &= R^2 + R^2 - 2R^2 \cos\frac{2\pi}{3} \\
&= 2R^2 - 2R^2 \left(-\frac{1}{2}\right) \\
&= 3R^2
\end{aligned}
$$

となります。1辺の長さが $a$ の正三角形の面積 $S$ は，

$$
S = \frac{\sqrt{3}}{4} a^2
$$

で与えられます。ここに $a^2 = 3R^2$ および $R = 2^{1/3}$ を代入すると，

$$
\begin{aligned}
S &= \frac{\sqrt{3}}{4} \cdot 3(2^{1/3})^2 \\
&= \frac{3\sqrt{3}}{4} \cdot 2^{2/3} \\
&= \finalanswer{S = \frac{3\sqrt{3}}{2^{4/3}}}
\end{aligned}
$$

となります。

===== FILE: 11complex_analysis/01/020.md =====
---
tags:
  - 基本
---

# 複素関数による写像

## 問題
複素数 $z = x + iy$（$x, y$ は実数）を $w = u + iv$（$u, v$ は実数）に移す複素関数 $w = f(z)$ による写像を考える。以下の問いに答えよ。

(1) 関数 $w = z^2$ により，複素平面上の直線 $x = c$（$c$ は正の定数）が $w$ 平面上で描く曲線の関係式を $u$ と $v$ を用いて表せ。

(2) 関数 $w = 1/z$ により，複素平面上の円 $|z - 1| = 1$（ただし原点 $z = 0$ を除く）が $w$ 平面上で描く図形の方程式を $u$ と $v$ を用いて表せ。

---

## 解答・解説

### (1)
$z = c + iy$ を関数 $w = z^2$ に代入して展開します。

$$
\begin{aligned}
w &= (c + iy)^2 \\
&= c^2 - y^2 + 2icy
\end{aligned}
$$

となります。実部と虚部を比較することにより，

$$
\begin{aligned}
u &= c^2 - y^2 \\
v &= 2cy
\end{aligned}
$$

が得られます。$c > 0$ であるため，虚部の式から実数パラメータ $y$ について解くと，

$$
y = \frac{v}{2c}
$$

となります。これを実部の式に代入すると，

$$
\begin{aligned}
u &= c^2 - \left(\frac{v}{2c}\right)^2 \\
&= \finalanswer{u = c^2 - \frac{v^2}{4c^2}}
\end{aligned}
$$

となります。これは $w$ 平面において頂点が $(c^2, 0)$ であり，軸が $u$ 軸に平行な放物線を表します。

<!-- FIGURE solution (1): w 平面（横軸 u，縦軸 v，原点 O）。頂点を (c^2, 0) とし，負の u 軸方向に開いた放物線 u = c^2 - v^2/(4c^2) を描く。 -->

### (2)
$w = 1/z$ より，$z = 1/w$ が成り立ちます。これを与えられた円の方程式 $|z - 1| = 1$ に代入すると，

$$
\left|\frac{1}{w} - 1\right| = 1
$$

となります。通分すると，

$$
\left|\frac{1 - w}{w}\right| = 1
$$

が得られます。両辺に分母の絶対値 $|w|$ を掛けると，

$$
|1 - w| = |w|
$$

となります。両辺を2乗して複素数の絶対値の性質 $|A|^2 = A \bar{A}$ を用いて展開します。

$$
\begin{aligned}
(1 - w)(1 - \bar{w}) &= w \bar{w} \\
1 - w - \bar{w} + w\bar{w} &= w\bar{w} \\
1 - (w + \bar{w}) &= 0
\end{aligned}
$$

となります。ここで $w = u + iv$ より $w + \bar{w} = 2u$ であるため，

$$
1 - 2u = 0
$$

が得られます。したがって，求める直線の方程式は，

$$
\finalanswer{u = \frac{1}{2}}
$$

となります。反転写像 $w = 1/z$ によって，原点を通る円は原点を通らない直線へと写されます。

===== FILE: 11complex_analysis/01/030.md =====
---
tags:
  - 基本
---

# コーシー・リーマンの関係

## 問題
複素数 $z = x + iy$（$x, y$ は実数）を変数とする関数 $f(z) = u(x, y) + i v(x, y)$（$u, v$ は実数値関数）の微分可能性について考える。以下の問いに答えよ。

(1) 複素共役をとる関数 $f(z) = \bar{z}$ の実部 $u$ および虚部 $v$ について，コーシー・リーマンの関係式が複素平面上のいかなる点でも成り立たないことを示せ。

(2) 関数 $f(z) = (x^2 - y^2 + 2x) + i(2xy + 2y)$ が複素平面の全域で正則であることを確かめ，導関数 $f'(z)$ を $z$ を用いた式で表せ。

---

## 解答・解説

### (1)
複素数 $z = x + iy$ の複素共役は $\bar{z} = x - iy$ です。したがって，実部 $u(x, y)$ と虚部 $v(x, y)$ は，

$$
\begin{aligned}
u(x, y) &= x \\
v(x, y) &= -y
\end{aligned}
$$

となります。それぞれの偏導関数を計算すると，

$$
\begin{aligned}
\frac{\partial u}{\partial x} &= 1, \quad \frac{\partial u}{\partial y} = 0 \\
\frac{\partial v}{\partial x} &= 0, \quad \frac{\partial v}{\partial y} = -1
\end{aligned}
$$

となります。コーシー・リーマンの関係式は，

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

で与えられます。ここで，

$$
\frac{\partial u}{\partial x} = 1 \neq -1 = \frac{\partial v}{\partial y}
$$

であるため，第1式がすべての点で成立しません。したがって，

$$
\finalanswer{\frac{\partial u}{\partial x} \neq \frac{\partial v}{\partial y}}
$$

となり，複素平面上のいかなる点においてもコーシー・リーマンの関係式は成り立ちません。

### (2)
与えられた関数の実部と虚部は，

$$
\begin{aligned}
u(x, y) &= x^2 - y^2 + 2x \\
v(x, y) &= 2xy + 2y
\end{aligned}
$$

です。各変数に関する1階偏導関数を計算すると，

$$
\begin{aligned}
\frac{\partial u}{\partial x} &= 2x + 2, \quad \frac{\partial u}{\partial y} = -2y \\
\frac{\partial v}{\partial x} &= 2y, \quad \frac{\partial v}{\partial y} = 2x + 2
\end{aligned}
$$

となります。これら4つの偏導関数は多項式であるため全平面で連続であり，

$$
\begin{aligned}
\frac{\partial u}{\partial x} &= \frac{\partial v}{\partial y} = 2x + 2 \\
\frac{\partial u}{\partial y} &= -\frac{\partial v}{\partial x} = -2y
\end{aligned}
$$

が全平面で成り立ちます。偏導関数が連続かつコーシー・リーマンの関係式を満たすため，$f(z)$ は全平面で正則です。

正則関数の導関数は実軸方向の微分係数として，

$$
f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}
$$

と計算できます。求めた偏導関数を代入すると，

$$
\begin{aligned}
f'(z) &= (2x + 2) + i(2y) \\
&= 2(x + iy) + 2 \\
&= \finalanswer{2z + 2}
\end{aligned}
$$

となります。

===== FILE: 11complex_analysis/01/040.md =====
---
tags:
  - 標準
---

# 調和関数と共役調和関数

## 問題
2変数の実数値関数 $u(x, y) = x^3 - 3xy^2 + 2x$ について考える。以下の問いに答えよ。

(1) $u(x, y)$ がラプラス方程式 $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ を満たす調和関数であることを示せ。

(2) $u(x, y)$ を実部とする正則関数 $f(z) = u(x, y) + iv(x, y)$（$z = x + iy$）が存在するとき，共役調和関数 $v(x, y)$ を求めよ。ただし $v(0, 0) = 0$ とする。

(3) (2)で得られた正則関数 $f(z)$ を $z$ の関数として表せ。

---

## 解答・解説

### (1)
関数 $u(x, y)$ の $x$ および $y$ に関する1階偏導関数を計算します。

$$
\begin{aligned}
\frac{\partial u}{\partial x} &= 3x^2 - 3y^2 + 2 \\
\frac{\partial u}{\partial y} &= -6xy
\end{aligned}
$$

となります。さらに2階偏導関数を計算すると，

$$
\begin{aligned}
\frac{\partial^2 u}{\partial x^2} &= 6x \\
\frac{\partial^2 u}{\partial y^2} &= -6x
\end{aligned}
$$

が得られます。両者の和をとると，

$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 6x + (-6x) = \finalanswer{0}
$$

となるため，$u(x, y)$ は全平面でラプラス方程式を満たし，調和関数であることが示されます。

### (2)
$f(z) = u + iv$ が正則であるための条件として，コーシー・リーマンの関係式が成り立ちます。

$$
\frac{\partial v}{\partial y} = \frac{\partial u}{\partial x}, \quad \frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y}
$$

第1式に (1) で求めた $\partial u/\partial x$ を代入すると，

$$
\frac{\partial v}{\partial y} = 3x^2 - 3y^2 + 2
$$

となります。この両辺を $y$ について積分すると，任意の実数値関数 $g(x)$ を用いて，

$$
v(x, y) = 3x^2 y - y^3 + 2y + g(x)
$$

と表せます。この式を $x$ で偏微分すると，

$$
\frac{\partial v}{\partial x} = 6xy + g'(x)
$$

となります。コーシー・リーマンの関係式の第2式 $\partial v/\partial x = -\partial u/\partial y = 6xy$ と比較すると，

$$
6xy + g'(x) = 6xy
$$

より，$g'(x) = 0$ が導かれます。したがって $g(x) = C$（$C$ は実定数）となります。条件 $v(0, 0) = 0$ を適用すると，

$$
v(0, 0) = C = 0
$$

となります。したがって，求める共役調和関数は，

$$
\finalanswer{v(x, y) = 3x^2 y - y^3 + 2y}
$$

となります。

### (3)
(2)で求めた実部 $u$ と虚部 $v$ から複素関数 $f(z)$ を構成します。

$$
\begin{aligned}
f(z) &= u(x, y) + iv(x, y) \\
&= (x^3 - 3xy^2 + 2x) + i(3x^2 y - y^3 + 2y)
\end{aligned}
$$

実部と虚部の項を整理してまとめます。

$$
\begin{aligned}
f(z) &= (x^3 + 3ix^2 y - 3xy^2 - iy^3) + 2(x + iy) \\
&= (x + iy)^3 + 2(x + iy)
\end{aligned}
$$

ここで $z = x + iy$ を代入すると，

$$
\finalanswer{f(z) = z^3 + 2z}
$$

となります。

===== FILE: 11complex_analysis/01/050.md =====
---
tags:
  - 標準
---

# 指数・対数・べき関数と分枝

## 問題
複素数 $z$ に対する対数関数およびべき関数の多価性と分枝について考える。対数の主値 $\operatorname{Log} z$ は偏角の範囲を $-\pi < \operatorname{Arg} z \le \pi$ として $\operatorname{Log} z = \ln |z| + i \operatorname{Arg} z$ と定義される。以下の問いに答えよ。

(1) 複素数 $z = -1 + i$ に対する対数の主値 $\operatorname{Log} z$ を求めよ。

(2) べき関数 $i^i$ のとり得るすべての値を求めよ。

(3) 主値をとる平方根関数 $f(z) = \exp\left(\frac{1}{2}\operatorname{Log} z\right)$ について，負の実軸上の点 $x$（$x < 0$）に対して，上半平面から近づく極限 $\lim_{\epsilon \to +0} f(x + i\epsilon)$ および下半平面から近づく極限 $\lim_{\epsilon \to +0} f(x - i\epsilon)$ をそれぞれ $x$ を用いて表せ。

---

## 解答・解説

### (1)
複素数 $z = -1 + i$ の絶対値は，

$$
|z| = \sqrt{(-1)^2 + 1^2} = \sqrt{2}
$$

となります。主値をとる偏角 $\operatorname{Arg} z$ は $-\pi < \operatorname{Arg} z \le \pi$ の範囲で $\cos\theta = -1/\sqrt{2}$ かつ $\sin\theta = 1/\sqrt{2}$ を満たすため，

$$
\operatorname{Arg} z = \frac{3\pi}{4}
$$

となります。これらを主値の定義式に代入すると，

$$
\begin{aligned}
\operatorname{Log} z &= \ln\sqrt{2} + i\frac{3\pi}{4} \\
&= \finalanswer{\frac{1}{2}\ln 2 + i\frac{3\pi}{4}}
\end{aligned}
$$

となります。

### (2)
一般の複素数 $\alpha, \beta$ に対するべき関数 $\alpha^\beta$ は，多価関数である対数 $\log\alpha$ を用いて，

$$
\alpha^\beta = \exp(\beta \log\alpha)
$$

と定義されます。$\alpha = i$ の対数は，整数 $k$ を用いて，

$$
\log i = \ln |i| + i \arg i = \ln 1 + i\left(\frac{\pi}{2} + 2k\pi\right) = i\left(\frac{\pi}{2} + 2k\pi\right)
$$

と表されます。これを用いて $i^i$ を計算すると，

$$
\begin{aligned}
i^i &= \exp(i \log i) \\
&= \exp\left(i \cdot i\left(\frac{\pi}{2} + 2k\pi\right)\right) \\
&= \finalanswer{\exp\left(-\frac{\pi}{2} - 2k\pi\right)} \quad (k \text{ は任意の整数})
\end{aligned}
$$

となります。すべての値は実数となります。

### (3)
負の実数 $x < 0$ に対し，$r = |x| = -x > 0$ とおきます。微小な $\epsilon > 0$ に対して上半平面から近づく点 $z = x + i\epsilon$ の極形式を考えると，$\epsilon \to +0$ の極限で絶対値は $r$ に近づき，偏角は $\pi$ に下から近づきます。したがって，

$$
\lim_{\epsilon \to +0} \operatorname{Log}(x + i\epsilon) = \ln r + i\pi
$$

となります。これを関数 $f(z)$ に代入すると，

$$
\begin{aligned}
\lim_{\epsilon \to +0} f(x + i\epsilon) &= \exp\left(\frac{1}{2}(\ln r + i\pi)\right) \\
&= \sqrt{r} \exp\left(i\frac{\pi}{2}\right) \\
&= i\sqrt{-x}
\end{aligned}
$$

となります。

同様に，下半平面から近づく点 $z = x - i\epsilon$ については，$\epsilon \to +0$ の極限で偏角は $-\pi$ に上から近づきます。したがって，

$$
\lim_{\epsilon \to +0} \operatorname{Log}(x - i\epsilon) = \ln r - i\pi
$$

となります。これを関数 $f(z)$ に代入すると，

$$
\begin{aligned}
\lim_{\epsilon \to +0} f(x - i\epsilon) &= \exp\left(\frac{1}{2}(\ln r - i\pi)\right) \\
&= \sqrt{r} \exp\left(-i\frac{\pi}{2}\right) \\
&= -i\sqrt{-x}
\end{aligned}
$$

となります。よって，それぞれの極限値は，

$$
\finalanswer{\lim_{\epsilon \to +0} f(x + i\epsilon) = i\sqrt{-x}}, \quad \finalanswer{\lim_{\epsilon \to +0} f(x - i\epsilon) = -i\sqrt{-x}}
$$

となります。負の実軸を横切る際に符号が反転し，不連続面（分岐切断）が存在することが分かります。

===== FILE: 11complex_analysis/02/02_010.md =====
---
tags:
  - 基本
---

# 複素線積分

## 問題
複素平面上において，原点 $0$ から点 $1 + i$ に至る3つの異なる経路 $C_1, C_2, C_3$ を考える。
- 経路 $C_1$：原点から実軸上を $1$ まで進み，そこから直線に沿って $1 + i$ まで進む折れ線経路。
- 経路 $C_2$：原点から点 $1 + i$ を直接結ぶ線分経路。
- 経路 $C_3$：放物線 $y = x^2$ に沿って原点から点 $1 + i$ まで進む曲線経路。

関数 $f(z) = \bar{z}$（複素共役）について，以下の問いに答えよ。

(1) 経路 $C_1$ に沿う線積分 $\int_{C_1} \bar{z}\,dz$ の値を求めよ。

(2) 経路 $C_2$ に沿う線積分 $\int_{C_2} \bar{z}\,dz$ の値を求めよ。

(3) 経路 $C_3$ に沿う線積分 $\int_{C_3} \bar{z}\,dz$ の値を求めよ。

---

## 解答・解説

### (1)
経路 $C_1$ を実軸上の区間 $C_{1a}$（$0 \to 1$）と垂直な区間 $C_{1b}$（$1 \to 1+i$）の2つに分割して計算します。

$C_{1a}$ 上では $z = t$（$t$ は $0$ から $1$ まで変化）とパラメータ表示できるため，$dz = dt$ および $\bar{z} = t$ となります。積分を実行すると，

$$
\int_{C_{1a}} \bar{z}\,dz = \int_0^1 t\,dt = \left[\frac{t^2}{2}\right]_0^1 = \frac{1}{2}
$$

となります。

$C_{1b}$ 上では $z = 1 + it$（$t$ は $0$ から $1$ まで変化）とパラメータ表示できるため，$dz = i\,dt$ および $\bar{z} = 1 - it$ となります。積分を実行すると，

$$
\begin{aligned}
\int_{C_{1b}} \bar{z}\,dz &= \int_0^1 (1 - it)i\,dt \\
&= \int_0^1 (i + t)\,dt \\
&= \left[it + \frac{t^2}{2}\right]_0^1 \\
&= \frac{1}{2} + i
\end{aligned}
$$

となります。経路全体の積分は両者の和となるため，

$$
\begin{aligned}
\int_{C_1} \bar{z}\,dz &= \frac{1}{2} + \left(\frac{1}{2} + i\right) \\
&= \finalanswer{1 + i}
\end{aligned}
$$

となります。

### (2)
線分経路 $C_2$ 上では，実部と虚部が等しいため $z = t + it = (1 + i)t$（$t$ は $0$ から $1$ まで変化）とパラメータ表示できます。微分および複素共役は，

$$
\begin{aligned}
dz &= (1 + i)\,dt \\
\bar{z} &= (1 - i)t
\end{aligned}
$$

となります。被積分関数と微分の積を作ると，

$$
\bar{z}\,dz = (1 - i)t \cdot (1 + i)\,dt = (1 - i^2)t\,dt = 2t\,dt
$$

となります。これを $t = 0$ から $1$ まで積分すると，

$$
\begin{aligned}
\int_{C_2} \bar{z}\,dz &= \int_0^1 2t\,dt \\
&= \left[t^2\right]_0^1 \\
&= \finalanswer{1}
\end{aligned}
$$

となります。

### (3)
放物線経路 $C_3$ 上では $y = x^2$ より，$x = t$ とおくと $z = t + it^2$（$t$ は $0$ から $1$ まで変化）と表せます。このとき，

$$
\begin{aligned}
dz &= (1 + 2it)\,dt \\
\bar{z} &= t - it^2
\end{aligned}
$$

となります。積を計算して展開すると，

$$
\begin{aligned}
\bar{z}\,dz &= (t - it^2)(1 + 2it)\,dt \\
&= (t + 2it^2 - it^2 - 2i^2 t^3)\,dt \\
&= (t + 2t^3 + it^2)\,dt
\end{aligned}
$$

となります。各項を $t = 0$ から $1$ まで積分すると，

$$
\begin{aligned}
\int_{C_3} \bar{z}\,dz &= \int_0^1 (t + 2t^3 + it^2)\,dt \\
&= \left[\frac{t^2}{2} + \frac{t^4}{2} + i\frac{t^3}{3}\right]_0^1 \\
&= \frac{1}{2} + \frac{1}{2} + \frac{i}{3} \\
&= \finalanswer{1 + \frac{i}{3}}
\end{aligned}
$$

となります。非正則関数 $f(z) = \bar{z}$ の積分では，端点が一致していても値が経路に依存することが確認されます。

===== FILE: 11complex_analysis/02/02_020.md =====
---
tags:
  - 標準
---

# コーシーの積分定理

## 問題
複素平面における閉曲線に沿う複素線積分について考える。閉曲線はすべて反時計回りの向きを持つものとする。以下の問いに答えよ。

(1) 整数 $n$ に対し，原点を中心とする単位円周 $C: |z| = 1$ に沿う線積分
$$
I_n = \oint_C z^n \,dz
$$
の値を求めよ。

(2) 原点を内部に含む任意の単純閉曲線 $C_1$ について，線積分
$$
J = \oint_{C_1} \frac{1}{z} \,dz
$$
の値を，コーシーの積分定理と経路の変形を用いて求めよ。

(3) 関数 $f(z) = \frac{e^z}{z^2 + 4}$ に対し，原点を中心とする単位円周 $C: |z| = 1$ に沿う線積分
$$
K = \oint_C \frac{e^z}{z^2 + 4} \,dz
$$
の値を求めよ。

---

## 解答・解説

### (1)
単位円周 $C$ 上の点を極形式 $z = e^{i\theta}$（$\theta$ は $0$ から $2\pi$ まで変化）でパラメータ表示します。微分は $dz = i e^{i\theta} d\theta$ となります。これらを積分に代入すると，

$$
\begin{aligned}
I_n &= \int_0^{2\pi} (e^{i\theta})^n \cdot i e^{i\theta} \,d\theta \\
&= i \int_0^{2\pi} e^{i(n+1)\theta} \,d\theta
\end{aligned}
$$

となります。

$n \neq -1$ の場合，指数関数を積分すると，

$$
\begin{aligned}
I_n &= i \left[\frac{e^{i(n+1)\theta}}{i(n+1)}\right]_0^{2\pi} \\
&= \frac{1}{n+1} \left(e^{i2\pi(n+1)} - 1\right) \\
&= 0
\end{aligned}
$$

となります。

$n = -1$ の場合，被積分関数の指数部分は $0$ となり，

$$
I_{-1} = i \int_0^{2\pi} 1 \,d\theta = 2\pi i
$$

となります。以上より，

$$
\finalanswer{I_n = \begin{cases} 2\pi i & (n = -1) \\ 0 & (n \neq -1) \end{cases}}
$$

となります。

### (2)
原点を取り囲む単純閉曲線 $C_1$ の内部に，原点を中心とし $C_1$ の内部に完全に含まれる十分に小さな半径 $\epsilon > 0$ の円周 $C_\epsilon: |z| = \epsilon$（反時計回り）をとります。

$C_1$ と $C_\epsilon$ の間に挟まれた2重連結領域において，関数 $g(z) = 1/z$ は特異点を持たず正則です。コーシーの積分定理を経路変形に適用すると，外側の閉曲線に沿う積分は内側の円周に沿う積分に等しくなります。

$$
J = \oint_{C_1} \frac{1}{z} \,dz = \oint_{C_\epsilon} \frac{1}{z} \,dz
$$

円周 $C_\epsilon$ を $z = \epsilon e^{i\theta}$（$\theta$ は $0$ から $2\pi$）とパラメータ表示すると，$dz = i\epsilon e^{i\theta} d\theta$ となり，

$$
\begin{aligned}
\oint_{C_\epsilon} \frac{1}{z} \,dz &= \int_0^{2\pi} \frac{1}{\epsilon e^{i\theta}} \cdot i\epsilon e^{i\theta} \,d\theta \\
&= i \int_0^{2\pi} d\theta \\
&= \finalanswer{2\pi i}
\end{aligned}
$$

となります。したがって，原点を囲む任意の単純閉曲線について値は常に $2\pi i$ となります。

### (3)
被積分関数 $f(z) = \frac{e^z}{z^2 + 4}$ の特異点は，分母が $0$ となる点，すなわち，

$$
z^2 + 4 = 0 \implies z = \pm 2i
$$

です。これらの特異点の原点からの距離は $| \pm 2i | = 2$ です。一方，積分路 $C$ は原点を中心とする半径 $1$ の円であるため，特異点 $z = \pm 2i$ はすべて $C$ の外部に存在します。

したがって，関数 $f(z)$ は単連結領域である円 $|z| \le 1$ の内部および境界上で正則です。コーシーの積分定理より，正則関数の閉曲線積分は $0$ となるため，

$$
\finalanswer{K = 0}
$$

となります。

===== FILE: 11complex_analysis/02/02_030.md =====
---
tags:
  - 標準
---

# コーシーの積分公式

## 問題
複素平面において，原点を中心とする半径 $2$ の反時計回りの円周 $C: |z| = 2$ に沿う複素線積分を考える。以下の問いに答えよ。

(1) コーシーの積分公式を用いて，積分
$$
I_1 = \oint_C \frac{e^z}{z - 1} \,dz
$$
の値を求めよ。

(2) 部分分数分解を用いて，積分
$$
I_2 = \oint_C \frac{e^z}{z^2 - 1} \,dz
$$
の値を求めよ。

(3) 積分
$$
I_3 = \oint_C \frac{1}{(z - 3)(z + 1)} \,dz
$$
の値を求めよ。

---

## 解答・解説

### (1)
関数 $f(z) = e^z$ は複素平面全域で正則です。被積分関数の特異点は $z = 1$ であり，これは積分路である円 $C: |z| = 2$ の内部に含まれます。

コーシーの積分公式によれば，領域内で正則な関数 $f(z)$ とその内部の点 $z_0$ について，

$$
\oint_C \frac{f(z)}{z - z_0} \,dz = 2\pi i f(z_0)
$$

が成り立ちます。$z_0 = 1$ および $f(z) = e^z$ を適用すると，

$$
\begin{aligned}
I_1 &= 2\pi i e^1 \\
&= \finalanswer{2\pi e i}
\end{aligned}
$$

となります。

### (2)
分母を因数分解し，被積分関数の分数部分を部分分数に分解します。

$$
\frac{1}{z^2 - 1} = \frac{1}{(z - 1)(z + 1)} = \frac{1}{2}\left(\frac{1}{z - 1} - \frac{1}{z + 1}\right)
$$

特異点 $z = 1$ および $z = -1$ は，いずれも絶対値が $1$ であるため円 $C: |z| = 2$ の内部にあります。部分分数分解の式を代入して積分を2つに分けます。

$$
I_2 = \frac{1}{2} \oint_C \frac{e^z}{z - 1} \,dz - \frac{1}{2} \oint_C \frac{e^z}{z + 1} \,dz
$$

それぞれの積分にコーシーの積分公式を適用すると，

$$
\begin{aligned}
\oint_C \frac{e^z}{z - 1} \,dz &= 2\pi i e^1 = 2\pi e i \\
\oint_C \frac{e^z}{z + 1} \,dz &= 2\pi i e^{-1} = 2\pi e^{-1} i
\end{aligned}
$$

となります。これらを代入して整理すると，

$$
\begin{aligned}
I_2 &= \frac{1}{2} (2\pi e i - 2\pi e^{-1} i) \\
&= \pi i (e - e^{-1}) \\
&= \finalanswer{2\pi i \sinh 1}
\end{aligned}
$$

となります。

### (3)
被積分関数の分母の零点は $z = 3$ と $z = -1$ です。円 $C: |z| = 2$ に対して，$z = -1$ は内部にありますが，$z = 3$ は $|3| = 3 > 2$ であるため外部にあります。

そこで，$C$ の内部および境界上で正則となる関数，

$$
g(z) = \frac{1}{z - 3}
$$

を定義します。被積分関数をこの $g(z)$ を用いて表すと，

$$
\frac{1}{(z - 3)(z + 1)} = \frac{g(z)}{z - (-1)}
$$

となります。$z_0 = -1$ は $C$ の内部の点であるため，コーシーの積分公式を適用すると，

$$
\begin{aligned}
I_3 &= \oint_C \frac{g(z)}{z - (-1)} \,dz \\
&= 2\pi i g(-1)
\end{aligned}
$$

となります。$g(-1)$ の値を計算して代入すると，

$$
\begin{aligned}
I_3 &= 2\pi i \left(\frac{1}{-1 - 3}\right) \\
&= 2\pi i \left(-\frac{1}{4}\right) \\
&= \finalanswer{-\frac{\pi i}{2}}
\end{aligned}
$$

となります。

===== FILE: 11complex_analysis/02/02_040.md =====
---
tags:
  - 標準
---

# 導関数の積分表示

## 問題
正則関数 $f(z)$ の高階導関数に関する積分表示（グルサの公式）について考える。原点を中心とする半径 $2$ の反時計回りの円周を $C: |z| = 2$ とする。以下の問いに答えよ。

(1) 積分
$$
I_1 = \oint_C \frac{e^{2z}}{(z - 1)^2} \,dz
$$
の値を求めよ。

(2) 積分
$$
I_2 = \oint_C \frac{\cos z}{z^3} \,dz
$$
の値を求めよ。

(3) 積分
$$
I_3 = \oint_C \frac{z^3}{(z - 1)^2 (z + 3)} \,dz
$$
の値を求めよ。

---

## 解答・解説

### (1)
コーシーの導関数の積分表示によれば，領域内で正則な関数 $f(z)$ とその内部の点 $z_0$ に対して，

$$
f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_C \frac{f(z)}{(z - z_0)^{n+1}} \,dz
$$

が成り立ちます。したがって，線積分は，

$$
\oint_C \frac{f(z)}{(z - z_0)^{n+1}} \,dz = \frac{2\pi i}{n!} f^{(n)}(z_0)
$$

と計算できます。

本問では $f(z) = e^{2z}$，$z_0 = 1$（$C$ の内部），$n = 1$ に対応します。導関数を求めると，

$$
f'(z) = 2e^{2z}
$$

となります。公式を適用すると，

$$
\begin{aligned}
I_1 &= \frac{2\pi i}{1!} f'(1) \\
&= 2\pi i \cdot 2e^2 \\
&= \finalanswer{4\pi i e^2}
\end{aligned}
$$

となります。

### (2)
被積分関数の分母の零点は $z = 0$ であり，円 $C: |z| = 2$ の内部にあります。分子の関数 $f(z) = \cos z$ は全平面で正則です。

本問は $z_0 = 0$，$n = 2$ の場合に対応します。$f(z)$ の2階導関数を求めると，

$$
\begin{aligned}
f'(z) &= -\sin z \\
f''(z) &= -\cos z
\end{aligned}
$$

となります。導関数の積分表示を適用すると，

$$
\begin{aligned}
I_2 &= \frac{2\pi i}{2!} f''(0) \\
&= \pi i (-\cos 0) \\
&= \finalanswer{-\pi i}
\end{aligned}
$$

となります。

### (3)
分母の零点は $z = 1$ と $z = -3$ です。$z = 1$ は円 $C: |z| = 2$ の内部にありますが，$z = -3$ は $| -3 | = 3 > 2$ であるため $C$ の外部にあります。

そこで，$C$ の内部および境界上で正則となる関数，

$$
g(z) = \frac{z^3}{z + 3}
$$

を定義します。被積分関数は $\frac{g(z)}{(z - 1)^2}$ と表せ，$z_0 = 1$（$n = 1$）の1階微分の積分表示が適用できます。商の微分法を用いて $g'(z)$ を計算すると，

$$
\begin{aligned}
g'(z) &= \frac{3z^2(z + 3) - z^3 \cdot 1}{(z + 3)^2} \\
&= \frac{3z^3 + 9z^2 - z^3}{(z + 3)^2} \\
&= \frac{2z^3 + 9z^2}{(z + 3)^2}
\end{aligned}
$$

となります。$z = 1$ を代入すると，

$$
g'(1) = \frac{2(1)^3 + 9(1)^2}{(1 + 3)^2} = \frac{11}{16}
$$

が得られます。導関数の積分表示より，

$$
\begin{aligned}
I_3 &= \frac{2\pi i}{1!} g'(1) \\
&= 2\pi i \cdot \frac{11}{16} \\
&= \finalanswer{\frac{11\pi i}{8}}
\end{aligned}
$$

となります。

===== FILE: 11complex_analysis/02/02_050.md =====
---
tags:
  - 発展
---

# リウヴィルの定理と代数学の基本定理

## 問題
全平面で正則な関数（整関数）の性質に関するリウヴィルの定理と，その応用について考える。以下の問いに答えよ。

(1) 整関数 $f(z)$ に対し，任意の点 $z_0$ を中心とする半径 $R > 0$ の円周 $C_R: z - z_0 = R e^{i\theta}$（$0 \le \theta < 2\pi$）をとる。グルサの公式を用いて，不等式
$$
|f'(z_0)| \le \frac{M(R)}{R}
$$
が成り立つことを示せ。ただし $M(R) = \max_{|z - z_0| = R} |f(z)|$ とする。

(2) 整関数 $f(z)$ が有界である，すなわちある正の実定数 $M$ が存在してすべての $z \in \mathbb{C}$ に対し $|f(z)| \le M$ を満たすとき，$f(z)$ は定数関数であることを示せ。

(3) 複素係数の $n$ 次多項式 $P(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$（$n \ge 1$，$a_n \neq 0$）が複素平面上に零点を持たないと仮定し，(2)のリウヴィルの定理を適用することにより，方程式 $P(z) = 0$ が少なくとも1つの複素数解を持つこと（代数学の基本定理）を示せ。

---

## 解答・解説

### (1)
グルサの公式（導関数の積分表示）において $n = 1$ とすると，

$$
f'(z_0) = \frac{1}{2\pi i} \oint_{C_R} \frac{f(z)}{(z - z_0)^2} \,dz
$$

が成り立ちます。両辺の絶対値をとり，積分の絶対値に関する不等式を適用します。円周 $C_R$ 上では $|z - z_0| = R$ であり，$|f(z)| \le M(R)$ が成り立ちます。

$$
\begin{aligned}
|f'(z_0)| &= \left| \frac{1}{2\pi i} \oint_{C_R} \frac{f(z)}{(z - z_0)^2} \,dz \right| \\
&\le \frac{1}{2\pi} \oint_{C_R} \frac{|f(z)|}{|z - z_0|^2} \,|dz| \\
&\le \frac{1}{2\pi} \frac{M(R)}{R^2} \oint_{C_R} |dz|
\end{aligned}
$$

円周 $C_R$ の周長は $\oint_{C_R} |dz| = 2\pi R$ であるため，

$$
\begin{aligned}
|f'(z_0)| &\le \frac{1}{2\pi} \frac{M(R)}{R^2} \cdot 2\pi R \\
&= \finalanswer{\frac{M(R)}{R}}
\end{aligned}
$$

が得られ，コーシーの評価式が示されます。

### (2)
仮定より，全平面で $|f(z)| \le M$ が成り立ちます。任意の点 $z_0 \in \mathbb{C}$ を中心とする半径 $R$ の円上での最大値について $M(R) \le M$ であるため，(1)の評価式より，

$$
|f'(z_0)| \le \frac{M}{R}
$$

が任意の $R > 0$ に対して成立します。ここで $f(z)$ は整関数であるため半径 $R$ はいくらでも大きく選ぶことができます。両辺で $R \to \infty$ の極限をとると，

$$
\lim_{R \to \infty} \frac{M}{R} = 0
$$

となります。絶対値は非負であることから，

$$
|f'(z_0)| = 0 \implies \finalanswer{f'(z_0) = 0}
$$

が導かれます。点 $z_0$ は任意に選べるため，複素平面の全域で $f'(z) = 0$ となります。全域で導関数が $0$ である正則関数は定数であるため，$f(z)$ は定数関数であることが示されます。

### (3)
多項式 $P(z)$ が複素平面上に根を持たないと仮定します。このとき，逆数関数，

$$
g(z) = \frac{1}{P(z)}
$$

は分母が $0$ にならないため，全複素平面で正則な関数（整関数）となります。

次に，$|z| \to \infty$ における $P(z)$ の振る舞いを評価します。最高次数の項でくくり出すと，

$$
P(z) = a_n z^n \left(1 + \frac{a_{n-1}}{a_n z} + \cdots + \frac{a_0}{a_n z^n}\right)
$$

となります。$n \ge 1$ かつ $a_n \neq 0$ であるため，$|z| \to \infty$ のとき括弧内の項は $1$ に収束し，$|P(z)| \to \infty$ となります。したがって，

$$
\lim_{|z| \to \infty} |g(z)| = \lim_{|z| \to \infty} \frac{1}{|P(z)|} = 0
$$

が得られます。極限が $0$ であることから，ある半径 $R_0 > 0$ が存在して，$|z| > R_0$ では $|g(z)| \le 1$ となります。また，閉円板 $|z| \le R_0$ は有界閉集合であり，$g(z)$ は連続であるため，最大値の定理よりこの領域内でも有界です。

したがって，$g(z)$ は全複素平面で有界な整関数となります。(2)のリウヴィルの定理より $g(z)$ は定数でなければならず，その逆数である $P(z)$ も定数となります。これは $P(z)$ が $n \ge 1$ 次の多項式であるという前提に矛盾します。

したがって，背理法により，

$$
\finalanswer{P(z) = 0 \text{ は少なくとも1つの複素数解を持つ}}
$$

ことが示されます。

===== FILE: 11complex_analysis/03/03_010.md =====
---
tags:
  - 基本
---

# テイラー展開と収束半径

## 問題
複素関数のテイラー展開と特異点との関係について考える。以下の問いに答えよ。

(1) 関数 $f(z) = \frac{1}{1 - z}$ の $z = 0$ のまわりのテイラー展開および収束半径 $R_1$ を求めよ。

(2) 関数 $g(z) = \frac{1}{3 - z}$ の $z = 1$ のまわりのテイラー展開および収束半径 $R_2$ を求めよ。

(3) 関数 $h(z) = \frac{1}{z^2 + 4}$ の $z = 1$ のまわりのテイラー展開の収束半径 $R_3$ を，特異点までの距離を幾何学的に考慮して求めよ。

---

## 解答・解説

### (1)
等比数列の和の公式を利用します。公比が $z$ である等比級数は $|z| < 1$ で収束し，

$$
\begin{aligned}
\frac{1}{1 - z} &= 1 + z + z^2 + \cdots \\
&= \finalanswer{\sum_{n=0}^\infty z^n}
\end{aligned}
$$

となります。

この級数が絶対収束するための条件は $|z| < 1$ です。したがって，収束半径は，

$$
\finalanswer{R_1 = 1}
$$

となります。これは展開の中心 $z = 0$ から特異点 $z = 1$ までの距離と一致します。

### (2)
$z = 1$ のまわりのテイラー展開を得るため，分母を展開の基底である $z - 1$ を用いて表します。

$$
\begin{aligned}
3 - z &= 2 - (z - 1) \\
&= 2 \left(1 - \frac{z - 1}{2}\right)
\end{aligned}
$$

これを関数 $g(z)$ に代入し，公比を $\frac{z - 1}{2}$ とする幾何級数として展開します。

$$
\begin{aligned}
g(z) &= \frac{1}{2} \cdot \frac{1}{1 - \frac{z - 1}{2}} \\
&= \frac{1}{2} \sum_{n=0}^\infty \left(\frac{z - 1}{2}\right)^n \\
&= \finalanswer{\sum_{n=0}^\infty \frac{1}{2^{n+1}} (z - 1)^n}
\end{aligned}
$$

となります。

この級数の収束条件は，

$$
\left|\frac{z - 1}{2}\right| < 1 \iff |z - 1| < 2
$$

であるため，収束半径は，

$$
\finalanswer{R_2 = 2}
$$

となります。中心 $z = 1$ から特異点 $z = 3$ までの距離 $|3 - 1| = 2$ と一致します。

### (3)
正則関数のテイラー級数の収束円は，展開の中心から最も近い特異点を通る円となります。

関数 $h(z) = \frac{1}{z^2 + 4}$ の特異点は，分母が $0$ となる点，

$$
z^2 + 4 = 0 \implies z = \pm 2i
$$

です。展開の中心は $z_0 = 1$ であるため，中心から各特異点までの距離 $d$ を計算します。

$$
\begin{aligned}
d &= |1 - (\pm 2i)| \\
&= \sqrt{1^2 + (\mp 2)^2} \\
&= \sqrt{1 + 4} \\
&= \sqrt{5}
\end{aligned}
$$

特異点 $2i$ および $-2i$ までの距離はともに $\sqrt{5}$ です。したがって，収束半径はこれら特異点までの距離に等しく，

$$
\finalanswer{R_3 = \sqrt{5}}
$$

となります。

===== FILE: 11complex_analysis/03/03_020.md =====
---
tags:
  - 標準
---

# ローラン展開

## 問題
有理関数 $f(z) = \frac{1}{(z - 1)(z - 2)}$ の円環領域におけるローラン展開について考える。以下の問いに答えよ。

(1) 円環領域 $1 < |z| < 2$ における $z = 0$ のまわりのローラン展開を求めよ。

(2) 領域 $|z| > 2$ における $z = 0$ のまわりのローラン展開を求めよ。

(3) 穴あき円板 $0 < |z - 1| < 1$ における $z = 1$ のまわりのローラン展開を求めよ。

---

## 解答・解説

### (1)
まず，被積分関数を部分分数に分解します。

$$
f(z) = \frac{1}{z - 2} - \frac{1}{z - 1}
$$

領域 $1 < |z| < 2$ では，$|z/2| < 1$ かつ $|1/z| < 1$ が成り立ちます。したがって，第1項は $z/2$ のべき，第2項は $1/z$ のべきとして展開します。

第1項について，

$$
\begin{aligned}
\frac{1}{z - 2} &= -\frac{1}{2} \cdot \frac{1}{1 - \frac{z}{2}} \\
&= -\frac{1}{2} \sum_{n=0}^\infty \left(\frac{z}{2}\right)^n \\
&= -\sum_{n=0}^\infty \frac{z^n}{2^{n+1}}
\end{aligned}
$$

となります。

第2項について，

$$
\begin{aligned}
-\frac{1}{z - 1} &= -\frac{1}{z} \cdot \frac{1}{1 - \frac{1}{z}} \\
&= -\frac{1}{z} \sum_{n=0}^\infty \left(\frac{1}{z}\right)^n \\
&= -\sum_{n=1}^\infty \frac{1}{z^n}
\end{aligned}
$$

となります。これらを合わせると，求めるローラン展開は，

$$
\finalanswer{f(z) = -\sum_{n=1}^\infty \frac{1}{z^n} - \sum_{n=0}^\infty \frac{z^n}{2^{n+1}}}
$$

となります。負のべき（主要部）と正のべき（正則部）の両方が現れます。

### (2)
領域 $|z| > 2$ では，$|2/z| < 1$ および $|1/z| < 1$ が成り立ちます。したがって，両方の項を $1/z$ のべきで展開します。

第1項について，

$$
\begin{aligned}
\frac{1}{z - 2} &= \frac{1}{z} \cdot \frac{1}{1 - \frac{2}{z}} \\
&= \frac{1}{z} \sum_{n=0}^\infty \left(\frac{2}{z}\right)^n \\
&= \sum_{n=0}^\infty \frac{2^n}{z^{n+1}} \\
&= \sum_{n=1}^\infty \frac{2^{n-1}}{z^n}
\end{aligned}
$$

となります。

(1)で求めた第2項の展開 $-\frac{1}{z-1} = -\sum_{n=1}^\infty \frac{1}{z^n}$ と合わせると，

$$
\begin{aligned}
f(z) &= \sum_{n=1}^\infty \frac{2^{n-1}}{z^n} - \sum_{n=1}^\infty \frac{1}{z^n} \\
&= \finalanswer{\sum_{n=1}^\infty \frac{2^{n-1} - 1}{z^n}}
\end{aligned}
$$

となります。

### (3)
$z = 1$ のまわりの展開であるため，基底を $z - 1$ とします。第2項はすでに基底のべき乗 $-\frac{1}{z - 1}$ の形になっています。

第1項について，分母を変形します。

$$
z - 2 = (z - 1) - 1 = -(1 - (z - 1))
$$

領域 $0 < |z - 1| < 1$ において公比は $|z - 1| < 1$ であるため，等比級数として展開します。

$$
\begin{aligned}
\frac{1}{z - 2} &= -\frac{1}{1 - (z - 1)} \\
&= -\sum_{n=0}^\infty (z - 1)^n
\end{aligned}
$$

となります。したがって，関数全体のローラン展開は，

$$
\finalanswer{f(z) = -\frac{1}{z - 1} - \sum_{n=0}^\infty (z - 1)^n}
$$

となります。主要部は $-(z - 1)^{-1}$ の1項のみであり，$z = 1$ が1位の極であることが確認されます。

===== FILE: 11complex_analysis/03/03_030.md =====
---
tags:
  - 標準
---

# 特異点の分類

## 問題
複素関数における孤立特異点の分類について考える。孤立特異点は，ローラン展開の主要部（負のべきの項）の現れ方によって，除去可能特異点，極，真性特異点に分類される。以下の問いに答えよ。

(1) 関数 $f(z) = \frac{\sin z}{z}$ の $z = 0$ におけるローラン展開を求め，特異点 $z = 0$ の種類を答えよ。

(2) 関数 $g(z) = \frac{1 - \cos z}{z^4}$ の $z = 0$ におけるローラン展開を求め，特異点 $z = 0$ の種類を答えよ。極である場合はその位数も答えよ。

(3) 関数 $h(z) = \exp\left(\frac{1}{z}\right)$ の $z = 0$ におけるローラン展開を求め，特異点 $z = 0$ の種類を答えよ。

---

## 解答・解説

### (1)
$\sin z$ の $z = 0$ のまわりのマクローリン展開は，

$$
\sin z = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} z^{2n+1} = z - \frac{z^3}{3!} + \frac{z^5}{5!} - \cdots
$$

で与えられます。これを $z$ で割ることにより，$f(z)$ のローラン展開を求めます。

$$
\begin{aligned}
f(z) &= \frac{1}{z} \left(z - \frac{z^3}{6} + \frac{z^5}{120} - \cdots\right) \\
&= \finalanswer{1 - \frac{z^2}{6} + \frac{z^4}{120} - \cdots}
\end{aligned}
$$

となります。

この展開には $z$ の負のべきの項（主要部）が一切現れず，正則部のみで構成されています。したがって，特異点 $z = 0$ は，

$$
\finalanswer{\text{除去可能特異点}}
$$

となります。

### (2)
$\cos z$ のマクローリン展開は，

$$
\cos z = 1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \frac{z^6}{6!} + \cdots
$$

です。分子の式を展開すると，

$$
1 - \cos z = \frac{z^2}{2} - \frac{z^4}{24} + \frac{z^6}{720} - \cdots
$$

となります。これを $z^4$ で割ると，

$$
\begin{aligned}
g(z) &= \frac{1}{z^4} \left(\frac{z^2}{2} - \frac{z^4}{24} + \frac{z^6}{720} - \cdots\right) \\
&= \finalanswer{\frac{1}{2z^2} - \frac{1}{24} + \frac{z^2}{720} - \cdots}
\end{aligned}
$$

が得られます。

主要部として有限個の負のべきが現れており，最も次数の低い（絶対値の大きい）負のべきは $z^{-2}$ です。したがって，特異点 $z = 0$ は，

$$
\finalanswer{2\text{位の極}}
$$

となります。

### (3)
指数関数 $e^w$ のマクローリン展開は，

$$
e^w = \sum_{n=0}^\infty \frac{w^n}{n!} = 1 + w + \frac{w^2}{2!} + \frac{w^3}{3!} + \cdots
$$

です。ここで $w = 1/z$ と置換すると，

$$
\begin{aligned}
h(z) &= \sum_{n=0}^\infty \frac{1}{n!} \left(\frac{1}{z}\right)^n \\
&= \finalanswer{1 + \frac{1}{z} + \frac{1}{2z^2} + \frac{1}{6z^3} + \cdots}
\end{aligned}
$$

となります。

この展開において，主要部には無限個の負のべきの項が存在します。したがって，特異点 $z = 0$ は，

$$
\finalanswer{\text{真性特異点}}
$$

となります。

===== FILE: 11complex_analysis/03/03_040.md =====
---
tags:
  - 発展
---

# 解析接続の入口

## 問題
べき級数の収束円の外側への解析接続について考える。以下の問いに答えよ。

(1) べき級数
$$
f_1(z) = \sum_{n=0}^\infty z^n
$$
の収束領域を求めよ。

(2) $f_1(z)$ が収束領域内で表す正則関数を $F(z)$ とする。$F(z)$ を点 $z_0 = -1/2$ のまわりでテイラー展開した級数を
$$
f_2(z) = \sum_{n=0}^\infty a_n \left(z + \frac{1}{2}\right)^n
$$
とする。各係数 $a_n$ およびこの級数 $f_2(z)$ の収束半径 $R_2$ を求めよ。

(3) 点 $z = -1$ は $f_1(z)$ の収束領域の外側にあるが，$f_2(z)$ の収束領域の内部にあることを示し，級数展開を用いて値 $f_2(-1)$ を求めよ。

---

## 解答・解説

### (1)
べき級数 $\sum_{n=0}^\infty c_n z^n$ の係数は $c_n = 1$ です。ダランベールの公式より，収束半径 $R_1$ は，

$$
R_1 = \lim_{n \to \infty} \left| \frac{c_n}{c_{n+1}} \right| = 1
$$

となります。したがって，求める収束領域は，

$$
\finalanswer{|z| < 1}
$$

となります。

### (2)
領域 $|z| < 1$ において，無限等比級数の和は，

$$
F(z) = \frac{1}{1 - z}
$$

となります。点 $z_0 = -1/2$ のまわりで展開するため，分母を変形します。

$$
\begin{aligned}
1 - z &= 1 - \left(z + \frac{1}{2} - \frac{1}{2}\right) \\
&= \frac{3}{2} - \left(z + \frac{1}{2}\right) \\
&= \frac{3}{2} \left[1 - \frac{2}{3}\left(z + \frac{1}{2}\right)\right]
\end{aligned}
$$

これを $F(z)$ に代入し，公比を $\frac{2}{3}(z + 1/2)$ とする等比級数として展開します。

$$
\begin{aligned}
F(z) &= \frac{2}{3} \cdot \frac{1}{1 - \frac{2}{3}\left(z + \frac{1}{2}\right)} \\
&= \frac{2}{3} \sum_{n=0}^\infty \left(\frac{2}{3}\right)^n \left(z + \frac{1}{2}\right)^n \\
&= \sum_{n=0}^\infty \frac{2^{n+1}}{3^{n+1}} \left(z + \frac{1}{2}\right)^n
\end{aligned}
$$

したがって，展開係数は，

$$
\finalanswer{a_n = \frac{2^{n+1}}{3^{n+1}}}
$$

となります。

収束条件は $\left|\frac{2}{3}\left(z + \frac{1}{2}\right)\right| < 1$ であるため，

$$
\left|z + \frac{1}{2}\right| < \frac{3}{2}
$$

となります。したがって，収束半径は，

$$
\finalanswer{R_2 = \frac{3}{2}}
$$

となります。

### (3)
点 $z = -1$ について，絶対値は $| -1 | = 1$ であり，$|z| < 1$ を満たさないため $f_1(z)$ の収束領域の外側（境界上）にあります。

一方，展開の中心 $z_0 = -1/2$ からの距離を計算すると，

$$
\left|-1 - \left(-\frac{1}{2}\right)\right| = \left|-\frac{1}{2}\right| = \frac{1}{2}
$$

となります。これは収束半径 $R_2 = 3/2$ よりも小さいため，

$$
\finalanswer{\left|-1 + \frac{1}{2}\right| = \frac{1}{2} < \frac{3}{2}}
$$

となり，点 $z = -1$ は級数 $f_2(z)$ の収束領域の内部に含まれることが示されます。

この点での値 $f_2(-1)$ を級数から計算すると，

$$
\begin{aligned}
f_2(-1) &= \sum_{n=0}^\infty \frac{2^{n+1}}{3^{n+1}} \left(-1 + \frac{1}{2}\right)^n \\
&= \frac{2}{3} \sum_{n=0}^\infty \frac{2^n}{3^n} \left(-\frac{1}{2}\right)^n \\
&= \frac{2}{3} \sum_{n=0}^\infty \left(-\frac{1}{3}\right)^n
\end{aligned}
$$

となります。初項 $2/3$，公比 $-1/3$ の無限等比級数の和の公式を適用すると，

$$
\begin{aligned}
f_2(-1) &= \frac{2}{3} \cdot \frac{1}{1 - \left(-\frac{1}{3}\right)} \\
&= \frac{2}{3} \cdot \frac{3}{4} \\
&= \finalanswer{\frac{1}{2}}
\end{aligned}
$$

となります。これは元の関数 $F(-1) = 1/(1 - (-1)) = 1/2$ と一致し，解析接続が実現されていることが示されます。

===== FILE: 11complex_analysis/04/04_010.md =====
---
tags:
  - 基本
---

# 留数の計算

## 問題
複素関数における孤立特異点での留数の計算について考える。以下の問いに答えよ。

(1) 関数 $f(z) = \frac{1}{z^2 + 1}$ の特異点 $z = i$ における留数 $\operatorname{Res}(f, i)$ を求めよ。

(2) 関数 $g(z) = \frac{e^z}{(z - 1)^2}$ の特異点 $z = 1$ における留数 $\operatorname{Res}(g, 1)$ を求めよ。

(3) 関数 $h(z) = z^2 \sin\left(\frac{1}{z}\right)$ の特異点 $z = 0$ における留数 $\operatorname{Res}(h, 0)$ を求めよ。

---

## 解答・解説

### (1)
関数 $f(z)$ の分母を因数分解すると，

$$
f(z) = \frac{1}{(z - i)(z + i)}
$$

となります。$z = i$ は1位の極です。1位の極における留数の公式を適用すると，

$$
\begin{aligned}
\operatorname{Res}(f, i) &= \lim_{z \to i} (z - i) f(z) \\
&= \lim_{z \to i} \frac{1}{z + i} \\
&= \frac{1}{2i} \\
&= \finalanswer{-\frac{i}{2}}
\end{aligned}
$$

となります。

### (2)
関数 $g(z)$ において，分母が $(z - 1)^2$ であり分子は $z = 1$ で $e \neq 0$ であるため，$z = 1$ は2位の極です。$m$ 位の極における留数の公式，

$$
\operatorname{Res}(g, z_0) = \frac{1}{(m-1)!} \lim_{z \to z_0} \frac{d^{m-1}}{dz^{m-1}} \left[(z - z_0)^m g(z)\right]
$$

において $m = 2$，$z_0 = 1$ とすると，

$$
\begin{aligned}
\operatorname{Res}(g, 1) &= \frac{1}{1!} \lim_{z \to 1} \frac{d}{dz} \left[(z - 1)^2 \frac{e^z}{(z - 1)^2}\right] \\
&= \lim_{z \to 1} \frac{d}{dz} [e^z] \\
&= \lim_{z \to 1} e^z \\
&= \finalanswer{e}
\end{aligned}
$$

となります。

### (3)
特異点 $z = 0$ は真性特異点であるため，ローラン展開を行って $1/z$ の係数を特定します。$\sin w$ のマクローリン展開，

$$
\sin w = w - \frac{w^3}{3!} + \frac{w^5}{5!} - \cdots
$$

に $w = 1/z$ を代入します。

$$
\sin\left(\frac{1}{z}\right) = \frac{1}{z} - \frac{1}{6z^3} + \frac{1}{120z^5} - \cdots
$$

この展開に $z^2$ を掛けます。

$$
\begin{aligned}
h(z) &= z^2 \left(\frac{1}{z} - \frac{1}{6z^3} + \frac{1}{120z^5} - \cdots\right) \\
&= z - \frac{1}{6z} + \frac{1}{120z^3} - \cdots
\end{aligned}
$$

留数はローラン展開における $z^{-1}$ の係数として定義されます。係数を比較すると，

$$
\finalanswer{\operatorname{Res}(h, 0) = -\frac{1}{6}}
$$

となります。

===== FILE: 11complex_analysis/04/04_020.md =====
---
tags:
  - 標準
---

# 有理関数の実積分

## 問題
留数定理を用いて，実軸全域にわたる定積分
$$
I = \int_{-\infty}^\infty \frac{1}{x^4 + 1} \,dx
$$
を計算することを考える（図）。以下の問いに答えよ。

<!-- FIGURE problem: 複素平面上の積分経路。実軸上の線分 [-R, R] と，上半平面の半径 R の大きな半円弧 C_R からなる反時計回りの閉経路。上半平面にある2つの極 z_0, z_1 の位置を明記する。 -->

(1) 複素関数 $f(z) = \frac{1}{z^4 + 1}$ の上半平面（$\operatorname{Im} z > 0$）にあるすべての極とその位置における留数を求めよ。

(2) 半径 $R > 1$ の上半平面の半円弧 $C_R: z = R e^{i\theta}$（$0 \le \theta \le \pi$）に沿う積分について，$\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0$ となることを示せ。

(3) 留数定理を用いて，定積分 $I$ の値を求めよ。

---

## 解答・解説

### (1)
極は分母が $0$ となる点，すなわち $z^4 + 1 = 0$ の解です。

$$
z^4 = -1 = e^{i\pi}
$$

この方程式の解は，$k = 0, 1, 2, 3$ に対して，

$$
z_k = \exp\left(i\frac{\pi + 2k\pi}{4}\right)
$$

となります。このうち上半平面（$\operatorname{Im} z > 0$）に存在するのは，虚部が正となる $k = 0$ および $k = 1$ の2点です。

$$
\begin{aligned}
z_0 &= e^{i\pi/4} = \frac{1 + i}{\sqrt{2}} \\
z_1 &= e^{i3\pi/4} = \frac{-1 + i}{\sqrt{2}}
\end{aligned}
$$

いずれも1位の極です。$f(z) = P(z)/Q(z)$ において $Q'(z_k) \neq 0$ のときの留数公式 $\operatorname{Res}(f, z_k) = P(z_k)/Q'(z_k)$ を用いると，

$$
\operatorname{Res}(f, z_k) = \frac{1}{4z_k^3} = \frac{z_k}{4z_k^4} = -\frac{z_k}{4}
$$

となります（$z_k^4 = -1$ を利用）。したがって，各極での留数は，

$$
\begin{aligned}
\operatorname{Res}(f, z_0) &= -\frac{1}{4} e^{i\pi/4} = \finalanswer{-\frac{1 + i}{4\sqrt{2}}} \\
\operatorname{Res}(f, z_1) &= -\frac{1}{4} e^{i3\pi/4} = \finalanswer{-\frac{-1 + i}{4\sqrt{2}}}
\end{aligned}
$$

となります。

### (2)
半円弧 $C_R$ 上では $|z| = R$ です。三角不等式より，

$$
|z^4 + 1| \ge |z|^4 - 1 = R^4 - 1
$$

が成り立ちます。したがって，被積分関数の絶対値の上界は，

$$
|f(z)| \le \frac{1}{R^4 - 1}
$$

となります。半円弧 $C_R$ の弧長は $\pi R$ であるため，積分の絶対値の評価を行うと，

$$
\begin{aligned}
\left| \int_{C_R} f(z) \,dz \right| &\le \int_{C_R} |f(z)| \,|dz| \\
&\le \frac{\pi R}{R^4 - 1}
\end{aligned}
$$

となります。$R \to \infty$ の極限をとると，

$$
\lim_{R \to \infty} \frac{\pi R}{R^4 - 1} = 0
$$

となるため，はさみうちの原理より，

$$
\finalanswer{\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0}
$$

が示されます。

### (3)
実軸上の区間 $[-R, R]$ と半円弧 $C_R$ を合わせた反時計回りの閉経路を $C$ とします。$R > 1$ のとき，上半平面の2つの極 $z_0, z_1$ は $C$ の内部に含まれます。

留数定理より，周回積分は内部の留数の和の $2\pi i$ 倍となります。

$$
\int_{-R}^R \frac{1}{x^4 + 1} \,dx + \int_{C_R} f(z) \,dz = 2\pi i \left[\operatorname{Res}(f, z_0) + \operatorname{Res}(f, z_1)\right]
$$

留数の和を計算すると，

$$
\begin{aligned}
\operatorname{Res}(f, z_0) + \operatorname{Res}(f, z_1) &= -\frac{1 + i}{4\sqrt{2}} - \frac{-1 + i}{4\sqrt{2}} \\
&= -\frac{2i}{4\sqrt{2}} \\
&= -\frac{i}{2\sqrt{2}}
\end{aligned}
$$

となります。$R \to \infty$ の極限をとると，(2)の結果より半円弧からの寄与は $0$ となるため，

$$
\begin{aligned}
I &= 2\pi i \left(-\frac{i}{2\sqrt{2}}\right) \\
&= \frac{2\pi}{2\sqrt{2}} \\
&= \finalanswer{\frac{\pi}{\sqrt{2}}}
\end{aligned}
$$

となります。

===== FILE: 11complex_analysis/04/04_030.md =====
---
tags:
  - 標準
---

# 三角関数の積分

## 問題
単位円周上の複素線積分を利用して，三角関数の定積分
$$
I = \int_0^{2\pi} \frac{d\theta}{a + \cos\theta} \quad (a > 1)
$$
を計算することを考える。以下の問いに答えよ。

(1) $z = e^{i\theta}$ と置換するとき，$\cos\theta$ および微小量 $d\theta$ を $z$ と $dz$ を用いて表せ。

(2) 積分 $I$ を，反時計回りの単位円周 $C: |z| = 1$ に沿う複素線積分の形に書き直せ。

(3) 留数定理を用いて，積分 $I$ の値を求めよ。

---

## 解答・解説

### (1)
オイラーの公式より $e^{i\theta} = \cos\theta + i\sin\theta$ および $e^{-i\theta} = \cos\theta - i\sin\theta$ です。これらを加えることで，

$$
\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}
$$

が得られます。$z = e^{i\theta}$ を代入すると，

$$
\finalanswer{\cos\theta = \frac{z + z^{-1}}{2} = \frac{z^2 + 1}{2z}}
$$

となります。

また，$z = e^{i\theta}$ の両辺を $\theta$ で微分すると，

$$
dz = i e^{i\theta} d\theta = i z d\theta
$$

となります。したがって，$d\theta$ について解くと，

$$
\finalanswer{d\theta = \frac{dz}{iz}}
$$

となります。

### (2)
(1)の結果を与えられた定積分 $I$ に代入します。$\theta$ が $0$ から $2\pi$ まで変化するとき，$z$ は単位円周 $C: |z| = 1$ を反時計回りに1周します。分母を整理すると，

$$
\begin{aligned}
a + \cos\theta &= a + \frac{z^2 + 1}{2z} \\
&= \frac{z^2 + 2az + 1}{2z}
\end{aligned}
$$

となります。被積分関数全体を $z$ で表すと，

$$
\begin{aligned}
\frac{d\theta}{a + \cos\theta} &= \frac{1}{\frac{z^2 + 2az + 1}{2z}} \cdot \frac{dz}{iz} \\
&= \frac{2}{i} \frac{dz}{z^2 + 2az + 1}
\end{aligned}
$$

となります。したがって，複素線積分の表現は，

$$
\finalanswer{I = \oint_C \frac{2}{i(z^2 + 2az + 1)} \,dz}
$$

となります。

### (3)
分母の多項式 $z^2 + 2az + 1 = 0$ の解を求めます。解の公式より，

$$
\begin{aligned}
z_1 &= -a + \sqrt{a^2 - 1} \\
z_2 &= -a - \sqrt{a^2 - 1}
\end{aligned}
$$

となります。$a > 1$ より $z_1, z_2$ はともに負の実数です。解と係数の関係から $z_1 z_2 = 1$ であり，$|z_2| = a + \sqrt{a^2 - 1} > 1$ であるため，もう一方の解の絶対値は，

$$
|z_1| = \frac{1}{|z_2|} < 1
$$

となります。したがって，単位円 $C$ の内部にある極は $z_1$ のみ（1位の極）です。

被積分関数 $f(z) = \frac{2}{i(z - z_1)(z - z_2)}$ の $z = z_1$ における留数を計算します。

$$
\begin{aligned}
\operatorname{Res}(f, z_1) &= \lim_{z \to z_1} (z - z_1) f(z) \\
&= \frac{2}{i(z_1 - z_2)}
\end{aligned}
$$

ここで $z_1 - z_2 = 2\sqrt{a^2 - 1}$ を代入すると，

$$
\operatorname{Res}(f, z_1) = \frac{2}{i \cdot 2\sqrt{a^2 - 1}} = \frac{1}{i\sqrt{a^2 - 1}}
$$

となります。留数定理を適用すると，

$$
\begin{aligned}
I &= 2\pi i \operatorname{Res}(f, z_1) \\
&= 2\pi i \cdot \frac{1}{i\sqrt{a^2 - 1}} \\
&= \finalanswer{\frac{2\pi}{\sqrt{a^2 - 1}}}
\end{aligned}
$$

となります。

===== FILE: 11complex_analysis/04/04_040.md =====
---
tags:
  - 標準
---

# ジョルダンの補題

## 問題
ディリクレ積分
$$
I = \int_0^\infty \frac{\sin x}{x} \,dx
$$
を複素積分を用いて求めることを考える。複素関数 $f(z) = \frac{e^{iz}}{z}$ および，実軸上の区間 $[-R, -\epsilon]$，原点を中心とする時計回りの小半円弧 $C_\epsilon: z = \epsilon e^{i(\pi - \theta)}$（$0 \le \theta \le \pi$），区間 $[\epsilon, R]$，反時計回りの大半円弧 $C_R: z = R e^{i\theta}$（$0 \le \theta \le \pi$）からなる閉経路を考える（図）。以下の問いに答えよ。

<!-- FIGURE problem: 複素平面上の積分経路。実軸上の [-R, -\epsilon] と [\epsilon, R]，原点を避ける上半平面の半径 \epsilon の小さな時計回り半円弧 C_\epsilon，および上半平面を閉じる半径 R の反時計回り大半円弧 C_R からなる閉経路。 -->

(1) 区間 $0 \le \theta \le \pi/2$ における不等式 $\sin\theta \ge \frac{2}{\pi}\theta$（ジョルダンの不等式）を用いて，大半円弧に沿う積分について $\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0$ となることを示せ。

(2) 小半円弧に沿う積分について，極限 $\lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz$ の値を求めよ。

(3) 閉経路全体にコーシーの積分定理を適用し，ディリクレ積分 $I$ の値を求めよ。

---

## 解答・解説

### (1)
大半円弧 $C_R$ 上では $z = R e^{i\theta} = R(\cos\theta + i\sin\theta)$（$0 \le \theta \le \pi$）であり，$dz = i R e^{i\theta} d\theta$ です。被積分関数の絶対値を評価すると，

$$
|e^{iz}| = |e^{iR\cos\theta - R\sin\theta}| = e^{-R\sin\theta}
$$

となります。積分を評価すると，

$$
\begin{aligned}
\left| \int_{C_R} \frac{e^{iz}}{z} \,dz \right| &\le \int_0^\pi \frac{e^{-R\sin\theta}}{R} \cdot R \,d\theta \\
&= \int_0^\pi e^{-R\sin\theta} \,d\theta \\
&= 2 \int_0^{\pi/2} e^{-R\sin\theta} \,d\theta
\end{aligned}
$$

となります。ここで $0 \le \theta \le \pi/2$ において $\sin\theta \ge \frac{2}{\pi}\theta$ を用いると，

$$
\begin{aligned}
\left| \int_{C_R} \frac{e^{iz}}{z} \,dz \right| &\le 2 \int_0^{\pi/2} e^{-R \frac{2}{\pi}\theta} \,d\theta \\
&= 2 \left[ -\frac{\pi}{2R} e^{-\frac{2R}{\pi}\theta} \right]_0^{\pi/2} \\
&= \frac{\pi}{R} \left(1 - e^{-R}\right)
\end{aligned}
$$

が得られます。$R \to \infty$ の極限をとると最右辺は $0$ に収束するため，

$$
\finalanswer{\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0}
$$

が示されます。

### (2)
$z = 0$ の近傍において指数関数をマクローリン展開すると，

$$
f(z) = \frac{e^{iz}}{z} = \frac{1}{z} + i - \frac{z}{2} + \cdots
$$

となります。小半円弧 $C_\epsilon$ は偏角が $\pi$ から $0$ へ向かう時計回りの向きを持ちます。主要部 $1/z$ の積分を計算すると，

$$
\int_{C_\epsilon} \frac{1}{z} \,dz = \int_\pi^0 \frac{1}{\epsilon e^{i\phi}} \cdot i\epsilon e^{i\phi} \,d\phi = i \int_\pi^0 d\phi = -\pi i
$$

となります。展開の残りの正則な項については，ある定数 $M > 0$ が存在して $|f(z) - 1/z| \le M$ と抑えられるため，

$$
\left| \int_{C_\epsilon} \left(f(z) - \frac{1}{z}\right) dz \right| \le M \cdot \pi\epsilon \to 0 \quad (\epsilon \to +0)
$$

となります。したがって，極限値は，

$$
\lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz = \finalanswer{-\pi i}
$$

となります。

### (3)
閉経路の内部には被積分関数 $f(z)$ の特異点は存在しません。コーシーの積分定理より，閉経路全体の積分は $0$ となります。

$$
\int_{-R}^{-\epsilon} \frac{e^{ix}}{x} \,dx + \int_{C_\epsilon} f(z) \,dz + \int_\epsilon^R \frac{e^{ix}}{x} \,dx + \int_{C_R} f(z) \,dz = 0
$$

第1項において変数変換 $x = -t$ を行うと，

$$
\int_{-R}^{-\epsilon} \frac{e^{ix}}{x} \,dx = \int_R^\epsilon \frac{e^{-it}}{-t} (-dt) = -\int_\epsilon^R \frac{e^{-ix}}{x} \,dx
$$

となります。これと第3項を合わせると，

$$
\int_\epsilon^R \frac{e^{ix} - e^{-ix}}{x} \,dx = 2i \int_\epsilon^R \frac{\sin x}{x} \,dx
$$

が得られます。全体の式において $R \to \infty$ および $\epsilon \to +0$ の極限をとり，(1)と(2)の結果を代入すると，

$$
2i \int_0^\infty \frac{\sin x}{x} \,dx - \pi i + 0 = 0
$$

となります。両辺を $2i$ で割ると，

$$
\finalanswer{\int_0^\infty \frac{\sin x}{x} \,dx = \frac{\pi}{2}}
$$

となります。

===== FILE: 11complex_analysis/04/04_050.md =====
---
tags:
  - 発展
---

# 主値積分

## 問題
実軸上に特異点を持つ関数のコーシーの主値積分について考える。実数直線上の積分
$$
I = \mathcal{P}\int_{-\infty}^\infty \frac{1}{(x - 1)(x^2 + 1)} \,dx
$$
について，以下の問いに答えよ。

(1) コーシーの主値積分 $I$ の定義式を書け。

(2) 複素関数 $f(z) = \frac{1}{(z - 1)(z^2 + 1)}$ について，実軸上の特異点 $z = 1$ を避ける半径 $\epsilon$ の時計回りの小半円弧 $C_\epsilon: z = 1 + \epsilon e^{i(\pi - \theta)}$（$0 \le \theta \le \pi$）に沿う積分の極限 $\lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz$ を求めよ。

(3) 上半平面にある極 $z = i$ における留数を求め，これを用いて主値積分 $I$ の値を求めよ。

---

## 解答・解説

### (1)
被積分関数は $x = 1$ において分母が $0$ となる特異点（1位の極）を持ちます。特異点の両側から等しい幅 $\epsilon$ で特異点を除外して極限をとるものがコーシーの主値積分です。したがって，定義式は，

$$
\finalanswer{\mathcal{P}\int_{-\infty}^\infty \frac{1}{(x - 1)(x^2 + 1)} \,dx = \lim_{\substack{R \to \infty \\ \epsilon \to +0}} \left( \int_{-R}^{1 - \epsilon} \frac{1}{(x - 1)(x^2 + 1)} \,dx + \int_{1 + \epsilon}^R \frac{1}{(x - 1)(x^2 + 1)} \,dx \right)}
$$

となります。

### (2)
$z = 1$ は $f(z)$ の1位の極です。$z = 1$ における留数を計算すると，

$$
\begin{aligned}
\operatorname{Res}(f, 1) &= \lim_{z \to 1} (z - 1) f(z) \\
&= \lim_{z \to 1} \frac{1}{z^2 + 1} \\
&= \frac{1}{1^2 + 1} \\
&= \frac{1}{2}
\end{aligned}
$$

となります。1位の極を通過する開き角 $\pi$ の時計回りの円弧に沿う積分の極限公式，

$$
\lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz = -\pi i \operatorname{Res}(f, 1)
$$

を適用すると，

$$
\begin{aligned}
\lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz &= -\pi i \left(\frac{1}{2}\right) \\
&= \finalanswer{-\frac{\pi i}{2}}
\end{aligned}
$$

となります。

### (3)
上半平面（$\operatorname{Im} z > 0$）にある特異点は $z^2 + 1 = 0$ の解である $z = i$ のみです。この点における留数を計算すると，

$$
\begin{aligned}
\operatorname{Res}(f, i) &= \lim_{z \to i} (z - i) f(z) \\
&= \lim_{z \to i} \frac{1}{(z - 1)(z + i)} \\
&= \frac{1}{(i - 1)(2i)} \\
&= \frac{1}{-2 - 2i} \\
&= \frac{-1 + i}{4}
\end{aligned}
$$

となります。したがって，上半平面の留数は，

$$
\finalanswer{\operatorname{Res}(f, i) = \frac{-1 + i}{4}}
$$

となります。

区間 $[-R, 1-\epsilon]$，$C_\epsilon$，$[1+\epsilon, R]$，および上半平面の大半円弧 $C_R$（$|z| = R$）からなる反時計回りの閉経路に留数定理を適用します。大半円弧上では被積分関数が $1/R^3$ のオーダーで減衰するため，$\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0$ です。したがって，

$$
\mathcal{P}\int_{-\infty}^\infty f(x) \,dx + \lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz = 2\pi i \operatorname{Res}(f, i)
$$

が成り立ちます。(2)の結果と留数の値を代入すると，

$$
\begin{aligned}
I - \frac{\pi i}{2} &= 2\pi i \left(\frac{-1 + i}{4}\right) \\
&= \frac{-\pi i - \pi}{2} \\
&= -\frac{\pi}{2} - \frac{\pi i}{2}
\end{aligned}
$$

となります。両辺の虚数部 $-\frac{\pi i}{2}$ が相殺され，

$$
\finalanswer{I = -\frac{\pi}{2}}
$$

となります。

===== FILE: 11complex_analysis/04/04_060.md =====
---
tags:
  - 発展
---

# 分岐切断のある積分

## 問題
多価関数であることを利用した鍵穴型（キーホール）経路の複素積分について考える。パラメータ $a$ は $0 < a < 1$ を満たす実定数とする。定積分
$$
I = \int_0^\infty \frac{x^{a-1}}{1 + x} \,dx
$$
について，以下の問いに答えよ。

<!-- FIGURE problem: 複素平面上の鍵穴型閉経路。正の実軸に沿った分岐切断（赤の実線），切断の直上を原点側から正の実軸正方向へ進む直線経路，半径 R の反時計回り大円 C_R，切断の直下を戻る直線経路，原点を囲む半径 \epsilon の時計回り小円 C_\epsilon。内部にある極 z = -1 の位置。 -->

(1) 複素関数 $f(z) = \frac{z^{a-1}}{1 + z}$ に対し，正の実軸（$[0, \infty)$）に分岐切断を入れ，偏角の範囲を $0 \le \arg z < 2\pi$ と定める。切断のすぐ上の経路 $z = x + i0$（$x: 0 \to \infty$）およびすぐ下の経路 $z = x - i0$（$x: \infty \to 0$）における $f(z)$ の値をそれぞれ $x$ を用いて表せ。

(2) 鍵穴型閉経路の大円 $C_R: z = R e^{i\theta}$ および小円 $C_\epsilon: z = \epsilon e^{i\theta}$（ともに偏角は $0 \to 2\pi$）に沿う積分について，$0 < a < 1$ のとき $\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0$ および $\lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz = 0$ となることを示せ。

(3) 留数定理を用いて，積分 $I$ の値を求めよ。

---

## 解答・解説

### (1)
多価関数 $z^{a-1}$ は $z = r e^{i\theta}$ に対し，

$$
z^{a-1} = \exp\left((a - 1)(\ln r + i\theta)\right) = r^{a-1} e^{i(a-1)\theta}
$$

と定義されます。

分岐切断のすぐ上の経路では，偏角は $\theta = 0$ です。したがって，$z = x$ となり，

$$
z^{a-1} = x^{a-1} e^{i(a-1)\cdot 0} = x^{a-1}
$$

となります。よって，切断のすぐ上での関数値は，

$$
\finalanswer{f(x + i0) = \frac{x^{a-1}}{1 + x}}
$$

となります。

一方，分岐切断のすぐ下の経路では，偏角は反時計回りに1周して $\theta = 2\pi$ となります。したがって，

$$
\begin{aligned}
z^{a-1} &= x^{a-1} e^{i(a-1)2\pi} \\
&= x^{a-1} e^{i2\pi a} e^{-i2\pi} \\
&= x^{a-1} e^{i2\pi a}
\end{aligned}
$$

となります。よって，切断のすぐ下での関数値は，

$$
\finalanswer{f(x - i0) = \frac{x^{a-1} e^{i2\pi a}}{1 + x}}
$$

となります。

### (2)
大円 $C_R$ 上では $|z| = R$ です。分母は $|1 + z| \ge R - 1$ と評価でき，分子は $|z^{a-1}| = R^{a-1}$ です。弧長は $2\pi R$ であるため，

$$
\begin{aligned}
\left| \int_{C_R} f(z) \,dz \right| &\le \frac{R^{a-1}}{R - 1} \cdot 2\pi R \\
&= 2\pi \frac{R^a}{R - 1}
\end{aligned}
$$

となります。ここで $a < 1$ であるため，$R \to \infty$ の極限をとると $R^a / (R - 1) \to 0$ となります。したがって，

$$
\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0
$$

が成り立ちます。

小円 $C_\epsilon$ 上では $|z| = \epsilon$ です。分母は $|1 + z| \ge 1 - \epsilon$ と評価でき，分子は $|z^{a-1}| = \epsilon^{a-1}$ です。弧長は $2\pi \epsilon$ であるため，

$$
\begin{aligned}
\left| \int_{C_\epsilon} f(z) \,dz \right| &\le \frac{\epsilon^{a-1}}{1 - \epsilon} \cdot 2\pi \epsilon \\
&= 2\pi \frac{\epsilon^a}{1 - \epsilon}
\end{aligned}
$$

となります。ここで $a > 0$ であるため，$\epsilon \to +0$ の極限をとると $\epsilon^a \to 0$ となります。したがって，

$$
\lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz = 0
$$

が成り立ちます。以上より，大円および小円に沿う積分の極限は，

$$
\finalanswer{\lim_{R \to \infty} \int_{C_R} f(z) \,dz = 0, \quad \lim_{\epsilon \to +0} \int_{C_\epsilon} f(z) \,dz = 0}
$$

となることが示されます。

### (3)
鍵穴型閉経路の内部にある特異点は，分母が $0$ となる $z = -1$ のみです。この点での偏角は $\arg(-1) = \pi$ であるため，

$$
(-1)^{a-1} = e^{i(a-1)\pi} = e^{i\pi a} e^{-i\pi} = -e^{i\pi a}
$$

となります。したがって，$z = -1$ における留数は，

$$
\operatorname{Res}(f, -1) = \lim_{z \to -1} (z + 1) f(z) = (-1)^{a-1} = -e^{i\pi a}
$$

となります。

閉経路全体の積分は，切断の上側（$\epsilon \to R$），大円 $C_R$，切断の下側（$R \to \epsilon$），小円 $C_\epsilon$ の4つの和です。留数定理より，

$$
\int_\epsilon^R f(x + i0) \,dx + \int_{C_R} f(z) \,dz + \int_R^\epsilon f(x - i0) \,dx + \int_{C_\epsilon} f(z) \,dz = 2\pi i \operatorname{Res}(f, -1)
$$

が成り立ちます。(1)と(2)の結果を用い，$R \to \infty$ および $\epsilon \to +0$ の極限をとると，

$$
\int_0^\infty \frac{x^{a-1}}{1 + x} \,dx - e^{i2\pi a} \int_0^\infty \frac{x^{a-1}}{1 + x} \,dx = 2\pi i \left(-e^{i\pi a}\right)
$$

となります。共通因数でまとめると，

$$
\left(1 - e^{i2\pi a}\right) I = -2\pi i e^{i\pi a}
$$

となります。両辺を $1 - e^{i2\pi a}$ で割って整理すると，

$$
\begin{aligned}
I &= \frac{-2\pi i e^{i\pi a}}{1 - e^{i2\pi a}} \\
&= \frac{2\pi i}{e^{i\pi a} - e^{-i\pi a}} \\
&= \frac{\pi}{\frac{e^{i\pi a} - e^{-i\pi a}}{2i}} \\
&= \finalanswer{\frac{\pi}{\sin(\pi a)}}
\end{aligned}
$$

となります。

===== END =====