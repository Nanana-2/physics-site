---
title: 東大理物 平成24年度 物理学 第2問：2原子分子の回転分配関数とオルソ・パラ水素
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成24年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成24年度 物理学 第2問：2原子分子の回転分配関数とオルソ・パラ水素

## 問題

原子 2 個からなる分子の回転について以下の設問に答えよ。原子間隔は一定とする。分配関数，比熱，内部エネルギーは全て 1 分子あたりの量とする。Boltzmann 定数を $k_{\mathrm{B}}$ とし，記号 $\beta = 1 / (k_{\mathrm{B}} T)$ を用いてよい。

(1) まず 2 原子分子を下図の様な剛体回転子として古典的に扱う。下図で $\theta, \varphi$ は 2 原子分子の向きを極座標表示した際の極角と方位角である。これらに共役な正準運動量を $p_\theta, p_\varphi$ とし，回転子の中心に対する慣性モーメントを $I$ とすると，回転のエネルギー $E$ は以下で与えられる。

$$
E = \frac{1}{2I}\left(p_\theta^2 + \frac{p_\varphi^2}{\sin^2\theta}\right)
$$

温度 $T$ における回転運動の分配関数 $Z$ を求めよ。計算の過程も示すこと。また比熱への回転運動の寄与 $C$ を求めよ。

