---
title: 東大理物 平成31年度 数学 第1問：SU(3) リー代数と行列の無限小変換
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成31年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成31年度 数学 第1問：SU(3) リー代数と行列の無限小変換

## 問題

以下の設問に答えよ。ただし正方行列 $X, Y$ に対して $\operatorname{tr} X$ は $X$ のトレース，$\det X$ は $X$ の行列式を表し，$[X, Y] = XY - YX$，$e^X = \displaystyle\sum_{k=0}^{\infty}\dfrac{X^k}{k!}$ とする。また，行列 $X$ に対して，$X^{\mathrm{T}}$ は $X$ の転置，$X^\dagger$ は $X$ のエルミート共役（転置の複素共役）を表す。ベクトル $\mathbf{x}$ に対して $\mathbf{x}^{\mathrm{T}}$ および $\mathbf{x}^\dagger$ も同様である。$I$ は単位行列を表す。虚数単位を $i$ とする。

1. $A, B$ をエルミート（$A^\dagger = A,\ B^\dagger = B$）かつトレースレス（$\operatorname{tr} A = \operatorname{tr} B = 0$）な有限次元の行列とする。以下の (i)〜(iii) を示せ。ただしエルミート行列 $A$ が対角行列 $D$ とユニタリー行列 $V$（$V^\dagger V = I$）を用いて $A = V^\dagger D V$ と対角化できること，および同じ型の正方行列 $X, Y$ に対して $\det(XY) = \det X \det Y$ が成り立つことを用いてもよい。

(i) $i[A, B]$ はエルミートかつトレースレスである。

(ii) $U = e^{iA}$ はユニタリー行列（$U^\dagger U = I$）である。

(iii) $U = e^{iA}$ は $\det U = 1$ をみたす。

任意のトレースレスな $3$ 行 $3$ 列エルミート行列 $T$ は $8$ つの実数 $\alpha_1, \alpha_2, \dots, \alpha_8$ と $8$ つのトレースレスな $3$ 行 $3$ 列エルミート行列 $T_1, T_2, \dots, T_8$ を用いて以下のように表すことができる。
{: .problem-lead }

$$
T = \begin{pmatrix}
\alpha_7 & \alpha_1 - i\alpha_2 & \alpha_3 - i\alpha_4 \\
\alpha_1 + i\alpha_2 & \alpha_8 & \alpha_5 - i\alpha_6 \\
\alpha_3 + i\alpha_4 & \alpha_5 + i\alpha_6 & -\alpha_7 - \alpha_8
\end{pmatrix} = \sum_{a=1}^{8} \alpha_a T_a
$$

2. 行列 $T_1, T_2$ および $T_7$ の具体形を書け。
3. 設問1の (i) より，実数 $A_{ab, c}\ (a, b, c = 1, 2, \dots, 8)$ を用いて $[T_a, T_b] = i\displaystyle\sum_{c=1}^{8} A_{ab, c} T_c$ と書ける。$A_{71, 2}$ および $A_{56, 8}$ を求めよ。
4. 実数 $\theta$ を用いて行列 $U$ を $U = e^{i\theta T} = \exp\left(i\theta\displaystyle\sum_{a=1}^{8} \alpha_a T_a\right)$ と定義し，複素 $3$ 成分のベクトル $\mathbf{x} = (x_1, x_2, x_3)^{\mathrm{T}}$，$\mathbf{y} = (y_1, y_2, y_3)^{\mathrm{T}}$，およびそれらに $U$ をかけたベクトル $\mathbf{x}' = U\mathbf{x}$，$\mathbf{y}' = U\mathbf{y}$ を考える。

(i) $G_a = \mathbf{x}^\dagger T_a \mathbf{y}$，$G_a' = \mathbf{x}'^\dagger T_a \mathbf{y}'$ とする（$a = 1, 2, \dots, 8$）。$G_a'$ を $\theta$ の1次まで展開すると，$G_a' = G_a + i\theta\displaystyle\sum_{b=1}^{8} H_{ab} G_b + \mathcal{O}(\theta^2)$ の形に書けることを示し，$H_{ab}$ を求めよ。

