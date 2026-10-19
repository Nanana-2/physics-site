===== FILE: 06solid_state/01/01_010.md =====
---
tags:
  - 基本
---

# ブラベー格子と基本並進ベクトル

## 問題
一辺 $a$ の立方体を慣用単位胞とする立方晶のブラベー格子を考える。単純立方格子は立方体の頂点だけに，体心立方格子は頂点と立方体の中心に，面心立方格子は頂点と6つの面の中心に格子点をもつ（図）。立方体の辺は直交座標の単位ベクトル $\boldsymbol{e}_x,\boldsymbol{e}_y,\boldsymbol{e}_z$ の向きにそろえ，格子点の1つを原点にとる。

3つのベクトル $\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3$ について，整数 $n_1,n_2,n_3$ を用いた $n_1\boldsymbol{a}_1+n_2\boldsymbol{a}_2+n_3\boldsymbol{a}_3$ の形の点がすべて格子点であり，逆にすべての格子点がこの形に書けるとき，これらを基本並進ベクトルとよぶ。基本並進ベクトルが張る平行六面体を基本単位胞とよぶ。以下の問いに答えよ。

<!-- FIGURE problem: 一辺 a の立方体（慣用単位胞）を左右に2つ並べて描く。左は体心立方格子で，8つの頂点と立方体の中心に黒丸を置く。右は面心立方格子で，8つの頂点と6つの面の中心に黒丸を置く（見えない奥の面の中心は薄い色にする）。どちらの立方体も左下手前の頂点を原点 O とし，O から x，y，z 軸を矢印で描いて e_x，e_y，e_z の向きを示す。各立方体の1辺に寸法線を引き，a とラベルを付ける。基本並進ベクトルの矢印は描かない。 -->

(1) 単純立方格子，体心立方格子，面心立方格子のそれぞれについて，慣用単位胞1個に含まれる格子点の数 $n_{\mathrm{sc}},n_{\mathrm{bcc}},n_{\mathrm{fcc}}$ を求めよ。

(2) 体心立方格子について，$\boldsymbol{a}_1=\dfrac{a}{2}(-\boldsymbol{e}_x+\boldsymbol{e}_y+\boldsymbol{e}_z)$，$\boldsymbol{a}_2=\dfrac{a}{2}(\boldsymbol{e}_x-\boldsymbol{e}_y+\boldsymbol{e}_z)$，$\boldsymbol{a}_3=\dfrac{a}{2}(\boldsymbol{e}_x+\boldsymbol{e}_y-\boldsymbol{e}_z)$ が基本並進ベクトルであることを示せ。体心立方格子の格子点は，整数 $m_1,m_2,m_3$ がすべて偶数またはすべて奇数であるような点 $\dfrac{a}{2}(m_1,m_2,m_3)$ の全体であることを用いてよい。

(3) (2) の基本単位胞の体積 $V_{\mathrm{bcc}}$ を求めよ。また，$a^3/V_{\mathrm{bcc}}$ が (1) の $n_{\mathrm{bcc}}$ と一致することを確かめよ。

(4) 面心立方格子について，原点から，原点を頂点にもつ慣用単位胞の $x=0$，$y=0$，$z=0$ の面の中心へ向かうベクトルをそれぞれ $\boldsymbol{a}_1',\boldsymbol{a}_2',\boldsymbol{a}_3'$ とし，これを基本並進ベクトルにとる。$\boldsymbol{a}_1',\boldsymbol{a}_2',\boldsymbol{a}_3'$ を成分で表し，基本単位胞の体積 $V_{\mathrm{fcc}}$ を求めよ。

---

## 解答・解説

### (1)
頂点の格子点はその頂点を共有する8個の単位胞に等しく属するので，1個の単位胞には $\dfrac{1}{8}$ 個として数えます。面の中心の格子点は2個の単位胞に共有されるので $\dfrac{1}{2}$ 個，立方体の中心の格子点は1個と数えます。

$$
\begin{aligned}
n_{\mathrm{sc}} &= 8\times\frac{1}{8}, \\
n_{\mathrm{bcc}} &= 8\times\frac{1}{8}+1, \\
n_{\mathrm{fcc}} &= 8\times\frac{1}{8}+6\times\frac{1}{2}
\end{aligned}
$$

より，

$$
\finalanswer{n_{\mathrm{sc}}=1},\qquad \finalanswer{n_{\mathrm{bcc}}=2},\qquad \finalanswer{n_{\mathrm{fcc}}=4}
$$

となります。

### (2)
示すことは2つあります。整数係数の組合せがすべて格子点になることと，すべての格子点が整数係数の組合せで書けることです。まず，整数 $n_1,n_2,n_3$ に対する点を成分で書きます。

$$
n_1\boldsymbol{a}_1+n_2\boldsymbol{a}_2+n_3\boldsymbol{a}_3=\frac{a}{2}\left(-n_1+n_2+n_3,\ n_1-n_2+n_3,\ n_1+n_2-n_3\right)
$$

3つの成分の係数どうしの差は，たとえば1番目と2番目では $2(n_2-n_1)$ のように偶数です。したがって係数はすべて偶数かすべて奇数になり，この点は格子点です。

逆に，格子点 $\dfrac{a}{2}(m_1,m_2,m_3)$ が与えられたとき，上の式と成分を比べて $n_1,n_2,n_3$ について解くと，

$$
n_1=\frac{m_2+m_3}{2},\qquad n_2=\frac{m_3+m_1}{2},\qquad n_3=\frac{m_1+m_2}{2}
$$

が得られます。$m_1,m_2,m_3$ はすべて同じ偶奇なので，2つの和は偶数で，$n_i$ は整数です。よって

$$
\finalanswer{\frac{a}{2}(m_1,m_2,m_3)=\frac{m_2+m_3}{2}\boldsymbol{a}_1+\frac{m_3+m_1}{2}\boldsymbol{a}_2+\frac{m_1+m_2}{2}\boldsymbol{a}_3}
$$

と，すべての格子点が整数係数の組合せで書けます。

### (3)
体積はスカラー三重積で求まり，成分の行列式として計算できます。

$$
\begin{aligned}
V_{\mathrm{bcc}}=\boldsymbol{a}_1\cdot(\boldsymbol{a}_2\times\boldsymbol{a}_3)
&=\left(\frac{a}{2}\right)^3
\begin{vmatrix}
-1 & 1 & 1\\
1 & -1 & 1\\
1 & 1 & -1
\end{vmatrix}
=\frac{a^3}{8}\times 4
\end{aligned}
$$

より，

$$
\finalanswer{V_{\mathrm{bcc}}=\frac{a^3}{2}}
$$

となります。$a^3/V_{\mathrm{bcc}}=2$ は $n_{\mathrm{bcc}}$ と一致します。基本単位胞には格子点がちょうど1個しか含まれないので，慣用単位胞の体積を基本単位胞の体積で割ると格子点の数になるのは当然です。

### (4)
$x=0$ の面の中心は $\left(0,\dfrac{a}{2},\dfrac{a}{2}\right)$ にあり，ほかの2面も同様です。

