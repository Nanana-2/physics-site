---
title: 東大理物 平成12年度 物理学 第2問：電離層プラズマ中の電磁波伝播
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成12年度 物理学 第2問：電離層プラズマ中の電磁波伝播

## 問題

電離層では空気分子は電子と陽イオンに電離されたプラズマ状態にある。電離層を伝搬する電磁波を考える。電離層は全体として中性であり電磁波に対して陽イオンは重いので動かず電子だけが動くとする。電子の質量は $m$，電荷を $-e$ とし，また電子密度は $n$ として常に一様であるとし伝搬する電磁波によって生ずる磁場が電子の運動に及ぼす効果は無視できるものとする。平面波（周波数 $\omega$，波数 $k$）が電離層に垂直入射したとして以下の問いに答えよ。なお Maxwell 方程式は

$$
\nabla\cdot\mathbf{E} = 4\pi\rho \qquad\qquad \nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} \tag{1}
$$

$$
\nabla \times \mathbf{E} = -\frac{1}{c}\frac{\partial\mathbf{B}}{\partial t} \qquad\qquad \nabla \times \mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t} \tag{2}
$$

$$
\nabla\cdot\mathbf{B} = 0 \qquad\qquad \nabla\cdot\mathbf{B} = 0 \tag{3}
$$

$$
\nabla \times \mathbf{B} = \frac{1}{c}\frac{\partial\mathbf{E}}{\partial t} + \frac{4\pi}{c}\mathbf{j} \qquad\qquad \nabla \times \mathbf{B} = \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t} + \mu_0\mathbf{j} \tag{4}
$$

と書かれる（左が C.G.S. 系，右が M.K.S. 系）。ここで $\mathbf{E}$ は電場，$\mathbf{B}$ は磁束密度，$\mathbf{j}$ は電流密度，$\varepsilon_0$ は真空の誘電率，$\mu_0$ は真空の透磁率をあらわす。必要ならば $\nabla \times (\nabla \times \mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$ の公式を用いてよい。また C.G.S. 系，M.K.S. 系のいずれの単位系を用いても良い。
{: .problem-lead }

(1) プラズマ中に誘起される電流密度 $\mathbf{j}$ は，入射する電磁波の電場ベクトル $\mathbf{E}$ と電気伝導度 $\sigma$ を用い，$\mathbf{j} = \sigma\mathbf{E}$ と書くことができる。まず外部磁場がゼロとして，電離層の電気伝導度 $\sigma$ を周波数 $\omega$ の関数として書け

(2) $k$ と $\omega$ の間の分散関係を求め電離層の屈折率（$n \equiv ck/\omega$）を計算せよ。次に $\omega < \omega_p$ のとき電磁波は伝搬できないことを示し，その物理的意味を説明せよ。ここで $\omega_p$ はプラズマ周波数であり C.G.S. 系では $\sqrt{4\pi n e^2/m}$，M.K.S. 系では $\sqrt{n e^2/m\varepsilon_0}$ で与えられる。

次に電磁波の伝搬方向に一定磁場 $\mathbf{B}_0$ がかかったとする。このとき磁場に対して右回りと左回りに円偏光した電磁波は異なる伝搬の仕方をする。$z$ 方向に伝搬する円偏光した電磁波の電場ベクトルは $\mathbf{E} = E_0 e^{i(kz - \omega t)}\dfrac{1}{\sqrt{2}}(\hat{\mathbf{x}} \pm i\hat{\mathbf{y}})$（$\hat{\mathbf{x}}, \hat{\mathbf{y}}$ は各々 $x$ 方向及び $y$ 方向の単位ベクトルで，$+$ 符号は右回り，$-$ 符号は左回り）と書けることを用い，以下に答えよ。

(3) 右回り左回りそれぞれの電磁波に対する電離層の電気伝導度を $\omega, \omega_c$ の関数として書け。ここで $\omega_c$ はサイクロトロン周波数であり C.G.S. 系では $eB_0/mc$，M.K.S. 系では $eB_0/m$ で与えられる。

(4) 右回り左回りそれぞれの電磁波に対する屈折率を $\omega, \omega_p$ 及び $\omega_c$ の関数として求めよ。またこのとき一方の電磁波は $\omega < \omega_p$ でも電離層を伝搬できることを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
電子の運動方程式と電流密度 $\mathbf{j} = -ne\mathbf{v}$ を複素振幅で解くと，周波数に依存する電気伝導度 $\sigma(\omega)$ が定まります。これをマクスウェル方程式の波動方程式へ組み込むことで，分散関係と屈折率が得られます。

伝搬方向に静磁場 $\mathbf{B}_0$ を加えると，ローレンツ力 $-e\mathbf{v} \times \mathbf{B}_0$ が $x$ 成分と $y$ 成分を結合させます。円偏光の基底ベクトル $\hat{\mathbf{x}} \pm i\hat{\mathbf{y}}$ は外積演算 $\cdot \times \hat{\mathbf{z}}$ の固有ベクトルになるため，右回りと左回りの円偏光ごとにスカラーの電気伝導度と屈折率が分離して求まります。
</div>

以下では M.K.S. 単位系を用い，電子の数密度を $n_e$ と書いて屈折率 $n$ と区別します。最終結果では問題文の記号に合わせて数密度を $n$ と表記します。

### (1)

外部磁場がなく，電磁波の磁場による力を無視すると，電場 $\mathbf{E} \propto e^{i(kz - \omega t)}$ のもとでの電子の運動方程式は次の通りです。

$$
m\frac{\mathrm{d}\mathbf{v}}{\mathrm{d}t} = -e\mathbf{E}
$$

定常振動解として速度も $\mathbf{v} \propto e^{i(kz - \omega t)}$ とおくと，$\dfrac{\mathrm{d}\mathbf{v}}{\mathrm{d}t} = -i\omega\mathbf{v}$ です。これを代入して $\mathbf{v}$ を求めます。

$$
\begin{aligned}
-i\omega m\mathbf{v} &= -e\mathbf{E} \\
\mathbf{v} &= \frac{e}{i\omega m}\mathbf{E} \\
&= -\frac{ie}{m\omega}\mathbf{E}
\end{aligned}
$$

電流密度 $\mathbf{j} = -n_e e\mathbf{v}$ に代入します。

$$
\begin{aligned}
\mathbf{j} &= -n_e e\left(-\frac{ie}{m\omega}\mathbf{E}\right) \\
&= \frac{i n_e e^2}{m\omega}\mathbf{E}
\end{aligned}
$$

$\mathbf{j} = \sigma\mathbf{E}$ と比較し，電子密度を問題文の記号 $n$ で書くと，電気伝導度 $\sigma(\omega)$ は次の通りです。

$$
\finalanswer{\sigma(\omega) = \frac{i n e^2}{m\omega}}
$$

### (2)

式 (2) の両辺の回転をとり，式 (4) と $\mathbf{j} = \sigma\mathbf{E}$ を代入します。

$$
\begin{aligned}
\nabla \times (\nabla \times \mathbf{E}) &= -\frac{\partial}{\partial t}(\nabla \times \mathbf{B}) \\
&= -\mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2} - \mu_0\sigma\frac{\partial\mathbf{E}}{\partial t}
\end{aligned}
$$

