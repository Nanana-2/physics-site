===== FILE: 13probability_statistics/01/01_010.md =====
---
tags:
  - 基本
---

# 条件付き確率とベイズの定理

## 問題
ある母集団において，特定の病気にかかっている人の割合が $p$（$0 < p < 1$）であるとする。無作為に選ばれた人が実際に罹患している事象を $D$，罹患していない事象を $D^c$ と表す。この病気の検査で陽性反応が出る事象を $+$ とする。実際に罹患している受検者が陽性と判定される確率が $P(+ \mid D) = 1-\beta$，罹患していない受検者が誤って陽性と判定される確率が $P(+ \mid D^c) = \alpha$ であるとする。ただし $0 < \alpha < 1$，$0 < \beta < 1$ である。以下の問いに答えよ。

(1) 無作為に選ばれた1人の受検者が陽性反応を示す確率 $P(+)$ を求めよ。

(2) 陽性反応を示した受検者が，実際に罹患している条件付き確率 $P(D \mid +)$ を求めよ。

(3) $p = 0.001$，$\alpha = 0.01$，$\beta = 0.05$ のとき，$P(D \mid +)$ の値を求めよ。

---

## 解答・解説

### (1)
事象の分割と条件付き確率の関係を図に示します。

<!-- FIGURE solution (1): 全事象を罹患Dと非罹患Dcに分割し，それぞれから検査陽性+が生じる確率を表す樹形図。 -->

受検者が陽性反応を示す事象 $+$ は，罹患していて陽性となる事象 $D \cap +$ と，罹患しておらず誤って陽性となる事象 $D^c \cap +$ の2つの互いに排反な事象の和事象として表されます。全確率の公式を用いると，事象 $+$ の確率は次のように展開されます。

$$
\begin{aligned}
P(+) &= P(+ \cap D) + P(+ \cap D^c) \\
&= P(+ \mid D) P(D) + P(+ \mid D^c) P(D^c)
\end{aligned}
$$

問題文の条件より，$P(D) = p$，$P(D^c) = 1-p$，$P(+ \mid D) = 1-\beta$，$P(+ \mid D^c) = \alpha$ です。これらを代入すると，

$$
\finalanswer{P(+) = (1-\beta)p + \alpha(1-p)}
$$

となります。

### (2)
陽性反応を示したという条件のもとで実際に罹患している確率は，条件付き確率の定義とベイズの定理により次のように表されます。

$$
P(D \mid +) = \frac{P(+ \cap D)}{P(+)} = \frac{P(+ \mid D)P(D)}{P(+)}
$$

分子は罹患していて陽性となる確率 $P(+ \mid D)P(D) = (1-\beta)p$ であり，分母は (1) で求めた全確率 $P(+)$ です。これらを代入すると，

$$
\finalanswer{P(D \mid +) = \frac{(1-\beta)p}{(1-\beta)p + \alpha(1-p)}}
$$

となります。

### (3)
(2) で求めた式に与えられた数値を代入します。分子を計算すると，

$$
(1-\beta)p = (1 - 0.05) \times 0.001 = 0.00095
$$

となります。分母の第2項を計算すると，

$$
\alpha(1-p) = 0.01 \times (1 - 0.001) = 0.01 \times 0.999 = 0.00999
$$

となります。したがって，分母全体の値は，

$$
P(+) = 0.00095 + 0.00999 = 0.01094
$$

となります。これらを比の式に代入して計算すると，

$$
\begin{aligned}
P(D \mid +) &= \frac{0.00095}{0.01094} \\
&= \frac{95}{1094} \\
&\approx \finalanswer{0.087}
\end{aligned}
$$

となります。罹患率 $p$ が非常に小さい場合，検査自体の精度が高くても，陽性反応が出た受検者が実際に罹患している確率は $10\,\%$ 未満にとどまります。

===== FILE: 13probability_statistics/01/01_020.md =====
---
tags:
  - 基本
---

# 確率変数と期待値

## 問題
非負の実数値をとる連続型確率変数 $X$ の確率密度関数が，正の実数 $\lambda$ を用いて次のように与えられている。
$x \ge 0$ において $f(x) = C x e^{-\lambda x}$，
$x < 0$ において $f(x) = 0$。
ただし $C$ は規格化定数である。以下の問いに答えよ。

(1) 規格化条件 $\int_{-\infty}^\infty f(x) dx = 1$ から，定数 $C$ を求めよ。

(2) $X$ の期待値 $E[X]$ を求めよ。

(3) 2次のモーメント $E[X^2]$ を求めよ。

---

## 解答・解説

### (1)
確率密度関数は全区間で積分すると $1$ にならなければなりません。$x < 0$ で $f(x) = 0$ であるため，規格化条件は半無限区間上の積分となります。

$$
\int_{-\infty}^\infty f(x) dx = C \int_0^\infty x e^{-\lambda x} dx = 1
$$

この積分を部分積分法により計算します。$u = x$，$v' = e^{-\lambda x}$ とおくと，

$$
\begin{aligned}
\int_0^\infty x e^{-\lambda x} dx &= \left[ -\frac{x}{\lambda} e^{-\lambda x} \right]_0^\infty + \frac{1}{\lambda} \int_0^\infty e^{-\lambda x} dx \\
&= 0 + \frac{1}{\lambda} \left[ -\frac{1}{\lambda} e^{-\lambda x} \right]_0^\infty \\
&= \frac{1}{\lambda^2}
\end{aligned}
$$

となります。したがって規格化条件は次のように書けます。

$$
C \cdot \frac{1}{\lambda^2} = 1
$$

両辺に $\lambda^2$ を掛けると，

$$
\finalanswer{C = \lambda^2}
$$

となります。

### (2)
連続型確率変数の期待値の定義に従い，計算を行います。

$$
E[X] = \int_{-\infty}^\infty x f(x) dx = \lambda^2 \int_0^\infty x^2 e^{-\lambda x} dx
$$

この積分を部分積分法により計算します。

$$
\begin{aligned}
\int_0^\infty x^2 e^{-\lambda x} dx &= \left[ -\frac{x^2}{\lambda} e^{-\lambda x} \right]_0^\infty + \frac{2}{\lambda} \int_0^\infty x e^{-\lambda x} dx \\
&= 0 + \frac{2}{\lambda} \cdot \frac{1}{\lambda^2} \\
&= \frac{2}{\lambda^3}
\end{aligned}
$$

となります。求めた積分値を期待値の式に代入すると，

$$
\begin{aligned}
E[X] &= \lambda^2 \cdot \frac{2}{\lambda^3} \\
&= \finalanswer{\frac{2}{\lambda}}
\end{aligned}
$$

となります。

### (3)
同様に，2次モーメント $E[X^2]$ を定義式に基づいて計算します。

$$
E[X^2] = \int_{-\infty}^\infty x^2 f(x) dx = \lambda^2 \int_0^\infty x^3 e^{-\lambda x} dx
$$

部分積分法を適用して次数を1つ下げます。

$$
\begin{aligned}
\int_0^\infty x^3 e^{-\lambda x} dx &= \left[ -\frac{x^3}{\lambda} e^{-\lambda x} \right]_0^\infty + \frac{3}{\lambda} \int_0^\infty x^2 e^{-\lambda x} dx \\
&= 0 + \frac{3}{\lambda} \cdot \frac{2}{\lambda^3} \\
&= \frac{6}{\lambda^4}
\end{aligned}
$$

となります。求めた積分値を代入すると，

$$
\begin{aligned}
E[X^2] &= \lambda^2 \cdot \frac{6}{\lambda^4} \\
&= \finalanswer{\frac{6}{\lambda^2}}
\end{aligned}
$$

となります。一般に自然数 $n$ に対して $\int_0^\infty x^n e^{-\lambda x} dx = \frac{n!}{\lambda^{n+1}}$ が成り立ちます。

===== FILE: 13probability_statistics/01/01_030.md =====
---
tags:
  - 基本
---

# 分散と共分散

