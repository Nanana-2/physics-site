---
title: 東大理物 平成25年度 数学 第1問：ファンデルモンド行列式と複素積分
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成25年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成25年度 数学 第1問：ファンデルモンド行列式と複素積分

## 問題

(1) $z_1, z_2, z_3, z_4$ を複素数とし，$\vec{z} = (z_1, z_2, z_3, z_4)$ とする。それを用いた行列式により $\Delta(\vec{z})$ を以下のように定義する。

$$
\Delta(\vec{z}) = \begin{vmatrix}
1 & 1 & 1 & 1 \\
z_1 & z_2 & z_3 & z_4 \\
(z_1)^2 & (z_2)^2 & (z_3)^2 & (z_4)^2 \\
(z_1)^3 & (z_2)^3 & (z_3)^3 & (z_4)^3
\end{vmatrix}
$$

$\Delta(\vec{z})$ が次の形に因数分解できることを以下の小問に従って示せ。

$$
\begin{aligned}
\Delta(\vec{z}) &= \prod_{1 \le i < j \le 4} (z_i - z_j) \\
&= (z_1 - z_2)(z_1 - z_3)(z_1 - z_4)(z_2 - z_3)(z_2 - z_4)(z_3 - z_4)
\end{aligned} \tag{1}
$$

(i) 式 (1) の両辺が $\vec{z}$ についての 6 次の同次（斉次）多項式であることを示せ。ここで，多変数関数に対し，$z_1^{a_1} z_2^{a_2} \cdots$ という項の次数は $a_1 + a_2 + \cdots$ であると定義する。また，同次とは，全ての項の次数が等しいことをいう。

(ii) $\Delta(\vec{z})$ は，互いに異なる $i$ と $j$ に対して $z_i$ が $z_j$ に一致するときゼロとなることを示せ。

(iii) これから，式 (1) の両辺が比例定数を除いて等しいことが示せる。これを用いて，係数を比較することにより比例定数が $1$ であることを示せ。

(2)

(i) 複素変数 $z$ の関数で，考えている領域で正則である $g(z)$ の表式

$$
\frac{1}{g(z)}\frac{\mathrm{d}g(z)}{\mathrm{d}z}, \qquad \frac{1}{g(z)}\frac{\mathrm{d}^2 g(z)}{\mathrm{d}z^2}
$$

を $\lambda(z) = \log(g(z))$ を用いてそれぞれ書き換えよ。

(ii) 設問 1 で定義された $\Delta(\vec{z})$ について，微分

$$
f(\vec{z}) = \frac{1}{\Delta(\vec{z})}\frac{\partial^2 \Delta(\vec{z})}{\partial z_1^2}
$$

を求めよ。また，$f(\vec{z})$ を $z_1$ の関数と見なしたとき，複素平面内で 2 次の極が無いことを示せ。ただし，ここおよび以下では $z_2, z_3, z_4$ は互いに異なるものとする。

(iii) 複素積分

$$
\oint_C \frac{\mathrm{d}z_1}{2\pi i}\,z_1 f(\vec{z})
$$

を求めよ。ここで積分経路 $C$ は内部に $z_2, z_3, z_4$ を含む円を反時計回りに一周する経路であり，$i$ は虚数単位である。

> 出典：東京大学大学院理学系研究科物理学専攻 平成25年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
行列式の各項はどれも $6$ 次で，2つの変数が等しいと2つの列が等しくなるので，行列式は $0$ になります。そのため，因数定理から $z_i - z_j$ がすべて因数になり，次数を比べると，行列式は差積の定数倍になります。

後半では，$\lambda = \log\Delta$ とおくと，積が和になり，微分を計算しやすくなります。複素積分は，積分経路の中にある極での留数の和として求めます。
</div>

### (1)(i)
式 (1) の左辺 $\Delta(\vec{z})$ を行列式の定義に従って展開します。$4$ 次の置換全体の集合を $S_4$ とすると，次式になります。

$$
\Delta(\vec{z}) = \sum_{\sigma \in S_4} \operatorname{sgn}(\sigma)\, 1 \cdot z_{\sigma(2)} \cdot z_{\sigma(3)}^2 \cdot z_{\sigma(4)}^3
$$