$$
\finalanswer{\boldsymbol{a}_1'=\frac{a}{2}(\boldsymbol{e}_y+\boldsymbol{e}_z)},\qquad
\finalanswer{\boldsymbol{a}_2'=\frac{a}{2}(\boldsymbol{e}_z+\boldsymbol{e}_x)},\qquad
\finalanswer{\boldsymbol{a}_3'=\frac{a}{2}(\boldsymbol{e}_x+\boldsymbol{e}_y)}
$$

体積は (3) と同じように行列式で計算します。

$$
V_{\mathrm{fcc}}=\left(\frac{a}{2}\right)^3
\begin{vmatrix}
0 & 1 & 1\\
1 & 0 & 1\\
1 & 1 & 0
\end{vmatrix}
=\frac{a^3}{8}\times 2
$$

より，

$$
\finalanswer{V_{\mathrm{fcc}}=\frac{a^3}{4}}
$$

となります。$a^3/V_{\mathrm{fcc}}=4$ は $n_{\mathrm{fcc}}$ と一致します。

===== FILE: 06solid_state/01/01_020.md =====
---
tags:
  - 基本
---

# 充填率と配位数

## 問題
同じ種類の原子を半径 $r$ の剛体球とみなし，最も近い原子どうしが接するように結晶をつくる。1つの原子から最も近い距離にある原子の数を配位数 $z$，慣用単位胞の体積のうち球が占める割合を充填率 $f$ とよぶ。慣用単位胞は一辺 $a$ の立方体とする。

ダイヤモンド構造は，面心立方格子の各格子点に，その点と，その点から $\dfrac{a}{4}(\boldsymbol{e}_x+\boldsymbol{e}_y+\boldsymbol{e}_z)$ だけずれた点の2つの原子を置いた構造である（図）。ここで $\boldsymbol{e}_x,\boldsymbol{e}_y,\boldsymbol{e}_z$ は立方体の辺の向きの単位ベクトルである。以下の問いに答えよ。

<!-- FIGURE problem: ダイヤモンド構造の慣用単位胞を描く。一辺 a の立方体で，左下手前の頂点を原点 O とし，x，y，z 軸を矢印で示す。8つの頂点と6つの面の中心に白丸を置く。立方体の内部，座標 (a/4)(1,1,1)，(a/4)(1,3,3)，(a/4)(3,1,3)，(a/4)(3,3,1) の4か所に黒丸を置く。原子どうしを結ぶ線（結合）は描かない。1辺に寸法線を引き，a とラベルを付ける。 -->

(1) 単純立方格子の各格子点に原子を置いた結晶について，最近接原子間距離，配位数 $z$，充填率 $f$ を求めよ。

(2) 体心立方格子の各格子点に原子を置いた結晶について，最近接原子間距離，$z$，$f$ を求めよ。

(3) 面心立方格子の各格子点に原子を置いた結晶について，最近接原子間距離，$z$，$f$ を求めよ。

(4) ダイヤモンド構造について，最近接原子間距離，$z$，$f$ を求めよ。

---

## 解答・解説

### (1)
最近接原子は立方体の辺に沿って隣り合う原子で，距離は $a$ です。$\pm\boldsymbol{e}_x,\pm\boldsymbol{e}_y,\pm\boldsymbol{e}_z$ の6方向にあるので $z=6$ です。球が接するので $r=\dfrac{a}{2}$ で，慣用単位胞には原子が1個含まれます。

$$
f=\frac{1\times\frac{4\pi}{3}\left(\frac{a}{2}\right)^3}{a^3}
$$

より，

$$
\finalanswer{z=6},\qquad \finalanswer{f=\frac{\pi}{6}\approx 0.524}
$$

となります（最近接原子間距離は $a$）。

### (2)
中心の原子と頂点の原子が体対角線に沿って接します。距離は体対角線の半分の $\dfrac{\sqrt{3}}{2}a$ で，頂点は8個あるので $z=8$ です。$r=\dfrac{\sqrt{3}}{4}a$ で，慣用単位胞には原子が2個含まれます。

$$
f=\frac{2\times\frac{4\pi}{3}\left(\frac{\sqrt{3}}{4}a\right)^3}{a^3}=\frac{8\pi}{3}\cdot\frac{3\sqrt{3}}{64}
$$

より，

$$
\finalanswer{z=8},\qquad \finalanswer{f=\frac{\sqrt{3}\pi}{8}\approx 0.680}
$$

となります（最近接原子間距離は $\dfrac{\sqrt{3}}{2}a$）。

### (3)
頂点の原子と，その頂点を含む面の中心の原子が面対角線に沿って接し，距離は $\dfrac{\sqrt{2}}{2}a$ です。原点から見ると最近接原子は $\dfrac{a}{2}(\pm1,\pm1,0)$ とその成分を入れ替えた位置にあり，$xy,yz,zx$ の各面に4個ずつで $z=12$ です。$r=\dfrac{\sqrt{2}}{4}a$ で，原子は4個含まれます。

$$
f=\frac{4\times\frac{4\pi}{3}\left(\frac{\sqrt{2}}{4}a\right)^3}{a^3}=\frac{16\pi}{3}\cdot\frac{2\sqrt{2}}{64}
$$

より，

$$
\finalanswer{z=12},\qquad \finalanswer{f=\frac{\sqrt{2}\pi}{6}\approx 0.740}
$$

となります（最近接原子間距離は $\dfrac{\sqrt{2}}{2}a$）。

### (4)
$\dfrac{a}{4}(1,1,1)$ にある原子の周りを調べます。面心立方格子の点 $(0,0,0)$，$\dfrac{a}{2}(1,1,0)$，$\dfrac{a}{2}(1,0,1)$，$\dfrac{a}{2}(0,1,1)$ との差はいずれも $\dfrac{a}{4}(\pm1,\pm1,\pm1)$ の形なので，距離は $\dfrac{\sqrt{3}}{4}a$ で4個です。これが最近接で $z=4$ となり，4個の原子は正四面体の頂点に並びます。$r=\dfrac{\sqrt{3}}{8}a$ で，慣用単位胞には面心立方の4個とずれた位置の4個を合わせて8個の原子が含まれます。

$$
f=\frac{8\times\frac{4\pi}{3}\left(\frac{\sqrt{3}}{8}a\right)^3}{a^3}=\frac{32\pi}{3}\cdot\frac{3\sqrt{3}}{512}
$$

より，

$$
\finalanswer{z=4},\qquad \finalanswer{f=\frac{\sqrt{3}\pi}{16}\approx 0.340}
$$

となります（最近接原子間距離は $\dfrac{\sqrt{3}}{4}a$）。充填率は面心立方の半分よりも小さく，すき間の多い構造です。ケイ素やゲルマニウムのような共有結合結晶でこの構造が現れるのは，球を密に詰めることよりも，結合の向きが正四面体になることが優先されるためです。

===== FILE: 06solid_state/01/01_030.md =====
---
tags:
  - 標準
---

# 逆格子ベクトルの構成

## 問題
3次元のブラベー格子の基本並進ベクトルを $\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3$ とし，基本単位胞の体積を $V=\boldsymbol{a}_1\cdot(\boldsymbol{a}_2\times\boldsymbol{a}_3)>0$ とする。$i,j=1,2,3$ に対して $\boldsymbol{a}_i\cdot\boldsymbol{b}_j=2\pi\delta_{ij}$ を満たすベクトル $\boldsymbol{b}_1,\boldsymbol{b}_2,\boldsymbol{b}_3$ を逆格子の基本ベクトルとよぶ。$\delta_{ij}$ はクロネッカーのデルタである。以下の問いに答えよ。

(1) $\boldsymbol{b}_1$ が $\boldsymbol{a}_2\times\boldsymbol{a}_3$ に平行であることを示し，$\boldsymbol{b}_1$ を $\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3$ と $V$ で表せ。$\boldsymbol{b}_2,\boldsymbol{b}_3$ も同様に表せ。

(2) 逆格子の基本単位胞の体積 $V^*=\boldsymbol{b}_1\cdot(\boldsymbol{b}_2\times\boldsymbol{b}_3)$ を $V$ で表せ。ベクトル三重積の公式 $\boldsymbol{A}\times(\boldsymbol{B}\times\boldsymbol{C})=\boldsymbol{B}(\boldsymbol{A}\cdot\boldsymbol{C})-\boldsymbol{C}(\boldsymbol{A}\cdot\boldsymbol{B})$ を用いてよい。

(3) 慣用単位胞の一辺が $a$ の面心立方格子の基本並進ベクトルを $\boldsymbol{a}_1=\dfrac{a}{2}(\boldsymbol{e}_y+\boldsymbol{e}_z)$，$\boldsymbol{a}_2=\dfrac{a}{2}(\boldsymbol{e}_z+\boldsymbol{e}_x)$，$\boldsymbol{a}_3=\dfrac{a}{2}(\boldsymbol{e}_x+\boldsymbol{e}_y)$ とする。$\boldsymbol{e}_x,\boldsymbol{e}_y,\boldsymbol{e}_z$ は直交座標の単位ベクトルである。逆格子の基本ベクトル $\boldsymbol{b}_1,\boldsymbol{b}_2,\boldsymbol{b}_3$ を求めよ。

(4) 一辺 $A$ の立方体を慣用単位胞とする体心立方格子は，$\dfrac{A}{2}(-\boldsymbol{e}_x+\boldsymbol{e}_y+\boldsymbol{e}_z)$，$\dfrac{A}{2}(\boldsymbol{e}_x-\boldsymbol{e}_y+\boldsymbol{e}_z)$，$\dfrac{A}{2}(\boldsymbol{e}_x+\boldsymbol{e}_y-\boldsymbol{e}_z)$ を基本並進ベクトルにもつ。このことを用いて，(3) の逆格子が体心立方格子であることを示し，その慣用単位胞の一辺 $A$ を求めよ。また，(2) の結果と体心立方格子の基本単位胞の体積が一致することを確かめよ。

---

## 解答・解説

### (1)
条件 $\boldsymbol{a}_2\cdot\boldsymbol{b}_1=\boldsymbol{a}_3\cdot\boldsymbol{b}_1=0$ から，$\boldsymbol{b}_1$ は $\boldsymbol{a}_2$ と $\boldsymbol{a}_3$ の両方に垂直です。$\boldsymbol{a}_2,\boldsymbol{a}_3$ は1次独立なので，両方に垂直な向きは $\boldsymbol{a}_2\times\boldsymbol{a}_3$ の向きに限られ，$\boldsymbol{b}_1=C\,\boldsymbol{a}_2\times\boldsymbol{a}_3$ と書けます。残りの条件 $\boldsymbol{a}_1\cdot\boldsymbol{b}_1=2\pi$ に代入すると $CV=2\pi$ です。添字を巡回させれば $\boldsymbol{b}_2,\boldsymbol{b}_3$ も得られます。

$$
\finalanswer{\boldsymbol{b}_1=\frac{2\pi}{V}\,\boldsymbol{a}_2\times\boldsymbol{a}_3},\qquad
\finalanswer{\boldsymbol{b}_2=\frac{2\pi}{V}\,\boldsymbol{a}_3\times\boldsymbol{a}_1},\qquad
\finalanswer{\boldsymbol{b}_3=\frac{2\pi}{V}\,\boldsymbol{a}_1\times\boldsymbol{a}_2}
$$

となります。

### (2)
まず $\boldsymbol{b}_2\times\boldsymbol{b}_3$ を計算します。三重積の公式で $\boldsymbol{A}=\boldsymbol{a}_3\times\boldsymbol{a}_1$，$\boldsymbol{B}=\boldsymbol{a}_1$，$\boldsymbol{C}=\boldsymbol{a}_2$ とおきます。

$$
\begin{aligned}
\boldsymbol{b}_2\times\boldsymbol{b}_3
&=\frac{(2\pi)^2}{V^2}(\boldsymbol{a}_3\times\boldsymbol{a}_1)\times(\boldsymbol{a}_1\times\boldsymbol{a}_2)\\
&=\frac{(2\pi)^2}{V^2}\Big[\boldsymbol{a}_1\{(\boldsymbol{a}_3\times\boldsymbol{a}_1)\cdot\boldsymbol{a}_2\}-\boldsymbol{a}_2\{(\boldsymbol{a}_3\times\boldsymbol{a}_1)\cdot\boldsymbol{a}_1\}\Big]
=\frac{(2\pi)^2}{V}\,\boldsymbol{a}_1
\end{aligned}
$$

$(\boldsymbol{a}_3\times\boldsymbol{a}_1)\cdot\boldsymbol{a}_2=V$ であり，$(\boldsymbol{a}_3\times\boldsymbol{a}_1)\cdot\boldsymbol{a}_1=0$ であることを使いました。これと $\boldsymbol{b}_1$ の内積をとり，$\boldsymbol{a}_1\cdot(\boldsymbol{a}_2\times\boldsymbol{a}_3)=V$ を使うと，

$$
\finalanswer{V^*=\frac{(2\pi)^3}{V}}
$$

となります。実空間の単位胞が小さいほど，逆空間の単位胞は大きくなります。

### (3)
$V$ と外積を計算して (1) に代入します。$\boldsymbol{a}_2\times\boldsymbol{a}_3=\dfrac{a^2}{4}(1,0,1)\times(1,1,0)=\dfrac{a^2}{4}(-1,1,1)$ で，$V=\boldsymbol{a}_1\cdot(\boldsymbol{a}_2\times\boldsymbol{a}_3)=\dfrac{a^3}{8}\times 2=\dfrac{a^3}{4}$ です。

$$
\boldsymbol{b}_1=\frac{2\pi}{a^3/4}\cdot\frac{a^2}{4}(-1,1,1)
$$

$\boldsymbol{b}_2,\boldsymbol{b}_3$ も同様に計算すると，

$$
\finalanswer{\boldsymbol{b}_1=\frac{2\pi}{a}(-\boldsymbol{e}_x+\boldsymbol{e}_y+\boldsymbol{e}_z)},\quad
\finalanswer{\boldsymbol{b}_2=\frac{2\pi}{a}(\boldsymbol{e}_x-\boldsymbol{e}_y+\boldsymbol{e}_z)},\quad
\finalanswer{\boldsymbol{b}_3=\frac{2\pi}{a}(\boldsymbol{e}_x+\boldsymbol{e}_y-\boldsymbol{e}_z)}
$$

となります。たとえば $\boldsymbol{a}_1\cdot\boldsymbol{b}_1=\pi(0+1+1)=2\pi$，$\boldsymbol{a}_1\cdot\boldsymbol{b}_2=\pi(0-1+1)=0$ となり，定義を満たしています。

### (4)
(3) の3つのベクトルは，体心立方格子の基本並進ベクトルで $\dfrac{A}{2}=\dfrac{2\pi}{a}$ とおいたものと一致します。基本並進ベクトルが一致すれば，その整数係数の組合せ全体である格子も一致するので，逆格子は体心立方格子です。

$$
\finalanswer{A=\frac{4\pi}{a}}
$$

体積を確かめます。(2) からは $V^*=\dfrac{(2\pi)^3}{a^3/4}=\dfrac{32\pi^3}{a^3}$ です。一方，一辺 $A$ の体心立方格子の基本単位胞の体積は，慣用単位胞の体積を格子点の数2で割った $\dfrac{A^3}{2}=\dfrac{1}{2}\left(\dfrac{4\pi}{a}\right)^3=\dfrac{32\pi^3}{a^3}$ で，両者は一致します。逆に，体心立方格子の逆格子は面心立方格子になります。

===== FILE: 06solid_state/01/01_040.md =====
---
tags:
  - 標準
---

# ミラー指数と格子面間隔

## 問題
ブラベー格子の基本並進ベクトルを $\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3$，逆格子の基本ベクトルを $\boldsymbol{b}_1,\boldsymbol{b}_2,\boldsymbol{b}_3$（$\boldsymbol{a}_i\cdot\boldsymbol{b}_j=2\pi\delta_{ij}$）とする。互いに素な整数 $h,k,l$（ここではすべて0でないとする）に対し，3点 $\boldsymbol{a}_1/h$，$\boldsymbol{a}_2/k$，$\boldsymbol{a}_3/l$ を通る平面に平行な格子面の族を $(hkl)$ 面とよび，隣り合う格子面の間隔を $d_{hkl}$ とする。また $\boldsymbol{G}_{hkl}=h\boldsymbol{b}_1+k\boldsymbol{b}_2+l\boldsymbol{b}_3$ とおく。以下の問いに答えよ。

(1) $\boldsymbol{G}_{hkl}$ が $(hkl)$ 面に垂直であることを示せ。

(2) $d_{hkl}$ を $|\boldsymbol{G}_{hkl}|$ で表せ。格子点 $\boldsymbol{R}=n_1\boldsymbol{a}_1+n_2\boldsymbol{a}_2+n_3\boldsymbol{a}_3$（$n_i$ は整数）に対して $\boldsymbol{G}_{hkl}\cdot\boldsymbol{R}$ を考えよ。

(3) 格子定数 $a$ の単純立方格子（$\boldsymbol{a}_1=a\boldsymbol{e}_x$，$\boldsymbol{a}_2=a\boldsymbol{e}_y$，$\boldsymbol{a}_3=a\boldsymbol{e}_z$）について，$d_{hkl}$ を $a,h,k,l$ で表せ。

(4) 慣用単位胞の一辺が $a$ の面心立方格子について，$x$ 軸に垂直な格子面の族の面間隔 $d_{\perp[100]}$ と，ベクトル $\boldsymbol{e}_x+\boldsymbol{e}_y+\boldsymbol{e}_z$ に垂直な格子面の族の面間隔 $d_{\perp[111]}$ を求めよ。面心立方格子の逆格子は，一辺 $\dfrac{4\pi}{a}$ の立方体を慣用単位胞とする体心立方格子であることを用いてよい。

---

## 解答・解説

### (1)
平面上の3点の差をとると，平面に平行な1次独立な2つのベクトル $\dfrac{\boldsymbol{a}_1}{h}-\dfrac{\boldsymbol{a}_2}{k}$ と $\dfrac{\boldsymbol{a}_1}{h}-\dfrac{\boldsymbol{a}_3}{l}$ が得られます。これらと $\boldsymbol{G}_{hkl}$ の内積を，$\boldsymbol{a}_i\cdot\boldsymbol{b}_j=2\pi\delta_{ij}$ を使って計算します。

$$
\finalanswer{\boldsymbol{G}_{hkl}\cdot\left(\frac{\boldsymbol{a}_1}{h}-\frac{\boldsymbol{a}_2}{k}\right)=2\pi-2\pi=0},\qquad
\finalanswer{\boldsymbol{G}_{hkl}\cdot\left(\frac{\boldsymbol{a}_1}{h}-\frac{\boldsymbol{a}_3}{l}\right)=0}
$$

平面内の1次独立な2方向の両方に垂直なので，$\boldsymbol{G}_{hkl}$ は $(hkl)$ 面に垂直となります。

### (2)
格子点との内積を計算すると，

$$
\boldsymbol{G}_{hkl}\cdot\boldsymbol{R}=2\pi(hn_1+kn_2+ln_3)
$$

となり，$2\pi$ の整数倍です。したがって，すべての格子点は $\boldsymbol{G}_{hkl}$ に垂直な平面の族 $\boldsymbol{G}_{hkl}\cdot\boldsymbol{r}=2\pi m$（$m$ は整数）のどれかに乗ります。

次に，どの平面にも格子点が乗っていることを確かめます。$h,k,l$ は互いに素なので，任意の整数 $m$ に対して $hn_1+kn_2+ln_3=m$ を満たす整数 $n_i$ が存在します（ベズーの等式）。したがって空の平面はなく，この平面の族がちょうど $(hkl)$ 面の族です。実際，$\boldsymbol{G}_{hkl}\cdot\dfrac{\boldsymbol{a}_1}{h}=2\pi$ なので，問題文の3点を通る平面は $m=1$ の面にあたります。平面 $\boldsymbol{G}\cdot\boldsymbol{r}=2\pi m$ と原点との距離は $2\pi m/|\boldsymbol{G}|$ なので，

$$
\finalanswer{d_{hkl}=\frac{2\pi}{|\boldsymbol{G}_{hkl}|}}
$$

となります。

### (3)
単純立方格子の逆格子の基本ベクトルは $\boldsymbol{b}_i=\dfrac{2\pi}{a}\boldsymbol{e}_i$ なので，$\boldsymbol{G}_{hkl}=\dfrac{2\pi}{a}(h,k,l)$ です。(2) に代入すると，

$$
\finalanswer{d_{hkl}=\frac{a}{\sqrt{h^2+k^2+l^2}}}
$$

となります。

### (4)
(2) の議論からわかるように，ある方向の面間隔は，その方向で最短の逆格子ベクトルの長さ $G_{\min}$ を使って $2\pi/G_{\min}$ と表せます。逆格子（一辺 $\dfrac{4\pi}{a}$ の体心立方格子）の点は，立方体の頂点 $\dfrac{4\pi}{a}(n_1,n_2,n_3)$ と中心 $\dfrac{2\pi}{a}(\text{奇数},\text{奇数},\text{奇数})$ からなります。

$x$ 軸上にある逆格子点は頂点だけなので，最短は $\dfrac{4\pi}{a}\boldsymbol{e}_x$ です。$(1,1,1)$ 方向では，中心の点 $\dfrac{2\pi}{a}(1,1,1)$ が最短で，長さは $\dfrac{2\sqrt{3}\pi}{a}$ です。

$$
\finalanswer{d_{\perp[100]}=\frac{a}{2}},\qquad \finalanswer{d_{\perp[111]}=\frac{a}{\sqrt{3}}}
$$

となります。

実空間でも確かめられます。面心立方の格子点は $\dfrac{a}{2}(m_1,m_2,m_3)$（$m_1+m_2+m_3$ が偶数）なので，$x$ 座標は $\dfrac{a}{2}$ の整数倍をとり，$x+y+z$ は $a$ の整数倍をとります。面 $x+y+z=na$ どうしの間隔は $a/\sqrt{3}$ です。面心立方格子では $(111)$ 面の間隔が最も広く，この面は原子が最も密に詰まった面です。

===== FILE: 06solid_state/01/01_050.md =====
---
tags:
  - 標準
---

# ブリルアンゾーン

## 問題
2次元のブラベー格子の基本並進ベクトルを $\boldsymbol{a}_1,\boldsymbol{a}_2$ とし，同じ平面内で $\boldsymbol{a}_i\cdot\boldsymbol{b}_j=2\pi\delta_{ij}$（$i,j=1,2$）を満たす $\boldsymbol{b}_1,\boldsymbol{b}_2$ を逆格子の基本ベクトルとする。原点と他の逆格子点を結ぶ線分の垂直二等分線で囲まれた，原点を含む最小の領域を第1ブリルアンゾーン（以下 BZ）とよぶ。$\boldsymbol{e}_x,\boldsymbol{e}_y$ は直交座標の単位ベクトル，$a>0$ は定数である。以下の問いに答えよ。

(1) 正方格子 $\boldsymbol{a}_1=a\boldsymbol{e}_x$，$\boldsymbol{a}_2=a\boldsymbol{e}_y$ について，$\boldsymbol{b}_1,\boldsymbol{b}_2$ を求め，BZ の境界を波数 $(k_x,k_y)$ の式で表し，BZ の面積 $S_{\mathrm{sq}}$ を求めよ。

(2) 六方格子（三角格子）$\boldsymbol{a}_1=a\boldsymbol{e}_x$，$\boldsymbol{a}_2=a\left(\dfrac{1}{2}\boldsymbol{e}_x+\dfrac{\sqrt{3}}{2}\boldsymbol{e}_y\right)$ について，$\boldsymbol{b}_1,\boldsymbol{b}_2$ とその長さ，および $\boldsymbol{b}_1$ と $\boldsymbol{b}_2$ のなす角を求めよ。

(3) (2) の格子の BZ について，原点から境界の各辺の中点までの距離 $k_{\mathrm{M}}$，原点から頂点までの距離 $k_{\mathrm{K}}$，面積 $S_{\mathrm{hex}}$ を求めよ。また，$S_{\mathrm{hex}}=|\boldsymbol{b}_1\times\boldsymbol{b}_2|$ であることを確かめよ。

(4) 一般の2次元格子が $N_1\times N_2$ 個の単位胞からなり，周期境界条件 $e^{i\boldsymbol{k}\cdot N_1\boldsymbol{a}_1}=e^{i\boldsymbol{k}\cdot N_2\boldsymbol{a}_2}=1$ を課す。BZ の面積が $|\boldsymbol{b}_1\times\boldsymbol{b}_2|$ に等しいことを用いて，BZ 内で許される波数 $\boldsymbol{k}$ の数を求めよ。

---

## 解答・解説

### (1)
$\boldsymbol{b}_1$ は $\boldsymbol{a}_2$ に垂直で $\boldsymbol{a}_1\cdot\boldsymbol{b}_1=2\pi$ を満たすので，$x$ 方向を向いた長さ $2\pi/a$ のベクトルです。

$$
\finalanswer{\boldsymbol{b}_1=\frac{2\pi}{a}\boldsymbol{e}_x},\qquad \finalanswer{\boldsymbol{b}_2=\frac{2\pi}{a}\boldsymbol{e}_y}
$$

原点に最も近い逆格子点 $\pm\boldsymbol{b}_1,\pm\boldsymbol{b}_2$ との垂直二等分線は，$k_x=\pm\pi/a$ と $k_y=\pm\pi/a$ です。次に近い $\dfrac{2\pi}{a}(\pm1,\pm1)$ との二等分線は，たとえば $k_x+k_y=2\pi/a$ のように正方形の頂点を通るだけなので，内側に切り込みません。

$$
\finalanswer{|k_x|=\frac{\pi}{a}\ (|k_y|\le\tfrac{\pi}{a}),\quad |k_y|=\frac{\pi}{a}\ (|k_x|\le\tfrac{\pi}{a})},\qquad \finalanswer{S_{\mathrm{sq}}=\frac{4\pi^2}{a^2}}
$$

となります。

### (2)
$\boldsymbol{b}_2$ は $\boldsymbol{a}_1=a\boldsymbol{e}_x$ に垂直なので $y$ 方向を向き，$\boldsymbol{a}_2\cdot\boldsymbol{b}_2=2\pi$ から大きさが決まります。$\boldsymbol{b}_1=\beta_x\boldsymbol{e}_x+\beta_y\boldsymbol{e}_y$ とおくと，$\boldsymbol{a}_1\cdot\boldsymbol{b}_1=2\pi$ から $\beta_x=2\pi/a$ です。さらに $\boldsymbol{a}_2\cdot\boldsymbol{b}_1=0$ から $\dfrac{1}{2}\beta_x+\dfrac{\sqrt{3}}{2}\beta_y=0$ となります。

$$
\finalanswer{\boldsymbol{b}_1=\frac{2\pi}{a}\left(\boldsymbol{e}_x-\frac{1}{\sqrt{3}}\boldsymbol{e}_y\right)},\qquad
\finalanswer{\boldsymbol{b}_2=\frac{4\pi}{\sqrt{3}a}\boldsymbol{e}_y}
$$

長さは $|\boldsymbol{b}_1|^2=\dfrac{4\pi^2}{a^2}\cdot\dfrac{4}{3}$ から求まり，$\boldsymbol{b}_1\cdot\boldsymbol{b}_2=-\dfrac{8\pi^2}{3a^2}$ から $\cos\phi=-\dfrac{1}{2}$ です。

$$
\finalanswer{|\boldsymbol{b}_1|=|\boldsymbol{b}_2|=\frac{4\pi}{\sqrt{3}a}},\qquad \finalanswer{\phi=120^\circ}
$$

となります。逆格子も三角格子で，実格子に対して $30^\circ$ 回転しています。

### (3)
最も近い逆格子点は $\pm\boldsymbol{b}_1,\pm\boldsymbol{b}_2,\pm(\boldsymbol{b}_1+\boldsymbol{b}_2)$ の6個で，いずれも長さ $\dfrac{4\pi}{\sqrt{3}a}$ です。その垂直二等分線が正六角形をつくり，辺の中点までの距離はその半分です。頂点までの距離は，中点までの距離を $\cos 30^\circ$ で割れば得られます。

$$
\finalanswer{k_{\mathrm{M}}=\frac{2\pi}{\sqrt{3}a}},\qquad \finalanswer{k_{\mathrm{K}}=\frac{4\pi}{3a}}
$$

BZ の形を図に示します。

<!-- FIGURE solution (3): 逆格子の三角格子を黒点で描く（原点 Γ を中心に，周囲6点と，その外側の点も少し）。原点から b1（右下がり，x 軸から -30°）と b2（真上）の矢印を描きラベルを付ける。原点と周囲6点を結ぶ線分の垂直二等分線を細い破線で描き，それらが囲む正六角形（頂点が x 軸上にない向き：辺の1つが b2 に垂直で上側にある）を太線で示して BZ とラベル。六角形の上辺の中点に M，右上の頂点に K のラベルを付ける。 -->

この正六角形の頂点が，次に近い逆格子点（距離 $2\pi/a$）の二等分線の内側にあることも確かめておきます。$k_{\mathrm{K}}=\dfrac{4\pi}{3a}<\dfrac{\pi}{a}\cdot 2\cdot\dfrac{1}{2}\cdot 2=\dfrac{2\pi}{a}\cdot\dfrac{1}{1}\cdot\dfrac{1}{1}$ は明らかに満たされ，その二等分線までの距離 $\pi/a\cdot\sqrt{3}\approx 5.44/a$ は $k_{\mathrm{K}}\approx 4.19/a$ より大きいので，六角形は切られません。正六角形の面積は，中点までの距離 $h$ を使って $2\sqrt{3}h^2$ です。

$$
S_{\mathrm{hex}}=2\sqrt{3}\left(\frac{2\pi}{\sqrt{3}a}\right)^2,\qquad
|\boldsymbol{b}_1\times\boldsymbol{b}_2|=\frac{2\pi}{a}\cdot\frac{4\pi}{\sqrt{3}a}
$$

より，

$$
\finalanswer{S_{\mathrm{hex}}=\frac{8\pi^2}{\sqrt{3}a^2}=|\boldsymbol{b}_1\times\boldsymbol{b}_2|}
$$

となります。

### (4)
$\boldsymbol{k}=x_1\boldsymbol{b}_1+x_2\boldsymbol{b}_2$ と展開して周期境界条件に代入すると，$e^{2\pi i N_1x_1}=e^{2\pi iN_2x_2}=1$ です。したがって

$$
\boldsymbol{k}=\frac{m_1}{N_1}\boldsymbol{b}_1+\frac{m_2}{N_2}\boldsymbol{b}_2\qquad(m_1,m_2\ \text{は整数})
$$

となり，許される $\boldsymbol{k}$ は面積 $\dfrac{|\boldsymbol{b}_1\times\boldsymbol{b}_2|}{N_1N_2}$ の平行四辺形ごとに1個ずつ並びます。BZ の面積をこの面積で割ると，

$$
\finalanswer{(\text{BZ 内の}\ \boldsymbol{k}\ \text{の数})=N_1N_2}
$$

となります。BZ 内の波数の数は単位胞の数に等しくなります。この事実は，格子振動のモード数や電子のバンドの状態数を数えるときに使います。

===== FILE: 06solid_state/01/01_060.md =====
---
tags:
  - 発展
---

# 結晶の回転対称性

## 問題
2次元のブラベー格子を考え，基本並進ベクトルを $\boldsymbol{a}_1,\boldsymbol{a}_2$ とする。ある格子点の周りの角 $\theta$ の回転 $\mathsf{R}(\theta)$ によって格子全体が自分自身に重なるとき，格子はこの回転について対称であるという。$n$ を正の整数として，$\theta=2\pi/n$ の回転について対称であることを $n$ 回回転対称性とよぶ。回転の中心を原点にとる。以下の問いに答えよ。

(1) $\mathsf{R}\boldsymbol{a}_j=\sum_{i=1}^{2}M_{ij}\boldsymbol{a}_i$（$j=1,2$）と書いたとき，係数 $M_{ij}$ がすべて整数であることを示せ。

(2) $\mathsf{R}$ を直交座標で表した $2\times2$ 行列と，(1) の行列 $M=(M_{ij})$ の関係を考えて，$\operatorname{tr}M=2\cos\theta$ を示せ。

(3) 格子と両立する回転対称性の $n$ をすべて求めよ。

(4) 3次元のブラベー格子で，ある軸の周りの角 $\theta=2\pi/n$ の回転について格子が対称であるとき，許される $n$ が (3) と同じであることを示せ。

---

## 解答・解説

### (1)
$\boldsymbol{a}_j$ は格子点なので，格子を自分自身に重ねる回転で移った $\mathsf{R}\boldsymbol{a}_j$ も格子点です。格子点はすべて基本並進ベクトルの整数係数の組合せで書けるので，

$$
\finalanswer{\mathsf{R}\boldsymbol{a}_j=M_{1j}\boldsymbol{a}_1+M_{2j}\boldsymbol{a}_2,\quad M_{ij}\in\mathbb{Z}}
$$

となります。$\boldsymbol{a}_1,\boldsymbol{a}_2$ は1次独立なので，係数は一意に決まります。

### (2)
$\boldsymbol{a}_1,\boldsymbol{a}_2$ の直交座標成分を列に並べた行列を $A$ とします。$A$ は1次独立な列をもつので正則です。直交座標での回転行列を $R$ とすると，(1) の関係は行列で $RA=AM$ と書けます。

$$
M=A^{-1}RA
$$

トレースは相似変換で変わらない（$\operatorname{tr}(XY)=\operatorname{tr}(YX)$）ので，$\operatorname{tr}M=\operatorname{tr}R$ です。直交座標の回転行列は

$$
R=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}
$$

なので，

$$
\finalanswer{\operatorname{tr}M=2\cos\theta}
$$

となります。(1) から左辺は整数なので，$2\cos\theta$ も整数でなければなりません。

### (3)
$-2\le 2\cos\theta\le 2$ なので，$2\cos\theta$ のとりうる値は $-2,-1,0,1,2$ の5つです。それぞれについて $\theta=2\pi/n$ を満たす正の整数 $n$ を求めます。

$$
\begin{aligned}
2\cos\theta=2 &: \theta=2\pi,\ n=1\\
2\cos\theta=1 &: \theta=\pi/3,\ n=6\\
2\cos\theta=0 &: \theta=\pi/2,\ n=4\\
2\cos\theta=-1 &: \theta=2\pi/3,\ n=3\\
2\cos\theta=-2 &: \theta=\pi,\ n=2
\end{aligned}
$$

より，

$$
\finalanswer{n=1,2,3,4,6}
$$

となります。逆に，これらの $n$ は正方格子（$n=4$）や三角格子（$n=6$）などで実際に実現します。たとえば5回回転では $2\cos 72^\circ\approx 0.618$ となって整数でないので，並進対称性と両立しません。

### (4)
3次元でも，回転で格子点は格子点に移るので，(1) と同じ議論で $3\times3$ の行列 $M$ の成分は整数です。(2) と同様に $\operatorname{tr}M$ は直交座標の回転行列のトレースに等しくなります。回転軸を $z$ 軸にとると，その回転行列のトレースは

$$
\operatorname{tr}R=\operatorname{tr}\begin{pmatrix}\cos\theta & -\sin\theta & 0\\ \sin\theta & \cos\theta & 0\\ 0 & 0 & 1\end{pmatrix}=1+2\cos\theta
$$

です。これが整数であることは $2\cos\theta$ が整数であることと同値なので，

$$
\finalanswer{n=1,2,3,4,6}
$$

となり，(3) と同じ結果です。準結晶では5回対称の回折像が観測されますが，これは準結晶が周期的な並進対称性をもたないためです。

===== FILE: 06solid_state/02/02_010.md =====
---
tags:
  - 標準
---

# イオン結晶の凝集エネルギーとマーデルング定数

## 問題
電荷 $+e$ と $-e$ のイオンが間隔 $r$ で交互に並んだ一次元のイオン鎖を考える（図）。イオンは全部で $2N$ 個あり（$N\gg1$），端の効果を無視するため鎖は環状につながっているとみなす。すべてのイオンの組の間にクーロン相互作用がはたらき，さらに最近接のイオンの組の間にだけ反発のポテンシャルエネルギー $C/r^n$（$C>0$，$n>1$）がはたらく。真空の誘電率を $\varepsilon_0$ とする。

1つのイオンが他のすべてのイオンから受けるクーロンのポテンシャルエネルギーの和を $-\dfrac{\alpha e^2}{4\pi\varepsilon_0 r}$ と書き，$\alpha$ をマーデルング定数とよぶ。以下の問いに答えよ。

<!-- FIGURE problem: 水平な直線上に等間隔で白丸（+e）と黒丸（-e）を交互に7〜9個並べる。中央の白丸の上に「基準」と書き，その右隣の黒丸との間に寸法線を引いて r とラベル。白丸に +e，黒丸に -e のラベルを付ける（数個だけでよい）。両端は点線で続くことを示す。 -->

(1) $\alpha$ を求めよ。$\ln(1+x)$ の $x=1$ でのテイラー展開を用いてよい。

(2) 鎖全体のポテンシャルエネルギー $U(r)$ を $N,\alpha,r,C,n$ で表せ。

(3) 平衡間隔 $r_0$ を求めよ。

(4) 平衡状態での鎖全体のエネルギー $U_0=U(r_0)$ を，$r_0$ を用いて表せ。

---

## 解答・解説

### (1)
$+e$ のイオンを基準にとります。距離 $mr$（$m=1,2,\ldots$）の位置には左右に1個ずつイオンがあり，その電荷は $m$ が奇数なら $-e$，偶数なら $+e$ です。したがって，基準のイオンとの相互作用エネルギーの和は

$$
\sum_{m=1}^{\infty}2\cdot\frac{(-1)^m e^2}{4\pi\varepsilon_0\,mr}
=-\frac{e^2}{4\pi\varepsilon_0 r}\cdot 2\sum_{m=1}^{\infty}\frac{(-1)^{m+1}}{m}
$$

となります。$\ln(1+x)=x-\dfrac{x^2}{2}+\dfrac{x^3}{3}-\cdots$ で $x=1$ とおくと，和は $\ln 2$ です。

$$
\finalanswer{\alpha=2\ln 2\approx 1.386}
$$

となります。基準を $-e$ のイオンにとっても同じ値になります。

### (2)
クーロンエネルギーは，各イオンについて (1) の和を足し合わせ，同じ組を2回数えているので $\dfrac{1}{2}$ をかけて求めます。

$$
U_{\mathrm{C}}=\frac{1}{2}\cdot 2N\cdot\left(-\frac{\alpha e^2}{4\pi\varepsilon_0 r}\right)=-\frac{N\alpha e^2}{4\pi\varepsilon_0 r}
$$

環状の鎖では，最近接の組の数はイオンの数と同じ $2N$ 個です。反発エネルギーは $2N\cdot C/r^n$ となるので，

$$
\finalanswer{U(r)=N\left(-\frac{\alpha e^2}{4\pi\varepsilon_0 r}+\frac{2C}{r^n}\right)}
$$

となります。

### (3)
平衡間隔では $U$ が極小になるので，$\dfrac{\mathrm{d}U}{\mathrm{d}r}=0$ とおきます。

$$
\frac{\mathrm{d}U}{\mathrm{d}r}=N\left(\frac{\alpha e^2}{4\pi\varepsilon_0 r^2}-\frac{2nC}{r^{n+1}}\right)=0
$$

より $r_0^{\,n-1}=\dfrac{8\pi\varepsilon_0 nC}{\alpha e^2}$ です。$\alpha=2\ln 2$ を代入すると，

$$
\finalanswer{r_0=\left(\frac{4\pi\varepsilon_0 nC}{e^2\ln 2}\right)^{1/(n-1)}}
$$

となります。$n>1$ なので，$r$ が小さいところでは反発項が勝ち，大きいところではクーロン引力が勝ちます。そのため，この停留点は確かに極小です。

### (4)
(3) の条件から $\dfrac{2C}{r_0^{\,n}}=\dfrac{1}{n}\cdot\dfrac{\alpha e^2}{4\pi\varepsilon_0 r_0}$ です。これを $U$ に代入して反発項を消去します。

$$
U_0=-\frac{N\alpha e^2}{4\pi\varepsilon_0 r_0}\left(1-\frac{1}{n}\right)
$$

$\alpha=2\ln 2$ を代入すると，

$$
\finalanswer{U_0=-\frac{Ne^2\ln 2}{2\pi\varepsilon_0 r_0}\left(1-\frac{1}{n}\right)}
$$

となります。反発の効果は $\dfrac{1}{n}$ の割合でエネルギーを浅くするだけです。$n\to\infty$（硬い芯）の極限では，純粋なクーロンエネルギー $-\dfrac{N\alpha e^2}{4\pi\varepsilon_0 r_0}$ に一致します。

===== FILE: 06solid_state/02/02_020.md =====
---
tags:
  - 標準
---

# ボルン・マイヤー型反発と体積弾性率

## 問題
NaCl 型構造のイオン結晶が $N$ 個のイオン対からなり，最近接イオン間距離を $R$ とする。各イオンの最近接イオンの数を $z$，マーデルング定数を $\alpha$ とし，最近接イオンの間にだけボルン・マイヤー型の反発 $\lambda e^{-R/\rho}$（$\lambda>0$，$\rho>0$）がはたらくとすると，結晶のポテンシャルエネルギーは

$$
U(R)=N\left(z\lambda e^{-R/\rho}-\frac{\alpha e^2}{4\pi\varepsilon_0 R}\right)
$$

と書ける。$\varepsilon_0$ は真空の誘電率である。絶対零度を考え，圧力は $p=-\dfrac{\mathrm{d}U}{\mathrm{d}V}$，体積弾性率は $B=-V\dfrac{\mathrm{d}p}{\mathrm{d}V}$ で定義する。以下の問いに答えよ。

(1) 平衡での最近接距離 $R_0$ が満たす条件式を求めよ。

(2) 平衡でのエネルギー $U_0=U(R_0)$ を $N,\alpha,R_0,\rho$ で表せ。

(3) NaCl 型構造では結晶の体積が $V=2NR^3$ となることを示せ。さらに，平衡での体積弾性率が $B=\dfrac{1}{18NR_0}\left.\dfrac{\mathrm{d}^2U}{\mathrm{d}R^2}\right|_{R_0}$ と表せることを示せ。

(4) $B$ を $\alpha,R_0,\rho$ で表せ。また，NaCl の値 $\alpha=1.748$，$R_0=0.282\ \mathrm{nm}$，$\rho=0.0321\ \mathrm{nm}$，$\dfrac{e^2}{4\pi\varepsilon_0}=2.307\times10^{-28}\ \mathrm{J\,m}$ を用いて $B$ の数値を求めよ。

---

## 解答・解説

### (1)
平衡では $U$ が極小になるので，$R$ で微分して0とおきます。

$$
\frac{\mathrm{d}U}{\mathrm{d}R}=N\left(-\frac{z\lambda}{\rho}e^{-R/\rho}+\frac{\alpha e^2}{4\pi\varepsilon_0 R^2}\right)=0
$$

より，

$$
\finalanswer{z\lambda e^{-R_0/\rho}=\frac{\rho\,\alpha e^2}{4\pi\varepsilon_0 R_0^{\,2}}}
$$

となります。この条件式は，反発力とクーロン引力が釣り合うことを表しています。

### (2)
(1) の条件式を使って $U$ の反発項を消去します。

$$
U_0=N\left(\frac{\rho}{R_0}\cdot\frac{\alpha e^2}{4\pi\varepsilon_0 R_0}-\frac{\alpha e^2}{4\pi\varepsilon_0 R_0}\right)
$$

より，

$$
\finalanswer{U_0=-\frac{N\alpha e^2}{4\pi\varepsilon_0 R_0}\left(1-\frac{\rho}{R_0}\right)}
$$

となります。反発の効果は $\rho/R_0$（典型的に1割程度）の割合でエネルギーを浅くします。

### (3)
NaCl 型構造の慣用単位胞は一辺 $2R$ の立方体で，Na$^+$ と Cl$^-$ がそれぞれ面心立方の位置に4個ずつ入るので，イオン対4個を含みます。イオン対1個あたりの体積は $(2R)^3/4=2R^3$ で，

$$
\finalanswer{V=2NR^3}
$$

となります。

次に $B$ を $R$ の微分で書き直します。$p=-\dfrac{\mathrm{d}U}{\mathrm{d}V}$ を代入すると $B=V\dfrac{\mathrm{d}^2U}{\mathrm{d}V^2}$ です。$\dfrac{\mathrm{d}V}{\mathrm{d}R}=6NR^2$ なので $\dfrac{\mathrm{d}}{\mathrm{d}V}=\dfrac{1}{6NR^2}\dfrac{\mathrm{d}}{\mathrm{d}R}$ となり，2階微分は

$$
\frac{\mathrm{d}^2U}{\mathrm{d}V^2}=\frac{1}{(6NR^2)^2}\frac{\mathrm{d}^2U}{\mathrm{d}R^2}+\frac{\mathrm{d}U}{\mathrm{d}R}\cdot\frac{1}{6NR^2}\frac{\mathrm{d}}{\mathrm{d}R}\left(\frac{1}{6NR^2}\right)
$$

と書けます。平衡では第2項が $\dfrac{\mathrm{d}U}{\mathrm{d}R}=0$ により消えるので，

$$
\finalanswer{B=\frac{2NR_0^{\,3}}{36N^2R_0^{\,4}}\left.\frac{\mathrm{d}^2U}{\mathrm{d}R^2}\right|_{R_0}=\frac{1}{18NR_0}\left.\frac{\mathrm{d}^2U}{\mathrm{d}R^2}\right|_{R_0}}
$$

となります。

### (4)
2階微分を計算し，(1) の条件式で指数関数を消去します。

$$
\begin{aligned}
\left.\frac{\mathrm{d}^2U}{\mathrm{d}R^2}\right|_{R_0}
&=N\left(\frac{z\lambda}{\rho^2}e^{-R_0/\rho}-\frac{2\alpha e^2}{4\pi\varepsilon_0 R_0^{\,3}}\right)
=\frac{N\alpha e^2}{4\pi\varepsilon_0 R_0^{\,3}}\left(\frac{R_0}{\rho}-2\right)
\end{aligned}
$$

(3) に代入すると，

$$
\finalanswer{B=\frac{\alpha e^2}{72\pi\varepsilon_0 R_0^{\,4}}\left(\frac{R_0}{\rho}-2\right)}
$$

となります。

数値は，$\dfrac{\alpha e^2}{72\pi\varepsilon_0}=\dfrac{\alpha}{18}\cdot\dfrac{e^2}{4\pi\varepsilon_0}=2.240\times10^{-29}\ \mathrm{J\,m}$，$R_0^{\,4}=6.324\times10^{-39}\ \mathrm{m^4}$，$\dfrac{R_0}{\rho}-2=6.785$ を使って計算します。

$$
\finalanswer{B\approx 2.4\times10^{10}\ \mathrm{Pa}}
$$

となります。これは NaCl の実測値（約 $24\ \mathrm{GPa}$）とよく一致します。逆に，実測の $B$ と $R_0$ から，反発の到達距離 $\rho$ を決めることもできます。

===== FILE: 06solid_state/02/02_030.md =====
---
tags:
  - 標準
---

# ファンデルワールス結晶とレナード・ジョーンズ

## 問題
希ガス原子 $N$ 個が面心立方格子に並んだ結晶を考える。2原子間のポテンシャルエネルギーはレナード・ジョーンズ型

$$
\phi(r)=4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right]
$$

（$\varepsilon>0$，$\sigma>0$）とし，すべての原子の組の間にはたらくとする。最近接原子間距離を $R$ とし，1つの原子から $j$ 番目の原子までの距離を $p_jR$ と書いて，格子和を $A_n=\sum_{j}p_j^{-n}$（和は基準の原子以外のすべての原子にわたる）と定義する。面心立方格子では $A_{12}=12.131$，$A_6=14.454$ である。端の効果は無視する。以下の問いに答えよ。

(1) 結晶全体のポテンシャルエネルギー $U(R)$ を $N,\varepsilon,\sigma,R,A_{12},A_6$ で表せ。

(2) 面心立方格子の第1近接と第2近接の原子について，それぞれの数と距離（$R$ を単位とする）を求めよ。さらに，第2近接までの和で近似した $A_{12}$ と $A_6$ の値を求めよ。

(3) 平衡での最近接距離 $R_0$ と凝集エネルギー $U_0=U(R_0)$ を求め，$R_0/\sigma$ と $U_0/(N\varepsilon)$ の数値を求めよ。

(4) 最近接原子の間の相互作用だけを考えた場合の $R_0/\sigma$ と $U_0/(N\varepsilon)$ を求めよ。

---

## 解答・解説

### (1)
1つの原子が他のすべての原子から受けるポテンシャルエネルギーを足し，原子数 $N$ をかけてから，同じ組を2回数えた分として $\dfrac{1}{2}$ をかけます。

$$
U=\frac{N}{2}\sum_j 4\varepsilon\left[\left(\frac{\sigma}{p_jR}\right)^{12}-\left(\frac{\sigma}{p_jR}\right)^{6}\right]
$$

$p_j$ の和を格子和でまとめると，

$$
\finalanswer{U(R)=2N\varepsilon\left[A_{12}\left(\frac{\sigma}{R}\right)^{12}-A_6\left(\frac{\sigma}{R}\right)^{6}\right]}
$$

となります。

### (2)
慣用単位胞の一辺を $a$ とすると，最近接は $\dfrac{a}{2}(\pm1,\pm1,0)$ 型の位置で，$R=\dfrac{a}{\sqrt{2}}$ です。第2近接は $a(\pm1,0,0)$ 型の位置で，距離は $a=\sqrt{2}R$ です。

$$
\finalanswer{\text{第1近接：12個，距離}\ R},\qquad \finalanswer{\text{第2近接：6個，距離}\ \sqrt{2}R}
$$

これらを格子和に入れると，

$$
\finalanswer{A_{12}\approx 12+\frac{6}{2^6}=12.094},\qquad \finalanswer{A_6\approx 12+\frac{6}{2^3}=12.75}
$$

となります。$A_{12}$ は正確な値にほぼ一致しますが，$A_6$ は遠くの原子からの寄与がまだ大きく残っています。

### (3)
$U$ を $R$ で微分して0とおくと，

$$
\frac{\mathrm{d}U}{\mathrm{d}R}=2N\varepsilon\left(-\frac{12A_{12}\sigma^{12}}{R^{13}}+\frac{6A_6\sigma^6}{R^7}\right)=0
$$

より $\left(\dfrac{R_0}{\sigma}\right)^6=\dfrac{2A_{12}}{A_6}$ です。これを $U$ に代入し，$\left(\dfrac{\sigma}{R_0}\right)^6=\dfrac{A_6}{2A_{12}}$ を使うと，$U_0=2N\varepsilon\left(\dfrac{A_6^2}{4A_{12}}-\dfrac{A_6^2}{2A_{12}}\right)$ となります。

$$
\finalanswer{R_0=\left(\frac{2A_{12}}{A_6}\right)^{1/6}\sigma\approx 1.09\,\sigma},\qquad
\finalanswer{U_0=-\frac{A_6^{\,2}}{2A_{12}}N\varepsilon\approx -8.61\,N\varepsilon}
$$

となります。数値は $2A_{12}/A_6=1.6786$，$A_6^{\,2}/(2A_{12})=208.92/24.262$ から求めました。

### (4)
最近接だけを考えることは，$A_{12}=A_6=12$ とおくことにあたります。(3) の式に代入すると，

$$
\finalanswer{R_0=2^{1/6}\sigma\approx 1.12\,\sigma},\qquad \finalanswer{U_0=-6N\varepsilon}
$$

となります。$U_0=-6N\varepsilon$ は，$6N$ 本の最近接の結合がそれぞれ2原子ポテンシャルの最小値 $-\varepsilon$ をもつことに対応します。遠くの原子からの引力を加えると，格子は約3％縮み，凝集エネルギーは約4割深くなります。

===== FILE: 06solid_state/02/02_040.md =====
---
tags:
  - 標準
---

# 共有結合と分子軌道

## 問題
水素分子イオン H$_2^+$ を考える。2つの陽子 A，B の位置は固定し，陽子間の反発は考えない。1個の電子のハミルトニアンを $\hat{H}$ とし，A，B を中心とする規格化された実数の 1s 軌道を $\phi_{\mathrm{A}},\phi_{\mathrm{B}}$ とする。次の積分を定義する。

$$
S=\int\phi_{\mathrm{A}}\phi_{\mathrm{B}}\,\mathrm{d}^3r,\qquad
\varepsilon_0=\int\phi_{\mathrm{A}}\hat{H}\phi_{\mathrm{A}}\,\mathrm{d}^3r=\int\phi_{\mathrm{B}}\hat{H}\phi_{\mathrm{B}}\,\mathrm{d}^3r,\qquad
\gamma=\int\phi_{\mathrm{A}}\hat{H}\phi_{\mathrm{B}}\,\mathrm{d}^3r=\int\phi_{\mathrm{B}}\hat{H}\phi_{\mathrm{A}}\,\mathrm{d}^3r
$$

ここで $0<S<1$，$\gamma<0$，$\varepsilon_0S-\gamma>0$ とする。試行関数 $\psi=c_{\mathrm{A}}\phi_{\mathrm{A}}+c_{\mathrm{B}}\phi_{\mathrm{B}}$（$c_{\mathrm{A}},c_{\mathrm{B}}$ は実数）を用い，エネルギーの期待値 $E=\dfrac{\int\psi\hat{H}\psi\,\mathrm{d}^3r}{\int\psi^2\,\mathrm{d}^3r}$ を最小にする変分法で考える。以下の問いに答えよ。

(1) $E$ を $c_{\mathrm{A}},c_{\mathrm{B}}$ で極値にする条件から，$c_{\mathrm{A}},c_{\mathrm{B}}$ が満たす連立方程式を導き，自明でない解をもつための $E$ の条件式（永年方程式）を求めよ。

(2) (1) の2つの解のエネルギー $E_{\mathrm{b}}<E_{\mathrm{a}}$ と，それぞれの規格化された波動関数 $\psi_{\mathrm{b}},\psi_{\mathrm{a}}$ を求めよ。

(3) $E_{\mathrm{a}}-\varepsilon_0$ と $\varepsilon_0-E_{\mathrm{b}}$ の比を $S$ で表せ。

(4) 陽子 A，B を結ぶ線分の中点を M とし，$\phi_{\mathrm{A}}(\mathrm{M})=\phi_{\mathrm{B}}(\mathrm{M})=\phi_{\mathrm{M}}$ とおく。M における確率密度 $|\psi_{\mathrm{b}}(\mathrm{M})|^2$ と $|\psi_{\mathrm{a}}(\mathrm{M})|^2$ を求めよ。また，$|\psi_{\mathrm{b}}(\mathrm{M})|^2$ と，2つの原子の確率密度の平均 $\dfrac{1}{2}\left[\phi_{\mathrm{A}}(\mathrm{M})^2+\phi_{\mathrm{B}}(\mathrm{M})^2\right]$ との比を求めよ。

---

## 解答・解説

### (1)
分子と分母を係数で書くと，$E\left(c_{\mathrm{A}}^2+2c_{\mathrm{A}}c_{\mathrm{B}}S+c_{\mathrm{B}}^2\right)=c_{\mathrm{A}}^2\varepsilon_0+2c_{\mathrm{A}}c_{\mathrm{B}}\gamma+c_{\mathrm{B}}^2\varepsilon_0$ です。両辺を $c_{\mathrm{A}}$ で微分し，極値の条件 $\partial E/\partial c_{\mathrm{A}}=0$ を使うと，

$$
E(2c_{\mathrm{A}}+2c_{\mathrm{B}}S)=2c_{\mathrm{A}}\varepsilon_0+2c_{\mathrm{B}}\gamma
$$

となります。$c_{\mathrm{B}}$ についても同様に計算すると，次の連立方程式が得られます。

$$
\begin{aligned}
(\varepsilon_0-E)c_{\mathrm{A}}+(\gamma-ES)c_{\mathrm{B}}&=0\\
(\gamma-ES)c_{\mathrm{A}}+(\varepsilon_0-E)c_{\mathrm{B}}&=0
\end{aligned}
$$

係数の行列式が0のときに自明でない解をもつので，

$$
\finalanswer{(\varepsilon_0-E)^2-(\gamma-ES)^2=0}
$$

となります。

### (2)
永年方程式から $\varepsilon_0-E=\pm(\gamma-ES)$ です。負号の場合は $E(1+S)=\varepsilon_0+\gamma$ で，連立方程式の1行目は $(\gamma-ES)(c_{\mathrm{B}}-c_{\mathrm{A}})=0$ となり，$c_{\mathrm{A}}=c_{\mathrm{B}}$ です。正号の場合は $E(1-S)=\varepsilon_0-\gamma$ で，$c_{\mathrm{A}}=-c_{\mathrm{B}}$ です。2つのエネルギーの差は $\dfrac{2(\varepsilon_0S-\gamma)}{1-S^2}>0$ なので，負号の解が低い方です。規格化条件は $c^2(2\pm2S)=1$ です。

$$
\finalanswer{E_{\mathrm{b}}=\frac{\varepsilon_0+\gamma}{1+S},\quad \psi_{\mathrm{b}}=\frac{\phi_{\mathrm{A}}+\phi_{\mathrm{B}}}{\sqrt{2(1+S)}}},\qquad
\finalanswer{E_{\mathrm{a}}=\frac{\varepsilon_0-\gamma}{1-S},\quad \psi_{\mathrm{a}}=\frac{\phi_{\mathrm{A}}-\phi_{\mathrm{B}}}{\sqrt{2(1-S)}}}
$$

となります。$\psi_{\mathrm{b}}$ が結合軌道，$\psi_{\mathrm{a}}$ が反結合軌道です。

### (3)
それぞれのずれを通分して計算します。

$$
E_{\mathrm{a}}-\varepsilon_0=\frac{\varepsilon_0S-\gamma}{1-S},\qquad
\varepsilon_0-E_{\mathrm{b}}=\frac{\varepsilon_0S-\gamma}{1+S}
$$

比をとると，

$$
\finalanswer{\frac{E_{\mathrm{a}}-\varepsilon_0}{\varepsilon_0-E_{\mathrm{b}}}=\frac{1+S}{1-S}}
$$

となります。準位の関係を図に示します。

<!-- FIGURE solution (3): エネルギー準位図。縦軸をエネルギーとする。左端と右端に短い横線で原子軌道 φA，φB の準位 ε0 を同じ高さに描く。中央に2本の横線を描き，上を E_a（反結合），下を E_b（結合）とラベル。E_a と ε0 の差が ε0 と E_b の差より大きいことが分かるように，E_a を ε0 から大きく上に，E_b を少し下に置く。左右の準位と中央の準位を細い破線で結ぶ。ε0 の高さに水平の点線を引き，上向きの矢印に E_a−ε0，下向きの矢印に ε0−E_b と付ける。 -->

$S>0$ なので，反結合軌道の持ち上がりは結合軌道の下がりより大きくなります。2つの軌道に電子が1個ずつ入ると，全体としては反発的になります。He$_2$ が安定な分子にならないのは，このためです。

### (4)
M では $\phi_{\mathrm{A}}=\phi_{\mathrm{B}}=\phi_{\mathrm{M}}$ なので，(2) の波動関数に代入します。

$$
\psi_{\mathrm{b}}(\mathrm{M})=\frac{2\phi_{\mathrm{M}}}{\sqrt{2(1+S)}},\qquad \psi_{\mathrm{a}}(\mathrm{M})=0
$$

これを2乗すると，

$$
\finalanswer{|\psi_{\mathrm{b}}(\mathrm{M})|^2=\frac{2\phi_{\mathrm{M}}^{\,2}}{1+S}},\qquad \finalanswer{|\psi_{\mathrm{a}}(\mathrm{M})|^2=0}
$$

となります。原子の確率密度の平均は M で $\phi_{\mathrm{M}}^{\,2}$ なので，

$$
\finalanswer{\frac{|\psi_{\mathrm{b}}(\mathrm{M})|^2}{\phi_{\mathrm{M}}^{\,2}}=\frac{2}{1+S}}
$$

となります。$0<S<1$ なのでこの比は1より大きく，結合軌道では電子が陽子の間に集まって両方の陽子を引きつけます。反結合軌道では，2つの陽子の垂直二等分面上で確率密度が0になります。

===== FILE: 06solid_state/02/02_050.md =====
---
tags:
  - 標準
---

# 金属結合の自由電子描像

## 問題
1価の金属を，価電子の自由電子気体と陽イオンからなる系とみなす。電子の数密度を $n$ とし，1電子あたりの体積に等しい球の半径 $r_s$ を $\dfrac{4\pi}{3}r_s^{\,3}=\dfrac{1}{n}$ で定義する。電子の質量を $m$，素電荷を $e$，真空の誘電率を $\varepsilon_0$，ボーア半径を $a_{\mathrm{B}}=\dfrac{4\pi\varepsilon_0\hbar^2}{me^2}$，リュードベリ定数を $\mathrm{Ry}=\dfrac{\hbar^2}{2ma_{\mathrm{B}}^{\,2}}$ とする。絶対零度を考え，電子のスピンの自由度は2とする。

静電エネルギーは次のように見積もる。結晶を，各イオンを中心とする半径 $r_s$ の球に分け，各球の中心に点電荷 $+e$ のイオンがあり，電子1個分の電荷 $-e$ が球内に一様に広がっているとする。球は電気的に中性なので，異なる球どうしの相互作用は無視する。以下の問いに答えよ。

(1) 1電子あたりの平均運動エネルギー $E_{\mathrm{K}}$ を $\hbar,m,r_s$ で表せ。

(2) 1つの球の静電エネルギー（一様な電荷分布の自己エネルギーと，イオンとの相互作用エネルギーの和）$E_{\mathrm{C}}$ を $e,\varepsilon_0,r_s$ で表せ。

(3) $x=r_s/a_{\mathrm{B}}$ とおき，1電子あたりのエネルギー $E_{\mathrm{tot}}=E_{\mathrm{K}}+E_{\mathrm{C}}$ を $\mathrm{Ry}$ 単位で $x$ の関数として表せ。$\mathrm{Ry}=\dfrac{e^2}{8\pi\varepsilon_0 a_{\mathrm{B}}}$ であることを用いてよい。

(4) $E_{\mathrm{tot}}$ を最小にする $x_0$ とそのときの $E_{\mathrm{tot}}$ を求め，数値で示せ。$a_{\mathrm{B}}=0.0529\ \mathrm{nm}$，$\mathrm{Ry}=13.6\ \mathrm{eV}$ とする。

---

## 解答・解説

### (1)
絶対零度では，電子は半径 $k_{\mathrm{F}}$ のフェルミ球の内部を占めます。スピンを含めた状態数を電子数と等しくおくと $2\cdot\dfrac{V}{(2\pi)^3}\cdot\dfrac{4\pi}{3}k_{\mathrm{F}}^{\,3}=nV$ なので，$k_{\mathrm{F}}=(3\pi^2n)^{1/3}$ です。$n=\dfrac{3}{4\pi r_s^{\,3}}$ を代入すると $k_{\mathrm{F}}=\left(\dfrac{9\pi}{4}\right)^{1/3}\dfrac{1}{r_s}$ となります。

平均運動エネルギーは，フェルミ球内で $\dfrac{\hbar^2k^2}{2m}$ を $k^2\,\mathrm{d}k$ の重みで平均して求めます。

$$
E_{\mathrm{K}}=\frac{\hbar^2}{2m}\frac{\int_0^{k_{\mathrm{F}}}k^4\,\mathrm{d}k}{\int_0^{k_{\mathrm{F}}}k^2\,\mathrm{d}k}=\frac{3}{5}\cdot\frac{\hbar^2k_{\mathrm{F}}^{\,2}}{2m}
$$

より，

$$
\finalanswer{E_{\mathrm{K}}=\frac{3\hbar^2}{10m}\left(\frac{9\pi}{4}\right)^{2/3}\frac{1}{r_s^{\,2}}}
$$

となります。

### (2)
一様な電荷の球の自己エネルギーは，半径0から少しずつ電荷を積み上げて求めます。半径 $r$ までに電荷 $q(r)=-e\,r^3/r_s^{\,3}$ があるとき，表面に $\mathrm{d}q=-3e\,r^2\mathrm{d}r/r_s^{\,3}$ を運ぶ仕事は $\dfrac{q\,\mathrm{d}q}{4\pi\varepsilon_0 r}$ です。

$$
W_{\mathrm{self}}=\int_0^{r_s}\frac{3e^2r^4}{4\pi\varepsilon_0 r_s^{\,6}}\,\mathrm{d}r=\frac{3}{5}\cdot\frac{e^2}{4\pi\varepsilon_0 r_s}
$$

一様な電荷 $-e$ が中心につくる電位は，殻ごとの寄与を足して $\displaystyle\int_0^{r_s}\frac{-3e\,r^2}{4\pi\varepsilon_0 r_s^{\,3}\,r}\,\mathrm{d}r=-\frac{3}{2}\cdot\frac{e}{4\pi\varepsilon_0 r_s}$ です。イオンとの相互作用エネルギーはこれに $+e$ をかけたものです。2つを足すと，

$$
\finalanswer{E_{\mathrm{C}}=\left(\frac{3}{5}-\frac{3}{2}\right)\frac{e^2}{4\pi\varepsilon_0 r_s}=-\frac{9}{10}\cdot\frac{e^2}{4\pi\varepsilon_0 r_s}}
$$

となります。

### (3)
$\dfrac{\hbar^2}{m}=2\,\mathrm{Ry}\,a_{\mathrm{B}}^{\,2}$ と $\dfrac{e^2}{4\pi\varepsilon_0}=2\,\mathrm{Ry}\,a_{\mathrm{B}}$ を (1)，(2) に代入します。

$$
\finalanswer{E_{\mathrm{tot}}=\left[\frac{3}{5}\left(\frac{9\pi}{4}\right)^{2/3}\frac{1}{x^2}-\frac{9}{5}\cdot\frac{1}{x}\right]\mathrm{Ry}\approx\left(\frac{2.21}{x^2}-\frac{1.80}{x}\right)\mathrm{Ry}}
$$

となります。ここで $\left(\dfrac{9\pi}{4}\right)^{2/3}=3.683$ を使いました。

### (4)
$E_{\mathrm{tot}}=\left(\dfrac{A}{x^2}-\dfrac{B}{x}\right)\mathrm{Ry}$ と書き，$x$ で微分して0とおくと $x_0=\dfrac{2A}{B}$ です。最小値は $-\dfrac{B^2}{4A}\,\mathrm{Ry}$ になります。$A=\dfrac{3}{5}\left(\dfrac{9\pi}{4}\right)^{2/3}$，$B=\dfrac{9}{5}$ を代入すると，

$$
\finalanswer{x_0=\frac{2}{3}\left(\frac{9\pi}{4}\right)^{2/3}\approx 2.46},\qquad
\finalanswer{E_{\mathrm{tot}}(x_0)=-\frac{27}{20}\left(\frac{4}{9\pi}\right)^{2/3}\mathrm{Ry}\approx -0.37\ \mathrm{Ry}\approx -5.0\ \mathrm{eV}}
$$

となります。$r_s=x_0a_{\mathrm{B}}\approx 0.13\ \mathrm{nm}$ です。エネルギーの $x$ 依存性を図に示します。

<!-- FIGURE solution (4): 横軸 x = r_s/a_B（0.5〜8），縦軸 エネルギー（Ry 単位，-0.6〜1.0）。3本の曲線を描く：運動エネルギー 2.21/x²（破線，正で単調減少），静電エネルギー -1.80/x（点線，負で 0 に近づく），和 E_tot（実線）。実線の極小点 (2.46, -0.37) に黒丸を置き，そこから両軸へ細い補助線を引いて値を示す。横軸 0 の水平線も細く描く。 -->

電子を詰めると運動エネルギーが上がり，広げるとイオンとの引力が弱まります。その釣り合いで密度が決まることが金属結合の本質です。実際のアルカリ金属では $r_s/a_{\mathrm{B}}\approx 3\sim 6$ で，見積もりより低密度です。これは，交換・相関の効果やイオン芯の反発を無視しているためです。

===== FILE: 06solid_state/03/03_010.md =====
---
tags:
  - 基本
---

# ブラッグ条件

## 問題
結晶内の原子が，間隔 $d$ で平行に並んだ格子面の上に周期的に配列しているとする。波長 $\lambda$ のX線が格子面に対して角 $\theta$（X線の進む向きと格子面のなす角，$0<\theta\le 90^\circ$）で入射し，各格子面で鏡面反射する（図）。以下の問いに答えよ。

<!-- FIGURE problem: 水平な平行線を2本（上の格子面，下の格子面）間隔 d で描き，それぞれの線上に等間隔に原子（黒丸）を5個ほど並べる。左上から平行なX線を2本描き，1本は上の面の原子で，もう1本は下の面の原子で鏡面反射して右上へ出ていく様子を矢印で示す。入射線と面のなす角を θ，反射線と面のなす角を θ とラベル。2本の面の間に寸法線を引いて d とラベル。経路差を示す補助線や垂線は描かない。 -->

(1) 隣り合う格子面で反射されたX線の経路差を求め，反射波が強め合う条件を整数 $n\,(\ge1)$ を用いて表せ。

(2) 単純立方格子の結晶に $\lambda=0.154\ \mathrm{nm}$ のX線を当てたところ，立方体の面に平行な $(100)$ 面からの1次（$n=1$）の反射が $\theta=15.0^\circ$ に観測された。格子定数 $a$ を求めよ。

(3) (2) の結晶の $(100)$ 面について，観測されうる反射の次数 $n$ をすべて求め，それぞれの $\theta$ を求めよ。

(4) 面間隔 $d$ の面族からの $n$ 次の反射の条件は，面間隔 $d/n$ の面族からの1次の反射の条件と同じであることを示せ。また，ある面族から反射が1つも起こらない $\lambda$ の範囲を求めよ。

---

## 解答・解説

### (1)
下の面で反射される波は，上の面で反射される波に比べて，入射側で $d\sin\theta$，反射側で $d\sin\theta$ だけ余分に進みます。これは，上の面の反射点から下の面へ下ろした垂線と入射線・反射線との幾何から分かります。

$$
\Delta=2d\sin\theta
$$

経路差が波長の整数倍のとき，すべての面からの反射波が同位相で重なって強め合うので，

$$
\finalanswer{2d\sin\theta=n\lambda\quad(n=1,2,\ldots)}
$$

となります。

### (2)
単純立方格子の $(100)$ 面は立方体の面に平行で，その面間隔は格子定数そのものです（$d=a$）。$n=1$ として (1) を $a$ について解きます。

$$
a=\frac{\lambda}{2\sin\theta}=\frac{0.154\ \mathrm{nm}}{2\times 0.2588}
$$

より，

$$
\finalanswer{a\approx 0.298\ \mathrm{nm}}
$$

となります。

### (3)
$\sin\theta\le1$ でなければならないので，$n\lambda\le 2d$，すなわち $n\le\dfrac{2a}{\lambda}=3.86$ です。したがって $n=1,2,3$ が観測されます。各次数の角度は $\sin\theta_n=n\sin\theta_1=0.2588\,n$ から求めます。

$$
\finalanswer{n=1:\ \theta=15.0^\circ},\qquad \finalanswer{n=2:\ \theta\approx 31.2^\circ},\qquad \finalanswer{n=3:\ \theta\approx 50.9^\circ}
$$

となります。それぞれ $\sin\theta=0.2588,\ 0.5176,\ 0.7765$ に対応します。次数が上がるほど，角度の間隔は広がります。

### (4)
(1) の条件の両辺を $n$ で割ります。

$$
\finalanswer{2d\sin\theta=n\lambda\iff 2\left(\frac{d}{n}\right)\sin\theta=\lambda}
$$

右の式は，面間隔 $d/n$ の面族からの1次の反射の条件そのものです。このため，$n$ 次の反射は指数 $(nh\,nk\,nl)$ の面族による1次の反射として扱えます。単純立方格子では，(2) の2次の反射を，間隔 $a/2$ の仮想的な $(200)$ 面による1次の反射とみなせます。

最低次の $n=1$ でも $\lambda\le 2d\sin\theta\le 2d$ が必要です。したがって，

$$
\finalanswer{\lambda>2d}
$$

のとき，反射は1つも起こりません。可視光（$\lambda\sim 500\ \mathrm{nm}$）では原子間隔の面族で回折が起こらず，結晶構造を調べるには原子間隔程度の波長をもつX線が必要です。

===== FILE: 06solid_state/03/03_020.md =====
---
tags:
  - 標準
---

# ラウエ条件とエバルト球

## 問題
基本並進ベクトル $\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3$ のブラベー格子の各格子点 $\boldsymbol{R}$ に同じ散乱体があり，波数ベクトル $\boldsymbol{k}$ のX線が弾性散乱されて波数ベクトル $\boldsymbol{k}'$ の向きに出ていく（$|\boldsymbol{k}'|=|\boldsymbol{k}|=k=2\pi/\lambda$）。散乱ベクトルを $\Delta\boldsymbol{k}=\boldsymbol{k}'-\boldsymbol{k}$ とすると，散乱波の振幅は $F=\sum_{\boldsymbol{R}}e^{-i\Delta\boldsymbol{k}\cdot\boldsymbol{R}}$ に比例する。逆格子の基本ベクトルを $\boldsymbol{b}_j$（$\boldsymbol{a}_i\cdot\boldsymbol{b}_j=2\pi\delta_{ij}$）とし，逆格子ベクトルを $\boldsymbol{G}=h\boldsymbol{b}_1+k\boldsymbol{b}_2+l\boldsymbol{b}_3$（$h,k,l$ は整数）とする。以下の問いに答えよ。

(1) $F$ のすべての項が同位相になる（$e^{-i\Delta\boldsymbol{k}\cdot\boldsymbol{R}}=1$ がすべての $\boldsymbol{R}$ で成り立つ）ための必要十分条件が，$\Delta\boldsymbol{k}$ が逆格子ベクトルであることを示せ。

(2) 弾性散乱で (1) の条件が成り立つとき，$\boldsymbol{k}$ と $\boldsymbol{G}=\Delta\boldsymbol{k}$ が満たす関係式を求めよ。

(3) $\boldsymbol{k}$ と $\boldsymbol{k}'$ のなす角を $2\theta$ とする。(1) の条件から，$\boldsymbol{G}$ に垂直な格子面の族（面間隔 $d$）についてのブラッグ条件 $2d\sin\theta=n\lambda$ を導け。$\boldsymbol{G}$ の方向で最短の逆格子ベクトルの長さが $2\pi/d$ であることを用いてよい。

(4) 結晶の向きを自由に変えられるとき，回折を起こしうる $\boldsymbol{G}$ の大きさの範囲を求めよ。また，格子定数 $a$ の単純立方格子に $\lambda=a$ のX線を当てたとき，回折を起こしうる $(hkl)$ を，符号と順序の入れ替えを同一視してすべて挙げよ。

---

## 解答・解説

### (1)
任意の格子点は $\boldsymbol{R}=\sum_i n_i\boldsymbol{a}_i$ と書けるので，条件はすべての $i$ で $\Delta\boldsymbol{k}\cdot\boldsymbol{a}_i$ が $2\pi$ の整数倍であることと同値です。$\boldsymbol{b}_j$ は1次独立なので，$\Delta\boldsymbol{k}=\sum_j x_j\boldsymbol{b}_j$ と展開できます。この展開で $\boldsymbol{a}_i$ との内積をとると，

$$
\Delta\boldsymbol{k}\cdot\boldsymbol{a}_i=2\pi x_i
$$

です。したがって条件は「すべての $x_i$ が整数」となり，

$$
\finalanswer{\Delta\boldsymbol{k}=\boldsymbol{G}}
$$

がラウエ条件です。この条件が成り立つと $|F|$ は散乱体の数に比例して大きくなり，成り立たないと位相がばらついて打ち消し合います。

### (2)
$\boldsymbol{k}'=\boldsymbol{k}+\boldsymbol{G}$ を弾性散乱の条件 $|\boldsymbol{k}'|^2=|\boldsymbol{k}|^2$ に代入して展開します。

$$
k^2+2\boldsymbol{k}\cdot\boldsymbol{G}+|\boldsymbol{G}|^2=k^2
$$

より，

$$
\finalanswer{2\boldsymbol{k}\cdot\boldsymbol{G}+|\boldsymbol{G}|^2=0}
$$

となります。これは，$\boldsymbol{k}$ の先端が，原点と逆格子点 $-\boldsymbol{G}$ を結ぶ線分の垂直二等分面上にあることを意味します。つまりブリルアンゾーンの境界上にある波が回折されます。

### (3)
$|\boldsymbol{k}|=|\boldsymbol{k}'|$ なので，$\boldsymbol{k},\boldsymbol{k}',\Delta\boldsymbol{k}$ は二等辺三角形をつくり，$|\Delta\boldsymbol{k}|=2k\sin\theta$ です。このとき $\Delta\boldsymbol{k}$ は頂角の二等分線に垂直なので，入射波と散乱波は $\boldsymbol{G}$ に垂直な面に対して同じ角 $\theta$ をなし，鏡面反射の配置になります。$\boldsymbol{G}$ はその方向で最短の逆格子ベクトルの整数倍 $n$ なので，$|\boldsymbol{G}|=2\pi n/d$ です。

$$
2\cdot\frac{2\pi}{\lambda}\sin\theta=\frac{2\pi n}{d}
$$

より，

$$
\finalanswer{2d\sin\theta=n\lambda}
$$

となります。逆にブラッグ条件が成り立てば，上の式をさかのぼって $\Delta\boldsymbol{k}=\boldsymbol{G}$ が得られるので，2つの条件は同値です。

### (4)
(3) から $|\boldsymbol{G}|=|\Delta\boldsymbol{k}|=2k\sin\theta\le 2k$ です。

$$
\finalanswer{0<|\boldsymbol{G}|\le\frac{4\pi}{\lambda}}
$$

この範囲の $\boldsymbol{G}$ は，結晶の向きを調節すれば回折条件を満たせます。

この条件は図のエバルト球で理解できます。$\boldsymbol{k}$ を終点が逆格子の原点 O になるように描き，始点 C を中心に半径 $k$ の球を描きます。球面上に乗った逆格子点 P に対して $\overrightarrow{\mathrm{CP}}$ が $\boldsymbol{k}'$ となり，回折が起こります。

<!-- FIGURE solution (4): 2次元の正方格子状に逆格子点（黒点）を並べる。1つの格子点を原点 O とする。左上の点 C から O へ向かう矢印を描き k とラベル。C を中心に，半径 |k| の円（エバルト球の断面）を描き，円周が O を通るようにする。円周上にちょうど乗る別の逆格子点 P を1つ選び，C から P への矢印を k'，O から P への矢印を G とラベル。円の半径に 2π/λ と注記。 -->

単純立方格子では $|\boldsymbol{G}|=\dfrac{2\pi}{a}\sqrt{h^2+k^2+l^2}$ なので，$\lambda=a$ の条件は $h^2+k^2+l^2\le 4$ です。これを満たす整数の組は次のとおりです。

$$
\finalanswer{(100),\ (110),\ (111),\ (200)}
$$

となります。$\lambda$ を短くするほど球が大きくなり，より多くの反射が観測できます。

===== FILE: 06solid_state/03/03_030.md =====
---
tags:
  - 標準
---

# 構造因子と消滅則

## 問題
一辺 $a$ の立方体を慣用単位胞とする結晶を考える。慣用単位胞の原点を格子点 $\boldsymbol{R}$（単純立方格子をなす）にとり，単位胞内の原子の位置を $\boldsymbol{r}_j=a(x_j\boldsymbol{e}_x+y_j\boldsymbol{e}_y+z_j\boldsymbol{e}_z)$ とする。原子はすべて同種で，原子形状因子を $f$ とする。散乱ベクトル $\Delta\boldsymbol{k}$ の散乱波の振幅は，すべての原子についての和 $\sum_{\boldsymbol{R}}\sum_j f\,e^{-i\Delta\boldsymbol{k}\cdot(\boldsymbol{R}+\boldsymbol{r}_j)}$ に比例するとする。以下の問いに答えよ。

(1) 振幅が $\boldsymbol{R}$ についての和と単位胞内の和の積に分かれることを示せ。そのうえで，回折が起こる $\Delta\boldsymbol{k}=\dfrac{2\pi}{a}(h\boldsymbol{e}_x+k\boldsymbol{e}_y+l\boldsymbol{e}_z)$（$h,k,l$ は整数）に対し，単位胞内の和（構造因子）$S_{hkl}$ を $h,k,l$ と $x_j,y_j,z_j$ で表せ。

(2) 体心立方格子（単位胞内の原子 $(0,0,0)$，$\left(\frac{1}{2},\frac{1}{2},\frac{1}{2}\right)$）について $S_{hkl}$ を求め，反射が消える条件を求めよ。また，現れる反射を $h^2+k^2+l^2$ の小さい順に4つ挙げよ。

(3) 面心立方格子（単位胞内の原子 $(0,0,0)$，$\left(0,\frac{1}{2},\frac{1}{2}\right)$，$\left(\frac{1}{2},0,\frac{1}{2}\right)$，$\left(\frac{1}{2},\frac{1}{2},0\right)$）について $S_{hkl}$ を求め，反射が消える条件を求めよ。また，現れる反射を $h^2+k^2+l^2$ の小さい順に4つ挙げよ。

(4) ダイヤモンド構造（(3) の4つの位置と，それぞれを $\left(\frac{1}{4},\frac{1}{4},\frac{1}{4}\right)$ だけずらした4つの位置）について，$|S_{hkl}|$ を求めよ。そのうえで，$(200)$ 反射と $(222)$ 反射が現れるかどうかを答えよ。

---

## 解答・解説

### (1)
指数関数の積の性質 $e^{-i\Delta\boldsymbol{k}\cdot(\boldsymbol{R}+\boldsymbol{r}_j)}=e^{-i\Delta\boldsymbol{k}\cdot\boldsymbol{R}}e^{-i\Delta\boldsymbol{k}\cdot\boldsymbol{r}_j}$ を使うと，和は次のように分かれます。

$$
\sum_{\boldsymbol{R}}\sum_j f\,e^{-i\Delta\boldsymbol{k}\cdot(\boldsymbol{R}+\boldsymbol{r}_j)}=\left(\sum_{\boldsymbol{R}}e^{-i\Delta\boldsymbol{k}\cdot\boldsymbol{R}}\right)\left(\sum_j f\,e^{-i\Delta\boldsymbol{k}\cdot\boldsymbol{r}_j}\right)
$$

第1因子は，$\Delta\boldsymbol{k}$ が一辺 $a$ の単純立方格子の逆格子ベクトル $\dfrac{2\pi}{a}(h,k,l)$ のときだけ大きくなります（ラウエ条件）。このとき $\Delta\boldsymbol{k}\cdot\boldsymbol{r}_j=2\pi(hx_j+ky_j+lz_j)$ なので，

$$
\finalanswer{S_{hkl}=f\sum_j\exp\!\left[-2\pi i(hx_j+ky_j+lz_j)\right]}
$$

となります。

### (2)
2つの原子の位置を代入し，$e^{-i\pi m}=(-1)^m$ を使います。

$$
S_{hkl}=f\left[1+e^{-i\pi(h+k+l)}\right]=f\left[1+(-1)^{h+k+l}\right]
$$

より，

$$
\finalanswer{S_{hkl}=2f\ (h+k+l\ \text{が偶数}),\qquad S_{hkl}=0\ (h+k+l\ \text{が奇数})}
$$

となり，$h+k+l$ が奇数の反射が消えます。現れる反射を小さい順に並べると，

$$
\finalanswer{(110),\ (200),\ (211),\ (220)}
$$

となります。

### (3)
4つの位置を代入します。

$$
S_{hkl}=f\left[1+(-1)^{k+l}+(-1)^{h+l}+(-1)^{h+k}\right]
$$

$h,k,l$ がすべて偶数またはすべて奇数なら，3つの和はすべて偶数で $S=4f$ です。偶奇が混ざると，たとえば $h,k$ が偶数で $l$ が奇数なら $1-1-1+1=0$ となり，2つが奇数の場合も同様に0です。

$$
\finalanswer{S_{hkl}=4f\ (h,k,l\ \text{がすべて同じ偶奇}),\qquad S_{hkl}=0\ (\text{偶奇が混在})}
$$

となります。現れる反射を小さい順に並べると，

$$
\finalanswer{(111),\ (200),\ (220),\ (311)}
$$

となります。

### (4)
ずらした4つの位置からの寄与は，(3) の和に共通の位相因子 $e^{-i\pi(h+k+l)/2}$ をかけたものです。

$$
S_{hkl}=S_{hkl}^{\mathrm{fcc}}\left[1+e^{-i\pi(h+k+l)/2}\right]
$$

偶奇が混在すれば $S^{\mathrm{fcc}}=0$ です。すべて奇数なら $h+k+l$ は奇数で，括弧内は $1\mp i$，絶対値は $\sqrt{2}$ です。すべて偶数なら $h+k+l$ は偶数で，$4$ の倍数のとき括弧内は2，$4$ の倍数でないときは0です。

$$
\begin{aligned}
&\finalanswer{|S_{hkl}|=4\sqrt{2}f}\quad(\text{すべて奇数})\\
&\finalanswer{|S_{hkl}|=8f}\quad(\text{すべて偶数で}\ h+k+l=4m)\\
&\finalanswer{|S_{hkl}|=0}\quad(\text{すべて偶数で}\ h+k+l=4m+2,\ \text{または偶奇が混在})
\end{aligned}
$$

$(200)$ は $h+k+l=2$，$(222)$ は $h+k+l=6$ で，どちらも $4m+2$ の形です。

$$
\finalanswer{(200)\ \text{と}\ (222)\ \text{はどちらも現れない}}
$$

となります。面心立方格子では許される反射も，基本構造の2つの原子からの波が打ち消し合って消えます。この追加の消滅則から，ダイヤモンド構造と面心立方構造を見分けられます。

===== FILE: 06solid_state/03/03_040.md =====
---
tags:
  - 発展
---

# 原子形状因子

## 問題
原子の電子の数密度 $n(\boldsymbol{r})$ が原子核を中心に球対称で，$n(\boldsymbol{r})=n(r)$（$r=|\boldsymbol{r}|$）と書けるとする。散乱ベクトル $\boldsymbol{G}$ に対する原子形状因子を

$$
f(\boldsymbol{G})=\int n(\boldsymbol{r})\,e^{-i\boldsymbol{G}\cdot\boldsymbol{r}}\,\mathrm{d}^3r
$$

で定義し，$G=|\boldsymbol{G}|$，電子の総数を $Z=\displaystyle\int n(\boldsymbol{r})\,\mathrm{d}^3r$ とする。以下の問いに答えよ。

(1) $f$ が $G$ だけの関数であることを示し，$f(G)$ を $n(r)$ の $r$ についての1重積分で表せ。

(2) $f(0)$ を求め，$G$ が小さいときの $f(G)$ を $G^2$ の項まで求めよ。電子の広がりは $\langle r^2\rangle=\dfrac{1}{Z}\displaystyle\int r^2 n(\boldsymbol{r})\,\mathrm{d}^3r$ を用いて表せ。

(3) 水素原子の 1s 状態の電子の数密度 $n(r)=\dfrac{1}{\pi a_{\mathrm{B}}^{\,3}}e^{-2r/a_{\mathrm{B}}}$（$a_{\mathrm{B}}$ はボーア半径）に対して $f(G)$ を求めよ。

(4) 波長 $\lambda$ のX線が格子面に対して角 $\theta$ で入射して弾性散乱されるとき（散乱角 $2\theta$），$G$ を $\theta$ と $\lambda$ で表せ。さらに，(3) の $f$ が $f(0)$ の半分になる $\dfrac{\sin\theta}{\lambda}$ の値を求めよ。$a_{\mathrm{B}}=0.0529\ \mathrm{nm}$ とする。

---

## 解答・解説

### (1)
球座標の極軸を $\boldsymbol{G}$ の向きにとると，$\boldsymbol{G}\cdot\boldsymbol{r}=Gr\cos\vartheta$ となり，角度の積分は $n(r)$ と分けて実行できます。$\mu=\cos\vartheta$ とおくと，

$$
\int_0^{2\pi}\!\mathrm{d}\varphi\int_{-1}^{1}e^{-iGr\mu}\,\mathrm{d}\mu=2\pi\cdot\frac{2\sin Gr}{Gr}
$$

です。これは $\boldsymbol{G}$ の向きによらないので，$f$ は $G$ だけの関数で，

$$
\finalanswer{f(G)=4\pi\int_0^{\infty}n(r)\,r^2\,\frac{\sin Gr}{Gr}\,\mathrm{d}r}
$$

となります。

### (2)
$G\to0$ では $\dfrac{\sin Gr}{Gr}\to1$ なので，$f(0)$ は電子の総数 $Z$ です。$G$ が小さいときは $\dfrac{\sin x}{x}=1-\dfrac{x^2}{6}+\cdots$ と展開して，$G^2$ の項まで残します。

$$
f(G)\approx 4\pi\int_0^\infty n(r)\,r^2\left(1-\frac{G^2r^2}{6}\right)\mathrm{d}r=Z-\frac{G^2}{6}\int r^2n(\boldsymbol{r})\,\mathrm{d}^3r
$$

より，

$$
\finalanswer{f(0)=Z},\qquad \finalanswer{f(G)\approx Z\left(1-\frac{G^2\langle r^2\rangle}{6}\right)}
$$

となります。電子雲が広いほど，$G$ が増えたときに形状因子は速く減少します。

### (3)
(1) の式に代入すると，

$$
f(G)=\frac{4}{a_{\mathrm{B}}^{\,3}G}\int_0^\infty r\,e^{-2r/a_{\mathrm{B}}}\sin Gr\,\mathrm{d}r
$$

となります。積分は $\sin Gr=\operatorname{Im}e^{iGr}$ と書き，$\kappa=2/a_{\mathrm{B}}$ として計算します。

$$
\int_0^\infty r\,e^{-\kappa r}\sin Gr\,\mathrm{d}r=\operatorname{Im}\frac{1}{(\kappa-iG)^2}=\frac{2\kappa G}{(\kappa^2+G^2)^2}
$$

$\kappa=2/a_{\mathrm{B}}$ を代入すると，積分の値は $\dfrac{4Ga_{\mathrm{B}}^{\,3}}{(4+G^2a_{\mathrm{B}}^{\,2})^2}$ です。

$$
\finalanswer{f(G)=\frac{16}{(4+G^2a_{\mathrm{B}}^{\,2})^2}=\frac{1}{\left(1+\frac{G^2a_{\mathrm{B}}^{\,2}}{4}\right)^2}}
$$

となります。$G$ が小さいときは $f\approx1-\dfrac{G^2a_{\mathrm{B}}^{\,2}}{2}$ です。1s 状態の $\langle r^2\rangle=3a_{\mathrm{B}}^{\,2}$ を (2) に入れた結果と一致します。

### (4)
弾性散乱では $|\boldsymbol{k}|=|\boldsymbol{k}'|=2\pi/\lambda$ で，両者のなす角が $2\theta$ なので，$G=|\boldsymbol{k}'-\boldsymbol{k}|=2k\sin\theta$ です。

$$
\finalanswer{G=\frac{4\pi\sin\theta}{\lambda}}
$$

$f=\dfrac{1}{2}$ の条件は $\left(1+\dfrac{G^2a_{\mathrm{B}}^{\,2}}{4}\right)^2=2$ です。これを解くと $Ga_{\mathrm{B}}=2\sqrt{\sqrt{2}-1}\approx1.287$ となります。

$$
\finalanswer{\frac{\sin\theta}{\lambda}=\frac{\sqrt{\sqrt{2}-1}}{2\pi a_{\mathrm{B}}}\approx 1.94\ \mathrm{nm^{-1}}}
$$

となります。形状因子の $G$ 依存性を図に示します。

<!-- FIGURE solution (4): 横軸 G a_B（0〜6），縦軸 f（0〜1）。曲線 f = 1/(1+(G a_B)²/4)² を実線で描く。G a_B = 0 で f = 1。f = 0.5 の水平な破線と，G a_B ≈ 1.29 の鉛直な破線を引き，交点に黒丸を置く。比較のため，小さい G の近似 1 − (G a_B)²/2 を点線で G a_B ≈ 1.4 まで描く。 -->

散乱角が大きい反射ほど，原子1個あたりの散乱が弱くなります。高次の反射の強度が下がる理由の1つは，この形状因子の減少です。

===== FILE: 06solid_state/03/03_050.md =====
---
tags:
  - 標準
---

# 粉末回折パターンの指数付け

## 問題
立方晶に属する単体金属の粉末試料に波長 $\lambda=0.1542\ \mathrm{nm}$ のX線を当て，回折角 $2\theta$ の小さい方から4つの回折ピークを次の位置に観測した。

$$
2\theta=43.36^\circ,\quad 50.50^\circ,\quad 74.20^\circ,\quad 90.04^\circ
$$

格子は単純立方，体心立方，面心立方のいずれかであり，慣用単位胞の一辺を $a$ とする。ミラー指数 $(hkl)$ は慣用単位胞についてとる。体心立方格子では $h+k+l$ が偶数の反射だけが現れ，面心立方格子では $h,k,l$ がすべて偶数またはすべて奇数の反射だけが現れ，単純立方格子ではすべての反射が現れることを用いてよい。以下の問いに答えよ。

(1) 立方晶の $(hkl)$ 反射について，$\sin^2\theta$ を $\lambda,a$ と $N=h^2+k^2+l^2$ で表せ。

(2) 単純立方，体心立方，面心立方のそれぞれについて，現れる反射の $N$ を小さい順に4つ求め，最初の値に対する比 $N/N_1$ を求めよ。

(3) 測定した4つのピークの $\sin^2\theta$ と，最初のピークに対する比を求め，格子の種類と各ピークの $(hkl)$ を決定せよ。

(4) 格子定数 $a$ を求めよ。

---

## 解答・解説

### (1)
立方晶の面間隔 $d=\dfrac{a}{\sqrt{N}}$ をブラッグ条件 $2d\sin\theta=\lambda$ に代入します（高次の反射は指数 $(nh\,nk\,nl)$ の1次の反射として扱います）。両辺を2乗すると，

$$
\finalanswer{\sin^2\theta=\frac{\lambda^2}{4a^2}N}
$$

となります。$\sin^2\theta$ の比が $N$ の比になるので，格子定数を知らなくても指数を決められます。

### (2)
$N$ は3つの整数の2乗の和です。$7$ は3つの2乗の和で書けないことに注意して，各格子の条件を満たすものを小さい順に選びます。

単純立方：$(100),(110),(111),(200)$ で $N=1,2,3,4$。体心立方：$(110),(200),(211),(220)$ で $N=2,4,6,8$。面心立方：$(111),(200),(220),(311)$ で $N=3,4,8,11$ です。

$$
\finalanswer{\text{単純立方・体心立方}:\ 1:2:3:4},\qquad \finalanswer{\text{面心立方}:\ 1:1.333:2.667:3.667}
$$

となります。単純立方と体心立方は最初の4本では区別できません。単純立方には $N=7$ がないので，7本目の比が単純立方では $8$，体心立方では $7$ となり，ここで区別できます。

### (3)
各ピークの $\theta$ は $21.68^\circ,\ 25.25^\circ,\ 37.10^\circ,\ 45.02^\circ$ です。それぞれの $\sin^2\theta$ を計算し，最初の値で割ります。

$$
\begin{aligned}
\sin^2\theta &= 0.1365,\ 0.1820,\ 0.3639,\ 0.5004\\
\text{比} &= 1:1.333:2.666:3.666
\end{aligned}
$$

比は (2) の面心立方と一致します。

$$
\finalanswer{\text{面心立方格子}},\qquad \finalanswer{(111),\ (200),\ (220),\ (311)}
$$

となります。

### (4)
(1) を $a$ について解いた $a=\dfrac{\lambda\sqrt{N}}{2\sin\theta}$ に，各ピークの値を代入します。

$$
\begin{aligned}
(111)&: \frac{0.1542\times\sqrt{3}}{2\times0.3694}=0.3615\ \mathrm{nm}\\
(200)&: \frac{0.1542\times 2}{2\times0.4266}=0.3615\ \mathrm{nm}\\
(220)&: \frac{0.1542\times\sqrt{8}}{2\times0.6032}=0.3615\ \mathrm{nm}\\
(311)&: \frac{0.1542\times\sqrt{11}}{2\times0.7074}=0.3615\ \mathrm{nm}
\end{aligned}
$$

4つの値はよく一致するので，

$$
\finalanswer{a\approx 0.3615\ \mathrm{nm}}
$$

となります。この値は銅の格子定数に一致します。実際の測定では，角度の誤差の影響が小さい高角のピークを重視して $a$ を決めることが多くあります。

===== FILE: 06solid_state/03/03_060.md =====
---
tags:
  - 発展
---

# 回折強度と温度：デバイ・ワラー因子

## 問題
同種の原子からなるブラベー格子の結晶を考える。格子点 $\boldsymbol{R}$ の原子は熱振動によって $\boldsymbol{R}+\boldsymbol{u}_{\boldsymbol{R}}$ の位置にあり，$\langle\cdots\rangle$ は熱平均を表す。逆格子ベクトル $\boldsymbol{G}$ のブラッグ反射の強度は

$$
I(\boldsymbol{G})\propto\left|\sum_{\boldsymbol{R}}\left\langle e^{-i\boldsymbol{G}\cdot(\boldsymbol{R}+\boldsymbol{u}_{\boldsymbol{R}})}\right\rangle\right|^2
$$

で与えられるとする。どの原子の変位も同じ統計的性質をもち，向きについて等方的で，$\langle\boldsymbol{u}\rangle=\boldsymbol{0}$ とする。原子が静止しているときの強度を $I_0$，原子の質量を $M$，ボルツマン定数を $k_{\mathrm{B}}$，温度を $T$ とする。以下の問いに答えよ。

(1) $I/I_0=\left|\left\langle e^{-i\boldsymbol{G}\cdot\boldsymbol{u}}\right\rangle\right|^2$ であることを示し，$\boldsymbol{u}$ の2次までの近似で $I/I_0$ を $G=|\boldsymbol{G}|$ と $\langle u^2\rangle=\langle|\boldsymbol{u}|^2\rangle$ で表せ。

(2) 変位の $\boldsymbol{G}$ 方向の成分 $x=\boldsymbol{G}\cdot\boldsymbol{u}/G$ が，平均0，分散 $\langle x^2\rangle$ の正規分布に従うとする。$\left\langle e^{-iGx}\right\rangle$ を計算し，$I/I_0$ を $G$ と $\langle u^2\rangle$ で表せ。

(3) 各原子が角振動数 $\omega$ の等方的な3次元の調和振動子として独立に振動する（アインシュタイン模型）とし，古典統計力学で扱う。$\langle u^2\rangle$ を求め，$I/I_0$ を $T$ の関数として表せ。

(4) (3) の振動子を量子力学で扱う。1つの成分の調和振動子の平均エネルギー $\hbar\omega\left(\langle n\rangle+\dfrac{1}{2}\right)$（$\langle n\rangle=\dfrac{1}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}$）と，平均運動エネルギーと平均ポテンシャルエネルギーが等しいことを用いて，$\langle u^2\rangle$ を求めよ。また，$T\to0$ での $I/I_0$ を求めよ。

