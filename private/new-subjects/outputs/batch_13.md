===== FILE: 11complex_analysis/05/05_010.md =====
---
tags:
  - 発展
---

# 等角写像と2次元静電場

## 問題
開き角 $\alpha$（$0 < \alpha \le 2\pi$）をもつ2次元の導体境界で囲まれた領域 $0 \le \theta \le \alpha$ を考える（図）。境界上の電位は $0$ に保たれている。複素座標 $z = x + iy = r e^{i\theta}$ に対し，複素ポテンシャルを実定数 $A > 0$ を用いて
$$
W(z) = A z^{\pi/\alpha}
$$
と定義する。電位 $\phi(x, y)$ は $W(z)$ の虚部 $\phi = \mathrm{Im}\, W(z)$ で与えられ，電場ベクトル $\boldsymbol{E} = (E_x, E_y)$ は $\boldsymbol{E} = -\nabla \phi$ で定まる。以下の問いに答えよ。

<!-- FIGURE problem: くさび形の導体領域。原点 O から角度 0 の半直線（x 軸正の向き）と角度 alpha の半直線が伸びており，その2本の半直線が導体壁となっている。内部領域 0 <= theta <= alpha が示されている。 -->

(1) 極座標 $(r, \theta)$ を用いて電位 $\phi(r, \theta)$ を表せ。また，導体表面 $\theta = 0$ および $\theta = \alpha$ で電位の境界条件が満たされていることを確かめよ。

(2) 電場の大きさ $|\boldsymbol{E}|$ を $A, \alpha, r$ を用いて表せ。

(3) 直角の角の外側（$\alpha = 3\pi/2$）および内側（$\alpha = \pi/2$）のそれぞれについて，導体の角の先端（$r \to 0$）における電場の大きさの極限を求めよ。

---

## 解答・解説

### (1)
複素数 $z$ を極形式 $z = r e^{i\theta}$ で表して複素ポテンシャルに代入します。

$$
\begin{aligned}
W(z) &= A (r e^{i\theta})^{\pi/\alpha} \\
&= A r^{\pi/\alpha} e^{i \pi \theta/\alpha}
\end{aligned}
$$

オイラーの公式を適用すると，

$$
W(z) = A r^{\pi/\alpha} \left( \cos\frac{\pi\theta}{\alpha} + i \sin\frac{\pi\theta}{\alpha} \right)
$$

となります。虚部をとると，電位は

$$
\finalanswer{\phi(r, \theta) = A r^{\pi/\alpha} \sin\frac{\pi\theta}{\alpha}}
$$

となります。境界条件を確認します。$\theta = 0$ のとき $\sin 0 = 0$ より $\phi(r, 0) = 0$ となります。$\theta = \alpha$ のとき $\sin \pi = 0$ より $\phi(r, \alpha) = 0$ となります。したがって，両方の導体表面で電位が $0$ となる境界条件が満たされています。

### (2)
複素ポテンシャルの複素微分と電場の関係を導きます。
$W(z) = \psi(x, y) + i \phi(x, y)$ とおくと，コーシー・リーマンの関係式 $\partial \psi/\partial x = \partial \phi/\partial y$ が成り立ちます。これにより，

$$
\begin{aligned}
\frac{dW}{dz} &= \frac{\partial \psi}{\partial x} + i \frac{\partial \phi}{\partial x} \\
&= \frac{\partial \phi}{\partial y} + i \frac{\partial \phi}{\partial x}
\end{aligned}
$$

となります。電場成分 $E_x = -\partial \phi/\partial x$，$E_y = -\partial \phi/\partial y$ を用いて絶対値をとると，

$$
\begin{aligned}
\left| \frac{dW}{dz} \right| &= \sqrt{\left(\frac{\partial \phi}{\partial y}\right)^2 + \left(\frac{\partial \phi}{\partial x}\right)^2} \\
&= \sqrt{E_y^2 + E_x^2} \\
&= |\boldsymbol{E}|
\end{aligned}
$$

が得られます。$W(z) = A z^{\pi/\alpha}$ を微分すると，

$$
\frac{dW}{dz} = \frac{A \pi}{\alpha} z^{\pi/\alpha - 1}
$$

となります。$|z| = r$ であるため，絶対値をとると，

$$
\finalanswer{|\boldsymbol{E}| = \frac{A \pi}{\alpha} r^{\pi/\alpha - 1}}
$$

となります。

### (3)
(2) で得られた電場の式に各開き角を代入して $r \to 0$ の極限を調べます。
$\alpha = 3\pi/2$ のとき，指数の値は $\pi/\alpha - 1 = 2/3 - 1 = -1/3$ となります。電場の大きさは

$$
|\boldsymbol{E}| = \frac{2A}{3} r^{-1/3}
$$

となります。$r \to 0$ の極限をとると，

$$
\finalanswer{\lim_{r \to 0} |\boldsymbol{E}| = \infty}
$$

となります。
一方，$\alpha = \pi/2$ のとき，指数の値は $\pi/\alpha - 1 = 2 - 1 = 1$ となります。電場の大きさは

$$
|\boldsymbol{E}| = 2A r
$$

となります。$r \to 0$ の極限をとると，

$$
\finalanswer{\lim_{r \to 0} |\boldsymbol{E}| = 0}
$$

となります。
尖った角の外側では電場が無限大に発散し，角の内側の隅では電場が $0$ に収束することが分かります。避雷針の先端で電場が集中する現象に対応しています。

===== FILE: 11complex_analysis/05/05_020.md =====
---
tags:
  - 発展
---

# 偏角の原理

## 問題
複素平面上の単純閉曲線 $C$ およびその内部で有理型な関数 $f(z)$ を考える。$C$ 上に $f(z)$ の零点および極は存在しないとする。以下の問いに答えよ。

(1) $f(z)$ が $C$ の内部に零点（重複度込みで計 $N$ 個）および極（重複度込みで計 $P$ 個）をもつとき，複素積分
$$
I = \frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)} dz
$$
が $N - P$ に等しくなることを示せ。

(2) 多項式 $P(z) = z^4 - 3z + 1$ について，円盤 $|z| < 1$ の内部に含まれる零点の個数を求めよ。

(3) 同じ多項式 $P(z)$ について，円環領域 $1 < |z| < 2$ に含まれる零点の個数を求めよ。

---

## 解答・解説

### (1)
被積分関数 $f'(z)/f(z)$ の特異点における留数を求めます。
$f(z)$ の $m$ 位の零点 $z = a$ の近傍では，正則で $g(a) \ne 0$ を満たす関数 $g(z)$ を用いて $f(z) = (z - a)^m g(z)$ と表されます。両辺の対数微分をとると，

$$
\begin{aligned}
\frac{f'(z)}{f(z)} &= \frac{m(z - a)^{m-1} g(z) + (z - a)^m g'(z)}{(z - a)^m g(z)} \\
&= \frac{m}{z - a} + \frac{g'(z)}{g(z)}
\end{aligned}
$$

となります。$g'(z)/g(z)$ は $z = a$ で正則であるため，$z = a$ における留数は $m$ となります。
同様に，$p$ 位の極 $z = b$ の近傍では $f(z) = (z - b)^{-p} h(z)$（$h(b) \ne 0$）と表され，対数微分は

$$
\frac{f'(z)}{f(z)} = -\frac{p}{z - b} + \frac{h'(z)}{h(z)}
$$

となり，留数は $-p$ となります。
留数定理を適用すると，積分の値は各零点と極における留数の総和に $2\pi i$ を掛けたものになります。

$$
\oint_C \frac{f'(z)}{f(z)} dz = 2\pi i \left( \sum m_j - \sum p_k \right) = 2\pi i (N - P)
$$

両辺を $2\pi i$ で割ると，

$$
\finalanswer{\frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)} dz = N - P}
$$

となります。

### (2)
ルーシェの定理を用いて零点の個数を決定します。
多項式を $f(z) = -3z$ と $g(z) = z^4 + 1$ の和 $P(z) = f(z) + g(z)$ とみなします。円周 $|z| = 1$ 上でそれぞれの絶対値を評価します。

