---
title: 東大理物 平成18年度 物理学 第3問：真空中の平面電磁波の性質
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成18年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成18年度 物理学 第3問：真空中の平面電磁波の性質

## 問題

以下に示す真空中での Maxwell の方程式を出発点として平面電磁波の性質を導き出したい。ここで，$\vec{E}$ と $\vec{B}$ はそれぞれ電場と磁束密度，$\epsilon_0$ と $\mu_0$ はそれぞれ真空の誘電率と透磁率である。また，$t$ は時間であり，$\nabla$ は空間座標 $\vec{r} = (x, y, z)$ についてのベクトル微分演算子である。電荷や電流の存在しない場合を考える。

$$
\nabla\cdot\vec{E} = 0 \tag{1}
$$

$$
\nabla\times\vec{B} = \epsilon_0\mu_0\frac{\partial\vec{E}}{\partial t} \tag{2}
$$

$$
\nabla\cdot\vec{B} = 0 \tag{3}
$$

$$
\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t} \tag{4}
$$

以下の設問に答えよ。

(1) 任意の三次元ベクトル $\vec{V}$ に対して次の公式が成り立つことを示せ。

$$
\nabla\times(\nabla\times\vec{V}) = \nabla(\nabla\cdot\vec{V}) - \nabla^2\vec{V}
$$

(2) 前問の公式を Maxwell の方程式に適用して，$\vec{E}$ に対する波動方程式および $\vec{B}$ に対する波動方程式をそれぞれ導け。

(3) 次の式で表される $\vec{E}$ および $\vec{B}$，すなわち平面波が前問で求めた波動方程式の解であるための条件を求めよ。ただし，$\vec{E}_0, \vec{B}_0, \vec{k}, \vec{k}'$ は定数ベクトル，$\omega, \omega', \alpha, \alpha'$ はそれぞれ定数で，$0 \le \alpha < \pi,\ 0 \le \alpha' < \pi$ である。

$$
\vec{E} = \vec{E}_0\sin(\vec{k}\cdot\vec{r} - \omega t + \alpha) \tag{5}
$$

$$
\vec{B} = \vec{B}_0\sin(\vec{k}'\cdot\vec{r} - \omega' t + \alpha') \tag{6}
$$

(4) 式 (5) と式 (6) で表される $\vec{E}$ および $\vec{B}$ がそれぞれの波数ベクトルに垂直であること，すなわち横波であることを示せ。

(5) 式 (5) と式 (6) において，$\vec{k} = \vec{k}'$，$\omega = \omega'$ および $\alpha = \alpha'$ であることを示せ。

(6) 式 (5) と式 (6) で表される $\vec{E}$ と $\vec{B}$ は互いに直交していることを示せ。

(7) 平面電磁波の位相速度を求めよ。

(8) 式 (5) と式 (6) で電場 $\vec{E}$ と磁場 $\vec{H}(= \vec{B}/\mu_0)$ の大きさの比 $|\vec{E}|/|\vec{H}|$ が常に一定であること，およびこの比は抵抗の次元をもつことを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成18年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
真空中のマクスウェル方程式は電場 $\vec{E}$ と磁束密度 $\vec{B}$ の1階偏微分方程式ですが，回転をもう一度とってベクトル公式を用いると，それぞれが単独で満たす2階の波動方程式に分かれます。

平面波の形を代入すると，空間微分 $\nabla$ は波数ベクトル $\vec{k}$ の掛け算に，時間微分 $\partial/\partial t$ は $-\omega$ の掛け算に置き換わります。そのため，発散や回転の微分方程式がすべて定数ベクトル同士の代数関係に変わり，横波性や直交性，位相速度を直接導くことができます。
</div>

### (1)

$\vec{V} = (V_x, V_y, V_z)$ とおき，$\vec{W} = \nabla\times\vec{V}$ の各成分を書き出します。

$$
W_x = \frac{\partial V_z}{\partial y} - \frac{\partial V_y}{\partial z}, \qquad W_y = \frac{\partial V_x}{\partial z} - \frac{\partial V_z}{\partial x}, \qquad W_z = \frac{\partial V_y}{\partial x} - \frac{\partial V_x}{\partial y}
$$

$\nabla\times(\nabla\times\vec{V}) = \nabla\times\vec{W}$ の $x$ 成分を計算します。途中で $\dfrac{\partial^2 V_x}{\partial x^2}$ を足して引きます。

$$
\begin{aligned}
\bigl[\nabla\times(\nabla\times\vec{V})\bigr]_x &= \frac{\partial W_z}{\partial y} - \frac{\partial W_y}{\partial z} \\
&= \frac{\partial}{\partial y}\left(\frac{\partial V_y}{\partial x} - \frac{\partial V_x}{\partial y}\right) - \frac{\partial}{\partial z}\left(\frac{\partial V_x}{\partial z} - \frac{\partial V_z}{\partial x}\right) \\
&= \frac{\partial^2 V_y}{\partial y\partial x} + \frac{\partial^2 V_z}{\partial z\partial x} - \frac{\partial^2 V_x}{\partial y^2} - \frac{\partial^2 V_x}{\partial z^2} \\
&= \frac{\partial}{\partial x}\left(\frac{\partial V_x}{\partial x} + \frac{\partial V_y}{\partial y} + \frac{\partial V_z}{\partial z}\right) - \left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)V_x \\
&= \bigl[\nabla(\nabla\cdot\vec{V}) - \nabla^2\vec{V}\bigr]_x
\end{aligned}
$$

