---
title: 東大理物 平成25年度 物理学 第2問：理想ボース気体とボース・アインシュタイン凝縮
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成25年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成25年度 物理学 第2問：理想ボース気体とボース・アインシュタイン凝縮

## 問題

十分大きな体積 $V$ の三次元領域に閉じ込められている理想ボース気体について以下の設問に答えよ。ただし，設問 1 から 6 においてパラメータ $t$ を含んだ積分

$$
\int_0^{\infty} \mathrm{d}x\,\frac{x^t}{e^x - 1}
$$

が $t = \dfrac{1}{2}, \dfrac{3}{2}$ のとき収束することを用いてもよい。

(1) 温度 $T$，化学ポテンシャル $\mu$ のグランドカノニカル分布における大分配関数の表式

$$
\Theta = \prod_i \Theta_i, \qquad \Theta_i = \sum_{n_i=0}^{\infty} \exp\!\left[-\beta(\epsilon_i - \mu) n_i\right], \qquad \beta = \frac{1}{k_{\mathrm{B}} T} \tag{1}
$$

を出発点にして，一粒子状態 $i$ にある粒子数の統計力学的平均値が

$$
f(\epsilon_i) = \frac{1}{\exp[\beta(\epsilon_i - \mu)] - 1} \tag{2}
$$

で与えられることを示せ。ここで $\epsilon_i$ は $i$ の一粒子エネルギー，$n_i$ は $i$ にある粒子数を表す。$k_{\mathrm{B}}$ はボルツマン定数を表すものとする。

スピン $0$ の理想ボース気体を考える。体積 $V$ が十分大きいので単位体積当たりの一粒子状態密度 $D(\epsilon)$ は，
{: .problem-lead }

$$
D(\epsilon) = \begin{cases} A\epsilon^{\frac{1}{2}}, & \epsilon \ge 0 \\ 0, & \epsilon < 0 \end{cases}, \qquad A = \frac{m^{\frac{3}{2}}}{2^{\frac{1}{2}}\pi^2 \hbar^3} \tag{3}
$$

とおくことができる。ここで $m$ はボース粒子の質量を表し，$\hbar$ はプランク定数を $2\pi$ で割ったものを表す。粒子数密度（全粒子数 $N$ を体積 $V$ で割ったもの）を $\rho$ で表し，$\rho'$ を

$$
\rho' \equiv \int_{-\infty}^{\infty} \mathrm{d}\epsilon\, D(\epsilon) f(\epsilon) = A\int_0^{\infty} \mathrm{d}\epsilon\,\epsilon^{\frac{1}{2}} f(\epsilon) \tag{4}
$$

と定義する。ある温度 $T_{\mathrm{c}}$ 以上では $\rho' = \rho$ が成り立つが，$T_{\mathrm{c}}$ より低温ではボース・アインシュタイン凝縮が起きるため $\rho' < \rho$ となる。また $T_{\mathrm{c}}$ 以下の温度では化学ポテンシャル $\mu$ はゼロとなる。

(2) ボース・アインシュタイン凝縮とはどのような現象か。40 字程度で説明せよ。

(3) $T_{\mathrm{c}}$ において平均粒子間距離 $\ell = \left(\dfrac{3}{4\pi\rho}\right)^{\frac{1}{3}}$ と熱的ドブロイ波長 $\lambda_T = \left(\dfrac{2\pi\hbar^2}{m k_{\mathrm{B}} T}\right)^{\frac{1}{2}}$ が同程度になることを示せ（ヒント：$T = T_{\mathrm{c}}$ のとき $\rho' = \rho$ かつ $\mu = 0$ である）。

(4) $T < T_{\mathrm{c}}$ における単位体積あたりの定積熱容量 $C_V = \left.\dfrac{\partial E}{\partial T}\right|_{N, V}$ の温度依存性を $C_V \propto T^{\gamma}$ と表したとき，$\gamma$ の値を求めよ。ここで $E$ は単位体積あたりの内部エネルギーで

$$
E = \int_{-\infty}^{\infty} \mathrm{d}\epsilon\,\epsilon D(\epsilon) f(\epsilon) = A\int_0^{\infty} \mathrm{d}\epsilon\,\epsilon^{\frac{3}{2}} f(\epsilon) \tag{5}
$$

を表す。

