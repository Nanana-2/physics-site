===== FILE: 06solid_state/12/12_010.md =====
---
tags:
  - 発展
---

# ベリー位相

## 問題
スピン $1/2$ の粒子が磁場 $\boldsymbol{B}(t)$ の中に置かれている。磁場の向きを球座標の角度 $(\theta(t), \phi(t))$ で表し，ハミルトニアンを
$$
H(t) = -\mu \boldsymbol{B}(t) \cdot \boldsymbol{\sigma}
$$
とおく。ここで $\mu > 0$ は磁気モーメント，$\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ はパウリ行列である。磁場の大きさ $B = |\boldsymbol{B}|$ は一定とし，
$$
\boldsymbol{B}(t) = B (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)
$$
とする。エネルギー固有値 $-\mu B$ に属する規格化された固有状態を
$$
|-(t)\rangle = \begin{pmatrix} \cos\dfrac{\theta}{2} \\ \sin\dfrac{\theta}{2} e^{i\phi} \end{pmatrix}
$$
と選ぶ。角度の組 $\boldsymbol{R} = (\theta, \phi)$ が閉曲線 $C$ に沿って断熱的に1周するとき，状態ベクトルが得るベリー位相 $\gamma$ は，ベリー接続 $\boldsymbol{A} = (A_\theta, A_\phi)$ の線積分
$$
\gamma = \oint_C (A_\theta d\theta + A_\phi d\phi)
$$
で与えられる。ただし成分は $A_\theta = i \langle -(t) | \frac{\partial}{\partial \theta} |-(t)\rangle$ および $A_\phi = i \langle -(t) | \frac{\partial}{\partial \phi} |-(t)\rangle$ で定義される。以下の問いに答えよ。（図）

<!-- FIGURE problem: 原点から単位球面に向かって伸びる磁場ベクトル B の向きが，天頂角 θ と方位角 φ で指定されている様子。球面上に閉曲線 C が描かれている見取り図。 -->

(1) ベリー接続の成分 $A_\theta$ および $A_\phi$ を求めよ。

(2) 天頂角が $\theta = \theta_0$（一定）のまま，方位角 $\phi$ が $0$ から $2\pi$ まで1周するときのベリー位相 $\gamma$ を求めよ。

(3) 閉曲線 $C$ が囲む単位球面上の領域の立体角を $\Omega$ とする。ベリー位相 $\gamma$ を $\Omega$ を用いて表せ。

---

## 解答・解説

<div class="approach" markdown>
時間変化するパラメータに対する固有状態の微分からベリー接続の各成分を求めます。閉曲線に沿った線積分を実行し，得られた結果を球面上に張られる領域の面積（立体角）と結びつけます。
</div>

### (1)
固有状態 $|-(t)\rangle$ を天頂角 $\theta$ で偏微分します。
$$
\frac{\partial}{\partial \theta} |-(t)\rangle = \begin{pmatrix} -\frac{1}{2}\sin\frac{\theta}{2} \\ \frac{1}{2}\cos\frac{\theta}{2} e^{i\phi} \end{pmatrix}
$$
この式とブラベクトル $\langle -(t)| = (\cos\frac{\theta}{2}, \sin\frac{\theta}{2} e^{-i\phi})$ の内積を計算すると，
$$
\begin{aligned}
A_\theta &= i \left(-\frac{1}{2}\cos\frac{\theta}{2}\sin\frac{\theta}{2} + \frac{1}{2}\sin\frac{\theta}{2}\cos\frac{\theta}{2} e^{-i\phi} e^{i\phi}\right) \\
&= \finalanswer{A_\theta = 0}
\end{aligned}
$$
が得られます。

次に，方位角 $\phi$ で偏微分します。
$$
\frac{\partial}{\partial \phi} |-(t)\rangle = \begin{pmatrix} 0 \\ i \sin\frac{\theta}{2} e^{i\phi} \end{pmatrix}
$$
同様に内積を計算すると，
$$
\begin{aligned}
A_\phi &= i \left(\sin\frac{\theta}{2} e^{-i\phi} \cdot i \sin\frac{\theta}{2} e^{i\phi}\right) \\
&= -\sin^2\frac{\theta}{2} \\
&= \finalanswer{A_\phi = -\frac{1 - \cos\theta}{2}}
\end{aligned}
$$
となります。

### (2)
天頂角が $\theta = \theta_0$ で一定であるため，$d\theta = 0$ です。
線積分の経路に沿って $\phi$ を $0$ から $2\pi$ まで積分します。
$$
\begin{aligned}
\gamma &= \int_0^{2\pi} A_\phi d\phi \\
&= \int_0^{2\pi} \left(-\frac{1 - \cos\theta_0}{2}\right) d\phi \\
&= \finalanswer{\gamma = -\pi(1 - \cos\theta_0)}
\end{aligned}
$$
が得られます。

