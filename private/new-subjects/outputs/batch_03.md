===== FILE: 06solid_state/08/08_010.md =====
---
tags:
  - 標準
---

# 真性半導体のキャリア密度

## 問題
半導体の伝導帯の底のエネルギーを $E_{\mathrm{c}}$，価電子帯の頂上のエネルギーを $E_{\mathrm{v}}$ とし，バンドギャップを $E_{\mathrm{g}}=E_{\mathrm{c}}-E_{\mathrm{v}}$ とする。伝導帯の電子のエネルギーは $E=E_{\mathrm{c}}+\dfrac{\hbar^2k^2}{2m_{\mathrm{e}}}$，価電子帯の電子のエネルギーは $E=E_{\mathrm{v}}-\dfrac{\hbar^2k^2}{2m_{\mathrm{h}}}$ と書けるとする。$m_{\mathrm{e}}>0$，$m_{\mathrm{h}}>0$ はそれぞれ電子と正孔の有効質量で，$k=|\boldsymbol{k}|$ である。スピンの自由度は2とする。

電子の占有確率はフェルミ分布 $f(E)=\dfrac{1}{e^{(E-\mu)/k_{\mathrm{B}}T}+1}$ に従う。$\mu$ は化学ポテンシャル，$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。$\mu$ はギャップの中にあり，$E_{\mathrm{c}}-\mu\gg k_{\mathrm{B}}T$ と $\mu-E_{\mathrm{v}}\gg k_{\mathrm{B}}T$ を満たすとする。必要なら $\displaystyle\int_0^\infty x^{1/2}e^{-x}\,\mathrm{d}x=\frac{\sqrt{\pi}}{2}$ を用いてよい。以下の問いに答えよ。

(1) 伝導帯の単位体積あたりの状態密度 $D_{\mathrm{c}}(E)$ を求めよ。また，伝導帯の電子密度 $n$ が $n=N_{\mathrm{c}}e^{-(E_{\mathrm{c}}-\mu)/k_{\mathrm{B}}T}$ の形に書けることを示し，$N_{\mathrm{c}}$ を求めよ。

(2) 価電子帯の正孔密度 $p$ を，状態が電子に占有されていない確率 $1-f(E)$ を用いて求めよ。$p=N_{\mathrm{v}}e^{-(\mu-E_{\mathrm{v}})/k_{\mathrm{B}}T}$ と書いたときの $N_{\mathrm{v}}$ も求めよ。さらに，積 $np$ を $N_{\mathrm{c}},N_{\mathrm{v}},E_{\mathrm{g}}$ で表せ。

(3) 不純物を含まない真性半導体では $n=p$ が成り立つ。このときのキャリア密度 $n_{\mathrm{i}}$ と化学ポテンシャル $\mu_{\mathrm{i}}$ を求めよ。

(4) $\ln\left(n_{\mathrm{i}}T^{-3/2}\right)$ を縦軸に，$1/T$ を横軸にとったグラフの傾きを求めよ。また，$E_{\mathrm{g}}=1.12\ \mathrm{eV}$ のケイ素の温度を $300\ \mathrm{K}$ から $310\ \mathrm{K}$ に上げると，$n_{\mathrm{i}}$ は何倍になるかを求めよ。$E_{\mathrm{g}}$ は温度によらないとし，$k_{\mathrm{B}}=8.617\times10^{-5}\ \mathrm{eV/K}$ とする。

---

## 解答・解説

### (1)
まず，エネルギーが $E$ 以下の状態の数を数えて，それを $E$ で微分します。許される $\boldsymbol{k}$ は波数空間の体積 $(2\pi)^3/V$ ごとに1個あります。$V$ は結晶の体積です。そのため，スピンを含めた単位体積あたりの状態の数は次のようになります。

$$
\begin{aligned}
\mathcal{N}_{\mathrm{c}}(E)&=2\cdot\frac{1}{(2\pi)^3}\cdot\frac{4\pi}{3}k^3\\
&=\frac{1}{3\pi^2}\left[\frac{2m_{\mathrm{e}}(E-E_{\mathrm{c}})}{\hbar^2}\right]^{3/2}
\end{aligned}
$$

これを $E$ で微分すると，

$$
\finalanswer{D_{\mathrm{c}}(E)=\frac{1}{2\pi^2}\left(\frac{2m_{\mathrm{e}}}{\hbar^2}\right)^{3/2}\sqrt{E-E_{\mathrm{c}}}}
$$

となります。$E_{\mathrm{c}}-\mu\gg k_{\mathrm{B}}T$ なので，伝導帯の中では $f(E)\approx e^{-(E-\mu)/k_{\mathrm{B}}T}$ と近似できます。$x=(E-E_{\mathrm{c}})/k_{\mathrm{B}}T$ とおいて積分すると，

$$
\begin{aligned}
n&=\int_{E_{\mathrm{c}}}^{\infty}D_{\mathrm{c}}(E)f(E)\,\mathrm{d}E\\
&\approx\frac{1}{2\pi^2}\left(\frac{2m_{\mathrm{e}}k_{\mathrm{B}}T}{\hbar^2}\right)^{3/2}e^{-(E_{\mathrm{c}}-\mu)/k_{\mathrm{B}}T}\int_0^\infty x^{1/2}e^{-x}\,\mathrm{d}x\\
&=\frac{1}{4\pi^{3/2}}\left(\frac{2m_{\mathrm{e}}k_{\mathrm{B}}T}{\hbar^2}\right)^{3/2}e^{-(E_{\mathrm{c}}-\mu)/k_{\mathrm{B}}T}
\end{aligned}
$$

が得られます。係数をまとめると，

$$
\finalanswer{N_{\mathrm{c}}=2\left(\frac{m_{\mathrm{e}}k_{\mathrm{B}}T}{2\pi\hbar^2}\right)^{3/2}}
$$

となります。$N_{\mathrm{c}}$ は，伝導帯の状態がすべて底のエネルギー $E_{\mathrm{c}}$ に集まっているとみなしたときの実効的な状態の数で，有効状態密度とよばれます。

### (2)
$\mu-E\gg k_{\mathrm{B}}T$ なので，価電子帯では電子が占有していない確率を次のように近似できます。

$$
1-f(E)=\frac{1}{e^{(\mu-E)/k_{\mathrm{B}}T}+1}\approx e^{-(\mu-E)/k_{\mathrm{B}}T}
$$

価電子帯の状態密度は，(1) の $m_{\mathrm{e}}$ を $m_{\mathrm{h}}$ に，$E-E_{\mathrm{c}}$ を $E_{\mathrm{v}}-E$ に置き換えたものです。同じ積分を実行すると，

$$
\begin{aligned}
&\finalanswer{p=N_{\mathrm{v}}e^{-(\mu-E_{\mathrm{v}})/k_{\mathrm{B}}T}}\\
&\finalanswer{N_{\mathrm{v}}=2\left(\frac{m_{\mathrm{h}}k_{\mathrm{B}}T}{2\pi\hbar^2}\right)^{3/2}}
\end{aligned}
$$

となります。キャリアの分布を図に示します。

<!-- FIGURE solution (2): 縦軸をエネルギー E とし，上に伝導帯の底 E_c，下に価電子帯の頂上 E_v の水平線を引き，その間のギャップの中ほどに μ の破線を引く。左側に状態密度を横向きに描く：E_c から上へ √(E−E_c) で広がる曲線と，E_v から下へ √(E_v−E) で広がる曲線。右側に，伝導帯の電子の分布 D_c f（E_c の少し上に山があり，上に向かって指数関数的に減る細い山）と，価電子帯の正孔の分布 D_v(1−f)（E_v の少し下に山がある細い山）を塗りつぶして描き，それぞれ n，p とラベルする。 -->

2つの密度をかけると $\mu$ が消えます。

$$
\finalanswer{np=N_{\mathrm{c}}N_{\mathrm{v}}e^{-E_{\mathrm{g}}/k_{\mathrm{B}}T}}
$$

となります。この積は $\mu$ によらないので，不純物を加えて $\mu$ が動いても，同じ温度なら同じ値になります。

### (3)
$n=p$ とおくと，$\mu$ についての方程式が得られます。

$$
e^{(2\mu-E_{\mathrm{c}}-E_{\mathrm{v}})/k_{\mathrm{B}}T}=\frac{N_{\mathrm{v}}}{N_{\mathrm{c}}}=\left(\frac{m_{\mathrm{h}}}{m_{\mathrm{e}}}\right)^{3/2}
$$

これを $\mu$ について解きます。キャリア密度は，$n_{\mathrm{i}}^{\,2}=np$ に (2) の結果を使えば求まります。

$$
\begin{aligned}
&\finalanswer{n_{\mathrm{i}}=\sqrt{N_{\mathrm{c}}N_{\mathrm{v}}}\,e^{-E_{\mathrm{g}}/2k_{\mathrm{B}}T}=2\left(\frac{k_{\mathrm{B}}T}{2\pi\hbar^2}\right)^{3/2}(m_{\mathrm{e}}m_{\mathrm{h}})^{3/4}e^{-E_{\mathrm{g}}/2k_{\mathrm{B}}T}}\\
&\finalanswer{\mu_{\mathrm{i}}=\frac{E_{\mathrm{c}}+E_{\mathrm{v}}}{2}+\frac{3}{4}k_{\mathrm{B}}T\ln\frac{m_{\mathrm{h}}}{m_{\mathrm{e}}}}
\end{aligned}
$$

となります。化学ポテンシャルはギャップの中央にあり，そこから有効質量の違いの分だけわずかにずれます。

### (4)
(3) の $n_{\mathrm{i}}$ を $T^{3/2}$ で割って対数をとると，$1/T$ の1次関数になります。

$$
\ln\left(n_{\mathrm{i}}T^{-3/2}\right)=\text{定数}-\frac{E_{\mathrm{g}}}{2k_{\mathrm{B}}}\cdot\frac{1}{T}
$$

したがって，

$$
\finalanswer{\text{傾き}=-\frac{E_{\mathrm{g}}}{2k_{\mathrm{B}}}}
$$

となります。この傾きを測ればバンドギャップが求まります。

2つの温度での $n_{\mathrm{i}}$ の比は，べきの因子と指数の因子の積です。

$$
\begin{aligned}
\frac{n_{\mathrm{i}}(310\ \mathrm{K})}{n_{\mathrm{i}}(300\ \mathrm{K})}
&=\left(\frac{310}{300}\right)^{3/2}\exp\left[\frac{E_{\mathrm{g}}}{2k_{\mathrm{B}}}\left(\frac{1}{300\ \mathrm{K}}-\frac{1}{310\ \mathrm{K}}\right)\right]\\
&=1.050\times e^{0.699}
\end{aligned}
$$

より，

$$
\finalanswer{\frac{n_{\mathrm{i}}(310\ \mathrm{K})}{n_{\mathrm{i}}(300\ \mathrm{K})}\approx2.1}
$$

となります。わずか $10\ \mathrm{K}$ で約2倍になり，その大部分は指数関数の因子によるものです。

===== FILE: 06solid_state/08/08_020.md =====
---
tags:
  - 標準
---

# ドナー準位と水素原子模型

## 問題
ケイ素やヒ化ガリウムに5価の不純物原子（ドナー）を加えると，余分な電子1個が電荷 $+e$ の不純物イオンに束縛される。この電子を，伝導帯の有効質量 $m^*$ をもつ自由粒子とみなす。電子は比誘電率 $\varepsilon_{\mathrm{r}}$ の一様な媒質の中で，イオンからクーロン引力を受けるとする。伝導帯の底をエネルギーの原点にとり，イオンを原点に置くと，電子のハミルトニアンは

$$
\hat{H}=-\frac{\hbar^2}{2m^*}\nabla^2-\frac{e^2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r}
$$

である。$\varepsilon_0$ は真空の誘電率，$r$ はイオンからの距離である。真空中の電子の質量を $m$ とし，ボーア半径を $a_{\mathrm{B}}=\dfrac{4\pi\varepsilon_0\hbar^2}{me^2}$，リュードベリ定数を $\mathrm{Ry}=\dfrac{\hbar^2}{2ma_{\mathrm{B}}^{\,2}}$ とする。

基底状態を，試行関数 $\psi_b(r)=\dfrac{1}{\sqrt{\pi b^3}}e^{-r/b}$（$b>0$）を用いた変分法で調べる。必要なら $\displaystyle\int_0^\infty r^ne^{-\lambda r}\,\mathrm{d}r=\frac{n!}{\lambda^{n+1}}$（$\lambda>0$）を用いてよい。以下の問いに答えよ。

(1) $\psi_b$ に対する運動エネルギーの期待値 $\langle T\rangle$ とポテンシャルエネルギーの期待値 $\langle V\rangle$ を，$b$ の関数として求めよ。

(2) エネルギーの期待値を最小にする $b$ を $a_{\mathrm{d}}$，そのときのエネルギーを $-E_{\mathrm{d}}$ とする。$a_{\mathrm{d}}$ と $E_{\mathrm{d}}$ を，$a_{\mathrm{B}}$，$\mathrm{Ry}$，$m^*/m$，$\varepsilon_{\mathrm{r}}$ で表せ。

(3) ヒ化ガリウムでは $m^*=0.067m$，$\varepsilon_{\mathrm{r}}=12.9$ である。$a_{\mathrm{B}}=0.0529\ \mathrm{nm}$，$\mathrm{Ry}=13.6\ \mathrm{eV}$ として，$E_{\mathrm{d}}$ と $a_{\mathrm{d}}$ を求めよ。また，$a_{\mathrm{d}}$ は格子定数 $0.565\ \mathrm{nm}$ の何倍かを求めよ。

(4) ドナーの密度 $N_{\mathrm{D}}$ が大きくなると，隣り合うドナーの電子の波動関数が重なり，電子はドナーから離れて結晶中を動けるようになる。この変化が起こる密度の目安を $N_{\mathrm{D}}^{\,1/3}a_{\mathrm{d}}=0.25$ とする。この目安の密度 $N_{\mathrm{M}}$ を $a_{\mathrm{B}}$，$m^*/m$，$\varepsilon_{\mathrm{r}}$ で表し，ヒ化ガリウムの値を求めよ。

---

## 解答・解説

### (1)
運動エネルギーの期待値は，部分積分によって $\dfrac{\hbar^2}{2m^*}\displaystyle\int|\nabla\psi_b|^2\,\mathrm{d}^3r$ と書けます。$\psi_b$ は $r$ だけの関数で，$|\nabla\psi_b|=\psi_b/b$ なので，規格化条件を使うと積分はすぐに求まります。

$$
\begin{aligned}
\langle T\rangle&=\frac{\hbar^2}{2m^*}\cdot\frac{1}{b^2}\int\psi_b^{\,2}\,\mathrm{d}^3r\\
&=\frac{\hbar^2}{2m^*b^2}
\end{aligned}
$$

ポテンシャルエネルギーの期待値は，$\langle 1/r\rangle$ を求めればわかります。与えられた積分で $n=1$，$\lambda=2/b$ とおきます。

$$
\begin{aligned}
\left\langle\frac{1}{r}\right\rangle&=\frac{1}{\pi b^3}\int_0^\infty\frac{1}{r}e^{-2r/b}\,4\pi r^2\,\mathrm{d}r\\
&=\frac{4}{b^3}\cdot\frac{b^2}{4}=\frac{1}{b}
\end{aligned}
$$

以上から，

$$
\begin{aligned}
&\finalanswer{\langle T\rangle=\frac{\hbar^2}{2m^*b^2}}\\
&\finalanswer{\langle V\rangle=-\frac{e^2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}b}}
\end{aligned}
$$

となります。

### (2)
エネルギーの期待値 $E(b)=\langle T\rangle+\langle V\rangle$ を $b$ で微分して0とおきます。

$$
\frac{\mathrm{d}E}{\mathrm{d}b}=-\frac{\hbar^2}{m^*b^3}+\frac{e^2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}b^2}=0
$$

これを解くと $b=\dfrac{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}\hbar^2}{m^*e^2}$ です。このとき $\langle V\rangle=-2\langle T\rangle$ となるので，エネルギーは $-\langle T\rangle$ に等しくなります。$a_{\mathrm{B}}$ と $\mathrm{Ry}$ を使って書き直すと，

$$
\begin{aligned}
&\finalanswer{a_{\mathrm{d}}=\varepsilon_{\mathrm{r}}\frac{m}{m^*}a_{\mathrm{B}}}\\
&\finalanswer{E_{\mathrm{d}}=\frac{m^*}{m}\cdot\frac{1}{\varepsilon_{\mathrm{r}}^{\,2}}\,\mathrm{Ry}}
\end{aligned}
$$

となります。このハミルトニアンは，水素原子の $m$ を $m^*$ に，$e^2$ を $e^2/\varepsilon_{\mathrm{r}}$ に置き換えたものです。試行関数は水素原子の基底状態と同じ形なので，この変分の結果は厳密な値と一致します。

### (3)
(2) の式に数値を代入します。

$$
\begin{aligned}
E_{\mathrm{d}}&=\frac{0.067}{12.9^2}\times13.6\ \mathrm{eV}\\
a_{\mathrm{d}}&=\frac{12.9}{0.067}\times0.0529\ \mathrm{nm}
\end{aligned}
$$

これを計算すると，

$$
\begin{aligned}
&\finalanswer{E_{\mathrm{d}}\approx5.5\ \mathrm{meV}}\\
&\finalanswer{a_{\mathrm{d}}\approx10\ \mathrm{nm}}\\
&\finalanswer{\frac{a_{\mathrm{d}}}{0.565\ \mathrm{nm}}\approx18}
\end{aligned}
$$

となります。束縛エネルギーは室温の熱エネルギー $k_{\mathrm{B}}T\approx26\ \mathrm{meV}$ より小さいので，室温ではほとんどのドナーが電離しています。電子の軌道は格子定数の約20倍に広がり，多数の原子を含みます。そのため，結晶を比誘電率 $\varepsilon_{\mathrm{r}}$ の連続媒質とみなす近似が正当化されます。

### (4)
目安の式を $N_{\mathrm{D}}$ について解き，(2) の $a_{\mathrm{d}}$ を代入します。

$$
\begin{aligned}
N_{\mathrm{M}}&=\left(\frac{0.25}{a_{\mathrm{d}}}\right)^3\\
&=\frac{1}{64}\left(\frac{m^*}{m\,\varepsilon_{\mathrm{r}}a_{\mathrm{B}}}\right)^3
\end{aligned}
$$

ヒ化ガリウムでは $a_{\mathrm{d}}=10.2\ \mathrm{nm}$ を使うと，

$$
\begin{aligned}
&\finalanswer{N_{\mathrm{M}}=\frac{1}{64}\left(\frac{m^*}{m\,\varepsilon_{\mathrm{r}}a_{\mathrm{B}}}\right)^3}\\
&\finalanswer{N_{\mathrm{M}}\approx1.5\times10^{22}\ \mathrm{m^{-3}}}
\end{aligned}
$$

となります。結晶の原子密度 $4\times10^{28}\ \mathrm{m^{-3}}$ と比べると，100万分の1以下のわずかな添加で金属的になります。有効質量が小さく誘電率が大きい物質ほど，ドナーの軌道が大きくなるからです。

===== FILE: 06solid_state/08/08_030.md =====
---
tags:
  - 標準
---

# 不純物半導体のフェルミ準位

## 問題
密度 $N_{\mathrm{D}}$ のドナーを含む n 型半導体を考える。アクセプターは含まないとする。伝導帯の底のエネルギーを $E_{\mathrm{c}}$，ドナー準位を $E_{\mathrm{D}}=E_{\mathrm{c}}-E_{\mathrm{d}}$（$E_{\mathrm{d}}>0$）とする。伝導帯の電子は非縮退であり，その密度は化学ポテンシャル $\mu$ を用いて $n=N_{\mathrm{c}}e^{-(E_{\mathrm{c}}-\mu)/k_{\mathrm{B}}T}$ と書ける。$N_{\mathrm{c}}$ は $T^{3/2}$ に比例する定数，$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。

1つのドナーがとりうる状態は，電子がない状態と，エネルギー $E_{\mathrm{D}}$ の電子が上向きまたは下向きのスピンで1個入った状態の3つとする。電子間の反発が強いため，電子が2個入った状態はないものとする。以下の問いに答えよ。

(1) 1つのドナーを化学ポテンシャル $\mu$，温度 $T$ の環境と電子をやりとりする系とみなし，大正準分布を用いて，ドナーが電子を1個もつ確率 $P_{\mathrm{d}}$ を求めよ。

(2) 正孔の寄与を無視すると，電気的中性の条件は $n=N_{\mathrm{D}}(1-P_{\mathrm{d}})$ である。$n_1=\dfrac{N_{\mathrm{c}}}{2}e^{-E_{\mathrm{d}}/k_{\mathrm{B}}T}$ とおいて，$n$ を $n_1$ と $N_{\mathrm{D}}$ で表せ。

(3) $n_1\ll N_{\mathrm{D}}$ の低温と，$n_1\gg N_{\mathrm{D}}$ の場合のそれぞれについて，$n$ と $\mu$ を求めよ。また，$T\to0$ での $\mu$ の極限を求めよ。

(4) さらに高温では，ドナーはすべて電離しているとみなせるが，価電子帯から励起された正孔も考える必要がある。正孔の密度を $p$ とし，$np=n_{\mathrm{i}}^{\,2}$ と中性の条件 $n=p+N_{\mathrm{D}}$ が成り立つとする。$n_{\mathrm{i}}$ は真性キャリア密度である。$n$ を $N_{\mathrm{D}}$ と $n_{\mathrm{i}}$ で表せ。また，$n=n_{\mathrm{i}}$ となるときの化学ポテンシャルを $\mu_{\mathrm{i}}$ として，$\mu-\mu_{\mathrm{i}}$ を求めよ。

---

## 解答・解説

### (1)
大正準分布では，粒子数 $N$，エネルギー $E$ の状態の重みは $e^{-(E-\mu N)/k_{\mathrm{B}}T}$ です。電子のない状態の重みは1で，電子が1個入った状態はスピンの向きで2つあります。そのため大分配関数は次のようになります。

$$
\Xi=1+2e^{-(E_{\mathrm{D}}-\mu)/k_{\mathrm{B}}T}
$$

電子が入っている2つの状態の重みを $\Xi$ で割ると，

$$
\finalanswer{P_{\mathrm{d}}=\frac{1}{1+\frac{1}{2}e^{(E_{\mathrm{D}}-\mu)/k_{\mathrm{B}}T}}}
$$

となります。フェルミ分布とは指数関数の前の係数 $\dfrac{1}{2}$ だけが異なります。2個目の電子が入れないため，電子のいない状態がスピンの縮退をもつ状態より相対的に少なくなるのです。

### (2)
電離したドナーの密度は次のとおりです。

$$
N_{\mathrm{D}}(1-P_{\mathrm{d}})=\frac{N_{\mathrm{D}}}{1+2e^{(\mu-E_{\mathrm{D}})/k_{\mathrm{B}}T}}
$$

$n$ の式から $e^{\mu/k_{\mathrm{B}}T}$ を $n$ で表し，分母の指数関数を書き直します。

$$
\begin{aligned}
2e^{(\mu-E_{\mathrm{D}})/k_{\mathrm{B}}T}&=\frac{2n}{N_{\mathrm{c}}}e^{(E_{\mathrm{c}}-E_{\mathrm{D}})/k_{\mathrm{B}}T}\\
&=\frac{n}{n_1}
\end{aligned}
$$

これを中性の条件に入れると，$n$ についての2次方程式 $n^2+n_1n-n_1N_{\mathrm{D}}=0$ が得られます。正の解をとると，

$$
\finalanswer{n=\frac{n_1}{2}\left(\sqrt{1+\frac{4N_{\mathrm{D}}}{n_1}}-1\right)}
$$

となります。

### (3)
$n_1\ll N_{\mathrm{D}}$ のときは，根号の中の1を無視できます。$n_1\gg N_{\mathrm{D}}$ のときは，根号を1次まで展開します。$\mu$ は，$n$ の式を逆に解いた $\mu=E_{\mathrm{c}}-k_{\mathrm{B}}T\ln(N_{\mathrm{c}}/n)$ から求めます。低温の場合は次のようになります。

$$
\begin{aligned}
&\finalanswer{n\approx\sqrt{\frac{N_{\mathrm{c}}N_{\mathrm{D}}}{2}}\,e^{-E_{\mathrm{d}}/2k_{\mathrm{B}}T}}\\
&\finalanswer{\mu\approx\frac{E_{\mathrm{c}}+E_{\mathrm{D}}}{2}-\frac{k_{\mathrm{B}}T}{2}\ln\frac{2N_{\mathrm{c}}}{N_{\mathrm{D}}}}
\end{aligned}
$$

$n_1\gg N_{\mathrm{D}}$ の場合は次のようになります。

$$
\begin{aligned}
&\finalanswer{n\approx N_{\mathrm{D}}}\\
&\finalanswer{\mu\approx E_{\mathrm{c}}-k_{\mathrm{B}}T\ln\frac{N_{\mathrm{c}}}{N_{\mathrm{D}}}}
\end{aligned}
$$

$N_{\mathrm{c}}\propto T^{3/2}$ なので，$T\to0$ で $T\ln N_{\mathrm{c}}\to0$ となり，

$$
\finalanswer{\mu\to\frac{E_{\mathrm{c}}+E_{\mathrm{D}}}{2}}
$$

となります。$n_1\gg N_{\mathrm{D}}$ では，ドナーの電子がほぼすべて伝導帯に出払っているので，この領域を出払い領域とよびます。電子密度の温度変化を図に示します。

<!-- FIGURE solution (3): 横軸 1/T，縦軸 ln n。右側の低温域（1/T が大きい）は傾き −E_d/(2k_B) の直線で，「ln n ∝ −E_d/2k_BT」と注記する。中央は ln N_D の高さの水平線で「出払い領域 n ≈ N_D」と注記する。左側の高温域（1/T が小さい）は傾き −E_g/(2k_B) のより急な直線で，「真性領域」と注記する。3つの部分を滑らかにつないだ1本の実線で描き，縦軸に ln N_D の目盛りを付ける。 -->

