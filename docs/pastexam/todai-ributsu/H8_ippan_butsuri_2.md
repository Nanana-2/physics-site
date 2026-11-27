---
title: 東大理物 平成8年度 一般教育科目 物理学 第2問：水平線と鉛直線に拘束された一様な棒の運動
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 一般教育科目 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成8年度 一般教育科目 物理学 第2問：水平線と鉛直線に拘束された一様な棒の運動

## 問題

図に示すように，長さ $\ell$，質量 $M$ の一様な細い棒の両端がそれぞれ水平線（$x$ 軸）上と鉛直線（$y$ 軸）上を離れないように拘束されて滑らかに動くようにしてある。棒の重心の座標を $(x, y)$，棒が鉛直線となす角を $\theta$ とする。
{: .problem-lead }

<figure class="problem-figure" markdown>
![水平線x軸と鉛直線y軸に両端を拘束された長さlの一様な棒の配置](../../assets/figures/pastexam-todai-ributsu/H8_ippan_butsuri_2-p-light.svg#only-light){ loading=lazy }
![水平線x軸と鉛直線y軸に両端を拘束された長さlの一様な棒の配置](../../assets/figures/pastexam-todai-ributsu/H8_ippan_butsuri_2-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) 棒の中点を通り棒に垂直な軸に関する慣性モーメント $I$ は $\dfrac{1}{12}M\ell^2$ であることを示せ。

(2) 力学的全エネルギーを書け。

棒が $x$ 軸から受ける抗力を $R_y$，$y$ 軸から受ける抗力を $R_x$ とする。

(3) $x$，$y$，$\theta$ に対する運動方程式を書け。

(4) 設問 (2) で導いたエネルギーが保存することを運動方程式から示せ。

時刻 $t = 0$ で $\theta = 0$ に棒を置いて $\theta$ が増す向きに初期角速度 $\omega_0$ を与えて放した。

(5) $t \ge 0$ での棒の角速度を $\theta$ と $\omega_0$ で表せ。

(6) $\theta$ が小さいとき運動方程式を近似的に解き，$\theta$ を時刻 $t$ の関数として与えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 一般教育科目 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
両端が直交する2軸上を滑る一様な剛体棒の平面運動を，重心座標 $(x, y)$ と傾き角 $\theta$ によるニュートン・オイラー方程式から解析する問題です。図の配置では $\theta$ の増加が時計回りの回転に対応するため，抗力 $R_x, R_y$ の重心まわりの力のモーメントの符号に注意します。幾何学的拘束条件 $x = \dfrac{\ell}{2}\sin\theta$，$y = -\dfrac{\ell}{2}\cos\theta$ を微分して代入すると抗力のなす仕事が打ち消し合って力学的エネルギーが保存し，微小角近似で単振動の解が得られます。
</div>

### (1)

棒は一様なので，単位長さあたりの線密度は $\rho = \dfrac{M}{\ell}$ です。棒の中点を原点として棒に沿った座標を $-\dfrac{\ell}{2} \le s \le \dfrac{\ell}{2}$ の $s$ とすると，長さ $\mathrm{d}s$ の微小部分の質量は $\mathrm{d}m = \rho\,\mathrm{d}s = \dfrac{M}{\ell}\,\mathrm{d}s$ であり，回転軸からの距離は $|s|$ です。したがって中点を通り棒に垂直な軸まわりの慣性モーメント $I$ は次式のように積分できます。

$$
\begin{aligned}
I &= \int_{-\ell/2}^{\ell/2} s^2\,\mathrm{d}m \\
&= \frac{M}{\ell}\int_{-\ell/2}^{\ell/2} s^2\,\mathrm{d}s \\
&= \frac{M}{\ell}\left[\frac{s^3}{3}\right]_{-\ell/2}^{\ell/2} \\
&= \frac{M}{\ell}\cdot\frac{\ell^3}{12} \\
&= \frac{1}{12} M \ell^2
\end{aligned}
$$

よって $I = \dfrac{1}{12}M\ell^2$ が証明されました。

### (2)

重力加速度の大きさを $g$ とし，鉛直上向きを $y$ 軸正方向，重力による位置エネルギーの基準を $y = 0$ にとります。剛体の運動エネルギーは重心の並進運動エネルギーと重心まわりの回転運動エネルギーの和で与えられるため，力学的全エネルギー $E$ は $(x, y, \theta)$ を用いて次のように表されます。

$$
E = \frac{1}{2}M(\dot{x}^2 + \dot{y}^2) + \frac{1}{2}I\dot{\theta}^2 + M g y
$$

ここで図の幾何学的配置より，棒の上端は $x$ 軸上の $(\ell\sin\theta, 0)$，下端は $y$ 軸上の $(0, -\ell\cos\theta)$ に位置するため，中点である重心の座標 $(x, y)$ は $\theta$ を用いて次のように表されます。

$$
x = \frac{\ell}{2}\sin\theta, \qquad y = -\frac{\ell}{2}\cos\theta
$$

これらを時間 $t$ で微分します。

$$
\dot{x} = \frac{\ell}{2}\cos\theta\,\dot{\theta}, \qquad \dot{y} = \frac{\ell}{2}\sin\theta\,\dot{\theta}
$$

よって $\dot{x}^2 + \dot{y}^2 = \dfrac{\ell^2}{4}\dot{\theta}^2$ となります。これと $I = \dfrac{1}{12}M\ell^2$ を $E$ に代入すると，$\theta$ のみで表した力学的全エネルギーも得られます。

$$
\begin{aligned}
E &= \frac{1}{2}M\left(\frac{\ell^2}{4}\dot{\theta}^2\right) + \frac{1}{2}\left(\frac{1}{12}M\ell^2\right)\dot{\theta}^2 - \frac{1}{2}M g \ell\cos\theta \\
&= \frac{1}{6}M\ell^2\dot{\theta}^2 - \frac{1}{2}M g \ell\cos\theta
\end{aligned}
$$

$$
\finalanswer{E = \frac{1}{2}M(\dot{x}^2 + \dot{y}^2) + \frac{1}{2}I\dot{\theta}^2 + M g y = \frac{1}{6}M\ell^2\dot{\theta}^2 - \frac{1}{2}M g \ell\cos\theta}
$$

### (3)

棒にはたらく外力は，重心にはたらく重力 $(0, -Mg)$，$x$ 軸上の端点 $(\ell\sin\theta, 0)$ にはたらく抗力 $(0, R_y)$，および $y$ 軸上の端点 $(0, -\ell\cos\theta)$ にはたらく抗力 $(R_x, 0)$ の3つです。ここで $R_x$ は $x$ 軸正方向成分，$R_y$ は $y$ 軸正方向成分として符号を定めます。

重心の並進運動方程式は次式となります。

$$
\begin{aligned}
M\ddot{x} &= R_x \\
M\ddot{y} &= R_y - Mg
\end{aligned}
$$

次に重心まわりの回転運動方程式を立てます。図のように角 $\theta$ が増加すると棒は重心まわりに時計回りに回転するため，時計回りの力のモーメントを正にとります。

- $x$ 軸上の端点の位置は重心から見て $\left(+\dfrac{\ell}{2}\sin\theta,\ +\dfrac{\ell}{2}\cos\theta\right)$ です。ここにはたらく力 $(0, R_y)$ は重心まわりに反時計回りのモーメント $+\dfrac{\ell}{2}R_y\sin\theta$ を与えるため，時計回り方向には $-\dfrac{\ell}{2}R_y\sin\theta$ となります。
- $y$ 軸上の端点の位置は重心から見て $\left(-\dfrac{\ell}{2}\sin\theta,\ -\dfrac{\ell}{2}\cos\theta\right)$ です。ここにはたらく力 $(R_x, 0)$ は重心まわりに反時計回りのモーメント $+\dfrac{\ell}{2}R_x\cos\theta$ を与えるため，時計回り方向には $-\dfrac{\ell}{2}R_x\cos\theta$ となります。

重力は重心にはたらくためモーメントは $0$ です。したがって $\theta$ に対する回転運動方程式は次式になります。

$$
I\ddot{\theta} = -\frac{\ell}{2}\left(R_x\cos\theta + R_y\sin\theta\right)
$$

$$
\finalanswer{M\ddot{x} = R_x,\qquad M\ddot{y} = R_y - Mg,\qquad I\ddot{\theta} = -\frac{\ell}{2}\left(R_x\cos\theta + R_y\sin\theta\right)}
$$

### (4)

(2) で導いた力学的全エネルギー $E = \dfrac{1}{2}M(\dot{x}^2 + \dot{y}^2) + \dfrac{1}{2}I\dot{\theta}^2 + Mgy$ を時間 $t$ で微分し，(3) の運動方程式を代入します。

$$
\begin{aligned}
\frac{\mathrm{d}E}{\mathrm{d}t} &= M\dot{x}\ddot{x} + M\dot{y}\ddot{y} + I\dot{\theta}\ddot{\theta} + Mg\dot{y} \\
&= \dot{x} R_x + \dot{y}(R_y - Mg) - \frac{\ell}{2}\left(R_x\cos\theta + R_y\sin\theta\right)\dot{\theta} + Mg\dot{y} \\
&= R_x\left(\dot{x} - \frac{\ell}{2}\cos\theta\,\dot{\theta}\right) + R_y\left(\dot{y} - \frac{\ell}{2}\sin\theta\,\dot{\theta}\right)
\end{aligned}
$$

ここで拘束条件 $x = \dfrac{\ell}{2}\sin\theta$，$y = -\dfrac{\ell}{2}\cos\theta$ の時間微分より

$$
\dot{x} = \frac{\ell}{2}\cos\theta\,\dot{\theta}, \qquad \dot{y} = \frac{\ell}{2}\sin\theta\,\dot{\theta}
$$

が成り立つため，括弧内はいずれも恒等的に $0$ となります。したがって

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = 0
$$

となり，力学的全エネルギー $E$ が保存することが運動方程式から示されました。これは滑らかな拘束面からの抗力が両端の変位方向と常に直交して仕事をしないことを表しています。

### (5)

(4) より力学的全エネルギー $E = \dfrac{1}{6}M\ell^2\dot{\theta}^2 - \dfrac{1}{2}Mg\ell\cos\theta$ は一定に保たれます。時刻 $t = 0$ では $\theta = 0$，$\dot{\theta} = \omega_0$ なので，初期エネルギーは

$$
E = \frac{1}{6}M\ell^2\omega_0^2 - \frac{1}{2}Mg\ell
$$

です。これを任意の時刻 $t \ge 0$ のエネルギーと等しいとおきます。

$$
\frac{1}{6}M\ell^2\dot{\theta}^2 - \frac{1}{2}Mg\ell\cos\theta = \frac{1}{6}M\ell^2\omega_0^2 - \frac{1}{2}Mg\ell
$$

両辺に $\dfrac{6}{M\ell^2}$ を掛けて $\dot{\theta}^2$ について整理します。

$$
\dot{\theta}^2 = \omega_0^2 - \frac{3g}{\ell}(1 - \cos\theta)
$$

平方根をとると，$t \ge 0$ における棒の角速度 $\dot{\theta}$ が求まります。

$$
\finalanswer{\dot{\theta} = \pm\sqrt{\omega_0^2 - \frac{3g}{\ell}(1 - \cos\theta)}}
$$

ただし，$t = 0$ の直後は正の符号をとり，最高点に達して折り返した後は負の符号をとります。

### (6)

(5) で得られたエネルギー保存式 $\dot{\theta}^2 = \omega_0^2 - \dfrac{3g}{\ell}(1 - \cos\theta)$ の両辺を時間 $t$ で微分します。

$$
2\dot{\theta}\ddot{\theta} = -\frac{3g}{\ell}\sin\theta\,\dot{\theta}
$$

$\dot{\theta}$ が恒等的に $0$ でない運動に対して両辺を $2\dot{\theta}$ で割ると，$\theta$ に関する厳密な運動方程式が得られます。

$$
\ddot{\theta} + \frac{3g}{2\ell}\sin\theta = 0
$$

$|\theta| \ll 1$ の微小角近似では $\sin\theta \approx \theta$ とおけるため，方程式は次の単振動方程式になります。

$$
\ddot{\theta} + \frac{3g}{2\ell}\theta = 0
$$

角振動数を $\Omega = \sqrt{\dfrac{3g}{2\ell}}$ とおくと，一般解は定数 $A, B$ を用いて

$$
\theta(t) = A\cos(\Omega t) + B\sin(\Omega t)
$$

と表されます。初期条件 $\theta(0) = 0$，$\dot{\theta}(0) = \omega_0$ を代入すると，$A = 0$，および $\Omega B = \omega_0$ より $B = \omega_0\sqrt{\dfrac{2\ell}{3g}}$ が決まります。

$$
\finalanswer{\theta(t) = \omega_0\sqrt{\frac{2\ell}{3g}}\sin\left(\sqrt{\frac{3g}{2\ell}}\,t\right)}
$$
