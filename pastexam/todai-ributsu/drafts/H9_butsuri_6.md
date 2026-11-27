---
title: 東大理物 平成9年度 物理学 第6問：非圧縮液滴の4重極表面振動と量子コヒーレント状態
tags:
  - 院試過去問
  - 東大理物
  - 力学
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 物理学
exam_number: 第6問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成9年度 物理学 第6問：非圧縮液滴の4重極表面振動と量子コヒーレント状態

## 問題

一様密度 $\rho_0$ で非圧縮性の液滴を考えよう。液滴は，ある初期条件のもとでその内部に渦の無い流れを生じ，時間とともに形を変えていくものとする。
{: .problem-lead }

(1) 液滴内部の速度分布を $\vec{v}(\vec{r}, t)$ として，以下の問いに答えよ。

(i) 連続の方程式を用いて，非圧縮性の条件を $\vec{v}(\vec{r}, t)$ に対する式として表せ。また，流れに渦が無いときには，$\vec{v} = -\operatorname{grad}\chi$ となる速度ポテンシャル $\chi(\vec{r}, t)$ が存在してラプラスの方程式

$$
\Delta\chi(\vec{r}, t) = 0
$$

を満たすことを示せ。

(ii) 上式の解は

$$
\chi(\vec{r}, t) = \sum_{\ell m} a_{\ell m}(t) f_\ell(r) Y_{\ell m}(\theta, \varphi)
$$

と書ける。このとき，動径関数は

$$
\left\{\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}r^2\frac{\mathrm{d}}{\mathrm{d}r} - \frac{\ell(\ell + 1)}{r^2}\right\}f_\ell(r) = 0
$$

に従う。この方程式の液滴内部で正則な解は $f_\ell(r) = r^\ell$ であることを示せ。その際，他の独立解は原点（$r = 0$）で正則でないことを確かめよ。

(2) 液滴の重心から $(\theta, \varphi)$ 方向を見たとき，表面までの距離が

$$
R(\theta, \varphi, t) = R_0 + q(t)Y_{20}(\theta, \varphi)
$$

と変動する場合を考える。以下では，変動の大きさ $|q(t)|$ が $R_0$ に比べて十分に小さいものとする。

(i) 液滴表面までの距離は，内部から表面へ向かって液体が流れることによって変化する。そこで，

$$
\frac{\partial}{\partial t}R(\theta, \varphi, t) = -\left.\frac{\partial}{\partial r}\chi(r, \theta, \varphi, t)\right|_{r = R}
$$

の関係が成り立つとして，速度ポテンシャル $\chi(\vec{r}, t)$ を $\dot{q}(t)$（$\equiv \dfrac{\mathrm{d}q}{\mathrm{d}t}$）を用いて表せ。ただし，変形は微小なので，右辺で $r = R$ を $r = R_0$ と近似して良いものとする。

(ii) 液滴内部の速度分布 $(v_x, v_y, v_z)$ を，$Y_{20}(\theta, \varphi) = \sqrt{\dfrac{5}{16\pi}}(3\cos^2\theta - 1)$ を使って求めよ。次に，液滴内部の全運動エネルギーを計算せよ。ただし，積分は，変形が小さいとして，半径 $R_0$ の球内で行えば良い。

(iii) 体積を保存した上記の変形に伴い，液滴の表面積は球形のときより $2q^2(t)$ だけ増加することが知られている。液滴の表面張力を $\sigma$ として，変形によるポテンシャル・エネルギーの変化を求めよ。

(3) ここで，量子的サイズの液滴の運動を考えよう。

(i) 上記 (2) の液滴の変形に伴うハミルトニアンは，お互いに正準共役な演算子 $\hat{q}, \hat{p}$ を用いて

$$
\hat{H} = \frac{1}{2M}\bigl\{\hat{p}^2 + (M\omega\hat{q})^2\bigr\}
$$

と表される。ここで，

