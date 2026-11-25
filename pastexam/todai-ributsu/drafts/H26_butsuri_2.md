---
title: 東大理物 平成26年度 物理学 第2問：2次元フェルミ粒子系と2バンド模型
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
  - 物性物理学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成26年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成26年度 物理学 第2問：2次元フェルミ粒子系と2バンド模型

## 問題

$xy$ 平面上の 2 次元空間内に閉じ込められたフェルミ粒子系のグランドカノニカル分布を考える。空間は，一辺の長さが $L$ の正方形として周期境界条件を採用する。以下の設問ではスピンの自由度は考えない。

まず，質量 $m$ の自由フェルミ粒子系を考える。

(1) フェルミ粒子の持つ波数を $\boldsymbol{k} = (k_x, k_y)$ とし，1 粒子の固有エネルギー $\varepsilon_{\boldsymbol{k}}$ を求めよ。さらに，この固有エネルギーの低い方から順に $N_0$ 番目までフェルミ粒子を詰めたとする。このときの固有エネルギーの最大の値を求めよ。ただし $N_0$ は十分大きな数とせよ。

(2) このフェルミ粒子系の大分配関数

$$
\Xi(T, \mu) = \sum_{N=0}^{\infty}\sum_{\{n_{\boldsymbol{k}}\}} e^{-\beta(E_N - \mu N)} \tag{1}
$$

を $\boldsymbol{k}$ の取り得る値についての積の形に変形せよ。ここで $\beta = 1 / (k_{\mathrm{B}} T)$，$k_{\mathrm{B}}$ はボルツマン定数，$T$ は絶対温度，$\mu$ は化学ポテンシャルである。また $n_{\boldsymbol{k}}$ は波数 $\boldsymbol{k}$ を持つ粒子の数を表し，$\{n_{\boldsymbol{k}}\}$ に関する和は，$N = \sum_{\boldsymbol{k}} n_{\boldsymbol{k}}$ を満たすすべての可能な $\{n_{\boldsymbol{k}}\}$ の組み合わせについての和である。また，$E_N$ は $\{n_{\boldsymbol{k}}\}$ に依存する全エネルギーで，$E_N = \sum_{\boldsymbol{k}} n_{\boldsymbol{k}} \varepsilon_{\boldsymbol{k}}$ で与えられる。

(3) グランドカノニカル分布において，全粒子数の期待値 $\overline{N}$ に関して

$$
\overline{N} = \sum_{\boldsymbol{k}} f(\varepsilon_{\boldsymbol{k}}) \tag{2}
$$

が成り立つことを示せ。ここで $f(\varepsilon_{\boldsymbol{k}})$ はフェルミ分布関数である。さらに，$L$ が十分大きいとして，(2) 式の $\boldsymbol{k}$ に関する和をエネルギー積分の形に書き直して積分を実行せよ。

(4) フェルミ分布関数の概形を用いて，低温の極限における比熱が温度 $T$ に比例する理由を定性的に説明せよ。

次に，1 つの波数 $\boldsymbol{k}$ に対して，エネルギーが負の状態とエネルギーが正の状態があるようなフェルミ粒子系を考える（図 1）。エネルギーが負の分散関係と正の分散関係は，それぞれ

$$
\varepsilon_{1\boldsymbol{k}} = -\Delta - \frac{\hbar^2 |\boldsymbol{k}|^2}{2M}, \qquad \varepsilon_{2\boldsymbol{k}} = \Delta + \frac{\hbar^2 |\boldsymbol{k}|^2}{2m} \tag{3}
$$

であるとする。絶対零度では，負のエネルギー状態に粒子が完全に詰まっていて，正のエネルギー状態には粒子が存在しないとする。

