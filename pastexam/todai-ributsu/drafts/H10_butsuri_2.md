---
title: 東大理物 平成10年度 物理学 第2問：電磁波の境界条件・完全導体反射と誘電体板の透過強度
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成10年度 物理学 第2問：電磁波の境界条件・完全導体反射と誘電体板の透過強度

## 問題

異なる媒質の境界面において，電磁波の満たす境界条件は一般に次のように与えられる。

$$
\begin{aligned}
E_{\mathrm{t}}(\mathrm{I}) - E_{\mathrm{t}}(\mathrm{II}) &= 0 \qquad \text{(1)} \\
D_{\mathrm{n}}(\mathrm{I}) - D_{\mathrm{n}}(\mathrm{II}) &= Q \qquad \text{(2)} \\
H_{\mathrm{t}}(\mathrm{I}) - H_{\mathrm{t}}(\mathrm{II}) &= J \qquad \text{(3)} \\
B_{\mathrm{n}}(\mathrm{I}) - B_{\mathrm{n}}(\mathrm{II}) &= 0 \qquad \text{(4)}
\end{aligned}
$$

ここに，$E$ は電場，$D$ は電束密度，$H$ は磁場，$B$ は磁束密度である。添字 $\mathrm{t}$，$\mathrm{n}$ は境界面に平行，垂直な成分をそれぞれ表わす。また，$(\mathrm{I})$，$(\mathrm{II})$ は媒質を示し，$Q$ は表面電荷密度，$J$ は表面電流密度である。
{: .problem-lead }

(1) マックスウェルの方程式とストークスの定理を用いて，式 (1) が成り立つことを示せ。

(2) マックスウェルの方程式とガウスの定理を用いて，式 (2) が成り立つことを示せ。

(3) 媒質 $(\mathrm{II})$ が完全導体である場合，その表面において電磁波の満たすべき境界条件を求めよ。

(4) 媒質 $(\mathrm{I})$ が真空，媒質 $(\mathrm{II})$ が完全導体とする。真空側（$x < 0$）から導体面（$yz$ 平面）に入射する平面波の電磁波を考える。この入射平面波は単色で $y$ 方向に偏光しており，

$$
E_y = E_0 \exp(-2\pi i\nu t + ikx) \qquad \text{(5)}
$$

で与えられる。ここに $\nu$ は電磁波の振動数，$k$ は波数である。これが金属表面（$x = 0$）で反射されるとき，導体面に流れる表面電流密度を求めよ。また，その方向を示せ。ただし，真空の誘電率と透磁率をそれぞれ $\varepsilon_0$，$\mu_0$ とする。

(5) 次に，媒質 $(\mathrm{I})$，$(\mathrm{II})$ が異なる誘電体であるとする。これらが，$yz$ 平面を境に互いに接している。ここに，$x < 0$ から (5) 式で与えられる平面波の電磁波が入射した。境界条件の式 (1)〜(4) を適用し，$x = 0$ の境界面における反射率（反射波と入射波の電場の比），および，透過率（透過波と入射波の電場の比）をそれぞれ求めよ。ただし，媒質 $(\mathrm{I})$ の誘電率を $\varepsilon_1$，媒質 $(\mathrm{II})$ の誘電率を $\varepsilon_2$ とし，透磁率はいずれも $\mu_0$ とする。

(6) 平行な境界面をもつ誘電体の板が真空中に置かれている。その境界面に垂直な方向から電場の振幅が $E_0$ である平面波の電磁波が入射する。平面波の振動数を $\nu$，板の厚さを $L$ とするとき，この板を透過する電磁波の強度（ポインティングベクトルの大きさ）を求めよ。ただし，誘電体の誘電率を $\varepsilon_1$，真空の誘電率を $\varepsilon_0$ とし，透磁率はいずれも $\mu_0$ とする。