## 問題
同一の確率空間上で定義された2つの確率変数 $X, Y$ を考える。$X, Y$ の期待値をそれぞれ $\mu_X, \mu_Y$，分散を $V[X], V[Y]$ とする。共分散は $\mathrm{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$ で定義される。以下の問いに答えよ。

(1) 共分散が $\mathrm{Cov}(X, Y) = E[XY] - \mu_X \mu_Y$ と表されることを示せ。

(2) 和 $X+Y$ の分散 $V[X+Y]$ を，$V[X]$，$V[Y]$，$\mathrm{Cov}(X, Y)$ を用いて表せ。

(3) $X$ と $Y$ が互いに独立であるとき，$V[X+Y] = V[X] + V[Y]$ となることを示せ。

---

## 解答・解説

### (1)
共分散の定義式に含まれる括弧を展開し，期待値の線形性を適用します。

$$
\begin{aligned}
\mathrm{Cov}(X, Y) &= E[(X - \mu_X)(Y - \mu_Y)] \\
&= E[XY - \mu_X Y - \mu_Y X + \mu_X \mu_Y]
\end{aligned}
$$

期待値の線形性により，各項の期待値の和として分解します。$\mu_X$ と $\mu_Y$ は定数であることに注意すると，

$$
\begin{aligned}
\mathrm{Cov}(X, Y) &= E[XY] - \mu_X E[Y] - \mu_Y E[X] + \mu_X \mu_Y \\
&= E[XY] - \mu_X \mu_Y - \mu_Y \mu_X + \mu_X \mu_Y \\
&= \finalanswer{E[XY] - \mu_X \mu_Y}
\end{aligned}
$$

となります。

### (2)
和 $X+Y$ の期待値は，期待値の線形性より $E[X+Y] = \mu_X + \mu_Y$ です。分散の定義に基づいて計算を進めます。

$$
\begin{aligned}
V[X+Y] &= E\left[ ((X+Y) - (\mu_X + \mu_Y))^2 \right] \\
&= E\left[ ((X - \mu_X) + (Y - \mu_Y))^2 \right]
\end{aligned}
$$

2乗の項を展開すると，

$$
V[X+Y] = E\left[ (X - \mu_X)^2 + 2(X - \mu_X)(Y - \mu_Y) + (Y - \mu_Y)^2 \right]
$$

となります。再び期待値の線形性を用いると，

$$
\begin{aligned}
V[X+Y] &= E[(X - \mu_X)^2] + E[(Y - \mu_Y)^2] + 2E[(X - \mu_X)(Y - \mu_Y)] \\
&= \finalanswer{V[X] + V[Y] + 2\mathrm{Cov}(X, Y)}
\end{aligned}
$$

となります。

### (3)
$X$ と $Y$ が互いに独立である場合，積の期待値について $E[XY] = E[X]E[Y] = \mu_X \mu_Y$ が成り立ちます。(1) で求めた共分散の表式にこの関係を代入すると，

$$
\begin{aligned}
\mathrm{Cov}(X, Y) &= E[XY] - \mu_X \mu_Y \\
&= \mu_X \mu_Y - \mu_X \mu_Y \\
&= 0
\end{aligned}
$$

となります。この結果を (2) で得られた分散の式へ代入すると，

$$
\finalanswer{V[X+Y] = V[X] + V[Y]}
$$

となります。独立な確率変数の和の分散は，それぞれの分散の単純な和に帰着されます。

===== FILE: 13probability_statistics/01/01_040.md =====
---
tags:
  - 標準
---

# モーメント母関数と特性関数

## 問題
確率変数 $X$ のモーメント母関数は $M_X(t) = E[e^{tX}]$ で定義される。また，パラメータ $\lambda > 0$ をもつ指数分布に従う連続型確率変数 $X$ の確率密度関数は，
$x \ge 0$ において $f(x) = \lambda e^{-\lambda x}$，
$x < 0$ において $f(x) = 0$
である。以下の問いに答えよ。

(1) $M_X(t)$ を $t$ で $n$ 回微分して $t = 0$ とおくことで，$n$ 次モーメント $E[X^n]$ が得られることを示せ。

(2) 指数分布に従う確率変数 $X$ について，$t < \lambda$ におけるモーメント母関数 $M_X(t)$ を求めよ。

(3) (2) で求めた $M_X(t)$ を用いて，$X$ の分散 $V[X]$ を求めよ。

---

## 解答・解説

### (1)
指数関数 $e^{tX}$ のマクローリン展開を考えます。

$$
e^{tX} = \sum_{k=0}^\infty \frac{(tX)^k}{k!} = 1 + tX + \frac{t^2 X^2}{2!} + \dots + \frac{t^n X^n}{n!} + \dots
$$

両辺の期待値をとると，期待値の線形性により次の級数表示が得られます。

$$
M_X(t) = E[e^{tX}] = \sum_{k=0}^\infty \frac{t^k}{k!} E[X^k]
$$

この級数を $t$ について項別に $n$ 回微分します。$k < n$ の項は微分により消滅し，$k = n$ の項は定数 $E[X^n]$ となります。$k > n$ の項は正のベキの $t$ を因子として残します。

$$
\frac{d^n}{dt^n} M_X(t) = E[X^n] + \sum_{k=n+1}^\infty \frac{t^{k-n}}{(k-n)!} E[X^k]
$$

ここで $t = 0$ とおくと，和のすべての項が $0$ となるため，

$$
\finalanswer{\left. \frac{d^n}{dt^n} M_X(t) \right|_{t=0} = E[X^n]}
$$

となります。

### (2)
モーメント母関数の定義式に従って積分を実行します。

$$
M_X(t) = \int_0^\infty e^{tx} \lambda e^{-\lambda x} dx = \lambda \int_0^\infty e^{-(\lambda - t)x} dx
$$

$t < \lambda$ の条件のもとでは $\lambda - t > 0$ であるため，この広義積分は収束します。積分を実行すると，

$$
\begin{aligned}
M_X(t) &= \lambda \left[ -\frac{1}{\lambda - t} e^{-(\lambda - t)x} \right]_0^\infty \\
&= \lambda \left( 0 - \left( -\frac{1}{\lambda - t} \right) \right) \\
&= \finalanswer{\frac{\lambda}{\lambda - t}}
\end{aligned}
$$

となります。

### (3)
分散は $V[X] = E[X^2] - (E[X])^2$ により計算できます。(2) で得られた $M_X(t) = \lambda(\lambda - t)^{-1}$ を微分します。1階微分を求めると，

$$
M_X'(t) = \frac{d}{dt} \left[ \lambda (\lambda - t)^{-1} \right] = \lambda (\lambda - t)^{-2}
$$

となります。$t = 0$ を代入すると，

$$
E[X] = M_X'(0) = \frac{\lambda}{\lambda^2} = \frac{1}{\lambda}
$$

となります。続いて2階微分を求めると，

$$
M_X''(t) = \frac{d}{dt} \left[ \lambda (\lambda - t)^{-2} \right] = 2\lambda (\lambda - t)^{-3}
$$

となります。$t = 0$ を代入すると，

$$
E[X^2] = M_X''(0) = \frac{2\lambda}{\lambda^3} = \frac{2}{\lambda^2}
$$

となります。したがって分散は，

$$
\begin{aligned}
V[X] &= E[X^2] - (E[X])^2 \\
&= \frac{2}{\lambda^2} - \left( \frac{1}{\lambda} \right)^2 \\
&= \finalanswer{\frac{1}{\lambda^2}}
\end{aligned}
$$

となります。

===== FILE: 13probability_statistics/02/02_010.md =====
---
tags:
  - 基本
---

# 二項分布

## 問題
1回の試行で事象が起こる確率を $p$（$0 < p < 1$）とする。この試行を独立に $n$ 回繰り返すとき，事象の生起回数を $X$ とする。$X$ が値 $k$ をとる確率は
$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \quad (k = 0, 1, \dots, n)
$$
である。以下の問いに答えよ。

(1) 二項定理を用いて，全確率の和 $\sum_{k=0}^n P(X = k)$ が $1$ となることを示せ。

(2) $k \binom{n}{k} = n \binom{n-1}{k-1}$（$k \ge 1$）の関係を用いて，期待値 $E[X]$ を求めよ。

(3) 階乗モーメント $E[X(X-1)]$ を計算することにより，分散 $V[X]$ を求めよ。

---

## 解答・解説

### (1)
二項定理の公式を想起します。実数 $a, b$ に対し，

$$
(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}
$$

が成り立ちます。ここで $a = p$，$b = 1-p$ とおくと，確率の総和は次のように表されます。

$$
\begin{aligned}
\sum_{k=0}^n P(X = k) &= \sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} \\
&= (p + (1-p))^n \\
&= 1^n \\
&= \finalanswer{1}
\end{aligned}
$$

となります。

### (2)
離散型確率変数の期待値の定義式を書きます。$k = 0$ の項は $0$ となるため，和は $k = 1$ から始められます。

$$
E[X] = \sum_{k=0}^n k P(X = k) = \sum_{k=1}^n k \binom{n}{k} p^k (1-p)^{n-k}
$$

問題文で与えられた関係式 $k \binom{n}{k} = n \binom{n-1}{k-1}$ を適用します。

$$
E[X] = \sum_{k=1}^n n \binom{n-1}{k-1} p^k (1-p)^{n-k}
$$

和の外へ定数 $n$ と $p$ を括り出します。

$$
E[X] = np \sum_{k=1}^n \binom{n-1}{k-1} p^{k-1} (1-p)^{(n-1)-(k-1)}
$$

ここで指標を $j = k-1$ と置き換えると，$j$ は $0$ から $n-1$ まで動きます。

$$
\begin{aligned}
E[X] &= np \sum_{j=0}^{n-1} \binom{n-1}{j} p^j (1-p)^{(n-1)-j} \\
&= np (p + (1-p))^{n-1} \\
&= \finalanswer{np}
\end{aligned}
$$

となります。

### (3)
同様にして $E[X(X-1)]$ を求めます。$k=0$ と $k=1$ では $k(k-1)=0$ となるため，和は $k=2$ から始まります。二項係数の恒等式 $k(k-1)\binom{n}{k} = n(n-1)\binom{n-2}{k-2}$ を用いると，

$$
\begin{aligned}
E[X(X-1)] &= \sum_{k=2}^n k(k-1) \binom{n}{k} p^k (1-p)^{n-k} \\
&= n(n-1) p^2 \sum_{k=2}^n \binom{n-2}{k-2} p^{k-2} (1-p)^{(n-2)-(k-2)}
\end{aligned}
$$

となります。$j = k-2$ と置換して二項定理を用いると，残りの和は $1$ となるため，

$$
E[X(X-1)] = n(n-1)p^2
$$

となります。これより 2 次モーメントは，

$$
E[X^2] = E[X(X-1)] + E[X] = n(n-1)p^2 + np
$$

と書けます。したがって分散は，

$$
\begin{aligned}
V[X] &= E[X^2] - (E[X])^2 \\
&= n(n-1)p^2 + np - (np)^2 \\
&= n^2 p^2 - np^2 + np - n^2 p^2 \\
&= np(1-p)
\end{aligned}
$$

となるため，

$$
\finalanswer{V[X] = np(1-p)}
$$

となります。

===== FILE: 13probability_statistics/02/02_020.md =====
---
tags:
  - 基本
---

# ポアソン分布と二項分布の極限

## 問題
二項分布の確率質量関数
$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \quad (k = 0, 1, \dots, n)
$$
において，積 $\lambda = np$（$\lambda > 0$）を一定に保ちながら $n \to \infty$ とする極限を考える。以下の問いに答えよ。

(1) 任意の固定された非負整数 $k$ に対し，$\lim_{n \to \infty} P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ となることを示せ。

(2) ポアソン分布に従う確率変数 $Y$（$P(Y = k) = \frac{\lambda^k e^{-\lambda}}{k!}$，$k = 0, 1, 2, \dots$）の期待値 $E[Y]$ を求めよ。

(3) 確率変数 $Y$ の分散 $V[Y]$ を求めよ。

---

## 解答・解説

### (1)
$p = \frac{\lambda}{n}$ を二項分布の式に代入し，各因子を分離して変形します。

$$
\begin{aligned}
P(X = k) &= \frac{n(n-1)\dots(n-k+1)}{k!} \left( \frac{\lambda}{n} \right)^k \left( 1 - \frac{\lambda}{n} \right)^{n-k} \\
&= \frac{\lambda^k}{k!} \cdot \frac{n(n-1)\dots(n-k+1)}{n^k} \cdot \left( 1 - \frac{\lambda}{n} \right)^n \cdot \left( 1 - \frac{\lambda}{n} \right)^{-k}
\end{aligned}
$$

ここで $n \to \infty$ の極限をとります。第2因子の分数は，

