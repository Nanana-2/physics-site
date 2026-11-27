---
title: 東大理物 平成21年度 数学 第2問：2準位系の連立1階常微分方程式と遷移確率
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成21年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成21年度 数学 第2問：2準位系の連立1階常微分方程式と遷移確率

## 問題

実変数 $t$ の関数 $f_1(t), f_2(t)$ が次の連立1階常微分方程式を満たす。

$$
i\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix} f_1(t) \\ f_2(t) \end{pmatrix} = \begin{pmatrix} a(t) & b(t) \\ b(t) & c(t) \end{pmatrix}\begin{pmatrix} f_1(t) \\ f_2(t) \end{pmatrix} \tag{1}
$$

ただし $a(t), b(t), c(t)$ は $t$ の実関数であり，$i = \sqrt{-1}$ とする。

(1) $|f_1(t)|^2 + |f_2(t)|^2$ が $t$ に依存しないことを示せ。

(2) $f_1(t) = e^{-i\int_0^t a(\tau)\mathrm{d}\tau}\tilde{f}_1(t)$，$f_2(t) = e^{-i\int_0^t c(\tau)\mathrm{d}\tau}\tilde{f}_2(t)$ によって $\tilde{f}_1(t)$ と $\tilde{f}_2(t)$ を定義すると，これらが

$$
i\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix} \tilde{f}_1(t) \\ \tilde{f}_2(t) \end{pmatrix} = \begin{pmatrix} 0 & \tilde{b}(t) \\ \tilde{b}(t)^* & 0 \end{pmatrix}\begin{pmatrix} \tilde{f}_1(t) \\ \tilde{f}_2(t) \end{pmatrix}
$$

という形の常微分方程式を満たすことを示せ。またこのときの $\tilde{b}(t)$ の表式を求めよ。ただし $\tilde{b}(t)^*$ は $\tilde{b}(t)$ の複素共役を表す。

(3) $a(t) = c(t) = 0$ であり，$b(t)$ が定数 $b_0$ であるとする。式 (1) の解 $f_1(t)$ を，$b_0$ および $f_1(0), f_2(0)$ を用いて表せ。

(4) $a(t) = c(t) = 0$ であり，$b(t)$ は $t \to -\infty$ で十分はやく減衰する関数であるとする。このとき，式 (1) の解 $f_1(t)$ を，$b(t)$ および $f_1(-\infty), f_2(-\infty)$ を用いて表せ。ただし $f_1(-\infty) = \lim_{t \to -\infty} f_1(t)$ などである。

(5) 設問4で，$b(t)$ が正の定数 $\beta, \omega, t_0$ を用いて

$$
b(t) = \frac{\beta\cos\omega t}{t^2 + t_0^2}
$$

で与えられる場合を考える。$f_1(-\infty) = 1,\ f_2(-\infty) = 0$ のとき，$|f_1(+\infty)|^2,\ |f_2(+\infty)|^2$ の値を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成21年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
係数行列が実対称行列のとき，エルミート性によって解ベクトルのノルムの2乗は時間に依存せず保存されます。また対角成分は位相因子をくくり出す変換で消すことができ，非対角成分だけの連立方程式に書き換えることができます。

対角成分が $0$ の連立方程式では，2つの関数の和と差をとると互いに独立な1階微分方程式に分かれます。係数 $b(t)$ が時間に依存しても変数分離でそのまま積分でき，無限区間の積分は複素平面上の留数定理で求めることができます。
</div>

### (1)

式 (1) を成分ごとに書くと，次の2式になります。

$$
i\dot{f}_1 = a f_1 + b f_2, \qquad i\dot{f}_2 = b f_1 + c f_2
$$

ここでドットは $t$ による微分を表します。$a, b, c$ は実関数なので，両辺の複素共役をとると次式になります。

$$
-i\dot{f}_1^* = a f_1^* + b f_2^*, \qquad -i\dot{f}_2^* = b f_1^* + c f_2^*
$$

