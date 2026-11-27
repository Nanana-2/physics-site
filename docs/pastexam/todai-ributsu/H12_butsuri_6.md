---
title: 東大理物 平成12年度 物理学 第6問：2次元電子の状態密度と周期ポテンシャルの摂動
tags:
  - 院試過去問
  - 東大理物
  - 物性物理学
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 物理学
exam_number: 第6問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成12年度 物理学 第6問：2次元電子の状態密度と周期ポテンシャルの摂動

## 問題

電子が2次元（$xy$ 面）内のみを動くとした場合に，以下のような問題を考えてみよう。各問には解答に至る道筋を添えて答えよ。
{: .problem-lead }

(1) 電子が面内では自由運動するとして Schrödinger 方程式を解き，波動関数 $\Psi(x, y)$ を求めよ。以下では，電子の質量を $m$ とし，電子のスピンや電子間の相互作用は無視せよ。

(2) 一般に，状態密度 $D(E)$ という量を，エネルギーが $E$ と $E + \delta E$ の間にある状態数が $D(E)\delta E$ となるような量として定義することができる。3次元自由空間に対して，系の $x, y, z$ 方向のサイズがそれぞれ $L$ であり周期的境界条件をもつとして，$D(E) \propto \sqrt{E}$ を示せ。

(3) 2次元運動の場合に，$x, y$ 方向のサイズがそれぞれ $L$ であり周期的境界条件をもつとして，状態密度を求めよ。

(4) $x, y$ 面内にさらに，例えば

$$
V(x, y) = V_0\bigl[\cos(2\pi x/a) + \cos(2\pi y/a)\bigr]
$$

のような周期ポテンシャルが加わった場合を考えよう。一般に，このような周期ポテンシャルが加わった場合に，波動関数 $\Psi$ はどのような形をとるか。

(5) 上記ポテンシャルの場合のように Schrödinger 方程式が変数分離できる場合は，

$$
V(x) = V_0\cos(2\pi x/a)
$$

というポテンシャル下での1次元 Schrödinger 方程式を解けばよい。このポテンシャルの振幅 $V_0$ が小さいとして摂動で扱い，この1次元問題に対してエネルギー・スペクトルがどのようになるか求めよ。

(6) 2次元での周期ポテンシャル問題に戻り，(a) エネルギー・スペクトルはどのような運動量又はそれに準ずるパラメータの関数として考えればよいのか，(b) このとき，エネルギー・スペクトルは定性的にどのような特徴をもつか，(c) 絶対零度で電子を詰めた場合に，どのような場合に金属になり，どのような場合に絶縁体・半導体になるか，を答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 物理学 第6問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，周期的境界条件のもとで許容される波数ベクトルが格子状に等間隔で並ぶことを利用し，エネルギー $E$ 以下の波数空間における3次元の体積や2次元の面積をエネルギーで微分することで状態密度を求めます。

後半では，格子並進に対する対称性から導かれるブロッホの定理によって周期ポテンシャル中の波動関数の一般形を捉えます。1次元ポテンシャル $V_0\cos(2\pi x/a)$ は逆格子ベクトル $G = 2\pi/a$ だけ離れた平面波同士を結合するため，一般の波数では非縮退2次摂動，ブリルアンゾーン境界 $k = \pm\pi/a$ 付近では縮退摂動を用いてエネルギーギャップの形成を求め，その結果を2次元のバンド構造と金属・絶縁体の分類へ広げます。
</div>

### (1)

2次元自由電子の時間によらないシュレーディンガー方程式は次の通りです。

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)\Psi(x, y) = E\Psi(x, y)
$$

変数分離形 $\Psi(x, y) = X(x)Y(y)$ を代入し，両辺を $\Psi$ で割ります。

$$
-\frac{\hbar^2}{2m}\frac{X''(x)}{X(x)} - \frac{\hbar^2}{2m}\frac{Y''(y)}{Y(y)} = E
$$