$$
|f(z)| = 3|z| = 3
$$

三角不等式を用いると，

$$
|g(z)| \le |z|^4 + 1 = 2
$$

となります。円周 $|z| = 1$ 上のすべての点で $|g(z)| < |f(z)|$ が成り立ちます。
ルーシェの定理により，$P(z)$ と $f(z)$ は $|z| < 1$ の内部で同じ個数の零点をもちます。$f(z) = -3z$ は $|z| < 1$ 内に零点 $z = 0$ を1つだけもつため，求める零点の個数を $N_1$ とおくと，

$$
\finalanswer{N_1 = 1}
$$

となります。

### (3)
円周 $|z| = 2$ の内部に含まれる零点の個数を評価します。
多項式を $F(z) = z^4$ と $G(z) = -3z + 1$ の和 $P(z) = F(z) + G(z)$ とみなします。円周 $|z| = 2$ 上でそれぞれの絶対値を評価します。

$$
|F(z)| = |z|^4 = 16
$$

三角不等式を用いると，

$$
|G(z)| \le 3|z| + 1 = 7
$$

となります。円周 $|z| = 2$ 上で $|G(z)| < |F(z)|$ が成り立ちます。
ルーシェの定理により，$P(z)$ と $F(z) = z^4$ は $|z| < 2$ の内部で同じ個数の零点をもちます。$z^4$ は原点に重複度4の零点をもつため，零点は全部で4個です。
円周 $|z| = 1$ 上では $|P(z)| \ge |f(z)| - |g(z)| \ge 3 - 2 = 1 > 0$ であるため零点は存在しません。
円環領域 $1 < |z| < 2$ に含まれる零点の個数を $N_2$ とおくと，

$$
N_2 = 4 - N_1 = 4 - 1
$$

より，

$$
\finalanswer{N_2 = 3}
$$

となります。

===== FILE: 11complex_analysis/05/05_030.md =====
---
tags:
  - 発展
---

# 鞍点法の入口

## 問題
大きな自然数 $N \gg 1$ に対する階乗 $N! = \Gamma(N+1)$ の漸近挙動を考える。ガンマ関数の積分表示は
$$
N! = \int_0^\infty t^N e^{-t} dt
$$
で与えられる。以下の問いに答えよ。

(1) 積分変数を $t = N s$ と変換することにより，積分が
$$
N! = N^{N+1} \int_0^\infty e^{N f(s)} ds
$$
と表されることを示し，$f(s)$ を求めよ。

(2) 関数 $f(s)$ が最大値をとる点 $s_0$ を求め，その点でのテイラー展開を $(s - s_0)^2$ の項まで求めよ。

(3) $N \gg 1$ のとき被積分関数が $s_0$ の近傍に鋭く局在することを利用し，ガウス積分の公式
$$
\int_{-\infty}^\infty e^{-a x^2} dx = \sqrt{\frac{\pi}{a}} \quad (a > 0)
$$
を用いてスターリングの公式
$$
N! \approx \sqrt{2\pi N} \left(\frac{N}{e}\right)^N
$$
を導け。

---

## 解答・解説

### (1)
変数変換 $t = N s$ を行います。微分は $dt = N ds$ であり，積分範囲は $s: 0 \to \infty$ となります。積分に代入すると，

$$
\begin{aligned}
N! &= \int_0^\infty (N s)^N e^{-N s} N ds \\
&= N^{N+1} \int_0^\infty s^N e^{-N s} ds
\end{aligned}
$$

となります。被積分関数の因子 $s^N$ を指数表示 $s^N = e^{N \ln s}$ に書き直して整理します。

$$
\begin{aligned}
N! &= N^{N+1} \int_0^\infty e^{N \ln s} e^{-N s} ds \\
&= N^{N+1} \int_0^\infty e^{N(\ln s - s)} ds
\end{aligned}
$$

したがって，指数の肩の関数は

$$
\finalanswer{f(s) = \ln s - s}
$$

となります。

### (2)
$f(s)$ の1階導関数および2階導関数を計算します。

$$
f'(s) = \frac{1}{s} - 1, \quad f''(s) = -\frac{1}{s^2}
$$

極値を与える条件 $f'(s) = 0$ を解くと，$s > 0$ における最大値の点は

$$
s_0 = 1
$$

となります。この点における関数の値と導関数の値は

$$
f(1) = -1, \quad f'(1) = 0, \quad f''(1) = -1
$$

となります。点 $s_0 = 1$ のまわりでテイラー展開を行うと，

$$
\begin{aligned}
f(s) &\approx f(1) + f'(1)(s - 1) + \frac{1}{2} f''(1)(s - 1)^2 \\
&= \finalanswer{f(s) \approx -1 - \frac{1}{2}(s - 1)^2}
\end{aligned}
$$

となります。

### (3)
$N$ が非常に大きいとき，指数関数 $e^{N f(s)}$ は最大値の点 $s = 1$ の極めて狭い近傍でのみ大きな値をもちます。展開式を代入し，局在性の高さから積分範囲を $(-\infty, \infty)$ に拡張して近似します。

$$
\begin{aligned}
N! &\approx N^{N+1} \int_{-\infty}^\infty e^{N \left( -1 - \frac{1}{2}(s - 1)^2 \right)} ds \\
&= N^{N+1} e^{-N} \int_{-\infty}^\infty e^{-\frac{N}{2}(s - 1)^2} ds
\end{aligned}
$$

ここで $x = s - 1$ とおくと，ガウス積分の公式（$a = N/2$）を適用できます。

$$
\int_{-\infty}^\infty e^{-\frac{N}{2}x^2} dx = \sqrt{\frac{\pi}{N/2}} = \sqrt{\frac{2\pi}{N}}
$$

代入して整理すると，

$$
\begin{aligned}
N! &\approx N^{N+1} e^{-N} \sqrt{\frac{2\pi}{N}} \\
&= \finalanswer{N! \approx \sqrt{2\pi N} \left(\frac{N}{e}\right)^N}
\end{aligned}
$$

となります。最急降下法（鞍点法）の基本原理により，階乗の漸近挙動を与える公式が導かれます。

===== FILE: 11complex_analysis/05/05_040.md =====
---
tags:
  - 発展
---

# クラマース・クローニッヒの関係

## 問題
複素周波数 $z$ の関数として複素感受率 $\chi(z)$ を考える。因果律により，$\chi(z)$ は上半平面 $\mathrm{Im}\, z > 0$ で正則であり，十分遠方で $\lim_{|z| \to \infty} |\chi(z)| = 0$ を満たすとする。実軸上の実周波数を $\omega$，固定された実周波数を $\omega_0$ とする（図）。以下の問いに答えよ。

<!-- FIGURE problem: 上半平面における積分経路。実軸上の点 omega_0 を中心とする半径 epsilon の上側小半円 C_epsilon と，区間 [-R, omega_0 - epsilon]，[omega_0 + epsilon, R]，および半径 R の大半円 C_R からなる反時計回りの閉経路。 -->

(1) 点 $\omega_0$ を中心とする半径 $\epsilon > 0$ の上側半円経路 $C_\epsilon: z = \omega_0 + \epsilon e^{i\theta}$（$\theta$ は $\pi$ から $0$ まで変化）に沿う積分について，極限
$$
\lim_{\epsilon \to 0} \int_{C_\epsilon} \frac{\chi(z)}{z - \omega_0} dz
$$
を求めよ。

(2) コーシーの積分定理を用いて，コーシーの主値積分
$$
\mathcal{P} \int_{-\infty}^\infty \frac{\chi(\omega)}{\omega - \omega_0} d\omega
$$
を $\chi(\omega_0)$ を用いて表せ。

(3) $\chi(\omega) = \chi_1(\omega) + i \chi_2(\omega)$（$\chi_1, \chi_2$ は実数値関数）と分解したとき，実部 $\chi_1(\omega_0)$ を $\chi_2(\omega)$ の主値積分で表す関係式を導け。

