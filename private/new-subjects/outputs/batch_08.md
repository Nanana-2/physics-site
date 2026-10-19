===== FILE: 09vector_analysis/01/01_010.md =====
---
tags:
  - 基本
---

# 内積・外積・スカラー三重積

## 問題
3つのベクトル

$$
\boldsymbol{a}=(1,2,0),\quad \boldsymbol{b}=(0,1,3),\quad \boldsymbol{c}=(2,0,1)
$$

を考える。以下の問いに答えよ。

(1) 外積 $\boldsymbol{a}\times\boldsymbol{b}$ を成分で求めよ。

(2) $\boldsymbol{a}$ と $\boldsymbol{b}$ を2辺とする平行四辺形の面積 $S$ を求めよ。

(3) $\boldsymbol{a},\boldsymbol{b},\boldsymbol{c}$ を3辺とする平行六面体の体積 $V$ を求めよ。

---

## 解答・解説

### (1)
外積の成分は，$\boldsymbol{a}=(a_x,a_y,a_z)$，$\boldsymbol{b}=(b_x,b_y,b_z)$ に対して次の式で与えられます。

$$
\boldsymbol{a}\times\boldsymbol{b}=(a_yb_z-a_zb_y,\ a_zb_x-a_xb_z,\ a_xb_y-a_yb_x)
$$

この式に成分を代入すると，

$$
\begin{aligned}
\boldsymbol{a}\times\boldsymbol{b}&=(2\cdot 3-0\cdot 1,\ 0\cdot 0-1\cdot 3,\ 1\cdot 1-2\cdot 0)\\
&=\finalanswer{(6,-3,1)}
\end{aligned}
$$

となります。検算として，$\boldsymbol{a}\cdot(\boldsymbol{a}\times\boldsymbol{b})=6-6+0=0$，$\boldsymbol{b}\cdot(\boldsymbol{a}\times\boldsymbol{b})=0-3+3=0$ となり，外積が両方のベクトルに直交していることを確かめられます。

### (2)
外積の大きさは $|\boldsymbol{a}||\boldsymbol{b}|\sin\theta$ で，これは2辺のなす角が $\theta$ の平行四辺形の面積に等しくなります。したがって，(1) の結果を使うと，

$$
\begin{aligned}
S&=|\boldsymbol{a}\times\boldsymbol{b}|\\
&=\sqrt{36+9+1}\\
&=\finalanswer{S=\sqrt{46}}
\end{aligned}
$$

となります。別の方法として，$|\boldsymbol{a}|^2=5$，$|\boldsymbol{b}|^2=10$，$\boldsymbol{a}\cdot\boldsymbol{b}=2$ から $|\boldsymbol{a}|^2|\boldsymbol{b}|^2-(\boldsymbol{a}\cdot\boldsymbol{b})^2=46$ となり，同じ値が得られます。

### (3)
平行六面体の体積は，底面積 $S$ に高さをかけたものです。高さは $\boldsymbol{c}$ の底面の法線方向の成分の大きさで，法線の向きは $\boldsymbol{a}\times\boldsymbol{b}$ の向きです。よって，体積はスカラー三重積の絶対値になり，

$$
\begin{aligned}
V&=|(\boldsymbol{a}\times\boldsymbol{b})\cdot\boldsymbol{c}|\\
&=|6\cdot 2+(-3)\cdot 0+1\cdot 1|\\
&=\finalanswer{V=13}
\end{aligned}
$$

となります。スカラー三重積は3つのベクトルを行に並べた行列式に等しく，行列式を1行目で展開すると $1\cdot 1-2\cdot(0-6)+0=13$ となり，同じ値と一致します。

===== FILE: 09vector_analysis/01/01_020.md =====
---
tags:
  - 基本
---

# ベクトル三重積

## 問題
$\boldsymbol{a},\boldsymbol{b},\boldsymbol{c},\boldsymbol{d}$ を3次元の任意のベクトルとする。以下の問いに答えよ。

(1) 成分を用いて次の式を示せ。

$$
\boldsymbol{a}\times(\boldsymbol{b}\times\boldsymbol{c})=\boldsymbol{b}(\boldsymbol{a}\cdot\boldsymbol{c})-\boldsymbol{c}(\boldsymbol{a}\cdot\boldsymbol{b})
$$

(2) (1) を用いて次の式を示せ。

$$
\boldsymbol{a}\times(\boldsymbol{b}\times\boldsymbol{c})+\boldsymbol{b}\times(\boldsymbol{c}\times\boldsymbol{a})+\boldsymbol{c}\times(\boldsymbol{a}\times\boldsymbol{b})=\boldsymbol{0}
$$

(3) スカラー三重積の性質と (1) を用いて，$(\boldsymbol{a}\times\boldsymbol{b})\cdot(\boldsymbol{c}\times\boldsymbol{d})$ を内積だけで表せ。

---

##解答・解説

### (1)
$x$ 成分を示せば，$y,z$ 成分は添字を巡回的に入れ替えるだけで同じように示せます。まず，$\boldsymbol{b}\times\boldsymbol{c}$ の $y,z$ 成分は次のとおりです。

$$
\begin{aligned}
(\boldsymbol{b}\times\boldsymbol{c})_y&=b_zc_x-b_xc_z\\
(\boldsymbol{b}\times\boldsymbol{c})_z&=b_xc_y-b_yc_x
\end{aligned}
$$

これを用いて左辺の $x$ 成分を計算し，$a_xb_xc_x$ を足して引くと，

$$
\begin{aligned}
[\boldsymbol{a}\times(\boldsymbol{b}\times\boldsymbol{c})]_x&=a_y(b_xc_y-b_yc_x)-a_z(b_zc_x-b_xc_z)\\
&=b_x(a_yc_y+a_zc_z)-c_x(a_yb_y+a_zb_z)\\
&=b_x(a_xc_x+a_yc_y+a_zc_z)-c_x(a_xb_x+a_yb_y+a_zb_z)\\
&=\finalanswer{b_x(\boldsymbol{a}\cdot\boldsymbol{c})-c_x(\boldsymbol{a}\cdot\boldsymbol{b})}
\end{aligned}
$$

となります。これは右辺の $x$ 成分と一致します。

### (2)
3つの項それぞれに (1) を適用します。

$$
\begin{aligned}
\boldsymbol{a}\times(\boldsymbol{b}\times\boldsymbol{c})&=\boldsymbol{b}(\boldsymbol{a}\cdot\boldsymbol{c})-\boldsymbol{c}(\boldsymbol{a}\cdot\boldsymbol{b})\\
\boldsymbol{b}\times(\boldsymbol{c}\times\boldsymbol{a})&=\boldsymbol{c}(\boldsymbol{b}\cdot\boldsymbol{a})-\boldsymbol{a}(\boldsymbol{b}\cdot\boldsymbol{c})\\
\boldsymbol{c}\times(\boldsymbol{a}\times\boldsymbol{b})&=\boldsymbol{a}(\boldsymbol{c}\cdot\boldsymbol{b})-\boldsymbol{b}(\boldsymbol{c}\cdot\boldsymbol{a})
\end{aligned}
$$

内積は交換できるので，3式を足すと右辺の6項は2つずつ打ち消し合います。したがって，

$$
\finalanswer{\boldsymbol{a}\times(\boldsymbol{b}\times\boldsymbol{c})+\boldsymbol{b}\times(\boldsymbol{c}\times\boldsymbol{a})+\boldsymbol{c}\times(\boldsymbol{a}\times\boldsymbol{b})=\boldsymbol{0}}
$$

となります。この式はヤコビ恒等式と呼ばれます。

### (3)
スカラー三重積では内積と外積を入れ替えられ，$(\boldsymbol{a}\times\boldsymbol{b})\cdot\boldsymbol{e}=\boldsymbol{a}\cdot(\boldsymbol{b}\times\boldsymbol{e})$ が成り立ちます。$\boldsymbol{e}=\boldsymbol{c}\times\boldsymbol{d}$ とおいてこの関係を使い，さらに (1) を適用すると，

$$
\begin{aligned}
(\boldsymbol{a}\times\boldsymbol{b})\cdot(\boldsymbol{c}\times\boldsymbol{d})&=\boldsymbol{a}\cdot[\boldsymbol{b}\times(\boldsymbol{c}\times\boldsymbol{d})]\\
&=\boldsymbol{a}\cdot[\boldsymbol{c}(\boldsymbol{b}\cdot\boldsymbol{d})-\boldsymbol{d}(\boldsymbol{b}\cdot\boldsymbol{c})]\\
&=\finalanswer{(\boldsymbol{a}\cdot\boldsymbol{c})(\boldsymbol{b}\cdot\boldsymbol{d})-(\boldsymbol{a}\cdot\boldsymbol{d})(\boldsymbol{b}\cdot\boldsymbol{c})}
\end{aligned}
$$