---

## 解答・解説

### (1)
各原子の変位は同じ統計に従うので，熱平均 $\left\langle e^{-i\boldsymbol{G}\cdot\boldsymbol{u}_{\boldsymbol{R}}}\right\rangle$ は $\boldsymbol{R}$ によらず，和の外に出せます。

$$
\sum_{\boldsymbol{R}}\left\langle e^{-i\boldsymbol{G}\cdot(\boldsymbol{R}+\boldsymbol{u}_{\boldsymbol{R}})}\right\rangle=\left\langle e^{-i\boldsymbol{G}\cdot\boldsymbol{u}}\right\rangle\sum_{\boldsymbol{R}}e^{-i\boldsymbol{G}\cdot\boldsymbol{R}}
$$

残りの和は静止した格子の振幅なので，強度の比は $I/I_0=\left|\left\langle e^{-i\boldsymbol{G}\cdot\boldsymbol{u}}\right\rangle\right|^2$ です。

次に，指数関数を2次まで展開します。$\langle\boldsymbol{u}\rangle=\boldsymbol{0}$ なので1次の項は消えます。等方性から $\langle u_\alpha u_\beta\rangle=\dfrac{\langle u^2\rangle}{3}\delta_{\alpha\beta}$ となるので，$\langle(\boldsymbol{G}\cdot\boldsymbol{u})^2\rangle=\dfrac{G^2\langle u^2\rangle}{3}$ です。

