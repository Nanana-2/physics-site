---
title: 東大理物 平成23年度 物理学 第2問：3スピン三角形モデルの磁化と比熱
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
  - 物性物理学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成23年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成23年度 物理学 第2問：3スピン三角形モデルの磁化と比熱

## 問題

温度 $T$ の熱浴中にあるスピン系に，外部から $z$ 方向に磁場 $\boldsymbol{H} = (0, 0, H)$ がかけられている。このスピン系は大きさが $S$ の3個の量子スピン $\boldsymbol{S}_1, \boldsymbol{S}_2, \boldsymbol{S}_3$ を3角形の3つの頂点に配置したもの（図参照）で構成されている。この系のハミルトニアン $\mathcal{H}$ は，$\mu$ をスピンの磁気モーメントとして，次のように与えられるとする。

$$
\mathcal{H} = -J\boldsymbol{S}_1 \cdot \boldsymbol{S}_2 - J'\boldsymbol{S}_2 \cdot \boldsymbol{S}_3 - J'\boldsymbol{S}_3 \cdot \boldsymbol{S}_1 - \mu\boldsymbol{H}\cdot(\boldsymbol{S}_1 + \boldsymbol{S}_2 + \boldsymbol{S}_3)
$$

<figure class="problem-figure" markdown>
![三角形の3頂点に配置された3個の量子スピンと交換相互作用J, J'](../../../docs/assets/figures/pastexam-todai-ributsu/H23_butsuri_2-p-light.svg#only-light)
![三角形の3頂点に配置された3個の量子スピンと交換相互作用J, J'](../../../docs/assets/figures/pastexam-todai-ributsu/H23_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">三角形の3頂点に配置された量子スピン $1, 2, 3$ と相互作用 $J, J'$。</figcaption>
</figure>

まず，$J = J' = 0$ の場合について，以下の設問に答えよ。
{: .problem-lead }

(1) この系の分配関数 $Z$ を求めよ。ただし，ボルツマン定数を $k_{\mathrm{B}}$ とし，$\beta = 1/(k_{\mathrm{B}} T)$ という記法を用いてもよい。

(2) $z$ 方向の磁化 $M$ を求めよ。解答は

$$
B_S(x) = \frac{2S + 1}{2S}\coth\!\left(\frac{2S + 1}{2S} x\right) - \frac{1}{2S}\coth\!\left(\frac{1}{2S} x\right)
$$

で定義されるブリユアン関数 $B_S(x)$ を用いて表せ。また，$\chi \equiv \lim_{H \to 0}(M / H)$ で定義される帯磁率 $\chi$ を求めよ。なお，$\coth(y) = (e^y + e^{-y})/(e^y - e^{-y})$ であり，また，$x$ が小さい時，

$$
B_S(x) \approx \frac{S + 1}{3S} x
$$

であることに注意せよ。

(3) 全系の比熱 $C_v$ を求めよ。解答は $B_S'(x)$（$\equiv \dfrac{\mathrm{d}B_S(x)}{\mathrm{d}x}$）を用いて表せ。さらに，高温極限（$k_{\mathrm{B}} T \gg \mu H$）での $C_v$ を求めよ。

次に，$S = 1/2$，かつ，$J \neq 0, J' = 0$ の場合について，以下の設問に答えよ。

(4) まず，$H = 0$ の場合に，全系のエネルギー固有値とその縮重度を求めよ。さらに，それを参考にして $H \neq 0$ の場合の分配関数 $Z$ を求めよ。

(5) $J$ の正負に注意しながら，$k_{\mathrm{B}} T \ll |J|$ における $z$ 方向の磁化 $M$ を求めよ。解答はブリユアン関数（$B_{1/2}, B_1$ など）を用いて表せ。

最後に，$S = 1/2$，かつ，$J = J' \neq 0$ の場合について，次の設問に答えよ。

(6) まず，$H = 0$ の場合に，全系のエネルギー固有値とその縮重度を求めよ。さらに，それを参考にして，$H \neq 0$ の場合の $k_{\mathrm{B}} T \ll |J|$ における $z$ 方向の磁化 $M$ を求めよ。解答は $J$ の正負に注意して，ブリユアン関数を用いて表せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成23年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
相互作用がないとき，3個のスピンは独立です。そのため，全系の分配関数は1個のスピンの分配関数の3乗になります。1個のスピンの分配関数は，$S_z=-S,\dots,S$ についての等比級数の和として求めます。

交換相互作用 $\boldsymbol{S}_1\cdot\boldsymbol{S}_2$ は，合成スピン $\boldsymbol{S}_{12}=\boldsymbol{S}_1+\boldsymbol{S}_2$ を使うと $\boldsymbol{S}_{12}^2$ と定数で書くことができます。そのため，エネルギー固有値は合成スピンの大きさごとに求めることができます。$J=J'$ のときは，3個のスピンの全スピンで同じように書き直します。

ゼーマン項は全スピンの $z$ 成分に比例するので，合成スピンの大きさを決めた状態の中で磁場の分配関数を作ることができます。$k_{\mathrm{B}}T\ll|J|$ では，ボルツマン因子が大きいのはエネルギーの低い合成スピンの状態だけです。$J$ の符号でどちらの状態が低いかが変わるので，符号ごとにその状態だけを残します。
</div>

### (1)
$J = J' = 0$ のとき，ハミルトニアンは $\mathcal{H} = -\mu H(S_{1z} + S_{2z} + S_{3z})$ であり，3個のスピンは互いに独立です。1個のスピンに対する分配関数 $Z_1$ を等比級数の和として計算します。$S_z$ の固有値は $m = -S, -S + 1, \dots, S$ の $2S + 1$ 個です。

$$
\begin{aligned}
Z_1 &= \sum_{m = -S}^{S} e^{\beta\mu H m} \\
&= e^{-\beta\mu H S}\,\frac{1 - e^{(2S + 1)\beta\mu H}}{1 - e^{\beta\mu H}} \\
&= \frac{e^{\frac{2S + 1}{2}\beta\mu H} - e^{-\frac{2S + 1}{2}\beta\mu H}}{e^{\frac{1}{2}\beta\mu H} - e^{-\frac{1}{2}\beta\mu H}} \\
&= \frac{\sinh\!\left(\dfrac{2S + 1}{2}\beta\mu H\right)}{\sinh\!\left(\dfrac{1}{2}\beta\mu H\right)}
\end{aligned}
$$

全系の分配関数 $Z$ は $Z_1^3$ で与えられます。

$$
\finalanswer{Z = \left[\frac{\sinh\!\left(\dfrac{2S + 1}{2}\beta\mu H\right)}{\sinh\!\left(\dfrac{1}{2}\beta\mu H\right)}\right]^3}
$$

### (2)
$z$ 方向の磁化 $M$ は $M = \dfrac{1}{\beta}\dfrac{\partial \ln Z}{\partial H}$ で与えられます。設問1の結果を代入して微分します。

$$
\begin{aligned}
M &= \frac{3}{\beta}\frac{\partial}{\partial H}\left[\ln\sinh\!\left(\frac{2S + 1}{2}\beta\mu H\right) - \ln\sinh\!\left(\frac{1}{2}\beta\mu H\right)\right] \\
&= 3\mu\left[\frac{2S + 1}{2}\coth\!\left(\frac{2S + 1}{2}\beta\mu H\right) - \frac{1}{2}\coth\!\left(\frac{1}{2}\beta\mu H\right)\right] \\
&= 3\mu S\left[\frac{2S + 1}{2S}\coth\!\left(\frac{2S + 1}{2S}\beta\mu S H\right) - \frac{1}{2S}\coth\!\left(\frac{1}{2S}\beta\mu S H\right)\right] \\
&= 3\mu S B_S(\beta\mu S H)
\end{aligned}
$$

次に $H \to 0$ の極限で $x = \beta\mu S H \to 0$ となるので，与えられた近似式 $B_S(x) \approx \dfrac{S + 1}{3S} x$ を用いて帯磁率 $\chi$ を求めます。

$$
\begin{aligned}
\chi &= \lim_{H \to 0}\frac{M}{H} \\
&= \lim_{H \to 0}\frac{3\mu S}{H}\cdot\frac{S + 1}{3S}\beta\mu S H \\
&= \beta\mu^2 S(S + 1) \\
&= \frac{\mu^2 S(S + 1)}{k_{\mathrm{B}} T}
\end{aligned}
$$

$$
\finalanswer{M = 3\mu S B_S(\beta\mu S H), \qquad \chi = \frac{\mu^2 S(S + 1)}{k_{\mathrm{B}} T}}
$$

### (3)
内部エネルギー $U$ は $U = \langle\mathcal{H}\rangle = -H M$ です。$x = \beta\mu S H = \dfrac{\mu S H}{k_{\mathrm{B}} T}$ とおくと，$U = -3\mu S H B_S(x)$ です。これを磁場一定のもとで温度 $T$ について微分し，比熱 $C_v$ を求めます。

$$
\begin{aligned}
C_v &= \left.\frac{\partial U}{\partial T}\right|_H \\
&= -3\mu S H B_S'(x)\frac{\partial x}{\partial T} \\
&= -3\mu S H B_S'(x)\left(-\frac{\mu S H}{k_{\mathrm{B}} T^2}\right) \\
&= 3 k_{\mathrm{B}} (\beta\mu S H)^2 B_S'(\beta\mu S H)
\end{aligned}
$$

高温極限 $k_{\mathrm{B}} T \gg \mu H$ では $x \ll 1$ であり，$B_S(x) \approx \dfrac{S + 1}{3S} x$ より $B_S'(x) \approx \dfrac{S + 1}{3S}$ となります。これを代入して高温極限の $C_v$ を求めます。

$$
\begin{aligned}
C_v &\approx 3 k_{\mathrm{B}}\left(\frac{\mu S H}{k_{\mathrm{B}} T}\right)^2 \frac{S + 1}{3S} \\
&= \frac{S(S + 1)\mu^2 H^2}{k_{\mathrm{B}} T^2}
\end{aligned}
$$

$$
\finalanswer{C_v = 3 k_{\mathrm{B}}(\beta\mu S H)^2 B_S'(\beta\mu S H), \qquad C_v \approx \frac{S(S + 1)\mu^2 H^2}{k_{\mathrm{B}} T^2}}
$$

### (4)
$S = 1/2$，$J \neq 0, J' = 0$ のとき，合成スピン $\boldsymbol{S}_{12} = \boldsymbol{S}_1 + \boldsymbol{S}_2$ を導入します。$\boldsymbol{S}_1^2 = \boldsymbol{S}_2^2 = \dfrac{3}{4}$ より，

$$
\begin{aligned}
\boldsymbol{S}_1 \cdot \boldsymbol{S}_2 &= \frac{1}{2}\left(\boldsymbol{S}_{12}^2 - \boldsymbol{S}_1^2 - \boldsymbol{S}_2^2\right) \\
&= \frac{1}{2}\left[S_{12}(S_{12} + 1) - \frac{3}{2}\right]
\end{aligned}
$$

となります。合成スピンの大きさは $S_{12} = 1$ と $S_{12} = 0$ の2通りであり，スピン3は相互作用しないため縮重度 $2$ をもちます。したがって $H = 0$ のエネルギー固有値と縮重度は次の2つです。

- $S_{12} = 1$ のとき：$E = -\dfrac{J}{4}$，縮重度は $3 \times 2 = 6$。
- $S_{12} = 0$ のとき：$E = \dfrac{3J}{4}$，縮重度は $1 \times 2 = 2$。

$H \neq 0$ のとき，ハミルトニアンは $\mathcal{H} = -J\boldsymbol{S}_1\cdot\boldsymbol{S}_2 - \mu H S_{12z} - \mu H S_{3z}$ と2つの独立な部分に分かれます。$S_{12} = 1$ では $S_{12z} = -1, 0, 1$，$S_{12} = 0$ では $S_{12z} = 0$ なので，対 $(1, 2)$ とスピン3の分配関数の積として全系の分配関数 $Z$ が求まります。

$$
\begin{aligned}
Z &= \left[e^{\frac{\beta J}{4}}\left(e^{\beta\mu H} + 1 + e^{-\beta\mu H}\right) + e^{-\frac{3\beta J}{4}}\right]\left(e^{\frac{\beta\mu H}{2}} + e^{-\frac{\beta\mu H}{2}}\right) \\
&= 2\cosh\!\left(\frac{\beta\mu H}{2}\right)\left[e^{\frac{\beta J}{4}}\bigl(1 + 2\cosh(\beta\mu H)\bigr) + e^{-\frac{3\beta J}{4}}\right]
\end{aligned}
$$

$$
\finalanswer{Z = 2\cosh\!\left(\frac{\beta\mu H}{2}\right)\left[e^{\frac{\beta J}{4}}\bigl(1 + 2\cosh(\beta\mu H)\bigr) + e^{-\frac{3\beta J}{4}}\right]}
$$

### (5)
設問4の $Z$ の対数をとり，$k_{\mathrm{B}} T \ll |J|$ すなわち $\beta|J| \gg 1$ のもとで $J$ の符号ごとに計算します。

$J > 0$ のとき，$e^{-3\beta J/4}$ は $e^{\beta J/4}$ の $e^{-\beta J} \ll 1$ 倍なので，無視することができます。$1 + 2\cosh(\beta\mu H)$ を $\sinh$ の比で書き直すと，分配関数は大きさ $1$ のスピンと大きさ $1/2$ のスピンの分配関数の積になります。

$$
\begin{aligned}
Z &\simeq 2\cosh\!\left(\frac{\beta\mu H}{2}\right)\cdot e^{\frac{\beta J}{4}}\bigl(1 + 2\cosh(\beta\mu H)\bigr) \\
&= 2\cosh\!\left(\frac{\beta\mu H}{2}\right)\cdot e^{\frac{\beta J}{4}}\frac{\sinh\!\left(\dfrac{3}{2}\beta\mu H\right)}{\sinh\!\left(\dfrac{1}{2}\beta\mu H\right)}
\end{aligned}
$$

磁化は，2つのスピンの磁化の和になります。設問2から，大きさ $S$ のスピン1個の磁化は $\mu S B_S(\beta\mu S H)$ です。$S = 1$ と $S = 1/2$ の磁化を足すと，次のようになります。

$$
M \simeq \mu B_1(\beta\mu H) + \frac{1}{2}\mu B_{1/2}\!\left(\frac{1}{2}\beta\mu H\right)
$$

$J < 0$ のとき，$e^{\beta J/4}$ は $e^{-3\beta J/4}$ の $e^{-\beta|J|} \ll 1$ 倍なので，無視することができます。対 $(1, 2)$ は $S_{12} = 0$ の状態に限られ，磁化にはスピン3だけが寄与します。

$$
\begin{aligned}
Z &\simeq 2\cosh\!\left(\frac{\beta\mu H}{2}\right)\,e^{-\frac{3\beta J}{4}} \\
M &\simeq \frac{1}{2}\mu B_{1/2}\!\left(\frac{1}{2}\beta\mu H\right)
\end{aligned}
$$

$$
\finalanswer{M \simeq \mu B_1(\beta\mu H) + \frac{1}{2}\mu B_{1/2}\!\left(\frac{\beta\mu H}{2}\right) \quad (J > 0), \qquad M \simeq \frac{1}{2}\mu B_{1/2}\!\left(\frac{\beta\mu H}{2}\right) \quad (J < 0)}
$$

### (6)
$J = J' \neq 0$ のとき，全スピン $\boldsymbol{S}_{\mathrm{tot}} = \boldsymbol{S}_1 + \boldsymbol{S}_2 + \boldsymbol{S}_3$ を導入します。$\boldsymbol{S}_1^2 = \boldsymbol{S}_2^2 = \boldsymbol{S}_3^2 = \dfrac{3}{4}$ より，交換相互作用の和は次のように書かれます。

$$
\begin{aligned}
\boldsymbol{S}_1\cdot\boldsymbol{S}_2 + \boldsymbol{S}_2\cdot\boldsymbol{S}_3 + \boldsymbol{S}_3\cdot\boldsymbol{S}_1 &= \frac{1}{2}\left(\boldsymbol{S}_{\mathrm{tot}}^2 - \boldsymbol{S}_1^2 - \boldsymbol{S}_2^2 - \boldsymbol{S}_3^2\right) \\
&= \frac{1}{2}\left[S_{\mathrm{tot}}(S_{\mathrm{tot}} + 1) - \frac{9}{4}\right]
\end{aligned}
$$

3個の $S = 1/2$ スピンを合成すると，全状態数 $2^3 = 8$ は $S_{\mathrm{tot}} = 3/2$ が1組と $S_{\mathrm{tot}} = 1/2$ が2組に分かれます。したがって $H = 0$ のエネルギー固有値と縮重度は次の2つです。

- $S_{\mathrm{tot}} = 3/2$ のとき：$E = -\dfrac{J}{2}\left(\dfrac{15}{4} - \dfrac{9}{4}\right) = -\dfrac{3J}{4}$，縮重度は $4$。
- $S_{\mathrm{tot}} = 1/2$ のとき：$E = -\dfrac{J}{2}\left(\dfrac{3}{4} - \dfrac{9}{4}\right) = \dfrac{3J}{4}$，縮重度は $2 \times 2 = 4$。

$H \neq 0$ のとき，全系の分配関数は $S_{\mathrm{tot}} = 3/2$ の1組と $S_{\mathrm{tot}} = 1/2$ の2組の和になります。

$$
Z = e^{\frac{3\beta J}{4}}\frac{\sinh(2\beta\mu H)}{\sinh\!\left(\dfrac{1}{2}\beta\mu H\right)} + 2 e^{-\frac{3\beta J}{4}}\cdot 2\cosh\!\left(\frac{1}{2}\beta\mu H\right)
$$

$k_{\mathrm{B}} T \ll |J|$ すなわち $\beta|J| \gg 1$ のもとで $J$ の符号ごとに計算します。

- $J > 0$ のとき：第2項は第1項に比べて $e^{-3\beta J/2} \ll 1$ だけ小さいため無視することができ，系は大きさ $3/2$ の単一スピンとして振る舞います。よって $M \simeq \dfrac{3}{2}\mu B_{3/2}\!\left(\dfrac{3}{2}\beta\mu H\right)$ です。
- $J < 0$ のとき：第1項は第2項に比べて $e^{-3\beta |J|/2} \ll 1$ だけ小さいため無視することができます。分配関数に掛かる縮重度の因子 $2$ は $\ln Z$ の $H$ 微分で消えるため，磁化は大きさ $1/2$ の単一スピンと同じ $M \simeq \dfrac{1}{2}\mu B_{1/2}\!\left(\dfrac{1}{2}\beta\mu H\right)$ になります。

$$
\finalanswer{M \simeq \frac{3}{2}\mu B_{3/2}\!\left(\frac{3\beta\mu H}{2}\right)\quad (J > 0), \qquad M \simeq \frac{1}{2}\mu B_{1/2}\!\left(\frac{\beta\mu H}{2}\right)\quad (J < 0)}
$$
