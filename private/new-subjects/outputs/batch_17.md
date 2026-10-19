===== FILE: 13probability_statistics/05/05_010.md =====
---
tags:
  - 標準
---

# マルコフ連鎖

## 問題
2つの状態 1 と 2 の間を遷移する離散時間のマルコフ連鎖を考える。ステップ $n$（$n = 0, 1, 2, \dots$）における状態確率ベクトルを $\boldsymbol{p}_n = \begin{pmatrix} p_n(1) \\ p_n(2) \end{pmatrix}$ とする。状態 1 から状態 2 への遷移確率を $\alpha$，状態 2 から状態 1 への遷移確率を $\beta$ とし（$0 < \alpha < 1$，$0 < \beta < 1$），遷移行列を
$$
P = \begin{pmatrix} 1-\alpha & \beta \\ \alpha & 1-\beta \end{pmatrix}
$$
と定義する。状態確率は漸化式 $\boldsymbol{p}_{n+1} = P \boldsymbol{p}_n$ に従って時間発展する。以下の問いに答えよ。

(1) 遷移行列 $P$ の固有値 $\lambda_1, \lambda_2$（$\lambda_1 > \lambda_2$）を求めよ。

(2) $P \boldsymbol{\pi} = \boldsymbol{\pi}$ かつ成分の和が 1 となる定常分布 $\boldsymbol{\pi} = \begin{pmatrix} \pi(1) \\ \pi(2) \end{pmatrix}$ を求めよ。

(3) 初期状態を $\boldsymbol{p}_0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ とするとき，ステップ $n$ における状態確率ベクトル $\boldsymbol{p}_n$ を求めよ。

---

## 解答・解説

### (1)
遷移行列 $P$ の固有値を求めるため，特性方程式 $\det(P - \lambda I) = 0$ を計算します。行列式を書き下すと，
$$
\begin{aligned}
\det(P - \lambda I) &= \det \begin{pmatrix} 1-\alpha-\lambda & \beta \\ \alpha & 1-\beta-\lambda \end{pmatrix} \\
&= (1-\alpha-\lambda)(1-\beta-\lambda) - \alpha\beta \\
&= \lambda^2 - (2-\alpha-\beta)\lambda + (1-\alpha-\beta)
\end{aligned}
$$
となります。この2次方程式を因数分解すると，
$$
\begin{aligned}
\det(P - \lambda I) &= (\lambda - 1)\{\lambda - (1-\alpha-\beta)\} = 0
\end{aligned}
$$
が得られます。条件 $0 < \alpha < 1$，$0 < \beta < 1$ より $1-\alpha-\beta < 1$ であるため，大きい方の固有値が $\lambda_1 = 1$ となります。

したがって，求める固有値は
$$
\finalanswer{\lambda_1 = 1, \quad \lambda_2 = 1 - \alpha - \beta}
$$
となります。

### (2)
定常分布 $\boldsymbol{\pi}$ は固有値 $\lambda_1 = 1$ に属する規格化された固有ベクトルです。方程式 $(P - I)\boldsymbol{\pi} = \boldsymbol{0}$ を成分ごとに書き下すと，
$$
\begin{aligned}
\begin{pmatrix} -\alpha & \beta \\ \alpha & -\beta \end{pmatrix} \begin{pmatrix} \pi(1) \\ \pi(2) \end{pmatrix} &= \begin{pmatrix} 0 \\ 0 \end{pmatrix}
\end{aligned}
$$
となります。両方の行から同一の関係式
$$
\begin{aligned}
\alpha \pi(1) &= \beta \pi(2)
\end{aligned}
$$
が得られます。確率の規格化条件 $\pi(1) + \pi(2) = 1$ に $\pi(2) = (\alpha/\beta)\pi(1)$ を代入すると，
$$
\begin{aligned}
\pi(1) + \frac{\alpha}{\beta}\pi(1) &= \frac{\alpha+\beta}{\beta}\pi(1) = 1
\end{aligned}
$$
となります。これを解いて各成分を求めると，
$$
\finalanswer{\boldsymbol{\pi} = \frac{1}{\alpha+\beta}\begin{pmatrix} \beta \\ \alpha \end{pmatrix}}
$$
となります。

