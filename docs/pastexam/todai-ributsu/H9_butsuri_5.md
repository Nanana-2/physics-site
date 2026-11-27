---
title: 東大理物 平成9年度 物理学 第5問：局在電子相と縮退フェルミ気体相の1次相転移と臨界点
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
  - 物性物理学
  - 熱力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 物理学
exam_number: 第5問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成9年度 物理学 第5問：局在電子相と縮退フェルミ気体相の1次相転移と臨界点

## 問題

結晶中の各原子（単位体積あたりの個数を $n$ とする）に1個ずつ電子が存在し，隣り合った原子の間で電子が弱く相互作用している系がある。ある温度 $T = T_t$ で，この系は1次相転移を示し，$T \ge T_t$ の相（高温相）では，各原子に1個ずつ捕えられた相互作用のない電子からなる系と同じ比熱と帯磁率を示した。$T \le T_t$ の相（低温相）では，弱い原子間の相互作用が摂動となり電子がある小さな確率で原子間をとび移るために，比熱，帯磁率は縮態した自由電子ガスと同じ温度依存性を示した。しかし，その比熱の絶対値は，自由電子ガスの比熱の表式において，自由電子の質量 $m_e$ をより大きな値 $m^*$（有効質量と呼ぶ）に置き換えたもので表わされた。十分低温のため，格子比熱，各相での熱膨張は無視できるものとして，次の問に答えよ。
{: .problem-lead }

(1) 高温相の単位体積あたりの帯磁率，磁場中での比熱を求めよ。磁場 $\vec{H}$ と電子の相互作用を表わすハミルトニアンは，

$$
\mathcal{H}_Z = \sum_i 2\mu_{\mathrm{B}}\vec{H}\cdot\vec{S}_i \qquad \text{(1)}
$$

で与えられるとする。ここで，$\mu_{\mathrm{B}} \equiv e\hbar/2m_e c$ は電子のボーア磁子，$\vec{S}_i$ は電子 $i$ のスピン演算子を表わす。

(2) 低温相の単位体積あたりの比熱は，温度 $T$ の最低次までで，

$$
c_p = \frac{k_{\mathrm{B}}^2 m^*}{3\hbar^2}\left(\frac{3n}{8\pi}\right)^{1/3} T \qquad \text{(2)}
$$

と与えられた（$k_{\mathrm{B}}$：ボルツマン定数）。式 (2) が温度に比例する理由を，有限温度のフェルミ分布関数を用いて定性的に説明せよ。

以下では，簡単のため (1)，(2) で求めた両相の比熱の表式が転移点 $T_t$ 近傍まで使えるものとし，磁場はかかっていないものとする。

(3) 上記の1次転移が起こるには，エントロピーの考察から，有効質量 $m^*$ と相転移温度 $T_t$ がどのような条件を満たさなければならないか？

(4) 今，この電子系に圧力 $P$ をかけたところ，相転移温度 $T_t$ が上昇し，低温相の比熱より求まる有効質量 $m^*$ が減少した（図参照）。有効質量および相転移温度の圧力依存性は，$m_0^*$，$T_{t0}$ を $P = 0$ での有効質量，転移温度として，

$$
\begin{aligned}
m^* &= m_0^*(1 + aP)^{-1} \qquad \text{(3)} \\
T_t &= T_{t0}(1 + bP) \qquad \text{(4)}
\end{aligned}
$$

（$a > 0, b > 0$）の実験式で与えられた。ある圧力 $P = P_c$（臨界圧力）以上で1次転移が消失するのは，$a, b$ がどのような条件を満たす場合か？

(5) $P_c$，および転移の消失する温度 $T = T_c$（臨界温度）を，$a, b, m_0^*, T_{t0}$ を用いて表わせ。