<figure class="problem-figure" markdown>
![k_y=0での2バンド分散関係](../../../docs/assets/figures/pastexam-todai-ributsu/H26_butsuri_2-p-light.svg#only-light)
![k_y=0での2バンド分散関係](../../../docs/assets/figures/pastexam-todai-ributsu/H26_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">図 1：$k_y = 0$ での分散関係</figcaption>
</figure>

(5) $0 < k_{\mathrm{B}} T \ll \Delta$ の温度領域において，粒子の分布がどのようになるかを定性的に説明せよ。

(6) 負のエネルギー状態のフェルミ粒子の粒子数の期待値を $\overline{N}_1(T)$ と書く。ただし，2 次元の波数 $\boldsymbol{k}$ の絶対値には上限 $K$ があるとし，絶対零度では

$$
\overline{N}_1(0) = \sum_{|\boldsymbol{k}| < K} 1
$$

と書けるとする。設問 5 と同じ温度領域において，$\mu$ を温度の関数として求めよ。ただし，$K$ は十分大きいとしてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成26年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2次元の放物線分散では，等しいエネルギー幅に含まれる状態数が一定です。そのため，波数についての和をエネルギー積分に直すと，粒子数を計算しやすくなります。

低温でギャップを越えて励起される粒子は少ないため，励起粒子と正孔の分布をボルツマン近似で扱うことができます。全粒子数を保つ条件から両者の数を等しくすることで，化学ポテンシャルを調べることができます。
</div>

### (1)
周期境界条件のもとで，波数 $\boldsymbol{k} = (k_x, k_y)$ は整数 $n_x, n_y$ を用いて $k_x = \dfrac{2\pi}{L}n_x$，$k_y = \dfrac{2\pi}{L}n_y$ と離散化されます。1 粒子の固有エネルギーは次のとおりです。

$$
\begin{aligned}
\varepsilon_{\boldsymbol{k}} &= \frac{\hbar^2 |\boldsymbol{k}|^2}{2m} \\
&= \frac{\hbar^2(k_x^2 + k_y^2)}{2m}
\end{aligned}
$$

スピンの自由度がないため，各波数状態にはフェルミ粒子が最大 1 個まで入ります。$N_0$ が十分大きいとき，占有される波数空間の領域は半径 $k_{\mathrm{F}}$ の円とみなされます。1 状態あたりの波数空間の面積は $\left(\dfrac{2\pi}{L}\right)^2$ なので，

$$
\begin{aligned}
N_0&=\frac{\pi k_{\mathrm{F}}^2}{(2\pi/L)^2}\\
&=\frac{L^2k_{\mathrm{F}}^2}{4\pi}\\
k_{\mathrm{F}}^2&=\frac{4\pi N_0}{L^2}
\end{aligned}
$$

となります。したがって，固有エネルギーの最大値を**フェルミエネルギー** $\varepsilon_{\mathrm{F}}$ といいます。したがって，

$$
\begin{aligned}
\varepsilon_{\mathrm{F}} &= \frac{\hbar^2 k_{\mathrm{F}}^2}{2m} \\
&= \frac{2\pi\hbar^2 N_0}{m L^2}
\end{aligned}
$$

$$
\finalanswer{\varepsilon_{\boldsymbol{k}} = \frac{\hbar^2 |\boldsymbol{k}|^2}{2m}, \qquad \varepsilon_{\mathrm{F}} = \frac{2\pi\hbar^2 N_0}{m L^2}}
$$

### (2)
全粒子数 $N$ についての和と $N = \displaystyle\sum_{\boldsymbol{k}} n_{\boldsymbol{k}}$ の制約つき和を合わせると，各波数 $\boldsymbol{k}$ の占有数 $n_{\boldsymbol{k}}$ を独立にすべての可能な値にわたって足し合わせる和に一致します。フェルミ粒子ではパウリの排他原理により $n_{\boldsymbol{k}} = 0, 1$ なので，次のように変形されます。

$$
\begin{aligned}
\Xi(T, \mu)
&= \sum_{N=0}^{\infty}\sum_{\sum_{\boldsymbol{k}} n_{\boldsymbol{k}} = N} \exp\!\left[-\beta\sum_{\boldsymbol{k}} n_{\boldsymbol{k}}(\varepsilon_{\boldsymbol{k}} - \mu)\right] \\
&= \prod_{\boldsymbol{k}}\left(\sum_{n_{\boldsymbol{k}} = 0}^{1} e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu) n_{\boldsymbol{k}}}\right) \\
&= \prod_{\boldsymbol{k}}\left(1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}\right)
\end{aligned}
$$

