---
title: 東大理物 平成9年度 一般教育科目 数学 第1問：3変数2次形式の直交対角化と回転行列の位数
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 一般教育科目 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成9年度 一般教育科目 数学 第1問：3変数2次形式の直交対角化と回転行列の位数

## 問題

実変数 $x, y, z$ に関する2次形式

$$
f(x, y, z) = 2x^2 + 3y^2 + 4z^2 - \sqrt{6}xy + \sqrt{6}yz \qquad \text{(1)}
$$

について，以下の設問に答えよ。
{: .problem-lead }

(a) ベクトル $\vec{r}$ を $\vec{r} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$ とし，$f(x, y, z) = \vec{r}^{\,T} A \vec{r}$ と表した時，対称行列 $A$ の固有値と単位固有ベクトル（第2成分は非負）を求めよ。ここでは $\vec{r}^{\,T}$ は $\vec{r}$ の転置を表す。

(b) 上で求めた $A$ の固有値 $\lambda_1, \lambda_2, \lambda_3$（$\lambda_1 \le \lambda_2 \le \lambda_3$）に対応する単位固有ベクトル $\vec{p}_1, \vec{p}_2, \vec{p}_3$ を並べて3行3列の行列 $P = (\vec{p}_1, \vec{p}_2, \vec{p}_3)$ を作る。$P$ による座標変換

$$
\vec{r} = P\vec{r}',\qquad \vec{r}' = \begin{pmatrix} x' \\ y' \\ z' \end{pmatrix} \qquad \text{(2)}
$$

を行った場合，$f(x, y, z)$ がどのような形に変換されるかを求めよ。また，$P$ によって変換されるベクトルはその大きさを変えないことを示せ。

(c) $P$ による変換をある軸のまわりの回転とみなした時，この回転軸の方向ベクトルを求めよ。

(d) $P^n = E$ となる最小の自然数 $n$ を求めよ。ただし $E$ は3次の単位行列である。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 一般教育科目 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
実対称行列の異なる固有値に属する固有ベクトルは互いに直交するため，規格化した固有ベクトルを並べた行列 $P$ は直交行列になります。直交変換は内積とベクトルの大きさを保ち，2次形式を固有値を係数とする平方和の標準形へ移します。

行列式が $+1$ の3次元直交行列 $P$ はある軸のまわりの回転を表すため，回転軸の方向ベクトルは固有値 $1$ の固有方程式 $P\vec{u} = \vec{u}$ から求まり，回転角 $\theta$ は対角和の公式 $\operatorname{Tr} P = 1 + 2\cos\theta$ から決まります。
</div>

### (a)

$f(x, y, z) = 2x^2 + 3y^2 + 4z^2 - \sqrt{6}xy + \sqrt{6}yz$ を対称行列 $A$ を用いて $\vec{r}^{\,T} A \vec{r}$ と表すと，$A$ は次の通りです。

$$
A = \begin{pmatrix}
2 & -\dfrac{\sqrt{6}}{2} & 0 \\[6pt]
-\dfrac{\sqrt{6}}{2} & 3 & \dfrac{\sqrt{6}}{2} \\[6pt]
0 & \dfrac{\sqrt{6}}{2} & 4
\end{pmatrix}
$$

固有方程式 $\det(A - \lambda E) = 0$ を計算します。

$$
\begin{aligned}
\det(A - \lambda E) &= \begin{vmatrix}
2 - \lambda & -\dfrac{\sqrt{6}}{2} & 0 \\[6pt]
-\dfrac{\sqrt{6}}{2} & 3 - \lambda & \dfrac{\sqrt{6}}{2} \\[6pt]
0 & \dfrac{\sqrt{6}}{2} & 4 - \lambda
\end{vmatrix} \\
&= (2 - \lambda)(3 - \lambda)(4 - \lambda) - \frac{3}{2}(4 - \lambda) - \frac{3}{2}(2 - \lambda) \\
&= (3 - \lambda)(2 - \lambda)(4 - \lambda) - 3(3 - \lambda) \\
&= (3 - \lambda)\bigl(\lambda^2 - 6\lambda + 8 - 3\bigr) \\
&= -( \lambda - 1)(\lambda - 3)(\lambda - 5)
\end{aligned}
$$

