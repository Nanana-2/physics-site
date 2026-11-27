---
title: 東大理物 平成9年度 一般教育科目 物理学 第3問：実在気体のエントロピー変化と状態方程式の決定
tags:
  - 院試過去問
  - 東大理物
  - 熱力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 一般教育科目 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成9年度 一般教育科目 物理学 第3問：実在気体のエントロピー変化と状態方程式の決定

## 問題

通常，気体は高温低密度の極限で理想気体に近づくが，一般には理想気体からのずれが観測される。このようなずれを示す気体1モルに対して，以下の設問に答えよ。
{: .problem-lead }

(1) この気体を体積 $V$ に保って熱容量を測定したところ，温度 $T_1 < T_2$ の間で，$C = 2.5R - gT^{-2}$ と表されることがわかった。但し，$R$ は気体定数であり，$g$ は温度によらない定数である。この測定で，温度 $T_1$ から温度 $T_2$ まで気体の温度を上昇させたときの気体のエントロピーの増加量を求めよ。

(2) 熱膨張率 $\alpha$ と等温圧縮率 $\kappa$ を測定したところ，次のような関数で表されることがわかった。

$$
\begin{aligned}
\alpha &\equiv \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p = \frac{1}{T}\left(1 + \frac{a}{VT}\right), & \qquad &\text{(i)} \\
\kappa &\equiv -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_T = \frac{1}{p}\left(1 + \frac{b}{VT}\right). & \qquad &\text{(ii)}
\end{aligned}
$$

但し，$V$，$T$，$p$ はそれぞれ気体の体積，温度，圧力である。また，$a$，$b$ は同じ次元を持つ定数である。$V$ の2階偏導関数を考えることにより，$a = 2b$ であることを証明せよ。

(3) この気体の状態方程式を以下の順で求めよう。

(イ) 先ず (ii) 式のみを用いて，等温過程における，$p$ と $V$ の関係を求めよ。

(ロ) (イ) の結果を (i) 式に代入して，状態方程式を決定せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 一般教育科目 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
定積過程でのエントロピー変化は定積熱容量 $C$ を $T$ で割って積分することで求まります。また，体積 $V(T, p)$ が状態量であることによる2階混合偏導関数の対称性 $\dfrac{\partial^2 V}{\partial p\partial T} = \dfrac{\partial^2 V}{\partial T\partial p}$ が熱膨張率 $\alpha$ と等温圧縮率 $\kappa$ の間の整合条件を与え，変数分離形の偏微分方程式を順に積分することで高温低密度極限の理想気体則から状態方程式が一意に決まります。
</div>

### (1)

体積 $V$ を一定に保つ準静的過程では，微小な温度変化 $\mathrm{d}T$ に対して気体が吸収する熱量は $\mathrm{d}'Q = C\,\mathrm{d}T$ であり，エントロピーの変化は $\mathrm{d}S = \dfrac{C}{T}\,\mathrm{d}T$ で与えられます。したがって，温度 $T_1$ から $T_2$ までのエントロピーの増加量 $\Delta S$ は次式のように積分できます。

$$
\begin{aligned}
\Delta S &= \int_{T_1}^{T_2} \frac{C}{T}\,\mathrm{d}T \\
&= \int_{T_1}^{T_2} \left(\frac{5R}{2T} - \frac{g}{T^3}\right)\mathrm{d}T \\
&= \left[\frac{5}{2}R\ln T + \frac{g}{2T^2}\right]_{T_1}^{T_2} \\
&= \frac{5}{2}R\ln\frac{T_2}{T_1} + \frac{g}{2}\left(\frac{1}{T_2^2} - \frac{1}{T_1^2}\right)
\end{aligned}
$$

$$
\finalanswer{\Delta S = \frac{5}{2}R\ln\frac{T_2}{T_1} + \frac{g}{2}\left(\frac{1}{T_2^2} - \frac{1}{T_1^2}\right)}
$$

### (2)

式 (i) と式 (ii) の両辺に $V$ を掛けると，$V(T, p)$ の1階偏導関数は次の形に整理できます。

