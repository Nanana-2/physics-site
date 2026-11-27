---
title: 東大理物 平成10年度 物理学 第1問：球対称井戸型ポテンシャルと逆2乗ポテンシャルにおける中心への落下
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成10年度 物理学 第1問：球対称井戸型ポテンシャルと逆2乗ポテンシャルにおける中心への落下

## 問題

中心対称場の中の粒子の運動に対するシュレーディンガー方程式は次のように与えられる。

$$
\frac{\hbar^2}{2m}\Delta\Psi + [E - U(r)]\Psi = 0
$$

ここで $m$ および $E$ はそれぞれ粒子の質量とエネルギー，また $U(r)$ は場のポテンシャルエネルギーである。ラプラス演算子 $\Delta$ は

$$
\Delta \equiv \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}
$$

で，$r = \sqrt{x^2 + y^2 + z^2}$ である。

中心対称場の中の運動では角運動量が保存されるので，波動関数 $\Psi$ の動径関数 $R_\ell(r)$ は次の方程式を満たす。

$$
\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}R_\ell}{\mathrm{d}r}\right) - \frac{\ell(\ell + 1)}{r^2}R_\ell + \frac{2m}{\hbar^2}[E - U(r)]R_\ell = 0
$$

ここで $\ell$ は粒子の角運動量である。以下では角運動量 $\ell = 0$ の動径関数 $R_0(r)$ について考えよう。
{: .problem-lead }

(1) 井戸型ポテンシャル，

$$
U(r) =
\begin{cases}
-U_0, & r \le r_0 \\
0, & r > r_0
\end{cases}
$$

において，以下の問いに答えよ。ただし，$U_0$ は正の定数で $-U_0 \le E \le 0$ とする。

(a) $r \le r_0$ での $R_0(r)$ の形を求めよ。

(b) $r > r_0$ での $R_0(r)$ の形を求めよ。

(c) 上記の (a) と (b) で求めた動径関数 $R_0(r)$ を $r = r_0$ でなめらかにつなぎ，粒子のエネルギー $E$ と $r_0$ との関係式を求めよ。

(d) $U_0$ が充分に大きいとして，上の答えを用いて粒子の負のエネルギー準位と動径関数 $R_0(r)$ のゼロ点の数との関係を述べよ。

(2) 次に中心対称なポテンシャルが

$$
U(r) =
\begin{cases}
-\dfrac{\alpha}{r_0^2}, & r \le r_0 \\[10pt]
-\dfrac{\alpha}{r^2}, & r \ge r_0
\end{cases}
$$

で与えられている。ここで $\alpha > 0$ とする。またここでは，$r_0$ が小さい場合を考えて $r = r_0$ の近くでの動径関数 $R_0(r)$ の振る舞いについて考察する。

(a) $r \le r_0$ の領域で動径関数 $R_0(r)$ を求めよ。ただし，$r_0$ は充分小さく，粒子のエネルギー $E$ はポテンシャルエネルギー（$-\alpha/r_0^2$）に比べて無視できるものとする。

(b) 動径関数 $R_0(r)$ は，$r \ge r_0$ の領域でしかも $r = r_0$ の近くでは近似的に次の方程式を満たす。

$$
\frac{\mathrm{d}^2 R_0}{\mathrm{d}r^2} + \frac{2}{r}\frac{\mathrm{d}R_0}{\mathrm{d}r} + \frac{\beta}{r^2}R_0 = 0
$$

ただし，$\beta = (2m/\hbar^2)\alpha$ である。この方程式の $r = r_0$ の近くの解を $R_0(r) \sim r^a$ と形を仮定して求めよ。ただし，その解は $\beta$ を用いて書くこと。

(c) 上記の (a) と (b) で求めた動径関数 $R_0(r)$ が $r = r_0$ でなめらかにつながるものとして，$r \ge r_0$ の領域の解を求めよ。