$$
\finalanswer{\Xi(T, \mu) = \prod_{\boldsymbol{k}}\left(1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}\right)}
$$

### (3)
大分配関数 (1) を $\mu$ で偏微分すると $\dfrac{\partial \Xi}{\partial \mu} = \beta \displaystyle\sum_{N}\sum_{\{n_{\boldsymbol{k}}\}} N e^{-\beta(E_N - \mu N)}$ となるため，全粒子数の期待値 $\overline{N}$ は (2) で得た積表示を用いて次のように計算されます。

$$
\begin{aligned}
\overline{N} &= \frac{1}{\beta}\frac{\partial \ln \Xi}{\partial \mu} \\
&= \frac{1}{\beta}\sum_{\boldsymbol{k}}\frac{\partial}{\partial \mu}\ln\!\left(1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}\right) \\
 &= \sum_{\boldsymbol{k}}\frac{e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}}{1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}} \\
&= \sum_{\boldsymbol{k}}\frac{1}{e^{\beta(\varepsilon_{\boldsymbol{k}} - \mu)} + 1} \\
&= \sum_{\boldsymbol{k}} f(\varepsilon_{\boldsymbol{k}})
\end{aligned}
$$

ここに $f(\varepsilon) = \dfrac{1}{e^{\beta(\varepsilon - \mu)} + 1}$ はフェルミ分布関数であり，(2) 式が成り立ちます。

次に，$L$ が十分大きいとして波数和を積分に置き換えます。

$$
\sum_{\boldsymbol{k}}\longrightarrow\frac{L^2}{(2\pi)^2}\int\mathrm{d}^2k
$$

$\varepsilon=\dfrac{\hbar^2k^2}{2m}$ より $k\,\mathrm{d}k=\dfrac{m}{\hbar^2}\,\mathrm{d}\varepsilon$ です。状態密度は，

$$
\begin{aligned}
D(\varepsilon)&=\frac{L^2}{(2\pi)^2}\,2\pi\frac{m}{\hbar^2}\\
&=\frac{mL^2}{2\pi\hbar^2}\qquad(\varepsilon\ge0)
\end{aligned}
$$

となり，エネルギーによらない定数です。したがって，粒子数の積分は次のようになります。

$$
\begin{aligned}
\overline{N}
&= \frac{m L^2}{2\pi\hbar^2}\int_0^{\infty}\frac{\mathrm{d}\varepsilon}{e^{\beta(\varepsilon - \mu)} + 1} \\
&= \frac{m L^2}{2\pi\hbar^2}\int_0^{\infty}\frac{e^{-\beta(\varepsilon - \mu)}}{1 + e^{-\beta(\varepsilon - \mu)}}\,\mathrm{d}\varepsilon \\
&= \frac{m L^2}{2\pi\hbar^2}\left[-\frac{1}{\beta}\ln\!\left(1 + e^{-\beta(\varepsilon - \mu)}\right)\right]_0^{\infty} \\
&= \frac{m L^2 k_{\mathrm{B}} T}{2\pi\hbar^2}\ln\!\left(1 + e^{\beta\mu}\right)
\end{aligned}
$$

$$
\finalanswer{\overline{N} = \frac{m L^2 k_{\mathrm{B}} T}{2\pi\hbar^2}\ln\!\left(1 + e^{\beta\mu}\right)}
$$

### (4)
フェルミ分布関数 $f(\varepsilon) = \dfrac{1}{e^{\beta(\varepsilon - \mu)} + 1}$ は，絶対零度 $T = 0$ では $\varepsilon < \varepsilon_{\mathrm{F}}$ で $1$，$\varepsilon > \varepsilon_{\mathrm{F}}$ で $0$ をとる階段関数です。低温 $k_{\mathrm{B}} T \ll \varepsilon_{\mathrm{F}}$ では，この階段の縁がフェルミエネルギー $\varepsilon_{\mathrm{F}}$ を中心とする幅 $\sim k_{\mathrm{B}} T$ の狭い領域でのみ滑らかに変化し，$\varepsilon_{\mathrm{F}} - \varepsilon \gg k_{\mathrm{B}} T$ の深い準位では依然として $f(\varepsilon) \simeq 1$，$\varepsilon - \varepsilon_{\mathrm{F}} \gg k_{\mathrm{B}} T$ の高い準位では $f(\varepsilon) \simeq 0$ に保たれます。

