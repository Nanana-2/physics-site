---
title: 東大理物 令和2年度 物理学 第3問：同軸ケーブル中の電磁波とTEMモード
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 令和2年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 令和2年度 物理学 第3問：同軸ケーブル中の電磁波とTEMモード

## 問題

同軸ケーブル中の電磁波の伝搬について考える。同軸ケーブルは図1に示すように，半径 $a$ の円柱芯線と中心軸を同じにして外側にある内半径 $b$ の円筒状導体から構成されている。円柱と円筒の間の空間は，誘電率 $\epsilon$，透磁率 $\mu$ の絶縁体で満たされているとする。外側の円筒の厚さは十分薄く，同軸ケーブルの長さは半径に比べて十分長く，かつ直線状であるとする。芯線および円筒状導体の電気抵抗は無視できるものとする。

同軸ケーブルに沿った方向を $z$ 軸とし，電場，磁場ともに $z$ 軸に平行な成分を持たない軸対称な伝搬モード（以下，TEM モードと呼ぶ）について考える。$\epsilon$ と $\mu$ は定数とする。絶縁体中の電磁波は Maxwell 方程式

$$
\nabla\times\boldsymbol E=-\frac{\partial\boldsymbol B}{\partial t}\tag{1}
$$

$$
\nabla\times\boldsymbol B=\mu\epsilon\frac{\partial\boldsymbol E}{\partial t}\tag{2}
$$

$$
\nabla\cdot\boldsymbol B=0\tag{3}
$$

$$
\nabla\cdot\boldsymbol E=0\tag{4}
$$

に従う。ここで $\boldsymbol{E}$ は電場，$\boldsymbol{B}$ は磁束密度である。以下，図1に示す円筒座標系 $(r, \theta, z)$ で考えることとする。任意の関数 $f$，ベクトル $\boldsymbol{A}$ に対する円筒座標系での勾配，発散，回転はそれぞれ

$$
\begin{aligned}
\nabla f &= \frac{\partial f}{\partial r}\mathbf{e}_r + \frac{1}{r}\frac{\partial f}{\partial\theta}\mathbf{e}_\theta + \frac{\partial f}{\partial z}\mathbf{e}_z \\
\nabla\cdot\boldsymbol{A} &= \frac{1}{r}\left[\frac{\partial}{\partial r}(r A_r) + \frac{\partial A_\theta}{\partial\theta} + r\frac{\partial A_z}{\partial z}\right] \\
\nabla\times\boldsymbol{A} &= \left[\frac{1}{r}\frac{\partial A_z}{\partial\theta} - \frac{\partial A_\theta}{\partial z}\right]\mathbf{e}_r + \left[\frac{\partial A_r}{\partial z} - \frac{\partial A_z}{\partial r}\right]\mathbf{e}_\theta + \frac{1}{r}\left[\frac{\partial}{\partial r}(r A_\theta) - \frac{\partial A_r}{\partial\theta}\right]\mathbf{e}_z
\end{aligned}
$$

で与えられる。$\mathbf{e}_r,\ \mathbf{e}_\theta,\ \mathbf{e}_z$ はそれぞれ $r, \theta, z$ 方向の単位ベクトルである。以下の設問に答えよ。