電離層は全体として中性で電子密度も一様なので $\rho = 0$ であり，式 (1) より $\nabla\cdot\mathbf{E} = 0$ です。公式 $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$ より左辺は $-\nabla^2\mathbf{E}$ になります。これと $\mu_0\varepsilon_0 = \dfrac{1}{c^2}$ を用います。

$$
\nabla^2\mathbf{E} = \frac{1}{c^2}\frac{\partial^2\mathbf{E}}{\partial t^2} + \mu_0\sigma\frac{\partial\mathbf{E}}{\partial t}
$$

平面波 $\mathbf{E} \propto e^{i(kz - \omega t)}$ を代入すると，$\nabla^2 \to -k^2$，$\dfrac{\partial}{\partial t} \to -i\omega$ となります。

$$
\begin{aligned}
-k^2\mathbf{E} &= \left(-\frac{\omega^2}{c^2} - i\omega\mu_0\sigma\right)\mathbf{E} \\
k^2 &= \frac{\omega^2}{c^2} + i\omega\mu_0\sigma
\end{aligned}
$$

ここに (1) の $\sigma = \dfrac{i n_e e^2}{m\omega}$ および $\mu_0 = \dfrac{1}{\varepsilon_0 c^2}$ を代入し，プラズマ周波数 $\omega_p = \sqrt{\dfrac{n_e e^2}{m\varepsilon_0}}$ を用います。

$$
\begin{aligned}
k^2 &= \frac{\omega^2}{c^2} + i\omega\cdot\frac{1}{\varepsilon_0 c^2}\cdot\frac{i n_e e^2}{m\omega} \\
&= \frac{\omega^2}{c^2} - \frac{n_e e^2}{m\varepsilon_0 c^2} \\
&= \frac{\omega^2 - \omega_p^2}{c^2}
\end{aligned}
$$