### (3)
天頂角が $0$ から $\theta_0$ まで，方位角が $0$ から $2\pi$ までの領域が張る立体角 $\Omega$ を計算します。
単位球面上の面積要素 $d\Omega = \sin\theta d\theta d\phi$ を積分すると，
$$
\begin{aligned}
\Omega &= \int_0^{2\pi} d\phi \int_0^{\theta_0} \sin\theta d\theta \\
&= 2\pi [-\cos\theta]_0^{\theta_0} \\
&= 2\pi(1 - \cos\theta_0)
\end{aligned}
$$
となります。
この立体角と (2) で求めたベリー位相を比較すると，
$$
\finalanswer{\gamma = -\frac{1}{2}\Omega}
$$
が得られます。
この関係式は任意の閉曲線に対しても成り立ち，ベリー位相が磁場の向きの描く立体角のみで決まることを表しています。

===== FILE: 06solid_state/12/12_020.md =====
---
tags:
  - 発展
---

# ベリー接続とベリー曲率

## 問題
3次元パラメータ空間のベクトル $\boldsymbol{d} = (d_x, d_y, d_z)$ に依存するハミルトニアン
$$
H(\boldsymbol{d}) = \boldsymbol{d} \cdot \boldsymbol{\sigma}
$$
を考える。ここで $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ はパウリ行列であり，$d = |\boldsymbol{d}| > 0$ とする。$\boldsymbol{d}$ を球座標
$$
\boldsymbol{d} = (d\sin\theta\cos\phi, d\sin\theta\sin\phi, d\cos\theta)
$$
で表したとき，固有値 $-d$ に属する規格化された固有状態を
$$
|-\rangle = \begin{pmatrix} \sin\dfrac{\theta}{2} \\ -\cos\dfrac{\theta}{2} e^{i\phi} \end{pmatrix}
$$
とおく。ベリー接続の極座標成分は $A_\theta = i \langle - | \frac{\partial}{\partial \theta} |-\rangle$ および $A_\phi = i \langle - | \frac{\partial}{\partial \phi} |-\rangle$ で定義される。以下の問いに答えよ。

(1) ベリー接続の成分 $A_\theta$ および $A_\phi$ を求めよ。

(2) ベリー曲率の成分 $F_{\theta\phi} = \frac{\partial A_\phi}{\partial \theta} - \frac{\partial A_\theta}{\partial \phi}$ を求めよ。

(3) $\boldsymbol{d}$ 空間におけるベクトル場としてのベリー曲率を $\boldsymbol{\Omega} = \Omega_d \boldsymbol{e}_d$ とする。単位球面上の面積要素 $d\boldsymbol{S} = \boldsymbol{e}_d d^2 \sin\theta d\theta d\phi$ を用いた関係式
$$
\boldsymbol{\Omega} \cdot d\boldsymbol{S} = F_{\theta\phi} d\theta d\phi
$$
を用いて，ベリー曲率ベクトル $\boldsymbol{\Omega}$ を $\boldsymbol{d}$ および $d$ を用いて表せ。

---

## 解答・解説

<div class="approach" markdown>
パラメータの微分から固有状態の内積を求めてベリー接続を導出し，その回転からベリー曲率を計算します。極座標での曲率成分をベクトルの面積分と対応づけることで，原点にある磁気単極子の場との類似性を導きます。
</div>

### (1)
固有状態 $|-\rangle$ を $\theta$ で偏微分します。
$$
\frac{\partial}{\partial \theta} |-\rangle = \begin{pmatrix} \frac{1}{2}\cos\frac{\theta}{2} \\ \frac{1}{2}\sin\frac{\theta}{2} e^{i\phi} \end{pmatrix}
$$
ブラベクトル $\langle -| = (\sin\frac{\theta}{2}, -\cos\frac{\theta}{2} e^{-i\phi})$ との内積を計算すると，
$$
\begin{aligned}
A_\theta &= i \left(\frac{1}{2}\sin\frac{\theta}{2}\cos\frac{\theta}{2} - \frac{1}{2}\cos\frac{\theta}{2}\sin\frac{\theta}{2}\right) \\
&= \finalanswer{A_\theta = 0}
\end{aligned}
$$
が得られます。

次に，$\phi$ で偏微分します。
$$
\frac{\partial}{\partial \phi} |-\rangle = \begin{pmatrix} 0 \\ -i \cos\frac{\theta}{2} e^{i\phi} \end{pmatrix}
$$
内積を計算すると，
$$
\begin{aligned}
A_\phi &= i \left(-\cos\frac{\theta}{2} e^{-i\phi} \cdot (-i)\cos\frac{\theta}{2} e^{i\phi}\right) \\
&= -\cos^2\frac{\theta}{2} \\
&= \finalanswer{A_\phi = -\frac{1 + \cos\theta}{2}}
\end{aligned}
$$
となります。

