===== FILE: 10integral_transforms/04/04_010.md =====
---
tags:
  - 標準
---

# 強制振動とフーリエ変換

## 問題
質量 $m$，減衰係数 $\gamma$，ばね定数 $k$ の減衰振動子に外力 $f(t)$ が加わるとき，変位 $x(t)$ が満たす運動方程式は次式で与えられる。
$$
m \frac{d^2 x}{dt^2} + \gamma \frac{dx}{dt} + k x = f(t)
$$
変位 $x(t)$ および外力 $f(t)$ のフーリエ変換を
$$
\tilde{x}(\omega) = \int_{-\infty}^\infty x(t) e^{-i\omega t} dt, \quad \tilde{f}(\omega) = \int_{-\infty}^\infty f(t) e^{-i\omega t} dt
$$
と定義する。以下の問いに答えよ。

(1) 運動方程式の両辺をフーリエ変換することにより，$\tilde{x}(\omega) = \chi(\omega) \tilde{f}(\omega)$ の関係を満たす複素感受率 $\chi(\omega)$ を求めよ。

(2) 外力として角振動数 $\omega$ の余弦波 $f(t) = f_0 \cos(\omega t)$（$f_0 > 0$）が長時間加わっているときの定常解を $x(t) = A(\omega) \cos(\omega t - \delta(\omega))$ と表す。振幅 $A(\omega)$ を $m, \gamma, k, \omega, f_0$ を用いて求めよ。ただし $A(\omega) > 0$ とする。

(3) 複素感受率を実部と虚部に分けて $\chi(\omega) = \chi'(\omega) - i \chi''(\omega)$ と定義するとき，$\chi''(\omega)$ を求めよ。また，外力が振動子に対して1周期あたりになす仕事 $W = \int_0^{2\pi/\omega} f(t) \frac{dx}{dt} dt$ を $\chi''(\omega)$ を用いて表せ。

---

## 解答・解説

### (1)
フーリエ変換の微分の性質を用います。変位 $x(t)$ の時間微分に関するフーリエ変換は，部分積分によりそれぞれ次のように表されます。
$$
\begin{aligned}
\int_{-\infty}^\infty \frac{dx}{dt} e^{-i\omega t} dt &= i\omega \tilde{x}(\omega) \\
\int_{-\infty}^\infty \frac{d^2 x}{dt^2} e^{-i\omega t} dt &= (i\omega)^2 \tilde{x}(\omega) = -\omega^2 \tilde{x}(\omega)
\end{aligned}
$$
運動方程式の両辺をフーリエ変換すると，
$$
\left(-m\omega^2 + i\gamma\omega + k\right) \tilde{x}(\omega) = \tilde{f}(\omega)
$$
となります。両辺を整理して $\tilde{x}(\omega) = \chi(\omega) \tilde{f}(\omega)$ の形に変形すると，
$$
\finalanswer{\chi(\omega) = \frac{1}{-m\omega^2 + i\gamma\omega + k}}
$$
となります。

### (2)
外力 $f(t) = f_0 \cos(\omega t)$ を複素表示の実部 $f(t) = \mathrm{Re}[f_0 e^{i\omega t}]$ として扱います。線形系の定常解は，複素感受率を用いて次のように表されます。
$$
x(t) = \mathrm{Re}\left[\chi(\omega) f_0 e^{i\omega t}\right]
$$
振幅 $A(\omega)$ は複素感受率の絶対値に比例するため，
$$
A(\omega) = f_0 |\chi(\omega)|
$$
となります。複素感受率の絶対値を計算すると，
$$
\begin{aligned}
|\chi(\omega)| &= \frac{1}{|(k - m\omega^2) + i\gamma\omega|} \\
&= \frac{1}{\sqrt{(k - m\omega^2)^2 + \gamma^2 \omega^2}}
\end{aligned}
$$
が得られます。したがって，振幅は
$$
\finalanswer{A(\omega) = \frac{f_0}{\sqrt{(k - m\omega^2)^2 + \gamma^2 \omega^2}}}
$$
となります。

### (3)
複素感受率の分母を有理化して実部と虚部に分解します。
$$
\begin{aligned}
\chi(\omega) &= \frac{1}{(k - m\omega^2) + i\gamma\omega} \\
&= \frac{(k - m\omega^2) - i\gamma\omega}{(k - m\omega^2)^2 + \gamma^2 \omega^2}
\end{aligned}
$$
定義 $\chi(\omega) = \chi'(\omega) - i \chi''(\omega)$ と比較すると，虚部 $\chi''(\omega)$ は
$$
\finalanswer{\chi''(\omega) = \frac{\gamma\omega}{(k - m\omega^2)^2 + \gamma^2 \omega^2}}
$$
となります。

