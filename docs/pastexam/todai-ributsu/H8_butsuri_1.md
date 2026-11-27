---
title: 東大理物 平成8年度 物理学 第1問：球対称井戸型ポテンシャルの浅い束縛状態とs波散乱の位相のずれ
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成8年度 物理学 第1問：球対称井戸型ポテンシャルの浅い束縛状態とs波散乱の位相のずれ

## 問題

質量 $m$ の粒子が半径 $a$ 深さ $V_0$ の井戸型ポテンシャル

$$
V(r) = \begin{cases} -V_0 & (r \le a) \\ 0 & (r > a) \end{cases}
$$

の中を運動する。次の設問に答えよ。
{: .problem-lead }

<figure class="problem-figure" markdown>
![半径a深さV_0の球対称井戸型ポテンシャルV(r)](../../assets/figures/pastexam-todai-ributsu/H8_butsuri_1-p-light.svg#only-light){ loading=lazy }
![半径a深さV_0の球対称井戸型ポテンシャルV(r)](../../assets/figures/pastexam-todai-ributsu/H8_butsuri_1-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) 波動関数を極座標 $(r, \theta, \phi)$ で

$$
\Psi(r, \theta, \phi) = R_\ell(r) Y_{\ell m}(\theta, \phi)
$$

のように表したとき $R_\ell(r)$ が従う方程式を書け。ただし，ラプラシアンを極座標で書くと

$$
\Delta = \frac{1}{r^2}\frac{\partial}{\partial r} r^2 \frac{\partial}{\partial r} + \frac{\hat{\Lambda}}{r^2}, \qquad \hat{\Lambda} = \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\sin\theta\frac{\partial}{\partial\theta} + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}
$$

のように表される。また，$Y_{\ell m}(\theta, \phi)$ は球面調和関数で演算子 $\hat{\Lambda}$ の固有関数である。

$$
\hat{\Lambda} Y_{\ell m}(\theta, \phi) = -\ell(\ell + 1) Y_{\ell m}(\theta, \phi)
$$

(2) $V_0$ のある値については s 状態（$\ell = 0$）に束縛状態が一つだけあり，その束縛エネルギー $\varepsilon$ は $V_0$ に比べて十分小さい（$0 < \varepsilon \ll V_0$）。

(a) ポテンシャルの深さ $V_0$ を求めよ。

(b) 上の束縛状態で井戸の外（$r > a$）に粒子が存在する確率を計算せよ。

(3) 次に同じポテンシャルによる散乱を考える。各 $\ell$ で，$r$ の十分大きいところで

$$
R_\ell(r) \sim A_\ell \frac{\sin\left(kr - \frac{1}{2}\ell\pi + \delta_\ell\right)}{r}
$$

で表されるとき，$\delta_\ell$ を位相のずれという。(2) と同じ $V_0$ の値について入射エネルギーが $E = \dfrac{9 V_0}{16}$ のとき，s 波（$\ell = 0$）の位相のずれの正接 $\tan\delta_0$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
球対称ポテンシャルに対するシュレーディンガー方程式に変数分離形を代入すると，動径波動関数 $R_\ell(r)$ の常微分方程式が得られます。s 波では $u(r) = r R_0(r)$ とおくことで $u(0) = 0$ の1次元井戸型問題として扱えるため，境界 $r = a$ における対数微分の連続条件から浅い束縛状態の深さ $V_0$，井戸外の存在確率，および散乱の位相のずれ $\tan\delta_0$ をすべて初等的に求めます。
</div>

### (1)

エネルギー固有値を $E$ とすると，定常状態のシュレーディンガー方程式は

$$
\left(-\frac{\hbar^2}{2m}\Delta + V(r)\right)\Psi(r, \theta, \phi) = E\Psi(r, \theta, \phi)
$$

です。ここに $\Psi(r, \theta, \phi) = R_\ell(r) Y_{\ell m}(\theta, \phi)$ と極座標のラプラシアンを代入し，固有値方程式 $\hat{\Lambda} Y_{\ell m} = -\ell(\ell + 1) Y_{\ell m}$ を用います。

$$
\left\{-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}R_\ell}{\mathrm{d}r}\right) - \frac{\ell(\ell + 1)}{r^2}R_\ell\right] + V(r)R_\ell\right\}Y_{\ell m}(\theta, \phi) = E R_\ell(r) Y_{\ell m}(\theta, \phi)
$$

