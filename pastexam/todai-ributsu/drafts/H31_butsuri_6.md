---
title: 東大理物 平成31年度 物理学 第6問：同軸ケーブルの電信方程式・特性インピーダンスと表皮効果
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成31年度
exam_subject: 物理学
exam_number: 第6問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成31年度 物理学 第6問：同軸ケーブルの電信方程式・特性インピーダンスと表皮効果

## 問題

テレビ用のアンテナケーブルなど，高周波電気信号を高速で伝送するのに同軸ケーブルがよく用いられる。図 1 に示すように，同軸ケーブルは円柱形の内部導体を円筒形の絶縁体と外部導体で覆った構造をしている。中心軸方向を $x$ 軸にとり，単位長さあたりの電気容量を $C$，自己インダクタンスを $L$ とおく。内部導体を流れる電流 $I$（外部導体を流れる電流と逆向き）と両導体間の電圧 $V$ は $x$ と時刻 $t$ の関数であり，両者の間には

$$
\frac{\partial I}{\partial x} = -C\frac{\partial V}{\partial t}, \tag{1}
$$

$$
\frac{\partial V}{\partial x} = -L\frac{\partial I}{\partial t} \tag{2}
$$

の関係がある。以下の設問に答えよ。必要に応じて，真空中の光速 $c = 3.0 \times 10^8\ \mathrm{m/s}$，真空の透磁率 $\mu_0 = 4\pi \times 10^{-7}\ \mathrm{H/m}$ を用いよ。以下，概算する場合は有効数字 1 桁でよいが，答えには単位を明記すること。