$$
\lim_{n \to \infty} \frac{n(n-1)\dots(n-k+1)}{n^k} = \lim_{n \to \infty} 1 \cdot \left( 1 - \frac{1}{n} \right) \dots \left( 1 - \frac{k-1}{n} \right) = 1
$$

となります。第3因子の極限はネイピア数の定義より，

$$
\lim_{n \to \infty} \left( 1 - \frac{\lambda}{n} \right)^n = e^{-\lambda}
$$

となります。第4因子の極限は，固定された $k$ に対して，

$$
\lim_{n \to \infty} \left( 1 - \frac{\lambda}{n} \right)^{-k} = (1 - 0)^{-k} = 1
$$

となります。すべての極限を合わせると，

$$
\finalanswer{\lim_{n \to \infty} P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}}
$$

となります。

### (2)
期待値の定義式に基づいて計算します。$k = 0$ の項は $0$ であるため除外できます。

$$
E[Y] = \sum_{k=0}^\infty k \frac{\lambda^k e^{-\lambda}}{k!} = \sum_{k=1}^\infty k \frac{\lambda^k e^{-\lambda}}{k!}
$$

$k / k! = 1 / (k-1)!$ を用い，$\lambda e^{-\lambda}$ を級数の外へ括り出します。

$$
E[Y] = \lambda e^{-\lambda} \sum_{k=1}^\infty \frac{\lambda^{k-1}}{(k-1)!}
$$

$m = k-1$ と指標を変換すると，和は指数関数のマクローリン展開そのものになります。

$$
\sum_{m=0}^\infty \frac{\lambda^m}{m!} = e^\lambda
$$

したがって期待値は，

$$
\begin{aligned}
E[Y] &= \lambda e^{-\lambda} \cdot e^\lambda \\
&= \finalanswer{\lambda}
\end{aligned}
$$

となります。

### (3)
分散の計算のために階乗モーメント $E[Y(Y-1)]$ を求めます。$k=0$ と $k=1$ の項は $0$ となるため，和は $k=2$ から始まります。

$$
E[Y(Y-1)] = \sum_{k=2}^\infty k(k-1) \frac{\lambda^k e^{-\lambda}}{k!} = \lambda^2 e^{-\lambda} \sum_{k=2}^\infty \frac{\lambda^{k-2}}{(k-2)!}
$$

$j = k-2$ とおいて総和をとると，級数は $e^\lambda$ となります。

$$
E[Y(Y-1)] = \lambda^2 e^{-\lambda} \cdot e^\lambda = \lambda^2
$$

これより 2 次モーメントは $E[Y^2] = E[Y(Y-1)] + E[Y] = \lambda^2 + \lambda$ となります。したがって分散は，

$$
\begin{aligned}
V[Y] &= E[Y^2] - (E[Y])^2 \\
&= \lambda^2 + \lambda - \lambda^2 \\
&= \finalanswer{\lambda}
\end{aligned}
$$

となります。ポアソン分布では平均と分散が一致します。

===== FILE: 13probability_statistics/02/02_030.md =====
---
tags:
  - 基本
---

# ガウス分布

## 問題
確率変数 $X$ の確率密度関数が，実数 $\mu$ と正の実数 $\sigma$ を用いて
$$
f(x) = C \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) \quad (-\infty < x < \infty)
$$
で与えられている。ただし $C$ は規格化定数である。以下の問いに答えよ。

(1) ガウス積分の公式 $\int_{-\infty}^\infty e^{-u^2} du = \sqrt{\pi}$ を用いて，規格化条件 $\int_{-\infty}^\infty f(x) dx = 1$ を満たす定数 $C$ を求めよ。

(2) 期待値 $E[X - \mu]$ が $0$ になることを示せ。

(3) 分散 $V[X] = E[(X-\mu)^2]$ を部分積分を用いて求めよ。

---

## 解答・解説

### (1)
確率密度関数の形状を図に示します。

<!-- FIGURE solution (1): 横軸x，縦軸f(x)のガウス曲線。平均値x=muを中心とした左右対称の釣り鐘型で，最大値f(mu)=Cを示す。 -->

全区間における規格化条件の式を立てます。

$$
\int_{-\infty}^\infty f(x) dx = C \int_{-\infty}^\infty \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) dx = 1
$$

変数変換 $u = \frac{x-\mu}{\sqrt{2}\sigma}$ を行うと，$dx = \sqrt{2}\sigma du$ となり，積分範囲は変わらず $(-\infty, \infty)$ です。積分に代入すると，

$$
\begin{aligned}
C \int_{-\infty}^\infty e^{-u^2} \sqrt{2}\sigma du &= C \sqrt{2}\sigma \int_{-\infty}^\infty e^{-u^2} du \\
&= C \sqrt{2}\sigma \cdot \sqrt{\pi} \\
&= C \sqrt{2\pi}\sigma
\end{aligned}
$$

となります。これが $1$ に等しいため，

$$
\finalanswer{C = \frac{1}{\sqrt{2\pi}\sigma}}
$$

となります。

### (2)
期待値の定義式に基づいて積分を記述します。

$$
E[X - \mu] = \frac{1}{\sqrt{2\pi}\sigma} \int_{-\infty}^\infty (x-\mu) \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) dx
$$

ここで $y = x - \mu$ と変数変換を行うと，$dx = dy$ となり，積分は次の形になります。

$$
E[X - \mu] = \frac{1}{\sqrt{2\pi}\sigma} \int_{-\infty}^\infty y \exp\left(-\frac{y^2}{2\sigma^2}\right) dy
$$

被積分関数 $g(y) = y \exp\left(-\frac{y^2}{2\sigma^2}\right)$ を考えると，$g(-y) = -g(y)$ であり奇関数です。対称区間 $(-\infty, \infty)$ 上での奇関数の積分は $0$ となるため，

$$
\finalanswer{E[X - \mu] = 0}
$$

となります。

### (3)
分散は $y = x-\mu$ の変数変換を用いると次のように表されます。

$$
V[X] = E[(X-\mu)^2] = \frac{1}{\sqrt{2\pi}\sigma} \int_{-\infty}^\infty y^2 \exp\left(-\frac{y^2}{2\sigma^2}\right) dy
$$

被積分関数を $y \cdot \left[ y \exp\left(-\frac{y^2}{2\sigma^2}\right) \right]$ と分解し，部分積分法を適用します。微分すると元の指数因子に戻る関係，

$$
\frac{d}{dy} \left[ -\sigma^2 \exp\left(-\frac{y^2}{2\sigma^2}\right) \right] = y \exp\left(-\frac{y^2}{2\sigma^2}\right)
$$

を利用すると，

$$
\int_{-\infty}^\infty y^2 \exp\left(-\frac{y^2}{2\sigma^2}\right) dy = \left[ -y \sigma^2 \exp\left(-\frac{y^2}{2\sigma^2}\right) \right]_{-\infty}^\infty + \sigma^2 \int_{-\infty}^\infty \exp\left(-\frac{y^2}{2\sigma^2}\right) dy
$$

となります。第1項の境界値は指数減衰が勝るため $0$ です。第2項の積分は (1) より $\sqrt{2\pi}\sigma$ と求まっているため，

$$
\int_{-\infty}^\infty y^2 \exp\left(-\frac{y^2}{2\sigma^2}\right) dy = 0 + \sigma^2 \cdot \sqrt{2\pi}\sigma = \sqrt{2\pi}\sigma^3
$$

となります。これを分散の式に代入すると，

$$
\begin{aligned}
V[X] &= \frac{1}{\sqrt{2\pi}\sigma} \cdot \sqrt{2\pi}\sigma^3 \\
&= \finalanswer{\sigma^2}
\end{aligned}
$$

となります。

===== FILE: 13probability_statistics/02/02_040.md =====
---
tags:
  - 標準
---

# 指数分布と待ち時間

## 問題
事象が発生するまでの待ち時間を表す連続型確率変数 $T$ の確率密度関数が，正の実数 $\lambda$ を用いて
$$
f(t) = \lambda e^{-\lambda t} \quad (t \ge 0)
$$
で与えられている（$t < 0$ では $f(t) = 0$）。以下の問いに答えよ。

(1) $t \ge 0$ に対し，待ち時間が $t$ を超える確率 $P(T > t)$ を求めよ。

(2) 任意の $s \ge 0, t \ge 0$ に対し，条件付き確率 $P(T > s + t \mid T > s)$ が $P(T > t)$ に等しいことを示せ。

(3) 期待値 $E[T] = \frac{1}{\lambda}$ を用いて，事象が期待値以上の時間発生しない確率 $P(T > E[T])$ を求めよ。

---

## 解答・解説

### (1)
待ち時間が $t$ より大きくなる確率は，確率密度関数を $t$ から無限大まで積分することにより求まります。

$$
P(T > t) = \int_t^\infty f(\tau) d\tau = \int_t^\infty \lambda e^{-\lambda \tau} d\tau
$$

この積分を実行します。

$$
\begin{aligned}
P(T > t) &= \left[ -e^{-\lambda \tau} \right]_t^\infty \\
&= 0 - (-e^{-\lambda t}) \\
&= \finalanswer{e^{-\lambda t}}
\end{aligned}
$$

となります。この関数は生存関数と呼ばれます。

### (2)
条件付き確率の定義式を適用します。

$$
P(T > s + t \mid T > s) = \frac{P(T > s + t \cap T > s)}{P(T > s)}
$$

$s \ge 0$ かつ $t \ge 0$ であるため，$s + t \ge s$ です。したがって，$T > s + t$ である事象は自動的に $T > s$ を満たし，共通部分は積事象 $T > s + t$ そのものになります。

$$
P(T > s + t \cap T > s) = P(T > s + t)
$$

(1) で求めた確率の式を代入します。

$$
\begin{aligned}
P(T > s + t \mid T > s) &= \frac{P(T > s + t)}{P(T > s)} \\
&= \frac{e^{-\lambda (s+t)}}{e^{-\lambda s}} \\
&= e^{-\lambda t}
\end{aligned}
$$

(1) の結果より $e^{-\lambda t} = P(T > t)$ であるため，

$$
\finalanswer{P(T > s + t \mid T > s) = P(T > t)}
$$

となります。すでに時刻 $s$ まで事象が起こらなかったという条件のもとで，さらに時間 $t$ 待つ確率は，初期状態から時間 $t$ 待つ確率と等しくなります。この性質は無記憶性と呼ばれます。

### (3)
期待値は $E[T] = \frac{1}{\lambda}$ です。(1) で求めた生存関数の式に $t = E[T] = \frac{1}{\lambda}$ を代入します。

