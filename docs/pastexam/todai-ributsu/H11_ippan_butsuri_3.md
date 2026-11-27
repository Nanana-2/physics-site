---
title: 東大理物 平成11年度 一般教育科目 物理学 第3問：理想気体中の音波の伝播・気柱共鳴と屈折
tags:
  - 院試過去問
  - 東大理物
  - 熱力学
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 一般教育科目 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成11年度 一般教育科目 物理学 第3問：理想気体中の音波の伝播・気柱共鳴と屈折

## 問題

媒質中を伝播する音は，媒質の密度の波である。$\Delta\rho$ を平均密度 $\rho$ からのずれとすると，$x$ 方向に伝播する音波は，波動方程式

$$
k\frac{\partial^2(\Delta\rho)}{\partial x^2} = \frac{\partial^2(\Delta\rho)}{\partial t^2}
$$

に従う。ここで $k$ は，断熱過程での $\rho$ に対する圧力 $P$ の変化率

$$
k = \left.\frac{\mathrm{d}P}{\mathrm{d}\rho}\right|_{\text{断熱過程}}
$$

である。

媒質が，温度 $T$ の理想気体である場合について，以下の問いに答えよ。ただし，理想気体の分子量を $M$，定積比熱に対する定圧比熱の比を $\gamma$，気体定数を $R$ とする。
{: .problem-lead }

(1) 理想気体の圧力 $P$ が，$P = \rho RT/M$ と表されることを示せ。

(2) $k$ を，$M$，$\gamma$，$T$ および $R$ を用いて表せ。ただし，断熱過程では，$P/\rho^\gamma = \text{一定}$ であることを用いてよい。

(3) ヘリウムガス（$M = 4.0$，$\gamma = 5/3$）中の音速は，同じ温度の窒素ガス（$M = 28.0$，$\gamma = 7/5$）中の音速の何倍になるか，有効数字2桁で答えよ。

(4) 理想気体中に，片端を閉じ他端を開いた長さ $\ell$ の管をおく。管の中の気柱にたつ音の基本定在波の振動数 $\nu_0$ を，音速を $v$ として，求めよ。それに基づいて，ヘリウムガス中と窒素ガス中での $\nu_0$ の違いを簡潔に説明せよ。

(5) 同じ温度のヘリウムガスと窒素ガスが，図のように薄膜で隔てられているとき，ヘリウムガス中から斜めに入射した音波はどのように進むか，図示し簡潔に説明せよ。

