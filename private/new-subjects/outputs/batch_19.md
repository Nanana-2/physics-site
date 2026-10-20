===== FILE: 14calculus/04/04_010.md =====
---
tags:
  - 基本
---

# 置換積分と部分積分

## 問題
積分の基本的な手法である部分積分法と置換積分法に関する以下の問いに答えよ。ただし，$C$ を積分定数とする。

(1) 部分積分法を用いて，不定積分 $\int x e^x dx$ を求めよ。

(2) 部分積分法を用いて，不定積分 $\int \ln x dx$（$x > 0$）を求めよ。

(3) $t = 1 + x^2$ とおく置換積分法を用いて，不定積分 $\int \frac{x}{\sqrt{1+x^2}} dx$ を求めよ。

---

## 解答・解説

<div class="approach" markdown>
被積分関数が積の形をしているときは，微分して簡単になる側と積分しやすい側に分けて部分積分を用います。また，関数の中に別の関数の導関数が掛け合わされている形を見つけたときは，置換積分によって基本関数の積分に変形します。
</div>

### (1)
部分積分法の公式 $\int f(x) g'(x) dx = f(x)g(x) - \int f'(x)g(x) dx$ を用います。$f(x) = x$，$g'(x) = e^x$ とおくと，$f'(x) = 1$，$g(x) = e^x$ となります。

公式に代入すると，次の式が得られます。

$$
\begin{aligned}
\int x e^x dx &= x e^x - \int 1 \cdot e^x dx \\
&= \finalanswer{\int x e^x dx = (x - 1)e^x + C}
\end{aligned}
$$

となります。

### (2)
被積分関数を $\ln x = 1 \cdot \ln x$ とみなして部分積分法を用います。$f(x) = \ln x$，$g'(x) = 1$ とおくと，$f'(x) = \dfrac{1}{x}$，$g(x) = x$ となります。

これらを部分積分の公式に代入します。

$$
\begin{aligned}
\int \ln x dx &= x \ln x - \int \frac{1}{x} \cdot x \, dx \\
&= x \ln x - \int 1 \, dx \\
&= \finalanswer{\int \ln x dx = x \ln x - x + C}
\end{aligned}
$$

が得られます。

### (3)
$t = 1 + x^2$ とおいて両辺を $x$ で微分すると，次式が成り立ちます。

$$
\frac{dt}{dx} = 2x \implies x \, dx = \frac{1}{2} dt
$$

この関係を用いて，与えられた不定積分を $t$ の積分に書き換えます。

$$
\begin{aligned}
\int \frac{x}{\sqrt{1+x^2}} dx &= \int \frac{1}{\sqrt{t}} \cdot \frac{1}{2} dt \\
&= \frac{1}{2} \int t^{-1/2} dt \\
&= \frac{1}{2} \left( 2 t^{1/2} \right) + C \\
&= \sqrt{t} + C
\end{aligned}
$$

最後に $t = 1 + x^2$ を代入します。

$$
\finalanswer{\int \frac{x}{\sqrt{1+x^2}} dx = \sqrt{1+x^2} + C}
$$

となります。

===== FILE: 14calculus/04/04_020.md =====
---
tags:
  - 標準
---

# 有理関数の積分

## 問題
有理関数の積分に関する以下の問いに答えよ。ただし，$a$ は正の定数，$C$ は積分定数とする。

(1) 不定積分 $\int \frac{1}{x^2+a^2} dx$ を求めよ。

(2) 次の恒等式を満たす実数の定数 $A, B$ を求めよ。
$$
\frac{1}{x(x^2+a^2)} = \frac{A}{x} + \frac{Bx}{x^2+a^2}
$$

(3) 不定積分 $\int \frac{1}{x(x^2+a^2)} dx$（$x > 0$）を求めよ。

---

## 解答・解説

<div class="approach" markdown>
分母が2次式の積分は逆三角関数を導く基本形になります。分母が因数分解できる有理関数は，部分分数分解によって1次式や既約2次式の和に分解してから個別に積分を計算します。
</div>

### (1)
$x = a \tan\theta$（$-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}$）とおいて置換積分を行います。両辺を微分すると $dx = \dfrac{a}{\cos^2\theta} d\theta = a(1+\tan^2\theta) d\theta$ となります。

被積分関数の分母は $x^2 + a^2 = a^2(1+\tan^2\theta)$ と変形できます。これを積分に代入します。

$$
\begin{aligned}
\int \frac{1}{x^2+a^2} dx &= \int \frac{1}{a^2(1+\tan^2\theta)} \cdot a(1+\tan^2\theta) d\theta \\
&= \frac{1}{a} \int 1 \, d\theta \\
&= \frac{1}{a} \theta + C
\end{aligned}
$$

$\theta = \arctan\left(\dfrac{x}{a}\right)$ であることから，次の式が得られます。

$$
\finalanswer{\int \frac{1}{x^2+a^2} dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C}
$$

です。

### (2)
与えられた式の右辺を通分してまとめます。

$$
\frac{A}{x} + \frac{Bx}{x^2+a^2} = \frac{A(x^2+a^2) + Bx^2}{x(x^2+a^2)} = \frac{(A+B)x^2 + Aa^2}{x(x^2+a^2)}
$$

これが元の式の左辺 $\dfrac{1}{x(x^2+a^2)}$ と任意の $x$ について一致するため，分子の係数を比較します。

$$
\begin{aligned}
A + B &= 0 \\
Aa^2 &= 1
\end{aligned}
$$

$a > 0$ より $a^2 \neq 0$ です。この連立方程式を解くと，係数は次のように求まります。

$$
\finalanswer{A = \frac{1}{a^2}, \quad B = -\frac{1}{a^2}}
$$

となります。

### (3)
(2) で求めた部分分数分解の結果を不定積分に代入します。

$$
\int \frac{1}{x(x^2+a^2)} dx = \frac{1}{a^2} \int \frac{1}{x} dx - \frac{1}{a^2} \int \frac{x}{x^2+a^2} dx
$$

第2項の積分については，分子が分母の導関数の定数倍であることに着目します。$\dfrac{d}{dx}(x^2+a^2) = 2x$ より，次のように変形できます。

$$
\int \frac{x}{x^2+a^2} dx = \frac{1}{2} \ln(x^2+a^2)
$$

$x > 0$ であることに注意して2つの項をまとめます。

$$
\begin{aligned}
\int \frac{1}{x(x^2+a^2)} dx &= \frac{1}{a^2} \ln x - \frac{1}{2a^2} \ln(x^2+a^2) + C \\
&= \frac{1}{2a^2} \ln(x^2) - \frac{1}{2a^2} \ln(x^2+a^2) + C \\
&= \finalanswer{\int \frac{1}{x(x^2+a^2)} dx = \frac{1}{2a^2} \ln\left(\frac{x^2}{x^2+a^2}\right) + C}
\end{aligned}
$$

が得られます。

===== FILE: 14calculus/04/04_030.md =====
---
tags:
  - 標準
---

# 三角関数を含む積分

## 問題
三角関数を含む不定積分と定積分に関する以下の問いに答えよ。

(1) $t = \tan \frac{x}{2}$（$-\pi < x < \pi$）とおくとき，$\cos x$ および微分 $\frac{dx}{dt}$ を $t$ の式で表せ。

(2) (1) の置換を用いて，不定積分 $\int \frac{1}{1+\cos x} dx$（$-\pi < x < \pi$）を求めよ。ただし，$C$ を積分定数とする。

(3) 自然数 $n \ge 2$ に対して，$I_n = \int_0^{\pi/2} \sin^n x dx$ とする。部分積分法を用いて $I_n$ と $I_{n-2}$ の間の漸化式を導け。

---

## 解答・解説

<div class="approach" markdown>
三角関数の有理式は，半角の正接による置換を行うことで代数的な有理関数の積分に帰着できます。三角関数の高次べきの定積分では，1つの因子を微分形とみなして部分積分を行うことで漸化式を導出します。
</div>

### (1)
倍角の公式 $\cos x = 2\cos^2\frac{x}{2} - 1$ を用います。$1 + \tan^2\frac{x}{2} = \dfrac{1}{\cos^2(x/2)}$ であるため，$\cos^2\frac{x}{2} = \dfrac{1}{1+t^2}$ が成り立ちます。

これを代入して $\cos x$ を $t$ で表します。

$$
\cos x = \frac{2}{1+t^2} - 1 = \finalanswer{\cos x = \frac{1-t^2}{1+t^2}}
$$

次に $t = \tan\frac{x}{2}$ の両辺を $x$ で微分します。

$$
\frac{dt}{dx} = \frac{1}{\cos^2(x/2)} \cdot \frac{1}{2} = \frac{1+t^2}{2}
$$