(d) 上で求めた解は $\beta < 1/4$ の場合と $\beta > 1/4$ の場合とでは振る舞いが大きく異なる。$\beta > 1/4$ の場合に，$r \ge r_0$ での動径関数 $R_0(r)$ のゼロ点の数に注目して，$r_0 \to 0$ の極限で粒子の運動に何が起きるかを理由を上げて説明せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
$\ell = 0$ の動径方程式は $u(r) = r R_0(r)$ と置換することで1次元シュレーディンガー方程式の形に整理されます。設問 (1) では3次元球対称井戸型ポテンシャルの束縛状態に対する固有値条件を導き，エネルギー準位と動径波動関数のゼロ点の数の対応を示します。

設問 (2) では短距離切断 $r_0$ を入れた引力逆2乗ポテンシャル $-\alpha/r^2$ のオイラー型微分方程式を解き，$\beta = 2m\alpha/\hbar^2 > 1/4$ のときに $r_0 \to 0$ でゼロ点が無限個に発散することから，基底エネルギーが $-\infty$ へ落ち込む現象を導きます。
</div>

### (1)(a)

$\ell = 0$ の動径方程式において，$u(r) = r R_0(r)$ と置きます。

$$
\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}R_0}{\mathrm{d}r}\right) = \frac{1}{r}\frac{\mathrm{d}^2 u}{\mathrm{d}r^2}
$$

したがって $u(r)$ の満たす方程式は次の通りです。

$$
\frac{\mathrm{d}^2 u}{\mathrm{d}r^2} + \frac{2m}{\hbar^2}[E - U(r)]u = 0
$$

$r \le r_0$ では $U(r) = -U_0$ であり，$-U_0 < E \le 0$ に対して正の波数

$$
k = \frac{\sqrt{2m(E + U_0)}}{\hbar}
$$

を定義すると，$u''(r) + k^2 u(r) = 0$ となります。一般解は定数 $A, A'$ を用いて $u(r) = A\sin(kr) + A'\cos(kr)$ です。

原点 $r = 0$ で動径関数 $R_0(r) = \dfrac{u(r)}{r}$ が有限であるためには $u(0) = 0$，すなわち $A' = 0$ である必要があります。なお $E = -U_0$ のときは $k = 0$ となり $u(r) = Cr$ ですが，これは $r > r_0$ の減衰解となめらかに接続できないため束縛状態を与えません。

したがって任意定数 $A$ を用いて，$r \le r_0$ での $R_0(r)$ は次のように表されます。

$$
\finalanswer{R_0(r) = \frac{A}{r}\sin(kr), \qquad k = \frac{\sqrt{2m(E + U_0)}}{\hbar}}
$$

### (1)(b)

$r > r_0$ では $U(r) = 0$ です。$-U_0 < E < 0$ のとき，正の定数

$$
\kappa = \frac{\sqrt{-2mE}}{\hbar}
$$

を定義すると，$u''(r) - \kappa^2 u(r) = 0$ となります。一般解は定数 $B, B'$ を用いて $u(r) = B e^{-\kappa r} + B' e^{\kappa r}$ です。

波動関数が無限遠で発散せず2乗可積分であるためには $r \to \infty$ で $u(r) \to 0$ となる必要があり，$B' = 0$ です。よって任意定数 $B$ を用いて，$r > r_0$ での $R_0(r)$ は次のように表されます。

$$
\finalanswer{R_0(r) = \frac{B}{r}e^{-\kappa r}, \qquad \kappa = \frac{\sqrt{-2mE}}{\hbar}}
$$

### (1)(c)

$R_0(r)$ と $\dfrac{\mathrm{d}R_0}{\mathrm{d}r}$ が $r = r_0$ で連続であることは，$u(r) = r R_0(r)$ と $u'(r)$ が $r = r_0$ で連続であることと同値です。接続条件を書き下します。

$$
\begin{aligned}
A\sin(kr_0) &= B e^{-\kappa r_0} \\
Ak\cos(kr_0) &= -B\kappa e^{-\kappa r_0}
\end{aligned}
$$

