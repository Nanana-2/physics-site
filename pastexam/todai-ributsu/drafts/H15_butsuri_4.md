---
title: 東大理物 平成15年度 物理学 第4問：剛体球の慣性モーメントと平面・斜面上の転がり運動
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成15年度
exam_subject: 物理学
exam_number: 第4問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成15年度 物理学 第4問：剛体球の慣性モーメントと平面・斜面上の転がり運動

## 問題

(1) 半径 $a$，厚さ $d$（$\ll a$），一様な密度 $\rho$ の薄い円板の，中心をとおり面に垂直な軸のまわりの慣性モーメント $I_z$，および中心を通り面に平行な軸のまわりの慣性モーメント $I_x$ を求めよ。

(2) 半径 $a$，質量 $M$ の一様な球の，質量中心を通る軸のまわりの慣性モーメントが

$$
I = \frac{2}{5}Ma^2
$$

であることを示せ。

(3) この球を摩擦のある水平な面に置き，中心の高さを中心に向かって水平に突いて初速 $v_0$ を与えた。球と面の静止摩擦係数を $\mu$，動摩擦係数を $\mu'$ とするとき，球が滑らずに転がるようになるまでの時間と，それまでに質量中心が進む距離を求めよ。また滑らずに転がるようになってからの質量中心の速さ $v$ と回転の角速度 $\omega$ を求めよ。ただし，以下の設問も含め，転がり摩擦は無視するものとする。

(4) 図1のように，面が前方で傾斜角 $\theta$ の上り斜面になっているとする。$\theta$ がある値より大きいと，滑らずに転がってきた球は滑りながら斜面を上るようになる。その $\theta$ の値を求めよ。ただし，斜面の下端は図1のように十分短い範囲で緩やかに変化しており，斜面全体にわたって摩擦係数は水平な部分と同じであるとする。

