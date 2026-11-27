---
title: 東大理物 平成26年度 物理学 第1問：水素原子基底状態と磁場中の荷電粒子
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成26年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号および式番号の表記を整えています。
---

# 東大理物 平成26年度 物理学 第1問：水素原子基底状態と磁場中の荷電粒子

## 問題

外部電磁場中での質量 $m$，電荷 $q$ の荷電粒子の量子力学的運動を考える。そのハミルトニアンは

$$
H = \frac{1}{2m}(\boldsymbol{p} - q\boldsymbol{A})^2 + q\phi
$$

で与えられる。ここでは，粒子のスピン自由度は考えない。$\phi$，$\boldsymbol{A}$ は，それぞれ電磁場のスカラーポテンシャルとベクトルポテンシャルを表し，ここでは時間によらないとする。量子化条件は，座標と運動量の正準交換関係，$[x, p_x] = x p_x - p_x x = i\hbar$，$[y, p_y] = [z, p_z] = i\hbar$，で与えられる。ここで，$\hbar = h / 2\pi$ で，$h$ はプランク定数を表す。以下の問いに答えよ。

まず，原点に置かれた $-q$ の電荷の作る静電ポテンシャルの中の運動を考える。その座標表示のハミルトニアンは，

$$
H = -\frac{\hbar^2}{2m}\nabla^2 - \frac{q^2}{4\pi\epsilon_0 r}
$$

で与えられる。ここで，$r = |\boldsymbol{r}|$ は原点からの距離，$\epsilon_0$ は真空の誘電率を表す。

(1) この基底状態は球対称性を持つ s 波状態となり，その波動関数 $\psi(r)$ は動径座標 $r$ のみの関数となる。長さの次元を持つ定数 $r_0$ と，エネルギーの次元を持つ定数 $E_0$ を適当に選んで，$r = r_0 \rho$，$E = -E_0 \varepsilon$ とおくと，基底状態のシュレーディンガー方程式は，無次元変数 $\rho$ と無次元エネルギー $\varepsilon$ を使って，

$$
\left[\frac{\mathrm{d}^2}{\mathrm{d}\rho^2} + \frac{2}{\rho}\frac{\mathrm{d}}{\mathrm{d}\rho} + \frac{2}{\rho}\right]\psi = \varepsilon\psi \tag{1}
$$

と書くことができる。このとき，$r_0$ と $E_0$ を，$m$，$q$，$\epsilon_0$，$\hbar$ を用いて表せ。必要であれば，任意の $r$ のみの関数 $f(r)$ にたいし，$\nabla^2 f(r) = \left(\dfrac{\mathrm{d}^2}{\mathrm{d}r^2} + \dfrac{2}{r}\dfrac{\mathrm{d}}{\mathrm{d}r}\right) f(r)$ となることを用いよ。

(2) (1) 式の節なし解 $\psi(r) = c e^{-\rho} = c e^{-r/r_0}$ は基底状態の波動関数を与える。ここで，定数 $c$ は波動関数の規格化因子を表す。基底状態のエネルギー $E$ と粒子の動径座標の拡がりの大きさ $\sqrt{\langle r^2 \rangle}$ を，それぞれ，$E_0$ と $r_0$ を用いて表せ。ここで，$\langle r^2 \rangle$ は $r^2$ の期待値を表す。

次に，$z$ 軸の負の方向を向いた強さ $B$ の一様な静磁場中での荷電粒子の運動を考える。このとき，ポテンシャルを $\boldsymbol{A}(\boldsymbol{r}) = (By/2, -Bx/2, 0)$，$\phi(\boldsymbol{r}) = 0$，とすると，ハミルトニアンは，

$$
H = \frac{1}{2m}\left[\left(p_x - \frac{qBy}{2}\right)^2 + \left(p_y + \frac{qBx}{2}\right)^2 + p_z^2\right] \tag{2}
$$

で与えられる。

(3) $p_1 = p_x - \dfrac{qBy}{2}$，$p_2 = p_y + \dfrac{qBx}{2}$，$p_z$ の間の交換関係を求めよ。

(4) 適当な定数 $k$ を選んで，新しい正準座標 $(X, P)$ を $X = k p_2$ と $P = p_1$ ととることにより，$(x, y)$ 方向の運動が 1 次元の調和振動子と等価になることを示し，その固有振動数 $\omega$ を求めよ。また，古典的描像では $\omega$ が何を表すか述べよ。

