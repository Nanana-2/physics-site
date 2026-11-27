---
title: 東大理物 平成8年度 一般教育科目 数学 第1問：非線形振動子の摂動展開と永年項の出現
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 一般教育科目 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成8年度 一般教育科目 数学 第1問：非線形振動子の摂動展開と永年項の出現

## 問題

時間 $t$ の関数 $y(t)$ に関する非線形常微分方程式

$$
\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} + y = \varepsilon y^3
$$

を，$t = 0$ における初期条件

$$
y = 1, \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = 0
$$

のもとで考察する。ただし，$\varepsilon$ は微小な正の定数とする。必要なら，$i$ を虚数単位として，恒等式

$$
(\cos\theta + i\sin\theta)^3 = \cos 3\theta + i\sin 3\theta
$$

を用いて，以下の設問に答えよ。
{: .problem-lead }

(a) $y$ を $\varepsilon$ に関し，

$$
y(t; \varepsilon) = \sum_{n=0}^{\infty} \varepsilon^n y_n(t)
$$

と展開するとき，$y_0$，$y_1$ に対する方程式および初期条件を求めよ。

(b) 前問の各方程式を解き，$y_0$，$y_1$ を求めよ。

(c) 前問の結果より，この展開にもとづく解の適否を，$t$ が大きくなった場合について論ぜよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 一般教育科目 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ダフィング型の非線形振動子に対する正則摂動展開の計算と，その破綻の原因である永年項を扱う典型問題です。$\varepsilon$ のべきごとに微分方程式と初期条件を分離すると，1次の項 $y_1(t)$ の右辺に固有角振動数 $1$ と共鳴する $\cos t$ 項が現れ，時間に比例して発散する $t\sin t$ 項が生じます。元の非線形方程式のエネルギー保存則から厳密解の有界性を示し，摂動展開が $t \gtrsim 1/\varepsilon$ で破綻する理由を非線形による振動数シフトと結びつけて論じます。
</div>

### (a)

摂動展開 $y(t; \varepsilon) = y_0(t) + \varepsilon y_1(t) + \varepsilon^2 y_2(t) + \cdots$ を微分方程式の両辺に代入し，$\varepsilon$ のべきで整理します。

$$
(y_0'' + y_0) + \varepsilon (y_1'' + y_1) + O(\varepsilon^2) = \varepsilon y_0^3 + O(\varepsilon^2)
$$

これが微小な $\varepsilon$ に対して恒等的に成り立つため，$\varepsilon^0$ と $\varepsilon^1$ の係数をそれぞれ比較すると，$y_0(t)$ と $y_1(t)$ に対する微分方程式が得られます。

$$
\begin{aligned}
\frac{\mathrm{d}^2 y_0}{\mathrm{d}t^2} + y_0 &= 0 \\
\frac{\mathrm{d}^2 y_1}{\mathrm{d}t^2} + y_1 &= y_0^3
\end{aligned}
$$

同様に，$t = 0$ における初期条件 $y(0; \varepsilon) = 1$，$y'(0; \varepsilon) = 0$ に摂動展開を代入して $\varepsilon$ の各次の係数を比較します。

$$
\begin{aligned}
y_0(0) + \varepsilon y_1(0) + O(\varepsilon^2) &= 1 \\
y_0'(0) + \varepsilon y_1'(0) + O(\varepsilon^2) &= 0
\end{aligned}
$$

これより，$y_0$ と $y_1$ の初期条件が次のように定まります。

$$
\finalanswer{\begin{aligned}
y_0'' + y_0 &= 0,\quad y_0(0) = 1,\ y_0'(0) = 0 \\
y_1'' + y_1 &= y_0^3,\quad y_1(0) = 0,\ y_1'(0) = 0
\end{aligned}}
$$

### (b)

まず $y_0'' + y_0 = 0$ の一般解は $y_0(t) = A\cos t + B\sin t$ です。初期条件 $y_0(0) = 1$，$y_0'(0) = 0$ より $A = 1$，$B = 0$ となり，次式が得られます。

$$
y_0(t) = \cos t
$$

次に $y_1$ の方程式 $y_1'' + y_1 = \cos^3 t$ を解きます。与えられた恒等式 $(\cos\theta + i\sin\theta)^3 = \cos 3\theta + i\sin 3\theta$ の実部をとると

$$
\cos 3\theta = \cos^3\theta - 3\cos\theta\sin^2\theta = 4\cos^3\theta - 3\cos\theta
$$

となるため，3倍角の公式

$$
\cos^3 t = \frac{3}{4}\cos t + \frac{1}{4}\cos 3t
$$

が得られます。したがって $y_1$ の方程式は次の通りです。

