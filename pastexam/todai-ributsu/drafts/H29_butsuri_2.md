---
title: 東大理物 平成29年度 物理学 第2問：正方格子反強磁性イジング模型の平均場近似とフラストレーション
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
  - 物性物理学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成29年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成29年度 物理学 第2問：正方格子反強磁性イジング模型の平均場近似とフラストレーション

## 問題

温度 $T$ の熱平衡状態にある大きさ $1/2$ のスピンを考える。スピンと外部磁場 $H$ の相互作用はハミルトニアン $\mathcal{H}_1 = -\mu H\sigma$ によって記述される。ただし，$\sigma$ はスピンの向きに応じて $+1$ または $-1$ の値をとる変数（スピン変数）で，$\mu$ はスピンの磁気モーメントの大きさを表す定数である。ボルツマン定数を $k_{\mathrm{B}}$ として，以下の設問に答えよ。

(1) 外部磁場 $H$ のもとで，$\sigma = +1$ となる確率 $p_+$ および $\sigma = -1$ となる確率 $p_-$ を求めよ。

(2) 外部磁場 $H$ のもとで，$\sigma$ の期待値が $\langle\sigma\rangle = \tanh\left(\dfrac{\mu H}{k_{\mathrm{B}}T}\right)$ となることを示せ。

次に図1のような正方格子上で隣接スピン間に交換相互作用 $J$ が働くイジング模型を考える。そのハミルトニアンは
{: .problem-lead }

$$
\mathcal{H}_2 = J\sum_{\langle i, j \rangle}\sigma_i\sigma_j - \mu H\sum_i \sigma_i
$$

で与えられる。ここで，$\sigma_i\ (= \pm 1)$ は格子点 $i$ におけるスピン変数を表し，$\displaystyle\sum_{\langle i, j \rangle}$ は隣接格子点の組についての和を表す。また，反強磁性相互作用（$J > 0$）を仮定する。この模型を平均場近似の範囲内で取り扱うことを考える。
{: .problem-lead }

