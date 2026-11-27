---
title: 東大理物 平成14年度 物理学 第3問：誘電体境界面での斜め入射電磁波の反射・屈折とブルースター角
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成14年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成14年度 物理学 第3問：誘電体境界面での斜め入射電磁波の反射・屈折とブルースター角

## 問題

角振動数 $\omega$ の単色電磁波が真空から誘電体に入射する場合を考える。Maxwell の方程式は次のように与えられる。

$$
\boldsymbol{\nabla}\cdot(\epsilon\boldsymbol{E}) = 0, \qquad \boldsymbol{\nabla}\cdot\boldsymbol{B} = 0
$$

$$
\boldsymbol{\nabla}\times\boldsymbol{E} = -\frac{\partial\boldsymbol{B}}{\partial t}, \qquad \boldsymbol{\nabla}\times\left(\frac{\boldsymbol{B}}{\mu}\right) = \frac{\partial(\epsilon\boldsymbol{E})}{\partial t}
$$

ここで $\boldsymbol{E}$ は電場，$\boldsymbol{B}$ は磁場，$\epsilon$ は誘電率，$\mu$ は透磁率を表す。図のように，3次元空間において $x < 0$ が真空，$x > 0$ が誘電体であるとする。真空の誘電率，透磁率をそれぞれ $\epsilon_0, \mu_0$ で表し，誘電体の誘電率は $\epsilon_1$（$> \epsilon_0$），透磁率は $\mu_0$ で与えられるものとする。電場，磁場はそれぞれ，入射波に対しては $\boldsymbol{E}_0(\boldsymbol{r}, t), \boldsymbol{B}_0(\boldsymbol{r}, t)$，屈折波に対しては $\boldsymbol{E}_1(\boldsymbol{r}, t), \boldsymbol{B}_1(\boldsymbol{r}, t)$，反射波に対しては $\boldsymbol{E}_2(\boldsymbol{r}, t), \boldsymbol{B}_2(\boldsymbol{r}, t)$ とする。以下の問に，解答に至る筋道を添えて答えよ。
{: .problem-lead }

