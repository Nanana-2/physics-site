---
title: 東大理物 令和2年度 数学 第2問：一般化パウリ行列と同時対角化・相互不偏基底
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 令和2年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 令和2年度 数学 第2問：一般化パウリ行列と同時対角化・相互不偏基底

## 問題

$d$ を $d \ge 2$ の自然数とし，$d \times d$ 行列 $X, Z$ を次のように定義する。

$$
X = \begin{pmatrix}
0 & 0 & 0 & \cdots & 1 \\
1 & 0 & 0 & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & 1 & 0
\end{pmatrix},\qquad
Z = \begin{pmatrix}
1 & 0 & 0 & \cdots & 0 \\
0 & w & 0 & \cdots & 0 \\
0 & 0 & w^2 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0 & w^{d-1}
\end{pmatrix}
$$

ここで，$w = e^{i\frac{2\pi}{d}}$ である。ただし，$i$ を虚数単位とする。すなわち，$X$ は，その $j$ 行 $j - 1$ 列成分が $X_{j, j-1} = 1\ (j = 2, 3, \dots, d)$ および $1$ 行 $d$ 列成分が $X_{1, d} = 1$ で与えられ，これら以外の行列成分がすべて $0$ の行列である。また，$Z$ はその対角成分が $Z_{j, j} = w^{j-1}\ (j = 1, 2, \dots, d)$ で与えられ，非対角成分がすべて $0$ の行列である。

さらに，$n, m = 0, 1, \dots, d - 1$ について，次の行列

$$
U^{(n, m)} = X^n Z^m = \underbrace{X \cdots X}_{n}\underbrace{Z \cdots Z}_{m}
$$

を定義する（$X$ を $n$ 個，$Z$ を $m$ 個掛けた積とする）。

また，複素 $d$ 次元空間の二つの複素列ベクトル $u = \begin{pmatrix} u_1 \\ \vdots \\ u_d \end{pmatrix}$ と $v = \begin{pmatrix} v_1 \\ \vdots \\ v_d \end{pmatrix}$ の内積 $\langle u, v \rangle$ は，$\langle u, v \rangle = \displaystyle\sum_{i=1}^{d} u_i^* v_i$ で与えられる。ただし，$*$ は複素共役を表す。

以下の設問に答えよ。解答を導く計算過程も解答用紙に記述すること。

(1) $Z$ のトレースが $0$ となることを示せ。

(2) $XZ$ と $ZX$ の間には，$c$ を複素数として，$ZX = cXZ$ の関係が成り立つ。このときの $c$ の値を求めよ。

(3) $U^{(1, m)} = XZ^m$ と同時対角化可能な行列 $U^{(n', m')}$ の $n', m'$ が満たすべき条件を求めよ。

(4) $U^{(1, m)}$ の固有値をすべて求めよ。

以下の設問では，$d = 3$ の場合について考える。

(5) $U^{(1, m)}$ の正規化した固有列ベクトルを $e_j^{(m)}\ (j = 1, 2, 3)$ とする。$e_j^{(m)}$ を求めよ。