$A \neq 0$ かつ $B \neq 0$ となる解に対して第2式を第1式で割ると，対数微分の連続条件が得られます。

$$
k\cot(kr_0) = -\kappa
$$

$k = \dfrac{\sqrt{2m(E + U_0)}}{\hbar}$ および $\kappa = \dfrac{\sqrt{-2mE}}{\hbar}$ を代入すると，$E$ と $r_0$ の関係式は次のようになります。

$$
\finalanswer{\sqrt{E + U_0}\cot\left(\frac{\sqrt{2m(E + U_0)}}{\hbar}r_0\right) = -\sqrt{-E}}
$$

### (1)(d)

無次元変数 $\xi = kr_0 > 0$，$\eta = \kappa r_0 > 0$ を導入すると，(1)(c) の条件式と $k^2 + \kappa^2 = \dfrac{2mU_0}{\hbar^2}$ の関係は次の連立方程式になります。

$$
\begin{aligned}
\eta &= -\xi\cot\xi \\
\xi^2 + \eta^2 &= \frac{2mU_0 r_0^2}{\hbar^2} \equiv R^2
\end{aligned}
$$

第1象限（$\xi > 0, \eta > 0$）において，$\eta = -\xi\cot\xi$ の曲線は

$$
\left(n - \frac{1}{2}\right)\pi < \xi < n\pi \qquad (n = 1, 2, 3, \dots)
$$

の各区間に1本ずつ存在し，区間の左端 $\xi = \left(n - \dfrac{1}{2}\right)\pi$ で $\eta = 0$，右端 $\xi \to n\pi - 0$ で $\eta \to +\infty$ へと単調増加します。したがって，半径 $R = \dfrac{\sqrt{2mU_0}}{\hbar}r_0$ の円 $\xi^2 + \eta^2 = R^2$ は，第 $n$ 番目の枝と高々1回交わります。

ここで $r > 0$ における $R_0(r)$ のゼロ点の個数を数えます。$r > r_0$ では $R_0(r) = \dfrac{B}{r}e^{-\kappa r}$ はゼロ点をもたないため，ゼロ点はすべて井戸内部 $0 < r < r_0$ での $\sin(kr) = 0$ から生じます。すなわち $kr = m\pi$（$m = 1, 2, \dots$）が $0 < kr < \xi$ の範囲に入る個数に等しくなります。

第 $n$ 番目の枝上の解 $\xi_n$ は $\left(n - \dfrac{1}{2}\right)\pi < \xi_n < n\pi$ を満たすため，$m = 1, 2, \dots, n - 1$ のちょうど $n - 1$ 個のゼロ点をもちます。さらに $\xi_n$ が大きいほどエネルギー $E_n = \dfrac{\hbar^2 \xi_n^2}{2mr_0^2} - U_0$ は高くなります。

以上より，次の関係が成り立ちます。

- 負のエネルギー固有準位を下から順に $E_1 < E_2 < \cdots < E_N < 0$ とすると，下から $n$ 番目の準位 $E_n$ に属する動径関数 $R_0(r)$ は $r > 0$ にちょうど $n - 1$ 個のゼロ点をもちます。すなわち基底状態では $0$ 個，第1励起状態では $1$ 個であり，エネルギー準位が1段上がるごとにゼロ点が1個ずつ増えます。
- 負のエネルギー束縛状態の総数 $N$ は $\dfrac{R}{\pi} + \dfrac{1}{2}$ を超えない最大の整数であり，$E \to 0^-$ に対応する波動関数の $r > 0$ におけるゼロ点の個数に等しくなります。

### (2)(a)

$r \le r_0$ では $U(r) = -\dfrac{\alpha}{r_0^2}$ です。条件より $E$ を $U(r) = -\dfrac{\alpha}{r_0^2}$ に比べて無視すると，$u(r) = r R_0(r)$ の方程式は次のようになります。

