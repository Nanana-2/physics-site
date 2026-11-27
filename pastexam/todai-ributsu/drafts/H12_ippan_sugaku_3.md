---
title: 東大理物 平成12年度 一般教育科目 数学 第3問：1次元熱伝導方程式のグリーン関数
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 積分変換
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 一般教育科目 数学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成12年度 一般教育科目 数学 第3問：1次元熱伝導方程式のグリーン関数

## 問題

時刻 $t = 0$ において $x = 0$ に強さ $1$ の熱を加えたときの，1次元空間におけるその後の熱の伝導は，方程式，

$$
\left(\kappa^2\frac{\partial^2}{\partial x^2} - \frac{\partial}{\partial t}\right)G(x, t) = -\delta(x)\delta(t) \qquad (\kappa\text{ は正定数}), \tag{1}
$$

の解 $G(x, t)$ によって記述される。ただし，$\delta(x)$ はディラックのデルタ関数である。また，$t = -\infty$ で $G(x, t) = 0$ とする。
{: .problem-lead }

(1) $G(x, t)$ のフーリエ変換 $g(k, \omega)$ を次の式で定義する：

$$
G(x, t) = \frac{1}{(2\pi)^2}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} g(k, \omega)e^{i(kx - \omega t)}\,\mathrm{d}k\,\mathrm{d}\omega \tag{2}
$$

このとき $g(k, \omega)$ の満たすべき方程式を式 (1) より導き，$g(k, \omega)$ を求めよ。

(2) 設問 (1) で求めた $g(k, \omega)$ を式 (2) に代入し，$\omega$ 積分を実行せよ。

(3) 設問 (2) に続いて $k$ 積分を実行し，$G(x, t)$ を求めよ。ただし，

$$
\int_{-\infty}^{\infty} e^{-\alpha^2}\,\mathrm{d}\alpha = \sqrt{\pi} \tag{3}
$$

を用いてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 一般教育科目 数学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
時間と空間の両方について2次元フーリエ変換を行うと，偏微分 $\dfrac{\partial}{\partial x}$ が $ik$，$\dfrac{\partial}{\partial t}$ が $-i\omega$ に置き換わり，熱伝導方程式は $g(k, \omega)$ に関する代数方程式になります。

$\omega$ 積分では極が複素 $\omega$ 平面の下半平面 $\omega = -i\kappa^2 k^2$ に位置するため，$t < 0$ で上半平面，$t > 0$ で下半平面の半円弧を閉じて留数定理を用いることで因果律 $G(x, t) = 0$（$t < 0$）が満たされます。続く $k$ 積分は指数部の平方完成とガウス積分によって閉じます。
</div>

### (1)

式 (2) の両辺に演算子 $\kappa^2\dfrac{\partial^2}{\partial x^2} - \dfrac{\partial}{\partial t}$ を作用させます。

$$
\begin{aligned}
\left(\kappa^2\frac{\partial^2}{\partial x^2} - \frac{\partial}{\partial t}\right)G(x, t) &= \frac{1}{(2\pi)^2}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} \bigl[\kappa^2(ik)^2 - (-i\omega)\bigr]g(k, \omega)e^{i(kx - \omega t)}\,\mathrm{d}k\,\mathrm{d}\omega \\
&= \frac{1}{(2\pi)^2}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} \bigl(-\kappa^2 k^2 + i\omega\bigr)g(k, \omega)e^{i(kx - \omega t)}\,\mathrm{d}k\,\mathrm{d}\omega
\end{aligned}
$$

一方，ディラックのデルタ関数のフーリエ積分表示は次の通りです。

$$
\delta(x)\delta(t) = \frac{1}{(2\pi)^2}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{i(kx - \omega t)}\,\mathrm{d}k\,\mathrm{d}\omega
$$

これらを式 (1) に代入します。

$$
\frac{1}{(2\pi)^2}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} \bigl(-\kappa^2 k^2 + i\omega\bigr)g(k, \omega)e^{i(kx - \omega t)}\,\mathrm{d}k\,\mathrm{d}\omega = -\frac{1}{(2\pi)^2}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{i(kx - \omega t)}\,\mathrm{d}k\,\mathrm{d}\omega
$$

フーリエ変換の一意性から，$g(k, \omega)$ が満たすべき方程式が得られます。

$$
\bigl(-\kappa^2 k^2 + i\omega\bigr)g(k, \omega) = -1
$$

両辺に $-1$ を掛けると $\bigl(\kappa^2 k^2 - i\omega\bigr)g(k, \omega) = 1$ です。これを $g(k, \omega)$ について解きます。

$$
\begin{aligned}
g(k, \omega) &= \frac{1}{\kappa^2 k^2 - i\omega} \\
&= \frac{i}{\omega + i\kappa^2 k^2}
\end{aligned}
$$

したがって，$g(k, \omega)$ の満たすべき方程式とその解は次の通りです。

$$
\finalanswer{\bigl(-\kappa^2 k^2 + i\omega\bigr)g(k, \omega) = -1, \qquad g(k, \omega) = \frac{1}{\kappa^2 k^2 - i\omega} = \frac{i}{\omega + i\kappa^2 k^2}}
$$

### (2)

(1) の $g(k, \omega)$ を式 (2) に代入し，$\omega$ に関する積分 $I_\omega(k, t)$ を取り出します。

$$
G(x, t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx} I_\omega(k, t)\,\mathrm{d}k
$$

