---
title: 東大理物 平成13年度 物理学 第1問：1次元井戸型ポテンシャルの束縛状態
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成13年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成13年度 物理学 第1問：1次元井戸型ポテンシャルの束縛状態

## 問題

図のような1次元の井戸型ポテンシャル $U(x)$

$$
U(x) = \begin{cases} -U_0 & |x| \le a \\ 0 & |x| > a \end{cases}
$$

の中での質量 $m$ の粒子の束縛状態（エネルギー $E < 0$）を考える。

<figure class="problem-figure" markdown>
![1次元の井戸型ポテンシャル](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_1-p-light.svg#only-light){ loading=lazy }
![1次元の井戸型ポテンシャル](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_1-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) まず，量子力学の不確定性関係を使ってこの問題を考える。

(a) 粒子がポテンシャル $U$ に束縛されていることから，直感的には粒子の位置の不確定性 $\Delta x$ は $a$ 程度だと考えられる。そこで，$\Delta x = a$ として粒子の運動量の不確定性 $\Delta p$ を求めよ。

(b) 運動量の大きさ $p$ は $\Delta p$ より大きいと考えて，(a) の結果から粒子の束縛状態が存在するためのポテンシャルの深さ $U_0$ にどのような条件が必要と思われるか。

(2) 実は上で求めた束縛状態が存在する条件は正しくなく，どんなに浅いポテンシャルに対しても束縛状態が存在する。

(a) シュレディンガー方程式を使って束縛状態（$E < 0$）の波動関数 $\psi(x)$ を求めよ。その際，エネルギー $E$ と $U_0, a, m$ の関係式を導け。（波動関数の規格化は考えなくてよい。）

(b) 1(b) の結果に反してどのような $U_0$ の値に対しても束縛状態が存在することを示せ。

(c) $U_0 \ll \dfrac{\hbar^2}{ma^2}$ のときに $E$ を求めよ。

(d) (c) の場合に粒子がポテンシャル井戸の外側にいる確率 $P(|x| > a)$ と内側にいる確率 $P(|x| < a)$ の比 $R = P(|x| > a)/P(|x| < a)$ を求めよ。また，これから 1(b) の考え方が正しくなかった理由を述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成13年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，ハイゼンベルクの不確定性関係 $\Delta x\,\Delta p \ge \hbar/2$ に $\Delta x = a$ を当てはめて運動エネルギーの下限を見積もり，全エネルギーが負になるための $U_0$ の条件を導きます。

後半では，ポテンシャルが $U(-x) = U(x)$ と左右対称であることから波動関数を偶関数と奇関数に分け，境界 $x = \pm a$ での接続条件を無次元変数 $\xi = ka$，$\eta = \kappa a$ のグラフの交点として扱います。浅い井戸の極限 $U_0 \ll \hbar^2/(ma^2)$ では $\xi, \eta \ll 1$ の近似でエネルギーと井戸内外の存在確率の比を計算し，波動関数の広がりと位置の不確定性 $\Delta x$ の関係から前半の仮定の誤りを特定します。
</div>

### (1)

#### (a)

位置と運動量の不確定性関係は $\Delta x\,\Delta p \ge \dfrac{\hbar}{2}$ です。$\Delta x = a$ を代入します。

$$
\begin{aligned}
a\,\Delta p &\ge \frac{\hbar}{2} \\
\Delta p &\ge \frac{\hbar}{2a}
\end{aligned}
$$

したがって，運動量の不確定性は $\Delta p$ の下限として次の値になります。

$$
\finalanswer{\Delta p \ge \frac{\hbar}{2a}}
$$

なお，オーダー評価として $\Delta x\,\Delta p \sim \hbar$ を用いると $\Delta p \sim \dfrac{\hbar}{a}$ となります。

#### (b)

運動量の大きさ $p$ が $\Delta p$ より大きいとすると，粒子の運動エネルギー $K = \dfrac{p^2}{2m}$ は次を満たします。

$$
\begin{aligned}
K &= \frac{p^2}{2m} \\
&> \frac{(\Delta p)^2}{2m} \\
&\ge \frac{\hbar^2}{8ma^2}
\end{aligned}
$$

井戸内部でのポテンシャルエネルギーは $-U_0$ なので，束縛状態が $E = K - U_0 < 0$ を満たすためには $U_0 > K$ が必要です。したがって，不確定性関係の素朴な見積もりからは次の条件が必要と考えられます。

$$
\finalanswer{U_0 > \frac{\hbar^2}{8ma^2}}
$$

なお，$\Delta p \sim \dfrac{\hbar}{a}$ を用いた場合は $U_0 > \dfrac{\hbar^2}{2ma^2}$ となります。いずれの見積もりでも，$U_0$ に $\dfrac{\hbar^2}{ma^2}$ 程度の下限があるという結論になります。

### (2)

#### (a)

時間によらない1次元シュレディンガー方程式は次の通りです。

$$
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\psi(x)}{\mathrm{d}x^2} + U(x)\psi(x) = E\psi(x)
$$

