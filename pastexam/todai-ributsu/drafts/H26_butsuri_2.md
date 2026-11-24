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
2 次元放物線分散では状態密度がエネルギーによらない定数となるため，自由フェルミ気体の粒子数積分を初等関数で厳密に評価することが可能です。大分配関数の積表示からフェルミ分布関数を導き，低温比熱が $T$ に比例する仕組みをフェルミ面近傍の熱励起として捉えるのが前半の柱です。

後半はエネルギーギャップ $2\Delta$ を持つ真性半導体型の 2 バンド模型です。低温 $k_{\mathrm{B}} T \ll \Delta$ では上下バンドの分布にボルツマン近似が成り立ち，負エネルギー帯に生じた空孔（正孔）数と正エネルギー帯へ励起された粒子数の釣り合いから，有効質量の比 $M/m$ による化学ポテンシャルの温度変化が定まります。
</div>

### (1)
周期境界条件のもとで，波数 $\boldsymbol{k} = (k_x, k_y)$ は整数 $n_x, n_y$ を用いて $k_x = \dfrac{2\pi}{L}n_x$，$k_y = \dfrac{2\pi}{L}n_y$ と離散化されます。1 粒子の固有エネルギーは次のとおりです。

$$
\varepsilon_{\boldsymbol{k}} = \frac{\hbar^2 |\boldsymbol{k}|^2}{2m} = \frac{\hbar^2(k_x^2 + k_y^2)}{2m}
$$

スピンの自由度がないため，各波数状態にはフェルミ粒子が最大 1 個まで入ります。$N_0$ が十分大きいとき，占有される波数空間の領域は半径 $k_{\mathrm{F}}$ の円とみなされます。1 状態あたりの波数空間の面積は $\left(\dfrac{2\pi}{L}\right)^2$ なので，

$$
N_0 = \frac{\pi k_{\mathrm{F}}^2}{(2\pi / L)^2} = \frac{L^2 k_{\mathrm{F}}^2}{4\pi} \implies k_{\mathrm{F}}^2 = \frac{4\pi N_0}{L^2}
$$

となります。したがって，固有エネルギーの最大値（フェルミエネルギー $\varepsilon_{\mathrm{F}}$）は次のとおりです。

$$
\varepsilon_{\mathrm{F}} = \frac{\hbar^2 k_{\mathrm{F}}^2}{2m} = \frac{2\pi\hbar^2 N_0}{m L^2}
$$

$$
\finalanswer{\varepsilon_{\boldsymbol{k}} = \frac{\hbar^2 |\boldsymbol{k}|^2}{2m}, \qquad \varepsilon_{\mathrm{F}} = \frac{2\pi\hbar^2 N_0}{m L^2}}
$$

### (2)
全粒子数 $N$ についての和と $N = \sum_{\boldsymbol{k}} n_{\boldsymbol{k}}$ の制約つき和を合わせると，各波数 $\boldsymbol{k}$ の占有数 $n_{\boldsymbol{k}}$ を独立にすべての可能な値にわたって足し合わせる和に一致します。フェルミ粒子ではパウリの排他原理により $n_{\boldsymbol{k}} = 0, 1$ なので，次のように変形されます。

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
大分配関数 (1) を $\mu$ で偏微分すると $\dfrac{\partial \Xi}{\partial \mu} = \beta \sum_{N}\sum_{\{n_{\boldsymbol{k}}\}} N e^{-\beta(E_N - \mu N)}$ となるため，全粒子数の期待値 $\overline{N}$ は (2) で得た積表示を用いて次のように計算されます。

$$
\begin{aligned}
\overline{N}
&= \frac{1}{\beta}\frac{\partial \ln \Xi}{\partial \mu}
= \frac{1}{\beta}\sum_{\boldsymbol{k}}\frac{\partial}{\partial \mu}\ln\!\left(1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}\right) \\
&= \sum_{\boldsymbol{k}}\frac{e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}}{1 + e^{-\beta(\varepsilon_{\boldsymbol{k}} - \mu)}}
= \sum_{\boldsymbol{k}}\frac{1}{e^{\beta(\varepsilon_{\boldsymbol{k}} - \mu)} + 1}
= \sum_{\boldsymbol{k}} f(\varepsilon_{\boldsymbol{k}})
\end{aligned}
$$

ここに $f(\varepsilon) = \dfrac{1}{e^{\beta(\varepsilon - \mu)} + 1}$ はフェルミ分布関数であり，(2) 式が成り立ちます。

