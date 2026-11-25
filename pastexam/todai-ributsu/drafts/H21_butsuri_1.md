---
title: 東大理物 平成21年度 物理学 第1問：不確定性関係とスピン1/2の相関
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成21年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成21年度 物理学 第1問：不確定性関係とスピン1/2の相関

## 問題

スピン角運動量について考える。$x, y, z$ 方向のスピン角運動量演算子をそれぞれ $s_x, s_y, s_z$ とすると，これらは交換関係 $[s_x, s_y] = i\hbar s_z$，$[s_y, s_z] = i\hbar s_x$，$[s_z, s_x] = i\hbar s_y$ を満たす。ただし $\hbar = h/(2\pi)$（$h$ はプランク定数）である。以下の設問に答えよ。

(1) 一般に，自己共役演算子 $P, Q$ が交換関係 $[P, Q] = iR$ を満たすとき，

(i) $P^\dagger = P,\ Q^\dagger = Q$ より，演算子 $R$ も自己共役（$R^\dagger = R$）であることを示せ。（$X^\dagger$ は $X$ の共役演算子を表す。）

(ii) 任意の状態 $|\psi\rangle$ に対し，$\Delta P \equiv P - \langle\psi|P|\psi\rangle$，$\Delta Q \equiv Q - \langle\psi|Q|\psi\rangle$ と置くとき，$[\Delta P, \Delta Q] = iR$ を示せ。

(iii) 任意の状態 $|\psi\rangle$ に対し，不確定性関係

$$
\langle\psi|(\Delta P)^2|\psi\rangle\langle\psi|(\Delta Q)^2|\psi\rangle \ge \frac{1}{4}\langle\psi|R|\psi\rangle^2 \tag{1}
$$

が成り立つことを示せ。（ヒント：実数 $x$ に対して $(\Delta P + ix\Delta Q)|\psi\rangle$ という状態を考えてみよ。）

次に，スピン $1/2$ の1粒子状態を考える。この場合のスピンの自由度は2次元のベクトル空間で表される。$z$ 軸方向のスピン固有状態を $|\uparrow\rangle, |\downarrow\rangle$ で表すと，それらは

$$
s_z|\uparrow\rangle = +\frac{\hbar}{2}|\uparrow\rangle, \quad s_z|\downarrow\rangle = -\frac{\hbar}{2}|\downarrow\rangle, \quad \langle\uparrow|\uparrow\rangle = \langle\downarrow|\downarrow\rangle = 1, \quad \langle\uparrow|\downarrow\rangle = \langle\downarrow|\uparrow\rangle = 0
$$

を満たす。このとき，$|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$，$|\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ とベクトル表示すると，スピン角運動量演算子はパウリ行列を用いて

$$
\boldsymbol{s} = (s_x, s_y, s_z) = \frac{\hbar}{2}\boldsymbol{\sigma}, \quad \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

と表される。以下の設問に答えよ。

(2) 一般に，$\boldsymbol{n}$ 方向（$\boldsymbol{n}$ は3次元空間での単位ベクトル）のスピン角運動量を表す演算子は $s(\boldsymbol{n}) = \boldsymbol{n}\cdot\boldsymbol{s}$ と与えられる。$\boldsymbol{n} = (\sin\theta, 0, \cos\theta)$ 方向のスピン $s(\boldsymbol{n})$ に対する固有値と固有状態を求め，$\xi|\uparrow\rangle + \eta|\downarrow\rangle = \begin{pmatrix} \xi \\ \eta \end{pmatrix}$ の形で表せ。

(3) 設問2で求めた固有状態それぞれに対し，$z$ 方向のスピン角運動量の期待値を求めよ。

(4) 状態 $|\psi\rangle = \dfrac{1}{2}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}$ に対し，非可換な $P, Q$ の例を一つ挙げて，設問1 (iii) の式 (1) が成り立っていることを確認せよ。