$$
\hat{q} = \sqrt{\frac{\hbar}{2M\omega}}(\hat{a}^\dagger + \hat{a}),\qquad \hat{p} = i\sqrt{\frac{\hbar M\omega}{2}}(\hat{a}^\dagger - \hat{a})
$$

の関係にある演算子 $\hat{a}^\dagger$ および $\hat{a}$（交換関係は $[\hat{a}, \hat{a}^\dagger] = 1$）を導入すれば，そのハミルトニアンは

$$
\hat{H} = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right)
$$

と書ける。$M$ および $\omega$ を $\rho_0, R_0, \sigma$ を用いて表せ。

(ii) ハイゼンベルク表示の演算子 $\hat{a}_{\mathrm{H}}(t) \equiv e^{i\hat{H}t/\hbar}\hat{a}e^{-i\hat{H}t/\hbar}$ の運動方程式を考えて，

$$
\hat{a}_{\mathrm{H}}(t) = e^{-i\omega t}\hat{a}
$$

が成り立つことを示せ。

(iii) 演算子 $\hat{a}$ の固有状態 $|z_0\rangle$；

$$
\hat{a}|z_0\rangle = z_0|z_0\rangle,\qquad z_0 = i\sqrt{\frac{M\omega}{2\hbar}}A_0
$$

を考える。$A_0$ は実定数で，$R_0$ に比べれば十分に小さい値であるとする。この $|z_0\rangle$ を初期状態とする状態 $|\psi(t)\rangle$（$= e^{-i\hat{H}t/\hbar}|z_0\rangle$）は，任意の時刻においてもやはり $\hat{a}$ の固有状態であることを示せ。また，その固有値 $z(t)$ を求めよ。

(iv) 状態 $|\psi(t)\rangle$ における $\hat{q}$ および $\hat{p}$ の期待値を求め，$A_0$ が何を意味するかについて述べよ。また，$A_0 \to 0$ のとき，エネルギーの値がどうなるかを答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 物理学 第6問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
密度一定の非圧縮流体では連続の方程式から $\nabla\cdot\vec{v} = 0$ が導かれ，渦なしの条件から速度ポテンシャル $\chi$ がラプラス方程式を満たします。そのため表面の微小な $Y_{20}$ 変形に対する内部流れは $r^2 Y_{20}$ の1項だけで定まり，運動エネルギーは $\dot{q}^2$ に比例する1自由度調和振動子になります。

量子化した後は，消滅演算子 $\hat{a}$ のハイゼンベルク表示が位相因子 $e^{-i\omega t}$ を掛けて時間発展する性質を用いることで，$\hat{a}$ の固有状態が任意の時刻でも固有状態のままで保たれ，期待値が古典的な単振動を描くことを導きます。
</div>

### (1)(i)

流体の密度を $\rho(\vec{r}, t)$ とすると，質量保存を表す連続の方程式は次の通りです。

$$
\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v}) = 0
$$

液滴は一様密度 $\rho_0$ の非圧縮性流体なので，$\rho(\vec{r}, t) = \rho_0$ は時間にも空間にもよらない定数です。したがって $\dfrac{\partial\rho}{\partial t} = 0$ および $\nabla\cdot(\rho_0\vec{v}) = \rho_0\nabla\cdot\vec{v}$ となり，非圧縮性の条件が得られます。

$$
\nabla\cdot\vec{v}(\vec{r}, t) = 0
$$

また流れに渦がないとき，速度場の回転は恒等的に $\nabla\times\vec{v} = \vec{0}$ です。液滴内部の単連結な領域において回転が $0$ のベクトル場は適当なスカラー場 $\chi(\vec{r}, t)$ の勾配として $\vec{v} = -\nabla\chi$ と表すことができます。これを非圧縮性の条件 $\nabla\cdot\vec{v} = 0$ に代入します。