逆数をとることで $\dfrac{dx}{dt}$ が求まります。

$$
\finalanswer{\frac{dx}{dt} = \frac{2}{1+t^2}}
$$

となります。

### (2)
(1) の結果を用いて，被積分関数と微小区間を $t$ で表します。分母は次のように簡単になります。

$$
1 + \cos x = 1 + \frac{1-t^2}{1+t^2} = \frac{2}{1+t^2}
$$

これを積分に代入すると，$t$ の式が打ち消し合います。

$$
\begin{aligned}
\int \frac{1}{1+\cos x} dx &= \int \frac{1+t^2}{2} \cdot \frac{2}{1+t^2} dt \\
&= \int 1 \, dt \\
&= t + C
\end{aligned}
$$

$t = \tan\frac{x}{2}$ を戻します。

$$
\finalanswer{\int \frac{1}{1+\cos x} dx = \tan\frac{x}{2} + C}
$$

が得られます。

### (3)
$\sin^n x = \sin^{n-1} x \cdot \sin x$ と分解し，$\sin x = (-\cos x)'$ とみなして部分積分を行います。

$$
\begin{aligned}
I_n &= \int_0^{\pi/2} \sin^{n-1} x (-\cos x)' dx \\
&= \left[ -\sin^{n-1} x \cos x \right]_0^{\pi/2} - \int_0^{\pi/2} (n-1)\sin^{n-2} x \cos x (-\cos x) dx
\end{aligned}
$$

$n \ge 2$ より境界項は両端で 0 となります。第2項の $\cos^2 x$ を $1 - \sin^2 x$ に書き換えます。

$$
\begin{aligned}
I_n &= (n-1) \int_0^{\pi/2} \sin^{n-2} x (1 - \sin^2 x) dx \\
&= (n-1) I_{n-2} - (n-1) I_n
\end{aligned}
$$

$I_n$ の項を左辺に移項してまとめます。

$$
n I_n = (n-1) I_{n-2}
$$

両辺を $n$ で割ると，求める漸化式が得られます。

$$
\finalanswer{I_n = \frac{n-1}{n} I_{n-2}}
$$

です。

===== FILE: 14calculus/04/04_040.md =====
---
tags:
  - 基本
---

# 定積分と面積・体積

## 問題
放物線 $y = x^2$ と直線 $y = 2x$ で囲まれた図形について，以下の問いに答えよ。

<!-- FIGURE problem: xy平面上に放物線 y = x^2 と直線 y = 2x を描き，原点 O(0,0) と交点 (2,4) で囲まれる領域に斜線を施す。交点から x 軸へ破線を下ろし，x 座標 2 を明示する。 -->

(1) 放物線と直線の交点の $x$ 座標をすべて求めよ。

(2) 放物線と直線で囲まれた部分の面積 $S$ を求めよ。

(3) この囲まれた部分を $x$ 軸のまわりに1回転させてできる回転体の体積 $V$ を求めよ。

---

## 解答・解説

<div class="approach" markdown>
交点の座標から積分の上下端を決定し，上下の関数の差を積分して面積を計算します。$x$ 軸まわりの回転体の体積は，各断面における円板の面積の差を積分することで求めます。
</div>

### (1)
交点では $y$ 座標が等しくなるため，次の方程式が成り立ちます。

$$
x^2 = 2x
$$

左辺に移項して因数分解します。

$$
x(x - 2) = 0
$$

したがって，交点の $x$ 座標は次のようになります。

$$
\finalanswer{x = 0, \ 2}
$$

です。

### (2)
区間 $0 \le x \le 2$ において，$2x \ge x^2$ であるため，直線が放物線の上側にあります。

面積 $S$ は上側の関数から下側の関数を引いた定積分で与えられます。

$$
\begin{aligned}
S &= \int_0^2 (2x - x^2) dx \\
&= \left[ x^2 - \frac{x^3}{3} \right]_0^2 \\
&= 4 - \frac{8}{3} \\
&= \finalanswer{S = \frac{4}{3}}
\end{aligned}
$$

となります。

### (3)
$x$ 軸まわりに回転させたとき，$x$ における断面積は外側の半径 $y = 2x$ の円から内側の半径 $y = x^2$ の円を除いた中空の円環となります。断面積を $A(x)$ とおきます。

$$
A(x) = \pi (2x)^2 - \pi (x^2)^2 = \pi (4x^2 - x^4)
$$

この断面積を $x = 0$ から $x = 2$ まで積分して体積 $V$ を求めます。

$$
\begin{aligned}
V &= \pi \int_0^2 (4x^2 - x^4) dx \\
&= \pi \left[ \frac{4x^3}{3} - \frac{x^5}{5} \right]_0^2 \\
&= \pi \left( \frac{32}{3} - \frac{32}{5} \right) \\
&= \pi \left( \frac{160 - 96}{15} \right) \\
&= \finalanswer{V = \frac{64\pi}{15}}
\end{aligned}
$$

が得られます。

===== FILE: 14calculus/04/04_050.md =====
---
tags:
  - 標準
---

# 曲線の長さ

## 問題
媒介変数 $\theta$ を用いて次のように表されるサイクロイドを考える。
$$
x = a(\theta - \sin\theta), \quad y = a(1 - \cos\theta) \quad (0 \le \theta \le 2\pi)
$$
ただし，$a$ は正の定数とする。以下の問いに答えよ。

<!-- FIGURE problem: 半径 a の円が平らな面上をすべることなく転がるときに円周上の1点が描く曲線（サイクロイド）を 0 から 2pi までの1周期分描く。原点 (0,0) から始まり，θ=pi で頂点 (pi a, 2a)，θ=2pi で (2pi a, 0) に達する軌跡を示す。 -->

(1) 導関数 $\frac{dx}{d\theta}$ および $\frac{dy}{d\theta}$ を計算し，$\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2$ を $\theta$ の式で表せ。

(2) $0 \le \theta \le 2\pi$ の範囲において，線素 $\sqrt{\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2}$ を三角関数の半角の公式を用いて絶対値を含まない簡単な式で表せ。

(3) このサイクロイドの1周期分（$0 \le \theta \le 2\pi$）の曲線の長さ $L$ を求めよ。

---

## 解答・解説

<div class="approach" markdown>
媒介変数で表示された曲線の弧長は，各座標の微分から微小線素をつくり積分することで求めます。サイクロイドでは根号の中に現れる三角関数の項を半角の公式によって整理することが計算の要点となります。
</div>

### (1)
$x, y$ をそれぞれ $\theta$ で微分します。

$$
\frac{dx}{d\theta} = a(1 - \cos\theta), \quad \frac{dy}{d\theta} = a\sin\theta
$$

それぞれの2乗を計算して足し合わせます。

$$
\begin{aligned}
\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2 &= a^2(1 - \cos\theta)^2 + a^2\sin^2\theta \\
&= a^2(1 - 2\cos\theta + \cos^2\theta + \sin^2\theta)
\end{aligned}
$$

$\cos^2\theta + \sin^2\theta = 1$ を用いて整理します。

$$
\finalanswer{\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2 = 2a^2(1 - \cos\theta)}
$$

となります。

### (2)
半角の公式 $1 - \cos\theta = 2\sin^2\dfrac{\theta}{2}$ を根号の中に用います。

$$
\sqrt{\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2} = \sqrt{4a^2 \sin^2\frac{\theta}{2}} = 2a \left| \sin\frac{\theta}{2} \right|
$$

ここで，$\theta$ の範囲は $0 \le \theta \le 2\pi$ であるため，半角の引数は $0 \le \dfrac{\theta}{2} \le \pi$ となります。この区間では常に $\sin\dfrac{\theta}{2} \ge 0$ です。

したがって，絶対値をそのまま外すことができます。

$$
\finalanswer{\sqrt{\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2} = 2a\sin\frac{\theta}{2}}
$$

が得られます。

### (3)
曲線の長さ $L$ は線素の定積分として与えられます。

$$
L = \int_0^{2\pi} \sqrt{\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2} d\theta
$$

(2) で求めた式を代入して積分を計算します。

$$
\begin{aligned}
L &= \int_0^{2\pi} 2a\sin\frac{\theta}{2} d\theta \\
&= 2a \left[ -2\cos\frac{\theta}{2} \right]_0^{2\pi} \\
&= -4a \left( \cos\pi - \cos 0 \right) \\
&= -4a (-1 - 1) \\
&= \finalanswer{L = 8a}
\end{aligned}
$$

となります。サイクロイド1周期分の弧長は，転がる円の半径のちょうど8倍になります。

