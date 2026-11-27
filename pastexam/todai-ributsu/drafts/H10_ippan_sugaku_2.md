---
title: 東大理物 平成10年度 一般教育科目 数学 第2問：定数変化法による非同次2階線形常微分方程式とデルタ関数極限
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 一般教育科目 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成10年度 一般教育科目 数学 第2問：定数変化法による非同次2階線形常微分方程式とデルタ関数極限

## 問題

関数 $y(x)$ に関する常微分方程式

$$
\frac{\mathrm{d}^2 y}{\mathrm{d}x^2} + \omega^2 y = f(x)
$$

について以下の設問に答えよ。ただし $\omega$ は正の定数であり，$x$ の範囲は $x \ge 0$ とする。
{: .problem-lead }

(a) $y = a(x)\cos\omega x + b(x)\sin\omega x$ とおいて上式に代入し，$\dfrac{\mathrm{d}a}{\mathrm{d}x}$ と $\dfrac{\mathrm{d}b}{\mathrm{d}x}$ に対する関係式を求めよ。ただし $\dfrac{\mathrm{d}a}{\mathrm{d}x}\cos\omega x + \dfrac{\mathrm{d}b}{\mathrm{d}x}\sin\omega x = 0$ とする。

(b) $a(x)$ と $b(x)$ を求めよ。

(c) $f(x) = 1/\lambda$（$0 \le x \le \lambda$），$0$（$x > \lambda$）のとき，$y(x)$ を求めよ。ただし $\lambda$ は正の定数であり，$x = 0$ で $y = \dfrac{\mathrm{d}y}{\mathrm{d}x} = 0$ とする。

(d) (c) で得られた $y(x)$ の $\lambda \to 0$ の極限を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 一般教育科目 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
調和振動子の強制振動を表す非同次2階常微分方程式を，定数変化法を用いて一般解の形に積分表示します。

(c) では幅 $\lambda$・面積 $1$ の矩形パルス外力に対する初期値問題を $0 \le x \le \lambda$ と $x > \lambda$ に分けて厳密に解き，(d) では $\lambda \to +0$ の極限をとることでデルタ関数撃力に対するグリーン関数 $\dfrac{\sin\omega x}{\omega}$ を導出します。
</div>

### (a)

$y(x) = a(x)\cos\omega x + b(x)\sin\omega x$ を $x$ で微分します。

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}a}{\mathrm{d}x}\cos\omega x + \frac{\mathrm{d}b}{\mathrm{d}x}\sin\omega x - \omega a(x)\sin\omega x + \omega b(x)\cos\omega x
$$

条件 $\dfrac{\mathrm{d}a}{\mathrm{d}x}\cos\omega x + \dfrac{\mathrm{d}b}{\mathrm{d}x}\sin\omega x = 0$ を用いると，1階導関数は次の形になります。

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = -\omega a(x)\sin\omega x + \omega b(x)\cos\omega x
$$

これをさらに $x$ で微分します。

$$
\frac{\mathrm{d}^2 y}{\mathrm{d}x^2} = -\omega\frac{\mathrm{d}a}{\mathrm{d}x}\sin\omega x + \omega\frac{\mathrm{d}b}{\mathrm{d}x}\cos\omega x - \omega^2 a(x)\cos\omega x - \omega^2 b(x)\sin\omega x
$$

元の微分方程式 $\dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2} + \omega^2 y = f(x)$ に代入すると，$a(x), b(x)$ の項が互いに打ち消し合い，次の関係式が得られます。

$$
-\omega\frac{\mathrm{d}a}{\mathrm{d}x}\sin\omega x + \omega\frac{\mathrm{d}b}{\mathrm{d}x}\cos\omega x = f(x)
$$

これを与えられた条件式と連立させます。

$$
\begin{aligned}
\frac{\mathrm{d}a}{\mathrm{d}x}\cos\omega x + \frac{\mathrm{d}b}{\mathrm{d}x}\sin\omega x &= 0 \\
-\frac{\mathrm{d}a}{\mathrm{d}x}\sin\omega x + \frac{\mathrm{d}b}{\mathrm{d}x}\cos\omega x &= \frac{f(x)}{\omega}
\end{aligned}
$$

第1式に $\cos\omega x$，第2式に $-\sin\omega x$ を掛けて加えると $\dfrac{\mathrm{d}a}{\mathrm{d}x}$ が得られ，第1式に $\sin\omega x$，第2式に $\cos\omega x$ を掛けて加えると $\dfrac{\mathrm{d}b}{\mathrm{d}x}$ が得られます。

$$
\finalanswer{\frac{\mathrm{d}a}{\mathrm{d}x} = -\frac{f(x)}{\omega}\sin\omega x,\qquad \frac{\mathrm{d}b}{\mathrm{d}x} = \frac{f(x)}{\omega}\cos\omega x}
$$

### (b)

(a) で求めた両式を $0$ から $x$ まで積分します。積分定数を $a_0 = a(0)$，$b_0 = b(0)$ とすると，$a(x)$ と $b(x)$ は次のように表されます。