(5) $P' = p_x + \dfrac{qBy}{2}$ は正準座標 $(X, P)$ のそれぞれと可換になることを示せ。また，$P'$ と正準共役な関係にあるエルミート演算子 $X'$ を，正準座標 $(X, P)$ と可換になるように，$x$ と $p_y$ の線形結合で構成せよ。

(6) ハミルトニアン (2) は正準座標 $(X, P)$ と $p_z$ で書かれており，もう一組の正準座標 $(X', P')$ には依存しない。今，$(X, P)$ 座標にのみ注目したとき，$X$ を対角化する表示で基底状態の波動関数はどう表されるか。さらに変数 $X'$ を考慮に入れる場合，それが特定の実数値 $X' = a$ を持つときには，この基底状態の波動関数を元の座標 $x$ で書き表すことができる。そのとき，$a$ はどういう意味を持つか述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成26年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号および式番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
基底状態は球対称なので，シュレーディンガー方程式は動径 $r$ だけの常微分方程式になります。長さとエネルギーを適当な定数 $r_0$，$E_0$ で割って無次元にすると，方程式から $\hbar$，$m$，$q$ などの定数が消え，基底状態の形が簡単な関数で書けます。

一様な磁場の中では，力学的運動量の $x$ 成分と $y$ 成分が交換しません。この2つの交換関係が $[x,p]$ と同じ形になるように定数倍すると，ハミルトニアンは1次元の調和振動子と同じ形になります。残りの正準変数の組はハミルトニアンに入らないので，エネルギー準位は縮退します。
</div>

### (1)
球対称な波動関数 $\psi(r)$ に対するシュレーディンガー方程式 $H\psi = E\psi$ に $r = r_0 \rho$，$E = -E_0 \varepsilon$ を代入します。$\dfrac{\mathrm{d}}{\mathrm{d}r} = \dfrac{1}{r_0}\dfrac{\mathrm{d}}{\mathrm{d}\rho}$ より，次式が得られます。

$$
\begin{aligned}
-\frac{\hbar^2}{2m r_0^2}\left(\frac{\mathrm{d}^2}{\mathrm{d}\rho^2} + \frac{2}{\rho}\frac{\mathrm{d}}{\mathrm{d}\rho}\right)\psi - \frac{q^2}{4\pi\epsilon_0 r_0 \rho}\psi &= -E_0 \varepsilon \psi \\
\frac{\hbar^2}{2m r_0^2 E_0}\left(\frac{\mathrm{d}^2}{\mathrm{d}\rho^2} + \frac{2}{\rho}\frac{\mathrm{d}}{\mathrm{d}\rho}\right)\psi + \frac{q^2}{4\pi\epsilon_0 r_0 E_0}\frac{1}{\rho}\psi &= \varepsilon\psi
\end{aligned}
$$

これを (1) 式と比較すると，次の条件が成り立てばよいことがわかります。

$$
\frac{\hbar^2}{2m r_0^2 E_0} = 1, \qquad \frac{q^2}{4\pi\epsilon_0 r_0 E_0} = 2
$$

第 1 式より $E_0 = \dfrac{\hbar^2}{2m r_0^2}$ であり，これを第 2 式に代入して $r_0$ と $E_0$ を求めます。

$$
\begin{aligned}
\frac{q^2}{4\pi\epsilon_0 r_0}\frac{2mr_0^2}{\hbar^2}&=2\\
r_0&=\frac{4\pi\epsilon_0\hbar^2}{mq^2}\\
E_0&=\frac{\hbar^2}{2mr_0^2}\\
&=\frac{mq^4}{32\pi^2\epsilon_0^2\hbar^2}
\end{aligned}
$$

したがって，

$$
\finalanswer{r_0 = \frac{4\pi\epsilon_0 \hbar^2}{m q^2}, \qquad E_0 = \frac{m q^4}{32\pi^2 \epsilon_0^2 \hbar^2}}
$$

### (2)
$\psi(\rho) = c e^{-\rho}$ に対して $\dfrac{\mathrm{d}\psi}{\mathrm{d}\rho} = -\psi$，$\dfrac{\mathrm{d}^2\psi}{\mathrm{d}\rho^2} = \psi$ です。これを (1) 式の左辺に代入すると，

$$
\left(1 - \frac{2}{\rho} + \frac{2}{\rho}\right)\psi = \psi
$$

となります。よって $\varepsilon = 1$ であり，基底状態のエネルギーは $E = -E_0$ です。

