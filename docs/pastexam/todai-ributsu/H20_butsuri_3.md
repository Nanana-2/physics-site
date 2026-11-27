---
title: 東大理物 平成20年度 物理学 第3問：長方形導波管内の電磁波伝搬
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成20年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成20年度 物理学 第3問：長方形導波管内の電磁波伝搬

## 問題

以下の設問を通して，自由空間と導波管（金属でできた中空の管）における電磁波の伝搬の違いについて考えよう。

(1) 電場を $\tilde{\boldsymbol{E}}$，磁場を $\tilde{\boldsymbol{B}}$ とすると，真空中のマクスウェル方程式は

$$
\begin{aligned}
\nabla\cdot\tilde{\boldsymbol{E}} &= 0, & \nabla\times\tilde{\boldsymbol{E}} &= -\frac{\partial\tilde{\boldsymbol{B}}}{\partial t}, \\
\nabla\cdot\tilde{\boldsymbol{B}} &= 0, & \nabla\times\tilde{\boldsymbol{B}} &= \frac{1}{c^2}\frac{\partial\tilde{\boldsymbol{E}}}{\partial t}
\end{aligned}
$$

と書ける。ここで $c$ は真空中の光速度である。これらの式から，次の波動方程式を導け。

$$
\left(\nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\tilde{\boldsymbol{E}} = \boldsymbol{0}, \qquad \left(\nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\tilde{\boldsymbol{B}} = \boldsymbol{0}.
$$

以下では，$z$ 方向に伝搬する電磁場の関数形を

$$
\begin{aligned}
\tilde{\boldsymbol{E}}(x, y, z, t) &= \boldsymbol{E}(x, y)\exp[i(kz - \omega t)], \\
\tilde{\boldsymbol{B}}(x, y, z, t) &= \boldsymbol{B}(x, y)\exp[i(kz - \omega t)]
\end{aligned}
$$

と仮定する（自由空間中を $z$ 方向に伝搬する電磁波では，電磁場の $z$ 成分は共にゼロであるが，境界が存在する場合には，それらは必ずしもゼロではないことに注意せよ）。

(2) このとき，$k$ と $\omega$ で表されるある $\gamma$ を用いると，$\boldsymbol{E}(x, y),\ \boldsymbol{B}(x, y)$ の $z$ 成分 $E_z, B_z$ が

$$
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \gamma^2\right)E_z = 0, \tag{1}
$$

$$
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \gamma^2\right)B_z = 0 \tag{2}
$$

という形の方程式を満たすことを示し，そのときの $\gamma^2$ を具体的に書き表せ。

次に，図1のような長方形（$a > b$）の断面を持つ導波管内を，$z$ 方向に伝搬する電磁波を考える。導波管の壁面は完全導体でできており，内部は真空とする。ただし，壁面の厚さは無視してよいものとする。また，$\boldsymbol{n}$ を壁面の内側を向く単位法線ベクトルとしたとき，壁面での境界条件は $\boldsymbol{n}\times\tilde{\boldsymbol{E}} = \boldsymbol{0},\ \boldsymbol{n}\cdot\tilde{\boldsymbol{B}} = 0$ で与えられる。