$$
\begin{aligned}
P(T > E[T]) &= e^{-\lambda \cdot \frac{1}{\lambda}} \\
&= e^{-1} \\
&= \finalanswer{\frac{1}{e}}
\end{aligned}
$$

となります。待ち時間が平均値を超える確率はパラメータ $\lambda$ によらず一定値となり，その値はおよそ $0.368$ です。

===== FILE: 13probability_statistics/02/02_050.md =====
---
tags:
  - 標準
---

# 確率変数の変換

## 問題
実数値をとる連続型確率変数 $X$ の確率密度関数を $f_X(x)$ とする。狭義単調増加で微分可能な関数 $g(x)$ による変数変換 $Y = g(X)$ を考える。以下の問いに答えよ。

(1) $Y$ の累積分布関数 $F_Y(y) = P(Y \le y)$ を $X$ の累積分布関数を用いて表し，それを $y$ で微分することにより，$Y$ の確率密度関数 $f_Y(y)$ を $f_X$ および $g^{-1}$ を用いて表せ。

(2) 区間 $(0, 1)$ 上の一様分布に従う確率変数 $U$（区間内で $f_U(u) = 1$，区間外で $0$）に対し，$X = -\frac{1}{\lambda} \ln U$（$\lambda > 0$）の確率密度関数 $f_X(x)$（$x > 0$）を求めよ。

