---
title: 東大理物 令和2年度 物理学 第1問：二状態系とベルの不等式
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 令和2年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 令和2年度 物理学 第1問：二状態系とベルの不等式

## 問題

量子力学的二状態系を考えよう。この場合，観測量は $2\times 2$ のエルミート行列で表される演算子に対応する。以下では次の行列表記をもつ観測量

$$
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},\qquad
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\qquad
\sigma(\theta) = (\cos\theta)\sigma_z + (\sin\theta)\sigma_x \tag{1}
$$

を考え，状態ベクトルを

$$
|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\qquad
|\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \tag{2}
$$

を用いて表す。

(1) 状態 $|\uparrow\rangle$ において観測量 $\sigma_z$ を測定した。測定結果が取りうる値 $s_z$，およびその期待値を求めよ。

(2) 状態 $|\uparrow\rangle$ において観測量 $\sigma_x$ を測定した。測定結果が取りうる値 $s_x$，およびその期待値を求めよ。

(3) 状態 $|\uparrow\rangle$ において観測量 $\sigma(\theta)$ を測定した。測定結果が取りうる値 $s_\theta$，およびその期待値を求めよ。

上記の二状態系 $A, B$ からなる複合系を考える。その状態は四状態
{: .problem-lead }

$$
|\uparrow\rangle_A|\uparrow\rangle_B,\quad
|\uparrow\rangle_A|\downarrow\rangle_B,\quad
|\downarrow\rangle_A|\uparrow\rangle_B,\quad
|\downarrow\rangle_A|\downarrow\rangle_B \tag{3}
$$

の線形結合で書ける。そのような複合系を準備したのち，二状態系 $A, B$ をそれぞれ別の場所で測定する。模式図は以下を参照せよ：
{: .problem-lead }

<figure class="problem-figure" markdown>
![複合系を準備し部分系AとBをそれぞれ別の場所で測定する模式図](../../../docs/assets/figures/pastexam-todai-ributsu/R2_butsuri_1-p-light.svg#only-light)
![複合系を準備し部分系AとBをそれぞれ別の場所で測定する模式図](../../../docs/assets/figures/pastexam-todai-ributsu/R2_butsuri_1-p-dark.svg#only-dark)
<figcaption markdown="span">模式図：</figcaption>
</figure>

この設定の下で，次の実験を考える。
{: .problem-lead }

実験：状態

$$
|\Psi\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\rangle_A|\downarrow\rangle_B - |\downarrow\rangle_A|\uparrow\rangle_B\right) \tag{4}
$$

の複合系を毎回新たに準備し，部分系 $A$ において観測量 $\sigma_z^A,\ \sigma_x^A,\ \sigma^A(\theta)$ のいずれか，部分系 $B$ において観測量 $\sigma_z^B,\ \sigma_x^B,\ \sigma^B(\varphi)$ のいずれかを測定する。この実験を，何度も繰り返すことを考えよう。
{: .problem-lead }

(4) 毎回，部分系 $A$ で $\sigma_z^A$，部分系 $B$ で $\sigma_z^B$ を測定する。取りうる測定結果の組 $(s_z^A, s_z^B)$ を述べよ。また，積 $s_z^A s_z^B$ の期待値を求めよ。

(5) 毎回，部分系 $A$ で $\sigma_x^A$，部分系 $B$ で $\sigma_x^B$ を測定する。取りうる測定結果の組 $(s_x^A, s_x^B)$ を述べよ。また，積 $s_x^A s_x^B$ の期待値を求めよ。

(6) 毎回，部分系 $A$ で $\sigma^A(\theta)$，部分系 $B$ で $\sigma^B(\theta)$ を測定する。この場合，測定結果の組 $(s_\theta^A, s_\theta^B)$ は $s_\theta^A = -s_\theta^B = \pm 1$ を満たすことを示せ。

(7) 毎回，部分系 $A$ で $\sigma^A(\theta)$，部分系 $B$ で $\sigma^B(\varphi)$ を測定する。取りうる測定結果の組 $(s_\theta^A, s_\varphi^B)$ を述べよ。また，積 $s_\theta^A s_\varphi^B$ の期待値を求めよ。

(8) 各回，部分系 $A$ で測定する観測量 $\sigma^A(\theta)$ を $\sigma^A(0^\circ),\ \sigma^A(120^\circ),\ \sigma^A(240^\circ)$ からそれぞれ $1/3$ の確率で測定者が選択することにし，また，部分系 $B$ でも，測定する観測量 $\sigma^B(\varphi)$ を $\sigma^B(0^\circ),\ \sigma^B(120^\circ),\ \sigma^B(240^\circ)$ からそれぞれ $1/3$ の確率で測定者が選択することにする。測定結果の組 $(s^A, s^B)$ の取りうる値を述べよ。また，積 $s^A s^B$ の期待値を求め，それが $0$ になることを示せ。

これまでは量子力学を用いて考察を行ったが，そのようにして得られた設問8の結論は，以下でのべる決定論的仮説と矛盾することを確認しよう。設問8の設定において，量子力学的には，各回の実験では，部分系 $A$ について $\sigma^A(0^\circ),\ \sigma^A(120^\circ),\ \sigma^A(240^\circ)$ のどれか一つ，部分系 $B$ について $\sigma^B(0^\circ),\ \sigma^B(120^\circ),\ \sigma^B(240^\circ)$ のどれか一つしか測定できない。これに対し，決定論的に，次のように考えてみよう。
{: .problem-lead }

仮説：各回の実験ごとに，実際に対応する観測量を測定したかしなかったかにかかわらず，部分系 $A$ で $\sigma^A(0^\circ),\ \sigma^A(120^\circ),\ \sigma^A(240^\circ)$ を測定したとすると得られるであろう測定結果 $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A)$，部分系 $B$ で $\sigma^B(0^\circ),\ \sigma^B(120^\circ),\ \sigma^B(240^\circ)$ を測定した場合に得られるであろう測定結果 $(s_{0^\circ}^B, s_{120^\circ}^B, s_{240^\circ}^B)$ があらかじめ決まっているとする。設問6よりこれらは