これを用いて $|f_1(t)|^2 + |f_2(t)|^2 = f_1^* f_1 + f_2^* f_2$ の時間微分を計算します。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t}\bigl(|f_1|^2 + |f_2|^2\bigr) &= \dot{f}_1^* f_1 + f_1^* \dot{f}_1 + \dot{f}_2^* f_2 + f_2^* \dot{f}_2 \\
&= i(a f_1^* + b f_2^*)f_1 - i f_1^*(a f_1 + b f_2) \\
&\quad + i(b f_1^* + c f_2^*)f_2 - i f_2^*(b f_1 + c f_2) \\
&= i\bigl(a|f_1|^2 + b f_2^* f_1 - a|f_1|^2 - b f_1^* f_2 + b f_1^* f_2 + c|f_2|^2 - b f_2^* f_1 - c|f_2|^2\bigr) \\
&= 0
\end{aligned}
$$

時間微分が恒等的に $0$ なので，$|f_1(t)|^2 + |f_2(t)|^2$ は $t$ に依存しません。

### (2)

$A(t) = \int_0^t a(\tau)\,\mathrm{d}\tau$，$C(t) = \int_0^t c(\tau)\,\mathrm{d}\tau$ とおくと，$f_1(t) = e^{-iA(t)}\tilde{f}_1(t)$，$f_2(t) = e^{-iC(t)}\tilde{f}_2(t)$ です。これらを $t$ で微分して $i$ を掛けます。

$$
\begin{aligned}
i\frac{\mathrm{d}f_1}{\mathrm{d}t} &= i\left(-ia(t)e^{-iA(t)}\tilde{f}_1 + e^{-iA(t)}\frac{\mathrm{d}\tilde{f}_1}{\mathrm{d}t}\right) \\
&= a(t)e^{-iA(t)}\tilde{f}_1 + ie^{-iA(t)}\frac{\mathrm{d}\tilde{f}_1}{\mathrm{d}t}
\end{aligned}
$$

同様に $f_2$ についても次式が得られます。

$$
i\frac{\mathrm{d}f_2}{\mathrm{d}t} = c(t)e^{-iC(t)}\tilde{f}_2 + ie^{-iC(t)}\frac{\mathrm{d}\tilde{f}_2}{\mathrm{d}t}
$$

これらを式 (1) の2つの式に代入します。

$$
\begin{aligned}
a(t)e^{-iA(t)}\tilde{f}_1 + ie^{-iA(t)}\frac{\mathrm{d}\tilde{f}_1}{\mathrm{d}t} &= a(t)e^{-iA(t)}\tilde{f}_1 + b(t)e^{-iC(t)}\tilde{f}_2 \\
c(t)e^{-iC(t)}\tilde{f}_2 + ie^{-iC(t)}\frac{\mathrm{d}\tilde{f}_2}{\mathrm{d}t} &= b(t)e^{-iA(t)}\tilde{f}_1 + c(t)e^{-iC(t)}\tilde{f}_2
\end{aligned}
$$

両辺の対角項を消してから，1つめの式に $e^{iA(t)}$，2つめの式に $e^{iC(t)}$ を掛けます。

$$
\begin{aligned}
i\frac{\mathrm{d}\tilde{f}_1}{\mathrm{d}t} &= b(t)e^{i(A(t) - C(t))}\tilde{f}_2 \\
i\frac{\mathrm{d}\tilde{f}_2}{\mathrm{d}t} &= b(t)e^{-i(A(t) - C(t))}\tilde{f}_1
\end{aligned}
$$

ここで $\tilde{b}(t) = b(t)e^{i(A(t) - C(t))}$ とおきます。$a, b, c$ は実関数なので $A(t), C(t)$ も実関数であり，$\tilde{b}(t)^* = b(t)e^{-i(A(t) - C(t))}$ です。よって行列の形で書くと次式を満たします。

$$
i\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix} \tilde{f}_1(t) \\ \tilde{f}_2(t) \end{pmatrix} = \begin{pmatrix} 0 & \tilde{b}(t) \\ \tilde{b}(t)^* & 0 \end{pmatrix}\begin{pmatrix} \tilde{f}_1(t) \\ \tilde{f}_2(t) \end{pmatrix}
$$

また，$\tilde{b}(t)$ の表式は次式となります。

