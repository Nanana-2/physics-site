---
title: 東大理物 平成26年度 数学第1問：常微分方程式・連立微分方程式・熱伝導方程式
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成26年度
exam_subject: 専門科目（数学）
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成26年度 数学第1問：常微分方程式・連立微分方程式・熱伝導方程式

## 問題

以下の設問に答えよ。変数 $x$ や $t$ は実数であり，関数 $y, y_1, y_2$ は実関数である。

(1) 微分方程式

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = -\alpha y
$$

を満たす関数 $y(x)$ を求めよ。$y(b) = A$ とする。$\alpha, b, A$ は実定数である。

(2) 連立微分方程式

$$
\begin{aligned}
\frac{\mathrm{d}y_1}{\mathrm{d}x} &= -\alpha y_1 \\
\frac{\mathrm{d}y_2}{\mathrm{d}x} &= \beta y_1 - \gamma y_2
\end{aligned}
$$

を満たす関数 $y_1(x)$，$y_2(x)$ を求めよ。$y_1(0) = A$，$y_2(0) = 0$ とする。$\alpha, \beta, \gamma, A$ は正の実定数であり，$\alpha \neq \gamma$ とする。$y_1(x)$，$y_2(x)$ の符号はどうなるか述べよ。

(3) 連立微分方程式

$$
\begin{aligned}
\frac{\mathrm{d}y_1}{\mathrm{d}x} &= -c y_1 + \sqrt{3}\, c y_2 \\
\frac{\mathrm{d}y_2}{\mathrm{d}x} &= \sqrt{3}\, c y_1 - 3 c y_2
\end{aligned}
$$

を満たす関数 $y_1(x)$，$y_2(x)$ を求めよ。ここで，$c$ は実定数であり，$y_1(0) = \dfrac{\sqrt{3} - 1}{2}$，$y_2(0) = \dfrac{\sqrt{3} + 1}{2}$ とする。

(4) 偏微分方程式

$$
\frac{\partial y}{\partial t} = \frac{\partial^2 y}{\partial x^2}
$$

の解 $y(x, t)$ を見つけたい。境界条件としては，実定数 $a > 0$ に対し，$x \le -a$ 及び $x \ge a$ では $y(x, t) = 0$ とする。$-a < x < a$ で微分可能な解を一つ以上示せ。ただし，$y = \text{定数}$ なる解は考慮しない。

(5) 非斉次微分方程式

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = -\alpha(1 - \beta y) y
$$

を満たす関数 $y(x)$ を求めよ。$\alpha, \beta$ は正定数である。$y(0) = A$ とする。ここで，$A$ は正定数である。

> 出典：[東京大学大学院理学系研究科物理学専攻](https://www.phys.s.u-tokyo.ac.jp/) 平成26年度修士課程入学試験問題 数学 第1問（Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。）

---

## 解答・解説

※ 本解答・解説は非公式であり，大学当局とは無関係です。

### 考え方

線形 1 階常微分方程式から出発し，逐次崩壊型の連立系，実対称行列の対角化を伴う連立系，ディリクレ境界条件つきの 1 次元熱伝導方程式，そしてベルヌーイ型の非線形常微分方程式へと段階的に展開する構成である。

連立系 (3) では係数行列が実対称であることに注目すると直交固有ベクトルで分解することができ，(5) では逆数 $u = 1/y$ へ変数変換することで 1 階線形常微分方程式へと変形でき，初期値 $A$ と $1/\beta$ の大小を場合分けせずに統一的に解を求めることができます。

### 解答

#### (1) 1階線形常微分方程式

両辺に積分因子 $e^{\alpha x}$ を掛けて整理すると，

$$
\begin{aligned}
e^{\alpha x}\frac{\mathrm{d}y}{\mathrm{d}x} + \alpha e^{\alpha x} y &= 0 \\
\frac{\mathrm{d}}{\mathrm{d}x}\left(e^{\alpha x} y\right) &= 0
\end{aligned}
$$

となる。よって $e^{\alpha x} y(x) = C$（$C$ は積分定数）である。初期条件 $y(b) = A$ より $C = A e^{\alpha b}$ であるから，

$$
y(x) = A e^{-\alpha(x - b)}
$$

を得る（この導出は $A = 0$ の場合にもそのまま成り立つ）。

$$
\finalanswer{y(x) = A e^{-\alpha(x - b)}}
$$

#### (2) 連立微分方程式と解の符号

第 1 式と初期条件 $y_1(0) = A$ より，(1) と同様にして

$$
y_1(x) = A e^{-\alpha x}
$$

を得る。これを第 2 式に代入して両辺に積分因子 $e^{\gamma x}$ を掛けると，

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}x}\left(e^{\gamma x} y_2\right) &= \beta A e^{(\gamma - \alpha) x} \\
e^{\gamma x} y_2(x) - y_2(0) &= \beta A \int_0^x e^{(\gamma - \alpha) s}\,\mathrm{d}s
= \frac{\beta A}{\gamma - \alpha}\left(e^{(\gamma - \alpha)x} - 1\right)
\end{aligned}
$$

