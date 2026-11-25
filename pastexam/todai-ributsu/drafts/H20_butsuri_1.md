---
title: 東大理物 平成20年度 物理学 第1問：2次元調和振動子の代数解法と極座標解法
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成20年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成20年度 物理学 第1問：2次元調和振動子の代数解法と極座標解法

## 問題

ハミルトニアンが

$$
\mathcal{H} = \frac{1}{2}\sum_{k=1}^{2}\left(\frac{p_k^2}{m} + m\omega^2 x_k^2\right)
$$

で与えられる2次元調和振動子の量子力学を考える。ここで $x_k$ は座標で $p_k$ はその正準運動量，$m$ は質量，$\hbar = h/2\pi$（$h$ はプランク定数），$\omega$ は角振動数である。正準交換関係は

$$
[x_k, p_l] = i\hbar\delta_{kl}, \quad [x_k, x_l] = [p_k, p_l] = 0, \qquad (k, l = 1, 2)
$$

である。このとき以下の設問に答えよ。

(1) 生成消滅演算子

$$
a_k^\dagger = \frac{1}{\sqrt{2\hbar}}\left(\sqrt{m\omega}x_k - i\frac{1}{\sqrt{m\omega}}p_k\right), \quad a_k = \frac{1}{\sqrt{2\hbar}}\left(\sqrt{m\omega}x_k + i\frac{1}{\sqrt{m\omega}}p_k\right), \qquad (k = 1, 2)
$$

がみたす交換関係を，$x_k, p_k$ の交換関係から導け。また，ハミルトニアン $\mathcal{H}$ を生成消滅演算子を用いて表せ。

(2) 基底状態 $|0\rangle$ は，消滅演算子を用いた条件

$$
a_k|0\rangle = 0, \qquad (k = 1, 2)
$$

により定義される。この定義式を，座標 $x_k$ を変数とする微分方程式に書き換え，対応する基底状態の波動関数 $\psi_0(r)$ を $r\ (=\sqrt{x_1^2 + x_2^2})$ の関数として求めよ。ただし，規格化因子を定める必要はない。

(3) ハミルトニアン $\mathcal{H}$ の全ての固有状態を基底状態 $|0\rangle$ と生成演算子で書き表し，それらの固有値を求めよ。また，各固有値に対する縮退度を求めよ。

次に2次元の極座標 $r, \theta\ (=\tan^{-1}(x_2/x_1))$ を用いた解析を行う。以下の設問では簡単のため $\hbar = m = \omega = 1$ とおく。必要であれば，2次元のラプラシアンの極座標表示

$$
\left(\frac{\partial^2}{\partial x_1^2} + \frac{\partial^2}{\partial x_2^2}\right)\psi = \frac{\partial^2\psi}{\partial r^2} + \frac{1}{r}\frac{\partial\psi}{\partial r} + \frac{1}{r^2}\frac{\partial^2\psi}{\partial\theta^2}
$$

を用いてよい。

(4) 波動関数を $\psi = R(r)\Theta(\theta)$ と変数分離し，シュレーディンガー方程式に代入する。$\theta$ 方向の方程式を解くと，$R(r)$ に関する微分方程式は

$$
\frac{\mathrm{d}^2 R}{\mathrm{d}r^2} + \frac{1}{r}\frac{\mathrm{d}R}{\mathrm{d}r} + \left(2E - r^2 - \frac{n^2}{r^2}\right)R = 0
$$

となることを導け。ここで $E$ はハミルトニアン $\mathcal{H}$ の固有値を表す。また，$n$ は角度方向の量子数であるが，それがどのような値をとるべきか，理由とともに述べよ。

(5) 設問2で求めた $\psi_0$ を用いて $R(r) = f(r)\psi_0(r)$ と書き換えると，$f(r)$ に対する微分方程式は

$$
\frac{\mathrm{d}^2 f}{\mathrm{d}r^2} + \frac{1}{r}(1 - 2r^2)\frac{\mathrm{d}f}{\mathrm{d}r} + \left(2E - 2 - \frac{n^2}{r^2}\right)f = 0
$$

となる。$f(r)$ を

$$
f(r) = r^\alpha \sum_{s=0}^{\infty} f_s r^s, \qquad (f_0 = 1)
$$

