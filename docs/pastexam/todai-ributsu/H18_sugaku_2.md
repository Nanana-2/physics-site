---
title: 東大理物 平成18年度 数学 第2問：変分法・ベルトラミの恒等式と最小回転面
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成18年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成18年度 数学 第2問：変分法・ベルトラミの恒等式と最小回転面

## 問題

以下の積分を考える。

$$
S = \int_{x_0}^{x_1} F\bigl(y(x), y'(x)\bigr)\,\mathrm{d}x. \tag{1}
$$

ここで，$y'(x) \equiv \mathrm{d}y(x)/\mathrm{d}x$ である。また，$F(y, y')$ および $y(x)$ は，いずれの変数についても何回でも微分可能な連続かつ一価な関数とする。さらに，曲線 $y = y(x)$ の端点は，$y(x_0) = y_0,\ y(x_1) = y_1$ のように固定されているものとする。以下の設問に答えよ。

(i) 積分 $S$ が曲線 $y = y(x)$ の変化に対して極値をとるための十分条件となる微分方程式を，関数 $y(x)$ の微小変分 $\delta y(x)$ を考える事で導出せよ。

(ii) 設問 (i) で求めた微分方程式は，

$$
F - y'\frac{\partial F}{\partial y'} = C,
$$

に変形できることを示せ。ここで，$C$ は定数である。

(iii) 曲線 $y = y(x)$ の両端点が $x_1 > x_0 > 0,\ y_1 > 0,\ y_0 > 0$ を満たすとする。この曲線を $x$ 軸のまわりに $360^\circ$ 回転して得られる回転面を考え，その表面積を (1) 式の形の積分を用いて表せ。

(iv) 設問 (iii) で得られた表面積を最小にする曲線 $y = y(x)$ が満たす微分方程式を導け。

(v) 設問 (iv) で得られた微分方程式を解き，曲線 $y(x)$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成18年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
端点を固定した微小変分 $\delta y(x)$ に対して積分の1次変分 $\delta S$ を計算し，部分積分で $\delta y'(x)$ の微分を隣の因子へ移すと，変分法の基本補題からオイラー・ラグランジュ方程式を導くことができます。

被積分関数 $F(y, y')$ が独立変数 $x$ を陽に含まないときは，2階のオイラー・ラグランジュ方程式を1階の保存量の式へ積分することができます。回転面の表面積も $x$ を陽に含まない汎関数なので，この1階微分方程式を変数分離で解いて曲線を求めることができます。
</div>

### (i)

原本では十分条件とありますが，1次変分から導くオイラー・ラグランジュ方程式は，一般には極値の必要条件です。方程式を満たす曲線では1次変分が $0$ になりますが，極小か極大かの判定には高次の変分の確認が必要です。

端点固定の変分は，$\delta y(x_0)=0$，$\delta y(x_1)=0$ を満たします。$\delta y'=\mathrm{d}(\delta y)/\mathrm{d}x$ を用い，第2項を部分積分して1次変分を計算します。

$$
\begin{aligned}
\delta S &= \int_{x_0}^{x_1} \left(\frac{\partial F}{\partial y}\delta y + \frac{\partial F}{\partial y'}\delta y'\right)\mathrm{d}x \\
&= \int_{x_0}^{x_1} \frac{\partial F}{\partial y}\delta y\,\mathrm{d}x + \left[\frac{\partial F}{\partial y'}\delta y\right]_{x_0}^{x_1} - \int_{x_0}^{x_1} \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right)\delta y\,\mathrm{d}x \\
&= \int_{x_0}^{x_1} \left\{\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right)\right\}\delta y(x)\,\mathrm{d}x
\end{aligned}
$$

ここで境界条件 $\delta y(x_0)=0$，$\delta y(x_1)=0$ より境界項が $0$ になります。任意の微小変分 $\delta y(x)$ に対して停留条件 $\delta S = 0$ が成り立つためには，変分法の基本補題より被積分関数の中括弧内が恒等的に $0$ でなければなりません。

$$
\finalanswer{\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right) = 0}
$$

### (ii)

$F - y'\dfrac{\partial F}{\partial y'}$ を $x$ で全微分します。$F(y, y')$ は $x$ を陽に含まないため，$\dfrac{\mathrm{d}F}{\mathrm{d}x} = \dfrac{\partial F}{\partial y}y' + \dfrac{\partial F}{\partial y'}y''$ です。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}x}\left(F - y'\frac{\partial F}{\partial y'}\right) &= \left(\frac{\partial F}{\partial y}y' + \frac{\partial F}{\partial y'}y''\right) - y''\frac{\partial F}{\partial y'} - y'\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right) \\
&= y'\left\{\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\partial F}{\partial y'}\right)\right\}
\end{aligned}
$$

設問 (i) のオイラー・ラグランジュ方程式より右辺の中括弧内は $0$ なので，次式が成り立ちます。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left(F - y'\frac{\partial F}{\partial y'}\right) = 0
$$