### (4)
$p=n_{\mathrm{i}}^{\,2}/n$ を中性の条件に代入すると，2次方程式 $n^2-N_{\mathrm{D}}n-n_{\mathrm{i}}^{\,2}=0$ が得られます。正の解は，

$$
\finalanswer{n=\frac{N_{\mathrm{D}}}{2}+\sqrt{\frac{N_{\mathrm{D}}^{\,2}}{4}+n_{\mathrm{i}}^{\,2}}}
$$

です。$\mu_{\mathrm{i}}$ の定義から $n_{\mathrm{i}}=N_{\mathrm{c}}e^{-(E_{\mathrm{c}}-\mu_{\mathrm{i}})/k_{\mathrm{B}}T}$ です。これと $n$ の式の比をとると，

$$
\finalanswer{\mu-\mu_{\mathrm{i}}=k_{\mathrm{B}}T\ln\frac{n}{n_{\mathrm{i}}}}
$$

となります。$n_{\mathrm{i}}\ll N_{\mathrm{D}}$ では $n\approx N_{\mathrm{D}}$ となり，(3) の出払い領域につながります。温度が上がって $n_{\mathrm{i}}\gg N_{\mathrm{D}}$ になると $n\approx n_{\mathrm{i}}$ となり，$\mu$ はギャップの中央付近の $\mu_{\mathrm{i}}$ に近づいて，半導体は真性半導体と同じように振る舞います。

===== FILE: 06solid_state/08/08_040.md =====
---
tags:
  - 基本
---

# 移動度と伝導度

## 問題
半導体に，密度 $n$ の伝導電子と密度 $p$ の正孔があるとする。電子は電荷 $-e$（$e>0$），有効質量 $m_{\mathrm{e}}$，緩和時間 $\tau_{\mathrm{e}}$ をもち，正孔は電荷 $+e$，有効質量 $m_{\mathrm{h}}$，緩和時間 $\tau_{\mathrm{h}}$ をもつ。$x$ 方向に一様な電場 $\mathcal{E}$ をかけたとき，電子と正孔の平均速度 $v_{\mathrm{e}},v_{\mathrm{h}}$ は

$$
\begin{aligned}
m_{\mathrm{e}}\frac{\mathrm{d}v_{\mathrm{e}}}{\mathrm{d}t}&=-e\mathcal{E}-\frac{m_{\mathrm{e}}}{\tau_{\mathrm{e}}}v_{\mathrm{e}}\\
m_{\mathrm{h}}\frac{\mathrm{d}v_{\mathrm{h}}}{\mathrm{d}t}&=e\mathcal{E}-\frac{m_{\mathrm{h}}}{\tau_{\mathrm{h}}}v_{\mathrm{h}}
\end{aligned}
$$

に従う。定常状態での速さを $|v_{\mathrm{e}}|=\mu_{\mathrm{e}}\mathcal{E}$，$|v_{\mathrm{h}}|=\mu_{\mathrm{h}}\mathcal{E}$ と書き，$\mu_{\mathrm{e}},\mu_{\mathrm{h}}$ を移動度とよぶ。電気伝導度 $\sigma$ は定常状態での $j=\sigma\mathcal{E}$ で定義する。以下の問いに答えよ。

(1) $\mu_{\mathrm{e}}$，$\mu_{\mathrm{h}}$ と $\sigma$ を求めよ。

(2) 真性半導体では $n=p=n_{\mathrm{i}}$ であり，$n_{\mathrm{i}}\propto T^{3/2}e^{-E_{\mathrm{g}}/2k_{\mathrm{B}}T}$ である。$E_{\mathrm{g}}$ はバンドギャップ，$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。移動度がどちらも $T^{-3/2}$ に比例するとき，$\ln\sigma$ を $1/T$ に対してプロットしたグラフの傾きを求めよ。

(3) 不純物を加えて $n$ を変えても，$np=n_{\mathrm{i}}^{\,2}$ は一定に保たれるとする。$\sigma$ を最小にする $n$ と，その最小値 $\sigma_{\min}$ を求めよ。また，真性半導体の伝導度 $\sigma_{\mathrm{i}}$ に対する比 $\sigma_{\min}/\sigma_{\mathrm{i}}$ を求めよ。

(4) 室温のケイ素で $n_{\mathrm{i}}=1.0\times10^{16}\ \mathrm{m^{-3}}$，$\mu_{\mathrm{e}}=0.14\ \mathrm{m^2/(V\,s)}$，$\mu_{\mathrm{h}}=0.045\ \mathrm{m^2/(V\,s)}$ とする。真性ケイ素の抵抗率 $\rho_{\mathrm{i}}$ と，密度 $N_{\mathrm{D}}=1.0\times10^{21}\ \mathrm{m^{-3}}$ のドナーがすべて電離したケイ素の抵抗率 $\rho$ を求めよ。$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

---

## 解答・解説

### (1)
定常状態では速度の時間微分が0になるので，運動方程式から速度が直接求まります。

$$
\begin{aligned}
v_{\mathrm{e}}&=-\frac{e\tau_{\mathrm{e}}}{m_{\mathrm{e}}}\mathcal{E}\\
v_{\mathrm{h}}&=\frac{e\tau_{\mathrm{h}}}{m_{\mathrm{h}}}\mathcal{E}
\end{aligned}
$$

電子は電場と逆向きに，正孔は電場の向きに動きます。電流密度は2つの寄与の和です。

$$
\begin{aligned}
j&=-env_{\mathrm{e}}+epv_{\mathrm{h}}\\
&=\left(\frac{ne^2\tau_{\mathrm{e}}}{m_{\mathrm{e}}}+\frac{pe^2\tau_{\mathrm{h}}}{m_{\mathrm{h}}}\right)\mathcal{E}
\end{aligned}
$$

これを読み取ると，

$$
\begin{aligned}
&\finalanswer{\mu_{\mathrm{e}}=\frac{e\tau_{\mathrm{e}}}{m_{\mathrm{e}}}}\\
&\finalanswer{\mu_{\mathrm{h}}=\frac{e\tau_{\mathrm{h}}}{m_{\mathrm{h}}}}\\
&\finalanswer{\sigma=e\left(n\mu_{\mathrm{e}}+p\mu_{\mathrm{h}}\right)}
\end{aligned}
$$

となります。電荷も速度も逆向きなので，電子と正孔は同じ向きの電流を運び，寄与は足し合わされます。

### (2)
$n=p=n_{\mathrm{i}}$ を (1) に代入すると $\sigma_{\mathrm{i}}=n_{\mathrm{i}}e(\mu_{\mathrm{e}}+\mu_{\mathrm{h}})$ です。$n_{\mathrm{i}}$ の $T^{3/2}$ と移動度の $T^{-3/2}$ が打ち消し合います。

$$
\sigma_{\mathrm{i}}\propto T^{3/2}e^{-E_{\mathrm{g}}/2k_{\mathrm{B}}T}\cdot T^{-3/2}=e^{-E_{\mathrm{g}}/2k_{\mathrm{B}}T}
$$

対数をとると $1/T$ の1次関数になるので，

$$
\finalanswer{\text{傾き}=-\frac{E_{\mathrm{g}}}{2k_{\mathrm{B}}}}
$$

となります。金属と違って，半導体の伝導度は温度とともに急激に増えます。

### (3)
$p=n_{\mathrm{i}}^{\,2}/n$ を代入すると，$\sigma$ は $n$ だけの関数になります。

$$
\sigma(n)=e\left(n\mu_{\mathrm{e}}+\frac{n_{\mathrm{i}}^{\,2}}{n}\mu_{\mathrm{h}}\right)
$$

$n$ で微分して0とおくと，$\mu_{\mathrm{e}}=n_{\mathrm{i}}^{\,2}\mu_{\mathrm{h}}/n^2$ です。これを解いて $\sigma$ に戻すと，

$$
\begin{aligned}
&\finalanswer{n=n_{\mathrm{i}}\sqrt{\frac{\mu_{\mathrm{h}}}{\mu_{\mathrm{e}}}}}\\
&\finalanswer{\sigma_{\min}=2en_{\mathrm{i}}\sqrt{\mu_{\mathrm{e}}\mu_{\mathrm{h}}}}\\
&\finalanswer{\frac{\sigma_{\min}}{\sigma_{\mathrm{i}}}=\frac{2\sqrt{\mu_{\mathrm{e}}\mu_{\mathrm{h}}}}{\mu_{\mathrm{e}}+\mu_{\mathrm{h}}}}
\end{aligned}
$$

となります。相加平均と相乗平均の関係からこの比は1以下で，等号は $\mu_{\mathrm{e}}=\mu_{\mathrm{h}}$ のときだけ成り立ちます。ふつうは $\mu_{\mathrm{e}}>\mu_{\mathrm{h}}$ なので，伝導度が最小になるのは真性半導体ではなく，わずかに p 型にした半導体です。

### (4)
真性ケイ素の抵抗率は $\sigma_{\mathrm{i}}$ の逆数です。

$$
\rho_{\mathrm{i}}=\frac{1}{1.602\times10^{-19}\times1.0\times10^{16}\times0.185}\ \Omega\,\mathrm{m}
$$

ドナーを加えた場合は $n=N_{\mathrm{D}}$ です。正孔の密度は $p=n_{\mathrm{i}}^{\,2}/N_{\mathrm{D}}=1.0\times10^{11}\ \mathrm{m^{-3}}$ で，無視できます。

$$
\rho=\frac{1}{1.602\times10^{-19}\times1.0\times10^{21}\times0.14}\ \Omega\,\mathrm{m}
$$

これらを計算すると，

$$
\begin{aligned}
&\finalanswer{\rho_{\mathrm{i}}\approx3.4\times10^{3}\ \Omega\,\mathrm{m}}\\
&\finalanswer{\rho\approx4.5\times10^{-2}\ \Omega\,\mathrm{m}}
\end{aligned}
$$

となります。原子1000万個に1個ほどのドナーを加えるだけで，抵抗率は約8万分の1になります。

===== FILE: 06solid_state/08/08_050.md =====
---
tags:
  - 発展
---

# pn 接合の空乏層

## 問題
$x<0$ にアクセプター密度 $N_{\mathrm{A}}$ の p 型半導体，$x>0$ にドナー密度 $N_{\mathrm{D}}$ の n 型半導体が接した階段型の pn 接合を考える。不純物はすべて電離しているとする。熱平衡では接合付近のキャリアが消えた空乏層ができる。空乏層を $-x_{\mathrm{p}}<x<x_{\mathrm{n}}$（$x_{\mathrm{p}},x_{\mathrm{n}}>0$）とし，その中では電荷密度が $-x_{\mathrm{p}}<x<0$ で $\rho=-eN_{\mathrm{A}}$，$0<x<x_{\mathrm{n}}$ で $\rho=+eN_{\mathrm{D}}$ であり，外側では $\rho=0$ で電場も0であるとする（図）。半導体の誘電率を $\varepsilon$，電位を $\phi(x)$，電場の $x$ 成分を $\mathcal{E}(x)=-\dfrac{\mathrm{d}\phi}{\mathrm{d}x}$ とし，空乏層の幅を $W=x_{\mathrm{p}}+x_{\mathrm{n}}$ とする。$e>0$ は素電荷である。以下の問いに答えよ。

<!-- FIGURE problem: 横軸 x，縦軸 電荷密度 ρ のグラフ。x = 0 に縦の破線を引き，左に「p 型」，右に「n 型」と書く。−x_p < x < 0 に高さ −eN_A の長方形（下向き）を，0 < x < x_n に高さ +eN_D の長方形（上向き）を描いて塗る。それ以外では ρ = 0。横軸に −x_p，0，x_n の目盛りを付ける。2つの長方形の面積が等しく見えるように，N_A > N_D として左の長方形を深く細く，右を浅く広く描く。電場や電位は描かない。 -->

(1) ガウスの法則 $\dfrac{\mathrm{d}\mathcal{E}}{\mathrm{d}x}=\dfrac{\rho}{\varepsilon}$ を用いて，空乏層の中の $\mathcal{E}(x)$ を求めよ。また，$x_{\mathrm{p}}$ と $x_{\mathrm{n}}$ の間に成り立つ関係式を求めよ。

(2) 内蔵電位 $V_{\mathrm{bi}}=\phi(x_{\mathrm{n}})-\phi(-x_{\mathrm{p}})$ を $W$ で表し，$W$ を $V_{\mathrm{bi}}$ で表せ。

(3) 熱平衡では化学ポテンシャル $\mu$ が場所によらず一定であり，伝導帯の底は $E_{\mathrm{c}}(x)=E_{\mathrm{c}}^{0}-e\phi(x)$ と曲がる。$E_{\mathrm{c}}^{0}$ は定数である。電子密度は $n(x)=N_{\mathrm{c}}e^{-[E_{\mathrm{c}}(x)-\mu]/k_{\mathrm{B}}T}$ と書ける。空乏層の外側の n 型領域では $n=N_{\mathrm{D}}$，p 型領域では $n=n_{\mathrm{i}}^{\,2}/N_{\mathrm{A}}$ である。$n_{\mathrm{i}}$ は真性キャリア密度，$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。$V_{\mathrm{bi}}$ を求めよ。

(4) p 側に対して n 側の電位を $V>0$ だけ高くする逆方向電圧をかける。空乏層の幅 $W(V)$ を求めよ。さらに，n 側の空乏層にある単位面積あたりの電荷 $Q$ を用いて，単位面積あたりの接合容量 $C=\dfrac{\mathrm{d}Q}{\mathrm{d}V}$ を求め，$1/C^2$ を $V$ の関数として表せ。

---

## 解答・解説

### (1)
各領域で電荷密度は一定なので，ガウスの法則を積分すると $\mathcal{E}$ は1次関数になります。積分定数は，空乏層の両端で電場が0になる条件で決めます。

$$
\finalanswer{\mathcal{E}(x)=
\begin{cases}
-\dfrac{eN_{\mathrm{A}}}{\varepsilon}(x+x_{\mathrm{p}}) & (-x_{\mathrm{p}}<x<0)\\[2mm]
\dfrac{eN_{\mathrm{D}}}{\varepsilon}(x-x_{\mathrm{n}}) & (0<x<x_{\mathrm{n}})
\end{cases}}
$$

境界 $x=0$ に面電荷はないので，電場は $x=0$ で連続です。2つの式の $x=0$ での値を等しいとおくと，

$$
\finalanswer{N_{\mathrm{A}}x_{\mathrm{p}}=N_{\mathrm{D}}x_{\mathrm{n}}}
$$

となります。これは空乏層全体が電気的に中性であることを表しています。空乏層の中で電場は負，すなわち n 側から p 側を向き，その大きさは接合面で最大になります。

### (2)
電位差は電場を積分して符号を変えたもので，(1) の三角形の面積に等しくなります。

$$
\begin{aligned}
V_{\mathrm{bi}}&=-\int_{-x_{\mathrm{p}}}^{x_{\mathrm{n}}}\mathcal{E}\,\mathrm{d}x\\
&=\frac{e}{2\varepsilon}\left(N_{\mathrm{A}}x_{\mathrm{p}}^{\,2}+N_{\mathrm{D}}x_{\mathrm{n}}^{\,2}\right)
\end{aligned}
$$

(1) の関係式と $W=x_{\mathrm{p}}+x_{\mathrm{n}}$ から，それぞれの幅は $W$ で表せます。