次に，$\langle r^2 \rangle$ を球座標の体積要素 $\mathrm{d}^3 r = 4\pi r^2\,\mathrm{d}r$ を用いて計算します。ガンマ関数の公式 $\displaystyle\int_0^\infty \rho^n e^{-2\rho}\,\mathrm{d}\rho = \dfrac{n!}{2^{n+1}}$ を用いると，

$$
\begin{aligned}
\langle r^2 \rangle &= \frac{\int_0^\infty r^2 |\psi(r)|^2 \cdot 4\pi r^2\,\mathrm{d}r}{\int_0^\infty |\psi(r)|^2 \cdot 4\pi r^2\,\mathrm{d}r} \\
&= r_0^2\,\frac{\int_0^\infty \rho^4 e^{-2\rho}\,\mathrm{d}\rho}{\int_0^\infty \rho^2 e^{-2\rho}\,\mathrm{d}\rho} \\
 &= r_0^2\,\frac{4!/2^5}{2!/2^3} \\
&= r_0^2\,\frac{24/32}{2/8} \\
&= 3r_0^2
\end{aligned}
$$

となります。したがって，$\sqrt{\langle r^2 \rangle} = \sqrt{3}\,r_0$ です。

$$
\finalanswer{E = -E_0, \qquad \sqrt{\langle r^2 \rangle} = \sqrt{3}\,r_0}
$$

### (3)
正準交換関係 $[x, p_x] = [y, p_y] = [z, p_z] = i\hbar$ および異なる方向成分の可換性を用いて計算します。まず $[p_1, p_2]$ は次のようになります。

$$
\begin{aligned}
[p_1, p_2] &= \left[p_x - \frac{qBy}{2},\; p_y + \frac{qBx}{2}\right] \\
&= \frac{qB}{2}[p_x, x] - \frac{qB}{2}[y, p_y] \\
 &= \frac{qB}{2}(-i\hbar) - \frac{qB}{2}(i\hbar) \\
&= -i\hbar qB
\end{aligned}
$$

また，$p_z$ は $x, y, p_x, p_y$ のいずれとも可換であるため，$[p_1, p_z] = 0$，$[p_2, p_z] = 0$ です。

$$
\finalanswer{[p_1, p_2] = -i\hbar qB, \qquad [p_1, p_z] = 0, \qquad [p_2, p_z] = 0}
$$

### (4)
$X = k p_2$，$P = p_1$ が正準交換関係 $[X, P] = i\hbar$ を満たす条件を求めます。(3) の結果 $[p_2, p_1] = i\hbar qB$ より，

$$
\begin{aligned}
[X,P]&=k[p_2,p_1]\\
&=i\hbar kqB
\end{aligned}
\qquad
\begin{aligned}
kqB&=1\\
k&=\frac{1}{qB}
\end{aligned}
$$

が得られます。ここで $qB\neq0$ とします。このとき $p_1 = P$，$p_2 = qB X$ であり，ハミルトニアン (2) の $(x, y)$ 方向に関する部分 $H_{xy}$ は次のように書き換えられます。

$$
\begin{aligned}
H_{xy} &= \frac{1}{2m}\left(p_1^2 + p_2^2\right) \\
&= \frac{P^2}{2m} + \frac{q^2 B^2}{2m}X^2 \\
&= \frac{P^2}{2m} + \frac{1}{2}m\omega^2 X^2
\end{aligned}
$$

ここで $\omega = \dfrac{|qB|}{m}$ とおきました。$(X, P)$ は正準交換関係 $[X, P] = i\hbar$ を満たすエルミート演算子なので，$(x, y)$ 方向の運動は質量 $m$，固有振動数 $\omega = \dfrac{|qB|}{m}$ の 1 次元調和振動子と等価です。

古典的描像では，$\omega$ は一様磁場中でローレンツ力を受けて $xy$ 面内を等速円運動する荷電粒子の角振動数を表します。この角振動数を**サイクロトロン角振動数**といいます。

$$
\finalanswer{k = \frac{1}{qB}, \qquad \omega = \frac{|qB|}{m}}
$$

### (5)
まず $P' = p_x + \dfrac{qBy}{2}$ と $P = p_1$，$X = \dfrac{1}{qB}p_2$ との交換関係を計算します。

