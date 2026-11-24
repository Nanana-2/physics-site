---
title: 東大理物 平成26年度 物理第3問：誘電体・導体境界面での電磁波の反射と抵抗損失
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成26年度
exam_subject: 専門科目（物理学）
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成26年度 物理第3問：誘電体・導体境界面での電磁波の反射と抵抗損失

## 問題

媒質中の Maxwell 方程式は以下のように表される。

$$
\begin{aligned}
\nabla \cdot \boldsymbol{D} &= \rho \tag{1} \\
\nabla \cdot \boldsymbol{B} &= 0 \tag{2} \\
\nabla \times \boldsymbol{E} &= -\frac{\partial \boldsymbol{B}}{\partial t} \tag{3} \\
\nabla \times \boldsymbol{H} &= \boldsymbol{j} + \frac{\partial \boldsymbol{D}}{\partial t} \tag{4}
\end{aligned}
$$

ここで $\rho$ および $\boldsymbol{j}$ は真電荷密度および真電流密度であり，原子や分子に束縛された電荷の寄与や変位電流は含まない。以下では線形応答する一様で等方的な媒質中の電磁場を考える。その場合，スカラー定数 $\epsilon$（誘電率），$\mu$（透磁率），および $\sigma$（電気伝導度）を用いて，$\boldsymbol{D} = \epsilon \boldsymbol{E}$，$\boldsymbol{H} = \boldsymbol{B} / \mu$，$\boldsymbol{j} = \sigma \boldsymbol{E}$ と書ける。誘電体中では $\epsilon = \epsilon_{\mathrm{d}}$（実数），$\sigma = 0$ とし，導体中では $\epsilon = \epsilon_{\mathrm{m}}$（実数），$\sigma = \sigma_{\mathrm{m}}$（実数）とする。透磁率はいずれの媒質中でも $\mu_0$（実数）とする。必要であれば，任意のベクトル $\boldsymbol{V}$ についての公式 $\nabla \times (\nabla \times \boldsymbol{V}) = \nabla(\nabla \cdot \boldsymbol{V}) - \nabla^2 \boldsymbol{V}$ を使ってよい。

(1) 全領域が誘電体で満たされている場合を考える。この媒質中を $+z$ 方向に伝搬する平面電磁波の電場は，複素表示を用いて $\boldsymbol{E}_0 \exp(ikz - i\omega t)$ と表される。（ただし物理量はその実部で表される。）この形の有限振幅の波が存在するための条件を $\omega$ と $k$ の間の関係式として示せ。またこの波の位相速度を求めよ。

(2) 全領域が導体で満たされている場合を考える。この媒質中で波の伝搬を表す $\boldsymbol{E}$ に関する方程式を $\boldsymbol{B}$ を使わずに表せ。

以下では誘電体が $z < 0$ の領域を，導体が $z > 0$ の領域を満たしている場合を考える。$z = -\infty$ から入射してきた，電場が $x$ 方向に偏光した平面電磁波の電場を $\boldsymbol{E}_{\mathrm{i}0} \exp(ikz - i\omega t)$，境界面 $z = 0$ で反射された波の電場を $\boldsymbol{E}_{\mathrm{r}0} \exp(-ikz - i\omega t)$，$z > 0$ における電場を $\boldsymbol{E}_{\mathrm{m}0} \exp(ik_{\mathrm{m}} z - i\omega t)$ と表す。

(3) (3) 式および (4) 式より，境界面における接続条件を導け。

(4) 設問 2 で求めた方程式より $k_{\mathrm{m}}$ の値を具体的に求め，$z > 0$ における電場の解（エネルギー保存則を満たすもの）を書き表せ。ただし導体内では (4) 式の右辺第 2 項（変位電流）は，第 1 項（真電流）に比べ十分小さいとし，無視してよい。

(5) 反射電力の入射電力に対する割合（電力反射率）を，微小量 $\sqrt{\omega \epsilon_{\mathrm{d}} / \sigma_{\mathrm{m}}}$ の 1 次までの近似で求めよ。

