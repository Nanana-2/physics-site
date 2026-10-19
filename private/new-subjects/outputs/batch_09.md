===== FILE: 09vector_analysis/05/05_010.md =====
---
tags:
  - 基本
---

# ガウスの発散定理

## 問題
3次元空間において，ベクトル場 $\boldsymbol{A}$ が
$$
\boldsymbol{A} = x \boldsymbol{e}_x + y \boldsymbol{e}_y + z^2 \boldsymbol{e}_z
$$
で与えられている。底面の半径が $R$，高さが $H$ の円柱領域
$$
V: x^2 + y^2 \le R^2, \quad 0 \le z \le H
$$
を考え，その境界面全体を $S$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 底面が xy 平面上にあり，中心軸が z 軸に一致する半径 R，高さ H の円柱領域 V を描く。底面 z=0，上面 z=H，側面 x^2+y^2=R^2 の境界を示し，それぞれの面における外向き単位法線ベクトル n を矢印で描く。 -->

(1) ベクトル場 $\boldsymbol{A}$ の発散 $\nabla \cdot \boldsymbol{A}$ を求めよ。

(2) 領域 $V$ における体積積分 $\int_V \nabla \cdot \boldsymbol{A} \, dV$ を計算せよ。

(3) 円柱の境界面 $S$ は，上面 $S_1$（$z=H$），底面 $S_2$（$z=0$），側面 $S_3$（$x^2+y^2=R^2$）の3つの面からなる。それぞれの面からの外向きフラックスを計算し，全フラックス $\int_S \boldsymbol{A} \cdot \boldsymbol{n} \, dS$ を求めて (2) の結果と一致することを確かめよ。

---

## 解答・解説

### (1)
直交座標系における発散の定義に従い，各成分を空間座標で偏微分します。ベクトル場 $\boldsymbol{A}$ の各成分は $A_x = x$，$A_y = y$，$A_z = z^2$ です。発散の定義式にこれらを代入すると，
$$
\begin{aligned}
\nabla \cdot \boldsymbol{A} &= \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} \\
&= \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(y) + \frac{\partial}{\partial z}(z^2) \\
&= \finalanswer{\nabla \cdot \boldsymbol{A} = 2 + 2z}
\end{aligned}
$$
となります。

### (2)
円柱座標系 $(r, \theta, z)$ を用いて体積積分を実行します。微小体積要素は $dV = r \, dr d\theta dz$ であり，領域 $V$ の積分範囲は $0 \le r \le R$，$0 \le \theta \le 2\pi$，$0 \le z \le H$ です。(1) で求めた被積分関数を代入すると，
$$
\begin{aligned}
\int_V \nabla \cdot \boldsymbol{A} \, dV &= \int_0^H dz \int_0^{2\pi} d\theta \int_0^R dr \, r (2 + 2z) \\
&= \left( \int_0^H (2 + 2z) \, dz \right) \left( \int_0^{2\pi} d\theta \right) \left( \int_0^R r \, dr \right)
\end{aligned}
$$
となります。各定積分をそれぞれ計算すると，
$$
\begin{aligned}
\int_0^H (2 + 2z) \, dz &= \left[ 2z + z^2 \right]_0^H = 2H + H^2 \\
\int_0^{2\pi} d\theta &= 2\pi \\
\int_0^R r \, dr &= \left[ \frac{1}{2}r^2 \right]_0^R = \frac{1}{2}R^2
\end{aligned}
$$
が得られます。これらを掛け合わせることにより，
$$
\begin{aligned}
\int_V \nabla \cdot \boldsymbol{A} \, dV &= (2H + H^2) \cdot 2\pi \cdot \left(\frac{1}{2}R^2\right) \\
&= \finalanswer{\int_V \nabla \cdot \boldsymbol{A} \, dV = \pi R^2 (2H + H^2)}
\end{aligned}
$$
となります。

### (3)
円柱の3つの境界面ごとに外向き単位法線ベクトル $\boldsymbol{n}$ を定め，面積分を個別に計算します。

上面 $S_1$（$z=H$）では，外向き法線は $+z$ 方向を向くため $\boldsymbol{n} = \boldsymbol{e}_z$ です。面上の位置ベクトルに対して $\boldsymbol{A} \cdot \boldsymbol{n} = z^2 = H^2$ と一定になるため，上面の面積 $\pi R^2$ を用いて，
$$
\int_{S_1} \boldsymbol{A} \cdot \boldsymbol{n} \, dS = \int_{S_1} H^2 \, dS = \pi R^2 H^2
$$
となります。

底面 $S_2$（$z=0$）では，外向き法線は $-z$ 方向を向くため $\boldsymbol{n} = -\boldsymbol{e}_z$ です。面上で $z=0$ であることから $\boldsymbol{A} \cdot \boldsymbol{n} = -z^2 = 0$ となり，
$$
\int_{S_2} \boldsymbol{A} \cdot \boldsymbol{n} \, dS = 0
$$
となります。

側面 $S_3$（$r=R$）では，外向き法線は動径方向を向くため $\boldsymbol{n} = \frac{x}{R}\boldsymbol{e}_x + \frac{y}{R}\boldsymbol{e}_y$ です。面上で $x^2+y^2=R^2$ であるため，
$$
\boldsymbol{A} \cdot \boldsymbol{n} = \frac{x^2 + y^2}{R} = \frac{R^2}{R} = R
$$
となります。側面積は $2\pi R H$ であるため，
$$
\int_{S_3} \boldsymbol{A} \cdot \boldsymbol{n} \, dS = \int_{S_3} R \, dS = R \cdot 2\pi R H = 2\pi R^2 H
$$
となります。

3つの面からの寄与をすべて足し合わせると，
$$
\begin{aligned}
\int_S \boldsymbol{A} \cdot \boldsymbol{n} \, dS &= \pi R^2 H^2 + 0 + 2\pi R^2 H \\
&= \finalanswer{\int_S \boldsymbol{A} \cdot \boldsymbol{n} \, dS = \pi R^2 (2H + H^2)}
\end{aligned}
$$
となり，(2) の体積積分の結果と一致することが確かめられます。

===== FILE: 09vector_analysis/05/05_020.md =====
---
tags:
  - 基本
---

# ストークスの定理

## 問題
3次元空間において，ベクトル場 $\boldsymbol{A}$ が
$$
\boldsymbol{A} = -y \boldsymbol{e}_x + x \boldsymbol{e}_y + z^2 \boldsymbol{e}_z
$$
で与えられている。$xy$ 平面上において原点を中心とする半径 $a$ の円周を $C$ とし，その向きは $+z$ 方向から見て反時計回りとする。また，$C$ を境界とする $xy$ 平面上の円板領域を $S$ とし，その法線ベクトルの向きを $+z$ 方向とする。以下の問いに答えよ。

<!-- FIGURE problem: xy 平面上に半径 a の円板領域 S を描く。その境界曲線 C 上に反時計回りの矢印を配置し，円板の中心から +z 方向に伸びる法線ベクトル n を描く。 -->

(1) ベクトル場 $\boldsymbol{A}$ の回転 $\nabla \times \boldsymbol{A}$ を求めよ。

(2) 曲面 $S$ における面積分 $\int_S (\nabla \times \boldsymbol{A}) \cdot \boldsymbol{n} \, dS$ を求めよ。

(3) 閉曲線 $C$ を極座標の偏角 $\theta$ を用いてパラメータ表示し，線積分 $\oint_C \boldsymbol{A} \cdot d\boldsymbol{r}$ を直接計算して (2) の結果と一致することを確かめよ。

---

## 解答・解説

### (1)
直交座標系における回転の定義に従って各成分を計算します。ベクトル場 $\boldsymbol{A}$ の成分は $A_x = -y$，$A_y = x$，$A_z = z^2$ です。回転の行列式表示を成分ごとに展開すると，
$$
\begin{aligned}
\nabla \times \boldsymbol{A} &= \left( \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} \right) \boldsymbol{e}_x + \left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right) \boldsymbol{e}_y + \left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right) \boldsymbol{e}_z \\
&= (0 - 0) \boldsymbol{e}_x + (0 - 0) \boldsymbol{e}_y + (1 - (-1)) \boldsymbol{e}_z
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{\nabla \times \boldsymbol{A} = 2 \boldsymbol{e}_z}
$$
となります。

### (2)
曲面 $S$ は $xy$ 平面上の円板であり，その単位法線ベクトルは問題の設定より $\boldsymbol{n} = \boldsymbol{e}_z$ です。被積分関数は，
$$
(\nabla \times \boldsymbol{A}) \cdot \boldsymbol{n} = (2 \boldsymbol{e}_z) \cdot \boldsymbol{e}_z = 2
$$
と一定になります。したがって，面積分は円板の面積 $\pi a^2$ を用いて，
$$
\begin{aligned}
\int_S (\nabla \times \boldsymbol{A}) \cdot \boldsymbol{n} \, dS &= \int_S 2 \, dS \\
&= 2 \int_S dS \\
&= \finalanswer{\int_S (\nabla \times \boldsymbol{A}) \cdot \boldsymbol{n} \, dS = 2\pi a^2}
\end{aligned}
$$
となります。

### (3)
閉曲線 $C$ を偏角 $\theta$（$0 \le \theta \le 2\pi$）を用いて媒介変数表示します。位置ベクトルおよびその微分は，
$$
\boldsymbol{r}(\theta) = a\cos\theta \boldsymbol{e}_x + a\sin\theta \boldsymbol{e}_y
$$
$$
d\boldsymbol{r} = (-a\sin\theta \boldsymbol{e}_x + a\cos\theta \boldsymbol{e}_y) \, d\theta
$$
となります。曲線 $C$ 上において $z=0$ であり，ベクトル場 $\boldsymbol{A}$ は，
$$
\boldsymbol{A} = -a\sin\theta \boldsymbol{e}_x + a\cos\theta \boldsymbol{e}_y
$$
と表されます。線積分の被積分関数となる内積を計算すると，
$$
\begin{aligned}
\boldsymbol{A} \cdot d\boldsymbol{r} &= \left[ (-a\sin\theta)(-a\sin\theta) + (a\cos\theta)(a\cos\theta) \right] d\theta \\
&= a^2 (\sin^2\theta + \cos^2\theta) \, d\theta \\
&= a^2 \, d\theta
\end{aligned}
$$
となります。これを $\theta$ について $0$ から $2\pi$ まで積分すると，
$$
\begin{aligned}
\oint_C \boldsymbol{A} \cdot d\boldsymbol{r} &= \int_0^{2\pi} a^2 \, d\theta \\
&= \finalanswer{\oint_C \boldsymbol{A} \cdot d\boldsymbol{r} = 2\pi a^2}
\end{aligned}
$$
が得られ，(2) の面積分の結果と一致することが示されます。

===== FILE: 09vector_analysis/05/05_030.md =====
---
tags:
  - 基本
---

# 平面のグリーンの定理

## 問題
$xy$ 平面上の有界な領域 $D$ と，その境界をなす反時計回りの滑らかな単一閉曲線 $C$ を考える。以下の問いに答えよ。

(1) 滑らかなスカラー関数 $P(x, y)$，$Q(x, y)$ に対する平面のグリーンの定理
$$
\oint_C (P \, dx + Q \, dy) = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$
を用いて，領域 $D$ の面積 $S$ が線積分
$$
S = \frac{1}{2} \oint_C (x \, dy - y \, dx)
$$
として表されることを示せ。

(2) 長軸の半径が $a$，短軸の半径が $b$ である楕円の境界線 $C$ を
$$
x = a\cos t, \quad y = b\sin t \quad (0 \le t \le 2\pi)
$$
とパラメータ表示するとき，$x \, dy - y \, dx$ を $t$ と $dt$ を用いて表せ。

(3) (1) の公式を用いて，楕円が囲む面積 $S$ を求めよ。

---

## 解答・解説

### (1)
領域 $D$ の面積 $S$ は，定義より重積分
$$
S = \iint_D 1 \, dx dy
$$
で与えられます。グリーンの定理の右辺の被積分関数が $1$ になるように，関数 $P(x, y)$ と $Q(x, y)$ を選びます。ここでは $P(x, y) = -y$，$Q(x, y) = x$ とおくと，各偏導関数は，
$$
\frac{\partial Q}{\partial x} = 1, \quad \frac{\partial P}{\partial y} = -1
$$
となります。これをグリーンの定理に適用すると，
$$
\begin{aligned}
\oint_C (-y \, dx + x \, dy) &= \iint_D (1 - (-1)) \, dx dy \\
&= 2 \iint_D dx dy \\
&= 2S
\end{aligned}
$$
が得られます。両辺を $2$ で割ることにより，
$$
\finalanswer{S = \frac{1}{2} \oint_C (x \, dy - y \, dx)}
$$
が導かれます。