---

## 解答・解説

### (1)
経路 $C_\epsilon$ 上の点を $z = \omega_0 + \epsilon e^{i\theta}$ とパラメータ表示します。微分は $dz = i\epsilon e^{i\theta} d\theta$ であり，積分範囲は $\theta: \pi \to 0$ となります。積分に代入すると，

$$
\begin{aligned}
\int_{C_\epsilon} \frac{\chi(z)}{z - \omega_0} dz &= \int_\pi^0 \frac{\chi(\omega_0 + \epsilon e^{i\theta})}{\epsilon e^{i\theta}} i\epsilon e^{i\theta} d\theta \\
&= i \int_\pi^0 \chi(\omega_0 + \epsilon e^{i\theta}) d\theta
\end{aligned}
$$

となります。$\epsilon \to 0$ の極限をとると，被積分関数は定数 $\chi(\omega_0)$ に収束するため，

$$
\begin{aligned}
\lim_{\epsilon \to 0} \int_{C_\epsilon} \frac{\chi(z)}{z - \omega_0} dz &= i \chi(\omega_0) \int_\pi^0 d\theta \\
&= \finalanswer{-i\pi \chi(\omega_0)}
\end{aligned}
$$

となります。

### (2)
実軸上の2つの線分 $[-R, \omega_0 - \epsilon]$，$[\omega_0 + \epsilon, R]$ と，小半円 $C_\epsilon$，および上半平面の半径 $R$ の大半円 $C_R$ からなる閉経路 $C$ をとります。被積分関数 $\chi(z)/(z - \omega_0)$ は閉経路の内部で正則であるため，コーシーの積分定理より

$$
\oint_C \frac{\chi(z)}{z - \omega_0} dz = 0
$$

となります。$R \to \infty$ のとき，$|\chi(z)| \to 0$ の条件により大半円 $C_R$ 上の積分は $0$ に収束します。各経路の寄与をまとめると，

$$
\lim_{R \to \infty, \epsilon \to 0} \left( \int_{-R}^{\omega_0 - \epsilon} \frac{\chi(\omega)}{\omega - \omega_0} d\omega + \int_{\omega_0 + \epsilon}^R \frac{\chi(\omega)}{\omega - \omega_0} d\omega \right) + \lim_{\epsilon \to 0} \int_{C_\epsilon} \frac{\chi(z)}{z - \omega_0} dz = 0
$$

となります。主値積分の定義および (1) の結果を代入すると，

$$
\mathcal{P} \int_{-\infty}^\infty \frac{\chi(\omega)}{\omega - \omega_0} d\omega - i\pi \chi(\omega_0) = 0
$$

となります。移項すると，

$$
\finalanswer{\mathcal{P} \int_{-\infty}^\infty \frac{\chi(\omega)}{\omega - \omega_0} d\omega = i\pi \chi(\omega_0)}
$$

となります。

### (3)
(2) で得られた等式を $\chi(\omega_0)$ について解きます。

$$
\begin{aligned}
\chi(\omega_0) &= \frac{1}{i\pi} \mathcal{P} \int_{-\infty}^\infty \frac{\chi(\omega)}{\omega - \omega_0} d\omega \\
&= -\frac{i}{\pi} \mathcal{P} \int_{-\infty}^\infty \frac{\chi_1(\omega) + i \chi_2(\omega)}{\omega - \omega_0} d\omega
\end{aligned}
$$

右辺の被積分関数を展開すると，$-i(\chi_1 + i\chi_2) = \chi_2 - i\chi_1$ となります。両辺の実部をとると，

$$
\finalanswer{\chi_1(\omega_0) = \frac{1}{\pi} \mathcal{P} \int_{-\infty}^\infty \frac{\chi_2(\omega)}{\omega - \omega_0} d\omega}
$$

となります。因果律の要請により，応答の実部（分散）と虚部（吸収）が互いに結びついていることが示されます。

===== FILE: 11complex_analysis/05/05_050.md =====
---
tags:
  - 発展
---

# 留数による級数の和

## 問題
実定数 $a > 0$ に対し，無限級数の和 $\sum_{n=-\infty}^\infty \frac{1}{n^2 + a^2}$ を留数定理を用いて求める。複素関数
$$
g(z) = \frac{\pi \cot(\pi z)}{z^2 + a^2}
$$
を考える。以下の問いに答えよ。

(1) 整数点 $z = n$（$n = 0, \pm 1, \pm 2, \dots$）における $g(z)$ の留数 $\mathrm{Res}(g, n)$ を求めよ。

(2) $z = \pm ia$ における留数の和 $\mathrm{Res}(g, ia) + \mathrm{Res}(g, -ia)$ を $a$ を用いて表せ。

(3) 適切な閉曲線上の積分を考えることにより，無限級数の和
$$
S = \sum_{n=-\infty}^\infty \frac{1}{n^2 + a^2}
$$
を求めよ。

---

## 解答・解説

### (1)
$\cot(\pi z) = \frac{\cos(\pi z)}{\sin(\pi z)}$ より，$z = n$ は $\sin(\pi z)$ の1位の零点です。
$g(z)$ の留数は，微分の公式を用いて計算できます。

$$
\begin{aligned}
\mathrm{Res}(g, n) &= \lim_{z \to n} (z - n) \frac{\pi \cos(\pi z)}{\sin(\pi z)(z^2 + a^2)} \\
&= \frac{\pi \cos(\pi n)}{\pi \cos(\pi n)(n^2 + a^2)} \\
&= \finalanswer{\frac{1}{n^2 + a^2}}
\end{aligned}
$$

となります。

### (2)
$z = ia$ における留数を求めます。分母を因数分解すると $z^2 + a^2 = (z - ia)(z + ia)$ であるため，

$$
\begin{aligned}
\mathrm{Res}(g, ia) &= \lim_{z \to ia} (z - ia) \frac{\pi \cot(\pi z)}{(z - ia)(z + ia)} \\
&= \frac{\pi \cot(i\pi a)}{2ia}
\end{aligned}
$$

となります。三角関数と双曲線関数の関係式 $\cos(ix) = \cosh x$ および $\sin(ix) = i \sinh x$ を用いると，

$$
\cot(i\pi a) = \frac{\cos(i\pi a)}{\sin(i\pi a)} = \frac{\cosh(\pi a)}{i \sinh(\pi a)} = -i \coth(\pi a)
$$

となります。代入すると，

$$
\mathrm{Res}(g, ia) = \frac{\pi (-i\coth(\pi a))}{2ia} = -\frac{\pi}{2a} \coth(\pi a)
$$

となります。同様に $z = -ia$ における留数を計算すると，

$$
\begin{aligned}
\mathrm{Res}(g, -ia) &= \frac{\pi \cot(-i\pi a)}{-2ia} \\
&= \frac{-\pi \cot(i\pi a)}{-2ia} \\
&= -\frac{\pi}{2a} \coth(\pi a)
\end{aligned}
$$

となります。2つの留数の和をとると，

$$
\finalanswer{\mathrm{Res}(g, ia) + \mathrm{Res}(g, -ia) = -\frac{\pi}{a} \coth(\pi a)}
$$

となります。

### (3)
頂点が $(N + 1/2)(\pm 1 \pm i)$（$N$ は自然数）である正方形経路 $C_N$ をとります。$C_N$ 上で $\cot(\pi z)$ は有界であり，分母の大きさは $|z^2 + a^2| \ge C N^2$（$C$ は定数）を満たします。経路の長さは $8(N + 1/2)$ であるため，積分の絶対値は $N \to \infty$ のとき $0$ に収束します。

$$
\lim_{N \to \infty} \oint_{C_N} g(z) dz = 0
$$

留数定理により，全平面における留数の総和は $0$ になります。

$$
\sum_{n=-\infty}^\infty \mathrm{Res}(g, n) + \mathrm{Res}(g, ia) + \mathrm{Res}(g, -ia) = 0
$$

(1) と (2) の結果を代入すると，

