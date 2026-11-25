---
title: 東大理物 平成21年度 物理学 第3問：2粒子の弾性散乱と球状ポテンシャル障壁
tags:
  - 院試過去問
  - 東大理物
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成21年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成21年度 物理学 第3問：2粒子の弾性散乱と球状ポテンシャル障壁

## 問題

質量 $m_1$ の粒子1と質量 $m_2$ の粒子2の弾性散乱を考える。散乱前で2つの粒子の距離が十分に離れており，両者の間の相互作用が無視できる状態において，粒子2の速さが $0$ になるように実験室系を選ぶ。このとき，粒子1の速さは $V_1$ であるとする（図1左）。以下では全て非相対論的古典力学の範囲で答えよ。また，粒子1，2ともに内部自由度を持たない質点とみなせるものとする。図1右に示すように，粒子1と2の重心系において散乱前に粒子1と2が十分に離れた状態での速度ベクトルを，それぞれ $\boldsymbol{v}_1, \boldsymbol{v}_2$，速さをそれぞれ $v_1, v_2$，また，散乱後に2つの粒子が十分離れた後の速度ベクトルを，それぞれ $\boldsymbol{v}'_1, \boldsymbol{v}'_2$，速さをそれぞれ $v'_1, v'_2$ とする。また，重心系での粒子1の散乱角を $\psi$ とする。ただし，$\psi$ は $0 \le \psi \le \pi$ の角度として定義する。