となります。$\boldsymbol{c}=\boldsymbol{a}$，$\boldsymbol{d}=\boldsymbol{b}$ とおくと $|\boldsymbol{a}\times\boldsymbol{b}|^2=|\boldsymbol{a}|^2|\boldsymbol{b}|^2-(\boldsymbol{a}\cdot\boldsymbol{b})^2$ となり，$\sin^2\theta=1-\cos^2\theta$ と一致します。

===== FILE: 09vector_analysis/01/01_030.md =====
---
tags:
  - 標準
---

# 空間曲線の接線と曲率

## 問題
$a>0$，$b>0$ を定数として，次の式で表されるらせんを考える。

$$
\boldsymbol{r}(t)=(a\cos t,\ a\sin t,\ bt)\quad (t\ge 0)
$$

$t=0$ の点から測った弧長を $s$，単位接線ベクトルを $\boldsymbol{T}=d\boldsymbol{r}/ds$ とする。曲率 $\kappa\ (\kappa\ge 0)$ と主法線単位ベクトル $\boldsymbol{N}$ を $d\boldsymbol{T}/ds=\kappa\boldsymbol{N}$ で定める。以下の問いに答えよ。

(1) 弧長 $s$ を $t$ の関数として求めよ。

(2) 単位接線ベクトル $\boldsymbol{T}$ を $t$ の関数として求めよ。

(3) 曲率 $\kappa$ を求めよ。

---

##解答・解説

### (1)
弧長は速さ $|d\boldsymbol{r}/dt|$ を $t$ で積分して得られます。まず速さを計算すると，

$$
\begin{aligned}
\left|\frac{d\boldsymbol{r}}{dt}\right|&=|(-a\sin t,\ a\cos t,\ b)|\\
&=\sqrt{a^2\sin^2 t+a^2\cos^2 t+b^2}\\
&=\sqrt{a^2+b^2}
\end{aligned}
$$

となり，$t$ によらない一定値です。よって，$0$ から $t$ まで積分すると，

$$
\finalanswer{s=\sqrt{a^2+b^2}\,t}
$$

となります。

### (2)
連鎖律により $d\boldsymbol{r}/ds=(d\boldsymbol{r}/dt)/(ds/dt)$ です。以下 $c=\sqrt{a^2+b^2}$ とおきます。(1) より $ds/dt=c$ なので，

$$
\finalanswer{\boldsymbol{T}=\frac{1}{\sqrt{a^2+b^2}}(-a\sin t,\ a\cos t,\ b)}
$$

となります。各成分の2乗の和が1になり，$\boldsymbol{T}$ が単位ベクトルであることを確かめられます。

### (3)
$\boldsymbol{T}$ を $t$ で微分してから $ds/dt=c$ で割ると，$s$ による微分が得られます。

$$
\begin{aligned}
\frac{d\boldsymbol{T}}{ds}&=\frac{1}{c}\frac{d\boldsymbol{T}}{dt}\\
&=\frac{1}{c^2}(-a\cos t,\ -a\sin t,\ 0)\\
&=\frac{a}{c^2}(-\cos t,\ -\sin t,\ 0)
\end{aligned}
$$

最後の式の $(-\cos t,-\sin t,0)$ は単位ベクトルで，これが $\boldsymbol{N}$ です。したがって，

$$
\finalanswer{\kappa=\frac{a}{a^2+b^2}}
$$

となります。$\boldsymbol{N}$ はらせんの軸である $z$ 軸に向かって水平を向いています。$b\to 0$ では半径 $a$ の円の曲率 $1/a$ と一致し，$a\to 0$ では直線になるので $\kappa\to 0$ となります。

===== FILE: 09vector_analysis/01/01_040.md =====
---
tags:
  - 基本
---

# 極座標での速度と加速度

## 問題
$xy$ 平面上を運動する質点の位置を極座標 $(r,\theta)$ で表し，$r,\theta$ は時刻 $t$ の関数とする。単位ベクトルを

$$
\begin{aligned}
\boldsymbol{e}_r&=\cos\theta\,\boldsymbol{e}_x+\sin\theta\,\boldsymbol{e}_y\\
\boldsymbol{e}_\theta&=-\sin\theta\,\boldsymbol{e}_x+\cos\theta\,\boldsymbol{e}_y
\end{aligned}
$$

で定め，時間微分をドットで表す（図）。以下の問いに答えよ。

<!-- FIGURE problem: xy 平面。原点 O から質点 P へ線分を引き，長さを r，x 軸からの角を θ とラベルする。P に単位ベクトル e_r（OP の延長方向）と e_θ（e_r を反時計回りに 90° 回した向き）を矢印で描く。x 軸，y 軸にもラベルを付ける。 -->

(1) $\dot{\boldsymbol{e}}_r$ と $\dot{\boldsymbol{e}}_\theta$ を $\dot{\theta}$，$\boldsymbol{e}_r$，$\boldsymbol{e}_\theta$ で表せ。

(2) 速度 $\boldsymbol{v}=\dot{\boldsymbol{r}}$ を $\boldsymbol{e}_r,\boldsymbol{e}_\theta$ の成分で表せ。

(3) 加速度 $\boldsymbol{a}=\ddot{\boldsymbol{r}}$ を $\boldsymbol{e}_r,\boldsymbol{e}_\theta$ の成分で表せ。

---

##解答・解説

### (1)
$\boldsymbol{e}_x,\boldsymbol{e}_y$ は時間によらないので，$\theta$ を通した時間依存だけを連鎖律で微分します。

$$
\begin{aligned}
\dot{\boldsymbol{e}}_r&=\dot{\theta}(-\sin\theta\,\boldsymbol{e}_x+\cos\theta\,\boldsymbol{e}_y)=\finalanswer{\dot{\boldsymbol{e}}_r=\dot{\theta}\,\boldsymbol{e}_\theta}\\
\dot{\boldsymbol{e}}_\theta&=\dot{\theta}(-\cos\theta\,\boldsymbol{e}_x-\sin\theta\,\boldsymbol{e}_y)=\finalanswer{\dot{\boldsymbol{e}}_\theta=-\dot{\theta}\,\boldsymbol{e}_r}
\end{aligned}
$$

となります。単位ベクトルは大きさが変わらないので，その時間微分は自分自身に直交します。

### (2)
位置ベクトルは $\boldsymbol{r}=r\boldsymbol{e}_r$ と書けます。積の微分を行い，(1) の結果を使うと，

$$
\begin{aligned}
\boldsymbol{v}&=\dot{r}\,\boldsymbol{e}_r+r\,\dot{\boldsymbol{e}}_r\\
&=\finalanswer{\boldsymbol{v}=\dot{r}\,\boldsymbol{e}_r+r\dot{\theta}\,\boldsymbol{e}_\theta}
\end{aligned}
$$

となります。第1項は動径方向の伸び縮み，第2項は回転による速度です。

### (3)
(2) の結果をもう一度時間で微分し，単位ベクトルの微分には (1) を使います。

$$
\begin{aligned}
\boldsymbol{a}&=\ddot{r}\,\boldsymbol{e}_r+\dot{r}\,\dot{\boldsymbol{e}}_r+(\dot{r}\dot{\theta}+r\ddot{\theta})\boldsymbol{e}_\theta+r\dot{\theta}\,\dot{\boldsymbol{e}}_\theta\\
&=\ddot{r}\,\boldsymbol{e}_r+\dot{r}\dot{\theta}\,\boldsymbol{e}_\theta+(\dot{r}\dot{\theta}+r\ddot{\theta})\boldsymbol{e}_\theta-r\dot{\theta}^2\,\boldsymbol{e}_r
\end{aligned}
$$

$\boldsymbol{e}_r$ と $\boldsymbol{e}_\theta$ の成分ごとにまとめると，

$$
\finalanswer{\boldsymbol{a}=(\ddot{r}-r\dot{\theta}^2)\boldsymbol{e}_r+(r\ddot{\theta}+2\dot{r}\dot{\theta})\boldsymbol{e}_\theta}
$$

となります。半径 $R$ の等速円運動では $\ddot{r}=\dot{r}=\ddot{\theta}=0$ なので $\boldsymbol{a}=-R\dot{\theta}^2\boldsymbol{e}_r$ となり，向心加速度と一致します。

===== FILE: 09vector_analysis/02/02_010.md =====
---
tags:
  - 基本
---

# 勾配と方向微分

## 問題
スカラー場

$$
\phi(x,y,z)=x^2+2y^2+3z^2
$$