### (3)
固有値 $\lambda_1 = 1$ および $\lambda_2 = 1-\alpha-\beta$ に対応する固有ベクトルを求めて，初期状態ベクトルを展開します。$\lambda_2$ に対する固有ベクトル方程式 $(P - \lambda_2 I)\boldsymbol{v}_2 = \boldsymbol{0}$ は
$$
\begin{aligned}
\begin{pmatrix} \beta & \beta \\ \alpha & \alpha \end{pmatrix} \begin{pmatrix} v_{21} \\ v_{22} \end{pmatrix} &= \begin{pmatrix} 0 \\ 0 \end{pmatrix}
\end{aligned}
$$
となるため，固有ベクトルとして $\boldsymbol{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ を選ぶことができます。また，$\lambda_1 = 1$ に属する固有ベクトルとして $\boldsymbol{v}_1 = \begin{pmatrix} \beta \\ \alpha \end{pmatrix}$ をとります。

初期ベクトル $\boldsymbol{p}_0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ をこれら2つの固有ベクトルの線形結合
$$
\begin{aligned}
\boldsymbol{p}_0 &= c_1 \boldsymbol{v}_1 + c_2 \boldsymbol{v}_2 = c_1 \begin{pmatrix} \beta \\ \alpha \end{pmatrix} + c_2 \begin{pmatrix} 1 \\ -1 \end{pmatrix}
\end{aligned}
$$
として表します。連立方程式
$$
\begin{aligned}
\beta c_1 + c_2 &= 1 \\
\alpha c_1 - c_2 &= 0
\end{aligned}
$$
を解くと，$c_1 = 1/(\alpha+\beta)$，$c_2 = \alpha/(\alpha+\beta)$ が得られます。遷移行列の $n$ 乗を作用させると，
$$
\begin{aligned}
\boldsymbol{p}_n &= P^n \boldsymbol{p}_0 \\
&= c_1 \lambda_1^n \boldsymbol{v}_1 + c_2 \lambda_2^n \boldsymbol{v}_2 \\
&= \frac{1}{\alpha+\beta} \begin{pmatrix} \beta \\ \alpha \end{pmatrix} + \frac{\alpha (1-\alpha-\beta)^n}{\alpha+\beta} \begin{pmatrix} 1 \\ -1 \end{pmatrix}
\end{aligned}
$$
となります。各成分を整理してまとめると，
$$
\finalanswer{\boldsymbol{p}_n = \frac{1}{\alpha+\beta} \begin{pmatrix} \beta + \alpha(1-\alpha-\beta)^n \\ \alpha - \alpha(1-\alpha-\beta)^n \end{pmatrix}}
$$
となります。$|1-\alpha-\beta| < 1$ より $n \to \infty$ で初期状態の記憶が失われ，定常分布 $\boldsymbol{\pi}$ に収束します。

===== FILE: 13probability_statistics/05/05_020.md =====
---
tags:
  - 発展
---

# マスター方程式

## 問題
ある系が2つの状態 1 と 2 の間を連続時間で遷移している。状態 1 から状態 2 への単位時間あたりの遷移確率を $k_1$（$k_1 > 0$），状態 2 から状態 1 への遷移確率を $k_2$（$k_2 > 0$）とする。時刻 $t$ において系が状態 1 にある確率を $p_1(t)$，状態 2 にある確率を $p_2(t)$ とする。確率はマスター方程式
$$
\frac{dp_1(t)}{dt} = -k_1 p_1(t) + k_2 p_2(t)
$$
に従う。以下の問いに答えよ。

(1) 確率の規格化条件 $p_1(t) + p_2(t) = 1$ を用いて，$p_1(t)$ のみに関する1階線形微分方程式を導け。

(2) 初期条件 $p_1(0) = 1$ のもとでこの微分方程式を解き，$p_1(t)$ を求めよ。

(3) 長時間極限 $t \to \infty$ における定常確率 $p_1(\infty)$ を求め，詳細釣り合いの条件 $k_1 p_1(\infty) = k_2 p_2(\infty)$ が成り立つことを示せ。

---

## 解答・解説

### (1)
系は状態 1 または状態 2 のいずれかをとるため，全確率は保存し，常に $p_1(t) + p_2(t) = 1$ が成り立ちます。これより $p_2(t) = 1 - p_1(t)$ と表せます。この表式をマスター方程式の右辺に代入すると，
$$
\begin{aligned}
\frac{dp_1(t)}{dt} &= -k_1 p_1(t) + k_2 \{1 - p_1(t)\} \\
&= -(k_1 + k_2) p_1(t) + k_2
\end{aligned}
$$
となります。項を移項して整理すると，
$$
\finalanswer{\frac{dp_1(t)}{dt} + (k_1 + k_2) p_1(t) = k_2}
$$
となります。

### (2)
導いた非同次1階線形微分方程式を解きます。両辺に積分因子 $e^{(k_1+k_2)t}$ をかけると，
$$
\begin{aligned}
\frac{d}{dt} \left\{ p_1(t) e^{(k_1+k_2)t} \right\} &= k_2 e^{(k_1+k_2)t}
\end{aligned}
$$
とまとめることができます。両辺を時刻 0 から $t$ まで積分すると，
$$
\begin{aligned}
\left[ p_1(s) e^{(k_1+k_2)s} \right]_0^t &= \int_0^t k_2 e^{(k_1+k_2)s} ds \\
p_1(t) e^{(k_1+k_2)t} - p_1(0) &= \frac{k_2}{k_1+k_2} \left\{ e^{(k_1+k_2)t} - 1 \right\}
\end{aligned}
$$
となります。初期条件 $p_1(0) = 1$ を代入し，両辺に $e^{-(k_1+k_2)t}$ をかけると，
$$
\begin{aligned}
p_1(t) &= e^{-(k_1+k_2)t} + \frac{k_2}{k_1+k_2} \left\{ 1 - e^{-(k_1+k_2)t} \right\} \\
&= \frac{k_2}{k_1+k_2} + \left(1 - \frac{k_2}{k_1+k_2}\right) e^{-(k_1+k_2)t}
\end{aligned}
$$
となります。係数を整理すると，
$$
\finalanswer{p_1(t) = \frac{k_2}{k_1+k_2} + \frac{k_1}{k_1+k_2} e^{-(k_1+k_2)t}}
$$
となります。

### (3)
$k_1 + k_2 > 0$ であるため，$t \to \infty$ の極限で指数関数部分はゼロに減衰します。したがって，定常確率は
$$
\finalanswer{p_1(\infty) = \frac{k_2}{k_1+k_2}}
$$
となります。このとき，状態 2 の定常確率は
$$
\begin{aligned}
p_2(\infty) &= 1 - p_1(\infty) \\
&= 1 - \frac{k_2}{k_1+k_2} \\
&= \frac{k_1}{k_1+k_2}
\end{aligned}
$$
となります。状態 1 から 2 への確率の流れ $k_1 p_1(\infty)$ と，状態 2 から 1 への確率の流れ $k_2 p_2(\infty)$ をそれぞれ計算すると，
$$
\begin{aligned}
k_1 p_1(\infty) &= \frac{k_1 k_2}{k_1+k_2} \\
k_2 p_2(\infty) &= \frac{k_2 k_1}{k_1+k_2}
\end{aligned}
$$
となり，両者が一致します。よって，
$$
\finalanswer{k_1 p_1(\infty) = k_2 p_2(\infty)}
$$
が成り立ち，状態間の正味の確率の流れが存在しない詳細釣り合いが示されました。

===== FILE: 13probability_statistics/05/05_030.md =====
---
tags:
  - 標準
---

# ポアソン過程

## 問題
単位時間あたり平均 $\lambda$（$\lambda > 0$）回発生する事象を観測する。時刻 0 から時刻 $t$ までの時間区間に発生する事象の数を $N(t)$ とすると，$N(t)$ はパラメータ $\lambda t$ のポアソン分布
$$
P(N(t) = n) = \frac{(\lambda t)^n}{n!} e^{-\lambda t} \quad (n = 0, 1, 2, \dots)
$$
に従う。時刻 0 から数えて最初の事象が発生するまでの待ち時間を $T_1$ とする。以下の問いに答えよ。

(1) 待ち時間が $t$ より大きくなる確率 $P(T_1 > t)$ を求めよ（$t \ge 0$）。

(2) $T_1$ の確率密度関数 $f(t)$ を求めよ（$t \ge 0$）。

(3) 待ち時間の期待値 $E[T_1]$ および分散 $V[T_1]$ を求めよ。

---

## 解答・解説

### (1)
事象が発生するまでの待ち時間 $T_1$ が $t$ より大きくなるという事象は，時刻 0 から時刻 $t$ までの間に事象が1回も発生しなかった事象 $N(t) = 0$ と同値です。与えられたポアソン分布の式において $n = 0$ を代入すると，
$$
\begin{aligned}
P(T_1 > t) &= P(N(t) = 0) \\
&= \frac{(\lambda t)^0}{0!} e^{-\lambda t}
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{P(T_1 > t) = e^{-\lambda t}}
$$
となります。

### (2)
確率変数 $T_1$ の累積分布関数 $F(t) = P(T_1 \le t)$ は，余事象の確率を用いて表されます。小問 (1) の結果を用いると，
$$
\begin{aligned}
F(t) &= 1 - P(T_1 > t) \\
&= 1 - e^{-\lambda t}
\end{aligned}
$$
となります。確率密度関数 $f(t)$ は累積分布関数を $t$ で微分することで得られます。$t \ge 0$ において微分を実行すると，
$$
\begin{aligned}
f(t) &= \frac{dF(t)}{dt} \\
&= \frac{d}{dt} \left( 1 - e^{-\lambda t} \right) \\
&= \lambda e^{-\lambda t}
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{f(t) = \lambda e^{-\lambda t}}
$$
となり，$T_1$ がパラメータ $\lambda$ の指数分布に従うことが導かれます。

### (3)
期待値 $E[T_1]$ は部分積分を用いて計算します。定義にしたがって立式すると，
$$
\begin{aligned}
E[T_1] &= \int_0^\infty t f(t) dt \\
&= \int_0^\infty t \lambda e^{-\lambda t} dt \\
&= \left[ -t e^{-\lambda t} \right]_0^\infty + \int_0^\infty e^{-\lambda t} dt \\
&= 0 + \left[ -\frac{1}{\lambda} e^{-\lambda t} \right]_0^\infty \\
&= \finalanswer{\frac{1}{\lambda}}
\end{aligned}
$$
となります。同様に，2次のモーメント $E[T_1^2]$ を計算します。部分積分を2回行うと，
$$
\begin{aligned}
E[T_1^2] &= \int_0^\infty t^2 \lambda e^{-\lambda t} dt \\
&= \left[ -t^2 e^{-\lambda t} \right]_0^\infty + \int_0^\infty 2t e^{-\lambda t} dt \\
&= 0 + \frac{2}{\lambda} \int_0^\infty t \lambda e^{-\lambda t} dt \\
&= \frac{2}{\lambda} E[T_1] \\
&= \frac{2}{\lambda^2}
\end{aligned}
$$
となります。分散 $V[T_1]$ は $E[T_1^2] - (E[T_1])^2$ で与えられます。数値を代入すると，
$$
\begin{aligned}
V[T_1] &= \frac{2}{\lambda^2} - \left(\frac{1}{\lambda}\right)^2 \\
&= \finalanswer{\frac{1}{\lambda^2}}
\end{aligned}
$$
となります。発生頻度 $\lambda$ が大きいほど，平均待ち時間およびそのばらつきは小さくなります。

===== FILE: 13probability_statistics/05/05_040.md =====
---
tags:
  - 発展
---

# ランジュバン方程式

## 問題
粘性流体中を運動する質量 $m$ の微粒子の1次元運動を考える。粒子の速度を $v(t)$，流体の粘性抵抗係数を $\gamma$（$\gamma > 0$）とする。微粒子はランジュバン方程式
$$
m \frac{dv(t)}{dt} = -\gamma v(t) + R(t)
$$
に従う。ここで $R(t)$ は溶媒分子の衝突によるランダム力（白色雑音）であり，アンサンブル平均について以下の性質をもつ。
$$
\langle R(t) \rangle = 0, \quad \langle R(t) R(t') \rangle = 2 D_v \delta(t - t')
$$
ただし $D_v > 0$ は定数，$\delta(t)$ はデルタ関数である。初期速度を $v(0) = v_0$ とする。以下の問いに答えよ。

(1) 任意の時刻 $t \ge 0$ における速度 $v(t)$ を，$v_0$，$m$，$\gamma$，$R(s)$（$0 \le s \le t$）を用いて表せ。

(2) 速度の平均値 $\langle v(t) \rangle$ を求めよ。

(3) 時間差 $\tau \ge 0$ に対し，長時間極限における速度相関関数 $\lim_{t \to \infty} \langle v(t) v(t+\tau) \rangle$ を求めよ。

---

## 解答・解説

### (1)
ランジュバン方程式の両辺を $m$ で割ると，
$$
\begin{aligned}
\frac{dv(t)}{dt} + \frac{\gamma}{m} v(t) &= \frac{1}{m} R(t)
\end{aligned}
$$
となります。両辺に積分因子 $e^{\frac{\gamma}{m}t}$ をかけると，左辺を1つの微分の形にまとめることができます。
$$
\begin{aligned}
\frac{d}{dt} \left\{ v(t) e^{\frac{\gamma}{m}t} \right\} &= \frac{1}{m} R(t) e^{\frac{\gamma}{m}t}
\end{aligned}
$$
時刻 0 から $t$ まで積分すると，
$$
\begin{aligned}
v(t) e^{\frac{\gamma}{m}t} - v_0 &= \frac{1}{m} \int_0^t e^{\frac{\gamma}{m}s} R(s) ds
\end{aligned}
$$
が得られます。両辺に $e^{-\frac{\gamma}{m}t}$ をかけると，
$$
\finalanswer{v(t) = v_0 e^{-\frac{\gamma}{m}t} + \frac{1}{m} \int_0^t e^{-\frac{\gamma}{m}(t-s)} R(s) ds}
$$
となります。

### (2)
小問 (1) で求めた解のアンサンブル平均をとります。線形性により，積分の外から平均を作用させることができます。
$$
\begin{aligned}
\langle v(t) \rangle &= v_0 e^{-\frac{\gamma}{m}t} + \frac{1}{m} \int_0^t e^{-\frac{\gamma}{m}(t-s)} \langle R(s) \rangle ds
\end{aligned}
$$
ランダム力の平均値について $\langle R(s) \rangle = 0$ であるため，右辺第2項の積分はゼロになります。したがって，
$$
\finalanswer{\langle v(t) \rangle = v_0 e^{-\frac{\gamma}{m}t}}
$$
となります。粘性散逸によって平均速度は特性時間 $m/\gamma$ で指数関数的に減衰します。

### (3)
時刻 $t$ と時刻 $t+\tau$ における速度の積の平均を計算します。$\langle R(s) \rangle = 0$ より，$v_0$ と $R$ の積の平均は消滅します。
$$
\begin{aligned}
\langle v(t) v(t+\tau) \rangle &= v_0^2 e^{-\frac{\gamma}{m}(2t+\tau)} \\
&\quad + \frac{1}{m^2} \int_0^t ds \int_0^{t+\tau} ds' e^{-\frac{\gamma}{m}(t-s)} e^{-\frac{\gamma}{m}(t+\tau-s')} \langle R(s) R(s') \rangle
\end{aligned}
$$
雑音の相関 $\langle R(s) R(s') \rangle = 2 D_v \delta(s - s')$ を代入します。積分範囲において $s \le t < t+\tau$ であるため，デルタ関数による $s'$ の積分範囲に $s$ が必ず含まれます。
$$
\begin{aligned}
\int_0^{t+\tau} e^{\frac{\gamma}{m}s'} 2 D_v \delta(s - s') ds' &= 2 D_v e^{\frac{\gamma}{m}s}
\end{aligned}
$$
これを用いて積分を整理すると，
$$
\begin{aligned}
\langle v(t) v(t+\tau) \rangle &= v_0^2 e^{-\frac{\gamma}{m}(2t+\tau)} + \frac{2 D_v}{m^2} e^{-\frac{\gamma}{m}(2t+\tau)} \int_0^t e^{\frac{2\gamma}{m}s} ds \\
&= v_0^2 e^{-\frac{\gamma}{m}(2t+\tau)} + \frac{2 D_v}{m^2} e^{-\frac{\gamma}{m}(2t+\tau)} \left[ \frac{m}{2\gamma} e^{\frac{2\gamma}{m}s} \right]_0^t \\
&= v_0^2 e^{-\frac{\gamma}{m}(2t+\tau)} + \frac{D_v}{m\gamma} e^{-\frac{\gamma}{m}\tau} \left( 1 - e^{-\frac{2\gamma}{m}t} \right)
\end{aligned}
$$
となります。ここで $t \to \infty$ の極限をとると，$e^{-\frac{\gamma}{m}t}$ を含む項はすべてゼロに収束します。したがって，
$$
\finalanswer{\lim_{t \to \infty} \langle v(t) v(t+\tau) \rangle = \frac{D_v}{m\gamma} e^{-\frac{\gamma}{m}\tau}}
$$
となります。長時間極限において系は定常状態に達し，相関は時間差 $\tau$ のみに依存する形となります。

===== FILE: 13probability_statistics/05/05_050.md =====
---
tags:
  - 標準
---

# 情報エントロピー

## 問題
ある系が $n$ 個の離散状態 $i = 1, 2, \dots, n$ のいずれかをとる。系が状態 $i$ にある確率を $p_i$（$p_i > 0$，$\sum_{i=1}^n p_i = 1$）とする。シャノン情報エントロピーは
$$
S = -\sum_{i=1}^n p_i \ln p_i
$$
で定義される。以下の問いに答えよ。

(1) 規格化条件 $\sum_{i=1}^n p_i = 1$ のもとで，$S$ を最大にする確率分布 $p_i$ およびその最大値を求めよ。

(2) 各状態 $i$ にエネルギー $E_i$ が割り振られているとする。規格化条件に加えて，平均エネルギーが一定である拘束条件
$$
\sum_{i=1}^n E_i p_i = U
$$
が課されている。未定乗数法を用いて，$S$ を最大にする確率分布 $p_i$ が
$$
p_i = \frac{e^{-\beta E_i}}{\sum_{j=1}^n e^{-\beta E_j}}
$$
の形（ボルツマン分布）で表されることを示せ。ただし，$\beta$ は平均エネルギーの条件に対応する未定乗数とする。

---

## 解答・解説

### (1)
拘束条件 $\sum_{i=1}^n p_i - 1 = 0$ のもとでエントロピー $S$ を最大化するため，ラグランジュの未定乗数 $\alpha$ を導入します。評価関数を
$$
\begin{aligned}
L(p_1, \dots, p_n, \alpha) &= -\sum_{i=1}^n p_i \ln p_i - \alpha \left( \sum_{i=1}^n p_i - 1 \right)
\end{aligned}
$$
とおきます。各 $p_i$ について偏微分して極値条件を求めると，
$$
\begin{aligned}
\frac{\partial L}{\partial p_i} &= -(\ln p_i + 1) - \alpha = 0
\end{aligned}
$$
となります。これを $\ln p_i$ について解くと，
$$
\begin{aligned}
\ln p_i &= -(1 + \alpha)
\end{aligned}
$$
となり，$p_i$ は状態 $i$ に依存しない定数 $C = e^{-(1+\alpha)}$ であることがわかります。規格化条件に代入すると，
$$
\begin{aligned}
\sum_{i=1}^n p_i &= n C = 1
\end{aligned}
$$
より $C = 1/n$ が得られます。したがって，エントロピーを最大化する確率は
$$
\finalanswer{p_i = \frac{1}{n}}
$$
となります。このときの $S$ の最大値は，等確率分布を定義式に代入して，
$$
\begin{aligned}
S_{\max} &= -\sum_{i=1}^n \frac{1}{n} \ln \frac{1}{n} \\
&= \ln n
\end{aligned}
$$
となります。よって最大値は
$$
\finalanswer{S_{\max} = \ln n}
$$
となります。

### (2)
2つの拘束条件，すなわち規格化条件 $\sum_{i=1}^n p_i = 1$ と内部エネルギーの条件 $\sum_{i=1}^n E_i p_i = U$ を考慮します。未定乗数 $\lambda$ および $\beta$ を用いてラグランジュ関数を
$$
\begin{aligned}
L &= -\sum_{i=1}^n p_i \ln p_i - \lambda \left( \sum_{i=1}^n p_i - 1 \right) - \beta \left( \sum_{i=1}^n E_i p_i - U \right)
\end{aligned}
$$
と定義します。各 $p_i$ で偏微分してゼロとおくと，
$$
\begin{aligned}
\frac{\partial L}{\partial p_i} &= -(\ln p_i + 1) - \lambda - \beta E_i = 0
\end{aligned}
$$
が得られます。これを $\ln p_i$ について解くと，
$$
\begin{aligned}
\ln p_i &= -(1 + \lambda) - \beta E_i
\end{aligned}
$$
となり，指数をとることで
$$
\begin{aligned}
p_i &= e^{-(1+\lambda)} e^{-\beta E_i}
\end{aligned}
$$
と導かれます。規格化条件 $\sum_{i=1}^n p_i = 1$ を適用すると，
$$
\begin{aligned}
e^{-(1+\lambda)} \sum_{j=1}^n e^{-\beta E_j} &= 1
\end{aligned}
$$
より，係数部分は
$$
\begin{aligned}
e^{-(1+\lambda)} &= \frac{1}{\sum_{j=1}^n e^{-\beta E_j}}
\end{aligned}
$$
と決定されます。これを $p_i$ の式に代入すると，
$$
\finalanswer{p_i = \frac{e^{-\beta E_i}}{\sum_{j=1}^n e^{-\beta E_j}}}
$$
が得られ，カノニカル分布（ボルツマン分布）の形が導かれます。

===== FILE: 13probability_statistics/06/06_010.md =====
---
tags:
  - 基本
---

# 場合の数と包除原理

## 問題
$n$ 人の人（$n \ge 2$）がそれぞれ自分の帽子を1個ずつ持ち寄り，ランダムにシャッフルして1人1個ずつ受け取る。すべて帽子の配り方は同様に確からしいとする。人 $k$（$k = 1, 2, \dots, n$）が自分の帽子を受け取る事象を $A_k$ とする。以下の問いに答えよ。

(1) 少なくとも1人が自分の帽子を受け取る事象 $\bigcup_{k=1}^n A_k$ の確率を，$n$ を用いた和の形で表せ。

(2) 誰も自分の帽子を受け取らない確率（完全順列の確率）$P_n$ を求めよ。

(3) 極限 $\lim_{n \to \infty} P_n$ を求めよ。

---

## 解答・解説

### (1)
包除原理によると，和事象の確率は共通部分の確率の交代和として
$$
\begin{aligned}
P\left(\bigcup_{k=1}^n A_k\right) &= \sum_{m=1}^n (-1)^{m-1} \sum_{1 \le i_1 < \dots < i_m \le n} P(A_{i_1} \cap \dots \cap A_{i_m})
\end{aligned}
$$
と表されます。特定の $m$ 人が自分の帽子を受け取り，残りの $n-m$ 人の帽子の配り方は任意である事象の確率を計算します。全事象の数は $n!$ 通り，この事象の場合の数は $(n-m)!$ 通りであるため，確率は
$$
\begin{aligned}
P(A_{i_1} \cap \dots \cap A_{i_m}) &= \frac{(n-m)!}{n!}
\end{aligned}
$$
となります。$n$ 人から $m$ 人を選ぶ組み合わせの数は $\binom{n}{m}$ 通りあるため，各 $m$ に対する和は
$$
\begin{aligned}
\sum_{1 \le i_1 < \dots < i_m \le n} P(A_{i_1} \cap \dots \cap A_{i_m}) &= \binom{n}{m} \frac{(n-m)!}{n!} \\
&= \frac{n!}{m!(n-m)!} \frac{(n-m)!}{n!} \\
&= \frac{1}{m!}
\end{aligned}
$$
となります。これを包除原理の式に代入すると，
$$
\finalanswer{P\left(\bigcup_{k=1}^n A_k\right) = \sum_{m=1}^n \frac{(-1)^{m-1}}{m!}}
$$
となります。

### (2)
誰も自分の帽子を受け取らない事象は，少なくとも1人が自分の帽子を受け取る事象の余事象です。小問 (1) の結果を用いて余事象の確率を計算すると，
$$
\begin{aligned}
P_n &= 1 - P\left(\bigcup_{k=1}^n A_k\right) \\
&= 1 - \sum_{m=1}^n \frac{(-1)^{m-1}}{m!} \\
&= 1 + \sum_{m=1}^n \frac{(-1)^m}{m!}
\end{aligned}
$$
となります。$m = 0$ の項が $1 = (-1)^0/0!$ であることに着目すると，和を1つの式にまとめることができます。
$$
\finalanswer{P_n = \sum_{m=0}^n \frac{(-1)^m}{m!}}
$$
となります。

### (3)
小問 (2) で得られた $P_n$ は，指数関数 $e^x$ のマクローリン展開
$$
\begin{aligned}
e^x &= \sum_{m=0}^\infty \frac{x^m}{m!}
\end{aligned}
$$
において $x = -1$ と置いた級数の部分和となっています。したがって，$n \to \infty$ の極限をとると，
$$
\begin{aligned}
\lim_{n \to \infty} P_n &= \sum_{m=0}^\infty \frac{(-1)^m}{m!} \\
&= e^{-1}
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{\lim_{n \to \infty} P_n = \frac{1}{e}}
$$
となります。人数 $n$ が十分に大きければ，全員が他人の帽子を受け取る確率は人数によらず約 $36.8\%$ でほぼ一定となります。

===== FILE: 13probability_statistics/06/06_020.md =====
---
tags:
  - 基本
---

# 誕生日問題

## 問題
1年を365日とし，どの人の誕生日も365日の中で同様に確からしいとする。ある集まりに $n$ 人（$2 \le n \le 365$）がいるとき，少なくとも2人の誕生日が一致する確率を考える。以下の問いに答えよ。

(1) $n$ 人全員の誕生日がすべて異なる確率 $Q_n$ を積の記号 $\prod$ を用いて表せ。

(2) $x \ll 1$ における近似式 $1 - x \approx e^{-x}$ を用いて，$Q_n$ を $n$ の指数関数の形で近似せよ。

(3) 少なくとも2人の誕生日が一致する確率 $P_n = 1 - Q_n$ が $1/2$ 以上となる最小の整数 $n$ を求めよ。ただし，必要であれば $2 \ln 2 \approx 1.386$，$\sqrt{365 \times 1.386} \approx 22.49$ を用いよ。

---

## 解答・解説

### (1)
1人目の誕生日は任意の日でよく，2人目は1人目と異なる日（364通り），3人目は先の2人と異なる日（363通り），と順に選んでいきます。$k$ 人目（$k = 1, 2, \dots, n$）の誕生日がそれまでの全員と異なる確率は $(365 - k + 1)/365$ です。積の法則により，全員の誕生日がすべて異なる確率 $Q_n$ は
$$
\begin{aligned}
Q_n &= \frac{365}{365} \times \frac{364}{365} \times \dots \times \frac{365 - n + 1}{365} \\
&= \prod_{k=1}^{n-1} \left( 1 - \frac{k}{365} \right)
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{Q_n = \prod_{k=1}^{n-1} \left( 1 - \frac{k}{365} \right)}
$$
となります。

### (2)
$n \ll 365$ であるとき，すべての $k \le n-1$ について $k/365 \ll 1$ が成り立ちます。近似式 $1 - x \approx e^{-x}$ を各項に適用すると，
$$
\begin{aligned}
Q_n &\approx \prod_{k=1}^{n-1} \exp\left( -\frac{k}{365} \right) \\
&= \exp\left( -\sum_{k=1}^{n-1} \frac{k}{365} \right)
\end{aligned}
$$
となります。指数の肩にある等差数列の和を計算すると，
$$
\begin{aligned}
\sum_{k=1}^{n-1} k &= \frac{n(n-1)}{2}
\end{aligned}
$$
となります。したがって，近似式は
$$
\finalanswer{Q_n \approx \exp\left( -\frac{n(n-1)}{730} \right)}
$$
となります。

### (3)
少なくとも2人の誕生日が一致する確率が $1/2$ 以上となる条件は，全員が異なる確率について $Q_n \le 1/2$ が満たされることです。小問 (2) の近似式を用いると，
$$
\begin{aligned}
\exp\left( -\frac{n(n-1)}{730} \right) &\le \frac{1}{2}
\end{aligned}
$$
となります。両辺の自然対数をとると，
$$
\begin{aligned}
-\frac{n(n-1)}{730} &\le -\ln 2 \\
n(n-1) &\ge 730 \ln 2
\end{aligned}
$$
が得られます。ここで $730 \ln 2 = 365 \times (2\ln 2) \approx 365 \times 1.386 \approx 505.89$ です。$n(n-1) \approx n^2$ とみなすと，$n \approx \sqrt{505.89} \approx 22.49$ と見積もられます。連続する整数の積を直接計算して判定すると，
$$
\begin{aligned}
n = 22 \text{ のとき} \quad 22 \times 21 &= 462 < 505.89 \\
n = 23 \text{ のとき} \quad 23 \times 22 &= 506 > 505.89
\end{aligned}
$$
となります。したがって，条件を満たす最小の整数は
$$
\finalanswer{n = 23}
$$
となります。わずか23人の集まりであっても，半数以上の確率で誕生日の一致が発生します。

===== FILE: 13probability_statistics/06/06_030.md =====
---
tags:
  - 標準
---

# 多項分布

## 問題
独立な試行を $n$ 回行う。各試行において互いに排他的な $k$ 個の事象 $A_1, A_2, \dots, A_k$ のいずれか1つが必ず起こり，それぞれの生起確率を $p_1, p_2, \dots, p_k$ とする（$p_i > 0$，$\sum_{i=1}^k p_i = 1$）。$n$ 回の試行のうち事象 $A_i$ が起こる回数を表す確率変数を $X_i$ とする。以下の問いに答えよ。

(1) 各 $X_i$ の周辺分布の名称を答え，期待値 $E[X_i]$ および分散 $V[X_i]$ を求めよ。

(2) $i \ne j$ とするとき，積の期待値 $E[X_i X_j]$ を求めよ。

(3) $i \ne j$ とするとき，$X_i$ と $X_j$ の共分散 $\operatorname{Cov}(X_i, X_j)$ を求めよ。

---

## 解答・解説

### (1)
各試行において事象 $A_i$ が起こる確率は $p_i$，起こらない確率は $1 - p_i$ です。他の事象の区別を無視すると，事象 $A_i$ の生起回数 $X_i$ は，成功確率 $p_i$，試行回数 $n$ の二項分布に従います。二項分布の公式より，期待値および分散は
$$
\begin{aligned}
E[X_i] &= \finalanswer{n p_i} \\
V[X_i] &= \finalanswer{n p_i (1 - p_i)}
\end{aligned}
$$
となります。周辺分布の名称は二項分布です。

### (2)
第 $m$ 回目（$m = 1, 2, \dots, n$）の試行において事象 $A_i$ が起これば 1，起こらなければ 0 をとる指示確率変数を $I_{i,m}$ と定義します。このとき，$X_i = \sum_{m=1}^n I_{i,m}$ と表されます。確率変数の積を展開すると，
$$
\begin{aligned}
X_i X_j &= \left( \sum_{m=1}^n I_{i,m} \right) \left( \sum_{l=1}^n I_{j,l} \right) \\
&= \sum_{m=1}^n I_{i,m} I_{j,m} + \sum_{m \ne l} I_{i,m} I_{j,l}
\end{aligned}
$$
となります。同一の試行において事象 $A_i$ と $A_j$（$i \ne j$）は排他的であるため，同時に起こることはなく $I_{i,m} I_{j,m} = 0$ です。一方，異なる試行 $m \ne l$ では独立であるため，期待値の積に分解できます。
$$
\begin{aligned}
E[I_{i,m} I_{j,l}] &= E[I_{i,m}] E[I_{j,l}] \\
&= p_i p_j
\end{aligned}
$$
$m \ne l$ を満たすペア $(m, l)$ の総数は $n(n-1)$ 個です。期待値をとると，
$$
\begin{aligned}
E[X_i X_j] &= 0 + \sum_{m \ne l} p_i p_j \\
&= n(n-1) p_i p_j
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{E[X_i X_j] = n(n-1) p_i p_j}
$$
となります。

### (3)
共分散の定義式 $\operatorname{Cov}(X_i, X_j) = E[X_i X_j] - E[X_i] E[X_j]$ を用います。小問 (1) および (2) の結果を代入すると，
$$
\begin{aligned}
\operatorname{Cov}(X_i, X_j) &= n(n-1) p_i p_j - (n p_i)(n p_j) \\
&= (n^2 - n) p_i p_j - n^2 p_i p_j \\
&= -n p_i p_j
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{\operatorname{Cov}(X_i, X_j) = -n p_i p_j}
$$
となります。全体の合計回数が $\sum_{i=1}^k X_i = n$ と固定されているため，一方の事象が多く起これば他方は起こりにくくなり，共分散は常に負となります。

===== FILE: 13probability_statistics/06/06_040.md =====
---
tags:
  - 標準
---

# コーシー分布

## 問題
確率変数 $X$ の確率密度関数が
$$
f(x) = \frac{1}{\pi (1 + x^2)} \quad (-\infty < x < \infty)
$$
で与えられる標準コーシー分布を考える。以下の問いに答えよ。

(1) 全区間積分が規格化条件 $\int_{-\infty}^\infty f(x) dx = 1$ を満たすことを示せ。

(2) 有限な積分範囲での積分 $\int_0^R x f(x) dx$ を計算し，$R \to \infty$ の極限を調べよ。また，この結果からコーシー分布の期待値 $E[X]$ が定義されない理由を説明せよ。

(3) 独立に標準コーシー分布に従う2つの確率変数 $X_1, X_2$ に対し，標本平均 $\bar{X} = (X_1 + X_2)/2$ の特性関数 $\phi_{\bar{X}}(t) = E[e^{i t \bar{X}}]$ を求めよ。ただし，$X$ の特性関数が $\phi(t) = e^{-|t|}$ であることを用いてよい。

---

## 解答・解説

### (1)
確率密度関数の不定積分を計算します。$1/(1+x^2)$ の原始関数は逆正接関数 $\arctan x$ です。広義積分を実行すると，
$$
\begin{aligned}
\int_{-\infty}^\infty f(x) dx &= \frac{1}{\pi} \lim_{R \to \infty} \int_{-R}^R \frac{1}{1 + x^2} dx \\
&= \frac{1}{\pi} \lim_{R \to \infty} \left[ \arctan x \right]_{-R}^R \\
&= \frac{1}{\pi} \left( \frac{\pi}{2} - \left( -\frac{\pi}{2} \right) \right) \\
&= \finalanswer{1}
\end{aligned}
$$
となり，全区間での積分が 1 となることが示されました。

### (2)
正の領域における期待値の積分を有限区間 $[0, R]$ で実行します。分子が分母の導関数の定数倍になっていることに着目すると，
$$
\begin{aligned}
\int_0^R x f(x) dx &= \frac{1}{\pi} \int_0^R \frac{x}{1 + x^2} dx \\
&= \frac{1}{2\pi} \left[ \ln(1 + x^2) \right]_0^R \\
&= \finalanswer{\frac{1}{2\pi} \ln(1 + R^2)}
\end{aligned}
$$
となります。ここで $R \to \infty$ の極限をとると，
$$
\begin{aligned}
\lim_{R \to \infty} \int_0^R x f(x) dx &= \infty
\end{aligned}
$$
となり正の無限大へ発散します。同様に，負の領域からの寄与は $-\infty$ に発散します。数学的に期待値 $E[X] = \int_{-\infty}^\infty x f(x) dx$ が定義されるためには，絶対可積分条件 $\int_{-\infty}^\infty |x| f(x) dx < \infty$ が満たされる必要があります。本問では正負両方の寄与が発散して不定形 $\infty - \infty$ となるため，期待値は定義されません。

### (3)
標本平均 $\bar{X} = X_1/2 + X_2/2$ の特性関数の定義式に代入します。$X_1$ と $X_2$ は互いに独立であるため，積の期待値は期待値の積に分解されます。
$$
\begin{aligned}
\phi_{\bar{X}}(t) &= E\left[ \exp\left( i t \frac{X_1 + X_2}{2} \right) \right] \\
&= E\left[ \exp\left( i \frac{t}{2} X_1 \right) \exp\left( i \frac{t}{2} X_2 \right) \right] \\
&= E\left[ \exp\left( i \frac{t}{2} X_1 \right) \right] E\left[ \exp\left( i \frac{t}{2} X_2 \right) \right] \\
&= \phi\left( \frac{t}{2} \right) \phi\left( \frac{t}{2} \right)
\end{aligned}
$$
与えられた特性関数 $\phi(t) = e^{-|t|}$ を代入すると，
$$
\begin{aligned}
\phi_{\bar{X}}(t) &= \exp\left( -\left|\frac{t}{2}\right| \right) \exp\left( -\left|\frac{t}{2}\right| \right) \\
&= \exp\left( -2 \times \frac{|t|}{2} \right) \\
&= e^{-|t|}
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{\phi_{\bar{X}}(t) = e^{-|t|}}
$$
となります。標本平均 $\bar{X}$ の特性関数がもとの確率変数 $X$ の特性関数と完全に一致することから，平均をとっても分布のばらつきが小さくならず，大数の法則が成立しないことがわかります。

===== FILE: 13probability_statistics/06/06_050.md =====
---
tags:
  - 標準
---

# 2変数ガウス分布と相関係数

## 問題
2つの確率変数 $X$ と $Y$ の同時確率密度関数が
$$
f(x, y) = \frac{1}{2\pi \sigma_X \sigma_Y \sqrt{1-\rho^2}} \exp\left[ -\frac{1}{2(1-\rho^2)} \left( \frac{x^2}{\sigma_X^2} - \frac{2\rho x y}{\sigma_X \sigma_Y} + \frac{y^2}{\sigma_Y^2} \right) \right]
$$
で与えられている。ここで $\sigma_X > 0$，$\sigma_Y > 0$，$-1 < \rho < 1$ である。以下の問いに答えよ。

(1) 指数関数の括弧内の式を $y$ について平方完成せよ。

(2) $y$ について全区間積分することにより，$X$ の周辺確率密度関数 $f_X(x) = \int_{-\infty}^\infty f(x, y) dy$ を求めよ。

(3) $X = x$ を与えたときの $Y$ の条件付き確率密度関数 $f_{Y|X}(y|x) = \frac{f(x, y)}{f_X(x)}$ を求め，条件付き期待値 $E[Y|X=x]$ を求めよ。

---

## 解答・解説

### (1)
指数関数の肩にある括弧内の2次式を $y$ の降べきの順に整理して平方完成します。
$$
\begin{aligned}
\frac{y^2}{\sigma_Y^2} - \frac{2\rho x}{\sigma_X \sigma_Y} y + \frac{x^2}{\sigma_X^2} &= \left( \frac{y}{\sigma_Y} - \frac{\rho x}{\sigma_X} \right)^2 - \frac{\rho^2 x^2}{\sigma_X^2} + \frac{x^2}{\sigma_X^2} \\
&= \frac{1}{\sigma_Y^2} \left( y - \rho \frac{\sigma_Y}{\sigma_X} x \right)^2 + (1 - \rho^2) \frac{x^2}{\sigma_X^2}
\end{aligned}
$$
となります。これに係数 $-1/\{2(1-\rho^2)\}$ を乗じると，
$$
\begin{aligned}
-\frac{1}{2(1-\rho^2)} \left( \frac{x^2}{\sigma_X^2} - \frac{2\rho x y}{\sigma_X \sigma_Y} + \frac{y^2}{\sigma_Y^2} \right) &= -\frac{x^2}{2\sigma_X^2} - \frac{\left( y - \rho \frac{\sigma_Y}{\sigma_X} x \right)^2}{2\sigma_Y^2 (1-\rho^2)}
\end{aligned}
$$
が得られます。したがって，括弧内の平方完成の形は
$$
\finalanswer{\frac{1}{\sigma_Y^2} \left( y - \rho \frac{\sigma_Y}{\sigma_X} x \right)^2 + (1 - \rho^2) \frac{x^2}{\sigma_X^2}}
$$
となります。

### (2)
小問 (1) の変形を用いると，同時確率密度関数は $x$ のみの部分と $y$ を含む部分の積に分解されます。
$$
\begin{aligned}
f(x, y) &= \frac{e^{-\frac{x^2}{2\sigma_X^2}}}{\sqrt{2\pi}\sigma_X} \times \frac{1}{\sqrt{2\pi}\sigma_Y\sqrt{1-\rho^2}} \exp\left[ -\frac{\left( y - \rho \frac{\sigma_Y}{\sigma_X} x \right)^2}{2\sigma_Y^2 (1-\rho^2)} \right]
\end{aligned}
$$
$y$ について $-\infty$ から $\infty$ まで積分します。$y$ に関する積分部分は，平均 $\rho \frac{\sigma_Y}{\sigma_X} x$，分散 $\sigma_Y^2 (1-\rho^2)$ の1次元正規分布の全区間積分であるため，積分値は 1 となります。
$$
\begin{aligned}
\int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}\sigma_Y\sqrt{1-\rho^2}} \exp\left[ -\frac{\left( y - \rho \frac{\sigma_Y}{\sigma_X} x \right)^2}{2\sigma_Y^2 (1-\rho^2)} \right] dy &= 1
\end{aligned}
$$
したがって，残った $x$ の関数が周辺確率密度関数となります。
$$
\finalanswer{f_X(x) = \frac{1}{\sqrt{2\pi}\sigma_X} \exp\left( -\frac{x^2}{2\sigma_X^2} \right)}
$$
となります。これは平均 0，分散 $\sigma_X^2$ の正規分布です。