(7) 前問で，振動数 $\nu$ の電磁波に対して，透過する電磁波の強度が最大になるような $L$ を求めよ。また，その時の透過強度の入射強度に対する比を求めよ。これらの結果についての物理的意味を考察し，簡潔に述べよ。以上の結果は，眼鏡の反射防止コーティングや干渉フィルターなどに広く応用されている。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
マクスウェル方程式の積分形から異なる媒質間の境界条件を導出し，完全導体表面での垂直入射反射と表面電流密度，さらに誘電体境界面でのフレネル振幅反射率・透過率を求めます。

後半では，厚さ $L$ の誘電体板の両境界面 $x = 0, L$ で電場・磁場の接線成分を連立させて透過振幅を求め，時間平均ポインティングベクトルから透過強度と完全透過の共振条件を導出します。
</div>

### (1)

ファラデーの電磁誘導の法則

$$
\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}
$$

を用います。媒質 $(\mathrm{I})$ と媒質 $(\mathrm{II})$ の境界面を垂直にまたぐ微小な長方形閉経路 $C$ をとります。境界面に平行な辺の長さを $\Delta l$，垂直な辺の長さを $\Delta h$ とし，閉経路 $C$ が囲む長方形領域を $S$，その面積ベクトルを $\mathrm{d}\mathbf{S}$ とします。

ファラデーの法則を曲面 $S$ 上で面積分し，左辺にストークスの定理を用います。

$$
\oint_C \mathbf{E}\cdot\mathrm{d}\mathbf{l} = -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot\mathrm{d}\mathbf{S}
$$

長方形の各辺に沿う線積分は，$\Delta h \to 0$ の極限で垂直な2辺の寄与が $O(\Delta h) \to 0$ となり消えます。また右辺の面積分も，境界面上で $\dfrac{\partial\mathbf{B}}{\partial t}$ が有限であるため面積 $\Delta l\Delta h \to 0$ とともに $0$ に収束します。残る平行な2辺の寄与より次式が得られます。

$$
\bigl(E_{\mathrm{t}}(\mathrm{I}) - E_{\mathrm{t}}(\mathrm{II})\bigr)\Delta l = 0
$$

$\Delta l \neq 0$ で割ると，式 (1) が導かれます。

$$
E_{\mathrm{t}}(\mathrm{I}) - E_{\mathrm{t}}(\mathrm{II}) = 0
$$

### (2)

電束密度に対するガウスの法則

$$
\nabla\cdot\mathbf{D} = \rho
$$

を用います。境界面をまたぐ底面積 $\Delta S$，高さ $\Delta h$ の微小な円柱をとり，その体積を $V$，表面を $\partial V$ とします。法線ベクトルは媒質 $(\mathrm{II})$ から媒質 $(\mathrm{I})$ へ向かう向きを正にとります。

ガウスの法則を体積 $V$ で積分し，左辺にガウスの発散定理を用います。

$$
\oint_{\partial V} \mathbf{D}\cdot\mathrm{d}\mathbf{S} = \int_V \rho\,\mathrm{d}V
$$

ここで $\Delta h \to 0$ の極限をとります。左辺では円柱側面の面積が $O(\Delta h) \to 0$ となるため側面の寄与が消え，上下の底面のみが残ります。右辺では体積電荷の寄与が $O(\Delta h) \to 0$ となり，境界面上の表面電荷密度 $Q$ のみが残って $Q\Delta S$ となります。

$$
\bigl(D_{\mathrm{n}}(\mathrm{I}) - D_{\mathrm{n}}(\mathrm{II})\bigr)\Delta S = Q\Delta S
$$

両辺を $\Delta S$ で割ると，式 (2) が導かれます。

$$
D_{\mathrm{n}}(\mathrm{I}) - D_{\mathrm{n}}(\mathrm{II}) = Q
$$

### (3)

