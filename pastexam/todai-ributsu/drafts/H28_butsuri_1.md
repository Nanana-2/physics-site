---
title: 東大理物 平成28年度 物理学 第1問：磁場中の2次元パウリ電子とゼロエネルギー束縛状態
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成28年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成28年度 物理学 第1問：磁場中の2次元パウリ電子とゼロエネルギー束縛状態

## 問題

$xy$ 平面内を動く電子の運動を量子力学的に考える。$z$ 方向には磁場があり，その磁束密度 $B_z(x, y)$ は，原点からの距離を $r = \sqrt{x^2 + y^2}$ として

$$
B_z(x, y) = \begin{cases} b > 0, & (r < R), \\ 0, & (r \ge R) \end{cases} \tag{1}
$$

と与えられるものとする。以下の手順に従って，エネルギーがゼロの束縛状態の個数を求める。

電子の波動関数はスピンの上向き，下向きに応じて $\psi_\uparrow(x, y)$ と $\psi_\downarrow(x, y)$ の二成分をもつので，まとめて縦ベクトルとして

$$
\Psi(x, y) = \begin{pmatrix} \psi_\uparrow(x, y) \\ \psi_\downarrow(x, y) \end{pmatrix} \qquad \text{略記すれば} \qquad |\Psi\rangle = \begin{pmatrix} |\psi_\uparrow\rangle \\ |\psi_\downarrow\rangle \end{pmatrix} \tag{2}
$$

と書け，ハミルトニアン $H$ は

$$
H = \frac{p_x^2 + p_y^2}{2m}\mathbf{1}_{2\times 2} + \frac{\hbar e B_z(x, y)}{2m}\sigma_z \tag{3}
$$

と書けるものとする。ただし $p_x$ と $p_y$ は

$$
p_x = -i\hbar\frac{\partial}{\partial x} + e A_x(x, y),\qquad p_y = -i\hbar\frac{\partial}{\partial y} + e A_y(x, y) \tag{4}
$$

であり，$\hbar$ はプランク定数 $h$ を $2\pi$ で割ったもの，$m$ は電子の質量，$-e < 0$ は電子の電荷，$A_x(x, y),\ A_y(x, y)$ はベクトルポテンシャルで，磁束密度 $B_z(x, y)$ との関係は

$$
B_z(x, y) = \frac{\partial A_y(x, y)}{\partial x} - \frac{\partial A_x(x, y)}{\partial y} \tag{5}
$$

で与えられる。また，行列は

$$
\mathbf{1}_{2\times 2} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\qquad
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\qquad
\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\qquad
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \tag{6}
$$

である。

(1) スピン角運動量演算子は

$$
S_x = \frac{\hbar}{2}\sigma_x,\qquad S_y = \frac{\hbar}{2}\sigma_y,\qquad S_z = \frac{\hbar}{2}\sigma_z \tag{7}
$$

で与えられる。交換関係 $[S_x, S_y]$ および $[H, S_z]$ を計算せよ。

(2) 演算子 $D$ を $D = p_x\sigma_x + p_y\sigma_y$ と定義する。この $D$ はエルミート演算子であって $D = D^\dagger$ を満たす。この $D$ について，次の関係式

$$
D\sigma_z = -\sigma_z D, \tag{8}
$$

$$
H = \frac{1}{2m} D^2 \tag{9}
$$

がそれぞれ成り立つことを示せ。

(3) 束縛状態 $|\Psi_n\rangle$ が $H$ の固有値 $E_n$ の固有状態であるとし，波動関数 $|\Phi_n\rangle$ を $|\Phi_n\rangle = D|\Psi_n\rangle$ で定める。このとき，式 (9) を用いて，

$$
\langle\Phi_n|\Phi_n\rangle = 2m E_n \langle\Psi_n|\Psi_n\rangle \tag{10}
$$

となることを示せ。

(4) エネルギー $E_n \neq 0$ の固有束縛状態 $|\Psi_n\rangle$ を考える。このとき，$E_n > 0$ であることを示せ。また，$|\Psi_n\rangle$ がエネルギー $E_n > 0$，$\sigma_z$ の固有値 $1$ の同時固有状態ならば，$|\Phi_n\rangle = D|\Psi_n\rangle$ が同じエネルギー $E_n$ で，$\sigma_z$ の固有値 $-1$ の同時固有状態であることを，式 (8) と (9) を用いて示せ。