(6) 導体内における $xy$ 面上単位面積当たりの抵抗損失電力 $\left\langle \int_0^\infty \boldsymbol{j} \cdot \boldsymbol{E}\,\mathrm{d}z \right\rangle$（ただし $\langle \ \rangle$ は時間平均を表す）を $\sqrt{\omega \epsilon_{\mathrm{d}} / \sigma_{\mathrm{m}}}$ の 1 次までの近似で求め，その $xy$ 面上単位面積当たりの入射電力に対する割合を表せ。

> 出典：[東京大学大学院理学系研究科物理学専攻](https://www.phys.s.u-tokyo.ac.jp/) 平成26年度修士課程入学試験問題 物理学 第3問（Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。）

---

## 解答・解説

※ 本解答・解説は非公式であり，大学当局とは無関係です。

### 考え方

誘電体と良導体の境界面に垂直入射する平面電磁波を扱い，反射率の 1 からのずれと導体内部のジュール熱損失が一致することを確かめる問題です。良導体中では変位電流を無視することができ，波動方程式が拡散方程式型になって複素波数 $k_{\mathrm{m}}$ が表皮深さ $\delta$ による指数減衰をもたらします。

境界条件から反射係数と透過係数を比 $k / k_{\mathrm{m}} \propto \sqrt{\omega \epsilon_{\mathrm{d}} / \sigma_{\mathrm{m}}}$ で展開すると，電力反射率 $R$ の低下分 $1 - R$ がちょうど導体内での抵抗損失電力の入射電力に対する比と一致し，エネルギー保存則が明快に検証される。

### 解答

#### (1) 誘電体中の分散関係と位相速度

誘電体中（$\epsilon = \epsilon_{\mathrm{d}}$，$\sigma = 0$，$\mu = \mu_0$，真電荷 $\rho = 0$）では，(1) 式より $\nabla \cdot \boldsymbol{E} = 0$ である。(3) 式の回転をとり，(4) 式 $\nabla \times \boldsymbol{B} = \mu_0 \epsilon_{\mathrm{d}}\dfrac{\partial \boldsymbol{E}}{\partial t}$ を代入すると，

$$
\begin{aligned}
\nabla \times (\nabla \times \boldsymbol{E}) &= -\frac{\partial}{\partial t}(\nabla \times \boldsymbol{B}) = -\mu_0 \epsilon_{\mathrm{d}}\frac{\partial^2 \boldsymbol{E}}{\partial t^2} \\
\nabla(\nabla \cdot \boldsymbol{E}) - \nabla^2 \boldsymbol{E} &= -\mu_0 \epsilon_{\mathrm{d}}\frac{\partial^2 \boldsymbol{E}}{\partial t^2} \\
\nabla^2 \boldsymbol{E} &= \mu_0 \epsilon_{\mathrm{d}}\frac{\partial^2 \boldsymbol{E}}{\partial t^2}
\end{aligned}
$$

を得る。ここに $\boldsymbol{E} = \boldsymbol{E}_0 \exp(ikz - i\omega t)$ を代入すると，

$$
\left(-k^2 + \mu_0 \epsilon_{\mathrm{d}} \omega^2\right)\boldsymbol{E}_0 = \boldsymbol{0}
$$

となる（また $\nabla \cdot \boldsymbol{E} = ik E_{0z} e^{i(kz-\omega t)} = 0$ より横波条件 $E_{0z} = 0$ を満たす）。有限振幅 $\boldsymbol{E}_0 \neq \boldsymbol{0}$ の波が存在するための条件は

$$
k^2 = \mu_0 \epsilon_{\mathrm{d}} \omega^2
$$

であり，$+z$ 方向に伝搬する波（$\omega > 0$，$k > 0$）については $\omega = \dfrac{k}{\sqrt{\mu_0 \epsilon_{\mathrm{d}}}}$ である。したがって，この波の位相速度 $v_{\mathrm{p}}$ は

$$
v_{\mathrm{p}} = \frac{\omega}{k} = \frac{1}{\sqrt{\mu_0 \epsilon_{\mathrm{d}}}}
$$

となる。

$$
\finalanswer{\omega^2 = \frac{k^2}{\mu_0 \epsilon_{\mathrm{d}}}\quad \left(\omega = \frac{k}{\sqrt{\mu_0 \epsilon_{\mathrm{d}}}}\right), \qquad v_{\mathrm{p}} = \frac{1}{\sqrt{\mu_0 \epsilon_{\mathrm{d}}}}}
$$

#### (2) 導体中の電場の方程式

導体中（$\epsilon = \epsilon_{\mathrm{m}}$，$\sigma = \sigma_{\mathrm{m}}$，$\mu = \mu_0$）では，(4) 式は $\nabla \times \boldsymbol{B} = \mu_0 \sigma_{\mathrm{m}}\boldsymbol{E} + \mu_0 \epsilon_{\mathrm{m}}\dfrac{\partial \boldsymbol{E}}{\partial t}$ となる。(3) 式の回転をとってこれを代入すると，

$$
\begin{aligned}
\nabla \times (\nabla \times \boldsymbol{E}) &= -\frac{\partial}{\partial t}(\nabla \times \boldsymbol{B}) \\
\nabla(\nabla \cdot \boldsymbol{E}) - \nabla^2 \boldsymbol{E} &= -\mu_0 \sigma_{\mathrm{m}}\frac{\partial \boldsymbol{E}}{\partial t} - \mu_0 \epsilon_{\mathrm{m}}\frac{\partial^2 \boldsymbol{E}}{\partial t^2}
\end{aligned}
$$

となる。さらに，(4) 式の発散と (1) 式から得られる電荷保存則 $\dfrac{\partial \rho}{\partial t} + \nabla \cdot \boldsymbol{j} = 0$ に $\boldsymbol{j} = \sigma_{\mathrm{m}}\boldsymbol{E} = \dfrac{\sigma_{\mathrm{m}}}{\epsilon_{\mathrm{m}}}\boldsymbol{D}$ を用いると，

$$
\frac{\partial \rho}{\partial t} + \frac{\sigma_{\mathrm{m}}}{\epsilon_{\mathrm{m}}}\rho = 0 \implies \rho(\boldsymbol{r}, t) = \rho(\boldsymbol{r}, 0) e^{-(\sigma_{\mathrm{m}} / \epsilon_{\mathrm{m}}) t}
$$

となり，一様な導体内の真電荷密度は緩和時間 $\epsilon_{\mathrm{m}} / \sigma_{\mathrm{m}}$ で速やかに減衰するため，定常的な波動場では $\rho = 0$ すなわち $\nabla \cdot \boldsymbol{E} = 0$ である。以上より，$\boldsymbol{E}$ に関する方程式は

$$
\finalanswer{\nabla^2 \boldsymbol{E} - \mu_0 \epsilon_{\mathrm{m}}\frac{\partial^2 \boldsymbol{E}}{\partial t^2} - \mu_0 \sigma_{\mathrm{m}}\frac{\partial \boldsymbol{E}}{\partial t} = \boldsymbol{0}}
$$

となる。

#### (3) 境界面 $z = 0$ における接続条件

境界面 $z = 0$ をまたぎ，境界面に平行な辺の長さ $\ell$，垂直な辺の長さ $h$ を持つ微小な長方形閉路 $C$（囲む面を $S$ とする）を考える。(3) 式および (4) 式の両辺を面 $S$ 上で面積分し，ストークスの定理を用いると，

$$
\oint_C \boldsymbol{E} \cdot \mathrm{d}\boldsymbol{l} = -\int_S \frac{\partial \boldsymbol{B}}{\partial t}\cdot \mathrm{d}\boldsymbol{S}, \qquad \oint_C \boldsymbol{H} \cdot \mathrm{d}\boldsymbol{l} = \int_S \left(\boldsymbol{j} + \frac{\partial \boldsymbol{D}}{\partial t}\right)\cdot \mathrm{d}\boldsymbol{S}
$$

となる。ここで $\ell$ を固定して $h \to 0$ の極限をとる。導体は有限の電気伝導度 $\sigma_{\mathrm{m}}$ を持つため $\boldsymbol{j} = \sigma_{\mathrm{m}}\boldsymbol{E}$ は有限であり，境界面に面電流は流れない。また $\dfrac{\partial \boldsymbol{B}}{\partial t}$ および $\dfrac{\partial \boldsymbol{D}}{\partial t}$ も有限であるため，いずれの右辺の面積分も $h \to 0$ で $0$ に収束する。したがって，電場および磁場の境界面に平行な成分（接線成分）$\boldsymbol{E}_{\parallel}$，$\boldsymbol{H}_{\parallel}$ は $z = 0$ で連続である。透磁率は両媒質とも $\mu_0$ なので，$\boldsymbol{B}_{\parallel}$ も連続である。

今，電場は $x$ 方向を向いており，各波の磁場は (3) 式 $\nabla \times \boldsymbol{E} = i\omega \boldsymbol{B}$ より $y$ 方向を向く。具体的には $E_x$ 成分に対して $B_y = \dfrac{1}{i\omega}\dfrac{\partial E_x}{\partial z}$ であるから，入射波・反射波・透過波の磁場振幅はそれぞれ $\dfrac{k}{\omega}E_{\mathrm{i}0}$，$-\dfrac{k}{\omega}E_{\mathrm{r}0}$，$\dfrac{k_{\mathrm{m}}}{\omega}E_{\mathrm{m}0}$ となる。よって $z = 0$ での接続条件は次のように与えられる。

$$
E_{\mathrm{i}0} + E_{\mathrm{r}0} = E_{\mathrm{m}0}, \qquad k(E_{\mathrm{i}0} - E_{\mathrm{r}0}) = k_{\mathrm{m}} E_{\mathrm{m}0}
$$

#### (4) 導体中の波数 $k_{\mathrm{m}}$ と電場の解

導体内で変位電流を無視すると，(2) で求めた方程式は

$$
\nabla^2 \boldsymbol{E} = \mu_0 \sigma_{\mathrm{m}}\frac{\partial \boldsymbol{E}}{\partial t}
$$

となる。ここに $\boldsymbol{E} = \boldsymbol{E}_{\mathrm{m}0} \exp(i k_{\mathrm{m}} z - i\omega t)$ を代入すると，

$$
-k_{\mathrm{m}}^2 = -i\omega \mu_0 \sigma_{\mathrm{m}} \implies k_{\mathrm{m}}^2 = i\omega \mu_0 \sigma_{\mathrm{m}} = \omega \mu_0 \sigma_{\mathrm{m}} e^{i\pi/2}
$$

を得る。平方根をとると $k_{\mathrm{m}} = \pm(1 + i)\sqrt{\dfrac{\omega \mu_0 \sigma_{\mathrm{m}}}{2}}$ となる。

$z > 0$ の領域で $z \to +\infty$ において電場が発散せずエネルギー保存則を満たすためには，$\operatorname{Im}(k_{\mathrm{m}}) > 0$（減衰解）を選ばなければならない。したがって，正符号をとって

$$
k_{\mathrm{m}} = (1 + i)\sqrt{\frac{\omega \mu_0 \sigma_{\mathrm{m}}}{2}}
$$

と定まる。表皮深さ $\delta \equiv \sqrt{\dfrac{2}{\omega \mu_0 \sigma_{\mathrm{m}}}}$ を導入すると $k_{\mathrm{m}} = \dfrac{1 + i}{\delta}$ であり，$z > 0$ における電場の解は

$$
\boldsymbol{E}(z, t) = \boldsymbol{E}_{\mathrm{m}0}\exp\!\left(-\frac{z}{\delta}\right)\exp\!\left[i\!\left(\frac{z}{\delta} - \omega t\right)\right]
$$

と表される。なお，(3) の接続条件より振幅は $\boldsymbol{E}_{\mathrm{m}0} = \dfrac{2k}{k + k_{\mathrm{m}}}\boldsymbol{E}_{\mathrm{i}0}$ である。

$$
\finalanswer{k_{\mathrm{m}} = (1 + i)\sqrt{\frac{\omega \mu_0 \sigma_{\mathrm{m}}}{2}}, \qquad \boldsymbol{E}(z, t) = \boldsymbol{E}_{\mathrm{m}0}\exp\!\left(-\sqrt{\frac{\omega \mu_0 \sigma_{\mathrm{m}}}{2}}\,z\right)\exp\!\left[i\!\left(\sqrt{\frac{\omega \mu_0 \sigma_{\mathrm{m}}}{2}}\,z - \omega t\right)\right]}
$$

#### (5) 電力反射率の近似計算

(3) の接続条件より，振幅反射率 $r = \dfrac{E_{\mathrm{r}0}}{E_{\mathrm{i}0}}$ は

$$
r = \frac{k - k_{\mathrm{m}}}{k + k_{\mathrm{m}}} = -\frac{1 - k/k_{\mathrm{m}}}{1 + k/k_{\mathrm{m}}}
$$

となる。微小量 $\eta \equiv \sqrt{\dfrac{\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}} \ll 1$ を用いて比 $\dfrac{k}{k_{\mathrm{m}}}$ を計算すると，$k = \omega\sqrt{\mu_0 \epsilon_{\mathrm{d}}}$ より

$$
\frac{k}{k_{\mathrm{m}}}
= \frac{\omega\sqrt{\mu_0 \epsilon_{\mathrm{d}}}}{(1 + i)\sqrt{\omega \mu_0 \sigma_{\mathrm{m}} / 2}}
= \frac{\sqrt{2}}{1 + i}\sqrt{\frac{\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}
= \frac{1 - i}{\sqrt{2}}\,\eta
$$

となる。入射波と反射波は同一の誘電体中を伝搬するため，電力反射率 $R$ は $R = |r|^2$ で与えられる。これを $\eta$ の 1 次まで展開すると，

$$
\begin{aligned}
R &= \left|\frac{1 - \dfrac{1 - i}{\sqrt{2}}\eta}{1 + \dfrac{1 - i}{\sqrt{2}}\eta}\right|^2
= \frac{\left(1 - \dfrac{\eta}{\sqrt{2}}\right)^2 + \left(\dfrac{\eta}{\sqrt{2}}\right)^2}{\left(1 + \dfrac{\eta}{\sqrt{2}}\right)^2 + \left(\dfrac{\eta}{\sqrt{2}}\right)^2} \\
&= \frac{1 - \sqrt{2}\,\eta + \eta^2}{1 + \sqrt{2}\,\eta + \eta^2}
= \left(1 - \sqrt{2}\,\eta + O(\eta^2)\right)\left(1 - \sqrt{2}\,\eta + O(\eta^2)\right) \\
&\simeq 1 - 2\sqrt{2}\,\eta
= 1 - 2\sqrt{\frac{2\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}
\end{aligned}
$$

となる。

$$
\finalanswer{R \simeq 1 - 2\sqrt{\frac{2\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}}
$$

#### (6) 導体内の抵抗損失電力と入射電力に対する割合

複素表示で表された単色場 $\boldsymbol{j} = \sigma_{\mathrm{m}}\boldsymbol{E}$ に対して，時間平均は $\langle \boldsymbol{j} \cdot \boldsymbol{E} \rangle = \dfrac{1}{2}\operatorname{Re}(\boldsymbol{j}^* \cdot \boldsymbol{E}) = \dfrac{1}{2}\sigma_{\mathrm{m}}|\boldsymbol{E}|^2$ で与えられる。よって導体内の $xy$ 面上単位面積当たりの抵抗損失電力 $P_{\mathrm{loss}}$ は，(4) の電場解（$\delta = \sqrt{\dfrac{2}{\omega \mu_0 \sigma_{\mathrm{m}}}}$）を用いて

$$
\begin{aligned}
P_{\mathrm{loss}}
&= \left\langle \int_0^\infty \boldsymbol{j} \cdot \boldsymbol{E}\,\mathrm{d}z \right\rangle
= \frac{1}{2}\sigma_{\mathrm{m}} |E_{\mathrm{m}0}|^2 \int_0^\infty e^{-2z/\delta}\,\mathrm{d}z \\
&= \frac{1}{4}\sigma_{\mathrm{m}} \delta |E_{\mathrm{m}0}|^2
\end{aligned}
$$

となる。ここで $E_{\mathrm{m}0} = \dfrac{2k}{k + k_{\mathrm{m}}}E_{\mathrm{i}0} = \dfrac{2(k/k_{\mathrm{m}})}{1 + k/k_{\mathrm{m}}}E_{\mathrm{i}0}$ と $\left|\dfrac{k}{k_{\mathrm{m}}}\right|^2 = \eta^2 = \dfrac{\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}$ を用いると，

$$
|E_{\mathrm{m}0}|^2
= \frac{4\eta^2}{1 + \sqrt{2}\,\eta + \eta^2}|E_{\mathrm{i}0}|^2
= 4\eta^2\left(1 + O(\eta)\right)|E_{\mathrm{i}0}|^2
$$

である。これを $P_{\mathrm{loss}}$ に代入して $\eta = \sqrt{\dfrac{\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}$ の 1 次まで求めると，

$$
\begin{aligned}
P_{\mathrm{loss}}
&\simeq \frac{1}{4}\sigma_{\mathrm{m}}\sqrt{\frac{2}{\omega \mu_0 \sigma_{\mathrm{m}}}}\cdot 4\frac{\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}|E_{\mathrm{i}0}|^2 \\
&= \sqrt{\frac{\epsilon_{\mathrm{d}}}{\mu_0}}\sqrt{\frac{2\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}\,|E_{\mathrm{i}0}|^2
\end{aligned}
$$

となる。

一方，$xy$ 面上単位面積当たりの入射電力 $P_{\mathrm{i}}$ は入射波のポインティングベクトルの $z$ 成分の時間平均であり，

$$
P_{\mathrm{i}}
= \frac{1}{2}\operatorname{Re}\!\left(\boldsymbol{E}_{\mathrm{i}} \times \boldsymbol{H}_{\mathrm{i}}^*\right)_z
= \frac{1}{2}\frac{k}{\omega \mu_0}|E_{\mathrm{i}0}|^2
= \frac{1}{2}\sqrt{\frac{\epsilon_{\mathrm{d}}}{\mu_0}}\,|E_{\mathrm{i}0}|^2
$$

で与えられる。したがって，抵抗損失電力の入射電力に対する割合は

$$
\frac{P_{\mathrm{loss}}}{P_{\mathrm{i}}}
\simeq \frac{\sqrt{\epsilon_{\mathrm{d}} / \mu_0}\sqrt{2\omega \epsilon_{\mathrm{d}} / \sigma_{\mathrm{m}}}\,|E_{\mathrm{i}0}|^2}{\dfrac{1}{2}\sqrt{\epsilon_{\mathrm{d}} / \mu_0}\,|E_{\mathrm{i}0}|^2}
= 2\sqrt{\frac{2\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}
$$

となる。

$$
\finalanswer{P_{\mathrm{loss}} \simeq \sqrt{\frac{\epsilon_{\mathrm{d}}}{\mu_0}}\sqrt{\frac{2\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}\,|E_{\mathrm{i}0}|^2, \qquad \frac{P_{\mathrm{loss}}}{P_{\mathrm{i}}} \simeq 2\sqrt{\frac{2\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}}
$$

<aside class="rigor-note" markdown>
**補足**：(5) と (6) の結果を足し合わせると $R + \dfrac{P_{\mathrm{loss}}}{P_{\mathrm{i}}} = 1$ となり，入射エネルギーが反射波と導体内のジュール熱損失に過不足なく分配されていることが確認できる。(5) で得られた電力反射率の近似式 $R \simeq 1 - 2\sqrt{\dfrac{2\omega \epsilon_{\mathrm{d}}}{\sigma_{\mathrm{m}}}}$ は**ハーゲン・ルーベンスの関係式**（Hagen–Rubens relation）と呼ばれ，赤外線などの低周波領域における金属の反射率をよく記述する。
</aside>
