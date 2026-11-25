---
title: 東大理物 平成24年度 数学 第2問：連立偏微分方程式の対角化による解法
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 微分方程式
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成24年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成24年度 数学 第2問：連立偏微分方程式の対角化による解法

## 問題

(1) 以下の連立偏微分方程式を考える。

$$
\left.\begin{aligned}
\frac{\partial u_1}{\partial t} + 4\frac{\partial u_2}{\partial x} &= 0 \\
\frac{\partial u_2}{\partial t} + \frac{\partial u_1}{\partial x} &= 0
\end{aligned}\right\} \tag{1}
$$

ここで $u_1(x, t), u_2(x, t)$ は $-\infty < t < +\infty$ および $-\infty < x < +\infty$ で定義された 2 変数関数である。以下の設問に答えよ。

(i) 式 (1) を以下のようにベクトル表記する。

$$
\frac{\partial\boldsymbol{u}}{\partial t} + A\frac{\partial\boldsymbol{u}}{\partial x} = \boldsymbol{0}, \qquad \boldsymbol{u} = \begin{pmatrix} u_1(x, t) \\ u_2(x, t) \end{pmatrix}
$$

このとき，係数行列 $A$ の固有値 $\lambda_1, \lambda_2$ と固有ベクトル $\boldsymbol{q}_1, \boldsymbol{q}_2$ を求めよ。

(ii) 設問 (i) で求めた $\boldsymbol{q}_1, \boldsymbol{q}_2$ を並べた 2 次元正方行列 $P = (\boldsymbol{q}_1\ \boldsymbol{q}_2)$ を用いて変換

$$
\begin{pmatrix} s_1(x, t) \\ s_2(x, t) \end{pmatrix} = P^{-1}\boldsymbol{u}
$$

を行い，式 (1) を $s_1(x, t), s_2(x, t)$ に対する偏微分方程式に書き換えよ。

(iii) 設問 (ii) で得られた式は $s_1(x, t), s_2(x, t)$ に対してそれぞれ独立な線形方程式であり，初期条件を与えれば解くことができる。さらに，その解から $u_1(x, t), u_2(x, t)$ を求めることができる。このことを用いて，初期条件

$$
u_1(x, t = 0) = e^{-x^2}, \qquad u_2(x, t = 0) = 0
$$

のもとに，連立偏微分方程式 (1) の解 $u_1(x, t), u_2(x, t)$ を求めよ。また $t = 1$ での解の概形を図示せよ。

(2) 2 つの関数 $f_1(x, t), f_2(x, t)$ に対する連立偏微分方程式

$$
\left.\begin{aligned}
\frac{\partial f_1}{\partial t} + \frac{\partial^2 f_1}{\partial x^2} - 6\frac{\partial^2 f_2}{\partial x^2} &= 0 \\
\frac{\partial f_2}{\partial t} + \frac{\partial^2 f_1}{\partial x^2} - 4\frac{\partial^2 f_2}{\partial x^2} &= 0
\end{aligned}\right\}
$$

を初期条件

$$
f_1(x, t = 0) = e^{-x^2}, \qquad f_2(x, t = 0) = 0
$$

のもとに解け。関数の定義域は $0 \le t < +\infty$ および $-\infty < x < +\infty$ とする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成24年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
連立の偏微分方程式は，空間微分の係数行列を対角化する基底に変えると，互いに独立な2つの方程式に分かれます。

問1では，分かれた方程式は1階の移流方程式なので，それぞれの成分は初期の形を保ったまま一定の速さで動きます。問2では，分かれた方程式は拡散方程式なので，フーリエ変換して解きます。
</div>

### (1)(i)
式 (1) より係数行列 $A$ は

$$
A = \begin{pmatrix} 0 & 4 \\ 1 & 0 \end{pmatrix}
$$

です。固有方程式を解きます。

$$
\begin{aligned}
\det(A - \lambda I) &= \lambda^2 - 4 \\
&= 0 \\
\lambda_1 &= 2 \\
\lambda_2 &= -2
\end{aligned}
$$

