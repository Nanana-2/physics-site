---
title: 東大理物 平成27年度 物理学 第2問：高分子鎖のランダムウォークと揺動散逸関係
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成27年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成27年度 物理学 第2問：高分子鎖のランダムウォークと揺動散逸関係

## 問題

高分子鎖について図1のようなモデル化を考えよう。高分子鎖の始点は，二次元正方格子の原点 $(x, y) = (0, 0)$ に固定されている。また，高分子鎖を構成するモノマー（単量体）の間をつなぐ手の長さは $\sqrt{2}$ で，それぞれの手は右斜上45度あるいは左斜上45度のいずれかの方向にのみ伸びることができるものとする。

$y$ 軸方向の長さが $L$（モノマー数が $L + 1$）の高分子鎖を考えると，その取りうる配位の総数は $2^L$ である。そのうち，終点が $(x, L)$ である配位の数を $C(x, L)$ とすると，$C(x, L)$ と $C(x, L + 1)$ との間には，以下の漸化式が成り立つ。

$$
C(x, L + 1) = C(x - 1, L) + C(x + 1, L) \tag{1}
$$

<figure class="problem-figure" markdown>
![高分子鎖のモデル](../../assets/figures/pastexam-todai-ributsu/H27_butsuri_2-p-light.svg#only-light)
![高分子鎖のモデル](../../assets/figures/pastexam-todai-ributsu/H27_butsuri_2-p-dark.svg#only-dark)
<figcaption markdown="span">図1：高分子鎖のモデル</figcaption>
</figure>

(1) $C(x, L)$ が以下で与えられることを示せ。

$$
C(x, L) = \begin{cases} \dfrac{L!}{\bigl((L - x)/2\bigr)!\,\bigl((L + x)/2\bigr)!} & \text{（$(L + x)$ が偶数，かつ $|x| \le L$ のとき）} \\ 0 & \text{（それ以外のとき）} \end{cases} \tag{2}
$$

(2) $x$ に関する $C(x, L)$ のフーリエ変換 $\tilde{C}(k, L)$

$$
\tilde{C}(k, L) = \sum_{x = -\infty}^{\infty} e^{-ikx} C(x, L),\qquad C(x, L) = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^{ikx} \tilde{C}(k, L)\,dk \tag{3}
$$

を導入する。式 (1) から $\tilde{C}(k, L)$ に関する漸化式を導け。

(3) $L = 0$ における初期条件と上で求めた漸化式から，$\tilde{C}(k, L)$ の表式を導け。

(4) $k^2 L$ を一定に保ったままで，$L$ を十分に大きくすることを考える。$\log\tilde{C}(k, L)$ を $k$ に関して2次まで展開し，$C(x, L)$ の漸近形を求めよ。必要であれば，ガウス積分の公式 $\displaystyle\int_{-\infty}^{\infty} e^{-ax^2}\,dx = \sqrt{\pi/a}$（ただし，$a$ は正の実数）を用いてよい。

終点のモノマーに電荷 $q$ を与える。それ以外のモノマーは電気的に中性とする。$x$ 軸の正の向きに大きさ $E$ の静電場を印加した状況を考える。$y$ 軸方向の長さが $L$ の系が，温度 $T$ の熱浴に接し，熱平衡状態にあるとき，以下の設問に答えよ。ただし，ボルツマン定数を $k_{\mathrm{B}}$ とする。また，$L$ は設問4の近似が使えるほどは大きくないとする。
{: .problem-lead }

(5) この系の分配関数を求めよ。

(6) 終点のモノマーの $x$ 軸方向の位置の期待値 $\langle x \rangle$ を $T$ と $E$ の関数として求めよ。

(7) $E = 0$ における $x$ の分散 $\langle x^2 \rangle_{E=0}$ と，$x$ の期待値の $E$ に関する微係数 $\left.\dfrac{\partial\langle x \rangle}{\partial E}\right|_{E=0}$ との間に比例関係が成り立つことを，$C(x, L)$ の詳細な形を用いずに示せ。また，その比例係数を求めよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成27年度修士課程入学試験 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
長さ $L$ の鎖の終点の分布 $C(x,L)$ は，長さ $L-1$ の鎖の隣り合う2点の分布の和で書くことができます。この漸化式は，$x$ についてフーリエ変換すると波数 $k$ ごとの掛け算になり，$\tilde C(k,L)$ を求めることができます。$L$ が大きいときは $k$ の小さいところが主になるので，$k$ について2次まで展開してガウス積分で逆変換します。

電場があると，終点の位置 $x$ に比例するエネルギーが加わります。そのため，分配関数を電場 $E$ で微分すると $x$ の平均が，もう1回微分すると $x$ の分散が出てきます。
</div>

### (1)
$x$ が $+1$ 変化する右斜上へのステップ数を $n_+$ とします。$x$ が $-1$ 変化する左斜上へのステップ数を $n_-$ とすると，

$$
n_+ + n_- = L,\qquad n_+ - n_- = x
$$

を満たす非負整数なので，連立して解くと

$$
n_+ = \frac{L + x}{2},\qquad n_- = \frac{L - x}{2}
$$

となります。$n_+,\ n_-$ がともに $0$ 以上 $L$ 以下の整数であるための必要十分条件は，$L + x$ が偶数かつ $|x| \le L$ であることです。それ以外の $(x, L)$ には到達できないため $C(x, L) = 0$ です。条件を満たすとき，$L$ ステップのうち右斜上となる $n_+$ ステップの選び方は二項係数 $\dbinom{L}{n_+}$ に等しいため，

$$
\begin{aligned}
C(x, L) &= \frac{L!}{n_-!\,n_+!} \\
&= \frac{L!}{\bigl((L - x)/2\bigr)!\,\bigl((L + x)/2\bigr)!}
\end{aligned}
$$

となり，式 (2) が成り立ちます。

### (2)
式 (1) を式 (3) のフーリエ変換の定義に代入し，和の添字をずらします。

$$
\begin{aligned}
\tilde{C}(k, L + 1)
&= \sum_{x = -\infty}^{\infty} e^{-ikx}\bigl[C(x - 1, L) + C(x + 1, L)\bigr] \\
&= \sum_{x' = -\infty}^{\infty} e^{-ik(x' + 1)} C(x', L) + \sum_{x'' = -\infty}^{\infty} e^{-ik(x'' - 1)} C(x'', L) \\
&= \left(e^{-ik} + e^{ik}\right)\tilde{C}(k, L) \\
&= 2\cos k\,\tilde{C}(k, L)
\end{aligned}
$$

したがって，

$$
\finalanswer{\tilde{C}(k, L + 1) = 2\cos k\,\tilde{C}(k, L)}
$$

### (3)
$L = 0$ では始点 $(0, 0)$ のみの1配位なので $C(x, 0) = \delta_{x, 0}$ です。よって初期条件は

$$
\tilde{C}(k, 0) = \sum_{x = -\infty}^{\infty} e^{-ikx}\delta_{x, 0} = 1
$$

です。問2の漸化式を $L$ 回繰り返し用います。したがって，

$$
\finalanswer{\tilde{C}(k, L) = \left(2\cos k\right)^L}
$$

### (4)
ここでは中心領域 $x=O(\sqrt{L})$ の漸近形を求めます。問3より $\ln\tilde{C}(k, L) = L\ln(2\cos k)$ です。$k$ が小さい領域で $\cos k = 1 - \dfrac{k^2}{2} + \mathcal{O}(k^4)$ と展開し，$\ln(1 + u) = u + \mathcal{O}(u^2)$ を用います。

$$
\begin{aligned}
\ln\tilde{C}(k, L)
&= L\ln 2 + L\ln\left(1 - \frac{k^2}{2} + \mathcal{O}(k^4)\right) \\
&= L\ln 2 - \frac{L}{2}k^2 + \mathcal{O}(L k^4)
\end{aligned}
$$

$k^2 L$ を一定に保って $L \to \infty$ とすると $L k^4 = (k^2 L)^2 / L \to 0$ となるため，$\tilde{C}(k, L) \simeq 2^L e^{-Lk^2/2}$ です。

$|\cos k|$ は $k=0,\pm\pi$ で最大値 $1$ をとります。そのため，逆フーリエ積分では $k=0$ 付近に加えて，区間の両端付近からの寄与も調べます。

まず，$k \approx 0$ からの寄与を求めます。積分範囲を $(-\infty, \infty)$ に広げ，ガウス積分の公式を用います。

$$
\begin{aligned}
\frac{2^L}{2\pi}\int_{-\infty}^{\infty}e^{ikx-Lk^2/2}\,\mathrm{d}k
&= \frac{2^L}{2\pi}\sqrt{\frac{2\pi}{L}}\exp\left(-\frac{x^2}{2L}\right) \\
&= \frac{2^L}{\sqrt{2\pi L}}\exp\left(-\frac{x^2}{2L}\right)
\end{aligned}
$$

次に，$k \approx \pm\pi$ からの寄与を求めます。$k = \pi + q$ とおくと，$\cos(\pi + q) = -\cos q$ と $e^{i(\pi + q)x} = (-1)^x e^{iqx}$ が成り立ちます。

$$
\begin{aligned}
\tilde{C}(\pi + q, L) &\simeq (-1)^L 2^L e^{-Lq^2/2} \\
\tilde{C}(\pi + q, L)\,e^{i(\pi + q)x} &\simeq (-1)^{L + x} 2^L e^{-Lq^2/2} e^{iqx}
\end{aligned}
$$

そのため，$k \approx 0$ と同じ積分から，寄与は $(-1)^{L + x}\dfrac{2^L}{\sqrt{2\pi L}}\exp\left(-\dfrac{x^2}{2L}\right)$ になります。

両者を合わせると，$L+x$ が奇数のときは $0$，偶数のときは2倍になります。$x$ は2刻みで値をとるため，連続密度に格子間隔 $2$ を掛けた値に一致します。したがって，$L+x$ が偶数のとき

$$
\finalanswer{C(x, L) \simeq 2^L\sqrt{\frac{2}{\pi L}}\exp\left(-\frac{x^2}{2L}\right)}
$$

$L+x$ が奇数のときは $C(x,L)=0$ です。

### (5)
終点 $(x, L)$ に電荷 $q$ があるとき，静電場 $E$ によるポテンシャルエネルギーは $U(x) = -qEx$ です。逆温度を $\beta = \dfrac{1}{k_{\mathrm{B}}T}$ とすると，分配関数 $Z(T, E)$ は

$$
Z(T, E) = \sum_{x = -\infty}^{\infty} C(x, L)\,e^{\beta q E x}
$$

となります。式 (3) の $\tilde{C}(k, L)$ で $k = i\beta q E$ とおいたものに等しいため，問3の結果 $\tilde{C}(k, L) = (2\cos k)^L$ と $\cos(i\theta) = \cosh\theta$ を用います。

$$
Z(T, E) = \tilde{C}(i\beta q E, L) = \left[2\cosh\left(\frac{qE}{k_{\mathrm{B}}T}\right)\right]^L
$$

したがって，

$$
\finalanswer{Z(T, E) = \left[2\cosh\left(\frac{qE}{k_{\mathrm{B}}T}\right)\right]^L}
$$

### (6)
終点の $x$ 座標の期待値 $\langle x \rangle$ は，分配関数 $Z(T, E)$ の対数微分で与えられます。

$$
\begin{aligned}
\langle x \rangle
&= \frac{1}{Z(T, E)}\sum_{x = -\infty}^{\infty} x C(x, L) e^{\beta q E x} \\
&= \frac{1}{\beta q}\frac{\partial\ln Z(T, E)}{\partial E} \\
&= \frac{k_{\mathrm{B}}T}{q}\frac{\partial}{\partial E}\left[L\ln\left(2\cosh\frac{qE}{k_{\mathrm{B}}T}\right)\right] \\
&= L\tanh\left(\frac{qE}{k_{\mathrm{B}}T}\right)
\end{aligned}
$$

したがって，

$$
\finalanswer{\langle x \rangle = L\tanh\left(\frac{qE}{k_{\mathrm{B}}T}\right)}
$$

### (7)
$C(x, L)$ の具体的な形を使わず，$Z(T, E) = \displaystyle\sum_{x} C(x, L) e^{\beta q E x}$ と空間反転対称性 $C(-x, L) = C(x, L)$ のみを用います。

$\langle x \rangle = \dfrac{1}{Z}\displaystyle\sum_{x} x C(x, L) e^{\beta q E x}$ の両辺を $E$ で偏微分します。

$$
\begin{aligned}
\frac{\partial\langle x \rangle}{\partial E}
&= \frac{1}{Z}\sum_{x} (\beta q) x^2 C(x, L) e^{\beta q E x}
 - \frac{1}{Z^2}\left(\sum_{x} x C(x, L) e^{\beta q E x}\right)\left(\sum_{x} (\beta q) x C(x, L) e^{\beta q E x}\right) \\
&= \beta q\left(\langle x^2 \rangle - \langle x \rangle^2\right)
\end{aligned}
$$

ここで $E = 0$ のときは $C(-x, L) = C(x, L)$ より $\langle x \rangle_{E=0} = 0$ なので，

$$
\left.\frac{\partial\langle x \rangle}{\partial E}\right|_{E=0} = \frac{q}{k_{\mathrm{B}}T}\langle x^2 \rangle_{E=0}
$$

となり，比例関係が成り立ちます。したがって，$\left.\dfrac{\partial\langle x \rangle}{\partial E}\right|_{E=0} = \alpha\langle x^2 \rangle_{E=0}$ と書いたときの比例係数 $\alpha$ は

$$
\finalanswer{\alpha = \frac{q}{k_{\mathrm{B}}T}}
$$

です。$q\neq0$ なら，逆に $\langle x^2 \rangle_{E=0} = \dfrac{k_{\mathrm{B}}T}{q}\left.\dfrac{\partial\langle x \rangle}{\partial E}\right|_{E=0}$ と表すこともできます。

<aside class="rigor-note" markdown>
問7の結果は，電場がないときの揺らぎ $\langle x^2\rangle$ が，電場に対する応答 $\partial\langle x\rangle/\partial E$ に比例することを表しています。このような揺らぎと応答の関係を**揺動散逸定理**といいます。問6の結果から $\left.\dfrac{\partial\langle x\rangle}{\partial E}\right|_{E=0} = \dfrac{qL}{k_{\mathrm{B}}T}$ なので，$\langle x^2 \rangle_{E=0} = L$ となり，ランダムウォークの2乗平均変位がステップ数 $L$ に比例することとも一致します。
</aside>