次に，スピン $1/2$ の粒子 $\mathrm{A}, \mathrm{B}$ からなる2粒子状態を考える。粒子 $\mathrm{A}$ の $\boldsymbol{a}$ 方向のスピン角運動量を表す演算子を $s_{\mathrm{A}}(\boldsymbol{a})$ とし，$z$ 軸方向のスピン角運動量の固有状態を $|\uparrow\rangle_{\mathrm{A}}, |\downarrow\rangle_{\mathrm{A}}$ で表すとする。すなわち $\boldsymbol{e}_z = (0, 0, 1)$ に対して

$$
s_{\mathrm{A}}(\boldsymbol{e}_z)|\uparrow\rangle_{\mathrm{A}} = \frac{\hbar}{2}|\uparrow\rangle_{\mathrm{A}}, \quad s_{\mathrm{A}}(\boldsymbol{e}_z)|\downarrow\rangle_{\mathrm{A}} = -\frac{\hbar}{2}|\downarrow\rangle_{\mathrm{A}}
$$

である。同様に粒子 $\mathrm{B}$ の $\boldsymbol{b}$ 方向のスピン角運動量を表す演算子を $s_{\mathrm{B}}(\boldsymbol{b})$ とし，$z$ 軸方向のスピン角運動量の固有状態を $|\uparrow\rangle_{\mathrm{B}}, |\downarrow\rangle_{\mathrm{B}}$ で表すとする。2粒子状態を表す基底として，これらの2つの1粒子状態の直積

$$
|u, v\rangle \equiv |u\rangle_{\mathrm{A}} \otimes |v\rangle_{\mathrm{B}}, \qquad u, v = \uparrow \text{ または } \downarrow
$$

を用いる。以下の設問に答えよ。ただし以下では，2粒子状態に作用する演算子として $s_{\mathrm{A}}(\boldsymbol{a}) \otimes I_{\mathrm{B}}$，$I_{\mathrm{A}} \otimes s_{\mathrm{B}}(\boldsymbol{b})$ をそれぞれ単に $s_{\mathrm{A}}(\boldsymbol{a})$，$s_{\mathrm{B}}(\boldsymbol{b})$ と書くことにする。ここで，$I_{\mathrm{A}}, I_{\mathrm{B}}$ はそれぞれ粒子 $\mathrm{A}$，粒子 $\mathrm{B}$ の1粒子状態に作用する恒等演算子である。

(5) $\boldsymbol{a} = (\sin\theta_{\boldsymbol{a}}, 0, \cos\theta_{\boldsymbol{a}})$，$\boldsymbol{b} = (\sin\theta_{\boldsymbol{b}}, 0, \cos\theta_{\boldsymbol{b}})$ としたとき，$s_{\mathrm{A}}(\boldsymbol{a}) + s_{\mathrm{B}}(\boldsymbol{b})$ の期待値を最大にする状態を $|\uparrow, \uparrow\rangle, |\uparrow, \downarrow\rangle, |\downarrow, \uparrow\rangle, |\downarrow, \downarrow\rangle$ の線形結合で表せ。

(6) 状態 $|\psi\rangle$ に対して観測される2つのスピンの相関は $\langle\psi|s_{\mathrm{A}}(\boldsymbol{a})s_{\mathrm{B}}(\boldsymbol{b})|\psi\rangle$ で与えられる。

$$
|\psi\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow, \downarrow\rangle - |\downarrow, \uparrow\rangle\bigr)
$$

という重ね合わせの状態に対して $\boldsymbol{a} = (\sin\theta_{\boldsymbol{a}}, 0, \cos\theta_{\boldsymbol{a}})$，$\boldsymbol{b} = (\sin\theta_{\boldsymbol{b}}, 0, \cos\theta_{\boldsymbol{b}})$ としたときの相関 $\langle\psi|s_{\mathrm{A}}(\boldsymbol{a})s_{\mathrm{B}}(\boldsymbol{b})|\psi\rangle$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成21年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
状態のノルムは必ず $0$ 以上です。この性質を実数 $x$ を含む状態 $(\Delta P + ix\Delta Q)|\psi\rangle$ に用いると，$x$ の2次式が常に $0$ 以上になる条件が得られ，判別式から交換関係で定まる不確定性関係を導くことができます。

