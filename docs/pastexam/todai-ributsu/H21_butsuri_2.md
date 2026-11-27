---
title: 東大理物 平成21年度 物理学 第2問：理想フェルミ気体と理想ボース気体
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成21年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成21年度 物理学 第2問：理想フェルミ気体と理想ボース気体

## 問題

フェルミ気体，ボース気体に関して，以下の設問に答えよ。

(1) フェルミオンとボソンの例をそれぞれ一つ挙げよ。

(2) 1粒子のとる，異なる2つの軌道波動関数 $\varphi_a(\boldsymbol{r})$ と $\varphi_b(\boldsymbol{r})$ が存在するとして，2個の同種粒子が，それぞれ $\varphi_a$ または $\varphi_b$ の状態をとるときの2粒子波動関数を考える。フェルミオン2個の場合，ボソン2個の場合のそれぞれに対して，要請される対称性に言及し，可能な波動関数の形を全て示せ。粒子1の位置を $\boldsymbol{r}_1$，粒子2の位置を $\boldsymbol{r}_2$ とせよ。各粒子のスピンについては，各フェルミオンのスピンの大きさは $1/2$ であり，粒子1の上向きスピン状態を $\alpha_1$，下向きスピン状態を $\beta_1$，粒子2についてはそれぞれ $\alpha_2, \beta_2$ とせよ。各ボソンのスピンの大きさは $0$ とせよ。波動関数の規格化はしなくてよい。

次に，粒子のスピンは無視して，以下の設問に答えよ。

(3) 1粒子のとる軌道波動関数は，3次元自由空間における固有状態とする。一辺の長さが $L$ の箱に対して周期的境界条件を採用して，1粒子の固有状態および対応する固有エネルギーを求めよ。これから，状態密度 $D(E)$（エネルギーが $E$ と $E + \mathrm{d}E$ の間にある状態の数が $D(E)\mathrm{d}E$ となるような量）を求めよ。ただし，各粒子の質量を $m(>0)$ とし，最低エネルギー準位をエネルギーの原点とし，また $L$ は十分大きいとせよ。

(4) 同種粒子 $N$ 個からなる理想気体を，設問3で考えた箱の中に入れる。温度 $T = 0$ においてどのような状態をとるかを，フェルミ気体，ボース気体のそれぞれの場合について述べ，全系のエネルギーを求めよ。系のハミルトニアンは

$$
\mathcal{H} = \sum_{\ell=1}^{N} \frac{\boldsymbol{p}_\ell^2}{2m}
$$

（$\boldsymbol{p}_\ell$ は $\ell$ 番目の粒子の運動量）であり，$N$ は十分大きいとせよ。

大正準集合（grand canonical ensemble）における大分配関数 $\Xi(T, \mu)$ は，

$$
\Xi(T, \mu) = \sum_N \sum_j e^{-\beta(E_j - \mu N)}
$$

で与えられる。ただし，$T$ は温度，$\mu$ は化学ポテンシャル，$\beta = 1/(k_{\mathrm{B}}T)$，$k_{\mathrm{B}}$ はボルツマン定数，$E_j$ は $N$ 個の粒子からなる系の $j$ 番目のエネルギー準位（ここでは $N$ によらないと仮定する）。
{: .problem-lead }

(5) 理想フェルミ気体，理想ボース気体のそれぞれについて，大分配関数を1粒子状態に関する積の形（$\Xi = \prod_i \Xi_i$）で求めよ。ただし，各粒子はエネルギー準位 $\varepsilon_1, \varepsilon_2, \cdots$ をもつ1粒子状態に入り，$E_j = \sum_i n_i \varepsilon_i$（ここで，$n_i$ は $i$ 番目の1粒子状態に入る粒子数，$j$ はここでは $n_1, n_2, \cdots$ の組を指定する番号）とせよ。

(6) 理想気体の大正準集合においては，$i$ 番目の1粒子状態に入る粒子数が $n_i$ 個である統計力学的確率分布は

