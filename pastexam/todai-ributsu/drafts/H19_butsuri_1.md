---
title: 東大理物 平成19年度 物理学 第1問：角運動量の交換関係と固有値の量子化
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成19年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成19年度 物理学 第1問：角運動量の交換関係と固有値の量子化

## 問題

量子論における軌道角運動量 $\boldsymbol{l}$ は古典論と同様に座標 $\boldsymbol{r}$ と運動量 $\boldsymbol{p}$ のベクトル積で与えられる。すなわち $\boldsymbol{l} = \boldsymbol{r}\times\boldsymbol{p}$ である。ここで，それぞれのベクトルの成分は $\boldsymbol{r} = (x, y, z)$，$\boldsymbol{p} = (p_x, p_y, p_z)$，$\boldsymbol{l} = (l_x, l_y, l_z)$ である。以下の設問に答えよ。ただし，$\hbar = \dfrac{h}{2\pi}$（$h$ はプランク定数）を用いよ。

(1) $l_z$ と $x, y, z$ との間の交換関係を求めよ。

(2) $l_z$ と $p_x, p_y, p_z$ との間の交換関係を求めよ。

(3) $l_a$ と $l_b$ との間の交換関係を求めよ。ただし，$a, b = x, y, z$ である。

量子論では，軌道角運動量 $\boldsymbol{l}$ を拡張して設問3の交換関係を満たす演算子を角運動量 $\boldsymbol{J}$ と呼ぶ。以下では，角運動量 $\boldsymbol{J}$ のみが力学変数である力学系を考える。ここで，変数 $A$ を $A = J_x - iJ_y$，変数 $B$ を $B = J_x^2 + J_y^2 + J_z^2$ と定義する。次の設問に答えよ。
{: .problem-lead }

(4) $A^\dagger A$ および $A A^\dagger$ を $B$ と $J_z$ を用いて書け。ただし，$A^\dagger$ は $A$ の複素共役演算子である。

(5) $B$ は演算子ではなくただの数であることを示せ。

$J_z$ は固有値を持つと考えて，その固有値を $\Theta_z$ および固有状態を $|\Theta_z\rangle$ とする。次の設問に答えよ。
{: .problem-lead }

(6) $A|\Theta_z\rangle \neq 0$ ならば $A|\Theta_z\rangle$ も $J_z$ の固有状態であることを示せ。また，その固有値を求めよ。

(7) $\langle\Theta_z|A^\dagger A|\Theta_z\rangle \ge 0$ と $\langle\Theta_z|AA^\dagger|\Theta_z\rangle \ge 0$ を用いて，$-m \le \Theta_z \le m$ を証明せよ。ただし，$m = \sqrt{B + \dfrac{1}{4}\hbar^2} - \dfrac{1}{2}\hbar$ である。

(8) 以上の結果を用いて，$m$ が $\hbar$ の整数倍であるかまたは半整数倍であることを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成19年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
軌道角運動量の成分は座標と運動量の積で作られるため，正準交換関係から角運動量同士の交換関係を直接計算することができます。この交換関係だけを出発点にすると，座標表示を使わずに角運動量の一般的な性質を調べることができます。

演算子 $A = J_x - iJ_y$ とその共役 $A^\dagger$ は，$J_z$ の固有値を $\hbar$ だけ増減させるはしご演算子としてはたらきます。一方，状態のノルムは必ず $0$ 以上なので，$A^\dagger A$ と $AA^\dagger$ の期待値が $0$ 以上という条件から固有値の上限と下限が定まり，はしごの段数が有限になることから量子化条件を導くことができます。
</div>

### (1)

$\boldsymbol{l} = \boldsymbol{r}\times\boldsymbol{p}$ より，$l_z = x p_y - y p_x$ です。正準交換関係 $[x_a, p_b] = i\hbar\delta_{ab}$，$[x_a, x_b] = 0$，および積の公式 $[XY, Z] = X[Y, Z] + [X, Z]Y$ を用いて計算します。

$$
\begin{aligned}
[l_z, x] &= [x p_y - y p_x, x] \\
&= x[p_y, x] + [x, x]p_y - y[p_x, x] - [y, x]p_x \\
&= 0 + 0 - y(-i\hbar) - 0 \\
&= i\hbar y
\end{aligned}
$$

