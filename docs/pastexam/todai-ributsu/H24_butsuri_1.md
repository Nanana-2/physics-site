---
title: 東大理物 平成24年度 物理学 第1問：磁場中および回転磁場中の電子スピンの運動
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成24年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成24年度 物理学 第1問：磁場中および回転磁場中の電子スピンの運動

## 問題

磁場中での電子スピンの量子力学的運動について，以下の設問に答えよ。ここでは，ハミルトニアンとして磁場 $\boldsymbol{H}$ とスピン $\boldsymbol{S}$ の Zeeman 相互作用

$$
\mathcal{H} = -\mu \boldsymbol{H} \cdot \boldsymbol{S} \tag{1}
$$

を考える。ただし，$\mu$ はある定数である。

(1) スピン $\boldsymbol{S} = (S_x, S_y, S_z)$ の各成分は，軌道角運動量と同じ交換関係を満たす。位置 $\boldsymbol{r} = (x, y, z)$ と運動量 $\boldsymbol{p} = (p_x, p_y, p_z)$ の各成分間の交換関係 $[x, p_x] = i\hbar$ などを用いて，軌道角運動量 $\boldsymbol{L} = \boldsymbol{r} \times \boldsymbol{p}$ の成分 $(L_x, L_y, L_z)$ の間の交換関係を求めよ。ただし，$\hbar = (\text{Planck 定数}) / (2\pi)$ である。

(2) 電子スピンの大きさは $1/2$ であるので，スピンの各成分を表わす演算子は $2 \times 2$ の行列で表現できる。ここで

$$
S_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad S_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

とするとき，$S_y$ を表す行列を求めよ。

ハミルトニアン (1) において，磁場 $\boldsymbol{H}$ の方向は $x$ 軸に平行で $\boldsymbol{H} = (H, 0, 0)$ の場合を考える。以下の設問 3〜6 では $\hbar = 1$ とする。
{: .problem-lead }

(3) ハミルトニアン (1) を行列表示し，その固有値 $\lambda_j$ と固有ベクトル $|\lambda_j\rangle$，（$j = 1, 2$）を求めよ。（磁場の方向が $x$ 軸に平行であることに注意）

(4) ハミルトニアン (1) で表される系の時刻 $t$ での状態ベクトルを $|\phi(t)\rangle$ とし，その時間発展を調べる。初期状態として，$t = 0$ でスピンが $z$ 方向を向いていたとする。つまり，この状態でのスピンの各成分の期待値は

$$
\langle\phi(0)|S_x|\phi(0)\rangle = \langle\phi(0)|S_y|\phi(0)\rangle = 0, \qquad \langle\phi(0)|S_z|\phi(0)\rangle = \frac{1}{2}
$$

である。その後の状態ベクトル $|\phi(t)\rangle$ を $t$ の関数として求めよ。また，時刻 $t$ でのスピンの期待値 $\bigl(\langle\phi(t)|S_x|\phi(t)\rangle, \langle\phi(t)|S_y|\phi(t)\rangle, \langle\phi(t)|S_z|\phi(t)\rangle\bigr)$ を求めよ。

次に，ハミルトニアン (1) において，磁場が回転磁場 $\boldsymbol{H} = (H_0 \cos\omega t, -H_0 \sin\omega t, H)$ で与えられる場合を考える。以下では，$a \equiv \mu H$，$a_0 \equiv \mu H_0$ とおく。

(5) ハミルトニアン (1) を

$$
\mathcal{H} = \mathcal{H}_1 + \mathcal{H}_2, \qquad \mathcal{H}_1 = -a S_z, \qquad \mathcal{H}_2 = -a_0(S_x \cos\omega t - S_y \sin\omega t)
$$

と 2 つの部分に分けて考える。$\mathcal{H}_1$ による運動を取り込んだ相互作用表示での状態ベクトル $|\psi(t)\rangle = e^{i\mathcal{H}_1 t}|\varphi(t)\rangle$ の時間発展を与える方程式を記せ。ただし，$|\varphi(t)\rangle$ は，Schrödinger 表示での状態ベクトルである。

(6) 特に，$\omega = a$ の場合を考える。初期状態として $t = 0$ でスピンが $z$ 方向を向いていた場合，その後のスピンの $z$ 成分の期待値 $\langle\varphi(t)|S_z|\varphi(t)\rangle$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成24年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
スピンの演算子は2行2列の行列なので，静磁場の中の時間発展は，初期状態をハミルトニアンの固有ベクトルで展開し，それぞれに位相因子を掛けて求めます。

