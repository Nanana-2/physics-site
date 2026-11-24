---
title: 東大理物 平成31年度 物理学 第1問：1次元調和振動子と4次非調和摂動
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成31年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成31年度 物理学 第1問：1次元調和振動子と4次非調和摂動

## 問題

ハミルトニアン

$$
H_0 = \frac{1}{2m}p^2 + \frac{m\omega^2}{2}x^2
$$

を持つ1次元調和振動子の量子力学系を考える。ここで $m$ と $\omega$ は振動子の質量と固有振動数，$x$ と $p$ は座標と運動量の演算子である。プランク定数を $2\pi$ で割ったものを $\hbar$ とするとき，$x$ と $p$ は交換関係 $[x, p] = i\hbar$ を満たす。このような1次元束縛ポテンシャルを持つ系のハミルトニアンが対角化可能で縮退を持たないことを既知として，以下の設問に答えよ。

(1) 演算子 $a, a^\dagger, N$ を次のように定義する。

$$
a = \sqrt{\frac{m\omega}{2\hbar}}\left(x + \frac{ip}{m\omega}\right),\qquad
a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(x - \frac{ip}{m\omega}\right),\qquad
N = a^\dagger a.
$$

これらの交換子 $[a, a^\dagger],\ [N, a],\ [N, a^\dagger]$ を計算せよ。また，$H_0$ と $N$ の間には $H_0 = \hbar\omega(\alpha N + \beta)$ という関係が成り立つ。$\alpha$ と $\beta$ の値を書け。

(2) 上記の演算子 $N = a^\dagger a$ の固有値が (i) 非負であること，(ii) 整数であること，を示せ。

(3) エネルギー準位の番号をエネルギーの低い方から順に $n = 0, 1, 2, \dots$ とする。$n = 0$ は基底状態に対応する。$n$ 番目の準位のエネルギーを求めよ。また，$n$ 番目の準位に対応する規格化された固有状態を $|n\rangle$ とするとき，$n \ge 1$ に対する $|n\rangle$ を $a^\dagger$ と $|0\rangle$ を用いて表せ。

以下では $H_0$ にポテンシャル $V = \lambda x^4$（$\lambda$ は正の定数）を加えたハミルトニアン

$$
H = H_0 + V = \frac{1}{2m}p^2 + \frac{m\omega^2}{2}x^2 + \lambda x^4
$$

を持つ系を考える。

(4) $V$ を摂動と考え，エネルギー固有値の摂動展開を求めたい。

(i) 準備として一般の $V$ に適用できる表式を得ておこう。$n$ 番目の準位のエネルギーの摂動展開を $E_n = E_n^{(0)} + E_n^{(1)} + E_n^{(2)} + \dots$ とする。1次と2次の摂動 $E_n^{(1)},\ E_n^{(2)}$ を，$H_0$ の固有値 $E_k^{(0)}\ (k = 0, 1, 2, \dots)$ および $H_0$ の規格化された固有状態からなる基底 $|k\rangle\ (k = 0, 1, 2, \dots)$ に関する $V$ の行列要素 $V_{kl}\ (k, l = 0, 1, 2, \dots)$ を用いて表せ。ただし行列要素は $V|l\rangle = \displaystyle\sum_{k=0}^{\infty} |k\rangle V_{kl}$ によって定義される。

(ii) $V = \lambda x^4$ の場合に行列要素 $V_{k0}$ を計算し，基底状態のエネルギーを $\lambda$ に関する摂動展開の2次まで求めよ。

(5) 次に，$V$ が摂動とはみなすことができない場合を考えよう。高いエネルギーを持つ固有状態は準古典的に扱うことができる。準位番号 $n$ が十分大きい極限において，エネルギー固有値 $E_n$ が $n$ の何乗に比例するか答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成31年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
調和振動子のハミルトニアンを生成・消滅演算子 $a^\dagger, a$ で表すと，交換関係とノルムの非負性だけから等間隔の離散スペクトルと固有状態が代数的に決まります。$x$ が $a + a^\dagger$ に比例するため，$V = \lambda x^4$ の行列要素は基底状態から有限個の準位（$k = 0, 2, 4$）へのみ遷移し，2次摂動の和が有限項で閉じます。

一方，高励起状態（$n \gg 1$）では4次項 $\lambda x^4$ が2次項を上回るため，ボーア・ゾンマーフェルトの量子化条件で相空間面積のエネルギー依存性を評価することで，$E_n$ のべき則を導くことができます。
</div>

### (1)
正準交換関係 $[x, p] = i\hbar$ を用いて $[a, a^\dagger]$ を計算します。

