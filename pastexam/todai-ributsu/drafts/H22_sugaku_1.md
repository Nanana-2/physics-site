---
title: 東大理物 平成22年度 数学 第1問：正定値対称行列に対する最急降下法の収束性
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成22年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成22年度 数学 第1問：正定値対称行列に対する最急降下法の収束性

## 問題

$A$ は $n$ 行 $n$ 列の実対称行列で，その固有値はすべて正とする。$\boldsymbol{x}$ と $\boldsymbol{b}$ は $n$ 行 $1$ 列の実数値をとる縦ベクトルとする。$\boldsymbol{x}$ に関する線形方程式 $A\boldsymbol{x} = \boldsymbol{b}$ の解 $\bar{\boldsymbol{x}}$ を求めたい。任意の初期ベクトル $\boldsymbol{x}^{(0)}$ から始めて，$\boldsymbol{x}^{(0)} \to \boldsymbol{x}^{(1)} \to \boldsymbol{x}^{(2)} \to \cdots \to \bar{\boldsymbol{x}}$ のような逐次的なステップにより $\bar{\boldsymbol{x}}$ を探索する手続きを考える。$n$ 行 $1$ 列の実数値をとる任意の縦ベクトル $\boldsymbol{y}$ に対して，その大きさを表す二種類のノルムとして，$\|\boldsymbol{y}\| = \sqrt{\boldsymbol{y}^{\mathrm{t}}\boldsymbol{y}}$ と $\|\boldsymbol{y}\|_A = \sqrt{\boldsymbol{y}^{\mathrm{t}} A \boldsymbol{y}}$ を定義する。ここで，$\boldsymbol{y}^{\mathrm{t}}$ は $\boldsymbol{y}$ の転置ベクトルを表す。以下の設問に答えよ。

(1) 線形方程式 $A\boldsymbol{x} = \boldsymbol{b}$ の解 $\bar{\boldsymbol{x}}$ は，次の量

$$
f(\boldsymbol{x}) = \frac{1}{2}\boldsymbol{x}^{\mathrm{t}} A \boldsymbol{x} - \boldsymbol{b}^{\mathrm{t}}\boldsymbol{x} = \frac{1}{2}\sum_{i=1}^n \sum_{j=1}^n x_i A_{ij} x_j - \sum_{i=1}^n b_i x_i
$$

の最小値で与えられる事を示せ。ここで，$x_i$ と $b_i$ はそれぞれ，縦ベクトル $\boldsymbol{x}$ と $\boldsymbol{b}$ の $i$ 番目の成分を表す。また，$A_{ij}$ は行列 $A$ の $(i, j)$ 成分を表す。

(2) $f(\boldsymbol{x})$ の最小値を与えるベクトル $\bar{\boldsymbol{x}}$ を探索する時に，$m$ 回後のステップのベクトル $\boldsymbol{x}^{(m)}$ から $(m + 1)$ 回後のステップのベクトル $\boldsymbol{x}^{(m+1)}$ を次の手順で求める。まず，適当な実数パラメーター $\alpha$ を選び，$\boldsymbol{x}^{(m+1)} = \boldsymbol{x}^{(m)} + \alpha\boldsymbol{r}$ とおく。ここで，探索方向ベクトル $\boldsymbol{r}$ は，その成分を $r_i = -\left.\dfrac{\partial f(\boldsymbol{x})}{\partial x_i}\right|_{\boldsymbol{x} = \boldsymbol{x}^{(m)}}$ として，$f(\boldsymbol{x})$ の勾配ベクトルと反対方向にとる。このとき，$\boldsymbol{r} = -A(\boldsymbol{x}^{(m)} - \bar{\boldsymbol{x}})$ であることを示せ。

(3) 一回のステップで $f(\boldsymbol{x})$ が最も大きく減少するようにパラメーター $\alpha$ を選ぶ。このとき，$\alpha$ を $\|\boldsymbol{r}\|$ と $\|\boldsymbol{r}\|_A$ を用いて表せ。