$$
s_{0^\circ}^A = -s_{0^\circ}^B,\qquad
s_{120^\circ}^A = -s_{120^\circ}^B,\qquad
s_{240^\circ}^A = -s_{240^\circ}^B \tag{5}
$$

を満たすとする。
{: .problem-lead }

(9) 上記の仮説のもと，設問8と同様，部分系 $A$ で $\sigma^A(0^\circ),\ \sigma^A(120^\circ),\ \sigma^A(240^\circ)$ をそれぞれ $1/3$ の確率で測定し，部分系 $B$ で $\sigma^B(0^\circ),\ \sigma^B(120^\circ),\ \sigma^B(240^\circ)$ をそれぞれ $1/3$ の確率で測定する。このとき，$\sigma^A(\theta)$ を測定した際に得られる測定結果を $s^A = s_\theta^A$，$\sigma^B(\varphi)$ を測定した際に得られる測定結果を $s^B = s_\varphi^B$ と書く。

(i) $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A) = (+1, +1, +1)$ の場合，$s^A s^B$ の期待値を求めよ。

(ii) $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A) = (+1, +1, -1)$ の場合，$s^A s^B$ の期待値を求めよ。

(iii) 八通り $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A) = (\pm 1, \pm 1, \pm 1)$ が任意に起こる場合，$s^A s^B$ の期待値は負であることを示せ。

設問8の量子力学による結果では $s^A s^B$ の期待値は $0$ であり，上記の決定論的仮説のもとでは $s^A s^B$ の期待値は負となった。これより，量子力学は上記の決定論的仮説とは矛盾することがわかる。（この問題は，N. David Mermin, Physics Today **38**, 4, pp. 38–47 (1985) を参考にした。）
{: .problem-lead }

> 出典：東京大学大学院理学系研究科物理学専攻 令和2年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
測定値の候補は演算子の固有値ですが，その値が実際に現れるかは状態との重なりで判断します。複合系では，選んだ2つの観測量の固有基底に状態を展開して，各結果の確率を求めます。

