---
title: 東大理物 平成31年度 物理学 第2問：1次元2状態古典スピン鎖の分配関数と相関長
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成31年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成31年度 物理学 第2問：1次元2状態古典スピン鎖の分配関数と相関長

## 問題

スピンを持つ原子が図1のように1次元的に並んで相互作用している古典的な系を考える。これらの原子に，左端から順に $i = 1, 2, \dots, L$ と番号を付け，$i$ 番目の原子のスピンの状態を表す変数を $\mathbf{S}_i$ とする。ただし，$L \ge 2$ とし，$\mathbf{S}_i$ は，$\hat{x} = (1, 0, 0)$ か $\hat{y} = (0, 1, 0)$ のいずれかをとるものとする（図1）。この系の各状態は，スピン配置 $(\mathbf{S}_1, \dots, \mathbf{S}_L)$ で指定され，そのエネルギーは，

$$
E(\mathbf{S}_1, \dots, \mathbf{S}_L) = -J\sum_{i=1}^{L-1} \mathbf{S}_i \cdot \mathbf{S}_{i+1} \tag{1}
$$

で与えられる。ここで，$J > 0$ である。この系が，温度 $T$ の熱平衡状態にあるとする。ここで，ボルツマン定数 $k_{\mathrm{B}}$ を用いて逆温度を $\beta = 1/(k_{\mathrm{B}}T)$ と定義し，系の分配関数を $Z_L(\beta)$ とする。以下の設問に答えよ。

