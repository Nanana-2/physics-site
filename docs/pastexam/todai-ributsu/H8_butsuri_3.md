---
title: 東大理物 平成8年度 物理学 第3問：1次元自由電子系の古典統計とフェルミ統計における常磁性
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成8年度 物理学 第3問：1次元自由電子系の古典統計とフェルミ統計における常磁性

## 問題

一次元の自由電子系を考える。系の長さを $L$，温度を $T$，電子数を $N$ とする。一様な磁場 $H$ のもとで，ハミルトニアンは

$$
\mathcal{H} = \sum_{i=1}^{N}\left(\frac{p_i^2}{2m} - \mu_i H\right)
$$

と書かれるものとする。ただし，$m$ は電子の質量，$p_i$，$\mu_i$ はそれぞれ $i$ 番目の電子の運動量とスピン磁気モーメントであり，$\mu_i$ は $\pm\mu_{\mathrm{B}}$（$\mu_{\mathrm{B}}$ はボーア磁子）の値だけをとる。また，$L$ は十分大きくて，電子状態に対する系の境界の影響は無視できるものとする。
{: .problem-lead }

(1) 電子はボルツマン統計に従うものと仮定して次の問に答えよ。

(a) $H = 0$ の場合に，カノニカルアンサンブルにおける分配関数を求めよ。

(b) それを用いて系の内部エネルギーを求めよ。

(c) $H \neq 0$ の場合は分配関数はどう書かれるか。

(d) それを用いて比熱を求めよ。

(e) 系の磁化 $M = \sum_i \langle \mu_i \rangle / L$ と $H$ の間の関係を求めよ。ただし，$\langle\ \rangle$ は熱平均を表わす。

(f) 帯磁率 $\chi = \lim_{H \to 0}(M / H)$ を求めよ。

(2) 電子がフェルミ統計に従うことを考慮して次の問に答えよ。

(a) $T = 0$，$H = 0$ における系の内部エネルギーをフェルミエネルギー $\varepsilon_{\mathrm{F}}$ と $N$ を用いて表わせ。

(b) $T = 0$ において，磁化 $M$ と磁場 $H$ の間の関係を求めよ。（結果は，$\mu_{\mathrm{B}} H$ と $2\varepsilon_{\mathrm{F}}$ の大小関係によって異なることに注意せよ。）

(c) 帯磁率 $\chi$ を求めよ。(1) の (f) で求めた $\chi$ の $T = 0$ における振舞いとの違いについて，物理的な理由をつけて説明せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
1次元自由電子系の熱力学・磁気的性質を，古典的なボルツマン統計と量子的なフェルミ統計の双方で比較する問題です。ボルツマン統計では並進自由度とスピン自由度の分配関数が積に分離するため，内部エネルギー・ショットキー比熱やキュリー則が導かれます。一方，フェルミ統計の絶対零度では1次元状態密度が $E^{-1/2}$ に比例することから，磁場中のスピン分極が飽和磁場 $2\varepsilon_{\mathrm{F}}/\mu_{\mathrm{B}}$ まで厳密に磁場に比例し，パウリの排他律によって絶対零度でも有限なパウリ常磁性帯磁率が得られます。
</div>

### (1)(a)

ボルツマン統計に従う $N$ 個の同種粒子系について，$\beta = \dfrac{1}{k_{\mathrm{B}} T}$ とおきます。$H = 0$ のとき各粒子は1次元の並進自由度に加えてスピン自由度 $\mu_i = \pm\mu_{\mathrm{B}}$ の2状態をもつため，1粒子あたりの分配関数 $z_1(0)$ は位相空間積分とスピン和から次のように計算されます。

$$
\begin{aligned}
z_1(0) &= \sum_{\mu = \pm\mu_{\mathrm{B}}} \int_0^L \mathrm{d}x \int_{-\infty}^{\infty} \frac{\mathrm{d}p}{h}\exp\left(-\beta\frac{p^2}{2m}\right) \\
&= 2 \cdot \frac{L}{h}\sqrt{\frac{2\pi m}{\beta}} \\
&= 2 L \sqrt{\frac{2\pi m k_{\mathrm{B}} T}{h^2}}
\end{aligned}
$$

電子は互いに区別できない同種粒子なので，ギブスの因子 $\dfrac{1}{N!}$ を付けて $N$ 粒子系の分配関数 $Z(0)$ が得られます。

$$
\finalanswer{Z(0) = \frac{1}{N!}\left(2 L \sqrt{\frac{2\pi m k_{\mathrm{B}} T}{h^2}}\right)^N}
$$

