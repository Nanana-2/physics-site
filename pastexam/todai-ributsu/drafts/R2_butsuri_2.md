---
title: 東大理物 令和2年度 物理学 第2問：古典理想気体と自由フェルミ気体
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 令和2年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加しています。
---

# 東大理物 令和2年度 物理学 第2問：古典理想気体と自由フェルミ気体

## 問題

体積 $V$，粒子数 $N$ の系が温度 $T$ の熱浴と接触している状況を考える。粒子の質量を $m$ とし，粒子間の相互作用は考えない。必要であれば，熱力学の関係式

$$
\begin{aligned}
dU &= d'Q - PdV + \mu dN, \\
d'Q &= TdS, \qquad (\text{可逆過程の場合}) \\
F &= U - TS,
\end{aligned} \tag{1}
$$

を用いてよい。ここで，$U$ は系の内部エネルギー，$Q$ は熱量，$P$ は圧力，$\mu$ は化学ポテンシャル，$S$ はエントロピー，$F$ はヘルムホルツの自由エネルギーである。

まず粒子を古典的に扱う。この場合，分配関数は

$$
Z = \frac{1}{h^{3N} N!} \int \cdots \int dp_{1x} dp_{1y} dp_{1z} \cdots dp_{Nz} dx_1 dy_1 dz_1 \cdots dz_N \, e^{-\beta H} \tag{2}
$$

で，ハミルトニアン $H$ は

$$
H = \sum_{i=1}^{N} \frac{1}{2m}\left(p_{ix}^2 + p_{iy}^2 + p_{iz}^2\right) \tag{3}
$$

で与えられる。ここで $(p_{ix}, p_{iy}, p_{iz})$ は $i$ 番目の粒子の運動量，$(x_i, y_i, z_i)$ は $i$ 番目の粒子の位置座標，$h$ はプランク定数（$h = 2\pi\hbar$），$\beta = 1/(k_{\mathrm{B}}T)$ で，$k_{\mathrm{B}}$ はボルツマン定数である。

(1) 式 (2) の積分を実行し，$Z(T, V, N)$ を求めよ。さらに，得られた結果を用いて，この系の圧力 $P(T, V, N)$ を求めよ。必要であれば

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{-ax^2} dx &= \sqrt{\frac{\pi}{a}}, \qquad (a > 0) \\
\ln N! &\approx N\ln N - N, \qquad (N\text{ が十分大きい場合})
\end{aligned} \tag{4}
$$

を用いてよい。

(2) 式 (2) には，$1/N!$ という因子がついている。もしこの因子が無かったとすると，ヘルムホルツの自由エネルギーが，ある熱力学的性質を満たさなくなる。このことを簡潔に説明せよ。

(3) この系のエントロピー $S(T, V, N)$ を求めよ。$T \to 0$ としたときに，古典的には $S$ はどうなるか述べよ。

(4) 体積が一定のときの熱容量 $C_V(T, V, N)$ を求めよ。

以下では，粒子がフェルミ粒子であるとして，量子力学的に扱う。系は化学ポテンシャル $\mu$ の粒子浴に接しているとして，グランドカノニカル分布で考える。粒子の運動エネルギーを

$$
\varepsilon_{\boldsymbol{k}} = \frac{\hbar^2}{2m}\left(k_x^2 + k_y^2 + k_z^2\right) \tag{5}
$$

と表す。ここで $\boldsymbol{k} = (k_x, k_y, k_z)$ は粒子の波数を表す。また，体積 $V$ は一辺の長さ $L$ の立方体とし（$V = L^3$），周期境界条件が満たされるものとする。ただし，スピンなどの粒子の内部自由度は考えなくてよい。

(5) この系の大分配関数 $\Xi(T, V, \mu)$ は

$$
\Xi(T, V, \mu) = \prod_{\boldsymbol{k}} \left(1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}\right) \tag{6}
$$

である。この式で，波数 $\boldsymbol{k}$ が取り得る値を求めよ。