===== FILE: 14calculus/04/04_060.md =====
---
tags:
  - 標準
---

# 区分求積法

## 問題
和の極限と定積分の関係に関する以下の問いに答えよ。

(1) 自然数 $n$ に対する和 $S_n = \sum_{k=1}^n \frac{1}{n+k}$ を，$\frac{1}{n}\sum_{k=1}^n f\left(\frac{k}{n}\right)$ の形に変形し，関数 $f(x)$ を求めよ。

(2) 区分求積法を用いて極限値 $\lim_{n\to\infty} S_n$ を定積分の形で表し，その値を求めよ。

(3) 区分求積法を用いて極限値 $\lim_{n\to\infty} \sum_{k=1}^n \frac{n}{n^2+k^2}$ を求めよ。

---

## 解答・解説

<div class="approach" markdown>
幅が $1/n$ の短冊の面積の和とみなすことで，和の極限を定積分に変換します。各項から $1/n$ をくくり出し，残りの部分を $k/n$ の関数として捉えることが計算の手がかりです。
</div>

### (1)
和の一般項の分母と分子を $n$ で割ることで，$k/n$ の形を作り出します。

$$
\frac{1}{n+k} = \frac{1}{n\left(1 + \frac{k}{n}\right)} = \frac{1}{n} \cdot \frac{1}{1 + \frac{k}{n}}
$$

これより，和 $S_n$ は次のように変形できます。

$$
S_n = \frac{1}{n}\sum_{k=1}^n \frac{1}{1 + \frac{k}{n}}
$$

求める関数は $x = \dfrac{k}{n}$ と対応する部分です。

$$
\finalanswer{f(x) = \frac{1}{1+x}}
$$

となります。

### (2)
連続関数 $f(x)$ に対する区分求積法の公式を用います。

$$
\lim_{n\to\infty} \frac{1}{n}\sum_{k=1}^n f\left(\frac{k}{n}\right) = \int_0^1 f(x) dx
$$

(1) の結果を代入して積分を計算します。

$$
\begin{aligned}
\lim_{n\to\infty} S_n &= \int_0^1 \frac{1}{1+x} dx \\
&= \left[ \ln(1+x) \right]_0^1 \\
&= \ln 2 - \ln 1 \\
&= \finalanswer{\lim_{n\to\infty} S_n = \ln 2}
\end{aligned}
$$

が得られます。

### (3)
与えられた式の分母と分子を $n^2$ で割ります。

$$
\frac{n}{n^2+k^2} = \frac{\frac{1}{n}}{1 + \left(\frac{k}{n}\right)^2} = \frac{1}{n} \cdot \frac{1}{1 + \left(\frac{k}{n}\right)^2}
$$

したがって，求める極限は関数 $g(x) = \dfrac{1}{1+x^2}$ の区分求積の形になります。

$$
\lim_{n\to\infty} \sum_{k=1}^n \frac{n}{n^2+k^2} = \lim_{n\to\infty} \frac{1}{n}\sum_{k=1}^n \frac{1}{1 + \left(\frac{k}{n}\right)^2} = \int_0^1 \frac{1}{1+x^2} dx
$$

この定積分は逆正接関数を用いて求められます。

$$
\begin{aligned}
\int_0^1 \frac{1}{1+x^2} dx &= \left[ \arctan x \right]_0^1 \\
&= \arctan 1 - \arctan 0 \\
&= \frac{\pi}{4}
\end{aligned}
$$

よって，極限値は次のようになります。

$$
\finalanswer{\lim_{n\to\infty} \sum_{k=1}^n \frac{n}{n^2+k^2} = \frac{\pi}{4}}
$$

です。

===== FILE: 14calculus/04/04_070.md =====
---
tags:
  - 標準
---

# 広義積分の収束

## 問題
特異点や無限区間を含む広義積分に関する以下の問いに答えよ。

(1) 実数の定数 $p$ に対して，広義積分 $\int_0^1 x^{-p} dx$ が収束するための $p$ の条件を求め，収束するときの積分値を求めよ。

(2) 実数の定数 $p$ に対して，広義積分 $\int_1^\infty x^{-p} dx$ が収束するための $p$ の条件を求め，収束するときの積分値を求めよ。

(3) 非負の整数 $n$ に対して，$I_n = \int_0^\infty x^n e^{-x} dx$ とする。$n \ge 1$ のとき部分積分法を用いて $I_n$ と $I_{n-1}$ の関係式を導き，$I_n$ の値を $n$ の式で表せ。

---

## 解答・解説

<div class="approach" markdown>
特異点や無限大に近づく極限として広義積分を定義し，べき関数の積分の収束性を判定します。指数関数を含む無限区間の広義積分では，部分積分によって次数を下げる漸化式を導きます。
</div>

### (1)
原点 $x = 0$ が被積分関数の特異点になり得るため，$\epsilon > 0$ として極限をとります。

$$
\int_0^1 x^{-p} dx = \lim_{\epsilon \to +0} \int_\epsilon^1 x^{-p} dx
$$

$p = 1$ のとき，積分は $\ln 1 - \ln\epsilon = -\ln\epsilon$ となり，$\epsilon \to +0$ で発散します。$p \neq 1$ のときは次のように計算されます。

$$
\int_\epsilon^1 x^{-p} dx = \left[ \frac{x^{1-p}}{1-p} \right]_\epsilon^1 = \frac{1 - \epsilon^{1-p}}{1-p}
$$

$\epsilon \to +0$ でこの極限が有限の値に収束するためには，$\epsilon$ の指数が正であること，すなわち $1 - p > 0 \iff p < 1$ が必要十分です。このとき $\epsilon^{1-p} \to 0$ となります。

収束条件と値は次のようになります。

$$
\finalanswer{p < 1 \text{ のとき収束し，} \int_0^1 x^{-p} dx = \frac{1}{1-p}}
$$

です。

### (2)
無限区間の積分として定義に基づき計算します。

$$
\int_1^\infty x^{-p} dx = \lim_{M \to \infty} \int_1^M x^{-p} dx
$$

$p = 1$ のときは $\ln M \to \infty$ となり発散します。$p \neq 1$ のときは次の形になります。

$$
\int_1^M x^{-p} dx = \left[ \frac{x^{1-p}}{1-p} \right]_1^M = \frac{M^{1-p} - 1}{1-p}
$$

$M \to \infty$ で有限の値に収束するためには，$M$ の指数が負であること，すなわち $1 - p < 0 \iff p > 1$ が必要十分です。このとき $M^{1-p} \to 0$ となります。

極限を計算すると，求める条件と値が得られます。

$$
\finalanswer{p > 1 \text{ のとき収束し，} \int_1^\infty x^{-p} dx = \frac{1}{p-1}}
$$

となります。

### (3)
$I_n$ に対して $e^{-x} = (-e^{-x})'$ とみなして部分積分を行います。

$$
I_n = \left[ -x^n e^{-x} \right]_0^\infty + \int_0^\infty n x^{n-1} e^{-x} dx
$$

指数関数は任意のべき関数よりも速く減衰するため，$\lim_{x\to\infty} x^n e^{-x} = 0$ です。また $x = 0$ でも値は 0 となります。

これにより，境界項は消えます。

$$
I_n = n \int_0^\infty x^{n-1} e^{-x} dx = n I_{n-1}
$$

初項 $I_0$ を計算します。

$$
I_0 = \int_0^\infty e^{-x} dx = \left[ -e^{-x} \right]_0^\infty = 0 - (-1) = 1
$$

この関係式を繰り返し用いることで，$I_n$ が求まります。

$$
\finalanswer{I_n = n!, \quad I_n = n I_{n-1}}
$$

が得られます。この積分はガンマ関数の定義式そのものです。

===== FILE: 14calculus/05/05_010.md =====
---
tags:
  - 基本
---

# 偏微分と全微分

## 問題
多変数関数の偏微分と全微分に関する以下の問いに答えよ。

(1) 2変数関数 $f(x, y) = x^2 y^3$ の1階偏導関数 $\frac{\partial f}{\partial x}$ および $\frac{\partial f}{\partial y}$ を求めよ。

(2) $f(x, y) = x^2 y^3$ の全微分 $df$ を求めよ。

(3) 縦の長さ $x$ と横の長さ $y$ を測定して長方形の面積 $S(x, y) = xy$ を求める。$x$ の測定誤差を $\Delta x$，$y$ の測定誤差を $\Delta y$ とするとき，全微分を用いて面積の相対誤差 $\frac{\Delta S}{S}$ の近似式を $\frac{\Delta x}{x}$ および $\frac{\Delta y}{y}$ を用いて表せ。

---

## 解答・解説

