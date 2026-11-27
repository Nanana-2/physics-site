---
title: 東大理物 平成23年度 物理学 第3問：電磁場中および非一様磁場中の荷電粒子の運動
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成23年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成23年度 物理学 第3問：電磁場中および非一様磁場中の荷電粒子の運動

## 問題

時間に依存しない電磁場中で，電荷 $q$（$> 0$）と質量 $m$ をもつ粒子の運動を考える。電場 $\boldsymbol{E}$，磁束密度 $\boldsymbol{B}$ の下で荷電粒子はローレンツ力

$$
\boldsymbol{F} = q(\boldsymbol{E} + \boldsymbol{v} \times \boldsymbol{B})
$$

を受ける。以下では，磁束密度 $\boldsymbol{B}$ の向きは常に $z$ 軸と平行とする。また，粒子の速度の大きさ $|\boldsymbol{v}|$ は光速度 $c$ に比べて十分小さく，相対論的効果は考えなくてよい。さらに，荷電粒子の運動に伴う電磁波の放出は無視する。

まず，電場が存在せず，一様な磁束密度，$\boldsymbol{B} = (0, 0, B)$，（$B > 0$）だけがある場合を考える。
{: .problem-lead }

(1) このとき，粒子の運動エネルギーは変化しない。その物理的理由を簡潔に述べよ。

(2) 時刻 $t = 0$ において，この粒子を位置 $\boldsymbol{x}_0 = (a, 0, 0)$ から初速度 $\boldsymbol{v}_0 = (0, v_0, 0)$ で放出したところ，原点を中心とする等速円運動を行った。この粒子の運動（位置と速度），および $a$ と $v_0$ の関係を求めよ。

次に，一様な磁束密度に加えて，一様な電場，$\boldsymbol{E} = (E, 0, 0)$，（$E > 0$）をかけた場合を考える。

(3) 設問2と同じ初期条件で粒子を放出したときの運動（位置と速度）を運動方程式を解いて求めよ。このとき $x, y$ 方向の運動に関しては，運動方程式を $u \equiv v_x + i v_y$（$v_x, v_y$ は速度の $x, y$ 成分）についての微分方程式に書き換えると簡単になる。さらに，得られた運動を設問2の場合と比較して，その特徴を述べ，運動の概略を図示せよ。

今度は，電場が存在せず，磁束密度が，$\boldsymbol{B} = (0, 0, B(x))$，（$B(x) > 0$）のように $x$ 軸方向に非一様な場合を考える。ただし，非一様性は非常に小さく，磁束密度は原点付近で $\boldsymbol{B}(x) \approx \boldsymbol{B}(0) + x B'(0)\hat{\boldsymbol{z}}$ と近似できるとする。ここで，$\hat{\boldsymbol{z}}$ は $z$ 軸方向の単位ベクトルを表し，$B'(0) = \left.\dfrac{\mathrm{d}B(x)}{\mathrm{d}x}\right|_{x=0}$ である。
{: .problem-lead }

(4) 設問2と同じ初期条件で粒子を放出したとき，荷電粒子が受けるローレンツ力は近似的に

$$
\boldsymbol{F} \approx q\boldsymbol{v} \times \boldsymbol{B}(0) + q\boldsymbol{v} \times \bigl(x B'(0)\hat{\boldsymbol{z}}\bigr)
$$

と書ける。この右辺第2項が非一様性の効果を表し，それを $\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{v})$ とおく。この項が荷電粒子の運動に及ぼす影響は，$\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{v})$ に非一様性が無い場合の原点を中心とする円運動解を代入し，円運動の1周期での平均 $\langle\boldsymbol{f}\rangle$ を計算することで評価できる。$\langle\boldsymbol{f}\rangle$ を求めよ。