$$
\frac{e^{-\beta(\varepsilon_i - \mu)n_i}}{\sum_n e^{-\beta(\varepsilon_i - \mu)n}}
$$

で与えられる。ここで，分母の和は，各状態に対して許される全ての粒子数の値にわたってとる。これを用いて，統計力学的平均値 $\langle n_i \rangle$ を，理想フェルミ気体，理想ボース気体のそれぞれについて求めよ。また，得られた理想フェルミ気体に対する分布の概形を，エネルギー $\varepsilon_i$ の関数として，$T = 0$ および $0 < k_{\mathrm{B}}T \ll \mu$ に対して描け。

3次元の理想ボース気体は低温においてボース・アインシュタイン凝縮する。
{: .problem-lead }

(7) 全ての1粒子状態 $i$ に対して $\langle n_i \rangle$ が正であるためには，理想ボース気体の化学ポテンシャル $\mu$ はどのような条件を満たさなければならないかを述べよ。最低エネルギー準位を $0$ とせよ。また，理想ボース気体に対する $\langle n_i \rangle$ を，エネルギー $\varepsilon_i$ の関数として $\mu = 0$ および $\mu \neq 0$ に対して概形を描け。ボース・アインシュタイン凝縮している場合，$\mu$ の値はいくらになるべきかを，理由とともに述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成21年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
同種粒子を区別できない量子力学では，粒子交換に対する波動関数の対称性によって，1つの1粒子状態に入れる粒子数の上限が決まります。フェルミオンは0個か1個に限られ，ボソンは任意の非負整数個をとることができます。

全粒子数を固定すると各状態の占有数に総和の拘束がつきますが，大正準集合では粒子数の和をすべてとるため，大分配関数が1粒子状態ごとの独立な積に分解されます。これにより，平均占有数と低温での振る舞いを1粒子準位ごとに計算することができます。
</div>

### (1)

半整数スピンをもつフェルミオンの例は電子であり，整数スピンをもつボソンの例は光子です。ほかにもフェルミオンには陽子や中性子や ${}^3\mathrm{He}$ 原子があり，ボソンには ${}^4\mathrm{He}$ 原子やパイ中間子があります。

- フェルミオンの例：電子
- ボソンの例：光子

### (2)

同種粒子の2粒子波動関数 $\Psi(1, 2)$ には，粒子1と粒子2の座標とスピンを同時に入れ替える交換操作に対して，フェルミオンでは反対称 $\Psi(2, 1) = -\Psi(1, 2)$，ボソンでは対称 $\Psi(2, 1) = +\Psi(1, 2)$ であることが要請されます。

まずフェルミオン2個の場合を考えます。軌道部分とスピン部分の積で波動関数を作ると，一方が対称でもう一方が反対称のときに全体が反対称になります。2つの軌道 $\varphi_a, \varphi_b$ から作られる対称な軌道波動関数は3通り，反対称な軌道波動関数は1通りです。また，スピン $1/2$ の2粒子から作られる対称なスピン状態は3通り，反対称なスピン状態は1通りです。したがって，可能な2粒子波動関数は次の6通りです。

- 軌道が対称でスピンが反対称の3通り：
  - $\varphi_a(\boldsymbol{r}_1)\varphi_a(\boldsymbol{r}_2)(\alpha_1\beta_2 - \beta_1\alpha_2)$
  - $\varphi_b(\boldsymbol{r}_1)\varphi_b(\boldsymbol{r}_2)(\alpha_1\beta_2 - \beta_1\alpha_2)$
  - $\bigl(\varphi_a(\boldsymbol{r}_1)\varphi_b(\boldsymbol{r}_2) + \varphi_b(\boldsymbol{r}_1)\varphi_a(\boldsymbol{r}_2)\bigr)(\alpha_1\beta_2 - \beta_1\alpha_2)$