$$
\begin{aligned}
\nabla\cdot(-\nabla\chi) &= 0 \\
\Delta\chi(\vec{r}, t) &= 0
\end{aligned}
$$

よって速度ポテンシャル $\chi(\vec{r}, t)$ はラプラスの方程式を満たします。

### (1)(ii)

動径方程式を展開します。

$$
\frac{\mathrm{d}^2 f_\ell}{\mathrm{d}r^2} + \frac{2}{r}\frac{\mathrm{d}f_\ell}{\mathrm{d}r} - \frac{\ell(\ell + 1)}{r^2}f_\ell = 0
$$

これはオイラー型の2階線形常微分方程式なので，$f_\ell(r) = r^\alpha$ を代入します。

$$
\begin{aligned}
\bigl(\alpha(\alpha - 1) + 2\alpha - \ell(\ell + 1)\bigr)r^{\alpha - 2} &= 0 \\
\bigl(\alpha(\alpha + 1) - \ell(\ell + 1)\bigr)r^{\alpha - 2} &= 0 \\
(\alpha - \ell)(\alpha + \ell + 1)r^{\alpha - 2} &= 0
\end{aligned}
$$

したがって特性根は $\alpha = \ell$ と $\alpha = -(\ell + 1)$ の2つであり，$\ell = 0, 1, 2, \dots$ に対して両者は常に異なるため，一般解は定数 $c_1, c_2$ を用いて次のように表されます。

$$
f_\ell(r) = c_1 r^\ell + c_2 r^{-(\ell + 1)}
$$

$\ell \ge 0$ より $\ell + 1 \ge 1$ であるため，他方の独立解 $r^{-(\ell + 1)}$ は原点 $r \to 0$ で発散し，原点で正則ではありません。一方 $r^\ell$ は原点を含め液滴内部全体で正則です。したがって液滴内部で正則な解は定数倍を除いて $f_\ell(r) = r^\ell$ に限られます。

### (2)(i)

(1)(ii) より液滴内部で正則な速度ポテンシャルは $\chi(r, \theta, \varphi, t) = \sum_{\ell m} a_{\ell m}(t) r^\ell Y_{\ell m}(\theta, \varphi)$ です。$r = R_0$ における表面の運動学的境界条件を計算します。

$$
\begin{aligned}
\frac{\partial R}{\partial t} &= \dot{q}(t)Y_{20}(\theta, \varphi) \\
-\left.\frac{\partial\chi}{\partial r}\right|_{r = R_0} &= -\sum_{\ell m} \ell a_{\ell m}(t) R_0^{\ell - 1} Y_{\ell m}(\theta, \varphi)
\end{aligned}
$$

両辺を比較し，球面調和関数 $Y_{\ell m}(\theta, \varphi)$ の直交性を用いて各 $(\ell, m)$ の係数を比較します。$\ell = 2, m = 0$ 以外の $\ell \ge 1$ の項はすべて $a_{\ell m}(t) = 0$ となり，$\ell = 2, m = 0$ については次式が得られます。

$$
-2 R_0 a_{20}(t) = \dot{q}(t)
$$

これより $a_{20}(t) = -\dfrac{\dot{q}(t)}{2R_0}$ です。なお $\ell = 0$ の空間定数項 $a_{00}(t)$ は速度 $\vec{v} = -\nabla\chi$ に寄与しないため $0$ に選べます。したがって速度ポテンシャルは次の通りです。

$$
\finalanswer{\chi(\vec{r}, t) = -\frac{\dot{q}(t)}{2R_0}r^2 Y_{20}(\theta, \varphi)}
$$

### (2)(ii)

$z = r\cos\theta$ および $r^2 = x^2 + y^2 + z^2$ を用いて，$r^2 Y_{20}(\theta, \varphi)$ を直交座標 $(x, y, z)$ で表します。