(5) 一様電場中での荷電粒子の運動を参考にして，磁束密度の非一様性が荷電粒子の運動に与える影響について述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成23年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
$xy$ 面内の速度を複素数 $u=v_x+iv_y$ にまとめると，$\boldsymbol{v}\times\boldsymbol{B}$ の $x$，$y$ 成分は $u$ に $-i$ と定数を掛けたものになります。そのため，$v_x$ と $v_y$ の連立方程式は，$u$ についての1階の線形微分方程式1本になります。一様電場はこの方程式に定数の項を加えるので，$u$ を一定の複素数だけずらして定数の項を消します。

磁場の勾配が小さいときは，力 $\boldsymbol{f}$ による軌道のずれも小さいと考えます。そのため，$\boldsymbol{f}$ には勾配のない円運動の解を代入し，1周期で平均した力を一定の外力とみなします。一定の外力は一様電場による力 $q\boldsymbol{E}$ と同じ形なので，(3) の結果を使うことができます。
</div>

### (1)
電場が存在しないとき，粒子が受けるローレンツ力 $\boldsymbol{F} = q\boldsymbol{v} \times \boldsymbol{B}$ は常に速度ベクトル $\boldsymbol{v}$ に直交しています。したがって力が粒子にする単位時間あたりの仕事 $\boldsymbol{F} \cdot \boldsymbol{v} = q(\boldsymbol{v} \times \boldsymbol{B}) \cdot \boldsymbol{v}$ は常に $0$ であり，運動エネルギー $\dfrac{1}{2}m\boldsymbol{v}^2$ は変化しません。

### (2)
$\omega \equiv \dfrac{qB}{m} > 0$ とおきます。$\boldsymbol{E} = \boldsymbol{0}$，$\boldsymbol{B} = (0, 0, B)$ のときの運動方程式は各成分で次のようになります。

$$
\begin{aligned}
\frac{\mathrm{d}v_x}{\mathrm{d}t} &= \omega v_y \\
\frac{\mathrm{d}v_y}{\mathrm{d}t} &= -\omega v_x \\
\frac{\mathrm{d}v_z}{\mathrm{d}t} &= 0
\end{aligned}
$$

$z$ 成分は初期条件 $z(0) = 0, v_z(0) = 0$ より $v_z(t) = 0$，$z(t) = 0$ です。$x, y$ 成分について $u = v_x + i v_y$ を導入すると $\dfrac{\mathrm{d}u}{\mathrm{d}t} = -i\omega u$ となり，初期条件 $u(0) = i v_0$ より $u(t) = i v_0 e^{-i\omega t}$ です。実部と虚部をとって速度と位置を求めます。

$$
\begin{aligned}
v_x(t) &= v_0 \sin(\omega t) \\
v_y(t) &= v_0 \cos(\omega t)
\end{aligned}
$$

これらを時刻 $0$ から $t$ まで積分し，初期位置 $x(0) = a, y(0) = 0$ を用います。

$$
\begin{aligned}
x(t) &= a + \frac{v_0}{\omega}\bigl(1 - \cos(\omega t)\bigr) \\
y(t) &= \frac{v_0}{\omega}\sin(\omega t)
\end{aligned}
$$

軌道が原点を中心とする円運動になるための条件は，中心の $x$ 座標 $a + \dfrac{v_0}{\omega}$ が $0$ になることです。よって

$$
\begin{aligned}
v_0 &= -\omega a \\
&= -\frac{qB}{m} a
\end{aligned}
$$

が得られます。これを代入すると，位置と速度は次のようになります。

$$
\begin{aligned}
\boldsymbol{x}(t) &= \bigl(a\cos(\omega t),\; -a\sin(\omega t),\; 0\bigr) \\
\boldsymbol{v}(t) &= \bigl(-a\omega\sin(\omega t),\; -a\omega\cos(\omega t),\; 0\bigr)
\end{aligned}
$$

$$
\finalanswer{\boldsymbol{x}(t) = \bigl(a\cos(\omega t),\; -a\sin(\omega t),\; 0\bigr), \qquad \boldsymbol{v}(t) = \bigl(-a\omega\sin(\omega t),\; -a\omega\cos(\omega t),\; 0\bigr), \qquad v_0 = -\frac{qB}{m}a \quad \left(\omega = \frac{qB}{m}\right)}
$$

