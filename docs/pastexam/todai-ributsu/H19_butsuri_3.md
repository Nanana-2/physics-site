---
title: 東大理物 平成19年度 物理学 第3問：回転座標系での三体問題とラグランジュ点
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成19年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成19年度 物理学 第3問：回転座標系での三体問題とラグランジュ点

## 問題

質量 $m_1$ の太陽と質量 $m_2$ の地球がお互いの重力によってケプラー運動しているものとする。簡単のために以下では軌道の離心率は無視して円運動の場合のみを考える。それらの公転面上で太陽と地球の重心を原点とする2次元座標系として，慣性系 $S$ と，太陽と地球が常に $x$ 軸上の点 $P_1$ と点 $P_2$ に位置するような回転系 $S'$ を考える（図1参照）。太陽と地球の距離を $a$ とすれば，$P_1$ と $P_2$ の座標はそれぞれ $(-\mu_2 a, 0)$，$(\mu_1 a, 0)$ で与えられる。ただし，

$$
\mu_1 \equiv \frac{m_1}{m_1 + m_2}, \qquad \mu_2 \equiv \frac{m_2}{m_1 + m_2} \tag{1}
$$

である。また，この回転系の角速度 $\omega$ はケプラーの第3法則より，

$$
G(m_1 + m_2) = \omega^2 a^3 \tag{2}
$$

を満たす（$G$ はニュートンの重力定数）。