束縛状態では $-U_0 < E < 0$ です。正の定数 $k$ と $\kappa$ を次で定めます。

$$
k = \frac{\sqrt{2m(U_0 + E)}}{\hbar}, \qquad \kappa = \frac{\sqrt{-2mE}}{\hbar}
$$

これらを使うと，各領域の方程式は次の形になります。

$$
\begin{aligned}
\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} + k^2\psi &= 0 \qquad (|x| < a) \\
\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} - \kappa^2\psi &= 0 \qquad (|x| > a)
\end{aligned}
$$

ポテンシャルは $U(-x) = U(x)$ を満たすため，固有関数は偶関数 $\psi(-x) = \psi(x)$ と奇関数 $\psi(-x) = -\psi(x)$ に分けることができます。また $|x| \to \infty$ で波動関数が発散しない条件から，$|x| > a$ では $e^{-\kappa|x|}$ の項だけが残ります。

偶関数の場合，任意定数 $A, B$ を用いて波動関数は次の形になります。

$$
\psi(x) = \begin{cases} A\cos(kx) & (|x| \le a) \\ B e^{-\kappa|x|} & (|x| > a) \end{cases}
$$

境界 $x = a$ で $\psi(x)$ と $\dfrac{\mathrm{d}\psi}{\mathrm{d}x}$ が連続になる条件を書きます。

$$
\begin{aligned}
A\cos(ka) &= B e^{-\kappa a} \\
-kA\sin(ka) &= -\kappa B e^{-\kappa a}
\end{aligned}
$$

1つめの式から $B = A\cos(ka)e^{\kappa a}$ です。また2つめの式を1つめの式で割ると，$k\tan(ka) = \kappa$ が得られます。$k$ と $\kappa$ の定義を代入すると，エネルギー $E$ を定める関係式は次の形になります。

$$
\sqrt{U_0 + E}\,\tan\left(\frac{a\sqrt{2m(U_0 + E)}}{\hbar}\right) = \sqrt{-E}
$$

奇関数の場合，任意定数 $C, D$ を用いて波動関数は次の形になります。

$$
\psi(x) = \begin{cases} C\sin(kx) & (|x| \le a) \\ D e^{-\kappa x} & (x > a) \\ -D e^{\kappa x} & (x < -a) \end{cases}
$$

境界 $x = a$ での連続条件は次の通りです。

$$
\begin{aligned}
C\sin(ka) &= D e^{-\kappa a} \\
kC\cos(ka) &= -\kappa D e^{-\kappa a}
\end{aligned}
$$

1つめの式から $D = C\sin(ka)e^{\kappa a}$ となり，2つめの式を1つめの式で割ると $-k\cot(ka) = \kappa$ が得られます。$k$ と $\kappa$ の定義を代入すると次の関係式になります。

$$
-\sqrt{U_0 + E}\,\cot\left(\frac{a\sqrt{2m(U_0 + E)}}{\hbar}\right) = \sqrt{-E}
$$

まとめると，規格化定数を除いた偶状態の波動関数とエネルギーの関係式は次の通りです。

$$
\finalanswer{\psi(x) = \begin{cases} \cos(kx) & (|x| \le a) \\ \cos(ka)e^{-\kappa(|x|-a)} & (|x| > a) \end{cases}, \qquad k\tan(ka) = \kappa}
$$

同様に，奇状態の波動関数とエネルギーの関係式は次の通りです。

$$
\finalanswer{\psi(x) = \begin{cases} \sin(kx) & (|x| \le a) \\ \mathrm{sgn}(x)\sin(ka)e^{-\kappa(|x|-a)} & (|x| > a) \end{cases}, \qquad -k\cot(ka) = \kappa}
$$