$$
\begin{aligned}
r^2 Y_{20}(\theta, \varphi) &= \sqrt{\frac{5}{16\pi}}\bigl(3r^2\cos^2\theta - r^2\bigr) \\
&= \sqrt{\frac{5}{16\pi}}\bigl(3z^2 - (x^2 + y^2 + z^2)\bigr) \\
&= \sqrt{\frac{5}{16\pi}}\bigl(2z^2 - x^2 - y^2\bigr)
\end{aligned}
$$

したがって速度ポテンシャルを直交座標で表すと次の通りです。

$$
\chi(x, y, z, t) = -\frac{\dot{q}(t)}{2R_0}\sqrt{\frac{5}{16\pi}}\bigl(2z^2 - x^2 - y^2\bigr)
$$

$\vec{v} = -\nabla\chi$ の各成分を偏微分して求めます。

$$
\begin{aligned}
v_x &= -\frac{\dot{q}(t)}{R_0}\sqrt{\frac{5}{16\pi}}\,x \\
v_y &= -\frac{\dot{q}(t)}{R_0}\sqrt{\frac{5}{16\pi}}\,y \\
v_z &= \frac{2\dot{q}(t)}{R_0}\sqrt{\frac{5}{16\pi}}\,z
\end{aligned}
$$

次に液滴内部の全運動エネルギー $T$ を半径 $R_0$ の球内で積分します。

$$
\begin{aligned}
T &= \frac{1}{2}\rho_0\int_{r \le R_0} (v_x^2 + v_y^2 + v_z^2)\,\mathrm{d}^3r \\
&= \frac{1}{2}\rho_0\frac{5\dot{q}^2}{16\pi R_0^2}\int_{r \le R_0} (x^2 + y^2 + 4z^2)\,\mathrm{d}^3r
\end{aligned}
$$

球領域 $r \le R_0$ の対称性より，$\int_{r \le R_0} x^2\,\mathrm{d}^3r$，$\int_{r \le R_0} y^2\,\mathrm{d}^3r$，$\int_{r \le R_0} z^2\,\mathrm{d}^3r$ はすべて等しく，それぞれの値は次の通りです。

$$
\begin{aligned}
\int_{r \le R_0} x^2\,\mathrm{d}^3r &= \frac{1}{3}\int_{r \le R_0} r^2\,\mathrm{d}^3r \\
&= \frac{1}{3}\int_0^{R_0} 4\pi r^4\,\mathrm{d}r \\
&= \frac{4\pi}{15}R_0^5
\end{aligned}
$$

したがって $\int_{r \le R_0}(x^2 + y^2 + 4z^2)\,\mathrm{d}^3r$ は $6 \cdot \dfrac{4\pi}{15}R_0^5$ すなわち $\dfrac{8\pi}{5}R_0^5$ となります。これを $T$ の式に代入します。

$$
\begin{aligned}
T &= \frac{1}{2}\rho_0\frac{5\dot{q}^2}{16\pi R_0^2}\cdot\frac{8\pi}{5}R_0^5 \\
&= \frac{1}{4}\rho_0 R_0^3 \dot{q}^2
\end{aligned}
$$

$$
\finalanswer{(v_x, v_y, v_z) = \frac{\dot{q}(t)}{R_0}\sqrt{\frac{5}{16\pi}}(-x, -y, 2z),\qquad T = \frac{1}{4}\rho_0 R_0^3 \dot{q}^2}
$$

### (2)(iii)

表面張力 $\sigma$ は単位面積当たりの表面エネルギーなので，球形からの表面積の増加分 $\Delta S = 2q^2(t)$ に対するポテンシャルエネルギーの変化 $V(q)$ は次の通りです。

$$
\finalanswer{V(q) = 2\sigma q^2(t)}
$$

### (3)(i)

(2)(ii) と (2)(iii) より，変形の座標 $q$ に対する古典ラグラジアンは $L = \dfrac{1}{4}\rho_0 R_0^3\dot{q}^2 - 2\sigma q^2$ です。$q$ に正準共役な運動量 $p = \dfrac{\partial L}{\partial\dot{q}}$ は $\dfrac{1}{2}\rho_0 R_0^3\dot{q}$ なので，これを用いてハミルトニアンを構成します。