<figure class="problem-figure" markdown>
![慣性系 S と回転系 S' の座標関係](../../assets/figures/pastexam-todai-ributsu/H19_butsuri_3-p1-light.svg#only-light)
![慣性系 S と回転系 S' の座標関係](../../assets/figures/pastexam-todai-ributsu/H19_butsuri_3-p1-dark.svg#only-dark)
<figcaption markdown="span">図1：慣性系 $S$ と回転系 $S'$。</figcaption>
</figure>

(1) この平面上の任意の点を $P$ としたとき，$S$ 系における $P$ の成分 $(\xi, \eta)$ を $S'$ 系での成分 $(x, y)$ で表せ。

(2) $S'$ 系からみて $(x, y)$ の位置にある質量 $m$ の質点を考える。$m$ は $m_1$ および $m_2$ に比べて十分小さく，この質点は太陽と地球のケプラー運動には影響を与えないとした時，設問1の結果からこの質点に対するラグランジアンが

$$
\mathcal{L} = \frac{m}{2}(\dot{x}^2 + \dot{y}^2) + \frac{m\omega^2}{2}(x^2 + y^2) + m\omega(x\dot{y} - \dot{x}y) + Gm\left(\frac{m_1}{r_1} + \frac{m_2}{r_2}\right) \tag{3}
$$

となることを示せ。ただし，

$$
r_1 \equiv \sqrt{(x + \mu_2 a)^2 + y^2}, \qquad r_2 \equiv \sqrt{(x - \mu_1 a)^2 + y^2} \tag{4}
$$

である。

(3) この質点の $S'$ 系における運動方程式の $x$ 成分および $y$ 成分を書き下せ。

(4) $S'$ 系から見たとき，この質点の加速度と速度がともに $0$ となるような特別な点（$\ddot{x} = \ddot{y} = \dot{x} = \dot{y} = 0$）はラグランジュ点と呼ばれ，全部で5つあることが知られている。運動方程式の $y$ 成分を考えることで，ラグランジュ点は

$$
\mu_1\left(\frac{a}{r_1}\right)^3 + \mu_2\left(\frac{a}{r_2}\right)^3 = 1 \tag{5}
$$

あるいは

$$
y = 0 \tag{6}
$$

のいずれかを満たすことを示せ。

(5) 式 (6) を満たす $S'$ 系の $x$ 軸上にあるラグランジュ点は，図2に示されているように，$P_1$ と $P_2$ の外側に一つずつ，および $P_1$ と $P_2$ の中間に一つ，合わせて3個存在することが知られている。特に地球からみてちょうど太陽の反対側にある $L_2$ 点は，天文観測衛星に適した位置である。この $L_2$ 点と $P_2$ との距離を $r_2$ として運動方程式の $x$ 成分を考えれば，$\mu_2/\mu_1$ が $u \equiv r_2/a$ の関数として

$$
\frac{\mu_2}{\mu_1} = \frac{3u^3}{(1 + u)^2}\frac{1 + u + u^2/3}{1 - u^3} \tag{7}
$$

と書けることを示せ。変形の際，$\mu_1 + \mu_2 = 1$ であることに注意せよ。

<figure class="problem-figure" markdown>
![x 軸上のラグランジュ点の配置](../../assets/figures/pastexam-todai-ributsu/H19_butsuri_3-p2-light.svg#only-light)
![x 軸上のラグランジュ点の配置](../../assets/figures/pastexam-todai-ributsu/H19_butsuri_3-p2-dark.svg#only-dark)
<figcaption markdown="span">図2：$x$ 軸上にあるラグランジュ点 $L_1, L_2, L_3$。</figcaption>
</figure>

(6) 式 (7) から，$\mu_2/\mu_1 \ll 1$ の場合 $u \ll 1$ となることがわかる。この場合，$L_2$ 点の位置 $u$ を $\mu_2/\mu_1$ の最低次で求めよ。特に，太陽と地球の系（$\mu_2/\mu_1 \approx 3\times 10^{-6}$，$a = 1.5\times 10^{11}\,\mathrm{m}$）の場合，地球と $L_2$ 点までの距離の値を近似的に求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成19年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
太陽と地球と一緒に回る回転系 $S'$ へ座標変換すると，2天体の位置が時間によらず固定されるため，ポテンシャルが時間に依存しなくなります。ラグランジアンは座標変換だけで書き換えることができるため，遠心力やコリオリ力を自動的に取り込んだ運動方程式を導くことができます。

回転系で静止する点では速度と加速度がともに $0$ になり，万有引力と遠心力のつり合いの式が残ります。ケプラーの第3法則を用いると重力定数と角速度を消して無次元量だけの関係式にまとめることができ，質量比が小さい極限で $L_2$ 点の位置を近似計算することができます。
</div>

### (1)

回転系 $S'$ は慣性系 $S$ に対して反時計回りに角度 $\omega t$ だけ回転しています。図1より，回転変換の式から $(\xi, \eta)$ は $(x, y)$ を用いて次式で表されます。

$$
\begin{aligned}
\xi &= x\cos\omega t - y\sin\omega t \\
\eta &= x\sin\omega t + y\cos\omega t
\end{aligned}
$$

したがって，$(\xi, \eta)$ は次式となります。

$$
\finalanswer{\xi = x\cos\omega t - y\sin\omega t, \qquad \eta = x\sin\omega t + y\cos\omega t}
$$

### (2)

設問1の座標変換を時間 $t$ で微分して $\dot{\xi}$ と $\dot{\eta}$ を求めます。

$$
\begin{aligned}
\dot{\xi} &= (\dot{x} - \omega y)\cos\omega t - (\dot{y} + \omega x)\sin\omega t \\
\dot{\eta} &= (\dot{x} - \omega y)\sin\omega t + (\dot{y} + \omega x)\cos\omega t
\end{aligned}
$$

2乗して足し合わせます。$\cos^2\omega t + \sin^2\omega t = 1$ であり，交差項が打ち消し合います。

$$
\begin{aligned}
\dot{\xi}^2 + \dot{\eta}^2 &= (\dot{x} - \omega y)^2 + (\dot{y} + \omega x)^2 \\
&= \dot{x}^2 - 2\omega\dot{x}y + \omega^2 y^2 + \dot{y}^2 + 2\omega x\dot{y} + \omega^2 x^2 \\
&= \dot{x}^2 + \dot{y}^2 + \omega^2(x^2 + y^2) + 2\omega(x\dot{y} - \dot{x}y)
\end{aligned}
$$

質量 $m$ の質点の運動エネルギーは $T = \dfrac{m}{2}(\dot{\xi}^2 + \dot{\eta}^2)$ です。また，$P_1(-\mu_2 a, 0)$ と $P_2(\mu_1 a, 0)$ からの距離は式 (4) の $r_1, r_2$ なので，太陽と地球による万有引力のポテンシャルエネルギーは次式です。

$$
U = -Gm\left(\frac{m_1}{r_1} + \frac{m_2}{r_2}\right)
$$

これらをラグランジアン $\mathcal{L} = T - U$ に代入します。

$$
\mathcal{L} = \frac{m}{2}(\dot{x}^2 + \dot{y}^2) + \frac{m\omega^2}{2}(x^2 + y^2) + m\omega(x\dot{y} - \dot{x}y) + Gm\left(\frac{m_1}{r_1} + \frac{m_2}{r_2}\right)
$$

これにより式 (3) が導かれます。

### (3)

式 (4) より，$r_1, r_2$ の偏微分は次式になります。

$$
\frac{\partial}{\partial x}\left(\frac{1}{r_1}\right) = -\frac{x + \mu_2 a}{r_1^3}, \qquad \frac{\partial}{\partial x}\left(\frac{1}{r_2}\right) = -\frac{x - \mu_1 a}{r_2^3}
$$

$$
\frac{\partial}{\partial y}\left(\frac{1}{r_1}\right) = -\frac{y}{r_1^3}, \qquad \frac{\partial}{\partial y}\left(\frac{1}{r_2}\right) = -\frac{y}{r_2^3}
$$

まず $x$ 成分についてラグランジアン $\mathcal{L}$ の各偏微分を計算します。

$$
\begin{aligned}
\frac{\partial\mathcal{L}}{\partial\dot{x}} &= m\dot{x} - m\omega y \\
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial\mathcal{L}}{\partial\dot{x}}\right) &= m\ddot{x} - m\omega\dot{y} \\
\frac{\partial\mathcal{L}}{\partial x} &= m\omega^2 x + m\omega\dot{y} - Gm\left(\frac{m_1(x + \mu_2 a)}{r_1^3} + \frac{m_2(x - \mu_1 a)}{r_2^3}\right)
\end{aligned}
$$

オイラー・ラグランジュ方程式 $\dfrac{\mathrm{d}}{\mathrm{d}t}\dfrac{\partial\mathcal{L}}{\partial\dot{x}} - \dfrac{\partial\mathcal{L}}{\partial x} = 0$ に代入し，両辺を $m$ で割ります。

$$
\ddot{x} - 2\omega\dot{y} - \omega^2 x + G\left(\frac{m_1(x + \mu_2 a)}{r_1^3} + \frac{m_2(x - \mu_1 a)}{r_2^3}\right) = 0
$$

次に $y$ 成分について同様に計算します。

$$
\begin{aligned}
\frac{\partial\mathcal{L}}{\partial\dot{y}} &= m\dot{y} + m\omega x \\
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial\mathcal{L}}{\partial\dot{y}}\right) &= m\ddot{y} + m\omega\dot{x} \\
\frac{\partial\mathcal{L}}{\partial y} &= m\omega^2 y - m\omega\dot{x} - Gm\left(\frac{m_1}{r_1^3} + \frac{m_2}{r_2^3}\right)y
\end{aligned}
$$

