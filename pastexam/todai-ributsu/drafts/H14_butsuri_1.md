---
title: 東大理物 平成14年度 物理学 第1問：1次元調和振動子とコヒーレント状態の不確定性関係
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成14年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成14年度 物理学 第1問：1次元調和振動子とコヒーレント状態の不確定性関係

## 問題

ハミルトニアン

$$
H = \frac{1}{2m}\hat{p}^2 + \frac{m\omega^2}{2}\hat{x}^2 \tag{1}
$$

で記述される1次元調和振動子を考えよう。ここで $\hat{p}$ は運動量演算子，$\hat{x}$ は位置演算子。この系は演算子

$$
a = \sqrt{\frac{m\omega}{2\hbar}}\hat{x} + \frac{i}{\sqrt{2m\hbar\omega}}\hat{p} \tag{2}
$$

$$
a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\hat{x} - \frac{i}{\sqrt{2m\hbar\omega}}\hat{p} \tag{3}
$$

を用いて調べることが出来る。以下の問に，解答に至る筋道を添えて答えよ。
{: .problem-lead }

(1) (1) 式のハミルトニアンを $a, a^\dagger$ を用いて表せ。また，$a, a^\dagger$ の物理的意味を述べよ。

(2) 基底状態 $|0\rangle$ は関係 $a|0\rangle = 0$ を満たす。これを用いて座標表示の基底状態波動関数 $\psi_0(x) = \langle x|0\rangle$ を求めよ。また，第一励起状態の波動関数 $\psi_1(x)$ を求めよ。ここでは規格化は考えなくてよい。

(3) 基底状態 $|0\rangle$ に演算子 $a^\dagger$ の指数関数をほどこして得られる状態

$$
|\alpha\rangle = \exp(\alpha a^\dagger)|0\rangle, \qquad \alpha\text{ は任意の複素数} \tag{4}
$$

はコヒーレント状態と呼ばれる。

(a) コヒーレント状態が演算子 $a$ の固有状態になっていることを示せ。

(b) コヒーレント状態の間の内積 $\langle\beta^*|\alpha\rangle$ を計算せよ。ただし $\langle\beta^*| = \langle 0|\exp(\beta^* a)$ である。

(c) コヒーレント状態が $n$ 番目の励起状態を含む確率を求めよ。

(d) コヒーレント状態について不確定性関係を調べよう。座標の期待値 $\langle\hat{x}\rangle \equiv \langle\alpha^*|\hat{x}|\alpha\rangle / \langle\alpha^*|\alpha\rangle$ と座標の二乗の期待値 $\langle\hat{x}^2\rangle \equiv \langle\alpha^*|\hat{x}^2|\alpha\rangle / \langle\alpha^*|\alpha\rangle$ を計算し，座標の不確定さの二乗

$$
(\Delta x)^2 = \bigl\langle (\hat{x} - \langle\hat{x}\rangle)^2 \bigr\rangle \tag{5}
$$

を求めよ。

(e) 同様に運動量の不確定さの二乗 $(\Delta p)^2 = \bigl\langle (\hat{p} - \langle\hat{p}\rangle)^2 \bigr\rangle$ を計算し，不確定関係を確かめよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成14年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，正準交換関係 $[\hat{x}, \hat{p}] = i\hbar$ から $a, a^\dagger$ の交換関係とハミルトニアンの表式を導き，$a|0\rangle = 0$ を座標表示の1階微分方程式として解くことで基底状態と第1励起状態の波動関数を求めます。

後半では，コヒーレント状態 $|\alpha\rangle = e^{\alpha a^\dagger}|0\rangle$ をべき級数に展開して $a$ の固有値方程式，異なるコヒーレント状態同士の内積，およびエネルギー固有状態の確率分布を導きます。さらに $\hat{x}, \hat{p}$ を $a, a^\dagger$ で書き換えて期待値と揺らぎを計算し，不確定性積を求めます。
</div>

### (1)

正準交換関係 $[\hat{x}, \hat{p}] = i\hbar$ を用いて，$a^\dagger a$ と $a a^\dagger$ を展開します。