電気伝導率 $\sigma \to \infty$ の完全導体の内部では，有限の電流密度に対してオームの法則 $\mathbf{j} = \sigma\mathbf{E}$ より電場が $\mathbf{E}(\mathrm{II}) = \mathbf{0}$ であり，したがって $\mathbf{D}(\mathrm{II}) = \mathbf{0}$ となります。さらに時間変動する電磁波に対してはファラデーの法則より $\dfrac{\partial\mathbf{B}}{\partial t} = \mathbf{0}$ となるため変動磁場も存在せず，$\mathbf{B}(\mathrm{II}) = \mathbf{0}$，$\mathbf{H}(\mathrm{II}) = \mathbf{0}$ となります。

これらを一般の境界条件 (1)〜(4) に代入すると，完全導体表面において媒質 $(\mathrm{I})$ 側の電磁波が満たすべき境界条件は次の4式となります。

$$
\finalanswer{\begin{aligned}
E_{\mathrm{t}}(\mathrm{I}) &= 0 \\
D_{\mathrm{n}}(\mathrm{I}) &= Q \\
H_{\mathrm{t}}(\mathrm{I}) &= J \\
B_{\mathrm{n}}(\mathrm{I}) &= 0
\end{aligned}}
$$

### (4)

$x < 0$ の真空領域から $+x$ 方向に進む入射波の電場を

$$
E_{y,\mathrm{i}}(x, t) = E_0 e^{-i\omega t + ikx}
$$

とします。ここで $\omega = 2\pi\nu$，真空中の波数は $k = \omega\sqrt{\varepsilon_0\mu_0}$ です。ファラデーの法則 $\nabla\times\mathbf{E} = -\mu_0\dfrac{\partial\mathbf{H}}{\partial t}$ より，入射波の磁場は $z$ 成分のみをもちます。

$$
\begin{aligned}
i\omega\mu_0 H_{z,\mathrm{i}} &= \frac{\partial E_{y,\mathrm{i}}}{\partial x} \\
&= ik E_{y,\mathrm{i}}
\end{aligned}
$$

$\dfrac{k}{\omega\mu_0} = \sqrt{\dfrac{\varepsilon_0}{\mu_0}}$ なので，入射波の磁場は次式で与えられます。

$$
H_{z,\mathrm{i}}(x, t) = \sqrt{\frac{\varepsilon_0}{\mu_0}}\,E_0 e^{-i\omega t + ikx}
$$

$-x$ 方向に反射する反射波の電場を $E_{y,\mathrm{r}}(x, t) = E_{\mathrm{r}} e^{-i\omega t - ikx}$ とすると，同様にして反射波の磁場は

$$
H_{z,\mathrm{r}}(x, t) = -\sqrt{\frac{\varepsilon_0}{\mu_0}}\,E_{\mathrm{r}} e^{-i\omega t - ikx}
$$

となります。完全導体表面 $x = 0$ での境界条件 $E_y(0, t) = 0$ より，$E_0 + E_{\mathrm{r}} = 0$ すなわち $E_{\mathrm{r}} = -E_0$ です。

よって導体表面 $x = 0$ の真空側における全磁場は次のように求まります。

$$
\begin{aligned}
H_z(0, t) &= H_{z,\mathrm{i}}(0, t) + H_{z,\mathrm{r}}(0, t) \\
&= 2\sqrt{\frac{\varepsilon_0}{\mu_0}}\,E_0 e^{-2\pi i\nu t}
\end{aligned}
$$

完全導体表面の境界条件をベクトル形で書くと，媒質 $(\mathrm{II})$ から $(\mathrm{I})$ へ向かう単位法線ベクトル $\mathbf{n} = -\hat{\mathbf{x}}$ を用いて $\mathbf{J} = \mathbf{n} \times \mathbf{H}(\mathrm{I})$ です。成分を計算します。

$$
\begin{aligned}
\mathbf{J} &= (-\hat{\mathbf{x}}) \times \bigl(H_z(0, t)\,\hat{\mathbf{z}}\bigr) \\
&= H_z(0, t)\,\hat{\mathbf{y}} \\
&= 2\sqrt{\frac{\varepsilon_0}{\mu_0}}\,E_0 e^{-2\pi i\nu t}\,\hat{\mathbf{y}}
\end{aligned}
$$