- 軌道が反対称でスピンが対称の3通り：
  - $\bigl(\varphi_a(\boldsymbol{r}_1)\varphi_b(\boldsymbol{r}_2) - \varphi_b(\boldsymbol{r}_1)\varphi_a(\boldsymbol{r}_2)\bigr)\alpha_1\alpha_2$
  - $\bigl(\varphi_a(\boldsymbol{r}_1)\varphi_b(\boldsymbol{r}_2) - \varphi_b(\boldsymbol{r}_1)\varphi_a(\boldsymbol{r}_2)\bigr)\beta_1\beta_2$
  - $\bigl(\varphi_a(\boldsymbol{r}_1)\varphi_b(\boldsymbol{r}_2) - \varphi_b(\boldsymbol{r}_1)\varphi_a(\boldsymbol{r}_2)\bigr)(\alpha_1\beta_2 + \beta_1\alpha_2)$

次にボソン2個の場合を考えます。スピンの大きさは $0$ なのでスピン自由度はなく，軌道波動関数そのものが粒子交換に対して対称でなければなりません。可能な2粒子波動関数は次の3通りです。

- $\varphi_a(\boldsymbol{r}_1)\varphi_a(\boldsymbol{r}_2)$
- $\varphi_b(\boldsymbol{r}_1)\varphi_b(\boldsymbol{r}_2)$
- $\varphi_a(\boldsymbol{r}_1)\varphi_b(\boldsymbol{r}_2) + \varphi_b(\boldsymbol{r}_1)\varphi_a(\boldsymbol{r}_2)$

### (3)

1粒子のシュレーディンガー方程式は $-\dfrac{\hbar^2}{2m}\nabla^2\varphi(\boldsymbol{r}) = E\varphi(\boldsymbol{r})$ です。一辺 $L$ の箱に対する周期的境界条件 $\varphi(x + L, y, z) = \varphi(x, y, z)$ などを課すと，波数ベクトル $\boldsymbol{k} = (k_x, k_y, k_z)$ は整数 $n_x, n_y, n_z$ を用いて次のように離散化されます。

$$
k_x = \frac{2\pi}{L}n_x, \qquad k_y = \frac{2\pi}{L}n_y, \qquad k_z = \frac{2\pi}{L}n_z \qquad (n_x, n_y, n_z = 0, \pm 1, \pm 2, \dots)
$$

これに対応する規格化された1粒子の固有状態と固有エネルギーは次式になります。

$$
\varphi_{\boldsymbol{k}}(\boldsymbol{r}) = \frac{1}{L^{3/2}}e^{i\boldsymbol{k}\cdot\boldsymbol{r}}, \qquad E_{\boldsymbol{k}} = \frac{\hbar^2 \boldsymbol{k}^2}{2m} = \frac{2\pi^2\hbar^2}{mL^2}(n_x^2 + n_y^2 + n_z^2)
$$

次に状態密度 $D(E)$ を求めます。波数空間において1つの1粒子状態が占める体積は $\left(\dfrac{2\pi}{L}\right)^3$ です。スピンは無視しているので縮退因子は $1$ となります。$L$ が十分大きいとき，エネルギーが $E$ 以下，すなわち波数の大きさ $k$ が $k(E) = \sqrt{\dfrac{2mE}{\hbar^2}}$ 以下である状態の総数 $\Omega(E)$ は，波数空間での半径 $k(E)$ の球の体積を1状態あたりの体積で割って求めることができます。

$$
\begin{aligned}
\Omega(E) &= \frac{\dfrac{4\pi}{3}k(E)^3}{\left(\dfrac{2\pi}{L}\right)^3} \\
&= \frac{L^3}{6\pi^2}\left(\frac{2mE}{\hbar^2}\right)^{3/2}
\end{aligned}
$$

状態密度 $D(E)$ は $\Omega(E)$ を $E$ で微分して得られます。