$$
\begin{aligned}
x_{\mathrm{p}}&=\frac{N_{\mathrm{D}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}W\\
x_{\mathrm{n}}&=\frac{N_{\mathrm{A}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}W
\end{aligned}
$$

これらを代入すると，括弧の中は $\dfrac{N_{\mathrm{A}}N_{\mathrm{D}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}W^2$ にまとまります。

$$
\begin{aligned}
&\finalanswer{V_{\mathrm{bi}}=\frac{eN_{\mathrm{A}}N_{\mathrm{D}}}{2\varepsilon(N_{\mathrm{A}}+N_{\mathrm{D}})}W^2}\\
&\finalanswer{W=\sqrt{\frac{2\varepsilon V_{\mathrm{bi}}}{e}\cdot\frac{N_{\mathrm{A}}+N_{\mathrm{D}}}{N_{\mathrm{A}}N_{\mathrm{D}}}}}
\end{aligned}
$$

となります。電場と電位を図に示します。

<!-- FIGURE solution (2): 上下2段のグラフ，共通の横軸 x（−x_p，0，x_n に目盛り）。上段は電場 𝓔(x)：−x_p で 0 から直線的に下がり，x = 0 で最も負になって，そこから直線的に戻り x_n で 0 になる逆三角形を実線で描く。三角形の内部を薄く塗り「面積 = V_bi」と注記する。下段は電位 φ(x)：x < −x_p で一定の低い値，−x_p から x_n にかけて S 字状に上がり，x > x_n で一定の高い値になる曲線を描く。両端の高さの差を矢印で示して V_bi とラベルする。 -->

### (3)
化学ポテンシャルが一定なので，電子密度は電位だけで決まり，$e^{e\phi(x)/k_{\mathrm{B}}T}$ に比例します。両側の空乏層の外での電子密度の比をとります。

$$
\frac{n(x_{\mathrm{n}})}{n(-x_{\mathrm{p}})}=e^{eV_{\mathrm{bi}}/k_{\mathrm{B}}T}=\frac{N_{\mathrm{D}}N_{\mathrm{A}}}{n_{\mathrm{i}}^{\,2}}
$$

対数をとると，

$$
\finalanswer{V_{\mathrm{bi}}=\frac{k_{\mathrm{B}}T}{e}\ln\frac{N_{\mathrm{A}}N_{\mathrm{D}}}{n_{\mathrm{i}}^{\,2}}}
$$

となります。n 側から p 側へ拡散しようとする電子を，内蔵電場が押し戻して釣り合っています。

### (4)
逆方向電圧をかけると，両側の電位差は $V_{\mathrm{bi}}+V$ になります。(2) の式の $V_{\mathrm{bi}}$ を置き換えると，

$$
\finalanswer{W(V)=\sqrt{\frac{2\varepsilon(V_{\mathrm{bi}}+V)}{e}\cdot\frac{N_{\mathrm{A}}+N_{\mathrm{D}}}{N_{\mathrm{A}}N_{\mathrm{D}}}}}
$$

となります。n 側の電荷は $Q=eN_{\mathrm{D}}x_{\mathrm{n}}$ で，(2) の $x_{\mathrm{n}}$ を使って $W$ で書き，$V$ で微分します。

$$
\begin{aligned}
Q&=\frac{eN_{\mathrm{A}}N_{\mathrm{D}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}W\\
\frac{\mathrm{d}W}{\mathrm{d}V}&=\frac{\varepsilon(N_{\mathrm{A}}+N_{\mathrm{D}})}{eN_{\mathrm{A}}N_{\mathrm{D}}W}
\end{aligned}
$$

2つをかけると $C=\varepsilon/W$ となり，これを2乗して逆数をとると，

$$
\begin{aligned}
&\finalanswer{C=\frac{\varepsilon}{W(V)}}\\
&\finalanswer{\frac{1}{C^2}=\frac{2(N_{\mathrm{A}}+N_{\mathrm{D}})}{e\varepsilon N_{\mathrm{A}}N_{\mathrm{D}}}(V_{\mathrm{bi}}+V)}
\end{aligned}
$$

となります。空乏層は間隔 $W$ の平行板コンデンサーのように振る舞います。$1/C^2$ を $V$ に対してプロットすると直線になり，横軸との交点 $V=-V_{\mathrm{bi}}$ から内蔵電位が，傾きから不純物密度が求まります。

===== FILE: 06solid_state/08/08_060.md =====
---
tags:
  - 標準
---

# 光吸収と直接・間接遷移

## 問題
格子定数 $a$ の半導体で，価電子帯の頂上を $\boldsymbol{k}=\boldsymbol{0}$，エネルギーの原点にとり，価電子帯の電子のエネルギーを $E_{\mathrm{v}}(\boldsymbol{k})=-\dfrac{\hbar^2k^2}{2m_{\mathrm{h}}}$ とする。$m_{\mathrm{h}}>0$ は正孔の有効質量である。角振動数 $\omega$ の光子を吸収して，価電子帯の電子が伝導帯に移る過程を考える。光子の波数は $\omega/c$ とする。$c$ は光速である。以下の問いに答えよ。

(1) 光子のエネルギー $\hbar\omega$ がバンドギャップ $E_{\mathrm{g}}$ に等しいとき，光子の波数とブリルアンゾーンの大きさ $\pi/a$ の比を，$E_{\mathrm{g}}$，$a$，$\hbar c$ で表せ。また，ケイ素の値 $E_{\mathrm{g}}=1.1\ \mathrm{eV}$，$a=0.54\ \mathrm{nm}$ と $\hbar c=197\ \mathrm{eV\,nm}$ を用いて，この比を求めよ。

(2) 伝導帯の底も $\boldsymbol{k}=\boldsymbol{0}$ にあり，$E_{\mathrm{c}}(\boldsymbol{k})=E_{\mathrm{g}}+\dfrac{\hbar^2k^2}{2m_{\mathrm{e}}}$ とする（直接遷移型）。$m_{\mathrm{e}}>0$ は電子の有効質量である。光子の波数を無視し，結晶運動量の保存を用いて，$\hbar\omega$ の光で励起される電子の波数 $k$ を求めよ。さらに，遷移の結合状態密度 $J(\hbar\omega)$ を，単位体積あたり，スピンを含めて，$J(\hbar\omega)=2\displaystyle\int\frac{\mathrm{d}^3k}{(2\pi)^3}\delta\bigl(\hbar\omega-E_{\mathrm{c}}(\boldsymbol{k})+E_{\mathrm{v}}(\boldsymbol{k})\bigr)$ で定義する。$J(\hbar\omega)$ を求め，吸収係数 $\alpha$ が $J$ に比例するとき，$\hbar\omega>E_{\mathrm{g}}$ での $\alpha$ の $\hbar\omega$ 依存性を求めよ。

(3) 次に，伝導帯の底が $\boldsymbol{k}_0$（$|\boldsymbol{k}_0|$ は $\pi/a$ と同程度）にあり，$E_{\mathrm{c}}(\boldsymbol{k})=E_{\mathrm{g}}+\dfrac{\hbar^2|\boldsymbol{k}-\boldsymbol{k}_0|^2}{2m_{\mathrm{e}}}$ とする（間接遷移型）。遷移にはフォノン1個の吸収または放出がともなう。フォノンのエネルギーは波数によらず $\hbar\Omega$ とする。価電子帯の頂上から伝導帯の底へ移る遷移で必要なフォノンの波数ベクトルを求めよ。また，フォノンを吸収する過程と放出する過程のそれぞれについて，吸収が始まる光子のエネルギーを求めよ。

(4) (3) の間接遷移で，価電子帯のどの状態から伝導帯のどの状態への遷移も，適当なフォノンを使って起こり，その確率は状態によらないとする。このとき吸収係数は

$$
\alpha\propto\int_0^\infty\!\mathrm{d}\varepsilon_1\int_0^\infty\!\mathrm{d}\varepsilon_2\,\sqrt{\varepsilon_1}\sqrt{\varepsilon_2}\;\delta\bigl(\hbar\omega\pm\hbar\Omega-E_{\mathrm{g}}-\varepsilon_1-\varepsilon_2\bigr)
$$

で与えられる。$\varepsilon_1$ は価電子帯の頂上から測った正孔のエネルギー，$\varepsilon_2$ は伝導帯の底から測った電子のエネルギーで，複号はフォノンの吸収が $+$，放出が $-$ である。$\alpha$ の $\hbar\omega$ 依存性を求めよ。また，$\sqrt{\alpha}$ を $\hbar\omega$ に対してプロットしたとき，2つの過程の直線が横軸と交わるエネルギーを $E_1<E_2$ とする。$E_{\mathrm{g}}$ と $\hbar\Omega$ を $E_1,E_2$ で表せ。必要なら $\displaystyle\int_0^1\sqrt{u(1-u)}\,\mathrm{d}u=\frac{\pi}{8}$ を用いてよい。

---

## 解答・解説

### (1)
光子の波数は $\omega/c=E_{\mathrm{g}}/\hbar c$ です。これを $\pi/a$ で割ると，

$$
\finalanswer{\frac{E_{\mathrm{g}}/\hbar c}{\pi/a}=\frac{E_{\mathrm{g}}a}{\pi\hbar c}}
$$

となります。ケイ素の値を代入します。

$$
\frac{E_{\mathrm{g}}a}{\pi\hbar c}=\frac{1.1\times0.54}{\pi\times197}
$$

これを計算すると，

$$
\finalanswer{\frac{E_{\mathrm{g}}a}{\pi\hbar c}\approx9.6\times10^{-4}}
$$

となります。光子の波数はブリルアンゾーンの大きさの1000分の1程度しかありません。そのため，光の吸収で電子の波数はほとんど変わらず，バンド図の上で遷移は縦向きになります。

### (2)
光子の波数を無視すると，結晶運動量の保存から，電子は同じ $\boldsymbol{k}$ のまま伝導帯に移ります。エネルギー保存の式を書き，換算質量 $m_{\mathrm{r}}$ を $\dfrac{1}{m_{\mathrm{r}}}=\dfrac{1}{m_{\mathrm{e}}}+\dfrac{1}{m_{\mathrm{h}}}$ で定義します。

$$
\hbar\omega=E_{\mathrm{g}}+\frac{\hbar^2k^2}{2m_{\mathrm{e}}}+\frac{\hbar^2k^2}{2m_{\mathrm{h}}}=E_{\mathrm{g}}+\frac{\hbar^2k^2}{2m_{\mathrm{r}}}
$$

これを $k$ について解くと，

$$
\finalanswer{k=\frac{\sqrt{2m_{\mathrm{r}}(\hbar\omega-E_{\mathrm{g}})}}{\hbar}}
$$

となります。結合状態密度は，自由電子の状態密度の計算で質量を $m_{\mathrm{r}}$ に，エネルギーを $\hbar\omega-E_{\mathrm{g}}$ に置き換えたものです。

$$
\begin{aligned}
J(\hbar\omega)&=\frac{1}{\pi^2}\int_0^\infty k^2\,\delta\!\left(\hbar\omega-E_{\mathrm{g}}-\frac{\hbar^2k^2}{2m_{\mathrm{r}}}\right)\mathrm{d}k\\
&=\frac{1}{2\pi^2}\left(\frac{2m_{\mathrm{r}}}{\hbar^2}\right)^{3/2}\sqrt{\hbar\omega-E_{\mathrm{g}}}
\end{aligned}
$$

これに比例するので，

$$
\begin{aligned}
&\finalanswer{J(\hbar\omega)=\frac{1}{2\pi^2}\left(\frac{2m_{\mathrm{r}}}{\hbar^2}\right)^{3/2}\sqrt{\hbar\omega-E_{\mathrm{g}}}}\\
&\finalanswer{\alpha\propto(\hbar\omega-E_{\mathrm{g}})^{1/2}}
\end{aligned}
$$

となります。

### (3)
光子の運動量は無視できるので，電子の波数の変化はすべてフォノンが受け持ちます。頂上 $\boldsymbol{0}$ から底 $\boldsymbol{k}_0$ への遷移では，フォノンを吸収するならその波数が $\boldsymbol{k}_0$，放出するなら $-\boldsymbol{k}_0$ です。逆格子ベクトルの差は除きます。

$$
\finalanswer{\boldsymbol{q}=\pm\boldsymbol{k}_0}
$$

エネルギー保存は，吸収なら $\hbar\omega+\hbar\Omega=E_{\mathrm{c}}-E_{\mathrm{v}}$，放出なら $\hbar\omega=E_{\mathrm{c}}-E_{\mathrm{v}}+\hbar\Omega$ です。$E_{\mathrm{c}}-E_{\mathrm{v}}$ の最小値は $E_{\mathrm{g}}$ なので，

$$
\begin{aligned}
&\finalanswer{\text{フォノン吸収}:\ \hbar\omega=E_{\mathrm{g}}-\hbar\Omega}\\
&\finalanswer{\text{フォノン放出}:\ \hbar\omega=E_{\mathrm{g}}+\hbar\Omega}
\end{aligned}
$$

となります。遷移の様子を図に示します。

<!-- FIGURE solution (3): 横軸 k，縦軸 E のバンド図。k = 0 に頂上をもつ下に凸でない（上に凸の）放物線を価電子帯として描き，その頂上を E = 0 とする。k = k0（右側，ゾーン境界に近い位置）に底をもつ下に凸の放物線を伝導帯として描き，底の高さを E_g とする。価電子帯の頂上から真上に短い波線矢印（光子 ħω）を描き，その先端から右へ水平な矢印（フォノン q = k0）を描いて伝導帯の底に届かせる。縦の破線で k = 0 と k = k0 の位置を示す。 -->

### (4)
デルタ関数で $\varepsilon_2$ の積分を実行すると，$\varepsilon_1$ の積分が残ります。$\epsilon=\hbar\omega\pm\hbar\Omega-E_{\mathrm{g}}>0$ とおき，$\varepsilon_1=\epsilon u$ と置き換えます。

$$
\begin{aligned}
\alpha&\propto\int_0^{\epsilon}\sqrt{\varepsilon_1(\epsilon-\varepsilon_1)}\,\mathrm{d}\varepsilon_1\\
&=\epsilon^2\int_0^1\sqrt{u(1-u)}\,\mathrm{d}u=\frac{\pi}{8}\epsilon^2
\end{aligned}
$$

したがって，

$$
\finalanswer{\alpha\propto(\hbar\omega-E_{\mathrm{g}}\pm\hbar\Omega)^2}
$$

となります。$\sqrt{\alpha}$ は $\hbar\omega$ の1次関数で，横軸との交点は (3) で求めた吸収の始まるエネルギーです。$E_1=E_{\mathrm{g}}-\hbar\Omega$，$E_2=E_{\mathrm{g}}+\hbar\Omega$ を解くと，

$$
\begin{aligned}
&\finalanswer{E_{\mathrm{g}}=\frac{E_1+E_2}{2}}\\
&\finalanswer{\hbar\Omega=\frac{E_2-E_1}{2}}
\end{aligned}
$$

となります。直接遷移の $1/2$ 乗に対して間接遷移は2乗で立ち上がるので，吸収端の形から遷移の種類を見分けられます。フォノンを吸収する過程はフォノンが熱的に励起されていないと起こらないので，低温では $E_1$ からの吸収が弱くなります。

===== FILE: 06solid_state/09/09_010.md =====
---
tags:
  - 標準
---

# ローレンツ模型と誘電関数

## 問題
絶縁体の結晶で，単位体積あたり $N$ 個の電子が，それぞれ平衡位置のまわりに調和的に束縛されているとする。電子の電荷を $-e$（$e>0$），質量を $m$ とし，$x$ 方向の一様な電場 $\mathcal{E}(t)=\mathrm{Re}\left[\mathcal{E}_0e^{-i\omega t}\right]$（$\omega>0$）をかけたときの変位 $x$ は

$$
m\ddot{x}=-m\omega_0^{\,2}x-m\gamma\dot{x}-e\mathcal{E}
$$

に従うとする。$\omega_0>0$ は共鳴角振動数，$\gamma>0$ は減衰率である。局所電場の補正とイオンの変位は無視する。複素数表示で $x,\mathcal{E}\propto e^{-i\omega t}$ とし，分極を $P=-Nex$，比誘電関数を $\varepsilon_{\mathrm{r}}(\omega)=1+\dfrac{P}{\varepsilon_0\mathcal{E}}$ で定義する。$\varepsilon_0$ は真空の誘電率である。$\omega_{\mathrm{p}}^{\,2}=\dfrac{Ne^2}{\varepsilon_0m}$ とおく。以下の問いに答えよ。

(1) 定常状態での $x$ の複素振幅を求め，$\varepsilon_{\mathrm{r}}(\omega)$ を $\omega_0,\gamma,\omega_{\mathrm{p}}$ で表せ。

(2) $\varepsilon_{\mathrm{r}}=\varepsilon'+i\varepsilon''$ と書いたときの実部 $\varepsilon'$ と虚部 $\varepsilon''$ を求めよ。また，静的な比誘電率 $\varepsilon_{\mathrm{r}}(0)$ を求めよ。

(3) 電場が単位体積あたりに1周期の平均でする仕事率 $\langle j\mathcal{E}\rangle$ が，$\dfrac{1}{2}\varepsilon_0\omega\varepsilon''|\mathcal{E}_0|^2$ となることを示せ。$j=\dfrac{\mathrm{d}P}{\mathrm{d}t}$ は分極電流の密度である。

(4) $\gamma\ll\omega_0$ のとき，$\omega$ が $\omega_0$ に近い範囲で $\varepsilon''$ を近似し，$\varepsilon''$ のピークの高さ，半値全幅，および面積 $\displaystyle\int_0^\infty\varepsilon''\,\mathrm{d}\omega$ を求めよ。

---

## 解答・解説

### (1)
$x\propto e^{-i\omega t}$ なので，時間微分は $-i\omega$ をかけることに置き換わります。運動方程式は代数方程式になります。

$$
m(-\omega^2+\omega_0^{\,2}-i\gamma\omega)x=-e\mathcal{E}
$$

これを $x$ について解き，$P=-Nex$ を比誘電関数の定義に代入すると，

$$
\begin{aligned}
&\finalanswer{x=-\frac{e}{m}\cdot\frac{\mathcal{E}_0}{\omega_0^{\,2}-\omega^2-i\gamma\omega}}\\
&\finalanswer{\varepsilon_{\mathrm{r}}(\omega)=1+\frac{\omega_{\mathrm{p}}^{\,2}}{\omega_0^{\,2}-\omega^2-i\gamma\omega}}
\end{aligned}
$$

となります。

### (2)
分母の複素共役を分子と分母にかけて，実部と虚部に分けます。

$$
\begin{aligned}
&\finalanswer{\varepsilon'=1+\frac{\omega_{\mathrm{p}}^{\,2}(\omega_0^{\,2}-\omega^2)}{(\omega_0^{\,2}-\omega^2)^2+\gamma^2\omega^2}}\\
&\finalanswer{\varepsilon''=\frac{\omega_{\mathrm{p}}^{\,2}\gamma\omega}{(\omega_0^{\,2}-\omega^2)^2+\gamma^2\omega^2}}
\end{aligned}
$$

$\omega\to0$ では虚部が消えます。

$$
\finalanswer{\varepsilon_{\mathrm{r}}(0)=1+\frac{\omega_{\mathrm{p}}^{\,2}}{\omega_0^{\,2}}}
$$

となります。$\varepsilon'$ は $\omega_0$ の下で大きくなり，$\omega_0$ の少し上では1より小さくなります。$\varepsilon''$ は $\omega>0$ で常に正で，$\omega_0$ の付近で大きくなります。2つの関数を図に示します。

<!-- FIGURE solution (2): 横軸 ω（0 から 2ω0），縦軸 ε。ε'（実線）は ω = 0 で 1 + ω_p²/ω0² から始まり，ω0 の手前で極大，ω0 で 1 を横切り，ω0 の少し上で極小（1 より小さく，負になってもよい）をとってから 1 に近づく。ε''（破線）は ω0 に鋭いピークをもつ山。縦軸 1 の位置に水平な点線を引き，横軸に ω0 の目盛りを付ける。ピークの半分の高さに幅 γ を示す両矢印を描く。 -->

### (3)
実数の量の積の時間平均は，複素振幅を使って $\dfrac{1}{2}\mathrm{Re}(j\mathcal{E}_0^{\,*})$ で計算できます。電流の複素振幅は $j=-i\omega P=-i\omega\varepsilon_0(\varepsilon_{\mathrm{r}}-1)\mathcal{E}_0$ です。

$$
\begin{aligned}
\langle j\mathcal{E}\rangle&=\frac{1}{2}\mathrm{Re}\left[-i\omega\varepsilon_0(\varepsilon'-1+i\varepsilon'')\right]|\mathcal{E}_0|^2\\
&=\frac{1}{2}\varepsilon_0\omega\varepsilon''|\mathcal{E}_0|^2
\end{aligned}
$$

より，

$$
\finalanswer{\langle j\mathcal{E}\rangle=\frac{1}{2}\varepsilon_0\omega\varepsilon''|\mathcal{E}_0|^2}
$$

となります。$\varepsilon''$ は媒質がエネルギーを吸収する割合を表し，$\varepsilon''>0$ なので電場は常に正の仕事をします。

### (4)
$\omega\approx\omega_0$ では $\omega_0^{\,2}-\omega^2\approx2\omega_0(\omega_0-\omega)$ と近似でき，分子の $\omega$ を $\omega_0$ に置き換えられます。

$$
\varepsilon''\approx\frac{\omega_{\mathrm{p}}^{\,2}\gamma/\omega_0}{4(\omega-\omega_0)^2+\gamma^2}
$$

これはローレンツ型の関数です。ピークの高さは $\omega=\omega_0$ の値で，半分になるのは $|\omega-\omega_0|=\gamma/2$ のときです。面積は $\displaystyle\int_{-\infty}^{\infty}\frac{\mathrm{d}y}{4y^2+\gamma^2}=\frac{\pi}{2\gamma}$ を使って求めます。

$$
\begin{aligned}
&\finalanswer{\varepsilon''_{\max}=\frac{\omega_{\mathrm{p}}^{\,2}}{\gamma\omega_0}}\\
&\finalanswer{\text{半値全幅}=\gamma}\\
&\finalanswer{\int_0^\infty\varepsilon''\,\mathrm{d}\omega\approx\frac{\pi\omega_{\mathrm{p}}^{\,2}}{2\omega_0}}
\end{aligned}
$$

となります。減衰率を小さくするとピークは高く細くなりますが，面積は $\gamma$ によりません。$\gamma\to0$ の極限で $\varepsilon''$ はデルタ関数になり，吸収は共鳴の振動数だけで起こります。

===== FILE: 06solid_state/09/09_020.md =====
---
tags:
  - 標準
---

# 局所電場とクラウジウス・モソッティの式

## 問題
同種の中性原子が立方格子に並んだ結晶を考える。原子の数密度を $N$ とし，各原子はその位置での局所電場 $\mathcal{E}_{\mathrm{loc}}$ に比例する双極子モーメント $p=\alpha\mathcal{E}_{\mathrm{loc}}$ をもつ。$\alpha>0$ は分極率である。結晶内の巨視的な電場 $\mathcal{E}$ と分極 $P$ は一様で，どちらも $z$ 方向を向いている。真空の誘電率を $\varepsilon_0$，比誘電率を $\varepsilon_{\mathrm{r}}=1+\dfrac{P}{\varepsilon_0\mathcal{E}}$ とする。

局所電場は次のように求める。着目する原子を中心とする球を考え，球の外は分極 $P$ の連続な媒質とみなし，球の中の原子は個別の双極子として扱う。球の中にある他の原子の双極子が中心につくる電場は，立方格子の対称性から0になることを用いてよい。以下の問いに答えよ。

(1) 分極 $P$ の一様な媒質に半径 $R$ の球形の空洞があるとき，空洞の表面に現れる分極電荷の面密度を求め，それが空洞の中心につくる電場を求めよ。また，局所電場 $\mathcal{E}_{\mathrm{loc}}$ を $\mathcal{E}$ と $P$ で表せ。

(2) $\varepsilon_{\mathrm{r}}$ と $N\alpha$ の間に成り立つ関係式を求めよ。

(3) $y=\dfrac{N\alpha}{3\varepsilon_0}$ とおき，$\varepsilon_{\mathrm{r}}$ を $y$ で表せ。$\varepsilon_{\mathrm{r}}$ が発散する $y$ の値を求めよ。また，$y\ll1$ のとき $\varepsilon_{\mathrm{r}}$ を $y^2$ の項まで展開せよ。

(4) 各原子の分極が，質量 $m$，電荷 $-e$ の電子1個が角振動数 $\omega_0$ の調和振動子として束縛されていることによるとする。減衰は無視する。角振動数 $\omega$ の電場に対する分極率 $\alpha(\omega)$ を求め，$\varepsilon_{\mathrm{r}}(\omega)$ が発散する角振動数を求めよ。$\omega_{\mathrm{p}}^{\,2}=\dfrac{Ne^2}{\varepsilon_0m}$ とおく。

---

## 解答・解説

### (1)
分極電荷の面密度は $\boldsymbol{P}\cdot\boldsymbol{n}$ です。$\boldsymbol{n}$ は媒質の外向きの法線で，空洞の表面では空洞の中心を向きます。空洞の中心から見た方向と $z$ 軸のなす角を $\theta$ とすると，

$$
\finalanswer{\sigma=-P\cos\theta}
$$

となります。面要素の電荷が中心につくる電場の $z$ 成分は，正の電荷なら $-\cos\theta$ の向きをもちます。これを球面全体で積分します。

$$
\begin{aligned}
\mathcal{E}_{\mathrm{s}}&=\int\frac{\sigma(-\cos\theta)}{4\pi\varepsilon_0R^2}R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi\\
&=\frac{P}{4\pi\varepsilon_0}\cdot2\pi\int_0^\pi\cos^2\theta\sin\theta\,\mathrm{d}\theta\\
&=\frac{P}{3\varepsilon_0}
\end{aligned}
$$

空洞の中心の電場は，巨視的な電場にこの電場を加えたものです。球の中の双極子の寄与は0なので，

$$
\begin{aligned}
&\finalanswer{\mathcal{E}_{\mathrm{s}}=\frac{P}{3\varepsilon_0}}\\
&\finalanswer{\mathcal{E}_{\mathrm{loc}}=\mathcal{E}+\frac{P}{3\varepsilon_0}}
\end{aligned}
$$

となります。空洞の表面の電荷の配置を図に示します。

<!-- FIGURE solution (1): 一様に分極した媒質（上向きの矢印 P を数本描いて示す）の中に円形の空洞を描く。空洞の円周上，上側に負の電荷（−）を，下側に正の電荷（+）を，極で多く赤道付近で少なくなるように並べる。空洞の中心 O から z 軸と角 θ をなす半径を1本描き，その端の面要素に σ = −P cos θ とラベルする。中心 O に上向きの矢印を描いて「P/3ε0」と注記する。 -->

### (2)
分極は双極子モーメントの密度なので $P=N\alpha\mathcal{E}_{\mathrm{loc}}$ です。(1) の局所電場を代入して $P$ について解きます。

$$
P=\frac{N\alpha}{1-N\alpha/3\varepsilon_0}\mathcal{E}
$$

これを比誘電率の定義に入れると $\varepsilon_{\mathrm{r}}-1=\dfrac{3y}{1-y}$ となります。ここで $y=N\alpha/3\varepsilon_0$ です。同じく $\varepsilon_{\mathrm{r}}+2=\dfrac{3}{1-y}$ なので，比をとると，

$$
\finalanswer{\frac{\varepsilon_{\mathrm{r}}-1}{\varepsilon_{\mathrm{r}}+2}=\frac{N\alpha}{3\varepsilon_0}}
$$

となります。これがクラウジウス・モソッティの式で，巨視的な誘電率と原子の分極率を結びつけます。

### (3)
(2) の関係式を $\varepsilon_{\mathrm{r}}$ について解くと，

$$
\finalanswer{\varepsilon_{\mathrm{r}}=\frac{1+2y}{1-y}}
$$

となります。分母が0になるとき発散するので，

$$
\finalanswer{y=1}
$$

です。$y\ll1$ では $\dfrac{1}{1-y}=1+y+y^2+\cdots$ を使って展開します。

$$
\finalanswer{\varepsilon_{\mathrm{r}}\approx1+3y+3y^2}
$$

となります。局所電場の補正を無視すると $\varepsilon_{\mathrm{r}}=1+3y$ なので，補正は $y^2$ の項から現れます。$y\to1$ では，周りの双極子がつくる電場が分極を強め合い，外部の電場がなくても分極が保たれる状態に近づきます。これは強誘電体の転移の単純な模型です。

### (4)
電子の運動方程式は $m\ddot{x}=-m\omega_0^{\,2}x-e\mathcal{E}_{\mathrm{loc}}$ です。$x\propto e^{-i\omega t}$ として解き，$p=-ex$ から分極率を読み取ります。

$$
\finalanswer{\alpha(\omega)=\frac{e^2}{m(\omega_0^{\,2}-\omega^2)}}
$$

これを (3) の $y$ に代入すると $y=\dfrac{\omega_{\mathrm{p}}^{\,2}}{3(\omega_0^{\,2}-\omega^2)}$ です。$\varepsilon_{\mathrm{r}}-1=\dfrac{3y}{1-y}$ を整理します。

$$
\varepsilon_{\mathrm{r}}(\omega)=1+\frac{\omega_{\mathrm{p}}^{\,2}}{\omega_0^{\,2}-\omega_{\mathrm{p}}^{\,2}/3-\omega^2}
$$

分母が0になる角振動数は，

$$
\finalanswer{\omega=\sqrt{\omega_0^{\,2}-\frac{\omega_{\mathrm{p}}^{\,2}}{3}}}
$$

となります。周りの双極子からの電場が復元力を弱めるため，結晶中の共鳴は孤立した原子の $\omega_0$ より低い振動数に移ります。

===== FILE: 06solid_state/09/09_030.md =====
---
tags:
  - 標準
---

# プラズマ振動

## 問題
金属の伝導電子を，数密度 $n_0$，電荷 $-e$（$e>0$），質量 $m$ の電子気体とみなす。イオンは動かない一様な正電荷の背景として扱い，その電荷密度は $+en_0$ とする。散乱は無視する。真空の誘電率を $\varepsilon_0$ とし，$\omega_{\mathrm{p}}^{\,2}=\dfrac{n_0e^2}{\varepsilon_0m}$ とおく。以下の問いに答えよ。

(1) 厚さ $d$ の無限に広い板状の領域にある電子が，すべて板に垂直な $x$ 方向に $u$ だけ変位したとする（図）。$|u|\ll d$ とする。板の両面に現れる電荷の面密度と，板の内部の電場を求めよ。また，電子の運動方程式を書き，振動の角振動数を求めよ。

(2) 電子の密度と速度を $n=n_0+\delta n(\boldsymbol{r},t)$，$\boldsymbol{v}(\boldsymbol{r},t)$ とし，連続の式 $\dfrac{\partial n}{\partial t}+\nabla\cdot(n\boldsymbol{v})=0$，運動方程式 $m\dfrac{\partial\boldsymbol{v}}{\partial t}=-e\boldsymbol{\mathcal{E}}$，ガウスの法則 $\nabla\cdot\boldsymbol{\mathcal{E}}=-\dfrac{e\,\delta n}{\varepsilon_0}$ を，$\delta n$ と $\boldsymbol{v}$ の1次まで考える。$\delta n$ が満たす方程式を導け。

(3) 角振動数 $\omega$ の一様な交流電場に対する，この電子気体の比誘電関数 $\varepsilon_{\mathrm{r}}(\omega)$ を求めよ。電束密度 $\boldsymbol{D}=\varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{\mathcal{E}}$ について外部の電荷がなく $\nabla\cdot\boldsymbol{D}=0$ が成り立つとき，電場が波数ベクトルと平行な縦波 $\boldsymbol{\mathcal{E}}\propto\boldsymbol{e}_xe^{i(kx-\omega t)}$（$k\ne0$）が存在する条件を求めよ。また，アルミニウムの伝導電子密度 $n_0=1.81\times10^{29}\ \mathrm{m^{-3}}$ を用いて $\hbar\omega_{\mathrm{p}}$ を eV 単位で求めよ。$e=1.602\times10^{-19}\ \mathrm{C}$，$m=9.109\times10^{-31}\ \mathrm{kg}$，$\varepsilon_0=8.854\times10^{-12}\ \mathrm{F/m}$，$\hbar=1.055\times10^{-34}\ \mathrm{J\,s}$ とする。

(4) 電子気体の圧力 $p$ を考え，(2) の運動方程式を $m\dfrac{\partial\boldsymbol{v}}{\partial t}=-e\boldsymbol{\mathcal{E}}-\dfrac{1}{n_0}\nabla p$ に置き換える。絶対零度の自由電子気体では $p=\dfrac{2}{5}nE_{\mathrm{F}}$ で，フェルミエネルギー $E_{\mathrm{F}}$ は $n^{2/3}$ に比例する。密度の変化が $\delta n\propto e^{i(kx-\omega t)}$ の形のとき，$\omega$ と $k$ の関係をフェルミ速度 $v_{\mathrm{F}}=\sqrt{2E_{\mathrm{F}}/m}$ を用いて表せ。

<!-- FIGURE problem: 縦長の帯（板の断面）を描き，左端を x = 0，右端を x = d として幅に寸法線 d を付ける。帯の内部を薄い灰色で塗り「正電荷の背景 +en0」と注記する。電子の分布を表す帯を同じ幅で破線で描き，右へ u だけずらす。ずれを矢印で u と示す。左端の細い領域（幅 u）と右端からはみ出した細い領域（幅 u）を強調して描く。x 軸の矢印を下に描く。電荷の符号や電場の向きは描かない。 -->

---

## 解答・解説

### (1)
電子が $+x$ 方向に $u$ ずれると，板の左端の幅 $u$ の部分では電子がいなくなって正の背景が残ります。右端では幅 $u$ の部分に電子があふれ出します。これらの電荷は面電荷とみなせます。

$$
\begin{aligned}
&\finalanswer{\text{左の面}:\ +en_0u}\\
&\finalanswer{\text{右の面}:\ -en_0u}
\end{aligned}
$$

逆符号の2枚の面電荷がつくる電場は，平行板コンデンサーと同じく内部だけにあり，正の面から負の面へ向かいます。

$$
\finalanswer{\mathcal{E}_x=\frac{en_0u}{\varepsilon_0}}
$$

電子には $-e\mathcal{E}_x$ の力がはたらき，これは変位を戻す向きです。

$$
m\ddot{u}=-\frac{n_0e^2}{\varepsilon_0}u
$$

これは単振動の方程式なので，

$$
\finalanswer{\omega=\omega_{\mathrm{p}}=\sqrt{\frac{n_0e^2}{\varepsilon_0m}}}
$$

となります。この振動数は板の厚さにもずれの大きさにもよりません。

### (2)
連続の式を1次まで残すと $\dfrac{\partial\,\delta n}{\partial t}+n_0\nabla\cdot\boldsymbol{v}=0$ です。これを時間で微分し，運動方程式とガウスの法則を順に代入します。

$$
\begin{aligned}
\frac{\partial^2\delta n}{\partial t^2}&=-n_0\nabla\cdot\frac{\partial\boldsymbol{v}}{\partial t}\\
&=\frac{n_0e}{m}\nabla\cdot\boldsymbol{\mathcal{E}}\\
&=-\frac{n_0e^2}{\varepsilon_0m}\delta n
\end{aligned}
$$

したがって，

$$
\finalanswer{\frac{\partial^2\delta n}{\partial t^2}=-\omega_{\mathrm{p}}^{\,2}\,\delta n}
$$

となります。密度の変化は空間のどんな形でも同じ角振動数 $\omega_{\mathrm{p}}$ で振動し，この模型では振動数が波数によりません。この集団振動をプラズマ振動とよびます。

### (3)
一様な電場のもとで電子の変位は $x=\dfrac{e\mathcal{E}}{m\omega^2}$ です。分極は $P=-n_0ex$ なので，

$$
\finalanswer{\varepsilon_{\mathrm{r}}(\omega)=1-\frac{\omega_{\mathrm{p}}^{\,2}}{\omega^2}}
$$

となります。縦波では $\nabla\cdot\boldsymbol{D}=ik\varepsilon_0\varepsilon_{\mathrm{r}}\mathcal{E}_x$ です。$k\ne0$，$\mathcal{E}_x\ne0$ でこれが0になるには $\varepsilon_{\mathrm{r}}=0$ が必要です。

$$
\finalanswer{\varepsilon_{\mathrm{r}}(\omega)=0,\ \text{すなわち}\ \omega=\omega_{\mathrm{p}}}
$$

となり，(2) の結果と一致します。アルミニウムの値を代入します。

$$
\begin{aligned}
\omega_{\mathrm{p}}^{\,2}&=\frac{1.81\times10^{29}\times(1.602\times10^{-19})^2}{8.854\times10^{-12}\times9.109\times10^{-31}}\ \mathrm{s^{-2}}\\
&=5.76\times10^{32}\ \mathrm{s^{-2}}
\end{aligned}
$$

$\omega_{\mathrm{p}}=2.40\times10^{16}\ \mathrm{s^{-1}}$ に $\hbar$ をかけて eV に直すと，

$$
\finalanswer{\hbar\omega_{\mathrm{p}}\approx15.8\ \mathrm{eV}}
$$

となります。高速の電子がアルミニウムの薄膜を通り抜けるとき，約 15 eV の整数倍のエネルギーを失うことが観測されており，プラズマ振動の量子が励起されていることがわかります。

### (4)
$E_{\mathrm{F}}\propto n^{2/3}$ なので $p\propto n^{5/3}$ です。圧力の変化は密度の変化に比例します。

$$
\delta p=\frac{\mathrm{d}p}{\mathrm{d}n}\delta n=\frac{5}{3}\cdot\frac{p}{n}\delta n=\frac{2}{3}E_{\mathrm{F}}\,\delta n
$$

(2) と同じ手順で，運動方程式の発散に圧力の項が加わります。

$$
\begin{aligned}
\frac{\partial^2\delta n}{\partial t^2}&=\frac{n_0e}{m}\nabla\cdot\boldsymbol{\mathcal{E}}+\frac{1}{m}\nabla^2\delta p\\
&=-\omega_{\mathrm{p}}^{\,2}\,\delta n+\frac{2E_{\mathrm{F}}}{3m}\nabla^2\delta n
\end{aligned}
$$

$\delta n\propto e^{i(kx-\omega t)}$ を代入し，$\dfrac{2E_{\mathrm{F}}}{m}=v_{\mathrm{F}}^{\,2}$ を使うと，

$$
\finalanswer{\omega^2=\omega_{\mathrm{p}}^{\,2}+\frac{1}{3}v_{\mathrm{F}}^{\,2}k^2}
$$

となります。圧力が復元力を補うので，波長が短いほど振動数がわずかに上がります。

===== FILE: 06solid_state/09/09_040.md =====
---
tags:
  - 発展
---

# イオン結晶の光学フォノンと LST 関係

## 問題
電荷 $+q$ と $-q$（$q>0$）の2種類のイオンからなるイオン結晶を考える。イオンの質量を $M_1,M_2$，換算質量を $M_{\mathrm{r}}=\dfrac{M_1M_2}{M_1+M_2}$，単位体積あたりのイオン対の数を $N$ とする。長波長の光学モードで，正イオンと負イオンの相対変位 $w$ は

$$
M_{\mathrm{r}}\ddot{w}=-M_{\mathrm{r}}\omega_{\mathrm{T}}^{\,2}w+q\mathcal{E}
$$

に従うとする。$\omega_{\mathrm{T}}>0$ は近距離力による復元力を表す定数，$\mathcal{E}$ は巨視的な電場で，局所電場の補正は無視する。電子の分極は高い振動数まで瞬時に追随し，分極に $\varepsilon_0(\varepsilon_\infty-1)\mathcal{E}$ を加えるとする。$\varepsilon_\infty>1$ は定数，$\varepsilon_0$ は真空の誘電率である。分極は $P=Nqw+\varepsilon_0(\varepsilon_\infty-1)\mathcal{E}$，比誘電関数は $\varepsilon_{\mathrm{r}}(\omega)=1+\dfrac{P}{\varepsilon_0\mathcal{E}}$ である。電磁場の遅延は無視し，電場は静電ポテンシャル $\phi$ から $\boldsymbol{\mathcal{E}}=-\nabla\phi$ で与えられ，自由電荷はないとする。以下の問いに答えよ。

(1) 角振動数 $\omega$ の電場に対する $\varepsilon_{\mathrm{r}}(\omega)$ を求めよ。また，静的な比誘電率 $\varepsilon_{\mathrm{r}}(0)$ を求め，$\varepsilon_{\mathrm{r}}(\omega)$ を $\varepsilon_{\mathrm{r}}(0)$，$\varepsilon_\infty$，$\omega_{\mathrm{T}}$ で表せ。

(2) 変位が $e^{i(\boldsymbol{k}\cdot\boldsymbol{r}-\omega t)}$ の形の波を考える。変位が $\boldsymbol{k}$ に垂直な横波と，$\boldsymbol{k}$ に平行な縦波のそれぞれについて，$\nabla\cdot\boldsymbol{D}=0$ と $\boldsymbol{\mathcal{E}}=-\nabla\phi$ を用いて振動数を求めよ。$\boldsymbol{D}=\varepsilon_0\boldsymbol{\mathcal{E}}+\boldsymbol{P}$ である。縦波の振動数を $\omega_{\mathrm{L}}$ として，$\dfrac{\omega_{\mathrm{L}}^{\,2}}{\omega_{\mathrm{T}}^{\,2}}$ を $\varepsilon_{\mathrm{r}}(0)$ と $\varepsilon_\infty$ で表せ。

(3) $\varepsilon_{\mathrm{r}}(\omega)$ を $\varepsilon_\infty,\omega_{\mathrm{L}},\omega_{\mathrm{T}}$ で表し，$\varepsilon_{\mathrm{r}}(\omega)<0$ となる $\omega$ の範囲を求めよ。また，塩化ナトリウムの値 $\varepsilon_{\mathrm{r}}(0)=5.9$，$\varepsilon_\infty=2.25$，$\omega_{\mathrm{T}}=3.09\times10^{13}\ \mathrm{s^{-1}}$ を用いて $\omega_{\mathrm{L}}$ を求めよ。

(4) ある結晶で，温度を下げると $\omega_{\mathrm{T}}^{\,2}=A(T-T_0)$ のように横波の振動数が小さくなる。$A>0$，$T_0$ は定数，$T$ は温度で，$T>T_0$ とする。$\omega_{\mathrm{L}}$ と $\varepsilon_\infty$ が温度によらないとき，$\varepsilon_{\mathrm{r}}(0)$ の温度依存性を求めよ。

---

## 解答・解説

### (1)
$w\propto e^{-i\omega t}$ として運動方程式を解くと $w=\dfrac{q\mathcal{E}}{M_{\mathrm{r}}(\omega_{\mathrm{T}}^{\,2}-\omega^2)}$ です。これを分極に代入すると，

$$
\finalanswer{\varepsilon_{\mathrm{r}}(\omega)=\varepsilon_\infty+\frac{Nq^2}{\varepsilon_0M_{\mathrm{r}}(\omega_{\mathrm{T}}^{\,2}-\omega^2)}}
$$

となります。$\omega=0$ とおくと静的な値が得られます。

$$
\finalanswer{\varepsilon_{\mathrm{r}}(0)=\varepsilon_\infty+\frac{Nq^2}{\varepsilon_0M_{\mathrm{r}}\omega_{\mathrm{T}}^{\,2}}}
$$

この式から $\dfrac{Nq^2}{\varepsilon_0M_{\mathrm{r}}}=\{\varepsilon_{\mathrm{r}}(0)-\varepsilon_\infty\}\omega_{\mathrm{T}}^{\,2}$ なので，

$$
\finalanswer{\varepsilon_{\mathrm{r}}(\omega)=\varepsilon_\infty+\frac{\{\varepsilon_{\mathrm{r}}(0)-\varepsilon_\infty\}\omega_{\mathrm{T}}^{\,2}}{\omega_{\mathrm{T}}^{\,2}-\omega^2}}
$$

となります。

### (2)
$\boldsymbol{\mathcal{E}}=-\nabla\phi=-i\boldsymbol{k}\phi$ なので，電場は常に $\boldsymbol{k}$ に平行です。

横波では $\boldsymbol{P}$ のイオンの部分が $\boldsymbol{k}$ に垂直です。$\nabla\cdot\boldsymbol{D}=0$ は $\boldsymbol{k}\cdot\boldsymbol{D}=0$ を意味します。$\boldsymbol{\mathcal{E}}$ は $\boldsymbol{k}$ に平行なので，この条件から $\boldsymbol{\mathcal{E}}=\boldsymbol{0}$ が導かれます。運動方程式に電場の項がなくなるので，

$$
\finalanswer{\text{横波}:\ \omega=\omega_{\mathrm{T}}}
$$

です。縦波では $\boldsymbol{\mathcal{E}}$，$\boldsymbol{P}$，$\boldsymbol{D}$ がすべて $\boldsymbol{k}$ に平行なので，$\boldsymbol{k}\cdot\boldsymbol{D}=0$ から $\boldsymbol{D}=\varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{\mathcal{E}}=\boldsymbol{0}$ です。$\mathcal{E}\ne0$ なので $\varepsilon_{\mathrm{r}}(\omega_{\mathrm{L}})=0$ が条件です。(1) の最後の式を0とおきます。

$$
\varepsilon_\infty(\omega_{\mathrm{T}}^{\,2}-\omega_{\mathrm{L}}^{\,2})+\{\varepsilon_{\mathrm{r}}(0)-\varepsilon_\infty\}\omega_{\mathrm{T}}^{\,2}=0
$$

これを解くと，

$$
\finalanswer{\frac{\omega_{\mathrm{L}}^{\,2}}{\omega_{\mathrm{T}}^{\,2}}=\frac{\varepsilon_{\mathrm{r}}(0)}{\varepsilon_\infty}}
$$

となります。これがリデイン・ザックス・テラーの関係です。縦波ではイオンの変位がつくる電場が復元力を強めるので，$\omega_{\mathrm{L}}>\omega_{\mathrm{T}}$ になります。

### (3)
(1) の式を通分し，(2) の関係 $\varepsilon_{\mathrm{r}}(0)\omega_{\mathrm{T}}^{\,2}=\varepsilon_\infty\omega_{\mathrm{L}}^{\,2}$ を使います。

$$
\begin{aligned}
\varepsilon_{\mathrm{r}}(\omega)&=\frac{\varepsilon_{\mathrm{r}}(0)\omega_{\mathrm{T}}^{\,2}-\varepsilon_\infty\omega^2}{\omega_{\mathrm{T}}^{\,2}-\omega^2}\\
&=\varepsilon_\infty\frac{\omega_{\mathrm{L}}^{\,2}-\omega^2}{\omega_{\mathrm{T}}^{\,2}-\omega^2}
\end{aligned}
$$

分子と分母の符号が異なるとき負になるので，

$$
\begin{aligned}
&\finalanswer{\varepsilon_{\mathrm{r}}(\omega)=\varepsilon_\infty\frac{\omega_{\mathrm{L}}^{\,2}-\omega^2}{\omega_{\mathrm{T}}^{\,2}-\omega^2}}\\
&\finalanswer{\varepsilon_{\mathrm{r}}<0\ \text{となるのは}\ \omega_{\mathrm{T}}<\omega<\omega_{\mathrm{L}}}
\end{aligned}
$$

となります。比誘電関数を図に示します。

<!-- FIGURE solution (3): 横軸 ω（0 から 2ω_T 程度），縦軸 ε_r。ω = 0 で ε_r(0) から始まり，ω_T に向かって正の無限大に発散する曲線。ω_T のすぐ上で負の無限大から上がり，ω_L で 0 を横切り，高振動数で ε_∞ に近づく曲線。ω_T に縦の破線（漸近線）を引く。ω_T < ω < ω_L の範囲を横軸に沿って塗り「ε_r < 0（全反射）」と注記する。縦軸に ε_r(0) と ε_∞ の目盛りを付け，ε_∞ に水平な点線を引く。 -->

この範囲では屈折率が純虚数になり，光は結晶に入れずに全反射されます。塩化ナトリウムの値を (2) の関係に代入します。

$$
\omega_{\mathrm{L}}=3.09\times10^{13}\times\sqrt{\frac{5.9}{2.25}}\ \mathrm{s^{-1}}
$$

これを計算すると，

$$
\finalanswer{\omega_{\mathrm{L}}\approx5.0\times10^{13}\ \mathrm{s^{-1}}}
$$

となります。赤外域のこの範囲で反射率が高くなる帯を残留線帯とよびます。

### (4)
(2) の関係を $\varepsilon_{\mathrm{r}}(0)$ について解き，$\omega_{\mathrm{T}}^{\,2}$ に与えられた温度依存性を代入します。

$$
\varepsilon_{\mathrm{r}}(0)=\varepsilon_\infty\frac{\omega_{\mathrm{L}}^{\,2}}{\omega_{\mathrm{T}}^{\,2}}
$$

より，

$$
\finalanswer{\varepsilon_{\mathrm{r}}(0)=\frac{\varepsilon_\infty\omega_{\mathrm{L}}^{\,2}}{A(T-T_0)}}
$$

となります。$T\to T_0$ で横波の振動数が0に近づくと，静的な誘電率は $1/(T-T_0)$ に比例して発散します。これは強誘電体の転移点の上で観測されるキュリー・ワイス則で，振動数が0に向かう横波の光学モードをソフトモードとよびます。

===== FILE: 06solid_state/09/09_050.md =====
---
tags:
  - 標準
---

# 金属の反射率

## 問題
金属の伝導電子を，数密度 $n$，電荷 $-e$（$e>0$），質量 $m$，緩和時間 $\tau$ のドルーデ模型で表す。直流伝導度を $\sigma_0=\dfrac{ne^2\tau}{m}$，プラズマ角振動数を $\omega_{\mathrm{p}}=\sqrt{\dfrac{ne^2}{\varepsilon_0m}}$ とする。$\varepsilon_0$ は真空の誘電率である。角振動数 $\omega>0$ の交流伝導度は $\sigma(\omega)=\dfrac{\sigma_0}{1-i\omega\tau}$，比誘電関数は $\varepsilon_{\mathrm{r}}(\omega)=1+\dfrac{i\sigma(\omega)}{\varepsilon_0\omega}$ で与えられる。イオン芯の分極は無視する。複素屈折率を $N=\sqrt{\varepsilon_{\mathrm{r}}}$（$\mathrm{Re}\,N\ge0$，$\mathrm{Im}\,N\ge0$）とし，真空から垂直に入射した光の反射率を $R=\left|\dfrac{1-N}{1+N}\right|^2$ とする。以下の問いに答えよ。

(1) $\varepsilon_{\mathrm{r}}(\omega)$ の実部と虚部を $\omega_{\mathrm{p}}$，$\tau$，$\omega$ で表せ。

(2) 減衰を無視する極限 $\tau\to\infty$ で，$\omega>\omega_{\mathrm{p}}$ のときの $R$ を $\omega_{\mathrm{p}}/\omega$ で表せ。また，$\omega\gg\omega_{\mathrm{p}}$ での $R$ の主要な振る舞いを求めよ。

(3) $\omega\tau\ll1$ の低振動数で，$\dfrac{\sigma_0}{\varepsilon_0\omega}\gg1$ とする。$1-R$ を $\sigma_0$，$\varepsilon_0$，$\omega$ で表せ。

(4) $\dfrac{1}{\tau}\ll\omega<\omega_{\mathrm{p}}$ とし，$\omega$ は $\omega_{\mathrm{p}}$ に近すぎないとする。$N=n_{\mathrm{r}}+i\kappa$ と書くと，$n_{\mathrm{r}}\ll\kappa$ となる。$1-R$ を $\tau$，$\omega$，$\omega_{\mathrm{p}}$ で表せ。また，$\omega\ll\omega_{\mathrm{p}}$ での $1-R$ を求めよ。

---

## 解答・解説

### (1)
$\sigma(\omega)$ の分子と分母に $1+i\omega\tau$ をかけて実数の分母にし，$\sigma_0/\varepsilon_0=\omega_{\mathrm{p}}^{\,2}\tau$ を使います。

$$
\begin{aligned}
\frac{i\sigma}{\varepsilon_0\omega}&=\frac{i\omega_{\mathrm{p}}^{\,2}\tau(1+i\omega\tau)}{\omega(1+\omega^2\tau^2)}\\
&=-\frac{\omega_{\mathrm{p}}^{\,2}\tau^2}{1+\omega^2\tau^2}+i\frac{\omega_{\mathrm{p}}^{\,2}\tau}{\omega(1+\omega^2\tau^2)}
\end{aligned}
$$

これに1を加えると，

$$
\begin{aligned}
&\finalanswer{\mathrm{Re}\,\varepsilon_{\mathrm{r}}=1-\frac{\omega_{\mathrm{p}}^{\,2}\tau^2}{1+\omega^2\tau^2}}\\
&\finalanswer{\mathrm{Im}\,\varepsilon_{\mathrm{r}}=\frac{\omega_{\mathrm{p}}^{\,2}\tau}{\omega(1+\omega^2\tau^2)}}
\end{aligned}
$$

となります。

### (2)
$\tau\to\infty$ では虚部が消え，$\varepsilon_{\mathrm{r}}=1-\omega_{\mathrm{p}}^{\,2}/\omega^2$ です。$\omega>\omega_{\mathrm{p}}$ ではこれが正なので，$N$ は1より小さい正の実数です。

$$
\finalanswer{R=\left(\frac{1-\sqrt{1-\omega_{\mathrm{p}}^{\,2}/\omega^2}}{1+\sqrt{1-\omega_{\mathrm{p}}^{\,2}/\omega^2}}\right)^2}
$$

となります。$\omega\gg\omega_{\mathrm{p}}$ では $N\approx1-\dfrac{\omega_{\mathrm{p}}^{\,2}}{2\omega^2}$ なので，分子は $\dfrac{\omega_{\mathrm{p}}^{\,2}}{2\omega^2}$，分母はほぼ2です。

$$
\finalanswer{R\approx\frac{\omega_{\mathrm{p}}^{\,4}}{16\omega^4}}
$$

となります。$\omega\to\omega_{\mathrm{p}}$ では $N\to0$ で $R\to1$ となり，$\omega_{\mathrm{p}}$ を境に反射率が急に下がります。

### (3)
$\omega\tau\ll1$ では (1) の虚部は $\dfrac{\sigma_0}{\varepsilon_0\omega}$ に近づき，実部より十分大きくなります。そこで $\varepsilon_{\mathrm{r}}\approx is$ と近似します。ここで $s=\dfrac{\sigma_0}{\varepsilon_0\omega}\gg1$ です。$\sqrt{i}=\dfrac{1+i}{\sqrt{2}}$ なので，$N$ の実部と虚部は等しくなります。

$$
N\approx n_0(1+i),\qquad n_0=\sqrt{\frac{s}{2}}\gg1
$$

これを反射率に代入し，$n_0$ が大きいとして展開します。

$$
\begin{aligned}
R&=\frac{(1-n_0)^2+n_0^{\,2}}{(1+n_0)^2+n_0^{\,2}}\\
&\approx1-\frac{2}{n_0}
\end{aligned}
$$

$n_0$ を戻すと，

$$
\finalanswer{1-R\approx2\sqrt{\frac{2\varepsilon_0\omega}{\sigma_0}}}
$$

となります。これをハーゲン・ルーベンスの関係とよびます。直流伝導度の大きい金属ほど，赤外光をよく反射します。

### (4)
$\omega\tau\gg1$ なので，(1) の式は $\varepsilon'\approx1-\dfrac{\omega_{\mathrm{p}}^{\,2}}{\omega^2}$，$\varepsilon''\approx\dfrac{\omega_{\mathrm{p}}^{\,2}}{\omega^3\tau}$ と近似できます。$\varepsilon'<0$ で $\varepsilon''$ は小さいです。$N^2=\varepsilon_{\mathrm{r}}$ の実部と虚部を比べ，$n_{\mathrm{r}}\ll\kappa$ を使います。

$$
\begin{aligned}
\kappa&\approx\sqrt{-\varepsilon'}=\frac{\sqrt{\omega_{\mathrm{p}}^{\,2}-\omega^2}}{\omega}\\
n_{\mathrm{r}}&=\frac{\varepsilon''}{2\kappa}
\end{aligned}
$$

反射率を $n_{\mathrm{r}}$ の1次まで展開します。$1+\kappa^2=1-\varepsilon'=\omega_{\mathrm{p}}^{\,2}/\omega^2$ に注意します。

$$
\begin{aligned}
1-R&\approx\frac{4n_{\mathrm{r}}}{1+\kappa^2}=\frac{2\varepsilon''\omega^2}{\kappa\,\omega_{\mathrm{p}}^{\,2}}\\
&=\frac{2}{\omega\tau\kappa}
\end{aligned}
$$

$\omega\kappa=\sqrt{\omega_{\mathrm{p}}^{\,2}-\omega^2}$ を使うと，

$$
\begin{aligned}
&\finalanswer{1-R\approx\frac{2}{\tau\sqrt{\omega_{\mathrm{p}}^{\,2}-\omega^2}}}\\
&\finalanswer{1-R\approx\frac{2}{\omega_{\mathrm{p}}\tau}\quad(\omega\ll\omega_{\mathrm{p}})}
\end{aligned}
$$

となります。減衰を無視すると $\omega<\omega_{\mathrm{p}}$ で $R=1$ でしたが，散乱があると $2/(\omega_{\mathrm{p}}\tau)$ 程度の光が吸収されます。反射率の全体像を図に示します。

<!-- FIGURE solution (4): 横軸 ω/ω_p（0〜2），縦軸 反射率 R（0〜1）。減衰のない場合を破線で描く：0 < ω/ω_p < 1 で R = 1，ω/ω_p > 1 で急に下がる。有限の τ（例えば ω_p τ = 30）の場合を実線で描く：低振動数側では 1 よりわずかに低いところから始まり，ω/ω_p < 1 で 1 − 2/(ω_p τ) 程度のほぼ平らな値をとり，ω_p 付近で丸みを帯びて下がる。ω/ω_p = 1 に縦の点線を引く。平らな部分と R = 1 の間のすき間に矢印を付けて「≈ 2/(ω_p τ)」と注記する。 -->

===== FILE: 06solid_state/10/10_010.md =====
---
tags:
  - 基本
---

# 原子の反磁性

## 問題
原子番号 $Z$ の原子で，すべての電子殻が閉じており，全軌道角運動量と全スピンがともに0で，基底状態の電子分布が球対称であるとする。この原子を $z$ 方向の一様な磁束密度 $B$ の中に置く。電子の電荷を $-e$（$e>0$），質量を $m$ とし，ベクトルポテンシャルを $\boldsymbol{A}=\dfrac{1}{2}\boldsymbol{B}\times\boldsymbol{r}$ にとる。電子 $i$ の運動エネルギーは $\dfrac{(\boldsymbol{p}_i+e\boldsymbol{A}(\boldsymbol{r}_i))^2}{2m}$ と書ける。全スピンが0なのでスピンの寄与は考えない。真空の透磁率を $\mu_0$ とし，原子の数密度 $n$ の物質の磁化率を，磁化 $M$ を用いて $\chi=\dfrac{\mu_0M}{B}$ で定義する。以下の問いに答えよ。

(1) $\nabla\times\boldsymbol{A}=\boldsymbol{B}$，$\nabla\cdot\boldsymbol{A}=0$ を確かめよ。また，1つの電子について

$$
\frac{(\boldsymbol{p}+e\boldsymbol{A})^2}{2m}=\frac{\boldsymbol{p}^2}{2m}+\frac{eB}{2m}L_z+\frac{e^2B^2}{8m}(x^2+y^2)
$$

となることを示せ。$L_z=xp_y-yp_x$ である。

(2) 1次の摂動論で，磁場による基底状態のエネルギーの変化 $\Delta E$ を，各電子の $\langle r_i^{\,2}\rangle$ の和 $\displaystyle\sum_{i=1}^{Z}\langle r_i^{\,2}\rangle$ を用いて求めよ。

(3) 原子の磁気モーメント $\mu_z=-\dfrac{\partial\Delta E}{\partial B}$ と磁化率 $\chi$ を求めよ。

(4) ヘリウム原子の2個の電子が，どちらも波動関数 $\psi(r)=\dfrac{1}{\sqrt{\pi b^3}}e^{-r/b}$ の状態にあるとする。$\langle r^2\rangle$ を $b$ で表し，1 mol あたりの磁化率 $\chi_{\mathrm{mol}}=\dfrac{\mu_0N_{\mathrm{A}}\mu_z}{B}$ を求めよ。また，$b=0.0313\ \mathrm{nm}$ として数値を求めよ。$\mu_0=4\pi\times10^{-7}\ \mathrm{H/m}$，$N_{\mathrm{A}}=6.022\times10^{23}\ \mathrm{mol^{-1}}$，$e=1.602\times10^{-19}\ \mathrm{C}$，$m=9.109\times10^{-31}\ \mathrm{kg}$ とし，必要なら $\displaystyle\int_0^\infty r^ne^{-\lambda r}\,\mathrm{d}r=\frac{n!}{\lambda^{n+1}}$ を用いてよい。

---

## 解答・解説

### (1)
成分で書くと $\boldsymbol{A}=\dfrac{B}{2}(-y,\,x,\,0)$ です。回転と発散を計算します。

$$
\begin{aligned}
\nabla\times\boldsymbol{A}&=\left(0,\ 0,\ \frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}\right)=(0,\,0,\,B)\\
\nabla\cdot\boldsymbol{A}&=\frac{\partial}{\partial x}\left(-\frac{By}{2}\right)+\frac{\partial}{\partial y}\left(\frac{Bx}{2}\right)=0
\end{aligned}
$$

次に2乗を展開します。$\nabla\cdot\boldsymbol{A}=0$ なので $\boldsymbol{p}\cdot\boldsymbol{A}=\boldsymbol{A}\cdot\boldsymbol{p}$ となり，交差項は $2e\boldsymbol{A}\cdot\boldsymbol{p}$ にまとまります。

$$
\begin{aligned}
\boldsymbol{A}\cdot\boldsymbol{p}&=\frac{B}{2}(xp_y-yp_x)=\frac{B}{2}L_z\\
\boldsymbol{A}^2&=\frac{B^2}{4}(x^2+y^2)
\end{aligned}
$$

これらを $(\boldsymbol{p}+e\boldsymbol{A})^2=\boldsymbol{p}^2+2e\boldsymbol{A}\cdot\boldsymbol{p}+e^2\boldsymbol{A}^2$ に入れて $2m$ で割ると，

$$
\finalanswer{\frac{(\boldsymbol{p}+e\boldsymbol{A})^2}{2m}=\frac{\boldsymbol{p}^2}{2m}+\frac{eB}{2m}L_z+\frac{e^2B^2}{8m}(x^2+y^2)}
$$

となります。

### (2)
1次の摂動では，追加された項の基底状態での期待値がエネルギーの変化です。全軌道角運動量が0の状態では，全電子の $L_z$ の和の期待値は0です。電子分布が球対称なので，$\langle x^2\rangle=\langle y^2\rangle=\langle z^2\rangle=\dfrac{1}{3}\langle r^2\rangle$ です。

$$
\Delta E=\frac{e^2B^2}{8m}\sum_i\langle x_i^{\,2}+y_i^{\,2}\rangle=\frac{e^2B^2}{8m}\cdot\frac{2}{3}\sum_i\langle r_i^{\,2}\rangle
$$

より，

$$
\finalanswer{\Delta E=\frac{e^2B^2}{12m}\sum_{i=1}^{Z}\langle r_i^{\,2}\rangle}
$$

となります。

### (3)
$\Delta E$ は $B^2$ に比例するので，磁気モーメントは $B$ に比例します。

$$
\finalanswer{\mu_z=-\frac{e^2B}{6m}\sum_i\langle r_i^{\,2}\rangle}
$$

磁化は $M=n\mu_z$ なので，

$$
\finalanswer{\chi=-\frac{\mu_0ne^2}{6m}\sum_i\langle r_i^{\,2}\rangle}
$$

となります。磁気モーメントは磁場と逆向きで，磁化率は負です。磁場をかけると電子の軌道運動が誘導電流のように変化し，磁場を打ち消す向きのモーメントが生じます。$\chi$ は温度によりません。

### (4)
与えられた積分で $n=4$，$\lambda=2/b$ とおいて $\langle r^2\rangle$ を計算します。

$$
\begin{aligned}
\langle r^2\rangle&=\frac{1}{\pi b^3}\int_0^\infty r^2e^{-2r/b}\,4\pi r^2\,\mathrm{d}r\\
&=\frac{4}{b^3}\cdot\frac{24b^5}{32}=3b^2
\end{aligned}
$$

2個の電子の和は $6b^2$ です。これを (3) の $\mu_z$ に入れると，

$$
\begin{aligned}
&\finalanswer{\langle r^2\rangle=3b^2}\\
&\finalanswer{\chi_{\mathrm{mol}}=-\frac{\mu_0N_{\mathrm{A}}e^2b^2}{m}}
\end{aligned}
$$

となります。数値を代入します。

$$
\chi_{\mathrm{mol}}=-\frac{4\pi\times10^{-7}\times6.022\times10^{23}\times(1.602\times10^{-19})^2\times(3.13\times10^{-11})^2}{9.109\times10^{-31}}\ \mathrm{m^3/mol}
$$

これを計算すると，

$$
\finalanswer{\chi_{\mathrm{mol}}\approx-2.1\times10^{-11}\ \mathrm{m^3/mol}}
$$

となります。測定値は約 $-2.4\times10^{-11}\ \mathrm{m^3/mol}$ で，単純な波動関数でもよく合います。磁化率は軌道の広がりの2乗に比例するので，外側の電子殻が大きい重い原子ほど反磁性が強くなります。

===== FILE: 06solid_state/10/10_020.md =====
---
tags:
  - 基本
---

# 常磁性とキュリーの法則

## 問題
単位体積あたり $n$ 個の，互いに独立なスピン $1/2$ の磁気モーメントを考える。$z$ 方向に磁束密度 $B$ をかけると，各モーメントの $z$ 成分は $+\mu_{\mathrm{B}}$ または $-\mu_{\mathrm{B}}$ の値をとり，そのエネルギーはそれぞれ $-\mu_{\mathrm{B}}B$，$+\mu_{\mathrm{B}}B$ である。$\mu_{\mathrm{B}}$ はボーア磁子である。温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$，真空の透磁率を $\mu_0$ とし，弱い磁場での磁化率を，磁化 $M$ を用いて $\chi=\dfrac{\mu_0M}{B}$ で定義する。以下の問いに答えよ。

(1) 1つのモーメントの分配関数と，モーメントの $z$ 成分の平均 $\langle\mu_z\rangle$ を求めよ。また，磁化 $M$ を求めよ。

(2) $\mu_{\mathrm{B}}B\ll k_{\mathrm{B}}T$ での $\chi$ を求め，$\chi=C/T$ と書いたときの $C$ を求めよ。

(3) 一般に，全角運動量の量子数 $J$ をもつイオンでは，角運動量の $z$ 成分の量子数 $m_J=-J,-J+1,\ldots,J$ に対して，モーメントの $z$ 成分が $-g\mu_{\mathrm{B}}m_J$，エネルギーが $g\mu_{\mathrm{B}}m_JB$ となる。$g$ はランデの $g$ 因子である。このイオンが単位体積あたり $n$ 個あるとき，弱い磁場での $\chi$ を求めよ。$\displaystyle\sum_{m_J=-J}^{J}m_J^{\,2}=\frac{J(J+1)(2J+1)}{3}$ を用いてよい。また，$J=1/2$，$g=2$ で (2) の結果に一致することを確かめよ。

(4) (1) の系の $N$ 個のモーメント全体のエントロピー $S$ を，$x=\mu_{\mathrm{B}}B/k_{\mathrm{B}}T$ の関数として求めよ。さらに，温度 $T_{\mathrm{i}}$，磁場 $B_{\mathrm{i}}$ の状態から，断熱的に磁場を $B_{\mathrm{f}}$ まで下げたときの温度 $T_{\mathrm{f}}$ を求めよ。格子振動など他の自由度との熱のやりとりは無視する。

---

## 解答・解説

### (1)
2つの状態のボルツマン因子を足すと分配関数になります。$x=\mu_{\mathrm{B}}B/k_{\mathrm{B}}T$ とおくと，

$$
\finalanswer{Z_1=e^{x}+e^{-x}=2\cosh x}
$$

です。平均のモーメントは，各状態の値に確率をかけて足したものです。

$$
\langle\mu_z\rangle=\mu_{\mathrm{B}}\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}
$$

より，

$$
\begin{aligned}
&\finalanswer{\langle\mu_z\rangle=\mu_{\mathrm{B}}\tanh\frac{\mu_{\mathrm{B}}B}{k_{\mathrm{B}}T}}\\
&\finalanswer{M=n\mu_{\mathrm{B}}\tanh\frac{\mu_{\mathrm{B}}B}{k_{\mathrm{B}}T}}
\end{aligned}
$$

となります。強い磁場や低温では，磁化はすべてのモーメントがそろった値 $n\mu_{\mathrm{B}}$ に飽和します。

### (2)
$x\ll1$ では $\tanh x\approx x$ なので，磁化は $B$ に比例します。

$$
M\approx\frac{n\mu_{\mathrm{B}}^{\,2}}{k_{\mathrm{B}}T}B
$$

これを磁化率の定義に入れると，

$$
\begin{aligned}
&\finalanswer{\chi=\frac{\mu_0n\mu_{\mathrm{B}}^{\,2}}{k_{\mathrm{B}}T}}\\
&\finalanswer{C=\frac{\mu_0n\mu_{\mathrm{B}}^{\,2}}{k_{\mathrm{B}}}}
\end{aligned}
$$

となります。磁化率が温度に反比例することをキュリーの法則とよびます。磁場はモーメントをそろえようとし，熱ゆらぎはばらばらにしようとするので，両者の比 $\mu_{\mathrm{B}}B/k_{\mathrm{B}}T$ で磁化が決まります。

### (3)
$y=g\mu_{\mathrm{B}}B/k_{\mathrm{B}}T\ll1$ とおき，ボルツマン因子を $e^{-ym_J}\approx1-ym_J$ と展開します。$m_J$ の和は0なので，分母は $2J+1$，分子は $m_J^{\,2}$ の和に比例します。

$$
\begin{aligned}
\langle\mu_z\rangle&\approx\frac{\sum_{m_J}(-g\mu_{\mathrm{B}}m_J)(1-ym_J)}{2J+1}\\
&=g\mu_{\mathrm{B}}y\frac{\sum_{m_J}m_J^{\,2}}{2J+1}=\frac{g^2\mu_{\mathrm{B}}^{\,2}J(J+1)}{3k_{\mathrm{B}}T}B
\end{aligned}
$$

磁化 $M=n\langle\mu_z\rangle$ から，

$$
\finalanswer{\chi=\frac{\mu_0ng^2\mu_{\mathrm{B}}^{\,2}J(J+1)}{3k_{\mathrm{B}}T}}
$$

となります。$J=1/2$，$g=2$ では $g^2J(J+1)/3=4\times\dfrac{3}{4}\times\dfrac{1}{3}=1$ となり，(2) の結果と一致します。キュリー定数を測ると，有効磁子数 $g\sqrt{J(J+1)}$ が求まります。

### (4)
$N$ 個の独立なモーメントの自由エネルギーは $F=-Nk_{\mathrm{B}}T\ln(2\cosh x)$ です。エントロピーは $S=-\partial F/\partial T$ で，$\dfrac{\partial x}{\partial T}=-\dfrac{x}{T}$ を使って微分します。

$$
\begin{aligned}
S&=Nk_{\mathrm{B}}\ln(2\cosh x)+Nk_{\mathrm{B}}T\tanh x\cdot\frac{\partial x}{\partial T}\\
&=Nk_{\mathrm{B}}\left[\ln(2\cosh x)-x\tanh x\right]
\end{aligned}
$$

より，

$$
\finalanswer{S=Nk_{\mathrm{B}}\left[\ln(2\cosh x)-x\tanh x\right]}
$$

となります。$x\to0$ では $S\to Nk_{\mathrm{B}}\ln2$ で，$x\to\infty$ では $S\to0$ です。$S$ は $x=\mu_{\mathrm{B}}B/k_{\mathrm{B}}T$ だけの関数なので，断熱過程では $B/T$ が一定に保たれます。

$$
\finalanswer{T_{\mathrm{f}}=\frac{B_{\mathrm{f}}}{B_{\mathrm{i}}}T_{\mathrm{i}}}
$$

となります。この断熱消磁は，ミリケルビン以下の低温をつくる方法として使われます。実際には，モーメントどうしの弱い相互作用による内部磁場のために，到達できる温度に下限があります。

===== FILE: 06solid_state/10/10_030.md =====
---
tags:
  - 標準
---

# パウリ常磁性

## 問題
数密度 $n$ の自由電子気体を考え，スピンを含めた単位体積あたりの状態密度を $D(E)$ とする。$E$ は運動エネルギーである。$z$ 方向に磁束密度 $B$ をかけると，スピンの磁気モーメントが磁場と平行な電子のエネルギーは $\mu_{\mathrm{B}}B$ だけ下がり，反平行な電子のエネルギーは $\mu_{\mathrm{B}}B$ だけ上がる。$\mu_{\mathrm{B}}$ はボーア磁子である。電子の軌道運動に対する磁場の効果は無視する。平行な電子の密度を $n_+$，反平行な電子の密度を $n_-$ とすると，磁化は $M=\mu_{\mathrm{B}}(n_+-n_-)$ である。化学ポテンシャルを $\mu$，フェルミ分布を $f(E)=\dfrac{1}{e^{(E-\mu)/k_{\mathrm{B}}T}+1}$，絶対零度でのフェルミエネルギーを $E_{\mathrm{F}}$ とする。$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度，$\mu_0$ は真空の透磁率である。磁化率は $\chi=\dfrac{\mu_0M}{B}$ で定義し，$B$ の1次までを考える。以下の問いに答えよ。

(1) 絶対零度で，$n_+$ と $n_-$ を $D$ と $\mu$ を用いて表せ。電子数が一定であることから，$\mu$ が $B$ の1次では変化しないことを示し，磁化率 $\chi_{\mathrm{P}}$ を $D(E_{\mathrm{F}})$ で表せ。

(2) 3次元の自由電子では $D(E_{\mathrm{F}})=\dfrac{3n}{2E_{\mathrm{F}}}$ である。$\chi_{\mathrm{P}}$ を $n$ と $E_{\mathrm{F}}$ で表せ。また，同じ密度の独立なスピン $1/2$ のモーメントによるキュリーの磁化率 $\chi_{\mathrm{C}}=\dfrac{\mu_0n\mu_{\mathrm{B}}^{\,2}}{k_{\mathrm{B}}T}$ との比 $\chi_{\mathrm{P}}/\chi_{\mathrm{C}}$ を，フェルミ温度 $T_{\mathrm{F}}=E_{\mathrm{F}}/k_{\mathrm{B}}$ を用いて表せ。

(3) 有限温度で，$M$ を $D(E)$ と $\partial f/\partial E$ を含む積分で表せ。また，電子が非縮退で $f(E)\approx e^{-(E-\mu)/k_{\mathrm{B}}T}$ と近似できる場合に，$\chi$ がキュリーの磁化率 $\chi_{\mathrm{C}}$ に一致することを示せ。

(4) 電子間の交換相互作用の効果を，平行な電子のエネルギーをさらに $\dfrac{I}{2}(n_+-n_-)$ だけ下げ，反平行な電子のエネルギーを同じだけ上げる項で表す。$I>0$ は定数である。絶対零度での磁化率 $\chi$ を $\chi_{\mathrm{P}}$，$I$，$D(E_{\mathrm{F}})$ で表せ。また，磁場がなくても磁化が生じる条件を求めよ。

---

## 解答・解説

### (1)
平行な電子の状態密度は，$D(E)/2$ を $\mu_{\mathrm{B}}B$ だけ低いエネルギーへずらしたものです。全エネルギーが $\mu$ 以下の状態を占有するので，運動エネルギーは $\mu+\mu_{\mathrm{B}}B$ まで詰まります。反平行な電子も同様に考えます。

$$
\finalanswer{n_\pm=\frac{1}{2}\int_0^{\mu\pm\mu_{\mathrm{B}}B}D(E)\,\mathrm{d}E}
$$

和をとって $B$ について展開すると，1次の項は打ち消し合います。

$$
n_++n_-=\int_0^{\mu}D(E)\,\mathrm{d}E+O(B^2)
$$

これが $B=0$ での電子数 $n$ に等しいので，$\mu=E_{\mathrm{F}}+O(B^2)$ です。差は1次の項だけが残ります。

$$
n_+-n_-\approx D(E_{\mathrm{F}})\mu_{\mathrm{B}}B
$$

これに $\mu_{\mathrm{B}}$ をかけて磁化を求めると，

$$
\finalanswer{\chi_{\mathrm{P}}=\mu_0\mu_{\mathrm{B}}^{\,2}D(E_{\mathrm{F}})}
$$

となります。2つのスピンの状態密度の様子を図に示します。

<!-- FIGURE solution (1): 縦軸をエネルギー E とし，左右に状態密度を横向きに描く。右側が平行スピン，左側が反平行スピンの状態密度 D/2（それぞれ √E 型の曲線）。右側は μ_B B だけ下に，左側は μ_B B だけ上にずらして描く。共通の化学ポテンシャル μ に水平な破線を引き，その下を両側とも塗る。右側の塗った部分が左側より多く，その差が幅 2μ_B B の細い帯になることがわかるように描き，帯を濃く塗る。ずれの大きさに μ_B B の矢印を付ける。 -->

### (2)
(1) に $D(E_{\mathrm{F}})=\dfrac{3n}{2E_{\mathrm{F}}}$ を代入し，比をとります。

$$
\begin{aligned}
&\finalanswer{\chi_{\mathrm{P}}=\frac{3\mu_0n\mu_{\mathrm{B}}^{\,2}}{2E_{\mathrm{F}}}}\\
&\finalanswer{\frac{\chi_{\mathrm{P}}}{\chi_{\mathrm{C}}}=\frac{3}{2}\cdot\frac{T}{T_{\mathrm{F}}}}
\end{aligned}
$$

となります。パウリの排他原理のために，磁場で向きを変えられるのはフェルミ面の近くの電子だけです。そのため磁化率はキュリーの値より $T/T_{\mathrm{F}}$ の程度だけ小さく，温度にもほとんどよりません。

### (3)
有限温度では，平行な電子の密度は $\dfrac{1}{2}\displaystyle\int D(E)f(E-\mu_{\mathrm{B}}B)\,\mathrm{d}E$ です。$f$ を $B$ について1次まで展開します。

$$
\begin{aligned}
n_+-n_-&=\frac{1}{2}\int D(E)\left[f(E-\mu_{\mathrm{B}}B)-f(E+\mu_{\mathrm{B}}B)\right]\mathrm{d}E\\
&\approx-\mu_{\mathrm{B}}B\int D(E)\frac{\partial f}{\partial E}\,\mathrm{d}E
\end{aligned}
$$

これに $\mu_{\mathrm{B}}$ をかけると，

$$
\finalanswer{M=\mu_{\mathrm{B}}^{\,2}B\int_0^\infty D(E)\left(-\frac{\partial f}{\partial E}\right)\mathrm{d}E}
$$

となります。非縮退の場合は $-\dfrac{\partial f}{\partial E}=\dfrac{f}{k_{\mathrm{B}}T}$ で，$\displaystyle\int D f\,\mathrm{d}E=n$ です。

$$
\finalanswer{\chi=\frac{\mu_0n\mu_{\mathrm{B}}^{\,2}}{k_{\mathrm{B}}T}=\chi_{\mathrm{C}}}
$$

となります。縮退した場合は $-\partial f/\partial E$ が $E=E_{\mathrm{F}}$ に集中したデルタ関数のようになり，(1) の結果に戻ります。

### (4)
(1) から，2つのスピンのエネルギーが逆向きに $\Delta$ ずつずれると，密度の差は $D(E_{\mathrm{F}})\Delta$ になります。交換相互作用があると $\Delta$ に密度の差そのものが含まれるので，自己無撞着な式が得られます。

$$
n_+-n_-=D(E_{\mathrm{F}})\left[\mu_{\mathrm{B}}B+\frac{I}{2}(n_+-n_-)\right]
$$

これを $n_+-n_-$ について解いて $\mu_0\mu_{\mathrm{B}}/B$ をかけると，

$$
\finalanswer{\chi=\frac{\chi_{\mathrm{P}}}{1-ID(E_{\mathrm{F}})/2}}
$$

となります。分母が0以下になると，磁場がなくても有限の磁化が安定になります。

$$
\finalanswer{\frac{I\,D(E_{\mathrm{F}})}{2}\ge1}
$$

これをストーナーの条件とよびます。$D(E_{\mathrm{F}})/2$ は1つのスピンあたりの状態密度です。フェルミ準位での状態密度が大きい鉄やニッケルなどの遷移金属で，この条件が満たされます。

===== FILE: 06solid_state/10/10_040.md =====
---
tags:
  - 標準
---

# 平均場近似による強磁性

## 問題
$N$ 個の格子点からなる結晶の各点 $i$ に，$\sigma_i=\pm1$ の値をとるスピンがあり，磁場の向きの磁気モーメント $\mu\sigma_i$ をもつとする。各格子点の最近接点の数を $z$ とし，ハミルトニアンを

$$
H=-J\sum_{\langle ij\rangle}\sigma_i\sigma_j-\mu B\sum_i\sigma_i
$$

とする。$J>0$ は交換相互作用の定数，$B$ は磁束密度で，最初の和は最近接の組についてそれぞれ1回ずつとる。平均場近似では，スピン $i$ に対する最近接スピンの影響を，その平均値 $m=\langle\sigma_j\rangle$ で置き換える。単位体積あたりのスピンの数を $n$，温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$，真空の透磁率を $\mu_0$ とする。磁化は $M=n\mu m$，磁化率は弱い磁場で $\chi=\dfrac{\mu_0M}{B}$ とする。以下の問いに答えよ。

(1) 平均場近似で，スピン $i$ のエネルギーを $\sigma_i$ の1次式で表し，$m$ が満たす方程式を求めよ。

(2) $B=0$ で，$m\ne0$ の解が存在する温度の範囲を求め，キュリー温度 $T_{\mathrm{C}}$ を $z$，$J$，$k_{\mathrm{B}}$ で表せ。

(3) $B=0$ で $T$ が $T_{\mathrm{C}}$ より少し低いとき，$m$ を $T/T_{\mathrm{C}}$ の関数として主要な項まで求めよ。$\tanh y\approx y-\dfrac{y^3}{3}$ を用いてよい。

(4) $T>T_{\mathrm{C}}$ で弱い磁場をかけたときの $\chi$ を求め，$\chi=\dfrac{C}{T-\theta}$ と書いたときの $C$ と $\theta$ を求めよ。

---

## 解答・解説

### (1)
スピン $i$ は $z$ 個の最近接スピンと結合しているので，それらを $m$ に置き換えると，$\sigma_i$ を含む項は次のようになります。

$$
\finalanswer{E_i=-(zJm+\mu B)\sigma_i}
$$

これは，有効的な磁場 $B+zJm/\mu$ の中にある独立なモーメントのエネルギーと同じ形です。$\sigma_i=\pm1$ の2つの状態で平均をとると $\tanh$ が現れます。その平均が $m$ に等しいとおくと，

$$
\finalanswer{m=\tanh\frac{zJm+\mu B}{k_{\mathrm{B}}T}}
$$

となります。右辺の $m$ は自分自身を決める式に入っているので，この式を自己無撞着方程式とよびます。

### (2)
$B=0$ では $m=\tanh(zJm/k_{\mathrm{B}}T)$ です。$m=0$ は常に解ですが，右辺の原点での傾き $zJ/k_{\mathrm{B}}T$ が1より大きいと，直線 $y=m$ と曲線が原点以外でも交わります。この式の解の様子を図に示します。

<!-- FIGURE solution (2): 横軸 m（−1.5〜1.5），縦軸 y。直線 y = m を細い実線で描く。曲線 y = tanh(T_C m/T) を2本描く：T > T_C の場合（原点での傾きが 1 より小さい，破線）は原点だけで直線と交わる；T < T_C の場合（傾きが 1 より大きい，太い実線）は原点と ±m_0 の3点で交わる。±m_0 の交点に黒丸を置く。縦軸 ±1 に水平な点線を引く。 -->

$\tanh$ は $m>0$ で上に凸なので，原点以外の交点が存在する条件は傾きが1より大きいことです。

$$
\begin{aligned}
&\finalanswer{T<T_{\mathrm{C}}}\\
&\finalanswer{T_{\mathrm{C}}=\frac{zJ}{k_{\mathrm{B}}}}
\end{aligned}
$$

となります。$T<T_{\mathrm{C}}$ では $m\ne0$ の解の方が自由エネルギーが低く，外部の磁場がなくても磁化が生じます。これが自発磁化です。

### (3)
$t=T/T_{\mathrm{C}}$ とおくと，方程式は $m=\tanh(m/t)$ です。$m$ が小さいので $\tanh$ を3次まで展開します。

$$
m=\frac{m}{t}-\frac{m^3}{3t^3}
$$

$m\ne0$ として両辺を $m$ で割ります。

$$
\begin{aligned}
m^2&=3t^3\left(\frac{1}{t}-1\right)\\
&=3t^2(1-t)
\end{aligned}
$$

$t\approx1$ なので，主要な項は

$$
\finalanswer{m\approx\sqrt{3\left(1-\frac{T}{T_{\mathrm{C}}}\right)}}
$$

となります。自発磁化は $T_{\mathrm{C}}$ に向かって $(T_{\mathrm{C}}-T)^{1/2}$ に比例して0になります。平均場近似では，この指数が格子の種類によらず $1/2$ になります。

### (4)
$T>T_{\mathrm{C}}$ では $B\to0$ で $m\to0$ なので，$\tanh$ を1次で近似できます。

$$
m=\frac{zJm+\mu B}{k_{\mathrm{B}}T}
$$

$zJ=k_{\mathrm{B}}T_{\mathrm{C}}$ を使って $m$ について解くと $m=\dfrac{\mu B}{k_{\mathrm{B}}(T-T_{\mathrm{C}})}$ です。$M=n\mu m$ から，

$$
\begin{aligned}
&\finalanswer{\chi=\frac{\mu_0n\mu^2}{k_{\mathrm{B}}(T-T_{\mathrm{C}})}}\\
&\finalanswer{C=\frac{\mu_0n\mu^2}{k_{\mathrm{B}}}}\\
&\finalanswer{\theta=T_{\mathrm{C}}}
\end{aligned}
$$

となります。これをキュリー・ワイス則とよびます。周りのスピンが外部の磁場と同じ向きにそろって磁場を強めるので，キュリーの法則より磁化率が大きくなり，$T_{\mathrm{C}}$ で発散します。


===== FILE: 06solid_state/10/10_050.md =====
---
tags:
  - 発展
---

# 反強磁性とネール温度

## 問題
格子点が A と B の2つの副格子に分かれた結晶を考える。A の点の最近接点はすべて B の点で，B の点の最近接点はすべて A の点である。各点の最近接点の数を $z$ とする。各点 $i$ には $\sigma_i=\pm1$ の値をとるスピンがあり，磁場の向きの磁気モーメント $\mu\sigma_i$ をもつ。ハミルトニアンを

$$
H=J\sum_{\langle ij\rangle}\sigma_i\sigma_j-\mu B\sum_i\sigma_i
$$

とする。$J>0$ であり，最初の和は最近接の組についてそれぞれ1回ずつとる。副格子 A，B のスピンの平均を $m_{\mathrm{A}},m_{\mathrm{B}}$ とし，平均場近似で考える。単位体積あたりのスピンの総数を $n$ とし，各副格子に $n/2$ ずつあるとする。温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$，真空の透磁率を $\mu_0$ とする。磁化は $M=\dfrac{n\mu}{2}(m_{\mathrm{A}}+m_{\mathrm{B}})$ で，磁化率は弱い磁場で $\chi=\dfrac{\mu_0M}{B}$ と定義する。以下の問いに答えよ。

(1) $m_{\mathrm{A}}$ と $m_{\mathrm{B}}$ が満たす平均場の方程式を求めよ。

(2) $B=0$ で $m_{\mathrm{A}}=-m_{\mathrm{B}}=m_{\mathrm{s}}\ne0$ の解が存在する温度の範囲を求め，ネール温度 $T_{\mathrm{N}}$ を求めよ。

(3) $T>T_{\mathrm{N}}$ で弱い磁場をかけたときの $\chi$ を求めよ。また，$\chi=\dfrac{C}{T-\theta}$ と書いたときの $\theta$ を求めよ。

(4) $T<T_{\mathrm{N}}$ で，(2) の解のまわりに弱い磁場をかける。$m_{\mathrm{A}}=m_{\mathrm{s}}+\delta_{\mathrm{A}}$，$m_{\mathrm{B}}=-m_{\mathrm{s}}+\delta_{\mathrm{B}}$ とおいて $\delta_{\mathrm{A}},\delta_{\mathrm{B}}$ の1次まで考え，$\chi$ を $T$，$T_{\mathrm{N}}$，$m_{\mathrm{s}}$ で表せ。また，$T=T_{\mathrm{N}}$ での値と，$T\to0$ での極限を求めよ。

---

## 解答・解説

### (1)
A の点の最近接点はすべて B の点です。そこで，相互作用の項で隣のスピンを $m_{\mathrm{B}}$ に置き換えると，A のスピン1つのエネルギーは $-(\mu B-zJm_{\mathrm{B}})\sigma_i$ になります。B のスピンも同じように扱えます。それぞれ2つの状態について平均をとると，

$$
\begin{aligned}
&\finalanswer{m_{\mathrm{A}}=\tanh\frac{\mu B-zJm_{\mathrm{B}}}{k_{\mathrm{B}}T}}\\
&\finalanswer{m_{\mathrm{B}}=\tanh\frac{\mu B-zJm_{\mathrm{A}}}{k_{\mathrm{B}}T}}
\end{aligned}
$$

となります。$J>0$ なので，隣の副格子の磁化はこのスピンを逆向きにそろえるようにはたらきます。

### (2)
$B=0$ で $m_{\mathrm{A}}=-m_{\mathrm{B}}=m_{\mathrm{s}}$ とおくと，(1) の2つの式はどちらも同じ式になります。

$$
m_{\mathrm{s}}=\tanh\frac{zJm_{\mathrm{s}}}{k_{\mathrm{B}}T}
$$

これは強磁性の平均場の方程式と同じ形です。右辺の原点での傾き $zJ/k_{\mathrm{B}}T$ が1より大きいときに限り，$m_{\mathrm{s}}\ne0$ の解があります。よって，

$$
\begin{aligned}
&\finalanswer{T<T_{\mathrm{N}}}\\
&\finalanswer{T_{\mathrm{N}}=\frac{zJ}{k_{\mathrm{B}}}}
\end{aligned}
$$

となります。$T_{\mathrm{N}}$ より低温では，2つの副格子がそれぞれ逆向きに自発磁化をもちます。それらが打ち消し合うので，全体の磁化は0です。

### (3)
$T>T_{\mathrm{N}}$ では，$B\to0$ で $m_{\mathrm{A}},m_{\mathrm{B}}\to0$ です。そこで $\tanh$ を1次で近似し，$zJ=k_{\mathrm{B}}T_{\mathrm{N}}$ を使います。

$$
\begin{aligned}
m_{\mathrm{A}}&=\frac{\mu B}{k_{\mathrm{B}}T}-\frac{T_{\mathrm{N}}}{T}m_{\mathrm{B}}\\
m_{\mathrm{B}}&=\frac{\mu B}{k_{\mathrm{B}}T}-\frac{T_{\mathrm{N}}}{T}m_{\mathrm{A}}
\end{aligned}
$$

2つの式を足して $m_{\mathrm{A}}+m_{\mathrm{B}}$ について解くと，

$$
m_{\mathrm{A}}+m_{\mathrm{B}}=\frac{2\mu B}{k_{\mathrm{B}}(T+T_{\mathrm{N}})}
$$

です。これを磁化の式に代入すると，

$$
\begin{aligned}
&\finalanswer{\chi=\frac{\mu_0n\mu^2}{k_{\mathrm{B}}(T+T_{\mathrm{N}})}}\\
&\finalanswer{\theta=-T_{\mathrm{N}}}
\end{aligned}
$$

となります。強磁性では $\theta=T_{\mathrm{C}}>0$ でしたが，反強磁性では $\theta$ が負になります。高温の磁化率から求めた $\theta$ の符号で，相互作用の符号を見分けられます。

### (4)
(2) の解では，$\tanh$ の引数が A で $T_{\mathrm{N}}m_{\mathrm{s}}/T$，B でその符号を変えたものです。どちらでも $\tanh$ の値の2乗は $m_{\mathrm{s}}^{\,2}$ なので，引数のずれに対する微分係数は $1-m_{\mathrm{s}}^{\,2}$ になります。

$$
\begin{aligned}
\delta_{\mathrm{A}}&=(1-m_{\mathrm{s}}^{\,2})\frac{\mu B-k_{\mathrm{B}}T_{\mathrm{N}}\delta_{\mathrm{B}}}{k_{\mathrm{B}}T}\\
\delta_{\mathrm{B}}&=(1-m_{\mathrm{s}}^{\,2})\frac{\mu B-k_{\mathrm{B}}T_{\mathrm{N}}\delta_{\mathrm{A}}}{k_{\mathrm{B}}T}
\end{aligned}
$$

2つの式は対称なので，解は $\delta_{\mathrm{A}}=\delta_{\mathrm{B}}=\delta$ です。この $\delta$ について解き，$M=n\mu\delta$ を使うと，

$$
\finalanswer{\chi=\frac{\mu_0n\mu^2(1-m_{\mathrm{s}}^{\,2})}{k_{\mathrm{B}}\left[T+(1-m_{\mathrm{s}}^{\,2})T_{\mathrm{N}}\right]}}
$$

となります。$T=T_{\mathrm{N}}$ では $m_{\mathrm{s}}=0$ です。$T\to0$ では $m_{\mathrm{s}}\to1$ となり，分子が0に近づきます。

$$
\begin{aligned}
&\finalanswer{\chi(T_{\mathrm{N}})=\frac{\mu_0n\mu^2}{2k_{\mathrm{B}}T_{\mathrm{N}}}}\\
&\finalanswer{\chi\to0\quad(T\to0)}
\end{aligned}
$$

となります。$T=T_{\mathrm{N}}$ での値は，(3) の式で $T=T_{\mathrm{N}}$ とおいた値と一致します。したがって，磁化率は $T_{\mathrm{N}}$ で発散せず，折れ曲がった極大をとります。その様子を図に示します。

<!-- FIGURE solution (4): 横軸 T/T_N（0〜3），縦軸 χ（任意単位）。T > T_N では χ ∝ 1/(T + T_N) の減少する曲線を実線で描く。T < T_N では，T = 0 で 0 から始まり，T_N に向かって増えて，T_N で上の曲線に連続につながる曲線を描く。T = T_N で尖った極大になるようにし，縦の破線を引いて「T_N」とラベルする。比較のため，強磁性のキュリー・ワイス則 1/(T − T_C) の形を，T_C = T_N として細い点線で T > T_N の範囲に描き，T_N で発散する様子を示す。 -->

===== FILE: 06solid_state/10/10_060.md =====
---
tags:
  - 発展
---

# スピン波

## 問題
間隔 $a$ で一直線上に並んだ $N$ 個のスピンからなる強磁性体を考え，周期境界条件 $\boldsymbol{S}_{n+N}=\boldsymbol{S}_n$ を課す。スピン演算子 $\boldsymbol{S}_n$ は $\hbar$ を単位とした無次元の量とし，$[S_n^x,S_m^y]=i\delta_{nm}S_n^z$ と，その添字 $x,y,z$ を巡回させた交換関係を満たす。各スピンの大きさを $S$ とする。ハミルトニアンは

$$
H=-J\sum_{n=1}^{N}\boldsymbol{S}_n\cdot\boldsymbol{S}_{n+1}
$$

で，$J>0$ である。演算子の時間変化は $\dfrac{\mathrm{d}\boldsymbol{S}_n}{\mathrm{d}t}=\dfrac{i}{\hbar}[H,\boldsymbol{S}_n]$ で与えられる。基底状態ではすべてのスピンが $+z$ 方向を向いている。

スピン波を量子化した粒子をマグノンとよぶ。マグノンは化学ポテンシャル0のボース分布に従い，1個あたり全スピンの $z$ 成分を1だけ減らす。必要なら $\displaystyle\int_0^\infty\frac{x^{1/2}}{e^x-1}\,\mathrm{d}x=\frac{\sqrt{\pi}}{2}\zeta\!\left(\frac{3}{2}\right)$ を用いてよい。以下の問いに答えよ。

(1) $\hbar\dfrac{\mathrm{d}\boldsymbol{S}_n}{\mathrm{d}t}=J\,\boldsymbol{S}_n\times(\boldsymbol{S}_{n-1}+\boldsymbol{S}_{n+1})$ となることを示せ。

(2) 基底状態からのずれが小さく，$S_n^z\approx S$ とみなせるとする。$S_n^x,S_n^y$ の1次まで残して (1) を線形化せよ。さらに $S_n^x=u\,e^{i(kna-\omega t)}$，$S_n^y=v\,e^{i(kna-\omega t)}$（$u,v$ は定数，$\omega\ge0$）とおいて，分散関係 $\hbar\omega(k)$ と比 $v/u$ を求めよ。

(3) $|k|a\ll1$ での $\hbar\omega$ を求め，$\hbar\omega=Dk^2$ と書いたときの $D$ を求めよ。また，格子定数 $a$ の3次元の単純立方格子では，同様の計算で $\hbar\omega=2JS\sum_{\alpha=x,y,z}(1-\cos k_\alpha a)$ となる。この場合の $|\boldsymbol{k}|a\ll1$ での $D$ を求めよ。

(4) 3次元の単純立方格子で，$k_{\mathrm{B}}T\ll JS$ の低温を考える。$k_{\mathrm{B}}$ はボルツマン定数，$T$ は温度である。(3) の $\hbar\omega=Dk^2$ を用い，$|\boldsymbol{k}|$ についての積分の上限を $\infty$ にしてよいとする。単位体積あたりのマグノン数を求め，絶対零度の磁化 $M(0)$ からの磁化の減少の割合 $\dfrac{M(0)-M(T)}{M(0)}$ を，$S$，$J$，$k_{\mathrm{B}}T$ で表せ。

---

## 解答・解説

### (1)
$H$ のうち $\boldsymbol{S}_n$ を含むのは $-J\boldsymbol{S}_n\cdot\boldsymbol{h}_n$ だけです。ここで $\boldsymbol{h}_n=\boldsymbol{S}_{n-1}+\boldsymbol{S}_{n+1}$ で，$\boldsymbol{h}_n$ は $\boldsymbol{S}_n$ と交換します。交換関係は $[S_n^b,S_n^a]=i\varepsilon_{bac}S_n^c$ とまとめて書けます。$\varepsilon_{bac}$ は完全反対称な記号です。これを使って，成分 $a$ の時間変化を計算します。

$$
\begin{aligned}
\frac{i}{\hbar}[H,S_n^a]&=\frac{i}{\hbar}(-J)h_n^b\,[S_n^b,S_n^a]\\
&=\frac{J}{\hbar}\varepsilon_{bac}h_n^bS_n^c\\
&=\frac{J}{\hbar}\left(\boldsymbol{S}_n\times\boldsymbol{h}_n\right)_a
\end{aligned}
$$

ここで $\varepsilon_{bac}=\varepsilon_{acb}$ を使いました。よって，

$$
\finalanswer{\hbar\frac{\mathrm{d}\boldsymbol{S}_n}{\mathrm{d}t}=J\,\boldsymbol{S}_n\times(\boldsymbol{S}_{n-1}+\boldsymbol{S}_{n+1})}
$$

となります。各スピンは，両隣のスピンがつくる有効的な磁場のまわりを歳差運動します。

### (2)
外積の $x$，$y$ 成分を書き，$z$ 成分をすべて $S$ で置き換えます。$x,y$ 成分どうしの積は2次なので落とします。

$$
\begin{aligned}
\hbar\frac{\mathrm{d}S_n^x}{\mathrm{d}t}&=JS\left(2S_n^y-S_{n-1}^y-S_{n+1}^y\right)\\
\hbar\frac{\mathrm{d}S_n^y}{\mathrm{d}t}&=-JS\left(2S_n^x-S_{n-1}^x-S_{n+1}^x\right)
\end{aligned}
$$

仮定した解を代入すると，$2-e^{ika}-e^{-ika}=2(1-\cos ka)$ が現れます。

$$
\begin{aligned}
-i\hbar\omega\,u&=2JS(1-\cos ka)\,v\\
-i\hbar\omega\,v&=-2JS(1-\cos ka)\,u
\end{aligned}
$$

2つの式から $v$ を消去すると $(\hbar\omega)^2=[2JS(1-\cos ka)]^2$ となるので，

$$
\begin{aligned}
&\finalanswer{\hbar\omega=2JS(1-\cos ka)=4JS\sin^2\frac{ka}{2}}\\
&\finalanswer{\frac{v}{u}=-i}
\end{aligned}
$$

となります。$u$ を実数にとると $S_n^x=u\cos(kna-\omega t)$，$S_n^y=u\sin(kna-\omega t)$ です。各スピンは $z$ 軸のまわりに同じ半径で回り，隣どうしで位相が $ka$ ずつずれます。その様子を図に示します。

<!-- FIGURE solution (2): 横一列に並んだ 8 個ほどの格子点から，それぞれ上向きに傾いた矢印（スピン）を描く。各矢印の先端は，その点を通る鉛直軸のまわりの小さな円（破線，斜めから見た楕円）の上にあり，先端の円上の位置が左から右へ一定の角度ずつずれていく。矢印の先端を結んだ曲線を細い実線で描き，波長 2π/k に相当する長さを寸法線で示す。格子間隔に a とラベルする。 -->

### (3)
$|k|a\ll1$ では $1-\cos ka\approx\dfrac{(ka)^2}{2}$ と近似できます。

$$
\finalanswer{\hbar\omega\approx JSa^2k^2,\qquad D=JSa^2}
$$

となります。3次元でも各成分について同じ近似を使うと，$\hbar\omega\approx JSa^2(k_x^2+k_y^2+k_z^2)$ です。

$$
\finalanswer{D=JSa^2\quad(\text{3次元の単純立方格子})}
$$

となります。音響フォノンの $\omega\propto k$ と違い，強磁性体のスピン波は $k^2$ に比例します。また $k\to0$ でエネルギーが0になり，ギャップがありません。

### (4)
マグノン数は，各モードのボース分布を波数空間で積分したものです。$x=Dk^2/k_{\mathrm{B}}T$ と置き換えると，与えられた積分の形になります。

$$
\begin{aligned}
n_{\mathrm{mag}}&=\int\frac{\mathrm{d}^3k}{(2\pi)^3}\frac{1}{e^{Dk^2/k_{\mathrm{B}}T}-1}\\
&=\frac{1}{4\pi^2}\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}\int_0^\infty\frac{x^{1/2}}{e^x-1}\,\mathrm{d}x\\
&=\frac{\zeta(3/2)}{8\pi^{3/2}}\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}
\end{aligned}
$$

単位体積あたりのスピンの数は $1/a^3$ なので，絶対零度の全スピンの $z$ 成分は単位体積あたり $S/a^3$ です。マグノン1個がこれを1だけ減らすので，減少の割合は $n_{\mathrm{mag}}a^3/S$ です。$D=JSa^2$ を代入すると $a$ が消えて，

$$
\finalanswer{\frac{M(0)-M(T)}{M(0)}=\frac{\zeta(3/2)}{8\pi^{3/2}S}\left(\frac{k_{\mathrm{B}}T}{JS}\right)^{3/2}}
$$

となります。これをブロッホの $T^{3/2}$ 則とよびます。平均場近似では，低温での磁化の減少は指数関数的に小さくなります。実際の強磁性体では，エネルギーの低いスピン波が励起されるため，べき乗でゆっくり減ります。

===== FILE: 06solid_state/10/10_070.md =====
---
tags:
  - 発展
---

# ランダウ反磁性とド・ハース・ファン・アルフェン効果の入口

## 問題
$xy$ 平面内を運動する2次元の電子気体を考える。試料は $L_x\times L_y$ の長方形で，面積を $A=L_xL_y$ とする。電子の質量を $m$，電荷を $-e$（$e>0$）とし，$z$ 方向に一様な磁束密度 $B>0$ をかける。ベクトルポテンシャルを $\boldsymbol{A}=(0,\,Bx,\,0)$ にとると，電子のハミルトニアンは

$$
\hat{H}=\frac{1}{2m}\left[\hat{p}_x^{\,2}+(\hat{p}_y+eBx)^2\right]
$$

である。$y$ 方向には周期境界条件を課す。スピンの自由度は2とし，ゼーマンエネルギーは無視する。サイクロトロン角振動数を $\omega_{\mathrm{c}}=eB/m$ とする。プランク定数を $h=2\pi\hbar$，真空の透磁率を $\mu_0$，ボーア磁子を $\mu_{\mathrm{B}}=\dfrac{e\hbar}{2m}$ とする。以下の問いに答えよ。

(1) 波動関数を $\psi=e^{ik_yy}\varphi(x)$ とおき，$\varphi(x)$ が満たす方程式を求めよ。また，エネルギー固有値 $E_n$（$n=0,1,2,\ldots$）と，$\varphi$ の中心の位置 $x_0$ を $k_y$ で表せ。

(2) $0\le x_0\le L_x$ となる状態だけが試料内にあるとして，1つの準位 $E_n$ に属する単位面積あたりの状態の数 $N_L$ を，スピンを含めて求めよ。

(3) 面密度 $n$ の電子が絶対零度で準位を下から占有する。ちょうど $\nu$ 個（$\nu$ は正の整数）の準位が満たされる磁束密度を $B_\nu$ とする。$1/B_\nu$ の間隔 $\Delta(1/B)$ を $n$ で表せ。また，磁場がないときのフェルミ円の面積 $S_{\mathrm{F}}=\pi k_{\mathrm{F}}^{\,2}$ を用いて $\Delta(1/B)$ を表せ。

(4) 温度 $T$ が $\hbar\omega_{\mathrm{c}}\ll k_{\mathrm{B}}T\ll\mu$ を満たすとする。$\mu$ は化学ポテンシャル，$k_{\mathrm{B}}$ はボルツマン定数である。単位面積あたりのグランドポテンシャルは $\dfrac{\Omega}{A}=N_L\displaystyle\sum_{n=0}^{\infty}\phi(E_n)$ で与えられる。ここで $\phi(E)=-k_{\mathrm{B}}T\ln\left(1+e^{(\mu-E)/k_{\mathrm{B}}T}\right)$ である。ゆっくり変化して無限遠で0になる関数 $F$ に対して成り立つ近似式 $\displaystyle\sum_{n=0}^{\infty}F\!\left(n+\frac{1}{2}\right)\approx\int_0^\infty F(x)\,\mathrm{d}x+\frac{F'(0)}{24}$ を用いて，$\Omega/A$ のうち $B$ に依存する部分を求めよ。さらに，単位面積あたりの磁化 $M=-\dfrac{\partial(\Omega/A)}{\partial B}$ から磁化率 $\chi_{\mathrm{L}}=\dfrac{\mu_0M}{B}$ を求めよ。また，2次元のパウリ常磁性の磁化率 $\chi_{\mathrm{P}}=\mu_0\mu_{\mathrm{B}}^{\,2}D$ との比 $\chi_{\mathrm{L}}/\chi_{\mathrm{P}}$ を求めよ。$D=\dfrac{m}{\pi\hbar^2}$ はスピンを含めた単位面積あたりの状態密度である。

---

## 解答・解説

### (1)
$\hat{H}$ は $y$ を含まないので，$\hat{p}_y$ の固有関数 $e^{ik_yy}$ を掛けた形に分離できます。$\hat{p}_y$ を $\hbar k_y$ に置き換えると，$x$ についての方程式が残ります。

$$
(\hbar k_y+eBx)^2=e^2B^2\left(x+\frac{\hbar k_y}{eB}\right)^2
$$

と書き直し，$e^2B^2/m=m\omega_{\mathrm{c}}^{\,2}$ を使うと，

$$
\finalanswer{\left[-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d}x^2}+\frac{1}{2}m\omega_{\mathrm{c}}^{\,2}(x-x_0)^2\right]\varphi=E\varphi}
$$

となります。これは中心が $x_0$ にずれた調和振動子の方程式なので，

$$
\begin{aligned}
&\finalanswer{E_n=\hbar\omega_{\mathrm{c}}\left(n+\frac{1}{2}\right)}\\
&\finalanswer{x_0=-\frac{\hbar k_y}{eB}}
\end{aligned}
$$

となります。このとびとびの準位をランダウ準位とよびます。エネルギーは $k_y$ によらないので，各準位は大きく縮退しています。

### (2)
周期境界条件から $k_y=2\pi j/L_y$（$j$ は整数）です。$x_0$ が $0$ から $L_x$ までの範囲に入るのは，$k_y$ が長さ $eBL_x/\hbar$ の区間にあるときです。この区間に入る $k_y$ の数にスピンの2を掛けて，面積 $A$ で割ります。

$$
\begin{aligned}
N_LA&=2\cdot\frac{eBL_x/\hbar}{2\pi/L_y}\\
&=\frac{2eBA}{h}
\end{aligned}
$$

より，

$$
\finalanswer{N_L=\frac{2eB}{h}}
$$

となります。これは，1つのスピンあたり磁束 $h/e$ を1本通すごとに状態が1つあることを意味します。

### (3)
$\nu$ 個の準位がちょうど満たされる条件は $n=\nu N_L$ です。これを $1/B$ について解きます。

$$
\frac{1}{B_\nu}=\frac{2e}{hn}\,\nu
$$

$1/B_\nu$ は $\nu$ に比例するので，間隔は一定です。磁場がないとき，スピンを含めると $n=k_{\mathrm{F}}^{\,2}/2\pi$ です。これを使って $n$ を $S_{\mathrm{F}}$ で書き直すと，

$$
\begin{aligned}
&\finalanswer{\Delta\!\left(\frac{1}{B}\right)=\frac{2e}{hn}}\\
&\finalanswer{\Delta\!\left(\frac{1}{B}\right)=\frac{2\pi e}{\hbar S_{\mathrm{F}}}}
\end{aligned}
$$

となります。ランダウ準位とフェルミエネルギーの関係を図に示します。

<!-- FIGURE solution (3): 横軸 B，縦軸 E。原点から直線的に広がるランダウ準位 E_n = ħω_c(n+1/2)（n = 0, 1, 2, 3, 4）を扇状の直線で描く。磁場がないときのフェルミエネルギー E_F の高さに水平な破線を引く。最上位の占有準位が B とともに上がってフェルミ準位を横切るたびに，占有される準位の数が1つ減ることがわかるように，各準位が E_F の線と交わる点に黒丸を置く。横軸に 1/B が等間隔になるように交点が並ぶ様子を注記してもよい。 -->

満たされる準位の数が変わるたびに，全エネルギーと磁化が変化します。そのため，磁化は $1/B$ について周期 $\Delta(1/B)$ で振動します。これがド・ハース・ファン・アルフェン効果です。周期を測るとフェルミ面の断面積が求まります。この式はオンサーガーの関係とよばれ，一般のフェルミ面でも成り立ちます。

### (4)
$F(x)=\phi(\hbar\omega_{\mathrm{c}}x)$ とおいて近似式を使います。$k_{\mathrm{B}}T\gg\hbar\omega_{\mathrm{c}}$ なので，$F$ は $x$ について十分ゆっくり変化します。積分の項は $E=\hbar\omega_{\mathrm{c}}x$ と置き換えて計算します。

$$
\frac{\Omega}{A}\approx\frac{N_L}{\hbar\omega_{\mathrm{c}}}\int_0^\infty\phi(E)\,\mathrm{d}E+\frac{N_L\hbar\omega_{\mathrm{c}}}{24}\phi'(0)
$$

$\dfrac{N_L}{\hbar\omega_{\mathrm{c}}}=\dfrac{m}{\pi\hbar^2}=D$ なので，第1項は磁場のないときの値で，$B$ によりません。第2項では $\phi'(E)$ がフェルミ分布に等しく，$\mu\gg k_{\mathrm{B}}T$ なので $\phi'(0)\approx1$ です。

$$
\begin{aligned}
\frac{\Delta\Omega}{A}&=\frac{1}{24}\cdot\frac{2eB}{h}\cdot\frac{\hbar eB}{m}\\
&=\frac{e^2B^2}{24\pi m}
\end{aligned}
$$

これを $B$ で微分して符号を変えると，$M=-\dfrac{e^2B}{12\pi m}$ です。磁化率は，

$$
\begin{aligned}
&\finalanswer{\frac{\Delta\Omega}{A}=\frac{e^2B^2}{24\pi m}}\\
&\finalanswer{\chi_{\mathrm{L}}=-\frac{\mu_0e^2}{12\pi m}}
\end{aligned}
$$

となります。パウリ常磁性の磁化率は次のように計算できます。

$$
\chi_{\mathrm{P}}=\mu_0\frac{e^2\hbar^2}{4m^2}\cdot\frac{m}{\pi\hbar^2}=\frac{\mu_0e^2}{4\pi m}
$$

よって比は，

$$
\finalanswer{\frac{\chi_{\mathrm{L}}}{\chi_{\mathrm{P}}}=-\frac{1}{3}}
$$

となります。軌道運動の量子化によって，自由電子は弱い反磁性を示します。これがランダウ反磁性です。古典力学では磁場は仕事をしないので，軌道運動による磁化は0になります。この反磁性は量子力学に特有の効果です。

===== FILE: 06solid_state/11/11_010.md =====
---
tags:
  - 基本
---

# 完全導電と完全反磁性

## 問題
金属の伝導電子を，数密度 $n$，電荷 $-e$（$e>0$），質量 $m$ の粒子の集まりとみなす。電気抵抗が完全に0の完全導体では，電子は散乱されず，平均速度 $\boldsymbol{v}$ は $m\dfrac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}=-e\boldsymbol{\mathcal{E}}$ に従うとする。電流密度は $\boldsymbol{j}=-ne\boldsymbol{v}$ である。場はゆっくり変化するとし，変位電流は無視する。マクスウェル方程式は $\nabla\times\boldsymbol{\mathcal{E}}=-\dfrac{\partial\boldsymbol{B}}{\partial t}$，$\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$，$\nabla\cdot\boldsymbol{B}=0$ である。$\mu_0$ は真空の透磁率である。

一方，超伝導体では，転移温度以下で内部の磁場が排除されることが実験で知られている。試料の表面から十分深いところでは，冷却や磁場をかけた順序によらず $\boldsymbol{B}=\boldsymbol{0}$ となる。これをマイスナー効果とよぶ。以下の問いに答えよ。

(1) 完全導体について，$\dfrac{\partial\boldsymbol{j}}{\partial t}$ を $\boldsymbol{\mathcal{E}}$ で表せ。

(2) (1) とマクスウェル方程式を用いて，完全導体の内部で $\nabla^2\dfrac{\partial\boldsymbol{B}}{\partial t}=\dfrac{1}{\lambda^2}\dfrac{\partial\boldsymbol{B}}{\partial t}$ となることを示し，$\lambda$ を求めよ。$\nabla\times(\nabla\times\boldsymbol{X})=\nabla(\nabla\cdot\boldsymbol{X})-\nabla^2\boldsymbol{X}$ を用いてよい。

(3) 完全導体が $x>0$ を占め，その外の $x<0$ には $z$ 方向の一様な磁束密度 $B_{\mathrm{a}}(t)$ があるとする。内部の $\dfrac{\partial B_z}{\partial t}$ を $x$ の関数として求めよ。さらに，次の2つの過程のあとに試料の表面から十分深いところ（$x\gg\lambda$）の $B_z$ を，完全導体と超伝導体のそれぞれについて求めよ。過程 (a) では，外部の磁場が0の状態で試料を転移温度以下に冷やし，その後に外部の磁場を $B_{\mathrm{a}}$ まで上げる。過程 (b) では，常伝導状態で外部の磁場を $B_{\mathrm{a}}$ にして磁場を試料の内部まで一様に浸透させ，その後に試料を転移温度以下に冷やし，最後に外部の磁場を0まで下げる。完全導体は，転移温度で抵抗が0になる物質とする。

(4) 外部の磁場の強さ $H$ に平行に置いた細長い円柱状の超伝導体を考え，表面付近の薄い層は無視する。内部の磁化 $M$ と磁化率 $\chi=M/H$ を求めよ。また，磁場をかけたことによる単位体積あたりのギブズ自由エネルギーの増加 $G_{\mathrm{s}}(H)-G_{\mathrm{s}}(0)$ を，$\mathrm{d}G=-\mu_0M\,\mathrm{d}H$ を用いて求めよ。温度は一定とする。

---

## 解答・解説

### (1)
電流密度を時間で微分し，運動方程式を代入します。

$$
\frac{\partial\boldsymbol{j}}{\partial t}=-ne\frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}=-ne\left(-\frac{e}{m}\boldsymbol{\mathcal{E}}\right)
$$

より，

$$
\finalanswer{\frac{\partial\boldsymbol{j}}{\partial t}=\frac{ne^2}{m}\boldsymbol{\mathcal{E}}}
$$

となります。抵抗のある金属では電場が電流に比例しますが，完全導体では電場が電流の時間変化に比例します。

### (2)
アンペールの法則の両辺を時間で微分してから回転をとり，(1) とファラデーの法則を順に代入します。

$$
\begin{aligned}
\nabla\times\left(\nabla\times\frac{\partial\boldsymbol{B}}{\partial t}\right)&=\mu_0\nabla\times\frac{\partial\boldsymbol{j}}{\partial t}\\
&=\frac{\mu_0ne^2}{m}\nabla\times\boldsymbol{\mathcal{E}}\\
&=-\frac{\mu_0ne^2}{m}\frac{\partial\boldsymbol{B}}{\partial t}
\end{aligned}
$$

左辺に公式を使います。$\nabla\cdot\boldsymbol{B}=0$ なので，左辺は $-\nabla^2\dfrac{\partial\boldsymbol{B}}{\partial t}$ になります。よって，

$$
\begin{aligned}
&\finalanswer{\nabla^2\frac{\partial\boldsymbol{B}}{\partial t}=\frac{1}{\lambda^2}\frac{\partial\boldsymbol{B}}{\partial t}}\\
&\finalanswer{\lambda=\sqrt{\frac{m}{\mu_0ne^2}}}
\end{aligned}
$$

となります。

### (3)
状況は $x$ だけに依存するので，(2) の方程式は $\dfrac{\partial B_z}{\partial t}$ についての常微分方程式になります。その解のうち，$x\to\infty$ で発散しないものを選びます。表面では，磁場の接線成分が連続であることから，外部の値 $\dot{B}_{\mathrm{a}}$ につながります。

$$
\finalanswer{\frac{\partial B_z}{\partial t}(x)=\dot{B}_{\mathrm{a}}\,e^{-x/\lambda}}
$$

となります。深いところでは磁場の時間変化が0なので，完全導体の内部の磁場は，抵抗が0になったときの値に凍結されます。過程 (a) では冷却したときの内部の磁場が0で，過程 (b) では $B_{\mathrm{a}}$ です。超伝導体では，どちらの過程でも磁場が排除されます。

$$
\begin{aligned}
&\finalanswer{\text{完全導体}:\ \text{(a)}\ B_z=0,\quad \text{(b)}\ B_z=B_{\mathrm{a}}}\\
&\finalanswer{\text{超伝導体}:\ \text{(a)}\ B_z=0,\quad \text{(b)}\ B_z=0}
\end{aligned}
$$

となります。過程 (b) の違いを図に示します。

<!-- FIGURE solution (3): 過程 (b) を表す上下2段の模式図。左から右へ「常伝導・外部磁場 B_a」「冷却後」「外部磁場を 0 に」の3コマを並べる。各コマで試料を四角で描き，磁力線を縦の線で描く。上段は完全導体：1コマ目は磁力線が試料を貫く，2コマ目も貫いたまま，3コマ目は外部の磁力線がなくなり試料の内部にだけ磁力線が閉じ込められて残る。下段は超伝導体：1コマ目は貫く，2コマ目で磁力線が試料をよけて外側を回る，3コマ目は試料の内外とも磁力線がない。段の左端に「完全導体」「超伝導体」とラベルする。 -->

完全導体の状態は経過によって変わるので，熱力学的な状態とはいえません。超伝導体の状態は温度と磁場だけで決まるので，熱力学の対象として扱えます。

### (4)
内部では $B=\mu_0(H+M)=0$ なので，

$$
\begin{aligned}
&\finalanswer{M=-H}\\
&\finalanswer{\chi=-1}
\end{aligned}
$$

となります。これは完全反磁性です。自由エネルギーの増加は，$M=-H$ を代入して $H$ について積分すると求まります。

$$
\begin{aligned}
G_{\mathrm{s}}(H)-G_{\mathrm{s}}(0)&=-\mu_0\int_0^HM\,\mathrm{d}H'\\
&=\mu_0\int_0^HH'\,\mathrm{d}H'
\end{aligned}
$$

より，

$$
\finalanswer{G_{\mathrm{s}}(H)-G_{\mathrm{s}}(0)=\frac{\mu_0H^2}{2}}
$$

となります。磁場を排除するには，この分のエネルギーが必要です。そのため，磁場を強くしていくと，ある磁場で常伝導状態のほうが安定になります。

===== FILE: 06solid_state/11/11_020.md =====
---
tags:
  - 標準
---

# ロンドン方程式と磁場侵入長

## 問題
超伝導体の中で，超伝導電流を運ぶ電子の数密度を $n_{\mathrm{s}}$，電荷を $-e$（$e>0$），質量を $m$ とする。超伝導電流の密度 $\boldsymbol{j}$ と磁束密度 $\boldsymbol{B}$ はロンドン方程式

$$
\nabla\times\boldsymbol{j}=-\frac{n_{\mathrm{s}}e^2}{m}\boldsymbol{B}
$$

に従うとする。静的な場を考え，$\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$，$\nabla\cdot\boldsymbol{B}=0$ が成り立つとする。$\mu_0$ は真空の透磁率である。以下の問いに答えよ。

(1) 超伝導体の内部で $\nabla^2\boldsymbol{B}=\dfrac{1}{\lambda_{\mathrm{L}}^{\,2}}\boldsymbol{B}$ となることを示し，$\lambda_{\mathrm{L}}$ を求めよ。$\nabla\times(\nabla\times\boldsymbol{X})=\nabla(\nabla\cdot\boldsymbol{X})-\nabla^2\boldsymbol{X}$ を用いてよい。

(2) 超伝導体が $x>0$ を占め，その外の $x<0$ には $z$ 方向の一様な磁束密度 $B_{\mathrm{a}}$ があるとする。内部の $B_z(x)$ と電流密度 $\boldsymbol{j}(x)$ を求めよ。また，$z$ 方向の単位長さあたりに流れる表面電流 $K=\displaystyle\int_0^\infty j_y\,\mathrm{d}x$ を求めよ。

(3) 厚さ $2d$ の超伝導体の板が $-d<x<d$ を占め，両側に $z$ 方向の磁束密度 $B_{\mathrm{a}}$ があるとする。内部の $B_z(x)$ と，板の中で平均した磁束密度 $\langle B_z\rangle$ を求めよ。また，$d\gg\lambda_{\mathrm{L}}$ と $d\ll\lambda_{\mathrm{L}}$ のそれぞれについて，$\langle B_z\rangle/B_{\mathrm{a}}$ を主要な項まで求めよ。$d\ll\lambda_{\mathrm{L}}$ では $(d/\lambda_{\mathrm{L}})^2$ の項まで求めよ。

(4) 超伝導電子の数密度が $n_{\mathrm{s}}(T)=n\left[1-\left(\dfrac{T}{T_{\mathrm{c}}}\right)^4\right]$ に従うとする。$n$ は定数，$T$ は温度，$T_{\mathrm{c}}$ は転移温度である。$\lambda_{\mathrm{L}}(T)$ を，絶対零度での値 $\lambda_{\mathrm{L}}(0)$ を用いて表せ。また，$T$ が $T_{\mathrm{c}}$ に近いときの $\lambda_{\mathrm{L}}(T)$ を，$1-T/T_{\mathrm{c}}$ の主要な項まで求めよ。

---

## 解答・解説

### (1)
アンペールの法則の回転をとり，ロンドン方程式を代入します。

$$
\begin{aligned}
\nabla\times(\nabla\times\boldsymbol{B})&=\mu_0\nabla\times\boldsymbol{j}\\
&=-\frac{\mu_0n_{\mathrm{s}}e^2}{m}\boldsymbol{B}
\end{aligned}
$$

左辺は，公式と $\nabla\cdot\boldsymbol{B}=0$ から $-\nabla^2\boldsymbol{B}$ です。よって，

$$
\begin{aligned}
&\finalanswer{\nabla^2\boldsymbol{B}=\frac{1}{\lambda_{\mathrm{L}}^{\,2}}\boldsymbol{B}}\\
&\finalanswer{\lambda_{\mathrm{L}}=\sqrt{\frac{m}{\mu_0n_{\mathrm{s}}e^2}}}
\end{aligned}
$$

となります。この方程式には一様な解 $\boldsymbol{B}=$ 一定 $\ne\boldsymbol{0}$ がありません。そのため，磁場は表面から $\lambda_{\mathrm{L}}$ 程度の深さまでしか入れません。

### (2)
$B_z$ は $x$ だけに依存するので，$\dfrac{\mathrm{d}^2B_z}{\mathrm{d}x^2}=\dfrac{B_z}{\lambda_{\mathrm{L}}^{\,2}}$ を解きます。$x\to\infty$ で有限であることと，表面で $B_z=B_{\mathrm{a}}$ となることから，

$$
\finalanswer{B_z(x)=B_{\mathrm{a}}e^{-x/\lambda_{\mathrm{L}}}}
$$

です。電流はアンペールの法則から求まります。$\nabla\times\boldsymbol{B}$ の $y$ 成分は $-\dfrac{\mathrm{d}B_z}{\mathrm{d}x}$ で，ほかの成分は0です。

$$
\finalanswer{\boldsymbol{j}(x)=\frac{B_{\mathrm{a}}}{\mu_0\lambda_{\mathrm{L}}}e^{-x/\lambda_{\mathrm{L}}}\,\boldsymbol{e}_y}
$$

これを $x$ について積分すると，

$$
\finalanswer{K=\frac{B_{\mathrm{a}}}{\mu_0}}
$$

となります。表面電流 $K$ は $\lambda_{\mathrm{L}}$ によりません。表面の薄い層を流れる電流が，内部の磁場をちょうど打ち消しています。

### (3)
板は $x\to-x$ について対称なので，解は偶関数の $\cosh(x/\lambda_{\mathrm{L}})$ です。両面で $B_z=B_{\mathrm{a}}$ となるように係数を決めると，

$$
\finalanswer{B_z(x)=B_{\mathrm{a}}\frac{\cosh(x/\lambda_{\mathrm{L}})}{\cosh(d/\lambda_{\mathrm{L}})}}
$$

です。これを板の厚さ $2d$ で平均します。

$$
\begin{aligned}
\langle B_z\rangle&=\frac{B_{\mathrm{a}}}{2d\cosh(d/\lambda_{\mathrm{L}})}\int_{-d}^{d}\cosh\frac{x}{\lambda_{\mathrm{L}}}\,\mathrm{d}x\\
&=B_{\mathrm{a}}\frac{\lambda_{\mathrm{L}}}{d}\tanh\frac{d}{\lambda_{\mathrm{L}}}
\end{aligned}
$$

より，

$$
\finalanswer{\langle B_z\rangle=B_{\mathrm{a}}\frac{\lambda_{\mathrm{L}}}{d}\tanh\frac{d}{\lambda_{\mathrm{L}}}}
$$

となります。$d\gg\lambda_{\mathrm{L}}$ では $\tanh\to1$ です。$d\ll\lambda_{\mathrm{L}}$ では $\tanh u\approx u-\dfrac{u^3}{3}$ と展開します。

$$
\begin{aligned}
&\finalanswer{\frac{\langle B_z\rangle}{B_{\mathrm{a}}}\approx\frac{\lambda_{\mathrm{L}}}{d}\quad(d\gg\lambda_{\mathrm{L}})}\\
&\finalanswer{\frac{\langle B_z\rangle}{B_{\mathrm{a}}}\approx1-\frac{d^2}{3\lambda_{\mathrm{L}}^{\,2}}\quad(d\ll\lambda_{\mathrm{L}})}
\end{aligned}
$$

となります。2つの場合の磁場の分布を図に示します。

<!-- FIGURE solution (3): 横軸 x（−d から d），縦軸 B_z/B_a（0〜1）。2本の曲線を描く。d = 5λ_L の場合（実線）：両端で 1，内部に入ると急に減って中央ではほぼ 0 になる U 字形。d = 0.5λ_L の場合（破線）：両端で 1，中央でもわずかに下がるだけの浅い U 字形。両端の x = ±d に縦の線を引き，片側の端から内側へ長さ λ_L の寸法線を付ける。 -->

厚い板はほぼ完全反磁性を示しますが，侵入長より薄い膜では磁場がほとんど排除されません。

### (4)
(1) から $\lambda_{\mathrm{L}}\propto n_{\mathrm{s}}^{-1/2}$ です。絶対零度では $n_{\mathrm{s}}=n$ なので，

$$
\finalanswer{\lambda_{\mathrm{L}}(T)=\frac{\lambda_{\mathrm{L}}(0)}{\sqrt{1-(T/T_{\mathrm{c}})^4}}}
$$

となります。$t=T/T_{\mathrm{c}}$ が1に近いときは，$1-t^4=(1-t)(1+t)(1+t^2)$ と因数分解でき，その値は $4(1-t)$ で近似できます。

$$
\finalanswer{\lambda_{\mathrm{L}}(T)\approx\frac{\lambda_{\mathrm{L}}(0)}{2\sqrt{1-T/T_{\mathrm{c}}}}}
$$

となります。転移温度に近づくと超伝導電子が減り，侵入長は $(T_{\mathrm{c}}-T)^{-1/2}$ に比例して発散します。

===== FILE: 06solid_state/11/11_030.md =====
---
tags:
  - 標準
---

# 臨界磁場と熱力学

## 問題
外部の磁場の強さ $H$ に平行に置いた，細長い円柱状の第1種超伝導体を考える。超伝導状態では内部の磁束密度が0で，磁化は $M=-H$ である。常伝導状態の磁化は無視する。単位体積あたりのギブズ自由エネルギー $G(T,H)$ は $\mathrm{d}G=-S\,\mathrm{d}T-\mu_0M\,\mathrm{d}H$ を満たす。$S$ は単位体積あたりのエントロピー，$T$ は温度，$\mu_0$ は真空の透磁率である。

超伝導状態と常伝導状態のギブズ自由エネルギーを $G_{\mathrm{s}}$，$G_{\mathrm{n}}$ とする。$H=H_{\mathrm{c}}(T)$ で2つが等しくなり，$H>H_{\mathrm{c}}$ で常伝導状態になる。$H_{\mathrm{c}}(T_{\mathrm{c}})=0$，$\dfrac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}<0$ とする。$T_{\mathrm{c}}$ は磁場がないときの転移温度である。単位体積あたりの熱容量は $C=T\dfrac{\partial S}{\partial T}$ で定義する。以下の問いに答えよ。

