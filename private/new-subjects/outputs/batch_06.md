===== FILE: 08differential_equations/01/01_010.md =====
---
tags:
  - 基本
---

# 変数分離形

## 問題
放射性原子核の数 $N(t)$ は，崩壊定数 $\lambda>0$ を用いて

$$
\frac{dN}{dt}=-\lambda N
$$

に従い，$N(0)=N_0$ である。また，温度 $T_\mathrm{a}$ が一定の環境に置かれた物体の温度 $T(t)$ は，定数 $k>0$ を用いて

$$
\frac{dT}{dt}=-k(T-T_\mathrm{a})
$$

に従い，$T(0)=T_1$ である。以下の問いに答えよ。

(1) $N(t)$ を求めよ。

(2) $N$ が $N_0/2$ になる時刻 $t_{1/2}$ を求めよ。

(3) (1) の結果を用いて，$T(t)$ を求めよ。

---

## 解答・解説

### (1)
$N\neq0$ として両辺を $N$ で割り，左辺に $N$ だけ，右辺に $t$ だけが現れるように変数を分けます。

$$
\frac{dN}{N}=-\lambda\,dt
$$

両辺を積分すると，$C$ を積分定数として

$$
\begin{aligned}
\int\frac{dN}{N}&=-\lambda\int dt\\
\ln|N|&=-\lambda t+C
\end{aligned}
$$

となります。$|N|=e^{C}e^{-\lambda t}$ なので，$A=\pm e^{C}$ と置くと $N=Ae^{-\lambda t}$ です。割り算のときに除いた $N\equiv0$ も解であり，これは $A=0$ の場合に含まれます。$t=0$ を代入すると $A=N_0$ なので，

$$
\finalanswer{N(t)=N_0e^{-\lambda t}}
$$

となります。

### (2)
条件 $N(t_{1/2})=N_0/2$ に (1) の結果を代入します。

$$
\begin{aligned}
N_0e^{-\lambda t_{1/2}}&=\frac{N_0}{2}\\
e^{\lambda t_{1/2}}&=2
\end{aligned}
$$

両辺の自然対数をとると，

$$
\finalanswer{t_{1/2}=\frac{\ln2}{\lambda}}
$$

となります。半減期は $N_0$ によらないので，どの時刻から測っても $N$ が半分になるまでの時間は同じです。

### (3)
周囲の温度との差 $u=T-T_\mathrm{a}$ を新しい未知関数にとります。$T_\mathrm{a}$ は定数なので $du/dt=dT/dt$ であり，

$$
\frac{du}{dt}=-ku,\quad u(0)=T_1-T_\mathrm{a}
$$

となります。これは (1) の方程式で $\lambda$ を $k$ に，$N_0$ を $T_1-T_\mathrm{a}$ に置き換えたものです。したがって，(1) の結果から

$$
u(t)=(T_1-T_\mathrm{a})e^{-kt}
$$

です。$T=T_\mathrm{a}+u$ に戻すと，

$$
\finalanswer{T(t)=T_\mathrm{a}+(T_1-T_\mathrm{a})e^{-kt}}
$$

となります。$t=0$ で $T_1$ と一致し，$t\to\infty$ で $T_\mathrm{a}$ に近づきます。温度差は時間 $\ln2/k$ ごとに半分になります。

===== FILE: 08differential_equations/01/01_020.md =====
---
tags:
  - 基本
---

# 同次形

## 問題
$x>0$，$y>0$ の範囲で，微分方程式

$$
\frac{dy}{dx}=\frac{x^2+y^2}{2xy}
$$

を考える。以下の問いに答えよ。

(1) $u=y/x$ と置くとき，$u$ が満たす微分方程式を求めよ。

(2) もとの方程式の一般解を求めよ。

(3) 初期条件 $y(1)=2$ を満たす解を求めよ。

---

## 解答・解説

### (1)
右辺の分子と分母を $x^2$ で割ると，$u$ だけの関数になります。

$$
\frac{x^2+y^2}{2xy}=\frac{1+u^2}{2u}
$$

一方，$y=ux$ を積の微分法で微分すると $dy/dx=u+x\,du/dx$ です。これらをもとの方程式に代入すると，

$$
u+x\frac{du}{dx}=\frac{1+u^2}{2u}
$$

となります。左辺の $u$ を右辺に移すと，

$$
\finalanswer{x\frac{du}{dx}=\frac{1-u^2}{2u}}
$$

となります。右辺に $x$ が含まれないので，この式は変数分離形です。

### (2)
$u^2\neq1$ として，左辺に $u$，右辺に $x$ を集めます。

$$
\frac{2u}{1-u^2}\,du=\frac{dx}{x}
$$

左辺の積分は $w=1-u^2$ と置くと $dw=-2u\,du$ なので，

$$
\begin{aligned}
\int\frac{2u}{1-u^2}\,du&=-\int\frac{dw}{w}\\
&=-\ln|1-u^2|
\end{aligned}
$$

となります。右辺の積分は $x>0$ より $\ln x$ です。$C_1$ を積分定数とすると，

$$
\begin{aligned}
-\ln|1-u^2|&=\ln x+C_1\\
|1-u^2|&=\frac{e^{-C_1}}{x}
\end{aligned}
$$

です。$C=\pm e^{-C_1}$ と置くと $1-u^2=C/x$ となります。除いておいた $u\equiv1$ も (1) の方程式を満たし，これは $C=0$ に対応します。$u=y/x$ を代入して両辺に $x^2$ を掛けると，

$$
\finalanswer{x^2-y^2=Cx}
$$

となります。$C$ は任意の定数です。$C\neq0$ の解曲線は，中心が $(C/2,0)$ の直角双曲線です。

### (3)
一般解に $x=1$，$y=2$ を代入すると $1-4=C$ なので，$C=-3$ です。このとき $y^2=x^2+3x$ であり，$y>0$ より

$$
\finalanswer{y=\sqrt{x^2+3x}}
$$

となります。検算のため，左辺と右辺をそれぞれ計算すると，

$$
\begin{aligned}
\frac{dy}{dx}&=\frac{2x+3}{2\sqrt{x^2+3x}}\\
\frac{x^2+y^2}{2xy}&=\frac{2x^2+3x}{2x\sqrt{x^2+3x}}=\frac{2x+3}{2\sqrt{x^2+3x}}
\end{aligned}
$$

となり，両者は一致します。

===== FILE: 08differential_equations/01/01_030.md =====
---
tags:
  - 基本
---

# 1階線形微分方程式

## 問題
$x>0$ で，微分方程式

$$
\frac{dy}{dx}-\frac{2y}{x}=x^2\cos x
$$

を考える。以下の問いに答えよ。

(1) 右辺を0とした方程式の一般解を求めよ。

(2) 定数変化法を用いて，もとの方程式の一般解を求めよ。

(3) 初期条件 $y(\pi/2)=0$ を満たす解を求めよ。

---

## 解答・解説

### (1)
$dy/dx=2y/x$ は変数分離形なので，$y\neq0$ として変数を分けて積分します。

$$
\begin{aligned}
\int\frac{dy}{y}&=\int\frac{2}{x}\,dx\\
\ln|y|&=2\ln x+C_1
\end{aligned}
$$

$C=\pm e^{C_1}$ と置き，$y\equiv0$ も $C=0$ として含めると，

$$
\finalanswer{y=Cx^2}
$$

となります。$C$ は任意の定数です。

### (2)
(1) の定数 $C$ を $x$ の関数 $v(x)$ に置き換えて，$y=v(x)x^2$ と置きます。積の微分法から

$$
\frac{dy}{dx}=v'x^2+2vx
$$

