---
title: 東大理物 平成16年度 物理学 第3問：一様磁場と周期電場による荷電粒子の加速
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成16年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成16年度 物理学 第3問：一様磁場と周期電場による荷電粒子の加速

## 問題

電磁場中での電荷 $q$，静止質量 $m$ をもつ粒子の加速を考える。電場 $\vec{E}$，磁場 $\vec{B}$ の下で荷電粒子はローレンツ力

$$
\vec{F} = q(\vec{E} + \vec{v}\times\vec{B}) \tag{1}
$$

を受ける。ここで，$\vec{v}$ は粒子の速度で，磁場 $\vec{B}$ は常に $z$ 軸方向に一様で一定，つまり，$\vec{B} = (0, 0, B)$ とする。また，荷電粒子の運動に伴う電磁波の放出を無視する。

まず，粒子の速度は光速度 $c$ に比べて十分小さく，したがって，相対論的効果を考えなくて良いとする。
{: .problem-lead }

(1) 電場が存在せず，一様な磁場だけがある場合，粒子を時刻 $t = 0$ に初速度 $\vec{v} = (v_0, 0, 0)$ で $\vec{x} = (0, 0, 0)$ から放出した場合にこの粒子の時刻 $t$ での速度と位置を求めよ。

(2) 一様磁場に周期的に変動する電場 $\vec{E} = (-E\sin(\Omega t), -E\cos(\Omega t), 0)$ を加え，設問1と同じ初期条件で荷電粒子を放出した場合，時刻 $t$ での粒子の速度を求めよ。ただし，$E$ は定数である。

(3) $\Omega = qB/m$ のとき十分時間がたてば荷電粒子の運動エネルギーが時間とともに増大することを示せ。

次に，粒子の速度が光速度に比べて無視できない（相対論的）場合を考える。このときは粒子の運動量 $\vec{p}$，エネルギー $\mathcal{E}$ は相対論的表式

$$
\vec{p} = \frac{m\vec{v}}{\sqrt{1 - (v^2/c^2)}}, \qquad \mathcal{E} = \frac{mc^2}{\sqrt{1 - (v^2/c^2)}}
$$

で与えられる。ここで $v = |\vec{v}|$ である。また，相対論的な場合も式 (1) で与えられるローレンツ力 $\vec{F}$ を使って運動方程式は $\mathrm{d}\vec{p}/\mathrm{d}t = \vec{F}$ と書ける。

(4) 設問1と同じく一様な磁場だけがあり，電場がない場合，粒子の速度が相対論的のときも，運動方程式の両辺と速度 $\vec{v}$ との内積をとることによって粒子の速さ $v$ が運動中一定であることを示せ。

(5) 前問までの結果を使って運動方程式を解き，粒子の速度 $\vec{v}(t)$ を求めよ。

(6) 相対論的な場合の結果を考慮して，設問3と同じく一様な磁場と振動数 $\Omega = qB/m$ で変動する電場が存在する場合，粒子の運動エネルギー（$\mathcal{E} - mc^2$）の増加はとまる。その理由を述べよ。ただし，最初荷電粒子の速度は光速に比べて小さいとして，具体的に相対論的な運動方程式を解く必要はない。

> 出典：東京大学大学院理学系研究科物理学専攻 平成16年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
一様磁場 $\vec{B} = (0, 0, B)$ のもとでの $xy$ 平面内の運動方程式は，複素速度 $w(t) = v_x(t) + i v_y(t)$ を導入すると1本の1階線形常微分方程式にまとまります。そのため回転電場が加わった場合でも，定数変化法や積分因子によって共鳴時と非共鳴時の解をまとめて求めることができます。

一様磁場のみの場合，ローレンツ力は速度に常に垂直で仕事をしないため，相対論的な運動方程式でも粒子の速さ $v$ とローレンツ因子 $\gamma$ が一定に保たれます。これにより相対論的な運動は質量を $\gamma m$ に置き換えた非相対論的サイクロトロン運動と同じ形になり，高速化に伴う角周波数の低下から加速が止まる理由がわかります。
</div>

### (1)

$\vec{E} = \vec{0}$，$\vec{B} = (0, 0, B)$ のとき，$\vec{v}\times\vec{B} = (v_y B, -v_x B, 0)$ です。$\omega = \dfrac{qB}{m}$ とおくと，運動方程式の各成分は次式になります。