(1) $G_{\mathrm{s}}(T,H)$ を $G_{\mathrm{s}}(T,0)$ と $H$ で表せ。また，$G_{\mathrm{n}}(T)-G_{\mathrm{s}}(T,0)$ を $H_{\mathrm{c}}(T)$ で表せ。

(2) 磁場 $H_{\mathrm{c}}(T)$ の中で起こる転移について，エントロピーの差 $S_{\mathrm{n}}-S_{\mathrm{s}}$ を $H_{\mathrm{c}}$ と $\dfrac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}$ で表せ。また，超伝導状態から常伝導状態に移るときに吸収される単位体積あたりの潜熱 $L$ を求め，$T=T_{\mathrm{c}}$ での値を求めよ。

(3) 磁場がないときの熱容量の差 $C_{\mathrm{s}}-C_{\mathrm{n}}$ を，$H_{\mathrm{c}}$ とその1階・2階の導関数で表せ。また，$T=T_{\mathrm{c}}$ での熱容量の跳び $\Delta C=C_{\mathrm{s}}-C_{\mathrm{n}}$ を求めよ。

(4) 臨界磁場が $H_{\mathrm{c}}(T)=H_0\left[1-\left(\dfrac{T}{T_{\mathrm{c}}}\right)^2\right]$ で表されるとする。$H_0$ は正の定数である。$L$ を $t=T/T_{\mathrm{c}}$ の関数として求め，$T=T_{\mathrm{c}}$ での $\Delta C$ を求めよ。また，$0<T<T_{\mathrm{c}}$ で $C_{\mathrm{s}}=C_{\mathrm{n}}$ となる温度を求めよ。