のようにべき級数展開するとき，$f(r)$ が原点 $r = 0$ で発散しないという条件を用いて実数パラメータ $\alpha$ を決定せよ。

(6) 設問5のべき級数が有限個の項からなるという条件から固有値 $E$ を求め，設問3で求めた固有値（ただし $\hbar = m = \omega = 1$ とおいたもの）と一致することを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成20年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2次元等方調和振動子は，直交座標では互いに独立な2つの1次元調和振動子の和に分かれます。生成消滅演算子を用いると，微分方程式を解かずに固有状態とエネルギー固有値，および縮退度を交換関係から直接求めることができます。

同じ系を極座標で書くと，回転対称性によって角度方向と動径方向に変数分離することができます。動径方程式から遠方の減衰因子 $\psi_0(r)$ をくくり出してべき級数展開すると，原点と無限遠で発散しない条件からエネルギー固有値が離散化されます。
</div>

### (1)

まず交換関係 $[a_k, a_l^\dagger]$ を正準交換関係 $[x_k, p_l] = i\hbar\delta_{kl}$，$[x_k, x_l] = [p_k, p_l] = 0$ から計算します。

$$
\begin{aligned}
[a_k, a_l^\dagger] &= \frac{1}{2\hbar}\left[\sqrt{m\omega}x_k + \frac{i}{\sqrt{m\omega}}p_k,\ \sqrt{m\omega}x_l - \frac{i}{\sqrt{m\omega}}p_l\right] \\
&= \frac{1}{2\hbar}\Bigl(m\omega[x_k, x_l] - i[x_k, p_l] + i[p_k, x_l] + \frac{1}{m\omega}[p_k, p_l]\Bigr) \\
&= \frac{1}{2\hbar}\bigl(-i(i\hbar\delta_{kl}) + i(-i\hbar\delta_{kl})\bigr) \\
&= \frac{1}{2\hbar}(\hbar\delta_{kl} + \hbar\delta_{kl}) \\
&= \delta_{kl}
\end{aligned}
$$

同様に $[a_k, a_l]$ と $[a_k^\dagger, a_l^\dagger]$ を計算します。

$$
\begin{aligned}
[a_k, a_l] &= \frac{1}{2\hbar}\Bigl(m\omega[x_k, x_l] + i[x_k, p_l] + i[p_k, x_l] - \frac{1}{m\omega}[p_k, p_l]\Bigr) \\
&= \frac{1}{2\hbar}\bigl(i(i\hbar\delta_{kl}) + i(-i\hbar\delta_{kl})\bigr) \\
&= 0
\end{aligned}
$$

エルミート共役をとると，$[a_k^\dagger, a_l^\dagger] = -[a_k, a_l]^\dagger = 0$ も得られます。

次に $a_k^\dagger a_k$ を展開します。

$$
\begin{aligned}
a_k^\dagger a_k &= \frac{1}{2\hbar}\left(\sqrt{m\omega}x_k - \frac{i}{\sqrt{m\omega}}p_k\right)\left(\sqrt{m\omega}x_k + \frac{i}{\sqrt{m\omega}}p_k\right) \\
&= \frac{1}{2\hbar}\left(m\omega x_k^2 + \frac{p_k^2}{m\omega} + i[x_k, p_k]\right) \\
&= \frac{1}{2\hbar\omega}\left(\frac{p_k^2}{m} + m\omega^2 x_k^2\right) - \frac{1}{2}
\end{aligned}
$$

両辺に $\hbar\omega$ を掛けて整理すると，$\dfrac{1}{2}\left(\dfrac{p_k^2}{m} + m\omega^2 x_k^2\right) = \hbar\omega\left(a_k^\dagger a_k + \dfrac{1}{2}\right)$ です。$k = 1, 2$ について足し合わせると，ハミルトニアン $\mathcal{H}$ は次式になります。

$$
\begin{aligned}
\mathcal{H} &= \hbar\omega\left(a_1^\dagger a_1 + \frac{1}{2}\right) + \hbar\omega\left(a_2^\dagger a_2 + \frac{1}{2}\right) \\
&= \hbar\omega\bigl(a_1^\dagger a_1 + a_2^\dagger a_2 + 1\bigr)
\end{aligned}
$$

したがって，交換関係とハミルトニアンは次のようになります。

