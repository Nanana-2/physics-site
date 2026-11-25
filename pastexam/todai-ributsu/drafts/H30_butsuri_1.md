---
title: 東大理物 平成30年度 物理学 第1問：二準位系の時間発展と断熱定理
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成30年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成30年度 物理学 第1問：二準位系の時間発展と断熱定理

## 問題

二つの状態 $|1\rangle$ と $|2\rangle$ からなる量子力学系を考える。この二つの状態は1に規格化されており（$\langle 1|1\rangle = \langle 2|2\rangle = 1$），かつ直交する（$\langle 1|2\rangle = 0$）ものとする。この系のハミルトニアンは

$$
H = \begin{pmatrix} \langle 1|H|1\rangle & \langle 1|H|2\rangle \\ \langle 2|H|1\rangle & \langle 2|H|2\rangle \end{pmatrix} = \begin{pmatrix} E_1 & V \\ V & E_2 \end{pmatrix} \tag{1}
$$

で与えられるとする。$E_1,\ E_2,\ V$ は実数とする。以下の設問に答えよ。

(1) 状態 $|2\rangle$ に対する演算子 $(H - E_2\mathbf{1})$ および演算子 $(H - E_2\mathbf{1})^2$ の期待値を求めよ。ただし $\mathbf{1}$ は $2\times 2$ の単位行列である。

(2) いま，$E_1,\ E_2,\ V$ は時間によらない一定値で，$0 < V$ とする。この系の二つのエネルギー固有値 $E_\pm\ (E_- < E_+)$ を求めよ。また，それらに対応する固有状態を $|\psi_+\rangle,\ |\psi_-\rangle$ とするとき，$|\psi_\pm\rangle = |1\rangle\langle 1|\psi_\pm\rangle + |2\rangle\langle 2|\psi_\pm\rangle$ の係数の比 $\langle 2|\psi_+\rangle / \langle 1|\psi_+\rangle$ および $\langle 2|\psi_-\rangle / \langle 1|\psi_-\rangle$ を $E_1,\ E_2,\ V$ を用いて表せ。

(3) この2つのエネルギー固有状態，$|\psi_+\rangle$ と $|\psi_-\rangle$，は直交することを示せ。

以上の設問ではハミルトニアン (1) の行列要素 $E_1,\ E_2,\ V$ は一定値をとると考えたが，以下では設定を少し変える。まず，$E_1$ が実数値のパラメータ $\lambda$ に $E_1 = E_2 - \mathcal{E}\lambda$ の形で依存し，$\mathcal{E},\ E_2,\ V$ は実定数とする。このとき，パラメータ $\lambda$ に依存するハミルトニアン
{: .problem-lead }

$$
H^{(\lambda)} = \begin{pmatrix} E_2 - \mathcal{E}\lambda & V \\ V & E_2 \end{pmatrix} \tag{2}
$$

を考えよう。以下の設問では，$0 < V \ll \mathcal{E}$ の関係が満たされているものとする。
{: .problem-lead }

(4) ハミルトニアン $H^{(\lambda)}$ の二つの固有値を $E_+(\lambda)$ と $E_-(\lambda)$（ただし $E_-(\lambda) < E_+(\lambda)$）とする。パラメータ $\lambda$ の値によらず $E_+(\lambda) - E_-(\lambda) \ge 2V$ の関係が満たされることを示せ。

設問4の固有値に対応した固有状態を $|\psi_+^{(\lambda)}\rangle,\ |\psi_-^{(\lambda)}\rangle$ とする。固有状態 $|\psi_+^{(\lambda)}\rangle$ は
{: .problem-lead }

$$
|\psi_+^{(\lambda)}\rangle = \cos\bigl(\theta(\lambda)\bigr)|1\rangle + \sin\bigl(\theta(\lambda)\bigr)|2\rangle \tag{3}
$$