<figure class="problem-figure" markdown>
![水平面から傾斜角thetaの上り斜面へ進む転がり球](../../../docs/assets/figures/pastexam-todai-ributsu/H15_butsuri_4-p-light.svg#only-light)
![水平面から傾斜角thetaの上り斜面へ進む転がり球](../../../docs/assets/figures/pastexam-todai-ributsu/H15_butsuri_4-p-dark.svg#only-dark)
<figcaption markdown="span">図1：水平面を滑らずに転がってきた球と傾斜角 $\theta$ の上り斜面。</figcaption>
</figure>

(5) 前方の斜面の部分に摩擦があり球が滑らずに転がって上る場合と，斜面の部分が滑らかで摩擦がない場合では，球はどちらが高くまで上ることができるか。理由を付けて簡単に説明せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成15年度 物理学 第4問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，薄い円板の慣性モーメントを極座標積分と直交軸の定理から求め，球を薄い円板の積み重ねとみなして積分することで球の慣性モーメント $I = \dfrac{2}{5}Ma^2$ を導きます。

後半では，並進の運動方程式と重心まわりの回転の運動方程式を連立させ，滑りの有無を摩擦力の向きと大きさに注意して解析します。斜面上の到達高さの比較は，並進と回転の運動エネルギーがそれぞれ位置エネルギーへ変換されるかどうかで判断します。
</div>

### (1)

円板の中心を原点とし，円板を含む面を $xy$ 平面，面に垂直な軸を $z$ 軸とします。半径 $r$ から $r + \mathrm{d}r$ の薄い円環の質量は $\mathrm{d}m = 2\pi r d\rho\,\mathrm{d}r$ なので，$z$ 軸まわりの慣性モーメント $I_z$ は次式になります。

$$
\begin{aligned}
I_z &= \int_{0}^{a} r^2\,(2\pi r d\rho)\,\mathrm{d}r \\
&= 2\pi\rho d\left[\frac{r^4}{4}\right]_{0}^{a} \\
&= \frac{1}{2}\pi\rho d a^4
\end{aligned}
$$

円板の厚さは $d \ll a$ なので平面物体とみなすことができ，直交軸の定理 $I_z = I_x + I_y$ が成り立ちます。対称性より $I_x = I_y$ なので，$I_x = \dfrac{1}{2}I_z$ です。

$$
\finalanswer{I_z = \frac{1}{2}\pi\rho d a^4, \qquad I_x = \frac{1}{4}\pi\rho d a^4}
$$

### (2)

球の中心を原点とし，$z$ 軸に垂直な面で球を厚さ $\mathrm{d}z$ の薄い円板に分割します。高さ $z$（$-a \le z \le a$）にある円板の半径は $\sqrt{a^2 - z^2}$ なので，設問 (1) の $I_z$ の結果を用いて $z$ 軸まわりの慣性モーメント $I$ を積分します。

$$
\begin{aligned}
I &= \int_{-a}^{a} \frac{1}{2}\pi\rho\bigl(a^2 - z^2\bigr)^2\,\mathrm{d}z \\
&= \pi\rho\int_{0}^{a} \bigl(a^4 - 2a^2 z^2 + z^4\bigr)\mathrm{d}z \\
&= \pi\rho\left[a^4 z - \frac{2}{3}a^2 z^3 + \frac{1}{5}z^5\right]_{0}^{a} \\
&= \frac{8}{15}\pi\rho a^5
\end{aligned}
$$

一様な球の体積は $\dfrac{4}{3}\pi a^3$ なので，密度は $\rho = \dfrac{3M}{4\pi a^3}$ です。これを代入します。

$$
\begin{aligned}
I &= \frac{8}{15}\pi a^5 \cdot \frac{3M}{4\pi a^3} \\
&= \frac{2}{5}Ma^2
\end{aligned}
$$

これで $I = \dfrac{2}{5}Ma^2$ が成り立つことがわかります。

### (3)

球の進行方向を $+x$ 方向，重力加速度を $g$ とします。時刻 $t = 0$ で質量中心の速度は $v(0) = v_0$，回転角速度は $\omega(0) = 0$ です。滑らずに転がる条件 $v = a\omega$ に達するまでは接触点が $+x$ 方向に滑るため，面から $-x$ 方向に動摩擦力 $f = \mu' Mg$ がはたらきます。

質量中心の並進の運動方程式と重心まわりの回転の運動方程式を立てます。

$$
M\frac{\mathrm{d}v}{\mathrm{d}t} = -\mu' Mg, \qquad I\frac{\mathrm{d}\omega}{\mathrm{d}t} = a\mu' Mg
$$

$I = \dfrac{2}{5}Ma^2$ を代入してそれぞれの加速度を求めます。

$$
\frac{\mathrm{d}v}{\mathrm{d}t} = -\mu' g, \qquad \frac{\mathrm{d}\omega}{\mathrm{d}t} = \frac{5\mu' g}{2a}
$$

初期条件 $v(0) = v_0$，$\omega(0) = 0$ のもとで時刻 $t$ まで積分します。

$$
v(t) = v_0 - \mu' g t, \qquad \omega(t) = \frac{5\mu' g}{2a}t
$$

時刻 $t_1$ で滑らずに転がり始める条件 $v(t_1) = a\omega(t_1)$ を立てます。

$$
v_0 - \mu' g t_1 = \frac{5}{2}\mu' g t_1
$$

移項して整理します。

$$
\frac{7}{2}\mu' g t_1 = v_0
$$

これを $t_1$ について解きます。

