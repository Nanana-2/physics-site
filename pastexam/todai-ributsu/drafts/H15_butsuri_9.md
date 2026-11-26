---
title: 東大理物 平成15年度 物理学 第9問：2原子分子の回転比熱と核スピンの影響
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成15年度
exam_subject: 物理学
exam_number: 第9問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成15年度 物理学 第9問：2原子分子の回転比熱と核スピンの影響

## 問題

慣性モーメント $I$ をもった異核2原子分子の回転運動について，次の問に答えよ。ただし，ボルツマン定数を $k_{\mathrm{B}}$ とし，比熱は1分子あたりの比熱とする。
{: .problem-lead }

(1) 古典統計力学を使って，この系の温度 $T$ での回転運動の比熱を求めよ。

(2) この系の回転運動を表すハミルトニアンは

$$
H = \frac{\mathbf{L}^2}{2I} = \frac{\hbar^2}{2I}\cdot\frac{-1}{\sin^2\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\sin\theta\frac{\partial}{\partial\theta} + \frac{\partial^2}{\partial\phi^2}\right)
$$

である。回転量子数 $l$（$l = 0, 1, 2, \dots$）を使って，このハミルトニアンの固有値 $E_l$ とその縮重度 $g_l$ を表せ（導出過程は不要）。

(3) この系の分配関数 $Z$ とエネルギー期待値 $\langle E \rangle$ を，$E_l, g_l$，温度 $T$ を使って表せ。

(4) 低温極限で有効な近似を用いて $Z$ の表式を求め，その近似の範囲で，系の比熱 $C(T)$ を $E_l, g_l, T$ を使って表せ。またその近似が成り立つ条件について述べよ。

次に慣性モーメント $I$ の等核2原子分子の回転運動について考える。2つの原子の原子核はともにスピン $1/2$ のフェルミ粒子であるとして，次の問に答えよ。ただし電子系の合成スピンはゼロであるとする。

(5) 核の合成スピンはどのような値を取り得るかを考え，それぞれの場合について回転運動のエネルギー固有値と縮重度を求めよ。

(6) 設問 (5) で求めたエネルギー固有値の具体的な表式を使って，低温極限での回転運動の比熱を求めよ。

(7) 十分高温で熱平衡に達した分子気体を急冷した直後に測定した低温比熱 $C_1$ と，熱平衡を保ちながらきわめてゆっくり冷却した後測定した低温比熱 $C_2$ では，違いがあったという。その理由として考えられることを簡単に述べよ。ただしいずれの場合も，分子気体は冷却後も気体のままであったとする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成15年度 物理学 第9問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，異核2原子分子の回転を剛体回転子として扱い，古典統計力学の等分配則および量子統計力学の分配関数から低温極限の比熱を求めます。

後半では，スピン $1/2$ の同種フェルミ粒子である2つの原子核の交換に対する波動関数の反対称性から，核の合成スピン状態と許される回転量子数 $l$ の偶奇が結び付くことを導きます。これにより，完全熱平衡での低温比熱と，高温のスピン存在比が凍結された急冷後の低温比熱の違いを説明します。
</div>

### (1)

2原子分子の回転運動は極角 $\theta$ と方位角 $\phi$ の2つの自由度をもち，古典ハミルトニアンは一般化運動量 $p_\theta, p_\phi$ を用いて次式になります。

$$
H_{\mathrm{cl}} = \frac{1}{2I}\left(p_\theta^2 + \frac{p_\phi^2}{\sin^2\theta}\right)
$$

古典分配関数 $Z_{\mathrm{cl}}$ を計算します。

$$
\begin{aligned}
Z_{\mathrm{cl}} &= \frac{1}{h^2}\int_{0}^{\pi} \mathrm{d}\theta \int_{0}^{2\pi} \mathrm{d}\phi \int_{-\infty}^{\infty} \mathrm{d}p_\theta \int_{-\infty}^{\infty} \mathrm{d}p_\phi \,\exp\!\left\{-\frac{1}{2Ik_{\mathrm{B}}T}\left(p_\theta^2 + \frac{p_\phi^2}{\sin^2\theta}\right)\right\} \\
&= \frac{1}{h^2}\int_{0}^{\pi} \mathrm{d}\theta \int_{0}^{2\pi} \mathrm{d}\phi \,\sqrt{2\pi I k_{\mathrm{B}}T}\cdot\sqrt{2\pi I k_{\mathrm{B}}T}\sin\theta \\
&= \frac{4\pi\cdot 2\pi I k_{\mathrm{B}}T}{h^2} \\
&= \frac{2I k_{\mathrm{B}}T}{\hbar^2}
\end{aligned}
$$

これより1分子あたりのエネルギー期待値 $\langle E \rangle$ と比熱 $C$ を求めます。

$$
\begin{aligned}
\langle E \rangle &= k_{\mathrm{B}}T^2\frac{\partial \log Z_{\mathrm{cl}}}{\partial T} \\
&= k_{\mathrm{B}}T
\end{aligned}
$$