<figure class="problem-figure" markdown>
![同軸ケーブルと円筒座標系](../../../docs/assets/figures/pastexam-todai-ributsu/R2_butsuri_3-p-light.svg#only-light)
![同軸ケーブルと円筒座標系](../../../docs/assets/figures/pastexam-todai-ributsu/R2_butsuri_3-p-dark.svg#only-dark)
<figcaption markdown="span">図1：</figcaption>
</figure>

(1) この TEM モードの磁束密度の $r$ 方向成分 $B_r$，電場の $\theta$ 方向成分 $E_\theta$ はともにゼロとなることを示せ。

(2) $E_r(r, z, t)$ に対する波動方程式を求めよ。

(3) $z$ 方向の波数を $k$，角周波数を $\omega$ として，電場および磁束密度を複素表示でそれぞれ

$$
E_r(r, z, t) = \mathcal{E}(r) e^{ikz - i\omega t},\qquad B_\theta(r, z, t) = \mathcal{B}(r) e^{ikz - i\omega t}
$$

と記述する。$\mathcal{E}(r = a) = E_0$ としたとき，$\mathcal{E}(r)$ を求めよ。

(4) 同軸ケーブルを伝搬する電磁波の位相速度を求めよ。

(5) 同軸ケーブル断面を通過する単位時間あたりの電磁波のエネルギーを求めよ。

(6) 位置 $z$，時刻 $t$ における円筒状導体に対する芯線の電圧 $V(z, t)$ を求めよ。

(7) 設問6で求めた電圧 $V$ と，芯線を流れる電流 $I$ の比 $V(z, t)/I(z, t)$ は特性インピーダンス $Z_0$ と呼ばれる。$Z_0$ を求めよ。

次に，同軸ケーブルを伝搬するパルスを考える。その電圧を $V(z, t)$ で表す。以下，$\epsilon$ および $\mu$ は周波数の関数であり，$\omega$ は波数 $k$ の関数とする。$V(z, t)$ の複素表示を波数 $k$ の波の重ね合わせとして

$$
V(z, t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} v(k) e^{ikz - i\omega(k)t}\,dk
$$

と表す。

(8) $v(k)$ がある波数 $k_0$ を中心とする狭い範囲でのみ $0$ でない値をとり，$\omega(k)$ が定数 $A$ を用いて

$$
\omega(k) = \omega(k_0) + A(k - k_0)
$$

と近似できるとき，複素表示での電圧パルスの振幅 $|V(z, t)|$ は，その波形を変えずに同軸ケーブル中を伝搬することを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 令和2年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
同軸ケーブルを伝わる波では，場が軸のまわりで対称で，進む向きの成分 $E_z$，$B_z$ がありません。この条件をマクスウェル方程式に入れると，残る成分は $E_r$ と $B_\theta$ だけになり，それぞれが波動方程式を満たします。

場が求まれば，運ばれる電力はポインティングベクトルを断面で積分して求めます。電圧は電場を $r$ で積分して，電流は芯線のまわりの磁場から求めます。

パルスは波数の異なる波の重ね合わせです。$\omega(k)$ が $k$ の1次式なら，どの波も同じ速さで進むので，パルスは形を変えずに進みます。
</div>

### (1)
TEM モードの仮定より $E_z = 0,\ B_z = 0$，軸対称性より $\dfrac{\partial}{\partial\theta} = 0$ です。

まず式 (3) $\nabla\cdot\boldsymbol{B} = 0$ を円筒座標系で書きます。

$$
\begin{aligned}
\frac{1}{r}\frac{\partial}{\partial r}(r B_r) &= 0 \\
r B_r &= f(z, t)
\end{aligned}
$$

ここで $f(z,t)$ は $r$ によらない関数です。完全導体内では電場が0なので，ファラデーの法則から磁束密度の時間変化は0です。したがって，伝搬する時間依存成分の磁束密度は導体内で0です。法線成分の連続性から $B_r(a,z,t)=0$ となり，$f(z,t)=0$ です。以下では，時間によらない外部磁場を加えず，この伝搬成分を扱います。

次に式 (1) $\nabla\times\boldsymbol{E} = -\dfrac{\partial\boldsymbol{B}}{\partial t}$ の $z$ 成分を書きます。$B_z = 0$ かつ $\dfrac{\partial}{\partial\theta} = 0$ より，

$$
\begin{aligned}
\frac{1}{r}\frac{\partial}{\partial r}(r E_\theta) &= 0 \\
r E_\theta &= g(z, t)
\end{aligned}
$$

となります。完全導体表面では電場の接線成分が $0$ であることから $r = a$ で $E_\theta = 0$ なので， $g(z, t) = a E_\theta(a, z, t) = 0$ となり，すべての $r\ (a < r < b)$ で $E_\theta = 0$ が成り立ちます。

### (2)
問1より，$0$ でない電磁場成分は $E_r(r, z, t)$ と $B_\theta(r, z, t)$ のみです。式 (1) の $\theta$ 成分と式 (2) の $r$ 成分を円筒座標系で書きます。

$$
\frac{\partial E_r}{\partial z} = -\frac{\partial B_\theta}{\partial t}, \qquad -\frac{\partial B_\theta}{\partial z} = \mu\epsilon\frac{\partial E_r}{\partial t}
$$

第1式を $z$ で偏微分し，第2式を $t$ で偏微分して，両式を組み合わせます。

$$
\begin{aligned}
\frac{\partial^2 E_r}{\partial z^2} &= -\frac{\partial^2 B_\theta}{\partial z\,\partial t} \\
&= \mu\epsilon\frac{\partial^2 E_r}{\partial t^2}
\end{aligned}
$$

したがって，

$$
\finalanswer{\frac{\partial^2 E_r}{\partial z^2} - \mu\epsilon\frac{\partial^2 E_r}{\partial t^2} = 0}
$$

### (3)
式 (4) $\nabla\cdot\boldsymbol{E} = 0$ を円筒座標系で書きます。 $E_\theta = E_z = 0$ です。

$$
\frac{1}{r}\frac{\partial}{\partial r}(r E_r) = 0
$$

$E_r(r, z, t) = \mathcal{E}(r) e^{ikz - i\omega t}$ を代入すると，

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}r}\bigl(r\mathcal{E}(r)\bigr) &= 0 \\
\mathcal{E}(r) &= \frac{C}{r}
\end{aligned}
$$

