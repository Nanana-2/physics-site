---
title: 東大理物 平成13年度 数学 第3問：減衰調和振動子のフーリエ変換とグリーン関数
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 積分変換
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成13年度
exam_subject: 数学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成13年度 数学 第3問：減衰調和振動子のフーリエ変換とグリーン関数

## 問題

未知関数 $x(t)$ に関する常微分方程式

$$
\frac{\mathrm{d}^2 x(t)}{\mathrm{d}t^2} + 2\alpha\frac{\mathrm{d}x(t)}{\mathrm{d}t} + \beta^2 x(t) = f(t)
$$

について以下の設問に答えよ。ここで，$\alpha$ および $\beta$ は正の定数とする。
{: .problem-lead }

(1) この方程式をフーリエ変換を用いて調べ，未知関数 $x$ を

$$
x(\omega) = C(\omega)f(\omega)
$$

の形で表せ。ただし $x(\omega), f(\omega)$ は $x(t), f(t)$ のフーリエ変換とする。

(2) $f(t) = \delta(t)$（デルタ関数）の場合を考える。(1) の結果を用い留数定理を適用して解 $x(t)$ を以下の場合について求めよ。

(i) $\alpha < \beta$

(ii) $\alpha = \beta$

(iii) $\alpha > \beta$

> 出典：東京大学大学院理学系研究科物理学専攻 平成13年度 数学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
定数係数の線形常微分方程式にフーリエ変換を行うと，時間微分 $\dfrac{\mathrm{d}}{\mathrm{d}t}$ が $-i\omega$ の掛け算に変わり，微分方程式が代数方程式 $x(\omega) = C(\omega)f(\omega)$ になります。

$f(t) = \delta(t)$ のときのフーリエ逆変換では，被積分関数の極は $\alpha > 0$ と $\beta > 0$ のため必ず複素 $\omega$ 平面の下半平面に現れます。$t < 0$ では上半平面，$t > 0$ では下半平面に半円を閉じて留数定理を用いると，極の配置に応じて3通りの解が導かれます。
</div>

### (1)

関数 $g(t)$ のフーリエ変換と逆変換を次で定めます。

$$
g(\omega) = \int_{-\infty}^{\infty} g(t) e^{i\omega t}\,\mathrm{d}t, \qquad g(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} g(\omega) e^{-i\omega t}\,\mathrm{d}\omega
$$

この定義のもとで，$x(t) = \dfrac{1}{2\pi}\int_{-\infty}^{\infty} x(\omega)e^{-i\omega t}\,\mathrm{d}\omega$ を時間 $t$ で1階および2階微分します。

$$
\begin{aligned}
\frac{\mathrm{d}x(t)}{\mathrm{d}t} &= \frac{1}{2\pi}\int_{-\infty}^{\infty} (-i\omega)x(\omega) e^{-i\omega t}\,\mathrm{d}\omega \\
\frac{\mathrm{d}^2 x(t)}{\mathrm{d}t^2} &= \frac{1}{2\pi}\int_{-\infty}^{\infty} (-\omega^2)x(\omega) e^{-i\omega t}\,\mathrm{d}\omega
\end{aligned}
$$

これらともとの常微分方程式の右辺 $f(t) = \dfrac{1}{2\pi}\int_{-\infty}^{\infty} f(\omega) e^{-i\omega t}\,\mathrm{d}\omega$ を方程式に代入します。

$$
\frac{1}{2\pi}\int_{-\infty}^{\infty} \bigl(-\omega^2 - 2i\alpha\omega + \beta^2\bigr) x(\omega) e^{-i\omega t}\,\mathrm{d}\omega = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(\omega) e^{-i\omega t}\,\mathrm{d}\omega
$$

フーリエ変換の一意性から，各 $\omega$ について次が成り立ちます。

$$
\bigl(-\omega^2 - 2i\alpha\omega + \beta^2\bigr) x(\omega) = f(\omega)
$$

両辺を $-\omega^2 - 2i\alpha\omega + \beta^2$ で割ります。

$$
x(\omega) = \frac{1}{-\omega^2 - 2i\alpha\omega + \beta^2}f(\omega)
$$

したがって，$x(\omega) = C(\omega)f(\omega)$ の形における $C(\omega)$ は次の通りです。

$$
\finalanswer{x(\omega) = C(\omega)f(\omega), \qquad C(\omega) = \frac{1}{-\omega^2 - 2i\alpha\omega + \beta^2} = -\frac{1}{\omega^2 + 2i\alpha\omega - \beta^2}}
$$

### (2)

$f(t) = \delta(t)$ のフーリエ変換は次になります。

