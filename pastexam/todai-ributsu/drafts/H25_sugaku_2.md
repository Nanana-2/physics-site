---
title: 東大理物 平成25年度 数学 第2問：2変数2階線形偏微分方程式の標準形と解
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
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
2 階微分の係数行列 $A = \{a_{i, j}\}$ は実対称行列なので，直交行列による対角化と各座標軸の定数倍を組み合わせることで，固有値の符号に応じた 3 種類の標準形へ変換できます。

さらに指数関数因子 $e^{\lambda_1 \xi_1 + \lambda_2 \xi_2}$ をくくり出すと，2 階微分から 1 階微分の項が生じるため，係数 $\lambda_1, \lambda_2$ の選び方によって 1 階微分の項を消去できます。
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
$\nabla_x = {}^t\!\left(\dfrac{\partial}{\partial x_1}, \dfrac{\partial}{\partial x_2}\right)$，$\nabla_\xi = {}^t\!\left(\dfrac{\partial}{\partial \xi_1}, \dfrac{\partial}{\partial \xi_2}\right)$ とおくと，設問 1 の結果は $\nabla_x = {}^t C \nabla_\xi$ と書かれます。2 階微分の項 $\mathcal{L}_2$ を行列 $A = \{a_{i, j}\}$ を用いて書き換えます。

$$
\begin{aligned}
\mathcal{L}_2 &= {}^t\nabla_x A \nabla_x \\
&= {}^t({}^t C \nabla_\xi) A ({}^t C \nabla_\xi) \\
&= {}^t\nabla_\xi \left(C A {}^t C\right) \nabla_\xi
\end{aligned}
$$

$A$ は実対称行列なので，実直交行列 $R$ を選んで対角化できます。その実固有値を $\mu_1, \mu_2$ とすると，$R A {}^t R = \operatorname{diag}(\mu_1, \mu_2)$ かつ $D = \det A = \mu_1 \mu_2$ です。対角行列 $S = \operatorname{diag}(s_1, s_2)$ を用いて $C = S R$ とおくと，$\det C = s_1 s_2 \det R$ かつ $C A {}^t C = \operatorname{diag}(s_1^2 \mu_1, s_2^2 \mu_2)$ となります。$D$ の符号で場合分けします。

- $D > 0$ のとき：$\mu_1 \mu_2 > 0$ より $\mu_1, \mu_2$ は同符号です。$s_1 = |\mu_1|^{-1/2}$，$s_2 = |\mu_2|^{-1/2}$ と選ぶと $\det C \neq 0$ かつ $C A {}^t C = \operatorname{diag}(\pm 1, \pm 1)$ となり，$\mathcal{L}_2 = \pm\left(\dfrac{\partial^2}{\partial \xi_1^2} + \dfrac{\partial^2}{\partial \xi_2^2}\right)$ です。
- $D = 0$ のとき：$A$ の成分のうち少なくとも 1 つは $0$ でないので，$\mu_1, \mu_2$ の一方は $0$，他方は $0$ でありません。$R$ の行を入れ替えて $\mu_1 = 0, \mu_2 \neq 0$ とし，$s_1 = 1$，$s_2 = |\mu_2|^{-1/2}$ と選ぶと $\det C \neq 0$ かつ $C A {}^t C = \operatorname{diag}(0, \pm 1)$ となり，$\mathcal{L}_2 = \pm\dfrac{\partial^2}{\partial \xi_2^2}$ です。
- $D < 0$ のとき：$\mu_1 \mu_2 < 0$ より $\mu_1, \mu_2$ は異符号です。$R$ の行を入れ替えて $\mu_1 > 0, \mu_2 < 0$ とし，$s_1 = \mu_1^{-1/2}$，$s_2 = (-\mu_2)^{-1/2}$ と選ぶと $\det C \neq 0$ かつ $C A {}^t C = \operatorname{diag}(1, -1)$ となり，$\mathcal{L}_2 = \dfrac{\partial^2}{\partial \xi_1^2} - \dfrac{\partial^2}{\partial \xi_2^2}$ です。

### (3)
設問 2 の変換後，$\mathcal{L}$ の 1 階微分の項は新たな実定数 $\tilde{b}_1, \tilde{b}_2$ を用いて $\tilde{b}_1 \dfrac{\partial}{\partial \xi_1} + \tilde{b}_2 \dfrac{\partial}{\partial \xi_2}$ と書かれます。$\psi(\xi_1, \xi_2) = e^{\lambda_1 \xi_1 + \lambda_2 \xi_2}\phi(\xi_1, \xi_2)$ を微分すると，各 $i = 1, 2$ に対して次式が成り立ちます。