$$
\begin{aligned}
[l_z, y] &= [x p_y - y p_x, y] \\
&= x[p_y, y] + [x, y]p_y - y[p_x, y] - [y, y]p_x \\
&= x(-i\hbar) + 0 - 0 - 0 \\
&= -i\hbar x
\end{aligned}
$$

$$
\begin{aligned}
[l_z, z] &= [x p_y - y p_x, z] \\
&= x[p_y, z] + [x, z]p_y - y[p_x, z] - [y, z]p_x \\
&= 0
\end{aligned}
$$

したがって，求める交換関係は次式となります。

$$
\finalanswer{[l_z, x] = i\hbar y, \qquad [l_z, y] = -i\hbar x, \qquad [l_z, z] = 0}
$$

### (2)

設問1と同様に，正準交換関係と $[p_a, p_b] = 0$ を用いて計算します。

$$
\begin{aligned}
[l_z, p_x] &= [x p_y - y p_x, p_x] \\
&= x[p_y, p_x] + [x, p_x]p_y - y[p_x, p_x] - [y, p_x]p_x \\
&= 0 + (i\hbar)p_y - 0 - 0 \\
&= i\hbar p_y
\end{aligned}
$$

$$
\begin{aligned}
[l_z, p_y] &= [x p_y - y p_x, p_y] \\
&= x[p_y, p_y] + [x, p_y]p_y - y[p_x, p_y] - [y, p_y]p_x \\
&= 0 + 0 - 0 - (i\hbar)p_x \\
&= -i\hbar p_x
\end{aligned}
$$

$$
\begin{aligned}
[l_z, p_z] &= [x p_y - y p_x, p_z] \\
&= x[p_y, p_z] + [x, p_z]p_y - y[p_x, p_z] - [y, p_z]p_x \\
&= 0
\end{aligned}
$$

したがって，求める交換関係は次式となります。

$$
\finalanswer{[l_z, p_x] = i\hbar p_y, \qquad [l_z, p_y] = -i\hbar p_x, \qquad [l_z, p_z] = 0}
$$

### (3)

$l_x = y p_z - z p_y$，$l_y = z p_x - x p_z$ に対して，設問1と設問2の結果を用いて $[l_z, l_x]$ を計算します。公式 $[X, YZ] = [X, Y]Z + Y[X, Z]$ を用います。

$$
\begin{aligned}
[l_z, l_x] &= [l_z, y p_z - z p_y] \\
&= [l_z, y]p_z + y[l_z, p_z] - [l_z, z]p_y - z[l_z, p_y] \\
&= (-i\hbar x)p_z + 0 - 0 - z(-i\hbar p_x) \\
&= i\hbar(z p_x - x p_z) \\
&= i\hbar l_y
\end{aligned}
$$

座標と運動量の定義は $x \to y \to z \to x$ の巡回置換に対して不変なので，$[l_x, l_y] = i\hbar l_z$ と $[l_y, l_z] = i\hbar l_x$ も同様に得られます。また，反対称性 $[l_b, l_a] = -[l_a, l_b]$ より $[l_a, l_a] = 0$ です。レヴィ・チヴィタ記号 $\varepsilon_{abc}$ を用いると，これらをまとめて次式で表すことができます。

$$
\finalanswer{[l_a, l_b] = i\hbar\sum_{c = x, y, z} \varepsilon_{abc}\, l_c \quad \bigl([l_x, l_y] = i\hbar l_z,\ [l_y, l_z] = i\hbar l_x,\ [l_z, l_x] = i\hbar l_y,\ [l_a, l_a] = 0\bigr)}
$$

### (4)

$J_x, J_y, J_z$ はエルミート演算子なので，$A = J_x - iJ_y$ のエルミート共役は $A^\dagger = J_x + iJ_y$ です。$[J_x, J_y] = i\hbar J_z$ と $J_x^2 + J_y^2 = B - J_z^2$ を用いて $A^\dagger A$ と $A A^\dagger$ を展開します。

$$
\begin{aligned}
A^\dagger A &= (J_x + iJ_y)(J_x - iJ_y) \\
&= J_x^2 + J_y^2 - i(J_x J_y - J_y J_x) \\
&= J_x^2 + J_y^2 - i[J_x, J_y] \\
&= (B - J_z^2) - i(i\hbar J_z) \\
&= B - J_z^2 + \hbar J_z
\end{aligned}
$$