### (2)
与えられたパラメータ表示から，微小変化量 $dx$ および $dy$ を求めます。パラメータ $t$ で微分すると，
$$
dx = -a\sin t \, dt, \quad dy = b\cos t \, dt
$$
となります。これらを $x \, dy - y \, dx$ に代入すると，
$$
\begin{aligned}
x \, dy - y \, dx &= (a\cos t)(b\cos t \, dt) - (b\sin t)(-a\sin t \, dt) \\
&= ab (\cos^2 t + \sin^2 t) \, dt
\end{aligned}
$$
となります。三角関数の相互関係 $\cos^2 t + \sin^2 t = 1$ を用いると，
$$
\finalanswer{x \, dy - y \, dx = ab \, dt}
$$
となります。

### (3)
(1) で導いた面積公式に，(2) で求めた微分形式を代入して積分を実行します。閉曲線全体を一周するパラメータの積分範囲は $0 \le t \le 2\pi$ です。したがって，
$$
\begin{aligned}
S &= \frac{1}{2} \oint_C (x \, dy - y \, dx) \\
&= \frac{1}{2} \int_0^{2\pi} ab \, dt \\
&= \frac{1}{2} ab \left[ t \right]_0^{2\pi} \\
&= \finalanswer{S = \pi ab}
\end{aligned}
$$
となります。この結果において $a = b = R$ と置くと円の面積 $\pi R^2$ と一致します。

===== FILE: 09vector_analysis/05/05_040.md =====
---
tags:
  - 標準
---

# グリーンの恒等式

## 問題
滑らかな境界面 $S$ を持つ3次元の有界領域 $V$ において，2回連続微分可能なスカラー場 $\phi(\boldsymbol{r})$ および $\psi(\boldsymbol{r})$ を考える。境界面 $S$ における外向き単位法線ベクトルを $\boldsymbol{n}$ とし，法線微分を $\frac{\partial \psi}{\partial n} = \nabla \psi \cdot \boldsymbol{n}$ と表記する。以下の問いに答えよ。

(1) ベクトル場 $\boldsymbol{A} = \phi \nabla \psi$ にガウスの発散定理を適用することにより，グリーンの第1恒等式
$$
\int_V \left( \phi \nabla^2 \psi + \nabla \phi \cdot \nabla \psi \right) dV = \int_S \phi \frac{\partial \psi}{\partial n} \, dS
$$
が成り立つことを示せ。

(2) グリーンの第1恒等式において $\phi$ と $\psi$ を入れ替えた式との差をとることで，グリーンの第2恒等式を導け。

(3) 領域 $V$ においてラプラス方程式 $\nabla^2 u = 0$ を満たし，境界面 $S$ 上で与えられた関数値をとるディリクレ問題
$$
u(\boldsymbol{r}) = f(\boldsymbol{r}) \quad (\boldsymbol{r} \in S)
$$
の解は，ただ1つに定まることをグリーンの第1恒等式を用いて示せ。

---

## 解答・解説

### (1)
ベクトル解析の公式を用いてベクトル場 $\boldsymbol{A} = \phi \nabla \psi$ の発散を計算します。積の微分法により，
$$
\begin{aligned}
\nabla \cdot \boldsymbol{A} &= \nabla \cdot (\phi \nabla \psi) \\
&= \nabla \phi \cdot \nabla \psi + \phi \nabla \cdot (\nabla \psi) \\
&= \nabla \phi \cdot \nabla \psi + \phi \nabla^2 \psi
\end{aligned}
$$
が得られます。ここでガウスの発散定理
$$
\int_V \nabla \cdot \boldsymbol{A} \, dV = \int_S \boldsymbol{A} \cdot \boldsymbol{n} \, dS
$$
を適用します。右辺の被積分関数は，
$$
\boldsymbol{A} \cdot \boldsymbol{n} = (\phi \nabla \psi) \cdot \boldsymbol{n} = \phi (\nabla \psi \cdot \boldsymbol{n}) = \phi \frac{\partial \psi}{\partial n}
$$
となります。したがって，体積積分と面積分を結ぶ等式として，
$$
\finalanswer{\int_V \left( \phi \nabla^2 \psi + \nabla \phi \cdot \nabla \psi \right) dV = \int_S \phi \frac{\partial \psi}{\partial n} \, dS}
$$
が導かれます。

### (2)
(1) で得られたグリーンの第1恒等式において，2つのスカラー場 $\phi$ と $\psi$ の役割を入れ替えると，
$$
\int_V \left( \psi \nabla^2 \phi + \nabla \psi \cdot \nabla \phi \right) dV = \int_S \psi \frac{\partial \phi}{\partial n} \, dS
$$
が成り立ちます。内積の可換性 $\nabla \phi \cdot \nabla \psi = \nabla \psi \cdot \nabla \phi$ を考慮して，第1恒等式からこの式の辺々を差し引くと，
$$
\int_V \left( \phi \nabla^2 \psi - \psi \nabla^2 \phi \right) dV = \finalanswer{\int_V \left( \phi \nabla^2 \psi - \psi \nabla^2 \phi \right) dV = \int_S \left( \phi \frac{\partial \psi}{\partial n} - \psi \frac{\partial \phi}{\partial n} \right) dS}
$$
が得られます。これがグリーンの第2恒等式です。

### (3)
境界値問題を満たす解が2つ存在すると仮定し，それらを $u_1(\boldsymbol{r})$，$u_2(\boldsymbol{r})$ と置きます。これらの差として新たな関数
$$
w(\boldsymbol{r}) = u_1(\boldsymbol{r}) - u_2(\boldsymbol{r})
$$
を定義します。ラプラス作用素の線形性より，領域 $V$ 内において，
$$
\nabla^2 w = \nabla^2 u_1 - \nabla^2 u_2 = 0
$$
が成り立ちます。また境界面 $S$ 上ではともに条件を満たすため，
$$
w(\boldsymbol{r}) = f(\boldsymbol{r}) - f(\boldsymbol{r}) = 0 \quad (\boldsymbol{r} \in S)
$$
となります。(1) のグリーンの第1恒等式において $\phi = \psi = w$ と置くと，
$$
\int_V \left( w \nabla^2 w + |\nabla w|^2 \right) dV = \int_S w \frac{\partial w}{\partial n} \, dS
$$
が得られます。ここで $\nabla^2 w = 0$ および境界面上で $w = 0$ を代入すると，
$$
\int_V |\nabla w|^2 \, dV = 0
$$
となります。被積分関数は $|\nabla w|^2 \ge 0$ を満たし連続であるため，領域 $V$ のすべての点において，
$$
|\nabla w| = 0 \implies \nabla w = \boldsymbol{0}
$$
でなければなりません。空間微分が恒等的に $0$ であることから $w(\boldsymbol{r})$ は領域 $V$ 全体で定数となります。境界面 $S$ 上で $w = 0$ であるため，領域 $V$ の全体で，
$$
\finalanswer{w(\boldsymbol{r}) = 0 \implies u_1(\boldsymbol{r}) = u_2(\boldsymbol{r})}
$$
となり，解がただ1つに定まることが証明されます。

===== FILE: 09vector_analysis/05/05_050.md =====
---
tags:
  - 標準
---

# 積分定理と保存則

## 問題
空間内に固定された任意の滑らかな閉曲面 $S$ と，それが囲む体積領域 $V$ を考える。空間に分布するある物理量の体積密度を $\rho(\boldsymbol{r}, t)$，流束密度ベクトルを $\boldsymbol{j}(\boldsymbol{r}, t)$ とする。この物理量は系内で新しく生成されたり消滅したりしないものとする。以下の問いに答えよ。

(1) 領域 $V$ 内の物理量の総量の時間変化率が，境界面 $S$ を通して外部へ流出する全フラックスの符号を変えたものに等しいという積分形の保存則
$$
\frac{d}{dt} \int_V \rho \, dV = - \int_S \boldsymbol{j} \cdot \boldsymbol{n} \, dS
$$
に対し，ガウスの発散定理を適用して1つの体積積分の等式にまとめよ。ただし $\boldsymbol{n}$ は $S$ の外向き単位法線ベクトルとする。

(2) 領域 $V$ が空間内の任意にとられた領域であることから導かれる，微分形の局所保存則（連続の式）を求めよ。

(3) 時間的に密度分布が変化しない定常状態（$\frac{\partial \rho}{\partial t} = 0$）において，閉曲面 $S$ を通過して流出する全流束（電磁気学における全電流に相当）が $0$ になることを示せ。

---

## 解答・解説

### (1)
領域 $V$ は時間的に固定されているため，時間微分と体積積分の順序を交換することができます。左辺は，
$$
\frac{d}{dt} \int_V \rho \, dV = \int_V \frac{\partial \rho}{\partial t} \, dV
$$
と変形されます。一方，右辺の面積分に対してガウスの発散定理を適用すると，
$$
\int_S \boldsymbol{j} \cdot \boldsymbol{n} \, dS = \int_V \nabla \cdot \boldsymbol{j} \, dV
$$
となります。右辺の項を左辺に移項して体積積分を1つにまとめると，
$$
\finalanswer{\int_V \left( \frac{\partial \rho}{\partial t} + \nabla \cdot \boldsymbol{j} \right) dV = 0}
$$
となります。

### (2)
(1) で得られた等式は，空間内のいかなる領域 $V$ を選んでも常に成立します。もし被積分関数がある点で非零であれば，その点の近傍で積分値が非零となる領域をとることができて矛盾が生じます。したがって，被積分関数が空間の各点で常に $0$ でなければなりません。これにより，局所的な連続の式として，
$$
\finalanswer{\frac{\partial \rho}{\partial t} + \nabla \cdot \boldsymbol{j} = 0}
$$
が得られます。

### (3)
定常状態の条件 $\frac{\partial \rho}{\partial t} = 0$ を (2) で得た連続の式に代入すると，
$$
\nabla \cdot \boldsymbol{j} = 0
$$
が成り立ちます。閉曲面 $S$ を通過して流出する全流束は，定義より面積分 $\int_S \boldsymbol{j} \cdot \boldsymbol{n} \, dS$ です。この面積分に再びガウスの発散定理を適用すると，
$$
\begin{aligned}
\int_S \boldsymbol{j} \cdot \boldsymbol{n} \, dS &= \int_V \nabla \cdot \boldsymbol{j} \, dV \\
&= \int_V 0 \, dV \\
&= \finalanswer{\int_S \boldsymbol{j} \cdot \boldsymbol{n} \, dS = 0}
\end{aligned}
$$
となり，閉曲面から流出する全流束が $0$ になることが示されます。

===== FILE: 09vector_analysis/05/05_060.md =====
---
tags:
  - 発展
---

# ヘルムホルツの分解定理

## 問題
空間全体で滑らかであり，無限遠で十分速く $0$ に収束する任意のベクトル場 $\boldsymbol{F}(\boldsymbol{r})$ は，回転のない縦波成分（渦なし場）と，発散のない横波成分（湧き出しなし場）の和として
$$
\boldsymbol{F} = -\nabla \phi + \nabla \times \boldsymbol{A}
$$
と一意に分解できる。これをヘルムホルツの分解定理という。以下の問いに答えよ。

(1) 縦波成分 $\boldsymbol{F}_L = -\nabla \phi$ の回転 $\nabla \times \boldsymbol{F}_L$，および横波成分 $\boldsymbol{F}_T = \nabla \times \boldsymbol{A}$ の発散 $\nabla \cdot \boldsymbol{F}_T$ をそれぞれ計算せよ。

(2) ベクトル恒等式
$$
\nabla \times (\nabla \times \boldsymbol{A}) = \nabla (\nabla \cdot \boldsymbol{A}) - \nabla^2 \boldsymbol{A}
$$
を用い，ゲージ条件としてクーロンゲージ $\nabla \cdot \boldsymbol{A} = 0$ を課すとき，$\nabla \cdot \boldsymbol{F}$ および $\nabla \times \boldsymbol{F}$ を $\phi$ と $\boldsymbol{A}$ のラプラシアンを用いて表せ。