### (2)
ベリー曲率の定義式に (1) で求めた成分を代入します。$A_\theta = 0$ であり，$A_\phi$ は $\phi$ に依存しないため，
$$
\begin{aligned}
F_{\theta\phi} &= \frac{\partial}{\partial \theta}\left(-\frac{1 + \cos\theta}{2}\right) - 0 \\
&= \finalanswer{F_{\theta\phi} = \frac{1}{2}\sin\theta}
\end{aligned}
$$
が得られます。

### (3)
与えられた関係式に面積要素と (2) の結果を代入します。
$$
\Omega_d d^2 \sin\theta d\theta d\phi = \frac{1}{2}\sin\theta d\theta d\phi
$$
両辺を $d^2 \sin\theta d\theta d\phi$ で割ると，動径成分が求まります。
$$
\Omega_d = \frac{1}{2d^2}
$$
動径方向の単位ベクトルは $\boldsymbol{e}_d = \frac{\boldsymbol{d}}{d}$ であるため，ベリー曲率ベクトルは
$$
\begin{aligned}
\boldsymbol{\Omega} &= \Omega_d \boldsymbol{e}_d \\
&= \frac{1}{2d^2} \frac{\boldsymbol{d}}{d} \\
&= \finalanswer{\boldsymbol{\Omega} = \frac{\boldsymbol{d}}{2d^3}}
\end{aligned}
$$
となります。
この式は，$\boldsymbol{d}$ 空間の原点に強さ $1/2$ の磁気単極子が存在するときに生じる磁場と同じ形をしています。

===== FILE: 06solid_state/12/12_030.md =====
---
tags:
  - 発展
---

# SSH 模型のバンドと巻き付き数

## 問題
1つの単位胞に2つの副格子サイト A，B を含む1次元格子（格子定数を $a$ とする）を考える。単位胞内の飛び移り積分を $v > 0$，隣接する単位胞間の飛び移り積分を $w > 0$ とする（図）。ブロッホ基底におけるハミルトニアンは，波数を $k$（$-\pi/a \le k < \pi/a$）として，
$$
H(k) = \begin{pmatrix} 0 & v + w e^{-ika} \\ v + w e^{ika} & 0 \end{pmatrix}
$$
と表される。このハミルトニアンをパウリ行列を用いて $H(k) = d_x(k)\sigma_x + d_y(k)\sigma_y$ と表す。以下の問いに答えよ。

<!-- FIGURE problem: 1次元格子において副格子サイト A と B が交互に並んでいる構造。単位胞内の結合が v，単位胞をまたぐ結合が w で表され，単位胞の長さ a が示されている見取り図。 -->

(1) 成分 $d_x(k)$ および $d_y(k)$ を求め，エネルギー固有値 $E(k)$ を求めよ。

(2) 複素数 $z(k) = d_x(k) + i d_y(k)$ を導入する。$k$ が $-\pi/a$ から $\pi/a$ まで動くとき，複素平面上で $z(k)$ が描く軌跡の形状を答えよ。

(3) $k$ が $-\pi/a$ から $\pi/a$ まで動くとき，$z(k)$ が原点のまわりを反時計回りに回る回数（巻き付き数）$\nu$ を，$v > w$ の場合と $v < w$ の場合についてそれぞれ求めよ。

---

## 解答・解説

<div class="approach" markdown>
ハミルトニアンをパウリ行列で展開して2次元ベクトルと対応づけます。波数を動かしたときのベクトルの軌跡が原点を囲むかどうかに着目して，飛び移り積分の大小によるトポロジカルな相の違いを判別します。
</div>

### (1)
パウリ行列の定義を用いて展開式を行列表示します。
$$
d_x \sigma_x + d_y \sigma_y = \begin{pmatrix} 0 & d_x - i d_y \\ d_x + i d_y & 0 \end{pmatrix}
$$
この行列と $H(k)$ の非対角成分を比較すると，
$$
d_x(k) + i d_y(k) = v + w e^{ika} = (v + w\cos ka) + i w\sin ka
$$
が得られます。実部と虚部を分けることにより，各成分が決まります。
$$
\finalanswer{d_x(k) = v + w\cos ka}, \quad \finalanswer{d_y(k) = w\sin ka}
$$
エネルギー固有値は $E(k) = \pm \sqrt{d_x(k)^2 + d_y(k)^2}$ で与えられます。
$$
\begin{aligned}
E(k) &= \pm \sqrt{(v + w\cos ka)^2 + w^2\sin^2 ka} \\
&= \finalanswer{E(k) = \pm \sqrt{v^2 + w^2 + 2vw\cos ka}}
\end{aligned}
$$
が得られます。