$$
\left\langle e^{-i\boldsymbol{G}\cdot\boldsymbol{u}}\right\rangle\approx1-\frac{G^2\langle u^2\rangle}{6}
$$

これを2乗し，2次まで残すと，

$$
\finalanswer{\frac{I}{I_0}\approx1-\frac{G^2\langle u^2\rangle}{3}}
$$

となります。

### (2)
正規分布で平均をとります。指数の肩を平方完成すると，ガウス積分に帰着します。

$$
\begin{aligned}
\left\langle e^{-iGx}\right\rangle
&=\frac{1}{\sqrt{2\pi\langle x^2\rangle}}\int_{-\infty}^{\infty}\exp\!\left(-\frac{x^2}{2\langle x^2\rangle}-iGx\right)\mathrm{d}x\\
&=\exp\!\left(-\frac{G^2\langle x^2\rangle}{2}\right)\frac{1}{\sqrt{2\pi\langle x^2\rangle}}\int_{-\infty}^{\infty}\exp\!\left(-\frac{(x+iG\langle x^2\rangle)^2}{2\langle x^2\rangle}\right)\mathrm{d}x
=e^{-G^2\langle x^2\rangle/2}
\end{aligned}
$$

等方性から $\langle x^2\rangle=\langle u^2\rangle/3$ です。これを2乗すると，

