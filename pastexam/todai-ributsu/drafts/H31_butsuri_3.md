---
title: 東大理物 平成31年度 物理学 第3問：連星系の重力波放射と軌道減衰
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成31年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成31年度 物理学 第3問：連星系の重力波放射と軌道減衰

## 問題

質量 $m_1,\ m_2$ をもつ二つの質点が互いの重力によって束縛運動している系を考える。それらの位置ベクトルをそれぞれ $\boldsymbol{r}_1,\ \boldsymbol{r}_2$ とし，相対位置ベクトルを $\boldsymbol{r} \equiv \boldsymbol{r}_2 - \boldsymbol{r}_1$ と定義する。軌道面上での $\boldsymbol{r}$ の2次元極座標表示 $(r, \varphi)$ を用いると，系のラグランジアンは

$$
\mathcal{L} = \frac{1}{2}\mu\left(\frac{dr}{dt}\right)^2 + \frac{1}{2}\mu r^2\left(\frac{d\varphi}{dt}\right)^2 + \frac{G\mu M}{r} \tag{1}
$$

となる。ここで，$G$ はニュートンの重力定数である。また，$M$ と $\mu$ は以下で定義される。

$$
M = m_1 + m_2,\qquad \mu = \frac{m_1 m_2}{m_1 + m_2}. \tag{2}
$$

この系に関する以下の設問に答えよ。なお，設問5と6は，それ以外の設問と独立に解くことができる。

(1) 式 (1) のラグランジアンを用いて，$r$ と $\varphi$ に対する運動方程式を求めよ。

(2) この系のエネルギー $E$ の表式，および $\varphi$ に共役な運動量 $J$ の表式を求めよ。

(3) $E$ と $J$ が運動の定数であることを示せ。

一般相対論によれば，この系から重力波が放射されることで，$E$ は保存せず徐々に減少する。以下では，重力波の放射の影響を考慮した場合の系の運動を，一般相対論ではなくニュートン力学を用いて近似的に取り扱う。さらに，任意の時刻 $t$ における軌道が半径 $a = a(t)$ の円軌道で近似できる場合を考え，その時刻でのエネルギー $E = E(t)$ が
{: .problem-lead }

$$
E = -\frac{G\mu M}{2a} \tag{3}
$$

と書けることを用いてよい。また重力波の放射に伴う $\mu$ と $M$ の変化は無視できるものとする。

(4) 半径 $a$ の円軌道の場合，この系からの重力波による単位時間あたりのエネルギー放射率は，$c$ を光速として，

$$
L_{\mathrm{GW}} = \frac{32 G^4}{5 c^5}\frac{\mu^2 M^3}{a^5} \tag{4}
$$

で与えられる。したがって，系の運動をニュートン力学で近似した場合には

$$
\frac{dE}{dt} = -L_{\mathrm{GW}} \tag{5}
$$

が成り立つ。式 (5) を $a$ に対する微分方程式に書き直せ。

(5) ケプラーの法則を用いれば，設問4の結果は公転周期 $P$ に対する次の微分方程式

$$
\frac{dP}{dt} = -A\left(\frac{P_{\mathrm{c}}}{P}\right)^{5/3} \tag{6}
$$

に書き換えられる。ここで，$A$ は無次元の数係数，$P_{\mathrm{c}}$ は時間の次元をもつ定数で，それらは設問6で具体的に計算する。ここでは，式 (6) を解いて，初期条件として公転周期 $P_0$ をもつ2質点系が，合体する（すなわち $P = 0$）までの時間 $\tau_{\mathrm{GW}}$ を，$A,\ P_{\mathrm{c}}$ および $P_0$ を用いて表せ。

(6) ケプラーの方程式

$$
G M P^2 = 4\pi^2 a^3 \tag{7}
$$

を用いて式 (6) を導き，$P_{\mathrm{c}} = G\mu^\alpha M^\beta c^\gamma$ とした時のべき指数 $\alpha, \beta, \gamma$ の値と $A$ の表式を求めよ。

(7) 2015年に，連星ブラックホール GW150914 からの重力波信号が直接検出された。地上で重力波の信号が検出され始めた時点での連星ブラックホールの公転周期は $P_0 \approx 0.06\ \mathrm{sec}$ であった。この連星ブラックホールは，それから $\tau_{\mathrm{GW}} \approx 0.15\ \mathrm{sec}$ 後に，重力波放射によって合体した。簡単のために，この連星は等質量 $m$ の2つのブラックホールからなり，また合体直前までニュートン力学近似が正しいものと仮定する。設問5と6の結果を利用することで，$m$ が太陽質量 $M_\odot$ の何倍であるかを概算せよ。$A$ の近似値を $2500$ とし，必要であれば $2GM_\odot/c^3 \approx 10^{-5}\ \mathrm{sec},\ 6^{3/5} \approx 2.9,\ 2^{1/5} \approx 1.1$ を用いてよい。

