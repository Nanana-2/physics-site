---
title: 東大理物 平成29年度 物理学 第1問：放物型ポテンシャル中の相互作用二粒子とクエンチ後の時間発展
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成29年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成29年度 物理学 第1問：放物型ポテンシャル中の相互作用二粒子とクエンチ後の時間発展

## 問題

1次元放物型ポテンシャル中の質量 $m$ の互いに区別できる2粒子を考える。これらの粒子の位置を $x_1,\ x_2$ とし，粒子間には距離の2乗に比例した相互作用が働くものとする。このとき，全系を記述するハミルトニアンは次のように与えられる。

$$
H = -\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x_1^2} + \frac{\partial^2}{\partial x_2^2}\right) + \frac{m\omega^2}{2}\left(x_1^2 + x_2^2\right) + \frac{m\omega^2\alpha}{4}\left(x_1 - x_2\right)^2
$$

ここで，$\omega\ (> 0)$ はポテンシャルの閉じ込めの強さを表す定数，$\alpha$ は粒子間の相互作用の強さを表す定数であり，$\hbar$ はプランク定数を $2\pi$ で割った量である。以下の設問に答えよ。なお，必要があれば，1次元調和振動子の基底状態の規格化された波動関数が適当な定数 $c\ (> 0)$ を用いて

$$
\left(\frac{c}{\pi}\right)^{\frac{1}{4}} e^{-\frac{c}{2}x^2}
$$

の形に書けること，また，積分公式

$$
\int_{-\infty}^{\infty} e^{-cx^2}\,dx = \sqrt{\frac{\pi}{c}}
$$

を用いてもよい。

(1) ハミルトニアン $H$ を運動エネルギーの部分 $K$ とそれ以外の部分 $V$ に分け（$H = K + V$），$K$ と $V$ をそれぞれ2粒子の重心座標 $x = (x_1 + x_2)/2$ と相対座標 $y = x_1 - x_2$ およびそれらに関する微分を用いて表せ。

(2) 設問1の $V$ に関する結果を用いると，系が安定に存在するための必要十分条件は，$\alpha_0$ をある定数として $\alpha > \alpha_0$ であることが分かる。$\alpha_0$ の値を求めよ。

(3) $\alpha > \alpha_0$ の場合に，系の基底状態のエネルギーを求めよ。また，規格化された波動関数を $x$ と $y$ の関数として求めよ。

以下では，波動関数の時間依存性を考える。時刻 $t < 0$ で系は $\alpha = 0$ の基底状態にあったとする。時刻 $t = 0$ で $\alpha$ の値を突然 $\alpha = \alpha_0$ に変え，その後 $\alpha = \alpha_0$ に保つとする。

(4) 時刻 $t = 0$ の系の波動関数 $\Psi(x, y; t = 0)$ を相対座標 $y$ に関するフーリエ変換を用いて

$$
\Psi(x, y; t = 0) = \int_{-\infty}^{\infty} \frac{dk}{2\pi} f(x, k) e^{iky}
$$

と表す。$f(x, k)$ を求めよ。

(5) 設問4の結果を用いて，時刻 $t\ (> 0)$ での系の波動関数 $\Psi(x, y; t)$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成29年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
相互作用が粒子間距離の2乗で書かれているため，重心と相対座標を使うとポテンシャルを分けることができます。運動エネルギーも同じ座標で分離できるので，2つの1次元の運動として扱うことができます。

ハミルトニアンを突然変えた直後も，波動関数は変化する前の値を保ちます。変化後の固有状態で展開すると，各成分にエネルギーに応じた時間の位相を掛けて時間発展を調べることができます。
</div>

### (1)
$x = \dfrac{x_1 + x_2}{2},\ y = x_1 - x_2$ より $x_1 = x + \dfrac{y}{2},\ x_2 = x - \dfrac{y}{2}$ です。偏微分の連鎖律を計算します。

$$
\frac{\partial}{\partial x_1} = \frac{1}{2}\frac{\partial}{\partial x} + \frac{\partial}{\partial y},\qquad
\frac{\partial}{\partial x_2} = \frac{1}{2}\frac{\partial}{\partial x} - \frac{\partial}{\partial y}
$$

これより2階微分の和は次のようになります。

$$
\frac{\partial^2}{\partial x_1^2} + \frac{\partial^2}{\partial x_2^2} = \frac{1}{2}\frac{\partial^2}{\partial x^2} + 2\frac{\partial^2}{\partial y^2}
$$