### (3)
条件付き確率密度関数の定義式に従って比を計算します。
$$
\begin{aligned}
f_{Y|X}(y|x) &= \frac{f(x, y)}{f_X(x)} \\
&= \frac{1}{\sqrt{2\pi}\sigma_Y\sqrt{1-\rho^2}} \exp\left[ -\frac{\left( y - \rho \frac{\sigma_Y}{\sigma_X} x \right)^2}{2\sigma_Y^2 (1-\rho^2)} \right]
\end{aligned}
$$
となります。したがって，条件付き分布は
$$
\finalanswer{f_{Y|X}(y|x) = \frac{1}{\sqrt{2\pi}\sigma_Y\sqrt{1-\rho^2}} \exp\left[ -\frac{\left( y - \rho \frac{\sigma_Y}{\sigma_X} x \right)^2}{2\sigma_Y^2 (1-\rho^2)} \right]}
$$
となります。これは正規分布の標準形と比較すると，平均が $\rho \frac{\sigma_Y}{\sigma_X} x$，分散が $\sigma_Y^2 (1-\rho^2)$ の正規分布であることがわかります。したがって，条件付き期待値は
$$
\finalanswer{E[Y|X=x] = \rho \frac{\sigma_Y}{\sigma_X} x}
$$
となります。相関係数 $\rho$ に比例して，$X$ の値に応じた $Y$ の期待値の線形回帰直線が得られます。

