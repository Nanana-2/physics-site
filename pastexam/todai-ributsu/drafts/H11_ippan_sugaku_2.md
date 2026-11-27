---
title: 東大理物 平成11年度 一般教育科目 数学 第2問：3次実行列の固有多項式と複素固有値条件
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 一般教育科目 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成11年度 一般教育科目 数学 第2問：3次実行列の固有多項式と複素固有値条件

## 問題

3行3列の実行列 $A = \{a_{ij}\}$ が与えられているとき，行列式 $\det[A - \lambda I]$ はパラメータ $\lambda$ について3次の多項式となる。ただし，$I$ は単位行列である。上の行列式を次のように書くことにする：

$$
F(\lambda) \equiv \det[A - \lambda I] = -\lambda^3 + P\lambda^2 + Q\lambda + R
$$

このとき以下の設問に答えよ。
{: .problem-lead }

(1) 上の3次式の係数 $P, Q, R$ は次のように表せることを示せ。

$$
\begin{aligned}
P &= \operatorname{Tr} A \\
Q &= \frac{1}{2}\bigl(\operatorname{Tr} A^2 - (\operatorname{Tr} A)^2\bigr) \\
R &= \det A
\end{aligned}
$$

ここで，$\operatorname{Tr}$ は行列の対角和を意味する。

(2) 特に $P = 0$ のとき，行列 $A = \{a_{ij}\}$ が複素共役の固有値をもつための条件を $Q, R$ を使って表せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 一般教育科目 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
(1) では $3 \times 3$ 行列式 $\det(A - \lambda I)$ を直接展開して $\lambda$ の各次数の係数を比較し，$\operatorname{Tr} A$ と $\operatorname{Tr} A^2$ の成分表示と照合することで $P, Q, R$ の表式を証明します。

(2) では $P = 0$ のときの3次方程式 $\lambda^3 - Q\lambda - R = 0$ に対して，実3次関数の増減と極値の積の符号を調べることで，互いに複素共役な虚数解の組をもつための必要十分条件を $Q$ と $R$ の不等式として導出します。
</div>

### (1)

行列 $A - \lambda I$ の行列式をサラスの方法などで展開します。

$$
\begin{aligned}
F(\lambda) &= \begin{vmatrix}
a_{11} - \lambda & a_{12} & a_{13} \\
a_{21} & a_{22} - \lambda & a_{23} \\
a_{31} & a_{32} & a_{33} - \lambda
\end{vmatrix} \\
&= (a_{11} - \lambda)(a_{22} - \lambda)(a_{33} - \lambda) + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} \\
&\quad - a_{13}a_{31}(a_{22} - \lambda) - a_{12}a_{21}(a_{33} - \lambda) - a_{23}a_{32}(a_{11} - \lambda)
\end{aligned}
$$

これを $\lambda$ の降べきの順に整理すると，各次数の係数は次のようになります。

まず $\lambda^2$ の係数 $P$ を読み取ります。

$$
\begin{aligned}
P &= a_{11} + a_{22} + a_{33} \\
&= \operatorname{Tr} A
\end{aligned}
$$

次に定数項 $R$ は $\lambda = 0$ を代入すれば次のように求まります。

$$
\begin{aligned}
R &= F(0) \\
&= \det A
\end{aligned}
$$

続いて $\lambda$ の1次の係数 $Q$ を読み取ります。

$$
Q = -(a_{11}a_{22} + a_{22}a_{33} + a_{33}a_{11}) + a_{12}a_{21} + a_{23}a_{32} + a_{31}a_{13}
$$

ここで $\operatorname{Tr} A^2$ と $(\operatorname{Tr} A)^2$ を成分で展開して比較します。

$$
\begin{aligned}
\operatorname{Tr} A^2 &= \sum_{i=1}^{3}\sum_{j=1}^{3} a_{ij}a_{ji} \\
&= a_{11}^2 + a_{22}^2 + a_{33}^2 + 2(a_{12}a_{21} + a_{23}a_{32} + a_{31}a_{13})
\end{aligned}
$$

$$
(\operatorname{Tr} A)^2 = a_{11}^2 + a_{22}^2 + a_{33}^2 + 2(a_{11}a_{22} + a_{22}a_{33} + a_{33}a_{11})
$$

両式の差をとって $2$ で割ると，$Q$ の表式に一致します。