左辺の第1項は $x$ のみ，第2項は $y$ のみの関数なので，それぞれ定数 $E_x = \dfrac{\hbar^2 k_x^2}{2m}$，$E_y = \dfrac{\hbar^2 k_y^2}{2m}$ とおくと，各方向の方程式は $X'' + k_x^2 X = 0$，$Y'' + k_y^2 Y = 0$ となります。波数ベクトル $\mathbf{k} = (k_x, k_y)$（$k_x, k_y \in \mathbb{R}$）を用いて平面波解が得られます。

$$
\finalanswer{\Psi_{\mathbf{k}}(x, y) = A e^{i(k_x x + k_y y)}, \qquad E = \frac{\hbar^2}{2m}(k_x^2 + k_y^2)}
$$

ここで $A$ は規格化定数です。なお，1辺 $L$ の正方形領域に周期的境界条件 $\Psi(x + L, y) = \Psi(x, y)$，$\Psi(x, y + L) = \Psi(x, y)$ を課す場合は，$A = \dfrac{1}{L}$，$k_x = \dfrac{2\pi}{L}n_x$，$k_y = \dfrac{2\pi}{L}n_y$（$n_x, n_y \in \mathbb{Z}$）となります。

### (2)

3次元自由空間で各方向に周期的境界条件 $\Psi(x + L, y, z) = \Psi(x, y + L, z) = \Psi(x, y, z + L) = \Psi(x, y, z)$ を課すと，許容される波数ベクトル $\mathbf{k} = (k_x, k_y, k_z)$ の成分は整数 $n_x, n_y, n_z$ を用いて次になります。

$$
k_x = \frac{2\pi}{L}n_x, \qquad k_y = \frac{2\pi}{L}n_y, \qquad k_z = \frac{2\pi}{L}n_z
$$

したがって，波数空間で1つの状態が占める体積は $\left(\dfrac{2\pi}{L}\right)^3$ です。エネルギー $E = \dfrac{\hbar^2 k^2}{2m}$ 以下にある状態は，波数空間で半径 $k_E = \dfrac{\sqrt{2mE}}{\hbar}$ の球の内部に含まれます。スピンを無視したときのエネルギー $E$ 以下の総状態数 $N_{3\mathrm{D}}(E)$ を求めます。

$$
\begin{aligned}
N_{3\mathrm{D}}(E) &= \frac{\dfrac{4}{3}\pi k_E^3}{(2\pi/L)^3} \\
&= \frac{L^3}{6\pi^2}k_E^3 \\
&= \frac{L^3}{6\pi^2}\left(\frac{2mE}{\hbar^2}\right)^{3/2}
\end{aligned}
$$

状態密度 $D_{3\mathrm{D}}(E)$ は $N_{3\mathrm{D}}(E)$ を $E$ で微分して得られます。