===== FILE: 13probability_statistics/06/06_060.md =====
---
tags:
  - 標準
---

# ガンマ分布

## 問題
同一のパラメータ $\lambda > 0$ をもつ指数分布に独立に従う $n$ 個の確率変数を $X_1, X_2, \dots, X_n$ とする。各 $X_i$ の確率密度関数は
$$
f(x) = \lambda e^{-\lambda x} \quad (x \ge 0)
$$
である（$x < 0$ では $f(x) = 0$）。以下の問いに答えよ。

(1) 各 $X_i$ の積率母関数 $M_X(\theta) = E[e^{\theta X}]$ を求めよ（$\theta < \lambda$）。

(2) 和 $S_n = \sum_{i=1}^n X_i$ の積率母関数 $M_{S_n}(\theta)$ を求めよ。

(3) パラメータ $n, \lambda$ のガンマ分布 $\Gamma(n, \lambda)$ の確率密度関数
$$
f_n(s) = \frac{\lambda^n}{(n-1)!} s^{n-1} e^{-\lambda s} \quad (s \ge 0)
$$
の積率母関数を計算し，和 $S_n$ の確率分布がガンマ分布 $\Gamma(n, \lambda)$ に一致することを示せ。

---

## 解答・解説

### (1)
積率母関数の定義に基づいて積分を実行します。$\theta < \lambda$ の条件のもとで，
$$
\begin{aligned}
M_X(\theta) &= \int_0^\infty e^{\theta x} \lambda e^{-\lambda x} dx \\
&= \lambda \int_0^\infty e^{-(\lambda - \theta)x} dx \\
&= \lambda \left[ -\frac{1}{\lambda - \theta} e^{-(\lambda - \theta)x} \right]_0^\infty \\
&= \frac{\lambda}{\lambda - \theta}
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{M_X(\theta) = \left( 1 - \frac{\theta}{\lambda} \right)^{-1}}
$$
となります。

