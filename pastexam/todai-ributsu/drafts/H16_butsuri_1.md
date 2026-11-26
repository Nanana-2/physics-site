---
title: 東大理物 平成16年度 物理学 第1問：1次元調和振動子のハイゼンベルグ表示とコヒーレント状態
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成16年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成16年度 物理学 第1問：1次元調和振動子のハイゼンベルグ表示とコヒーレント状態

## 問題

質量 $m$，振動数 $\omega$ をもつ一次元調和振動子のハミルトニアン演算子 $\mathbf{H}$ は

$$
\mathbf{H} = \frac{\mathbf{p}^2}{2m} + \frac{m\omega^2}{2}\mathbf{x}^2
$$

で与えられる。ここで，$\mathbf{x}$ と $\mathbf{p}$ はそれぞれ位置座標演算子と運動量演算子である。この系を解析するために，ハイゼンベルグ表示を用いる。また，演算子

$$
a = \sqrt{\frac{m\omega}{2\hbar}}\left(\mathbf{x}(0) + i\frac{\mathbf{p}(0)}{m\omega}\right), \qquad a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\mathbf{x}(0) - i\frac{\mathbf{p}(0)}{m\omega}\right)
$$

を導入する。ここで，$\mathbf{x}(0)$ と $\mathbf{p}(0)$ は時刻 $t = 0$ での演算子である。以下の問いに答えよ。

(1) 演算子 $\mathbf{N} = a^\dagger a$ と $a^\dagger$ との交換関係および $\mathbf{N}$ と $a$ との交換関係を求めよ。

(2) 演算子 $\mathbf{N}$ の固有状態を $|n\rangle$ とし，その固有値を $n$ とすると，

$$
\mathbf{N}|n\rangle = n|n\rangle
$$

が成り立つ。ここで，$a^\dagger|n\rangle = C|n + 1\rangle$ および $a|n\rangle = D|n - 1\rangle$ であることを示し，係数 $C$ と $D$ を求めよ。ただし，係数 $C$ と $D$ は正の数とし，状態 $|n\rangle$ は $\langle n|n\rangle = 1$ と規格化されているとする。

(3) 上の結果を用いて $n$ がゼロ又は正の整数であることを証明せよ。

さて，ハイゼンベルグ表示では演算子 $\mathbf{x}(t)$ および演算子 $\mathbf{p}(t)$ は時刻 $t$ に依存する。それらの演算子の時間変化はハイゼンベルグ方程式で与えられる。以下の問いに答えよ。
{: .problem-lead }

(4) $\mathbf{x}(t)$ および $\mathbf{p}(t)$ についてのハイゼンベルグ方程式を書け。

(5) 上記の方程式を解いて $\mathbf{x}(t)$ と $\mathbf{p}(t)$ を求め，それらが古典解と類似の時間変動をすることを示せ。

(6) 期待値 $\langle n|\mathbf{x}(t)|n\rangle$ および $\langle n|\mathbf{p}(t)|n\rangle$ を求めよ。

(7) 期待値 $\langle\lambda|\mathbf{x}(t)|\lambda\rangle$ および $\langle\lambda|\mathbf{p}(t)|\lambda\rangle$ が調和振動子の古典解と類似の時間変動を示すような状態 $|\lambda\rangle$ は，基底状態 $|G\rangle$ に演算子 $a$ および $a^\dagger$ を作用して作ることができる。つまり，この状態 $|\lambda\rangle$ は $|\lambda\rangle = F(a, a^\dagger)|G\rangle$ と書ける。関数 $F(a, a^\dagger)$ の具体例を示せ。ただし，基底状態は $a|G\rangle = 0$ を満たすものとする。また，状態 $|\lambda\rangle$ の規格化条件は無視してよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成16年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
調和振動子の生成消滅演算子は交換関係 $[a, a^\dagger] = 1$ を満たし，個数演算子 $\mathbf{N} = a^\dagger a$ の固有値を $1$ ずつ増減させます。状態のノルムが $0$ 以上であることから固有値 $n$ は負にならず，下降操作が有限回で止まるため固有値が非負整数に制限されます。

ハイゼンベルグ表示では演算子 $\mathbf{x}(t)$ と $\mathbf{p}(t)$ が古典力学の正準方程式と同じ形の線形微分方程式に従うため，時刻 $0$ の生成消滅演算子の線形結合で時間発展をそのまま表すことができます。消滅演算子 $a$ の固有状態を作ると，位置と運動量の期待値が古典的な単振動に一致します。
</div>

### (1)

正準交換関係 $[\mathbf{x}(0), \mathbf{p}(0)] = i\hbar$ を用いて，まず $[a, a^\dagger]$ を計算します。

