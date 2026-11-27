---
title: 東大理物 平成19年度 数学 第1問：回転行列の指数関数・対角化とファンデルモンド行列式
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成19年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成19年度 数学 第1問：回転行列の指数関数・対角化とファンデルモンド行列式

## 問題

正方行列 $A$ に対して，$U^{-1}AU$ が対角行列になるようなユニタリ行列 $U$ が存在するためには，$A$ が正規行列であることが必要十分である。正規行列とは，$A^* A = A A^*$ を満たす行列であり，$A^*$ は行列 $A$ を転置し複素共役をとった行列である。実ユニタリ行列を直交行列と呼ぶ。以下の設問に答えよ。

(1) 行列

$$
B = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
$$

は直交行列であることを示せ。ここで，$\theta$ は実数。

(2) 任意の正方行列 $A$ について，

$$
\exp A \equiv \sum_{m=0}^{\infty} \frac{A^m}{m!}
$$

は収束し，$\exp A$ を定義することができる。ただし，$A^0$ は単位行列とする。$A = \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$ のとき，

$$
\exp A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = B
$$

を示せ。

(3) 行列 $B$ を対角化せよ。

次に，一般の次元をもつ行列の例として，変数の組 $\{x_1, \dots, x_n\}$ について

$$
C = \begin{pmatrix}
1 & 1 & \dots & 1 \\
x_1 & x_2 & \dots & x_n \\
\vdots & \vdots & \vdots & \vdots \\
x_1^{n-1} & x_2^{n-1} & \dots & x_n^{n-1}
\end{pmatrix}
$$

を考えよう。

(4) $|C| \propto \prod_{i<j}(x_j - x_i)$ を示せ。ここで $|C|$ は行列 $C$ の行列式。

(5) この結果を用いて，上記の行列 $C$ が正則である（逆行列をもつ）のはどのような場合かを述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成19年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2次元回転行列 $B$ の生成子 $A$ は，2乗すると単位行列の負の定数倍になります。そのためべき級数 $\exp A$ は偶数次と奇数次に分かれ，三角関数のマクローリン展開から直接 $B$ にまとまります。また直交行列は正規行列なので，複素数の範囲でユニタリ行列によって対角化することができます。

後半の行列 $C$ の行列式は各変数 $x_1, \dots, x_n$ についての多項式であり，2つの変数が一致すると同じ列が現れて $0$ になります。この性質と行基本変形による次数下げを用いると，行列式を差積の形で表すことができます。
</div>

### (1)

$\theta$ は実数なので，$B$ の成分はすべて実数です。よって 

$$
\begin{aligned}
B^* &= {}^t B \\
&= \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}
\end{aligned}
$$

となります。積 $B^* B$ と $B B^*$ を計算します。

$$
\begin{aligned}
B^* B &= \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \\
&= \begin{pmatrix} \cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta \\ -\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{pmatrix} \\
&= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\end{aligned}
$$

$$
\begin{aligned}
B B^* &= \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \\
&= \begin{pmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta \\ \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{pmatrix} \\
&= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\end{aligned}
$$

$B$ は実行列であり，$B^* B=I$，$B B^*=I$ を満たすため，実ユニタリ行列すなわち直交行列です。

### (2)

$J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ とおくと $A = \theta J$ です。$J$ のべき乗を計算します。

$$
\begin{aligned}
J^2 &= \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \\
&= \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} \\
&= -I \\
J^3 &= -J \\
J^4 &= I
\end{aligned}
$$

これより，非負整数 $k$ に対して $A^{2k} = (-1)^k \theta^{2k} I$，$A^{2k+1} = (-1)^k \theta^{2k+1} J$ が成り立ちます。$\exp A$ の和を偶数項 $m = 2k$ と奇数項 $m = 2k + 1$ に分けます。

$$
\begin{aligned}
\exp A &= \sum_{k=0}^{\infty} \frac{A^{2k}}{(2k)!} + \sum_{k=0}^{\infty} \frac{A^{2k+1}}{(2k + 1)!} \\
&= \left(\sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k}}{(2k)!}\right)I + \left(\sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k+1}}{(2k + 1)!}\right)J \\
&= (\cos\theta)I + (\sin\theta)J \\
&= \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \\
&= B
\end{aligned}
$$

### (3)

$B$ は直交行列なので正規行列であり，ユニタリ行列 $U$ によって対角化することができます。まず固有方程式を解きます。

$$
\begin{aligned}
\det(B - \lambda I) &= 0 \\
(\cos\theta - \lambda)^2 + \sin^2\theta &= 0 \\
\lambda^2 - 2\lambda\cos\theta + 1 &= 0
\end{aligned}
$$

2次方程式を解くと，固有値は次のとおりです。

$$
\begin{aligned}
\lambda &= \cos\theta \pm i\sin\theta \\
&= e^{\pm i\theta}
\end{aligned}
$$

固有値 $\lambda_1 = e^{i\theta}$ に対する固有ベクトル $\boldsymbol{u}_1 = \begin{pmatrix} x \\ y \end{pmatrix}$ を求めます。$(B - e^{i\theta}I)\boldsymbol{u}_1 = \boldsymbol{0}$ の1行目を書き出します。

$$
\begin{aligned}
(\cos\theta - e^{i\theta})x - \sin\theta\,y &= 0 \\
-i\sin\theta\,x - \sin\theta\,y &= 0
\end{aligned}
$$

