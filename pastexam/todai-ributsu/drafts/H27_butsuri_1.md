---
title: 東大理物 平成27年度 物理学 第1問：円周上のデルタ関数ポテンシャルと束縛・散乱状態
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成27年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加しています。
---

# 東大理物 平成27年度 物理学 第1問：円周上のデルタ関数ポテンシャルと束縛・散乱状態

## 問題

以下のハミルトニアンで記述される一次元量子系を考える。

$$
H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)
$$

ここで $2\pi\hbar\ (= h)$ はプランク定数，$m$ は考えている粒子の質量，$V(x)$ は時間によらないポテンシャルエネルギーである。系は長さ $2\pi L$ の一次元円周上で定義されているものとし，$x$ と $x + 2\pi L$ を同一点とみなす。波動関数 $\psi(x)$ およびポテンシャル $V(x)$ は周期的境界条件 $\psi(x + 2\pi L) = \psi(x),\ V(x + 2\pi L) = V(x)$ を満たすものとする。

(1) $V(x) = 0$ の場合にシュレディンガー方程式 $H\psi(x) = E\psi(x)$ を解け。エネルギー $E$ はどのような値に量子化されるか，またエネルギー固有値に縮退があるのかどうか述べよ。

以下ではポテンシャルがデルタ関数，つまり円周を $x \in [-\pi L, \pi L]$ とあらわした時

$$
V(x) = \frac{\hbar^2 v}{2m}\delta(x)
$$

と与えられる場合を考える。$v$ は定数である。

(2) 波動関数 $\psi(x)$ の微分 $\psi'(x) = \dfrac{d\psi}{dx}$ は $x = 0$ で次のような不連続性を持つことを，シュレディンガー方程式を用いて説明せよ。

$$
\lim_{\epsilon \to 0+}\bigl(\psi'(\epsilon) - \psi'(-\epsilon)\bigr) = v\psi(0)
$$

(3) $v < 0$ の場合，負エネルギー状態が一つだけ存在することを示す。まず，$x = 0$ を除く円周 $x \in (0, 2\pi L)$ で波動関数を $\psi(x) = e^{\kappa x} + A e^{-\kappa x}$（$A$ は定数，$\kappa > 0$）の形に仮定する。それがエネルギー固有値 $E = -\dfrac{\hbar^2\kappa^2}{2m}$ に対応するシュレディンガー方程式の解であることを確認せよ。次に $x = 0$ における接続条件を調べ，$A$ の表式，及び $v$ と $\kappa$ の関係を定めよ。最後にグラフを利用して任意の $v < 0$ に対して $\kappa$ が一つだけ定まることを示せ。

(4) $v > 0,\ E > 0$ の場合の解を調べる。$E$ を正のパラメータ $k$ を用いて $E = \dfrac{\hbar^2 k^2}{2m}$ と書く。設問3と同様の解析を行って境界条件を満たすシュレディンガー方程式の解の形を定め，$k$ と $v$ の間の関係を求めよ。なお，ポテンシャルエネルギーの影響を受けない解もあることに留意せよ。

(5) 設問4で $k \gg v$ の場合，$v = 0$ の場合と比較したときのエネルギー固有値の補正を，$v$ について一次まで求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成27年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
円周上のデルタ関数ポテンシャルは原点 $x = 0$ でのみ波動関数の1階微分に跳びを生じさせるため，$x \in (0, 2\pi L)$ の自由粒子解に対して周期性と原点での接続条件を課すだけで厳密な固有値方程式が得られます。

円周上の左右対称性（$x \leftrightarrow 2\pi L - x$）により，正エネルギー状態は原点に節をもつ奇対称解（ポテンシャルの影響を受けない）と偶対称解（$2k\tan(\pi L k) = v$ でエネルギーが押し上げられる）へ明確に分離されます。
</div>

### (1)
$V(x) = 0$ のシュレディンガー方程式は $-\dfrac{\hbar^2}{2m}\psi''(x) = E\psi(x)$ です。周期境界条件 $\psi(x + 2\pi L) = \psi(x)$ を満たす有界解は $E \ge 0$ に限られ，波数 $k_n$ を用いて $\psi(x) = C e^{i k_n x}$ とおくと $e^{i k_n \cdot 2\pi L} = 1$ より $k_n = \dfrac{n}{L}\ (n = 0, \pm 1, \pm 2, \dots)$ となります。

規格化された固有関数とエネルギー固有値は次のとおりです。

$$
\psi_n(x) = \frac{1}{\sqrt{2\pi L}} e^{i\frac{n}{L}x},\qquad E_n = \frac{\hbar^2 n^2}{2m L^2} \qquad (n = 0, \pm 1, \pm 2, \dots)
$$

