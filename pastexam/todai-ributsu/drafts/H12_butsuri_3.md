---
title: 東大理物 平成12年度 物理学 第3問：スピン1/2磁性体の断熱消磁
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成12年度 物理学 第3問：スピン1/2磁性体の断熱消磁

## 問題

低温を得る方法の1つに磁性体の断熱消磁がある。磁性体のモデルとして結晶格子の各格子点 $i$ に $1/2$ のスピンが存在する系を考える。磁性体と外部磁場 $H$ の相互作用は

$$
\mathcal{H}_1 = -\mu H \sum_i \sigma_i
$$

と表される。ただし $\sigma_i$ はスピンの向きに応じて $+1$ 又は $-1$ の値を取る変数で，$\mu$ は磁気モーメントである。以下の設問ではスピン以外の自由度は考えなくて良い。

まず，異なる格子点上のスピン間に相互作用が無いとして次の (1) から (3) の問いに答えよ
{: .problem-lead }

(1) 1格子点当たりの自由エネルギーとエントロピーを温度 $T$，磁場 $H$ の関数として求めよ。

(2) i) $H = 0$ の場合，ii) $H$ が有限で小さいとき，iii) $H$ が大きいとき，の3つの場合について，1格子点当たりのエントロピーを温度 $T$ の関数として定性的にグラフで示せ。

(3) 最初，磁場 $H_i$ のもとで，磁性体が温度 $T_i$ の熱浴と接して熱平衡状態にあった。次に熱浴との接触を断ち，磁性体を外界から孤立させて磁場を $H_f$ までゆっくり下げた。このときの磁性体の温度 $T_f$ を求めよ。

これまでは，スピン間の相互作用を無視しているため，(3) の問いで $H_f = 0$ とすると不合理な結果が生じる。一方現実の磁性体では，隣接する格子点上のスピンの間に相互作用が働き，このため低温で強磁性や反強磁性などの秩序状態が実現する。この事を考慮して以下の問いに答えよ。
{: .problem-lead }

(4) (3) の問いで $H_f = 0$ とすると，どのような不合理な結果が生じるか，述べよ。

(5) 現実の磁性体に対して $H_f = 0$ としたとき，磁性体の温度 $T_f$ はどうなるか，定性的に論じよ。

(6) 最近接格子点上のスピン間に強さ $J$ の相互作用があるとき，1格子点当たりの自由エネルギーは

$$
F = -kT\log 2 - \frac{(\mu H)^2 + J^2 z/2}{2kT}
$$

で与えられることが知られている。ここで，$k$ は Boltzmann 定数，$z$ は1つの格子点に対する最近接格子点の数である。

この系に対して，(3) の問いで述べた断熱消磁を実行した。この過程で系の状態は常にある温度に対するカノニカル分布で表されると仮定して，最終磁場 $H_f$ における温度 $T_f$ を $H_f$ の関数として求め（$0 \le H_f \le H_i$），結果を図示せよ。ただし $kT \gg \mu H \gg |J|\sqrt{z}$ と仮定する。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
相互作用のないスピン系では各格子点が独立なので，1格子点当たりの分配関数から自由エネルギーとエントロピーを直接計算することができ，エントロピーは比 $\mu H/(kT)$ のみの単調減少関数になります。

熱浴から切り離して磁場をゆっくり変化させる準静的断熱過程ではエントロピーが保存されるため，等エントロピー条件 $S(T_f, H_f) = S(T_i, H_i)$ から最終温度 $T_f$ が定まります。相互作用がある場合は，外部磁場が $0$ でもスピン間に有効な内部磁場が働くことに対応して，高温展開の自由エネルギーに $J^2 z/2$ の項が加わり，その等エントロピー条件から $H_f = 0$ でも有限の到達温度が求まります。
</div>

以下では問題文の記号に合わせて，ボルツマン定数を $k$，自然対数を $\ln$ で表します。

### (1)

異なる格子点のスピン間に相互作用がないため，1格子点当たりの分配関数 $Z_1$ は $\sigma = \pm 1$ の2状態の和になります。

$$
\begin{aligned}
Z_1 &= e^{\mu H/(kT)} + e^{-\mu H/(kT)} \\
&= 2\cosh\left(\frac{\mu H}{kT}\right)
\end{aligned}
$$

これより1格子点当たりの自由エネルギー $F(T, H) = -kT\ln Z_1$ を求めます。

$$
F(T, H) = -kT\ln\left[2\cosh\left(\frac{\mu H}{kT}\right)\right]
$$

1格子点当たりのエントロピー $S(T, H)$ は $S = -\left(\dfrac{\partial F}{\partial T}\right)_H$ を計算して求めます。