となります。$C$ は定数です。条件 $\mathcal{E}(a) = E_0$ より $C = a E_0$ です。したがって，

$$
\finalanswer{\mathcal{E}(r) = \frac{a E_0}{r}}
$$

### (4)
問2の波動方程式に $E_r(r, z, t) = \mathcal{E}(r) e^{ikz - i\omega t}$ を代入します。

$$
\begin{aligned}
\left(-k^2 + \mu\epsilon\omega^2\right)\mathcal{E}(r) e^{ikz - i\omega t} &= 0 \\
k^2 &= \mu\epsilon\omega^2
\end{aligned}
$$

$\omega > 0,\ k > 0$ とすると，位相速度 $v_{\mathrm{p}} = \dfrac{\omega}{k}$ は次のようになります。したがって，

$$
\finalanswer{v_{\mathrm{p}} = \frac{1}{\sqrt{\mu\epsilon}}}
$$

### (5)
問2の第1式 $\dfrac{\partial E_r}{\partial z} = -\dfrac{\partial B_\theta}{\partial t}$ に複素表示を代入します。

$$
\begin{aligned}
ik\mathcal{E}(r) &= i\omega\mathcal{B}(r) \\
\mathcal{B}(r) &= \frac{k}{\omega}\mathcal{E}(r) \\
&= \sqrt{\mu\epsilon}\,\frac{a E_0}{r}
\end{aligned}
$$

電磁波のエネルギー流束を表すポインティングベクトル $\boldsymbol{S} = \dfrac{1}{\mu}\boldsymbol{E}\times\boldsymbol{B}$ の $z$ 成分は $S_z = \dfrac{1}{\mu} E_r B_\theta$ です。時間平均をとると，複素表示に対して $\overline{S}_z = \dfrac{1}{2\mu}\operatorname{Re}\bigl(\mathcal{E}(r)\mathcal{B}^*(r)\bigr)$ となります。

$$
\begin{aligned}
\overline{S}_z(r) &= \frac{1}{2\mu}\sqrt{\mu\epsilon}\,\frac{a^2 |E_0|^2}{r^2} \\
&= \frac{1}{2}\sqrt{\frac{\epsilon}{\mu}}\,\frac{a^2 |E_0|^2}{r^2}
\end{aligned}
$$

これを同軸ケーブルの断面（$a \le r \le b,\ 0 \le \theta < 2\pi$）にわたって積分し，単位時間あたりの通過エネルギーの時間平均 $\overline{P}$ を求めます。

$$
\begin{aligned}
\overline{P}
&= \int_0^{2\pi}\mathrm{d}\theta \int_a^b \overline{S}_z(r)\,r\,\mathrm{d}r \\
&= 2\pi \cdot \frac{1}{2}\sqrt{\frac{\epsilon}{\mu}}\,a^2 |E_0|^2 \int_a^b \frac{\mathrm{d}r}{r} \\
&= \pi\sqrt{\frac{\epsilon}{\mu}}\,a^2 |E_0|^2 \ln\left(\frac{b}{a}\right)
\end{aligned}
$$

$E_0$ を実数とし，$E_r=(aE_0/r)\cos(kz-\omega t)$ とすると，瞬時電力は

$$
\finalanswer{P(z,t)=2\pi\sqrt{\frac\epsilon\mu}a^2E_0^2\ln\left(\frac ba\right)\cos^2(kz-\omega t)}
$$

です。時間平均すると，