$$
\begin{aligned}
f(\omega) &= \int_{-\infty}^{\infty} \delta(t) e^{i\omega t}\,\mathrm{d}t \\
&= 1
\end{aligned}
$$

よって (1) の結果から $x(\omega) = C(\omega)$ となり，フーリエ逆変換は次の形になります。

$$
x(t) = -\frac{1}{2\pi}\int_{-\infty}^{\infty} \frac{e^{-i\omega t}}{\omega^2 + 2i\alpha\omega - \beta^2}\,\mathrm{d}\omega
$$

分母の2次方程式 $\omega^2 + 2i\alpha\omega - \beta^2 = 0$ の根を解の公式で求めます。

$$
\omega_\pm = -i\alpha \pm \sqrt{\beta^2 - \alpha^2}
$$

$\alpha > 0$，$\beta > 0$ のとき，3つの場合すべてにおいて極の虚部は負です。

- $\alpha < \beta$ のとき：$\operatorname{Im}\omega_\pm = -\alpha < 0$。
- $\alpha = \beta$ のとき：重根 $\omega_0 = -i\alpha$ に対して $\operatorname{Im}\omega_0 = -\alpha < 0$。
- $\alpha > \beta$ のとき：$\sqrt{\alpha^2 - \beta^2} < \alpha$ なので $\operatorname{Im}\omega_\pm = -\alpha \pm \sqrt{\alpha^2 - \beta^2} < 0$。

複素 $\omega$ 平面で実軸上の区間 $[-R, R]$ と半径 $R$ の半円弧 $C_R^\pm$ を合わせた閉経路を考えます。$\omega = \omega_{\mathrm{r}} + i\omega_{\mathrm{i}}$ に対して $\bigl|e^{-i\omega t}\bigr| = e^{\omega_{\mathrm{i}} t}$ です。

$t < 0$ のときは上半平面の半円弧 $C_R^+$（$\omega_{\mathrm{i}} \ge 0$）で閉経路をとると，ジョルダンの補題より $R \to \infty$ で半円弧上の積分は $0$ に収束します。上半平面には被積分関数の極が存在しないため，コーシーの積分定理からいずれの場合も $x(t) = 0$ です。

$t > 0$ のときは下半平面の半円弧 $C_R^-$（$\omega_{\mathrm{i}} \le 0$）で時計回りの閉経路をとると，$R \to \infty$ で半円弧上の積分は $0$ に収束します。時計回りの向きを考慮して留数定理を使うと次になります。

$$
\begin{aligned}
x(t) &= -\frac{1}{2\pi} \cdot (-2\pi i)\sum_{\operatorname{Im}\omega_k < 0} \operatorname{Res}_{\omega = \omega_k}\left(\frac{e^{-i\omega t}}{\omega^2 + 2i\alpha\omega - \beta^2}\right) \\
&= i\sum_{\operatorname{Im}\omega_k < 0} \operatorname{Res}_{\omega = \omega_k}\left(\frac{e^{-i\omega t}}{\omega^2 + 2i\alpha\omega - \beta^2}\right)
\end{aligned}
$$

以下，$t > 0$ の各場合について留数を計算します。

#### (i) $\alpha < \beta$

$\omega_1 = \sqrt{\beta^2 - \alpha^2} > 0$ とおきます。2つの1位の極は $\omega_+ = -i\alpha + \omega_1$，$\omega_- = -i\alpha - \omega_1$ であり，$\omega_+ - \omega_- = 2\omega_1$ です。各極での留数を求めます。

$$
\begin{aligned}
\operatorname{Res}_{\omega = \omega_+}\left(\frac{e^{-i\omega t}}{(\omega - \omega_+)(\omega - \omega_-)}\right) &= \frac{e^{-i(-i\alpha + \omega_1)t}}{2\omega_1} \\
&= \frac{e^{-\alpha t} e^{-i\omega_1 t}}{2\omega_1}
\end{aligned}
$$

$$
\begin{aligned}
\operatorname{Res}_{\omega = \omega_-}\left(\frac{e^{-i\omega t}}{(\omega - \omega_+)(\omega - \omega_-)}\right) &= \frac{e^{-i(-i\alpha - \omega_1)t}}{-2\omega_1} \\
&= -\frac{e^{-\alpha t} e^{i\omega_1 t}}{2\omega_1}
\end{aligned}
$$

留数の和に $i$ を掛けます。

