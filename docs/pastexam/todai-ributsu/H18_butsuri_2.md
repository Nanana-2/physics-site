---
title: 東大理物 平成18年度 物理学 第2問：黒体輻射のプランク分布とウィーンの変位則
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成18年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成18年度 物理学 第2問：黒体輻射のプランク分布とウィーンの変位則

## 問題

一辺の長さが $L$ の立方体の箱があって，絶対温度 $T$ の熱浴に接しているとする。箱の中に存在する電磁波が熱浴と熱平衡になっている場合を考える。ただし，ボルツマン定数を $k_{\mathrm{B}}$ とし，$\hbar = h/2\pi$ とする。

(1) 箱の中の異なる角振動数を持つ電磁波は，お互いに独立に振る舞うと考えられる。さらに，ある角振動数 $\omega$ を持つ電磁波は，同じ角振動数を持つ量子力学的な調和振動子として扱うことができる。絶対温度 $T$ の場合に，角振動数 $\omega$ の調和振動子の分配関数を求めよ。

(2) 設問1の調和振動子の平均エネルギーを求めよ。さらに，非常に低温の場合と非常に高温の場合に，平均エネルギーはどのような温度依存性を持つか調べ，その結果について物理的内容を簡潔に説明せよ。

(3) 電磁波は箱の中で定在波を作る。壁の位置で節を作るとして，電磁波の波数 $\vec{k} = (k_x, k_y, k_z)$ のとり得る値を求めよ。

(4) 波数 $\vec{k}$ を持つ電磁波の角振動数は，$k = |\vec{k}|$ として $\omega = ck$ で与えられる。ここで $c$ は光速度である。箱内の電磁波の持つ全エネルギーは，すべてのとり得る角振動数についての和として書ける。このとき，全エネルギー $E$ を

$$
E = \int_{0}^{\infty} \varepsilon(k)\,\mathrm{d}k
$$

という形に表したときの $\varepsilon(k)$ を求めよ。ただし，箱の一辺の長さ $L$ は十分長いとして，固有振動についての和を積分の形にしてよい。また，零点振動のエネルギーは無視せよ。（電磁波は横波であり，横波の偏光の方向が2通りあることも考慮せよ。）

(5) 全エネルギー $E$ が，どのような温度のべき乗則に従うか求めよ。

(6) 非常に低温の場合に，設問4で得られた $\varepsilon(k)$ が極大になる $k_{\max}$ の表式を求めよ。絶対温度が $2.7\,\mathrm{K}$ のとき，$k_{\max}$ の波数を持つ電磁波の波長を求めよ。ただし $\hbar = 1.0\times 10^{-34}\,\mathrm{J\,s}$，$c = 3.0\times 10^{8}\,\mathrm{m/s}$，$k_{\mathrm{B}} = 1.4\times 10^{-23}\,\mathrm{J/K}$ を用いて，有効数字2桁で答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成18年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
空洞内の電磁波は，定在波の波数と偏光で指定される独立な量子調和振動子の集まりとして表すことができます。1つの振動子のエネルギー準位は $\hbar\omega$ 刻みで等間隔なので，分配関数は等比級数としてまとまり，平均エネルギーを対数微分で求めることができます。

箱の一辺 $L$ が十分大きいときは，離散的な波数の和を波数空間の積分に置き換えることができます。無次元変数 $x = \hbar c k / (k_{\mathrm{B}}T)$ で積分を書き換えると，定積分の値によらず全エネルギーの温度依存性を直接読み取ることができます。
</div>

### (1)

角振動数 $\omega$ の量子調和振動子のエネルギー固有値は，$n = 0, 1, 2, \dots$ に対して $E_n = \hbar\omega\left(n + \dfrac{1}{2}\right)$ です。$\beta = \dfrac{1}{k_{\mathrm{B}}T}$ とおいて分配関数 $Z$ を計算します。

$$
\begin{aligned}
Z &= \sum_{n=0}^{\infty} e^{-\beta\hbar\omega(n + 1/2)} \\
&= e^{-\beta\hbar\omega/2}\sum_{n=0}^{\infty} \bigl(e^{-\beta\hbar\omega}\bigr)^n \\
&= \frac{e^{-\beta\hbar\omega/2}}{1 - e^{-\beta\hbar\omega}} \\
&= \frac{1}{2\sinh\!\left(\dfrac{\hbar\omega}{2k_{\mathrm{B}}T}\right)}
\end{aligned}
$$

したがって，分配関数は次式となります。

$$
\finalanswer{Z = \frac{e^{-\hbar\omega/(2k_{\mathrm{B}}T)}}{1 - e^{-\hbar\omega/(k_{\mathrm{B}}T)}} = \frac{1}{2\sinh\!\left(\dfrac{\hbar\omega}{2k_{\mathrm{B}}T}\right)}}
$$

### (2)

平均エネルギー $\langle\varepsilon\rangle$ は $-\dfrac{\partial\ln Z}{\partial\beta}$ から計算します。まず $\ln Z = -\dfrac{1}{2}\beta\hbar\omega - \ln\bigl(1 - e^{-\beta\hbar\omega}\bigr)$ を $\beta$ で微分します。