$$
\frac{\mathrm{d}v_x}{\mathrm{d}t} = \omega v_y, \qquad \frac{\mathrm{d}v_y}{\mathrm{d}t} = -\omega v_x, \qquad \frac{\mathrm{d}v_z}{\mathrm{d}t} = 0
$$

複素速度 $w(t) = v_x(t) + i v_y(t)$ を導入すると，最初の2式は1つの式にまとまります。

$$
\begin{aligned}
\frac{\mathrm{d}w}{\mathrm{d}t} &= \omega v_y - i\omega v_x \\
&= -i\omega(v_x + i v_y) \\
&= -i\omega w
\end{aligned}
$$

初期条件 $w(0) = v_0$ のもとで積分すると $w(t) = v_0 e^{-i\omega t} = v_0\cos(\omega t) - i v_0\sin(\omega t)$ です。また $v_z(0) = 0$ より $v_z(t) = 0$ なので，時刻 $t$ での速度 $\vec{v}(t)$ は次式になります。

$$
\vec{v}(t) = \bigl(v_0\cos(\omega t),\ -v_0\sin(\omega t),\ 0\bigr)
$$

これを初期位置 $\vec{x}(0) = (0, 0, 0)$ から時刻 $t$ まで積分して位置を求めます。

$$
\begin{aligned}
x(t) &= \int_{0}^{t} v_0\cos(\omega t')\,\mathrm{d}t' \\
&= \frac{v_0}{\omega}\sin(\omega t)
\end{aligned}
$$

$$
\begin{aligned}
y(t) &= \int_{0}^{t} \bigl(-v_0\sin(\omega t')\bigr)\,\mathrm{d}t' \\
&= \frac{v_0}{\omega}\bigl(\cos(\omega t) - 1\bigr)
\end{aligned}
$$

$z(t) = 0$ なので，$\omega = \dfrac{qB}{m}$ を用いて速度と位置は次式となります。

$$
\finalanswer{\vec{v}(t) = \left(v_0\cos\frac{qB}{m}t,\ -v_0\sin\frac{qB}{m}t,\ 0\right), \qquad \vec{x}(t) = \left(\frac{mv_0}{qB}\sin\frac{qB}{m}t,\ \frac{mv_0}{qB}\left(\cos\frac{qB}{m}t - 1\right),\ 0\right)}
$$

### (2)

$\vec{E} = (-E\sin(\Omega t), -E\cos(\Omega t), 0)$ を加えると，運動方程式の $x, y, z$ 成分は次式になります。

$$
\frac{\mathrm{d}v_x}{\mathrm{d}t} = \omega v_y - \frac{qE}{m}\sin(\Omega t), \qquad \frac{\mathrm{d}v_y}{\mathrm{d}t} = -\omega v_x - \frac{qE}{m}\cos(\Omega t), \qquad \frac{\mathrm{d}v_z}{\mathrm{d}t} = 0
$$

$v_z(0) = 0$ より $v_z(t) = 0$ です。設問1と同様に $w(t) = v_x(t) + i v_y(t)$ を導入し，運動方程式を1本にまとめます。

$$
\begin{aligned}
\frac{\mathrm{d}w}{\mathrm{d}t} &= -i\omega w - \frac{qE}{m}\bigl(\sin(\Omega t) + i\cos(\Omega t)\bigr) \\
&= -i\omega w - i\frac{qE}{m}\bigl(\cos(\Omega t) - i\sin(\Omega t)\bigr) \\
&= -i\omega w - i\frac{qE}{m}e^{-i\Omega t}
\end{aligned}
$$

両辺に $e^{i\omega t}$ を掛けてまとめます。

$$
\frac{\mathrm{d}}{\mathrm{d}t}\bigl(e^{i\omega t}w(t)\bigr) = -i\frac{qE}{m}e^{i(\omega - \Omega)t}
$$

初期条件 $w(0) = v_0$ のもとで $0$ から $t$ まで積分します。$\Omega \neq \omega$ の場合と $\Omega = \omega$ の場合に分けて計算します。

まず $\Omega \neq \omega$ のとき，右辺を積分します。

$$
\begin{aligned}
e^{i\omega t}w(t) - v_0 &= -i\frac{qE}{m}\left[\frac{e^{i(\omega - \Omega)t'}}{i(\omega - \Omega)}\right]_{0}^{t} \\
&= -\frac{qE}{m(\omega - \Omega)}\bigl(e^{i(\omega - \Omega)t} - 1\bigr)
\end{aligned}
$$

両辺に $e^{-i\omega t}$ を掛けると $w(t)$ が得られます。

$$
\begin{aligned}
w(t) &= v_0 e^{-i\omega t} + \frac{qE}{m(\omega - \Omega)}\bigl(e^{-i\omega t} - e^{-i\Omega t}\bigr)
\end{aligned}
$$

実部と虚部をとると，$v_x(t)$ と $v_y(t)$ は次式になります。

$$
\begin{aligned}
v_x(t) &= v_0\cos(\omega t) + \frac{qE}{m(\omega - \Omega)}\bigl(\cos(\omega t) - \cos(\Omega t)\bigr) \\
v_y(t) &= -v_0\sin(\omega t) - \frac{qE}{m(\omega - \Omega)}\bigl(\sin(\omega t) - \sin(\Omega t)\bigr)
\end{aligned}
$$

次に $\Omega = \omega$ のとき，右辺は定数 $-i\dfrac{qE}{m}$ なので積分は次式になります。

$$
e^{i\omega t}w(t) - v_0 = -i\frac{qE}{m}t
$$

両辺に $e^{-i\omega t}$ を掛けます。

$$
\begin{aligned}
w(t) &= \left(v_0 - i\frac{qE}{m}t\right)e^{-i\omega t} \\
&= \left(v_0\cos(\omega t) - \frac{qE}{m}t\sin(\omega t)\right) + i\left(-v_0\sin(\omega t) - \frac{qE}{m}t\cos(\omega t)\right)
\end{aligned}
$$

したがって，$\omega = \dfrac{qB}{m}$ を用いて速度 $\vec{v}(t) = (v_x(t), v_y(t), 0)$ は次のようになります。

$$
\finalanswer{
\begin{aligned}
\Omega \neq \omega &: \quad v_x(t) = v_0\cos(\omega t) + \frac{qE}{m(\omega - \Omega)}\bigl(\cos(\omega t) - \cos(\Omega t)\bigr), \\
&\phantom{: \quad} v_y(t) = -v_0\sin(\omega t) - \frac{qE}{m(\omega - \Omega)}\bigl(\sin(\omega t) - \sin(\Omega t)\bigr), \quad v_z(t) = 0 \\
\Omega = \omega &: \quad v_x(t) = v_0\cos(\omega t) - \frac{qE}{m}t\sin(\omega t), \\
&\phantom{: \quad} v_y(t) = -v_0\sin(\omega t) - \frac{qE}{m}t\cos(\omega t), \quad v_z(t) = 0
\end{aligned}
}
$$

### (3)

$\Omega = \omega = \dfrac{qB}{m}$ のとき，設問2で得た $w(t) = \left(v_0 - i\dfrac{qE}{m}t\right)e^{-i\omega t}$ を用いて速さの2乗 $|\vec{v}(t)|^2 = |w(t)|^2$ を計算します。

$$
\begin{aligned}
|\vec{v}(t)|^2 &= \left|\left(v_0 - i\frac{qE}{m}t\right)e^{-i\omega t}\right|^2 \\
&= \left|v_0 - i\frac{qE}{m}t\right|^2 \\
&= v_0^2 + \left(\frac{qE}{m}t\right)^2
\end{aligned}
$$

したがって，時刻 $t$ における荷電粒子の運動エネルギー $K(t) = \dfrac{1}{2}m|\vec{v}(t)|^2$ は次式になります。

$$
K(t) = \frac{1}{2}m v_0^2 + \frac{q^2 E^2}{2m}t^2
$$

$qE \neq 0$ より第2項は $t^2$ に比例して正の値をとりながら単調に増加します。よって荷電粒子の運動エネルギーは時間とともに増大します。

### (4)

電場がないときの相対論的運動方程式は $\dfrac{\mathrm{d}\vec{p}}{\mathrm{d}t} = q(\vec{v}\times\vec{B})$ です。両辺と速度 $\vec{v}$ の内積をとります。

右辺は $\vec{v}\times\vec{B}$ が $\vec{v}$ に垂直なため $0$ です。

$$
\vec{v}\cdot\bigl(q(\vec{v}\times\vec{B})\bigr) = 0
$$

左辺を $\gamma = \left(1 - \dfrac{v^2}{c^2}\right)^{-1/2}$ を用いて計算します。$\vec{p} = m\gamma\vec{v}$ であり，$\dfrac{\mathrm{d}\gamma}{\mathrm{d}t} = \gamma^3\dfrac{\vec{v}\cdot\dot{\vec{v}}}{c^2}$ です。

$$
\begin{aligned}
\vec{v}\cdot\frac{\mathrm{d}\vec{p}}{\mathrm{d}t} &= \vec{v}\cdot\left(m\gamma\dot{\vec{v}} + m\gamma^3\frac{\vec{v}\cdot\dot{\vec{v}}}{c^2}\vec{v}\right) \\
&= m\gamma(\vec{v}\cdot\dot{\vec{v}})\left(1 + \gamma^2\frac{v^2}{c^2}\right) \\
&= m\gamma(\vec{v}\cdot\dot{\vec{v}})\left(1 + \frac{v^2/c^2}{1 - v^2/c^2}\right) \\
&= m\gamma^3(\vec{v}\cdot\dot{\vec{v}}) \\
&= \frac{\mathrm{d}}{\mathrm{d}t}\bigl(\gamma mc^2\bigr)
\end{aligned}
$$

したがって $\dfrac{\mathrm{d}\mathcal{E}}{\mathrm{d}t} = 0$ となり，エネルギー $\mathcal{E} = \dfrac{mc^2}{\sqrt{1 - v^2/c^2}}$ は運動中一定です。$\mathcal{E}$ は $v \ge 0$ の単調増加関数なので，粒子の速さ $v$ も運動中一定です。

### (5)

設問4より，粒子の速さ $v$ は初期値 $v_0$ のまま一定なので，ローレンツ因子 $\gamma_0 = \dfrac{1}{\sqrt{1 - v_0^2/c^2}}$ も時間によらない定数になります。したがって，相対論的運動方程式は次のように書くことができます。

$$
\gamma_0 m\frac{\mathrm{d}\vec{v}}{\mathrm{d}t} = q(\vec{v}\times\vec{B})
$$

これは設問1の非相対論的運動方程式において，質量 $m$ を $\gamma_0 m$ に置き換えたものと全く同じです。角周波数を

$$
\begin{aligned}
\omega_{\mathrm{rel}} &= \frac{qB}{\gamma_0 m} \\
&= \frac{qB}{m}\sqrt{1 - \frac{v_0^2}{c^2}}
\end{aligned}
$$

とおくと，初期条件 $\vec{v}(0) = (v_0, 0, 0)$ のもとでの解は次式となります。

$$
\finalanswer{\vec{v}(t) = \bigl(v_0\cos(\omega_{\mathrm{rel}} t),\ -v_0\sin(\omega_{\mathrm{rel}} t),\ 0\bigr), \qquad \omega_{\mathrm{rel}} = \frac{qB}{m}\sqrt{1 - \frac{v_0^2}{c^2}}}
$$

### (6)

最初は荷電粒子の速さ $v$ が光速 $c$ に比べて十分小さいため，磁場中での回転の角周波数 $\omega_{\mathrm{rel}} = \dfrac{qB}{m}\sqrt{1 - v^2/c^2}$ は電場の角周波数 $\Omega = \dfrac{qB}{m}$ にほぼ一致します。そのため粒子は電場と同期して回転しながら加速され，運動エネルギーが増加します。

しかし加速が進んで速さ $v$ が大きくなると，設問5の結果の通り相対論的効果によって粒子の回転の角周波数 $\omega_{\mathrm{rel}}$ が $\Omega = \dfrac{qB}{m}$ より小さくなります。すると粒子と電場の位相の同期が崩れて次第にずれが広がり，やがて粒子が電場から減速される向きに力を受ける位相に入るため，運動エネルギーの増加は止まります。