各固有値に対応する固有ベクトル $\boldsymbol{q}_1, \boldsymbol{q}_2$ を求めます。

$\lambda_1=2$ では，固有方程式の2行目は $x-2y=0$ です。

$$
\begin{aligned}
x&=2y\\
\begin{pmatrix}x\\y\end{pmatrix}&=y\begin{pmatrix}2\\1\end{pmatrix}
\end{aligned}
$$

$y=1$ を選び，$\boldsymbol q_1={}^t(2,1)$ とします。

$\lambda_2=-2$ では，2行目は $x+2y=0$ です。

$$
\begin{aligned}
x&=-2y\\
\begin{pmatrix}x\\y\end{pmatrix}&=y\begin{pmatrix}-2\\1\end{pmatrix}
\end{aligned}
$$

$y=1$ を選び，$\boldsymbol q_2={}^t(-2,1)$ とします。

$$
\finalanswer{\lambda_1 = 2,\; \boldsymbol{q}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \qquad \lambda_2 = -2,\; \boldsymbol{q}_2 = \begin{pmatrix} -2 \\ 1 \end{pmatrix}}
$$

### (1)(ii)


$$
\begin{aligned}
\boldsymbol{s} &= {}^t(s_1, s_2) \\
&= P^{-1}\boldsymbol{u}
\end{aligned}
$$

 より $\boldsymbol{u} = P\boldsymbol{s}$ です。式 (1) の左から $P^{-1}$ を掛けます。

$$
\begin{aligned}
P^{-1}\frac{\partial\boldsymbol{u}}{\partial t} + P^{-1} A P \frac{\partial\boldsymbol{s}}{\partial x} &= \boldsymbol{0} \\
\frac{\partial\boldsymbol{s}}{\partial t} + \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}\frac{\partial\boldsymbol{s}}{\partial x} &= \boldsymbol{0}
\end{aligned}
$$

成分ごとに書くと次の2式になります。

$$
\finalanswer{\frac{\partial s_1}{\partial t} + 2\frac{\partial s_1}{\partial x} = 0, \qquad \frac{\partial s_2}{\partial t} - 2\frac{\partial s_2}{\partial x} = 0}
$$

### (1)(iii)


$$
P = \begin{pmatrix} 2 & -2 \\ 1 & 1 \end{pmatrix}
$$

 の行列式は $\det P = 4$ なので，逆行列は

$$
P^{-1} = \frac{1}{4}\begin{pmatrix} 1 & 2 \\ -1 & 2 \end{pmatrix}
$$

です。初期条件 $\boldsymbol{u}(x, 0) = {}^t(e^{-x^2}, 0)$ を $\boldsymbol{s}(x, 0)$ へ変換します。

$$
\begin{aligned}
\begin{pmatrix} s_1(x, 0) \\ s_2(x, 0) \end{pmatrix} &= \frac{1}{4}\begin{pmatrix} 1 & 2 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} e^{-x^2} \\ 0 \end{pmatrix} \\
&= \begin{pmatrix} \frac{1}{4}e^{-x^2} \\ -\frac{1}{4}e^{-x^2} \end{pmatrix}
\end{aligned}
$$

設問 (1)(ii) の一般解は $s_1(x, t) = F(x - 2t)$，$s_2(x, t) = G(x + 2t)$ です。初期条件を合わせると，

$$
s_1(x, t) = \frac{1}{4}e^{-(x - 2t)^2}, \qquad s_2(x, t) = -\frac{1}{4}e^{-(x + 2t)^2}
$$

となります。$\boldsymbol{u} = P\boldsymbol{s}$ を計算して元の関数に戻します。

$$
\begin{aligned}
\begin{pmatrix} u_1(x, t) \\ u_2(x, t) \end{pmatrix} &= \begin{pmatrix} 2 & -2 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} \frac{1}{4}e^{-(x - 2t)^2} \\ -\frac{1}{4}e^{-(x + 2t)^2} \end{pmatrix} \\
&= \begin{pmatrix} \frac{1}{2}\left(e^{-(x - 2t)^2} + e^{-(x + 2t)^2}\right) \\ \frac{1}{4}\left(e^{-(x - 2t)^2} - e^{-(x + 2t)^2}\right) \end{pmatrix}
\end{aligned}
$$