$$
\begin{aligned}
A A^\dagger &= (J_x - iJ_y)(J_x + iJ_y) \\
&= J_x^2 + J_y^2 + i(J_x J_y - J_y J_x) \\
&= J_x^2 + J_y^2 + i[J_x, J_y] \\
&= (B - J_z^2) + i(i\hbar J_z) \\
&= B - J_z^2 - \hbar J_z
\end{aligned}
$$

したがって，$A^\dagger A$ と $A A^\dagger$ は次式となります。

$$
\finalanswer{A^\dagger A = B - J_z^2 + \hbar J_z, \qquad A A^\dagger = B - J_z^2 - \hbar J_z}
$$

### (5)

$B = J_x^2 + J_y^2 + J_z^2$ と $J_z$ の交換関係を計算します。$[J_z^2, J_z] = 0$ です。

$$
\begin{aligned}
[B, J_z] &= [J_x^2, J_z] + [J_y^2, J_z] + [J_z^2, J_z] \\
&= J_x[J_x, J_z] + [J_x, J_z]J_x + J_y[J_y, J_z] + [J_y, J_z]J_y \\
&= J_x(-i\hbar J_y) + (-i\hbar J_y)J_x + J_y(i\hbar J_x) + (i\hbar J_x)J_y \\
&= i\hbar(-J_x J_y - J_y J_x + J_y J_x + J_x J_y) \\
&= 0
\end{aligned}
$$

$x, y, z$ の巡回置換から，$[B, J_x] = 0$ および $[B, J_y] = 0$ も同様に成り立ちます。

この力学系では角運動量 $\boldsymbol{J}$ のみが力学変数なので，$B$ は系に存在するすべての力学変数と可換です。すべての力学変数と可換な演算子は，既約な状態空間の上で恒等演算子の定数倍となるため，$B$ は演算子ではなくただの数になります。

### (6)

まず $J_z$ と $A = J_x - iJ_y$ の交換関係を計算します。

$$
\begin{aligned}
[J_z, A] &= [J_z, J_x] - i[J_z, J_y] \\
&= i\hbar J_y - i(-i\hbar J_x) \\
&= i\hbar J_y - \hbar J_x \\
&= -\hbar(J_x - iJ_y) \\
&= -\hbar A
\end{aligned}
$$

これより $J_z A = A J_z - \hbar A$ です。この両辺を固有状態 $|\Theta_z\rangle$ に作用させます。

$$
\begin{aligned}
J_z\bigl(A|\Theta_z\rangle\bigr) &= (A J_z - \hbar A)|\Theta_z\rangle \\
&= A(\Theta_z|\Theta_z\rangle) - \hbar A|\Theta_z\rangle \\
&= (\Theta_z - \hbar)\bigl(A|\Theta_z\rangle\bigr)
\end{aligned}
$$

したがって，$A|\Theta_z\rangle \neq 0$ ならば $A|\Theta_z\rangle$ も $J_z$ の固有状態であり，その固有値は $\Theta_z - \hbar$ です。

$$
\finalanswer{\Theta_z - \hbar}
$$

### (7)

$m = \sqrt{B + \dfrac{1}{4}\hbar^2} - \dfrac{1}{2}\hbar$ の両辺に $\dfrac{1}{2}\hbar$ を足して2乗すると，$B$ を $m$ で表すことができます。

$$
\begin{aligned}
\left(m + \frac{1}{2}\hbar\right)^2 &= B + \frac{1}{4}\hbar^2 \\
m^2 + m\hbar + \frac{1}{4}\hbar^2 &= B + \frac{1}{4}\hbar^2 \\
B &= m^2 + m\hbar
\end{aligned}
$$

また $B = J_x^2 + J_y^2 + J_z^2$ の期待値は3つのエルミート演算子の2乗の和なので $B \ge 0$ であり，よって $m \ge 0$ です。

設問4の結果と $B = m^2 + m\hbar$ を2つの不等式に代入し，左辺を因数分解します。まず $\langle\Theta_z|A^\dagger A|\Theta_z\rangle \ge 0$ について計算します。

$$
\begin{aligned}
\langle\Theta_z|A^\dagger A|\Theta_z\rangle &= \langle\Theta_z|(B - J_z^2 + \hbar J_z)|\Theta_z\rangle \\
&= (m^2 + m\hbar - \Theta_z^2 + \hbar\Theta_z)\langle\Theta_z|\Theta_z\rangle \\
&= (m + \Theta_z)(m + \hbar - \Theta_z)\langle\Theta_z|\Theta_z\rangle \ge 0
\end{aligned}
$$

