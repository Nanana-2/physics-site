---
title: 東大理物 平成27年度 物理学 第3問：等速運動する荷電粒子がつくる電磁場とローレンツ変換
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成27年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成27年度 物理学 第3問：等速運動する荷電粒子がつくる電磁場とローレンツ変換

## 問題

Maxwell 方程式は，以下のように表される。

$$
\begin{aligned}
\nabla\cdot\boldsymbol{E} &= \frac{\rho}{\epsilon_0}, & \nabla\times\boldsymbol{E} &= -\frac{\partial\boldsymbol{B}}{\partial t}, \\
\nabla\cdot\boldsymbol{B} &= 0, & \frac{1}{\mu_0}\nabla\times\boldsymbol{B} &= \epsilon_0\frac{\partial\boldsymbol{E}}{\partial t} + \boldsymbol{i}
\end{aligned}
$$

ここで，$\boldsymbol{E},\ \boldsymbol{B}$ はそれぞれ電場と磁束密度，$\rho,\ \boldsymbol{i}$ はそれぞれ電荷密度および電流密度である。また，光速 $c$，真空誘電率 $\epsilon_0$，真空透磁率 $\mu_0$ の間には，$\epsilon_0\mu_0 = 1/c^2$ の関係が成り立つ。

まず，3次元直交座標系 $\mathcal{O}$ において，$z$ 軸上の $-\infty$ から $+\infty$ まで一定間隔で並べられた荷電粒子群が，$z$ 軸に沿って速度 $\boldsymbol{v} = (0, 0, v_z)$ で等速運動している系を考える。ここで，各荷電粒子は電荷 $q$ を持ち，その間隔は座標系 $\mathcal{O}$ において $a$ であるとする。

(1) 座標系 $\mathcal{O}$ において，点 $(x, 0, 0)$（ただし $|x| \gg a$）での電場 $\boldsymbol{E}$ と磁束密度 $\boldsymbol{B}$ を求めよ。

この系を，座標系 $\mathcal{O}$ に対して速度 $\boldsymbol{v} = (0, 0, v_z)$ で等速運動する座標系 $\mathcal{O}'$ で記述することを考える。このとき，座標系 $\mathcal{O}(t, x, y, z)$ と $\mathcal{O}'(t', x', y', z')$ の間には Lorentz 変換の関係
{: .problem-lead }

$$
(ct', x', y', z') = \bigl(\gamma(ct - \beta z),\ x,\ y,\ \gamma(z - \beta ct)\bigr) \tag{1}
$$

が成り立つ。ただし $\beta = v_z/c,\ \gamma = 1/\sqrt{1 - \beta^2}$ である。
{: .problem-lead }

(2) 座標系 $\mathcal{O}'$ において，荷電粒子の間隔 $a'$ が $a' = \gamma a$ となることを，式 (1) を用いて示せ。

(3) 座標系 $\mathcal{O}'$ において，点 $(x', y', z')$（ただし $x'^2 + y'^2 \gg a'^2$）での電場 $\boldsymbol{E}'$ と磁束密度 $\boldsymbol{B}'$ を求めよ。

座標系 $\mathcal{O}$ と $\mathcal{O}'$ における電場 $\boldsymbol{E}$ と $\boldsymbol{E}'$ および磁束密度 $\boldsymbol{B}$ と $\boldsymbol{B}'$ の各成分の間には，以下の関係式が成り立つ。
{: .problem-lead }