次に1周期あたりの仕事を求めます。定常変位は
$$
\begin{aligned}
x(t) &= \mathrm{Re}\left[(\chi' - i\chi'') f_0 (\cos\omega t + i\sin\omega t)\right] \\
&= f_0 \left(\chi'\cos\omega t + \chi''\sin\omega t\right)
\end{aligned}
$$
と展開できるため，速度は
$$
\frac{dx}{dt} = \omega f_0 \left(-\chi'\sin\omega t + \chi''\cos\omega t\right)
$$
となります。これを仕事の表式に代入して1周期にわたって積分します。三角関数の直交性
$$
\begin{aligned}
\int_0^{2\pi/\omega} \cos^2(\omega t) dt &= \frac{\pi}{\omega} \\
\int_0^{2\pi/\omega} \cos(\omega t) \sin(\omega t) dt &= 0
\end{aligned}
$$
を用いると，仕事は
$$
\begin{aligned}
W &= \int_0^{2\pi/\omega} f_0 \cos(\omega t) \cdot \omega f_0 \left(-\chi'\sin\omega t + \chi''\cos\omega t\right) dt \\
&= \omega f_0^2 \chi''(\omega) \frac{\pi}{\omega} \\
&= \finalanswer{W = \pi f_0^2 \chi''(\omega)}
\end{aligned}
$$
となります。エネルギー散逸が応答関数の虚部によって直接決定されることを意味します。

===== FILE: 10integral_transforms/04/04_020.md =====
---
tags:
  - 標準
---

# 熱方程式の解法

## 問題
1次元無限領域 $-\infty < x < \infty$ における温度分布 $u(x, t)$ は，熱拡散率 $D > 0$ の熱伝導方程式
$$
\frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}
$$
に従う。空間変数 $x$ に関するフーリエ変換とその逆変換を
$$
\tilde{u}(k, t) = \int_{-\infty}^\infty u(x, t) e^{-ikx} dx, \quad u(x, t) = \frac{1}{2\pi} \int_{-\infty}^\infty \tilde{u}(k, t) e^{ikx} dk
$$
とする。以下の問いに答えよ。

(1) 熱方程式の両辺をフーリエ変換することにより，$\tilde{u}(k, t)$ が満たす時間 $t$ に関する微分方程式を導き，初期条件 $\tilde{u}(k, 0) = \tilde{f}(k)$ のもとで $\tilde{u}(k, t)$ を求めよ。

(2) ガウス積分の公式
$$
\frac{1}{2\pi} \int_{-\infty}^\infty e^{-a k^2} e^{ikx} dk = \frac{1}{\sqrt{4\pi a}} \exp\left(-\frac{x^2}{4a}\right) \quad (a > 0)
$$
を用いて，熱核（基本解）$G(x, t) = \frac{1}{2\pi} \int_{-\infty}^\infty e^{-D k^2 t} e^{ikx} dk$ を計算せよ。

(3) 初期条件が $u(x, 0) = Q \delta(x)$（$Q$ は正の定数，$\delta(x)$ はディラックのデルタ関数）で与えられるとき，時刻 $t > 0$ における温度分布 $u(x, t)$ を求めよ。また，全熱量 $\int_{-\infty}^\infty u(x, t) dx$ を求めよ。

---

## 解答・解説

### (1)
空間微分に関するフーリエ変換を実行します。部分積分により
$$
\int_{-\infty}^\infty \frac{\partial^2 u}{\partial x^2} e^{-ikx} dx = (ik)^2 \tilde{u}(k, t) = -k^2 \tilde{u}(k, t)
$$
となるため，熱方程式の両辺をフーリエ変換すると，
$$
\frac{\partial \tilde{u}}{\partial t} = -D k^2 \tilde{u}(k, t)
$$
が得られます。これは $\tilde{u}$ に関する1階の常微分方程式であり，初期条件 $\tilde{u}(k, 0) = \tilde{f}(k)$ を適用して解くと，
$$
\finalanswer{\tilde{u}(k, t) = \tilde{f}(k) e^{-D k^2 t}}
$$
となります。

### (2)
与えられた熱核の定義式
$$
G(x, t) = \frac{1}{2\pi} \int_{-\infty}^\infty e^{-D t k^2} e^{ikx} dk
$$
に対して，公式のパラメータを $a = Dt$ と対応させます。$t > 0$ において $a > 0$ であるため，公式を直接適用すると，
$$
\finalanswer{G(x, t) = \frac{1}{\sqrt{4\pi D t}} \exp\left(-\frac{x^2}{4Dt}\right)}
$$
となります。

### (3)
初期条件 $u(x, 0) = Q \delta(x)$ をフーリエ変換すると，
$$
\tilde{f}(k) = \int_{-\infty}^\infty Q \delta(x) e^{-ikx} dx = Q
$$
となります。(1) の結果より波数空間の解は
$$
\tilde{u}(k, t) = Q e^{-D k^2 t}
$$
となるため，これを逆フーリエ変換します。(2) で求めた熱核 $G(x, t)$ を用いると，温度分布は
$$
u(x, t) = Q G(x, t) = \finalanswer{u(x, t) = \frac{Q}{\sqrt{4\pi D t}} \exp\left(-\frac{x^2}{4Dt}\right)}
$$
となります。

全熱量を求めるため，この分布を全空間で積分します。
$$
\int_{-\infty}^\infty u(x, t) dx = \frac{Q}{\sqrt{4\pi D t}} \int_{-\infty}^\infty \exp\left(-\frac{x^2}{4Dt}\right) dx
$$
ここでガウス積分の公式 $\int_{-\infty}^\infty e^{-\alpha x^2} dx = \sqrt{\pi/\alpha}$ において $\alpha = 1/(4Dt)$ と置くと，空間積分は $\sqrt{4\pi Dt}$ となります。したがって，全熱量は
$$
\int_{-\infty}^\infty u(x, t) dx = \frac{Q}{\sqrt{4\pi D t}} \cdot \sqrt{4\pi D t} = \finalanswer{\int_{-\infty}^\infty u(x, t) dx = Q}
$$
となります。熱が拡散しても全体の熱量が一定に保存されることを示しています。

===== FILE: 10integral_transforms/04/04_030.md =====
---
tags:
  - 発展
---

# ポアソン方程式のグリーン関数

## 問題
3次元空間全域におけるポアソン方程式に対するグリーン関数 $G(\boldsymbol{r})$ は次の方程式を満たす。
$$
-\nabla^2 G(\boldsymbol{r}) = \delta(\boldsymbol{r})
$$
3次元フーリエ変換とその逆変換を
$$
\tilde{G}(\boldsymbol{k}) = \int G(\boldsymbol{r}) e^{-i \boldsymbol{k}\cdot\boldsymbol{r}} d^3r, \quad G(\boldsymbol{r}) = \frac{1}{(2\pi)^3} \int \tilde{G}(\boldsymbol{k}) e^{i \boldsymbol{k}\cdot\boldsymbol{r}} d^3k
$$
と定義する。以下の問いに答えよ。

(1) 方程式の両辺をフーリエ変換することにより，$\tilde{G}(\boldsymbol{k})$ を求めよ。ただし $k = |\boldsymbol{k}|$ とする。

(2) 波数ベクトル $\boldsymbol{k}$ に対する3次元極座標 $(k, \theta, \phi)$（極軸を $\boldsymbol{r}$ の向きにとる）を導入し，逆変換の立体角積分を実行することにより，$G(\boldsymbol{r})$ を $k$ に関する1重積分として表せ。ただし $r = |\boldsymbol{r}|$ とする。

(3) ディリクレ積分の公式 $\int_0^\infty \frac{\sin x}{x} dx = \frac{\pi}{2}$ を用いて (2) の積分を計算し，グリーン関数 $G(\boldsymbol{r})$ を求めよ。

---

## 解答・解説

### (1)
ラプラシアンのフーリエ変換を行います。部分積分を適用すると，
$$
\int \nabla^2 G(\boldsymbol{r}) e^{-i \boldsymbol{k}\cdot\boldsymbol{r}} d^3r = -k^2 \tilde{G}(\boldsymbol{k})
$$
となります。また，デルタ関数のフーリエ変換は
$$
\int \delta(\boldsymbol{r}) e^{-i \boldsymbol{k}\cdot\boldsymbol{r}} d^3r = 1
$$
です。方程式 $-\nabla^2 G(\boldsymbol{r}) = \delta(\boldsymbol{r})$ の両辺をフーリエ変換すると，
$$
k^2 \tilde{G}(\boldsymbol{k}) = 1
$$
が得られます。したがって，波数空間のグリーン関数は
$$
\finalanswer{\tilde{G}(\boldsymbol{k}) = \frac{1}{k^2}}
$$
となります。

### (2)
3次元逆フーリエ変換の積分を実行します。
$$
G(\boldsymbol{r}) = \frac{1}{(2\pi)^3} \int \frac{1}{k^2} e^{i \boldsymbol{k}\cdot\boldsymbol{r}} d^3k
$$
極軸を空間ベクトル $\boldsymbol{r}$ の方向にとると，$\boldsymbol{k}\cdot\boldsymbol{r} = kr\cos\theta$ と表され，体積要素は $d^3k = k^2 \sin\theta dk d\theta d\phi$ となります。角度成分の積分を実行すると，
$$
\int_0^{2\pi} d\phi = 2\pi
$$
および
$$
\begin{aligned}
\int_0^\pi e^{i kr\cos\theta} \sin\theta d\theta &= \left[-\frac{e^{i kr\cos\theta}}{ikr}\right]_0^\pi \\
&= \frac{e^{ikr} - e^{-ikr}}{ikr} \\
&= \frac{2\sin(kr)}{kr}
\end{aligned}
$$
が得られます。これらを元の式に代入すると，
$$
\begin{aligned}
G(\boldsymbol{r}) &= \frac{1}{(2\pi)^3} \int_0^\infty dk k^2 \frac{1}{k^2} \cdot 2\pi \cdot \frac{2\sin(kr)}{kr} \\
&= \finalanswer{G(\boldsymbol{r}) = \frac{1}{2\pi^2 r} \int_0^\infty \frac{\sin(kr)}{k} dk}
\end{aligned}
$$
となります。

### (3)
(2) で得られた積分において変数変換を行います。$x = kr$ と置くと，$dk/k = dx/x$ となるため，積分範囲を変えずに
$$
\int_0^\infty \frac{\sin(kr)}{k} dk = \int_0^\infty \frac{\sin x}{x} dx
$$
と書き直せます。ディリクレ積分の公式 $\int_0^\infty \frac{\sin x}{x} dx = \frac{\pi}{2}$ を適用すると，
$$
\begin{aligned}
G(\boldsymbol{r}) &= \frac{1}{2\pi^2 r} \cdot \frac{\pi}{2} \\
&= \finalanswer{G(\boldsymbol{r}) = \frac{1}{4\pi r}}
\end{aligned}
$$
となります。静電気学における点電荷のクーロンポテンシャルの表式と一致します。

===== FILE: 10integral_transforms/04/04_040.md =====
---
tags:
  - 標準
---

# 単スリットの回折

## 問題
波長 $\lambda$ の単色平行光が，幅 $a$ の単スリットに垂直に入射している（図）。開口面を $x$ 軸上にとり，開口関数を次式で定義する。
$$
g(x) = \begin{cases} 1 & (|x| \le a/2) \\ 0 & (|x| > a/2) \end{cases}
$$
回折角を $\theta$ とし，波数 $k = 2\pi/\lambda$ に対する空間周波数を $k_x = k \sin\theta$ とする。以下の問いに答えよ。

<!-- FIGURE problem: スリット幅 a の開口が x 軸上の -a/2 から a/2 に配置され，左から波長 lambda の平行光が入射している見取り図。右側に回折角 theta の光線が描かれている。 -->

(1) 回折波の複素振幅を与える開口関数のフーリエ変換 $U(k_x) = \int_{-\infty}^\infty g(x) e^{-ik_x x} dx$ を求めよ。

(2) 回折強度 $I(k_x) = |U(k_x)|^2$ を求め，中心の強度 $I_0 = I(0)$ を用いて表せ。

(3) 回折強度が $I(k_x) = 0$ となる最小の正の回折角 $\theta_1$ に対し，$\sin\theta_1$ を求めよ。また，第1副極大（$k_x a / 2 \approx 3\pi/2$）における強度 $I_1$ と中心強度 $I_0$ の比 $I_1 / I_0$ を求めよ。

---

## 解答・解説

### (1)
開口関数の定義にしたがって有限区間の積分を計算します。
$$
\begin{aligned}
U(k_x) &= \int_{-a/2}^{a/2} e^{-ik_x x} dx \\
&= \left[\frac{e^{-ik_x x}}{-ik_x}\right]_{-a/2}^{a/2} \\
&= \frac{e^{-ik_x a/2} - e^{ik_x a/2}}{-ik_x}
\end{aligned}
$$
オイラーの公式 $\sin u = (e^{iu} - e^{-iu})/(2i)$ を適用すると，
$$
\begin{aligned}
U(k_x) &= \frac{2\sin(k_x a / 2)}{k_x} \\
&= \finalanswer{U(k_x) = a \frac{\sin(k_x a / 2)}{k_x a / 2}}
\end{aligned}
$$
となります。

### (2)
回折強度 $I(k_x)$ は複素振幅の絶対値の2乗で定義されます。
$$
I(k_x) = |U(k_x)|^2 = a^2 \left(\frac{\sin(k_x a / 2)}{k_x a / 2}\right)^2
$$
$k_x \to 0$ の極限をとると，$\lim_{u \to 0} (\sin u)/u = 1$ より中心強度は
$$
I_0 = I(0) = a^2
$$
となります。したがって，回折強度は
$$
\finalanswer{I(k_x) = I_0 \left(\frac{\sin(k_x a / 2)}{k_x a / 2}\right)^2}
$$
となります。

### (3)
強度 $I(k_x) = 0$ となる条件は，分子が $\sin(k_x a / 2) = 0$ かつ $k_x \ne 0$ となることです。最小の正の値は
$$
\frac{k_x a}{2} = \pi
$$
となります。$k_x = k \sin\theta = (2\pi/\lambda)\sin\theta$ を代入すると，
$$
\frac{2\pi}{\lambda} \sin\theta_1 \cdot \frac{a}{2} = \pi
$$
となり，整理すると
$$
\finalanswer{\sin\theta_1 = \frac{\lambda}{a}}
$$
が得られます。

第1副極大は $u = k_x a / 2 \approx 3\pi/2$ で生じるため，その位置での強度は
$$
I_1 \approx I_0 \left(\frac{\sin(3\pi/2)}{3\pi/2}\right)^2 = I_0 \left(\frac{-1}{3\pi/2}\right)^2 = I_0 \frac{4}{9\pi^2}
$$
となります。したがって，中心強度との比は
$$
\finalanswer{\frac{I_1}{I_0} = \frac{4}{9\pi^2}}
$$
となります。数値としては約 $0.045$ であり，光の大部分が中央の主極大に集中していることを示します。

===== FILE: 10integral_transforms/04/04_050.md =====
---
tags:
  - 発展
---

# サンプリング定理

## 問題
連続信号 $f(t)$ のフーリエ変換を $\tilde{f}(\omega) = \int_{-\infty}^\infty f(t) e^{-i\omega t} dt$ とする。$\tilde{f}(\omega)$ は $|\omega| > \omega_{\mathrm{max}}$ で恒等的に $0$ である帯域制限信号とする。周期 $T$ のデルタ関数列
$$
s(t) = \sum_{n=-\infty}^\infty \delta(t - nT)
$$
を $f(t)$ に乗じて得られるサンプリング信号 $f_s(t) = f(t) s(t)$ を考える。以下の問いに答えよ。

(1) デルタ関数列のフーリエ級数展開が $s(t) = \frac{1}{T} \sum_{m=-\infty}^\infty e^{i m \omega_s t}$（$\omega_s = 2\pi/T$）となることを用いて，$f_s(t)$ のフーリエ変換 $\tilde{f}_s(\omega)$ を $\tilde{f}(\omega)$ を用いて表せ。

(2) スペクトルの重なり（エイリアシング）を生じさせずに元の信号のスペクトル $\tilde{f}(\omega)$ を分離するために，サンプリング角振動数 $\omega_s$ が満たすべき条件を求めよ。

(3) (2) の条件が満たされているとき，周波数領域の理想低域通過フィルタ
$$
H(\omega) = \begin{cases} T & (|\omega| \le \omega_s / 2) \\ 0 & (|\omega| > \omega_s / 2) \end{cases}
$$
を用いて $\tilde{f}(\omega) = H(\omega) \tilde{f}_s(\omega)$ と復元できる。逆フーリエ変換を行うことにより，サンプル値 $f(nT)$ から連続信号 $f(t)$ を復元する補間公式を導け。

---

## 解答・解説

### (1)
サンプリング信号 $f_s(t)$ にデルタ関数列のフーリエ級数展開を代入します。
$$
f_s(t) = f(t) \cdot \frac{1}{T} \sum_{m=-\infty}^\infty e^{i m \omega_s t} = \frac{1}{T} \sum_{m=-\infty}^\infty f(t) e^{i m \omega_s t}
$$
この両辺をフーリエ変換すると，
$$
\begin{aligned}
\tilde{f}_s(\omega) &= \int_{-\infty}^\infty \left(\frac{1}{T} \sum_{m=-\infty}^\infty f(t) e^{i m \omega_s t}\right) e^{-i\omega t} dt \\
&= \frac{1}{T} \sum_{m=-\infty}^\infty \int_{-\infty}^\infty f(t) e^{-i(\omega - m\omega_s)t} dt
\end{aligned}
$$
となります。積分の定義と照らし合わせると，
$$
\finalanswer{\tilde{f}_s(\omega) = \frac{1}{T} \sum_{m=-\infty}^\infty \tilde{f}(\omega - m\omega_s)}
$$
となります。

### (2)
$\tilde{f}_s(\omega)$ は元のスペクトル $\tilde{f}(\omega)$ が周波数軸上で周期 $\omega_s$ ごとに複製されて並んだ構造をもちます。各スペクトル成分 $\tilde{f}(\omega - m\omega_s)$ の帯域幅は $[m\omega_s - \omega_{\mathrm{max}}, m\omega_s + \omega_{\mathrm{max}}]$ です。

隣り合う $m = 0$ の成分の上限 $\omega_{\mathrm{max}}$ と $m = 1$ の成分の下限 $\omega_s - \omega_{\mathrm{max}}$ が重ならないための条件は，
$$
\omega_s - \omega_{\mathrm{max}} > \omega_{\mathrm{max}}
$$
となります。両辺を整理すると，
$$
\finalanswer{\omega_s > 2\omega_{\mathrm{max}}}
$$
が得られます。

### (3)
サンプリング信号を時間領域で直接表すと，デルタ関数の性質より
$$
f_s(t) = \sum_{n=-\infty}^\infty f(t) \delta(t - nT) = \sum_{n=-\infty}^\infty f(nT) \delta(t - nT)
$$
となります。周波数領域での積 $\tilde{f}(\omega) = H(\omega) \tilde{f}_s(\omega)$ は，時間領域における畳み込み積分 $f(t) = (f_s * h)(t)$ に対応します。ここでフィルタ $H(\omega)$ の逆フーリエ変換 $h(t)$ を計算すると，
$$
\begin{aligned}
h(t) &= \frac{1}{2\pi} \int_{-\omega_s/2}^{\omega_s/2} T e^{i\omega t} d\omega \\
&= \frac{T}{2\pi} \left[\frac{e^{i\omega t}}{it}\right]_{-\omega_s/2}^{\omega_s/2} \\
&= \frac{T}{\pi t} \sin\left(\frac{\omega_s t}{2}\right)
\end{aligned}
$$
となります。$\omega_s = 2\pi/T$ を代入すると，
$$
h(t) = \frac{\sin(\pi t / T)}{\pi t / T}
$$
が得られます。したがって，畳み込みを実行すると，
$$
\begin{aligned}
f(t) &= \int_{-\infty}^\infty \sum_{n=-\infty}^\infty f(nT) \delta(\tau - nT) h(t - \tau) d\tau \\
&= \sum_{n=-\infty}^\infty f(nT) h(t - nT) \\
&= \finalanswer{f(t) = \sum_{n=-\infty}^\infty f(nT) \frac{\sin\left(\frac{\pi}{T}(t - nT)\right)}{\frac{\pi}{T}(t - nT)}}
\end{aligned}
$$
となります。離散的なサンプル値から元の連続関数が一意に完全に復元されます。

===== FILE: 10integral_transforms/05/05_010.md =====
---
tags:
  - 基本
---

# ラプラス変換の定義と基本変換

## 問題
実数 $t \ge 0$ で定義された関数 $f(t)$ のラプラス変換は次式で定義される。
$$
\mathcal{L}[f(t)] = F(s) = \int_0^\infty f(t) e^{-st} dt
$$
以下の問いに答えよ。

(1) 定数 $a$ に対し，$f(t) = e^{at}$（$s > a$）のラプラス変換を求めよ。

(2) 定数 $\omega > 0$ に対し，オイラーの公式を用いて $\cos(\omega t)$ および $\sin(\omega t)$（$s > 0$）のラプラス変換を求めよ。

(3) 非負の整数 $n$ に対し，$f(t) = t^n$（$s > 0$）のラプラス変換を求めよ。

---

## 解答・解説

### (1)
定義式にしたがって指数関数の積分を計算します。
$$
\begin{aligned}
\mathcal{L}[e^{at}] &= \int_0^\infty e^{at} e^{-st} dt \\
&= \int_0^\infty e^{-(s-a)t} dt \\
&= \left[-\frac{e^{-(s-a)t}}{s-a}\right]_0^\infty
\end{aligned}
$$
$s > a$ のとき上端の極限値は $0$ となるため，
$$
\finalanswer{\mathcal{L}[e^{at}] = \frac{1}{s-a}}
$$
となります。

### (2)
オイラーの公式 $e^{i\omega t} = \cos(\omega t) + i \sin(\omega t)$ を用います。(1) の結果において $a = i\omega$ と置くと，
$$
\mathcal{L}[e^{i\omega t}] = \frac{1}{s - i\omega}
$$
が得られます。分母を有理化して実部と虚部に分けると，
$$
\begin{aligned}
\frac{1}{s - i\omega} &= \frac{s + i\omega}{(s - i\omega)(s + i\omega)} \\
&= \frac{s}{s^2 + \omega^2} + i \frac{\omega}{s^2 + \omega^2}
\end{aligned}
$$
となります。線形性より実部どうしおよび虚部どうしを比較すると，
$$
\finalanswer{\mathcal{L}[\cos(\omega t)] = \frac{s}{s^2 + \omega^2}}
$$
および
$$
\finalanswer{\mathcal{L}[\sin(\omega t)] = \frac{\omega}{s^2 + \omega^2}}
$$
となります。

### (3)
$I_n = \int_0^\infty t^n e^{-st} dt$ と置き，部分積分を行います。
$$
\begin{aligned}
I_n &= \left[t^n \frac{e^{-st}}{-s}\right]_0^\infty - \int_0^\infty n t^{n-1} \frac{e^{-st}}{-s} dt \\
&= 0 + \frac{n}{s} \int_0^\infty t^{n-1} e^{-st} dt \\
&= \frac{n}{s} I_{n-1}
\end{aligned}
$$
$n = 0$ のときは
$$
I_0 = \int_0^\infty e^{-st} dt = \frac{1}{s}
$$
となります。漸化式を繰り返し適用すると，
$$
\begin{aligned}
I_n &= \frac{n}{s} \cdot \frac{n-1}{s} \cdots \frac{1}{s} I_0 \\
&= \finalanswer{\mathcal{L}[t^n] = \frac{n!}{s^{n+1}}}
\end{aligned}
$$
となります。

===== FILE: 10integral_transforms/05/05_020.md =====
---
tags:
  - 基本
---

# ラプラス変換の性質

## 問題
関数 $f(t)$ のラプラス変換を $F(s) = \mathcal{L}[f(t)]$ とする。以下の問いに答えよ。

(1) 部分積分を用いて，導関数のラプラス変換 $\mathcal{L}[f'(t)] = s F(s) - f(0)$ を導け。また，これを用いて2階導関数のラプラス変換 $\mathcal{L}[f''(t)]$ を $F(s), f(0), f'(0)$ を用いて表せ。

(2) 定数 $a > 0$ に対し，$s$ 領域の移動定理 $\mathcal{L}[e^{-at} f(t)] = F(s+a)$ を示せ。またこれを用いて $\mathcal{L}[e^{-at} \cos(\omega t)]$ を求めよ。

(3) 像関数の微分に関する公式 $\frac{d}{ds}F(s) = -\mathcal{L}[t f(t)]$ を示せ。またこれを用いて $\mathcal{L}[t \sin(\omega t)]$ を求めよ。

---

## 解答・解説

### (1)
定義にしたがって部分積分を行います。
$$
\begin{aligned}
\mathcal{L}[f'(t)] &= \int_0^\infty f'(t) e^{-st} dt \\
&= \left[f(t) e^{-st}\right]_0^\infty - \int_0^\infty f(t) (-s e^{-st}) dt \\
&= -f(0) + s \int_0^\infty f(t) e^{-st} dt
\end{aligned}
$$
したがって，
$$
\finalanswer{\mathcal{L}[f'(t)] = s F(s) - f(0)}
$$
となります。

この結果を2階導関数に適用します。$g(t) = f'(t)$ と置くと，
$$
\begin{aligned}
\mathcal{L}[f''(t)] &= \mathcal{L}[g'(t)] \\
&= s \mathcal{L}[g(t)] - g(0) \\
&= s \left(s F(s) - f(0)\right) - f'(0) \\
&= \finalanswer{\mathcal{L}[f''(t)] = s^2 F(s) - s f(0) - f'(0)}
\end{aligned}
$$
となります。

### (2)
定義式に代入して指数関数をまとめます。
$$
\begin{aligned}
\mathcal{L}[e^{-at} f(t)] &= \int_0^\infty \left(e^{-at} f(t)\right) e^{-st} dt \\
&= \int_0^\infty f(t) e^{-(s+a)t} dt
\end{aligned}
$$
右辺は定義より $F(s+a)$ そのものであるため，
$$
\finalanswer{\mathcal{L}[e^{-at} f(t)] = F(s+a)}
$$
が示されます。

$\cos(\omega t)$ のラプラス変換は $\frac{s}{s^2 + \omega^2}$ であるため，$s$ を $s+a$ に置き換えると，
$$
\finalanswer{\mathcal{L}[e^{-at} \cos(\omega t)] = \frac{s+a}{(s+a)^2 + \omega^2}}
$$
となります。

### (3)
像関数の定義式をパラメータ $s$ について積分記号下で微分します。
$$
\begin{aligned}
\frac{d}{ds} F(s) &= \frac{d}{ds} \int_0^\infty f(t) e^{-st} dt \\
&= \int_0^\infty f(t) \frac{\partial}{\partial s}\left(e^{-st}\right) dt \\
&= \int_0^\infty f(t) (-t e^{-st}) dt \\
&= -\int_0^\infty (t f(t)) e^{-st} dt
\end{aligned}
$$
したがって，
$$
\finalanswer{\frac{d}{ds}F(s) = -\mathcal{L}[t f(t)]}
$$
が得られます。

$\sin(\omega t)$ のラプラス変換は $\frac{\omega}{s^2 + \omega^2}$ です。この関係式を適用すると，
$$
\begin{aligned}
\mathcal{L}[t \sin(\omega t)] &= -\frac{d}{ds}\left(\frac{\omega}{s^2 + \omega^2}\right) \\
&= -\left(-\frac{\omega \cdot 2s}{(s^2 + \omega^2)^2}\right) \\
&= \finalanswer{\mathcal{L}[t \sin(\omega t)] = \frac{2\omega s}{(s^2 + \omega^2)^2}}
\end{aligned}
$$
となります。

===== FILE: 10integral_transforms/05/05_030.md =====
---
tags:
  - 基本
---

# 部分分数による逆変換

## 問題
ラプラス逆変換を $\mathcal{L}^{-1}[F(s)] = f(t)$ と表す。以下の像関数の逆ラプラス変換を求めよ。

(1) $F_1(s) = \frac{1}{(s+1)(s+3)}$

(2) $F_2(s) = \frac{s}{(s+1)(s^2 + 4)}$

(3) $F_3(s) = \frac{1}{(s+2)^2 (s+1)}$

---

## 解答・解説

### (1)
部分分数展開を行います。
$$
F_1(s) = \frac{A}{s+1} + \frac{B}{s+3}
$$
ヘビサイドの展開定理（留数法）により係数を決定します。
$$
\begin{aligned}
A &= \lim_{s \to -1} (s+1) F_1(s) = \frac{1}{-1+3} = \frac{1}{2} \\
B &= \lim_{s \to -3} (s+3) F_1(s) = \frac{1}{-3+1} = -\frac{1}{2}
\end{aligned}
$$
したがって，展開式は
$$
F_1(s) = \frac{1}{2}\left(\frac{1}{s+1} - \frac{1}{s+3}\right)
$$
となります。公式 $\mathcal{L}^{-1}\left[\frac{1}{s-a}\right] = e^{at}$ を用いて逆変換すると，
$$
\finalanswer{f_1(t) = \frac{1}{2}\left(e^{-t} - e^{-3t}\right)}
$$
となります。

### (2)
部分分数に分解します。
$$
F_2(s) = \frac{A}{s+1} + \frac{Bs + C}{s^2 + 4}
$$
係数 $A$ は
$$
A = \lim_{s \to -1} (s+1) F_2(s) = \frac{-1}{(-1)^2 + 4} = -\frac{1}{5}
$$
となります。両辺を通分して分子を比較すると，
$$
s = A(s^2 + 4) + (Bs + C)(s + 1) = (A + B)s^2 + (B + C)s + (4A + C)
$$
が得られます。各次数の係数を比較すると，
$$
\begin{aligned}
s^2 \text{ の係数}: &\quad A + B = 0 \implies B = \frac{1}{5} \\
\text{定数項}: &\quad 4A + C = 0 \implies C = -4A = \frac{4}{5}
\end{aligned}
$$
となります。したがって，
$$
F_2(s) = \frac{1}{5}\left(-\frac{1}{s+1} + \frac{s}{s^2 + 4} + 2 \cdot \frac{2}{s^2 + 4}\right)
$$
と表せます。各項を逆変換すると，
$$
\finalanswer{f_2(t) = \frac{1}{5}\left(-e^{-t} + \cos(2t) + 2\sin(2t)\right)}
$$
となります。

### (3)
重解をもつ場合の展開を行います。
$$
F_3(s) = \frac{A}{s+1} + \frac{B}{s+2} + \frac{C}{(s+2)^2}
$$
係数 $A$ と $C$ は
$$
\begin{aligned}
A &= \lim_{s \to -1} (s+1) F_3(s) = \frac{1}{(-1+2)^2} = 1 \\
C &= \lim_{s \to -2} (s+2)^2 F_3(s) = \frac{1}{-2+1} = -1
\end{aligned}
$$
となります。係数 $B$ を求めるため，両辺に $s = 0$ を代入すると，
$$
\frac{1}{4} = A + \frac{B}{2} + \frac{C}{4} = 1 + \frac{B}{2} - \frac{1}{4}
$$
となり，整理すると $B = -1$ が得られます。したがって，
$$
F_3(s) = \frac{1}{s+1} - \frac{1}{s+2} - \frac{1}{(s+2)^2}
$$
となります。公式 $\mathcal{L}^{-1}\left[\frac{1}{(s+2)^2}\right] = t e^{-2t}$ を用いて各項を逆変換すると，
$$
\finalanswer{f_3(t) = e^{-t} - (1+t)e^{-2t}}
$$
となります。

===== FILE: 10integral_transforms/05/05_040.md =====
---
tags:
  - 標準
---

# 初期値問題の解法

## 問題
次の2階線形微分方程式の初期値問題を考える。
$$
\frac{d^2 y}{dt^2} + 4\frac{dy}{dt} + 3y = e^{-2t}, \quad y(0) = 1, \quad y'(0) = 0
$$
以下の問いに答えよ。

(1) 両辺をラプラス変換し，像関数 $Y(s) = \mathcal{L}[y(t)]$ を $s$ の代数式として求めよ。

(2) 像関数 $Y(s)$ を部分分数展開せよ。

(3) $Y(s)$ を逆ラプラス変換し，微分方程式の解 $y(t)$ を求めよ。

---

## 解答・解説

### (1)
導関数のラプラス変換の公式
$$
\begin{aligned}
\mathcal{L}[y'(t)] &= s Y(s) - y(0) \\
\mathcal{L}[y''(t)] &= s^2 Y(s) - s y(0) - y'(0)
\end{aligned}
$$
を用います。初期条件 $y(0) = 1, y'(0) = 0$ を代入すると，
$$
\begin{aligned}
\mathcal{L}[y'(t)] &= s Y(s) - 1 \\
\mathcal{L}[y''(t)] &= s^2 Y(s) - s
\end{aligned}
$$
となります。微分方程式の両辺をラプラス変換すると，
$$
(s^2 Y(s) - s) + 4(s Y(s) - 1) + 3 Y(s) = \frac{1}{s+2}
$$
が得られます。$Y(s)$ について整理すると，
$$
(s^2 + 4s + 3) Y(s) = s + 4 + \frac{1}{s+2} = \frac{(s+4)(s+2) + 1}{s+2} = \frac{(s+3)^2}{s+2}
$$
となります。$s^2 + 4s + 3 = (s+1)(s+3)$ であるため，両辺を割ると，
$$
\finalanswer{Y(s) = \frac{s+3}{(s+1)(s+2)}}
$$
となります。

### (2)
得られた有理関数を部分分数に分解します。
$$
Y(s) = \frac{s+3}{(s+1)(s+2)} = \frac{A}{s+1} + \frac{B}{s+2}
$$
各係数を計算すると，
$$
\begin{aligned}
A &= \lim_{s \to -1} (s+1) Y(s) = \frac{-1+3}{-1+2} = 2 \\
B &= \lim_{s \to -2} (s+2) Y(s) = \frac{-2+3}{-2+1} = -1
\end{aligned}
$$
となります。したがって，展開式は
$$
\finalanswer{Y(s) = \frac{2}{s+1} - \frac{1}{s+2}}
$$
となります。

### (3)
部分分数展開された各項を逆ラプラス変換します。基本公式 $\mathcal{L}^{-1}\left[\frac{1}{s-a}\right] = e^{at}$ を用いると，
$$
\begin{aligned}
y(t) &= 2 \mathcal{L}^{-1}\left[\frac{1}{s+1}\right] - \mathcal{L}^{-1}\left[\frac{1}{s+2}\right] \\
&= \finalanswer{y(t) = 2e^{-t} - e^{-2t}}
\end{aligned}
$$
となります。$t = 0$ において $y(0) = 2 - 1 = 1$，$y'(0) = -2 + 2 = 0$ となり，初期条件を満たしていることが確認できます。

===== FILE: 10integral_transforms/05/05_050.md =====
---
tags:
  - 標準
---

# RLC 回路の過渡応答

## 問題
自己インダクタンス $L$，抵抗 $R$，電気容量 $C$ の直列 RLC 回路に，時刻 $t = 0$ で直流起電力 $E$ を接続した。初期状態において回路に電流は流れておらず，コンデンサの電荷も蓄えられていなかったものとする（$i(0) = 0$，$q(0) = 0$）。電流 $i(t)$ は次の方程式を満たす。
$$
L \frac{di}{dt} + R i + \frac{1}{C}\int_0^t i(t') dt' = E \quad (t \ge 0)
$$
以下の問いに答えよ。

(1) 方程式の両辺をラプラス変換し，電流の像関数 $I(s) = \mathcal{L}[i(t)]$ を求めよ。

(2) 不足減衰の条件 $R^2 < \frac{4L}{C}$ のもとで，減衰定数 $\gamma = \frac{R}{2L}$ および角振動数 $\omega = \sqrt{\frac{1}{LC} - \gamma^2}$ を用いて，$I(s)$ を $(s + \gamma)^2 + \omega^2$ を含む形に変形せよ。

(3) $I(s)$ を逆ラプラス変換し，時刻 $t \ge 0$ における電流 $i(t)$ を求めよ。また，コンデンサの端子電圧 $v_C(t) = \frac{1}{C}\int_0^t i(t') dt'$ の $t \to \infty$ における極限値を求めよ。

---

## 解答・解説

### (1)
積分のラプラス変換の公式 $\mathcal{L}\left[\int_0^t i(t') dt'\right] = \frac{I(s)}{s}$ を用います。初期条件 $i(0) = 0$ を考慮して方程式の両辺をラプラス変換すると，
$$
L s I(s) + R I(s) + \frac{1}{C s} I(s) = \frac{E}{s}
$$
となります。両辺に $s$ を掛けてまとめると，
$$
\left(L s^2 + R s + \frac{1}{C}\right) I(s) = E
$$
が得られます。したがって，像関数は
$$
\finalanswer{I(s) = \frac{E}{L s^2 + R s + \frac{1}{C}}}
$$
となります。

### (2)
分母を $L$ で括り，平方完成を行います。
$$
I(s) = \frac{E}{L} \frac{1}{s^2 + \frac{R}{L} s + \frac{1}{LC}}
$$
ここで $\frac{R}{L} = 2\gamma$ を用いて分母を平方完成すると，
$$
s^2 + 2\gamma s + \frac{1}{LC} = (s + \gamma)^2 + \left(\frac{1}{LC} - \gamma^2\right)
$$
となります。不足減衰の条件より $\omega^2 = \frac{1}{LC} - \gamma^2 > 0$ であるため，
$$
\finalanswer{I(s) = \frac{E}{\omega L} \frac{\omega}{(s + \gamma)^2 + \omega^2}}
$$
と変形されます。

### (3)
移動定理と正弦関数の変換公式
$$
\mathcal{L}^{-1}\left[\frac{\omega}{(s + \gamma)^2 + \omega^2}\right] = e^{-\gamma t} \sin(\omega t)
$$
を適用すると，電流は
$$
\finalanswer{i(t) = \frac{E}{\omega L} e^{-\gamma t} \sin(\omega t)}
$$
となります。

次にコンデンサ電圧の終端値を求めます。最終値の定理を用いると，
$$
\lim_{t \to \infty} v_C(t) = \lim_{s \to 0} s V_C(s) = \lim_{s \to 0} s \left(\frac{I(s)}{C s}\right) = \lim_{s \to 0} \frac{I(s)}{C}
$$
となります。(1) で求めた $I(s)$ において $s \to 0$ の極限をとると，
$$
\lim_{s \to 0} I(s) = \frac{E}{1/C} = C E
$$
となります。したがって，端子電圧の極限値は
$$
\lim_{t \to \infty} v_C(t) = \frac{C E}{C} = \finalanswer{\lim_{t \to \infty} v_C(t) = E}
$$
となります。十分時間が経過するとコンデンサが電源電圧まで完全に充電される物理的状況と一致します。

===== FILE: 10integral_transforms/05/05_060.md =====
---
tags:
  - 発展
---

# 畳み込みとヴォルテラ型積分方程式

## 問題
2つの関数 $f(t), g(t)$ の畳み込みは
$$
(f * g)(t) = \int_0^t f(t - \tau) g(\tau) d\tau
$$
で定義される。以下の問いに答えよ。

(1) 重積分の積分の順序を交換することにより，畳み込みのラプラス変換が $\mathcal{L}[(f * g)(t)] = F(s) G(s)$ となることを示せ。ただし $F(s) = \mathcal{L}[f(t)], G(s) = \mathcal{L}[g(t)]$ とする。

<!-- FIGURE solution (1): tau-t 平面において，直線 tau = 0，t = tau，および t -> \infty で囲まれる領域（0 <= tau <= t < \infty）を示す図。縦軸 t，横軸 tau，原点 O。 -->

(2) 未知関数 $y(t)$ に関する次のヴォルテラ型積分方程式
$$
y(t) = \sin t + 2 \int_0^t \cos(t - \tau) y(\tau) d\tau
$$
の両辺をラプラス変換し，像関数 $Y(s) = \mathcal{L}[y(t)]$ を求めよ。

(3) 像関数 $Y(s)$ を逆ラプラス変換し，積分方程式の解 $y(t)$ を求めよ。

---

## 解答・解説

### (1)
定義式にしたがって重積分の形に書き表します。積分領域を図に示します。

<!-- FIGURE solution (1): tau-t 平面において，直線 tau = 0，t = tau，および t -> \infty で囲まれる領域（0 <= tau <= t < \infty）を示す図。縦軸 t，横軸 tau，原点 O。 -->

$$
\mathcal{L}[(f * g)(t)] = \int_0^\infty e^{-st} \left(\int_0^t f(t - \tau) g(\tau) d\tau\right) dt
$$
この積分の領域は $0 \le \tau \le t < \infty$ です。積分の順序を交換すると，$\tau$ の範囲は $0 \le \tau < \infty$ となり，$t$ の範囲は $\tau \le t < \infty$ となるため，
$$
\mathcal{L}[(f * g)(t)] = \int_0^\infty g(\tau) \left(\int_\tau^\infty f(t - \tau) e^{-st} dt\right) d\tau
$$
と変形されます。内側の積分において $u = t - \tau$ と置換すると，$t = u + \tau$ かつ $dt = du$ となり，
$$
\int_\tau^\infty f(t - \tau) e^{-st} dt = \int_0^\infty f(u) e^{-s(u+\tau)} du = e^{-s\tau} \int_0^\infty f(u) e^{-su} du = e^{-s\tau} F(s)
$$
が得られます。これを元の式に代入すると，
$$
\begin{aligned}
\mathcal{L}[(f * g)(t)] &= \int_0^\infty g(\tau) e^{-s\tau} F(s) d\tau \\
&= F(s) \int_0^\infty g(\tau) e^{-s\tau} d\tau \\
&= \finalanswer{\mathcal{L}[(f * g)(t)] = F(s) G(s)}
\end{aligned}
$$
が示されます。

### (2)
積分方程式の積分項は $\cos t$ と $y(t)$ の畳み込み $(\cos * y)(t)$ です。方程式の両辺をラプラス変換すると，
$$
Y(s) = \mathcal{L}[\sin t] + 2 \mathcal{L}[\cos t] Y(s)
$$
となります。公式 $\mathcal{L}[\sin t] = \frac{1}{s^2 + 1}$ および $\mathcal{L}[\cos t] = \frac{s}{s^2 + 1}$ を代入すると，
$$
Y(s) = \frac{1}{s^2 + 1} + \frac{2s}{s^2 + 1} Y(s)
$$
が得られます。両辺に $s^2 + 1$ を掛けてまとめると，
$$
(s^2 + 1 - 2s) Y(s) = 1
$$
となり，$(s-1)^2 Y(s) = 1$ より像関数は
$$
\finalanswer{Y(s) = \frac{1}{(s-1)^2}}
$$
となります。

### (3)
公式 $\mathcal{L}^{-1}\left[\frac{1}{s^2}\right] = t$ に対して，$s$ 領域の移動定理 $\mathcal{L}^{-1}[F(s-a)] = e^{at} f(t)$ を適用します。$a = 1$ と置くことにより，
$$
\finalanswer{y(t) = t e^t}
$$
が得られます。積分方程式がラプラス変換によって単純な代数方程式に帰着され，容易に解けることがわかります。

===== FILE: 10integral_transforms/05/05_070.md =====
---
tags:
  - 発展
---

# ブロムウィッチ積分による逆変換

## 問題
ラプラス逆変換を与える複素反転公式（ブロムウィッチ積分）は次式で定義される。
$$
f(t) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} F(s) e^{st} ds \quad (t > 0)
$$
ここで積分路は，複素平面上ですべての極の右側を通る直線 $\mathrm{Re}(s) = c$ である。像関数
$$
F(s) = \frac{1}{s(s+a)} \quad (a > 0)
$$
に対する逆変換を考える。以下の問いに答えよ。

(1) 被積分関数 $g(s) = F(s) e^{st}$ のすべての極の位置とその位数を答えよ。また，各極における留数を求めよ。

(2) 直線 $\mathrm{Re}(s) = c$（$-R \le \mathrm{Im}(s) \le R$）と，左半平面にある半径 $R$ の半円弧 $C_R$（中心 $c$，偏角 $\pi/2 \le \theta \le 3\pi/2$）からなる閉経路を考える（図）。$t > 0$ において，半円弧に沿う積分が $R \to \infty$ で $0$ に収束することを示せ。

<!-- FIGURE solution (2): 複素 s 平面において，直線 Re(s) = c 上の線分と，s = c を中心として左半平面へ広がる半径 R の半円弧 C_R からなる反時計回りの積分経路。実軸上の s = 0 と s = -a に二つの極が描かれている。横軸 Re(s)，縦軸 Im(s)，原点 O。 -->

(3) 留数定理を用いてブロムウィッチ積分を計算し，$f(t)$ を求めよ。

---

## 解答・解説

### (1)
被積分関数は
$$
g(s) = \frac{e^{st}}{s(s+a)}
$$
です。分母が $0$ となる点は $s = 0$ および $s = -a$ であり，いずれも1位の極です。各極における留数を計算します。
$$
\begin{aligned}
\mathrm{Res}[g(s), 0] &= \lim_{s \to 0} s g(s) = \lim_{s \to 0} \frac{e^{st}}{s+a} = \frac{1}{a} \\
\mathrm{Res}[g(s), -a] &= \lim_{s \to -a} (s+a) g(s) = \lim_{s \to -a} \frac{e^{st}}{s} = -\frac{1}{a} e^{-at}
\end{aligned}
$$
したがって，求める留数は
$$
\finalanswer{\mathrm{Res}[g(s), 0] = \frac{1}{a}}
$$
および
$$
\finalanswer{\mathrm{Res}[g(s), -a] = -\frac{1}{a} e^{-at}}
$$
となります。

### (2)
積分路を図に示します。

<!-- FIGURE solution (2): 複素 s 平面において，直線 Re(s) = c 上の線分と，s = c を中心として左半平面へ広がる半径 R の半円弧 C_R からなる反時計回りの積分経路。実軸上の s = 0 と s = -a に二つの極が描かれている。横軸 Re(s)，縦軸 Im(s)，原点 O。 -->

半円弧 $C_R$ 上の点を $s = c + R e^{i\theta}$（$\pi/2 \le \theta \le 3\pi/2$）と表します。実部は $\mathrm{Re}(s) = c + R \cos\theta \le c$ であり，$\cos\theta \le 0$ です。十分大きな $R$ に対して三角不等式を適用すると，
$$
|F(s)| = \frac{1}{|s||s+a|} \le \frac{1}{(R-c)(R-c-a)}
$$
となります。この上限を $M_R$ と置くと，$R \to \infty$ で $M_R = O(R^{-2})$ です。積分の絶対値を評価すると，
$$
\begin{aligned}
\left|\int_{C_R} F(s) e^{st} ds\right| &\le \int_{\pi/2}^{3\pi/2} |F(s)| e^{(c + R\cos\theta)t} R d\theta \\
&\le M_R R e^{ct} \int_{\pi/2}^{3\pi/2} e^{R t \cos\theta} d\theta
\end{aligned}
$$
となります。$\cos\theta \le 0$ より被積分関数は常に $1$ 以下であるため，積分値は有限値 $\pi$ で抑えられます。
$$
\left|\int_{C_R} F(s) e^{st} ds\right| \le M_R R e^{ct} \pi
$$
$M_R R \propto R^{-1} \to 0$（$R \to \infty$）であるため，
$$
\finalanswer{\lim_{R \to \infty} \int_{C_R} F(s) e^{st} ds = 0}
$$
が示されます。

### (3)
直線路と半円弧 $C_R$ を合わせた反時計回りの閉経路を $C$ とします。十分大きな $R$ に対してすべての極 $s = 0, -a$ は閉経路の内部に含まれます。留数定理を適用すると，
$$
\frac{1}{2\pi i} \oint_C F(s) e^{st} ds = \mathrm{Res}[g(s), 0] + \mathrm{Res}[g(s), -a]
$$
となります。(2) の結果より $R \to \infty$ で半円弧の寄与は消滅するため，閉経路に沿う積分はブロムウィッチ積分そのものに一致します。
$$
\begin{aligned}
f(t) &= \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} F(s) e^{st} ds \\
&= \frac{1}{a} - \frac{1}{a} e^{-at} \\
&= \finalanswer{f(t) = \frac{1}{a}\left(1 - e^{-at}\right)}
\end{aligned}
$$
となります。部分分数展開を用いた初等的な逆変換の結果と一致します。

===== FILE: 10integral_transforms/06/06_010.md =====
---
tags:
  - 標準
---

# 有限長の棒の熱伝導とフーリエ級数

## 問題
長さ $L$ の一様な棒における温度分布 $u(x, t)$（$0 \le x \le L$，$t \ge 0$）は，熱拡散率 $D > 0$ の熱伝導方程式
$$
\frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}
$$
に従う。棒の両端は零度に保たれており，境界条件は $u(0, t) = u(L, t) = 0$ である。時刻 $t = 0$ における初期温度分布は一様に $T_0$（$T_0 > 0$）であったとする。以下の問いに答えよ。

(1) 変数分離解 $u(x, t) = X(x) T(t)$ を仮定し，境界条件を満たす空間の固有関数 $X_n(x)$ および対応する時間関数 $T_n(t)$（$n = 1, 2, 3, \dots$）を求めよ。ただし $X_n(x)$ の振幅係数は $1$ とする。

(2) 初期条件 $u(x, 0) = T_0$ をフーリエ正弦級数
$$
u(x, 0) = \sum_{n=1}^\infty c_n \sin\left(\frac{n\pi x}{L}\right)
$$
として展開するとき，展開係数 $c_n$ を求めよ。

(3) 時刻 $t > 0$ における温度分布 $u(x, t)$ を級数表示で求めよ。また，十分時間が経過したとき（$t \gg L^2 / (\pi^2 D)$）における棒の中央 $x = L/2$ の温度の近似式を求めよ。

---

## 解答・解説

### (1)
変数分離形 $u(x, t) = X(x) T(t)$ を方程式に代入して整理します。
$$
\frac{1}{D T}\frac{dT}{dt} = \frac{1}{X}\frac{d^2 X}{dx^2} = -\lambda^2
$$
空間部分の方程式は $X''(x) + \lambda^2 X(x) = 0$ であり，一般解は
$$
X(x) = A \cos(\lambda x) + B \sin(\lambda x)
$$
となります。境界条件 $X(0) = 0$ より $A = 0$ が定まり，さらに $X(L) = 0$ より $\sin(\lambda L) = 0$ となります。非自明な解を得る条件から，固有値および固有関数は
$$
\lambda_n = \frac{n\pi}{L}, \quad \finalanswer{X_n(x) = \sin\left(\frac{n\pi x}{L}\right)} \quad (n = 1, 2, 3, \dots)
$$
となります。

対応する時間部分の方程式は $\frac{dT}{dt} = -D \lambda_n^2 T$ であるため，解は
$$
\finalanswer{T_n(t) = \exp\left(-\frac{n^2 \pi^2 D t}{L^2}\right)}
$$
となります。

### (2)
フーリエ正弦級数の係数公式を適用します。
$$
\begin{aligned}
c_n &= \frac{2}{L} \int_0^L T_0 \sin\left(\frac{n\pi x}{L}\right) dx \\
&= \frac{2T_0}{L} \left[-\frac{L}{n\pi} \cos\left(\frac{n\pi x}{L}\right)\right]_0^L \\
&= \frac{2T_0}{n\pi} \left(1 - (-1)^n\right)
\end{aligned}
$$
したがって，係数は
$$
\finalanswer{c_n = \frac{2T_0}{n\pi}\left(1 - (-1)^n\right)}
$$
となります。$n$ が偶数のときは $c_n = 0$ であり，$n = 2m-1$（奇数）のときは $c_{2m-1} = \frac{4T_0}{(2m-1)\pi}$ となります。

### (3)
重ね合わせの原理により，全体の解は各モードの積の総和として表されます。奇数項のみが残るため，$n = 2m-1$ と置いて和をとると，
$$
\finalanswer{u(x, t) = \sum_{m=1}^\infty \frac{4T_0}{(2m-1)\pi} \sin\left(\frac{(2m-1)\pi x}{L}\right) \exp\left(-\frac{(2m-1)^2 \pi^2 D t}{L^2}\right)}
$$
となります。

$t \gg L^2/(\pi^2 D)$ の長時間極限では，減衰の最も遅い基本モード（$m = 1$）が全体を支配します。棒の中央 $x = L/2$ では $\sin(\pi / 2) = 1$ となるため，温度分布は次のように近似されます。
$$
\finalanswer{u(L/2, t) \approx \frac{4T_0}{\pi} \exp\left(-\frac{\pi^2 D t}{L^2}\right)}
$$
高調波が指数関数的に急速に減衰し，最終的に基本対称モードのみが観測される振る舞いを示します。

===== FILE: 10integral_transforms/06/06_020.md =====
---
tags:
  - 標準
---

# 周期的な強制振動

## 問題
減衰振動子の運動方程式
$$
m \frac{d^2 x}{dt^2} + \gamma \frac{dx}{dt} + k x = f(t)
$$
において，外力 $f(t)$ が周期 $T = 2\pi/\Omega$ をもつ次の矩形波であるとする。
$$
f(t) = \begin{cases} F_0 & (0 < t < \pi/\Omega) \\ -F_0 & (-\pi/\Omega < t < 0) \end{cases}, \quad f(t + T) = f(t)
$$
ただし $F_0 > 0$ とする。以下の問いに答えよ。

(1) 周期外力 $f(t)$ のフーリエ級数展開（正弦級数）を求めよ。

(2) 単一角振動数の外力 $F_n \sin(n\Omega t)$ に対する定常応答を $x_n(t) = A_n \sin(n\Omega t - \delta_n)$ と表すとき，振幅 $A_n$ および位相遅れ $\delta_n$ を与える $\tan\delta_n$ を $m, \gamma, k, n\Omega, F_n$ を用いて求めよ。ただし $0 \le \delta_n < \pi$ とする。

(3) 重ね合わせの原理により，全体の定常応答 $x(t)$ を級数表示で表せ。また，$n\Omega$ が系の固有角振動数 $\omega_0 = \sqrt{k/m}$ に極めて近い奇数 $n$ の成分が存在するとき，その高調波成分が共鳴を起こす。この共鳴が生じる外力の基本角振動数 $\Omega$ の条件を $n, k, m$ を用いて表せ。

---

## 解答・解説

### (1)
外力 $f(t)$ は奇関数であるため，余弦成分はすべて $0$ となり正弦級数に展開されます。展開係数は
$$
\begin{aligned}
b_n &= \frac{2}{T/2} \int_0^{T/2} f(t) \sin(n\Omega t) dt \\
&= \frac{2\Omega}{\pi} \int_0^{\pi/\Omega} F_0 \sin(n\Omega t) dt \\
&= \frac{2F_0 \Omega}{\pi} \left[-\frac{\cos(n\Omega t)}{n\Omega}\right]_0^{\pi/\Omega} \\
&= \frac{2F_0}{n\pi} \left(1 - (-1)^n\right)
\end{aligned}
$$
となります。偶数成分は $b_n = 0$ となり，奇数成分（$n = 2m-1$）のみが残るため，
$$
\finalanswer{f(t) = \sum_{m=1}^\infty \frac{4F_0}{(2m-1)\pi} \sin\left((2m-1)\Omega t\right)}
$$
が得られます。

### (2)
外力 $F_n \sin(n\Omega t) = \mathrm{Im}[F_n e^{i n\Omega t}]$ に対する複素運動方程式
$$
m \ddot{z} + \gamma \dot{z} + k z = F_n e^{i n\Omega t}
$$
の定常解を $z(t) = Z_n e^{i n\Omega t}$ と置いて代入すると，
$$
\left(-m n^2 \Omega^2 + i\gamma n\Omega + k\right) Z_n = F_n
$$
が得られます。複素振幅の絶対値と偏角を求めることにより，
$$
\finalanswer{A_n = \frac{F_n}{\sqrt{(k - m n^2 \Omega^2)^2 + \gamma^2 n^2 \Omega^2}}}
$$
および
$$
\finalanswer{\tan\delta_n = \frac{\gamma n\Omega}{k - m n^2 \Omega^2}}
$$
が導かれます。

### (3)
外力の各フーリエ成分 $F_{2m-1} = \frac{4F_0}{(2m-1)\pi}$ に対する応答を重ね合わせます。全体の定常解は
$$
\finalanswer{x(t) = \sum_{m=1}^\infty \frac{4F_0}{(2m-1)\pi \sqrt{(k - m(2m-1)^2 \Omega^2)^2 + \gamma^2 (2m-1)^2 \Omega^2}} \sin\left((2m-1)\Omega t - \delta_{2m-1}\right)}
$$
となります。

共鳴条件は，外力の高調波角振動数が固有角振動数と一致する $n\Omega = \omega_0 = \sqrt{k/m}$ です。したがって，基本角振動数に関する条件は
$$
\finalanswer{\Omega = \frac{1}{n}\sqrt{\frac{k}{m}}}
$$
となります。基本波の振動数が固有振動数より低くても，高調波成分によって共鳴が励起される現象を表しています。

===== FILE: 10integral_transforms/06/06_030.md =====
---
tags:
  - 標準
---

# 回折格子と2次元フーリエ変換

## 問題
フラウンホーファー回折において，開口面 $(x, y)$ の開口関数を $g(x, y)$ とすると，回折波の複素振幅は2次元フーリエ変換
$$
U(k_x, k_y) = \iint_{-\infty}^\infty g(x, y) e^{-i(k_x x + k_y y)} dx dy
$$
で与えられる。以下の問いに答えよ。

(1) 開口関数が変数分離形 $g(x, y) = g_1(x) g_2(y)$ で表されるとき，2次元フーリエ変換 $U(k_x, k_y)$ が各1次元フーリエ変換の積 $U_1(k_x) U_2(k_y)$ に分離できることを示せ。

(2) $x$ 方向に幅 $a$ のスリットが等間隔 $d$（$d > a$）で $N$ 本並んだ開口（図）を考える。1本のスリットの開口関数を
$$
g_0(x) = \begin{cases} 1 & (|x| \le a/2) \\ 0 & (|x| > a/2) \end{cases}
$$
とするとき，全体の開口関数 $g_1(x) = \sum_{n=0}^{N-1} g_0(x - nd)$ のフーリエ変換 $U_1(k_x)$ を求めよ。

<!-- FIGURE problem: x 軸に沿って等間隔 d で並んだ N 本のスリット（各スリットの幅 a）の配置図。原点から 0, d, 2d, ..., (N-1)d にスリットの中心がある。 -->

(3) 回折強度 $I(k_x) = |U_1(k_x)|^2$ を求めよ。また，主極大が現れる空間周波数 $k_x$ の条件を整数 $m$ を用いて表せ。

---

## 解答・解説

### (1)
重積分の性質を用います。指数関数の法則 $e^{-i(k_x x + k_y y)} = e^{-ik_x x} e^{-ik_y y}$ を適用すると，
$$
\begin{aligned}
U(k_x, k_y) &= \iint_{-\infty}^\infty g_1(x) g_2(y) e^{-ik_x x} e^{-ik_y y} dx dy \\
&= \left(\int_{-\infty}^\infty g_1(x) e^{-ik_x x} dx\right) \left(\int_{-\infty}^\infty g_2(y) e^{-ik_y y} dy\right)
\end{aligned}
$$
が得られます。各積分はそれぞれ1次元フーリエ変換の定義式であるため，
$$
\finalanswer{U(k_x, k_y) = U_1(k_x) U_2(k_y)}
$$
が示されます。

### (2)
フーリエ変換の移動定理 $\int_{-\infty}^\infty g_0(x - nd) e^{-ik_x x} dx = e^{-ik_x nd} U_0(k_x)$ を用います。単一スリットの変換は
$$
U_0(k_x) = \int_{-a/2}^{a/2} e^{-ik_x x} dx = a \frac{\sin(k_x a / 2)}{k_x a / 2}
$$
です。全体の変換は各スリットの寄与の和となるため，
$$
U_1(k_x) = U_0(k_x) \sum_{n=0}^{N-1} e^{-ik_x nd}
$$
となります。等比数列の和の公式を適用すると，
$$
\sum_{n=0}^{N-1} \left(e^{-ik_x d}\right)^n = \frac{1 - e^{-ik_x Nd}}{1 - e^{-ik_x d}} = \frac{e^{-ik_x Nd/2}\left(e^{ik_x Nd/2} - e^{-ik_x Nd/2}\right)}{e^{-ik_x d/2}\left(e^{ik_x d/2} - e^{-ik_x d/2}\right)} = e^{-ik_x (N-1)d/2} \frac{\sin(N k_x d / 2)}{\sin(k_x d / 2)}
$$
が得られます。したがって，
$$
\finalanswer{U_1(k_x) = a \frac{\sin(k_x a / 2)}{k_x a / 2} \frac{\sin(N k_x d / 2)}{\sin(k_x d / 2)} e^{-i k_x (N-1)d / 2}}
$$
となります。

### (3)
回折強度 $I(k_x)$ は複素振幅の絶対値の2乗であるため，位相因子 $e^{-i k_x (N-1)d/2}$ の大きさは $1$ となり消去されます。
$$
\finalanswer{I(k_x) = a^2 \left(\frac{\sin(k_x a / 2)}{k_x a / 2}\right)^2 \left(\frac{\sin(N k_x d / 2)}{\sin(k_x d / 2)}\right)^2}
$$
となります。

主極大は多スリット干渉項の分母が $0$ となる点，すなわち $\sin(k_x d / 2) = 0$ で生じます。このとき分子も同時に $0$ となり，極限値は $N^2$ に達します。この条件は整数 $m$ を用いて $\frac{k_x d}{2} = m\pi$ と表されるため，
$$
\finalanswer{k_x = \frac{2\pi m}{d}}
$$
となります。$k_x = (2\pi/\lambda)\sin\theta$ を代入すると通常の回折格子の条件式 $d \sin\theta = m\lambda$ が得られます。

===== FILE: 10integral_transforms/06/06_040.md =====
---
tags:
  - 標準
---

# ラプラス変換による連立微分方程式

## 問題
2つのループが抵抗 $R$ で結合された電気回路において，各ループの電流 $i_1(t), i_2(t)$ は次の連立微分方程式を満たす。
$$
\begin{aligned}
L \frac{di_1}{dt} + 2R i_1 - R i_2 &= E \\
L \frac{di_2}{dt} - R i_1 + 2R i_2 &= 0
\end{aligned}
$$
時刻 $t = 0$ における初期条件は $i_1(0) = 0, i_2(0) = 0$ である。定数 $E, L, R$ はすべて正とする。以下の問いに答えよ。

(1) 連立方程式の両辺をラプラス変換し，像関数 $I_1(s) = \mathcal{L}[i_1(t)]$ および $I_2(s) = \mathcal{L}[i_2(t)]$ を求めよ。

(2) $I_1(s)$ および $I_2(s)$ を部分分数展開せよ。

(3) 逆ラプラス変換を行い，電流 $i_1(t)$ および $i_2(t)$ を求めよ。また，定常状態における電流 $i_1(\infty)$ および $i_2(\infty)$ を求めよ。

---

## 解答・解説

### (1)
初期条件 $i_1(0) = 0, i_2(0) = 0$ のもとで両辺をラプラス変換します。
$$
\begin{aligned}
(Ls + 2R) I_1(s) - R I_2(s) &= \frac{E}{s} \\
-R I_1(s) + (Ls + 2R) I_2(s) &= 0
\end{aligned}
$$
第2式より $I_2(s) = \frac{R}{Ls + 2R} I_1(s)$ と表せます。これを第1式に代入すると，
$$
\left((Ls + 2R) - \frac{R^2}{Ls + 2R}\right) I_1(s) = \frac{E}{s}
$$
となります。係数の分子を通分して因数分解すると，
$$
(Ls + 2R)^2 - R^2 = (Ls + R)(Ls + 3R)
$$
が得られます。したがって，像関数はそれぞれ
$$
\finalanswer{I_1(s) = \frac{E(Ls + 2R)}{s(Ls + R)(Ls + 3R)}}
$$
および
$$
\finalanswer{I_2(s) = \frac{E R}{s(Ls + R)(Ls + 3R)}}
$$
となります。

### (2)
$L$ をくくり出し，有理関数を標準的な形に直して部分分数分解します。
$$
I_1(s) = \frac{E}{L^2} \frac{s + 2R/L}{s(s + R/L)(s + 3R/L)} = \frac{A_1}{s} + \frac{B_1}{s + R/L} + \frac{C_1}{s + 3R/L}
$$
各留数を計算すると，
$$
\begin{aligned}
A_1 &= \lim_{s \to 0} s I_1(s) = \frac{E \cdot 2R}{R \cdot 3R} = \frac{2E}{3R} \\
B_1 &= \lim_{s \to -R/L} (s + R/L) I_1(s) = \frac{E(-R + 2R)}{-R(-R + 3R)} = -\frac{E}{2R} \\
C_1 &= \lim_{s \to -3R/L} (s + 3R/L) I_1(s) = \frac{E(-3R + 2R)}{-3R(-3R + R)} = -\frac{E}{6R}
\end{aligned}
$$
となります。同様に $I_2(s)$ について計算すると，
$$
\begin{aligned}
A_2 &= \lim_{s \to 0} s I_2(s) = \frac{ER}{R \cdot 3R} = \frac{E}{3R} \\
B_2 &= \lim_{s \to -R/L} (s + R/L) I_2(s) = \frac{ER}{-R \cdot 2R} = -\frac{E}{2R} \\
C_2 &= \lim_{s \to -3R/L} (s + 3R/L) I_2(s) = \frac{ER}{-3R \cdot (-2R)} = \frac{E}{6R}
\end{aligned}
$$
となります。したがって，展開式は
$$
\finalanswer{I_1(s) = \frac{E}{R}\left(\frac{2/3}{s} - \frac{1/2}{s + R/L} - \frac{1/6}{s + 3R/L}\right)}
$$
および
$$
\finalanswer{I_2(s) = \frac{E}{R}\left(\frac{1/3}{s} - \frac{1/2}{s + R/L} + \frac{1/6}{s + 3R/L}\right)}
$$
となります。

### (3)
部分分数展開の各項を逆ラプラス変換します。
$$
\finalanswer{i_1(t) = \frac{E}{R}\left(\frac{2}{3} - \frac{1}{2}\exp\left(-\frac{Rt}{L}\right) - \frac{1}{6}\exp\left(-\frac{3Rt}{L}\right)\right)}
$$
および
$$
\finalanswer{i_2(t) = \frac{E}{R}\left(\frac{1}{3} - \frac{1}{2}\exp\left(-\frac{Rt}{L}\right) + \frac{1}{6}\exp\left(-\frac{3Rt}{L}\right)\right)}
$$
となります。

$t \to \infty$ の極限をとると，指数関数項は $0$ に収束するため，定常電流は
$$
\finalanswer{i_1(\infty) = \frac{2E}{3R}}
$$
および
$$
\finalanswer{i_2(\infty) = \frac{E}{3R}}
$$
となります。インダクタを短絡とみなした純抵抗回路の直流解析結果と一致します。

===== FILE: 10integral_transforms/06/06_050.md =====
---
tags:
  - 標準
---

# インパルス応答と伝達関数

## 問題
入力 $x(t)$ と出力 $y(t)$ をもつ線形システムが次の2階微分方程式で記述される。
$$
\frac{d^2 y}{dt^2} + 3 \frac{dy}{dt} + 2 y = x(t)
$$
初期状態は静止状態にあるものとする（$y(0) = 0$，$y'(0) = 0$）。以下の問いに答えよ。

(1) 入力および出力のラプラス変換をそれぞれ $X(s) = \mathcal{L}[x(t)], Y(s) = \mathcal{L}[y(t)]$ とするとき，伝達関数 $H(s) = Y(s)/X(s)$ を求めよ。

(2) 入力が単位インパルス $x(t) = \delta(t)$（$\delta(t)$ はディラックのデルタ関数）であるときの出力，すなわちインパルス応答 $h(t) = \mathcal{L}^{-1}[H(s)]$（$t \ge 0$）を求めよ。

(3) 入力が単位ステップ関数 $x(t) = u(t)$（$t \ge 0$ で $1$，$t < 0$ で $0$）であるときのステップ応答 $y(t)$ を，インパルス応答 $h(t)$ との畳み込み積分 $y(t) = \int_0^t h(\tau) d\tau$ を計算することにより求めよ。

---

## 解答・解説

### (1)
静止初期条件 $y(0) = 0, y'(0) = 0$ のもとで方程式の両辺をラプラス変換します。
$$
(s^2 + 3s + 2) Y(s) = X(s)
$$
伝達関数の定義にしたがって整理すると，
$$
\finalanswer{H(s) = \frac{1}{s^2 + 3s + 2}}
$$
が得られます。

### (2)
インパルス応答は伝達関数の逆ラプラス変換です。分母を因数分解して部分分数に展開します。
$$
H(s) = \frac{1}{(s+1)(s+2)} = \frac{1}{s+1} - \frac{1}{s+2}
$$
各項を逆変換すると，
$$
\finalanswer{h(t) = e^{-t} - e^{-2t}}
$$
となります。

### (3)
単位ステップ入力に対する応答は，インパルス応答の時間積分として表されます。
$$
\begin{aligned}
y(t) &= \int_0^t h(\tau) d\tau \\
&= \int_0^t \left(e^{-\tau} - e^{-2\tau}\right) d\tau \\
&= \left[-e^{-\tau} + \frac{1}{2}e^{-2\tau}\right]_0^t
\end{aligned}
$$
上下端の値を代入して整理すると，
$$
\begin{aligned}
y(t) &= \left(-e^{-t} + \frac{1}{2}e^{-2t}\right) - \left(-1 + \frac{1}{2}\right) \\
&= \finalanswer{y(t) = \frac{1}{2} - e^{-t} + \frac{1}{2}e^{-2t}}
\end{aligned}
$$
となります。$t \to \infty$ で出力は定常値 $1/2$ に漸近し，微分方程式の特解と一致します。

===== FILE: 10integral_transforms/06/06_060.md =====
---
tags:
  - 発展
---

# 自己相関とウィーナー・ヒンチンの定理

## 問題
実数二乗可積分信号 $x(t)$ に対し，自己相関関数 $R(\tau)$ を次式で定義する。
$$
R(\tau) = \int_{-\infty}^\infty x(t) x(t + \tau) dt
$$
また，$x(t)$ のフーリエ変換を $\tilde{x}(\omega) = \int_{-\infty}^\infty x(t) e^{-i\omega t} dt$ とし，パワースペクトル密度を $S(\omega) = |\tilde{x}(\omega)|^2$ とする。以下の問いに答えよ。

(1) 自己相関関数が偶関数 $R(-\tau) = R(\tau)$ であることを示せ。また，$\tau = 0$ における値 $R(0)$ を信号の全エネルギー $E = \int_{-\infty}^\infty |x(t)|^2 dt$ を用いて表せ。

(2) 自己相関関数のフーリエ変換 $\tilde{R}(\omega) = \int_{-\infty}^\infty R(\tau) e^{-i\omega \tau} d\tau$ が，パワースペクトル密度 $S(\omega)$ に等しいこと（ウィーナー・ヒンチンの定理）を重積分の変数変換を用いて示せ。

(3) 信号 $x(t) = e^{-\alpha t} u(t)$（$\alpha > 0$，$u(t)$ は $t \ge 0$ で $1$，$t < 0$ で $0$ の単位ステップ関数）に対し，自己相関関数 $R(\tau)$ およびパワースペクトル密度 $S(\omega)$ を求めよ。

---

## 解答・解説

### (1)
定義式において置換積分を行います。
$$
R(-\tau) = \int_{-\infty}^\infty x(t) x(t - \tau) dt
$$
$u = t - \tau$ と置くと，$t = u + \tau$ かつ $dt = du$ となります。積分範囲は変わらないため，
$$
R(-\tau) = \int_{-\infty}^\infty x(u + \tau) x(u) du = \int_{-\infty}^\infty x(u) x(u + \tau) du
$$
となり，
$$
\finalanswer{R(-\tau) = R(\tau)}
$$
が示されます。

$\tau = 0$ を代入すると，
$$
R(0) = \int_{-\infty}^\infty x(t)^2 dt = \finalanswer{R(0) = E}
$$
となり，自己相関関数の原点での値は信号の全エネルギーに一致します。

### (2)
自己相関関数のフーリエ変換に定義を代入して二重積分の順序を交換します。
$$
\begin{aligned}
\tilde{R}(\omega) &= \int_{-\infty}^\infty \left(\int_{-\infty}^\infty x(t) x(t + \tau) dt\right) e^{-i\omega \tau} d\tau \\
&= \int_{-\infty}^\infty x(t) \left(\int_{-\infty}^\infty x(t + \tau) e^{-i\omega \tau} d\tau\right) dt
\end{aligned}
$$
内側の積分において $u = t + \tau$ と置換すると，$\tau = u - t$ かつ $d\tau = du$ となるため，
$$
\int_{-\infty}^\infty x(t + \tau) e^{-i\omega \tau} d\tau = \int_{-\infty}^\infty x(u) e^{-i\omega(u - t)} du = e^{i\omega t} \int_{-\infty}^\infty x(u) e^{-i\omega u} du = e^{i\omega t} \tilde{x}(\omega)
$$
が得られます。これを外側の積分に戻すと，
$$
\tilde{R}(\omega) = \tilde{x}(\omega) \int_{-\infty}^\infty x(t) e^{i\omega t} dt
$$
となります。実数信号の性質より $\int_{-\infty}^\infty x(t) e^{i\omega t} dt = \left(\int_{-\infty}^\infty x(t) e^{-i\omega t} dt\right)^* = \tilde{x}(\omega)^*$ が成り立つため，
$$
\finalanswer{\tilde{R}(\omega) = S(\omega)}
$$
が示されます。

### (3)
まずパワースペクトル密度を求めます。信号のフーリエ変換は
$$
\tilde{x}(\omega) = \int_0^\infty e^{-\alpha t} e^{-i\omega t} dt = \frac{1}{\alpha + i\omega}
$$
となるため，パワースペクトル密度は
$$
\finalanswer{S(\omega) = \frac{1}{\alpha^2 + \omega^2}}
$$
となります。

次に自己相関関数を計算します。$\tau \ge 0$ のとき，2つの関数の重なりは $t \ge 0$ の範囲であるため，
$$
R(\tau) = \int_0^\infty e^{-\alpha t} e^{-\alpha(t + \tau)} dt = e^{-\alpha\tau} \int_0^\infty e^{-2\alpha t} dt = \frac{e^{-\alpha\tau}}{2\alpha}
$$
となります。(1) で示した偶関数性 $R(-\tau) = R(\tau)$ より，負の領域も含めて絶対値記号でまとめると，
$$
\finalanswer{R(\tau) = \frac{1}{2\alpha} \exp(-\alpha |\tau|)}
$$
が得られます。この自己相関関数のフーリエ変換が $S(\omega)$ と厳密に一致することが確かめられます。

===== FILE: 10integral_transforms/06/06_070.md =====
---
tags:
  - 標準
---

# 離散フーリエ変換の入口

## 問題
長さ $N$ の有限離散複素データ列 $x_n$（$n = 0, 1, \dots, N-1$）に対する離散フーリエ変換（DFT）は，回転因子 $W_N = e^{-i 2\pi / N}$ を用いて次式で定義される。
$$
X_k = \sum_{n=0}^{N-1} x_n W_N^{kn} \quad (k = 0, 1, \dots, N-1)
$$
以下の問いに答えよ。

(1) 整数 $m$ に対し，和 $S_m = \sum_{n=0}^{N-1} W_N^{mn}$ を考える。$m$ が $N$ の倍数である場合，および $N$ の倍数でない場合について，等比数列の和の公式を用いて $S_m$ の値を求めよ。

(2) (1) の直交関係を用いて，DFT の定義式から逆離散フーリエ変換（IDFT）の公式
$$
x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k W_N^{-kn} \quad (n = 0, 1, \dots, N-1)
$$
を導け。

(3) データ長 $N = 4$ に対し，入力信号が $x_0 = 1, x_1 = 0, x_2 = -1, x_3 = 0$ で与えられるとき，離散フーリエ変換の各成分 $X_0, X_1, X_2, X_3$ を求めよ。

---

## 解答・解説

### (1)
回転因子の定義より $W_N^m = e^{-i 2\pi m / N}$ です。

$m$ が $N$ の整数倍である場合，$m/N$ は整数となるため $W_N^m = e^{-i 2\pi \times \text{整数}} = 1$ となります。したがって，和は
$$
\finalanswer{S_m = N}
$$
となります。

$m$ が $N$ の倍数でない場合，$W_N^m \ne 1$ であるため等比数列の和の公式を適用できます。
$$
S_m = \frac{1 - (W_N^m)^N}{1 - W_N^m} = \frac{1 - W_N^{mN}}{1 - W_N^m}
$$
ここで分子の指数は $W_N^{mN} = (e^{-i 2\pi / N})^{mN} = e^{-i 2\pi m} = 1$ となるため，分子が $0$ になります。したがって，
$$
\finalanswer{S_m = 0}
$$
となります。

### (2)
証明したい式の右辺に DFT の定義を代入し，和の順序を交換します。
$$
\begin{aligned}
\sum_{k=0}^{N-1} X_k W_N^{-km} &= \sum_{k=0}^{N-1} \left(\sum_{n=0}^{N-1} x_n W_N^{kn}\right) W_N^{-km} \\
&= \sum_{n=0}^{N-1} x_n \left(\sum_{k=0}^{N-1} W_N^{k(n-m)}\right)
\end{aligned}
$$
ここで内側の和に対して (1) の結果を適用します。$0 \le n, m \le N-1$ の範囲において $n - m$ が $N$ の倍数となるのは $n = m$ のときに限られます。したがって，内側の和はクロネッカーのデルタを用いて
$$
\sum_{k=0}^{N-1} W_N^{k(n-m)} = N \delta_{n, m}
$$
と表されます。これを代入すると，
$$
\sum_{k=0}^{N-1} X_k W_N^{-km} = \sum_{n=0}^{N-1} x_n N \delta_{n, m} = N x_m
$$
が得られます。両辺を $N$ で割り，添字 $m$ を $n$ に書き改めると，
$$
\finalanswer{x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k W_N^{-kn}}
$$
が導かれます。

### (3)
$N = 4$ のとき，回転因子は
$$
W_4 = e^{-i 2\pi / 4} = e^{-i\pi / 2} = -i
$$
となります。定義にしたがって各成分を計算します。
$$
X_k = x_0 W_4^0 + x_1 W_4^k + x_2 W_4^{2k} + x_3 W_4^{3k}
$$
入力信号の値 $x_0 = 1, x_1 = 0, x_2 = -1, x_3 = 0$ を代入すると，
$$
X_k = 1 - W_4^{2k} = 1 - (-i)^{2k} = 1 - (-1)^k
$$
となります。各 $k$ について計算すると，
$$
\begin{aligned}
k = 0: &\quad X_0 = 1 - 1 = \finalanswer{X_0 = 0} \\
k = 1: &\quad X_1 = 1 - (-1) = \finalanswer{X_1 = 2} \\
k = 2: &\quad X_2 = 1 - 1 = \finalanswer{X_2 = 0} \\
k = 3: &\quad X_3 = 1 - (-1) = \finalanswer{X_3 = 2}
\end{aligned}
$$
となります。直流成分（平均値）が $0$ であり，特定の周波数成分のみが抽出されていることがわかります。

===== END =====