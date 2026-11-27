---
title: 東大理物 平成12年度 一般教育科目 物理学 第2問：直線導線内の電流によるローレンツ力と電荷密度の変化
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 一般教育科目 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成12年度 一般教育科目 物理学 第2問：直線導線内の電流によるローレンツ力と電荷密度の変化

## 問題

半径 $a$ の円形断面を持つ無限に長い直線導線がある。電流が流れていないとき，導線内の電荷分布は一様で，正電荷密度は $\rho_+ = \rho_0$，伝導電子による負電荷密度は $-\rho_- = -\rho_0$ であるが，電流を流すと，負電荷密度 $-\rho_-$ には $-\rho_0$ からのずれが生じる。これに関連した次の各設問に答えよ。導線の内外で誘電率および透磁率は，それぞれ真空での値 $\varepsilon_0, \mu_0$ を用いてよい。
{: .problem-lead }

(1) 外部電場が加わると電子は平均の移動速度（ドリフト速度）で流れる。この結果生ずる一様で定常な電流密度 $j$ を電子の電荷密度 $-\rho_-$ と電子のドリフト速度 $v$（$> 0$）で表せ。

(2) この電流が導線の内外につくる磁場（磁束密度 $B$）を，導線の中心からの距離 $r$ の関数として求め，その向きを図示せよ。

(3) この磁場が導線内の一個の伝導電子に作用するローレンツ力の大きさを，電子のドリフト速度 $v$ と磁場の大きさで表し，その向きを図示せよ。

(4) 伝導電子は，設問 (3) で求めた磁場からのローレンツ力を受けているにもかかわらず定常的に運動している。それは磁場のローレンツ力をうち消す電場がつくられているからである。この電場を求め，その向きを図示せよ。

(5) これまでの結果をもとに，電流が流れると電荷分布がどう変化するかを簡潔に説明せよ。

(6) 実際に変化した電荷分布を求めよ。ただし，正電荷密度を $\rho_+$，負電荷密度を $-\rho_-$ とおき，各電荷密度を $\rho_0$ と $v$ で表し，電流が流れていない場合からの変化を求めよ。

(7) 断面積 $1\,\mathrm{mm^2}$ の銅線に $1\,\mathrm{A}$ の電流が流れるときの電子のドリフト速度を計算し，上で求めた電荷密度の変化の割合を評価せよ。ただし，銅の質量密度は $9 \times 10^3\,\mathrm{kg\cdot m^{-3}}$，原子量は $63.55$ であり，原子1個あたり自由電子が1個あるとする。また，素電荷は $1.6 \times 10^{-19}\,\mathrm{C}$，アヴォガドロ定数は $6 \times 10^{23}\,\mathrm{mol^{-1}}$，真空の光速度は $3 \times 10^8\,\mathrm{m\cdot s^{-1}}$ とする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 一般教育科目 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
円筒対称な定常電流がつくる磁場はアンペールの法則で導線の内外に分けて求まり，その磁場中をドリフトする電子には導線の中心軸へ向かうローレンツ力が働きます。

電子が軸方向に定常運動を保つには，この中心向きの磁気力と釣り合う外向きの静電気力が必要であり，負電荷の電子に対して外向きの力を及ぼす電場は中心軸向きになります。この動径方向電場へガウスの法則を用いると，導線内部の正味電荷密度が $v^2/c^2$ に比例して負に偏ることが求まります。
</div>

円筒座標 $(r, \phi, z)$ をとり，導線の中心軸を $z$ 軸，電流の向きを $+z$ 方向とします。伝導電子は負の電荷をもつため，電子のドリフト速度ベクトルは $-z$ 方向の $\mathbf{v} = -v\hat{\mathbf{z}}$（$v > 0$）です。

### (1)

単位体積当たりの電子の電荷は $-\rho_-$，電子の速度は $\mathbf{v} = -v\hat{\mathbf{z}}$ なので，電流密度ベクトル $\mathbf{j}$ は次の通りです。

$$
\begin{aligned}
\mathbf{j} &= (-\rho_-)\mathbf{v} \\
&= (-\rho_-)(-v\hat{\mathbf{z}}) \\
&= \rho_- v\hat{\mathbf{z}}
\end{aligned}
$$