$$
\begin{aligned}
x(t) &= i\left(\frac{e^{-\alpha t} e^{-i\omega_1 t}}{2\omega_1} - \frac{e^{-\alpha t} e^{i\omega_1 t}}{2\omega_1}\right) \\
&= \frac{e^{-\alpha t}}{\omega_1}\cdot\frac{e^{i\omega_1 t} - e^{-i\omega_1 t}}{2i} \\
&= \frac{e^{-\alpha t}}{\sqrt{\beta^2 - \alpha^2}}\sin\left(\sqrt{\beta^2 - \alpha^2}\,t\right)
\end{aligned}
$$

したがって，$\alpha < \beta$ の解は次の通りです。

$$
\finalanswer{x(t) = \begin{cases} 0 & (t < 0) \\ \dfrac{e^{-\alpha t}}{\sqrt{\beta^2 - \alpha^2}}\sin\left(\sqrt{\beta^2 - \alpha^2}\,t\right) & (t > 0) \end{cases}}
$$

#### (ii) $\alpha = \beta$

分母は $(\omega + i\alpha)^2$ となり，$\omega_0 = -i\alpha$ が2位の極になります。2位の極での留数を計算します。

$$
\begin{aligned}
\operatorname{Res}_{\omega = -i\alpha}\left(\frac{e^{-i\omega t}}{(\omega + i\alpha)^2}\right) &= \left.\frac{\mathrm{d}}{\mathrm{d}\omega}\left(e^{-i\omega t}\right)\right|_{\omega = -i\alpha} \\
&= \left.(-i t e^{-i\omega t})\right|_{\omega = -i\alpha} \\
&= -i t e^{-\alpha t}
\end{aligned}
$$

これに $i$ を掛けます。

$$
\begin{aligned}
x(t) &= i\left(-i t e^{-\alpha t}\right) \\
&= t e^{-\alpha t}
\end{aligned}
$$

したがって，$\alpha = \beta$ の解は次の通りです。

$$
\finalanswer{x(t) = \begin{cases} 0 & (t < 0) \\ t e^{-\alpha t} & (t > 0) \end{cases}}
$$

#### (iii) $\alpha > \beta$

$\gamma = \sqrt{\alpha^2 - \beta^2} > 0$ とおきます。2つの1位の極は $\omega_+ = -i(\alpha - \gamma)$，$\omega_- = -i(\alpha + \gamma)$ であり，$\omega_+ - \omega_- = 2i\gamma$ です。各極での留数を求めます。

$$
\begin{aligned}
\operatorname{Res}_{\omega = \omega_+}\left(\frac{e^{-i\omega t}}{(\omega - \omega_+)(\omega - \omega_-)}\right) &= \frac{e^{-(\alpha - \gamma)t}}{2i\gamma} \\
\operatorname{Res}_{\omega = \omega_-}\left(\frac{e^{-i\omega t}}{(\omega - \omega_+)(\omega - \omega_-)}\right) &= -\frac{e^{-(\alpha + \gamma)t}}{2i\gamma}
\end{aligned}
$$

留数の和に $i$ を掛けます。

$$
\begin{aligned}
x(t) &= i\cdot\frac{e^{-(\alpha - \gamma)t} - e^{-(\alpha + \gamma)t}}{2i\gamma} \\
&= \frac{e^{-\alpha t}}{\gamma}\cdot\frac{e^{\gamma t} - e^{-\gamma t}}{2} \\
&= \frac{e^{-\alpha t}}{\sqrt{\alpha^2 - \beta^2}}\sinh\left(\sqrt{\alpha^2 - \beta^2}\,t\right)
\end{aligned}
$$

したがって，$\alpha > \beta$ の解は次の通りです。

$$
\finalanswer{x(t) = \begin{cases} 0 & (t < 0) \\ \dfrac{e^{-\alpha t}}{\sqrt{\alpha^2 - \beta^2}}\sinh\left(\sqrt{\alpha^2 - \beta^2}\,t\right) & (t > 0) \end{cases}}
$$

<aside class="rigor-note" markdown>
(1) でフーリエ変換の符号規約を $g(\omega) = \int_{-\infty}^{\infty} g(t)e^{-i\omega t}\,\mathrm{d}t$ と選んだ場合は，$C(\omega) = \dfrac{1}{-\omega^2 + 2i\alpha\omega + \beta^2}$ となります。このとき極はすべて上半平面に現れ，$t > 0$ で上半平面，$t < 0$ で下半平面の閉経路をとることで，(2) の実空間の解 $x(t)$ はまったく同じ式になります。また，得られた3つの解はいずれも $x(0^+) = 0$，$\dot{x}(0^+) = 1$ を満たしており，(i) と (iii) で $\alpha \to \beta$ の極限をとると (ii) の $t e^{-\alpha t}$ に一致します。
</aside>