です。これをもとの方程式の左辺に代入すると，

$$
\begin{aligned}
\frac{dy}{dx}-\frac{2y}{x}&=v'x^2+2vx-2vx\\
&=v'x^2
\end{aligned}
$$

となり，$v$ を含む項が打ち消し合います。これが右辺 $x^2\cos x$ に等しいので $v'=\cos x$ であり，$C$ を積分定数として $v=\sin x+C$ です。したがって，

$$
\finalanswer{y=x^2(\sin x+C)}
$$

となります。この計算は，方程式全体を $x^2$ で割ると左辺が次のようにまとまることと同じです。

$$
\frac{d}{dx}\left(\frac{y}{x^2}\right)=\frac{1}{x^2}\left(\frac{dy}{dx}-\frac{2y}{x}\right)
$$

つまり $1/x^2$ が積分因子になっています。

### (3)
一般解に $x=\pi/2$ を代入すると，$\sin(\pi/2)=1$ より

$$
\frac{\pi^2}{4}(1+C)=0
$$

なので $C=-1$ です。よって，

$$
\finalanswer{y=x^2(\sin x-1)}
$$

となります。$\sin x\le1$ なので，この解はつねに $y\le0$ です。

===== FILE: 08differential_equations/01/01_040.md =====
---
tags:
  - 標準
---

# ベルヌーイ型

## 問題
個体数 $N(t)$ が，正の定数 $r$，$K$ を用いて

$$
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
$$

に従い，$N(0)=N_0$ ($0<N_0<K$) とする。以下の問いに答えよ。

(1) $u=1/N$ と置くとき，$u$ が満たす微分方程式を求めよ。

(2) $N(t)$ を求めよ。

(3) $N_0<K/2$ のとき，$dN/dt$ が最大となる時刻 $t^*$ を求めよ。

---

## 解答・解説

### (1)
方程式は $dN/dt-rN=-(r/K)N^2$ と書け，$N^2$ の項を含むベルヌーイ型です。$u=N^{-1}$ を $t$ で微分し，もとの方程式を代入します。

$$
\begin{aligned}
\frac{du}{dt}&=-\frac{1}{N^2}\frac{dN}{dt}\\
&=-\frac{1}{N^2}\left(rN-\frac{r}{K}N^2\right)\\
&=-\frac{r}{N}+\frac{r}{K}
\end{aligned}
$$

$1/N=u$ なので，

$$
\finalanswer{\frac{du}{dt}+ru=\frac{r}{K}}
$$

となります。非線形の方程式が，$u$ についての1階線形方程式になりました。

### (2)
(1) の方程式の右辺を0とした方程式の一般解は $Ce^{-rt}$ で，定数の特解は $u=1/K$ です。初期条件 $u(0)=1/N_0$ から $C=1/N_0-1/K$ と決まるので，

$$
\begin{aligned}
u(t)&=\frac{1}{K}+\left(\frac{1}{N_0}-\frac{1}{K}\right)e^{-rt}\\
&=\frac{N_0+(K-N_0)e^{-rt}}{KN_0}
\end{aligned}
$$

となります。$N=1/u$ より，

$$
\finalanswer{N(t)=\frac{KN_0}{N_0+(K-N_0)e^{-rt}}}
$$

です。$t=0$ で $N_0$ と一致し，$t\to\infty$ で $K$ に近づきます。

### (3)
$dN/dt=rN(1-N/K)$ は $N$ の2次関数で，$N=K/2$ で最大になります。$0<N<K$ では $dN/dt>0$ なので $N$ は単調に増加し，$N_0<K/2$ ならば $N=K/2$ となる時刻がちょうど1つあります。(2) の結果を $N(t^*)=K/2$ に代入すると，

$$
\begin{aligned}
\frac{KN_0}{N_0+(K-N_0)e^{-rt^*}}&=\frac{K}{2}\\
2N_0&=N_0+(K-N_0)e^{-rt^*}\\
e^{-rt^*}&=\frac{N_0}{K-N_0}
\end{aligned}
$$

となります。対数をとると，

$$
\finalanswer{t^*=\frac{1}{r}\ln\frac{K-N_0}{N_0}}
$$

です。$K-N_0>N_0$ なので $t^*>0$ です。$N(t)$ のグラフを図に示します。

<!-- FIGURE solution (3): 横軸 t，縦軸 N，原点 O。縦軸上の N_0（K/2 より下）から出発して単調に増加し，水平な点線 N=K に漸近する S 字形の曲線を実線で描く。縦軸に K/2 の目盛りを付け，曲線が N=K/2 を横切る点（変曲点）に黒丸を打ち，その横軸の位置に t^* とラベルを付ける。 -->

===== FILE: 08differential_equations/01/01_050.md =====
---
tags:
  - 標準
---

# 完全微分方程式と積分因子

## 問題
$x>0$ で，微分方程式

$$
(x^2+y^2+x)\,dx+xy\,dy=0
$$

を考える。以下の問いに答えよ。

(1) 両辺に $x$ だけの関数 $\mu(x)$ を掛けて完全微分形にする。$\mu(1)=1$ となる $\mu(x)$ を求めよ。

(2) 一般解を，$C$ を任意定数として $F(x,y)=C$ の形で求めよ。

---

## 解答・解説

### (1)
$M=x^2+y^2+x$，$N=xy$ と置きます。$M\,dx+N\,dy=0$ が完全微分形となる条件は $\partial M/\partial y=\partial N/\partial x$ ですが，左辺は $2y$，右辺は $y$ なので，このままでは完全微分形ではありません。$\mu M$，$\mu N$ について同じ条件を課すと，$\mu$ は $x$ だけの関数なので

$$
\begin{aligned}
\frac{\partial(\mu M)}{\partial y}&=\frac{\partial(\mu N)}{\partial x}\\
\mu\frac{\partial M}{\partial y}&=\frac{d\mu}{dx}N+\mu\frac{\partial N}{\partial x}
\end{aligned}
$$

となります。$d\mu/dx$ について解き，$M$，$N$ を代入すると，

$$
\begin{aligned}
\frac{1}{\mu}\frac{d\mu}{dx}&=\frac{1}{N}\left(\frac{\partial M}{\partial y}-\frac{\partial N}{\partial x}\right)\\
&=\frac{2y-y}{xy}\\
&=\frac{1}{x}
\end{aligned}
$$

です。右辺が $y$ を含まないので，$x$ だけの積分因子が存在します。積分すると $\ln|\mu|=\ln x+c$ となり，$\mu(1)=1$ より

$$
\finalanswer{\mu(x)=x}
$$

となります。

### (2)
$\mu=x$ を掛けた方程式は

$$
(x^3+xy^2+x^2)\,dx+x^2y\,dy=0
$$

です。$dx$ の係数の $y$ 微分と $dy$ の係数の $x$ 微分はどちらも $2xy$ となり，完全微分形になっています。そこで $\partial F/\partial x=x^3+xy^2+x^2$，$\partial F/\partial y=x^2y$ を満たす $F$ を探します。後者を $y$ で積分すると，$g(x)$ を $x$ だけの関数として

$$
F=\frac{x^2y^2}{2}+g(x)
$$

です。これを $x$ で微分したものが前者と等しいことから，

$$
\begin{aligned}
xy^2+g'(x)&=x^3+xy^2+x^2\\
g'(x)&=x^3+x^2\\
g(x)&=\frac{x^4}{4}+\frac{x^3}{3}
\end{aligned}
$$

となります。解は $F=$ 一定で与えられ，全体を12倍して定数をあらためて $C$ と書くと，

$$
\finalanswer{3x^4+4x^3+6x^2y^2=C}
$$

