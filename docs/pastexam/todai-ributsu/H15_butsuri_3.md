---
title: 東大理物 平成15年度 物理学 第3問：円筒導体内の偏心直線導線がつくる電磁場と鏡像法
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成15年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成15年度 物理学 第3問：円筒導体内の偏心直線導線がつくる電磁場と鏡像法

## 問題

真空中に無限に長い直線状導線と半径 $R\,[\mathrm{m}]$ の無限に長い中空の円筒導体が図1のように置かれている。導線は円筒の中心 O から $x$ 軸方向に $x_0\,[\mathrm{m}]$（$0 \le x_0 < R$）の位置にあるものとする。任意の点 A（中心 O から距離 $r\,[\mathrm{m}]$，$x$ 軸からの角度 $\phi\,[\mathrm{rad}]$）での動径方向と円周方向の電場を $E_r, E_\phi\,[\mathrm{V/m}]$，磁束密度を $B_r, B_\phi\,[\mathrm{Wb/m^2}]$ として，以下の設問に答えよ。ただし，真空中の誘電率と透磁率を $\epsilon_0, \mu_0$ とし，SI 単位系（MKSA 単位系）を用いるものとする。
{: .problem-lead }

<figure class="problem-figure" markdown>
![半径Rの円筒導体と中心からx0ずれた直線導線の断面図](../../assets/figures/pastexam-todai-ributsu/H15_butsuri_3-p-light.svg#only-light)
![半径Rの円筒導体と中心からx0ずれた直線導線の断面図](../../assets/figures/pastexam-todai-ributsu/H15_butsuri_3-p-dark.svg#only-dark)
<figcaption markdown="span">図1：半径 $R$ の中空円筒導体と，$x$ 軸上の $x_0$ に置かれた無限長直線導線の断面。</figcaption>
</figure>

まず，導線が円筒の中心 O にある場合（$x_0 = 0$）を考える。以下の設問に答えよ。

(1) 導線に電流 $I\,[\mathrm{A}]$ が紙面の下から上の方向に，円筒導体にはその反対方向に電流 $I\,[\mathrm{A}]$ が一様に流れているとする。円筒内（$r < R$）及び円筒外（$r > R$）の各領域で，磁束密度 $B_r, B_\phi\,[\mathrm{Wb/m^2}]$ を求めよ。

(2) 導線が $\lambda\,[\mathrm{C/m}]$ の線電荷密度（単位長さ当りの電荷）で一様に帯電している場合を考える。ただし，円筒は接地されているものとする。

(a) 円筒内（$r < R$）及び円筒外（$r > R$）の各領域で，電場 $E_r, E_\phi\,[\mathrm{V/m}]$ を求めよ。

(b) 円筒面に生じる面電荷密度 $\sigma\,[\mathrm{C/m^2}]$ と単位長さ当りの総電荷量 $\lambda_t\,[\mathrm{C/m}]$ を求めよ。

(c) 円筒が接地されずに絶縁されていた場合，電場は円筒内と円筒外でどうなるか。ただし，絶縁前に帯電はされていないものとする。

次に，導線が円筒導体の中心 O からずれている場合（$0 < x_0 < R$）を考える。以下の問いに答えよ。

(3) 設問 (1) と同様に，導線に電流 $I\,[\mathrm{A}]$ が紙面の下から上の方向に，円筒導体にはその反対方向に電流 $I\,[\mathrm{A}]$ が一様に流れている。円筒外（$r > R$）での磁束密度 $B_r, B_\phi\,[\mathrm{Wb/m^2}]$ を求めよ。

(4) 設問 (2) と同様に，導線が $\lambda\,[\mathrm{C/m}]$ の線電荷密度（単位長さ当りの電荷）で一様に帯電している。ただし，円筒は接地されているものとする。

(a) 円筒導体に対する電気映像が，中心 O から $x$ 軸方向に $R^2/x_0$ 離れた位置にある線電荷密度 $-\lambda$ の無限に長い導線であることを示し，円筒内での電場 $E_r, E_\phi\,[\mathrm{V/m}]$ を求めよ。

(b) 円筒面に生じる面電荷密度 $\sigma\,[\mathrm{C/m^2}]$ を求めよ。

(c) 円筒を左右半分に分けて考えた時，$x > 0$ の部分（$0^\circ \le \phi < 90^\circ$ 及び $270^\circ < \phi \le 360^\circ$）と $x < 0$ の部分（$90^\circ < \phi < 270^\circ$）の半円筒面に帯電する単位長さ当りの電荷 $\lambda_+, \lambda_-\,[\mathrm{C/m}]$ をそれぞれ求め，

$$
\frac{\lambda_+ - \lambda_-}{\lambda_+ + \lambda_-} = S \cdot x_0
$$

となる $S$ を求めよ。ただし，$x_0 \ll R$ として考えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成15年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半の同軸配置では，円筒対称性からアンペールの法則とガウスの法則だけで円筒内外の磁場と電場が定まります。

後半の偏心配置では，磁場は導線と円筒の電流がつくる磁場の重ね合わせとして成分計算し，電場は接地円筒面が等電位面となるように鏡像線電荷を配置して求めます。面電荷密度を左右の半円筒で積分することで，導線の位置ずれに対する感度 $S$ が得られます。
</div>

### (1)

$x_0 = 0$ のとき系は軸対称であり，磁場は動径成分をもたず $B_r = 0$ であり，$B_\phi$ は $r$ のみに依存します。中心 O を中心とする半径 $r$ の円周に沿ってアンペールの法則 $\oint \boldsymbol{B}\cdot\mathrm{d}\boldsymbol{\ell} = \mu_0 I_{\mathrm{enc}}$ を用います。

$r < R$ では円周内を貫く電流は導線の $+I$ のみなので，$2\pi r B_\phi = \mu_0 I$ です。

$$
B_r = 0, \qquad B_\phi = \frac{\mu_0 I}{2\pi r}
$$

$r > R$ では円周内を貫く正味の電流は $I + (-I) = 0$ なので，$2\pi r B_\phi = 0$ です。

$$
B_r = 0, \qquad B_\phi = 0
$$

したがって，各領域での磁束密度は次式となります。

$$
\finalanswer{
\begin{aligned}
r < R &: \quad B_r = 0, \qquad B_\phi = \frac{\mu_0 I}{2\pi r} \\
r > R &: \quad B_r = 0, \qquad B_\phi = 0
\end{aligned}
}
$$

### (2)

#### (a)

軸対称性より $E_\phi = 0$ であり，$E_r$ は $r$ のみに依存します。中心 O を軸とする半径 $r$，単位長さの円筒閉曲面に対してガウスの法則 $\iint \boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = \dfrac{Q_{\mathrm{enc}}}{\epsilon_0}$ を用います。

$r < R$ では内部の単位長さあたりの電荷は $\lambda$ なので，$2\pi r E_r = \dfrac{\lambda}{\epsilon_0}$ です。一方，$r > R$ では接地された円筒導体の電位と無限遠の電位がいずれも $0$ で等しく，導体外部に電荷が存在しないため，電場は恒等的に $0$ です。

$$
\finalanswer{
\begin{aligned}
r < R &: \quad E_r = \frac{\lambda}{2\pi\epsilon_0 r}, \qquad E_\phi = 0 \\
r > R &: \quad E_r = 0, \qquad E_\phi = 0
\end{aligned}
}
$$

#### (b)

円筒導体の内面 $r = R$ の直内側の電場は $E_r(R^-) = \dfrac{\lambda}{2\pi\epsilon_0 R}$，導体内部の電場は $0$ です。円筒面を挟む微小なガウス閉曲面を考えると，面電荷密度 $\sigma$ は $\sigma = \epsilon_0\bigl(0 - E_r(R^-)\bigr)$ となります。

$$
\begin{aligned}
\sigma &= -\epsilon_0\cdot\frac{\lambda}{2\pi\epsilon_0 R} \\
&= -\frac{\lambda}{2\pi R}
\end{aligned}
$$

単位長さあたりの総電荷量 $\lambda_t$ は全円周にわたって積分します。

$$
\begin{aligned}
\lambda_t &= 2\pi R\sigma \\
&= -\lambda
\end{aligned}
$$

$$
\finalanswer{\sigma = -\frac{\lambda}{2\pi R}, \qquad \lambda_t = -\lambda}
$$

#### (c)

円筒が絶縁されていて初期に帯電していない場合，導体内部の電場が $0$ であることから内面には依然として単位長さあたり $-\lambda$ の電荷が誘導されます。円筒全体の電荷保存により，円筒外面には単位長さあたり $+\lambda$ の電荷が一様に分布します。

したがって，円筒外 $r > R$ の半径 $r$ の円筒閉曲面内の正味電荷は $\lambda + (-\lambda) + \lambda = \lambda$ となり，円筒内と同様に $E_r = \dfrac{\lambda}{2\pi\epsilon_0 r}$ が生じます。円筒内 $r < R$ の電場は変わりません。

$$
\finalanswer{
\begin{aligned}
r < R &: \quad E_r = \frac{\lambda}{2\pi\epsilon_0 r}, \qquad E_\phi = 0 \\
r > R &: \quad E_r = \frac{\lambda}{2\pi\epsilon_0 r}, \qquad E_\phi = 0
\end{aligned}
}
$$

### (3)

円筒外 $r > R$ における磁束密度は，位置 $(x_0, 0)$ の導線電流 $+I$ がつくる磁束密度 $\boldsymbol{B}^{(1)}$ と，円筒導体に一様に流れる電流 $-I$ がつくる磁束密度 $\boldsymbol{B}^{(2)}$ の重ね合わせです。

まず円筒導体の電流 $-I$ は軸対称なので，$r > R$ において次式をつくります。

$$
B_r^{(2)} = 0, \qquad B_\phi^{(2)} = -\frac{\mu_0 I}{2\pi r}
$$

次に位置 $(x_0, 0)$ の導線から点 $\mathrm{A}(r\cos\phi, r\sin\phi)$ への相対位置ベクトルは $\Delta\boldsymbol{r} = (r\cos\phi - x_0,\ r\sin\phi)$ であり，その距離の2乗は $d^2 = r^2 + x_0^2 - 2rx_0\cos\phi$ です。紙面下から上へ向かう単位ベクトルを $\hat{\boldsymbol{z}}$ とすると，$\boldsymbol{B}^{(1)} = \dfrac{\mu_0 I}{2\pi d^2}(\hat{\boldsymbol{z}}\times\Delta\boldsymbol{r})$ です。

$$
\boldsymbol{B}^{(1)} = \frac{\mu_0 I}{2\pi d^2}\bigl(-r\sin\phi,\ r\cos\phi - x_0\bigr)
$$

動径方向の単位ベクトル $\hat{\boldsymbol{e}}_r = (\cos\phi, \sin\phi)$ と円周方向の単位ベクトル $\hat{\boldsymbol{e}}_\phi = (-\sin\phi, \cos\phi)$ との内積をそれぞれ計算します。

$$
\begin{aligned}
B_r^{(1)} &= \frac{\mu_0 I}{2\pi d^2}\bigl(-r\sin\phi\cos\phi + (r\cos\phi - x_0)\sin\phi\bigr) \\
&= -\frac{\mu_0 I x_0\sin\phi}{2\pi(r^2 + x_0^2 - 2rx_0\cos\phi)}
\end{aligned}
$$

$$
\begin{aligned}
B_\phi^{(1)} &= \frac{\mu_0 I}{2\pi d^2}\bigl(r\sin^2\phi + (r\cos\phi - x_0)\cos\phi\bigr) \\
&= \frac{\mu_0 I(r - x_0\cos\phi)}{2\pi(r^2 + x_0^2 - 2rx_0\cos\phi)}
\end{aligned}
$$

$\boldsymbol{B}^{(1)}$ と $\boldsymbol{B}^{(2)}$ を足し合わせて整理します。

$$
\begin{aligned}
B_\phi &= \frac{\mu_0 I}{2\pi}\left(\frac{r - x_0\cos\phi}{r^2 + x_0^2 - 2rx_0\cos\phi} - \frac{1}{r}\right) \\
&= \frac{\mu_0 I}{2\pi}\frac{r(r - x_0\cos\phi) - (r^2 + x_0^2 - 2rx_0\cos\phi)}{r(r^2 + x_0^2 - 2rx_0\cos\phi)} \\
&= \frac{\mu_0 I x_0(r\cos\phi - x_0)}{2\pi r(r^2 + x_0^2 - 2rx_0\cos\phi)}
\end{aligned}
$$

以上より，$r > R$ での磁束密度は次式となります。

$$
\finalanswer{B_r = -\frac{\mu_0 I x_0\sin\phi}{2\pi(r^2 + x_0^2 - 2rx_0\cos\phi)}, \qquad B_\phi = \frac{\mu_0 I x_0(r\cos\phi - x_0)}{2\pi r(r^2 + x_0^2 - 2rx_0\cos\phi)}}
$$

### (4)

#### (a)

位置 $(x_0, 0)$ の線電荷 $+\lambda$ と位置 $(x_1, 0)$（$x_1 = \dfrac{R^2}{x_0} > R$）の線電荷 $-\lambda$ が点 $\mathrm{A}(r, \phi)$ につくる静電ポテンシャル $V(r, \phi)$ を考えます。各線電荷からの距離を $d_0, d_1$ とおきます。

$$
d_0^2 = r^2 + x_0^2 - 2rx_0\cos\phi, \qquad d_1^2 = r^2 + x_1^2 - 2rx_1\cos\phi
$$

定数 $C$ を含めたポテンシャルは次式です。

$$
V(r, \phi) = \frac{\lambda}{4\pi\epsilon_0}\log\frac{d_1^2}{d_0^2} + C
$$

円筒面 $r = R$ 上で $d_1^2$ を計算し，$x_1 = \dfrac{R^2}{x_0}$ を代入します。

$$
\begin{aligned}
\left.d_1^2\right|_{r = R} &= R^2 + \frac{R^4}{x_0^2} - 2\frac{R^3}{x_0}\cos\phi \\
&= \frac{R^2}{x_0^2}\bigl(x_0^2 + R^2 - 2Rx_0\cos\phi\bigr) \\
&= \frac{R^2}{x_0^2}\left.d_0^2\right|_{r = R}
\end{aligned}
$$

したがって $r = R$ 上では比 $\dfrac{d_1^2}{d_0^2} = \dfrac{R^2}{x_0^2}$ が角度 $\phi$ によらず一定となります。定数を $C = -\dfrac{\lambda}{2\pi\epsilon_0}\log\dfrac{R}{x_0}$ と選ぶと，すべての $\phi$ に対して $V(R, \phi) = 0$ を満たします。鏡像線電荷は円筒外 $x_1 > R$ にあるため，円筒内 $r < R$ の電荷分布は元の問題と同一であり，境界条件も一致することから，解の一意性により $(R^2/x_0, 0)$ の線電荷 $-\lambda$ が求める電気映像です。

このポテンシャルを極座標で微分して円筒内 $r < R$ の電場 $E_r = -\dfrac{\partial V}{\partial r}$，$E_\phi = -\dfrac{1}{r}\dfrac{\partial V}{\partial\phi}$ を計算します。

$$
\begin{aligned}
E_r &= -\frac{\lambda}{4\pi\epsilon_0}\left(\frac{1}{d_1^2}\frac{\partial d_1^2}{\partial r} - \frac{1}{d_0^2}\frac{\partial d_0^2}{\partial r}\right) \\
&= \frac{\lambda}{2\pi\epsilon_0}\left(\frac{r - x_0\cos\phi}{r^2 + x_0^2 - 2rx_0\cos\phi} - \frac{r - x_1\cos\phi}{r^2 + x_1^2 - 2rx_1\cos\phi}\right)
\end{aligned}
$$

$$
\begin{aligned}
E_\phi &= -\frac{\lambda}{4\pi\epsilon_0 r}\left(\frac{1}{d_1^2}\frac{\partial d_1^2}{\partial\phi} - \frac{1}{d_0^2}\frac{\partial d_0^2}{\partial\phi}\right) \\
&= \frac{\lambda}{2\pi\epsilon_0}\left(\frac{x_0\sin\phi}{r^2 + x_0^2 - 2rx_0\cos\phi} - \frac{x_1\sin\phi}{r^2 + x_1^2 - 2rx_1\cos\phi}\right)
\end{aligned}
$$

$x_1 = \dfrac{R^2}{x_0}$ を用いると，円筒内の電場は次式となります。

$$
\finalanswer{
\begin{aligned}
E_r &= \frac{\lambda}{2\pi\epsilon_0}\left(\frac{r - x_0\cos\phi}{r^2 + x_0^2 - 2rx_0\cos\phi} - \frac{r - \dfrac{R^2}{x_0}\cos\phi}{r^2 + \dfrac{R^4}{x_0^2} - 2r\dfrac{R^2}{x_0}\cos\phi}\right) \\
E_\phi &= \frac{\lambda}{2\pi\epsilon_0}\left(\frac{x_0\sin\phi}{r^2 + x_0^2 - 2rx_0\cos\phi} - \frac{\dfrac{R^2}{x_0}\sin\phi}{r^2 + \dfrac{R^4}{x_0^2} - 2r\dfrac{R^2}{x_0}\cos\phi}\right)
\end{aligned}
}
$$

#### (b)

円筒面の内側の電場 $E_r(R^-, \phi)$ に $r = R$ および $d_1^2 = \dfrac{R^2}{x_0^2}d_0^2$ を代入して整理します。

$$
\begin{aligned}
E_r(R^-, \phi) &= \frac{\lambda}{2\pi\epsilon_0 d_0^2}\left\{R - x_0\cos\phi - \frac{x_0^2}{R^2}\left(R - \frac{R^2}{x_0}\cos\phi\right)\right\} \\
&= \frac{\lambda}{2\pi\epsilon_0 d_0^2}\left(R - \frac{x_0^2}{R}\right) \\
&= \frac{\lambda(R^2 - x_0^2)}{2\pi\epsilon_0 R(R^2 + x_0^2 - 2Rx_0\cos\phi)}
\end{aligned}
$$

面電荷密度 $\sigma = -\epsilon_0 E_r(R^-, \phi)$ は次式となります。

$$
\finalanswer{\sigma = -\frac{\lambda(R^2 - x_0^2)}{2\pi R(R^2 + x_0^2 - 2Rx_0\cos\phi)}}
$$

#### (c)

$x_0 \ll R$ より $\varepsilon = \dfrac{x_0}{R} \ll 1$ とおき，面電荷密度 $\sigma$ を $\varepsilon$ の1次まで展開します。

$$
\begin{aligned}
\sigma &= -\frac{\lambda}{2\pi R}\frac{1 - \varepsilon^2}{1 - 2\varepsilon\cos\phi + \varepsilon^2} \\
&\simeq -\frac{\lambda}{2\pi R}\bigl(1 + 2\varepsilon\cos\phi\bigr) \\
&= -\frac{\lambda}{2\pi R}\left(1 + \frac{2x_0}{R}\cos\phi\right)
\end{aligned}
$$

$x > 0$ の半円筒（$-\dfrac{\pi}{2} \le \phi \le \dfrac{\pi}{2}$）および $x < 0$ の半円筒（$\dfrac{\pi}{2} \le \phi \le \dfrac{3\pi}{2}$）にわたって $\sigma R\,\mathrm{d}\phi$ を積分します。

$$
\begin{aligned}
\lambda_+ &= \int_{-\pi/2}^{\pi/2} \sigma R\,\mathrm{d}\phi \\
&\simeq -\frac{\lambda}{2\pi}\int_{-\pi/2}^{\pi/2} \left(1 + \frac{2x_0}{R}\cos\phi\right)\mathrm{d}\phi \\
&= -\frac{\lambda}{2\pi}\left(\pi + \frac{4x_0}{R}\right) \\
&= -\frac{\lambda}{2}\left(1 + \frac{4x_0}{\pi R}\right)
\end{aligned}
$$

$$
\begin{aligned}
\lambda_- &= \int_{\pi/2}^{3\pi/2} \sigma R\,\mathrm{d}\phi \\
&\simeq -\frac{\lambda}{2\pi}\int_{\pi/2}^{3\pi/2} \left(1 + \frac{2x_0}{R}\cos\phi\right)\mathrm{d}\phi \\
&= -\frac{\lambda}{2\pi}\left(\pi - \frac{4x_0}{R}\right) \\
&= -\frac{\lambda}{2}\left(1 - \frac{4x_0}{\pi R}\right)
\end{aligned}
$$

これより比 $\dfrac{\lambda_+ - \lambda_-}{\lambda_+ + \lambda_-}$ を計算します。

$$
\begin{aligned}
\frac{\lambda_+ - \lambda_-}{\lambda_+ + \lambda_-} &= \frac{-\dfrac{4\lambda x_0}{\pi R}}{-\lambda} \\
&= \frac{4}{\pi R}x_0
\end{aligned}
$$

したがって，$\lambda_+, \lambda_-$ および $S$ は次式となります。

$$
\finalanswer{\lambda_+ = -\frac{\lambda}{2}\left(1 + \frac{4x_0}{\pi R}\right), \qquad \lambda_- = -\frac{\lambda}{2}\left(1 - \frac{4x_0}{\pi R}\right), \qquad S = \frac{4}{\pi R}}
$$