したがって，電流の向きを正とした電流密度 $j$ は次の通りです。なお，電子のドリフトの向きを正にとる場合は $j = -\rho_- v$ となり，電流は電子のドリフトと逆向きに流れます。

$$
\finalanswer{j = \rho_- v}
$$

### (2)

導線は無限に長く軸対称なので，磁束密度 $\mathbf{B}$ は $z$ 軸を中心とする同心円の接線方向，すなわち電流の向きに対して右ねじの向きである $+\hat{\boldsymbol{\phi}}$ 方向を向き，大きさ $B(r)$ は中心からの距離 $r$ のみに依存します。半径 $r$ の円周 $C$ に沿ってアンペールの法則 $\oint_C \mathbf{B}\cdot\mathrm{d}\mathbf{l} = \mu_0 I_{\mathrm{enc}}$ を用います。

導線の内部（$r \le a$）では，円 $C$ の内側を貫く電流は $I_{\mathrm{enc}} = \pi r^2 j$ であり，$j = \rho_- v$ を代入すると $\pi r^2 \rho_- v$ です。

$$
\begin{aligned}
2\pi r B(r) &= \mu_0 \pi r^2 \rho_- v \\
B(r) &= \frac{\mu_0 \rho_- v}{2}r
\end{aligned}
$$

導線の外部（$r > a$）では，円 $C$ の内側を貫く電流は全電流 $I_{\mathrm{enc}} = \pi a^2 j$ であり，$\pi a^2 \rho_- v$ です。

$$
\begin{aligned}
2\pi r B(r) &= \mu_0 \pi a^2 \rho_- v \\
B(r) &= \frac{\mu_0 \rho_- v a^2}{2r}
\end{aligned}
$$

したがって，磁束密度 $B(r)$ は次の通りです。向きは電流に対して右ねじの向きであり，(3)，(4) の向きと合わせて下の図に示します。

$$
\finalanswer{B(r) = \begin{cases} \dfrac{\mu_0 \rho_- v}{2}r & (r \le a) \\[1.5ex] \dfrac{\mu_0 \rho_- v a^2}{2r} & (r > a) \end{cases}}
$$