(5) エネルギー $E = 0$ の固有束縛状態 $|\Psi\rangle$ を考える。まず，$D|\Psi\rangle = 0$ を示せ。次に，ある関数 $\rho(x, y)$ を用いて，ベクトルポテンシャルを

$$
A_x(x, y) = -\frac{\partial\rho(x, y)}{\partial y},\qquad A_y(x, y) = +\frac{\partial\rho(x, y)}{\partial x} \tag{11}
$$

と表せるものとする。さらに $f_\uparrow(x, y)$ と $f_\downarrow(x, y)$ を

$$
\psi_\uparrow(x, y) = f_\uparrow(x, y)\exp\left[\frac{e}{\hbar}\rho(x, y)\right],\qquad \psi_\downarrow(x, y) = f_\downarrow(x, y)\exp\left[-\frac{e}{\hbar}\rho(x, y)\right] \tag{12}
$$

によって定義する。$|\Psi\rangle$ がエネルギー $E = 0$ の固有状態であるとき，$f_\uparrow(x, y)$ と $f_\downarrow(x, y)$ に対する方程式を求めよ。さらに，それを用いて，$f_\uparrow(x, y)$ は $w = x + iy$ の正則関数，$f_\downarrow(x, y)$ は $\bar{w} = x - iy$ の正則関数であることを説明せよ。

(6) 引き続きエネルギー $E = 0$ の固有束縛状態 $|\Psi\rangle$ を考える。式 (1) の磁束密度を再現する $\rho(x, y)$ は

$$
\rho(x, y) = \begin{cases} \dfrac{br^2}{4}, & (r < R), \\ \dfrac{bR^2}{2}\left(\dfrac{1}{2} + \log\dfrac{r}{R}\right), & (r \ge R) \end{cases} \tag{13}
$$

で与えられる。$\rho(x, y)$ の $r \to \infty$ での振舞いと，束縛状態の波動関数は規格化可能であることに注意して，スピンが上向きでエネルギーがゼロの束縛状態は存在しないことを示せ。また，スピンが下向きでエネルギーがゼロの束縛状態の波動関数には，一次独立なものがいくつあるか答えよ。ただし，$f_\uparrow(x, y)$ および $f_\downarrow(x, y)$ はそれぞれ $w$ および $\bar{w}$ の有限次多項式であると仮定してよい。

（この問題は Y. Aharonov and A. Casher, Phys. Rev. **A 19** (1979) 2461 を参考にした。）
{: .problem-lead }

> 出典：東京大学大学院理学系研究科物理学専攻 平成28年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
磁気モーメントの $g$ 因子がちょうど $2$ である2次元パウリ電子のハミルトニアンは，ディラック型演算子 $D = p_x\sigma_x + p_y\sigma_y$ の2乗 $H = D^2/(2m)$ として因数分解され（超対称量子力学の構造），すべてのエネルギー固有値が非負になるとともに，$E > 0$ の状態はスピン上向き・下向きで完全に対をなします。

一方，$E = 0$ の状態は1階の微分方程式 $D|\Psi\rangle = 0$ に従い，ベクトルポテンシャルをスカラーポテンシャル $\rho$ で表すと正則・反正則関数の問題へ整理されるため，遠方での規格化条件だけからゼロエネルギー束縛状態の個数が全磁束のみで決まること（アハラノフ・カッシャーの定理）が導かれます。
</div>

### (1)
パウリ行列の積 $\sigma_x\sigma_y = i\sigma_z,\ \sigma_y\sigma_x = -i\sigma_z$ より，

$$
[S_x, S_y] = \frac{\hbar^2}{4}\left(\sigma_x\sigma_y - \sigma_y\sigma_x\right) = \frac{\hbar^2}{4}(2i\sigma_z) = i\hbar\left(\frac{\hbar}{2}\sigma_z\right) = i\hbar S_z
$$