$$
\begin{aligned}
\frac{\partial\psi}{\partial \xi_i} &= e^{\lambda_1 \xi_1 + \lambda_2 \xi_2}\left(\frac{\partial\phi}{\partial \xi_i} + \lambda_i\phi\right) \\
\frac{\partial^2\psi}{\partial \xi_i^2} &= e^{\lambda_1 \xi_1 + \lambda_2 \xi_2}\left(\frac{\partial^2\phi}{\partial \xi_i^2} + 2\lambda_i\frac{\partial\phi}{\partial \xi_i} + \lambda_i^2\phi\right)
\end{aligned}
$$

これらを $\mathcal{L}\psi = E\psi$ に代入し，両辺を $e^{\lambda_1 \xi_1 + \lambda_2 \xi_2} \neq 0$ で割って各場合を調べます。

- $D > 0$ のとき：2 階微分の符号を $\sigma \in \{+1, -1\}$ とすると，次式になります。
  $$
  \begin{aligned}
  \sigma\left(\frac{\partial^2\phi}{\partial\xi_1^2} + \frac{\partial^2\phi}{\partial\xi_2^2}\right) + (2\sigma\lambda_1 + \tilde{b}_1)\frac{\partial\phi}{\partial\xi_1} + (2\sigma\lambda_2 + \tilde{b}_2)\frac{\partial\phi}{\partial\xi_2} + \bigl(\sigma\lambda_1^2 + \sigma\lambda_2^2 + \tilde{b}_1\lambda_1 + \tilde{b}_2\lambda_2\bigr)\phi &= E\phi
  \end{aligned}
  $$
  ここで $\lambda_1 = -\dfrac{\sigma\tilde{b}_1}{2}$，$\lambda_2 = -\dfrac{\sigma\tilde{b}_2}{2}$ と選んで両辺に $\sigma$ を掛けると 1 階微分の項が消え，定数 $F$ を用いて式 (2) の形になります。

- $D = 0$ のとき：2 階微分の符号を $\sigma \in \{+1, -1\}$ とすると，次式になります。
  $$
  \begin{aligned}
  \sigma\frac{\partial^2\phi}{\partial\xi_2^2} + \tilde{b}_1\frac{\partial\phi}{\partial\xi_1} + (2\sigma\lambda_2 + \tilde{b}_2)\frac{\partial\phi}{\partial\xi_2} + \bigl(\sigma\lambda_2^2 + \tilde{b}_1\lambda_1 + \tilde{b}_2\lambda_2\bigr)\phi &= E\phi
  \end{aligned}
  $$
  ここで $\lambda_2 = -\dfrac{\sigma\tilde{b}_2}{2}$，$\lambda_1 = 0$ と選んで両辺に $-\sigma$ を掛けると $\dfrac{\partial\phi}{\partial\xi_2}$ の項が消え，定数 $\beta = -\sigma\tilde{b}_1$ と定数 $F$ を用いて式 (3) の形になります。

- $D < 0$ のとき：次式になります。
  $$
  \begin{aligned}
  \left(\frac{\partial^2\phi}{\partial\xi_1^2} - \frac{\partial^2\phi}{\partial\xi_2^2}\right) + (2\lambda_1 + \tilde{b}_1)\frac{\partial\phi}{\partial\xi_1} + (-2\lambda_2 + \tilde{b}_2)\frac{\partial\phi}{\partial\xi_2} + \bigl(\lambda_1^2 - \lambda_2^2 + \tilde{b}_1\lambda_1 + \tilde{b}_2\lambda_2\bigr)\phi &= E\phi
  \end{aligned}
  $$
  ここで $\lambda_1 = -\dfrac{\tilde{b}_1}{2}$，$\lambda_2 = \dfrac{\tilde{b}_2}{2}$ と選ぶと 1 階微分の項がともに消え，定数 $F$ を用いて式 (4) の形になります。

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
\phi(0, \xi_2) = \int_{-\infty}^{\infty} f(y) e^{i y \xi_2}\,\mathrm{d}y = \delta(\xi_2)
$$

デルタ関数のフーリエ積分表示 $\delta(\xi_2) = \dfrac{1}{2\pi}\displaystyle\int_{-\infty}^{\infty} e^{i y \xi_2}\,\mathrm{d}y$ と比較すると，$f(y) = \dfrac{1}{2\pi}$ です。

これを $\xi_1 > 0$ の積分へ代入し，指数部分を $y$ について平方完成します。

$$
\begin{aligned}
-y^2 \xi_1 + i y \xi_2 &= -\xi_1\left(y^2 - \frac{i\xi_2}{\xi_1} y\right) \\
&= -\xi_1\left(y - \frac{i\xi_2}{2\xi_1}\right)^2 - \frac{\xi_2^2}{4\xi_1}
\end{aligned}
$$

ガウス積分 $\displaystyle\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x = \sqrt{\pi}$ を用いて積分を計算します。

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
$u = \xi_1 - \xi_2$，$v = \xi_1 + \xi_2$ とおくと，$\phi(\xi_1, \xi_2) = G_1(u) + G_2(v)$ です。合成関数の微分法を用いて $\xi_1$ と $\xi_2$ による 2 階偏微分を計算します。

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