(6) 大分配関数を用いて，全粒子数の期待値 $\overline{N}$ が

$$
\overline{N} = \sum_{\boldsymbol{k}} f(\varepsilon_{\boldsymbol{k}}) \tag{7}
$$

となることを示せ。ここで $f(\varepsilon_{\boldsymbol{k}})$ はフェルミ分布関数

$$
f(\varepsilon_{\boldsymbol{k}}) = \frac{1}{e^{\beta(\varepsilon_{\boldsymbol{k}} - \mu)} + 1} \tag{8}
$$

である。

(7) フェルミ粒子系の縮退温度より十分高い温度では，$\mu$ は負で絶対値の大きな値（$|\mu| \gg k_{\mathrm{B}}T$）となる。この場合，フェルミ分布関数は

$$
f(\varepsilon_{\boldsymbol{k}}) \approx e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)} \tag{9}
$$

と近似してよい。このような温度領域で，$L$ が十分大きいとして式 (7) の $\boldsymbol{k}$ の取り得る値についての和を積分の形に書き直して積分を実行し，$\mu$ を $T, V$ と $\overline{N}$（簡単のために $\overline{N} = N$ と書いてよい）の関数として求めよ。

(8) 設問7と同様の温度領域におけるエントロピーが，近似的に $S \approx -\dfrac{\mu}{T}N$ となることを示せ。

(9) 一方，縮退温度より十分低い温度では，この自由フェルミ粒子系の熱容量 $C_V$ は $T$ に比例して $C_V = \gamma T$ と書けることが分かっている。このことと設問8の結果を考慮して，フェルミ粒子系でのエントロピーを温度の関数としてグラフにせよ。比較のために，設問3で考えたエントロピーの温度依存性も点線で書き加えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 令和2年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
古典理想気体の分配関数は運動量と位置の積分に完全に分離され，状態方程式やザックール・テトローデのエントロピーをそのまま与えますが，古典論では $T \to 0$ でエントロピーが $-\infty$ へ発散し熱力学第三法則と矛盾します。

同じ無相互作用系をフェルミ粒子として大分配関数で扱うと，高温極限では化学ポテンシャルを通じて古典結果と一致する一方，低温極限ではパウリの排他原理により $C_V = \gamma T$ から $S = \gamma T \to 0$ となり，古典統計力学の破綻が量子統計によって解消される構造が見えます。
</div>

### (1)
位置座標の積分は各粒子につき体積 $V$ を与え，運動量の各成分の積分はガウス積分公式 (4)（$a = \dfrac{\beta}{2m}$）より $\sqrt{\dfrac{2\pi m}{\beta}} = \sqrt{2\pi m k_{\mathrm{B}} T}$ となります。よって分配関数 $Z(T, V, N)$ は次のようになります。

$$
\begin{aligned}
Z(T, V, N)
&= \frac{1}{h^{3N} N!} V^N \left(\int_{-\infty}^{\infty} e^{-\frac{\beta p^2}{2m}}\,\mathrm{d}p\right)^{3N} \\
&= \frac{V^N}{h^{3N} N!}\left(\sqrt{2\pi m k_{\mathrm{B}} T}\right)^{3N} \\
&= \frac{V^N}{N!}\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right)^{\frac{3N}{2}}
\end{aligned}
$$

ヘルムホルツの自由エネルギー $F = -k_{\mathrm{B}} T \ln Z$ より，圧力 $P = -\left(\dfrac{\partial F}{\partial V}\right)_{T,N}$ を求めます。

$$
\begin{aligned}
P(T, V, N)
&= k_{\mathrm{B}} T \left(\frac{\partial \ln Z}{\partial V}\right)_{T,N} \\
&= k_{\mathrm{B}} T \frac{\partial}{\partial V}(N\ln V) = \frac{N k_{\mathrm{B}} T}{V}
\end{aligned}
$$

したがって，