$$
\sum_{n=-\infty}^\infty \frac{1}{n^2 + a^2} - \frac{\pi}{a} \coth(\pi a) = 0
$$

となります。移項すると，

$$
\finalanswer{\sum_{n=-\infty}^\infty \frac{1}{n^2 + a^2} = \frac{\pi}{a} \coth(\pi a)}
$$

となります。

===== FILE: 11complex_analysis/06/06_010.md =====
---
tags:
  - 基本
---

# 複素数の幾何学的な意味

## 問題
複素数平面における回転と拡大を考える。虚数単位を $i$ とする。以下の問いに答えよ。

(1) 複素数 $\alpha = \sqrt{3} + i$ の絶対値 $|\alpha|$ および偏角 $\arg \alpha$（$0 \le \arg \alpha < 2\pi$）を求めよ。

(2) 点 $z = 1 - i$ を，原点を中心として反時計回りに $\pi/3$ だけ回転し，さらに原点からの距離を $2$ 倍に拡大した点を表す複素数 $w$ を求めよ。

(3) 点 $z_1 = 2 + i$ を点 $z_0 = 1 + 2i$ のまわりに反時計回りに $\pi/2$ だけ回転させた点を表す複素数 $z_2$ を求めよ。

---

## 解答・解説

### (1)
複素数 $\alpha = a + ib$ の絶対値の定義式を適用します。

$$
\begin{aligned}
|\alpha| &= \sqrt{(\sqrt{3})^2 + 1^2} \\
&= \sqrt{3 + 1} \\
&= \finalanswer{2}
\end{aligned}
$$

極形式 $\alpha = |\alpha|(\cos\theta + i\sin\theta)$ と比較すると，

$$
\cos\theta = \frac{\sqrt{3}}{2}, \quad \sin\theta = \frac{1}{2}
$$

となります。条件 $0 \le \theta < 2\pi$ を満たす偏角は，

$$
\finalanswer{\arg \alpha = \frac{\pi}{6}}
$$

となります。

### (2)
原点中心の反時計回りの角 $\phi$ の回転と $k$ 倍の拡大は，複素数 $k e^{i\phi}$ を掛ける操作に対応します。
$k = 2$ および $\phi = \pi/3$ を代入して展開します。

$$
\begin{aligned}
2 e^{i\pi/3} &= 2 \left( \cos\frac{\pi}{3} + i \sin\frac{\pi}{3} \right) \\
&= 2 \left( \frac{1}{2} + i \frac{\sqrt{3}}{2} \right) \\
&= 1 + i\sqrt{3}
\end{aligned}
$$

これを $z = 1 - i$ に掛けます。

$$
\begin{aligned}
w &= (1 + i\sqrt{3})(1 - i) \\
&= 1 - i + i\sqrt{3} - i^2\sqrt{3} \\
&= 1 - i + i\sqrt{3} + \sqrt{3}
\end{aligned}
$$

実部と虚部に整理すると，

$$
\finalanswer{w = (1 + \sqrt{3}) + i(\sqrt{3} - 1)}
$$

となります。

### (3)
点 $z_0$ を中心とする回転を考えるため，点 $z_0$ を原点に移す平行移動を行います。
点 $z_1$ の相対位置は $z_1 - z_0$ と表されます。このベクトルを反時計回りに $\pi/2$ 回転させるには $e^{i\pi/2} = i$ を掛けます。回転後の点 $z_2$ は次の方程式を満たします。

$$
z_2 - z_0 = i(z_1 - z_0)
$$

$z_1 - z_0$ を計算すると，

$$
\begin{aligned}
z_1 - z_0 &= (2 + i) - (1 + 2i) \\
&= 1 - i
\end{aligned}
$$

となります。これに $i$ を掛けると，

$$
\begin{aligned}
i(z_1 - z_0) &= i(1 - i) \\
&= i - i^2 \\
&= 1 + i
\end{aligned}
$$

となります。両辺に $z_0$ を加えると，

$$
\begin{aligned}
z_2 &= (1 + 2i) + (1 + i) \\
&= \finalanswer{2 + 3i}
\end{aligned}
$$

となります。

===== FILE: 11complex_analysis/06/06_020.md =====
---
tags:
  - 基本
---

# 正則でない関数の例

## 問題
複素数 $z = x + iy$（$x, y$ は実数）の複素共役を $\bar{z} = x - iy$ とする。複素関数 $f(z) = u(x, y) + i v(x, y)$ が複素微分可能であるための必要条件として，コーシー・リーマンの関係式
$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$
が知られている。以下の問いに答えよ。

(1) 関数 $f(z) = \bar{z}$ について，実部 $u(x, y)$ と虚部 $v(x, y)$ がコーシー・リーマンの関係式を満たす点 $(x, y)$ は存在しないことを示せ。

(2) 関数 $g(z) = |z|^2$ について，実部 $u(x, y)$ と虚部 $v(x, y)$ を求め，コーシー・リーマンの関係式を満たす点 $(x, y)$ を求めよ。

(3) 微分係数の定義式を用いて，関数 $g(z) = |z|^2$ の $z = 0$ における微分係数 $g'(0)$ を求めよ。

---

## 解答・解説

### (1)
$f(z) = \bar{z} = x - iy$ より，実部と虚部は

$$
u(x, y) = x, \quad v(x, y) = -y
$$

となります。各変数について偏導関数を計算すると，

$$
\frac{\partial u}{\partial x} = 1, \quad \frac{\partial v}{\partial y} = -1
$$

$$
\frac{\partial u}{\partial y} = 0, \quad \frac{\partial v}{\partial x} = 0
$$

となります。コーシー・リーマンの関係式の第1式を調べると，

$$
\finalanswer{\frac{\partial u}{\partial x} \ne \frac{\partial v}{\partial y}}
$$

となり，恒等的に $1 = -1$ となるため満たされる点 $(x, y)$ は存在しません。したがって，関数 $\bar{z}$ は複素平面上のいかなる点でもコーシー・リーマンの関係式を満たさず，複素微分可能ではありません。

### (2)
$|z|^2 = x^2 + y^2$ であるため，実部と虚部は

$$
\finalanswer{u(x, y) = x^2 + y^2, \quad v(x, y) = 0}
$$

となります。それぞれの偏導関数を計算すると，

$$
\frac{\partial u}{\partial x} = 2x, \quad \frac{\partial v}{\partial y} = 0
$$

$$
\frac{\partial u}{\partial y} = 2y, \quad \frac{\partial v}{\partial x} = 0
$$

となります。コーシー・リーマンの関係式を満たす条件は，

$$
2x = 0, \quad 2y = 0
$$

となります。したがって，満たす点は原点のみであり，

$$
\finalanswer{(x, y) = (0, 0)}
$$

となります。

### (3)
複素微分係数の定義式に従って極限を計算します。

$$
g'(0) = \lim_{\Delta z \to 0} \frac{g(0 + \Delta z) - g(0)}{\Delta z}
$$

$g(0) = 0$ および $g(\Delta z) = |\Delta z|^2 = \Delta z \, \overline{\Delta z}$ を代入すると，

$$
\begin{aligned}
g'(0) &= \lim_{\Delta z \to 0} \frac{\Delta z \, \overline{\Delta z}}{\Delta z} \\
&= \lim_{\Delta z \to 0} \overline{\Delta z}
\end{aligned}
$$

となります。$\Delta z \to 0$ のとき複素共役も $\overline{\Delta z} \to 0$ に収束するため，極限値は接近の方向に依存せず一意に定まります。