と点 $\mathrm{P}(1,1,1)$ を考える。単位ベクトル $\boldsymbol{n}$ の向きの方向微分を，点 P から $\boldsymbol{n}$ の向きに距離 $s$ だけ進んだときの $d\phi/ds$ の $s=0$ での値で定める。以下の問いに答えよ。

(1) 点 P における勾配 $\nabla\phi$ を求めよ。

(2) 点 P における $\boldsymbol{n}=(1,2,2)/3$ の向きの方向微分を求めよ。

(3) 点 P を通る等高面 $\phi=6$ の，点 P における単位法線ベクトルのうち $\phi$ が増える向きのものを求めよ。

---

##解答・解説

### (1)
勾配は各座標による偏微分を成分とするベクトルです。

$$
\nabla\phi=(2x,\ 4y,\ 6z)
$$

$(x,y,z)=(1,1,1)$ を代入すると，

$$
\finalanswer{\nabla\phi(\mathrm{P})=(2,4,6)}
$$

となります。

### (2)
点 P から $\boldsymbol{n}$ の向きに進む直線は $\boldsymbol{r}(s)=\boldsymbol{r}_{\mathrm{P}}+s\boldsymbol{n}$ です。連鎖律により，$\phi(\boldsymbol{r}(s))$ の $s$ 微分は勾配と $\boldsymbol{n}$ の内積になります。

$$
\frac{d\phi}{ds}=\frac{\partial\phi}{\partial x}n_x+\frac{\partial\phi}{\partial y}n_y+\frac{\partial\phi}{\partial z}n_z=\nabla\phi\cdot\boldsymbol{n}
$$

(1) の結果と $\boldsymbol{n}$ の内積を計算すると，

$$
\begin{aligned}
\nabla\phi(\mathrm{P})\cdot\boldsymbol{n}&=\frac{1}{3}(2\cdot 1+4\cdot 2+6\cdot 2)\\
&=\finalanswer{\frac{22}{3}}
\end{aligned}
$$

となります。方向微分の最大値は $\boldsymbol{n}$ が勾配と同じ向きのときの $|\nabla\phi|=2\sqrt{14}\approx 7.48$ で，$22/3\approx 7.33$ はこれより小さくなっています。

### (3)
等高面上の曲線に沿って進むと $\phi$ は変わらないので，その接線方向 $\boldsymbol{t}$ について $\nabla\phi\cdot\boldsymbol{t}=0$ です。よって，勾配は等高面に垂直で，$\phi$ が増える向きを向いています。$\phi(\mathrm{P})=1+2+3=6$ なので P は確かにこの等高面上にあります。$|\nabla\phi(\mathrm{P})|=\sqrt{4+16+36}=2\sqrt{14}$ で割って正規化すると，

$$
\begin{aligned}
\boldsymbol{e}&=\frac{(2,4,6)}{2\sqrt{14}}\\
&=\finalanswer{\frac{1}{\sqrt{14}}(1,2,3)}
\end{aligned}
$$

となります。

===== FILE: 09vector_analysis/02/02_020.md =====
---
tags:
  - 基本
---

# 発散の計算と意味

## 問題
位置ベクトルを $\boldsymbol{r}=(x,y,z)$，その大きさを $r=|\boldsymbol{r}|$ とし，$r\neq 0$ の領域を考える。$f(r)$ は $r$ の微分可能な関数とする。以下の問いに答えよ。

(1) $\nabla\cdot\boldsymbol{r}$ を求めよ。

(2) $\nabla\cdot(f(r)\boldsymbol{r})$ を $f$，$f'$，$r$ で表せ。

(3) $\nabla\cdot(r^n\boldsymbol{r})=0$ が $r\neq 0$ のすべての点で成り立つような実数 $n$ を求めよ。

---

##解答・解説

### (1)
発散は各成分をその座標で偏微分して足したものです。

$$
\begin{aligned}
\nabla\cdot\boldsymbol{r}&=\frac{\partial x}{\partial x}+\frac{\partial y}{\partial y}+\frac{\partial z}{\partial z}\\
&=\finalanswer{3}
\end{aligned}
$$

となります。この場はどの点でも単位体積あたり一定の割合で湧き出しています。

### (2)
$x$ 成分 $f(r)x$ を $x$ で偏微分します。$r^2=x^2+y^2+z^2$ を $x$ で微分すると $\partial r/\partial x=x/r$ となるので，

$$
\begin{aligned}
\frac{\partial}{\partial x}\bigl(f(r)x\bigr)&=f(r)+x f'(r)\frac{\partial r}{\partial x}\\
&=f(r)+f'(r)\frac{x^2}{r}
\end{aligned}
$$

となります。$y,z$ 成分も同じ形なので，3つを足して $x^2+y^2+z^2=r^2$ を使うと，

$$
\begin{aligned}
\nabla\cdot(f\boldsymbol{r})&=3f+f'\frac{x^2+y^2+z^2}{r}\\
&=\finalanswer{\nabla\cdot(f(r)\boldsymbol{r})=3f(r)+rf'(r)}
\end{aligned}
$$

となります。$f=1$ とおくと (1) の結果と一致します。

### (3)
(2) の結果に $f(r)=r^n$ を代入します。$f'=nr^{n-1}$ なので，

$$
\begin{aligned}
\nabla\cdot(r^n\boldsymbol{r})&=3r^n+r\cdot nr^{n-1}\\
&=(3+n)r^n
\end{aligned}
$$

となります。これが $r\neq 0$ で常に零になるのは $3+n=0$ のときなので，

$$
\finalanswer{n=-3}
$$

となります。このときの場 $\boldsymbol{r}/r^3$ は点電荷のクーロン場と同じ形で，原点以外には湧き出しがありません。

===== FILE: 09vector_analysis/02/02_030.md =====
---
tags:
  - 基本
---

# 回転の計算と意味

## 問題
角速度ベクトル $\boldsymbol{\omega}$ で原点を通る軸のまわりに剛体回転する物体の速度場は $\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{r}$ である。ここで $\boldsymbol{r}=(x,y,z)$ は位置ベクトル，$\boldsymbol{\omega}$ は定ベクトルである。以下の問いに答えよ。

(1) $\boldsymbol{\omega}=\omega\boldsymbol{e}_z$ のとき，$\boldsymbol{v}$ を成分で求めよ。

(2) (1) の場合について，$\nabla\times\boldsymbol{v}$ を求めよ。

(3) 一般の定ベクトル $\boldsymbol{\omega}$ について，$\nabla\times(\boldsymbol{\omega}\times\boldsymbol{r})$ を $\boldsymbol{\omega}$ で表せ。

---

##解答・解説

### (1)
外積の成分の式に $\boldsymbol{\omega}=(0,0,\omega)$ と $\boldsymbol{r}=(x,y,z)$ を代入すると，

$$
\begin{aligned}
\boldsymbol{v}&=(0\cdot z-\omega y,\ \omega x-0\cdot z,\ 0\cdot y-0\cdot x)\\
&=\finalanswer{\boldsymbol{v}=(-\omega y,\ \omega x,\ 0)}
\end{aligned}
$$

となります。速さは $\omega\sqrt{x^2+y^2}$ で，回転軸からの距離に比例します。

### (2)
回転の各成分を計算します。$v_z=0$ で，$v_x,v_y$ は $z$ によらないので，$x,y$ 成分は零です。$z$ 成分だけが残り，

$$
\begin{aligned}
(\nabla\times\boldsymbol{v})_z&=\frac{\partial v_y}{\partial x}-\frac{\partial v_x}{\partial y}\\
&=\omega-(-\omega)\\
&=2\omega
\end{aligned}
$$

となります。よって，

$$
\finalanswer{\nabla\times\boldsymbol{v}=2\omega\boldsymbol{e}_z}
$$

となります。

### (3)
$x$ 成分を計算します。$\boldsymbol{\omega}\times\boldsymbol{r}$ の $y,z$ 成分は $\omega_zx-\omega_xz$ と $\omega_xy-\omega_yx$ です。$\boldsymbol{\omega}$ は定数なので，

$$
\begin{aligned}
[\nabla\times(\boldsymbol{\omega}\times\boldsymbol{r})]_x&=\frac{\partial}{\partial y}(\omega_xy-\omega_yx)-\frac{\partial}{\partial z}(\omega_zx-\omega_xz)\\
&=\omega_x+\omega_x\\
&=2\omega_x
\end{aligned}
$$

となります。$y,z$ 成分も同じように $2\omega_y$，$2\omega_z$ となるので，

$$
\finalanswer{\nabla\times(\boldsymbol{\omega}\times\boldsymbol{r})=2\boldsymbol{\omega}}
$$

となります。速度場の回転は，各点での局所的な回転の角速度の2倍を表しています。剛体回転ではこれがどの点でも同じ値になります。

===== FILE: 09vector_analysis/02/02_040.md =====
---
tags:
  - 標準
---

# ナブラを含む恒等式

## 問題
$\phi,\psi$ をスカラー場，$\boldsymbol{A}$ をベクトル場とし，いずれも2回連続微分可能とする。以下の問いに答えよ。

(1) $\nabla\times(\nabla\phi)=\boldsymbol{0}$ となることを示せ。

(2) $\nabla\cdot(\nabla\times\boldsymbol{A})=0$ となることを示せ。

(3) $\nabla\times(\phi\nabla\psi)$ を考えて，$\nabla\cdot(\nabla\phi\times\nabla\psi)=0$ となることを示せ。

---

##解答・解説

### (1)
$x$ 成分を計算します。2回連続微分可能な関数では偏微分の順序を交換できるので，

$$
\begin{aligned}
[\nabla\times(\nabla\phi)]_x&=\frac{\partial}{\partial y}\frac{\partial\phi}{\partial z}-\frac{\partial}{\partial z}\frac{\partial\phi}{\partial y}\\
&=0
\end{aligned}
$$

となります。$y,z$ 成分も同じように零なので，

$$
\finalanswer{\nabla\times(\nabla\phi)=\boldsymbol{0}}
$$

となります。勾配で表される場は渦を持ちません。

### (2)
回転の成分を書き出して発散をとります。

$$
\begin{aligned}
\nabla\cdot(\nabla\times\boldsymbol{A})&=\frac{\partial}{\partial x}\left(\frac{\partial A_z}{\partial y}-\frac{\partial A_y}{\partial z}\right)+\frac{\partial}{\partial y}\left(\frac{\partial A_x}{\partial z}-\frac{\partial A_z}{\partial x}\right)\\
&\quad+\frac{\partial}{\partial z}\left(\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}\right)
\end{aligned}
$$

