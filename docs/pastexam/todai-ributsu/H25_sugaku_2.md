---
title: 東大理物 平成25年度 数学 第2問：2変数2階線形偏微分方程式の標準形と解
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成25年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成25年度 数学 第2問：2変数2階線形偏微分方程式の標準形と解

## 問題

$\mathcal{L}$ を微分演算子，$\psi(x_1, x_2)$ を 2 個の実変数 $x_1, x_2$ の関数として，微分方程式 $\mathcal{L}\psi(x_1, x_2) = E\psi(x_1, x_2)$ を考える。ここで，$E$ は定数である。$\mathcal{L}$ の形を

$$
\mathcal{L} = \sum_{i=1}^2 \sum_{j=1}^2 a_{i, j}\frac{\partial^2}{\partial x_i \partial x_j} + \sum_{i=1}^2 b_i \frac{\partial}{\partial x_i}
$$

とする。ここで $a_{i, j}, b_i$（$i, j = 1, 2$）は実定数で，$a_{i, j}$（$i, j = 1, 2$）のうち少なくとも一つはゼロでないとし，$a_{j, i} = a_{i, j}$ とする。また，$\{a_{i, j}\}$ を 2 行 2 列の行列とみなしたときの行列式を $D$ とする。この微分方程式の解の性質について，以下の設問に答えよ。

(1) 或る実行列 $C = \{c_{i, j}\}$（$i, j = 1, 2$）を用いて，変数を

$$
\begin{pmatrix} \xi_1 \\ \xi_2 \end{pmatrix} = C\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
$$

のように線形変換したときに，微分演算子 $\dfrac{\partial}{\partial x_1}, \dfrac{\partial}{\partial x_2}$ を $\dfrac{\partial}{\partial \xi_1}, \dfrac{\partial}{\partial \xi_2}$ で表せ。ただし，$C$ の行列式はゼロでないとする。

(2) $\mathcal{L}$ の中の 2 階微分の項に関して，適当な $C$ を選ぶと，$D > 0$ の場合は

$$
\pm\left(\frac{\partial^2}{\partial \xi_1^2} + \frac{\partial^2}{\partial \xi_2^2}\right)
$$

となり，$D = 0$ の場合は

$$
\pm\frac{\partial^2}{\partial \xi_2^2}
$$

となり，$D < 0$ の場合は

$$
\frac{\partial^2}{\partial \xi_1^2} - \frac{\partial^2}{\partial \xi_2^2}
$$

となることを示せ。

(3) 次に，$\psi(\xi_1, \xi_2) = e^{\lambda_1 \xi_1 + \lambda_2 \xi_2}\phi(\xi_1, \xi_2)$ のように書き換える。ここで，$\lambda_i$（$i = 1, 2$）は定数である。これにより $\mathcal{L}$ の 1 階微分の項を変換でき，$\phi$ に対する微分方程式は，$\lambda_i$（$i = 1, 2$）を適当に選べば，$D > 0$ の場合には

$$
\left(\frac{\partial^2}{\partial \xi_1^2} + \frac{\partial^2}{\partial \xi_2^2}\right)\phi(\xi_1, \xi_2) = F\phi(\xi_1, \xi_2) \tag{2}
$$

$D = 0$ の場合には

$$
\left(\beta\frac{\partial}{\partial \xi_1} - \frac{\partial^2}{\partial \xi_2^2}\right)\phi(\xi_1, \xi_2) = F\phi(\xi_1, \xi_2) \tag{3}
$$

$D < 0$ の場合には

$$
\left(\frac{\partial^2}{\partial \xi_1^2} - \frac{\partial^2}{\partial \xi_2^2}\right)\phi(\xi_1, \xi_2) = F\phi(\xi_1, \xi_2) \tag{4}
$$

の形になることを示せ。ここで，$F, \beta$ はそれぞれ定数であるが，具体的に与えなくてよい。

(4) 式 (3) において $F = 0, \beta = 1$ とする。

(i) $\xi_1 > 0$ に対して

$$
\phi(\xi_1, \xi_2) = \int_{-\infty}^{\infty} f(y) e^{-y^2 \xi_1} e^{i y \xi_2}\,\mathrm{d}y
$$

は，式 (3) を満たすことを示せ。ここで $i$ は虚数単位，また，$f(y)$ は実変数 $y$ の関数であり，この積分の収束条件を満たすとする。

(ii) $\xi_1 = 0$ で $\phi(\xi_1, \xi_2) = \delta(\xi_2)$ の場合に，$\xi_1 > 0$ に対して，この方程式の解を求めよ。ここで $\delta(x)$ はデルタ関数である。また，$\displaystyle\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x = \sqrt{\pi}$ であることは既知としてよい。