となる。$y_2(0) = 0$ より，

$$
y_2(x) = \frac{\beta A}{\gamma - \alpha}\left(e^{-\alpha x} - e^{-\gamma x}\right)
$$

を得る。

次に，$y_1(x)$ と $y_2(x)$ の符号を調べる。$A > 0$ より，すべての実数 $x$ に対して $y_1(x) = A e^{-\alpha x} > 0$ である。また，$y_2(x)$ を

$$
y_2(x) = \beta A e^{-\alpha x}\,\frac{1 - e^{-(\gamma - \alpha) x}}{\gamma - \alpha}
$$

と書き換えると，$\beta A e^{-\alpha x} > 0$ であるから，符号は $\dfrac{1 - e^{-(\gamma - \alpha)x}}{\gamma - \alpha}$ の符号に一致する。
- $x > 0$ のとき：$\gamma > \alpha$ なら分子・分母とも正，$\gamma < \alpha$ なら分子・分母とも負であるため，いずれの場合も $y_2(x) > 0$ である。
- $x = 0$ のとき：$y_2(0) = 0$ である。
- $x < 0$ のとき：$\gamma > \alpha$ なら分子が負・分母が正，$\gamma < \alpha$ なら分子が正・分母が負であるため，いずれの場合も $y_2(x) < 0$ である。

$$
\finalanswer{y_1(x) = A e^{-\alpha x}, \qquad y_2(x) = \frac{\beta A}{\gamma - \alpha}\left(e^{-\alpha x} - e^{-\gamma x}\right)}
$$

（符号：$y_1(x) > 0$（すべての $x$）；$y_2(x) > 0$（$x > 0$），$y_2(0) = 0$，$y_2(x) < 0$（$x < 0$）。）

#### (3) 実対称行列による連立微分方程式

方程式を行列形式で書くと，

$$
\frac{\mathrm{d}}{\mathrm{d}x}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = c M \begin{pmatrix} y_1 \\ y_2 \end{pmatrix}, \qquad M = \begin{pmatrix} -1 & \sqrt{3} \\ \sqrt{3} & -3 \end{pmatrix}
$$

となる。$M$ の固有方程式は

$$
\det(M - \lambda I) = (\lambda + 1)(\lambda + 3) - 3 = \lambda(\lambda + 4) = 0
$$

より，固有値は $\lambda_1 = 0$，$\lambda_2 = -4$ である。それぞれに対応する規格化された固有ベクトルは

$$
\boldsymbol{v}_1 = \frac{1}{2}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}, \qquad \boldsymbol{v}_2 = \frac{1}{2}\begin{pmatrix} -1 \\ \sqrt{3} \end{pmatrix}
$$

となる。初期値ベクトルを $\boldsymbol{v}_1, \boldsymbol{v}_2$ で展開すると，

$$
\begin{pmatrix} y_1(0) \\ y_2(0) \end{pmatrix}
= \frac{1}{2}\begin{pmatrix} \sqrt{3} - 1 \\ \sqrt{3} + 1 \end{pmatrix}
= \boldsymbol{v}_1 + \boldsymbol{v}_2
$$

と表される。したがって，一般解に初期条件を代入すると

$$
\begin{pmatrix} y_1(x) \\ y_2(x) \end{pmatrix}
= e^{\lambda_1 c x}\boldsymbol{v}_1 + e^{\lambda_2 c x}\boldsymbol{v}_2
= \frac{1}{2}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix} + \frac{1}{2}e^{-4cx}\begin{pmatrix} -1 \\ \sqrt{3} \end{pmatrix}
$$

となる。

$$
\finalanswer{y_1(x) = \frac{\sqrt{3} - e^{-4cx}}{2}, \qquad y_2(x) = \frac{1 + \sqrt{3}\,e^{-4cx}}{2}}
$$

#### (4) 1次元熱伝導方程式の解

$-a < x < a$ の領域で変数分離解 $y(x, t) = X(x) T(t)$ を仮定し，偏微分方程式に代入すると，