$x, y, z$ の巡回置換によって $y$ 成分と $z$ 成分についても同じ等式が成り立ちます。したがって，$\nabla\times(\nabla\times\vec{V}) = \nabla(\nabla\cdot\vec{V}) - \nabla^2\vec{V}$ が成り立ちます。

### (2)

式 (4) の両辺の回転をとり，設問1の公式と式 (1)，式 (2) を用います。

$$
\begin{aligned}
\nabla\times(\nabla\times\vec{E}) &= -\frac{\partial}{\partial t}(\nabla\times\vec{B}) \\
\nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E} &= -\epsilon_0\mu_0\frac{\partial^2\vec{E}}{\partial t^2} \\
-\nabla^2\vec{E} &= -\epsilon_0\mu_0\frac{\partial^2\vec{E}}{\partial t^2} \\
\left(\nabla^2 - \epsilon_0\mu_0\frac{\partial^2}{\partial t^2}\right)\vec{E} &= \vec{0}
\end{aligned}
$$

同様に，式 (2) の両辺の回転をとり，設問1の公式と式 (3)，式 (4) を用います。

$$
\begin{aligned}
\nabla\times(\nabla\times\vec{B}) &= \epsilon_0\mu_0\frac{\partial}{\partial t}(\nabla\times\vec{E}) \\
\nabla(\nabla\cdot\vec{B}) - \nabla^2\vec{B} &= -\epsilon_0\mu_0\frac{\partial^2\vec{B}}{\partial t^2} \\
\left(\nabla^2 - \epsilon_0\mu_0\frac{\partial^2}{\partial t^2}\right)\vec{B} &= \vec{0}
\end{aligned}
$$

したがって，$\vec{E}$ と $\vec{B}$ に対する波動方程式は次式となります。

$$
\finalanswer{\left(\nabla^2 - \epsilon_0\mu_0\frac{\partial^2}{\partial t^2}\right)\vec{E} = \vec{0}, \qquad \left(\nabla^2 - \epsilon_0\mu_0\frac{\partial^2}{\partial t^2}\right)\vec{B} = \vec{0}}
$$

### (3)

$\vec{E}_0 \neq \vec{0}$，$\vec{B}_0 \neq \vec{0}$ とします。式 (5) に対して $\nabla^2\vec{E}$ と $\dfrac{\partial^2\vec{E}}{\partial t^2}$ を計算します。

$$
\begin{aligned}
\nabla^2\vec{E} &= \left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)\vec{E}_0\sin(\vec{k}\cdot\vec{r} - \omega t + \alpha) \\
&= -(k_x^2 + k_y^2 + k_z^2)\vec{E}_0\sin(\vec{k}\cdot\vec{r} - \omega t + \alpha) \\
&= -|\vec{k}|^2\vec{E}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^2\vec{E}}{\partial t^2} &= -\omega^2\vec{E}_0\sin(\vec{k}\cdot\vec{r} - \omega t + \alpha) \\
&= -\omega^2\vec{E}
\end{aligned}
$$

