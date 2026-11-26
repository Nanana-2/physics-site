---
title: 東大理物 平成17年度 物理学 第3問：単色平面波中の自由電子の運動とポンデロモーティブエネルギー
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成17年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成17年度 物理学 第3問：単色平面波中の自由電子の運動とポンデロモーティブエネルギー

## 問題

真空中で，高い強度の単色光（電磁波）と自由電子（質量 $m$，電荷 $-e$）との相互作用を考える。電子にはたらく力 $\boldsymbol{F} = -e(\boldsymbol{E} + \boldsymbol{v}\times\boldsymbol{B})$（$\boldsymbol{E}, \boldsymbol{B}$ はそれぞれ光の電場と磁束密度，$\boldsymbol{v}$ は電子の速度）のうち，光の磁場成分と電子との相互作用の寄与が十分小さいのはどのような場合かを具体的に考察しよう。空間内のある点で，$x$ 方向に直線偏光した角振動数 $\omega$ を持つ単色平面波の電場を $E_x = E_0\sin\omega t$ と表すとき，以下の設問に答えよ。ただし，真空中での光の速さを $c$ とする。

(1) 光の電場の振幅 $E_0$ と磁束密度の振幅 $B_0$ の比 $E_0/B_0$ が $c$ であることに注意し，電子にはたらく力のうち，光の磁場成分と電子との相互作用の寄与が十分小さくなるための $\boldsymbol{v}$ の大きさに関する条件を求めよ。

以下の設問2, 3, 5では，設問1で考察した光の磁場成分と電子との相互作用の寄与が十分小さく，無視してよい場合を考える。

(2) 時刻 $t = t_0$ で電子の速度が $0$ であったとする。時刻 $t > t_0$ における光の電場 $E_x$ 中での電子の運動エネルギーを求めよ。

(3) 設問2で求めた運動エネルギーについて，光の電場の1周期 $T = 2\pi/\omega$ にわたる平均を求めよ。また，求めた平均が取りうる最小値を明示し，その物理的意味を簡潔に説明せよ。時間に依存するある物理量 $u(t)$ の1周期にわたる平均 $\langle u(t) \rangle$ は，

