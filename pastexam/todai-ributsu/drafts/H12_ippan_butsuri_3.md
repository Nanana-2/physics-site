---
title: 東大理物 平成12年度 一般教育科目 物理学 第3問：ヤングの干渉実験とレンズ結像の分解能
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 一般教育科目 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成12年度 一般教育科目 物理学 第3問：ヤングの干渉実験とレンズ結像の分解能

## 問題

(1) 図1に示すような実験器具で，単色光を使ったヤングの干渉実験を行った。光を単スリット A に通した後，複スリット B，C を通過させると，複スリットから回折した光が干渉し，その結果，スクリーン上に明暗の干渉縞ができた。複スリット B と C の間隔は，$d = 30\,\mu\mathrm{m}$，複スリットとスクリーンとの間の距離は，$a = 5\,\mathrm{cm}$ であった。光は赤色で，波長は $\lambda = 0.6\,\mu\mathrm{m}$ である。この時，スクリーン上で観察される干渉縞の間隔（明線と明線の間隔）$s$ を求めよ。B，C の各々のスリットの幅は十分狭いとしてよい。

(2) 次に，図2に示すような配置に変えた（垂直上方から見た図）。つまり，図1のスクリーンの位置にレンズを置き，スクリーンをその後方に移動させ，複スリットの拡大像をスクリーンに写し出した。使用したレンズは，直径 $L = 2\,\mathrm{cm}$ で焦点距離 $f = 4.5\,\mathrm{cm}$ のものである。この時，ピントのあった像を得るには，レンズとスクリーンの間の距離 $b$ を何 $\mathrm{cm}$ にすればよいか。また，スクリーン上に輝線として写し出された複スリット像の間隔 $D$ は何 $\mathrm{mm}$ か。

(3) 図2の配置のまま，複スリットを，B と C の間隔 $d = 2\,\mu\mathrm{m}$ のものに交換した。すると，スクリーン上に写し出された複スリットの像が2本の輝線ではなく，1本の輝線として観察された。ルーペでスクリーン上の像を拡大してみても，輝線は1本のままであった。なぜ，複スリットの間隔が狭い場合には2本の輝線に分離して観察されないのか，理由を説明せよ。

(4) スクリーン上で2本の輝線として観察される複スリットの最小間隔 $d_0$ を求めよ。

(5) 設問 (3) の観察で，$d_0$ が狭い場合でも複スリットの像が2本に分離された輝線としてスクリーンに写し出されるようにしたい。光源の波長を変えない場合，どのような工夫をすればよいか。また波長を変えて良い場合は，どのようにすればよいか。各々理由をつけて答えよ。