$A_z$ を含む項は $\partial_x\partial_yA_z-\partial_y\partial_xA_z$ の組になり，偏微分の順序を交換すると打ち消し合います。$A_x$，$A_y$ を含む項も同じです。よって，

$$
\finalanswer{\nabla\cdot(\nabla\times\boldsymbol{A})=0}
$$

となります。回転で表される場には湧き出しがありません。

### (3)
$\nabla\times(\phi\nabla\psi)$ の $x$ 成分を積の微分で展開します。

$$
\begin{aligned}
[\nabla\times(\phi\nabla\psi)]_x&=\frac{\partial}{\partial y}\left(\phi\frac{\partial\psi}{\partial z}\right)-\frac{\partial}{\partial z}\left(\phi\frac{\partial\psi}{\partial y}\right)\\
&=\frac{\partial\phi}{\partial y}\frac{\partial\psi}{\partial z}-\frac{\partial\phi}{\partial z}\frac{\partial\psi}{\partial y}+\phi\left(\frac{\partial^2\psi}{\partial y\partial z}-\frac{\partial^2\psi}{\partial z\partial y}\right)\\
&=(\nabla\phi\times\nabla\psi)_x
\end{aligned}
$$

他の成分も同じなので $\nabla\phi\times\nabla\psi=\nabla\times(\phi\nabla\psi)$ です。この式の発散をとり，(2) を $\boldsymbol{A}=\phi\nabla\psi$ として適用すると，

$$
\begin{aligned}
\nabla\cdot(\nabla\phi\times\nabla\psi)&=\nabla\cdot[\nabla\times(\phi\nabla\psi)]\\
&=\finalanswer{0}
\end{aligned}
$$

となります。

===== FILE: 09vector_analysis/02/02_050.md =====
---
tags:
  - 標準
---

# レヴィ・チビタ記号による証明

## 問題
$\varepsilon_{ijk}$ をレヴィ・チビタ記号とする。$\varepsilon_{123}=1$ で，任意の2つの添字の入れ替えで符号が変わるものである。$\delta_{ij}$ はクロネッカーのデルタ，添字 $i,j,\ldots$ は $1,2,3$ をとり，同じ添字が2回現れたら和をとる。$\partial_i=\partial/\partial x_i$ とし，回転を $(\nabla\times\boldsymbol{A})_i=\varepsilon_{ijk}\partial_jA_k$ で表す。ベクトル場 $\boldsymbol{A}$ は2回連続微分可能とする。以下の問いに答えよ。

(1) 次の式を示せ。

$$
\varepsilon_{ijk}\varepsilon_{imn}=\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km}
$$

(2) (1) を用いて，$\nabla\times(\nabla\times\boldsymbol{A})=\nabla(\nabla\cdot\boldsymbol{A})-\nabla^2\boldsymbol{A}$ となることを示せ。

(3) $\boldsymbol{c}$ を定ベクトル，$r=|\boldsymbol{r}|$ として，$\boldsymbol{A}=r^2\boldsymbol{c}$ に対する $\nabla\times(\nabla\times\boldsymbol{A})$ を (2) を用いて求めよ。

---

##解答・解説

### (1)
$j,k,m,n$ を固定して場合分けします。左辺で $\varepsilon_{ijk}\neq 0$ となるには $j\neq k$ かつ $i$ が残りの1つの値であることが必要で，$\varepsilon_{imn}\neq 0$ にも同じ条件が必要です。よって，左辺が零でないのは $j\neq k$ かつ $\{m,n\}=\{j,k\}$ のときだけです。

$j=m$，$k=n$ ($j\neq k$) のとき，左辺は $\varepsilon_{ijk}^2=1$，右辺は $1-\delta_{jk}\delta_{kj}=1$ です。$j=n$，$k=m$ ($j\neq k$) のとき，左辺は $\varepsilon_{ijk}\varepsilon_{ikj}=-1$，右辺は $\delta_{jk}\delta_{kj}-1=-1$ です。それ以外の場合，左辺は零です。右辺も，$\delta_{jm}\delta_{kn}$ か $\delta_{jn}\delta_{km}$ が1になるのは $\{m,n\}=\{j,k\}$ のときに限られ，$j=k$ なら2項が等しく打ち消すので零です。よって，すべての場合に

$$
\finalanswer{\varepsilon_{ijk}\varepsilon_{imn}=\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km}}
$$

が成り立ちます。

### (2)
回転を2回適用した式の第 $i$ 成分を書き，$\varepsilon_{ijk}=\varepsilon_{kij}$ と並べ替えて (1) を使います。

$$
\begin{aligned}
[\nabla\times(\nabla\times\boldsymbol{A})]_i&=\varepsilon_{ijk}\partial_j(\varepsilon_{kmn}\partial_mA_n)\\
&=\varepsilon_{kij}\varepsilon_{kmn}\partial_j\partial_mA_n\\
&=(\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm})\partial_j\partial_mA_n\\
&=\partial_i\partial_jA_j-\partial_j\partial_jA_i
\end{aligned}
$$

第1項は $\nabla(\nabla\cdot\boldsymbol{A})$ の第 $i$ 成分，第2項は $\nabla^2A_i$ です。したがって，

$$
\finalanswer{\nabla\times(\nabla\times\boldsymbol{A})=\nabla(\nabla\cdot\boldsymbol{A})-\nabla^2\boldsymbol{A}}
$$

となります。

### (3)
$r^2=x_jx_j$ より $\partial_ir^2=2x_i$，$\nabla^2r^2=6$ です。これを使って (2) の右辺の2つの項を計算すると，

$$
\begin{aligned}
\nabla\cdot\boldsymbol{A}&=c_i\partial_ir^2=2\boldsymbol{c}\cdot\boldsymbol{r}\\
\nabla(\nabla\cdot\boldsymbol{A})&=2\boldsymbol{c}\\
\nabla^2\boldsymbol{A}&=(\nabla^2r^2)\boldsymbol{c}=6\boldsymbol{c}
\end{aligned}
$$

となります。(2) に代入すると，

$$
\finalanswer{\nabla\times(\nabla\times\boldsymbol{A})=-4\boldsymbol{c}}
$$

となります。直接計算すると $\nabla\times(r^2\boldsymbol{c})=2\boldsymbol{r}\times\boldsymbol{c}$ です。さらに剛体回転の場の回転 $\nabla\times(\boldsymbol{c}\times\boldsymbol{r})=2\boldsymbol{c}$ を使うと，$-2\cdot 2\boldsymbol{c}=-4\boldsymbol{c}$ となり，結果と一致します。

===== FILE: 09vector_analysis/02/02_060.md =====
---
tags:
  - 標準
---

# 保存場の判定とポテンシャル

## 問題
$\alpha,\beta$ を定数として，ベクトル場

$$
\boldsymbol{F}=(2xy+z^3,\ \alpha x^2+z,\ \beta xz^2+y)
$$

を考える。以下の問いに答えよ。