$$
\begin{aligned}
D_{3\mathrm{D}}(E) &= \frac{\mathrm{d}N_{3\mathrm{D}}(E)}{\mathrm{d}E} \\
&= \frac{L^3}{6\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\cdot\frac{3}{2}E^{1/2} \\
&= \frac{L^3}{4\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}
\end{aligned}
$$

これより，$D_{3\mathrm{D}}(E) \propto \sqrt{E}$ が成り立ちます。

### (3)

2次元で $x, y$ 方向にサイズ $L$ の周期的境界条件を課すと，$k_x = \dfrac{2\pi}{L}n_x$，$k_y = \dfrac{2\pi}{L}n_y$ となり，波数空間で1つの状態が占める面積は $\left(\dfrac{2\pi}{L}\right)^2$ です。

エネルギー $E > 0$ 以下にある状態は半径 $k_E = \dfrac{\sqrt{2mE}}{\hbar}$ の円の内部に含まれるため，スピンを無視した総状態数 $N_{2\mathrm{D}}(E)$ は次になります。

$$
\begin{aligned}
N_{2\mathrm{D}}(E) &= \frac{\pi k_E^2}{(2\pi/L)^2} \\
&= \frac{L^2}{4\pi}\cdot\frac{2mE}{\hbar^2} \\
&= \frac{mL^2}{2\pi\hbar^2}E
\end{aligned}
$$

これを $E$ で微分して2次元の状態密度 $D_{2\mathrm{D}}(E)$ を求めます。

$$
\begin{aligned}
D_{2\mathrm{D}}(E) &= \frac{\mathrm{d}N_{2\mathrm{D}}(E)}{\mathrm{d}E} \\
&= \frac{mL^2}{2\pi\hbar^2} \qquad (E > 0)
\end{aligned}
$$

$E < 0$ には状態が存在しないので $D_{2\mathrm{D}}(E) = 0$ です。したがって，2次元自由電子の状態密度はエネルギーによらない定数になります。

$$
\finalanswer{D(E) = \begin{cases} \dfrac{mL^2}{2\pi\hbar^2} & (E > 0) \\ 0 & (E < 0) \end{cases}}
$$

### (4)

ポテンシャル $V(x, y)$ は格子並進に対して $V(x + a, y) = V(x, y + a) = V(x, y)$ の周期性をもちます。したがって，ブロッホの定理より，エネルギー固有関数は平面波 $e^{i\mathbf{k}\cdot\mathbf{r}}$ と格子と同じ周期をもつ周期関数 $u_{\mathbf{k}}(\mathbf{r})$ の積になります。このような波動関数を**ブロッホ関数**といいます。

$$
\finalanswer{\Psi_{\mathbf{k}}(x, y) = e^{i(k_x x + k_y y)} u_{\mathbf{k}}(x, y), \qquad u_{\mathbf{k}}(x + a, y) = u_{\mathbf{k}}(x, y + a) = u_{\mathbf{k}}(x, y)}
$$

なお，与えられたポテンシャル $V(x, y) = V_0\cos(2\pi x/a) + V_0\cos(2\pi y/a)$ は $x$ と $y$ の和に分かれるため，固有関数はさらに1次元ブロッホ関数の積 $\Psi_{\mathbf{k}}(x, y) = e^{i(k_x x + k_y y)} u_{k_x}(x) u_{k_y}(y)$ の形になります。

### (5)

逆格子ベクトルを $G = \dfrac{2\pi}{a}$ とおくと，摂動ポテンシャル $V(x)$ は次の形になります。

$$
V(x) = \frac{V_0}{2}\left(e^{iGx} + e^{-iGx}\right)
$$

無摂動ハミルトニアン $H_0 = -\dfrac{\hbar^2}{2m}\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}$ の固有状態は $|k\rangle = \dfrac{1}{\sqrt{L}}e^{ikx}$，固有エネルギーは $E^{(0)}(k) = \dfrac{\hbar^2 k^2}{2m}$ です。摂動 $V$ の行列要素 $\langle k'|V|k\rangle$ を計算します。

$$
\begin{aligned}
\langle k'|V|k\rangle &= \frac{V_0}{2L}\int_0^L e^{i(k - k')x}\left(e^{iGx} + e^{-iGx}\right)\mathrm{d}x \\
&= \frac{V_0}{2}\left(\delta_{k',\, k + G} + \delta_{k',\, k - G}\right)
\end{aligned}
$$

まず，$|k\rangle$ が $|k \pm G\rangle$ と縮退していない領域，すなわち $k$ が $\pm\dfrac{G}{2}$ から十分離れている場合を非縮退摂動論で計算します。対角行列要素は $\langle k|V|k\rangle = 0$ なので，1次摂動エネルギーは $E^{(1)}(k) = 0$ です。2次摂動エネルギー $E^{(2)}(k)$ を計算します。

$$
\begin{aligned}
E^{(2)}(k) &= \frac{|\langle k + G|V|k\rangle|^2}{E^{(0)}(k) - E^{(0)}(k + G)} + \frac{|\langle k - G|V|k\rangle|^2}{E^{(0)}(k) - E^{(0)}(k - G)} \\
&= \frac{V_0^2}{4}\cdot\frac{2m}{\hbar^2}\left[\frac{1}{k^2 - (k + G)^2} + \frac{1}{k^2 - (k - G)^2}\right] \\
&= \frac{mV_0^2}{2\hbar^2}\left(\frac{1}{-2kG - G^2} + \frac{1}{2kG - G^2}\right) \\
&= \frac{mV_0^2}{2\hbar^2}\cdot\frac{-2G^2}{G^4 - 4k^2 G^2} \\
&= \frac{mV_0^2}{\hbar^2(4k^2 - G^2)}
\end{aligned}
$$