測定方向をランダムに選ぶ場合，方向を固定した期待値をその選択確率で平均します。値があらかじめ定まるという仮説も，同じ方向の選び方で平均して比較します。
</div>

### (1)
$|\uparrow\rangle$ は $\sigma_z$ の固有値 $+1$ に属する固有状態です。

$$
\begin{aligned}
\sigma_z|\uparrow\rangle &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} \\
&= (+1)|\uparrow\rangle
\end{aligned}
$$

よって測定結果は確率 $1$ で $+1$ となり，期待値も $+1$ です。したがって，

$$
\finalanswer{s_z = +1,\qquad \langle s_z \rangle = 1}
$$

### (2)
$\sigma_x$ の固有値 $+1,\ -1$ に対応する規格化された固有状態は，それぞれ

$$
|+_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix},\qquad
|-_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

です。$\sigma_x|\pm_x\rangle=\pm|\pm_x\rangle$ を満たします。状態 $|\uparrow\rangle$ をこの固有基底で展開します。

$$
|\uparrow\rangle = \frac{1}{\sqrt{2}}\left(|+_x\rangle + |-_x\rangle\right)
$$

よって $s_x = +1$ と $s_x = -1$ がそれぞれ確率 $\left|\dfrac{1}{\sqrt{2}}\right|^2 = \dfrac{1}{2}$ で得られます。期待値は次のようになります。

$$
\begin{aligned}
\langle s_x \rangle &= \langle\uparrow|\sigma_x|\uparrow\rangle \\
&= \frac{1}{2}(+1) + \frac{1}{2}(-1) \\
&= 0
\end{aligned}
$$

したがって，

$$
\finalanswer{s_x = \pm 1,\qquad \langle s_x \rangle = 0}
$$

### (3)
$\sigma(\theta)$ の行列表記は次のとおりです。

$$
\sigma(\theta) = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}
$$



$$
\begin{aligned}
\sigma(\theta)^2 &= (\cos^2\theta + \sin^2\theta)I \\
&= I
\end{aligned}
$$

 なので，$\sigma(\theta)$ の固有値は $\pm 1$ です。それぞれに対応する規格化固有状態は

$$
|+\theta\rangle = \begin{pmatrix} \cos\dfrac{\theta}{2} \\ \sin\dfrac{\theta}{2} \end{pmatrix},\qquad
|-\theta\rangle = \begin{pmatrix} -\sin\dfrac{\theta}{2} \\ \cos\dfrac{\theta}{2} \end{pmatrix}
$$

です。状態 $|\uparrow\rangle$ をこの基底で展開します。

$$
|\uparrow\rangle = \cos\frac{\theta}{2}\,|+\theta\rangle - \sin\frac{\theta}{2}\,|-\theta\rangle
$$

したがって，$s_\theta = +1$ を得る確率は $\cos^2\dfrac{\theta}{2}$，$s_\theta = -1$ を得る確率は $\sin^2\dfrac{\theta}{2}$ です。$\theta$ の値によって確率が $0$ になる場合を分けると，取りうる値 $s_\theta$ は次のようになります。ここで $n$ は整数です。

- $\theta = 2n\pi$ のとき：$s_\theta = +1$ のみ
- $\theta = (2n + 1)\pi$ のとき：$s_\theta = -1$ のみ
- それ以外の $\theta$ のとき：$s_\theta = \pm 1$

また，期待値は次のとおりです。

$$
\begin{aligned}
\langle s_\theta \rangle &= \langle\uparrow|\sigma(\theta)|\uparrow\rangle \\
&= (+1)\cos^2\frac{\theta}{2} + (-1)\sin^2\frac{\theta}{2} \\
&= \cos\theta
\end{aligned}
$$

したがって，

$$
\finalanswer{\langle s_\theta\rangle=\cos\theta,\qquad s_\theta\in\begin{cases}\{+1\}&\theta=2n\pi\\\{-1\}&\theta=(2n+1)\pi\\\{+1,-1\}&\theta\notin\pi\mathbb Z\end{cases}\quad(n\in\mathbb Z)}
$$