オイラー・ラグランジュ方程式 $\dfrac{\mathrm{d}}{\mathrm{d}t}\dfrac{\partial\mathcal{L}}{\partial\dot{y}} - \dfrac{\partial\mathcal{L}}{\partial y} = 0$ に代入し，両辺を $m$ で割ります。

$$
\ddot{y} + 2\omega\dot{x} - \omega^2 y + G\left(\frac{m_1}{r_1^3} + \frac{m_2}{r_2^3}\right)y = 0
$$

したがって，運動方程式の $x$ 成分および $y$ 成分は次式となります。

$$
\finalanswer{
\begin{aligned}
m\ddot{x} &= 2m\omega\dot{y} + m\omega^2 x - Gm\left(\frac{m_1(x + \mu_2 a)}{r_1^3} + \frac{m_2(x - \mu_1 a)}{r_2^3}\right) \\
m\ddot{y} &= -2m\omega\dot{x} + m\omega^2 y - Gm\left(\frac{m_1}{r_1^3} + \frac{m_2}{r_2^3}\right)y
\end{aligned}
}
$$

### (4)

ラグランジュ点では $\ddot{x} = \ddot{y} = \dot{x} = \dot{y} = 0$ です。これを設問3の運動方程式の $y$ 成分に代入します。

$$
\left(\omega^2 - G\frac{m_1}{r_1^3} - G\frac{m_2}{r_2^3}\right)y = 0
$$

式 (1) と式 (2) より，$Gm_1 = \mu_1 G(m_1 + m_2) = \mu_1 \omega^2 a^3$，および $Gm_2 = \mu_2 \omega^2 a^3$ です。これらを代入して $\omega^2$ をくくり出します。

$$
\begin{aligned}
\omega^2\left(1 - \mu_1\frac{a^3}{r_1^3} - \mu_2\frac{a^3}{r_2^3}\right)y &= 0 \\
\left(1 - \mu_1\left(\frac{a}{r_1}\right)^3 - \mu_2\left(\frac{a}{r_2}\right)^3\right)y &= 0
\end{aligned}
$$

$\omega \neq 0$ なので，この積が $0$ であることから，次式または $y = 0$ が成り立ちます。

$$
\mu_1\left(\frac{a}{r_1}\right)^3 + \mu_2\left(\frac{a}{r_2}\right)^3 = 1
$$

### (5)