$$
\finalanswer{[a_k, a_l^\dagger] = \delta_{kl}, \quad [a_k, a_l] = [a_k^\dagger, a_l^\dagger] = 0, \quad \mathcal{H} = \hbar\omega\bigl(a_1^\dagger a_1 + a_2^\dagger a_2 + 1\bigr)}
$$

### (2)

座標表示では $p_k = -i\hbar\dfrac{\partial}{\partial x_k}$ です。これを消滅演算子 $a_k$ の定義式に代入し，条件 $a_k|0\rangle = 0$ を波動関数 $\psi_0(x_1, x_2)$ に対する微分方程式に書き換えます。

$$
\begin{aligned}
\frac{1}{\sqrt{2\hbar}}\left(\sqrt{m\omega}x_k + \frac{i}{\sqrt{m\omega}}\left(-i\hbar\frac{\partial}{\partial x_k}\right)\right)\psi_0 &= 0 \\
\left(m\omega x_k + \hbar\frac{\partial}{\partial x_k}\right)\psi_0 &= 0 \\
\frac{\partial\psi_0}{\partial x_k} &= -\frac{m\omega}{\hbar}x_k\psi_0
\end{aligned}
$$

$k = 1, 2$ について変数分離で積分します。まず $k = 1$ の式から次式が得られます。

$$
\begin{aligned}
\frac{1}{\psi_0}\frac{\partial\psi_0}{\partial x_1} &= -\frac{m\omega}{\hbar}x_1 \\
\psi_0(x_1, x_2) &= g(x_2)\exp\!\left(-\frac{m\omega}{2\hbar}x_1^2\right)
\end{aligned}
$$

これを $k = 2$ の式に代入すると，$g'(x_2) = -\dfrac{m\omega}{\hbar}x_2 g(x_2)$ となり，$g(x_2) = C\exp\!\left(-\dfrac{m\omega}{2\hbar}x_2^2\right)$（$C$ は $0$ でない任意定数）が得られます。よって $r = \sqrt{x_1^2 + x_2^2}$ を用いて書くと次式になります。

$$
\begin{aligned}
\psi_0(r) &= C\exp\!\left(-\frac{m\omega}{2\hbar}(x_1^2 + x_2^2)\right) \\
&= C\exp\!\left(-\frac{m\omega}{2\hbar}r^2\right)
\end{aligned}
$$

したがって，基底状態の波動関数は任意定数 $C$ を用いて次式となります。

$$
\finalanswer{\psi_0(r) = C\exp\!\left(-\frac{m\omega}{2\hbar}r^2\right)}
$$

### (3)

個数演算子を $N_k = a_k^\dagger a_k$（$k = 1, 2$）とおきます。設問1の交換関係から $[N_k, a_l^\dagger] = \delta_{kl}a_k^\dagger$，$[N_k, a_l] = -\delta_{kl}a_k$ および $[N_1, N_2] = 0$ が成り立ちます。

非負整数 $n_1, n_2 = 0, 1, 2, \dots$ に対して次の規格化された状態を定義します。

$$
|n_1, n_2\rangle = \frac{1}{\sqrt{n_1!\,n_2!}}(a_1^\dagger)^{n_1}(a_2^\dagger)^{n_2}|0\rangle
$$

交換関係 $[N_k, (a_k^\dagger)^{n_k}] = n_k (a_k^\dagger)^{n_k}$ と $N_k|0\rangle = 0$ より，$N_k|n_1, n_2\rangle = n_k|n_1, n_2\rangle$ です。よって，ハミルトニアン $\mathcal{H} = \hbar\omega(N_1 + N_2 + 1)$ を作用させると次式が得られます。

$$
\begin{aligned}
\mathcal{H}|n_1, n_2\rangle &= \hbar\omega(N_1 + N_2 + 1)|n_1, n_2\rangle \\
&= \hbar\omega(n_1 + n_2 + 1)|n_1, n_2\rangle
\end{aligned}
$$

逆に，任意の固有状態に消滅演算子 $a_1, a_2$ を繰り返し作用させると固有値が $\hbar\omega$ ずつ下がりますが，$N_k = a_k^\dagger a_k$ の固有値は $0$ 以上なので，有限回で $a_1|\psi\rangle = a_2|\psi\rangle = 0$ となる基底状態 $|0\rangle$ に達します。設問2より基底状態は定数倍を除いて一意なので，すべての固有状態は $|n_1, n_2\rangle$ の線形結合で尽くされます。