回転する磁場が加わると，ハミルトニアンは時間によります。そこで，$\mathcal{H}_1 = -a S_z$ を使ったユニタリー変換で，$z$ 軸のまわりに角速度 $a$ で回る表示に変えます。共鳴条件 $\omega = a$ のもとでは，この表示の回る角速度と磁場の角速度が等しくなります。そのため，この表示のハミルトニアンは時間によらなくなり，静磁場のときと同じ方法で解くことができます。
</div>

### (1)
軌道角運動量の各成分は $L_x = y p_z - z p_y$，$L_y = z p_x - x p_z$，$L_z = x p_y - y p_x$ です。交換関係 

$$
\begin{aligned}
[x, p_x] &= [y, p_y] \\
&= [z, p_z] \\
&= i\hbar
\end{aligned}
$$

 と異なる成分同士の可換性を用いて $[L_x, L_y]$ を計算します。

$$
\begin{aligned}
[L_x, L_y] &= [y p_z - z p_y,\; z p_x - x p_z] \\
&= [y p_z, z p_x] - [y p_z, x p_z] - [z p_y, z p_x] + [z p_y, x p_z] \\
&= y[p_z, z]p_x + x[z, p_z]p_y \\
&= y(-i\hbar)p_x + x(i\hbar)p_y \\
&= i\hbar(x p_y - y p_x) \\
&= i\hbar L_z
\end{aligned}
$$

$x \to y \to z \to x$ の巡回置換によって，残りの交換関係も同様に得られます。

$$
\finalanswer{[L_x, L_y] = i\hbar L_z, \qquad [L_y, L_z] = i\hbar L_x, \qquad [L_z, L_x] = i\hbar L_y}
$$

### (2)
設問1よりスピン演算子は $[S_z, S_x] = i\hbar S_y$ を満たすので，$S_y = \dfrac{1}{i\hbar}[S_z, S_x]$ として計算します。

$$
\begin{aligned}
[S_z, S_x] &= \frac{\hbar^2}{4}\left[\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\right] \\
&= \frac{\hbar^2}{4}\left[\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} - \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\right] \\
&= \frac{\hbar^2}{2}\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
\end{aligned}
$$

両辺を $i\hbar$ で割ると $S_y$ が求まります。

$$
\begin{aligned}
S_y &= \frac{1}{i\hbar}\cdot\frac{\hbar^2}{2}\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \\
&= \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\end{aligned}
$$

$$
\finalanswer{S_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}}
$$

### (3)
$\hbar = 1$，$\boldsymbol{H} = (H, 0, 0)$ のとき，ハミルトニアン (1) の行列表示は次式になります。

$$
\begin{aligned}
\mathcal{H} &= -\mu H S_x \\
&= -\frac{\mu H}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
\end{aligned}
$$

固有方程式を解いて固有値 $\lambda_j$ を求めます。

$$
\begin{aligned}
\det(\mathcal{H} - \lambda I) &= \lambda^2 - \left(\frac{\mu H}{2}\right)^2 \\
&= 0 \\
\lambda_1 &= -\frac{\mu H}{2} \\
\lambda_2 &= \frac{\mu H}{2}
\end{aligned}
$$

それぞれの固有値に対する規格化された固有ベクトル $|\lambda_j\rangle$ を求めます。

$\mu H\ne0$ とします。$\lambda_1=-\mu H/2$ の固有方程式から，

$$
\begin{aligned}
c_1-c_2&=0\\
\begin{pmatrix}c_1\\c_2\end{pmatrix}&=c_1\begin{pmatrix}1\\1\end{pmatrix}
\end{aligned}
$$

です。$2|c_1|^2=1$ なので，$c_1=1/\sqrt2$ を選びます。

$\lambda_2=\mu H/2$ の固有方程式から，

$$
\begin{aligned}
c_1+c_2&=0\\
\begin{pmatrix}c_1\\c_2\end{pmatrix}&=c_1\begin{pmatrix}1\\-1\end{pmatrix}
\end{aligned}
$$

です。同じ規格化で $c_1=1/\sqrt2$ を選びます。$\mu H=0$ ではハミルトニアンが零行列になり，任意の0でないベクトルが固有ベクトルです。その場合も，ここで選んだ2本を直交基底として使うことができます。

$$
\finalanswer{\mathcal{H} = -\frac{\mu H}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \lambda_1 = -\frac{\mu H}{2},\; |\lambda_1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad \lambda_2 = \frac{\mu H}{2},\; |\lambda_2\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}}
$$

### (4)
$t = 0$ でスピンが $z$ 方向を向いているので，初期状態は $S_z$ の固有値 $1/2$ の固有ベクトル 