です。また式 (3) の $H$ は $\mathbf{1}_{2\times 2}$ と $\sigma_z$ のみを含み，空間演算子 $p_x, p_y, B_z(x, y)$ はスピン行列 $S_z = \dfrac{\hbar}{2}\sigma_z$ とすべて可換なので，$[H, S_z] = 0$ です。したがって，

$$
\finalanswer{[S_x, S_y] = i\hbar S_z,\qquad [H, S_z] = 0}
$$

### (2)
まずパウリ行列の反交換関係 $\sigma_x\sigma_z = -\sigma_z\sigma_x,\ \sigma_y\sigma_z = -\sigma_z\sigma_y$ より，

$$
D\sigma_z = (p_x\sigma_x + p_y\sigma_y)\sigma_z = -\sigma_z(p_x\sigma_x + p_y\sigma_y) = -\sigma_z D
$$

となり，式 (8) が成り立ちます。

次に $D^2$ を展開します。$\sigma_x^2 = \sigma_y^2 = \mathbf{1}_{2\times 2}$ および $\sigma_x\sigma_y = -\sigma_y\sigma_x = i\sigma_z$ を用います。

$$
\begin{aligned}
D^2
&= (p_x\sigma_x + p_y\sigma_y)(p_x\sigma_x + p_y\sigma_y) \\
&= \left(p_x^2 + p_y^2\right)\mathbf{1}_{2\times 2} + p_x p_y\sigma_x\sigma_y + p_y p_x\sigma_y\sigma_x \\
&= \left(p_x^2 + p_y^2\right)\mathbf{1}_{2\times 2} + i[p_x, p_y]\sigma_z
\end{aligned}
$$

任意の関数 $\psi(x, y)$ に $[p_x, p_y]$ を作用させて交換子を計算します。

$$
\begin{aligned}
[p_x, p_y]\psi
&= \left(-i\hbar\frac{\partial}{\partial x} + eA_x\right)\left(-i\hbar\frac{\partial\psi}{\partial y} + eA_y\psi\right)
 - \left(-i\hbar\frac{\partial}{\partial y} + eA_y\right)\left(-i\hbar\frac{\partial\psi}{\partial x} + eA_x\psi\right) \\
&= -i\hbar e\left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right)\psi = -i\hbar e B_z(x, y)\psi
\end{aligned}
$$

よって $i[p_x, p_y] = \hbar e B_z(x, y)$ となり，

$$
D^2 = \left(p_x^2 + p_y^2\right)\mathbf{1}_{2\times 2} + \hbar e B_z(x, y)\sigma_z = 2m H
$$

すなわち式 (9) $H = \dfrac{1}{2m}D^2$ が成り立ちます。

### (3)
$D = D^\dagger$ と式 (9) $D^2 = 2mH$，および $H|\Psi_n\rangle = E_n|\Psi_n\rangle$ を用います。

$$
\begin{aligned}
\langle\Phi_n|\Phi_n\rangle
&= \langle\Psi_n|D^\dagger D|\Psi_n\rangle \\
&= \langle\Psi_n|D^2|\Psi_n\rangle \\
&= 2m\langle\Psi_n|H|\Psi_n\rangle = 2m E_n \langle\Psi_n|\Psi_n\rangle
\end{aligned}
$$

よって式 (10) が成り立ちます。

### (4)
束縛状態 $|\Psi_n\rangle$ は零ベクトルではないので $\langle\Psi_n|\Psi_n\rangle > 0$ であり，またノルムの非負性より $\langle\Phi_n|\Phi_n\rangle \ge 0$ です。式 (10) より $E_n = \dfrac{\langle\Phi_n|\Phi_n\rangle}{2m\langle\Psi_n|\Psi_n\rangle} \ge 0$ であり，仮定 $E_n \neq 0$ から $E_n > 0$ です。

さらに $E_n > 0$ より $\langle\Phi_n|\Phi_n\rangle = 2m E_n\langle\Psi_n|\Psi_n\rangle > 0$ なので，$|\Phi_n\rangle = D|\Psi_n\rangle$ は零でない状態ベクトルです。式 (9) より $H$ と $D$ は可換（$HD = \dfrac{1}{2m}D^3 = DH$）なので，