(5) 式 (4) において $F = 0$ の場合を考える。

$$
\phi(\xi_1, \xi_2) = G_1(\xi_1 - \xi_2) + G_2(\xi_1 + \xi_2)
$$

は，式 (4) を満たすことを示せ。ここで $G_i$（$i = 1, 2$）は微分可能な任意の関数である。

> 出典：東京大学大学院理学系研究科物理学専攻 平成25年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2階微分の係数行列 $A$ は実対称行列なので，直交行列で対角化することができます。さらに座標を固有値の大きさに応じて伸び縮みさせると，2階微分の部分は，固有値の符号によって3種類の形のどれかになります。

残る1階微分の項は，$\psi$ を $e^{\lambda_1 \xi_1 + \lambda_2 \xi_2}\phi$ とおいて消します。指数関数を微分すると1階微分の項が新しく出てくるので，これがもとの1階微分の項と打ち消し合うように $\lambda_1$，$\lambda_2$ を選びます。
</div>

### (1)
線形変換の成分表示は

$$
\begin{aligned}
\xi_1 &= c_{1,1} x_1 + c_{1,2} x_2 \\
\xi_2 &= c_{2,1} x_1 + c_{2,2} x_2
\end{aligned}
$$

です。合成関数の微分の公式より，$\dfrac{\partial}{\partial x_1}$ と $\dfrac{\partial}{\partial x_2}$ は次のように表されます。

$$
\begin{aligned}
\frac{\partial}{\partial x_1} &= \frac{\partial \xi_1}{\partial x_1}\frac{\partial}{\partial \xi_1} + \frac{\partial \xi_2}{\partial x_1}\frac{\partial}{\partial \xi_2} \\
&= c_{1,1}\frac{\partial}{\partial \xi_1} + c_{2,1}\frac{\partial}{\partial \xi_2}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial}{\partial x_2} &= \frac{\partial \xi_1}{\partial x_2}\frac{\partial}{\partial \xi_1} + \frac{\partial \xi_2}{\partial x_2}\frac{\partial}{\partial \xi_2} \\
&= c_{1,2}\frac{\partial}{\partial \xi_1} + c_{2,2}\frac{\partial}{\partial \xi_2}
\end{aligned}
$$

$$
\finalanswer{\frac{\partial}{\partial x_1} = c_{1,1}\frac{\partial}{\partial \xi_1} + c_{2,1}\frac{\partial}{\partial \xi_2}, \qquad \frac{\partial}{\partial x_2} = c_{1,2}\frac{\partial}{\partial \xi_1} + c_{2,2}\frac{\partial}{\partial \xi_2}}
$$

### (2)
$\nabla_x={}^t\!\left(\dfrac{\partial}{\partial x_1},\dfrac{\partial}{\partial x_2}\right)$，$\nabla_\xi={}^t\!\left(\dfrac{\partial}{\partial\xi_1},\dfrac{\partial}{\partial\xi_2}\right)$ とおきます。設問1の $\nabla_x={}^tC\nabla_\xi$ を用いると，主部は

$$
\begin{aligned}
\mathcal L_2&={}^t\nabla_xA\nabla_x\\
&={}^t\nabla_\xi(CA{}^tC)\nabla_\xi
\end{aligned}
$$

です。実直交行列 $R$ を選び，$RA{}^tR=\operatorname{diag}(\mu_1,\mu_2)$ とします。$D=\mu_1\mu_2$ です。$S=\operatorname{diag}(s_1,s_2)$ と $C=SR$ を用いると，

$$
CA{}^tC=\operatorname{diag}(s_1^2\mu_1,s_2^2\mu_2)
$$

となります。

$D>0$ では両固有値が同符号です。その符号を $\sigma\in\{1,-1\}$ とし，$s_i=|\mu_i|^{-1/2}$ と選びます。

$$
\begin{aligned}
s_i^2\mu_i&=\frac{\mu_i}{|\mu_i|}\\
&=\sigma\\
\mathcal L_2&=\sigma\left(\frac{\partial^2}{\partial\xi_1^2}+\frac{\partial^2}{\partial\xi_2^2}\right)
\end{aligned}
$$

$D=0$ では，$A\ne O$ なので一方の固有値だけが0です。軸を入れ替えて $\mu_1=0$，$\mu_2\ne0$ とし，$s_1=1$，$s_2=|\mu_2|^{-1/2}$ を選びます。

$$
\begin{aligned}
CA{}^tC&=\operatorname{diag}(0,\operatorname{sgn}\mu_2)\\
\mathcal L_2&=\sigma\frac{\partial^2}{\partial\xi_2^2}
\end{aligned}
$$