$$
\finalanswer{g'(0) = 0}
$$

となります。関数 $|z|^2$ は原点でのみ複素微分可能であり，その近傍を含む領域では微分可能でないため，どの領域でも正則にはなりません。

===== FILE: 11complex_analysis/06/06_030.md =====
---
tags:
  - 標準
---

# 零点と極の位数

## 問題
複素平面上の関数における零点と極の性質を調べる。以下の問いに答えよ。

(1) 有理関数
$$
f(z) = \frac{(z - 2)^3}{(z^2 - 1)^2}
$$
のすべての零点とその位数 $m$，およびすべての極とその位数 $p$ を求めよ。

(2) 関数
$$
g(z) = \frac{1 - \cos z}{z^3}
$$
の $z = 0$ における極の位数 $p$ および留数 $\mathrm{Res}(g, 0)$ を求めよ。

(3) 関数
$$
h(z) = \frac{1}{\sin z - z}
$$
の $z = 0$ における極の位数 $p$ を求めよ。

---

## 解答・解説

### (1)
分子と分母を因数分解して零点を調べます。
分子は $(z - 2)^3$ であるため，分子の零点は $z = 2$（位数3）です。
分母は

$$
(z^2 - 1)^2 = (z - 1)^2 (z + 1)^2
$$

と因数分解されるため，分母の零点は $z = 1$（位数2）および $z = -1$（位数2）です。
分子と分母に共通の零点は存在しないため，零点とその位数は

$$
\finalanswer{z = 2 \quad (m = 3)}
$$

となります。極とその位数は

$$
\finalanswer{z = 1 \quad (p = 2), \quad z = -1 \quad (p = 2)}
$$

となります。

### (2)
分子の余弦関数のマクローリン展開を用います。

$$
\cos z = 1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \dots
$$

分子に代入すると，

$$
1 - \cos z = \frac{z^2}{2} - \frac{z^4}{24} + \dots
$$

となります。これを $z^3$ で割ってローラン展開を求めます。

$$
\begin{aligned}
g(z) &= \frac{1}{z^3} \left( \frac{z^2}{2} - \frac{z^4}{24} + \dots \right) \\
&= \frac{1}{2z} - \frac{z}{24} + \dots
\end{aligned}
$$

主部の負べきの項は $z^{-1}$ のみであるため，極の位数は

$$
\finalanswer{p = 1}
$$

となります。留数は $z^{-1}$ の係数であるため，

$$
\finalanswer{\mathrm{Res}(g, 0) = \frac{1}{2}}
$$

となります。

### (3)
分母の関数のテイラー展開を求めます。
正弦関数のマクローリン展開は

$$
\sin z = z - \frac{z^3}{3!} + \frac{z^5}{5!} - \dots
$$

です。分母を計算すると，

$$
\begin{aligned}
\sin z - z &= -\frac{z^3}{6} + \frac{z^5}{120} - \dots \\
&= -\frac{z^3}{6} \left( 1 - \frac{z^2}{20} + \dots \right)
\end{aligned}
$$

となります。したがって，$z = 0$ は分母の3位の零点です。
逆数をとると，

$$
h(z) = -\frac{6}{z^3} \left( 1 - \frac{z^2}{20} + \dots \right)^{-1} = -\frac{6}{z^3} - \frac{3}{10z} + \dots
$$

となり，主部の最高次は $z^{-3}$ となります。したがって，極の位数は

$$
\finalanswer{p = 3}
$$

となります。

===== FILE: 11complex_analysis/06/06_040.md =====
---
tags:
  - 標準
---

# フーリエ型の実積分

## 問題
実定数 $a > 0$ および $k > 0$ に対し，実積分
$$
I = \int_{-\infty}^\infty \frac{\cos(kx)}{x^2 + a^2} dx
$$
を考える。複素関数 $f(z) = \frac{e^{ikz}}{z^2 + a^2}$ を上半平面の閉経路で積分する。以下の問いに答えよ。

(1) 上半平面 $\mathrm{Im}\, z > 0$ にある $f(z)$ の極を求め，その極における留数を求めよ。

(2) 半径 $R$（$R > a$）の上半円弧 $C_R: z = R e^{i\theta}$（$0 \le \theta \le \pi$）に沿う積分について，極限
$$
\lim_{R \to \infty} \int_{C_R} f(z) dz = 0
$$
が成り立つことを示せ。

(3) 留数定理を用いて実積分 $I$ を求めよ。

---

## 解答・解説

### (1)
分母の零点は $z^2 + a^2 = 0$ より $z = \pm ia$ です。上半平面 $\mathrm{Im}\, z > 0$ にある極は

$$
\finalanswer{z = ia}
$$

となります。この点における留数を計算すると，

$$
\begin{aligned}
\mathrm{Res}(f, ia) &= \lim_{z \to ia} (z - ia) \frac{e^{ikz}}{(z - ia)(z + ia)} \\
&= \frac{e^{ik(ia)}}{2ia} \\
&= \finalanswer{\frac{e^{-ka}}{2ia}}
\end{aligned}
$$

となります。

### (2)
上半円弧 $C_R$ 上の点 $z = R(\cos\theta + i\sin\theta)$ において分子の絶対値を評価します。

$$
|e^{ikz}| = |e^{ikR\cos\theta - kR\sin\theta}| = e^{-kR\sin\theta}
$$

$0 \le \theta \le \pi$ において $\sin\theta \ge 0$ かつ $k > 0$ であるため，$e^{-kR\sin\theta} \le 1$ が成り立ちます。
分母の絶対値は，三角不等式より

$$
|z^2 + a^2| \ge |z|^2 - a^2 = R^2 - a^2
$$

となります。線素は $|dz| = R d\theta$ であるため，積分の絶対値を上から評価すると，

$$
\begin{aligned}
\left| \int_{C_R} f(z) dz \right| &\le \int_0^\pi \frac{1}{R^2 - a^2} R d\theta \\
&= \frac{\pi R}{R^2 - a^2}
\end{aligned}
$$

となります。$R \to \infty$ の極限をとると，分母が $R^2$ のオーダーで分子が $R$ のオーダーであるため，

$$
\finalanswer{\lim_{R \to \infty} \left| \int_{C_R} f(z) dz \right| = 0}
$$

となり，積分は $0$ に収束します。

### (3)
実軸上の区間 $[-R, R]$ と半円弧 $C_R$ からなる閉経路に留数定理を適用します。

$$
\int_{-R}^R \frac{e^{ikx}}{x^2 + a^2} dx + \int_{C_R} f(z) dz = 2\pi i \, \mathrm{Res}(f, ia)
$$

$R \to \infty$ の極限をとり，(2) の結果を適用すると，

$$
\begin{aligned}
\int_{-\infty}^\infty \frac{e^{ikx}}{x^2 + a^2} dx &= 2\pi i \left( \frac{e^{-ka}}{2ia} \right) \\
&= \frac{\pi}{a} e^{-ka}
\end{aligned}
$$

となります。オイラーの公式 $e^{ikx} = \cos(kx) + i\sin(kx)$ を用いて両辺の実部をとると，

$$
\finalanswer{I = \frac{\pi}{a} e^{-ka}}
$$

となります。なお，虚部の被積分関数は奇関数であるため積分値は $0$ となります。

===== FILE: 11complex_analysis/06/06_050.md =====
---
tags:
  - 標準
---

# ガウス積分の複素数への拡張

## 問題
ガウス積分 $\int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}$ を利用して，パラメータ $k > 0$ を含む実積分
$$
J = \int_{-\infty}^\infty e^{-x^2} \cos(kx) dx
$$
を求める。複素関数 $f(z) = e^{-z^2}$ と，実軸上の線分 $[-R, R]$，垂直線分 $[R, R + i b]$，水平線分 $[R + i b, -R + i b]$，垂直線分 $[-R + i b, -R]$ からなる長方形経路 $C$ を考える（$b > 0, R > 0$）。以下の問いに答えよ。

<!-- FIGURE problem: 複素平面上の長方形経路。頂点は -R, R, R + ib, -R + ib であり，反時計回りの矢印がつけられている。実軸上の線分，右側の垂直線分，上側の水平線分，左側の垂直線分からなる。 -->

(1) $R \to \infty$ のとき，2つの垂直線分に沿う $f(z)$ の積分の絶対値が $0$ に収束することを示せ。

(2) コーシーの積分定理を用いて，水平線分に沿う実積分
$$
\int_{-\infty}^\infty e^{-(x + i b)^2} dx
$$
の値を求めよ。