$$
H|\Phi_n\rangle = HD|\Psi_n\rangle = DH|\Psi_n\rangle = E_n D|\Psi_n\rangle = E_n|\Phi_n\rangle
$$

となり，また式 (8) と $\sigma_z|\Psi_n\rangle = (+1)|\Psi_n\rangle$ より，

$$
\sigma_z|\Phi_n\rangle = \sigma_z D|\Psi_n\rangle = -D\sigma_z|\Psi_n\rangle = -D|\Psi_n\rangle = -|\Phi_n\rangle
$$

となります。よって $|\Phi_n\rangle$ はエネルギー $E_n$，$\sigma_z$ の固有値 $-1$ の同時固有状態です。

### (5)
$E = 0$ の固有束縛状態 $|\Psi\rangle$ に対して式 (10) を用いると $\|D|\Psi\rangle\|^2 = 2m\cdot 0\cdot\langle\Psi|\Psi\rangle = 0$ なので，$D|\Psi\rangle = 0$ です。

$D = p_x\sigma_x + p_y\sigma_y = \begin{pmatrix} 0 & p_x - ip_y \\ p_x + ip_y & 0 \end{pmatrix}$ より，$D|\Psi\rangle = 0$ は次の2つの1階偏微分方程式に分離されます。

$$
(p_x + ip_y)\psi_\uparrow = 0,\qquad (p_x - ip_y)\psi_\downarrow = 0
$$

式 (11) の $A_x = -\dfrac{\partial\rho}{\partial y},\ A_y = +\dfrac{\partial\rho}{\partial x}$ を代入すると，

$$
\begin{aligned}
A_x + i A_y &= i\left(\frac{\partial\rho}{\partial x} + i\frac{\partial\rho}{\partial y}\right) \\
A_x - i A_y &= -i\left(\frac{\partial\rho}{\partial x} - i\frac{\partial\rho}{\partial y}\right)
\end{aligned}
$$

なので，$p_x \pm ip_y$ は次のように整理されます。

$$
\begin{aligned}
(p_x + ip_y)\psi_\uparrow
&= -i\hbar\left[\left(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\right) - \frac{e}{\hbar}\left(\frac{\partial\rho}{\partial x} + i\frac{\partial\rho}{\partial y}\right)\right]\left(f_\uparrow e^{\frac{e}{\hbar}\rho}\right) \\
&= -i\hbar\,e^{\frac{e}{\hbar}\rho}\left(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\right)f_\uparrow = 0
\end{aligned}
$$

$$
\begin{aligned}
(p_x - ip_y)\psi_\downarrow
&= -i\hbar\left[\left(\frac{\partial}{\partial x} - i\frac{\partial}{\partial y}\right) + \frac{e}{\hbar}\left(\frac{\partial\rho}{\partial x} - i\frac{\partial\rho}{\partial y}\right)\right]\left(f_\downarrow e^{-\frac{e}{\hbar}\rho}\right) \\
&= -i\hbar\,e^{-\frac{e}{\hbar}\rho}\left(\frac{\partial}{\partial x} - i\frac{\partial}{\partial y}\right)f_\downarrow = 0
\end{aligned}
$$

よって $f_\uparrow,\ f_\downarrow$ に対する方程式は次のとおりです。したがって，

$$
\finalanswer{\left(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\right)f_\uparrow(x, y) = 0,\qquad \left(\frac{\partial}{\partial x} - i\frac{\partial}{\partial y}\right)f_\downarrow(x, y) = 0}
$$

**正則性の説明**：$w = x + iy,\ \bar{w} = x - iy$ に対するウィルティンガー微分は $\dfrac{\partial}{\partial\bar{w}} = \dfrac{1}{2}\left(\dfrac{\partial}{\partial x} + i\dfrac{\partial}{\partial y}\right)$，$\dfrac{\partial}{\partial w} = \dfrac{1}{2}\left(\dfrac{\partial}{\partial x} - i\dfrac{\partial}{\partial y}\right)$ です。上の方程式はそれぞれ $\dfrac{\partial f_\uparrow}{\partial\bar{w}} = 0$（実部・虚部について $w$ のコーシー・リーマン関係式）および $\dfrac{\partial f_\downarrow}{\partial w} = 0$（$\bar{w}$ のコーシー・リーマン関係式）であるため，$f_\uparrow(x, y)$ は $w$ の正則関数，$f_\downarrow(x, y)$ は $\bar{w}$ の正則関数です。

