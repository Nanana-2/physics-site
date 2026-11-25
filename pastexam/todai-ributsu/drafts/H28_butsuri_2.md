---
title: 東大理物 平成28年度 物理学 第2問：独立調和振動子と1次元連成振動子鎖の比熱
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
  - 物性物理学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成28年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成28年度 物理学 第2問：独立調和振動子と1次元連成振動子鎖の比熱

## 問題

自然長 $a$ のバネと質量 $m$ の質点からなる系が，温度 $T$ の平衡状態にある場合について考える。バネ定数は $m\omega^2$ であり，$\omega > 0$ とする。

まず，$N$ 個の質点がそれぞれ独立にバネと結合し，互いに独立な調和振動子系をなす場合を考える（図1）。系のハミルトニアンは，$j$ 番目の質点の位置を $x_j$，運動量を $p_j$ として

$$
H = \sum_{j=1}^{N}\left(\frac{1}{2m}p_j^2 + \frac{m\omega^2}{2}(x_j - a)^2\right) \tag{1}
$$

で与えられるとする。ただし，バネの質量は無視できるものとする。ボルツマン定数を $k_{\mathrm{B}}$ として，以下の問に答えよ。

<figure class="problem-figure" markdown>
![j番目の調和振動子](../../../docs/assets/figures/pastexam-todai-ributsu/H28_butsuri_2-p1-light.svg#only-light)
![j番目の調和振動子](../../../docs/assets/figures/pastexam-todai-ributsu/H28_butsuri_2-p1-dark.svg#only-dark)
<figcaption markdown="span">図1：$j$ 番目の調和振動子。</figcaption>
</figure>

(1) この系を古典力学的に考えた場合，質点1個当たりの内部エネルギー $U$，比熱 $C$ を求めよ。また，1番目の質点の位置の平均 $\langle x_1 \rangle$，位置の分散 $\langle x_1^2 \rangle - \langle x_1 \rangle^2$ を求めよ。必要なら，次の公式を用いてよい。

$$
\int_{-\infty}^{\infty} e^{-\alpha x^2} dx = \sqrt{\frac{\pi}{\alpha}},\qquad
\int_{-\infty}^{\infty} x^2 e^{-\alpha x^2} dx = \frac{1}{2\alpha}\sqrt{\frac{\pi}{\alpha}},\qquad (\alpha > 0) \tag{2}
$$

(2) この系を量子力学的に考えた場合，質点1個当たりの内部エネルギー $U_{\mathrm{Q}}$，比熱 $C_{\mathrm{Q}}$ を求めよ。また，1番目の質点の位置の平均，位置の分散を求めよ。温度が高い極限と低い極限において，比熱 $C_{\mathrm{Q}}$ と設問1の結果 $C$ を比較せよ。必要なら，次の関係を用いてよい。量子力学での調和振動子（位置座標 $X$，運動量 $P$）の固有ベクトル $|n\rangle,\ (n = 0, 1, 2, \dots)$ の固有値は

$$
H|n\rangle = \left(\frac{1}{2m}P^2 + \frac{m\omega^2}{2}X^2\right)|n\rangle = \hbar\omega\left(n + \frac{1}{2}\right)|n\rangle \tag{3}
$$

で与えられる。ここで固有ベクトル $|n\rangle$ は完全規格直交系をなすとする。また，位置の演算子 $X$ に対して

$$
X|n\rangle = \sqrt{\frac{\hbar}{2m\omega}}\left(\sqrt{n}\,|n - 1\rangle + \sqrt{n + 1}\,|n + 1\rangle\right),\quad n > 0,\qquad X|0\rangle = \sqrt{\frac{\hbar}{2m\omega}}|1\rangle \tag{4}
$$

であるとしてよい。

次に，$N$ 個の質点を $N + 1$ 個のバネで1次元的に結合した場合について考える（図2）。運動は1次元的であり，質点の位置をそれぞれ $x_1, x_2, \dots, x_N$，運動量を $p_1, p_2, \dots, p_N$ とする。系のハミルトニアンは

$$
\begin{aligned}
H &= \frac{m\omega^2}{2}(x_1 - a)^2 + \frac{1}{2m}p_1^2 + \frac{m\omega^2}{2}(x_2 - x_1 - a)^2 + \frac{1}{2m}p_2^2 + \dots \\
&\quad + \frac{m\omega^2}{2}(x_N - x_{N-1} - a)^2 + \frac{1}{2m}p_N^2 + \frac{m\omega^2}{2}\bigl((N + 1)a - x_N - a\bigr)^2
\end{aligned} \tag{5}
$$

で与えられる。

<figure class="problem-figure" markdown>
![N個の質点をN+1個のバネで結合した1次元連成振動子系](../../../docs/assets/figures/pastexam-todai-ributsu/H28_butsuri_2-p2-light.svg#only-light)
![N個の質点をN+1個のバネで結合した1次元連成振動子系](../../../docs/assets/figures/pastexam-todai-ributsu/H28_butsuri_2-p2-dark.svg#only-dark)
<figcaption markdown="span">図2：$N$ 個の質点を $N + 1$ 個のバネで結合した1次元連成振動子系。両端は全体の自然長で固定されている。</figcaption>
</figure>

(3) この系は $N$ 個の独立な基準振動の和で表される。それぞれの基準振動の固有振動数が以下で与えられることを示せ。

$$
\omega_\ell = \omega\sqrt{2 - 2\cos\left(\frac{\ell}{N + 1}\pi\right)},\qquad \ell = 1, 2, \dots, N \tag{6}
$$

(4) この系を古典力学的に考えた場合，質点1個当たりの比熱 $C_1$ を求めよ。

(5) この系を量子力学的に考えた場合，質点1個当たりの比熱 $C_{1\mathrm{Q}}$ は，$N$ が非常に大きく，かつ低温の極限では温度のべきに比例する。つまり，$C_{1\mathrm{Q}} \simeq A T^b$ の形に表わされる。べき $b$ と係数 $A$ を求めよ。必要なら，次の公式を用いてよい。

$$
\int_0^{\infty} \frac{x}{e^x - 1}dx = \frac{1}{2}\int_0^{\infty} \frac{x^2 e^x}{(e^x - 1)^2}dx = \frac{\pi^2}{6} \tag{7}
$$

> 出典：東京大学大学院理学系研究科物理学専攻 平成28年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
バネにつながれた振動子が独立なら，分配関数は1個の振動子の分配関数の $N$ 乗です。古典系では，位置と運動量についての積分がそれぞれガウス積分になるので，比熱や位置の分散は温度によらない定数か温度に比例する量になります。

質点どうしをバネで結ぶと，変位は互いに独立ではありません。そこで変位を基準振動の座標に変換し，振動数の異なる独立な振動子の集まりとして扱います。低温では振動数の低いモードだけが励起されるので，振動数が $0$ に近いモードの数え方から比熱の温度依存性を求めます。
</div>

### (1)
$\beta=\dfrac{1}{k_{\mathrm B}T}$ とおきます。振動子は互いに独立なので，座標 $X=x_1-a$，運動量 $p=p_1$ の1個の分配関数を式 (2) から計算します。

$$
\begin{aligned}
Z_1 &= \frac{1}{h}\int_{-\infty}^{\infty} e^{-\frac{\beta p^2}{2m}}\,\mathrm{d}p \int_{-\infty}^{\infty} e^{-\frac{\beta m\omega^2}{2}X^2}\,\mathrm{d}X \\
&= \frac{1}{h}\sqrt{\frac{2\pi m}{\beta}}\sqrt{\frac{2\pi}{\beta m\omega^2}} \\
&= \frac{2\pi}{h\beta\omega}
\end{aligned}
$$

これより1質点あたりの内部エネルギー $U$ と比熱 $C$ は次のようになります。

$$
\begin{aligned}
U&=-\frac{\partial\ln Z_1}{\partial\beta}\\
&=\frac{1}{\beta}\\
&=k_{\mathrm B}T\\
C&=\frac{\partial U}{\partial T}\\
&=k_{\mathrm B}
\end{aligned}
$$

また $X = x_1 - a$ の分布は偶関数なので $\langle X \rangle = 0$，すなわち $\langle x_1 \rangle = a$ です。$\alpha=\dfrac{\beta m\omega^2}{2}$ とおき，式 (2) から位置の分散 $\langle X^2\rangle$ を求めます。

$$
\begin{aligned}
\langle X^2 \rangle &= \frac{\int_{-\infty}^{\infty} X^2 e^{-\alpha X^2}\,\mathrm{d}X}{\int_{-\infty}^{\infty} e^{-\alpha X^2}\,\mathrm{d}X} \\
&= \frac{1}{2\alpha} \\
&= \frac{1}{\beta m\omega^2} \\
&= \frac{k_{\mathrm{B}}T}{m\omega^2}
\end{aligned}
$$

したがって，

$$
\finalanswer{U = k_{\mathrm{B}}T,\qquad C = k_{\mathrm{B}},\qquad \langle x_1 \rangle = a,\qquad \langle x_1^2 \rangle - \langle x_1 \rangle^2 = \frac{k_{\mathrm{B}}T}{m\omega^2}}
$$

### (2)
1個の量子調和振動子の分配関数 $Z_{1\mathrm{Q}}$ を式 (3) より計算します。

$$
\begin{aligned}
Z_{1\mathrm{Q}} &= \sum_{n=0}^{\infty} e^{-\beta\hbar\omega\left(n + \frac{1}{2}\right)} \\
&= \frac{e^{-\frac{\beta\hbar\omega}{2}}}{1 - e^{-\beta\hbar\omega}} \\
&= \frac{1}{2\sinh\left(\dfrac{\beta\hbar\omega}{2}\right)}
\end{aligned}
$$

これより1質点あたりの内部エネルギー $U_{\mathrm{Q}}$ と比熱 $C_{\mathrm{Q}}$ を求めます。

$$
\begin{aligned}
U_{\mathrm{Q}} &= -\frac{\partial\ln Z_{1\mathrm{Q}}}{\partial\beta} \\
&= \hbar\omega\left(\frac{1}{2} + \frac{1}{e^{\beta\hbar\omega} - 1}\right) \\
&= \frac{\hbar\omega}{2}\coth\left(\frac{\beta\hbar\omega}{2}\right) \\
C_{\mathrm{Q}} &= \frac{\partial U_{\mathrm{Q}}}{\partial T} \\
&= k_{\mathrm{B}}\left(\frac{\hbar\omega}{k_{\mathrm{B}}T}\right)^2\frac{e^{\frac{\hbar\omega}{k_{\mathrm{B}}T}}}{\left(e^{\frac{\hbar\omega}{k_{\mathrm{B}}T}} - 1\right)^2}
\end{aligned}
$$

次に位置の平均と分散を求めます。$X=x_1-a$ とすると，式 (4) から $\langle n|X|n\rangle=0$ なので，$\langle x_1\rangle=a$ です。各固有状態の分散は，

$$
\begin{aligned}
\langle n|X^2|n\rangle&=\|X|n\rangle\|^2\\
&=\frac{\hbar}{2m\omega}\bigl(n+n+1\bigr)\\
&=\frac{\hbar}{m\omega}\left(n+\frac12\right)
\end{aligned}
$$

です。エネルギー固有値の熱平均を使うと，

$$
\begin{aligned}
\langle x_1^2 \rangle - \langle x_1 \rangle^2 &= \langle X^2 \rangle \\
&= \frac{1}{Z_{1\mathrm{Q}}}\sum_{n=0}^{\infty} \langle n|X^2|n\rangle e^{-\beta\hbar\omega\left(n + \frac{1}{2}\right)} \\
&= \frac{1}{m\omega^2} U_{\mathrm{Q}} \\
&= \frac{\hbar}{2m\omega}\coth\left(\frac{\hbar\omega}{2k_{\mathrm{B}}T}\right)
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{U_{\mathrm{Q}} = \hbar\omega\left(\frac{1}{2} + \frac{1}{e^{\frac{\hbar\omega}{k_{\mathrm{B}}T}} - 1}\right),\qquad C_{\mathrm{Q}} = k_{\mathrm{B}}\left(\frac{\hbar\omega}{k_{\mathrm{B}}T}\right)^2\frac{e^{\frac{\hbar\omega}{k_{\mathrm{B}}T}}}{\left(e^{\frac{\hbar\omega}{k_{\mathrm{B}}T}} - 1\right)^2},\qquad \langle x_1 \rangle = a,\qquad \langle x_1^2 \rangle - \langle x_1 \rangle^2 = \frac{\hbar}{2m\omega}\coth\left(\frac{\hbar\omega}{2k_{\mathrm{B}}T}\right)}
$$

古典論の結果 $C = k_{\mathrm{B}}$ と比べます。$k_{\mathrm{B}}T \gg \hbar\omega$ の高温では，$e^{\hbar\omega/(k_{\mathrm{B}}T)} - 1 \simeq \dfrac{\hbar\omega}{k_{\mathrm{B}}T}$ なので，$C_{\mathrm{Q}} \to k_{\mathrm{B}}$ となり，古典論の結果と一致します。

$k_{\mathrm{B}}T \ll \hbar\omega$ の低温では，$C_{\mathrm{Q}} \simeq k_{\mathrm{B}}\left(\dfrac{\hbar\omega}{k_{\mathrm{B}}T}\right)^2 e^{-\hbar\omega/(k_{\mathrm{B}}T)}$ となり，$C_{\mathrm{Q}}$ は指数関数的に $0$ に近づきます。古典論の比熱は温度によらず $k_{\mathrm{B}}$ なので，低温では2つの結果は大きく異なります。

### (3)
平衡位置からの変位を $u_j = x_j - ja\ (j = 1, 2, \dots, N)$ とおき，固定端条件を $u_0 = u_{N+1} = 0$ で表します。ハミルトニアン (5) は次のように書かれます。

$$
H = \sum_{j=1}^{N} \frac{p_j^2}{2m} + \frac{m\omega^2}{2}\sum_{j=0}^{N} \left(u_{j+1} - u_j\right)^2
$$

離散サイン変換という直交変換により基準座標 $Q_\ell$ と基準運動量 $P_\ell\ (\ell = 1, 2, \dots, N)$ を定義します。

$$
u_j = \sqrt{\frac{2}{N + 1}}\sum_{\ell=1}^{N} Q_\ell \sin\left(\frac{\ell j\pi}{N + 1}\right),\qquad
p_j = \sqrt{\frac{2}{N + 1}}\sum_{\ell=1}^{N} P_\ell \sin\left(\frac{\ell j\pi}{N + 1}\right)
$$

$j=0,N+1$ では $u_0 = u_{N+1} = 0$ を満たします。直交性 $\dfrac{2}{N + 1}\displaystyle\sum_{j=1}^{N}\sin\left(\dfrac{\ell j\pi}{N + 1}\right)\sin\left(\dfrac{\ell' j\pi}{N + 1}\right) = \delta_{\ell\ell'}$ より運動エネルギーは $\displaystyle\sum_{j=1}^{N}\dfrac{p_j^2}{2m} = \sum_{\ell=1}^{N}\dfrac{P_\ell^2}{2m}$ です。

一方，ポテンシャルエネルギーは $u_0 = u_{N+1} = 0$ を用いて部分和をとると

$$
\sum_{j=0}^{N} (u_{j+1} - u_j)^2 = \sum_{j=1}^{N} u_j\left(2u_j - u_{j-1} - u_{j+1}\right)
$$

となり，三角関数の和積公式より

$$
2\sin\left(\frac{\ell j\pi}{N + 1}\right) - \sin\left(\frac{\ell(j - 1)\pi}{N + 1}\right) - \sin\left(\frac{\ell(j + 1)\pi}{N + 1}\right)
= \left[2 - 2\cos\left(\frac{\ell\pi}{N + 1}\right)\right]\sin\left(\frac{\ell j\pi}{N + 1}\right)
$$

なので，再び直交性を用いてハミルトニアンは次のように対角化されます。

$$
H = \sum_{\ell=1}^{N}\left(\frac{P_\ell^2}{2m} + \frac{m\omega_\ell^2}{2} Q_\ell^2\right),\qquad
\omega_\ell = \omega\sqrt{2 - 2\cos\left(\frac{\ell}{N + 1}\pi\right)} \quad (\ell = 1, 2, \dots, N)
$$

よって $N$ 個の独立な基準振動の和で表され，各固有振動数が式 (6) で与えられることが確かめられます。

### (4)
問3の直交変換は正準変換なので，古典分配関数は固有振動数 $\omega_\ell\ (\ell = 1, \dots, N)$ をもつ $N$ 個の独立な古典調和振動子の分配関数の積になります。各モードの内部エネルギーは $\omega_\ell$ によらず $k_{\mathrm{B}}T$ なので，全内部エネルギーは $N k_{\mathrm{B}}T$，質点1個あたりの比熱 $C_1$ は $k_{\mathrm{B}}$ です。したがって，

$$
\finalanswer{C_1 = k_{\mathrm{B}}}
$$

### (5)
問2と問3より，量子1次元連成振動子系の質点1個あたりの比熱 $C_{1\mathrm{Q}}$ は各基準モードの比熱の平均です。

$$
C_{1\mathrm{Q}} = \frac{1}{N}\sum_{\ell=1}^{N} k_{\mathrm{B}}\left(\frac{\beta\hbar\omega_\ell}{1}\right)^2\frac{e^{\beta\hbar\omega_\ell}}{\left(e^{\beta\hbar\omega_\ell} - 1\right)^2}
$$

式 (6) の振動数は $\omega_\ell=2\omega\sin\!\left(\dfrac{\ell\pi}{2(N+1)}\right)$ です。低温 $k_{\mathrm B}T\ll\hbar\omega$ では，$\beta\hbar\omega_\ell\lesssim1$ となる低振動数のモードを考えます。$\ell\ll N$ に対して，

$$
\begin{aligned}
\omega_\ell&\simeq\frac{\pi\omega}{N+1}\ell\\
&\simeq\frac{\pi\omega}{N}\ell
\end{aligned}
$$

と近似します。多くのモードが熱励起される大きな $N$ を考え，和を $\ell$ の積分に置き換えて上限を $\infty$ に伸ばします。

積分変数を $x=\dfrac{\beta\hbar\pi\omega}{N}\ell$ とすると，$\mathrm{d}\ell=\dfrac{Nk_{\mathrm B}T}{\pi\hbar\omega}\mathrm{d}x$ です。式 (7) の積分を用います。

$$
\begin{aligned}
C_{1\mathrm{Q}} &\simeq \frac{k_{\mathrm{B}}}{N}\int_0^{\infty} \frac{\left(\frac{\beta\hbar\pi\omega}{N}\ell\right)^2 e^{\frac{\beta\hbar\pi\omega}{N}\ell}}{\left(e^{\frac{\beta\hbar\pi\omega}{N}\ell} - 1\right)^2}\,\mathrm{d}\ell \\
&= \frac{k_{\mathrm{B}}}{N}\cdot\frac{N k_{\mathrm{B}}T}{\pi\hbar\omega}\int_0^{\infty}\frac{x^2 e^x}{(e^x - 1)^2}\,\mathrm{d}x \\
&= \frac{k_{\mathrm{B}}^2 T}{\pi\hbar\omega}\cdot\frac{\pi^2}{3} \\
&= \frac{\pi k_{\mathrm{B}}^2}{3\hbar\omega} T
\end{aligned}
$$

したがって，$C_{1\mathrm{Q}} \simeq A T^b$ と比較すると，

$$
\finalanswer{b = 1,\qquad A = \frac{\pi k_{\mathrm{B}}^2}{3\hbar\omega}}
$$

<aside class="rigor-note" markdown>
有限の $N$ では最低振動数が $\omega_1\simeq\pi\omega/(N+1)$ なので，低温で常に $T$ に比例するわけではありません。和を連続積分にするには，$\hbar\omega_1\ll k_{\mathrm B}T\ll\hbar\omega$ の範囲が必要です。$N\to\infty$ を先にとった低温極限で，設問5のべき則が得られます。
</aside>