(3) $b = k/2$ とおくことにより，実積分 $J$ を求めよ。

---

## 解答・解説

### (1)
右側の垂直線分 $C_1$ 上の点を $z = R + iy$（$0 \le y \le b$）と表します。微分は $dz = i dy$ です。被積分関数の絶対値を計算すると，

$$
\begin{aligned}
|e^{-z^2}| &= |e^{-(R + iy)^2}| \\
&= |e^{-R^2 + y^2 - 2iRy}| \\
&= e^{-R^2 + y^2} \\
&\le e^{-R^2 + b^2}
\end{aligned}
$$

となります。積分の絶対値を上から評価すると，

$$
\left| \int_{C_1} f(z) dz \right| \le \int_0^b e^{-R^2 + b^2} dy = b e^{-R^2 + b^2}
$$

となります。$R \to \infty$ の極限をとると，

$$
\finalanswer{\lim_{R \to \infty} \left| \int_{C_1} f(z) dz \right| = 0}
$$

となります。左側の垂直線分上でも同様に $z = -R + iy$ となり，絶対値の評価は同一であるため $0$ に収束します。

### (2)
関数 $f(z) = e^{-z^2}$ は全平面で正則であるため，コーシーの積分定理より閉経路に沿う積分は $0$ になります。

$$
\oint_C f(z) dz = 0
$$

4本の線分に沿う積分に分解すると，

$$
\int_{-R}^R e^{-x^2} dx + \int_{C_1} f(z) dz + \int_R^{-R} e^{-(x + ib)^2} dx + \int_{C_2} f(z) dz = 0
$$

となります。$R \to \infty$ の極限をとり，(1) の結果を代入すると垂直線分の寄与は消滅します。

$$
\int_{-\infty}^\infty e^{-x^2} dx - \int_{-\infty}^\infty e^{-(x + ib)^2} dx = 0
$$

ガウス積分の値 $\sqrt{\pi}$ を代入すると，

$$
\finalanswer{\int_{-\infty}^\infty e^{-(x + i b)^2} dx = \sqrt{\pi}}
$$

となります。

### (3)
(2) で求めた被積分関数を展開します。

$$
\begin{aligned}
e^{-(x + ib)^2} &= e^{-x^2 + b^2 - 2ibx} \\
&= e^{b^2} e^{-x^2} (\cos(2bx) - i\sin(2bx))
\end{aligned}
$$

これを (2) の等式に代入します。

$$
e^{b^2} \int_{-\infty}^\infty e^{-x^2} (\cos(2bx) - i\sin(2bx)) dx = \sqrt{\pi}
$$

被積分関数のうち $e^{-x^2}\sin(2bx)$ は奇関数であるため，対称区間の積分は $0$ になります。両辺の実部をとると，

$$
e^{b^2} \int_{-\infty}^\infty e^{-x^2} \cos(2bx) dx = \sqrt{\pi}
$$

となります。ここで $b = k/2$ を代入すると，

$$
e^{k^2/4} \int_{-\infty}^\infty e^{-x^2} \cos(kx) dx = \sqrt{\pi}
$$

となります。両辺を $e^{k^2/4}$ で割ると，

$$
\finalanswer{J = \sqrt{\pi} e^{-k^2/4}}
$$

となります。

===== FILE: 11complex_analysis/06/06_060.md =====
---
tags:
  - 発展
---

# 対数を含む実積分

## 問題
対数関数を含む実積分
$$
I_1 = \int_0^\infty \frac{\ln x}{x^2 + 1} dx, \quad I_2 = \int_0^\infty \frac{1}{x^2 + 1} dx
$$
を考える。複素関数 $f(z) = \frac{\mathrm{Log}\, z}{z^2 + 1}$ を上半平面で積分する。対数の主値の偏角を $-\pi/2 < \arg z < 3\pi/2$ と定め，$\mathrm{Log}\, z = \ln |z| + i \arg z$ とする。以下の問いに答えよ。

(1) 上半平面にある $f(z)$ の極 $z = i$ における留数 $\mathrm{Res}(f, i)$ を求めよ。

(2) 実軸の負の部分 $z = -t$（$t > 0$）における $f(z)$ を $t$ を用いて表し，積分 $\int_{-\infty}^0 f(x) dx$ を $t$ に関する2つの実積分で表せ。

(3) 上半平面の半円経路を用いた複素積分を考えることにより，$I_1$ および $I_2$ の値を求めよ。

---

## 解答・解説

### (1)
極 $z = i$ における対数関数の値を計算します。$|i| = 1$ かつ $\arg i = \pi/2$ であるため，

$$
\mathrm{Log}(i) = \ln 1 + i\frac{\pi}{2} = i\frac{\pi}{2}
$$

となります。留数の計算式に代入すると，

$$
\begin{aligned}
\mathrm{Res}(f, i) &= \lim_{z \to i} (z - i) \frac{\mathrm{Log}\, z}{(z - i)(z + i)} \\
&= \frac{\mathrm{Log}(i)}{2i} \\
&= \frac{i\pi/2}{2i} \\
&= \finalanswer{\frac{\pi}{4}}
\end{aligned}
$$

となります。

### (2)
実軸の負の部分では $z = -t = t e^{i\pi}$（$t > 0$）であるため，対数関数は

$$
\mathrm{Log}\, z = \ln t + i\pi
$$

となります。分母は $z^2 + 1 = (-t)^2 + 1 = t^2 + 1$ となります。
$x = -t$ と置換すると $dx = -dt$ であり，積分範囲は $t: \infty \to 0$ となります。

$$
\begin{aligned}
\int_{-\infty}^0 f(x) dx &= \int_\infty^0 \frac{\ln t + i\pi}{t^2 + 1} (-dt) \\
&= \int_0^\infty \frac{\ln t + i\pi}{t^2 + 1} dt \\
&= \finalanswer{\int_0^\infty \frac{\ln t}{t^2 + 1} dt + i\pi \int_0^\infty \frac{1}{t^2 + 1} dt}
\end{aligned}
$$

となります。

### (3)
原点を中心とする小半円 $C_\epsilon$（半径 $\epsilon$）と大半円 $C_R$（半径 $R$），および実軸上の区間 $[-R, -\epsilon]$，$[\epsilon, R]$ からなる閉経路に留数定理を適用します。
$\epsilon \to 0$ のとき $C_\epsilon$ 上の積分は $\epsilon \ln \epsilon \to 0$ より消滅し，$R \to \infty$ のとき $C_R$ 上の積分も $\frac{\ln R}{R} \to 0$ より消滅します。
したがって，実軸全体の積分が留数定理に結びつきます。

$$
\int_0^\infty \frac{\ln x}{x^2 + 1} dx + \left( \int_0^\infty \frac{\ln t}{t^2 + 1} dt + i\pi \int_0^\infty \frac{1}{t^2 + 1} dt \right) = 2\pi i \, \mathrm{Res}(f, i)
$$

(1) の結果を代入して整理すると，

$$
2 I_1 + i\pi I_2 = 2\pi i \left( \frac{\pi}{4} \right) = \frac{i\pi^2}{2}
$$

となります。実部と虚部をそれぞれ比較すると，

$$
2 I_1 = 0 \implies \finalanswer{I_1 = 0}
$$

$$
\pi I_2 = \frac{\pi^2}{2} \implies \finalanswer{I_2 = \frac{\pi}{2}}
$$

となります。1つの複素積分から2つの実積分の値が同時に導かれます。

===== FILE: 11complex_analysis/06/06_070.md =====
---
tags:
  - 標準
---

# 経路の変形と多価関数の積分

## 問題
実パラメータ $p$（$0 < p < 1$）を含む実積分
$$
K = \int_0^\infty \frac{x^{p-1}}{x + 1} dx
$$
を考える。複素関数 $f(z) = \frac{z^{p-1}}{z + 1}$ を用い，分枝切断を正の実軸 $[0, \infty)$ に設定して偏角を $0 \le \arg z < 2\pi$ と定める。以下の問いに答えよ。

