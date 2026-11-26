---
title: 東大理物 平成20年度 数学 第2問：エルミート多項式の母関数と微分方程式
tags:
  - 院試過去問
  - 東大理物
  - 複素関数
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成20年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成20年度 数学 第2問：エルミート多項式の母関数と微分方程式

## 問題

$n = 0, 1, 2, \cdots$ に対して，関数 $f_n(x)$ を

$$
f_n(x) = e^{x^2}\frac{\mathrm{d}^n}{\mathrm{d}x^n}\left(e^{-x^2}\right)
$$

と定義する。以下の設問に答えよ。

(i) $f_n(x)$ は $x$ の多項式である。$x$ の何次の多項式であるか答えよ。

(ii) $n > 1$ に対して，

$$
\int_{-\infty}^{\infty} x f_n(x) e^{-x^2}\,\mathrm{d}x
$$

を求めよ。

(iii) 一般の $n$ に対して，

$$
\int_{-\infty}^{\infty} x^n f_n(x) e^{-x^2}\,\mathrm{d}x
$$

を求めよ。ただし，必要であれば，

$$
\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x = \sqrt{\pi}
$$

を用いてよい。

(iv) $z$ を複素数とするとき，

$$
e^{-z^2} = \frac{1}{2\pi i}\oint_C \frac{e^{-\omega^2}}{\omega - z}\,\mathrm{d}\omega
$$

が成り立つ。ここで，複素平面上の積分経路 $C$ は，図1のような $z$ を中心とした半径 $1$ の反時計回りの円周であるとする。このことを用いて，

$$
\sum_{n=0}^{\infty} \frac{t^n}{n!} f_n(z) = e^{-t^2 - 2zt} \qquad (|t| < 1)
$$

となることを示せ。ただし，今の場合，無限級数和と積分の順序を入れ替えてもよい。