$n = 0$（基底状態 $E_0 = 0$）は定数関数 $\psi_0(x) = \dfrac{1}{\sqrt{2\pi L}}$ のみで**縮退はありません**。一方，$n \neq 0$（$E_n > 0$）では $+|n|$ と $-|n|$ が同じエネルギーを与えるため，**2重に縮退しています**（$\cos(nx/L)$ と $\sin(nx/L)$ の2つの独立な解があります）。したがって，

$$
\finalanswer{\psi_n(x) = \frac{1}{\sqrt{2\pi L}} e^{i\frac{n}{L}x},\qquad E_n = \frac{\hbar^2 n^2}{2m L^2} \qquad (n = 0, \pm 1, \pm 2, \dots)}
$$

### (2)
シュレディンガー方程式を整理すると次式になります。

$$
\psi''(x) - v\delta(x)\psi(x) = -\frac{2mE}{\hbar^2}\psi(x)
$$

両辺を $x = -\epsilon$ から $x = \epsilon$（$\epsilon > 0$）まで積分します。

$$
\int_{-\epsilon}^{\epsilon} \psi''(x)\,\mathrm{d}x - v\int_{-\epsilon}^{\epsilon} \delta(x)\psi(x)\,\mathrm{d}x = -\frac{2mE}{\hbar^2}\int_{-\epsilon}^{\epsilon}\psi(x)\,\mathrm{d}x
$$

左辺第1項は $\psi'(\epsilon) - \psi'(-\epsilon)$，第2項は $-v\psi(0)$ です。波動関数 $\psi(x)$ は $x = 0$ で連続かつ有界なので，$\epsilon \to 0+$ の極限で右辺の積分は $0$ に収束します。よって次式が得られます。

$$
\lim_{\epsilon \to 0+}\bigl(\psi'(\epsilon) - \psi'(-\epsilon)\bigr) = v\psi(0)
$$

### (3)
$x \in (0, 2\pi L)$ では $\delta(x) = 0$ なので，$\psi(x) = e^{\kappa x} + A e^{-\kappa x}$ を2回微分すると $\psi''(x) = \kappa^2(e^{\kappa x} + A e^{-\kappa x}) = \kappa^2\psi(x)$ となり，

$$
H\psi(x) = -\frac{\hbar^2}{2m}\psi''(x) = -\frac{\hbar^2\kappa^2}{2m}\psi(x)
$$

となってエネルギー固有値 $E = -\dfrac{\hbar^2\kappa^2}{2m}$ の解であることが確かめられます。

次に $x = 0$ と $x = 2\pi L$ が同一点であることから，連続条件 $\psi(0+) = \psi(2\pi L-)$ を課します。

$$
1 + A = e^{2\pi L\kappa} + A e^{-2\pi L\kappa} \implies A\left(1 - e^{-2\pi L\kappa}\right) = e^{2\pi L\kappa} - 1 \implies A = e^{2\pi L\kappa}
$$

続いて問2の接続条件 $\psi'(0+) - \psi'(2\pi L-) = v\psi(0)$ を課します。$\psi'(0+) = \kappa(1 - A)$，$\psi'(2\pi L-) = \kappa(e^{2\pi L\kappa} - A e^{-2\pi L\kappa}) = \kappa(A - 1)$，$\psi(0) = 1 + A$ より，

$$
\begin{aligned}
2\kappa(1 - A) &= v(1 + A) \\
2\kappa\left(1 - e^{2\pi L\kappa}\right) &= v\left(1 + e^{2\pi L\kappa}\right) \\
-v &= 2\kappa\frac{e^{2\pi L\kappa} - 1}{e^{2\pi L\kappa} + 1} = 2\kappa\tanh(\pi L\kappa)
\end{aligned}
$$

したがって，

$$
\finalanswer{A = e^{2\pi L\kappa},\qquad -v = 2\kappa\tanh(\pi L\kappa)}
$$

**解の一意性**：関数 $y = 2\kappa\tanh(\pi L\kappa)$ は $\kappa > 0$ で連続かつ狭義単調増加であり，$\kappa \to 0+$ で $y \to 0$，$\kappa \to \infty$ で $y \to \infty$ です。したがって，任意の $v < 0$ に対する水平線 $y = -v\ (> 0)$ とちょうど1点 $\kappa = \kappa_0 > 0$ で交わり，負エネルギー状態が唯一つ定まります。