<figure class="problem-figure" markdown>
![圧力Pと温度Tの相図および1次相転移線と臨界点(P_c, T_c)](../../assets/figures/pastexam-todai-ributsu/H9_butsuri_5-p-light.svg#only-light){ loading=lazy }
![圧力Pと温度Tの相図および1次相転移線と臨界点(P_c, T_c)](../../assets/figures/pastexam-todai-ributsu/H9_butsuri_5-p-dark.svg#only-dark){ loading=lazy }
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 物理学 第5問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
高温相は各格子点に1個ずつ局在した独立なスピン $1/2$ の集まりなので，1電子のゼーマン準位 $\pm\mu_{\mathrm{B}}H$ に対する分配関数から帯磁率と磁場中比熱を直接計算します。

ゼロ磁場での1次相転移では，低温相から高温相へ移るときに潜熱 $T_t(s_{\mathrm{H}} - s_{\mathrm{L}}) > 0$ が吸収される必要があるため，低温相のエントロピー $\int_0^{T_t} \dfrac{c_p}{T}\,\mathrm{d}T$ が高温相のスピンエントロピー $n k_{\mathrm{B}}\ln 2$ より小さくなければなりません。圧力を上げて両相のエントロピーが等しくなる点として臨界圧力 $P_c$ と臨界温度 $T_c$ を決定します。
</div>

### (1)

磁場 $\vec{H}$ の向きを $z$ 軸にとります。式 (1) のスピン演算子 $\vec{S}_i$ は無次元の大きさ $1/2$ のスピン演算子なので，各電子の $S_i^z$ の固有値は $+\dfrac{1}{2}$ と $-\dfrac{1}{2}$ です。したがって1電子のエネルギー固有値は $+\mu_{\mathrm{B}}H$ と $-\mu_{\mathrm{B}}H$ になります。

逆温度を $\beta = \dfrac{1}{k_{\mathrm{B}}T}$ とすると，1電子の分配関数 $Z_1$ は次の通りです。

$$
\begin{aligned}
Z_1 &= e^{-\beta\mu_{\mathrm{B}}H} + e^{\beta\mu_{\mathrm{B}}H} \\
&= 2\cosh(\beta\mu_{\mathrm{B}}H)
\end{aligned}
$$

単位体積当たり $n$ 個の局在電子は区別でき互いに独立であるため，単位体積当たりの分配関数は $Z = Z_1^n$ です。単位体積当たりのヘルムホルツ自由エネルギー $f = -\dfrac{1}{\beta}\ln Z$ を求めます。

$$
f = -\frac{n}{\beta}\ln\bigl(2\cosh(\beta\mu_{\mathrm{B}}H)\bigr)
$$

単位体積当たりの磁化 $M = -\left(\dfrac{\partial f}{\partial H}\right)_T$ を計算します。

$$
\begin{aligned}
M &= \frac{n}{\beta}\frac{\beta\mu_{\mathrm{B}}\sinh(\beta\mu_{\mathrm{B}}H)}{\cosh(\beta\mu_{\mathrm{B}}H)} \\
&= n\mu_{\mathrm{B}}\tanh\left(\frac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

これより弱磁場極限 $H \to 0$ での単位体積当たりの帯磁率 $\chi = \lim_{H \to 0}\dfrac{M}{H}$ は，$|x| \ll 1$ での近似 $\tanh x \approx x$ を用いて次のように求まります。

$$
\chi = \frac{n\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T}
$$

なお有限磁場 $H$ における微分帯磁率 $\chi(H) = \left(\dfrac{\partial M}{\partial H}\right)_T$ は $\dfrac{n\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T\cosh^2(\mu_{\mathrm{B}}H/(k_{\mathrm{B}}T))}$ です。

次に磁場中での単位体積当たりの内部エネルギー $u = -\dfrac{\partial\ln Z}{\partial\beta}$ を求めます。

$$
\begin{aligned}
u &= -n\frac{\partial}{\partial\beta}\ln\bigl(2\cosh(\beta\mu_{\mathrm{B}}H)\bigr) \\
&= -n\mu_{\mathrm{B}}H\tanh\left(\frac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

これを $T$ で偏微分して，磁場中での単位体積当たりの比熱 $c_H = \left(\dfrac{\partial u}{\partial T}\right)_H$ を計算します。

$$
\begin{aligned}
c_H &= -n\mu_{\mathrm{B}}H \cdot \frac{1}{\cosh^2\left(\dfrac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)}\left(-\frac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T^2}\right) \\
&= n k_{\mathrm{B}}\left(\frac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)^2\frac{1}{\cosh^2\left(\dfrac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)}
\end{aligned}
$$

$$
\finalanswer{\chi = \frac{n\mu_{\mathrm{B}}^2}{k_{\mathrm{B}}T},\qquad c_H = n k_{\mathrm{B}}\left(\frac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)^2\frac{1}{\cosh^2\left(\dfrac{\mu_{\mathrm{B}}H}{k_{\mathrm{B}}T}\right)}}
$$

### (2)

有限温度 $T$ におけるフェルミ分布関数は，化学ポテンシャルを $\mu$ として

$$
f(\varepsilon) = \frac{1}{e^{(\varepsilon - \mu)/(k_{\mathrm{B}}T)} + 1}
$$

で与えられます。$T = 0$ ではフェルミエネルギー $\varepsilon_{\mathrm{F}}$ 以下の状態が占有率 $1$，それより上の状態が占有率 $0$ となる階段関数です。

温度が $k_{\mathrm{B}}T \ll \varepsilon_{\mathrm{F}}$ を満たす $T > 0$ に上がると，フェルミ分布関数 $f(\varepsilon)$ が $T = 0$ から変化するのは，$\varepsilon_{\mathrm{F}}$ を中心とする幅 $k_{\mathrm{B}}T$ 程度のエネルギー範囲に限られます。$\varepsilon_{\mathrm{F}}$ より十分低い準位にある電子は，すぐ上の準位がすでに他の電子で占有されているためパウリの排他原理によって熱励起することができません。

したがって，熱励起に関与できる単位体積当たりの電子数 $\Delta n$ は，フェルミエネルギー付近の状態密度 $D(\varepsilon_{\mathrm{F}})$ に幅 $k_{\mathrm{B}}T$ を掛けた $D(\varepsilon_{\mathrm{F}})k_{\mathrm{B}}T$ 程度となります。これらの電子がそれぞれ熱エネルギー $k_{\mathrm{B}}T$ 程度を受け取るため，温度 $T$ での内部エネルギーの増加分 $\Delta u$ は

$$
\Delta u \sim D(\varepsilon_{\mathrm{F}})(k_{\mathrm{B}}T)^2 \propto T^2
$$

となります。これを温度 $T$ で微分した比熱 $c_p = \dfrac{\partial u}{\partial T}$ は $D(\varepsilon_{\mathrm{F}})k_{\mathrm{B}}^2 T$ 程度となり，温度 $T$ に比例します。また3次元自由電子気体では $D(\varepsilon_{\mathrm{F}}) \propto m^* n^{1/3}$ となるため，比熱係数は有効質量 $m^*$ に比例します。

### (3)

磁場がかかっていない $H = 0$ の場合を考えます。熱力学第3法則より $T = 0$ における低温相のエントロピーは $0$ なので，温度 $T$ における低温相の単位体積当たりのエントロピー $s_{\mathrm{L}}(T)$ は式 (2) を積分して求めます。

$$
\begin{aligned}
s_{\mathrm{L}}(T) &= \int_0^T \frac{c_p(T')}{T'}\,\mathrm{d}T' \\
&= \frac{k_{\mathrm{B}}^2 m^*}{3\hbar^2}\left(\frac{3n}{8\pi}\right)^{1/3} T
\end{aligned}
$$

一方，高温相では (1) の結果で $H = 0$ とすると $c_H = 0$ です。各原子に局在した $n$ 個の独立なスピン $1/2$ 電子は上向きと下向きの2状態を自由にとるため，単位体積当たりの微視的状態数は $W = 2^n$ となり，高温相の単位体積当たりのエントロピー $s_{\mathrm{H}}$ は温度によらず一定値になります。

$$
\begin{aligned}
s_{\mathrm{H}} &= k_{\mathrm{B}}\ln(2^n) \\
&= n k_{\mathrm{B}}\ln 2
\end{aligned}
$$

温度 $T = T_t$ において $T \le T_t$ の低温相から $T \ge T_t$ の高温相への1次相転移が起こるためには，$T < T_t$ で $g_{\mathrm{L}} < g_{\mathrm{H}}$，$T > T_t$ で $g_{\mathrm{H}} < g_{\mathrm{L}}$ が成り立つ必要があります。ギブズ自由エネルギーの差の傾きは $\dfrac{\partial(g_{\mathrm{H}} - g_{\mathrm{L}})}{\partial T} = -(s_{\mathrm{H}} - s_{\mathrm{L}})$ なので，転移点 $T = T_t$ で高温相のエントロピーが低温相のエントロピーより厳密に大きいこと，すなわち正の潜熱 $T_t(s_{\mathrm{H}} - s_{\mathrm{L}}(T_t)) > 0$ をもつことが必要です。

$$
s_{\mathrm{L}}(T_t) < s_{\mathrm{H}}
$$

両辺に上の表式を代入して $m^* T_t$ について解きます。

$$
\begin{aligned}
\frac{k_{\mathrm{B}}^2 m^*}{3\hbar^2}\left(\frac{3n}{8\pi}\right)^{1/3} T_t &< n k_{\mathrm{B}}\ln 2 \\
m^* T_t &< \frac{3\hbar^2 n\ln 2}{k_{\mathrm{B}}}\left(\frac{8\pi}{3n}\right)^{1/3}
\end{aligned}
$$

右辺の $n$ のべきを整理すると $3n\left(\dfrac{8\pi}{3n}\right)^{1/3} = 2(9\pi n^2)^{1/3}$ となります。

$$
\finalanswer{m^* T_t < \frac{2\hbar^2\ln 2}{k_{\mathrm{B}}}(9\pi n^2)^{1/3}}
$$

### (4)

(3) の右辺の定数を

$$
K \equiv \frac{2\hbar^2\ln 2}{k_{\mathrm{B}}}(9\pi n^2)^{1/3}
$$

とおきます。$P = 0$ で1次相転移が起きているため，初期条件として $m_0^* T_{t0} < K$ が成り立っています。

圧力 $P$ を加えたときの積 $m^*(P)T_t(P)$ を式 (3) と式 (4) から計算します。

$$
m^*(P)T_t(P) = m_0^* T_{t0}\frac{1 + bP}{1 + aP}
$$

ある有限の正の圧力 $P = P_c$ で1次相転移がなくなるのは，圧力増加に伴って低温相のエントロピーが高温相のエントロピーに追いつき，潜熱が $0$ になる点，すなわち

$$
m^*(P_c)T_t(P_c) = K
$$

を満たす $P_c > 0$ が存在するときです。関数 $h(P) = \dfrac{1 + bP}{1 + aP}$ は $P = 0$ で $1$ をとり，$P \to \infty$ で $\dfrac{b}{a}$ へ単調に近づきます。したがって $m_0^* T_{t0} h(P)$ が $P > 0$ のどこかで $m_0^* T_{t0}$ より大きい $K$ に達するための必要十分条件は，$b > a$ となって $h(P)$ が単調増加であり，かつ $P \to \infty$ での上限が $K$ を超えることです。

$$
m_0^* T_{t0}\frac{b}{a} > K
$$

両辺を $m_0^* T_{t0}$ で割り，$K$ を戻します。

$$
\finalanswer{\frac{b}{a} > \frac{2\hbar^2\ln 2}{k_{\mathrm{B}} m_0^* T_{t0}}(9\pi n^2)^{1/3}}
$$

### (5)

臨界圧力 $P_c$ を決める方程式 $m_0^* T_{t0}\dfrac{1 + bP_c}{1 + aP_c} = K$ を $P_c$ について解きます。

$$
\begin{aligned}
m_0^* T_{t0}(1 + bP_c) &= K(1 + aP_c) \\
(b\,m_0^* T_{t0} - aK)P_c &= K - m_0^* T_{t0}
\end{aligned}
$$

したがって $P_c$ は次の通りです。

$$
P_c = \frac{K - m_0^* T_{t0}}{b\,m_0^* T_{t0} - aK}
$$

次に臨界温度 $T_c = T_{t0}(1 + bP_c)$ を計算します。

$$
\begin{aligned}
T_c &= T_{t0}\left(1 + \frac{b(K - m_0^* T_{t0})}{b\,m_0^* T_{t0} - aK}\right) \\
&= T_{t0}\frac{b\,m_0^* T_{t0} - aK + bK - b\,m_0^* T_{t0}}{b\,m_0^* T_{t0} - aK} \\
&= \frac{(b - a)K T_{t0}}{b\,m_0^* T_{t0} - aK}
\end{aligned}
$$

ここで $K = \dfrac{2\hbar^2\ln 2}{k_{\mathrm{B}}}(9\pi n^2)^{1/3}$ です。

$$
\finalanswer{P_c = \frac{K - m_0^* T_{t0}}{b\,m_0^* T_{t0} - aK},\qquad T_c = \frac{(b - a)K T_{t0}}{b\,m_0^* T_{t0} - aK},\qquad K = \frac{2\hbar^2\ln 2}{k_{\mathrm{B}}}(9\pi n^2)^{1/3}}
$$