したがって複素振幅表示での表面電流密度は $J_y = 2\sqrt{\dfrac{\varepsilon_0}{\mu_0}}\,E_0\exp(-2\pi i\nu t)$ であり，その方向は入射電場の偏光方向と平行な $y$ 軸方向です。

$$
\finalanswer{\mathbf{J} = 2\sqrt{\frac{\varepsilon_0}{\mu_0}}\,E_0 \exp(-2\pi i\nu t)\,\hat{\mathbf{y}}}
$$

### (5)

角振動数を $\omega = 2\pi\nu$ とし，媒質 $(\mathrm{I})$ および媒質 $(\mathrm{II})$ での波数をそれぞれ $k_1 = \omega\sqrt{\varepsilon_1\mu_0}$，$k_2 = \omega\sqrt{\varepsilon_2\mu_0}$ とします。入射波，反射波，透過波の電場（$y$ 成分）および対応する磁場（$z$ 成分）を各領域ごとに表します。

まず媒質 $(\mathrm{I})$（$x < 0$）での電磁場は次の通りです。

$$
\begin{aligned}
E_y(\mathrm{I}) &= \left(E_0 e^{ik_1 x} + E_{\mathrm{r}} e^{-ik_1 x}\right)e^{-i\omega t} \\
H_z(\mathrm{I}) &= \sqrt{\frac{\varepsilon_1}{\mu_0}}\left(E_0 e^{ik_1 x} - E_{\mathrm{r}} e^{-ik_1 x}\right)e^{-i\omega t}
\end{aligned}
$$

次に媒質 $(\mathrm{II})$（$x > 0$）での電磁場は次の通りです。

$$
\begin{aligned}
E_y(\mathrm{II}) &= E_{\mathrm{t}} e^{ik_2 x - i\omega t} \\
H_z(\mathrm{II}) &= \sqrt{\frac{\varepsilon_2}{\mu_0}}\,E_{\mathrm{t}} e^{ik_2 x - i\omega t}
\end{aligned}
$$

誘電体境界面 $x = 0$ には自由表面電流が存在しないため $J = 0$ です。境界条件 (1) と (3) より $E_y$ と $H_z$ が $x = 0$ で連続となります。

$$
\begin{aligned}
E_0 + E_{\mathrm{r}} &= E_{\mathrm{t}} \\
\sqrt{\varepsilon_1}(E_0 - E_{\mathrm{r}}) &= \sqrt{\varepsilon_2}\,E_{\mathrm{t}}
\end{aligned}
$$

第1式を第2式に代入して $E_{\mathrm{r}}/E_0$ を求めます。

$$
\begin{aligned}
\sqrt{\varepsilon_1}(E_0 - E_{\mathrm{r}}) &= \sqrt{\varepsilon_2}(E_0 + E_{\mathrm{r}}) \\
\left(\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}\right)E_{\mathrm{r}} &= \left(\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2}\right)E_0
\end{aligned}
$$

これより振幅反射率 $r = \dfrac{E_{\mathrm{r}}}{E_0}$ および振幅透過率 $t = \dfrac{E_{\mathrm{t}}}{E_0}$ は $t = 1 + r$ を用いて次のように得られます。

$$
\finalanswer{r = \frac{\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2}}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}},\qquad t = \frac{2\sqrt{\varepsilon_1}}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}}}
$$

### (6)

誘電体板が $0 \le x \le L$ の領域にあり，その両側（$x < 0$ と $x > L$）が真空であるとします。角振動数を $\omega = 2\pi\nu$ とし，真空および誘電体中の波数と波動アドミタンスを次のように置きます。