### (2)
$z(k) = d_x(k) + i d_y(k)$ に (1) の結果を代入します。
$$
z(k) = v + w e^{ika}
$$
$k$ が $-\pi/a$ から $\pi/a$ まで変化するとき，位相 $ka$ は $-\pi$ から $\pi$ まで変化します。
したがって，複素平面上で描く軌跡は，
$$
\finalanswer{\text{点 } (v, 0) \text{ を中心とする半径 } w \text{ の円}}
$$
となります。

### (3)
円の中心は実軸上の点 $v > 0$ にあり，半径は $w > 0$ です。
原点が円の内部にあるか外部にあるかによって巻き付き数が決まります。

$v > w$ のとき，円周上の点はすべて実部が正の領域に存在し，原点は円の外部にあります。したがって，原点のまわりを回らないため，
$$
\finalanswer{\nu = 0}
$$
となります。

$v < w$ のとき，円は実軸と点 $v - w < 0$ および点 $v + w > 0$ で交わり，原点は円の内部に含まれます。反時計回りに1周するため，
$$
\finalanswer{\nu = 1}
$$
となります。
巻き付き数は飛び移り積分の大小関係によって整数値として定まり，ギャップが閉じない限り変化しない不変量となります。

===== FILE: 06solid_state/12/12_040.md =====
---
tags:
  - 発展
---

# SSH 模型の端状態

## 問題
半無限の1次元 SSH 鎖（単位胞 $n = 1, 2, 3, \dots$）を考える。各単位胞 $n$ に副格子サイト $\text{A}_n$ と $\text{B}_n$ があり，格子の左端は $\text{A}_1$ である。単位胞内の飛び移り積分を $v > 0$，単位胞間の飛び移り積分を $w > 0$ とする。状態ベクトルを
$$
|\psi\rangle = \sum_{n=1}^\infty (a_n |\text{A}_n\rangle + b_n |\text{B}_n\rangle)
$$
とおく。定常シュレーディンガー方程式 $H|\psi\rangle = E|\psi\rangle$ を各サイトの成分で書くと，
$$
\begin{aligned}
v b_n + w b_{n-1} &= E a_n \quad (n \ge 1, \text{ただし } b_0 = 0) \\
v a_n + w a_{n+1} &= E b_n \quad (n \ge 1)
\end{aligned}
$$
となる。ここでエネルギー $E = 0$ の解を考える。以下の問いに答えよ。

(1) すべての $n \ge 1$ について $b_n = 0$ としたとき，$a_n$ に対する漸化式を求めよ。

(2) (1) の漸化式を解き，$a_1$ を用いて $a_n$ を表せ。また，波動関数が境界に局在して規格化可能（$\sum_{n=1}^\infty |a_n|^2 < \infty$）となるための条件を $v$ と $w$ の不等式で答えよ。

(3) 規格化可能な条件が満たされるとき，振幅の絶対値 $|a_n|$ が単位胞 1 個進むごとに $e^{-a/\xi}$（$a$ は単位胞の長さ）の割合で減衰するとみなす。局在長 $\xi$ を $a, v, w$ を用いて表せ。

---

## 解答・解説

<div class="approach" markdown>
エネルギーがゼロのときに固有方程式が2つの副格子に分離することを利用します。漸化式を解いて波動関数の空間分布を求め，無限遠での収束条件から局在状態が現れる条件を導きます。
</div>

### (1)
与えられた連立方程式において $E = 0$ および $b_n = 0$ とおきます。
第1式は両辺が $0$ となり満たされます。
第2式に代入すると，
$$
v a_n + w a_{n+1} = 0
$$
が得られます。両辺を整理すると，
$$
\finalanswer{a_{n+1} = -\frac{v}{w} a_n}
$$
となります。

### (2)
(1) で得られた漸化式を繰り返し適用します。
$$
\begin{aligned}
a_n &= \left(-\frac{v}{w}\right) a_{n-1} \\
&= \left(-\frac{v}{w}\right)^2 a_{n-2} \\
&= \finalanswer{a_n = \left(-\frac{v}{w}\right)^{n-1} a_1}
\end{aligned}
$$
が得られます。
波動関数が規格化可能であるための条件は，二乗和が収束することです。
$$
\sum_{n=1}^\infty |a_n|^2 = |a_1|^2 \sum_{n=1}^\infty \left(\frac{v}{w}\right)^{2(n-1)} < \infty
$$
この無限等比級数の公比は $(v/w)^2$ です。公比が 1 より小さくなければならないため，
$$
\left(\frac{v}{w}\right)^2 < 1
$$
が成り立ちます。$v > 0, w > 0$ であることから，求める条件は
$$
\finalanswer{v < w}
$$
となります。

