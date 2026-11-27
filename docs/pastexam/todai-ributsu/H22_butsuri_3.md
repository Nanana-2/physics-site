---
title: 東大理物 平成22年度 物理学 第3問：複素振幅のマクスウェル方程式と平行平板線路
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成22年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成22年度 物理学 第3問：複素振幅のマクスウェル方程式と平行平板線路

## 問題

Maxwell 方程式は

$$
\begin{aligned}
\nabla \cdot \boldsymbol{B}(\boldsymbol{r}, t) &= 0, & \nabla \times \boldsymbol{E}(\boldsymbol{r}, t) + \frac{\partial}{\partial t}\boldsymbol{B}(\boldsymbol{r}, t) &= \boldsymbol{0}, \\
\nabla \cdot \boldsymbol{D}(\boldsymbol{r}, t) &= \rho(\boldsymbol{r}, t), & \nabla \times \boldsymbol{H}(\boldsymbol{r}, t) - \frac{\partial}{\partial t}\boldsymbol{D}(\boldsymbol{r}, t) &= \boldsymbol{J}(\boldsymbol{r}, t)
\end{aligned}
$$

で与えられる。ただし，電場 $\boldsymbol{E}(\boldsymbol{r}, t)$，電束密度 $\boldsymbol{D}(\boldsymbol{r}, t)$，磁束密度 $\boldsymbol{B}(\boldsymbol{r}, t)$，磁場 $\boldsymbol{H}(\boldsymbol{r}, t)$，電荷密度 $\rho(\boldsymbol{r}, t)$，電流密度 $\boldsymbol{J}(\boldsymbol{r}, t)$ である。また，以下のベクトル公式を必要に応じて用いてよい。

$$
\begin{aligned}
\nabla \cdot (\nabla \times \boldsymbol{X}) &= 0 \\
\nabla \times (\nabla \times \boldsymbol{X}) &= \nabla(\nabla \cdot \boldsymbol{X}) - \nabla^2 \boldsymbol{X}
\end{aligned}
$$

(1) 電場の角振動数 $\omega$ で変化する成分を，複素振幅 $\boldsymbol{E}(\boldsymbol{r})$ を用いて $\boldsymbol{E}(\boldsymbol{r}, t) = \boldsymbol{E}(\boldsymbol{r}) e^{-i\omega t}$ と表すと，その実部が実際の場に対応する。ただし，$i$ は虚数単位である。他の物理量に対してもこのような表式を用いて，Maxwell 方程式を時間微分を含まない複素振幅の方程式に書き直せ。

以降，電場と電束密度，磁場と磁束密度の関係が $\boldsymbol{D}(\boldsymbol{r}) = \varepsilon\boldsymbol{E}(\boldsymbol{r})$，$\boldsymbol{B}(\boldsymbol{r}) = \mu\boldsymbol{H}(\boldsymbol{r})$ と書けるとする。ただし，誘電率 $\varepsilon$（$> 0$）および透磁率 $\mu$（$> 0$）は実数の定数とする。
{: .problem-lead }

(2) 複素振幅 $\boldsymbol{E}(\boldsymbol{r}), \boldsymbol{H}(\boldsymbol{r})$ がそれぞれ満たす方程式を $\rho(\boldsymbol{r}), \boldsymbol{J}(\boldsymbol{r})$ を用いて表せ。ただし，$\boldsymbol{E}(\boldsymbol{r})$ の方程式は $\boldsymbol{H}(\boldsymbol{r})$ を含まず，$\boldsymbol{H}(\boldsymbol{r})$ の方程式は $\boldsymbol{E}(\boldsymbol{r})$ を含まない形にせよ。

(3) $\rho(\boldsymbol{r}) = 0$ かつ $\boldsymbol{J}(\boldsymbol{r}) = \sigma\boldsymbol{E}(\boldsymbol{r})$ の場合を考える。ただし，電気伝導度 $\sigma$（$\ge 0$）は実数の定数であるとする。このとき，$\boldsymbol{E}(\boldsymbol{r}), \boldsymbol{H}(\boldsymbol{r})$ の解の一つとして，$x, y$ によらない

