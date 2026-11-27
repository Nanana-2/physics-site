---
title: 東大理物 平成10年度 一般教育科目 物理学 第1問：斜面を転がり落ちる剛体の運動と石球・トロッコの衝突判定
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 一般教育科目 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成10年度 一般教育科目 物理学 第1問：斜面を転がり落ちる剛体の運動と石球・トロッコの衝突判定

## 問題

転がり迫る石の球に追われている人がトロッコに乗って逃げるときに，逃げきれるか否かを以下の手順で考察しよう。
{: .problem-lead }

(1) 勾配 $\theta$ の斜面を滑らずに転がり落ちる半径 $r$，質量 $m$，中心のまわりの慣性モーメント $I$ の回転体（円板，球など）の運動を考えよう。重力加速度を $g$，斜面の回転体におよぼす転がりまさつ力を $F$，回転体の回転角を $\alpha$，斜面に沿って測った回転体の中心位置を $x$ とする。回転体の運動は以下の連立方程式によって決定される。回転に関する運動方程式 (ii) を与えて，方程式を完成させよ。

$$
\begin{aligned}
m\ddot{x} &= mg\sin\theta - F \qquad &\text{(i)} \\
&\qquad &\text{(ii)} \\
\dot{x} &= r\dot{\alpha} \qquad &\text{(iii)}
\end{aligned}
$$

但し，$\ddot{\ } \equiv \mathrm{d}^2/\mathrm{d}t^2$，$\dot{\ } \equiv \mathrm{d}/\mathrm{d}t$ である。

(2) 上の方程式 (i)，(ii)，(iii) を用いて回転体の全エネルギー，

$$
E = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}I\dot{\alpha}^2 - mgx\sin\theta
$$

が保存することを確認せよ。

(3) 以下の (a)，(b)，(c) に述べる三物体の運動は，$m, I$ を適当に定義すると，問 (1) の方程式 (i)，(ii)，(iii) に従う。

(a) 一個の車輪を考える。半径は $20\,\mathrm{cm}$，質量は $40\,\mathrm{kg}$ であり，車輪の質量分布は一番外側の輪の部分に集中している円環（リング）であるとする。これが斜面をすべらずに転がり落ちる運動を考える。

(b) トロッコを考える。トロッコを，一つの車輪からなり車軸の上に車台が乗っているものとモデル化する。車輪を (a) で考えた円環とし，それが質量の無視できる円板により車軸とつながっており，車軸にはトロッコの車台の質量とそれに乗った人の質量をあわせた $360\,\mathrm{kg}$ の重量がかかっているとする。車輪は斜面をすべらずに転がり落ちるとし，車軸のまさつは無視する。

(c) 石球を考える。質量 $M = 2.0 \times 10^4\,\mathrm{kg}$，半径 $R = 1.0\,\mathrm{m}$ の石球が斜面をすべらずに転がり落ちるとする。球の中心のまわりの慣性モーメントは $\dfrac{2}{5}MR^2$ で与えられる。

上の (a)，(b)，(c) のそれぞれの物体の，斜面に沿った方向の加速度を $g_a, g_b, g_c$ とする。勾配 $30^\circ$ の斜面を直線状下方に転がる場合に，$g_a : g_b : g_c$ の比を求めよ。

(4) 問 (3) の (b) に述べたトロッコが動き始めた時，石球の中心はトロッコ後端から $6.0\,\mathrm{m}$ のところにあり，秒速 $3.0\,\mathrm{m}$ で迫っていた。トロッコの車高は石球の半径に等しいとすると，石球はトロッコに衝突するかしないかを判定し，後者の場合には約何 $\mathrm{m}$ まで接近するかを計算せよ。計算には $g = 9.8\,\mathrm{m/s^2}$ を用いよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 一般教育科目 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
斜面を滑らずに転がる剛体の並進・回転の運動方程式と拘束条件を連立させ，エネルギー保存則を確認するとともに，慣性モーメントの比率 $\dfrac{I}{mr^2}$ から斜面方向の加速度を統一的に導きます。

(3) では車輪・トロッコ・石球の有効質量と回転慣性を整理して加速度比を求め，(4) ではトロッコと石球の相対加速度から最接近時刻および石球表面とトロッコ後端との最小距離を計算して衝突の有無を判定します。
</div>

### (1)