$$
\frac{\mathrm{d}^2 u}{\mathrm{d}r^2} + \frac{2m\alpha}{\hbar^2 r_0^2}u = 0
$$

ここで $\beta = \dfrac{2m\alpha}{\hbar^2} > 0$ を用いると，波数は $k_0 = \dfrac{\sqrt{\beta}}{r_0}$ です。(1)(a) と同様に原点 $r = 0$ での有限性から $u(0) = 0$ となるため，$r \le r_0$ での動径関数 $R_0(r)$ は定数 $A$ を用いて次のように表されます。

$$
\finalanswer{R_0(r) = \frac{A}{r}\sin\left(\frac{\sqrt{\beta}}{r_0}r\right)}
$$

### (2)(b)

与えられたオイラー型微分方程式に $R_0(r) = r^a$ を代入します。

$$
\bigl(a(a - 1) + 2a + \beta\bigr)r^{a - 2} = 0
$$

よって特性方程式は

$$
a^2 + a + \beta = 0
$$

となり，その2解 $a_\pm$ は次の通りです。

$$
a_\pm = \frac{-1 \pm \sqrt{1 - 4\beta}}{2}
$$

任意定数 $C_1, C_2$ を用いて，$\beta$ と $\dfrac{1}{4}$ の大小によって一般解の形を3通りに分けて表します。

まず $\beta < \dfrac{1}{4}$ のとき，$a_\pm$ は相異なる2実数となり，一般解は次の通りです。

$$
R_0(r) = C_1 r^{(-1 + \sqrt{1 - 4\beta})/2} + C_2 r^{(-1 - \sqrt{1 - 4\beta})/2}
$$

次に $\beta = \dfrac{1}{4}$ のとき，重解 $a_+ = -\dfrac{1}{2}$，$a_- = -\dfrac{1}{2}$ をもち，一般解は次の通りです。

$$
R_0(r) = r^{-1/2}\bigl(C_1 + C_2\ln r\bigr)
$$

最後に $\beta > \dfrac{1}{4}$ のとき，$\mu = \dfrac{\sqrt{4\beta - 1}}{2} > 0$ とおくと $a_\pm = -\dfrac{1}{2} \pm i\mu$ となり，実関数形の一般解は次の通りです。

$$
R_0(r) = r^{-1/2}\bigl(C_1\cos(\mu\ln r) + C_2\sin(\mu\ln r)\bigr)
$$

$$
\finalanswer{R_0(r) =
\begin{cases}
C_1 r^{(-1 + \sqrt{1 - 4\beta})/2} + C_2 r^{(-1 - \sqrt{1 - 4\beta})/2} & \left(\beta < \dfrac{1}{4}\right) \\[10pt]
r^{-1/2}(C_1 + C_2\ln r) & \left(\beta = \dfrac{1}{4}\right) \\[10pt]
r^{-1/2}\left[C_1\cos\left(\dfrac{\sqrt{4\beta - 1}}{2}\ln r\right) + C_2\sin\left(\dfrac{\sqrt{4\beta - 1}}{2}\ln r\right)\right] & \left(\beta > \dfrac{1}{4}\right)
\end{cases}}
$$

### (2)(c)

無次元変数 $x = \dfrac{r}{r_0} \ge 1$ を用い，$u(r) = r R_0(r)$ と $u'(r)$ の $r = r_0$（$x = 1$）における連続条件を課します。(2)(a) の解 $u(r) = A\sin(\sqrt{\beta}x)$ より，$x = 1$ での値と導関数は次の通りです。

$$
\begin{aligned}
u(r_0) &= A\sin\sqrt{\beta} \\
r_0 u'(r_0) &= A\sqrt{\beta}\cos\sqrt{\beta}
\end{aligned}
$$

各場合について接続定数を決定します。

#### $\beta < 1/4$ の場合