$$
\boldsymbol{E}(z) = \boldsymbol{E}_0 e^{ikz}, \qquad \boldsymbol{H}(z) = \boldsymbol{H}_0 e^{ikz}
$$

の組み合わせを考える。$\boldsymbol{E}_0, \boldsymbol{H}_0$ は，$x, y, z$ によらない複素ベクトルである。このとき，$z$ 方向の単位ベクトルを $\boldsymbol{s}$ として，$\boldsymbol{E}_0 \perp \boldsymbol{s}, \boldsymbol{H}_0 \perp \boldsymbol{s}, \boldsymbol{E}_0 \perp \boldsymbol{H}_0$ を示せ。

(4) 設問3で $\sigma = 0$ の場合，位相速度および $\boldsymbol{E}(z)$ と $\boldsymbol{H}(z)$ の振幅の比 $|\boldsymbol{E}| / |\boldsymbol{H}|$ を $\varepsilon, \mu$ を用いて表せ。また，$\sigma \neq 0$ の場合，電磁場の振る舞いが $\sigma = 0$ の場合と比べてどのように異なるかを説明せよ。

(5) 図のように，幅 $a$ で $z$ 方向には無限遠まで続く2枚の完全導体が真空中で狭い間隔 $b$（$a \gg b$）で対向した平行平板線路を考える。この2枚の導体間に設問3で与えた電場，磁場が存在し，それ以外の部分では電場，磁場の振幅がゼロであるとする。このとき，境界条件に注意して，導体間の電場，磁場の方向を示せ。

