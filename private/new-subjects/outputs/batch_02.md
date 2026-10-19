===== FILE: 06solid_state/05/05_010.md =====
---
tags:
  - 基本
---

# デュロン・プティの法則

## 問題
$N$ 個の原子からなる結晶を，各原子が平衡位置のまわりで小さく振動する系とみなす。変位の2次までをとる調和近似では，質量で重みをつけた基準座標 $Q_s$ とそれに共役な運動量 $P_s$（$s=1,2,\ldots,3N$）を用いて，結晶のハミルトニアンは

$$
H=U_0+\sum_{s=1}^{3N}\left(\frac{P_s^{\,2}}{2}+\frac{1}{2}\omega_s^{\,2}Q_s^{\,2}\right)
$$

と書ける。$U_0$ はすべての原子が平衡位置にあるときのエネルギー，$\omega_s>0$ は基準振動の角振動数であり，体積を一定に保てばどちらも温度によらない。振動数が0の並進・回転のモードは数が $3N$ に比べて少ないので無視する。古典統計力学では，正準共役な変数の組1つにつき，位相空間の体積 $h=2\pi\hbar$ を1つの状態として数える。温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$ とする。以下の問いに答えよ。

(1) 質量 $M$，角振動数 $\omega$ の1次元の調和振動子 $H_1=\dfrac{p^2}{2M}+\dfrac{1}{2}M\omega^2x^2$ について，古典統計力学での分配関数 $Z_1$ と平均エネルギー $\langle E\rangle$ を求めよ。

(2) 結晶の分配関数 $Z$，内部エネルギー $U$，定積比熱 $C_V$ を求めよ。

(3) 気体定数を $R=8.314\ \mathrm{J/(mol\,K)}$ として，1 mol あたりの $C_V$ を数値で求めよ。また，銅のモル質量を $63.55\ \mathrm{g/mol}$ として，銅 1 g あたりの比熱 $c$ を求めよ。

(4) 振動子を量子力学で扱うと，角振動数 $\omega$ の1次元の調和振動子の平均エネルギーは $\langle E\rangle=\hbar\omega\left(\dfrac{1}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}+\dfrac{1}{2}\right)$ となる。$x=\hbar\omega/k_{\mathrm{B}}T$ とおき，$x\ll1$ のときの振動子1つの比熱 $C$ を $x^2$ の項まで求めよ。また，$C$ が古典的な値 $k_{\mathrm{B}}$ より 1% 小さくなる温度を $\hbar\omega/k_{\mathrm{B}}$ を用いて表せ。

---

## 解答・解説

### (1)
古典統計での分配関数は，ボルツマン因子を位相空間で積分して $h$ で割ったものです。$\beta=1/k_{\mathrm{B}}T$ とおくと，運動量と座標の積分はどちらもガウス積分になります。

$$
Z_1=\frac{1}{h}\int_{-\infty}^{\infty}e^{-\beta p^2/2M}\,\mathrm{d}p\int_{-\infty}^{\infty}e^{-\beta M\omega^2x^2/2}\,\mathrm{d}x=\frac{1}{h}\sqrt{\frac{2\pi M}{\beta}}\sqrt{\frac{2\pi}{\beta M\omega^2}}=\frac{2\pi}{h\beta\omega}
$$

平均エネルギーは $\langle E\rangle=-\partial\ln Z_1/\partial\beta$ から求まり，

$$
\finalanswer{Z_1=\frac{k_{\mathrm{B}}T}{\hbar\omega}},\qquad \finalanswer{\langle E\rangle=k_{\mathrm{B}}T}
$$

となります。運動エネルギーとポテンシャルエネルギーが $k_{\mathrm{B}}T/2$ ずつ寄与しており，結果は $M$ にも $\omega$ にもよりません。

### (2)
ハミルトニアンは独立な $3N$ 個の振動子の和なので，分配関数は各振動子の分配関数の積になります。各振動子の分配関数は，(1) で $M=1$，$\omega=\omega_s$ とおいたものです。

$$
\finalanswer{Z=e^{-\beta U_0}\prod_{s=1}^{3N}\frac{k_{\mathrm{B}}T}{\hbar\omega_s}}
$$

$\ln Z=-\beta U_0-3N\ln\beta-\sum_s\ln\hbar\omega_s$ を $\beta$ で微分して符号を変えると内部エネルギーが得られ，それを $T$ で微分すると比熱が得られます。

$$
\finalanswer{U=U_0+3Nk_{\mathrm{B}}T},\qquad \finalanswer{C_V=3Nk_{\mathrm{B}}}
$$

となります。比熱は振動数の分布によらず，原子の数だけで決まります。これがデュロン・プティの法則です。

### (3)
1 mol では $Nk_{\mathrm{B}}=R$ なので，比熱は $3R$ です。

$$
\finalanswer{C_V=3R\approx 24.9\ \mathrm{J/(mol\,K)}}
$$

銅 1 g は $1/63.55$ mol にあたるので，$c=24.94/63.55\ \mathrm{J/(g\,K)}$ を計算すると，

$$
\finalanswer{c\approx 0.392\ \mathrm{J/(g\,K)}}
$$

となります。室温での銅の測定値は約 $0.385\ \mathrm{J/(g\,K)}$ で，よく一致します。

### (4)
展開しやすいように，平均エネルギーを双曲線関数で書き直します。$\dfrac{1}{e^x-1}+\dfrac{1}{2}=\dfrac{e^x+1}{2(e^x-1)}$ なので，

$$
\langle E\rangle=\frac{\hbar\omega}{2}\coth\frac{x}{2}
$$

です。$y\ll1$ では $\coth y=\dfrac{1}{y}+\dfrac{y}{3}-\cdots$ と展開できるので，

$$
\langle E\rangle\approx\frac{\hbar\omega}{2}\left(\frac{2}{x}+\frac{x}{6}\right)=k_{\mathrm{B}}T+\frac{(\hbar\omega)^2}{12k_{\mathrm{B}}T}
$$

となります。これを $T$ で微分すると，

$$
\finalanswer{C=k_{\mathrm{B}}\left(1-\frac{x^2}{12}\right)}
$$

が得られます。ずれが 1% になるのは $x^2/12=0.01$，すなわち $x=\sqrt{0.12}\approx0.346$ のときなので，

$$
\finalanswer{T\approx 2.9\,\frac{\hbar\omega}{k_{\mathrm{B}}}}
$$

となります。デュロン・プティの法則が成り立つのは，$k_{\mathrm{B}}T$ が振動の量子 $\hbar\omega$ より十分大きい温度に限られます。

===== FILE: 06solid_state/05/05_020.md =====
---
tags:
  - 標準
---

# アインシュタイン模型

## 問題
$N$ 個の原子からなる結晶で，各原子が平衡位置のまわりで，同じ角振動数 $\omega_{\mathrm{E}}$ をもつ3次元の等方的な調和振動子として独立に振動するとみなす（アインシュタイン模型）。振動子は量子力学で扱い，1次元の調和振動子のエネルギー準位を $\left(n+\dfrac{1}{2}\right)\hbar\omega_{\mathrm{E}}$（$n=0,1,2,\ldots$）とする。アインシュタイン温度を $\Theta_{\mathrm{E}}=\hbar\omega_{\mathrm{E}}/k_{\mathrm{B}}$ とする。$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度であり，体積は一定に保つ。以下の問いに答えよ。

(1) 1次元の調和振動子1つについて，分配関数 $Z_1$ と平均エネルギー $\langle E\rangle$ を求めよ。

(2) 結晶の振動の内部エネルギー $U$ と定積比熱 $C_V$ を，$x=\Theta_{\mathrm{E}}/T$ を用いて表せ。

(3) $T\gg\Theta_{\mathrm{E}}$ での $C_V$ の極限値を求めよ。また，$T\ll\Theta_{\mathrm{E}}$ での $C_V$ の主要な振る舞いを求めよ。

(4) ダイヤモンドを $\Theta_{\mathrm{E}}=1320\ \mathrm{K}$ のアインシュタイン模型で表す。$T=300\ \mathrm{K}$ での 1 mol あたりの $C_V$ を，(2) の式と (3) の低温での式のそれぞれで求めよ。気体定数を $R=8.314\ \mathrm{J/(mol\,K)}$ とする。

---

## 解答・解説

### (1)
$\beta=1/k_{\mathrm{B}}T$ とおき，ボルツマン因子をすべての準位について足します。和は公比 $e^{-\beta\hbar\omega_{\mathrm{E}}}$ の等比級数です。

$$
\finalanswer{Z_1=\sum_{n=0}^{\infty}e^{-\beta(n+1/2)\hbar\omega_{\mathrm{E}}}=\frac{e^{-\beta\hbar\omega_{\mathrm{E}}/2}}{1-e^{-\beta\hbar\omega_{\mathrm{E}}}}}
$$

平均エネルギーは $\langle E\rangle=-\partial\ln Z_1/\partial\beta$ で求まり，

$$
\finalanswer{\langle E\rangle=\frac{\hbar\omega_{\mathrm{E}}}{2}+\frac{\hbar\omega_{\mathrm{E}}}{e^{\hbar\omega_{\mathrm{E}}/k_{\mathrm{B}}T}-1}}
$$

となります。第1項は零点エネルギー，第2項は平均の励起数に $\hbar\omega_{\mathrm{E}}$ をかけたものです。

### (2)
結晶は独立な1次元振動子 $3N$ 個からなるので，内部エネルギーは $\langle E\rangle$ の $3N$ 倍です。$\hbar\omega_{\mathrm{E}}=k_{\mathrm{B}}\Theta_{\mathrm{E}}$ を使うと，

$$
\finalanswer{U=3Nk_{\mathrm{B}}\Theta_{\mathrm{E}}\left(\frac{1}{2}+\frac{1}{e^{x}-1}\right)}
$$

となります。$T$ で微分するときは $\dfrac{\mathrm{d}x}{\mathrm{d}T}=-\dfrac{x}{T}$ を使います。

$$
\finalanswer{C_V=3Nk_{\mathrm{B}}\frac{x^2e^x}{(e^x-1)^2}}
$$

となります。

### (3)
$T\gg\Theta_{\mathrm{E}}$ では $x\ll1$ なので，$e^x\approx1$，$e^x-1\approx x$ と近似できます。

$$
\finalanswer{C_V\to3Nk_{\mathrm{B}}}
$$

となり，デュロン・プティの値に戻ります。$T\ll\Theta_{\mathrm{E}}$ では $x\gg1$ なので，分母を $(e^x-1)^2\approx e^{2x}$ と近似できます。

$$
\finalanswer{C_V\approx3Nk_{\mathrm{B}}\left(\frac{\Theta_{\mathrm{E}}}{T}\right)^2e^{-\Theta_{\mathrm{E}}/T}}
$$

となります。比熱の温度依存性を図に示します。

<!-- FIGURE solution (3): 横軸 T/Θ_E（0〜1.5），縦軸 C_V/(3N k_B)（0〜1.1）。曲線 x²e^x/(e^x−1)²（x = Θ_E/T）を実線で描く。T/Θ_E が小さいところでは横軸に沿ってほぼ0で，T/Θ_E ≈ 0.2 付近から立ち上がり，1 に漸近する。縦軸 1 の位置に水平な破線を引き「デュロン・プティ」と注記。T/Θ_E = 0.227 の位置に縦の点線を引き「ダイヤモンド 300 K」と注記する。 -->

低温では，振動の量子 $k_{\mathrm{B}}\Theta_{\mathrm{E}}$ を励起する確率がボルツマン因子 $e^{-\Theta_{\mathrm{E}}/T}$ で抑えられるので，比熱は指数関数的に0へ近づきます。実際の結晶の低温比熱は $T^3$ に比例してもっとゆっくり減ります。これは，振動数の低い音響モードがあるためです。

### (4)
$x=1320/300=4.40$ です。$e^{4.40}=81.45$，$x^2=19.36$ を (2) の式に代入します。

$$
\frac{x^2e^x}{(e^x-1)^2}=\frac{19.36\times81.45}{(80.45)^2}=0.2436
$$

$3R=24.94\ \mathrm{J/(mol\,K)}$ をかけると，

$$
\finalanswer{C_V\approx6.08\ \mathrm{J/(mol\,K)}}
$$

となります。低温での式では $x^2e^{-x}=19.36\times0.01228=0.2377$ なので，

$$
\finalanswer{C_V\approx5.93\ \mathrm{J/(mol\,K)}}
$$

となります。2つの値の違いは約 2.5% です。ダイヤモンドは原子が軽く結合が強いので $\Theta_{\mathrm{E}}$ が高く，室温でも比熱はデュロン・プティの値の4分の1ほどしかありません。測定値は約 $6.1\ \mathrm{J/(mol\,K)}$ です。

===== FILE: 06solid_state/05/05_030.md =====
---
tags:
  - 標準
---

# デバイ模型と T^3 則

## 問題
$N$ 個の原子からなる体積 $V$ の結晶を考え，原子の数密度を $n=N/V$ とする。結晶中の弾性波は，縦波1つと横波2つの分枝からなる。それぞれ $\omega=v_{\mathrm{L}}k$ と $\omega=v_{\mathrm{T}}k$（$k=|\boldsymbol{k}|$）の線形な分散に従うとする。周期境界条件を課し，$V$ は十分大きいとする。デバイ模型では，3つの分枝に共通の角振動数 $\omega_{\mathrm{D}}$ 以下のモードだけがあるとし，モードの総数が $3N$ になるように $\omega_{\mathrm{D}}$ を選ぶ。デバイ温度を $\Theta_{\mathrm{D}}=\hbar\omega_{\mathrm{D}}/k_{\mathrm{B}}$ とする。角振動数 $\omega$ のモード1つの比熱は，$x=\hbar\omega/k_{\mathrm{B}}T$ として $k_{\mathrm{B}}\dfrac{x^2e^x}{(e^x-1)^2}$ である。$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。以下の問いに答えよ。

(1) $0<\omega<\omega_{\mathrm{D}}$ での状態密度 $D(\omega)$ を求めよ。また，平均の音速 $v_{\mathrm{D}}$ を $\dfrac{3}{v_{\mathrm{D}}^{\,3}}=\dfrac{1}{v_{\mathrm{L}}^{\,3}}+\dfrac{2}{v_{\mathrm{T}}^{\,3}}$ で定義し，$\omega_{\mathrm{D}}$ を $v_{\mathrm{D}}$ と $n$ で表せ。

(2) 定積比熱 $C_V$ を，$T/\Theta_{\mathrm{D}}$ と1つの定積分を用いて表せ。また，$T\gg\Theta_{\mathrm{D}}$ での $C_V$ を求めよ。

(3) $T\ll\Theta_{\mathrm{D}}$ での $C_V$ を求めよ。$\displaystyle\int_0^\infty\frac{x^3}{e^x-1}\,\mathrm{d}x=\frac{\pi^4}{15}$ と部分積分を用いてよい。

(4) 銅の値 $n=8.47\times10^{28}\ \mathrm{m^{-3}}$，$v_{\mathrm{L}}=4.76\times10^3\ \mathrm{m/s}$，$v_{\mathrm{T}}=2.325\times10^3\ \mathrm{m/s}$ を用いて，$v_{\mathrm{D}}$ と $\Theta_{\mathrm{D}}$ を求めよ。さらに，$T=10\ \mathrm{K}$ での 1 mol あたりの $C_V$ を (3) の式で求めよ。$\hbar=1.055\times10^{-34}\ \mathrm{J\,s}$，$k_{\mathrm{B}}=1.381\times10^{-23}\ \mathrm{J/K}$，気体定数 $R=8.314\ \mathrm{J/(mol\,K)}$ とする。

---

## 解答・解説

### (1)
周期境界条件のもとでは，許される $\boldsymbol{k}$ が波数空間の体積 $(2\pi)^3/V$ ごとに1個ずつあります。音速 $v$ の1つの分枝について，角振動数が $\omega$ 以下のモードの数は，半径 $\omega/v$ の球の中の点の数 $\dfrac{V}{(2\pi)^3}\cdot\dfrac{4\pi}{3}\left(\dfrac{\omega}{v}\right)^3$ です。3つの分枝を足すと，

$$
\mathcal{N}(\omega)=\frac{V\omega^3}{6\pi^2}\left(\frac{1}{v_{\mathrm{L}}^{\,3}}+\frac{2}{v_{\mathrm{T}}^{\,3}}\right)=\frac{V\omega^3}{2\pi^2v_{\mathrm{D}}^{\,3}}
$$

となり，これを $\omega$ で微分すると状態密度が得られます。$\mathcal{N}(\omega_{\mathrm{D}})=3N$ とおくと $\omega_{\mathrm{D}}$ が決まります。

$$
\finalanswer{D(\omega)=\frac{3V\omega^2}{2\pi^2v_{\mathrm{D}}^{\,3}}},\qquad \finalanswer{\omega_{\mathrm{D}}=v_{\mathrm{D}}\left(6\pi^2n\right)^{1/3}}
$$

となります。$\omega_{\mathrm{D}}$ を使うと $D(\omega)=9N\omega^2/\omega_{\mathrm{D}}^{\,3}$ とも書けます。

### (2)
各モードの比熱に状態密度をかけて積分します。$x=\hbar\omega/k_{\mathrm{B}}T$ と置き換えると，上限は $\hbar\omega_{\mathrm{D}}/k_{\mathrm{B}}T=\Theta_{\mathrm{D}}/T$ になります。

$$
C_V=\int_0^{\omega_{\mathrm{D}}}\frac{9N\omega^2}{\omega_{\mathrm{D}}^{\,3}}\,k_{\mathrm{B}}\frac{x^2e^x}{(e^x-1)^2}\,\mathrm{d}\omega
$$