(1) 全空間で $\nabla\times\boldsymbol{F}=\boldsymbol{0}$ となる $\alpha,\beta$ を求めよ。

(2) (1) の場合に，$\boldsymbol{F}=\nabla\phi$ かつ $\phi(0,0,0)=0$ を満たすスカラー関数 $\phi$ を求めよ。

(3) (1) の場合に，原点から点 $(1,2,1)$ までの任意の経路に沿う線積分 $\int\boldsymbol{F}\cdot d\boldsymbol{r}$ を求めよ。

---

##解答・解説

### (1)
回転の3成分を計算します。

$$
\begin{aligned}
(\nabla\times\boldsymbol{F})_x&=\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}=1-1=0\\
(\nabla\times\boldsymbol{F})_y&=\frac{\partial F_x}{\partial z}-\frac{\partial F_z}{\partial x}=(3-\beta)z^2\\
(\nabla\times\boldsymbol{F})_z&=\frac{\partial F_y}{\partial x}-\frac{\partial F_x}{\partial y}=2(\alpha-1)x
\end{aligned}
$$

これがすべての点で零になるので，

$$
\finalanswer{\alpha=1},\quad \finalanswer{\beta=3}
$$

となります。

### (2)
全空間で回転が零なので，原点からの線積分は経路によらず，それが $\phi$ になります。原点から $(x,0,0)$，$(x,y,0)$，$(x,y,z)$ の順に座標軸に平行に進む経路を選びます。各区間では1つの座標だけが変わるので，その座標の成分だけを積分します。

$$
\begin{aligned}
\phi(x,y,z)&=\int_0^xF_x(t,0,0)\,dt+\int_0^yF_y(x,t,0)\,dt+\int_0^zF_z(x,y,t)\,dt\\
&=\int_0^x0\,dt+\int_0^yx^2\,dt+\int_0^z(3xt^2+y)\,dt\\
&=0+x^2y+(xz^3+yz)
\end{aligned}
$$

よって，

$$
\finalanswer{\phi=x^2y+xz^3+yz}
$$

となります。偏微分すると $\nabla\phi=(2xy+z^3,\ x^2+z,\ 3xz^2+y)$ となり，$\boldsymbol{F}$ と一致します。

### (3)
$\boldsymbol{F}=\nabla\phi$ のとき，$\boldsymbol{F}\cdot d\boldsymbol{r}=d\phi$ なので，線積分は終点と始点での $\phi$ の差になります。したがって，

$$
\begin{aligned}
\int\boldsymbol{F}\cdot d\boldsymbol{r}&=\phi(1,2,1)-\phi(0,0,0)\\
&=1\cdot 2+1\cdot 1+2\cdot 1\\
&=\finalanswer{5}
\end{aligned}
$$

となります。

===== FILE: 09vector_analysis/03/03_010.md =====
---
tags:
  - 基本
---

# 円筒座標の勾配と発散

## 問題
円筒座標 $(\rho,\varphi,z)$ を $x=\rho\cos\varphi$，$y=\rho\sin\varphi$，$z=z$ で定め，単位ベクトルを

$$
\begin{aligned}
\boldsymbol{e}_\rho&=(\cos\varphi,\ \sin\varphi,\ 0)\\
\boldsymbol{e}_\varphi&=(-\sin\varphi,\ \cos\varphi,\ 0)
\end{aligned}
$$

と $\boldsymbol{e}_z$ とする。$f$ はスカラー場である。以下の問いに答えよ。

(1) 位置ベクトルの微小変化 $d\boldsymbol{r}$ を $d\rho,d\varphi,dz$ と $\boldsymbol{e}_\rho,\boldsymbol{e}_\varphi,\boldsymbol{e}_z$ で表せ。

(2) $df=\nabla f\cdot d\boldsymbol{r}$ を用いて，$\nabla f$ を円筒座標で表せ。

(3) $\boldsymbol{A}=A_\rho(\rho)\boldsymbol{e}_\rho$ の発散 $\nabla\cdot\boldsymbol{A}$ を，(2) で得た $\nabla$ の表式と $\boldsymbol{e}_\rho$ の $\varphi$ 微分を用いて求めよ。

---

## 解答・解説

### (1)
位置ベクトルは $\boldsymbol{r}=\rho\boldsymbol{e}_\rho+z\boldsymbol{e}_z$ と書けます。$\boldsymbol{e}_\rho$ は $\varphi$ に依存し，成分を微分すると $\partial\boldsymbol{e}_\rho/\partial\varphi=\boldsymbol{e}_\varphi$ です。したがって，

$$
\begin{aligned}
d\boldsymbol{r}&=d\rho\,\boldsymbol{e}_\rho+\rho\,d\boldsymbol{e}_\rho+dz\,\boldsymbol{e}_z\\
&=\finalanswer{d\boldsymbol{r}=d\rho\,\boldsymbol{e}_\rho+\rho\,d\varphi\,\boldsymbol{e}_\varphi+dz\,\boldsymbol{e}_z}
\end{aligned}
$$

となります。各座標を変えたときの変位の大きさにかかる係数 $h_\rho=1$，$h_\varphi=\rho$，$h_z=1$ をスケール因子といいます。

### (2)
$\nabla f=G_\rho\boldsymbol{e}_\rho+G_\varphi\boldsymbol{e}_\varphi+G_z\boldsymbol{e}_z$ とおき，(1) との内積をとります。これを全微分と等しいとおくと，

$$
\begin{aligned}
G_\rho\,d\rho+G_\varphi\,\rho\,d\varphi+G_z\,dz&=df\\
&=\frac{\partial f}{\partial\rho}d\rho+\frac{\partial f}{\partial\varphi}d\varphi+\frac{\partial f}{\partial z}dz
\end{aligned}
$$

となります。$d\rho,d\varphi,dz$ は独立なので係数を比べると，

$$
\finalanswer{\nabla f=\frac{\partial f}{\partial\rho}\boldsymbol{e}_\rho+\frac{1}{\rho}\frac{\partial f}{\partial\varphi}\boldsymbol{e}_\varphi+\frac{\partial f}{\partial z}\boldsymbol{e}_z}
$$

となります。$\varphi$ 成分の $1/\rho$ は，スケール因子 $h_\varphi=\rho$ で割ったものです。

### (3)
(2) から $\nabla=\boldsymbol{e}_\rho\partial_\rho+\boldsymbol{e}_\varphi\rho^{-1}\partial_\varphi+\boldsymbol{e}_z\partial_z$ です。微分演算子は $\boldsymbol{e}_\rho$ にも作用し，$\partial_\varphi\boldsymbol{e}_\rho=\boldsymbol{e}_\varphi$，$\partial_\rho\boldsymbol{e}_\rho=\partial_z\boldsymbol{e}_\rho=\boldsymbol{0}$ です。したがって，

$$
\begin{aligned}
\nabla\cdot\boldsymbol{A}&=\boldsymbol{e}_\rho\cdot\frac{\partial}{\partial\rho}(A_\rho\boldsymbol{e}_\rho)+\boldsymbol{e}_\varphi\cdot\frac{1}{\rho}\frac{\partial}{\partial\varphi}(A_\rho\boldsymbol{e}_\rho)\\
&=\frac{dA_\rho}{d\rho}+\frac{A_\rho}{\rho}\\
&=\finalanswer{\nabla\cdot\boldsymbol{A}=\frac{1}{\rho}\frac{d}{d\rho}(\rho A_\rho)}
\end{aligned}
$$

となります。$A_\rho=1/\rho$ のとき発散は零になり，直線電荷のつくる電場は軸の外に湧き出しを持たないことがわかります。

===== FILE: 09vector_analysis/03/03_020.md =====
---
tags:
  - 標準
---

# 球座標のラプラシアン

## 問題
$r=\sqrt{x^2+y^2+z^2}$ とし，$r$ だけの関数 $f(r)$ を考える。$f$ は2回微分可能で，$'$ は $r$ による微分を表す。以下の問いに答えよ。

(1) $r>0$ における $\nabla^2f$ を，直交座標での計算により $f',f'',r$ で表せ。

(2) $r>0$ で $\nabla^2f=0$ を満たす $f(r)$ をすべて求めよ。任意定数は $A,B$ とせよ。

(3) $a>0$，$k>0$ を定数とする。$0\le r<a$ で $\nabla^2u=-k$ を満たし，$r=0$ で有限，$u(a)=0$ となる球対称な $u(r)$ を求めよ。

---

##解答・解説

### (1)
$\partial r/\partial x=x/r$ を用いて，$f$ を $x$ で2回偏微分します。

$$
\begin{aligned}
\frac{\partial f}{\partial x}&=f'\frac{x}{r}\\
\frac{\partial^2f}{\partial x^2}&=f''\frac{x^2}{r^2}+f'\left(\frac{1}{r}-\frac{x^2}{r^3}\right)
\end{aligned}
$$