<figure class="problem-figure" markdown>
![2原子分子の向きを表す極角thetaと方位角phi](../../../docs/assets/figures/pastexam-todai-ributsu/H24_butsuri_2-p-light.svg#only-light)
![2原子分子の向きを表す極角thetaと方位角phi](../../../docs/assets/figures/pastexam-todai-ributsu/H24_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">剛体回転子としての 2 原子分子の向き $(\theta, \varphi)$。</figcaption>
</figure>

(2) 次に量子論的に扱うと，エネルギー準位は以下で与えられる。

$$
E_\ell = \frac{\hbar^2}{2I}\ell(\ell + 1) \qquad (\ell = 0, 1, 2, \dots) \tag{1}
$$

ただし $\hbar = (\text{Planck 定数}) / (2\pi)$ である。$E_\ell$ の縮退度 $(2\ell + 1)$ に注意して，温度 $T$ における回転運動の分配関数 $Z$ を表す式を与えよ。また，十分高温では $Z$ が積分で近似できるとし，比熱への回転運動の寄与 $C$ を求めよ。設問 1 の $C$ の結果との関係を述べよ。

(3) 十分低温での回転運動の比熱 $C$ を温度 $T$ の関数として近似的に求めよ。

具体的な 2 原子分子として水素分子を考えよう。水素原子核には核スピンがあり，水素分子にはオルソ水素とパラ水素という核スピン異性体が存在する。二つの水素原子核の合成スピンの大きさは，オルソ水素では $1$，パラ水素では $0$ である。また軌道部分の波動関数は，二つの水素原子核の入れ換えに関して式 (1) の $\ell$ が偶数のとき対称，奇数のとき反対称である。
{: .problem-lead }

(4) オルソ水素とパラ水素の回転エネルギー準位として，式 (1) の $E_\ell$ でどのような $\ell$ の値が許されるか，理由と共に答えよ。

(5) 十分高温の水素ガスにおけるオルソ水素分子の数 $N_{\mathrm{o}}$ とパラ水素分子の数 $N_{\mathrm{p}}$ の存在比 $N_{\mathrm{o}} / N_{\mathrm{p}}$ はいくらか，理由と共に答えよ。

(6) 水素分子の場合，慣性モーメント $I$ は

$$
\frac{\hbar^2}{2I} = k_{\mathrm{B}}\Theta, \qquad \Theta \simeq 90\ \mathrm{K}
$$

で与えられる。十分高温で熱平衡にある水素ガスを急冷して $30\ \mathrm{K}$ にした。オルソ成分とパラ成分の間の遷移は遅いので，しばらくは設問 5 の存在比が保たれる。この状況での平均の内部エネルギーに対する回転運動の寄与を $U$ とするとき，$U / k_{\mathrm{B}}$ を有効数字 2 桁で求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成24年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2 原子分子の回転は自由度 $2$ の系なので，古典的な分配関数では運動量 $p_\theta, p_\varphi$ に関する 2 回のガウス積分から $Z \propto T$ が得られ，等分配則に従う比熱 $C = k_{\mathrm{B}}$ が出ます。量子論では高温側で和を積分に置き換えると古典結果に一致し，低温側では基底状態と第 1 励起状態の 2 準位近似で指数関数的に減少します。

水素分子では 2 つの陽子がフェルミ粒子なので，全波動関数の反対称性から核スピンの対称性と回転量子数 $\ell$ の偶奇が結びつきます。急冷後はオルソ水素とパラ水素がそれぞれ独立に最低準位へ落ちるため，オルソ成分には $\ell = 1$ の回転エネルギーが残ります。
</div>

### (1)
2 自由度の位相空間 $(\theta, \varphi, p_\theta, p_\varphi)$ 上の積分を $h^2$ で割って古典分配関数 $Z$ を計算します。

$$
\begin{aligned}
Z &= \frac{1}{h^2}\int_0^{\pi}\mathrm{d}\theta \int_0^{2\pi}\mathrm{d}\varphi \int_{-\infty}^{\infty}\mathrm{d}p_\theta \int_{-\infty}^{\infty}\mathrm{d}p_\varphi \exp\!\left[-\frac{\beta}{2I}\left(p_\theta^2 + \frac{p_\varphi^2}{\sin^2\theta}\right)\right] \\
&= \frac{1}{h^2}\int_0^{\pi}\mathrm{d}\theta \int_0^{2\pi}\mathrm{d}\varphi \left(\sqrt{\frac{2\pi I}{\beta}}\right)\left(\sqrt{\frac{2\pi I}{\beta}}\,\sin\theta\right) \\
&= \frac{2\pi I}{\beta h^2}\int_0^{2\pi}\mathrm{d}\varphi \int_0^{\pi}\sin\theta\,\mathrm{d}\theta \\
&= \frac{2\pi I}{\beta h^2}\cdot 2\pi \cdot 2 \\
&= \frac{8\pi^2 I k_{\mathrm{B}} T}{h^2} \\
&= \frac{2I k_{\mathrm{B}} T}{\hbar^2}
\end{aligned}
$$

1 分子あたりの内部エネルギー $U$ と比熱 $C$ を求めます。

$$
\begin{aligned}
U &= -\frac{\partial \ln Z}{\partial \beta} \\
&= -\frac{\partial}{\partial \beta}\ln\!\left(\frac{2I}{\beta\hbar^2}\right) \\
&= \frac{1}{\beta} \\
&= k_{\mathrm{B}} T
\end{aligned}
$$

$$
\begin{aligned}
C &= \frac{\partial U}{\partial T} \\
&= k_{\mathrm{B}}
\end{aligned}
$$

$$
\finalanswer{Z = \frac{8\pi^2 I k_{\mathrm{B}} T}{h^2} = \frac{2I k_{\mathrm{B}} T}{\hbar^2}, \qquad C = k_{\mathrm{B}}}
$$

### (2)
各エネルギー準位 $E_\ell = \dfrac{\hbar^2}{2I}\ell(\ell + 1)$ の縮退度が $2\ell + 1$ なので，量子論での分配関数 $Z$ は次式で与えられます。

$$
Z = \sum_{\ell=0}^{\infty} (2\ell + 1)\exp\!\left[-\frac{\beta\hbar^2}{2I}\ell(\ell + 1)\right]
$$

十分高温で $\dfrac{\beta\hbar^2}{2I} \ll 1$ のとき，和を $\ell = 0$ から $\infty$ までの積分で近似します。$u = \ell(\ell + 1)$ とおくと $\mathrm{d}u = (2\ell + 1)\,\mathrm{d}\ell$ なので，積分は次のように計算することができます。

$$
\begin{aligned}
Z &\simeq \int_0^{\infty} (2\ell + 1)\exp\!\left[-\frac{\beta\hbar^2}{2I}\ell(\ell + 1)\right]\mathrm{d}\ell \\
&= \int_0^{\infty} \exp\!\left(-\frac{\beta\hbar^2}{2I}u\right)\mathrm{d}u \\
&= \frac{2I}{\beta\hbar^2} \\
&= \frac{2I k_{\mathrm{B}} T}{\hbar^2}
\end{aligned}
$$

したがって高温極限の分配関数は設問 1 の古典的な分配関数に一致し，比熱への寄与も $C = k_{\mathrm{B}}$ となって設問 1 の結果と一致します。

$$
\finalanswer{Z = \sum_{\ell=0}^{\infty} (2\ell + 1)\exp\!\left[-\frac{\beta\hbar^2}{2I}\ell(\ell + 1)\right], \qquad C = k_{\mathrm{B}}}
$$

### (3)
十分低温で $\dfrac{\beta\hbar^2}{2I} \gg 1$ のとき，分配関数 $Z$ の和は基底状態 $\ell = 0$ と第 1 励起状態 $\ell = 1$ の 2 項で近似することができます。$E_0 = 0$，$E_1 = \dfrac{\hbar^2}{I}$ であり，縮退度はそれぞれ $1$ と $3$ です。

$$
Z \simeq 1 + 3\exp\!\left(-\frac{\beta\hbar^2}{I}\right)
$$

内部エネルギー $U$ を求め，$e^{-\beta\hbar^2 / I} \ll 1$ を用いて主要項を残します。

$$
\begin{aligned}
U &= -\frac{\partial \ln Z}{\partial \beta} \\
&\simeq \frac{3\dfrac{\hbar^2}{I}\exp\!\left(-\dfrac{\beta\hbar^2}{I}\right)}{1 + 3\exp\!\left(-\dfrac{\beta\hbar^2}{I}\right)} \\
&\simeq 3\frac{\hbar^2}{I}\exp\!\left(-\frac{\hbar^2}{I k_{\mathrm{B}} T}\right)
\end{aligned}
$$

これを温度 $T$ で微分して低温の比熱 $C$ を求めます。

$$
\begin{aligned}
C &= \frac{\partial U}{\partial T} \\
&\simeq 3\frac{\hbar^2}{I}\cdot\frac{\hbar^2}{I k_{\mathrm{B}} T^2}\exp\!\left(-\frac{\hbar^2}{I k_{\mathrm{B}} T}\right) \\
&= 3 k_{\mathrm{B}}\left(\frac{\hbar^2}{I k_{\mathrm{B}} T}\right)^2 \exp\!\left(-\frac{\hbar^2}{I k_{\mathrm{B}} T}\right)
\end{aligned}
$$

$$
\finalanswer{C \simeq 3 k_{\mathrm{B}}\left(\frac{\hbar^2}{I k_{\mathrm{B}} T}\right)^2 \exp\!\left(-\frac{\hbar^2}{I k_{\mathrm{B}} T}\right)}
$$

### (4)
水素原子核である陽子はスピン $1/2$ のフェルミ粒子なので，2 つの陽子の入れ換えに対して核の全波動関数は反対称でなければなりません。全波動関数は核スピン部分の波動関数と回転の軌道部分の波動関数の積で表されます。

- オルソ水素は合成核スピン $S = 1$ の三重項状態であり，核スピン部分は陽子の入れ換えに対して対称です。したがって軌道部分は反対称である必要があり，$\ell$ は**奇数**（$\ell = 1, 3, 5, \dots$）のみが許されます。
- パラ水素は合成核スピン $S = 0$ の一重項状態であり，核スピン部分は陽子の入れ換えに対して反対称です。したがって軌道部分は対称である必要があり，$\ell$ は**偶数**（$\ell = 0, 2, 4, \dots$）のみが許されます。

### (5)
オルソ水素の核スピン状態の縮退度は $2S + 1 = 3$，パラ水素の核スピン状態の縮退度は $2S + 1 = 1$ です。それぞれの分配関数 $Z_{\mathrm{o}}, Z_{\mathrm{p}}$ は次式で与えられます。

$$
\begin{aligned}
Z_{\mathrm{o}} &= 3\sum_{\ell = 1, 3, 5, \dots} (2\ell + 1)\exp\!\left[-\frac{\beta\hbar^2}{2I}\ell(\ell + 1)\right] \\
Z_{\mathrm{p}} &= \sum_{\ell = 0, 2, 4, \dots} (2\ell + 1)\exp\!\left[-\frac{\beta\hbar^2}{2I}\ell(\ell + 1)\right]
\end{aligned}
$$

十分高温では，奇数 $\ell$ についての和と偶数 $\ell$ についての和は，いずれもすべての $\ell$ についての和のちょうど半分に近づきます。

$$
\sum_{\ell = 1, 3, 5, \dots} (2\ell + 1) e^{-\beta E_\ell} \simeq \sum_{\ell = 0, 2, 4, \dots} (2\ell + 1) e^{-\beta E_\ell} \simeq \frac{I k_{\mathrm{B}} T}{\hbar^2}
$$

存在比 $N_{\mathrm{o}} / N_{\mathrm{p}}$ は分配関数の比 $Z_{\mathrm{o}} / Z_{\mathrm{p}}$ に等しいので，核スピンの縮退度の比そのままになります。

$$
\finalanswer{\frac{N_{\mathrm{o}}}{N_{\mathrm{p}}} = 3}
$$

### (6)
急冷後の温度は $T = 30\ \mathrm{K}$ であり，$\Theta \simeq 90\ \mathrm{K}$ なので $\dfrac{\Theta}{T} = 3$ です。各準位のエネルギーは $\beta E_\ell = \dfrac{\Theta}{T}\ell(\ell + 1) = 3\ell(\ell + 1)$ です。

- パラ水素は $\ell = 0, 2, 4, \dots$ の準位をとります。$\ell = 0$ のエネルギーは $E_0 = 0$，次の $\ell = 2$ は $\beta E_2 = 3 \times 6 = 18$ なので，ボルツマン因子は $e^{-18} \approx 1.5 \times 10^{-8}$ です。したがって $30\ \mathrm{K}$ ではパラ水素は実質的にすべて $\ell = 0$ にあり，1 分子あたりの内部エネルギーは $U_{\mathrm{p}} / k_{\mathrm{B}} \simeq 0\ \mathrm{K}$ です。
- オルソ水素は $\ell = 1, 3, 5, \dots$ の準位をとります。最低準位 $\ell = 1$ のエネルギーは $E_1 / k_{\mathrm{B}} = 2\Theta = 180\ \mathrm{K}$ であり，次の $\ell = 3$ とのエネルギー差は $\beta(E_3 - E_1) = 3 \times (12 - 2) = 30$ なので，相対的なボルツマン因子は $e^{-30} \approx 9.4 \times 10^{-14}$ です。したがって $30\ \mathrm{K}$ ではオルソ水素は実質的にすべて $\ell = 1$ にあり，1 分子あたりの内部エネルギーは $U_{\mathrm{o}} / k_{\mathrm{B}} \simeq 180\ \mathrm{K}$ です。

急冷後も存在比 $N_{\mathrm{o}} : N_{\mathrm{p}} = 3 : 1$ が保たれているので，オルソ水素の割合は $3/4$，パラ水素の割合は $1/4$ です。平均の内部エネルギーに対する回転運動の寄与 $U / k_{\mathrm{B}}$ を計算します。

$$
\begin{aligned}
\frac{U}{k_{\mathrm{B}}} &= \frac{3}{4}\frac{U_{\mathrm{o}}}{k_{\mathrm{B}}} + \frac{1}{4}\frac{U_{\mathrm{p}}}{k_{\mathrm{B}}} \\
&\simeq \frac{3}{4} \times 180\ \mathrm{K} + \frac{1}{4} \times 0\ \mathrm{K} \\
&= 135\ \mathrm{K}
\end{aligned}
$$

有効数字 2 桁で表すと次のとおりです。

$$
\finalanswer{\frac{U}{k_{\mathrm{B}}} \simeq 1.4 \times 10^2\ \mathrm{K}}
$$

<aside class="rigor-note" markdown>
設問 1 では 2 個の原子の区別を意識せず位相空間全体を積分しました。同種 2 原子分子を古典的に扱う場合は回転の対称性因子 $1/2$ が分配関数に掛かりますが，対数の微分で定数因子が落ちるため内部エネルギー $U$ と比熱 $C$ は変わりません。
</aside>