(3) 標準正規分布に従う確率変数 $Z$（確率密度関数 $f_Z(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$）に対し，$W = Z^2$ の確率密度関数 $f_W(w)$（$w > 0$）を求めよ。

---

## 解答・解説

### (1)
$g(x)$ は狭義単調増加であるため，逆関数 $g^{-1}(y)$ が一意に存在し，不等式 $g(X) \le y$ は $X \le g^{-1}(y)$ と同値です。したがって $Y$ の累積分布関数は，

$$
F_Y(y) = P(Y \le y) = P(X \le g^{-1}(y)) = F_X(g^{-1}(y))
$$

となります。確率密度関数は累積分布関数の導関数であるため，合成関数の微分公式を適用します。

$$
\begin{aligned}
f_Y(y) &= \frac{d}{dy} F_Y(y) \\
&= \frac{d}{dy} F_X(g^{-1}(y)) \\
&= F_X'(g^{-1}(y)) \frac{d g^{-1}(y)}{dy} \\
&= \finalanswer{f_X(g^{-1}(y)) \frac{d g^{-1}(y)}{dy}}
\end{aligned}
$$

となります。

### (2)
$X = -\frac{1}{\lambda} \ln U$ を $U$ について解くと，$U = e^{-\lambda X}$ となります。$0 < U < 1$ に対応する $X$ の定義域は $x > 0$ です。この変換関数は単調減少であるため，累積分布関数を慎重に立てます。

$$
F_X(x) = P(X \le x) = P\left( -\frac{1}{\lambda}\ln U \le x \right)
$$

両辺に $-\lambda$ を掛けると不等号の向きが反転します。

$$
F_X(x) = P(\ln U \ge -\lambda x) = P(U \ge e^{-\lambda x})
$$

$U$ は $(0, 1)$ 上の一様分布に従うため，任意の $u \in (0, 1)$ に対し $P(U \ge u) = 1 - u$ です。したがって，

$$
F_X(x) = 1 - e^{-\lambda x}
$$

となります。これを $x$ で微分して確率密度関数を求めると，

$$
\begin{aligned}
f_X(x) &= \frac{d}{dx} (1 - e^{-\lambda x}) \\
&= \finalanswer{\lambda e^{-\lambda x}}
\end{aligned}
$$

となります。一様乱数から対数変換によって指数分布が生成されます。

### (3)
$W = Z^2$ に対し，$w > 0$ での累積分布関数を考えます。

$$
F_W(w) = P(W \le w) = P(Z^2 \le w) = P(-\sqrt{w} \le Z \le \sqrt{w})
$$

標準正規分布の対称性を用いると，この確率は正の領域の積分を2倍したものとして表せます。

$$
F_W(w) = \int_{-\sqrt{w}}^{\sqrt{w}} f_Z(z) dz = 2 \int_0^{\sqrt{w}} f_Z(z) dz
$$

これを $w$ について微分します。微積分学の基本定理と合成関数の微分法を用いると，

$$
f_W(w) = \frac{d}{dw} \left[ 2 \int_0^{\sqrt{w}} f_Z(z) dz \right] = 2 f_Z(\sqrt{w}) \frac{d}{dw}(\sqrt{w}) = 2 f_Z(\sqrt{w}) \frac{1}{2\sqrt{w}} = \frac{f_Z(\sqrt{w})}{\sqrt{w}}
$$

となります。$f_Z(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ を代入すると，

$$
\finalanswer{f_W(w) = \frac{1}{\sqrt{2\pi w}} e^{-w/2}}
$$

となります。これは自由度1のカイ二乗分布の密度関数に一致します。

===== FILE: 13probability_statistics/02/02_060.md =====
---
tags:
  - 標準
---

# マクスウェル速度分布

## 問題
絶対温度 $T$ の熱平衡状態にある質量 $m$ の希薄気体分子の速度ベクトル $\boldsymbol{v} = (v_x, v_y, v_z)$ を考える。各速度成分 $v_i$（$i = x, y, z$）は互いに独立であり，同一の確率密度関数
$$
f_1(v_i) = \left(\frac{m}{2\pi k_B T}\right)^{1/2} \exp\left(-\frac{m v_i^2}{2 k_B T}\right) \quad (-\infty < v_i < \infty)
$$
に従う。ここで $k_B$ はボルツマン定数である。以下の問いに答えよ。

(1) 速度ベクトルの3次元同時確率密度関数 $f_{\boldsymbol{v}}(\boldsymbol{v}) = f_{\boldsymbol{v}}(v_x, v_y, v_z)$ を求めよ。

(2) 速度空間における球座標変換を用いて，分子の速さ $v = |\boldsymbol{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}$ の確率密度関数 $F(v)$（$v \ge 0$）を求めよ。

(3) 確率密度関数 $F(v)$ が最大値をとる最頻速度 $v_p$ を求めよ。

---

## 解答・解説

### (1)
3つの速度成分 $v_x, v_y, v_z$ は互いに独立であるため，同時確率密度関数はそれぞれの周辺確率密度関数の積として与えられます。

$$
f_{\boldsymbol{v}}(v_x, v_y, v_z) = f_1(v_x) f_1(v_y) f_1(v_z)
$$

各成分の分布関数を代入すると，

$$
\begin{aligned}
f_{\boldsymbol{v}}(v_x, v_y, v_z) &= \left(\frac{m}{2\pi k_B T}\right)^{1/2} e^{-\frac{m v_x^2}{2k_B T}} \left(\frac{m}{2\pi k_B T}\right)^{1/2} e^{-\frac{m v_y^2}{2k_B T}} \left(\frac{m}{2\pi k_B T}\right)^{1/2} e^{-\frac{m v_z^2}{2k_B T}} \\
&= \finalanswer{\left(\frac{m}{2\pi k_B T}\right)^{3/2} \exp\left(-\frac{m(v_x^2 + v_y^2 + v_z^2)}{2 k_B T}\right)}
\end{aligned}
$$

となります。

### (2)
速さの確率密度関数の概形を図に示します。

<!-- FIGURE solution (2): 横軸を速さv，縦軸をF(v)とするグラフ。原点O(0,0)から2次関数的に立ち上がり，最頻速度v=v_pで極大値をとって裾野が指数関数的に減衰する曲線。 -->

速度空間における微小体積要素 $dv_x dv_y dv_z$ 内に速度ベクトルが存在する確率は $f_{\boldsymbol{v}}(\boldsymbol{v}) dv_x dv_y dv_z$ です。速さが $v$ から $v + dv$ の間にある確率は，速度空間において半径 $v$，厚み $dv$ の球殻に含まれる確率と等しくなります。球殻の体積要素は角度成分を積分することにより $4\pi v^2 dv$ となります。したがって，

$$
F(v) dv = f_{\boldsymbol{v}}(\boldsymbol{v}) \cdot 4\pi v^2 dv
$$

が成り立ちます。$v^2 = v_x^2 + v_y^2 + v_z^2$ であるため，(1) の結果を代入すると，

$$
\finalanswer{F(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 \exp\left(-\frac{m v^2}{2 k_B T}\right)}
$$

となります。

### (3)
$F(v)$ を最大にする $v$ を求めるため，$\alpha = \frac{m}{2k_B T}$ とおいて $F(v)$ を $v$ で微分します。

$$
F(v) = 4\pi \left(\frac{\alpha}{\pi}\right)^{3/2} v^2 e^{-\alpha v^2}
$$

$g(v) = v^2 e^{-\alpha v^2}$ の極値を求めます。積の微分公式を用いると，

$$
\begin{aligned}
\frac{d g(v)}{dv} &= 2v e^{-\alpha v^2} + v^2 (-2\alpha v) e^{-\alpha v^2} \\
&= 2v (1 - \alpha v^2) e^{-\alpha v^2}
\end{aligned}
$$

となります。$v > 0$ において導関数が $0$ となる条件は，括弧の中身が $0$ になることです。

$$
1 - \alpha v^2 = 0 \implies v^2 = \frac{1}{\alpha}
$$

$v > 0$ であるため極大点を与える速度は $v = \frac{1}{\sqrt{\alpha}}$ です。$\alpha = \frac{m}{2k_B T}$ を代入すると，

$$
\finalanswer{v_p = \sqrt{\frac{2 k_B T}{m}}}
$$

となります。

===== FILE: 13probability_statistics/03/03_010.md =====
---
tags:
  - 標準
---

# チェビシェフの不等式と大数の法則

## 問題
確率変数 $X$ の期待値を $\mu$，分散を $\sigma^2$（$> 0$）とする。以下の問いに答えよ。

(1) 任意の正の定数 $\epsilon > 0$ に対し，チェビシェフの不等式
$$
P(|X - \mu| \ge \epsilon) \le \frac{\sigma^2}{\epsilon^2}
$$
が成り立つことを示せ。

(2) 互いに独立に同一の分布（平均 $\mu$，分散 $\sigma^2$）に従う $n$ 個の確率変数 $X_1, X_2, \dots, X_n$ を考える。標本平均 $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$ の分散 $V[\bar{X}_n]$ を求めよ。

(3) チェビシェフの不等式を標本平均 $\bar{X}_n$ に適用し，任意の $\epsilon > 0$ に対して $\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) = 0$（大数の弱法則）が成り立つことを示せ。

---

## 解答・解説

### (1)
連続型確率変数の場合について示します（離散型の場合も積分を和に置き換えることで同様に成り立ちます）。確率密度関数を $f(x)$ とすると，分散の定義は，

$$
\sigma^2 = \int_{-\infty}^\infty (x - \mu)^2 f(x) dx
$$

です。積分範囲を $|x - \mu| \ge \epsilon$ の領域と $|x - \mu| < \epsilon$ の領域に分割します。被積分関数は常に非負であるため，領域を狭めると値は小さくなります。

$$
\sigma^2 \ge \int_{|x - \mu| \ge \epsilon} (x - \mu)^2 f(x) dx
$$

この積分領域内では常に $(x - \mu)^2 \ge \epsilon^2$ が成立します。したがって，

$$
\sigma^2 \ge \epsilon^2 \int_{|x - \mu| \ge \epsilon} f(x) dx
$$

となります。右辺の積分は確率の定義より $P(|X - \mu| \ge \epsilon)$ そのものです。

$$
\sigma^2 \ge \epsilon^2 P(|X - \mu| \ge \epsilon)
$$

両辺を正の数 $\epsilon^2$ で割ると，

$$
\finalanswer{P(|X - \mu| \ge \epsilon) \le \frac{\sigma^2}{\epsilon^2}}
$$

となります。

### (2)
標本平均の定義に従って分散の演算を行います。定数の二乗が外に出る性質を用いると，

$$
V[\bar{X}_n] = V\left[ \frac{1}{n} \sum_{i=1}^n X_i \right] = \frac{1}{n^2} V\left[ \sum_{i=1}^n X_i \right]
$$

となります。各確率変数 $X_i$ は互いに独立であるため，和の分散は個々の分散の和に等しくなります。

$$
V\left[ \sum_{i=1}^n X_i \right] = \sum_{i=1}^n V[X_i] = \sum_{i=1}^n \sigma^2 = n\sigma^2
$$

これを代入すると，

$$
\begin{aligned}
V[\bar{X}_n] &= \frac{1}{n^2} (n\sigma^2) \\
&= \finalanswer{\frac{\sigma^2}{n}}
\end{aligned}
$$

となります。標本サイズ $n$ が大きくなるにつれて，標本平均のばらつきは $1/n$ で減少します。

### (3)
期待値の線形性により，$E[\bar{X}_n] = \frac{1}{n}\sum_{i=1}^n E[X_i] = \mu$ です。チェビシェフの不等式を確率変数 $\bar{X}_n$ に対して適用します。

$$
P(|\bar{X}_n - \mu| \ge \epsilon) \le \frac{V[\bar{X}_n]}{\epsilon^2}
$$

(2) で求めた分散 $V[\bar{X}_n] = \frac{\sigma^2}{n}$ を代入すると，

$$
0 \le P(|\bar{X}_n - \mu| \ge \epsilon) \le \frac{\sigma^2}{n \epsilon^2}
$$

となります。ここで $\epsilon$ と $\sigma$ は $n$ に依存しない固定された正の定数であるため，$n \to \infty$ の極限で最右辺は $0$ に収束します。

$$
\lim_{n \to \infty} \frac{\sigma^2}{n \epsilon^2} = 0
$$

はさみうちの原理により，不等式で挟まれた確率の極限も $0$ となります。したがって，

$$
\finalanswer{\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) = 0}
$$

となります。

===== FILE: 13probability_statistics/03/03_020.md =====
---
tags:
  - 発展
---

# 中心極限定理

## 問題
互いに独立に同一の分布に従う確率変数列 $X_1, X_2, \dots$ があり，各 $X_j$ の期待値は $0$，分散は $\sigma^2$（$\sigma > 0$）であるとする。規格化された和
$$
Z_n = \frac{1}{\sqrt{n}\sigma} \sum_{j=1}^n X_j
$$
の漸近挙動を特性関数を用いて考える。以下の問いに答えよ。

(1) 各 $X_j$ の特性関数 $\phi_X(t) = E[e^{itX_j}]$ を原点 $t = 0$ のまわりで $t^2$ の項まで展開せよ。

(2) $Z_n$ の特性関数 $\phi_{Z_n}(t) = E[e^{it Z_n}]$ を，$\phi_X$ を用いて表せ。

(3) $n \to \infty$ における極限 $\lim_{n \to \infty} \phi_{Z_n}(t)$ を求めよ。

---

## 解答・解説

### (1)
指数関数 $e^{itX_j}$ を原点まわりでテイラー展開します。

$$
e^{itX_j} = 1 + itX_j + \frac{(itX_j)^2}{2!} + o(t^2) = 1 + itX_j - \frac{t^2}{2} X_j^2 + o(t^2)
$$

両辺の期待値をとります。期待値の線形性を用いると，

$$
\phi_X(t) = E[e^{itX_j}] = 1 + it E[X_j] - \frac{t^2}{2} E[X_j^2] + o(t^2)
$$

となります。問題文の条件より $E[X_j] = 0$，$E[X_j^2] = V[X_j] + (E[X_j])^2 = \sigma^2$ です。これらを代入すると，

$$
\finalanswer{\phi_X(t) = 1 - \frac{\sigma^2 t^2}{2} + o(t^2)}
$$

となります。

### (2)
$Z_n$ の定義式を特性関数の定義に代入します。

$$
\phi_{Z_n}(t) = E\left[ \exp\left( it \frac{1}{\sqrt{n}\sigma} \sum_{j=1}^n X_j \right) \right] = E\left[ \prod_{j=1}^n \exp\left( \frac{it}{\sqrt{n}\sigma} X_j \right) \right]
$$

$X_1, X_2, \dots, X_n$ は互いに独立であるため，積の期待値は期待値の積に分解されます。

$$
\phi_{Z_n}(t) = \prod_{j=1}^n E\left[ \exp\left( \frac{it}{\sqrt{n}\sigma} X_j \right) \right]
$$

各 $X_j$ は同一の分布に従うため，すべての因子は同一の特性関数で評価されます。したがって，

$$
\finalanswer{\phi_{Z_n}(t) = \left[ \phi_X\left( \frac{t}{\sqrt{n}\sigma} \right) \right]^n}
$$

となります。

### (3)
(1) で求めた展開式に引数 $\frac{t}{\sqrt{n}\sigma}$ を代入します。

$$
\phi_X\left( \frac{t}{\sqrt{n}\sigma} \right) = 1 - \frac{\sigma^2}{2} \left( \frac{t}{\sqrt{n}\sigma} \right)^2 + o\left( \frac{1}{n} \right) = 1 - \frac{t^2}{2n} + o\left( \frac{1}{n} \right)
$$

これを (2) の式に代入し，$n \to \infty$ の極限を考えます。

$$
\phi_{Z_n}(t) = \left( 1 - \frac{t^2}{2n} + o\left( \frac{1}{n} \right) \right)^n
$$

実数 $a$ に対する基本的な極限定理 $\lim_{n \to \infty} \left( 1 + \frac{a}{n} + o\left(\frac{1}{n}\right) \right)^n = e^a$ を適用します。ここで $a = -\frac{t^2}{2}$ とみなすと，

$$
\begin{aligned}
\lim_{n \to \infty} \phi_{Z_n}(t) &= \lim_{n \to \infty} \left( 1 - \frac{t^2 / 2}{n} + o\left( \frac{1}{n} \right) \right)^n \\
&= \finalanswer{e^{-t^2/2}}
\end{aligned}
$$

となります。この極限値は標準正規分布 $N(0, 1)$ の特性関数と完全に一致します。

===== FILE: 13probability_statistics/03/03_030.md =====
---
tags:
  - 標準
---

# 1次元ランダムウォーク

## 問題
直線上を運動する粒子が，単位時間ごとに独立に，確率 $p$ で $+a$，確率 $q = 1-p$ で $-a$（$a > 0$）だけ移動する（図）。$i$ 回目の移動量を $S_i$ とし，$n$ ステップ後の粒子の位置を $X_n = \sum_{i=1}^n S_i$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 数直線の原点Oと，粒子が確率pで右へ距離a，確率qで左へ距離aジャンプする様子を示す矢印。 -->

(1) 1ステップあたりの移動量 $S_i$ の期待値 $E[S_i]$ を求めよ。

(2) $n$ ステップ後の位置 $X_n$ の期待値 $E[X_n]$ を求めよ。

(3) $n$ ステップ後の位置 $X_n$ の分散 $V[X_n]$ を求めよ。

---

## 解答・解説

### (1)
確率変数 $S_i$ がとる値は $+a$ と $-a$ の2通りです。離散確率変数の期待値の定義式に基づいて計算します。

$$
E[S_i] = a \cdot P(S_i = a) + (-a) \cdot P(S_i = -a)
$$

与えられた確率を代入すると，

$$
\begin{aligned}
E[S_i] &= a p + (-a) q \\
&= (p - q)a
\end{aligned}
$$

となります。$q = 1-p$ を代入して $p$ のみで表すと，

$$
\finalanswer{E[S_i] = (2p - 1)a}
$$

となります。

### (2)
粒子の位置は $n$ 個の独立なステップの和 $X_n = \sum_{i=1}^n S_i$ で表されます。期待値の線形性を適用すると，

$$
E[X_n] = E\left[ \sum_{i=1}^n S_i \right] = \sum_{i=1}^n E[S_i]
$$

となります。(1) で求めた期待値 $E[S_i] = (2p-1)a$ を代入すると，

$$
\begin{aligned}
E[X_n] &= \sum_{i=1}^n (2p - 1)a \\
&= \finalanswer{n(2p - 1)a}
\end{aligned}
$$

となります。対称なランダムウォーク（$p = 1/2$）では期待値は $0$ となります。

### (3)
まず 1 ステップの分散 $V[S_i] = E[S_i^2] - (E[S_i])^2$ を計算します。$S_i^2$ の期待値は，

$$
E[S_i^2] = a^2 p + (-a)^2 q = a^2(p + q) = a^2
$$

となります。したがって $S_i$ の分散は，

$$
\begin{aligned}
V[S_i] &= a^2 - ((p - q)a)^2 \\
&= a^2 (1 - (p - q)^2)
\end{aligned}
$$

となります。ここで $p + q = 1$ より $1 - (p-q)^2 = (p+q)^2 - (p-q)^2 = 4pq$ が成り立ちます。

$$
V[S_i] = 4pq a^2
$$

各ステップ $S_i$ は互いに独立であるため，和の分散は個々の分散の和に等しくなります。

$$
\begin{aligned}
V[X_n] &= \sum_{i=1}^n V[S_i] \\
&= \sum_{i=1}^n 4pq a^2 \\
&= \finalanswer{4npq a^2}
\end{aligned}
$$

となります。対称な場合（$p = q = 1/2$）は $V[X_n] = n a^2$ となり，粒子が広がる幅を表す標準偏差は $\sqrt{n}a$ に比例して増大します。

===== FILE: 13probability_statistics/03/03_040.md =====
---
tags:
  - 標準
---

# ランダムウォークと拡散方程式

## 問題
1次元格子（格子間隔 $\Delta x$）上を，微小時間 $\Delta t$ ごとに確率 $1/2$ で左右いずれかに距離 $\Delta x$ だけジャンプする対称ランダムウォークを考える（図）。時刻 $t$ において粒子が位置 $x$ に存在する確率を $P(x, t)$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 1次元格子の点x-Δx, x, x+Δxと，両隣の格子点から点xへ確率1/2で遷移する様子を示す矢印。 -->

(1) 時刻 $t + \Delta t$ における確率 $P(x, t+\Delta t)$ を，$P(x - \Delta x, t)$ および $P(x + \Delta x, t)$ を用いた差分方程式で表せ。

(2) $P(x, t)$ が十分滑らかであるとして，$P(x, t+\Delta t)$ を $t$ について，$P(x \pm \Delta x, t)$ を $x$ についてテイラー展開せよ。

(3) $\Delta t$ および $(\Delta x)^2$ の1次の微小項を残し，比 $D = \frac{(\Delta x)^2}{2\Delta t}$ を有限に保ったまま $\Delta x \to 0, \Delta t \to 0$ の連続極限をとることにより，拡散方程式を導け。

---

## 解答・解説

### (1)
粒子が時刻 $t + \Delta t$ に位置 $x$ に存在するためには，時刻 $t$ に左隣の格子点 $x - \Delta x$ にいて右にジャンプするか，または右隣の格子点 $x + \Delta x$ にいて左にジャンプするかのいずれかでなければなりません。左右への遷移確率はそれぞれ $1/2$ であるため，全確率の公式より次の漸化式が得られます。

$$
\finalanswer{P(x, t+\Delta t) = \frac{1}{2} P(x - \Delta x, t) + \frac{1}{2} P(x + \Delta x, t)}
$$

となります。

### (2)
$P(x, t)$ を周りでテイラー展開します。左辺の関数を時間 $t$ について1次まで展開すると，

$$
P(x, t+\Delta t) = P(x, t) + \frac{\partial P(x, t)}{\partial t} \Delta t + O((\Delta t)^2)
$$

となります。右辺に現れる空間依存の項を $x$ の周りで2次の項までテイラー展開します。

$$
P(x + \Delta x, t) = P(x, t) + \frac{\partial P(x, t)}{\partial x} \Delta x + \frac{1}{2} \frac{\partial^2 P(x, t)}{\partial x^2} (\Delta x)^2 + O((\Delta x)^3)
$$

$$
P(x - \Delta x, t) = P(x, t) - \frac{\partial P(x, t)}{\partial x} \Delta x + \frac{1}{2} \frac{\partial^2 P(x, t)}{\partial x^2} (\Delta x)^2 + O((\Delta x)^3)
$$

となります。

### (3)
(2) で求めた空間の2つの展開式の平均をとります。1次の導関数を含む項は互いに符号が異なり相殺されます。

$$
\frac{1}{2} P(x - \Delta x, t) + \frac{1}{2} P(x + \Delta x, t) = P(x, t) + \frac{1}{2} \frac{\partial^2 P(x, t)}{\partial x^2} (\Delta x)^2 + O((\Delta x)^4)
$$

これを (1) の差分方程式の右辺に代入し，時間の展開式と等置します。

$$
P(x, t) + \frac{\partial P(x, t)}{\partial t} \Delta t = P(x, t) + \frac{1}{2} \frac{\partial^2 P(x, t)}{\partial x^2} (\Delta x)^2
$$

両辺から共通項 $P(x, t)$ を引き，両辺を $\Delta t$ で割ります。

$$
\frac{\partial P(x, t)}{\partial t} = \frac{(\Delta x)^2}{2\Delta t} \frac{\partial^2 P(x, t)}{\partial x^2}
$$

拡散係数を $D = \frac{(\Delta x)^2}{2\Delta t}$ と定義し，この値を有限に保ったまま $\Delta x \to 0$ かつ $\Delta t \to 0$ の極限をとると，

$$
\finalanswer{\frac{\partial P}{\partial t} = D \frac{\partial^2 P}{\partial x^2}}
$$

となります。微視的な粒子の不規則運動の連続極限としてマクロな拡散方程式が導出されます。

===== FILE: 13probability_statistics/04/04_010.md =====
---
tags:
  - 基本
---

# 標本平均と不偏分散

## 問題
平均 $\mu$，分散 $\sigma^2$ をもつ同一の母集団から，互いに独立に抽出された大きさ $n$（$n \ge 2$）の無作為標本 $X_1, X_2, \dots, X_n$ を考える。標本平均を $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ とする。以下の問いに答えよ。

(1) 等式 $\sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i - \mu)^2 - n(\bar{X} - \mu)^2$ が成り立つことを示せ。