$$
|\phi(0)\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

 です。これを設問3の固有ベクトルで展開すると，

$$
|\phi(0)\rangle = \frac{1}{\sqrt{2}}|\lambda_1\rangle + \frac{1}{\sqrt{2}}|\lambda_2\rangle
$$

となります。時間発展演算子 $e^{-i\mathcal{H}t}$ を作用させて $|\phi(t)\rangle$ を求めます。

$$
\begin{aligned}
|\phi(t)\rangle &= \frac{1}{\sqrt{2}}e^{-i\lambda_1 t}|\lambda_1\rangle + \frac{1}{\sqrt{2}}e^{-i\lambda_2 t}|\lambda_2\rangle \\
&= \frac{1}{2}e^{i\frac{\mu H}{2}t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \frac{1}{2}e^{-i\frac{\mu H}{2}t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} \\
&= \begin{pmatrix} \cos\!\left(\frac{\mu H t}{2}\right) \\ i\sin\!\left(\frac{\mu H t}{2}\right) \end{pmatrix}
\end{aligned}
$$

この状態における $S_x, S_y, S_z$ の期待値を計算します。

$$
\begin{aligned}
\langle\phi(t)|S_x|\phi(t)\rangle &= \frac{1}{2}\begin{pmatrix} \cos\frac{\mu H t}{2} & -i\sin\frac{\mu H t}{2} \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} \cos\frac{\mu H t}{2} \\ i\sin\frac{\mu H t}{2} \end{pmatrix} \\
&= \frac{1}{2}\left(i\cos\frac{\mu H t}{2}\sin\frac{\mu H t}{2} - i\sin\frac{\mu H t}{2}\cos\frac{\mu H t}{2}\right) \\
&= 0
\end{aligned}
$$

$$
\begin{aligned}
\langle\phi(t)|S_y|\phi(t)\rangle &= \frac{1}{2}\begin{pmatrix} \cos\frac{\mu H t}{2} & -i\sin\frac{\mu H t}{2} \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} \cos\frac{\mu H t}{2} \\ i\sin\frac{\mu H t}{2} \end{pmatrix} \\
&= \frac{1}{2}\begin{pmatrix} \cos\frac{\mu H t}{2} & -i\sin\frac{\mu H t}{2} \end{pmatrix}\begin{pmatrix} \sin\frac{\mu H t}{2} \\ i\cos\frac{\mu H t}{2} \end{pmatrix} \\
&= \cos\frac{\mu H t}{2}\sin\frac{\mu H t}{2} \\
&= \frac{1}{2}\sin(\mu H t)
\end{aligned}
$$

$$
\begin{aligned}
\langle\phi(t)|S_z|\phi(t)\rangle &= \frac{1}{2}\begin{pmatrix} \cos\frac{\mu H t}{2} & -i\sin\frac{\mu H t}{2} \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} \cos\frac{\mu H t}{2} \\ i\sin\frac{\mu H t}{2} \end{pmatrix} \\
&= \frac{1}{2}\left(\cos^2\frac{\mu H t}{2} - \sin^2\frac{\mu H t}{2}\right) \\
&= \frac{1}{2}\cos(\mu H t)
\end{aligned}
$$

$$
\finalanswer{|\phi(t)\rangle = \begin{pmatrix} \cos\!\left(\frac{\mu H t}{2}\right) \\ i\sin\!\left(\frac{\mu H t}{2}\right) \end{pmatrix}, \qquad \bigl(\langle S_x \rangle, \langle S_y \rangle, \langle S_z \rangle\bigr) = \left(0,\; \frac{1}{2}\sin(\mu H t),\; \frac{1}{2}\cos(\mu H t)\right)}
$$

### (5)
$|\psi(t)\rangle = e^{i\mathcal{H}_1 t}|\varphi(t)\rangle$ を $t$ で微分し，シュレーディンガー方程式 $i\dfrac{\mathrm{d}}{\mathrm{d}t}|\varphi(t)\rangle = (\mathcal{H}_1 + \mathcal{H}_2)|\varphi(t)\rangle$ を代入します。

$$
\begin{aligned}
i\frac{\mathrm{d}}{\mathrm{d}t}|\psi(t)\rangle &= -\mathcal{H}_1 e^{i\mathcal{H}_1 t}|\varphi(t)\rangle + e^{i\mathcal{H}_1 t} i\frac{\mathrm{d}}{\mathrm{d}t}|\varphi(t)\rangle \\
&= -\mathcal{H}_1 e^{i\mathcal{H}_1 t}|\varphi(t)\rangle + e^{i\mathcal{H}_1 t}(\mathcal{H}_1 + \mathcal{H}_2)|\varphi(t)\rangle \\
&= e^{i\mathcal{H}_1 t}\mathcal{H}_2 e^{-i\mathcal{H}_1 t}|\psi(t)\rangle
\end{aligned}
$$

