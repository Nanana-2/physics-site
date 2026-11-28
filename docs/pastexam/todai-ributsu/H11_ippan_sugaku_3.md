---
title: 東大理物 平成11年度 一般教育科目 数学 第3問：モニックエルミート多項式の構成と漸化式
tags:
  - 院試過去問
  - 東大理物
  - 特殊関数・変分法
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 一般教育科目 数学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成11年度 一般教育科目 数学 第3問：モニックエルミート多項式の構成と漸化式

## 問題

$H_n(x)$（$n = 0, 1, 2, \dots$）を $x$ の $n$ 次の多項式で次の性質を満たすものとする。

$$
\begin{aligned}
H_n(x) &= x^n + (\text{$n$ より低次の多項式}) \\
\int_{-\infty}^{\infty} \mathrm{d}x\, e^{-x^2} H_n(x) H_m(x) &= 0 \qquad (n \neq m)
\end{aligned}
$$

(1) $n = 1, 2, 3$ について $H_n(x)$ を具体的に構成せよ。ただし次の積分公式を用いて良い。

$$
\int_{-\infty}^{\infty} \mathrm{d}x\, x^{2m} e^{-x^2} = \sqrt{\pi}\frac{(2m)!}{4^m m!} \qquad (m = 0, 1, 2, \dots)
$$

一般に $n$ 次の多項式 $P(x)$ は $H_\ell(x)$ を用いて $P(x) = \sum_{\ell=0}^{n} c_\ell H_\ell(x)$ と展開できることに注意し，次の設問に答えよ。

(2) $H_n(-x) - (-1)^n H_n(x) = 0$ となることを帰納法を用いて証明せよ。

(3) $a_n$ を適当な係数として $H_n(x)$ が次の形の漸化式を満たすことを証明せよ。

$$
\begin{aligned}
x H_n(x) &= H_{n+1}(x) + a_n H_{n-1}(x) \\
\frac{\mathrm{d}}{\mathrm{d}x} H_n(x) &= n H_{n-1}(x)
\end{aligned}
$$

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 一般教育科目 数学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
重み関数 $e^{-x^2}$ に対する最高次係数 $1$ の直交多項式列の性質を，内積の直交性と多項式の展開基底性だけから導出します。

(1) ではグラム・シュミット直交化と同様に低次多項式との直交条件から係数を順次決定します。(2) では奇偶の差を表す多項式が低次直交基底と直交することを用いて数学的帰納法で示し，(3) では直交展開と部分積分を組み合わせて3項漸化式および微分公式を証明します。
</div>

### (1)

重み $e^{-x^2}$ 付きの内積を次のように記します。

$$
\langle f, g \rangle = \int_{-\infty}^{\infty} e^{-x^2} f(x) g(x)\,\mathrm{d}x
$$

与えられた積分公式より，偶べきのモーメントは次の値になります。

$$
\begin{aligned}
\langle 1, 1 \rangle &= \sqrt{\pi} \\
\langle x^2, 1 \rangle &= \frac{\sqrt{\pi}}{2} \\
\langle x^4, 1 \rangle &= \frac{3\sqrt{\pi}}{4}
\end{aligned}
$$

また被積分関数が奇関数となる奇べきの積分はすべて $0$ であり，$\langle x^{2k+1}, 1 \rangle = 0$（$k = 0, 1, 2, \dots$）が成り立ちます。

まず $n = 0$ のとき，最高次係数が $1$ の $0$ 次多項式なので $H_0(x) = 1$ です。

次に $n = 1$ について $H_1(x) = x + c_0$ とおきます。$\langle H_1, H_0 \rangle = 0$ より，

$$
\begin{aligned}
\langle x + c_0, 1 \rangle &= \langle x, 1 \rangle + c_0\langle 1, 1 \rangle \\
&= c_0\sqrt{\pi} \\
&= 0
\end{aligned}
$$

となるため $c_0 = 0$ であり，$H_1(x) = x$ を得ます。

次に $n = 2$ について $H_2(x) = x^2 + b_1 x + b_0$ とおきます。$\langle H_2, H_0 \rangle = 0$ および $\langle H_2, H_1 \rangle = 0$ より，各内積を計算すると次式が成り立ちます。

$$
\begin{aligned}
\frac{\sqrt{\pi}}{2} + b_0\sqrt{\pi} &= 0 \\
b_1\frac{\sqrt{\pi}}{2} &= 0
\end{aligned}
$$

これより $b_0 = -\dfrac{1}{2}$，$b_1 = 0$ となり，$H_2(x) = x^2 - \dfrac{1}{2}$ を得ます。

