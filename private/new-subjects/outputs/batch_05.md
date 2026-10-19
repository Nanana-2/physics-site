===== FILE: 07linear_algebra/04/04_010.md =====
---
tags:
  - 基本
---

# 内積とノルム

## 問題
実内積空間 $V$ において，元 $\boldsymbol{x}, \boldsymbol{y}$ の内積を $(\boldsymbol{x}, \boldsymbol{y})$ と表し，ノルムを $\|\boldsymbol{x}\| = \sqrt{(\boldsymbol{x}, \boldsymbol{x})}$ と定義する。以下の問いに答えよ。

(1) 任意の実数 $t$ に対し，二次式 $f(t) = \|\boldsymbol{x} + t\boldsymbol{y}\|^2$ を $t$ について降べきの順に整理せよ。

(2) すべての実数 $t$ に対して $f(t) \ge 0$ が成り立つことを用いて，コーシー・シュワルツの不等式を示せ。

(3) コーシー・シュワルツの不等式を用いて，三角不等式 $\|\boldsymbol{x} + \boldsymbol{y}\| \le \|\boldsymbol{x}\| + \|\boldsymbol{y}\|$ を示せ。

---

## 解答・解説

### (1)
ノルムの定義にしたがって内積の線形性と対称性を用いて展開します。実内積空間の性質より $(\boldsymbol{x}, \boldsymbol{y}) = (\boldsymbol{y}, \boldsymbol{x})$ が成り立ちます。

ノルムの定義式を展開すると，
$$
\begin{aligned}
f(t) &= (\boldsymbol{x} + t\boldsymbol{y}, \boldsymbol{x} + t\boldsymbol{y}) \\
&= (\boldsymbol{x}, \boldsymbol{x}) + 2t(\boldsymbol{x}, \boldsymbol{y}) + t^2(\boldsymbol{y}, \boldsymbol{y}) \\
&= \finalanswer{\|\boldsymbol{y}\|^2 t^2 + 2(\boldsymbol{x}, \boldsymbol{y})t + \|\boldsymbol{x}\|^2}
\end{aligned}
$$
となります。

### (2)
ノルムの非負性により，すべての実数 $t$ に対して $f(t) = \|\boldsymbol{x} + t\boldsymbol{y}\|^2 \ge 0$ が常に成立します。

$\boldsymbol{y} = \boldsymbol{0}$ のときは両辺ともに $0$ となり等号が成り立ちます。$\boldsymbol{y} \neq \boldsymbol{0}$ のとき，$\|\boldsymbol{y}\|^2 > 0$ であるため，$f(t)$ は下に凸な $t$ の二次関数となります。これが常に非負である条件は，二次方程式 $f(t) = 0$ の判別式 $D$ が $0$ 以下であることです。

判別式の条件を計算すると，
$$
\begin{aligned}
\frac{D}{4} = (\boldsymbol{x}, \boldsymbol{y})^2 - \|\boldsymbol{x}\|^2 \|\boldsymbol{y}\|^2 \le 0
\end{aligned}
$$
となります。

したがって，項を移行すると，
$$
\finalanswer{(\boldsymbol{x}, \boldsymbol{y})^2 \le \|\boldsymbol{x}\|^2 \|\boldsymbol{y}\|^2}
$$
となります。両辺の非負の平方根をとれば $|(\boldsymbol{x}, \boldsymbol{y})| \le \|\boldsymbol{x}\| \|\boldsymbol{y}\|$ が得られます。

### (3)
和のノルムの二乗を展開し，コーシー・シュワルツの不等式を適用します。

和のノルムの二乗を計算すると，
$$
\begin{aligned}
\|\boldsymbol{x} + \boldsymbol{y}\|^2 &= \|\boldsymbol{x}\|^2 + 2(\boldsymbol{x}, \boldsymbol{y}) + \|\boldsymbol{y}\|^2
\end{aligned}
$$
となります。

不等式 $(\boldsymbol{x}, \boldsymbol{y}) \le |(\boldsymbol{x}, \boldsymbol{y})| \le \|\boldsymbol{x}\| \|\boldsymbol{y}\|$ を代入すると，
$$
\begin{aligned}
\|\boldsymbol{x} + \boldsymbol{y}\|^2 &\le \|\boldsymbol{x}\|^2 + 2\|\boldsymbol{x}\|\|\boldsymbol{y}\| + \|\boldsymbol{y}\|^2 \\
&= (\|\boldsymbol{x}\| + \|\boldsymbol{y}\|)^2
\end{aligned}
$$
となります。

両辺ともに非負の実数であるため，平方根をとると，
$$
\finalanswer{\|\boldsymbol{x} + \boldsymbol{y}\| \le \|\boldsymbol{x}\| + \|\boldsymbol{y}\|}
$$
となります。
===== FILE: 07linear_algebra/04/04_020.md =====
---
tags:
  - 基本
---

# グラム・シュミットの直交化

## 問題
3次元実数ベクトル空間 $\mathbb{R}^3$ の標準内積において，次の3つの一次独立なベクトルを考える。
$$
\boldsymbol{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \quad \boldsymbol{v}_2 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \boldsymbol{v}_3 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}
$$
グラム・シュミットの直交化法を用いて正規直交基底 $\{\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3\}$ を構成する。以下の問いに答えよ。

(1) $\boldsymbol{v}_1$ を正規化して単位ベクトル $\boldsymbol{e}_1$ を求めよ。

(2) $\boldsymbol{v}_2$ から $\boldsymbol{e}_1$ 方向の成分を除いた直交ベクトルを求め，それを正規化して単位ベクトル $\boldsymbol{e}_2$ を求めよ。

(3) $\boldsymbol{v}_3$ から $\boldsymbol{e}_1$ および $\boldsymbol{e}_2$ 方向の成分を除いた直交ベクトルを求め，それを正規化して単位ベクトル $\boldsymbol{e}_3$ を求めよ。

---

## 解答・解説

### (1)
ベクトルのノルムを計算し，自身をノルムで割ることで単位ベクトルを求めます。

$\boldsymbol{v}_1$ のノルムを計算すると，
$$
\begin{aligned}
\|\boldsymbol{v}_1\| &= \sqrt{1^2 + 0^2 + 1^2} \\
&= \sqrt{2}
\end{aligned}
$$
となります。

したがって，正規化したベクトルは，
$$
\boldsymbol{e}_1 = \frac{\boldsymbol{v}_1}{\|\boldsymbol{v}_1\|} = \finalanswer{\frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}}
$$
となります。

### (2)
$\boldsymbol{v}_2$ の $\boldsymbol{e}_1$ 方向への正射影成分を差し引いて直交ベクトル $\boldsymbol{u}_2$ を構成します。

内積を計算すると，
$$
\begin{aligned}
(\boldsymbol{v}_2, \boldsymbol{e}_1) &= 1 \cdot \frac{1}{\sqrt{2}} + 1 \cdot 0 + 0 \cdot \frac{1}{\sqrt{2}} \\
&= \frac{1}{\sqrt{2}}
\end{aligned}
$$
となります。

直交ベクトル $\boldsymbol{u}_2 = \boldsymbol{v}_2 - (\boldsymbol{v}_2, \boldsymbol{e}_1)\boldsymbol{e}_1$ を計算すると，
$$
\begin{aligned}
\boldsymbol{u}_2 &= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} - \frac{1}{\sqrt{2}} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \\
&= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} - \begin{pmatrix} 1/2 \\ 0 \\ 1/2 \end{pmatrix} \\
&= \begin{pmatrix} 1/2 \\ 1 \\ -1/2 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}
\end{aligned}
$$
となります。

$\boldsymbol{u}_2$ のノルムを求めると，
$$
\begin{aligned}
\|\boldsymbol{u}_2\| &= \frac{1}{2} \sqrt{1^2 + 2^2 + (-1)^2} \\
&= \frac{\sqrt{6}}{2}
\end{aligned}
$$
となります。

よって，正規化した単位ベクトルは，
$$
\boldsymbol{e}_2 = \frac{\boldsymbol{u}_2}{\|\boldsymbol{u}_2\|} = \finalanswer{\frac{1}{\sqrt{6}} \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}}
$$
となります。

### (3)
$\boldsymbol{v}_3$ から $\boldsymbol{e}_1$ および $\boldsymbol{e}_2$ の両方向への射影成分を差し引きます。

各基底ベクトルとの内積を計算すると，
$$
\begin{aligned}
(\boldsymbol{v}_3, \boldsymbol{e}_1) &= 0 \cdot \frac{1}{\sqrt{2}} + 1 \cdot 0 + 1 \cdot \frac{1}{\sqrt{2}} = \frac{1}{\sqrt{2}} \\
(\boldsymbol{v}_3, \boldsymbol{e}_2) &= 0 \cdot \frac{1}{\sqrt{6}} + 1 \cdot \frac{2}{\sqrt{6}} + 1 \cdot \left(-\frac{1}{\sqrt{6}}\right) = \frac{1}{\sqrt{6}}
\end{aligned}
$$
となります。

直交ベクトル $\boldsymbol{u}_3 = \boldsymbol{v}_3 - (\boldsymbol{v}_3, \boldsymbol{e}_1)\boldsymbol{e}_1 - (\boldsymbol{v}_3, \boldsymbol{e}_2)\boldsymbol{e}_2$ を求めると，
$$
\begin{aligned}
\boldsymbol{u}_3 &= \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - \frac{1}{2} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} - \frac{1}{6} \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \\
&= \begin{pmatrix} -1/2 - 1/6 \\ 1 - 2/6 \\ 1 - 1/2 + 1/6 \end{pmatrix} \\
&= \begin{pmatrix} -2/3 \\ 2/3 \\ 2/3 \end{pmatrix} = \frac{2}{3} \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}
\end{aligned}
$$
となります。

ノルムを計算すると $\|\boldsymbol{u}_3\| = (2/3)\sqrt{(-1)^2 + 1^2 + 1^2} = 2/\sqrt{3}$ となります。

したがって，正規化した単位ベクトルは，
$$
\boldsymbol{e}_3 = \frac{\boldsymbol{u}_3}{\|\boldsymbol{u}_3\|} = \finalanswer{\frac{1}{\sqrt{3}} \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}}
$$
となります。
===== FILE: 07linear_algebra/04/04_030.md =====
---
tags:
  - 標準
---

# 直交射影と最小二乗法

## 問題
$m \times n$ 実数行列 $A$ は列フルランク（$\operatorname{rank} A = n$ かつ $m > n$）とする。ベクトル $\boldsymbol{b} \in \mathbb{R}^m$ に対して連立方程式 $A\boldsymbol{x} = \boldsymbol{b}$ が厳密な解をもたないとき，残差ノルムの二乗 $S(\boldsymbol{x}) = \|A\boldsymbol{x} - \boldsymbol{b}\|^2$ を最小にする最小二乗解 $\hat{\boldsymbol{x}}$ を求める。以下の問いに答えよ。

(1) 残差ベクトル $\boldsymbol{b} - A\hat{\boldsymbol{x}}$ が $A$ の値域内の任意のベクトル $A\boldsymbol{y}$（$\boldsymbol{y} \in \mathbb{R}^n$）と直交する条件から，$\hat{\boldsymbol{x}}$ が満たすべき正規方程式を導け。