$$
\finalanswer{\frac{I}{I_0}=\exp\!\left(-\frac{G^2\langle u^2\rangle}{3}\right)}
$$

となります。この指数因子をデバイ・ワラー因子とよびます。展開すれば (1) の結果に一致します。調和振動子の熱平衡状態では，変位は実際に正規分布に従います。

### (3)
等方的な調和振動子のポテンシャルは $\dfrac{1}{2}M\omega^2u^2$ です。古典統計の等分配則により，3つの自由度のポテンシャルエネルギーの平均は $\dfrac{3}{2}k_{\mathrm{B}}T$ です。

$$
\frac{1}{2}M\omega^2\langle u^2\rangle=\frac{3}{2}k_{\mathrm{B}}T
$$

これを (2) に代入すると，

$$
\finalanswer{\langle u^2\rangle=\frac{3k_{\mathrm{B}}T}{M\omega^2}},\qquad \finalanswer{\frac{I}{I_0}=\exp\!\left(-\frac{G^2k_{\mathrm{B}}T}{M\omega^2}\right)}
$$

となります。高温では $\ln I$ が $T$ に比例して減少し，$G$ の大きい高次の反射ほど強く弱まります。

### (4)
1つの成分について，全エネルギーの平均は平均ポテンシャルエネルギーの2倍，すなわち $M\omega^2\langle x^2\rangle$ です。これを量子力学の平均エネルギーと等しくおきます。