<figure class="problem-figure" markdown>
![y=2kappa tanh(pi L kappa)とy=-vの交点](../../../docs/assets/figures/pastexam-todai-ributsu/H27_butsuri_1-s-light.svg#only-light)
![y=2kappa tanh(pi L kappa)とy=-vの交点](../../../docs/assets/figures/pastexam-todai-ributsu/H27_butsuri_1-s-dark.svg#only-dark)
<figcaption markdown="span">$y = 2\kappa\tanh(\pi L\kappa)$（実線）と $y = -v > 0$（破線）のグラフ。任意の $v < 0$ に対して交点 $\kappa_0 > 0$ が唯一つ定まる。</figcaption>
</figure>

### (4)
$x \in (0, 2\pi L)$ での一般解は $\psi(x) = C_1\cos\bigl(k(x - \pi L)\bigr) + C_2\sin\bigl(k(x - \pi L)\bigr)$（あるいは $e^{ikx}$ と $e^{-ikx}$ の線形結合）です。

- **奇対称解**（$C_1 = 0$）：$\psi(x) = C_2\sin\bigl(k(x - \pi L)\bigr)$。連続条件 $\psi(0+) = \psi(2\pi L-)$ は $-C_2\sin(\pi L k) = C_2\sin(\pi L k)$ より $\sin(\pi L k) = 0$，すなわち $k = \dfrac{n}{L}\ (n = 1, 2, 3, \dots)$ です。このとき $\psi(0) = 0$ かつ $\psi'(0+) = \psi'(2\pi L-) = (-1)^n k C_2$ となるため接続条件も自動的に満たされ，ポテンシャル $v$ の影響を受けません（$\psi(x) \propto \sin(nx/L)$）。
- **偶対称解**（$C_2 = 0$）：$\psi(x) = C_1\cos\bigl(k(x - \pi L)\bigr)$。連続条件 $\psi(0+) = \psi(2\pi L-) = C_1\cos(\pi L k)$ は任意の $k$ で満たされます。接続条件 $\psi'(0+) - \psi'(2\pi L-) = v\psi(0)$ を書き下すと，$\psi'(0+) = k C_1\sin(\pi L k),\ \psi'(2\pi L-) = -k C_1\sin(\pi L k)$ より，

$$
2k\sin(\pi L k) = v\cos(\pi L k) \implies 2k\tan(\pi L k) = v
$$

（$\cos(\pi L k) = 0$ のときは左辺 $\neq 0$，右辺 $= 0$ で解になりません。）したがって，奇対称解と偶対称解はそれぞれ次のとおりです。

$$
\finalanswer{\psi_{\mathrm{odd}}(x) \propto \sin\left(\frac{n}{L}x\right),\ k = \frac{n}{L} \ (n = 1, 2, \dots);\qquad \psi_{\mathrm{even}}(x) \propto \cos\bigl(k(x - \pi L)\bigr),\ 2k\tan(\pi L k) = v}
$$

### (5)
$v = 0$ のとき $k_n^{(0)} = \dfrac{n}{L}\ (n = 1, 2, \dots)$ であった2重縮退準位に対する補正を調べます（$k \gg v$ より $n \ge 1$）。

- **奇対称解**：問4より $k = \dfrac{n}{L}$ のまま変化しないため，エネルギー固有値の補正は $\Delta E_n^{\mathrm{odd}} = 0$ です。
- **偶対称解**：$k_n = \dfrac{n}{L} + \delta k_n$（$|\pi L\delta k_n| \ll 1$）とおいて $2k_n\tan(\pi L k_n) = v$ を1次まで展開します。$\tan(\pi L k_n) = \tan(\pi L\delta k_n) \simeq \pi L\delta k_n$ より，

$$
2\frac{n}{L}(\pi L\delta k_n) \simeq v \implies \delta k_n \simeq \frac{v}{2\pi n}
$$

エネルギーの補正を $v$ の1次まで求めます。

$$
\begin{aligned}
\Delta E_n^{\mathrm{even}}
&= \frac{\hbar^2}{2m}\left[\left(\frac{n}{L} + \delta k_n\right)^2 - \left(\frac{n}{L}\right)^2\right] \\
&\simeq \frac{\hbar^2}{m}\frac{n}{L}\delta k_n = \frac{\hbar^2 v}{2\pi m L}
\end{aligned}
$$

したがって，$v$ の1次までのエネルギー固有値の補正は奇対称解で $0$，偶対称解で $\dfrac{\hbar^2 v}{2\pi m L}$ です。

$$
\finalanswer{\Delta E_n^{\mathrm{odd}} = 0,\qquad \Delta E_n^{\mathrm{even}} = \frac{\hbar^2 v}{2\pi m L}}
$$

<aside class="rigor-note" markdown>
問5の1次補正は縮退摂動論とも完全に一致します。$v = 0$ の固有基底として実の正規直交基底 $\psi_n^{\mathrm{even}}(x) = \dfrac{1}{\sqrt{\pi L}}\cos(nx/L)$ と $\psi_n^{\mathrm{odd}}(x) = \dfrac{1}{\sqrt{\pi L}}\sin(nx/L)$ を選ぶと，$V(x) = \dfrac{\hbar^2 v}{2m}\delta(x)$ はこの基底ですでに対角化されており，対角成分は $\langle V \rangle_{\mathrm{odd}} = 0$，$\langle V \rangle_{\mathrm{even}} = \dfrac{\hbar^2 v}{2m}\cdot\dfrac{1}{\pi L} = \dfrac{\hbar^2 v}{2\pi m L}$ となります。
</aside>