$t=1$ では，$u_1$ は $x=\pm2$ 付近に高さがほぼ $1/2$ の2つの山をもちます。$u_2$ は $x=2$ 付近に高さがほぼ $1/4$ の山，$x=-2$ 付近に深さがほぼ $-1/4$ の谷をもちます。両側のガウス関数の裾が重なるため，極値の位置と値はこれらからわずかにずれます。概形を下図に示します。

<figure class="problem-figure" markdown>
![t=1におけるu_1(x,1)とu_2(x,1)の概形](../../../docs/assets/figures/pastexam-todai-ributsu/H24_sugaku_2-s-light.svg#only-light)
![t=1におけるu_1(x,1)とu_2(x,1)の概形](../../../docs/assets/figures/pastexam-todai-ributsu/H24_sugaku_2-s-dark.svg#only-dark)
<figcaption markdown="span">$t = 1$ における $u_1(x, 1)$（左）と $u_2(x, 1)$（右）の概形。</figcaption>
</figure>

$$
\finalanswer{u_1(x, t) = \frac{1}{2}\left(e^{-(x - 2t)^2} + e^{-(x + 2t)^2}\right), \qquad u_2(x, t) = \frac{1}{4}\left(e^{-(x - 2t)^2} - e^{-(x + 2t)^2}\right)}
$$

### (2)
$\boldsymbol{f} = {}^t(f_1, f_2)$ とおいて連立偏微分方程式を行列形式で書きます。

$$
\frac{\partial\boldsymbol{f}}{\partial t} = M\frac{\partial^2\boldsymbol{f}}{\partial x^2}, \qquad M = \begin{pmatrix} -1 & 6 \\ -1 & 4 \end{pmatrix}
$$

行列 $M$ の固有値と固有ベクトルを求めます。

$$
\begin{aligned}
\det(M - \mu I) &= (-1 - \mu)(4 - \mu) + 6 \\
&= \mu^2 - 3\mu + 2 \\
&= (\mu - 1)(\mu - 2) \\
&= 0
\end{aligned}
$$

固有値は $\mu_1 = 1$，$\mu_2 = 2$ です。対応する固有ベクトルはそれぞれ 

$$
\boldsymbol{v}_1 = \begin{pmatrix} 3 \\ 1 \end{pmatrix}
$$

，

$$
\boldsymbol{v}_2 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}
$$

 です。これらを並べた行列 

$$
Q = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}
$$

 の逆行列は 

$$
Q^{-1} = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}
$$

 です。



$$
\begin{aligned}
\boldsymbol{g} &= {}^t(g_1, g_2) \\
&= Q^{-1}\boldsymbol{f}
\end{aligned}
$$

 と変換すると，方程式は独立な2本の拡散方程式に分かれます。

$$
\frac{\partial g_1}{\partial t} = \frac{\partial^2 g_1}{\partial x^2}, \qquad \frac{\partial g_2}{\partial t} = 2\frac{\partial^2 g_2}{\partial x^2}
$$

初期条件を $\boldsymbol{g}(x, 0)$ へ変換します。

$$
\begin{aligned}
\begin{pmatrix} g_1(x, 0) \\ g_2(x, 0) \end{pmatrix} &= \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}\begin{pmatrix} e^{-x^2} \\ 0 \end{pmatrix} \\
&= \begin{pmatrix} e^{-x^2} \\ -e^{-x^2} \end{pmatrix}
\end{aligned}
$$

ここで一般の正定数 $D > 0$ に対し，拡散方程式 $\dfrac{\partial h}{\partial t} = D\dfrac{\partial^2 h}{\partial x^2}$ を初期条件 $h(x, 0) = e^{-x^2}$ のもとでフーリエ変換を用いて解きます。