(2) 正方行列 $A^{\mathsf{T}} A$ が正則であることを示し，最小二乗解 $\hat{\boldsymbol{x}}$ を $A$ と $\boldsymbol{b}$ を用いて表せ。

(3) $\boldsymbol{b}$ の値域への直交射影ベクトルを $\boldsymbol{p} = A\hat{\boldsymbol{x}}$ とする。$\boldsymbol{p} = P\boldsymbol{b}$ を満たす射影行列 $P$ を $A$ を用いて表せ。

---

## 解答・解説

### (1)
残差ベクトルが $A$ の列空間全体と直交するという幾何学的条件を式に表します。

すべての $\boldsymbol{y} \in \mathbb{R}^n$ に対して内積が $0$ となることから，
$$
\begin{aligned}
(A\boldsymbol{y})^{\mathsf{T}} (\boldsymbol{b} - A\hat{\boldsymbol{x}}) &= 0 \\
\boldsymbol{y}^{\mathsf{T}} A^{\mathsf{T}} (\boldsymbol{b} - A\hat{\boldsymbol{x}}) &= 0 \\
\boldsymbol{y}^{\mathsf{T}} (A^{\mathsf{T}}\boldsymbol{b} - A^{\mathsf{T}} A\hat{\boldsymbol{x}}) &= 0
\end{aligned}
$$
となります。

この等式が任意のベクトル $\boldsymbol{y}$ に対して成立するためには，括弧内のベクトルがゼロベクトルでなければなりません。

したがって，求める正規方程式は，
$$
\finalanswer{A^{\mathsf{T}} A \hat{\boldsymbol{x}} = A^{\mathsf{T}} \boldsymbol{b}}
$$
となります。

### (2)
$A^{\mathsf{T}} A$ の核がゼロベクトルのみからなることを確認して正則性を示します。

$A^{\mathsf{T}} A \boldsymbol{v} = \boldsymbol{0}$ を満たす任意のベクトル $\boldsymbol{v} \in \mathbb{R}^n$ を考えます。左から $\boldsymbol{v}^{\mathsf{T}}$ を掛けると，
$$
\begin{aligned}
\boldsymbol{v}^{\mathsf{T}} A^{\mathsf{T}} A \boldsymbol{v} &= 0 \\
(A\boldsymbol{v})^{\mathsf{T}} (A\boldsymbol{v}) &= 0 \\
\|A\boldsymbol{v}\|^2 &= 0
\end{aligned}
$$
となり，$A\boldsymbol{v} = \boldsymbol{0}$ が導かれます。

$A$ は列フルランクであり，列ベクトルは一次独立であるため，$A\boldsymbol{v} = \boldsymbol{0}$ から直ちに $\boldsymbol{v} = \boldsymbol{0}$ が従います。核がゼロベクトルのみであるため $n$ 次正方行列 $A^{\mathsf{T}} A$ は正則であり，逆行列 $(A^{\mathsf{T}} A)^{-1}$ が存在します。

正規方程式の両辺に左から逆行列を掛けると，
$$
\finalanswer{\hat{\boldsymbol{x}} = (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} \boldsymbol{b}}
$$
となります。

### (3)
得られた最小二乗解 $\hat{\boldsymbol{x}}$ を射影ベクトルの式に代入します。

射影ベクトル $\boldsymbol{p}$ を計算すると，
$$
\begin{aligned}
\boldsymbol{p} &= A\hat{\boldsymbol{x}} \\
&= A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} \boldsymbol{b}
\end{aligned}
$$
となります。

$\boldsymbol{p} = P\boldsymbol{b}$ と比較すると，射影行列は，
$$
\finalanswer{P = A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}}
$$
となります。この行列は $P^2 = P$ および $P^{\mathsf{T}} = P$ を満たす対称射影行列となります。
===== FILE: 07linear_algebra/04/04_040.md =====
---
tags:
  - 基本
---

# 直交行列と回転

## 問題
3次実正方行列 $R$ は直交行列（$R^{\mathsf{T}}R = I$）であり，$\det R = 1$ を満たすとする。以下の問いに答えよ。

(1) 行列式の性質を用いて，$\det(R - I) = 0$ が成り立つことを示せ。

(2) 固有値 $1$ に属する実固有ベクトル $\boldsymbol{n}$ が存在し，$\boldsymbol{n}$ と平行な任意のベクトル $\boldsymbol{v} = c\boldsymbol{n}$（$c$ は実数）に対して $R\boldsymbol{v} = \boldsymbol{v}$ となることを示せ。

(3) $z$ 軸まわりの角度 $\theta$ の回転を表す直交行列
$$
R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
の固有値をすべて求めよ。

---

## 解答・解説

### (1)
転置行列の行列式が元の行列式に等しいこと，および直交行列の性質を利用します。

3次単位行列 $I$ に対して，
$$
\begin{aligned}
\det(R - I) &= \det\left((R - I)^{\mathsf{T}}\right) \\
&= \det(R^{\mathsf{T}} - I) \\
&= \det\left(R^{\mathsf{T}}(I - R)\right)
\end{aligned}
$$
となります。

行列式の積の性質，および 3次行列の符号の取り出しを行うと，
$$
\begin{aligned}
\det\left(R^{\mathsf{T}}(I - R)\right) &= \det(R^{\mathsf{T}}) \det(I - R) \\
&= 1 \cdot \det(-(R - I)) \\
&= (-1)^3 \det(R - I) \\
&= -\det(R - I)
\end{aligned}
$$
となります。

したがって，
$$
\begin{aligned}
2\det(R - I) &= 0
\end{aligned}
$$
となり，
$$
\finalanswer{\det(R - I) = 0}
$$
となります。

### (2)
特性方程式から固有ベクトルの存在を導き，線形性を適用します。

(1)より $\det(R - 1 \cdot I) = 0$ であるため，$\lambda = 1$ は $R$ の固有値です。$R$ は実行列であり固有値 $1$ は実数であるため，対応する固有方程式 $(R - I)\boldsymbol{n} = \boldsymbol{0}$ は非自明な実数解 $\boldsymbol{n} \neq \boldsymbol{0}$ をもちます。

この固有ベクトルに対し，任意の実数スカラー $c$ を掛けると，
$$
\begin{aligned}
R\boldsymbol{v} &= R(c\boldsymbol{n}) \\
&= c(R\boldsymbol{n}) \\
&= c\boldsymbol{n} \\
&= \finalanswer{\boldsymbol{v}}
\end{aligned}
$$
となります。この $\boldsymbol{n}$ が張る直線上の点は回転変換によって変化しないため，$\boldsymbol{n}$ は回転軸の方向ベクトルを表します。

### (3)
特性方程式を立てて解を計算します。

特性方程式を計算すると，
$$
\begin{aligned}
\det(R_z(\theta) - \lambda I) &= \begin{vmatrix} \cos\theta - \lambda & -\sin\theta & 0 \\ \sin\theta & \cos\theta - \lambda & 0 \\ 0 & 0 & 1 - \lambda \end{vmatrix} \\
&= (1 - \lambda) \left( (\cos\theta - \lambda)^2 + \sin^2\theta \right) \\
&= (1 - \lambda) (\lambda^2 - 2\lambda\cos\theta + 1) = 0
\end{aligned}
$$
となります。

二次方程式 $\lambda^2 - 2\lambda\cos\theta + 1 = 0$ を解くと，
$$
\begin{aligned}
\lambda &= \cos\theta \pm \sqrt{\cos^2\theta - 1} \\
&= \cos\theta \pm i\sin\theta = e^{\pm i\theta}
\end{aligned}
$$
となります。

したがって，求める3つの固有値は，
$$
\finalanswer{\lambda = 1, \quad e^{i\theta}, \quad e^{-i\theta}}
$$
となります。
===== FILE: 07linear_algebra/04/04_050.md =====
---
tags:
  - 標準
---

# 実対称行列の直交対角化

## 問題
実行列 $A$ は対称行列（$A^{\mathsf{T}} = A$）であるとする。以下の問いに答えよ。

(1) $A$ の相異なる2つの固有値 $\lambda_1, \lambda_2$（$\lambda_1 \neq \lambda_2$）に対応する固有ベクトルをそれぞれ $\boldsymbol{x}_1, \boldsymbol{x}_2$ とするとき，標準内積 $(\boldsymbol{x}_1, \boldsymbol{x}_2) = \boldsymbol{x}_1^{\mathsf{T}}\boldsymbol{x}_2 = 0$ が成り立つことを示せ。

(2) 実対称行列
$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}
$$
のすべての固有値と，それらに対応する長さ $1$ の固有ベクトルを求めよ。

(3) (2)で求めた固有ベクトルを列とする直交行列 $P$ を構成し，$P^{\mathsf{T}}AP$ を計算して対角化せよ。

---

## 解答・解説

### (1)
内積の結合律と行列の対称性を利用して関係式を導きます。

$\boldsymbol{x}_1^{\mathsf{T}} A \boldsymbol{x}_2$ を2通りの方法で計算します。一方では，
$$
\begin{aligned}
\boldsymbol{x}_1^{\mathsf{T}} (A \boldsymbol{x}_2) &= \boldsymbol{x}_1^{\mathsf{T}} (\lambda_2 \boldsymbol{x}_2) \\
&= \lambda_2 \boldsymbol{x}_1^{\mathsf{T}} \boldsymbol{x}_2
\end{aligned}
$$
となります。他方では，転置の公式と $A^{\mathsf{T}} = A$ を用いて，
$$
\begin{aligned}
(A \boldsymbol{x}_1)^{\mathsf{T}} \boldsymbol{x}_2 &= (\lambda_1 \boldsymbol{x}_1)^{\mathsf{T}} \boldsymbol{x}_2 \\
&= \lambda_1 \boldsymbol{x}_1^{\mathsf{T}} \boldsymbol{x}_2
\end{aligned}
$$
となります。両者は同一の量であるため，差をとると，
$$
\begin{aligned}
(\lambda_1 - \lambda_2) \boldsymbol{x}_1^{\mathsf{T}} \boldsymbol{x}_2 &= 0
\end{aligned}
$$
となります。

前提条件より $\lambda_1 \neq \lambda_2$ であるため，
$$
\finalanswer{\boldsymbol{x}_1^{\mathsf{T}}\boldsymbol{x}_2 = 0}
$$
となります。

### (2)
特性方程式を解いて固有値と固有ベクトルを求めます。

特性方程式を計算すると，
$$
\begin{aligned}
\det(A - \lambda I) &= \begin{vmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{vmatrix} \\
&= (2 - \lambda)^2 - 1 \\
&= \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3) = 0
\end{aligned}
$$
となり，固有値は $\lambda = 1, 3$ となります。

$\lambda_1 = 1$ のとき，$(A - I)\boldsymbol{x} = \boldsymbol{0}$ より，
$$
\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$x_1 + x_2 = 0$ を得ます。規格化条件 $x_1^2 + x_2^2 = 1$ を課すと，
$$
\boldsymbol{u}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$
となります。

$\lambda_2 = 3$ のとき，$(A - 3I)\boldsymbol{x} = \boldsymbol{0}$ より，
$$
\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$x_1 - x_2 = 0$ を得ます。規格化すると，
$$
\boldsymbol{u}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$
となります。