$$
\begin{aligned}
k_0 &= 2\pi\nu\sqrt{\varepsilon_0\mu_0}, & Y_0 &= \sqrt{\frac{\varepsilon_0}{\mu_0}} \\
k_1 &= 2\pi\nu\sqrt{\varepsilon_1\mu_0}, & Y_1 &= \sqrt{\frac{\varepsilon_1}{\mu_0}}
\end{aligned}
$$

時間因子 $e^{-i\omega t}$ を省略して各領域の電場 $E_y(x)$ と磁場 $H_z(x)$ を書きます。

- 真空領域 $x < 0$：$E_y = E_0 e^{ik_0 x} + E_{\mathrm{r}} e^{-ik_0 x}$，$H_z = Y_0(E_0 e^{ik_0 x} - E_{\mathrm{r}} e^{-ik_0 x})$
- 誘電体領域 $0 \le x \le L$：$E_y = A e^{ik_1 x} + B e^{-ik_1 x}$，$H_z = Y_1(A e^{ik_1 x} - B e^{-ik_1 x})$
- 真空領域 $x > L$：$E_y = E_{\mathrm{t}} e^{ik_0(x - L)}$，$H_z = Y_0 E_{\mathrm{t}} e^{ik_0(x - L)}$

まず $x = L$ における $E_y$ と $H_z$ の連続条件を書き下します。

$$
\begin{aligned}
A e^{ik_1 L} + B e^{-ik_1 L} &= E_{\mathrm{t}} \\
Y_1\left(A e^{ik_1 L} - B e^{-ik_1 L}\right) &= Y_0 E_{\mathrm{t}}
\end{aligned}
$$

これを $A, B$ について解きます。

$$
\begin{aligned}
A &= \frac{1}{2}\left(1 + \frac{Y_0}{Y_1}\right)E_{\mathrm{t}} e^{-ik_1 L} \\
B &= \frac{1}{2}\left(1 - \frac{Y_0}{Y_1}\right)E_{\mathrm{t}} e^{ik_1 L}
\end{aligned}
$$

次に $x = 0$ における $E_y$ と $H_z$ の連続条件を書き下します。

$$
\begin{aligned}
E_0 + E_{\mathrm{r}} &= A + B \\
Y_0(E_0 - E_{\mathrm{r}}) &= Y_1(A - B)
\end{aligned}
$$

第2式の両辺を $Y_0$ で割ってから第1式と足し合わせ，$E_{\mathrm{r}}$ を消去します。

$$
2E_0 = \left(1 + \frac{Y_1}{Y_0}\right)A + \left(1 - \frac{Y_1}{Y_0}\right)B
$$

ここに先ほどの $A, B$ を代入して整理します。

$$
\begin{aligned}
\frac{E_0}{E_{\mathrm{t}}} &= \frac{1}{4}\left(1 + \frac{Y_1}{Y_0}\right)\left(1 + \frac{Y_0}{Y_1}\right)e^{-ik_1 L} + \frac{1}{4}\left(1 - \frac{Y_1}{Y_0}\right)\left(1 - \frac{Y_0}{Y_1}\right)e^{ik_1 L} \\
&= \frac{e^{-ik_1 L} + e^{ik_1 L}}{2} - \frac{1}{2}\left(\frac{Y_1}{Y_0} + \frac{Y_0}{Y_1}\right)\frac{e^{ik_1 L} - e^{-ik_1 L}}{2} \\
&= \cos(k_1 L) - \frac{i}{2}\left(\sqrt{\frac{\varepsilon_1}{\varepsilon_0}} + \sqrt{\frac{\varepsilon_0}{\varepsilon_1}}\right)\sin(k_1 L)
\end{aligned}
$$

絶対値の2乗を計算します。