$\omega=k_{\mathrm{B}}Tx/\hbar$ を代入すると，

$$
\finalanswer{C_V=9Nk_{\mathrm{B}}\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^3\int_0^{\Theta_{\mathrm{D}}/T}\frac{x^4e^x}{(e^x-1)^2}\,\mathrm{d}x}
$$

となります。$T\gg\Theta_{\mathrm{D}}$ では積分範囲で $x\ll1$ なので，被積分関数は $x^2$ で近似でき，積分は $\dfrac{1}{3}\left(\dfrac{\Theta_{\mathrm{D}}}{T}\right)^3$ になります。

$$
\finalanswer{C_V\to3Nk_{\mathrm{B}}}
$$

となり，デュロン・プティの値に戻ります。

### (3)
$T\ll\Theta_{\mathrm{D}}$ では，被積分関数が $x\gg1$ で指数関数的に小さくなるので，上限を $\infty$ にしてよくなります。$\dfrac{e^x}{(e^x-1)^2}=\dfrac{\mathrm{d}}{\mathrm{d}x}\left(-\dfrac{1}{e^x-1}\right)$ を使って部分積分すると，

$$
\int_0^\infty\frac{x^4e^x}{(e^x-1)^2}\,\mathrm{d}x=\left[-\frac{x^4}{e^x-1}\right]_0^\infty+\int_0^\infty\frac{4x^3}{e^x-1}\,\mathrm{d}x=\frac{4\pi^4}{15}
$$

となります。境界項は両端で0です。これを (2) に代入すると，

$$
\finalanswer{C_V=\frac{12\pi^4}{5}Nk_{\mathrm{B}}\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^3}
$$

となります。低温で励起されるのは $\hbar\omega\lesssim k_{\mathrm{B}}T$ の長波長の音響モードだけで，その数が $T^3$ に比例します。

### (4)
まず $v_{\mathrm{D}}$ を求めます。$1/v_{\mathrm{L}}^{\,3}=9.27\times10^{-12}\ \mathrm{s^3/m^3}$，$2/v_{\mathrm{T}}^{\,3}=1.591\times10^{-10}\ \mathrm{s^3/m^3}$ で，和は $1.684\times10^{-10}\ \mathrm{s^3/m^3}$ です。横波の寄与が大部分を占めます。

$$
\finalanswer{v_{\mathrm{D}}\approx2.61\times10^3\ \mathrm{m/s}}
$$

次に $(6\pi^2n)^{1/3}=1.712\times10^{10}\ \mathrm{m^{-1}}$ から $\omega_{\mathrm{D}}=4.47\times10^{13}\ \mathrm{s^{-1}}$ を求め，$\Theta_{\mathrm{D}}=\hbar\omega_{\mathrm{D}}/k_{\mathrm{B}}$ を計算します。

$$
\finalanswer{\Theta_{\mathrm{D}}\approx342\ \mathrm{K}}
$$

1 mol では $\dfrac{12\pi^4}{5}R=1944\ \mathrm{J/(mol\,K)}$ で，$(10/342)^3=2.50\times10^{-5}$ なので，

$$
\finalanswer{C_V\approx4.9\times10^{-2}\ \mathrm{J/(mol\,K)}}
$$

となります。音速から求めた $\Theta_{\mathrm{D}}$ は，比熱の測定から得られる銅の値 $343\ \mathrm{K}$ とよく一致します。10 K の比熱は，デュロン・プティの値の 0.2% ほどしかありません。

===== FILE: 06solid_state/05/05_040.md =====
---
tags:
  - 発展
---

# 熱膨張とグリュナイゼン定数

## 問題
$N$ 個の原子からなる体積 $V$ の結晶を考える。基準振動の角振動数 $\omega_s$（$s=1,\ldots,3N$）は $V$ に依存するが，温度にはよらないとする（準調和近似）。このとき結晶のヘルムホルツ自由エネルギーは

$$
F(V,T)=U_0(V)+\sum_{s}\left[\frac{\hbar\omega_s}{2}+k_{\mathrm{B}}T\ln\left(1-e^{-\hbar\omega_s/k_{\mathrm{B}}T}\right)\right]
$$

で与えられる。$U_0(V)$ は原子が静止しているときのエネルギーで，$V=V_0$ で極小をとる。$B_0=V_0U_0''(V_0)$ とおく。グリュナイゼン定数を $\gamma_{\mathrm{G}}=-\dfrac{\mathrm{d}\ln\omega_s}{\mathrm{d}\ln V}$ で定義し，これはすべてのモードで等しい定数であるとする。振動のエネルギーを $E_{\mathrm{vib}}=\sum_s\hbar\omega_s\left(\langle n_s\rangle+\dfrac{1}{2}\right)$，$\langle n_s\rangle=\dfrac{1}{e^{\hbar\omega_s/k_{\mathrm{B}}T}-1}$ とし，定積比熱を $C_V=(\partial E_{\mathrm{vib}}/\partial T)_V$，体膨張係数を $\alpha_V=\dfrac{1}{V}\left(\dfrac{\partial V}{\partial T}\right)_p$ とする。$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。以下の問いに答えよ。

(1) 圧力 $p=-(\partial F/\partial V)_T$ を，$U_0$，$\gamma_{\mathrm{G}}$，$E_{\mathrm{vib}}$，$V$ を用いて表せ。

(2) $p=0$ のもとで，$V-V_0$ が $V_0$ に比べて小さいとして1次の近似をとり，$\alpha_V$ を $\gamma_{\mathrm{G}}$，$C_V$，$B_0$，$V_0$ で表せ。

(3) 質量 $M$ の原子 $N$ 個が格子定数 $a$ で一直線上に並び，最近接原子の間だけに対ポテンシャル $\phi(r)$ がはたらく一次元の鎖を考える。鎖の長さを $L=Na$ とし，周期境界条件を課す。基準振動は波数 $k=\dfrac{2\pi m}{Na}$（$m$ は整数）で指定され，角振動数は $\omega_k=2\sqrt{\dfrac{\phi''(a)}{M}}\left|\sin\dfrac{ka}{2}\right|$ である。$\gamma_{\mathrm{G}}=-\dfrac{\mathrm{d}\ln\omega_k}{\mathrm{d}\ln L}$ を $a$ と $\phi$ の導関数で表せ。さらに，$\phi(r)=4\varepsilon\left[\left(\dfrac{\sigma}{r}\right)^{12}-\left(\dfrac{\sigma}{r}\right)^6\right]$（$\varepsilon>0$，$\sigma>0$）で $a=2^{1/6}\sigma$ のときの $\gamma_{\mathrm{G}}$ を求めよ。

(4) 銅の値 $\gamma_{\mathrm{G}}=2.0$，$B_0=1.37\times10^{11}\ \mathrm{Pa}$，モル体積 $7.11\times10^{-6}\ \mathrm{m^3/mol}$ を用い，室温の $C_V$ をデュロン・プティの値 $3R$（$R=8.314\ \mathrm{J/(mol\,K)}$）として，線膨張係数 $\alpha_L=\alpha_V/3$ を求めよ。また，デバイ温度 $\Theta_{\mathrm{D}}$ より十分低い温度で $C_V=\dfrac{12\pi^4}{5}Nk_{\mathrm{B}}\left(\dfrac{T}{\Theta_{\mathrm{D}}}\right)^3$ を用いて，$\alpha_V$ を $T$ の関数として表せ。

---

## 解答・解説

### (1)
自由エネルギーの括弧の中は $\omega_s$ を通して $V$ に依存するので，$\omega_s$ で微分してから $\mathrm{d}\omega_s/\mathrm{d}V$ をかけます。

$$
\frac{\partial}{\partial\omega_s}\left[\frac{\hbar\omega_s}{2}+k_{\mathrm{B}}T\ln\left(1-e^{-\hbar\omega_s/k_{\mathrm{B}}T}\right)\right]=\frac{\hbar}{2}+\frac{\hbar e^{-\hbar\omega_s/k_{\mathrm{B}}T}}{1-e^{-\hbar\omega_s/k_{\mathrm{B}}T}}=\hbar\left(\langle n_s\rangle+\frac{1}{2}\right)
$$

グリュナイゼン定数の定義から $\dfrac{\mathrm{d}\omega_s}{\mathrm{d}V}=-\gamma_{\mathrm{G}}\dfrac{\omega_s}{V}$ です。これをかけて $s$ について足し，符号を変えると，

$$
\finalanswer{p=-\frac{\mathrm{d}U_0}{\mathrm{d}V}+\gamma_{\mathrm{G}}\frac{E_{\mathrm{vib}}}{V}}
$$

となります。第2項は格子振動が押し広げる圧力で，熱圧力ともよばれます。

### (2)
$U_0$ を $V_0$ のまわりで展開すると，$U_0'(V_0)=0$ なので $U_0'(V)\approx U_0''(V_0)(V-V_0)=B_0\dfrac{V-V_0}{V_0}$ です。これを (1) で $p=0$ とおいた式に入れ，右辺の $V$ を $V_0$ で置き換えます。

$$
\frac{V-V_0}{V_0}=\frac{\gamma_{\mathrm{G}}E_{\mathrm{vib}}}{B_0V_0}
$$

両辺を $T$ で微分すると，零点エネルギーは温度によらないので消え，$C_V$ だけが残ります。

$$
\finalanswer{\alpha_V=\frac{\gamma_{\mathrm{G}}C_V}{B_0V_0}}
$$

となります。これをグリュナイゼンの関係式とよびます。$\gamma_{\mathrm{G}}>0$ なら結晶は温まると膨張します。

### (3)
$ka=2\pi m/N$ は $a$ によらないので，$\sin(ka/2)$ も $a$ によりません。したがって $\omega_k\propto\sqrt{\phi''(a)}$ です。$N$ は一定なので $\mathrm{d}\ln L=\mathrm{d}\ln a$ で，

$$
\frac{\mathrm{d}\ln\omega_k}{\mathrm{d}\ln a}=\frac{a}{2}\cdot\frac{\phi'''(a)}{\phi''(a)}
$$

となります。符号を変えると，

$$
\finalanswer{\gamma_{\mathrm{G}}=-\frac{a\,\phi'''(a)}{2\,\phi''(a)}}
$$

となります。調和ポテンシャルでは $\phi'''=0$ なので $\gamma_{\mathrm{G}}=0$ となり，熱膨張は起こりません。熱膨張は非調和性から生じる効果です。

次にレナード・ジョーンズ型の微分を計算し，$a=2^{1/6}\sigma$ で $(\sigma/a)^6=\dfrac{1}{2}$，$(\sigma/a)^{12}=\dfrac{1}{4}$ を代入します。

$$
\begin{aligned}
\phi''(a)&=\frac{4\varepsilon}{a^2}\left[156\left(\frac{\sigma}{a}\right)^{12}-42\left(\frac{\sigma}{a}\right)^6\right]=\frac{72\varepsilon}{a^2}\\
\phi'''(a)&=\frac{4\varepsilon}{a^3}\left[-2184\left(\frac{\sigma}{a}\right)^{12}+336\left(\frac{\sigma}{a}\right)^6\right]=-\frac{1512\varepsilon}{a^3}
\end{aligned}
$$

これを代入すると，

$$
\finalanswer{\gamma_{\mathrm{G}}=\frac{1512}{144}=10.5}
$$