パウリの排他原理により，深い準位にある粒子は近傍の状態がすでに占有されているため熱励起されることがなく，$\varepsilon_{\mathrm{F}}$ からおよそ $k_{\mathrm{B}} T$ 以内のエネルギー帯にある粒子のみが，$\varepsilon_{\mathrm{F}}$ よりおよそ $k_{\mathrm{B}} T$ 高い空状態へ励起されます。励起される粒子数は状態密度 $D(\varepsilon_{\mathrm{F}})$ を用いて $\Delta N \sim D(\varepsilon_{\mathrm{F}}) k_{\mathrm{B}} T$ の程度であり，各粒子が得る平均エネルギー増加は $\Delta\varepsilon \sim k_{\mathrm{B}} T$ の程度です。したがって，絶対零度からの内部エネルギーの増加は

$$
\Delta U = U(T) - U(0) \sim \Delta N \cdot \Delta\varepsilon \sim D(\varepsilon_{\mathrm{F}})(k_{\mathrm{B}} T)^2 \propto T^2
$$

となります。これを温度 $T$ で微分して得られる比熱 $C = \dfrac{\partial U}{\partial T}$ は $C \sim D(\varepsilon_{\mathrm{F}}) k_{\mathrm{B}}^2 T$ となり，温度 $T$ に比例します。

### (5)
負のエネルギー帯を**価電子帯**，正のエネルギー帯を**伝導帯**といいます。絶対零度では価電子帯が完全に満たされ，伝導帯は空です。この占有状態に対応する化学ポテンシャル $\mu$ は，ギャップ $(-\Delta,\Delta)$ の内部にあります。

$0<k_{\mathrm{B}}T\ll\Delta$ では，負のエネルギー帯の上端 $-\Delta$ 付近にあるごく一部の粒子が，正のエネルギー帯の下端 $\Delta$ 付近へ熱励起されます。両方のバンド端は $\boldsymbol{k}=\boldsymbol{0}$ にあります。

正のエネルギー帯では $\boldsymbol{k}\approx\boldsymbol{0}$ 付近に少数の励起粒子が生じ，負のエネルギー帯には同数の空席が生じます。この空席を**正孔**といいます。励起粒子と正孔の数は，低温で $e^{-\Delta/(k_{\mathrm{B}}T)}$ を含む指数関数に従って小さくなります。

$|\boldsymbol{k}|$ の大きい負のエネルギー状態は，ほぼ完全に占有されたままです。高い正のエネルギー状態は，ほぼ空のままです。

### (6)
正のエネルギー帯の粒子数の期待値を $\overline{N}_2(T)$ とすると，全粒子数保存より

$$
\overline{N}_1(T) + \overline{N}_2(T) = \overline{N}_1(0) \implies \overline{N}_1(0) - \overline{N}_1(T) = \overline{N}_2(T)
$$

が成り立ちます。左辺は負のエネルギー帯に生じた正孔数であり，次のように表されます。

$$
\begin{aligned}
\overline{N}_1(0) - \overline{N}_1(T) &= \sum_{|\boldsymbol{k}| < K}\left[1 - f(\varepsilon_{1\boldsymbol{k}})\right] \\
&= \sum_{|\boldsymbol{k}| < K}\frac{1}{e^{\beta(\mu - \varepsilon_{1\boldsymbol{k}})} + 1}
\end{aligned}
$$

ここでは $-\Delta<\mu<\Delta$ かつ $\beta(\mu+\Delta)\gg1$，$\beta(\Delta-\mu)\gg1$ として，分母の $1$ を無視するボルツマン近似を用います。得られた結果が仮定を満たす温度範囲は後で確認します。また，波数和を積分に置き換えるため $L$ を十分大きくとり，$K$ が熱的に励起される波数より十分大きいとして積分の上限を $\infty$ に伸ばします。

