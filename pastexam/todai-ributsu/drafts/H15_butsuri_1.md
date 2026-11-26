---
title: 東大理物 平成15年度 物理学 第1問：1次元井戸型ポテンシャルの急膨張と断熱定理
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成15年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成15年度 物理学 第1問：1次元井戸型ポテンシャルの急膨張と断熱定理

## 問題

高さ無限大の壁に囲まれた幅 $2L$ の一次元井戸型ポテンシャルに，高さ無限大で幅が $L$ に比べて十分小さいポテンシャル障壁を設け，質量 $m$ の粒子を左半分（幅 $L$）に閉じこめる（図1）。井戸型ポテンシャルの底をエネルギーの原点とする。
{: .problem-lead }

<figure class="problem-figure" markdown>
![中央に障壁のある幅2Lの1次元無限井戸型ポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H15_butsuri_1-p-light.svg#only-light)
![中央に障壁のある幅2Lの1次元無限井戸型ポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H15_butsuri_1-p-dark.svg#only-dark)
<figcaption markdown="span">図1：幅 $2L$ の1次元井戸型ポテンシャルと中央 $x = L$ の薄い障壁。</figcaption>
</figure>

(1) 粒子が量子力学的な基底状態にあるとして，そのエネルギー $E_0$ を求めよ。

(2) ポテンシャル障壁を突然取り去って，粒子が幅 $2L$ のポテンシャル井戸全体を動けるようにする。このとき，粒子が基底状態にある確率を求めよ。またエネルギー期待値はいくらか。

(3) ポテンシャル障壁を取り去った時刻から $t$ 秒後の粒子の波動関数を $\psi(x, t)$ とする。いま仮に $\psi(x, t)$ がわかったとしよう。時刻 $t$ において粒子の位置を観測したとき，粒子が井戸の左半分でみつかる確率は，この $\psi(x, t)$ を用いてどのように書けるか。ただし，$\psi(x, t)$ は規格化されているとする。

(4) 上記の $\psi(x, t)$ の表式を求めよ。ただし級数和はそのまま残してよい。

(5) 今度は設問 (1) の状態からポテンシャル障壁をきわめてゆっくりと右端まで動かす場合について考えよう。このようなゆっくりとしたポテンシャルの変化に対しては断熱定理が成り立ち，粒子は連続的に移り変わることのできる量子数の同じ固有状態にとどまる。このことを使って，粒子が幅 $2L$ のポテンシャル井戸全体を動けるようにした後の粒子のエネルギー期待値を，設問 (1) で求めた $E_0$ を用いて表せ。

(6) 上記の断熱定理が成り立つことを，以下の手順で示せ。

左側のポテンシャル井戸の幅が $a$ のとき（$L \le a \le 2L$）に粒子が取り得る固有状態を $\phi_n(x, a)$，その固有エネルギーを $\varepsilon_n(a)$（$n$ は負でない整数）と書く。$\phi_n(x, a)$ は規格直交化されているものとする。$t = 0$ で基底状態にいた粒子の，時間 $t$ での波動関数をつぎのように展開する。

$$
\psi(x, t) = \sum_{n} c_n(t)\phi_n(x, a)\exp\!\left\{-\frac{i}{\hbar}\int_{0}^{t} \varepsilon_n(a)\,\mathrm{d}\tau\right\}.
$$

$a$ が時間に依存することに注意して，時間に依存する波動方程式から，係数ベクトル $\{c_n(t)\}$ の満たすべき関係式が次の形に書けることを示し，$a$ や $t$ によらない係数行列 $J_{mn}$ の表式を求めよ。

$$
\frac{\mathrm{d}c_n(t)}{\mathrm{d}t} = -\sum_{m} c_m(t)\frac{1}{a}\frac{\mathrm{d}a}{\mathrm{d}t} J_{mn}\exp\!\left\{+\frac{i}{\hbar}\int_{0}^{t} \bigl[\varepsilon_n(a) - \varepsilon_m(a)\bigr]\mathrm{d}\tau\right\}.
$$

ただし $J_{nn} = 0$ である。次にこの関係式を用いて，ある条件の下で断熱定理（$c_n(t) \simeq c_n(0)$）が成り立つことを説明せよ。

(7) ポテンシャル井戸の左半分に閉じ込められた粒子を，運動エネルギー $E_0$ の古典粒子だとする。設問 (5) と同様に壁をゆっくりと（断熱的に）右端まで動かしたあとのエネルギーが，設問 (5) で求めた量子系の結果と同じであることを示せ。ただし，粒子は壁と弾性衝突（はねかえり係数 $1$）するとし，壁を動かしている間に粒子は壁と十分多くの回数衝突するとせよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成15年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，障壁を突然取り去る前後で波動関数そのものは変わらないことを用いて，幅 $2L$ の井戸の固有状態へ展開し，展開係数から基底状態の確率や時間発展する波動関数を求めます。

後半では，幅 $a(t)$ が時間変化する井戸の瞬間固有状態で波動関数を展開し，シュレーディンガー方程式に代入することで，状態間の遷移を与える結合行列 $J_{mn}$ と断熱条件を導きます。さらに古典粒子が動く壁と弾性衝突を繰り返す際の速度変化から，同じエネルギー変化が得られることを導きます。
</div>

### (1)

粒子は $0 < x < L$ に閉じ込められているため，この領域での時間によらないシュレーディンガー方程式は次式になります。

$$
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2 \psi}{\mathrm{d}x^2} = E\psi
$$

境界条件は $\psi(0) = \psi(L) = 0$ です。波数を $k = \dfrac{\sqrt{2mE}}{\hbar}$ とおくと，この境界条件を満たす解は正の整数 $n$ に対して $\sin(kx)$ の形となり，$kL = n\pi$ です。基底状態は $n = 1$ のときなので，エネルギー $E_0$ と規格化された波動関数 $\psi_0(x)$ は次式になります。

$$
\psi_0(x) = \begin{cases}
\sqrt{\dfrac{2}{L}}\sin\!\left(\dfrac{\pi x}{L}\right) & (0 < x < L) \\
0 & (L \le x < 2L)
\end{cases}
$$

$$
\finalanswer{E_0 = \frac{\pi^2\hbar^2}{2mL^2}}
$$

### (2)

障壁を取り去った後の幅 $2L$ の井戸における規格化された固有状態 $\varphi_k(x)$ と固有エネルギー $\mathcal{E}_k$ は，正の整数 $k = 1, 2, 3, \dots$ に対して次式です。

$$
\varphi_k(x) = \sqrt{\frac{1}{L}}\sin\!\left(\frac{k\pi x}{2L}\right), \qquad \mathcal{E}_k = \frac{k^2\pi^2\hbar^2}{8mL^2}
$$

ここで $\mathcal{E}_k = \dfrac{k^2}{4}E_0$ の関係があります。障壁を突然取り去った直後の波動関数は $\psi_0(x)$ のまま変化しません。幅 $2L$ の井戸の基底状態 $\varphi_1(x)$ との内積 $c_1$ を計算します。

$$
\begin{aligned}
c_1 &= \int_{0}^{2L} \varphi_1^*(x)\psi_0(x)\,\mathrm{d}x \\
&= \frac{\sqrt{2}}{L}\int_{0}^{L} \sin\!\left(\frac{\pi x}{2L}\right)\sin\!\left(\frac{\pi x}{L}\right)\mathrm{d}x \\
&= \frac{\sqrt{2}}{2L}\int_{0}^{L} \left\{\cos\!\left(\frac{\pi x}{2L}\right) - \cos\!\left(\frac{3\pi x}{2L}\right)\right\}\mathrm{d}x \\
&= \frac{\sqrt{2}}{2L}\left[\frac{2L}{\pi}\sin\!\left(\frac{\pi x}{2L}\right) - \frac{2L}{3\pi}\sin\!\left(\frac{3\pi x}{2L}\right)\right]_{0}^{L} \\
&= \frac{\sqrt{2}}{\pi}\left(1 + \frac{1}{3}\right) \\
&= \frac{4\sqrt{2}}{3\pi}
\end{aligned}
$$

したがって，粒子が基底状態にある確率 $P_1 = |c_1|^2$ は次式になります。

$$
\begin{aligned}
P_1 &= \left(\frac{4\sqrt{2}}{3\pi}\right)^2 \\
&= \frac{32}{9\pi^2}
\end{aligned}
$$

次にエネルギー期待値を求めます。障壁を取り去った直後の状態 $\psi_0(x)$ は $L \le x < 2L$ で $0$ であり，ポテンシャルエネルギーは $0 < x < 2L$ で $0$ です。したがって，新しいハミルトニアン $H$ に対する期待値は取り去る前と同じになります。

$$
\begin{aligned}
\langle E \rangle &= \int_{0}^{2L} \psi_0^*(x)\left(-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d}x^2}\right)\psi_0(x)\,\mathrm{d}x \\
&= \int_{0}^{L} \psi_0^*(x)\,E_0\psi_0(x)\,\mathrm{d}x \\
&= E_0
\end{aligned}
$$