斜面下向きを $x$ の正の向きとすると，回転体が斜面から受ける摩擦力 $F$ は斜面上向きに働きます。回転体の中心のまわりで，この摩擦力 $F$ は $\alpha$ が増加する回転方向に大きさ $rF$ の力のモーメントを及ぼします。重力および垂直抗力の作用線は中心を通るため，中心まわりの力のモーメントは $0$ です。

したがって，回転に関する運動方程式 (ii) は次の通りです。

$$
\finalanswer{I\ddot{\alpha} = rF}
$$

### (2)

全エネルギー $E = \dfrac{1}{2}m\dot{x}^2 + \dfrac{1}{2}I\dot{\alpha}^2 - mgx\sin\theta$ を時刻 $t$ で微分します。

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = m\dot{x}\ddot{x} + I\dot{\alpha}\ddot{\alpha} - mg\dot{x}\sin\theta
$$

ここに (i) $m\ddot{x} = mg\sin\theta - F$ および (ii) $I\ddot{\alpha} = rF$ を代入します。

$$
\begin{aligned}
\frac{\mathrm{d}E}{\mathrm{d}t} &= \dot{x}(mg\sin\theta - F) + \dot{\alpha}(rF) - mg\dot{x}\sin\theta \\
&= F(r\dot{\alpha} - \dot{x})
\end{aligned}
$$

滑らずに転がる条件 (iii) $\dot{x} = r\dot{\alpha}$ より $r\dot{\alpha} - \dot{x} = 0$ となるため，次式が成り立ちます。

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = 0
$$

よって，全エネルギー $E$ は時間によらず保存することが確認されます。

### (3)

まず一般の回転体の斜面方向の加速度 $\ddot{x}$ を求めます。(iii) を時間微分すると $\ddot{x} = r\ddot{\alpha}$ なので，(ii) より $F = \dfrac{I}{r^2}\ddot{x}$ となります。これを (i) に代入して整理します。

$$
\begin{aligned}
m\ddot{x} &= mg\sin\theta - \frac{I}{r^2}\ddot{x} \\
\ddot{x} &= \frac{g\sin\theta}{1 + \dfrac{I}{mr^2}}
\end{aligned}
$$

この式を3つの物体それぞれに用います。

まず (a) の車輪単体は質量 $m_a = 40\,\mathrm{kg}$，半径 $r_a = 0.20\,\mathrm{m}$ の円環であり，すべての質量が半径 $r_a$ に集中しているため $I_a = m_a r_a^2$，すなわち $\dfrac{I_a}{m_a r_a^2} = 1$ です。したがって加速度 $g_a$ は次の通りです。

$$
\begin{aligned}
g_a &= \frac{1}{1 + 1}g\sin\theta \\
&= \frac{1}{2}g\sin\theta
\end{aligned}
$$

次に (b) のトロッコを考えます。車輪の質量 $m_w = 40\,\mathrm{kg}$ と車台・人の質量 $m_c = 360\,\mathrm{kg}$ を合わせた並進質量は $m_b = 400\,\mathrm{kg}$ です。一方，車軸の摩擦はないため車台と人は回転せず，回転する部分の慣性モーメントは車輪のみの $I_b = m_w r_a^2$ です。よって無次元慣性比は $\dfrac{I_b}{m_b r_a^2} = \dfrac{40}{400}$ すなわち $\dfrac{1}{10}$ となり，加速度 $g_b$ は次の通りです。

$$
\begin{aligned}
g_b &= \frac{1}{1 + 1/10}g\sin\theta \\
&= \frac{10}{11}g\sin\theta
\end{aligned}
$$

最後に (c) の石球は質量 $M$，半径 $R$，慣性モーメント $I_c = \dfrac{2}{5}MR^2$ より $\dfrac{I_c}{MR^2} = \dfrac{2}{5}$ です。したがって加速度 $g_c$ は次の通りです。

$$
\begin{aligned}
g_c &= \frac{1}{1 + 2/5}g\sin\theta \\
&= \frac{5}{7}g\sin\theta
\end{aligned}
$$

以上より，$g_a : g_b : g_c$ の比は斜面角度 $\theta = 30^\circ$ の値によらず次のように求まります。

$$
\begin{aligned}
g_a : g_b : g_c &= \frac{1}{2} : \frac{10}{11} : \frac{5}{7} \\
&= 77 : 140 : 110
\end{aligned}
$$

$$
\finalanswer{g_a : g_b : g_c = 77 : 140 : 110}
$$