スピン $1/2$ の演算子は2行2列のパウリ行列で表されるため，任意方向の固有状態は2次方程式から直接求めることができます。2粒子系でも，粒子 $\mathrm{A}$ と粒子 $\mathrm{B}$ の演算子は別々の空間に作用して互いに可換なため，各1粒子状態の直積として整理することができます。
</div>

### (1)

(i) 交換関係 $[P, Q] = PQ - QP = iR$ の両辺のエルミート共役をとります。$(XY)^\dagger = Y^\dagger X^\dagger$ と $P^\dagger = P$，$Q^\dagger = Q$ を用います。

$$
\begin{aligned}
(iR)^\dagger &= (PQ - QP)^\dagger \\
-iR^\dagger &= Q^\dagger P^\dagger - P^\dagger Q^\dagger \\
-iR^\dagger &= QP - PQ \\
-iR^\dagger &= -[P, Q] \\
-iR^\dagger &= -iR
\end{aligned}
$$

両辺を $-i$ で割ると，$R^\dagger = R$ が得られます。したがって，演算子 $R$ は自己共役です。

(ii) $\bar{P} = \langle\psi|P|\psi\rangle$，$\bar{Q} = \langle\psi|Q|\psi\rangle$ とおきます。$\bar{P}$ と $\bar{Q}$ は複素数であり，任意の演算子と可換です。よって，交換関係を次のように展開します。

$$
\begin{aligned}
[\Delta P, \Delta Q] &= [P - \bar{P}, Q - \bar{Q}] \\
&= [P, Q] - [P, \bar{Q}] - [\bar{P}, Q] + [\bar{P}, \bar{Q}] \\
&= [P, Q] - 0 - 0 + 0 \\
&= iR
\end{aligned}
$$

(iii) $P, Q$ は自己共役なので，$\bar{P}, \bar{Q}$ は実数であり，$(\Delta P)^\dagger = \Delta P$，$(\Delta Q)^\dagger = \Delta Q$ です。任意の実数 $x$ に対して状態 $|\phi\rangle = (\Delta P + ix\Delta Q)|\psi\rangle$ を考え，そのノルムの2乗を計算します。

$$
\begin{aligned}
\langle\phi|\phi\rangle &= \langle\psi|(\Delta P + ix\Delta Q)^\dagger(\Delta P + ix\Delta Q)|\psi\rangle \\
&= \langle\psi|(\Delta P - ix\Delta Q)(\Delta P + ix\Delta Q)|\psi\rangle \\
&= \langle\psi|\bigl((\Delta P)^2 + ix(\Delta P\Delta Q - \Delta Q\Delta P) + x^2(\Delta Q)^2\bigr)|\psi\rangle \\
&= \langle\psi|(\Delta P)^2|\psi\rangle + ix\langle\psi|[\Delta P, \Delta Q]|\psi\rangle + x^2\langle\psi|(\Delta Q)^2|\psi\rangle
\end{aligned}
$$

ここで (ii) の $[\Delta P, \Delta Q] = iR$ を代入します。

$$
\begin{aligned}
\langle\phi|\phi\rangle &= \langle\psi|(\Delta Q)^2|\psi\rangle x^2 - \langle\psi|R|\psi\rangle x + \langle\psi|(\Delta P)^2|\psi\rangle
\end{aligned}
$$

任意の $|\phi\rangle$ に対して $\langle\phi|\phi\rangle \ge 0$ です。$A = \langle\psi|(\Delta Q)^2|\psi\rangle \ge 0$，$B = \langle\psi|R|\psi\rangle$，$C = \langle\psi|(\Delta P)^2|\psi\rangle \ge 0$ とおきます。$R$ は自己共役なので $B$ は実数です。

