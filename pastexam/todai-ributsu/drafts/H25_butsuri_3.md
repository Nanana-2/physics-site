---
title: 東大理物 平成25年度 物理学 第3問：電磁場中の荷電粒子のラグランジアンと運動
tags:
  - 院試過去問
  - 東大理物
  - 力学
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成25年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成25年度 物理学 第3問：電磁場中の荷電粒子のラグランジアンと運動

## 問題

ベクトルポテンシャル $\boldsymbol{A}(\boldsymbol{r}, t)$，スカラーポテンシャル $\varphi(\boldsymbol{r}, t)$ の電磁場内における粒子の運動を考える。この粒子の質量を $m$，電荷を $q$，位置ベクトルを $\boldsymbol{r} = (x, y, z)$ とすると，そのラグランジアンは

$$
L = \frac{1}{2}m\left|\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}\right|^2 + q\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}\cdot\boldsymbol{A} - q\varphi \tag{1}
$$

で与えられる。

(1) 式 (1) を用いて，この粒子に対するオイラー・ラグランジュ方程式を書き下せ。

(2) 設問 1 で得られたオイラー・ラグランジュ方程式が，ローレンツ力のもとでの運動方程式：

$$
m\frac{\mathrm{d}^2\boldsymbol{r}}{\mathrm{d}t^2} = q\boldsymbol{E} + q\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} \times \boldsymbol{B} \tag{2}
$$

に帰着することを示し，電場 $\boldsymbol{E}$ および磁場 $\boldsymbol{B}$ をベクトルポテンシャル $\boldsymbol{A}$ とスカラーポテンシャル $\varphi$ を用いてそれぞれ書き下せ。

(3) 任意の関数 $\Lambda = \Lambda(\boldsymbol{r}, t)$ に対するゲージ変換：

$$
\boldsymbol{A}' = \boldsymbol{A} + \operatorname{grad}\Lambda, \qquad \varphi' = \varphi - \frac{\partial\Lambda}{\partial t} \tag{3}
$$

のもとで，電場および磁場が不変であることを示せ。また，この変換のもとで得られる式 (1) のラグランジアンを $L'$ としたとき，$L'$ が $L$ と同じオイラー・ラグランジュ方程式を与える理由を簡単に述べよ。

以下の設問では，具体的にベクトルポテンシャルが

$$
\boldsymbol{A} = \left(-\frac{B}{2}y,\; \frac{B}{2}x,\; 0\right) \qquad (B\text{ は定数}), \tag{4}
$$

スカラーポテンシャルが

$$
\varphi = \frac{\alpha}{2}\left(2z^2 - x^2 - y^2\right) \qquad (\alpha\text{ は定数}), \tag{5}
$$

で与えられるものとし，特に $q > 0$，$0 < \alpha < \dfrac{q B^2}{4m}$ の場合を考える。

(4) 式 (4) と式 (5) に対応する磁場 $\boldsymbol{B}$ および電場 $\boldsymbol{E}$ を求めよ。

(5) 粒子の運動方程式の $z$ 成分を書き下し，粒子が $z$ 方向にどのような運動をするかを簡単に説明せよ。

(6) 粒子の運動方程式の $x$ 成分と $y$ 成分を書き下せ。この粒子の運動を $xy$ 平面上に射影したとき，どのような運動であるかを簡単に説明せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成25年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ラグランジアンの $q\dot{\boldsymbol{r}}\cdot\boldsymbol{A}$ の項をオイラー・ラグランジュ方程式に入れると，$\boldsymbol{A}(\boldsymbol{r}, t)$ を時間で全微分した項から，空間微分と速度の積が出てきます。この項を整理すると，ローレンツ力の磁場の項 $q\dot{\boldsymbol{r}} \times (\nabla \times \boldsymbol{A})$ になります。

四重極の電場と一様な磁場の中では，$z$ 方向の運動と $xy$ 面内の運動が分かれます。$x$ と $y$ の連立方程式は，複素数 $\zeta = x + iy$ にまとめると係数が定数の2階線形微分方程式になるので，解を $e^{i\Omega t}$ とおいて振動数の2次方程式を解きます。
</div>

### (1)
$\boldsymbol{r} = (x_1, x_2, x_3) = (x, y, z)$，$\dot{x}_i = \dfrac{\mathrm{d}x_i}{\mathrm{d}t}$ と書きます。式 (1) のラグランジアンを $\dot{x}_i$ と $x_i$ で偏微分します。

$$
\begin{aligned}
\frac{\partial L}{\partial \dot{x}_i} &= m\dot{x}_i + q A_i \\
\frac{\partial L}{\partial x_i} &= q\sum_{j=1}^3 \dot{x}_j \frac{\partial A_j}{\partial x_i} - q\frac{\partial \varphi}{\partial x_i}
\end{aligned}
$$

オイラー・ラグランジュ方程式 $\dfrac{\mathrm{d}}{\mathrm{d}t}\left(\dfrac{\partial L}{\partial \dot{x}_i}\right) - \dfrac{\partial L}{\partial x_i} = 0$ に代入すると，各成分 $i = 1, 2, 3$ について次式が得られます。