(ii) $z_i = \displaystyle\sum_{j, k = 1}^{3} \varepsilon_{ijk} x_j y_k$，$z_i' = \displaystyle\sum_{j, k = 1}^{3} \varepsilon_{ijk} x_j' y_k'$ とし，$\mathbf{z} = (z_1, z_2, z_3)^{\mathrm{T}}$，$\mathbf{z}' = (z_1', z_2', z_3')^{\mathrm{T}}$ とする。$\mathbf{z}'$ を $\theta$ の1次まで展開すると $\mathbf{z}' = (I + i\theta M)\mathbf{z} + \mathcal{O}(\theta^2)$ の形に書けることを示し，行列 $M$ を求めよ。ただし $\varepsilon_{ijk}$ は3階の完全反対称テンソルで，$\varepsilon_{123} = 1,\ \varepsilon_{ijk} = -\varepsilon_{jik} = -\varepsilon_{kji}$ である。$\displaystyle\sum_{k=1}^{3} \varepsilon_{ijk}\varepsilon_{k\ell m} = \delta_{i\ell}\delta_{jm} - \delta_{im}\delta_{j\ell}$ を用いてもよい（$\delta_{i\ell}$ 等はクロネッカーの $\delta$ 記号を表す）。

> 出典：東京大学大学院理学系研究科物理学専攻 平成31年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

## 解答・解説

<div class="approach" markdown>
エルミートかつトレースレスな行列 $A$ の指数関数 $e^{iA}$ は行列式 $1$ のユニタリー行列（特殊ユニタリー群 $\mathrm{SU}(n)$）をなし，その生成元どうしの交換関係は再び同じ空間内に閉じてリー代数を形成します。

$n = 3$ の基本表現ベクトル $\mathbf{x}, \mathbf{y}$ から作られる双線形量 $G_a = \mathbf{x}^\dagger T_a \mathbf{y}$ の無限小変換は構造定数 $A_{ab, c}$ で決まる随伴表現に従い，反対称積 $\mathbf{z} = \mathbf{x} \times \mathbf{y}$ は $\operatorname{tr} T = 0$ を通じて $-T^{\mathrm{T}}$ を生成元とする反基本表現として変換されます。
</div>

### (1)
(i) $A^\dagger = A,\ B^\dagger = B$ と $(XY)^\dagger = Y^\dagger X^\dagger$ を用いて $i[A, B]$ のエルミート共役をとります。

$$
\begin{aligned}
\bigl(i[A, B]\bigr)^\dagger
&= (-i)(AB - BA)^\dagger \\
&= -i\left(B^\dagger A^\dagger - A^\dagger B^\dagger\right) \\
&= -i(BA - AB) = i(AB - BA) = i[A, B]
\end{aligned}
$$

よって $i[A, B]$ はエルミートです。またトレースの巡回性 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ より，

$$
\operatorname{tr}\bigl(i[A, B]\bigr) = i\bigl(\operatorname{tr}(AB) - \operatorname{tr}(BA)\bigr) = 0
$$

となるため，トレースレスでもあります。

(ii) $A^\dagger = A$ より，$U = e^{iA}$ のエルミート共役は次のようになります。

$$
U^\dagger = \left(\sum_{k=0}^{\infty} \frac{(iA)^k}{k!}\right)^\dagger = \sum_{k=0}^{\infty} \frac{(-i)^k (A^\dagger)^k}{k!} = \sum_{k=0}^{\infty} \frac{(-iA)^k}{k!} = e^{-iA}
$$

$iA$ と $-iA$ は可換なので指数法則 $e^{X}e^{Y} = e^{X+Y}$ が成り立ち，

$$
U^\dagger U = e^{-iA} e^{iA} = e^{-iA + iA} = e^0 = I
$$

となります。よって $U$ はユニタリー行列です。

(iii) エルミート行列 $A$ はユニタリー行列 $V$（$V^\dagger V = I$）と実対角行列 $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$ を用いて $A = V^\dagger D V$ と対角化されます。任意の非負整数 $k$ に対して $A^k = V^\dagger D^k V$ なので，

$$
U = e^{iA} = \sum_{k=0}^{\infty} \frac{i^k}{k!} V^\dagger D^k V = V^\dagger e^{iD} V
$$

となります。ここで $e^{iD} = \operatorname{diag}(e^{id_1}, e^{id_2}, \dots, e^{id_n})$ です。行列式の積の公式と $\det(V^\dagger)\det(V) = \det(V^\dagger V) = \det I = 1$ を用いると，

$$
\begin{aligned}
\det U
&= \det(V^\dagger)\det(e^{iD})\det(V) \\
&= \det(V^\dagger V)\prod_{j=1}^{n} e^{id_j} \\
&= \exp\left(i\sum_{j=1}^{n} d_j\right) = e^{i\operatorname{tr} D}
\end{aligned}
$$

さらに $\operatorname{tr} D = \operatorname{tr}(V A V^\dagger) = \operatorname{tr}(A V^\dagger V) = \operatorname{tr} A = 0$ なので，$\det U = e^0 = 1$ が成り立ちます。

### (2)
与えられた $T = \displaystyle\sum_{a=1}^{8} \alpha_a T_a$ の各成分から $\alpha_1,\ \alpha_2,\ \alpha_7$ の係数を取り出します。したがって，

$$
\finalanswer{T_1 = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix},\qquad
T_2 = \begin{pmatrix} 0 & -i & 0 \\ i & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix},\qquad
T_7 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}}
$$