$$
\begin{aligned}
\left(\frac{\partial V}{\partial T}\right)_p &= \frac{V}{T} + \frac{a}{T^2} \\
\left(\frac{\partial V}{\partial p}\right)_T &= -\frac{V}{p} - \frac{b}{pT}
\end{aligned}
$$

まず第1式を $T$ 一定のもとで $p$ で偏微分し，第2式を代入します。

$$
\begin{aligned}
\frac{\partial^2 V}{\partial p\,\partial T} &= \frac{1}{T}\left(\frac{\partial V}{\partial p}\right)_T \\
&= \frac{1}{T}\left(-\frac{V}{p} - \frac{b}{pT}\right) \\
&= -\frac{V}{pT} - \frac{b}{pT^2}
\end{aligned}
$$

次に第2式を $p$ 一定のもとで $T$ で偏微分し，第1式を代入します。

$$
\begin{aligned}
\frac{\partial^2 V}{\partial T\,\partial p} &= -\frac{1}{p}\left(\frac{\partial V}{\partial T}\right)_p + \frac{b}{pT^2} \\
&= -\frac{1}{p}\left(\frac{V}{T} + \frac{a}{T^2}\right) + \frac{b}{pT^2} \\
&= -\frac{V}{pT} + \frac{b - a}{pT^2}
\end{aligned}
$$

体積 $V(T, p)$ は状態量であり滑らかな関数なので，2階混合偏導関数の順序交換 $\dfrac{\partial^2 V}{\partial p\,\partial T} = \dfrac{\partial^2 V}{\partial T\,\partial p}$ が成り立ちます。両辺を比較すると

$$
-\frac{V}{pT} - \frac{b}{pT^2} = -\frac{V}{pT} + \frac{b - a}{pT^2}
$$

となり，$-b = b - a$ すなわち $a = 2b$ が導かれます。

### (3)

#### (イ)

等温過程では温度 $T$ が定数なので，式 (ii) から得られる微分方程式

$$
\left(\frac{\partial V}{\partial p}\right)_T = -\frac{1}{p}\left(V + \frac{b}{T}\right)
$$

を変数分離します。

$$
\frac{\mathrm{d}V}{V + \dfrac{b}{T}} = -\frac{\mathrm{d}p}{p}
$$

$T$ を固定して両辺を積分すると，$\ln\left(V + \dfrac{b}{T}\right) = -\ln p + \text{const.}$ となるため，温度 $T$ のみに依存する関数 $f(T)$ を用いて次式が得られます。

$$
\finalanswer{p\left(V + \frac{b}{T}\right) = f(T)}
$$

#### (ロ)

(イ) で得られた関係を $V$ について解くと

$$
V = \frac{f(T)}{p} - \frac{b}{T}
$$

となります。これを $p$ 一定のもとで $T$ で偏微分します。

$$
\left(\frac{\partial V}{\partial T}\right)_p = \frac{f'(T)}{p} + \frac{b}{T^2}
$$

一方で，式 (i) に (2) の結果 $a = 2b$ と上式の $V$ を代入すると次式が得られます。

$$
\begin{aligned}
\left(\frac{\partial V}{\partial T}\right)_p &= \frac{V}{T} + \frac{2b}{T^2} \\
&= \frac{f(T)}{pT} - \frac{b}{T^2} + \frac{2b}{T^2} \\
&= \frac{f(T)}{pT} + \frac{b}{T^2}
\end{aligned}
$$

これら2つの表式を比較すると，すべての $p, T$ に対して

$$
\frac{f'(T)}{p} = \frac{f(T)}{pT}
$$

すなわち $\dfrac{f'(T)}{f(T)} = \dfrac{1}{T}$ が成り立ちます。これを積分すると，積分定数 $k$ を用いて

$$
f(T) = k T
$$

となります。したがって気体の状態方程式は

$$
p\left(V + \frac{b}{T}\right) = k T
$$

となります。ここで問題文の前提より，この気体1モルは高温低密度の極限すなわち $T \to \infty$，$V \to \infty$ で理想気体の状態方程式 $pV = RT$ に近づきます。この極限では $\dfrac{b}{VT} \to 0$ なので $pV \to kT$ となり，定数は $k = R$ と定まります。

以上より，求める状態方程式は次の通りです。

$$
\finalanswer{p\left(V + \frac{b}{T}\right) = RT}
$$