したがって固有値は小さい順に $\lambda_1 = 1$，$\lambda_2 = 3$，$\lambda_3 = 5$ です。

次に各固有値に対する第2成分が非負の単位固有ベクトルを求めます。

まず $\lambda_1 = 1$ のとき，$(A - E)\vec{v} = \vec{0}$ より次式が成り立ちます。

$$
\begin{aligned}
x - \frac{\sqrt{6}}{2}y &= 0 \\
\frac{\sqrt{6}}{2}y + 3z &= 0
\end{aligned}
$$

これより $x = \dfrac{\sqrt{6}}{2}y$，$z = -\dfrac{\sqrt{6}}{6}y$ です。$y = \sqrt{6}$ とおくと $(3, \sqrt{6}, -1)^T$ となり，大きさは $\sqrt{9 + 6 + 1} = 4$ なので，単位固有ベクトルは $\vec{p}_1 = \dfrac{1}{4}(3, \sqrt{6}, -1)^T$ です。

次に $\lambda_2 = 3$ のとき，$(A - 3E)\vec{v} = \vec{0}$ より次式が成り立ちます。

$$
\begin{aligned}
-x - \frac{\sqrt{6}}{2}y &= 0 \\
\frac{\sqrt{6}}{2}y + z &= 0
\end{aligned}
$$

これより $x = -\dfrac{\sqrt{6}}{2}y$，$z = -\dfrac{\sqrt{6}}{2}y$ です。$y = 2$ とおくと $(-\sqrt{6}, 2, -\sqrt{6})^T$ となり，大きさは $\sqrt{6 + 4 + 6} = 4$ なので，単位固有ベクトルは $\vec{p}_2 = \dfrac{1}{4}(-\sqrt{6}, 2, -\sqrt{6})^T$ です。

最後に $\lambda_3 = 5$ のとき，$(A - 5E)\vec{v} = \vec{0}$ より次式が成り立ちます。

$$
\begin{aligned}
-3x - \frac{\sqrt{6}}{2}y &= 0 \\
\frac{\sqrt{6}}{2}y - z &= 0
\end{aligned}
$$

これより $x = -\dfrac{\sqrt{6}}{6}y$，$z = \dfrac{\sqrt{6}}{2}y$ です。$y = \sqrt{6}$ とおくと $(-1, \sqrt{6}, 3)^T$ となり，大きさは $\sqrt{1 + 6 + 9} = 4$ なので，単位固有ベクトルは $\vec{p}_3 = \dfrac{1}{4}(-1, \sqrt{6}, 3)^T$ です。

$$
\finalanswer{\lambda_1 = 1,\ \vec{p}_1 = \frac{1}{4}\begin{pmatrix} 3 \\ \sqrt{6} \\ -1 \end{pmatrix},\qquad \lambda_2 = 3,\ \vec{p}_2 = \frac{1}{4}\begin{pmatrix} -\sqrt{6} \\ 2 \\ -\sqrt{6} \end{pmatrix},\qquad \lambda_3 = 5,\ \vec{p}_3 = \frac{1}{4}\begin{pmatrix} -1 \\ \sqrt{6} \\ 3 \end{pmatrix}}
$$

### (b)

行列 $P = (\vec{p}_1, \vec{p}_2, \vec{p}_3)$ の各列ベクトルは実対称行列 $A$ の相異なる固有値に属する単位固有ベクトルなので，互いに直交する正規直交基底をなします。すなわち $P^T P = E$ が成り立つ直交行列であり，$A P = (\lambda_1\vec{p}_1, \lambda_2\vec{p}_2, \lambda_3\vec{p}_3)$ より次式が得られます。

$$
P^T A P = \begin{pmatrix}
1 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 5
\end{pmatrix}
$$

座標変換 $\vec{r} = P\vec{r}'$ を2次形式 $f(x, y, z) = \vec{r}^{\,T} A \vec{r}$ に代入します。