(3) ポアソン方程式 $\nabla^2 u(\boldsymbol{r}) = -g(\boldsymbol{r})$ の空間全体での解が
$$
u(\boldsymbol{r}) = \frac{1}{4\pi} \int \frac{g(\boldsymbol{r}')}{|\boldsymbol{r} - \boldsymbol{r}'|} \, dV'
$$
で与えられることを利用して，ポテンシャル $\phi(\boldsymbol{r})$ を $\boldsymbol{F}$ の発散を含む体積積分の形で表せ。

---

## 解答・解説

### (1)
ベクトル解析の基本的な恒等式を適用します。任意の滑らかなスカラー場 $\phi$ に対し，勾配の回転は恒等的に零ベクトルとなります。成分を用いて計算すると，
$$
\begin{aligned}
\nabla \times \boldsymbol{F}_L &= -\nabla \times (\nabla \phi) \\
&= - \left( \frac{\partial^2 \phi}{\partial y \partial z} - \frac{\partial^2 \phi}{\partial z \partial y} \right) \boldsymbol{e}_x - \left( \frac{\partial^2 \phi}{\partial z \partial x} - \frac{\partial^2 \phi}{\partial x \partial z} \right) \boldsymbol{e}_y - \left( \frac{\partial^2 \phi}{\partial x \partial y} - \frac{\partial^2 \phi}{\partial y \partial x} \right) \boldsymbol{e}_z \\
&= \finalanswer{\nabla \times \boldsymbol{F}_L = \boldsymbol{0}}
\end{aligned}
$$
となります。同様に，任意のベクトル場 $\boldsymbol{A}$ に対し，回転の発散は恒等的に零となります。
$$
\begin{aligned}
\nabla \cdot \boldsymbol{F}_T &= \nabla \cdot (\nabla \times \boldsymbol{A}) \\
&= \frac{\partial}{\partial x}\left( \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} \right) + \frac{\partial}{\partial y}\left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right) + \frac{\partial}{\partial z}\left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right) \\
&= \finalanswer{\nabla \cdot \boldsymbol{F}_T = 0}
\end{aligned}
$$
となります。

### (2)
分解式 $\boldsymbol{F} = -\nabla \phi + \nabla \times \boldsymbol{A}$ の発散をとります。(1) の結果より $\nabla \cdot (\nabla \times \boldsymbol{A}) = 0$ であるため，
$$
\nabla \cdot \boldsymbol{F} = -\nabla \cdot (\nabla \phi) + \nabla \cdot (\nabla \times \boldsymbol{A}) = -\nabla^2 \phi
$$
となります。したがって，
$$
\finalanswer{\nabla \cdot \boldsymbol{F} = -\nabla^2 \phi}
$$
が得られます。

次に，分解式の回転をとります。(1) より $\nabla \times (\nabla \phi) = \boldsymbol{0}$ であり，与えられた恒等式とクーロンゲージ条件 $\nabla \cdot \boldsymbol{A} = 0$ を代入すると，
$$
\begin{aligned}
\nabla \times \boldsymbol{F} &= -\nabla \times (\nabla \phi) + \nabla \times (\nabla \times \boldsymbol{A}) \\
&= \boldsymbol{0} + \nabla (\nabla \cdot \boldsymbol{A}) - \nabla^2 \boldsymbol{A} \\
&= \finalanswer{\nabla \times \boldsymbol{F} = -\nabla^2 \boldsymbol{A}}
\end{aligned}
$$
となります。

### (3)
(2) で導いた関係式
$$
\nabla^2 \phi(\boldsymbol{r}) = - \nabla \cdot \boldsymbol{F}(\boldsymbol{r})
$$
は，スカラー関数 $\phi$ に関するポアソン方程式です。ここで源となる密度関数は $g(\boldsymbol{r}) = \nabla \cdot \boldsymbol{F}(\boldsymbol{r})$ に対応します。問題文で与えられたポアソン方程式のグリーン関数解の公式に $g(\boldsymbol{r}')$ を代入することにより，
$$
\finalanswer{\phi(\boldsymbol{r}) = \frac{1}{4\pi} \int \frac{\nabla' \cdot \boldsymbol{F}(\boldsymbol{r}')}{|\boldsymbol{r} - \boldsymbol{r}'|} \, dV'}
$$
となります。ただし $\nabla'$ は積分変数 $\boldsymbol{r}'$ に関する微分作用素を表します。この式は，場 $\boldsymbol{F}$ の発散（湧き出し）がスカラーポテンシャルの源になっていることを明示しています。

===== FILE: 09vector_analysis/06/06_010.md =====
---
tags:
  - 発展
---

# 1/r のラプラシアンとデルタ関数

## 問題
3次元空間の位置ベクトルを $\boldsymbol{r} = x\boldsymbol{e}_x + y\boldsymbol{e}_y + z\boldsymbol{e}_z$，原点からの距離を $r = |\boldsymbol{r}| = \sqrt{x^2+y^2+z^2}$ とする。以下の問いに答えよ。

(1) 原点以外の領域（$r \ne 0$）において，極座標における球対称関数のラプラシアンの公式
$$
\nabla^2 f(r) = \frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{df}{dr} \right)
$$
を用いて，$\nabla^2 \left( \frac{1}{r} \right)$ を計算せよ。

(2) 原点を中心とする半径 $R$ の球面を $S$ とし，その外向き単位法線ベクトルを $\boldsymbol{n} = \frac{\boldsymbol{r}}{R}$ とする。ベクトル場 $\nabla \left( \frac{1}{r} \right)$ の球面 $S$ 上における面積分
$$
\int_S \nabla \left( \frac{1}{r} \right) \cdot \boldsymbol{n} \, dS
$$
を直接計算せよ。

(3) 3次元ディラックのデルタ関数 $\delta(\boldsymbol{r})$ は，原点を含む任意の領域 $V$ において
$$
\int_V \delta(\boldsymbol{r}) \, dV = 1
$$
を満たし，$r \ne 0$ で $0$ となる超関数である。ガウスの発散定理と (1), (2) の結果を整合させることにより，空間全体で成立する関係式
$$
\nabla^2 \left( \frac{1}{r} \right) = -4\pi \delta(\boldsymbol{r})
$$
を導け。

---

## 解答・解説

### (1)
関数 $f(r) = \frac{1}{r}$ を $r$ で微分すると，
$$
\frac{df}{dr} = -\frac{1}{r^2}
$$
となります。これに $r^2$ を掛けると，
$$
r^2 \frac{df}{dr} = r^2 \left( -\frac{1}{r^2} \right) = -1
$$
となります。この値は $r$ に依存しない定数です。公式に従ってこれをさらに $r$ で微分すると，
$$
\frac{d}{dr} \left( r^2 \frac{df}{dr} \right) = \frac{d}{dr}(-1) = 0
$$
となります。したがって，$r \ne 0$ において，
$$
\finalanswer{\nabla^2 \left( \frac{1}{r} \right) = 0}
$$
が得られます。

### (2)
まずスカラー関数 $1/r$ の勾配を求めます。連鎖律を用いると，
$$
\frac{\partial}{\partial x} \left( \frac{1}{r} \right) = -\frac{1}{r^2} \frac{\partial r}{\partial x} = -\frac{x}{r^3}
$$
となるため，ベクトル表記では
$$
\nabla \left( \frac{1}{r} \right) = -\frac{\boldsymbol{r}}{r^3}
$$
となります。半径 $R$ の球面 $S$ 上では $r = R$ であり，外向き単位法線ベクトルは $\boldsymbol{n} = \frac{\boldsymbol{r}}{R}$ です。面上の各点における内積を計算すると，
$$
\begin{aligned}
\nabla \left( \frac{1}{r} \right) \cdot \boldsymbol{n} &= \left( -\frac{\boldsymbol{r}}{R^3} \right) \cdot \left( \frac{\boldsymbol{r}}{R} \right) \\
&= -\frac{\boldsymbol{r} \cdot \boldsymbol{r}}{R^4} \\
&= -\frac{R^2}{R^4} \\
&= -\frac{1}{R^2}
\end{aligned}
$$
となります。この値は球面上のすべての点で一定です。球面の全面積は $4\pi R^2$ であるため，面積分を実行すると，
$$
\begin{aligned}
\int_S \nabla \left( \frac{1}{r} \right) \cdot \boldsymbol{n} \, dS &= \int_S \left( -\frac{1}{R^2} \right) dS \\
&= -\frac{1}{R^2} \int_S dS \\
&= -\frac{1}{R^2} \cdot 4\pi R^2 \\
&= \finalanswer{\int_S \nabla \left( \frac{1}{r} \right) \cdot \boldsymbol{n} \, dS = -4\pi}
\end{aligned}
$$
となります。この積分値は球の半径 $R$ に依存しません。

### (3)
原点を内部に含む任意の有界領域 $V$ と，その境界面 $S$ を考えます。ガウスの発散定理を形式的に適用すると，
$$
\int_V \nabla^2 \left( \frac{1}{r} \right) dV = \int_S \nabla \left( \frac{1}{r} \right) \cdot \boldsymbol{n} \, dS
$$
が成り立ちます。(2) より，右辺の面積分の値は領域の形状や大きさによらず常に $-4\pi$ となります。

一方，(1) より被積分関数 $\nabla^2 (1/r)$ は $r \ne 0$ のすべての点で $0$ です。それにもかかわらず，原点を含む任意の体積で積分した結果が $-4\pi$ という有限の値を保つことから，被積分関数は原点 $\boldsymbol{r} = \boldsymbol{0}$ に特異的に集中した重みを持つ必要があります。3次元デルタ関数の定義
$$
\int_V \delta(\boldsymbol{r}) \, dV = 1
$$
と比較すると，両者の空間積分値が領域の選び方によらず常に $-4\pi$ 倍の関係で一致することから，超関数の等式として
$$
\finalanswer{\nabla^2 \left( \frac{1}{r} \right) = -4\pi \delta(\boldsymbol{r})}
$$
が導かれます。

===== FILE: 09vector_analysis/06/06_020.md =====
---
tags:
  - 標準
---

# 点源の場とガウスの法則

## 問題
原点に置かれた強さ $Q$ の点源が作るベクトル場が
$$
\boldsymbol{E}(\boldsymbol{r}) = \frac{Q}{4\pi} \frac{\boldsymbol{r}}{r^3}
$$
で与えられている。ただし $\boldsymbol{r} = (x, y, z)$，$r = |\boldsymbol{r}|$ である。以下の問いに答えよ。

<!-- FIGURE problem: 原点 O に点源 Q が置かれ，それを囲む滑らかな閉曲面 S と，原点の直近に描かれた小さな半径 ε の球面 S_ε を描く。両曲面の外向き法線ベクトル n をそれぞれ図示する。 -->

(1) 原点以外の領域（$r \ne 0$）において，発散 $\nabla \cdot \boldsymbol{E}$ を計算せよ。

(2) 原点を内部に含む滑らかな閉曲面 $S$ を考える。原点を中心とし，曲面 $S$ の内部に完全に含まれる十分小さな半径 $\varepsilon$ の球面を $S_\varepsilon$ とする。曲面 $S$ と $S_\varepsilon$ で挟まれた領域にガウスの発散定理を適用することにより，
$$
\int_S \boldsymbol{E} \cdot \boldsymbol{n} \, dS = \int_{S_\varepsilon} \boldsymbol{E} \cdot \boldsymbol{n} \, dS
$$
が成り立つことを示せ。ただし各曲面上の法線ベクトル $\boldsymbol{n}$ は，原点から外側へ向かう向きにとる。

(3) 球面 $S_\varepsilon$ 上における面積分を直接計算し，閉曲面 $S$ を通過する全フラックス $\int_S \boldsymbol{E} \cdot \boldsymbol{n} \, dS$ の値を求めよ。

---

## 解答・解説

### (1)
ベクトル解析の公式 $\nabla \cdot (f \boldsymbol{r}) = (\nabla f) \cdot \boldsymbol{r} + f (\nabla \cdot \boldsymbol{r})$ を適用します。スカラー関数 $f(r) = r^{-3}$ に対し，その勾配は連鎖律より，
$$
\nabla (r^{-3}) = -3r^{-4} \frac{\boldsymbol{r}}{r} = -3 \frac{\boldsymbol{r}}{r^5}
$$
となります。また位置ベクトルの発散は，
$$
\nabla \cdot \boldsymbol{r} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3
$$
となります。これらを合わせて $\nabla \cdot \left(\frac{\boldsymbol{r}}{r^3}\right)$ を計算すると，
$$
\begin{aligned}
\nabla \cdot \left(\frac{\boldsymbol{r}}{r^3}\right) &= \left( -3 \frac{\boldsymbol{r}}{r^5} \right) \cdot \boldsymbol{r} + \frac{1}{r^3} \cdot 3 \\
&= -3 \frac{r^2}{r^5} + \frac{3}{r^3} \\
&= -\frac{3}{r^3} + \frac{3}{r^3} \\
&= 0
\end{aligned}
$$
が得られます。定数倍を考慮することにより，原点以外の領域において，
$$
\finalanswer{\nabla \cdot \boldsymbol{E} = 0}
$$
となります。