<!-- FIGURE problem: 複素平面上の鍵穴経路（キーホール経路）。正の実軸を挟む上下の往復線分と，原点まわりの半径 epsilon の小円，無限遠の半径 R の大円からなる反時計回りの閉経路。 -->

(1) 孤立特異点 $z = -1$ における $f(z)$ の留数 $\mathrm{Res}(f, -1)$ を $p$ を用いて表せ。

(2) 正の実軸の上側（$z = x + i0$）および下側（$z = x - i0$）における $f(z)$ の値について，比 $f(x - i0) / f(x + i0)$ を求めよ。

(3) 鍵穴経路（キーホール経路）に沿う積分に留数定理を適用することにより，実積分 $K$ を求めよ。

---

## 解答・解説

### (1)
偏角の範囲 $0 \le \arg z < 2\pi$ において，負の実軸上の点 $z = -1$ は $z = e^{i\pi}$ と表されます。
分子の多価関数に代入すると，

$$
z^{p-1} = (e^{i\pi})^{p-1} = e^{i\pi(p-1)} = -e^{i\pi p}
$$

となります。留数の公式を適用すると，

$$
\begin{aligned}
\mathrm{Res}(f, -1) &= \lim_{z \to -1} (z + 1) \frac{z^{p-1}}{z + 1} \\
&= \finalanswer{-e^{i\pi p}}
\end{aligned}
$$

となります。

### (2)
正の実軸の上側では偏角は $\arg z = 0$ であるため，

$$
f(x + i0) = \frac{x^{p-1}}{x + 1}
$$

となります。一方，正の実軸の下側では偏角が1周して $\arg z = 2\pi$ となるため，

$$
\begin{aligned}
f(x - i0) &= \frac{(x e^{i2\pi})^{p-1}}{x + 1} \\
&= \frac{x^{p-1} e^{i2\pi(p-1)}}{x + 1} \\
&= e^{i2\pi p} \frac{x^{p-1}}{x + 1}
\end{aligned}
$$

となります。両者の比をとると，

$$
\finalanswer{\frac{f(x - i0)}{f(x + i0)} = e^{i2\pi p}}
$$

となります。

### (3)
原点をまわる半径 $\epsilon$ の小円 $C_\epsilon$，半径 $R$ の大円 $C_R$，および切断の上下の線分からなる鍵穴経路をとります。
$0 < p < 1$ の条件により，$\epsilon \to 0$ のとき $C_\epsilon$ 上の積分は $\epsilon^p \to 0$ より消滅し，$R \to \infty$ のとき $C_R$ 上の積分も $R^{p-1} \to 0$ より消滅します。
留数定理より，上下の線分に沿う積分の和が留数に結びつきます。

$$
\int_0^\infty f(x + i0) dx + \int_\infty^0 f(x - i0) dx = 2\pi i \, \mathrm{Res}(f, -1)
$$

(2) の関係式 $f(x - i0) = e^{i2\pi p} f(x + i0)$ を代入すると，

$$
(1 - e^{i2\pi p}) \int_0^\infty \frac{x^{p-1}}{x + 1} dx = 2\pi i (-e^{i\pi p})
$$

となります。両辺を整理して $K$ について解きます。

$$
\begin{aligned}
K &= \frac{-2\pi i e^{i\pi p}}{1 - e^{i2\pi p}} \\
&= \frac{2\pi i}{e^{i\pi p} - e^{-i\pi p}} \\
&= \frac{\pi}{\frac{e^{i\pi p} - e^{-i\pi p}}{2i}}
\end{aligned}
$$

分母にオイラーの公式から導かれる正弦関数を代入すると，

$$
\finalanswer{K = \frac{\pi}{\sin(\pi p)}}
$$

となります。

===== FILE: 11complex_analysis/06/06_080.md =====
---
tags:
  - 発展
---

# 複素ポテンシャルと2次元流れ

## 問題
2次元非圧縮・渦なしの流れを考える。速度場 $\boldsymbol{v} = (u, v)$ に対し，複素速度ポテンシャル $W(z) = \phi(x, y) + i \psi(x, y)$（$\phi$ は速度ポテンシャル，$\psi$ は流れの関数）を導入すると，複素速度は $\frac{dW}{dz} = u - iv$ で与えられる。半径 $a$ の円柱のまわりの，無限遠で流速 $U > 0$（$x$ 軸正の向き）となる一様流の複素ポテンシャルは
$$
W(z) = U \left( z + \frac{a^2}{z} \right)
$$
で与えられる（図）。以下の問いに答えよ。

<!-- FIGURE problem: 半径 a の円柱のまわりを一様流 U が左から右へ流れる様子。円柱の中心を原点とし，x 軸と y 軸が示されている。 -->

(1) 極座標 $z = r e^{i\theta}$（$r \ge a$）を用いて，流れの関数 $\psi(r, \theta)$ を求めよ。また，円柱表面 $r = a$ 上で $\psi$ が一定値をとることを示せ。

(2) 円柱表面（$r = a$）上の流速の大きさ $|\boldsymbol{v}|$ を $U$ と $\theta$ を用いて表せ。

(3) 流体の密度を $\rho$，無限遠での圧力を $p_\infty$ とする。ベルヌーイの定理
$$
p + \frac{1}{2} \rho |\boldsymbol{v}|^2 = p_\infty + \frac{1}{2} \rho U^2
$$
を用いて，円柱表面上の圧力分布 $p(\theta)$ を求めよ。

---

## 解答・解説

### (1)
$z = r e^{i\theta}$ を複素ポテンシャルに代入します。

$$
\begin{aligned}
W(z) &= U \left( r e^{i\theta} + \frac{a^2}{r} e^{-i\theta} \right) \\
&= U \left[ r (\cos\theta + i\sin\theta) + \frac{a^2}{r} (\cos\theta - i\sin\theta) \right] \\
&= U \left( r + \frac{a^2}{r} \right) \cos\theta + i U \left( r - \frac{a^2}{r} \right) \sin\theta
\end{aligned}
$$

虚部をとると，流れの関数は

$$
\finalanswer{\psi(r, \theta) = U \left( r - \frac{a^2}{r} \right) \sin\theta}
$$

となります。円柱表面 $r = a$ を代入すると，

$$
\finalanswer{\psi(a, \theta) = 0}
$$

となり，角度 $\theta$ によらず一定値をとります。流線 $\psi = \mathrm{const}$ が円柱境界と一致するため，表面を横切る流れが存在しない条件が満たされています。

### (2)
複素微分により複素速度を求めます。

$$
\frac{dW}{dz} = U \left( 1 - \frac{a^2}{z^2} \right)
$$

円柱表面 $r = a$ 上では $z = a e^{i\theta}$ であるため，代入すると，

$$
\begin{aligned}
\frac{dW}{dz} &= U (1 - e^{-2i\theta}) \\
&= U e^{-i\theta} (e^{i\theta} - e^{-i\theta}) \\
&= 2i U e^{-i\theta} \sin\theta
\end{aligned}
$$

となります。流速の大きさは複素速度の絶対値に等しいため，

$$
\begin{aligned}
|\boldsymbol{v}| &= \left| \frac{dW}{dz} \right| \\
&= |2i U e^{-i\theta} \sin\theta| \\
&= \finalanswer{2U |\sin\theta|}
\end{aligned}
$$

となります。

### (3)
ベルヌーイの定理を変形すると，表面上の圧力は

$$
p(\theta) = p_\infty + \frac{1}{2}\rho U^2 - \frac{1}{2}\rho |\boldsymbol{v}|^2
$$

となります。(2) の結果 $|\boldsymbol{v}|^2 = 4 U^2 \sin^2\theta$ を代入すると，

$$
\begin{aligned}
p(\theta) &= p_\infty + \frac{1}{2}\rho U^2 - \frac{1}{2}\rho (4 U^2 \sin^2\theta) \\
&= \finalanswer{p_\infty + \frac{1}{2}\rho U^2 (1 - 4\sin^2\theta)}
\end{aligned}
$$