これらを波動方程式に代入します。

$$
\bigl(-|\vec{k}|^2 + \epsilon_0\mu_0\omega^2\bigr)\vec{E}_0\sin(\vec{k}\cdot\vec{r} - \omega t + \alpha) = \vec{0}
$$

これがすべての $\vec{r}, t$ について成り立つための条件は $|\vec{k}|^2 = \epsilon_0\mu_0\omega^2$ です。式 (6) についても同様に計算すると $|\vec{k}'|^2 = \epsilon_0\mu_0\omega'^2$ が得られます。

$$
\finalanswer{|\vec{k}|^2 = \epsilon_0\mu_0\omega^2, \qquad |\vec{k}'|^2 = \epsilon_0\mu_0\omega'^2}
$$

### (4)

式 (5) の発散を計算して式 (1) に代入します。

$$
\begin{aligned}
\nabla\cdot\vec{E} &= \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z} \\
&= (k_x E_{0x} + k_y E_{0y} + k_z E_{0z})\cos(\vec{k}\cdot\vec{r} - \omega t + \alpha) \\
&= (\vec{k}\cdot\vec{E}_0)\cos(\vec{k}\cdot\vec{r} - \omega t + \alpha) = 0
\end{aligned}
$$

この等式がすべての $\vec{r}, t$ について成り立つためには $\vec{k}\cdot\vec{E}_0 = 0$ が必要です。よって $\vec{k}\cdot\vec{E} = (\vec{k}\cdot\vec{E}_0)\sin(\vec{k}\cdot\vec{r} - \omega t + \alpha) = 0$ となり，$\vec{E}$ は波数ベクトル $\vec{k}$ に垂直です。

同様に式 (6) を式 (3) に代入すると，次式が得られます。

$$
\nabla\cdot\vec{B} = (\vec{k}'\cdot\vec{B}_0)\cos(\vec{k}'\cdot\vec{r} - \omega' t + \alpha') = 0
$$

よって $\vec{k}'\cdot\vec{B}_0 = 0$ となり，$\vec{k}'\cdot\vec{B} = 0$ です。したがって，$\vec{E}$ と $\vec{B}$ はそれぞれの波数ベクトルに垂直であり，横波です。

### (5)

式 (5) の回転と式 (6) の時間微分を計算して式 (4) に代入します。

$$
\begin{aligned}
\nabla\times\vec{E} &= (\vec{k}\times\vec{E}_0)\cos(\vec{k}\cdot\vec{r} - \omega t + \alpha) \\
-\frac{\partial\vec{B}}{\partial t} &= \omega'\vec{B}_0\cos(\vec{k}'\cdot\vec{r} - \omega' t + \alpha')
\end{aligned}
$$

よって，すべての $\vec{r}, t$ に対して次式が恒等的に成り立ちます。

$$
(\vec{k}\times\vec{E}_0)\cos(\vec{k}\cdot\vec{r} - \omega t + \alpha) = \omega'\vec{B}_0\cos(\vec{k}'\cdot\vec{r} - \omega' t + \alpha')
$$