<div class="approach" markdown>
偏微分では対象とする変数以外を定数とみなして通常の1変数微分を行います。微小変化に対する関数の変動は全微分で表され，これを用いて物理測定における合成誤差の見積もり式を導きます。
</div>

### (1)
$x$ で偏微分するときは $y$ を定数として扱い，$y$ で偏微分するときは $x$ を定数として扱います。

$$
\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(x^2) \cdot y^3 = 2x y^3
$$

同様に $y$ について微分します。

$$
\frac{\partial f}{\partial y} = x^2 \cdot \frac{\partial}{\partial y}(y^3) = 3x^2 y^2
$$

したがって，求める偏導関数は次のようになります。

$$
\finalanswer{\frac{\partial f}{\partial x} = 2x y^3, \quad \frac{\partial f}{\partial y} = 3x^2 y^2}
$$

です。

### (2)
2変数関数の全微分は各変数の偏導関数を用いて $df = \dfrac{\partial f}{\partial x} dx + \dfrac{\partial f}{\partial y} dy$ と定義されます。

(1) で求めた偏導関数を代入します。

$$
\finalanswer{df = 2x y^3 dx + 3x^2 y^2 dy}
$$

となります。

### (3)
面積関数 $S(x, y) = xy$ の全微分を計算します。偏導関数はそれぞれ $\dfrac{\partial S}{\partial x} = y$ および $\dfrac{\partial S}{\partial y} = x$ です。

微小変化に対する面積の変化量 $\Delta S$ は全微分で近似できます。

$$
\Delta S \approx \frac{\partial S}{\partial x}\Delta x + \frac{\partial S}{\partial y}\Delta y = y \Delta x + x \Delta y
$$

この両辺を元の面積 $S = xy$ で割ります。

$$
\frac{\Delta S}{S} \approx \frac{y \Delta x + x \Delta y}{xy} = \frac{\Delta x}{x} + \frac{\Delta y}{y}
$$

したがって，求める相対誤差の式が得られます。

$$
\finalanswer{\frac{\Delta S}{S} \approx \frac{\Delta x}{x} + \frac{\Delta y}{y}}
$$

積の形をした物理量の相対誤差は，各因子の相対誤差の和として見積もることができます。

===== FILE: 14calculus/05/05_020.md =====
---
tags:
  - 標準
---

# 合成関数の偏微分

## 問題
2次元の直交座標 $(x, y)$ と極座標 $(r, \theta)$ の関係は次式で与えられる。
$$
x = r\cos\theta, \quad y = r\sin\theta \quad (r > 0)
$$
以下の問いに答えよ。

(1) $r = \sqrt{x^2+y^2}$ および $\theta = \arctan\left(\frac{y}{x}\right)$ とする。偏導関数 $\frac{\partial r}{\partial x}$ および $\frac{\partial \theta}{\partial x}$ を $r$ と $\theta$ の式で表せ。

(2) 2階微分可能な関数 $u(x, y)$ に対して，連鎖律を用いて $\frac{\partial u}{\partial x}$ を $\frac{\partial u}{\partial r}$，$\frac{\partial u}{\partial \theta}$，$r$，$\theta$ で表せ。

(3) 関数 $u$ が角度 $\theta$ に依存せず動径 $r$ のみに依存するとき，2次元のラプラシアン $\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}$ を $r$ と $u$ の $r$ に関する導関数で表せ。

---

## 解答・解説

<div class="approach" markdown>
多変数関数の合成関数の微分では連鎖律を用いて各中間変数の寄与を足し合わせます。極座標表示への変換を微分演算子に適用し，特に対称性のある場合には角度微分の項を落として動径成分のみを整理します。
</div>

### (1)
$r^2 = x^2 + y^2$ の両辺を $x$ で偏微分します。

$$
2r \frac{\partial r}{\partial x} = 2x \implies \frac{\partial r}{\partial x} = \frac{x}{r} = \frac{r\cos\theta}{r} = \cos\theta
$$

次に $\theta = \arctan(y/x)$ の両辺を $x$ で偏微分します。$(\arctan t)' = \dfrac{1}{1+t^2}$ を用います。

$$
\frac{\partial \theta}{\partial x} = \frac{1}{1 + (y/x)^2} \cdot \left( -\frac{y}{x^2} \right) = -\frac{y}{x^2 + y^2} = -\frac{r\sin\theta}{r^2} = -\frac{\sin\theta}{r}
$$

偏導関数はそれぞれ次のようになります。

$$
\finalanswer{\frac{\partial r}{\partial x} = \cos\theta, \quad \frac{\partial \theta}{\partial x} = -\frac{\sin\theta}{r}}
$$

です。

### (2)
合成関数の微分公式（連鎖律）を用います。

$$
\frac{\partial u}{\partial x} = \frac{\partial u}{\partial r}\frac{\partial r}{\partial x} + \frac{\partial u}{\partial \theta}\frac{\partial \theta}{\partial x}
$$

(1) で求めた偏導関数を代入します。

$$
\finalanswer{\frac{\partial u}{\partial x} = \cos\theta \frac{\partial u}{\partial r} - \frac{\sin\theta}{r} \frac{\partial u}{\partial \theta}}
$$

が得られます。

### (3)
$y$ についても同様に連鎖律を適用すると，次の偏導関数が得られます。

$$
\frac{\partial r}{\partial y} = \sin\theta, \quad \frac{\partial \theta}{\partial y} = \frac{\cos\theta}{r}
$$

$u$ が $r$ のみに依存するとき，$\dfrac{\partial u}{\partial \theta} = 0$ となり，$\dfrac{\partial u}{\partial r} = \dfrac{du}{dr}$ です。1階微分は次のように簡単になります。

$$
\frac{\partial u}{\partial x} = \cos\theta \frac{du}{dr} = \frac{x}{r}\frac{du}{dr}, \quad \frac{\partial u}{\partial y} = \sin\theta \frac{du}{dr} = \frac{y}{r}\frac{du}{dr}
$$

これらをもう一度それぞれ $x, y$ で微分します。積の微分法を用います。

$$
\frac{\partial^2 u}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{x}{r}\right)\frac{du}{dr} + \frac{x}{r}\frac{\partial}{\partial x}\left(\frac{du}{dr}\right) = \left(\frac{1}{r} - \frac{x^2}{r^3}\right)\frac{du}{dr} + \frac{x^2}{r^2}\frac{d^2 u}{dr^2}
$$

同様に $y$ についても計算します。

$$
\frac{\partial^2 u}{\partial y^2} = \left(\frac{1}{r} - \frac{y^2}{r^3}\right)\frac{du}{dr} + \frac{y^2}{r^2}\frac{d^2 u}{dr^2}
$$

2つの式を足し合わせます。$x^2 + y^2 = r^2$ を用いると，次式が得られます。

$$
\begin{aligned}
\Delta u &= \left(\frac{2}{r} - \frac{x^2+y^2}{r^3}\right)\frac{du}{dr} + \frac{x^2+y^2}{r^2}\frac{d^2 u}{dr^2} \\
&= \left(\frac{2}{r} - \frac{1}{r}\right)\frac{du}{dr} + \frac{d^2 u}{dr^2} \\
&= \finalanswer{\Delta u = \frac{d^2 u}{dr^2} + \frac{1}{r}\frac{du}{dr}}
\end{aligned}
$$

となります。

===== FILE: 14calculus/05/05_030.md =====
---
tags:
  - 標準
---

# 陰関数の微分

## 問題
陰関数の微分法に関する以下の問いに答えよ。

(1) 2変数関数 $F(x, y) = 0$ が微分可能な陰関数 $y = y(x)$ を定めるとき，導関数 $\frac{dy}{dx}$ を $F$ の偏導関数 $F_x = \frac{\partial F}{\partial x}$ および $F_y = \frac{\partial F}{\partial y}$（$F_y \neq 0$）を用いて表せ。

(2) 円の方程式 $x^2 + y^2 - R^2 = 0$（$R > 0$）によって定まる陰関数について，(1) の公式を用いて導関数 $\frac{dy}{dx}$ を求めよ。

(3) 3つの変数 $x, y, z$ の間に状態方程式 $F(x, y, z) = 0$ が成り立っており，任意の2変数が独立変数として選べるとする。偏微分係数の積に関する次の関係式を示せ。
$$
\left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1
$$

---

## 解答・解説

<div class="approach" markdown>
陰関数で定義された関係式の全微分を 0 とおくことで，各変数の微分の比を偏微分係数で表現します。熱力学の状態方程式において現れる巡回関係式も，全微分の性質から導かれます。
</div>

### (1)
$F(x, y(x)) = 0$ の両辺を $x$ で微分します。合成関数の微分法を用いると，次の式が成り立ちます。

