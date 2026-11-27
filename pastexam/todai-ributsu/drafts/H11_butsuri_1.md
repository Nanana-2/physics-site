---
title: 東大理物 平成11年度 物理学 第1問：1次元無限井戸型ポテンシャル中の2電子系とスピン依存接触相互作用
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成11年度 物理学 第1問：1次元無限井戸型ポテンシャル中の2電子系とスピン依存接触相互作用

## 問題

井戸型ポテンシャルの中に置かれた電子系の運動を考える。電子の運動は $x$ 軸方向のみを考えればよく，それに直行する方向の運動は考えない。ポテンシャルは $-a < x < a$（$a$ は正の定数）では $0$ で，$x = -a$ および $x = +a$ に無限に高い壁をもつ。$i$ 番目（$i = 1, 2, \dots$）の電子の座標を $x_i$ とし，そのスピンを $\vec{s}_i$ と表わす。またその電子のスピン波動関数については，上向きを $u_\uparrow(i)$，下向きを $u_\downarrow(i)$ とする。電子の質量を $m$ として，以下の設問に答えよ。
{: .problem-lead }

(1) 1個の電子をこの井戸型ポテンシャルの中に入れた時のエネルギー固有値を求めよ。ただし，下から $n$ 番目（$n = 1, 2, \dots$）のものを $E_n$ とせよ。

(2) 電子はフェルミ粒子である。この事実は，この井戸型ポテンシャル内に2個の電子を入れた時に，それらの波動関数にどのような条件を課すか，述べよ。

(3) 2個の電子をこの井戸型ポテンシャル内に入れたところ，最も低いエネルギー固有状態が実現された。この時の系のエネルギー固有値を求め，その状態での電子系の波動関数を，スピン部分まで含めて示せ。さらに，電子の合成スピン演算子

$$
\vec{S} = \vec{s}_1 + \vec{s}_2
$$

に対して，この状態での $(\vec{S}\cdot\vec{S})$ の期待値を求めよ。以後，$(\cdot)$ は内積を表わす。

(4) 設問 (3) と同じ場合で，2番目に低いエネルギー固有状態が実現されていたとする。このエネルギー固有値に属する系の固有状態には，どのようなものがあり得るか。スピン部分まで含め，それらの波動関数を示せ。

(5) ここで電子間に

$$
V = f \times (\vec{s}_1\cdot\vec{s}_2) \times \delta(x_1 - x_2)
$$

という相互作用が働くとする。ただし $f$ は結合定数で，十分に小さい正の値をとるものとし，$\delta(\ )$ はデルタ関数を表わす。この相互作用が加わったとき，設問 (3) で求めた状態のエネルギー固有値の変化を計算せよ。

(6) 設問 (5) の相互作用 $V$ が働いたとき，設問 (3) の状態と，設問 (4) で考えた状態（複数でもよい）は，どのように混ざるか答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
1次元無限井戸型ポテンシャル中の1粒子固有状態をもとに，フェルミ粒子の反対称性を使って2電子系の基底状態および第1励起状態を構成します。空間部分の対称性とスピン部分の対称性が互いに反対になることに注意して，1重項と3重項を整理します。

後半のスピン依存デルタ関数型相互作用については，1次摂動によるエネルギーシフトを計算したうえで，合成スピンの保存と空間反転対称性の両面から基底状態と第1励起状態との混合の有無を判定します。
</div>

### (1)

井戸の内部 $-a < x < a$ における1電子の時間に依存しないシュレーディンガー方程式は次の通りです。

$$
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\phi(x)}{\mathrm{d}x^2} = E\phi(x)
$$

壁の位置 $x = \pm a$ でポテンシャルが無限大となるため，境界条件は $\phi(-a) = 0$ および $\phi(a) = 0$ です。$E > 0$ として波数 $k = \dfrac{\sqrt{2mE}}{\hbar} > 0$ を導入すると，一般解は

$$
\phi(x) = A\cos(kx) + B\sin(kx)
$$

となります。境界条件 $\phi(\pm a) = 0$ を代入します。

$$
\begin{aligned}
A\cos(ka) + B\sin(ka) &= 0 \\
A\cos(ka) - B\sin(ka) &= 0
\end{aligned}
$$

両式の和と差をとると，$A\cos(ka) = 0$ および $B\sin(ka) = 0$ が得られます。恒等的に $0$ でない解は偶関数解と奇関数解の2系列に分かれます。