したがって，$x$ によらない定数 $C$ を用いて $F - y'\dfrac{\partial F}{\partial y'} = C$ と変形することができます。

### (iii)
曲線の弧長要素は次のとおりです。

$$
\mathrm{d}s=\sqrt{1+y'(x)^2}\,\mathrm{d}x
$$

回転の半径は $|y(x)|$ なので，一般の回転面の面積は次の式です。

$$
\finalanswer{S=2\pi\int_{x_0}^{x_1}|y(x)|\sqrt{1+y'(x)^2}\,\mathrm{d}x}
$$

端点で $y_0,y_1>0$ という条件だけでは，途中でも $y>0$ とは限りません。以下では，軸を横切らない正の半径関数 $y(x)>0$ を考え，$|y|=y$ として停留曲線を求めます。

### (iv)
正の半径関数について，$F=2\pi y\sqrt{1+y'^2}$ です。偏微分は次のようになります。

$$
\begin{aligned}
\frac{\partial F}{\partial y}&=2\pi\sqrt{1+y'^2},\\
\frac{\partial F}{\partial y'}&=\frac{2\pi yy'}{\sqrt{1+y'^2}}
\end{aligned}
$$

オイラー・ラグランジュ方程式に代入します。

$$
\begin{aligned}
0&=\frac{\partial F}{\partial y}-\frac{\mathrm{d}}{\mathrm{d}x}\frac{\partial F}{\partial y'}\\
&=\frac{2\pi}{(1+y'^2)^{3/2}}\bigl(1+y'^2-yy''\bigr)
\end{aligned}
$$

したがって，面積を最小にする滑らかな正の曲線は，次の必要条件を満たします。

$$
\finalanswer{yy''=1+y'^2}
$$

設問(ii)の保存量を使うと，さらに次の関係が得られます。

$$
\begin{aligned}
F-y'\frac{\partial F}{\partial y'}
&=2\pi y\sqrt{1+y'^2}-\frac{2\pi yy'^2}{\sqrt{1+y'^2}}\\
&=\frac{2\pi y}{\sqrt{1+y'^2}}\\
&=C
\end{aligned}
$$

$c=C/(2\pi)>0$ とおくと，次の1階の式になります。

$$
y'^2=\frac{y^2}{c^2}-1
$$

ただし，1階の式だけでは定数関数 $y\equiv c$ も解になります。定数関数は元の式 $yy''=1+y'^2$ を満たさないので，停留曲線から除きます。

### (v)
$y>c$ の区間で1階の式を変数分離します。

$$
\frac{\mathrm{d}y}{\sqrt{y^2-c^2}}=\pm\frac{\mathrm{d}x}{c}
$$

$y=c\cosh t$ とおくと，積分して $t=\pm(x-b)/c$ です。$\cosh$ は偶関数なので，両方の符号から同じ関数が得られます。$y=c$ の折り返し点では元の2階方程式から $y''=1/c$ となり，次の関数で滑らかにつながります。

$$
\finalanswer{y(x)=c\cosh\!\left(\frac{x-b}{c}\right),\qquad c>0}
$$

これは面積が停留する曲線です。$c,b$ は端点条件を満たすものから選びますが，任意の端点条件で解が存在し，一意に定まるわけではありません。複数の解がある場合は，2次変分や面積の比較による最小性の判定が必要です。

例えば両端の半径が同じ $R$，端点間の距離が $d=x_1-x_0$ なら，$b=(x_0+x_1)/2$ であり，次の条件が必要です。

$$
R=c\cosh\!\left(\frac{d}{2c}\right)
$$

$q=d/(2c)$ とおくと $d/(2R)=q/\cosh q$ です。右辺の最大値は $q\tanh q=1$ を満たす点で約 $0.6627$ なので，$d/R>1.3255$ なら正の滑らかな停留曲線は存在しません。したがって，得た懸垂線を端点条件によらず最小曲線と断定することはできません。
