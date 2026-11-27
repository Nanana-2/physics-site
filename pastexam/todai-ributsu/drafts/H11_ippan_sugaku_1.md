---
title: 東大理物 平成11年度 一般教育科目 数学 第1問：ディリクレ積分の複素積分による評価とフーリエ級数
tags:
  - 院試過去問
  - 東大理物
  - 複素関数
  - 積分変換
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 一般教育科目 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成11年度 一般教育科目 数学 第1問：ディリクレ積分の複素積分による評価とフーリエ級数

## 問題

以下の設問に答えよ。
{: .problem-lead }

(1) $\alpha$ を実数としたときに次の積分を複素積分の方法を用いて求めよ。

$$
\int_0^\infty \mathrm{d}x\,\frac{\sin \alpha x}{x}
$$

(2) 区間 $[-\pi, \pi]$ で定義された関数 $f(x) = |x|$ のフーリエ級数展開を次のように表わしたとする：

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}(a_n\cos nx + b_n\sin nx) \qquad x \in [-\pi, \pi]
$$

このとき次の設問 (i), (ii) に答えよ。

(i) $a_n$（$n = 0, 1, 2, \dots$），$b_n$（$n = 1, 2, \dots$）を求めよ。

(ii) (i) の結果を用いて，次式を証明せよ。

$$
1 + \frac{1}{3^2} + \frac{1}{5^2} + \cdots = \sum_{n=0}^{\infty}\frac{1}{(2n + 1)^2} = \frac{\pi^2}{8}
$$

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 一般教育科目 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
(1) はディリクレ積分を複素積分で求める問題です。$\alpha$ の符号で場合分けを行い，$\alpha > 0$ の場合について関数 $\dfrac{e^{i\alpha z}}{z}$ を原点を避ける小半円と上半面の大半円からなる閉経路に沿って積分し，コーシーの積分定理とジョルダンの補題を用います。

(2) は偶関数 $|x|$ のフーリエ係数を部分積分で計算し，区分的に滑らかかつ連続な関数のフーリエ級数が各点で元の関数値に収束することを用いて $x = 0$ を代入することで無限級数の和を証明します。
</div>

### (1)

求める積分を $I(\alpha)$ とおきます。

$$
I(\alpha) = \int_0^\infty \frac{\sin\alpha x}{x}\,\mathrm{d}x
$$

$\alpha = 0$ のときは被積分関数が恒等的に $0$ なので，$I(0) = 0$ です。また $\alpha < 0$ のときは $\sin(\alpha x) = -\sin(|\alpha| x)$ より $I(\alpha) = -I(|\alpha|)$ が成り立ちます。したがって，以下では $\alpha > 0$ の場合を求めます。

被積分関数は偶関数であるため，次式が成り立ちます。

$$
I(\alpha) = \frac{1}{2}\lim_{\substack{\varepsilon \to +0 \\ R \to \infty}} \left(\int_{-R}^{-\varepsilon} + \int_{\varepsilon}^{R}\right)\frac{\sin\alpha x}{x}\,\mathrm{d}x
$$

複素関数 $g(z) = \dfrac{e^{i\alpha z}}{z}$ を考え，次の4つの部分からなる反時計回りの閉曲線 $C = L_1 + C_\varepsilon + L_2 + C_R$ に沿って積分します。

- $L_1$：実軸上の区間 $[-R, -\varepsilon]$ を左から右へ進む経路
- $C_\varepsilon$：原点を中心とする半径 $\varepsilon$ の上半円 $z = \varepsilon e^{i\theta}$ を $\theta = \pi$ から $0$ へ時計回りに進む経路
- $L_2$：実軸上の区間 $[\varepsilon, R]$ を左から右へ進む経路
- $C_R$：原点を中心とする半径 $R$ の上半円 $z = R e^{i\theta}$ を $\theta = 0$ から $\pi$ へ反時計回りに進む経路

$g(z)$ は閉曲線 $C$ の内部および周上で正則なので，コーシーの積分定理より次式が成り立ちます。

$$
\int_{L_1} g(z)\,\mathrm{d}z + \int_{C_\varepsilon} g(z)\,\mathrm{d}z + \int_{L_2} g(z)\,\mathrm{d}z + \int_{C_R} g(z)\,\mathrm{d}z = 0
$$

まず $L_1$ と $L_2$ の和を計算します。$L_1$ の積分で $x \mapsto -x$ と変数変換すると，$\cos(\alpha x)/x$ の奇関数部分が打ち消し合い，虚部だけが残ります。

$$
\begin{aligned}
\int_{L_1} g(z)\,\mathrm{d}z + \int_{L_2} g(z)\,\mathrm{d}z &= \int_{\varepsilon}^{R}\frac{e^{i\alpha x} - e^{-i\alpha x}}{x}\,\mathrm{d}x \\
&= 2i\int_{\varepsilon}^{R}\frac{\sin\alpha x}{x}\,\mathrm{d}x
\end{aligned}
$$

次に小半円 $C_\varepsilon$ 上の積分を計算します。$z = \varepsilon e^{i\theta}$，$\mathrm{d}z = i\varepsilon e^{i\theta}\,\mathrm{d}\theta$ を代入すると，

$$
\int_{C_\varepsilon}\frac{e^{i\alpha z}}{z}\,\mathrm{d}z = i\int_{\pi}^{0} e^{i\alpha\varepsilon e^{i\theta}}\,\mathrm{d}\theta
$$

となります。$\varepsilon \to +0$ のとき被積分関数は $[0, \pi]$ 上で $1$ に一様収束するため，極限は次の通りです。

$$
\lim_{\varepsilon \to +0}\int_{C_\varepsilon}\frac{e^{i\alpha z}}{z}\,\mathrm{d}z = -i\pi
$$