---

## 解答・解説

### (1)
温度を一定にして，$M=-H$ を使って $H$ について積分します。

$$
\begin{aligned}
G_{\mathrm{s}}(T,H)-G_{\mathrm{s}}(T,0)&=-\mu_0\int_0^HM\,\mathrm{d}H'\\
&=\frac{\mu_0H^2}{2}
\end{aligned}
$$

常伝導状態の自由エネルギーは磁場によりません。$H=H_{\mathrm{c}}$ で $G_{\mathrm{s}}=G_{\mathrm{n}}$ とおくと，

$$
\begin{aligned}
&\finalanswer{G_{\mathrm{s}}(T,H)=G_{\mathrm{s}}(T,0)+\frac{\mu_0H^2}{2}}\\
&\finalanswer{G_{\mathrm{n}}(T)-G_{\mathrm{s}}(T,0)=\frac{\mu_0H_{\mathrm{c}}(T)^2}{2}}
\end{aligned}
$$

となります。臨界磁場を測ると，超伝導状態の凝縮エネルギーが求まります。

### (2)
エントロピーは $S=-\partial G/\partial T$ です。$G_{\mathrm{s}}$ に含まれる $\mu_0H^2/2$ は温度によらないので，$S_{\mathrm{s}}$ は磁場によりません。したがって，(1) の2つ目の式を $T$ で微分すれば差が得られます。