### (3)
まず $[T_7, T_1]$ を直接計算します。

$$
\begin{aligned}
[T_7, T_1]
&= \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
 - \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix} \\
&= \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
 - \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
 = \begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = i T_2
\end{aligned}
$$

定義 $[T_7, T_1] = i\displaystyle\sum_{c=1}^{8} A_{71, c} T_c$ と比較すると $A_{71, 2} = 1$ です。

次に $T_5,\ T_6,\ T_8$ を書き下し，$[T_5, T_6]$ を計算します。

$$
T_5 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix},\qquad
T_6 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -i \\ 0 & i & 0 \end{pmatrix},\qquad
T_8 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{pmatrix}
$$

$$
\begin{aligned}
[T_5, T_6]
&= \begin{pmatrix} 0 & 0 & 0 \\ 0 & i & 0 \\ 0 & 0 & -i \end{pmatrix}
 - \begin{pmatrix} 0 & 0 & 0 \\ 0 & -i & 0 \\ 0 & 0 & i \end{pmatrix} \\
&= \begin{pmatrix} 0 & 0 & 0 \\ 0 & 2i & 0 \\ 0 & 0 & -2i \end{pmatrix} = 2i T_8
\end{aligned}
$$

定義 $[T_5, T_6] = i\displaystyle\sum_{c=1}^{8} A_{56, c} T_c$ と比較すると $A_{56, 8} = 2$ です。したがって，

$$
\finalanswer{A_{71, 2} = 1,\qquad A_{56, 8} = 2}
$$

### (4)
(i) $U = e^{i\theta T} = I + i\theta T + \mathcal{O}(\theta^2)$，および $U^\dagger = e^{-i\theta T} = I - i\theta T + \mathcal{O}(\theta^2)$ を $G_a' = \mathbf{x}'^\dagger T_a \mathbf{y}' = \mathbf{x}^\dagger U^\dagger T_a U \mathbf{y}$ に代入し，$\theta$ の1次まで展開します。

$$
\begin{aligned}
G_a'
&= \mathbf{x}^\dagger (I - i\theta T) T_a (I + i\theta T)\mathbf{y} + \mathcal{O}(\theta^2) \\
&= \mathbf{x}^\dagger T_a \mathbf{y} + i\theta\,\mathbf{x}^\dagger (T_a T - T T_a)\mathbf{y} + \mathcal{O}(\theta^2) \\
&= G_a + i\theta\,\mathbf{x}^\dagger [T_a, T]\mathbf{y} + \mathcal{O}(\theta^2)
\end{aligned}
$$

ここで $T = \displaystyle\sum_{c=1}^{8} \alpha_c T_c$ と設問3の交換関係 $[T_a, T_c] = i\displaystyle\sum_{b=1}^{8} A_{ac, b} T_b$ を代入します。

$$
\begin{aligned}
\mathbf{x}^\dagger [T_a, T]\mathbf{y}
&= \sum_{c=1}^{8} \alpha_c\,\mathbf{x}^\dagger [T_a, T_c]\mathbf{y} \\
&= \sum_{c=1}^{8} \alpha_c \left(i\sum_{b=1}^{8} A_{ac, b}\,\mathbf{x}^\dagger T_b \mathbf{y}\right) \\
&= \sum_{b=1}^{8} \left(i\sum_{c=1}^{8} \alpha_c A_{ac, b}\right) G_b
\end{aligned}
$$