$A = 0$ のとき，任意の実数 $x$ に対して $-Bx + C \ge 0$ が成り立つためには $B = 0$ である必要があり，$AC = 0 = \dfrac{1}{4}B^2$ となって式 (1) が成り立ちます。$A > 0$ のときは，$x$ の2次関数 $Ax^2 - Bx + C$ がすべての実数 $x$ で $0$ 以上になる条件から，判別式が $0$ 以下となります。

$$
\begin{aligned}
B^2 - 4AC &\le 0 \\
AC &\ge \frac{1}{4}B^2
\end{aligned}
$$

$A, B, C$ を元に戻すと，次式が成り立ちます。

$$
\langle\psi|(\Delta P)^2|\psi\rangle\langle\psi|(\Delta Q)^2|\psi\rangle \ge \frac{1}{4}\langle\psi|R|\psi\rangle^2
$$

### (2)

$\boldsymbol{n} = (\sin\theta, 0, \cos\theta)$ 方向のスピン角運動量演算子 $s(\boldsymbol{n}) = \boldsymbol{n}\cdot\boldsymbol{s}$ を行列で書きます。

$$
\begin{aligned}
s(\boldsymbol{n}) &= \sin\theta\,s_x + \cos\theta\,s_z \\
&= \frac{\hbar}{2}\bigl(\sin\theta\,\sigma_x + \cos\theta\,\sigma_z\bigr) \\
&= \frac{\hbar}{2}\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}
\end{aligned}
$$

固有値を $\lambda$ として固有方程式を解きます。

$$
\begin{aligned}
\det\bigl(s(\boldsymbol{n}) - \lambda I\bigr) &= 0 \\
\left(\frac{\hbar}{2}\cos\theta - \lambda\right)\left(-\frac{\hbar}{2}\cos\theta - \lambda\right) - \frac{\hbar^2}{4}\sin^2\theta &= 0 \\
\lambda^2 - \frac{\hbar^2}{4}(\cos^2\theta + \sin^2\theta) &= 0 \\
\lambda^2 &= \frac{\hbar^2}{4}
\end{aligned}
$$

よって固有値は $\lambda = \pm\dfrac{\hbar}{2}$ です。次に各固有値に対する規格化された固有状態 $\begin{pmatrix} \xi \\ \eta \end{pmatrix}$ を求めます。

まず $\lambda = +\dfrac{\hbar}{2}$ のとき，固有値方程式の1行目は次式になります。

$$
\begin{aligned}
(\cos\theta - 1)\xi + \sin\theta\,\eta &= 0 \\
-2\sin^2\frac{\theta}{2}\,\xi + 2\sin\frac{\theta}{2}\cos\frac{\theta}{2}\,\eta &= 0
\end{aligned}
$$

これより $\xi : \eta = \cos\dfrac{\theta}{2} : \sin\dfrac{\theta}{2}$ です。$|\xi|^2 + |\eta|^2 = 1$ を満たすように規格化すると，任意の全体位相 $e^{i\alpha}$（$\alpha$ は実数）を除いて $\begin{pmatrix} \cos\dfrac{\theta}{2} \\ \sin\dfrac{\theta}{2} \end{pmatrix}$ となります。この表示は $\sin\dfrac{\theta}{2} = 0$ や $\cos\dfrac{\theta}{2} = 0$ の場合にも固有値方程式を満たします。

次に $\lambda = -\dfrac{\hbar}{2}$ のとき，固有値方程式の1行目は次式になります。

$$
\begin{aligned}
(\cos\theta + 1)\xi + \sin\theta\,\eta &= 0 \\
2\cos^2\frac{\theta}{2}\,\xi + 2\sin\frac{\theta}{2}\cos\frac{\theta}{2}\,\eta &= 0
\end{aligned}
$$

これより $\xi : \eta = -\sin\dfrac{\theta}{2} : \cos\dfrac{\theta}{2}$ です。規格化すると，全体位相を除いて $\begin{pmatrix} -\sin\dfrac{\theta}{2} \\ \cos\dfrac{\theta}{2} \end{pmatrix}$ となります。これも $\sin\dfrac{\theta}{2} = 0$ や $\cos\dfrac{\theta}{2} = 0$ の場合に成り立ちます。