$$
\finalanswer{S_{\mathrm{n}}-S_{\mathrm{s}}=-\mu_0H_{\mathrm{c}}\frac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}}
$$

転移は一定の温度で起こるので，潜熱はエントロピーの差に $T$ を掛けたものです。

$$
\begin{aligned}
&\finalanswer{L=-\mu_0TH_{\mathrm{c}}\frac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}}\\
&\finalanswer{L=0\quad(T=T_{\mathrm{c}})}
\end{aligned}
$$

となります。$\dfrac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}<0$ なので $L>0$ で，超伝導状態のほうがエントロピーが小さく，秩序のある状態です。磁場の中では転移は1次転移ですが，磁場がないとき $T_{\mathrm{c}}$ では潜熱がなく，2次転移になります。

### (3)
磁場がないときの熱容量の差は，(2) のエントロピーの差を $T$ で微分して $T$ を掛けたものです。

$$
\begin{aligned}
C_{\mathrm{s}}-C_{\mathrm{n}}&=T\frac{\mathrm{d}}{\mathrm{d}T}(S_{\mathrm{s}}-S_{\mathrm{n}})\\
&=\mu_0T\frac{\mathrm{d}}{\mathrm{d}T}\left(H_{\mathrm{c}}\frac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}\right)
\end{aligned}
$$

