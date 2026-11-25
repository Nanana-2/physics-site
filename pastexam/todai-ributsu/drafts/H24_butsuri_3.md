---
title: 東大理物 平成24年度 物理学 第3問：誘電体による光の分散と異常分散
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成24年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成24年度 物理学 第3問：誘電体による光の分散と異常分散

## 問題

誘電体による光の分散の性質を考察するために，誘電体を構成する原子に束縛された電子を考える。電子には，変位に比例する復元力が働くものとする。いま，誘電体の外部から入射する光の電場を $\boldsymbol{E} = \boldsymbol{E}_0 \cos\omega t$ と表す。電子の質量を $m$，電荷を $e$（$< 0$）とし，束縛電子の単振動の固有角振動数を $\omega_0$ とする。また，電子の位置（変位）を $\boldsymbol{r}$，速度を $\boldsymbol{v}$ と書く。以下の設問に答えよ。

(1) 電子の運動方程式を書き下せ。ただし，電子の自己力と磁場による Lorentz 力は無視してよい。

(2) 設問 1 で求めた運動方程式の解が $\boldsymbol{r} = \boldsymbol{R}\cos\omega t$ で与えられるとし，振幅 $\boldsymbol{R}$ を決めた上で束縛電子による電流密度 $\boldsymbol{i}_{\mathrm{d}} = N e \boldsymbol{v}$ の表式を求めよ。ただし，$N$ は単位体積あたりの電子数である。

(3) 真空中の透磁率を $\mu_0$，誘電率を $\varepsilon_0$ とし，磁束密度を $\boldsymbol{B}$ と書くとき，Ampère-Maxwell の法則を表す真空中の Maxwell 方程式は次式で与えられる。

$$
\frac{1}{\mu_0}\operatorname{rot}\boldsymbol{B} = \varepsilon_0 \frac{\partial\boldsymbol{E}}{\partial t} + \boldsymbol{i} \tag{1}
$$

式 (1) が電荷保存則と矛盾しないことを示せ。

(4) Ampère-Maxwell の法則を表す方程式 (1) は，電場 $\boldsymbol{E} = \boldsymbol{E}_0 \cos\omega t$，電流密度 $\boldsymbol{i} = \boldsymbol{0}$ の場合には，

$$
\operatorname{rot}\boldsymbol{B} = -C\omega \boldsymbol{E}_0 \sin\omega t \tag{2}
$$

の形に書ける。真空中では式 (2) 中の係数は $C = \varepsilon_0 \mu_0$ となる。一方，誘電体中では光の電場 $\boldsymbol{E} = \boldsymbol{E}_0 \cos\omega t$ に対する束縛電子の応答の効果として電流密度 $\boldsymbol{i}_{\mathrm{d}}$ が存在し，式 (1) 中の電流密度 $\boldsymbol{i}$ に寄与する。このとき，Ampère-Maxwell の法則を表す方程式を式 (2) と同じ形で表し，係数 $C$ の具体的な表式を求めよ。

(5) 設問 4 で求めた係数 $C$ は，誘電体の誘電率 $\varepsilon$ と透磁率 $\mu$ の積に対応する。このことに注意して，光の角振動数 $\omega$ の関数である誘電体の屈折率 $n(\omega) = \sqrt{\dfrac{\varepsilon\mu}{\varepsilon_0 \mu_0}}$ の表式を $\omega_0$ とプラズマ特性振動数 $\omega_{\mathrm{p}} = \sqrt{\dfrac{N e^2}{m \varepsilon_0}}$ を用いて表せ。得られた表式は分散関係式と呼ばれる。

(6) 太陽光を石英製のプリズム（可視光領域で $n(\omega) > 1$）を通して分光すると，そのスペクトルは光の振動数の順に，紫，藍，青，緑，黄，橙，赤のように並ぶことはよく知られている。一方，ある特殊な物質 F（注）でできたプリズムを通して分光したところ，そのスペクトルは振動数の順にならずに黄，橙，赤，紫，藍，青の順になった。答案用紙に次頁の図を書き写し，石英の分散曲線と物質 F の分散曲線の概略を，それぞれの場合の固有角振動数 $\omega_0$ の位置が分かるように描け。

（注）物質 F は，フクシンという染料の一種をエタノールに溶かしたもの。
{: .problem-lead }