となります。検算として左辺の全微分をとると $12x\{(x^2+y^2+x)\,dx+xy\,dy\}$ となり，もとの方程式の左辺の $12\mu$ 倍と一致します。

===== FILE: 08differential_equations/01/01_060.md =====
---
tags:
  - 発展
---

# 解の存在と一意性

## 問題
$x\ge0$ の範囲で，初期値問題

$$
\frac{dy}{dx}=2\sqrt{|y|},\quad y(0)=0
$$

を考える。$y\equiv0$ はこの初期値問題の解である。$f(y)=2\sqrt{|y|}$ と置く。以下の問いに答えよ。

(1) $x>0$ で $y>0$ となる解を求めよ。

(2) $y=0$ を含むどんな区間でも，すべての $y_1$，$y_2$ に対して

$$
|f(y_1)-f(y_2)|\le L|y_1-y_2|
$$

を満たす定数 $L$ は存在しないことを示せ。

(3) $\delta>0$ とする。$y_1\ge\delta$，$y_2\ge\delta$ であるすべての $y_1$，$y_2$ について (2) の不等式が成り立つような $L$ の最小値を求めよ。

---

## 解答・解説

### (1)
$y>0$ では $|y|=y$ なので，変数を分けて積分します。

$$
\begin{aligned}
\int\frac{dy}{2\sqrt{y}}&=\int dx\\
\sqrt{y}&=x+C
\end{aligned}
$$

$x\to+0$ で $y\to0$ となるには $C=0$ が必要です。$C<0$ では小さい $x$ で右辺が負になり，$C>0$ では初期条件を満たしません。したがって，

$$
\finalanswer{y=x^2}
$$

となります。実際 $y'=2x=2\sqrt{x^2}$ です。さらに，任意の $a>0$ に対して，$0\le x\le a$ で $y=0$，$x>a$ で $y=(x-a)^2$ とつないだ関数も微分可能な解になります。同じ初期条件から無数の解が出るので，一意性が崩れています。

### (2)
$0$ と，区間内の $0$ に近い点 $h\neq0$ をとり，2点での差の比を計算します。

$$
\frac{|f(h)-f(0)|}{|h-0|}=\frac{2\sqrt{|h|}}{|h|}=\frac{2}{\sqrt{|h|}}
$$

$h\to0$ とすると，

$$
\finalanswer{\lim_{h\to0}\frac{|f(h)-f(0)|}{|h|}=\infty}
$$

となります。不等式を満たす $L$ があれば，この比はつねに $L$ 以下でなければなりません。比はいくらでも大きくなるので，そのような $L$ は存在しません。$f$ のグラフの傾き $1/\sqrt{y}$ が $y\to+0$ で発散することが原因です。リプシッツ条件は解の一意性を保証する条件なので，それが破れている点 $y=0$ から (1) のように複数の解が出ます。

### (3)
$y_1>y_2\ge\delta$ として，差の比を因数分解で簡単にします。

$$
\begin{aligned}
\frac{f(y_1)-f(y_2)}{y_1-y_2}&=\frac{2(\sqrt{y_1}-\sqrt{y_2})}{(\sqrt{y_1}-\sqrt{y_2})(\sqrt{y_1}+\sqrt{y_2})}\\
&=\frac{2}{\sqrt{y_1}+\sqrt{y_2}}
\end{aligned}
$$

$y_1>\delta$ より $\sqrt{y_1}+\sqrt{y_2}>2\sqrt{\delta}$ なので，比はつねに $1/\sqrt{\delta}$ より小さく，$L=1/\sqrt{\delta}$ で不等式が成り立ちます。逆に $y_2=\delta$ として $y_1\to\delta$ とすると比は $1/\sqrt{\delta}$ に近づくので，$L<1/\sqrt{\delta}$ では不等式が破れます。よって，

$$
\finalanswer{L_{\min}=\frac{1}{\sqrt{\delta}}}
$$

となります。$\delta\to0$ で発散し，(2) の結果と一致します。初期値が $y(0)=y_0>0$ ならリプシッツ条件が成り立つので，解は $y=(x+\sqrt{y_0})^2$ だけです。

===== FILE: 08differential_equations/02/02_010.md =====
---
tags:
  - 基本
---

# 定数係数の同次方程式

## 問題
変位 $x(t)$ が，正の定数 $\gamma$，$\omega_0$ を用いて

$$
\ddot{x}+2\gamma\dot{x}+\omega_0^2x=0
$$

に従い，初期条件は $x(0)=x_0$，$\dot{x}(0)=0$ である。以下の問いに答えよ。

(1) $\gamma<\omega_0$ のとき，$\omega_1=\sqrt{\omega_0^2-\gamma^2}$ を用いて $x(t)$ を求めよ。

(2) $\gamma=\omega_0$ のとき，$x(t)$ を求めよ。

(3) $\gamma>\omega_0$ のとき，$\kappa=\sqrt{\gamma^2-\omega_0^2}$ を用いて $x(t)$ を求めよ。

---

## 解答・解説

### (1)
$x=e^{\lambda t}$ を代入すると，$\lambda$ が満たす特性方程式とその解が得られます。

$$
\begin{aligned}
\lambda^2+2\gamma\lambda+\omega_0^2&=0\\
\lambda&=-\gamma\pm\sqrt{\gamma^2-\omega_0^2}
\end{aligned}
$$

$\gamma<\omega_0$ では $\lambda=-\gamma\pm i\omega_1$ と複素数になります。オイラーの公式で $e^{\pm i\omega_1t}$ を三角関数に直すと，$A$，$B$ を実定数として一般解は

$$
x=e^{-\gamma t}(A\cos\omega_1t+B\sin\omega_1t)
$$

です。$x(0)=A$，$\dot{x}(0)=-\gamma A+\omega_1B$ なので，初期条件から $A=x_0$，$B=\gamma x_0/\omega_1$ となります。よって，

$$
\finalanswer{x(t)=x_0e^{-\gamma t}\left(\cos\omega_1t+\frac{\gamma}{\omega_1}\sin\omega_1t\right)}
$$

です。振幅が $e^{-\gamma t}$ で減衰しながら振動します。

### (2)
$\gamma=\omega_0$ では特性方程式が重解 $\lambda=-\gamma$ をもち，$e^{-\gamma t}$ しか得られません。このとき方程式は $(d/dt+\gamma)^2x=0$ と書け，$te^{-\gamma t}$ も解になります。

$$
\begin{aligned}
\left(\frac{d}{dt}+\gamma\right)^2(te^{-\gamma t})&=\left(\frac{d}{dt}+\gamma\right)e^{-\gamma t}\\
&=0
\end{aligned}
$$

一般解は $x=(A+Bt)e^{-\gamma t}$ です。$x(0)=A=x_0$，$\dot{x}(0)=B-\gamma A=0$ より $B=\gamma x_0$ なので，

$$
\finalanswer{x(t)=x_0(1+\gamma t)e^{-\gamma t}}
$$

となります。(1) の結果で $\omega_1\to0$ とすると，$\sin\omega_1t/\omega_1\to t$ より，この式と一致します。

### (3)
$\gamma>\omega_0$ では特性根 $-\gamma\pm\kappa$ は相異なる負の実数です。$e^{\pm\kappa t}$ の代わりにその和と差である $\cosh\kappa t$，$\sinh\kappa t$ を使うと，一般解は

$$
x=e^{-\gamma t}(A\cosh\kappa t+B\sinh\kappa t)
$$

です。$x(0)=A$，$\dot{x}(0)=-\gamma A+\kappa B$ なので，$A=x_0$，$B=\gamma x_0/\kappa$ となり，