$$
\frac{\partial F}{\partial x}\frac{dx}{dx} + \frac{\partial F}{\partial y}\frac{dy}{dx} = 0
$$

$\dfrac{dx}{dx} = 1$ であるため，式を整理します。

$$
F_x + F_y \frac{dy}{dx} = 0
$$

$F_y \neq 0$ より，両辺を $F_y$ で割ることで導関数が得られます。

$$
\finalanswer{\frac{dy}{dx} = -\frac{F_x}{F_y}}
$$

です。

### (2)
$F(x, y) = x^2 + y^2 - R^2$ とおきます。各変数について偏微分を計算します。

$$
F_x = \frac{\partial F}{\partial x} = 2x, \quad F_y = \frac{\partial F}{\partial y} = 2y
$$

(1) の公式に代入します。

$$
\finalanswer{\frac{dy}{dx} = -\frac{2x}{2y} = -\frac{x}{y}}
$$

となります。

### (3)
$F(x, y, z) = 0$ の全微分を考えます。

$$
dF = F_x dx + F_y dy + F_z dz = 0
$$

$z$ を一定として扱うとき $dz = 0$ となるため，次式が成り立ちます。

$$
F_x dx + F_y dy = 0 \implies \left(\frac{\partial x}{\partial y}\right)_z = -\frac{F_y}{F_x}
$$

同様に，$x$ を一定とすると $dx = 0$ より次式が得られます。

$$
F_y dy + F_z dz = 0 \implies \left(\frac{\partial y}{\partial z}\right)_x = -\frac{F_z}{F_y}
$$

さらに $y$ を一定とすると $dy = 0$ より次式が得られます。

$$
F_z dz + F_x dx = 0 \implies \left(\frac{\partial z}{\partial x}\right)_y = -\frac{F_x}{F_z}
$$

これら3つの偏微分係数の積を計算します。

$$
\begin{aligned}
\left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y &= \left(-\frac{F_y}{F_x}\right) \left(-\frac{F_z}{F_y}\right) \left(-\frac{F_x}{F_z}\right) \\
&= \finalanswer{\left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1}
\end{aligned}
$$

となり，等式が示されました。右辺が $+1$ ではなく $-1$ になる点が重要です。

===== FILE: 14calculus/05/05_040.md =====
---
tags:
  - 標準
---

# 2変数のテイラー展開と極値

## 問題
2変数関数 $f(x, y) = x^3 + y^3 - 3xy$ の極値に関する以下の問いに答えよ。

(1) 1階偏導関数 $f_x = \frac{\partial f}{\partial x}$ および $f_y = \frac{\partial f}{\partial y}$ を求め，停留点（$f_x = 0$ かつ $f_y = 0$ を満たす点）をすべて求めよ。

(2) 2階偏導関数 $f_{xx} = \frac{\partial^2 f}{\partial x^2}$，$f_{yy} = \frac{\partial^2 f}{\partial y^2}$，$f_{xy} = \frac{\partial^2 f}{\partial x \partial y}$ を求めよ。

(3) ヘッセ行列の行列式 $D = f_{xx}f_{yy} - (f_{xy})^2$ を用いて，各停留点における極値（極大・極小・鞍点）を判定せよ。極値をとる場合はその極値も求めよ。

---

## 解答・解説

<div class="approach" markdown>
多変数関数の極値の候補は1階偏導関数がすべて 0 となる停留点として求められます。各停留点における曲面の局所的な曲がり方は，2階偏導関数から構成されるヘッセ行列の行列式と対角成分の符号によって判定します。
</div>

### (1)
$f(x, y)$ をそれぞれの変数で偏微分します。

$$
f_x = 3x^2 - 3y, \quad f_y = 3y^2 - 3x
$$

停留点の条件 $f_x = 0$ および $f_y = 0$ より，次の連立方程式が得られます。

$$
\begin{aligned}
y &= x^2 \\
x &= y^2
\end{aligned}
$$

第1式を第2式に代入します。

$$
x = (x^2)^2 = x^4 \implies x(x^3 - 1) = 0
$$

実数の範囲で解くと $x = 0$ または $x = 1$ です。対応する $y$ は $y = 0, 1$ となります。

したがって，停留点は次の2点です。

$$
\finalanswer{(x, y) = (0, 0), \ (1, 1)}
$$

となります。

### (2)
1階偏導関数をさらに偏微分します。

$$
\begin{aligned}
f_{xx} &= \frac{\partial}{\partial x}(3x^2 - 3y) = 6x \\
f_{yy} &= \frac{\partial}{\partial y}(3y^2 - 3x) = 6y \\
f_{xy} &= \frac{\partial}{\partial y}(3x^2 - 3y) = -3
\end{aligned}
$$

求める2階偏導関数は次の通りです。

$$
\finalanswer{f_{xx} = 6x, \quad f_{yy} = 6y, \quad f_{xy} = -3}
$$

です。

### (3)
ヘッセ行列の行列式 $D$ は次式で与えられます。

$$
D = f_{xx}f_{yy} - (f_{xy})^2 = (6x)(6y) - (-3)^2 = 36xy - 9
$$

求めた2つの停留点について調べます。

まず点 $(0, 0)$ においては次のようになります。

$$
D(0, 0) = -9 < 0
$$

行列式が負であるため，点 $(0, 0)$ は極値をとらず鞍点（峠点）です。

次に点 $(1, 1)$ においては次のようになります。

$$
D(1, 1) = 36 - 9 = 27 > 0
$$

行列式が正であり，かつ $f_{xx}(1, 1) = 6 > 0$ であるため，下に凸の曲面となります。したがって，点 $(1, 1)$ で極小値をとります。

その極小値を計算します。

$$
f(1, 1) = 1^3 + 1^3 - 3 \cdot 1 \cdot 1 = -1
$$

以上より，判定結果は次のようになります。

$$
\finalanswer{(0, 0) \text{ は鞍点}，\quad (1, 1) \text{ で極小値 } -1}
$$

が得られます。

===== FILE: 14calculus/05/05_050.md =====
---
tags:
  - 標準
---

# 条件付き極値

## 問題
制約条件のもとでの関数の極値に関する以下の問いに答えよ。

(1) 周の長さが $2L$（$L > 0$）で一定である長方形を考える。2辺の長さを $x, y$（$x > 0, y > 0$）とするとき，制約条件 $x + y = L$ のもとで面積 $S(x, y) = xy$ を最大にする $x, y$ の値をラグランジュの未定乗数法を用いて求めよ。

(2) 楕円 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$（$a > b > 0$）上の点 $(x, y)$ と原点との距離の2乗 $f(x, y) = x^2 + y^2$ を考える。ラグランジュの未定乗数法を用いて，$f(x, y)$ の最大値および最小値を求めよ。

---

## 解答・解説

<div class="approach" markdown>
制約条件を持つ多変数関数の極値問題では，未定乗数を導入して目的関数と制約関数の勾配ベクトルが平行になる条件を求めます。各停留点における関数の値を比較して大域的な最大値や最小値を特定します。
</div>

### (1)
制約条件を $g(x, y) = x + y - L = 0$ とおきます。未定乗数 $\lambda$ を導入し，次のラグランジュ関数を定義します。

$$
F(x, y, \lambda) = xy - \lambda (x + y - L)
$$

極値を与える点では各変数に関する偏微分が 0 となります。

$$
\begin{aligned}
\frac{\partial F}{\partial x} &= y - \lambda = 0 \\
\frac{\partial F}{\partial y} &= x - \lambda = 0 \\
\frac{\partial F}{\partial \lambda} &= -(x + y - L) = 0
\end{aligned}
$$

最初の2式より $x = y = \lambda$ が得られます。これを第3式に代入します。

$$
x + x = L \implies x = \frac{L}{2}
$$

したがって，$y$ も同様に求まります。

$$
\finalanswer{x = \frac{L}{2}, \quad y = \frac{L}{2}}
$$

長方形が正方形になるときに面積は最大になります。

### (2)
制約条件を $g(x, y) = \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - 1 = 0$ とおきます。ラグランジュ関数を次のように設定します。

$$
F(x, y, \lambda) = x^2 + y^2 - \lambda \left( \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1 \right)
$$

停留点の条件を求めます。

$$
\begin{aligned}
\frac{\partial F}{\partial x} &= 2x\left(1 - \frac{\lambda}{a^2}\right) = 0 \\
\frac{\partial F}{\partial y} &= 2y\left(1 - \frac{\lambda}{b^2}\right) = 0
\end{aligned}
$$