$$
\begin{aligned}
\left|\frac{E_0}{E_{\mathrm{t}}}\right|^2 &= \cos^2(k_1 L) + \frac{1}{4}\left(\frac{\varepsilon_1}{\varepsilon_0} + 2 + \frac{\varepsilon_0}{\varepsilon_1}\right)\sin^2(k_1 L) \\
&= 1 + \frac{1}{4}\left(\frac{\varepsilon_1}{\varepsilon_0} - 2 + \frac{\varepsilon_0}{\varepsilon_1}\right)\sin^2(k_1 L) \\
&= 1 + \frac{(\varepsilon_1 - \varepsilon_0)^2}{4\varepsilon_0\varepsilon_1}\sin^2(k_1 L)
\end{aligned}
$$

透過波は真空中を伝播する単色平面波なので，その時間平均ポインティングベクトルの大きさ $I_{\mathrm{t}}$ は入射強度 $I_0 = \dfrac{1}{2}\sqrt{\dfrac{\varepsilon_0}{\mu_0}}\,E_0^2$ を用いて次式で与えられます。

$$
\begin{aligned}
I_{\mathrm{t}} &= \frac{1}{2}\sqrt{\frac{\varepsilon_0}{\mu_0}}\,|E_{\mathrm{t}}|^2 \\
&= \frac{\dfrac{1}{2}\sqrt{\dfrac{\varepsilon_0}{\mu_0}}\,E_0^2}{1 + \dfrac{(\varepsilon_1 - \varepsilon_0)^2}{4\varepsilon_0\varepsilon_1}\sin^2\left(2\pi\nu\sqrt{\varepsilon_1\mu_0}\,L\right)}
\end{aligned}
$$

$$
\finalanswer{I_{\mathrm{t}} = \frac{\dfrac{1}{2}\sqrt{\dfrac{\varepsilon_0}{\mu_0}}\,E_0^2}{1 + \dfrac{(\varepsilon_1 - \varepsilon_0)^2}{4\varepsilon_0\varepsilon_1}\sin^2\left(2\pi\nu\sqrt{\varepsilon_1\mu_0}\,L\right)}}
$$

### (7)

(6) で求めた透過強度 $I_{\mathrm{t}}$ の分母が最小値 $1$ をとるとき，$I_{\mathrm{t}}$ は最大になります。その条件は $\sin\left(2\pi\nu\sqrt{\varepsilon_1\mu_0}\,L\right) = 0$ です。$L > 0$ より，正の整数 $m = 1, 2, 3, \dots$ を用いて次式が得られます。

$$
2\pi\nu\sqrt{\varepsilon_1\mu_0}\,L = m\pi
$$

これを $L$ について解きます。

$$
L = \frac{m}{2\nu\sqrt{\varepsilon_1\mu_0}} \qquad (m = 1, 2, 3, \dots)
$$

このとき分母は $1$ となるため，透過強度 $I_{\mathrm{t}}$ の入射強度 $I_0 = \dfrac{1}{2}\sqrt{\dfrac{\varepsilon_0}{\mu_0}}\,E_0^2$ に対する比は次の通りです。

$$
\frac{I_{\mathrm{t}}}{I_0} = 1
$$

誘電体中の電磁波の波長は $\lambda_1 = \dfrac{1}{\nu\sqrt{\varepsilon_1\mu_0}}$ なので，最大透過条件は $L = m\dfrac{\lambda_1}{2}$ と書き換えられます。この条件のもとでは，板内を1往復する光路長 $2L = m\lambda_1$ が波長の整数倍となります。板の表面 $x = 0$ での真空から誘電体への反射波には位相のずれ $\pi$ が生じるのに対し，裏面 $x = L$ での誘電体から真空への反射波には位相のずれが生じないため，表面反射波と板内多重反射を経て戻る反射波とがちょうど逆位相で打ち消し合います。その結果，反射波全体が完全に消滅し，入射したエネルギーの $100\%$ が透過します。

$$
\finalanswer{L = \frac{m}{2\nu\sqrt{\varepsilon_1\mu_0}} \quad (m = 1, 2, 3, \dots),\qquad \frac{I_{\mathrm{t}}}{I_0} = 1}
$$