したがって，求める固有値と規格化固有ベクトルは，
$$
\finalanswer{\lambda_1 = 1, \quad \boldsymbol{u}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}; \quad \lambda_2 = 3, \quad \boldsymbol{u}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}}
$$
となります。

### (3)
得られた正規直交基底を並べて変換行列を構成します。

直交行列を $P = (\boldsymbol{u}_1 \ \boldsymbol{u}_2)$ と定義すると，
$$
P = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}
$$
となります。

転置行列との積を計算すると，
$$
\begin{aligned}
P^{\mathsf{T}} A P &= \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} 1 & -1 \\ 3 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} \\
&= \finalanswer{\begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}}
\end{aligned}
$$
となります。対角成分には固有値が並びます。
===== FILE: 07linear_algebra/04/04_060.md =====
---
tags:
  - 標準
---

# 二次形式の標準形

## 問題
実変数 $x, y$ の二次形式
$$
q(x, y) = 5x^2 - 4xy + 8y^2
$$
を考える。以下の問いに答えよ。

(1) 列ベクトル $\boldsymbol{x} = \begin{pmatrix} x \\ y \end{pmatrix}$ を用いて $q(x, y) = \boldsymbol{x}^{\mathsf{T}} A \boldsymbol{x}$ と表すとき，実対称行列 $A$ を求めよ。

(2) $A$ の固有値を求め，適当な直交変換 $\boldsymbol{x} = P\boldsymbol{x}'$（$\boldsymbol{x}' = \begin{pmatrix} x' \\ y' \end{pmatrix}$）によって $q$ を標準形 $\lambda_1 (x')^2 + \lambda_2 (y')^2$ の形に変換せよ。

(3) 二次形式 $q(x, y)$ が $(x, y) \neq (0, 0)$ に対して常に正の値をとる（正定値である）ことを示し，方程式 $q(x, y) = 1$ が $xy$ 平面上で表す曲線の形状を答えよ。

---

## 解答・解説

### (1)
交差項 $-4xy$ の係数を対称に半分ずつ分割して非対角成分に配置します。

二次形式を行列表現に書き直すと，
$$
\begin{aligned}
q(x, y) &= 5x^2 - 2xy - 2yx + 8y^2 \\
&= \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 5 & -2 \\ -2 & 8 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
\end{aligned}
$$
となります。

したがって，対称行列 $A$ は，
$$
\finalanswer{A = \begin{pmatrix} 5 & -2 \\ -2 & 8 \end{pmatrix}}
$$
となります。

### (2)
行列 $A$ の特性方程式を解いて主軸の伸縮率を求めます。

特性方程式を計算すると，
$$
\begin{aligned}
\det(A - \lambda I) &= \begin{vmatrix} 5 - \lambda & -2 \\ -2 & 8 - \lambda \end{vmatrix} \\
&= (5 - \lambda)(8 - \lambda) - 4 \\
&= \lambda^2 - 13\lambda + 36 = (\lambda - 4)(\lambda - 9) = 0
\end{aligned}
$$
となり，固有値は $\lambda_1 = 4, \lambda_2 = 9$ となります。

直交行列 $P$ による座標変換 $\boldsymbol{x} = P\boldsymbol{x}'$ を施すと，
$$
\begin{aligned}
q &= (P\boldsymbol{x}')^{\mathsf{T}} A (P\boldsymbol{x}') \\
&= (\boldsymbol{x}')^{\mathsf{T}} (P^{\mathsf{T}} A P) \boldsymbol{x}' \\
&= \begin{pmatrix} x' & y' \end{pmatrix} \begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix} \begin{pmatrix} x' \\ y' \end{pmatrix}
\end{aligned}
$$
となります。

したがって，標準形は，
$$
\finalanswer{q = 4(x')^2 + 9(y')^2}
$$
となります。

### (3)
標準形における各変数の二乗の係数に着目します。

直交変換はベクトルの長さを保つため，$(x, y) \neq (0, 0)$ であることと $(x', y') \neq (0, 0)$ であることは同値です。

固有値がともに正（$\lambda_1 = 4 > 0, \lambda_2 = 9 > 0$）であるため，
$$
\begin{aligned}
q(x, y) &= 4(x')^2 + 9(y')^2 > 0
\end{aligned}
$$
となり，正定値性が示されます。

また，方程式 $q(x, y) = 1$ は新座標において，
$$
\begin{aligned}
\frac{(x')^2}{(1/2)^2} + \frac{(y')^2}{(1/3)^2} = 1
\end{aligned}
$$
と表されます。

したがって，曲線の形状は，
$$
\finalanswer{\text{楕円}}
$$
となります。主軸の長さは直交行列 $P$ の回転角に対応して傾いた楕円を表します。
===== FILE: 07linear_algebra/05/05_010.md =====
---
tags:
  - 基本
---

# エルミート行列の固有値

## 問題
複素ベクトル空間 $\mathbb{C}^n$ における内積を $(\boldsymbol{x}, \boldsymbol{y}) = \boldsymbol{x}^\dagger \boldsymbol{y}$ と定義する。$n$ 次正方行列 $H$ はエルミート行列（$H^\dagger = H$）であるとする。以下の問いに答えよ。

(1) 任意の複素ベクトル $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^n$ に対し，等式 $(H\boldsymbol{x}, \boldsymbol{y}) = (\boldsymbol{x}, H\boldsymbol{y})$ が成り立つことを示せ。

(2) $H\boldsymbol{x} = \lambda \boldsymbol{x}$（$\boldsymbol{x} \neq \boldsymbol{0}$）を満たす固有値 $\lambda$ は必ず実数であることを示せ。

(3) 相異なる固有値 $\lambda_1, \lambda_2$（$\lambda_1 \neq \lambda_2$）に属する固有ベクトルをそれぞれ $\boldsymbol{x}_1, \boldsymbol{x}_2$ とするとき，これらが直交すること，すなわち $(\boldsymbol{x}_1, \boldsymbol{x}_2) = 0$ を示せ。

---

## 解答・解説

### (1)
エルミート共役の定義および随伴行列の計算法則を適用します。

左辺の内積を行列の積の形で記述すると，
$$
\begin{aligned}
(H\boldsymbol{x}, \boldsymbol{y}) &= (H\boldsymbol{x})^\dagger \boldsymbol{y} \\
&= \boldsymbol{x}^\dagger H^\dagger \boldsymbol{y}
\end{aligned}
$$
となります。

ここで $H^\dagger = H$ を代入すると，
$$
\begin{aligned}
\boldsymbol{x}^\dagger H^\dagger \boldsymbol{y} &= \boldsymbol{x}^\dagger (H\boldsymbol{y}) \\
&= (\boldsymbol{x}, H\boldsymbol{y})
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{(H\boldsymbol{x}, \boldsymbol{y}) = (\boldsymbol{x}, H\boldsymbol{y})}
$$
となります。

### (2)
(1)の内積の等式に $\boldsymbol{y} = \boldsymbol{x}$ を代入します。

左辺を計算すると，
$$
\begin{aligned}
(H\boldsymbol{x}, \boldsymbol{x}) &= (\lambda \boldsymbol{x}, \boldsymbol{x}) \\
&= (\lambda \boldsymbol{x})^\dagger \boldsymbol{x} \\
&= \lambda^* \boldsymbol{x}^\dagger \boldsymbol{x} = \lambda^* \|\boldsymbol{x}\|^2
\end{aligned}
$$
となります。右辺を計算すると，
$$
\begin{aligned}
(\boldsymbol{x}, H\boldsymbol{x}) &= (\boldsymbol{x}, \lambda \boldsymbol{x}) \\
&= \boldsymbol{x}^\dagger (\lambda \boldsymbol{x}) \\
&= \lambda \boldsymbol{x}^\dagger \boldsymbol{x} = \lambda \|\boldsymbol{x}\|^2
\end{aligned}
$$
となります。

(1)より両者は等しいため，
$$
\begin{aligned}
(\lambda^* - \lambda) \|\boldsymbol{x}\|^2 &= 0
\end{aligned}
$$
となります。

$\boldsymbol{x} \neq \boldsymbol{0}$ より $\|\boldsymbol{x}\|^2 > 0$ であるため，
$$
\finalanswer{\lambda^* = \lambda}
$$
となり，固有値 $\lambda$ は実数となります。

### (3)
異なる固有値に対応する固有ベクトルに対して (1)の等式を評価します。

$(H\boldsymbol{x}_1, \boldsymbol{x}_2)$ を計算すると，
$$
\begin{aligned}
(H\boldsymbol{x}_1, \boldsymbol{x}_2) &= (\lambda_1 \boldsymbol{x}_1, \boldsymbol{x}_2) \\
&= \lambda_1^* (\boldsymbol{x}_1, \boldsymbol{x}_2) \\
&= \lambda_1 (\boldsymbol{x}_1, \boldsymbol{x}_2)
\end{aligned}
$$
となります。ここで $\lambda_1$ が実数であることを用いました。

一方，$(\boldsymbol{x}_1, H\boldsymbol{x}_2)$ を計算すると，
$$
\begin{aligned}
(\boldsymbol{x}_1, H\boldsymbol{x}_2) &= (\boldsymbol{x}_1, \lambda_2 \boldsymbol{x}_2) \\
&= \lambda_2 (\boldsymbol{x}_1, \boldsymbol{x}_2)
\end{aligned}
$$
となります。

両辺を減算すると，
$$
\begin{aligned}
(\lambda_1 - \lambda_2) (\boldsymbol{x}_1, \boldsymbol{x}_2) &= 0
\end{aligned}
$$
となります。

$\lambda_1 \neq \lambda_2$ であるため，
$$
\finalanswer{(\boldsymbol{x}_1, \boldsymbol{x}_2) = 0}
$$
となり，相異なる固有値に属する固有ベクトルが直交することが示されます。
===== FILE: 07linear_algebra/05/05_020.md =====
---
tags:
  - 標準
---

# ユニタリー対角化

## 問題
2次のエルミート行列
$$
H = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
$$
を考える。以下の問いに答えよ。

(1) $H$ の固有値 $\lambda_1, \lambda_2$（$\lambda_1 < \lambda_2$）を求めよ。

(2) 各固有値に対応する規格化された固有ベクトル $\boldsymbol{u}_1, \boldsymbol{u}_2$ を求めよ。

(3) これらの固有ベクトルを列とするユニタリー行列 $U = (\boldsymbol{u}_1 \ \boldsymbol{u}_2)$ を構成し，$U^\dagger H U$ を計算して対角化せよ。

---

## 解答・解説

### (1)
特性方程式を解いて固有値を求めます。

特性方程式を立てると，
$$
\begin{aligned}
\det(H - \lambda I) &= \begin{vmatrix} -\lambda & -i \\ i & -\lambda \end{vmatrix} \\
&= (-\lambda)^2 - (-i)(i) \\
&= \lambda^2 - 1 = 0
\end{aligned}
$$
となります。

$\lambda_1 < \lambda_2$ の順に並べると，
$$
\finalanswer{\lambda_1 = -1, \quad \lambda_2 = 1}
$$
となります。

### (2)
各固有値に対して連立方程式を解き，ベクトルのノルムが $1$ になるよう規格化します。