$$
\begin{aligned}
C &= \frac{\partial \langle E \rangle}{\partial T} \\
&= k_{\mathrm{B}}
\end{aligned}
$$

したがって，古典統計力学による回転比熱は次式となります。

$$
\finalanswer{C = k_{\mathrm{B}}}
$$

### (2)

角運動量演算子の2乗 $\mathbf{L}^2$ の固有値は $\hbar^2 l(l + 1)$，縮重度は磁気量子数 $m = -l, -l + 1, \dots, l$ の個数 $2l + 1$ です。したがって，ハミルトニアン $H = \dfrac{\mathbf{L}^2}{2I}$ の固有値 $E_l$ と縮重度 $g_l$ は次式となります。

$$
\finalanswer{E_l = \frac{\hbar^2}{2I}l(l + 1), \qquad g_l = 2l + 1 \qquad (l = 0, 1, 2, \dots)}
$$

### (3)

正準分布より，分配関数 $Z$ とエネルギー期待値 $\langle E \rangle$ は次式となります。

$$
\finalanswer{Z = \sum_{l=0}^{\infty} g_l e^{-E_l/(k_{\mathrm{B}}T)}, \qquad \langle E \rangle = \frac{1}{Z}\sum_{l=0}^{\infty} g_l E_l e^{-E_l/(k_{\mathrm{B}}T)}}
$$

### (4)

$E_0 = 0 < E_1 < E_2 < \dots$ なので，低温極限では励起状態へのボルツマン因子が急激に小さくなります。したがって，$Z$ の和を基底状態 $l = 0$ と第1励起状態 $l = 1$ の2項までで打ち切る近似が有効になります。

$$
\begin{aligned}
Z &\simeq g_0 e^{-E_0/(k_{\mathrm{B}}T)} + g_1 e^{-E_1/(k_{\mathrm{B}}T)} \\
&= g_0 e^{-E_0/(k_{\mathrm{B}}T)}\left(1 + \frac{g_1}{g_0}e^{-(E_1 - E_0)/(k_{\mathrm{B}}T)}\right)
\end{aligned}
$$

ここで $E_0 = 0$，$g_0 = 1$ を用いると $Z \simeq 1 + g_1 e^{-E_1/(k_{\mathrm{B}}T)}$ です。対数 $\log Z$ を $e^{-(E_1 - E_0)/(k_{\mathrm{B}}T)} \ll 1$ として1次まで展開します。

$$
\log Z \simeq \log g_0 - \frac{E_0}{k_{\mathrm{B}}T} + \frac{g_1}{g_0}e^{-(E_1 - E_0)/(k_{\mathrm{B}}T)}
$$

これよりエネルギー期待値 $\langle E \rangle = k_{\mathrm{B}}T^2\dfrac{\partial \log Z}{\partial T}$ と比熱 $C(T) = \dfrac{\partial \langle E \rangle}{\partial T}$ を計算します。

$$
\begin{aligned}
\langle E \rangle &\simeq E_0 + \frac{g_1}{g_0}(E_1 - E_0)e^{-(E_1 - E_0)/(k_{\mathrm{B}}T)}
\end{aligned}
$$

$$
\begin{aligned}
C(T) &= \frac{\partial \langle E \rangle}{\partial T} \\
&\simeq \frac{g_1}{g_0}k_{\mathrm{B}}\left(\frac{E_1 - E_0}{k_{\mathrm{B}}T}\right)^2 e^{-(E_1 - E_0)/(k_{\mathrm{B}}T)}
\end{aligned}
$$

$E_0 = 0$，$g_0 = 1$ を代入すると，$C(T) \simeq g_1 k_{\mathrm{B}}\left(\dfrac{E_1}{k_{\mathrm{B}}T}\right)^2 e^{-E_1/(k_{\mathrm{B}}T)}$ となります。

$$
\finalanswer{Z \simeq g_0 e^{-E_0/(k_{\mathrm{B}}T)} + g_1 e^{-E_1/(k_{\mathrm{B}}T)}, \qquad C(T) \simeq \frac{g_1}{g_0}k_{\mathrm{B}}\left(\frac{E_1 - E_0}{k_{\mathrm{B}}T}\right)^2 e^{-(E_1 - E_0)/(k_{\mathrm{B}}T)}}
$$

この近似が成り立つ条件は，第1励起準位とのエネルギー差 $E_1 - E_0 = \dfrac{\hbar^2}{I}$ に比べて熱エネルギーが十分小さいことです。

$$
k_{\mathrm{B}}T \ll E_1 - E_0 = \frac{\hbar^2}{I}
$$

このとき $e^{-E_1/(k_{\mathrm{B}}T)} \ll 1$ であり，$l \ge 2$ の寄与 $e^{-E_2/(k_{\mathrm{B}}T)} = e^{-3E_1/(k_{\mathrm{B}}T)}$ は $l = 1$ の寄与に比べて十分小さくなります。

### (5)