### (3)
振幅の絶対値は，
$$
|a_n| = |a_1| \left(\frac{v}{w}\right)^{n-1}
$$
と表されます。
左端からの距離を $x_n = (n-1)a$ とおくと，振幅の減衰は次のように表すことができます。
$$
|a_n| = |a_1| e^{-(n-1)a/\xi} = |a_1| \left(e^{-a/\xi}\right)^{n-1}
$$
両式の底を等しいとおきます。
$$
e^{-a/\xi} = \frac{v}{w}
$$
両辺の自然対数を取ります。
$$
-\frac{a}{\xi} = \ln\left(\frac{v}{w}\right) = -\ln\left(\frac{w}{v}\right)
$$
両辺を $\xi$ について解くと，
$$
\finalanswer{\xi = \frac{a}{\ln\left(\dfrac{w}{v}\right)}}
$$
が得られます。
$v$ が $w$ に近づくと局在長は発散し，端状態はバルク全体へ広がります。

===== FILE: 06solid_state/12/12_050.md =====
---
tags:
  - 発展
---

# 2次元の2バンド模型とチャーン数

## 問題
2次元正方格子（格子定数を $1$ とする）上の2バンドハミルトニアン
$$
H(\boldsymbol{k}) = \boldsymbol{d}(\boldsymbol{k}) \cdot \boldsymbol{\sigma}
$$
を考える。ここで $\boldsymbol{k} = (k_x, k_y)$（$-\pi \le k_x, k_y < \pi$）であり，
$$
\boldsymbol{d}(\boldsymbol{k}) = (\sin k_x, \sin k_y, m + \cos k_x + \cos k_y)
$$
である（$m$ は実数定数）。固有値は $E_\pm(\boldsymbol{k}) = \pm |\boldsymbol{d}(\boldsymbol{k})|$ である。占有バンドのチャーン数 $C$ は，単位ベクトル $\hat{\boldsymbol{d}}(\boldsymbol{k}) = \boldsymbol{d}(\boldsymbol{k})/|\boldsymbol{d}(\boldsymbol{k})|$ による写像度に対応する。以下の問いに答えよ。

(1) バンドギャップが閉じる（$|\boldsymbol{d}(\boldsymbol{k})| = 0$ となる）条件は $\sin k_x = 0$，$\sin k_y = 0$，および $m + \cos k_x + \cos k_y = 0$ である。ギャップが閉じる $m$ の値と，そのときの $\boldsymbol{k}$ をすべて求めよ。

(2) $|m| > 2$ のとき，$d_z(\boldsymbol{k})$ の符号がブリルアンゾーン全体で正（$m > 2$ のとき）または負（$m < -2$ のとき）で一定となることを示せ。また，$\hat{\boldsymbol{d}}(\boldsymbol{k})$ が単位球面の半球しか覆わないことから，$|m| > 2$ におけるチャーン数 $C$ を求めよ。

(3) チャーン数 $C$ は $\boldsymbol{d} = (0, 0, d_z)$ となる4つの高対称点 $\boldsymbol{k}_i$ における符号を用いて
$$
C = \frac{1}{2} \sum_{i} \operatorname{sgn}(\det J_i) \operatorname{sgn}(d_z(\boldsymbol{k}_i))
$$
と表される。ここで $J_i$ は高対称点における $(d_x, d_y)$ のヤコビ行列である。$-2 < m < 0$ および $0 < m < 2$ における $C$ をそれぞれ求めよ。

---

## 解答・解説

<div class="approach" markdown>
パラメータベクトルがゼロになる点を求めてトポロジカル相の境界を特定します。高対称点における局所的なベクトルの振る舞いとヤコビアンの符号の寄与を足し合わせることで，各領域のチャーン数を導きます。
</div>

### (1)
$-\pi \le k_x, k_y < \pi$ の範囲で $\sin k_x = 0$ かつ $\sin k_y = 0$ を満たす点は，$(0,0)$，$(\pi,0)$，$(0,\pi)$，$(\pi,\pi)$ の4点です。
それぞれの点について $m + \cos k_x + \cos k_y = 0$ に代入します。

$\boldsymbol{k} = (0,0)$ のとき，$\cos 0 + \cos 0 = 2$ であるため，$m + 2 = 0$ より $m = -2$ です。
$\boldsymbol{k} = (\pi,0)$ および $(0,\pi)$ のとき，$\cos\pi + \cos 0 = 0$ であるため，$m = 0$ です。
$\boldsymbol{k} = (\pi,\pi)$ のとき，$\cos\pi + \cos\pi = -2$ であるため，$m - 2 = 0$ より $m = 2$ です。
したがって，ギャップが閉じる条件は，
$$
\finalanswer{m = -2 \quad (\boldsymbol{k} = (0,0))}
$$
$$
\finalanswer{m = 0 \quad (\boldsymbol{k} = (\pi,0), (0,\pi))}
$$
$$
\finalanswer{m = 2 \quad (\boldsymbol{k} = (\pi,\pi))}
$$
となります。