(4) $\boldsymbol{x}^{(m)}$ の $\bar{\boldsymbol{x}}$ からのズレを $\delta\boldsymbol{x}^{(m)} = \boldsymbol{x}^{(m)} - \bar{\boldsymbol{x}}$ とする。このとき，$\|\delta\boldsymbol{x}^{(m+1)}\|_A$ を $\|\delta\boldsymbol{x}^{(m)}\|_A$，$\|\boldsymbol{r}\|$ および $\|\boldsymbol{r}\|_A$ を用いて表せ。

(5) $A$ の $n$ 個の固有値を $\lambda_i$，対応する規格直交化された固有ベクトルを $\boldsymbol{a}_i$（$i = 1, 2, \cdots, n$）とする。さらに，$\delta\boldsymbol{x}^{(m)}$ の固有ベクトル $\boldsymbol{a}_i$ による展開を $\delta\boldsymbol{x}^{(m)} = \sum_{i=1}^n \rho_i \boldsymbol{a}_i$ とする。このとき，ノルムの変化，$R = \dfrac{\|\delta\boldsymbol{x}^{(m+1)}\|_A}{\|\delta\boldsymbol{x}^{(m)}\|_A}$，を固有値 $\lambda_i$ と展開係数 $\rho_i$ を用いて表せ。

(6) $A$ を $2$ 行 $2$ 列とし，その固有値の比 $p = \lambda_1 / \lambda_2$ が $0 < p \le 1$ を満たすとする。このとき，設問 (5) の結果を用いて $R$ に上限があることを示し，任意の初期ベクトル $\boldsymbol{x}^{(0)}$ から始めた探索が必ず収束することを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成22年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
$A$ が対称で固有値がすべて正のとき，$\boldsymbol{y}^{\mathrm{t}}A\boldsymbol{y}$ は $\boldsymbol{y}\neq\boldsymbol{0}$ で正になります。そのため，$f(\boldsymbol{x})$ を $\bar{\boldsymbol{x}}$ のまわりで平方完成すると，$A\boldsymbol{x}=\boldsymbol{b}$ を解く問題を $f$ の最小値を探す問題に置き換えることができます。

1回のステップでは，$f(\boldsymbol{x}^{(m)}+\alpha\boldsymbol{r})$ を $\alpha$ の2次関数とみて，その最小を与える $\alpha$ を選びます。ズレ $\delta\boldsymbol{x}^{(m)}$ を $A$ の固有ベクトルで展開すると，$A$ を掛ける操作は各成分に固有値を掛けることになります。そのため，ノルムの比 $R$ を固有値と展開係数で書くことができます。

2行2列では展開係数が $\rho_1$ と $\rho_2$ の2つだけになります。$R^2$ の分母に相加平均と相乗平均の不等式を用いると，$\rho_1$，$\rho_2$ によらない上限を作ることができます。
</div>

### (1)
$A$ は実対称行列なので $A^{\mathrm{t}} = A$ であり，任意のベクトル $\boldsymbol{u}, \boldsymbol{v}$ に対して $\boldsymbol{u}^{\mathrm{t}} A \boldsymbol{v} = \boldsymbol{v}^{\mathrm{t}} A \boldsymbol{u}$ です。$\boldsymbol{b} = A\bar{\boldsymbol{x}}$ を $f(\boldsymbol{x})$ に代入して平方完成します。

$$
\begin{aligned}
f(\boldsymbol{x}) &= \frac{1}{2}\boldsymbol{x}^{\mathrm{t}} A \boldsymbol{x} - (A\bar{\boldsymbol{x}})^{\mathrm{t}}\boldsymbol{x} \\
&= \frac{1}{2}\boldsymbol{x}^{\mathrm{t}} A \boldsymbol{x} - \bar{\boldsymbol{x}}^{\mathrm{t}} A \boldsymbol{x} \\
&= \frac{1}{2}(\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathrm{t}} A (\boldsymbol{x} - \bar{\boldsymbol{x}}) - \frac{1}{2}\bar{\boldsymbol{x}}^{\mathrm{t}} A \bar{\boldsymbol{x}} \\
&= \frac{1}{2}\|\boldsymbol{x} - \bar{\boldsymbol{x}}\|_A^2 - \frac{1}{2}\|\bar{\boldsymbol{x}}\|_A^2
\end{aligned}
$$