$\mathcal H_1=-aS_z$ は対角行列なので，指数関数は各対角成分の指数になります。

$$
\begin{aligned}
\mathcal H_1&=\begin{pmatrix}-a/2&0\\0&a/2\end{pmatrix}\\
e^{i\mathcal H_1t}&=\begin{pmatrix}e^{-iat/2}&0\\0&e^{iat/2}\end{pmatrix}
\end{aligned}
$$

また，$\mathcal H_2$ を行列で表すと，

$$
\begin{aligned}
\mathcal{H}_2 &= -\frac{a_0}{2}\begin{pmatrix} 0 & \cos\omega t + i\sin\omega t \\ \cos\omega t - i\sin\omega t & 0 \end{pmatrix} \\
&= -\frac{a_0}{2}\begin{pmatrix} 0 & e^{i\omega t} \\ e^{-i\omega t} & 0 \end{pmatrix}
\end{aligned}
$$

これを用いて相互作用表示のハミルトニアン $\mathcal{H}_{\mathrm{I}}(t) \equiv e^{i\mathcal{H}_1 t}\mathcal{H}_2 e^{-i\mathcal{H}_1 t}$ を計算します。

$$
\begin{aligned}
\mathcal{H}_{\mathrm{I}}(t) &= -\frac{a_0}{2}\begin{pmatrix} e^{-iat/2} & 0 \\ 0 & e^{iat/2} \end{pmatrix}\begin{pmatrix} 0 & e^{i\omega t} \\ e^{-i\omega t} & 0 \end{pmatrix}\begin{pmatrix} e^{iat/2} & 0 \\ 0 & e^{-iat/2} \end{pmatrix} \\
&= -\frac{a_0}{2}\begin{pmatrix} 0 & e^{i(\omega - a)t} \\ e^{-i(\omega - a)t} & 0 \end{pmatrix} \\
&= -a_0\bigl(S_x \cos(\omega - a)t - S_y \sin(\omega - a)t\bigr)
\end{aligned}
$$

したがって，$|\psi(t)\rangle$ の時間発展方程式は次のとおりです。

$$
\finalanswer{i\frac{\mathrm{d}}{\mathrm{d}t}|\psi(t)\rangle = -a_0\bigl(S_x \cos(\omega - a)t - S_y \sin(\omega - a)t\bigr)|\psi(t)\rangle}
$$

### (6)
$\omega = a$ を設問5の方程式に代入すると，時間依存性が消えて次式になります。

$$
i\frac{\mathrm{d}}{\mathrm{d}t}|\psi(t)\rangle = -a_0 S_x|\psi(t)\rangle
$$

初期条件は 

$$
\begin{aligned}
|\psi(0)\rangle &= |\varphi(0)\rangle \\
&= \begin{pmatrix} 1 \\ 0 \end{pmatrix}
\end{aligned}
$$

 です。この方程式と初期条件は，設問4において $\mu H$ を $a_0$ に置き換えたものと一致します。したがって，時刻 $t$ における $|\psi(t)\rangle$ は

$$
|\psi(t)\rangle = \begin{pmatrix} \cos\!\left(\frac{a_0 t}{2}\right) \\ i\sin\!\left(\frac{a_0 t}{2}\right) \end{pmatrix}
$$

であり，$\langle\psi(t)|S_z|\psi(t)\rangle = \dfrac{1}{2}\cos(a_0 t)$ です。

$S_z$ は $\mathcal{H}_1 = -a S_z$ と可換なので，$e^{i\mathcal{H}_1 t} S_z e^{-i\mathcal{H}_1 t} = S_z$ が成り立ちます。よってシュレーディンガー表示での期待値 $\langle\varphi(t)|S_z|\varphi(t)\rangle$ は次のように求まります。

$$
\begin{aligned}
\langle\varphi(t)|S_z|\varphi(t)\rangle &= \langle\psi(t)|e^{i\mathcal{H}_1 t} S_z e^{-i\mathcal{H}_1 t}|\psi(t)\rangle \\
&= \langle\psi(t)|S_z|\psi(t)\rangle \\
&= \frac{1}{2}\cos(a_0 t)
\end{aligned}
$$

$$
\finalanswer{\langle\varphi(t)|S_z|\varphi(t)\rangle = \frac{1}{2}\cos(a_0 t)}
$$