$$
t_1 = \frac{2v_0}{7\mu' g}
$$

時刻 $t_1$ までに質量中心が進む距離 $x_1$ を計算します。

$$
\begin{aligned}
x_1 &= v_0 t_1 - \frac{1}{2}\mu' g t_1^2 \\
&= v_0\left(\frac{2v_0}{7\mu' g}\right) - \frac{1}{2}\mu' g\left(\frac{2v_0}{7\mu' g}\right)^2 \\
&= \frac{2v_0^2}{7\mu' g} - \frac{2v_0^2}{49\mu' g} \\
&= \frac{12 v_0^2}{49\mu' g}
\end{aligned}
$$

時刻 $t_1$ 以降は摩擦力が $0$ となり，速さ $v$ と角速度 $\omega$ は一定に保たれます。$t = t_1$ を代入して求めます。

$$
\begin{aligned}
v &= v_0 - \mu' g\cdot\frac{2v_0}{7\mu' g} \\
&= \frac{5}{7}v_0
\end{aligned}
$$

$$
\begin{aligned}
\omega &= \frac{v}{a} \\
&= \frac{5v_0}{7a}
\end{aligned}
$$

以上をまとめると，求める各量は次式となります。

$$
\finalanswer{t_1 = \frac{2v_0}{7\mu' g}, \qquad x_1 = \frac{12 v_0^2}{49\mu' g}, \qquad v = \frac{5}{7}v_0, \qquad \omega = \frac{5v_0}{7a}}
$$

### (4)

斜面に沿って上向きに座標 $s$ をとり，斜面を上る向きの回転角速度を $\omega$ とします。斜面から球にはたらく静止摩擦力を斜面上向きを正として $f$ とおきます。並進と回転の運動方程式は次式です。

$$
M\frac{\mathrm{d}^2 s}{\mathrm{d}t^2} = -Mg\sin\theta + f, \qquad I\frac{\mathrm{d}\omega}{\mathrm{d}t} = -af
$$

滑らずに転がる条件 $\dfrac{\mathrm{d}^2 s}{\mathrm{d}t^2} = a\dfrac{\mathrm{d}\omega}{\mathrm{d}t}$ と $I = \dfrac{2}{5}Ma^2$ を第2式に代入して $f$ を表します。

$$
f = -\frac{2}{5}M\frac{\mathrm{d}^2 s}{\mathrm{d}t^2}
$$

これを第1式に代入します。

$$
M\frac{\mathrm{d}^2 s}{\mathrm{d}t^2} = -Mg\sin\theta - \frac{2}{5}M\frac{\mathrm{d}^2 s}{\mathrm{d}t^2}
$$

移項して整理します。

$$
\frac{7}{5}M\frac{\mathrm{d}^2 s}{\mathrm{d}t^2} = -Mg\sin\theta
$$

よって $\dfrac{\mathrm{d}^2 s}{\mathrm{d}t^2} = -\dfrac{5}{7}g\sin\theta$ であり，必要な静止摩擦力 $f$ は次式になります。

$$
\begin{aligned}
f &= -\frac{2}{5}M\left(-\frac{5}{7}g\sin\theta\right) \\
&= \frac{2}{7}Mg\sin\theta
\end{aligned}
$$

垂直抗力は $N = Mg\cos\theta$ なので，最大静止摩擦力は $\mu N = \mu Mg\cos\theta$ です。滑らずに転がり続けるための条件は $f \le \mu N$ です。

$$
\frac{2}{7}Mg\sin\theta \le \mu Mg\cos\theta
$$

両辺を $Mg\cos\theta > 0$ で割ります。

$$
\tan\theta \le \frac{7}{2}\mu
$$

したがって，これより大きいと滑り始める臨界の傾斜角 $\theta$ は次式となります。

$$
\finalanswer{\theta = \arctan\!\left(\frac{7}{2}\mu\right)}
$$

### (5)

摩擦があり滑らずに転がって上る方が高くまで上ることができます。

斜面に入る直前の球は，並進運動エネルギー $\dfrac{1}{2}Mv^2$ に加えて，回転運動エネルギー $\dfrac{1}{2}I\omega^2 = \dfrac{1}{5}Mv^2$ をもっています。

摩擦があり滑らずに転がって上る場合，静止摩擦力は接触点が瞬間的に静止しているため仕事をせず，力学的エネルギーが保存します。最高点では並進も回転も同時に止まるため，並進と回転の両方の運動エネルギー $\dfrac{7}{10}Mv^2$ がすべて重力による位置エネルギーに変換され，到達高さは $h_1 = \dfrac{7v^2}{10g}$ となります。

一方，斜面が滑らかで摩擦がない場合，重心まわりに力のモーメントがはたらかないため，回転角速度 $\omega$ は斜面を上る間も一定のまま変わりません。その結果，回転運動エネルギーは位置エネルギーに変換されず，並進運動エネルギー $\dfrac{1}{2}Mv^2$ のみが位置エネルギーに変換されるため，到達高さは $h_2 = \dfrac{v^2}{2g}$ にとどまります。$h_1 > h_2$ なので，摩擦があって滑らずに転がる方が高く上ります。
