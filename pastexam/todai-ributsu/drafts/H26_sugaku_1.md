---
title: 東大理物 平成26年度 数学 第1問：常微分方程式・連立微分方程式・熱伝導方程式
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成26年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成26年度 数学 第1問：常微分方程式・連立微分方程式・熱伝導方程式

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

> 出典：東京大学大学院理学系研究科物理学専攻 平成26年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
1階の線形微分方程式は，両辺に積分因子を掛けると，左辺が1つの関数の微分になり，積分して解くことができます。連立方程式は，一方の式から求めた解をもう一方に代入するか，係数行列の固有ベクトルの方向に分けると，1階の方程式を順に解く形になります。

熱伝導方程式は，解を時間の関数と位置の関数の積とおくと，2つの常微分方程式に分かれます。境界条件を満たす位置の関数を選び，その和で初期条件を表します。非線形の方程式は，$y$ の逆数を新しい未知関数にすると，線形の方程式になります。
</div>

### (1)
両辺に積分因子 $e^{\alpha x}$ を掛けて整理します。

$$
\begin{aligned}
e^{\alpha x}\frac{\mathrm{d}y}{\mathrm{d}x} + \alpha e^{\alpha x} y &= 0 \\
\frac{\mathrm{d}}{\mathrm{d}x}\left(e^{\alpha x} y\right) &= 0
\end{aligned}
$$

よって $e^{\alpha x}y(x)=C$ となります。ここで $C$ は積分定数です。初期条件から $C=Ae^{\alpha b}$ なので，求める解は次のとおりです。$A=0$ の場合も同じ導出が成り立ちます。

$$
\finalanswer{y(x) = A e^{-\alpha(x - b)}}
$$

### (2)
第 1 式と初期条件 $y_1(0) = A$ より，(1) と同様にして $y_1(x) = A e^{-\alpha x}$ が得られます。これを第 2 式に代入して両辺に積分因子 $e^{\gamma x}$ を掛けると，次式が得られます。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}x}\left(e^{\gamma x} y_2\right) &= \beta A e^{(\gamma - \alpha) x} \\
e^{\gamma x} y_2(x) - y_2(0) &= \beta A \int_0^x e^{(\gamma - \alpha) s}\,\mathrm{d}s \\
&= \frac{\beta A}{\gamma - \alpha}\left(e^{(\gamma - \alpha)x} - 1\right)
\end{aligned}
$$

$y_2(0) = 0$ より，$y_2(x) = \dfrac{\beta A}{\gamma - \alpha}\left(e^{-\alpha x} - e^{-\gamma x}\right)$ となります。

次に，$y_1(x)$ と $y_2(x)$ の符号を調べます。$A > 0$ より，すべての実数 $x$ に対して $y_1(x) = A e^{-\alpha x} > 0$ です。また，$y_2(x)$ を

$$
y_2(x) = \beta A e^{-\alpha x}\,\frac{1 - e^{-(\gamma - \alpha) x}}{\gamma - \alpha}
$$

と書き換えると，$\beta A e^{-\alpha x} > 0$ なので，符号は $\dfrac{1 - e^{-(\gamma - \alpha)x}}{\gamma - \alpha}$ の符号に一致します。

- $x > 0$ のとき：$\gamma > \alpha$ なら分子・分母とも正，$\gamma < \alpha$ なら分子・分母とも負であるため，いずれの場合も $y_2(x) > 0$ です。
- $x = 0$ のとき：$y_2(0) = 0$ です。
- $x < 0$ のとき：$\gamma > \alpha$ なら分子が負・分母が正，$\gamma < \alpha$ なら分子が正・分母が負であるため，いずれの場合も $y_2(x) < 0$ です。

$$
\finalanswer{y_1(x) = A e^{-\alpha x}, \qquad y_2(x) = \frac{\beta A}{\gamma - \alpha}\left(e^{-\alpha x} - e^{-\gamma x}\right)}
$$



### (3)
方程式を行列形式で書きます。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = c M \begin{pmatrix} y_1 \\ y_2 \end{pmatrix}, \qquad M = \begin{pmatrix} -1 & \sqrt{3} \\ \sqrt{3} & -3 \end{pmatrix}
$$

$M$ の固有方程式は

$$
\begin{aligned}
\det(M - \lambda I) &= (\lambda + 1)(\lambda + 3) - 3 \\
&= \lambda(\lambda + 4) \\
&= 0
\end{aligned}
$$

より，固有値は $\lambda_1 = 0$，$\lambda_2 = -4$ です。それぞれに対応する規格化された固有ベクトルは次のとおりです。

$$
\boldsymbol{v}_1 = \frac{1}{2}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}, \qquad \boldsymbol{v}_2 = \frac{1}{2}\begin{pmatrix} -1 \\ \sqrt{3} \end{pmatrix}
$$

初期値ベクトルを $\boldsymbol{v}_1, \boldsymbol{v}_2$ で展開すると，

$$
\begin{pmatrix} y_1(0) \\ y_2(0) \end{pmatrix}
= \frac{1}{2}\begin{pmatrix} \sqrt{3} - 1 \\ \sqrt{3} + 1 \end{pmatrix}
= \boldsymbol{v}_1 + \boldsymbol{v}_2
$$