<figure class="problem-figure" markdown>
![導線内の電流，電子のドリフト速度，磁場，ローレンツ力，および電場の向き](../../assets/figures/pastexam-todai-ributsu/H12_ippan_butsuri_2-s-light.svg#only-light){ loading=lazy }
![導線内の電流，電子のドリフト速度，磁場，ローレンツ力，および電場の向き](../../assets/figures/pastexam-todai-ributsu/H12_ippan_butsuri_2-s-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">導線の側面図（左）と断面図（右：電流 $\mathbf{j}$ は紙面の奥から手前向き，電子のドリフト速度 $\mathbf{v}$ は手前から奥向き）。磁場 $\mathbf{B}$ は反時計回り，ローレンツ力 $\mathbf{F}_B$ と釣り合いの電場 $\mathbf{E}$ はともに中心軸向き，静電気力 $-e\mathbf{E}$ は外向きになる。</figcaption>
</figure>

### (3)

電荷 $-e$ をもち速度 $\mathbf{v} = -v\hat{\mathbf{z}}$ で動く1個の伝導電子が磁場 $\mathbf{B} = B(r)\hat{\boldsymbol{\phi}}$ から受けるローレンツ力 $\mathbf{F}_B$ を計算します。円筒座標の基底は $\hat{\mathbf{z}} \times \hat{\boldsymbol{\phi}} = -\hat{\mathbf{r}}$ を満たします。

$$
\begin{aligned}
\mathbf{F}_B &= (-e)\mathbf{v} \times \mathbf{B} \\
&= (-e)(-v\hat{\mathbf{z}}) \times \bigl(B(r)\hat{\boldsymbol{\phi}}\bigr) \\
&= e v B(r)(\hat{\mathbf{z}} \times \hat{\boldsymbol{\phi}}) \\
&= -e v B(r)\hat{\mathbf{r}}
\end{aligned}
$$

したがって，ローレンツ力の大きさは $F_B = evB$ であり，$r \le a$ では $F_B = \dfrac{1}{2}\mu_0 e \rho_- v^2 r$ となります。向きは導線の中心軸に向かう動径内向き，すなわち $-\hat{\mathbf{r}}$ 方向であり，(2) の図に示しています。

$$
\finalanswer{F_B = evB, \qquad \mathbf{F}_B = -evB(r)\hat{\mathbf{r}}}
$$

### (4)

伝導電子が動径方向に加速されずに定常運動を続けるためには，電場 $\mathbf{E}$ による静電気力 $(-e)\mathbf{E}$ がローレンツ力 $\mathbf{F}_B$ を打ち消す必要があります。

$$
\begin{aligned}
(-e)\mathbf{E} + \mathbf{F}_B &= \mathbf{0} \\
(-e)\mathbf{E} - e v B(r)\hat{\mathbf{r}} &= \mathbf{0}
\end{aligned}
$$

これを $\mathbf{E}$ について解くと $\mathbf{E} = -v B(r)\hat{\mathbf{r}}$ です。導線内部（$r \le a$）の $B(r) = \dfrac{\mu_0 \rho_- v}{2}r$ を代入します。

$$
\begin{aligned}
\mathbf{E}(r) &= -v\cdot\frac{\mu_0 \rho_- v}{2}r\,\hat{\mathbf{r}} \\
&= -\frac{\mu_0 \rho_- v^2}{2}r\,\hat{\mathbf{r}}
\end{aligned}
$$

静電気力 $-e\mathbf{E}$ が動径外向きになるため，負電荷の電子に対する電場 $\mathbf{E}$ の向きは導線の中心軸に向かう動径内向き，すなわち $-\hat{\mathbf{r}}$ 方向です。向きは (2) の図に示しています。

$$
\finalanswer{\mathbf{E}(r) = -\frac{\mu_0 \rho_- v^2}{2}r\,\hat{\mathbf{r}} \qquad (r \le a)}
$$

### (5)

導線内部の伝導電子は，電流自身がつくる磁場から中心軸へ向かうローレンツ力を受けて内側に引き寄せられます。その結果，導線の内部では動かない陽イオン格子による正電荷密度に比べて負電荷密度の大きさ $\rho_-$ がわずかに大きくなり，導線内部は正味として負に帯電します。この内部の余剰な負電荷が中心軸向きの動径電場 $\mathbf{E}$ をつくり，電子に対する外向きの静電気力が内向きのローレンツ力と釣り合った状態で定常になります。同時に，導線全体が電気的に中性であれば，電子が内側に引き寄せられた分だけ導線の外表面（$r = a$）に正の表面電荷が現れます。

### (6)

結晶格子をつくる陽イオンは動かないため，正電荷密度は電流の有無によらず $\rho_+ = \rho_0$ のままで変化は $0$ です。

導線内部（$r < a$）の半径 $r$，長さ $\ell$ の同軸円筒にガウスの法則を当てはめます。側面の外向き法線ベクトルは $+\hat{\mathbf{r}}$ であり，$\mathbf{E} = -E(r)\hat{\mathbf{r}}$ は内向きなので，表面を貫く電束は次の通りです。

$$
\begin{aligned}
\oint \mathbf{E}\cdot\mathrm{d}\mathbf{S} &= -E(r) \cdot 2\pi r\ell \\
&= -\frac{\mu_0 \rho_- v^2}{2}r \cdot 2\pi r\ell \\
&= -\pi r^2 \ell \mu_0 \rho_- v^2
\end{aligned}
$$

円筒内部の正味電荷は $(\rho_+ - \rho_-)\pi r^2 \ell$ なので，ガウスの法則から次が成り立ちます。

$$
\begin{aligned}
-\pi r^2 \ell \mu_0 \rho_- v^2 &= \frac{(\rho_+ - \rho_-)\pi r^2 \ell}{\varepsilon_0} \\
\rho_+ - \rho_- &= -\varepsilon_0\mu_0 v^2 \rho_-
\end{aligned}
$$

真空の光速 $c = \dfrac{1}{\sqrt{\varepsilon_0\mu_0}}$ より $\varepsilon_0\mu_0 = \dfrac{1}{c^2}$ です。また $\rho_+ = \rho_0$ を代入して移項します。

$$
\begin{aligned}
\rho_0 - \rho_- &= -\frac{v^2}{c^2}\rho_- \\
\rho_-\left(1 - \frac{v^2}{c^2}\right) &= \rho_0
\end{aligned}
$$

両辺を $1 - \dfrac{v^2}{c^2}$ で割ると次になります。

$$
\rho_- = \frac{\rho_0}{1 - v^2/c^2}
$$

よって負電荷密度は $-\rho_- = -\dfrac{\rho_0}{1 - v^2/c^2}$ であり，電流が流れていない場合（$-\rho_0$）からの変化 $\Delta(-\rho_-) = -\rho_- - (-\rho_0)$ を計算します。

$$
\begin{aligned}
\Delta(-\rho_-) &= -\frac{\rho_0}{1 - v^2/c^2} + \rho_0 \\
&= -\frac{v^2/c^2}{1 - v^2/c^2}\rho_0
\end{aligned}
$$

したがって，各電荷密度および電流が流れていない場合からの変化は次の通りです。

$$
\finalanswer{\rho_+ = \rho_0 \quad (\Delta\rho_+ = 0), \qquad -\rho_- = -\frac{\rho_0}{1 - v^2/c^2} \quad \left(\Delta(-\rho_-) = -\frac{v^2/c^2}{1 - v^2/c^2}\rho_0 \approx -\frac{v^2}{c^2}\rho_0\right)}
$$

### (7)

まず銅の単位体積当たりの自由電子数 $n$ を求めます。銅の質量密度は $d = 9 \times 10^3\,\mathrm{kg\cdot m^{-3}}$，モル質量は $M = 63.55 \times 10^{-3}\,\mathrm{kg\cdot mol^{-1}}$，アヴォガドロ定数は $N_{\mathrm{A}} = 6 \times 10^{23}\,\mathrm{mol^{-1}}$ であり，原子1個当たり自由電子が1個あります。

$$
\begin{aligned}
n &= \frac{d N_{\mathrm{A}}}{M} \\
&= \frac{9 \times 10^3 \times 6 \times 10^{23}}{63.55 \times 10^{-3}} \\
&\approx 8.50 \times 10^{28}\,\mathrm{m^{-3}}
\end{aligned}
$$

断面積 $S = 1\,\mathrm{mm^2} = 1 \times 10^{-6}\,\mathrm{m^2}$，電流 $I = 1\,\mathrm{A}$，素電荷 $e = 1.6 \times 10^{-19}\,\mathrm{C}$ より，関係 $I = n e v S$ から電子のドリフト速度 $v$ を計算します。

$$
\begin{aligned}
v &= \frac{I}{n e S} \\
&= \frac{1}{8.50 \times 10^{28} \times 1.6 \times 10^{-19} \times 1 \times 10^{-6}} \\
&= \frac{1}{1.36 \times 10^4} \\
&\approx 7.36 \times 10^{-5}\,\mathrm{m/s}
\end{aligned}
$$

次に電荷密度の変化の割合 $\dfrac{\rho_- - \rho_0}{\rho_0} = \dfrac{v^2/c^2}{1 - v^2/c^2} \approx \dfrac{v^2}{c^2}$ を，$c = 3 \times 10^8\,\mathrm{m/s}$ を用いて計算します。

$$
\begin{aligned}
\frac{v^2}{c^2} &= \left(\frac{7.36 \times 10^{-5}}{3 \times 10^8}\right)^2 \\
&= \left(2.45 \times 10^{-13}\right)^2 \\
&\approx 6.0 \times 10^{-26}
\end{aligned}
$$

したがって，電子のドリフト速度と電荷密度の変化の割合は次の通りです。

$$
\finalanswer{v \approx 7.4 \times 10^{-5}\,\mathrm{m\cdot s^{-1}}, \qquad \frac{\rho_- - \rho_0}{\rho_0} \approx 6.0 \times 10^{-26}}
$$

<aside class="rigor-note" markdown>
(5) と (6) で生じた導線内部の余剰負電荷は，単位長さ当たり $\pi a^2(\rho_0 - \rho_-) = -\pi a^2\dfrac{v^2/c^2}{1 - v^2/c^2}\rho_0$ です。導線全体が電気的に中性を保つとき，外表面 $r = a$ に面電荷密度 $\sigma_s = \dfrac{a}{2}\dfrac{v^2/c^2}{1 - v^2/c^2}\rho_0$ の正電荷が現れ，その結果 $r > a$ の外部空間の動径電場は $0$ になります。また (7) の通り通常の銅線では $v/c \sim 10^{-13}$ と小さいため，電荷密度の変化の割合は $10^{-26}$ の桁にとどまります。
</aside>