$$
\begin{aligned}
[P', P] &= \left[p_x + \frac{qBy}{2},\; p_x - \frac{qBy}{2}\right] = 0, \\
[P', X] &= \frac{1}{qB}\left[p_x + \frac{qBy}{2},\; p_y + \frac{qBx}{2}\right] \\
&= \frac{1}{qB}\left(\frac{qB}{2}[p_x, x] + \frac{qB}{2}[y, p_y]\right)
= \frac{1}{2}(-i\hbar + i\hbar) = 0
\end{aligned}
$$

以上より，$P'$ は $X$ および $P$ のそれぞれと可換です。

次に，$x$ と $p_y$ の実係数線形結合 $X' = \alpha x + \beta p_y$（$\alpha, \beta \in \mathbb{R}$）をおきます。$x, p_y$ がエルミート演算子なので $X'$ もエルミート演算子です。$X'$ と $X, P, P'$ との交換関係はそれぞれ次のようになります。

$$
\begin{aligned}
[X', X] &= \left[\alpha x + \beta p_y,\; \frac{p_y}{qB} + \frac{x}{2}\right] = 0, \\
[X', P] &= \left[\alpha x + \beta p_y,\; p_x - \frac{qBy}{2}\right] = \alpha(i\hbar) - \beta\frac{qB}{2}(-i\hbar) = i\hbar\left(\alpha + \frac{qB}{2}\beta\right), \\
[X', P'] &= \left[\alpha x + \beta p_y,\; p_x + \frac{qBy}{2}\right] = \alpha(i\hbar) + \beta\frac{qB}{2}(-i\hbar) = i\hbar\left(\alpha - \frac{qB}{2}\beta\right)
\end{aligned}
$$

条件 $[X', P] = 0$ および $[X', P'] = i\hbar$ より，

$$
\alpha + \frac{qB}{2}\beta = 0, \qquad \alpha - \frac{qB}{2}\beta = 1
$$

が得られます。これを解くと $\alpha = \dfrac{1}{2}$，$\beta = -\dfrac{1}{qB}$ となります。したがって，

$$
\finalanswer{X' = \frac{1}{2}x - \frac{1}{qB}p_y}
$$

### (6)
(4) より，$H_{xy}$ は固有振動数 $\omega=\dfrac{|qB|}{m}$ の1次元調和振動子のハミルトニアンです。$X$ を対角化する表示で，規格化した基底状態の波動関数は次のとおりです。

$$
\begin{aligned}
\psi_0(X) &= \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega}{2\hbar}X^2\right) \\
&= \left(\frac{|qB|}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{|qB|}{2\hbar}X^2\right)
\end{aligned}
$$

さらに，(4) と (5) の定義より $X = \dfrac{1}{qB}p_y + \dfrac{1}{2}x$，$X' = \dfrac{1}{2}x - \dfrac{1}{qB}p_y$ なので，両者の和は

$$
X + X' = x \implies X = x - X'
$$

を満たします。$X$ と $X'$ は可換なので同時対角化が可能であり，$X' = a$ の固有状態では $X = x - a$ と置き換えられます。よって，基底状態の波動関数の $x$ 依存性は

$$
\psi_{0,a}(x) = \left(\frac{|qB|}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{|qB|}{2\hbar}(x - a)^2\right)
$$

と表されます。

ここで $a$ は，調和振動子の波動関数が局在する中心の $x$ 座標を表しています。古典的描像では，$m\dot{y} = p_y + \dfrac{qBx}{2}$ より $X' = x - \dfrac{m\dot{y}}{qB}$ は時間によらない保存量となり，$a$ は一様磁場中をサイクロトロン運動する荷電粒子の円軌道の中心の $x$ 座標に対応します。円軌道の中心を**案内中心**といいます。

$$
\finalanswer{\psi_0(X) = \left(\frac{|qB|}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{|qB|}{2\hbar}X^2\right)}
$$

<aside class="rigor-note" markdown>
一様磁場 $\boldsymbol{B}=(0,0,-B)$ では，案内中心の $y$ 座標を

$$
Y'\equiv\frac{P'}{qB}=\frac{p_x}{qB}+\frac{y}{2}
$$

と定義します。$m\dot{x}=p_x-qBy/2$ より，古典的には $Y'=y+\dfrac{m\dot{x}}{qB}$ となります。$(X',Y')$ の交換関係は $[X',Y']=\dfrac{i\hbar}{qB}$ です。案内中心の両座標はハミルトニアンと可換ですが，互いには可換ではありません。

各ランダウ準位は案内中心の位置の自由度に対応して巨視的に縮退します。磁気長さ $\ell_B=\sqrt{\dfrac{\hbar}{|qB|}}$ を使うと，(6) の波動関数の $x$ 依存性は $\exp\!\left(-\dfrac{(x-a)^2}{2\ell_B^2}\right)$ と表されます。
</aside>