続いて大半円 $C_R$ 上の積分をジョルダンの補題に従って評価します。$z = R e^{i\theta}$ を代入し，$0 \le \theta \le \dfrac{\pi}{2}$ で成り立つ不等式 $\sin\theta \ge \dfrac{2}{\pi}\theta$ を用います。

$$
\begin{aligned}
\left|\int_{C_R}\frac{e^{i\alpha z}}{z}\,\mathrm{d}z\right| &\le \int_0^\pi \left|e^{i\alpha R(\cos\theta + i\sin\theta)}\right|\mathrm{d}\theta \\
&= \int_0^\pi e^{-\alpha R\sin\theta}\,\mathrm{d}\theta \\
&= 2\int_0^{\pi/2} e^{-\alpha R\sin\theta}\,\mathrm{d}\theta \\
&\le 2\int_0^{\pi/2} e^{-2\alpha R\theta/\pi}\,\mathrm{d}\theta \\
&= \frac{\pi}{\alpha R}\left(1 - e^{-\alpha R}\right)
\end{aligned}
$$

$\alpha > 0$ より，$R \to \infty$ の極限で $\int_{C_R} g(z)\,\mathrm{d}z \to 0$ となります。

以上の結果をコーシーの積分定理の式に代入し，$\varepsilon \to +0$，$R \to \infty$ の極限をとります。

$$
2i\int_0^\infty \frac{\sin\alpha x}{x}\,\mathrm{d}x - i\pi = 0
$$

したがって $\alpha > 0$ のとき $I(\alpha) = \dfrac{\pi}{2}$ です。$\alpha = 0$ および $\alpha < 0$ の場合を合わせて結論が得られます。

$$
\finalanswer{\int_0^\infty \frac{\sin\alpha x}{x}\,\mathrm{d}x =
\begin{cases}
\dfrac{\pi}{2} & (\alpha > 0) \\[8pt]
0 & (\alpha = 0) \\[8pt]
-\dfrac{\pi}{2} & (\alpha < 0)
\end{cases}}
$$

### (2) (i)

$f(x) = |x|$ は区間 $[-\pi, \pi]$ 上の偶関数です。$b_n$（$n = 1, 2, \dots$）の被積分関数 $|x|\sin nx$ は奇関数であるため，対称区間 $[-\pi, \pi]$ での積分はすべて $0$ になります。

$$
\begin{aligned}
b_n &= \frac{1}{\pi}\int_{-\pi}^{\pi} |x|\sin nx\,\mathrm{d}x \\
&= 0 \qquad (n = 1, 2, \dots)
\end{aligned}
$$

次に $a_0$ を求めます。

$$
\begin{aligned}
a_0 &= \frac{1}{\pi}\int_{-\pi}^{\pi} |x|\,\mathrm{d}x \\
&= \frac{2}{\pi}\int_0^\pi x\,\mathrm{d}x \\
&= \frac{2}{\pi}\left[\frac{x^2}{2}\right]_0^\pi \\
&= \pi
\end{aligned}
$$

続いて $n \ge 1$ に対する $a_n$ を部分積分で計算します。

$$
\begin{aligned}
a_n &= \frac{1}{\pi}\int_{-\pi}^{\pi} |x|\cos nx\,\mathrm{d}x \\
&= \frac{2}{\pi}\int_0^\pi x\cos nx\,\mathrm{d}x \\
&= \frac{2}{\pi}\left\{\left[\frac{x\sin nx}{n}\right]_0^\pi - \int_0^\pi \frac{\sin nx}{n}\,\mathrm{d}x\right\} \\
&= \frac{2}{\pi}\left[\frac{\cos nx}{n^2}\right]_0^\pi \\
&= \frac{2}{\pi n^2}\bigl((-1)^n - 1\bigr)
\end{aligned}
$$

$n$ の偶奇で整理すると，偶数 $n = 2k$（$k \ge 1$）のとき $a_{2k} = 0$，奇数 $n = 2k + 1$（$k \ge 0$）のとき $a_{2k+1} = -\dfrac{4}{\pi(2k + 1)^2}$ となります。

$$
\finalanswer{a_0 = \pi,\quad a_n = \frac{2\bigl((-1)^n - 1\bigr)}{\pi n^2}\quad (n = 1, 2, \dots),\quad b_n = 0\quad (n = 1, 2, \dots)}
$$

### (2) (ii)

(i) で求めた係数をフーリエ級数に代入すると，次の展開が得られます。

$$
f(x) = \frac{\pi}{2} - \frac{4}{\pi}\sum_{n=0}^{\infty}\frac{\cos\bigl((2n + 1)x\bigr)}{(2n + 1)^2}
$$

関数 $f(x) = |x|$ を周期 $2\pi$ の周期関数に拡張したものは実軸全体で連続かつ区分的に滑らかです。したがってディリクレの収束定理により，このフーリエ級数はすべての $x \in [-\pi, \pi]$ において $f(x)$ に各点収束します。さらに各項の絶対値が $\dfrac{4}{\pi(2n + 1)^2}$ で上から抑えられるため一様収束も成り立ちます。

特に $x = 0$ を代入すると，$f(0) = 0$ および $\cos 0 = 1$ より次式が成り立ちます。

$$
0 = \frac{\pi}{2} - \frac{4}{\pi}\sum_{n=0}^{\infty}\frac{1}{(2n + 1)^2}
$$

移項して両辺に $\dfrac{\pi}{4}$ を掛けると，求める等式が証明されます。

$$
\sum_{n=0}^{\infty}\frac{1}{(2n + 1)^2} = \frac{\pi^2}{8}
$$