$$
\finalanswer{Z(T, V, N) = \frac{V^N}{N!}\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right)^{\frac{3N}{2}},\qquad P(T, V, N) = \frac{N k_{\mathrm{B}} T}{V}}
$$

### (2)
$1/N!$ の因子を除いた分配関数を $Z' = N! Z$ とすると，ヘルムホルツの自由エネルギー $F' = -k_{\mathrm{B}} T \ln Z'$ は次のようになります。

$$
F'(T, V, N) = -N k_{\mathrm{B}} T \left[\ln V + \frac{3}{2}\ln\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right)\right]
$$

ここで体積と粒子数をともに $\alpha$ 倍（$V \to \alpha V,\ N \to \alpha N$）すると，

$$
F'(T, \alpha V, \alpha N) = \alpha F'(T, V, N) - \alpha N k_{\mathrm{B}} T \ln\alpha \neq \alpha F'(T, V, N)
$$

となり，自由エネルギーが**示量性**（系の大きさに比例する性質）を満たさなくなります。因子 $1/N!$ は同種粒子の不可弁別性に由来し，自由エネルギーの示量性を保証する役割をもちます。

### (3)
$N$ が十分大きいとしてスターリングの公式 $\ln N! \approx N\ln N - N$ を用いると，自由エネルギーは次のようになります。

$$
\begin{aligned}
F(T, V, N)
&= -k_{\mathrm{B}} T \left[N\ln V - (N\ln N - N) + \frac{3N}{2}\ln\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right)\right] \\
&= -N k_{\mathrm{B}} T \left[\ln\left(\frac{V}{N}\right) + \frac{3}{2}\ln\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right) + 1\right]
\end{aligned}
$$

熱力学関係式 (1) より $\mathrm{d}F = -S\,\mathrm{d}T - P\,\mathrm{d}V + \mu\,\mathrm{d}N$ なので，$S = -\left(\dfrac{\partial F}{\partial T}\right)_{V,N}$ を計算します。

$$
\begin{aligned}
S(T, V, N)
&= N k_{\mathrm{B}}\left[\ln\left(\frac{V}{N}\right) + \frac{3}{2}\ln\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right) + 1\right] + N k_{\mathrm{B}} T \cdot \frac{3}{2T} \\
&= N k_{\mathrm{B}}\left[\ln\left(\frac{V}{N}\right) + \frac{3}{2}\ln\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right) + \frac{5}{2}\right]
\end{aligned}
$$

したがって，

$$
\finalanswer{S(T, V, N) = N k_{\mathrm{B}}\left[\ln\left(\frac{V}{N}\right) + \frac{3}{2}\ln\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right) + \frac{5}{2}\right]}
$$

この式で $T \to 0$ とすると $\ln T \to -\infty$ となるため，古典的には $S \to -\infty$ へ発散し，絶対零度でエントロピーが $0$ に近づくという熱力学第三法則に反します。

### (4)
定積熱容量は $C_V = T\left(\dfrac{\partial S}{\partial T}\right)_{V,N}$ で与えられます。問3の結果を $T$ で偏微分します。

$$
C_V(T, V, N) = T \cdot N k_{\mathrm{B}} \cdot \frac{3}{2T} = \frac{3}{2} N k_{\mathrm{B}}
$$

したがって，

$$
\finalanswer{C_V(T, V, N) = \frac{3}{2} N k_{\mathrm{B}}}
$$

### (5)
一辺の長さ $L$ の立方体における自由粒子の平面波波動関数 $\psi_{\boldsymbol{k}}(\boldsymbol{r}) = \dfrac{1}{\sqrt{V}}e^{i\boldsymbol{k}\cdot\boldsymbol{r}}$ に周期境界条件 $\psi(x + L, y, z) = \psi(x, y, z)$（$y, z$ 方向も同様）を課すと，$e^{i k_x L} = e^{i k_y L} = e^{i k_z L} = 1$ となります。よって各成分は $\dfrac{2\pi}{L}$ の整数倍です。したがって，

