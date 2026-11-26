---
title: 東大理物 平成14年度 物理学 第4問：逆さ円錐漏斗面上の質点の運動と有効ポテンシャル
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成14年度
exam_subject: 物理学
exam_number: 第4問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成14年度 物理学 第4問：逆さ円錐漏斗面上の質点の運動と有効ポテンシャル

## 問題

図のように頂角が $\alpha$ の円錐を切り，鉛直軸に沿って逆さにして作った漏斗状の滑らかな面がある。切り口の高さを $h$ として，この斜面上の質量 $m$ の質点の運動を考える。以下の問に，解答に至る筋道を添えて答えよ。
{: .problem-lead }

(1) 鉛直方向に $z$ 軸をとり，質点の座標を円柱座標 $(z, \theta)$ で表したとき，質点の斜面上の運動のラグランジアンを求めよ。ただし，重力の加速度定数を $g$ とする。

(2) この系の保存量を求めよ。

(3) 質点が高さ $2h$ の斜面上で水平に初速度 $v_0$ で運動を始めたとする。初速度の違いによる質点の運動の違いについて述べよ。

<figure class="problem-figure" markdown>
![高さhで切り口をもつ逆さ円錐の滑らかな斜面](../../../docs/assets/figures/pastexam-todai-ributsu/H14_butsuri_4-p-light.svg#only-light)
![高さhで切り口をもつ逆さ円錐の滑らかな斜面](../../../docs/assets/figures/pastexam-todai-ributsu/H14_butsuri_4-p-dark.svg#only-dark)
<figcaption markdown="span">図1：切り口の高さ $h$，半頂角 $\alpha$ の逆さ円錐漏斗面と，高さ $2h$ で水平初速度 $v_0$ を与えられた質点。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成14年度 物理学 第4問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
円錐面上の束縛条件を円柱座標で表してラグランジアンを作ると，方位角 $\theta$ が循環座標となり，$z$ 軸まわりの角運動量と力学的エネルギーが保存量として得られます。

角運動量保存則を用いて $\dot{\theta}$ を消去すると，高さ $z$ に関する1次元の有効ポテンシャルが得られます。初期条件 $z = 2h$ におけるエネルギーと有効ポテンシャルの交点である折り返し点の位置を切り口の高さ $h$ および $2h$ と比べることで，初速度 $v_0$ に応じた運動の分類ができます。
</div>

### (1)

図に従い，円錐の頂点を原点とし，$z$ 軸と円錐の母線がなす半頂角を $\alpha$ とします。円柱座標の動径距離 $\rho$ は斜面の拘束条件より $\rho = z\tan\alpha$ です。時間微分すると $\dot{\rho} = \dot{z}\tan\alpha$ となります。

質点の速度の2乗 $v^2 = \dot{\rho}^2 + \rho^2\dot{\theta}^2 + \dot{z}^2$ を $(z, \theta)$ で表します。

$$
\begin{aligned}
v^2 &= \dot{z}^2\tan^2\alpha + z^2\tan^2\alpha\,\dot{\theta}^2 + \dot{z}^2 \\
&= \bigl(1 + \tan^2\alpha\bigr)\dot{z}^2 + z^2\tan^2\alpha\,\dot{\theta}^2 \\
&= \frac{\dot{z}^2}{\cos^2\alpha} + z^2\tan^2\alpha\,\dot{\theta}^2
\end{aligned}
$$

重力による位置エネルギーは $U = mgz$ なので，ラグランジアン $L = \dfrac{1}{2}mv^2 - U$ は次式となります。

$$
\finalanswer{L = \frac{1}{2}m\left(\frac{\dot{z}^2}{\cos^2\alpha} + z^2\tan^2\alpha\,\dot{\theta}^2\right) - mgz}
$$

### (2)

ラグランジアン $L$ は方位角 $\theta$ を陽に含まないため，$\theta$ に共役な一般化運動量である $z$ 軸まわりの角運動量 $\ell$ が保存します。

$$
\begin{aligned}
\ell &= \frac{\partial L}{\partial\dot{\theta}} \\
&= m z^2\tan^2\alpha\,\dot{\theta}
\end{aligned}
$$

また，$L$ は時間 $t$ を陽に含まず，束縛条件も時間に依存しないため，力学的エネルギー $E$ が保存します。

$$
E = \frac{1}{2}m\left(\frac{\dot{z}^2}{\cos^2\alpha} + z^2\tan^2\alpha\,\dot{\theta}^2\right) + mgz
$$

したがって，この系の保存量は $z$ 軸まわりの角運動量 $\ell$ と力学的エネルギー $E$ の2つです。

$$
\finalanswer{\ell = m z^2\tan^2\alpha\,\dot{\theta}, \qquad E = \frac{1}{2}m\left(\frac{\dot{z}^2}{\cos^2\alpha} + z^2\tan^2\alpha\,\dot{\theta}^2\right) + mgz}
$$

### (3)

初期状態は $z(0) = 2h$，$\dot{z}(0) = 0$，水平速度 $\rho(0)\dot{\theta}(0) = v_0$（$\rho(0) = 2h\tan\alpha$）です。したがって保存量 $\ell = m\rho(0)v_0$ と $E$ の値は次式になります。

$$
\ell = 2mh v_0\tan\alpha, \qquad E = \frac{1}{2}m v_0^2 + 2mgh
$$

$\dot{\theta} = \dfrac{\ell}{m z^2\tan^2\alpha}$ をエネルギー保存則に代入して $\dot{\theta}$ を消去します。

$$
\frac{m}{2\cos^2\alpha}\dot{z}^2 + U_{\mathrm{eff}}(z) = E
$$

ここで $z$ 方向の運動を決める有効ポテンシャル $U_{\mathrm{eff}}(z)$ を計算します。

$$
\begin{aligned}
U_{\mathrm{eff}}(z) &= \frac{\ell^2}{2m z^2\tan^2\alpha} + mgz \\
&= \frac{4m^2 h^2 v_0^2\tan^2\alpha}{2m z^2\tan^2\alpha} + mgz \\
&= \frac{2mh^2 v_0^2}{z^2} + mgz
\end{aligned}
$$

$U_{\mathrm{eff}}(z)$ には角度 $\alpha$ が現れません。$\dot{z}^2 \ge 0$ の条件を整理するために $E - U_{\mathrm{eff}}(z)$ を因数分解します。

$$
\begin{aligned}
E - U_{\mathrm{eff}}(z) &= \frac{1}{2}m v_0^2\left(1 - \frac{4h^2}{z^2}\right) + mg(2h - z) \\
&= \frac{m(z - 2h)}{2z^2}\Bigl\{v_0^2(z + 2h) - 2gz^2\Bigr\} \\
&= -\frac{m(z - 2h)}{2z^2}\bigl(2gz^2 - v_0^2 z - 2h v_0^2\bigr)
\end{aligned}
$$

$v_0 > 0$ のとき，$2gz^2 - v_0^2 z - 2h v_0^2 = 0$ の正の解 $z_1$ を求めます。

$$
z_1 = \frac{v_0^2 + \sqrt{v_0^4 + 16gh v_0^2}}{4g}
$$

$z > 0$ において $E - U_{\mathrm{eff}}(z) \ge 0$ となる範囲は $z = 2h$ と $z = z_1$ の間であり，これが質点の鉛直方向の運動範囲になります。

まず $z_1 = 2h$ となる条件を $2g(2h)^2 - v_0^2(2h) - 2h v_0^2 = 0$ から求めると，$8gh^2 = 4h v_0^2$ すなわち $v_0 = \sqrt{2gh}$ です。

次に折り返し点がちょうど切り口の高さ $h$ に一致する条件 $z_1 = h$ を $2gh^2 - v_0^2 h - 2h v_0^2 = 0$ から求めると，$2gh^2 = 3h v_0^2$ すなわち $v_0 = \sqrt{\dfrac{2}{3}gh}$ です。

なお，質点が斜面から離れずに運動し続ける条件は垂直抗力 $N \ge 0$ ですが，円錐の内側では重力の法線成分 $mg\sin\alpha$ も遠心力の法線成分 $m\rho\dot{\theta}^2\cos\alpha$ もともに斜面へ押し付ける向きにはたらくため，任意の $v_0$ に対して常に $N > 0$ が満たされます。

以上より，初速度 $v_0$ の大きさによって質点の運動は次の5通りに分類されます。

- $0 \le v_0 < \sqrt{\dfrac{2}{3}gh}$ のとき：$z_1 < h$ となり，質点は初期位置 $z = 2h$ から下降し，下向きの速度をもったまま切り口 $z = h$ から外へ落下します。特に $v_0 = 0$ のときは母線に沿ってまっすぐ下り，それ以外では $z$ 軸まわりを回転しながららせん状に下ります。
- $v_0 = \sqrt{\dfrac{2}{3}gh}$ のとき：$z_1 = h$ となり，質点は回転しながら下降して切り口 $z = h$ でちょうど $\dot{z} = 0$ に達します。切り口で落下せず斜面上に残る限界の場合であり，$h \le z \le 2h$ の範囲を上下に振動しながら回転運動を行います。
- $\sqrt{\dfrac{2}{3}gh} < v_0 < \sqrt{2gh}$ のとき：$h < z_1 < 2h$ となり，質点は切り口に達することなく $z = z_1$ で折り返し，$z_1 \le z \le 2h$ の範囲を上下に振動しながら $z$ 軸のまわりを回転し続けます。
- $v_0 = \sqrt{2gh}$ のとき：$z_1 = 2h$ が有効ポテンシャルの極小点に一致するため，質点は高さ $z = 2h$ の水平円周上を一定の速さ $v_0$ で等速円運動します。
- $v_0 > \sqrt{2gh}$ のとき：$z_1 > 2h$ となり，質点は初期位置 $z = 2h$ から上昇して最高点 $z = z_1$ で折り返し，$2h \le z \le z_1$ の範囲を上下に振動しながら $z$ 軸のまわりを回転し続けます。