$$
\frac{1}{T(t)}\frac{\mathrm{d}T}{\mathrm{d}t} = \frac{1}{X(x)}\frac{\mathrm{d}^2 X}{\mathrm{d}x^2} = -k^2
$$

となる（$k$ は実定数とする。分離定数が $0$ または正のときは境界条件 $X(-a) = X(a) = 0$ を満たす零でない解が存在しない）。これより $T(t) = e^{-k^2 t}$，$X(x) = C_1 \cos(kx) + C_2 \sin(kx)$ を得る。

境界条件 $X(-a) = X(a) = 0$ より，零でない解は $k_n = \dfrac{n\pi}{2a}$（$n = 1, 2, 3, \dots$）に対して

$$
X_n(x) = \sin\!\left(\frac{n\pi(x + a)}{2a}\right)
$$

と与えられる（奇数 $n$ では $\cos\!\left(\dfrac{n\pi x}{2a}\right)$ に，偶数 $n$ では $\sin\!\left(\dfrac{n\pi x}{2a}\right)$ に比例する）。特に $n = 1$ を選べば，$C \neq 0$ を任意の実定数として

$$
y(x, t) = \begin{cases} C \exp\!\left(-\dfrac{\pi^2}{4a^2} t\right)\cos\!\left(\dfrac{\pi x}{2a}\right) & (-a < x < a) \\ 0 & (|x| \ge a) \end{cases}
$$

は $-a < x < a$ で微分可能であり，定数でない解の一つを与える。より一般に，任意の自然数 $n$ に対して

$$
\finalanswer{y_n(x, t) = \begin{cases} C \exp\!\left(-\dfrac{n^2 \pi^2}{4a^2} t\right)\sin\!\left(\dfrac{n\pi(x + a)}{2a}\right) & (-a < x < a) \\ 0 & (|x| \ge a) \end{cases} \quad (C \neq 0,\; n = 1, 2, \dots)}
$$

が条件を満たす解である。

#### (5) 非線形常微分方程式（ベルヌーイ型）

$y(0) = A > 0$ であり，$y \equiv 0$ は方程式の解であるため，解の一意性より解の存在区間内で $y(x) \neq 0$ である。そこで $u(x) = \dfrac{1}{y(x)}$ と変数変換すると，$\dfrac{\mathrm{d}y}{\mathrm{d}x} = -\dfrac{1}{u^2}\dfrac{\mathrm{d}u}{\mathrm{d}x}$ より方程式は

$$
\begin{aligned}
-\frac{1}{u^2}\frac{\mathrm{d}u}{\mathrm{d}x} &= -\alpha\left(1 - \frac{\beta}{u}\right)\frac{1}{u} \\
\frac{\mathrm{d}u}{\mathrm{d}x} &= \alpha(u - \beta)
\end{aligned}
$$

と 1 階線形常微分方程式に変形される。これを (1) と同様に解くと，初期条件 $u(0) = \dfrac{1}{A}$ より

$$
\begin{aligned}
u(x) - \beta &= \left(u(0) - \beta\right) e^{\alpha x} = \left(\frac{1}{A} - \beta\right) e^{\alpha x} \\
u(x) &= \beta + \left(\frac{1}{A} - \beta\right) e^{\alpha x} = \frac{A\beta + (1 - A\beta) e^{\alpha x}}{A}
\end{aligned}
$$

となる。$y(x) = \dfrac{1}{u(x)}$ より，求める解は

$$
\finalanswer{y(x) = \frac{A}{A\beta + (1 - A\beta) e^{\alpha x}}}
$$

である（$A\beta = 1$ のときは定数解 $y(x) = \dfrac{1}{\beta}$ に一致する）。

<aside class="rigor-note" markdown>
**補足**：(5) の解の存在区間は初期値 $A$ と平衡点 $1/\beta$ の大小関係に依存する。$0 < A \le 1/\beta$ のときは分母がすべての実数 $x$ で正となるため，解は全実数軸上で大域的に存在し，$x \to +\infty$ で $0$（$A = 1/\beta$ なら $1/\beta$），$x \to -\infty$ で $1/\beta$ に漸近する。一方，$A > 1/\beta$ のときは $x_* = \dfrac{1}{\alpha}\ln\!\left(\dfrac{A\beta}{A\beta - 1}\right) > 0$ で分母が $0$ となって発散するため，初期値 $x = 0$ を含む解の存在区間は $x < x_*$ である。
</aside>