より，

$$
\finalanswer{C_{\mathrm{s}}-C_{\mathrm{n}}=\mu_0T\left[\left(\frac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}\right)^2+H_{\mathrm{c}}\frac{\mathrm{d}^2H_{\mathrm{c}}}{\mathrm{d}T^2}\right]}
$$

となります。$T=T_{\mathrm{c}}$ では $H_{\mathrm{c}}=0$ なので，第2項が消えます。

$$
\finalanswer{\Delta C=\mu_0T_{\mathrm{c}}\left(\frac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}\right)^2_{T=T_{\mathrm{c}}}}
$$

となります。これをラトガースの関係式とよびます。$\Delta C>0$ なので，熱容量は転移温度で超伝導側に跳び上がります。

### (4)
$\dfrac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}=-\dfrac{2H_0t}{T_{\mathrm{c}}}$ を (2) と (3) に代入します。潜熱と転移温度での跳びは，

$$
\begin{aligned}
&\finalanswer{L=2\mu_0H_0^{\,2}t^2(1-t^2)}\\
&\finalanswer{\Delta C=\frac{4\mu_0H_0^{\,2}}{T_{\mathrm{c}}}}
\end{aligned}
$$

となります。熱容量の差は，$\dfrac{\mathrm{d}^2H_{\mathrm{c}}}{\mathrm{d}T^2}=-\dfrac{2H_0}{T_{\mathrm{c}}^{\,2}}$ も使って計算します。

$$
\begin{aligned}
C_{\mathrm{s}}-C_{\mathrm{n}}&=\mu_0T\left[\frac{4H_0^{\,2}t^2}{T_{\mathrm{c}}^{\,2}}-\frac{2H_0^{\,2}(1-t^2)}{T_{\mathrm{c}}^{\,2}}\right]\\
&=\frac{2\mu_0H_0^{\,2}}{T_{\mathrm{c}}}\,t\,(3t^2-1)
\end{aligned}
$$

$0<t<1$ でこれが0になるのは $3t^2=1$ のときなので，

$$
\finalanswer{T=\frac{T_{\mathrm{c}}}{\sqrt{3}}}
$$

となります。熱容量の差の温度依存性を図に示します。

<!-- FIGURE solution (4): 横軸 t = T/T_c（0〜1），縦軸 (C_s − C_n)T_c/(2μ0 H0²)。曲線 t(3t² − 1) を実線で描く。t = 0 で 0，0 < t < 1/√3 で負（極小は t = 1/3 で値 −2/9），t = 1/√3 ≈ 0.577 で 0 を横切り，t = 1 で 2 に達する。t = 1/√3 に縦の点線を引いて目盛りを付け，t = 1 の値 2 に黒丸を置いて「ΔC」と注記する。 -->

低温では，超伝導状態の熱容量が常伝導状態より小さくなります。エネルギーギャップのために励起が抑えられるからです。

===== FILE: 06solid_state/11/11_040.md =====
---
tags:
  - 標準
---

# 磁束の量子化

## 問題
超伝導体の中で，超伝導電流を運ぶ粒子を電荷 $q$，質量 $m^*$ の粒子とみなす。これらの粒子がつくる状態を，1つの巨視的な波動関数 $\psi(\boldsymbol{r})=\sqrt{n_{\mathrm{s}}}\,e^{i\theta(\boldsymbol{r})}$ で表す。$n_{\mathrm{s}}$ は粒子の数密度で一定とし，$\theta$ は実数の位相である。$\psi$ は空間の各点で1つの値をとる。ベクトルポテンシャルを $\boldsymbol{A}$ とすると，電流密度は