以上より，基底状態にある確率とエネルギー期待値は次式となります。

$$
\finalanswer{P_1 = \frac{32}{9\pi^2}, \qquad \langle E \rangle = E_0 = \frac{\pi^2\hbar^2}{2mL^2}}
$$

### (3)

時刻 $t$ における位置の存在確率密度は $|\psi(x, t)|^2$ です。井戸の左半分は $0 \le x \le L$ なので，粒子が左半分で見つかる確率 $P_{\mathrm{left}}(t)$ は次式となります。

$$
\finalanswer{P_{\mathrm{left}}(t) = \int_{0}^{L} |\psi(x, t)|^2\,\mathrm{d}x}
$$

### (4)

時刻 $t = 0$ の状態 $\psi_0(x)$ を幅 $2L$ の井戸の固有状態 $\varphi_k(x)$ で展開し，各展開係数 $c_k = \int_{0}^{L} \varphi_k^*(x)\psi_0(x)\,\mathrm{d}x$ を求めます。

まず $k = 2$ のとき，$\varphi_2(x) = \sqrt{\dfrac{1}{L}}\sin\!\left(\dfrac{\pi x}{L}\right)$ なので，積分の値は次式になります。

$$
\begin{aligned}
c_2 &= \frac{\sqrt{2}}{L}\int_{0}^{L} \sin^2\!\left(\frac{\pi x}{L}\right)\mathrm{d}x \\
&= \frac{\sqrt{2}}{L}\cdot\frac{L}{2} \\
&= \frac{1}{\sqrt{2}}
\end{aligned}
$$

