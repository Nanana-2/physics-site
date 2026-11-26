---
title: 東大理物 平成16年度 物理学 第4問：中心力場の散乱とスイングバイ加速の原理
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成16年度
exam_subject: 物理学
exam_number: 第4問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成16年度 物理学 第4問：中心力場の散乱とスイングバイ加速の原理

## 問題

宇宙探査機は燃料の不足を補うため，しばしばスイングバイという航法で加速を行うことがある。（例えばアポロ13号は月の重力を，火星探査機のぞみは地球の重力を使って加速した。）中心力場の力学からこの原理について考える。
{: .problem-lead }

(1) 2次元の極座標系 $(r, \phi)$ を用いて中心力ポテンシャル $U(r)$ 中を運動する質量 $m$ の質点の Lagrangian を書き，Euler-Lagrange の方程式を用いて角運動量の保存則を導け。

(2) 図1のように質量 $m$ の探査機が質量 $M$ の惑星に対して距離 $b$ の漸近線 $SS'$ に沿って無限遠方から速さ $v$ で進入し，漸近線 $TT'$ に沿って出てゆくものとする。ただし，$M \gg m$ の関係があり，惑星は静止しているとみなしてよい。惑星の位置を原点とし，探査機の座標を $(r, \phi)$ とするとき次式が成り立つことを示せ。

$$
\dot{\phi} = \frac{vb}{r^2} \tag{1}
$$

