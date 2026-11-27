---
title: 東大理物 平成10年度 物理学 第7問：1次元ヘルムホルツ方程式のグリーン関数・無限弦の波動方程式と2次元ラプラス方程式
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 積分変換
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 物理学
exam_number: 第7問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成10年度 物理学 第7問：1次元ヘルムホルツ方程式のグリーン関数・無限弦の波動方程式と2次元ラプラス方程式

## 問題

(1) 次の方程式 (1) を満足する有界な1次元の関数 $\phi(x)$ を，フーリエ変換の方法によって求めたい。

$$
\left(-\frac{\mathrm{d}^2}{\mathrm{d}x^2} + \lambda^2\right)\phi(x) = \delta(x - a) \qquad \text{(1)}
$$

ただし $\delta(x)$ はデルタ関数であり，$\lambda$ は正の実数である。

(a) $\phi(x)$ のフーリエ変換を $\hat{\phi}(k)$ とするとき，$\hat{\phi}(k)$ の満たす方程式をもとめ，$\hat{\phi}(k)$ を決定せよ。

(b) $\phi(x)$ をもとめよ。

(2) 振幅 $\psi(x, t)$ の満たす運動方程式が

$$
\frac{\partial^2\psi}{\partial t^2} = v^2\frac{\partial^2\psi}{\partial x^2} \qquad \text{(2)}
$$

で表わされる1次元の無限に長い弦の振動を，初期条件

$$
\begin{aligned}
\text{(A)}\quad \psi(x, t = 0) &= |x - 2n\pi| - \frac{\pi}{2} \qquad \text{(3)} \\
(2n - 1)\pi &< x < (2n + 1)\pi \qquad \text{(4)} \\
n &= 0, \pm 1, \pm 2, \dots \qquad \text{(5)} \\
\text{(B)}\quad \frac{\partial\psi(x, t = 0)}{\partial t} &= 0 \qquad \text{(6)}
\end{aligned}
$$

を満たすように決定せよ。また $0 \le t \le \pi/(2v)$ の時間範囲で，$\psi(x, t)$ がどのように変化するかを，述べよ。

(3) 2次元空間における関数 $\psi$ は半径 $a$ の円の外部で有界で，2次元のラプラス方程式

$$
\Delta\psi = \frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} = 0 \qquad \text{(7)}
$$

を満たし，円周上の極座標 $(a, \theta)$ で表わされる点では

$$
\psi(a, \theta) = \cos^2\theta \qquad \text{(8)}
$$

という値をとる。$\psi$ を決定せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 物理学 第7問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
数理物理学の典型的な3つの偏微分・常微分方程式を解きます。設問 (1) では1次元修正ヘルムホルツ方程式のグリーン関数をフーリエ変換と留数定理によって導出します。

設問 (2) では周期三角波を初期変位とする1次元波動方程式をダランベールの公式とフーリエ級数展開の両面から解き，2つの進行波の重ね合わせによる波形変化を調べます。設問 (3) では2次元ラプラス方程式を極座標で変数分離し，無限遠での有界条件と円周上の境界条件から一意解を決定します。
</div>

### (1)(a)

関数 $\phi(x)$ のフーリエ変換 $\hat{\phi}(k)$ および逆変換を次のように定義します。

$$
\begin{aligned}
\hat{\phi}(k) &= \int_{-\infty}^{\infty} \phi(x) e^{-ikx}\,\mathrm{d}x \\
\phi(x) &= \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat{\phi}(k) e^{ikx}\,\mathrm{d}k
\end{aligned}
$$

方程式 (1) の両辺に $e^{-ikx}$ を掛けて全実軸で積分します。有界なグリーン関数は $|x| \to \infty$ で $\phi(x), \phi'(x) \to 0$ を満たすため，部分積分を2回行うことで $-\dfrac{\mathrm{d}^2\phi}{\mathrm{d}x^2}$ のフーリエ変換は $k^2\hat{\phi}(k)$ となります。またデルタ関数のフーリエ変換は $\int_{-\infty}^{\infty}\delta(x - a)e^{-ikx}\,\mathrm{d}x = e^{-ika}$ です。

したがって $\hat{\phi}(k)$ の満たす方程式は次の通りです。

$$
(k^2 + \lambda^2)\hat{\phi}(k) = e^{-ika}
$$

$\lambda > 0$ よりすべての実数 $k$ に対して $k^2 + \lambda^2 > 0$ なので，両辺を $k^2 + \lambda^2$ で割って $\hat{\phi}(k)$ が決定されます。

$$
\finalanswer{(k^2 + \lambda^2)\hat{\phi}(k) = e^{-ika},\qquad \hat{\phi}(k) = \frac{e^{-ika}}{k^2 + \lambda^2}}
$$

