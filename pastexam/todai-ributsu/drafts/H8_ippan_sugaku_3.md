---
title: 東大理物 平成8年度 一般教育科目 数学 第3問：長い針に対するビュフォンの針の問題
tags:
  - 院試過去問
  - 東大理物
  - 確率・統計
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 一般教育科目 数学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成8年度 一般教育科目 数学 第3問：長い針に対するビュフォンの針の問題

## 問題

床一面に引かれた間隔 $a$ の平行線に上から長さ $l$（$\ge a$）の棒を落としたとき，棒が平行線と交わる確率 $P(l)$ を以下の手順にしたがって求めよ。
{: .problem-lead }

<figure class="problem-figure" markdown>
![間隔aの平行線群と長さlの棒の配置](../../../docs/assets/figures/pastexam-todai-ributsu/H8_ippan_sugaku_3-p-light.svg#only-light){ loading=lazy }
![間隔aの平行線群と長さlの棒の配置](../../../docs/assets/figures/pastexam-todai-ributsu/H8_ippan_sugaku_3-p-dark.svg#only-dark){ loading=lazy }
</figure>

(a) 棒の一端が平行線から $x$ の距離（$0 \le x \le a/2$）にあるときに，棒が平行線と交わる確率 $p(x)$ を求めよ。ただし，棒の方位角は床面内で一様に分布するものとする。また，棒の太さは無視する。

(b) $x$ が $[0, a/2]$ の区間で一様に分布するとして，$P(l)$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 一般教育科目 数学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
棒の長さが平行線の間隔以上である $l \ge a$ の長い針に対するビュフォンの針の問題です。棒の一端から両側の平行線までの距離がそれぞれ $x$ と $a - x$ であるため，余事象である棒がどちらの平行線とも交わらない方位角の範囲を逆正弦関数 $\arcsin$ で求めると条件付き確率 $p(x)$ が得られます。それを $[0, a/2]$ 上で平均すれば $P(l)$ が閉じた形で求まります。
</div>

### (a)

平行線に平行な向きを基準として，棒の一端から他端へ向かう方向の方位角を $-\pi < \phi \le \pi$ の範囲の $\phi$ とします。最も近い平行線が下方すなわち距離 $x$ の位置にあり，反対側の隣り合う平行線が上方すなわち距離 $a - x$ の位置にあるように座標をとります。なお $0 \le x \le \dfrac{a}{2}$ なので $0 \le x \le a - x \le a \le l$ です。

棒の他端の垂直変位は $l\sin\phi$ で与えられます。したがって棒がどちらの平行線とも交わらないための条件は，他端がこれら2本の平行線の内側に収まること，すなわち

$$
-x < l\sin\phi < a - x
$$

が成り立つことです。$0 \le \dfrac{x}{l} \le 1$ かつ $0 \le \dfrac{a - x}{l} \le 1$ なので，角度

$$
\theta_1 = \arcsin\left(\frac{x}{l}\right), \qquad \theta_2 = \arcsin\left(\frac{a - x}{l}\right)
$$

をそれぞれ区間 $\left[0, \dfrac{\pi}{2}\right]$ に定義できます。

$-\pi < \phi \le \pi$ の範囲で $-\dfrac{x}{l} < \sin\phi < \dfrac{a - x}{l}$ を満たす $\phi$ の範囲は，右向き側と左向き側の2つの区間に分かれます。

- 右向き側では $-\theta_1 < \phi < \theta_2$ であり，その角度幅は $\theta_1 + \theta_2$ です。
- 左向き側では $\pi - \theta_2 < \phi \le \pi$ および $-\pi < \phi < -\pi + \theta_1$ であり，合わせた角度幅は同じく $\theta_1 + \theta_2$ です。

したがって，棒がどの平行線とも交わらない方位角の合計幅は $2(\theta_1 + \theta_2)$ となります。方位角 $\phi$ は幅 $2\pi$ の区間 $(-\pi, \pi]$ に一様に分布するため，棒が平行線と交わらない確率は $\dfrac{2(\theta_1 + \theta_2)}{2\pi} = \dfrac{\theta_1 + \theta_2}{\pi}$ です。

よって，余事象をとることで棒が少なくとも1本の平行線と交わる確率 $p(x)$ が得られます。

$$
\finalanswer{p(x) = 1 - \frac{1}{\pi}\left[\arcsin\left(\frac{x}{l}\right) + \arcsin\left(\frac{a - x}{l}\right)\right]}
$$

### (b)

$x$ は区間 $\left[0, \dfrac{a}{2}\right]$ で一様に分布するため，求める確率 $P(l)$ は $p(x)$ をこの区間で平均した値です。

$$
P(l) = \frac{2}{a}\int_0^{a/2} p(x)\,\mathrm{d}x
$$

(a) の結果を代入し，第2項の積分では変数変換 $u = a - x$ を行います。

$$
\begin{aligned}
\int_0^{a/2}\left[\arcsin\left(\frac{x}{l}\right) + \arcsin\left(\frac{a - x}{l}\right)\right]\mathrm{d}x &= \int_0^{a/2}\arcsin\left(\frac{x}{l}\right)\mathrm{d}x + \int_{a/2}^{a}\arcsin\left(\frac{u}{l}\right)\mathrm{d}u \\
&= \int_0^a \arcsin\left(\frac{x}{l}\right)\mathrm{d}x
\end{aligned}
$$

次に $t = \dfrac{x}{l}$ と置換し，部分積分を用いて $\int \arcsin t\,\mathrm{d}t = t\arcsin t + \sqrt{1 - t^2}$ を計算します。

$$
\begin{aligned}
\int_0^a \arcsin\left(\frac{x}{l}\right)\mathrm{d}x &= l\int_0^{a/l}\arcsin t\,\mathrm{d}t \\
&= l\left[t\arcsin t + \sqrt{1 - t^2}\right]_0^{a/l} \\
&= a\arcsin\left(\frac{a}{l}\right) + \sqrt{l^2 - a^2} - l
\end{aligned}
$$

これを $P(l)$ の式に代入して整理します。

$$
\begin{aligned}
P(l) &= 1 - \frac{2}{\pi a}\left[a\arcsin\left(\frac{a}{l}\right) + \sqrt{l^2 - a^2} - l\right] \\
&= 1 + \frac{2}{\pi}\left[\frac{l}{a} - \sqrt{\left(\frac{l}{a}\right)^2 - 1} - \arcsin\left(\frac{a}{l}\right)\right]
\end{aligned}
$$

さらに恒等式 $\dfrac{\pi}{2} - \arcsin\left(\dfrac{a}{l}\right) = \arccos\left(\dfrac{a}{l}\right)$ を用いると，次の簡潔な形にも表されます。

$$
P(l) = \frac{2}{\pi}\left[\frac{l}{a} - \sqrt{\left(\frac{l}{a}\right)^2 - 1} + \arccos\left(\frac{a}{l}\right)\right]
$$

極限を確認すると，$l = a$ のとき $P(a) = \dfrac{2}{\pi}$ となり短い針の公式 $P(l) = \dfrac{2l}{\pi a}$ と連続に接続します。また $l/a \to \infty$ のとき $\dfrac{l}{a} - \sqrt{\left(\dfrac{l}{a}\right)^2 - 1} \to 0$ かつ $\arccos\left(\dfrac{a}{l}\right) \to \dfrac{\pi}{2}$ より $P(l) \to 1$ となり，物理的・幾何学的に整合しています。

$$
\finalanswer{P(l) = \frac{2}{\pi}\left[\frac{l}{a} - \sqrt{\left(\frac{l}{a}\right)^2 - 1} + \arccos\left(\frac{a}{l}\right)\right]}
$$