(2) 偏差平方和の期待値 $E\left[\sum_{i=1}^n (X_i - \bar{X})^2\right]$ を求めよ。

(3) 不偏分散 $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ の期待値 $E[S^2]$ が母分散 $\sigma^2$ に等しくなることを示せ。

---

## 解答・解説

### (1)
各偏差の項に母平均 $\mu$ を挿入して2つに分離します。

$$
X_i - \bar{X} = (X_i - \mu) - (\bar{X} - \mu)
$$

両辺を2乗して $i = 1$ から $n$ までの総和をとります。

$$
\begin{aligned}
\sum_{i=1}^n (X_i - \bar{X})^2 &= \sum_{i=1}^n \left[ (X_i - \mu) - (\bar{X} - \mu) \right]^2 \\
&= \sum_{i=1}^n (X_i - \mu)^2 - 2(\bar{X} - \mu) \sum_{i=1}^n (X_i - \mu) + \sum_{i=1}^n (\bar{X} - \mu)^2
\end{aligned}
$$

ここで標本平均の定義より $\sum_{i=1}^n X_i = n\bar{X}$ であるため，交差項の和は次のようになります。

$$
\sum_{i=1}^n (X_i - \mu) = \sum_{i=1}^n X_i - n\mu = n(\bar{X} - \mu)
$$

また最右項は $i$ に依存しない定数の $n$ 個の和であるため $n(\bar{X} - \mu)^2$ です。これらを代入すると，

$$
\begin{aligned}
\sum_{i=1}^n (X_i - \bar{X})^2 &= \sum_{i=1}^n (X_i - \mu)^2 - 2(\bar{X} - \mu) \cdot n(\bar{X} - \mu) + n(\bar{X} - \mu)^2 \\
&= \sum_{i=1}^n (X_i - \mu)^2 - 2n(\bar{X} - \mu)^2 + n(\bar{X} - \mu)^2 \\
&= \finalanswer{\sum_{i=1}^n (X_i - \mu)^2 - n(\bar{X} - \mu)^2}
\end{aligned}
$$

となります。

### (2)
(1) で得られた等式の両辺の期待値をとります。

$$
E\left[ \sum_{i=1}^n (X_i - \bar{X})^2 \right] = \sum_{i=1}^n E[(X_i - \mu)^2] - n E[(\bar{X} - \mu)^2]
$$

母分散の定義より，各標本について $E[(X_i - \mu)^2] = \sigma^2$ です。また $\bar{X}$ の期待値は $\mu$ であるため，$E[(\bar{X} - \mu)^2] = V[\bar{X}]$ です。標本平均の分散は $V[\bar{X}] = \frac{\sigma^2}{n}$ であるため，代入すると，

$$
\begin{aligned}
E\left[ \sum_{i=1}^n (X_i - \bar{X})^2 \right] &= \sum_{i=1}^n \sigma^2 - n \left( \frac{\sigma^2}{n} \right) \\
&= n\sigma^2 - \sigma^2 \\
&= \finalanswer{(n-1)\sigma^2}
\end{aligned}
$$

となります。未知の母平均 $\mu$ の代わりに標本平均 $\bar{X}$ を用いることで，自由度が1つ失われます。

### (3)
不偏分散の定義式に期待値の線形性を適用します。

$$
E[S^2] = E\left[ \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2 \right] = \frac{1}{n-1} E\left[ \sum_{i=1}^n (X_i - \bar{X})^2 \right]
$$

(2) で得られた期待値 $(n-1)\sigma^2$ を代入します。

$$
\begin{aligned}
E[S^2] &= \frac{1}{n-1} \cdot (n-1)\sigma^2 \\
&= \finalanswer{\sigma^2}
\end{aligned}
$$

となります。偏差平方和を $n$ ではなく $n-1$ で割ることにより，その期待値が厳密に母分散と一致する不偏推定量が得られます。

===== FILE: 13probability_statistics/04/04_020.md =====
---
tags:
  - 標準
---

# 最尤推定

## 問題
(1) 平均 $\lambda$（$\lambda > 0$）のポアソン分布に従う母集団から，互いに独立に得られた $n$ 個の標本 $k_1, k_2, \dots, k_n$ に対する対数尤度関数 $\ln L(\lambda)$ を求めよ。

(2) 対数尤度関数の停留条件 $\frac{d \ln L}{d\lambda} = 0$ から，パラメータ $\lambda$ の最尤推定量 $\hat{\lambda}$ を求めよ。

(3) 平均 $\mu$，既知の分散 $\sigma^2$ をもつ正規分布に従う母集団から，互いに独立に得られた $n$ 個の標本 $x_1, x_2, \dots, x_n$ に対し，対数尤度関数を最大化することで平均 $\mu$ の最尤推定量 $\hat{\mu}$ を求めよ。

---

## 解答・解説

### (1)
各標本値 $k_i$ が出現する確率は $P(k_i) = \frac{\lambda^{k_i} e^{-\lambda}}{k_i!}$ です。標本は互いに独立に得られるため，尤度関数 $L(\lambda)$ は各確率の積として表されます。