$$
\begin{aligned}
[a, a^\dagger] &= \frac{m\omega}{2\hbar}\left[\mathbf{x}(0) + \frac{i}{m\omega}\mathbf{p}(0),\ \mathbf{x}(0) - \frac{i}{m\omega}\mathbf{p}(0)\right] \\
&= \frac{m\omega}{2\hbar}\left(-\frac{i}{m\omega}[\mathbf{x}(0), \mathbf{p}(0)] + \frac{i}{m\omega}[\mathbf{p}(0), \mathbf{x}(0)]\right) \\
&= \frac{1}{2\hbar}\bigl(-i(i\hbar) + i(-i\hbar)\bigr) \\
&= 1
\end{aligned}
$$

積の交換関係の公式 $[XY, Z] = X[Y, Z] + [X, Z]Y$ を用いて $[\mathbf{N}, a^\dagger]$ と $[\mathbf{N}, a]$ を計算します。

$$
\begin{aligned}
[\mathbf{N}, a^\dagger] &= [a^\dagger a, a^\dagger] \\
&= a^\dagger[a, a^\dagger] + [a^\dagger, a^\dagger]a \\
&= a^\dagger\cdot 1 + 0 \\
&= a^\dagger
\end{aligned}
$$

$$
\begin{aligned}
[\mathbf{N}, a] &= [a^\dagger a, a] \\
&= a^\dagger[a, a] + [a^\dagger, a]a \\
&= 0 + (-1)a \\
&= -a
\end{aligned}
$$

したがって，求める交換関係は次式となります。

$$
\finalanswer{[\mathbf{N}, a^\dagger] = a^\dagger, \qquad [\mathbf{N}, a] = -a}
$$

### (2)

設問1の交換関係から $\mathbf{N}a^\dagger = a^\dagger\mathbf{N} + a^\dagger$ および $\mathbf{N}a = a\mathbf{N} - a$ です。これらを固有状態 $|n\rangle$ に作用させます。

$$
\begin{aligned}
\mathbf{N}\bigl(a^\dagger|n\rangle\bigr) &= (a^\dagger\mathbf{N} + a^\dagger)|n\rangle \\
&= (n + 1)\bigl(a^\dagger|n\rangle\bigr)
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{N}\bigl(a|n\rangle\bigr) &= (a\mathbf{N} - a)|n\rangle \\
&= (n - 1)\bigl(a|n\rangle\bigr)
\end{aligned}
$$

よって $a^\dagger|n\rangle$ は固有値 $n + 1$ の固有状態 $|n + 1\rangle$ の定数倍，$a|n\rangle$ は固有値 $n - 1$ の固有状態 $|n - 1\rangle$ の定数倍であり，$a^\dagger|n\rangle = C|n + 1\rangle$，$a|n\rangle = D|n - 1\rangle$ と書くことができます。

次に規格化条件 $\langle n|n\rangle = \langle n + 1|n + 1\rangle = \langle n - 1|n - 1\rangle = 1$ と $[a, a^\dagger] = 1$ を用いて $C^2$ と $D^2$ を計算します。

$$
\begin{aligned}
C^2 &= \langle n|a a^\dagger|n\rangle \\
&= \langle n|(a^\dagger a + 1)|n\rangle \\
&= \langle n|(\mathbf{N} + 1)|n\rangle \\
&= n + 1
\end{aligned}
$$

$$
\begin{aligned}
D^2 &= \langle n|a^\dagger a|n\rangle \\
&= \langle n|\mathbf{N}|n\rangle \\
&= n
\end{aligned}
$$

係数 $C$ と $D$ は正の数なので，$C = \sqrt{n + 1}$，$D = \sqrt{n}$ となります。

$$
\finalanswer{C = \sqrt{n + 1}, \qquad D = \sqrt{n}}
$$

### (3)

任意の固有状態 $|n\rangle$ に対して，状態のノルムの2乗は $0$ 以上です。

$$
\begin{aligned}
n &= \langle n|\mathbf{N}|n\rangle \\
&= \langle n|a^\dagger a|n\rangle \\
&= \|a|n\rangle\|^2 \ge 0
\end{aligned}
$$

したがって，$\mathbf{N}$ のすべての固有値は $0$ 以上です。

ここで，$n$ が $0$ でも正の整数でもないと仮定します。このとき $n$ を超えない最大の非負整数を $k$ とすると，$0 < n - k < 1$ です。設問2より，状態 $|n\rangle$ に消滅演算子 $a$ を1回作用させるごとにノルムの2乗は固有値に等しく $0$ でないため，状態はゼロベクトルになりません。$k + 1$ 回作用させると，固有値 $n - (k + 1) < 0$ をもつゼロでない固有状態 $a^{k+1}|n\rangle$ が得られます。