各置換 $\sigma$ に対応する項 $z_{\sigma(2)}^1 z_{\sigma(3)}^2 z_{\sigma(4)}^3$ の次数は，すべて

$$
0 + 1 + 2 + 3 = 6
$$

です。したがって左辺は $\vec{z}$ についての6次の同次多項式です。

一方，右辺は $(z_i - z_j)$ の形の1次の同次多項式を $6$ 個掛け合わせた積なので，展開したすべての項の次数は $1 + 1 + 1 + 1 + 1 + 1 = 6$ です。したがって右辺も6次の同次多項式です。

### (1)(ii)
互いに異なる $i, j$ に対して $z_i = z_j$ のとき，$\Delta(\vec{z})$ を定義する行列の第 $i$ 列と第 $j$ 列はすべての成分が一致します。行列式は2つの列が一致すると $0$ になるので，$\Delta(\vec{z}) = 0$ が成り立ちます。

### (1)(iii)
式 (1) の両辺が比例定数 $c$ を除いて等しいので，

$$
\Delta(\vec{z}) = c(z_1 - z_2)(z_1 - z_3)(z_1 - z_4)(z_2 - z_3)(z_2 - z_4)(z_3 - z_4)
$$

とおきます。両辺の $z_2 z_3^2 z_4^3$ の係数を比べます。

左辺 $\Delta(\vec{z})$ の展開で $z_2 z_3^2 z_4^3$ が現れるのは単位置換に対応する対角成分の積 $1 \cdot z_2 \cdot z_3^2 \cdot z_4^3$ のみなので，その係数は $1$ です。

右辺の積から $z_2 z_3^2 z_4^3$ を作るには，6つの因子 $(z_i - z_j)$ のすべてから $-z_j$ を選ぶ以外にありません。

$$
\begin{aligned}
(-z_2)(-z_3)(-z_4)(-z_3)(-z_4)(-z_4) &= (-1)^6 z_2 z_3^2 z_4^3 \\
&= z_2 z_3^2 z_4^3
\end{aligned}
$$

したがって右辺の $z_2 z_3^2 z_4^3$ の係数は $c$ です。両辺の係数を比べると $c = 1$ となります。

### (2)(i)
$g(z)\ne0$ となる点の近傍で正則な対数の枝を選び，$\lambda(z)=\log g(z)$ とします。領域全体で同じ枝を選ぶ必要はありません。この近傍で $z$ 微分すると，

$$
\frac{\mathrm{d}\lambda}{\mathrm{d}z} = \frac{1}{g(z)}\frac{\mathrm{d}g(z)}{\mathrm{d}z}
$$

両辺をさらに $z$ で微分します。

$$
\begin{aligned}
\frac{\mathrm{d}^2\lambda}{\mathrm{d}z^2} &= -\frac{1}{g(z)^2}\left(\frac{\mathrm{d}g(z)}{\mathrm{d}z}\right)^2 + \frac{1}{g(z)}\frac{\mathrm{d}^2 g(z)}{\mathrm{d}z^2} \\
&= -\left(\frac{\mathrm{d}\lambda}{\mathrm{d}z}\right)^2 + \frac{1}{g(z)}\frac{\mathrm{d}^2 g(z)}{\mathrm{d}z^2}
\end{aligned}
$$

これを $\dfrac{1}{g(z)}\dfrac{\mathrm{d}^2 g(z)}{\mathrm{d}z^2}$ について整理すると，次式が得られます。

$$
\finalanswer{\frac{1}{g(z)}\frac{\mathrm{d}g(z)}{\mathrm{d}z} = \frac{\mathrm{d}\lambda}{\mathrm{d}z}, \qquad \frac{1}{g(z)}\frac{\mathrm{d}^2 g(z)}{\mathrm{d}z^2} = \frac{\mathrm{d}^2\lambda}{\mathrm{d}z^2} + \left(\frac{\mathrm{d}\lambda}{\mathrm{d}z}\right)^2}
$$