$$
(E_x, E_y, E_z) = \bigl(\gamma(E_x' + c\beta B_y'),\ \gamma(E_y' - c\beta B_x'),\ E_z'\bigr) \tag{2}
$$

$$
(B_x, B_y, B_z) = \left(\gamma\left(B_x' - \frac{\beta}{c}E_y'\right),\ \gamma\left(B_y' + \frac{\beta}{c}E_x'\right),\ B_z'\right) \tag{3}
$$

(4) 設問3の結果と式 (2)，(3) を用いて座標系 $\mathcal{O}$ における電場 $\boldsymbol{E}$ と磁束密度 $\boldsymbol{B}$ を求めよ。さらにこの結果を設問1の結果と比較せよ。

次に，座標系 $\mathcal{O}$ において $z$ 軸上を速度 $\boldsymbol{v} = (0, 0, v_z)$ で等速運動する1個の荷電粒子（電荷 $q$）のみがある場合を考える。このとき，この荷電粒子は座標系 $\mathcal{O}'$ の原点にとどまり続けると考えることができる。

(5) 座標系 $\mathcal{O}'$ において，点 $(x', y', z')$ での電場 $\boldsymbol{E}'$ と磁束密度 $\boldsymbol{B}'$ を求めよ。ただし，原点は除く。

(6) 座標系 $\mathcal{O}$ において，点 $(x, 0, 0)$（ただし $x \neq 0$）での電場 $\boldsymbol{E}$ と磁束密度 $\boldsymbol{B}$ を求めよ。式 (1)，(2)，(3) の関係がこの場合でも成り立つことを用いてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成27年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
電荷とともに動く慣性系では電荷が静止しているため，静電場から電磁場を求めることができます。電場と磁場のローレンツ変換を使うと，運動する電荷の場を同じ静電場から調べることができます。
</div>

### (1)
$|x| \gg a$ の遠方では，$z$ 軸上の荷電粒子列は一様な線電荷密度 $\lambda = \dfrac{q}{a}$ および定常電流 $I = \lambda v_z = \dfrac{q v_z}{a}$とみなすことができます。

軸対称性より，半径 $r = |x|$，長さ $\ell$ の円筒面に対してガウスの法則を用いると，

$$
\begin{aligned}
2\pi r\ell E_r &= \frac{\lambda\ell}{\epsilon_0}\\
E_r &= \frac{q}{2\pi\epsilon_0 ar}
\end{aligned}
$$

であり，点 $(x, 0, 0)$ では $E_x = \dfrac{q}{2\pi\epsilon_0 a x},\ E_y = E_z = 0$ です。

同様に半径 $r = |x|$ の円周に沿ってアンペールの法則を用いると，

$$
\begin{aligned}
2\pi rB_\varphi &= \mu_0 I\\
&= \frac{\mu_0 qv_z}{a}\\
B_\varphi &= \frac{\mu_0 qv_z}{2\pi ar}
\end{aligned}
$$

であり，点 $(x, 0, 0)$ では接線方向 $\boldsymbol{e}_\varphi = \operatorname{sgn}(x)\,\boldsymbol{e}_y$ なので $B_y = \dfrac{\mu_0 q v_z}{2\pi a x},\ B_x = B_z = 0$ です。したがって，

$$
\finalanswer{\boldsymbol{E} = \left(\frac{q}{2\pi\epsilon_0 a x},\ 0,\ 0\right),\qquad \boldsymbol{B} = \left(0,\ \frac{\mu_0 q v_z}{2\pi a x},\ 0\right)}
$$

### (2)
隣り合う2つの荷電粒子を粒子1，粒子2とし，系 $\mathcal{O}$ における時刻 $t = 0$ の位置をそれぞれ $z_1 = 0,\ z_2 = a$ とします。

式 (1) の $z' = \gamma(z - \beta ct)$ に $t = 0$ を代入すると，粒子1，2の系 $\mathcal{O}'$ における $z'$ 座標はそれぞれ

$$
z_1' = \gamma(0 - 0) = 0,\qquad z_2' = \gamma(a - 0) = \gamma a
$$

となります。系 $\mathcal{O}'$ では荷電粒子群は静止しているため，$z_1'$ と $z_2'$ は時刻 $t'$ によらず一定です。よって系 $\mathcal{O}'$ での間隔 $a'$ は $a' = z_2' - z_1' = \gamma a$ となります。

### (3)
系 $\mathcal{O}'$ では荷電粒子群は $z'$ 軸上に間隔 $a' = \gamma a$ で静止しているため，電流は $0$ であり磁束密度は $\boldsymbol{B}' = \mathbf{0}$ です。

また $r' = \sqrt{x'^2 + y'^2} \gg a'$ では一様な線電荷密度 $\lambda' = \dfrac{q}{a'} = \dfrac{q}{\gamma a}$ とみなせるため，ガウスの法則より動径方向の電場 $E_{r'}' = \dfrac{q}{2\pi\epsilon_0 a' r'}$ が生じます。直交座標成分で表すと次のとおりです。したがって，

$$
\finalanswer{\boldsymbol{E}' = \frac{q}{2\pi\epsilon_0 \gamma a (x'^2 + y'^2)}(x',\ y',\ 0),\qquad \boldsymbol{B}' = (0,\ 0,\ 0)}
$$

### (4)
式 (1) より $x' = x,\ y' = y$ です。問3の $\boldsymbol{E}',\ \boldsymbol{B}' = \mathbf{0}$ を式 (2)，(3) に代入します。 設問3の条件 $r'=\sqrt{x'^2+y'^2}\gg a'$ は，$r=\sqrt{x^2+y^2}\gg\gamma a$ となります。以下はこの連続近似が成り立つ範囲で考えます。

$$
\begin{aligned}
(E_x, E_y, E_z)
&= (\gamma E_x',\ \gamma E_y',\ 0) \\
&= \frac{q}{2\pi\epsilon_0 a (x^2 + y^2)}(x,\ y,\ 0)
\end{aligned}
$$

$$
\begin{aligned}
(B_x, B_y, B_z)
&= \left(-\gamma\frac{\beta}{c}E_y',\ \gamma\frac{\beta}{c}E_x',\ 0\right) \\
&= \frac{v_z}{c^2}\frac{q}{2\pi\epsilon_0 a (x^2 + y^2)}(-y,\ x,\ 0) \\
&= \frac{\mu_0 q v_z}{2\pi a (x^2 + y^2)}(-y,\ x,\ 0)
\end{aligned}
$$

ここで $\beta = v_z/c$ および $\dfrac{1}{\epsilon_0 c^2} = \mu_0$ を用いました。したがって，

$$
\finalanswer{\boldsymbol{E} = \frac{q}{2\pi\epsilon_0 a (x^2 + y^2)}(x,\ y,\ 0),\qquad \boldsymbol{B} = \frac{\mu_0 q v_z}{2\pi a (x^2 + y^2)}(-y,\ x,\ 0)}
$$

**設問1との比較**：$y = 0$ を代入すると点 $(x, 0, 0)$ での電磁場は $\boldsymbol{E} = \left(\dfrac{q}{2\pi\epsilon_0 a x},\ 0,\ 0\right)$，$\boldsymbol{B} = \left(0,\ \dfrac{\mu_0 q v_z}{2\pi a x},\ 0\right)$ となり，設問1で直接マクスウェル方程式から求めた結果と完全に一致します。

### (5)
系 $\mathcal{O}'$ では電荷 $q$ が原点に静止しているため，磁束密度は $\mathbf{0}$，電場はクーロンの法則で与えられます。したがって，

$$
\finalanswer{\boldsymbol{E}' = \frac{q}{4\pi\epsilon_0 (x'^2 + y'^2 + z'^2)^{3/2}}(x',\ y',\ z'),\qquad \boldsymbol{B}' = (0,\ 0,\ 0)}
$$