<figure class="problem-figure" markdown>
![同軸ケーブルの構造模式図](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p1-light.svg#only-light)
![同軸ケーブルの構造模式図](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p1-dark.svg#only-dark)
<figcaption markdown="span">図 1：同軸ケーブルの構造（左から順に半径 $a$ の内部導体，絶縁体，内半径 $b$ の外部導体，保護被覆）。</figcaption>
</figure>

<figure class="problem-figure" markdown>
![特性インピーダンスZ_0で終端した同軸ケーブル](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p2-light.svg#only-light)
![特性インピーダンスZ_0で終端した同軸ケーブル](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p2-dark.svg#only-dark)
<figcaption markdown="span">図 2：信号発生器（SG）と特性インピーダンス $Z_0$ の終端抵抗をつないだ同軸ケーブル。</figcaption>
</figure>

(1) 式 (1) と (2) より $I$ または $V$ に関する波動方程式を導き，同軸ケーブルでの電気信号の伝送速度 $v$ を，$C$ と $L$ を用いて表せ。

(2) $C$ と $L$ は，内部導体の半径を $a$，外部導体の内半径を $b$，絶縁体の誘電率を $\varepsilon$ とし，また絶縁体の透磁率が真空の透磁率 $\mu_0$ と等しいとして，

$$
C = \frac{2\pi\varepsilon}{\log\left(\dfrac{b}{a}\right)}, \qquad L = \frac{\mu_0 \log\left(\dfrac{b}{a}\right)}{2\pi} \tag{3}
$$

で与えられる。$\log(b/a) = 1.8$，絶縁体の比誘電率が $2.2$ の同軸ケーブルを伝播する周波数 $f = 500\ \mathrm{MHz}$ の正弦波に対して，波長 $\lambda$ を概算せよ。

(3) $x$ 軸正方向に伝送される電圧と電流の波において，両者の間には比例関係 $V = Z_0 I$ が成り立つ。ここで，$Z_0$ は特性インピーダンスと呼ばれるケーブルの構造によって決定される実定数である。同軸ケーブルの終端での反射を防ぐためには，図 2 のように，抵抗値が $Z_0$ と等しい抵抗器を接続する必要がある。まず，$Z_0$ を，$C$ と $L$ を用いて表せ。そののち，設問 2 の同軸ケーブルに対して $Z_0$ を概算せよ。

(4) 次に，終端に $Z_0$ と異なる抵抗値 $r$ をもつ抵抗器をつなげたときの反射を考える。図 3 のように，電圧の高さが $V_1$ のパルス波を入力した場合に対して，反射により生じるパルス波の電圧の高さ $V_2$ を，$r$，$Z_0$，$V_1$ を用いて表せ。

<figure class="problem-figure" markdown>
![抵抗rで終端した同軸ケーブルにおけるパルス波の反射](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p3-light.svg#only-light)
![抵抗rで終端した同軸ケーブルにおけるパルス波の反射](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p3-dark.svg#only-dark)
<figcaption markdown="span">図 3：終端抵抗 $r$ による入力パルス $V_1$ の反射パルス $V_2$。</figcaption>
</figure>

(5) 内部導体の電気抵抗を考慮した場合，式 (2) は

$$
\frac{\partial V}{\partial x} = -L\frac{\partial I}{\partial t} - RI \tag{4}
$$

に置き換えられる。ここで，$R$ は内部導体の軸方向の単位長さ当たりの電気抵抗であり，信号の減衰を引き起こす。図 4 のように，長さ $d$ の同軸ケーブルの左端において振幅 $V_1$，角周波数 $\omega$ の正弦波の交流電圧（複素表示で $V = V_1 e^{-i\omega t}$）を与えたとき，右端での交流電圧の振幅 $V_2$ を答えよ。ただし，$L\omega$ は $R$ に比べて十分に大きいものとして近似計算を行ってよい。また，反射を防ぐために右端には抵抗値 $Z_0$ の抵抗器がつながれている。

<figure class="problem-figure" markdown>
![長さdの同軸ケーブルにおける交流信号の減衰](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p4-light.svg#only-light)
![長さdの同軸ケーブルにおける交流信号の減衰](../../../docs/assets/figures/pastexam-todai-ributsu/H31_butsuri_6-p4-dark.svg#only-dark)
<figcaption markdown="span">図 4：長さ $d$ の同軸ケーブルの左端に交流電圧 $V_1$ を与え，右端の終端抵抗 $Z_0$ の両端電圧 $V_2$ を測る系。</figcaption>
</figure>

(6) 高周波では，電流は導体の表面近傍の狭い領域に集中して流れる。この現象は表皮効果と呼ばれ，実効的な導体の断面積の減少により設問 5 で論じた信号の減衰を顕著にする。さて，簡単な例として，半径 $a$ の円柱導体の軸方向に角周波数 $\omega$ の正弦波の交流電流が流れている場合を考えよう。電流密度は軸方向成分のみをもち，中心軸からの距離 $r$（$r \le a$）の関数として，複素表示で $j(r, t) = J(r) e^{-i\omega t}$ と表される。ここで，$j(r, t)$ の位相は $r$ に依存するので，$J(r)$ は一般に複素数となる。電流とそれにより作られる円周方向の磁束密度 $B(r, t)$ との関係，磁束密度の時間変動と軸方向に生じる誘導電場 $E(r, t)$ との関係，および電流密度と電場との比例関係 $j(r, t) = \sigma E(r, t)$（$\sigma$ は導体の電気伝導率）より，$J(r)$ に関する微分方程式が得られる。表面近傍（$r \approx a$）における電流密度の振幅が，$|J(r)| \approx |J(a)|\exp[(r - a)/\delta]$ と近似できるものとして，表皮深さ（skin depth）と呼ばれる長さ $\delta$（$\ll a$）を $\omega$，$\sigma$，導体中の透磁率 $\mu$ を用いて表せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成31年度修士課程入学試験 物理学 第6問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
無損失の同軸ケーブルでは電信方程式から $I$・$V$ を直接消去するだけで 1 次元波動方程式が得られ，幾何因子 $\log(b/a)$ が積 $LC$ で打ち消し合うため伝送速度は絶縁体中の光速 $c/\sqrt{\varepsilon_{\mathrm{r}}}$ に一致します。一方，比 $\sqrt{L/C}$ である特性インピーダンス $Z_0$ は幾何形状と真空の波動インピーダンス $\mu_0 c$ から定まります。

後半では，導体の有限抵抗 $R$ を入れた電信方程式の複素波数から減衰定数 $R/(2Z_0)$ を導き，さらに円柱導体内のアンペール・ファラデーの法則から高周波電流が表面近傍の表皮深さ $\delta = \sqrt{2/(\omega\mu\sigma)}$ に局在する仕組みを導きます。
</div>

### (1)
式 (2) の両辺を $x$ で偏微分し，式 (1) の両辺を $t$ で偏微分した結果を代入します。

$$
\begin{aligned}
\frac{\partial^2 V}{\partial x^2} &= -L\frac{\partial^2 I}{\partial x \partial t} \\
&= -L\frac{\partial}{\partial t}\left(-C\frac{\partial V}{\partial t}\right) = LC\frac{\partial^2 V}{\partial t^2}
\end{aligned}
$$

同様に，式 (1) を $x$ で偏微分して式 (2) を用いると，$I$ についても同じ形の波動方程式 $\dfrac{\partial^2 I}{\partial x^2} = LC\dfrac{\partial^2 I}{\partial t^2}$ が得られます。1 次元波動方程式 $\dfrac{\partial^2 V}{\partial x^2} = \dfrac{1}{v^2}\dfrac{\partial^2 V}{\partial t^2}$ と比較すると，伝送速度 $v$ は次のとおりです。

$$
\finalanswer{\frac{\partial^2 V}{\partial x^2} = LC\frac{\partial^2 V}{\partial t^2},\qquad v = \frac{1}{\sqrt{LC}}}
$$

### (2)
式 (3) より $LC$ の積を計算すると，$\log(b/a)$ と $2\pi$ が打ち消し合います。絶縁体の比誘電率を $\varepsilon_{\mathrm{r}} = \varepsilon / \varepsilon_0$（$\varepsilon_0 \mu_0 = 1/c^2$）とすると，

$$
LC = \mu_0 \varepsilon = \mu_0 \varepsilon_0 \varepsilon_{\mathrm{r}} = \frac{\varepsilon_{\mathrm{r}}}{c^2} \implies v = \frac{1}{\sqrt{LC}} = \frac{c}{\sqrt{\varepsilon_{\mathrm{r}}}}
$$

となります。$\varepsilon_{\mathrm{r}} = 2.2$，$f = 500\ \mathrm{MHz} = 5.0 \times 10^8\ \mathrm{Hz}$，$c = 3.0 \times 10^8\ \mathrm{m/s}$ を代入して波長 $\lambda = v / f$ を求めます。

$$
\lambda = \frac{v}{f} = \frac{c}{f\sqrt{\varepsilon_{\mathrm{r}}}} = \frac{3.0 \times 10^8}{5.0 \times 10^8 \times \sqrt{2.2}} \approx \frac{0.6}{1.48} \approx 0.40\ \mathrm{m}
$$

有効数字 1 桁で概算すると，

$$
\finalanswer{\lambda \approx 0.4\ \mathrm{m}}
$$

### (3)
$x$ 軸正方向に速度 $v = 1/\sqrt{LC}$ で伝送される波は，$V(x, t) = f(x - vt)$，$I(x, t) = g(x - vt)$ と表されます（$f, g$ は任意の関数）。これを式 (2) に代入すると，

$$
f'(x - vt) = -L(-v)g'(x - vt) = L v g'(x - vt) = \sqrt{\frac{L}{C}}\,g'(x - vt)
$$

となります。両辺を積分して定常成分を $0$ とすると $V = \sqrt{\dfrac{L}{C}}\,I$ となるため，特性インピーダンス $Z_0$ は

$$
Z_0 = \sqrt{\frac{L}{C}}
$$

です。式 (3) と $\varepsilon = \varepsilon_{\mathrm{r}}\varepsilon_0$，$\sqrt{\mu_0 / \varepsilon_0} = \mu_0 c$ を用いて数値を概算します。

$$
\begin{aligned}
Z_0 &= \sqrt{\frac{L}{C}} = \frac{\log(b/a)}{2\pi}\sqrt{\frac{\mu_0}{\varepsilon}} = \frac{\log(b/a)}{2\pi}\frac{\mu_0 c}{\sqrt{\varepsilon_{\mathrm{r}}}} \\
&= \frac{1.8}{2\pi}\cdot\frac{4\pi \times 10^{-7} \times 3.0 \times 10^8}{\sqrt{2.2}}
= \frac{108}{\sqrt{2.2}} \approx 73\ \Omega
\end{aligned}
$$

有効数字 1 桁で概算すると $Z_0 \approx 7 \times 10\ \Omega$（$70\ \Omega$）です。

$$
\finalanswer{Z_0 = \sqrt{\frac{L}{C}}, \qquad Z_0 \approx 7 \times 10\ \Omega\ (70\ \Omega)}
$$

### (4)
$x$ 軸負方向に進む反射波 $V_-(x, t) = h(x + vt)$，$I_-(x, t) = k(x + vt)$ を式 (2) に代入すると，$h'(x + vt) = -Lv k'(x + vt)$ より $V_- = -Z_0 I_-$ となります。

したがって，終端抵抗 $r$ の位置における全電圧 $V$ と全電流 $I$ は，入力パルス $V_1$ と反射パルス $V_2$ の重ね合わせにより

$$
V = V_1 + V_2, \qquad I = \frac{V_1}{Z_0} - \frac{V_2}{Z_0}
$$

となります。終端の抵抗器 $r$ でのオームの法則 $V = rI$ にこれらを代入して $V_2$ を解きます。

$$
\begin{aligned}
V_1 + V_2 &= \frac{r}{Z_0}(V_1 - V_2) \\
\left(1 + \frac{r}{Z_0}\right)V_2 &= \left(\frac{r}{Z_0} - 1\right)V_1 \\
V_2 &= \frac{r - Z_0}{r + Z_0}V_1
\end{aligned}
$$

したがって，

$$
\finalanswer{V_2 = \frac{r - Z_0}{r + Z_0}V_1}
$$

### (5)
右端は抵抗値 $Z_0$ で終端されているため反射はなく，$x$ 軸正方向へ進む波 $V(x, t) = V_1 e^{i(kx - \omega t)}$，$I(x, t) = I_1 e^{i(kx - \omega t)}$ のみを考えます。式 (1) と式 (4) に代入すると，

$$
\begin{aligned}
ik I_1 &= i\omega C V_1 \implies I_1 = \frac{\omega C}{k}V_1, \\
ik V_1 &= (i\omega L - R)I_1
\end{aligned}
$$

となります。$I_1$ を消去して $k^2$ を求めます。

$$
\begin{aligned}
-k^2 &= i\omega C(i\omega L - R) = -\omega^2 LC - i\omega CR \\
k^2 &= \omega^2 LC\left(1 + i\frac{R}{\omega L}\right)
\end{aligned}
$$

条件 $L\omega \gg R$ すなわち $\dfrac{R}{\omega L} \ll 1$ のもとで平方根を 1 次まで展開し，$+x$ 方向に伝搬・減衰する解（$\operatorname{Re} k > 0$，$\operatorname{Im} k > 0$）を選びます。

$$
k = \omega\sqrt{LC}\sqrt{1 + i\frac{R}{\omega L}} \simeq \omega\sqrt{LC}\left(1 + i\frac{R}{2\omega L}\right) = \omega\sqrt{LC} + i\frac{R}{2}\sqrt{\frac{C}{L}}
$$

よって $V(x, t) = V_1 \exp\!\left(-\dfrac{R}{2}\sqrt{\dfrac{C}{L}}\,x\right)\exp\!\left[i\left(\omega\sqrt{LC}\,x - \omega t\right)\right]$ となり，右端 $x = d$ での交流電圧の振幅 $V_2$ は次のとおりです（$Z_0 = \sqrt{L/C}$ を用いて $V_1 \exp\!\left(-\dfrac{Rd}{2Z_0}\right)$ とも表されます）。

$$
\finalanswer{V_2 = V_1\exp\!\left(-\frac{R}{2}\sqrt{\frac{C}{L}}\,d\right) = V_1\exp\!\left(-\frac{Rd}{2Z_0}\right)}
$$

### (6)
円柱座標 $(r, \phi, z)$ で軸方向を $z$ 軸にとります。軸対称性より磁束密度は円周方向成分 $B(r, t)$ のみをもち，電場は軸方向成分 $E(r, t)$ のみをもちます。導体内では変位電流を無視し，アンペールの法則とファラデーの電磁誘導の法則を書き下します。

- アンペールの法則：半径 $r$ の円周上の線積分より $2\pi r B(r, t) = \mu \int_0^r 2\pi r' j(r', t)\,\mathrm{d}r'$，両辺を $r$ で微分すると
  $$
  \frac{1}{r}\frac{\partial}{\partial r}\bigl(r B(r, t)\bigr) = \mu j(r, t)
  $$
- ファラデーの法則：軸に平行な辺と半径方向の辺からなる微小長方形の閉路より
  $$
  \frac{\partial E(r, t)}{\partial r} = \frac{\partial B(r, t)}{\partial t}
  $$
  （$\nabla \times \boldsymbol{E} = -\dfrac{\partial \boldsymbol{B}}{\partial t}$ の $\phi$ 成分 $-\dfrac{\partial E_z}{\partial r} = -\dfrac{\partial B_\phi}{\partial t}$ に一致します。）

これらに $j(r, t) = \sigma E(r, t) = J(r) e^{-i\omega t}$ と $B(r, t) = \tilde{B}(r) e^{-i\omega t}$ を代入します。ファラデーの法則より

$$
\frac{1}{\sigma}\frac{\mathrm{d}J}{\mathrm{d}r} = -i\omega \tilde{B} \implies \tilde{B} = \frac{i}{\omega\sigma}\frac{\mathrm{d}J}{\mathrm{d}r}
$$

となり，これをアンペールの法則に代入すると $J(r)$ に関する微分方程式が得られます。

$$
\begin{aligned}
\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{i}{\omega\sigma}\frac{\mathrm{d}J}{\mathrm{d}r}\right) &= \mu J \\
\frac{\mathrm{d}^2 J}{\mathrm{d}r^2} + \frac{1}{r}\frac{\mathrm{d}J}{\mathrm{d}r} &= -i\omega\mu\sigma J
\end{aligned}
$$

表面近傍（$r \approx a$）では $J(r)$ が長さ $\delta \ll a$ のスケールで急激に変化するため，$\left|\dfrac{1}{r}\dfrac{\mathrm{d}J}{\mathrm{d}r}\right| \sim \dfrac{|J|}{a\delta} \ll \dfrac{|J|}{\delta^2} \sim \left|\dfrac{\mathrm{d}^2 J}{\mathrm{d}r^2}\right|$ となって 1 階微分の項を無視することができます。

$$
\frac{\mathrm{d}^2 J}{\mathrm{d}r^2} \simeq -i\omega\mu\sigma J
$$

$J(r) = J(a) e^{\kappa(r - a)}$ を代入すると $\kappa^2 = -i\omega\mu\sigma = \omega\mu\sigma e^{-i\pi/2}$ となります。導体内部（$r < a$）へ向かって減衰するためには $\operatorname{Re}\kappa > 0$ を選ぶ必要があり，

$$
\kappa = (1 - i)\sqrt{\frac{\omega\mu\sigma}{2}}
$$

が得られます。したがって $|J(r)| = |J(a)|\exp\!\left[\sqrt{\dfrac{\omega\mu\sigma}{2}}\,(r - a)\right]$ となり，表皮深さ $\delta$ は次のとおりです。

$$
\finalanswer{\delta = \sqrt{\frac{2}{\omega\mu\sigma}}}
$$

<aside class="rigor-note" markdown>
設問 3 で概算した特性インピーダンス $Z_0 \approx 73\ \Omega$ は，実際のテレビ用同軸ケーブルの標準規格である $75\ \Omega$ にほぼ一致しています。また設問 6 の円柱導体の厳密解は $J(r) \propto I_0\bigl(\sqrt{-i\omega\mu\sigma}\,r\bigr)$（第 1 種変形ベッセル関数）で与えられ，$\delta \ll a$ の漸近形が表面からの指数減衰 $\exp[(r - a)/\delta]$ に一致します。
</aside>
