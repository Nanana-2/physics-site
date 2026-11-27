---
title: 東大理物 平成12年度 一般教育科目 数学 第1問：2次元保存ベクトル場とスカラーポテンシャル
tags:
  - 院試過去問
  - 東大理物
  - ベクトル解析
  - 微積分
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 一般教育科目 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成12年度 一般教育科目 数学 第1問：2次元保存ベクトル場とスカラーポテンシャル

## 問題

2次元空間におけるベクトル場 $\mathbf{E}(x, y)$ の各成分 $E_x(x, y), E_y(x, y)$ は，必要な階数まで微分可能であるとして，以下の設問に答えよ。
{: .problem-lead }

(1) $\dfrac{\partial E_y}{\partial x} - \dfrac{\partial E_x}{\partial y} = 0$ のとき，あるスカラー場 $\varphi(x, y)$ が存在して，

$$
\mathbf{E} = \operatorname{grad}\varphi = \left(\frac{\partial\varphi}{\partial x}, \frac{\partial\varphi}{\partial y}\right)
$$

とあらわせることを示せ。

但し，次の関係を用いて良い。

$$
\iint_S \left(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\right)\mathrm{d}x\,\mathrm{d}y = \oint_C \mathbf{E}\cdot\mathrm{d}\mathbf{r} = \oint_C (E_x\,\mathrm{d}x + E_y\,\mathrm{d}y)
$$

ここで $S$ は閉じた道 $C$ で囲まれる領域の内部であり，線積分の向きは反時計回りである。

