---
title: 東大理物 平成22年度 物理学 第1問：無限井戸型ポテンシャルと中央のデルタ関数ポテンシャル
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成22年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成22年度 物理学 第1問：無限井戸型ポテンシャルと中央のデルタ関数ポテンシャル

## 問題

ポテンシャル

$$
V_0(x) = \begin{cases} \infty & (x \le -L) \\ 0 & (-L < x < L) \\ \infty & (x \ge L) \end{cases}
$$

に閉じ込められている質量 $m$ の粒子の1次元運動を考える。このとき，次の設問に答えよ。答えだけでなく，途中の考え方も述べよ。

(1) この粒子のすべてのエネルギー固有値と，それらに対応する $1$ に規格化された波動関数を求めよ。

(2) 設問1で求めたエネルギー固有値の最小値がゼロでない値をとる物理的理由を説明せよ。

次に，$V_0(x)$ にデルタ関数型のポテンシャルを加えたポテンシャル $V_0(x) + V_1\delta(x)$ 中の粒子に関して以下の設問に答えよ。ただし，$V_1 > 0$ とする。

(3) 基底状態のエネルギーを $V_1$ の1次まで求めよ。

(4) 第1励起状態のエネルギーを求めよ。

(5) 基底状態と第1励起状態の波動関数の概略をそれぞれ図示せよ。

(6) $V_1$ をゼロから無限大まで増加させるとき，基底状態と第1励起状態のエネルギーが $V_1$ の関数としてどのように変化するかの概略を図示せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成22年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
井戸は原点について左右対称なので，ハミルトニアンは $x\to-x$ の反転で変わりません。そのため，固有関数は偶関数か奇関数のどちらかに選ぶことができ，偶関数と奇関数を分けて扱うことができます。

デルタ関数 $V_1\delta(x)$ は，波動関数の原点での値を通してだけエネルギーに効きます。そこで，偶関数と奇関数のそれぞれについて原点での値に注目します。$V_1$ が小さいときは，無摂動の波動関数で $V_1\delta(x)$ の期待値をとる1次の摂動論を用います。

$V_1$ が大きい極限は，デルタ関数を含む方程式を原点の前後で積分し，傾きの跳びと原点での波動関数の値を結び付けて扱います。$V_1$ を増やしたときのエネルギーの変化は，$V_1=0$ と $V_1\to\infty$ の2つの端から描きます。
</div>

### (1)
$|x| \ge L$ ではポテンシャルが無限大なので $\psi(x) = 0$ です。$-L < x < L$ でのシュレーディンガー方程式は $E > 0$ に対して $k = \dfrac{\sqrt{2mE}}{\hbar} > 0$ とおくと次のようになります。

$$
\begin{aligned}
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} &= E\psi \\
\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} + k^2\psi &= 0
\end{aligned}
$$

一般解は $\psi(x) = A\cos(kx) + B\sin(kx)$ です。境界条件 $\psi(-L)=0$，$\psi(L)=0$ を課します。

$$
\begin{aligned}
A\cos(kL) + B\sin(kL) &= 0 \\
A\cos(kL) - B\sin(kL) &= 0
\end{aligned}
$$

2式の和と差から $A\cos(kL) = 0$，$B\sin(kL) = 0$ が得られます。恒等的に $0$ でない解が存在するのは次の2通りです。

- $B = 0$ かつ $\cos(kL) = 0$ のとき：$kL = \dfrac{n\pi}{2}$（$n = 1, 3, 5, \dots$）となり，$\psi_n(x) = A\cos\!\left(\dfrac{n\pi x}{2L}\right)$ です。
- $A = 0$ かつ $\sin(kL) = 0$ のとき：$kL = \dfrac{n\pi}{2}$（$n = 2, 4, 6, \dots$）となり，$\psi_n(x) = B\sin\!\left(\dfrac{n\pi x}{2L}\right)$ です。

規格化条件を課すと，偶関数の余弦の係数と奇関数の正弦の係数は，それぞれ絶対値が $1/\sqrt L$ となります。

$$
\int_{-L}^L\cos^2\!\left(\frac{n\pi x}{2L}\right)\mathrm{d}x=L\quad(n=1,3,5,\dots),
$$

$$
\int_{-L}^L\sin^2\!\left(\frac{n\pi x}{2L}\right)\mathrm{d}x=L\quad(n=2,4,6,\dots)
$$

各状態の残る係数を実数正に選びます。エネルギーは，$E_n=\hbar^2k_n^2/(2m)$ に $k_n=n\pi/(2L)$ を代入して求めます。

$$
\finalanswer{E_n = \frac{\pi^2 \hbar^2 n^2}{8m L^2} \quad (n = 1, 2, 3, \dots)}
$$

対応する規格化波動関数は次のとおりです。

$$
\finalanswer{\psi_n(x)=\begin{cases}
0 &( |x|\ge L),\\
\dfrac{1}{\sqrt L}\cos\!\left(\dfrac{n\pi x}{2L}\right)&(|x|<L,\ n=1,3,5,\dots),\\
\dfrac{1}{\sqrt L}\sin\!\left(\dfrac{n\pi x}{2L}\right)&(|x|<L,\ n=2,4,6,\dots)
\end{cases}}
$$