<figure class="problem-figure" markdown>
![真空と誘電体の境界面x=0における入射波・反射波・屈折波](../../assets/figures/pastexam-todai-ributsu/H14_butsuri_3-p-light.svg#only-light)
![真空と誘電体の境界面x=0における入射波・反射波・屈折波](../../assets/figures/pastexam-todai-ributsu/H14_butsuri_3-p-dark.svg#only-dark)
<figcaption markdown="span">図1：真空（$x < 0$，$\epsilon_0, \mu_0$）から誘電体（$x > 0$，$\epsilon_1, \mu_0$）へ入射する電磁波の進行方向 $\boldsymbol{n}_0, \boldsymbol{n}_1, \boldsymbol{n}_2$ と入射角 $\theta_0$・屈折角 $\theta_1$。</figcaption>
</figure>

(1) 真空と誘電体の境界 $x = 0$ において，

$$
\boldsymbol{E}_{0,\mathrm{t}}(0, y, z, t) + \boldsymbol{E}_{2,\mathrm{t}}(0, y, z, t) = \boldsymbol{E}_{1,\mathrm{t}}(0, y, z, t) \tag{1}
$$

$$
\epsilon_0\bigl[E_{0,x}(0, y, z, t) + E_{2,x}(0, y, z, t)\bigr] = \epsilon_1 E_{1,x}(0, y, z, t) \tag{2}
$$

$$
\boldsymbol{B}_{0,\mathrm{t}}(0, y, z, t) + \boldsymbol{B}_{2,\mathrm{t}}(0, y, z, t) = \boldsymbol{B}_{1,\mathrm{t}}(0, y, z, t) \tag{3}
$$

が成立する。ここで添字の $\mathrm{t}$ は各ベクトルの真空と誘電体の境界に平行な成分，添字の $x$ は $x$ 成分を表す。

(a) (1) 式が成立することを示せ。

(b) 誘導電荷密度 $\rho$ と電場 $\boldsymbol{E}$ の間には関係式 $\epsilon_0\boldsymbol{\nabla}\cdot\boldsymbol{E} = \rho$ が成立する。誘電体の表面（$x = +0$）における電荷の面密度 $\sigma(y, z, t)$ を $E_{1,x}(0, y, z, t), \epsilon_0, \epsilon_1$ を用いて表せ。

(2) 入射波の方向が $xy$ 面にあるように座標軸をとり，$x, y, z$ 軸方向の単位ベクトルをそれぞれ $\hat{\boldsymbol{x}}, \hat{\boldsymbol{y}}, \hat{\boldsymbol{z}}$ で表す。入射波の進行方向の単位ベクトルを $\boldsymbol{n}_0 = \hat{\boldsymbol{x}}\cos\theta_0 + \hat{\boldsymbol{y}}\sin\theta_0$（$0 < \theta_0 < \pi/2$）とし，入射波の磁場 $\boldsymbol{B}_0(\boldsymbol{r}, t)$ が $z$ 方向に直線偏光している場合，

$$
\boldsymbol{B}_0(\boldsymbol{r}, t) = \hat{\boldsymbol{z}}B_0\exp\!\bigl[i(k_0\boldsymbol{n}_0\cdot\boldsymbol{r} - \omega t)\bigr]
$$

を考える。入射波の電場は，

$$
\boldsymbol{E}_0(\boldsymbol{r}, t) = \boldsymbol{E}_0\exp\!\bigl[i(k_0\boldsymbol{n}_0\cdot\boldsymbol{r} - \omega t)\bigr]
$$

と表す。

(a) $k_0$ を $\omega, \epsilon_0, \mu_0$ を用いて表せ。

(b) 入射波の電場の振幅 $\boldsymbol{E}_0$ を $B_0, \hat{\boldsymbol{z}}, k_0, \boldsymbol{n}_0, \omega$ を用いて表せ。

(3) 屈折波，反射波の磁場をそれぞれ，

$$
\boldsymbol{B}_1(\boldsymbol{r}, t) = \hat{\boldsymbol{z}}B_1\exp\!\bigl[i(k_1\boldsymbol{n}_1\cdot\boldsymbol{r} - \omega t)\bigr]
$$

$$
\boldsymbol{B}_2(\boldsymbol{r}, t) = \hat{\boldsymbol{z}}B_2\exp\!\bigl[i(k_0\boldsymbol{n}_2\cdot\boldsymbol{r} - \omega t)\bigr]
$$

と表す。$\boldsymbol{n}_1, \boldsymbol{n}_2$ はそれぞれ屈折波，反射波の進行方向の単位ベクトルであり，これらを

$$
\boldsymbol{n}_1 = \hat{\boldsymbol{x}}\cos\theta_1 + \hat{\boldsymbol{y}}\sin\theta_1
$$

$$
\boldsymbol{n}_2 = -\hat{\boldsymbol{x}}\cos\theta_0 + \hat{\boldsymbol{y}}\sin\theta_0
$$

と表す。

(a) (3) 式を用いて入射角 $\theta_0$ と屈折角 $\theta_1$ の関係式を求めよ。

(b) (1) 式と (3) 式を用いて $B_1, B_2$ を求めよ。答えは $k_0, k_1, \theta_0, \theta_1, B_0$ を用いて表せ。

(c) $\theta_0 + \theta_1 = \pi/2$ のとき，何が起こるか。

> 出典：東京大学大学院理学系研究科物理学専攻 平成14年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，マクスウェル方程式にストークスの定理とガウスの発散定理を用いて，境界面での接線電場の連続性と誘電体表面の分極電荷密度を導きます。

後半では，磁場が入射面に垂直な直線偏光の平面波について，マクスウェル方程式から分散関係と電場・磁場の関係式を求めます。境界面での位相整合からスネルの法則を導き，接線成分の連続条件を連立させることで反射波と屈折波の振幅比および無反射条件が得られます。
</div>

### (1)

#### (a)

境界面 $x = 0$ をまたぎ，境界に平行な長さ $\Delta\ell$ の辺と境界に垂直な幅 $\delta$ の辺からなる微小長方形の閉経路 $C$ と，その囲む面 $S$ を考えます。境界に平行な辺の単位方向ベクトルを $\hat{\boldsymbol{t}}$ とし，面 $S$ の法線単位ベクトルを $\hat{\boldsymbol{n}}_S$ とします。

ファラデーの法則 $\boldsymbol{\nabla}\times\boldsymbol{E} = -\dfrac{\partial\boldsymbol{B}}{\partial t}$ を面 $S$ 上で面積分し，左辺にストークスの定理を用います。

$$
\oint_{C} \boldsymbol{E}\cdot\mathrm{d}\boldsymbol{\ell} = -\iint_{S} \frac{\partial\boldsymbol{B}}{\partial t}\cdot\hat{\boldsymbol{n}}_S\,\mathrm{d}S
$$

幅 $\delta \to 0$ の極限をとります。$x < 0$ の全電場は $\boldsymbol{E}_0 + \boldsymbol{E}_2$，$x > 0$ の全電場は $\boldsymbol{E}_1$ であり，境界に垂直な辺の寄与は $\delta \to 0$ で $0$ になります。また，$\dfrac{\partial\boldsymbol{B}}{\partial t}$ は有限なので右辺の面積分は面積 $\delta\Delta\ell \to 0$ とともに $0$ になります。したがって左辺は次式になります。

$$
\bigl\{\boldsymbol{E}_1(0, y, z, t) - \boldsymbol{E}_0(0, y, z, t) - \boldsymbol{E}_2(0, y, z, t)\bigr\}\cdot\hat{\boldsymbol{t}}\,\Delta\ell = 0
$$

境界に平行な任意の方向 $\hat{\boldsymbol{t}}$ に対してこれが成り立つため，式 (1) が成立します。

$$
\boldsymbol{E}_{0,\mathrm{t}}(0, y, z, t) + \boldsymbol{E}_{2,\mathrm{t}}(0, y, z, t) = \boldsymbol{E}_{1,\mathrm{t}}(0, y, z, t)
$$

#### (b)

境界面 $x = 0$ をまたぐ底面積 $\Delta S$，厚さ $\delta$ の微小円柱領域 $V$ を考え，$\epsilon_0\boldsymbol{\nabla}\cdot\boldsymbol{E} = \rho$ を体積積分してガウスの発散定理を用います。

$$
\epsilon_0\iint_{\partial V} \boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = \iiint_{V} \rho\,\mathrm{d}V
$$

厚さ $\delta \to 0$ の極限では側面の寄与は $0$ になり，右辺は表面の誘導電荷 $\sigma(y, z, t)\Delta S$ に等しくなります。$x = +0$ 側の外向き法線は $+\hat{\boldsymbol{x}}$，$x = -0$ 側の外向き法線は $-\hat{\boldsymbol{x}}$ なので，次式が得られます。

$$
\epsilon_0\Bigl\{E_{1,x}(0, y, z, t) - \bigl[E_{0,x}(0, y, z, t) + E_{2,x}(0, y, z, t)\bigr]\Bigr\}\Delta S = \sigma(y, z, t)\Delta S
$$

式 (2) より $E_{0,x}(0, y, z, t) + E_{2,x}(0, y, z, t) = \dfrac{\epsilon_1}{\epsilon_0}E_{1,x}(0, y, z, t)$ を代入して整理します。

$$
\begin{aligned}
\sigma(y, z, t) &= \epsilon_0\left(1 - \frac{\epsilon_1}{\epsilon_0}\right)E_{1,x}(0, y, z, t) \\
&= -(\epsilon_1 - \epsilon_0)E_{1,x}(0, y, z, t)
\end{aligned}
$$

$$
\finalanswer{\sigma(y, z, t) = -(\epsilon_1 - \epsilon_0)E_{1,x}(0, y, z, t)}
$$

### (2)

#### (a)

真空中（$\epsilon = \epsilon_0, \mu = \mu_0$）のマクスウェル方程式において，$\boldsymbol{\nabla} \to i k_0\boldsymbol{n}_0$，$\dfrac{\partial}{\partial t} \to -i\omega$ と置き換えます。

$$
i k_0\boldsymbol{n}_0\times\boldsymbol{E}_0 = i\omega\hat{\boldsymbol{z}}B_0, \qquad i k_0\boldsymbol{n}_0\times\left(\frac{\hat{\boldsymbol{z}}B_0}{\mu_0}\right) = -i\omega\epsilon_0\boldsymbol{E}_0
$$

第2式より $\boldsymbol{E}_0 = -\dfrac{k_0}{\omega\epsilon_0\mu_0}(\boldsymbol{n}_0\times\hat{\boldsymbol{z}})B_0$ なので，これを第1式に代入します。

$$
\begin{aligned}
i\omega\hat{\boldsymbol{z}}B_0 &= -\frac{i k_0^2}{\omega\epsilon_0\mu_0}\bigl[\boldsymbol{n}_0\times(\boldsymbol{n}_0\times\hat{\boldsymbol{z}})\bigr]B_0 \\
&= -\frac{i k_0^2}{\omega\epsilon_0\mu_0}\bigl[(\boldsymbol{n}_0\cdot\hat{\boldsymbol{z}})\boldsymbol{n}_0 - (\boldsymbol{n}_0\cdot\boldsymbol{n}_0)\hat{\boldsymbol{z}}\bigr]B_0 \\
&= \frac{i k_0^2}{\omega\epsilon_0\mu_0}\hat{\boldsymbol{z}}B_0
\end{aligned}
$$

ここで $\boldsymbol{n}_0\cdot\hat{\boldsymbol{z}} = 0$ および $|\boldsymbol{n}_0| = 1$ を用いました。両辺を比較すると $k_0^2 = \omega^2\epsilon_0\mu_0$ であり，$k_0 > 0$ より次式となります。

$$
\finalanswer{k_0 = \omega\sqrt{\epsilon_0\mu_0}}
$$

#### (b)

小問 (a) の関係 $\epsilon_0\mu_0 = \dfrac{k_0^2}{\omega^2}$ を $\boldsymbol{E}_0 = -\dfrac{k_0}{\omega\epsilon_0\mu_0}(\boldsymbol{n}_0\times\hat{\boldsymbol{z}})B_0$ に代入します。

$$
\begin{aligned}
\boldsymbol{E}_0 &= -\frac{k_0}{\omega}\cdot\frac{\omega^2}{k_0^2}(\boldsymbol{n}_0\times\hat{\boldsymbol{z}})B_0 \\
&= \frac{\omega}{k_0}(\hat{\boldsymbol{z}}\times\boldsymbol{n}_0)B_0
\end{aligned}
$$

$$
\finalanswer{\boldsymbol{E}_0 = \frac{\omega}{k_0}(\hat{\boldsymbol{z}}\times\boldsymbol{n}_0)B_0}
$$

### (3)

#### (a)

境界 $x = 0$ において，$\boldsymbol{n}_0\cdot\boldsymbol{r} = y\sin\theta_0$，$\boldsymbol{n}_1\cdot\boldsymbol{r} = y\sin\theta_1$，$\boldsymbol{n}_2\cdot\boldsymbol{r} = y\sin\theta_0$ です。磁場はすべて $z$ 方向で境界に平行なので，式 (3) に代入して共通因子 $\hat{\boldsymbol{z}}e^{-i\omega t}$ を除きます。

$$
(B_0 + B_2)e^{i k_0 y\sin\theta_0} = B_1 e^{i k_1 y\sin\theta_1}
$$

これがすべての $y$ に対して恒等的に成り立つためには指数部の $y$ の係数が等しくなければなりません。

$$
k_0\sin\theta_0 = k_1\sin\theta_1
$$

誘電体中の波数は真空中と同様に $k_1 = \omega\sqrt{\epsilon_1\mu_0}$ なので，$\dfrac{k_1}{k_0} = \sqrt{\dfrac{\epsilon_1}{\epsilon_0}}$ です。したがって，入射角 $\theta_0$ と屈折角 $\theta_1$ の間にスネルの法則が成り立ちます。

$$
\finalanswer{k_0\sin\theta_0 = k_1\sin\theta_1 \qquad \left(\sqrt{\epsilon_0}\sin\theta_0 = \sqrt{\epsilon_1}\sin\theta_1\right)}
$$

#### (b)

小問 (a) の位相一致により，式 (3) から振幅の間の第1の関係式が得られます。

$$
B_0 + B_2 = B_1
$$

次に，各波の電場振幅を設問 (2)(b) と同様に求めます。

$$
\boldsymbol{E}_0 = \frac{\omega}{k_0}(\hat{\boldsymbol{z}}\times\boldsymbol{n}_0)B_0, \qquad \boldsymbol{E}_1 = \frac{\omega}{k_1}(\hat{\boldsymbol{z}}\times\boldsymbol{n}_1)B_1, \qquad \boldsymbol{E}_2 = \frac{\omega}{k_0}(\hat{\boldsymbol{z}}\times\boldsymbol{n}_2)B_2
$$

各外積を計算して境界に平行な $y$ 成分を取り出します。

$$
\hat{\boldsymbol{z}}\times\boldsymbol{n}_0 = -\hat{\boldsymbol{x}}\sin\theta_0 + \hat{\boldsymbol{y}}\cos\theta_0
$$

$$
\hat{\boldsymbol{z}}\times\boldsymbol{n}_1 = -\hat{\boldsymbol{x}}\sin\theta_1 + \hat{\boldsymbol{y}}\cos\theta_1
$$

$$
\hat{\boldsymbol{z}}\times\boldsymbol{n}_2 = -\hat{\boldsymbol{x}}\sin\theta_0 - \hat{\boldsymbol{y}}\cos\theta_0
$$

これらを式 (1) の $y$ 成分に代入し，共通因子 $\omega e^{i(k_0 y\sin\theta_0 - \omega t)}$ を除くと，第2の関係式が得られます。

$$
\frac{\cos\theta_0}{k_0}(B_0 - B_2) = \frac{\cos\theta_1}{k_1}B_1
$$

第1式から $B_2 = B_1 - B_0$ を第2式に代入して $B_1$ を求めます。

$$
\begin{aligned}
\frac{\cos\theta_0}{k_0}(2B_0 - B_1) &= \frac{\cos\theta_1}{k_1}B_1 \\
\left(\frac{\cos\theta_0}{k_0} + \frac{\cos\theta_1}{k_1}\right)B_1 &= \frac{2\cos\theta_0}{k_0}B_0
\end{aligned}
$$

両辺に $k_0 k_1$ を掛けて整理すると $B_1$ が得られます。

$$
B_1 = \frac{2k_1\cos\theta_0}{k_1\cos\theta_0 + k_0\cos\theta_1}B_0
$$

さらに $B_2 = B_1 - B_0$ を計算します。

$$
\begin{aligned}
B_2 &= \frac{2k_1\cos\theta_0 - (k_1\cos\theta_0 + k_0\cos\theta_1)}{k_1\cos\theta_0 + k_0\cos\theta_1}B_0 \\
&= \frac{k_1\cos\theta_0 - k_0\cos\theta_1}{k_1\cos\theta_0 + k_0\cos\theta_1}B_0
\end{aligned}
$$

したがって，$B_1, B_2$ は次式となります。

$$
\finalanswer{B_1 = \frac{2k_1\cos\theta_0}{k_1\cos\theta_0 + k_0\cos\theta_1}B_0, \qquad B_2 = \frac{k_1\cos\theta_0 - k_0\cos\theta_1}{k_1\cos\theta_0 + k_0\cos\theta_1}B_0}
$$

#### (c)

$\theta_0 + \theta_1 = \dfrac{\pi}{2}$ のとき，$\cos\theta_0 = \sin\theta_1$ および $\cos\theta_1 = \sin\theta_0$ が成り立ちます。これを小問 (b) で求めた $B_2$ の分子に代入し，小問 (a) のスネルの法則 $k_0\sin\theta_0 = k_1\sin\theta_1$ を用います。

$$
\begin{aligned}
k_1\cos\theta_0 - k_0\cos\theta_1 &= k_1\sin\theta_1 - k_0\sin\theta_0 \\
&= 0
\end{aligned}
$$

したがって反射波の振幅が $B_2 = 0$ となり，反射波は完全に消えて入射波はすべて誘電体内へ透過します。このときの入射角 $\theta_0$（$\tan\theta_0 = \sqrt{\epsilon_1/\epsilon_0}$）を**ブルースター角**といいます。