$$
\begin{aligned}
\frac{1}{2}\bigl(\operatorname{Tr} A^2 - (\operatorname{Tr} A)^2\bigr) &= a_{12}a_{21} + a_{23}a_{32} + a_{31}a_{13} - (a_{11}a_{22} + a_{22}a_{33} + a_{33}a_{11}) \\
&= Q
\end{aligned}
$$

以上より，$P, Q, R$ の3つの等式がすべて成り立つことが証明されます。

<aside class="rigor-note" markdown>
複素数体上の重複度込みの3つの固有値 $\lambda_1, \lambda_2, \lambda_3$ と解と係数の関係を用いて示すこともできます。$F(\lambda) = -(\lambda - \lambda_1)(\lambda - \lambda_2)(\lambda - \lambda_3)$ を展開すると，$P$ は $\sum_i \lambda_i$ すなわち $\operatorname{Tr} A$ となり，$R$ は $\lambda_1\lambda_2\lambda_3$ すなわち $\det A$ となります。同様に $Q$ についても次式が成り立ちます。

$$
\begin{aligned}
Q &= -(\lambda_1\lambda_2 + \lambda_2\lambda_3 + \lambda_3\lambda_1) \\
&= \frac{1}{2}\left(\sum_{i=1}^{3}\lambda_i^2 - \left(\sum_{i=1}^{3}\lambda_i\right)^2\right) \\
&= \frac{1}{2}\bigl(\operatorname{Tr} A^2 - (\operatorname{Tr} A)^2\bigr)
\end{aligned}
$$
</aside>

### (2)

$A$ は実行列なので $Q, R$ は実数です。$P = 0$ のとき，固有方程式 $F(\lambda) = 0$ は次の実係数3次方程式になります。

$$
g(\lambda) \equiv \lambda^3 - Q\lambda - R = 0
$$

実係数3次方程式が実数でない互いに複素共役な2つの固有値をもつための必要十分条件は，3重実解を除いて $g(\lambda) = 0$ が実数解をちょうど1個だけもつことです。

導関数 $g'(\lambda) = 3\lambda^2 - Q$ の符号によって $Q$ の値で場合分けを行います。

まず $Q < 0$ のとき，すべての実数 $\lambda$ で $g'(\lambda) = 3\lambda^2 - Q > 0$ となるため，$g(\lambda)$ は実軸全体で狭義単調増加です。$\lim_{\lambda \to \pm\infty} g(\lambda) = \pm\infty$ より，$R$ の値によらず実数解は必ず1個だけ存在し，残りの2解は実数でない複素共役な組となります。このとき $4Q^3 < 0 \le 27R^2$ なので，不等式 $27R^2 > 4Q^3$ は自動的に成り立ちます。

次に $Q = 0$ のとき，$g(\lambda) = \lambda^3 - R$ です。$R = 0$ のときは $\lambda = 0$ が3重実解となり複素共役な虚数解をもちません。一方 $R \neq 0$ のときは実数解 $\lambda = R^{1/3}$ が1個と，虚数解 $\lambda = R^{1/3}\left(-\dfrac{1}{2} \pm i\dfrac{\sqrt{3}}{2}\right)$ が1組存在します。したがって条件は $R \neq 0$，すなわち $27R^2 > 0 = 4Q^3$ です。

最後に $Q > 0$ のとき，$g'(\lambda) = 0$ は2つの異なる実数解 $\lambda_{\pm} = \pm\sqrt{\dfrac{Q}{3}}$ をもち，$g(\lambda)$ は $\lambda_-$ で極大，$\lambda_+$ で極小となります。各極値を計算します。

$$
\begin{aligned}
g(\lambda_-) &= \frac{2Q}{3}\sqrt{\frac{Q}{3}} - R \\
g(\lambda_+) &= -\frac{2Q}{3}\sqrt{\frac{Q}{3}} - R
\end{aligned}
$$

3次関数 $y = g(\lambda)$ のグラフが横軸とちょうど1点だけで交わるための必要十分条件は，極大値と極小値が同符号であること，すなわち $g(\lambda_-)g(\lambda_+) > 0$ です。

$$
\begin{aligned}
g(\lambda_-)g(\lambda_+) &= R^2 - \frac{4}{27}Q^3 \\
&> 0
\end{aligned}
$$

両辺に $27$ を掛けると $27R^2 > 4Q^3$ が得られます。

以上3つの場合を統合すると，$Q$ の符号にかかわらず，行列 $A$ が実数でない複素共役の固有値をもつための必要十分条件は $27R^2 > 4Q^3$ に一致します。

$$
\finalanswer{27R^2 > 4Q^3}
$$