両辺を $Y_{\ell m}(\theta, \phi)$ で割ると，$R_\ell(r)$ が従う動径方程式が得られます。

$$
\finalanswer{-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}R_\ell}{\mathrm{d}r}\right) - \frac{\ell(\ell + 1)}{r^2}R_\ell\right] + V(r)R_\ell(r) = E R_\ell(r)}
$$

### (2)(a)

s 状態すなわち $\ell = 0$ について $u(r) = r R_0(r)$ とおきます。$\dfrac{1}{r^2}\dfrac{\mathrm{d}}{\mathrm{d}r}\left(r^2\dfrac{\mathrm{d}R_0}{\mathrm{d}r}\right) = \dfrac{1}{r}\dfrac{\mathrm{d}^2 u}{\mathrm{d}r^2}$ なので，動径方程式は次の1次元型の方程式になります。

$$
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2 u}{\mathrm{d}r^2} + V(r) u(r) = E u(r)
$$

原点 $r = 0$ で $R_0(r) = u(r)/r$ が発散しないためには境界条件 $u(0) = 0$ が必要です。束縛エネルギーを $\varepsilon > 0$ として $E = -\varepsilon$ とおき，波数パラメータ

$$
K = \frac{\sqrt{2m(V_0 - \varepsilon)}}{\hbar}, \qquad \kappa = \frac{\sqrt{2m\varepsilon}}{\hbar}
$$

を定義します。井戸の内側 $r \le a$ と外側 $r > a$ の解は，$u(0) = 0$ および無限遠で減衰する条件 $u(\infty) = 0$ を課すことで定数 $A, B$ を用いて次のように表されます。

$$
u(r) = \begin{cases} A \sin(K r) & (0 \le r \le a) \\ B e^{-\kappa r} & (r > a) \end{cases}
$$

$r = a$ における $u(r)$ と $u'(r)$ の連続条件をそれぞれ書きます。

$$
\begin{aligned}
A \sin(K a) &= B e^{-\kappa a} \\
A K \cos(K a) &= -\kappa B e^{-\kappa a}
\end{aligned}
$$

第2式を第1式で割ると，束縛エネルギーを決める固有値条件が得られます。

$$
K \cot(K a) = -\kappa
$$

すなわち $\cot(Ka) = -\dfrac{\kappa}{K}$ であり，$\kappa > 0$ より $\cot(Ka) < 0$ が必要です。$Ka$ の各非負整数 $n = 0, 1, 2, \dots$ に対する各区間 $\left(\dfrac{\pi}{2} + n\pi,\ (n + 1)\pi\right)$ に高々1つの束縛状態が現れるため，束縛状態が1つだけ存在するためには $\dfrac{\pi}{2} < Ka < \dfrac{3\pi}{2}$ でなければなりません。

さらに条件 $0 < \varepsilon \ll V_0$ のもとでは $\dfrac{\kappa}{K} = \sqrt{\dfrac{\varepsilon}{V_0 - \varepsilon}} \ll 1$ なので，$\cot(Ka) = -\dfrac{\kappa}{K} \to -0$ となり，$Ka$ は $\dfrac{\pi}{2}$ のごく近傍に位置します。したがって

$$
K a \approx \frac{\pi}{2}
$$

であり，$\varepsilon \ll V_0$ より $K \approx \dfrac{\sqrt{2m V_0}}{\hbar}$ を代入すると次式が得られます。

$$
\frac{\sqrt{2m V_0}}{\hbar} a = \frac{\pi}{2}
$$

これを $V_0$ について解くとポテンシャルの深さが求まります。

$$
\finalanswer{V_0 = \frac{\hbar^2 \pi^2}{8 m a^2}}
$$

### (2)(b)

球面調和関数 $Y_{00}(\theta, \phi) = \dfrac{1}{\sqrt{4\pi}}$ は立体角について規格化されているため，半径 $r$ から $r + \mathrm{d}r$ の球殻内に粒子を見いだす確率は $|R_0(r)|^2 r^2\,\mathrm{d}r = |u(r)|^2\,\mathrm{d}r$ に比例します。したがって井戸の外 $r > a$ に粒子が存在する確率 $P(r > a)$ は次式で与えられます。

