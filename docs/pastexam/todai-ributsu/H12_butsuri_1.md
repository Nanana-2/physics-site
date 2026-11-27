---
title: 東大理物 平成12年度 物理学 第1問：1次元二重井戸ポテンシャルとトンネル分裂
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成12年度 物理学 第1問：1次元二重井戸ポテンシャルとトンネル分裂

## 問題

図1の様な1次元ポテンシャル $V(x)$ すなわち

$$
\begin{aligned}
V(x) &= \infty && (|x| > d + a\text{ のとき}), \\
V(x) &= 0 && (d + a > |x| > d\text{ のとき}), \\
V(x) &= V_0 && (|x| < d\text{ のとき}),
\end{aligned}
$$

の中に質量 $m$ の粒子が一個入っている系を考える。このように，1次元シュレーディンガー方程式でポテンシャルエネルギーが1次元座標 $x$ の関数として $V(x) = V(-x)$ を満たすとき，ハミルトニアン

$$
H(x) = -\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d}x^2} + V(x)
$$

の固有関数 $\Psi$ は，$\Psi(x) = \Psi(-x)$ であるパリティが偶のものと $\Psi(x) = -\Psi(-x)$ であるパリティが奇のものに分かれることに注意して，以下の問いに答えよ。但し $\hbar$ はプランク定数である。