$$
\finalanswer{\tilde{b}(t) = b(t)\exp\!\left(i\int_0^t \bigl(a(\tau) - c(\tau)\bigr)\,\mathrm{d}\tau\right)}
$$

### (3)

$a(t) = c(t) = 0$，$b(t) = b_0$ のとき，式 (1) は次の2式になります。

$$
i\frac{\mathrm{d}f_1}{\mathrm{d}t} = b_0 f_2, \qquad i\frac{\mathrm{d}f_2}{\mathrm{d}t} = b_0 f_1
$$

和 $g_+(t) = f_1(t) + f_2(t)$ と差 $g_-(t) = f_1(t) - f_2(t)$ を導入し，2式の和と差をとります。

$$
\begin{aligned}
i\frac{\mathrm{d}g_+}{\mathrm{d}t} &= b_0 g_+ \\
i\frac{\mathrm{d}g_-}{\mathrm{d}t} &= -b_0 g_-
\end{aligned}
$$

それぞれ積分すると，初期値 $g_\pm(0) = f_1(0) \pm f_2(0)$ を用いて次式が得られます。

$$
g_+(t) = \bigl(f_1(0) + f_2(0)\bigr)e^{-ib_0 t}, \qquad g_-(t) = \bigl(f_1(0) - f_2(0)\bigr)e^{ib_0 t}
$$

これより $f_1(t) = \dfrac{g_+(t) + g_-(t)}{2}$ を計算します。

$$
\begin{aligned}
f_1(t) &= \frac{1}{2}\Bigl(\bigl(f_1(0) + f_2(0)\bigr)e^{-ib_0 t} + \bigl(f_1(0) - f_2(0)\bigr)e^{ib_0 t}\Bigr) \\
&= f_1(0)\frac{e^{ib_0 t} + e^{-ib_0 t}}{2} - i f_2(0)\frac{e^{ib_0 t} - e^{-ib_0 t}}{2i} \\
&= f_1(0)\cos(b_0 t) - i f_2(0)\sin(b_0 t)
\end{aligned}
$$

したがって，解 $f_1(t)$ は次式となります。

$$
\finalanswer{f_1(t) = f_1(0)\cos(b_0 t) - i f_2(0)\sin(b_0 t)}
$$

### (4)

$a(t) = c(t) = 0$ のとき，式 (1) は

$$
i\frac{\mathrm{d}f_1}{\mathrm{d}t} = b(t)f_2, \qquad i\frac{\mathrm{d}f_2}{\mathrm{d}t} = b(t)f_1
$$

です。設問3と同様に $g_\pm(t) = f_1(t) \pm f_2(t)$ とおくと，次式が得られます。

$$
\begin{aligned}
\frac{\mathrm{d}g_+}{\mathrm{d}t} &= -i b(t) g_+ \\
\frac{\mathrm{d}g_-}{\mathrm{d}t} &= i b(t) g_-
\end{aligned}
$$

$b(t)$ は $t \to -\infty$ で十分はやく減衰するため，積分 $\Phi(t) = \int_{-\infty}^{t} b(\tau)\,\mathrm{d}\tau$ が収束します。各微分方程式を $-\infty$ から $t$ まで積分します。

$$
\begin{aligned}
g_+(t) &= g_+(-\infty)e^{-i\Phi(t)} = \bigl(f_1(-\infty) + f_2(-\infty)\bigr)e^{-i\Phi(t)} \\
g_-(t) &= g_-(-\infty)e^{i\Phi(t)} = \bigl(f_1(-\infty) - f_2(-\infty)\bigr)e^{i\Phi(t)}
\end{aligned}
$$

$f_1(t) = \dfrac{g_+(t) + g_-(t)}{2}$ に代入して整理します。

$$
\begin{aligned}
f_1(t) &= \frac{1}{2}\Bigl(\bigl(f_1(-\infty) + f_2(-\infty)\bigr)e^{-i\Phi(t)} + \bigl(f_1(-\infty) - f_2(-\infty)\bigr)e^{i\Phi(t)}\Bigr) \\
&= f_1(-\infty)\frac{e^{i\Phi(t)} + e^{-i\Phi(t)}}{2} - i f_2(-\infty)\frac{e^{i\Phi(t)} - e^{-i\Phi(t)}}{2i} \\
&= f_1(-\infty)\cos\Phi(t) - i f_2(-\infty)\sin\Phi(t)
\end{aligned}
$$