$k = 2j$（$j \ge 2$ の整数）のとき，$\sin\!\left(\dfrac{j\pi x}{L}\right)$ と $\sin\!\left(\dfrac{\pi x}{L}\right)$ は区間 $[0, L]$ で直交するため，$c_{2j} = 0$ となります。

$k$ が奇数のとき，$k = 2j + 1$（$j = 0, 1, 2, \dots$）として積和の公式で積分します。

$$
\begin{aligned}
c_k &= \frac{\sqrt{2}}{2L}\int_{0}^{L} \left\{\cos\!\left(\frac{(k - 2)\pi x}{2L}\right) - \cos\!\left(\frac{(k + 2)\pi x}{2L}\right)\right\}\mathrm{d}x \\
&= \frac{\sqrt{2}}{\pi}\left\{\frac{\sin\!\left(\dfrac{(k - 2)\pi}{2}\right)}{k - 2} - \frac{\sin\!\left(\dfrac{(k + 2)\pi}{2}\right)}{k + 2}\right\}
\end{aligned}
$$

奇数 $k = 2j + 1$ に対して $\sin\!\left(\dfrac{(k - 2)\pi}{2}\right) = -(-1)^j$ かつ $\sin\!\left(\dfrac{(k + 2)\pi}{2}\right) = -(-1)^j$ が成り立つため，次のように整理することができます。

$$
\begin{aligned}
c_{2j+1} &= -\frac{\sqrt{2}\,(-1)^j}{\pi}\left(\frac{1}{2j - 1} - \frac{1}{2j + 3}\right) \\
&= -\frac{4\sqrt{2}\,(-1)^j}{\pi\bigl((2j + 1)^2 - 4\bigr)} \\
&= \frac{4\sqrt{2}\,(-1)^j}{\pi\bigl(4 - (2j + 1)^2\bigr)}
\end{aligned}
$$

各固有状態は時間とともに $e^{-i\mathcal{E}_k t/\hbar}$ の位相因子をもつため，時刻 $t$ の波動関数 $\psi(x, t) = \sum_{k=1}^{\infty} c_k \varphi_k(x) e^{-i\mathcal{E}_k t/\hbar}$ は次式となります。ここで $\mathcal{E}_k = \dfrac{k^2}{4}E_0$ です。