$$
\hat{h}(k, t) = \int_{-\infty}^{\infty} h(x, t) e^{-ikx}\,\mathrm{d}x
$$

 とおくと，$\dfrac{\partial\hat{h}}{\partial t} = -D k^2 \hat{h}$ および初期条件

$$
\begin{aligned}
\hat{h}(k, 0) &= \int_{-\infty}^{\infty} e^{-x^2 - ikx}\,\mathrm{d}x \\
&= e^{-\frac{k^2}{4}}\int_{-\infty}^{\infty} e^{-\left(x + \frac{ik}{2}\right)^2}\,\mathrm{d}x \\
&= \sqrt{\pi}\,e^{-\frac{k^2}{4}}
\end{aligned}
$$

平方完成で移動した積分路は，元の実軸へ平行移動することができます。被積分関数は整関数であり，実部が $\pm R$ の縦辺の積分は定数倍の $e^{-aR^2}$ で抑えられるため，$R\to\infty$ で0になるからです。ここで $a>0$ はガウスの2次の係数です。逆変換の積分にも同じ理由を用います。

時間の方程式と初期値から，

$$
\begin{aligned}
\hat h(k,t)&=\hat h(k,0)e^{-Dk^2t}\\
&=\sqrt\pi\,e^{-k^2/4}e^{-Dk^2t}\\
&=\sqrt\pi\,e^{-(1/4+Dt)k^2}
\end{aligned}
$$

です。逆フーリエ変換を計算します。

$$
\begin{aligned}
h(x, t) &= \frac{1}{2\pi}\int_{-\infty}^{\infty} \sqrt{\pi}\,e^{-\left(\frac{1}{4} + Dt\right)k^2 + ikx}\,\mathrm{d}k \\
&= \frac{\sqrt{\pi}}{2\pi}\sqrt{\frac{\pi}{\frac{1}{4} + Dt}}\exp\!\left(-\frac{x^2}{4\left(\frac{1}{4} + Dt\right)}\right) \\
&= \frac{1}{\sqrt{1 + 4Dt}}\exp\!\left(-\frac{x^2}{1 + 4Dt}\right)
\end{aligned}
$$

$D = 1$ と $D = 2$ を代入すると，$g_1, g_2$ は次のようになります。

$$
g_1(x, t) = \frac{1}{\sqrt{1 + 4t}}\exp\!\left(-\frac{x^2}{1 + 4t}\right), \qquad g_2(x, t) = -\frac{1}{\sqrt{1 + 8t}}\exp\!\left(-\frac{x^2}{1 + 8t}\right)
$$

最後に $\boldsymbol{f} = Q\boldsymbol{g}$ を計算して $f_1(x, t), f_2(x, t)$ を求めます。

$$
\begin{aligned}
f_1(x, t) &= 3 g_1(x, t) + 2 g_2(x, t) \\
&= \frac{3}{\sqrt{1 + 4t}}\exp\!\left(-\frac{x^2}{1 + 4t}\right) - \frac{2}{\sqrt{1 + 8t}}\exp\!\left(-\frac{x^2}{1 + 8t}\right)
\end{aligned}
$$

$$
\begin{aligned}
f_2(x, t) &= g_1(x, t) + g_2(x, t) \\
&= \frac{1}{\sqrt{1 + 4t}}\exp\!\left(-\frac{x^2}{1 + 4t}\right) - \frac{1}{\sqrt{1 + 8t}}\exp\!\left(-\frac{x^2}{1 + 8t}\right)
\end{aligned}
$$

$$
\finalanswer{f_1(x, t) = \frac{3}{\sqrt{1 + 4t}}\exp\!\left(-\frac{x^2}{1 + 4t}\right) - \frac{2}{\sqrt{1 + 8t}}\exp\!\left(-\frac{x^2}{1 + 8t}\right), \qquad f_2(x, t) = \frac{1}{\sqrt{1 + 4t}}\exp\!\left(-\frac{x^2}{1 + 4t}\right) - \frac{1}{\sqrt{1 + 8t}}\exp\!\left(-\frac{x^2}{1 + 8t}\right)}
$$