$\vec{E}_0 \neq \vec{0}$，$\vec{B}_0 \neq \vec{0}$ かつ $\vec{k}\perp\vec{E}_0$ より $\vec{k}\times\vec{E}_0 \neq \vec{0}$ です。上の等式がすべての $\vec{r}, t$ で成り立つためには，左辺の $\cos(\vec{k}\cdot\vec{r} - \omega t + \alpha)$ が $0$ になる超平面の集合と，右辺の $\cos(\vec{k}'\cdot\vec{r} - \omega' t + \alpha')$ が $0$ になる超平面の集合が一致しなければなりません。

ここで正の角振動数 $\omega > 0, \omega' > 0$ をとると，波数ベクトルと角振動数は一致し，$\vec{k} = \vec{k}'$，$\omega = \omega'$ となります。また，零点となる超平面が一致するためには，ある整数 $n$ に対して $\alpha' - \alpha = n\pi$ でなければなりません。

与えられた範囲 $0 \le \alpha < \pi$ および $0 \le \alpha' < \pi$ より，$-\pi < \alpha' - \alpha < \pi$ です。この範囲に入る整数 $n$ は $n = 0$ のみなので，$\alpha' - \alpha = 0$，すなわち $\alpha = \alpha'$ となります。

### (6)

設問5で得られた $\vec{k} = \vec{k}'$，$\omega = \omega'$，$\alpha = \alpha'$ を式 (4) の代入式に用いると，すべての $\vec{r}, t$ で次式が成り立ちます。

$$
(\vec{k}\times\vec{E}_0 - \omega\vec{B}_0)\cos(\vec{k}\cdot\vec{r} - \omega t + \alpha) = \vec{0}
$$

したがって，$\vec{B}_0 = \dfrac{1}{\omega}(\vec{k}\times\vec{E}_0)$ です。$\vec{E}_0$ と $\vec{B}_0$ の内積を計算します。

$$
\begin{aligned}
\vec{E}_0\cdot\vec{B}_0 &= \frac{1}{\omega}\vec{E}_0\cdot(\vec{k}\times\vec{E}_0) \\
&= 0
\end{aligned}
$$

よって $\vec{E}\cdot\vec{B} = (\vec{E}_0\cdot\vec{B}_0)\sin^2(\vec{k}\cdot\vec{r} - \omega t + \alpha) = 0$ となり，$\vec{E}$ と $\vec{B}$ は互いに直交しています。

### (7)

位相 $\vec{k}\cdot\vec{r} - \omega t + \alpha$ が一定となる等位相面が波数ベクトル $\vec{k}$ の方向へ進む速さが位相速度 $v_{\mathrm{p}}$ です。設問3で得た関係 $|\vec{k}|^2 = \epsilon_0\mu_0\omega^2$ を用いて計算します。

$$
\begin{aligned}
v_{\mathrm{p}} &= \frac{\omega}{|\vec{k}|} \\
&= \frac{1}{\sqrt{\epsilon_0\mu_0}}
\end{aligned}
$$

したがって，平面電磁波の位相速度は次式となります。

$$
\finalanswer{v_{\mathrm{p}} = \frac{1}{\sqrt{\epsilon_0\mu_0}}}
$$

### (8)

設問4より $\vec{k}$ と $\vec{E}_0$ は垂直なので，設問6の $\vec{B}_0 = \dfrac{1}{\omega}(\vec{k}\times\vec{E}_0)$ の大きさは次式になります。

$$
\begin{aligned}
|\vec{B}_0| &= \frac{|\vec{k}||\vec{E}_0|}{\omega} \\
&= \sqrt{\epsilon_0\mu_0}|\vec{E}_0|
\end{aligned}
$$

設問5より $\vec{E}$ と $\vec{B}$ は位相が完全に一致しているため，$\sin(\vec{k}\cdot\vec{r} - \omega t + \alpha) \neq 0$ のすべての点と時刻において，電場と磁場 $\vec{H} = \vec{B}/\mu_0$ の大きさの比は次のようになります。

$$
\begin{aligned}
\frac{|\vec{E}|}{|\vec{H}|} &= \frac{\mu_0|\vec{E}|}{|\vec{B}|} \\
&= \frac{\mu_0|\vec{E}_0|}{|\vec{B}_0|} \\
&= \frac{\mu_0|\vec{E}_0|}{\sqrt{\epsilon_0\mu_0}|\vec{E}_0|} \\
&= \sqrt{\frac{\mu_0}{\epsilon_0}}
\end{aligned}
$$

これは真空の誘電率と透磁率だけで決まる定数なので，常に一定です。

次にこの比の次元を調べます。電場の単位は単位長さあたりの電圧 $\mathrm{V/m}$ であり，アンペールの法則 $\oint \vec{H}\cdot\mathrm{d}\vec{l} = I$ より磁場の単位は単位長さあたりの電流 $\mathrm{A/m}$ です。したがって，比 $|\vec{E}|/|\vec{H}|$ の単位は次のようになります。

$$
\begin{aligned}
\frac{[\vec{E}]}{[\vec{H}]} &= \frac{\mathrm{V/m}}{\mathrm{A/m}} \\
&= \frac{\mathrm{V}}{\mathrm{A}} \\
&= \Omega
\end{aligned}
$$

オームの法則 $R = V/I$ より $\mathrm{V/A}$ は電気抵抗の単位 $\Omega$ なので，この比は抵抗の次元をもちます。
