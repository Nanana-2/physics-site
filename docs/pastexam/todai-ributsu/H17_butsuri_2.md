---
title: 東大理物 平成17年度 物理学 第2問：金属の自由電子気体と熱電子放出
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成17年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成17年度 物理学 第2問：金属の自由電子気体と熱電子放出

## 問題

金属中の伝導電子系をフェルミ・ディラック統計に従う自由電子気体と見なす単純なモデルを考える。図1に示したように，金属内部を表す一辺 $L$ の立方体の箱の中はポテンシャルがゼロで，外部は $V(>0)$ になっているものとする。この中に $N$ 個の電子が存在する。このとき以下の設問に答えよ。ただし，電子の質量を $m$，ボルツマン定数を $k_{\mathrm{B}}$，$\hbar = h/(2\pi)$（$h$ はプランク定数）とする。なお，設問2以降では，$L$ および $N$ が十分に大きいとし，エネルギー準位の分布はほぼ連続と見なしてよい。

<figure class="problem-figure" markdown>
![金属内部の自由電子気体のポテンシャルと分布](../../assets/figures/pastexam-todai-ributsu/H17_butsuri_2-p-light.svg#only-light)
![金属内部の自由電子気体のポテンシャルと分布](../../assets/figures/pastexam-todai-ributsu/H17_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">図1：金属内部のポテンシャルと電子のエネルギー分布（左：$T = 0$，右：$T > 0$）。</figcaption>
</figure>

(1) $V$ が十分に大きいものとし，波動関数 $\psi(x, y, z)$ に周期的境界条件

$$
\psi(x + L, y, z) = \psi(x, y, z), \quad \psi(x, y + L, z) = \psi(x, y, z), \quad \psi(x, y, z + L) = \psi(x, y, z),
$$

を適用することによって，箱の中の電子状態を表わす固有関数と固有エネルギーを求めよ。

(2) 状態密度 $g(\varepsilon)$ を求めよ。状態密度とは，エネルギーが $\varepsilon$ と $\varepsilon + \mathrm{d}\varepsilon$ の範囲にある単位体積あたりの電子状態の数を $g(\varepsilon)\mathrm{d}\varepsilon$ と表したときの $g(\varepsilon)$ である。

(3) 温度 $T = 0$ における化学ポテンシャル（フェルミ準位）$\mu_0$ と，電子の数密度 $n = N/L^3$ との関係を求めよ。

(4) 温度 $T > 0$ では高いエネルギー状態にも有限の確率で電子が分布するので，一部の電子は表面から外部（真空中）に飛び出すことができる。表面に垂直で外向きの方向を $+z$ 軸として，単位面積から単位時間に外部に流れ出す電子の数 $J_n$ を，フェルミ分布関数 $f(\varepsilon)$，電子の $z$ 方向の速度 $v_z$ を含む三次元波数空間での積分として表せ。その際，三次元波数空間の積分範囲を明示せよ。

(5) $k_{\mathrm{B}}T \ll (V - \mu)$（ただし $\mu$ は有限温度での化学ポテンシャル）という近似のもとで設問4の積分を実行することにより，表面から単位時間，単位面積あたりに外部に流れ出す電子の数が

$$
J_n = \frac{4\pi m(k_{\mathrm{B}}T)^2}{(2\pi\hbar)^3}\exp\!\left(-\frac{V - \mu}{k_{\mathrm{B}}T}\right)
$$

となることを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成17年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
周期的境界条件を課した立方体内の自由電子は，離散的な波数ベクトル $\boldsymbol{k}$ をもつ平面波で表されます。箱の一辺 $L$ が十分大きいときは波数空間での和を積分に置き換えることができ，スピンの2重縮退を含めて状態密度やフェルミ準位を計算することができます。

金属表面から真空中へ飛び出せるのは，表面に垂直な方向の運動エネルギーがポテンシャル障壁 $V$ を超える電子だけです。その領域では $\varepsilon - \mu \ge V - \mu \gg k_{\mathrm{B}}T$ となるため，フェルミ分布関数を指数関数で近似して3次元波数積分を各成分の積に分解することができます。
</div>

### (1)

箱の内部ではポテンシャルが $0$ なので，1電子のシュレーディンガー方程式は次式になります。

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)\psi(x, y, z) = \varepsilon\psi(x, y, z)
$$

平面波解 $\psi_{\boldsymbol{k}}(\boldsymbol{r}) = C e^{i(k_x x + k_y y + k_z z)}$ を代入し，周期的境界条件を課します。

$$
e^{ik_x L} = e^{ik_y L} = e^{ik_z L} = 1
$$

したがって，波数ベクトル $\boldsymbol{k} = (k_x, k_y, k_z)$ は整数 $n_x, n_y, n_z$ を用いて次のように離散化されます。

$$
k_x = \frac{2\pi}{L}n_x, \qquad k_y = \frac{2\pi}{L}n_y, \qquad k_z = \frac{2\pi}{L}n_z \qquad (n_x, n_y, n_z = 0, \pm 1, \pm 2, \dots)
$$

箱の体積 $L^3$ にわたる規格化条件 $\int_0^L\int_0^L\int_0^L |\psi_{\boldsymbol{k}}|^2\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z = 1$ より $|C|^2 L^3 = 1$ なので，$C = \dfrac{1}{L^{3/2}}$ です。また各波数 $\boldsymbol{k}$ には上向きと下向きの2つのスピン状態があります。以上より，固有関数と固有エネルギーは次式となります。

$$
\finalanswer{\psi_{\boldsymbol{k}}(\boldsymbol{r}) = \frac{1}{L^{3/2}}e^{i\boldsymbol{k}\cdot\boldsymbol{r}}, \qquad \varepsilon_{\boldsymbol{k}} = \frac{\hbar^2 \boldsymbol{k}^2}{2m} = \frac{2\pi^2\hbar^2}{mL^2}(n_x^2 + n_y^2 + n_z^2) \quad (n_x, n_y, n_z \in \mathbb{Z})}
$$

### (2)

波数空間において1つの波数ベクトル $\boldsymbol{k}$ が占める体積は $\left(\dfrac{2\pi}{L}\right)^3$ です。電子はスピン $1/2$ をもつため，1つの波数 $\boldsymbol{k}$ あたり2つの電子状態が存在します。

エネルギーが $\varepsilon$ 以下，すなわち波数の大きさ $k$ が $k(\varepsilon) = \sqrt{\dfrac{2m\varepsilon}{\hbar^2}}$ 以下である単位体積あたりの電子状態の総数 $G(\varepsilon)$ を計算します。

$$
\begin{aligned}
G(\varepsilon) &= \frac{2}{L^3}\cdot\frac{\dfrac{4\pi}{3}k(\varepsilon)^3}{\left(\dfrac{2\pi}{L}\right)^3} \\
&= \frac{1}{3\pi^2}\left(\frac{2m\varepsilon}{\hbar^2}\right)^{3/2}
\end{aligned}
$$

状態密度 $g(\varepsilon)$ は $G(\varepsilon)$ を $\varepsilon$ で微分して得られます。

$$
\begin{aligned}
g(\varepsilon) &= \frac{\mathrm{d}G(\varepsilon)}{\mathrm{d}\varepsilon} \\
&= \frac{1}{3\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\cdot\frac{3}{2}\varepsilon^{1/2} \\
&= \frac{1}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{\varepsilon}
\end{aligned}
$$

したがって，状態密度 $g(\varepsilon)$ は次式となります。

$$
\finalanswer{g(\varepsilon) = \frac{1}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{\varepsilon} = \frac{m\sqrt{2m\varepsilon}}{\pi^2\hbar^3}}
$$

### (3)

温度 $T = 0$ では，フェルミ分布関数は $\varepsilon < \mu_0$ で $1$，$\varepsilon > \mu_0$ で $0$ です。したがって，電子の数密度 $n = \dfrac{N}{L^3}$ は状態密度 $g(\varepsilon)$ を $0$ から $\mu_0$ まで積分したものに等しくなります。

$$
\begin{aligned}
n &= \int_{0}^{\mu_0} g(\varepsilon)\,\mathrm{d}\varepsilon \\
&= \frac{1}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\int_{0}^{\mu_0} \varepsilon^{1/2}\,\mathrm{d}\varepsilon \\
&= \frac{1}{3\pi^2}\left(\frac{2m\mu_0}{\hbar^2}\right)^{3/2}
\end{aligned}
$$

これを $\mu_0$ について解きます。

$$
\left(\frac{2m\mu_0}{\hbar^2}\right)^{3/2} = 3\pi^2 n
$$

両辺を $2/3$ 乗します。

$$
\frac{2m\mu_0}{\hbar^2} = (3\pi^2 n)^{2/3}
$$

したがって，$\mu_0$ と $n$ の関係は次式となります。

$$
\finalanswer{\mu_0 = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}}
$$

### (4)

波数 $\boldsymbol{k}$ の電子が単位体積あたりに占める状態密度は，スピン縮退度 $2$ を含めて $\dfrac{2}{(2\pi)^3}\,\mathrm{d}k_x\,\mathrm{d}k_y\,\mathrm{d}k_z$ です。温度 $T$ でその状態が占有されている確率はフェルミ分布関数 $f(\varepsilon) = \dfrac{1}{e^{(\varepsilon - \mu)/(k_{\mathrm{B}}T)} + 1}$ です。ここで $\varepsilon = \dfrac{\hbar^2(k_x^2 + k_y^2 + k_z^2)}{2m}$ です。

金属表面から $+z$ 方向に外部へ飛び出すためには，$z$ 方向の速度が正であり，かつ $z$ 方向の運動エネルギーがポテンシャル障壁 $V$ を超えている必要があります。

$$
\frac{1}{2}m v_z^2 = \frac{\hbar^2 k_z^2}{2m} > V, \qquad k_z > 0
$$

すなわち $k_z > \sqrt{\dfrac{2mV}{\hbar^2}}$ となります。一方，$x$ 方向と $y$ 方向の波数 $k_x, k_y$ は表面に平行な運動に対応するため，$-\infty < k_x < \infty$，$-\infty < k_y < \infty$ のすべての値をとることができます。

この領域の電子は単位時間・単位面積あたり $v_z = \dfrac{\hbar k_z}{m}$ の流束で表面を通過するため，外部へ流れ出す電子の数 $J_n$ は次の3次元波数積分で表されます。

$$
\finalanswer{J_n = \frac{2}{(2\pi)^3}\int_{-\infty}^{\infty}\mathrm{d}k_x\int_{-\infty}^{\infty}\mathrm{d}k_y\int_{\sqrt{2mV}/\hbar}^{\infty}\mathrm{d}k_z\, v_z f(\varepsilon)}
$$

### (5)

設問4の積分領域では $k_z > \sqrt{\dfrac{2mV}{\hbar^2}}$ なので，すべての電子のエネルギーは $\varepsilon = \dfrac{\hbar^2(k_x^2 + k_y^2 + k_z^2)}{2m} > V$ を満たします。仮定 $k_{\mathrm{B}}T \ll V - \mu$ より $\dfrac{\varepsilon - \mu}{k_{\mathrm{B}}T} > \dfrac{V - \mu}{k_{\mathrm{B}}T} \gg 1$ なので，フェルミ分布関数 $f(\varepsilon)$ の分母の $1$ を無視して次のように近似することができます。

$$
\begin{aligned}
f(\varepsilon) &= \frac{1}{\exp\!\left(\dfrac{\varepsilon - \mu}{k_{\mathrm{B}}T}\right) + 1} \\
&\simeq \exp\!\left(-\frac{\varepsilon - \mu}{k_{\mathrm{B}}T}\right) \\
&= \exp\!\left(\frac{\mu}{k_{\mathrm{B}}T}\right)\exp\!\left(-\frac{\hbar^2 k_x^2}{2mk_{\mathrm{B}}T}\right)\exp\!\left(-\frac{\hbar^2 k_y^2}{2mk_{\mathrm{B}}T}\right)\exp\!\left(-\frac{\hbar^2 k_z^2}{2mk_{\mathrm{B}}T}\right)
\end{aligned}
$$

これを設問4の積分に代入すると，$k_x, k_y, k_z$ の3つの積分の積に分離されます。

$$
J_n = \frac{2}{(2\pi)^3}\exp\!\left(\frac{\mu}{k_{\mathrm{B}}T}\right)\left(\int_{-\infty}^{\infty} e^{-\frac{\hbar^2 k_x^2}{2mk_{\mathrm{B}}T}}\,\mathrm{d}k_x\right)\left(\int_{-\infty}^{\infty} e^{-\frac{\hbar^2 k_y^2}{2mk_{\mathrm{B}}T}}\,\mathrm{d}k_y\right)\left(\int_{\sqrt{2mV}/\hbar}^{\infty} \frac{\hbar k_z}{m}e^{-\frac{\hbar^2 k_z^2}{2mk_{\mathrm{B}}T}}\,\mathrm{d}k_z\right)
$$

まず $k_x$ と $k_y$ のガウス積分は同じ値になります。

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{-\frac{\hbar^2 k_x^2}{2mk_{\mathrm{B}}T}}\,\mathrm{d}k_x &= \int_{-\infty}^{\infty} e^{-\frac{\hbar^2 k_y^2}{2mk_{\mathrm{B}}T}}\,\mathrm{d}k_y \\
&= \sqrt{\frac{2\pi m k_{\mathrm{B}}T}{\hbar^2}}
\end{aligned}
$$

次に $k_z$ の積分は，$\varepsilon_z = \dfrac{\hbar^2 k_z^2}{2m}$ と置換します。$\mathrm{d}\varepsilon_z = \dfrac{\hbar^2 k_z}{m}\,\mathrm{d}k_z$ より $\dfrac{\hbar k_z}{m}\,\mathrm{d}k_z = \dfrac{1}{\hbar}\,\mathrm{d}\varepsilon_z$ であり，積分区間は $V \le \varepsilon_z < \infty$ になります。

$$
\begin{aligned}
\int_{\sqrt{2mV}/\hbar}^{\infty} \frac{\hbar k_z}{m}e^{-\frac{\hbar^2 k_z^2}{2mk_{\mathrm{B}}T}}\,\mathrm{d}k_z &= \frac{1}{\hbar}\int_{V}^{\infty} e^{-\frac{\varepsilon_z}{k_{\mathrm{B}}T}}\,\mathrm{d}\varepsilon_z \\
&= \frac{1}{\hbar}\left[-k_{\mathrm{B}}T e^{-\frac{\varepsilon_z}{k_{\mathrm{B}}T}}\right]_{V}^{\infty} \\
&= \frac{k_{\mathrm{B}}T}{\hbar}\exp\!\left(-\frac{V}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

以上をすべて掛け合わせます。

$$
\begin{aligned}
J_n &= \frac{2}{(2\pi)^3}\exp\!\left(\frac{\mu}{k_{\mathrm{B}}T}\right)\cdot\frac{2\pi m k_{\mathrm{B}}T}{\hbar^2}\cdot\frac{k_{\mathrm{B}}T}{\hbar}\exp\!\left(-\frac{V}{k_{\mathrm{B}}T}\right) \\
&= \frac{4\pi m(k_{\mathrm{B}}T)^2}{(2\pi\hbar)^3}\exp\!\left(-\frac{V - \mu}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

これで求める表式が得られます。