$A$ の固有値はすべて正なので，任意の $\boldsymbol{y}$ に対して $\|\boldsymbol{y}\|_A^2 = \boldsymbol{y}^{\mathrm{t}} A \boldsymbol{y} \ge 0$ であり，等号が成り立つのは $\boldsymbol{y} = \boldsymbol{0}$ のときに限ります。したがって $f(\boldsymbol{x})$ は $\boldsymbol{x} = \bar{\boldsymbol{x}}$ で唯一の最小値 $-\dfrac{1}{2}\|\bar{\boldsymbol{x}}\|_A^2$ をとります。

### (2)
$\displaystyle f(\boldsymbol{x}) = \dfrac{1}{2}\sum_{j=1}^n \sum_{k=1}^n x_j A_{jk} x_k - \sum_{j=1}^n b_j x_j$ を $x_i$ で偏微分し，対称性 $A_{ji} = A_{ij}$ を用います。

$$
\begin{aligned}
\frac{\partial f(\boldsymbol{x})}{\partial x_i} &= \frac{1}{2}\sum_{k=1}^n A_{ik} x_k + \frac{1}{2}\sum_{j=1}^n x_j A_{ji} - b_i \\
&= \sum_{j=1}^n A_{ij} x_j - b_i \\
&= (A\boldsymbol{x} - \boldsymbol{b})_i
\end{aligned}
$$

$\boldsymbol{x} = \boldsymbol{x}^{(m)}$ として $\boldsymbol{b} = A\bar{\boldsymbol{x}}$ を代入すると，次式が成り立ちます。

$$
\begin{aligned}
\boldsymbol{r} &= -(A\boldsymbol{x}^{(m)} - \boldsymbol{b}) \\
&= -(A\boldsymbol{x}^{(m)} - A\bar{\boldsymbol{x}}) \\
&= -A(\boldsymbol{x}^{(m)} - \bar{\boldsymbol{x}})
\end{aligned}
$$

### (3)
$f(\boldsymbol{x}^{(m)} + \alpha\boldsymbol{r})$ を $\alpha$ について展開します。対称性 $A^{\mathrm{t}} = A$ と $A\boldsymbol{x}^{(m)} - \boldsymbol{b} = -\boldsymbol{r}$ を用います。

$$
\begin{aligned}
f(\boldsymbol{x}^{(m)} + \alpha\boldsymbol{r}) &= \frac{1}{2}(\boldsymbol{x}^{(m)} + \alpha\boldsymbol{r})^{\mathrm{t}} A (\boldsymbol{x}^{(m)} + \alpha\boldsymbol{r}) - \boldsymbol{b}^{\mathrm{t}}(\boldsymbol{x}^{(m)} + \alpha\boldsymbol{r}) \\
&= f(\boldsymbol{x}^{(m)}) + \alpha\boldsymbol{r}^{\mathrm{t}}(A\boldsymbol{x}^{(m)} - \boldsymbol{b}) + \frac{1}{2}\alpha^2 \boldsymbol{r}^{\mathrm{t}} A \boldsymbol{r} \\
&= f(\boldsymbol{x}^{(m)}) - \alpha\|\boldsymbol{r}\|^2 + \frac{1}{2}\alpha^2 \|\boldsymbol{r}\|_A^2
\end{aligned}
$$

残差 $\boldsymbol{r}=\boldsymbol{0}$ なら，すでに解に達しているので反復を終了します。以下では $\boldsymbol{r}\ne\boldsymbol{0}$ とします。$\boldsymbol{r} \neq \boldsymbol{0}$ のとき $\|\boldsymbol{r}\|_A^2 > 0$ なので，この $\alpha$ の2次関数は微分が $0$ になる点で最小値をとります。

$$
\frac{\mathrm{d}}{\mathrm{d}\alpha}f(\boldsymbol{x}^{(m)}+\alpha\boldsymbol{r})
=-\|\boldsymbol{r}\|^2+\alpha\|\boldsymbol{r}\|_A^2
$$

微分を $0$ とおき，$\alpha$ について解きます。

$$
-\|\boldsymbol{r}\|^2+\alpha\|\boldsymbol{r}\|_A^2=0
$$

$$
\finalanswer{\alpha = \frac{\|\boldsymbol{r}\|^2}{\|\boldsymbol{r}\|_A^2}}
$$