$$
\finalanswer{a(x) = a_0 - \frac{1}{\omega}\int_0^x f(t)\sin(\omega t)\,\mathrm{d}t,\qquad b(x) = b_0 + \frac{1}{\omega}\int_0^x f(t)\cos(\omega t)\,\mathrm{d}t}
$$

### (c)

初期条件から積分定数 $a_0, b_0$ を定めます。(a) の途中の式より $y(0) = a_0$ および $y'(0) = \omega b_0$ です。条件 $y(0) = 0$，$y'(0) = 0$ および $\omega > 0$ より，$a_0 = 0$，$b_0 = 0$ となります。

このとき (b) の結果を $y(x) = a(x)\cos\omega x + b(x)\sin\omega x$ に代入し，三角関数の加法定理でまとめると，次式が得られます。

$$
\begin{aligned}
y(x) &= -\frac{\cos\omega x}{\omega}\int_0^x f(t)\sin(\omega t)\,\mathrm{d}t + \frac{\sin\omega x}{\omega}\int_0^x f(t)\cos(\omega t)\,\mathrm{d}t \\
&= \frac{1}{\omega}\int_0^x f(t)\sin\bigl(\omega(x - t)\bigr)\,\mathrm{d}t
\end{aligned}
$$

外力 $f(t)$ の定義に従って，$0 \le x \le \lambda$ と $x > \lambda$ に場合分けして積分を計算します。

まず $0 \le x \le \lambda$ のとき，区間 $[0, x]$ 上で $f(t) = \dfrac{1}{\lambda}$ なので，次のように積分されます。

$$
\begin{aligned}
y(x) &= \frac{1}{\lambda\omega}\int_0^x \sin\bigl(\omega(x - t)\bigr)\,\mathrm{d}t \\
&= \frac{1}{\lambda\omega}\left[\frac{\cos\bigl(\omega(x - t)\bigr)}{\omega}\right]_0^x \\
&= \frac{1 - \cos\omega x}{\lambda\omega^2}
\end{aligned}
$$

次に $x > \lambda$ のとき，区間 $[0, \lambda]$ で $f(t) = \dfrac{1}{\lambda}$，区間 $(\lambda, x]$ で $f(t) = 0$ なので，次のように積分されます。

$$
\begin{aligned}
y(x) &= \frac{1}{\lambda\omega}\int_0^\lambda \sin\bigl(\omega(x - t)\bigr)\,\mathrm{d}t \\
&= \frac{1}{\lambda\omega}\left[\frac{\cos\bigl(\omega(x - t)\bigr)}{\omega}\right]_0^\lambda \\
&= \frac{\cos\bigl(\omega(x - \lambda)\bigr) - \cos\omega x}{\lambda\omega^2}
\end{aligned}
$$

なお $x = \lambda$ において両式はともに $\dfrac{1 - \cos\omega\lambda}{\lambda\omega^2}$ に一致し，$y(x)$ と $y'(x)$ はともに連続につながります。

$$
\finalanswer{y(x) =
\begin{cases}
\dfrac{1 - \cos\omega x}{\lambda\omega^2} & (0 \le x \le \lambda) \\[10pt]
\dfrac{\cos\bigl(\omega(x - \lambda)\bigr) - \cos\omega x}{\lambda\omega^2} & (x > \lambda)
\end{cases}}
$$

### (d)

任意の固定した $x > 0$ に対して $\lambda \to +0$ とすると，十分に小さい $\lambda$ では常に $x > \lambda$ となります。したがって (c) の $x > \lambda$ の表式に対して極限を計算します。

$$
\begin{aligned}
\lim_{\lambda \to +0} y(x) &= \lim_{\lambda \to +0}\frac{\cos(\omega x - \omega\lambda) - \cos\omega x}{\lambda\omega^2} \\
&= -\frac{1}{\omega}\lim_{h \to +0}\frac{\cos(\omega x) - \cos(\omega x - h)}{h} \\
&= -\frac{1}{\omega}\left.\frac{\mathrm{d}}{\mathrm{d}u}(\cos u)\right|_{u = \omega x} \\
&= \frac{\sin\omega x}{\omega}
\end{aligned}
$$

ここで $h = \omega\lambda$ と置きました。また $x = 0$ においては任意の $\lambda > 0$ で $y(0) = 0$ であり，$\dfrac{\sin(\omega\cdot 0)}{\omega} = 0$ に一致します。したがってすべての $x \ge 0$ で極限は $\dfrac{\sin\omega x}{\omega}$ となります。

$$
\finalanswer{\lim_{\lambda \to +0} y(x) = \frac{\sin\omega x}{\omega} \qquad (x \ge 0)}
$$

<aside class="rigor-note" markdown>
$\lambda \to +0$ の極限では，幅 $\lambda$・高さ $1/\lambda$ の矩形パルス $f(x)$ は原点でのディラックのデルタ関数 $\delta(x)$ に近づきます。したがって得られた極限 $y(x) = \dfrac{\sin\omega x}{\omega}$（$x \ge 0$）は，初期条件 $y(0) = 0, y'(0^+) = 1$ を満たす因果グリーン関数に他なりません。
</aside>