となります。円柱の最前面および最後面（$\theta = 0, \pi$）では流速が $0$ となり圧力が最大値 $p_\infty + \frac{1}{2}\rho U^2$ をとります。円柱の上端および下端（$\theta = \pm \pi/2$）では流速が最大の $2U$ となり，圧力は最小値 $p_\infty - \frac{3}{2}\rho U^2$ をとります。

===== FILE: 11complex_analysis/06/06_090.md =====
---
tags:
  - 発展
---

# ガンマ関数の解析接続

## 問題
$\mathrm{Re}\, z > 0$ においてガンマ関数は積分
$$
\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} dt
$$
によって定義される。以下の問いに答えよ。

(1) 部分積分を用いて，$\mathrm{Re}\, z > 0$ において関係式 $\Gamma(z+1) = z \Gamma(z)$ が成り立つことを示せ。

(2) 関数関係式を用いて $\Gamma(z)$ を負の非整数へ解析接続する。$\Gamma(1/2) = \sqrt{\pi}$ を用いて，$\Gamma(-1/2)$ および $\Gamma(-3/2)$ の値を求めよ。

(3) 非正の整数 $z = -n$（$n = 0, 1, 2, \dots$）が $\Gamma(z)$ の1位の極であることを示し，その点における留数 $\mathrm{Res}(\Gamma, -n)$ を $n$ を用いて表せ。

---

## 解答・解説

### (1)
定義式において引数を $z+1$ とおきます。

$$
\Gamma(z+1) = \int_0^\infty t^z e^{-t} dt
$$

$u = t^z$，$v' = e^{-t}$ として部分積分を行います。

$$
\Gamma(z+1) = \left[ -t^z e^{-t} \right]_0^\infty + \int_0^\infty z t^{z-1} e^{-t} dt
$$

$\mathrm{Re}\, z > 0$ のとき，境界項は $t \to \infty$ において指数関数により $0$ に収束し，$t \to 0$ においても $t^z \to 0$ となるため消滅します。残った積分から定数 $z$ を外に出すと，

$$
\finalanswer{\Gamma(z+1) = z \Gamma(z)}
$$

が成り立ちます。

### (2)
関数関係式を変形すると，

$$
\Gamma(z) = \frac{\Gamma(z+1)}{z}
$$

となります。この式を用いることで，右辺が定義される領域を通じて左辺の定義域を負の方向へ広げることができます。
$z = -1/2$ を代入すると，

$$
\begin{aligned}
\Gamma(-1/2) &= \frac{\Gamma(1/2)}{-1/2} \\
&= -2 \sqrt{\pi}
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{\Gamma(-1/2) = -2\sqrt{\pi}}
$$

となります。次に $z = -3/2$ を代入すると，

$$
\begin{aligned}
\Gamma(-3/2) &= \frac{\Gamma(-1/2)}{-3/2} \\
&= \frac{-2\sqrt{\pi}}{-3/2} \\
&= \finalanswer{\frac{4}{3}\sqrt{\pi}}
\end{aligned}
$$

となります。

### (3)
関係式を $n+1$ 回繰り返し適用すると，

$$
\Gamma(z) = \frac{\Gamma(z + n + 1)}{z(z + 1)(z + 2)\cdots(z + n)}
$$

が得られます。$z \to -n$ の極限において，分子は $\Gamma(1) = 1$ となり有限確定値をもちます。分母は $z + n$ の因子のみが $0$ に収束し，他の因子は非零です。したがって，$z = -n$ は位数1の極となります。
この極における留数を計算すると，

$$
\begin{aligned}
\mathrm{Res}(\Gamma, -n) &= \lim_{z \to -n} (z + n)\Gamma(z) \\
&= \lim_{z \to -n} \frac{\Gamma(z + n + 1)}{z(z + 1)\cdots(z + n - 1)} \\
&= \frac{\Gamma(1)}{(-n)(-n + 1)\cdots(-1)}
\end{aligned}
$$

分母には負の符号が $n$ 個あり，絶対値の積は $n!$ に等しいため，

$$
\finalanswer{\mathrm{Res}(\Gamma, -n) = \frac{(-1)^n}{n!}}
$$

となります。

===== FILE: 11complex_analysis/06/06_100.md =====
---
tags:
  - 発展
---

# 等角写像による境界値問題

## 問題
帯状領域 $D = \{z = x+iy \mid -\infty < x < \infty, \, 0 < y < \pi\}$ における2次元静電ポテンシャル $\phi(x, y)$ の境界値問題を等角写像を用いて解く。写像 $w = e^z$（$w = u + iv$）を用いる。以下の問いに答えよ。

<!-- FIGURE problem: z 平面における帯状領域 0 < y < pi と，写像 w = e^z によって移される w 平面の上半平面 v > 0 の対応を示す見取り図。 -->

(1) 写像 $w = e^z$ によって，領域 $D$ が $w$ 平面の上半平面 $\mathrm{Im}\, w > 0$ に写されることを示せ。また，境界の直線 $y = 0$ および $y = \pi$ が $w$ 平面の実軸のどの部分に対応するか答えよ。

(2) $w$ 平面の上半平面において，実軸上の境界条件が $u > 0$ で $\phi = 0$，$u < 0$ で $\phi = V_0$（$V_0$ は正の定数）であるとする。ラプラス方程式を満たす電位 $\phi$ を極座標 $w = \rho e^{i\theta}$（$\rho > 0, 0 < \theta < \pi$）の偏角 $\theta = \arg w$ を用いて表せ。

(3) 等角写像 $w = e^z$ を用いて，元の帯状領域における電位分布 $\phi(x, y)$ を $x, y$ で表せ。

---

## 解答・解説

### (1)
$z = x + iy$ を代入して $w = e^z$ の実部と虚部を求めます。

$$
\begin{aligned}
w &= e^{x+iy} \\
&= e^x (\cos y + i \sin y)
\end{aligned}
$$

実部と虚部は

$$
u = e^x \cos y, \quad v = e^x \sin y
$$

となります。領域 $D$ では $0 < y < \pi$ であるため，常に $\sin y > 0$ です。また指数関数は $e^x > 0$ であるため，虚部は

$$
\finalanswer{v = \mathrm{Im}\, w > 0}
$$

を満たし，上半平面全体に1対1に写されます。
境界 $y = 0$ を代入すると $u = e^x > 0$ かつ $v = 0$ となるため，

$$
\finalanswer{u > 0 \quad (v = 0)}
$$

すなわち実軸の正の部分に対応します。
境界 $y = \pi$ を代入すると $u = -e^x < 0$ かつ $v = 0$ となるため，

$$
\finalanswer{u < 0 \quad (v = 0)}
$$

すなわち実軸の負の部分に対応します。

### (2)
複素対数関数 $\mathrm{Log}\, w = \ln \rho + i\theta$ の虚部 $\theta = \arg w$ は調和関数であり，2次元ラプラス方程式を満たします。
境界条件を満たす電位を定数 $A, B$ を用いて

$$
\phi = A\theta + B
$$

とおきます。実軸正の部分（$\theta = 0$）で $\phi = 0$ であるため，

$$
B = 0
$$

となります。実軸負の部分（$\theta = \pi$）で $\phi = V_0$ であるため，

$$
A\pi = V_0 \implies A = \frac{V_0}{\pi}
$$

となります。したがって，求める電位は

$$
\finalanswer{\phi = \frac{V_0}{\pi}\theta}
$$

となります。

### (3)
写像 $w = e^z$ と極形式 $w = \rho e^{i\theta}$ を比較します。

$$
w = e^x e^{iy} = \rho e^{i\theta}
$$

両辺の絶対値と偏角を比べると，

$$
\rho = e^x, \quad \theta = y
$$

が得られます。この $\theta = y$ を (2) で求めた電位の式に代入すると，

$$
\finalanswer{\phi(x, y) = \frac{V_0}{\pi} y}
$$

となります。電位が $x$ に依存せず $y$ について線形に変化し，平行平板電極間の電位分布と一致することが分かります。

===== END =====