$\lambda_1 = -1$ のとき，方程式 $(H + I)\boldsymbol{u} = \boldsymbol{0}$ より，
$$
\begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix} \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$u_1 - i u_2 = 0$ を得ます。$u_2 = 1$ と選ぶと $u_1 = i$ となり，ノルムは $\sqrt{|i|^2 + 1^2} = \sqrt{2}$ です。規格化すると，
$$
\boldsymbol{u}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} i \\ 1 \end{pmatrix}
$$
となります。

$\lambda_2 = 1$ のとき，方程式 $(H - I)\boldsymbol{u} = \boldsymbol{0}$ より，
$$
\begin{pmatrix} -1 & -i \\ i & -1 \end{pmatrix} \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$-u_1 - i u_2 = 0$ を得ます。$u_2 = 1$ と選ぶと $u_1 = -i$ となり，規格化すると，
$$
\boldsymbol{u}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} -i \\ 1 \end{pmatrix}
$$
となります。

したがって，求める規格化固有ベクトルは，
$$
\finalanswer{\boldsymbol{u}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} i \\ 1 \end{pmatrix}, \quad \boldsymbol{u}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} -i \\ 1 \end{pmatrix}}
$$
となります。

### (3)
固有ベクトルを並べて行列 $U$ を作り，随伴行列を左から掛けます。

ユニタリー行列は，
$$
U = \frac{1}{\sqrt{2}} \begin{pmatrix} i & -i \\ 1 & 1 \end{pmatrix}
$$
となります。このエルミート共役をとると，
$$
U^\dagger = \frac{1}{\sqrt{2}} \begin{pmatrix} -i & 1 \\ i & 1 \end{pmatrix}
$$
となります。

変換後の行列を計算すると，
$$
\begin{aligned}
U^\dagger H U &= \frac{1}{\sqrt{2}} \begin{pmatrix} -i & 1 \\ i & 1 \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} i & -i \\ 1 & 1 \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} i & -1 \\ i & 1 \end{pmatrix} \begin{pmatrix} i & -i \\ 1 & 1 \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} -1 - 1 & 1 - 1 \\ -1 + 1 & 1 + 1 \end{pmatrix} \\
&= \finalanswer{\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}}
\end{aligned}
$$
となります。対角線上に固有値が並びます。
===== FILE: 07linear_algebra/05/05_030.md =====
---
tags:
  - 発展
---

# 正規行列とスペクトル分解

## 問題
$n$ 次エルミート行列 $A$ が固有値 $\lambda_k$（$k=1, 2, \dots, n$）と対応する正規直交固有ベクトル系 $\{\boldsymbol{u}_k\}$ をもつとする。各固有空間への射影行列を $P_k = \boldsymbol{u}_k \boldsymbol{u}_k^\dagger$ と定義する。以下の問いに答えよ。

(1) 射影行列 $P_k$ がエルミート性 $P_k^\dagger = P_k$，直交性 $P_j P_k = \delta_{jk} P_k$（$\delta_{jk}$ はクロネッカーのデルタ），および完全性関係 $\sum_{k=1}^n P_k = I$ を満たすことを示せ。

(2) 行列 $A$ が射影行列の線形結合として $A = \sum_{k=1}^n \lambda_k P_k$（スペクトル分解）と表せることを示せ。

(3) エルミート行列
$$
A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}
$$
に対する各射影行列 $P_1, P_2$ を具体的に計算し，$A = \lambda_1 P_1 + \lambda_2 P_2$ を確かめよ。

---

## 解答・解説

### (1)
外積の定義にしたがって行列演算を行います。

まずエルミート性を確認すると，
$$
\begin{aligned}
P_k^\dagger &= (\boldsymbol{u}_k \boldsymbol{u}_k^\dagger)^\dagger \\
&= (\boldsymbol{u}_k^\dagger)^\dagger \boldsymbol{u}_k^\dagger \\
&= \boldsymbol{u}_k \boldsymbol{u}_k^\dagger = P_k
\end{aligned}
$$
となります。

次に直交性を調べます。基底の正規直交性 $\boldsymbol{u}_j^\dagger \boldsymbol{u}_k = \delta_{jk}$ を用いると，
$$
\begin{aligned}
P_j P_k &= (\boldsymbol{u}_j \boldsymbol{u}_j^\dagger) (\boldsymbol{u}_k \boldsymbol{u}_k^\dagger) \\
&= \boldsymbol{u}_j (\boldsymbol{u}_j^\dagger \boldsymbol{u}_k) \boldsymbol{u}_k^\dagger \\
&= \delta_{jk} \boldsymbol{u}_j \boldsymbol{u}_k^\dagger = \delta_{jk} P_k
\end{aligned}
$$
となります。

固有ベクトルを列ベクトルとして並べた行列 $U = (\boldsymbol{u}_1 \ \dots \ \boldsymbol{u}_n)$ はユニタリー行列であり，$U U^\dagger = I$ を満たします。ブロック行列の積を計算すると，
$$
\begin{aligned}
U U^\dagger &= \sum_{k=1}^n \boldsymbol{u}_k \boldsymbol{u}_k^\dagger = \sum_{k=1}^n P_k = I
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{P_k^\dagger = P_k, \quad P_j P_k = \delta_{jk} P_k, \quad \sum_{k=1}^n P_k = I}
$$
となります。

### (2)
ユニタリー対角化の関係式から分解を導出します。

対角行列を $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ とすると，$U^\dagger A U = \Lambda$ より，
$$
\begin{aligned}
A &= U \Lambda U^\dagger
\end{aligned}
$$
となります。

列ベクトルと行ベクトルの積の和として書き直すと，
$$
\begin{aligned}
A &= (\boldsymbol{u}_1 \ \dots \ \boldsymbol{u}_n) \begin{pmatrix} \lambda_1 & & O \\ & \ddots & \\ O & & \lambda_n \end{pmatrix} \begin{pmatrix} \boldsymbol{u}_1^\dagger \\ \vdots \\ \boldsymbol{u}_n^\dagger \end{pmatrix} \\
&= (\lambda_1 \boldsymbol{u}_1 \ \dots \ \lambda_n \boldsymbol{u}_n) \begin{pmatrix} \boldsymbol{u}_1^\dagger \\ \vdots \\ \boldsymbol{u}_n^\dagger \end{pmatrix} \\
&= \finalanswer{\sum_{k=1}^n \lambda_k \boldsymbol{u}_k \boldsymbol{u}_k^\dagger = \sum_{k=1}^n \lambda_k P_k}
\end{aligned}
$$
となります。

### (3)
具体的に固有値と固有ベクトルを求め，外積を計算します。

特性方程式 $\det(A - \lambda I) = (1 - \lambda)^2 - 4 = 0$ より，固有値は $\lambda_1 = 3, \lambda_2 = -1$ です。

$\lambda_1 = 3$ に属する規格化固有ベクトルは $\boldsymbol{u}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$，$\lambda_2 = -1$ に属する規格化固有ベクトルは $\boldsymbol{u}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ です。

射影行列を求めると，
$$
\begin{aligned}
P_1 &= \frac{1}{2} \begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \end{pmatrix} = \finalanswer{\frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}} \\
P_2 &= \frac{1}{2} \begin{pmatrix} 1 \\ -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \end{pmatrix} = \finalanswer{\frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}}
\end{aligned}
$$
となります。

スペクトル分解の和を計算すると，
$$
\begin{aligned}
3 P_1 - 1 P_2 &= \frac{3}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} - \frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} \\
&= \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} = A
\end{aligned}
$$
となり，分解が成立することが確かめられます。
===== FILE: 07linear_algebra/05/05_040.md =====
---
tags:
  - 標準
---

# 可換な行列の同時対角化

## 問題
$n$ 次エルミート行列 $A, B$ が可換である，すなわち交換子 $[A, B] = AB - BA = O$ を満たすとする。以下の問いに答えよ。

(1) $A$ の固有値 $\lambda$ に属する固有空間を $V_\lambda = \{\boldsymbol{x} \in \mathbb{C}^n \mid A\boldsymbol{x} = \lambda\boldsymbol{x}\}$ とする。$\boldsymbol{x} \in V_\lambda$ ならば $B\boldsymbol{x} \in V_\lambda$ が成り立つことを示せ。

(2) $A$ の固有値がすべて相異なるとき，$A$ の固有ベクトルはすべて $B$ の固有ベクトルでもあることを示せ。

(3) 行列
$$
A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$
に対して交換子 $[A, B]$ を計算し，両者が同時対角化可能であるかどうかを判定せよ。

---

## 解答・解説

### (1)
可換性を利用して行列を作用させる順序を入れ替えます。

$\boldsymbol{x} \in V_\lambda$ に対してベクトル $B\boldsymbol{x}$ に $A$ を左から作用させると，
$$
\begin{aligned}
A(B\boldsymbol{x}) &= (AB)\boldsymbol{x} \\
&= (BA)\boldsymbol{x} \\
&= B(A\boldsymbol{x})
\end{aligned}
$$
となります。

ここで $A\boldsymbol{x} = \lambda \boldsymbol{x}$ を代入すると，
$$
\begin{aligned}
B(A\boldsymbol{x}) &= B(\lambda \boldsymbol{x}) \\
&= \lambda (B\boldsymbol{x})
\end{aligned}
$$
となります。

したがって，$A(B\boldsymbol{x}) = \lambda (B\boldsymbol{x})$ が成り立ち，
$$
\finalanswer{B\boldsymbol{x} \in V_\lambda}
$$
となります。

### (2)
固有空間の次元に着目して比例関係を導きます。

$A$ の固有値がすべて相異なる場合，各固有空間 $V_\lambda$ の次元はすべて $1$ です。

したがって，$V_\lambda$ 内の非ゼロベクトル $\boldsymbol{x}$ はその空間の基底をなし，(1)より $B\boldsymbol{x} \in V_\lambda$ であることから，$B\boldsymbol{x}$ は $\boldsymbol{x}$ のスカラー倍として一意に表されます。

ある複素数 $\mu$ が存在して，
$$
\finalanswer{B\boldsymbol{x} = \mu \boldsymbol{x}}
$$
が成立します。これは $\boldsymbol{x}$ が行列 $B$ の固有ベクトルであることを意味します。共通の基底によって両者は同時に直交対角化されます。

### (3)
積の計算を直接行い，交換関係を調べます。

2つの積をそれぞれ計算すると，
$$
\begin{aligned}
AB &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \\
BA &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
\end{aligned}
$$
となります。

交換子を計算すると，
$$
\begin{aligned}
[A, B] &= AB - BA \\
&= \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} - \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \\
&= \finalanswer{\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}}
\end{aligned}
$$
となります。

$[A, B] \neq O$ であるため，
$$
\finalanswer{\text{同時対角化可能ではない}}
$$
となります。物理的には非可換な物理量は互いに同時に確定値をとることができない不確定性に対応します。
===== FILE: 07linear_algebra/05/05_050.md =====
---
tags:
  - 基本
---

# パウリ行列の性質

## 問題
パウリ行列
$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$
および2次単位行列 $I$ を考える。以下の問いに答えよ。

(1) $\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = I$ および $\sigma_x \sigma_y = i \sigma_z$ を示せ。また反交換関係 $\{\sigma_x, \sigma_y\} = \sigma_x \sigma_y + \sigma_y \sigma_x$ を求めよ。