$\langle\Theta_z|\Theta_z\rangle > 0$ より $(m + \Theta_z)(m + \hbar - \Theta_z) \ge 0$ です。$m \ge 0$ より $-m < m + \hbar$ なので，次式が得られます。

$$
-m \le \Theta_z \le m + \hbar
$$

次に $\langle\Theta_z|A A^\dagger|\Theta_z\rangle \ge 0$ について同様に計算します。

$$
\begin{aligned}
\langle\Theta_z|A A^\dagger|\Theta_z\rangle &= \langle\Theta_z|(B - J_z^2 - \hbar J_z)|\Theta_z\rangle \\
&= (m^2 + m\hbar - \Theta_z^2 - \hbar\Theta_z)\langle\Theta_z|\Theta_z\rangle \\
&= (m - \Theta_z)(m + \hbar + \Theta_z)\langle\Theta_z|\Theta_z\rangle \ge 0
\end{aligned}
$$

$\langle\Theta_z|\Theta_z\rangle > 0$ および $-(m + \hbar) < m$ より，次式が得られます。

$$
-(m + \hbar) \le \Theta_z \le m
$$

2つの不等式の共通範囲をとると，$-m \le \Theta_z \le m$ が成り立ちます。

### (8)

設問6より，固有状態 $|\Theta_z\rangle$ に $A$ を1回作用させるたびに，$0$ でない限り $J_z$ の固有値が $\hbar$ ずつ下がります。しかし設問7より固有値には下限 $-m$ があるため，$A$ を有限回作用させたところで必ず $A|\Theta_{\min}\rangle = 0$ となる最小固有値 $\Theta_{\min}$ と固有状態 $|\Theta_{\min}\rangle \neq 0$ に達します。

このとき $\langle\Theta_{\min}|A^\dagger A|\Theta_{\min}\rangle = 0$ なので，設問7の因数分解から次式が成り立ちます。

$$
(m + \Theta_{\min})(m + \hbar - \Theta_{\min}) = 0
$$

設問7より $\Theta_{\min} \le m < m + \hbar$ なので $m + \hbar - \Theta_{\min} > 0$ です。よって $m + \Theta_{\min} = 0$，すなわち $\Theta_{\min} = -m$ となります。

次に $A^\dagger$ について考えます。設問6の $[J_z, A] = -\hbar A$ のエルミート共役をとると，$[A^\dagger, J_z] = -\hbar A^\dagger$ すなわち $[J_z, A^\dagger] = \hbar A^\dagger$ です。よって $A^\dagger|\Theta_z\rangle \neq 0$ ならば，その状態は固有値 $\Theta_z + \hbar$ の $J_z$ の固有状態になります。

$|\Theta_{\min}\rangle$ に $A^\dagger$ を繰り返し作用させると，固有値は $-m$ から $\hbar$ ずつ増えますが，設問7の上限 $m$ を超えることはできません。したがって，ある非負整数 $k$ 回作用させたところで最大固有値 $\Theta_{\max} = -m + k\hbar$ の状態 $|\Theta_{\max}\rangle = (A^\dagger)^k|\Theta_{\min}\rangle \neq 0$ に達し，$A^\dagger|\Theta_{\max}\rangle = 0$ となります。

このとき $\langle\Theta_{\max}|A A^\dagger|\Theta_{\max}\rangle = 0$ なので，設問7の因数分解から次式が成り立ちます。

$$
(m - \Theta_{\max})(m + \hbar + \Theta_{\max}) = 0
$$

$\Theta_{\max} \ge -m > -(m + \hbar)$ より $m + \hbar + \Theta_{\max} > 0$ なので，$\Theta_{\max} = m$ です。これを $\Theta_{\max} = -m + k\hbar$ と等しいとおいて解きます。

$$
\begin{aligned}
-m + k\hbar &= m \\
2m &= k\hbar \\
m &= \frac{k}{2}\hbar
\end{aligned}
$$

$k$ は $0$ 以上の整数なので，$k$ が偶数のとき $m$ は $\hbar$ の整数倍，$k$ が奇数のとき $m$ は $\hbar$ の半整数倍になります。
