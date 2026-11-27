---
title: 東大理物 平成9年度 一般教育科目 物理学 第2問：静磁場と回転電場中の荷電粒子のサイクロトロン共鳴
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 一般教育科目 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成9年度 一般教育科目 物理学 第2問：静磁場と回転電場中の荷電粒子のサイクロトロン共鳴

## 問題

電荷 $q$，質量 $m$ の荷電粒子の位置ベクトルを $\mathbf{r}(t) = (x(t), y(t), z(t))$ で表わす。粒子の速度は光速度と比べて十分小さいとして以下の設問に答えよ。
{: .problem-lead }

(1) 一様な静磁場 $\mathbf{B} = (0, 0, B)$ がかかっているときの荷電粒子の運動で，時刻 $t = 0$ での初期条件 $\mathbf{r} = (0, 0, 0)$，$\mathrm{d}\mathbf{r}/\mathrm{d}t = (v_0, 0, u_0)$ を満たすものを求めよ。

(2) 上記静磁場と振動数 $\omega = qB/m$ をもつ電場 $\mathbf{E} = (E\cos\omega t, -E\sin\omega t, 0)$ がかかっているとき，運動方程式の解で，時刻 $t = 0$ での初期条件 $\mathbf{r} = (0, 0, 0)$，$\mathrm{d}\mathbf{r}/\mathrm{d}t = (0, 0, 0)$ を満たすものを求めよ。この場合，運動方程式は複素変数 $\mathrm{d}x/\mathrm{d}t + i\mathrm{d}y/\mathrm{d}t$ を用いると扱いやすい。

(3) (2) について，運動エネルギー $K$ の変化率 $\mathrm{d}K/\mathrm{d}t$ を求めよ。また，電場 $\mathbf{E}$ と粒子の速度 $\mathbf{v}$ の関係に注目して，この結果を説明せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 一般教育科目 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
一様静磁場中の荷電粒子は，磁場に垂直な面内でサイクロトロン角振動数 $\omega = qB/m$ の等速円運動を行い，磁場に平行な方向へは等速運動をするらせん運動を描きます。ここにサイクロトロン回転と同じ向き・同じ角振動数で回転する電場を加えると，複素速度 $w = \dot{x} + i\dot{y}$ に関する1階線形方程式が共鳴条件を満たし，速度ベクトルが常に電場と同方向を向くことで粒子の速さが時間に比例して増大します。
</div>

### (1)

非相対論的な荷電粒子にはたらくローレンツ力による運動方程式は $m\ddot{\mathbf{r}} = q\dot{\mathbf{r}} \times \mathbf{B}$ です。$\mathbf{B} = (0, 0, B)$ を代入して成分ごとに書き下すと次式になります。

$$
\begin{aligned}
m\ddot{x} &= q B \dot{y} \\
m\ddot{y} &= -q B \dot{x} \\
m\ddot{z} &= 0
\end{aligned}
$$

ここで $\omega = \dfrac{qB}{m}$ とおきます。$z$ 成分は $\ddot{z} = 0$ より初期条件 $z(0) = 0$，$\dot{z}(0) = u_0$ より

$$
z(t) = u_0 t
$$

と求まります。$x, y$ 成分については複素変数 $w(t) = \dot{x}(t) + i\dot{y}(t)$ を導入します。運動方程式の第1式と第2式を $\dot{w} = \ddot{x} + i\ddot{y}$ にまとめると

$$
\begin{aligned}
\dot{w} &= \omega \dot{y} - i\omega \dot{x} \\
&= -i\omega (\dot{x} + i\dot{y}) \\
&= -i\omega w
\end{aligned}
$$

が得られます。初期条件 $w(0) = v_0$ のもとでこれを解くと

$$
\begin{aligned}
w(t) &= v_0 e^{-i\omega t} \\
&= v_0 \cos\omega t - i v_0 \sin\omega t
\end{aligned}
$$