$$
\begin{aligned}
\langle\varepsilon\rangle &= -\frac{\partial\ln Z}{\partial\beta} \\
&= \frac{1}{2}\hbar\omega + \frac{\hbar\omega e^{-\beta\hbar\omega}}{1 - e^{-\beta\hbar\omega}} \\
&= \frac{1}{2}\hbar\omega + \frac{\hbar\omega}{e^{\beta\hbar\omega} - 1}
\end{aligned}
$$

したがって，平均エネルギーは次式となります。

$$
\finalanswer{\langle\varepsilon\rangle = \frac{1}{2}\hbar\omega + \frac{\hbar\omega}{e^{\hbar\omega/(k_{\mathrm{B}}T)} - 1}}
$$

非常に低温の場合，すなわち $k_{\mathrm{B}}T \ll \hbar\omega$ のときは $e^{\beta\hbar\omega} \gg 1$ なので，次のように近似することができます。

$$
\langle\varepsilon\rangle \simeq \frac{1}{2}\hbar\omega + \hbar\omega e^{-\hbar\omega/(k_{\mathrm{B}}T)}
$$

熱エネルギー $k_{\mathrm{B}}T$ がエネルギー準位の間隔 $\hbar\omega$ より十分小さいため，励起状態への熱励起は指数関数的に抑えられます。そのため平均エネルギーは温度によらない零点振動のエネルギー $\dfrac{1}{2}\hbar\omega$ に近づきます。

非常に高温の場合，すなわち $k_{\mathrm{B}}T \gg \hbar\omega$ のときは $\beta\hbar\omega \ll 1$ なので，$e^{\beta\hbar\omega} - 1 \simeq \beta\hbar\omega + \dfrac{1}{2}(\beta\hbar\omega)^2$ と展開します。

$$
\begin{aligned}
\langle\varepsilon\rangle &\simeq \frac{1}{2}\hbar\omega + \frac{\hbar\omega}{\beta\hbar\omega\left(1 + \dfrac{1}{2}\beta\hbar\omega\right)} \\
&\simeq \frac{1}{2}\hbar\omega + \frac{1}{\beta}\left(1 - \frac{1}{2}\beta\hbar\omega\right) \\
&= k_{\mathrm{B}}T
\end{aligned}
$$

エネルギー準位の間隔 $\hbar\omega$ が熱エネルギー $k_{\mathrm{B}}T$ に比べて十分小さいため，エネルギーの離散性が目立たなくなり，平均エネルギーは温度 $T$ に比例して古典統計力学のエネルギー等分配則 $k_{\mathrm{B}}T$ に一致します。

### (3)

立方体の箱を $0 \le x, y, z \le L$ の領域にとります。各方向の壁 $x = 0, L$，$y = 0, L$，$z = 0, L$ で節を作る定在波は $\sin(k_x x)\sin(k_y y)\sin(k_z z)$ の形をとるため，境界条件は $\sin(k_x L) = \sin(k_y L) = \sin(k_z L) = 0$ です。$k_x, k_y, k_z$ の符号を変えても同じ定在波を表すため，独立な定在波の波数は正の整数 $n_x, n_y, n_z$ を用いて次のように表されます。

$$
\finalanswer{\vec{k} = \left(\frac{\pi}{L}n_x,\ \frac{\pi}{L}n_y,\ \frac{\pi}{L}n_z\right) \qquad (n_x, n_y, n_z = 1, 2, 3, \dots)}
$$

### (4)

波数空間の第1象限 $k_x, k_y, k_z > 0$ において，1つの波数ベクトル $\vec{k}$ が占める体積は $\left(\dfrac{\pi}{L}\right)^3$ です。半径が $k$ から $k + \mathrm{d}k$ の間の球殻のうち第1象限に含まれる体積は $\dfrac{1}{8}\cdot 4\pi k^2\,\mathrm{d}k = \dfrac{\pi}{2}k^2\,\mathrm{d}k$ なので，波数の大きさが $k$ から $k + \mathrm{d}k$ の間にある偏光を含めたモード数 $\mathrm{d}N(k)$ は，偏光の2通りを掛けて次式になります。

$$
\begin{aligned}
\mathrm{d}N(k) &= 2\cdot\frac{\dfrac{\pi}{2}k^2\,\mathrm{d}k}{\left(\dfrac{\pi}{L}\right)^3} \\
&= \frac{L^3}{\pi^2}k^2\,\mathrm{d}k
\end{aligned}
$$

設問2より零点振動のエネルギーを除いた1モードあたりの平均エネルギーは $\dfrac{\hbar\omega}{e^{\beta\hbar\omega} - 1} = \dfrac{\hbar ck}{e^{\hbar ck / (k_{\mathrm{B}}T)} - 1}$ です。これを $\mathrm{d}N(k)$ に掛けて積分すると全エネルギー $E$ になります。