- 偶関数解：$B = 0$ かつ $\cos(ka) = 0$ より，$ka = \dfrac{n\pi}{2}$（$n = 1, 3, 5, \dots$）
- 奇関数解：$A = 0$ かつ $\sin(ka) = 0$ より，$ka = \dfrac{n\pi}{2}$（$n = 2, 4, 6, \dots$）

両者をまとめると，すべての正の整数 $n = 1, 2, 3, \dots$ に対して波数は $k_n = \dfrac{n\pi}{2a}$ となります。これよりエネルギー固有値 $E_n$ を求めます。

$$
\begin{aligned}
E_n &= \frac{\hbar^2 k_n^2}{2m} \\
&= \frac{\hbar^2 \pi^2 n^2}{8ma^2}
\end{aligned}
$$

なお，規格化された1電子固有関数 $\phi_n(x)$（$-a < x < a$）は，偶奇に応じて次の通りです。

$$
\phi_n(x) =
\begin{cases}
\dfrac{1}{\sqrt{a}}\cos\left(\dfrac{n\pi x}{2a}\right) & (n = 1, 3, 5, \dots) \\[10pt]
\dfrac{1}{\sqrt{a}}\sin\left(\dfrac{n\pi x}{2a}\right) & (n = 2, 4, 6, \dots)
\end{cases}
$$

特に $n = 1, 2$ の固有関数は次のようになります。

$$
\begin{aligned}
\phi_1(x) &= \frac{1}{\sqrt{a}}\cos\left(\frac{\pi x}{2a}\right) \\
\phi_2(x) &= \frac{1}{\sqrt{a}}\sin\left(\frac{\pi x}{a}\right)
\end{aligned}
$$

$$
\finalanswer{E_n = \frac{\hbar^2 \pi^2 n^2}{8ma^2} \quad (n = 1, 2, 3, \dots)}
$$

### (2)

2個の電子の座標とスピン変数をまとめて $(x_1, \sigma_1)$，$(x_2, \sigma_2)$ とし，2電子系の波動関数を $\Psi(x_1, \sigma_1; x_2, \sigma_2)$ とします。電子はフェルミ粒子であるため，2個の電子の座標とスピンを同時に入れ替えたとき，波動関数は符号を反転させる必要があります。すなわち，次の反対称性の条件が課されます。

$$
\Psi(x_2, \sigma_2; x_1, \sigma_1) = -\Psi(x_1, \sigma_1; x_2, \sigma_2)
$$

この結果として，2個の電子は空間状態とスピン状態を合わせた同一の1粒子量子状態を同時に占有することができません。

### (3)

電子間の相互作用がないとき，2電子系のエネルギー固有値は1電子エネルギー固有値の和 $E_{n_1} + E_{n_2}$ となります。最も低いエネルギー固有値は $n_1 = 1$ かつ $n_2 = 1$ のときに実現されます。

$$
\begin{aligned}
E_{\mathrm{g}} &= E_1 + E_1 \\
&= \frac{\hbar^2 \pi^2}{4ma^2}
\end{aligned}
$$

このとき空間部分の波動関数 $\phi_1(x_1)\phi_1(x_2)$ は2電子の入れ替えに対して対称です。したがって (2) の反対称性の条件を満たすため，スピン部分は入れ替えに対して反対称なスピン1重項状態である必要があります。規格化された基底状態の波動関数 $\Psi_0$ は次の通りです。

$$
\Psi_0 = \phi_1(x_1)\phi_1(x_2)\frac{1}{\sqrt{2}}\bigl(u_\uparrow(1)u_\downarrow(2) - u_\downarrow(1)u_\uparrow(2)\bigr)
$$

ここで $\phi_1(x) = \dfrac{1}{\sqrt{a}}\cos\left(\dfrac{\pi x}{2a}\right)$（$-a < x < a$）です。

次に合成スピン $\vec{S} = \vec{s}_1 + \vec{s}_2$ に対して $\vec{S}\cdot\vec{S}$ の期待値を求めます。$\vec{S}^2$ の固有値は合成スピン量子数 $S$ を用いて $\hbar^2 S(S + 1)$ で与えられます。スピン1重項状態 $\chi_{0,0} = \dfrac{1}{\sqrt{2}}\bigl(u_\uparrow(1)u_\downarrow(2) - u_\downarrow(1)u_\uparrow(2)\bigr)$ は $S = 0$ の固有状態であるため，次が成り立ちます。

$$
\langle \Psi_0 | \vec{S}\cdot\vec{S} | \Psi_0 \rangle = 0
$$