$$
L(\lambda) = \prod_{i=1}^n \frac{\lambda^{k_i} e^{-\lambda}}{k_i!}
$$

両辺の自然対数をとると，積の対数は対数の和になります。

$$
\begin{aligned}
\ln L(\lambda) &= \sum_{i=1}^n \ln\left( \frac{\lambda^{k_i} e^{-\lambda}}{k_i!} \right) \\
&= \sum_{i=1}^n \left( k_i \ln\lambda - \lambda - \ln(k_i!) \right)
\end{aligned}
$$

和を項ごとにまとめると，

$$
\finalanswer{\ln L(\lambda) = \left( \sum_{i=1}^n k_i \right) \ln\lambda - n\lambda - \sum_{i=1}^n \ln(k_i!)}
$$

となります。

### (2)
(1) で得られた対数尤度関数を $\lambda$ について微分します。最右項は $\lambda$ に依存しないため微分すると $0$ です。

$$
\frac{d \ln L(\lambda)}{d\lambda} = \frac{1}{\lambda} \sum_{i=1}^n k_i - n
$$

これを $0$ とおく停留条件を課します。

$$
\frac{1}{\hat{\lambda}} \sum_{i=1}^n k_i - n = 0
$$

両辺に $\hat{\lambda}$ を掛けて整理すると，

$$
\finalanswer{\hat{\lambda} = \frac{1}{n} \sum_{i=1}^n k_i}
$$

となります。ポアソン分布の母平均の最尤推定量は標本平均に一致します。

### (3)
正規分布 $N(\mu, \sigma^2)$ に対する同時確率密度から尤度関数を構成します。

$$
L(\mu) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(x_i - \mu)^2}{2\sigma^2} \right)
$$

両辺の自然対数をとると，

$$
\begin{aligned}
\ln L(\mu) &= \sum_{i=1}^n \left[ -\ln(\sqrt{2\pi}\sigma) - \frac{(x_i - \mu)^2}{2\sigma^2} \right] \\
&= -n \ln(\sqrt{2\pi}\sigma) - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu)^2
\end{aligned}
$$

となります。この関数を $\mu$ で微分します。

$$
\frac{d \ln L(\mu)}{d\mu} = -\frac{1}{2\sigma^2} \sum_{i=1}^n 2(x_i - \mu)(-1) = \frac{1}{\sigma^2} \sum_{i=1}^n (x_i - \mu)
$$

停留条件 $\left. \frac{d \ln L}{d\mu} \right|_{\mu = \hat{\mu}} = 0$ より，

$$
\sum_{i=1}^n (x_i - \hat{\mu}) = 0
$$

となります。総和を展開して $\hat{\mu}$ について解くと，

$$
\begin{aligned}
\sum_{i=1}^n x_i - n\hat{\mu} &= 0 \\
\hat{\mu} &= \finalanswer{\frac{1}{n} \sum_{i=1}^n x_i}
\end{aligned}
$$

となります。正規分布の母平均の最尤推定量も標本平均となります。

===== FILE: 13probability_statistics/04/04_030.md =====
---
tags:
  - 基本
---

# 誤差の伝播

## 問題
互いに独立に測定された2つの物理量 $X, Y$ の真値をそれぞれ $x_0, y_0$，不確かさ（標準偏差）を $\sigma_X, \sigma_Y$ とする。物理量 $Z = f(X, Y)$ の測定値の不確かさ $\sigma_Z$ を考える。以下の問いに答えよ。

(1) 関数 $f(X, Y)$ を真値 $(x_0, y_0)$ のまわりで1次までテイラー展開し，合成不確かさの関係式
$$
\sigma_Z^2 = \left(\frac{\partial f}{\partial X}\right)^2 \sigma_X^2 + \left(\frac{\partial f}{\partial Y}\right)^2 \sigma_Y^2
$$
を導け。ただし偏微分係数は真値 $(x_0, y_0)$ で評価された値である。

(2) 積 $Z = XY$ に対する相対不確かさ $\frac{\sigma_Z}{Z}$ を，$\frac{\sigma_X}{X}$ および $\frac{\sigma_Y}{Y}$ を用いて表せ。

(3) 単振り子の周期 $T$ と糸の長さ $L$ を測定して重力加速度 $g = \frac{4\pi^2 L}{T^2}$ を決定するとき，$g$ の相対不確かさ $\frac{\sigma_g}{g}$ を，$\frac{\sigma_L}{L}$ および $\frac{\sigma_T}{T}$ を用いて表せ。

---

## 解答・解説

### (1)
$f(X, Y)$ を測定値の平均値である真値 $(x_0, y_0)$ の近傍で1次の項まで展開します。

$$
f(X, Y) \approx f(x_0, y_0) + \frac{\partial f}{\partial X} (X - x_0) + \frac{\partial f}{\partial Y} (Y - y_0)
$$

$E[X] = x_0$，$E[Y] = y_0$ であるため，期待値をとると $E[Z] \approx f(x_0, y_0)$ です。偏差は次のように近似されます。

$$
Z - E[Z] \approx \frac{\partial f}{\partial X} (X - x_0) + \frac{\partial f}{\partial Y} (Y - y_0)
$$

分散の定義に従ってこの式を2乗し，期待値をとります。

$$
\sigma_Z^2 = E[(Z - E[Z])^2] \approx \left(\frac{\partial f}{\partial X}\right)^2 E[(X - x_0)^2] + \left(\frac{\partial f}{\partial Y}\right)^2 E[(Y - y_0)^2] + 2\frac{\partial f}{\partial X}\frac{\partial f}{\partial Y} E[(X - x_0)(Y - y_0)]
$$

$X$ と $Y$ は互いに独立であるため共分散項 $E[(X - x_0)(Y - y_0)]$ は $0$ です。また $E[(X - x_0)^2] = \sigma_X^2$，$E[(Y - y_0)^2] = \sigma_Y^2$ を代入すると，

$$
\finalanswer{\sigma_Z^2 = \left(\frac{\partial f}{\partial X}\right)^2 \sigma_X^2 + \left(\frac{\partial f}{\partial Y}\right)^2 \sigma_Y^2}
$$

となります。

### (2)
$f(X, Y) = XY$ に対して各変数で偏微分を計算します。

$$
\frac{\partial f}{\partial X} = Y, \quad \frac{\partial f}{\partial Y} = X
$$

(1) の誤差伝播式に代入すると，

$$
\sigma_Z^2 = Y^2 \sigma_X^2 + X^2 \sigma_Y^2
$$

となります。両辺を $Z^2 = X^2 Y^2$ で割ると，

$$
\left(\frac{\sigma_Z}{Z}\right)^2 = \frac{Y^2 \sigma_X^2}{X^2 Y^2} + \frac{X^2 \sigma_Y^2}{X^2 Y^2} = \left(\frac{\sigma_X}{X}\right)^2 + \left(\frac{\sigma_Y}{Y}\right)^2
$$

となります。両辺の正の平方根をとると，

$$
\finalanswer{\frac{\sigma_Z}{Z} = \sqrt{\left(\frac{\sigma_X}{X}\right)^2 + \left(\frac{\sigma_Y}{Y}\right)^2}}
$$

となります。

### (3)
$g = \frac{4\pi^2 L}{T^2}$ の対数をとると関係が簡潔になります。

$$
\ln g = \ln(4\pi^2) + \ln L - 2\ln T
$$

各変数による偏微分を求めます。

$$
\frac{\partial g}{\partial L} = \frac{g}{L}, \quad \frac{\partial g}{\partial T} = -\frac{2g}{T}
$$

これらを (1) の誤差伝播式に代入すると，

$$
\sigma_g^2 = \left( \frac{g}{L} \right)^2 \sigma_L^2 + \left( -\frac{2g}{T} \right)^2 \sigma_T^2
$$

となります。両辺を $g^2$ で割ると，

$$
\left(\frac{\sigma_g}{g}\right)^2 = \left(\frac{\sigma_L}{L}\right)^2 + 4\left(\frac{\sigma_T}{T}\right)^2
$$

となります。両辺の正の平方根をとると，

$$
\finalanswer{\frac{\sigma_g}{g} = \sqrt{\left(\frac{\sigma_L}{L}\right)^2 + 4\left(\frac{\sigma_T}{T}\right)^2}}
$$

となります。周期の2乗に反比例するため，周期の相対不確かさは重力加速度の不確かさに対して2倍の重みで寄与します。

===== FILE: 13probability_statistics/04/04_040.md =====
---
tags:
  - 標準
---

# 最小二乗法によるフィット

## 問題
$n$ 組の測定データ $(x_i, y_i)$（$i = 1, 2, \dots, n$，$n \ge 3$）に対して，直線モデル $y = ax + b$ を当てはめる（図）。残差平方和
$$
S(a, b) = \sum_{i=1}^n (y_i - (a x_i + b))^2
$$
を最小化する。標本平均を $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$，$\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ とする。以下の問いに答えよ。

<!-- FIGURE problem: xy平面上に散布されたデータ点(x_i, y_i)と，直線y=ax+b。データ点から直線へ下ろした縦方向の残差を破線で示す。 -->

(1) $\frac{\partial S}{\partial b} = 0$ から，最適な切片 $b$ を傾き $a$ および平均値 $\bar{x}, \bar{y}$ を用いて表せ。

(2) (1) の関係式を用いて $S(a, b)$ から $b$ を消去し，$\frac{\partial S}{\partial a} = 0$ を解くことで，最適な傾き $a$ を求めよ。

(3) 各 $y_i$ の誤差が互いに独立で，共通の分散 $\sigma^2$ をもつ（$V[y_i] = \sigma^2$）と仮定するとき，(2) で求めた傾きの推定量 $\hat{a}$ の分散 $V[\hat{a}]$ を求めよ。

---

## 解答・解説

### (1)
残差平方和 $S(a, b)$ を切片 $b$ で偏微分します。

$$
\frac{\partial S}{\partial b} = \sum_{i=1}^n 2(y_i - a x_i - b)(-1) = -2 \left( \sum_{i=1}^n y_i - a \sum_{i=1}^n x_i - n b \right)
$$

この式を $0$ とおく停留条件を課します。

$$
\sum_{i=1}^n y_i - a \sum_{i=1}^n x_i - n b = 0
$$

両辺を $n$ で割ると $\bar{y} - a \bar{x} - b = 0$ となるため，