### (2)
$S_n = \sum_{i=1}^n X_i$ の積率母関数を考えます。$X_1, \dots, X_n$ は互いに独立であるため，指数法則により積の期待値は各確率変数の積率母関数の積に等しくなります。
$$
\begin{aligned}
M_{S_n}(\theta) &= E\left[ \exp\left( \theta \sum_{i=1}^n X_i \right) \right] \\
&= E\left[ \prod_{i=1}^n e^{\theta X_i} \right] \\
&= \prod_{i=1}^n E\left[ e^{\theta X_i} \right] \\
&= \{ M_X(\theta) \}^n
\end{aligned}
$$
小問 (1) の結果を代入すると，
$$
\finalanswer{M_{S_n}(\theta) = \left( 1 - \frac{\theta}{\lambda} \right)^{-n}}
$$
となります。

### (3)
密度関数 $f_n(s)$ から直接，積率母関数を計算します。
$$
\begin{aligned}
M(\theta) &= \int_0^\infty e^{\theta s} f_n(s) ds \\
&= \int_0^\infty e^{\theta s} \frac{\lambda^n}{(n-1)!} s^{n-1} e^{-\lambda s} ds \\
&= \frac{\lambda^n}{(n-1)!} \int_0^\infty s^{n-1} e^{-(\lambda - \theta)s} ds
\end{aligned}
$$
ここで変数変換 $u = (\lambda - \theta)s$ を行うと，$ds = du/(\lambda - \theta)$ となります。積分範囲は $0$ から $\infty$ のままです。
$$
\begin{aligned}
\int_0^\infty s^{n-1} e^{-(\lambda - \theta)s} ds &= \int_0^\infty \left( \frac{u}{\lambda - \theta} \right)^{n-1} e^{-u} \frac{du}{\lambda - \theta} \\
&= \frac{1}{(\lambda - \theta)^n} \int_0^\infty u^{n-1} e^{-u} du
\end{aligned}
$$
ガンマ関数の定義より $\int_0^\infty u^{n-1} e^{-u} du = \Gamma(n) = (n-1)!$ です。これを代入すると，
$$
\begin{aligned}
M(\theta) &= \frac{\lambda^n}{(n-1)!} \frac{(n-1)!}{(\lambda - \theta)^n} \\
&= \left( \frac{\lambda}{\lambda - \theta} \right)^n \\
&= \finalanswer{\left( 1 - \frac{\theta}{\lambda} \right)^{-n}}
\end{aligned}
$$
が得られます。この式は小問 (2) で求めた和 $S_n$ の積率母関数 $M_{S_n}(\theta)$ と完全に一致します。積率母関数と確率分布の1対1対応性（一意性）により，和 $S_n$ の確率分布はガンマ分布 $\Gamma(n, \lambda)$ に一致することが示されました。