(2) $k = x, y, z$ に対し $\operatorname{Tr}(\sigma_k) = 0$ であること，および相異なる $j, k$ に対して $\operatorname{Tr}(\sigma_j \sigma_k) = 0$ となることを示せ。

(3) 任意の実数 $a, b, c, d$ を用いた任意の2次エルミート行列
$$
H = \begin{pmatrix} a & b - ic \\ b + ic & d \end{pmatrix}
$$
を，$I, \sigma_x, \sigma_y, \sigma_z$ の実数係数の線形結合として表せ。

---

## 解答・解説

### (1)
定義に従って行列の積を直接計算します。

二乗の計算を行うと，
$$
\begin{aligned}
\sigma_x^2 &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \\
\sigma_y^2 &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \\
\sigma_z^2 &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
\end{aligned}
$$
となります。

積 $\sigma_x \sigma_y$ を計算すると，
$$
\begin{aligned}
\sigma_x \sigma_y &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \\
&= \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = i \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \finalanswer{i \sigma_z}
\end{aligned}
$$
となります。

逆順の積は $\sigma_y \sigma_x = -i \sigma_z$ となるため，反交換関係は，
$$
\begin{aligned}
\{\sigma_x, \sigma_y\} &= \sigma_x \sigma_y + \sigma_y \sigma_x \\
&= i\sigma_z - i\sigma_z = \finalanswer{O}
\end{aligned}
$$
となります。

### (2)
対角和を直接計算し，積については生成されるパウリ行列のトレースに帰着させます。

各パウリ行列のトレースを調べると，
$$
\begin{aligned}
\operatorname{Tr}(\sigma_x) &= 0 + 0 = 0 \\
\operatorname{Tr}(\sigma_y) &= 0 + 0 = 0 \\
\operatorname{Tr}(\sigma_z) &= 1 + (-1) = 0
\end{aligned}
$$
となります。

相異なる添字 $j, k$ については，積は第3のパウリ行列の定数倍（$\sigma_j \sigma_k = i \epsilon_{jkl} \sigma_l$）となります。

トレースの線形性を用いると，
$$
\begin{aligned}
\operatorname{Tr}(\sigma_j \sigma_k) &= i \epsilon_{jkl} \operatorname{Tr}(\sigma_l) = 0
\end{aligned}
$$
となり，
$$
\finalanswer{\operatorname{Tr}(\sigma_k) = 0, \quad \operatorname{Tr}(\sigma_j \sigma_k) = 0 \quad (j \neq k)}
$$
となります。

### (3)
基底行列による展開係数を対角成分と非対角成分から特定します。

行列 $H$ を対角成分と非対角成分に分離して変形すると，
$$
\begin{aligned}
H &= \begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix} + \begin{pmatrix} 0 & b - ic \\ b + ic & 0 \end{pmatrix} \\
&= \left( \frac{a+d}{2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \frac{a-d}{2} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \right) + b \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + c \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\end{aligned}
$$
となります。

したがって，求める線形結合の表現は，
$$
\finalanswer{H = \frac{a+d}{2} I + b \sigma_x + c \sigma_y + \frac{a-d}{2} \sigma_z}
$$
となります。展開係数はすべて実数であり，パウリ行列と単位行列が2次エルミート行列の空間の実基底をなすことを示しています。
===== FILE: 07linear_algebra/05/05_060.md =====
---
tags:
  - 標準
---

# 行列のトレースと行列式の不変性

## 問題
$n$ 次正方行列 $A, B$ および正則行列 $P$ に対し，相似変換 $A' = P^{-1} A P$ を考える。以下の問いに答えよ。

(1) 成分計算を用いて $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$ が成り立つことを示せ。

(2) (1)の結果を用いてトレースが相似変換に対して不変であること，すなわち $\operatorname{Tr}(P^{-1} A P) = \operatorname{Tr}(A)$ を示せ。また，行列式の積の性質を用いて $\det(P^{-1} A P) = \det A$ を示せ。

(3) 行列 $A$ が対角化可能であるとき，$A$ の相異なる固有値および重複を含めたすべての固有値を $\lambda_1, \lambda_2, \dots, \lambda_n$ とする。$\operatorname{Tr}(A)$ および $\det A$ をこれらの固有値を用いて表せ。

---

## 解答・解説

### (1)
行列の積の定義を行列成分の和の順序交換を用いて変形します。

行列の積 $AB$ の $(i, i)$ 成分は $\sum_{j=1}^n A_{ij} B_{ji}$ です。トレースの定義により対角成分の和をとると，
$$
\begin{aligned}
\operatorname{Tr}(AB) &= \sum_{i=1}^n (AB)_{ii} \\
&= \sum_{i=1}^n \sum_{j=1}^n A_{ij} B_{ji}
\end{aligned}
$$
となります。

各成分は単なる数であるため積の順序を入れ替えることができ，和の順序を交換すると，
$$
\begin{aligned}
\sum_{i=1}^n \sum_{j=1}^n A_{ij} B_{ji} &= \sum_{j=1}^n \sum_{i=1}^n B_{ji} A_{ij} \\
&= \sum_{j=1}^n (BA)_{jj} \\
&= \operatorname{Tr}(BA)
\end{aligned}
$$
となります。

したがって，
$$
\finalanswer{\operatorname{Tr}(AB) = \operatorname{Tr}(BA)}
$$
となります。

### (2)
巡回対称性とスカラーの積の可換性を用います。

$P^{-1}$ と $(AP)$ をひとかたまりとみなして (1)の巡回公式を適用すると，
$$
\begin{aligned}
\operatorname{Tr}(P^{-1} A P) &= \operatorname{Tr}\left( P^{-1} (AP) \right) \\
&= \operatorname{Tr}\left( (AP) P^{-1} \right) \\
&= \operatorname{Tr}\left( A (P P^{-1}) \right) \\
&= \operatorname{Tr}(A I) = \finalanswer{\operatorname{Tr}(A)}
\end{aligned}
$$
となります。

行列式については積の分解公式を適用すると，
$$
\begin{aligned}
\det(P^{-1} A P) &= \det(P^{-1}) \det A \det P \\
&= \frac{1}{\det P} \det A \det P \\
&= \finalanswer{\det A}
\end{aligned}
$$
となります。

### (3)
相似変換によって固有値を対角成分にもつ行列へと帰着させます。

仮定より $A$ は正則行列 $P$ によって対角化され，
$$
P^{-1} A P = \Lambda = \begin{pmatrix} \lambda_1 & & O \\ & \ddots & \\ O & & \lambda_n \end{pmatrix}
$$
と表されます。

(2)の不変性を用いると，
$$
\begin{aligned}
\operatorname{Tr}(A) &= \operatorname{Tr}(\Lambda) \\
&= \finalanswer{\sum_{k=1}^n \lambda_k}
\end{aligned}
$$
となります。

同様に行列式については，
$$
\begin{aligned}
\det A &= \det \Lambda \\
&= \finalanswer{\prod_{k=1}^n \lambda_k}
\end{aligned}
$$
となります。これらは基底の選び方によらない固有の幾何学的不変量です。
===== FILE: 07linear_algebra/06/06_010.md =====
---
tags:
  - 標準
---

# 連成振動の基準モード

## 問題
滑らかな水平面上にある質量 $m$ の2つの質点1，2が，ばね定数 $k$ の等しい3本の軽いばねによって直列につながれ，両端は静止した壁に固定されている（図）。質点1，2のつりあいの位置からの変位をそれぞれ $x_1, x_2$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 水平面上に直列に並んだ2つの台車（質点1, 2）。左の壁と質点1の間，質点1と質点2の間，質点2と右の壁の間にそれぞれ同じばね（ばね定数 k）が接続されている。各質点には質量 m と変位 x_1, x_2 が明記されている。 -->

(1) 系の運動方程式を行列の形式
$$
M \ddot{\boldsymbol{x}} + K \boldsymbol{x} = \boldsymbol{0}, \quad \boldsymbol{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
$$
で表すとき，質量行列 $M$ と剛性行列 $K$ を求めよ。

(2) 単振動解 $\boldsymbol{x}(t) = \boldsymbol{A} \cos(\omega t + \phi)$ を仮定して得られる一般化固有値問題 $(K - \omega^2 M)\boldsymbol{A} = \boldsymbol{0}$ から，固有角振動数 $\omega_1, \omega_2$（$\omega_1 < \omega_2$）を求めよ。

(3) 各固有角振動数に対応する基準モード（振幅比を表すベクトル）を求めよ。

---

## 解答・解説

### (1)
各質点に作用する弾性力をフックの法則から求めて運動方程式を立てます。

質点1および質点2に働く力は，ばねの伸び縮みを考慮すると，
$$
\begin{aligned}
m \ddot{x}_1 &= -k x_1 + k(x_2 - x_1) = -2k x_1 + k x_2 \\
m \ddot{x}_2 &= -k(x_2 - x_1) - k x_2 = k x_1 - 2k x_2
\end{aligned}
$$
となります。

移項してベクトル表示に整理すると，
$$
\begin{pmatrix} m & 0 \\ 0 & m \end{pmatrix} \begin{pmatrix} \ddot{x}_1 \\ \ddot{x}_2 \end{pmatrix} + \begin{pmatrix} 2k & -k \\ -k & 2k \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となります。

したがって，質量行列と剛性行列は，
$$
\finalanswer{M = \begin{pmatrix} m & 0 \\ 0 & m \end{pmatrix}, \quad K = \begin{pmatrix} 2k & -k \\ -k & 2k \end{pmatrix}}
$$
となります。

### (2)
解の仮定を運動方程式に代入して非自明な解をもつ条件を行列式から導きます。

$\ddot{\boldsymbol{x}} = -\omega^2 \boldsymbol{x}$ を代入すると，$(K - \omega^2 M)\boldsymbol{A} = \boldsymbol{0}$ を得ます。$\boldsymbol{A} \neq \boldsymbol{0}$ であるための条件は，
$$
\begin{aligned}
\det(K - \omega^2 M) &= \begin{vmatrix} 2k - m\omega^2 & -k \\ -k & 2k - m\omega^2 \end{vmatrix} \\
&= (2k - m\omega^2)^2 - k^2 = 0
\end{aligned}
$$
となります。

因数分解すると，
$$
\begin{aligned}
(2k - m\omega^2 - k)(2k - m\omega^2 + k) &= (k - m\omega^2)(3k - m\omega^2) = 0
\end{aligned}
$$
となります。

固有角振動数は正であるため，小さい順に，
$$
\finalanswer{\omega_1 = \sqrt{\frac{k}{m}}, \quad \omega_2 = \sqrt{\frac{3k}{m}}}
$$
となります。

### (3)
各固有角振動数を方程式 $(K - \omega^2 M)\boldsymbol{A} = \boldsymbol{0}$ に代入します。

$\omega_1^2 = k/m$ のとき，
$$
\begin{pmatrix} k & -k \\ -k & k \end{pmatrix} \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$A_1 - A_2 = 0$ を得ます。

$\omega_2^2 = 3k/m$ のとき，
$$
\begin{pmatrix} -k & -k \\ -k & -k \end{pmatrix} \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$A_1 + A_2 = 0$ を得ます。

したがって，各モードの振幅比は，
$$
\finalanswer{\omega_1 : \boldsymbol{A}_1 \propto \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \omega_2 : \boldsymbol{A}_2 \propto \begin{pmatrix} 1 \\ -1 \end{pmatrix}}
$$
となります。$\omega_1$ は2質点が同じ向きに同位相で揺れるモード，$\omega_2$ は互いに逆向きに逆位相で揺れるモードを表します。
===== FILE: 07linear_algebra/06/06_020.md =====
---
tags:
  - 標準
---

# 慣性テンソルの主軸

## 問題
$xy$ 平面上において，質量 $m$ の等しい3つの質点がそれぞれ点 $(a, 0, 0)$，点 $(0, a, 0)$，点 $(a, a, 0)$ に静止して配置されている（図）。原点 $O$ まわりの剛体の慣性テンソルを $I$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 直交座標系 xyz において，xy 平面上に置かれた3つの質点。座標 (a,0,0), (0,a,0), (a,a,0) に同じ黒丸と質量 m が示されている。 -->

(1) 慣性テンソルの定義式
$$
I_{xx} = \sum_k m_k (y_k^2 + z_k^2), \quad I_{xy} = -\sum_k m_k x_k y_k
$$
および他の成分の定義にしたがって，行列 $I$ を求めよ。

(2) 行列 $I$ の固有値をすべて求め，主慣性モーメントを求めよ。

(3) 各主慣性モーメントに対応する主軸（規格化された固有ベクトル）を求めよ。

---

## 解答・解説

### (1)
3つの質点について各テンソル成分の和を個別に計算します。

各質点の座標は，質点1が $(a, 0, 0)$，質点2が $(0, a, 0)$，質点3が $(a, a, 0)$ であり，すべての質点で $z_k = 0$ です。

対角成分を計算すると，
$$
\begin{aligned}
I_{xx} &= m(0^2 + a^2 + a^2) = 2ma^2 \\
I_{yy} &= m(a^2 + 0^2 + a^2) = 2ma^2 \\
I_{zz} &= I_{xx} + I_{yy} = m((a^2+0) + (0+a^2) + (a^2+a^2)) = 4ma^2
\end{aligned}
$$
となります。

非対角成分を計算すると，
$$
\begin{aligned}
I_{xy} = I_{yx} &= -m(a \cdot 0 + 0 \cdot a + a \cdot a) = -ma^2 \\
I_{xz} = I_{zx} &= 0 \\
I_{yz} = I_{zy} &= 0
\end{aligned}
$$
となります。

したがって，求める慣性テンソル行列は，
$$
\finalanswer{I = ma^2 \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & 0 \\ 0 & 0 & 4 \end{pmatrix}}
$$
となります。

### (2)
行列がブロック対角化されていることに注目して固有方程式を解きます。

特性方程式を計算すると，
$$
\begin{aligned}
\det(I - \lambda I_3) &= (4ma^2 - \lambda) \begin{vmatrix} 2ma^2 - \lambda & -ma^2 \\ -ma^2 & 2ma^2 - \lambda \end{vmatrix} \\
&= (4ma^2 - \lambda) \left( (2ma^2 - \lambda)^2 - (ma^2)^2 \right) = 0
\end{aligned}
$$
となります。

二乗の差を展開すると，
$$
\begin{aligned}
(2ma^2 - \lambda - ma^2)(2ma^2 - \lambda + ma^2) &= (ma^2 - \lambda)(3ma^2 - \lambda)
\end{aligned}
$$
となります。

したがって，主慣性モーメントは，
$$
\finalanswer{I_1 = ma^2, \quad I_2 = 3ma^2, \quad I_3 = 4ma^2}
$$
となります。

### (3)
各主慣性モーメントの方程式を解いて単位固有ベクトルを求めます。

$I_1 = ma^2$ のとき，上側 $2 \times 2$ ブロックの方程式は，
$$
ma^2 \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} u_x \\ u_y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$u_x - u_y = 0$ かつ $u_z = 0$ を得ます。規格化すると，
$$
\boldsymbol{u}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}
$$
となります。

