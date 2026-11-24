---
title: 東大理物 平成29年度 物理学 第5問：光共振器とモード同期によるフェムト秒レーザーパルス
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成29年度
exam_subject: 物理学
exam_number: 第5問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して解答にグラフを追加しています。
---

# 東大理物 平成29年度 物理学 第5問：光共振器とモード同期によるフェムト秒レーザーパルス

## 問題

物質中の超高速現象の観測にフェムト秒（$10^{-15}\ \mathrm{s}$）レーザーパルスが広く使われている。ここでは，「モード同期」と呼ばれる方法によってフェムト秒パルスを発生させる原理を簡単なモデルを用いて考察しよう。いま，図 1 のように間隔 $d$ で平行に設置された 2 枚の鏡で構成された共振器中に屈折率 $\eta$ のレーザー媒質があるとする。この共振器中に図 2 のように，レーザー媒質で決まる角周波数の範囲内に，等しい振幅 $E_0$，および，等しい角周波数間隔 $\Delta\omega$ の $N$ 個のモード（角周波数と位相でラベルされた成分電場）が存在するとし，その全複素電場を $E(t) = E_0 \sum_{n=0}^{N-1} e^{i(\omega_n t + \phi_n)}$ と書く。ここで，$\omega_n$ は角周波数，$\phi_n$ はそのモードの位相である。全てのモードを同期させ，同位相で振動させることができたとし，全ての $n$ に対して $\phi_n = \phi_0$ と表す。このとき全複素電場は，$E(t) = E_0 e^{i\phi_0} \sum_{n=0}^{N-1} e^{i\omega_n t}$ で与えられる。以下の設問に答えよ。

