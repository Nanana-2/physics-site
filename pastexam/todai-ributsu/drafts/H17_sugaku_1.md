---
title: 東大理物 平成17年度 数学 第1問：2次形式の直交対角化と勾配系の漸近安定性
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成17年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成17年度 数学 第1問：2次形式の直交対角化と勾配系の漸近安定性

## 問題

(1) $n$ 個の $n$ 次元列ベクトル $\boldsymbol{u}_j$（$j = 1, \cdots, n$）を用いて，行列 $U$ を $U = (\boldsymbol{u}_1, \boldsymbol{u}_2, \cdots, \boldsymbol{u}_n)$ で定義するとき，$U$ がユニタリー行列ならば，$\{\boldsymbol{u}_j\}$ は正規直交系をなすことを示せ。

(2) $A$ を実対称行列，$\boldsymbol{x} = (x_1, \cdots, x_n)^T$ を $n$ 次元ベクトルとする。ただし，$T$ は転置を表す。このとき実2次形式 $\phi(\boldsymbol{x}) = \boldsymbol{x}^T A\boldsymbol{x}$ に対し適当な直交変換 $\boldsymbol{x} = P\boldsymbol{y}$ を行うと，対角行列 $B$ を用いて $\phi = \boldsymbol{y}^T B\boldsymbol{y} = \displaystyle\sum_{i=1}^{n} \lambda_i y_i^2$ の標準形に変換できる。$\phi(\boldsymbol{x}) = 4x_1^2 + 2x_2^2 + 2x_3^2 - 2x_1 x_2 + 2x_2 x_3 - 2x_3 x_1$ について $A,\ P,\ \lambda_i$（$i = 1, 2, 3$）を求め標準形で表わせ。

(3) $A$ を $n$ 次実対称行列として，次の微分方程式を考える。

$$
\frac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = A\boldsymbol{x}
$$

このとき，スカラー関数 $\Phi(\boldsymbol{x})$ を用いて $\dfrac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = -\nabla_{\boldsymbol{x}}\Phi(\boldsymbol{x})$ と書けることを $\Phi(\boldsymbol{x})$ の具体形とともに示せ。ただし，$\dfrac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = \left(\dfrac{\mathrm{d}x_1}{\mathrm{d}t}, \cdots, \dfrac{\mathrm{d}x_n}{\mathrm{d}t}\right)^T$，$\nabla_{\boldsymbol{x}}\Phi = \left(\dfrac{\partial\Phi}{\partial x_1}, \cdots, \dfrac{\partial\Phi}{\partial x_n}\right)^T$ である。

(4) 設問 (3) で軌道 $\boldsymbol{x}(t)$ に沿った $\Phi$ の微分 $\mathrm{d}\Phi(\boldsymbol{x}(t))/\mathrm{d}t$ は，$\dfrac{\mathrm{d}\Phi(\boldsymbol{x}(t))}{\mathrm{d}t} \le 0$ を満たすことを示せ。また，任意の $\boldsymbol{x}(\boldsymbol{x} \neq \boldsymbol{0})$ に対し $\Phi > 0$ が成り立つならば，解軌道は最終的に $\boldsymbol{x} = \boldsymbol{0}$ に漸近することを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成17年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
実対称行列は実直交行列によって対角化することができ，固有ベクトルを列に並べた直交変換で2次形式から交差項を消すことができます。

実対称行列 $A$ による線形微分方程式 $\mathrm{d}\boldsymbol{x}/\mathrm{d}t = A\boldsymbol{x}$ は，2次形式 $\Phi(\boldsymbol{x}) = -\dfrac{1}{2}\boldsymbol{x}^T A\boldsymbol{x}$ の負の勾配として書くことができます。このとき $\Phi$ の正定値性は $A$ のすべての固有値が負であることと同値になるため，直交対角化によって解の長時間挙動を直接求めることができます。
</div>

### (1)

$U = (\boldsymbol{u}_1, \boldsymbol{u}_2, \dots, \boldsymbol{u}_n)$ のエルミート共役 $U^\dagger$ は，行ベクトル $\boldsymbol{u}_1^\dagger, \boldsymbol{u}_2^\dagger, \dots, \boldsymbol{u}_n^\dagger$ を縦に並べた行列です。

$$
U^\dagger = \begin{pmatrix} \boldsymbol{u}_1^\dagger \\ \boldsymbol{u}_2^\dagger \\ \vdots \\ \boldsymbol{u}_n^\dagger \end{pmatrix}
$$

したがって，積 $U^\dagger U$ の $(j, k)$ 成分は内積 $(\boldsymbol{u}_j, \boldsymbol{u}_k) = \boldsymbol{u}_j^\dagger \boldsymbol{u}_k$ に等しくなります。

$$
\begin{aligned}
(U^\dagger U)_{jk} &= \boldsymbol{u}_j^\dagger \boldsymbol{u}_k \\
&= (\boldsymbol{u}_j, \boldsymbol{u}_k)
\end{aligned}
$$

$U$ はユニタリー行列なので $U^\dagger U = I$ であり，すべての $j, k = 1, \dots, n$ に対して $(U^\dagger U)_{jk} = \delta_{jk}$ が成り立ちます。よって次式が得られます。