$G = \dfrac{2\pi}{a}$ を代入すると，ブリルアンゾーン境界 $k = \pm\dfrac{\pi}{a}$ から離れた波数でのエネルギーは次の通りです。

$$
E(k) \approx \frac{\hbar^2 k^2}{2m} + \frac{mV_0^2 a^2}{4\hbar^2(k^2 a^2 - \pi^2)}
$$

この表式は $k \to \pm\dfrac{\pi}{a}$ で発散します。これは $k = \dfrac{G}{2}$ で $E^{(0)}(k) = E^{(0)}(k - G)$，および $k = -\dfrac{G}{2}$ で $E^{(0)}(k) = E^{(0)}(k + G)$ と縮退が起こるためです。

そこで $k \approx \dfrac{\pi}{a}$ の近傍では，強く結合する2状態 $|k\rangle$ と $|k - G\rangle$ の部分空間で縮退摂動論を用います。この2状態に対するハミルトニアン行列は次の通りです。

$$
H_{\mathrm{eff}} = \begin{pmatrix} E^{(0)}(k) & \dfrac{V_0}{2} \\[1.2ex] \dfrac{V_0}{2} & E^{(0)}(k - G) \end{pmatrix}
$$

永年方程式 $\det(H_{\mathrm{eff}} - E I) = 0$ を展開して解きます。

$$
\begin{aligned}
\bigl(E^{(0)}(k) - E\bigr)\bigl(E^{(0)}(k - G) - E\bigr) - \frac{V_0^2}{4} &= 0 \\
E^2 - \bigl(E^{(0)}(k) + E^{(0)}(k - G)\bigr)E + E^{(0)}(k)E^{(0)}(k - G) - \frac{V_0^2}{4} &= 0
\end{aligned}
$$

2次方程式の解の公式を当てはめます。

$$
\begin{aligned}
E_\pm(k) &= \frac{E^{(0)}(k) + E^{(0)}(k - G)}{2} \pm \sqrt{\left(\frac{E^{(0)}(k) - E^{(0)}(k - G)}{2}\right)^2 + \frac{V_0^2}{4}}
\end{aligned}
$$

特に $k = \dfrac{\pi}{a}$ では $E^{(0)}\left(\dfrac{\pi}{a}\right)$ と $E^{(0)}\left(-\dfrac{\pi}{a}\right)$ がともに $\dfrac{\hbar^2\pi^2}{2ma^2}$ に等しいため，2つの固有エネルギーは次の値に分裂します。

$$
E_\pm\left(\frac{\pi}{a}\right) = \frac{\hbar^2\pi^2}{2ma^2} \pm \frac{|V_0|}{2}
$$

$k = -\dfrac{\pi}{a}$ の近傍でも $|k\rangle$ と $|k + G\rangle$ を用いて同様の式が得られます。したがって，$k = \pm\dfrac{\pi}{a}$ において幅 $\Delta E = |V_0|$ のエネルギーギャップが開き，自由電子の放物線 $E^{(0)}(k)$ が上下のエネルギーバンドに分裂します。

$$
\finalanswer{E(k) \approx \frac{\hbar^2 k^2}{2m} + \frac{mV_0^2 a^2}{4\hbar^2(k^2 a^2 - \pi^2)} \quad \left(k \not\approx \pm\frac{\pi}{a}\right)}
$$

$$
\finalanswer{E_\pm(k) = \frac{E^{(0)}(k) + E^{(0)}(k \mp G)}{2} \pm \sqrt{\left(\frac{E^{(0)}(k) - E^{(0)}(k \mp G)}{2}\right)^2 + \frac{V_0^2}{4}} \quad \left(k \approx \pm\frac{\pi}{a}\right)}
$$

ここで $G = \dfrac{2\pi}{a}$ であり，境界 $k = \pm\dfrac{\pi}{a}$ に幅 $|V_0|$ のエネルギーギャップが生じます。

### (6)

#### (a)