念のため昇降演算子 $s_{i\pm} = s_{ix} \pm i s_{iy}$ を用いて直接確認することもできます。$\vec{S}^2 = \vec{s}_1^2 + \vec{s}_2^2 + 2s_{1z}s_{2z} + s_{1+}s_{2-} + s_{1-}s_{2+}$ を $\chi_{0,0}$ に作用させると，$\vec{s}_1^2$ と $\vec{s}_2^2$ の固有値はともに $\dfrac{3}{4}\hbar^2$，$2s_{1z}s_{2z}\chi_{0,0} = -\dfrac{1}{2}\hbar^2\chi_{0,0}$，$(s_{1+}s_{2-} + s_{1-}s_{2+})\chi_{0,0} = -\hbar^2\chi_{0,0}$ となり，和は $0$ に一致します。

$$
\finalanswer{E_{\mathrm{g}} = \frac{\hbar^2 \pi^2}{4ma^2},\quad \Psi_0 = \frac{1}{a}\cos\left(\frac{\pi x_1}{2a}\right)\cos\left(\frac{\pi x_2}{2a}\right)\frac{u_\uparrow(1)u_\downarrow(2) - u_\downarrow(1)u_\uparrow(2)}{\sqrt{2}},\quad \langle \vec{S}\cdot\vec{S} \rangle = 0}
$$

### (4)

2電子系の2番目に低いエネルギー固有値は，一方の電子が $n = 1$，他方が $n = 2$ の準位を占めるときに実現されます。そのエネルギー固有値は次の通りです。

$$
\begin{aligned}
E_{\mathrm{e}} &= E_1 + E_2 \\
&= \frac{\hbar^2 \pi^2}{8ma^2}(1^2 + 2^2) \\
&= \frac{5\hbar^2 \pi^2}{8ma^2}
\end{aligned}
$$

$\phi_1$ と $\phi_2$ は異なる1粒子軌道であるため，2電子の入れ替えに対して対称な空間波動関数 $\Phi_{\mathrm{s}}$ と反対称な空間波動関数 $\Phi_{\mathrm{a}}$ の両方を構成することができます。

$$
\begin{aligned}
\Phi_{\mathrm{s}}(x_1, x_2) &= \frac{1}{\sqrt{2}}\bigl(\phi_1(x_1)\phi_2(x_2) + \phi_2(x_1)\phi_1(x_2)\bigr) \\
\Phi_{\mathrm{a}}(x_1, x_2) &= \frac{1}{\sqrt{2}}\bigl(\phi_1(x_1)\phi_2(x_2) - \phi_2(x_1)\phi_1(x_2)\bigr)
\end{aligned}
$$

全体の波動関数を反対称にするため，対称な空間状態 $\Phi_{\mathrm{s}}$ には反対称なスピン1重項状態（$S = 0$）を組み合わせ，反対称な空間状態 $\Phi_{\mathrm{a}}$ には対称なスピン3重項状態（$S = 1$）を組み合わせます。したがって，固有状態は合計4重に縮退しており，規格化された固有波動関数は次の4通りです。

まずスピン1重項状態（$S = 0$，$M_S = 0$）は次の1通りです。

$$
\Psi_{1,0} = \frac{1}{\sqrt{2}}\bigl(\phi_1(x_1)\phi_2(x_2) + \phi_2(x_1)\phi_1(x_2)\bigr)\frac{1}{\sqrt{2}}\bigl(u_\uparrow(1)u_\downarrow(2) - u_\downarrow(1)u_\uparrow(2)\bigr)
$$

次にスピン3重項状態（$S = 1$，$M_S = +1, 0, -1$）は次の3通りです。

$$
\begin{aligned}
\Psi_{1,+1} &= \frac{1}{\sqrt{2}}\bigl(\phi_1(x_1)\phi_2(x_2) - \phi_2(x_1)\phi_1(x_2)\bigr)u_\uparrow(1)u_\uparrow(2) \\
\Psi_{1,0}^{(\mathrm{t})} &= \frac{1}{\sqrt{2}}\bigl(\phi_1(x_1)\phi_2(x_2) - \phi_2(x_1)\phi_1(x_2)\bigr)\frac{1}{\sqrt{2}}\bigl(u_\uparrow(1)u_\downarrow(2) + u_\downarrow(1)u_\uparrow(2)\bigr) \\
\Psi_{1,-1} &= \frac{1}{\sqrt{2}}\bigl(\phi_1(x_1)\phi_2(x_2) - \phi_2(x_1)\phi_1(x_2)\bigr)u_\downarrow(1)u_\downarrow(2)
\end{aligned}
$$

