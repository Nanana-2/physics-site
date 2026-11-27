---
title: 東大理物 平成13年度 物理学 第3問：遅延ポテンシャルと加速点粒子の電磁波放射
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成13年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成13年度 物理学 第3問：遅延ポテンシャルと加速点粒子の電磁波放射

## 問題

時間・空間座標に依存する電荷分布 $\rho(\mathbf{r}', t')$ と電流分布 $\mathbf{j}(\mathbf{r}', t')$ がある。これらによって誘起される電磁ポテンシャルは，ローレンツ条件のもとで，次のように表せる。（以下，MKSA有理単位系を用いる。）

$$
\phi(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0} \int \frac{\rho(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|}\,\mathrm{d}^3 r', \qquad \mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{j}(\mathbf{r}', t')}{|\mathbf{r} - \mathbf{r}'|}\,\mathrm{d}^3 r'. \tag{1}
$$

$\varepsilon_0$ と $\mu_0$ は，それぞれ真空の誘電率と透磁率で，光速は $c = 1/\sqrt{\varepsilon_0\mu_0}$ と書ける。また，$t'$ は，$t, \mathbf{r}, \mathbf{r}', c$ で決まる量であり，次の設問で考察する。
{: .problem-lead }

(1) 電磁波が伝わる時の遅延効果を考慮して，(1) 式の $t'$ を決定せよ。

(2) 電荷 $e$ を持つ点粒子の運動を考え，その位置座標を $\mathbf{x}(t')$ とする。このとき，$\rho(\mathbf{r}', t')$ と $\mathbf{j}(\mathbf{r}', t')$ をディラックのデルタ関数を用いて表せ。

(3) この点粒子がつくる遠方（$|\mathbf{r}| = r \gg |\mathbf{x}|$）での電磁ポテンシャルは，点粒子の速度 $\mathbf{v}$ が光速に比べて十分小さい場合には，(1) 式の $1/|\mathbf{r} - \mathbf{r}'|$ を $1/r$ で近似して求める事ができる。この電磁ポテンシャルが，$v/c$ の一次までの近似で，以下のように表せる事を示せ。

$$
\phi(\mathbf{r}, t) = \frac{e}{4\pi\varepsilon_0 r}\left(1 + \frac{\hat{\mathbf{r}}\cdot\mathbf{v}(t_0)}{c}\right), \qquad c\mathbf{A}(\mathbf{r}, t) = \frac{e}{4\pi\varepsilon_0 r}\frac{\mathbf{v}(t_0)}{c}. \tag{2}
$$

ただし，$\hat{\mathbf{r}} = \mathbf{r}/r$，$t_0 = t - r/c$ である。

(4) 前問の結果から，電場 $\mathbf{E}(\mathbf{r}, t) = -\nabla\phi - \partial\mathbf{A}/\partial t$ と磁束密度 $\mathbf{B}(\mathbf{r}, t) = \nabla \times \mathbf{A}$ の遠方での主要項（$1/r$ に比例する項）が，点粒子の加速度 $\mathbf{a}$ を用いて以下のように表せる事を示せ。

$$
\mathbf{E}(\mathbf{r}, t) = \frac{e}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf{r}} \times \bigl(\hat{\mathbf{r}} \times \mathbf{a}(t_0)\bigr), \qquad c\mathbf{B}(\mathbf{r}, t) = -\frac{e}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf{r}} \times \mathbf{a}(t_0). \tag{3}
$$

ここで，ベクトル積の公式 $\mathbf{X} \times (\mathbf{Y} \times \mathbf{Z}) = \mathbf{Y}(\mathbf{X}\cdot\mathbf{Z}) - \mathbf{Z}(\mathbf{X}\cdot\mathbf{Y})$ を使ってよい。

(5) (3) 式を用いて以下の設問に答えよ。

(a) 点粒子が，図1のように，一定の振幅 $b$ と一定の振動数で $x$ 軸上を単振動しているとする。このとき，原点から距離 $r$ だけ離れた球面上（$r \gg b$ とする）で，点粒子の運動の一周期あたりに，電磁波の強度が最大となる場所はどこか？ 理由を付けて答えよ。