### (2)
任意の $\boldsymbol{k}$ に対して $-2 \le \cos k_x + \cos k_y \le 2$ が成り立ちます。
$m > 2$ のとき，
$$
d_z(\boldsymbol{k}) = m + \cos k_x + \cos k_y \ge m - 2 > 0
$$
となり，常に正です。
$m < -2$ のとき，
$$
d_z(\boldsymbol{k}) = m + \cos k_x + \cos k_y \le m + 2 < 0
$$
となり，常に負です。
したがって，$\hat{\boldsymbol{d}}(\boldsymbol{k})$ の $z$ 成分は正または負のいずれかに限定され，単位球面の北半球または南半球のいずれか一方しか覆いません。球面の全体を覆うことができないため，巻き付き数はゼロとなります。
$$
\finalanswer{C = 0}
$$
が得られます。

### (3)
高対称点における $(d_x, d_y) = (\sin k_x, \sin k_y)$ のヤコビ行列を求めます。
$$
J = \begin{pmatrix} \cos k_x & 0 \\ 0 & \cos k_y \end{pmatrix}
$$
行列式は $\det J = \cos k_x \cos k_y$ です。各点での値は，
$\boldsymbol{k} = (0,0)$ で $\det J = (+1)(+1) = +1$，
$\boldsymbol{k} = (\pi,0)$ および $(0,\pi)$ で $\det J = (-1)(+1) = -1$，
$\boldsymbol{k} = (\pi,\pi)$ で $\det J = (-1)(-1) = +1$
となります。

$-2 < m < 0$ のとき，高対称点での $d_z$ の符号は，$(0,0)$ で正，他の3点で負となります。与えられた式に代入すると，
$$
\begin{aligned}
C &= \frac{1}{2} \left[ (+1)(+1) + (-1)(-1) + (-1)(-1) + (+1)(-1) \right] \\
&= \frac{1}{2} (1 + 1 + 1 - 1) \\
&= \finalanswer{C = 1}
\end{aligned}
$$
が得られます。

$0 < m < 2$ のとき，高対称点での $d_z$ の符号は，$(\pi,\pi)$ で負，他の3点で正となります。同様に代入すると，
$$
\begin{aligned}
C &= \frac{1}{2} \left[ (+1)(+1) + (-1)(+1) + (-1)(+1) + (+1)(-1) \right] \\
&= \frac{1}{2} (1 - 1 - 1 - 1) \\
&= \finalanswer{C = -1}
\end{aligned}
$$
となります。

===== FILE: 06solid_state/12/12_060.md =====
---
tags:
  - 発展
---

# 量子ホール効果とチャーン数

## 問題
一様な磁場 $B > 0$ が $z$ 方向に印加された面積 $S$ の2次元電子系を考える。電子（電荷 $-e$，$e > 0$）のランダウ準位のエネルギーは，非負の整数 $n$ を用いて
$$
E_n = \hbar \omega_c \left(n + \frac{1}{2}\right)
$$
である。ここで $\omega_c = eB/m$ はサイクロトロン振動数である。各ランダウ準位の軌道縮退度は $N_\Phi = eBS/h$ である。ホール伝導度 $\sigma_{xy}$ は，フェルミ準位以下の占有バンドのチャーン数の総和 $C$ を用いて
$$
\sigma_{xy} = \frac{e^2}{h} C
$$
で与えられる。以下の問いに答えよ。

(1) 電子密度を $n_e$ とする。占有率 $\nu = n_e S / N_\Phi$ がちょうど整数 $\nu_0$ であり，エネルギーの低い方から $\nu_0$ 個のランダウ準位が完全に満たされているとき，ホール伝導度を $\sigma_{xy} = - j_y / E_x$ の関係から古典論に従って導き，$e, h, \nu_0$ を用いて表せ。

(2) (1) の結果と与えられた式を比較して，完全に満ちた各ランダウ準位がもつチャーン数 $C_n$（各 $n$ に対する値）を求めよ。

(3) $y$ 方向に境界をもつ帯状の系において，境界の閉じ込めポテンシャル $V(y)$ により，下端（$y = 0$ 近傍）では $\frac{\partial V}{\partial y} < 0$，上端（$y = L_y$ 近傍）では $\frac{\partial V}{\partial y} > 0$ となっている。ランダウゲージにおける電子の群速度が $v_x = -\frac{1}{eB}\frac{\partial V}{\partial y}$ で与えられるとき，下端と上端を流れる端状態の群速度の符号（正または負）をそれぞれ答えよ。また，一方の端を流れる端状態の総数 $N_{\text{edge}}$ とチャーン数の総和 $C$ の関係を等式で表せ。

---

## 解答・解説

<div class="approach" markdown>
古典的なローレンツ力から導かれるホール伝導度とトポロジカルな表式を比較します。境界のポテンシャル勾配から端状態の運動方向を求め，バルクのチャーン数と境界を流れる状態の対応関係を明らかにします。
</div>