$I_2 = 3ma^2$ のとき，方程式は，
$$
ma^2 \begin{pmatrix} -1 & -1 \\ -1 & -1 \end{pmatrix} \begin{pmatrix} u_x \\ u_y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$u_x + u_y = 0$ かつ $u_z = 0$ を得ます。規格化すると，
$$
\boldsymbol{u}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}
$$
となります。

$I_3 = 4ma^2$ のときは直ちに $z$ 軸方向と定まります。

したがって，主軸方向の単位ベクトルは，
$$
\finalanswer{\boldsymbol{u}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \boldsymbol{u}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}, \quad \boldsymbol{u}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}}
$$
となります。
===== FILE: 07linear_algebra/06/06_030.md =====
---
tags:
  - 標準
---

# 二準位系のハミルトニアン

## 問題
量子力学における二準位系のハミルトニアンを行列
$$
H = \begin{pmatrix} \epsilon & \Delta \\ \Delta & -\epsilon \end{pmatrix}
$$
とする。ここで $\epsilon > 0, \Delta > 0$ は実数定数である。以下の問いに答えよ。

(1) ハミルトニアン $H$ の固有エネルギー $E_{\pm}$（$E_- < E_+$）を求めよ。

(2) 関係式
$$
\cos 2\theta = \frac{\epsilon}{\sqrt{\epsilon^2 + \Delta^2}}, \quad \sin 2\theta = \frac{\Delta}{\sqrt{\epsilon^2 + \Delta^2}} \quad (0 < \theta < \pi/4)
$$
によって混合角 $\theta$ を導入するとき，$E_+$ に対応する規格化された固有ベクトルを $\theta$ を用いて表せ。

(3) 摂動が弱い極限 $\Delta \ll \epsilon$ において，固有エネルギー $E_+$ を $\Delta/\epsilon$ の2次の微小量までテイラー展開せよ。

---

## 解答・解説

### (1)
特性方程式を解いてエネルギー固有値を求めます。

特性方程式を計算すると，
$$
\begin{aligned}
\det(H - E I) &= \begin{vmatrix} \epsilon - E & \Delta \\ \Delta & -\epsilon - E \end{vmatrix} \\
&= -(\epsilon - E)(\epsilon + E) - \Delta^2 \\
&= E^2 - \epsilon^2 - \Delta^2 = 0
\end{aligned}
$$
となります。

したがって，大小関係 $E_- < E_+$ を考慮すると，
$$
\finalanswer{E_+ = \sqrt{\epsilon^2 + \Delta^2}, \quad E_- = -\sqrt{\epsilon^2 + \Delta^2}}
$$
となります。非対角相互作用 $\Delta$ の存在により準位反発が生じます。

### (2)
$E_0 = \sqrt{\epsilon^2 + \Delta^2}$ と定義し，固有ベクトルの方程式を解きます。

$(H - E_0 I)\boldsymbol{u} = \boldsymbol{0}$ より，第1成分の方程式は，
$$
\begin{aligned}
(\epsilon - E_0) u_1 + \Delta u_2 &= 0
\end{aligned}
$$
となります。両辺を $E_0$ で割り混合角を代入すると，
$$
\begin{aligned}
(\cos 2\theta - 1) u_1 + \sin 2\theta u_2 &= 0
\end{aligned}
$$
となります。

倍角の公式 $\cos 2\theta - 1 = -2\sin^2\theta$ および $\sin 2\theta = 2\sin\theta\cos\theta$ を代入すると，
$$
\begin{aligned}
-2\sin^2\theta u_1 + 2\sin\theta\cos\theta u_2 &= 0 \\
-\sin\theta u_1 + \cos\theta u_2 &= 0
\end{aligned}
$$
となります。

規格化条件 $u_1^2 + u_2^2 = 1$ を満たす解をとると，
$$
\finalanswer{\boldsymbol{u}_+ = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}}
$$
となります。

### (3)
二項展開を用いて平方根の近似計算を行います。

固有エネルギーの式を整理して括り出すと，
$$
\begin{aligned}
E_+ &= \epsilon \sqrt{1 + \left(\frac{\Delta}{\epsilon}\right)^2}
\end{aligned}
$$
となります。

微小量 $x = (\Delta/\epsilon)^2 \ll 1$ に対する近似式 $(1+x)^{1/2} = 1 + \frac{1}{2}x - \frac{1}{8}x^2 + \dots$ を適用すると，
$$
\begin{aligned}
E_+ &= \epsilon \left( 1 + \frac{1}{2}\left(\frac{\Delta}{\epsilon}\right)^2 + O\left(\left(\frac{\Delta}{\epsilon}\right)^4\right) \right) \\
&= \finalanswer{\epsilon + \frac{\Delta^2}{2\epsilon}}
\end{aligned}
$$
となります。2次の摂動論によるエネルギーシフトの結果と一致します。
===== FILE: 07linear_algebra/06/06_040.md =====
---
tags:
  - 発展
---

# レイリー商と変分原理

## 問題
$n$ 次実対称行列 $A$ の固有値を小さい順に $\lambda_1 \le \lambda_2 \le \dots \le \lambda_n$ とし，対応する正規直交固有ベクトル系を $\{\boldsymbol{u}_1, \boldsymbol{u}_2, \dots, \boldsymbol{u}_n\}$ とする。ゼロでない任意のベクトル $\boldsymbol{x} \in \mathbb{R}^n$ に対して定義されるレイリー商
$$
R(\boldsymbol{x}) = \frac{\boldsymbol{x}^{\mathsf{T}} A \boldsymbol{x}}{\boldsymbol{x}^{\mathsf{T}}\boldsymbol{x}}
$$
を考える。以下の問いに答えよ。

(1) 任意の非ゼロベクトル $\boldsymbol{x}$ を正規直交固有ベクトルで展開することにより，不等式 $\lambda_1 \le R(\boldsymbol{x}) \le \lambda_n$ を示せ。

(2) $R(\boldsymbol{x}) = \lambda_1$ が成り立つための必要十分条件は，$\boldsymbol{x}$ が $\lambda_1$ に対する固有ベクトルであることを示せ。

(3) 行列
$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}
$$
に対し，試行ベクトル $\boldsymbol{x}_t = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ を用いてレイリー商 $R(\boldsymbol{x}_t)$ を計算し，実際の最小固有値と比較せよ。

---

## 解答・解説

### (1)
正規直交基底による展開を分母と分子に代入します。

ベクトルを $\boldsymbol{x} = \sum_{k=1}^n c_k \boldsymbol{u}_k$ と展開します。正規直交性 $\boldsymbol{u}_j^{\mathsf{T}}\boldsymbol{u}_k = \delta_{jk}$ より，分母は，
$$
\begin{aligned}
\boldsymbol{x}^{\mathsf{T}}\boldsymbol{x} &= \sum_{k=1}^n c_k^2
\end{aligned}
$$
となります。分子は $A\boldsymbol{u}_k = \lambda_k \boldsymbol{u}_k$ を用いると，
$$
\begin{aligned}
\boldsymbol{x}^{\mathsf{T}} A \boldsymbol{x} &= \sum_{k=1}^n \lambda_k c_k^2
\end{aligned}
$$
となります。