<figure class="problem-figure" markdown>
![石英の分散曲線と物質Fの分散曲線の枠図](../../../docs/assets/figures/pastexam-todai-ributsu/H24_butsuri_3-p-light.svg#only-light)
![石英の分散曲線と物質Fの分散曲線の枠図](../../../docs/assets/figures/pastexam-todai-ributsu/H24_butsuri_3-p-dark.svg#only-dark)
<figcaption markdown="span">図 1（左）：石英の分散曲線，図 2（右）：物質 F の分散曲線。網掛け領域（$\omega_{\mathrm{R}}$ から $\omega_{\mathrm{V}}$）が赤・橙・黄・緑・青・藍・紫の可視光領域を表す。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成24年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
物質の中の電子を，復元力 $-m\omega_0^2 \boldsymbol{r}$ を受ける調和振動子として扱います。光の電場で揺すられた電子の変位から電流密度を求め，マクスウェル方程式に入れると，電子の運動は誘電率を変える効果として表されます。

この誘電率から求めた屈折率 $n(\omega)$ は，$\omega$ が $\omega_0$ をまたぐと振る舞いが変わります。そこで，$\omega_0$ が可視光より高い場合と，可視光の範囲にある場合に分けて，プリズムで曲がる角度の大小を色ごとに比べます。
</div>

### (1)
固有角振動数 $\omega_0$ の単振動の復元力は $-m\omega_0^2 \boldsymbol{r}$ であり，電場から受ける力は $e\boldsymbol{E} = e\boldsymbol{E}_0 \cos\omega t$ です。電子の運動方程式は次のとおりです。

$$
\finalanswer{m\frac{\mathrm{d}^2\boldsymbol{r}}{\mathrm{d}t^2} = -m\omega_0^2 \boldsymbol{r} + e\boldsymbol{E}_0 \cos\omega t}
$$

### (2)
$\boldsymbol{r} = \boldsymbol{R}\cos\omega t$ を設問1の運動方程式に代入します。$\dfrac{\mathrm{d}^2\boldsymbol{r}}{\mathrm{d}t^2} = -\omega^2 \boldsymbol{R}\cos\omega t$ なので，次式が得られます。

$$
\begin{aligned}
-m\omega^2 \boldsymbol{R}\cos\omega t &= -m\omega_0^2 \boldsymbol{R}\cos\omega t + e\boldsymbol{E}_0 \cos\omega t \\
m(\omega_0^2 - \omega^2)\boldsymbol{R} &= e\boldsymbol{E}_0 \\
\boldsymbol{R} &= \frac{e}{m(\omega_0^2 - \omega^2)}\boldsymbol{E}_0
\end{aligned}
$$

速度は $\boldsymbol{v} = \dfrac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} = -\omega\boldsymbol{R}\sin\omega t$ です。これを用いて電流密度 $\boldsymbol{i}_{\mathrm{d}} = N e \boldsymbol{v}$ を求めます。

$$
\begin{aligned}
\boldsymbol{i}_{\mathrm{d}} &= N e (-\omega\boldsymbol{R}\sin\omega t) \\
&= -\frac{N e^2 \omega}{m(\omega_0^2 - \omega^2)}\boldsymbol{E}_0 \sin\omega t
\end{aligned}
$$

$$
\finalanswer{\boldsymbol{R} = \frac{e}{m(\omega_0^2 - \omega^2)}\boldsymbol{E}_0, \qquad \boldsymbol{i}_{\mathrm{d}} = -\frac{N e^2 \omega}{m(\omega_0^2 - \omega^2)}\boldsymbol{E}_0 \sin\omega t}
$$

### (3)
式 (1) の両辺の発散をとります。任意のベクトル場 $\boldsymbol{B}$ に対して $\operatorname{div}(\operatorname{rot}\boldsymbol{B}) = 0$ が成り立ちます。

$$
\begin{aligned}
0 &= \frac{1}{\mu_0}\operatorname{div}(\operatorname{rot}\boldsymbol{B}) \\
&= \varepsilon_0 \frac{\partial}{\partial t}(\operatorname{div}\boldsymbol{E}) + \operatorname{div}\boldsymbol{i}
\end{aligned}
$$

真空中のガウスの法則 $\operatorname{div}\boldsymbol{E} = \dfrac{\rho}{\varepsilon_0}$ を代入します。ここで $\rho$ は電荷密度です。

$$
\begin{aligned}
0 &= \varepsilon_0 \frac{\partial}{\partial t}\left(\frac{\rho}{\varepsilon_0}\right) + \operatorname{div}\boldsymbol{i} \\
\frac{\partial\rho}{\partial t} + \operatorname{div}\boldsymbol{i} &= 0
\end{aligned}
$$

これは電荷保存則そのものであり，式 (1) は電荷保存則と矛盾しません。

### (4)
式 (1) に $\boldsymbol{E} = \boldsymbol{E}_0 \cos\omega t$ と設問2の $\boldsymbol{i} = \boldsymbol{i}_{\mathrm{d}}$ を代入し，両辺に $\mu_0$ を掛けます。

$$
\begin{aligned}
\frac{1}{\mu_0}\operatorname{rot}\boldsymbol{B} &= \varepsilon_0 (-\omega\boldsymbol{E}_0 \sin\omega t) - \frac{N e^2 \omega}{m(\omega_0^2 - \omega^2)}\boldsymbol{E}_0 \sin\omega t \\
\operatorname{rot}\boldsymbol{B} &= -\mu_0\left(\varepsilon_0 + \frac{N e^2}{m(\omega_0^2 - \omega^2)}\right)\omega\boldsymbol{E}_0 \sin\omega t
\end{aligned}
$$

これを式 (2) と比較すると，係数 $C$ は次のとおりです。

$$
\finalanswer{\operatorname{rot}\boldsymbol{B} = -C\omega\boldsymbol{E}_0 \sin\omega t, \qquad C = \varepsilon_0 \mu_0\left(1 + \frac{N e^2}{m\varepsilon_0(\omega_0^2 - \omega^2)}\right)}
$$

### (5)
設問4で求めた $C = \varepsilon\mu$ を $\varepsilon_0 \mu_0$ で割り，$\omega_{\mathrm{p}}^2 = \dfrac{N e^2}{m\varepsilon_0}$ を代入します。

$$
\begin{aligned}
n^2(\omega) &= \frac{\varepsilon\mu}{\varepsilon_0 \mu_0} \\
&= \frac{C}{\varepsilon_0 \mu_0} \\
&= 1 + \frac{N e^2}{m\varepsilon_0(\omega_0^2 - \omega^2)} \\
&= 1 + \frac{\omega_{\mathrm{p}}^2}{\omega_0^2 - \omega^2}
\end{aligned}
$$

平方根をとると屈折率 $n(\omega)$ が得られます。

$$
\finalanswer{n(\omega) = \sqrt{1 + \frac{\omega_{\mathrm{p}}^2}{\omega_0^2 - \omega^2}}}
$$

### (6)
プリズムによる光の屈折角は屈折率 $n(\omega)$ が大きいほど大きくなります。

- 石英：可視光領域で $n(\omega) > 1$ であり，振動数が高い紫から低い赤の順に並んでいるので，可視光領域全体で $n(\omega)$ は $\omega$ とともに単調増加しています。式 $n^2(\omega) = 1 + \dfrac{\omega_{\mathrm{p}}^2}{\omega_0^2 - \omega^2}$ がこの振る舞いを示すのは，$\omega_0$ が可視光領域より高い紫外領域にあるときです。
- 物質 F：緑の光が吸収されて見えず，屈折角が大きい順に黄，橙，赤，紫，藍，青と並んでいます。$\omega_0$ が可視光領域内の緑の位置にあると，$\omega < \omega_0$ の側では $n^2(\omega) > 1$ かつ $\omega$ が $\omega_0$ に近づくほど $n(\omega)$ が大きくなるため黄 $>$ 橙 $>$ 赤 $> 1$ となります。一方，$\omega > \omega_0$ の側では $n^2(\omega) < 1$ かつ $\omega$ が大きいほど $n^2(\omega)$ が $1$ に近づくため $1 >$ 紫 $>$ 藍 $>$ 青となります。したがって全体の屈折率の大きさは黄 $>$ 橙 $>$ 赤 $>$ 紫 $>$ 藍 $>$ 青の順になり，観測結果と一致します。

以上より，石英と物質 F の分散曲線の概略は次の図のようになります。

<figure class="problem-figure" markdown>
![石英と物質Fの分散曲線の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H24_butsuri_3-s-light.svg#only-light)
![石英と物質Fの分散曲線の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H24_butsuri_3-s-dark.svg#only-dark)
<figcaption markdown="span">左は石英の分散曲線で $\omega_0$ が可視光領域より高い側にあり，右は物質 F の分散曲線で $\omega_0$ が可視光領域内の緑の位置にある。</figcaption>
</figure>

<aside class="rigor-note" markdown>
実際の物質では電子の運動に減衰項が働くため，$\omega = \omega_0$ で $n^2(\omega)$ は無限大に発散せず有限の極大・極小を経て連続的に変化します。このとき $\omega \approx \omega_0$ で光の吸収が強く起きるため，物質 F のスペクトルでは緑の光が欠けて観測されます。
</aside>