$$
\begin{aligned}
H &= \frac{1}{2M}p^2 + \frac{1}{2}M\omega^2 q^2 \\
&= \frac{p^2}{\rho_0 R_0^3} + 2\sigma q^2
\end{aligned}
$$

係数を比較すると，$M$ と $M\omega^2$ は次のように定まります。

$$
\begin{aligned}
M &= \frac{1}{2}\rho_0 R_0^3 \\
\frac{1}{2}M\omega^2 &= 2\sigma
\end{aligned}
$$

第2式に $M$ を代入して $\omega > 0$ を求めます。

$$
\begin{aligned}
\omega^2 &= \frac{4\sigma}{M} \\
&= \frac{8\sigma}{\rho_0 R_0^3}
\end{aligned}
$$

$$
\finalanswer{M = \frac{1}{2}\rho_0 R_0^3,\qquad \omega = \sqrt{\frac{8\sigma}{\rho_0 R_0^3}}}
$$

### (3)(ii)

$\hat{a}_{\mathrm{H}}(t) = e^{i\hat{H}t/\hbar}\hat{a}e^{-i\hat{H}t/\hbar}$ を時刻 $t$ で微分してハイゼンベルクの運動方程式を立てます。

$$
\begin{aligned}
\frac{\mathrm{d}\hat{a}_{\mathrm{H}}(t)}{\mathrm{d}t} &= \frac{i}{\hbar}e^{i\hat{H}t/\hbar}[\hat{H}, \hat{a}]e^{-i\hat{H}t/\hbar} \\
&= i\omega e^{i\hat{H}t/\hbar}[\hat{a}^\dagger\hat{a}, \hat{a}]e^{-i\hat{H}t/\hbar}
\end{aligned}
$$

交換関係 $[\hat{a}, \hat{a}^\dagger] = 1$ より $[\hat{a}^\dagger\hat{a}, \hat{a}] = -\hat{a}$ なので，次式が成り立ちます。

$$
\begin{aligned}
\frac{\mathrm{d}\hat{a}_{\mathrm{H}}(t)}{\mathrm{d}t} &= -i\omega e^{i\hat{H}t/\hbar}\hat{a}e^{-i\hat{H}t/\hbar} \\
&= -i\omega\hat{a}_{\mathrm{H}}(t)
\end{aligned}
$$

初期条件 $\hat{a}_{\mathrm{H}}(0) = \hat{a}$ のもとでこの1階線形微分方程式を積分すると，求める式が導かれます。

$$
\hat{a}_{\mathrm{H}}(t) = e^{-i\omega t}\hat{a}
$$

### (3)(iii)

状態 $|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|z_0\rangle$ に $\hat{a}$ を左から作用させます。恒等式 $e^{-i\hat{H}t/\hbar}e^{i\hat{H}t/\hbar} = 1$ を挿入し，(3)(ii) の結果を用います。

$$
\begin{aligned}
\hat{a}|\psi(t)\rangle &= e^{-i\hat{H}t/\hbar}\left(e^{i\hat{H}t/\hbar}\hat{a}e^{-i\hat{H}t/\hbar}\right)|z_0\rangle \\
&= e^{-i\hat{H}t/\hbar}\hat{a}_{\mathrm{H}}(t)|z_0\rangle \\
&= e^{-i\hat{H}t/\hbar}e^{-i\omega t}\hat{a}|z_0\rangle \\
&= e^{-i\omega t}z_0 e^{-i\hat{H}t/\hbar}|z_0\rangle \\
&= z_0 e^{-i\omega t}|\psi(t)\rangle
\end{aligned}
$$

したがって $|\psi(t)\rangle$ は任意の時刻 $t$ において $\hat{a}$ の固有状態であり，その固有値 $z(t)$ は次の通りです。