$$
\begin{aligned}
S(T, H) &= -\frac{\partial}{\partial T}\left\{-kT\ln\left[2\cosh\left(\frac{\mu H}{kT}\right)\right]\right\} \\
&= k\ln\left[2\cosh\left(\frac{\mu H}{kT}\right)\right] + kT\cdot\frac{\sinh\left(\dfrac{\mu H}{kT}\right)}{\cosh\left(\dfrac{\mu H}{kT}\right)}\cdot\left(-\frac{\mu H}{kT^2}\right) \\
&= k\ln\left[2\cosh\left(\frac{\mu H}{kT}\right)\right] - \frac{\mu H}{T}\tanh\left(\frac{\mu H}{kT}\right)
\end{aligned}
$$

したがって，1格子点当たりの自由エネルギーとエントロピーは次の通りです。

$$
\finalanswer{F(T, H) = -kT\ln\left[2\cosh\left(\frac{\mu H}{kT}\right)\right], \qquad S(T, H) = k\ln\left[2\cosh\left(\frac{\mu H}{kT}\right)\right] - \frac{\mu H}{T}\tanh\left(\frac{\mu H}{kT}\right)}
$$

### (2)

無次元変数 $x = \dfrac{\mu H}{kT}$ を用いると，エントロピーは $S = k\bigl[\ln(2\cosh x) - x\tanh x\bigr]$ です。$x$ に関する微分を計算します。

$$
\begin{aligned}
\frac{\mathrm{d}S}{\mathrm{d}x} &= k\left(\tanh x - \tanh x - \frac{x}{\cosh^2 x}\right) \\
&= -\frac{kx}{\cosh^2 x}
\end{aligned}
$$

よって $x > 0$ で $\dfrac{\mathrm{d}S}{\mathrm{d}x} < 0$ であり，$S$ は $x$ の単調減少関数です。

- (i) $H = 0$ のとき：すべての温度 $T > 0$ で $x = 0$ なので，$S(T) = k\ln 2$ の一定値になります。
- (ii) $H$ が有限で小さいとき：$T \to 0^+$ で $x \to +\infty$ となるため $S \approx 2kx e^{-2x} \to 0$ と指数関数的に $0$ へ近づき，$T$ の上昇とともに単調増加して $T \gg \mu H/k$ で $k\ln 2$ に漸近します。
- (iii) $H$ が大きいとき：同じ温度 $T$ での $x = \dfrac{\mu H}{kT}$ が (ii) より大きいため，すべての $T > 0$ で (ii) の曲線より下側を通り，より高い温度域 $T \sim \mu H/k$ にかけて $0$ から $k\ln 2$ へ単調増加します。

以上をまとめたグラフを下に示します。

