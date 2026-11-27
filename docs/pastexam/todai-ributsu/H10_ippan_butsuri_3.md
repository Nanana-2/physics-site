---
title: 東大理物 平成10年度 一般教育科目 物理学 第3問：理想気体のマイヤーの関係・ポアソンの法則とディーゼル機関の断熱圧縮
tags:
  - 院試過去問
  - 東大理物
  - 熱力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成10年度
exam_subject: 一般教育科目 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成10年度 一般教育科目 物理学 第3問：理想気体のマイヤーの関係・ポアソンの法則とディーゼル機関の断熱圧縮

## 問題

気体の比熱においては，その体積を一定に保ちながら測る場合の定積比熱 $C_V = (\delta Q/\mathrm{d}T)_V$ と，圧力を一定に保ちながら測る場合の定圧比熱 $C_p = (\delta Q/\mathrm{d}T)_p$ とは値が異なる。但し，$T$ は温度，$V$ は体積，$p$ は圧力，$Q$ は熱量である。
{: .problem-lead }

(1) 1モルの理想気体の状態方程式を書き，これを用いて理想気体1モルの $C_V$ と $C_p$ の関係を導け。但し，気体定数を $R$ とせよ。

(2) 理想気体が準静的な断熱変化をするときに

$$
C_V\mathrm{d}T + p\mathrm{d}V = 0
$$

が成り立つことを示せ。

(3) 理想気体が準静的な断熱変化をするときに

$$
p V^{C_p/C_V} = \text{一定}
$$

が成り立つことを示せ。

(4) ディーゼル機関ではシリンダー内で空気を圧縮して温度を上げ，重油の霧を点火させる。この圧縮が準静的かつ断熱的に行われ，空気は理想気体であると仮定しよう。重油の霧の点火温度が $627\,^\circ\mathrm{C}$ の場合，シリンダー内の空気の体積を何分の一に圧縮させればこの点火温度に達するか，有効数字2桁で計算せよ。但し圧縮前の空気の温度は $27\,^\circ\mathrm{C}$ であり，空気の比熱比は $C_p/C_V = \dfrac{7}{5}$ とする。

> 出典：東京大学大学院理学系研究科物理学専攻 平成10年度 一般教育科目 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
理想気体の状態方程式と熱力学第1法則，および理想気体の内部エネルギーが温度のみの関数であるというジュールの法則を用いて，マイヤーの関係式 $C_p - C_V = R$ と準静的断熱変化の微分方程式，さらにポアソンの法則 $pV^{C_p/C_V} = \text{const.}$ を順に導きます。

最後にポアソンの法則を温度と体積の関係式 $TV^{\gamma - 1} = \text{const.}$ に書き換え，摂氏温度を絶対温度に換算してディーゼル機関に必要な圧縮比を計算します。
</div>

### (1)

1モルの理想気体の状態方程式は次の通りです。

$$
pV = RT
$$

熱力学第1法則より，準静的過程において系が吸収する微小熱量 $\delta Q$ は内部エネルギー $U$ の変化 $\mathrm{d}U$ と外部にする仕事 $p\mathrm{d}V$ の和で与えられます。

$$
\delta Q = \mathrm{d}U + p\mathrm{d}V
$$

体積一定の過程では $\mathrm{d}V = 0$ なので，定積モル比熱 $C_V$ は次式で表されます。

$$
C_V = \left(\frac{\delta Q}{\mathrm{d}T}\right)_V = \left(\frac{\partial U}{\partial T}\right)_V
$$

理想気体の内部エネルギー $U$ は温度 $T$ のみの関数（$U = U(T)$）であるため，任意の過程において $\mathrm{d}U = C_V\mathrm{d}T$ が成り立ちます。

一方，圧力一定の過程では状態方程式の微分 $p\mathrm{d}V + V\mathrm{d}p = R\mathrm{d}T$ で $\mathrm{d}p = 0$ とすると $p\mathrm{d}V = R\mathrm{d}T$ となります。したがって定圧過程での熱量は次の通りです。

$$
\begin{aligned}
\delta Q &= \mathrm{d}U + p\mathrm{d}V \\
&= C_V\mathrm{d}T + R\mathrm{d}T \\
&= (C_V + R)\mathrm{d}T
\end{aligned}
$$