まず負のエネルギー帯の空席数は次のように計算されます。

$$
\begin{aligned}
\overline{N}_1(0) - \overline{N}_1(T)
&\simeq \sum_{|\boldsymbol{k}| < K} e^{-\beta(\mu - \varepsilon_{1\boldsymbol{k}})}
= e^{-\beta(\mu + \Delta)}\sum_{|\boldsymbol{k}| < K} e^{-\beta\frac{\hbar^2 |\boldsymbol{k}|^2}{2M}} \\
&\simeq \frac{L^2}{(2\pi)^2} e^{-\beta(\mu + \Delta)}\int_0^{\infty} 2\pi k\, e^{-\beta\frac{\hbar^2 k^2}{2M}}\,\mathrm{d}k
= \frac{M L^2 k_{\mathrm{B}} T}{2\pi\hbar^2} e^{-\beta(\mu + \Delta)}
\end{aligned}
$$

同様に，正のエネルギー帯の粒子数は次のようになります。

$$
\begin{aligned}
\overline{N}_2(T)
&= \sum_{|\boldsymbol{k}| < K}\frac{1}{e^{\beta(\varepsilon_{2\boldsymbol{k}} - \mu)} + 1}
\simeq e^{-\beta(\Delta - \mu)}\sum_{|\boldsymbol{k}| < K} e^{-\beta\frac{\hbar^2 |\boldsymbol{k}|^2}{2m}} \\
&\simeq \frac{L^2}{(2\pi)^2} e^{-\beta(\Delta - \mu)}\int_0^{\infty} 2\pi k\, e^{-\beta\frac{\hbar^2 k^2}{2m}}\,\mathrm{d}k
= \frac{m L^2 k_{\mathrm{B}} T}{2\pi\hbar^2} e^{-\beta(\Delta - \mu)}
\end{aligned}
$$

両者を等しいとおくと，

$$
\begin{aligned}
\frac{M L^2 k_{\mathrm{B}} T}{2\pi\hbar^2} e^{-\beta(\mu + \Delta)} &= \frac{m L^2 k_{\mathrm{B}} T}{2\pi\hbar^2} e^{-\beta(\Delta - \mu)} \\
e^{2\beta\mu} &= \frac{M}{m} \\
\mu(T) &= \frac{1}{2}k_{\mathrm{B}} T \ln\!\left(\frac{M}{m}\right)
\end{aligned}
$$

が得られます。質量比 $M/m$ を有限の値に保って十分低温にすると，$|\mu(T)|\ll\Delta$ となります。具体的には $\beta\Delta\pm\dfrac{1}{2}\ln(M/m)\gg1$ の両方が満たされる範囲で，先に用いたボルツマン近似と整合します。

$$
\finalanswer{\mu(T) = \frac{1}{2}k_{\mathrm{B}} T \ln\!\left(\frac{M}{m}\right)}
$$

<aside class="rigor-note" markdown>
2次元では状態密度が有効質量に比例するため，低温の化学ポテンシャルの温度勾配は $\dfrac{\mathrm{d}\mu}{\mathrm{d}T}\simeq\dfrac{1}{2}k_{\mathrm{B}}\ln(M/m)$ です。3次元では状態密度に現れる質量因子が $m^{3/2}$ となるため，$\mu(T)\simeq\dfrac{3}{4}k_{\mathrm{B}}T\ln(M/m)$ であり，温度勾配は $\dfrac{3}{4}k_{\mathrm{B}}\ln(M/m)$ になります。

$M>m$ では負のエネルギー帯の状態密度が正のエネルギー帯より大きいため，正孔数と励起粒子数が等しくなる化学ポテンシャルは，ギャップの中央 $0$ より正のエネルギー帯側にあります。2次元で $K\to\infty$ とした連続近似では，粒子数の条件をボルツマン近似なしで

$$
\frac{\ln(1+e^{-\beta(\mu+\Delta)})}{\ln(1+e^{-\beta(\Delta-\mu)})}=\frac{m}{M}
$$

と表すことができます。
</aside>