<figure class="problem-figure" markdown>
![1格子点当たりのエントロピーの温度依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H12_butsuri_3-s1-light.svg#only-light){ loading=lazy }
![1格子点当たりのエントロピーの温度依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H12_butsuri_3-s1-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">1格子点当たりのエントロピー $S(T)$ の温度依存性。（i）$H = 0$（実線），（ii）$H$ が小さいとき（破線），（iii）$H$ が大きいとき（一点鎖線）。</figcaption>
</figure>

### (3)

孤立系で磁場をゆっくり変化させる過程は準静的な断熱過程なので，エントロピーは保存されます。

$$
S(T_f, H_f) = S(T_i, H_i)
$$

(2) で示したように，エントロピー $S$ は $x = \dfrac{\mu H}{kT}$ のみの狭義単調減少関数（$x \ge 0$）です。したがって，エントロピーが等しいことから前後の $x$ の値が一致します。

$$
\frac{\mu H_f}{kT_f} = \frac{\mu H_i}{kT_i}
$$

これを $T_f$ について解くと，最終温度 $T_f$ は次の通りです。

$$
\finalanswer{T_f = T_i\frac{H_f}{H_i}}
$$

### (4)

(3) の式で $H_f = 0$ とすると $T_f = 0$ となり，有限の操作で絶対零度に到達できるという結果になります。これは熱力学第3法則に反します。

グラフの上でも矛盾が生じます。無相互作用モデルでは $H = 0$ のエントロピーがすべての正の温度で $S(T, 0) = k\ln 2$ と一定であり，絶対零度付近で $0$ に下がらないため，初期状態のエントロピー $S(T_i, H_i) < k\ln 2$ を保った水平線は $H = 0$ の曲線と正の温度で交点をもたなくなってしまいます。

### (5)

現実の磁性体ではスピン間に相互作用が働くため，外部磁場が $H = 0$ であっても低温になるとスピンが自発的に秩序化して強磁性や反強磁性の状態に移行します。この秩序化によって $H = 0$ のエントロピー曲線 $S(T, 0)$ は，転移温度 $T_c \sim |J|/k$ のあたりから温度低下とともに $k\ln 2$ より下がり，$T \to 0$ で $0$ に収束して熱力学第3法則を満たします。

したがって，初期状態 $(T_i, H_i)$ からエントロピー一定の水平線をたどって $H_f = 0$ まで消磁しても，その水平線は $H = 0$ のエントロピー曲線と必ず正の温度で交わります。よって最終温度 $T_f$ は絶対零度には達せず，スピン間の相互作用の強さに対応する有限の正の温度（$T_f > 0$）にとどまります。

### (6)

与えられた1格子点当たりの自由エネルギー $F(T, H)$ を温度 $T$ で偏微分してエントロピー $S(T, H)$ を求めます。

$$
\begin{aligned}
S(T, H) &= -\left(\frac{\partial F}{\partial T}\right)_H \\
&= -\frac{\partial}{\partial T}\left[-kT\ln 2 - \frac{(\mu H)^2 + J^2 z/2}{2kT}\right] \\
&= k\ln 2 - \frac{(\mu H)^2 + J^2 z/2}{2kT^2}
\end{aligned}
$$

準静的な断熱消磁の過程ではエントロピーが保存されるため，$S(T_f, H_f) = S(T_i, H_i)$ が成り立ちます。

$$
k\ln 2 - \frac{(\mu H_f)^2 + J^2 z/2}{2kT_f^2} = k\ln 2 - \frac{(\mu H_i)^2 + J^2 z/2}{2kT_i^2}
$$

両辺の $k\ln 2$ と係数 $-\dfrac{1}{2k}$ を取り除きます。

$$
\frac{(\mu H_f)^2 + J^2 z/2}{T_f^2} = \frac{(\mu H_i)^2 + J^2 z/2}{T_i^2}
$$

$T_f > 0$ について解きます。

$$
\begin{aligned}
T_f^2 &= T_i^2\frac{(\mu H_f)^2 + J^2 z/2}{(\mu H_i)^2 + J^2 z/2} \\
T_f &= T_i\sqrt{\frac{(\mu H_f)^2 + J^2 z/2}{(\mu H_i)^2 + J^2 z/2}}
\end{aligned}
$$

したがって，最終温度 $T_f$ は次の通りです。

$$
\finalanswer{T_f = T_i\sqrt{\frac{(\mu H_f)^2 + J^2 z/2}{(\mu H_i)^2 + J^2 z/2}}}
$$

このグラフの特徴を確認します。$H_f = H_i$ では $T_f = T_i$ です。$\mu H_f \gg |J|\sqrt{z}$ の領域では無相互作用の直線 $T_f = T_i \dfrac{H_f}{H_i}$ にほぼ沿って減少しますが，$H_f$ が小さくなると直線の上側へ離れ，$H_f = 0$ では水平な接線 $\left.\dfrac{\mathrm{d}T_f}{\mathrm{d}H_f}\right|_{H_f=0} = 0$ をもって有限の正の温度 $T_f(0)$ に到達します。

$$
T_f(0) = T_i\frac{|J|\sqrt{z/2}}{\sqrt{(\mu H_i)^2 + J^2 z/2}} \approx T_i\frac{|J|\sqrt{z/2}}{\mu H_i}
$$

$T_f$ の $H_f$ 依存性（$0 \le H_f \le H_i$）を下に図示します。

<figure class="problem-figure" markdown>
![断熱消磁における最終温度の磁場依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H12_butsuri_3-s2-light.svg#only-light){ loading=lazy }
![断熱消磁における最終温度の磁場依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H12_butsuri_3-s2-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">スピン間相互作用がある場合の最終温度 $T_f$ の $H_f$ 依存性（実線）と，無相互作用の直線 $T_f = T_i H_f/H_i$（破線）。</figcaption>
</figure>

<aside class="rigor-note" markdown>
(6) の自由エネルギーの表式は，$kT \gg \mu H$ かつ $kT \gg |J|\sqrt{z}$ の高温展開から得られる近似式です。断熱消磁の最終状態でもこの近似が成り立つためには，$T_f(0) \gg |J|\sqrt{z}/k$，すなわち初期温度が $kT_i \gg \mu H_i$ を満たしていることが必要になります。なお，(6) で $J = 0$ とおくと $T_f = T_i H_f/H_i$ となり，(3) の結果と一致します。
</aside>