$$
\finalanswer{\boldsymbol{k} = \frac{2\pi}{L}(n_x, n_y, n_z) \qquad (n_x, n_y, n_z = 0, \pm 1, \pm 2, \dots)}
$$

### (6)
大分配関数 $\Xi(T, V, \mu)$ の対数をとります。

$$
\ln\Xi(T, V, \mu) = \sum_{\boldsymbol{k}} \ln\left(1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}\right)
$$

全粒子数の期待値 $\overline{N}$ は $\overline{N} = \dfrac{1}{\beta}\left(\dfrac{\partial \ln\Xi}{\partial \mu}\right)_{T,V}$ で与えられるため，これを計算します。

$$
\begin{aligned}
\overline{N}
&= \frac{1}{\beta}\sum_{\boldsymbol{k}} \frac{\beta e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}}{1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}} \\
&= \sum_{\boldsymbol{k}} \frac{1}{e^{\beta(\varepsilon_{\boldsymbol{k}} - \mu)} + 1} = \sum_{\boldsymbol{k}} f(\varepsilon_{\boldsymbol{k}})
\end{aligned}
$$

よって式 (7) が成り立ちます。

### (7)
$L$ が十分大きいとき，波数空間の1状態あたりの体積は $\left(\dfrac{2\pi}{L}\right)^3 = \dfrac{(2\pi)^3}{V}$ なので，和を積分 $\displaystyle\sum_{\boldsymbol{k}} \to \dfrac{V}{(2\pi)^3}\int \mathrm{d}^3k$ に置き換えます。式 (9) を用いて $N = \overline{N}$ を計算します。

$$
\begin{aligned}
N
&\approx \frac{V}{(2\pi)^3}\int_{-\infty}^{\infty}\mathrm{d}k_x \int_{-\infty}^{\infty}\mathrm{d}k_y \int_{-\infty}^{\infty}\mathrm{d}k_z \, \exp\left[-\beta\left(\frac{\hbar^2}{2m}(k_x^2 + k_y^2 + k_z^2) - \mu\right)\right] \\
&= \frac{V}{(2\pi)^3} e^{\beta\mu} \left(\int_{-\infty}^{\infty} e^{-\frac{\beta\hbar^2}{2m}k_x^2}\,\mathrm{d}k_x\right)^3 \\
&= \frac{V}{(2\pi)^3} e^{\beta\mu} \left(\sqrt{\frac{2\pi m}{\beta\hbar^2}}\right)^3 \\
&= V e^{\beta\mu} \left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right)^{\frac{3}{2}}
\end{aligned}
$$

ここで $h = 2\pi\hbar$ を用いました。両辺の対数をとって $\mu$ について解きます。

$$
\beta\mu = \ln\left[\frac{N}{V}\left(\frac{h^2}{2\pi m k_{\mathrm{B}} T}\right)^{\frac{3}{2}}\right]
$$

したがって，

$$
\finalanswer{\mu = k_{\mathrm{B}} T \ln\left[\frac{N}{V}\left(\frac{h^2}{2\pi m k_{\mathrm{B}} T}\right)^{\frac{3}{2}}\right]}
$$

### (8)
グランドポテンシャル $J(T, V, \mu) = -k_{\mathrm{B}} T \ln\Xi(T, V, \mu)$ は $\mathrm{d}J = -S\,\mathrm{d}T - P\,\mathrm{d}V - \overline{N}\,\mathrm{d}\mu$ を満たすため，エントロピーは $S = -\left(\dfrac{\partial J}{\partial T}\right)_{V,\mu}$ で与えられます。

高温領域（$|\mu| \gg k_{\mathrm{B}} T,\ \mu < 0$）ではすべての $\boldsymbol{k}$ について $e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)} \ll 1$ なので，$\ln\left(1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}\right) \approx e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}$ と近似することができます。問7の積分結果を用いると，

