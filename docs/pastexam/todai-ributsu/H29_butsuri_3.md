---
title: 東大理物 平成29年度 物理学 第3問：二重振り子の基準振動と断熱的パラメータ変化
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成29年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成29年度 物理学 第3問：二重振り子の基準振動と断熱的パラメータ変化

## 問題

図1のような $xy$ 平面内を運動する二重振り子を考える。ここで，鉛直下向きを $y$ 軸の正の向きとする。原点 $O$ と質点1，質点1と質点2は，長さがそれぞれ $\ell_1,\ \ell_2$ の質量が無視できる糸でつながれている。質点1，質点2の質量はそれぞれ $m_1,\ m_2$ とする。空気抵抗や摩擦，糸のたわみは無視できるとする。また，任意の変数 $q$ の時間微分を $\dot{q}$ と表す。重力加速度を $g$ として，以下の設問に答えよ。

<figure class="problem-figure" markdown>
![二重振り子の座標と角度](../../assets/figures/pastexam-todai-ributsu/H29_butsuri_3-p-light.svg#only-light)
![二重振り子の座標と角度](../../assets/figures/pastexam-todai-ributsu/H29_butsuri_3-p-dark.svg#only-dark)
<figcaption markdown="span">図1：二重振り子</figcaption>
</figure>

(1) この系のラグランジアンを，$m_1,\ m_2$ とデカルト座標系における質点の座標 $(x_1, y_1),\ (x_2, y_2)$，およびそれらの時間微分 $\dot{x}_1,\ \dot{y}_1,\ \dot{x}_2,\ \dot{y}_2$ を用いて表せ。

(2) $x_1,\ y_1,\ x_2,\ y_2$ を，$\ell_1,\ \ell_2$，および，それぞれの糸の鉛直下向きからの角度 $\theta_1,\ \theta_2$ を用いて表せ。

以下，振動が微小（$|\theta_1| \ll 1,\ |\theta_2| \ll 1$）である場合を考え，$\theta_1,\ \theta_2,\ \dot{\theta}_1,\ \dot{\theta}_2$ について3次以上の項を無視する。

(3) この場合，ラグランジアンは定数を除いて以下の式で表されることを示せ。

$$
L = \frac{1}{2}(m_1 + m_2)\ell_1^2\dot{\theta}_1^2 + \frac{1}{2}m_2\ell_2^2\dot{\theta}_2^2 + m_2\ell_1\ell_2\dot{\theta}_1\dot{\theta}_2 - \frac{1}{2}(m_1 + m_2)g\ell_1\theta_1^2 - \frac{1}{2}m_2 g\ell_2\theta_2^2
$$

(4) 設問3で与えられたラグランジアンから $\theta_1,\ \theta_2$ に関する運動方程式を導け。

(5) $\omega$ をこの系の固有角振動数とするとき，運動方程式は，$\theta_1(t) = a_1\cos\omega t,\ \theta_2(t) = a_2\cos\omega t$ の形の解をもつ。ここで，$a_1,\ a_2$ は時間によらない係数である。このことを用いて，固有角振動数 $\omega$ を $g,\ m_1,\ m_2,\ \ell_1,\ \ell_2$ で表せ。

次に $m_1$ が $m_2$ に比べて非常に大きい（$m_1 \gg m_2$）状況を考えよう。
{: .problem-lead }

(6) $|\ell_1 - \ell_2|$ が $\sqrt{m_2/m_1}\,(\ell_1 + \ell_2)$ に比べて十分大きく，後者が前者に対して無視できるとき，固有角振動数は $m_1,\ m_2$ を含まない形で表される。このとき，全ての固有角振動数と対応する固有モードの係数の組 $(a_1, a_2)$ を求めよ。

(7) はじめ，$\ell_1 \gg \ell_2$ として，初期条件 $\theta_1 = \theta_2,\ \dot{\theta}_1 = \dot{\theta}_2 = 0$ で二重振り子を振動させる。その後，全体の長さ $\ell_1 + \ell_2 = \ell$ を保ったまま，固有角振動数に比べて非常にゆっくりと $\ell_1$ を短くしていく。横軸を $\ell_2/\ell$，縦軸を $g/(\omega^2\ell)$ に取り，固有角振動数の変化の様子を図示せよ。また，最終的に $\ell_2 \gg \ell_1$ となった時，質点1が止まり，質点2のみが振動する。その理由を述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成29年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
振れの角が小さいときは，ラグランジアンを角度とその時間微分の2次まで展開すると，運動方程式は連立の線形方程式になります。解を $\cos\omega t$ の形におくと，振幅が $0$ でない解がある条件から固有振動数が求まります。

糸の長さを固有振動の周期よりゆっくり変えると，系は同じ固有モードにとどまったまま，振動数と振幅の比が変わっていきます。そこで，長さの比を変えたときに2つの固有振動数がどう動くかを追い，はじめのモードが長さを変えた後にどのモードにつながるかを調べます。
</div>

### (1)
鉛直下向きを $y$ 軸の正の向きとしているので，重力ポテンシャルエネルギーは $U = -m_1 g y_1 - m_2 g y_2$ です。運動エネルギー $T$ との差 $L = T - U$ をとります。したがって，

$$
\finalanswer{L = \frac{1}{2}m_1\left(\dot{x}_1^2 + \dot{y}_1^2\right) + \frac{1}{2}m_2\left(\dot{x}_2^2 + \dot{y}_2^2\right) + m_1 g y_1 + m_2 g y_2}
$$

### (2)
図1から，各質点の座標は次のようになります。

$$
\finalanswer{x_1 = \ell_1\sin\theta_1,\qquad y_1 = \ell_1\cos\theta_1,\qquad x_2 = \ell_1\sin\theta_1 + \ell_2\sin\theta_2,\qquad y_2 = \ell_1\cos\theta_1 + \ell_2\cos\theta_2}
$$

### (3)
問2の座標を時間微分します。

$$
\begin{aligned}
\dot{x}_1 &= \ell_1\dot{\theta}_1\cos\theta_1, & \dot{y}_1 &= -\ell_1\dot{\theta}_1\sin\theta_1 \\
\dot{x}_2 &= \ell_1\dot{\theta}_1\cos\theta_1 + \ell_2\dot{\theta}_2\cos\theta_2, & \dot{y}_2 &= -\ell_1\dot{\theta}_1\sin\theta_1 - \ell_2\dot{\theta}_2\sin\theta_2
\end{aligned}
$$

これより速度の2乗は $\dot{x}_1^2 + \dot{y}_1^2 = \ell_1^2\dot{\theta}_1^2$ および $\dot{x}_2^2 + \dot{y}_2^2 = \ell_1^2\dot{\theta}_1^2 + \ell_2^2\dot{\theta}_2^2 + 2\ell_1\ell_2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1 - \theta_2)$ となります。

$|\theta_1| \ll 1,\ |\theta_2| \ll 1$ より $\cos(\theta_1 - \theta_2) \simeq 1$，$\cos\theta_i \simeq 1 - \dfrac{1}{2}\theta_i^2\ (i = 1, 2)$ として2次まで残すと，

$$
\begin{aligned}
L
&\simeq \frac{1}{2}(m_1 + m_2)\ell_1^2\dot{\theta}_1^2 + \frac{1}{2}m_2\ell_2^2\dot{\theta}_2^2 + m_2\ell_1\ell_2\dot{\theta}_1\dot{\theta}_2 \\
&\quad + (m_1 + m_2)g\ell_1\left(1 - \frac{1}{2}\theta_1^2\right) + m_2 g\ell_2\left(1 - \frac{1}{2}\theta_2^2\right)
\end{aligned}
$$

定数項 $(m_1 + m_2)g\ell_1 + m_2 g\ell_2$ を除くと，問題文のラグランジアンが得られます。

### (4)
設問3のラグランジアンに対して $\theta_1,\ \theta_2$ のオイラー・ラグランジュ方程式 $\dfrac{\mathrm{d}}{\mathrm{d}t}\left(\dfrac{\partial L}{\partial\dot{\theta}_i}\right) - \dfrac{\partial L}{\partial\theta_i} = 0$ を用います。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t}\left[(m_1 + m_2)\ell_1^2\dot{\theta}_1 + m_2\ell_1\ell_2\dot{\theta}_2\right] + (m_1 + m_2)g\ell_1\theta_1 &= 0 \\
\frac{\mathrm{d}}{\mathrm{d}t}\left[m_2\ell_2^2\dot{\theta}_2 + m_2\ell_1\ell_2\dot{\theta}_1\right] + m_2 g\ell_2\theta_2 &= 0
\end{aligned}
$$

