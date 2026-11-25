---
title: 東大理物 平成18年度 物理学 第1問：1次元無限井戸型ポテンシャルの摂動論とパリティ
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成18年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成18年度 物理学 第1問：1次元無限井戸型ポテンシャルの摂動論とパリティ

## 問題

1次元系で無限に高い2つの壁にはさまれた領域を考える。1次元の座標を $x$ で表すこととし，壁の位置は $x = -a$，及び，$x = a$ とする（$a > 0$）。そこに質量 $m$ の粒子がある。二つの壁の間の領域でのポテンシャルエネルギーを $U(x)$ と表わす。以下の設問に答えよ。ただし，$\hbar = h/(2\pi)$（$h$ はプランク定数）とする。

(1) この粒子の従う，時間に依存しないシュレーディンガー方程式を示せ。ただし，基底状態から見て第 $n$ 励起状態のエネルギー固有値を $E_n$ とせよ。また，$n = 0$ は基底状態を表わすとせよ。次に，このシュレーディンガー方程式を解く際の境界条件を述べよ。さらに，

$$
U(x) = 0, \qquad -a < x < a \tag{1}
$$

の場合（図1参照）について，エネルギー固有値 $E_n$（$n = 0, 1, 2, \dots$）を，解を得る概略とともに示せ。固有波動関数 $\phi_n(x)$ を，$n = 0, 1$ の場合について，具体的に示せ。