### (3)
一様電場 $\boldsymbol{E} = (E, 0, 0)$ を加えると，運動方程式の $x, y$ 成分は

$$
\begin{aligned}
\frac{\mathrm{d}v_x}{\mathrm{d}t} &= \frac{qE}{m} + \omega v_y \\
\frac{\mathrm{d}v_y}{\mathrm{d}t} &= -\omega v_x
\end{aligned}
$$

となり，$z$ 成分は $v_z(t) = 0$，$z(t) = 0$ のままです。$u = v_x + i v_y$ についてまとめると次式になります。

$$
\frac{\mathrm{d}u}{\mathrm{d}t}=\frac{qE}{m}-i\omega u
$$

$\omega=qB/m$ を使って定数項を吸収します。

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(u+i\frac EB\right)
=-i\omega\left(u+i\frac EB\right)
$$

初期条件 $u(0) = i v_0$ を用いてこの微分方程式を解きます。

$$
u(t)+i\frac EB=i\left(v_0+\frac EB\right)e^{-i\omega t}
$$

$u(t)$ について解き，指数関数を実部と虚部に分けます。

$$
u(t)=-i\frac EB+i\left(v_0+\frac EB\right)\bigl(\cos(\omega t)-i\sin(\omega t)\bigr)
$$

実部と虚部から速度 $\boldsymbol{v}(t)$ が求まります。

$$
\begin{aligned}
v_x(t) &= \left(v_0 + \frac{E}{B}\right)\sin(\omega t) \\
v_y(t) &= -\frac{E}{B} + \left(v_0 + \frac{E}{B}\right)\cos(\omega t) \\
v_z(t) &= 0
\end{aligned}
$$

これを時刻 $0$ から $t$ まで積分し，$x(0) = a, y(0) = 0$ および設問2の関係 $v_0 = -a\omega$ を代入して位置 $\boldsymbol{x}(t)$ を求めます。

$$
\begin{aligned}
x(t) &= a + \frac{1}{\omega}\left(v_0 + \frac{E}{B}\right)\bigl(1 - \cos(\omega t)\bigr) \\
&= \frac{E}{B\omega} + \left(a - \frac{E}{B\omega}\right)\cos(\omega t) \\
y(t) &= -\frac{E}{B}t + \frac{1}{\omega}\left(v_0 + \frac{E}{B}\right)\sin(\omega t) \\
&= -\frac{E}{B}t - \left(a - \frac{E}{B\omega}\right)\sin(\omega t) \\
z(t) &= 0
\end{aligned}
$$

設問2の場合と比べると，角振動数 $\omega = \dfrac{qB}{m}$ の円運動の半径が $|a|$ から $\left|a - \dfrac{E}{B\omega}\right|$ に変わるとともに，円運動の中心が $-y$ 方向へ一定のドリフト速度 $\boldsymbol{v}_{\mathrm{d}} = \left(0, -\dfrac{E}{B}, 0\right)$ で等速直線運動します。全体の軌道は $y$ 軸の負の方向へ進むトロコイド曲線になります。$a > \dfrac{E}{B\omega} > 0$ のときの軌道の概略を次の図に示します。