### (4)
更新後のずれは次のようになります。

$$
\begin{aligned}
\delta\boldsymbol{x}^{(m+1)}&=\boldsymbol{x}^{(m+1)}-\bar{\boldsymbol{x}}\\
&=\delta\boldsymbol{x}^{(m)}+\alpha\boldsymbol{r}
\end{aligned}
$$

右辺の $A$ ノルムの2乗を展開します。$A\delta\boldsymbol{x}^{(m)}=-\boldsymbol{r}$ と最適な $\alpha$ の式を用います。

$$
\begin{aligned}
\|\delta\boldsymbol{x}^{(m+1)}\|_A^2 &= (\delta\boldsymbol{x}^{(m)} + \alpha\boldsymbol{r})^{\mathrm{t}} A (\delta\boldsymbol{x}^{(m)} + \alpha\boldsymbol{r}) \\
&= \|\delta\boldsymbol{x}^{(m)}\|_A^2 + 2\alpha\boldsymbol{r}^{\mathrm{t}} A\delta\boldsymbol{x}^{(m)} + \alpha^2 \|\boldsymbol{r}\|_A^2 \\
&= \|\delta\boldsymbol{x}^{(m)}\|_A^2 - 2\alpha\|\boldsymbol{r}\|^2 + \alpha^2 \|\boldsymbol{r}\|_A^2 \\
&= \|\delta\boldsymbol{x}^{(m)}\|_A^2 - 2\frac{\|\boldsymbol{r}\|^4}{\|\boldsymbol{r}\|_A^2} + \frac{\|\boldsymbol{r}\|^4}{\|\boldsymbol{r}\|_A^2} \\
&= \|\delta\boldsymbol{x}^{(m)}\|_A^2 - \frac{\|\boldsymbol{r}\|^4}{\|\boldsymbol{r}\|_A^2}
\end{aligned}
$$

平方根をとると次式が得られます。

$$
\finalanswer{\|\delta\boldsymbol{x}^{(m+1)}\|_A = \sqrt{\|\delta\boldsymbol{x}^{(m)}\|_A^2 - \frac{\|\boldsymbol{r}\|^4}{\|\boldsymbol{r}\|_A^2}}}
$$

### (5)
以下の比 $R$ は，まだ解に達していない $\delta\boldsymbol{x}^{(m)}\ne\boldsymbol{0}$ の段階で定義します。$\displaystyle \delta\boldsymbol{x}^{(m)} = \sum_{i=1}^n \rho_i \boldsymbol{a}_i$ と $A\boldsymbol{a}_i = \lambda_i \boldsymbol{a}_i$，および正規直交性 $\boldsymbol{a}_i^{\mathrm{t}}\boldsymbol{a}_j = \delta_{ij}$ を用いて各ノルムの2乗を計算します。まず 

$$
\begin{aligned}
\boldsymbol{r}&=-A\delta\boldsymbol{x}^{(m)}\\
&=-\sum_{i=1}^n\lambda_i\rho_i\boldsymbol{a}_i
\end{aligned}
$$

なので，

$$
\|\delta\boldsymbol{x}^{(m)}\|_A^2=\sum_{i=1}^n\lambda_i\rho_i^2
$$

残差の通常のノルムと $A$ ノルムは，それぞれ次のようになります。

$$
\begin{aligned}
\|\boldsymbol{r}\|^2&=\sum_{i=1}^n\lambda_i^2\rho_i^2,\\
\|\boldsymbol{r}\|_A^2&=\sum_{i=1}^n\lambda_i^3\rho_i^2
\end{aligned}
$$

となります。これらを設問 (4) の結果に代入して $R = \dfrac{\|\delta\boldsymbol{x}^{(m+1)}\|_A}{\|\delta\boldsymbol{x}^{(m)}\|_A}$ を求めます。

$$
\begin{aligned}
R &= \sqrt{1 - \frac{\|\boldsymbol{r}\|^4}{\|\delta\boldsymbol{x}^{(m)}\|_A^2 \|\boldsymbol{r}\|_A^2}} \\
&= \sqrt{1 - \frac{\left(\sum_{i=1}^n \lambda_i^2 \rho_i^2\right)^2}{\left(\sum_{i=1}^n \lambda_i \rho_i^2\right)\left(\sum_{i=1}^n \lambda_i^3 \rho_i^2\right)}}
\end{aligned}
$$