<figure class="problem-figure" markdown>
![閉曲線Cとその内部の領域S](../../assets/figures/pastexam-todai-ributsu/H12_ippan_sugaku_1-p-light.svg#only-light){ loading=lazy }
![閉曲線Cとその内部の領域S](../../assets/figures/pastexam-todai-ributsu/H12_ippan_sugaku_1-p-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">反時計回りの閉曲線 $C$ とその内部の領域 $S$。</figcaption>
</figure>

(2) $\mathbf{E} = (x^2 - y^2, -2xy)$ のとき $\dfrac{\partial E_y}{\partial x} - \dfrac{\partial E_x}{\partial y} = 0$ となることを示し，設問 (1) における $\varphi(x, y)$ を求めよ。

(3) 点 $(x, y)$ における接線が，設問 (2) の $\mathbf{E}(x, y)$ と平行になる曲線群 $\psi(x, y) = a$（$a =$ 定数）を決定せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 一般教育科目 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
グリーンの定理により $\dfrac{\partial E_y}{\partial x} - \dfrac{\partial E_x}{\partial y} = 0$ であれば任意の閉曲線に沿う線積分が $0$ になるため，固定した始点から任意の点 $(x, y)$ までの線積分は経路によらない一価関数 $\varphi(x, y)$ を定めます。この $\varphi$ を座標軸に沿った微小増分で偏微分すると $\mathbf{E} = \operatorname{grad}\varphi$ が得られます。

後半では，接線方向が $\mathbf{E}$ に平行という条件を1階微分方程式 $E_y\,\mathrm{d}x - E_x\,\mathrm{d}y = 0$ に書き直します。この場では $\dfrac{\partial E_x}{\partial x} + \dfrac{\partial E_y}{\partial y} = 0$ も成り立つため完全微分方程式となり，そのまま積分して曲線群 $\psi(x, y) = a$ を求めることができます。
</div>

### (1)

条件 $\dfrac{\partial E_y}{\partial x} - \dfrac{\partial E_x}{\partial y} = 0$ が2次元平面全体で成り立つので，与えられたグリーンの定理から，任意の閉曲線 $C$ に沿う線積分は $0$ になります。

$$
\begin{aligned}
\oint_C \mathbf{E}\cdot\mathrm{d}\mathbf{r} &= \iint_S \left(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\right)\mathrm{d}x\,\mathrm{d}y \\
&= 0
\end{aligned}
$$

ここで平面上の基準点 $P_0(x_0, y_0)$ を固定し，$P_0$ から任意の点 $P(x, y)$ に至る2つの任意の経路 $C_1, C_2$ を考えます。$C_1$ に沿って $P_0$ から $P$ へ進み，$C_2$ を逆向きにたどって $P$ から $P_0$ へ戻る閉曲線 $C = C_1 - C_2$ に上式を用いると次が成り立ちます。

$$
\begin{aligned}
\int_{C_1} \mathbf{E}\cdot\mathrm{d}\mathbf{r} - \int_{C_2} \mathbf{E}\cdot\mathrm{d}\mathbf{r} &= \oint_C \mathbf{E}\cdot\mathrm{d}\mathbf{r} \\
&= 0
\end{aligned}
$$

よって $\int_{C_1}\mathbf{E}\cdot\mathrm{d}\mathbf{r} = \int_{C_2}\mathbf{E}\cdot\mathrm{d}\mathbf{r}$ となり，$P_0$ から $P(x, y)$ への線積分は経路によらず終点 $(x, y)$ のみで定まります。そこでスカラー場 $\varphi(x, y)$ を次で定義します。

$$
\varphi(x, y) = \int_{(x_0, y_0)}^{(x, y)} \bigl(E_x(x', y')\,\mathrm{d}x' + E_y(x', y')\,\mathrm{d}y'\bigr)
$$

この $\varphi(x, y)$ の偏導関数を求めます。点 $(x, y)$ から $x$ 軸に平行に $(x + \Delta x, y)$ へ進む線分を経路の末尾に付け加えると，経路独立性より $\varphi(x + \Delta x, y) - \varphi(x, y)$ はその線分上の積分だけで表すことができます。この線分上では $y' = y$ が一定で $\mathrm{d}y' = 0$ です。

$$
\begin{aligned}
\frac{\partial\varphi}{\partial x} &= \lim_{\Delta x \to 0}\frac{\varphi(x + \Delta x, y) - \varphi(x, y)}{\Delta x} \\
&= \lim_{\Delta x \to 0}\frac{1}{\Delta x}\int_{x}^{x + \Delta x} E_x(x', y)\,\mathrm{d}x' \\
&= E_x(x, y)
\end{aligned}
$$

同様に，$(x, y)$ から $y$ 軸に平行に $(x, y + \Delta y)$ へ進む線分を用いると $x' = x$ が一定で $\mathrm{d}x' = 0$ なので次が成り立ちます。

$$
\begin{aligned}
\frac{\partial\varphi}{\partial y} &= \lim_{\Delta y \to 0}\frac{\varphi(x, y + \Delta y) - \varphi(x, y)}{\Delta y} \\
&= \lim_{\Delta y \to 0}\frac{1}{\Delta y}\int_{y}^{y + \Delta y} E_y(x, y')\,\mathrm{d}y' \\
&= E_y(x, y)
\end{aligned}
$$

以上より，$\mathbf{E} = \left(\dfrac{\partial\varphi}{\partial x}, \dfrac{\partial\varphi}{\partial y}\right) = \operatorname{grad}\varphi$ を満たすスカラー場 $\varphi(x, y)$ の存在が成り立ちます。

### (2)

$E_x(x, y) = x^2 - y^2$，$E_y(x, y) = -2xy$ について偏微分を計算します。

$$
\begin{aligned}
\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} &= \frac{\partial}{\partial x}(-2xy) - \frac{\partial}{\partial y}(x^2 - y^2) \\
&= (-2y) - (-2y) \\
&= 0
\end{aligned}
$$

よって条件 $\dfrac{\partial E_y}{\partial x} - \dfrac{\partial E_x}{\partial y} = 0$ が成り立ちます。

次に $\varphi(x, y)$ を求めます。$\dfrac{\partial\varphi}{\partial x} = x^2 - y^2$ を $x$ について積分します。ここで $f(y)$ は $y$ のみの任意関数です。

$$
\varphi(x, y) = \frac{1}{3}x^3 - xy^2 + f(y)
$$

これを $y$ で偏微分し，$\dfrac{\partial\varphi}{\partial y} = -2xy$ と比較します。

$$
\begin{aligned}
\frac{\partial\varphi}{\partial y} &= -2xy + f'(y) \\
-2xy + f'(y) &= -2xy
\end{aligned}
$$

よって $f'(y) = 0$ となり，$f(y) = C$（$C$ は任意定数）です。したがって，$\varphi(x, y)$ は任意定数 $C$ を用いて次のように表されます。

$$
\finalanswer{\varphi(x, y) = \frac{1}{3}x^3 - xy^2 + C}
$$

### (3)

曲線 $\psi(x, y) = a$ 上の微小変位 $(\mathrm{d}x, \mathrm{d}y)$ は接線方向を向き，全微分は $\dfrac{\partial\psi}{\partial x}\mathrm{d}x + \dfrac{\partial\psi}{\partial y}\mathrm{d}y = 0$ を満たします。接線が $\mathbf{E} = (x^2 - y^2, -2xy)$ に平行である条件は次になります。

$$
\begin{aligned}
\frac{\mathrm{d}x}{x^2 - y^2} &= \frac{\mathrm{d}y}{-2xy} \\
2xy\,\mathrm{d}x + (x^2 - y^2)\,\mathrm{d}y &= 0
\end{aligned}
$$

ここで $P(x, y) = 2xy$，$Q(x, y) = x^2 - y^2$ とおいて完全微分条件を確かめます。

$$
\begin{aligned}
\frac{\partial P}{\partial y} &= 2x \\
\frac{\partial Q}{\partial x} &= 2x
\end{aligned}
$$

$\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}$ が成り立つため，左辺は完全微分 $\mathrm{d}\psi$ になっています。$\dfrac{\partial\psi}{\partial x} = 2xy$ を $x$ で積分します。ここで $g(y)$ は $y$ のみの関数です。

$$
\psi(x, y) = x^2 y + g(y)
$$

これを $y$ で偏微分し，$\dfrac{\partial\psi}{\partial y} = x^2 - y^2$ と比べます。

$$
\begin{aligned}
x^2 + g'(y) &= x^2 - y^2 \\
g'(y) &= -y^2
\end{aligned}
$$

積分定数を $a$ に吸収させると $g(y) = -\dfrac{1}{3}y^3$ となります。したがって，定数 $a$ を用いた曲線群 $\psi(x, y) = a$ は次の通りです。

$$
\finalanswer{\psi(x, y) = x^2 y - \frac{1}{3}y^3 = a}
$$

<aside class="rigor-note" markdown>
(2) の $\varphi(x, y) = \dfrac{1}{3}x^3 - xy^2$ と (3) の $\psi(x, y) = x^2 y - \dfrac{1}{3}y^3$ は，複素変数 $z = x + iy$ に対する正則関数 $\dfrac{1}{3}z^3 = \left(\dfrac{1}{3}x^3 - xy^2\right) + i\left(x^2 y - \dfrac{1}{3}y^3\right)$ の実部と虚部になっています。そのためコーシー・リーマンの方程式から $\operatorname{grad}\varphi\cdot\operatorname{grad}\psi = 0$ が成り立ち，等ポテンシャル線 $\varphi(x, y) = \text{const.}$ と力線 $\psi(x, y) = a$ は至るところ直交します。
</aside>