### (1)(b)

分配関数 $Z(0)$ の対数をとると，$\beta$ に依存する項は $-\dfrac{N}{2}\ln\beta$ のみです。

$$
\ln Z(0) = -\frac{N}{2}\ln\beta + \text{const.}
$$

したがって系の内部エネルギー $U$ は次式で与えられます。

$$
\begin{aligned}
U &= -\frac{\partial}{\partial\beta}\ln Z(0) \\
&= \frac{N}{2\beta} \\
&= \frac{1}{2} N k_{\mathrm{B}} T
\end{aligned}
$$

これは1次元自由粒子のエネルギー等分配則と一致します。

$$
\finalanswer{U = \frac{1}{2} N k_{\mathrm{B}} T}
$$

### (1)(c)

$H \neq 0$ のとき，1粒子分配関数 $z_1(H)$ のスピン和にボルツマン因子 $e^{\beta\mu H}$ が加わります。

$$
\begin{aligned}
\sum_{\mu = \pm\mu_{\mathrm{B}}} e^{\beta\mu H} &= e^{\beta\mu_{\mathrm{B}} H} + e^{-\beta\mu_{\mathrm{B}} H} \\
&= 2\cosh\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)
\end{aligned}
$$

並進部分の積分は (1)(a) と同じなので，$N$ 粒子系の分配関数 $Z(H)$ は次のようになります。

$$
\finalanswer{Z(H) = \frac{1}{N!}\left[2 L \sqrt{\frac{2\pi m k_{\mathrm{B}} T}{h^2}}\cosh\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)\right]^N}
$$

### (1)(d)

$\ln Z(H)$ から磁場 $H$ 一定のもとでの内部エネルギー $U(H)$ を求めます。

$$
\ln Z(H) = -\frac{N}{2}\ln\beta + N\ln\cosh(\beta\mu_{\mathrm{B}} H) + \text{const.}
$$

$$
\begin{aligned}
U(H) &= -\left(\frac{\partial \ln Z(H)}{\partial\beta}\right)_H \\
&= \frac{1}{2} N k_{\mathrm{B}} T - N \mu_{\mathrm{B}} H \tanh\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)
\end{aligned}
$$

これを磁場 $H$ 一定のもとで温度 $T$ で微分して比熱 $C$ を計算します。

$$
\begin{aligned}
C &= \left(\frac{\partial U(H)}{\partial T}\right)_H \\
&= \frac{1}{2} N k_{\mathrm{B}} - N\mu_{\mathrm{B}} H \cdot \frac{1}{\cosh^2\left(\dfrac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)}\cdot\left(-\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T^2}\right) \\
&= \frac{1}{2} N k_{\mathrm{B}} + N k_{\mathrm{B}}\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)^2 \operatorname{sech}^2\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)
\end{aligned}
$$

第1項は1次元並進運動の比熱，第2項は2準位スピン系によるショットキー比熱です。なお単位長さあたりまたは1粒子あたりの比熱として定義する場合はそれぞれ $L$ または $N$ で割った量になります。

$$
\finalanswer{C = \frac{1}{2} N k_{\mathrm{B}} + N k_{\mathrm{B}}\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)^2 \operatorname{sech}^2\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)}
$$

### (1)(e)

分配関数 $Z(H)$ の定義から，磁化 $M = \dfrac{1}{L}\sum_{i=1}^{N}\langle\mu_i\rangle$ は自由エネルギー $F = -k_{\mathrm{B}} T \ln Z(H)$ の磁場微分として得られます。

$$
\begin{aligned}
M &= \frac{1}{L\beta}\left(\frac{\partial \ln Z(H)}{\partial H}\right)_T \\
&= \frac{N}{L\beta}\cdot\beta\mu_{\mathrm{B}}\tanh(\beta\mu_{\mathrm{B}} H) \\
&= \frac{N\mu_{\mathrm{B}}}{L}\tanh\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)
\end{aligned}
$$

$$
\finalanswer{M = \frac{N\mu_{\mathrm{B}}}{L}\tanh\left(\frac{\mu_{\mathrm{B}} H}{k_{\mathrm{B}} T}\right)}
$$

### (1)(f)

$H \to 0$ の極限では $\tanh x = x + O(x^3)$ を用いて帯磁率 $\chi$ を求めます。

$$
\begin{aligned}
\chi &= \lim_{H \to 0}\frac{M}{H} \\
&= \frac{N\mu_{\mathrm{B}}^2}{L k_{\mathrm{B}} T}
\end{aligned}
$$

このようにボルツマン統計では温度に反比例するキュリーの法則が得られます。