### (4)
状態 $|\Psi\rangle = \dfrac{1}{\sqrt{2}}\left(|\uparrow\rangle_A|\downarrow\rangle_B - |\downarrow\rangle_A|\uparrow\rangle_B\right)$ は，すでに $\sigma_z^A$ と $\sigma_z^B$ の同時固有基底で展開されています。

$|\uparrow\rangle_A|\downarrow\rangle_B$ に対応する測定結果は $(+1, -1)$，$|\downarrow\rangle_A|\uparrow\rangle_B$ に対応する測定結果は $(-1, +1)$ であり，それぞれ確率 $\dfrac{1}{2}$ で得られます。どちらの場合も積は $s_z^A s_z^B = -1$ なので，期待値も $-1$ です。したがって，

$$
\finalanswer{(s_z^A, s_z^B) = (+1, -1),\ (-1, +1),\qquad \langle s_z^A s_z^B \rangle = -1}
$$

### (5)
$|\uparrow\rangle = \dfrac{1}{\sqrt{2}}(|+_x\rangle + |-_x\rangle)$，$|\downarrow\rangle = \dfrac{1}{\sqrt{2}}(|+_x\rangle - |-_x\rangle)$ を式 (4) に代入します。

$$
\begin{aligned}
|\Psi\rangle
&= \frac{1}{2\sqrt{2}}\Bigl[(|+_x\rangle_A + |-_x\rangle_A)(|+_x\rangle_B - |-_x\rangle_B) - (|+_x\rangle_A - |-_x\rangle_A)(|+_x\rangle_B + |-_x\rangle_B)\Bigr] \\
&= -\frac{1}{\sqrt{2}}\left(|+_x\rangle_A|-_x\rangle_B - |-_x\rangle_A|+_x\rangle_B\right)
\end{aligned}
$$

よって測定結果の組は $(+1, -1)$ と $(-1, +1)$ がそれぞれ確率 $\dfrac{1}{2}$ で得られ，積の期待値は $-1$ です。したがって，

$$
\finalanswer{(s_x^A, s_x^B) = (+1, -1),\ (-1, +1),\qquad \langle s_x^A s_x^B \rangle = -1}
$$

### (6)
問3の固有基底 $|+\theta\rangle,\ |-\theta\rangle$ を用いて $|\uparrow\rangle,\ |\downarrow\rangle$ を表します。

$$
|\uparrow\rangle = \cos\frac{\theta}{2}|+\theta\rangle - \sin\frac{\theta}{2}|-\theta\rangle,\qquad
|\downarrow\rangle = \sin\frac{\theta}{2}|+\theta\rangle + \cos\frac{\theta}{2}|-\theta\rangle
$$

これらを $|\Psi\rangle$ に代入すると，展開の同符号項が打ち消し合い，次のようになります。

$$
\begin{aligned}
|\Psi\rangle
&= \frac{1}{\sqrt{2}}\left[\left(\cos^2\frac{\theta}{2} + \sin^2\frac{\theta}{2}\right)|+\theta\rangle_A|-\theta\rangle_B - \left(\sin^2\frac{\theta}{2} + \cos^2\frac{\theta}{2}\right)|-\theta\rangle_A|+\theta\rangle_B\right] \\
&= \frac{1}{\sqrt{2}}\left(|+\theta\rangle_A|-\theta\rangle_B - |-\theta\rangle_A|+\theta\rangle_B\right)
\end{aligned}
$$

よって $\sigma^A(\theta),\ \sigma^B(\theta)$ の測定で得られる組は $(+1, -1)$ と $(-1, +1)$で，確率はそれぞれ $\dfrac12$ です。取りうる組はこの2通りのみであり，必ず $s_\theta^A=\pm1$，$s_\theta^B=\mp1$ が成り立ちます。

### (7)
問6で示した $|\Psi\rangle = \dfrac{1}{\sqrt{2}}\left(|+\theta\rangle_A|-\theta\rangle_B - |-\theta\rangle_A|+\theta\rangle_B\right)$ に対して，部分系 $B$ の状態を $\sigma^B(\varphi)$ の固有基底 $|+\varphi\rangle_B,\ |-\varphi\rangle_B$ で展開します。

