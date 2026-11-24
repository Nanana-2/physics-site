---
title: 東大理物 平成30年度 物理学 第2問：古典理想気体と箱中ボース粒子の低温エントロピー
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成30年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成30年度 物理学 第2問：古典理想気体と箱中ボース粒子の低温エントロピー

## 問題

各辺が $L, L, 2L$（体積 $V = L \times L \times 2L$）の直方体の中に質量が $m$ の粒子が $N$ 個あり，温度 $T$ の熱平衡状態にあるとする。ボルツマン定数を $k_{\mathrm{B}}$ とする。粒子は互いに区別できないとする。ここで，$L,\ N$ は有限の値を持つものとする。粒子間の相互作用は考えず，系のハミルトニアンは，$i$ 番目の粒子の位置を $(x_i, y_i, z_i)$，運動量を $(p_i^x, p_i^y, p_i^z)$ として

$$
\mathcal{H} = \sum_{i=1}^{N} \frac{1}{2m}\left[(p_i^x)^2 + (p_i^y)^2 + (p_i^z)^2\right] \tag{1}
$$

で与えられるものとする。必要であれば以下の積分公式を用いてよい。

$$
\int_{-\infty}^{\infty} e^{-ax^2} dx = \sqrt{\frac{\pi}{a}},\qquad a > 0 \tag{2}
$$

また，必要であれば，エントロピー $S(T)$ と定積熱容量 $C_V(T)$ の熱力学的関係