<figure class="problem-figure" markdown>
![無摂動の無限井戸型ポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H18_butsuri_1-p1-light.svg#only-light)
![無摂動の無限井戸型ポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H18_butsuri_1-p1-dark.svg#only-dark)
<figcaption markdown="span">図1：ポテンシャル（設問1）。</figcaption>
</figure>

(2) 設問1の各固有関数 $\phi_n(x)$ は，座標系の $x \to -x$ なる変換によってどのように変化するか述べよ。波動関数のそのような性質は，ハミルトニアンのどの不変性の帰結として起こるのか説明せよ。

(3) ポテンシャル $U(x)$ をゼロからわずかにずらす事にする。まず，図2のように，

$$
\begin{aligned}
U(x) &= 0, & -a &< x \le 0 \tag{2} \\
U(x) &= -w, & 0 &< x < a \tag{3}
\end{aligned}
$$

とする。$w$ は正の実数であるが，絶対値は十分小さいものとする。この時の，$n = 0$ の状態と $n = 1$ の状態のエネルギー固有値をそれぞれ1次の摂動論で求めよ。

<figure class="problem-figure" markdown>
![階段状の摂動を加えたポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H18_butsuri_1-p2-light.svg#only-light)
![階段状の摂動を加えたポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H18_butsuri_1-p2-dark.svg#only-dark)
<figcaption markdown="span">図2：ポテンシャル（設問3）。</figcaption>
</figure>

(4) 設問3の場合，設問1に比べてポテンシャルがわずかに変わっている。ここで，$n = 0$ の状態の波動関数を $\psi_0(x)$ とすると，$\psi_0(x)$ を設問1の $\phi_n(x)$（$n = 0, 1, 2, \dots$）で展開した時の $\phi_0(x)$ と $\phi_1(x)$ の確率振幅を，$w$ に関して1次の項まで求めよ。

(5) 設問1の波動関数 $\phi_0(x)$ に対して座標 $x$ の期待値 $\langle x \rangle$ がどのようになるか，簡単な説明とともに示せ。それは，設問2とはどのような関係にあるか述べよ。

(6) 設問4の波動関数 $\psi_0(x)$ を $\phi_0(x)$ と $\phi_1(x)$ までで展開したものに対して，期待値 $\langle x \rangle$ を $w$ の1次まで示せ。それはポテンシャルの変化と関連づけて，どのように解釈できるか述べよ。

(7) 十分小さい正の実数 $u$ に対して，次のポテンシャルを考える（図3）。

$$
U(x) = -ux/a, \qquad -a < x < a \tag{4}
$$

この時の，$n = 0$ の状態と $n = 1$ の状態のエネルギー固有値はそれぞれどのようになるか，$u$ に関して1次までの効果を述べよ。

<figure class="problem-figure" markdown>
![線形に傾いたポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H18_butsuri_1-p3-light.svg#only-light)
![線形に傾いたポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H18_butsuri_1-p3-dark.svg#only-dark)
<figcaption markdown="span">図3：ポテンシャル（設問7）。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成18年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
無限に高い壁が原点について左右対称な位置にあるため，無摂動の固有関数は偶関数と奇関数に交互に分かれます。この対称性を使うと，確率密度 $|\phi_n(x)|^2$ が常に偶関数になるため，奇関数や左右半分の領域での積分を簡単に見通すことができます。

ポテンシャルのずれが小さいときは，縮退のない定常摂動論を用います。1次のエネルギー補正は無摂動状態での摂動の期待値で与えられ，1次の波動関数補正は他の固有状態との行列要素をエネルギー差で割った和として計算することができます。
</div>

### (1)

領域 $-a < x < a$ において，時間に依存しないシュレーディンガー方程式は次式になります。

$$
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\phi_n(x)}{\mathrm{d}x^2} + U(x)\phi_n(x) = E_n\phi_n(x)
$$

壁の外側 $|x| \ge a$ ではポテンシャルが無限大なので粒子は存在できず，$\phi_n(x) = 0$ です。波動関数の連続性より，境界条件は次式になります。

$$
\phi_n(-a) = 0, \qquad \phi_n(a) = 0
$$

$U(x) = 0$ のとき，方程式は $\dfrac{\mathrm{d}^2\phi_n}{\mathrm{d}x^2} + k_n^2\phi_n = 0$ となります。ここで $k_n = \dfrac{\sqrt{2mE_n}}{\hbar} > 0$ とおきました。この一般解は定数 $A, B$ を用いて

$$
\phi_n(x) = A\cos(k_n x) + B\sin(k_n x)
$$

です。境界条件 $\phi_n(\pm a) = 0$ を代入します。

$$
\begin{aligned}
A\cos(k_n a) + B\sin(k_n a) &= 0 \\
A\cos(k_n a) - B\sin(k_n a) &= 0
\end{aligned}
$$

2式の和と差をとると，$A\cos(k_n a) = 0$ と $B\sin(k_n a) = 0$ が得られます。恒等的に $0$ でない解が存在するのは，$B = 0$ かつ $\cos(k_n a) = 0$ の場合と，$A = 0$ かつ $\sin(k_n a) = 0$ の場合の2通りです。

前者は $k_n a = \dfrac{\pi}{2}, \dfrac{3\pi}{2}, \dfrac{5\pi}{2}, \dots$ を与え，後者は $k_n a = \pi, 2\pi, 3\pi, \dots$ を与えます。これらを小さい順にまとめて $n = 0, 1, 2, \dots$ で番号を付けると，波数は $k_n = \dfrac{(n + 1)\pi}{2a}$ となります。これよりエネルギー固有値 $E_n$ は次式になります。

$$
\begin{aligned}
E_n &= \frac{\hbar^2 k_n^2}{2m} \\
&= \frac{\hbar^2 \pi^2 (n + 1)^2}{8ma^2} \qquad (n = 0, 1, 2, \dots)
\end{aligned}
$$

次に $n = 0$ と $n = 1$ の固有波動関数を規格化します。$n = 0$ では $k_0 = \dfrac{\pi}{2a}$ の偶関数 $\phi_0(x) = A\cos\!\left(\dfrac{\pi x}{2a}\right)$ です。

$$
\begin{aligned}
1 &= \int_{-a}^{a} |A|^2 \cos^2\!\left(\frac{\pi x}{2a}\right)\mathrm{d}x \\
&= |A|^2 \int_{-a}^{a} \frac{1 + \cos(\pi x / a)}{2}\,\mathrm{d}x \\
&= |A|^2 a
\end{aligned}
$$

正の定数として $A = \dfrac{1}{\sqrt{a}}$ をとります。同様に $n = 1$ では $k_1 = \dfrac{\pi}{a}$ の奇関数 $\phi_1(x) = B\sin\!\left(\dfrac{\pi x}{a}\right)$ であり，$\int_{-a}^{a}\sin^2\!\left(\dfrac{\pi x}{a}\right)\mathrm{d}x = a$ なので $B = \dfrac{1}{\sqrt{a}}$ です。

したがって，エネルギー固有値と $n = 0, 1$ の固有波動関数は次式となります。

$$
\finalanswer{E_n = \frac{\hbar^2 \pi^2 (n + 1)^2}{8ma^2} \ (n = 0, 1, 2, \dots), \quad \phi_0(x) = \frac{1}{\sqrt{a}}\cos\!\left(\frac{\pi x}{2a}\right), \quad \phi_1(x) = \frac{1}{\sqrt{a}}\sin\!\left(\frac{\pi x}{a}\right)}
$$

### (2)

設問1で求めた固有関数 $\phi_n(x)$ は，$n$ が偶数のとき $\phi_n(x) = \dfrac{1}{\sqrt{a}}\cos\!\left(\dfrac{(n + 1)\pi x}{2a}\right)$，$n$ が奇数のとき $\phi_n(x) = \dfrac{1}{\sqrt{a}}\sin\!\left(\dfrac{(n + 1)\pi x}{2a}\right)$ です。したがって，$x \to -x$ の変換に対して次のように変化します。

$$
\phi_n(-x) = (-1)^n \phi_n(x)
$$

すなわち，$n$ が偶数のときは偶関数であり変化せず，$n$ が奇数のときは奇関数であり符号が反転します。

この性質は，ハミルトニアン $\mathcal{H} = -\dfrac{\hbar^2}{2m}\dfrac{\mathrm{d}^2}{\mathrm{d}x^2} + U(x)$ が空間反転 $x \to -x$ に対して不変であることの帰結です。空間反転を行うパリティ演算子 $\mathcal{P}$ はハミルトニアン $\mathcal{H}$ と可換であり，1次元束縛状態のエネルギー固有値には縮退がないため，すべてのエネルギー固有状態は必ずパリティの固有状態になり，固有値 $+1$ の偶関数か固有値 $-1$ の奇関数のどちらかになります。

### (3)

式 (2) と式 (3) で与えられるポテンシャルを摂動ハミルトニアン $H' = U(x)$ とみなします。縮退のない1次の摂動論より，エネルギー固有値の1次補正は $E_n^{(1)} = \langle\phi_n|H'|\phi_n\rangle$ です。

設問2より $\phi_n(-x) = (-1)^n\phi_n(x)$ なので，確率密度 $|\phi_n(x)|^2$ は偶関数です。よって $0 < x < a$ での積分は全領域 $-a < x < a$ での積分のちょうど半分になります。

$$
\begin{aligned}
E_n^{(1)} &= \int_{-a}^{a} |\phi_n(x)|^2 U(x)\,\mathrm{d}x \\
&= -w\int_{0}^{a} |\phi_n(x)|^2\,\mathrm{d}x \\
&= -\frac{w}{2}\int_{-a}^{a} |\phi_n(x)|^2\,\mathrm{d}x \\
&= -\frac{w}{2}
\end{aligned}
$$

これは $n = 0$ でも $n = 1$ でも同じ値 $-\dfrac{w}{2}$ です。無摂動の固有値 $E_0^{(0)} = \dfrac{\hbar^2\pi^2}{8ma^2}$，$E_1^{(0)} = \dfrac{\hbar^2\pi^2}{2ma^2}$ に加えると，$w$ の1次までのエネルギー固有値は次式となります。

$$
\finalanswer{E_0 = \frac{\hbar^2 \pi^2}{8ma^2} - \frac{w}{2}, \qquad E_1 = \frac{\hbar^2 \pi^2}{2ma^2} - \frac{w}{2}}
$$

### (4)

縮退のない定常摂動論により，基底状態 $\psi_0(x)$ を無摂動の固有関数 $\phi_n(x)$ で展開すると，$w$ の1次まで次式になります。

$$
\psi_0(x) = \phi_0(x) + \sum_{n=1}^{\infty} \frac{\langle\phi_n|H'|\phi_0\rangle}{E_0^{(0)} - E_n^{(0)}}\phi_n(x)
$$

規格化による $\phi_0(x)$ の係数の補正は $w^2$ の次数から現れるため，$w$ の1次までで $\phi_0(x)$ の確率振幅は $c_0 = 1$ です。

次に $\phi_1(x)$ の確率振幅 $c_1 = \dfrac{\langle\phi_1|H'|\phi_0\rangle}{E_0^{(0)} - E_1^{(0)}}$ を求めます。まず行列要素 $\langle\phi_1|H'|\phi_0\rangle$ を計算します。$\theta = \dfrac{\pi x}{a}$ と置換すると $\mathrm{d}x = \dfrac{a}{\pi}\,\mathrm{d}\theta$ です。

$$
\begin{aligned}
\langle\phi_1|H'|\phi_0\rangle &= \int_{0}^{a} \frac{1}{\sqrt{a}}\sin\!\left(\frac{\pi x}{a}\right)(-w)\frac{1}{\sqrt{a}}\cos\!\left(\frac{\pi x}{2a}\right)\mathrm{d}x \\
&= -\frac{w}{a}\cdot\frac{a}{\pi}\int_{0}^{\pi} \sin\theta\cos\frac{\theta}{2}\,\mathrm{d}\theta \\
&= -\frac{w}{2\pi}\int_{0}^{\pi}\left(\sin\frac{3\theta}{2} + \sin\frac{\theta}{2}\right)\mathrm{d}\theta \\
&= -\frac{w}{2\pi}\left[-\frac{2}{3}\cos\frac{3\theta}{2} - 2\cos\frac{\theta}{2}\right]_{0}^{\pi} \\
&= -\frac{w}{2\pi}\left(0 - \left(-\frac{2}{3} - 2\right)\right) \\
&= -\frac{4w}{3\pi}
\end{aligned}
$$

エネルギー差は次式になります。

$$
\begin{aligned}
E_0^{(0)} - E_1^{(0)} &= \frac{\hbar^2\pi^2}{8ma^2} - \frac{4\hbar^2\pi^2}{8ma^2} \\
&= -\frac{3\hbar^2\pi^2}{8ma^2}
\end{aligned}
$$

これらを $c_1$ に代入します。

$$
\begin{aligned}
c_1 &= \frac{-\dfrac{4w}{3\pi}}{-\dfrac{3\hbar^2\pi^2}{8ma^2}} \\
&= \frac{32\,ma^2 w}{9\pi^3\hbar^2}
\end{aligned}
$$

したがって，$\phi_0(x)$ と $\phi_1(x)$ の確率振幅は $w$ の1次まで次式となります。

$$
\finalanswer{c_0 = 1, \qquad c_1 = \frac{32\,ma^2 w}{9\pi^3\hbar^2}}
$$

### (5)

波動関数 $\phi_0(x)$ に対する座標 $x$ の期待値 $\langle x \rangle$ は次式です。

$$
\langle x \rangle = \int_{-a}^{a} x|\phi_0(x)|^2\,\mathrm{d}x
$$

設問2より $\phi_0(-x) = \phi_0(x)$ なので $|\phi_0(x)|^2$ は偶関数です。したがって被積分関数 $x|\phi_0(x)|^2$ は奇関数となり，原点に関して対称な区間 $[-a, a]$ で積分すると $0$ になります。

$$
\finalanswer{\langle x \rangle = 0}
$$

これは設問2で示したハミルトニアンの空間反転不変性の帰結です。系が $x \to -x$ で不変なため，粒子の存在確率密度 $|\phi_0(x)|^2$ も左右対称になり，位置の平均値がちょうど中心の $0$ になります。

### (6)

$\psi_0(x) = \phi_0(x) + c_1\phi_1(x)$ に対して $\langle x \rangle$ を計算します。$c_1$ は実数であり $w$ の1次なので，$c_1^2$ の項は $w^2$ となり無視することができます。また設問5より $\langle\phi_0|x|\phi_0\rangle = 0$ です。

$$
\begin{aligned}
\langle x \rangle &= \langle\phi_0|x|\phi_0\rangle + c_1\langle\phi_0|x|\phi_1\rangle + c_1\langle\phi_1|x|\phi_0\rangle + O(w^2) \\
&= 2c_1\langle\phi_0|x|\phi_1\rangle + O(w^2)
\end{aligned}
$$

行列要素 $\langle\phi_0|x|\phi_1\rangle$ を計算します。被積分関数 $x\phi_0(x)\phi_1(x)$ は偶関数なので，$0$ から $a$ までの積分の2倍になります。$\theta = \dfrac{\pi x}{a}$ と置換すると $x = \dfrac{a}{\pi}\theta$，$\mathrm{d}x = \dfrac{a}{\pi}\,\mathrm{d}\theta$ です。

$$
\begin{aligned}
\langle\phi_0|x|\phi_1\rangle &= \frac{2}{a}\int_{0}^{a} x\cos\!\left(\frac{\pi x}{2a}\right)\sin\!\left(\frac{\pi x}{a}\right)\mathrm{d}x \\
&= \frac{2a}{\pi^2}\int_{0}^{\pi} \theta\cdot\frac{1}{2}\left(\sin\frac{3\theta}{2} + \sin\frac{\theta}{2}\right)\mathrm{d}\theta \\
&= \frac{a}{\pi^2}\left(\int_{0}^{\pi} \theta\sin\frac{3\theta}{2}\,\mathrm{d}\theta + \int_{0}^{\pi} \theta\sin\frac{\theta}{2}\,\mathrm{d}\theta\right)
\end{aligned}
$$

$k = \dfrac{3}{2}, \dfrac{1}{2}$ に対して $\cos(k\pi) = 0$ なので，部分積分は次のようになります。

$$
\begin{aligned}
\int_{0}^{\pi} \theta\sin(k\theta)\,\mathrm{d}\theta &= \left[-\frac{\theta\cos(k\theta)}{k}\right]_{0}^{\pi} + \frac{1}{k}\int_{0}^{\pi}\cos(k\theta)\,\mathrm{d}\theta \\
&= 0 + \left[\frac{\sin(k\theta)}{k^2}\right]_{0}^{\pi} \\
&= \frac{\sin(k\pi)}{k^2}
\end{aligned}
$$

これを用いて $\langle\phi_0|x|\phi_1\rangle$ を計算します。

$$
\begin{aligned}
\langle\phi_0|x|\phi_1\rangle &= \frac{a}{\pi^2}\left(\frac{\sin(3\pi/2)}{(3/2)^2} + \frac{\sin(\pi/2)}{(1/2)^2}\right) \\
&= \frac{a}{\pi^2}\left(-\frac{4}{9} + 4\right) \\
&= \frac{32a}{9\pi^2}
\end{aligned}
$$

設問4で求めた $c_1 = \dfrac{32\,ma^2 w}{9\pi^3\hbar^2}$ を代入します。

$$
\begin{aligned}
\langle x \rangle &= 2\cdot\frac{32\,ma^2 w}{9\pi^3\hbar^2}\cdot\frac{32a}{9\pi^2} \\
&= \frac{2048\,ma^3 w}{81\pi^5\hbar^2}
\end{aligned}
$$

したがって，$w$ の1次までの期待値 $\langle x \rangle$ は次式となります。

$$
\finalanswer{\langle x \rangle = \frac{2048\,ma^3 w}{81\pi^5\hbar^2}}
$$

$w > 0$ なので $\langle x \rangle > 0$ です。$0 < x < a$ の領域でポテンシャルエネルギーが $-w$ だけ低くなったため，粒子はより低いポテンシャルの領域である $x > 0$ 側に見出されやすくなり，位置の期待値が正の側へずれます。

### (7)

式 (4) のポテンシャル $H' = U(x) = -\dfrac{ux}{a}$ に対する1次の摂動エネルギー $E_n^{(1)}$ を求めます。

$$
E_n^{(1)} = \int_{-a}^{a} \left(-\frac{ux}{a}\right)|\phi_n(x)|^2\,\mathrm{d}x
$$

設問2より $|\phi_0(x)|^2$ と $|\phi_1(x)|^2$ はともに偶関数であり，$U(x) = -\dfrac{ux}{a}$ は奇関数です。よって被積分関数 $-\dfrac{ux}{a}|\phi_n(x)|^2$ は奇関数となり，区間 $[-a, a]$ での積分は $0$ になります。

$$
E_0^{(1)} = 0, \qquad E_1^{(1)} = 0
$$

したがって，$u$ に関して1次までの範囲では $n = 0$ と $n = 1$ のエネルギー固有値はいずれも変化せず，無摂動の値のままとなります。

$$
\finalanswer{E_0 = \frac{\hbar^2 \pi^2}{8ma^2}, \qquad E_1 = \frac{\hbar^2 \pi^2}{2ma^2}}
$$