$$
P(r > a) = \frac{\displaystyle\int_a^\infty |u(r)|^2\,\mathrm{d}r}{\displaystyle\int_0^a |u(r)|^2\,\mathrm{d}r + \int_a^\infty |u(r)|^2\,\mathrm{d}r}
$$

境界での値 $u_a = u(a)$ を用いて，$A\sin(Ka) = u_a$ および $B e^{-\kappa a} = u_a$ より各領域の積分を厳密に計算します。まず井戸の外側 $r > a$ の積分です。

$$
\begin{aligned}
\int_a^\infty |u(r)|^2\,\mathrm{d}r &= B^2 \int_a^\infty e^{-2\kappa r}\,\mathrm{d}r \\
&= B^2 \frac{e^{-2\kappa a}}{2\kappa} \\
&= \frac{u_a^2}{2\kappa}
\end{aligned}
$$

次に井戸の内側 $0 \le r \le a$ の積分です。半角の公式と境界条件 $\cot(Ka) = -\dfrac{\kappa}{K}$ を用います。

$$
\begin{aligned}
\int_0^a |u(r)|^2\,\mathrm{d}r &= A^2 \int_0^a \sin^2(Kr)\,\mathrm{d}r \\
&= A^2 \left(\frac{a}{2} - \frac{\sin(2Ka)}{4K}\right) \\
&= \frac{u_a^2}{\sin^2(Ka)}\left(\frac{a}{2} - \frac{\sin(Ka)\cos(Ka)}{2K}\right) \\
&= u_a^2 \left[\frac{a}{2}\left(1 + \cot^2(Ka)\right) - \frac{\cot(Ka)}{2K}\right] \\
&= u_a^2 \left[\frac{a}{2}\left(1 + \frac{\kappa^2}{K^2}\right) + \frac{\kappa}{2K^2}\right]
\end{aligned}
$$

したがって全領域の積分は次のように因数分解できます。

$$
\begin{aligned}
\int_0^\infty |u(r)|^2\,\mathrm{d}r &= u_a^2 \left[\frac{1}{2\kappa} + \frac{\kappa}{2K^2} + \frac{a}{2}\left(1 + \frac{\kappa^2}{K^2}\right)\right] \\
&= \frac{u_a^2}{2\kappa}\left(1 + \frac{\kappa^2}{K^2}\right)(1 + \kappa a)
\end{aligned}
$$

ここで $1 + \dfrac{\kappa^2}{K^2} = \dfrac{V_0}{V_0 - \varepsilon}$ です。よって $P(r > a)$ の厳密な表式は次式となります。

$$
P(r > a) = \frac{1 - \dfrac{\varepsilon}{V_0}}{1 + \kappa a}
$$

いま条件 $0 < \varepsilon \ll V_0$ のもとでは，$\kappa a = \dfrac{\sqrt{2m\varepsilon}}{\hbar} a \approx \dfrac{\pi}{2}\sqrt{\dfrac{\varepsilon}{V_0}} \ll 1$ であり，$\dfrac{\varepsilon}{V_0}$ は $(\kappa a)^2$ の高次微小量です。したがって $\sqrt{\varepsilon / V_0}$ の1次まで残せば

$$
\begin{aligned}
P(r > a) &\approx \frac{1}{1 + \kappa a} \\
&\approx 1 - \frac{\pi}{2}\sqrt{\frac{\varepsilon}{V_0}}
\end{aligned}
$$

となり，浅い束縛極限 $\varepsilon/V_0 \to 0$ では $P(r > a) \to 1$ すなわち粒子はほとんど井戸の外側に広がって存在します。

$$
\finalanswer{P(r > a) = \frac{1 - \varepsilon/V_0}{1 + \kappa a} \approx 1 - \frac{\pi}{2}\sqrt{\frac{\varepsilon}{V_0}} \quad \left(\kappa = \frac{\sqrt{2m\varepsilon}}{\hbar}\right)}
$$

### (3)

入射エネルギー $E = \dfrac{9 V_0}{16} > 0$ の s 波散乱状態を考えます。井戸の外側 $r > a$ と内側 $r \le a$ での波数をそれぞれ $k$ および $K'$ とおきます。