$$
\begin{aligned}
[a, a^\dagger]
&= \frac{m\omega}{2\hbar}\left[x + \frac{ip}{m\omega},\ x - \frac{ip}{m\omega}\right] \\
&= \frac{m\omega}{2\hbar}\left(-\frac{i}{m\omega}[x, p] + \frac{i}{m\omega}[p, x]\right) \\
&= \frac{m\omega}{2\hbar}\left(-\frac{i}{m\omega}(i\hbar) + \frac{i}{m\omega}(-i\hbar)\right) = 1
\end{aligned}
$$

これを用いて $[N, a]$ と $[N, a^\dagger]$ を計算します。

$$
\begin{aligned}
[N, a] &= [a^\dagger a, a] = [a^\dagger, a]a + a^\dagger[a, a] = -a \\
[N, a^\dagger] &= [a^\dagger a, a^\dagger] = [a^\dagger, a^\dagger]a + a^\dagger[a, a^\dagger] = a^\dagger
\end{aligned}
$$

次に $N = a^\dagger a$ を展開して $H_0$ と比較します。

$$
\begin{aligned}
N = a^\dagger a
&= \frac{m\omega}{2\hbar}\left(x - \frac{ip}{m\omega}\right)\left(x + \frac{ip}{m\omega}\right) \\
&= \frac{m\omega}{2\hbar}\left(x^2 + \frac{p^2}{m^2\omega^2} + \frac{i}{m\omega}[x, p]\right) \\
&= \frac{1}{\hbar\omega}\left(\frac{p^2}{2m} + \frac{m\omega^2}{2}x^2\right) - \frac{1}{2} = \frac{H_0}{\hbar\omega} - \frac{1}{2}
\end{aligned}
$$

よって $H_0 = \hbar\omega\left(N + \dfrac{1}{2}\right)$ となります。したがって，

$$
\finalanswer{[a, a^\dagger] = 1,\quad [N, a] = -a,\quad [N, a^\dagger] = a^\dagger,\qquad \alpha = 1,\quad \beta = \frac{1}{2}}
$$

### (2)
$N$ の固有値 $\nu$ に対応する規格化された固有状態を $|\psi\rangle$（$N|\psi\rangle = \nu|\psi\rangle,\ \langle\psi|\psi\rangle = 1$）とします。

(i) 非負性：状態ベクトル $a|\psi\rangle$ のノルムの2乗は $0$ 以上なので，

$$
\nu = \langle\psi|N|\psi\rangle = \langle\psi|a^\dagger a|\psi\rangle = \|a|\psi\rangle\|^2 \ge 0
$$

となります。よって $N$ の固有値は非負です。

(ii) 整数性：問1の交換関係 $[N, a] = -a$ より，

$$
N(a|\psi\rangle) = (aN - a)|\psi\rangle = (\nu - 1)(a|\psi\rangle)
$$

が成り立ちます。すなわち $a|\psi\rangle \neq 0$ ならば，$a|\psi\rangle$ は $N$ の固有値 $\nu - 1$ に対応する固有状態です。同様に $k$ 回作用させると，$a^k|\psi\rangle \neq 0$ である限り $a^k|\psi\rangle$ は固有値 $\nu - k$ の固有状態となります。

もし $\nu$ が非負整数でないと仮定すると，任意の非負整数 $k$ に対して $\nu - k \neq 0$ なので，(i) より $\|a(a^k|\psi\rangle)\|^2 = (\nu - k)\|a^k|\psi\rangle\|^2 \neq 0$ となって $a^k|\psi\rangle$ は決して $0$ になりません。すると $k > \nu$ なる整数 $k$ に対して負の固有値 $\nu - k < 0$ が存在することになり，(i) の非負性に矛盾します。

したがって，ある非負整数 $n$ に対して $a^n|\psi\rangle \neq 0$ かつ $a^{n+1}|\psi\rangle = 0$ でなければなりません。このとき $N(a^n|\psi\rangle) = a^\dagger a(a^n|\psi\rangle) = 0$ である一方，$N(a^n|\psi\rangle) = (\nu - n)(a^n|\psi\rangle)$ なので，$\nu = n$ となります。よって $N$ の固有値は非負の整数です。

### (3)
問2より $N$ の固有値は非負整数であり，最小の固有値は $a|0\rangle = 0$ を満たす基底状態 $|0\rangle$ の固有値 $0$ です。また $[N, a^\dagger] = a^\dagger$ より $N(a^\dagger|n\rangle) = (n + 1)(a^\dagger|n\rangle)$ であり，そのノルムの2乗は

$$
\langle n|a a^\dagger|n\rangle = \langle n|(N + 1)|n\rangle = n + 1 > 0
$$

なので，$a^\dagger$ を作用させることで $n = 0, 1, 2, \dots$ のすべての非負整数が固有値として実現します。各固有状態 $|n\rangle$ は位相因子を除いて $a^\dagger|n\rangle = \sqrt{n + 1}\,|n + 1\rangle$ を満たします。これを $n = 0$ から繰り返し用いると，