内積 $\langle +\varphi | +\theta \rangle = \cos\dfrac{\theta-\varphi}{2}$，$\langle -\varphi | +\theta \rangle = \sin\dfrac{\theta-\varphi}{2}$，$\langle +\varphi | -\theta \rangle = -\sin\dfrac{\theta-\varphi}{2}$，$\langle -\varphi | -\theta \rangle = \cos\dfrac{\theta-\varphi}{2}$ を用いると，

$$
\begin{aligned}
|-\theta\rangle_B &= -\sin\frac{\theta-\varphi}{2}|+\varphi\rangle_B + \cos\frac{\theta-\varphi}{2}|-\varphi\rangle_B \\
|+\theta\rangle_B &= \cos\frac{\theta-\varphi}{2}|+\varphi\rangle_B + \sin\frac{\theta-\varphi}{2}|-\varphi\rangle_B
\end{aligned}
$$

なので，$|\Psi\rangle$ は次のように展開されます。

$$
\begin{aligned}
|\Psi\rangle
&= -\frac{1}{\sqrt{2}}\sin\frac{\theta-\varphi}{2}\,|+\theta\rangle_A|+\varphi\rangle_B
   + \frac{1}{\sqrt{2}}\cos\frac{\theta-\varphi}{2}\,|+\theta\rangle_A|-\varphi\rangle_B \\
&\quad - \frac{1}{\sqrt{2}}\cos\frac{\theta-\varphi}{2}\,|-\theta\rangle_A|+\varphi\rangle_B
   - \frac{1}{\sqrt{2}}\sin\frac{\theta-\varphi}{2}\,|-\theta\rangle_A|-\varphi\rangle_B
\end{aligned}
$$

各結果の確率は次のとおりです。

$$
\begin{aligned}
P(+1, +1) &= P(-1, -1) & \\
&= \frac{1}{2}\sin^2\frac{\theta-\varphi}{2} \\
P(+1, -1) &= P(-1, +1) & \\
&= \frac{1}{2}\cos^2\frac{\theta-\varphi}{2}
\end{aligned}
$$

これより，取りうる組 $(s_\theta^A, s_\varphi^B)$ は角度差 $\theta - \varphi$ に応じて次のようになります。ここで $n$ は整数です。

- $\theta - \varphi = 2n\pi$ のとき：$(+1, -1),\ (-1, +1)$
- $\theta - \varphi = (2n + 1)\pi$ のとき：$(+1, +1),\ (-1, -1)$
- それ以外のとき：$(+1, +1),\ (+1, -1),\ (-1, +1),\ (-1, -1)$ の4通りすべて

また，積 $s_\theta^A s_\varphi^B$ の期待値は次のようになります。

$$
\begin{aligned}
\langle s_\theta^A s_\varphi^B \rangle
&= (+1)\cdot 2\cdot\frac{1}{2}\sin^2\frac{\theta-\varphi}{2} + (-1)\cdot 2\cdot\frac{1}{2}\cos^2\frac{\theta-\varphi}{2} \\
&= -\cos(\theta - \varphi)
\end{aligned}
$$

したがって，

$$
\finalanswer{\langle s_\theta^As_\varphi^B\rangle=-\cos(\theta-\varphi)}
$$

$\Delta=\theta-\varphi$ とおくと，取りうる組は

$$
\finalanswer{(s_\theta^A,s_\varphi^B)\in\begin{cases}\{(+1,-1),(-1,+1)\}&\Delta=2n\pi\\\{(+1,+1),(-1,-1)\}&\Delta=(2n+1)\pi\\\{+1,-1\}^2&\Delta\notin\pi\mathbb Z\end{cases}\quad(n\in\mathbb Z)}
$$



### (8)
角度の組 $(\theta,\varphi)$ は $\{0^\circ,120^\circ,240^\circ\}^2$ の9通りがそれぞれ確率 $1/9$ で選ばれます。異なる方向を選んだ場合，同符号と異符号の結果がいずれも正の確率を持ちます。したがって，取りうる組は

$$
\finalanswer{(s^A,s^B)\in\{(+1,+1),(+1,-1),(-1,+1),(-1,-1)\}}
$$

です。