$$
\finalanswer{x(t)=x_0e^{-\gamma t}\left(\cosh\kappa t+\frac{\gamma}{\kappa}\sinh\kappa t\right)}
$$

です。振動せずに0へ近づき，長時間では $e^{-(\gamma-\kappa)t}$ のように減衰します。$\gamma-\kappa<\gamma$ なので，臨界減衰の場合より遅く減衰します。3つの場合の $x(t)$ を図に示します。

<!-- FIGURE solution (3): 横軸 t，縦軸 x，原点 O。3本の曲線はすべて t=0 で x=x_0，傾き0から出発する。実線は減衰振動で，x=0 を何度も横切りながら振幅が減っていく。破線は臨界減衰で，x=0 を横切らずに速やかに0へ近づく。点線は過減衰で，x=0 を横切らず，破線よりゆっくり0へ近づく。凡例に 減衰振動，臨界減衰，過減衰 と書く。 -->

===== FILE: 08differential_equations/02/02_020.md =====
---
tags:
  - 基本
---

# 未定係数法

## 問題
微分方程式

$$
y''-3y'+2y=f(x)
$$

を考える。以下の問いに答えよ。

(1) $f(x)=2x^2$ のとき，多項式の特解 $y_\mathrm{p}$ を求めよ。

(2) $f(x)=e^{3x}$ のとき，特解 $y_\mathrm{p}$ を求めよ。

(3) $f(x)=10\sin x$ のとき，特解 $y_\mathrm{p}$ を求めよ。

---

## 解答・解説

### (1)
$y$ の係数が0でないので，2次式を左辺に入れると2次式が出てきます。そこで $y_\mathrm{p}=ax^2+bx+c$ と置いて左辺を計算すると，

$$
\begin{aligned}
y_\mathrm{p}''-3y_\mathrm{p}'+2y_\mathrm{p}&=2a-3(2ax+b)+2(ax^2+bx+c)\\
&=2ax^2+(2b-6a)x+(2a-3b+2c)
\end{aligned}
$$

となります。これを $2x^2$ と係数ごとに等しくおくと，$2a=2$，$2b-6a=0$，$2a-3b+2c=0$ です。順に解くと $a=1$，$b=3$，$c=7/2$ なので，

$$
\finalanswer{y_\mathrm{p}=x^2+3x+\frac{7}{2}}
$$

となります。

### (2)
指数関数は微分しても形が変わらないので，$y_\mathrm{p}=Ae^{3x}$ と置きます。左辺に代入すると，

$$
\begin{aligned}
y_\mathrm{p}''-3y_\mathrm{p}'+2y_\mathrm{p}&=(9-9+2)Ae^{3x}\\
&=2Ae^{3x}
\end{aligned}
$$

です。これが $e^{3x}$ に等しいので $A=1/2$ となり，

$$
\finalanswer{y_\mathrm{p}=\frac{1}{2}e^{3x}}
$$

です。係数 $9-9+2$ は特性多項式 $\lambda^2-3\lambda+2$ に $\lambda=3$ を代入した値です。$3$ は特性根 $1$，$2$ のどちらでもないので，この値は0にならず $A$ が決まります。

### (3)
$y'$ の項があるため，$\sin x$ を微分すると $\cos x$ も現れます。そこで $y_\mathrm{p}=A\cos x+B\sin x$ と置きます。$y_\mathrm{p}'=-A\sin x+B\cos x$，$y_\mathrm{p}''=-y_\mathrm{p}$ を代入すると，

$$
\begin{aligned}
y_\mathrm{p}''-3y_\mathrm{p}'+2y_\mathrm{p}&=y_\mathrm{p}-3y_\mathrm{p}'\\
&=(A-3B)\cos x+(3A+B)\sin x
\end{aligned}
$$

となります。これを $10\sin x$ と比べると $A-3B=0$，$3A+B=10$ なので，$B=1$，$A=3$ です。したがって，

$$
\finalanswer{y_\mathrm{p}=3\cos x+\sin x}
$$

となります。方程式は線形なので，$f$ が (1) から (3) の和であれば，3つの特解を足したものが特解になります。これに $C_1e^x+C_2e^{2x}$ を加えたものが一般解です。$f=e^{x}$ のように特性根と同じ指数をもつ場合は $Ae^{x}$ が左辺を0にするので，$Axe^{x}$ と置く必要があります。

===== FILE: 08differential_equations/02/02_030.md =====
---
tags:
  - 標準
---

# 定数変化法

## 問題
$-\pi/2<x<\pi/2$ で，微分方程式

$$
y''+y=\frac{1}{\cos x}
$$

を考える。以下の問いに答えよ。

(1) 解を $y=u_1(x)\cos x+u_2(x)\sin x$ と置き，条件 $u_1'\cos x+u_2'\sin x=0$ を課す。$u_1'$ と $u_2'$ を求めよ。

(2) 一般解を求めよ。

---

##解答・解説

### (1)
右辺を0とした方程式の基本解 $\cos x$，$\sin x$ の係数を関数に置き換えています。$y$ を微分し，課した条件を使うと，$u_1'$，$u_2'$ を含む項が消えます。

$$
\begin{aligned}
y'&=u_1'\cos x+u_2'\sin x-u_1\sin x+u_2\cos x\\
&=-u_1\sin x+u_2\cos x
\end{aligned}
$$

もう一度微分すると，

$$
y''=-u_1'\sin x+u_2'\cos x-u_1\cos x-u_2\sin x
$$

です。$y$ を加えると $u_1$，$u_2$ そのものを含む項は打ち消し合い，方程式は $-u_1'\sin x+u_2'\cos x=1/\cos x$ となります。課した条件とあわせて，次の連立方程式が得られます。

$$
\begin{aligned}
u_1'\cos x+u_2'\sin x&=0\\
-u_1'\sin x+u_2'\cos x&=\frac{1}{\cos x}
\end{aligned}
$$

第1式に $\cos x$ を掛けて第2式の $\sin x$ 倍を引くと $u_1'$ が，第1式に $\sin x$ を掛けて第2式の $\cos x$ 倍を足すと $u_2'$ が求まります。$\sin^2x+\cos^2x=1$ より，