$$
(\boldsymbol{u}_j, \boldsymbol{u}_k) = \delta_{jk} \qquad (j, k = 1, \dots, n)
$$

したがって，$\{\boldsymbol{u}_j\}$ は正規直交系をなします。

### (2)

2次形式 $\phi(\boldsymbol{x}) = 4x_1^2 + 2x_2^2 + 2x_3^2 - 2x_1 x_2 + 2x_2 x_3 - 2x_3 x_1$ に対応する実対称行列 $A$ は，対角成分に $x_i^2$ の係数，非対角成分に $x_i x_j$（$i \neq j$）の係数の半分を置いて定まります。

$$
A = \begin{pmatrix} 4 & -1 & -1 \\ -1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}
$$

固有方程式 $\det(A - \lambda I) = 0$ を計算します。第2行から第3行を引くと共通因子 $1 - \lambda$ をくくり出すことができます。

$$
\begin{aligned}
\det(A - \lambda I) &= \begin{vmatrix} 4 - \lambda & -1 & -1 \\ -1 & 2 - \lambda & 1 \\ -1 & 1 & 2 - \lambda \end{vmatrix} \\
&= \begin{vmatrix} 4 - \lambda & -1 & -1 \\ 0 & 1 - \lambda & -(1 - \lambda) \\ -1 & 1 & 2 - \lambda \end{vmatrix} \\
&= (1 - \lambda)\begin{vmatrix} 4 - \lambda & -1 & -1 \\ 0 & 1 & -1 \\ -1 & 1 & 2 - \lambda \end{vmatrix}
\end{aligned}
$$

さらに第3列に第2列を加えて第2行で余因子展開します。

$$
\begin{aligned}
\det(A - \lambda I) &= (1 - \lambda)\begin{vmatrix} 4 - \lambda & -1 & -2 \\ 0 & 1 & 0 \\ -1 & 1 & 3 - \lambda \end{vmatrix} \\
&= (1 - \lambda)\bigl((4 - \lambda)(3 - \lambda) - 2\bigr) \\
&= (1 - \lambda)(\lambda^2 - 7\lambda + 10) \\
&= -( \lambda - 1)(\lambda - 2)(\lambda - 5)
\end{aligned}
$$

よって3つの固有値は $\lambda_1 = 1$，$\lambda_2 = 2$，$\lambda_3 = 5$ です。次に各固有値に対する規格化された固有ベクトル $\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3$ を求めます。

$\lambda_1 = 1$ のとき，$(A - I)\boldsymbol{v} = \boldsymbol{0}$ を書きます。

$$
\begin{pmatrix} 3 & -1 & -1 \\ -1 & 1 & 1 \\ -1 & 1 & 1 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

第1式と第2式を加えると $2v_1 = 0$ より $v_1 = 0$，第2式より $v_2 + v_3 = 0$ です。規格化すると $\boldsymbol{p}_1 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$ が得られます。

$\lambda_2 = 2$ のとき，$(A - 2I)\boldsymbol{v} = \boldsymbol{0}$ を書きます。

$$
\begin{pmatrix} 2 & -1 & -1 \\ -1 & 0 & 1 \\ -1 & 1 & 0 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

第2式より $v_1 = v_3$，第3式より $v_1 = v_2$ です。規格化すると $\boldsymbol{p}_2 = \dfrac{1}{\sqrt{3}}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ が得られます。

$\lambda_3 = 5$ のとき，$(A - 5I)\boldsymbol{v} = \boldsymbol{0}$ を書きます。

$$
\begin{pmatrix} -1 & -1 & -1 \\ -1 & -3 & 1 \\ -1 & 1 & -3 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

第2式から第3式を引くと $-4v_2 + 4v_3 = 0$ より $v_2 = v_3$，第1式より $v_1 = -2v_2$ です。規格化すると $\boldsymbol{p}_3 = \dfrac{1}{\sqrt{6}}\begin{pmatrix} -2 \\ 1 \\ 1 \end{pmatrix}$ が得られます。

実対称行列の異なる固有値に属する固有ベクトルなので $\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3$ は互いに直交します。これらを列に並べた行列 $P = (\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3)$ は直交行列であり，$P^T A P = \operatorname{diag}(1, 2, 5)$ です。したがって求める $A, P, \lambda_i$ および標準形は次式となります。

$$
\finalanswer{
A = \begin{pmatrix} 4 & -1 & -1 \\ -1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}, \quad
P = \begin{pmatrix} 0 & \dfrac{1}{\sqrt{3}} & -\dfrac{2}{\sqrt{6}} \\[6pt] \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{6}} \\[6pt] -\dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{6}} \end{pmatrix}, \quad
(\lambda_1, \lambda_2, \lambda_3) = (1, 2, 5), \quad
\phi = y_1^2 + 2y_2^2 + 5y_3^2
}
$$

### (3)

スカラー関数 $\Phi(\boldsymbol{x})$ を次式で定義します。