### (2)
粒子は幅 $2L$ の有限領域に閉じ込められているため，位置の不確定さ $\Delta x$ は最大でも $L$ の程度に制限されます。ハイゼンベルクの不確定性関係 $\Delta x \cdot \Delta p \ge \dfrac{\hbar}{2}$ より，運動量の不確定さ $\Delta p$ は $0$ にならず $\Delta p \gtrsim \dfrac{\hbar}{2L} > 0$ を満たします。したがって運動量の2乗の期待値 $\langle p^2 \rangle \ge (\Delta p)^2 > 0$ となり，運動エネルギー $\dfrac{\langle p^2 \rangle}{2m}$ が $0$ より大きい値をとります。

### (3)
$V_1 \delta(x)$ を摂動ハミルトニアン $\hat{H}' = V_1 \delta(x)$ とみなし，1次の摂動論を用います。無摂動の基底状態は $\psi_1^{(0)}(x) = \dfrac{1}{\sqrt{L}}\cos\!\left(\dfrac{\pi x}{2L}\right)$，エネルギーは $E_1^{(0)} = \dfrac{\pi^2 \hbar^2}{8m L^2}$ です。1次のエネルギー補正 $E_1^{(1)}$ を計算します。

$$
\begin{aligned}
E_1^{(1)} &= \int_{-L}^{L} \bigl|\psi_1^{(0)}(x)\bigr|^2 V_1\delta(x)\,\mathrm{d}x \\
&= V_1 \bigl|\psi_1^{(0)}(0)\bigr|^2 \\
&= \frac{V_1}{L}
\end{aligned}
$$

したがって基底状態のエネルギーを $V_1$ の1次まで求めると次のようになります。

$$
\finalanswer{E_1 \simeq \frac{\pi^2 \hbar^2}{8m L^2} + \frac{V_1}{L}}
$$

### (4)
無摂動の第1励起状態は奇関数 $\psi_2^{(0)}(x) = \dfrac{1}{\sqrt{L}}\sin\!\left(\dfrac{\pi x}{L}\right)$ であり，原点で $\psi_2^{(0)}(0) = 0$ となります。したがって任意の $V_1 > 0$ に対して

$$
\begin{aligned}
V_1\delta(x)\psi_2^{(0)}(x) &= V_1\psi_2^{(0)}(0)\delta(x) \\
&= 0
\end{aligned}
$$

が成り立ちます。この式は摂動の次数によらないので，$\psi_2^{(0)}(x)$ はそのまま摂動後のハミルトニアンの固有状態になります。

偶関数の状態のエネルギーは，$V_1$ を増やすと単調に増えます。ただし，$V_1 \to \infty$ でも基底状態のエネルギーは $E_2$ を超えません。よって，第1励起状態はこの奇関数の状態のままで，エネルギーは $V_1$ によらず一定です。

$$
\finalanswer{E_2 = \frac{\pi^2 \hbar^2}{2m L^2}}
$$

### (5)
基底状態の波動関数 $\psi_1(x)$ は偶関数であり，原点 $x = 0$ でシュレーディンガー方程式を積分すると1階微分の跳びの条件

$$
\psi_1'(0+) - \psi_1'(0-) = \frac{2m V_1}{\hbar^2}\psi_1(0) > 0
$$

が得られます。基底状態の符号を正に選ぶと，原点で傾きが負から正に跳び，中央にくぼみのある左右対称な2つの山になります。一方，第1励起状態の波動関数 $\psi_2(x)$ は $V_1 = 0$ のときと同じ $\dfrac{1}{\sqrt{L}}\sin\!\left(\dfrac{\pi x}{L}\right)$ のままです。それぞれの概略を次の図に示します。

<figure class="problem-figure" markdown>
![基底状態と第1励起状態の波動関数の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H22_butsuri_1-s1-light.svg#only-light)
![基底状態と第1励起状態の波動関数の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H22_butsuri_1-s1-dark.svg#only-dark)
<figcaption markdown="span">左は基底状態の波動関数 $\psi_1(x)$ の概略で破線が $V_1 = 0$ のとき，右は第1励起状態の波動関数 $\psi_2(x)$ の概略。</figcaption>
</figure>

### (6)
$V_1 = 0$ のとき $E_1 = \dfrac{\pi^2 \hbar^2}{8m L^2}$，$E_2 = \dfrac{\pi^2 \hbar^2}{2m L^2}$ です。$V_1$ を増加させると，$E_2$ は一定値 $\dfrac{\pi^2 \hbar^2}{2m L^2}$ のまま変化しません。

一方，$E_1$ は $V_1 = 0$ の近傍で傾き $1/L$ で増加を始め，$V_1$ とともに単調に増加します。$V_1 \to \infty$ の極限では原点 $x = 0$ に無限に高い壁が立つため $\psi_1(0) \to 0$ となり，粒子は幅 $L$ の独立な2つの井戸 $(-L, 0)$ と $(0, L)$ に閉じ込められます。幅 $L$ の無限井戸の基底エネルギーは $\dfrac{\pi^2 \hbar^2}{2m L^2}$ なので，$E_1$ は $V_1 \to \infty$ で $E_2$ に下から漸近します。概略は次の図のとおりです。

<figure class="problem-figure" markdown>
![V_1の関数としての基底状態と第1励起状態のエネルギー変化](../../../docs/assets/figures/pastexam-todai-ributsu/H22_butsuri_1-s2-light.svg#only-light)
![V_1の関数としての基底状態と第1励起状態のエネルギー変化](../../../docs/assets/figures/pastexam-todai-ributsu/H22_butsuri_1-s2-dark.svg#only-dark)
<figcaption markdown="span">$V_1$ を $0$ から $\infty$ へ増やすときの基底状態エネルギー $E_1$ と第1励起状態エネルギー $E_2$ の変化。</figcaption>
</figure>