<figure class="problem-figure" markdown>
![複素平面上の積分経路 C](../../../docs/assets/figures/pastexam-todai-ributsu/H20_sugaku_2-p-light.svg#only-light)
![複素平面上の積分経路 C](../../../docs/assets/figures/pastexam-todai-ributsu/H20_sugaku_2-p-dark.svg#only-dark)
<figcaption markdown="span">図1：積分経路 $C$（$\omega$ の複素平面）。</figcaption>
</figure>

(v) 設問 (iv) で得られた関数 $e^{-t^2 - 2zt}$ は，

$$
\frac{\partial^2}{\partial z^2}e^{-t^2 - 2zt} - 2z\frac{\partial}{\partial z}e^{-t^2 - 2zt} = -2t\frac{\partial}{\partial t}e^{-t^2 - 2zt}
$$

という式を満たす。このことを用いて，関数 $f_n(z)$ が

$$
\frac{\mathrm{d}^2}{\mathrm{d}z^2}f_n(z) - 2z\frac{\mathrm{d}}{\mathrm{d}z}f_n(z) + \lambda f_n(z) = 0
$$

という微分方程式を満たすということを示し，そのときの $\lambda$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成20年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
重み関数 $e^{-x^2}$ を掛けると $f_n(x)e^{-x^2}$ が $e^{-x^2}$ の $n$ 階導関数そのものに戻るため，$x^k$ との積の積分は部分積分を繰り返すだけでガウス積分として計算することができます。さらに $e^{-x^2}$ は $x \to \pm\infty$ で任意の多項式より速く $0$ に収束するため，すべての境界項が消えます。

また，$n$ 階導関数はコーシーの積分公式を微分して周回積分で表すことができます。この周回積分表示に $t^n/n!$ を掛けて和をとると被積分関数が等比級数としてまとまり，すべての $f_n(z)$ を1つの母関数へ集約して微分方程式を導くことができます。
</div>

### (i)

$f_n(x)$ の定義式より，$\dfrac{\mathrm{d}^n}{\mathrm{d}x^n}(e^{-x^2}) = f_n(x)e^{-x^2}$ です。この両辺をさらに $x$ で微分します。

$$
\begin{aligned}
\frac{\mathrm{d}^{n+1}}{\mathrm{d}x^{n+1}}(e^{-x^2}) &= \frac{\mathrm{d}}{\mathrm{d}x}\bigl(f_n(x)e^{-x^2}\bigr) \\
&= \bigl(f_n'(x) - 2x f_n(x)\bigr)e^{-x^2}
\end{aligned}
$$

両辺に $e^{x^2}$ を掛けると，漸化式 $f_{n+1}(x) = f_n'(x) - 2x f_n(x)$ が得られます。

これを用いて，$f_n(x)$ が最高次項 $(-2)^n x^n$ をもつ $n$ 次多項式であることを数学的帰納法で確かめます。$n = 0$ のときは $f_0(x) = e^{x^2}e^{-x^2} = 1 = (-2)^0 x^0$ なので $0$ 次多項式です。$f_n(x)$ が最高次項 $(-2)^n x^n$ をもつ $n$ 次多項式であると仮定すると，$f_n'(x)$ は高々 $n - 1$ 次であり，$-2x f_n(x)$ は最高次項 $(-2)^{n+1}x^{n+1}$ をもつ $n + 1$ 次多項式となります。よって $f_{n+1}(x) = f_n'(x) - 2x f_n(x)$ も最高次項 $(-2)^{n+1}x^{n+1}$ をもつ $n + 1$ 次多項式です。

したがって，$f_n(x)$ は $x$ の $n$ 次の多項式です。

### (ii)

定義より $f_n(x)e^{-x^2} = \dfrac{\mathrm{d}^n}{\mathrm{d}x^n}(e^{-x^2})$ です。任意の非負整数 $k$ に対して $\dfrac{\mathrm{d}^k}{\mathrm{d}x^k}(e^{-x^2}) = f_k(x)e^{-x^2}$ は多項式と $e^{-x^2}$ の積なので，$x \to \pm\infty$ で $0$ に収束します。同様に $x \cdot \dfrac{\mathrm{d}^k}{\mathrm{d}x^k}(e^{-x^2})$ も $x \to \pm\infty$ で $0$ に収束します。

$n > 1$ すなわち $n \ge 2$ のとき，部分積分を1回行います。

$$
\begin{aligned}
\int_{-\infty}^{\infty} x f_n(x)e^{-x^2}\,\mathrm{d}x &= \int_{-\infty}^{\infty} x \frac{\mathrm{d}^n}{\mathrm{d}x^n}\left(e^{-x^2}\right)\,\mathrm{d}x \\
&= \left[x\frac{\mathrm{d}^{n-1}}{\mathrm{d}x^{n-1}}\left(e^{-x^2}\right)\right]_{-\infty}^{\infty} - \int_{-\infty}^{\infty} \frac{\mathrm{d}^{n-1}}{\mathrm{d}x^{n-1}}\left(e^{-x^2}\right)\,\mathrm{d}x \\
&= 0 - \left[\frac{\mathrm{d}^{n-2}}{\mathrm{d}x^{n-2}}\left(e^{-x^2}\right)\right]_{-\infty}^{\infty} \\
&= 0
\end{aligned}
$$

ここで $n \ge 2$ より $n - 2 \ge 0$ なので，最後の境界項も $0$ になります。したがって，求める積分の値は次式となります。

$$
\finalanswer{\int_{-\infty}^{\infty} x f_n(x)e^{-x^2}\,\mathrm{d}x = 0}
$$

### (iii)

$n = 0$ のときは $f_0(x) = 1$ なので，積分は $\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x = \sqrt{\pi}$ です。

$n \ge 1$ のとき，$I_n = \int_{-\infty}^{\infty} x^n \dfrac{\mathrm{d}^n}{\mathrm{d}x^n}(e^{-x^2})\,\mathrm{d}x$ に対して部分積分を繰り返します。任意の非負整数 $j, k$ に対して $x^j \dfrac{\mathrm{d}^k}{\mathrm{d}x^k}(e^{-x^2}) = x^j f_k(x)e^{-x^2}$ は $x \to \pm\infty$ で $0$ になるため，各段階の境界項はすべて $0$ になります。

$$
\begin{aligned}
\int_{-\infty}^{\infty} x^n f_n(x)e^{-x^2}\,\mathrm{d}x &= \int_{-\infty}^{\infty} x^n \frac{\mathrm{d}^n}{\mathrm{d}x^n}\left(e^{-x^2}\right)\,\mathrm{d}x \\
&= \left[x^n\frac{\mathrm{d}^{n-1}}{\mathrm{d}x^{n-1}}\left(e^{-x^2}\right)\right]_{-\infty}^{\infty} - n\int_{-\infty}^{\infty} x^{n-1}\frac{\mathrm{d}^{n-1}}{\mathrm{d}x^{n-1}}\left(e^{-x^2}\right)\,\mathrm{d}x \\
&= (-1)n\int_{-\infty}^{\infty} x^{n-1}\frac{\mathrm{d}^{n-1}}{\mathrm{d}x^{n-1}}\left(e^{-x^2}\right)\,\mathrm{d}x \\
&= (-1)^2 n(n - 1)\int_{-\infty}^{\infty} x^{n-2}\frac{\mathrm{d}^{n-2}}{\mathrm{d}x^{n-2}}\left(e^{-x^2}\right)\,\mathrm{d}x \\
&\ \,\vdots \\
&= (-1)^n n!\int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x \\
&= (-1)^n n!\sqrt{\pi}
\end{aligned}
$$

この結果は $n = 0$ のときも $(-1)^0 0!\sqrt{\pi} = \sqrt{\pi}$ として成り立ちます。したがって，一般の $n$ に対する積分の値は次式となります。

$$
\finalanswer{\int_{-\infty}^{\infty} x^n f_n(x)e^{-x^2}\,\mathrm{d}x = (-1)^n n!\sqrt{\pi}}
$$

### (iv)

与えられたコーシーの積分公式

$$
e^{-z^2} = \frac{1}{2\pi i}\oint_C \frac{e^{-\omega^2}}{\omega - z}\,\mathrm{d}\omega
$$

の両辺を $z$ で $n$ 回微分します。$\dfrac{\mathrm{d}^n}{\mathrm{d}z^n}(\omega - z)^{-1} = \dfrac{n!}{(\omega - z)^{n+1}}$ より，次式が得られます。

$$
\frac{\mathrm{d}^n}{\mathrm{d}z^n}\left(e^{-z^2}\right) = \frac{n!}{2\pi i}\oint_C \frac{e^{-\omega^2}}{(\omega - z)^{n+1}}\,\mathrm{d}\omega
$$

両辺に $e^{z^2}\dfrac{t^n}{n!}$ を掛けると，次式になります。

$$
\frac{t^n}{n!}f_n(z) = \frac{e^{z^2}}{2\pi i}\oint_C \frac{e^{-\omega^2}}{\omega - z}\left(\frac{t}{\omega - z}\right)^n\,\mathrm{d}\omega
$$

$n = 0$ から $\infty$ まで和をとり，和と積分の順序を入れ替えます。

$$
\sum_{n=0}^{\infty} \frac{t^n}{n!}f_n(z) = \frac{e^{z^2}}{2\pi i}\oint_C \frac{e^{-\omega^2}}{\omega - z}\left(\sum_{n=0}^{\infty}\left(\frac{t}{\omega - z}\right)^n\right)\mathrm{d}\omega
$$

経路 $C$ は $z$ を中心とする半径 $1$ の円周なので，$C$ 上の任意の点 $\omega$ で $|\omega - z| = 1$ です。したがって $|t| < 1$ のとき $\left|\dfrac{t}{\omega - z}\right| = |t| < 1$ となり，括弧内の無限等比級数は次のように収束します。

$$
\begin{aligned}
\sum_{n=0}^{\infty}\left(\frac{t}{\omega - z}\right)^n &= \frac{1}{1 - \dfrac{t}{\omega - z}} \\
&= \frac{\omega - z}{\omega - z - t}
\end{aligned}
$$

これを積分に代入します。

$$
\begin{aligned}
\sum_{n=0}^{\infty} \frac{t^n}{n!}f_n(z) &= \frac{e^{z^2}}{2\pi i}\oint_C \frac{e^{-\omega^2}}{\omega - z}\cdot\frac{\omega - z}{\omega - (z + t)}\,\mathrm{d}\omega \\
&= \frac{e^{z^2}}{2\pi i}\oint_C \frac{e^{-\omega^2}}{\omega - (z + t)}\,\mathrm{d}\omega
\end{aligned}
$$

$|t| < 1$ より $|(z + t) - z| = |t| < 1$ なので，点 $\omega = z + t$ は半径 $1$ の円周 $C$ の内部にあります。また $e^{-\omega^2}$ は複素平面全体で正則なので，コーシーの積分公式より周回積分は $2\pi i e^{-(z + t)^2}$ に等しくなります。

$$
\begin{aligned}
\sum_{n=0}^{\infty} \frac{t^n}{n!}f_n(z) &= e^{z^2}\cdot e^{-(z + t)^2} \\
&= e^{z^2 - (z^2 + 2zt + t^2)} \\
&= e^{-t^2 - 2zt}
\end{aligned}
$$

以上より，与えられた等式が成り立ちます。

### (v)

設問 (iv) より $|t| < 1$ で $e^{-t^2 - 2zt} = \sum_{n=0}^{\infty} \dfrac{t^n}{n!}f_n(z)$ が成り立ちます。この級数を $z$ および $t$ について項別微分します。

$$
\begin{aligned}
\frac{\partial}{\partial z}e^{-t^2 - 2zt} &= \sum_{n=0}^{\infty} \frac{t^n}{n!}\frac{\mathrm{d}f_n(z)}{\mathrm{d}z} \\
\frac{\partial^2}{\partial z^2}e^{-t^2 - 2zt} &= \sum_{n=0}^{\infty} \frac{t^n}{n!}\frac{\mathrm{d}^2 f_n(z)}{\mathrm{d}z^2} \\
t\frac{\partial}{\partial t}e^{-t^2 - 2zt} &= t\sum_{n=1}^{\infty} \frac{n t^{n-1}}{n!}f_n(z) \\
&= \sum_{n=0}^{\infty} \frac{t^n}{n!}\,n f_n(z)
\end{aligned}
$$

これらを与えられた偏微分方程式に代入し，左辺へ移項します。

$$
\begin{aligned}
\sum_{n=0}^{\infty} \frac{t^n}{n!}\left(\frac{\mathrm{d}^2 f_n(z)}{\mathrm{d}z^2} - 2z\frac{\mathrm{d}f_n(z)}{\mathrm{d}z}\right) &= \sum_{n=0}^{\infty} \frac{t^n}{n!}\bigl(-2n f_n(z)\bigr) \\
\sum_{n=0}^{\infty} \frac{t^n}{n!}\left(\frac{\mathrm{d}^2 f_n(z)}{\mathrm{d}z^2} - 2z\frac{\mathrm{d}f_n(z)}{\mathrm{d}z} + 2n f_n(z)\right) &= 0
\end{aligned}
$$

この等式は $|t| < 1$ のすべての $t$ に対して恒等的に成り立つので，べき級数展開の一意性より各 $t^n$ の係数はすべて $0$ になります。

$$
\frac{\mathrm{d}^2}{\mathrm{d}z^2}f_n(z) - 2z\frac{\mathrm{d}}{\mathrm{d}z}f_n(z) + 2n f_n(z) = 0
$$

したがって，$f_n(z)$ は与えられた微分方程式を満たし，そのときの $\lambda$ は次式となります。

$$
\finalanswer{\lambda = 2n}
$$