$L_2$ 点は $y = 0$ かつ $P_2(\mu_1 a, 0)$ より外側，すなわち $x > \mu_1 a$ に位置します。$P_2$ と $L_2$ の距離が $r_2 = u a$ なので，$L_2$ 点の座標 $x$ および $P_1$ からの距離 $r_1$ は $\mu_1 + \mu_2 = 1$ を用いて次のように表されます。

$$
\begin{aligned}
x &= \mu_1 a + r_2 = (\mu_1 + u)a \\
x - \mu_1 a &= r_2 = u a \\
x + \mu_2 a &= r_1 = (\mu_1 + \mu_2 + u)a = (1 + u)a
\end{aligned}
$$

設問3の運動方程式の $x$ 成分に $\ddot{x} = \dot{y} = 0$ と $Gm_1 = \mu_1\omega^2 a^3$，$Gm_2 = \mu_2\omega^2 a^3$ を代入します。

$$
\begin{aligned}
\omega^2 x &= G\frac{m_1(x + \mu_2 a)}{r_1^3} + G\frac{m_2(x - \mu_1 a)}{r_2^3} \\
\omega^2(\mu_1 + u)a &= \mu_1\omega^2 a^3 \frac{1}{r_1^2} + \mu_2\omega^2 a^3 \frac{1}{r_2^2}
\end{aligned}
$$

両辺を $\omega^2 a$ で割り，$r_1 = (1 + u)a$，$r_2 = u a$ を代入します。

$$
\mu_1 + u = \frac{\mu_1}{(1 + u)^2} + \frac{\mu_2}{u^2}
$$

ここで $\mu_1 + \mu_2 = 1$ を用いて左辺の $u$ を $u(\mu_1 + \mu_2)$ に書き換え，$\mu_1$ の項を左辺に，$\mu_2$ の項を右辺に集めます。

$$
\begin{aligned}
\mu_1 + (\mu_1 + \mu_2)u &= \frac{\mu_1}{(1 + u)^2} + \frac{\mu_2}{u^2} \\
\mu_1\left(1 + u - \frac{1}{(1 + u)^2}\right) &= \mu_2\left(\frac{1}{u^2} - u\right)
\end{aligned}
$$

両辺の括弧内をそれぞれ通分します。

$$
\begin{aligned}
1 + u - \frac{1}{(1 + u)^2} &= \frac{(1 + u)^3 - 1}{(1 + u)^2} \\
&= \frac{3u + 3u^2 + u^3}{(1 + u)^2} \\
&= \frac{3u\left(1 + u + u^2/3\right)}{(1 + u)^2}
\end{aligned}
$$

$$
\frac{1}{u^2} - u = \frac{1 - u^3}{u^2}
$$

これらを代入して $\dfrac{\mu_2}{\mu_1}$ について解きます。

$$
\begin{aligned}
\frac{\mu_2}{\mu_1} &= \frac{3u\left(1 + u + u^2/3\right)}{(1 + u)^2}\cdot\frac{u^2}{1 - u^3} \\
&= \frac{3u^3}{(1 + u)^2}\frac{1 + u + u^2/3}{1 - u^3}
\end{aligned}
$$

これにより式 (7) が導かれます。

### (6)

$u \ll 1$ のとき，式 (7) の右辺で $u$ の高次の項を無視すると $(1 + u)^2 \simeq 1$，$1 + u + u^2/3 \simeq 1$，$1 - u^3 \simeq 1$ となります。したがって最低次では次式が成り立ちます。

$$
\begin{aligned}
\frac{\mu_2}{\mu_1} &\simeq 3u^3 \\
u &\simeq \left(\frac{\mu_2}{3\mu_1}\right)^{1/3}
\end{aligned}
$$

太陽と地球の系では $\dfrac{\mu_2}{\mu_1} \approx 3\times 10^{-6}$，$a = 1.5\times 10^{11}\,\mathrm{m}$ なので，$u$ と地球から $L_2$ 点までの距離 $r_2 = u a$ は次のように求めることができます。

$$
\begin{aligned}
u &\approx \left(\frac{3\times 10^{-6}}{3}\right)^{1/3} \\
&= \bigl(10^{-6}\bigr)^{1/3} \\
&= 10^{-2}
\end{aligned}
$$

$$
\begin{aligned}
r_2 &= u a \\
&\approx 10^{-2}\times 1.5\times 10^{11}\,\mathrm{m} \\
&= 1.5\times 10^{9}\,\mathrm{m}
\end{aligned}
$$

したがって，$u$ の最低次の表式と地球から $L_2$ 点までの近似距離は次式となります。

$$
\finalanswer{u \simeq \left(\frac{\mu_2}{3\mu_1}\right)^{1/3}, \qquad r_2 \approx 1.5\times 10^{9}\,\mathrm{m}}
$$