### (2)
曲面 $S$ の内部から，半径 $\varepsilon$ の球の内部を取り除いた領域を $V_\varepsilon$ とします。この領域 $V_\varepsilon$ には原点が含まれないため，領域全体で場 $\boldsymbol{E}$ は連続かつ微分可能です。$V_\varepsilon$ の全境界に対するガウスの発散定理を適用すると，
$$
\int_{V_\varepsilon} \nabla \cdot \boldsymbol{E} \, dV = \int_S \boldsymbol{E} \cdot \boldsymbol{n} \, dS + \int_{S_\varepsilon} \boldsymbol{E} \cdot \boldsymbol{n}_{\text{in}} \, dS
$$
が成り立ちます。ここで $\boldsymbol{n}_{\text{in}}$ は領域 $V_\varepsilon$ から見た外向き法線ベクトルであり，原点に向かう内向きを指します。原点から外側を向く単位法線ベクトルを $\boldsymbol{n}$ とすると $\boldsymbol{n}_{\text{in}} = -\boldsymbol{n}$ です。(1) より領域 $V_\varepsilon$ 内で $\nabla \cdot \boldsymbol{E} = 0$ であるため，
$$
0 = \int_S \boldsymbol{E} \cdot \boldsymbol{n} \, dS - \int_{S_\varepsilon} \boldsymbol{E} \cdot \boldsymbol{n} \, dS
$$
となります。したがって，
$$
\finalanswer{\int_S \boldsymbol{E} \cdot \boldsymbol{n} \, dS = \int_{S_\varepsilon} \boldsymbol{E} \cdot \boldsymbol{n} \, dS}
$$
が示されます。

### (3)
球面 $S_\varepsilon$ 上において $r = \varepsilon$ であり，外向き単位法線ベクトルは $\boldsymbol{n} = \frac{\boldsymbol{r}}{\varepsilon}$ です。被積分関数となる内積を計算すると，
$$
\begin{aligned}
\boldsymbol{E} \cdot \boldsymbol{n} &= \left( \frac{Q}{4\pi \varepsilon^3} \boldsymbol{r} \right) \cdot \left( \frac{\boldsymbol{r}}{\varepsilon} \right) \\
&= \frac{Q}{4\pi \varepsilon^4} (\boldsymbol{r} \cdot \boldsymbol{r}) \\
&= \frac{Q}{4\pi \varepsilon^4} \varepsilon^2 \\
&= \frac{Q}{4\pi \varepsilon^2}
\end{aligned}
$$
となります。この値は球面上のすべての点で一定です。半径 $\varepsilon$ の球面の表面積は $4\pi \varepsilon^2$ であるため，面積分を実行すると，
$$
\begin{aligned}
\int_{S_\varepsilon} \boldsymbol{E} \cdot \boldsymbol{n} \, dS &= \frac{Q}{4\pi \varepsilon^2} \int_{S_\varepsilon} dS \\
&= \frac{Q}{4\pi \varepsilon^2} \cdot 4\pi \varepsilon^2 \\
&= Q
\end{aligned}
$$
が得られます。(2) の結果より，この積分値は外側の閉曲面 $S$ における面積分と等しいため，
$$
\finalanswer{\int_S \boldsymbol{E} \cdot \boldsymbol{n} \, dS = Q}
$$
となります。この結果は電磁気学におけるガウスの法則そのものを表しています。

===== FILE: 09vector_analysis/06/06_030.md =====
---
tags:
  - 発展
---

# 多重極展開の入口

## 問題
原点付近に局在する電荷系を考える。源となる点電荷の位置ベクトルを $\boldsymbol{r}'$，遠方の観測点の位置ベクトルを $\boldsymbol{r}$ とし，$r = |\boldsymbol{r}|$，$r' = |\boldsymbol{r}'|$ とする。観測点は源に比べて十分遠方にある（$r' \ll r$）とする。以下の問いに答えよ。