$\lambda_1 \le \lambda_k \le \lambda_n$ であるため，各項について，
$$
\begin{aligned}
\lambda_1 \sum_{k=1}^n c_k^2 \le \sum_{k=1}^n \lambda_k c_k^2 \le \lambda_n \sum_{k=1}^n c_k^2
\end{aligned}
$$
が成り立ちます。

両辺を正の実数 $\sum_{k=1}^n c_k^2 > 0$ で割ると，
$$
\finalanswer{\lambda_1 \le R(\boldsymbol{x}) \le \lambda_n}
$$
となります。

### (2)
差をとって非負項の和の性質を利用します。

$R(\boldsymbol{x}) = \lambda_1$ は $\boldsymbol{x}^{\mathsf{T}} A \boldsymbol{x} - \lambda_1 \boldsymbol{x}^{\mathsf{T}}\boldsymbol{x} = 0$ と同値です。

展開式を代入すると，
$$
\begin{aligned}
\sum_{k=1}^n (\lambda_k - \lambda_1) c_k^2 &= 0
\end{aligned}
$$
となります。

すべての $k$ において $\lambda_k - \lambda_1 \ge 0$ かつ $c_k^2 \ge 0$ であるため，和が $0$ になるためには各項がすべて $0$ でなければなりません。

したがって，$\lambda_k > \lambda_1$ であるすべての添字 $k$ に対して $c_k = 0$ となる必要があります。

これにより $\boldsymbol{x}$ は $\lambda_k = \lambda_1$ を満たす固有ベクトルの線形結合のみで表されるため，
$$
\finalanswer{A\boldsymbol{x} = \lambda_1 \boldsymbol{x}}
$$
が導かれます。十分条件は定義式に固有方程式を直接代入すれば明らかです。

### (3)
試行ベクトルを用いて直接行列積を計算します。

レイリー商を計算すると，
$$
\begin{aligned}
R(\boldsymbol{x}_t) &= \frac{\begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix}}{\begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix}} \\
&= \frac{\begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix}}{1} = \finalanswer{2}
\end{aligned}
$$
となります。

行列 $A$ の最小固有値は $\det(A - \lambda I) = (\lambda - 1)(\lambda - 3) = 0$ より $\lambda_1 = 1$ です。

したがって，
$$
\finalanswer{\lambda_1 = 1 \le R(\boldsymbol{x}_t) = 2}
$$
となり，試行ベクトルのレイリー商が最小固有値の上界を与える変分原理が確かめられます。
===== FILE: 07linear_algebra/06/06_050.md =====
---
tags:
  - 標準
---

# マルコフ行列と定常分布

## 問題
実変数 $p, q$（$0 < p < 1, 0 < q < 1$）に対して定義されるマルコフ遷移確率行列
$$
T = \begin{pmatrix} 1-p & q \\ p & 1-q \end{pmatrix}
$$
を考える。以下の問いに答えよ。

(1) 全成分が $1$ の行ベクトル $\boldsymbol{e}^{\mathsf{T}} = (1 \ 1)$ に対し $\boldsymbol{e}^{\mathsf{T}} T = \boldsymbol{e}^{\mathsf{T}}$ が成り立つことを確かめ，$\det(T - I) = 0$ であることから $T$ が固有値 $1$ をもつことを示せ。

(2) トレースを用いて $T$ のもう一つの固有値 $\lambda_2$ を求め，$|\lambda_2| < 1$ が成り立つことを示せ。

(3) 固有値 $1$ に属する定常分布ベクトル $\boldsymbol{\pi} = \begin{pmatrix} \pi_1 \\ \pi_2 \end{pmatrix}$（$T\boldsymbol{\pi} = \boldsymbol{\pi}$ かつ $\pi_1 + \pi_2 = 1$）を $p, q$ を用いて表せ。

---

## 解答・解説

### (1)
行ベクトルの積を計算して各列の確率保存性を確認します。

行ベクトルとの積を計算すると，
$$
\begin{aligned}
\boldsymbol{e}^{\mathsf{T}} T &= \begin{pmatrix} 1 & 1 \end{pmatrix} \begin{pmatrix} 1-p & q \\ p & 1-q \end{pmatrix} \\
&= \begin{pmatrix} (1-p) + p & q + (1-q) \end{pmatrix} \\
&= \begin{pmatrix} 1 & 1 \end{pmatrix} = \boldsymbol{e}^{\mathsf{T}}
\end{aligned}
$$
となります。

両辺から $\boldsymbol{e}^{\mathsf{T}}$ を引くと $\boldsymbol{e}^{\mathsf{T}}(T - I) = \boldsymbol{0}^{\mathsf{T}}$ となります。転置をとると $(T^{\mathsf{T}} - I)\boldsymbol{e} = \boldsymbol{0}$ となり，非ゼロベクトル $\boldsymbol{e}$ が解であるため $\det(T^{\mathsf{T}} - I) = 0$ です。

転置行列の行列式は元の行列式と等しいため，
$$
\finalanswer{\det(T - I) = 0}
$$
となり，$\lambda = 1$ が $T$ の固有値であることが示されます。

### (2)
行列のトレースが固有値の和に等しい性質を用います。

行列 $T$ のトレースを計算すると，
$$
\begin{aligned}
\operatorname{Tr}(T) &= (1 - p) + (1 - q) \\
&= 2 - p - q
\end{aligned}
$$
となります。

一方，固有値の和は $1 + \lambda_2$ であるため，
$$
\begin{aligned}
1 + \lambda_2 &= 2 - p - q
\end{aligned}
$$
となります。

したがって，固有値は，
$$
\finalanswer{\lambda_2 = 1 - p - q}
$$
となります。

条件 $0 < p < 1$ かつ $0 < q < 1$ より $0 < p + q < 2$ です。各辺から $1$ を引いて符号を反転させると $-1 < 1 - (p+q) < 1$ となるため，
$$
\finalanswer{|\lambda_2| < 1}
$$
となります。

### (3)
固有方程式 $(T - I)\boldsymbol{\pi} = \boldsymbol{0}$ を連立させて解きます。

方程式を行列表示すると，
$$
\begin{pmatrix} -p & q \\ p & -q \end{pmatrix} \begin{pmatrix} \pi_1 \\ \pi_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$-p\pi_1 + q\pi_2 = 0$ より $\pi_2 = \frac{p}{q}\pi_1$ を得ます。

規格化条件 $\pi_1 + \pi_2 = 1$ に代入すると，
$$
\begin{aligned}
\pi_1 + \frac{p}{q}\pi_1 &= \frac{p+q}{q}\pi_1 = 1
\end{aligned}
$$
となり，$\pi_1 = \frac{q}{p+q}$ を得ます。

したがって，求める定常分布ベクトルは，
$$
\finalanswer{\boldsymbol{\pi} = \frac{1}{p+q} \begin{pmatrix} q \\ p \end{pmatrix}}
$$
となります。
===== FILE: 07linear_algebra/06/06_060.md =====
---
tags:
  - 発展
---

# 特異値分解

## 問題
$3 \times 2$ 実実行列
$$
A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \\ 0 & 0 \end{pmatrix}
$$
を考える。以下の問いに答えよ。

(1) $2 \times 2$ 対称行列 $A^{\mathsf{T}} A$ の固有値 $\lambda_1 \ge \lambda_2$ を求め，正の固有値の平方根として行列 $A$ のゼロでない特異値 $\sigma_1$ を求めよ。

(2) $A^{\mathsf{T}} A$ の正規直交固有ベクトル $\boldsymbol{v}_1, \boldsymbol{v}_2$ を求め，これを用いて $\boldsymbol{u}_1 = \frac{1}{\sigma_1} A \boldsymbol{v}_1$ を計算せよ。

(3) 行列 $A$ の特異値分解におけるランク1近似の表式 $A_1 = \sigma_1 \boldsymbol{u}_1 \boldsymbol{v}_1^{\mathsf{T}}$ を計算し，これが元の行列 $A$ と厳密に一致することを確かめよ。

---

## 解答・解説

### (1)
積行列 $A^{\mathsf{T}} A$ を計算しその特性方程式を解きます。

転置行列との積を計算すると，
$$
\begin{aligned}
A^{\mathsf{T}} A &= \begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} \\
&= \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
\end{aligned}
$$
となります。

特性方程式を計算すると，
$$
\begin{aligned}
\det(A^{\mathsf{T}} A - \lambda I) &= \begin{vmatrix} 1 - \lambda & 1 \\ 1 & 1 - \lambda \end{vmatrix} \\
&= (1 - \lambda)^2 - 1 = \lambda(\lambda - 2) = 0
\end{aligned}
$$
となります。

したがって，固有値は大きい順に $\lambda_1 = 2, \lambda_2 = 0$ であり，特異値は，
$$
\finalanswer{\sigma_1 = \sqrt{2}}
$$
となります。

### (2)
各固有値に対する単位固有ベクトルを求め，像のベクトルを規格化します。

$\lambda_1 = 2$ に対して $(A^{\mathsf{T}} A - 2I)\boldsymbol{v} = \boldsymbol{0}$ より，
$$
\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
となり，$v_1 = v_2$ を得ます。規格化すると，
$$
\boldsymbol{v}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$
となります。

$\lambda_2 = 0$ に対しては直交するベクトルとして，
$$
\boldsymbol{v}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$
となります。

左特異ベクトル $\boldsymbol{u}_1$ を計算すると，
$$
\begin{aligned}
\boldsymbol{u}_1 &= \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
\end{aligned}
$$
となります。

したがって，求めるベクトルは，
$$
\finalanswer{\boldsymbol{v}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \boldsymbol{v}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \quad \boldsymbol{u}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}}
$$
となります。$\|\boldsymbol{u}_1\| = 1$ であり正規化されています。

### (3)
外積によるダイアド表現を計算します。

定義式に代入して計算すると，
$$
\begin{aligned}
A_1 &= \sigma_1 \boldsymbol{u}_1 \boldsymbol{v}_1^{\mathsf{T}} \\
&= \sqrt{2} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \end{pmatrix} \\
&= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \end{pmatrix} \\
&= \finalanswer{\begin{pmatrix} 1 & 1 \\ 0 & 0 \\ 0 & 0 \end{pmatrix}}
\end{aligned}
$$
となります。これは元の行列 $A$ と厳密に一致し，行列 $A$ の階数が $1$ であったため第1特異値成分のみで完全に復元されます。
===== FILE: 07linear_algebra/07/07_010.md =====
---
tags:
  - 基本
---

# 掃き出し法による逆行列

## 問題
3次正方行列
$$
A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & 0 \end{pmatrix}
$$
を考える。以下の問いに答えよ。

(1) 行列式 $\det A$ を計算し，$A$ が逆行列をもつことを示せ。

(2) 拡大行列 $(A \mid I)$ に対する行基本変形（掃き出し法）を用いて，逆行列 $A^{-1}$ を求めよ。

(3) 積 $A A^{-1}$ を直接計算し，単位行列 $I$ になることを確かめよ。

---

## 解答・解説

### (1)
サラスの公式または余因子展開を用いて行列式を計算します。

第1列で展開して計算すると，
$$
\begin{aligned}
\det A &= 1 \cdot \begin{vmatrix} 1 & 2 \\ 1 & 0 \end{vmatrix} - 0 \cdot \begin{vmatrix} 2 & 1 \\ 1 & 0 \end{vmatrix} + 1 \cdot \begin{vmatrix} 2 & 1 \\ 1 & 2 \end{vmatrix} \\
&= (0 - 2) + (4 - 1) \\
&= -2 + 3 = \finalanswer{1}
\end{aligned}
$$
となります。