$$
\begin{aligned}
\Phi(\boldsymbol{x}) &= -\frac{1}{2}\boldsymbol{x}^T A\boldsymbol{x} \\
&= -\frac{1}{2}\sum_{j=1}^{n}\sum_{k=1}^{n} a_{jk} x_j x_k
\end{aligned}
$$

ここで $a_{jk}$ は $A$ の $(j, k)$ 成分であり，$A$ が実対称行列なので $a_{jk} = a_{kj}$ です。$\Phi(\boldsymbol{x})$ を $x_i$ で偏微分します。

$$
\begin{aligned}
\frac{\partial\Phi}{\partial x_i} &= -\frac{1}{2}\sum_{j=1}^{n}\sum_{k=1}^{n} a_{jk}\bigl(\delta_{ij}x_k + x_j\delta_{ik}\bigr) \\
&= -\frac{1}{2}\left(\sum_{k=1}^{n} a_{ik} x_k + \sum_{j=1}^{n} a_{ji} x_j\right) \\
&= -\sum_{k=1}^{n} a_{ik} x_k \\
&= -(A\boldsymbol{x})_i
\end{aligned}
$$

ここで $a_{ji} = a_{ij}$ を用いました。したがって $-\nabla_{\boldsymbol{x}}\Phi(\boldsymbol{x}) = A\boldsymbol{x}$ となり，微分方程式は $\dfrac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = -\nabla_{\boldsymbol{x}}\Phi(\boldsymbol{x})$ と書くことができます。なお $\Phi(\boldsymbol{x})$ には任意の定数を加えても同じ勾配を与えます。

$$
\finalanswer{\Phi(\boldsymbol{x}) = -\frac{1}{2}\boldsymbol{x}^T A\boldsymbol{x}}
$$

### (4)

軌道 $\boldsymbol{x}(t)$ に沿った $\Phi(\boldsymbol{x}(t))$ の時間微分を合成関数の微分則と設問 (3) の関係 $\dfrac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = -\nabla_{\boldsymbol{x}}\Phi(\boldsymbol{x})$ を用いて計算します。

$$
\begin{aligned}
\frac{\mathrm{d}\Phi(\boldsymbol{x}(t))}{\mathrm{d}t} &= \sum_{i=1}^{n} \frac{\partial\Phi}{\partial x_i}\frac{\mathrm{d}x_i}{\mathrm{d}t} \\
&= \bigl(\nabla_{\boldsymbol{x}}\Phi(\boldsymbol{x}(t))\bigr)^T \frac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} \\
&= -\bigl(\nabla_{\boldsymbol{x}}\Phi(\boldsymbol{x}(t))\bigr)^T \nabla_{\boldsymbol{x}}\Phi(\boldsymbol{x}(t)) \\
&= -\sum_{i=1}^{n} \left(\frac{\partial\Phi}{\partial x_i}\right)^2 \le 0
\end{aligned}
$$

これにより $\dfrac{\mathrm{d}\Phi(\boldsymbol{x}(t))}{\mathrm{d}t} \le 0$ が成り立ちます。

次に，$\Phi(\boldsymbol{x}) = -\dfrac{1}{2}\boldsymbol{x}^T A\boldsymbol{x}$ が任意の $\boldsymbol{x} \neq \boldsymbol{0}$ に対して $\Phi(\boldsymbol{x}) > 0$ を満たす場合を考えます。$A$ は実対称行列なので，実直交行列 $P$ を用いて $P^T A P = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ と対角化することができます。$\boldsymbol{x} = P\boldsymbol{y}$ と変換すると，$\Phi(\boldsymbol{x})$ は次式になります。

$$
\begin{aligned}
\Phi(\boldsymbol{x}) &= -\frac{1}{2}\boldsymbol{y}^T P^T A P\boldsymbol{y} \\
&= -\frac{1}{2}\sum_{i=1}^{n} \lambda_i y_i^2
\end{aligned}
$$

任意の $\boldsymbol{y} \neq \boldsymbol{0}$ に対して $\Phi > 0$ が成り立つため，各 $k = 1, \dots, n$ について $y_k = 1$，他の成分を $0$ と選ぶと $-\dfrac{1}{2}\lambda_k > 0$，すなわちすべての固有値が $\lambda_k < 0$ となります。

微分方程式 $\dfrac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = A\boldsymbol{x}$ に $\boldsymbol{x} = P\boldsymbol{y}$ を代入し，左から $P^T$ を掛けます。

$$
\frac{\mathrm{d}\boldsymbol{y}}{\mathrm{d}t} = P^T A P\boldsymbol{y}
$$

これを各成分ごとに書くと，次式になります。

$$
\frac{\mathrm{d}y_i}{\mathrm{d}t} = \lambda_i y_i \qquad (i = 1, \dots, n)
$$

各成分を積分すると $y_i(t) = y_i(0)e^{\lambda_i t}$ が得られます。すべての $i$ で $\lambda_i < 0$ なので，$t \to \infty$ の極限で $y_i(t) \to 0$ となります。したがって $\boldsymbol{x}(t) = P\boldsymbol{y}(t) \to \boldsymbol{0}$ となり，解軌道は最終的に $\boldsymbol{x} = \boldsymbol{0}$ に漸近します。
