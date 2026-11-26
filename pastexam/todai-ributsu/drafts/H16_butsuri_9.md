---
title: 東大理物 平成16年度 物理学 第9問：1次元周期ポテンシャル障壁の転送行列とバンド構造
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
  - 物性物理
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成16年度
exam_subject: 物理学
exam_number: 第9問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成16年度 物理学 第9問：1次元周期ポテンシャル障壁の転送行列とバンド構造

## 問題

幅 $b$ を持つ矩形ポテンシャル障壁 $V(z)$ による一次元電子の散乱を考える。$V(z)$ の左（$z = -\infty$）から入射する電子の波動関数を $\psi_l$，右から入射する電子のそれを $\psi_r$ とすると，図1の様に $z < -b/2$ 及び $z > b/2$ で

$$
\psi_l(z) = \begin{cases}
\exp[ikz] + R\exp[-ikz] & (z < -b/2) \\
T\exp[ikz] & (z > b/2)
\end{cases} \tag{1}
$$

及び

$$
\psi_r(z) = \begin{cases}
T\exp[-ikz] & (z < -b/2) \\
\exp[-ikz] + R\exp[ikz] & (z > b/2)
\end{cases} \tag{2}
$$

と表される。ただし，$T, R$ はそれぞれ透過係数及び反射係数であり，$T = e^{i\alpha}\sin(\gamma)$，$R = i e^{i\alpha}\cos(\gamma)$ の様に位相差 $\alpha$ と散乱振幅に関係した量 $\gamma$ で表される。また，波数 $k$ は電子のエネルギー $E$ と質量 $m$ を用いて次のように書ける。

$$
k = \sqrt{2mE}/\hbar \tag{3}
$$