$$
k = \frac{\sqrt{2m E}}{\hbar}, \qquad K' = \frac{\sqrt{2m(E + V_0)}}{\hbar}
$$

(2)(a) の結果 $V_0 = \dfrac{\hbar^2 \pi^2}{8 m a^2}$ すなわち $\dfrac{\sqrt{2m V_0}}{\hbar} a = \dfrac{\pi}{2}$ を用いると，$k a$ と $K' a$ は具体的な数値として求まります。

$$
\begin{aligned}
k a &= \sqrt{\frac{E}{V_0}}\cdot\frac{\sqrt{2m V_0}}{\hbar} a \\
&= \sqrt{\frac{9}{16}}\cdot\frac{\pi}{2} \\
&= \frac{3\pi}{8}
\end{aligned}
$$

$$
\begin{aligned}
K' a &= \sqrt{\frac{E + V_0}{V_0}}\cdot\frac{\sqrt{2m V_0}}{\hbar} a \\
&= \sqrt{\frac{25}{16}}\cdot\frac{\pi}{2} \\
&= \frac{5\pi}{8}
\end{aligned}
$$

$u(r) = r R_0(r)$ の解は，井戸の内側 $r \le a$ では $u(0) = 0$ より $u(r) = C \sin(K' r)$，井戸の外側 $r > a$ では $V(r) = 0$ の厳密解として

$$
u(r) = A_0 \sin(k r + \delta_0)
$$

となります。$r = a$ における対数微分 $u'(a)/u(a)$ の連続条件を立てます。

$$
K' \cot(K' a) = k \cot(k a + \delta_0)
$$

両辺の逆数をとって $\tan(ka + \delta_0)$ を求めます。

$$
\tan(k a + \delta_0) = \frac{k}{K'} \tan(K' a)
$$

ここで $\dfrac{k}{K'} = \dfrac{3}{5}$ です。半角の公式より $\tan\dfrac{\pi}{8} = \sqrt{2} - 1$ なので，$\tan\dfrac{3\pi}{8}$ と $\tan\dfrac{5\pi}{8}$ の値は次のようになります。

$$
\begin{aligned}
\tan\frac{3\pi}{8} &= \cot\frac{\pi}{8} \\
&= \sqrt{2} + 1
\end{aligned}
$$

$$
\begin{aligned}
\tan\frac{5\pi}{8} &= -\tan\frac{3\pi}{8} \\
&= -(\sqrt{2} + 1)
\end{aligned}
$$

したがって

$$
\tan\left(\frac{3\pi}{8} + \delta_0\right) = -\frac{3}{5}(\sqrt{2} + 1)
$$

となります。加法定理 $\tan\delta_0 = \tan\bigl((ka + \delta_0) - ka\bigr)$ を用います。$t = \sqrt{2} + 1$ とおくと $t^2 = 3 + 2\sqrt{2}$ であり，$\tan(ka) = t$，$\tan(ka + \delta_0) = -\dfrac{3}{5}t$ を代入して計算します。

$$
\begin{aligned}
\tan\delta_0 &= \frac{\tan(ka + \delta_0) - \tan(ka)}{1 + \tan(ka + \delta_0)\tan(ka)} \\
&= \frac{-\dfrac{3}{5}t - t}{1 - \dfrac{3}{5}t^2} \\
&= \frac{-8t}{5 - 3t^2} \\
&= \frac{-8(\sqrt{2} + 1)}{5 - 3(3 + 2\sqrt{2})} \\
&= \frac{-8(\sqrt{2} + 1)}{-4 - 6\sqrt{2}} \\
&= \frac{4(\sqrt{2} + 1)}{3\sqrt{2} + 2}
\end{aligned}
$$

分母を有理化します。

$$
\begin{aligned}
\tan\delta_0 &= \frac{4(\sqrt{2} + 1)(3\sqrt{2} - 2)}{(3\sqrt{2})^2 - 2^2} \\
&= \frac{4(6 - 2\sqrt{2} + 3\sqrt{2} - 2)}{18 - 4} \\
&= \frac{4(4 + \sqrt{2})}{14} \\
&= \frac{2(4 + \sqrt{2})}{7}
\end{aligned}
$$

$$
\finalanswer{\tan\delta_0 = \frac{2(4 + \sqrt{2})}{7}}
$$