$$
\ln\Xi(T, V, \mu) \approx \sum_{\boldsymbol{k}} e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)} \approx V e^{\frac{\mu}{k_{\mathrm{B}} T}}\left(\frac{2\pi m k_{\mathrm{B}} T}{h^2}\right)^{\frac{3}{2}} = N
$$

となります。よって $J = -k_{\mathrm{B}} T \ln\Xi$ を $V, \mu$ 一定のもとで $T$ について偏微分します。

$$
\begin{aligned}
S
&= -\left(\frac{\partial J}{\partial T}\right)_{V,\mu} \\
&= k_{\mathrm{B}}\ln\Xi + k_{\mathrm{B}} T \left(\frac{\partial \ln\Xi}{\partial T}\right)_{V,\mu} \\
&= k_{\mathrm{B}} N + k_{\mathrm{B}} T \left(-\frac{\mu}{k_{\mathrm{B}} T^2} + \frac{3}{2T}\right) N \\
&= -\frac{\mu}{T} N + \frac{5}{2} N k_{\mathrm{B}}
\end{aligned}
$$

ここで仮定より $-\mu = |\mu| \gg k_{\mathrm{B}} T$ なので，$\dfrac{5}{2} k_{\mathrm{B}}$ は $-\dfrac{\mu}{T}$ に比べて十分小さく無視することができます。したがって，

$$
S \approx -\frac{\mu}{T} N
$$

が成り立ちます。

### (9)
縮退温度 $T_{\mathrm{F}}$ より十分低い温度（$T \ll T_{\mathrm{F}}$）では，$C_V = \gamma T$ と熱力学第三法則 $S(T \to 0) = 0$ より，

$$
S(T) = \int_0^T \frac{C_V(T')}{T'}\,\mathrm{d}T' = \int_0^T \gamma\,\mathrm{d}T' = \gamma T
$$

となり，エントロピーは原点 $(0, 0)$ から傾き $\gamma$ で線形に立ち上がります。一方，高温領域（$T \gg T_{\mathrm{F}}$）では，問7の $\mu$ を問8の式 $S = -\dfrac{\mu}{T} N + \dfrac{5}{2} N k_{\mathrm{B}}$ に代入すると問3の古典理想気体の結果 $S_{\mathrm{cl}}(T)$ に一致し，対数的に緩やかに増加します。

以上をまとめたグラフは次のとおりです（実線がフェルミ粒子系のエントロピー $S_{\mathrm{F}}$，破線が古典理想気体のエントロピー $S_{\mathrm{cl}}$）。

<figure class="problem-figure" markdown>
![フェルミ粒子系と古典理想気体のエントロピーの温度依存性](../../../docs/assets/figures/pastexam-todai-ributsu/R2_butsuri_2-s-light.svg#only-light)
![フェルミ粒子系と古典理想気体のエントロピーの温度依存性](../../../docs/assets/figures/pastexam-todai-ributsu/R2_butsuri_2-s-dark.svg#only-dark)
<figcaption markdown="span">自由フェルミ粒子系のエントロピー $S_{\mathrm{F}}$（実線）と古典理想気体のエントロピー $S_{\mathrm{cl}}$（破線）の温度依存性。$T \ll T_{\mathrm{F}}$ では $S_{\mathrm{F}} \simeq \gamma T \to 0$ となり，$T \gg T_{\mathrm{F}}$ では古典結果に漸近する。</figcaption>
</figure>

<aside class="rigor-note" markdown>
問3で導いた古典理想気体のエントロピーはザックール・テトローデの式と呼ばれます。問7の化学ポテンシャルを問8の精密な表式 $S = -\dfrac{\mu}{T}N + \dfrac{5}{2}Nk_{\mathrm{B}}$ に代入すると，定数項 $\dfrac{5}{2}Nk_{\mathrm{B}}$ も含めてザックール・テトローデの式に完全に一致します。量子統計から古典極限をとることで，古典論では手で導入した $1/h^{3N}$ と $1/N!$ の因子が自然に再現されます。
</aside>