$$
\finalanswer{\psi(x, t) = \frac{1}{\sqrt{2L}}\sin\!\left(\frac{\pi x}{L}\right)e^{-i E_0 t/\hbar} + \frac{4\sqrt{2}}{\pi\sqrt{L}}\sum_{j=0}^{\infty} \frac{(-1)^j}{4 - (2j + 1)^2}\sin\!\left(\frac{(2j + 1)\pi x}{2L}\right)\exp\!\left(-i\frac{(2j + 1)^2 E_0 t}{4\hbar}\right)}
$$

### (5)

断熱定理により，障壁を十分ゆっくり右端 $x = 2L$ まで動かすと，粒子は常にその時点の井戸の基底状態にとどまります。幅 $2L$ になった後の基底状態エネルギーは $\mathcal{E}_1 = \dfrac{\pi^2\hbar^2}{2m(2L)^2}$ なので，$E_0 = \dfrac{\pi^2\hbar^2}{2mL^2}$ を用いて次式となります。

$$
\finalanswer{\langle E \rangle = \frac{1}{4}E_0}
$$

### (6)

展開式 $\psi(x, t) = \sum_{m} c_m(t)\phi_m(x, a)\exp\!\left\{-\dfrac{i}{\hbar}\int_{0}^{t} \varepsilon_m(a)\,\mathrm{d}\tau\right\}$ を時間に依存するシュレーディンガー方程式 $i\hbar\dfrac{\partial\psi}{\partial t} = H(a)\psi$ に代入します。左辺の時間微分を計算します。

$$
\begin{aligned}
i\hbar\frac{\partial\psi}{\partial t} &= \sum_{m} \left\{i\hbar\frac{\mathrm{d}c_m}{\mathrm{d}t}\phi_m + i\hbar c_m\frac{\mathrm{d}a}{\mathrm{d}t}\frac{\partial\phi_m}{\partial a} + c_m\varepsilon_m(a)\phi_m\right\}\exp\!\left\{-\frac{i}{\hbar}\int_{0}^{t} \varepsilon_m(a)\,\mathrm{d}\tau\right\}
\end{aligned}
$$

右辺は $H(a)\phi_m(x, a) = \varepsilon_m(a)\phi_m(x, a)$ より左辺の最後の項と一致して打ち消し合います。したがって，次式が残ります。

$$
\sum_{m} \left\{\frac{\mathrm{d}c_m}{\mathrm{d}t}\phi_m(x, a) + c_m\frac{\mathrm{d}a}{\mathrm{d}t}\frac{\partial\phi_m(x, a)}{\partial a}\right\}\exp\!\left\{-\frac{i}{\hbar}\int_{0}^{t} \varepsilon_m(a)\,\mathrm{d}\tau\right\} = 0
$$

両辺に $\phi_n^*(x, a)$ を掛けて $x$ について $0$ から $a$ まで積分し，正規直交性 $\int_{0}^{a} \phi_n^*(x, a)\phi_m(x, a)\,\mathrm{d}x = \delta_{nm}$ を用います。

$$
\frac{\mathrm{d}c_n}{\mathrm{d}t}\exp\!\left\{-\frac{i}{\hbar}\int_{0}^{t} \varepsilon_n(a)\,\mathrm{d}\tau\right\} + \sum_{m} c_m\frac{\mathrm{d}a}{\mathrm{d}t}\left(\int_{0}^{a} \phi_n^*(x, a)\frac{\partial\phi_m(x, a)}{\partial a}\,\mathrm{d}x\right)\exp\!\left\{-\frac{i}{\hbar}\int_{0}^{t} \varepsilon_m(a)\,\mathrm{d}\tau\right\} = 0
$$

両辺に $\exp\!\left\{+\dfrac{i}{\hbar}\int_{0}^{t} \varepsilon_n(a)\,\mathrm{d}\tau\right\}$ を掛けて移項すると，次の形になります。

$$
\frac{\mathrm{d}c_n(t)}{\mathrm{d}t} = -\sum_{m} c_m(t)\frac{1}{a}\frac{\mathrm{d}a}{\mathrm{d}t} J_{mn}\exp\!\left\{+\frac{i}{\hbar}\int_{0}^{t} \bigl[\varepsilon_n(a) - \varepsilon_m(a)\bigr]\mathrm{d}\tau\right\}
$$

ここで $J_{mn}$ は次式で定義されます。

$$
J_{mn} = a\int_{0}^{a} \phi_n^*(x, a)\frac{\partial\phi_m(x, a)}{\partial a}\,\mathrm{d}x
$$