(5) $T < T_{\mathrm{c}}$ における単位体積当たりのエントロピー $S$ の温度依存性を $S \propto T^{\nu}$ と表したとき，$\nu$ を求めよ。

一様磁場の下でのスピン $1$ の理想ボース気体を考える。物理量 $\tilde{\rho}$ を
{: .problem-lead }

$$
\tilde{\rho} \equiv \int_{-\infty}^{\infty} \mathrm{d}\epsilon\,\tilde{D}(\epsilon) f(\epsilon), \qquad \tilde{D}(\epsilon) \equiv D(\epsilon - \epsilon_{\mathrm{Z}}) + D(\epsilon) + D(\epsilon + \epsilon_{\mathrm{Z}}) \tag{6}
$$

と定義すると，ボース・アインシュタイン凝縮の転移温度 $\tilde{T}_{\mathrm{c}}$ 以上では $\tilde{\rho}$ は粒子数密度 $\rho$ に等しいが，$\tilde{T}_{\mathrm{c}}$ より低温では $\tilde{\rho} < \rho$ となる。ここで $\epsilon_{\mathrm{Z}}$（$> 0$）はゼーマンエネルギーを表す。

(6) ゼーマンエネルギー $\epsilon_{\mathrm{Z}}$ を $\epsilon_{\mathrm{Z},1}$（$\ll k_{\mathrm{B}} T$）から $\epsilon_{\mathrm{Z},2}$（$\gg k_{\mathrm{B}} T$）まで断熱的に変化させたときの終状態の温度は始状態の温度より高いか低いかを，理由と共に述べよ。この断熱過程において常にボース・アインシュタイン凝縮は起きているものとしてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成25年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
転移温度以下では化学ポテンシャル $\mu$ が最低エネルギー準位に固定されるため，励起状態の粒子数密度や内部エネルギーの積分は $x = \beta\epsilon$ の変数変換だけで温度依存性のべき乗をくくり出すことができます。

スピン $1$ の系に強い磁場をかけると，ゼーマン分裂した 3 つの副準位のうち上位の 2 つは励起エネルギーが $k_{\mathrm{B}} T$ より十分大きくなって熱励起に関与できなくなります。断熱過程ではエントロピーが保たれるため，寄与する自由度の減少が温度の変化として現れます。
</div>

### (1)
各状態 $i$ について $\epsilon_i - \mu > 0$ のもとで，式 (1) の $\Theta_i$ は公比 $e^{-\beta(\epsilon_i - \mu)} < 1$ の無限等比級数なので，和を計算することができます。

$$
\begin{aligned}
\Theta_i &= \sum_{n_i=0}^{\infty} \left(e^{-\beta(\epsilon_i - \mu)}\right)^{n_i} \\
&= \frac{1}{1 - e^{-\beta(\epsilon_i - \mu)}}
\end{aligned}
$$

グランドカノニカル分布における状態 $i$ の平均粒子数 $\langle n_i \rangle$ は，大分配関数 $\Theta$ の対数を $\epsilon_i$ で偏微分して得られます。

$$
\begin{aligned}
\langle n_i \rangle &= \frac{1}{\Theta_i}\sum_{n_i=0}^{\infty} n_i e^{-\beta(\epsilon_i - \mu) n_i} \\
&= -\frac{1}{\beta}\frac{\partial \ln \Theta}{\partial \epsilon_i} \\
&= -\frac{1}{\beta}\frac{\partial \ln \Theta_i}{\partial \epsilon_i} \\
&= \frac{1}{\beta}\frac{\partial}{\partial \epsilon_i}\ln\!\left(1 - e^{-\beta(\epsilon_i - \mu)}\right) \\
&= \frac{1}{\beta}\cdot\frac{\beta e^{-\beta(\epsilon_i - \mu)}}{1 - e^{-\beta(\epsilon_i - \mu)}} \\
&= \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1}
\end{aligned}
$$

以上より，式 (2) が成り立ちます。

### (2)
転移温度以下で，巨視的な数のボース粒子が最低エネルギーの一粒子状態に集まる現象。

### (3)
$T = T_{\mathrm{c}}$ のとき $\rho' = \rho$ かつ $\mu = 0$ なので，式 (4) において $x = \beta_{\mathrm{c}}\epsilon = \dfrac{\epsilon}{k_{\mathrm{B}} T_{\mathrm{c}}}$ と変数変換します。