第1式を $\ell_1$，第2式を $m_2\ell_2$ で割ります。したがって，

$$
\finalanswer{(m_1 + m_2)\ell_1\ddot{\theta}_1 + m_2\ell_2\ddot{\theta}_2 + (m_1 + m_2)g\theta_1 = 0,\qquad \ell_1\ddot{\theta}_1 + \ell_2\ddot{\theta}_2 + g\theta_2 = 0}
$$

### (5)
$\theta_1(t) = a_1\cos\omega t,\ \theta_2(t) = a_2\cos\omega t$ を問4の運動方程式に代入します。

$$
\begin{pmatrix}
(m_1 + m_2)(g - \ell_1\omega^2) & -m_2\ell_2\omega^2 \\
-\ell_1\omega^2 & g - \ell_2\omega^2
\end{pmatrix}
\begin{pmatrix} a_1 \\ a_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$(a_1, a_2) \neq (0, 0)$ の解をもつ条件は係数行列の行列式が $0$ であることです。

$$
\begin{aligned}
(m_1 + m_2)(g - \ell_1\omega^2)(g - \ell_2\omega^2) - m_2\ell_1\ell_2\omega^4 &= 0 \\
m_1\ell_1\ell_2\omega^4 - (m_1 + m_2)g(\ell_1 + \ell_2)\omega^2 + (m_1 + m_2)g^2 &= 0
\end{aligned}
$$

