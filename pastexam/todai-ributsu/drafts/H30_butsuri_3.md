---
title: 東大理物 平成30年度 物理学 第3問：電気双極子放射と二波源の干渉
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成30年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成30年度 物理学 第3問：電気双極子放射と二波源の干渉

## 問題

電磁気現象は次の Maxwell 方程式で記述される。ただし，$\boldsymbol{E}$ は電場，$\boldsymbol{B}$ は磁束密度，$\rho$ は電荷密度，$\boldsymbol{j}$ は電流密度，$\varepsilon_0$ は真空誘電率，$\mu_0$ は真空透磁率，$c = 1/\sqrt{\varepsilon_0\mu_0}$ は光速度である。

$$
\begin{aligned}
\nabla\cdot\boldsymbol{E} &= \frac{\rho}{\varepsilon_0} \qquad &(1) \\
\nabla\cdot\boldsymbol{B} &= 0 \qquad &(2) \\
\nabla\times\boldsymbol{E} &= -\frac{\partial\boldsymbol{B}}{\partial t} \qquad &(3) \\
\nabla\times\boldsymbol{B} &= \mu_0\boldsymbol{j} + \frac{1}{c^2}\frac{\partial\boldsymbol{E}}{\partial t} \qquad &(4)
\end{aligned}
$$

電気双極子がつくる電磁場を求めたい。このとき以下の設問に答えよ。
{: .problem-lead }

(1) 最初に，静的な電気双極子 $\boldsymbol{p} = qd\boldsymbol{e}_z$ を考える。ただし，$q$ は電荷，$d$ は正負の電荷間の距離，$\boldsymbol{e}_z$ は $z$ 方向の単位ベクトルを表す。点電荷の静電ポテンシャルを用いて，この双極子が位置 $\boldsymbol{r}$ につくる静電ポテンシャル $\phi_0(\boldsymbol{r})$ を $\boldsymbol{p}$ を用いて表し，電場 $\boldsymbol{E}(\boldsymbol{r}) = -\nabla\phi_0(\boldsymbol{r})$ を極座標 $r, \theta, \varphi$ で表せ。ただし，双極子の中心は原点にあり，$d \ll r$ とする。

(2) 一般に，場が時間変動する状況を考え，電場 $\boldsymbol{E}(\boldsymbol{r}, t)$ および磁束密度 $\boldsymbol{B}(\boldsymbol{r}, t)$ をスカラーポテンシャル $\phi(\boldsymbol{r}, t)$ とベクトルポテンシャル $\boldsymbol{A}(\boldsymbol{r}, t)$ を用いて表せ。

(3) 設問2の結果とローレンツ条件 $\nabla\cdot\boldsymbol{A} + \dfrac{1}{c^2}\dfrac{\partial\phi}{\partial t} = 0$ を用いて，Maxwell 方程式が次の形式で表せることを示せ。

$$
\nabla^2\phi - \frac{1}{c^2}\frac{\partial^2\phi}{\partial t^2} = -\frac{\rho}{\varepsilon_0} \tag{5}
$$

$$
\nabla^2\boldsymbol{A} - \frac{1}{c^2}\frac{\partial^2\boldsymbol{A}}{\partial t^2} = -\mu_0\boldsymbol{j} \tag{6}
$$

図1のように原点で $z$ 方向に距離 $d$ だけ離れた2つの微小導体球が導線でつながれ，導線は十分細く，$z$ 方向に一様に電流密度 $j_z(\boldsymbol{r}, t) = I_0 e^{i\omega t}\delta(x)\delta(y)$ が流れているものとする。ただし，$I_0$ は定数である。ここで，物理量としては実部を取るものとするが，以下の設問4，5では複素数表示のままで答えてもよい。
{: .problem-lead }