### (6)
系 $\mathcal{O}$ の点 $(x, 0, 0)$・時刻 $t$ を式 (1) で系 $\mathcal{O}'$ の座標へ変換すると，

$$
x' = x,\qquad y' = 0,\qquad z' = \gamma(0 - \beta ct) = -\gamma v_z t
$$

となります。よって $x'^2 + y'^2 + z'^2 = x^2 + \gamma^2 v_z^2 t^2$ です。これを問5の $\boldsymbol{E}',\ \boldsymbol{B}' = \mathbf{0}$ に代入し，式 (2)，(3) を用いて系 $\mathcal{O}$ での電磁場を求めます。

$$
\begin{aligned}
E_x &= \gamma E_x' \\
&= \frac{\gamma q x}{4\pi\epsilon_0 \left(x^2 + \gamma^2 v_z^2 t^2\right)^{3/2}} \\
E_y &= \gamma E_y' \\
&= 0 \\
E_z &= E_z' \\
&= -\frac{\gamma q v_z t}{4\pi\epsilon_0 \left(x^2 + \gamma^2 v_z^2 t^2\right)^{3/2}}
\end{aligned}
$$

$$
\begin{aligned}
B_x &= 0 \\
B_y &= \gamma\frac{\beta}{c}E_x' \\
&= \frac{v_z}{c^2} E_x \\
&= \frac{\mu_0 \gamma q v_z x}{4\pi \left(x^2 + \gamma^2 v_z^2 t^2\right)^{3/2}} \\
B_z &= 0
\end{aligned}
$$

したがって，

$$
\finalanswer{\boldsymbol{E} = \frac{\gamma q}{4\pi\epsilon_0 \left(x^2 + \gamma^2 v_z^2 t^2\right)^{3/2}}(x,\ 0,\ -v_z t),\qquad \boldsymbol{B} = \left(0,\ \frac{\mu_0 \gamma q v_z x}{4\pi \left(x^2 + \gamma^2 v_z^2 t^2\right)^{3/2}},\ 0\right)}
$$

<aside class="rigor-note" markdown>
$t=0$ の最接近時刻には，電場の大きさは同じ距離にある静止電荷の $\gamma$ 倍です。$v_z\neq0$ のとき，場が強くなる時間幅は $\Delta t\sim |x|/(\gamma|v_z|)$ であり，同じ速さの非相対論的な見積もりの $1/\gamma$ 倍になります。高エネルギー荷電粒子の電気力線は，進行方向に垂直な面へ集中します。
</aside>