点 $(x, y)$ は楕円上の点であるため，$(x, y) \neq (0, 0)$ です。$a > b > 0$ より $a^2 \neq b^2$ であることに注意して場合分けを行います。

$x \neq 0$ のときは $\lambda = a^2$ となります。このとき $1 - \dfrac{\lambda}{b^2} = 1 - \dfrac{a^2}{b^2} \neq 0$ であるため，$y = 0$ でなければなりません。制約条件から $x = \pm a$ となり，このときの値は $f(\pm a, 0) = a^2$ です。

$y \neq 0$ のときは $\lambda = b^2$ となります。同様に $x = 0$ が導かれ，制約条件から $y = \pm b$ となります。このときの値は $f(0, \pm b) = b^2$ です。

$a > b$ より，$a^2 > b^2$ です。したがって，最大値と最小値は次のように決まります。

$$
\finalanswer{\text{最大値 } a^2, \quad \text{最小値 } b^2}
$$

となります。

===== FILE: 14calculus/06/06_010.md =====
---
tags:
  - 基本
---

# 累次積分と積分順序の交換

## 問題
累次積分 $I = \int_0^1 \left( \int_y^1 e^{-x^2} dx \right) dy$ について，以下の問いに答えよ。

<!-- FIGURE problem: xy平面上に積分領域 D を描く。x軸の範囲は 0 から 1，y軸の範囲は 0 から 1。直線 y=x と直線 x=1，および x軸 (y=0) で囲まれた直角三角形の領域に斜線を施す。内側の積分が y から 1 までの横方向の線分であることを示す矢印を描く。 -->

(1) この積分の積分領域 $D$ を，$x$ の範囲を先に指定する不等式（$0 \le x \le 1$ かつ $g_1(x) \le y \le g_2(x)$）の形で表せ。

(2) 積分の順序を交換して，$I$ を $x$ について外側，$y$ について内側の累次積分の形で表せ。

(3) 順序を交換した累次積分を計算し，$I$ の値を求めよ。

---

## 解答・解説

<div class="approach" markdown>
初等関数で積分できない関数を含む累次積分では，積分順序を交換することで容易に積分可能な形に変形できます。領域の幾何学的な形状を図から捉え直し，変数の取り得る範囲を逆の順序で表現します。
</div>

### (1)
問題で与えられた積分の範囲から，領域 $D$ は次のように表されています。

$$
0 \le y \le 1, \quad y \le x \le 1
$$

これは $xy$ 平面において，直線 $y = 0$（$x$ 軸），直線 $x = 1$，および直線 $y = x$ で囲まれた直角三角形の領域を表しています。

$x$ を先に固定すると，$x$ は 0 から 1 までの値をとります。その各 $x$ に対して，$y$ は下限の 0 から上限の $x$ まで動きます。

したがって，領域 $D$ は次のように表されます。

$$
\finalanswer{0 \le x \le 1, \quad 0 \le y \le x}
$$

です。

### (2)
(1) で求めた積分範囲に従って，重積分の累次積分表示を書き換えます。外側を $x$ の積分，内側を $y$ の積分とします。

$$
\finalanswer{I = \int_0^1 \left( \int_0^x e^{-x^2} dy \right) dx}
$$

となります。

### (3)
内側の $y$ に関する積分を先に計算します。被積分関数 $e^{-x^2}$ は $y$ に依存しないため，定数として扱えます。

$$
\int_0^x e^{-x^2} dy = e^{-x^2} \int_0^x 1 \, dy = x e^{-x^2}
$$

これを外側の $x$ の積分に代入します。

$$
I = \int_0^1 x e^{-x^2} dx
$$

この積分は $t = x^2$ とおく置換積分，あるいは導関数に着目することで直接計算できます。$(e^{-x^2})' = -2x e^{-x^2}$ を用います。

$$
\begin{aligned}
I &= \left[ -\frac{1}{2} e^{-x^2} \right]_0^1 \\
&= -\frac{1}{2} e^{-1} - \left(-\frac{1}{2} e^0\right) \\
&= \finalanswer{I = \frac{1 - e^{-1}}{2}}
\end{aligned}
$$

が得られます。

===== FILE: 14calculus/06/06_020.md =====
---
tags:
  - 基本
---

# 極座標による重積分とガウス積分

## 問題
重積分を用いたガウス積分の導出に関する以下の問いに答えよ。

(1) 平面極座標への変数変換 $x = r\cos\theta$，$y = r\sin\theta$ に対するヤコビアン $J = \frac{\partial(x, y)}{\partial(r, \theta)}$ を計算せよ。

(2) 半径 $R$ の円板領域 $D_R = \{ (x, y) \mid x^2 + y^2 \le R^2 \}$ における重積分 $I_R = \iint_{D_R} e^{-(x^2+y^2)} dxdy$ を，極座標を用いて計算せよ。

(3) 1変数の積分 $I = \int_{-\infty}^\infty e^{-x^2} dx$ とする。$I^2 = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)} dxdy$ であることを用いて，$I$ の値を求めよ。

---

## 解答・解説

<div class="approach" markdown>
直交座標の2乗の形をした広義積分は，2次元の平面全体に拡張して極座標変換を行うことで容易に計算できます。動径方向の積分で現れる $r$ はヤコビアンに由来し，これが被積分関数の合成関数の微分形を作り出します。
</div>

### (1)
ヤコビアンは偏導関数を並べた行列の行列式として定義されます。

$$
J = \det \begin{pmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\ \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} \end{pmatrix} = \det \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}
$$

行列式を計算します。

$$
J = (\cos\theta)(r\cos\theta) - (-r\sin\theta)(\sin\theta) = r(\cos^2\theta + \sin^2\theta)
$$

$\cos^2\theta + \sin^2\theta = 1$ より，ヤコビアンが求まります。

$$
\finalanswer{J = r}
$$

となります。

### (2)
円板領域 $D_R$ は極座標において $0 \le r \le R$，$0 \le \theta \le 2\pi$ と表されます。面積要素は $dxdy = r dr d\theta$ となります。

重積分を累次積分に書き換えます。

$$
\begin{aligned}
I_R &= \int_0^{2\pi} d\theta \int_0^R e^{-r^2} r \, dr \\
&= \left( \int_0^{2\pi} 1 \, d\theta \right) \left( \int_0^R r e^{-r^2} dr \right)
\end{aligned}
$$

$\theta$ の積分は $2\pi$ です。$r$ の積分は $(e^{-r^2})' = -2r e^{-r^2}$ を用いて計算します。

$$
\int_0^R r e^{-r^2} dr = \left[ -\frac{1}{2} e^{-r^2} \right]_0^R = \frac{1 - e^{-R^2}}{2}
$$

これらを掛け合わせます。

$$
I_R = 2\pi \cdot \frac{1 - e^{-R^2}}{2} = \finalanswer{I_R = \pi (1 - e^{-R^2})}
$$

が得られます。

### (3)
実数全体での積分 $I = \int_{-\infty}^\infty e^{-x^2} dx$ に対して，$I^2$ を積分の積として表します。

$$
I^2 = \left( \int_{-\infty}^\infty e^{-x^2} dx \right) \left( \int_{-\infty}^\infty e^{-y^2} dy \right) = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)} dxdy
$$

平面全体での重積分は，$R \to \infty$ の極限における円板上の積分 $I_R$ の極限と一致します。

$$
I^2 = \lim_{R\to\infty} I_R = \lim_{R\to\infty} \pi (1 - e^{-R^2}) = \pi
$$

被積分関数 $e^{-x^2}$ は常に正であるため，$I > 0$ です。

したがって，平方根をとることでガウス積分の値が決まります。

$$
\finalanswer{I = \sqrt{\pi}}
$$

です。

===== FILE: 14calculus/06/06_030.md =====
---
tags:
  - 標準
---

# 変数変換とヤコビアン

## 問題
重積分の変数変換に関する以下の問いに答えよ。ただし，$a, b$ は正の定数とする。

(1) 変数変換 $x = au$，$y = bv$ に対するヤコビアン $J = \frac{\partial(x, y)}{\partial(u, v)}$ を求めよ。

(2) 楕円領域 $D = \left\{ (x, y) \;\middle|\; \frac{x^2}{a^2} + \frac{y^2}{b^2} \le 1 \right\}$ の面積 $S = \iint_D dxdy$ を，(1) の変数変換を用いて求めよ。

(3) 重積分 $K = \iint_D (x^2 + y^2) dxdy$ を求めよ。

---

## 解答・解説

<div class="approach" markdown>
楕円領域での重積分は，座標軸を拡大・縮小する変数変換によって単位円盤上の積分に帰着させます。円盤領域に変換した後は極座標を用いることで，対称性を生かして計算を進めることができます。
</div>