よって分散関係は $\omega^2 = c^2 k^2 + \omega_p^2$ です。また屈折率 $n = \dfrac{ck}{\omega}$ は次のようになります。

$$
\begin{aligned}
n^2 &= \frac{c^2 k^2}{\omega^2} \\
&= 1 - \frac{\omega_p^2}{\omega^2}
\end{aligned}
$$

$$
\finalanswer{\omega^2 = c^2 k^2 + \omega_p^2, \qquad n = \sqrt{1 - \frac{\omega_p^2}{\omega^2}}}
$$

$\omega < \omega_p$ のとき，$k^2 = \dfrac{\omega^2 - \omega_p^2}{c^2} < 0$ となります。$\kappa = \dfrac{\sqrt{\omega_p^2 - \omega^2}}{c} > 0$ とおくと波数は純虚数 $k = i\kappa$ となり，電磁波は $e^{i(kz - \omega t)} = e^{-\kappa z}e^{-i\omega t}$ と $z$ 方向に指数関数的に減衰するため，電離層の内部を伝搬できません。

物理的な意味は次の通りです。プラズマ周波数 $\omega_p$ は，電子集団が陽イオンの背景に対して変位したときに静電的な復元力で振動する固有の角周波数です。入射波の周波数 $\omega$ が $\omega_p$ より低いと，電子は入射電場の変化に十分速く追随して動き，入射電場を打ち消す向きの分極電場をつくるため，電磁波はプラズマ内部へ侵入できず境界で全反射されます。

### (3)

一定磁場 $\mathbf{B}_0 = B_0\hat{\mathbf{z}}$ がかかっているときの電子の運動方程式は次の通りです。

$$
m\frac{\mathrm{d}\mathbf{v}}{\mathrm{d}t} = -e\bigl(\mathbf{E} + \mathbf{v} \times \mathbf{B}_0\bigr)
$$

右回り（$+$）および左回り（$-$）の円偏光基底ベクトル $\mathbf{e}_\pm = \dfrac{1}{\sqrt{2}}(\hat{\mathbf{x}} \pm i\hat{\mathbf{y}})$ に対して，外積 $\mathbf{e}_\pm \times \hat{\mathbf{z}}$ を計算します。$\hat{\mathbf{x}} \times \hat{\mathbf{z}} = -\hat{\mathbf{y}}$，$\hat{\mathbf{y}} \times \hat{\mathbf{z}} = \hat{\mathbf{x}}$ を用います。

$$
\begin{aligned}
\mathbf{e}_\pm \times \hat{\mathbf{z}} &= \frac{1}{\sqrt{2}}\bigl(-\hat{\mathbf{y}} \pm i\hat{\mathbf{x}}\bigr) \\
&= \pm i\cdot\frac{1}{\sqrt{2}}\bigl(\hat{\mathbf{x}} \pm i\hat{\mathbf{y}}\bigr) \\
&= \pm i\mathbf{e}_\pm
\end{aligned}
$$

電場 $\mathbf{E}_\pm = E_0 e^{i(kz - \omega t)}\mathbf{e}_\pm$ に対して速度も $\mathbf{v}_\pm = v_\pm e^{i(kz - \omega t)}\mathbf{e}_\pm$ とおき，運動方程式に代入します。

$$
\begin{aligned}
-i\omega m v_\pm \mathbf{e}_\pm &= -e E_0 \mathbf{e}_\pm - e B_0 v_\pm (\mathbf{e}_\pm \times \hat{\mathbf{z}}) \\
-i\omega m v_\pm &= -e E_0 \mp i e B_0 v_\pm \\
-i m(\omega \mp \omega_c) v_\pm &= -e E_0
\end{aligned}
$$

ここでサイクロトロン周波数 $\omega_c = \dfrac{eB_0}{m}$ を用いました。$v_\pm$ について解くと次になります。

$$
\begin{aligned}
v_\pm &= \frac{e}{i m(\omega \mp \omega_c)}E_0 \\
&= -\frac{ie}{m(\omega \mp \omega_c)}E_0
\end{aligned}
$$

電流密度 $\mathbf{j}_\pm = -n_e e\mathbf{v}_\pm$ に代入します。