### (4)

トロッコが動き始めた時刻を $t = 0$ とし，斜面に沿って下向きに座標をとります。$t = 0$ における石球の中心位置を $0$，トロッコ後端の位置を $x_0 = 6.0\,\mathrm{m}$ とします。

$\theta = 30^\circ$，$\sin 30^\circ = \dfrac{1}{2}$，$g = 9.8\,\mathrm{m/s^2}$ より，トロッコと石球の加速度を求めます。

$$
\begin{aligned}
g_b &= \frac{10}{11} \times 9.8 \times \frac{1}{2} \\
&= \frac{49}{11}\,\mathrm{m/s^2}
\end{aligned}
$$

$$
\begin{aligned}
g_c &= \frac{5}{7} \times 9.8 \times \frac{1}{2} \\
&= \frac{7}{2}\,\mathrm{m/s^2}
\end{aligned}
$$

$g_b > g_c$ なので，トロッコは石球よりも大きな加速度で下ります。相対加速度 $a_{\mathrm{rel}} = g_b - g_c$ を計算します。

$$
\begin{aligned}
a_{\mathrm{rel}} &= \frac{49}{11} - \frac{7}{2} \\
&= \frac{98 - 77}{22} \\
&= \frac{21}{22}\,\mathrm{m/s^2}
\end{aligned}
$$

時刻 $t$ における石球の中心位置は $x_{\mathrm{ball}}(t) = v_0 t + \dfrac{1}{2}g_c t^2$（$v_0 = 3.0\,\mathrm{m/s}$），トロッコ後端の位置は $x_{\mathrm{cart}}(t) = x_0 + \dfrac{1}{2}g_b t^2$ です。したがって石球の中心とトロッコ後端の斜面に沿った距離 $D(t)$ は次式で与えられます。

$$
\begin{aligned}
D(t) &= x_{\mathrm{cart}}(t) - x_{\mathrm{ball}}(t) \\
&= x_0 - v_0 t + \frac{1}{2}a_{\mathrm{rel}} t^2 \\
&= \frac{1}{2}a_{\mathrm{rel}}\left(t - \frac{v_0}{a_{\mathrm{rel}}}\right)^2 + x_0 - \frac{v_0^2}{2a_{\mathrm{rel}}}
\end{aligned}
$$

$D(t)$ が最小となる時刻 $t^*$ を求めます。

$$
\begin{aligned}
t^* &= \frac{v_0}{a_{\mathrm{rel}}} \\
&= \frac{3.0}{21/22} \\
&= \frac{22}{7}\,\mathrm{s}
\end{aligned}
$$

続いてそのときの最小距離 $D_{\min}$ を計算します。

$$
\begin{aligned}
D_{\min} &= 6.0 - \frac{3.0^2}{2 \times (21/22)} \\
&= 6 - \frac{9 \times 11}{21} \\
&= 6 - \frac{33}{7} \\
&= \frac{9}{7}\,\mathrm{m}
\end{aligned}
$$

ここでトロッコの車高が石球の半径 $R = 1.0\,\mathrm{m}$ に等しいため，斜面から高さ $R$ の位置にある石球の最前端がトロッコの後端に接触する条件は $D(t) \le R = 1.0\,\mathrm{m}$ です。

最小値 $D_{\min} = \dfrac{9}{7}\,\mathrm{m} \approx 1.29\,\mathrm{m}$ は $R = 1.0\,\mathrm{m}$ より大きいため，石球はトロッコに衝突しません。

最接近時における石球表面とトロッコ後端との間隔 $d_{\min}$ を求めます。

$$
\begin{aligned}
d_{\min} &= D_{\min} - R \\
&= \frac{9}{7} - 1.0 \\
&= \frac{2}{7}\,\mathrm{m} \\
&\approx 0.29\,\mathrm{m}
\end{aligned}
$$

以上より，石球はトロッコに衝突せず，表面とトロッコ後端との間隔は約 $0.29\,\mathrm{m}$，石球中心とトロッコ後端との距離は約 $1.3\,\mathrm{m}$ まで接近した後に引き離されます。

$$
\finalanswer{d_{\min} = \frac{2}{7}\,\mathrm{m} \approx 0.29\,\mathrm{m},\qquad D_{\min} = \frac{9}{7}\,\mathrm{m} \approx 1.3\,\mathrm{m}}
$$