ここで $\phi_1(x) = \dfrac{1}{\sqrt{a}}\cos\left(\dfrac{\pi x}{2a}\right)$，$\phi_2(x) = \dfrac{1}{\sqrt{a}}\sin\left(\dfrac{\pi x}{a}\right)$（$-a < x < a$）です。

$$
\finalanswer{\begin{aligned}
\Psi_{1,0} &= \frac{\phi_1(x_1)\phi_2(x_2) + \phi_2(x_1)\phi_1(x_2)}{\sqrt{2}}\cdot\frac{u_\uparrow(1)u_\downarrow(2) - u_\downarrow(1)u_\uparrow(2)}{\sqrt{2}} \\
\Psi_{1,+1} &= \frac{\phi_1(x_1)\phi_2(x_2) - \phi_2(x_1)\phi_1(x_2)}{\sqrt{2}}\,u_\uparrow(1)u_\uparrow(2) \\
\Psi_{1,0}^{(\mathrm{t})} &= \frac{\phi_1(x_1)\phi_2(x_2) - \phi_2(x_1)\phi_1(x_2)}{\sqrt{2}}\cdot\frac{u_\uparrow(1)u_\downarrow(2) + u_\downarrow(1)u_\uparrow(2)}{\sqrt{2}} \\
\Psi_{1,-1} &= \frac{\phi_1(x_1)\phi_2(x_2) - \phi_2(x_1)\phi_1(x_2)}{\sqrt{2}}\,u_\downarrow(1)u_\downarrow(2)
\end{aligned}}
$$

### (5)

結合定数 $f$ は十分に小さい正の定数であるため，$V = f(\vec{s}_1\cdot\vec{s}_2)\delta(x_1 - x_2)$ を摂動として扱います。(3) で求めた基底状態 $\Psi_0$ は非縮退なので，1次摂動によるエネルギー固有値の変化 $\Delta E_0^{(1)}$ は期待値 $\langle \Psi_0 | V | \Psi_0 \rangle$ で与えられます。

まずスピン部分の期待値を計算します。$\vec{S} = \vec{s}_1 + \vec{s}_2$ の2乗を展開すると次式が得られます。

$$
\vec{s}_1\cdot\vec{s}_2 = \frac{1}{2}\left(\vec{S}^2 - \vec{s}_1^2 - \vec{s}_2^2\right)
$$

$\Psi_0$ は $S = 0$ のスピン1重項であり，各電子のスピン量子数は $s_1 = \dfrac{1}{2}$，$s_2 = \dfrac{1}{2}$ なので，期待値は次のように求まります。

$$
\begin{aligned}
\langle \vec{s}_1\cdot\vec{s}_2 \rangle &= \frac{1}{2}\left(0 - \frac{3}{4}\hbar^2 - \frac{3}{4}\hbar^2\right) \\
&= -\frac{3}{4}\hbar^2
\end{aligned}
$$

次に空間部分の期待値を計算します。デルタ関数の性質より $x_2 = x_1$ での1重積分になります。

$$
\begin{aligned}
\int_{-a}^{a}\mathrm{d}x_1 \int_{-a}^{a}\mathrm{d}x_2\, |\phi_1(x_1)\phi_1(x_2)|^2 \delta(x_1 - x_2) &= \int_{-a}^{a} |\phi_1(x)|^4\,\mathrm{d}x \\
&= \frac{1}{a^2}\int_{-a}^{a} \cos^4\left(\frac{\pi x}{2a}\right)\mathrm{d}x
\end{aligned}
$$

ここで変数変換 $\theta = \dfrac{\pi x}{2a}$ を行うと，$\mathrm{d}x = \dfrac{2a}{\pi}\,\mathrm{d}\theta$，積分区間は $-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$ となります。倍角公式を2回用いて積分します。

$$
\begin{aligned}
\frac{1}{a^2}\int_{-a}^{a}\cos^4\left(\frac{\pi x}{2a}\right)\mathrm{d}x &= \frac{2}{\pi a}\int_{-\pi/2}^{\pi/2}\cos^4\theta\,\mathrm{d}\theta \\
&= \frac{2}{\pi a}\int_{-\pi/2}^{\pi/2}\left(\frac{1 + \cos 2\theta}{2}\right)^2\mathrm{d}\theta \\
&= \frac{1}{2\pi a}\int_{-\pi/2}^{\pi/2}\left(1 + 2\cos 2\theta + \frac{1 + \cos 4\theta}{2}\right)\mathrm{d}\theta \\
&= \frac{1}{2\pi a}\cdot\frac{3}{2}\pi \\
&= \frac{3}{4a}
\end{aligned}
$$