$$
\begin{aligned}
E &= \int_{0}^{\infty} \frac{\hbar ck}{e^{\hbar ck/(k_{\mathrm{B}}T)} - 1}\cdot\frac{L^3}{\pi^2}k^2\,\mathrm{d}k \\
&= \int_{0}^{\infty} \frac{L^3 \hbar c}{\pi^2}\frac{k^3}{e^{\hbar ck/(k_{\mathrm{B}}T)} - 1}\,\mathrm{d}k
\end{aligned}
$$

したがって，$\varepsilon(k)$ は次式となります。

$$
\finalanswer{\varepsilon(k) = \frac{L^3 \hbar c}{\pi^2}\frac{k^3}{e^{\hbar ck/(k_{\mathrm{B}}T)} - 1}}
$$

### (5)

無次元変数 $x = \dfrac{\hbar ck}{k_{\mathrm{B}}T}$ を導入します。$k = \dfrac{k_{\mathrm{B}}T}{\hbar c}x$，$\mathrm{d}k = \dfrac{k_{\mathrm{B}}T}{\hbar c}\,\mathrm{d}x$ を設問4の $E$ の積分に代入します。

$$
\begin{aligned}
E &= \frac{L^3 \hbar c}{\pi^2}\int_{0}^{\infty} \left(\frac{k_{\mathrm{B}}T}{\hbar c}\right)^3 \frac{x^3}{e^x - 1}\cdot\frac{k_{\mathrm{B}}T}{\hbar c}\,\mathrm{d}x \\
&= \frac{L^3 k_{\mathrm{B}}^4}{\pi^2 \hbar^3 c^3}\left(\int_{0}^{\infty}\frac{x^3}{e^x - 1}\,\mathrm{d}x\right)T^4
\end{aligned}
$$

定積分 $\int_{0}^{\infty} \dfrac{x^3}{e^x - 1}\,\mathrm{d}x$ は温度 $T$ によらない正の定数です。したがって，全エネルギー $E$ は絶対温度 $T$ の4乗に比例します。

$$
\finalanswer{E \propto T^4}
$$

### (6)

非常に低温の場合には $e^{\hbar ck/(k_{\mathrm{B}}T)} \gg 1$ となるため，分母の $-1$ を無視して $\varepsilon(k)$ を次のように近似することができます。

$$
\varepsilon(k) \simeq \frac{L^3 \hbar c}{\pi^2} k^3 e^{-\hbar ck/(k_{\mathrm{B}}T)}
$$

この関数が極大となる $k = k_{\max}$ を求めるため，$k$ で微分して $0$ とおきます。

$$
\begin{aligned}
\frac{\mathrm{d}\varepsilon}{\mathrm{d}k} &= \frac{L^3 \hbar c}{\pi^2}\left(3k^2 - \frac{\hbar c}{k_{\mathrm{B}}T}k^3\right)e^{-\hbar ck/(k_{\mathrm{B}}T)} \\
&= \frac{L^3 \hbar c}{\pi^2}k^2\left(3 - \frac{\hbar ck}{k_{\mathrm{B}}T}\right)e^{-\hbar ck/(k_{\mathrm{B}}T)} = 0
\end{aligned}
$$

$k > 0$ より $3 - \dfrac{\hbar c k_{\max}}{k_{\mathrm{B}}T} = 0$ となり，$k_{\max}$ の表式は次式になります。

$$
k_{\max} = \frac{3k_{\mathrm{B}}T}{\hbar c}
$$

次に $T = 2.7\,\mathrm{K}$ における波長 $\lambda = \dfrac{2\pi}{k_{\max}}$ を計算します。

$$
\begin{aligned}
\lambda &= \frac{2\pi\hbar c}{3k_{\mathrm{B}}T} \\
&= \frac{2\pi \times 1.0\times 10^{-34} \times 3.0\times 10^{8}}{3 \times 1.4\times 10^{-23} \times 2.7} \\
&= \frac{2\pi \times 10^{-26}}{3.78\times 10^{-23}} \\
&\simeq 1.66\times 10^{-3}\,\mathrm{m}
\end{aligned}
$$

有効数字2桁で丸めると $\lambda = 1.7\times 10^{-3}\,\mathrm{m}$ となります。

$$
\finalanswer{k_{\max} = \frac{3k_{\mathrm{B}}T}{\hbar c}, \qquad \lambda = 1.7\times 10^{-3}\,\mathrm{m}}
$$

<aside class="rigor-note" markdown>
分母の $-1$ を無視せずに $\varepsilon(k)$ を直接微分すると，無次元変数 $x = \dfrac{\hbar c k_{\max}}{k_{\mathrm{B}}T}$ に対する方程式 $3 - x = 3e^{-x}$ が得られます。この正の解は数値的に $x \simeq 2.821$ であり，近似値 $x = 3$ との差は約 $6\%$ です。厳密解と問題文の定数を用いると波長は $\lambda \simeq 1.8\times 10^{-3}\,\mathrm{m}$ となります。
</aside>
