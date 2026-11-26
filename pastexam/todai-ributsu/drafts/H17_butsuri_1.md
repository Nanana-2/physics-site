---
title: 東大理物 平成17年度 物理学 第1問：1次元井戸型ポテンシャルの散乱と共鳴透過
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成17年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成17年度 物理学 第1問：1次元井戸型ポテンシャルの散乱と共鳴透過

## 問題

幅 $a$，深さ $-V_0\ (< 0)$ の一次元井戸型ポテンシャル $V(x)$ を考える（図1）。質量 $m$ の粒子が，$x = -\infty$ から波数 $k$ の平面波 $e^{ikx}$ で入射すると，その一部は反射し，一部は透過する。このとき，$x < -a/2$ と $x > a/2$ における波動関数を，それぞれ $\psi = e^{ikx} + Re^{-ikx}$，$\psi = Te^{ikx}$ とし，また $-a/2 \le x \le a/2$ における波動関数を $\psi = \alpha e^{ipx} + \beta e^{-ipx}$ として，以下の設問に答えよ。ただし，$\hbar = h/(2\pi)$（$h$ はプランク定数）とする。

<figure class="problem-figure" markdown>
![1次元井戸型ポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H17_butsuri_1-p-light.svg#only-light)
![1次元井戸型ポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H17_butsuri_1-p-dark.svg#only-dark)
<figcaption markdown="span">図1：幅 $a$，深さ $-V_0$ の1次元井戸型ポテンシャル。</figcaption>
</figure>

(1) 入射波，反射波，透過波に対するフラックス（確率密度の流れ）を，$\hbar, m, k, R, T$ を用いて表せ。また $T$ と $R$ の関係式を与えよ。

(2) $T = |T|e^{i\theta}$ と書くとき，位相 $\theta$ が現れる物理的理由を簡潔に述べよ。

(3) $p$ を $\hbar, m, k, V_0$ を用いて表せ。

(4) $T$ を以下の式のように表すとき，$A$ と $B$ を $k$ と $p$ を用いて表せ。

$$
T = \frac{e^{-ika}}{A\cos(pa) - iB\sin(pa)}
$$

(5) 入射した波が反射を全く受けない（完全透過する）ための $k$ が満たすべき条件を求めよ。また，完全透過がおこる物理的理由を簡潔に述べよ。

(6) $|T|^2$ を $k$ の関数として図示せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成17年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
ポテンシャルが区分的に一定な1次元散乱問題では，各領域でのシュレーディンガー方程式の解が平面波の線形結合になります。井戸の左右2つの境界で波動関数とその1階導関数が連続である条件を連立させると，井戸内の係数 $\alpha, \beta$ と反射振幅 $R$ を消して透過振幅 $T$ を直接求めることができます。

定常状態では確率密度の流れが空間的に一定になるため，入射流と反射流・透過流のつり合いから $|R|^2 + |T|^2 = 1$ が成り立ちます。また，井戸の内部では波数が $k$ から $p$ へ変わるため，左右の境界での反射波同士の干渉によって透過率が波数 $k$ に応じて振動します。
</div>

### (1)

1次元の確率密度の流れ $j(x)$ は次式で定義されます。

$$
j(x) = \frac{\hbar}{2mi}\left(\psi^*\frac{\mathrm{d}\psi}{\mathrm{d}x} - \psi\frac{\mathrm{d}\psi^*}{\mathrm{d}x}\right)
$$

入射波 $\psi_{\mathrm{in}} = e^{ikx}$，反射波 $\psi_{\mathrm{ref}} = R e^{-ikx}$，透過波 $\psi_{\mathrm{tr}} = T e^{ikx}$ のそれぞれについて計算します。

$$
\begin{aligned}
j_{\mathrm{in}} &= \frac{\hbar}{2mi}\bigl(e^{-ikx}(ik e^{ikx}) - e^{ikx}(-ik e^{-ikx})\bigr) \\
&= \frac{\hbar}{2mi}(2ik) \\
&= \frac{\hbar k}{m}
\end{aligned}
$$

$$
\begin{aligned}
j_{\mathrm{ref}} &= \frac{\hbar}{2mi}\bigl(R^* e^{ikx}(-ik R e^{-ikx}) - R e^{-ikx}(ik R^* e^{ikx})\bigr) \\
&= \frac{\hbar}{2mi}\bigl(-2ik|R|^2\bigr) \\
&= -\frac{\hbar k}{m}|R|^2
\end{aligned}
$$

$$
\begin{aligned}
j_{\mathrm{tr}} &= \frac{\hbar}{2mi}\bigl(T^* e^{-ikx}(ik T e^{ikx}) - T e^{ikx}(-ik T^* e^{-ikx})\bigr) \\
&= \frac{\hbar}{2mi}\bigl(2ik|T|^2\bigr) \\
&= \frac{\hbar k}{m}|T|^2
\end{aligned}
$$

次に $T$ と $R$ の関係式を求めます。$x < -a/2$ での波動関数 $\psi = e^{ikx} + Re^{-ikx}$ 全体の確率密度の流れ $j_-$ を計算します。

$$
\begin{aligned}
j_- &= \frac{\hbar}{2mi}\Bigl((e^{-ikx} + R^* e^{ikx})ik(e^{ikx} - Re^{-ikx}) - (e^{ikx} + Re^{-ikx})(-ik)(e^{-ikx} - R^* e^{ikx})\Bigr) \\
&= \frac{\hbar k}{2m}\Bigl((1 - |R|^2 - Re^{-2ikx} + R^* e^{2ikx}) + (1 - |R|^2 + Re^{-2ikx} - R^* e^{2ikx})\Bigr) \\
&= \frac{\hbar k}{m}\bigl(1 - |R|^2\bigr)
\end{aligned}
$$

定常状態の連続の式より $\dfrac{\mathrm{d}j}{\mathrm{d}x} = 0$ なので，$x < -a/2$ での流れ $j_-$ と $x > a/2$ での流れ $j_{\mathrm{tr}}$ は等しくなります。

$$
\frac{\hbar k}{m}\bigl(1 - |R|^2\bigr) = \frac{\hbar k}{m}|T|^2
$$

両辺を $\dfrac{\hbar k}{m}$ で割って整理すると，$|R|^2 + |T|^2 = 1$ が得られます。

$$
\finalanswer{j_{\mathrm{in}} = \frac{\hbar k}{m}, \quad j_{\mathrm{ref}} = -\frac{\hbar k}{m}|R|^2, \quad j_{\mathrm{tr}} = \frac{\hbar k}{m}|T|^2, \quad |R|^2 + |T|^2 = 1}
$$

### (2)

井戸の領域 $-a/2 \le x \le a/2$ ではポテンシャルが $-V_0 < 0$ と低いため，粒子の運動エネルギーが増えて波数 $p$ が自由空間の波数 $k$ より大きくなります。そのため，井戸を通過する間に進む位相が自由空間をそのまま進む場合と異なり，さらに井戸の左右の壁での多重反射に伴う干渉も加わります。この結果，ポテンシャルがない場合の透過波 $e^{ikx}$ と比べて位相のずれが生じ，それが位相因子 $e^{i\theta}$ として現れます。

### (3)

エネルギー固有値を $E$ とします。井戸の外側 $|x| > a/2$ では $V(x) = 0$ なので $E = \dfrac{\hbar^2 k^2}{2m}$ です。井戸の内側 $-a/2 \le x \le a/2$ では $V(x) = -V_0$ なので，シュレーディンガー方程式 $-\dfrac{\hbar^2}{2m}\dfrac{\mathrm{d}^2\psi}{\mathrm{d}x^2} - V_0\psi = E\psi$ に $\psi = \alpha e^{ipx} + \beta e^{-ipx}$ を代入すると次式が成り立ちます。

$$
\frac{\hbar^2 p^2}{2m} - V_0 = \frac{\hbar^2 k^2}{2m}
$$

これを $p^2$ について解きます。

$$
p^2 = k^2 + \frac{2mV_0}{\hbar^2}
$$

$p > 0$ をとると，$p$ は次式となります。

$$
\finalanswer{p = \sqrt{k^2 + \frac{2mV_0}{\hbar^2}}}
$$

### (4)

まず $x = a/2$ における波動関数 $\psi$ とその導関数 $\psi'$ の連続条件を書きます。

$$
\begin{aligned}
\alpha e^{ipa/2} + \beta e^{-ipa/2} &= T e^{ika/2} \\
ip\bigl(\alpha e^{ipa/2} - \beta e^{-ipa/2}\bigr) &= ik T e^{ika/2}
\end{aligned}
$$

第2式を $ip$ で割って第1式と足し引きし，$\alpha$ と $\beta$ を $T$ で表します。

$$
\begin{aligned}
\alpha &= \frac{1}{2}\left(1 + \frac{k}{p}\right)T e^{i(k - p)a/2} \\
\beta &= \frac{1}{2}\left(1 - \frac{k}{p}\right)T e^{i(k + p)a/2}
\end{aligned}
$$

次に $x = -a/2$ における $\psi$ と $\psi'$ の連続条件を書きます。

$$
\begin{aligned}
e^{-ika/2} + R e^{ika/2} &= \alpha e^{-ipa/2} + \beta e^{ipa/2} \\
ik\bigl(e^{-ika/2} - R e^{ika/2}\bigr) &= ip\bigl(\alpha e^{-ipa/2} - \beta e^{ipa/2}\bigr)
\end{aligned}
$$

第2式を $ik$ で割って第1式に加え，$R$ を消します。

$$
2e^{-ika/2} = \alpha\left(1 + \frac{p}{k}\right)e^{-ipa/2} + \beta\left(1 - \frac{p}{k}\right)e^{ipa/2}
$$

ここに先ほど求めた $\alpha$ と $\beta$ を代入します。

$$
\begin{aligned}
2e^{-ika/2} &= \frac{1}{2}T e^{ika/2}\left\{\left(1 + \frac{k}{p}\right)\left(1 + \frac{p}{k}\right)e^{-ipa} + \left(1 - \frac{k}{p}\right)\left(1 - \frac{p}{k}\right)e^{ipa}\right\} \\
&= \frac{1}{2}T e^{ika/2}\left\{\left(2 + \frac{k}{p} + \frac{p}{k}\right)e^{-ipa} + \left(2 - \frac{k}{p} - \frac{p}{k}\right)e^{ipa}\right\} \\
&= \frac{1}{2}T e^{ika/2}\left\{2\bigl(e^{ipa} + e^{-ipa}\bigr) - \left(\frac{k}{p} + \frac{p}{k}\right)\bigl(e^{ipa} - e^{-ipa}\bigr)\right\} \\
&= \frac{1}{2}T e^{ika/2}\left\{4\cos(pa) - 2i\left(\frac{k}{p} + \frac{p}{k}\right)\sin(pa)\right\}
\end{aligned}
$$

両辺を $2$ で割って $T$ について解きます。

$$
T = \frac{e^{-ika}}{\cos(pa) - \dfrac{i}{2}\left(\dfrac{k}{p} + \dfrac{p}{k}\right)\sin(pa)}
$$

与えられた表式と比べると，$A$ と $B$ は次式となります。

$$
\finalanswer{A = 1, \qquad B = \frac{1}{2}\left(\frac{k}{p} + \frac{p}{k}\right) = \frac{k^2 + p^2}{2kp}}
$$

### (5)

設問4の結果から透過率 $|T|^2$ を計算します。$\cos^2(pa) = 1 - \sin^2(pa)$ を用います。

$$
\begin{aligned}
|T|^2 &= \frac{1}{\cos^2(pa) + B^2\sin^2(pa)} \\
&= \frac{1}{1 + (B^2 - 1)\sin^2(pa)}
\end{aligned}
$$

ここで $B^2 - 1$ を整理します。

$$
\begin{aligned}
B^2 - 1 &= \frac{(k^2 + p^2)^2}{4k^2 p^2} - 1 \\
&= \frac{(p^2 - k^2)^2}{4k^2 p^2}
\end{aligned}
$$

$V_0 > 0$ より $p^2 - k^2 = \dfrac{2mV_0}{\hbar^2} > 0$ なので $B^2 - 1 > 0$ です。したがって，完全透過すなわち $|T|^2 = 1$ が成り立つ条件は $\sin(pa) = 0$ です。$p > 0$ より，正の整数 $n$ を用いて $pa = n\pi$ となります。設問3より $p = \sqrt{k^2 + \dfrac{2mV_0}{\hbar^2}}$ を代入して $k$ の条件に書き換えます。

$$
k^2 + \frac{2mV_0}{\hbar^2} = \left(\frac{n\pi}{a}\right)^2
$$

移項して $k^2$ について整理します。

$$
k^2 = \left(\frac{n\pi}{a}\right)^2 - \frac{2mV_0}{\hbar^2}
$$

$k > 0$ となるためには $\dfrac{n\pi}{a} > \sqrt{\dfrac{2mV_0}{\hbar^2}}$，すなわち自然数 $n$ が $n > \dfrac{a}{\pi}\sqrt{\dfrac{2mV_0}{\hbar^2}}$ を満たす必要があります。よって求める条件は，この範囲の自然数 $n$ を用いて次式となります。

$$
\finalanswer{k = \sqrt{\left(\frac{n\pi}{a}\right)^2 - \frac{2mV_0}{\hbar^2}}}
$$

完全透過が起こる物理的理由は次の通りです。井戸内の波長を $\lambda_{\mathrm{in}} = \dfrac{2\pi}{p}$ とすると，条件 $pa = n\pi$ は $a = n\dfrac{\lambda_{\mathrm{in}}}{2}$ すなわち井戸の幅 $a$ が井戸内の半波長の整数倍になるときに対応します。このとき，井戸の左端 $x = -a/2$ で反射される波と，井戸内を往復して右端 $x = a/2$ で反射されて戻ってくる波との位相差が $\pi$ の奇数倍となり，反射波同士が互いに打ち消し合うため，反射が消えて完全透過が起こります。

### (6)

設問5で得た透過率は，次式で表されます。

$$
|T|^2 = \frac{1}{1 + \dfrac{(p^2 - k^2)^2}{4k^2 p^2}\sin^2(pa)}
$$

$p^2 - k^2 = \dfrac{2mV_0}{\hbar^2}$ は一定なので，$k \to 0$ では一般に $\sin(a\sqrt{2mV_0}/\hbar) \neq 0$ のとき分母が発散して $|T|^2 \to 0$ となります。$k$ が増加すると，設問5の共鳴波数 $k_1, k_2, k_3, \dots$ で $|T|^2 = 1$ に達しながら振動します。また $k \to \infty$ では $\dfrac{(p^2 - k^2)^2}{4k^2 p^2} \propto \dfrac{1}{k^4} \to 0$ となるため，谷の深さは次第に浅くなり $|T|^2$ は $1$ に漸近します。概形は次の図のようになります。

<figure class="problem-figure" markdown>
![透過率の波数依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H17_butsuri_1-s-light.svg#only-light)
![透過率の波数依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H17_butsuri_1-s-dark.svg#only-dark)
<figcaption markdown="span">透過率 $|T|^2$ の波数 $k$ 依存性（$k_1, k_2, k_3$ は完全透過の共鳴波数）。</figcaption>
</figure>