積 $s^A s^B$ の期待値は，9通りの角度組に対する問7の結果の平均です。

- $\theta = \varphi$ となる組は $(0^\circ, 0^\circ),\ (120^\circ, 120^\circ),\ (240^\circ, 240^\circ)$ の $3$ 通りあり，いずれも $-\cos(0^\circ) = -1$。
- $\theta \neq \varphi$ となる組は残りの $6$ 通りあり，いずれも $|\theta - \varphi| = 120^\circ$ または $240^\circ$ なので 

$$
\begin{aligned}
-\cos(\theta - \varphi) &= -\left(-\dfrac{1}{2}\right) \\
&= \dfrac{1}{2}
\end{aligned}
$$

。

よって，

$$
\begin{aligned}
\langle s^A s^B \rangle &= \frac{1}{9}\left[3\times(-1) + 6\times\frac{1}{2}\right] \\
&= \frac{-3 + 3}{9} \\
&= 0
\end{aligned}
$$

となり，期待値が $0$ になることが確かめられます。

### (9)
仮説の式 (5) より $s_\varphi^B = -s_\varphi^A$ なので，角度の組 $(\theta, \varphi)$ を選んだときの積は 

$$
\begin{aligned}
s^A s^B &= s_\theta^A s_\varphi^B \\
&= -s_\theta^A s_\varphi^A
\end{aligned}
$$

 です。$9$ 通りの組 $(\theta, \varphi)$ が等確率 $\dfrac{1}{9}$ で選ばれるため，与えられた $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A)$ に対する期待値は次の式で求めることができます。

$$
\begin{aligned}
\langle s^A s^B \rangle
&= -\frac{1}{9}\sum_{\theta}\sum_{\varphi} s_\theta^A s_\varphi^A \\
&= -\frac{1}{9}\left(s_{0^\circ}^A + s_{120^\circ}^A + s_{240^\circ}^A\right)^2
\end{aligned}
$$

(i) $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A) = (+1, +1, +1)$ のとき，$9$ 通りのすべての組で $s^A s^B = -1$ となります。

$$
\begin{aligned}
\langle s^A s^B \rangle &= -\frac{1}{9}(1 + 1 + 1)^2 \\
&= -1
\end{aligned}
$$

したがって，

$$
\finalanswer{\langle s^As^B\rangle=-1}
$$

(ii) $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A) = (+1, +1, -1)$ のとき，$9$ 通りの組のうち $s_\theta^A s_\varphi^A = +1$ となる組が $5$ 通り，$s_\theta^A s_\varphi^A = -1$ となる組が $4$ 通りなので，

$$
\begin{aligned}
\langle s^A s^B \rangle &= -\frac{1}{9}(1 + 1 - 1)^2 \\
&= -\frac{1}{9}
\end{aligned}
$$

したがって，

$$
\finalanswer{\langle s^As^B\rangle=-\frac19}
$$

(iii) 八通りの組合せ $(s_{0^\circ}^A, s_{120^\circ}^A, s_{240^\circ}^A) \in \{+1, -1\}^3$ について，3つの値の和 $S = s_{0^\circ}^A + s_{120^\circ}^A + s_{240^\circ}^A$ が取りうる値は，3つとも同符号のときの $\pm 3$ と，2つが同符号で1つが異符号のときの $\pm 1$ のみであり，$S = 0$ になることはありません。

よって各組合せ $k\ (k = 1, \dots, 8)$ が生起したときの条件付き期待値 $E_k = -\dfrac{1}{9}S_k^2$ は $-1$ または $-\dfrac{1}{9}$ のいずれかであり，すべての $k$ について $E_k \le -\dfrac{1}{9} < 0$ を満たします。

八通りが任意の確率分布 $\{p_k\}$（$p_k \ge 0,\ \sum_{k=1}^8 p_k = 1$）で生起するとき，全体の期待値は

$$
\begin{aligned}
\langle s^A s^B \rangle &= \sum_{k=1}^{8} p_k E_k \le -\frac{1}{9}\sum_{k=1}^{8} p_k \\
&= -\frac{1}{9} < 0
\end{aligned}
$$

となり，常に負であることが確かめられます。