したがって，固有値と対応する固有状態は全体位相を除いて次のようになります。

$$
\finalanswer{
\begin{aligned}
\lambda = +\frac{\hbar}{2} &: \quad \cos\frac{\theta}{2}|\uparrow\rangle + \sin\frac{\theta}{2}|\downarrow\rangle = \begin{pmatrix} \cos\dfrac{\theta}{2} \\[6pt] \sin\dfrac{\theta}{2} \end{pmatrix} \\
\lambda = -\frac{\hbar}{2} &: \quad -\sin\frac{\theta}{2}|\uparrow\rangle + \cos\frac{\theta}{2}|\downarrow\rangle = \begin{pmatrix} -\sin\dfrac{\theta}{2} \\[6pt] \cos\dfrac{\theta}{2} \end{pmatrix}
\end{aligned}
}
$$

### (3)

固有値 $+\dfrac{\hbar}{2}$ の固有状態を $|+\rangle_{\boldsymbol{n}}$，固有値 $-\dfrac{\hbar}{2}$ の固有状態を $|-\rangle_{\boldsymbol{n}}$ とおきます。それぞれの状態で $s_z = \dfrac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ の期待値を計算します。

まず $|+\rangle_{\boldsymbol{n}}$ については次のようになります。

$$
\begin{aligned}
{}_{\boldsymbol{n}}\langle +|s_z|+\rangle_{\boldsymbol{n}} &= \begin{pmatrix} \cos\dfrac{\theta}{2} & \sin\dfrac{\theta}{2} \end{pmatrix} \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \cos\dfrac{\theta}{2} \\[6pt] \sin\dfrac{\theta}{2} \end{pmatrix} \\
&= \frac{\hbar}{2}\left(\cos^2\frac{\theta}{2} - \sin^2\frac{\theta}{2}\right) \\
&= \frac{\hbar}{2}\cos\theta
\end{aligned}
$$

次に $|-\rangle_{\boldsymbol{n}}$ については次のようになります。

$$
\begin{aligned}
{}_{\boldsymbol{n}}\langle -|s_z|-\rangle_{\boldsymbol{n}} &= \begin{pmatrix} -\sin\dfrac{\theta}{2} & \cos\dfrac{\theta}{2} \end{pmatrix} \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} -\sin\dfrac{\theta}{2} \\[6pt] \cos\dfrac{\theta}{2} \end{pmatrix} \\
&= \frac{\hbar}{2}\left(\sin^2\frac{\theta}{2} - \cos^2\frac{\theta}{2}\right) \\
&= -\frac{\hbar}{2}\cos\theta
\end{aligned}
$$

したがって，固有値 $+\dfrac{\hbar}{2}$ の固有状態に対する期待値は $+\dfrac{\hbar}{2}\cos\theta$，固有値 $-\dfrac{\hbar}{2}$ の固有状態に対する期待値は $-\dfrac{\hbar}{2}\cos\theta$ です。

$$
\finalanswer{{}_{\boldsymbol{n}}\langle +|s_z|+\rangle_{\boldsymbol{n}} = \frac{\hbar}{2}\cos\theta, \qquad {}_{\boldsymbol{n}}\langle -|s_z|-\rangle_{\boldsymbol{n}} = -\frac{\hbar}{2}\cos\theta}
$$

### (4)

非可換な自己共役演算子の例として $P = s_x$，$Q = s_y$ を選びます。交換関係 $[s_x, s_y] = i\hbar s_z$ より，$R = \hbar s_z$ です。

状態 $|\psi\rangle = \dfrac{1}{2}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}$ は $\langle\psi|\psi\rangle = \dfrac{3 + 1}{4} = 1$ と規格化されています。各スピン成分の期待値を計算します。