$$
\begin{aligned}
\rho &= A\int_0^{\infty} \mathrm{d}\epsilon\,\frac{\epsilon^{\frac{1}{2}}}{e^{\epsilon/(k_{\mathrm{B}} T_{\mathrm{c}})} - 1} \\
&= A\left(k_{\mathrm{B}} T_{\mathrm{c}}\right)^{\frac{3}{2}}\int_0^{\infty} \mathrm{d}x\,\frac{x^{\frac{1}{2}}}{e^x - 1}
\end{aligned}
$$

ここで $I_{1/2} \equiv \displaystyle\int_0^{\infty} \mathrm{d}x\,\dfrac{x^{1/2}}{e^x - 1}$ とおきます。問題文の仮定より $I_{1/2}$ は収束する正の無次元定数です。式 (3) の $A = \dfrac{m^{3/2}}{2^{1/2}\pi^2 \hbar^3}$ と $\lambda_{T_{\mathrm{c}}} = \left(\dfrac{2\pi\hbar^2}{m k_{\mathrm{B}} T_{\mathrm{c}}}\right)^{1/2}$ を用いて $\rho\lambda_{T_{\mathrm{c}}}^3$ を計算します。

$$
\begin{aligned}
\rho \lambda_{T_{\mathrm{c}}}^3 &= \frac{m^{\frac{3}{2}}}{2^{\frac{1}{2}}\pi^2 \hbar^3}\left(k_{\mathrm{B}} T_{\mathrm{c}}\right)^{\frac{3}{2}} I_{1/2} \cdot \left(\frac{2\pi\hbar^2}{m k_{\mathrm{B}} T_{\mathrm{c}}}\right)^{\frac{3}{2}} \\
&= \frac{2^{\frac{3}{2}}\pi^{\frac{3}{2}}}{2^{\frac{1}{2}}\pi^2}\,I_{1/2} \\
&= \frac{2}{\sqrt{\pi}}\,I_{1/2}
\end{aligned}
$$

平均粒子間距離は $\ell = \left(\dfrac{3}{4\pi\rho}\right)^{1/3}$ なので，$\ell$ と $\lambda_{T_{\mathrm{c}}}$ の比は次のようになります。

$$
\begin{aligned}
\frac{\lambda_{T_{\mathrm{c}}}}{\ell} &= \left(\frac{4\pi}{3}\,\rho\lambda_{T_{\mathrm{c}}}^3\right)^{\frac{1}{3}} \\
&= \left(\frac{8\sqrt{\pi}}{3}\,I_{1/2}\right)^{\frac{1}{3}}
\end{aligned}
$$

右辺は系のパラメータによらない $1$ の程度の無次元定数なので，$T = T_{\mathrm{c}}$ において平均粒子間距離 $\ell$ と熱的ドブロイ波長 $\lambda_{T_{\mathrm{c}}}$ は同程度になります。

### (4)
$T < T_{\mathrm{c}}$ では $\mu = 0$ です。式 (5) において $x = \dfrac{\epsilon}{k_{\mathrm{B}} T}$ と変数変換します。

$$
\begin{aligned}
E &= A\int_0^{\infty} \mathrm{d}\epsilon\,\frac{\epsilon^{\frac{3}{2}}}{e^{\epsilon/(k_{\mathrm{B}} T)} - 1} \\
&= A\left(k_{\mathrm{B}} T\right)^{\frac{5}{2}}\int_0^{\infty} \mathrm{d}x\,\frac{x^{\frac{3}{2}}}{e^x - 1}
\end{aligned}
$$

ここで $I_{3/2} \equiv \displaystyle\int_0^{\infty} \mathrm{d}x\,\dfrac{x^{3/2}}{e^x - 1}$ は収束する正の定数です。よって $E = A I_{3/2} k_{\mathrm{B}}^{5/2} T^{5/2}$ となり，これを $T$ で偏微分すると定積熱容量 $C_V$ が得られます。

$$
\begin{aligned}
C_V &= \left.\frac{\partial E}{\partial T}\right|_{N, V} \\
&= \frac{5}{2} A I_{3/2} k_{\mathrm{B}}^{\frac{5}{2}}\,T^{\frac{3}{2}}
\end{aligned}
$$

したがって，$C_V \propto T^{3/2}$ であり，$\gamma = \dfrac{3}{2}$ です。

$$
\finalanswer{\gamma = \frac{3}{2}}
$$