$y,z$ についても同じ形になるので，3つを足して $x^2+y^2+z^2=r^2$ を使うと，

$$
\begin{aligned}
\nabla^2f&=f''+f'\left(\frac{3}{r}-\frac{1}{r}\right)\\
&=\finalanswer{\nabla^2f=f''+\frac{2}{r}f'}
\end{aligned}
$$

となります。

### (2)
(1) の結果は次のようにまとめられます。

$$
f''+\frac{2}{r}f'=\frac{1}{r^2}\frac{d}{dr}\left(r^2f'\right)
$$

これが零なので $r^2f'$ は定数で，それを $-B$ とおきます。$f'=-B/r^2$ を積分すると，

$$
\finalanswer{f(r)=A+\frac{B}{r}}
$$

となります。$1/r$ は点電荷のポテンシャルの形で，原点以外では調和関数です。

### (3)
(2) と同じまとめ方を使うと，方程式は次のようになります。

$$
\frac{1}{r^2}\frac{d}{dr}\left(r^2u'\right)=-k
$$

両辺に $r^2$ をかけて積分すると，積分定数 $C$ を含む式が得られます。

$$
\begin{aligned}
r^2u'&=-\frac{k}{3}r^3+C\\
u'&=-\frac{k}{3}r+\frac{C}{r^2}
\end{aligned}
$$

$C\neq 0$ だと $u$ は $r\to 0$ で $C/r$ のように発散するので，$C=0$ です。$u'=-kr/3$ を積分して $u(a)=0$ を課すと，

$$
\begin{aligned}
u(r)&=-\frac{k}{6}r^2+D,\quad D=\frac{k}{6}a^2\\
&=\finalanswer{u(r)=\frac{k}{6}\left(a^2-r^2\right)}
\end{aligned}
$$

となります。$u$ は中心で最大値 $ka^2/6$ をとり，一様に帯電した球の内部の電位と同じ形をしています。

===== FILE: 09vector_analysis/03/03_030.md =====
---
tags:
  - 発展
---

# 一般の直交曲線座標

## 問題
直交曲線座標 $(u_1,u_2,u_3)$ を考える。位置ベクトルの微小変化が

$$
d\boldsymbol{r}=h_1\,du_1\,\boldsymbol{e}_1+h_2\,du_2\,\boldsymbol{e}_2+h_3\,du_3\,\boldsymbol{e}_3
$$

と書けるとする。ここで $h_i>0$ はスケール因子，$\boldsymbol{e}_i$ は正規直交な単位ベクトルで $\boldsymbol{e}_1\times\boldsymbol{e}_2=\boldsymbol{e}_3$ を満たす。$\partial_i=\partial/\partial u_i$，$f$ はスカラー場，$\boldsymbol{A}=A_1\boldsymbol{e}_1+A_2\boldsymbol{e}_2+A_3\boldsymbol{e}_3$ とする。ベクトル解析の恒等式は直交座標で示されたものを用いてよい。以下の問いに答えよ。

(1) $df=\nabla f\cdot d\boldsymbol{r}$ を用いて，$\nabla f$ を求めよ。

(2) $\nabla\cdot(\boldsymbol{e}_1/(h_2h_3))=0$ となることを示せ。

(3) (2) を用いて，$\nabla\cdot\boldsymbol{A}$ を求めよ。

(4) $\nabla\times\boldsymbol{A}$ の $\boldsymbol{e}_1$ 成分を求めよ。

---

##解答・解説

### (1)
$\nabla f=\sum_iG_i\boldsymbol{e}_i$ とおくと，$\boldsymbol{e}_i$ が正規直交なので $\nabla f\cdot d\boldsymbol{r}=\sum_iG_ih_i\,du_i$ です。これを $df=\sum_i\partial_if\,du_i$ と比べると $G_ih_i=\partial_if$ なので，

$$
\finalanswer{\nabla f=\frac{1}{h_1}\partial_1f\,\boldsymbol{e}_1+\frac{1}{h_2}\partial_2f\,\boldsymbol{e}_2+\frac{1}{h_3}\partial_3f\,\boldsymbol{e}_3}
$$

となります。特に $f=u_i$ とおくと $\nabla u_i=\boldsymbol{e}_i/h_i$ です。

### (2)
$\nabla u_i=\boldsymbol{e}_i/h_i$ を使うと，$\boldsymbol{e}_1/(h_2h_3)$ は2つの勾配の外積で書けます。

$$
\begin{aligned}
\nabla u_2\times\nabla u_3&=\frac{\boldsymbol{e}_2\times\boldsymbol{e}_3}{h_2h_3}\\
&=\frac{\boldsymbol{e}_1}{h_2h_3}
\end{aligned}
$$

勾配の外積の発散は恒等的に零です。したがって，

$$
\finalanswer{\nabla\cdot\left(\frac{\boldsymbol{e}_1}{h_2h_3}\right)=\nabla\cdot(\nabla u_2\times\nabla u_3)=0}
$$

となります。

### (3)
$A_1\boldsymbol{e}_1=(h_2h_3A_1)\,\boldsymbol{e}_1/(h_2h_3)$ と分け，$\nabla\cdot(\psi\boldsymbol{B})=\nabla\psi\cdot\boldsymbol{B}+\psi\nabla\cdot\boldsymbol{B}$ を使います。(2) により第2項は零なので，(1) を使うと，

$$
\begin{aligned}
\nabla\cdot(A_1\boldsymbol{e}_1)&=\nabla(h_2h_3A_1)\cdot\frac{\boldsymbol{e}_1}{h_2h_3}\\
&=\frac{1}{h_1h_2h_3}\partial_1(h_2h_3A_1)
\end{aligned}
$$

となります。他の成分も添字を巡回させて同じように計算できるので，

$$
\finalanswer{\nabla\cdot\boldsymbol{A}=\frac{1}{h_1h_2h_3}\left[\partial_1(h_2h_3A_1)+\partial_2(h_3h_1A_2)+\partial_3(h_1h_2A_3)\right]}
$$

となります。

### (4)
$A_i\boldsymbol{e}_i=(h_iA_i)\nabla u_i$ と書き，$\nabla\times(\psi\nabla u)=\nabla\psi\times\nabla u$ を使います。この式は勾配の回転が零であることから得られます。$\boldsymbol{e}_1$ 成分を持つのは，$A_2,A_3$ の項で $\boldsymbol{e}_3\times\boldsymbol{e}_2$，$\boldsymbol{e}_2\times\boldsymbol{e}_3$ が現れる部分です。

$$
\begin{aligned}
\nabla(h_2A_2)\times\frac{\boldsymbol{e}_2}{h_2}&\ni\frac{\partial_3(h_2A_2)}{h_3}\frac{\boldsymbol{e}_3\times\boldsymbol{e}_2}{h_2}=-\frac{\partial_3(h_2A_2)}{h_2h_3}\boldsymbol{e}_1\\
\nabla(h_3A_3)\times\frac{\boldsymbol{e}_3}{h_3}&\ni\frac{\partial_2(h_3A_3)}{h_2}\frac{\boldsymbol{e}_2\times\boldsymbol{e}_3}{h_3}=\frac{\partial_2(h_3A_3)}{h_2h_3}\boldsymbol{e}_1
\end{aligned}
$$

$A_1$ の項は $\boldsymbol{e}_1$ との外積なので $\boldsymbol{e}_1$ 成分を持ちません。よって，

$$
\finalanswer{(\nabla\times\boldsymbol{A})_1=\frac{1}{h_2h_3}\left[\partial_2(h_3A_3)-\partial_3(h_2A_2)\right]}
$$

となります。$h_1=h_2=h_3=1$ とおくと，(3) と (4) は直交座標の式と一致します。

===== FILE: 09vector_analysis/03/03_040.md =====
---
tags:
  - 基本
---

# 体積要素と面積要素

## 問題
球座標 $(r,\theta,\varphi)$ を

$$
x=r\sin\theta\cos\varphi,\quad y=r\sin\theta\sin\varphi,\quad z=r\cos\theta
$$

で定める。ただし $r\ge 0$，$0\le\theta\le\pi$，$0\le\varphi<2\pi$ とする。以下の問いに答えよ。

(1) ヤコビアン $\partial(x,y,z)/\partial(r,\theta,\varphi)$ を求めよ。

(2) 半径 $a$ の球面 $r=a$ 上の面積要素 $dS$ を，$\partial\boldsymbol{r}/\partial\theta$ と $\partial\boldsymbol{r}/\partial\varphi$ の外積の大きさから求めよ。

(3) 球面 $r=a$ のうち $0\le\theta\le\alpha$ の部分の面積 $S$ を求めよ。ただし $0<\alpha\le\pi$ とする。

---

##解答・解説

### (1)
ヤコビアンは偏微分を並べた行列式です。

$$
J=\begin{vmatrix}
\sin\theta\cos\varphi & \sin\theta\sin\varphi & \cos\theta\\
r\cos\theta\cos\varphi & r\cos\theta\sin\varphi & -r\sin\theta\\
-r\sin\theta\sin\varphi & r\sin\theta\cos\varphi & 0
\end{vmatrix}
$$

3列目で展開すると，2つの余因子は $r^2\sin\theta\cos\theta$ と $-r\sin^2\theta$ です。したがって，

$$
\begin{aligned}
J&=\cos\theta\cdot r^2\sin\theta\cos\theta+(-r\sin\theta)\cdot(-r\sin^2\theta)\\
&=r^2\sin\theta(\cos^2\theta+\sin^2\theta)\\
&=\finalanswer{J=r^2\sin\theta}
\end{aligned}
$$

となります。体積要素は $dV=r^2\sin\theta\,dr\,d\theta\,d\varphi$ です。

### (2)
$\theta,\varphi$ をそれぞれ $d\theta,d\varphi$ だけ変えると，球面上に2辺が $(\partial\boldsymbol{r}/\partial\theta)d\theta$ と $(\partial\boldsymbol{r}/\partial\varphi)d\varphi$ の平行四辺形ができます。$r=a$ での2つのベクトルとその外積は

$$
\begin{aligned}
\frac{\partial\boldsymbol{r}}{\partial\theta}&=a(\cos\theta\cos\varphi,\ \cos\theta\sin\varphi,\ -\sin\theta)\\
\frac{\partial\boldsymbol{r}}{\partial\varphi}&=a(-\sin\theta\sin\varphi,\ \sin\theta\cos\varphi,\ 0)\\
\frac{\partial\boldsymbol{r}}{\partial\theta}\times\frac{\partial\boldsymbol{r}}{\partial\varphi}&=a^2\sin\theta(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)
\end{aligned}
$$

です。括弧内は単位ベクトル $\boldsymbol{e}_r$ なので，外積の大きさは $a^2\sin\theta$ です。よって，

$$
\finalanswer{dS=a^2\sin\theta\,d\theta\,d\varphi}
$$

となります。

### (3)
(2) の面積要素を $\theta$ は $0$ から $\alpha$ まで，$\varphi$ は $0$ から $2\pi$ まで積分すると，

$$
\begin{aligned}
S&=\int_0^{2\pi}d\varphi\int_0^\alpha a^2\sin\theta\,d\theta\\
&=2\pi a^2\Bigl[-\cos\theta\Bigr]_0^\alpha\\
&=\finalanswer{S=2\pi a^2(1-\cos\alpha)}
\end{aligned}
$$

となります。$\alpha=\pi$ とすると球の表面積 $4\pi a^2$ と一致します。

===== FILE: 09vector_analysis/04/04_010.md =====
---
tags:
  - 基本
---

# 線積分

## 問題
$xy$ 平面内で，質点に力

$$
\boldsymbol{F}=k(-y\,\boldsymbol{e}_x+x\,\boldsymbol{e}_y)
$$

がはたらく。$k$ は正の定数である。$a>0$ として，点 $\mathrm{A}(a,0)$ から点 $\mathrm{B}(0,a)$ まで質点を動かすときに力がする仕事を考える（図）。以下の問いに答えよ。

<!-- FIGURE problem: xy 平面。原点 O，x 軸上の点 A(a,0)，y 軸上の点 B(0,a) を描く。A から B へ，原点中心・半径 a の反時計回りの四分円弧を C1 とラベルし，A と B を結ぶ線分を C2 とラベルする。どちらも A から B への向きの矢印を付ける。力の矢印は描かない。 -->

(1) 原点を中心とする半径 $a$ の円弧に沿って反時計回りに動かすときの仕事 $W_1$ を求めよ。

(2) 線分 AB に沿って動かすときの仕事 $W_2$ を求めよ。

(3) 原点を中心とする半径 $a$ の円周に沿って，A から反時計回りに1周するときの仕事 $W_3$ を求めよ。

---

##解答・解説

### (1)
円弧を $\boldsymbol{r}=(a\cos t,\ a\sin t)$，$0\le t\le\pi/2$ と媒介変数で表します。$d\boldsymbol{r}=(-a\sin t,\ a\cos t)\,dt$ で，円弧上の力は $\boldsymbol{F}=ka(-\sin t,\ \cos t)$ です。仕事 $\int\boldsymbol{F}\cdot d\boldsymbol{r}$ を計算すると，

$$
\begin{aligned}
W_1&=\int_0^{\pi/2}ka^2(\sin^2t+\cos^2t)\,dt\\
&=\finalanswer{W_1=\frac{\pi}{2}ka^2}
\end{aligned}
$$

となります。円周上では力が接線方向を向き，大きさが一定の $ka$ なので，仕事は力の大きさと弧の長さ $\pi a/2$ の積になっています。

### (2)
線分を $\boldsymbol{r}=(a(1-t),\ at)$，$0\le t\le 1$ と表すと，$d\boldsymbol{r}=(-a,\ a)\,dt$ です。線分上の力は $\boldsymbol{F}=k(-at,\ a(1-t))$ なので，

$$
\begin{aligned}
\boldsymbol{F}\cdot d\boldsymbol{r}&=k\left[(-at)(-a)+a(1-t)a\right]dt\\
&=ka^2\,dt
\end{aligned}
$$

となります。これを $0$ から $1$ まで積分すると，

$$
\finalanswer{W_2=ka^2}
$$

となります。

### (3)
(1) と同じ媒介変数表示で $t$ を $0$ から $2\pi$ まで動かすと，被積分関数は (1) と同じ $ka^2$ です。よって，

$$
\begin{aligned}
W_3&=\int_0^{2\pi}ka^2\,dt\\
&=\finalanswer{W_3=2\pi ka^2}
\end{aligned}
$$

となります。$W_1\neq W_2$ で，閉じた経路を1周する仕事も零でないので，この力は保存力ではありません。実際，$\nabla\times\boldsymbol{F}=2k\boldsymbol{e}_z\neq\boldsymbol{0}$ です。

===== FILE: 09vector_analysis/04/04_020.md =====
---
tags:
  - 標準
---

# 経路によらない線積分

## 問題
$\alpha$ を定数として，ベクトル場

$$
\boldsymbol{F}=(y^2,\ 2xy+z,\ \alpha y)
$$

を考える。原点 O から点 $\mathrm{P}(1,1,1)$ までの線積分 $\int\boldsymbol{F}\cdot d\boldsymbol{r}$ について，以下の問いに答えよ。

(1) $\nabla\times\boldsymbol{F}$ を求めよ。

(2) 線分 OP に沿う線積分 $I_1$ を求めよ。

(3) O から $(1,0,0)$，$(1,1,0)$ を順に通って P に至る，座標軸に平行な線分をつないだ経路に沿う線積分 $I_2$ を求めよ。

---

##解答・解説

### (1)
回転の3成分を計算します。

$$
\begin{aligned}
(\nabla\times\boldsymbol{F})_x&=\frac{\partial(\alpha y)}{\partial y}-\frac{\partial(2xy+z)}{\partial z}=\alpha-1\\
(\nabla\times\boldsymbol{F})_y&=\frac{\partial(y^2)}{\partial z}-\frac{\partial(\alpha y)}{\partial x}=0\\
(\nabla\times\boldsymbol{F})_z&=\frac{\partial(2xy+z)}{\partial x}-\frac{\partial(y^2)}{\partial y}=2y-2y=0
\end{aligned}
$$

よって，

$$
\finalanswer{\nabla\times\boldsymbol{F}=(\alpha-1)\boldsymbol{e}_x}
$$

となります。全空間で回転が零になるのは $\alpha=1$ のときだけです。

### (2)
線分を $\boldsymbol{r}=(t,t,t)$，$0\le t\le 1$ と表すと，$d\boldsymbol{r}=(1,1,1)\,dt$ です。$\boldsymbol{F}$ に代入して内積をとると，

$$
\begin{aligned}
\boldsymbol{F}\cdot d\boldsymbol{r}&=(t^2+2t^2+t+\alpha t)\,dt\\
&=\left[3t^2+(1+\alpha)t\right]dt
\end{aligned}
$$

となります。$0$ から $1$ まで積分すると，

$$
\begin{aligned}
I_1&=\Bigl[t^3+\frac{1+\alpha}{2}t^2\Bigr]_0^1\\
&=\finalanswer{I_1=\frac{3+\alpha}{2}}
\end{aligned}
$$

となります。

### (3)
各区間では1つの座標だけが変わるので，その座標の成分だけを積分します。O から $(1,0,0)$ では $y=z=0$ なので $F_x=0$ です。$(1,0,0)$ から $(1,1,0)$ では $x=1$，$z=0$ なので $F_y=2y$ です。$(1,1,0)$ から P では $x=y=1$ なので $F_z=\alpha$ です。したがって，

$$
\begin{aligned}
I_2&=\int_0^10\,dx+\int_0^12y\,dy+\int_0^1\alpha\,dz\\
&=0+1+\alpha\\
&=\finalanswer{I_2=1+\alpha}
\end{aligned}
$$

となります。差は $I_2-I_1=(\alpha-1)/2$ で，$I_1=I_2$ となるのは (1) で回転が零になる $\alpha=1$ のときに限られます。このとき $\boldsymbol{F}=\nabla(xy^2+yz)$ で，どちらの積分も $\phi(\mathrm{P})-\phi(\mathrm{O})=2$ と一致します。

===== FILE: 09vector_analysis/04/04_030.md =====
---
tags:
  - 基本
---

# 面積分と流束

## 問題
原点を中心とする半径 $a$ の球面 $S$ と，その外向き単位法線ベクトル $\boldsymbol{n}$ を考える。ベクトル場 $\boldsymbol{A}$ の流束を

$$
\Phi=\int_S\boldsymbol{A}\cdot\boldsymbol{n}\,dS
$$

で定める。位置ベクトルを $\boldsymbol{r}=(x,y,z)$，$r=|\boldsymbol{r}|$ とし，球座標 $(r,\theta,\varphi)$ を用いてよい。以下の問いに答えよ。

(1) $\boldsymbol{A}=\boldsymbol{r}$ のとき，$\Phi$ を求めよ。

(2) $\boldsymbol{A}=z\,\boldsymbol{e}_z$ のとき，$\Phi$ を求めよ。

(3) $\boldsymbol{A}=\boldsymbol{r}/r^3$ のとき，$\Phi$ を求めよ。

---

##解答・解説

### (1)
球面上では $\boldsymbol{n}=\boldsymbol{r}/a$ で，面積要素は $dS=a^2\sin\theta\,d\theta\,d\varphi$ です。$\boldsymbol{A}\cdot\boldsymbol{n}=r^2/a=a$ となり球面上で一定なので，

$$
\begin{aligned}
\Phi&=\int_0^{2\pi}d\varphi\int_0^\pi a\cdot a^2\sin\theta\,d\theta\\
&=a^3\cdot 2\pi\cdot 2\\
&=\finalanswer{\Phi=4\pi a^3}
\end{aligned}
$$

となります。$\nabla\cdot\boldsymbol{r}=3$ に球の体積 $4\pi a^3/3$ をかけた値と一致します。

### (2)
$\boldsymbol{e}_z\cdot\boldsymbol{n}=z/a$ なので，球面上で $z=a\cos\theta$ を使うと次のようになります。

$$
\begin{aligned}
\boldsymbol{A}\cdot\boldsymbol{n}&=\frac{z^2}{a}\\
&=a\cos^2\theta
\end{aligned}
$$

$\theta$ の積分は $u=\cos\theta$ と置換します。$du=-\sin\theta\,d\theta$ で，$\theta:0\to\pi$ は $u:1\to -1$ に対応するので，

$$
\begin{aligned}
\Phi&=a^3\int_0^{2\pi}d\varphi\int_0^\pi\cos^2\theta\sin\theta\,d\theta\\
&=2\pi a^3\int_{-1}^{1}u^2\,du\\
&=2\pi a^3\cdot\frac{2}{3}\\
&=\finalanswer{\Phi=\frac{4}{3}\pi a^3}
\end{aligned}
$$

となります。$\nabla\cdot(z\boldsymbol{e}_z)=1$ なので，流束は球の体積と一致します。

### (3)
球面上では $\boldsymbol{A}\cdot\boldsymbol{n}=(\boldsymbol{r}\cdot\boldsymbol{r})/(a\cdot a^3)=1/a^2$ で一定です。したがって，

$$
\begin{aligned}
\Phi&=\frac{1}{a^2}\int_0^{2\pi}d\varphi\int_0^\pi a^2\sin\theta\,d\theta\\
&=\finalanswer{\Phi=4\pi}
\end{aligned}
$$

となります。流束は半径 $a$ によりません。$\boldsymbol{r}/r^3$ は原点以外で発散が零なので，湧き出しは原点に集中していて，それを囲む球面の大きさに関係なく同じ流束が出ていきます。

===== FILE: 09vector_analysis/04/04_040.md =====
---
tags:
  - 標準
---

# 立体角

## 問題
$xy$ 平面上にある，原点 O を中心とする半径 $a$ の円板 $D$ と，$z$ 軸上の点 $\mathrm{P}(0,0,h)$ を考える。ただし $h>0$ である（図）。円板上の点 Q に対し $\boldsymbol{R}=\overrightarrow{\mathrm{PQ}}$，$R=|\boldsymbol{R}|$，$\boldsymbol{n}=-\boldsymbol{e}_z$ として，円板が点 P に張る立体角を

$$
\Omega=\int_D\frac{\boldsymbol{R}\cdot\boldsymbol{n}}{R^3}\,dS
$$

で定める。以下の問いに答えよ。

<!-- FIGURE problem: 3次元の見取り図。xy 平面上に原点 O を中心とする半径 a の円板を斜めから見た楕円として描き，半径に a のラベルを付ける。z 軸上の O の上方に点 P を置き，OP の長さを h とラベルする。円板上の一点 Q と P を線分で結ぶ。円板の下向きに単位法線 n の矢印を描く。 -->

(1) 円板のうち，中心からの距離が $\rho$ と $\rho+d\rho$ の間にある細い円環が P に張る立体角 $d\Omega$ を求めよ。

(2) 立体角 $\Omega$ を求めよ。

(3) $h\gg a$ のとき，$\Omega$ の $a/h$ についての主要項を求めよ。

---

##解答・解説

### (1)
中心から距離 $\rho$ の点 Q は $(\rho\cos\varphi,\ \rho\sin\varphi,\ 0)$ と書けます。$\boldsymbol{R}=(\rho\cos\varphi,\ \rho\sin\varphi,\ -h)$ なので，$\boldsymbol{R}\cdot\boldsymbol{n}=h$，$R=\sqrt{h^2+\rho^2}$ です。被積分関数は円環上で一定なので，円環の面積 $2\pi\rho\,d\rho$ をかけると，

$$
\finalanswer{d\Omega=\frac{2\pi h\rho\,d\rho}{(h^2+\rho^2)^{3/2}}}
$$

となります。

### (2)
(1) を $\rho$ について $0$ から $a$ まで積分します。$u=h^2+\rho^2$ と置換すると $du=2\rho\,d\rho$ となるので，

$$
\begin{aligned}
\Omega&=2\pi h\int_0^a\frac{\rho\,d\rho}{(h^2+\rho^2)^{3/2}}\\
&=\pi h\int_{h^2}^{h^2+a^2}u^{-3/2}\,du\\
&=\pi h\Bigl[-2u^{-1/2}\Bigr]_{h^2}^{h^2+a^2}\\
&=2\pi h\left(\frac{1}{h}-\frac{1}{\sqrt{h^2+a^2}}\right)\\
&=\finalanswer{\Omega=2\pi\left(1-\frac{h}{\sqrt{h^2+a^2}}\right)}
\end{aligned}
$$

となります。P から円板の縁を見込む半頂角を $\alpha$ とすると $\cos\alpha=h/\sqrt{h^2+a^2}$ なので，$\Omega=2\pi(1-\cos\alpha)$ と書けます。これは単位球面上の球冠の面積と一致します。$h\to 0$ では $\Omega\to 2\pi$ で，円板が P から見て半空間を覆います。

### (3)
$h\gg a$ では $a^2/h^2\ll 1$ なので，$(1+x)^{-1/2}\approx 1-x/2$ を $x=a^2/h^2$ として使います。

$$
\begin{aligned}
\frac{h}{\sqrt{h^2+a^2}}&=\left(1+\frac{a^2}{h^2}\right)^{-1/2}\\
&\approx 1-\frac{a^2}{2h^2}
\end{aligned}
$$

これを (2) に代入すると，

$$
\begin{aligned}
\Omega&\approx 2\pi\cdot\frac{a^2}{2h^2}\\
&=\finalanswer{\Omega\approx\frac{\pi a^2}{h^2}}
\end{aligned}
$$

となります。遠方から見ると，立体角は円板の面積 $\pi a^2$ を距離の2乗で割ったものになります。

===== END =====