と書くことができ，この $\theta(\lambda)$ を $\lambda$ の関数として図示すると図1のようになる。$|\lambda| \lesssim \mathcal{O}(V/\mathcal{E})$ の範囲内でのみ状態 $|\psi_+^{(\lambda)}\rangle$ は $|1\rangle$ と $|2\rangle$ から大きく異なるが，それは $|\lambda| \lesssim \mathcal{O}(V/\mathcal{E})$ の場合に $H^{(\lambda)}$ の非対角項 $V$ が二つの対角項 $(E_2 - \mathcal{E}\lambda)$ と $E_2$ の差 $\mathcal{E}\lambda$ と同程度かそれ以上の大きさになるためである。
{: .problem-lead }

さて，以下の設問5と6では，パラメータ $\lambda$ が時刻 $t$ とともに $\lambda = t/T$ のように変化，すなわちハミルトニアンが $H(t) = H^{(\lambda = t/T)}$ の形で変化する系を考える（$T$ は定数）。この系の時間変化がゆっくりである（$T$ が大きい）場合に，状態 $|\psi(t)\rangle$ の時間発展を調べよう。$\{|1\rangle, |2\rangle\}$ を基底に用いて
{: .problem-lead }

$$
|\psi(t)\rangle = c_1(t)|1\rangle + c_2(t)|2\rangle = \bigl(|1\rangle, |2\rangle\bigr)\begin{pmatrix} c_1(t) \\ c_2(t) \end{pmatrix} \tag{4}
$$

で表される状態 $|\psi(t)\rangle$ の時間発展は，次のシュレディンガー方程式によって与えられる。
{: .problem-lead }

$$
i\hbar\frac{\partial}{\partial t}\begin{pmatrix} c_1(t) \\ c_2(t) \end{pmatrix} = \begin{pmatrix} E_2 - \mathcal{E}\dfrac{t}{T} & V \\ V & E_2 \end{pmatrix}\begin{pmatrix} c_1(t) \\ c_2(t) \end{pmatrix} \tag{5}
$$

ここで，$\hbar$ はプランク定数を $2\pi$ で割ったものである。$\lambda$ の値を $\lambda = t/T$ とした二つの状態 $\{|\psi_+^{(t/T)}\rangle, |\psi_-^{(t/T)}\rangle\}$ を基底として用い，状態 $|\psi(t)\rangle$ を表すことを考える。
{: .problem-lead }

$$
|\psi(t)\rangle = c_+(t)|\psi_+^{(t/T)}\rangle + c_-(t)|\psi_-^{(t/T)}\rangle = \bigl(|\psi_+^{(t/T)}\rangle, |\psi_-^{(t/T)}\rangle\bigr)\begin{pmatrix} c_+(t) \\ c_-(t) \end{pmatrix} \tag{6}
$$

(5) 以下の小問に答えよ。

(i) このとき $c_\pm(t)$ の時間発展を記述する方程式を $\theta(t/T)$ などを用いる形で書き表せ。

(ii) さらに，係数 $c_\pm(t)$ を複素位相分だけ変えた量

$$
\tilde{c}_\pm(t) = c_\pm(t)\,e^{\frac{i}{\hbar}\int_{-T}^{t} dt'\,E_\pm(t'/T)} \tag{7}
$$

を導入する。$c_\pm(t)$ の時間発展方程式を $\tilde{c}_\pm(t)$ の時間発展方程式に書き直せ。

(6) 時刻 $t = -T$，すなわち $\lambda = -1$ において $|\psi(t)\rangle = |\psi_+^{(\lambda = -1)}\rangle$ であるとする。条件 $TV^2/\mathcal{E} \gg \hbar$ が満たされる（系の時間変化が十分にゆっくり）ならば，時刻 $t = +T$ に至っても $|\tilde{c}_+(t)| \simeq 1,\ |\tilde{c}_-(t)| \ll 1$ のままである。その理由を，$\tilde{c}_-(t)$ を定性的に評価して説明せよ。ただし，$\mathcal{O}(1)$ の区間 $I$ の上で実関数 $g(x)$ が緩やかに $\mathcal{O}(1)$ 程度変化し，実関数 $\chi(x)$ によって $e^{i\chi(x)}$ が $I$ 上で激しく振動する場合には，$\left|\int_I dx\,g(x) e^{i\chi(x)}\right| \ll 1$ となることを用いてよい。