$$
\begin{aligned}
\langle\psi|s_x|\psi\rangle &= \frac{1}{4}\begin{pmatrix} \sqrt{3} & 1 \end{pmatrix}\frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix} \\
&= \frac{\hbar}{8}\begin{pmatrix} \sqrt{3} & 1 \end{pmatrix}\begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix} \\
&= \frac{\sqrt{3}}{4}\hbar
\end{aligned}
$$

$$
\begin{aligned}
\langle\psi|s_y|\psi\rangle &= \frac{1}{4}\begin{pmatrix} \sqrt{3} & 1 \end{pmatrix}\frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix} \\
&= \frac{\hbar}{8}\begin{pmatrix} \sqrt{3} & 1 \end{pmatrix}\begin{pmatrix} -i \\ i\sqrt{3} \end{pmatrix} \\
&= 0
\end{aligned}
$$

$$
\begin{aligned}
\langle\psi|s_z|\psi\rangle &= \frac{1}{4}\begin{pmatrix} \sqrt{3} & 1 \end{pmatrix}\frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix} \\
&= \frac{\hbar}{8}(3 - 1) \\
&= \frac{\hbar}{4}
\end{aligned}
$$

パウリ行列の性質 $\sigma_x^2 = \sigma_y^2 = I$ より，$s_x^2 = s_y^2 = \dfrac{\hbar^2}{4}I$ です。よって，ゆらぎの2乗平均は次式になります。

$$
\begin{aligned}
\langle\psi|(\Delta s_x)^2|\psi\rangle &= \langle\psi|s_x^2|\psi\rangle - \langle\psi|s_x|\psi\rangle^2 \\
&= \frac{\hbar^2}{4} - \frac{3\hbar^2}{16} \\
&= \frac{\hbar^2}{16}
\end{aligned}
$$

$$
\begin{aligned}
\langle\psi|(\Delta s_y)^2|\psi\rangle &= \langle\psi|s_y^2|\psi\rangle - \langle\psi|s_y|\psi\rangle^2 \\
&= \frac{\hbar^2}{4} - 0 \\
&= \frac{\hbar^2}{4}
\end{aligned}
$$

これらから式 (1) の左辺と右辺を求めます。

$$
\begin{aligned}
\langle\psi|(\Delta P)^2|\psi\rangle\langle\psi|(\Delta Q)^2|\psi\rangle &= \frac{\hbar^2}{16}\cdot\frac{\hbar^2}{4} \\
&= \frac{\hbar^4}{64}
\end{aligned}
$$

$$
\begin{aligned}
\frac{1}{4}\langle\psi|R|\psi\rangle^2 &= \frac{1}{4}\bigl(\hbar\langle\psi|s_z|\psi\rangle\bigr)^2 \\
&= \frac{1}{4}\left(\frac{\hbar^2}{4}\right)^2 \\
&= \frac{\hbar^4}{64}
\end{aligned}
$$

左辺と右辺はいずれも $\dfrac{\hbar^4}{64}$ であり，式 (1) が等号付きで成り立っていることを確認することができます。

### (5)

$s_{\mathrm{A}}(\boldsymbol{a})$ は粒子 $\mathrm{A}$ のみに作用し，$s_{\mathrm{B}}(\boldsymbol{b})$ は粒子 $\mathrm{B}$ のみに作用します。設問2より，$s_{\mathrm{A}}(\boldsymbol{a})$ と $s_{\mathrm{B}}(\boldsymbol{b})$ の最大固有値はいずれも $+\dfrac{\hbar}{2}$ です。よって，任意の状態 $|\Phi\rangle$ に対して次の不等式が成り立ちます。

$$
\begin{aligned}
\langle\Phi|\bigl(s_{\mathrm{A}}(\boldsymbol{a}) + s_{\mathrm{B}}(\boldsymbol{b})\bigr)|\Phi\rangle &= \langle\Phi|s_{\mathrm{A}}(\boldsymbol{a})|\Phi\rangle + \langle\Phi|s_{\mathrm{B}}(\boldsymbol{b})|\Phi\rangle \\
&\le \frac{\hbar}{2} + \frac{\hbar}{2} \\
&= \hbar
\end{aligned}
$$