$$
\finalanswer{\frac{\mathrm{d}}{\mathrm{d}t}\left(m\frac{\mathrm{d}x_i}{\mathrm{d}t} + q A_i\right) - q\sum_{j=1}^3 \frac{\mathrm{d}x_j}{\mathrm{d}t}\frac{\partial A_j}{\mathrm{d}x_i} + q\frac{\partial \varphi}{\partial x_i} = 0 \qquad (i = 1, 2, 3)}
$$

### (2)
設問1の方程式で $A_i(\boldsymbol{r}(t), t)$ の時間全微分を連鎖律で展開します。

$$
\begin{aligned}
\frac{\mathrm{d}A_i}{\mathrm{d}t} &= \frac{\partial A_i}{\partial t} + \sum_{j=1}^3 \dot{x}_j \frac{\partial A_i}{\partial x_j}
\end{aligned}
$$

これを設問1の方程式に代入して $m\ddot{x}_i$ について整理します。

$$
\begin{aligned}
m\ddot{x}_i + q\frac{\partial A_i}{\partial t} + q\sum_{j=1}^3 \dot{x}_j \frac{\partial A_i}{\partial x_j} &= q\sum_{j=1}^3 \dot{x}_j \frac{\partial A_j}{\partial x_i} - q\frac{\partial \varphi}{\partial x_i} \\
m\ddot{x}_i &= q\left(-\frac{\partial \varphi}{\partial x_i} - \frac{\partial A_i}{\partial t}\right) + q\sum_{j=1}^3 \dot{x}_j\left(\frac{\partial A_j}{\partial x_i} - \frac{\partial A_i}{\partial x_j}\right)
\end{aligned}
$$

右辺第2項を $i = 1$ の成分について書き出します。

$$
\begin{aligned}
\sum_{j=1}^3 \dot{x}_j\left(\frac{\partial A_j}{\partial x_1} - \frac{\partial A_1}{\partial x_j}\right) &= \dot{y}\left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right) + \dot{z}\left(\frac{\partial A_z}{\partial x} - \frac{\partial A_x}{\partial z}\right) \\
&= \dot{y}(\nabla \times \boldsymbol{A})_z - \dot{z}(\nabla \times \boldsymbol{A})_y \\
&= \bigl(\dot{\boldsymbol{r}} \times (\nabla \times \boldsymbol{A})\bigr)_x
\end{aligned}
$$

$y$ 成分と $z$ 成分についても同様に成り立ちます。よって電場 $\boldsymbol{E}$ と磁場 $\boldsymbol{B}$ を次式で定義すれば，オイラー・ラグランジュ方程式は式 (2) に一致します。

$$
\finalanswer{\boldsymbol{E} = -\nabla\varphi - \frac{\partial\boldsymbol{A}}{\partial t}, \qquad \boldsymbol{B} = \nabla \times \boldsymbol{A}}
$$

### (3)
式 (3) のゲージ変換のもとで変換後の電場 $\boldsymbol{E}'$ と磁場 $\boldsymbol{B}'$ を計算します。任意の滑らかなスカラー関数 $\Lambda$ に対して $\nabla \times (\nabla\Lambda) = \boldsymbol{0}$ であり，空間微分と時間微分の順序は入れ替えることができます。

$$
\begin{aligned}
\boldsymbol{B}' &= \nabla \times \boldsymbol{A}' \\
&= \nabla \times \left(\boldsymbol{A} + \nabla\Lambda\right) \\
&= \nabla \times \boldsymbol{A} + \nabla \times (\nabla\Lambda) \\
&= \boldsymbol{B}
\end{aligned}
$$

$$
\begin{aligned}
\boldsymbol{E}' &= -\nabla\varphi' - \frac{\partial\boldsymbol{A}'}{\partial t} \\
&= -\nabla\left(\varphi - \frac{\partial\Lambda}{\partial t}\right) - \frac{\partial}{\partial t}\left(\boldsymbol{A} + \nabla\Lambda\right) \\
&= -\nabla\varphi + \nabla\frac{\partial\Lambda}{\partial t} - \frac{\partial\boldsymbol{A}}{\partial t} - \frac{\partial}{\partial t}\nabla\Lambda \\
&= \boldsymbol{E}
\end{aligned}
$$

以上より，$\boldsymbol{E}$ と $\boldsymbol{B}$ はゲージ変換のもとで不変です。

次に，変換後のラグランジアン $L'$ と元のラグランジアン $L$ の差を計算します。

$$
\begin{aligned}
L' - L &= q\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}\cdot\nabla\Lambda + q\frac{\partial\Lambda}{\partial t} \\
&= \frac{\mathrm{d}}{\mathrm{d}t}\bigl(q\Lambda(\boldsymbol{r}, t)\bigr)
\end{aligned}
$$

$L'$ と $L$ の差は座標と時刻の関数 $q\Lambda(\boldsymbol{r}, t)$ の時間全微分になります。作用積分 $S' = \displaystyle\int_{t_1}^{t_2} L'\,\mathrm{d}t$ と $S = \displaystyle\int_{t_1}^{t_2} L\,\mathrm{d}t$ の差は両端の時刻 $t_1, t_2$ での値 $[q\Lambda(\boldsymbol{r}, t)]_{t_1}^{t_2}$ だけになります。変分をとるとき両端の座標は固定されるので $\delta S' = \delta S$ となり，$L'$ は $L$ と同じオイラー・ラグランジュ方程式を与えます。

### (4)
式 (4) と式 (5) は時間によらないので，$\boldsymbol{B} = \nabla \times \boldsymbol{A}$，$\boldsymbol{E} = -\nabla\varphi$ を計算します。

$$
\begin{aligned}
B_x &= \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} = 0 \\
B_y &= \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} = 0 \\
B_z &= \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} = \frac{B}{2} - \left(-\frac{B}{2}\right) = B
\end{aligned}
$$