<figure class="problem-figure" markdown>
![長方形導波管の模式図](../../assets/figures/pastexam-todai-ributsu/H20_butsuri_3-p-light.svg#only-light)
![長方形導波管の模式図](../../assets/figures/pastexam-todai-ributsu/H20_butsuri_3-p-dark.svg#only-dark)
<figcaption markdown="span">図1：$z$ 方向に無限に伸びている導波管の模式図。ただし，$z < 0$ の領域のみ描かれている。</figcaption>
</figure>

(3) 変数分離法を用いて，式 (1) を $E_z$ について解くことを考える。導波管壁面の境界条件に注意すると，整数 $m, n$ を用いて

$$
\gamma^2 = \frac{m^2\pi^2}{a^2} + \frac{n^2\pi^2}{b^2}
$$

と書けることを示せ。また，この整数の組 $(m, n)$ に対する解 $E_z$ を求めよ。ただし，$E_z$ の最大値を $E$ とせよ。

(4) 設問3と同じ整数の組 $(m, n)$ を用いると，式 (2) の解は

$$
B_z = B\cos\alpha x\cos\beta y
$$

と書ける。ただし，

$$
\alpha = \frac{m\pi}{a}, \qquad \beta = \frac{n\pi}{b}
$$

である。このとき，残りの成分 $E_x, E_y, B_x, B_y$ を求めよ。

(5) 設問3と4で得られた解 $\boldsymbol{E}(x, y),\ \boldsymbol{B}(x, y)$ のうち，$E_z = 0$ を満たす特別な場合を考える。4つの整数の組 $(m, n) = (0, 0),\ (1, 0),\ (0, 1),\ (1, 1)$ に対応する電磁場の解のうち，$z$ 方向に伝搬する電磁波を表し，かつ，その振動数が最小となるものはどれか。その最小振動数と $(m, n)$ を答え，理由も述べよ。

(6) 設問5で $E_z = 0$ の代わりに，$B_z = 0$ を満たす場合はどうなるか。同じく，最小振動数と $(m, n)$ を，理由をつけて答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成20年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
導波管のように $z$ 方向に一様な系では，電磁場の $z$ 依存性と時間依存性を平面波因子 $e^{i(kz - \omega t)}$ に分離することができます。この形をマクスウェル方程式に代入すると，横成分 $E_x, E_y, B_x, B_y$ はすべて縦成分 $E_z, B_z$ の $x, y$ 微分だけで表すことができます。

長方形の完全導体壁面では，断面内の波数 $\alpha, \beta$ が境界条件によって離散化されます。波数 $k$ が実数になって $z$ 方向に伝搬するためには $\omega^2/c^2 > \gamma^2$ が必要になるため，モードごとに伝搬できる振動数の下限が決まります。
</div>

### (1)

$\nabla\times\tilde{\boldsymbol{E}} = -\dfrac{\partial\tilde{\boldsymbol{B}}}{\partial t}$ の両辺の回転をとります。ベクトル恒等式 $\nabla\times(\nabla\times\boldsymbol{A}) = \nabla(\nabla\cdot\boldsymbol{A}) - \nabla^2\boldsymbol{A}$ と，残りのマクスウェル方程式 $\nabla\cdot\tilde{\boldsymbol{E}} = 0$，$\nabla\times\tilde{\boldsymbol{B}} = \dfrac{1}{c^2}\dfrac{\partial\tilde{\boldsymbol{E}}}{\partial t}$ を用います。

$$
\begin{aligned}
\nabla\times(\nabla\times\tilde{\boldsymbol{E}}) &= -\frac{\partial}{\partial t}(\nabla\times\tilde{\boldsymbol{B}}) \\
\nabla(\nabla\cdot\tilde{\boldsymbol{E}}) - \nabla^2\tilde{\boldsymbol{E}} &= -\frac{1}{c^2}\frac{\partial^2\tilde{\boldsymbol{E}}}{\partial t^2} \\
-\nabla^2\tilde{\boldsymbol{E}} &= -\frac{1}{c^2}\frac{\partial^2\tilde{\boldsymbol{E}}}{\partial t^2} \\
\left(\nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\tilde{\boldsymbol{E}} &= \boldsymbol{0}
\end{aligned}
$$

同様に，$\nabla\times\tilde{\boldsymbol{B}} = \dfrac{1}{c^2}\dfrac{\partial\tilde{\boldsymbol{E}}}{\partial t}$ の両辺の回転をとり，$\nabla\cdot\tilde{\boldsymbol{B}} = 0$ と $\nabla\times\tilde{\boldsymbol{E}} = -\dfrac{\partial\tilde{\boldsymbol{B}}}{\partial t}$ を用います。

$$
\begin{aligned}
\nabla\times(\nabla\times\tilde{\boldsymbol{B}}) &= \frac{1}{c^2}\frac{\partial}{\partial t}(\nabla\times\tilde{\boldsymbol{E}}) \\
\nabla(\nabla\cdot\tilde{\boldsymbol{B}}) - \nabla^2\tilde{\boldsymbol{B}} &= -\frac{1}{c^2}\frac{\partial^2\tilde{\boldsymbol{B}}}{\partial t^2} \\
\left(\nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\tilde{\boldsymbol{B}} &= \boldsymbol{0}
\end{aligned}
$$

### (2)

$\tilde{E}_z(x, y, z, t) = E_z(x, y)e^{i(kz - \omega t)}$ に対して，各偏微分を計算します。

$$
\frac{\partial^2\tilde{E}_z}{\partial z^2} = (ik)^2 E_z e^{i(kz - \omega t)} = -k^2 E_z e^{i(kz - \omega t)}
$$

$$
\frac{\partial^2\tilde{E}_z}{\partial t^2} = (-i\omega)^2 E_z e^{i(kz - \omega t)} = -\omega^2 E_z e^{i(kz - \omega t)}
$$

これらを設問1の波動方程式の $z$ 成分に代入し，両辺の共通因子 $e^{i(kz - \omega t)} \neq 0$ を除きます。

$$
\begin{aligned}
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} - k^2 + \frac{\omega^2}{c^2}\right)E_z &= 0 \\
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \gamma^2\right)E_z &= 0
\end{aligned}
$$

$\tilde{B}_z(x, y, z, t) = B_z(x, y)e^{i(kz - \omega t)}$ についても全く同じ計算から式 (2) が得られます。ここで $\gamma^2$ は次式となります。

$$
\finalanswer{\gamma^2 = \frac{\omega^2}{c^2} - k^2}
$$

### (3)

完全導体壁面での境界条件 $\boldsymbol{n}\times\tilde{\boldsymbol{E}} = \boldsymbol{0}$ は，壁面に平行な電場成分が $0$ であることを表します。$z$ 方向は4つの壁面 $x = 0, a$ および $y = 0, b$ のすべてに平行なので，$E_z(x, y)$ に対する境界条件は次式になります。

$$
E_z(0, y) = E_z(a, y) = 0, \qquad E_z(x, 0) = E_z(x, b) = 0
$$

$E_z(x, y) = X(x)Y(y)$ と変数分離して式 (1) に代入し，$X(x)Y(y)$ で割ります。

$$
\begin{aligned}
\frac{1}{X}\frac{\mathrm{d}^2 X}{\mathrm{d}x^2} + \frac{1}{Y}\frac{\mathrm{d}^2 Y}{\mathrm{d}y^2} + \gamma^2 &= 0 \\
-\frac{1}{X}\frac{\mathrm{d}^2 X}{\mathrm{d}x^2} &= \frac{1}{Y}\frac{\mathrm{d}^2 Y}{\mathrm{d}y^2} + \gamma^2
\end{aligned}
$$

左辺は $x$ のみの関数，右辺は $y$ のみの関数なので，両辺は定数 $\alpha^2$ に等しくなります。$\beta^2 = \gamma^2 - \alpha^2$ とおくと，次の2つの常微分方程式が得られます。

$$
\frac{\mathrm{d}^2 X}{\mathrm{d}x^2} + \alpha^2 X = 0, \qquad \frac{\mathrm{d}^2 Y}{\mathrm{d}y^2} + \beta^2 Y = 0
$$

境界条件は $X(0) = X(a) = 0$ および $Y(0) = Y(b) = 0$ です。$\alpha^2 \le 0$ のときは $X(0) = X(a) = 0$ を満たす $0$ でない解が存在しません。よって $\alpha^2 > 0$ であり，一般解 $X(x) = C_1\cos\alpha x + C_2\sin\alpha x$ に $X(0) = 0$ を課すと $C_1 = 0$，$X(a) = 0$ を課すと $\sin\alpha a = 0$ となります。したがって，整数 $m$ を用いて $\alpha = \dfrac{m\pi}{a}$ です。同様に $Y(0) = Y(b) = 0$ から整数 $n$ を用いて $\beta = \dfrac{n\pi}{b}$ となり，次式が得られます。

$$
\gamma^2 = \alpha^2 + \beta^2 = \frac{m^2\pi^2}{a^2} + \frac{n^2\pi^2}{b^2}
$$

また，正の整数 $m, n$ に対して最大値が $E$ となる解 $E_z(x, y)$ は，全体の符号を除いて次式になります。

$$
\finalanswer{E_z(x, y) = E\sin\!\left(\frac{m\pi x}{a}\right)\sin\!\left(\frac{n\pi y}{b}\right)}
$$

### (4)

$\tilde{\boldsymbol{E}} = \boldsymbol{E}(x, y)e^{i(kz - \omega t)}$，$\tilde{\boldsymbol{B}} = \boldsymbol{B}(x, y)e^{i(kz - \omega t)}$ を $\nabla\times\tilde{\boldsymbol{E}} = -\dfrac{\partial\tilde{\boldsymbol{B}}}{\partial t}$ と $\nabla\times\tilde{\boldsymbol{B}} = \dfrac{1}{c^2}\dfrac{\partial\tilde{\boldsymbol{E}}}{\partial t}$ に代入し，$x, y$ 成分を書き出します。

$$
\begin{aligned}
\frac{\partial E_z}{\partial y} - ikE_y &= i\omega B_x \\
ikE_x - \frac{\partial E_z}{\partial x} &= i\omega B_y \\
\frac{\partial B_z}{\partial y} - ikB_y &= -\frac{i\omega}{c^2}E_x \\
ikB_x - \frac{\partial B_z}{\partial x} &= -\frac{i\omega}{c^2}E_y
\end{aligned}
$$

まず第2式と第3式から $B_y$ を消して $E_x$ を求めます。第2式より $B_y = \dfrac{k}{\omega}E_x + \dfrac{i}{\omega}\dfrac{\partial E_z}{\partial x}$ です。これを第3式に代入します。

$$
\begin{aligned}
\frac{\partial B_z}{\partial y} - ik\left(\frac{k}{\omega}E_x + \frac{i}{\omega}\frac{\partial E_z}{\partial x}\right) &= -\frac{i\omega}{c^2}E_x \\
i\left(\frac{\omega}{c^2} - \frac{k^2}{\omega}\right)E_x &= -\frac{k}{\omega}\frac{\partial E_z}{\partial x} - \frac{\partial B_z}{\partial y} \\
\frac{i}{\omega}\left(\frac{\omega^2}{c^2} - k^2\right)E_x &= -\frac{1}{\omega}\left(k\frac{\partial E_z}{\partial x} + \omega\frac{\partial B_z}{\partial y}\right)
\end{aligned}
$$

$\gamma^2 = \dfrac{\omega^2}{c^2} - k^2$ を用いて両辺に $-i\omega/\gamma^2$ を掛けると，$E_x$ が得られます。

$$
E_x = \frac{i}{\gamma^2}\left(k\frac{\partial E_z}{\partial x} + \omega\frac{\partial B_z}{\partial y}\right)
$$

これを $B_y = \dfrac{k}{\omega}E_x + \dfrac{i}{\omega}\dfrac{\partial E_z}{\partial x}$ に代入して $B_y$ を求めます。

$$
\begin{aligned}
B_y &= \frac{ik}{\omega\gamma^2}\left(k\frac{\partial E_z}{\partial x} + \omega\frac{\partial B_z}{\partial y}\right) + \frac{i}{\omega}\frac{\partial E_z}{\partial x} \\
&= \frac{i}{\omega\gamma^2}\left((k^2 + \gamma^2)\frac{\partial E_z}{\partial x} + k\omega\frac{\partial B_z}{\partial y}\right) \\
&= \frac{i}{\gamma^2}\left(\frac{\omega}{c^2}\frac{\partial E_z}{\partial x} + k\frac{\partial B_z}{\partial y}\right)
\end{aligned}
$$

次に第1式と第4式から同様に $E_y$ と $B_x$ を求めます。第1式より $B_x = -\dfrac{k}{\omega}E_y - \dfrac{i}{\omega}\dfrac{\partial E_z}{\partial y}$ です。これを第4式に代入します。

$$
\begin{aligned}
ik\left(-\frac{k}{\omega}E_y - \frac{i}{\omega}\frac{\partial E_z}{\partial y}\right) - \frac{\partial B_z}{\partial x} &= -\frac{i\omega}{c^2}E_y \\
\frac{i}{\omega}\left(\frac{\omega^2}{c^2} - k^2\right)E_y &= -\frac{k}{\omega}\frac{\partial E_z}{\partial y} + \frac{\partial B_z}{\partial x} \\
E_y &= \frac{i}{\gamma^2}\left(k\frac{\partial E_z}{\partial y} - \omega\frac{\partial B_z}{\partial x}\right)
\end{aligned}
$$

これを $B_x = -\dfrac{k}{\omega}E_y - \dfrac{i}{\omega}\dfrac{\partial E_z}{\partial y}$ に代入します。

$$
\begin{aligned}
B_x &= -\frac{ik}{\omega\gamma^2}\left(k\frac{\partial E_z}{\partial y} - \omega\frac{\partial B_z}{\partial x}\right) - \frac{i}{\omega}\frac{\partial E_z}{\partial y} \\
&= \frac{i}{\omega\gamma^2}\left(-(k^2 + \gamma^2)\frac{\partial E_z}{\partial y} + k\omega\frac{\partial B_z}{\partial x}\right) \\
&= \frac{i}{\gamma^2}\left(-\frac{\omega}{c^2}\frac{\partial E_z}{\partial y} + k\frac{\partial B_z}{\partial x}\right)
\end{aligned}
$$

ここで $E_z = E\sin\alpha x\sin\beta y$，$B_z = B\cos\alpha x\cos\beta y$ の各偏微分を計算します。

$$
\begin{aligned}
\frac{\partial E_z}{\partial x} &= \alpha E\cos\alpha x\sin\beta y, & \frac{\partial E_z}{\partial y} &= \beta E\sin\alpha x\cos\beta y \\
\frac{\partial B_z}{\partial x} &= -\alpha B\sin\alpha x\cos\beta y, & \frac{\partial B_z}{\partial y} &= -\beta B\cos\alpha x\sin\beta y
\end{aligned}
$$

これらを代入すると，残りの4成分は次式となります。

$$
\finalanswer{
\begin{aligned}
E_x &= \frac{i}{\gamma^2}\bigl(k\alpha E - \omega\beta B\bigr)\cos\alpha x\sin\beta y \\
E_y &= \frac{i}{\gamma^2}\bigl(k\beta E + \omega\alpha B\bigr)\sin\alpha x\cos\beta y \\
B_x &= -\frac{i}{\gamma^2}\left(k\alpha B + \frac{\omega}{c^2}\beta E\right)\sin\alpha x\cos\beta y \\
B_y &= \frac{i}{\gamma^2}\left(\frac{\omega}{c^2}\alpha E - k\beta B\right)\cos\alpha x\sin\beta y
\end{aligned}
}
$$

### (5)

$E_z = 0$ の場合，すなわち $E = 0$ とおいた解を調べます。

まず $(m, n) = (0, 0)$ のときは $\alpha = \beta = 0$ であり，$\gamma^2 = 0$ です。$B_z = B$ は $x, y$ によらない定数となります。このとき $\nabla\cdot\tilde{\boldsymbol{B}} = 0$ の式より $\dfrac{\partial B_x}{\partial x} + \dfrac{\partial B_y}{\partial y} + ikB = 0$ ですが，境界条件 $\boldsymbol{n}\cdot\tilde{\boldsymbol{B}} = 0$ を用いて導波管の断面全体で積分すると，ガウスの発散定理から $\iint \left(\dfrac{\partial B_x}{\partial x} + \dfrac{\partial B_y}{\partial y}\right)\mathrm{d}x\,\mathrm{d}y = 0$ です。よって $ikB = 0$ となり，$k \neq 0$ の伝搬波では $B = 0$ です。また $E_z = B_z = 0$ かつ $\gamma^2 = 0$ の場合，断面内で $\nabla_\perp\cdot\boldsymbol{E} = 0$，$\nabla_\perp\times\boldsymbol{E} = \boldsymbol{0}$ を満たす電場は静電ポテンシャルの勾配で書かれますが，単連結な中空導波管の周囲全体で電位が等しいため $\boldsymbol{E} = \boldsymbol{0}$，$\boldsymbol{B} = \boldsymbol{0}$ となります。したがって $(0, 0)$ は $z$ 方向に伝搬する電磁波を与えません。

次に $(m, n) = (1, 0), (0, 1), (1, 1)$ のときは $\gamma^2 > 0$ であり，$B \neq 0$ とすると設問4の式から $0$ でない電磁場が得られます。これらの電磁場が $z$ 方向に減衰せず伝搬するためには，波数 $k$ が $0$ でない実数，すなわち $k^2 > 0$ である必要があります。設問2より

$$
k^2 = \frac{\omega^2}{c^2} - \gamma^2 > 0
$$

なので，角振動数 $\omega$ は $\omega > c\gamma$ を満たさなければなりません。振動数 $\nu = \dfrac{\omega}{2\pi}$ では $\nu > \dfrac{c\gamma}{2\pi}$ です。

各 $(m, n)$ に対する $\gamma = \pi\sqrt{\dfrac{m^2}{a^2} + \dfrac{n^2}{b^2}}$ の値を $a > b$ に注意して比べます。

$$
\gamma_{(1, 0)} = \frac{\pi}{a} < \gamma_{(0, 1)} = \frac{\pi}{b} < \gamma_{(1, 1)} = \pi\sqrt{\frac{1}{a^2} + \frac{1}{b^2}}
$$

よって，伝搬可能な振動数の下限が最小となるのは $(m, n) = (1, 0)$ です。その最小の角振動数 $\omega_{\min}$ と振動数 $\nu_{\min} = \dfrac{\omega_{\min}}{2\pi}$ は次式となります。

$$
\finalanswer{(m, n) = (1, 0), \qquad \omega_{\min} = \frac{\pi c}{a} \quad \left(\nu_{\min} = \frac{c}{2a}\right)}
$$

### (6)

$B_z = 0$ の場合，すなわち $B = 0$ とおいた解を調べます。

設問3より $E_z = E\sin\dfrac{m\pi x}{a}\sin\dfrac{n\pi y}{b}$ です。$m = 0$ または $n = 0$ のときは $\sin 0 = 0$ となるため $E_z$ が恒等的に $0$ となります。このとき $B = 0$ かつ $E_z = 0$ なので，設問4の式から $E_x = E_y = B_x = B_y = 0$ となり，$(0, 0), (1, 0), (0, 1)$ のいずれも電磁場が恒等的に $0$ になってしまいます。

したがって，与えられた4組のうち $z$ 方向に伝搬する $0$ でない電磁波を表すのは $(m, n) = (1, 1)$ のみです。このとき $\gamma = \pi\sqrt{\dfrac{1}{a^2} + \dfrac{1}{b^2}}$ であり，$k^2 = \dfrac{\omega^2}{c^2} - \gamma^2 > 0$ より，最小の角振動数 $\omega_{\min}$ と振動数 $\nu_{\min} = \dfrac{\omega_{\min}}{2\pi}$ は次式となります。

$$
\finalanswer{(m, n) = (1, 1), \qquad \omega_{\min} = \pi c\sqrt{\frac{1}{a^2} + \frac{1}{b^2}} \quad \left(\nu_{\min} = \frac{c}{2}\sqrt{\frac{1}{a^2} + \frac{1}{b^2}}\right)}
$$