<figure class="problem-figure" markdown>
![式(3)で導入したθ(λ)のλ依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H30_butsuri_1-p-light.svg#only-light)
![式(3)で導入したθ(λ)のλ依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H30_butsuri_1-p-dark.svg#only-dark)
<figcaption markdown="span">図1：式 (3) で導入した $\theta(\lambda)$ の $\lambda$ 依存性を $2V/\mathcal{E} = 0.1$ の場合に示す。$|\lambda| \gg (V/\mathcal{E})$ では $\lambda < 0$ なら $\theta \simeq 0$，$\lambda > 0$ なら $\theta \simeq +\pi/2$ であるが，図中矢印（$\leftrightarrow$）で示した $|\lambda| \lesssim \mathcal{O}(V/\mathcal{E})$ の範囲では $\theta$ の値が $0$ と $+\pi/2$ の間の中間的な値をとる。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成30年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
各時刻の固有状態を基底にすると，エネルギーによる位相の変化と，基底自体の変化を分けることができます。固有状態の時間微分も含めて方程式を変換し，異なる状態の係数を結ぶ項を調べます。

時間の位相を係数から分けると，遷移振幅を振動する関数の積分として扱うことができます。基底が変わる時間幅と，エネルギー差による位相の変化を比較して，遷移の大きさを評価します。
</div>

### (1)
行列 $(H - E_2\mathbf{1})$ とその2乗を計算します。

$$
H - E_2\mathbf{1} = \begin{pmatrix} E_1 - E_2 & V \\ V & 0 \end{pmatrix},\qquad
(H - E_2\mathbf{1})^2 = \begin{pmatrix} (E_1 - E_2)^2 + V^2 & (E_1 - E_2)V \\ (E_1 - E_2)V & V^2 \end{pmatrix}
$$

状態 $|2\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ に対する期待値はそれぞれの $(2, 2)$ 成分です。したがって，

$$
\finalanswer{\langle 2|(H - E_2\mathbf{1})|2\rangle = 0,\qquad \langle 2|(H - E_2\mathbf{1})^2|2\rangle = V^2}
$$

### (2)
固有方程式 $\det(H - E\mathbf{1}) = 0$ を解きます。

$$
\begin{aligned}
(E_1 - E)(E_2 - E) - V^2 &= 0 \\
E^2 - (E_1 + E_2)E + E_1 E_2 - V^2 &= 0 \\
E_\pm &= \frac{E_1 + E_2}{2} \pm \sqrt{\left(\frac{E_1 - E_2}{2}\right)^2 + V^2}
\end{aligned}
$$

$V > 0$ より $E_- < E_+$ です。固有方程式 $(H - E_\pm\mathbf{1})|\psi_\pm\rangle = 0$ の第1行より $(E_1 - E_\pm)\langle 1|\psi_\pm\rangle + V\langle 2|\psi_\pm\rangle = 0$ となるため，係数の比は次のようになります。

$$
\begin{aligned}
\frac{\langle 2|\psi_\pm\rangle}{\langle 1|\psi_\pm\rangle}
&= \frac{E_\pm - E_1}{V} \\
&= \frac{E_2 - E_1}{2V} \pm \sqrt{\left(\frac{E_2 - E_1}{2V}\right)^2 + 1}
\end{aligned}
$$

したがって，

$$
\finalanswer{E_\pm = \frac{E_1 + E_2}{2} \pm \sqrt{\left(\frac{E_1 - E_2}{2}\right)^2 + V^2},\qquad \frac{\langle 2|\psi_\pm\rangle}{\langle 1|\psi_\pm\rangle} = \frac{E_2 - E_1}{2V} \pm \sqrt{\left(\frac{E_2 - E_1}{2V}\right)^2 + 1}}
$$

### (3)
問2で求めた係数の比 $r_\pm = \dfrac{\langle 2|\psi_\pm\rangle}{\langle 1|\psi_\pm\rangle}$ はともに実数であり，その積を計算すると

$$
\begin{aligned}
r_+ r_- &= \left(\frac{E_2 - E_1}{2V}\right)^2 - \left[\left(\frac{E_2 - E_1}{2V}\right)^2 + 1\right] \\
&= -1
\end{aligned}
$$

となります。よって内積 $\langle\psi_+|\psi_-\rangle$ は

$$
\begin{aligned}
\langle\psi_+|\psi_-\rangle &= \langle\psi_+|1\rangle\langle 1|\psi_-\rangle + \langle\psi_+|2\rangle\langle 2|\psi_-\rangle \\
&= \langle\psi_+|1\rangle\langle 1|\psi_-\rangle\left(1 + r_+ r_-\right) \\
&= \langle\psi_+|1\rangle\langle 1|\psi_-\rangle(1 - 1) \\
&= 0
\end{aligned}
$$

となり，$|\psi_+\rangle$ と $|\psi_-\rangle$ は直交します。

### (4)
問2の固有値の式に $E_1 = E_2 - \mathcal{E}\lambda$ を代入すると，$E_1 - E_2 = -\mathcal{E}\lambda$ より，

$$
E_\pm(\lambda) = E_2 - \frac{\mathcal{E}\lambda}{2} \pm \sqrt{\left(\frac{\mathcal{E}\lambda}{2}\right)^2 + V^2}
$$

となります。したがって2つの固有値の差は

$$
\begin{aligned}
E_+(\lambda) - E_-(\lambda) &= \sqrt{(\mathcal{E}\lambda)^2 + 4V^2} \ge \sqrt{4V^2} \\
&= 2V
\end{aligned}
$$

となり，任意の実数 $\lambda$ に対して $E_+(\lambda) - E_-(\lambda) \ge 2V$ が成り立ちます。等号は $\lambda=0$ のときに成立します。

### (5)
(i) $|\psi_+^{(\lambda)}\rangle = \cos\theta(\lambda)|1\rangle + \sin\theta(\lambda)|2\rangle$ と直交する規格化された固有状態 $|\psi_-^{(\lambda)}\rangle$ は，位相を選んで

$$
|\psi_-^{(\lambda)}\rangle = -\sin\theta(\lambda)|1\rangle + \cos\theta(\lambda)|2\rangle
$$

ととることができます。時刻 $t$ に対する時間微分を 

$$
\begin{aligned}
\dot{\theta}(t) &= \dfrac{\mathrm{d}}{\mathrm{d}t}\theta(t/T) \\
&= \dfrac{1}{T}\theta'(t/T)
\end{aligned}
$$

 とおくと，基底ベクトルの時間微分は次のようになります。

$$
\frac{\partial}{\partial t}|\psi_+^{(t/T)}\rangle = \dot{\theta}(t)\,|\psi_-^{(t/T)}\rangle,\qquad
\frac{\partial}{\partial t}|\psi_-^{(t/T)}\rangle = -\dot{\theta}(t)\,|\psi_+^{(t/T)}\rangle
$$

式 (6) をシュレディンガー方程式 $i\hbar\dfrac{\partial}{\partial t}|\psi(t)\rangle = H(t)|\psi(t)\rangle$ に代入します。

$$
i\hbar\left[\left(\dot{c}_+ - \dot{\theta}\,c_-\right)|\psi_+^{(t/T)}\rangle + \left(\dot{c}_- + \dot{\theta}\,c_+\right)|\psi_-^{(t/T)}\rangle\right]
= E_+(t/T) c_+|\psi_+^{(t/T)}\rangle + E_-(t/T) c_-|\psi_-^{(t/T)}\rangle
$$

正規直交基底 $|\psi_+^{(t/T)}\rangle,\ |\psi_-^{(t/T)}\rangle$ の係数を比較して次式を得ます。したがって，

$$
\finalanswer{i\hbar\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix} c_+(t) \\ c_-(t) \end{pmatrix} = \begin{pmatrix} E_+(t/T) & i\hbar\,\dot{\theta}(t) \\ -i\hbar\,\dot{\theta}(t) & E_-(t/T) \end{pmatrix}\begin{pmatrix} c_+(t) \\ c_-(t) \end{pmatrix}}
$$



(ii) 式 (7) より $c_\pm(t) = \tilde{c}_\pm(t)\exp\left(-\dfrac{i}{\hbar}\displaystyle\int_{-T}^{t} E_\pm(t'/T)\,\mathrm{d}t'\right)$ なので，時間微分は

$$
i\hbar\dot{c}_\pm(t) = \left(i\hbar\dot{\tilde{c}}_\pm(t) + E_\pm(t/T)\tilde{c}_\pm(t)\right)\exp\left(-\frac{i}{\hbar}\int_{-T}^{t} E_\pm(t'/T)\,\mathrm{d}t'\right)
$$

となります。これを (i) の方程式に代入すると対角項 $E_\pm \tilde{c}_\pm$ が打ち消し合い，$\Delta E(\lambda) = E_+(\lambda) - E_-(\lambda)$ とおいて次式が得られます。したがって，

$$
\finalanswer{\frac{\mathrm{d}\tilde{c}_+(t)}{\mathrm{d}t} = \dot{\theta}(t)\,e^{\frac{i}{\hbar}\int_{-T}^{t}\Delta E(t'/T)\,\mathrm{d}t'}\,\tilde{c}_-(t),\qquad \frac{\mathrm{d}\tilde{c}_-(t)}{\mathrm{d}t} = -\dot{\theta}(t)\,e^{-\frac{i}{\hbar}\int_{-T}^{t}\Delta E(t'/T)\,\mathrm{d}t'}\,\tilde{c}_+(t)}
$$

### (6)
初期条件は $\tilde c_+(-T)=1$，$\tilde c_-(-T)=0$ です。$\tilde c_+(t)\simeq1$ とする1次近似で，問5(ii)の第2式を積分します。最後にこの近似と整合することを確認します。

$$
\begin{aligned}
\tilde{c}_-(T)
&\simeq -\int_{-T}^{T} \dot{\theta}(t)\exp\left(-\frac{i}{\hbar}\int_{-T}^{t}\Delta E(t'/T)\,\mathrm{d}t'\right)\mathrm{d}t \\
&= -\int_{-1}^{1} \frac{\mathrm{d}\theta(\lambda)}{\mathrm{d}\lambda}\,e^{-i\chi(\lambda)}\,\mathrm{d}\lambda
\end{aligned}
$$

ここで実関数 $\chi(\lambda)$ は $\chi(\lambda) = \dfrac{T}{\hbar}\displaystyle\int_{-1}^{\lambda}\Delta E(\lambda')\,\mathrm{d}\lambda'$ です。

$\theta(\lambda)$ は主に $|\lambda|\lesssim V/\mathcal E$ の領域で変わり，外側では微分が小さくなります。$x=\mathcal E\lambda/V$ とおくと，この変化は幅が $\mathcal O(1)$ の区間で起こります。

$$
\tilde{c}_-(T) \simeq -\int_I \frac{\mathrm{d}\theta}{\mathrm{d}x}\,e^{-i\chi(x)}\,\mathrm{d}x
$$

区間 $I$ の上で $g(x) = \dfrac{\mathrm{d}\theta}{\mathrm{d}x}$ は緩やかに $\mathcal{O}(1)$ 程度変化する実関数です。一方，位相 $\chi(x)$ の変化率を問4の不等式 $\Delta E(\lambda) \ge 2V$ を用いて評価すると，

$$
\begin{aligned}
\frac{\mathrm{d}\chi}{\mathrm{d}x} &= \frac{V}{\mathcal{E}}\frac{\mathrm{d}\chi}{\mathrm{d}\lambda} \\
&= \frac{TV}{\hbar\mathcal{E}}\Delta E(\lambda) \ge \frac{2TV^2}{\hbar\mathcal{E}} \gg 1
\end{aligned}
$$

となります。したがって区間 $I$ 上で $e^{-i\chi(x)}$ は激しく振動するため，問題文の事実より $|\tilde{c}_-(T)| \ll 1$ となります。また規格化条件 $|\tilde c_+(t)|^2+|\tilde c_-(t)|^2=1$ より，

$$
\begin{aligned}
|\tilde{c}_+(T)| &= \sqrt{1 - |\tilde{c}_-(T)|^2} \\
&\simeq 1
\end{aligned}
$$

 が保たれます。