$$
\begin{aligned}
E_x &= -\frac{\partial\varphi}{\partial x} = \alpha x \\
E_y &= -\frac{\partial\varphi}{\partial y} = \alpha y \\
E_z &= -\frac{\partial\varphi}{\partial z} = -2\alpha z
\end{aligned}
$$

$$
\finalanswer{\boldsymbol{B} = (0,\; 0,\; B), \qquad \boldsymbol{E} = (\alpha x,\; \alpha y,\; -2\alpha z)}
$$

### (5)
設問4の結果を式 (2) の $z$ 成分に代入します。$(\dot{\boldsymbol{r}} \times \boldsymbol{B})_z = 0$ なので，次式が得られます。

$$
m\frac{\mathrm{d}^2 z}{\mathrm{d}t^2} = -2q\alpha z
$$

$q > 0$，$\alpha > 0$ なので，$\omega_z = \sqrt{\dfrac{2q\alpha}{m}}$ とおくと $\dfrac{\mathrm{d}^2 z}{\mathrm{d}t^2} + \omega_z^2 z = 0$ となります。したがって，粒子は $z = 0$ を中心として角振動数 $\sqrt{\dfrac{2q\alpha}{m}}$ の単振動を行います。

$$
\finalanswer{m\frac{\mathrm{d}^2 z}{\mathrm{d}t^2} = -2q\alpha z}
$$

### (6)
設問4の結果を式 (2) の $x$ 成分と $y$ 成分に代入します。

$$
\begin{aligned}
m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} &= q\alpha x + qB\frac{\mathrm{d}y}{\mathrm{d}t} \\
m\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} &= q\alpha y - qB\frac{\mathrm{d}x}{\mathrm{d}t}
\end{aligned}
$$

複素変数 $\zeta(t) = x(t) + i y(t)$ を導入し，第1式に第2式の $i$ 倍を加えます。

$$
\begin{aligned}
m\ddot{\zeta} &= q\alpha\zeta + qB(\dot{y} - i\dot{x}) \\
m\ddot{\zeta} &= q\alpha\zeta - i qB\dot{\zeta} \\
\ddot{\zeta} + i\frac{qB}{m}\dot{\zeta} - \frac{q\alpha}{m}\zeta &= 0
\end{aligned}
$$

$\omega_{\mathrm{c}} = \dfrac{qB}{m}$ とおき，$\zeta(t) = C e^{-i\Omega t}$ を代入して特性方程式を解きます。

$$
\begin{aligned}
-\Omega^2 + \omega_{\mathrm{c}}\Omega - \frac{q\alpha}{m} &= 0 \\
\Omega^2 - \omega_{\mathrm{c}}\Omega + \frac{q\alpha}{m} &= 0 \\
\Omega_{\pm} &= \frac{\omega_{\mathrm{c}} \pm \sqrt{\omega_{\mathrm{c}}^2 - \dfrac{4q\alpha}{m}}}{2}
\end{aligned}
$$

条件 $0 < \alpha < \dfrac{qB^2}{4m}$ より $\omega_{\mathrm{c}}^2 - \dfrac{4q\alpha}{m} = \dfrac{4q}{m}\left(\dfrac{qB^2}{4m} - \alpha\right) > 0$ が成り立ちます。また $\Omega_+ \Omega_- = \dfrac{q\alpha}{m} > 0$ なので，$\Omega_+$ と $\Omega_-$ はともに $\omega_{\mathrm{c}}$ と同符号の異なる実数です。

一般解は複素定数 $C_+, C_-$ を用いて

$$
\zeta(t) = C_+ e^{-i\Omega_+ t} + C_- e^{-i\Omega_- t}
$$

と書かれます。したがって，$xy$ 平面上に射影した運動は，異なる2つの角振動数 $\Omega_+$ と $\Omega_-$ をもつ同方向の等速円運動の重ね合わせであり，粒子は原点の周りの有界な領域にとどまります。

$$
\finalanswer{m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} = q\alpha x + qB\frac{\mathrm{d}y}{\mathrm{d}t}, \qquad m\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} = q\alpha y - qB\frac{\mathrm{d}x}{\mathrm{d}t}}
$$