$$
|n\rangle = \frac{1}{\sqrt{n}}\,a^\dagger|n - 1\rangle = \dots = \frac{1}{\sqrt{n!}}\,(a^\dagger)^n|0\rangle
$$

となります。また $H_0 = \hbar\omega\left(N + \dfrac{1}{2}\right)$ より $n$ 番目のエネルギー固有値は $E_n^{(0)} = \hbar\omega\left(n + \dfrac{1}{2}\right)$ です。したがって，

$$
\finalanswer{E_n^{(0)} = \hbar\omega\left(n + \frac{1}{2}\right),\qquad |n\rangle = \frac{1}{\sqrt{n!}}\,(a^\dagger)^n|0\rangle}
$$

### (4)
(i) 非縮退の定常摂動論を用います。固有値方程式 $(H_0 + \epsilon V)|\psi_n\rangle = E_n|\psi_n\rangle$ において（最後に $\epsilon = 1$ とおきます），

$$
E_n = E_n^{(0)} + \epsilon E_n^{(1)} + \epsilon^2 E_n^{(2)} + \dots,\qquad
|\psi_n\rangle = |n\rangle + \epsilon|\psi_n^{(1)}\rangle + \epsilon^2|\psi_n^{(2)}\rangle + \dots
$$

と展開し，中間規格化条件 $\langle n|\psi_n^{(1)}\rangle = \langle n|\psi_n^{(2)}\rangle = \dots = 0$ を課します。$\epsilon$ の1次および2次の項を比較すると，

$$
\begin{aligned}
\left(H_0 - E_n^{(0)}\right)|\psi_n^{(1)}\rangle &= \left(E_n^{(1)} - V\right)|n\rangle \\
\left(H_0 - E_n^{(0)}\right)|\psi_n^{(2)}\rangle &= \left(E_n^{(1)} - V\right)|\psi_n^{(1)}\rangle + E_n^{(2)}|n\rangle
\end{aligned}
$$

となります。第1式に左から $\langle n|$ を掛けると $E_n^{(1)} = \langle n|V|n\rangle = V_{nn}$ を得ます。また $k \neq n$ に対して左から $\langle k|$ を掛けると $\left(E_k^{(0)} - E_n^{(0)}\right)\langle k|\psi_n^{(1)}\rangle = -V_{kn}$ より，

$$
|\psi_n^{(1)}\rangle = \sum_{k \neq n} \frac{V_{kn}}{E_n^{(0)} - E_k^{(0)}}|k\rangle
$$

となります。これを第2式に代入して左から $\langle n|$ を掛けると，$E_n^{(2)} = \langle n|V|\psi_n^{(1)}\rangle$ および $V$ のエルミート性 $V_{nk} = V_{kn}^*$ より次式が得られます。したがって，

$$
\finalanswer{E_n^{(1)} = V_{nn},\qquad E_n^{(2)} = \sum_{k \neq n} \frac{|V_{kn}|^2}{E_n^{(0)} - E_k^{(0)}}}
$$

(ii) $x = \sqrt{\dfrac{\hbar}{2m\omega}}(a + a^\dagger)$ より，摂動ポテンシャルは

$$
V = \lambda x^4 = \lambda\left(\frac{\hbar}{2m\omega}\right)^2 (a + a^\dagger)^4
$$

です。$a|n\rangle = \sqrt{n}\,|n - 1\rangle,\ a^\dagger|n\rangle = \sqrt{n + 1}\,|n + 1\rangle$ を用いて $(a + a^\dagger)^4|0\rangle$ を順に計算します。

$$
\begin{aligned}
(a + a^\dagger)|0\rangle &= |1\rangle \\
(a + a^\dagger)^2|0\rangle &= |0\rangle + \sqrt{2}\,|2\rangle \\
(a + a^\dagger)^3|0\rangle &= |1\rangle + \sqrt{2}\left(\sqrt{2}\,|1\rangle + \sqrt{3}\,|3\rangle\right) = 3|1\rangle + \sqrt{6}\,|3\rangle \\
(a + a^\dagger)^4|0\rangle &= 3\left(|0\rangle + \sqrt{2}\,|2\rangle\right) + \sqrt{6}\left(\sqrt{3}\,|2\rangle + 2|4\rangle\right) \\
&= 3|0\rangle + 6\sqrt{2}\,|2\rangle + 2\sqrt{6}\,|4\rangle
\end{aligned}
$$

よって $V_{k0} = \langle k|V|0\rangle$ は $k = 0, 2, 4$ のみ $0$ でなく，次のように求まります。