$$
M\omega^2\langle x^2\rangle=\hbar\omega\left(\langle n\rangle+\frac{1}{2}\right)=\frac{\hbar\omega}{2}\coth\frac{\hbar\omega}{2k_{\mathrm{B}}T}
$$

$\langle u^2\rangle=3\langle x^2\rangle$ なので，

$$
\finalanswer{\langle u^2\rangle=\frac{3\hbar}{2M\omega}\coth\frac{\hbar\omega}{2k_{\mathrm{B}}T}}
$$

となります。$T\to0$ では $\coth\to1$ となるので，

$$
\finalanswer{\frac{I}{I_0}\to\exp\!\left(-\frac{\hbar G^2}{2M\omega}\right)}
$$

となります。高温では $\coth y\approx1/y$ となり，(3) の古典的な結果に戻ります。絶対零度でも零点振動のために強度は $I_0$ まで回復しません。軽い原子ほど，この効果は大きくなります。

===== FILE: 06solid_state/04/04_010.md =====
---
tags:
  - 基本
---

# 一次元単原子鎖の分散関係

## 問題
質量 $M$ の原子が間隔 $a$ で一直線上に並び，隣り合う原子どうしがばね定数 $C$ のばねでつながれた一次元の鎖を考える（図）。$n$ 番目の原子の，平衡位置 $na$ からの鎖方向の変位を $u_n$ とする。原子は全部で $N$ 個あり，周期境界条件 $u_{n+N}=u_n$ を課す。以下の問いに答えよ。

<!-- FIGURE problem: 水平な直線上に質量 M の原子（同じ大きさの丸）を5個並べ，隣どうしをばね（ジグザグ線）でつなぐ。中央の原子に n，左右に n−1，n+1 のラベル。平衡位置を細い縦の破線で示し，隣の平衡位置との間に寸法線を引いて a とラベル。中央の原子を平衡位置から少し右にずらし，そのずれを矢印で u_n と示す。ばねの1つに C とラベル。 -->

(1) $n$ 番目の原子の運動方程式を書け。

(2) $u_n=A\,e^{i(kna-\omega t)}$（$A$ は定数，$\omega\ge0$）の形の解を仮定し，$\omega$ と $k$ の関係（分散関係）を求めよ。

(3) 周期境界条件から許される $k$ の値を求めよ。さらに，$k$ と $k+2\pi/a$ が同じ原子の運動を表すことを示し，独立な $k$ の数を求めよ。

(4) 長波長（$|k|a\ll1$）での $\omega$ を求め，音速 $v_{\mathrm{s}}$ を求めよ。また，$\omega$ の最大値 $\omega_{\mathrm{m}}$ を求めよ。