<aside class="rigor-note" markdown>
フーリエ変換に $\dfrac{1}{\sqrt{2\pi}}$ の対称係数をつける流儀をとった場合は，方程式は $(k^2 + \lambda^2)\hat{\phi}(k) = \dfrac{e^{-ika}}{\sqrt{2\pi}}$，解は $\hat{\phi}(k) = \dfrac{e^{-ika}}{\sqrt{2\pi}(k^2 + \lambda^2)}$ となりますが，逆変換で得られる $\phi(x)$ は定義の流儀によらず同一です。
</aside>

### (1)(b)

(1)(a) で得た $\hat{\phi}(k)$ をフーリエ逆変換します。

$$
\phi(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \frac{e^{ik(x - a)}}{k^2 + \lambda^2}\,\mathrm{d}k
$$

複素 $k$ 平面において被積分関数 $g(k) = \dfrac{e^{ik(x - a)}}{(k - i\lambda)(k + i\lambda)}$ は上半面の $k = +i\lambda$ と下半面の $k = -i\lambda$ に1位の極をもちます。$x - a$ の符号で積分経路を閉じ分けます。

まず $x - a \ge 0$ のとき，上半面の半径 $R$ の半円弧 $C_+$ で閉経路をつくると，ジョルダンの補題により $R \to \infty$ で半円弧上の積分は $0$ に収束します。閉経路内の極は $k = i\lambda$ のみなので，留数定理より次式が得られます。

$$
\begin{aligned}
\phi(x) &= \frac{1}{2\pi}\cdot 2\pi i \operatorname{Res}_{k = i\lambda}\frac{e^{ik(x - a)}}{(k - i\lambda)(k + i\lambda)} \\
&= i\frac{e^{-\lambda(x - a)}}{2i\lambda} \\
&= \frac{1}{2\lambda}e^{-\lambda(x - a)}
\end{aligned}
$$

次に $x - a < 0$ のとき，下半面の半円弧 $C_-$ を時計回りに閉じて経路をつくると，極 $k = -i\lambda$ の留数に負号をつけて次式が得られます。

$$
\begin{aligned}
\phi(x) &= \frac{1}{2\pi}\cdot (-2\pi i)\operatorname{Res}_{k = -i\lambda}\frac{e^{ik(x - a)}}{(k - i\lambda)(k + i\lambda)} \\
&= -i\frac{e^{\lambda(x - a)}}{-2i\lambda} \\
&= \frac{1}{2\lambda}e^{\lambda(x - a)}
\end{aligned}
$$

両者をまとめると，有界な解 $\phi(x)$ は次のようになります。

$$
\finalanswer{\phi(x) = \frac{1}{2\lambda}e^{-\lambda|x - a|}}
$$

### (2)

初期変位を $f(x) = \psi(x, 0)$ とおきます。$f(x)$ は周期 $2\pi$ の連続な偶関数の三角波であり，$(2n - 1)\pi \le x \le (2n + 1)\pi$ で $f(x) = |x - 2n\pi| - \dfrac{\pi}{2}$ です。

1次元波動方程式 $\dfrac{\partial^2\psi}{\partial t^2} = v^2\dfrac{\partial^2\psi}{\partial x^2}$ の一般解はダランベールの公式で与えられます。初期条件 $\psi(x, 0) = f(x)$ および $\dfrac{\partial\psi}{\partial t}(x, 0) = 0$ を用いると，解は次の形に一意に定まります。

$$
\psi(x, t) = \frac{1}{2}\bigl(f(x - vt) + f(x + vt)\bigr)
$$

ここで $f(x)$ は周期 $2\pi$ の偶関数なので，フーリエ級数展開すると次の表示も得られます。

$$
f(x) = -\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos\bigl((2k + 1)x\bigr)}{(2k + 1)^2}
$$

これをダランベールの解に代入し，和積公式 $\dfrac{1}{2}\bigl(\cos(m(x - vt)) + \cos(m(x + vt))\bigr) = \cos(mx)\cos(mvt)$ を用いると，フーリエ級数表示は次の通りです。

$$
\psi(x, t) = -\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos\bigl((2k + 1)x\bigr)\cos\bigl((2k + 1)vt\bigr)}{(2k + 1)^2}
$$

次に $0 \le t \le \dfrac{\pi}{2v}$ の範囲での波形の時間変化を調べます。周期性と偶対称性より，半周期区間 $0 \le x \le \pi$ で考えれば十分です。$s = vt$（$0 \le s \le \dfrac{\pi}{2}$）とおき，$x - s$ と $x + s$ がどの区間に属するかで場合分けします。

まず $0 \le x \le s$ のとき，$x - s \in [-\pi, 0]$ かつ $x + s \in [0, \pi]$ なので，$f(x - s) = (s - x) - \dfrac{\pi}{2}$，$f(x + s) = (x + s) - \dfrac{\pi}{2}$ となり，次式が得られます。