よって $G_a' = G_a + i\theta\displaystyle\sum_{b=1}^{8} H_{ab} G_b + \mathcal{O}(\theta^2)$ の形に書くことができ，$H_{ab}$ が求まります。したがって，

$$
\finalanswer{H_{ab} = i\sum_{c=1}^{8} \alpha_c A_{ac, b}}
$$

(ii) $\mathbf{x}' = (I + i\theta T)\mathbf{x} + \mathcal{O}(\theta^2)$，$\mathbf{y}' = (I + i\theta T)\mathbf{y} + \mathcal{O}(\theta^2)$ を $z_i' = \displaystyle\sum_{j, k = 1}^{3} \varepsilon_{ijk} x_j' y_k'$ に代入して $\theta$ の1次まで展開します。

$$
z_i' = z_i + i\theta\sum_{j, k, p = 1}^{3} \varepsilon_{ijk}\left(T_{jp} x_p y_k + T_{kp} x_j y_p\right) + \mathcal{O}(\theta^2)
$$

右辺第2項の括弧内第2項でダミー添字 $j$ と $k$ を入れ替え，$\varepsilon_{ikj} = -\varepsilon_{ijk}$ を用いると，

$$
\sum_{j, k, p = 1}^{3} \varepsilon_{ijk}\left(T_{jp} x_p y_k + T_{kp} x_j y_p\right)
= \sum_{j, k, p = 1}^{3} \varepsilon_{ijk} T_{jp}\left(x_p y_k - x_k y_p\right)
$$

となります。ここで $z_m = \displaystyle\sum_{r, s = 1}^{3} \varepsilon_{mrs} x_r y_s$ と与えられた公式 $\displaystyle\sum_{m=1}^{3} \varepsilon_{mpk}\varepsilon_{mrs} = \delta_{pr}\delta_{ks} - \delta_{ps}\delta_{kr}$ を用いると，

$$
\sum_{m=1}^{3} \varepsilon_{mpk} z_m = \sum_{r, s = 1}^{3} \left(\delta_{pr}\delta_{ks} - \delta_{ps}\delta_{kr}\right) x_r y_s = x_p y_k - x_k y_p
$$

が成り立ちます。これを上の式に代入し，再び $\displaystyle\sum_{k=1}^{3} \varepsilon_{ijk}\varepsilon_{mpk} = \delta_{im}\delta_{jp} - \delta_{ip}\delta_{jm}$ と $\operatorname{tr} T = 0$ を用います。

$$
\begin{aligned}
\sum_{j, k, p = 1}^{3} \varepsilon_{ijk} T_{jp}\left(x_p y_k - x_k y_p\right)
&= \sum_{j, k, p, m = 1}^{3} \varepsilon_{ijk}\varepsilon_{mpk} T_{jp} z_m \\
&= \sum_{j, p, m = 1}^{3} \left(\delta_{im}\delta_{jp} - \delta_{ip}\delta_{jm}\right) T_{jp} z_m \\
&= \left(\sum_{j=1}^{3} T_{jj}\right) z_i - \sum_{m=1}^{3} T_{mi} z_m \\
&= (\operatorname{tr} T) z_i - \sum_{m=1}^{3} (T^{\mathrm{T}})_{im} z_m \\
&= -\sum_{m=1}^{3} (T^{\mathrm{T}})_{im} z_m
\end{aligned}
$$

よって $\mathbf{z}' = \left(I + i\theta(-T^{\mathrm{T}})\right)\mathbf{z} + \mathcal{O}(\theta^2)$ となります（$T$ はエルミートなので $-T^{\mathrm{T}} = -T^*$ とも表すことができます）。したがって，

$$
\finalanswer{M = -T^{\mathrm{T}} = -T^*}
$$

<aside class="rigor-note" markdown>
本問題の8個の行列 $T_1, \dots, T_8$ はリー代数 $\mathfrak{su}(3)$ の基底をなします（ゲルマン行列の線形結合で表されます）。設問4(ii)の変換は，有限変換では $\det U = 1$ と $U^{-1} = U^\dagger$ より $\mathbf{z}' = (U\mathbf{x})\times(U\mathbf{y}) = (\det U)(U^{-1})^{\mathrm{T}}\mathbf{z} = U^*\mathbf{z} = e^{-i\theta T^*}\mathbf{z}$ となり，基本表現 $\mathbf{3}$ の反対称テンソル積が反基本表現 $\bar{\mathbf{3}}$ に変換されることに対応しています。
</aside>