$$
\finalanswer{\overline{P} = \pi\sqrt{\frac{\epsilon}{\mu}}\,a^2 |E_0|^2 \ln\left(\frac{b}{a}\right)}
$$

### (6)
$r=b$ の外側導体を基準とした $r=a$ の芯線の電圧 $V(z, t)$ は，電場の線積分で与えられます。

$$
\begin{aligned}
V(z, t) &= -\int_b^a E_r(r, z, t)\,\mathrm{d}r \\
&= \int_a^b \frac{a E_0}{r} e^{ikz - i\omega t}\,\mathrm{d}r \\
&= a E_0 \ln\left(\frac{b}{a}\right) e^{ikz - i\omega t}
\end{aligned}
$$

したがって，

$$
\finalanswer{V(z, t) = a E_0 \ln\left(\frac{b}{a}\right) e^{ikz - i\omega t}}
$$

### (7)
芯線のすぐ外側 $r\to a+0$ の円周に沿って，式 (2) の積分形を用います。断面 $r<a$ では完全導体内部の電場が0なので，変位電流の寄与はありません。芯線を $z$ 軸正方向に流れる電流を $I(z,t)$ とすると，

$$
\begin{aligned}
\oint_{r=a} \boldsymbol{B}\cdot\mathrm{d}\boldsymbol{\ell} &= 2\pi a B_\theta(a, z, t) \\
&= \mu I(z, t)
\end{aligned}
$$

問5より $B_\theta(a, z, t) = \sqrt{\mu\epsilon}\,E_0 e^{ikz - i\omega t}$ なので，

$$
\begin{aligned}
I(z, t) &= \frac{2\pi a}{\mu}\sqrt{\mu\epsilon}\,E_0 e^{ikz - i\omega t} \\
&= 2\pi a\sqrt{\frac{\epsilon}{\mu}}\,E_0 e^{ikz - i\omega t}
\end{aligned}
$$

となります。問6の $V(z, t)$ との比をとって特性インピーダンス $Z_0$ を求めます。

$$
\begin{aligned}
Z_0 &= \frac{V(z, t)}{I(z, t)} \\
&= \frac{a E_0 \ln(b/a)}{2\pi a\sqrt{\epsilon/\mu}\,E_0} \\
&= \frac{1}{2\pi}\sqrt{\frac{\mu}{\epsilon}}\ln\left(\frac{b}{a}\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{Z_0 = \frac{1}{2\pi}\sqrt{\frac{\mu}{\epsilon}}\ln\left(\frac{b}{a}\right)}
$$

### (8)
$\omega(k) = \omega(k_0) + A(k - k_0)$ を $V(z, t)$ の積分に代入し，波数 $k$ に依存しない位相因子を積分の外へ出します。

$$
\begin{aligned}
V(z, t)
&= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} v(k)\exp\Bigl[ikz - i\bigl(\omega(k_0) + A(k - k_0)\bigr)t\Bigr]\,\mathrm{d}k \\
&= e^{-i(\omega(k_0) - A k_0)t} \cdot \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} v(k) e^{ik(z - At)}\,\mathrm{d}k \\
&= e^{-i(\omega(k_0) - A k_0)t}\,V(z - At, 0)
\end{aligned}
$$

ここで $\left|e^{-i(\omega(k_0) - A k_0)t}\right| = 1$ なので，両辺の絶対値をとると次式が得られます。

$$
|V(z, t)| = |V(z - At, 0)|
$$

これは，時刻 $t = 0$ の振幅の波形 $|V(z, 0)|$ を，$z$ 方向に $At$ だけずらしたものです。したがって，電圧パルスの振幅 $|V(z, t)|$ は，波形を変えずに一定の速さ $A$ で進みます。

<aside class="rigor-note" markdown>
問5〜7の結果には，次の関係が成り立ちます。

$$
\begin{aligned}
\frac{|V|^2}{2Z_0}&=\frac{a^2|E_0|^2[\ln(b/a)]^2}{2(2\pi)^{-1}\sqrt{\mu/\epsilon}\ln(b/a)}\\
&=\pi\sqrt{\frac\epsilon\mu}a^2|E_0|^2\ln(b/a)\\
&=\overline P
\end{aligned}
$$

問8の定数 $A$ は $\omega'(k_0)$ です。波形が保たれるのは，重ね合わせに含まれる波数と伝搬時間の範囲で，無視した2次以上の位相の変化が十分小さい場合です。
</aside>