### (1)
電場 $\boldsymbol{E} = (E_x, 0, 0)$ と磁場 $\boldsymbol{B} = (0, 0, B)$ のもとでの電子の運動方程式を考えます。定常状態ではローレンツ力と電場による力が釣り合います。
$$
-e (\boldsymbol{E} + \boldsymbol{v} \times \boldsymbol{B}) = 0
$$
$x$ 成分を比較すると，ドリフト速度が得られます。
$$
-e (E_x + v_y B) = 0 \implies v_y = -\frac{E_x}{B}
$$
電流密度は $\boldsymbol{j} = -e n_e \boldsymbol{v}$ であるため，$y$ 方向の電流密度は
$$
j_y = -e n_e v_y = \frac{e n_e E_x}{B}
$$
となります。電子密度は $n_e = \nu_0 N_\Phi / S = \nu_0 eB/h$ と書けるため，代入すると，
$$
j_y = \frac{e (\nu_0 eB/h) E_x}{B} = \frac{\nu_0 e^2}{h} E_x
$$
が得られます。定義式 $\sigma_{xy} = -j_y / E_x$ に代入すると，符号を含めた大きさとして
$$
\finalanswer{\sigma_{xy} = \nu_0 \frac{e^2}{h}}
$$
が得られます。

### (2)
完全に満たされた $\nu_0$ 個のランダウ準位に対するチャーン数の総和は，各準位のチャーン数 $C_n$ の和です。
$$
C = \sum_{n=0}^{\nu_0 - 1} C_n
$$
量子ホール伝導度の式 $\sigma_{xy} = \frac{e^2}{h} C$ と (1) の結果を等しいとおきます。
$$
\frac{e^2}{h} C = \nu_0 \frac{e^2}{h} \implies C = \nu_0
$$
この等式は任意の正の整数 $\nu_0$ について成り立つため，各準位が担うチャーン数はすべて等しく，
$$
\finalanswer{C_n = 1}
$$
となります。

### (3)
群速度の式 $v_x = -\frac{1}{eB}\frac{\partial V}{\partial y}$ にポテンシャルの傾きの符号を代入します。
下端（$y = 0$ 近傍）では $\frac{\partial V}{\partial y} < 0$ であるため，
$$
v_x > 0 \quad (\finalanswer{\text{下端：正}})
$$
となります。
上端（$y = L_y$ 近傍）では $\frac{\partial V}{\partial y} > 0$ であるため，
$$
v_x < 0 \quad (\finalanswer{\text{上端：負}})
$$
となります。
各ランダウ準位は端でポテンシャルによりエネルギーが上昇し，フェルミ準位とそれぞれ 1 回ずつ交差します。したがって，一方の端を横切る端状態の数 $N_{\text{edge}}$ は満たされたランダウ準位の数 $\nu_0$ と一致し，チャーン数の総和 $C$ と等しくなります。
$$
\finalanswer{N_{\text{edge}} = C}
$$
が成り立ちます。
これをバルク・エッジ対応といいます。

===== FILE: 06solid_state/12/12_070.md =====
---
tags:
  - 発展
---

# トポロジカル絶縁体の表面状態

## 問題
3次元トポロジカル絶縁体の表面（$xy$ 平面）における2次元電子の有効ハミルトニアンは
$$
H = v (\sigma_x p_y - \sigma_y p_x)
$$
で与えられる。ここで $v > 0$ はフェルミ速度，$\boldsymbol{p} = (p_x, p_y)$ は2次元運動量，$\boldsymbol{\sigma} = (\sigma_x, \sigma_y)$ はパウリ行列である。運動量を極座標表示 $p_x = p \cos\theta, p_y = p \sin\theta$（$p > 0$）で表す。以下の問いに答えよ。

(1) ハミルトニアン $H$ のエネルギー固有値 $E_\pm(p)$ を求めよ。

(2) 正のエネルギー固有値 $E_+(p)$ に属する規格化された固有状態を求めよ。また，この状態におけるスピンの期待値ベクトル $\langle \boldsymbol{\sigma} \rangle = (\langle \sigma_x \rangle, \langle \sigma_y \rangle)$ を求め，運動量との内積 $\langle \boldsymbol{\sigma} \rangle \cdot \boldsymbol{p}$ を計算せよ。

(3) 運動量 $\boldsymbol{p}$（角度 $\theta$）をもつ正のエネルギー状態 $|+\rangle$ から，反対向きの運動量 $-\boldsymbol{p}$（角度 $\theta + \pi$）をもつ状態 $|+'\rangle$ への，非磁性不純物ポテンシャル $V_{\text{imp}} = V_0 I$（$V_0$ は定数，$I$ は $2\times 2$ の単位行列）による遷移振幅 $\langle +' | V_{\text{imp}} | + \rangle$ を計算せよ。