<figure class="problem-figure" markdown>
![正方格子上のA・B副格子と最近接交換相互作用J](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_2-p1-light.svg#only-light)
![正方格子上のA・B副格子と最近接交換相互作用J](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_2-p1-dark.svg#only-dark)
<figcaption markdown="span">図1</figcaption>
</figure>

(3) 正方格子は図1のように1つおきに A, B の2つの格子に分けることができる。平均場近似では，格子 A, B 上のスピンはそれぞれ

$$
\mu H_{\mathrm{eff, A}} = -zJ\langle\sigma_{\mathrm{B}}\rangle + \mu H,\qquad
\mu H_{\mathrm{eff, B}} = -zJ\langle\sigma_{\mathrm{A}}\rangle + \mu H
$$

で決まる有効磁場 $H_{\mathrm{eff, A}},\ H_{\mathrm{eff, B}}$ を感じると仮定する。ここで $\langle\sigma_{\mathrm{A}}\rangle,\ \langle\sigma_{\mathrm{B}}\rangle$ は，それぞれ格子 A, B 上のスピン変数の期待値である。また，$z$ は隣接スピンの数で，正方格子では $z = 4$ である。この有効磁場のもとで，格子 A, B 上のスピン変数の期待値を計算すると，$\langle\sigma_{\mathrm{A}}\rangle$ と $\langle\sigma_{\mathrm{B}}\rangle$ が満たすべき式（セルフ・コンシステント方程式）はある関数 $f(x)$ を用いて以下の形で表される。

$$
\langle\sigma_{\mathrm{A}}\rangle = f(\langle\sigma_{\mathrm{B}}\rangle),\qquad \langle\sigma_{\mathrm{B}}\rangle = f(\langle\sigma_{\mathrm{A}}\rangle).
$$

$f(x)$ を求めよ。

(4) $H = 0$ のとき，セルフ・コンシステント方程式が反強磁性秩序に対応する解 $\langle\sigma_{\mathrm{A}}\rangle = -\langle\sigma_{\mathrm{B}}\rangle \neq 0$ をもつための条件を考える。$y = f(x)$ のグラフを考えることで，このような解は，ある転移温度 $T_{\mathrm{N}}$ よりも低温でのみ存在することがわかる。$T_{\mathrm{N}}$ を求めよ。

(5) セルフ・コンシステント方程式を利用して，$T > T_{\mathrm{N}}$ における1スピンあたりの帯磁率

$$
\chi = \lim_{H \to 0}\frac{\mathrm{d}}{\mathrm{d}H}\left(\mu\frac{\langle\sigma_{\mathrm{A}}\rangle + \langle\sigma_{\mathrm{B}}\rangle}{2}\right)
$$

を求めよ。

次に図2のような正方格子上の隣接スピン間および対角線方向の隣接スピン間に，それぞれ交換相互作用 $J,\ J'$ が働くイジング模型を考える。そのハミルトニアンは
{: .problem-lead }

$$
\mathcal{H}_3 = J\sum_{\langle i, j \rangle}\sigma_i\sigma_j + J'\sum_{\langle\langle i, j \rangle\rangle}\sigma_i\sigma_j - \mu H\sum_i \sigma_i
$$

で与えられる。ここで，$\displaystyle\sum_{\langle\langle i, j \rangle\rangle}$ は図2の破線で示される対角線方向の隣接格子点の組についての和を表す。ただし，交換相互作用が $0 < J' < J$ という条件を満たしているとする。
{: .problem-lead }

<figure class="problem-figure" markdown>
![正方格子上の最近接相互作用Jと対角線方向相互作用J'](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_2-p2-light.svg#only-light)
![正方格子上の最近接相互作用Jと対角線方向相互作用J'](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_2-p2-dark.svg#only-dark)
<figcaption markdown="span">図2</figcaption>
</figure>

(6) 設問3と同様にして2つの格子 A, B を考え，平均場近似を適用して，$H = 0$ のときのセルフ・コンシステント方程式を書き下せ。また，$\langle\sigma_{\mathrm{A}}\rangle = -\langle\sigma_{\mathrm{B}}\rangle \neq 0$ となるような反強磁性秩序の転移温度を求めよ。さらに $J' \to J$ の極限で転移温度が $0$ となることを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成29年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
隣接スピンの平均を使うと，各格子点の交換相互作用を有効磁場として扱うことができます。正方格子を2つの副格子に分けることで，隣接するスピンが逆向きを向く配置を調べることができます。

平均スピンが小さい範囲では，平均場の方程式を1次まで展開することで応答を求めることができます。同じ副格子を結ぶ相互作用も，有効磁場に含めて比較します。
</div>

### (1)
逆温度を $\beta = \dfrac{1}{k_{\mathrm{B}}T}$ とします。分配関数 $Z_1$ は

$$
\begin{aligned}
Z_1 &= e^{\beta\mu H} + e^{-\beta\mu H} \\
&= 2\cosh\left(\frac{\mu H}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

なので，ボルツマン分布より各状態の確率は次のようになります。したがって，

$$
\finalanswer{p_+ = \frac{e^{\frac{\mu H}{k_{\mathrm{B}}T}}}{e^{\frac{\mu H}{k_{\mathrm{B}}T}} + e^{-\frac{\mu H}{k_{\mathrm{B}}T}}},\qquad p_- = \frac{e^{-\frac{\mu H}{k_{\mathrm{B}}T}}}{e^{\frac{\mu H}{k_{\mathrm{B}}T}} + e^{-\frac{\mu H}{k_{\mathrm{B}}T}}}}
$$

### (2)
問1の確率を用いて $\sigma$ の期待値を計算します。

$$
\begin{aligned}
\langle\sigma\rangle &= (+1)p_+ + (-1)p_- \\
&= \frac{e^{\frac{\mu H}{k_{\mathrm{B}}T}} - e^{-\frac{\mu H}{k_{\mathrm{B}}T}}}{e^{\frac{\mu H}{k_{\mathrm{B}}T}} + e^{-\frac{\mu H}{k_{\mathrm{B}}T}}} \\
&= \tanh\left(\frac{\mu H}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

よって題意の関係が成り立ちます。

### (3)
問2の結果の磁場 $H$ をそれぞれ有効磁場 $H_{\mathrm{eff, A}},\ H_{\mathrm{eff, B}}$ に置き換えます。正方格子では $z = 4$ なので，

$$
\langle\sigma_{\mathrm{A}}\rangle = \tanh\left(\frac{-4J\langle\sigma_{\mathrm{B}}\rangle + \mu H}{k_{\mathrm{B}}T}\right),\qquad
\langle\sigma_{\mathrm{B}}\rangle = \tanh\left(\frac{-4J\langle\sigma_{\mathrm{A}}\rangle + \mu H}{k_{\mathrm{B}}T}\right)
$$

となります。したがって，関数 $f(x)$ は

$$
\finalanswer{f(x) = \tanh\left(\frac{-zJx + \mu H}{k_{\mathrm{B}}T}\right) = \tanh\left(\frac{-4Jx + \mu H}{k_{\mathrm{B}}T}\right)}
$$

### (4)
$H = 0$ のとき $f(x) = -\tanh\left(\dfrac{4Jx}{k_{\mathrm{B}}T}\right)$ は奇関数です。反強磁性秩序の解 $\langle\sigma_{\mathrm{A}}\rangle = -\langle\sigma_{\mathrm{B}}\rangle \equiv m\ (\neq 0)$ を代入すると，2つの式はともに1つの方程式にまとまります。

$$
\begin{aligned}
m &= f(-m) \\
&= \tanh\left(\frac{4Jm}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

右辺の関数 $g(m) = \tanh\left(\dfrac{4Jm}{k_{\mathrm{B}}T}\right)$ は $m > 0$ で上に凸かつ $\displaystyle\lim_{m\to\infty} g(m) = 1$ であり，原点 $m = 0$ での傾きは $g'(0) = \dfrac{4J}{k_{\mathrm{B}}T}$ です。したがって $y = m$ と $y = g(m)$ が $m = 0$ 以外の交点をもつための必要十分条件は原点での傾きが $1$ より大きいことです。

$$
\frac{4J}{k_{\mathrm{B}}T} > 1 \iff T < \frac{4J}{k_{\mathrm{B}}}
$$

よって転移温度 $T_{\mathrm{N}}$ は $\dfrac{4J}{k_{\mathrm{B}}}$ です。したがって，

$$
\finalanswer{T_{\mathrm{N}} = \frac{4J}{k_{\mathrm{B}}}}
$$

### (5)
$T>T_{\mathrm N}$ では自発磁化がありません。微小磁場のもとで両副格子の期待値は等しいので，$\langle\sigma_{\mathrm A}\rangle=\langle\sigma_{\mathrm B}\rangle\equiv\sigma$ とします。$H\to0$ で $\sigma\to0$ となるため，$\tanh u=u+\mathcal O(u^3)$ を用います。

$$
\begin{aligned}
\sigma &= \tanh\left(\frac{-4J\sigma + \mu H}{k_{\mathrm{B}}T}\right) \\
&\simeq \frac{-4J\sigma + \mu H}{k_{\mathrm{B}}T} \\
\left(1 + \frac{4J}{k_{\mathrm{B}}T}\right)\sigma &\simeq \frac{\mu H}{k_{\mathrm{B}}T} \\
\sigma &\simeq \frac{\mu H}{k_{\mathrm{B}}T + 4J}
\end{aligned}
$$

これを帯磁率 $\chi$ の定義に代入します。

$$
\begin{aligned}
\chi &= \lim_{H \to 0}\frac{\mathrm{d}}{\mathrm{d}H}(\mu\sigma) \\
&= \frac{\mu^2}{k_{\mathrm{B}}T + 4J} \\
&= \frac{\mu^2}{k_{\mathrm{B}}(T + T_{\mathrm{N}})}
\end{aligned}
$$

したがって，

$$
\finalanswer{\chi = \frac{\mu^2}{k_{\mathrm{B}}T + 4J} = \frac{\mu^2}{k_{\mathrm{B}}(T + T_{\mathrm{N}})}}
$$

### (6)
格子 A の1つのスピンは，相互作用 $J$ で格子 B の4個のスピンと結ばれています。対角線方向の相互作用 $J'$ は，同じ格子 A の4個のスピンを結びます。格子 B についても同様です。

よって $H = 0$ での平均場近似の有効磁場はそれぞれ次のようになります。

$$
\mu H_{\mathrm{eff, A}} = -4J\langle\sigma_{\mathrm{B}}\rangle - 4J'\langle\sigma_{\mathrm{A}}\rangle,\qquad
\mu H_{\mathrm{eff, B}} = -4J\langle\sigma_{\mathrm{A}}\rangle - 4J'\langle\sigma_{\mathrm{B}}\rangle
$$

したがってセルフ・コンシステント方程式は次のとおりです。

$$
\langle\sigma_{\mathrm{A}}\rangle = \tanh\left(-\frac{4J\langle\sigma_{\mathrm{B}}\rangle + 4J'\langle\sigma_{\mathrm{A}}\rangle}{k_{\mathrm{B}}T}\right),\qquad
\langle\sigma_{\mathrm{B}}\rangle = \tanh\left(-\frac{4J\langle\sigma_{\mathrm{A}}\rangle + 4J'\langle\sigma_{\mathrm{B}}\rangle}{k_{\mathrm{B}}T}\right)
$$

ここに反強磁性秩序解 

$$
\begin{aligned}
\langle\sigma_{\mathrm{A}}\rangle &= -\langle\sigma_{\mathrm{B}}\rangle \\
&= m\ (\neq 0)
\end{aligned}
$$

 を代入します。

$$
m = \tanh\left(\frac{4(J - J')m}{k_{\mathrm{B}}T}\right)
$$

$0 < J' < J$ より $J - J' > 0$ なので，問4と同様に原点での傾きが $1$ より大きい条件から転移温度 $T_{\mathrm{N}}'$ が決まります。

$$
\frac{4(J - J')}{k_{\mathrm{B}}T} > 1 \iff T < T_{\mathrm{N}}' = \frac{4(J - J')}{k_{\mathrm{B}}}
$$

この式において $J' \to J$ の極限をとると，

$$
\begin{aligned}
\lim_{J' \to J} T_{\mathrm{N}}' &= \lim_{J' \to J} \frac{4(J - J')}{k_{\mathrm{B}}} \\
&= 0
\end{aligned}
$$

となり，転移温度が $0$ に近づくことが確かめられます。したがって，

$$
\finalanswer{\langle\sigma_{\mathrm{A}}\rangle = \tanh\left(-\frac{4J\langle\sigma_{\mathrm{B}}\rangle + 4J'\langle\sigma_{\mathrm{A}}\rangle}{k_{\mathrm{B}}T}\right),\quad \langle\sigma_{\mathrm{B}}\rangle = \tanh\left(-\frac{4J\langle\sigma_{\mathrm{A}}\rangle + 4J'\langle\sigma_{\mathrm{B}}\rangle}{k_{\mathrm{B}}T}\right),\qquad T_{\mathrm{N}}' = \frac{4(J - J')}{k_{\mathrm{B}}}}
$$

<aside class="rigor-note" markdown>
設問6は，2つの副格子の平均が逆向きとなる配置についての結果です。この配置の1スピン当たりの基底エネルギーは $-2J+2J'$ です。一方，列ごとに向きが交互に変わる配置では $-2J'$ となるため，$J'>J/2$ では後者のエネルギーが低くなります。設問6の転移温度を，この領域で実現する秩序全体の転移温度と解釈しないようにします。
</aside>
