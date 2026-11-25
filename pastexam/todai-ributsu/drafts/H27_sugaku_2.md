---
title: 東大理物 平成27年度 数学 第2問：拡散方程式の遅延グリーン関数と複素積分
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 複素解析
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成27年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化しています。
---

# 東大理物 平成27年度 数学 第2問：拡散方程式の遅延グリーン関数と複素積分

## 問題

実数 $t$ および $x$ の複素関数 $f(t, x)$ が

$$
\frac{\partial f(t, x)}{\partial t} = \lambda\frac{\partial^2 f(t, x)}{\partial x^2} + S(t, x) \tag{1}
$$

という微分方程式を満たすとする。ただし $\lambda$ は正の実定数，$S(t, x)$ は与えられた関数である。$f(t, x)$ は $x$ に関してフーリエ変換可能な関数であるとして，以下の設問に答えよ。

(1) $S(t, x) = 0$ のとき，方程式 (1) の一般解は

$$
f(t, x) = \int_{-\infty}^{\infty} \frac{dk}{2\pi}\tilde{f}(k)\exp\left(-\lambda k^2 t - ikx\right) \tag{2}
$$

という形に表されることを示せ。ただし，$\tilde{f}(k)$ は $k$ の関数である。

(2) 関数 $G(t, x, t', x')$ が

$$
\frac{\partial G(t, x, t', x')}{\partial t} = \lambda\frac{\partial^2 G(t, x, t', x')}{\partial x^2} + \delta(t - t')\delta(x - x') \tag{3}
$$

という方程式を満たすとする。ただし，$\delta(x)$ はデルタ関数である。このとき

$$
f(t, x) = \int_{-\infty}^{\infty} dt' \int_{-\infty}^{\infty} dx'\, G(t, x, t', x') S(t', x') \tag{4}
$$

という関数が方程式 (1) の解となることを示せ。

(3) 複素定数 $C$ と $\alpha$ を適切に選べば

$$
G(t, x, t', x') = C\int_{-\infty}^{\infty} \frac{d\omega}{2\pi}\int_{-\infty}^{\infty} \frac{dk}{2\pi}\frac{e^{i\omega(t - t') - ik(x - x')}}{\omega - i\alpha\lambda k^2} \tag{5}
$$

という関数は方程式 (3) を満たすことを示せ。また，そのような $C$ と $\alpha$ を求めよ。

(4) 式 (5) において，まず $\omega$ についての積分を，$t < t'$ および $t > t'$ それぞれの場合について行え。ただし，設問3で得られた $C$ と $\alpha$ の値を用いること。

(5) さらに式 (5) の $k$ についての積分を行い，$t < t'$ および $t > t'$ それぞれの場合について，$G(t, x, t', x')$ の具体的な関数形を求めよ。ただし，必要であれば

$$
\int_{-\infty}^{\infty} dx\, e^{-x^2} = \sqrt{\pi} \tag{6}
$$

という公式を用いよ。

(6) 関数 $S(t, x)$ が

$$
S(t, x) = \delta(t)\cos(px) \tag{7}
$$

という形に与えられているとする。ただし，$p$ は実定数である。このとき $t < 0$ で $f(t, x) = 0$ となるような $f(t, x)$ を求めよ。また，得られた関数 $f(t, x)$ について，$t$ をある正の値に固定した場合の最大値と，その最大値を与える $x$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成27年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
拡散方程式は時間と位置について係数が定数なので，フーリエ変換すると，微分は $i\omega$ や $ik$ を掛ける操作になります。そのため，点状の源に対する解 $G$ のフーリエ変換は，代数方程式から求まります。

$G$ を時間に戻す $\omega$ の積分では，$t<t'$ のときと $t>t'$ のときで，経路を閉じる半平面が異なります。被積分関数の極は上半平面にだけあるので，片方の場合は積分が $0$ になり，源より前の時刻には応答がないことがわかります。
</div>

### (1)
$f(t, x)$ の $x$ に関するフーリエ変換を $\hat{f}(t, k)$ とし，逆変換を

$$
f(t, x) = \int_{-\infty}^{\infty} \frac{\mathrm{d}k}{2\pi}\,\hat{f}(t, k) e^{-ikx}
$$

と表します。これを $S(t, x) = 0$ の式 (1) に代入します。

$$
\int_{-\infty}^{\infty} \frac{\mathrm{d}k}{2\pi}\left(\frac{\partial\hat{f}(t, k)}{\partial t} + \lambda k^2\hat{f}(t, k)\right)e^{-ikx} = 0
$$