これを $\mathrm{d}T$ で割ると定圧モル比熱 $C_p = \left(\dfrac{\delta Q}{\mathrm{d}T}\right)_p$ が得られ，マイヤーの関係式が導かれます。

$$
C_p - C_V = R
$$

$$
\finalanswer{pV = RT,\qquad C_p - C_V = R}
$$

### (2)

(1) で示したように，理想気体の内部エネルギー $U$ は温度 $T$ のみの関数であり，任意の微小変化に対して $\mathrm{d}U = C_V\mathrm{d}T$ が成り立ちます。

準静的な断熱変化では外界との熱のやり取りがないため $\delta Q = 0$ です。これを熱力学第1法則 $\delta Q = \mathrm{d}U + p\mathrm{d}V$ に代入します。

$$
0 = C_V\mathrm{d}T + p\mathrm{d}V
$$

したがって次式が成り立ちます。

$$
C_V\mathrm{d}T + p\mathrm{d}V = 0
$$

### (3)

1モルの理想気体の状態方程式 $pV = RT$ の両辺の全微分をとると，

$$
p\mathrm{d}V + V\mathrm{d}p = R\mathrm{d}T
$$

より $\mathrm{d}T = \dfrac{p\mathrm{d}V + V\mathrm{d}p}{R}$ です。これを (2) の式に代入します。

$$
C_V\frac{p\mathrm{d}V + V\mathrm{d}p}{R} + p\mathrm{d}V = 0
$$

両辺に $R$ を掛けて整理し，(1) のマイヤーの関係式 $C_V + R = C_p$ を用います。

$$
\begin{aligned}
C_V V\mathrm{d}p + (C_V + R)p\mathrm{d}V &= 0 \\
C_V V\mathrm{d}p + C_p p\mathrm{d}V &= 0
\end{aligned}
$$

両辺を $C_V pV$ で割って変数分離します。

$$
\frac{\mathrm{d}p}{p} + \frac{C_p}{C_V}\frac{\mathrm{d}V}{V} = 0
$$

比熱比 $\gamma = \dfrac{C_p}{C_V}$ を定数として両辺を積分すると，積分定数 $C$ を用いて次式が得られます。

$$
\ln p + \frac{C_p}{C_V}\ln V = C
$$

すなわち $\ln\left(p V^{C_p/C_V}\right) = C$ となり，ポアソンの法則が導かれます。

$$
p V^{C_p/C_V} = e^C = \text{const.}
$$

### (4)

比熱比を $\gamma = \dfrac{7}{5}$ とおきます。(3) のポアソンの法則 $p V^\gamma = \text{const.}$ に状態方程式 $p = \dfrac{RT}{V}$ を代入すると，温度 $T$ と体積 $V$ の関係式が得られます。

$$
T V^{\gamma - 1} = \text{const.}
$$

圧縮前の状態を $(T_1, V_1)$，点火温度に達した圧縮後の状態を $(T_2, V_2)$ とします。絶対温度に換算すると $T_1 = 300\,\mathrm{K}$（$27\,^\circ\mathrm{C}$），$T_2 = 900\,\mathrm{K}$（$627\,^\circ\mathrm{C}$）です。

$T_1 V_1^{\gamma - 1} = T_2 V_2^{\gamma - 1}$ より体積比 $\dfrac{V_1}{V_2}$ を求めます。ここで $\gamma - 1$ の値は $\dfrac{2}{5}$ なので，$\dfrac{1}{\gamma - 1} = \dfrac{5}{2}$ です。

$$
\begin{aligned}
\frac{V_1}{V_2} &= \left(\frac{T_2}{T_1}\right)^{1/(\gamma - 1)} \\
&= \left(\frac{900}{300}\right)^{5/2} \\
&= 3^{5/2} \\
&= 9\sqrt{3}
\end{aligned}
$$

$\sqrt{3} \approx 1.732$ を代入すると，

$$
9\sqrt{3} \approx 15.59
$$

となります。有効数字2桁で表すと $\dfrac{V_1}{V_2} \approx 16$，すなわち体積を $\dfrac{1}{16}$ に圧縮すれば点火温度に達します。

$$
\finalanswer{\frac{1}{16}}
$$