$$
\begin{aligned}
a^\dagger a &= \left(\sqrt{\frac{m\omega}{2\hbar}}\hat{x} - \frac{i}{\sqrt{2m\hbar\omega}}\hat{p}\right)\left(\sqrt{\frac{m\omega}{2\hbar}}\hat{x} + \frac{i}{\sqrt{2m\hbar\omega}}\hat{p}\right) \\
&= \frac{m\omega}{2\hbar}\hat{x}^2 + \frac{1}{2m\hbar\omega}\hat{p}^2 + \frac{i}{2\hbar}(\hat{x}\hat{p} - \hat{p}\hat{x}) \\
&= \frac{1}{\hbar\omega}\left(\frac{1}{2m}\hat{p}^2 + \frac{m\omega^2}{2}\hat{x}^2\right) - \frac{1}{2} \\
&= \frac{H}{\hbar\omega} - \frac{1}{2}
\end{aligned}
$$

したがって，ハミルトニアン $H$ は次式となります。

$$
\finalanswer{H = \hbar\omega\left(a^\dagger a + \frac{1}{2}\right)}
$$

同様に計算すると交換関係 $[a, a^\dagger] = 1$ が成り立つため，$[H, a] = -\hbar\omega a$，$[H, a^\dagger] = +\hbar\omega a^\dagger$ となります。エネルギー固有値 $E$ をもつ固有状態 $|E\rangle$ に $a$ や $a^\dagger$ を作用させると，$H(a|E\rangle) = (E - \hbar\omega)(a|E\rangle)$，$H(a^\dagger|E\rangle) = (E + \hbar\omega)(a^\dagger|E\rangle)$ となります。すなわち，$a$ は調和振動子のエネルギー量子を1個減らしてエネルギーを $\hbar\omega$ だけ下げる**消滅演算子**，$a^\dagger$ はエネルギー量子を1個増やしてエネルギーを $\hbar\omega$ だけ上げる**生成演算子**です。

### (2)

座標表示では $\hat{x} \to x$，$\hat{p} \to -i\hbar\dfrac{\mathrm{d}}{\mathrm{d}x}$ です。条件 $a|0\rangle = 0$ を座標表示で書きます。

$$
\left(\sqrt{\frac{m\omega}{2\hbar}}x + \sqrt{\frac{\hbar}{2m\omega}}\frac{\mathrm{d}}{\mathrm{d}x}\right)\psi_0(x) = 0
$$

両辺に $\sqrt{\dfrac{2m\omega}{\hbar}}$ を掛けて整理します。

$$
\frac{\mathrm{d}\psi_0}{\mathrm{d}x} = -\frac{m\omega}{\hbar}x\psi_0
$$

変数分離して積分すると，定数因子を除いた基底状態波動関数 $\psi_0(x)$ が得られます。

$$
\psi_0(x) = \exp\!\left(-\frac{m\omega}{2\hbar}x^2\right)
$$

第1励起状態は生成演算子 $a^\dagger$ を $\psi_0(x)$ に作用させて求めます。

$$
\begin{aligned}
a^\dagger\psi_0(x) &= \sqrt{\frac{\hbar}{2m\omega}}\left(\frac{m\omega}{\hbar}x - \frac{\mathrm{d}}{\mathrm{d}x}\right)\exp\!\left(-\frac{m\omega}{2\hbar}x^2\right) \\
&= \sqrt{\frac{\hbar}{2m\omega}}\left(\frac{m\omega}{\hbar}x + \frac{m\omega}{\hbar}x\right)\exp\!\left(-\frac{m\omega}{2\hbar}x^2\right) \\
&= \sqrt{\frac{2m\omega}{\hbar}}\,x\exp\!\left(-\frac{m\omega}{2\hbar}x^2\right)
\end{aligned}
$$

規格化定数を除くと，基底状態と第1励起状態の波動関数は次式となります。

$$
\finalanswer{\psi_0(x) = \exp\!\left(-\frac{m\omega}{2\hbar}x^2\right), \qquad \psi_1(x) = x\exp\!\left(-\frac{m\omega}{2\hbar}x^2\right)}
$$

### (3)

#### (a)

$[a, a^\dagger] = 1$ より，任意の自然数 $n$ に対して $[a, (a^\dagger)^n] = n(a^\dagger)^{n-1}$ が成り立ちます。$a|0\rangle = 0$ を用いて，$|\alpha\rangle = \sum_{n=0}^{\infty} \dfrac{\alpha^n}{n!}(a^\dagger)^n|0\rangle$ に $a$ を作用させます。