$$
\boldsymbol{j}=\frac{q}{2m^*}\left[\psi^*(-i\hbar\nabla-q\boldsymbol{A})\psi+\psi(i\hbar\nabla-q\boldsymbol{A})\psi^*\right]
$$

で与えられる。真空の透磁率を $\mu_0$，プランク定数を $h=2\pi\hbar$ とする。

磁場侵入長より十分厚い超伝導体のリングがあり，その穴を磁束が貫いている（図）。リングの内部で表面から十分深いところを一周する閉じた経路を $C$ とし，$C$ の上では $\boldsymbol{j}=\boldsymbol{0}$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 厚みのあるドーナツ形のリングを斜め上から見た図。リングの穴を上下に貫く磁力線を数本描く。リングの断面の中ほどを一周する閉じた破線を描いて C とラベルし，向きを矢印で示す。リングの表面付近に薄い層があることを細い線で示し，その厚さに λ と注記する。電流の向きは描かない。 -->

(1) $\boldsymbol{j}$ を $n_{\mathrm{s}}$，$\theta$，$\boldsymbol{A}$ で表せ。

(2) (1) の回転をとり，$\nabla\times\nabla\theta=\boldsymbol{0}$ が成り立つ領域でロンドン方程式の形の式を導け。さらに，$\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$ と組み合わせたときの磁場侵入長 $\lambda$ を求めよ。また，$q=-2e$，$m^*=2m$，$n_{\mathrm{s}}=n/2$ のときの $\lambda$ を，$m$，$n$，$e$ で表せ。$e>0$ は素電荷，$m$ は電子の質量である。

(3) 経路 $C$ が囲む磁束 $\Phi=\displaystyle\oint_C\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}$ が，ある整数 $N$ を用いてとびとびの値に限られることを示し，$\Phi$ を $N$，$h$，$q$ で表せ。

(4) 実験で測定された磁束の最小単位は $\Phi_0=2.07\times10^{-15}\ \mathrm{Wb}$ であった。$|q|$ を求め，素電荷 $e=1.602\times10^{-19}\ \mathrm{C}$ の何倍かを答えよ。$h=6.626\times10^{-34}\ \mathrm{J\,s}$ とする。

---

## 解答・解説

### (1)
$\nabla\psi=i\sqrt{n_{\mathrm{s}}}\,e^{i\theta}\nabla\theta$ です。これを使うと，$\psi^*(-i\hbar\nabla-q\boldsymbol{A})\psi$ は $n_{\mathrm{s}}(\hbar\nabla\theta-q\boldsymbol{A})$ になります。もう一方の項はその複素共役で，同じ実数の値をとります。2つを足して $\dfrac{q}{2m^*}$ を掛けると，

$$
\finalanswer{\boldsymbol{j}=\frac{qn_{\mathrm{s}}}{m^*}\left(\hbar\nabla\theta-q\boldsymbol{A}\right)}
$$

となります。$\hbar\nabla\theta-q\boldsymbol{A}$ は粒子1個の運動量にあたり，それを $m^*$ で割ったものが速度です。

### (2)
(1) の回転をとり，$\nabla\times\boldsymbol{A}=\boldsymbol{B}$ と $\nabla\times\nabla\theta=\boldsymbol{0}$ を使います。

$$
\finalanswer{\nabla\times\boldsymbol{j}=-\frac{q^2n_{\mathrm{s}}}{m^*}\boldsymbol{B}}
$$

これはロンドン方程式と同じ形です。11-2 と同じ計算で，アンペールの法則と組み合わせると $\nabla^2\boldsymbol{B}=\boldsymbol{B}/\lambda^2$ が得られます。

$$
\finalanswer{\lambda=\sqrt{\frac{m^*}{\mu_0q^2n_{\mathrm{s}}}}}
$$

$q^2=4e^2$，$m^*=2m$，$n_{\mathrm{s}}=n/2$ を代入すると，$\dfrac{m^*}{q^2n_{\mathrm{s}}}=\dfrac{m}{ne^2}$ です。

$$
\finalanswer{\lambda=\sqrt{\frac{m}{\mu_0ne^2}}}
$$

となります。電子が2個ずつ対をつくっても，侵入長は電子1個ずつで考えた値と変わりません。侵入長からは粒子の電荷を決められないことになります。

### (3)
経路 $C$ の上では $\boldsymbol{j}=\boldsymbol{0}$ なので，(1) から $\hbar\nabla\theta=q\boldsymbol{A}$ です。これを $C$ に沿って一周積分します。

$$
\Phi=\oint_C\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}=\frac{\hbar}{q}\oint_C\nabla\theta\cdot\mathrm{d}\boldsymbol{l}
$$

$\psi$ は1つの値をとるので，一周して戻ったとき位相は $2\pi$ の整数倍しか変わりません。

$$
\oint_C\nabla\theta\cdot\mathrm{d}\boldsymbol{l}=2\pi N\quad(N\ \text{は整数})
$$

これを代入すると，

$$
\finalanswer{\Phi=N\frac{h}{q}}
$$

となります。リングを貫く磁束は $h/|q|$ の整数倍に限られます。リングの穴には超伝導体がないので，そこでは $\nabla\times\nabla\theta=\boldsymbol{0}$ が成り立たなくてもかまいません。

### (4)
最小単位は $N=\pm1$ にあたるので，$|q|=h/\Phi_0$ です。

$$
|q|=\frac{6.626\times10^{-34}}{2.07\times10^{-15}}\ \mathrm{C}
$$

これを計算すると，

$$
\begin{aligned}
&\finalanswer{|q|\approx3.20\times10^{-19}\ \mathrm{C}}\\
&\finalanswer{|q|\approx2e}
\end{aligned}
$$

となります。超伝導電流を運ぶ粒子の電荷は電子2個分です。これは，電子が対をつくって凝縮しているというBCS理論の描像を直接裏づける結果です。

===== FILE: 06solid_state/11/11_050.md =====
---
tags:
  - 発展
---

# ギンツブルグ・ランダウ理論の入口

## 問題
超伝導状態を，複素数の秩序変数 $\psi(\boldsymbol{r})$ で表す。転移温度 $T_{\mathrm{c}}$ の近くで，単位体積あたりの自由エネルギーを

$$
f_{\mathrm{s}}=f_{\mathrm{n}}+\alpha|\psi|^2+\frac{\beta}{2}|\psi|^4+\frac{1}{2m^*}\left|(-i\hbar\nabla-q\boldsymbol{A})\psi\right|^2
$$

とおく。$f_{\mathrm{n}}$ は常伝導状態の自由エネルギー密度，$q$ と $m^*$ は超伝導電流を運ぶ粒子の電荷と質量，$\boldsymbol{A}$ はベクトルポテンシャルである。係数は $\alpha=a(T-T_{\mathrm{c}})$，$\beta>0$ で，$a>0$ と $\beta$ は温度によらない定数である。$T$ は温度とする。

熱力学的臨界磁場 $H_{\mathrm{c}}$ を，$f_{\mathrm{n}}$ と $f_{\mathrm{s}}$ の最小値の差が $\dfrac{\mu_0H_{\mathrm{c}}^{\,2}}{2}$ に等しいことで定義する。$\mu_0$ は真空の透磁率である。電流密度は $\boldsymbol{j}=\dfrac{q\hbar}{2m^*i}\left(\psi^*\nabla\psi-\psi\nabla\psi^*\right)-\dfrac{q^2}{m^*}|\psi|^2\boldsymbol{A}$ で与えられる。$T<T_{\mathrm{c}}$ でコヒーレンス長を $\xi=\dfrac{\hbar}{\sqrt{2m^*|\alpha|}}$ と定義する。以下の問いに答えよ。

(1) $\psi$ が一様で $\boldsymbol{A}=\boldsymbol{0}$ のとき，$f_{\mathrm{s}}$ を最小にする $|\psi|^2=|\psi_0|^2$ を，$T>T_{\mathrm{c}}$ と $T<T_{\mathrm{c}}$ のそれぞれについて求めよ。また，$T<T_{\mathrm{c}}$ での $f_{\mathrm{s}}-f_{\mathrm{n}}$ の最小値と $H_{\mathrm{c}}(T)$ を求めよ。

(2) 単位体積あたりの熱容量を $C=-T\dfrac{\partial^2f}{\partial T^2}$ とする。$T\to T_{\mathrm{c}}$ での跳び $\Delta C=C_{\mathrm{s}}-C_{\mathrm{n}}$ を $a,\beta,T_{\mathrm{c}}$ で表せ。また，(1) の $H_{\mathrm{c}}(T)$ を用いた $\mu_0T_{\mathrm{c}}\left(\dfrac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}\right)^2$ が $\Delta C$ に一致することを確かめよ。

(3) $T<T_{\mathrm{c}}$，$\boldsymbol{A}=\boldsymbol{0}$ で，$\psi$ が実数で $x$ だけに依存するとする。$\psi$ について自由エネルギーの積分 $\displaystyle\int f_{\mathrm{s}}\,\mathrm{d}x$ を極小にする条件から，$\psi(x)$ が満たす微分方程式を求めよ。さらに，常伝導体と接する境界 $x=0$ で $\psi(0)=0$，$x\to\infty$ で $\psi\to\psi_0>0$，$\psi'\to0$ とする。この方程式の両辺に $\psi'$ を掛けて積分する方法を用いて，$x>0$ での $\psi(x)$ を $\psi_0$ と $\xi$ で表せ。

(4) $T<T_{\mathrm{c}}$ で $\psi=\psi_0$ が実数の定数のとき，$\nabla\times\boldsymbol{j}$ を $\boldsymbol{B}=\nabla\times\boldsymbol{A}$ で表せ。それと $\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$ から得られる磁場侵入長 $\lambda$ を，$m^*,q,\beta,\mu_0,\alpha$ で表せ。また，比 $\kappa=\lambda/\xi$ が温度によらないことを示し，$\kappa$ を $m^*,q,\hbar,\beta,\mu_0$ で表せ。

---

## 解答・解説

### (1)
$x=|\psi|^2\ge0$ とおくと，$f_{\mathrm{s}}-f_{\mathrm{n}}=\alpha x+\dfrac{\beta}{2}x^2$ は下に凸な放物線です。頂点の位置は $x=-\alpha/\beta$ です。$T>T_{\mathrm{c}}$ では $\alpha>0$ で頂点が負の側にあるので，$x\ge0$ での最小は $x=0$ です。$T<T_{\mathrm{c}}$ では頂点が正の側にあります。

$$
\begin{aligned}
&\finalanswer{|\psi_0|^2=0\quad(T>T_{\mathrm{c}})}\\
&\finalanswer{|\psi_0|^2=-\frac{\alpha}{\beta}=\frac{a(T_{\mathrm{c}}-T)}{\beta}\quad(T<T_{\mathrm{c}})}
\end{aligned}
$$

となります。頂点の値と臨界磁場の定義から，

$$
\begin{aligned}
&\finalanswer{f_{\mathrm{s}}-f_{\mathrm{n}}=-\frac{\alpha^2}{2\beta}}\\
&\finalanswer{H_{\mathrm{c}}(T)=\frac{a(T_{\mathrm{c}}-T)}{\sqrt{\mu_0\beta}}}
\end{aligned}
$$

となります。秩序変数は $(T_{\mathrm{c}}-T)^{1/2}$ に比例して現れ，臨界磁場は $T_{\mathrm{c}}$ の近くで温度差に比例します。

### (2)
$T<T_{\mathrm{c}}$ での差は $-\dfrac{a^2(T-T_{\mathrm{c}})^2}{2\beta}$ です。これを $T$ で2回微分すると $-\dfrac{a^2}{\beta}$ になります。熱容量の定義に代入して $T\to T_{\mathrm{c}}$ とすると，

$$
\finalanswer{\Delta C=\frac{a^2T_{\mathrm{c}}}{\beta}}
$$

となります。一方，(1) から $\dfrac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}=-\dfrac{a}{\sqrt{\mu_0\beta}}$ なので，

$$
\begin{aligned}
\mu_0T_{\mathrm{c}}\left(\frac{\mathrm{d}H_{\mathrm{c}}}{\mathrm{d}T}\right)^2&=\mu_0T_{\mathrm{c}}\cdot\frac{a^2}{\mu_0\beta}\\
&=\frac{a^2T_{\mathrm{c}}}{\beta}
\end{aligned}
$$

で，$\Delta C$ と一致します。ギンツブルグ・ランダウ理論は，11-3 の熱力学から得たラトガースの関係式を満たしています。

### (3)
$\psi$ が実数なら，積分は $\displaystyle\int\left[\alpha\psi^2+\frac{\beta}{2}\psi^4+\frac{\hbar^2}{2m^*}\psi'^2\right]\mathrm{d}x$ です。$\psi$ を $\psi+\delta\psi$ に変え，$\psi'\delta\psi'$ の項を部分積分して1次の変化を0とおくと，

$$
\finalanswer{-\frac{\hbar^2}{2m^*}\psi''+\alpha\psi+\beta\psi^3=0}
$$

が得られます。両辺に $\psi'$ を掛けると，各項は完全微分になります。$x\to\infty$ の条件で積分定数を決め，$\beta\psi_0^{\,2}=|\alpha|$ を使います。

$$
\begin{aligned}
\frac{\hbar^2}{4m^*}\psi'^2&=-\frac{|\alpha|}{2}\psi^2+\frac{\beta}{4}\psi^4+\frac{|\alpha|}{4}\psi_0^{\,2}\\
&=\frac{|\alpha|}{4\psi_0^{\,2}}\left(\psi_0^{\,2}-\psi^2\right)^2
\end{aligned}
$$

$\dfrac{m^*|\alpha|}{\hbar^2}=\dfrac{1}{2\xi^2}$ なので，$\psi'=\dfrac{\psi_0^{\,2}-\psi^2}{\sqrt{2}\,\xi\psi_0}$ です。$\psi'>0$ の側をとって，$\psi(0)=0$ から積分すると，

$$
\finalanswer{\psi(x)=\psi_0\tanh\frac{x}{\sqrt{2}\,\xi}}
$$

となります。秩序変数の様子を図に示します。

<!-- FIGURE solution (3): 横軸 x/ξ（0〜5），縦軸 ψ/ψ0（0〜1.1）。曲線 tanh(x/(√2 ξ)) を実線で描く。x = 0 で 0 から立ち上がり，x/ξ ≈ 3 でほぼ 1 になる。縦軸 1 に水平な破線を引く。x < 0 の側を薄く塗って「常伝導体」と注記する。x = √2 ξ に縦の点線を引き，そこで ψ/ψ0 = tanh 1 ≈ 0.76 となる点に黒丸を置く。 -->

秩序変数は，境界から $\xi$ 程度の距離で一様な値に回復します。$\xi\propto|\alpha|^{-1/2}$ なので，コヒーレンス長は $T_{\mathrm{c}}$ に向かって $(T_{\mathrm{c}}-T)^{-1/2}$ に比例して発散します。

### (4)
$\psi$ が実数の定数なら，電流密度の第1項は0で，$\boldsymbol{j}=-\dfrac{q^2\psi_0^{\,2}}{m^*}\boldsymbol{A}$ です。回転をとると，

$$
\finalanswer{\nabla\times\boldsymbol{j}=-\frac{q^2\psi_0^{\,2}}{m^*}\boldsymbol{B}}
$$

となり，ロンドン方程式が得られます。11-2 と同じ計算で $\lambda^2=\dfrac{m^*}{\mu_0q^2\psi_0^{\,2}}$ です。これに $\psi_0^{\,2}=|\alpha|/\beta$ を代入すると，

$$
\finalanswer{\lambda=\sqrt{\frac{m^*\beta}{\mu_0q^2|\alpha|}}}
$$

となります。$\lambda$ も $\xi$ も $|\alpha|^{-1/2}$ に比例するので，比をとると $|\alpha|$ が消えます。

$$
\begin{aligned}
\kappa^2=\frac{\lambda^2}{\xi^2}&=\frac{m^*\beta}{\mu_0q^2|\alpha|}\cdot\frac{2m^*|\alpha|}{\hbar^2}\\
&=\frac{2m^{*2}\beta}{\mu_0q^2\hbar^2}
\end{aligned}
$$

より，

$$
\finalanswer{\kappa=\frac{m^*}{\hbar|q|}\sqrt{\frac{2\beta}{\mu_0}}}
$$

となります。これをギンツブルグ・ランダウ・パラメータとよびます。$\kappa<1/\sqrt{2}$ の物質は第1種超伝導体，$\kappa>1/\sqrt{2}$ の物質は磁束が侵入した状態をとる第2種超伝導体になります。

===== FILE: 06solid_state/11/11_060.md =====
---
tags:
  - 発展
---

# ジョセフソン効果の入口

## 問題
2つの超伝導体 1，2 が薄い絶縁層をはさんで接している（図）。それぞれの超伝導状態を，巨視的な波動関数 $\psi_1=\sqrt{n_1}\,e^{i\theta_1}$，$\psi_2=\sqrt{n_2}\,e^{i\theta_2}$ で表す。$n_1,n_2$ は各超伝導体の中の電荷 $q$ の粒子の数，$\theta_1,\theta_2$ は実数の位相である。絶縁層を通した結合を実数の定数 $K$ で表し，

$$
\begin{aligned}
i\hbar\frac{\mathrm{d}\psi_1}{\mathrm{d}t}&=U_1\psi_1+K\psi_2\\
i\hbar\frac{\mathrm{d}\psi_2}{\mathrm{d}t}&=U_2\psi_2+K\psi_1
\end{aligned}
$$

に従うとする。超伝導体 2 に対する超伝導体 1 の電位を $V$ とし，$U_1=\dfrac{qV}{2}$，$U_2=-\dfrac{qV}{2}$ とおく。位相差を $\delta=\theta_2-\theta_1$ とする。外部の回路が粒子を補給するので，常に $n_1=n_2=n$ が保たれるとする。超伝導体 1 から 2 へ流れる電流は，上の方程式から求めた $\dfrac{\mathrm{d}n_1}{\mathrm{d}t}$ を用いて $I=-q\dfrac{\mathrm{d}n_1}{\mathrm{d}t}$ で与えられる。プランク定数を $h=2\pi\hbar$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 横長の長方形を2つ，間に細い縦長の帯をはさんで左右に並べる。左の長方形に「超伝導体 1」と ψ1，右に「超伝導体 2」と ψ2，間の帯に「絶縁層」とラベルする。2つの長方形の外側の端から導線を出し，電源（電池の記号）と電流計につなぐ回路を描く。左右の長方形の間の電位差を V として，左側が + になるように記号を付ける。電流の向きは描かない。 -->

(1) $\dfrac{\mathrm{d}n_1}{\mathrm{d}t}$，$\dfrac{\mathrm{d}n_2}{\mathrm{d}t}$ と $\dfrac{\mathrm{d}\delta}{\mathrm{d}t}$ を求めよ。

(2) 電流を $I=I_{\mathrm{c}}\sin\delta$ と書いたときの $I_{\mathrm{c}}$ を $q,K,n,\hbar$ で表せ。また，$V=0$ のとき $I$ が時間によらないことを示し，$V=0$ で流れうる電流の範囲を求めよ。

(3) 一定の電圧 $V=V_0\ne0$ をかけたとき，$\delta(t)$ と $I(t)$ を求めよ。$t=0$ での位相差を $\delta_0$ とする。また，電流の振動数 $f$ を $|q|$，$V_0$，$h$ で表し，$q=-2e$ のときの比 $f/V_0$ を数値で求めよ。$e=1.602\times10^{-19}\ \mathrm{C}$，$h=6.626\times10^{-34}\ \mathrm{J\,s}$ とする。

(4) 同じ $I_{\mathrm{c}}$ をもつ2つの接合 a，b を超伝導体のリングの中に並列に入れた素子を考える。リングを磁束 $\Phi$ が貫くとき，2つの接合の位相差 $\delta_{\mathrm{a}},\delta_{\mathrm{b}}$ の間には $\delta_{\mathrm{a}}-\delta_{\mathrm{b}}=\dfrac{2\pi\Phi}{\Phi_0}$ が成り立つとする。$\Phi_0=h/|q|$ である。$V=0$ で素子全体に流れる電流 $I=I_{\mathrm{c}}(\sin\delta_{\mathrm{a}}+\sin\delta_{\mathrm{b}})$ を，$\bar{\delta}=\dfrac{\delta_{\mathrm{a}}+\delta_{\mathrm{b}}}{2}$ と $\Phi$ で表せ。また，$V=0$ で流れうる電流の最大値 $I_{\max}$ を $\Phi$ の関数として求めよ。

---

## 解答・解説

### (1)
$\psi_1=\sqrt{n_1}\,e^{i\theta_1}$ を1つ目の方程式に代入し，両辺を $e^{i\theta_1}$ で割ります。$n_1=n_2=n$ を使うと，次のようになります。

$$
\frac{i\hbar\dot{n}_1}{2\sqrt{n}}-\hbar\sqrt{n}\,\dot{\theta}_1=U_1\sqrt{n}+K\sqrt{n}\,e^{i\delta}
$$

虚部と実部を比べると，$\dot{n}_1$ と $\dot{\theta}_1$ が求まります。

$$
\begin{aligned}
\dot{n}_1&=\frac{2Kn}{\hbar}\sin\delta\\
\dot{\theta}_1&=-\frac{U_1}{\hbar}-\frac{K}{\hbar}\cos\delta
\end{aligned}
$$

2つ目の方程式も同じように扱うと，$e^{i\delta}$ の代わりに $e^{-i\delta}$ が現れます。

$$
\begin{aligned}
\dot{n}_2&=-\frac{2Kn}{\hbar}\sin\delta\\
\dot{\theta}_2&=-\frac{U_2}{\hbar}-\frac{K}{\hbar}\cos\delta
\end{aligned}
$$

位相の式の差をとると，$\cos\delta$ の項が打ち消し合います。

$$
\begin{aligned}
&\finalanswer{\frac{\mathrm{d}n_1}{\mathrm{d}t}=\frac{2Kn}{\hbar}\sin\delta}\\
&\finalanswer{\frac{\mathrm{d}n_2}{\mathrm{d}t}=-\frac{2Kn}{\hbar}\sin\delta}\\
&\finalanswer{\frac{\mathrm{d}\delta}{\mathrm{d}t}=\frac{qV}{\hbar}}
\end{aligned}
$$

となります。一方が減るぶん他方が増えるので，粒子は絶縁層を通り抜けて移動しています。

### (2)
電流の定義に (1) の $\dot{n}_1$ を代入すると，$I=-\dfrac{2qKn}{\hbar}\sin\delta$ です。よって，

$$
\finalanswer{I_{\mathrm{c}}=-\frac{2qKn}{\hbar}}
$$

となります。$V=0$ では，(1) から $\dfrac{\mathrm{d}\delta}{\mathrm{d}t}=0$ なので，$\delta$ は一定です。したがって $I=I_{\mathrm{c}}\sin\delta$ も時間によりません。$\delta$ は任意の値をとれるので，

$$
\finalanswer{-|I_{\mathrm{c}}|\le I\le|I_{\mathrm{c}}|}
$$

の範囲の電流が電圧0で流れます。これを直流ジョセフソン効果とよびます。絶縁層があっても，位相差に応じた超伝導電流が抵抗なしに流れます。

### (3)
$V=V_0$ が一定なら，(1) の $\dot{\delta}$ も一定です。積分すると，

$$
\begin{aligned}
&\finalanswer{\delta(t)=\delta_0+\frac{qV_0}{\hbar}t}\\
&\finalanswer{I(t)=I_{\mathrm{c}}\sin\left(\delta_0+\frac{qV_0}{\hbar}t\right)}
\end{aligned}
$$

となります。角振動数は $|q|V_0/\hbar$ なので，振動数は次のとおりです。

$$
\finalanswer{f=\frac{|q|V_0}{h}}
$$

$|q|=2e$ を代入します。

$$
\frac{f}{V_0}=\frac{2\times1.602\times10^{-19}}{6.626\times10^{-34}}\ \mathrm{Hz/V}
$$

これを計算すると，

$$
\finalanswer{\frac{f}{V_0}\approx4.84\times10^{14}\ \mathrm{Hz/V}}
$$

となります。一定の電圧をかけると，電流は平均0で振動します。これが交流ジョセフソン効果です。比 $2e/h$ は物質によらないので，電圧の標準を定めるのに使われています。

### (4)
$\delta_{\mathrm{a}}=\bar{\delta}+\dfrac{\pi\Phi}{\Phi_0}$，$\delta_{\mathrm{b}}=\bar{\delta}-\dfrac{\pi\Phi}{\Phi_0}$ と書けます。正弦関数の和を積に直すと，

$$
\finalanswer{I=2I_{\mathrm{c}}\sin\bar{\delta}\,\cos\frac{\pi\Phi}{\Phi_0}}
$$

となります。$\bar{\delta}$ は自由に選べるので，$|\sin\bar{\delta}|=1$ のとき電流が最大になります。

$$
\finalanswer{I_{\max}=2|I_{\mathrm{c}}|\left|\cos\frac{\pi\Phi}{\Phi_0}\right|}
$$

となります。最大電流の磁束依存性を図に示します。

<!-- FIGURE solution (4): 横軸 Φ/Φ0（−2〜2），縦軸 I_max/|I_c|（0〜2.2）。曲線 2|cos(πΦ/Φ0)| を実線で描く。Φ/Φ0 が整数のとき値 2 の極大，半整数のとき 0 になり，周期 1 で繰り返す。縦軸 2 に水平な点線を引き，隣り合う極大の間に両矢印を描いて「周期 Φ0」と注記する。 -->

最大電流は，磁束が $\Phi_0$ 変わるごとに1周期振動します。$\Phi_0$ はきわめて小さいので，この素子を使うと微弱な磁場を高い感度で測定できます。これが SQUID（超伝導量子干渉素子）です。

===== END =====