$$
\finalanswer{\chi = \frac{N\mu_{\mathrm{B}}^2}{L k_{\mathrm{B}} T}}
$$

### (2)(a)

長さ $L$ の1次元系に周期的境界条件を課すと，整数 $n \in \mathbb{Z}$ に対して波数 $k = \dfrac{2\pi n}{L}$ が間隔 $\dfrac{2\pi}{L}$ で分布します。$L$ が十分大きいので和を積分に置き換えることができます。1粒子エネルギーは $\varepsilon(k) = \dfrac{\hbar^2 k^2}{2m}$ です。

$T = 0$，$H = 0$ では各スピン状態につき $|k| \le k_{\mathrm{F}}$ の状態がすべて占有されます。ここでフェルミ波数 $k_{\mathrm{F}}$ は $\varepsilon_{\mathrm{F}} = \dfrac{\hbar^2 k_{\mathrm{F}}^2}{2m}$ で定義されます。全電子数 $N$ はスピン縮退度 $2$ を掛けて次のように表されます。

$$
\begin{aligned}
N &= 2 \cdot \frac{L}{2\pi}\int_{-k_{\mathrm{F}}}^{k_{\mathrm{F}}} \mathrm{d}k \\
&= \frac{2 L k_{\mathrm{F}}}{\pi}
\end{aligned}
$$

同様に，系の全内部エネルギー $U$ を計算します。

$$
\begin{aligned}
U &= 2 \cdot \frac{L}{2\pi}\int_{-k_{\mathrm{F}}}^{k_{\mathrm{F}}} \frac{\hbar^2 k^2}{2m}\,\mathrm{d}k \\
&= \frac{L\hbar^2}{\pi m}\cdot\frac{k_{\mathrm{F}}^3}{3} \\
&= \frac{1}{3}\left(\frac{2 L k_{\mathrm{F}}}{\pi}\right)\left(\frac{\hbar^2 k_{\mathrm{F}}^2}{2m}\right) \\
&= \frac{1}{3} N \varepsilon_{\mathrm{F}}
\end{aligned}
$$

$$
\finalanswer{U = \frac{1}{3} N \varepsilon_{\mathrm{F}}}
$$

### (2)(b)

まず $H \ge 0$ の場合を考えます。磁場中での電子の1粒子エネルギーは，スピン磁気モーメントが $+\mu_{\mathrm{B}}$ の上向きスピンでは $\varepsilon_+(k) = \dfrac{\hbar^2 k^2}{2m} - \mu_{\mathrm{B}} H$，$-\mu_{\mathrm{B}}$ の下向きスピンでは $\varepsilon_-(k) = \dfrac{\hbar^2 k^2}{2m} + \mu_{\mathrm{B}} H$ となります。絶対零度 $T = 0$ では，両スピン成分とも同じ化学ポテンシャル $\mu$ 以下のすべてのエネルギー状態が占有されます。

まず両方のスピン状態がともに占有される場合，すなわち $\mu \ge \mu_{\mathrm{B}} H$ の場合を考えます。それぞれのスピン成分のフェルミ波数 $k_+, k_-$ は

$$
\frac{\hbar^2 k_+^2}{2m} = \mu + \mu_{\mathrm{B}} H, \qquad \frac{\hbar^2 k_-^2}{2m} = \mu - \mu_{\mathrm{B}} H
$$

を満たします。上向き・下向きスピンの電子数 $N_+, N_-$ は1スピンあたりの関係 $N_\pm = \dfrac{L k_\pm}{\pi}$ と (2)(a) の $N = \dfrac{2L k_{\mathrm{F}}}{\pi}$ を用いると次のように表されます。

$$
N_+ = \frac{N}{2}\sqrt{\frac{\mu + \mu_{\mathrm{B}} H}{\varepsilon_{\mathrm{F}}}}, \qquad N_- = \frac{N}{2}\sqrt{\frac{\mu - \mu_{\mathrm{B}} H}{\varepsilon_{\mathrm{F}}}}
$$

無次元量 $x_+ = \sqrt{\dfrac{\mu + \mu_{\mathrm{B}} H}{\varepsilon_{\mathrm{F}}}}$ と $x_- = \sqrt{\dfrac{\mu - \mu_{\mathrm{B}} H}{\varepsilon_{\mathrm{F}}}}$ を導入すると，全電子数の保存 $N_+ + N_- = N$ とエネルギー差の条件は次の2式になります。

$$
\begin{aligned}
x_+ + x_- &= 2 \\
x_+^2 - x_-^2 &= \frac{2\mu_{\mathrm{B}} H}{\varepsilon_{\mathrm{F}}}
\end{aligned}
$$