### (6)
$r \ge R$ において式 (13) より

$$
\exp\left[\pm\frac{e}{\hbar}\rho(x, y)\right] = \exp\left(\pm\frac{ebR^2}{4\hbar}\right)\left(\frac{r}{R}\right)^{\pm N_\Phi},\qquad N_\Phi \equiv \frac{ebR^2}{2\hbar} = \frac{e\Phi}{2\pi\hbar} > 0
$$

となります（ここで $\Phi = \pi R^2 b$ は全磁束です）。

**スピン上向き（$\psi_\uparrow$）**：$f_\uparrow(w)$ は $w$ の多項式なので，$f_\uparrow \not\equiv 0$ ならば最高次の次数を $k\ (\ge 0)$ として $r \to \infty$ で $|f_\uparrow(w)| \sim |c_k| r^k$ となります。したがって $|\psi_\uparrow(x, y)|^2 \propto r^{2(k + N_\Phi)}$ となり，$k + N_\Phi > 0$ より2次元積分

$$
\int_R^{\infty} |\psi_\uparrow|^2\,r\,\mathrm{d}r \propto \int_R^{\infty} r^{2k + 2N_\Phi + 1}\,\mathrm{d}r = \infty
$$

が発散します。ゆえに規格化可能なスピン上向きの $E = 0$ 束縛状態は存在しません。

**スピン下向き（$\psi_\downarrow$）**：単項式基底 $f_\downarrow(\bar{w}) = \bar{w}^k\ (k = 0, 1, 2, \dots)$ を考えます。原点付近 $r < R$ では滑らかで有界なので，規格化可能性は $r \to \infty$ の積分収束条件のみで決まります。

$$
\int_R^{\infty} |\psi_\downarrow|^2\,r\,\mathrm{d}r \propto \int_R^{\infty} r^{2k - 2N_\Phi + 1}\,\mathrm{d}r
$$

この積分が収束するための必要十分条件は，指数が $-1$ より小さいことです。

$$
2k - 2N_\Phi + 1 < -1 \iff k < N_\Phi - 1
$$

$k$ は非負整数（$k = 0, 1, 2, \dots$）なので，この不等式を満たす $k$ の個数は $N_\Phi = \dfrac{ebR^2}{2\hbar}$ に応じて次のようになります。

- $N_\Phi \le 1$ のとき：$0$ 個
- $N_\Phi > 1$ で $N_\Phi$ が非整数のとき：$k = 0, 1, \dots, \lfloor N_\Phi \rfloor - 1$ の計 $\lfloor N_\Phi \rfloor$ 個（ここで $\lfloor x \rfloor$ は $x$ を超えない最大の整数）
- $N_\Phi > 1$ で $N_\Phi$ が整数のとき：$k = 0, 1, \dots, N_\Phi - 2$ の計 $N_\Phi - 1$ 個

これらをまとめて，天井関数 $\lceil x \rceil$（$x$ 以上の最小の整数）を用いて $\max\bigl(0,\ \lceil N_\Phi \rceil - 1\bigr)$ 個と表すことができます。したがって，一次独立な状態の個数 $M$ は

$$
\finalanswer{M = \max\left(0,\ \left\lceil \frac{ebR^2}{2\hbar} \right\rceil - 1\right)}
$$

です（$N_\Phi = \dfrac{ebR^2}{2\hbar}$ が $1$ 以下のときは $0$ 個，$N_\Phi > 1$ のときは $N_\Phi$ より真に小さい最大の整数個です）。

<aside class="rigor-note" markdown>
問6の結果はアハラノフ・カッシャー（Aharonov–Casher）の定理として知られています。全磁束 $\Phi = \pi R^2 b$ を磁束量子 $\Phi_0 = h/e = 2\pi\hbar/e$ で割った無次元量 $N_\Phi = \Phi/\Phi_0$ だけでゼロエネルギー束縛状態の縮退度が決まり，磁場分布の細かな形には依存しません（トポロジカル不変量である指数定理の具体例です）。
</aside>