### (5)
定積過程での熱力学関係式 $\left.\dfrac{\partial S}{\partial T}\right|_{N, V} = \dfrac{C_V}{T}$ と熱力学第三法則 $S(T = 0) = 0$ を用いて，$T < T_{\mathrm{c}}$ における単位体積あたりのエントロピー $S$ を求めます。

$$
\begin{aligned}
S(T) &= \int_0^T \frac{C_V(T')}{T'}\,\mathrm{d}T' \\
&= \frac{5}{2} A I_{3/2} k_{\mathrm{B}}^{\frac{5}{2}} \int_0^T (T')^{\frac{1}{2}}\,\mathrm{d}T' \\
&= \frac{5}{3} A I_{3/2} k_{\mathrm{B}}^{\frac{5}{2}}\,T^{\frac{3}{2}}
\end{aligned}
$$

したがって，$S \propto T^{3/2}$ であり，$\nu = \dfrac{3}{2}$ です。

$$
\finalanswer{\nu = \frac{3}{2}}
$$

### (6)
スピン $1$ の系では，式 (6) の状態密度 $\tilde{D}(\epsilon) = D(\epsilon - \epsilon_{\mathrm{Z}}) + D(\epsilon) + D(\epsilon + \epsilon_{\mathrm{Z}})$ に対応する 3 つのスピン状態があり，一粒子エネルギーの下限は $-\epsilon_{\mathrm{Z}}$ です。常にボース・アインシュタイン凝縮が起きているので，化学ポテンシャルは最低エネルギーである $\mu = -\epsilon_{\mathrm{Z}}$ に固定されます。

単位体積あたりの内部エネルギー $\tilde{E}$ は，最低エネルギー準位を基準とした励起エネルギー $\tilde{\epsilon} = \epsilon + \epsilon_{\mathrm{Z}} \ge 0$ を用いると，3 つのスピン成分の和になります。$\epsilon = \tilde{\epsilon} - \epsilon_{\mathrm{Z}}$ より，各成分の励起スペクトルはそれぞれ $\tilde{\epsilon} \ge 0$，$\tilde{\epsilon} \ge \epsilon_{\mathrm{Z}}$，$\tilde{\epsilon} \ge 2\epsilon_{\mathrm{Z}}$ から始まります。

始状態の温度を $T_1$，終状態の温度を $T_2$ とします。スピン $0$ の理想ボース気体の $T < T_{\mathrm{c}}$ における単位体積あたりのエントロピーを $S_0(T) = c T^{3/2}$ とおきます。ここで $c = \dfrac{5}{3} A I_{3/2} k_{\mathrm{B}}^{5/2} > 0$ です。

- 始状態では $\epsilon_{\mathrm{Z},1} \ll k_{\mathrm{B}} T_1$ なので，3 つのスピン成分のエネルギー差は熱エネルギーに比べて無視することができ，$\tilde{D}(\epsilon) \simeq 3 D(\epsilon + \epsilon_{\mathrm{Z},1})$ となります。よって 3 成分すべてが等しくエントロピーに寄与し，始状態のエントロピー $S_1$ はおよそ $3 S_0(T_1) = 3 c T_1^{3/2}$ です。
- 終状態では $\epsilon_{\mathrm{Z},2} \gg k_{\mathrm{B}} T_2$ なので，上側の 2 つのスピン成分の分布関数 $f(\epsilon)$ は $e^{-\epsilon_{\mathrm{Z},2}/(k_{\mathrm{B}} T_2)}$ や $e^{-2\epsilon_{\mathrm{Z},2}/(k_{\mathrm{B}} T_2)}$ の因子で強く抑えられ，エントロピーへの寄与は無視することができます。よって最低のスピン成分のみが寄与し，終状態のエントロピー $S_2$ はおよそ $S_0(T_2) = c T_2^{3/2}$ です。

断熱変化ではエントロピーが減少しません。特に準静的な断熱変化では $S_2 = S_1$ が成り立つので，次式が得られます。

$$
\begin{aligned}
c T_2^{\frac{3}{2}} &\simeq 3 c T_1^{\frac{3}{2}} \\
T_2 &\simeq 3^{\frac{2}{3}} T_1 > T_1
\end{aligned}
$$

非可逆な断熱変化であっても $S_2 \ge S_1$ なので $T_2$ はさらに高くなります。したがって，終状態の温度は始状態の温度より**高い**です。