第2式を因数分解して第1式を代入すると，

$$
2(x_+ - x_-) = \frac{2\mu_{\mathrm{B}} H}{\varepsilon_{\mathrm{F}}}
$$

すなわち $x_+ - x_- = \dfrac{\mu_{\mathrm{B}} H}{\varepsilon_{\mathrm{F}}}$ が得られます。これと $x_+ + x_- = 2$ から $x_\pm$ が厳密に決まります。

$$
x_+ = 1 + \frac{\mu_{\mathrm{B}} H}{2\varepsilon_{\mathrm{F}}}, \qquad x_- = 1 - \frac{\mu_{\mathrm{B}} H}{2\varepsilon_{\mathrm{F}}}
$$

$x_- \ge 0$ の条件は $\mu_{\mathrm{B}} H \le 2\varepsilon_{\mathrm{F}}$ です。この範囲では磁化 $M = \dfrac{\mu_{\mathrm{B}}(N_+ - N_-)}{L}$ は次の通り $H$ に厳密に比例します。

$$
\begin{aligned}
M &= \frac{N\mu_{\mathrm{B}}}{2L}(x_+ - x_-) \\
&= \frac{N\mu_{\mathrm{B}}^2 H}{2 L \varepsilon_{\mathrm{F}}}
\end{aligned}
$$

一方，$\mu_{\mathrm{B}} H > 2\varepsilon_{\mathrm{F}}$ となると $N_- = 0$，$N_+ = N$ となりすべての電子のスピンが磁場方向に揃う完全分極状態に達します。このとき磁化は飽和値

$$
M = \frac{N\mu_{\mathrm{B}}}{L}
$$

をとります。$H < 0$ の場合は対称性 $M(-H) = -M(H)$ により符号が反転します。以上をまとめると次のようになります。

$$
\finalanswer{M = \begin{cases} \dfrac{N\mu_{\mathrm{B}}^2 H}{2 L \varepsilon_{\mathrm{F}}} & (|\mu_{\mathrm{B}} H| \le 2\varepsilon_{\mathrm{F}}) \\[10pt] \operatorname{sgn}(H)\dfrac{N\mu_{\mathrm{B}}}{L} & (|\mu_{\mathrm{B}} H| > 2\varepsilon_{\mathrm{F}}) \end{cases}}
$$

### (2)(c)

(2)(b) で得た結果より，$T = 0$ におけるフェルミ電子系のパウリ常磁性帯磁率 $\chi$ は次式となります。

$$
\begin{aligned}
\chi &= \lim_{H \to 0}\frac{M}{H} \\
&= \frac{N\mu_{\mathrm{B}}^2}{2 L \varepsilon_{\mathrm{F}}}
\end{aligned}
$$

(1)(f) で得たボルツマン統計の帯磁率 $\chi_{\mathrm{cl}} = \dfrac{N\mu_{\mathrm{B}}^2}{L k_{\mathrm{B}} T}$ は $T \to 0$ で無限大に発散するのに対し，フェルミ統計の帯磁率 $\chi = \dfrac{N\mu_{\mathrm{B}}^2}{2 L \varepsilon_{\mathrm{F}}}$ は $T = 0$ でも温度によらない有限の定数にとどまります。

この違いの物理的理由はパウリの排他律にあります。ボルツマン統計ではすべての電子が同じ低い運動量状態を占めることができるため，絶対零度では微小な磁場をかけるだけで全電子のスピンが一斉に磁場方向へ向きを揃え，帯磁率が発散します。これに対してフェルミ統計では，パウリの排他律によって1つの量子状態に同じスピンの電子は1個しか入れず，フェルミ準位より十分下にある電子はスピンを反転させようとしても移る先の同じ運動量状態がすでに占有されているため向きを変えられません。磁場に応じてスピンを反転して磁化に寄与できるのはフェルミエネルギー $\varepsilon_{\mathrm{F}}$ 近傍の幅 $\sim \mu_{\mathrm{B}} H$ にある一部の電子のみであり，その割合はおよそ $\mu_{\mathrm{B}} H / \varepsilon_{\mathrm{F}}$ に抑えられるため，$T = 0$ における帯磁率は古典結果の $k_{\mathrm{B}} T$ を $2\varepsilon_{\mathrm{F}}$ で置き換えた有限値にとどまります。

$$
\finalanswer{\chi = \frac{N\mu_{\mathrm{B}}^2}{2 L \varepsilon_{\mathrm{F}}}}
$$