となり，実部と虚部から $\dot{x}(t) = v_0 \cos\omega t$，$\dot{y}(t) = -v_0 \sin\omega t$ が従います。初期条件 $x(0) = 0$，$y(0) = 0$ のもとで時刻 $0$ から $t$ まで積分すると，各成分の位置が求まります。

$$
\begin{aligned}
x(t) &= \int_0^t v_0 \cos\omega t'\,\mathrm{d}t' \\
&= \frac{v_0}{\omega}\sin\omega t
\end{aligned}
$$

$$
\begin{aligned}
y(t) &= \int_0^t (-v_0 \sin\omega t')\,\mathrm{d}t' \\
&= \frac{v_0}{\omega}(\cos\omega t - 1)
\end{aligned}
$$

なお $B = 0$ すなわち $\omega = 0$ の極限では $x(t) = v_0 t$，$y(t) = 0$，$z(t) = u_0 t$ の等速直線運動になります。

$$
\finalanswer{x(t) = \frac{v_0}{\omega}\sin\omega t,\qquad y(t) = \frac{v_0}{\omega}(\cos\omega t - 1),\qquad z(t) = u_0 t\qquad \left(\omega = \frac{qB}{m}\right)}
$$

### (2)

静磁場 $\mathbf{B} = (0, 0, B)$ と回転電場 $\mathbf{E} = (E\cos\omega t, -E\sin\omega t, 0)$ のもとでの運動方程式 $m\ddot{\mathbf{r}} = q(\mathbf{E} + \dot{\mathbf{r}} \times \mathbf{B})$ を成分ごとに書きます。

$$
\begin{aligned}
m\ddot{x} &= q E \cos\omega t + q B \dot{y} \\
m\ddot{y} &= -q E \sin\omega t - q B \dot{x} \\
m\ddot{z} &= 0
\end{aligned}
$$

$z$ 成分は初期条件 $z(0) = 0$，$\dot{z}(0) = 0$ よりすべての時刻で $z(t) = 0$ です。

$x, y$ 成分について複素変数 $w(t) = \dot{x}(t) + i\dot{y}(t)$ を導入すると，$\cos\omega t - i\sin\omega t = e^{-i\omega t}$ を用いて次式が得られます。

$$
\dot{w} + i\omega w = \frac{qE}{m} e^{-i\omega t}
$$

両辺に積分因子 $e^{i\omega t}$ を掛けると，左辺は完全微分になります。

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(e^{i\omega t} w\right) = \frac{qE}{m}
$$

初期条件 $w(0) = 0$ のもとで $0$ から $t$ まで積分すると $e^{i\omega t} w(t) = \dfrac{qE}{m}t$ となり，複素速度は次のように求まります。

$$
\begin{aligned}
w(t) &= \frac{qE}{m} t e^{-i\omega t} \\
&= \frac{qE}{m} t \cos\omega t - i\frac{qE}{m} t \sin\omega t
\end{aligned}
$$

したがって速度の各成分は $\dot{x}(t) = \dfrac{qE}{m} t \cos\omega t$，$\dot{y}(t) = -\dfrac{qE}{m} t \sin\omega t$ です。複素位置 $\zeta(t) = x(t) + i y(t)$ を初期条件 $\zeta(0) = 0$ のもとで部分積分により求めます。

$$
\begin{aligned}
\zeta(t) &= \frac{qE}{m}\int_0^t t' e^{-i\omega t'}\,\mathrm{d}t' \\
&= \frac{qE}{m}\left[\frac{i}{\omega}t' e^{-i\omega t'}\right]_0^t - \frac{i qE}{m\omega}\int_0^t e^{-i\omega t'}\,\mathrm{d}t' \\
&= \frac{qE}{m\omega^2}\left(i\omega t e^{-i\omega t} + e^{-i\omega t} - 1\right)
\end{aligned}
$$

ここで $e^{-i\omega t} = \cos\omega t - i\sin\omega t$ および $i e^{-i\omega t} = \sin\omega t + i\cos\omega t$ を代入して実部と虚部を取り出すと，位置ベクトル $\mathbf{r}(t)$ の各成分が得られます。

$$
\begin{aligned}
x(t) &= \frac{qE}{m\omega^2}\left(\omega t\sin\omega t + \cos\omega t - 1\right) \\
y(t) &= \frac{qE}{m\omega^2}\left(\omega t\cos\omega t - \sin\omega t\right) \\
z(t) &= 0
\end{aligned}
$$

$\omega = \dfrac{qB}{m}$ を代入すれば係数 $\dfrac{qE}{m\omega^2}$ は $\dfrac{mE}{qB^2}$ に等しくなります。

$$
\finalanswer{x(t) = \frac{qE}{m\omega^2}\left(\omega t\sin\omega t + \cos\omega t - 1\right),\qquad y(t) = \frac{qE}{m\omega^2}\left(\omega t\cos\omega t - \sin\omega t\right),\qquad z(t) = 0}
$$

### (3)

(2) で求めた速度は

$$
\mathbf{v}(t) = \left(\frac{qE}{m} t \cos\omega t,\ -\frac{qE}{m} t \sin\omega t,\ 0\right)
$$

なので，その大きさの2乗は $|w(t)|^2$ に等しく，$|\mathbf{v}(t)|^2 = \left(\dfrac{qE}{m}t\right)^2$ となります。したがって運動エネルギー $K(t)$ は次式で与えられます。

$$
\begin{aligned}
K(t) &= \frac{1}{2}m|\mathbf{v}(t)|^2 \\
&= \frac{q^2 E^2}{2m} t^2
\end{aligned}
$$

これを時間 $t$ で微分すると，運動エネルギーの変化率が求まります。

$$
\frac{\mathrm{d}K}{\mathrm{d}t} = \frac{q^2 E^2}{m} t
$$

次に，電場 $\mathbf{E}(t)$ と粒子の速度 $\mathbf{v}(t)$ の関係に注目してこの結果を説明します。$\mathbf{E}(t) = (E\cos\omega t, -E\sin\omega t, 0)$ と $\mathbf{v}(t)$ を比較すると，すべての時刻 $t \ge 0$ で

$$
\mathbf{v}(t) = \frac{q t}{m}\mathbf{E}(t)
$$

が成り立っています。すなわち，電場 $\mathbf{E}$ は粒子が静磁場中で行うサイクロトロン円運動とまったく同じ向き・同じ角振動数 $\omega = qB/m$ で回転しているため，力 $q\mathbf{E}$ と速度 $\mathbf{v}$ は常に同じ向きを向きます。一方，磁場によるローレンツ力 $q\mathbf{v} \times \mathbf{B}$ は常に $\mathbf{v}$ と直交するため仕事をしません。したがって運動エネルギーの変化率は電場のする仕事率 $q\mathbf{E} \cdot \mathbf{v}$ のみに等しく，

$$
\begin{aligned}
\frac{\mathrm{d}K}{\mathrm{d}t} &= q\mathbf{E} \cdot \mathbf{v} \\
&= q\mathbf{E} \cdot \left(\frac{qt}{m}\mathbf{E}\right) \\
&= \frac{q^2 E^2}{m} t
\end{aligned}
$$

と表されます。一定の大きさの力 $|qE|$ が常に進行方向にはたらき続けるサイクロトロン共鳴の状態にあるため，粒子の速さは $|qE|t/m$ と時間に比例して増大し，その結果として単位時間あたりに電場がする仕事率 $\mathrm{d}K/\mathrm{d}t$ も時間に比例して増大します。

$$
\finalanswer{\frac{\mathrm{d}K}{\mathrm{d}t} = \frac{q^2 E^2}{m} t}
$$