$$
\begin{aligned}
V_{00} &= \frac{3\lambda\hbar^2}{4m^2\omega^2}, \qquad
V_{20} = \frac{3\sqrt{2}\,\lambda\hbar^2}{2m^2\omega^2}, \qquad
V_{40} = \frac{\sqrt{6}\,\lambda\hbar^2}{2m^2\omega^2} \\
V_{k0} &= 0 \qquad (k \neq 0, 2, 4)
\end{aligned}
$$

これらを (i) の公式に代入し，$E_0^{(0)} - E_2^{(0)} = -2\hbar\omega$，$E_0^{(0)} - E_4^{(0)} = -4\hbar\omega$ を用いて基底状態の1次・2次摂動エネルギーを求めます。

$$
\begin{aligned}
E_0^{(1)} &= V_{00} = \frac{3\lambda\hbar^2}{4m^2\omega^2} \\
E_0^{(2)} &= \frac{|V_{20}|^2}{-2\hbar\omega} + \frac{|V_{40}|^2}{-4\hbar\omega} \\
&= \lambda^2\left(\frac{\hbar}{2m\omega}\right)^4 \left(\frac{72}{-2\hbar\omega} + \frac{24}{-4\hbar\omega}\right) \\
&= \frac{\lambda^2\hbar^4}{16m^4\omega^4}\left(-\frac{42}{\hbar\omega}\right) = -\frac{21\lambda^2\hbar^3}{8m^4\omega^5}
\end{aligned}
$$

したがって，基底状態のエネルギーの $\lambda$ に関する2次までの摂動展開は

$$
\finalanswer{E_0 = \frac{1}{2}\hbar\omega + \frac{3\lambda\hbar^2}{4m^2\omega^2} - \frac{21\lambda^2\hbar^3}{8m^4\omega^5}}
$$

です（$V_{k0}$ は上記のとおり $V_{00} = \dfrac{3\lambda\hbar^2}{4m^2\omega^2},\ V_{20} = \dfrac{3\sqrt{2}\,\lambda\hbar^2}{2m^2\omega^2},\ V_{40} = \dfrac{\sqrt{6}\,\lambda\hbar^2}{2m^2\omega^2}$，その他は $0$）。

### (5)
$n \gg 1$ の高エネルギー領域では古典的転回点 $|x|$ が大きくなり，$\lambda x^4 \gg \dfrac{1}{2}m\omega^2 x^2$ となるため，全ポテンシャルは4次項 $U(x) \simeq \lambda x^4$ で近似することができます。

ボーア・ゾンマーフェルトの量子化条件（WKB 近似）を用います。古典的転回点を $\pm x_0$（$\lambda x_0^4 = E_n$，すなわち $x_0 = (E_n/\lambda)^{1/4}$）とおき，1周期にわたる作用積分 $\oint p\,\mathrm{d}x$ を変数変換 $x = x_0 u$ で評価します。

$$
\begin{aligned}
\oint p\,\mathrm{d}x
&= 4\int_0^{x_0} \sqrt{2m\left(E_n - \lambda x^4\right)}\,\mathrm{d}x \\
&= 4\sqrt{2m E_n}\left(\frac{E_n}{\lambda}\right)^{\frac{1}{4}} \int_0^1 \sqrt{1 - u^4}\,\mathrm{d}u \\
&= C\, E_n^{\frac{3}{4}}
\end{aligned}
$$

ここで $C = 4\sqrt{2m}\,\lambda^{-1/4}\displaystyle\int_0^1 \sqrt{1 - u^4}\,\mathrm{d}u$ は $E_n$ によらない正の定数です。量子化条件 $\oint p\,\mathrm{d}x = 2\pi\hbar\left(n + \dfrac{1}{2}\right) \simeq 2\pi\hbar n$（$n \gg 1$）より，$E_n^{3/4} \propto n$，すなわち $E_n \propto n^{4/3}$ となります。したがって，エネルギー固有値 $E_n$ は $n$ の $\dfrac{4}{3}$ 乗に比例します。

$$
\finalanswer{E_n \propto n^{4/3}}
$$

<aside class="rigor-note" markdown>
一般のべき乗ポテンシャル $U(x) = \lambda |x|^\gamma\ (\gamma > 0)$ に対して同じ準古典評価を行うと，作用積分は $E_n^{1/2 + 1/\gamma}$ に比例するため，$E_n \propto n^{2\gamma/(\gamma + 2)}$ となります。$\gamma = 2$（調和振動子）で $E_n \propto n$，$\gamma = 4$（4次非調和振動子）で $E_n \propto n^{4/3}$，$\gamma \to \infty$（無限井戸型ポテンシャル）で $E_n \propto n^2$ となり，代表的な1次元束縛系の漸近則を統一的に再現します。
</aside>