$$
\begin{aligned}
a|\alpha\rangle &= \sum_{n=0}^{\infty} \frac{\alpha^n}{n!}\,a(a^\dagger)^n|0\rangle \\
&= \sum_{n=1}^{\infty} \frac{\alpha^n}{n!}\,n(a^\dagger)^{n-1}|0\rangle \\
&= \alpha\sum_{m=0}^{\infty} \frac{\alpha^m}{m!}(a^\dagger)^m|0\rangle \\
&= \alpha|\alpha\rangle
\end{aligned}
$$

これで $|\alpha\rangle$ が演算子 $a$ の固有値 $\alpha$ に属する固有状態になっていることがわかります。

#### (b)

規格化されたエネルギー固有状態 $|n\rangle = \dfrac{1}{\sqrt{n!}}(a^\dagger)^n|0\rangle$（$\langle m|n\rangle = \delta_{mn}$）を用いて $|\alpha\rangle$ と $\langle\beta^*|$ を展開します。

$$
|\alpha\rangle = \sum_{n=0}^{\infty} \frac{\alpha^n}{\sqrt{n!}}|n\rangle, \qquad \langle\beta^*| = \sum_{m=0}^{\infty} \frac{(\beta^*)^m}{\sqrt{m!}}\langle m|
$$

両者の内積 $\langle\beta^*|\alpha\rangle$ を計算します。

$$
\begin{aligned}
\langle\beta^*|\alpha\rangle &= \sum_{m=0}^{\infty}\sum_{n=0}^{\infty} \frac{(\beta^*)^m \alpha^n}{\sqrt{m!\,n!}}\langle m|n\rangle \\
&= \sum_{n=0}^{\infty} \frac{(\beta^*\alpha)^n}{n!} \\
&= \exp(\beta^*\alpha)
\end{aligned}
$$

したがって，内積は次式となります。

$$
\finalanswer{\langle\beta^*|\alpha\rangle = \exp(\beta^*\alpha)}
$$

#### (c)

小問 (b) より，コヒーレント状態のノルムの2乗は $\langle\alpha^*|\alpha\rangle = \exp(|\alpha|^2)$ です。また，規格化された $n$ 番目の励起状態 $|n\rangle$ との内積は $\langle n|\alpha\rangle = \dfrac{\alpha^n}{\sqrt{n!}}$ です。したがって，状態 $|\alpha\rangle$ の中に $|n\rangle$ を見いだす確率 $P_n$ は次式となります。

$$
\begin{aligned}
P_n &= \frac{|\langle n|\alpha\rangle|^2}{\langle\alpha^*|\alpha\rangle} \\
&= \frac{|\alpha|^{2n}/n!}{e^{|\alpha|^2}} \\
&= e^{-|\alpha|^2}\frac{|\alpha|^{2n}}{n!}
\end{aligned}
$$

$$
\finalanswer{P_n = e^{-|\alpha|^2}\frac{|\alpha|^{2n}}{n!}}
$$

#### (d)

式 (2) と式 (3) の和をとることで，位置演算子 $\hat{x}$ を $a, a^\dagger$ で表します。

$$
\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\bigl(a + a^\dagger\bigr)
$$

小問 (a) の $a|\alpha\rangle = \alpha|\alpha\rangle$ およびそのエルミート共役 $\langle\alpha^*|a^\dagger = \alpha^*\langle\alpha^*|$ を用いて期待値 $\langle\hat{x}\rangle$ を計算します。

$$
\begin{aligned}
\langle\hat{x}\rangle &= \sqrt{\frac{\hbar}{2m\omega}}\frac{\langle\alpha^*|(a + a^\dagger)|\alpha\rangle}{\langle\alpha^*|\alpha\rangle} \\
&= \sqrt{\frac{\hbar}{2m\omega}}(\alpha + \alpha^*)
\end{aligned}
$$

次に $\hat{x}^2$ を $[a, a^\dagger] = 1$ を用いて正規順序に直します。

$$
\begin{aligned}
\hat{x}^2 &= \frac{\hbar}{2m\omega}\bigl(a^2 + a a^\dagger + a^\dagger a + (a^\dagger)^2\bigr) \\
&= \frac{\hbar}{2m\omega}\bigl(a^2 + 2a^\dagger a + (a^\dagger)^2 + 1\bigr)
\end{aligned}
$$