ここで $k = \dfrac{\sqrt{2m(U_0 + E)}}{\hbar}$，$\kappa = \dfrac{\sqrt{-2mE}}{\hbar}$，また $\mathrm{sgn}(x)$ は $x > 0$ で $+1$，$x < 0$ で $-1$ をとる符号関数です。

#### (b)

無次元量 $\xi = ka > 0$，$\eta = \kappa a > 0$ を導入します。$k$ と $\kappa$ の定義から，$\xi^2 + \eta^2$ を計算します。

$$
\begin{aligned}
\xi^2 + \eta^2 &= (k^2 + \kappa^2)a^2 \\
&= \frac{2m(U_0 + E) - 2mE}{\hbar^2}a^2 \\
&= \frac{2mU_0 a^2}{\hbar^2}
\end{aligned}
$$

$R = \dfrac{\sqrt{2mU_0}a}{\hbar} > 0$ とおくと，$\xi$ と $\eta$ は第1象限の円弧 $\xi^2 + \eta^2 = R^2$ の上にあります。一方，(a) で得た関係式は偶状態について $\eta = \xi\tan\xi$，奇状態について $\eta = -\xi\cot\xi$ となります。

<figure class="problem-figure" markdown>
![束縛状態のエネルギーを決めるグラフ](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_1-s-light.svg#only-light){ loading=lazy }
![束縛状態のエネルギーを決めるグラフ](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_1-s-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">$\xi\eta$ 平面の第1象限における円弧 $\xi^2 + \eta^2 = R^2$ と曲線 $\eta = \xi\tan\xi$（実線），$\eta = -\xi\cot\xi$（破線）の交点。</figcaption>
</figure>

第1象限で偶状態の曲線 $\eta = \xi\tan\xi$ の $0 < \xi < \dfrac{\pi}{2}$ の枝を考えます。この区間では $\xi\tan\xi$ は $\xi \to 0^+$ で $0$ に近づき，$\xi \to \left(\dfrac{\pi}{2}\right)^-$ で $+\infty$ に単調増加します。一方，円弧 $\eta = \sqrt{R^2 - \xi^2}$ は $\xi = 0$ で $\eta = R > 0$ をとり，$\xi = R$ で $\eta = 0$ まで単調減少します。

差の関数 $g(\xi) = \xi\tan\xi - \sqrt{R^2 - \xi^2}$ は $0 < \xi < \min\left(R, \dfrac{\pi}{2}\right)$ で連続であり，$\xi \to 0^+$ で $g(\xi) \to -R < 0$，区間の右端では $g(\xi) > 0$ となります。中間値の定理より，どんな正の $R$ に対しても，すなわちどんなに小さい $U_0 > 0$ に対しても，この区間に必ず1つの交点が存在します。したがって，$U_0$ の値にかかわらず少なくとも1つの偶の束縛状態が存在します。

#### (c)

$U_0 \ll \dfrac{\hbar^2}{ma^2}$ のとき，$R^2 = \dfrac{2mU_0 a^2}{\hbar^2} \ll 1$ です。$R < \dfrac{\pi}{2}$ なので束縛状態は偶状態が1つだけ存在し，交点は $0 < \xi < R \ll 1$ にあります。$\xi \ll 1$ より $\tan\xi = \xi + O(\xi^3)$ と近似します。

$$
\begin{aligned}
\eta &= \xi\tan\xi \\
&\approx \xi^2
\end{aligned}
$$

これを $\xi^2 + \eta^2 = R^2$ に代入します。

$$
\begin{aligned}
\xi^2 + \xi^4 &\approx R^2 \\
\xi^2 &\approx R^2
\end{aligned}
$$

ここで $\xi^4 \ll \xi^2$ を無視しました。よって $\eta \approx \xi^2 \approx R^2 = \dfrac{2mU_0 a^2}{\hbar^2}$ となります。これより $\kappa = \dfrac{\eta}{a} \approx \dfrac{2mU_0 a}{\hbar^2}$ です。エネルギー $E = -\dfrac{\hbar^2\kappa^2}{2m}$ に代入します。

$$
\begin{aligned}
E &= -\frac{\hbar^2}{2m}\left(\frac{\eta}{a}\right)^2 \\
&\approx -\frac{\hbar^2}{2ma^2}\left(\frac{2mU_0 a^2}{\hbar^2}\right)^2 \\
&= -\frac{2mU_0^2 a^2}{\hbar^2}
\end{aligned}
$$

したがって，浅い井戸における束縛状態のエネルギーは次の通りです。

$$
\finalanswer{E \approx -\frac{2mU_0^2 a^2}{\hbar^2}}
$$

#### (d)

(c) の束縛状態は偶状態なので，規格化前の波動関数を $\psi(x) = \cos(kx)$（$|x| \le a$），$\psi(x) = \cos(ka)e^{-\kappa(|x|-a)}$（$|x| > a$）とします。井戸の内側 $|x| < a$ と外側 $|x| > a$ での $|\psi(x)|^2$ の積分を計算します。

まず内側の積分です。

$$
\begin{aligned}
\int_{-a}^{a} |\psi(x)|^2\,\mathrm{d}x &= 2\int_0^a \cos^2(kx)\,\mathrm{d}x \\
&= \int_0^a \bigl(1 + \cos(2kx)\bigr)\,\mathrm{d}x \\
&= a + \frac{\sin(2ka)}{2k}
\end{aligned}
$$

次に外側の積分です。

$$
\begin{aligned}
\int_{|x| > a} |\psi(x)|^2\,\mathrm{d}x &= 2\cos^2(ka)\int_a^\infty e^{-2\kappa(x-a)}\,\mathrm{d}x \\
&= 2\cos^2(ka)\cdot\frac{1}{2\kappa} \\
&= \frac{\cos^2(ka)}{\kappa}
\end{aligned}
$$

$ka = \xi \ll 1$ なので，$\cos(ka) \approx 1$ および $\dfrac{\sin(2ka)}{2k} \approx a$ と近似します。よって内側の積分は $2a$，外側の積分は $\dfrac{1}{\kappa}$ となります。したがって，存在確率の比 $R$ は次の通りです。

$$
\begin{aligned}
R &= \frac{P(|x| > a)}{P(|x| < a)} \\
&= \frac{\cos^2(ka)}{\kappa\left(a + \dfrac{\sin(2ka)}{2k}\right)} \\
&\approx \frac{1}{2\kappa a} \\
&\approx \frac{\hbar^2}{4mU_0 a^2}
\end{aligned}
$$

$$
\finalanswer{R \approx \frac{\hbar^2}{4mU_0 a^2}}
$$

$U_0 \ll \dfrac{\hbar^2}{ma^2}$ のもとでは $R \gg 1$ となり，粒子はほとんどの時間ポテンシャル井戸の外側に染み出して存在しています。1(b) の考え方では，粒子が井戸の内部 $|x| \le a$ に閉じ込められているとみなして位置の不確定性を $\Delta x = a$ と固定したため，運動エネルギーの下限が $\dfrac{\hbar^2}{ma^2}$ 程度に大きく見積もられてしまいました。実際には，井戸が浅くなるほど波動関数は井戸の外側へ長さ $\dfrac{1}{\kappa} \approx \dfrac{\hbar^2}{2mU_0 a} \gg a$ の範囲まで大きく広がり，$\Delta x \sim \dfrac{1}{\kappa}$ となります。その結果，運動エネルギーは $\dfrac{\hbar^2\kappa^2}{2m} \sim \dfrac{mU_0^2 a^2}{\hbar^2}$ と $U_0^2$ のオーダーまで小さくなり，井戸の内部にいる確率 $P(|x| < a) \approx 2\kappa a$ によるポテンシャルエネルギーの期待値 $-U_0 P(|x| < a) \approx -\dfrac{4mU_0^2 a^2}{\hbar^2}$ が運動エネルギーを常に上回るため，どんなに浅い井戸でも負のエネルギーをもつ束縛状態が存在します。

<aside class="rigor-note" markdown>
(d) のエネルギー収支を確かめます。浅い井戸の極限では $P(|x| < a) \approx 2\kappa a = \dfrac{4mU_0 a^2}{\hbar^2}$ なので，ポテンシャルエネルギーの期待値は $\langle U \rangle \approx -\dfrac{4mU_0^2 a^2}{\hbar^2}$ です。一方，井戸外側の波動関数 $\psi(x) \propto e^{-\kappa|x|}$ が運動エネルギーの大部分を担い，$\langle K \rangle = E - \langle U \rangle$ はおよそ $\dfrac{2mU_0^2 a^2}{\hbar^2}$ となって，$E = \langle K \rangle + \langle U \rangle$ から $-\dfrac{2mU_0^2 a^2}{\hbar^2}$ が再現されます。
</aside>