<figure class="problem-figure" markdown>
![ヤングの干渉実験の配置](../../../docs/assets/figures/pastexam-todai-ributsu/H12_ippan_butsuri_3-p1-light.svg#only-light){ loading=lazy }
![ヤングの干渉実験の配置](../../../docs/assets/figures/pastexam-todai-ributsu/H12_ippan_butsuri_3-p1-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">図1：単スリット A，複スリット B，C，およびスクリーンによるヤングの干渉実験の配置。</figcaption>
</figure>

<figure class="problem-figure" markdown>
![レンズを用いた複スリット結像の配置](../../../docs/assets/figures/pastexam-todai-ributsu/H12_ippan_butsuri_3-p2-light.svg#only-light){ loading=lazy }
![レンズを用いた複スリット結像の配置](../../../docs/assets/figures/pastexam-todai-ributsu/H12_ippan_butsuri_3-p2-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">図2：図1のスクリーンの位置に直径 $L$ のレンズを置いて複スリットの拡大像をスクリーンに結ぶ配置（上方から見た図）。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 一般教育科目 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
前半では，2つのスリットからの光路差が波長の整数倍になる条件から干渉縞の間隔 $s = a\lambda/d$ を求め，薄肉レンズの結像公式と横倍率からスクリーン上の拡大像の位置と間隔を計算します。

後半では，図1のスクリーン位置にレンズを置いたという配置が鍵になります。レンズ面には複スリットによる0次および $\pm 1$ 次以上の回折光が干渉縞をつくっており，複スリット像が2本に分離して再現されるためには，レンズの有限な直径 $L$ が0次の明線だけでなく $\pm 1$ 次の明線も取り込む必要があります。この条件 $s \le L/2$ から最小分解間隔 $d_0$ と分解能を高める方法を導きます。
</div>

### (1)

スクリーン上で中心から測った位置を $x$ とします。$d \ll a$ および $|x| \ll a$ のとき，複スリット B，C からスクリーン上の点 $x$ までの光路差 $\Delta l$ は次で近似されます。

$$
\Delta l \approx d\sin\theta \approx d\frac{x}{a}
$$

明線が生じる条件は，整数 $m$ を用いて $\Delta l = m\lambda$ です。したがって，$m$ 番目の明線の位置 $x_m$ は次になります。

$$
x_m = m\frac{a\lambda}{d}
$$

隣り合う明線の間隔 $s = x_{m+1} - x_m$ に，$a = 5\,\mathrm{cm} = 5.0 \times 10^{-2}\,\mathrm{m}$，$\lambda = 0.6\,\mu\mathrm{m} = 6.0 \times 10^{-7}\,\mathrm{m}$，$d = 30\,\mu\mathrm{m} = 3.0 \times 10^{-5}\,\mathrm{m}$ を代入します。

$$
\begin{aligned}
s &= \frac{a\lambda}{d} \\
&= \frac{5.0 \times 10^{-2} \times 6.0 \times 10^{-7}}{3.0 \times 10^{-5}} \\
&= 1.0 \times 10^{-3}\,\mathrm{m}
\end{aligned}
$$

したがって，干渉縞の間隔 $s$ は次の通りです。

$$
\finalanswer{s = 1.0\,\mathrm{mm}}
$$

### (2)

薄肉レンズの結像公式 $\dfrac{1}{a} + \dfrac{1}{b} = \dfrac{1}{f}$ に，$a = 5\,\mathrm{cm}$，$f = 4.5\,\mathrm{cm}$ を代入して $b$ を求めます。

$$
\begin{aligned}
\frac{1}{b} &= \frac{1}{f} - \frac{1}{a} \\
&= \frac{1}{4.5} - \frac{1}{5} \\
&= \frac{5 - 4.5}{22.5} \\
&= \frac{0.5}{22.5} \\
&= \frac{1}{45}
\end{aligned}
$$

よって $b = 45\,\mathrm{cm}$ です。

像の横倍率 $M$ は $M = \dfrac{b}{a}$ です。これよりスクリーン上の複スリット像の間隔 $D = Md$ を計算します。

$$
\begin{aligned}
M &= \frac{b}{a} \\
&= \frac{45}{5} \\
&= 9
\end{aligned}
$$

$$
\begin{aligned}
D &= Md \\
&= 9 \times 30\,\mu\mathrm{m} \\
&= 270\,\mu\mathrm{m} \\
&= 0.27\,\mathrm{mm}
\end{aligned}
$$

したがって，$b$ と $D$ の値は次の通りです。

$$
\finalanswer{b = 45\,\mathrm{cm}, \qquad D = 0.27\,\mathrm{mm}}
$$

### (3)

複スリット B，C を通過した光は回折して広がり，複スリットから距離 $a$ にあるレンズの位置で間隔 $s = \dfrac{a\lambda}{d}$ の干渉縞をつくります。レンズによってスクリーン上に複スリットの2本の像が再現されるためには，レンズの中央に入る0次の回折光だけでなく，複スリットの間隔 $d$ の情報を含む $\pm 1$ 次以上の回折光もレンズを通過してスクリーン上で再び干渉する必要があります。

複スリットの間隔を $d = 2\,\mu\mathrm{m}$ に狭めると，レンズの位置での明線間隔 $s$ は次の値になります。

$$
\begin{aligned}
s &= \frac{a\lambda}{d} \\
&= \frac{5.0 \times 10^{-2} \times 6.0 \times 10^{-7}}{2.0 \times 10^{-6}} \\
&= 1.5 \times 10^{-2}\,\mathrm{m} \\
&= 1.5\,\mathrm{cm}
\end{aligned}
$$

レンズの半径は $\dfrac{L}{2} = 1.0\,\mathrm{cm}$ であり，$s = 1.5\,\mathrm{cm} > 1.0\,\mathrm{cm}$ となるため，$\pm 1$ 次の回折光はレンズの外側に外れてしまい，0次の回折光しかレンズに入りません。別の見方をすれば，直径 $L$ の有限な開口をもつレンズを通過する際の回折によって，各スリットの像がスクリーン上で幅 $\sim \dfrac{b\lambda}{L}$ だけ広がり，2本の輝線が完全に重なり合ってしまうためです。像そのものの段階で2本の分離情報が失われているため，スクリーン上の像をルーペで拡大しても1本の輝線にしか見えません。

### (4)

単スリット A からのコヒーレントな単色光が複スリットに垂直入射している図2の配置では，0次の回折光がレンズの中心を通り，$\pm 1$ 次の回折光がレンズ中心から距離 $s = \dfrac{a\lambda}{d}$ の位置に到達します。スクリーン上に2本の輝線として分離した像が結ばれるための条件は，$\pm 1$ 次の回折光がレンズ中心から半径 $\dfrac{L}{2}$ 以内の有効開口に入ることです。

$$
\frac{a\lambda}{d} \le \frac{L}{2}
$$

これを $d$ について解くと $d \ge \dfrac{2a\lambda}{L}$ となります。

この下限 $d_0 = \dfrac{2a\lambda}{L}$ に $a = 5\,\mathrm{cm}$，$L = 2\,\mathrm{cm}$，$\lambda = 0.6\,\mu\mathrm{m}$ を代入します。

$$
\begin{aligned}
d_0 &= \frac{2 \times 5\,\mathrm{cm} \times 0.6\,\mu\mathrm{m}}{2\,\mathrm{cm}} \\
&= 3.0\,\mu\mathrm{m}
\end{aligned}
$$

この値は (3) の $d = 2\,\mu\mathrm{m}$ より大きく，$d = 2\,\mu\mathrm{m}$ で分離できなかった事実とも整合します。したがって，求める最小間隔 $d_0$ は次の通りです。

$$
\finalanswer{d_0 = \frac{2a\lambda}{L} = 3.0\,\mu\mathrm{m}}
$$

### (5)

(4) の式 $d_0 = \dfrac{2a\lambda}{L}$ より，より狭い複スリット間隔を分離するには $d_0$ を小さくすればよいことがわかります。

光源の波長 $\lambda$ を変えない場合，次の工夫が有効です。

- レンズの直径 $L$ を大きくする。開口が広くなることで，回折角の大きい $\pm 1$ 次以上の回折光をレンズに取り込むことができるためです。
- 複スリットとレンズの距離 $a$ を小さくする。焦点距離の短いレンズを用いて複スリットに近づけると，レンズ面での干渉縞の間隔 $s = \dfrac{a\lambda}{d}$ が狭くなり，$\pm 1$ 次の回折光がレンズ内に入りやすくなるためです。
- 複スリットとレンズの間を屈折率 $n$（$> 1$）の透明な媒質で満たす。媒質中では光の波長が $\dfrac{\lambda}{n}$ に短くなり，最小間隔が $\dfrac{d_0}{n}$ に減少するためです。
- 光を複スリットに対して斜めに入射させる。0次の回折光をレンズの端に通すことで，片側の1次回折光がレンズの反対側の端まで入れるようになり，条件が $s \le L$ となって最小間隔が半分の $\dfrac{a\lambda}{L}$ まで小さくなるためです。

光源の波長 $\lambda$ を変えてよい場合は，赤色光より波長の短い光を用います。たとえば青色光や紫色光，さらに紫外線など波長 $\lambda$ の短い光に変えると，回折による広がり角 $\dfrac{\lambda}{d}$ が小さくなってレンズ面での明線間隔 $s = \dfrac{a\lambda}{d}$ が狭まり，$\pm 1$ 次の回折光がレンズを通過できるようになるため，より狭い間隔の複スリットを2本に分離して観察することができます。

<aside class="rigor-note" markdown>
(4) で導いた $d_0 = \dfrac{2a\lambda}{L}$ は，単スリット A からの垂直入射によるコヒーレント照明に対するアッベの分解能の基準であり，レンズの開口半角 $\theta$ を用いて $d_0 = \dfrac{\lambda}{\sin\theta} \approx \dfrac{2a\lambda}{L}$ と表されます。実際，幅 $L$ の1次元開口を通した2つの同位相点光源の像の振幅は $\operatorname{sinc}\left(\dfrac{L(X' - d/2)}{a\lambda}\right) + \operatorname{sinc}\left(\dfrac{L(X' + d/2)}{a\lambda}\right)$ に比例し，$d = d_0$ のとき中央 $X' = 0$ の強度がちょうど $0$ になって2本の輝線が明瞭に分かれます。なお，光源が互いにインコヒーレントである場合のレイリー基準は，1次元スリット開口で $\dfrac{a\lambda}{L} = 1.5\,\mu\mathrm{m}$，円形開口で $1.22\dfrac{a\lambda}{L} \approx 1.8\,\mu\mathrm{m}$ ですが，図2は単スリット A によるコヒーレント垂直照明であるため，(3) の $d = 2\,\mu\mathrm{m}$ でも分離されず $d_0 = 3.0\,\mu\mathrm{m}$ が該当します。
</aside>