となります。反発側が急で引力側がゆるやかなため $\phi'''<0$ となり，$\gamma_{\mathrm{G}}$ は正になります。

### (4)
(2) の式に数値を代入します。$C_V=3R=24.94\ \mathrm{J/(mol\,K)}$，$B_0V_0=1.37\times10^{11}\times7.11\times10^{-6}=9.74\times10^5\ \mathrm{J/mol}$ です。

$$
\alpha_V=\frac{2.0\times24.94}{9.74\times10^5}\ \mathrm{K^{-1}}=5.12\times10^{-5}\ \mathrm{K^{-1}}
$$

3で割ると，

$$
\finalanswer{\alpha_L\approx1.7\times10^{-5}\ \mathrm{K^{-1}}}
$$

となります。銅の測定値 $1.65\times10^{-5}\ \mathrm{K^{-1}}$ とよく一致します。低温では比熱の $T^3$ 則を代入して，

$$
\finalanswer{\alpha_V=\frac{12\pi^4}{5}\cdot\frac{\gamma_{\mathrm{G}}Nk_{\mathrm{B}}}{B_0V_0}\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^3}
$$

となります。熱膨張係数は比熱と同じく $T^3$ に比例して0に近づき，熱力学第3法則と矛盾しません。

===== FILE: 06solid_state/05/05_050.md =====
---
tags:
  - 発展
---

# フォノンによる熱伝導

## 問題
絶縁体の結晶では，熱はおもにフォノンが運ぶ。フォノンを，数密度 $n_{\mathrm{ph}}$ の粒子の気体とみなす。粒子はすべて同じ速さ $v$ をもち，向きは等方的に分布しているとする。$z$ 方向に温度勾配 $\mathrm{d}T/\mathrm{d}z$ があり，各粒子は平均時間 $\tau$ ごとに衝突して，その場所の温度での平均エネルギー $\varepsilon(T)$ をもつようになるとする。速度の $z$ 成分が $v_z$ の粒子は，位置 $z-v_z\tau$ で最後に衝突したとみなす。$n_{\mathrm{ph}}$ は場所によらず一定とし，単位体積あたりの熱容量を $c=n_{\mathrm{ph}}\,\mathrm{d}\varepsilon/\mathrm{d}T$，平均自由行程を $\ell=v\tau$ とする。熱流密度は $j_z=n_{\mathrm{ph}}\langle v_z\varepsilon\rangle$（$\langle\cdots\rangle$ は向きについての平均）であり，熱伝導率 $\kappa$ を $j_z=-\kappa\,\mathrm{d}T/\mathrm{d}z$ で定義する。デバイ温度を $\Theta_{\mathrm{D}}$，ボルツマン定数を $k_{\mathrm{B}}$ とする。以下の問いに答えよ。

(1) $\kappa$ を $c$，$v$，$\ell$ で表せ。

(2) $T\gg\Theta_{\mathrm{D}}$ では $c$ と $v$ は温度によらず，$\ell$ は各モードのフォノン数の平均 $\langle n\rangle=\dfrac{1}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}$ に反比例するとする。$\kappa\propto T^{p}$ と書いたときの $p$ を求めよ。

(3) 格子定数 $a$ の一次元の結晶で，フォノンの波数 $q$ を $-\pi/a<q\le\pi/a$ にとる。波数 $q\ (>0)$ の2つのフォノンが衝突して1つのフォノン $q'$ になるとき，結晶運動量の保存は $q+q=q'+G$ と書ける。ここで $q'$ も同じ範囲にあり，$G$ は $2\pi/a$ の整数倍である。$G\ne0$ となる過程（ウムクラップ過程）が起こるための $q$ の条件を求めよ。エネルギー保存は他の分枝との組合せで満たされるとし，ここでは考えない。さらに，分散を $\omega=v|q|$，$\Theta_{\mathrm{D}}=\dfrac{\hbar v\pi}{ak_{\mathrm{B}}}$ として，この条件を満たすフォノンのエネルギーの最小値を $k_{\mathrm{B}}\Theta_{\mathrm{D}}$ で表せ。$T\ll\Theta_{\mathrm{D}}$ で $\ell$ がこのエネルギーのフォノン数の平均に反比例するとき，$\ell$ の主要な温度依存性を求めよ。

(4) さらに低温では，$\ell$ は試料の太さ $D$ に等しくなる。$c$ をデバイの $T^3$ 則 $c=\dfrac{12\pi^4}{5}nk_{\mathrm{B}}\left(\dfrac{T}{\Theta_{\mathrm{D}}}\right)^3$（$n$ は原子の数密度）で表すとき，$\kappa$ の温度依存性を求めよ。また，ケイ素の値 $n=5.0\times10^{28}\ \mathrm{m^{-3}}$，$\Theta_{\mathrm{D}}=645\ \mathrm{K}$，$v=6.0\times10^3\ \mathrm{m/s}$ と $D=1.0\ \mathrm{mm}$ を用いて，$T=4.0\ \mathrm{K}$ での $\kappa$ を求めよ。$k_{\mathrm{B}}=1.381\times10^{-23}\ \mathrm{J/K}$ とする。

---

## 解答・解説

### (1)
粒子のエネルギーは最後に衝突した場所の温度で決まるので，$\varepsilon(T(z-v_z\tau))$ を $v_z\tau$ の1次まで展開します。

$$
\varepsilon(T(z-v_z\tau))\approx\varepsilon(T(z))-v_z\tau\frac{\mathrm{d}\varepsilon}{\mathrm{d}T}\frac{\mathrm{d}T}{\mathrm{d}z}
$$

向きの平均をとると，$\langle v_z\rangle=0$ なので第1項は消えます。等方的な分布では $\langle v_z^{\,2}\rangle=v^2\langle\cos^2\theta\rangle=v^2/3$ です。

$$
j_z=-n_{\mathrm{ph}}\frac{v^2}{3}\tau\frac{\mathrm{d}\varepsilon}{\mathrm{d}T}\frac{\mathrm{d}T}{\mathrm{d}z}=-\frac{1}{3}cv^2\tau\frac{\mathrm{d}T}{\mathrm{d}z}
$$

$v\tau=\ell$ を使うと，

$$
\finalanswer{\kappa=\frac{1}{3}cv\ell}
$$

となります。気体分子運動論の熱伝導率と同じ形です。

### (2)
$T\gg\Theta_{\mathrm{D}}$ ではすべてのモードで $\hbar\omega\ll k_{\mathrm{B}}T$ なので，$\langle n\rangle\approx k_{\mathrm{B}}T/\hbar\omega$ となり，$T$ に比例します。したがって $\ell\propto1/T$ です。$c$ と $v$ は一定なので，

$$
\finalanswer{p=-1}
$$

となります。高温では，フォノンの数が増えるほど互いに散乱し合って，熱が伝わりにくくなります。

### (3)
$G=0$ で済むのは，$2q$ が範囲 $-\pi/a<q'\le\pi/a$ に入るとき，すなわち $q\le\pi/2a$ のときです。$2q$ がこの範囲を超えると，$G=2\pi/a$ を引かないと $q'$ が範囲に戻りません。

$$
\finalanswer{q>\frac{\pi}{2a}}
$$

この過程を図に示します。

<!-- FIGURE solution (3): 横向きの数直線を k 軸とし，−π/a，0，π/a に目盛りを付け，−π/a から π/a の区間を太線にして「第1ブリルアンゾーン」と注記する。0 から右向きの矢印 q を2本つないで描き（各長さは π/a の 0.7 倍ほど），合計 2q の先端がゾーンの右端 π/a を越えて外に出る様子を示す。その先端から左へ長さ 2π/a の矢印を描いて G とラベルし，ゾーン内に戻った点を q' = 2q − 2π/a（負の値）として黒丸で示す。 -->

このようなフォノンのエネルギーは $\hbar vq$ より大きく，$\Theta_{\mathrm{D}}$ の定義から $\hbar v\pi/a=k_{\mathrm{B}}\Theta_{\mathrm{D}}$ なので，

$$
\finalanswer{\hbar\omega_{\min}=\frac{k_{\mathrm{B}}\Theta_{\mathrm{D}}}{2}}
$$

となります。$T\ll\Theta_{\mathrm{D}}$ では，このエネルギーのフォノン数の平均は $\langle n\rangle\approx e^{-\Theta_{\mathrm{D}}/2T}$ です。$\ell$ はこれに反比例するので，

$$
\finalanswer{\ell\propto e^{\Theta_{\mathrm{D}}/2T}}
$$

となります。$G=0$ の正常過程ではフォノン全体の結晶運動量が変わらないので，熱流は減衰しません。熱抵抗を生むのはウムクラップ過程です。低温ではその頻度が指数関数的に小さくなるので，$\ell$ は急激に伸びます。

### (4)
$\ell=D$ は温度によらないので，$\kappa=\dfrac{1}{3}cvD$ の温度依存性は $c$ と同じです。

$$
\finalanswer{\kappa\propto T^3}
$$

数値を代入します。$\dfrac{12\pi^4}{5}nk_{\mathrm{B}}=1.614\times10^8\ \mathrm{J/(m^3\,K)}$，$(4.0/645)^3=2.385\times10^{-7}$ なので，$c=38.5\ \mathrm{J/(m^3\,K)}$ です。

$$
\kappa=\frac{1}{3}\times38.5\times6.0\times10^3\times1.0\times10^{-3}\ \mathrm{W/(m\,K)}
$$

より，

$$
\finalanswer{\kappa\approx77\ \mathrm{W/(m\,K)}}
$$

となります。熱伝導率の温度依存性の全体像を図に示します。

<!-- FIGURE solution (4): 両対数グラフ。横軸 T（対数），縦軸 κ（対数）。左の低温側は傾き 3 の直線で立ち上がり（「∝T³，境界散乱」と注記），極大を経て，中間温度では急激に減少し（「∝ e^{Θ_D/2T}，ウムクラップ」と注記），右の高温側は傾き −1 の直線になる（「∝ 1/T」と注記）。極大の位置に縦の点線を引く。目盛りの数値は入れなくてよい。 -->

低温の熱伝導率は試料の大きさや表面の状態に左右されます。極大の位置はおよそ $\Theta_{\mathrm{D}}$ の数十分の1の温度にきます。

===== FILE: 06solid_state/05/05_060.md =====
---
tags:
  - 標準
---

# 低次元系の比熱

## 問題
面積 $A$ の平面内に $N$ 個の原子が並んだ2次元の結晶を考え，原子の面密度を $n=N/A$ とする。原子は面内でだけ動き，格子振動は縦波と横波の2つの分枝からなる。どちらの分枝も分散 $\omega=vk$（$k=|\boldsymbol{k}|$，$v$ は一定）に従うとする。周期境界条件を課し，$A$ は十分大きいとする。デバイ模型にならって，2つの分枝に共通の角振動数 $\omega_{\mathrm{D}}$ 以下のモードだけがあり，その総数が $2N$ になるとする。$\Theta_{\mathrm{D}}=\hbar\omega_{\mathrm{D}}/k_{\mathrm{B}}$ とし，角振動数 $\omega$ のモードの熱エネルギーの平均を $\dfrac{\hbar\omega}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}$ とする。$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。必要なら $\displaystyle\int_0^\infty\frac{x}{e^x-1}\,\mathrm{d}x=\frac{\pi^2}{6}$ と $\displaystyle\int_0^\infty\frac{x^2}{e^x-1}\,\mathrm{d}x=2\zeta(3)$，$\zeta(3)=1.202$ を用いてよい。以下の問いに答えよ。

(1) 状態密度 $D(\omega)$（$0<\omega<\omega_{\mathrm{D}}$）を求め，$\omega_{\mathrm{D}}$ を $v$ と $n$ で表せ。

(2) $T\ll\Theta_{\mathrm{D}}$ での比熱 $C$ を，$N$，$k_{\mathrm{B}}$，$T/\Theta_{\mathrm{D}}$ で表せ。

(3) $d$ 次元の結晶で，低振動数の状態密度が $D(\omega)\propto\omega^{d-1}$ となるとする。十分低温での比熱の温度依存性を求めよ。

(4) 原子1層からなる膜では，面に垂直な方向の振動の分枝もあり，その分散は $\omega=bk^2$（$b>0$ は定数）となる。この分枝だけの状態密度 $D_{\mathrm{f}}(\omega)$ と，十分低温での比熱 $C_{\mathrm{f}}$ を求めよ。

---

## 解答・解説

### (1)
2次元では，許される $\boldsymbol{k}$ が面積 $(2\pi)^2/A$ ごとに1個あります。1つの分枝について，$|\boldsymbol{k}|<\omega/v$ の円の中のモードの数は $\dfrac{A}{(2\pi)^2}\pi\left(\dfrac{\omega}{v}\right)^2$ です。2つの分枝を合わせると $\dfrac{A\omega^2}{2\pi v^2}$ となり，これを $\omega$ で微分すると状態密度になります。

$$
\finalanswer{D(\omega)=\frac{A\omega}{\pi v^2}}
$$

モードの総数を $2N$ とおくと $\dfrac{A\omega_{\mathrm{D}}^{\,2}}{2\pi v^2}=2N$ なので，

$$
\finalanswer{\omega_{\mathrm{D}}=2v\sqrt{\pi n}}
$$

となります。これを使うと $D(\omega)=\dfrac{4N\omega}{\omega_{\mathrm{D}}^{\,2}}$ と書けます。

### (2)
熱エネルギーは，各モードの平均エネルギーを状態密度で重みづけて積分したものです。$x=\hbar\omega/k_{\mathrm{B}}T$ と置き換え，$T\ll\Theta_{\mathrm{D}}$ なので上限を $\infty$ にします。

$$
E=\int_0^{\infty}\frac{4N\omega}{\omega_{\mathrm{D}}^{\,2}}\cdot\frac{\hbar\omega}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}\,\mathrm{d}\omega=4Nk_{\mathrm{B}}T\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^2\cdot2\zeta(3)
$$

これを $T$ で微分すると，

$$
\finalanswer{C=24\zeta(3)Nk_{\mathrm{B}}\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^2\approx28.8\,Nk_{\mathrm{B}}\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^2}
$$

となります。3次元の $T^3$ 則に対して，2次元では $T^2$ になります。

### (3)
低温では上限を $\infty$ にしてよいので，熱エネルギーは $\displaystyle E\propto\int_0^\infty\omega^{d-1}\frac{\hbar\omega}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}\,\mathrm{d}\omega$ です。$\omega=k_{\mathrm{B}}Tx/\hbar$ と置き換えると，温度は積分の外に $T^{d+1}$ として出ます。

$$
E\propto T^{d+1}\int_0^\infty\frac{x^d}{e^x-1}\,\mathrm{d}x
$$

積分は $T$ によらない定数なので，

$$
\finalanswer{C\propto T^{d}}
$$

となります。$d=3$ がデバイの $T^3$ 則，$d=2$ が (2) の結果にあたります。指数は線形分散の音響モードの数え方だけで決まります。

### (4)
$|\boldsymbol{k}|<k$ の円の中のモードの数は $\dfrac{A}{4\pi}k^2$ で，$k^2=\omega/b$ を代入すると $\dfrac{A\omega}{4\pi b}$ です。これを $\omega$ で微分すると，

$$
\finalanswer{D_{\mathrm{f}}(\omega)=\frac{A}{4\pi b}}
$$

となり，状態密度は $\omega$ によらない定数です。熱エネルギーは (2) と同様に計算できます。

$$
E_{\mathrm{f}}=\frac{A}{4\pi b}\int_0^\infty\frac{\hbar\omega}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}\,\mathrm{d}\omega=\frac{A}{4\pi b}\cdot\frac{(k_{\mathrm{B}}T)^2}{\hbar}\cdot\frac{\pi^2}{6}
$$

これを $T$ で微分すると，

$$
\finalanswer{C_{\mathrm{f}}=\frac{\pi Ak_{\mathrm{B}}^{\,2}}{12\hbar b}T}
$$

となります。$T$ に比例するこの寄与は，面内の分枝による $T^2$ の寄与より低温でゆっくり減ります。そのため十分低温では，面に垂直な振動が比熱を支配します。

===== FILE: 06solid_state/06/06_010.md =====
---
tags:
  - 基本
---

# 箱の中の自由電子とフェルミ波数

## 問題
一辺 $L$ の立方体（体積 $V=L^3$）の中に，質量 $m$ の電子が $N$ 個あり，互いに相互作用せず自由に運動するとする。波動関数には周期境界条件 $\psi(x+L,y,z)=\psi(x,y+L,z)=\psi(x,y,z+L)=\psi(x,y,z)$ を課す。電子のスピンの自由度は2で，絶対零度の基底状態を考える。電子の数密度を $n=N/V$ とする。以下の問いに答えよ。

(1) 1電子のシュレーディンガー方程式を解き，規格化された波動関数，許される波数ベクトル $\boldsymbol{k}$，エネルギー $E$ を求めよ。

(2) 基底状態で占有される最大の波数（フェルミ波数）$k_{\mathrm{F}}$ を $n$ で表し，フェルミエネルギー $E_{\mathrm{F}}$ を求めよ。

(3) ナトリウムでは $n=2.65\times10^{28}\ \mathrm{m^{-3}}$ である。$k_{\mathrm{F}}$，$E_{\mathrm{F}}$（eV 単位），フェルミ速度 $v_{\mathrm{F}}=\hbar k_{\mathrm{F}}/m$，フェルミ温度 $T_{\mathrm{F}}=E_{\mathrm{F}}/k_{\mathrm{B}}$ を求めよ。$\hbar=1.055\times10^{-34}\ \mathrm{J\,s}$，$m=9.109\times10^{-31}\ \mathrm{kg}$，$e=1.602\times10^{-19}\ \mathrm{C}$，$k_{\mathrm{B}}=1.381\times10^{-23}\ \mathrm{J/K}$ とする。

(4) 基底状態の全エネルギー $E_0$ を $N$ と $E_{\mathrm{F}}$ で表せ。また，$N$ を一定に保ったときの圧力 $p=-\partial E_0/\partial V$ と体積弾性率 $B=-V\,\partial p/\partial V$ を $n$ と $E_{\mathrm{F}}$ で表し，ナトリウムについて数値を求めよ。

---

## 解答・解説

### (1)
ポテンシャルがないので，シュレーディンガー方程式 $-\dfrac{\hbar^2}{2m}\nabla^2\psi=E\psi$ の解は平面波です。周期境界条件から $e^{ik_xL}=1$ などが必要で，各成分は $2\pi/L$ の整数倍に限られます。

$$
\finalanswer{\psi_{\boldsymbol{k}}=\frac{1}{\sqrt{V}}e^{i\boldsymbol{k}\cdot\boldsymbol{r}},\quad \boldsymbol{k}=\frac{2\pi}{L}(n_x,n_y,n_z),\quad E=\frac{\hbar^2k^2}{2m}}
$$

となります。$n_x,n_y,n_z$ は整数です。許される $\boldsymbol{k}$ は，波数空間で体積 $(2\pi/L)^3$ ごとに1個ずつ並びます。

### (2)
基底状態では，エネルギーの低い状態から順に，各 $\boldsymbol{k}$ に電子が2個ずつ入ります。そのため占有される状態は半径 $k_{\mathrm{F}}$ の球の内部になります。球の中の状態の数にスピンの2をかけて $N$ とおきます。

$$
N=2\cdot\frac{\frac{4\pi}{3}k_{\mathrm{F}}^{\,3}}{(2\pi/L)^3}=\frac{Vk_{\mathrm{F}}^{\,3}}{3\pi^2}
$$

より，

$$
\finalanswer{k_{\mathrm{F}}=\left(3\pi^2n\right)^{1/3}},\qquad \finalanswer{E_{\mathrm{F}}=\frac{\hbar^2}{2m}\left(3\pi^2n\right)^{2/3}}
$$

となります。フェルミ波数は電子密度だけで決まり，箱の形や大きさにはよりません。

この球を図に示します。

<!-- FIGURE solution (2): 波数空間の k_z = 0 の断面を描く。k_x，k_y 軸を引き，間隔 2π/L の正方格子状に小さな点を並べる（各方向に ±8 個程度）。原点を中心に半径 k_F の円を描き，円の内側の点を黒，外側の点を白抜きにする。隣り合う点の間隔に 2π/L，円の半径に k_F とラベル。 -->

### (3)
$3\pi^2n=7.846\times10^{29}\ \mathrm{m^{-3}}$ の3乗根をとると，

$$
\finalanswer{k_{\mathrm{F}}\approx9.22\times10^{9}\ \mathrm{m^{-1}}}
$$

です。これを (2) の式に代入すると $E_{\mathrm{F}}=5.20\times10^{-19}\ \mathrm{J}$ で，$e$ で割って eV に直します。

$$
\finalanswer{E_{\mathrm{F}}\approx3.24\ \mathrm{eV}},\qquad \finalanswer{v_{\mathrm{F}}\approx1.07\times10^6\ \mathrm{m/s}},\qquad \finalanswer{T_{\mathrm{F}}\approx3.76\times10^4\ \mathrm{K}}
$$

となります。フェルミ温度は室温の100倍以上なので，室温の金属の電子は絶対零度の状態に近いといえます。

### (4)
全エネルギーは，フェルミ球内の各状態のエネルギーにスピンの2をかけて足したものです。和を積分に直すと，

$$
E_0=2\cdot\frac{V}{(2\pi)^3}\int_0^{k_{\mathrm{F}}}\frac{\hbar^2k^2}{2m}4\pi k^2\,\mathrm{d}k=\frac{V}{\pi^2}\cdot\frac{\hbar^2}{2m}\cdot\frac{k_{\mathrm{F}}^{\,5}}{5}
$$

となります。$N=Vk_{\mathrm{F}}^{\,3}/3\pi^2$ を使うと，

$$
\finalanswer{E_0=\frac{3}{5}NE_{\mathrm{F}}}
$$

です。$N$ が一定なら $E_{\mathrm{F}}\propto V^{-2/3}$ なので $E_0\propto V^{-2/3}$ で，$p=\dfrac{2E_0}{3V}$ となります。さらに $p\propto V^{-5/3}$ から $B=\dfrac{5}{3}p$ です。

$$
\finalanswer{p=\frac{2}{5}nE_{\mathrm{F}}\approx5.5\times10^9\ \mathrm{Pa}},\qquad \finalanswer{B=\frac{2}{3}nE_{\mathrm{F}}\approx9.2\times10^9\ \mathrm{Pa}}
$$

となります。この圧力は電子を閉じ込めているイオンとの引力が支えます。ナトリウムの体積弾性率の測定値は約 $6\times10^9\ \mathrm{Pa}$ で，自由電子の値と同じ程度です。

===== FILE: 06solid_state/06/06_020.md =====
---
tags:
  - 基本
---

# 状態密度とフェルミエネルギー

## 問題
質量 $m$ の自由電子が，一辺 $L$ の $d$ 次元の箱（$d=1,2,3$）の中にあるとし，周期境界条件を課す。エネルギーは $E=\dfrac{\hbar^2k^2}{2m}$ である。スピンを含めて，エネルギーが $E$ と $E+\mathrm{d}E$ の間にある1電子状態の数を $D(E)\,\mathrm{d}E$ とし，$D(E)$ を状態密度とよぶ。電子の数を $N$，数密度を $n=N/L^d$ とし，絶対零度での最高占有エネルギーをフェルミエネルギー $E_{\mathrm{F}}$ とする。以下の問いに答えよ。

(1) 3次元（体積 $V=L^3$）の $D(E)$ を求め，$D(E_{\mathrm{F}})$ を $N$ と $E_{\mathrm{F}}$ で表せ。

(2) 2次元（面積 $A=L^2$）の $D(E)$ と，$E_{\mathrm{F}}$ を $n$ で表した式を求めよ。また，半導体界面の2次元電子系で，電子が質量 $m^*=0.067m$ の自由粒子として振る舞い，$n=3.0\times10^{15}\ \mathrm{m^{-2}}$ のときの $E_{\mathrm{F}}$ を meV 単位で求めよ。$\hbar=1.055\times10^{-34}\ \mathrm{J\,s}$，$m=9.109\times10^{-31}\ \mathrm{kg}$，$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

(3) 1次元（長さ $L$）の $D(E)$ と，$E_{\mathrm{F}}$ を $n$ で表した式を求めよ。

(4) エネルギーが $E$ 以下の状態の数 $\mathcal{N}(E)$ が $E^{d/2}$ に比例することを用いて，$d=1,2,3$ に共通な式として $D(E_{\mathrm{F}})$ を $d$，$N$，$E_{\mathrm{F}}$ で表せ。

---

## 解答・解説

### (1)
まずエネルギーが $E$ 以下の状態の数を数え，それを $E$ で微分します。3次元では許される $\boldsymbol{k}$ が体積 $(2\pi/L)^3$ ごとに1個あるので，半径 $k=\sqrt{2mE}/\hbar$ の球の中の状態の数は，スピンを含めて次のようになります。

$$
\mathcal{N}(E)=2\cdot\frac{V}{(2\pi)^3}\cdot\frac{4\pi}{3}k^3=\frac{V}{3\pi^2}\left(\frac{2mE}{\hbar^2}\right)^{3/2}
$$

これを $E$ で微分すると，

$$
\finalanswer{D(E)=\frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}}
$$

となります。$\mathcal{N}(E_{\mathrm{F}})=N$ なので，$D(E)=\dfrac{3}{2}\cdot\dfrac{\mathcal{N}(E)}{E}$ に $E=E_{\mathrm{F}}$ を代入して，

$$
\finalanswer{D(E_{\mathrm{F}})=\frac{3N}{2E_{\mathrm{F}}}}
$$

となります。

### (2)
2次元では，$\boldsymbol{k}$ が面積 $(2\pi/L)^2$ ごとに1個あるので，半径 $k$ の円の中の状態の数は次のとおりです。

$$
\mathcal{N}(E)=2\cdot\frac{A}{(2\pi)^2}\pi k^2=\frac{AmE}{\pi\hbar^2}
$$

$E$ に比例するので，状態密度は定数になります。$\mathcal{N}(E_{\mathrm{F}})=N$ とおくと $E_{\mathrm{F}}$ が求まります。

$$
\finalanswer{D(E)=\frac{Am}{\pi\hbar^2}},\qquad \finalanswer{E_{\mathrm{F}}=\frac{\pi\hbar^2n}{m}}
$$

$m$ を $m^*=6.103\times10^{-32}\ \mathrm{kg}$ に置き換えて数値を代入すると，$E_{\mathrm{F}}=1.72\times10^{-21}\ \mathrm{J}$ なので，

$$
\finalanswer{E_{\mathrm{F}}\approx10.7\ \mathrm{meV}}
$$

となります。金属の数 eV に比べてずっと小さく，フェルミ温度は約 120 K です。

### (3)
1次元では $k$ が間隔 $2\pi/L$ で並び，$|k|$ 以下の範囲は $-k$ から $k$ までの長さ $2k$ なので，

$$
\mathcal{N}(E)=2\cdot\frac{2k}{2\pi/L}=\frac{2L}{\pi\hbar}\sqrt{2mE}
$$

となります。これを微分し，$\mathcal{N}(E_{\mathrm{F}})=N$ から $k_{\mathrm{F}}=\pi n/2$ を求めます。

$$
\finalanswer{D(E)=\frac{L}{\pi\hbar}\sqrt{\frac{2m}{E}}},\qquad \finalanswer{E_{\mathrm{F}}=\frac{\pi^2\hbar^2n^2}{8m}}
$$

となります。1次元の状態密度はバンドの底 $E\to0$ で発散します。

### (4)
$\mathcal{N}(E)=CE^{d/2}$ と書くと，$D(E)=\dfrac{\mathrm{d}\mathcal{N}}{\mathrm{d}E}=\dfrac{d}{2}\cdot\dfrac{\mathcal{N}(E)}{E}$ です。$E=E_{\mathrm{F}}$ では $\mathcal{N}=N$ なので，

$$
\finalanswer{D(E_{\mathrm{F}})=\frac{dN}{2E_{\mathrm{F}}}}
$$

となります。$d=3$ では (1) の結果に一致します。$d=2$ では $D=N/E_{\mathrm{F}}$ となり (2) の $\dfrac{Am}{\pi\hbar^2}$ と，$d=1$ では $D=N/2E_{\mathrm{F}}$ となり (3) の結果と一致します。3つの次元の状態密度を図に示します。

<!-- FIGURE solution (4): 横に3つの小さなグラフを並べる。どれも横軸 E（0 から右へ），縦軸 D(E)。左「3次元」は √E に比例して増える曲線，中央「2次元」は E > 0 で一定の水平線（E = 0 で 0 から立ち上がる段差），右「1次元」は E → 0 で発散し 1/√E で減る曲線。各グラフに E_F の位置の縦の破線を引き，E_F 以下の部分を薄く塗る。 -->

金属の性質を決める $E_{\mathrm{F}}$ 付近の状態密度は，どの次元でも $N/E_{\mathrm{F}}$ と同じ程度の大きさになります。

===== FILE: 06solid_state/06/06_030.md =====
---
tags:
  - 標準
---

# 電子比熱とゾンマーフェルト展開

## 問題
自由電子気体のフェルミ分布関数を $f(E)=\dfrac{1}{e^{(E-\mu)/k_{\mathrm{B}}T}+1}$ とする。$\mu$ は化学ポテンシャル，$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。$H(E)$ を $E<0$ で0となる滑らかな関数とし，$k_{\mathrm{B}}T\ll\mu$ の低温を考える。スピンを含めた状態密度を $D(E)$，電子数を $N$，絶対零度での化学ポテンシャルをフェルミエネルギー $E_{\mathrm{F}}$ とする。必要なら $\displaystyle\int_{-\infty}^{\infty}\frac{x^2e^x}{(e^x+1)^2}\,\mathrm{d}x=\frac{\pi^2}{3}$ を用いてよい。以下の問いに答えよ。

(1) $T^2$ の項までの近似で，次の式が成り立つことを示せ。

$$
\int_0^\infty H(E)f(E)\,\mathrm{d}E\approx\int_0^\mu H(E)\,\mathrm{d}E+\frac{\pi^2}{6}(k_{\mathrm{B}}T)^2H'(\mu)
$$

(2) 電子数が一定であることから，$\mu$ を $T^2$ の項まで $D(E_{\mathrm{F}})$，$D'(E_{\mathrm{F}})$ で表せ。また，3次元の自由電子 $D(E)\propto\sqrt{E}$ の場合の $\mu$ を $E_{\mathrm{F}}$ と $k_{\mathrm{B}}T$ で表せ。

(3) 内部エネルギー $U(T)$ を $T^2$ の項まで求め，電子比熱 $C_{\mathrm{el}}=\gamma T$ の $\gamma$ を $D(E_{\mathrm{F}})$ で表せ。また，3次元の自由電子について，$C_{\mathrm{el}}$ を $N$，$k_{\mathrm{B}}$，$T$，フェルミ温度 $T_{\mathrm{F}}=E_{\mathrm{F}}/k_{\mathrm{B}}$ で表せ。

(4) ナトリウムを1価の3次元自由電子金属とみなし，$T_{\mathrm{F}}=3.76\times10^4\ \mathrm{K}$ とする。1 mol あたりの $\gamma$ を $\mathrm{mJ/(mol\,K^2)}$ 単位で求めよ。また，$T=300\ \mathrm{K}$ での電子比熱と格子比熱 $3R$ の比を求めよ。気体定数を $R=8.314\ \mathrm{J/(mol\,K)}$ とする。

---

## 解答・解説

### (1)
$f$ の微分が $E=\mu$ の近くの幅 $k_{\mathrm{B}}T$ の範囲にだけ値をもつことを利用するため，部分積分で $-\partial f/\partial E$ の積分に直します。$K(E)=\displaystyle\int_0^EH(E')\,\mathrm{d}E'$ とおくと，$K(0)=0$，$f(\infty)=0$ なので境界項は消えます。

$$
\int_0^\infty H f\,\mathrm{d}E=\int_0^\infty K(E)\left(-\frac{\partial f}{\partial E}\right)\mathrm{d}E
$$

$-\partial f/\partial E$ は $E=0$ では $e^{-\mu/k_{\mathrm{B}}T}$ 程度に小さいので，下限を $-\infty$ にしてかまいません。$K$ を $\mu$ のまわりで2次まで展開し，$x=(E-\mu)/k_{\mathrm{B}}T$ とおくと，$-\dfrac{\partial f}{\partial E}=\dfrac{1}{k_{\mathrm{B}}T}\cdot\dfrac{e^x}{(e^x+1)^2}$ です。この関数は $x$ について偶関数で，積分すると1になります。1次の項は奇関数なので消えます。

$$
\int_0^\infty H f\,\mathrm{d}E\approx K(\mu)+\frac{1}{2}K''(\mu)(k_{\mathrm{B}}T)^2\int_{-\infty}^{\infty}\frac{x^2e^x}{(e^x+1)^2}\,\mathrm{d}x
$$

$K''=H'$ と与えられた積分の値を使うと，

$$
\finalanswer{\int_0^\infty H(E)f(E)\,\mathrm{d}E\approx\int_0^\mu H(E)\,\mathrm{d}E+\frac{\pi^2}{6}(k_{\mathrm{B}}T)^2H'(\mu)}
$$

となります。

### (2)
(1) で $H=D$ とおき，電子数が絶対零度の値 $\displaystyle\int_0^{E_{\mathrm{F}}}D\,\mathrm{d}E$ に等しいとします。$\mu-E_{\mathrm{F}}$ は $T^2$ の程度なので，$\displaystyle\int_{E_{\mathrm{F}}}^{\mu}D\,\mathrm{d}E\approx D(E_{\mathrm{F}})(\mu-E_{\mathrm{F}})$ と近似できます。

$$
D(E_{\mathrm{F}})(\mu-E_{\mathrm{F}})+\frac{\pi^2}{6}(k_{\mathrm{B}}T)^2D'(E_{\mathrm{F}})=0
$$

より，

$$
\finalanswer{\mu=E_{\mathrm{F}}-\frac{\pi^2}{6}(k_{\mathrm{B}}T)^2\frac{D'(E_{\mathrm{F}})}{D(E_{\mathrm{F}})}}
$$

となります。$D\propto\sqrt{E}$ では $D'/D=1/2E_{\mathrm{F}}$ なので，

$$
\finalanswer{\mu=E_{\mathrm{F}}\left[1-\frac{\pi^2}{12}\left(\frac{k_{\mathrm{B}}T}{E_{\mathrm{F}}}\right)^2\right]}
$$

となります。状態密度が上に向かって増えるので，同じ電子数を保つには $\mu$ がわずかに下がります。

### (3)
(1) で $H=ED$ とおきます。第1項を $E_{\mathrm{F}}$ のまわりで展開すると，$\displaystyle\int_0^\mu ED\,\mathrm{d}E\approx U_0+E_{\mathrm{F}}D(E_{\mathrm{F}})(\mu-E_{\mathrm{F}})$ です。$U_0$ は絶対零度のエネルギーです。第2項は $\dfrac{\pi^2}{6}(k_{\mathrm{B}}T)^2\left[D(E_{\mathrm{F}})+E_{\mathrm{F}}D'(E_{\mathrm{F}})\right]$ です。(2) の結果を代入すると $D'$ を含む項が打ち消し合い，

$$
\finalanswer{U=U_0+\frac{\pi^2}{6}D(E_{\mathrm{F}})(k_{\mathrm{B}}T)^2}
$$

となります。これを $T$ で微分すると，

$$
\finalanswer{\gamma=\frac{\pi^2}{3}k_{\mathrm{B}}^{\,2}D(E_{\mathrm{F}})}
$$

です。3次元の自由電子では $D(E_{\mathrm{F}})=\dfrac{3N}{2E_{\mathrm{F}}}$ なので，

$$
\finalanswer{C_{\mathrm{el}}=\frac{\pi^2}{2}Nk_{\mathrm{B}}\frac{T}{T_{\mathrm{F}}}}
$$

となります。熱的に励起されるのはフェルミ面の近くの幅 $k_{\mathrm{B}}T$ にある電子だけなので，比熱は古典的な値 $\dfrac{3}{2}Nk_{\mathrm{B}}$ より $T/T_{\mathrm{F}}$ の程度だけ小さくなります。

### (4)
1 mol では $Nk_{\mathrm{B}}=R$ なので，$\gamma=\dfrac{\pi^2R}{2T_{\mathrm{F}}}=\dfrac{4.935\times8.314}{3.76\times10^4}\ \mathrm{J/(mol\,K^2)}$ を計算します。

$$
\finalanswer{\gamma\approx1.09\ \mathrm{mJ/(mol\,K^2)}}
$$

$T=300\ \mathrm{K}$ では $C_{\mathrm{el}}=0.327\ \mathrm{J/(mol\,K)}$ で，$3R=24.94\ \mathrm{J/(mol\,K)}$ との比は，

$$
\finalanswer{\frac{C_{\mathrm{el}}}{3R}\approx1.3\times10^{-2}}
$$

となります。室温では電子比熱は格子比熱の約 1% にすぎず，古典論で電子比熱が観測されない理由がこれで説明できます。ナトリウムの $\gamma$ の測定値は $1.38\ \mathrm{mJ/(mol\,K^2)}$ で，自由電子の値より少し大きくなります。

===== FILE: 06solid_state/06/06_040.md =====
---
tags:
  - 基本
---

# ドルーデ模型と電気伝導度

## 問題
金属中の伝導電子を，数密度 $n$，電荷 $-e$（$e>0$），質量 $m$ の粒子の集まりとみなす。$x$ 方向に一様な電場 $\mathcal{E}$ をかけたとき，電子の平均速度の $x$ 成分 $v$ は，散乱の効果を摩擦力で表した運動方程式

$$
m\frac{\mathrm{d}v}{\mathrm{d}t}=-e\mathcal{E}-\frac{m}{\tau}v
$$

に従うとする。$\tau>0$ は緩和時間である。電流密度は $j=-nev$ で，電気伝導度 $\sigma$ を定常状態での $j=\sigma\mathcal{E}$ で定義する。以下の問いに答えよ。

(1) 時刻 $t=0$ に電場をかけ始め，$v(0)=0$ とする。$v(t)$ を求め，定常状態での平均速度（ドリフト速度）$v_{\mathrm{d}}$ を求めよ。

(2) $\sigma$ を $n,e,\tau,m$ で表せ。

(3) 定常状態で，摩擦力が電子に対して単位時間・単位体積あたりにする仕事の大きさ $P$ を求め，$P=j\mathcal{E}$ であることを示せ。

(4) 銅の値 $n=8.47\times10^{28}\ \mathrm{m^{-3}}$，室温の抵抗率 $\rho=1.70\times10^{-8}\ \Omega\,\mathrm{m}$ を用いて $\tau$ を求めよ。また，フェルミ速度 $v_{\mathrm{F}}=1.57\times10^6\ \mathrm{m/s}$ を用いた平均自由行程 $\ell=v_{\mathrm{F}}\tau$ と，$j=1.0\times10^6\ \mathrm{A/m^2}$ のときの $|v_{\mathrm{d}}|$ を求めよ。$m=9.109\times10^{-31}\ \mathrm{kg}$，$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

---

## 解答・解説

### (1)
運動方程式は $v$ についての1階の線形微分方程式です。$\mathrm{d}v/\mathrm{d}t=0$ とおくと定常解 $v_{\mathrm{d}}$ が得られ，それからのずれは $e^{-t/\tau}$ で減衰します。

$$
v_{\mathrm{d}}=-\frac{e\tau\mathcal{E}}{m},\qquad v(t)=v_{\mathrm{d}}+Ce^{-t/\tau}
$$

$v(0)=0$ から $C=-v_{\mathrm{d}}$ です。

$$
\finalanswer{v(t)=-\frac{e\tau\mathcal{E}}{m}\left(1-e^{-t/\tau}\right)},\qquad \finalanswer{v_{\mathrm{d}}=-\frac{e\tau\mathcal{E}}{m}}
$$

となります。電子は電場と逆向きに動き，時間 $\tau$ 程度で定常状態に達します。

### (2)
定常状態の電流密度は $j=-nev_{\mathrm{d}}$ で，これに (1) の $v_{\mathrm{d}}$ を代入すると電場に比例します。

$$
j=-ne\left(-\frac{e\tau\mathcal{E}}{m}\right)=\frac{ne^2\tau}{m}\mathcal{E}
$$

比例係数を読み取ると，

$$
\finalanswer{\sigma=\frac{ne^2\tau}{m}}
$$

となります。電荷の符号は2乗で効くので，$\sigma$ はキャリアの符号によりません。

### (3)
電子1個にはたらく摩擦力は $-mv_{\mathrm{d}}/\tau$ で，その仕事率は力と速度の積です。運動を妨げる向きなので仕事は負で，その大きさに電子密度をかけます。

$$
P=n\cdot\frac{m}{\tau}v_{\mathrm{d}}^{\,2}=\frac{nm}{\tau}\left(\frac{e\tau\mathcal{E}}{m}\right)^2=\frac{ne^2\tau}{m}\mathcal{E}^2
$$

(2) の結果から $\dfrac{ne^2\tau}{m}\mathcal{E}^2=\sigma\mathcal{E}^2=j\mathcal{E}$ なので，

$$
\finalanswer{P=\sigma\mathcal{E}^2=j\mathcal{E}}
$$

となります。電場が電子にする仕事は，定常状態ではすべて散乱を通して格子に渡され，ジュール熱になります。

### (4)
(2) を $\tau$ について解くと $\tau=\dfrac{m}{ne^2\rho}$ です。$ne^2=2.174\times10^{-9}\ \mathrm{C^2/m^3}$ で，これに $\rho$ をかけると $3.70\times10^{-17}$ です。

$$
\finalanswer{\tau\approx2.5\times10^{-14}\ \mathrm{s}}
$$

平均自由行程は $\ell=1.57\times10^6\times2.47\times10^{-14}\ \mathrm{m}$，ドリフト速度は $|v_{\mathrm{d}}|=j/ne$ で求めます。

$$
\finalanswer{\ell\approx39\ \mathrm{nm}},\qquad \finalanswer{|v_{\mathrm{d}}|\approx7.4\times10^{-5}\ \mathrm{m/s}}
$$

となります。平均自由行程は原子間隔の100倍以上もあり，電子は格子の原子に毎回ぶつかるのではありません。ドリフト速度はフェルミ速度の $10^{-10}$ 倍ほどの小さな速度です。

===== FILE: 06solid_state/06/06_050.md =====
---
tags:
  - 標準
---

# ホール効果

## 問題
幅 $w$（$y$ 方向），厚さ $d$（$z$ 方向）の長い板状の試料に，$x$ 方向に電流 $I$ を流し，$z$ 方向に一様な磁束密度 $B$ をかける（図）。キャリアは1種類で，電荷 $q$（電子なら $q=-e$，正孔なら $q=+e$，$e>0$），数密度 $n$，質量 $m$，緩和時間 $\tau$ をもつ。キャリアの平均速度 $\boldsymbol{v}$ は

$$
m\frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}=q\left(\boldsymbol{\mathcal{E}}+\boldsymbol{v}\times\boldsymbol{B}\right)-\frac{m}{\tau}\boldsymbol{v}
$$

に従うとする。定常状態で，$y$ 方向には電流が流れず（$j_y=0$），電場の成分 $\mathcal{E}_x,\mathcal{E}_y$ は一様であるとする。電流密度を $j_x=nqv_x$，ホール係数を $R_{\mathrm{H}}=\dfrac{\mathcal{E}_y}{j_xB}$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 直方体の板を斜め上から見た図。長い辺を x 方向（右向き），幅を y 方向（奥向き），厚さを z 方向（上向き）にとり，左下手前に x，y，z 軸の矢印を描く。左端から右端へ電流 I の太い矢印を x 方向に描く。板を上下に貫く磁束密度 B の矢印を z 方向に数本描く。y = 0 の面（手前の側面）と y = w の面（奥の側面）にそれぞれ「y = 0」「y = w」とラベル。幅に寸法線 w，厚さに寸法線 d を付ける。キャリアの軌道や電荷のたまり方は描かない。 -->

(1) $\mathcal{E}_y$ を $j_x,B,n,q$ で表し，$R_{\mathrm{H}}$ を求めよ。

(2) 抵抗率 $\rho_{xx}=\mathcal{E}_x/j_x$ を求めよ。

(3) $d=0.050\ \mathrm{mm}$，$I=2.0\ \mathrm{A}$，$B=1.5\ \mathrm{T}$ で測定したところ，$y=0$ の面に対する $y=w$ の面の電位は $+4.42\ \mu\mathrm{V}$ であった。$R_{\mathrm{H}}$ を求め，キャリアの符号と数密度 $n$ を答えよ。$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

(4) 移動度を $\mu=|q|\tau/m$ で定義する。$\mu$ を $R_{\mathrm{H}}$ と $\rho_{xx}$ で表せ。また，(3) の試料の抵抗率が $\rho_{xx}=1.70\times10^{-8}\ \Omega\,\mathrm{m}$ のときの $\mu$ と，サイクロトロン角振動数 $\omega_{\mathrm{c}}=|q|B/m$ を用いた $\omega_{\mathrm{c}}\tau$ を求めよ。

---

## 解答・解説

### (1)
$\boldsymbol{B}=B\boldsymbol{e}_z$ のとき $\boldsymbol{v}\times\boldsymbol{B}=(v_yB,\,-v_xB,\,0)$ です。定常状態の運動方程式を成分で書きます。

$$
\begin{aligned}
0&=q(\mathcal{E}_x+v_yB)-\frac{m}{\tau}v_x\\
0&=q(\mathcal{E}_y-v_xB)-\frac{m}{\tau}v_y
\end{aligned}
$$

$j_y=0$ より $v_y=0$ なので，2つ目の式から $\mathcal{E}_y=v_xB$ です。$v_x=j_x/nq$ を代入すると，

$$
\finalanswer{\mathcal{E}_y=\frac{j_xB}{nq}},\qquad \finalanswer{R_{\mathrm{H}}=\frac{1}{nq}}
$$

となります。$y$ 方向の電場がローレンツ力を打ち消すので，キャリアはまっすぐ $x$ 方向に進みます。$R_{\mathrm{H}}$ の符号はキャリアの電荷の符号と同じです。

### (2)
$v_y=0$ なので，1つ目の式は磁場を含まず，$v_x=q\tau\mathcal{E}_x/m$ となります。これを $j_x=nqv_x$ に代入すると，

$$
\finalanswer{\rho_{xx}=\frac{m}{nq^2\tau}}
$$

となります。抵抗率は $B$ によらず，1種類のキャリアのドルーデ模型では磁気抵抗が生じません。

### (3)
$\mathcal{E}_y$ が一様なので，$y=0$ の面に対する $y=w$ の面の電位は $V=-\mathcal{E}_yw$ です。$j_x=I/wd$ と (1) を使うと，$w$ が消えます。

$$
V=-R_{\mathrm{H}}\frac{IB}{d}
$$

$R_{\mathrm{H}}$ について解いて数値を代入すると，

$$
R_{\mathrm{H}}=-\frac{Vd}{IB}=-\frac{4.42\times10^{-6}\times5.0\times10^{-5}}{2.0\times1.5}\ \mathrm{m^3/C}
$$

より，

$$
\finalanswer{R_{\mathrm{H}}\approx-7.37\times10^{-11}\ \mathrm{m^3/C}}
$$

となります。$R_{\mathrm{H}}<0$ なので，

$$
\finalanswer{\text{キャリアは負電荷（電子）},\quad n=\frac{1}{e|R_{\mathrm{H}}|}\approx8.47\times10^{28}\ \mathrm{m^{-3}}}
$$

となります。この密度は，銅で原子1個あたり1個の伝導電子があるとした値と一致します。

### (4)
(1) と (2) から $|R_{\mathrm{H}}|=\dfrac{1}{n|q|}$，$\rho_{xx}=\dfrac{m}{nq^2\tau}$ です。比をとると $n$ が消えます。

$$
\finalanswer{\mu=\frac{|R_{\mathrm{H}}|}{\rho_{xx}}}
$$

数値を代入すると $\mu=7.37\times10^{-11}/1.70\times10^{-8}$ です。また，$\omega_{\mathrm{c}}\tau=|q|B\tau/m=\mu B$ です。

$$
\finalanswer{\mu\approx4.3\times10^{-3}\ \mathrm{m^2/(V\,s)}},\qquad \finalanswer{\omega_{\mathrm{c}}\tau\approx6.5\times10^{-3}}
$$

となります。$\omega_{\mathrm{c}}\tau\ll1$ なので，電子はサイクロトロン運動を1周するずっと前に散乱されます。このため室温の金属は弱磁場の領域にあります。

===== FILE: 06solid_state/06/06_060.md =====
---
tags:
  - 標準
---

# 交流伝導度とプラズマ周波数

## 問題
金属の伝導電子を，数密度 $n$，電荷 $-e$（$e>0$），質量 $m$，緩和時間 $\tau$ のドルーデ模型で表す。$x$ 方向の一様な交流電場 $\mathcal{E}(t)=\mathrm{Re}\left[\mathcal{E}_0e^{-i\omega t}\right]$（$\omega>0$）をかけたとき，電子の平均速度 $v$ は $m\dfrac{\mathrm{d}v}{\mathrm{d}t}=-e\mathcal{E}-\dfrac{m}{\tau}v$ に従う。複素数表示で $v,\mathcal{E}\propto e^{-i\omega t}$ とし，電流密度 $j=-nev$ から交流伝導度 $\sigma(\omega)=j/\mathcal{E}$ を定義する。イオン芯の分極は無視する。変位電流と伝導電流の和を $-i\omega\varepsilon_0\varepsilon_{\mathrm{r}}(\omega)\mathcal{E}$ と書いて比誘電関数 $\varepsilon_{\mathrm{r}}(\omega)$ を定義する。金属中の電磁波は $e^{i(K z-\omega t)}$ の形で，$K=N\omega/c$，$N=\sqrt{\varepsilon_{\mathrm{r}}}$（$\mathrm{Im}\,N\ge0$）である。真空から垂直に入射した光の反射率は $R=\left|\dfrac{1-N}{1+N}\right|^2$ である。$\varepsilon_0$ は真空の誘電率，$c$ は光速である。以下の問いに答えよ。

(1) $\sigma(\omega)$ を直流伝導度 $\sigma_0=\dfrac{ne^2\tau}{m}$ と $\omega\tau$ で表せ。

(2) $\varepsilon_{\mathrm{r}}(\omega)$ を求めよ。また，$\omega\tau\gg1$ で $\varepsilon_{\mathrm{r}}\approx1-\dfrac{\omega_{\mathrm{p}}^{\,2}}{\omega^2}$ の形になることを示し，$\omega_{\mathrm{p}}$ を求めよ。

(3) $\omega\tau\gg1$ とする。$\omega<\omega_{\mathrm{p}}$ での反射率 $R$ を求めよ。また，この場合に金属中の電場の振幅が $1/e$ になる深さ $\delta$ を求め，$\omega\ll\omega_{\mathrm{p}}$ での $\delta$ を $c$ と $\omega_{\mathrm{p}}$ で表せ。

(4) ナトリウム（$n=2.65\times10^{28}\ \mathrm{m^{-3}}$）について，$\omega_{\mathrm{p}}$，$\hbar\omega_{\mathrm{p}}$（eV 単位），$\lambda_{\mathrm{p}}=2\pi c/\omega_{\mathrm{p}}$，$\omega\ll\omega_{\mathrm{p}}$ での $\delta$ を求めよ。$e=1.602\times10^{-19}\ \mathrm{C}$，$m=9.109\times10^{-31}\ \mathrm{kg}$，$\varepsilon_0=8.854\times10^{-12}\ \mathrm{F/m}$，$c=2.998\times10^8\ \mathrm{m/s}$，$\hbar=1.055\times10^{-34}\ \mathrm{J\,s}$ とする。

---

## 解答・解説

### (1)
$v\propto e^{-i\omega t}$ なので，時間微分は $-i\omega$ をかけることに置き換わります。運動方程式は代数方程式になります。

$$
-i\omega mv=-e\mathcal{E}-\frac{m}{\tau}v\quad\Longrightarrow\quad v=-\frac{e\tau}{m(1-i\omega\tau)}\mathcal{E}
$$

$j=-nev$ に代入すると，

$$
\finalanswer{\sigma(\omega)=\frac{\sigma_0}{1-i\omega\tau}}
$$

となります。$\omega\to0$ で直流の値に戻り，$\omega\tau\gg1$ では電流が電場より $90^\circ$ 遅れる慣性的な応答になります。

### (2)
変位電流 $-i\omega\varepsilon_0\mathcal{E}$ と伝導電流 $\sigma\mathcal{E}$ の和を $-i\omega\varepsilon_0\varepsilon_{\mathrm{r}}\mathcal{E}$ と比べると，$\varepsilon_{\mathrm{r}}=1+\dfrac{i\sigma}{\varepsilon_0\omega}$ です。(1) を代入すると，

$$
\finalanswer{\varepsilon_{\mathrm{r}}(\omega)=1+\frac{i\sigma_0}{\varepsilon_0\omega(1-i\omega\tau)}}
$$

となります。$\omega\tau\gg1$ では $1-i\omega\tau\approx-i\omega\tau$ と近似でき，第2項は $\dfrac{i\sigma_0}{\varepsilon_0\omega(-i\omega\tau)}=-\dfrac{ne^2}{\varepsilon_0m\omega^2}$ になります。したがって

$$
\finalanswer{\varepsilon_{\mathrm{r}}\approx1-\frac{\omega_{\mathrm{p}}^{\,2}}{\omega^2},\qquad \omega_{\mathrm{p}}=\sqrt{\frac{ne^2}{\varepsilon_0m}}}
$$

となります。$\omega_{\mathrm{p}}$ はプラズマ角振動数とよばれ，緩和時間によりません。

### (3)
$\omega<\omega_{\mathrm{p}}$ では $\varepsilon_{\mathrm{r}}<0$ なので，$N$ は純虚数 $N=i\kappa$ で，$\kappa=\sqrt{\omega_{\mathrm{p}}^{\,2}/\omega^2-1}>0$ です。反射率の分子と分母は互いに複素共役なので絶対値が等しくなります。

$$
\finalanswer{R=\frac{|1-i\kappa|^2}{|1+i\kappa|^2}=1}
$$

となり，光は完全に反射されます。金属中では $e^{iKz}=e^{-\kappa\omega z/c}$ となり，波は進まずに減衰します。

$$
\finalanswer{\delta=\frac{c}{\kappa\omega}=\frac{c}{\sqrt{\omega_{\mathrm{p}}^{\,2}-\omega^2}}},\qquad \finalanswer{\delta\approx\frac{c}{\omega_{\mathrm{p}}}\quad(\omega\ll\omega_{\mathrm{p}})}
$$

となります。反射率の振動数依存性を図に示します。

<!-- FIGURE solution (3): 横軸 ω/ω_p（0〜3），縦軸 反射率 R（0〜1）。0 < ω/ω_p < 1 では R = 1 の水平な実線，ω/ω_p = 1 で急に落ち，ω/ω_p > 1 では R = ((1−N)/(1+N))²，N = √(1−ω_p²/ω²) の曲線が 0 に向かって急速に減衰する。ω/ω_p = 1 に縦の破線を引き「ω_p」とラベル。左側に「反射」，右側に「透過」と注記する。 -->

$\omega>\omega_{\mathrm{p}}$ では $N$ が実数になり，光は金属を透過します。

### (4)
$ne^2=6.801\times10^{-10}$，$\varepsilon_0m=8.065\times10^{-42}$ から $\omega_{\mathrm{p}}^{\,2}=8.433\times10^{31}\ \mathrm{s^{-2}}$ です。

$$
\finalanswer{\omega_{\mathrm{p}}\approx9.18\times10^{15}\ \mathrm{s^{-1}}},\qquad \finalanswer{\hbar\omega_{\mathrm{p}}\approx6.05\ \mathrm{eV}}
$$

波長と侵入長は定義どおりに計算します。

$$
\finalanswer{\lambda_{\mathrm{p}}\approx205\ \mathrm{nm}},\qquad \finalanswer{\delta\approx33\ \mathrm{nm}}
$$

となります。可視光は $\omega<\omega_{\mathrm{p}}$ なので反射され，これが金属光沢の原因です。ナトリウムは実際に波長約 210 nm より短い紫外線を透過します。室温の $\tau\sim3\times10^{-14}\ \mathrm{s}$ では $\omega_{\mathrm{p}}\tau\sim300$ となり，$\omega\tau\gg1$ の近似は可視光の領域で成り立ちます。

===== FILE: 06solid_state/06/06_070.md =====
---
tags:
  - 標準
---

# 金属の比熱：電子とフォノンの分離

## 問題
銅の低温での定圧比熱を測定し，1 mol あたりの値として次の結果を得た。この温度域では定圧比熱と定積比熱の差は無視でき，比熱を $C$ と書く。

| $T\ (\mathrm{K})$ | 1.00 | 2.00 | 3.00 | 4.00 |
|---|---|---|---|---|
| $C\ (\mathrm{mJ/(mol\,K)})$ | 0.743 | 1.776 | 3.386 | 5.865 |

比熱は伝導電子の寄与 $\gamma T$ と格子振動の寄与 $\beta T^3$ の和で表されるとする。格子比熱はデバイ模型の低温の式 $\dfrac{12\pi^4}{5}R\left(\dfrac{T}{\Theta_{\mathrm{D}}}\right)^3$ に従うとし，気体定数を $R=8.314\ \mathrm{J/(mol\,K)}$ とする。以下の問いに答えよ。

(1) $C/T$ を $T^2$ の関数として表し，$C/T$ を縦軸，$T^2$ を横軸にとったグラフの切片と傾きがそれぞれ何を表すかを答えよ。

(2) $T=1.00\ \mathrm{K}$ と $4.00\ \mathrm{K}$ のデータを用いて $\gamma$ と $\beta$ を求めよ。また，$T=2.00\ \mathrm{K}$ と $3.00\ \mathrm{K}$ のデータがこの直線に乗ることを確かめよ。

(3) デバイ温度 $\Theta_{\mathrm{D}}$ を求めよ。

(4) 電子比熱と格子比熱が等しくなる温度 $T^*$ を求めよ。また，1価の3次元自由電子模型の電子比熱 $\dfrac{\pi^2}{2}R\dfrac{T}{T_{\mathrm{F}}}$ において，銅のフェルミエネルギーを $E_{\mathrm{F}}=7.00\ \mathrm{eV}$ として $\gamma$ の値 $\gamma_{\mathrm{free}}$ を求め，比 $\gamma/\gamma_{\mathrm{free}}$ を求めよ。$T_{\mathrm{F}}=E_{\mathrm{F}}/k_{\mathrm{B}}$，$k_{\mathrm{B}}=1.381\times10^{-23}\ \mathrm{J/K}$，$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

---

## 解答・解説

### (1)
$C=\gamma T+\beta T^3$ の両辺を $T$ で割ると，

$$
\finalanswer{\frac{C}{T}=\gamma+\beta T^2}
$$

となります。$C/T$ は $T^2$ の1次関数なので，グラフは直線になります。

$$
\finalanswer{\text{切片}=\gamma\ \text{（電子比熱の係数）},\qquad \text{傾き}=\beta\ \text{（格子比熱の係数）}}
$$

となります。このプロットを使うと，大きさの違う2つの寄与をきれいに分けられます。

### (2)
各温度で $C/T$ を計算します。

$$
\begin{aligned}
T=1.00\ \mathrm{K}&:\ C/T=0.743\\
T=2.00\ \mathrm{K}&:\ C/T=0.888\\
T=3.00\ \mathrm{K}&:\ C/T=1.1287\\
T=4.00\ \mathrm{K}&:\ C/T=1.4663
\end{aligned}
$$

単位は $\mathrm{mJ/(mol\,K^2)}$ です。1.00 K と 4.00 K の2点を通る直線の傾きは $\dfrac{1.4663-0.743}{16-1}$ で，切片は $0.743$ から傾き1つ分を引いたものです。

$$
\finalanswer{\gamma\approx0.695\ \mathrm{mJ/(mol\,K^2)}},\qquad \finalanswer{\beta\approx0.0482\ \mathrm{mJ/(mol\,K^4)}}
$$

となります。この直線から，$T=2.00\ \mathrm{K}$ では $0.695+0.0482\times4=0.888$，$T=3.00\ \mathrm{K}$ では $0.695+0.0482\times9=1.129$ となり，測定値と一致します。データを図に示します。

<!-- FIGURE solution (2): 横軸 T²（K²，0〜17），縦軸 C/T（mJ/(mol K²)，0〜1.6）。4つの測定点 (1, 0.743)，(4, 0.888)，(9, 1.129)，(16, 1.466) を黒丸で描き，直線 C/T = 0.695 + 0.0482 T² を実線で T² = 0 まで延長する。切片 0.695 に矢印を付けて「γ」と注記し，直線の途中に三角形を描いて傾きを「β」と注記する。 -->

### (3)
格子比熱の係数は $\beta=\dfrac{12\pi^4R}{5\Theta_{\mathrm{D}}^{\,3}}$ なので，これを $\Theta_{\mathrm{D}}$ について解きます。$\dfrac{12\pi^4}{5}R=1944\ \mathrm{J/(mol\,K)}$，$\beta=4.82\times10^{-5}\ \mathrm{J/(mol\,K^4)}$ です。

$$
\Theta_{\mathrm{D}}=\left(\frac{1944}{4.82\times10^{-5}}\right)^{1/3}\ \mathrm{K}=\left(4.03\times10^7\right)^{1/3}\ \mathrm{K}
$$

より，

$$
\finalanswer{\Theta_{\mathrm{D}}\approx343\ \mathrm{K}}
$$

となります。

### (4)
$\gamma T^*=\beta T^{*3}$ とおくと $T^*=\sqrt{\gamma/\beta}=\sqrt{0.695/0.0482}\ \mathrm{K}$ です。

$$
\finalanswer{T^*\approx3.8\ \mathrm{K}}
$$

これより低温では電子比熱が支配的になります。次に $T_{\mathrm{F}}=\dfrac{7.00\times1.602\times10^{-19}}{1.381\times10^{-23}}\ \mathrm{K}=8.12\times10^4\ \mathrm{K}$ を使うと，$\gamma_{\mathrm{free}}=\dfrac{\pi^2R}{2T_{\mathrm{F}}}$ です。

$$
\finalanswer{\gamma_{\mathrm{free}}\approx0.505\ \mathrm{mJ/(mol\,K^2)}},\qquad \finalanswer{\frac{\gamma}{\gamma_{\mathrm{free}}}\approx1.38}
$$

となります。$\gamma$ はフェルミ準位の状態密度に比例するので，この比は実際の状態密度が自由電子の値より約4割大きいことを示します。その原因には，バンド構造の効果や，電子とフォノンの相互作用があります。

===== FILE: 06solid_state/07/07_010.md =====
---
tags:
  - 標準
---

# ブロッホの定理

## 問題
一次元の結晶中の質量 $m$ の電子を考える。ポテンシャル $V(x)$ は実数で，周期 $a$ をもつ（$V(x+a)=V(x)$）。ハミルトニアンは $\hat{H}=-\dfrac{\hbar^2}{2m}\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}+V(x)$ である。結晶は $N$ 個の単位胞からなり，長さを $L=Na$ として，波動関数に周期境界条件 $\psi(x+L)=\psi(x)$ を課す。関数を $a$ だけずらす並進演算子 $\hat{T}_a$ を $\hat{T}_af(x)=f(x+a)$ で定義する。以下の問いに答えよ。

(1) $\hat{H}$ と $\hat{T}_a$ が交換すること，すなわち任意の関数 $f$ に対して $\hat{T}_a\hat{H}f=\hat{H}\hat{T}_af$ となることを示せ。

(2) $\psi$ を $\hat{H}$ と $\hat{T}_a$ の同時固有関数とし，$\hat{T}_a\psi=\lambda\psi$ とする。周期境界条件から $\lambda$ のとりうる値を求め，$\lambda=e^{ika}$ と書いたときの $k$ の値を求めよ。また，異なる $\lambda$ の数を求めよ。

(3) (2) の $\psi$ が，周期 $a$ の関数 $u_k(x)$ を用いて $\psi(x)=e^{ikx}u_k(x)$ と書けることを示せ。

(4) $u_k$ が満たす微分方程式を求めよ。また，その方程式がエネルギー $E$ の解 $u_k$ をもつとき，$k$ を $k+G$（$G=2\pi/a$）に置き換えた方程式は，同じエネルギー $E$ の解 $e^{-iGx}u_k(x)$ をもつことを示せ。

---

## 解答・解説

### (1)
$\hat{T}_a\hat{H}f$ は，$\hat{H}f$ の変数 $x$ を $x+a$ に置き換えたものです。2階微分は変数をずらしても形が変わらず，ポテンシャルは周期性から $V(x+a)=V(x)$ です。

$$
\hat{T}_a\hat{H}f(x)=-\frac{\hbar^2}{2m}f''(x+a)+V(x+a)f(x+a)=\left[-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d}x^2}+V(x)\right]f(x+a)
$$

右辺は $\hat{H}$ を $\hat{T}_af$ に作用させたものなので，

$$
\finalanswer{\hat{T}_a\hat{H}f=\hat{H}\hat{T}_af}
$$

となります。交換する演算子には同時固有関数をとれます。エネルギーが縮退している場合でも，その固有空間の中で $\hat{T}_a$ の固有関数を選べます。

### (2)
$\hat{T}_a$ を $N$ 回作用させると，$x$ を $Na=L$ だけずらすことになり，周期境界条件からもとの関数に戻ります。

$$
\hat{T}_a^{\,N}\psi=\lambda^N\psi=\psi(x+L)=\psi(x)
$$

したがって $\lambda^N=1$ で，$\lambda$ は1の $N$ 乗根です。

$$
\finalanswer{\lambda=e^{2\pi i\ell/N},\qquad k=\frac{2\pi\ell}{Na}\quad(\ell\ \text{は整数})}
$$

$\ell$ を $N$ だけ変えても $\lambda$ は変わらないので，異なる $\lambda$ は $\ell=0,1,\ldots,N-1$ に対応する

$$
\finalanswer{N\ \text{個}}
$$

です。$k$ を $-\pi/a<k\le\pi/a$ にとれば，第1ブリルアンゾーンの中の $N$ 個の波数に1対1に対応します。

### (3)
$u_k(x)=e^{-ikx}\psi(x)$ と定義し，これが周期 $a$ をもつことを確かめます。$\psi(x+a)=e^{ika}\psi(x)$ を使うと，

$$
u_k(x+a)=e^{-ik(x+a)}\psi(x+a)=e^{-ik(x+a)}e^{ika}\psi(x)=e^{-ikx}\psi(x)=u_k(x)
$$

となります。したがって

$$
\finalanswer{\psi(x)=e^{ikx}u_k(x),\qquad u_k(x+a)=u_k(x)}
$$

と書けます。これがブロッホの定理で，結晶中の電子の波動関数は，平面波に格子の周期をもつ関数をかけた形をしています。

### (4)
$\psi=e^{ikx}u_k$ を微分すると，$\dfrac{\mathrm{d}}{\mathrm{d}x}\left(e^{ikx}u\right)=e^{ikx}\left(\dfrac{\mathrm{d}}{\mathrm{d}x}+ik\right)u$ です。これを2回使ってシュレーディンガー方程式に代入し，$e^{ikx}$ で割ると，

$$
\finalanswer{\left[-\frac{\hbar^2}{2m}\left(\frac{\mathrm{d}}{\mathrm{d}x}+ik\right)^2+V(x)\right]u_k=Eu_k}
$$

となります。次に $w(x)=e^{-iGx}u_k(x)$ とおくと，$Ga=2\pi$ なので $w$ も周期 $a$ をもちます。微分の規則から

$$
\left(\frac{\mathrm{d}}{\mathrm{d}x}+ik+iG\right)\left(e^{-iGx}u_k\right)=e^{-iGx}\left(\frac{\mathrm{d}}{\mathrm{d}x}+ik\right)u_k
$$

が成り立ち，これを2回使うと，

$$
\finalanswer{\left[-\frac{\hbar^2}{2m}\left(\frac{\mathrm{d}}{\mathrm{d}x}+i(k+G)\right)^2+V\right]w=e^{-iGx}\,Eu_k=Ew}
$$

となります。$k$ と $k+G$ で同じエネルギー固有値の組が現れるので，バンド $E_n(k)$ は逆格子ベクトルの周期をもつ関数です。

===== FILE: 06solid_state/07/07_020.md =====
---
tags:
  - 標準
---

# ほとんど自由な電子とバンドギャップ

## 問題
長さ $L=Na$ の一次元の結晶中の質量 $m$ の電子を考え，周期境界条件を課す。周期 $a$ のポテンシャルを $V(x)=\sum_GV_Ge^{iGx}$ とフーリエ展開する。和は $G=2\pi\ell/a$（$\ell$ は整数）にわたり，$V_0=0$ とする。$V(x)$ は実数なので $V_{-G}=V_G^{\,*}$ である。波動関数を $\psi(x)=\dfrac{1}{\sqrt{L}}\sum_qC_qe^{iqx}$ と展開する。和は周期境界条件で許される $q=2\pi j/L$（$j$ は整数）にわたる。$\lambda_q=\dfrac{\hbar^2q^2}{2m}$ とおく。ポテンシャルは弱いとする。以下の問いに答えよ。

(1) シュレーディンガー方程式から係数 $C_q$ が満たす式を導け。

(2) $G_1=2\pi/a$ とし，$k$ が $\pi/a$ に近いとき，$C_k$ と $C_{k-G_1}$ だけを残す近似でエネルギー $E_\pm(k)$ を求めよ。また，$k=\pi/a$ でのエネルギーギャップ $E_{\mathrm{g}}$ を求めよ。

(3) $V(x)=2V_1\cos\dfrac{2\pi x}{a}$（$V_1>0$）とする。$k=\pi/a$ での2つの状態の規格化された波動関数を，(2) の近似で求めよ。また，それぞれの状態でのポテンシャルの期待値 $\langle V\rangle$ を求めよ。

(4) $k=\pi/a+\kappa$ で $|\kappa|$ が十分小さいとき，$E_\pm$ を $\kappa^2$ の項まで求めよ。$\varepsilon=\lambda_{\pi/a}$ とし，$|V_{G_1}|<2\varepsilon$ とする。さらに，下のバンドを $E_-\approx E_-(\pi/a)+\dfrac{\hbar^2\kappa^2}{2m^*}$ と書いたときの $m^*$ を求めよ。

---

## 解答・解説

### (1)
展開をシュレーディンガー方程式 $\left(-\dfrac{\hbar^2}{2m}\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}+V\right)\psi=E\psi$ に代入します。ポテンシャルの項は $V_GC_qe^{i(q+G)x}$ の和になるので，$q+G$ を $q$ と付け替えて $e^{iqx}$ の係数をそろえます。

$$
\sum_q\left[(\lambda_q-E)C_q+\sum_GV_GC_{q-G}\right]e^{iqx}=0
$$

平面波は1次独立なので，各係数が0になります。

$$
\finalanswer{(\lambda_q-E)C_q+\sum_GV_GC_{q-G}=0}
$$

となります。$C_q$ は逆格子ベクトルだけ離れた $C_{q-G}$ とだけ結びつくので，1つの固有状態は $q=k-G$ の形の平面波だけを含みます。これはブロッホの定理と同じ内容です。

### (2)
$q=k$ と $q=k-G_1$ の式で，$C_k$ と $C_{k-G_1}$ 以外を無視します。2つ目の式では $G=-G_1$ の項が $C_k$ を与えます。

$$
\begin{aligned}
(\lambda_k-E)C_k+V_{G_1}C_{k-G_1}&=0\\
V_{-G_1}C_k+(\lambda_{k-G_1}-E)C_{k-G_1}&=0
\end{aligned}
$$

係数の行列式を0とおくと $(\lambda_k-E)(\lambda_{k-G_1}-E)=|V_{G_1}|^2$ となり，これを解くと，

$$
\finalanswer{E_\pm(k)=\frac{\lambda_k+\lambda_{k-G_1}}{2}\pm\sqrt{\left(\frac{\lambda_k-\lambda_{k-G_1}}{2}\right)^2+|V_{G_1}|^2}}
$$

となります。$k=\pi/a$ では $\lambda_k=\lambda_{k-G_1}$ なので，2つのエネルギーの差は

$$
\finalanswer{E_{\mathrm{g}}=2|V_{G_1}|}
$$

となります。分散関係を図に示します。

<!-- FIGURE solution (2): 横軸 k（−2π/a から 2π/a），縦軸 E。自由電子の放物線 ħ²k²/2m を細い破線で描く。その上に，ほとんど自由な電子のバンドを実線で描く：放物線に沿うが，k = ±π/a で上下に分かれ，下の曲線は水平な接線で終わり，上の曲線は水平な接線で始まる。k = ±π/a に縦の点線を引き，k = π/a での上下のすき間を矢印で示して「E_g = 2|V_G|」と注記する。 -->

### (3)
$2V_1\cos(2\pi x/a)=V_1e^{iG_1x}+V_1e^{-iG_1x}$ なので，$V_{G_1}=V_{-G_1}=V_1$ です。$k=\pi/a$ では $k-G_1=-\pi/a$ です。(2) の1つ目の式で $E=\varepsilon\pm V_1$ とおくと，$C_{-\pi/a}=\pm C_{\pi/a}$ となります。

$$
\finalanswer{E_+=\varepsilon+V_1:\ \psi_+=\sqrt{\frac{2}{L}}\cos\frac{\pi x}{a}},\qquad \finalanswer{E_-=\varepsilon-V_1:\ \psi_-=\sqrt{\frac{2}{L}}\sin\frac{\pi x}{a}}
$$

となります。$\psi_-$ の全体の位相因子 $i$ は省きました。期待値は，$\cos^2(\pi x/a)=\dfrac{1}{2}\left(1+\cos\dfrac{2\pi x}{a}\right)$ を使い，$\cos^2(2\pi x/a)$ の平均が $\dfrac{1}{2}$ であることから求まります。

$$
\langle V\rangle_+=\frac{2}{L}\int_0^L\frac{1}{2}\left(1+\cos\frac{2\pi x}{a}\right)2V_1\cos\frac{2\pi x}{a}\,\mathrm{d}x
$$

$\langle V\rangle_-$ も同様に計算すると，

$$
\finalanswer{\langle V\rangle_+=V_1},\qquad \finalanswer{\langle V\rangle_-=-V_1}
$$

となります。どちらの状態も運動エネルギーは $\varepsilon$ なので，エネルギーの違いはポテンシャルだけから生じます。上の状態ではポテンシャルの山 $x=0,a$ に電子が集まり，下の状態では谷 $x=a/2$ に集まります。

### (4)
$\lambda_{\pi/a+\kappa}$ と $\lambda_{\kappa-\pi/a}$ の平均は $\varepsilon+\dfrac{\hbar^2\kappa^2}{2m}$，差の半分は $\dfrac{\hbar^2\pi\kappa}{ma}$ です。$\left(\dfrac{\hbar^2\pi\kappa}{ma}\right)^2=4\varepsilon\cdot\dfrac{\hbar^2\kappa^2}{2m}$ と書けるので，平方根を $\sqrt{|V|^2+X}\approx|V|+\dfrac{X}{2|V|}$ と展開します。

$$
\finalanswer{E_\pm\approx\varepsilon\pm|V_{G_1}|+\frac{\hbar^2\kappa^2}{2m}\left(1\pm\frac{2\varepsilon}{|V_{G_1}|}\right)}
$$

となります。展開が使えるのは $\dfrac{\hbar^2\pi|\kappa|}{ma}\ll|V_{G_1}|$ の範囲です。下のバンドの係数を $\dfrac{\hbar^2}{2m^*}$ と比べると，

$$
\finalanswer{m^*=\frac{m}{1-2\varepsilon/|V_{G_1}|}=-\frac{m|V_{G_1}|}{2\varepsilon-|V_{G_1}|}}
$$

となります。ポテンシャルが弱いほど $|m^*|$ は小さく，下のバンドの上端では有効質量が負になります。

===== FILE: 06solid_state/07/07_030.md =====
---
tags:
  - 発展
---

# クローニッヒ・ペニー模型

## 問題
一次元の結晶中の質量 $m$ の電子を考える。周期 $a=w+b$ のポテンシャルは，$0<x<w$ で $V=0$，$w<x<a$ で $V=V_0>0$ であり，これが周期 $a$ で繰り返される（図）。エネルギー $E$ が $0<E<V_0$ の範囲にあるとし，$\alpha=\dfrac{\sqrt{2mE}}{\hbar}$，$\beta=\dfrac{\sqrt{2m(V_0-E)}}{\hbar}$ とおく。波動関数 $\psi$ とその導関数 $\psi'$ は至るところで連続である。$\psi$ と $\psi'$ を並べた列ベクトルを $\Psi(x)=\begin{pmatrix}\psi(x)\\ \psi'(x)\end{pmatrix}$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 横軸 x，縦軸 V(x) のグラフ。高さ V0 の長方形の障壁が周期的に3〜4個並んだ形を太線で描く。障壁と障壁の間（V = 0）の幅を w，障壁の幅を b とし，それぞれに寸法線を付ける。1周期分（井戸1つと障壁1つ）にまたがる寸法線を引いて a = w + b とラベル。x = 0 を1つの井戸の左端にとって目盛りを付け，x = w，x = a にも目盛りを付ける。0 と V0 の間の高さに水平な破線を引いて E とラベルする。 -->

(1) $0\le x\le w$ で $\Psi(w)=M_w\Psi(0)$，$w\le x\le a$ で $\Psi(a)=M_b\Psi(w)$ となる $2\times2$ 行列 $M_w$，$M_b$ を求め，それぞれの行列式を求めよ。

(2) ブロッホの定理 $\psi(x+a)=e^{ika}\psi(x)$（$k$ は実数）を用いて，$k$ と $E$ の関係式を $\alpha,\beta,w,b$ で表せ。

(3) $b\to0$，$V_0\to\infty$ の極限を，$V_0b$ を一定に保ってとる。$P=\dfrac{mV_0ba}{\hbar^2}$ とおき，(2) の関係式がどうなるかを求めよ。

(4) (3) の模型で $0<P\ll1$ とする。$P$ の1次の近似で，最も低いバンドの底のエネルギー $E_1$ と，1番目と2番目のバンドの間のギャップ $\Delta E$ を，$V_0,b,a$ で表せ。

---

## 解答・解説

### (1)
$0<x<w$ ではシュレーディンガー方程式は $\psi''=-\alpha^2\psi$ で，初期値 $\psi(0),\psi'(0)$ を満たす解は次のとおりです。

$$
\psi(x)=\psi(0)\cos\alpha x+\frac{\psi'(0)}{\alpha}\sin\alpha x
$$

障壁の中では $\psi''=\beta^2\psi$ なので，三角関数が双曲線関数に置き換わります。$\psi$ と $\psi'$ を $x=w$，$x=a$ で並べると，

$$
\finalanswer{M_w=\begin{pmatrix}\cos\alpha w & \dfrac{\sin\alpha w}{\alpha}\\ -\alpha\sin\alpha w & \cos\alpha w\end{pmatrix}},\qquad
\finalanswer{M_b=\begin{pmatrix}\cosh\beta b & \dfrac{\sinh\beta b}{\beta}\\ \beta\sinh\beta b & \cosh\beta b\end{pmatrix}}
$$

となります。$\cos^2+\sin^2=1$，$\cosh^2-\sinh^2=1$ から，

$$
\finalanswer{\det M_w=\det M_b=1}
$$

となります。

### (2)
1周期の転送行列を $M=M_bM_w$ とすると $\Psi(a)=M\Psi(0)$ です。一方，ブロッホの定理から $\Psi(a)=e^{ika}\Psi(0)$ なので，$e^{ika}$ は $M$ の固有値です。固有方程式は $\lambda^2-(\operatorname{tr}M)\lambda+\det M=0$ で，$\det M=1$ なので $\lambda+\lambda^{-1}=\operatorname{tr}M$ です。$\lambda=e^{ika}$ を代入すると $2\cos ka=\operatorname{tr}M$ になります。行列の積の対角成分を足すと，

$$
\operatorname{tr}(M_bM_w)=2\cos\alpha w\cosh\beta b+\left(\frac{\beta}{\alpha}-\frac{\alpha}{\beta}\right)\sin\alpha w\sinh\beta b
$$

となるので，

$$
\finalanswer{\cos ka=\cos\alpha w\cosh\beta b+\frac{\beta^2-\alpha^2}{2\alpha\beta}\sin\alpha w\sinh\beta b}
$$

となります。右辺の絶対値が1以下になるエネルギーだけで実数の $k$ が存在し，そこが許容バンドです。

### (3)
$\beta^2b\approx2mV_0b/\hbar^2$ は一定ですが，$\beta b=\sqrt{\beta^2b}\sqrt{b}\to0$ です。したがって $\cosh\beta b\to1$，$\sinh\beta b\approx\beta b$ と近似でき，$w\to a$ となります。第2項の係数は，$\alpha^2$ が $\beta^2$ に比べて無視できるので次のようになります。

$$
\frac{\beta^2-\alpha^2}{2\alpha\beta}\cdot\beta b\to\frac{\beta^2b}{2\alpha}=\frac{mV_0b}{\hbar^2\alpha}=\frac{P}{\alpha a}
$$

よって

$$
\finalanswer{\cos ka=\cos\alpha a+P\,\frac{\sin\alpha a}{\alpha a}}
$$

となります。右辺を $\alpha a$ の関数として図に示します。

<!-- FIGURE solution (3): 横軸 αa（0〜3π），縦軸 f(αa) = cos αa + P sin(αa)/(αa) で P = 3π/2 の場合を実線で描く。αa = 0 で f = 1 + P（約 5.7）から始まり，振動しながら振幅が減る。縦軸 +1 と −1 に水平な破線を引く。曲線が −1 ≤ f ≤ 1 にある αa の区間を横軸上に太線で示して「許容バンド」と注記し，その間の区間を「ギャップ」と注記する。αa = π，2π，3π に目盛りを付ける。 -->

### (4)
バンドの底は $k=0$，すなわち右辺が1になるところです。$\alpha a\ll1$ として $\cos\alpha a\approx1-\dfrac{(\alpha a)^2}{2}$，$\dfrac{\sin\alpha a}{\alpha a}\approx1$ と近似すると，$(\alpha a)^2=2P$ です。$E_1=\dfrac{\hbar^2\alpha^2}{2m}$ に代入すると，

$$
\finalanswer{E_1=\frac{\hbar^2P}{ma^2}=\frac{V_0b}{a}}
$$

となります。これはポテンシャルの空間平均に等しい値です。

ギャップは $k=\pi/a$ の右辺 $=-1$ のところに開きます。$\alpha a=\pi$ では $\sin\alpha a=0$ なので，1番目のバンドの上端は $\alpha a=\pi$ です。$\alpha a=\pi+\eta$ とおくと右辺は $-1+\dfrac{\eta^2}{2}-\dfrac{P\eta}{\pi}$ となり，これが再び $-1$ になる $\eta=2P/\pi$ が2番目のバンドの底です。エネルギーの差は $\dfrac{\hbar^2}{2ma^2}\left[(\pi+\eta)^2-\pi^2\right]\approx\dfrac{\hbar^2}{2ma^2}\cdot4P$ なので，

$$
\finalanswer{\Delta E=\frac{2\hbar^2P}{ma^2}=\frac{2V_0b}{a}}
$$

となります。デルタ関数列のフーリエ係数は $V_G=V_0b/a$ なので，この結果はほとんど自由な電子の近似のギャップ $2|V_G|$ と一致します。

===== FILE: 06solid_state/07/07_040.md =====
---
tags:
  - 標準
---

# 強束縛近似

## 問題
各格子点 $\boldsymbol{R}_n$ に1つずつ原子軌道 $\phi_n$ がある結晶を考える。原子軌道どうしの重なりは無視し，$\langle\phi_m|\phi_n\rangle=\delta_{mn}$ とする。ハミルトニアン $\hat{H}$ の行列要素は，$\langle\phi_n|\hat{H}|\phi_n\rangle=\varepsilon_0$，最近接の格子点の組について $\langle\phi_m|\hat{H}|\phi_n\rangle=-t$（$t>0$），それ以外は0とする。格子点の数を $N$ とし，ブロッホ和 $\psi_{\boldsymbol{k}}=\dfrac{1}{\sqrt{N}}\sum_ne^{i\boldsymbol{k}\cdot\boldsymbol{R}_n}\phi_n$ に対してエネルギーを $E(\boldsymbol{k})=\langle\psi_{\boldsymbol{k}}|\hat{H}|\psi_{\boldsymbol{k}}\rangle$ で求める。周期境界条件を課し，群速度を $\boldsymbol{v}=\dfrac{1}{\hbar}\nabla_{\boldsymbol{k}}E$ とする。以下の問いに答えよ。

(1) 格子定数 $a$ の一次元の鎖について $E(k)$ を求め，バンド幅 $W_1$ を求めよ。

(2) 格子定数 $a$ の2次元の正方格子について $E(k_x,k_y)$ を求めよ。また，ブリルアンゾーンの点 $\Gamma\,(0,0)$，$\mathrm{X}\,(\pi/a,0)$，$\mathrm{M}\,(\pi/a,\pi/a)$ でのエネルギーと，バンド幅 $W_2$ を求めよ。

(3) (2) の正方格子で，電子が格子点あたり1個ある（スピンの自由度は2）とする。絶対零度でのフェルミエネルギー $E_{\mathrm{F}}$ を求め，第1ブリルアンゾーン内のフェルミ面を表す式を求めよ。また，フェルミ面が囲む面積がブリルアンゾーンの面積の何倍かを求めよ。

(4) (3) のフェルミ面上の点 $\mathrm{P}\,(\pi/2a,\pi/2a)$ と点 $\mathrm{X}$ での群速度 $\boldsymbol{v}$ を求めよ。

---

## 解答・解説

### (1)
ブロッホ和を代入すると，$E(k)=\dfrac{1}{N}\sum_{m,n}e^{ik(n-m)a}\langle\phi_m|\hat{H}|\phi_n\rangle$ です。値をもつのは $m=n$ と $m=n\pm1$ の項だけで，$n$ についての和は $N$ 個の同じ項になります。

$$
E(k)=\varepsilon_0-t\left(e^{ika}+e^{-ika}\right)
$$

より，

$$
\finalanswer{E(k)=\varepsilon_0-2t\cos ka},\qquad \finalanswer{W_1=4t}
$$

となります。ハミルトニアンは異なる $k$ のブロッホ和を混ぜないので，この期待値はこの模型での厳密な固有値です。

### (2)
最近接は $\pm a\boldsymbol{e}_x$，$\pm a\boldsymbol{e}_y$ の4つなので，(1) と同じ計算で $x$ 方向と $y$ 方向の寄与が加わります。

$$
\finalanswer{E(k_x,k_y)=\varepsilon_0-2t\left(\cos k_xa+\cos k_ya\right)}
$$

3つの点で余弦の値を代入すると，

$$
\finalanswer{E(\Gamma)=\varepsilon_0-4t},\qquad \finalanswer{E(\mathrm{X})=\varepsilon_0},\qquad \finalanswer{E(\mathrm{M})=\varepsilon_0+4t},\qquad \finalanswer{W_2=8t}
$$

となります。バンドの底は $\Gamma$，上端は $\mathrm{M}$ です。最近接の数を $z$ とすると，バンド幅は $2zt$ になります。

### (3)
$\boldsymbol{k}$ を $(\pi/a,\pi/a)$ だけずらすと，余弦の符号が両方とも反転し，$E$ は $2\varepsilon_0-E$ に移ります。したがって $\varepsilon_0$ より下の状態と上の状態は同じ数あります。バンドの状態数はスピンを含めて $2N$ で，電子は $N$ 個なのでちょうど半分が埋まります。

$$
\finalanswer{E_{\mathrm{F}}=\varepsilon_0}
$$

フェルミ面は $\cos k_xa+\cos k_ya=0$ です。$\cos k_xa=\cos(\pi-|k_y|a)$ と書き直すと，ゾーン内では次のようになります。

$$
\finalanswer{|k_x|+|k_y|=\frac{\pi}{a}}
$$

これは $(\pm\pi/a,0)$ と $(0,\pm\pi/a)$ を頂点とする正方形です。フェルミ面を図に示します。

<!-- FIGURE solution (3): k_x，k_y 軸を引き，第1ブリルアンゾーン（一辺 2π/a の正方形，頂点 (±π/a, ±π/a)）を細い実線で描く。その内側に，頂点 (±π/a, 0)，(0, ±π/a) をもつ45°回転した正方形を太線で描いてフェルミ面とし，内側を薄く塗る。原点に Γ，(π/a, 0) に X，(π/a, π/a) に M，フェルミ面の辺上の (π/2a, π/2a) に P のラベルを付ける。 -->

正方形の面積は対角線の長さ $2\pi/a$ から $\dfrac{1}{2}\left(\dfrac{2\pi}{a}\right)^2$ で，ゾーンの面積 $\left(\dfrac{2\pi}{a}\right)^2$ と比べて

$$
\finalanswer{\frac{1}{2}\ \text{倍}}
$$

となります。半分が埋まることと合っています。

### (4)
(2) の $E$ を微分すると，$\nabla_{\boldsymbol{k}}E=2ta\left(\sin k_xa,\ \sin k_ya\right)$ です。点 $\mathrm{P}$ では2つの正弦がどちらも1になります。

$$
\finalanswer{\boldsymbol{v}(\mathrm{P})=\frac{2ta}{\hbar}\left(\boldsymbol{e}_x+\boldsymbol{e}_y\right),\quad |\boldsymbol{v}|=\frac{2\sqrt{2}\,ta}{\hbar}}
$$

となります。この向きは，フェルミ面の辺 $k_x+k_y=\pi/a$ に垂直です。点 $\mathrm{X}$ では $\sin\pi=\sin0=0$ なので，

$$
\finalanswer{\boldsymbol{v}(\mathrm{X})=\boldsymbol{0}}
$$

となります。$\mathrm{X}$ は $E$ の鞍点で，状態密度はこのエネルギーで対数的に発散します。

===== FILE: 06solid_state/07/07_050.md =====
---
tags:
  - 標準
---

# 有効質量

## 問題
一次元の結晶中の電子のバンドを $E(k)$ とする。波数 $k$ のまわりに局在した波束は群速度 $v=\dfrac{1}{\hbar}\dfrac{\mathrm{d}E}{\mathrm{d}k}$ で動き，外力 $F$ のもとで波数は $\hbar\dfrac{\mathrm{d}k}{\mathrm{d}t}=F$ に従うとする。電子の電荷を $-e$（$e>0$），真空中の電子の質量を $m$ とする。以下の問いに答えよ。

(1) $\dfrac{\mathrm{d}v}{\mathrm{d}t}=\dfrac{F}{m^*}$ と書いたときの有効質量 $m^*$ を $E(k)$ で表せ。

(2) 強束縛近似のバンド $E(k)=\varepsilon_0-2t\cos ka$（$t>0$，$a$ は格子定数）について，$m^*(k)$ を求めよ。また，$k=0$ と $k=\pi/a$ での $m^*$ と，$m^*$ が発散する $k$ を求めよ。

(3) $t=1.0\ \mathrm{eV}$，$a=0.30\ \mathrm{nm}$ のとき，バンドの底での $m^*/m$ を求めよ。$\hbar=1.055\times10^{-34}\ \mathrm{J\,s}$，$m=9.109\times10^{-31}\ \mathrm{kg}$，$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

(4) (2) のバンドで，上端 $k=\pi/a$ の近くの1つの状態 $k_{\mathrm{e}}$ だけが空いており，他の状態はすべて電子で占められている。鎖の長さを $L$ とし，電流を $I=-\dfrac{e}{L}\sum v(k)$（和は占有された状態にわたる）とする。$I$ を $v(k_{\mathrm{e}})$ で表せ。また，一様な電場 $\mathcal{E}$ のもとで空いた状態の波数も $\hbar\dfrac{\mathrm{d}k_{\mathrm{e}}}{\mathrm{d}t}=-e\mathcal{E}$ に従う。この空いた状態の運動を，電荷 $+e$，正の質量 $m_{\mathrm{h}}$ の粒子の運動方程式 $m_{\mathrm{h}}\dfrac{\mathrm{d}v}{\mathrm{d}t}=e\mathcal{E}$ とみなすときの $m_{\mathrm{h}}$ を求めよ。

---

## 解答・解説

### (1)
$v$ は $k$ を通して時間に依存するので，合成関数の微分をとり，$\dfrac{\mathrm{d}k}{\mathrm{d}t}=\dfrac{F}{\hbar}$ を代入します。

$$
\frac{\mathrm{d}v}{\mathrm{d}t}=\frac{1}{\hbar}\frac{\mathrm{d}^2E}{\mathrm{d}k^2}\frac{\mathrm{d}k}{\mathrm{d}t}=\frac{1}{\hbar^2}\frac{\mathrm{d}^2E}{\mathrm{d}k^2}F
$$

これを $F/m^*$ と比べると，

$$
\finalanswer{m^*=\hbar^2\left(\frac{\mathrm{d}^2E}{\mathrm{d}k^2}\right)^{-1}}
$$

となります。有効質量はバンドの曲率で決まり，自由電子 $E=\hbar^2k^2/2m$ では $m^*=m$ に戻ります。

### (2)
2階微分は $\dfrac{\mathrm{d}^2E}{\mathrm{d}k^2}=2ta^2\cos ka$ です。これを (1) に代入すると，

$$
\finalanswer{m^*(k)=\frac{\hbar^2}{2ta^2\cos ka}}
$$

となります。$k=0$ と $k=\pi/a$ では $\cos ka=\pm1$ です。

$$
\finalanswer{m^*(0)=\frac{\hbar^2}{2ta^2}},\qquad \finalanswer{m^*(\pi/a)=-\frac{\hbar^2}{2ta^2}},\qquad \finalanswer{k=\pm\frac{\pi}{2a}\ \text{で発散}}
$$

となります。$k$ による変化を図に示します。

<!-- FIGURE solution (2): 上下2段のグラフ，共通の横軸 k（−π/a から π/a）。上段：E(k) = ε0 − 2t cos ka の実線，底 ε0 − 2t と上端 ε0 + 2t に目盛り，k = ±π/(2a) の変曲点に黒丸。下段：1/m* ∝ cos ka を実線で描き，k = 0 で正の最大，k = ±π/(2a) で 0，k = ±π/a で負の最小になる。k = ±π/(2a) に上下段を貫く縦の破線を引き，下段の正の領域に「m* > 0」，負の領域に「m* < 0」と注記。 -->

変曲点 $k=\pm\pi/2a$ を境に，力を加えたときの加速の向きが反転します。上端付近では，力と逆向きに加速されます。

### (3)
バンドの底の有効質量を $m$ で割ります。$2ta^2m=2\times1.602\times10^{-19}\times(3.0\times10^{-10})^2\times9.109\times10^{-31}=2.627\times10^{-68}\ \mathrm{J\,m^2\,kg}$，$\hbar^2=1.113\times10^{-68}\ \mathrm{J^2\,s^2}$ なので，

$$
\finalanswer{\frac{m^*}{m}\approx0.42}
$$

となります。隣の原子へ移る行列要素 $t$ が大きく，格子定数が大きいほど，電子は軽く動けます。

### (4)
バンドは $E(-k)=E(k)$ を満たすので $v(-k)=-v(k)$ で，すべての状態についての速度の和は0です。空いた状態を除いた和は，全体の和から $v(k_{\mathrm{e}})$ を引いたものになります。

$$
\finalanswer{I=-\frac{e}{L}\left[0-v(k_{\mathrm{e}})\right]=\frac{e}{L}v(k_{\mathrm{e}})}
$$

となります。この電流は，電荷 $+e$ の粒子1個が速度 $v(k_{\mathrm{e}})$ で動くときの電流と同じです。

次に，空いた状態の速度の時間変化を (1) と同じように計算します。$k_{\mathrm{e}}$ は上端の近くにあるので，$m^*(k_{\mathrm{e}})\approx-\dfrac{\hbar^2}{2ta^2}$ です。

$$
\frac{\mathrm{d}v(k_{\mathrm{e}})}{\mathrm{d}t}=\frac{-e\mathcal{E}}{m^*(k_{\mathrm{e}})}=\frac{2ta^2}{\hbar^2}e\mathcal{E}
$$

これを $m_{\mathrm{h}}\dfrac{\mathrm{d}v}{\mathrm{d}t}=e\mathcal{E}$ と比べると，

$$
\finalanswer{m_{\mathrm{h}}=\frac{\hbar^2}{2ta^2}}
$$

となります。満ちたバンドにできた空席は，正の電荷と正の質量をもつ粒子として振る舞います。これが正孔です。

===== FILE: 06solid_state/07/07_060.md =====
---
tags:
  - 基本
---

# 金属・半導体・絶縁体

## 問題
結晶中の電子の状態をバンドで考える。絶対零度で，電子はエネルギーの低い状態から順に占有するとする。電子のスピンの自由度は2である。異なるバンドどうしはエネルギーが重ならず，間にギャップがあると仮定する。ただし (3) では，弱い周期ポテンシャルの中の自由電子を考える。以下の問いに答えよ。

(1) 格子定数 $a$ の一次元の結晶が $N$ 個の単位胞からなり，周期境界条件を課す。1つのバンドに入りうる電子の数を求めよ。

(2) (1) の結晶で，各単位胞に原子が1個あり，各原子が価電子を $Z$ 個もつとする。完全に満たされたバンドの数と，一部だけ占有されたバンドがあるかどうかを，$Z$ が偶数と奇数の場合について答えよ。また，$Z=1$ で最も低いバンドが $E(k)=\varepsilon_0-2t\cos ka$（$t>0$）のとき，フェルミ波数 $k_{\mathrm{F}}$ とフェルミエネルギー $E_{\mathrm{F}}$ を求めよ。

(3) 格子定数 $a$ の2次元の正方格子で，単位胞あたり $Z$ 個の電子があり，それらを自由電子とみなしたときのフェルミ円の半径 $k_{\mathrm{F}}$ を求めよ。$Z=1$ と $Z=2$ のそれぞれについて，$k_{\mathrm{F}}a$ の数値を，第1ブリルアンゾーンの辺の中点までの距離 $\pi/a$ と頂点までの距離 $\sqrt{2}\pi/a$ と比べ，フェルミ円がゾーンの内側に収まるかどうかを答えよ。

(4) ナトリウムは体心立方格子で，基本単位胞に原子が1個あり，原子1個あたりの価電子は1個である。ケイ素はダイヤモンド構造で，基本単位胞に原子が2個あり，原子1個あたりの価電子は4個である。それぞれについて，基本単位胞あたりの価電子の数と，完全に満たされたバンドの数を答え，一部だけ占有されたバンドがあるかどうかを答えよ。

---

## 解答・解説

### (1)
周期境界条件から $k=\dfrac{2\pi\ell}{Na}$（$\ell$ は整数）で，第1ブリルアンゾーン $-\pi/a<k\le\pi/a$ には $\ell$ が $N$ 個入ります。1つのバンドは各 $k$ に1つの軌道状態をもち，そこにスピンの向きの違う電子が2個入ります。

$$
\finalanswer{2N\ \text{個}}
$$

となります。3次元でもゾーン内の $\boldsymbol{k}$ の数は単位胞の数に等しいので，同じ結果になります。

### (2)
電子は全部で $ZN$ 個あり，1つのバンドには $2N$ 個入るので，下から $Z/2$ 個分のバンドが埋まります。

$$
\finalanswer{Z\ \text{が偶数}:\ Z/2\ \text{個のバンドが満ち，一部占有のバンドはない}}
$$

$$
\finalanswer{Z\ \text{が奇数}:\ (Z-1)/2\ \text{個のバンドが満ち，次のバンドがちょうど半分占有される}}
$$

となります。一部だけ占有されたバンドがあると，フェルミ準位のすぐ上に空いた状態があるので，弱い電場でも電子が加速されて電流が流れます。そのため $Z$ が奇数なら金属です。$Z$ が偶数のときは，ギャップがあれば絶縁体か半導体になります。

$Z=1$ では，$|k|<k_{\mathrm{F}}$ の状態の数 $2\cdot\dfrac{2k_{\mathrm{F}}}{2\pi/Na}$ を $N$ とおきます。

$$
\finalanswer{k_{\mathrm{F}}=\frac{\pi}{2a}},\qquad \finalanswer{E_{\mathrm{F}}=\varepsilon_0-2t\cos\frac{\pi}{2}=\varepsilon_0}
$$

となり，フェルミ準位はバンドの中央にきます。

### (3)
半径 $k_{\mathrm{F}}$ の円の中の状態の数は，スピンを含めて $2\cdot\dfrac{\pi k_{\mathrm{F}}^{\,2}}{(2\pi)^2/A}$ です。$A$ は結晶の面積です。これを電子数 $ZA/a^2$ に等しいとおくと，

$$
\finalanswer{k_{\mathrm{F}}=\frac{\sqrt{2\pi Z}}{a}}
$$

となります。$\pi=3.14$，$\sqrt{2}\pi=4.44$ と比べます。

$$
\finalanswer{Z=1:\ k_{\mathrm{F}}a=2.51<\pi\ \text{でゾーンの内側に収まる}}
$$

$$
\finalanswer{Z=2:\ \pi<k_{\mathrm{F}}a=3.54<\sqrt{2}\pi\ \text{で辺の外にはみ出す}}
$$

となります。2つのフェルミ円を図に示します。

<!-- FIGURE solution (3): k_x，k_y 軸を引き，第1ブリルアンゾーン（一辺 2π/a の正方形，辺の中点が ±π/a）を太線で描く。原点中心に半径 2.51/a の円を破線で描いて「Z = 1」，半径 3.54/a の円を実線で描いて「Z = 2」とラベル。Z = 2 の円が正方形の4辺の中点付近で外にはみ出し，4つの角は円の外に残る様子が分かるようにする。正方形の外にはみ出した部分を薄く塗る。 -->

$Z=2$ では電子が2番目のバンドに入る一方，最も低いバンドにはゾーンの角に空きが残ります。ポテンシャルが弱いとバンドが重なるので，単位胞あたりの電子数が偶数でも金属になります。2価のマグネシウムやカルシウムが金属であるのは，このためです。

### (4)
ナトリウムは基本単位胞あたり価電子1個なので，(2) の $Z$ が奇数の場合にあたります。

$$
\finalanswer{\text{ナトリウム}:\ 1\ \text{個，満ちたバンドは}\ 0\ \text{個，最も低いバンドが半分占有される}}
$$

ケイ素は基本単位胞あたり $2\times4=8$ 個の価電子をもちます。

$$
\finalanswer{\text{ケイ素}:\ 8\ \text{個，満ちたバンドは}\ 4\ \text{個，一部占有のバンドはない}}
$$

となります。ナトリウムは金属になり，ケイ素は満ちた4つのバンドの上にギャップがあるので，絶縁体か半導体になります。実際のケイ素のギャップは約 1.1 eV で，半導体です。

===== FILE: 06solid_state/07/07_070.md =====
---
tags:
  - 発展
---

# 電場中のブロッホ電子

## 問題
格子定数 $a$ の一次元の結晶中で，電子のバンドを $E(k)=\varepsilon_0-2t\cos ka$（$t>0$）とする。電子の電荷を $-e$（$e>0$）とし，$+x$ 方向に一様な静電場 $\mathcal{E}>0$ をかける。静電ポテンシャルは $-\mathcal{E}x$ なので，位置 $x$ の電子のポテンシャルエネルギーは $e\mathcal{E}x$ である。電子を，位置 $x$ と波数 $k$ をもつ波束として扱い，その速度は群速度 $v=\dfrac{1}{\hbar}\dfrac{\mathrm{d}E}{\mathrm{d}k}$ であるとする。電場はバンド間の遷移を起こさないほど弱いとし，(4) を除いて散乱は無視する。以下の問いに答えよ。

(1) 波束の全エネルギー $E(k)+e\mathcal{E}x$ が保存されることを用いて，$k$ の時間変化を表す運動方程式を導け。

(2) $k(0)=0$ として $k(t)$ を求めよ。$k$ と $k+2\pi/a$ が同じ状態を表すことに注意して，電子の運動の周期 $T_{\mathrm{B}}$ と角振動数 $\omega_{\mathrm{B}}=2\pi/T_{\mathrm{B}}$ を求めよ。

(3) $x(0)=0$ として $x(t)$ を求め，電子が動く範囲を求めよ。

(4) 散乱の緩和時間を $\tau$ とすると，振動が観測されるには $\omega_{\mathrm{B}}\tau\gg1$ が必要である。$\mathcal{E}=1.0\times10^6\ \mathrm{V/m}$ として，次の2つの場合の $\omega_{\mathrm{B}}\tau$ を求めよ。通常の結晶で $a=0.30\ \mathrm{nm}$，$\tau=1.0\times10^{-14}\ \mathrm{s}$ の場合と，半導体超格子で周期 $a=10\ \mathrm{nm}$，バンド幅 $4t=20\ \mathrm{meV}$，$\tau=0.50\ \mathrm{ps}$ の場合である。また，超格子での電子が動く範囲の幅を求めよ。$\hbar=1.055\times10^{-34}\ \mathrm{J\,s}$，$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

---

## 解答・解説

### (1)
全エネルギーを時間で微分して0とおきます。$E$ は $k$ を通して時間に依存し，$\dfrac{\mathrm{d}x}{\mathrm{d}t}=v=\dfrac{1}{\hbar}\dfrac{\mathrm{d}E}{\mathrm{d}k}$ です。

$$
\frac{\mathrm{d}E}{\mathrm{d}k}\frac{\mathrm{d}k}{\mathrm{d}t}+e\mathcal{E}\cdot\frac{1}{\hbar}\frac{\mathrm{d}E}{\mathrm{d}k}=0
$$

$\dfrac{\mathrm{d}E}{\mathrm{d}k}\ne0$ のとき両辺をこれで割ると，次の式が得られます。$\dfrac{\mathrm{d}E}{\mathrm{d}k}=0$ となる孤立した点でも，連続性から同じ式が成り立ちます。

$$
\finalanswer{\hbar\frac{\mathrm{d}k}{\mathrm{d}t}=-e\mathcal{E}}
$$

となります。結晶運動量 $\hbar k$ は，外力 $-e\mathcal{E}$ だけで変化します。周期ポテンシャルからの力は，バンドの形 $E(k)$ にすでに含まれています。

### (2)
(1) の右辺は一定なので，$k$ は時間に比例して減少します。

$$
\finalanswer{k(t)=-\frac{e\mathcal{E}}{\hbar}t}
$$

$k$ が $-\pi/a$ に達すると，それは $\pi/a$ と同じ状態なので，ゾーンの反対側から再び現れます。これはゾーン境界でのブラッグ反射にあたります。$k$ が $2\pi/a$ だけ変化すると状態がもとに戻るので，

$$
\finalanswer{T_{\mathrm{B}}=\frac{2\pi\hbar}{e\mathcal{E}a}},\qquad \finalanswer{\omega_{\mathrm{B}}=\frac{e\mathcal{E}a}{\hbar}}
$$

となります。

### (3)
速度は $v=\dfrac{2ta}{\hbar}\sin ka$ で，$k=-\omega_{\mathrm{B}}t/a$ を代入すると $v=-\dfrac{2ta}{\hbar}\sin\omega_{\mathrm{B}}t$ です。これを時間で積分します。

$$
x(t)=-\frac{2ta}{\hbar}\int_0^t\sin\omega_{\mathrm{B}}t'\,\mathrm{d}t'=\frac{2ta}{\hbar\omega_{\mathrm{B}}}\left(\cos\omega_{\mathrm{B}}t-1\right)
$$

$\hbar\omega_{\mathrm{B}}=e\mathcal{E}a$ を使うと，

$$
\finalanswer{x(t)=\frac{2t}{e\mathcal{E}}\left(\cos\omega_{\mathrm{B}}t-1\right)},\qquad \finalanswer{-\frac{4t}{e\mathcal{E}}\le x\le0}
$$

となります。電子は電場の中を一方向に加速され続けるのではなく，その場で振動します。これがブロッホ振動です。範囲の幅 $4t/e\mathcal{E}$ は，バンド幅をポテンシャルエネルギーの勾配で割ったもので，全エネルギーの保存からも直接得られます。運動の様子を図に示します。

<!-- FIGURE solution (3): 上下2段のグラフ，共通の横軸 t（0 から 2T_B）。上段：k(t)。縦軸 −π/a〜π/a。0 から直線的に減少し，−π/a に達すると π/a へ跳んで再び減少するのこぎり波を実線で描き，跳ぶ位置に縦の点線。下段：x(t)。縦軸に 0 と −4t/(eℰ) の目盛り。x = (2t/eℰ)(cos ω_B t − 1) を実線で描き，0 から下がって −4t/(eℰ) で折り返し，0 に戻る振動を2周期分示す。横軸に T_B と 2T_B の目盛り。 -->

### (4)
$\omega_{\mathrm{B}}=e\mathcal{E}a/\hbar$ を計算して $\tau$ をかけます。通常の結晶では $\omega_{\mathrm{B}}=\dfrac{1.602\times10^{-19}\times1.0\times10^6\times3.0\times10^{-10}}{1.055\times10^{-34}}\ \mathrm{s^{-1}}=4.56\times10^{11}\ \mathrm{s^{-1}}$ です。超格子では，$a$ が大きいぶん $\omega_{\mathrm{B}}=1.52\times10^{13}\ \mathrm{s^{-1}}$ になります。

$$
\finalanswer{\text{通常の結晶}:\ \omega_{\mathrm{B}}\tau\approx4.6\times10^{-3}},\qquad \finalanswer{\text{超格子}:\ \omega_{\mathrm{B}}\tau\approx7.6}
$$

超格子での範囲の幅は $4t/e\mathcal{E}=0.020\ \mathrm{V}/(1.0\times10^6\ \mathrm{V/m})$ です。

$$
\finalanswer{\frac{4t}{e\mathcal{E}}=2.0\times10^{-8}\ \mathrm{m}=20\ \mathrm{nm}}
$$

となります。通常の結晶では電子が1周期を回るずっと前に散乱されるので，ブロッホ振動は見えません。周期が長くバンド幅の狭い超格子では $\omega_{\mathrm{B}}\tau>1$ となり，約 2.4 THz の振動が実際に観測されています。

===== END =====