等号が成り立ち期待値が最大値 $\hbar$ をとるのは，$|\Phi\rangle$ が $s_{\mathrm{A}}(\boldsymbol{a})$ の固有値 $+\dfrac{\hbar}{2}$ の固有状態であり，かつ $s_{\mathrm{B}}(\boldsymbol{b})$ の固有値 $+\dfrac{\hbar}{2}$ の固有状態であるときに限られます。すなわち，設問2で求めた各粒子の固有状態の直積です。

$$
\begin{aligned}
|\Phi\rangle &= |+\rangle_{\mathrm{A}, \boldsymbol{a}} \otimes |+\rangle_{\mathrm{B}, \boldsymbol{b}} \\
&= \left(\cos\frac{\theta_{\boldsymbol{a}}}{2}|\uparrow\rangle_{\mathrm{A}} + \sin\frac{\theta_{\boldsymbol{a}}}{2}|\downarrow\rangle_{\mathrm{A}}\right) \otimes \left(\cos\frac{\theta_{\boldsymbol{b}}}{2}|\uparrow\rangle_{\mathrm{B}} + \sin\frac{\theta_{\boldsymbol{b}}}{2}|\downarrow\rangle_{\mathrm{B}}\right) \\
&= \cos\frac{\theta_{\boldsymbol{a}}}{2}\cos\frac{\theta_{\boldsymbol{b}}}{2}|\uparrow, \uparrow\rangle + \cos\frac{\theta_{\boldsymbol{a}}}{2}\sin\frac{\theta_{\boldsymbol{b}}}{2}|\uparrow, \downarrow\rangle \\
&\quad + \sin\frac{\theta_{\boldsymbol{a}}}{2}\cos\frac{\theta_{\boldsymbol{b}}}{2}|\downarrow, \uparrow\rangle + \sin\frac{\theta_{\boldsymbol{a}}}{2}\sin\frac{\theta_{\boldsymbol{b}}}{2}|\downarrow, \downarrow\rangle
\end{aligned}
$$

したがって，期待値を最大にする状態は全体位相を除いて次式となります。

$$
\finalanswer{\cos\frac{\theta_{\boldsymbol{a}}}{2}\cos\frac{\theta_{\boldsymbol{b}}}{2}|\uparrow, \uparrow\rangle + \cos\frac{\theta_{\boldsymbol{a}}}{2}\sin\frac{\theta_{\boldsymbol{b}}}{2}|\uparrow, \downarrow\rangle + \sin\frac{\theta_{\boldsymbol{a}}}{2}\cos\frac{\theta_{\boldsymbol{b}}}{2}|\downarrow, \uparrow\rangle + \sin\frac{\theta_{\boldsymbol{a}}}{2}\sin\frac{\theta_{\boldsymbol{b}}}{2}|\downarrow, \downarrow\rangle}
$$

### (6)

$s_{\mathrm{A}}(\boldsymbol{a}) = \sin\theta_{\boldsymbol{a}}\,s_{\mathrm{A}x} + \cos\theta_{\boldsymbol{a}}\,s_{\mathrm{A}z}$ と $s_{\mathrm{B}}(\boldsymbol{b}) = \sin\theta_{\boldsymbol{b}}\,s_{\mathrm{B}x} + \cos\theta_{\boldsymbol{b}}\,s_{\mathrm{B}z}$ の積を成分ごとに展開します。

$$
\begin{aligned}
s_{\mathrm{A}}(\boldsymbol{a})s_{\mathrm{B}}(\boldsymbol{b}) &= \sin\theta_{\boldsymbol{a}}\sin\theta_{\boldsymbol{b}}\,s_{\mathrm{A}x}s_{\mathrm{B}x} + \sin\theta_{\boldsymbol{a}}\cos\theta_{\boldsymbol{b}}\,s_{\mathrm{A}x}s_{\mathrm{B}z} \\
&\quad + \cos\theta_{\boldsymbol{a}}\sin\theta_{\boldsymbol{b}}\,s_{\mathrm{A}z}s_{\mathrm{B}x} + \cos\theta_{\boldsymbol{a}}\cos\theta_{\boldsymbol{b}}\,s_{\mathrm{A}z}s_{\mathrm{B}z}
\end{aligned}
$$