<figure class="problem-figure" markdown>
![幅a・間隔bの平行平板線路](../../assets/figures/pastexam-todai-ributsu/H22_butsuri_3-p-light.svg#only-light)
![幅a・間隔bの平行平板線路](../../assets/figures/pastexam-todai-ributsu/H22_butsuri_3-p-dark.svg#only-dark)
<figcaption markdown="span">平行平板線路</figcaption>
</figure>

(6) 設問5の場合，2枚の導体を流れる電流の $z$ 依存性を説明せよ。

(7) 設問5の場合，任意の $z = z_0$ における2枚の導体間の電位差と導体を流れる電流の大きさの比を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成22年度修士課程入学試験 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
時間依存性を $e^{-i\omega t}$ とおくと，時間微分は $-i\omega$ を掛けることに置き換わります。そのため，マクスウェル方程式は空間微分だけの方程式になり，回転をもう一度とると $\boldsymbol{E}$ と $\boldsymbol{H}$ を別々の方程式に分けることができます。

平面波 $e^{ikz}$ に対しては，$\nabla$ は $ik\boldsymbol{s}$ を掛けることに置き換わります。発散と回転の式は $\boldsymbol{E}_0$，$\boldsymbol{H}_0$，$\boldsymbol{s}$ の内積と外積の式になるので，3つのベクトルの向きの関係をそこから読み取ります。

平行平板線路では，完全導体の表面で電場の接線成分と磁場の法線成分が $0$ になります。場の向きはこの境界条件から選びます。電流は導体表面の磁場から求め，電位差は電場を板の間で積分して求めます。
</div>

### (1)
すべての場に $e^{-i\omega t}$ の時間依存性を代入すると，$\dfrac{\partial}{\partial t}$ が $-i\omega$ に置き換わります。共通の因子 $e^{-i\omega t} \neq 0$ を除くと，複素振幅の Maxwell 方程式は次の4式になります。

$$
\finalanswer{\begin{aligned}
\nabla \cdot \boldsymbol{B}(\boldsymbol{r}) &= 0, & \nabla \times \boldsymbol{E}(\boldsymbol{r}) - i\omega\boldsymbol{B}(\boldsymbol{r}) &= \boldsymbol{0}, \\
\nabla \cdot \boldsymbol{D}(\boldsymbol{r}) &= \rho(\boldsymbol{r}), & \nabla \times \boldsymbol{H}(\boldsymbol{r}) + i\omega\boldsymbol{D}(\boldsymbol{r}) &= \boldsymbol{J}(\boldsymbol{r})
\end{aligned}}
$$

### (2)
$\boldsymbol{D} = \varepsilon\boldsymbol{E}$，$\boldsymbol{B} = \mu\boldsymbol{H}$ を設問1の方程式に代入すると，次のようになります。

$$
\begin{aligned}
\nabla \cdot \boldsymbol{H} &= 0, & \nabla \times \boldsymbol{E} &= i\omega\mu\boldsymbol{H} \\
\nabla \cdot \boldsymbol{E} &= \frac{\rho}{\varepsilon}, & \nabla \times \boldsymbol{H} &= \boldsymbol{J} - i\omega\varepsilon\boldsymbol{E}
\end{aligned}
$$

まず $\boldsymbol{E}$ についての方程式を導きます。$\nabla \times \boldsymbol{E} = i\omega\mu\boldsymbol{H}$ の両辺の回転をとり，$\nabla \times \boldsymbol{H} = \boldsymbol{J} - i\omega\varepsilon\boldsymbol{E}$ とベクトル公式を用います。

$$
\begin{aligned}
\nabla \times (\nabla \times \boldsymbol{E}) &= i\omega\mu(\nabla \times \boldsymbol{H}) \\
\nabla(\nabla \cdot \boldsymbol{E}) - \nabla^2 \boldsymbol{E} &= i\omega\mu(\boldsymbol{J} - i\omega\varepsilon\boldsymbol{E}) \\
\frac{1}{\varepsilon}\nabla\rho - \nabla^2 \boldsymbol{E} &= i\omega\mu\boldsymbol{J} + \varepsilon\mu\omega^2 \boldsymbol{E} \\
\nabla^2 \boldsymbol{E} + \varepsilon\mu\omega^2 \boldsymbol{E} &= \frac{1}{\varepsilon}\nabla\rho - i\omega\mu\boldsymbol{J}
\end{aligned}
$$

次に $\boldsymbol{H}$ についての方程式を導きます。$\nabla \times \boldsymbol{H} = \boldsymbol{J} - i\omega\varepsilon\boldsymbol{E}$ の両辺の回転をとり，$\nabla \times \boldsymbol{E} = i\omega\mu\boldsymbol{H}$ と $\nabla \cdot \boldsymbol{H} = 0$ を用います。

$$
\begin{aligned}
\nabla \times (\nabla \times \boldsymbol{H}) &= \nabla \times \boldsymbol{J} - i\omega\varepsilon(\nabla \times \boldsymbol{E}) \\
\nabla(\nabla \cdot \boldsymbol{H}) - \nabla^2 \boldsymbol{H} &= \nabla \times \boldsymbol{J} + \varepsilon\mu\omega^2 \boldsymbol{H} \\
\nabla^2 \boldsymbol{H} + \varepsilon\mu\omega^2 \boldsymbol{H} &= -\nabla \times \boldsymbol{J}
\end{aligned}
$$

$$
\finalanswer{\nabla^2 \boldsymbol{E} + \varepsilon\mu\omega^2 \boldsymbol{E} = \frac{1}{\varepsilon}\nabla\rho - i\omega\mu\boldsymbol{J}, \qquad \nabla^2 \boldsymbol{H} + \varepsilon\mu\omega^2 \boldsymbol{H} = -\nabla \times \boldsymbol{J}}
$$

### (3)
$\boldsymbol{E}(z) = \boldsymbol{E}_0 e^{ikz}$，$\boldsymbol{H}(z) = \boldsymbol{H}_0 e^{ikz}$ に対して $\nabla$ は $ik\boldsymbol{s}$ として作用します。ここで $k \neq 0$ とします。

$\rho = 0$ より $\nabla \cdot \boldsymbol{E} = 0$ および $\nabla \cdot \boldsymbol{H} = 0$ に代入します。

$$
\begin{aligned}
ik(\boldsymbol{s} \cdot \boldsymbol{E}_0) e^{ikz} &= 0 \implies \boldsymbol{s} \cdot \boldsymbol{E}_0 = 0 \\
ik(\boldsymbol{s} \cdot \boldsymbol{H}_0) e^{ikz} &= 0 \implies \boldsymbol{s} \cdot \boldsymbol{H}_0 = 0
\end{aligned}
$$

よって $\boldsymbol{E}_0 \perp \boldsymbol{s}$ かつ $\boldsymbol{H}_0 \perp \boldsymbol{s}$ です。さらに $\nabla \times \boldsymbol{E} = i\omega\mu\boldsymbol{H}$ に代入すると，

$$
\begin{aligned}
ik(\boldsymbol{s} \times \boldsymbol{E}_0) e^{ikz} &= i\omega\mu\boldsymbol{H}_0 e^{ikz} \\
\boldsymbol{H}_0 &= \frac{k}{\omega\mu}(\boldsymbol{s} \times \boldsymbol{E}_0)
\end{aligned}
$$

となります。両辺と $\boldsymbol{E}_0$ の内積をとると，$\boldsymbol{E}_0 \cdot (\boldsymbol{s} \times \boldsymbol{E}_0) = 0$ より $\boldsymbol{E}_0 \cdot \boldsymbol{H}_0 = 0$ です。したがって $\boldsymbol{E}_0 \perp \boldsymbol{H}_0$ が成り立ちます。

### (4)
設問2の $\boldsymbol{E}$ の方程式に $\rho = 0$，$\boldsymbol{J} = \sigma\boldsymbol{E}$，$\boldsymbol{E}(z) = \boldsymbol{E}_0 e^{ikz}$ を代入します。

$$
\begin{aligned}
\left(-k^2 + \varepsilon\mu\omega^2 + i\omega\mu\sigma\right)\boldsymbol{E}_0 &= \boldsymbol{0} \\
k^2 &= \varepsilon\mu\omega^2 + i\omega\mu\sigma
\end{aligned}
$$

$\sigma = 0$ のとき，$+z$ 方向へ伝搬する波の波数は $k = \omega\sqrt{\varepsilon\mu}$ であり，位相速度 $v_{\mathrm{p}}$ は次式になります。

$$
v_{\mathrm{p}} = \frac{\omega}{k} = \frac{1}{\sqrt{\varepsilon\mu}}
$$

また設問3の $\boldsymbol{H}_0 = \dfrac{k}{\omega\mu}(\boldsymbol{s} \times \boldsymbol{E}_0)$ と $\boldsymbol{E}_0 \perp \boldsymbol{s}$ より，$|\boldsymbol{H}_0| = \dfrac{k}{\omega\mu}|\boldsymbol{E}_0|$ です。よって振幅の比 $|\boldsymbol{E}| / |\boldsymbol{H}|$ は次のとおりです。

$$
\begin{aligned}
\frac{|\boldsymbol{E}|}{|\boldsymbol{H}|} &= \frac{\omega\mu}{k} \\
&= \frac{\omega\mu}{\omega\sqrt{\varepsilon\mu}} \\
&= \sqrt{\frac{\mu}{\varepsilon}}
\end{aligned}
$$

$\sigma \neq 0$ のとき，$k^2 = \varepsilon\mu\omega^2 + i\omega\mu\sigma$ は虚部をもつため波数 $k = k_{\mathrm{r}} + i k_{\mathrm{i}}$（$k_{\mathrm{r}} > 0, k_{\mathrm{i}} > 0$）が複素数になります。

電磁場は $e^{ikz} = e^{-k_{\mathrm{i}} z} e^{i k_{\mathrm{r}} z}$ に比例するので，進むにつれて振幅が指数関数的に減衰します。減衰する分のエネルギーは，ジュール熱になります。

位相速度 $\omega / k_{\mathrm{r}}$ は，角振動数 $\omega$ によって変わるようになります。また，$\boldsymbol{H}_0 = \dfrac{k}{\omega\mu}(\boldsymbol{s} \times \boldsymbol{E}_0)$ の $k$ が複素数になるので，電場と磁場の振動には位相差が生じます。

$$
\finalanswer{v_{\mathrm{p}} = \frac{1}{\sqrt{\varepsilon\mu}}, \qquad \frac{|\boldsymbol{E}|}{|\boldsymbol{H}|} = \sqrt{\frac{\mu}{\varepsilon}}}
$$

### (5)
完全導体の内部および導体外では電場・磁場が $0$ です。導体板の表面 $y = 0$ および $y = b$ における境界条件より，導体表面に平行な電場成分と垂直な磁場成分は連続なので，$E_x = E_z = 0$ かつ $H_y = 0$ です。

設問3の横波の条件 $\boldsymbol{E}_0 \perp \boldsymbol{s}$ と $E_x = 0$ より，導体間の電場は $y$ 方向を向きます。また $\boldsymbol{H}_0 = \dfrac{k}{\omega\mu_0}(\boldsymbol{s} \times \boldsymbol{E}_0)$ より，$\boldsymbol{E}$ が $+y$ 方向を向くとき $\boldsymbol{H}$ は $-x$ 方向を向きます。したがって，電場は $y$ 軸に平行，磁場は $x$ 軸に平行です。

### (6)
導体板の内部では磁場が $0$，導体間では $\boldsymbol{H}(z, t) = H_x(z, t)\hat{\boldsymbol{x}}$ が存在するため，アンペールの法則の境界条件より導体表面には表面電流密度 $\boldsymbol{K} = \boldsymbol{n} \times \boldsymbol{H}$ が流れます。ここで $\boldsymbol{n}$ は導体から真空側へ向く単位法線ベクトルです。

$y$ 軸は下向きにとっています。上側の導体板 $y = 0$ では $\boldsymbol{n} = +\hat{\boldsymbol{y}}$，下側の導体板 $y = b$ では $\boldsymbol{n} = -\hat{\boldsymbol{y}}$ です。

$$
\begin{aligned}
\boldsymbol{K}_{\mathrm{top}} &= \hat{\boldsymbol{y}} \times (H_x \hat{\boldsymbol{x}}) = -H_x \hat{\boldsymbol{z}} \\
\boldsymbol{K}_{\mathrm{bot}} &= -\hat{\boldsymbol{y}} \times (H_x \hat{\boldsymbol{x}}) = +H_x \hat{\boldsymbol{z}}
\end{aligned}
$$

2枚の導体を流れる電流は，ともに $z$ 軸に平行で，互いに逆向きです。$k = \omega\sqrt{\varepsilon_0 \mu_0}$ とすると，$H_x(z, t)$ は $e^{i(kz - \omega t)}$ に比例します。したがって，電流は $z$ について波数 $k$ で振動し，その形のまま速さ $\dfrac{1}{\sqrt{\varepsilon_0 \mu_0}}$ で $+z$ 方向へ進みます。

### (7)
導体間は真空なので $\varepsilon = \varepsilon_0$，$\mu = \mu_0$，$\sigma = 0$ です。任意の $z = z_0$ において，導体間の電場 $\boldsymbol{E}$ は $y$ に依存しないため，2枚の導体間の電位差の大きさ $V(z_0)$ は

$$
V(z_0) = b|\boldsymbol{E}(z_0)|
$$

です。また幅 $a$ の導体板を流れる全電流の大きさ $I(z_0)$ は，設問6より表面電流密度の大きさが $|\boldsymbol{K}(z_0)| = |\boldsymbol{H}(z_0)|$ なので，

$$
I(z_0) = a|\boldsymbol{H}(z_0)|
$$

となります。設問4の結果 $|\boldsymbol{E}| / |\boldsymbol{H}| = \sqrt{\dfrac{\mu_0}{\varepsilon_0}}$ を用いて比を求めます。

$$
\begin{aligned}
\frac{V(z_0)}{I(z_0)} &= \frac{b|\boldsymbol{E}(z_0)|}{a|\boldsymbol{H}(z_0)|} \\
&= \frac{b}{a}\sqrt{\frac{\mu_0}{\varepsilon_0}}
\end{aligned}
$$

$$
\finalanswer{\frac{b}{a}\sqrt{\frac{\mu_0}{\varepsilon_0}}}
$$