よって運動エネルギー $K$ は $K = -\dfrac{\hbar^2}{4m}\dfrac{\partial^2}{\partial x^2} - \dfrac{\hbar^2}{m}\dfrac{\partial^2}{\partial y^2}$ です。また $x_1^2 + x_2^2 = 2x^2 + \dfrac{1}{2}y^2$ をポテンシャル $V$ に代入します。

$$
\begin{aligned}
V &= \frac{m\omega^2}{2}\left(2x^2 + \frac{1}{2}y^2\right) + \frac{m\omega^2\alpha}{4}y^2 \\
&= m\omega^2 x^2 + \frac{m\omega^2(1 + \alpha)}{4}y^2
\end{aligned}
$$

したがって，

$$
\finalanswer{K = -\frac{\hbar^2}{4m}\frac{\partial^2}{\partial x^2} - \frac{\hbar^2}{m}\frac{\partial^2}{\partial y^2},\qquad V = m\omega^2 x^2 + \frac{m\omega^2(1 + \alpha)}{4}y^2}
$$

### (2)
規格化できる束縛状態を持つには，相対座標 $y$ の2次の係数が正である必要があります。$1+\alpha>0$，すなわち $\alpha>-1$ が条件です。したがって，

$$
\finalanswer{\alpha_0 = -1}
$$

### (3)
重心運動の質量と角振動数を $M=2m$，$\omega_x=\omega$ とします。相対運動の換算質量と角振動数を $\mu=m/2$，$\omega_y=\omega\sqrt{1+\alpha}$ とすると，ハミルトニアンは次の和に分離されます。

$$
H = H_x + H_y,\qquad
H_x = -\frac{\hbar^2}{2M}\frac{\partial^2}{\partial x^2} + \frac{1}{2}M\omega_x^2 x^2,\qquad
H_y = -\frac{\hbar^2}{2\mu}\frac{\partial^2}{\partial y^2} + \frac{1}{2}\mu\omega_y^2 y^2
$$

基底状態のエネルギーは両者の零点エネルギーの和です。

$$
\begin{aligned}
E_0 &= \frac{1}{2}\hbar\omega_x + \frac{1}{2}\hbar\omega_y \\
&= \frac{1}{2}\hbar\omega\left(1 + \sqrt{1 + \alpha}\right)
\end{aligned}
$$

座標変換 $(x_1, x_2) \mapsto (x, y)$ のヤコビアンは

$$
\begin{aligned}
\left|\dfrac{\partial(x_1, x_2)}{\partial(x, y)}\right| &= \left|\begin{matrix} 1 & 1/2 \\ 1 & -1/2 \end{matrix}\right| \\
&= 1
\end{aligned}
$$

なので，$\mathrm{d}x_1\,\mathrm{d}x_2 = \mathrm{d}x\,\mathrm{d}y$ です。1次元調和振動子の基底波動関数のパラメータはそれぞれ質量と角振動数の積を $\hbar$ で割った量なので，

$$
\begin{aligned}
c_x &= \frac{M\omega_x}{\hbar} \\
&= \frac{2m\omega}{\hbar} \\
c_y &= \frac{\mu\omega_y}{\hbar} \\
&= \frac{m\omega\sqrt{1 + \alpha}}{2\hbar}
\end{aligned}
$$

となります。両者の積をとると規格化された基底状態波動関数 $\Psi_0(x, y)$ が得られます。

$$
\begin{aligned}
\Psi_0(x, y)
&= \left(\frac{c_x}{\pi}\right)^{\frac{1}{4}}\left(\frac{c_y}{\pi}\right)^{\frac{1}{4}}\exp\left(-\frac{c_x}{2}x^2 - \frac{c_y}{2}y^2\right) \\
&= \left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{2}}(1 + \alpha)^{\frac{1}{8}}\exp\left(-\frac{m\omega}{\hbar}x^2 - \frac{m\omega\sqrt{1 + \alpha}}{4\hbar}y^2\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{E_0 = \frac{1}{2}\hbar\omega\left(1 + \sqrt{1 + \alpha}\right),\qquad \Psi_0(x, y) = \left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{2}}(1 + \alpha)^{\frac{1}{8}}\exp\left(-\frac{m\omega}{\hbar}x^2 - \frac{m\omega\sqrt{1 + \alpha}}{4\hbar}y^2\right)}
$$

### (4)
$t = 0$ の波動関数は問3で $\alpha = 0$ とおいたものです。