続いて $n = 3$ について $H_3(x) = x^3 + d_2 x^2 + d_1 x + d_0$ とおきます。直交条件 $\langle H_3, 1 \rangle = 0$，$\langle H_3, x \rangle = 0$，$\langle H_3, x^2 - \dfrac{1}{2} \rangle = 0$ より，次の連立方程式が得られます。

$$
\begin{aligned}
d_2\frac{\sqrt{\pi}}{2} + d_0\sqrt{\pi} &= 0 \\
\frac{3\sqrt{\pi}}{4} + d_1\frac{\sqrt{\pi}}{2} &= 0 \\
d_2\left(\frac{3\sqrt{\pi}}{4} - \frac{\sqrt{\pi}}{4}\right) + d_0\left(\frac{\sqrt{\pi}}{2} - \frac{\sqrt{\pi}}{2}\right) &= 0
\end{aligned}
$$

第3式より $d_2\dfrac{\sqrt{\pi}}{2} = 0$ なので $d_2 = 0$ であり，第1式から $d_0 = 0$，第2式から $d_1 = -\dfrac{3}{2}$ が求まります。よって $H_3(x) = x^3 - \dfrac{3}{2}x$ です。

$$
\finalanswer{H_1(x) = x,\qquad H_2(x) = x^2 - \frac{1}{2},\qquad H_3(x) = x^3 - \frac{3}{2}x}
$$

### (2)

すべての非負整数 $n$ に対して $H_n(-x) = (-1)^n H_n(x)$ が成り立つことを，強い数学的帰納法で証明します。

まず $n = 0$ のとき，$H_0(x) = 1$ より $H_0(-x) = 1$ かつ $(-1)^0 H_0(x) = 1$ なので，差は $0$ となり成り立ちます。

次に $k \ge 1$ とし，$0 \le m \le k - 1$ を満たすすべての整数 $m$ に対して $H_m(-x) = (-1)^m H_m(x)$ が成り立つと仮定します。ここで多項式

$$
g_k(x) = H_k(-x) - (-1)^k H_k(x)
$$

を定義します。高々 $k - 1$ 次の多項式 $q_{k-1}(x)$ を用いて $H_k(x) = x^k + q_{k-1}(x)$ と書くと，

$$
H_k(-x) = (-1)^k x^k + q_{k-1}(-x)
$$

なので，$g_k(x)$ では最高次の項 $(-1)^k x^k$ が打ち消し合い，$g_k(x)$ は高々 $k - 1$ 次の多項式となります。したがって問題文の注意より，適当な定数 $c_0, c_1, \dots, c_{k-1}$ を用いて次のように展開されます。

$$
g_k(x) = \sum_{\ell=0}^{k-1} c_\ell H_\ell(x)
$$

任意の $m$（$0 \le m \le k - 1$）に対して $g_k$ と $H_m$ の内積を計算します。第1項では $t = -x$ と変数変換し，帰納法の仮定 $H_m(-t) = (-1)^m H_m(t)$ を用います。

$$
\begin{aligned}
\langle g_k, H_m \rangle &= \int_{-\infty}^{\infty} e^{-x^2} H_k(-x) H_m(x)\,\mathrm{d}x - (-1)^k \langle H_k, H_m \rangle \\
&= \int_{-\infty}^{\infty} e^{-t^2} H_k(t) H_m(-t)\,\mathrm{d}t - (-1)^k \langle H_k, H_m \rangle \\
&= (-1)^m \langle H_k, H_m \rangle - (-1)^k \langle H_k, H_m \rangle \\
&= 0
\end{aligned}
$$

最後の等号では $m < k$ に対する直交性 $\langle H_k, H_m \rangle = 0$ を用いました。

一方，展開式を用いて内積をとると直交性より次式が得られます。

$$
\langle g_k, H_m \rangle = c_m \langle H_m, H_m \rangle
$$

$H_m(x)$ は最高次係数 $1$ の多項式なので恒等的に $0$ ではなく，$\langle H_m, H_m \rangle = \int_{-\infty}^{\infty} e^{-x^2}\{H_m(x)\}^2\,\mathrm{d}x > 0$ です。よってすべての $m = 0, 1, \dots, k - 1$ に対して $c_m = 0$ となり，$g_k(x) \equiv 0$ すなわち $H_k(-x) - (-1)^k H_k(x) = 0$ が成り立ちます。

以上より，帰納法によってすべての $n = 0, 1, 2, \dots$ で $H_n(-x) - (-1)^n H_n(x) = 0$ が証明されます。

### (3)

以下では $n \ge 1$ とします。