$s = \dfrac{\sqrt{1 - 4\beta}}{2}$ とおき，$u(r) = c_+ x^{1/2 + s} + c_- x^{1/2 - s}$ とします。$x = 1$ での接続条件は次の連立方程式です。

$$
\begin{aligned}
c_+ + c_- &= A\sin\sqrt{\beta} \\
\left(\frac{1}{2} + s\right)c_+ + \left(\frac{1}{2} - s\right)c_- &= A\sqrt{\beta}\cos\sqrt{\beta}
\end{aligned}
$$

第2式から第1式の $\dfrac{1}{2}$ 倍を引くと $s(c_+ - c_-) = A\left(\sqrt{\beta}\cos\sqrt{\beta} - \dfrac{1}{2}\sin\sqrt{\beta}\right)$ となるため，$c_\pm$ が求まります。

$$
c_\pm = \frac{A}{2\sqrt{1 - 4\beta}}\left[\left(\sqrt{1 - 4\beta} \mp 1\right)\sin\sqrt{\beta} \pm 2\sqrt{\beta}\cos\sqrt{\beta}\right]
$$

したがって $R_0(r) = \dfrac{u(r)}{r}$ は次の通りです。

$$
R_0(r) = \frac{c_+}{r_0}\left(\frac{r}{r_0}\right)^{(-1 + \sqrt{1 - 4\beta})/2} + \frac{c_-}{r_0}\left(\frac{r}{r_0}\right)^{(-1 - \sqrt{1 - 4\beta})/2}
$$

#### $\beta = 1/4$ の場合

$u(r) = x^{1/2}(b_1 + b_2\ln x)$ とおき，$x = 1$ で接続します。

$$
\begin{aligned}
b_1 &= A\sin\frac{1}{2} \\
\frac{1}{2}b_1 + b_2 &= \frac{A}{2}\cos\frac{1}{2}
\end{aligned}
$$

これより $b_2 = \dfrac{A}{2}\left(\cos\dfrac{1}{2} - \sin\dfrac{1}{2}\right)$ が得られます。

$$
R_0(r) = \frac{A}{r_0}\left(\frac{r}{r_0}\right)^{-1/2}\left[\sin\frac{1}{2} + \frac{1}{2}\left(\cos\frac{1}{2} - \sin\frac{1}{2}\right)\ln\frac{r}{r_0}\right]
$$

#### $\beta > 1/4$ の場合

$\mu = \dfrac{\sqrt{4\beta - 1}}{2}$ とおき，$u(r) = x^{1/2}\bigl(d_1\cos(\mu\ln x) + d_2\sin(\mu\ln x)\bigr)$ とします。$x = 1$ で接続します。

$$
\begin{aligned}
d_1 &= A\sin\sqrt{\beta} \\
\frac{1}{2}d_1 + \mu d_2 &= A\sqrt{\beta}\cos\sqrt{\beta}
\end{aligned}
$$

これより $d_2 = \dfrac{A}{\sqrt{4\beta - 1}}\left(2\sqrt{\beta}\cos\sqrt{\beta} - \sin\sqrt{\beta}\right)$ が求まります。

$$
R_0(r) = \frac{A}{r_0}\left(\frac{r}{r_0}\right)^{-1/2}\left[\sin\sqrt{\beta}\,\cos\left(\mu\ln\frac{r}{r_0}\right) + \frac{2\sqrt{\beta}\cos\sqrt{\beta} - \sin\sqrt{\beta}}{\sqrt{4\beta - 1}}\sin\left(\mu\ln\frac{r}{r_0}\right)\right]
$$

以上3通りの解をまとめます。