$$
S(T_2) = S(T_1) + \int_{T_1}^{T_2} \frac{C_V(T')}{T'}\,dT' \tag{3}
$$

を用いてよい。

まず，粒子の運動を古典力学的に考える。
{: .problem-lead }

(1) 粒子数を $N$ に固定した場合，以下の問いに答えよ。

(i) この系の内部エネルギーと定積熱容量を $T,\ N$ の関数として求めよ。

(ii) この系の圧力を $T,\ V,\ N$ の関数として求めよ。

(iii) ある温度 $T_0$ でのエントロピー $S(T_0)$ と，温度を $T_0/2$ に下げた時のエントロピー $S(T_0/2)$ との差を

$$
\Delta S(T_0, T_0/2) \equiv S(T_0) - S(T_0/2) \tag{4}
$$

と定義する。この量を求めよ。

(2) 次に，粒子が壁を通して外界と出入りできる場合を考える。外界での粒子の化学ポテンシャル $\mu$ は温度変化しないものとする。以下の問いに答えよ。

(i) 与えられた一定の体積，化学ポテンシャルのもとで，この系の温度 $T_1$ での粒子数の期待値と温度 $T_2$ での粒子数の期待値の比 $\langle N(T_1)\rangle / \langle N(T_2)\rangle$ を求めよ。

(ii) 温度 $T$ でのこの系の粒子数密度 $\langle N(T)\rangle / V$ と圧力 $P$ の関係を求めよ。

以下では，粒子の運動を量子力学的に考える。

(3) 系に $N$ 個の粒子が閉じ込められている場合を考える。ここで，粒子は互いに区別できないボース粒子とする。体積 $V = L \times L \times 2L$ の容器に閉じ込められている1粒子のエネルギー固有値，固有関数は，$L, L, 2L$ の直方体の各辺の方向の座標をそれぞれ $x, y, z$ として

$$
\mathcal{H}\Psi^{n_x, n_y, n_z}(x, y, z) = E(n_x, n_y, n_z)\Psi^{n_x, n_y, n_z}(x, y, z) \tag{5}
$$

を満たす。ただし，

$$
\Psi^{n_x, n_y, n_z}(x, y, z) = \frac{\sin\left(\frac{n_x\pi}{L}x\right)}{\sqrt{L/2}}\frac{\sin\left(\frac{n_y\pi}{L}y\right)}{\sqrt{L/2}}\frac{\sin\left(\frac{n_z\pi}{2L}z\right)}{\sqrt{L}} \tag{6}
$$

$$
E(n_x, n_y, n_z) = \frac{\pi^2}{2m}\frac{\hbar^2\left[n_x^2 + n_y^2 + \left(\frac{n_z}{2}\right)^2\right]}{L^2},\qquad n_\alpha = 1, 2, \dots,\ \alpha = x, y, z \tag{7}
$$

で与えられることを用いてよい。ここで $\hbar$ はプランク定数を $2\pi$ で割ったものである。

(i) この系の基底状態と第一励起状態のエネルギーを求めよ。

(ii) $k_{\mathrm{B}}T$ が基底状態と第一励起状態のエネルギー差の大きさに比べて十分小さい場合に，この系の内部エネルギーの温度依存性を求め，設問1で求めた結果と比較せよ。

(iii) $T = 0$ での定積熱容量を求めよ。

(iv) ある温度 $T_0$ でのエントロピー $S(T_0)$ と，温度を $T_0/2$ に下げた時のエントロピー $S(T_0/2)$ との差を

$$
\Delta S(T_0, T_0/2) \equiv S(T_0) - S(T_0/2) \tag{8}
$$

と定義する。$T_0 \to 0$ の極限でのこの量の値を求めよ。

(v) 低温でのエントロピーに関して設問1(iii)で求めた結果と設問3(iv)の結果を比較し，その違いをエントロピーと状態数の関係をあたえるボルツマンの原理の観点から説明せよ。ただし，半径 $r$ の $d$ 次元超球の表面積は $a_d r^{d-1}$ で与えられることを用いてよい。ここで $a_d$ は $r$ に依存しないある定数である。

> 出典：東京大学大学院理学系研究科物理学専攻 平成30年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
古典理想気体では相空間が連続であるため，温度を半分にすると運動量空間の等エネルギー面の面積が常に同じ比率で縮小し，温度 $T_0$ によらずエントロピー差が一定値 $\dfrac{3}{2}Nk_{\mathrm{B}}\ln 2$ を保ちます。

一方，有限体積の箱に閉じ込められた量子ボース粒子系では1粒子準位が離散的になり，基底状態と第1励起状態の間に有限のエネルギーギャップ $\Delta\epsilon$ が生じます。そのため $k_{\mathrm{B}}T \ll \Delta\epsilon$ では熱励起が指数関数的に抑えられ，系は唯一の基底状態へ落ちて熱力学第三法則が自然に成り立ちます。
</div>

### (1)
逆温度を $\beta = \dfrac{1}{k_{\mathrm{B}}T}$ とし，古典系の分配関数 $Z(T, V, N)$ を式 (2) を用いて計算します（$h = 2\pi\hbar$）。

$$
\begin{aligned}
Z(T, V, N)
&= \frac{1}{N!\,h^{3N}}\int \mathrm{d}^{3N}r\,\mathrm{d}^{3N}p\,e^{-\beta\mathcal{H}} \\
&= \frac{V^N}{N!\,h^{3N}}\left(\int_{-\infty}^{\infty} e^{-\frac{\beta}{2m}p^2}\,\mathrm{d}p\right)^{3N} \\
&= \frac{V^N}{N!}\left(\frac{2\pi m}{\beta h^2}\right)^{\frac{3N}{2}}
\end{aligned}
$$

(i) 内部エネルギー $U = -\dfrac{\partial\ln Z}{\partial\beta}$ と定積熱容量 $C_V = \left(\dfrac{\partial U}{\partial T}\right)_{V, N}$ を求めます。

$$
U = -\frac{\partial}{\partial\beta}\left(-\frac{3N}{2}\ln\beta\right) = \frac{3N}{2\beta} = \frac{3}{2}Nk_{\mathrm{B}}T,\qquad
C_V = \left(\frac{\partial U}{\partial T}\right)_{V, N} = \frac{3}{2}Nk_{\mathrm{B}}
$$

したがって，

$$
\finalanswer{U = \frac{3}{2}Nk_{\mathrm{B}}T,\qquad C_V = \frac{3}{2}Nk_{\mathrm{B}}}
$$

(ii) ヘルムホルツの自由エネルギー $F = -k_{\mathrm{B}}T\ln Z$ より圧力 $P = -\left(\dfrac{\partial F}{\partial V}\right)_{T, N}$ を求めます。

$$
P = k_{\mathrm{B}}T\left(\frac{\partial\ln Z}{\partial V}\right)_{T, N} = k_{\mathrm{B}}T\cdot\frac{N}{V} = \frac{Nk_{\mathrm{B}}T}{V}
$$

したがって，

$$
\finalanswer{P = \frac{Nk_{\mathrm{B}}T}{V}}
$$

(iii) 式 (3) に $C_V(T') = \dfrac{3}{2}Nk_{\mathrm{B}}$ を代入します。

$$
\Delta S(T_0, T_0/2) = \int_{T_0/2}^{T_0} \frac{3Nk_{\mathrm{B}}}{2T'}\,\mathrm{d}T' = \frac{3}{2}Nk_{\mathrm{B}}\ln\frac{T_0}{T_0/2} = \frac{3}{2}Nk_{\mathrm{B}}\ln 2
$$

したがって，

$$
\finalanswer{\Delta S(T_0, T_0/2) = \frac{3}{2}Nk_{\mathrm{B}}\ln 2}
$$

### (2)
大分配関数 $\Xi(T, V, \mu)$ を計算します。

$$
\begin{aligned}
\Xi(T, V, \mu)
&= \sum_{N=0}^{\infty} e^{\beta\mu N} Z(T, V, N) \\
&= \sum_{N=0}^{\infty} \frac{1}{N!}\left[e^{\beta\mu} V \left(\frac{2\pi m k_{\mathrm{B}}T}{h^2}\right)^{\frac{3}{2}}\right]^N \\
&= \exp\left[e^{\beta\mu} V \left(\frac{2\pi m k_{\mathrm{B}}T}{h^2}\right)^{\frac{3}{2}}\right]
\end{aligned}
$$

(i) 粒子数の期待値は $\langle N(T)\rangle = \dfrac{1}{\beta}\left(\dfrac{\partial\ln\Xi}{\partial\mu}\right)_{T, V}$ です。

$$
\langle N(T)\rangle = e^{\frac{\mu}{k_{\mathrm{B}}T}} V \left(\frac{2\pi m k_{\mathrm{B}}T}{h^2}\right)^{\frac{3}{2}}
$$

体積 $V$ と化学ポテンシャル $\mu$ が一定なので，温度 $T_1,\ T_2$ での比をとります。

$$
\frac{\langle N(T_1)\rangle}{\langle N(T_2)\rangle} = \left(\frac{T_1}{T_2}\right)^{\frac{3}{2}}\exp\left[\frac{\mu}{k_{\mathrm{B}}}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]
$$

したがって，

$$
\finalanswer{\frac{\langle N(T_1)\rangle}{\langle N(T_2)\rangle} = \left(\frac{T_1}{T_2}\right)^{\frac{3}{2}}\exp\left[\frac{\mu}{k_{\mathrm{B}}}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]}
$$

(ii) グランドポテンシャル $J = -PV = -k_{\mathrm{B}}T\ln\Xi$ より，

$$
PV = k_{\mathrm{B}}T\ln\Xi = k_{\mathrm{B}}T\,\langle N(T)\rangle \implies P = \frac{\langle N(T)\rangle}{V}\,k_{\mathrm{B}}T
$$

となります。したがって，

$$
\finalanswer{P = \frac{\langle N(T)\rangle}{V}\,k_{\mathrm{B}}T}
$$

### (3)
(i) 式 (7) より，1粒子のエネルギー準位で最も低いのは $(n_x, n_y, n_z) = (1, 1, 1)$，次に低いのは $(n_x, n_y, n_z) = (1, 1, 2)$ です。

$$
\begin{aligned}
\epsilon_0 &= E(1, 1, 1) = \frac{\pi^2\hbar^2}{2mL^2}\left(1 + 1 + \frac{1}{4}\right) = \frac{9\pi^2\hbar^2}{8mL^2} \\
\epsilon_1 &= E(1, 1, 2) = \frac{\pi^2\hbar^2}{2mL^2}\left(1 + 1 + 1\right) = \frac{3\pi^2\hbar^2}{2mL^2}
\end{aligned}
$$

ボース粒子は同一状態に何個でも入ることができるため，$N$ 粒子系の基底状態は $N$ 個すべてが $(1, 1, 1)$ にある状態（縮退なし），第一励起状態は $N - 1$ 個が $(1, 1, 1)$ にあり $1$ 個だけが $(1, 1, 2)$ にある状態（粒子は区別できないのでやはり縮退なし）です。エネルギー差を $\Delta\epsilon = \epsilon_1 - \epsilon_0 = \dfrac{3\pi^2\hbar^2}{8mL^2}$ とおくと，

$$
E_0 = N\epsilon_0 = \frac{9N\pi^2\hbar^2}{8mL^2},\qquad
E_1 = (N - 1)\epsilon_0 + \epsilon_1 = \frac{(9N + 3)\pi^2\hbar^2}{8mL^2}
$$

となります。したがって，

$$
\finalanswer{E_0 = \frac{9N\pi^2\hbar^2}{8mL^2},\qquad E_1 = \frac{(9N + 3)\pi^2\hbar^2}{8mL^2}}
$$

(ii) $k_{\mathrm{B}}T \ll \Delta\epsilon = E_1 - E_0 = \dfrac{3\pi^2\hbar^2}{8mL^2}$ のとき，第二励起状態以上のボルツマン因子は無視するほど小さいため，基底状態と第一励起状態のみを残して分配関数を近似することができます。

$$
Z(T) \simeq e^{-\beta E_0} + e^{-\beta E_1} = e^{-\beta E_0}\left(1 + e^{-\beta\Delta\epsilon}\right)
$$

内部エネルギー $U(T) = -\dfrac{\partial\ln Z}{\partial\beta}$ を計算します。

$$
\begin{aligned}
U(T)
&\simeq E_0 + \frac{\Delta\epsilon\,e^{-\beta\Delta\epsilon}}{1 + e^{-\beta\Delta\epsilon}} \\
&\simeq E_0 + \Delta\epsilon\,e^{-\frac{\Delta\epsilon}{k_{\mathrm{B}}T}}
= \frac{9N\pi^2\hbar^2}{8mL^2} + \frac{3\pi^2\hbar^2}{8mL^2}\exp\left(-\frac{3\pi^2\hbar^2}{8mL^2 k_{\mathrm{B}}T}\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{U(T) \simeq E_0 + \Delta\epsilon\,e^{-\frac{\Delta\epsilon}{k_{\mathrm{B}}T}} \qquad \left(E_0 = \frac{9N\pi^2\hbar^2}{8mL^2},\ \Delta\epsilon = \frac{3\pi^2\hbar^2}{8mL^2}\right)}
$$

**設問1との比較**：古典論の設問1では内部エネルギーは $U = \dfrac{3}{2}Nk_{\mathrm{B}}T$ と温度 $T$ に比例して $T \to 0$ で $0$ になります。これに対し量子論では，不確定性関係に由来する有限の基底エネルギー（零点エネルギー）$E_0 > 0$ をもち，温度上昇に伴う増加分も $T$ に比例せず指数関数 $e^{-\Delta\epsilon/(k_{\mathrm{B}}T)}$ で極めて緩やかに立ち上がります。

(iii) (ii) の $U(T)$ を $T$ で微分して定積熱容量を求め，$T \to 0$ の極限をとります。

$$
C_V(T) = \left(\frac{\partial U}{\partial T}\right)_{V, N} \simeq k_{\mathrm{B}}\left(\frac{\Delta\epsilon}{k_{\mathrm{B}}T}\right)^2 e^{-\frac{\Delta\epsilon}{k_{\mathrm{B}}T}} \xrightarrow{T \to 0} 0
$$

したがって，

$$
\finalanswer{C_V(0) = 0}
$$

(iv) 式 (8) と式 (3) に (iii) の低温表現を代入します。$x = \dfrac{\Delta\epsilon}{k_{\mathrm{B}}T'}$ と変数変換します。

$$
\begin{aligned}
\Delta S(T_0, T_0/2)
&= \int_{T_0/2}^{T_0} \frac{C_V(T')}{T'}\,\mathrm{d}T' \\
&\simeq k_{\mathrm{B}}\int_{\frac{\Delta\epsilon}{k_{\mathrm{B}}T_0}}^{\frac{2\Delta\epsilon}{k_{\mathrm{B}}T_0}} x\,e^{-x}\,\mathrm{d}x \\
&= k_{\mathrm{B}}\left[\left(1 + \frac{\Delta\epsilon}{k_{\mathrm{B}}T_0}\right)e^{-\frac{\Delta\epsilon}{k_{\mathrm{B}}T_0}} - \left(1 + \frac{2\Delta\epsilon}{k_{\mathrm{B}}T_0}\right)e^{-\frac{2\Delta\epsilon}{k_{\mathrm{B}}T_0}}\right]
\end{aligned}
$$

$T_0 \to 0$ のとき $\dfrac{\Delta\epsilon}{k_{\mathrm{B}}T_0} \to \infty$ なので，この値は $0$ に収束します。したがって，

$$
\finalanswer{\lim_{T_0 \to 0} \Delta S(T_0, T_0/2) = 0}
$$

(v) ボルツマンの原理 $S = k_{\mathrm{B}}\ln W$（$W$ は微視的状態数）の観点から両者を比較します。

- **古典系（設問1(iii)）**：エネルギー $U$ をもつ等エネルギー面は，$3N$ 次元運動量空間において半径 $p = \sqrt{2mU}$ の $3N$ 次元超球面です。その表面積は $a_{3N} p^{3N - 1} \propto U^{(3N - 1)/2}$ であり，微小幅 $\delta U$ の状態数 $W_{\mathrm{cl}}(U) \propto V^N p^{3N - 1}\dfrac{\mathrm{d}p}{\mathrm{d}U}\delta U \propto U^{3N/2 - 1} \simeq U^{3N/2}$（運動量空間の体積で評価しても $\propto p^{3N} \propto U^{3N/2}$）となります。$U = \dfrac{3}{2}Nk_{\mathrm{B}}T$ より，温度を $T_0$ から $T_0/2$ に下げると，どんな低温でも状態数の比は $W_{\mathrm{cl}}(T_0)/W_{\mathrm{cl}}(T_0/2) = 2^{3N/2}$ と一定の比を保ちます。そのためエントロピー差 $\Delta S = k_{\mathrm{B}}\ln\left(W_{\mathrm{cl}}(T_0)/W_{\mathrm{cl}}(T_0/2)\right) = \dfrac{3}{2}Nk_{\mathrm{B}}\ln 2$ は $T_0 \to 0$ でも $0$ にならず（$S \to -\infty$ へ発散），熱力学第三法則を満たしません。
- **量子系（設問3(iv)）**：有限の箱の中ではエネルギー準位が離散的であり，基底状態と第一励起状態の間に有限のエネルギーギャップ $\Delta\epsilon > 0$ が存在します。$k_{\mathrm{B}}T_0 \ll \Delta\epsilon$ の低温極限では励起状態への遷移が凍結し，系は縮退のない唯一の基底状態（状態数 $W = 1$）をとるため，$S(T_0) \to k_{\mathrm{B}}\ln 1 = 0$ となり，$\Delta S(T_0, T_0/2) \to 0$ となります。

<aside class="rigor-note" markdown>
本問では $L, N$ を有限に固定して $T_0 \to 0$ の極限をとったため，有限サイズギャップ $\Delta\epsilon \propto L^{-2}$ によって $C_V$ や $S$ が指数関数的に $0$ へ収束しました。熱力学極限（$N, V \to \infty$ を先に $N/V$ 一定でとる極限）では3次元理想ボース気体はボース・アインシュタイン凝縮を起こし，低温では $C_V \propto T^{3/2},\ S \propto T^{3/2}$ のべき乗則で $0$ に収束します。
</aside>