これは $\mathbf{N}$ の固有値がすべて $0$ 以上であることに矛盾します。したがって $n$ は $0$ または正の整数であり，ちょうど $n$ 回 $a$ を作用させた状態 $|0\rangle$ で $a|0\rangle = 0$ となります。

### (4)

ハイゼンベルグ表示における任意の時刻 $t$ で正準交換関係 $[\mathbf{x}(t), \mathbf{p}(t)] = i\hbar$ が成り立ちます。ハミルトニアン $\mathbf{H}$ は時間に依存せず $\mathbf{H} = \dfrac{\mathbf{p}(t)^2}{2m} + \dfrac{m\omega^2}{2}\mathbf{x}(t)^2$ と書くことができます。ハイゼンベルグ方程式 $\dfrac{\mathrm{d}\mathbf{A}}{\mathrm{d}t} = \dfrac{1}{i\hbar}[\mathbf{A}, \mathbf{H}]$ を計算します。

$$
\begin{aligned}
\frac{\mathrm{d}\mathbf{x}(t)}{\mathrm{d}t} &= \frac{1}{i\hbar}\left[\mathbf{x}(t),\ \frac{\mathbf{p}(t)^2}{2m}\right] \\
&= \frac{1}{2mi\hbar}\Bigl(\mathbf{p}(t)[\mathbf{x}(t), \mathbf{p}(t)] + [\mathbf{x}(t), \mathbf{p}(t)]\mathbf{p}(t)\Bigr) \\
&= \frac{1}{2mi\hbar}\bigl(2i\hbar\mathbf{p}(t)\bigr) \\
&= \frac{\mathbf{p}(t)}{m}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}\mathbf{p}(t)}{\mathrm{d}t} &= \frac{1}{i\hbar}\left[\mathbf{p}(t),\ \frac{m\omega^2}{2}\mathbf{x}(t)^2\right] \\
&= \frac{m\omega^2}{2i\hbar}\Bigl(\mathbf{x}(t)[\mathbf{p}(t), \mathbf{x}(t)] + [\mathbf{p}(t), \mathbf{x}(t)]\mathbf{x}(t)\Bigr) \\
&= \frac{m\omega^2}{2i\hbar}\bigl(-2i\hbar\mathbf{x}(t)\bigr) \\
&= -m\omega^2\mathbf{x}(t)
\end{aligned}
$$

したがって，ハイゼンベルグ方程式は次式となります。

$$
\finalanswer{\frac{\mathrm{d}\mathbf{x}(t)}{\mathrm{d}t} = \frac{\mathbf{p}(t)}{m}, \qquad \frac{\mathrm{d}\mathbf{p}(t)}{\mathrm{d}t} = -m\omega^2\mathbf{x}(t)}
$$

### (5)

設問4の第1式を時間 $t$ で微分し，第2式を代入します。

$$
\begin{aligned}
\frac{\mathrm{d}^2\mathbf{x}(t)}{\mathrm{d}t^2} &= \frac{1}{m}\frac{\mathrm{d}\mathbf{p}(t)}{\mathrm{d}t} \\
&= -\omega^2\mathbf{x}(t)
\end{aligned}
$$

これは単振動の2階線形常微分方程式なので，一般解は時刻 $t = 0$ の演算子 $\mathbf{x}(0)$ と $\dot{\mathbf{x}}(0) = \dfrac{\mathbf{p}(0)}{m}$ を用いて次のように表されます。

$$
\mathbf{x}(t) = \mathbf{x}(0)\cos\omega t + \frac{\mathbf{p}(0)}{m\omega}\sin\omega t
$$

これを時間微分して $m$ を掛けると $\mathbf{p}(t)$ が得られます。

$$
\mathbf{p}(t) = \mathbf{p}(0)\cos\omega t - m\omega\mathbf{x}(0)\sin\omega t
$$

また，$a$ と $a^\dagger$ の定義から $\mathbf{x}(0) = \sqrt{\dfrac{\hbar}{2m\omega}}(a + a^\dagger)$，$\mathbf{p}(0) = -i\sqrt{\dfrac{m\hbar\omega}{2}}(a - a^\dagger)$ を代入すると，次式になります。

$$
\begin{aligned}
\mathbf{x}(t) &= \sqrt{\frac{\hbar}{2m\omega}}\bigl(a e^{-i\omega t} + a^\dagger e^{i\omega t}\bigr) \\
\mathbf{p}(t) &= -i\sqrt{\frac{m\hbar\omega}{2}}\bigl(a e^{-i\omega t} - a^\dagger e^{i\omega t}\bigr)
\end{aligned}
$$