$$
\begin{aligned}
D(E) &= \frac{\mathrm{d}\Omega(E)}{\mathrm{d}E} \\
&= \frac{L^3}{6\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \cdot \frac{3}{2}E^{1/2} \\
&= \frac{L^3}{4\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}
\end{aligned}
$$

したがって，固有状態，固有エネルギー，状態密度は次式となります。

$$
\finalanswer{\varphi_{\boldsymbol{k}}(\boldsymbol{r}) = \frac{1}{L^{3/2}}e^{i\boldsymbol{k}\cdot\boldsymbol{r}}, \quad E_{\boldsymbol{k}} = \frac{\hbar^2 \boldsymbol{k}^2}{2m} \ \left(\boldsymbol{k} = \frac{2\pi}{L}\boldsymbol{n},\ \boldsymbol{n}\in\mathbb{Z}^3\right), \quad D(E) = \frac{L^3}{4\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}}
$$

### (4)

まずフェルミ気体の場合を考えます。パウリの排他原理により，1つの1粒子状態には最大1個の粒子しか入ることができません。そのため $T = 0$ では，エネルギーの低い1粒子状態から順に $N$ 個の粒子が1個ずつ詰まり，ある最大エネルギー $E_{\mathrm{F}}$ までの状態がすべて占有されます。この $E_{\mathrm{F}}$ を**フェルミエネルギー**といいます。

総粒子数 $N$ と $E_{\mathrm{F}}$ の関係は，状態密度 $D(E)$ の積分で与えられます。

$$
\begin{aligned}
N &= \int_0^{E_{\mathrm{F}}} D(E)\,\mathrm{d}E \\
&= \frac{L^3}{4\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \int_0^{E_{\mathrm{F}}} E^{1/2}\,\mathrm{d}E \\
&= \frac{L^3}{6\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} E_{\mathrm{F}}^{3/2}
\end{aligned}
$$

これを $E_{\mathrm{F}}$ について解きます。

$$
E_{\mathrm{F}} = \frac{\hbar^2}{2m}\left(\frac{6\pi^2 N}{L^3}\right)^{2/3}
$$

全系のエネルギー $E_{\mathrm{Fermi}}$ は $E D(E)$ を $0$ から $E_{\mathrm{F}}$ まで積分して求めます。

$$
\begin{aligned}
E_{\mathrm{Fermi}} &= \int_0^{E_{\mathrm{F}}} E D(E)\,\mathrm{d}E \\
&= \frac{L^3}{4\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \int_0^{E_{\mathrm{F}}} E^{3/2}\,\mathrm{d}E \\
&= \frac{L^3}{4\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \cdot \frac{2}{5} E_{\mathrm{F}}^{5/2} \\
&= \frac{3}{5} N E_{\mathrm{F}} \\
&= \frac{3\hbar^2 N}{10m}\left(\frac{6\pi^2 N}{L^3}\right)^{2/3}
\end{aligned}
$$

次にボース気体の場合を考えます。ボソンは1つの1粒子状態に何個でも入ることができるため，$T = 0$ ではすべての $N$ 個の粒子が最低エネルギー準位 $\boldsymbol{k} = \boldsymbol{0}$ の状態に入ります。最低エネルギー準位をエネルギーの原点としているので，全系のエネルギー $E_{\mathrm{Bose}}$ は $0$ となります。

$$
\finalanswer{E_{\mathrm{Fermi}} = \frac{3\hbar^2 N}{10m}\left(\frac{6\pi^2 N}{L^3}\right)^{2/3}, \qquad E_{\mathrm{Bose}} = 0}
$$

### (5)

微視的状態は占有数の組 $\{n_1, n_2, \dots\}$ で指定され，全粒子数と全エネルギーは $N = \sum_i n_i$，$E_j = \sum_i n_i\varepsilon_i$ です。大分配関数では全粒子数 $N$ についても和をとるため，各 $n_i$ を互いに独立に許されるすべての値にわたって足し上げることができます。

$$
\begin{aligned}
\Xi(T, \mu) &= \sum_{N=0}^{\infty} \sum_{\sum_i n_i = N} \exp\!\left(-\beta\sum_i (\varepsilon_i - \mu)n_i\right) \\
&= \sum_{n_1} \sum_{n_2} \cdots \prod_i e^{-\beta(\varepsilon_i - \mu)n_i} \\
&= \prod_i \left(\sum_{n_i} e^{-\beta(\varepsilon_i - \mu)n_i}\right)
\end{aligned}
$$

理想フェルミ気体では，各状態に許される粒子数は $n_i = 0, 1$ だけです。

$$
\begin{aligned}
\Xi_i &= \sum_{n_i = 0}^{1} e^{-\beta(\varepsilon_i - \mu)n_i} \\
&= 1 + e^{-\beta(\varepsilon_i - \mu)}
\end{aligned}
$$

理想ボース気体では，各状態に許される粒子数は $n_i = 0, 1, 2, \dots$ です。すべての $i$ で $\varepsilon_i - \mu > 0$ のとき，無限等比級数が収束します。

$$
\begin{aligned}
\Xi_i &= \sum_{n_i = 0}^{\infty} e^{-\beta(\varepsilon_i - \mu)n_i} \\
&= \frac{1}{1 - e^{-\beta(\varepsilon_i - \mu)}}
\end{aligned}
$$

したがって，大分配関数はそれぞれ次式となります。

$$
\finalanswer{\Xi_{\mathrm{Fermi}} = \prod_i \left(1 + e^{-\beta(\varepsilon_i - \mu)}\right), \qquad \Xi_{\mathrm{Bose}} = \prod_i \frac{1}{1 - e^{-\beta(\varepsilon_i - \mu)}}}
$$

### (6)

$x = e^{-\beta(\varepsilon_i - \mu)}$ とおきます。確率分布から平均値 $\langle n_i \rangle$ は次式で与えられます。

$$
\langle n_i \rangle = \frac{\sum_n n x^n}{\sum_n x^n}
$$

理想フェルミ気体では $n = 0, 1$ の和をとります。

$$
\begin{aligned}
\langle n_i \rangle &= \frac{0\cdot 1 + 1\cdot x}{1 + x} \\
&= \frac{x}{1 + x} \\
&= \frac{1}{x^{-1} + 1} \\
&= \frac{1}{e^{\beta(\varepsilon_i - \mu)} + 1}
\end{aligned}
$$

理想ボース気体では $n = 0, 1, 2, \dots$ の和をとります。$0 < x < 1$ のもとで $\sum_{n=0}^{\infty} x^n = \dfrac{1}{1 - x}$ を $x$ で微分すると，$\sum_{n=0}^{\infty} n x^{n-1} = \dfrac{1}{(1 - x)^2}$ となります。両辺に $x$ を掛けて $\sum_{n=0}^{\infty} n x^n = \dfrac{x}{(1 - x)^2}$ を得ます。

$$
\begin{aligned}
\langle n_i \rangle &= \frac{\dfrac{x}{(1 - x)^2}}{\dfrac{1}{1 - x}} \\
&= \frac{x}{1 - x} \\
&= \frac{1}{x^{-1} - 1} \\
&= \frac{1}{e^{\beta(\varepsilon_i - \mu)} - 1}
\end{aligned}
$$

したがって，平均粒子数はそれぞれ次式となります。

$$
\finalanswer{\langle n_i \rangle_{\mathrm{Fermi}} = \frac{1}{e^{\beta(\varepsilon_i - \mu)} + 1}, \qquad \langle n_i \rangle_{\mathrm{Bose}} = \frac{1}{e^{\beta(\varepsilon_i - \mu)} - 1}}
$$

理想フェルミ気体の分布は，$T = 0$ では $\varepsilon_i < \mu$ で $1$，$\varepsilon_i > \mu$ で $0$ の階段関数になります。$0 < k_{\mathrm{B}}T \ll \mu$ では $\varepsilon_i = \mu$ でちょうど $\dfrac{1}{2}$ をとり，$\varepsilon_i = \mu$ の前後で幅 $k_{\mathrm{B}}T$ 程度の範囲でなだらかに $1$ から $0$ へ減少します。概形は次の図のようになります。

<figure class="problem-figure" markdown>
![理想フェルミ気体の平均粒子数の概形](../../assets/figures/pastexam-todai-ributsu/H21_butsuri_2-s1-light.svg#only-light)
![理想フェルミ気体の平均粒子数の概形](../../assets/figures/pastexam-todai-ributsu/H21_butsuri_2-s1-dark.svg#only-dark)
<figcaption markdown="span">理想フェルミ気体の $\langle n_i \rangle$ の概形（破線：$T = 0$，実線：$0 < k_{\mathrm{B}}T \ll \mu$）。</figcaption>
</figure>

### (7)

すべての1粒子状態 $i$ に対して $\langle n_i \rangle = \dfrac{1}{e^{\beta(\varepsilon_i - \mu)} - 1} > 0$ であるためには，分母が正，すなわち $e^{\beta(\varepsilon_i - \mu)} > 1$ である必要があります。これはすべての $i$ に対して $\varepsilon_i - \mu > 0$ となることと同値です。最低エネルギー準位が $\varepsilon_0 = 0$ なので，この条件はすべての準位で成り立つために $\mu < 0$ となります。

$$
\finalanswer{\mu < 0}
$$

$\langle n_i \rangle$ を $\varepsilon_i \ge 0$ の関数として描くと，$\mu < 0$ のときは $\varepsilon_i = 0$ で有限値 $\dfrac{1}{e^{-\beta\mu} - 1}$ をとり，$\varepsilon_i$ の増加とともに単調減少します。$\mu = 0$ のときは $\varepsilon_i \to +0$ で $\langle n_i \rangle \simeq \dfrac{k_{\mathrm{B}}T}{\varepsilon_i} \to +\infty$ と発散します。概形は次の図のようになります。

<figure class="problem-figure" markdown>
![理想ボース気体の平均粒子数の概形](../../assets/figures/pastexam-todai-ributsu/H21_butsuri_2-s2-light.svg#only-light)
![理想ボース気体の平均粒子数の概形](../../assets/figures/pastexam-todai-ributsu/H21_butsuri_2-s2-dark.svg#only-dark)
<figcaption markdown="span">理想ボース気体の $\langle n_i \rangle$ の概形（実線：$\mu = 0$，破線：$\mu < 0$）。</figcaption>
</figure>

次に，ボース・アインシュタイン凝縮しているときの $\mu$ の値を求めます。励起状態にある粒子数の総和 $N_{\mathrm{ex}}$ は，3次元の状態密度 $D(\varepsilon) \propto \sqrt{\varepsilon}$ を用いて次のように評価することができます。

$$
N_{\mathrm{ex}}(T, \mu) = \int_0^\infty \frac{D(\varepsilon)}{e^{\beta(\varepsilon - \mu)} - 1}\,\mathrm{d}\varepsilon
$$

$\mu \le 0$ の範囲で $N_{\mathrm{ex}}(T, \mu)$ は $\mu = 0$ のときに最大値 $N_{\mathrm{ex}}(T, 0)$ をとり，この積分は有限値に収束します。温度が転移温度より低く，全粒子数 $N$ が $N_{\mathrm{ex}}(T, 0)$ を超えると，励起状態に入りきらない粒子 $N_0 = N - N_{\mathrm{ex}}$ が巨視的な個数だけ基底状態 $\varepsilon_0 = 0$ に凝縮します。基底状態の占有数は

$$
N_0 = \frac{1}{e^{-\beta\mu} - 1}
$$

なので，これを $\mu$ について解きます。

$$
\begin{aligned}
e^{-\beta\mu} &= 1 + \frac{1}{N_0} \\
\mu &= -k_{\mathrm{B}}T\ln\!\left(1 + \frac{1}{N_0}\right)
\end{aligned}
$$

ボース・アインシュタイン凝縮では $N_0$ が $N$ と同程度の巨視的な数になるため，$N \to \infty$ の極限で $\mu \simeq -\dfrac{k_{\mathrm{B}}T}{N_0} \to 0$ となります。したがって，ボース・アインシュタイン凝縮している場合，$\mu = 0$ となります。

$$
\finalanswer{\mu = 0}
$$