$$
\begin{aligned}
f(x, y, z) &= (P\vec{r}')^T A (P\vec{r}') \\
&= \vec{r}'^{\,T} (P^T A P) \vec{r}' \\
&= x'^2 + 3y'^2 + 5z'^2
\end{aligned}
$$

次に $P$ によって変換されるベクトルの大きさが変わらないことを示します。任意のベクトル $\vec{r}' \in \mathbb{R}^3$ に対して $\vec{r} = P\vec{r}'$ の大きさの2乗を計算します。

$$
\begin{aligned}
|\vec{r}|^2 &= \vec{r}^{\,T}\vec{r} \\
&= (P\vec{r}')^T (P\vec{r}') \\
&= \vec{r}'^{\,T} (P^T P) \vec{r}' \\
&= \vec{r}'^{\,T}\vec{r}' \\
&= |\vec{r}'|^2
\end{aligned}
$$

$|\vec{r}| \ge 0$，$|\vec{r}'| \ge 0$ より $|\vec{r}| = |\vec{r}'|$ となり，$P$ による変換はベクトルの大きさを変えません。

$$
\finalanswer{f = x'^2 + 3y'^2 + 5z'^2}
$$

### (c)

行列 $P$ を成分で書きます。

$$
P = \frac{1}{4}\begin{pmatrix}
3 & -\sqrt{6} & -1 \\
\sqrt{6} & 2 & \sqrt{6} \\
-1 & -\sqrt{6} & 3
\end{pmatrix}
$$

念のため行列式を計算すると $\det P = 1$ であり，$P$ は確かに空間の回転を表します。

回転軸の方向ベクトル $\vec{u} = (u_x, u_y, u_z)^T \neq \vec{0}$ は回転によって不変なので，$P\vec{u} = \vec{u}$ すなわち $(P - E)\vec{u} = \vec{0}$ を満たします。

$$
\frac{1}{4}\begin{pmatrix}
-1 & -\sqrt{6} & -1 \\
\sqrt{6} & -2 & \sqrt{6} \\
-1 & -\sqrt{6} & -1
\end{pmatrix}
\begin{pmatrix} u_x \\ u_y \\ u_z \end{pmatrix}
= \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

第1行および第2行より次の連立方程式が得られます。

$$
\begin{aligned}
u_x + \sqrt{6}u_y + u_z &= 0 \\
\sqrt{6}(u_x + u_z) - 2u_y &= 0
\end{aligned}
$$

第1式より $u_x + u_z = -\sqrt{6}u_y$ を第2式に代入すると $-8u_y = 0$ となるため，$u_y = 0$ です。したがって $u_z = -u_x$ となり，回転軸の方向ベクトルは任意の実数 $k \neq 0$ に対して $k(1, 0, -1)^T$，大きさ $1$ に規格化すると $\pm\dfrac{1}{\sqrt{2}}(1, 0, -1)^T$ です。

$$
\finalanswer{\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}\quad \left(\pm\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}\right)}
$$

### (d)

3次元空間の回転行列 $P$ の回転角を $0 \le \theta \le \pi$ の範囲の $\theta$ とすると，回転軸を $z$ 軸にとった基底で $P$ は

$$
R(\theta) = \begin{pmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

と相似になります。行列の対角和は基底の取り方によらないため，次式が成り立ちます。

$$
\begin{aligned}
1 + 2\cos\theta &= \operatorname{Tr} P \\
&= \frac{3 + 2 + 3}{4} \\
&= 2
\end{aligned}
$$

これより $\cos\theta = \dfrac{1}{2}$ となり，回転角は $\theta = \dfrac{\pi}{3}$ です。

回転行列の $n$ 乗 $P^n$ は同じ軸のまわりの回転角 $n\theta = \dfrac{n\pi}{3}$ の回転を表します。したがって $P^n = E$ となるための必要十分条件は $\dfrac{n\pi}{3}$ が $2\pi$ の整数倍になること，すなわち $n$ が $6$ の倍数になることです。

よって $P^n = E$ を満たす最小の自然数は $n = 6$ です。

$$
\finalanswer{n = 6}
$$