スピン $1/2$ の2つの原子核を合成すると，核の合成スピン $S$ は $S = 0$ のスピン1重項と $S = 1$ のスピン3重項の2つの値をとります。核スピン縮重度は $S = 0$ で $1$，$S = 1$ で $3$ です。

2つの原子核は同種のフェルミ粒子なので，核の入れ替えに対して分子全体の波動関数は反対称でなければなりません。合成スピン $0$ の電子系および振動の基底状態は核の入れ替えに対して対称なので，回転の波動関数と核スピン波動関数の積が反対称になる必要があります。核の入れ替えは空間反転 $\theta \to \pi - \theta$，$\phi \to \phi + \pi$ に対応し，回転状態は $(-1)^l$ の符号変化を受けます。

$S = 0$ のとき，核スピン状態は反対称なので回転波動関数は対称である必要があり，$l$ は偶数 $l = 0, 2, 4, \dots$ のみ許されます。各 $l$ の縮重度は核スピン縮重度 $1$ と回転縮重度 $2l + 1$ の積です。

$$
E_l = \frac{\hbar^2}{2I}l(l + 1), \qquad g_l^{(S=0)} = 2l + 1
$$

$S = 1$ のとき，核スピン状態は対称なので回転波動関数は反対称である必要があり，$l$ は奇数 $l = 1, 3, 5, \dots$ のみ許されます。各 $l$ の縮重度は核スピン縮重度 $3$ と回転縮重度 $2l + 1$ の積です。

$$
E_l = \frac{\hbar^2}{2I}l(l + 1), \qquad g_l^{(S=1)} = 3(2l + 1)
$$

### (6)

完全な熱平衡状態における等核2原子分子の分配関数 $Z_{\mathrm{eq}}$ は，設問 (5) で求めた $S = 0$ と $S = 1$ のすべての状態についての和です。

$$
Z_{\mathrm{eq}} = \sum_{l = 0, 2, 4, \dots} (2l + 1)e^{-\frac{\hbar^2 l(l+1)}{2Ik_{\mathrm{B}}T}} + \sum_{l = 1, 3, 5, \dots} 3(2l + 1)e^{-\frac{\hbar^2 l(l+1)}{2Ik_{\mathrm{B}}T}}
$$

エネルギーの低い順に並べると，基底状態は $S = 0$ の $l = 0$ 状態であり $E_0 = 0$，縮重度は $1$ です。第1励起状態は $S = 1$ の $l = 1$ 状態であり $E_1 = \dfrac{\hbar^2}{I}$，縮重度は $3 \times 3 = 9$ です。低温極限 $k_{\mathrm{B}}T \ll \dfrac{\hbar^2}{I}$ ではこの2準位のみを残して近似します。

$$
Z_{\mathrm{eq}} \simeq 1 + 9\exp\!\left(-\frac{\hbar^2}{Ik_{\mathrm{B}}T}\right)
$$

設問 (4) と同様に計算すると，低温極限の回転比熱 $C(T)$ は次式となります。

$$
\finalanswer{C(T) \simeq 9k_{\mathrm{B}}\left(\frac{\hbar^2}{Ik_{\mathrm{B}}T}\right)^2\exp\!\left(-\frac{\hbar^2}{Ik_{\mathrm{B}}T}\right)}
$$

### (7)

$S = 0$ の状態を**パラ状態**，$S = 1$ の状態を**オルト状態**といいます。パラ状態とオルト状態の間の遷移には原子核スピンの反転が必要であり，外部からの強い磁気的摂動がない限りその遷移確率は小さく，緩和時間が長くなります。

十分高温の熱平衡状態では多くの回転準位が励起されるため，$S = 0$ の分子と $S = 1$ の分子の個数比は核スピン縮重度の比 $1 : 3$ になります。この気体を急冷した直後に測定する比熱 $C_1$ では，オルト・パラ間の遷移が追いつかず $1 : 3$ の混合比が凍結されたままになります。このとき，$S = 0$ の分子はエネルギー差 $\dfrac{3\hbar^2}{I}$ の $l = 0$ と $l = 2$ の間でのみ，$S = 1$ の分子はエネルギー差 $\dfrac{5\hbar^2}{I}$ の $l = 1$ と $l = 3$ の間でのみ励起するため，2種類の成分の加重平均の比熱 $C_1 = \dfrac{1}{4}C_{S=0} + \dfrac{3}{4}C_{S=1}$ が観測されます。

一方，熱平衡を保ちながら十分ゆっくり冷却すると，オルト状態からパラ状態への緩和が進行し，ほとんどの分子が $S = 0$ の $l = 0$ 基底状態へ移ります。このときの比熱 $C_2$ はエネルギー差 $\dfrac{\hbar^2}{I}$ の $l = 0$ と $l = 1$ の間の熱励起を伴う設問 (6) の平衡比熱 $C_{\mathrm{eq}}$ に従います。このように，急冷では核スピン状態の組成比が凍結されるのに対し，緩慢冷却ではオルト・パラ間の熱平衡が実現されるため，$C_1$ と $C_2$ に違いが生じます。