非負整数 $n, m = 0, 1, 2, \dots$ に対して $N = n + 1$，$M = m + 1$ とおくと，$\phi_m(x, a) = \sqrt{\dfrac{2}{a}}\sin\!\left(\dfrac{M\pi x}{a}\right)$ は実関数です。これを $a$ で偏微分します。

$$
\frac{\partial\phi_m(x, a)}{\partial a} = -\frac{1}{2a}\sqrt{\frac{2}{a}}\sin\!\left(\frac{M\pi x}{a}\right) - \frac{M\pi x}{a^2}\sqrt{\frac{2}{a}}\cos\!\left(\frac{M\pi x}{a}\right)
$$

$\xi = \dfrac{x}{a}$ と置換して $J_{mn}$ を計算します。

$$
\begin{aligned}
J_{mn} &= a\int_{0}^{1} \sqrt{\frac{2}{a}}\sin(N\pi\xi)\left\{-\frac{1}{2a}\sqrt{\frac{2}{a}}\sin(M\pi\xi) - \frac{M\pi\xi}{a}\sqrt{\frac{2}{a}}\cos(M\pi\xi)\right\}a\,\mathrm{d}\xi \\
&= -\frac{1}{2}\delta_{mn} - 2M\pi\int_{0}^{1} \xi\sin(N\pi\xi)\cos(M\pi\xi)\,\mathrm{d}\xi
\end{aligned}
$$

まず $m = n$ のときの第2項を倍角の公式と部分積分で計算します。

$$
\begin{aligned}
2N\pi\int_{0}^{1} \xi\sin(N\pi\xi)\cos(N\pi\xi)\,\mathrm{d}\xi &= N\pi\int_{0}^{1} \xi\sin(2N\pi\xi)\,\mathrm{d}\xi \\
&= N\pi\left[-\frac{\xi\cos(2N\pi\xi)}{2N\pi}\right]_{0}^{1} \\
&= -\frac{1}{2}
\end{aligned}
$$

よって $J_{nn} = -\dfrac{1}{2} - \left(-\dfrac{1}{2}\right) = 0$ です。次に $m \neq n$ のときは積和の公式と部分積分 $\int_{0}^{1} \xi\sin(K\pi\xi)\,\mathrm{d}\xi = -\dfrac{(-1)^K}{K\pi}$（$K$ は $0$ でない整数）を用います。

$$
\begin{aligned}
J_{mn} &= -M\pi\int_{0}^{1} \xi\Bigl\{\sin\bigl((N + M)\pi\xi\bigr) + \sin\bigl((N - M)\pi\xi\bigr)\Bigr\}\mathrm{d}\xi \\
&= M\pi\left\{\frac{(-1)^{N+M}}{(N + M)\pi} + \frac{(-1)^{N-M}}{(N - M)\pi}\right\} \\
&= (-1)^{N+M} M\left(\frac{1}{N + M} + \frac{1}{N - M}\right) \\
&= (-1)^{n+m}\frac{2MN}{N^2 - M^2}
\end{aligned}
$$

これは $a$ にも $t$ にもよりません。$N = n + 1$，$M = m + 1$ を戻すと $J_{mn}$ は次式となります。

$$
\finalanswer{J_{mn} = \begin{cases} (-1)^{n+m}\dfrac{2(m + 1)(n + 1)}{(n + 1)^2 - (m + 1)^2} & (m \neq n) \\ 0 & (m = n) \end{cases}}
$$

次に断熱定理が成り立つ理由を説明します。時刻 $t = 0$ で基底状態 $c_0(0) = 1$，$c_n(0) = 0$（$n \ge 1$）にあるとし，壁の移動速度が十分遅い場合を考えます。1次の摂動近似で右辺に $c_m(t) \simeq \delta_{m0}$ を代入して $n \ge 1$ の係数 $c_n(t)$ を時間積分します。

$$
c_n(t) \simeq -J_{0n}\int_{0}^{t} \frac{1}{a}\frac{\mathrm{d}a}{\mathrm{d}t'}\exp\!\left\{+\frac{i}{\hbar}\int_{0}^{t'} \bigl[\varepsilon_n(a) - \varepsilon_0(a)\bigr]\mathrm{d}\tau\right\}\mathrm{d}t'
$$