これを $\omega^2$ の2次方程式として解き，$\omega > 0$ をとります。

$$
\begin{aligned}
\omega_\pm^2
&= \frac{g}{2m_1\ell_1\ell_2}\left[(m_1 + m_2)(\ell_1 + \ell_2) \pm \sqrt{(m_1 + m_2)^2(\ell_1 + \ell_2)^2 - 4m_1(m_1 + m_2)\ell_1\ell_2}\right] \\
&= \frac{g}{2m_1\ell_1\ell_2}\left[(m_1 + m_2)(\ell_1 + \ell_2) \pm \sqrt{(m_1 + m_2)^2(\ell_1 - \ell_2)^2 + 4m_2(m_1 + m_2)\ell_1\ell_2}\right]
\end{aligned}
$$

したがって，

$$
\finalanswer{\omega_\pm = \sqrt{\frac{g}{2m_1\ell_1\ell_2}\left[(m_1 + m_2)(\ell_1 + \ell_2) \pm \sqrt{(m_1 + m_2)^2(\ell_1 - \ell_2)^2 + 4m_2(m_1 + m_2)\ell_1\ell_2}\right]}}
$$

### (6)
問5の2次方程式の両辺を $(m_1 + m_2)\omega^4$ で割り，$X = \dfrac{g}{\omega^2}$ についての2次方程式に書き直します。

$$
X^2 - (\ell_1 + \ell_2)X + \frac{m_1}{m_1 + m_2}\ell_1\ell_2 = 0
$$

解の公式から，$X$ は次のようになります。

$$
X = \frac{1}{2}\left[\ell_1 + \ell_2 \pm \sqrt{(\ell_1 - \ell_2)^2 + \frac{4m_2}{m_1 + m_2}\ell_1\ell_2}\right]
$$

ここで $4\ell_1\ell_2 \le (\ell_1 + \ell_2)^2$ であり，条件 $|\ell_1 - \ell_2| \gg \sqrt{\dfrac{m_2}{m_1}}(\ell_1 + \ell_2)$ より根号内の第2項は第1項に比べて十分小さいため省略することができます。すると $X = \ell_1$ または $X = \ell_2$，すなわち

$$
\omega_1 = \sqrt{\frac{g}{\ell_1}},\qquad \omega_2 = \sqrt{\frac{g}{\ell_2}}
$$

となります。$k$ を $0$ でない任意定数として，対応する固有モード $(a_1,a_2)$ を問5の連立方程式から求めます。

$\omega_1 = \sqrt{\dfrac{g}{\ell_1}}$ のモードは，第2式 $-\ell_1\omega_1^2 a_1 + (g - \ell_2\omega_1^2)a_2 = 0$ から求めます。$\omega_1^2 = g/\ell_1$ を代入します。

$$
\begin{aligned}
-g a_1 + g\left(1 - \frac{\ell_2}{\ell_1}\right)a_2 &= 0 \\
\frac{a_2}{a_1} &= \frac{\ell_1}{\ell_1 - \ell_2}
\end{aligned}
$$