<figure class="problem-figure" markdown>
![ヘリウムガスから窒素ガスへの薄膜境界面に入射する音波](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_3-p-light.svg#only-light){ loading=lazy }
![ヘリウムガスから窒素ガスへの薄膜境界面に入射する音波](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_3-p-dark.svg#only-dark){ loading=lazy }
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 一般教育科目 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
理想気体の状態方程式を密度で書き換え，断熱関係式 $P/\rho^\gamma = \text{const.}$ を微分することで音速の2乗 $k = v^2$ を導きます。

得られた音速の公式 $v = \sqrt{\gamma RT/M}$ を用いてヘリウムガスと窒素ガスの音速比を評価し，閉管の基本振動数の違いと，薄膜境界面における音波の反射およびスネルの法則による屈折の向きを導きます。
</div>

### (1)

体積 $V$ の中に物質量 $n$ の理想気体が入っているとすると，理想気体の状態方程式は

$$
PV = nRT
$$

です。分子量を $M$ とすると，この気体の全質量は $m = nM$ となるため，密度 $\rho$ は次式で与えられます。

$$
\begin{aligned}
\rho &= \frac{m}{V} \\
&= \frac{nM}{V}
\end{aligned}
$$

これより $\dfrac{n}{V} = \dfrac{\rho}{M}$ が得られます。状態方程式の両辺を $V$ で割ってこれを代入すると，求める関係式が得られます。

$$
\begin{aligned}
P &= \frac{n}{V}RT \\
&= \frac{\rho RT}{M}
\end{aligned}
$$

<aside class="rigor-note" markdown>
SI単位系で厳密に書く場合，分子量 $M$ は無次元量でありモル質量は $M_{\mathrm{mol}} = M \times 10^{-3}\,\mathrm{kg/mol}$ ですが，本問では $1\,\mathrm{mol}$ 当たりの質量をそのまま $M$ と記す慣用表記が用いられています。
</aside>

### (2)

断熱過程では定数 $C$ を用いて $P = C\rho^\gamma$ と表されます。これを $\rho$ で微分して $k$ を計算します。

$$
\begin{aligned}
k &= \left.\frac{\mathrm{d}P}{\mathrm{d}\rho}\right|_{S} \\
&= \gamma C \rho^{\gamma - 1} \\
&= \gamma\frac{P}{\rho}
\end{aligned}
$$

ここに (1) で示した $P = \dfrac{\rho RT}{M}$ を代入します。

$$
\finalanswer{k = \frac{\gamma RT}{M}}
$$

### (3)

波動方程式 $k\dfrac{\partial^2(\Delta\rho)}{\partial x^2} = \dfrac{\partial^2(\Delta\rho)}{\partial t^2}$ を標準形 $v^2\dfrac{\partial^2 u}{\partial x^2} = \dfrac{\partial^2 u}{\partial t^2}$ と比較すると，音速 $v$ は $v = \sqrt{k}$ で与えられます。

$$
v = \sqrt{\frac{\gamma RT}{M}}
$$

同じ温度 $T$ におけるヘリウムガス（$M_{\mathrm{He}} = 4.0$，$\gamma_{\mathrm{He}} = \dfrac{5}{3}$）中の音速 $v_{\mathrm{He}}$ と，窒素ガス（$M_{\mathrm{N_2}} = 28.0$，$\gamma_{\mathrm{N_2}} = \dfrac{7}{5}$）中の音速 $v_{\mathrm{N_2}}$ の比を計算します。

$$
\begin{aligned}
\frac{v_{\mathrm{He}}}{v_{\mathrm{N_2}}} &= \sqrt{\frac{\gamma_{\mathrm{He}}}{\gamma_{\mathrm{N_2}}}\cdot\frac{M_{\mathrm{N_2}}}{M_{\mathrm{He}}}} \\
&= \sqrt{\frac{5/3}{7/5}\cdot\frac{28.0}{4.0}} \\
&= \sqrt{\frac{25}{21}\cdot 7} \\
&= \sqrt{\frac{25}{3}} \\
&= \frac{5}{\sqrt{3}} \\
&\approx 2.887
\end{aligned}
$$

有効数字2桁に丸めると $2.9$ 倍となります。

$$
\finalanswer{\frac{v_{\mathrm{He}}}{v_{\mathrm{N_2}}} \approx 2.9}
$$

### (4)

片端を閉じ他端を開いた長さ $\ell$ の閉管では，開口端補正を無視すると閉端が変位の節，開端が変位の腹となります。最も波長の長い基本定在波では，管の長さ $\ell$ にちょうど $\dfrac{1}{4}$ 波長が収まります。

$$
\ell = \frac{\lambda_0}{4}
$$

よって基本波長は $\lambda_0 = 4\ell$ であり，波の基本式 $v = \nu_0\lambda_0$ より基本振動数 $\nu_0$ は次のように求まります。

$$
\nu_0 = \frac{v}{4\ell}
$$

基本振動数 $\nu_0$ は音速 $v$ に比例します。(3) の結果より，同温度のヘリウムガス中の音速は窒素ガス中の音速の約 $2.9$ 倍であるため，ヘリウムガス中での基本振動数 $\nu_0$ は窒素ガス中での基本振動数の約 $2.9$ 倍高くなります。

$$
\finalanswer{\nu_0 = \frac{v}{4\ell}}
$$

### (5)

ヘリウムガス中の音速を $v_1 = v_{\mathrm{He}}$，窒素ガス中の音速を $v_2 = v_{\mathrm{N_2}}$ とします。薄膜境界面へ入射角 $\theta_1$ で斜めに入射した音波は，境界面で一部が反射角 $\theta_1$ でヘリウムガス中へ反射し，残りは窒素ガス中へ屈折して透過します。

屈折角を $\theta_2$ とすると，スネルの法則より次式が成り立ちます。

$$
\frac{\sin\theta_1}{\sin\theta_2} = \frac{v_1}{v_2}
$$

(3) より $\dfrac{v_1}{v_2} = \dfrac{5}{\sqrt{3}} > 1$ なので，$\sin\theta_2 = \dfrac{v_2}{v_1}\sin\theta_1 < \sin\theta_1$ が常に成り立ちます。したがって，入射角 $\theta_1$ の値によらず全反射は起こらず，透過した音波は入射角より小さい屈折角 $\theta_2 < \theta_1$ で，薄膜の法線に近づく向きに折れ曲がって窒素ガス中へ進みます。

音波の進行の様子を図示すると次の通りです。

![薄膜境界面における音波の反射と屈折](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_3-s-light.svg#only-light){ loading=lazy }
![薄膜境界面における音波の反射と屈折](../../assets/figures/pastexam-todai-ributsu/H11_ippan_butsuri_3-s-dark.svg#only-dark){ loading=lazy }