### (2)(ii)
式 (1) の対数をとり，$\lambda(\vec{z}) = \log(\Delta(\vec{z}))$ を $z_1$ で1回および2回偏微分します。$z_1$ を含む因子は $(z_1 - z_2)(z_1 - z_3)(z_1 - z_4)$ だけなので，次のようになります。

$$
\begin{aligned}
\frac{\partial\lambda}{\partial z_1} &= \sum_{j=2}^4 \frac{1}{z_1 - z_j} \\
\frac{\partial^2\lambda}{\partial z_1^2} &= -\sum_{j=2}^4 \frac{1}{(z_1 - z_j)^2}
\end{aligned}
$$

設問 (2)(i) の結果にこれらを代入して $f(\vec{z})$ を計算します。

$$
\begin{aligned}
f(\vec{z}) &= \frac{\partial^2\lambda}{\partial z_1^2} + \left(\frac{\partial\lambda}{\partial z_1}\right)^2 \\
&= -\sum_{j=2}^4 \frac{1}{(z_1 - z_j)^2} + \left(\sum_{j=2}^4 \frac{1}{z_1 - z_j}\right)^2 \\
&= -\sum_{j=2}^4 \frac{1}{(z_1 - z_j)^2} + \sum_{j=2}^4 \frac{1}{(z_1 - z_j)^2} + \sum_{\substack{2 \le j, k \le 4 \\ j \neq k}} \frac{1}{(z_1 - z_j)(z_1 - z_k)} \\
&= 2\left(\frac{1}{(z_1 - z_2)(z_1 - z_3)} + \frac{1}{(z_1 - z_2)(z_1 - z_4)} + \frac{1}{(z_1 - z_3)(z_1 - z_4)}\right)
\end{aligned}
$$

$\dfrac1{(z_1-z_j)^2}$ の項はすべて打ち消し合っています。$z_2,z_3,z_4$ は互いに異なるので，特異点が生じる候補は $z_1=z_2,z_3,z_4$ だけで，極があれば高々1次です。留数が0になる候補は可除特異点なので，必ず3個の極があるわけではありません。いずれの場合も2次の極はありません。

$$
\finalanswer{f(\vec{z}) = 2\left(\frac{1}{(z_1 - z_2)(z_1 - z_3)} + \frac{1}{(z_1 - z_2)(z_1 - z_4)} + \frac{1}{(z_1 - z_3)(z_1 - z_4)}\right)}
$$

### (2)(iii)
被積分関数 $z_1f(\vec z)$ の $C$ 内の特異点の候補は $z_1=z_2,z_3,z_4$ です。それぞれの点で留数を計算します。可除特異点の場合，その点の留数は0です。

$$
\begin{aligned}
\operatorname{Res}_{z_1 = z_2}\bigl(z_1 f(\vec{z})\bigr) &= 2 z_2\left(\frac{1}{z_2 - z_3} + \frac{1}{z_2 - z_4}\right) \\
\operatorname{Res}_{z_1 = z_3}\bigl(z_1 f(\vec{z})\bigr) &= 2 z_3\left(\frac{1}{z_3 - z_2} + \frac{1}{z_3 - z_4}\right) \\
\operatorname{Res}_{z_1 = z_4}\bigl(z_1 f(\vec{z})\bigr) &= 2 z_4\left(\frac{1}{z_4 - z_2} + \frac{1}{z_4 - z_3}\right)
\end{aligned}
$$

留数定理を用いて3つの留数の和を計算し，同じ分母の組ごとにまとめます。

$$
\begin{aligned}
\oint_C \frac{\mathrm{d}z_1}{2\pi i}\,z_1 f(\vec{z}) &= \sum_{j=2}^4 \operatorname{Res}_{z_1 = z_j}\bigl(z_1 f(\vec{z})\bigr) \\
&= 2\left(\frac{z_2 - z_3}{z_2 - z_3} + \frac{z_2 - z_4}{z_2 - z_4} + \frac{z_3 - z_4}{z_3 - z_4}\right) \\
&= 2(1 + 1 + 1) \\
&= 6
\end{aligned}
$$

$$
\finalanswer{\oint_C\frac{\mathrm{d}z_1}{2\pi i}\,z_1f(\vec z)=6}
$$