<figure class="problem-figure" markdown>
![間隔dの2枚の鏡と屈折率etaのレーザー媒質からなる共振器](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_5-p1-light.svg#only-light)
![間隔dの2枚の鏡と屈折率etaのレーザー媒質からなる共振器](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_5-p1-dark.svg#only-dark)
<figcaption markdown="span">図 1：間隔 $d$ で平行に設置された 2 枚の鏡で構成された共振器中に屈折率 $\eta$ のレーザー媒質がある。</figcaption>
</figure>

<figure class="problem-figure" markdown>
![等間隔Delta omegaのN個のモードスペクトル](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_5-p2-light.svg#only-light)
![等間隔Delta omegaのN個のモードスペクトル](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_5-p2-dark.svg#only-dark)
<figcaption markdown="span">図 2：レーザー媒質で決まる角周波数の範囲内に，等しい振幅 $E_0$，および，等しい角周波数間隔 $\Delta\omega$ の $N$ 個のモード（角周波数と位相でラベルされた成分電場）が存在する。</figcaption>
</figure>

(1) 共振器中には定在波が立つことに注意して，共振器中に存在する隣り合うモードの角周波数間隔 $\Delta\omega = \omega_{n+1} - \omega_n$ を $d$，$\eta$，および，真空中の光速 $c$ を用いて表せ。

(2) $n$ 番目のモードの角周波数 $\omega_n$ を角周波数間隔 $\Delta\omega$ を用いて $\omega_n = \omega_0 + n\Delta\omega$ と表せば，各モードからの $E(t)$ への寄与は公比 $e^{i\Delta\omega t}$ の等比数列となる。その和を計算した結果として得られる $E(t)$ の表式を求めよ。

(3) いま，光の強度 $I(t)$ を $I(t) = |E(t)|^2$ と表し，$E(t)$ に対する設問 2 の結果を代入すると $I(t) = E_0^2 \dfrac{\sin^2(\boxed{\text{ア}})}{\sin^2(\boxed{\text{イ}})}$ の形に整理できる。アとイに入るべき表式を $N$，$\Delta\omega$，および，$t$ を用いて答えよ。ただし，$I(t)$ の表式の分母がゼロとなる点での関数値は，その極限値で定義されるものとする。

$I(t)$ は周期的に最大値をとり，それがモード同期によって発生する超短パルスに相当する。$I(t)$ が最大値をとる時刻の一つは $t = 0$ であることに注意して以下の設問に答えよ。
{: .problem-lead }

(4) 設問 3 で得られた光の強度 $I(t)$ の最大値を求めよ。また，得られた光強度の最大値は，各モードの位相が全くランダムな時のおおよそ何倍となるか答えよ。

(5) 設問 3 の結果から，$I(t)$ が最大値をとる時刻は $m$ を整数として $t = m\Delta t_{\mathrm{sep}}$ と表される。$\Delta t_{\mathrm{sep}}$ を $\Delta\omega$ を用いて表せ。

(6) 実際には $N$ は非常に大きな数であるが，簡単のため $N = 5$ とする。設問 3 から 5 の結果に基づいて，$\dfrac{I(t)}{E_0^2}$ のグラフの概形を描け。

(7) モード同期によって発生する超短パルスのパルス幅 $\Delta t_{\mathrm{p}}$ を $I(t)$ が最大値をとった時刻から最初に 0 となる時刻までの時間と定義する。$\Delta t_{\mathrm{p}}$ を $\Delta\omega$，および，$N$ を用いて表せ。一方，レーザー媒質が増幅作用をもつ帯域幅 $\Delta\nu$ は $N\Delta\omega / (2\pi)$ で与えられる。$\Delta t_{\mathrm{p}}$ と $\Delta\nu$ の関係を求め，その物理的意味を簡潔に述べよ。

(8) モード同期によって発生した超短パルスを共振器外（真空中）に取り出したときの波長範囲が $560\text{〜}640\ \mathrm{nm}$ であった。このとき，レーザー媒質が増幅作用をもつ帯域幅 $\Delta\nu\ [\mathrm{s}^{-1}]$ を求め，さらに設問 7 の結果を用いてモード同期によって発生するフェムト秒パルスのパルス幅 $\Delta t_{\mathrm{p}}$ を求めよ。ただし，真空中の光速を $c = 3.0 \times 10^8\ \mathrm{m\,s}^{-1}$ とする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成29年度修士課程入学試験 物理学 第5問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して解答にグラフを追加しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
間隔 $d$ の共振器に立つ定在波モードを同位相で重ね合わせる計算は，空間の回折格子における多光束干渉（ディリクレ核）と数学的に同じ構造であり，等比数列の和から鋭いパルス列 $I(t) \propto \sin^2(N\Delta\omega t / 2) / \sin^2(\Delta\omega t / 2)$ が得られます。

位相をそろえることでピーク強度はランダム位相時の $N$ 倍に増大し，パルス間隔 $\Delta t_{\mathrm{sep}}$ は共振器内の光の 1 往復時間に，パルス幅 $\Delta t_{\mathrm{p}}$ は増幅帯域幅 $\Delta\nu$ の逆数（時間・周波数の不確定性関係）に対応します。
</div>

### (1)
屈折率 $\eta$ の媒質中での光速は $c/\eta$ なので，角周波数 $\omega$ の光の媒質中波長は $\lambda = \dfrac{2\pi c}{\eta\omega}$ です。間隔 $d$ の 2 枚の鏡を節とする定在波の条件は，正の整数 $q$ を用いて次のように表されます。

$$
d = q\frac{\lambda_q}{2} = q\frac{\pi c}{\eta\omega_q} \implies \omega_q = \frac{\pi c}{\eta d}\,q
$$

したがって，隣り合うモードの角周波数間隔 $\Delta\omega = \omega_{n+1} - \omega_n$ は次のとおりです。

$$
\finalanswer{\Delta\omega = \frac{\pi c}{\eta d}}
$$

### (2)
$\omega_n = \omega_0 + n\Delta\omega$ を $E(t)$ の定義式に代入し，初項 $1$，公比 $e^{i\Delta\omega t}$ の等比数列の和を計算します。

$$
\begin{aligned}
E(t)
&= E_0 e^{i\phi_0}\sum_{n=0}^{N-1} e^{i(\omega_0 + n\Delta\omega) t} \\
&= E_0 e^{i(\phi_0 + \omega_0 t)}\sum_{n=0}^{N-1} \left(e^{i\Delta\omega t}\right)^n \\
&= E_0 e^{i(\phi_0 + \omega_0 t)}\frac{1 - e^{iN\Delta\omega t}}{1 - e^{i\Delta\omega t}}
\end{aligned}
$$

さらに分子・分母からそれぞれ $e^{iN\Delta\omega t / 2}$，$e^{i\Delta\omega t / 2}$ をくくり出すと，次のようにも表されます。

$$
E(t) = E_0 e^{i\left[\phi_0 + \left(\omega_0 + \frac{N-1}{2}\Delta\omega\right) t\right]}\frac{\sin\left(\dfrac{N\Delta\omega t}{2}\right)}{\sin\left(\dfrac{\Delta\omega t}{2}\right)}
$$

$$
\finalanswer{E(t) = E_0 e^{i(\phi_0 + \omega_0 t)}\frac{1 - e^{iN\Delta\omega t}}{1 - e^{i\Delta\omega t}}}
$$

### (3)
設問 2 の結果の絶対値の 2 乗を計算します。実数 $\theta$ に対して $|1 - e^{i\theta}|^2 = (1 - \cos\theta)^2 + \sin^2\theta = 2(1 - \cos\theta) = 4\sin^2(\theta/2)$ なので，

$$
\begin{aligned}
I(t) = |E(t)|^2
&= E_0^2 \frac{|1 - e^{iN\Delta\omega t}|^2}{|1 - e^{i\Delta\omega t}|^2} \\
&= E_0^2 \frac{4\sin^2\left(\dfrac{N\Delta\omega t}{2}\right)}{4\sin^2\left(\dfrac{\Delta\omega t}{2}\right)}
= E_0^2 \frac{\sin^2\left(\dfrac{N\Delta\omega t}{2}\right)}{\sin^2\left(\dfrac{\Delta\omega t}{2}\right)}
\end{aligned}
$$

となります。したがって，アは $\dfrac{N\Delta\omega t}{2}$，イは $\dfrac{\Delta\omega t}{2}$ です。

$$
\finalanswer{\frac{N\Delta\omega t}{2}, \qquad \frac{\Delta\omega t}{2}}
$$

### (4)
$I(t)$ が最大値をとる $t = 0$ での極限値を求めます。$\lim_{x \to 0}\dfrac{\sin x}{x} = 1$ より，

$$
I_{\max} = \lim_{t \to 0} E_0^2 \frac{\sin^2(N\Delta\omega t / 2)}{\sin^2(\Delta\omega t / 2)} = E_0^2 \left(\frac{N\Delta\omega / 2}{\Delta\omega / 2}\right)^2 = N^2 E_0^2
$$

となります。

一方，各モードの位相 $\phi_n$ が全くランダムな場合，強度 $I_{\mathrm{rand}}(t) = |E(t)|^2$ を位相について平均すると，$n \neq m$ の干渉項 $\langle e^{i(\phi_n - \phi_m)} \rangle = 0$ が消えるため，

$$
\langle I_{\mathrm{rand}}(t) \rangle
= E_0^2 \sum_{n=0}^{N-1}\sum_{m=0}^{N-1} \left\langle e^{i(\phi_n - \phi_m)} \right\rangle e^{i(\omega_n - \omega_m) t}
= E_0^2 \sum_{n=0}^{N-1} 1 = N E_0^2
$$

となります。したがって，モード同期時の光強度の最大値 $N^2 E_0^2$ は，位相がランダムなときの強度 $N E_0^2$ のおおよそ **$N$ 倍**になります。

$$
\finalanswer{I_{\max} = N^2 E_0^2, \qquad \frac{I_{\max}}{\langle I_{\mathrm{rand}} \rangle} = N}
$$

### (5)
$I(t) = E_0^2 \dfrac{\sin^2(N\Delta\omega t / 2)}{\sin^2(\Delta\omega t / 2)}$ が最大値 $N^2 E_0^2$ をとるのは，分母が $0$ となる時刻，すなわち整数 $m$ を用いて

$$
\frac{\Delta\omega t}{2} = m\pi \implies t = m\frac{2\pi}{\Delta\omega}
$$

のときです。したがって，$\Delta t_{\mathrm{sep}}$ は次のとおりです。

$$
\finalanswer{\Delta t_{\mathrm{sep}} = \frac{2\pi}{\Delta\omega}}
$$

### (6)
$N = 5$ のとき，$\dfrac{I(t)}{E_0^2} = \dfrac{\sin^2(5\Delta\omega t / 2)}{\sin^2(\Delta\omega t / 2)}$ は周期 $\Delta t_{\mathrm{sep}} = \dfrac{2\pi}{\Delta\omega}$ の周期関数であり，次の特徴をもちます。

- 主極大：$t = m\Delta t_{\mathrm{sep}}$（$m$ は整数）で最大値 $N^2 = 25$ をとります。
- 零点：$t = \dfrac{k}{5}\Delta t_{\mathrm{sep}}$（$k$ は $5$ の倍数でない整数）で $0$ になります。
- 副極大：隣り合う主極大の間に $N - 2 = 3$ 個の小さな副極大が現れます（中央の $t = \dfrac{1}{2}\Delta t_{\mathrm{sep}}$ では高さ $1$，その左右では高さ約 $1.5$）。

以上の特徴をまとめたグラフの概形は次の図のとおりです。

<figure class="problem-figure" markdown>
![N=5のときのモード同期光強度I(t)/E_0^2のグラフ](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_5-s-light.svg#only-light)
![N=5のときのモード同期光強度I(t)/E_0^2のグラフ](../../../docs/assets/figures/pastexam-todai-ributsu/H29_butsuri_5-s-dark.svg#only-dark)
<figcaption markdown="span">$N = 5$ における $\dfrac{I(t)}{E_0^2}$ の時間変化。周期 $\Delta t_{\mathrm{sep}}$ ごとに高さ $25$ の主極大が現れ，その間に $4$ 個の零点と $3$ 個の副極大がある。</figcaption>
</figure>

### (7)
$t = 0$ で最大値をとったあと，$I(t)$ が最初に $0$ となるのは分子 $\sin(N\Delta\omega t / 2)$ が最初に $0$ となる時刻なので，

$$
\frac{N\Delta\omega \Delta t_{\mathrm{p}}}{2} = \pi \implies \Delta t_{\mathrm{p}} = \frac{2\pi}{N\Delta\omega}
$$

となります。ここに帯域幅 $\Delta\nu = \dfrac{N\Delta\omega}{2\pi}$ を代入すると，

$$
\Delta t_{\mathrm{p}} = \frac{1}{\Delta\nu} \iff \Delta t_{\mathrm{p}}\,\Delta\nu = 1
$$

が得られます。この関係は，時間領域の波形と周波数領域のスペクトルがフーリエ変換で結ばれていることに由来する時間と周波数の不確定性関係を表しており，より短い時間幅 $\Delta t_{\mathrm{p}}$ の超短パルスを生成するためには，より広い増幅帯域幅 $\Delta\nu$ をもつレーザー媒質が必要であることを示しています。

$$
\finalanswer{\Delta t_{\mathrm{p}} = \frac{2\pi}{N\Delta\omega}, \qquad \Delta t_{\mathrm{p}}\,\Delta\nu = 1}
$$

### (8)
真空中での波長 $\lambda_1 = 560\ \mathrm{nm} = 5.60 \times 10^{-7}\ \mathrm{m}$ と $\lambda_2 = 640\ \mathrm{nm} = 6.40 \times 10^{-7}\ \mathrm{m}$ に対応する周波数の差が帯域幅 $\Delta\nu$ です。

$$
\begin{aligned}
\Delta\nu
&= \frac{c}{\lambda_1} - \frac{c}{\lambda_2}
= c\frac{\lambda_2 - \lambda_1}{\lambda_1 \lambda_2} \\
&= 3.0 \times 10^8 \times \frac{(640 - 560) \times 10^{-9}}{560 \times 10^{-9} \times 640 \times 10^{-9}} \\
&= \frac{3.0 \times 10^{17} \times 80}{560 \times 640}
= \frac{3.0 \times 10^{17}}{4480}
\approx 6.7 \times 10^{13}\ \mathrm{s}^{-1}
\end{aligned}
$$

設問 7 の関係 $\Delta t_{\mathrm{p}} = \dfrac{1}{\Delta\nu}$ より，パルス幅 $\Delta t_{\mathrm{p}}$ は次のようになります。

$$
\Delta t_{\mathrm{p}} = \frac{1}{\Delta\nu} = \frac{4480}{3.0 \times 10^{17}} \approx 1.5 \times 10^{-14}\ \mathrm{s} = 15\ \mathrm{fs}
$$

$$
\finalanswer{\Delta\nu \approx 6.7 \times 10^{13}\ \mathrm{s}^{-1}, \qquad \Delta t_{\mathrm{p}} \approx 1.5 \times 10^{-14}\ \mathrm{s}\ (15\ \mathrm{fs})}
$$

<aside class="rigor-note" markdown>
設問 1 と設問 5 の結果を組み合わせると，パルス間隔は $\Delta t_{\mathrm{sep}} = \dfrac{2\pi}{\Delta\omega} = \dfrac{2\eta d}{c}$ となります。これは屈折率 $\eta$ の媒質を満たした長さ $d$ の共振器内を光パルスが 1 往復する時間に等しく，単一の超短パルスが 2 枚の鏡の間を往復しながら半透鏡を通して 1 往復ごとに外部へ射出される描像と完全に一致します。
</aside>