$$
\begin{aligned}
\psi(x, t) &= s - \frac{\pi}{2} \\
&= vt - \frac{\pi}{2}
\end{aligned}
$$

次に $s \le x \le \pi - s$ のとき，$x - s, x + s \in [0, \pi]$ なので，$f(x - s) = (x - s) - \dfrac{\pi}{2}$，$f(x + s) = (x + s) - \dfrac{\pi}{2}$ となり，次式が得られます。

$$
\psi(x, t) = x - \frac{\pi}{2}
$$

最後に $\pi - s \le x \le \pi$ のとき，$x - s \in [0, \pi]$ かつ $x + s \in [\pi, 2\pi]$ なので，$f(x - s) = (x - s) - \dfrac{\pi}{2}$，$f(x + s) = (2\pi - x - s) - \dfrac{\pi}{2}$ となり，次式が得られます。

$$
\begin{aligned}
\psi(x, t) &= \frac{\pi}{2} - s \\
&= \frac{\pi}{2} - vt
\end{aligned}
$$

したがって $0 \le t \le \dfrac{\pi}{2v}$ の間，波形は次のように変化します。

- $t = 0$ では，各 $x = 2n\pi$ に変位 $-\dfrac{\pi}{2}$ の尖った谷，各 $x = (2n + 1)\pi$ に変位 $+\dfrac{\pi}{2}$ の尖った山をもつ三角波です。
- $0 < t < \dfrac{\pi}{2v}$ では，すべての山と谷の先端が水平に削り取られた対称な台形波となります。$x = 2n\pi$ 付近の谷は幅 $2vt$，高さ $-\left(\dfrac{\pi}{2} - vt\right)$ の水平な底になって上昇し，$x = (2n + 1)\pi$ 付近の山は幅 $2vt$，高さ $\dfrac{\pi}{2} - vt$ の水平な頂になって下降します。一方，その間の斜面部分の傾きは $\pm 1$ のまま変化しません。
- $t = \dfrac{\pi}{2v}$ に達すると，水平部分の幅が $\pi$ となって斜面部分が完全に消滅し，弦全体がすべての $x$ で $\psi\left(x, \dfrac{\pi}{2v}\right) \equiv 0$ の一直線になります。この瞬間は変位が $0$ である代わりに，各点の速度が最大となっています。

以上をまとめると，求める解は次の通りです。

$$
\finalanswer{\psi(x, t) = \frac{1}{2}\bigl(f(x - vt) + f(x + vt)\bigr) = -\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos\bigl((2k + 1)x\bigr)\cos\bigl((2k + 1)vt\bigr)}{(2k + 1)^2}}
$$

### (3)

2次元極座標 $(r, \theta)$ を用いると，2次元ラプラス方程式は次の形になります。

$$
\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial\psi}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2\psi}{\partial\theta^2} = 0
$$

変数分離 $\psi(r, \theta) = R(r)\Theta(\theta)$ を行い，角度方向の一価性 $\Theta(\theta + 2\pi) = \Theta(\theta)$ を課すと，分離定数は $m^2$（$m = 0, 1, 2, \dots$）となります。それぞれの $m$ に対する動径方程式 $r^2 R'' + r R' - m^2 R = 0$ の一般解は次の通りです。

- $m = 0$：$R_0(r) = A_0 + B_0\ln r$
- $m \ge 1$：$R_m(r) = A_m r^m + B_m r^{-m}$

関数 $\psi(r, \theta)$ は円の外部 $r \ge a$ で有界であるため，$r \to \infty$ で発散する項 $\ln r$ および $r^m$（$m \ge 1$）の係数はすべて $0$ である必要があります。すなわち $B_0 = 0$ かつすべての $m \ge 1$ で $A_m = 0$ です。

したがって外部領域 $r \ge a$ における有界な調和関数の一般形は次のようになります。

$$
\psi(r, \theta) = A_0 + \sum_{m=1}^{\infty} r^{-m}\bigl(C_m\cos m\theta + D_m\sin m\theta\bigr)
$$

ここで $r = a$ の円周上の境界条件を半角公式でフーリエ級数の形に書き換えます。

$$
\begin{aligned}
\psi(a, \theta) &= \cos^2\theta \\
&= \frac{1}{2} + \frac{1}{2}\cos 2\theta
\end{aligned}
$$

三角関数の直交性により両式の係数を比較すると，$A_0 = \dfrac{1}{2}$，$C_2 a^{-2} = \dfrac{1}{2}$ より $C_2 = \dfrac{a^2}{2}$ となり，それ以外のすべての係数は $0$ と一意に定まります。

よって求める関数 $\psi(r, \theta)$（$r \ge a$）は次の通りです。

$$
\finalanswer{\psi(r, \theta) = \frac{1}{2} + \frac{a^2}{2r^2}\cos 2\theta \qquad (r \ge a)}
$$