$$
I_\omega(k, t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \frac{i e^{-i\omega t}}{\omega + i\kappa^2 k^2}\,\mathrm{d}\omega
$$

被積分関数は複素 $\omega$ 平面上に1位の極 $\omega_0 = -i\kappa^2 k^2$ をもちます。$k \neq 0$ のとき $\kappa > 0$ より $\operatorname{Im}\omega_0 = -\kappa^2 k^2 < 0$ であり，極は下半平面にあります。また $k = 0$ でも条件 $G(x, -\infty) = 0$ を満たすよう極を下半平面側に微小量 $-i\varepsilon$（$\varepsilon \to 0^+$）だけずらして $\omega_0 = -i(\kappa^2 k^2 + \varepsilon)$ と扱います。

$\omega = \omega_{\mathrm{r}} + i\omega_{\mathrm{i}}$ に対して $\bigl|e^{-i\omega t}\bigr| = e^{\omega_{\mathrm{i}} t}$ なので，$t$ の符号によって閉経路の向きを選びます。

$t < 0$ のときは上半平面（$\omega_{\mathrm{i}} \ge 0$）に半径 $R$ の半円弧 $C_R^+$ を閉じて $R \to \infty$ とします。ジョルダンの補題により半円弧上の積分は $0$ に収束し，上半平面内に極は存在しないため，コーシーの積分定理から $I_\omega(k, t) = 0$ となります。これにより境界条件 $G(x, -\infty) = 0$ が満たされます。

$t > 0$ のときは下半平面（$\omega_{\mathrm{i}} \le 0$）に半径 $R$ の半円弧 $C_R^-$ を時計回りに閉じて $R \to \infty$ とします。ジョルダンの補題により半円弧上の積分は $0$ に収束し，時計回りの留数定理を用いて次が得られます。

$$
\begin{aligned}
I_\omega(k, t) &= \frac{1}{2\pi} \cdot (-2\pi i)\operatorname{Res}_{\omega = -i\kappa^2 k^2}\left(\frac{i e^{-i\omega t}}{\omega + i\kappa^2 k^2}\right) \\
&= (-i)\cdot i e^{-i(-i\kappa^2 k^2)t} \\
&= e^{-\kappa^2 k^2 t}
\end{aligned}
$$

したがって，$\omega$ 積分を行った結果は次の通りです。

$$
\finalanswer{G(x, t) = \begin{cases} \dfrac{1}{2\pi}\displaystyle\int_{-\infty}^{\infty} e^{-\kappa^2 k^2 t + ikx}\,\mathrm{d}k & (t > 0) \\[2ex] 0 & (t < 0) \end{cases}}
$$

### (3)

$t < 0$ では (2) の通り $G(x, t) = 0$ です。$t > 0$ のとき，指数部分を $k$ について平方完成します。

$$
\begin{aligned}
-\kappa^2 t k^2 + ikx &= -\kappa^2 t\left(k^2 - \frac{ix}{\kappa^2 t}k\right) \\
&= -\kappa^2 t\left[\left(k - \frac{ix}{2\kappa^2 t}\right)^2 + \frac{x^2}{4\kappa^4 t^2}\right] \\
&= -\kappa^2 t\left(k - \frac{ix}{2\kappa^2 t}\right)^2 - \frac{x^2}{4\kappa^2 t}
\end{aligned}
$$

これを (2) の積分に代入します。

$$
G(x, t) = \frac{1}{2\pi}\exp\left(-\frac{x^2}{4\kappa^2 t}\right)\int_{-\infty}^{\infty} \exp\left[-\kappa^2 t\left(k - \frac{ix}{2\kappa^2 t}\right)^2\right]\mathrm{d}k
$$

ここで変数変換 $\alpha = \kappa\sqrt{t}\left(k - \dfrac{ix}{2\kappa^2 t}\right)$（$\mathrm{d}k = \dfrac{\mathrm{d}\alpha}{\kappa\sqrt{t}}$）を行います。被積分関数 $e^{-\alpha^2}$ は全複素平面で正則であり，$|\operatorname{Re}\alpha| \to \infty$ で $0$ に急速に減衰するため，コーシーの積分定理より実軸に平行な直線 $\operatorname{Im}\alpha = -\dfrac{x}{2\kappa\sqrt{t}}$ 上の積分は実軸上の積分と一致します。式 (3) を用いて計算します。

$$
\begin{aligned}
G(x, t) &= \frac{1}{2\pi}\exp\left(-\frac{x^2}{4\kappa^2 t}\right)\cdot\frac{1}{\kappa\sqrt{t}}\int_{-\infty}^{\infty} e^{-\alpha^2}\,\mathrm{d}\alpha \\
&= \frac{1}{2\pi\kappa\sqrt{t}}\exp\left(-\frac{x^2}{4\kappa^2 t}\right)\cdot\sqrt{\pi} \\
&= \frac{1}{2\kappa\sqrt{\pi t}}\exp\left(-\frac{x^2}{4\kappa^2 t}\right)
\end{aligned}
$$

以上より，1次元熱伝導方程式のグリーン関数 $G(x, t)$ は次の通りです。

$$
\finalanswer{G(x, t) = \begin{cases} \dfrac{1}{2\kappa\sqrt{\pi t}}\exp\left(-\dfrac{x^2}{4\kappa^2 t}\right) & (t > 0) \\[2ex] 0 & (t < 0) \end{cases}}
$$

<aside class="rigor-note" markdown>
得られた $G(x, t)$ を $t > 0$ で全空間について積分すると，$\int_{-\infty}^{\infty} G(x, t)\,\mathrm{d}x = 1$ となり，$t = 0$ に加えた強さ $1$ の熱量が時刻によらず保存されることが確かめられます。また $t \to 0^+$ の極限では分布の幅 $\sqrt{2}\kappa\sqrt{t}$ が $0$ に縮みながら全面積 $1$ を保つため，$G(x, t) \to \delta(x)$ となります。
</aside>