<figure class="problem-figure" markdown>
![L=6の場合の1次元スピン配置の例](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_2-p-light.svg#only-light)
![L=6の場合の1次元スピン配置の例](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">図1：$L = 6$ の場合のスピン配置の例。</figcaption>
</figure>

(1) $L = 2$ の場合に，可能なスピン配置をすべて列挙し，それぞれのエネルギーを求めよ。また，その結果をもとに，分配関数 $Z_2(\beta)$ を求めよ。

(2) $L = 3$ の場合に，可能なスピン配置をすべて列挙し，それぞれのエネルギーを求めよ。また，その結果をもとに，分配関数 $Z_3(\beta)$ を求めよ。

(3) 一般の $L$ について，$Z_L(\beta)$ を求めよ。ただし，$L \ge 3$ のとき，$Z_L(\beta)$ は $Z_{L-1}(\beta)$ を用いて表すことができる。その関係式を用いてよい。

(4) 一般の $L$ について，系の自由エネルギー $F_L(\beta)$ を求めよ。

(5) $L$ が十分大きい極限での，スピン1個あたりの内部エネルギー $u(\beta)$ を求めよ。また，高温極限および低温極限での $u(\beta)$ の値とスピン配置の出現確率との関係について説明せよ。

次に，原子数 $L$ の系の左端のスピン $\mathbf{S}_1$ と右端のスピン $\mathbf{S}_L$ の内積の期待値 $\langle \mathbf{S}_1 \cdot \mathbf{S}_L \rangle$ について考える。

(6) 原子数 $L$ の系において，$\mathbf{S}_1 = \hat{a}$ かつ $\mathbf{S}_L = \hat{b}$（$\hat{a}, \hat{b}$ は，$\hat{x}, \hat{y}$ のいずれか）である確率を $P_L(\hat{a}, \hat{b})$ とする。$L \ge 3$ のとき，$P_L(\hat{a}, \hat{b})$ と $P_{L-1}(\hat{a}, \hat{b})$ の間には，以下の関係が成り立つ。

$$
\begin{pmatrix} P_L(\hat{x}, \hat{x}) & P_L(\hat{x}, \hat{y}) \\ P_L(\hat{y}, \hat{x}) & P_L(\hat{y}, \hat{y}) \end{pmatrix}
= \begin{pmatrix} P_{L-1}(\hat{x}, \hat{x}) & P_{L-1}(\hat{x}, \hat{y}) \\ P_{L-1}(\hat{y}, \hat{x}) & P_{L-1}(\hat{y}, \hat{y}) \end{pmatrix}
\begin{pmatrix} Q(\hat{x}, \hat{x}) & Q(\hat{x}, \hat{y}) \\ Q(\hat{y}, \hat{x}) & Q(\hat{y}, \hat{y}) \end{pmatrix} \tag{2}
$$

このとき，4つの行列要素 $Q(\hat{a}, \hat{b})$ を $\beta, J$ を用いて表せ。

(7) $\langle \mathbf{S}_1 \cdot \mathbf{S}_L \rangle$ を，$\beta, J, L$ を用いて表せ。また，$\langle \mathbf{S}_1 \cdot \mathbf{S}_L \rangle$ は，$L$ に依存しない定数 $A, B, \xi$ を用いて

$$
\langle \mathbf{S}_1 \cdot \mathbf{S}_L \rangle = A + B\exp\left(-\frac{L - 1}{\xi}\right) \tag{3}
$$

と書ける。高温極限および低温極限における $\xi$ を，それぞれ $\beta, J$ を用いて表せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成31年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
開いた鎖の端に原子を1つ加えると，エネルギーは新しいボンド1本の分だけ変わります。加えたスピンの向きについて和をとると，残りのスピンの向きによらない因子 $e^{\beta J}+1$ が出ます。そのため，$Z_L$ は $Z_{L-1}$ にこの因子を掛けたものになります。

両端のスピンの同時確率も，原子を1つ加えるごとに2行2列の行列 $Q$ を掛けたものになります。そこで $Q$ を対角化すると，相関は $Q$ の2つの固有値の比の $L$ 乗で変わります。相関長は，この比の対数から求めます。
</div>

### (1)


$\hat{x}\cdot\hat{x} = \hat{y}\cdot\hat{y} = 1$， $\hat{x}\cdot\hat{y} = \hat{y}\cdot\hat{x} = 0$ です。$L = 2$ の可能なスピン配置は $2^2 = 4$ 通りあり，それぞれのエネルギー $E(\mathbf{S}_1, \mathbf{S}_2) = -J\,\mathbf{S}_1\cdot\mathbf{S}_2$ は次のとおりです。

- $(\hat{x}, \hat{x})$：$E = -J$
- $(\hat{x}, \hat{y})$：$E = 0$
- $(\hat{y}, \hat{x})$：$E = 0$
- $(\hat{y}, \hat{y})$：$E = -J$

よって分配関数 $Z_2(\beta)$ は次のように求まります。

$$
\begin{aligned}
Z_2(\beta) &= e^{\beta J} + 1 + 1 + e^{\beta J} \\
&= 2\left(e^{\beta J} + 1\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{Z_2(\beta) = 2\left(e^{\beta J} + 1\right)}
$$

### (2)
$L = 3$ の可能なスピン配置は $2^3 = 8$ 通りあり，それぞれのエネルギー $E(\mathbf{S}_1, \mathbf{S}_2, \mathbf{S}_3) = -J(\mathbf{S}_1\cdot\mathbf{S}_2 + \mathbf{S}_2\cdot\mathbf{S}_3)$ は次のとおりです。

- $(\hat{x}, \hat{x}, \hat{x})$，$(\hat{y}, \hat{y}, \hat{y})$：$E=-2J$ です。計2通りあります。
- $(\hat{x}, \hat{x}, \hat{y})$，$(\hat{x}, \hat{y}, \hat{y})$，$(\hat{y}, \hat{x}, \hat{x})$，$(\hat{y}, \hat{y}, \hat{x})$：$E=-J$ です。計4通りあります。
- $(\hat{x}, \hat{y}, \hat{x})$，$(\hat{y}, \hat{x}, \hat{y})$：$E=0$ です。計2通りあります。

よって分配関数 $Z_3(\beta)$ は次のように求まります。

$$
\begin{aligned}
Z_3(\beta) &= 2e^{2\beta J} + 4e^{\beta J} + 2 \\
&= 2\left(e^{\beta J} + 1\right)^2
\end{aligned}
$$

したがって，

$$
\finalanswer{Z_3(\beta) = 2\left(e^{\beta J} + 1\right)^2}
$$

### (3)
$L \ge 3$ のとき，右端のスピン $\mathbf{S}_L$ についての和を先に計算します。$\mathbf{S}_{L-1}$ が $\hat{x}, \hat{y}$ のいずれであっても $\displaystyle\sum_{\mathbf{S}_L \in \{\hat{x}, \hat{y}\}} e^{\beta J\,\mathbf{S}_{L-1}\cdot\mathbf{S}_L} = e^{\beta J} + 1$ となるため，次の漸化式が成り立ちます。

$$
\begin{aligned}
Z_L(\beta)
&= \sum_{\mathbf{S}_1, \dots, \mathbf{S}_{L-1}} e^{-\beta E(\mathbf{S}_1, \dots, \mathbf{S}_{L-1})} \sum_{\mathbf{S}_L} e^{\beta J\,\mathbf{S}_{L-1}\cdot\mathbf{S}_L} \\
&= \left(e^{\beta J} + 1\right) Z_{L-1}(\beta)
\end{aligned}
$$

問1の $Z_2(\beta) = 2(e^{\beta J} + 1)$ から繰り返し用いると，一般の $L \ge 2$ に対して次式が得られます。したがって，

$$
\finalanswer{Z_L(\beta) = 2\left(e^{\beta J} + 1\right)^{L - 1}}
$$

### (4)
ヘルムホルツの自由エネルギー $F_L(\beta) = -\dfrac{1}{\beta}\ln Z_L(\beta)$ に問3の結果を代入します。

$$
F_L(\beta) = -\frac{1}{\beta}\left[\ln 2 + (L - 1)\ln\left(e^{\beta J} + 1\right)\right]
$$

したがって，

$$
\finalanswer{F_L(\beta) = -\frac{1}{\beta}\left[\ln 2 + (L - 1)\ln\left(e^{\beta J} + 1\right)\right]}
$$

### (5)
系全体の内部エネルギー $U_L(\beta)$ は $U_L(\beta) = -\dfrac{\partial \ln Z_L(\beta)}{\partial\beta}$ で与えられます。

$$
\begin{aligned}
U_L(\beta) &= -\frac{\partial}{\partial\beta}\Bigl[\ln 2 + (L - 1)\ln\left(e^{\beta J} + 1\right)\Bigr] \\
&= -(L - 1)\frac{J e^{\beta J}}{e^{\beta J} + 1} \\
&= -(L - 1)\frac{J}{1 + e^{-\beta J}}
\end{aligned}
$$

$L$ が十分大きい極限でスピン1個あたりの内部エネルギー $u(\beta) = \displaystyle\lim_{L\to\infty}\dfrac{U_L(\beta)}{L}$ を求めます。

$$
\begin{aligned}
u(\beta) &= -\frac{J e^{\beta J}}{e^{\beta J} + 1} \\
&= -\frac{J}{1 + e^{-\beta J}}
\end{aligned}
$$

したがって，

$$
\finalanswer{u(\beta) = -\frac{J}{1 + e^{-\beta J}}}
$$

この結果を，高温と低温の極限で確かめます。$\beta J\to0$ の高温では，$u(\beta)\to-J/2$ です。このとき $2^L$ 通りの配置はすべて同じ確率で現れるので，隣り合うスピンの向きがそろう確率とそろわない確率は，ともに $1/2$ です。そろうとボンドのエネルギーは $-J$，そろわないと $0$ なので，ボンド1本あたりの平均エネルギーは $-J/2$ になります。

$\beta J \to \infty$ の低温では，$u(\beta) \to -J$ です。このとき現れるのは，すべてのスピンが $\hat{x}$ にそろった配置と，すべて $\hat{y}$ にそろった配置だけです。どちらの配置でも，すべてのボンドのエネルギーは $-J$ になります。

### (6)
確率 $P_L(\hat{a}, \hat{b})$ の定義より，

$$
\begin{aligned}
P_L(\hat{a}, \hat{b})
&= \frac{1}{Z_L(\beta)}\sum_{\mathbf{S}_2, \dots, \mathbf{S}_{L-1}} e^{-\beta E(\hat{a}, \mathbf{S}_2, \dots, \mathbf{S}_{L-1})}\,e^{\beta J\,\mathbf{S}_{L-1}\cdot\hat{b}} \\
&= \sum_{\hat{c} \in \{\hat{x}, \hat{y}\}} \left(\frac{1}{Z_{L-1}(\beta)}\sum_{\mathbf{S}_2, \dots, \mathbf{S}_{L-2}} e^{-\beta E(\hat{a}, \mathbf{S}_2, \dots, \mathbf{S}_{L-2}, \hat{c})}\right) \frac{Z_{L-1}(\beta)}{Z_L(\beta)}\,e^{\beta J\,\hat{c}\cdot\hat{b}} \\
&= \sum_{\hat{c} \in \{\hat{x}, \hat{y}\}} P_{L-1}(\hat{a}, \hat{c})\,\frac{e^{\beta J\,\hat{c}\cdot\hat{b}}}{e^{\beta J} + 1}
\end{aligned}
$$

ここで問3の関係 $\dfrac{Z_{L-1}(\beta)}{Z_L(\beta)} = \dfrac{1}{e^{\beta J} + 1}$ を用いました。式 (2) と比較すると，$Q(\hat{c}, \hat{b}) = \dfrac{e^{\beta J\,\hat{c}\cdot\hat{b}}}{e^{\beta J} + 1}$ です。したがって，

$$
\finalanswer{Q(\hat{x}, \hat{x}) = Q(\hat{y}, \hat{y}) = \frac{e^{\beta J}}{e^{\beta J} + 1},\qquad Q(\hat{x}, \hat{y}) = Q(\hat{y}, \hat{x}) = \frac{1}{e^{\beta J} + 1}}
$$

### (7)
行列 $P_L = \begin{pmatrix} P_L(\hat{x}, \hat{x}) & P_L(\hat{x}, \hat{y}) \\ P_L(\hat{y}, \hat{x}) & P_L(\hat{y}, \hat{y}) \end{pmatrix}$，$Q = \begin{pmatrix} Q(\hat{x}, \hat{x}) & Q(\hat{x}, \hat{y}) \\ Q(\hat{y}, \hat{x}) & Q(\hat{y}, \hat{y}) \end{pmatrix}$ とおきます。問1より $L = 2$ の同時確率行列は

$$
\begin{aligned}
P_2 &= \frac{1}{2\left(e^{\beta J} + 1\right)}\begin{pmatrix} e^{\beta J} & 1 \\ 1 & e^{\beta J} \end{pmatrix} \\
&= \frac{1}{2} Q
\end{aligned}
$$

なので，式 (2) を繰り返し用いると $P_L = P_2 Q^{L - 2} = \dfrac{1}{2} Q^{L - 1}$ となります。

実対称行列 $Q$ の固有値を求めます。

$$
\begin{aligned}
\lambda_+ &= Q(\hat{x}, \hat{x}) + Q(\hat{x}, \hat{y}) \\
&= 1 \\
\lambda_- &= Q(\hat{x}, \hat{x}) - Q(\hat{x}, \hat{y}) \\
&= \frac{e^{\beta J} - 1}{e^{\beta J} + 1} \\
&= \tanh\left(\frac{\beta J}{2}\right)
\end{aligned}
$$

内積の期待値 $\langle \mathbf{S}_1 \cdot \mathbf{S}_L \rangle$ は，$\hat{x}\cdot\hat{x}=1$，$\hat{y}\cdot\hat{y}=1$，$\hat{x}\cdot\hat{y}=0$ より $P_L$ のトレースに等しくなります。

$$
\begin{aligned}
\langle \mathbf{S}_1 \cdot \mathbf{S}_L \rangle &= P_L(\hat{x}, \hat{x}) + P_L(\hat{y}, \hat{y}) \\
&= \operatorname{Tr}(P_L) \\
&= \frac{1}{2}\operatorname{Tr}\left(Q^{L - 1}\right) \\
&= \frac{1}{2}\left(\lambda_+^{L - 1} + \lambda_-^{L - 1}\right) \\
&= \frac{1}{2} + \frac{1}{2}\left(\frac{e^{\beta J} - 1}{e^{\beta J} + 1}\right)^{L - 1} \\
&= \frac{1}{2} + \frac{1}{2}\left[\tanh\left(\frac{\beta J}{2}\right)\right]^{L - 1}
\end{aligned}
$$

式 (3) と比較すると，$A = \dfrac{1}{2},\ B = \dfrac{1}{2}$ であり，$J > 0$ より $0 < \tanh\left(\dfrac{\beta J}{2}\right) < 1$ なので，相関長 $\xi$ は次のように表されます。

$$
\begin{aligned}
\xi &= -\frac{1}{\ln\tanh\left(\dfrac{\beta J}{2}\right)} \\
&= \frac{1}{\ln\left(\dfrac{e^{\beta J} + 1}{e^{\beta J} - 1}\right)}
\end{aligned}
$$

まず，$\beta J \ll 1$ の高温を考えます。$\tanh\left(\dfrac{\beta J}{2}\right) \simeq \dfrac{\beta J}{2}$ なので，相関長は次のようになります。

$$
\begin{aligned}
\xi &\simeq -\frac{1}{\ln\left(\dfrac{\beta J}{2}\right)} \\
&= \frac{1}{\ln\left(\dfrac{2}{\beta J}\right)}
\end{aligned}
$$

次に，$\beta J \gg 1$ の低温を考えます。$e^{-\beta J}$ の1次まで展開します。

$$
\begin{aligned}
\dfrac{e^{\beta J} + 1}{e^{\beta J} - 1} &= \dfrac{1 + e^{-\beta J}}{1 - e^{-\beta J}} \\
&\simeq 1 + 2e^{-\beta J}
\end{aligned}
$$

より $\ln\left(\dfrac{e^{\beta J} + 1}{e^{\beta J} - 1}\right) \simeq 2e^{-\beta J}$ なので，

$$
\xi \simeq \frac{1}{2}e^{\beta J}
$$

したがって，高温極限および低温極限の相関長をそれぞれ $\xi_{\mathrm{high}},\ \xi_{\mathrm{low}}$ とすると，

$$
\finalanswer{\langle \mathbf{S}_1 \cdot \mathbf{S}_L \rangle = \frac{1}{2} + \frac{1}{2}\left(\frac{e^{\beta J} - 1}{e^{\beta J} + 1}\right)^{L - 1},\qquad \xi_{\mathrm{high}} \simeq \frac{1}{\ln\left(\dfrac{2}{\beta J}\right)},\qquad \xi_{\mathrm{low}} \simeq \frac{1}{2}e^{\beta J}}
$$

<aside class="rigor-note" markdown>
有限の温度では $0<\tanh(\beta J/2)<1$ なので，$L\to\infty$ で相関は $1/2$ に近づきます。無相関の平均値を確認すると，

$$
\begin{aligned}
\langle\boldsymbol S_1\rangle\cdot\langle\boldsymbol S_L\rangle
&=\frac{\hat x+\hat y}{2}\cdot\frac{\hat x+\hat y}{2}\\
&=\frac12
\end{aligned}
$$

です。距離とともに0へ減衰するのは，この定数を引いた相関です。
</aside>