<figure class="problem-figure" markdown>
![時間変動する電気双極子](../../../docs/assets/figures/pastexam-todai-ributsu/H30_butsuri_3-p1-light.svg#only-light)
![時間変動する電気双極子](../../../docs/assets/figures/pastexam-todai-ributsu/H30_butsuri_3-p1-dark.svg#only-dark)
<figcaption markdown="span">図1：時間変動する電気双極子（電流の符号は図の太線の矢印の向きを正とする）。</figcaption>
</figure>

(4) 上下の各導体球に蓄えられる電荷 $\pm q(t)$ を $I_0,\ \omega$ などを用いて表せ。

(5) 式 (6) を満たすベクトルポテンシャル $\boldsymbol{A}(\boldsymbol{r}, t)$ の解は次式 (7) で表される。

$$
\boldsymbol{A}(\boldsymbol{r}, t) = \frac{\mu_0}{4\pi}\int d^3r'\,\frac{\boldsymbol{j}\!\left(\boldsymbol{r}', t - \frac{|\boldsymbol{r} - \boldsymbol{r}'|}{c}\right)}{|\boldsymbol{r} - \boldsymbol{r}'|} \tag{7}
$$

上で与えた電流密度 $j_z$ が十分離れた位置 $\boldsymbol{r}$ に生じさせるベクトルポテンシャルを書き下し，その結果から $\boldsymbol{B}(\boldsymbol{r}, t)$ を求めよ。また，$\boldsymbol{B}(\boldsymbol{r}, t)$ と式 (4) を用いて，電場 $\boldsymbol{E}(\boldsymbol{r}, t)$ を求めよ。ただし，$\boldsymbol{B}(\boldsymbol{r}, t)$ と $\boldsymbol{E}(\boldsymbol{r}, t)$ は，$r$ に対して最もゆっくり減衰する項一つずつのみ求めればよい。ここで，この電流から放射される電磁波の波数を $k$ とするとき，$k = \omega/c$ の関係を用いてよい。また位置 $\boldsymbol{r}$ は，$d \ll r,\ kr \gg 1$ を満たす十分離れた点とする。なお，任意のベクトル場 $\boldsymbol{V}$ に関する公式 $\nabla\times\boldsymbol{V} = \left(\boldsymbol{e}_r\dfrac{\partial}{\partial r} + \boldsymbol{e}_\theta\dfrac{\partial}{r\partial\theta} + \boldsymbol{e}_\varphi\dfrac{\partial}{r\sin\theta\partial\varphi}\right)\times\boldsymbol{V}$ を用いてよい。ただし，$\boldsymbol{e}_r,\ \boldsymbol{e}_\theta,\ \boldsymbol{e}_\varphi$ は，それぞれ $r, \theta, \varphi$ 方向の単位ベクトルである。

(6) 設問5で得られた電場と磁場の解を用いて，それらの実数成分からポインティングベクトル $\boldsymbol{S} = \dfrac{1}{\mu_0}\boldsymbol{E}\times\boldsymbol{B}$ とその時間平均 $\overline{\boldsymbol{S}}$ を計算し，$I_0,\ d,\ r,\ \mu_0,\ c,\ \omega,\ k,\ \theta$ などを用いて表せ。

次に，図2のように，2つの波源から電磁波が放射される場合を考える。各波源は $y$ 軸上，$y = -D/2$ と $y = D/2$ の位置にあり，波源1，2が発する電場は，波源から距離 $R_n\ (n = 1, 2)$ にある $xy$ 平面内の観測点でそれぞれ，$\boldsymbol{E}_n(R_n) = \boldsymbol{e}_z E_0(R_n)\cos(\omega t - kR_n - \delta_n)$ で与えられるものとする。ただし，$\delta_n$ は各波源ごとに設定できる任意の位相とする。

<figure class="problem-figure" markdown>
![xy平面内の2つの波源と観測点](../../../docs/assets/figures/pastexam-todai-ributsu/H30_butsuri_3-p2-light.svg#only-light)
![xy平面内の2つの波源と観測点](../../../docs/assets/figures/pastexam-todai-ributsu/H30_butsuri_3-p2-dark.svg#only-dark)
<figcaption markdown="span">図2：$xy$ 平面内の2つの波源と観測点。</figcaption>
</figure>

(7) 2つの波源からの放射が十分離れた $xy$ 平面内の点 $\boldsymbol{r} = (r\cos\varphi, r\sin\varphi, 0)$ に作る電界強度 $|\boldsymbol{E}|^2$ を計算し，$\delta_n = 0\ (n = 1, 2)$ のときの角度 $\varphi$ 依存性を求めよ。また，強度が最大値の $1/2$ になる角度幅 $\Delta\varphi$ を求め，$\Delta\varphi$ を小さくする方法について議論せよ。さらに，各波源の電場の位相 $\delta_n$ を制御し，電界強度が最大となる方向が $\varphi = \varphi_0$ となるような，位相の差 $\delta_2 - \delta_1$ を求めよ。ただし，$D \ll r$ とし，$E_0(R_1) = E_0(R_2)$ と見なしてよい。

> 出典：東京大学大学院理学系研究科物理学専攻 平成30年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
時間変化する電流がつくる場は，電流の各部分から遅れて届くポテンシャルを足し合わせて求めます。遠方では $1/r$ で減る項だけが残るので，空間微分は位相 $e^{-ikr}$ の微分 $-ik\boldsymbol{e}_r$ に置き換えます。電場と磁場が求まれば，その積からエネルギーの流れを計算します。

2つのアンテナからの電場を足すと，観測点までの道のりの差による位相と，2つの電流の位相差が，同じ指数関数の中に入ります。和を積に直すと，強度は角度による因子と時間の振動の因子の積になるので，強度が最大になる向きと，強度が半分になる角度を求めることができます。
</div>

### (1)
正電荷 $+q$ が $\boldsymbol{r}_+ = (d/2)\boldsymbol{e}_z$，負電荷 $-q$ が $\boldsymbol{r}_- = -(d/2)\boldsymbol{e}_z$ にあるときの静電ポテンシャルは，$d \ll r$ で1次まで展開すると次のように求まります。

$$
\begin{aligned}
\phi_0(\boldsymbol{r}) &= \frac{q}{4\pi\varepsilon_0}\left(\frac{1}{|\boldsymbol{r} - \frac{d}{2}\boldsymbol{e}_z|} - \frac{1}{|\boldsymbol{r} + \frac{d}{2}\boldsymbol{e}_z|}\right) \\
&\simeq \frac{q}{4\pi\varepsilon_0 r}\left[\left(1 + \frac{d\cos\theta}{2r}\right) - \left(1 - \frac{d\cos\theta}{2r}\right)\right] \\
&= \frac{qd\cos\theta}{4\pi\varepsilon_0 r^2} \\
&= \frac{\boldsymbol{p}\cdot\boldsymbol{r}}{4\pi\varepsilon_0 r^3}
\end{aligned}
$$

極座標における勾配公式を用いて電場 $\boldsymbol{E}(\boldsymbol{r}) = -\nabla\phi_0(\boldsymbol{r})$ を計算します。

$$
\begin{aligned}
\boldsymbol{E}(\boldsymbol{r})
&= -\left(\frac{\partial\phi_0}{\partial r}\boldsymbol{e}_r + \frac{1}{r}\frac{\partial\phi_0}{\partial\theta}\boldsymbol{e}_\theta + \frac{1}{r\sin\theta}\frac{\partial\phi_0}{\partial\varphi}\boldsymbol{e}_\varphi\right) \\
&= \frac{p}{4\pi\varepsilon_0 r^3}\left(2\cos\theta\,\boldsymbol{e}_r + \sin\theta\,\boldsymbol{e}_\theta\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{\phi_0(\boldsymbol{r}) = \frac{\boldsymbol{p}\cdot\boldsymbol{r}}{4\pi\varepsilon_0 r^3},\qquad \boldsymbol{E}(\boldsymbol{r}) = \frac{p}{4\pi\varepsilon_0 r^3}\left(2\cos\theta\,\boldsymbol{e}_r + \sin\theta\,\boldsymbol{e}_\theta\right)}
$$

### (2)
式 (2) $\nabla\cdot\boldsymbol{B} = 0$ より $\boldsymbol{B}$ はベクトルポテンシャル $\boldsymbol{A}$ の回転として表されます。これを式 (3) に代入すると $\nabla\times\left(\boldsymbol{E} + \dfrac{\partial\boldsymbol{A}}{\partial t}\right) = 0$ となるため，スカラーポテンシャル $\phi$ を用いて $\boldsymbol{E} + \dfrac{\partial\boldsymbol{A}}{\partial t} = -\nabla\phi$ と表されます。したがって，

$$
\finalanswer{\boldsymbol{E}(\boldsymbol{r}, t) = -\nabla\phi(\boldsymbol{r}, t) - \frac{\partial\boldsymbol{A}(\boldsymbol{r}, t)}{\partial t},\qquad \boldsymbol{B}(\boldsymbol{r}, t) = \nabla\times\boldsymbol{A}(\boldsymbol{r}, t)}
$$

### (3)
問2の表式を式 (1) に代入し，ローレンツ条件 $\nabla\cdot\boldsymbol{A} = -\dfrac{1}{c^2}\dfrac{\partial\phi}{\partial t}$ を用います。

$$
\begin{aligned}
\nabla\cdot\left(-\nabla\phi - \frac{\partial\boldsymbol{A}}{\partial t}\right) &= \frac{\rho}{\varepsilon_0} \\
-\nabla^2\phi - \frac{\partial}{\partial t}(\nabla\cdot\boldsymbol{A}) &= \frac{\rho}{\varepsilon_0} \\
\nabla^2\phi - \frac{1}{c^2}\frac{\partial^2\phi}{\partial t^2} &= -\frac{\rho}{\varepsilon_0}
\end{aligned}
$$

次に問2の表式を式 (4) に代入し，ベクトル恒等式 $\nabla\times(\nabla\times\boldsymbol{A}) = \nabla(\nabla\cdot\boldsymbol{A}) - \nabla^2\boldsymbol{A}$ とローレンツ条件を用います。

$$
\nabla(\nabla\cdot\boldsymbol{A}) - \nabla^2\boldsymbol{A} = \mu_0\boldsymbol{j} + \frac{1}{c^2}\frac{\partial}{\partial t}\left(-\nabla\phi - \frac{\partial\boldsymbol{A}}{\partial t}\right)
$$

右辺の時間微分の項を左辺に移し，$\nabla$ を含む項をまとめます。

$$
-\nabla^2\boldsymbol{A} + \frac{1}{c^2}\frac{\partial^2\boldsymbol{A}}{\partial t^2} + \nabla\left(\nabla\cdot\boldsymbol{A} + \frac{1}{c^2}\frac{\partial\phi}{\partial t}\right) = \mu_0\boldsymbol{j}
$$

ローレンツ条件から，左辺の第3項は $0$ です。両辺に $-1$ を掛けると，次の式になります。

$$
\nabla^2\boldsymbol{A} - \frac{1}{c^2}\frac{\partial^2\boldsymbol{A}}{\partial t^2} = -\mu_0\boldsymbol{j}
$$

よって式 (5) および式 (6) が導かれます。

### (4)
導線を流れる電流は $+z$ 向きに $I(t) = I_0 e^{i\omega t}$ なので，$z=+d/2$ の上の導体球の電荷 $+q(t)$ について電荷保存則 $\dfrac{\mathrm{d}q}{\mathrm{d}t} = I_0 e^{i\omega t}$ が成り立ちます。定常振動解を $q(t) \propto e^{i\omega t}$ とおいて積分します。

$$
\begin{aligned}
i\omega q(t) &= I_0 e^{i\omega t} \\
q(t) &= \frac{I_0}{i\omega}e^{i\omega t} \\
&= -\frac{i I_0}{\omega}e^{i\omega t}
\end{aligned}
$$

したがって，上下の各導体球に蓄えられる電荷は

$$
\finalanswer{\pm q(t) = \pm\frac{I_0}{i\omega}e^{i\omega t} = \mp\frac{i I_0}{\omega}e^{i\omega t}}
$$

### (5)
問1からの流れのとおり，導線は点とみなすことができる電気双極子として扱います。そのため，導線の長さ $d$ は波長より十分短く，$kd \ll 1$ とします。導線の範囲 $-d/2 \le z' \le d/2$ では $d \ll r$ でもあるので，$|\boldsymbol{r} - \boldsymbol{r}'| \simeq r$ として式 (7) を積分します。

$$
\begin{aligned}
\boldsymbol{A}(\boldsymbol{r}, t)
&\simeq \frac{\mu_0}{4\pi r}\int_{-d/2}^{d/2} \mathrm{d}z'\,I_0 e^{i\omega\left(t - \frac{r}{c}\right)}\boldsymbol{e}_z \\
&= \frac{\mu_0 I_0 d}{4\pi r}e^{i(\omega t - kr)}\boldsymbol{e}_z
\end{aligned}
$$

次に $\boldsymbol{B} = \nabla\times\boldsymbol{A}$ を計算します。$kr \gg 1$ より，$1/r$ の微分（$\mathcal{O}(r^{-2})$）に比べて位相 $e^{-ikr}$ の $r$ 微分（$\mathcal{O}(kr^{-1})$）が最もゆっくり減衰する項を与えます。$\boldsymbol{e}_r\times\boldsymbol{e}_z = -\sin\theta\,\boldsymbol{e}_\varphi$ を用います。

$$
\begin{aligned}
\boldsymbol{B}(\boldsymbol{r}, t)
&\simeq \left(\boldsymbol{e}_r\frac{\partial}{\partial r}\right)\times\left(\frac{\mu_0 I_0 d}{4\pi r}e^{i(\omega t - kr)}\boldsymbol{e}_z\right) \\
&\simeq (-ik)\frac{\mu_0 I_0 d}{4\pi r}e^{i(\omega t - kr)}\left(\boldsymbol{e}_r\times\boldsymbol{e}_z\right) \\
&= \frac{i\mu_0 k I_0 d}{4\pi r}\sin\theta\,e^{i(\omega t - kr)}\boldsymbol{e}_\varphi
\end{aligned}
$$

続いて遠方（$\boldsymbol{j} = \mathbf{0}$）の式 (4) $\dfrac{1}{c^2}\dfrac{\partial\boldsymbol{E}}{\partial t} = \nabla\times\boldsymbol{B}$ より，$\dfrac{i\omega}{c^2}\boldsymbol{E} = \nabla\times\boldsymbol{B}$ です。同様に $e^{-ikr}$ の $r$ 微分のみを残し，$\boldsymbol{e}_r\times\boldsymbol{e}_\varphi = -\boldsymbol{e}_\theta$ および $\omega = ck$ を用います。

$$
\begin{aligned}
\boldsymbol{E}(\boldsymbol{r}, t)
&\simeq \frac{c^2}{i\omega}(-ik)\left(\boldsymbol{e}_r\times\boldsymbol{e}_\varphi\right)\frac{i\mu_0 k I_0 d}{4\pi r}\sin\theta\,e^{i(\omega t - kr)} \\
&= c\left(\frac{i\mu_0 k I_0 d}{4\pi r}\sin\theta\,e^{i(\omega t - kr)}\right)\boldsymbol{e}_\theta \\
&= \frac{i\mu_0 \omega I_0 d}{4\pi r}\sin\theta\,e^{i(\omega t - kr)}\boldsymbol{e}_\theta
\end{aligned}
$$

したがって，

$$
\finalanswer{\boldsymbol{A}(\boldsymbol{r}, t) = \frac{\mu_0 I_0 d}{4\pi r}e^{i(\omega t - kr)}\boldsymbol{e}_z,\qquad \boldsymbol{B}(\boldsymbol{r}, t) = \frac{i\mu_0 k I_0 d}{4\pi r}\sin\theta\,e^{i(\omega t - kr)}\boldsymbol{e}_\varphi,\qquad \boldsymbol{E}(\boldsymbol{r}, t) = \frac{i\mu_0 \omega I_0 d}{4\pi r}\sin\theta\,e^{i(\omega t - kr)}\boldsymbol{e}_\theta}
$$

### (6)
$I_0$ を実数として問5の $\boldsymbol{E},\ \boldsymbol{B}$ の実部をとります（$\operatorname{Re}(i e^{i\alpha}) = -\sin\alpha$）。

$$
\begin{aligned}
\operatorname{Re}\boldsymbol{E}(\boldsymbol{r}, t) &= -\frac{\mu_0\omega I_0 d}{4\pi r}\sin\theta\sin(\omega t - kr)\,\boldsymbol{e}_\theta \\
\operatorname{Re}\boldsymbol{B}(\boldsymbol{r}, t) &= -\frac{\mu_0 k I_0 d}{4\pi r}\sin\theta\sin(\omega t - kr)\,\boldsymbol{e}_\varphi
\end{aligned}
$$

$\boldsymbol{e}_\theta\times\boldsymbol{e}_\varphi = \boldsymbol{e}_r$ および $\omega = ck$ より，ポインティングベクトル $\boldsymbol{S} = \dfrac{1}{\mu_0}\boldsymbol{E}\times\boldsymbol{B}$ は次のようになります。

$$
\boldsymbol{S} = \frac{\mu_0\omega k I_0^2 d^2}{16\pi^2 r^2}\sin^2\theta\sin^2(\omega t - kr)\,\boldsymbol{e}_r
= \frac{\mu_0 c k^2 I_0^2 d^2}{16\pi^2 r^2}\sin^2\theta\sin^2(\omega t - kr)\,\boldsymbol{e}_r
$$

1周期にわたる時間平均は $\overline{\sin^2(\omega t - kr)} = \dfrac{1}{2}$ なので，

$$
\overline{\boldsymbol{S}} = \frac{\mu_0 c k^2 I_0^2 d^2}{32\pi^2 r^2}\sin^2\theta\,\boldsymbol{e}_r
= \frac{\mu_0 \omega^2 I_0^2 d^2}{32\pi^2 c r^2}\sin^2\theta\,\boldsymbol{e}_r
$$

となります。したがって，

$$
\finalanswer{\boldsymbol{S} = \frac{\mu_0 c k^2 I_0^2 d^2}{16\pi^2 r^2}\sin^2\theta\sin^2(\omega t - kr)\,\boldsymbol{e}_r,\qquad \overline{\boldsymbol{S}} = \frac{\mu_0 c k^2 I_0^2 d^2}{32\pi^2 r^2}\sin^2\theta\,\boldsymbol{e}_r}
$$

### (7)
点 $\boldsymbol{r} = (r\cos\varphi, r\sin\varphi, 0)$ と2つの波源 $(0, \mp D/2, 0)$ の距離 $R_1,\ R_2$ を $D \ll r$ で1次まで展開します。

$$
\begin{aligned}
R_1 &= \sqrt{r^2\cos^2\varphi + \left(r\sin\varphi + \frac{D}{2}\right)^2} \\
&\simeq r + \frac{D}{2}\sin\varphi
\end{aligned}
$$

$R_2$ は，$R_1$ の式の $D$ を $-D$ に置き換えて求めます。

$$
R_2 \simeq r - \frac{D}{2}\sin\varphi
$$

$E_0(R_1) = E_0(R_2) \equiv E_0$ とし，和積公式を用いて合成電場 $\boldsymbol{E} = \boldsymbol{E}_1 + \boldsymbol{E}_2$ を計算します。

$$
\begin{aligned}
\boldsymbol{E}
&= \boldsymbol{e}_z E_0\left[\cos\left(\omega t - kr - \frac{kD}{2}\sin\varphi - \delta_1\right) + \cos\left(\omega t - kr + \frac{kD}{2}\sin\varphi - \delta_2\right)\right] \\
&= 2\boldsymbol{e}_z E_0\cos\left(\frac{kD\sin\varphi - (\delta_2 - \delta_1)}{2}\right)\cos\left(\omega t - kr - \frac{\delta_1 + \delta_2}{2}\right)
\end{aligned}
$$

よって瞬時の電界強度 $|\boldsymbol{E}|^2$ および時間平均 $\overline{|\boldsymbol{E}|^2}$ は次のとおりです。

$$
|\boldsymbol{E}|^2 = 4E_0^2\cos^2\left(\frac{kD\sin\varphi - (\delta_2 - \delta_1)}{2}\right)\cos^2\left(\omega t - kr - \frac{\delta_1 + \delta_2}{2}\right),\qquad
\overline{|\boldsymbol{E}|^2} = 2E_0^2\cos^2\left(\frac{kD\sin\varphi - (\delta_2 - \delta_1)}{2}\right)
$$



$\delta_1 = \delta_2 = 0$ のとき，角度依存性は $\cos^2\left(\dfrac{kD}{2}\sin\varphi\right)$ となり，$\varphi = 0$ で最大値をとります。最大値の $1/2$ となる角度 $\pm\varphi_{1/2}$ は次式で決まります。

$$
\begin{aligned}
\frac{kD}{2}\sin\varphi_{1/2}&=\frac{\pi}{4}\\
\sin\varphi_{1/2}&=\frac{\pi}{2kD}\\
&=\frac{\lambda}{4D}
\end{aligned}
$$

半値点が存在するには $\pi/(2kD)\le1$，すなわち $kD\ge\pi/2$ が必要です。この範囲では，半値全幅は

$$
\finalanswer{\Delta\varphi=2\arcsin\!\left(\frac{\pi}{2kD}\right)\qquad(kD\ge\pi/2)}
$$

です。$0<kD<\pi/2$ では全方向の強度が最大値の半分より大きいため，半値点はありません。$kD\gg1$ なら $\Delta\varphi\simeq\pi/(kD)$ なので，$D$ または $k$ を大きくすると幅を小さくすることができます。ただし，同じ高さの極大が複数現れる場合があります。

最大となる位相条件は，

$$
\begin{aligned}
\cos^2\!\left(\frac{kD\sin\varphi_0-(\delta_2-\delta_1)}{2}\right)&=1\\
kD\sin\varphi_0-(\delta_2-\delta_1)&=2n\pi
\end{aligned}
$$

です。整数の符号を取り直すと，

$$
\finalanswer{\delta_2-\delta_1=kD\sin\varphi_0+2m\pi\qquad(m\in\mathbb Z)}
$$

が得られます。また，同位相の場合の瞬時値と平均値は

$$
\finalanswer{|\boldsymbol E|^2=4E_0^2\cos^2\!\left(\frac{kD}{2}\sin\varphi\right)\cos^2(\omega t-kr),\qquad
\overline{|\boldsymbol E|^2}=2E_0^2\cos^2\!\left(\frac{kD}{2}\sin\varphi\right)\quad(\delta_1=\delta_2=0)}
$$

です。

<aside class="rigor-note" markdown>
同位相の波源では，極大の条件は $kD\sin\varphi=2m\pi$ です。$m\neq0$ の極大が現れるのは $D\ge\lambda$ の場合です。位相差を変えて全方向へ走査する場合に，別の整数次数の極大を避ける間隔の条件は $D\le\lambda/2$ です。間隔 $D$ を大きくすると半値幅は狭くなりますが，$D$ が大きすぎると別の向きにも極大が現れます。
</aside>
