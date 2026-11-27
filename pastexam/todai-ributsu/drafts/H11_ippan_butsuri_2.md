---
title: 東大理物 平成11年度 一般教育科目 物理学 第2問：一様帯電球の電場・静電ポテンシャルと静電エネルギー
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 一般教育科目 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成11年度 一般教育科目 物理学 第2問：一様帯電球の電場・静電ポテンシャルと静電エネルギー

## 問題

半径 $a$ の球内に電荷が一様に分布している。球の外側には電荷はないものとする。球内の電荷分布を $\rho$（$> 0$）として，以下の問いに答えよ。
{: .problem-lead }

(1) 球の内外の電場の大きさ $E(r)$ を，球の中心からの距離 $r$ の関数として求め，そのグラフを描け。

(2) 同じく球の内外の静電ポテンシャル $\phi(r)$ を $r$ の関数として求め，そのグラフを描け。ただし，無限遠での静電ポテンシャルを $0$ とすること。

(3) 無限遠から少しずつ電荷を持ってきてこのような電荷分布をつくるのに要する仕事 $W_1$ を計算せよ。

(4) 球内および球外の空間の静電場のエネルギーをそれぞれ計算し，全空間の静電場のエネルギー $W_2$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 一般教育科目 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
球対称な電荷分布に対してガウスの法則を用い，球の内外での電場 $E(r)$ を求めます。次に電場を無限遠から線積分して静電ポテンシャル $\phi(r)$ を導出し，両者のグラフを描きます。

後半では，球殻を薄い層ごとに積み上げて帯電球を形成するときの仕事 $W_1$ と，静電場のエネルギー密度 $\dfrac{1}{2}\varepsilon_0 E^2$ を球内・球外それぞれで体積積分した静電エネルギー $W_2$ を計算し，両者が一致することを確認します。
</div>

### (1)

真空の誘電率を $\varepsilon_0$ とします。電荷分布は球対称であるため，電場は中心から外向きの動径方向のみを向き，その大きさ $E(r)$ は中心からの距離 $r$ だけに依存します。

中心が球の中心と一致する半径 $r$ の球面 $S_r$ にガウスの法則を用います。

$$
4\pi r^2 E(r) = \frac{Q_{\mathrm{in}}(r)}{\varepsilon_0}
$$

ここで $Q_{\mathrm{in}}(r)$ は半径 $r$ の球の内部に含まれる総電荷です。球の内部と外部に分けて計算します。

まず球内（$0 \le r \le a$）では $Q_{\mathrm{in}}(r) = \dfrac{4}{3}\pi r^3 \rho$ なので，次式が成り立ちます。

$$
\begin{aligned}
4\pi r^2 E(r) &= \frac{4\pi r^3 \rho}{3\varepsilon_0} \\
E(r) &= \frac{\rho}{3\varepsilon_0}r
\end{aligned}
$$

次に球外（$r > a$）では球全体の総電荷 $Q = \dfrac{4}{3}\pi a^3 \rho$ が含まれるため，次式が成り立ちます。

$$
\begin{aligned}
4\pi r^2 E(r) &= \frac{4\pi a^3 \rho}{3\varepsilon_0} \\
E(r) &= \frac{\rho a^3}{3\varepsilon_0 r^2}
\end{aligned}
$$

境界 $r = a$ において電場は連続であり，最大値 $E(a) = \dfrac{\rho a}{3\varepsilon_0}$ をとります。$E(r)$ のグラフは (2) の $\phi(r)$ と並べて下に示します。

$$
\finalanswer{E(r) =
\begin{cases}
\dfrac{\rho}{3\varepsilon_0}r & (0 \le r \le a) \\[10pt]
\dfrac{\rho a^3}{3\varepsilon_0 r^2} & (r > a)
\end{cases}}
$$

### (2)

無限遠を基準 $\phi(\infty) = 0$ とすると，距離 $r$ での静電ポテンシャル $\phi(r)$ は次式で与えられます。