===== FILE: 13probability_statistics/06/06_070.md =====
---
tags:
  - 標準
---

# 二項分布のガウス近似

## 問題
成功確率 $p$（$0 < p < 1$），失敗確率 $q = 1-p$ の試行を $n$ 回行う二項分布
$$
P(X = k) = \binom{n}{k} p^k q^{n-k}
$$
において，$n$ が非常に大きく，$k$ が平均値 $np$ の近傍にある場合を考える。偏差を $x = k - np$ とおく（$|x| \ll np, nq$）。スターリングの公式
$$
\ln (m!) \approx m \ln m - m + \frac{1}{2} \ln(2\pi m)
$$
を用いる。以下の問いに答えよ。

(1) $\ln P(X=k)$ にスターリングの公式を適用し，$n, k, n-k$ を用いた対数表現を導け。

(2) $k = np + x$，$n-k = nq - x$ を代入し，$\ln(1+u) \approx u - u^2/2$ を用いて $\ln P(X=k)$ を $x$ の2次の項まで展開せよ。

(3) 前問の結果から，二項分布の確率がガウス分布
$$
P(X = k) \approx \frac{1}{\sqrt{2\pi n p q}} \exp\left( -\frac{x^2}{2 n p q} \right)
$$
で近似できることを示せ。

---

## 解答・解説

### (1)
二項分布の確率の自然対数をとると，階乗の和と差に分解されます。
$$
\begin{aligned}
\ln P(X = k) &= \ln(n!) - \ln(k!) - \ln((n-k)!) + k \ln p + (n-k) \ln q
\end{aligned}
$$
各階乗に対してスターリングの公式を適用します。一次の項は $n - k - (n-k) = 0$ となり相殺します。残った項をまとめると，
$$
\begin{aligned}
\ln P(X = k) &\approx n \ln n - k \ln k - (n-k)\ln(n-k) + k \ln p + (n-k) \ln q \\
&\quad + \frac{1}{2} \ln \frac{2\pi n}{(2\pi k)(2\pi (n-k))} \\
&= -k \ln \frac{k}{np} - (n-k) \ln \frac{n-k}{nq} - \frac{1}{2} \ln \left( \frac{2\pi k(n-k)}{n} \right)
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{\ln P(X=k) \approx -k \ln \frac{k}{np} - (n-k) \ln \frac{n-k}{nq} - \frac{1}{2} \ln \left( \frac{2\pi k(n-k)}{n} \right)}
$$
となります。

### (2)
$k = np + x$ および $n-k = nq - x$ を各対数項に代入します。
$$
\begin{aligned}
\ln \frac{k}{np} &= \ln \left( 1 + \frac{x}{np} \right) \approx \frac{x}{np} - \frac{x^2}{2n^2 p^2} \\
\ln \frac{n-k}{nq} &= \ln \left( 1 - \frac{x}{nq} \right) \approx -\frac{x}{nq} - \frac{x^2}{2n^2 q^2}
\end{aligned}
$$
これらを用いて主要項を展開します。
$$
\begin{aligned}
-k \ln \frac{k}{np} &= -(np + x) \left( \frac{x}{np} - \frac{x^2}{2n^2 p^2} \right) \\
&\approx -x + \frac{x^2}{2np} - \frac{x^2}{np} \\
&= -x - \frac{x^2}{2np}
\end{aligned}
$$
同様に，第2項を展開します。
$$
\begin{aligned}
-(n-k) \ln \frac{n-k}{nq} &= -(nq - x) \left( -\frac{x}{nq} - \frac{x^2}{2n^2 q^2} \right) \\
&\approx x + \frac{x^2}{2nq} - \frac{x^2}{nq} \\
&= x - \frac{x^2}{2nq}
\end{aligned}
$$
これら2つの和をとると，$x$ の1次の項が打ち消し合います。
$$
\begin{aligned}
-k \ln \frac{k}{np} - (n-k) \ln \frac{n-k}{nq} &\approx -x - \frac{x^2}{2np} + x - \frac{x^2}{2nq} \\
&= -\frac{x^2}{2n} \left( \frac{1}{p} + \frac{1}{q} \right) \\
&= -\frac{x^2}{2n} \frac{p+q}{pq} \\
&= -\frac{x^2}{2npq}
\end{aligned}
$$
また，対数内の前駆係数は最低次として $k \approx np$，$n-k \approx nq$ を代入すると，
$$
\begin{aligned}
-\frac{1}{2} \ln \left( \frac{2\pi k(n-k)}{n} \right) &\approx -\frac{1}{2} \ln (2\pi npq)
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{\ln P(X=k) \approx -\frac{1}{2} \ln(2\pi npq) - \frac{x^2}{2npq}}
$$
となります。

### (3)
小問 (2) で得られた対数の展開式について，両辺の指数をとります。
$$
\begin{aligned}
P(X = k) &\approx \exp\left( -\frac{1}{2} \ln(2\pi npq) - \frac{x^2}{2npq} \right) \\
&= \exp\left( \ln \frac{1}{\sqrt{2\pi npq}} \right) \exp\left( -\frac{x^2}{2npq} \right) \\
&= \finalanswer{\frac{1}{\sqrt{2\pi n p q}} \exp\left( -\frac{x^2}{2 n p q} \right)}
\end{aligned}
$$
が得られます。これにより，二項分布が平均 $np$，分散 $npq$ のガウス分布（ド・モアブル–ラプラスの極限定理）によって精度よく近似できることが示されました。

===== FILE: 13probability_statistics/06/06_080.md =====
---
tags:
  - 発展
---

# ランダムウォークの初到達

## 問題
数直線上の単純ランダムウォークを考える。原点 $X_0 = 0$ を出発し，各ステップで独立に確率 $1/2$ で $+1$，確率 $1/2$ で $-1$ 移動する。ステップ $n$ における位置を $X_n$ とする。正の整数 $a$ に対し，ウォークがステップ $n$ で初めて位置 $a$ に到達する確率を考える（図）。以下の問いに答えよ。