ブロッホ関数の波数ベクトル $\mathbf{k} = (k_x, k_y)$，すなわち結晶運動量 $\hbar\mathbf{k}$ とバンド指標の関数 $E_n(\mathbf{k})$ として考えます。逆格子ベクトル $\mathbf{G} = \left(\dfrac{2\pi}{a}m_x, \dfrac{2\pi}{a}m_y\right)$（$m_x, m_y \in \mathbb{Z}$）だけずれた波数は同じブロッホ状態を与えるため，第1ブリルアンゾーン $-\dfrac{\pi}{a} \le k_x \le \dfrac{\pi}{a}$，$-\dfrac{\pi}{a} \le k_y \le \dfrac{\pi}{a}$ の範囲で考えれば十分です。

#### (b)

変数分離性から2次元のエネルギー固有値は1次元の固有値の和 $E_{n_x, n_y}(k_x, k_y) = E_{n_x}(k_x) + E_{n_y}(k_y)$ になります。したがって，$k_x = \pm\dfrac{\pi}{a}$ や $k_y = \pm\dfrac{\pi}{a}$ のブリルアンゾーン境界でそれぞれエネルギーの不連続が生じ，逆空間で周期的で正方形の対称性をもつ複数のエネルギーバンドが形成されます。

ただし1次元の場合と異なり，2次元では異なる $\mathbf{k}$ 方向のエネルギーバンドが重なり合うことがあります。たとえば $V_0$ が小さいとき，第1バンドの上端は角 $(k_x, k_y) = \left(\dfrac{\pi}{a}, \dfrac{\pi}{a}\right)$ にあって $E_{1,\max} \approx 2\dfrac{\hbar^2\pi^2}{2ma^2} - |V_0|$ となる一方，第2バンドの下端は辺の中点 $\left(\dfrac{\pi}{a}, 0\right)$ にあって $E_{2,\min} \approx \dfrac{\hbar^2\pi^2}{2ma^2} + \dfrac{|V_0|}{2}$ となります。$|V_0|$ が十分小さい場合は $E_{2,\min} < E_{1,\max}$ となって第1バンドと第2バンドのエネルギー領域が重なり，全 $\mathbf{k}$ 空間にわたるエネルギーギャップは開きません。$|V_0|$ が十分大きくなるとバンドの重なりが解消し，バンド間に全域的なエネルギーギャップが生じます。

#### (c)

絶対零度で電子をエネルギーの低い状態から順に詰めていくと，フェルミエネルギー $E_{\mathrm{F}}$ の位置によって電気伝導の性質が分かれます。

- 金属になる場合：フェルミエネルギー $E_{\mathrm{F}}$ がいずれかのエネルギーバンドの内部にあり，部分的に電子で満たされたバンドが存在するときです。たとえば単位格子当たりの電子数が整数でない場合や，整数であっても (b) のように隣り合うバンド同士がエネルギー的に重なり合っている場合は，フェルミ面近傍に無限小のエネルギーで遷移できる空状態が存在するため，外部電場によって電子が加速されて金属になります。
- 絶縁体・半導体になる場合：あるバンドまでが完全に電子で満たされ，その上のバンドが完全に空であり，かつ最高被占バンドの上端と最低空バンドの下端の間に全域的なエネルギーギャップが存在するときです。スピンを無視したモデルでは1つのバンドに単位格子当たり1個の電子が入るため，単位格子当たりの電子数が整数であり，さらにポテンシャルが十分強くてバンドの重なりがなくエネルギーギャップが開いている場合に，絶対零度で電流を運ぶ励起状態がなく絶縁体または半導体になります。一般に室温での熱エネルギーに比べてギャップが大きいものが絶縁体，小さく熱励起によるキャリアが生じるものが半導体です。

<aside class="rigor-note" markdown>
(1) から (3) では問題文の指示に従いスピンを無視して計算しました。電子のスピン自由度 $2$ を考慮する場合は，状態密度 $D_{3\mathrm{D}}(E)$ および $D_{2\mathrm{D}}(E)$ がいずれも $2$ 倍になり，(6)(c) で1つのバンドを満たす電子数は単位格子当たり2個となります。また (5) の1次元ポテンシャル $V_0\cos(2\pi x/a)$ では，高次のゾーン境界 $k = \pm n\pi/a$（$n \ge 2$）にも $n$ 次の摂動で幅 $O(|V_0|^n)$ のエネルギーギャップが開きます。
</aside>