と表されます。したがって，一般解に初期条件を代入すると次の結果が得られます。

$$
\begin{pmatrix} y_1(x) \\ y_2(x) \end{pmatrix}
= e^{\lambda_1 c x}\boldsymbol{v}_1 + e^{\lambda_2 c x}\boldsymbol{v}_2
= \frac{1}{2}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix} + \frac{1}{2}e^{-4cx}\begin{pmatrix} -1 \\ \sqrt{3} \end{pmatrix}
$$

$$
\finalanswer{y_1(x) = \frac{\sqrt{3} - e^{-4cx}}{2}, \qquad y_2(x) = \frac{1 + \sqrt{3}\,e^{-4cx}}{2}}
$$

### (4)
$-a < x < a$ の領域で変数分離解 $y(x, t) = X(x) T(t)$ を仮定し，偏微分方程式に代入します。

$$
\begin{aligned}
\frac{1}{T(t)}\frac{\mathrm{d}T}{\mathrm{d}t} &= \frac{1}{X(x)}\frac{\mathrm{d}^2 X}{\mathrm{d}x^2} \\
&= -k^2
\end{aligned}
$$

ここで $k$ は実定数です。分離定数が $0$ または正のとき，境界条件 $X(-a)=X(a)=0$ を満たす $0$ でない解はありません。$-k^2$ と選んだ場合は $T(t)=e^{-k^2t}$，$X(x)=C_1\cos(kx)+C_2\sin(kx)$ が得られます。

境界条件 $X(-a) = X(a) = 0$ より，零でない解は $k_n = \dfrac{n\pi}{2a}$（$n = 1, 2, 3, \dots$）に対して

$$
X_n(x) = \sin\!\left(\frac{n\pi(x + a)}{2a}\right)
$$

と与えられます。奇数 $n$ では $\cos\!\left(\dfrac{n\pi x}{2a}\right)$，偶数 $n$ では $\sin\!\left(\dfrac{n\pi x}{2a}\right)$ に比例します。特に $n=1$ を選べば，$C\neq0$ を任意の実定数として

$$
y(x, t) = \begin{cases} C \exp\!\left(-\dfrac{\pi^2}{4a^2} t\right)\cos\!\left(\dfrac{\pi x}{2a}\right) & (-a < x < a) \\ 0 & (|x| \ge a) \end{cases}
$$

は $-a < x < a$ で微分可能であり，定数でない解の一つを与えます。より一般に，任意の自然数 $n$ に対して次の関数が条件を満たす解です。

$$
\finalanswer{y_n(x, t) = \begin{cases} C \exp\!\left(-\dfrac{n^2 \pi^2}{4a^2} t\right)\sin\!\left(\dfrac{n\pi(x + a)}{2a}\right) & (-a < x < a) \\ 0 & (|x| \ge a) \end{cases} \quad (C \neq 0,\; n = 1, 2, \dots)}
$$

### (5)
$y(0) = A > 0$ であり，$y \equiv 0$ は方程式の解であるため，解の一意性より解の存在区間内で $y(x) \neq 0$ です。そこで $u(x) = \dfrac{1}{y(x)}$ と変数変換します。$\dfrac{\mathrm{d}y}{\mathrm{d}x} = -\dfrac{1}{u^2}\dfrac{\mathrm{d}u}{\mathrm{d}x}$ より，方程式は次のように 1 階線形常微分方程式に変形されます。

$$
\begin{aligned}
-\frac{1}{u^2}\frac{\mathrm{d}u}{\mathrm{d}x} &= -\alpha\left(1 - \frac{\beta}{u}\right)\frac{1}{u} \\
\frac{\mathrm{d}u}{\mathrm{d}x} &= \alpha(u - \beta)
\end{aligned}
$$

これを (1) と同様に解くと，初期条件 $u(0) = \dfrac{1}{A}$ より次のようになります。

$$
\begin{aligned}
u(x) - \beta &= \left(u(0) - \beta\right) e^{\alpha x} \\
&= \left(\frac{1}{A} - \beta\right) e^{\alpha x} \\
u(x) &= \beta + \left(\frac{1}{A} - \beta\right) e^{\alpha x} \\
&= \frac{A\beta + (1 - A\beta) e^{\alpha x}}{A}
\end{aligned}
$$

$y(x)=\dfrac{1}{u(x)}$ より，求める解は次のとおりです。$A\beta=1$ の場合は定数解 $y(x)=\dfrac{1}{\beta}$ に一致します。

$$
\finalanswer{y(x) = \frac{A}{A\beta + (1 - A\beta) e^{\alpha x}}}
$$

<aside class="rigor-note" markdown>
(5) の解の存在区間は，初期値 $A$ と平衡点 $1/\beta$ の大小関係に依存します。$0<A<1/\beta$ では分母が全実数 $x$ で正なので，解は全実数軸上で存在します。$x\to+\infty$ で $0$，$x\to-\infty$ で $1/\beta$ に漸近します。$A=1/\beta$ では，常に $y(x)=1/\beta$ です。

$A>1/\beta$ では $x_*=\dfrac{1}{\alpha}\ln\!\left(\dfrac{A\beta}{A\beta-1}\right)>0$ で分母が $0$ になります。初期値 $x=0$ を含む解の存在区間は $x<x_*$ です。
</aside>