$\det A = 1 \neq 0$ であるため，正則行列の判定条件により $A$ は逆行列をもちます。

### (2)
拡大行列の左半分を基本変形によって単位行列へ変形します。

初期の拡大行列を配置します。
$$
\begin{pmatrix} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 2 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 \end{pmatrix}
$$
第3行から第1行を引きます。
$$
\begin{pmatrix} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 2 & 0 & 1 & 0 \\ 0 & -1 & -1 & -1 & 0 & 1 \end{pmatrix}
$$
第3行に第2行を加えます。
$$
\begin{pmatrix} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 2 & 0 & 1 & 0 \\ 0 & 0 & 1 & -1 & 1 & 1 \end{pmatrix}
$$
第2行から第3行の2倍を引き，第1行から第3行を引きます。
$$
\begin{pmatrix} 1 & 2 & 0 & 2 & -1 & -1 \\ 0 & 1 & 0 & 2 & -1 & -2 \\ 0 & 0 & 1 & -1 & 1 & 1 \end{pmatrix}
$$
最後に第1行から第2行の2倍を引きます。
$$
\begin{pmatrix} 1 & 0 & 0 & -2 & 1 & 3 \\ 0 & 1 & 0 & 2 & -1 & -2 \\ 0 & 0 & 1 & -1 & 1 & 1 \end{pmatrix}
$$
右半分に残った行列を取り出すと，
$$
\finalanswer{A^{-1} = \begin{pmatrix} -2 & 1 & 3 \\ 2 & -1 & -2 \\ -1 & 1 & 1 \end{pmatrix}}
$$
となります。

### (3)
得られた行列と元の行列の積を計算します。

積を計算すると，
$$
\begin{aligned}
A A^{-1} &= \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} -2 & 1 & 3 \\ 2 & -1 & -2 \\ -1 & 1 & 1 \end{pmatrix} \\
&= \begin{pmatrix} -2+4-1 & 1-2+1 & 3-4+1 \\ 0+2-2 & 0-1+2 & 0-2+2 \\ -2+2+0 & 1-1+0 & 3-2+0 \end{pmatrix} \\
&= \finalanswer{\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}}
\end{aligned}
$$
となり，正しく単位行列が得られることが確かめられます。
===== FILE: 07linear_algebra/07/07_020.md =====
---
tags:
  - 標準
---

# LU 分解と連立方程式

## 問題
連立一次方程式 $A\boldsymbol{x} = \boldsymbol{b}$ において，係数行列 $A$ および右辺ベクトル $\boldsymbol{b}$ を
$$
A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 5 & 4 \\ 2 & 7 & 8 \end{pmatrix}, \quad \boldsymbol{b} = \begin{pmatrix} 4 \\ 13 \\ 17 \end{pmatrix}
$$
とする。以下の問いに答えよ。

(1) ガウスの消去法を適用することにより，対角成分がすべて $1$ の下三角行列 $L$ と上三角行列 $U$ の積として行列 $A$ を $LU$ 分解せよ。

(2) 補助方程式 $L\boldsymbol{y} = \boldsymbol{b}$ を前進消去によって解き，ベクトル $\boldsymbol{y}$ を求めよ。

(3) 方程式 $U\boldsymbol{x} = \boldsymbol{y}$ を後退代入によって解き，元の連立方程式の解 $\boldsymbol{x}$ を求めよ。

---

## 解答・解説

### (1)
基本変形により上三角行列を作り，その消去係数を下三角行列の成分として配置します。

第1列の消去を行います。第2行から第1行の2倍を引き，第3行から第1行の1倍を引くと，
$$
\begin{pmatrix} 2 & 1 & 1 \\ 0 & 3 & 2 \\ 0 & 6 & 7 \end{pmatrix}
$$
となります。消去係数は $l_{21} = 2, l_{31} = 1$ です。

次に第2列の消去を行います。第3行から第2行の2倍を引くと，
$$
\begin{pmatrix} 2 & 1 & 1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}
$$
となります。消去係数は $l_{32} = 2$ です。

したがって，求める $L$ と $U$ は，
$$
\finalanswer{L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 1 & 2 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}}
$$
となります。

### (2)
下三角行列の性質を用いて上から順番に未知数を決定します。

方程式を行列表示すると，
$$
\begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = \begin{pmatrix} 4 \\ 13 \\ 17 \end{pmatrix}
$$
となります。

第1式より，
$$
y_1 = 4
$$
となります。

第2式に代入すると，
$$
\begin{aligned}
2(4) + y_2 &= 13 \\
y_2 &= 13 - 8 = 5
\end{aligned}
$$
となります。

第3式に代入すると，
$$
\begin{aligned}
4 + 2(5) + y_3 &= 17 \\
14 + y_3 &= 17 \\
y_3 &= 3
\end{aligned}
$$
となります。

したがって，中間ベクトルは，
$$
\finalanswer{\boldsymbol{y} = \begin{pmatrix} 4 \\ 5 \\ 3 \end{pmatrix}}
$$
となります。

### (3)
上三角方程式を下から順番に未知数を求めて解きます。

方程式を行列表示すると，
$$
\begin{pmatrix} 2 & 1 & 1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 4 \\ 5 \\ 3 \end{pmatrix}
$$
となります。

第3式より，
$$
\begin{aligned}
3x_3 &= 3 \\
x_3 &= 1
\end{aligned}
$$
となります。

第2式に代入すると，
$$
\begin{aligned}
3x_2 + 2(1) &= 5 \\
3x_2 &= 3 \\
x_2 &= 1
\end{aligned}
$$
となります。

第1式に代入すると，
$$
\begin{aligned}
2x_1 + 1 + 1 &= 4 \\
2x_1 &= 2 \\
x_1 &= 1
\end{aligned}
$$
となります。

したがって，連立方程式の解は，
$$
\finalanswer{\boldsymbol{x} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}}
$$
となります。
===== FILE: 07linear_algebra/07/07_030.md =====
---
tags:
  - 標準
---

# べき等行列と射影

## 問題
正方行列 $P$ が関係式 $P^2 = P$（べき等性）を満たすとする。以下の問いに答えよ。

(1) $P$ の固有値 $\lambda$ は $0$ または $1$ のいずれかに限られることを示せ。

(2) 行列 $Q = I - P$ を定義するとき，$Q^2 = Q$ および $PQ = QP = O$ が成り立つことを示せ。

(3) 任意のベクトル $\boldsymbol{x}$ は，$\boldsymbol{u} \in \operatorname{Im} P$（$P\boldsymbol{u} = \boldsymbol{u}$）と $\boldsymbol{v} \in \operatorname{Ker} P$（$P\boldsymbol{v} = \boldsymbol{0}$）の和として $\boldsymbol{x} = \boldsymbol{u} + \boldsymbol{v}$ の形に一意に分解できることを示せ。

---

## 解答・解説

### (1)
固有値方程式の両辺に左から行列を掛けて比較します。

$\boldsymbol{x} \neq \boldsymbol{0}$ を固有値 $\lambda$ に属する固有ベクトルとすると，$P\boldsymbol{x} = \lambda \boldsymbol{x}$ です。

両辺に左から $P$ を掛けると，
$$
\begin{aligned}
P(P\boldsymbol{x}) &= P(\lambda \boldsymbol{x}) \\
P^2 \boldsymbol{x} &= \lambda (P\boldsymbol{x}) = \lambda^2 \boldsymbol{x}
\end{aligned}
$$
となります。

一方，仮定 $P^2 = P$ より，
$$
\begin{aligned}
P^2 \boldsymbol{x} &= P\boldsymbol{x} = \lambda \boldsymbol{x}
\end{aligned}
$$
となります。

両式を等置すると，
$$
\begin{aligned}
(\lambda^2 - \lambda) \boldsymbol{x} &= \boldsymbol{0}
\end{aligned}
$$
となります。

$\boldsymbol{x} \neq \boldsymbol{0}$ より，
$$
\begin{aligned}
\lambda(\lambda - 1) &= 0
\end{aligned}
$$
となり，
$$
\finalanswer{\lambda = 0 \quad \text{または} \quad \lambda = 1}
$$
となります。

### (2)
行列積の分配法則を用いて直接展開します。

$Q^2$ を計算すると，
$$
\begin{aligned}
Q^2 &= (I - P)(I - P) \\
&= I^2 - IP - PI + P^2 \\
&= I - 2P + P \\
&= I - P = \finalanswer{Q}
\end{aligned}
$$
となります。

積 $PQ$ および $QP$ を計算すると，
$$
\begin{aligned}
PQ &= P(I - P) = P - P^2 = P - P = \finalanswer{O} \\
QP &= (I - P)P = P - P^2 = P - P = \finalanswer{O}
\end{aligned}
$$
となります。

### (3)
恒等的な分解を構成し，条件の検証と一意性の証明を行います。

任意のベクトル $\boldsymbol{x}$ に対して，
$$
\boldsymbol{u} = P\boldsymbol{x}, \quad \boldsymbol{v} = (I - P)\boldsymbol{x} = Q\boldsymbol{x}
$$
と定義します。このとき $\boldsymbol{u} + \boldsymbol{v} = P\boldsymbol{x} + (I - P)\boldsymbol{x} = \boldsymbol{x}$ が自明に成り立ちます。

各ベクトルへの作用を確かめると，
$$
\begin{aligned}
P\boldsymbol{u} &= P(P\boldsymbol{x}) = P^2 \boldsymbol{x} = P\boldsymbol{x} = \boldsymbol{u} \\
P\boldsymbol{v} &= P(I - P)\boldsymbol{x} = (PQ)\boldsymbol{x} = \boldsymbol{0}
\end{aligned}
$$
となり，条件を満たす分解が存在します。

次に一意性を示します。仮に別の分解 $\boldsymbol{x} = \boldsymbol{u}' + \boldsymbol{v}'$（$P\boldsymbol{u}' = \boldsymbol{u}', P\boldsymbol{v}' = \boldsymbol{0}$）が存在したとします。

両辺に左から $P$ を掛けると，
$$
\begin{aligned}
P\boldsymbol{x} &= P(\boldsymbol{u}' + \boldsymbol{v}') \\
&= P\boldsymbol{u}' + P\boldsymbol{v}' \\
&= \boldsymbol{u}' + \boldsymbol{0} = \boldsymbol{u}'
\end{aligned}
$$
となります。

これにより $\boldsymbol{u}' = P\boldsymbol{x} = \boldsymbol{u}$ が導かれ，直ちに $\boldsymbol{v}' = \boldsymbol{x} - \boldsymbol{u}' = \boldsymbol{x} - \boldsymbol{u} = \boldsymbol{v}$ となります。

したがって，分解は，
$$
\finalanswer{\boldsymbol{x} = \boldsymbol{u} + \boldsymbol{v} \quad (P\boldsymbol{u}=\boldsymbol{u}, \ P\boldsymbol{v}=\boldsymbol{0})}
$$
の形に一意に定まります。全空間が像空間と核空間の直和に分解されることを意味します。
===== END =====