$$
\phi(r) = \int_r^\infty E(r')\,\mathrm{d}r'
$$

まず球外（$r \ge a$）で積分を計算します。

$$
\begin{aligned}
\phi(r) &= \int_r^\infty \frac{\rho a^3}{3\varepsilon_0 r'^2}\,\mathrm{d}r' \\
&= \frac{\rho a^3}{3\varepsilon_0}\left[-\frac{1}{r'}\right]_r^\infty \\
&= \frac{\rho a^3}{3\varepsilon_0 r}
\end{aligned}
$$

次に球内（$0 \le r \le a$）では積分区間を $[r, a]$ と $[a, \infty)$ に分けます。

$$
\begin{aligned}
\phi(r) &= \int_r^a \frac{\rho}{3\varepsilon_0}r'\,\mathrm{d}r' + \phi(a) \\
&= \frac{\rho}{6\varepsilon_0}(a^2 - r^2) + \frac{\rho a^2}{3\varepsilon_0} \\
&= \frac{\rho}{6\varepsilon_0}(3a^2 - r^2)
\end{aligned}
$$

中心 $r = 0$ で最大値 $\phi(0) = \dfrac{\rho a^2}{2\varepsilon_0}$ をとり，表面 $r = a$ で $\phi(a) = \dfrac{\rho a^2}{3\varepsilon_0}$ に滑らかにつながります。

(1) の $E(r)$ と (2) の $\phi(r)$ のグラフは次の通りです。

![一様帯電球内外の電場E(r)と静電ポテンシャルphi(r)のグラフ](../../../docs/assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_2-s-light.svg#only-light){ loading=lazy }
![一様帯電球内外の電場E(r)と静電ポテンシャルphi(r)のグラフ](../../../docs/assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_2-s-dark.svg#only-dark){ loading=lazy }

$$
\finalanswer{\phi(r) =
\begin{cases}
\dfrac{\rho}{6\varepsilon_0}(3a^2 - r^2) & (0 \le r \le a) \\[10pt]
\dfrac{\rho a^3}{3\varepsilon_0 r} & (r > a)
\end{cases}}
$$

### (3)

すでに半径 $r$ まで電荷密度 $\rho$ の一様帯電球が形成されている状態を考えます。この球に含まれる電荷は $q(r) = \dfrac{4}{3}\pi r^3 \rho$ であり，その表面（距離 $r$）における静電ポテンシャルは次の通りです。

$$
\begin{aligned}
\phi_{\mathrm{surf}}(r) &= \frac{q(r)}{4\pi\varepsilon_0 r} \\
&= \frac{\rho r^2}{3\varepsilon_0}
\end{aligned}
$$

ここに無限遠から電荷 $\mathrm{d}q = 4\pi r^2 \rho\,\mathrm{d}r$ を運んで厚さ $\mathrm{d}r$ の薄い球殻を貼り付けるのに要する仕事 $\mathrm{d}W_1$ を計算します。

$$
\begin{aligned}
\mathrm{d}W_1 &= \phi_{\mathrm{surf}}(r)\,\mathrm{d}q \\
&= \frac{\rho r^2}{3\varepsilon_0}\cdot 4\pi r^2 \rho\,\mathrm{d}r \\
&= \frac{4\pi\rho^2}{3\varepsilon_0}r^4\,\mathrm{d}r
\end{aligned}
$$

これを $r = 0$ から $r = a$ まで積分して全体の仕事 $W_1$ を求めます。

$$
\begin{aligned}
W_1 &= \int_0^a \frac{4\pi\rho^2}{3\varepsilon_0}r^4\,\mathrm{d}r \\
&= \frac{4\pi\rho^2}{3\varepsilon_0}\cdot\frac{a^5}{5} \\
&= \frac{4\pi\rho^2 a^5}{15\varepsilon_0}
\end{aligned}
$$

なお，総電荷 $Q = \dfrac{4}{3}\pi a^3 \rho$ を用いると $W_1 = \dfrac{3Q^2}{20\pi\varepsilon_0 a}$ とも表されます。

$$
\finalanswer{W_1 = \frac{4\pi\rho^2 a^5}{15\varepsilon_0}}
$$

### (4)

静電場のエネルギー密度は $u = \dfrac{1}{2}\varepsilon_0 \{E(r)\}^2$ です。球内（$0 \le r \le a$）の静電場のエネルギー $W_{\mathrm{in}}$ を体積積分で計算します。

$$
\begin{aligned}
W_{\mathrm{in}} &= \int_0^a \frac{1}{2}\varepsilon_0 \left(\frac{\rho r}{3\varepsilon_0}\right)^2 \cdot 4\pi r^2\,\mathrm{d}r \\
&= \frac{2\pi\rho^2}{9\varepsilon_0}\int_0^a r^4\,\mathrm{d}r \\
&= \frac{2\pi\rho^2 a^5}{45\varepsilon_0}
\end{aligned}
$$

次に球外（$r > a$）の静電場のエネルギー $W_{\mathrm{out}}$ を計算します。

$$
\begin{aligned}
W_{\mathrm{out}} &= \int_a^\infty \frac{1}{2}\varepsilon_0 \left(\frac{\rho a^3}{3\varepsilon_0 r^2}\right)^2 \cdot 4\pi r^2\,\mathrm{d}r \\
&= \frac{2\pi\rho^2 a^6}{9\varepsilon_0}\int_a^\infty \frac{1}{r^2}\,\mathrm{d}r \\
&= \frac{2\pi\rho^2 a^6}{9\varepsilon_0}\cdot\frac{1}{a} \\
&= \frac{2\pi\rho^2 a^5}{9\varepsilon_0}
\end{aligned}
$$

したがって，全空間の静電場のエネルギー $W_2 = W_{\mathrm{in}} + W_{\mathrm{out}}$ は次の通りです。

$$
\begin{aligned}
W_2 &= \frac{2\pi\rho^2 a^5}{45\varepsilon_0} + \frac{10\pi\rho^2 a^5}{45\varepsilon_0} \\
&= \frac{12\pi\rho^2 a^5}{45\varepsilon_0} \\
&= \frac{4\pi\rho^2 a^5}{15\varepsilon_0}
\end{aligned}
$$

全空間の静電場のエネルギー $W_2$ は (3) で求めた電荷分布をつくる仕事 $W_1$ に一致します。

$$
\finalanswer{W_{\mathrm{in}} = \frac{2\pi\rho^2 a^5}{45\varepsilon_0},\qquad W_{\mathrm{out}} = \frac{2\pi\rho^2 a^5}{9\varepsilon_0},\qquad W_2 = \frac{4\pi\rho^2 a^5}{15\varepsilon_0}}
$$