$$
\finalanswer{R = \sqrt{1 - \frac{\left(\sum_{i=1}^n \lambda_i^2 \rho_i^2\right)^2}{\left(\sum_{i=1}^n \lambda_i \rho_i^2\right)\left(\sum_{i=1}^n \lambda_i^3 \rho_i^2\right)}}}
$$

### (6)
$n = 2$ のとき，設問 (5) の $R^2$ を通分して整理します。

$$
\begin{aligned}
R^2 &= \frac{(\lambda_1 \rho_1^2 + \lambda_2 \rho_2^2)(\lambda_1^3 \rho_1^2 + \lambda_2^3 \rho_2^2) - (\lambda_1^2 \rho_1^2 + \lambda_2^2 \rho_2^2)^2}{(\lambda_1 \rho_1^2 + \lambda_2 \rho_2^2)(\lambda_1^3 \rho_1^2 + \lambda_2^3 \rho_2^2)} \\
&= \frac{\lambda_1\lambda_2(\lambda_1^2 - 2\lambda_1\lambda_2 + \lambda_2^2)\rho_1^2 \rho_2^2}{\lambda_1^4 \rho_1^4 + \lambda_2^4 \rho_2^4 + \lambda_1\lambda_2(\lambda_1^2 + \lambda_2^2)\rho_1^2 \rho_2^2} \\
&= \frac{\lambda_1\lambda_2(\lambda_2 - \lambda_1)^2 \rho_1^2 \rho_2^2}{\lambda_1^4 \rho_1^4 + \lambda_2^4 \rho_2^4 + \lambda_1\lambda_2(\lambda_1^2 + \lambda_2^2)\rho_1^2 \rho_2^2}
\end{aligned}
$$

$\rho_1 = 0$ または $\rho_2 = 0$ のときは分子が $0$ となり $R = 0$ です。$\rho_1 \neq 0$ かつ $\rho_2 \neq 0$ のとき，分母に対して相加平均と相乗平均の不等式 $\lambda_1^4 \rho_1^4 + \lambda_2^4 \rho_2^4 \ge 2\lambda_1^2 \lambda_2^2 \rho_1^2 \rho_2^2$ を用います。

$$
\begin{aligned}
\lambda_1^4 \rho_1^4 + \lambda_2^4 \rho_2^4 + \lambda_1\lambda_2(\lambda_1^2 + \lambda_2^2)\rho_1^2 \rho_2^2 &\ge \lambda_1\lambda_2(\lambda_1^2 + 2\lambda_1\lambda_2 + \lambda_2^2)\rho_1^2 \rho_2^2 \\
&= \lambda_1\lambda_2(\lambda_2 + \lambda_1)^2 \rho_1^2 \rho_2^2
\end{aligned}
$$

したがって $R^2$ は次のように上から抑えられます。

$$
\begin{aligned}
R^2 &\le \frac{\lambda_1\lambda_2(\lambda_2 - \lambda_1)^2 \rho_1^2 \rho_2^2}{\lambda_1\lambda_2(\lambda_2 + \lambda_1)^2 \rho_1^2 \rho_2^2} \\
&= \left(\frac{\lambda_2 - \lambda_1}{\lambda_2 + \lambda_1}\right)^2 \\
&= \left(\frac{1 - p}{1 + p}\right)^2
\end{aligned}
$$

$0 < p \le 1$ より $R_0 \equiv \dfrac{1 - p}{1 + p}$ は $0 \le R_0 < 1$ を満たし，すべてのステップで $R \le R_0 < 1$ が成り立ちます。よって任意の初期ベクトル $\boldsymbol{x}^{(0)}$ に対して

$$
\|\delta\boldsymbol{x}^{(m)}\|_A \le R_0^m \|\delta\boldsymbol{x}^{(0)}\|_A
$$

となり，$m \to \infty$ で $R_0^m \to 0$ なので $\|\delta\boldsymbol{x}^{(m)}\|_A \to 0$，すなわち $\boldsymbol{x}^{(m)} \to \bar{\boldsymbol{x}}$ と必ず収束します。