$$
\begin{aligned}
&\finalanswer{u_1'=-\tan x}\\
&\finalanswer{u_2'=1}
\end{aligned}
$$

となります。連立方程式の係数行列式は $\cos x$ と $\sin x$ のロンスキアンで，その値は1です。

### (2)
$u_1'$，$u_2'$ を積分します。$u_1$ は $w=\cos x$ と置くと $dw=-\sin x\,dx$ で，区間内で $\cos x>0$ なので

$$
\begin{aligned}
u_1&=-\int\frac{\sin x}{\cos x}\,dx=\int\frac{dw}{w}\\
&=\ln(\cos x)+C_1
\end{aligned}
$$

となります。また $u_2=x+C_2$ です。これらを $y=u_1\cos x+u_2\sin x$ に代入すると，

$$
\finalanswer{y=C_1\cos x+C_2\sin x+\cos x\ln(\cos x)+x\sin x}
$$

となります。$C_1$，$C_2$ は任意の定数です。検算として，特解 $y_\mathrm{p}=\cos x\ln(\cos x)+x\sin x$ を2回微分すると，

$$
\begin{aligned}
y_\mathrm{p}'&=-\sin x\ln(\cos x)+x\cos x\\
y_\mathrm{p}''&=-\cos x\ln(\cos x)+\frac{\sin^2x}{\cos x}+\cos x-x\sin x
\end{aligned}
$$

です。足し合わせると $y_\mathrm{p}''+y_\mathrm{p}=\sin^2x/\cos x+\cos x=1/\cos x$ となり，右辺と一致します。$1/\cos x$ は微分しても有限個の関数の組に収まらないので，未定係数法ではこの特解を見つけられません。

===== FILE: 08differential_equations/02/02_040.md =====
---
tags:
  - 標準
---

# ロンスキアンと解の一次独立性

## 問題
$p(x)$，$q(x)$ を連続関数とし，方程式

$$
y''+p(x)y'+q(x)y=0
$$

の2つの解 $y_1$，$y_2$ に対してロンスキアンを $W(x)=y_1y_2'-y_1'y_2$ と定める。以下の問いに答えよ。

(1) $W(x)$ を，ある点 $x_0$ での値 $W(x_0)$ と $p$ を用いて表せ。

(2) $-1<x<1$ で方程式

$$
(1-x^2)y''-2xy'+2y=0
$$

を考える。$y_1=x$ と，$y_2(0)=-1$，$y_2'(0)=0$ を満たす解 $y_2$ について，$W(x)$ を求めよ。

(3) (2) の $y_2$ を求めよ。$(y_2/y_1)'$ を考えよ。

---

## 解答・解説

### (1)
$W$ を微分すると $y_1'y_2'$ の項が打ち消し合います。

$$
\begin{aligned}
W'&=y_1'y_2'+y_1y_2''-y_1''y_2-y_1'y_2'\\
&=y_1y_2''-y_1''y_2
\end{aligned}
$$

方程式から $y_j''=-py_j'-qy_j$ を代入すると，$q$ の項も打ち消し合います。

$$
\begin{aligned}
W'&=y_1(-py_2'-qy_2)-(-py_1'-qy_1)y_2\\
&=-p(y_1y_2'-y_1'y_2)\\
&=-pW
\end{aligned}
$$

これは $W$ についての1階線形方程式です。積分因子を掛けると次の量の微分が0になるので，これは定数で，その値は $x=x_0$ での値 $W(x_0)$ です。

$$
\frac{d}{dx}\left[W\exp\left(\int_{x_0}^{x}p(s)\,ds\right)\right]=(W'+pW)\exp\left(\int_{x_0}^{x}p(s)\,ds\right)=0
$$

したがって，

$$
\finalanswer{W(x)=W(x_0)\exp\left(-\int_{x_0}^{x}p(s)\,ds\right)}
$$

となります。これをアーベルの公式といいます。指数関数は0にならないので，$W$ は恒等的に0であるか，どこでも0でないかのどちらかです。

### (2)
両辺を $1-x^2$ で割ると $p(x)=-2x/(1-x^2)$ です。$x_0=0$ での値は $W(0)=y_1(0)y_2'(0)-y_1'(0)y_2(0)=1$ です。$p$ の積分は $w=1-s^2$ と置くと $dw=-2s\,ds$ なので，

$$
\begin{aligned}
\int_0^x p(s)\,ds&=\int_0^x\frac{-2s}{1-s^2}\,ds=\int_1^{1-x^2}\frac{dw}{w}\\
&=\ln(1-x^2)
\end{aligned}
$$

となります。(1) の結果に代入すると，

$$
\finalanswer{W(x)=\frac{1}{1-x^2}}
$$

です。$W\neq0$ なので，$y_1$ と $y_2$ は一次独立です。

### (3)
商の微分法から $(y_2/y_1)'=W/y_1^2$ です。まず $0<x<1$ で考え，右辺を部分分数に分けます。

$$
\begin{aligned}
\frac{d}{dx}\left(\frac{y_2}{x}\right)&=\frac{1}{x^2(1-x^2)}\\
&=\frac{1}{x^2}+\frac{1}{2}\left(\frac{1}{1+x}+\frac{1}{1-x}\right)
\end{aligned}
$$

これを積分すると，$c$ を積分定数として

$$
\frac{y_2}{x}=-\frac{1}{x}+\frac{1}{2}\ln\frac{1+x}{1-x}+c
$$

です。両辺に $x$ を掛けると $y_2=-1+(x/2)\ln\{(1+x)/(1-x)\}+cx$ となります。この式は $-1<x<1$ 全体でなめらかで，$y_2(0)=-1$ を満たします。対数を含む項の $x=0$ での微分は0なので，$y_2'(0)=c$ です。条件 $y_2'(0)=0$ より $c=0$ となり，

$$
\finalanswer{y_2=\frac{x}{2}\ln\frac{1+x}{1-x}-1}
$$

となります。解の一意性から，これは $-1<x<1$ 全体での解です。$x\to\pm1$ では対数的に発散し，$y_1=x$ とは振る舞いが異なります。

===== FILE: 08differential_equations/02/02_050.md =====
---
tags:
  - 標準
---

# オイラー型方程式

## 問題
$x>0$ で定義された関数 $y(x)$ を考え，$y'=dy/dx$ とする。$x=e^t$ と置いて $y$ を $t$ の関数とみなし，$t$ による微分を $\dot{y}$，$\ddot{y}$ で表す。以下の問いに答えよ。

(1) $x^2y''$ を $\dot{y}$，$\ddot{y}$ で表せ。

(2) 方程式 $x^2y''-3xy'+4y=0$ の一般解を求めよ。

(3) 方程式 $x^2y''+xy'+y=0$ の解で，$y(1)=0$，$y'(1)=1$ を満たすものを求めよ。

---

## 解答・解説

### (1)
$t=\ln x$ より $dt/dx=1/x$ です。合成関数の微分法から

$$
y'=\frac{dt}{dx}\dot{y}=\frac{1}{x}\dot{y}
$$

なので，$xy'=\dot{y}$ です。もう一度 $x$ で微分します。$\dot{y}$ は $t$ の関数なので，その $x$ 微分にも $dt/dx=1/x$ が掛かります。

$$
\begin{aligned}
y''&=\frac{d}{dx}\left(\frac{1}{x}\dot{y}\right)\\
&=-\frac{1}{x^2}\dot{y}+\frac{1}{x}\cdot\frac{1}{x}\ddot{y}
\end{aligned}
$$

両辺に $x^2$ を掛けると，

$$
\finalanswer{x^2y''=\ddot{y}-\dot{y}}
$$

となります。

### (2)
(1) の結果と $xy'=\dot{y}$ を代入すると，$t$ についての定数係数の方程式になります。

$$
\begin{aligned}
(\ddot{y}-\dot{y})-3\dot{y}+4y&=0\\
\ddot{y}-4\dot{y}+4y&=0
\end{aligned}
$$

特性方程式 $\lambda^2-4\lambda+4=(\lambda-2)^2=0$ は重解 $\lambda=2$ をもつので，一般解は $y=(C_1+C_2t)e^{2t}$ です。$e^{t}=x$，$t=\ln x$ を代入すると，

$$
\finalanswer{y=x^2(C_1+C_2\ln x)}
$$

となります。$C_1$，$C_2$ は任意の定数です。$y=x^2\ln x$ を直接代入すると，$y'=2x\ln x+x$，$y''=2\ln x+3$ より左辺は $(2-6+4)x^2\ln x+(3-3)x^2=0$ となります。

### (3)
同じように代入すると，$\dot{y}$ の項が打ち消し合います。

$$
\begin{aligned}
(\ddot{y}-\dot{y})+\dot{y}+y&=0\\
\ddot{y}+y&=0
\end{aligned}
$$

一般解は $y=C_1\cos t+C_2\sin t$ であり，$x$ で書くと $y=C_1\cos(\ln x)+C_2\sin(\ln x)$ です。$x=1$ は $t=0$ にあたるので，$y(1)=C_1=0$ です。また $y'=\dot{y}/x$ より $y'(1)=\dot{y}(0)=C_2=1$ です。したがって，

$$
\finalanswer{y=\sin(\ln x)}
$$

となります。$x\to+0$ では $\ln x\to-\infty$ なので，この解は無限回振動します。

===== FILE: 08differential_equations/02/02_060.md =====
---
tags:
  - 基本
---

# 共振

## 問題
変位 $x(t)$ が，正の定数 $\omega_0$，$\omega$ と定数 $f_0$ を用いて

$$
\ddot{x}+\omega_0^2x=f_0\cos\omega t
$$

に従う。以下の問いに答えよ。

(1) $\omega=\omega_0$ のとき，定数 $A$，$B$ を用いた $x=t(A\cos\omega_0t+B\sin\omega_0t)$ の形の特解を求めよ。

(2) $\omega\neq\omega_0$ のとき，$x(0)=0$，$\dot{x}(0)=0$ を満たす解を求めよ。

(3) (2) の解の $\omega\to\omega_0$ の極限を求めよ。

---

## 解答・解説

### (1)
$\cos\omega_0t$ は右辺を0とした方程式の解なので，$A\cos\omega_0t+B\sin\omega_0t$ を代入しても左辺は0になります。そのため $t$ を掛けた形を使います。$g(t)=A\cos\omega_0t+B\sin\omega_0t$ と置くと，$\ddot{g}=-\omega_0^2g$ です。$x=tg$ を2回微分すると $\ddot{x}=2\dot{g}+t\ddot{g}$ なので，

$$
\begin{aligned}
\ddot{x}+\omega_0^2x&=2\dot{g}+t(\ddot{g}+\omega_0^2g)\\
&=2\omega_0(-A\sin\omega_0t+B\cos\omega_0t)
\end{aligned}
$$

となります。これを $f_0\cos\omega_0t$ と比べると $A=0$，$B=f_0/(2\omega_0)$ なので，

$$
\finalanswer{x_\mathrm{p}=\frac{f_0}{2\omega_0}t\sin\omega_0t}
$$

となります。

### (2)
$\omega\neq\omega_0$ では，特解を $C\cos\omega t$ と置けます。代入すると $(\omega_0^2-\omega^2)C=f_0$ です。一般解は，$D_1$，$D_2$ を定数として

$$
x=\frac{f_0}{\omega_0^2-\omega^2}\cos\omega t+D_1\cos\omega_0t+D_2\sin\omega_0t
$$

です。$x(0)=0$ から $D_1=-f_0/(\omega_0^2-\omega^2)$，$\dot{x}(0)=\omega_0D_2=0$ から $D_2=0$ となるので，

$$
\finalanswer{x(t)=\frac{f_0}{\omega_0^2-\omega^2}\left(\cos\omega t-\cos\omega_0t\right)}
$$

です。

### (3)
差を積に直す公式を使い，分母の $\omega_0^2-\omega^2=(\omega_0+\omega)(\omega_0-\omega)$ と組み合わせます。

$$
\begin{aligned}
\cos\omega t-\cos\omega_0t&=2\sin\frac{(\omega_0+\omega)t}{2}\sin\frac{(\omega_0-\omega)t}{2}\\
x(t)&=\frac{2f_0}{\omega_0+\omega}\sin\frac{(\omega_0+\omega)t}{2}\cdot\frac{\sin\{(\omega_0-\omega)t/2\}}{\omega_0-\omega}
\end{aligned}
$$

$\omega\to\omega_0$ では最後の因子が $t/2$ に近づきます。したがって，

$$
\begin{aligned}
x(t)&\to\frac{2f_0}{2\omega_0}\sin\omega_0t\cdot\frac{t}{2}\\
&=\finalanswer{\frac{f_0}{2\omega_0}t\sin\omega_0t}
\end{aligned}
$$

となります。(1) の特解は $x_\mathrm{p}(0)=0$，$\dot{x}_\mathrm{p}(0)=0$ を満たすので，この極限は共振時の同じ初期値問題の解と一致します。$\omega$ が $\omega_0$ に近いときはゆっくりしたうなりが生じ，その周期が無限に長くなった極限で振幅が時間に比例して増え続けます。共振時の解を図に示します。

<!-- FIGURE solution (3): 横軸 t，縦軸 x，原点 O。曲線 x=(f_0/(2ω_0)) t sin(ω_0 t) を実線で描く（f_0>0 とする）。直線 x=(f_0/(2ω_0)) t と x=-(f_0/(2ω_0)) t を点線で描き，振動の包絡線であることがわかるようにする。振動は5〜6周期程度描く。 -->

===== FILE: 08differential_equations/03/03_010.md =====
---
tags:
  - 標準
---

# 連立1階線形方程式

## 問題
連立微分方程式

$$
\begin{aligned}
\dot{x}&=4x-2y\\
\dot{y}&=x+y
\end{aligned}
$$

を考え，$\boldsymbol{u}=(x,y)^{\mathrm{T}}$ として $\dot{\boldsymbol{u}}=A\boldsymbol{u}$ と書く。以下の問いに答えよ。

(1) 係数行列 $A$ の固有値を求めよ。

(2) 一般解を求めよ。

(3) $x(0)=1$，$y(0)=0$ を満たす解を求めよ。

---

## 解答・解説

### (1)
係数行列は次のとおりです。

$$
A=\begin{pmatrix}4&-2\\1&1\end{pmatrix}
$$

固有方程式を立てて因数分解すると，

$$
\begin{aligned}
\det(A-\lambda I)&=(4-\lambda)(1-\lambda)+2\\
&=\lambda^2-5\lambda+6\\
&=(\lambda-2)(\lambda-3)
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{\lambda=2,\ 3}
$$

です。

### (2)
$\boldsymbol{u}=e^{\lambda t}\boldsymbol{v}$ を方程式に代入すると $A\boldsymbol{v}=\lambda\boldsymbol{v}$ となるので，$\lambda$ が固有値，$\boldsymbol{v}$ が固有ベクトルのとき解になります。$\lambda=2$ では $A-2I$ の第2行から $x-y=0$ で，$\boldsymbol{v}_1=(1,1)^{\mathrm{T}}$ です。$\lambda=3$ では $A-3I$ の第2行から $x-2y=0$ で，$\boldsymbol{v}_2=(2,1)^{\mathrm{T}}$ です。2つの固有ベクトルは一次独立なので，その重ね合わせで2次元の解空間全体が表せます。よって，

$$
\finalanswer{\begin{pmatrix}x\\y\end{pmatrix}=C_1e^{2t}\begin{pmatrix}1\\1\end{pmatrix}+C_2e^{3t}\begin{pmatrix}2\\1\end{pmatrix}}
$$

となります。$C_1$，$C_2$ は任意の定数です。

### (3)
一般解に $t=0$ を代入して初期条件と等しくおくと，

$$
\begin{aligned}
C_1+2C_2&=1\\
C_1+C_2&=0
\end{aligned}
$$

となります。第1式から第2式を引くと $C_2=1$，したがって $C_1=-1$ です。よって，

$$
\begin{aligned}
&\finalanswer{x(t)=2e^{3t}-e^{2t}}\\
&\finalanswer{y(t)=e^{3t}-e^{2t}}
\end{aligned}
$$

となります。検算として，$\dot{x}=6e^{3t}-2e^{2t}$ と $4x-2y=8e^{3t}-4e^{2t}-2e^{3t}+2e^{2t}$ は一致します。$\dot{y}=3e^{3t}-2e^{2t}$ と $x+y$ も一致します。$t\to\infty$ では $e^{3t}$ の項が大きくなり，解は大きい固有値の固有ベクトル $(2,1)^{\mathrm{T}}$ の方向へ伸びていきます。

===== FILE: 08differential_equations/03/03_020.md =====
---
tags:
  - 標準
---

# 平衡点の分類

## 問題
実数の定数 $c\ge0$，$k\neq0$ を含む連立微分方程式

$$
\begin{aligned}
\dot{x}&=y\\
\dot{y}&=-kx-cy
\end{aligned}
$$

の平衡点 $(0,0)$ を考える。以下の問いに答えよ。

(1) 係数行列の固有値 $\lambda$ を求めよ。

(2) 平衡点が鞍点となる $k$ の範囲を求めよ。

(3) $k>0$ とする。平衡点が安定ならせんとなる $c$ の範囲を求めよ。

---

## 解答・解説

### (1)
係数行列は $A=\begin{pmatrix}0&1\\-k&-c\end{pmatrix}$ です。固有方程式を立てると，

$$
\begin{aligned}
\det(A-\lambda I)&=-\lambda(-c-\lambda)+k\\
&=\lambda^2+c\lambda+k
\end{aligned}
$$

となります。これを0とおいて解くと，

$$
\finalanswer{\lambda=\frac{-c\pm\sqrt{c^2-4k}}{2}}
$$

です。この系は，$x$ を変位，$y$ を速度とする減衰振動子 $\ddot{x}+c\dot{x}+kx=0$ と同じです。

### (2)
2次元の線形系の平衡点は固有値 $\lambda_1$，$\lambda_2$ で分類されます。同符号の実数なら結節，異符号の実数なら鞍点，実部が0でない複素数ならせん，純虚数なら渦心です。解と係数の関係から

$$
\begin{aligned}
\lambda_1+\lambda_2&=-c\\
\lambda_1\lambda_2&=k
\end{aligned}
$$

です。鞍点の条件は2つの固有値が異符号の実数であること，すなわち $\lambda_1\lambda_2<0$ です。$k<0$ なら判別式 $c^2-4k$ は正なので，固有値はたしかに実数です。したがって，

$$
\finalanswer{k<0}
$$

となります。ばねが復元力ではなく反発力を与える場合にあたり，平衡点から離れる向きの解が必ず含まれます。

### (3)
$k>0$ では $\lambda_1\lambda_2>0$ なので，鞍点にはなりません。固有値が複素数となるのは判別式が負のとき，つまり $c^2<4k$ のときで，その実部は $-c/2$ です。らせんとなるには実部が0でないことが必要で，$c\ge0$ より $c>0$ です。このとき実部は負なので，解は回転しながら原点に近づき，安定ならせんになります。したがって，

$$
\finalanswer{0<c<2\sqrt{k}}
$$

となります。$c=0$ では固有値が純虚数となり渦心，$c\ge2\sqrt{k}$ では2つの負の実数となり安定結節です。$ck$ 平面での分類を図に示します。

<!-- FIGURE solution (3): 横軸 c（c≥0 の部分だけ），縦軸 k，原点 O。放物線 k=c^2/4（c≥0）を実線で描く。k<0 の領域に 鞍点，放物線より上で c>0 の領域に 安定ならせん，放物線と c 軸の間（0<k≤c^2/4）に 安定結節 とラベルを付ける。縦軸の正の部分（c=0，k>0）を太線で描き 渦心 とラベルを付ける。 -->

===== FILE: 08differential_equations/03/03_030.md =====
---
tags:
  - 標準
---

# 非線形系の線形化

## 問題
被食者の数 $x(t)$ と捕食者の数 $y(t)$ が，正の定数 $a$，$b$，$c$，$d$ を用いて

$$
\begin{aligned}
\dot{x}&=ax-bxy\\
\dot{y}&=-cy+dxy
\end{aligned}
$$

に従う。$x\ge0$，$y\ge0$ とする。以下の問いに答えよ。

(1) 平衡点をすべて求めよ。

(2) 原点のまわりで線形化した方程式の係数行列の固有値を求めよ。

(3) 原点以外の平衡点のまわりで線形化したとき，平衡点からの微小なずれが振動する周期 $T$ を求めよ。

---

## 解答・解説

### (1)
平衡点では $\dot{x}=\dot{y}=0$ なので，

$$
\begin{aligned}
x(a-by)&=0\\
y(-c+dx)&=0
\end{aligned}
$$

を解きます。$x=0$ なら第2式から $y=0$ です。$x\neq0$ なら第1式から $y=a/b$ で，このとき第2式から $x=c/d$ です。したがって，

$$
\finalanswer{(x,y)=(0,0),\ \left(\frac{c}{d},\frac{a}{b}\right)}
$$

となります。

### (2)
右辺を $x$，$y$ で偏微分したヤコビ行列が，線形化した方程式の係数行列になります。

$$
J=\begin{pmatrix}a-by&-bx\\dy&-c+dx\end{pmatrix}
$$

原点では $J=\mathrm{diag}(a,-c)$ なので，固有値は

$$
\finalanswer{\lambda=a,\ -c}
$$

です。異符号の実数なので原点は鞍点です。捕食者がいなければ被食者は指数関数的に増え，被食者がいなければ捕食者は指数関数的に減ることに対応しています。

### (3)
$x=c/d+\xi$，$y=a/b+\eta$ と置き，$\xi$，$\eta$ の2次の項を無視します。$a-by=-b\eta$，$-c+dx=d\xi$ なので，

$$
\begin{aligned}
\dot{\xi}&=\left(\frac{c}{d}+\xi\right)(-b\eta)\simeq-\frac{bc}{d}\eta\\
\dot{\eta}&=\left(\frac{a}{b}+\eta\right)d\xi\simeq\frac{ad}{b}\xi
\end{aligned}
$$

となります。第1式をもう一度微分して第2式を代入すると，

$$
\begin{aligned}
\ddot{\xi}&=-\frac{bc}{d}\dot{\eta}\\
&=-\frac{bc}{d}\cdot\frac{ad}{b}\xi\\
&=-ac\,\xi
\end{aligned}
$$

です。これは角振動数 $\sqrt{ac}$ の単振動なので，

$$
\finalanswer{T=\frac{2\pi}{\sqrt{ac}}}
$$

となります。係数行列の固有値は $\pm i\sqrt{ac}$ の純虚数で，線形化した系の平衡点は渦心です。もとの非線形系でも，$V=dx-c\ln x+by-a\ln y$ の時間微分を計算すると0になるので，軌道は $V=$ 一定の閉曲線になります。相平面の軌道を図に示します。

<!-- FIGURE solution (3): 横軸 x，縦軸 y，原点 O，第1象限のみ。点 (c/d, a/b) に黒丸を打ち，そのまわりを囲む入れ子の閉曲線を3本描く。内側ほど楕円に近く，外側ほど左下に膨らんだ卵形にする。各閉曲線に反時計回りの矢印を付ける。横軸上に c/d，縦軸上に a/b の目盛りを付ける。 -->

===== FILE: 08differential_equations/03/03_040.md =====
---
tags:
  - 標準
---

# 保存系と相図

## 問題
振り子の振れ角 $\theta(t)$ が，正の定数 $\omega_0$ を用いて

$$
\ddot{\theta}+\omega_0^2\sin\theta=0
$$

に従う。$v=\dot{\theta}$ とし，$\theta v$ 平面上の軌道を考える。平衡点 $(\theta,v)=(\pi,0)$ を通る軌道をセパラトリクスという。以下の問いに答えよ。

(1) $E=v^2/2+U(\theta)$ が時間によらず一定となる関数 $U(\theta)$ を，$U(0)=0$ となるように求めよ。

(2) $-\pi\le\theta\le\pi$ の範囲で，セパラトリクスを $v$ についての式で表せ。

(3) セパラトリクス上を運動し，$\theta(0)=0$，$\dot{\theta}(0)>0$ となる解 $\theta(t)$ を求めよ。

---

## 解答・解説

### (1)
運動方程式の両辺に $\dot{\theta}$ を掛けると，各項が時間微分の形にまとまります。

$$
\begin{aligned}
\dot{\theta}\ddot{\theta}+\omega_0^2\dot{\theta}\sin\theta&=0\\
\frac{d}{dt}\left(\frac{\dot{\theta}^2}{2}-\omega_0^2\cos\theta\right)&=0
\end{aligned}
$$

括弧内に定数を加えても保存量なので，$U(0)=0$ となるように $\omega_0^2$ を加えると，

$$
\finalanswer{U(\theta)=\omega_0^2(1-\cos\theta)}
$$

となります。$E$ は単位質量・単位長さあたりの力学的エネルギーにあたります。

### (2)
セパラトリクスは $(\pi,0)$ を通るので，その上での $E$ の値は $U(\pi)=2\omega_0^2$ です。$E=2\omega_0^2$ を $v^2$ について解き，半角の公式を使うと，

$$
\begin{aligned}
v^2&=2\{2\omega_0^2-\omega_0^2(1-\cos\theta)\}\\
&=2\omega_0^2(1+\cos\theta)\\
&=4\omega_0^2\cos^2\frac{\theta}{2}
\end{aligned}
$$

となります。$-\pi\le\theta\le\pi$ では $\cos(\theta/2)\ge0$ なので，

$$
\finalanswer{v=\pm2\omega_0\cos\frac{\theta}{2}}
$$

です。$E<2\omega_0^2$ の軌道はセパラトリクスの内側の閉曲線で，振り子は往復運動をします。$E>2\omega_0^2$ の軌道は外側の波形の曲線で，振り子は回転し続けます。相図を図に示します。

<!-- FIGURE solution (2): 横軸 θ（-2π から 2π），縦軸 v，原点 O。曲線 v=±2ω_0 cos(θ/2) とその 2π ずらしを太線で描き，θ=±π で交わる目の形のセパラトリクスにする。目の内側に原点のまわりの閉曲線を2本，θ=±2π のまわりにも同様の閉曲線を描く。セパラトリクスの上側と下側に，θ 方向に続く波形の曲線を1本ずつ描く。点 (±π,0) に白丸を打つ。軌道の向きは上半平面で右向き，下半平面で左向きの矢印で示す。縦軸に 2ω_0 の目盛りを付ける。 -->

### (3)
$\dot{\theta}(0)>0$ なので上側の枝 $\dot{\theta}=2\omega_0\cos(\theta/2)$ を解きます。$\varphi=\theta/2$ と置くと $\dot{\varphi}=\omega_0\cos\varphi$ で，変数を分けると $d\varphi/\cos\varphi=\omega_0\,dt$ です。左辺は $w=\sin\varphi$ と置くと $dw=\cos\varphi\,d\varphi$ より $d\varphi/\cos\varphi=dw/(1-w^2)$ となるので，$t=0$ で $\varphi=0$ から積分すると，

$$
\begin{aligned}
\omega_0t&=\int_0^{\sin\varphi}\frac{dw}{1-w^2}\\
&=\frac{1}{2}\ln\frac{1+\sin\varphi}{1-\sin\varphi}\\
&=\tanh^{-1}(\sin\varphi)
\end{aligned}
$$

となります。これを $\varphi$ について解くと $\sin\varphi=\tanh\omega_0t$ なので，

$$
\finalanswer{\theta(t)=2\arcsin(\tanh\omega_0t)}
$$

です。$t=0$ での微分は $2\omega_0$ で，(2) の $\theta=0$ での $v$ と一致します。$t\to\infty$ で $\theta\to\pi$ となり，倒立の位置に近づくのに無限の時間がかかります。

===== FILE: 08differential_equations/03/03_050.md =====
---
tags:
  - 発展
---

# リアプノフ関数と安定性

## 問題
正の定数 $\omega_0$，$\gamma$ を含む連立微分方程式

$$
\begin{aligned}
\dot{x}&=y\\
\dot{y}&=-\omega_0^2x-2\gamma y
\end{aligned}
$$

を考える。関数の時間微分は解軌道に沿ってとる。以下の問いに答えよ。

(1) 次の関数 $V$ について，$dV/dt$ を $x$，$y$ で表せ。

$$
V=\frac{1}{2}\left(y^2+\omega_0^2x^2\right)
$$

(2) 実数 $\varepsilon$ を含む関数 $V_\varepsilon=V+\varepsilon xy$ について，$dV_\varepsilon/dt$ を $x$，$y$ で表せ。

(3) $(x,y)\neq(0,0)$ のすべての点で $dV_\varepsilon/dt<0$ となる $\varepsilon$ の範囲を求めよ。

---

## 解答・解説

### (1)
合成関数の微分法で $V$ を微分し，方程式を代入します。

$$
\begin{aligned}
\frac{dV}{dt}&=y\dot{y}+\omega_0^2x\dot{x}\\
&=y(-\omega_0^2x-2\gamma y)+\omega_0^2xy\\
&=\finalanswer{-2\gamma y^2}
\end{aligned}
$$

となります。$V$ は力学的エネルギーにあたり，減衰によって増えることはありません。ただし $y=0$，$x\neq0$ の点では $dV/dt=0$ となるので，この $V$ だけでは原点に近づくことまでは言えません。

### (2)
付け加えた項 $xy$ の時間微分を計算します。

$$
\begin{aligned}
\frac{d}{dt}(xy)&=\dot{x}y+x\dot{y}\\
&=y^2-\omega_0^2x^2-2\gamma xy
\end{aligned}
$$

これを $\varepsilon$ 倍して (1) の結果に加えると，

$$
\finalanswer{\frac{dV_\varepsilon}{dt}=-\varepsilon\omega_0^2x^2-2\varepsilon\gamma xy-(2\gamma-\varepsilon)y^2}
$$

となります。

### (3)
$dV_\varepsilon/dt<0$ は，二次形式 $Q=\varepsilon\omega_0^2x^2+2\varepsilon\gamma xy+(2\gamma-\varepsilon)y^2$ が正定値であることと同じです。$\alpha x^2+2\beta xy+\delta y^2$ は平方完成すると $\alpha(x+\beta y/\alpha)^2+(\alpha\delta-\beta^2)y^2/\alpha$ となるので，正定値の条件は $\alpha>0$ かつ $\alpha\delta-\beta^2>0$ です。第1の条件は $\varepsilon>0$ です。第2の条件を $\varepsilon>0$ で割って整理すると，

$$
\begin{aligned}
\varepsilon\omega_0^2(2\gamma-\varepsilon)-\varepsilon^2\gamma^2&>0\\
2\gamma\omega_0^2-\varepsilon(\omega_0^2+\gamma^2)&>0
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{0<\varepsilon<\frac{2\gamma\omega_0^2}{\omega_0^2+\gamma^2}}
$$

です。このとき $\varepsilon<2\gamma$ なので，$y^2$ の係数も正になっています。一方，$V_\varepsilon$ 自身が正定値となる条件は，同じ判定法から $\varepsilon^2<\omega_0^2$ です。$\omega_0^2+\gamma^2\ge2\gamma\omega_0$ より上の範囲の上限は $\omega_0$ 以下なので，この条件は自動的に満たされます。正定値で時間微分が負定値の関数が見つかったので，原点は漸近安定です。

===== END =====