演算子 $\mathbf{x}(t)$ と $\mathbf{p}(t)$ の時間依存性は，初期値 $\mathbf{x}(0), \mathbf{p}(0)$ に対して $\cos\omega t$ と $\sin\omega t$ で振動する形になっており，古典調和振動子の運動の解と同じ形の時間変動をします。

$$
\finalanswer{\mathbf{x}(t) = \mathbf{x}(0)\cos\omega t + \frac{\mathbf{p}(0)}{m\omega}\sin\omega t, \qquad \mathbf{p}(t) = \mathbf{p}(0)\cos\omega t - m\omega\mathbf{x}(0)\sin\omega t}
$$

### (6)

設問2より $a|n\rangle = \sqrt{n}|n - 1\rangle$，$a^\dagger|n\rangle = \sqrt{n + 1}|n + 1\rangle$ であり，異なる固有値の固有状態は直交するため $\langle n|n - 1\rangle = \langle n|n + 1\rangle = 0$ です。したがって $\langle n|a|n\rangle = 0$，$\langle n|a^\dagger|n\rangle = 0$ となります。

これを設問5の $\mathbf{x}(t)$ と $\mathbf{p}(t)$ の表式に代入します。

$$
\begin{aligned}
\langle n|\mathbf{x}(t)|n\rangle &= \sqrt{\frac{\hbar}{2m\omega}}\bigl(\langle n|a|n\rangle e^{-i\omega t} + \langle n|a^\dagger|n\rangle e^{i\omega t}\bigr) \\
&= 0
\end{aligned}
$$

$$
\begin{aligned}
\langle n|\mathbf{p}(t)|n\rangle &= -i\sqrt{\frac{m\hbar\omega}{2}}\bigl(\langle n|a|n\rangle e^{-i\omega t} - \langle n|a^\dagger|n\rangle e^{i\omega t}\bigr) \\
&= 0
\end{aligned}
$$

したがって，期待値はいずれも $0$ となります。

$$
\finalanswer{\langle n|\mathbf{x}(t)|n\rangle = 0, \qquad \langle n|\mathbf{p}(t)|n\rangle = 0}
$$

### (7)

$0$ でない複素数 $\lambda$ を用いて，関数 $F(a, a^\dagger)$ を次のように選びます。

$$
\begin{aligned}
F(a, a^\dagger) &= e^{\lambda a^\dagger} \\
&= \sum_{n=0}^{\infty} \frac{\lambda^n}{n!}(a^\dagger)^n
\end{aligned}
$$

この状態 $|\lambda\rangle = e^{\lambda a^\dagger}|G\rangle$ に消滅演算子 $a$ を作用させます。$[a, (a^\dagger)^n] = n(a^\dagger)^{n-1}$ と $a|G\rangle = 0$ を用います。

$$
\begin{aligned}
a|\lambda\rangle &= \sum_{n=1}^{\infty} \frac{\lambda^n}{n!}\,n(a^\dagger)^{n-1}|G\rangle \\
&= \lambda\sum_{m=0}^{\infty} \frac{\lambda^m}{m!}(a^\dagger)^m|G\rangle \\
&= \lambda|\lambda\rangle
\end{aligned}
$$

エルミート共役をとると $\langle\lambda|a^\dagger = \lambda^*\langle\lambda|$ も成り立ちます。この状態は消滅演算子 $a$ の固有状態であり，**コヒーレント状態**といいます。$\lambda = |\lambda|e^{i\varphi}$ と表し，規格化因子 $\langle\lambda|\lambda\rangle$ で割った期待値を計算します。

$$
\begin{aligned}
\frac{\langle\lambda|\mathbf{x}(t)|\lambda\rangle}{\langle\lambda|\lambda\rangle} &= \sqrt{\frac{\hbar}{2m\omega}}\bigl(\lambda e^{-i\omega t} + \lambda^* e^{i\omega t}\bigr) \\
&= \sqrt{\frac{2\hbar}{m\omega}}|\lambda|\cos(\omega t - \varphi)
\end{aligned}
$$

$$
\begin{aligned}
\frac{\langle\lambda|\mathbf{p}(t)|\lambda\rangle}{\langle\lambda|\lambda\rangle} &= -i\sqrt{\frac{m\hbar\omega}{2}}\bigl(\lambda e^{-i\omega t} - \lambda^* e^{i\omega t}\bigr) \\
&= -\sqrt{2m\hbar\omega}|\lambda|\sin(\omega t - \varphi)
\end{aligned}
$$

これらは角振動数 $\omega$ の古典的な単振動と同じ時間変動を示します。したがって，$F(a, a^\dagger)$ の具体例は次式となります。

$$
\finalanswer{F(a, a^\dagger) = e^{\lambda a^\dagger} \qquad (\lambda \neq 0)}
$$