ここで $\sigma=\operatorname{sgn}\mu_2$ です。

$D<0$ では両固有値が異符号です。$\mu_1>0$，$\mu_2<0$ の順に軸を選び，$s_i=|\mu_i|^{-1/2}$ とします。

$$
\begin{aligned}
CA{}^tC&=\operatorname{diag}(1,-1)\\
\mathcal L_2&=\frac{\partial^2}{\partial\xi_1^2}-\frac{\partial^2}{\partial\xi_2^2}
\end{aligned}
$$

いずれも $s_1,s_2$ は0でなく，$\det C=s_1s_2\det R\ne0$ です。

### (3)
$\boldsymbol b={}^t(b_1,b_2)$ とします。1階微分の係数は，

$$
\begin{aligned}
{}^t\boldsymbol b\nabla_x&={}^t\boldsymbol b\,{}^tC\nabla_\xi\\
&={}^t(C\boldsymbol b)\nabla_\xi
\end{aligned}
$$

なので，$\tilde{\boldsymbol b}=C\boldsymbol b$ と定義します。

$\psi=e^{\lambda_1\xi_1+\lambda_2\xi_2}\phi$ の微分は，

$$
\begin{aligned}
\partial_i\psi&=e^{\lambda_1\xi_1+\lambda_2\xi_2}(\partial_i\phi+\lambda_i\phi)\\
\partial_i^2\psi&=e^{\lambda_1\xi_1+\lambda_2\xi_2}(\partial_i^2\phi+2\lambda_i\partial_i\phi+\lambda_i^2\phi)
\end{aligned}
$$

です。ここで $\partial_i=\partial/\partial\xi_i$ と書きました。

$D>0$ では，指数関数を割ると，

$$
\begin{aligned}
\sigma(\partial_1^2+\partial_2^2)\phi
&+(2\sigma\lambda_1+\tilde b_1)\partial_1\phi
 +(2\sigma\lambda_2+\tilde b_2)\partial_2\phi\\
&+\left[\sigma(\lambda_1^2+\lambda_2^2)+\tilde b_1\lambda_1+\tilde b_2\lambda_2\right]\phi=E\phi
\end{aligned}
$$

となります。$\lambda_i=-\sigma\tilde b_i/2$ と選び，両辺に $\sigma$ を掛けます。

$$
(\partial_1^2+\partial_2^2)\phi=\left(\sigma E+\frac{\tilde b_1^2+\tilde b_2^2}{4}\right)\phi
$$

右辺の括弧を $F$ とおけば式 (2) です。

$D=0$ では，$\lambda_1=0$，$\lambda_2=-\sigma\tilde b_2/2$ を選びます。$\partial_2\phi$ の係数は0になりますが，$\partial_1\phi$ の項は残ります。

$$
\sigma\partial_2^2\phi+\tilde b_1\partial_1\phi=\left(E+\frac{\sigma\tilde b_2^2}{4}\right)\phi
$$

両辺に $-\sigma$ を掛けると，

$$
(-\sigma\tilde b_1\partial_1-\partial_2^2)\phi=\left(-\sigma E-\frac{\tilde b_2^2}{4}\right)\phi
$$

です。$\beta=-\sigma\tilde b_1$ とおき，右辺の括弧を $F$ とすれば式 (3) になります。

$D<0$ では，$\lambda_1=-\tilde b_1/2$，$\lambda_2=\tilde b_2/2$ と選ぶと，両方向の1階微分の項が0になります。

$$
(\partial_1^2-\partial_2^2)\phi=\left(E+\frac{\tilde b_1^2-\tilde b_2^2}{4}\right)\phi
$$

右辺の括弧を $F$ とすれば式 (4) です。

### (4)(i)
$\xi_1 > 0$ のもとで，積分記号下の微分を行います。

$$
\begin{aligned}
\frac{\partial\phi}{\partial\xi_1} &= \int_{-\infty}^{\infty} (-y^2) f(y) e^{-y^2 \xi_1} e^{i y \xi_2}\,\mathrm{d}y \\
\frac{\partial^2\phi}{\partial\xi_2^2} &= \int_{-\infty}^{\infty} (iy)^2 f(y) e^{-y^2 \xi_1} e^{i y \xi_2}\,\mathrm{d}y \\
&= \int_{-\infty}^{\infty} (-y^2) f(y) e^{-y^2 \xi_1} e^{i y \xi_2}\,\mathrm{d}y
\end{aligned}
$$

両辺の差をとると次式となり，$F = 0, \beta = 1$ の式 (3) を満たします。