---

## 解答・解説

### (1)
$n$ 番目の原子は，右のばねから $C(u_{n+1}-u_n)$，左のばねから $-C(u_n-u_{n-1})$ の力を受けます。ばねの伸びが隣どうしの変位の差で決まるからです。

$$
\finalanswer{M\ddot{u}_n=C(u_{n+1}+u_{n-1}-2u_n)}
$$

となります。

### (2)
仮定した解を代入します。$u_{n\pm1}=u_ne^{\pm ika}$，$\ddot{u}_n=-\omega^2u_n$ なので，両辺を $u_n$ で割ると，

$$
-M\omega^2=C\left(e^{ika}+e^{-ika}-2\right)=-2C(1-\cos ka)=-4C\sin^2\frac{ka}{2}
$$

となります。$\omega\ge0$ として平方根をとると，

$$
\finalanswer{\omega=2\sqrt{\frac{C}{M}}\left|\sin\frac{ka}{2}\right|}
$$

となります。分散関係を図に示します。

<!-- FIGURE solution (2): 横軸 k（−2π/a から 2π/a），縦軸 ω。曲線 ω = 2√(C/M)|sin(ka/2)| を実線で描く。k = ±π/a に鉛直の破線を引き，その間を「第1ブリルアンゾーン」と注記。縦軸に最大値 2√(C/M) の目盛りを付ける。原点付近に，傾き a√(C/M) の接線を点線で短く描く。 -->

### (3)
周期境界条件 $u_{n+N}=u_n$ から $e^{ikNa}=1$ が必要です。

$$
\finalanswer{k=\frac{2\pi m}{Na}\quad(m\ \text{は整数})}
$$

$k$ を $k+2\pi/a$ に置き換えると，$e^{i(k+2\pi/a)na}=e^{ikna}e^{2\pi in}=e^{ikna}$ となり，すべての原子の変位は変わりません。原子は格子点の上にしかないので，波長の違う波でも原子の位置で同じ値をとれば区別できないのです。したがって $-\pi/a<k\le\pi/a$ に限ってよく，この範囲には $m$ が $N$ 個入ります。

$$
\finalanswer{\text{独立な}\ k\ \text{の数}=N}
$$

となり，原子の自由度の数と一致します。

### (4)
$|k|a\ll1$ では $\sin\dfrac{ka}{2}\approx\dfrac{ka}{2}$ と近似できます。

$$
\omega\approx a\sqrt{\frac{C}{M}}\,|k|
$$

$\omega$ が $|k|$ に比例するので，波は分散なく一定の速さで伝わります。

$$
\finalanswer{v_{\mathrm{s}}=a\sqrt{\frac{C}{M}}},\qquad \finalanswer{\omega_{\mathrm{m}}=2\sqrt{\frac{C}{M}}}
$$

となり，最大値はゾーン境界 $k=\pm\pi/a$ でとります。長波長では鎖は連続な弾性体として振る舞い，音波が伝わります。波長が原子間隔に近づくと離散性が効いて，$\omega$ は直線からずれます。

===== FILE: 06solid_state/04/04_020.md =====
---
tags:
  - 標準
---

# 一次元二原子鎖：音響モードと光学モード

## 問題
質量 $M_1$ と $M_2$（$M_1>M_2$）の2種類の原子が交互に一直線上に並び，隣り合う原子どうしがすべて同じばね定数 $C$ のばねでつながれている（図）。隣り合う原子の間隔は $a/2$ で，周期は $a$ である。$s$ 番目の単位胞の質量 $M_1$ の原子の変位を $u_s$，質量 $M_2$ の原子の変位を $v_s$ とし，$v_s$ の原子は $u_s$ の原子と $u_{s+1}$ の原子の間にある。以下の問いに答えよ。

<!-- FIGURE problem: 水平な直線上に大きい丸（M1）と小さい丸（M2）を交互に4組ほど並べ，隣どうしをばね（ジグザグ線）でつなぐ。中央付近の大きい丸に u_s，その右の小さい丸に v_s，その右の大きい丸に u_{s+1}，中央の大きい丸の左の小さい丸に v_{s−1} とラベル。隣り合う原子の間に寸法線で a/2，同じ種類の原子どうしの間に寸法線で a を示す。ばねの1つに C とラベル。 -->

(1) $u_s$ と $v_s$ の運動方程式を書け。

(2) $u_s=u\,e^{i(ksa-\omega t)}$，$v_s=v\,e^{i(ksa-\omega t)}$（$u,v$ は定数）の形の解を仮定し，分散関係 $\omega^2(k)$ を求めよ。

(3) $k\to0$ での2つの枝の $\omega$ を求めよ。また，それぞれの枝での振幅比 $v/u$ を求めよ。

(4) ゾーン境界 $k=\pi/a$ での2つの枝の $\omega$ を求め，各モードで動く原子を答えよ。また，$M_1=M_2$ のときにギャップが閉じることを確かめよ。

---

## 解答・解説

### (1)
各原子は左右の2本のばねから力を受け，力は両隣の原子との変位の差に比例します。$u_s$ の原子の両隣は $v_{s-1}$ と $v_s$，$v_s$ の原子の両隣は $u_s$ と $u_{s+1}$ です。

$$
\finalanswer{M_1\ddot{u}_s=C(v_s+v_{s-1}-2u_s)},\qquad \finalanswer{M_2\ddot{v}_s=C(u_{s+1}+u_s-2v_s)}
$$

となります。

### (2)
仮定した解を代入し，共通の因子 $e^{i(ksa-\omega t)}$ で割ると，$u,v$ の連立方程式になります。

$$
\begin{aligned}
(2C-M_1\omega^2)\,u-C(1+e^{-ika})\,v&=0\\
-C(1+e^{ika})\,u+(2C-M_2\omega^2)\,v&=0
\end{aligned}
$$

係数の行列式を0とおきます。$|1+e^{ika}|^2=2+2\cos ka=4\cos^2\dfrac{ka}{2}$ を使うと，

$$
M_1M_2\omega^4-2C(M_1+M_2)\omega^2+4C^2\sin^2\frac{ka}{2}=0
$$

となります。これを $\omega^2$ についての2次方程式として解くと，

$$
\finalanswer{\omega^2=C\left(\frac{1}{M_1}+\frac{1}{M_2}\right)\pm C\sqrt{\left(\frac{1}{M_1}+\frac{1}{M_2}\right)^2-\frac{4}{M_1M_2}\sin^2\frac{ka}{2}}}
$$

となります。負号が音響モード，正号が光学モードです。分散関係を図に示します。

<!-- FIGURE solution (2): 横軸 k（0 から π/a），縦軸 ω。下の曲線（音響モード）は原点から直線的に立ち上がり，k = π/a で √(2C/M1) に達して水平になる。上の曲線（光学モード）は k = 0 で √(2C(1/M1+1/M2)) から始まり，k = π/a で √(2C/M2) まで下がって水平になる。k = π/a に鉛直の破線を引く。縦軸に √(2C/M1)，√(2C/M2)，√(2C(1/M1+1/M2)) の目盛りを付け，√(2C/M1) と √(2C/M2) の間を「ギャップ」と矢印で示す。 -->

### (3)
$k\to0$ では $\sin^2\dfrac{ka}{2}\approx\dfrac{k^2a^2}{4}$ です。小さい方の解は，2次方程式の定数項を1次の係数で割った値で近似できます。

$$
\finalanswer{\omega_-\approx\sqrt{\frac{C}{2(M_1+M_2)}}\,ka},\qquad \finalanswer{\omega_+\approx\sqrt{2C\left(\frac{1}{M_1}+\frac{1}{M_2}\right)}}
$$

振幅比は (2) の1行目の式 $\dfrac{v}{u}=\dfrac{2C-M_1\omega^2}{C(1+e^{-ika})}$ に，$k\to0$ の値を代入して求めます。

$$
\finalanswer{\text{音響モード}:\ \frac{v}{u}=1},\qquad \finalanswer{\text{光学モード}:\ \frac{v}{u}=-\frac{M_1}{M_2}}
$$

となります。音響モードでは2種類の原子がそろって動く音波になり，光学モードでは重心を止めたまま逆位相に動きます。イオン結晶の光学モードは電気双極子を振動させるので，赤外光と強く結合します。

### (4)
$k=\pi/a$ では $1+e^{-i\pi}=0$ なので，(2) の連立方程式は $(2C-M_1\omega^2)u=0$ と $(2C-M_2\omega^2)v=0$ に分かれます。

$$
\finalanswer{\omega_-=\sqrt{\frac{2C}{M_1}}\ (v=0)},\qquad \finalanswer{\omega_+=\sqrt{\frac{2C}{M_2}}\ (u=0)}
$$

となります。音響モードの上端では重い原子だけが，光学モードの下端では軽い原子だけが振動します。$M_1>M_2$ なので，$\sqrt{2C/M_1}<\omega<\sqrt{2C/M_2}$ には波が存在しないギャップが開きます。

$M_1=M_2=M$ とおくと両者は $\sqrt{2C/M}$ に一致し，ギャップは閉じます。このとき鎖は間隔 $a/2$ の単原子鎖そのものです。4-1 の分散関係を周期 $a$ のゾーンに折り返したものに一致します。

===== FILE: 06solid_state/04/04_030.md =====
---
tags:
  - 標準
---

# フォノンの状態密度

## 問題
格子振動の状態密度 $D(\omega)$ を，角振動数が $\omega$ と $\omega+\mathrm{d}\omega$ の間にある基準振動の数が $D(\omega)\,\mathrm{d}\omega$ となるように定義する。$\hbar$ は換算プランク定数，$k_{\mathrm{B}}$ はボルツマン定数である。

前半では，質量 $M$ の原子 $N$ 個が間隔 $a$ でばね定数 $C$ のばねにつながれた一次元の鎖（長さ $L=Na$，周期境界条件）を考える。その分散関係は $\omega=\omega_{\mathrm{m}}\left|\sin\dfrac{ka}{2}\right|$，$\omega_{\mathrm{m}}=2\sqrt{C/M}$ である。後半では，体積 $V=L^3$ の立方体の中に $N$ 個の原子がある3次元の結晶を考え，周期境界条件を課す。以下の問いに答えよ。

(1) 一次元の鎖について，許される $k$ の間隔を求め，$0<\omega<\omega_{\mathrm{m}}$ での $D(\omega)$ を求めよ。また，$\displaystyle\int_0^{\omega_{\mathrm{m}}}D(\omega)\,\mathrm{d}\omega$ を求めよ。

(2) 3次元の結晶で，縦波1つと横波2つの3つの分枝がすべて $\omega=vk$（$k=|\boldsymbol{k}|$，$v$ は一定）に従うとする（デバイ近似）。$D(\omega)$ を求めよ。

(3) (2) の分散関係がある角振動数 $\omega_{\mathrm{D}}$ まで続き，それより上に振動がないとする。全モード数が $3N$ であることから $\omega_{\mathrm{D}}$ を求めよ。

(4) 振動数 $\omega$ のモードの熱エネルギーの平均は $\dfrac{\hbar\omega}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}$ である（零点エネルギーは温度によらないので除く）。$\Theta_{\mathrm{D}}=\hbar\omega_{\mathrm{D}}/k_{\mathrm{B}}$ とし，$T\ll\Theta_{\mathrm{D}}$ での定積比熱 $C_V$ を求めよ。$\displaystyle\int_0^\infty\frac{x^3}{e^x-1}\,\mathrm{d}x=\frac{\pi^4}{15}$ を用いてよい。

---

## 解答・解説

### (1)
周期境界条件 $e^{ikL}=1$ から $k=2\pi m/L$ なので，$k$ の間隔は $2\pi/L$ です。したがって $\mathrm{d}k$ の中のモード数は $\dfrac{L}{2\pi}\mathrm{d}k$ です。$\pm k$ が同じ $\omega$ を与えるので2倍し，$\mathrm{d}k$ を $\mathrm{d}\omega$ に換算します。

$$
D(\omega)=2\cdot\frac{L}{2\pi}\left|\frac{\mathrm{d}\omega}{\mathrm{d}k}\right|^{-1},\qquad
\frac{\mathrm{d}\omega}{\mathrm{d}k}=\frac{a\omega_{\mathrm{m}}}{2}\cos\frac{ka}{2}=\frac{a}{2}\sqrt{\omega_{\mathrm{m}}^{\,2}-\omega^2}
$$

$L=Na$ を使うと，

$$
\finalanswer{\Delta k=\frac{2\pi}{L}},\qquad \finalanswer{D(\omega)=\frac{2N}{\pi\sqrt{\omega_{\mathrm{m}}^{\,2}-\omega^2}}}
$$

となります。積分は $\displaystyle\int_0^{\omega_{\mathrm{m}}}\frac{\mathrm{d}\omega}{\sqrt{\omega_{\mathrm{m}}^{\,2}-\omega^2}}=\frac{\pi}{2}$ から求まります。

$$
\finalanswer{\int_0^{\omega_{\mathrm{m}}}D(\omega)\,\mathrm{d}\omega=N}
$$

となり，原子の自由度の数と一致します。状態密度の形を図に示します。

<!-- FIGURE solution (1): 横軸 ω（0 から ω_m を少し超えるところまで），縦軸 D(ω)。曲線 D = 2N/(π√(ω_m² − ω²)) を実線で描く。ω = 0 での値 2N/(π ω_m) に目盛りを付け，ω → ω_m で発散することを示すため ω = ω_m に鉛直の破線（漸近線）を引く。ω > ω_m では D = 0 の線を描く。 -->

群速度が0になるゾーン境界で状態密度が発散します（ファン・ホーブ特異点）。

### (2)
3次元では許される $\boldsymbol{k}$ が $\left(\dfrac{2\pi}{L}\right)^3$ の体積ごとに1個あります。1つの分枝について，$|\boldsymbol{k}|<k$ の球の中のモード数は $\dfrac{V}{(2\pi)^3}\cdot\dfrac{4\pi}{3}k^3$ です。3分枝分を足して $k=\omega/v$ とおきます。

$$
\mathcal{N}(\omega)=3\cdot\frac{V}{6\pi^2}\left(\frac{\omega}{v}\right)^3=\frac{V\omega^3}{2\pi^2v^3}
$$

これを $\omega$ で微分すると，

$$
\finalanswer{D(\omega)=\frac{3V\omega^2}{2\pi^2v^3}}
$$

となります。

### (3)
$\mathcal{N}(\omega_{\mathrm{D}})=3N$ とおきます。

$$
\frac{V\omega_{\mathrm{D}}^{\,3}}{2\pi^2v^3}=3N
$$

より，

$$
\finalanswer{\omega_{\mathrm{D}}=v\left(\frac{6\pi^2N}{V}\right)^{1/3}}
$$

となります。これを使うと，状態密度は $D(\omega)=\dfrac{9N\omega^2}{\omega_{\mathrm{D}}^{\,3}}$ とも書けます。

### (4)
熱エネルギーは，各モードの平均エネルギーを状態密度で重みづけて積分したものです。$x=\hbar\omega/k_{\mathrm{B}}T$ と置き換えると，上限は $\Theta_{\mathrm{D}}/T$ になります。$T\ll\Theta_{\mathrm{D}}$ では，この上限を $\infty$ にしてよくなります。

$$
\begin{aligned}
E&=\int_0^{\omega_{\mathrm{D}}}\frac{9N\omega^2}{\omega_{\mathrm{D}}^{\,3}}\cdot\frac{\hbar\omega}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}\,\mathrm{d}\omega
\approx 9Nk_{\mathrm{B}}T\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^3\int_0^\infty\frac{x^3}{e^x-1}\,\mathrm{d}x
=\frac{3\pi^4}{5}Nk_{\mathrm{B}}\frac{T^4}{\Theta_{\mathrm{D}}^{\,3}}
\end{aligned}
$$

これを $T$ で微分すると，

$$
\finalanswer{C_V=\frac{12\pi^4}{5}Nk_{\mathrm{B}}\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^3}
$$

となります。これはデバイの $T^3$ 則です。低温では熱的に励起されるのが $\omega\lesssim k_{\mathrm{B}}T/\hbar$ の長波長の音響モードだけなので，その数が $\omega^2$ に比例する状態密度から $T^3$ が生じます。

===== FILE: 06solid_state/04/04_040.md =====
---
tags:
  - 標準
---

# フォノンの量子化

## 問題
質量 $M$ の原子 $N$ 個が間隔 $a$ で並び，隣り合う原子がばね定数 $C$ のばねでつながれた一次元の鎖を，周期境界条件のもとで量子力学で扱う。$n$ 番目の原子の変位を $u_n$，運動量を $p_n$ とし，ハミルトニアンを

$$
H=\sum_{n=1}^{N}\frac{p_n^{\,2}}{2M}+\frac{C}{2}\sum_{n=1}^{N}(u_{n+1}-u_n)^2
$$

とする。演算子は $[u_n,p_m]=i\hbar\delta_{nm}$，$[u_n,u_m]=[p_n,p_m]=0$ を満たす。許される波数 $k=\dfrac{2\pi m}{Na}$（$-\pi/a<k\le\pi/a$）に対して基準座標を

$$
Q_k=\frac{1}{\sqrt{N}}\sum_n u_n e^{-ikna},\qquad P_k=\frac{1}{\sqrt{N}}\sum_n p_n e^{ikna}
$$