(b) 点粒子が，図2のように，一定の半径 $b$ と一定の角振動数で $xy$ 平面上を回転運動しているとする。このとき，原点から距離 $r$ だけ離れた球面上（$r \gg b$ とする）で，点粒子の運動の一周期あたりに，電磁波の強度が最大となる場所はどこか？ 理由を付けて答えよ。

<figure class="problem-figure" markdown>
![x軸上の単振動](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_3-p1-light.svg#only-light){ loading=lazy }
![x軸上の単振動](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_3-p1-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">図1：$x$ 軸上を振幅 $b$ で単振動する点粒子。</figcaption>
</figure>

<figure class="problem-figure" markdown>
![xy平面上の円運動](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_3-p2-light.svg#only-light){ loading=lazy }
![xy平面上の円運動](../../assets/figures/pastexam-todai-ributsu/H13_butsuri_3-p2-dark.svg#only-dark){ loading=lazy }
<figcaption markdown="span">図2：$xy$ 平面上を半径 $b$ で円運動する点粒子。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成13年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
点 $\mathbf{r}'$ から観測点 $\mathbf{r}$ まで電磁波が光速 $c$ で伝わる時間遅れ $|\mathbf{r} - \mathbf{r}'|/c$ を遅延時刻 $t'$ に取り込み，遠方条件 $r \gg |\mathbf{x}|$ のもとで $t'$ を $t_0 = t - r/c$ の周りに展開することで，スカラーポテンシャルの $v/c$ の1次項とベクトルポテンシャルの主要項を導きます。

遠方で空間微分 $\nabla$ を行うと，$1/r$ や $\hat{\mathbf{r}}$ の微分は $1/r^2$ の高次項になるため，$t_0 = t - r/c$ を通じた微分 $\nabla t_0 = -\hat{\mathbf{r}}/c$ だけを残せば放射場が得られます。電磁波のエネルギー流束はポインティングベクトル $\mathbf{S} = (\mathbf{E} \times \mathbf{B})/\mu_0$ の大きさで与えられるため，単振動と円運動の加速度ベクトルを代入して1周期平均の角度依存性を調べます。
</div>

### (1)

位置 $\mathbf{r}'$ にある電荷や電流の変化が光速 $c$ で観測点 $\mathbf{r}$ に到達するまでには，時間 $\dfrac{|\mathbf{r} - \mathbf{r}'|}{c}$ がかかります。したがって，時刻 $t$ に観測点 $\mathbf{r}$ へ寄与する波源の時刻 $t'$ は，この伝搬時間だけさかのぼった遅延時刻となります。

$$
\finalanswer{t' = t - \frac{|\mathbf{r} - \mathbf{r}'|}{c}}
$$

### (2)

時刻 $t'$ に位置 $\mathbf{x}(t')$ にあり，速度 $\mathbf{v}(t') = \dfrac{\mathrm{d}\mathbf{x}(t')}{\mathrm{d}t'}$ で運動する電荷 $e$ の点粒子の電荷密度と電流密度は，3次元のディラックのデルタ関数 $\delta(\mathbf{r}' - \mathbf{x}(t'))$ を用いて次のように表されます。

$$
\finalanswer{\rho(\mathbf{r}', t') = e\,\delta\bigl(\mathbf{r}' - \mathbf{x}(t')\bigr), \qquad \mathbf{j}(\mathbf{r}', t') = e\,\mathbf{v}(t')\,\delta\bigl(\mathbf{r}' - \mathbf{x}(t')\bigr)}
$$

### (3)

遠方 $r \gg |\mathbf{r}'|$ において，距離 $|\mathbf{r} - \mathbf{r}'|$ を $|\mathbf{r}'|/r$ の1次まで展開します。

$$
\begin{aligned}
|\mathbf{r} - \mathbf{r}'| &= \sqrt{r^2 - 2\mathbf{r}\cdot\mathbf{r}' + |\mathbf{r}'|^2} \\
&= r\sqrt{1 - \frac{2\hat{\mathbf{r}}\cdot\mathbf{r}'}{r} + \frac{|\mathbf{r}'|^2}{r^2}} \\
&\approx r - \hat{\mathbf{r}}\cdot\mathbf{r}'
\end{aligned}
$$

これより遅延時刻 $t'$ は $t_0 = t - \dfrac{r}{c}$ を用いて次のように近似されます。

$$
\begin{aligned}
t' &= t - \frac{|\mathbf{r} - \mathbf{r}'|}{c} \\
&\approx t_0 + \frac{\hat{\mathbf{r}}\cdot\mathbf{r}'}{c}
\end{aligned}
$$

式 (1) の分母の $\dfrac{1}{|\mathbf{r} - \mathbf{r}'|}$ を $\dfrac{1}{r}$ で置き換え，分子の $\rho(\mathbf{r}', t')$ を $t_0$ の周りに $\dfrac{\hat{\mathbf{r}}\cdot\mathbf{r}'}{c}$ の1次までテイラー展開します。

$$
\begin{aligned}
\phi(\mathbf{r}, t) &\approx \frac{1}{4\pi\varepsilon_0 r} \int \rho\left(\mathbf{r}', t_0 + \frac{\hat{\mathbf{r}}\cdot\mathbf{r}'}{c}\right)\mathrm{d}^3 r' \\
&\approx \frac{1}{4\pi\varepsilon_0 r} \int \left[\rho(\mathbf{r}', t_0) + \frac{\hat{\mathbf{r}}\cdot\mathbf{r}'}{c}\frac{\partial \rho(\mathbf{r}', t_0)}{\partial t_0}\right]\mathrm{d}^3 r' \\
&= \frac{1}{4\pi\varepsilon_0 r}\left[\int \rho(\mathbf{r}', t_0)\,\mathrm{d}^3 r' + \frac{\hat{\mathbf{r}}}{c}\cdot\frac{\mathrm{d}}{\mathrm{d}t_0}\int \mathbf{r}'\rho(\mathbf{r}', t_0)\,\mathrm{d}^3 r'\right]
\end{aligned}
$$

ここに (2) の $\rho(\mathbf{r}', t_0) = e\,\delta(\mathbf{r}' - \mathbf{x}(t_0))$ を代入します。

$$
\begin{aligned}
\int \rho(\mathbf{r}', t_0)\,\mathrm{d}^3 r' &= e \\
\int \mathbf{r}'\rho(\mathbf{r}', t_0)\,\mathrm{d}^3 r' &= e\,\mathbf{x}(t_0)
\end{aligned}
$$

第2式を $t_0$ で微分すると $e\,\mathbf{v}(t_0)$ となるため，$\phi(\mathbf{r}, t)$ は次の形になります。

$$
\phi(\mathbf{r}, t) = \frac{e}{4\pi\varepsilon_0 r}\left(1 + \frac{\hat{\mathbf{r}}\cdot\mathbf{v}(t_0)}{c}\right)
$$

次にベクトルポテンシャル $\mathbf{A}(\mathbf{r}, t)$ を求めます。$\mathbf{j}$ はすでに速度 $\mathbf{v}$ に比例する $O(v/c)$ の量なので，$c\mathbf{A}$ を $v/c$ の1次まで求めるには $\mathbf{j}(\mathbf{r}', t') \approx \mathbf{j}(\mathbf{r}', t_0)$ として十分です。$\mu_0 = \dfrac{1}{\varepsilon_0 c^2}$ を用います。

$$
\begin{aligned}
c\mathbf{A}(\mathbf{r}, t) &\approx \frac{c\mu_0}{4\pi r} \int \mathbf{j}(\mathbf{r}', t_0)\,\mathrm{d}^3 r' \\
&= \frac{1}{4\pi\varepsilon_0 c r} \int e\,\mathbf{v}(t_0)\,\delta\bigl(\mathbf{r}' - \mathbf{x}(t_0)\bigr)\,\mathrm{d}^3 r' \\
&= \frac{e}{4\pi\varepsilon_0 r}\frac{\mathbf{v}(t_0)}{c}
\end{aligned}
$$

以上より，式 (2) の2式が成り立ちます。

### (4)

$t_0 = t - \dfrac{r}{c}$ より，空間微分と時間微分に関して次が成り立ちます。

$$
\nabla t_0 = -\frac{1}{c}\nabla r = -\frac{\hat{\mathbf{r}}}{c}, \qquad \frac{\partial t_0}{\partial t} = 1
$$

また $\dfrac{1}{r}$ や $\hat{\mathbf{r}} = \dfrac{\mathbf{r}}{r}$ を空間微分すると $O(1/r^2)$ の項が生じるため，遠方で $1/r$ に比例する主要項だけを取り出すには，$t_0$ に依存する $\mathbf{v}(t_0)$ だけを微分します。$\dfrac{\mathrm{d}\mathbf{v}(t_0)}{\mathrm{d}t_0} = \mathbf{a}(t_0)$ を用いて，$-\nabla\phi$ と $-\dfrac{\partial\mathbf{A}}{\partial t}$ の $1/r$ の項をそれぞれ計算します。

$$
\begin{aligned}
-\nabla\phi(\mathbf{r}, t) &\approx -\frac{e}{4\pi\varepsilon_0 r}\nabla\left(\frac{\hat{\mathbf{r}}\cdot\mathbf{v}(t_0)}{c}\right) \\
&\approx -\frac{e}{4\pi\varepsilon_0 c r}\bigl(\hat{\mathbf{r}}\cdot\mathbf{a}(t_0)\bigr)\nabla t_0 \\
&= \frac{e}{4\pi\varepsilon_0 c^2 r}\hat{\mathbf{r}}\bigl(\hat{\mathbf{r}}\cdot\mathbf{a}(t_0)\bigr)
\end{aligned}
$$

$$
\begin{aligned}
-\frac{\partial\mathbf{A}(\mathbf{r}, t)}{\partial t} &= -\frac{e}{4\pi\varepsilon_0 c^2 r}\frac{\partial\mathbf{v}(t_0)}{\partial t} \\
&= -\frac{e}{4\pi\varepsilon_0 c^2 r}\mathbf{a}(t_0)
\end{aligned}
$$

これらを足し合わせ，公式 $\mathbf{X} \times (\mathbf{Y} \times \mathbf{Z}) = \mathbf{Y}(\mathbf{X}\cdot\mathbf{Z}) - \mathbf{Z}(\mathbf{X}\cdot\mathbf{Y})$ に $\mathbf{X} = \hat{\mathbf{r}}$，$\mathbf{Y} = \hat{\mathbf{r}}$，$\mathbf{Z} = \mathbf{a}(t_0)$ を代入すると，$\hat{\mathbf{r}}\cdot\hat{\mathbf{r}} = 1$ より次が成り立ちます。

$$
\begin{aligned}
\mathbf{E}(\mathbf{r}, t) &= \frac{e}{4\pi\varepsilon_0 c^2 r}\left[\hat{\mathbf{r}}\bigl(\hat{\mathbf{r}}\cdot\mathbf{a}(t_0)\bigr) - \mathbf{a}(t_0)\right] \\
&= \frac{e}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf{r}} \times \bigl(\hat{\mathbf{r}} \times \mathbf{a}(t_0)\bigr)
\end{aligned}
$$

次に磁束密度の主要項 $c\mathbf{B} = c\nabla \times \mathbf{A}$ を計算します。任意のベクトル関数 $\mathbf{v}(t_0)$ に対して $\nabla \times \mathbf{v}(t_0) = (\nabla t_0) \times \mathbf{a}(t_0)$ が成り立つことを用います。

$$
\begin{aligned}
c\mathbf{B}(\mathbf{r}, t) &\approx \frac{e}{4\pi\varepsilon_0 c r}\nabla \times \mathbf{v}(t_0) \\
&= \frac{e}{4\pi\varepsilon_0 c r}(\nabla t_0) \times \mathbf{a}(t_0) \\
&= -\frac{e}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf{r}} \times \mathbf{a}(t_0)
\end{aligned}
$$

以上より，式 (3) が得られます。

### (5)

まず，式 (3) から電磁波のエネルギー流束を表すポインティングベクトル $\mathbf{S} = \dfrac{1}{\mu_0}\mathbf{E} \times \mathbf{B}$ を求めます。$\mathbf{w} = \hat{\mathbf{r}} \times \mathbf{a}(t_0)$ とおくと，$\hat{\mathbf{r}} \perp \mathbf{w}$ であり，式 (3) は次の形になります。

$$
\mathbf{E} = \frac{e}{4\pi\varepsilon_0 c^2 r}\,\hat{\mathbf{r}} \times \mathbf{w}, \qquad \mathbf{B} = -\frac{e}{4\pi\varepsilon_0 c^3 r}\,\mathbf{w}
$$

ベクトル積の公式から，外積 $(\hat{\mathbf{r}} \times \mathbf{w}) \times (-\mathbf{w})$ を計算します。

$$
\begin{aligned}
(\hat{\mathbf{r}} \times \mathbf{w}) \times (-\mathbf{w}) &= \mathbf{w} \times (\hat{\mathbf{r}} \times \mathbf{w}) \\
&= \hat{\mathbf{r}}|\mathbf{w}|^2 - \mathbf{w}(\mathbf{w}\cdot\hat{\mathbf{r}}) \\
&= |\mathbf{w}|^2\hat{\mathbf{r}}
\end{aligned}
$$

$\dfrac{1}{\mu_0} = \varepsilon_0 c^2$ を用いて $\mathbf{S}$ を計算します。

$$
\begin{aligned}
\mathbf{S}(\mathbf{r}, t) &= \frac{1}{\mu_0}\mathbf{E} \times \mathbf{B} \\
&= \varepsilon_0 c^2 \left(\frac{e}{4\pi\varepsilon_0 c^2 r}\right)^2 \frac{1}{c}\,|\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2\,\hat{\mathbf{r}} \\
&= \frac{e^2}{16\pi^2\varepsilon_0 c^3 r^2}\,|\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2\,\hat{\mathbf{r}}
\end{aligned}
$$

したがって，半径 $r$ の球面上の各点での電磁波の強度は，1周期平均 $\bigl\langle |\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2 \bigr\rangle$ に比例します。

#### (a)

$x$ 軸上の単振動の角振動数を $\omega$ とすると，位置と加速度は次の通りです。

$$
\mathbf{x}(t) = \bigl(b\cos(\omega t),\, 0,\, 0\bigr), \qquad \mathbf{a}(t_0) = \bigl(-b\omega^2\cos(\omega t_0),\, 0,\, 0\bigr)
$$

観測方向 $\hat{\mathbf{r}} = (\hat{r}_x, \hat{r}_y, \hat{r}_z)$ が $x$ 軸となす角を $\alpha$ とすると，$\hat{r}_x = \cos\alpha$ なので $|\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2$ は次のようになります。

$$
\begin{aligned}
|\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2 &= |\mathbf{a}(t_0)|^2 \sin^2\alpha \\
&= b^2\omega^4 \cos^2(\omega t_0) \sin^2\alpha
\end{aligned}
$$

1周期にわたる時間平均は $\langle \cos^2(\omega t_0) \rangle = \dfrac{1}{2}$ です。

$$
\bigl\langle |\mathbf{S}| \bigr\rangle = \frac{e^2 b^2\omega^4}{32\pi^2\varepsilon_0 c^3 r^2}\sin^2\alpha
$$

$\sin^2\alpha$ は $\alpha = \dfrac{\pi}{2}$，すなわち $\hat{r}_x = 0$ で最大値 $1$ をとります。したがって，強度が最大となる場所は球面と $yz$ 平面の交線である次の大円上です。

$$
\finalanswer{x = 0, \qquad y^2 + z^2 = r^2}
$$

#### (b)

$xy$ 平面上の等速円運動の角振動数を $\omega$ とすると，位置と加速度は次の通りです。

$$
\mathbf{x}(t) = \bigl(b\cos(\omega t),\, b\sin(\omega t),\, 0\bigr), \qquad \mathbf{a}(t_0) = \bigl(-b\omega^2\cos(\omega t_0),\, -b\omega^2\sin(\omega t_0),\, 0\bigr)
$$

極座標 $(\theta, \varphi)$ を用いて $\hat{\mathbf{r}} = (\sin\theta\cos\varphi,\, \sin\theta\sin\varphi,\, \cos\theta)$ とおきます。内積 $\hat{\mathbf{r}}\cdot\mathbf{a}(t_0)$ を計算します。

$$
\begin{aligned}
\hat{\mathbf{r}}\cdot\mathbf{a}(t_0) &= -b\omega^2\sin\theta\bigl(\cos\varphi\cos(\omega t_0) + \sin\varphi\sin(\omega t_0)\bigr) \\
&= -b\omega^2\sin\theta\cos(\omega t_0 - \varphi)
\end{aligned}
$$

これより $|\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2 = |\mathbf{a}(t_0)|^2 - \bigl(\hat{\mathbf{r}}\cdot\mathbf{a}(t_0)\bigr)^2$ を計算します。

$$
\begin{aligned}
|\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2 &= b^2\omega^4 - b^2\omega^4\sin^2\theta\cos^2(\omega t_0 - \varphi) \\
&= b^2\omega^4\left[1 - \sin^2\theta\cos^2(\omega t_0 - \varphi)\right]
\end{aligned}
$$

1周期にわたる時間平均は $\langle \cos^2(\omega t_0 - \varphi) \rangle = \dfrac{1}{2}$ です。

$$
\begin{aligned}
\bigl\langle |\hat{\mathbf{r}} \times \mathbf{a}(t_0)|^2 \bigr\rangle &= b^2\omega^4\left(1 - \frac{1}{2}\sin^2\theta\right) \\
&= \frac{1}{2}b^2\omega^4\left(1 + \cos^2\theta\right)
\end{aligned}
$$

したがって，1周期平均の電磁波の強度は次のようになります。

$$
\bigl\langle |\mathbf{S}| \bigr\rangle = \frac{e^2 b^2\omega^4}{32\pi^2\varepsilon_0 c^3 r^2}\left(1 + \cos^2\theta\right)
$$

$1 + \cos^2\theta$ は $\theta = 0$ および $\theta = \pi$ で最大値 $2$ をとります。これは，円運動の加速度ベクトルが常に $xy$ 平面内にあり，$z$ 軸方向から見れば加速度が常に視線に垂直となって $|\hat{\mathbf{r}} \times \mathbf{a}| = |\mathbf{a}|$ が1周期中ずっと最大になるためです。したがって，強度が最大となる場所は $z$ 軸と球面の交点である次の2点です。

$$
\finalanswer{(0, 0, r), \qquad (0, 0, -r)}
$$

<aside class="rigor-note" markdown>
(3) のスカラーポテンシャルの第2項 $\dfrac{\hat{\mathbf{r}}\cdot\mathbf{v}(t_0)}{c}$ は，点粒子に対する厳密なリエナール・ヴィーヘルトポテンシャルの分母 $1 - \dfrac{\hat{\mathbf{r}}\cdot\mathbf{v}}{c}$ を $v/c$ の1次まで展開した項と一致します。また (3) のテイラー展開で $2$ 次以上の項を無視してよい条件は，波源の大きさ $b$ が放射される電磁波の波長 $\lambda \sim c/\omega$ より十分小さいこと，すなわち $b\omega/c \sim v/c \ll 1$ です。
</aside>