状態 $|\psi\rangle = \dfrac{1}{\sqrt{2}}(|\uparrow, \downarrow\rangle - |\downarrow, \uparrow\rangle)$ に各演算子積を作用させます。$s_x|\uparrow\rangle = \dfrac{\hbar}{2}|\downarrow\rangle$，$s_x|\downarrow\rangle = \dfrac{\hbar}{2}|\uparrow\rangle$，$s_z|\uparrow\rangle = +\dfrac{\hbar}{2}|\uparrow\rangle$，$s_z|\downarrow\rangle = -\dfrac{\hbar}{2}|\downarrow\rangle$ を用います。

$$
\begin{aligned}
s_{\mathrm{A}x}s_{\mathrm{B}x}|\psi\rangle &= \frac{1}{\sqrt{2}}\frac{\hbar^2}{4}\bigl(|\downarrow, \uparrow\rangle - |\uparrow, \downarrow\rangle\bigr) = -\frac{\hbar^2}{4}|\psi\rangle \\
s_{\mathrm{A}z}s_{\mathrm{B}z}|\psi\rangle &= \frac{1}{\sqrt{2}}\frac{\hbar^2}{4}\bigl(-|\uparrow, \downarrow\rangle + |\downarrow, \uparrow\rangle\bigr) = -\frac{\hbar^2}{4}|\psi\rangle \\
s_{\mathrm{A}x}s_{\mathrm{B}z}|\psi\rangle &= \frac{1}{\sqrt{2}}\frac{\hbar^2}{4}\bigl(-|\downarrow, \downarrow\rangle - |\uparrow, \uparrow\rangle\bigr) \\
s_{\mathrm{A}z}s_{\mathrm{B}x}|\psi\rangle &= \frac{1}{\sqrt{2}}\frac{\hbar^2}{4}\bigl(|\uparrow, \uparrow\rangle + |\downarrow, \downarrow\rangle\bigr)
\end{aligned}
$$

$|\uparrow, \uparrow\rangle$ と $|\downarrow, \downarrow\rangle$ は $|\psi\rangle$ に直交するため，$\langle\psi|s_{\mathrm{A}x}s_{\mathrm{B}z}|\psi\rangle = 0$，$\langle\psi|s_{\mathrm{A}z}s_{\mathrm{B}x}|\psi\rangle = 0$ です。以上をまとめると，相関は次のように計算することができます。

$$
\begin{aligned}
\langle\psi|s_{\mathrm{A}}(\boldsymbol{a})s_{\mathrm{B}}(\boldsymbol{b})|\psi\rangle &= \sin\theta_{\boldsymbol{a}}\sin\theta_{\boldsymbol{b}}\left(-\frac{\hbar^2}{4}\right) + \cos\theta_{\boldsymbol{a}}\cos\theta_{\boldsymbol{b}}\left(-\frac{\hbar^2}{4}\right) \\
&= -\frac{\hbar^2}{4}\bigl(\cos\theta_{\boldsymbol{a}}\cos\theta_{\boldsymbol{b}} + \sin\theta_{\boldsymbol{a}}\sin\theta_{\boldsymbol{b}}\bigr) \\
&= -\frac{\hbar^2}{4}\cos(\theta_{\boldsymbol{a}} - \theta_{\boldsymbol{b}})
\end{aligned}
$$

したがって，求める相関は次式となります。

$$
\finalanswer{\langle\psi|s_{\mathrm{A}}(\boldsymbol{a})s_{\mathrm{B}}(\boldsymbol{b})|\psi\rangle = -\frac{\hbar^2}{4}\cos(\theta_{\boldsymbol{a}} - \theta_{\boldsymbol{b}})}
$$