(1) 距離の逆数
$$
\frac{1}{|\boldsymbol{r} - \boldsymbol{r}'|} = \frac{1}{\sqrt{r^2 - 2\boldsymbol{r}\cdot\boldsymbol{r}' + r'^2}}
$$
に対し，$s = \frac{2\boldsymbol{r}\cdot\boldsymbol{r}' - r'^2}{r^2}$ と置いてべき級数展開を行うことにより，$\frac{r'}{r}$ の1次の微小量まで展開した式を求めよ。

(2) 複数の点電荷 $q_i$ が位置 $\boldsymbol{r}_i$ に配置されているとき，遠方に作る静電ポテンシャル
$$
\phi(\boldsymbol{r}) = \frac{1}{4\pi\varepsilon_0} \sum_i \frac{q_i}{|\boldsymbol{r} - \boldsymbol{r}_i|}
$$
に対し，(1) の結果を適用せよ。全電荷 $Q = \sum_i q_i$ および双極子モーメント $\boldsymbol{p} = \sum_i q_i \boldsymbol{r}_i$ を用いて，$\phi(\boldsymbol{r})$ を $\frac{1}{r^2}$ の項まで求めよ。

(3) $z$ 軸上の点 $(0, 0, d/2)$ に電荷 $+q$，点 $(0, 0, -d/2)$ に電荷 $-q$ が置かれた電気双極子を考える。この系の全電荷 $Q$ および双極子モーメント $\boldsymbol{p}$ を求め，遠方でのポテンシャル $\phi(\boldsymbol{r})$ を極座標 $(r, \theta)$ を用いて表せ。

---

## 解答・解説

### (1)
距離の逆数を $r$ でくくり出すと，
$$
\frac{1}{|\boldsymbol{r} - \boldsymbol{r}'|} = \frac{1}{r} \left( 1 - \frac{2\boldsymbol{r}\cdot\boldsymbol{r}' - r'^2}{r^2} \right)^{-1/2} = \frac{1}{r} (1 - s)^{-1/2}
$$
と変形されます。$|s| \ll 1$ であるため，関数 $(1-s)^{-1/2}$ をマクローリン展開すると，
$$
(1 - s)^{-1/2} = 1 + \frac{1}{2}s + \frac{3}{8}s^2 + \dots
$$
となります。ここで $s$ の定義式を代入し，$r'/r$ の1次の項までを取り出すと，
$$
\begin{aligned}
\frac{1}{|\boldsymbol{r} - \boldsymbol{r}'|} &= \frac{1}{r} \left[ 1 + \frac{1}{2} \left( \frac{2\boldsymbol{r}\cdot\boldsymbol{r}' - r'^2}{r^2} \right) + \mathcal{O}\left( \left(\frac{r'}{r}\right)^2 \right) \right] \\
&= \frac{1}{r} \left( 1 + \frac{\boldsymbol{r}\cdot\boldsymbol{r}'}{r^2} \right) + \mathcal{O}\left( \frac{1}{r^3} \right)
\end{aligned}
$$
が得られます。したがって，1次までの展開式は，
$$
\finalanswer{\frac{1}{|\boldsymbol{r} - \boldsymbol{r}'|} = \frac{1}{r} + \frac{\boldsymbol{r}\cdot\boldsymbol{r}'}{r^3}}
$$
となります。

### (2)
各電荷の作るポテンシャルの表式に (1) で求めた展開式を代入します。
$$
\begin{aligned}
\phi(\boldsymbol{r}) &= \frac{1}{4\pi\varepsilon_0} \sum_i q_i \left( \frac{1}{r} + \frac{\boldsymbol{r}\cdot\boldsymbol{r}_i}{r^3} \right) \\
&= \frac{1}{4\pi\varepsilon_0} \left( \frac{1}{r} \sum_i q_i + \frac{\boldsymbol{r}}{r^3} \cdot \sum_i q_i \boldsymbol{r}_i \right)
\end{aligned}
$$
となります。ここで全電荷の定義 $Q = \sum_i q_i$ および双極子モーメントの定義 $\boldsymbol{p} = \sum_i q_i \boldsymbol{r}_i$ を代入すると，
$$
\finalanswer{\phi(\boldsymbol{r}) = \frac{1}{4\pi\varepsilon_0} \left( \frac{Q}{r} + \frac{\boldsymbol{p}\cdot\boldsymbol{r}}{r^3} \right)}
$$
が得られます。第1項は単一の点電荷としての寄与（モノポール項），第2項は電荷の偏りによる寄与（ダイポール項）を表します。

### (3)
与えられた2つの点電荷について，定義に従って各物理量を計算します。全電荷は，
$$
Q = (+q) + (-q) = 0
$$
となります。双極子モーメントは，各位置ベクトル $\boldsymbol{r}_1 = \frac{d}{2}\boldsymbol{e}_z$，$\boldsymbol{r}_2 = -\frac{d}{2}\boldsymbol{e}_z$ を用いて，
$$
\begin{aligned}
\boldsymbol{p} &= q \left( \frac{d}{2}\boldsymbol{e}_z \right) + (-q) \left( -\frac{d}{2}\boldsymbol{e}_z \right) \\
&= q d \boldsymbol{e}_z
\end{aligned}
$$
となります。全電荷と双極子モーメントはそれぞれ，
$$
\finalanswer{Q = 0, \quad \boldsymbol{p} = qd \boldsymbol{e}_z}
$$
となります。

極座標系において位置ベクトルと $z$ 軸のなす角を $\theta$ と置くと，内積は $\boldsymbol{p} \cdot \boldsymbol{r} = qd \, r\cos\theta$ となります。(2) の展開式に $Q=0$ とこの内積を代入すると，遠方でのポテンシャルは，
$$
\begin{aligned}
\phi(r, \theta) &= \frac{1}{4\pi\varepsilon_0} \frac{qd \, r\cos\theta}{r^3} \\
&= \finalanswer{\phi(r, \theta) = \frac{qd\cos\theta}{4\pi\varepsilon_0 r^2}}
\end{aligned}
$$
となります。

===== FILE: 09vector_analysis/07/07_010.md =====
---
tags:
  - 基本
---

# ラプラシアンの計算

## 問題
3次元空間のラプラシアン $\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$ に関して，以下の問いに答えよ。

(1) 直交座標系において，スカラー関数 $f(x, y, z) = x^2 + 2y^2 - 3z^2$ のラプラシアン $\nabla^2 f$ を求めよ。

(2) 原点からの距離 $r = \sqrt{x^2+y^2+z^2}$ の関数 $f(r)$ について，連鎖律を用いて勾配が
$$
\nabla f(r) = \frac{f'(r)}{r} \boldsymbol{r}
$$
と表されることを示せ。ただし $f'(r) = \frac{df}{dr}$，$\boldsymbol{r} = x\boldsymbol{e}_x + y\boldsymbol{e}_y + z\boldsymbol{e}_z$ とする。

(3) 球対称な関数 $f(r)$ に対するラプラシアンが
$$
\nabla^2 f(r) = f''(r) + \frac{2}{r}f'(r)
$$
となることを示し，これを用いて $f(r) = r^n$（$n$ は定数，$r>0$）のラプラシアン $\nabla^2 (r^n)$ を求めよ。

---

## 解答・解説

### (1)
関数 $f(x, y, z) = x^2 + 2y^2 - 3z^2$ を各変数で2階偏微分します。
$$
\begin{aligned}
\frac{\partial^2 f}{\partial x^2} &= \frac{\partial}{\partial x}(2x) = 2 \\
\frac{\partial^2 f}{\partial y^2} &= \frac{\partial}{\partial y}(4y) = 4 \\
\frac{\partial^2 f}{\partial z^2} &= \frac{\partial}{\partial z}(-6z) = -6
\end{aligned}
$$
となります。定義に従ってこれらを足し合わせると，
$$
\begin{aligned}
\nabla^2 f &= 2 + 4 + (-6) \\
&= \finalanswer{\nabla^2 f = 0}
\end{aligned}
$$
が得られます。ラプラシアンが恒等的に $0$ となるこのような関数は調和関数と呼ばれます。

### (2)
距離 $r = \sqrt{x^2+y^2+z^2}$ の $x$ に関する偏微分を計算すると，
$$
\frac{\partial r}{\partial x} = \frac{\partial}{\partial x}\left( x^2+y^2+z^2 \right)^{1/2} = \frac{1}{2}\left( x^2+y^2+z^2 \right)^{-1/2} \cdot 2x = \frac{x}{r}
$$
となります。同様に $\frac{\partial r}{\partial y} = \frac{y}{r}$，$\frac{\partial r}{\partial z} = \frac{z}{r}$ が成り立ちます。合成関数の微分法を用いると，
$$
\frac{\partial f(r)}{\partial x} = \frac{df}{dr} \frac{\partial r}{\partial x} = f'(r) \frac{x}{r}
$$
が得られます。$y, z$ 成分についても同様に計算してベクトルとしてまとめると，
$$
\begin{aligned}
\nabla f(r) &= \frac{\partial f}{\partial x}\boldsymbol{e}_x + \frac{\partial f}{\partial y}\boldsymbol{e}_y + \frac{\partial f}{\partial z}\boldsymbol{e}_z \\
&= f'(r) \frac{x}{r}\boldsymbol{e}_x + f'(r) \frac{y}{r}\boldsymbol{e}_y + f'(r) \frac{z}{r}\boldsymbol{e}_z \\
&= \finalanswer{\nabla f(r) = \frac{f'(r)}{r} \boldsymbol{r}}
\end{aligned}
$$
が示されます。

### (3)
ラプラシアンは勾配の発散 $\nabla^2 f = \nabla \cdot (\nabla f)$ で定義されます。(2) で求めたベクトル場に対して発散の公式 $\nabla \cdot (g \boldsymbol{r}) = (\nabla g) \cdot \boldsymbol{r} + g (\nabla \cdot \boldsymbol{r})$ を適用します。ここで $g(r) = \frac{f'(r)}{r}$ と置くと，
$$
g'(r) = \frac{f''(r)r - f'(r)}{r^2} = \frac{f''(r)}{r} - \frac{f'(r)}{r^2}
$$
となります。(2) の結果を用いると $\nabla g(r) = \frac{g'(r)}{r}\boldsymbol{r}$ であり，また $\nabla \cdot \boldsymbol{r} = 3$ であることから，
$$
\begin{aligned}
\nabla^2 f(r) &= \nabla \cdot (g(r) \boldsymbol{r}) \\
&= \left( \frac{g'(r)}{r}\boldsymbol{r} \right) \cdot \boldsymbol{r} + 3 g(r) \\
&= g'(r) r + 3 g(r) \\
&= \left( f''(r) - \frac{f'(r)}{r} \right) + 3 \frac{f'(r)}{r} \\
&= f''(r) + \frac{2}{r}f'(r)
\end{aligned}
$$
が得られます。

次に $f(r) = r^n$ に対して導関数を求めると，
$$
f'(r) = n r^{n-1}, \quad f''(r) = n(n-1) r^{n-2}
$$
となります。これらを上の公式に代入すると，
$$
\begin{aligned}
\nabla^2 (r^n) &= n(n-1) r^{n-2} + \frac{2}{r} (n r^{n-1}) \\
&= \left[ n(n-1) + 2n \right] r^{n-2} \\
&= \finalanswer{\nabla^2 (r^n) = n(n+1) r^{n-2}}
\end{aligned}
$$
となります。特に $n = -1$ のとき，この式は $r \ne 0$ において $0$ になります。

===== FILE: 09vector_analysis/07/07_020.md =====
---
tags:
  - 標準
---

# パラメータ表示した曲面の面積分

## 問題
原点を中心とする半径 $R$ の球面 $S$ は，極座標の角度パラメータ $\theta$（$0 \le \theta \le \pi$）および $\phi$（$0 \le \phi \le 2\pi$）を用いて
$$
\boldsymbol{r}(\theta, \phi) = R\sin\theta\cos\phi \, \boldsymbol{e}_x + R\sin\theta\sin\phi \, \boldsymbol{e}_y + R\cos\theta \, \boldsymbol{e}_z
$$
と表される。以下の問いに答えよ。

(1) $\theta$ 方向および $\phi$ 方向の接ベクトル $\frac{\partial \boldsymbol{r}}{\partial \theta}$，$\frac{\partial \boldsymbol{r}}{\partial \phi}$ をそれぞれ求めよ。

(2) 法線ベクトル $\frac{\partial \boldsymbol{r}}{\partial \theta} \times \frac{\partial \boldsymbol{r}}{\partial \phi}$ を計算し，その大きさが $R^2 \sin\theta$ となることを示せ。

(3) ベクトル場 $\boldsymbol{A} = z \boldsymbol{e}_z$ の球面 $S$ 全体における外向きの面積分
$$
\int_S \boldsymbol{A} \cdot d\boldsymbol{S}
$$
を，パラメータ $\theta, \phi$ による重積分として計算せよ。ただし面素ベクトルは $d\boldsymbol{S} = \left( \frac{\partial \boldsymbol{r}}{\partial \theta} \times \frac{\partial \boldsymbol{r}}{\partial \phi} \right) d\theta d\phi$ とする。

---

## 解答・解説

### (1)
位置ベクトル $\boldsymbol{r}(\theta, \phi)$ の各成分をパラメータで偏微分します。$\theta$ について偏微分すると，
$$
\begin{aligned}
\frac{\partial \boldsymbol{r}}{\partial \theta} &= \frac{\partial}{\partial \theta}(R\sin\theta\cos\phi)\boldsymbol{e}_x + \frac{\partial}{\partial \theta}(R\sin\theta\sin\phi)\boldsymbol{e}_y + \frac{\partial}{\partial \theta}(R\cos\theta)\boldsymbol{e}_z \\
&= \finalanswer{\frac{\partial \boldsymbol{r}}{\partial \theta} = R\cos\theta\cos\phi \, \boldsymbol{e}_x + R\cos\theta\sin\phi \, \boldsymbol{e}_y - R\sin\theta \, \boldsymbol{e}_z}
\end{aligned}
$$
となります。同様に $\phi$ について偏微分すると，
$$
\begin{aligned}
\frac{\partial \boldsymbol{r}}{\partial \phi} &= \frac{\partial}{\partial \phi}(R\sin\theta\cos\phi)\boldsymbol{e}_x + \frac{\partial}{\partial \phi}(R\sin\theta\sin\phi)\boldsymbol{e}_y + \frac{\partial}{\partial \phi}(R\cos\theta)\boldsymbol{e}_z \\
&= \finalanswer{\frac{\partial \boldsymbol{r}}{\partial \phi} = -R\sin\theta\sin\phi \, \boldsymbol{e}_x + R\sin\theta\cos\phi \, \boldsymbol{e}_y}
\end{aligned}
$$
となります。

### (2)
(1) で求めた2つの接ベクトルの外積を成分ごとに計算します。
$$
\begin{aligned}
\frac{\partial \boldsymbol{r}}{\partial \theta} \times \frac{\partial \boldsymbol{r}}{\partial \phi} &= \begin{vmatrix} \boldsymbol{e}_x & \boldsymbol{e}_y & \boldsymbol{e}_z \\ R\cos\theta\cos\phi & R\cos\theta\sin\phi & -R\sin\theta \\ -R\sin\theta\sin\phi & R\sin\theta\cos\phi & 0 \end{vmatrix} \\
&= \left[ 0 - (-R^2\sin^2\theta\cos\phi) \right] \boldsymbol{e}_x + \left[ (-R^2\sin^2\theta\sin\phi) - 0 \right] \boldsymbol{e}_y \\
&\quad + \left[ R^2\sin\theta\cos\theta\cos^2\phi - (-R^2\sin\theta\cos\theta\sin^2\phi) \right] \boldsymbol{e}_z \\
&= R^2\sin^2\theta\cos\phi \, \boldsymbol{e}_x + R^2\sin^2\theta\sin\phi \, \boldsymbol{e}_y + R^2\sin\theta\cos\theta \, \boldsymbol{e}_z
\end{aligned}
$$
が得られます。共通因数 $R\sin\theta$ をくくり出すと，
$$
\frac{\partial \boldsymbol{r}}{\partial \theta} \times \frac{\partial \boldsymbol{r}}{\partial \phi} = R\sin\theta \, \boldsymbol{r}(\theta, \phi)
$$
と表されます。ベクトルの大きさを計算すると，$|\boldsymbol{r}| = R$ であり，積分範囲 $0 \le \theta \le \pi$ において $\sin\theta \ge 0$ であるため，
$$
\begin{aligned}
\left| \frac{\partial \boldsymbol{r}}{\partial \theta} \times \frac{\partial \boldsymbol{r}}{\partial \phi} \right| &= R\sin\theta |\boldsymbol{r}| \\
&= \finalanswer{\left| \frac{\partial \boldsymbol{r}}{\partial \theta} \times \frac{\partial \boldsymbol{r}}{\partial \phi} \right| = R^2\sin\theta}
\end{aligned}
$$
が示されます。これにより面素の面積が $dS = R^2\sin\theta \, d\theta d\phi$ となることが確認できます。

### (3)
球面上の各点においてベクトル場は $\boldsymbol{A} = z \boldsymbol{e}_z = R\cos\theta \, \boldsymbol{e}_z$ です。(2) で得られた法線ベクトルとの内積をとると，$z$ 成分のみが寄与するため，
$$
\begin{aligned}
\boldsymbol{A} \cdot \left( \frac{\partial \boldsymbol{r}}{\partial \theta} \times \frac{\partial \boldsymbol{r}}{\partial \phi} \right) &= (R\cos\theta)(R^2\sin\theta\cos\theta) \\
&= R^3 \sin\theta\cos^2\theta
\end{aligned}
$$
となります。したがって，求める面積分は重積分として，
$$
\begin{aligned}
\int_S \boldsymbol{A} \cdot d\boldsymbol{S} &= \int_0^{2\pi} d\phi \int_0^\pi d\theta \, R^3 \sin\theta\cos^2\theta \\
&= R^3 \left( \int_0^{2\pi} d\phi \right) \left( \int_0^\pi \cos^2\theta \sin\theta \, d\theta \right)
\end{aligned}
$$
と表されます。それぞれの定積分を計算します。$\theta$ の積分については $u = \cos\theta$（$du = -\sin\theta \, d\theta$）と置換すると，
$$
\int_0^\pi \cos^2\theta \sin\theta \, d\theta = \int_1^{-1} u^2 (-du) = \int_{-1}^1 u^2 \, du = \left[ \frac{1}{3}u^3 \right]_{-1}^1 = \frac{2}{3}
$$
となります。また $\phi$ の積分は $2\pi$ です。これらを掛け合わせると，
$$
\begin{aligned}
\int_S \boldsymbol{A} \cdot d\boldsymbol{S} &= R^3 \cdot 2\pi \cdot \frac{2}{3} \\
&= \finalanswer{\int_S \boldsymbol{A} \cdot d\boldsymbol{S} = \frac{4}{3}\pi R^3}
\end{aligned}
$$
となります。この値は，ガウスの発散定理により $\nabla \cdot \boldsymbol{A} = \frac{\partial z}{\partial z} = 1$ を球全体の体積で積分した結果と一致します。

===== FILE: 09vector_analysis/07/07_030.md =====
---
tags:
  - 基本
---

# 体積積分と重心

## 問題
一様な密度 $\rho_0$ を持つ半径 $R$ の中実な上半球領域
$$
V: x^2 + y^2 + z^2 \le R^2, \quad z \ge 0
$$
を考える。以下の問いに答えよ。

<!-- FIGURE problem: xyz 座標系において，xy 平面より上側（z >= 0）にある半径 R の上半球を描く。底面となる円板と球面部分の境界を示し，球座標の动径 r，極角 θ，方位角 φ を図示する。 -->

(1) 3次元球座標 $(r, \theta, \phi)$（$x=r\sin\theta\cos\phi$，$y=r\sin\theta\sin\phi$，$z=r\cos\theta$）における体積要素 $dV$ を示し，上半球の体積 $V$ を計算せよ。

(2) 領域の対称性から重心の $x$ 座標および $y$ 座標が $x_G = 0$，$y_G = 0$ となることを説明せよ。また重心の $z$ 座標 $z_G$ を体積積分を用いて定義する式を示せ。

(3) 体積積分 $\int_V z \, dV$ を計算し，上半球の重心の座標 $z_G$ を求めよ。

---

## 解答・解説

### (1)
球座標変換におけるヤコビアンの計算により，微小体積要素は
$$
dV = r^2\sin\theta \, dr d\theta d\phi
$$
となります。上半球領域 $V$ に対応する各変数の積分範囲は，
$$
0 \le r \le R, \quad 0 \le \theta \le \frac{\pi}{2}, \quad 0 \le \phi \le 2\pi
$$
です。体積 $V$ を求める積分を実行すると，
$$
\begin{aligned}
V &= \int_V dV \\
&= \left( \int_0^R r^2 \, dr \right) \left( \int_0^{\pi/2} \sin\theta \, d\theta \right) \left( \int_0^{2\pi} d\phi \right)
\end{aligned}
$$
となります。それぞれの定積分を計算すると，
$$
\int_0^R r^2 \, dr = \frac{R^3}{3}, \quad \int_0^{\pi/2} \sin\theta \, d\theta = [-\cos\theta]_0^{\pi/2} = 1, \quad \int_0^{2\pi} d\phi = 2\pi
$$
となります。したがって体積は，
$$
\finalanswer{V = \frac{2}{3}\pi R^3}
$$
となります。

### (2)
領域 $V$ は $xz$ 平面に関して対称（$y \to -y$ で不変）であり，被積分関数 $y$ は $y$ について奇関数です。同様に $yz$ 平面に関しても対称（$x \to -x$ で不変）であり，被積分関数 $x$ は奇関数です。そのため積分領域内で対称な点同士の寄与が打ち消し合い，
$$
\int_V x \, dV = 0, \quad \int_V y \, dV = 0
$$
となります。密度が一様であるため重心座標の定義式より直ちに $x_G = 0$，$y_G = 0$ が得られます。

重心の $z$ 座標 $z_G$ は，全体の質量に対する $z$ 方向の一次モーメントの比として，
$$
\finalanswer{z_G = \frac{1}{V}\int_V z \, dV}
$$
で定義されます。

### (3)
球座標における関係式 $z = r\cos\theta$ を代入して体積積分を計算します。
$$
\begin{aligned}
\int_V z \, dV &= \int_0^{2\pi} d\phi \int_0^{\pi/2} d\theta \int_0^R dr \, r^2\sin\theta (r\cos\theta) \\
&= \left( \int_0^R r^3 \, dr \right) \left( \int_0^{\pi/2} \sin\theta\cos\theta \, d\theta \right) \left( \int_0^{2\pi} d\phi \right)
\end{aligned}
$$
各定積分をそれぞれ計算します。
$$
\begin{aligned}
\int_0^R r^3 \, dr &= \left[ \frac{1}{4}r^4 \right]_0^R = \frac{R^4}{4} \\
\int_0^{\pi/2} \sin\theta\cos\theta \, d\theta &= \left[ \frac{1}{2}\sin^2\theta \right]_0^{\pi/2} = \frac{1}{2} \\
\int_0^{2\pi} d\phi &= 2\pi
\end{aligned}
$$
これらを掛け合わせることにより，
$$
\int_V z \, dV = \frac{R^4}{4} \cdot \frac{1}{2} \cdot 2\pi = \frac{\pi R^4}{4}
$$
が得られます。(2) の定義式に (1) で求めた体積 $V$ とこの値を代入すると，
$$
\begin{aligned}
z_G &= \frac{\frac{\pi R^4}{4}}{\frac{2}{3}\pi R^3} \\
&= \frac{1}{4} \cdot \frac{3}{2} R \\
&= \finalanswer{z_G = \frac{3}{8}R}
\end{aligned}
$$
となります。

===== FILE: 09vector_analysis/07/07_040.md =====
---
tags:
  - 標準
---

# 流体の渦度と循環

## 問題
2次元の理想流体の渦糸（点渦）が原点に存在するとき，周囲の流れの速度場 $\boldsymbol{v}$ は直交座標系において
$$
\boldsymbol{v} = -\frac{\Gamma}{2\pi} \frac{y}{x^2+y^2} \boldsymbol{e}_x + \frac{\Gamma}{2\pi} \frac{x}{x^2+y^2} \boldsymbol{e}_y
$$
で与えられる。ただし $\Gamma$ は渦の強さを表す正の定数である。以下の問いに答えよ。

(1) 原点以外の領域（$r = \sqrt{x^2+y^2} > 0$）において，渦度ベクトル $\boldsymbol{\omega} = \nabla \times \boldsymbol{v}$ を計算せよ。

(2) $xy$ 平面上において，原点を中心とする半径 $R$ の円周 $C$ を反時計回りに1周する閉経路とする。この経路に沿った循環
$$
\oint_C \boldsymbol{v} \cdot d\boldsymbol{r}
$$
を直接計算せよ。

(3) 原点を内部に含まない任意の滑らかな閉曲線 $C'$ に沿った循環 $\oint_{C'} \boldsymbol{v} \cdot d\boldsymbol{r}$ を，ストークスの定理を用いて求めよ。

---

## 解答・解説

### (1)
速度場は $z$ 成分を持たず，また $x$ と $y$ のみに依存するため，回転ベクトルの非零成分は $z$ 成分のみです。速度の各成分を $v_x = -\frac{\Gamma}{2\pi}\frac{y}{x^2+y^2}$，$v_y = \frac{\Gamma}{2\pi}\frac{x}{x^2+y^2}$ として計算します。商の微分法を用いると，
$$
\begin{aligned}
\frac{\partial v_y}{\partial x} &= \frac{\Gamma}{2\pi} \frac{1 \cdot (x^2+y^2) - x \cdot 2x}{(x^2+y^2)^2} = \frac{\Gamma}{2\pi} \frac{y^2 - x^2}{(x^2+y^2)^2} \\
\frac{\partial v_x}{\partial y} &= -\frac{\Gamma}{2\pi} \frac{1 \cdot (x^2+y^2) - y \cdot 2y}{(x^2+y^2)^2} = -\frac{\Gamma}{2\pi} \frac{x^2 - y^2}{(x^2+y^2)^2} = \frac{\Gamma}{2\pi} \frac{y^2 - x^2}{(x^2+y^2)^2}
\end{aligned}
$$
となります。したがって，回転の $z$ 成分は，
$$
\omega_z = \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} = 0
$$
となります。これより，原点以外の領域において，
$$
\finalanswer{\boldsymbol{\omega} = \boldsymbol{0}}
$$
が得られます。

### (2)
円周経路 $C$ を極座標の偏角 $\theta$（$0 \le \theta \le 2\pi$）を用いて媒介変数表示します。
$$
x = R\cos\theta, \quad y = R\sin\theta
$$
位置ベクトルの微分は，
$$
d\boldsymbol{r} = (-R\sin\theta \boldsymbol{e}_x + R\cos\theta \boldsymbol{e}_y) \, d\theta
$$
となります。経路 $C$ 上において $x^2+y^2 = R^2$ であるため，速度場は
$$
\boldsymbol{v} = \frac{\Gamma}{2\pi R} (-\sin\theta \boldsymbol{e}_x + \cos\theta \boldsymbol{e}_y)
$$
と表されます。線積分の被積分関数を計算すると，
$$
\begin{aligned}
\boldsymbol{v} \cdot d\boldsymbol{r} &= \frac{\Gamma}{2\pi R} \left[ (-R\sin\theta)(-\sin\theta) + (R\cos\theta)(\cos\theta) \right] d\theta \\
&= \frac{\Gamma}{2\pi} (\sin^2\theta + \cos^2\theta) \, d\theta \\
&= \frac{\Gamma}{2\pi} \, d\theta
\end{aligned}
$$
となります。これを $\theta$ について $0$ から $2\pi$ まで積分すると，
$$
\begin{aligned}
\oint_C \boldsymbol{v} \cdot d\boldsymbol{r} &= \int_0^{2\pi} \frac{\Gamma}{2\pi} \, d\theta \\
&= \finalanswer{\oint_C \boldsymbol{v} \cdot d\boldsymbol{r} = \Gamma}
\end{aligned}
$$
となります。循環は半径 $R$ によらず一定値 $\Gamma$ をとります。

### (3)
閉曲線 $C'$ が原点を含まないため，$C'$ を境界とする $xy$ 平面上の有界な領域 $S'$ の全体において速度場 $\boldsymbol{v}$ は滑らかであり特異点を持ちません。ストークスの定理を適用すると，
$$
\oint_{C'} \boldsymbol{v} \cdot d\boldsymbol{r} = \int_{S'} (\nabla \times \boldsymbol{v}) \cdot \boldsymbol{n} \, dS
$$
が成り立ちます。(1) より領域 $S'$ のすべての点において $\nabla \times \boldsymbol{v} = \boldsymbol{0}$ であるため，
$$
\begin{aligned}
\oint_{C'} \boldsymbol{v} \cdot d\boldsymbol{r} &= \int_{S'} \boldsymbol{0} \cdot \boldsymbol{n} \, dS \\
&= \finalanswer{\oint_{C'} \boldsymbol{v} \cdot d\boldsymbol{r} = 0}
\end{aligned}
$$
となります。

===== FILE: 09vector_analysis/07/07_050.md =====
---
tags:
  - 標準
---

# マクスウェル方程式の積分形と微分形

## 問題
電磁気学におけるマクスウェル方程式に関して，以下の問いに答えよ。

(1) 空間に固定された任意の開曲面 $S$ と，その向きづけられた境界曲線 $C$ に対するファラデーの電磁誘導の法則の積分形
$$
\oint_C \boldsymbol{E} \cdot d\boldsymbol{r} = - \frac{d}{dt} \int_S \boldsymbol{B} \cdot \boldsymbol{n} \, dS
$$
に対し，ストークスの定理を適用して微分形
$$
\nabla \times \boldsymbol{E} = - \frac{\partial \boldsymbol{B}}{\partial t}
$$
を導け。

(2) 変位電流を含むアンペール・マクスウェルの法則の微分形
$$
\nabla \times \boldsymbol{H} = \boldsymbol{j} + \frac{\partial \boldsymbol{D}}{\partial t}
$$
にストークスの定理を適用し，対応する積分形の法則を導け。

(3) (1) で導いたファラデーの法則の微分形の両辺の発散をとることにより，磁束密度に対するガウスの法則 $\nabla \cdot \boldsymbol{B} = 0$ と両立する時間微分に関する関係式を導け。

---

## 解答・解説

### (1)
左辺の線積分に対してストークスの定理を適用すると，
$$
\oint_C \boldsymbol{E} \cdot d\boldsymbol{r} = \int_S (\nabla \times \boldsymbol{E}) \cdot \boldsymbol{n} \, dS
$$
となります。右辺においては曲面 $S$ が空間に固定されているため，時間微分を積分の内部に入れて偏微分に置き換えることができます。
$$
-\frac{d}{dt} \int_S \boldsymbol{B} \cdot \boldsymbol{n} \, dS = - \int_S \frac{\partial \boldsymbol{B}}{\partial t} \cdot \boldsymbol{n} \, dS
$$
これらにより，すべての項を左辺に集めると，
$$
\int_S \left( \nabla \times \boldsymbol{E} + \frac{\partial \boldsymbol{B}}{\partial t} \right) \cdot \boldsymbol{n} \, dS = 0
$$
が得られます。この等式は任意の曲面 $S$ および任意の法線方向 $\boldsymbol{n}$ に対して成立するため，被積分関数のベクトル自体が恒等的に $\boldsymbol{0}$ でなければなりません。したがって，
$$
\finalanswer{\nabla \times \boldsymbol{E} = - \frac{\partial \boldsymbol{B}}{\partial t}}
$$
が導かれます。

### (2)
任意の開曲面 $S$ に対し，微分形方程式の両辺と単位法線ベクトル $\boldsymbol{n}$ の内積をとり，曲面全体で積分します。
$$
\int_S (\nabla \times \boldsymbol{H}) \cdot \boldsymbol{n} \, dS = \int_S \left( \boldsymbol{j} + \frac{\partial \boldsymbol{D}}{\partial t} \right) \cdot \boldsymbol{n} \, dS
$$
左辺の面積分に対してストークスの定理を適用すると，境界曲線 $C$ に沿った線積分に変換されます。
$$
\int_S (\nabla \times \boldsymbol{H}) \cdot \boldsymbol{n} \, dS = \oint_C \boldsymbol{H} \cdot d\boldsymbol{r}
$$
これらを結ぶことにより，積分形の法則として，
$$
\finalanswer{\oint_C \boldsymbol{H} \cdot d\boldsymbol{r} = \int_S \left( \boldsymbol{j} + \frac{\partial \boldsymbol{D}}{\partial t} \right) \cdot \boldsymbol{n} \, dS}
$$
が得られます。

### (3)
ファラデーの法則の微分形の両辺に対して発散をとります。
$$
\nabla \cdot (\nabla \times \boldsymbol{E}) = \nabla \cdot \left( - \frac{\partial \boldsymbol{B}}{\partial t} \right)
$$
ベクトル解析の恒等式より，任意のベクトル場の回転の発散は恒等的に $0$ です。すなわち左辺は $\nabla \cdot (\nabla \times \boldsymbol{E}) = 0$ となります。右辺については空間微分と時間微分の順序を入れ替えると，
$$
- \frac{\partial}{\partial t} (\nabla \cdot \boldsymbol{B}) = 0
$$
が得られます。両辺に $-1$ を掛けることにより，
$$
\finalanswer{\frac{\partial}{\partial t}(\nabla \cdot \boldsymbol{B}) = 0}
$$
が導かれます。この結果は，ある初期時刻で磁気単極子が存在せず $\nabla \cdot \boldsymbol{B} = 0$ であれば，その後のすべての時刻においても $\nabla \cdot \boldsymbol{B} = 0$ が保たれることを示しています。

===== FILE: 09vector_analysis/07/07_060.md =====
---
tags:
  - 標準
---

# ポインティングの定理の導出

## 問題
電磁場の局所的エネルギー保存則（ポインティングの定理）に関して，以下の問いに答えよ。

(1) 任意の滑らかな2つのベクトル場 $\boldsymbol{E}$，$\boldsymbol{H}$ に対し，ベクトル解析の恒等式
$$
\nabla \cdot (\boldsymbol{E} \times \boldsymbol{H}) = \boldsymbol{H} \cdot (\nabla \times \boldsymbol{E}) - \boldsymbol{E} \cdot (\nabla \times \boldsymbol{H})
$$
が成り立つことを直交座標の成分を用いて示せ。

(2) 真空中におけるマクスウェル方程式
$$
\nabla \times \boldsymbol{E} = -\mu_0 \frac{\partial \boldsymbol{H}}{\partial t}, \quad \nabla \times \boldsymbol{H} = \boldsymbol{j} + \varepsilon_0 \frac{\partial \boldsymbol{E}}{\partial t}
$$
を (1) の恒等式に代入せよ。電磁場のエネルギー密度 $u = \frac{1}{2}\varepsilon_0 E^2 + \frac{1}{2}\mu_0 H^2$ およびポインティングベクトル $\boldsymbol{S} = \boldsymbol{E} \times \boldsymbol{H}$ を用いて，局所的エネルギー保存則
$$
\frac{\partial u}{\partial t} + \nabla \cdot \boldsymbol{S} = -\boldsymbol{j} \cdot \boldsymbol{E}
$$
を導け。

(3) (2) の微分形の保存則を任意の有界領域 $V$ で体積積分し，ガウスの発散定理を適用して積分形のエネルギー保存則を導け。

---

## 解答・解説

### (1)
外積の各成分は，
$$
(\boldsymbol{E} \times \boldsymbol{H})_x = E_y H_z - E_z H_y
$$
$$
(\boldsymbol{E} \times \boldsymbol{H})_y = E_z H_x - E_x H_z
$$
$$
(\boldsymbol{E} \times \boldsymbol{H})_z = E_x H_y - E_y H_x
$$
で与えられます。この発散をとると，
$$
\begin{aligned}
\nabla \cdot (\boldsymbol{E} \times \boldsymbol{H}) &= \frac{\partial}{\partial x}(E_y H_z - E_z H_y) + \frac{\partial}{\partial y}(E_z H_x - E_x H_z) + \frac{\partial}{\partial z}(E_x H_y - E_y H_x) \\
&= \left( \frac{\partial E_y}{\partial x} H_z + E_y \frac{\partial H_z}{\partial x} - \frac{\partial E_z}{\partial x} H_y - E_z \frac{\partial H_y}{\partial x} \right) \\
&\quad + \left( \frac{\partial E_z}{\partial y} H_x + E_z \frac{\partial H_x}{\partial y} - \frac{\partial E_x}{\partial y} H_z - E_x \frac{\partial H_z}{\partial y} \right) \\
&\quad + \left( \frac{\partial E_x}{\partial z} H_y + E_x \frac{\partial H_y}{\partial z} - \frac{\partial E_y}{\partial z} H_x - E_y \frac{\partial H_x}{\partial z} \right)
\end{aligned}
$$
となります。この項を $H_x, H_y, H_z$ でくくった部分と，$-E_x, -E_y, -E_z$ でくくった部分に再整理します。
$$
\begin{aligned}
\nabla \cdot (\boldsymbol{E} \times \boldsymbol{H}) &= H_x \left( \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} \right) + H_y \left( \frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x} \right) + H_z \left( \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} \right) \\
&\quad - E_x \left( \frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z} \right) - E_y \left( \frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x} \right) - E_z \left( \frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y} \right)
\end{aligned}
$$
回転ベクトルの定義を用いると，
$$
\finalanswer{\nabla \cdot (\boldsymbol{E} \times \boldsymbol{H}) = \boldsymbol{H} \cdot (\nabla \times \boldsymbol{E}) - \boldsymbol{E} \cdot (\nabla \times \boldsymbol{H})}
$$
が示されます。

### (2)
(1) の恒等式の右辺にマクスウェル方程式を代入します。
$$
\begin{aligned}
\nabla \cdot (\boldsymbol{E} \times \boldsymbol{H}) &= \boldsymbol{H} \cdot \left( -\mu_0 \frac{\partial \boldsymbol{H}}{\partial t} \right) - \boldsymbol{E} \cdot \left( \boldsymbol{j} + \varepsilon_0 \frac{\partial \boldsymbol{E}}{\partial t} \right) \\
&= -\mu_0 \boldsymbol{H} \cdot \frac{\partial \boldsymbol{H}}{\partial t} - \varepsilon_0 \boldsymbol{E} \cdot \frac{\partial \boldsymbol{E}}{\partial t} - \boldsymbol{j} \cdot \boldsymbol{E}
\end{aligned}
$$
時間微分の連鎖律を用いると，
$$
\mu_0 \boldsymbol{H} \cdot \frac{\partial \boldsymbol{H}}{\partial t} = \frac{\partial}{\partial t}\left( \frac{1}{2}\mu_0 H^2 \right), \quad \varepsilon_0 \boldsymbol{E} \cdot \frac{\partial \boldsymbol{E}}{\partial t} = \frac{\partial}{\partial t}\left( \frac{1}{2}\varepsilon_0 E^2 \right)
$$
となります。したがって，エネルギー密度の定義 $u = \frac{1}{2}\varepsilon_0 E^2 + \frac{1}{2}\mu_0 H^2$ を用いると，
$$
\nabla \cdot (\boldsymbol{E} \times \boldsymbol{H}) = -\frac{\partial u}{\partial t} - \boldsymbol{j} \cdot \boldsymbol{E}
$$
となります。ポインティングベクトル $\boldsymbol{S} = \boldsymbol{E} \times \boldsymbol{H}$ を代入して項を移行すると，
$$
\finalanswer{\frac{\partial u}{\partial t} + \nabla \cdot \boldsymbol{S} = -\boldsymbol{j} \cdot \boldsymbol{E}}
$$
が得られます。

### (3)
(2) の等式の各項を領域 $V$ で体積積分します。
$$
\int_V \frac{\partial u}{\partial t} \, dV + \int_V \nabla \cdot \boldsymbol{S} \, dV = - \int_V \boldsymbol{j} \cdot \boldsymbol{E} \, dV
$$
第1項は領域が時間変化しないことから全エネルギーの時間変化率 $-\frac{d}{dt}\int_V u \, dV$ としてまとめられます。第2項に対してガウスの発散定理を適用すると，境界面 $S_b$ を通過する面積分になります。項を移行して整理すると，
$$
\finalanswer{-\frac{d}{dt}\int_V u \, dV = \int_{S_b} \boldsymbol{S} \cdot \boldsymbol{n} \, dS + \int_V \boldsymbol{j} \cdot \boldsymbol{E} \, dV}
$$
が得られます。これは，領域内の電磁場エネルギーの減少率が，境界面から流出する放射エネルギーフラックスと，電場が荷電粒子系に対して行う仕事率（ジュール熱など）の和に等しいことを示しています。

===== FILE: 09vector_analysis/07/07_070.md =====
---
tags:
  - 発展
---

# 応力テンソルの入口

## 問題
連続体力学において，媒質内部の微小な面素 $d\boldsymbol{S} = \boldsymbol{n} dS$（$\boldsymbol{n}$ は単位法線ベクトル）に作用する単位面積あたりの力（トラクションベクトル）を $\boldsymbol{t}$ とする。この力は2階の応力テンソル $T$ を用いて $\boldsymbol{t} = T \boldsymbol{n}$，すなわち成分表示では
$$
t_i = \sum_{j=1}^3 T_{ij} n_j \quad (i = 1, 2, 3)
$$
と表される。以下の問いに答えよ。

(1) 静止流体のように，あらゆる方向の面に垂直かつ内向きに一定の静水圧 $p$ が加わっている状態を考える。このときの応力テンソルが
$$
T_{ij} = -p \, \delta_{ij}
$$
（$\delta_{ij}$ はクロネッカーのデルタ）と表されるとき，任意の単位法線ベクトル $\boldsymbol{n}$ を持つ面に働くトラクションベクトル $\boldsymbol{t}$ を求めよ。

(2) 閉曲面 $S$ で囲まれた領域 $V$ に作用する全表面力 $\boldsymbol{F}_S = \int_S \boldsymbol{t} \, dS$ の各成分 $F_{S, i} = \int_S \sum_{j=1}^3 T_{ij} n_j \, dS$ に対し，ガウスの発散定理を適用して体積積分で表せ。

(3) (1) の静止流体の圧力分布 $p(\boldsymbol{r})$ が空間的に一様でない場合について，(2) の結果を用いて全表面力 $\boldsymbol{F}_S$ を圧力の勾配 $\nabla p$ の体積積分として表せ。

---

## 解答・解説

### (1)
トラクションベクトルの各成分の定義式に $T_{ij} = -p \, \delta_{ij}$ を代入します。
$$
\begin{aligned}
t_i &= \sum_{j=1}^3 (-p \, \delta_{ij}) n_j \\
&= -p \sum_{j=1}^3 \delta_{ij} n_j \\
&= -p n_i
\end{aligned}
$$
となります。これをベクトル形式にまとめると，
$$
\finalanswer{\boldsymbol{t} = -p \boldsymbol{n}}
$$
となります。この式は，面に対して垂直（法線方向）かつ領域の内側へ押し込む向きに大きさ $p$ の圧力が作用することを示しています。

### (2)
表面力の第 $i$ 成分を表す面積分において，固定された添字 $i$ に対してベクトル場 $\boldsymbol{A}^{(i)}$ を
$$
\boldsymbol{A}^{(i)} = (T_{i1}, T_{i2}, T_{i3})
$$
と定義します。すると被積分関数は $\sum_{j=1}^3 T_{ij} n_j = \boldsymbol{A}^{(i)} \cdot \boldsymbol{n}$ と内積の形になります。これにガウスの発散定理を適用すると，
$$
\begin{aligned}
F_{S, i} &= \int_S \boldsymbol{A}^{(i)} \cdot \boldsymbol{n} \, dS \\
&= \int_V \nabla \cdot \boldsymbol{A}^{(i)} \, dV \\
&= \int_V \left( \sum_{j=1}^3 \frac{\partial T_{ij}}{\partial x_j} \right) dV
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{F_{S, i} = \int_V \sum_{j=1}^3 \frac{\partial T_{ij}}{\partial x_j} \, dV}
$$
が得られます。

### (3)
(1) で与えられた応力テンソル $T_{ij} = -p(\boldsymbol{r}) \, \delta_{ij}$ を (2) の体積積分の被積分関数に代入します。
$$
\begin{aligned}
\sum_{j=1}^3 \frac{\partial T_{ij}}{\partial x_j} &= \sum_{j=1}^3 \frac{\partial}{\partial x_j} (-p \, \delta_{ij}) \\
&= -\sum_{j=1}^3 \delta_{ij} \frac{\partial p}{\partial x_j} \\
&= -\frac{\partial p}{\partial x_i}
\end{aligned}
$$
となります。これはスカラー関数 $p$ の勾配ベクトル $\nabla p$ の第 $i$ 成分の符号を変えたものに一致します。3つの成分をベクトルとしてまとめると，
$$
\finalanswer{\boldsymbol{F}_S = - \int_V \nabla p \, dV}
$$
が得られます。重力場中で静水圧が $p(z) = p_0 - \rho g z$（$z$ 軸鉛直上向き）と分布している場合，$\nabla p = -\rho g \boldsymbol{e}_z$ となり，$\boldsymbol{F}_S = \rho g V \boldsymbol{e}_z$ となって流体の浮力を導く基礎方程式となります。

===== FILE: 09vector_analysis/07/07_080.md =====
---
tags:
  - 標準
---

# 曲面の法線と単位接ベクトル

## 問題
3次元空間内の半径 $R$ の円柱面 $S$ を考える。以下の問いに答えよ。

(1) 円柱面が陰関数
$$
F(x, y, z) = x^2 + y^2 - R^2 = 0
$$
で与えられているとき，勾配ベクトル $\nabla F$ を求め，曲面上の点 $(x, y, z)$ における外向きの単位法線ベクトル $\boldsymbol{n}$ を求めよ。

(2) この円柱面を円柱座標の偏角 $\phi$（$0 \le \phi \le 2\pi$）および高さ $z$ を用いて
$$
\boldsymbol{r}(\phi, z) = R\cos\phi \, \boldsymbol{e}_x + R\sin\phi \, \boldsymbol{e}_y + z \, \boldsymbol{e}_z
$$
と媒介変数表示する。2つの接ベクトル $\frac{\partial \boldsymbol{r}}{\partial \phi}$ および $\frac{\partial \boldsymbol{r}}{\partial z}$ を求めよ。

(3) 接ベクトルの外積 $\frac{\partial \boldsymbol{r}}{\partial \phi} \times \frac{\partial \boldsymbol{r}}{\partial z}$ を計算し，これが (1) で求めた単位法線ベクトル $\boldsymbol{n}$ と同じ向きを持つことを確かめよ。また，微小面積要素 $dS$ を $d\phi$ と $dz$ を用いて表せ。

---

## 解答・解説

### (1)
スカラー関数 $F(x, y, z) = x^2 + y^2 - R^2$ の勾配を計算します。
$$
\begin{aligned}
\nabla F &= \frac{\partial F}{\partial x}\boldsymbol{e}_x + \frac{\partial F}{\partial y}\boldsymbol{e}_y + \frac{\partial F}{\partial z}\boldsymbol{e}_z \\
&= 2x \boldsymbol{e}_x + 2y \boldsymbol{e}_y
\end{aligned}
$$
となります。曲面上の点では $x^2+y^2=R^2$ であるため，このベクトルの大きさは，
$$
|\nabla F| = \sqrt{(2x)^2 + (2y)^2} = \sqrt{4(x^2+y^2)} = \sqrt{4R^2} = 2R
$$
となります。外向き単位法線ベクトルは勾配ベクトルをその大きさで割ることにより，
$$
\begin{aligned}
\boldsymbol{n} &= \frac{\nabla F}{|\nabla F|} \\
&= \frac{2x \boldsymbol{e}_x + 2y \boldsymbol{e}_y}{2R} \\
&= \finalanswer{\boldsymbol{n} = \frac{x}{R}\boldsymbol{e}_x + \frac{y}{R}\boldsymbol{e}_y}
\end{aligned}
$$
となります。

### (2)
位置ベクトル $\boldsymbol{r}(\phi, z)$ を各パラメータで偏微分して接ベクトルを求めます。$\phi$ で偏微分すると，
$$
\begin{aligned}
\frac{\partial \boldsymbol{r}}{\partial \phi} &= \frac{\partial}{\partial \phi}(R\cos\phi)\boldsymbol{e}_x + \frac{\partial}{\partial \phi}(R\sin\phi)\boldsymbol{e}_y + \frac{\partial}{\partial \phi}(z)\boldsymbol{e}_z \\
&= \finalanswer{\frac{\partial \boldsymbol{r}}{\partial \phi} = -R\sin\phi \, \boldsymbol{e}_x + R\cos\phi \, \boldsymbol{e}_y}
\end{aligned}
$$
となります。同様に $z$ で偏微分すると，
$$
\begin{aligned}
\frac{\partial \boldsymbol{r}}{\partial z} &= \frac{\partial}{\partial z}(R\cos\phi)\boldsymbol{e}_x + \frac{\partial}{\partial z}(R\sin\phi)\boldsymbol{e}_y + \frac{\partial}{\partial z}(z)\boldsymbol{e}_z \\
&= \finalanswer{\frac{\partial \boldsymbol{r}}{\partial z} = \boldsymbol{e}_z}
\end{aligned}
$$
となります。

### (3)
(2) で求めた2つの接ベクトルの外積を計算します。
$$
\begin{aligned}
\frac{\partial \boldsymbol{r}}{\partial \phi} \times \frac{\partial \boldsymbol{r}}{\partial z} &= \begin{vmatrix} \boldsymbol{e}_x & \boldsymbol{e}_y & \boldsymbol{e}_z \\ -R\sin\phi & R\cos\phi & 0 \\ 0 & 0 & 1 \end{vmatrix} \\
&= (R\cos\phi - 0)\boldsymbol{e}_x - (-R\sin\phi - 0)\boldsymbol{e}_y + 0\boldsymbol{e}_z \\
&= R\cos\phi \, \boldsymbol{e}_x + R\sin\phi \, \boldsymbol{e}_y
\end{aligned}
$$
となります。円柱面上の直交座標との関係 $x = R\cos\phi$，$y = R\sin\phi$ を用いると，
$$
\frac{\partial \boldsymbol{r}}{\partial \phi} \times \frac{\partial \boldsymbol{r}}{\partial z} = R \left( \frac{x}{R}\boldsymbol{e}_x + \frac{y}{R}\boldsymbol{e}_y \right) = R \boldsymbol{n}
$$
と表されます。$R > 0$ であるため，このベクトルは (1) で求めた外向き単位法線ベクトル $\boldsymbol{n}$ と同じ向きを持ちます。

微小面積要素 $dS$ はこの外積ベクトルの大きさに微小変化量 $d\phi dz$ を掛けたものであるため，
$$
\begin{aligned}
dS &= \left| \frac{\partial \boldsymbol{r}}{\partial \phi} \times \frac{\partial \boldsymbol{r}}{\partial z} \right| d\phi dz \\
&= \finalanswer{dS = R \, d\phi dz}
\end{aligned}
$$
となります。

===== FILE: 09vector_analysis/07/07_090.md =====
---
tags:
  - 標準
---

# 立体角と点電荷のフラックス

## 問題
原点に置かれた電荷 $q$ が空間の点 $\boldsymbol{r}$ に作る電場は
$$
\boldsymbol{E}(\boldsymbol{r}) = \frac{q}{4\pi\varepsilon_0} \frac{\boldsymbol{r}}{r^3}
$$
で与えられる。原点から見た微小面素 $d\boldsymbol{S} = \boldsymbol{n} dS$ の立体角は
$$
d\Omega = \frac{\boldsymbol{r} \cdot d\boldsymbol{S}}{r^3}
$$
と定義される。以下の問いに答えよ。

<!-- FIGURE problem: 原点 O に点電荷 q が置かれている。原点の外側に描かれた閉曲面 S_out と，原点を内部に包む閉曲面 S_in を並べて描く。それぞれの閉曲面から微小面素 dS と法線ベクトル n を取り出し，原点から張られる微小立体角 dΩ の錐状の立体角領域を描く。 -->

(1) 電場の微小フラックス $d\Phi = \boldsymbol{E} \cdot d\boldsymbol{S}$ を微小立体角 $d\Omega$ を用いて表せ。

(2) 原点を内部に含まない滑らかな閉曲面 $S_{\text{out}}$ を考える。この閉曲面を通過する全フラックス
$$
\Phi_{\text{out}} = \oint_{S_{\text{out}}} \boldsymbol{E} \cdot d\boldsymbol{S}
$$
が $0$ となることを，ガウスの発散定理を用いて示せ。

(3) 原点を内部に含む滑らかな閉曲面 $S_{\text{in}}$ を考える。全フラックス $\Phi_{\text{in}} = \oint_{S_{\text{in}}} \boldsymbol{E} \cdot d\boldsymbol{S}$ を求めよ。また，閉曲面全体が張る立体角 $\oint_{S_{\text{in}}} d\Omega$ を求めよ。

---

## 解答・解説

### (1)
電場の定義式を微小フラックスの式に代入します。
$$
\begin{aligned}
d\Phi &= \boldsymbol{E} \cdot d\boldsymbol{S} \\
&= \left( \frac{q}{4\pi\varepsilon_0} \frac{\boldsymbol{r}}{r^3} \right) \cdot d\boldsymbol{S} \\
&= \frac{q}{4\pi\varepsilon_0} \left( \frac{\boldsymbol{r} \cdot d\boldsymbol{S}}{r^3} \right)
\end{aligned}
$$
となります。ここで立体角の定義式 $d\Omega = \frac{\boldsymbol{r} \cdot d\boldsymbol{S}}{r^3}$ を代入すると，
$$
\finalanswer{d\Phi = \frac{q}{4\pi\varepsilon_0} \, d\Omega}
$$
となります。この関係式は，電場のフラックスが幾何学的な立体角に比例することを示しています。

### (2)
閉曲面 $S_{\text{out}}$ が囲む体積領域を $V_{\text{out}}$ とします。原点は $V_{\text{out}}$ の外部にあるため，領域 $V_{\text{out}}$ のすべての点において $r \ne 0$ です。この領域全体で電場 $\boldsymbol{E}$ は滑らかであり，発散を計算すると，
$$
\nabla \cdot \boldsymbol{E} = \frac{q}{4\pi\varepsilon_0} \nabla \cdot \left(\frac{\boldsymbol{r}}{r^3}\right) = 0
$$
となります。したがって，ガウスの発散定理を適用すると，
$$
\begin{aligned}
\Phi_{\text{out}} &= \oint_{S_{\text{out}}} \boldsymbol{E} \cdot d\boldsymbol{S} \\
&= \int_{V_{\text{out}}} \nabla \cdot \boldsymbol{E} \, dV \\
&= \int_{V_{\text{out}}} 0 \, dV \\
&= \finalanswer{\Phi_{\text{out}} = 0}
\end{aligned}
$$
が示されます。

### (3)
原点を中心とする十分小さな半径 $R$ の球面 $S_R$ を閉曲面 $S_{\text{in}}$ の内部にとります。曲面 $S_{\text{in}}$ と $S_R$ で挟まれた領域には原点が含まれないため，(2) と同様に発散定理を用いることで全フラックスは球面 $S_R$ 上の積分に帰着されます。
$$
\oint_{S_{\text{in}}} \boldsymbol{E} \cdot d\boldsymbol{S} = \oint_{S_R} \boldsymbol{E} \cdot \boldsymbol{n} \, dS
$$
半径 $R$ の球面上では電場の大きさは $\frac{q}{4\pi\varepsilon_0 R^2}$ で法線方向を向き，球面の表面積は $4\pi R^2$ です。したがって全フラックスは，
$$
\Phi_{\text{in}} = \frac{q}{4\pi\varepsilon_0 R^2} \cdot 4\pi R^2 = \finalanswer{\Phi_{\text{in}} = \frac{q}{\varepsilon_0}}
$$
となります。

次に，(1) で求めた関係式 $d\Phi = \frac{q}{4\pi\varepsilon_0} d\Omega$ を閉曲面全体で積分します。
$$
\oint_{S_{\text{in}}} d\Phi = \frac{q}{4\pi\varepsilon_0} \oint_{S_{\text{in}}} d\Omega
$$
左辺の値は求めた全フラックス $\Phi_{\text{in}} = \frac{q}{\varepsilon_0}$ であるため，
$$
\frac{q}{\varepsilon_0} = \frac{q}{4\pi\varepsilon_0} \oint_{S_{\text{in}}} d\Omega
$$
が成り立ちます。両辺を $\frac{q}{4\pi\varepsilon_0}$ で割ることにより，
$$
\finalanswer{\oint_{S_{\text{in}}} d\Omega = 4\pi}
$$
が得られます。内側に点源を含む閉曲面全体の立体角は，閉曲面の形状によらず常に全立体角 $4\pi$ となります。

===== END =====