<!-- FIGURE problem: 横軸にステップ数 n（0 から n までの目盛り），縦軸に位置 x（原点 O，位置 a，位置 b，位置 2a-b の目盛り）をとる。原点から出発して途中で初めて直線 x=a に達し，その後ステップ n で x=b（b < a）に至る折れ線パスを描く。直線 x=a に初めて達した点から終点までの軌跡を，直線 x=a に関して線対称に折り返して終点 x=2a-b に至る点線のパスを描く。 -->

(1) ステップ $n$ で位置 $b$（$b < a$）にあり，途中で少なくとも1度は位置 $a$ に達したパスの総数は，原点からステップ $n$ で位置 $2a - b$ に至るパスの総数に等しいことを，鏡像原理（反射原理）を用いて示せ。

(2) ステップ $n$ で初めて位置 $a$ に到達するパスの総数 $N(n, a)$ を求めよ（$n \ge a$，$n - a$ は偶数）。

(3) ステップ $n$ で初めて位置 $a$ に到達する確率 $f_a(n)$ を求めよ。

---

## 解答・解説

### (1)
原点から出発して途中で直線 $x = a$ に達し，時刻 $n$ で位置 $b$（$b < a$）に至る任意のパスを考えます。パスが初めて $x = a$ に到達する時刻を $\tau$（$1 \le \tau \le n$）とします。

時刻 $\tau$ 以降（$\tau \le t \le n$）の軌跡を，直線 $x = a$ に関して線対称に折り返します。対称移動によって位置 $x$ は $x' = a - (x - a) = 2a - x$ に変換されます。したがって，終点 $X_n = b$ は
$$
\begin{aligned}
X_n' &= 2a - b
\end{aligned}
$$
に移ります。$2a - b > a$ であるため，原点から $2a - b$ に至るいかなるパスも必ず途中で直線 $x = a$ を通過します。この折り返し操作は，途中で $a$ を通って $b$ に至るパスと，原点から $2a - b$ に至るパスとの間に1対1の全単射を与えます。したがって，両者のパスの総数は等しく，
$$
\finalanswer{N(\text{途中 } a \text{ を経由して } X_n = b) = N(X_n = 2a - b)}
$$
が示されました。

### (2)
ステップ $n$ で初めて位置 $a$ に達するためには，ステップ $n-1$ で位置 $a-1$ にいて，最後のステップで $+1$ 移動しなければなりません。さらに，ステップ $n-1$ までの間に一度も位置 $a$ に達してはならないという条件がつきます。

したがって，求めるパスの総数は，ステップ $n-1$ で位置 $a-1$ に至る全パス数から，ステップ $n-1$ までに位置 $a$ を通過して $a-1$ に達するパス数を引いたものとなります。小問 (1) の鏡像原理において $n \to n-1$，$b = a-1$ とすると，途中で $a$ を経由するパス数は原点から $2a - (a-1) = a+1$ に至るパス数に等しくなります。ステップ $m$ で位置 $y$ に至るパス数は二項係数を用いて $\binom{m}{(m+y)/2}$ と表せるので，
$$
\begin{aligned}
N(n, a) &= \binom{n-1}{\frac{(n-1)+(a-1)}{2}} - \binom{n-1}{\frac{(n-1)+(a+1)}{2}} \\
&= \binom{n-1}{\frac{n+a-2}{2}} - \binom{n-1}{\frac{n+a}{2}}
\end{aligned}
$$
となります。ここで $k = (n+a)/2$ とおくと，
$$
\begin{aligned}
N(n, a) &= \binom{n-1}{k-1} - \binom{n-1}{k} \\
&= \frac{(n-1)!}{(k-1)!(n-k)!} - \frac{(n-1)!}{k!(n-k-1)!} \\
&= \frac{(n-1)!}{k!(n-k)!} \{ k - (n-k) \} \\
&= \frac{(n-1)!}{k!(n-k)!} (2k - n)
\end{aligned}
$$
となります。$2k - n = a$ であるため，
$$
\begin{aligned}
N(n, a) &= \frac{a}{n} \frac{n!}{k!(n-k)!} \\
&= \frac{a}{n} \binom{n}{k}
\end{aligned}
$$
となります。$k$ を元に戻すと，
$$
\finalanswer{N(n, a) = \frac{a}{n} \binom{n}{\frac{n+a}{2}}}
$$
となります。

### (3)
各ステップでの移動の確率はそれぞれ $1/2$ であり，互いに独立です。したがって，長さ $n$ の任意のパスが生起する確率は等しく $(1/2)^n$ です。小問 (2) で求めたパスの総数にこの確率をかけると，
$$
\begin{aligned}
f_a(n) &= N(n, a) \left( \frac{1}{2} \right)^n \\
&= \frac{a}{n} \binom{n}{\frac{n+a}{2}} \left( \frac{1}{2} \right)^n
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{f_a(n) = \frac{a}{n} \binom{n}{\frac{n+a}{2}} \left( \frac{1}{2} \right)^n}
$$
となります。この確率は，ステップ $n$ で位置 $a$ にいる確率 $P(X_n = a)$ に因子 $a/n$ を乗じた形となっています。

===== FILE: 13probability_statistics/06/06_090.md =====
---
tags:
  - 標準
---

# ベイズ推定

## 問題
あるコインを投げたときに表が出る確率を $\theta$（$0 \le \theta \le 1$）とする。$\theta$ の事前分布として，パラメータ $\alpha > 0, \beta > 0$ をもつベータ分布
$$
p(\theta) = \frac{1}{B(\alpha, \beta)} \theta^{\alpha - 1} (1 - \theta)^{\beta - 1}
$$
を採用する。ただし $B(\alpha, \beta) = \int_0^1 \theta^{\alpha-1} (1-\theta)^{\beta-1} d\theta$ はベータ関数である。このコインを独立に $n$ 回投げたところ，表が $k$ 回，裏が $n-k$ 回出た。以下の問いに答えよ。

(1) 得られたデータのもとでの $\theta$ の事後分布 $p(\theta|k)$ を求めよ。

(2) 二乗誤差損失のもとでのベイズ推定量である事後期待値 $\hat{\theta}_{\mathrm{Bayes}} = E[\theta|k]$ を求めよ。ただし，ベータ分布 $\mathrm{Beta}(a, b)$ の期待値が $a/(a+b)$ であることを用いてよい。

(3) 事後期待値 $\hat{\theta}_{\mathrm{Bayes}}$ は，最尤推定量 $\hat{\theta}_{\mathrm{ML}} = k/n$ と事前期待値 $E[\theta] = \alpha/(\alpha+\beta)$ の重み付き内分（凸結合）として表せることを示せ。

---

## 解答・解説

### (1)
コインを $n$ 回投げて表が $k$ 回出る尤度関数は二項分布に従います。
$$
\begin{aligned}
L(k|\theta) &= \binom{n}{k} \theta^k (1 - \theta)^{n-k}
\end{aligned}
$$
ベイズの定理により，事後分布 $p(\theta|k)$ は尤度と事前分布の積に比例します。
$$
\begin{aligned}
p(\theta|k) &\propto L(k|\theta) p(\theta) \\
&\propto \left\{ \theta^k (1 - \theta)^{n-k} \right\} \left\{ \theta^{\alpha - 1} (1 - \theta)^{\beta - 1} \right\} \\
&= \theta^{(\alpha + k) - 1} (1 - \theta)^{(\beta + n - k) - 1}
\end{aligned}
$$
この核はパラメータ $\alpha' = \alpha + k$，$\beta' = \beta + n - k$ のベータ分布の形をしています。規格化定数を補うと，
$$
\finalanswer{p(\theta|k) = \frac{1}{B(\alpha + k, \beta + n - k)} \theta^{\alpha + k - 1} (1 - \theta)^{\beta + n - k - 1}}
$$
となります。事前分布と事後分布が同一の関数族に属する共役事前分布の関係となっています。

### (2)
事後分布はパラメータ $\alpha + k$ および $\beta + n - k$ のベータ分布に従います。与えられたベータ分布の期待値の公式において，$a = \alpha + k$，$b = \beta + n - k$ と対応させると，
$$
\begin{aligned}
\hat{\theta}_{\mathrm{Bayes}} &= \frac{a}{a + b} \\
&= \frac{\alpha + k}{(\alpha + k) + (\beta + n - k)} \\
&= \frac{\alpha + k}{\alpha + \beta + n}
\end{aligned}
$$
となります。したがって，事後期待値は
$$
\finalanswer{\hat{\theta}_{\mathrm{Bayes}} = \frac{\alpha + k}{\alpha + \beta + n}}
$$
となります。

### (3)
小問 (2) で得られた事後期待値を，最尤推定量 $\hat{\theta}_{\mathrm{ML}} = k/n$ と事前期待値 $E[\theta] = \alpha/(\alpha+\beta)$ を含む形に変形します。分子の各項をそれぞれの期待値で括り出すと，
$$
\begin{aligned}
\hat{\theta}_{\mathrm{Bayes}} &= \frac{\alpha}{\alpha + \beta + n} + \frac{k}{\alpha + \beta + n} \\
&= \frac{\alpha + \beta}{\alpha + \beta + n} \left( \frac{\alpha}{\alpha + \beta} \right) + \frac{n}{\alpha + \beta + n} \left( \frac{k}{n} \right)
\end{aligned}
$$
となります。ここで重みとして
$$
\begin{aligned}
w &= \frac{n}{\alpha + \beta + n}
\end{aligned}
$$
を定義すると，$1 - w = (\alpha + \beta)/(\alpha + \beta + n)$ となります。これを用いて書き直すと，
$$
\finalanswer{\hat{\theta}_{\mathrm{Bayes}} = (1 - w) E[\theta] + w \hat{\theta}_{\mathrm{ML}}}
$$
が得られます。重み $w$ は $0 < w < 1$ を満たすため，事後期待値は事前期待値と最尤推定量の内分点となっています。データ数 $n$ が小さいときは事前情報が重視され，$n \to \infty$ の極限では $w \to 1$ となり最尤推定量に一致します。