スピン部分と空間部分の期待値を掛け合わせると，基底状態のエネルギー変化が得られます。

$$
\begin{aligned}
\Delta E_0^{(1)} &= f \left(-\frac{3}{4}\hbar^2\right)\left(\frac{3}{4a}\right) \\
&= -\frac{9f\hbar^2}{16a}
\end{aligned}
$$

$f > 0$ より，相互作用 $V$ によって1重項基底状態のエネルギーは低下します。

$$
\finalanswer{\Delta E_0 = -\frac{9f\hbar^2}{16a}}
$$

<aside class="rigor-note" markdown>
スピン演算子 $\vec{s}_i$ を $\hbar$ を含まない無次元演算子（$\vec{s}_i^2 = \dfrac{3}{4}$）として定義する流儀を採用した場合は，$\Delta E_0 = -\dfrac{9f}{16a}$ となります。解答では角運動量としての次元をもつ標準的な定義（$\vec{s}_i = \dfrac{\hbar}{2}\vec{\sigma}_i$）に従いました。
</aside>

### (6)

相互作用 $V = f(\vec{s}_1\cdot\vec{s}_2)\delta(x_1 - x_2)$ による，(3) の基底状態 $\Psi_0$ と (4) の4つの第1励起状態との行列要素を調べます。

まず (4) の3つのスピン3重項状態 $\Psi_{1,+1}, \Psi_{1,0}^{(\mathrm{t})}, \Psi_{1,-1}$ について考えます。$\vec{s}_1\cdot\vec{s}_2$ は合成スピン $\vec{S}^2$ と可換であるため，異なる合成スピン量子数をもつ $S = 0$ の状態と $S = 1$ の状態の間の行列要素は $0$ になります。さらに空間部分についても，3重項状態の空間波動関数 $\Phi_{\mathrm{a}}(x_1, x_2)$ は $x_1 = x_2$ で恒等的に $0$ となるため，$\delta(x_1 - x_2)$ を掛けた時点で恒等的に消えます。

次に (4) のスピン1重項状態 $\Psi_{1,0}$ との行列要素 $\langle \Psi_{1,0} | V | \Psi_0 \rangle$ を計算します。スピン部分はどちらも $S = 0$ なので $\langle \chi_{0,0} | \vec{s}_1\cdot\vec{s}_2 | \chi_{0,0} \rangle = -\dfrac{3}{4}\hbar^2$ となり $0$ ではありません。一方，空間部分の積分は次のようになります。

$$
\begin{aligned}
I &= \int_{-a}^{a}\mathrm{d}x_1 \int_{-a}^{a}\mathrm{d}x_2\, \Phi_{\mathrm{s}}^*(x_1, x_2)\,\delta(x_1 - x_2)\,\phi_1(x_1)\phi_1(x_2) \\
&= \sqrt{2}\int_{-a}^{a} \phi_1(x)^3 \phi_2(x)\,\mathrm{d}x
\end{aligned}
$$

ここで $\phi_1(x) = \dfrac{1}{\sqrt{a}}\cos\left(\dfrac{\pi x}{2a}\right)$ は偶関数，$\phi_2(x) = \dfrac{1}{\sqrt{a}}\sin\left(\dfrac{\pi x}{a}\right)$ は奇関数であるため，被積分関数 $\phi_1(x)^3\phi_2(x)$ は奇関数です。したがって対称区間 $[-a, a]$ 上の積分は $0$ となります。

$$
I = 0
$$

よって，4つの状態すべてに対して1次の行列要素 $\langle \Psi_{1,\alpha} | V | \Psi_0 \rangle$ は $0$ になります。

さらに高次の摂動を含めた厳密な意味でも，両者はまったく混ざりません。2電子の座標を同時に反転させる空間反転演算子 $\mathcal{P}: (x_1, x_2) \mapsto (-x_1, -x_2)$ を考えると，井戸型ポテンシャルとデルタ関数 $\delta((-x_1) - (-x_2)) = \delta(x_1 - x_2)$ の双方が $\mathcal{P}$ のもとで不変なので，全ハミルトニアン $H_0 + V$ は $\mathcal{P}$ と可換です。$\Psi_0$ のパリティ固有値は $(+1)(+1) = +1$ であるのに対し，(4) の4状態はすべて $(+1)(-1) = -1$ のパリティ固有値をもつため，パリティの異なる状態間は摂動の何次まで考えても混合しません。

以上より，(3) の状態と (4) で考えた4つの状態は，いずれもまったく混ざりません。