したがって，解 $f_1(t)$ は次式となります。

$$
\finalanswer{f_1(t) = f_1(-\infty)\cos\!\left(\int_{-\infty}^{t} b(\tau)\,\mathrm{d}\tau\right) - i f_2(-\infty)\sin\!\left(\int_{-\infty}^{t} b(\tau)\,\mathrm{d}\tau\right)}
$$

### (5)

$f_1(-\infty) = 1$，$f_2(-\infty) = 0$ を設問4の結果に代入すると，$f_1(t) = \cos\Phi(t)$ です。また設問1より $|f_1(t)|^2 + |f_2(t)|^2 = |f_1(-\infty)|^2 + |f_2(-\infty)|^2 = 1$ なので，$|f_2(t)|^2 = 1 - |f_1(t)|^2 = \sin^2\Phi(t)$ となります。

ここで $\Phi(+\infty)$ を求めます。

$$
\Phi(+\infty) = \int_{-\infty}^{\infty} \frac{\beta\cos\omega t}{t^2 + t_0^2}\,\mathrm{d}t
$$

$\dfrac{\beta\sin\omega t}{t^2 + t_0^2}$ は奇関数なので積分が $0$ です。よって，複素積分として次のように書くことができます。

$$
\Phi(+\infty) = \int_{-\infty}^{\infty} \frac{\beta e^{i\omega t}}{t^2 + t_0^2}\,\mathrm{d}t
$$

複素変数 $z$ の関数 $h(z) = \dfrac{\beta e^{i\omega z}}{z^2 + t_0^2}$ を考えます。半径 $R > t_0$ に対して，実軸上の区間 $[-R, R]$ と上半平面の半円弧 $C_R$（$z = Re^{i\theta},\ 0 \le \theta \le \pi$）からなる閉経路を反時計回りに積分します。

上半平面にある $h(z)$ の極は $z = it_0$ の1位の極のみです。$z = it_0$ での留数を求めます。

$$
\begin{aligned}
\operatorname{Res}_{z = it_0} h(z) &= \lim_{z \to it_0} (z - it_0)\frac{\beta e^{i\omega z}}{(z - it_0)(z + it_0)} \\
&= \frac{\beta e^{i\omega(it_0)}}{2it_0} \\
&= \frac{\beta e^{-\omega t_0}}{2it_0}
\end{aligned}
$$

一方，$\omega > 0$ のとき半円弧 $C_R$ 上では $|e^{i\omega z}| = e^{-\omega R\sin\theta} \le 1$ であり，$|z^2 + t_0^2| \ge R^2 - t_0^2$ なので，半円弧上の積分は次のように上から抑えることができます。

$$
\begin{aligned}
\left|\int_{C_R} \frac{\beta e^{i\omega z}}{z^2 + t_0^2}\,\mathrm{d}z\right| &\le \int_0^\pi \frac{\beta}{R^2 - t_0^2} R\,\mathrm{d}\theta \\
&= \frac{\pi\beta R}{R^2 - t_0^2} \xrightarrow{R \to \infty} 0
\end{aligned}
$$

したがって，留数定理より $R \to \infty$ の極限をとって次式が得られます。

$$
\begin{aligned}
\Phi(+\infty) &= 2\pi i \cdot \frac{\beta e^{-\omega t_0}}{2it_0} \\
&= \frac{\pi\beta}{t_0}e^{-\omega t_0}
\end{aligned}
$$

以上より，$|f_1(+\infty)|^2$ と $|f_2(+\infty)|^2$ の値は次式となります。

$$
\finalanswer{|f_1(+\infty)|^2 = \cos^2\!\left(\frac{\pi\beta}{t_0}e^{-\omega t_0}\right), \qquad |f_2(+\infty)|^2 = \sin^2\!\left(\frac{\pi\beta}{t_0}e^{-\omega t_0}\right)}
$$