<figure class="problem-figure" markdown>
![一様電磁場中での荷電粒子のトロコイド軌道の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H23_butsuri_3-s-light.svg#only-light)
![一様電磁場中での荷電粒子のトロコイド軌道の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H23_butsuri_3-s-dark.svg#only-dark)
<figcaption markdown="span">一様電場 $\boldsymbol{E} = (E, 0, 0)$ と一様磁場 $\boldsymbol{B} = (0, 0, B)$ 中での粒子の軌道（実線）。破線は設問2の円軌道，$\boldsymbol{v}_{\mathrm{d}}$ は $-y$ 方向のドリフト速度を表す。</figcaption>
</figure>

$$
\finalanswer{\begin{aligned}
\boldsymbol{x}(t) &= \left(\frac{E}{B\omega} + \left(a - \frac{E}{B\omega}\right)\cos(\omega t),\; -\frac{E}{B}t - \left(a - \frac{E}{B\omega}\right)\sin(\omega t),\; 0\right) \\
\boldsymbol{v}(t) &= \left(\left(v_0 + \frac{E}{B}\right)\sin(\omega t),\; -\frac{E}{B} + \left(v_0 + \frac{E}{B}\right)\cos(\omega t),\; 0\right)
\end{aligned}}
$$

### (4)
$\omega_0 \equiv \dfrac{qB(0)}{m}$ とおきます。非一様性の力 $\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{v}) = q\boldsymbol{v} \times \bigl(x B'(0)\hat{\boldsymbol{z}}\bigr)$ を成分で書きます。

$$
\boldsymbol{f}(\boldsymbol{x}, \boldsymbol{v}) = q B'(0) x\,(v_y,\; -v_x,\; 0)
$$

設問2の円運動解 $x(t) = a\cos(\omega_0 t)$，$v_x(t) = -a\omega_0 \sin(\omega_0 t)$，$v_y(t) = -a\omega_0 \cos(\omega_0 t)$ を代入します。

$$
\begin{aligned}
f_x(t) &= -q a^2 \omega_0 B'(0)\cos^2(\omega_0 t) \\
f_y(t) &= q a^2 \omega_0 B'(0)\cos(\omega_0 t)\sin(\omega_0 t) \\
f_z(t) &= 0
\end{aligned}
$$

1周期 $T = \dfrac{2\pi}{\omega_0}$ にわたる時間平均を計算します。$\dfrac{1}{T}\displaystyle\int_0^T \cos^2(\omega_0 t)\,\mathrm{d}t = \dfrac{1}{2}$，$\dfrac{1}{T}\displaystyle\int_0^T \cos(\omega_0 t)\sin(\omega_0 t)\,\mathrm{d}t = 0$ より，次式が得られます。

$$
\begin{aligned}
\langle f_x \rangle &= -\frac{1}{2}q a^2 \omega_0 B'(0) \\
&= -\frac{m v_0^2}{2 B(0)} B'(0) \\
\langle f_y \rangle &= 0 \\
\langle f_z \rangle &= 0
\end{aligned}
$$

$$
\finalanswer{\begin{aligned}
\langle\boldsymbol{f}\rangle &= \left(-\frac{1}{2}q a^2 \omega_0 B'(0),\; 0,\; 0\right) \\
&= \left(-\frac{m v_0^2}{2 B(0)} B'(0),\; 0,\; 0\right)
\end{aligned}}
$$

### (5)
設問3の結果から，一様な磁束密度 $\boldsymbol{B}(0) = (0, 0, B(0))$ の中で $x$ 方向に一定の力 $q E$ が働くと，粒子の円運動の中心は $y$ 方向に速度 $-\dfrac{E}{B(0)} = -\dfrac{qE}{qB(0)}$ でドリフトします。

設問4で求めた平均の力 $\langle\boldsymbol{f}\rangle$ は，実効的な一様電場

$$
\begin{aligned}
\boldsymbol{E}_{\mathrm{eff}} &= \frac{\langle\boldsymbol{f}\rangle}{q} \\
&= \left(-\frac{1}{2} a^2 \omega_0 B'(0),\; 0,\; 0\right)
\end{aligned}
$$

が働いていることと同等です。したがって，磁束密度の非一様性によって円運動の中心は磁場および磁場勾配の両方に垂直な $y$ 軸方向に一定のドリフト速度

$$
\begin{aligned}
\boldsymbol{v}_{\nabla B} &= \left(0,\; -\frac{E_{\mathrm{eff}, x}}{B(0)},\; 0\right) \\
&= \left(0,\; \frac{a^2 \omega_0 B'(0)}{2 B(0)},\; 0\right) \\
&= \left(0,\; \frac{m v_0^2 B'(0)}{2 q B(0)^2},\; 0\right)
\end{aligned}
$$

で移動します。$B'(0) > 0$ のときは $+y$ 方向，$B'(0) < 0$ のときは $-y$ 方向へドリフトします。