$N = n_1 + n_2$（$N = 0, 1, 2, \dots$）とおくと，エネルギー固有値は $E_N = \hbar\omega(N + 1)$ です。与えられた $N$ に対して $n_1 + n_2 = N$ を満たす非負整数の組 $(n_1, n_2)$ は $(N, 0), (N - 1, 1), \dots, (0, N)$ の $N + 1$ 通りあり，これらに対応する固有状態は互いに直交します。よって固有値 $E_N = \hbar\omega(N + 1)$ の縮退度は $N + 1$ です。

$$
\finalanswer{|n_1, n_2\rangle = \frac{1}{\sqrt{n_1!\,n_2!}}(a_1^\dagger)^{n_1}(a_2^\dagger)^{n_2}|0\rangle, \quad E_N = \hbar\omega(N + 1) \ (N = n_1 + n_2 = 0, 1, 2, \dots), \quad g_N = N + 1}
$$

### (4)

$\hbar = m = \omega = 1$ のとき，座標表示のシュレーディンガー方程式は次の通りです。

$$
\begin{aligned}
\left(-\frac{1}{2}\left(\frac{\partial^2}{\partial x_1^2} + \frac{\partial^2}{\partial x_2^2}\right) + \frac{1}{2}(x_1^2 + x_2^2)\right)\psi &= E\psi \\
\left(\frac{\partial^2}{\partial r^2} + \frac{1}{r}\frac{\partial}{\partial r} + \frac{1}{r^2}\frac{\partial^2}{\partial\theta^2} + 2E - r^2\right)\psi &= 0
\end{aligned}
$$

$\psi(r, \theta) = R(r)\Theta(\theta)$ を代入し，両辺を $R(r)\Theta(\theta)$ で割ってから $r^2$ を掛けます。

$$
\begin{aligned}
\frac{r^2}{R}\left(\frac{\mathrm{d}^2 R}{\mathrm{d}r^2} + \frac{1}{r}\frac{\mathrm{d}R}{\mathrm{d}r} + (2E - r^2)R\right) + \frac{1}{\Theta}\frac{\mathrm{d}^2\Theta}{\mathrm{d}\theta^2} &= 0 \\
\frac{r^2}{R}\left(\frac{\mathrm{d}^2 R}{\mathrm{d}r^2} + \frac{1}{r}\frac{\mathrm{d}R}{\mathrm{d}r} + (2E - r^2)R\right) &= -\frac{1}{\Theta}\frac{\mathrm{d}^2\Theta}{\mathrm{d}\theta^2}
\end{aligned}
$$

左辺は $r$ のみの関数，右辺は $\theta$ のみの関数なので，両辺は定数に等しくなります。その分離定数を $n^2$ とおくと，$\theta$ に関する方程式は

$$
\frac{\mathrm{d}^2\Theta}{\mathrm{d}\theta^2} + n^2\Theta = 0
$$

です。この一般解は $n \neq 0$ で $\Theta(\theta) = A e^{in\theta} + B e^{-in\theta}$，$n = 0$ で $\Theta(\theta) = A + B\theta$ となります。波動関数 $\psi(r, \theta)$ は同じ空間点を表す角度 $\theta$ と $\theta + 2\pi$ で同じ値をとる1価関数でなければならないため，周期条件 $\Theta(\theta + 2\pi) = \Theta(\theta)$ が課されます。この条件から，$n = 0$ では $B = 0$ となり，$n \neq 0$ では $e^{\pm 2\pi i n} = 1$ すなわち $n$ が整数であることが必要です。

また，動径方向の方程式を $r^2$ で割って $R(r)$ を掛けると次式が導かれます。

$$
\frac{\mathrm{d}^2 R}{\mathrm{d}r^2} + \frac{1}{r}\frac{\mathrm{d}R}{\mathrm{d}r} + \left(2E - r^2 - \frac{n^2}{r^2}\right)R = 0
$$

したがって，$n$ は波動関数の1価性 $\Theta(\theta + 2\pi) = \Theta(\theta)$ より任意の整数 $n = 0, \pm 1, \pm 2, \dots$ をとります。

### (5)