(6) 任意の $m, m' = 0, 1, 2$（ただし $m' \neq m$）と任意の $j, j' = 1, 2, 3$ に対して $\left|\langle e_j^{(m)}, e_{j'}^{(m')} \rangle\right|^2 = \dfrac{1}{3}$ が成り立つことを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 令和2年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
巡回シフト行列 $X$ とクロック行列 $Z$ はいずれもユニタリ行列であり，$ZX = wXZ$ というワイル交換関係だけで積の交換則や $d$ 乗の値がすべて決まります。ユニタリ行列は正規行列なので，同時対角化可能性は可換条件と同値であり，指数に関する合同式へ整理されます。

また $Z$ による相似変換 $Z U^{(1,m)} Z^{-1} = w U^{(1,m)}$ から固有値が $1$ の $d$ 乗根の回転として縮退なく並び，特に $d = 3$ では異なる $m$ に対応する固有基底どうしが互いに均一な重なり $\dfrac{1}{3}$ をもつ相互不偏基底を構成します。
</div>

### (1)
$Z$ のトレースは対角成分の和です。$d \ge 2$ より $w = e^{2\pi i/d} \neq 1$ かつ $w^d = e^{2\pi i} = 1$ なので，等比数列の和の公式から次式が成り立ちます。

$$
\operatorname{Tr}(Z) = \sum_{j=1}^{d} w^{j-1} = \frac{1 - w^d}{1 - w} = 0
$$

よって $Z$ のトレースは $0$ です。

### (2)
複素 $d$ 次元空間の標準基底ベクトルを $b_1, b_2, \dots, b_d$ とします（$b_{d+1} \equiv b_1$ と約束します）。定義より各基底に対する $X, Z$ の作用は次のとおりです。

$$
X b_j = b_{j+1},\qquad Z b_j = w^{j-1} b_j \qquad (j = 1, 2, \dots, d)
$$

これらを順に作用させます。$j = 1, 2, \dots, d - 1$ に対しては

$$
\begin{aligned}
ZX b_j &= Z b_{j+1} = w^j b_{j+1} \\
XZ b_j &= X(w^{j-1} b_j) = w^{j-1} b_{j+1}
\end{aligned}
$$

となり，$j = d$ に対しても $w^d = 1$ より

$$
\begin{aligned}
ZX b_d &= Z b_1 = 1\cdot b_1 = w^d b_1 \\
XZ b_d &= X(w^{d-1} b_d) = w^{d-1} b_1
\end{aligned}
$$

となります。よってすべての基底 $b_j\ (j = 1, \dots, d)$ に対して $ZX b_j = w XZ b_j$ が成り立つため，$ZX = w XZ$ です。したがって，

$$
\finalanswer{c = w = e^{i\frac{2\pi}{d}}}
$$

### (3)
$X$ は置換行列，$Z$ は絶対値 $1$ の対角行列なので，ともにユニタリ行列（$X^\dagger X = I,\ Z^\dagger Z = I$）です。したがってその積 $U^{(n, m)} = X^n Z^m$ もすべてユニタリ行列であり，正規行列としてそれぞれ単独でユニタリ対角化可能です。

2つの対角化可能な行列（特に正規行列）が同時対角化可能であることと，それらが可換であることは同値です。問2の関係 $ZX = w XZ$ を繰り返し用いると，任意の非負整数 $a, b$ に対して $Z^a X^b = w^{ab} X^b Z^a$ が成り立ちます。これを用いて $U^{(1, m)}$ と $U^{(n', m')}$ の積を2通りの順序で計算します。

$$
\begin{aligned}
U^{(1, m)} U^{(n', m')}
&= X Z^m X^{n'} Z^{m'} = w^{m n'} X^{n' + 1} Z^{m + m'} \\
U^{(n', m')} U^{(1, m)}
&= X^{n'} Z^{m'} X Z^m = w^{m'} X^{n' + 1} Z^{m + m'}
\end{aligned}
$$

$X^{n'+1} Z^{m+m'}$ は正則（ユニタリ）行列なので，両者が等しくなるための必要十分条件は $w^{m n'} = w^{m'}$，すなわち $w^{m' - m n'} = 1$ です。$w = e^{2\pi i/d}$ は原始 $d$ 乗根なので，これは $m' - m n'$ が $d$ の倍数であることと同値です。したがって，

$$
\finalanswer{m' \equiv m n' \pmod{d} \qquad (n', m' \in \{0, 1, \dots, d - 1\})}
$$

（すなわち $n' \in \{0, 1, \dots, d - 1\}$ に対して $m'$ が $m n'$ を $d$ で割った余りに等しいことが条件です。）

### (4)
まず $(U^{(1, m)})^d = (X Z^m)^d$ を計算します。関係 $Z^m X^k = w^{mk} X^k Z^m$ を用いて $X$ をすべて左側へ集めると，左から $k$ 番目の $Z^m\ (k = 1, 2, \dots, d - 1)$ はその後ろにある $d - k$ 個の $X$ を飛び越えるため，$w^{m(d - k)}$ の因子を生じます。

$$
\begin{aligned}
(X Z^m)^d
&= \left(\prod_{k=1}^{d-1} w^{m(d - k)}\right) X^d Z^{md} \\
&= w^{m\frac{d(d-1)}{2}} I
\end{aligned}
$$

ここで $X^d = I$ および $Z^d = I$ を用いました。さらに $w^{d/2} = e^{i\pi} = -1$ なので，

$$
(U^{(1, m)})^d = (-1)^{m(d - 1)} I
$$

となります。よって $U^{(1, m)}$ の任意の固有値 $\lambda$ は $\lambda^d = (-1)^{m(d - 1)}$ を満たします。

一方，問2より $Z U^{(1, m)} Z^{-1} = Z X Z^{m - 1} = w X Z^m = w U^{(1, m)}$ が成り立ちます。したがって $\lambda$ が $U^{(1, m)}$ の固有値であれば（固有ベクトルを $v$ とすると $U^{(1, m)}(Z^{-1} v) = w\lambda (Z^{-1} v)$ となるため），$w\lambda,\ w^2\lambda,\ \dots,\ w^{d-1}\lambda$ もすべて $U^{(1, m)}$ の固有値です。これらは相異なる $d$ 個の複素数であるため，$\lambda^d = (-1)^{m(d - 1)}$ の $d$ 個の解がすべて重複度 $1$ の固有値として現れます。

- $m(d - 1)$ が偶数のとき（$d$ が奇数，または $d$ が偶数かつ $m$ が偶数）：$\lambda^d = 1$ の解より $\lambda_j = w^{j - 1} = e^{2\pi i(j - 1)/d}$（$j = 1, 2, \dots, d$）。
- $m(d - 1)$ が奇数のとき（$d$ が偶数かつ $m$ が奇数）：$\lambda^d = -1$ の解より $\lambda_j = e^{\pi i/d} w^{j - 1} = e^{\pi i(2j - 1)/d}$（$j = 1, 2, \dots, d$）。

これらは1つの式でまとめて表すことができます。したがって，

$$
\finalanswer{\lambda_j = \exp\left[i\frac{\pi}{d}\bigl(2(j - 1) + m(d - 1)\bigr)\right] \qquad (j = 1, 2, \dots, d)}
$$

### (5)
$d = 3$ のとき $d - 1 = 2$ は偶数なので，問4よりすべての $m = 0, 1, 2$ に対して $U^{(1, m)} = X Z^m$ の固有値は $\lambda_j = w^{j - 1}$（$j = 1, 2, 3$，$w = e^{2\pi i/3}$）です。

行列 $U^{(1, m)} = X Z^m$ を具体的に書き下すと，

$$
U^{(1, m)} = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 & 0 \\ 0 & w^m & 0 \\ 0 & 0 & w^{2m} \end{pmatrix} = \begin{pmatrix} 0 & 0 & w^{2m} \\ 1 & 0 & 0 \\ 0 & w^m & 0 \end{pmatrix}
$$

となります。固有ベクトルを $v = (v_1, v_2, v_3)^\top$ とおき，固有方程式 $U^{(1, m)} v = w^{j - 1} v$ を成分ごとに書きます。

$$
w^{2m} v_3 = w^{j - 1} v_1,\qquad v_1 = w^{j - 1} v_2,\qquad w^m v_2 = w^{j - 1} v_3
$$

第2式より $v_2 = w^{-(j - 1)} v_1$，第3式より $v_3 = w^{m - 2(j - 1)} v_1 = w^{m + j - 1} v_1$ です（$w^3 = 1$ を用いました）。これを第1式に代入すると $w^{2m} v_3 = w^{3m + j - 1} v_1 = w^{j - 1} v_1$ となり一致します。

$|v_1|^2 + |v_2|^2 + |v_3|^2 = 3|v_1|^2 = 1$ より，全体の位相因子を除いて $v_1 = \dfrac{1}{\sqrt{3}}$ と選ぶと，正規化された固有列ベクトル $e_j^{(m)}$ が決まります。したがって，

$$
\finalanswer{e_j^{(m)} = \frac{1}{\sqrt{3}}\begin{pmatrix} 1 \\ w^{-(j - 1)} \\ w^{m + j - 1} \end{pmatrix} \qquad (j = 1, 2, 3;\ m = 0, 1, 2)}
$$

（全体の位相因子 $e^{i\phi}$ の任意性があります。）

### (6)
問5の結果と $w^* = w^{-1}$ を用いて，内積 $\langle e_j^{(m)}, e_{j'}^{(m')} \rangle$ を計算します。

$$
\begin{aligned}
\langle e_j^{(m)}, e_{j'}^{(m')} \rangle
&= \frac{1}{3}\left(1 + w^{j - 1} w^{-(j' - 1)} + w^{-(m + j - 1)} w^{m' + j' - 1}\right) \\
&= \frac{1}{3}\left(1 + w^{j - j'} + w^{(m' - m) - (j - j')}\right)
\end{aligned}
$$

ここで $a = j - j'$，$b = (m' - m) - (j - j')$，$\Delta m = m' - m$ とおきます。仮定 $m \neq m'$（$m, m' \in \{0, 1, 2\}$）より $\Delta m \not\equiv 0 \pmod{3}$ です。$\Delta j = j - j'$ の $3$ を法とする余りに応じて次の3通りに分かれます。

- $\Delta j \equiv 0 \pmod{3}$ のとき：$a \equiv 0,\ b \equiv \Delta m$ より $1 + w^a + w^b = 2 + w^{\Delta m}$。
- $\Delta j \equiv \Delta m \pmod{3}$ のとき：$a \equiv \Delta m,\ b \equiv 0$ より $1 + w^a + w^b = 2 + w^{\Delta m}$。
- $\Delta j \equiv -\Delta m \pmod{3}$ のとき：$a \equiv -\Delta m,\ b \equiv 2\Delta m \equiv -\Delta m$ より $1 + w^a + w^b = 1 + 2w^{-\Delta m}$。

$\Delta m \equiv \pm 1 \pmod{3}$ のいずれに対しても $w^{\pm 1} = -\dfrac{1}{2} \pm i\dfrac{\sqrt{3}}{2}$ なので，

$$
\begin{aligned}
\left|2 + w^{\pm 1}\right|^2 &= \left(\frac{3}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{9}{4} + \frac{3}{4} = 3 \\
\left|1 + 2w^{\pm 1}\right|^2 &= 0^2 + \left(\sqrt{3}\right)^2 = 3
\end{aligned}
$$

となり，すべての場合で $\left|1 + w^a + w^b\right|^2 = 3$ が成り立ちます。したがって，任意の $m \neq m'$ と任意の $j, j' = 1, 2, 3$ に対して，

$$
\left|\langle e_j^{(m)}, e_{j'}^{(m')} \rangle\right|^2 = \frac{3}{9} = \frac{1}{3}
$$

が成り立ちます。

<aside class="rigor-note" markdown>
行列 $X, Z$ は $d$ 次元の一般化パウリ行列（ワイル・ハイゼンベルク群の生成元）であり，$d = 2$ では通常のパウリ行列 $\sigma_x, \sigma_z$ に一致します。問6で示したように，異なる正規直交基底の任意のベクトルどうしの内積の絶対値2乗がすべて $\dfrac{1}{d}$ になる基底の組を相互不偏基底（mutually unbiased bases, MUB）と呼び，量子情報理論における量子状態トモグラフィや量子鍵配送で重要な役割を果たします。$d = 3$ では標準基底（$Z$ の固有基底）と $U^{(1,0)}, U^{(1,1)}, U^{(1,2)}$ の固有基底の計 $d + 1 = 4$ 組が最大の相互不偏基底をなします。
</aside>