<figure class="problem-figure" markdown>
![惑星による探査機の重力散乱の幾何](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_4-p1-light.svg#only-light)
![惑星による探査機の重力散乱の幾何](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_4-p1-dark.svg#only-dark)
<figcaption markdown="span">図1：静止した惑星 $M$ のまわりの探査機 $m$ の双曲線軌道と漸近線 $SS', TT'$。</figcaption>
</figure>

(3) 探査機が惑星に最も近づいた時の惑星までの距離 $r_0$ を $v, b, M$ と重力定数 $G$ を用いて表わせ。ただし，ポテンシャル $U(r)$ は $U(r) = -\dfrac{GMm}{r}$ と表わされる。

(4) 探査機の $(x, y)$ 座標系における速度を $(v_x, v_y)$ とおくと，$v_x$ と $\phi$ の間に次の微分方程式が成立することを示せ。ただし，式 (1) を用いてよい。

$$
\mathrm{d}v_x = -\frac{GM}{vb}\cos\phi\,\mathrm{d}\phi \tag{2}
$$

(5) 入射前後における角度変化 $\theta$ が $\tan\dfrac{\theta}{2} = \dfrac{GM}{v^2 b}$ で表わされることを示せ。ただし，式 (2) を用いてよい。

(6) 図2のように惑星が速度ベクトル $\vec{W}$ で太陽に対して運動していたところへ探査機がやってきた。探査機の太陽に対する相対速度ベクトルが入射前は $\vec{v}$，出射後は $\vec{u}$ であったとして，惑星の運動量の変化を無視せずに，入射前後における探査機のエネルギー変化，$\dfrac{1}{2}m|\vec{u}|^2 - \dfrac{1}{2}m|\vec{v}|^2$ を求めよ。ただし，惑星の引力圏内では，太陽からの引力は無視できるものとする。

(7) 上の結果から探査機の加速が可能なことを示せ。また，増加した探査機のエネルギーはどこから来たか答えよ。

<figure class="problem-figure" markdown>
![太陽に対して運動する惑星によるスイングバイ](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_4-p2-light.svg#only-light)
![太陽に対して運動する惑星によるスイングバイ](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_4-p2-dark.svg#only-dark)
<figcaption markdown="span">図2：太陽に対して速度 $\vec{W}$ で運動する惑星と，入射速度 $\vec{v}$・出射速度 $\vec{u}$ で通過する探査機。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成16年度 物理学 第4問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，静止した惑星の重力場中での2次元極座標の運動を考えます。角運動量保存則と力学的エネルギー保存則を組み合わせることで，軌道方程式を直接解かずに最近接距離と散乱角を求めることができます。

後半では，太陽に対して速度 $\vec{W}$ で運動する惑星と探査機の2体系に運動量保存則とエネルギー保存則を立てます。出射後の惑星の速度を消去することで，惑星の反跳を含めた探査機の運動エネルギー変化が導かれます。
</div>

### (1)

2次元極座標 $(r, \phi)$ における質点の速度の2乗は $\dot{r}^2 + r^2\dot{\phi}^2$ なので，ラグランジアン $L$ は次式となります。

$$
L = \frac{1}{2}m\bigl(\dot{r}^2 + r^2\dot{\phi}^2\bigr) - U(r)
$$

座標 $\phi$ に関するオイラー・ラグランジュ方程式を立てます。

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{\phi}}\right) - \frac{\partial L}{\partial \phi} = 0
$$

ポテンシャル $U(r)$ は $\phi$ を含まないため $\dfrac{\partial L}{\partial \phi} = 0$ であり，$\dfrac{\partial L}{\partial \dot{\phi}} = m r^2\dot{\phi}$ です。これらを代入します。

$$
\frac{\mathrm{d}}{\mathrm{d}t}\bigl(m r^2\dot{\phi}\bigr) = 0
$$

したがって，角運動量 $\ell = m r^2\dot{\phi}$ は時間によらず一定であり，角運動量保存則が成り立ちます。

$$
\finalanswer{L = \frac{1}{2}m\bigl(\dot{r}^2 + r^2\dot{\phi}^2\bigr) - U(r), \qquad m r^2\dot{\phi} = \text{const.}}
$$

### (2)

図1において，探査機は無限遠方の漸近線 $SS'$ に沿って惑星 $M$ の上方から反時計回りの向きに進入します。漸近線 $SS'$ と原点 $M$ との垂直距離が衝突径数 $b$ なので，無限遠方での角運動量の大きさは $m v b$ であり，角度 $\phi$ が増加する向きに運動するため角運動量は正の値 $+m v b$ です。

設問 (1) の角運動量保存則より，軌道上の任意の点 $(r, \phi)$ において次式が成り立ちます。

$$
m r^2\dot{\phi} = m v b
$$

両辺を $m r^2$ で割ると，式 (1) が得られます。

$$
\dot{\phi} = \frac{vb}{r^2}
$$

### (3)

無限遠方では $r \to \infty$ で $U(r) \to 0$ であり，探査機の速さは $v$ なので，探査機の全エネルギーは $\dfrac{1}{2}m v^2$ です。

探査機が惑星に最も近づく点 $r = r_0$ では動径方向の速度が $\dot{r} = 0$ となり，式 (1) より $\dot{\phi} = \dfrac{vb}{r_0^2}$ なので，速さは $r_0\dot{\phi} = \dfrac{vb}{r_0}$ です。エネルギー保存則を立てます。

$$
\frac{1}{2}m\left(\frac{vb}{r_0}\right)^2 - \frac{GMm}{r_0} = \frac{1}{2}m v^2
$$

両辺に $\dfrac{2 r_0^2}{m v^2}$ を掛けて移項すると，$r_0$ に関する2次方程式になります。

$$
r_0^2 + \frac{2GM}{v^2}r_0 - b^2 = 0
$$

解の公式を用い，$r_0 > 0$ を満たす正の根を選びます。

$$
\finalanswer{r_0 = \sqrt{b^2 + \left(\frac{GM}{v^2}\right)^2} - \frac{GM}{v^2}}
$$

### (4)

位置ベクトル $\boldsymbol{r} = (r\cos\phi, r\sin\phi)$ にある探査機にはたらく万有引力の $x$ 成分は $F_x = -\dfrac{GMm}{r^2}\cos\phi$ です。$x$ 方向の運動方程式を立てます。

$$
m\frac{\mathrm{d}v_x}{\mathrm{d}t} = -\frac{GMm}{r^2}\cos\phi
$$

両辺を $m$ で割ります。

$$
\frac{\mathrm{d}v_x}{\mathrm{d}t} = -\frac{GM}{r^2}\cos\phi
$$

ここで式 (1) より $\dfrac{\mathrm{d}\phi}{\mathrm{d}t} = \dfrac{vb}{r^2}$ なので，合成関数の微分則から $\dfrac{\mathrm{d}v_x}{\mathrm{d}\phi}$ を求めます。

$$
\begin{aligned}
\frac{\mathrm{d}v_x}{\mathrm{d}\phi} &= \frac{\mathrm{d}v_x/\mathrm{d}t}{\mathrm{d}\phi/\mathrm{d}t} \\
&= \frac{-\dfrac{GM}{r^2}\cos\phi}{\dfrac{vb}{r^2}} \\
&= -\frac{GM}{vb}\cos\phi
\end{aligned}
$$

両辺に $\mathrm{d}\phi$ を掛けると，式 (2) が成り立つことがわかります。

$$
\mathrm{d}v_x = -\frac{GM}{vb}\cos\phi\,\mathrm{d}\phi
$$

### (5)

図1において，漸近線 $SS'$ と $TT'$ は $x$ 軸に対して対称であり，それぞれ $+x$ 軸となす角が $\alpha$ です。2つの漸近線の交点における角度の関係より，入射前後の角度変化 $\theta$ と $\alpha$ の間には $\theta + 2\alpha = \pi$，すなわち $\alpha = \dfrac{\pi - \theta}{2}$ が成り立ちます。

探査機は無限遠の $S$ 側から進入して惑星の左側を回り，$T'$ 側へ抜けるため，偏角 $\phi$ は $\phi = \alpha$ から $\phi = 2\pi - \alpha$ まで連続的に増加します。また，エネルギー保存則より出射後の無限遠での速さも $v$ に等しいため，入射前と出射後の速度の $x$ 成分はそれぞれ次式になります。

$$
v_{x,\mathrm{in}} = -v\cos\alpha, \qquad v_{x,\mathrm{out}} = v\cos\alpha
$$

式 (2) の両辺を $\phi = \alpha$ から $\phi = 2\pi - \alpha$ まで積分します。左辺の積分は速度の $x$ 成分の変化量です。

$$
\begin{aligned}
\int_{v_{x,\mathrm{in}}}^{v_{x,\mathrm{out}}} \mathrm{d}v_x &= v_{x,\mathrm{out}} - v_{x,\mathrm{in}} \\
&= 2v\cos\alpha
\end{aligned}
$$

右辺の積分を計算します。

$$
\begin{aligned}
-\frac{GM}{vb}\int_{\alpha}^{2\pi - \alpha} \cos\phi\,\mathrm{d}\phi &= -\frac{GM}{vb}\bigl[\sin\phi\bigr]_{\alpha}^{2\pi - \alpha} \\
&= -\frac{GM}{vb}\bigl(\sin(2\pi - \alpha) - \sin\alpha\bigr) \\
&= -\frac{GM}{vb}(-2\sin\alpha) \\
&= \frac{2GM}{vb}\sin\alpha
\end{aligned}
$$

左辺と右辺を等しいとおきます。

$$
2v\cos\alpha = \frac{2GM}{vb}\sin\alpha
$$

両辺を $2v\sin\alpha$ で割ります。

$$
\frac{\cos\alpha}{\sin\alpha} = \frac{GM}{v^2 b}
$$

ここで $\alpha = \dfrac{\pi}{2} - \dfrac{\theta}{2}$ を代入します。

$$
\begin{aligned}
\frac{\cos\alpha}{\sin\alpha} &= \cot\left(\frac{\pi}{2} - \frac{\theta}{2}\right) \\
&= \tan\frac{\theta}{2}
\end{aligned}
$$

したがって，次式が成り立ちます。

$$
\tan\frac{\theta}{2} = \frac{GM}{v^2 b}
$$

### (6)

出射後の惑星の太陽に対する速度ベクトルを $\vec{W}'$ とおきます。惑星の引力圏内では太陽からの引力を無視するため，探査機と惑星からなる2体系の全運動量と全エネルギーが保存します。まず運動量保存則を立てます。

$$
M\vec{W} + m\vec{v} = M\vec{W}' + m\vec{u}
$$

これを $\vec{W}'$ について解きます。

$$
\vec{W}' = \vec{W} - \frac{m}{M}(\vec{u} - \vec{v})
$$

次に，入射前と出射後の十分に離れた位置では万有引力によるポテンシャルエネルギーは $0$ とみなすことができるため，エネルギー保存則は次式になります。

$$
\frac{1}{2}M|\vec{W}|^2 + \frac{1}{2}m|\vec{v}|^2 = \frac{1}{2}M|\vec{W}'|^2 + \frac{1}{2}m|\vec{u}|^2
$$

探査機のエネルギー変化 $\Delta E = \dfrac{1}{2}m|\vec{u}|^2 - \dfrac{1}{2}m|\vec{v}|^2$ を惑星の運動エネルギー変化で表し，上で求めた $\vec{W}'$ を代入します。

$$
\begin{aligned}
\frac{1}{2}m|\vec{u}|^2 - \frac{1}{2}m|\vec{v}|^2 &= \frac{1}{2}M|\vec{W}|^2 - \frac{1}{2}M|\vec{W}'|^2 \\
&= \frac{1}{2}M|\vec{W}|^2 - \frac{1}{2}M\left|\vec{W} - \frac{m}{M}(\vec{u} - \vec{v})\right|^2 \\
&= \frac{1}{2}M|\vec{W}|^2 - \frac{1}{2}M\left(|\vec{W}|^2 - \frac{2m}{M}\vec{W}\cdot(\vec{u} - \vec{v}) + \frac{m^2}{M^2}|\vec{u} - \vec{v}|^2\right) \\
&= m\vec{W}\cdot(\vec{u} - \vec{v}) - \frac{m^2}{2M}|\vec{u} - \vec{v}|^2
\end{aligned}
$$

したがって，探査機のエネルギー変化は次式となります。

$$
\finalanswer{\frac{1}{2}m|\vec{u}|^2 - \frac{1}{2}m|\vec{v}|^2 = m\vec{W}\cdot(\vec{u} - \vec{v}) - \frac{m^2}{2M}|\vec{u} - \vec{v}|^2}
$$

### (7)

設問 (6) で得たエネルギー変化の式を次のようにまとめます。

$$
\frac{1}{2}m|\vec{u}|^2 - \frac{1}{2}m|\vec{v}|^2 = m(\vec{u} - \vec{v})\cdot\left(\vec{W} - \frac{m}{2M}(\vec{u} - \vec{v})\right)
$$

探査機が惑星による重力散乱で進行方向を曲げられ，速度変化 $\vec{u} - \vec{v}$ が惑星の進行方向 $\vec{W}$ と正の内積をもつ軌道を選べば，$\vec{W}\cdot(\vec{u} - \vec{v}) > \dfrac{m}{2M}|\vec{u} - \vec{v}|^2$ を満たすことができます。実際，図2のように惑星の進行方向 $\vec{W}$ に対して後方側を回り込む軌道をとると，$\vec{u} - \vec{v}$ は $\vec{W}$ とほぼ同じ向きになり，特に $M \gg m$ のもとでは第2項 $-\dfrac{m^2}{2M}|\vec{u} - \vec{v}|^2$ が第1項に比べて十分小さいため，$\Delta E \simeq m\vec{W}\cdot(\vec{u} - \vec{v}) > 0$ となって探査機を加速することができます。

また，設問 (6) のエネルギー保存則より

$$
\frac{1}{2}m|\vec{u}|^2 - \frac{1}{2}m|\vec{v}|^2 = -\left(\frac{1}{2}M|\vec{W}'|^2 - \frac{1}{2}M|\vec{W}|^2\right)
$$

が成り立っています。したがって，増加した探査機の運動エネルギーは，惑星の太陽に対する運動エネルギーがわずかに減少することで供給されたものです。