$$
\Psi(x, y; t = 0) = \left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{2}}\exp\left(-\frac{m\omega}{\hbar}x^2 - \frac{m\omega}{4\hbar}y^2\right)
$$

フーリエ変換の反転公式より $f(x, k) = \displaystyle\int_{-\infty}^{\infty} \Psi(x, y; t = 0) e^{-iky}\,\mathrm{d}y$ を平方完成とガウス積分公式を用いて計算します。

$$
\begin{aligned}
f(x, k)
&= \left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{2}} e^{-\frac{m\omega}{\hbar}x^2} \int_{-\infty}^{\infty} \exp\left[-\frac{m\omega}{4\hbar}\left(y + \frac{2i\hbar k}{m\omega}\right)^2 - \frac{\hbar k^2}{m\omega}\right]\mathrm{d}y \\
&= \left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{2}} \sqrt{\frac{4\pi\hbar}{m\omega}}\,\exp\left(-\frac{m\omega}{\hbar}x^2 - \frac{\hbar k^2}{m\omega}\right) \\
&= 2\exp\left(-\frac{m\omega}{\hbar}x^2 - \frac{\hbar k^2}{m\omega}\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{f(x, k) = 2\exp\left(-\frac{m\omega}{\hbar}x^2 - \frac{\hbar k^2}{m\omega}\right)}
$$

### (5)
$t > 0$ では $\alpha = \alpha_0 = -1$ なので，ハミルトニアンは

$$
H = H_x + H_y^{\mathrm{free}},\qquad H_x = -\frac{\hbar^2}{4m}\frac{\partial^2}{\partial x^2} + m\omega^2 x^2,\qquad H_y^{\mathrm{free}} = -\frac{\hbar^2}{m}\frac{\partial^2}{\partial y^2}
$$

となります。重心部分は $H_x$ の基底状態で，固有値は $\hbar\omega/2$ です。相対運動の平面波 $e^{iky}$ の固有値は $\hbar^2k^2/m$ なので，各フーリエ成分に次の時間発展因子が掛かります。

$$
\exp\left[-\frac{i}{\hbar}\left(\frac{\hbar\omega}{2}+\frac{\hbar^2k^2}{m}\right)t\right]
$$

$$
\begin{aligned}
\Psi(x, y; t)
&= e^{-\frac{i}{2}\omega t}\int_{-\infty}^{\infty} \frac{\mathrm{d}k}{2\pi}\,f(x, k)\exp\left(iky - i\frac{\hbar k^2}{m}t\right) \\
&= \frac{1}{\pi}e^{-\frac{i}{2}\omega t}e^{-\frac{m\omega}{\hbar}x^2}\int_{-\infty}^{\infty}\exp\left[-\frac{\hbar(1 + i\omega t)}{m\omega}k^2 + iky\right]\mathrm{d}k
\end{aligned}
$$

ガウス積分公式を複素数 $c = \dfrac{\hbar(1 + i\omega t)}{m\omega}$（$\operatorname{Re} c > 0$）へ解析接続して積分します。

$$
\begin{aligned}
\int_{-\infty}^{\infty}\exp\left(-c k^2 + iky\right)\mathrm{d}k
&= \sqrt{\frac{\pi}{c}}\exp\left(-\frac{y^2}{4c}\right) \\
&= \sqrt{\frac{\pi m\omega}{\hbar(1 + i\omega t)}}\exp\left(-\frac{m\omega}{4\hbar(1 + i\omega t)}y^2\right)
\end{aligned}
$$

これを代入して整理します。したがって，

$$
\finalanswer{\Psi(x, y; t) = \left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{2}}\frac{e^{-\frac{i}{2}\omega t}}{\sqrt{1 + i\omega t}}\exp\left(-\frac{m\omega}{\hbar}x^2 - \frac{m\omega}{4\hbar(1 + i\omega t)}y^2\right)}
$$

$\sqrt{1+i\omega t}$ は実部が正の主値分枝を使います。

<aside class="rigor-note" markdown>
相対座標の確率密度は，

$$
|\psi_y(y;t)|^2\propto\frac{1}{\sqrt{1+\omega^2t^2}}\exp\left[-\frac{m\omega y^2}{2\hbar(1+\omega^2t^2)}\right]
$$

です。したがって，標準偏差は $\Delta y(t)=\sqrt{\dfrac{\hbar}{m\omega}(1+\omega^2t^2)}$ となります。これは，相対座標の閉じ込めがなくなった後の自由波束の広がりを表します。
</aside>