$f(r) = \sum_{s=0}^{\infty} f_s r^{s+\alpha}$ を微分します。

$$
\begin{aligned}
\frac{\mathrm{d}f}{\mathrm{d}r} &= \sum_{s=0}^{\infty} (s + \alpha) f_s r^{s + \alpha - 1} \\
\frac{\mathrm{d}^2 f}{\mathrm{d}r^2} &= \sum_{s=0}^{\infty} (s + \alpha)(s + \alpha - 1) f_s r^{s + \alpha - 2}
\end{aligned}
$$

これらを $f(r)$ に対する微分方程式に代入します。

$$
\begin{aligned}
&\sum_{s=0}^{\infty} \bigl((s + \alpha)(s + \alpha - 1) + (s + \alpha) - n^2\bigr) f_s r^{s + \alpha - 2} \\
&\quad + \sum_{s=0}^{\infty} \bigl(2E - 2 - 2(s + \alpha)\bigr) f_s r^{s + \alpha} = 0
\end{aligned}
$$

最初の和の係数は $(s + \alpha)^2 - n^2$ です。左辺で最も低いべきである $r^{\alpha - 2}$ の項は $s = 0$ のみから現れ，その係数は $0$ でなければなりません。

$$
(\alpha^2 - n^2)f_0 = 0
$$

$f_0 = 1 \neq 0$ なので，$\alpha^2 = n^2$ すなわち $\alpha = |n|$ または $\alpha = -|n|$ です。

ここで $r \to 0$ のとき $f(r) \sim r^\alpha$ です。$\alpha = -|n|$ で $n \neq 0$ のときは $r \to 0$ で $f(r)$ が発散します。また $n = 0$ のときは $\alpha = |n| = -|n| = 0$ です。したがって，$f(r)$ が原点 $r = 0$ で発散しない条件から，$\alpha$ は次式となります。

$$
\finalanswer{\alpha = |n|}
$$

### (6)

設問5で得た級数方程式に $\alpha = |n|$ を代入し，$r^{s + |n| - 2}$ のべきごとに係数をまとめます。

まず $s = 1$ の項である $r^{|n| - 1}$ の係数は次式になります。

$$
\bigl((|n| + 1)^2 - n^2\bigr)f_1 = (2|n| + 1)f_1 = 0
$$

$|n| \ge 0$ より $2|n| + 1 \neq 0$ なので，$f_1 = 0$ です。

次に $s \ge 2$ に対して，第2の和の添字を $s \to s - 2$ とずらして $r^{s + |n| - 2}$ の係数を $0$ とおきます。

$$
\begin{aligned}
\bigl((s + |n|)^2 - n^2\bigr)f_s + \bigl(2E - 2 - 2(s - 2 + |n|)\bigr)f_{s-2} &= 0 \\
s(s + 2|n|)f_s &= 2\bigl(s + |n| - 1 - E\bigr)f_{s-2}
\end{aligned}
$$

$f_1 = 0$ とこの漸化式より，すべての奇数 $s = 1, 3, 5, \dots$ に対して $f_s = 0$ となります。一方，偶数 $s = 2k$（$k = 0, 1, 2, \dots$）については $f_0 = 1$ から順に決まります。

べき級数が有限個の項からなるとき，ある非負整数 $k$ に対して $f_{2k} \neq 0$ かつ $f_{2k+2} = 0$ となります。漸化式に $s = 2k + 2$ を代入すると，$f_{2k+2} = 0$ かつ $f_{2k} \neq 0$ であるための条件は右辺の係数が $0$ になることです。

$$
\begin{aligned}
(2k + 2) + |n| - 1 - E &= 0 \\
E &= 2k + |n| + 1
\end{aligned}
$$

ここで $k = 0, 1, 2, \dots$，$n = 0, \pm 1, \pm 2, \dots$ なので，$N = 2k + |n|$ とおくと，$N$ はすべての非負整数 $0, 1, 2, \dots$ をとります。したがって，固有値は $E = N + 1$ となり，設問3で求めた固有値 $E_N = \hbar\omega(N + 1)$ において $\hbar = m = \omega = 1$ とおいたものと一致します。

$$
\finalanswer{E = 2k + |n| + 1 \quad (k = 0, 1, 2, \dots,\ n = 0, \pm 1, \pm 2, \dots)}
$$