$$
\langle u(t) \rangle = \frac{1}{T}\int_{t}^{t + T} u(t')\,\mathrm{d}t'
$$

で定義される。

(4) 光の強度 $I\ [\mathrm{W/m^2}]$ がポインティングベクトル $\boldsymbol{S} = \boldsymbol{E}\times(\boldsymbol{B}/\mu_0)$（$\mu_0$ は真空の透磁率）の大きさの1周期平均に相当することに注意し，電場の振幅 $E_0$ を光の強度 $I$ と $Z_0 = \sqrt{\mu_0/\epsilon_0}$（$\epsilon_0$ は真空の誘電率）を含む式で表せ。$Z_0$ は真空の放射インピーダンスと呼ばれる。

(5) 電子の運動エネルギーについて，設問3で求めた平均が取りうる最小値を $U$ と書く。設問4の結果を用い，$U\ [\mathrm{J}]$ の表式を，光の強度 $I\ [\mathrm{W/m^2}]$，その波長 $\lambda\ [\mathrm{m}]$，電子の質量 $m\ [\mathrm{kg}]$ と電荷の大きさ $e\ [\mathrm{C}]$，光の速さ $c\ [\mathrm{m/s}]$，および $Z_0$ を用いて表せ。

(6) 設問5で得られた $U$ の表式に光の強度 $I$ と波長 $\lambda$ 以外の物理量を代入すると，数値係数は $1.5\times 10^{-24}\,\mathrm{s}$ となる。いま，$\lambda = 0.8\,\mu\mathrm{m} = 8\times 10^{-7}\,\mathrm{m}$ のとき，$I < 10^{18}\,\mathrm{W/m^2}$ であれば，設問1で考察したように，電子にはたらく力のうち，光の磁場成分と電子との相互作用の寄与が十分小さいことを示せ。ただし，$m = 9\times 10^{-31}\,\mathrm{kg}$ とする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成17年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
真空中の平面電磁波では磁束密度の振幅 $B_0$ が電場の振幅 $E_0$ の $1/c$ 倍になるため，ローレンツ力の磁気力と電気力の大きさの比の上界は電子の速さと光速の比 $v/c$ になります。そのため電子が非相対論的な速さで動く範囲では，磁場からの力を無視して1次元の運動方程式をそのまま積分することができます。

電子が電場から受ける振動運動の平均エネルギーは，光の強度 $I$ と波長 $\lambda$ で表すことができます。この平均エネルギーを電子の静止エネルギー $mc^2$ と比べることで，$v \ll c$ が成り立つ光強度の範囲を数値的に確かめることができます。
</div>

### (1)

電子にはたらく電気力の振幅は $F_E = e E_0$ です。一方，磁場成分による力の大きさは $|\boldsymbol{v}\times\boldsymbol{B}| \le |\boldsymbol{v}|B_0$ であり，$B_0 = \dfrac{E_0}{c}$ を用いると次の不等式が成り立ちます。

$$
\begin{aligned}
F_B &= e|\boldsymbol{v}\times\boldsymbol{B}| \\
&\le e|\boldsymbol{v}|B_0 \\
&= e|\boldsymbol{v}|\frac{E_0}{c}
\end{aligned}
$$

電気力との大きさの比は次式になります。

$$
\frac{F_B}{F_E} \le \frac{|\boldsymbol{v}|}{c}
$$

したがって，磁場成分と電子との相互作用の寄与が十分小さくなるための条件は次式となります。

$$
\finalanswer{|\boldsymbol{v}| \ll c}
$$

### (2)

磁場からの力を無視すると，電子には $x$ 方向の電気力のみがはたらきます。時刻 $t = t_0$ で速度が $0$ なので $y, z$ 方向の速度は常に $0$ であり，$x$ 方向の運動方程式は次式になります。

$$
m\frac{\mathrm{d}v_x}{\mathrm{d}t} = -e E_0\sin\omega t
$$

両辺を $t_0$ から $t$ まで積分し，$v_x(t_0) = 0$ を用います。

$$
\begin{aligned}
v_x(t) &= -\frac{e E_0}{m}\int_{t_0}^{t} \sin\omega t'\,\mathrm{d}t' \\
&= -\frac{e E_0}{m}\left[-\frac{\cos\omega t'}{\omega}\right]_{t_0}^{t} \\
&= \frac{e E_0}{m\omega}\bigl(\cos\omega t - \cos\omega t_0\bigr)
\end{aligned}
$$

したがって，時刻 $t > t_0$ における電子の運動エネルギー $K(t) = \dfrac{1}{2}m v_x(t)^2$ は次式となります。

$$
\finalanswer{K(t) = \frac{e^2 E_0^2}{2m\omega^2}\bigl(\cos\omega t - \cos\omega t_0\bigr)^2}
$$

### (3)

設問2で求めた $K(t)$ を展開します。

$$
K(t') = \frac{e^2 E_0^2}{2m\omega^2}\bigl(\cos^2\omega t' - 2\cos\omega t_0\cos\omega t' + \cos^2\omega t_0\bigr)
$$

1周期 $T = \dfrac{2\pi}{\omega}$ にわたる三角関数の平均を計算します。

$$
\begin{aligned}
\frac{1}{T}\int_{t}^{t + T} \cos\omega t'\,\mathrm{d}t' &= \frac{1}{T}\left[\frac{\sin\omega t'}{\omega}\right]_{t}^{t + 2\pi/\omega} \\
&= 0
\end{aligned}
$$

$$
\begin{aligned}
\frac{1}{T}\int_{t}^{t + T} \cos^2\omega t'\,\mathrm{d}t' &= \frac{1}{T}\int_{t}^{t + T} \frac{1 + \cos 2\omega t'}{2}\,\mathrm{d}t' \\
&= \frac{1}{2}
\end{aligned}
$$

これらを用いて運動エネルギーの1周期平均 $\langle K(t) \rangle$ を計算します。

$$
\begin{aligned}
\langle K(t) \rangle &= \frac{e^2 E_0^2}{2m\omega^2}\left(\frac{1}{2} - 0 + \cos^2\omega t_0\right) \\
&= \frac{e^2 E_0^2}{4m\omega^2}\bigl(1 + 2\cos^2\omega t_0\bigr)
\end{aligned}
$$

$\cos^2\omega t_0 \ge 0$ なので，$\langle K(t) \rangle$ は $\cos\omega t_0 = 0$ のときに最小値 $\dfrac{e^2 E_0^2}{4m\omega^2}$ をとります。

$$
\finalanswer{\langle K(t) \rangle = \frac{e^2 E_0^2}{4m\omega^2}\bigl(1 + 2\cos^2\omega t_0\bigr), \qquad \langle K(t) \rangle_{\min} = \frac{e^2 E_0^2}{4m\omega^2}}
$$

電子の速度 $v_x(t) = \dfrac{e E_0}{m\omega}\cos\omega t - \dfrac{e E_0}{m\omega}\cos\omega t_0$ は，電場と同期して往復する振動運動と，初期位相 $t_0$ で決まる一定の並進運動の和になっています。1周期平均の運動エネルギーは振動運動の平均エネルギーと並進運動のエネルギーの和であり，最小値 $\dfrac{e^2 E_0^2}{4m\omega^2}$ は並進速度が $0$ であるときの純粋な振動運動の平均運動エネルギーを表します。

### (4)

真空中の単色平面波では $\boldsymbol{E}$ と $\boldsymbol{B}$ が互いに直交し，$|\boldsymbol{B}| = \dfrac{|\boldsymbol{E}|}{c} = \sqrt{\epsilon_0\mu_0}\,|\boldsymbol{E}|$ が成り立ちます。これよりポインティングベクトル $\boldsymbol{S} = \boldsymbol{E}\times(\boldsymbol{B}/\mu_0)$ の大きさを計算します。

$$
\begin{aligned}
|\boldsymbol{S}| &= \frac{|\boldsymbol{E}||\boldsymbol{B}|}{\mu_0} \\
&= \sqrt{\frac{\epsilon_0}{\mu_0}}\,E_x^2 \\
&= \frac{E_0^2}{Z_0}\sin^2\omega t
\end{aligned}
$$

$\sin^2\omega t$ の1周期平均は $\dfrac{1}{2}$ なので，光の強度 $I = \langle |\boldsymbol{S}| \rangle$ は次式になります。

$$
I = \frac{E_0^2}{2Z_0}
$$

これを $E_0 > 0$ について解くと，次式となります。

$$
\finalanswer{E_0 = \sqrt{2Z_0 I}}
$$

### (5)

波長 $\lambda$ と角振動数 $\omega$ の関係は $\omega = \dfrac{2\pi c}{\lambda}$ です。これと設問4の $E_0^2 = 2Z_0 I$ を，設問3で求めた最小値 $U = \dfrac{e^2 E_0^2}{4m\omega^2}$ に代入します。

$$
\begin{aligned}
U &= \frac{e^2 (2Z_0 I)}{4m\left(\dfrac{2\pi c}{\lambda}\right)^2} \\
&= \frac{2e^2 Z_0 I \lambda^2}{16\pi^2 m c^2} \\
&= \frac{e^2 Z_0}{8\pi^2 m c^2}\,I\lambda^2
\end{aligned}
$$

したがって，$U$ の表式は次式となります。

$$
\finalanswer{U = \frac{e^2 Z_0}{8\pi^2 m c^2}\,I\lambda^2}
$$

### (6)

設問5の表式に与えられた数値係数 $1.5\times 10^{-24}\,\mathrm{s}$ と $\lambda = 8\times 10^{-7}\,\mathrm{m}$，$I < 10^{18}\,\mathrm{W/m^2}$ を代入して $U$ の上限を計算します。

$$
\begin{aligned}
U &< 1.5\times 10^{-24} \times 10^{18} \times \bigl(8\times 10^{-7}\bigr)^2 \\
&= 1.5\times 10^{-6} \times 6.4\times 10^{-13} \\
&= 9.6\times 10^{-19}\,\mathrm{J}
\end{aligned}
$$

ここで，ドリフト速度が $0$ のときの電子の振動速度の振幅を $v_{\max} = \dfrac{e E_0}{m\omega}$ とすると，$U = \dfrac{1}{4}m v_{\max}^2$ の関係があります。これより $\dfrac{v_{\max}}{c}$ の大きさを求めます。$m = 9\times 10^{-31}\,\mathrm{kg}$，$c = 3\times 10^{8}\,\mathrm{m/s}$ を用いて $mc^2$ を計算します。

$$
\begin{aligned}
mc^2 &= 9\times 10^{-31} \times \bigl(3\times 10^{8}\bigr)^2 \\
&= 8.1\times 10^{-14}\,\mathrm{J}
\end{aligned}
$$

これを用いて $\dfrac{v_{\max}}{c}$ の上限を求めます。

$$
\begin{aligned}
\frac{v_{\max}}{c} &= \sqrt{\frac{4U}{mc^2}} \\
&< \sqrt{\frac{4 \times 9.6\times 10^{-19}}{8.1\times 10^{-14}}} \\
&= \sqrt{4.74\times 10^{-5}} \\
&\simeq 6.9\times 10^{-3} \ll 1
\end{aligned}
$$

初期位相 $t_0$ による並進成分を含めても速度の最大値は高々 $2v_{\max}$ であり，依然として $\dfrac{|\boldsymbol{v}|}{c} \lesssim 10^{-2} \ll 1$ が成り立ちます。したがって設問1の条件 $|\boldsymbol{v}| \ll c$ が満たされ，光の磁場成分と電子との相互作用の寄与は十分小さいことがわかります。