<figure class="problem-figure" markdown>
![1次元対称二重井戸ポテンシャル](../../assets/figures/pastexam-todai-ributsu/H12_butsuri_1-p-light.svg#only-light){ loading=lazy }
![1次元対称二重井戸ポテンシャル](../../assets/figures/pastexam-todai-ributsu/H12_butsuri_1-p-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">図1：幅 $a$ の2つの井戸を幅 $2d$，高さ $V_0$ の障壁で隔てた1次元ポテンシャル。</figcaption>
</figure>

(1) この系のエネルギー固有値 $E$ を決める式を $E < V_0$ の条件が満たされている場合について求めよ。

(2) 基底状態と第一励起状態の波動関数をそれぞれ $|\Psi_0\rangle$ と $|\Psi_1\rangle$ とし，エネルギー固有値をそれぞれ $E = E_0, E_1$ とする。$E_1 < V_0$ が満たされる場合に，$|\Psi_0\rangle$ と $|\Psi_1\rangle$ の概形を $x$ の関数として描け。

(3) $V_0$ が有限で $d$ が無限大の極限をとった時の $E_0, E_1$ を $\overline{E}_0, \overline{E}_1$ とする。$\overline{E}_0, \overline{E}_1$ を一意的に決める式を求めよ。

(4) $d$ が大きいが有限であるとする。$\overline{E}_0$ を用いて，$\Delta \equiv E_1 - E_0$ の $d$ 依存性がどうなっているかを議論せよ。

$V_0$ と $d$ が大きいとき，規格化された波動関数 $|\Psi_0\rangle$ や $|\Psi_1\rangle$ のほとんどの重みは $d + a > |x| > d$ の中にあると考えてよい。したがって，$|\Psi_0\rangle$ や $|\Psi_1\rangle$ は近似的に右の井戸に粒子が存在し，わずかに $|x| < d$ へ浸み出している状態 $|R\rangle$ と，左の井戸に粒子が存在し，わずかに $|x| < d$ へ浸み出している状態 $|L\rangle$ の1次結合であらわされるとみなせる。$|R\rangle$ と $|L\rangle$ は規格化され，互いに直交しているとし，また，$|\Psi_0\rangle$ や $|\Psi_1\rangle$ よりも高い励起状態については無視して良いとして，以下に答えよ。
{: .problem-lead }

(5) $|\Psi_0\rangle$ と $|\Psi_1\rangle$ を $|R\rangle$ と $|L\rangle$ の1次結合であらわせ。

(6) $|R\rangle$ と $|L\rangle$ を基底とする表現をとって，ハミルトニアンを2行2列の行列で表せ。

(7) $t = 0$ に粒子の波動関数が右の井戸に存在する状態 $|R\rangle$ で表わされていたとき，トンネリングによって時刻 $t$ に粒子が左の井戸の状態 $|L\rangle$ に移っている確率を $\Delta$ を用いて表わし，得られた $\Delta$ 依存性の物理的意味を議論せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ポテンシャルが左右対称 $V(-x) = V(x)$ であるため，固有関数を偶関数 $\cosh(\kappa x)$ と奇関数 $\sinh(\kappa x)$ に分けて $x = d$ で接続すると，エネルギー固有値を定める超越方程式がそれぞれ $\tanh(\kappa d)$ と $\coth(\kappa d)$ を含む形で得られます。

障壁の半幅 $d$ が大きい極限では $\tanh(\kappa d)$ と $\coth(\kappa d)$ がともに $1$ に近づいて偶奇の準位が縮退し，有限 $d$ での差 $e^{-2\kappa d}$ を1次展開することでエネルギー分裂 $\Delta = E_1 - E_0$ の指数的な $d$ 依存性を求めます。後半では偶奇の2準位を左右の局在状態 $|R\rangle, |L\rangle$ の基底で書き直し，シュレーディンガー方程式の時間発展からトンネル遷移の確率を計算します。
</div>

### (1)

$0 < E < V_0$ の範囲で，正の波数 $k$ と減衰定数 $\kappa$ を次で定めます。

$$
k = \frac{\sqrt{2mE}}{\hbar}, \qquad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}
$$

各領域のシュレーディンガー方程式は次の通りです。

$$
\begin{aligned}
\frac{\mathrm{d}^2\Psi}{\mathrm{d}x^2} + k^2\Psi &= 0 \qquad (d < |x| < d + a) \\
\frac{\mathrm{d}^2\Psi}{\mathrm{d}x^2} - \kappa^2\Psi &= 0 \qquad (|x| < d)
\end{aligned}
$$

$|x| \ge d + a$ で $V(x) = \infty$ なので境界条件は $\Psi(\pm(d + a)) = 0$ です。$d < x < d + a$ における解は任意定数 $A$ を用いて次になります。

$$
\Psi(x) = A\sin\bigl[k(d + a - x)\bigr] \qquad (d < x < d + a)
$$

$x = d$ における対数微分 $\dfrac{\Psi'(d)}{\Psi(d)}$ を右側から求めます。

$$
\begin{aligned}
\frac{\Psi'(d + 0)}{\Psi(d + 0)} &= \frac{-kA\cos(ka)}{A\sin(ka)} \\
&= -k\cot(ka)
\end{aligned}
$$

次に中央の障壁 $|x| < d$ での解を偶奇それぞれについて求め，$x = d$ での連続条件 $\dfrac{\Psi'(d - 0)}{\Psi(d - 0)} = \dfrac{\Psi'(d + 0)}{\Psi(d + 0)}$ を課します。

偶パリティ $\Psi(-x) = \Psi(x)$ の場合，$|x| < d$ では $\Psi(x) = B\cosh(\kappa x)$ です。左側からの対数微分を等しくおきます。

$$
\begin{aligned}
\frac{\kappa B\sinh(\kappa d)}{B\cosh(\kappa d)} &= -k\cot(ka) \\
\kappa\tanh(\kappa d) &= -k\cot(ka)
\end{aligned}
$$

奇パリティ $\Psi(-x) = -\Psi(x)$ の場合，$|x| < d$ では $\Psi(x) = B\sinh(\kappa x)$ です。左側からの対数微分を等しくおきます。

$$
\begin{aligned}
\frac{\kappa B\cosh(\kappa d)}{B\sinh(\kappa d)} &= -k\cot(ka) \\
\kappa\coth(\kappa d) &= -k\cot(ka)
\end{aligned}
$$

以上より，$E < V_0$ のエネルギー固有値 $E$ を決める式は偶パリティと奇パリティについてそれぞれ次の通りです。ただし $k = \dfrac{\sqrt{2mE}}{\hbar}$，$\kappa = \dfrac{\sqrt{2m(V_0 - E)}}{\hbar}$ です。

$$
\finalanswer{\kappa\tanh(\kappa d) = -k\cot(ka), \qquad \kappa\coth(\kappa d) = -k\cot(ka)}
$$

### (2)

1次元束縛状態の固有関数は，エネルギーが低い順に節の数が $0, 1, 2, \dots$ と増えます。基底状態 $|\Psi_0\rangle$ は節をもたない偶関数，第1励起状態 $|\Psi_1\rangle$ は原点 $x = 0$ に節を1つもつ奇関数です。

いずれも $|x| = d + a$ で $0$ になり，井戸領域 $d < |x| < d + a$ では正弦関数として上に凸または下に凸の山をつくり，障壁領域 $|x| < d$ では指数的に減衰しながら $x = \pm d$ で傾きを含めて滑らかにつながります。$|\Psi_0\rangle$ は $x = 0$ で正の極小値をとり，$|\Psi_1\rangle$ は $x = 0$ で $0$ を横切って左右で符号が反転します。概形を下に示します。

<figure class="problem-figure" markdown>
![基底状態と第1励起状態の波動関数の概形](../../assets/figures/pastexam-todai-ributsu/H12_butsuri_1-s-light.svg#only-light){ loading=lazy }
![基底状態と第1励起状態の波動関数の概形](../../assets/figures/pastexam-todai-ributsu/H12_butsuri_1-s-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">基底状態 $\Psi_0(x)$（偶パリティ）と第1励起状態 $\Psi_1(x)$（奇パリティ）の概形。</figcaption>
</figure>

### (3)

$E_0, E_1 < V_0$ より $\kappa > 0$ なので，$d \to \infty$ の極限では $\tanh(\kappa d) \to 1$ および $\coth(\kappa d) \to 1$ となります。したがって，(1) の偶パリティと奇パリティの方程式はいずれも同じ式になり，$\overline{E}_0 = \overline{E}_1$ と縮退します。

$\overline{k} = \dfrac{\sqrt{2m\overline{E}_0}}{\hbar}$，$\overline{\kappa} = \dfrac{\sqrt{2m(V_0 - \overline{E}_0)}}{\hbar}$ とおくと，方程式は次になります。

$$
\overline{\kappa} = -\overline{k}\cot(\overline{k}a)
$$

ここで基底状態は井戸内部に節をもたないため，$0 < \overline{k}a < \pi$ です。右辺が正になるには $\cot(\overline{k}a) < 0$ が必要なので，$\dfrac{\pi}{2} < \overline{k}a < \pi$ の範囲に限られます。この区間では $-\overline{k}\cot(\overline{k}a)$ は $0$ から $+\infty$ へ単調増加し，$\overline{\kappa} = \sqrt{\dfrac{2mV_0}{\hbar^2} - \overline{k}^2}$ は単調減少するため，解はただ1つに決まります。

$$
\finalanswer{\overline{E}_0 = \overline{E}_1,\qquad \sqrt{V_0 - \overline{E}_0} = -\sqrt{\overline{E}_0}\,\cot\left(\frac{a\sqrt{2m\overline{E}_0}}{\hbar}\right) \qquad \left(\frac{\pi}{2} < \frac{a\sqrt{2m\overline{E}_0}}{\hbar} < \pi\right)}
$$

### (4)

関数 $f(E) = k\cot(ka) + \kappa$ を定めます。(3) より $f(\overline{E}_0) = 0$ です。$d$ が十分大きく $\overline{\kappa}d \gg 1$ のとき，$\tanh(\kappa d)$ と $\coth(\kappa d)$ を $e^{-2\kappa d}$ の1次まで展開します。

$$
\begin{aligned}
\tanh(\kappa d) &= \frac{1 - e^{-2\kappa d}}{1 + e^{-2\kappa d}} \\
&\approx 1 - 2e^{-2\kappa d}
\end{aligned}
$$

$$
\begin{aligned}
\coth(\kappa d) &= \frac{1 + e^{-2\kappa d}}{1 - e^{-2\kappa d}} \\
&\approx 1 + 2e^{-2\kappa d}
\end{aligned}
$$

これらを (1) の偶状態および奇状態の方程式に代入します。

$$
\begin{aligned}
k_0\cot(k_0 a) + \kappa_0\left(1 - 2e^{-2\kappa_0 d}\right) &\approx 0 \\
k_1\cot(k_1 a) + \kappa_1\left(1 + 2e^{-2\kappa_1 d}\right) &\approx 0
\end{aligned}
$$

$f(E)$ を用いて書き直し，右辺の小さな項では $\kappa_0, \kappa_1$ を $\overline{\kappa}$ で置き換えます。

$$
\begin{aligned}
f(E_0) &\approx 2\overline{\kappa}e^{-2\overline{\kappa}d} \\
f(E_1) &\approx -2\overline{\kappa}e^{-2\overline{\kappa}d}
\end{aligned}
$$

一方，$E_0$ と $E_1$ は $\overline{E}_0$ に近いため，$f(E)$ を $\overline{E}_0$ の周りに1次展開すると $f(E_1) - f(E_0) \approx f'(\overline{E}_0)(E_1 - E_0)$ です。導関数 $f'(E)$ を $\dfrac{\mathrm{d}k}{\mathrm{d}E} = \dfrac{m}{\hbar^2 k}$ および $\dfrac{\mathrm{d}\kappa}{\mathrm{d}E} = -\dfrac{m}{\hbar^2\kappa}$ を用いて計算します。

$$
\begin{aligned}
f'(E) &= \frac{\mathrm{d}k}{\mathrm{d}E}\left(\cot(ka) - \frac{ka}{\sin^2(ka)}\right) + \frac{\mathrm{d}\kappa}{\mathrm{d}E} \\
&= \frac{m}{\hbar^2 k}\left(\cot(ka) - ka\bigl(1 + \cot^2(ka)\bigr)\right) - \frac{m}{\hbar^2\kappa}
\end{aligned}
$$

$E = \overline{E}_0$ では $\cot(\overline{k}a) = -\dfrac{\overline{\kappa}}{\overline{k}}$ なので，$1 + \cot^2(\overline{k}a) = \dfrac{\overline{k}^2 + \overline{\kappa}^2}{\overline{k}^2}$ です。これを代入して整理します。

$$
\begin{aligned}
f'(\overline{E}_0) &= \frac{m}{\hbar^2\overline{k}}\left(-\frac{\overline{\kappa}}{\overline{k}} - \frac{a(\overline{k}^2 + \overline{\kappa}^2)}{\overline{k}}\right) - \frac{m}{\hbar^2\overline{\kappa}} \\
&= -\frac{m}{\hbar^2}\left(\frac{\overline{\kappa}}{\overline{k}^2} + \frac{1}{\overline{\kappa}}\right) - \frac{ma(\overline{k}^2 + \overline{\kappa}^2)}{\hbar^2\overline{k}^2} \\
&= -\frac{m(\overline{k}^2 + \overline{\kappa}^2)}{\hbar^2\overline{k}^2\overline{\kappa}}(1 + \overline{\kappa}a)
\end{aligned}
$$

$f'(\overline{E}_0)(E_1 - E_0) \approx -4\overline{\kappa}e^{-2\overline{\kappa}d}$ より，$\Delta = E_1 - E_0$ を求めます。

$$
\begin{aligned}
\Delta &= -\frac{4\overline{\kappa}}{f'(\overline{E}_0)}e^{-2\overline{\kappa}d} \\
&= \frac{4\hbar^2\overline{k}^2\overline{\kappa}^2}{m(\overline{k}^2 + \overline{\kappa}^2)(1 + \overline{\kappa}a)}e^{-2\overline{\kappa}d} \\
&= \frac{8\overline{E}_0(V_0 - \overline{E}_0)}{V_0\left(1 + \dfrac{a\sqrt{2m(V_0 - \overline{E}_0)}}{\hbar}\right)}\exp\left(-\frac{2d\sqrt{2m(V_0 - \overline{E}_0)}}{\hbar}\right)
\end{aligned}
$$

したがって，$\Delta = E_1 - E_0$ は障壁幅 $2d$ とともに指数関数 $\exp\left(-\dfrac{2d\sqrt{2m(V_0 - \overline{E}_0)}}{\hbar}\right)$ に比例して急速に $0$ へ減少します。

$$
\finalanswer{\Delta \approx \frac{8\overline{E}_0(V_0 - \overline{E}_0)}{V_0\left(1 + \dfrac{a\sqrt{2m(V_0 - \overline{E}_0)}}{\hbar}\right)}\exp\left(-\frac{2d\sqrt{2m(V_0 - \overline{E}_0)}}{\hbar}\right)}
$$

### (5)

左右反転演算子 $P$ に対して，$|R\rangle$ と $|L\rangle$ の位相を $P|R\rangle = |L\rangle$ かつ $P|L\rangle = |R\rangle$ となるように選びます。$|R\rangle$ と $|L\rangle$ は正規直交なので，$|\Psi_0\rangle$ が偶パリティ（$P|\Psi_0\rangle = +|\Psi_0\rangle$），$|\Psi_1\rangle$ が奇パリティ（$P|\Psi_1\rangle = -|\Psi_1\rangle$）を満たす規格化された1次結合は次の通りです。

$$
\finalanswer{|\Psi_0\rangle = \frac{1}{\sqrt{2}}\bigl(|R\rangle + |L\rangle\bigr), \qquad |\Psi_1\rangle = \frac{1}{\sqrt{2}}\bigl(|R\rangle - |L\rangle\bigr)}
$$

### (6)

$|\Psi_0\rangle$ と $|\Psi_1\rangle$ が張る2次元部分空間でのハミルトニアンは $H = E_0|\Psi_0\rangle\langle\Psi_0| + E_1|\Psi_1\rangle\langle\Psi_1|$ です。(5) の関係から，$|R\rangle$ と $|L\rangle$ を $|\Psi_0\rangle$ と $|\Psi_1\rangle$ で表します。

$$
|R\rangle = \frac{1}{\sqrt{2}}\bigl(|\Psi_0\rangle + |\Psi_1\rangle\bigr), \qquad |L\rangle = \frac{1}{\sqrt{2}}\bigl(|\Psi_0\rangle - |\Psi_1\rangle\bigr)
$$

これを用いて各行列要素を計算します。

$$
\begin{aligned}
\langle R|H|R\rangle &= \frac{1}{2}\bigl(\langle\Psi_0| + \langle\Psi_1|\bigr)H\bigl(|\Psi_0\rangle + |\Psi_1\rangle\bigr) \\
&= \frac{E_0 + E_1}{2}
\end{aligned}
$$

$$
\begin{aligned}
\langle L|H|L\rangle &= \frac{1}{2}\bigl(\langle\Psi_0| - \langle\Psi_1|\bigr)H\bigl(|\Psi_0\rangle - |\Psi_1\rangle\bigr) \\
&= \frac{E_0 + E_1}{2}
\end{aligned}
$$

$$
\begin{aligned}
\langle R|H|L\rangle &= \frac{1}{2}\bigl(\langle\Psi_0| + \langle\Psi_1|\bigr)H\bigl(|\Psi_0\rangle - |\Psi_1\rangle\bigr) \\
&= \frac{E_0 - E_1}{2} \\
&= -\frac{\Delta}{2}
\end{aligned}
$$

同様に $\langle L|H|R\rangle = -\dfrac{\Delta}{2}$ です。$\overline{E} = \dfrac{E_0 + E_1}{2}$ とおくと，$|R\rangle, |L\rangle$ を基底とするハミルトニアンの行列表現は次の通りです。なお，(4) の近似の範囲では $\overline{E} \approx \overline{E}_0$ です。

$$
\finalanswer{H = \begin{pmatrix} \dfrac{E_0 + E_1}{2} & -\dfrac{\Delta}{2} \\[1.2ex] -\dfrac{\Delta}{2} & \dfrac{E_0 + E_1}{2} \end{pmatrix}}
$$

### (7)

時刻 $t = 0$ の状態は $|\psi(0)\rangle = |R\rangle$ であり，これを固有状態で展開すると $|\psi(0)\rangle = \dfrac{1}{\sqrt{2}}\bigl(|\Psi_0\rangle + |\Psi_1\rangle\bigr)$ です。これに時間発展演算子 $e^{-iHt/\hbar}$ を作用させます。

$$
|\psi(t)\rangle = \frac{1}{\sqrt{2}}\left(e^{-iE_0 t/\hbar}|\Psi_0\rangle + e^{-iE_1 t/\hbar}|\Psi_1\rangle\right)
$$

時刻 $t$ に左の井戸の状態 $|L\rangle$ に見出される確率振幅 $\langle L|\psi(t)\rangle$ を計算します。$\langle L|\Psi_0\rangle = \dfrac{1}{\sqrt{2}}$，$\langle L|\Psi_1\rangle = -\dfrac{1}{\sqrt{2}}$ です。

$$
\begin{aligned}
\langle L|\psi(t)\rangle &= \frac{1}{2}\left(e^{-iE_0 t/\hbar} - e^{-iE_1 t/\hbar}\right) \\
&= \frac{1}{2}e^{-i(E_0 + E_1)t/(2\hbar)}\left(e^{i\Delta t/(2\hbar)} - e^{-i\Delta t/(2\hbar)}\right) \\
&= i e^{-i(E_0 + E_1)t/(2\hbar)}\sin\left(\frac{\Delta t}{2\hbar}\right)
\end{aligned}
$$

求める確率 $P_{R \to L}(t) = \bigl|\langle L|\psi(t)\rangle\bigr|^2$ は次の通りです。

$$
\finalanswer{P_{R \to L}(t) = \sin^2\left(\frac{\Delta t}{2\hbar}\right)}
$$

この式から，粒子は周期 $T = \dfrac{2\pi\hbar}{\Delta}$ で左右の井戸の間を往復し，右の井戸から左の井戸へ完全に移るまでの時間は $\tau = \dfrac{\pi\hbar}{\Delta}$ となります。(4) の結果から $\Delta \propto e^{-2\overline{\kappa}d}$ なので，トンネル遷移時間 $\tau$ は障壁幅 $2d$ に対して $\tau \propto \exp\left(\dfrac{2d\sqrt{2m(V_0 - \overline{E}_0)}}{\hbar}\right)$ と指数関数的に長くなります。障壁が厚くなるほど $|R\rangle$ と $|L\rangle$ の重なりが小さくなってエネルギー分裂 $\Delta$ が $0$ に近づき，極限 $d \to \infty$ では $\Delta \to 0$ となって粒子は右の井戸にとどまり続けます。

<aside class="rigor-note" markdown>
(3) で $\overline{E}_0 < V_0$ の束縛状態が少なくとも1つ存在するためには，$k = \dfrac{\sqrt{2mV_0}}{\hbar}$ のときに $ka > \dfrac{\pi}{2}$，すなわち $V_0 > \dfrac{\pi^2\hbar^2}{8ma^2}$ が必要です。また (4) の導出で $\overline{\kappa}a \gg 1$ かつ $\overline{E}_0 \ll V_0$ の深い井戸の極限をとると，係数部分は $\dfrac{8\overline{E}_0}{\overline{\kappa}a}$ となります。
</aside>
