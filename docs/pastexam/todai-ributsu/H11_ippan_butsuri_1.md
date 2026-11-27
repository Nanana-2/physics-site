---
title: 東大理物 平成11年度 一般教育科目 物理学 第1問：クーロン力による荷電粒子の散乱と最近接距離
tags:
  - 院試過去問
  - 東大理物
  - 力学
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 一般教育科目 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成11年度 一般教育科目 物理学 第1問：クーロン力による荷電粒子の散乱と最近接距離

## 問題

電荷 $+Ze$ を持つ非常に重い原子核に向かって，質量 $m$，電荷 $q$ の荷電粒子が初速度 $v_0$ を持って無限遠から衝突パラメータ（無限遠での粒子の運動方向を延長して得られる直線と標的（ここでは原子核）との距離）$b$ で近づくとき，次の問いに答えよ。ただし，粒子間にはクーロン力のみが働くものとし，原子核の反跳は無視する。また，クーロンの法則の比例定数は $k$ とせよ。
{: .problem-lead }

<figure class="problem-figure" markdown>
![クーロン散乱の設定図](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_1-p-light.svg#only-light){ loading=lazy }
![クーロン散乱の設定図](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_1-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) 荷電粒子の描く軌道を，衝突パラメータ $b$ が大きい場合と小さい場合（ただし $b > 0$），および $q$ の符号が正と負の場合，計四つの組み合わせについて，同一の図の中に定性的に描け。

(2) 荷電粒子が持つ原子核の周りの角運動量 $\mathbf{L}$ を，原子核を原点とする荷電粒子の位置ベクトル $\mathbf{r}$ を用いて表わせ。

(3) $\mathbf{L}$ が保存することを示せ。

(4) 衝突パラメータが $b$ であるとき，$\mathbf{L}$ の大きさを求めよ。

(5) 軌道上で荷電粒子が原子核に最も近づく点における粒子間の距離を $s$ とするとき，この点における荷電粒子の速さ $v_s$ はどう表わされるか。

(6) $q = +e$ とするとき，$s$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 一般教育科目 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
固定された原子核がつくるクーロン場中の荷電粒子の運動は，中心力による双曲線散乱です。まず斥力と引力，および衝突パラメータの大小に応じた4通りの軌道を定性的に描きます。

続いて中心力による角運動量保存則と力学的エネルギー保存則を定式化し，最近接点では速度が動径ベクトルに直交することを利用して，最近接点での速さ $v_s$ と最近接距離 $s$ を導出します。
</div>

### (1)

原子核の電荷は $+Ze > 0$ であるため，$q > 0$ のときは斥力が働いて粒子は原子核から遠ざかる向きに曲げられ，$q < 0$ のときは引力が働いて粒子は原子核側へ引き寄せられる向きに曲げられます。また，衝突パラメータ $b$ が小さいほど粒子は原子核の近くを通って強いクーロン力を受けるため，散乱角が大きくなります。

以上4通りの組み合わせ（(1) $q > 0$・$b$ 大，(2) $q > 0$・$b$ 小，(3) $q < 0$・$b$ 大，(4) $q < 0$・$b$ 小）を同一の図に定性的に描くと次のようになります。

![荷電粒子の散乱軌道の定性的な図](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_1-s-light.svg#only-light){ loading=lazy }
![荷電粒子の散乱軌道の定性的な図](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_1-s-dark.svg#only-dark){ loading=lazy }

### (2)

原子核を原点とする荷電粒子の位置ベクトルを $\mathbf{r}$，速度ベクトルを $\mathbf{v} = \dfrac{\mathrm{d}\mathbf{r}}{\mathrm{d}t}$ とすると，運動量は $\mathbf{p} = m\mathbf{v}$ です。したがって原子核の周りの角運動量 $\mathbf{L}$ は次のように表されます。

$$
\finalanswer{\mathbf{L} = \mathbf{r} \times m\frac{\mathrm{d}\mathbf{r}}{\mathrm{d}t}}
$$

### (3)

角運動量 $\mathbf{L} = \mathbf{r} \times m\mathbf{v}$ を時刻 $t$ で微分します。

$$
\begin{aligned}
\frac{\mathrm{d}\mathbf{L}}{\mathrm{d}t} &= \frac{\mathrm{d}\mathbf{r}}{\mathrm{d}t} \times m\mathbf{v} + \mathbf{r} \times m\frac{\mathrm{d}\mathbf{v}}{\mathrm{d}t} \\
&= \mathbf{v} \times m\mathbf{v} + \mathbf{r} \times \mathbf{F}
\end{aligned}
$$

ここで運動方程式 $m\dfrac{\mathrm{d}\mathbf{v}}{\mathrm{d}t} = \mathbf{F}$ を用いました。第1項は同一ベクトルの外積なので $\mathbf{v} \times m\mathbf{v} = \mathbf{0}$ です。

また荷電粒子に働くクーロン力 $\mathbf{F}$ は，原子核からの距離 $r = |\mathbf{r}|$ を用いて

$$
\mathbf{F} = \frac{kZeq}{r^3}\mathbf{r}
$$

と表される中心力であり，$\mathbf{r}$ と平行です。したがって第2項の力のモーメントも $\mathbf{r} \times \mathbf{F} = \mathbf{0}$ となります。

$$
\frac{\mathrm{d}\mathbf{L}}{\mathrm{d}t} = \mathbf{0}
$$

よって，角運動量 $\mathbf{L}$ は時間によらず保存します。

### (4)

(3) より角運動量 $\mathbf{L}$ は軌道上のすべての点で一定なので，無限遠での値を用いて大きさ $L = |\mathbf{L}|$ を計算します。

無限遠で荷電粒子が速度 $\mathbf{v}_0$ で直線運動しているとき，原子核から粒子の位置ベクトル $\mathbf{r}$ に下ろした垂線の長さ，すなわち $\mathbf{r}$ と $\mathbf{v}_0$ のなす角を $\theta$ としたときの $r\sin\theta$ は，定義より衝突パラメータ $b$ に等しくなります。

$$
\begin{aligned}
L &= |\mathbf{r} \times m\mathbf{v}_0| \\
&= m v_0 r \sin\theta \\
&= m v_0 b
\end{aligned}
$$

$$
\finalanswer{L = mv_0 b}
$$

### (5)

荷電粒子が原子核に最も近づく点では，原子核からの距離 $r(t)$ が極小となるため，動径方向の速度成分は $\dfrac{\mathrm{d}r}{\mathrm{d}t} = 0$ です。したがって，最近接点では速度ベクトル $\mathbf{v}_s$ と位置ベクトル $\mathbf{r}_s$ は互いに直交します。

この点における角運動量の大きさは $L = m v_s s$ となります。(3) と (4) の角運動量保存則より，次式が成り立ちます。

$$
m v_s s = m v_0 b
$$

両辺を $ms$ で割って $v_s$ を求めます。

$$
\finalanswer{v_s = \frac{b}{s}v_0}
$$

### (6)

クーロン力は保存力なので，力学的エネルギーが保存します。無限遠では静電ポテンシャルエネルギーが $0$ であり，荷電粒子の速さは $v_0$ です。$q = +e$ のとき，最近接点（距離 $s$，速さ $v_s$）での静電ポテンシャルエネルギーは $\dfrac{kZe^2}{s}$ となるため，エネルギー保存則は次の通りです。

$$
\frac{1}{2}m v_0^2 = \frac{1}{2}m v_s^2 + \frac{kZe^2}{s}
$$

ここに (5) で求めた $v_s = \dfrac{b}{s}v_0$ を代入します。

$$
\frac{1}{2}m v_0^2 = \frac{1}{2}m v_0^2 \frac{b^2}{s^2} + \frac{kZe^2}{s}
$$

両辺に $\dfrac{2s^2}{m v_0^2}$ を掛けて $s$ に関する2次方程式に整理します。

$$
s^2 - \frac{2kZe^2}{m v_0^2}s - b^2 = 0
$$

解の公式を用いて $s$ を求めます。

$$
s = \frac{kZe^2}{m v_0^2} \pm \sqrt{\left(\frac{kZe^2}{m v_0^2}\right)^2 + b^2}
$$

$s > 0$ および $b > 0$ より，負の符号は不適であるため正の符号をとります。

$$
\finalanswer{s = \frac{kZe^2}{m v_0^2} + \sqrt{\left(\frac{kZe^2}{m v_0^2}\right)^2 + b^2}}
$$