$$
\finalanswer{z(t) = z_0 e^{-i\omega t} = i\sqrt{\frac{M\omega}{2\hbar}}A_0 e^{-i\omega t}}
$$

### (3)(iv)

状態 $|\psi(t)\rangle$ が $\langle\psi(t)|\psi(t)\rangle = 1$ と規格化されているとすると，(3)(iii) の固有値方程式 $\hat{a}|\psi(t)\rangle = z(t)|\psi(t)\rangle$ およびそのエルミート共役 $\langle\psi(t)|\hat{a}^\dagger = z^*(t)\langle\psi(t)|$ を用いて $\hat{q}$ と $\hat{p}$ の期待値を計算します。

まず $z(t)$ の実部と虚部を求めます。$A_0$ が実数なので，

$$
\begin{aligned}
z(t) &= i\sqrt{\frac{M\omega}{2\hbar}}A_0(\cos\omega t - i\sin\omega t) \\
&= \sqrt{\frac{M\omega}{2\hbar}}A_0(\sin\omega t + i\cos\omega t)
\end{aligned}
$$

です。これより $\langle\hat{q}\rangle$ と $\langle\hat{p}\rangle$ を計算します。

$$
\begin{aligned}
\langle\psi(t)|\hat{q}|\psi(t)\rangle &= \sqrt{\frac{\hbar}{2M\omega}}\bigl(z^*(t) + z(t)\bigr) \\
&= \sqrt{\frac{\hbar}{2M\omega}}\cdot 2\sqrt{\frac{M\omega}{2\hbar}}A_0\sin\omega t \\
&= A_0\sin\omega t
\end{aligned}
$$

$$
\begin{aligned}
\langle\psi(t)|\hat{p}|\psi(t)\rangle &= i\sqrt{\frac{\hbar M\omega}{2}}\bigl(z^*(t) - z(t)\bigr) \\
&= i\sqrt{\frac{\hbar M\omega}{2}}\left(-2i\sqrt{\frac{M\omega}{2\hbar}}A_0\cos\omega t\right) \\
&= M\omega A_0\cos\omega t
\end{aligned}
$$

したがって $|A_0|$ は液滴表面の4重極変形の期待値 $\langle\hat{q}\rangle = A_0\sin\omega t$ の振動振幅を表し，$A_0$ の符号は $t = 0$ で変形が始まる向きに対応します。

次にこの状態でのエネルギー期待値 $\langle\hat{H}\rangle$ を計算します。

$$
\begin{aligned}
\langle\psi(t)|\hat{H}|\psi(t)\rangle &= \hbar\omega\left(\langle\psi(t)|\hat{a}^\dagger\hat{a}|\psi(t)\rangle + \frac{1}{2}\right) \\
&= \hbar\omega\left(|z(t)|^2 + \frac{1}{2}\right) \\
&= \frac{1}{2}M\omega^2 A_0^2 + \frac{1}{2}\hbar\omega
\end{aligned}
$$

$A_0 \to 0$ の極限では古典的な振動エネルギー $\dfrac{1}{2}M\omega^2 A_0^2$ は $0$ になりますが，状態 $|\psi(t)\rangle$ は基底状態 $|0\rangle$ に一致し，エネルギーは $0$ にはならず零点エネルギー

$$
E_0 = \frac{1}{2}\hbar\omega = \hbar\sqrt{\frac{2\sigma}{\rho_0 R_0^3}}
$$

に近づきます。

$$
\finalanswer{\langle\hat{q}\rangle = A_0\sin\omega t,\qquad \langle\hat{p}\rangle = M\omega A_0\cos\omega t,\qquad \lim_{A_0 \to 0}\langle\hat{H}\rangle = \frac{1}{2}\hbar\omega = \hbar\sqrt{\frac{2\sigma}{\rho_0 R_0^3}}}
$$