===== FILE: 13probability_statistics/06/06_100.md =====
---
tags:
  - 標準
---

# ブラウン運動の平均二乗変位

## 問題
粘性流体中における質量 $m$ の微粒子の1次元ブラウン運動を考える。粒子の位置を $x(t)$，速度を $v(t) = dx/dt$，流体の粘性抵抗係数を $\gamma$（$\gamma > 0$）とする。微粒子はランジュバン方程式
$$
m \frac{dv}{dt} = -\gamma v + R(t)
$$
に従う。ここでランダム力 $R(t)$ は平均がゼロ（$\langle R(t) \rangle = 0$）であり，位置との相関をもたない（$\langle x(t) R(t) \rangle = 0$）。系は温度 $T$ の熱平衡状態にあり，エネルギー等分配則 $\langle m v^2 \rangle = k_B T$（$k_B$ はボルツマン定数）が成り立つ。以下の問いに答えよ。

(1) 関係式 $x \frac{dx}{dt} = \frac{1}{2}\frac{d}{dt}(x^2)$ および $x \frac{dv}{dt} = \frac{1}{2}\frac{d^2}{dt^2}(x^2) - v^2$ を用いて，平均二乗変位 $u(t) = \langle x(t)^2 \rangle$ が満たす微分方程式を導け。

(2) 長時間領域（$t \gg m/\gamma$）において，慣性項 $m \frac{d^2 u}{dt^2}$ を無視できる場合の微分方程式を解き，$u(t)$ を求めよ。ただし $x(0) = 0$ とする。

(3) アインシュタインの拡散係数 $D = \frac{k_B T}{\gamma}$ を用いて，長時間極限における平均二乗変位 $u(t)$ を表せ。

---

## 解答・解説

### (1)
ランジュバン方程式の両辺に位置 $x(t)$ を乗じます。
$$
\begin{aligned}
m x \frac{dv}{dt} &= -\gamma x v + x R(t)
\end{aligned}
$$
与えられた恒等式
$$
\begin{aligned}
x v &= \frac{1}{2}\frac{d}{dt}(x^2) \\
x \frac{dv}{dt} &= \frac{1}{2}\frac{d^2}{dt^2}(x^2) - v^2
\end{aligned}
$$
を代入すると，
$$
\begin{aligned}
m \left( \frac{1}{2}\frac{d^2}{dt^2}(x^2) - v^2 \right) &= -\frac{\gamma}{2}\frac{d}{dt}(x^2) + x R(t)
\end{aligned}
$$
となります。両辺のアンサンブル平均をとります。$\langle x R(t) \rangle = 0$ であり，微分の演算とアンサンブル平均は交換可能です。
$$
\begin{aligned}
\frac{m}{2} \frac{d^2 \langle x^2 \rangle}{dt^2} - m \langle v^2 \rangle &= -\frac{\gamma}{2} \frac{d\langle x^2 \rangle}{dt}
\end{aligned}
$$
平均二乗変位 $u(t) = \langle x(t)^2 \rangle$ を用い，等分配則 $m \langle v^2 \rangle = k_B T$ を代入して両辺を2倍すると，
$$
\finalanswer{m \frac{d^2 u}{dt^2} + \gamma \frac{du}{dt} = 2 k_B T}
$$
が得られます。

### (2)
特性時間 $t \gg m/\gamma$ の長時間領域では，第1項の慣性項 $m \frac{d^2 u}{dt^2}$ は粘性抵抗の項に比べて十分に小さく無視できます。したがって，微分方程式は
$$
\begin{aligned}
\gamma \frac{du}{dt} &= 2 k_B T
\end{aligned}
$$
と簡約されます。これを整理すると，
$$
\begin{aligned}
\frac{du}{dt} &= \frac{2 k_B T}{\gamma}
\end{aligned}
$$
となります。初期条件 $u(0) = \langle x(0)^2 \rangle = 0$ のもとで時間 $t$ について積分すると，
$$
\begin{aligned}
u(t) &= \int_0^t \frac{2 k_B T}{\gamma} dt' \\
&= \frac{2 k_B T}{\gamma} t
\end{aligned}
$$
となります。したがって，
$$
\finalanswer{u(t) = \frac{2 k_B T}{\gamma} t}
$$
となります。

### (3)
アインシュタインの関係式により，流体中の微粒子の拡散係数は $D = \frac{k_B T}{\gamma}$ で定義されます。小問 (2) で得られた平均二乗変位の式にこの定義を代入すると，
$$
\begin{aligned}
u(t) &= 2 \left( \frac{k_B T}{\gamma} \right) t \\
&= 2 D t
\end{aligned}
$$
となります。したがって，求める関係式は
$$
\finalanswer{u(t) = 2 D t}
$$
となります。微視的なランダム運動による変位の2乗平均が，巨視的な拡散係数 $D$ と時間 $t$ に比例して増大するというアインシュタインの拡散則が示されました。

===== FILE: 13probability_statistics/06/06_110.md =====
---
tags:
  - 標準
---

# 拡散方程式と確率の流れ

## 問題
1次元空間における粒子の確率密度関数を $P(x, t)$ とする。$P(x, t)$ は拡散方程式
$$
\frac{\partial P(x, t)}{\partial t} = D \frac{\partial^2 P(x, t)}{\partial x^2}
$$
を満たす（$D > 0$ は拡散係数）。確率の流れ（確率流密度）を $J(x, t) = -D \frac{\partial P(x, t)}{\partial x}$ で定義する。以下の問いに答えよ。

(1) 確率密度 $P$ と確率流密度 $J$ の間に連続の式
$$
\frac{\partial P}{\partial t} + \frac{\partial J}{\partial x} = 0
$$
が成り立つことを示せ。

(2) 無限遠において確率流がゼロ（$\lim_{x \to \pm\infty} J(x, t) = 0$）であるとき，全空間での確率の総和 $\int_{-\infty}^\infty P(x, t) dx$ が時間的に保存することを示せ。

(3) 時刻 $t = 0$ に原点にあった粒子に対する拡散方程式の基本解
$$
P(x, t) = \frac{1}{\sqrt{4\pi D t}} \exp\left( -\frac{x^2}{4 D t} \right) \quad (t > 0)
$$
を用いて，確率流密度 $J(x, t)$ を求めよ。

---

## 解答・解説

### (1)
確率流密度 $J(x, t) = -D \frac{\partial P}{\partial x}$ の空間微分を計算します。
$$
\begin{aligned}
\frac{\partial J}{\partial x} &= \frac{\partial}{\partial x} \left( -D \frac{\partial P}{\partial x} \right) \\
&= -D \frac{\partial^2 P}{\partial x^2}
\end{aligned}
$$
となります。拡散方程式 $\frac{\partial P}{\partial t} = D \frac{\partial^2 P}{\partial x^2}$ を用いて右辺を書き換えると，
$$
\begin{aligned}
\frac{\partial J}{\partial x} &= -\frac{\partial P}{\partial t}
\end{aligned}
$$
が得られます。移項して整理すると，
$$
\finalanswer{\frac{\partial P}{\partial t} + \frac{\partial J}{\partial x} = 0}
$$
となり，局所的な確率保存則を表す連続の式が成り立ちます。

### (2)
全確率 $I(t) = \int_{-\infty}^\infty P(x, t) dx$ の時間微分を計算します。積分の内側に時間微分を入れると，
$$
\begin{aligned}
\frac{d I(t)}{dt} &= \int_{-\infty}^\infty \frac{\partial P(x, t)}{\partial t} dx
\end{aligned}
$$
となります。小問 (1) の連続の式 $\frac{\partial P}{\partial t} = -\frac{\partial J}{\partial x}$ を代入すると，
$$
\begin{aligned}
\frac{d I(t)}{dt} &= \int_{-\infty}^\infty \left( -\frac{\partial J(x, t)}{\partial x} \right) dx \\
&= - \left[ J(x, t) \right]_{-\infty}^\infty \\
&= - \left( \lim_{x \to \infty} J(x, t) - \lim_{x \to -\infty} J(x, t) \right)
\end{aligned}
$$
となります。境界条件 $\lim_{x \to \pm\infty} J(x, t) = 0$ を適用すると，
$$
\begin{aligned}
\frac{d I(t)}{dt} &= 0
\end{aligned}
$$
が得られます。したがって，全確率の時間変化率はゼロであり，
$$
\finalanswer{\frac{d}{dt} \int_{-\infty}^\infty P(x, t) dx = 0}
$$
が成り立ち，全確率が時間的に不変（保存）であることが示されました。

### (3)
基本解 $P(x, t)$ を空間変数 $x$ で偏微分します。
$$
\begin{aligned}
\frac{\partial P(x, t)}{\partial x} &= \frac{1}{\sqrt{4\pi D t}} \frac{\partial}{\partial x} \exp\left( -\frac{x^2}{4 D t} \right) \\
&= \frac{1}{\sqrt{4\pi D t}} \left( -\frac{2x}{4 D t} \right) \exp\left( -\frac{x^2}{4 D t} \right) \\
&= -\frac{x}{2 D t} P(x, t)
\end{aligned}
$$
となります。確率流密度の定義式 $J(x, t) = -D \frac{\partial P}{\partial x}$ に代入すると，
$$
\begin{aligned}
J(x, t) &= -D \left( -\frac{x}{2 D t} P(x, t) \right) \\
&= \frac{x}{2 t} P(x, t)
\end{aligned}
$$
となります。$P(x, t)$ の表式を代入して整理すると，
$$
\finalanswer{J(x, t) = \frac{x}{4\sqrt{\pi D t^3}} \exp\left( -\frac{x^2}{4 D t} \right)}
$$
となります。$x > 0$ では $J > 0$（正の向きの流れ），$x < 0$ では $J < 0$（負の向きの流れ）となり，確率が原点から両側の外側に向かって対称に流出していく様子を表しています。

===== END =====