$$
\finalanswer{b = \bar{y} - a \bar{x}}
$$

となります。最良適合直線は重心 $(\bar{x}, \bar{y})$ を必ず通過します。

### (2)
(1) で得られた $b = \bar{y} - a \bar{x}$ を残差の式に代入します。

$$
y_i - (a x_i + b) = (y_i - \bar{y}) - a (x_i - \bar{x})
$$

これより残差平方和は傾き $a$ のみの関数として表せます。

$$
S(a) = \sum_{i=1}^n \left[ (y_i - \bar{y}) - a (x_i - \bar{x}) \right]^2
$$

この式を $a$ で微分します。

$$
\frac{dS}{da} = -2 \sum_{i=1}^n (x_i - \bar{x}) \left[ (y_i - \bar{y}) - a (x_i - \bar{x}) \right]
$$

$\frac{dS}{da} = 0$ とおくと，

$$
\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) - a \sum_{i=1}^n (x_i - \bar{x})^2 = 0
$$

となります。$a$ について解くと，

$$
\finalanswer{a = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}}
$$

となります。

### (3)
(2) で得られた推定量 $\hat{a}$ を $y_i$ の線形結合として書き直します。

$$
\hat{a} = \sum_{i=1}^n c_i y_i, \quad c_i = \frac{x_i - \bar{x}}{\sum_{j=1}^n (x_j - \bar{x})^2}
$$

各 $y_i$ は互いに独立で同一の分散 $\sigma^2$ をもつため，線形結合の分散の公式を適用します。

$$
V[\hat{a}] = \sum_{i=1}^n c_i^2 V[y_i] = \sigma^2 \sum_{i=1}^n c_i^2
$$

係数の二乗和を計算すると，

$$
\sum_{i=1}^n c_i^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{\left[ \sum_{j=1}^n (x_j - \bar{x})^2 \right]^2} = \frac{1}{\sum_{i=1}^n (x_i - \bar{x})^2}
$$

となります。したがって傾きの推定量の分散は，

$$
\finalanswer{V[\hat{a}] = \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2}}
$$

となります。$x$ の測定値が広く散らばっているほど，傾きの決定精度が高くなります。

===== FILE: 13probability_statistics/04/04_050.md =====
---
tags:
  - 標準
---

# カイ二乗分布と適合度検定

## 問題
互いに独立に標準正規分布 $N(0, 1)$ に従う $k$ 個の確率変数を $Z_1, Z_2, \dots, Z_k$ とする。これらを用いて定義される統計量
$$
\chi^2 = \sum_{i=1}^k Z_i^2
$$
は自由度 $k$ のカイ二乗分布に従う。以下の問いに答えよ。

(1) 統計量 $\chi^2$ の期待値 $E[\chi^2]$ を求めよ。

(2) 統計量 $\chi^2$ の分散 $V[\chi^2]$ を求めよ。

(3) 表が出る確率 $p$（$0 < p < 1$），裏が出る確率 $1-p$ のコインを $N$ 回投げる試行を考える。表の出た回数を $O_1$，裏の出た回数を $O_2$（$O_1 + O_2 = N$）とし，それぞれの期待度数を $E_1 = Np$，$E_2 = N(1-p)$ とする。ピアソンのカイ二乗統計量
$$
X^2 = \frac{(O_1 - E_1)^2}{E_1} + \frac{(O_2 - E_2)^2}{E_2}
$$
が，単一の二項確率変数 $O_1$ の標準化変数の2乗 $\frac{(O_1 - Np)^2}{Np(1-p)}$ に等しくなることを示せ。

---

## 解答・解説

### (1)
標準正規分布 $N(0, 1)$ に従う各 $Z_i$ について，定義より $E[Z_i] = 0$，$V[Z_i] = 1$ です。したがって2次モーメントは，

$$
E[Z_i^2] = V[Z_i] + (E[Z_i])^2 = 1 + 0 = 1
$$

となります。期待値の線形性を用いて和をとると，

$$
\begin{aligned}
E[\chi^2] &= E\left[ \sum_{i=1}^k Z_i^2 \right] \\
&= \sum_{i=1}^k E[Z_i^2] \\
&= \sum_{i=1}^k 1 \\
&= \finalanswer{k}
\end{aligned}
$$

となります。

### (2)
標準正規分布の4次モーメントは $E[Z_i^4] = 3$ です。これより各 $Z_i^2$ の分散は，

$$
V[Z_i^2] = E[(Z_i^2)^2] - (E[Z_i^2])^2 = E[Z_i^4] - 1^2 = 3 - 1 = 2
$$

となります。$Z_1, Z_2, \dots, Z_k$ は互いに独立であるため，$Z_1^2, Z_2^2, \dots, Z_k^2$ も互いに独立です。独立な確率変数の和の分散は分散の和となるため，

$$
\begin{aligned}
V[\chi^2] &= V\left[ \sum_{i=1}^k Z_i^2 \right] \\
&= \sum_{i=1}^k V[Z_i^2] \\
&= \sum_{i=1}^k 2 \\
&= \finalanswer{2k}
\end{aligned}
$$

となります。

### (3)
条件 $O_1 + O_2 = N$ および $E_1 + E_2 = Np + N(1-p) = N$ より，裏の偏差は表の偏差を用いて次のように表せます。

$$
O_2 - E_2 = (N - O_1) - (N - E_1) = -(O_1 - E_1)
$$

この関係を2乗すると $(O_2 - E_2)^2 = (O_1 - E_1)^2$ となります。これを与えられたピアソンの統計量 $X^2$ に代入します。

$$
\begin{aligned}
X^2 &= \frac{(O_1 - E_1)^2}{Np} + \frac{(O_2 - E_2)^2}{N(1-p)} \\
&= (O_1 - E_1)^2 \left( \frac{1}{Np} + \frac{1}{N(1-p)} \right)
\end{aligned}
$$

括弧内を通分して整理します。

$$
\frac{1}{Np} + \frac{1}{N(1-p)} = \frac{(1-p) + p}{Np(1-p)} = \frac{1}{Np(1-p)}
$$

$E_1 = Np$ を代入すると，

$$
\finalanswer{X^2 = \frac{(O_1 - Np)^2}{Np(1-p)}}
$$

となります。この式は二項分布の平均 $Np$ と分散 $Np(1-p)$ による標準化変数の2乗であり，中心極限定理により $N$ が大きい極限で自由度1のカイ二乗分布に従います。

===== FILE: 13probability_statistics/04/04_060.md =====
---
tags:
  - 標準
---

# 信頼区間

## 問題
平均 $\mu$（未知），分散 $\sigma^2$（既知，$\sigma > 0$）の正規分布 $N(\mu, \sigma^2)$ から抽出された大きさ $n$ の無作為標本 $X_1, X_2, \dots, X_n$ を考える。標本平均を $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ とする。以下の問いに答えよ。

(1) 標本平均 $\bar{X}$ が従う確率分布の平均と分散を求めよ。

(2) 統計量 $Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$ は標準正規分布 $N(0, 1)$ に従う。標準正規分布の両側 $100\alpha\,\%$ 点を $z_{\alpha/2}$（すなわち $P(-z_{\alpha/2} \le Z \le z_{\alpha/2}) = 1 - \alpha$）とするとき，母平均 $\mu$ に対する信頼係数 $1-\alpha$ の信頼区間を求めよ。

(3) この信頼区間の幅を半分にするためには，標本の大きさ $n$ を何倍にする必要があるか求めよ。

---

## 解答・解説

### (1)
標本平均の期待値を計算します。期待値の線形性より，

$$
E[\bar{X}] = E\left[ \frac{1}{n} \sum_{i=1}^n X_i \right] = \frac{1}{n} \sum_{i=1}^n E[X_i] = \frac{1}{n} \cdot n\mu = \mu
$$

となります。続いて分散を計算します。各標本は互いに独立であるため，

$$
V[\bar{X}] = V\left[ \frac{1}{n} \sum_{i=1}^n X_i \right] = \frac{1}{n^2} \sum_{i=1}^n V[X_i] = \frac{1}{n^2} \cdot n\sigma^2 = \frac{\sigma^2}{n}
$$

となります。正規分布の再生性により，$\bar{X}$ もまた正規分布に従います。したがって求める平均と分散は，

$$
\finalanswer{E[\bar{X}] = \mu}, \quad \finalanswer{V[\bar{X}] = \frac{\sigma^2}{n}}
$$

となります。

### (2)
標準正規分布における採択域を図に示します。

<!-- FIGURE solution (2): 横軸z，縦軸phi(z)の標準正規分布曲線。中央の面積1-alphaの部分を塗りつぶし，両側の裾野の面積alpha/2を区切る臨界値-z_{alpha/2}とz_{alpha/2}を示す。 -->

確率の式に統計量 $Z$ の定義を代入します。

$$
P\left( -z_{\alpha/2} \le \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \le z_{\alpha/2} \right) = 1 - \alpha
$$

括弧内の不等式を母平均 $\mu$ について解きます。各辺に標準誤差 $\frac{\sigma}{\sqrt{n}}$ を掛けます。

$$
-z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \le \bar{X} - \mu \le z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
$$

各辺から $\bar{X}$ を引きます。

$$
-\bar{X} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \le -\mu \le -\bar{X} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
$$

各辺に $-1$ を掛けると不等号の向きが反転します。

$$
\bar{X} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \le \mu \le \bar{X} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
$$

したがって，母平均 $\mu$ に対する信頼係数 $1-\alpha$ の信頼区間は，

$$
\finalanswer{\left[ \bar{X} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}}, \ \bar{X} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right]}
$$

となります。

### (3)
(2) で求めた信頼区間の幅 $L$ は，区間の上限と下限の差として計算されます。

$$
L = \left( \bar{X} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right) - \left( \bar{X} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right) = 2 z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
$$

信頼区間の幅 $L$ は標本サイズの平方根 $\sqrt{n}$ に反比例します。幅を $\frac{1}{2} L$ にするためには，新たな標本サイズを $n'$ とすると，

$$
\frac{1}{\sqrt{n'}} = \frac{1}{2} \cdot \frac{1}{\sqrt{n}}
$$

を満たす必要があります。両辺の逆数をとると，

$$
\sqrt{n'} = 2\sqrt{n}
$$

となり，両辺を2乗すると，

$$
\finalanswer{n' = 4n}
$$

となります。したがって標本の大きさを $4$ 倍にする必要があります。

===== END =====