期待値 $\langle\hat{x}^2\rangle$ を計算します。

$$
\begin{aligned}
\langle\hat{x}^2\rangle &= \frac{\hbar}{2m\omega}\bigl(\alpha^2 + 2\alpha^*\alpha + (\alpha^*)^2 + 1\bigr) \\
&= \frac{\hbar}{2m\omega}\bigl((\alpha + \alpha^*)^2 + 1\bigr)
\end{aligned}
$$

したがって，座標の不確定さの2乗 $(\Delta x)^2 = \langle\hat{x}^2\rangle - \langle\hat{x}\rangle^2$ は次式となります。

$$
\begin{aligned}
(\Delta x)^2 &= \frac{\hbar}{2m\omega}\bigl((\alpha + \alpha^*)^2 + 1\bigr) - \frac{\hbar}{2m\omega}(\alpha + \alpha^*)^2 \\
&= \frac{\hbar}{2m\omega}
\end{aligned}
$$

$$
\finalanswer{\langle\hat{x}\rangle = \sqrt{\frac{\hbar}{2m\omega}}(\alpha + \alpha^*), \qquad \langle\hat{x}^2\rangle = \frac{\hbar}{2m\omega}\bigl((\alpha + \alpha^*)^2 + 1\bigr), \qquad (\Delta x)^2 = \frac{\hbar}{2m\omega}}
$$

#### (e)

式 (2) と式 (3) の差から，運動量演算子 $\hat{p}$ を $a, a^\dagger$ で表します。

$$
\hat{p} = -i\sqrt{\frac{m\hbar\omega}{2}}\bigl(a - a^\dagger\bigr)
$$

同様に期待値 $\langle\hat{p}\rangle$ を計算します。

$$
\begin{aligned}
\langle\hat{p}\rangle &= -i\sqrt{\frac{m\hbar\omega}{2}}\frac{\langle\alpha^*|(a - a^\dagger)|\alpha\rangle}{\langle\alpha^*|\alpha\rangle} \\
&= -i\sqrt{\frac{m\hbar\omega}{2}}(\alpha - \alpha^*)
\end{aligned}
$$

$\hat{p}^2$ を正規順序に直して期待値 $\langle\hat{p}^2\rangle$ を計算します。

$$
\begin{aligned}
\hat{p}^2 &= -\frac{m\hbar\omega}{2}\bigl(a^2 - a a^\dagger - a^\dagger a + (a^\dagger)^2\bigr) \\
&= -\frac{m\hbar\omega}{2}\bigl(a^2 - 2a^\dagger a + (a^\dagger)^2 - 1\bigr)
\end{aligned}
$$

$$
\begin{aligned}
\langle\hat{p}^2\rangle &= -\frac{m\hbar\omega}{2}\bigl(\alpha^2 - 2\alpha^*\alpha + (\alpha^*)^2 - 1\bigr) \\
&= -\frac{m\hbar\omega}{2}\bigl((\alpha - \alpha^*)^2 - 1\bigr)
\end{aligned}
$$

したがって，運動量の不確定さの2乗 $(\Delta p)^2 = \langle\hat{p}^2\rangle - \langle\hat{p}\rangle^2$ は次式となります。

$$
\begin{aligned}
(\Delta p)^2 &= -\frac{m\hbar\omega}{2}\bigl((\alpha - \alpha^*)^2 - 1\bigr) - \left(-\frac{m\hbar\omega}{2}(\alpha - \alpha^*)^2\right) \\
&= \frac{m\hbar\omega}{2}
\end{aligned}
$$

小問 (d) の結果と掛け合わせて不確定性の積を求めます。

$$
\begin{aligned}
\Delta x\,\Delta p &= \sqrt{\frac{\hbar}{2m\omega}}\cdot\sqrt{\frac{m\hbar\omega}{2}} \\
&= \frac{\hbar}{2}
\end{aligned}
$$

任意の複素数 $\alpha$ に対してハイゼンベルグの不確定性関係 $\Delta x\,\Delta p \ge \dfrac{\hbar}{2}$ の等号が成り立ちます。

$$
\finalanswer{(\Delta p)^2 = \frac{m\hbar\omega}{2}, \qquad \Delta x\,\Delta p = \frac{\hbar}{2}}
$$