<figure class="problem-figure" markdown>
![実験室系と重心系での弾性散乱](../../../docs/assets/figures/pastexam-todai-ributsu/H21_butsuri_3-p1-light.svg#only-light)
![実験室系と重心系での弾性散乱](../../../docs/assets/figures/pastexam-todai-ributsu/H21_butsuri_3-p1-dark.svg#only-dark)
<figcaption markdown="span">図1：（a）実験室系，（b）重心系。</figcaption>
</figure>

(1) 速度ベクトル $\boldsymbol{v}_1$ と $\boldsymbol{v}_2$ の間に成り立つ関係式，および速さ $v_2$ と $v'_2$ の間に成り立つ関係式を，それぞれ1つ示せ。

(2) 実験室系における粒子2の散乱後の運動エネルギー $\varepsilon$ を，$m_1, m_2, V_1, \psi$ を用いて表せ。

2つの粒子の間に働く力が，2つの粒子の間の距離 $r$ を変数とするポテンシャル $U(r)$ によって与えられるとする。
{: .problem-lead }

(3) 重心系におけるこの2粒子系のラグランジアンを，粒子2から粒子1への相対位置ベクトル $\boldsymbol{r} = \boldsymbol{r}_1 - \boldsymbol{r}_2$ と換算質量 $m = 1/(1/m_1 + 1/m_2)$ を用いて書き表せ。ここで $\boldsymbol{r}_1$ と $\boldsymbol{r}_2$ は，それぞれ重心系における粒子1と2の位置ベクトルである。座標系として，図2のように，2つの粒子が運動する平面上に定義される極座標系 $\boldsymbol{r} = (r, \phi)$ を用いよ。すなわち，$r, \phi$ とその時間微分 $\dot{r}, \dot{\phi}$ を用いて書き表すこと。

<figure class="problem-figure" markdown>
![極座標の定義とポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H21_butsuri_3-p2-light.svg#only-light)
![極座標の定義とポテンシャル](../../../docs/assets/figures/pastexam-todai-ributsu/H21_butsuri_3-p2-dark.svg#only-dark)
<figcaption markdown="span">図2：$(r, \phi)$ 座標の定義とポテンシャル。</figcaption>
</figure>

(4) 設問3で求めたラグランジアンと最小作用の原理（オイラー・ラグランジュ方程式）から角運動量保存則，

$$
mr^2\dot{\phi} = \text{一定}
$$

を導け。

さらに，ポテンシャル $U(r)$ は

$$
U(r) = \begin{cases} U_0 & (r \le r_0) \\ 0 & (r > r_0) \end{cases}
$$

により与えられるとする。ここで，$U_0$ は，

$$
0 < U_0 < \frac{m}{2}V_1^2
$$

を満たす定数である。
{: .problem-lead }

(5) 図2に示すように，衝突パラメーター $b$ が $0 \le b \le r_0$ であるとき，図2のように $r_0\sin\theta = b$ により $0 \le \theta \le \pi/2$ の大きさの角度 $\theta$ を定義する。また，定数 $n$ を

$$
n = \sqrt{1 - \frac{2U_0}{mV_1^2}}
$$

により定義する。相対位置ベクトル $\boldsymbol{r}$ の軌跡の略図を示し，さらに，角度 $\theta$ と重心系での散乱角 $\psi$ の間に成り立つ関係を $n$ を用いて表せ。散乱の様子が $\theta$ の値によって質的に異なる場合は，それぞれの略図を示せ。

(6) 衝突パラメーター $b$ が $0$ から $r_0$ の間で様々な値をとる場合に，実験室系における粒子2の散乱後の運動エネルギーの最大値 $\varepsilon_{\max}$ を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成21年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2粒子の散乱を重心系に移すと，全運動量が $0$ になるため2粒子の運動が1つの換算質量 $m$ の粒子の中心力問題にまとまります。さらに中心力のもとでは角運動量が保存されるため，運動が1つの平面内に限られます。

ポテンシャルが半径 $r_0$ の球面で不連続に変化するとき，境界では半径方向のみに力がはたらき，接線方向の速度成分は変わりません。この接線速度の連続性とエネルギー保存を組み合わせると，球面での軌道の折れ曲がりが光の屈折や全反射と同じ形で決まります。
</div>

### (1)

重心系では系の全運動量が常に $\boldsymbol{0}$ です。よって散乱前の速度ベクトル $\boldsymbol{v}_1, \boldsymbol{v}_2$ の間には次の関係が成り立ちます。

$$
m_1\boldsymbol{v}_1 + m_2\boldsymbol{v}_2 = \boldsymbol{0}
$$

同様に散乱後についても $m_1\boldsymbol{v}'_1 + m_2\boldsymbol{v}'_2 = \boldsymbol{0}$ が成り立つため，$v_1 = \dfrac{m_2}{m_1}v_2$，$v'_1 = \dfrac{m_2}{m_1}v'_2$ です。弾性散乱では散乱前後で運動エネルギーの和が保存されるので，次式が成り立ちます。

$$
\begin{aligned}
\frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2 &= \frac{1}{2}m_1 {v'_1}^2 + \frac{1}{2}m_2 {v'_2}^2 \\
\frac{1}{2}m_2\left(\frac{m_2}{m_1} + 1\right)v_2^2 &= \frac{1}{2}m_2\left(\frac{m_2}{m_1} + 1\right){v'_2}^2 \\
v_2^2 &= {v'_2}^2
\end{aligned}
$$

速さは非負なので，$v'_2 = v_2$ です。

$$
\finalanswer{m_1\boldsymbol{v}_1 + m_2\boldsymbol{v}_2 = \boldsymbol{0}, \qquad v'_2 = v_2}
$$

### (2)

実験室系における散乱前の粒子1の速度ベクトルを $\boldsymbol{V}_1$ とします。粒子2は散乱前に静止しているので，重心の速度ベクトル $\boldsymbol{V}_{\mathrm{G}}$ は次式になります。

$$
\boldsymbol{V}_{\mathrm{G}} = \frac{m_1\boldsymbol{V}_1 + m_2\cdot\boldsymbol{0}}{m_1 + m_2} = \frac{m_1}{m_1 + m_2}\boldsymbol{V}_1
$$

重心系における散乱前の粒子2の速度ベクトルは $\boldsymbol{v}_2 = \boldsymbol{0} - \boldsymbol{V}_{\mathrm{G}} = -\boldsymbol{V}_{\mathrm{G}}$ です。設問1より，$v'_2 = v_2 = V_{\mathrm{G}}$ です。また重心系では $\boldsymbol{v}_2$ は $\boldsymbol{v}_1$ と反対向きであり，$\boldsymbol{v}'_2$ は $\boldsymbol{v}'_1$ と反対向きなので，$\boldsymbol{v}_2$ と $\boldsymbol{v}'_2$ のなす角も $\psi$ になります。したがって，$\boldsymbol{v}'_2$ と $\boldsymbol{V}_{\mathrm{G}} = -\boldsymbol{v}_2$ のなす角は $\pi - \psi$ です。

実験室系での散乱後の粒子2の速度ベクトルは $\boldsymbol{V}'_2 = \boldsymbol{v}'_2 + \boldsymbol{V}_{\mathrm{G}}$ です。この大きさの2乗を計算します。

$$
\begin{aligned}
{V'_2}^2 &= |\boldsymbol{v}'_2 + \boldsymbol{V}_{\mathrm{G}}|^2 \\
&= {v'_2}^2 + V_{\mathrm{G}}^2 + 2\boldsymbol{v}'_2\cdot\boldsymbol{V}_{\mathrm{G}} \\
&= V_{\mathrm{G}}^2 + V_{\mathrm{G}}^2 + 2V_{\mathrm{G}}^2\cos(\pi - \psi) \\
&= 2V_{\mathrm{G}}^2(1 - \cos\psi) \\
&= 4V_{\mathrm{G}}^2\sin^2\frac{\psi}{2}
\end{aligned}
$$

$V_{\mathrm{G}} = \dfrac{m_1}{m_1 + m_2}V_1$ を代入して，粒子2の散乱後の運動エネルギー $\varepsilon = \dfrac{1}{2}m_2 {V'_2}^2$ を求めます。

$$
\begin{aligned}
\varepsilon &= \frac{1}{2}m_2 \cdot 4\left(\frac{m_1}{m_1 + m_2}\right)^2 V_1^2 \sin^2\frac{\psi}{2} \\
&= \frac{2m_1^2 m_2}{(m_1 + m_2)^2}V_1^2\sin^2\frac{\psi}{2}
\end{aligned}
$$

したがって，求める運動エネルギーは次式となります。

$$
\finalanswer{\varepsilon = \frac{2m_1^2 m_2}{(m_1 + m_2)^2}V_1^2\sin^2\frac{\psi}{2}}
$$

### (3)

重心系では $m_1\boldsymbol{r}_1 + m_2\boldsymbol{r}_2 = \boldsymbol{0}$ です。これと相対位置ベクトル $\boldsymbol{r} = \boldsymbol{r}_1 - \boldsymbol{r}_2$ を連立して $\boldsymbol{r}_1, \boldsymbol{r}_2$ を $\boldsymbol{r}$ で表します。

$$
\boldsymbol{r}_1 = \frac{m_2}{m_1 + m_2}\boldsymbol{r}, \qquad \boldsymbol{r}_2 = -\frac{m_1}{m_1 + m_2}\boldsymbol{r}
$$

両辺を時間微分すると $\dot{\boldsymbol{r}}_1 = \dfrac{m_2}{m_1 + m_2}\dot{\boldsymbol{r}}$，$\dot{\boldsymbol{r}}_2 = -\dfrac{m_1}{m_1 + m_2}\dot{\boldsymbol{r}}$ です。これを用いて運動エネルギー $T$ を書き換えます。

$$
\begin{aligned}
T &= \frac{1}{2}m_1\dot{\boldsymbol{r}}_1^2 + \frac{1}{2}m_2\dot{\boldsymbol{r}}_2^2 \\
&= \frac{1}{2}m_1\left(\frac{m_2}{m_1 + m_2}\right)^2\dot{\boldsymbol{r}}^2 + \frac{1}{2}m_2\left(\frac{m_1}{m_1 + m_2}\right)^2\dot{\boldsymbol{r}}^2 \\
&= \frac{1}{2}\frac{m_1 m_2(m_2 + m_1)}{(m_1 + m_2)^2}\dot{\boldsymbol{r}}^2 \\
&= \frac{1}{2}\frac{m_1 m_2}{m_1 + m_2}\dot{\boldsymbol{r}}^2 \\
&= \frac{1}{2}m\dot{\boldsymbol{r}}^2
\end{aligned}
$$

ここで $m = \dfrac{1}{1/m_1 + 1/m_2} = \dfrac{m_1 m_2}{m_1 + m_2}$ です。平面極座標 $(r, \phi)$ では $x = r\cos\phi$，$y = r\sin\phi$ より $\dot{x} = \dot{r}\cos\phi - r\dot{\phi}\sin\phi$，$\dot{y} = \dot{r}\sin\phi + r\dot{\phi}\cos\phi$ なので，$\dot{\boldsymbol{r}}^2$ は次式になります。

$$
\begin{aligned}
\dot{\boldsymbol{r}}^2 &= \dot{x}^2 + \dot{y}^2 \\
&= \dot{r}^2(\cos^2\phi + \sin^2\phi) + r^2\dot{\phi}^2(\sin^2\phi + \cos^2\phi) \\
&= \dot{r}^2 + r^2\dot{\phi}^2
\end{aligned}
$$

したがって，重心系におけるラグランジアン $L = T - U(r)$ は次式となります。

$$
\finalanswer{L = \frac{1}{2}m\bigl(\dot{r}^2 + r^2\dot{\phi}^2\bigr) - U(r)}
$$

### (4)

ラグランジアン $L = \dfrac{1}{2}m(\dot{r}^2 + r^2\dot{\phi}^2) - U(r)$ は角度 $\phi$ を陽に含まないため，$\dfrac{\partial L}{\partial \phi} = 0$ です。また，$\dot{\phi}$ による偏微分は $\dfrac{\partial L}{\partial \dot{\phi}} = mr^2\dot{\phi}$ です。これらを $\phi$ に関するオイラー・ラグランジュ方程式に代入します。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{\phi}}\right) - \frac{\partial L}{\partial \phi} &= 0 \\
\frac{\mathrm{d}}{\mathrm{d}t}\bigl(mr^2\dot{\phi}\bigr) &= 0
\end{aligned}
$$

時間微分が $0$ なので，$mr^2\dot{\phi}$ は時間によらず一定です。

### (5)

散乱前の相対速度は $\boldsymbol{v} = \dot{\boldsymbol{r}} = \boldsymbol{v}_1 - \boldsymbol{v}_2 = \boldsymbol{V}_1$ なので，入射時の相対速さは $v = V_1$ であり，全エネルギーは $E = \dfrac{1}{2}mV_1^2$ です。また，$r > r_0$ と $r < r_0$ の各領域ではポテンシャルが一定なので力がはたらかず，相対位置ベクトル $\boldsymbol{r}$ の軌跡は直線になります。

境界 $r = r_0$ での運動を調べます。半径 $r_0$ の球面ではポテンシャルが半径方向にのみ変化するので，接線方向の速度成分は連続であり，角運動量 $L_z = mr^2\dot{\phi}$ が保存されます。入射時の角運動量の大きさは $mV_1 b = mV_1 r_0\sin\theta$ です。

まず粒子が領域 $r < r_0$ に入る場合を考えます。領域 $r < r_0$ での速さを $v_{\mathrm{in}}$ とすると，エネルギー保存則から次式が得られます。

$$
\begin{aligned}
\frac{1}{2}m v_{\mathrm{in}}^2 + U_0 &= \frac{1}{2}m V_1^2 \\
v_{\mathrm{in}}^2 &= V_1^2\left(1 - \frac{2U_0}{mV_1^2}\right) \\
v_{\mathrm{in}} &= n V_1
\end{aligned}
$$

ここで $0 < U_0 < \dfrac{m}{2}V_1^2$ より $0 < n < 1$ です。境界 $r = r_0$ での法線と内部の軌跡がなす屈折角を $\theta'$（$0 \le \theta' < \pi/2$）とすると，角運動量保存則から次式が成り立ちます。

$$
\begin{aligned}
m V_1 r_0 \sin\theta &= m v_{\mathrm{in}} r_0 \sin\theta' \\
\sin\theta &= n\sin\theta'
\end{aligned}
$$

したがって，$\sin\theta < n$ のときと $\sin\theta \ge n$ のときで散乱の様子が質的に異なります。

まず $\sin\theta < n$ の場合を考えます。このとき $\sin\theta' = \dfrac{\sin\theta}{n} < 1$ となる実角 $\theta'$ が存在し，粒子は領域 $r < r_0$ に入って屈折角 $\theta'$ で直進します。次に境界 $r = r_0$ に再び到達すると，対称性から入射角 $\theta'$ で外へ出て出射角が $\theta$ になります。$0 < n < 1$ より $\theta' > \theta$ なので，入口と出口で進行方向はそれぞれ同じ向きに $\theta' - \theta$ ずつ曲がります。よって重心系での散乱角 $\psi$ は次式になります。

$$
\psi = 2(\theta' - \theta)
$$

これより $\theta' = \theta + \dfrac{\psi}{2}$ を $\sin\theta = n\sin\theta'$ に代入すると，次の関係式が得られます。

$$
\sin\theta = n\sin\!\left(\theta + \frac{\psi}{2}\right)
$$

次に $\sin\theta \ge n$ の場合を考えます。入射時の半径方向速度の大きさは $V_1\cos\theta$ なので，半径方向の運動エネルギーは次のように計算することができます。

$$
\begin{aligned}
\frac{1}{2}m(V_1\cos\theta)^2 &= \frac{1}{2}mV_1^2(1 - \sin^2\theta) \\
&\le \frac{1}{2}mV_1^2(1 - n^2) \\
&= U_0
\end{aligned}
$$

半径方向の運動エネルギーが障壁の高さ $U_0$ を超えないため，粒子は領域 $r < r_0$ に入ることができず，境界 $r = r_0$ で入射角と反射角がともに $\theta$ となる弾性反射をします。このとき進行方向は $\pi - 2\theta$ だけ変化するので，散乱角 $\psi$ は次式になります。

$$
\psi = \pi - 2\theta
$$

2つの場合の軌跡の略図は次の図のようになります。

<figure class="problem-figure" markdown>
![相対位置ベクトルの軌跡の略図](../../../docs/assets/figures/pastexam-todai-ributsu/H21_butsuri_3-s-light.svg#only-light)
![相対位置ベクトルの軌跡の略図](../../../docs/assets/figures/pastexam-todai-ributsu/H21_butsuri_3-s-dark.svg#only-dark)
<figcaption markdown="span">相対位置ベクトル $\boldsymbol{r}$ の軌跡の略図（左：$\sin\theta < n$ での屈折透過，右：$\sin\theta \ge n$ での全反射）。</figcaption>
</figure>

以上より，$\theta$ と $\psi$ の関係は次のようになります。

$$
\finalanswer{
\begin{cases}
\sin\theta = n\sin\!\left(\theta + \dfrac{\psi}{2}\right) & (\sin\theta < n) \\[8pt]
\psi = \pi - 2\theta & (\sin\theta \ge n)
\end{cases}
}
$$

### (6)

設問2より，粒子2の散乱後の運動エネルギーは $\varepsilon = \dfrac{2m_1^2 m_2}{(m_1 + m_2)^2}V_1^2\sin^2\dfrac{\psi}{2}$ です。$0 \le \psi \le \pi$ の範囲では $\sin^2\dfrac{\psi}{2}$ は $\psi$ の単調増加関数なので，$\varepsilon$ が最大となるのは $\psi$ が最大となるときです。

設問5で得られた $\psi(\theta)$ の増減を調べます。まず $0 \le \theta < \arcsin n$ の範囲では $\psi(\theta) = 2\arcsin\!\left(\dfrac{\sin\theta}{n}\right) - 2\theta$ です。これを $\theta$ で微分します。

$$
\begin{aligned}
\frac{\mathrm{d}\psi}{\mathrm{d}\theta} &= 2\cdot\frac{\dfrac{\cos\theta}{n}}{\sqrt{1 - \dfrac{\sin^2\theta}{n^2}}} - 2 \\
&= 2\left(\frac{\cos\theta}{\sqrt{n^2 - \sin^2\theta}} - 1\right)
\end{aligned}
$$

$0 < n < 1$ より $n^2 - \sin^2\theta < 1 - \sin^2\theta = \cos^2\theta$ なので，$\sqrt{n^2 - \sin^2\theta} < \cos\theta$ です。したがって $\dfrac{\mathrm{d}\psi}{\mathrm{d}\theta} > 0$ となり，$\psi(\theta)$ は単調増加します。

次に $\arcsin n \le \theta \le \dfrac{\pi}{2}$ の範囲では $\psi(\theta) = \pi - 2\theta$ なので，$\dfrac{\mathrm{d}\psi}{\mathrm{d}\theta} = -2 < 0$ となり単調減少します。

よって，$\psi(\theta)$ は臨界角 $\theta_{\mathrm{c}} = \arcsin n$ で最大値 $\psi_{\max} = \pi - 2\theta_{\mathrm{c}}$ をとります。このときの $\sin^2\dfrac{\psi_{\max}}{2}$ を計算します。

$$
\begin{aligned}
\sin^2\frac{\psi_{\max}}{2} &= \sin^2\!\left(\frac{\pi}{2} - \theta_{\mathrm{c}}\right) \\
&= \cos^2\theta_{\mathrm{c}} \\
&= 1 - \sin^2\theta_{\mathrm{c}} \\
&= 1 - n^2 \\
&= \frac{2U_0}{mV_1^2}
\end{aligned}
$$

これを設問2の $\varepsilon$ の式に代入し，$m = \dfrac{m_1 m_2}{m_1 + m_2}$ を用いて整理します。

$$
\begin{aligned}
\varepsilon_{\max} &= \frac{2m_1^2 m_2}{(m_1 + m_2)^2}V_1^2 \cdot \frac{2U_0}{mV_1^2} \\
&= \frac{4m_1^2 m_2}{(m_1 + m_2)^2}\cdot\frac{m_1 + m_2}{m_1 m_2}\,U_0 \\
&= \frac{4m_1}{m_1 + m_2}U_0
\end{aligned}
$$

したがって，実験室系における粒子2の散乱後の運動エネルギーの最大値は次式となります。

$$
\finalanswer{\varepsilon_{\max} = \frac{4m_1}{m_1 + m_2}U_0}
$$