フーリエ変換の一意性より，各 $k$ に対して

$$
\frac{\partial\hat{f}(t, k)}{\partial t} = -\lambda k^2\hat{f}(t, k)
$$

が成り立ちます。$t$ について解くと $\hat{f}(t,k)=\tilde{f}(k)e^{-\lambda k^2t}$ となります。ここで $\tilde{f}(k)=\hat{f}(0,k)$ です。逆変換の式に代入すると式 (2) が得られます。

### (2)
式 (4) の両辺に演算子 $\dfrac{\partial}{\partial t} - \lambda\dfrac{\partial^2}{\partial x^2}$ を作用させ，積分記号下で微分して式 (3) を代入します。

$$
\begin{aligned}
\left(\frac{\partial}{\partial t} - \lambda\frac{\partial^2}{\partial x^2}\right)f(t, x)
&= \int_{-\infty}^{\infty}\mathrm{d}t'\int_{-\infty}^{\infty}\mathrm{d}x'\left[\left(\frac{\partial}{\partial t} - \lambda\frac{\partial^2}{\partial x^2}\right)G(t, x, t', x')\right]S(t', x') \\
&= \int_{-\infty}^{\infty}\mathrm{d}t'\int_{-\infty}^{\infty}\mathrm{d}x'\,\delta(t - t')\delta(x - x')S(t', x') \\
&= S(t, x)
\end{aligned}
$$

よって式 (4) の $f(t, x)$ は方程式 (1) の解です。

### (3)
式 (5) に演算子 $\dfrac{\partial}{\partial t} - \lambda\dfrac{\partial^2}{\partial x^2}$ を作用させます。

$$
\begin{aligned}
\left(\frac{\partial}{\partial t} - \lambda\frac{\partial^2}{\partial x^2}\right)G(t, x, t', x')
&= C\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{2\pi}\int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi}\,\frac{i\omega + \lambda k^2}{\omega - i\alpha\lambda k^2} e^{i\omega(t - t') - ik(x - x')} \\
&= iC\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{2\pi}\int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi}\,\frac{\omega - i\lambda k^2}{\omega - i\alpha\lambda k^2} e^{i\omega(t - t') - ik(x - x')}
\end{aligned}
$$

$\alpha = 1$ と選ぶと分子と分母が約分されて $1$ となり，さらに $iC = 1$ すなわち $C = -i$ と選ぶと，デルタ関数のフーリエ積分表示より

$$
\begin{aligned}
\left(\frac{\partial}{\partial t} - \lambda\frac{\partial^2}{\partial x^2}\right)G(t, x, t', x') &= \left(\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{2\pi} e^{i\omega(t - t')}\right)\left(\int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi} e^{-ik(x - x')}\right) \\
&= \delta(t - t')\delta(x - x')
\end{aligned}
$$

となって式 (3) を満たします。したがって，

$$
\finalanswer{C = -i,\qquad \alpha = 1}
$$

### (4)
問3の結果より，$\omega$ に関する積分は

$$
I_\omega(t - t', k) = -i\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{2\pi}\frac{e^{i\omega(t - t')}}{\omega - i\lambda k^2}
$$

です。被積分関数の極は $\omega = i\lambda k^2$ であり，$k \neq 0$ かつ $\lambda > 0$ より複素 $\omega$ 平面の上半平面 $\operatorname{Im}\omega > 0$ にあります。 $k=0$ は $k\to0$ の極限で扱い，実軸上の極には $\omega-i0^+$ の処方を用います。

$t < t'$ のときを考えます。下半平面の大きな半円弧の上では，$\left|e^{i\omega(t - t')}\right| = e^{-\operatorname{Im}\omega(t - t')} \to 0$ となります。そのため，閉経路は下半平面にとります。閉経路の中に極はないので，コーシーの積分定理より $I_\omega = 0$ です。

$t > t'$ のときは，上半平面の大きな半円弧の上で $\left|e^{i\omega(t - t')}\right| \to 0$ となります。そのため，閉経路は上半平面に反時計回りにとります。極 $\omega = i\lambda k^2$ が閉経路の中にあるので，留数定理を用います。