(8) 連星ブラックホールの公転周期が $P_0$ のときの公転半径を $a_0$ とする。それ以降，重力波放射に伴い $a$ は徐々に減少するが，やがてある長さ $a_{\min}$ 以下になると，上述のニュートン力学的な2質点の運動という描像が破綻する。これは物理的には，ブラックホールはその質量に対応した特徴的な長さスケールをもち，$a = 0$ になる以前に2つのブラックホールが実効的に合体するためである。GW150914 の場合，合体までに放射される重力波によって，設問7で得られた質量 $m$ の約一割に相当するエネルギーが系から失われたと考えられている。このとき，$a_{\min}$ と $m$ の関係式を導け。ただし簡単のために，$a_0 \gg a_{\min}$ と近似できるものとし，$a$ が $a_0$ から $a_{\min}$ になるまでは上述のニュートン力学近似が正しく，かつ $a$ が $a_{\min}$ になった後は重力波が放射されないものと仮定せよ。この設問においても，式 (3) における $\mu$ と $M$ の時間変化率は，$a$ の時間変化率に比べて小さく無視できるものとする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成31年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ラグランジアンは角度 $\varphi$ を含まず，時間にもあらわによらないので，角運動量とエネルギーが保存します。重力波の放射を考えると，エネルギーは与えられた割合で減っていきます。円軌道のエネルギーは半径 $a$ だけで書くことができるので，エネルギーの減り方から半径の減り方が求まります。

観測で直接わかるのは，軌道半径ではなく公転周期です。そこで，ケプラーの法則で半径を周期に書き換え，周期についての微分方程式にします。観測された周期と合体までの時間をこの式に入れると，星の質量を見積もることができます。
</div>

### (1)
ラグランジアン (1) の各偏微分を計算します。

$$
\begin{aligned}
\frac{\partial\mathcal{L}}{\partial r} &= \mu r\dot{\varphi}^2 - \frac{G\mu M}{r^2}, \qquad
\frac{\partial\mathcal{L}}{\partial\dot{r}} = \mu\dot{r} \\
\frac{\partial\mathcal{L}}{\partial\varphi} &= 0, \qquad
\frac{\partial\mathcal{L}}{\partial\dot{\varphi}} = \mu r^2\dot{\varphi}
\end{aligned}
$$

オイラー・ラグランジュ方程式 $\dfrac{\mathrm{d}}{\mathrm{d}t}\left(\dfrac{\partial\mathcal{L}}{\partial\dot{q}}\right) - \dfrac{\partial\mathcal{L}}{\partial q} = 0$ を $r$ と $\varphi$ について書きます。したがって，

$$
\finalanswer{\mu\frac{\mathrm{d}^2 r}{\mathrm{d}t^2} - \mu r\left(\frac{\mathrm{d}\varphi}{\mathrm{d}t}\right)^2 + \frac{G\mu M}{r^2} = 0,\qquad \frac{\mathrm{d}}{\mathrm{d}t}\left(\mu r^2\frac{\mathrm{d}\varphi}{\mathrm{d}t}\right) = 0}
$$

### (2)
$\varphi$ に共役な運動量 $J$ は角運動量です。系のエネルギーはハミルトニアンから求めます。

$$
\begin{aligned}
J&=\frac{\partial\mathcal L}{\partial\dot\varphi}\\
&=\mu r^2\dot\varphi\\
E&=\dot r\frac{\partial\mathcal L}{\partial\dot r}+\dot\varphi\frac{\partial\mathcal L}{\partial\dot\varphi}-\mathcal L\\
&=\mu\dot r^2+\mu r^2\dot\varphi^2-\mathcal L
\end{aligned}
$$

したがって，

$$
\finalanswer{E = \frac{1}{2}\mu\left(\frac{\mathrm{d}r}{\mathrm{d}t}\right)^2 + \frac{1}{2}\mu r^2\left(\frac{\mathrm{d}\varphi}{\mathrm{d}t}\right)^2 - \frac{G\mu M}{r},\qquad J = \mu r^2\frac{\mathrm{d}\varphi}{\mathrm{d}t}}
$$

### (3)
まず問1の $\varphi$ に関する運動方程式より，

$$
\begin{aligned}
\frac{\mathrm{d}J}{\mathrm{d}t} &= \frac{\mathrm{d}}{\mathrm{d}t}\left(\mu r^2\dot{\varphi}\right) \\
&= 0
\end{aligned}
$$