で定義する。逆変換は $u_n=\dfrac{1}{\sqrt{N}}\sum_k Q_ke^{ikna}$，$p_n=\dfrac{1}{\sqrt{N}}\sum_k P_ke^{-ikna}$ であり，$\sum_n e^{i(k-k')na}=N\delta_{kk'}$ を用いてよい。$u_n,p_n$ はエルミート演算子である。以下の問いに答えよ。

(1) $Q_k^\dagger$，$P_k^\dagger$ を $Q_{-k}$，$P_{-k}$ で表し，交換関係 $[Q_k,P_{k'}]$ を求めよ。

(2) $H$ を $Q_k,P_k$ で表し，$H=\sum_k\left[\dfrac{P_kP_{-k}}{2M}+\dfrac{1}{2}M\omega_k^{\,2}Q_kQ_{-k}\right]$ の形になることを示して $\omega_k$ を求めよ。

(3) $k\ne0$ に対して $a_k=\sqrt{\dfrac{M\omega_k}{2\hbar}}\left(Q_k+\dfrac{i}{M\omega_k}P_{-k}\right)$ と定義する。$[a_k,a_{k'}^\dagger]$ を求めよ。また，$k=0$ の一様な並進を除いたハミルトニアンが $H=\sum_k\hbar\omega_k\left(a_k^\dagger a_k+\dfrac{1}{2}\right)$ と書けることを示せ。

(4) $a_k^\dagger a_k$ の固有値が $0,1,2,\ldots$ であることを用いて，温度 $T$ の熱平衡でのフォノン数の平均 $\langle n_k\rangle$ を求めよ。また，$k_{\mathrm{B}}T\gg\hbar\omega_k$ でのモード1つあたりの平均エネルギーを求めよ。$k_{\mathrm{B}}$ はボルツマン定数である。

---

## 解答・解説

### (1)
$u_n,p_n$ はエルミートなので，エルミート共役をとると指数関数の符号だけが反転します。

$$
\finalanswer{Q_k^\dagger=Q_{-k}},\qquad \finalanswer{P_k^\dagger=P_{-k}}
$$

交換関係は定義を代入し，$[u_n,p_m]=i\hbar\delta_{nm}$ で和を1つ消して計算します。

$$
[Q_k,P_{k'}]=\frac{1}{N}\sum_{n,m}e^{-ikna}e^{ik'ma}[u_n,p_m]=\frac{i\hbar}{N}\sum_n e^{-i(k-k')na}
$$

より，

$$
\finalanswer{[Q_k,P_{k'}]=i\hbar\,\delta_{kk'}}
$$

となります。$Q_k$ と $P_k$ は正準共役な組です。

### (2)
運動エネルギーには逆変換を代入し，$n$ についての和を先に実行します。

$$
\sum_n p_n^{\,2}=\frac{1}{N}\sum_{k,k'}P_kP_{k'}\sum_n e^{-i(k+k')na}=\sum_kP_kP_{-k}
$$

ポテンシャルでは $u_{n+1}-u_n=\dfrac{1}{\sqrt{N}}\sum_kQ_ke^{ikna}(e^{ika}-1)$ と書けます。同様に計算すると，因子 $(e^{ika}-1)(e^{-ika}-1)=2-2\cos ka=4\sin^2\dfrac{ka}{2}$ が現れます。

$$
\frac{C}{2}\sum_n(u_{n+1}-u_n)^2=\sum_k2C\sin^2\frac{ka}{2}\,Q_kQ_{-k}
$$

これを $\dfrac{1}{2}M\omega_k^{\,2}Q_kQ_{-k}$ と比べると，

$$
\finalanswer{\omega_k=2\sqrt{\frac{C}{M}}\left|\sin\frac{ka}{2}\right|}
$$

となり，古典的な分散関係と一致します。

### (3)
$a_k^\dagger=\sqrt{\dfrac{M\omega_k}{2\hbar}}\left(Q_{-k}-\dfrac{i}{M\omega_k}P_k\right)$ です。$\omega_{-k}=\omega_k$ と (1) の交換関係を使って計算します。

$$
[a_k,a_{k'}^\dagger]=\frac{M\omega_k}{2\hbar}\cdot\frac{1}{M\omega_k}\left(-i[Q_k,P_{k'}]+i[P_{-k},Q_{-k'}]\right)=\frac{1}{2\hbar}(\hbar+\hbar)\delta_{kk'}
$$

より，

$$
\finalanswer{[a_k,a_{k'}^\dagger]=\delta_{kk'}}
$$

となります。次に $\hbar\omega_ka_k^\dagger a_k$ を展開します。

$$
\hbar\omega_ka_k^\dagger a_k=\frac{1}{2}M\omega_k^{\,2}Q_{-k}Q_k+\frac{P_kP_{-k}}{2M}+\frac{i\omega_k}{2}\left(Q_{-k}P_{-k}-P_kQ_k\right)
$$

$k$ について和をとると，最後の項では $k\to-k$ の付け替えで $Q_{-k}P_{-k}$ を $Q_kP_k$ にできます。その結果，最後の項は $\dfrac{i\omega_k}{2}[Q_k,P_k]=-\dfrac{\hbar\omega_k}{2}$ の和になります。

$$
\finalanswer{H=\sum_{k\ne0}\hbar\omega_k\left(a_k^\dagger a_k+\frac{1}{2}\right)}
$$

となります。格子振動は独立な調和振動子の集まりであり，$a_k^\dagger$ は波数 $k$ のフォノンを1個つくる演算子です。

### (4)
モード $k$ のエネルギー準位は $\left(n+\dfrac{1}{2}\right)\hbar\omega_k$ です。カノニカル分布で $n$ を平均します。$x=e^{-\hbar\omega_k/k_{\mathrm{B}}T}$ とおくと，等比級数の和とその微分で計算できます。

$$
\langle n_k\rangle=\frac{\sum_n n\,x^n}{\sum_n x^n}=\frac{x}{1-x}
$$

より，

$$
\finalanswer{\langle n_k\rangle=\frac{1}{e^{\hbar\omega_k/k_{\mathrm{B}}T}-1}}
$$

となります。これはボース・アインシュタイン分布で，化学ポテンシャルは0です。高温では $\dfrac{1}{e^y-1}\approx\dfrac{1}{y}-\dfrac{1}{2}$ と展開できます。

$$
\finalanswer{\hbar\omega_k\left(\langle n_k\rangle+\frac{1}{2}\right)\approx k_{\mathrm{B}}T}
$$

となり，古典的な等分配則に戻ります。

===== FILE: 06solid_state/04/04_050.md =====
---
tags:
  - 発展
---

# 中性子非弾性散乱とフォノン

## 問題
質量 $m_{\mathrm{n}}$ の中性子が，波数ベクトル $\boldsymbol{k}$ で結晶に入射し，フォノンを1個生成または消滅させて，波数ベクトル $\boldsymbol{k}'$ で出ていく。フォノンの波数ベクトルを $\boldsymbol{q}$（第1ブリルアンゾーン内），角振動数を $\omega(\boldsymbol{q})$ とする。結晶運動量の保存は逆格子ベクトル $\boldsymbol{G}$ の差を除いて成り立つ。以下の問いに答えよ。

(1) フォノンを生成する場合と消滅させる場合のそれぞれについて，エネルギー保存と結晶運動量保存の式を書き，$\hbar\omega$ と $\boldsymbol{q}$ を $\boldsymbol{k},\boldsymbol{k}'$ で表せ。

(2) 波長 $0.20\ \mathrm{nm}$ の中性子の運動エネルギーと，同じ波長のX線光子のエネルギーを求めよ。$h=6.626\times10^{-34}\ \mathrm{J\,s}$，$m_{\mathrm{n}}=1.675\times10^{-27}\ \mathrm{kg}$，$c=2.998\times10^{8}\ \mathrm{m/s}$，$e=1.602\times10^{-19}\ \mathrm{C}$ とする。

(3) 原子が間隔 $a=0.300\ \mathrm{nm}$ で $x$ 方向に並んだ一次元的な結晶があり，分散関係が $\hbar\omega(q)=\hbar\omega_{\mathrm{m}}\left|\sin\dfrac{qa}{2}\right|$ で与えられるとする。エネルギー $E_{\mathrm{i}}=30.0\ \mathrm{meV}$ の中性子を $+x$ 方向に入射し，$+x$ 方向に出ていく中性子のエネルギーを測ったところ $E_{\mathrm{f}}=20.0\ \mathrm{meV}$ であった。$\dfrac{\hbar^2}{2m_{\mathrm{n}}}=2.072\times10^{-2}\ \mathrm{meV\,nm^2}$ として，フォノンのエネルギー $\hbar\omega$，波数 $q$，および $\hbar\omega_{\mathrm{m}}$ を求めよ。

(4) 同じ $q$ のフォノンについて，生成過程と消滅過程の散乱強度の比を求めよ。散乱確率は，生成では $\langle n\rangle+1$，消滅では $\langle n\rangle$ に比例するとしてよい。$\langle n\rangle$ は温度 $T$ でのフォノン数の平均である。$T=300\ \mathrm{K}$，$\hbar\omega=10.0\ \mathrm{meV}$，$k_{\mathrm{B}}=8.617\times10^{-5}\ \mathrm{eV/K}$ として数値も求めよ。

---

## 解答・解説

### (1)
フォノンを生成する場合は，中性子が失ったエネルギーと運動量がフォノンに渡ります。消滅させる場合は，逆に中性子がフォノンのエネルギーと運動量を受け取ります。結晶運動量は逆格子ベクトルの差を除いて保存するので，$\boldsymbol{q}$ がゾーン内に入るように $\boldsymbol{G}$ を選びます。

$$
\begin{aligned}
&\text{生成}:\quad \frac{\hbar^2k^2}{2m_{\mathrm{n}}}=\frac{\hbar^2k'^2}{2m_{\mathrm{n}}}+\hbar\omega(\boldsymbol{q}),\qquad \boldsymbol{k}=\boldsymbol{k}'+\boldsymbol{q}-\boldsymbol{G}\\
&\text{消滅}:\quad \frac{\hbar^2k^2}{2m_{\mathrm{n}}}+\hbar\omega(\boldsymbol{q})=\frac{\hbar^2k'^2}{2m_{\mathrm{n}}},\qquad \boldsymbol{k}+\boldsymbol{q}=\boldsymbol{k}'+\boldsymbol{G}
\end{aligned}
$$

これらを $\hbar\omega$ と $\boldsymbol{q}$ について解くと，

$$
\finalanswer{\text{生成}:\ \hbar\omega=\frac{\hbar^2(k^2-k'^2)}{2m_{\mathrm{n}}},\quad \boldsymbol{q}=\boldsymbol{k}-\boldsymbol{k}'+\boldsymbol{G}},\qquad
\finalanswer{\text{消滅}:\ \hbar\omega=\frac{\hbar^2(k'^2-k^2)}{2m_{\mathrm{n}}},\quad \boldsymbol{q}=\boldsymbol{k}'-\boldsymbol{k}+\boldsymbol{G}}
$$

となります。$\boldsymbol{k},\boldsymbol{k}'$ を測れば，分散関係の1点 $(\boldsymbol{q},\omega)$ が決まります。

### (2)
中性子のエネルギーはド・ブロイの関係 $p=h/\lambda$ から $\dfrac{h^2}{2m_{\mathrm{n}}\lambda^2}$，光子のエネルギーは $\dfrac{hc}{\lambda}$ です。数値を代入します。

$$
\frac{h^2}{2m_{\mathrm{n}}\lambda^2}=\frac{(6.626\times10^{-34})^2}{2\times1.675\times10^{-27}\times(0.20\times10^{-9})^2}\ \mathrm{J}=3.28\times10^{-21}\ \mathrm{J}
$$

$$
\finalanswer{E_{\mathrm{n}}\approx 20\ \mathrm{meV}},\qquad \finalanswer{E_{\mathrm{X}}\approx 6.2\ \mathrm{keV}}
$$

となります。どちらも波数は原子間隔の逆数程度ですが，中性子のエネルギーはフォノンのエネルギー（$1\sim100\ \mathrm{meV}$）と同程度です。そのため，散乱によるエネルギーの変化を相対的に大きな量として測れます。X線では同じ変化が $10^{-6}$ 程度にしかならず，分解するのが困難です。

### (3)
$E_{\mathrm{f}}<E_{\mathrm{i}}$ なので，フォノンの生成です。エネルギー保存から $\hbar\omega=E_{\mathrm{i}}-E_{\mathrm{f}}$ です。波数は $k=\sqrt{E/(\hbar^2/2m_{\mathrm{n}})}$ から求まり，$k_{\mathrm{i}}=\sqrt{30.0/0.02072}=38.05\ \mathrm{nm^{-1}}$，$k_{\mathrm{f}}=\sqrt{20.0/0.02072}=31.07\ \mathrm{nm^{-1}}$ です。どちらも $+x$ 向きなので，$q=k_{\mathrm{i}}-k_{\mathrm{f}}-G$ です。ゾーン境界 $\pi/a=10.47\ \mathrm{nm^{-1}}$ より小さいので $G=0$ となります。

$$
\finalanswer{\hbar\omega=10.0\ \mathrm{meV}},\qquad \finalanswer{q\approx 6.98\ \mathrm{nm^{-1}}}
$$

このとき $\dfrac{qa}{2}=1.047\ \mathrm{rad}$（$60^\circ$）で，$\sin\dfrac{qa}{2}=0.866$ です。分散関係に代入すると，

$$
\finalanswer{\hbar\omega_{\mathrm{m}}=\frac{10.0\ \mathrm{meV}}{0.866}\approx 11.5\ \mathrm{meV}}
$$

となります。入射エネルギーや散乱角を変えて測定を繰り返すと，分散曲線全体が得られます。

### (4)
強度の比は散乱確率の比です。$\langle n\rangle=\dfrac{1}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}$ を代入すると $\langle n\rangle+1=\dfrac{e^{\hbar\omega/k_{\mathrm{B}}T}}{e^{\hbar\omega/k_{\mathrm{B}}T}-1}$ なので，比は簡単な形になります。

$$
\finalanswer{\frac{I_{\text{生成}}}{I_{\text{消滅}}}=\frac{\langle n\rangle+1}{\langle n\rangle}=e^{\hbar\omega/k_{\mathrm{B}}T}}
$$

$T=300\ \mathrm{K}$ では $k_{\mathrm{B}}T=25.85\ \mathrm{meV}$ なので，$\hbar\omega/k_{\mathrm{B}}T=0.387$ です。

$$
\finalanswer{\frac{I_{\text{生成}}}{I_{\text{消滅}}}\approx 1.47}
$$

となります。この関係は詳細釣り合いとよばれます。低温ほど消滅過程は弱くなり，$T\to0$ ではフォノンの生成だけが観測されます。

===== FILE: 06solid_state/04/04_060.md =====
---
tags:
  - 標準
---

# フォノンの群速度とゾーン境界

## 問題
質量 $M$ の原子が間隔 $a$ で並び，隣り合う原子がばね定数 $C$ のばねでつながれた一次元の単原子鎖を考える。$n$ 番目の原子の変位を $u_n$ とすると，$u_n=A\,e^{i(kna-\omega t)}$（$A$ は複素定数）の形の解が存在し，その分散関係は $\omega(k)=2\sqrt{\dfrac{C}{M}}\left|\sin\dfrac{ka}{2}\right|$ である。群速度を $v_{\mathrm{g}}=\dfrac{\mathrm{d}\omega}{\mathrm{d}k}$，位相速度を $v_{\mathrm{p}}=\dfrac{\omega}{k}$ と定義する。以下の問いに答えよ。

(1) $0<k\le\pi/a$ での $v_{\mathrm{g}}(k)$ と $v_{\mathrm{p}}(k)$ を求め，$k\to0$ と $k=\pi/a$ での値をそれぞれ求めよ。

(2) $k=\pi/a$ の解と $k=-\pi/a$ の解が同じ原子の運動を表すことを示せ。また，$k=\pi/a$ の解の実部 $u_n(t)$ を，$A=|A|e^{i\varphi}$ として求めよ。

(3) 鎖に沿って進む波を，原子が間隔 $a$ で並んだ「面」による反射とみなす。垂直入射（$\theta=90^\circ$）の1次のブラッグ条件を満たす波長 $\lambda$ と，それに対応する波数 $k$ を求めよ。

(4) 一般の一次元結晶の分散関係 $\omega(k)$ が，$\omega(k+2\pi/a)=\omega(k)$ と $\omega(-k)=\omega(k)$ を満たし，$k=\pi/a$ の近くで微分可能であるとする。$\left.\dfrac{\mathrm{d}\omega}{\mathrm{d}k}\right|_{k=\pi/a}=0$ を示せ。

---

## 解答・解説

### (1)
$0<k\le\pi/a$ では $\sin\dfrac{ka}{2}\ge0$ なので，絶対値を外して微分できます。

$$
\finalanswer{v_{\mathrm{g}}=a\sqrt{\frac{C}{M}}\cos\frac{ka}{2}},\qquad \finalanswer{v_{\mathrm{p}}=\frac{2}{k}\sqrt{\frac{C}{M}}\sin\frac{ka}{2}}
$$

$k\to0$ では $\cos\to1$，$\sin\dfrac{ka}{2}\approx\dfrac{ka}{2}$ なので，どちらも音速に一致します。$k=\pi/a$ では $\cos\dfrac{\pi}{2}=0$ です。

$$
\finalanswer{k\to0:\ v_{\mathrm{g}}=v_{\mathrm{p}}=a\sqrt{\frac{C}{M}}},\qquad
\finalanswer{k=\frac{\pi}{a}:\ v_{\mathrm{g}}=0,\quad v_{\mathrm{p}}=\frac{2a}{\pi}\sqrt{\frac{C}{M}}}
$$

となります。2つの速度の $k$ 依存性を図に示します。

<!-- FIGURE solution (1): 横軸 k（0 から π/a），縦軸 速度（a√(C/M) を単位に 0〜1）。群速度 v_g = cos(ka/2) を実線で，位相速度 v_p = sin(ka/2)/(ka/2) を破線で描く。k = 0 で両方とも 1 から出発する。k = π/a で v_g は 0，v_p は 2/π ≈ 0.64 になることを黒丸で示し，値を注記する。 -->

ゾーン境界では位相速度は有限ですが，エネルギーを運ぶ群速度は0になります。

### (2)
$k=\pm\pi/a$ を代入すると，$e^{\pm i\pi n}=(-1)^n$ はどちらの符号でも同じです。

$$
u_n=A\,e^{\pm i\pi n}e^{-i\omega t}=A(-1)^ne^{-i\omega t}
$$

したがって2つの解は同じ運動を表します。実部をとると，

$$
\finalanswer{u_n(t)=|A|(-1)^n\cos(\omega t-\varphi)}
$$

となります。一般の $k$ では実部が $\cos(kna-\omega t+\varphi)$ となり，山の位置が時間とともに移動します。$k=\pi/a$ では，すべての原子がその場で同じ振動数で振動し，隣どうしが逆位相になるだけで，パターンは移動しません。これは右向きと左向きの波が同じ振幅で重なった定在波です。

### (3)
間隔 $d=a$ の面に垂直入射（$\sin\theta=1$）する波の1次のブラッグ条件は $2a=\lambda$ です。

$$
\finalanswer{\lambda=2a},\qquad \finalanswer{k=\frac{2\pi}{\lambda}=\frac{\pi}{a}}
$$

となります。ゾーン境界の波は，各原子で反射された波が強め合うので，逆向きに進む波と同じ強さで混ざります。その結果，(2) で見た定在波になり，群速度が0になります。

### (4)
周期性と対称性を順に使って，$k=\pi/a$ の両側の値を結びつけます。小さな $\kappa$ に対して，

$$
\omega\!\left(\frac{\pi}{a}+\kappa\right)=\omega\!\left(-\frac{\pi}{a}+\kappa\right)=\omega\!\left(\frac{\pi}{a}-\kappa\right)
$$

が成り立ちます。1つ目の等号では周期性を，2つ目の等号では偶関数であることを使いました。$\omega(k)$ は $k=\pi/a$ について左右対称です。この式の両辺を $\kappa$ で微分して $\kappa=0$ とおくと，$\omega'(\pi/a)=-\omega'(\pi/a)$ となります。

$$
\finalanswer{\left.\frac{\mathrm{d}\omega}{\mathrm{d}k}\right|_{k=\pi/a}=0}
$$

となります。この結果はばね模型の細部によらず，周期性と反転対称性だけから決まります。そのため二原子鎖の音響・光学モードのどちらでも，また電子のエネルギーバンドでも，ゾーン境界で群速度は0になります。

===== END =====