次に，$L$ が十分大きいとして $\sum_{\boldsymbol{k}} \to \dfrac{L^2}{(2\pi)^2}\int \mathrm{d}^2 k$ と置き換えます。$\varepsilon = \dfrac{\hbar^2 k^2}{2m}$ より $k\,\mathrm{d}k = \dfrac{m}{\hbar^2}\,\mathrm{d}\varepsilon$ なので，2 次元状態密度はエネルギーによらない定数 $D(\varepsilon) = \dfrac{L^2}{(2\pi)^2}\cdot 2\pi \dfrac{m}{\hbar^2} = \dfrac{m L^2}{2\pi\hbar^2}$（$\varepsilon \ge 0$）となります。よって積分を計算すると次の結果が得られます。

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
絶対零度では負のエネルギー帯（価電子帯，$\varepsilon_{1\boldsymbol{k}} \le -\Delta$）が完全に満たされ，正のエネルギー帯（伝導帯，$\varepsilon_{2\boldsymbol{k}} \ge \Delta$）が完全に空であるため，化学ポテンシャル $\mu$ はエネルギーギャップ $(-\Delta, \Delta)$ の内部に位置します。

$0 < k_{\mathrm{B}} T \ll \Delta$ の温度領域では，熱エネルギー $k_{\mathrm{B}} T$ がギャップ幅 $2\Delta$ に比べて極めて小さいため，負のエネルギー帯の上端近傍（$\boldsymbol{k} \approx \boldsymbol{0}$，$\varepsilon_{1\boldsymbol{k}} \approx -\Delta$）にあるごく一部の粒子だけが熱励起によってギャップを越え，正のエネルギー帯の下端近傍（$\boldsymbol{k} \approx \boldsymbol{0}$，$\varepsilon_{2\boldsymbol{k}} \approx \Delta$）の準位へ移ります。その結果，正のエネルギー帯の $\boldsymbol{k} \approx \boldsymbol{0}$ 近傍に指数関数的に小さい割合（$\sim e^{-\Delta/(k_{\mathrm{B}} T)}$）の粒子が分布し，負のエネルギー帯の $\boldsymbol{k} \approx \boldsymbol{0}$ 近傍に同数の空席（正孔）が生じます。一方，$|\boldsymbol{k}|$ の大きい負エネルギー状態はほぼ完全に占有されたままであり，高エネルギーの正エネルギー状態はほぼ完全に空のままです。

### (6)
正のエネルギー帯の粒子数の期待値を $\overline{N}_2(T)$ とすると，全粒子数保存より

$$
\overline{N}_1(T) + \overline{N}_2(T) = \overline{N}_1(0) \implies \overline{N}_1(0) - \overline{N}_1(T) = \overline{N}_2(T)
$$

が成り立ちます。左辺は負のエネルギー帯に生じた空席（正孔）の数であり，次のように表されます。

$$
\overline{N}_1(0) - \overline{N}_1(T)
= \sum_{|\boldsymbol{k}| < K}\left[1 - f(\varepsilon_{1\boldsymbol{k}})\right]
= \sum_{|\boldsymbol{k}| < K}\frac{1}{e^{\beta(\mu - \varepsilon_{1\boldsymbol{k}})} + 1}
$$

ここで $-\Delta < \mu < \Delta$ かつ $\beta(\mu + \Delta) \gg 1$，$\beta(\Delta - \mu) \gg 1$ を仮定して（結果がこれを満たすことを後で確かめます），分母の $1$ を無視するボルツマン近似を行い，$K$ が十分大きいことから波数積分の上限を $\infty$ に伸ばします。

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

が得られます。$k_{\mathrm{B}} T \ll \Delta$ のもとで $|\mu(T)| \ll \Delta$ なので，$\beta(\Delta \pm \mu) \gg 1$ の仮定は自己無撞着に満たされています。

$$
\finalanswer{\mu(T) = \frac{1}{2}k_{\mathrm{B}} T \ln\!\left(\frac{M}{m}\right)}
$$

<aside class="rigor-note" markdown>
2 次元では状態密度が有効質量に比例するため，化学ポテンシャルの温度勾配の係数は $\dfrac{1}{2}k_{\mathrm{B}}\ln(M/m)$ となります（3 次元真性半導体では状態密度が $m^{3/2}$ に比例するため，$\dfrac{3}{4}k_{\mathrm{B}} T \ln(M/m)$ になります）。$M > m$ のとき負のエネルギー帯の状態密度が正のエネルギー帯より大きく，正孔数と励起粒子数を釣り合わせるために $\mu$ はギャップ中央（$0$）から正のエネルギー帯側へ引き上げられます。また，(3) の結果を用いると，2 次元では $K \to \infty$ の積分は近似なしでも $\ln(1 + e^{-\beta(\mu+\Delta)}) / \ln(1 + e^{-\beta(\Delta-\mu)}) = m/M$ と厳密に書き下すことができます。
</aside>