遷移角振動数 $\omega_{n0}(t') = \dfrac{\varepsilon_n(a) - \varepsilon_0(a)}{\hbar}$ を用いて部分積分を行います。

$$
c_n(t) \simeq \left[\frac{i J_{0n}}{\omega_{n0}(t')}\frac{1}{a}\frac{\mathrm{d}a}{\mathrm{d}t'} e^{i\int_{0}^{t'} \omega_{n0}\,\mathrm{d}\tau}\right]_{0}^{t} - i J_{0n}\int_{0}^{t} \frac{\mathrm{d}}{\mathrm{d}t'}\left(\frac{1}{\omega_{n0}(t') a}\frac{\mathrm{d}a}{\mathrm{d}t'}\right)e^{i\int_{0}^{t'} \omega_{n0}\,\mathrm{d}\tau}\,\mathrm{d}t'
$$

したがって，壁の幅の相対変化率 $\dfrac{1}{a}\left|\dfrac{\mathrm{d}a}{\mathrm{d}t}\right|$ がすべての $n \ge 1$ に対する遷移角振動数 $\omega_{n0} = \dfrac{\varepsilon_n(a) - \varepsilon_0(a)}{\hbar}$ に比べて十分小さい条件

$$
\frac{1}{a}\left|\frac{\mathrm{d}a}{\mathrm{d}t}\right| \ll \frac{\varepsilon_n(a) - \varepsilon_0(a)}{\hbar}
$$

が成り立つとき，右辺は $\dfrac{\hbar\dot{a}}{a(\varepsilon_n - \varepsilon_0)}$ の程度で $0$ に近づきます。よって任意の $n \ge 1$ について $c_n(t) \simeq 0$，かつ規格化条件より $c_0(t) \simeq 1$ となり，断熱定理 $c_n(t) \simeq c_n(0)$ が成り立ちます。

### (7)

壁の幅が $a(t)$ であるとき，古典粒子の速さを $v(t)$，壁の移動速度を $u = \dfrac{\mathrm{d}a}{\mathrm{d}t} > 0$ とおきます。壁は十分ゆっくり動くため $u \ll v$ です。

粒子が速さ $v$ で右向きの動く壁に衝突すると，壁とともに動く座標系では粒子は速さ $v - u$ で衝突し，弾性衝突によって逆向きに速さ $v - u$ ではね返ります。静止座標系に戻すと，衝突後の粒子の速さ $v'$ は次式になります。

$$
\begin{aligned}
v' &= (v - u) - u \\
&= v - 2u
\end{aligned}
$$

したがって，1回の衝突による速さの変化は $\Delta v = -2\dfrac{\mathrm{d}a}{\mathrm{d}t}$ です。一方，粒子が左端 $x = 0$ で反射して再び右の壁に戻るまでの時間間隔は，壁の動きが十分遅いので $\Delta t \simeq \dfrac{2a}{v}$ です。

壁が動く間に粒子は十分多くの回数衝突するため，速さの時間変化率を連続的な微分方程式で近似します。

$$
\begin{aligned}
\frac{\mathrm{d}v}{\mathrm{d}t} &\simeq \frac{\Delta v}{\Delta t} \\
&= \frac{-2\,\dfrac{\mathrm{d}a}{\mathrm{d}t}}{\dfrac{2a}{v}} \\
&= -\frac{v}{a}\frac{\mathrm{d}a}{\mathrm{d}t}
\end{aligned}
$$

両辺に $a$ を掛けて移項します。

$$
a\frac{\mathrm{d}v}{\mathrm{d}t} + v\frac{\mathrm{d}a}{\mathrm{d}t} = 0
$$

左辺を積の微分にまとめます。

$$
\frac{\mathrm{d}(va)}{\mathrm{d}t} = 0
$$

よって積 $va$ は壁をゆっくり動かす過程で一定に保たれます。壁の位置が $a = L$ から $a = 2L$ へ変化すると，粒子の速さは初速 $v_0$ から $v_1 = \dfrac{1}{2}v_0$ になります。したがって，変化後の運動エネルギー $E_1$ は次式となります。

$$
\begin{aligned}
E_1 &= \frac{1}{2}m v_1^2 \\
&= \frac{1}{2}m\left(\frac{v_0}{2}\right)^2 \\
&= \frac{1}{4}E_0
\end{aligned}
$$

これは設問 (5) で求めた量子系の結果 $\dfrac{1}{4}E_0$ と一致します。