$$
\begin{aligned}
I_\omega(t - t', k) &= (-i)\cdot\frac{2\pi i}{2\pi}\,e^{i(i\lambda k^2)(t - t')} \\
&= e^{-\lambda k^2(t - t')}
\end{aligned}
$$

したがって，$\omega$ についての積分結果は

$$
\finalanswer{-i\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{2\pi}\frac{e^{i\omega(t - t')}}{\omega - i\lambda k^2} = \begin{cases} 0 & (t < t') \\ e^{-\lambda k^2(t - t')} & (t > t') \end{cases}}
$$

### (5)
$t < t'$ のときは，問4より $G(t, x, t', x') = 0$ です。

$t > t'$ のときは，問4の結果を $k$ で積分し，平方完成と式 (6) のガウス積分の公式を用います。平方完成後の積分路は複素平面内で実軸と平行な直線になりますが，被積分関数が整関数で，両端の接続部分の積分が $0$ に収束するため，実軸へ移して同じ公式を使うことができます。

$$
\begin{aligned}
G(t, x, t', x')
&= \int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi}\exp\bigl[-\lambda(t - t')k^2 - ik(x - x')\bigr] \\
&= \frac{1}{2\pi}\exp\left[-\frac{(x - x')^2}{4\lambda(t - t')}\right]\int_{-\infty}^{\infty}\exp\left[-\lambda(t - t')\left(k + \frac{i(x - x')}{2\lambda(t - t')}\right)^2\right]\mathrm{d}k \\
&= \frac{1}{2\pi}\sqrt{\frac{\pi}{\lambda(t - t')}}\exp\left[-\frac{(x - x')^2}{4\lambda(t - t')}\right] \\
&= \frac{1}{\sqrt{4\pi\lambda(t - t')}}\exp\left[-\frac{(x - x')^2}{4\lambda(t - t')}\right]
\end{aligned}
$$

したがって，

$$
\finalanswer{G(t, x, t', x') = \begin{cases} 0 & (t < t') \\ \dfrac{1}{\sqrt{4\pi\lambda(t - t')}}\exp\left[-\dfrac{(x - x')^2}{4\lambda(t - t')}\right] & (t > t') \end{cases}}
$$

### (6)
式 (7) の $S(t', x') = \delta(t')\cos(px')$ を式 (4) に代入します。問5の $G$ は $t < t'$ で $0$ なので，$t < 0$ では $f(t, x) = 0$ となり初期条件を満たします。

$t > 0$ のときは $t'$ 積分により $t' = 0$ が選ばれ，$\cos(px') = \operatorname{Re}\bigl(e^{ipx'}\bigr)$ と $u = x' - x$ の置換およびガウス積分を用いて次のように計算されます。

$$
\begin{aligned}
f(t, x) &= \int_{-\infty}^{\infty} G(t, x, 0, x')\cos(px')\,\mathrm{d}x' \\
&= \operatorname{Re}\left[\frac{1}{\sqrt{4\pi\lambda t}}\int_{-\infty}^{\infty}\exp\left(-\frac{(x' - x)^2}{4\lambda t} + ipx'\right)\mathrm{d}x'\right] \\
&= \operatorname{Re}\left[\frac{e^{ipx}}{\sqrt{4\pi\lambda t}}\int_{-\infty}^{\infty}\exp\left(-\frac{u^2}{4\lambda t} + ipu\right)\mathrm{d}u\right] \\
 &= \operatorname{Re}\left[e^{ipx}\,e^{-\lambda p^2 t}\right] \\
&= e^{-\lambda p^2 t}\cos(px)
\end{aligned}
$$



$t>0$ を固定すると $\cos(px)\le1$ なので，最大値は $e^{-\lambda p^2t}$ です。$p\neq0$ では $x=2n\pi/p$ で最大値をとり，$p=0$ では任意の実数 $x$ で最大値 $1$ をとります。したがって，

$$
\finalanswer{f(t,x)=\begin{cases}0&(t<0)\\e^{-\lambda p^2t}\cos(px)&(t>0)\end{cases}}
$$

です。また，最大値と最大値を与える位置を $f_{\max}(t),x_{\max}$ と書くと，

$$
\finalanswer{f_{\max}(t)=e^{-\lambda p^2t}}
$$

および

$$
\finalanswer{x_{\max}=\frac{2n\pi}{p}\quad(n\in\mathbb{Z},\ p\neq0),\qquad x_{\max}\in\mathbb{R}\quad(p=0)}
$$

となります。

<aside class="rigor-note" markdown>
$p\neq0$ のフーリエモード $\cos(px)$ は，空間パターンを保ちながら緩和時間 $\tau_p=(\lambda p^2)^{-1}$ で指数減衰します。$p=0$ の一定成分は減衰しません。波数の絶対値が大きい短波長の成分ほど速く減衰するため，拡散によって分布が滑らかになります。
</aside>