$$
y_1'' + y_1 = \frac{3}{4}\cos t + \frac{1}{4}\cos 3t
$$

右辺の $\cos t$ は同次方程式 $y_1'' + y_1 = 0$ の解と共鳴するため，特解を

$$
y_{1,\mathrm{p}}(t) = c_1 t\sin t + c_2 \cos 3t
$$

とおいて代入します。2階微分を計算すると $(t\sin t)'' = 2\cos t - t\sin t$，$(\cos 3t)'' = -9\cos 3t$ なので，左辺は次のようになります。

$$
y_{1,\mathrm{p}}'' + y_{1,\mathrm{p}} = 2 c_1 \cos t - 8 c_2 \cos 3t
$$

右辺と係数を比較すると $2 c_1 = \dfrac{3}{4}$，$ -8 c_2 = \dfrac{1}{4}$ より $c_1 = \dfrac{3}{8}$，$c_2 = -\dfrac{1}{32}$ が得られます。したがって一般解は任意定数 $C_1, C_2$ を用いて次のように表されます。

$$
y_1(t) = C_1 \cos t + C_2 \sin t + \frac{3}{8} t\sin t - \frac{1}{32}\cos 3t
$$

初期条件 $y_1(0) = 0$，$y_1'(0) = 0$ を課します。

$$
\begin{aligned}
C_1 - \frac{1}{32} &= 0 \\
C_2 &= 0
\end{aligned}
$$

これより $C_1 = \dfrac{1}{32}$，$C_2 = 0$ となり，$y_1(t)$ が求まります。

$$
\finalanswer{y_0(t) = \cos t,\qquad y_1(t) = \frac{3}{8} t\sin t + \frac{1}{32}(\cos t - \cos 3t)}
$$

### (c)

(b) の結果を用いると，$\varepsilon$ の1次までの摂動展開は次の形をとります。

$$
y(t; \varepsilon) = \cos t + \varepsilon\left[\frac{3}{8} t\sin t + \frac{1}{32}(\cos t - \cos 3t)\right] + O(\varepsilon^2)
$$

この第1次補正項に含まれる $\dfrac{3}{8}\varepsilon t\sin t$ は時間 $t$ に比例して振幅が増大する永年項であり，$t \to \infty$ で発散します。

一方，元の非線形方程式 $y'' + y - \varepsilon y^3 = 0$ の両辺に $y'$ を掛けて積分すると，次のエネルギー保存則が得られます。

$$
\frac{1}{2}\left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2 + V(y) = E, \qquad V(y) = \frac{1}{2}y^2 - \frac{1}{4}\varepsilon y^4
$$

ポテンシャル $V(y)$ は $y = 0$ に極小値 $0$ をもち，$y = \pm\dfrac{1}{\sqrt{\varepsilon}}$ に極大値 $\dfrac{1}{4\varepsilon}$ をもつ対称な山を形成します。初期条件 $y(0) = 1$，$y'(0) = 0$ に対するエネルギーは $E = \dfrac{1}{2} - \dfrac{1}{4}\varepsilon$ であり，微小な $\varepsilon$ すなわち $0 < \varepsilon < 1$ では $1 < \dfrac{1}{\sqrt{\varepsilon}}$ かつ $E < \dfrac{1}{4\varepsilon}$ が成り立ちます。したがって厳密解 $y(t; \varepsilon)$ はすべての時刻 $t$ でポテンシャルの谷の内部 $-1 \le y(t; \varepsilon) \le 1$ に閉じ込められた有界な周期振動解となります。

それにもかかわらず，上記の単純なべき級数展開では $t$ が大きくなり $\varepsilon t \gtrsim 1$ すなわち $t \gtrsim \dfrac{1}{\varepsilon}$ に達すると，第1次項 $\varepsilon y_1(t)$ が $0$ 次項 $y_0(t)$ と同程度以上に大きくなり，摂動展開の前提が破綻して厳密解をまったく再現しなくなります。この破綻は，非線形項 $\varepsilon y^3$ によって厳密な周期解の角振動数が $1$ から $\omega(\varepsilon) = 1 - \dfrac{3}{8}\varepsilon + O(\varepsilon^2)$ へとわずかに変化するにもかかわらず，固定された角振動数 $1$ の関数で展開したことに起因します。実際，$\cos\bigl((1 - \dfrac{3}{8}\varepsilon)t\bigr)$ を $\varepsilon$ で展開すると $\cos t + \dfrac{3}{8}\varepsilon t\sin t + O(\varepsilon^2 t^2)$ となって永年項が現れます。したがって，この摂動展開にもとづく解は $t \ll \dfrac{1}{\varepsilon}$ の短い時間領域でのみ有効であり，$t \gtrsim \dfrac{1}{\varepsilon}$ の長時間領域では不適切です。