---

## 解答・解説

<div class="approach" markdown>
ディラック型のハミルトニアンを行列表示して固有値と固有状態を求めます。スピンの期待値が運動量と直交することを確認し，逆向きの運動量をもつ状態とのスピンの直交性から散乱振幅を評価します。
</div>

### (1)
運動量の極座標表示をハミルトニアンに代入します。
$$
H = v p (\sigma_x \sin\theta - \sigma_y \cos\theta)
$$
パウリ行列を行列表示で代入すると，
$$
H = v p \begin{pmatrix} 0 & \sin\theta + i\cos\theta \\ \sin\theta - i\cos\theta & 0 \end{pmatrix}
$$
が得られます。ここで $\sin\theta + i\cos\theta = i(\cos\theta - i\sin\theta) = i e^{-i\theta}$ であるため，
$$
H = vp \begin{pmatrix} 0 & i e^{-i\theta} \\ -i e^{i\theta} & 0 \end{pmatrix}
$$
となります。固有値を $E$ として特性方程式 $\det(H - E I) = 0$ を解きます。
$$
(-E)^2 - (vp)^2 (i e^{-i\theta})(-i e^{i\theta}) = 0 \implies E^2 - (vp)^2 = 0
$$
これより，エネルギー固有値は
$$
\finalanswer{E_\pm(p) = \pm vp}
$$
となります。

### (2)
$E_+(p) = vp$ に対する固有方程式を解きます。
$$
vp \begin{pmatrix} 0 & i e^{-i\theta} \\ -i e^{i\theta} & 0 \end{pmatrix} \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = vp \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}
$$
第1行より $i e^{-i\theta} u_2 = u_1$ が得られます。規格化条件 $|u_1|^2 + |u_2|^2 = 1$ を用いると，
$$
\finalanswer{|+\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i e^{i\theta} \end{pmatrix}}
$$
が得られます。

この状態におけるスピンの期待値を計算します。
$$
\begin{aligned}
\langle \sigma_x \rangle &= \frac{1}{2} \begin{pmatrix} 1 & i e^{-i\theta} \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ -i e^{i\theta} \end{pmatrix} \\
&= \frac{1}{2} (-i e^{i\theta} + i e^{-i\theta}) \\
&= \sin\theta
\end{aligned}
$$
同様に $y$ 成分を計算します。
$$
\begin{aligned}
\langle \sigma_y \rangle &= \frac{1}{2} \begin{pmatrix} 1 & i e^{-i\theta} \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 1 \\ -i e^{i\theta} \end{pmatrix} \\
&= \frac{1}{2} (-e^{i\theta} - e^{-i\theta}) \\
&= -\cos\theta
\end{aligned}
$$
したがって，期待値ベクトルは
$$
\finalanswer{\langle \boldsymbol{\sigma} \rangle = (\sin\theta, -\cos\theta)}
$$
となります。
運動量ベクトル $\boldsymbol{p} = (p\cos\theta, p\sin\theta)$ との内積を計算すると，
$$
\begin{aligned}
\langle \boldsymbol{\sigma} \rangle \cdot \boldsymbol{p} &= \sin\theta \cdot (p\cos\theta) + (-\cos\theta) \cdot (p\sin\theta) \\
&= \finalanswer{\langle \boldsymbol{\sigma} \rangle \cdot \boldsymbol{p} = 0}
\end{aligned}
$$
が得られます。
スピンの向きが運動量に対して常に直交しており，これをスピン・運動量ロッキングといいます。

### (3)
反対向きの運動量をもつ状態 $|+'\rangle$ は，角度を $\theta + \pi$ とおくことで得られます。
$e^{i(\theta + \pi)} = -e^{i\theta}$ であるため，
$$
|+'\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i e^{i\theta} \end{pmatrix}
$$
となります。ブラベクトルは $\langle +'| = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -i e^{-i\theta} \end{pmatrix}$ です。
不純物ポテンシャルによる遷移振幅を計算します。
$$
\begin{aligned}
\langle +' | V_{\text{imp}} | + \rangle &= V_0 \langle +' | + \rangle \\
&= \frac{V_0}{2} \begin{pmatrix} 1 & -i e^{-i\theta} \end{pmatrix} \begin{pmatrix} 1 \\ -i e^{i\theta} \end{pmatrix} \\
&= \frac{V_0}{2} \left[ 1 + (-i e^{-i\theta})(-i e^{i\theta}) \right] \\
&= \frac{V_0}{2} (1 - 1) \\
&= \finalanswer{\langle +' | V_{\text{imp}} | + \rangle = 0}
\end{aligned}
$$
となります。
スピンの向きが逆を向いているため，非磁性不純物による真後ろへの散乱（後方散乱）が完全に消えることがわかります。

===== END =====