となるため，$J$ は運動の定数です。

次に $E$ を時間 $t$ で微分し，問1の2つの運動方程式を代入します。

$$
\begin{aligned}
\frac{\mathrm{d}E}{\mathrm{d}t} &= \mu\dot{r}\ddot{r} + \mu r\dot{r}\dot{\varphi}^2 + \mu r^2\dot{\varphi}\ddot{\varphi} + \frac{G\mu M}{r^2}\dot{r} \\
&= \dot{r}\left(\mu\ddot{r} - \mu r\dot{\varphi}^2 + \frac{G\mu M}{r^2}\right) + \dot{\varphi}\left(2\mu r\dot{r}\dot{\varphi} + \mu r^2\ddot{\varphi}\right) \\
&= \dot{r}\left(\mu\ddot{r} - \mu r\dot{\varphi}^2 + \frac{G\mu M}{r^2}\right) + \dot{\varphi}\frac{\mathrm{d}}{\mathrm{d}t}\left(\mu r^2\dot{\varphi}\right) \\
&= 0
\end{aligned}
$$

よって $E$ も運動の定数です。

### (4)
$\mu,M$ を定数として，式 (3) の $E=-\dfrac{G\mu M}{2a}$ を時間 $t$ で微分します。

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = \frac{G\mu M}{2a^2}\frac{\mathrm{d}a}{\mathrm{d}t}
$$

これを式 (4), (5) の $\dfrac{\mathrm{d}E}{\mathrm{d}t} = -\dfrac{32 G^4 \mu^2 M^3}{5 c^5 a^5}$ に代入して $\dfrac{\mathrm{d}a}{\mathrm{d}t}$ について解きます。

$$
\begin{aligned}
\frac{\mathrm{d}a}{\mathrm{d}t} &= -\frac{2a^2}{G\mu M}\cdot\frac{32 G^4 \mu^2 M^3}{5 c^5 a^5} \\
&= -\frac{64 G^3 \mu M^2}{5 c^5 a^3}
\end{aligned}
$$

したがって，

$$
\finalanswer{\frac{\mathrm{d}a}{\mathrm{d}t} = -\frac{64 G^3 \mu M^2}{5 c^5 a^3}}
$$

### (5)
式 (6) を変数分離します。初期条件を $P(0)=P_0$，合体時刻の条件を $P(\tau_{\mathrm{GW}})=0$ として積分します。

$$
\begin{aligned}
P^{5/3}\,\mathrm{d}P &= -A P_{\mathrm{c}}^{5/3}\,\mathrm{d}t \\
\int_{P_0}^{0} P^{5/3}\,\mathrm{d}P &= -A P_{\mathrm{c}}^{5/3}\int_{0}^{\tau_{\mathrm{GW}}} \mathrm{d}t \\
-\frac{3}{8}P_0^{8/3} &= -A P_{\mathrm{c}}^{5/3}\tau_{\mathrm{GW}}
\end{aligned}
$$

これを $\tau_{\mathrm{GW}}$ について解きます。したがって，

$$
\finalanswer{\tau_{\mathrm{GW}} = \frac{3}{8A}\frac{P_0^{8/3}}{P_{\mathrm{c}}^{5/3}} = \frac{3}{8A}P_0\left(\frac{P_0}{P_{\mathrm{c}}}\right)^{5/3}}
$$

### (6)
ケプラーの方程式 (7) $G M P^2 = 4\pi^2 a^3$ の両辺の対数微分をとると，

$$
\begin{aligned}
\frac{2}{P}\frac{\mathrm{d}P}{\mathrm{d}t} &= \frac{3}{a}\frac{\mathrm{d}a}{\mathrm{d}t} \\
\frac{\mathrm{d}P}{\mathrm{d}t} &= \frac{3P}{2a}\frac{\mathrm{d}a}{\mathrm{d}t}
\end{aligned}
$$

となります。これに問4の $\dfrac{\mathrm{d}a}{\mathrm{d}t}$ と式 (7) から得られる $a = \left(\dfrac{GM}{4\pi^2}\right)^{1/3} P^{2/3}$ を代入します。