これより $y = -ix$ を選ぶことができます。規格化すると $\boldsymbol{u}_1 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix}$ です。このベクトルは $\sin\theta = 0$ の場合にも固有ベクトルになります。

同様に固有値 $\lambda_2 = e^{-i\theta}$ に対する固有ベクトル $\boldsymbol{u}_2 = \begin{pmatrix} x \\ y \end{pmatrix}$ は，1行目が $i\sin\theta\,x - \sin\theta\,y = 0$ となるため $y = ix$ を選ぶことができます。規格化すると $\boldsymbol{u}_2 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix}$ です。

$\boldsymbol{u}_1$ と $\boldsymbol{u}_2$ は互いに直交するので，これらを並べた行列

$$
U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix}
$$

はユニタリ行列であり，

$$
\begin{aligned}
U^{-1} &= U^* \\
&= \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix}
\end{aligned}
$$

です。実際に $U^{-1}BU$ を計算します。

$$
\begin{aligned}
U^{-1}BU &= \frac{1}{2}\begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix}\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix} \\
&= \frac{1}{2}\begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix}\begin{pmatrix} e^{i\theta} & e^{-i\theta} \\ -ie^{i\theta} & ie^{-i\theta} \end{pmatrix} \\
&= \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{pmatrix}
\end{aligned}
$$

したがって，ユニタリ行列 $U$ により次のように対角化されます。

$$
\finalanswer{U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix}, \qquad U^{-1}BU = \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{pmatrix}}
$$

### (4)

$n$ 次の行列 $C$ の行列式を $D_n(x_1, \dots, x_n) = |C|$ とおき，数学的帰納法によって $\displaystyle D_n(x_1, \dots, x_n) = \prod_{1 \le i < j \le n}(x_j - x_i)$ が成り立つことを示します。

$n=1$ なら $C=(1)$ で行列式は $1$ です。空積を $1$ とする約束により，差積の式も成り立ちます。$n=2$ の場合は，次のように直接計算します。

$$
\begin{aligned}
D_2(x_1, x_2) &= \begin{vmatrix} 1 & 1 \\ x_1 & x_2 \end{vmatrix} \\
&= x_2 - x_1
\end{aligned}
$$

次に $n - 1$ 次で成り立つと仮定し，$n$ 次の行列式 $D_n$ を変形します。下の行から順に，第 $k$ 行（$k = n, n - 1, \dots, 2$）から第 $k - 1$ 行の $x_1$ 倍を引きます。この行基本変形で行列式の値は変わりません。第 $k$ 行の第 $j$ 成分は $x_j^{k-1} - x_1 x_j^{k-2} = (x_j - x_1)x_j^{k-2}$ となります。

$$
\begin{aligned}
D_n(x_1, \dots, x_n) &= \begin{vmatrix}
1 & 1 & \dots & 1 \\
0 & x_2 - x_1 & \dots & x_n - x_1 \\
0 & x_2(x_2 - x_1) & \dots & x_n(x_n - x_1) \\
\vdots & \vdots & \ddots & \vdots \\
0 & x_2^{n-2}(x_2 - x_1) & \dots & x_n^{n-2}(x_n - x_1)
\end{vmatrix}
\end{aligned}
$$

第1列について余因子展開し，さらに各列から共通因子 $(x_2 - x_1), \dots, (x_n - x_1)$ をくくり出します。

$$
\begin{aligned}
D_n(x_1, \dots, x_n) &= \begin{vmatrix}
x_2 - x_1 & \dots & x_n - x_1 \\
x_2(x_2 - x_1) & \dots & x_n(x_n - x_1) \\
\vdots & \ddots & \vdots \\
x_2^{n-2}(x_2 - x_1) & \dots & x_n^{n-2}(x_n - x_1)
\end{vmatrix} \\
&= (x_2 - x_1)\cdots(x_n - x_1)\begin{vmatrix}
1 & \dots & 1 \\
x_2 & \dots & x_n \\
\vdots & \ddots & \vdots \\
x_2^{n-2} & \dots & x_n^{n-2}
\end{vmatrix} \\
&= \left(\prod_{j=2}^{n}(x_j - x_1)\right) D_{n-1}(x_2, \dots, x_n)
\end{aligned}
$$

帰納法の仮定 $\displaystyle D_{n-1}(x_2, \dots, x_n) = \prod_{2 \le i < j \le n}(x_j - x_i)$ を代入すると，次式が得られます。

$$
\begin{aligned}
D_n(x_1, \dots, x_n) &= \left(\prod_{j=2}^{n}(x_j - x_1)\right)\left(\prod_{2 \le i < j \le n}(x_j - x_i)\right) \\
&= \prod_{1 \le i < j \le n}(x_j - x_i)
\end{aligned}
$$

以上より，任意の $n \ge 2$ に対して $\displaystyle |C| = \prod_{i < j}(x_j - x_i)$ となり，特に $\displaystyle |C| \propto \prod_{i < j}(x_j - x_i)$ が成り立ちます。

### (5)

正方行列 $C$ が正則であるための必要十分条件は $|C| \neq 0$ です。設問4より $\displaystyle |C| = \prod_{i < j}(x_j - x_i)$ なので，$|C| \neq 0$ であることは，すべての組 $i < j$ に対して $x_j - x_i \neq 0$ となることと同値です。

$x_1,\dots,x_n$ がすべて互いに異なる場合に限り，行列 $C$ は正則です。

$$
\finalanswer{x_i\ne x_j\quad(i\ne j)}
$$