---
title: 東大理物 平成9年度 一般教育科目 物理学 第1問：剛体棒で結ばれた2質点と質点の完全弾性衝突
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 一般教育科目 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成9年度 一般教育科目 物理学 第1問：剛体棒で結ばれた2質点と質点の完全弾性衝突

## 問題

長さ $2a$ で質量の無視できる剛体の棒の両端に，ともに質量 $M$ をもつ質点 $\mathrm{A}$ および $\mathrm{B}$ が取り付けられ，図のように $xy$ 平面内に静止している。そこに質量 $m$ の質点 $\mathrm{C}$ が，図のように直線 $y = a$ に沿って，速度 $v$ で $x$ 軸の正の向きに等速直線運動して，質点 $\mathrm{A}$ と衝突した。衝突は完全弾性的であり，衝突後の $\mathrm{C}$ の運動は $x$ 軸に平行であるとして，以下の設問に答えよ。ただし摩擦や重力は考えない。
{: .problem-lead }

<figure class="problem-figure" markdown>
![xy平面内の剛体棒で結ばれた2質点A・Bと直線y=aに沿って入射する質点Cの配置](../../../docs/assets/figures/pastexam-todai-ributsu/H9_ippan_butsuri_1-p-light.svg#only-light){ loading=lazy }
![xy平面内の剛体棒で結ばれた2質点A・Bと直線y=aに沿って入射する質点Cの配置](../../../docs/assets/figures/pastexam-todai-ributsu/H9_ippan_butsuri_1-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) 衝突後の系（$\mathrm{A}$，$\mathrm{B}$，$\mathrm{C}$）の運動を記述するのに適した複数個の物理量を定義し，それらがどのような力学的保存則により決定されるかを述べ，式で表わせ。

(2) 力学的保存則を解いて，上で定義した物理量を，$M$，$m$，$a$，および $v$ で表わせ。

(3) 衝突後，質点 $\mathrm{A}$ および $\mathrm{B}$ の速度の $x$ 成分は，どのように時間変化するか。衝突後の経過時間 $t$ の関数として，同一のグラフに図示せよ。特徴的な座標の値も記入すること。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 一般教育科目 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
摩擦や重力がないため，質点 $\mathrm{A}, \mathrm{B}, \mathrm{C}$ からなる孤立系では衝突の前後で運動量と角運動量が保存され，さらに完全弾性衝突であるため運動エネルギーも保存されます。衝突後の $\mathrm{C}$ の運動は $x$ 軸に平行なので，剛体 $\mathrm{AB}$ の重心も $x$ 軸の正の向きに並進しながら重心まわりに一定の角速度で回転します。3つの保存則を連立して並進速度と角速度を求め，重心の並進速度と回転による速度を重ね合わせることで $\mathrm{A}, \mathrm{B}$ の速度の $x$ 成分が得られます。
</div>

### (1)

衝突前の全運動量は $x$ 軸正方向のみであり，衝突後の質点 $\mathrm{C}$ の運動も $x$ 軸に平行です。したがって運動量保存則より，剛体 $\mathrm{AB}$ の重心も衝突後に $y$ 方向の速度をもたず，$x$ 軸に平行に運動します。以上を踏まえ，衝突後の系の運動を記述する3つの物理量を次のように定義します。

- 衝突後の質点 $\mathrm{C}$ の速度の $x$ 成分を $u$ とします。
- 衝突後の剛体 $\mathrm{AB}$ の重心の速度の $x$ 成分を $V$ とします。
- 衝突後の剛体 $\mathrm{AB}$ の重心まわりの時計回りの角速度を $\omega$ とします。

衝突の前後で外力ははたらかず，衝突は完全弾性的であるため，以下の3つの力学的保存則が成り立ちます。

第1に，系全体の $x$ 方向の運動量保存則が成り立ちます。剛体 $\mathrm{AB}$ の全質量は $2M$ なので，次式が得られます。

$$
m v = m u + 2 M V
$$

第2に，原点 $\mathrm{O}$ すなわち衝突時の剛体 $\mathrm{AB}$ の重心位置まわりの角運動量保存則が成り立ちます。紙面表から裏へ向かう向きすなわち時計回りを正とします。剛体 $\mathrm{AB}$ の重心まわりの慣性モーメントは $I = 2 M a^2$ であり，衝突直後の重心の位置ベクトルは原点に一致するため，重心の並進運動による原点まわりの角運動量は $0$ です。したがって次式が得られます。

$$
m v a = m u a + 2 M a^2 \omega
$$

第3に，完全弾性衝突であるため力学的エネルギー保存則すなわち運動エネルギー保存則が成り立ちます。剛体 $\mathrm{AB}$ の運動エネルギーは重心の並進運動エネルギーと重心まわりの回転運動エネルギーの和なので，次式となります。

$$
\frac{1}{2} m v^2 = \frac{1}{2} m u^2 + \frac{1}{2}(2M) V^2 + \frac{1}{2}(2 M a^2)\omega^2
$$

これら3つの独立な保存則によって，未知量 $u, V, \omega$ が一意に決定されます。

### (2)

(1) で得た3つの保存則の式を連立して解きます。まず運動量保存則と角運動量保存則をそれぞれ整理します。

$$
\begin{aligned}
m(v - u) &= 2 M V \\
m(v - u) &= 2 M a \omega
\end{aligned}
$$

これらを比較すると，次の関係が得られます。

$$
a\omega = V
$$

次に，運動エネルギー保存則の両辺を $2$ 倍して変形し，$a\omega = V$ を代入します。

$$
\begin{aligned}
m(v^2 - u^2) &= 2 M V^2 + 2 M (a\omega)^2 \\
m(v - u)(v + u) &= 4 M V^2
\end{aligned}
$$

ここで衝突が起こるためには $v \neq u$ すなわち $V \neq 0$ です。運動量保存則 $m(v - u) = 2 M V$ を上式に代入して両辺を $2 M V$ で割ると，次式が得られます。

$$
v + u = 2 V
$$

これと $m(v - u) = 2 M V$ を連立して $u$ を消去します。$u = 2V - v$ を代入すると

$$
m(2v - 2V) = 2 M V
$$

となり，$(m + M)V = mv$ から $V$ が求まります。続いて $u = 2V - v$ および $\omega = \dfrac{V}{a}$ を計算します。

$$
\begin{aligned}
V &= \frac{m}{m + M} v \\
u &= \frac{2m}{m + M} v - v \\
&= \frac{m - M}{m + M} v \\
\omega &= \frac{m v}{(m + M) a}
\end{aligned}
$$

なお，質量 $M$ の質点 $\mathrm{A}$ に質量 $m$ の質点 $\mathrm{C}$ が正面弾性衝突したときと同じ反発結果になっており，これは衝突瞬間に質点 $\mathrm{B}$ の初速度が $V - a\omega = 0$ となって棒に沿う方向以外の撃力を $\mathrm{B}$ が受けないことと整合しています。

$$
\finalanswer{u = \frac{m - M}{m + M} v,\qquad V = \frac{m}{m + M} v,\qquad \omega = \frac{m v}{(m + M) a}}
$$

### (3)

衝突直後の時刻を $t = 0$ とします。衝突後，剛体 $\mathrm{AB}$ の重心は速度 $V$ で $x$ 軸の正の向きに等速直線運動し，棒は重心まわりに一定の時計回り角速度 $\omega$ で回転します。時刻 $t$ における重心の座標は $(Vt, 0)$ であり，棒が $y$ 軸正方向から時計回りに回転した角度は $\theta(t) = \omega t$ です。

したがって，時刻 $t$ における質点 $\mathrm{A}$ と質点 $\mathrm{B}$ の $x$ 座標はそれぞれ次のようになります。

$$
\begin{aligned}
x_{\mathrm{A}}(t) &= V t + a \sin\omega t \\
x_{\mathrm{B}}(t) &= V t - a \sin\omega t
\end{aligned}
$$

これらを時間 $t$ で微分し，(2) で得られた関係 $a\omega = V$ を用いると，質点 $\mathrm{A}$ および $\mathrm{B}$ の速度の $x$ 成分が得られます。

$$
\begin{aligned}
v_{\mathrm{A}x}(t) &= V + a\omega\cos\omega t \\
&= V(1 + \cos\omega t) \\
v_{\mathrm{B}x}(t) &= V - a\omega\cos\omega t \\
&= V(1 - \cos\omega t)
\end{aligned}
$$

ここで $V = \dfrac{m}{m + M}v$，周期は $T = \dfrac{2\pi}{\omega}$ すなわち $\dfrac{2\pi(m + M)a}{m v}$ です。

$v_{\mathrm{A}x}(t)$ と $v_{\mathrm{B}x}(t)$ はいずれも最小値 $0$ と最大値 $2V = \dfrac{2m}{m + M}v$ の間を周期 $T = \dfrac{2\pi}{\omega}$ で単振動します。$t = 0$ では $v_{\mathrm{A}x}(0) = 2V$，$v_{\mathrm{B}x}(0) = 0$ であり，半周期後の $t = \dfrac{\pi}{\omega}$ で $v_{\mathrm{A}x} = 0$，$v_{\mathrm{B}x} = 2V$ となって両者の値が入れ替わります。また $t = \dfrac{\pi}{2\omega}, \dfrac{3\pi}{2\omega}, \dots$ では両曲線が $v_x = V$ で交わります。これを同一のグラフに図示すると次のようになります。

![衝突後の質点AおよびBの速度のx成分の時間変化](../../../docs/assets/figures/pastexam-todai-ributsu/H9_ippan_butsuri_1-s-light.svg#only-light){ loading=lazy }
![衝突後の質点AおよびBの速度のx成分の時間変化](../../../docs/assets/figures/pastexam-todai-ributsu/H9_ippan_butsuri_1-s-dark.svg#only-dark){ loading=lazy }

$$
\finalanswer{v_{\mathrm{A}x}(t) = \frac{m v}{m + M}\left(1 + \cos\omega t\right),\qquad v_{\mathrm{B}x}(t) = \frac{m v}{m + M}\left(1 - \cos\omega t\right),\qquad \omega = \frac{m v}{(m + M)a}}
$$