$$
\begin{aligned}
\frac{\mathrm{d}P}{\mathrm{d}t}
&= \frac{3P}{2a}\left(-\frac{64 G^3 \mu M^2}{5 c^5 a^3}\right) \\
&= -\frac{96}{5}\frac{G^3 \mu M^2 P}{c^5 a^4} \\
&= -\frac{96}{5}\frac{G^3 \mu M^2 P}{c^5}\left(\frac{4\pi^2}{GM}\right)^{4/3} P^{-8/3} \\
&= -\frac{96}{5}(2\pi)^{8/3}\frac{G^{5/3}\mu M^{2/3}}{c^5 P^{5/3}} \\
&= -\frac{96}{5}(2\pi)^{8/3}\left(\frac{G\mu^{3/5}M^{2/5}c^{-3}}{P}\right)^{5/3}
\end{aligned}
$$

式 (6) および $P_{\mathrm{c}} = G\mu^\alpha M^\beta c^\gamma$ と比較すると，各定数が決まります。したがって，

$$
\finalanswer{\alpha = \frac{3}{5},\qquad \beta = \frac{2}{5},\qquad \gamma = -3,\qquad A = \frac{96}{5}(2\pi)^{8/3}}
$$

### (7)
問5の結果より $P_{\mathrm{c}}$ を $P_0,\ \tau_{\mathrm{GW}},\ A$ で表します。

$$
P_{\mathrm{c}} = P_0\left(\frac{3}{8A}\frac{P_0}{\tau_{\mathrm{GW}}}\right)^{3/5}
$$

与えられた数値 $P_0 \approx 0.06\ \mathrm{sec},\ \tau_{\mathrm{GW}} \approx 0.15\ \mathrm{sec},\ A \approx 2500$ を代入します。 $\dfrac{P_0}{\tau_{\mathrm{GW}}} = \dfrac{0.06}{0.15} = \dfrac{2}{5}$ より，

$$
\begin{aligned}
\frac{3}{8A}\frac{P_0}{\tau_{\mathrm{GW}}} &\approx \frac{3}{8\times 2500}\cdot\frac{2}{5} \\
&= \frac{6}{10^5} \\
&= 6\times 10^{-5} \\
P_{\mathrm{c}} &\approx \left(6\times 10^{-2}\ \mathrm{sec}\right)\left(6\times 10^{-5}\right)^{3/5} \\
&= 6\times 6^{3/5}\times 10^{-5}\ \mathrm{sec} \\
&\approx 6\times 2.9\times 10^{-5}\ \mathrm{sec} \\
&= 1.74\times 10^{-4}\ \mathrm{sec}
\end{aligned}
$$

一方，等質量 $m_1 = m_2 = m$ のとき $M = 2m,\ \mu = \dfrac{m}{2}$ なので，問6の $P_{\mathrm{c}}$ は次のようになります。

$$
\begin{aligned}
P_{\mathrm{c}} &= \frac{G}{c^3}\left(\frac{m}{2}\right)^{3/5}(2m)^{2/5} \\
&= 2^{-1/5}\frac{Gm}{c^3} \\
&= \frac{1}{2\cdot 2^{1/5}}\left(\frac{2GM_\odot}{c^3}\right)\frac{m}{M_\odot}
\end{aligned}
$$

これに $\dfrac{2GM_\odot}{c^3} \approx 10^{-5}\ \mathrm{sec},\ 2^{1/5} \approx 1.1$ を代入して $\dfrac{m}{M_\odot}$ を求めます。

$$
\begin{aligned}
\frac{m}{M_\odot} &\approx 2\times 1.1 \times \frac{1.74\times 10^{-4}}{10^{-5}} \\
&\approx 2.2 \times 17.4 \\
&\approx 38
\end{aligned}
$$

したがって，$m$ は太陽質量 $M_\odot$ のおよそ $38$ 倍です。有効数字1桁では約 $40$ 倍です。

$$
\finalanswer{\frac{m}{M_\odot} \approx 38}
$$

### (8)
公転半径が $a_0$ から $a_{\min}$ まで減少する間に重力波として放射される全エネルギー $\Delta E$ は，式 (3) と $a_0 \gg a_{\min}$ より次のように近似されます。

$$
\begin{aligned}
\Delta E &= E(a_0) - E(a_{\min}) \\
&= -\frac{G\mu M}{2a_0} - \left(-\frac{G\mu M}{2a_{\min}}\right) \\
&\simeq \frac{G\mu M}{2a_{\min}}
\end{aligned}
$$

等質量連星なので，

$$
\begin{aligned}
\mu M&=\frac m2\cdot2m\\
&=m^2
\end{aligned}
$$

です。放出されたエネルギーを，問題で指定された $mc^2/10$ と等しくおくと，

$$
\begin{aligned}
\frac{G m^2}{2 a_{\min}} &= \frac{1}{10}m c^2 \\
a_{\min} &= \frac{5 G m}{c^2}
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{a_{\min} = \frac{5 G m}{c^2}}
$$