まず第1の漸化式を示します。$x H_n(x)$ は最高次の項が $x^{n+1}$ である $n + 1$ 次の多項式なので，$H_\ell(x)$（$0 \le \ell \le n + 1$）の線形結合として次のように展開されます。最高次係数の比較から $\ell = n + 1$ の係数は $1$ です。

$$
x H_n(x) = H_{n+1}(x) + \sum_{\ell=0}^{n} c_\ell H_\ell(x)
$$

両辺と $H_m(x)$（$0 \le m \le n$）の内積をとると，直交性より次式が得られます。

$$
c_m \langle H_m, H_m \rangle = \langle x H_n, H_m \rangle
$$

ここで右辺は $\langle H_n, x H_m \rangle$ と書き換えられます。

- $0 \le m \le n - 2$ のとき：$x H_m(x)$ は高々 $n - 1$ 次の多項式であるため，$H_0, \dots, H_{n-1}$ の線形結合として表され，$H_n$ と直交します。したがって $\langle H_n, x H_m \rangle = 0$ となり，$c_m = 0$ です。
- $m = n$ のとき：(2) より $H_n(-x) = (-1)^n H_n(x)$ なので，$\{H_n(x)\}^2$ は偶関数であり，被積分関数 $e^{-x^2} x \{H_n(x)\}^2$ は奇関数です。よって対称区間 $(-\infty, \infty)$ の積分は $0$ となり，$c_n = 0$ です。

したがって $m = n - 1$ の項だけが残り，$a_n = c_{n-1}$ とおけば $a_n = \dfrac{\langle H_n, x H_{n-1} \rangle}{\langle H_{n-1}, H_{n-1} \rangle}$ に対して次式が成り立ちます。

$$
x H_n(x) = H_{n+1}(x) + a_n H_{n-1}(x)
$$

次に第2の漸化式を示します。$H_n'(x) = \dfrac{\mathrm{d}}{\mathrm{d}x}H_n(x)$ は最高次の項が $n x^{n-1}$ である $n - 1$ 次の多項式なので，最高次係数を比較して次のように展開されます。

$$
H_n'(x) = n H_{n-1}(x) + \sum_{\ell=0}^{n-2} d_\ell H_\ell(x)
$$

任意の $m$（$0 \le m \le n - 2$）に対して両辺と $H_m(x)$ の内積をとり，右辺を部分積分で変形します。$|x| \to \infty$ で $e^{-x^2}$ が任意の多項式より速く $0$ に収束するため境界項は消えます。

$$
\begin{aligned}
d_m \langle H_m, H_m \rangle &= \int_{-\infty}^{\infty} e^{-x^2} H_n'(x) H_m(x)\,\mathrm{d}x \\
&= \left[e^{-x^2} H_n(x) H_m(x)\right]_{-\infty}^{\infty} - \int_{-\infty}^{\infty} H_n(x)\frac{\mathrm{d}}{\mathrm{d}x}\bigl(e^{-x^2} H_m(x)\bigr)\,\mathrm{d}x \\
&= \int_{-\infty}^{\infty} e^{-x^2} H_n(x)\bigl(2x H_m(x) - H_m'(x)\bigr)\,\mathrm{d}x
\end{aligned}
$$

ここで $2x H_m(x) - H_m'(x)$ は次数が $m + 1$ の多項式です。$m \le n - 2$ より $m + 1 \le n - 1 < n$ であるため，この多項式は $H_0, \dots, H_{n-1}$ の線形結合で表され，$H_n$ と直交します。したがって右辺は $0$ であり，$\langle H_m, H_m \rangle > 0$ よりすべての $m = 0, 1, \dots, n - 2$ について $d_m = 0$ となります。

よって求める第2の漸化式が得られます。

$$
\frac{\mathrm{d}}{\mathrm{d}x} H_n(x) = n H_{n-1}(x)
$$

<aside class="rigor-note" markdown>
上の部分積分を $m = n - 1$ に対して行うと，$2x H_{n-1}(x) - H_{n-1}'(x)$ の最高次項は $2 x^n$ なので，
$$
\begin{aligned}
n \langle H_{n-1}, H_{n-1} \rangle &= \langle H_n', H_{n-1} \rangle \\
&= 2\langle H_n, H_n \rangle
\end{aligned}
$$
が成り立ちます。一方 $x H_{n-1}(x) = H_n(x) + a_{n-1}H_{n-2}(x)$ より $\langle H_n, x H_{n-1} \rangle = \langle H_n, H_n \rangle$ となるため，第1の漸化式の係数は具体的に $a_n = \dfrac{n}{2}$ と決定されます。
</aside>