$$
\finalanswer{R_0(r) =
\begin{cases}
\dfrac{c_+}{r_0}\left(\dfrac{r}{r_0}\right)^{(-1 + \sqrt{1 - 4\beta})/2} + \dfrac{c_-}{r_0}\left(\dfrac{r}{r_0}\right)^{(-1 - \sqrt{1 - 4\beta})/2} & \left(\beta < \dfrac{1}{4}\right) \\[12pt]
\dfrac{A}{r_0}\left(\dfrac{r}{r_0}\right)^{-1/2}\left[\sin\dfrac{1}{2} + \dfrac{1}{2}\left(\cos\dfrac{1}{2} - \sin\dfrac{1}{2}\right)\ln\dfrac{r}{r_0}\right] & \left(\beta = \dfrac{1}{4}\right) \\[12pt]
\dfrac{A}{r_0}\left(\dfrac{r}{r_0}\right)^{-1/2}\left[\sin\sqrt{\beta}\,\cos\left(\mu\ln\dfrac{r}{r_0}\right) + \dfrac{2\sqrt{\beta}\cos\sqrt{\beta} - \sin\sqrt{\beta}}{\sqrt{4\beta - 1}}\sin\left(\mu\ln\dfrac{r}{r_0}\right)\right] & \left(\beta > \dfrac{1}{4}\right)
\end{cases}}
$$

### (2)(d)

$\beta > \dfrac{1}{4}$ の場合，(2)(c) で求めた $r \ge r_0$ における解は，振幅定数 $D$ と位相定数 $\delta$ を用いて次のようにまとめることができます。

$$
R_0(r) = D\left(\frac{r}{r_0}\right)^{-1/2}\cos\left(\mu\ln\frac{r}{r_0} + \delta\right), \qquad \mu = \frac{\sqrt{4\beta - 1}}{2} > 0
$$

この近似式は $|E| \ll \dfrac{\alpha}{r^2}$ を満たす範囲，すなわち $r_0 \le r \ll r_{\max} = \sqrt{\dfrac{\alpha}{|E|}}$ で成り立ちます。特に $E = 0$ の極限では $r_{\max} \to \infty$ となり，任意の有限の $r$ に対して上の振動解がそのまま成り立ちます。

位相 $\mu\ln\dfrac{r}{r_0} + \delta$ は $r$ を固定して $r_0 \to 0$ とするとき，対数関数 $\ln\dfrac{r}{r_0}$ が $+\infty$ へ発散するため，$r_0 \le r \le r_{\max}$ の区間内で無限回 $\pi$ だけ増加します。したがって $E = 0$ の波動関数が $r \ge r_0$ にもつゼロ点の個数 $N(r_0)$ は，$\dfrac{\mu}{\pi}\ln\dfrac{r_{\max}}{r_0}$ のように $r_0 \to 0$ で無限大に発散します。

(1)(d) で示したように，$E \to 0^-$ の波動関数がもつゼロ点の個数は負のエネルギーをもつ束縛状態の個数に対応し，ゼロ点が1個少ない状態ほどエネルギー固有値は低くなります。さらに $r_0$ を小さくしていくと，ゼロ点が0個の基底状態は井戸領域 $r \lesssim r_0$ に局在し，そのエネルギー固有値はポテンシャル深さの尺度に従って

$$
E_{\mathrm{ground}} \sim -\frac{\alpha}{r_0^2} \to -\infty \qquad (r_0 \to 0)
$$

のように下に有界でなく発散します。

したがって $\beta > \dfrac{1}{4}$ のとき，$r_0 \to 0$ の極限では負のエネルギーの束縛状態が無限個出現してエネルギー固有値に下限が存在しなくなり，粒子はエネルギーをいくらでも低くしながら原点へ落ち込んで局在してしまいます。この現象を**中心への落下**といいます。

<div class="rigor-note" markdown>
$\beta < \dfrac{1}{4}$ の場合は $r \ge r_0$ の解がべき関数の線形結合であり，ゼロ点は高々1個しか生じないため，不確定性原理による運動エネルギーの増加が引力ポテンシャル $-\alpha/r^2$ に打ち勝ち，粒子は原点へ落下しません。臨界値 $\beta = \dfrac{1}{4}$，すなわち $\alpha = \dfrac{\hbar^2}{8m}$ はハーディの不等式に対応する境界です。
</div>