$$
\begin{aligned}
\mathbf{j}_\pm &= -n_e e\left(-\frac{ie}{m(\omega \mp \omega_c)}\mathbf{E}_\pm\right) \\
&= \frac{i n_e e^2}{m(\omega \mp \omega_c)}\mathbf{E}_\pm
\end{aligned}
$$

したがって，右回り（$+$）および左回り（$-$）の円偏光に対する電気伝導度 $\sigma_\pm(\omega)$ は次の通りです。

$$
\finalanswer{\sigma_+(\omega) = \frac{i n e^2}{m(\omega - \omega_c)}, \qquad \sigma_-(\omega) = \frac{i n e^2}{m(\omega + \omega_c)}}
$$

### (4)

$\mathbf{e}_\pm$ は $\hat{\mathbf{z}}$ に垂直なので $\nabla\cdot\mathbf{E}_\pm = 0$ が成り立ちます。(2) と同じ波動方程式に $\sigma_\pm(\omega)$ を代入して屈折率 $n_\pm = \dfrac{ck_\pm}{\omega}$ を計算します。

$$
\begin{aligned}
n_\pm^2 &= 1 + \frac{i\sigma_\pm(\omega)}{\varepsilon_0\omega} \\
&= 1 + \frac{i}{\varepsilon_0\omega}\cdot\frac{i n_e e^2}{m(\omega \mp \omega_c)} \\
&= 1 - \frac{\omega_p^2}{\omega(\omega \mp \omega_c)}
\end{aligned}
$$

したがって，右回り（$+$）と左回り（$-$）の屈折率は次の通りです。

$$
\finalanswer{n_+ = \sqrt{1 - \frac{\omega_p^2}{\omega(\omega - \omega_c)}}, \qquad n_- = \sqrt{1 - \frac{\omega_p^2}{\omega(\omega + \omega_c)}}}
$$

$\omega < \omega_p$ での伝搬条件を調べます。電磁波が伝搬できる条件は $n_\pm^2 > 0$，すなわち波数 $k_\pm$ が実数になることです。

右回り（$+$）の円偏光では，$0 < \omega < \omega_c$ の周波数帯において $\omega - \omega_c < 0$ となります。このとき次が成り立ちます。

$$
\begin{aligned}
n_+^2 &= 1 - \frac{\omega_p^2}{\omega(\omega - \omega_c)} \\
&= 1 + \frac{\omega_p^2}{\omega(\omega_c - \omega)} \\
&> 1
\end{aligned}
$$

よって $0 < \omega < \omega_c$ では $\omega < \omega_p$ であっても常に $n_+^2 > 0$ となり，右回りの円偏光は電離層を伝搬できます。なお，左回り（$-$）の円偏光についても，$n_-^2 > 0$ となる条件 $\omega(\omega + \omega_c) > \omega_p^2$ は $\omega > \dfrac{-\omega_c + \sqrt{\omega_c^2 + 4\omega_p^2}}{2}$ を与えます。この下限は $\omega_p$ より小さいため，左回りでも $\dfrac{-\omega_c + \sqrt{\omega_c^2 + 4\omega_p^2}}{2} < \omega < \omega_p$ の範囲では伝搬できますが，どれほど低い周波数でも $\omega < \omega_c$ である限り伝搬できるのは右回り円偏光だけです。

<aside class="rigor-note" markdown>
C.G.S. ガウス単位系を用いた場合，(1) と (3) の電気伝導度 $\sigma$ の表式自体は $\dfrac{i n e^2}{m\omega}$ および $\dfrac{i n e^2}{m(\omega \mp \omega_c)}$ で同じ形になります。波動方程式では $k^2 = \dfrac{\omega^2}{c^2} + \dfrac{4\pi i\omega\sigma}{c^2}$ となり，$\omega_p = \sqrt{\dfrac{4\pi n e^2}{m}}$ と $\omega_c = \dfrac{eB_0}{mc}$ を用いることで (2) と (4) の分散関係と屈折率は同じ式になります。また，$z = 0$ で $\operatorname{Re}\bigl[e^{-i\omega t}(\hat{\mathbf{x}} + i\hat{\mathbf{y}})\bigr] = \cos(\omega t)\,\hat{\mathbf{x}} + \sin(\omega t)\,\hat{\mathbf{y}}$ は $+\hat{\mathbf{z}}$ 軸のまわりに右ねじの向きに回転し，磁場 $\mathbf{B}_0 = B_0\hat{\mathbf{z}}$ 中の負電荷の電子のサイクロトロン回転と同じ向きになるため，右回り偏光が $\omega = \omega_c$ で共鳴します。
</aside>
