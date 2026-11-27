---
title: 東大理物 平成10年度 一般教育科目 物理学 第2問：定常電流と2層同心球殻導体の抵抗および境界面蓄積電荷
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 一般教育科目 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成10年度 一般教育科目 物理学 第2問：定常電流と2層同心球殻導体の抵抗および境界面蓄積電荷

## 問題

(1) 図のように断面積 $S$，長さ $L$ の円柱導体に一様な定常電流 $I$ が流れている。その抵抗 $R$ は抵抗率 $\rho$ により $R = \rho L/S$ と表せる。この導体中の電流密度 $j$（電流に垂直な単位断面積当たりの電流）はいくらか。また，導体中の電場 $E$ と電流密度 $j$ との関係を導け。

<figure class="problem-figure" markdown>
![断面積S・長さLの円柱導体を流れる定常電流I](../../../docs/assets/figures/pastexam-todai-ributsu/H10_ippan_butsuri_2-p1-light.svg#only-light){ loading=lazy }
![断面積S・長さLの円柱導体を流れる定常電流I](../../../docs/assets/figures/pastexam-todai-ributsu/H10_ippan_butsuri_2-p1-dark.svg#only-dark){ loading=lazy }
</figure>

(2) 球形電極（半径 $a$）と球殻電極（半径 $b$）が同心に配置されており，それらの間は半径 $c$ のところで2層の球殻に分けられ（$a < c < b$），内側に抵抗率 $\rho_1$ の導体，外側に抵抗率 $\rho_2$ の導体が詰められている（下に断面図を示す）。電極間に電圧をかけ，一様な定常電流 $I$ を流す。中心からの距離を $r$ として，以下の問に答えよ。なお，実際上，球に細い穴をあけ中心の電極に導線をつなぐが，その穴と導線の影響は無視できるものとする。また，電極，導線の抵抗率も十分小さく無視できるものとする。

<figure class="problem-figure" markdown>
![2層同心球殻導体の断面図](../../../docs/assets/figures/pastexam-todai-ributsu/H10_ippan_butsuri_2-p2-light.svg#only-light){ loading=lazy }
![2層同心球殻導体の断面図](../../../docs/assets/figures/pastexam-todai-ributsu/H10_ippan_butsuri_2-p2-dark.svg#only-dark){ loading=lazy }
</figure>

(a) 電流密度 $j$，電極間の電場の強さ $E$ を $r$ の関数で表せ。

(b) 電極間の電圧 $V$，抵抗 $R$ を求めよ。

(c) 中心の電極表面にたまっている全電荷 $Q$ を求めよ。

(d) 異なる導体の境界面にたまっている全電荷 $Q'$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 一般教育科目 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
(1) では巨視的なオームの法則 $V = RI$ から微分形のオームの法則 $E = \rho j$ を導きます。

(2) では球対称な2層導体に定常電流 $I$ が流れるとき，任意の同心球面を通過する全電流が一定であることから $j(r)$ と $E(r)$ を求め，電場の動径積分で電圧 $V$ と抵抗 $R$ を計算します。さらに内側の電極表面と2導体の境界面 $r = c$ での電場の不連続にガウスの法則を用い，蓄積電荷 $Q$ および $Q'$ を導出します。
</div>

### (1)

一様な定常電流 $I$ が断面積 $S$ の円柱導体を流れているため，電流密度 $j$ は定義より次の通りです。

$$
j = \frac{I}{S}
$$

導体の両端の電位差を $V$ とすると，一様な導体内部では電場の強さ $E$ は一定であり $V = EL$ です。オームの法則 $V = RI$ に $R = \dfrac{\rho L}{S}$ を代入して整理します。

$$
\begin{aligned}
EL &= \frac{\rho L}{S}I \\
E &= \rho\frac{I}{S} \\
E &= \rho j
\end{aligned}
$$

$$
\finalanswer{j = \frac{I}{S},\qquad E = \rho j}
$$

### (2)(a)

定常電流 $I$ は中心の球形電極（半径 $a$）と外側の球殻電極（半径 $b$）の間を球対称に流れます。以下では中心から外向きを正として計算します。

中心からの距離 $r$（$a < r < b$）にある半径 $r$ の同心球面の表面積は $4\pi r^2$ です。電荷の保存則より，定常状態ではどの同心球面を通過する全電流も $I$ に等しいため，電流密度 $j(r)$ は次のようになります。

$$
j(r) = \frac{I}{4\pi r^2} \qquad (a < r < b)
$$

(1) で導いた関係 $E = \rho j$ を各層に用いると，電場の強さ $E(r)$ は内側の層 $a < r < c$ で $E(r) = \dfrac{\rho_1 I}{4\pi r^2}$，外側の層 $c < r < b$ で $E(r) = \dfrac{\rho_2 I}{4\pi r^2}$ と求まります。

$$
\finalanswer{j(r) = \frac{I}{4\pi r^2},\qquad E(r) =
\begin{cases}
\dfrac{\rho_1 I}{4\pi r^2} & (a < r < c) \\[10pt]
\dfrac{\rho_2 I}{4\pi r^2} & (c < r < b)
\end{cases}}
$$

### (2)(b)

電極間の電圧 $V$ は，中心電極（$r = a$）から外側電極（$r = b$）まで電場 $E(r)$ を動径方向に積分して求めます。

$$
\begin{aligned}
V &= \int_a^b E(r)\,\mathrm{d}r \\
&= \int_a^c \frac{\rho_1 I}{4\pi r^2}\,\mathrm{d}r + \int_c^b \frac{\rho_2 I}{4\pi r^2}\,\mathrm{d}r \\
&= \frac{\rho_1 I}{4\pi}\left[-\frac{1}{r}\right]_a^c + \frac{\rho_2 I}{4\pi}\left[-\frac{1}{r}\right]_c^b \\
&= \frac{I}{4\pi}\left\{\rho_1\left(\frac{1}{a} - \frac{1}{c}\right) + \rho_2\left(\frac{1}{c} - \frac{1}{b}\right)\right\}
\end{aligned}
$$

したがって電極間の抵抗 $R = \dfrac{V}{I}$ は次の通りです。

$$
R = \frac{1}{4\pi}\left\{\rho_1\left(\frac{1}{a} - \frac{1}{c}\right) + \rho_2\left(\frac{1}{c} - \frac{1}{b}\right)\right\}
$$

$$
\finalanswer{V = \frac{I}{4\pi}\left\{\rho_1\left(\frac{1}{a} - \frac{1}{c}\right) + \rho_2\left(\frac{1}{c} - \frac{1}{b}\right)\right\},\qquad R = \frac{1}{4\pi}\left\{\rho_1\left(\frac{1}{a} - \frac{1}{c}\right) + \rho_2\left(\frac{1}{c} - \frac{1}{b}\right)\right\}}
$$

### (2)(c)

各導体の誘電率を真空の誘電率 $\varepsilon_0$ とします。電極内部では抵抗率が十分小さいため電場は $E = 0$ であり，電荷は電極表面にのみ分布します。中心電極をわずかに外側から囲む半径 $r = a + 0$ の球面にガウスの法則を用います。

$$
4\pi a^2 E(a + 0) = \frac{Q}{\varepsilon_0}
$$

ここに (a) で求めた $E(a + 0) = \dfrac{\rho_1 I}{4\pi a^2}$ を代入します。

$$
\begin{aligned}
Q &= 4\pi \varepsilon_0 a^2 \cdot \frac{\rho_1 I}{4\pi a^2} \\
&= \varepsilon_0 \rho_1 I
\end{aligned}
$$

なお電流 $I$ の向きが外側から中心へ向かう場合は符号が反転して $-\varepsilon_0 \rho_1 I$ となります。

$$
\finalanswer{Q = \varepsilon_0 \rho_1 I}
$$

### (2)(d)

異なる導体の境界面 $r = c$ を挟む半径 $c - 0$ と半径 $c + 0$ の2つの同心球面からなる薄い球殻領域にガウスの法則を用います。境界面の外側と内側での電束の差が境界面にたまった全電荷 $Q'$ を $\varepsilon_0$ で割ったものに等しくなります。

$$
\frac{Q'}{\varepsilon_0} = 4\pi c^2 E(c + 0) - 4\pi c^2 E(c - 0)
$$

ここに $E(c + 0) = \dfrac{\rho_2 I}{4\pi c^2}$ および $E(c - 0) = \dfrac{\rho_1 I}{4\pi c^2}$ を代入します。

$$
\begin{aligned}
Q' &= \varepsilon_0 \left(4\pi c^2 \frac{\rho_2 I}{4\pi c^2} - 4\pi c^2 \frac{\rho_1 I}{4\pi c^2}\right) \\
&= \varepsilon_0 (\rho_2 - \rho_1)I
\end{aligned}
$$

なお，導体内部の $a < r < c$ と $c < r < b$ では $\nabla\cdot\mathbf{j} = 0$ より $\nabla\cdot\mathbf{E} = 0$ であるため体積電荷密度は $0$ であり，電荷は境界面 $r = c$ と電極表面にのみ蓄積します。また外側電極の内表面 $r = b$ には $-\varepsilon_0\rho_2 I$ の電荷がたまり，系全体の電荷の総和は $Q + Q' + (-\varepsilon_0\rho_2 I) = 0$ となります。

$$
\finalanswer{Q' = \varepsilon_0 (\rho_2 - \rho_1)I}
$$

<div class="rigor-note" markdown>
各導体の誘電率が $\varepsilon_1, \varepsilon_2$ として区別されている場合は，ガウスの法則は電束密度 $\mathbf{D} = \varepsilon\mathbf{E}$ に対して用いられるため，自由電荷は $Q = \varepsilon_1 \rho_1 I$，$Q' = (\varepsilon_2 \rho_2 - \varepsilon_1 \rho_1)I$ となります。本問では誘電率の指定がないため，標準的に両導体とも真空の誘電率 $\varepsilon_0$ として求めました。
</div>