### (1)
ヤコビ行列の各成分を偏微分によって計算します。

$$
\frac{\partial x}{\partial u} = a, \quad \frac{\partial x}{\partial v} = 0, \quad \frac{\partial y}{\partial u} = 0, \quad \frac{\partial y}{\partial v} = b
$$

ヤコビアンはこれらを行列式に並べたものです。

$$
J = \det \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix} = ab - 0 = \finalanswer{J = ab}
$$

となります。

### (2)
変数変換 $x = au, y = bv$ により，楕円の不等式は次のように変換されます。

$$
\frac{(au)^2}{a^2} + \frac{(bv)^2}{b^2} \le 1 \implies u^2 + v^2 \le 1
$$

$uv$ 平面における領域を $D' = \{ (u, v) \mid u^2 + v^2 \le 1 \}$ とおきます。これは半径 1 の単位円盤です。面積要素は $dxdy = |J| dudv = ab \, dudv$ となります。

面積 $S$ を計算します。

$$
S = \iint_D dxdy = \iint_{D'} ab \, dudv = ab \iint_{D'} dudv
$$

$\iint_{D'} dudv$ は単位円盤の面積 $\pi \cdot 1^2 = \pi$ です。

したがって，楕円の面積が得られます。

$$
\finalanswer{S = \pi ab}
$$

です。

### (3)
被積分関数に変数変換を適用します。

$$
x^2 + y^2 = a^2 u^2 + b^2 v^2
$$

積分は次のように書き換えられます。

$$
K = \iint_{D'} (a^2 u^2 + b^2 v^2) ab \, dudv
$$

ここで $uv$ 平面の極座標 $u = r\cos\theta, v = r\sin\theta$（$0 \le r \le 1, 0 \le \theta \le 2\pi$）を導入します。面積要素は $dudv = r dr d\theta$ です。

$$
K = ab \int_0^1 dr \int_0^{2\pi} d\theta \, r (a^2 r^2 \cos^2\theta + b^2 r^2 \sin^2\theta)
$$

$\theta$ に関する積分を計算します。対称性より $\int_0^{2\pi} \cos^2\theta d\theta = \int_0^{2\pi} \sin^2\theta d\theta = \pi$ です。

$$
\int_0^{2\pi} (a^2 \cos^2\theta + b^2 \sin^2\theta) d\theta = \pi(a^2 + b^2)
$$

残る $r$ の積分を計算します。

$$
\int_0^1 r^3 dr = \left[ \frac{r^4}{4} \right]_0^1 = \frac{1}{4}
$$

これらを掛け合わせます。

$$
K = ab \cdot \pi(a^2 + b^2) \cdot \frac{1}{4} = \finalanswer{K = \frac{\pi ab(a^2 + b^2)}{4}}
$$

が得られます。

===== FILE: 14calculus/06/06_040.md =====
---
tags:
  - 標準
---

# 3重積分と球座標

## 問題
3次元の球座標 $(r, \theta, \phi)$ は直交座標 $(x, y, z)$ との間で次のように定義される。
$$
x = r\sin\theta\cos\phi, \quad y = r\sin\theta\sin\phi, \quad z = r\cos\theta
$$
ここで $r \ge 0$，$0 \le \theta \le \pi$，$0 \le \phi < 2\pi$ である。以下の問いに答えよ。

(1) ヤコビアン $J = \frac{\partial(x, y, z)}{\partial(r, \theta, \phi)}$ を計算し，体積要素が $dV = r^2\sin\theta \, dr d\theta d\phi$ となることを示せ。

(2) 半径 $R$ の球領域 $V = \{ (x, y, z) \mid x^2 + y^2 + z^2 \le R^2 \}$ の体積を，球座標の3重積分を用いて求めよ。

(3) 質量 $M$，半径 $R$ の一様な球（密度 $\rho = \frac{M}{\frac{4}{3}\pi R^3}$）の，$z$ 軸まわりの慣性モーメント $I_z = \iiint_V \rho (x^2 + y^2) dV$ を求めよ。

---

## 解答・解説

<div class="approach" markdown>
球対称な物理対象の積分は球座標系を用いることで3つの独立な1変数積分に分解できます。体積要素に含まれる幾何学的な因子をヤコビアンから導き，回転対称性を利用して慣性モーメントを計算します。
</div>

### (1)
偏導関数を行列に並べます。

$$
J = \det \begin{pmatrix}
\sin\theta\cos\phi & r\cos\theta\cos\phi & -r\sin\theta\sin\phi \\
\sin\theta\sin\phi & r\cos\theta\sin\phi & r\sin\theta\cos\phi \\
\cos\theta & -r\sin\theta & 0
\end{pmatrix}
$$

第3行について余因子展開を行います。

$$
\begin{aligned}
J &= \cos\theta \cdot (r^2 \sin\theta\cos\theta \cos^2\phi + r^2 \sin\theta\cos\theta \sin^2\phi) \\
&\quad - (-r\sin\theta) \cdot (r\sin^2\theta \cos^2\phi + r\sin^2\theta \sin^2\phi) \\
&= \cos\theta (r^2 \sin\theta\cos\theta) + r\sin\theta (r\sin^2\theta) \\
&= r^2 \sin\theta (\cos^2\theta + \sin^2\theta)
\end{aligned}
$$

$\cos^2\theta + \sin^2\theta = 1$ より，ヤコビアンが求まります。

$$
J = r^2 \sin\theta
$$

体積要素は $dV = |J| dr d\theta d\phi$ で与えられます。$0 \le \theta \le \pi$ では $\sin\theta \ge 0$ であるため，次の式が得られます。

$$
\finalanswer{dV = r^2\sin\theta \, dr d\theta d\phi}
$$

となり，示されました。

### (2)
球領域 $V$ は球座標で $0 \le r \le R$，$0 \le \theta \le \pi$，$0 \le \phi \le 2\pi$ と表されます。体積は各成分の積に分解できます。

$$
\begin{aligned}
\iiint_V dV &= \left( \int_0^R r^2 dr \right) \left( \int_0^\pi \sin\theta d\theta \right) \left( \int_0^{2\pi} d\phi \right)
\end{aligned}
$$

各積分を個別に計算します。

$$
\int_0^R r^2 dr = \frac{R^3}{3}, \quad \int_0^\pi \sin\theta d\theta = [-\cos\theta]_0^\pi = 2, \quad \int_0^{2\pi} d\phi = 2\pi
$$

これらを掛け合わせます。

$$
\finalanswer{\iiint_V dV = \frac{4}{3}\pi R^3}
$$

が得られます。

### (3)
$z$ 軸からの距離の2乗は次のように表されます。

$$
x^2 + y^2 = (r\sin\theta\cos\phi)^2 + (r\sin\theta\sin\phi)^2 = r^2 \sin^2\theta
$$

慣性モーメントの積分を球座標で表します。

$$
I_z = \rho \int_0^R r^4 dr \int_0^\pi \sin^3\theta d\theta \int_0^{2\pi} d\phi
$$

各積分を計算します。$\sin^3\theta = \sin\theta(1-\cos^2\theta)$ より，次式が成り立ちます。

$$
\int_0^\pi \sin^3\theta d\theta = \left[ -\cos\theta + \frac{\cos^3\theta}{3} \right]_0^\pi = \left(1 - \frac{1}{3}\right) - \left(-1 + \frac{1}{3}\right) = \frac{4}{3}
$$

動径方向の積分は $\int_0^R r^4 dr = \dfrac{R^5}{5}$ です。積分全体をまとめます。

$$
I_z = \rho \cdot \frac{R^5}{5} \cdot \frac{4}{3} \cdot 2\pi = \frac{8\pi \rho R^5}{15}
$$

$\rho = \dfrac{M}{\frac{4}{3}\pi R^3}$ を代入します。

$$
I_z = \frac{8\pi R^5}{15} \cdot \frac{3M}{4\pi R^3} = \finalanswer{I_z = \frac{2}{5}MR^2}
$$

となります。

===== FILE: 14calculus/06/06_050.md =====
---
tags:
  - 標準
---

# 重心と慣性モーメント

## 問題
質量 $M$，半径 $R$ の一様な半円板 $D = \{ (x, y) \mid x^2 + y^2 \le R^2, \, y \ge 0 \}$ を考える。面密度を $\sigma = \frac{2M}{\pi R^2}$ とする。以下の問いに答えよ。

<!-- FIGURE problem: xy平面上に x^2 + y^2 <= R^2 かつ y >= 0 で定義される半円板 D を描く。底辺は x 軸上の -R から R までの線分。対称軸として y 軸を描き，重心 G が y 軸上にあることを示す目印 (0, y_G) を置く。 -->

(1) 対称性より重心の $x$ 座標は $x_G = 0$ である。重心の $y$ 座標 $y_G = \frac{1}{M}\iint_D y \sigma \, dxdy$ を極座標を用いて求めよ。

(2) この半円板の直径（$x$ 軸）のまわりの慣性モーメント $I_x = \iint_D y^2 \sigma \, dxdy$ を求めよ。

(3) 重心を通り $x$ 軸に平行な軸のまわりの慣性モーメント $I_G$ を，平行軸の定理を用いて求めよ。

---

## 解答・解説

<div class="approach" markdown>
半円板のような円形境界を持つ領域のモーメント計算は極座標変換によって簡潔に実行できます。重心位置と任意の軸まわりの慣性モーメントが求まれば，平行軸の定理によって重心軸まわりの慣性モーメントが得られます。
</div>

### (1)
極座標 $x = r\cos\theta, y = r\sin\theta$ を導入します。半円板の領域は $0 \le r \le R$，$0 \le \theta \le \pi$ であり，面積要素は $dxdy = r dr d\theta$ です。

$y$ の積分を計算します。

$$
\begin{aligned}
\iint_D y \, dxdy &= \int_0^\pi d\theta \int_0^R (r\sin\theta) r \, dr \\
&= \left( \int_0^\pi \sin\theta d\theta \right) \left( \int_0^R r^2 dr \right) \\
&= [-\cos\theta]_0^\pi \cdot \left[ \frac{r^3}{3} \right]_0^R \\
&= 2 \cdot \frac{R^3}{3} \\
&= \frac{2R^3}{3}
\end{aligned}
$$

面密度 $\sigma = \dfrac{2M}{\pi R^2}$ を掛けて $M$ で割ります。

$$
y_G = \frac{\sigma}{M} \cdot \frac{2R^3}{3} = \frac{2}{\pi R^2} \cdot \frac{2R^3}{3} = \finalanswer{y_G = \frac{4R}{3\pi}}
$$

となります。

### (2)
$x$ 軸まわりの慣性モーメント $I_x$ の被積分関数は $y^2 = r^2 \sin^2\theta$ です。

$$
I_x = \sigma \int_0^\pi \sin^2\theta d\theta \int_0^R r^3 dr
$$

それぞれの定積分を計算します。半角の公式より $\int_0^\pi \sin^2\theta d\theta = \dfrac{\pi}{2}$ です。また動径方向は $\int_0^R r^3 dr = \dfrac{R^4}{4}$ です。

式をまとめます。

$$
I_x = \sigma \cdot \frac{\pi}{2} \cdot \frac{R^4}{4} = \left(\frac{2M}{\pi R^2}\right) \frac{\pi R^4}{8}
$$

約分すると次のようになります。

$$
\finalanswer{I_x = \frac{1}{4}MR^2}
$$

が得られます。

### (3)
平行軸の定理によれば，質量 $M$ の剛体について，ある軸まわりの慣性モーメント $I_x$ と，それと平行で重心を通る軸まわりの慣性モーメント $I_G$ の間には次の関係が成り立ちます。

$$
I_x = I_G + M y_G^2
$$

これを $I_G$ について解きます。

$$
I_G = I_x - M y_G^2
$$

(1) と (2) の結果を代入します。

$$
\begin{aligned}
I_G &= \frac{1}{4}MR^2 - M \left(\frac{4R}{3\pi}\right)^2 \\
&= \finalanswer{I_G = MR^2 \left( \frac{1}{4} - \frac{16}{9\pi^2} \right)}
\end{aligned}
$$

です。

===== FILE: 14calculus/06/06_060.md =====
---
tags:
  - 発展
---

# 重積分の物理への応用

## 問題
半径 $R$，総質量 $M$ の一様な薄い球殻がある。球殻の中心を原点にとり，外部の点 $P(0, 0, z)$（$z > R$）に質量 $m$ の質点を置く。球殻の面密度を $\sigma = \frac{M}{4\pi R^2}$，万有引力定数を $G$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 原点 O を中心とする半径 R の薄い球殻を描く。z 軸上に中心からの距離 z (z > R) の位置にある点 P を置く。球殻上の点 Q の球座標 (R, theta, phi) を示し，点 Q と点 P の間の距離を s とする。線分 OP と OQ のなす角を theta とする。 -->

(1) 球面上の点 $Q(R\sin\theta\cos\phi, R\sin\theta\sin\phi, R\cos\theta)$ と点 $P$ との距離 $s$ を，$R, z, \theta$ を用いて表せ。

(2) 球殻の微小面素 $dS = R^2\sin\theta \, d\theta d\phi$ がつくる万有引力のポテンシャルエネルギーを球殻全体で積分し，点 $P$ の質点が球殻から受ける全ポテンシャルエネルギー $U(z)$ を求めよ。ただし，無限遠を基準（$U \to 0$）とする。

(3) 質点が受ける万有引力 $\boldsymbol{F}$ をポテンシャルの勾配 $\boldsymbol{F} = -\frac{dU}{dz}\boldsymbol{e}_z$ から求めよ。

---

## 解答・解説

<div class="approach" markdown>
球殻上の微小面素からの寄与を足し合わせるため，余弦定理による幾何学的距離を導入して面積分を計算します。角度変数を距離変数へと置換積分することで，球殻外部における引力ポテンシャルが中心に全質量が集まった場合と等価になることを導きます。
</div>

### (1)
点 $Q$ と点 $P(0, 0, z)$ の座標の差から距離 $s$ の2乗を計算します。

$$
s^2 = (R\sin\theta\cos\phi)^2 + (R\sin\theta\sin\phi)^2 + (z - R\cos\theta)^2
$$

第1項と第2項をまとめると $R^2\sin^2\theta$ となります。第3項を展開します。

$$
\begin{aligned}
s^2 &= R^2\sin^2\theta + z^2 - 2Rz\cos\theta + R^2\cos^2\theta \\
&= R^2 + z^2 - 2Rz\cos\theta
\end{aligned}
$$

$s > 0$ であるため，正の平方根をとります。

$$
\finalanswer{s = \sqrt{R^2 + z^2 - 2Rz\cos\theta}}
$$

となります。

### (2)
微小面素の質量は $dM = \sigma dS = \sigma R^2\sin\theta \, d\theta d\phi$ です。これが点 $P$ の質点につくるポテンシャルエネルギーは次式で与えられます。

$$
dU = -\frac{G m \, dM}{s} = -\frac{Gm\sigma R^2\sin\theta}{s} d\theta d\phi
$$

$\phi$ は被積分関数に含まれないため，$\phi$ の積分は単に $2\pi$ となります。

$$
U(z) = -2\pi Gm\sigma R^2 \int_0^\pi \frac{\sin\theta}{\sqrt{R^2 + z^2 - 2Rz\cos\theta}} d\theta
$$

ここで $u = s^2 = R^2 + z^2 - 2Rz\cos\theta$ とおいて置換積分を行います。両辺を微分すると $du = 2Rz\sin\theta d\theta$ となります。

積分の上下端は，$\theta = 0$ のとき $u = (z - R)^2$（$s = z - R$），$\theta = \pi$ のとき $u = (z + R)^2$（$s = z + R$）です。$z > R$ であることに注意します。

$$
\int_0^\pi \frac{\sin\theta}{s} d\theta = \int_{z-R}^{z+R} \frac{1}{s} \cdot \frac{s \, ds}{Rz} = \frac{1}{Rz} \int_{z-R}^{z+R} 1 \, ds = \frac{(z+R) - (z-R)}{Rz} = \frac{2}{z}
$$

これを $U(z)$ の式に代入します。

$$
U(z) = -2\pi Gm\sigma R^2 \cdot \frac{2}{z} = -\frac{4\pi R^2 \sigma G m}{z}
$$

球殻の総質量が $M = 4\pi R^2 \sigma$ であることを用いると，次の式が得られます。

$$
\finalanswer{U(z) = -\frac{GMm}{z}}
$$

です。

### (3)
保存力の定義 $\boldsymbol{F} = -\dfrac{dU}{dz}\boldsymbol{e}_z$ に従って力を計算します。

$$
\frac{dU}{dz} = \frac{d}{dz}\left( -\frac{GMm}{z} \right) = \frac{GMm}{z^2}
$$

したがって，質点が受ける力は次のようになります。

$$
\finalanswer{\boldsymbol{F} = -\frac{GMm}{z^2}\boldsymbol{e}_z}
$$

となります。球殻の外部にいる質点に対して，球殻の質量があたかも原点にすべて集中しているかのように万有引力が作用することがわかります。

===== END =====