よって，$(a_1, a_2) = k(\ell_1 - \ell_2,\ \ell_1)$ です。

$\omega_2 = \sqrt{\dfrac{g}{\ell_2}}$ のモードは，第1式 $(m_1 + m_2)(g - \ell_1\omega_2^2)a_1 = m_2\ell_2\omega_2^2 a_2$ から求めます。$\omega_2^2 = g/\ell_2$ を代入します。

$$
\begin{aligned}
\frac{a_1}{a_2} &= \frac{m_2}{m_1 + m_2}\frac{\ell_2}{\ell_2 - \ell_1} \\
&\simeq 0
\end{aligned}
$$

$m_1\gg m_2$ と長さの条件から，$|a_1/a_2|\ll\sqrt{m_2/m_1}\ll1$ です。よって，$(a_1, a_2) = k(0, 1)$ となります。

したがって，

$$
\finalanswer{\omega_1 = \sqrt{\frac{g}{\ell_1}}:\ (a_1, a_2) = k(\ell_1 - \ell_2,\ \ell_1),\qquad \omega_2 = \sqrt{\frac{g}{\ell_2}}:\ (a_1, a_2) = k(0,\ 1) \quad (k \neq 0)}
$$

### (7)
$\ell_1 + \ell_2 = \ell$，$u = \dfrac{\ell_2}{\ell}\ (0 < u < 1)$ とおくと $\dfrac{\ell_1}{\ell} = 1 - u$ であり，問6の $X = \dfrac{g}{\omega^2}$ を $\ell$ で割った量は次のようになります。

$$
\frac{g}{\omega_\mp^2 \ell} = \frac{1}{2}\left[1 \pm \sqrt{(1 - 2u)^2 + \frac{4m_2}{m_1 + m_2}u(1 - u)}\right]
$$

$u=1/2$ から離れた領域では，2本の曲線は $y=1-u$ と $y=u$ に近づきます。それぞれ $\omega^2=g/\ell_1$ と $\omega^2=g/\ell_2$ の振動です。$u=1/2$ では $\ell_1=\ell_2$ ですが，2本の曲線は交差しません。最小間隔は $\sqrt{\dfrac{m_2}{m_1+m_2}}\simeq\sqrt{\dfrac{m_2}{m_1}}$ です。

<figure class="problem-figure" markdown>
![l2/lに対するg/(omega^2 l)の変化と擬交差](../../assets/figures/pastexam-todai-ributsu/H29_butsuri_3-s-light.svg#only-light)
![l2/lに対するg/(omega^2 l)の変化と擬交差](../../assets/figures/pastexam-todai-ributsu/H29_butsuri_3-s-dark.svg#only-dark)
<figcaption markdown="span">$\ell_2/\ell$ に対する $g/(\omega^2\ell)$ の変化。$m_1 \gg m_2$ のもとで $\ell_2/\ell = 1/2$ に擬交差が現れ，初期状態は上側の分枝（$\omega_-$，矢印）に沿って断熱的に変化する。</figcaption>
</figure>

最後に，糸の長さを変えた後の振動がこのようになる理由を説明します。

はじめの $\ell_1\gg\ell_2$ では，低振動数の固有モードは

$$
\begin{aligned}
\frac{a_2}{a_1} &\simeq \frac{\ell_1}{\ell_1-\ell_2} \\
&\simeq 1
\end{aligned}
$$

です。したがって，指定された初期条件はこのモードを近似的に励起します。有限の長さ比では振幅比が厳密には1と異なるため，他方のモードもわずかに含まれます。

有限の質量比では2つの固有振動数は交差しません。固有モードの変化を表す混合角を $\eta$ と書くと，$|\dot\eta|\ll|\omega_+-\omega_-|$ を満たすほどゆっくり長さを変える場合，モード間の移行は無視できます。初めに励起した振動は，グラフの上側の分枝に沿って変化します。

最後の $\ell_2\gg\ell_1$ では，上側の分枝は $\sqrt{g/\ell_2}$ の振動へつながります。設問6の振幅比が $(a_1,a_2)\propto(0,1)$ となるため，近似の範囲で質点1は静止し，質点2が振動します。

<aside class="rigor-note" markdown>
糸の長さを変える操作は系に仕事をするため，振動エネルギーが途中で一定とは限りません。ゆっくり長さを変えるときに保たれる量は，各モードのエネルギーを振動数で割った作用変数 $E_i/\omega_i$ です。
</aside>