$$
\left(\frac{\partial}{\partial\xi_1} - \frac{\partial^2}{\partial\xi_2^2}\right)\phi(\xi_1, \xi_2) = 0
$$

### (4)(ii)
$\xi_1 = 0$ の条件を設問 (4)(i) の表式に代入します。

$$
\begin{aligned}
\phi(0, \xi_2) &= \int_{-\infty}^{\infty} f(y) e^{i y \xi_2}\,\mathrm{d}y \\
&= \delta(\xi_2)
\end{aligned}
$$

初期条件は分布として解釈します。デルタ関数のフーリエ表示は

$$
\delta(\xi_2)=\frac1{2\pi}\int_{\mathbb R}e^{iy\xi_2}\,\mathrm{d}y
$$

なので，係数は $f(y)=\dfrac1{2\pi}$ です。$\xi_1=0$ での積分は通常の収束積分ではなく，$\xi_1\downarrow0$ での分布の極限です。

これを $\xi_1 > 0$ の積分へ代入し，指数部分を $y$ について平方完成します。

$$
\begin{aligned}
-y^2 \xi_1 + i y \xi_2 &= -\xi_1\left(y^2 - \frac{i\xi_2}{\xi_1} y\right) \\
&= -\xi_1\left(y - \frac{i\xi_2}{2\xi_1}\right)^2 - \frac{\xi_2^2}{4\xi_1}
\end{aligned}
$$

平方完成後の積分路は実軸から平行移動しています。$a=\xi_1>0$，$b=\xi_2/(2\xi_1)$ とおくと，被積分関数 $e^{-a(z-ib)^2}$ は整関数です。実軸と $\operatorname{Im}z=b$ を結ぶ長方形では，縦辺の絶対値は定数倍の $e^{-aR^2}$ で抑えられ，$R\to\infty$ で0になります。そのため積分路を平行移動して，

$$
\begin{aligned}
\int_{\mathbb R}e^{-a(y-ib)^2}\,\mathrm{d}y
&=\int_{\mathbb R+ib}e^{-a(z-ib)^2}\,\mathrm{d}z\\
&=\int_{\mathbb R}e^{-au^2}\,\mathrm{d}u\\
&=\sqrt{\frac\pi a}
\end{aligned}
$$

です。この結果を用いると，

$$
\begin{aligned}
\phi(\xi_1, \xi_2) &= \frac{1}{2\pi}\exp\!\left(-\frac{\xi_2^2}{4\xi_1}\right)\int_{-\infty}^{\infty} \exp\!\left[-\xi_1\left(y - \frac{i\xi_2}{2\xi_1}\right)^2\right]\mathrm{d}y \\
&= \frac{1}{2\pi}\exp\!\left(-\frac{\xi_2^2}{4\xi_1}\right)\sqrt{\frac{\pi}{\xi_1}} \\
&= \frac{1}{2\sqrt{\pi\xi_1}}\exp\!\left(-\frac{\xi_2^2}{4\xi_1}\right)
\end{aligned}
$$

$$
\finalanswer{\phi(\xi_1, \xi_2) = \frac{1}{2\sqrt{\pi\xi_1}}\exp\!\left(-\frac{\xi_2^2}{4\xi_1}\right)}
$$

### (5)
通常の2階偏微分で式 (4) を確かめるため，以下では $G_1,G_2$ が2階微分可能な場合を計算します。原本の「微分可能」を1回だけと読む場合には，2階微分を分布として解釈する必要があります。

$u=\xi_1-\xi_2$，$v=\xi_1+\xi_2$ とおくと，$\phi=G_1(u)+G_2(v)$ です。合成関数の微分法で各偏微分を求めます。

$$
\begin{aligned}
\frac{\partial\phi}{\partial\xi_1} &= G_1'(u) + G_2'(v) \\
\frac{\partial^2\phi}{\partial\xi_1^2} &= G_1''(u) + G_2''(v)
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial\phi}{\partial\xi_2} &= -G_1'(u) + G_2'(v) \\
\frac{\partial^2\phi}{\partial\xi_2^2} &= (-1)^2 G_1''(u) + G_2''(v) \\
&= G_1''(u) + G_2''(v)
\end{aligned}
$$

したがって両者の差は $0$ になります。

$$
\left(\frac{\partial^2}{\partial\xi_1^2} - \frac{\partial^2}{\partial\xi_2^2}\right)\phi(\xi_1, \xi_2) = 0
$$

以上より，$\phi(\xi_1, \xi_2) = G_1(\xi_1 - \xi_2) + G_2(\xi_1 + \xi_2)$ は $F = 0$ の式 (4) を満たします。