<figure class="problem-figure" markdown>
![矩形ポテンシャル障壁による電子の散乱](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-p1-light.svg#only-light)
![矩形ポテンシャル障壁による電子の散乱](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-p1-dark.svg#only-dark)
<figcaption markdown="span">図1：左から入射する波動関数 $\psi_l(z)$ と右から入射する波動関数 $\psi_r(z)$。</figcaption>
</figure>

(1) 波動関数の一般解 $\psi$ は

$$
\psi(z) = \begin{cases}
A_{-1}\exp[ikz] + B_{-1}\exp[-ikz] & (z < -b/2) \\
A_0\exp[ikz] + B_0\exp[-ikz] & (z > b/2)
\end{cases} \tag{4}
$$

の様に書ける（図2）。一般解が線形独立解 $\psi_r, \psi_l$ の重ね合わせで書ける事を利用して，$A_{-1}, B_{-1}$ と $A_0, B_0$ の関係式を導け。また，それを式 (5) の様に行列表示した時の，行列要素を $\alpha, \gamma$ で表せ。（$M$ は転送行列と呼ばれる。）

$$
\begin{pmatrix} A_0 \\ B_0 \end{pmatrix} = M \begin{pmatrix} A_{-1} \\ B_{-1} \end{pmatrix} \tag{5}
$$

<figure class="problem-figure" markdown>
![一般解の振幅](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-p2-light.svg#only-light)
![一般解の振幅](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-p2-dark.svg#only-dark)
<figcaption markdown="span">図2：単一障壁の両側における一般解 $\psi(z)$ の平面波振幅。</figcaption>
</figure>

<figure class="problem-figure" markdown>
![1次元周期ポテンシャル障壁](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-p3-light.svg#only-light)
![1次元周期ポテンシャル障壁](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-p3-dark.svg#only-dark)
<figcaption markdown="span">図3：間隔 $a$ で並んだ1次元周期ポテンシャル障壁と各自由領域の波動関数。</figcaption>
</figure>

次に $V(z)$ が間隔 $a(> b)$ で等間隔に並んでいる時（すなわち一次元周期系）の電子状態を考える。図3の様に波動関数 $\Psi$ は $na < z < (n+1)a$ かつポテンシャルがゼロになる領域で $A_n\exp[ikz] + B_n\exp[-ikz]$ と書ける。今，$-a + b/2 < z < a - b/2$ に注目し，$\Psi$ がこの領域で線形独立解 $\psi_r, \psi_l$ の重ね合わせで書ける事を利用すると，ここでも式 (5) が成り立つ事，また一般に以下の関係が成り立つ事がわかる。

$$
\begin{pmatrix} A_n \\ B_n \end{pmatrix} = M \begin{pmatrix} A_{n-1} \\ B_{n-1} \end{pmatrix} \tag{6}
$$

(2) 周期系の波動関数 $\Psi$ はブロッホ条件 $\Psi(z+a) = \exp[iqa]\Psi(z)$ を満たす事が知られている。この条件を用いて $A_n, B_n$ が満たすべき関係式を示せ。ただし，$q$ はブロッホ波数である。（波数 $k$ は式 (3) によって定義されるエネルギーの関数であり，ブロッホ波数 $q$ とは直接関係するものではない事に留意せよ。）

(3) ブロッホ条件と式 (6) が同時に成り立つ時，$q$ と $k$ は次の式で関係付けられる事を示せ。

$$
\cos(qa) = \frac{\cos(ka + \alpha)}{\sin(\gamma)} \tag{7}
$$

次に，$\alpha, \gamma$ が波数 $k$ を介して

$$
\gamma = \frac{\pi}{2}\frac{k}{k_c}, \qquad \alpha = -c\frac{k}{k_c} \tag{8}
$$

の様にエネルギーに依存している場合を考える。ただし，$k_c, c$ は定数であり，$\pi/2 < k_c a - c$ を満たす。以下，$0 < k < k_c$ で示されるエネルギー範囲で考えよ。

(4) 式 (7) の右辺の値を波数 $k$ の関数としてプロットせよ。

(5) $ka + \alpha$ が $\pi$ の整数倍の時，式 (7) を満たす実数の $q$ が存在しない事を示し，その物理的意味を述べよ。

(6) 実数の $q$ が存在するための $k$ の条件を $k_c, c, a$ を用いて示せ。

(7) $k_c a - c = 5\pi/2$ の場合，$q$ と $E$ の関係式（すなわち分散関係）の概略図を示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成16年度 物理学 第9問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，単一障壁の2つの散乱解 $\psi_l, \psi_r$ の線形結合として一般解を表し，障壁の左右の平面波振幅を結ぶ転送行列 $M$ を求めます。これに1次元周期系のブロッホ条件を組み合わせると，ゼロでない振幅が存在するための行列式条件から分散関係が得られます。

後半では，$\alpha$ と $\gamma$ がともに $k$ に比例することを利用して，$|\cos(qa)| \le 1$ という不等式を三角関数の角度の不等式として直接解き，許容される波数領域とエネルギーバンド構造を描きます。
</div>

### (1)

一般解 $\psi(z)$ を線形独立解 $\psi_l(z)$ と $\psi_r(z)$ の重ね合わせ $\psi(z) = c_l \psi_l(z) + c_r \psi_r(z)$ と表します。$z < -b/2$ および $z > b/2$ の各領域で式 (1) と式 (2) を代入して整理します。

$$
\psi(z) = \begin{cases}
c_l e^{ikz} + (R c_l + T c_r) e^{-ikz} & (z < -b/2) \\
(T c_l + R c_r) e^{ikz} + c_r e^{-ikz} & (z > b/2)
\end{cases}
$$

これを式 (4) と比較すると，各振幅は次の関係を満たします。

$$
A_{-1} = c_l, \qquad B_{-1} = R c_l + T c_r, \qquad A_0 = T c_l + R c_r, \qquad B_0 = c_r
$$

$c_l = A_{-1}$ と $c_r = B_0$ を $B_{-1} = R c_l + T c_r$ に代入して $B_0$ について解きます。

$$
B_0 = -\frac{R}{T}A_{-1} + \frac{1}{T}B_{-1}
$$

次にこれを $A_0 = T A_{-1} + R B_0$ に代入して整理します。

$$
\begin{aligned}
A_0 &= T A_{-1} + R\left(-\frac{R}{T}A_{-1} + \frac{1}{T}B_{-1}\right) \\
&= \frac{T^2 - R^2}{T}A_{-1} + \frac{R}{T}B_{-1}
\end{aligned}
$$

したがって，転送行列 $M$ は $T, R$ を用いて次式となります。

$$
M = \begin{pmatrix} \dfrac{T^2 - R^2}{T} & \dfrac{R}{T} \\[8pt] -\dfrac{R}{T} & \dfrac{1}{T} \end{pmatrix}
$$

ここに $T = e^{i\alpha}\sin\gamma$，$R = i e^{i\alpha}\cos\gamma$ を代入します。まず $T^2 - R^2$ を計算します。

$$
\begin{aligned}
T^2 - R^2 &= e^{2i\alpha}\sin^2\gamma - (i)^2 e^{2i\alpha}\cos^2\gamma \\
&= e^{2i\alpha}\bigl(\sin^2\gamma + \cos^2\gamma\bigr) \\
&= e^{2i\alpha}
\end{aligned}
$$

これを用いて各行列要素を $\alpha, \gamma$ で表します。

$$
\begin{aligned}
M_{11} &= \frac{e^{2i\alpha}}{e^{i\alpha}\sin\gamma} \\
&= \frac{e^{i\alpha}}{\sin\gamma}
\end{aligned}
$$

$$
\begin{aligned}
M_{12} &= \frac{i e^{i\alpha}\cos\gamma}{e^{i\alpha}\sin\gamma} \\
&= i\frac{\cos\gamma}{\sin\gamma}
\end{aligned}
$$

同様に $M_{21} = -i\dfrac{\cos\gamma}{\sin\gamma}$，$M_{22} = \dfrac{e^{-i\alpha}}{\sin\gamma}$ となります。

以上より，関係式および転送行列 $M$ は次式となります。

$$
\finalanswer{
A_0 = \frac{T^2 - R^2}{T}A_{-1} + \frac{R}{T}B_{-1}, \quad B_0 = -\frac{R}{T}A_{-1} + \frac{1}{T}B_{-1}, \qquad
M = \frac{1}{\sin\gamma}\begin{pmatrix} e^{i\alpha} & i\cos\gamma \\ -i\cos\gamma & e^{-i\alpha} \end{pmatrix}
}
$$

### (2)

$(n - 1)a + b/2 < z < na - b/2$ の自由領域にある点 $z$ をとると，$z + a$ は $na + b/2 < z + a < (n + 1)a - b/2$ の自由領域に属します。したがって，ブロッホ条件 $\Psi(z + a) = e^{iqa}\Psi(z)$ の両辺は次のように書くことができます。

$$
\begin{aligned}
\Psi(z + a) &= A_n e^{ik(z + a)} + B_n e^{-ik(z + a)} \\
&= \bigl(A_n e^{ika}\bigr) e^{ikz} + \bigl(B_n e^{-ika}\bigr) e^{-ikz}
\end{aligned}
$$

$$
\begin{aligned}
e^{iqa}\Psi(z) &= e^{iqa}\bigl(A_{n-1} e^{ikz} + B_{n-1} e^{-ikz}\bigr) \\
&= \bigl(e^{iqa} A_{n-1}\bigr) e^{ikz} + \bigl(e^{iqa} B_{n-1}\bigr) e^{-ikz}
\end{aligned}
$$

$e^{ikz}$ と $e^{-ikz}$ は線形独立なので，係数を比較します。

$$
A_n e^{ika} = e^{iqa} A_{n-1}, \qquad B_n e^{-ika} = e^{iqa} B_{n-1}
$$

両辺をそれぞれ $e^{ika}$，$e^{-ika}$ で割ると，求める関係式が得られます。

$$
\finalanswer{A_n = e^{i(q - k)a} A_{n-1}, \qquad B_n = e^{i(q + k)a} B_{n-1}}
$$

### (3)

設問 (2) で得たブロッホ条件を行列で書くと，次式になります。

$$
\begin{pmatrix} A_n \\ B_n \end{pmatrix} = \begin{pmatrix} e^{i(q - k)a} & 0 \\ 0 & e^{i(q + k)a} \end{pmatrix} \begin{pmatrix} A_{n-1} \\ B_{n-1} \end{pmatrix}
$$

これと式 (6) が同時に成り立つため，次の方程式が得られます。

$$
\left\{M - \begin{pmatrix} e^{i(q - k)a} & 0 \\ 0 & e^{i(q + k)a} \end{pmatrix}\right\} \begin{pmatrix} A_{n-1} \\ B_{n-1} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$(A_{n-1}, B_{n-1}) \neq (0, 0)$ なる解が存在するためには，左辺の係数行列の行列式 $D$ が $0$ である必要があります。設問 (1) の $M$ を代入して行列式 $D$ を計算します。

$$
\begin{aligned}
D &= \det\begin{pmatrix} \dfrac{e^{i\alpha}}{\sin\gamma} - e^{i(q - k)a} & i\dfrac{\cos\gamma}{\sin\gamma} \\[10pt] -i\dfrac{\cos\gamma}{\sin\gamma} & \dfrac{e^{-i\alpha}}{\sin\gamma} - e^{i(q + k)a} \end{pmatrix} \\
&= \left(\frac{e^{i\alpha}}{\sin\gamma} - e^{i(q - k)a}\right)\left(\frac{e^{-i\alpha}}{\sin\gamma} - e^{i(q + k)a}\right) - \frac{\cos^2\gamma}{\sin^2\gamma} \\
&= \frac{1 - \cos^2\gamma}{\sin^2\gamma} - \frac{e^{i(\alpha + qa + ka)} + e^{i(-\alpha + qa - ka)}}{\sin\gamma} + e^{2iqa} \\
&= 1 - \frac{e^{iqa}\bigl(e^{i(ka + \alpha)} + e^{-i(ka + \alpha)}\bigr)}{\sin\gamma} + e^{2iqa}
\end{aligned}
$$

$D = 0$ の両辺を $e^{iqa}$ で割ります。

$$
e^{-iqa} + e^{iqa} - \frac{e^{i(ka + \alpha)} + e^{-i(ka + \alpha)}}{\sin\gamma} = 0
$$

オイラーの公式を用いて余弦で表します。

$$
2\cos(qa) - \frac{2\cos(ka + \alpha)}{\sin\gamma} = 0
$$

移項して両辺を $2$ で割ると，式 (7) が成り立つことがわかります。

$$
\cos(qa) = \frac{\cos(ka + \alpha)}{\sin(\gamma)}
$$

### (4)

式 (8) を式 (7) の右辺に代入し，この関数を $f(k)$ とおきます。

$$
\begin{aligned}
f(k) &= \frac{\cos(ka + \alpha)}{\sin(\gamma)} \\
&= \frac{\cos\!\left((k_c a - c)\dfrac{k}{k_c}\right)}{\sin\!\left(\dfrac{\pi}{2}\dfrac{k}{k_c}\right)}
\end{aligned}
$$

区間 $0 < k < k_c$ において，分母 $\sin\!\left(\dfrac{\pi k}{2k_c}\right)$ は $0$ から $1$ へ単調に増加します。分子 $\cos\!\left((k_c a - c)\dfrac{k}{k_c}\right)$ は $k = 0$ で $1$ であり，$k$ の増加に伴って振動します。したがって $f(k)$ は次の性質をもちます。

- $k \to +0$ のとき，分子は $1$ に近づき分母は $\dfrac{\pi k}{2k_c} \to +0$ となるため，$f(k) \to +\infty$ と発散します。
- $k$ が増加すると，$f(k)$ は振幅 $\dfrac{1}{\sin(\pi k/(2k_c))} > 1$ の包絡線に挟まれながら正負に振動し，$k \to k_c$ に向かって包絡線は $\pm 1$ に近づきます。
- $k_c a - c > \dfrac{\pi}{2}$ より，$f(k)$ は区間 $(0, k_c)$ 内に少なくとも1つの零点をもちます。また $k = k_c$ では $f(k_c) = \cos(k_c a - c)$ となります。

代表例として設問 (7) の $k_c a - c = \dfrac{5\pi}{2}$ の場合のプロットを次の図に示します。横軸上の太線部分が $|f(k)| \le 1$ となる領域です。

<figure class="problem-figure" markdown>
![式(7)右辺の波数kに対するプロット](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-s1-light.svg#only-light)
![式(7)右辺の波数kに対するプロット](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-s1-dark.svg#only-dark)
<figcaption markdown="span">$k_c a - c = 5\pi/2$ における $f(k) = \cos(ka + \alpha)/\sin(\gamma)$ のグラフ。網掛けおよび横軸上の太線は $|f(k)| \le 1$ となる範囲。</figcaption>
</figure>

### (5)

$ka + \alpha = n\pi$（$n$ は整数）のとき，$\cos(n\pi) = \pm 1$ なので $|\cos(ka + \alpha)| = 1$ です。一方，$0 < k < k_c$ より $0 < \gamma < \dfrac{\pi}{2}$ なので，$0 < \sin(\gamma) < 1$ が成り立ちます。したがって，式 (7) の右辺の大きさは次式を満たします。

$$
\left|\frac{\cos(ka + \alpha)}{\sin(\gamma)}\right| = \frac{1}{\sin(\gamma)} > 1
$$

任意の実数 $q$ に対して $|\cos(qa)| \le 1$ であるため，式 (7) を満たす実数のブロッホ波数 $q$ は存在しません。

この物理的意味は次の通りです。$ka + \alpha = n\pi$ のとき，周期 $a$ で並んだ隣り合う障壁からの反射波の位相差である $ka + \alpha$ が $\pi$ の整数倍となり，反射波同士が強め合うブラッグ反射が起こります。その結果，周期系の中を定常的に伝播する進行波状態が存在できず，$q$ が複素数となって波動関数が指数関数的に減衰するエネルギーギャップである**禁制帯**が生じます。

### (6)

式 (7) を満たす実数 $q$ が存在するための必要十分条件は $|\cos(qa)| \le 1$，すなわち次式です。

$$
\left|\frac{\cos(ka + \alpha)}{\sin(\gamma)}\right| \le 1
$$

$0 < k < k_c$ では $\sin(\gamma) > 0$ なので，両辺に $\sin(\gamma)$ を掛けます。

$$
|\cos(ka + \alpha)| \le \sin(\gamma)
$$

ここで無次元変数 $u = \dfrac{k}{k_c}$（$0 < u < 1$）および定数 $\beta = k_c a - c > \dfrac{\pi}{2}$ を導入します。$ka + \alpha = \beta u$ であり，$\sin(\gamma)$ は余弦に書き換えることができます。

$$
\begin{aligned}
\sin(\gamma) &= \sin\!\left(\frac{\pi}{2}u\right) \\
&= \cos\!\left(\frac{\pi}{2}(1 - u)\right)
\end{aligned}
$$

したがって不等式は次の形になります。

$$
|\cos(\beta u)| \le \cos\!\left(\frac{\pi}{2}(1 - u)\right)
$$

$\theta_0 = \dfrac{\pi}{2}(1 - u)$ は $0 < \theta_0 < \dfrac{\pi}{2}$ を満たすため，不等式 $|\cos(\beta u)| \le \cos\theta_0$ が成り立つための条件は，ある自然数 $n = 1, 2, \dots$ に対して次式が成り立つことです。

$$
(n - 1)\pi + \frac{\pi}{2}(1 - u) \le \beta u \le n\pi - \frac{\pi}{2}(1 - u)
$$

左側の不等式を $u$ について整理します。

$$
\left(\beta + \frac{\pi}{2}\right)u \ge \left(n - \frac{1}{2}\right)\pi
$$

両辺に $2$ を掛けて $2\beta + \pi > 0$ で割ります。

$$
u \ge \frac{(2n - 1)\pi}{2\beta + \pi}
$$

同様に右側の不等式を整理します。

$$
\left(\beta - \frac{\pi}{2}\right)u \le \left(n - \frac{1}{2}\right)\pi
$$

仮定より $\beta = k_c a - c > \dfrac{\pi}{2}$ なので $2\beta - \pi > 0$ であり，両辺をこれで割ることができます。

$$
u \le \frac{(2n - 1)\pi}{2\beta - \pi}
$$

$u = \dfrac{k}{k_c}$ と $\beta = k_c a - c$ を戻し，範囲 $0 < k < k_c$ と合わせます。下限が $k_c$ 未満となる条件は $(2n - 1)\pi < 2(k_c a - c) + \pi$ すなわち $(n - 1)\pi < k_c a - c$ です。したがって，求める $k$ の条件は，$(n - 1)\pi < k_c a - c$ を満たす自然数 $n$ を用いて次式となります。ただし，右辺の上限が $k_c$ 以上となる最大の $n$ については $k < k_c$ の範囲に限ります。

$$
\finalanswer{\frac{(2n - 1)\pi k_c}{2(k_c a - c) + \pi} \le k \le \frac{(2n - 1)\pi k_c}{2(k_c a - c) - \pi}}
$$

### (7)

$k_c a - c = \dfrac{5\pi}{2}$ を設問 (6) の条件に代入します。$2(k_c a - c) + \pi = 6\pi$，$2(k_c a - c) - \pi = 4\pi$ であり，$(n - 1)\pi < \dfrac{5\pi}{2}$ を満たす自然数は $n = 1, 2, 3$ です。$E_c = \dfrac{\hbar^2 k_c^2}{2m}$ とおき，式 (3) より $E = \left(\dfrac{k}{k_c}\right)^2 E_c$ であることから，各バンドの波数 $k$，エネルギー $E$，および第1ブリルアンゾーン $-\dfrac{\pi}{a} \le q \le \dfrac{\pi}{a}$ におけるブロッホ波数 $q$ の対応を求めます。

$n = 1$ の第1バンドでは $\dfrac{1}{6}k_c \le k \le \dfrac{1}{4}k_c$ であり，エネルギー範囲は $\dfrac{1}{36}E_c \le E \le \dfrac{1}{16}E_c$ です。$k = \dfrac{1}{6}k_c$ で $\cos(qa) = 1$（$q = 0$），$k = \dfrac{1}{4}k_c$ で $\cos(qa) = -1$（$q = \pm\dfrac{\pi}{a}$）となり，$E$ は $|q|$ とともに単調増加します。

$n = 2$ の第2バンドでは $\dfrac{1}{2}k_c \le k \le \dfrac{3}{4}k_c$ であり，エネルギー範囲は $\dfrac{1}{4}E_c \le E \le \dfrac{9}{16}E_c$ です。$k = \dfrac{1}{2}k_c$ で $\cos(qa) = -1$（$q = \pm\dfrac{\pi}{a}$），$k = \dfrac{3}{4}k_c$ で $\cos(qa) = 1$（$q = 0$）となり，$E$ は $|q|$ の増加とともに単調減少します。

$n = 3$ の第3バンドでは $\dfrac{5}{6}k_c \le k < k_c$ であり，エネルギー範囲は $\dfrac{25}{36}E_c \le E < E_c$ です。$k = \dfrac{5}{6}k_c$ で $\cos(qa) = 1$（$q = 0$），$k \to k_c$ で $\cos(qa) \to 0$（$q \to \pm\dfrac{\pi}{2a}$）となり，$E$ は $|q|$ とともに単調増加します。

また，各バンド端 $q = 0, \pm\dfrac{\pi}{a}$ では $\sin(qa) = 0$ となるため，$\dfrac{\mathrm{d}E}{\mathrm{d}q} = 0$ で水平に接します。以上を還元ゾーン表示で描いた分散関係の概略図を次に示します。

<figure class="problem-figure" markdown>
![分散関係E(q)の概略図](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-s2-light.svg#only-light)
![分散関係E(q)の概略図](../../../docs/assets/figures/pastexam-todai-ributsu/H16_butsuri_9-s2-dark.svg#only-dark)
<figcaption markdown="span">$k_c a - c = 5\pi/2$ における還元ゾーン表示の分散関係 $E(q)$（$E_c = \hbar^2 k_c^2/(2m)$）。</figcaption>
</figure>
