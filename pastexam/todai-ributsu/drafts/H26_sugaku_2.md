---
title: 東大理物 平成26年度 数学 第2問：巡回行列の対角化と結合2バンド行列の固有値
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成26年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成26年度 数学 第2問：巡回行列の対角化と結合2バンド行列の固有値

## 問題

(1) 次の $n$（$\ge 3$）次元正方行列 $A(\epsilon, t)$ について，設問 (i) から (v) に答えよ。

$$
A(\epsilon, t) \equiv \begin{pmatrix}
\epsilon & t & & & & t \\
t & \epsilon & t & & & \\
 & t & \epsilon & \ddots & & \\
 & & \ddots & \ddots & t & \\
 & & & t & \epsilon & t \\
t & & & & t & \epsilon
\end{pmatrix},
$$

すなわち，$A_{i,i} = \epsilon$（$i = 1, 2, \dots, n$），$A_{i,i+1} = A_{i+1,i} = t$（$i = 1, 2, \dots, n - 1$），$A_{n,1} = A_{1,n} = t$，であり，これら以外の成分はすべて $0$ であるものとする。また，$\epsilon, t$ は実数，特に $t > 0$ であるとする。

(i) 任意の $n$ 個の実数 $x_1, x_2, \dots, x_n$ を成分に持つ $n$ 次元縦ベクトルに対して，

$$
P\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_{n-1} \\ x_n \end{pmatrix} = \begin{pmatrix} x_2 \\ x_3 \\ x_4 \\ \vdots \\ x_n \\ x_1 \end{pmatrix}
$$

となるような行列 $P$ を具体的に成分で表せ。

(ii) $PA - AP$ を求めよ。

(iii) $P$ の互いに線形独立な $n$ 個の固有縦ベクトル，$\boldsymbol{u}_1, \boldsymbol{u}_2, \dots, \boldsymbol{u}_n$，及び，それぞれの固有値を求めよ。

(iv) $P$ の 2 つの互いに異なる固有値に対応する固有縦ベクトルを $\boldsymbol{x}, \boldsymbol{y}$ とする。このとき，$\boldsymbol{x}^{\dagger} A \boldsymbol{y} = 0$ であることを示せ。ここで，$\boldsymbol{x}^{\dagger} \equiv {}^t \boldsymbol{x}^*$ は $\boldsymbol{x}$ のエルミート共役である。

(v) $D \equiv U^{\dagger} A U$ が対角行列であるようなユニタリ行列 $U$ と，そのときの $D$ とを求めよ。

(2) 次の $2n$ 次元正方行列 $B$ について，設問 (i)，(ii) に答えよ。

$$
B \equiv \begin{pmatrix} A(0, t) & \lambda I \\ \lambda I & A(0, 2t) \end{pmatrix}
$$

ただし，$A(\epsilon, t)$ は前問で定義された行列，$I$ は $n$ 次元単位行列，$\lambda$ は正の実数である。

(i) $B$ の $2n$ 個の固有値をすべて求めよ。

(ii) (i) で求めた固有値を $\lambda = 0$ の場合と比較せよ。とくに，$\lambda$ が小さく $0 < \lambda \ll t$ である場合，$\lambda$ がゼロでないことによって生じる固有値の微小な変化が $\lambda$ の何乗に比例するかを答えよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成26年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
巡回シフトと可換な行列では，シフトの固有ベクトルを使って行列の成分を整理することができます。周期性に合った基底を選ぶことで，大きな行列の対角化を各波数ごとの計算として扱うことができます。

2つの行列を結ぶ部分が単位行列に比例するため，結合を加えても異なる波数は混ざりません。各波数の2成分だけを調べることで，全固有値と弱い結合による変化を求めることができます。
</div>

### (1)(i)
任意の縦ベクトル $\boldsymbol{x} = {}^t(x_1, \dots, x_n)$ に対して $(P\boldsymbol{x})_i = x_{i+1}$（$i = 1, \dots, n - 1$），$(P\boldsymbol{x})_n = x_1$ となる行列 $P$ の成分は，$P_{i, i+1} = 1$（$i = 1, 2, \dots, n - 1$），$P_{n, 1} = 1$，およびそれ以外の成分はすべて $0$ です。行列の形で書き表すと次のとおりです。

$$
\finalanswer{P = \begin{pmatrix}
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & \cdots & 0 & 1 \\
1 & 0 & \cdots & 0 & 0
\end{pmatrix}}
$$

### (1)(ii)
$P$ は実の直交行列であり，逆行列 $P^{-1} = {}^t P$ は $(P^{-1})_{i+1, i} = 1$（$i = 1, \dots, n - 1$），$(P^{-1})_{1, n} = 1$，その他は $0$ です。よって行列 $A(\epsilon, t)$ は

$$
A(\epsilon, t) = \epsilon I + t\left(P + P^{-1}\right)
$$

と表されます。$P$ は単位行列 $I$，$P$，および $P^{-1}$ のいずれとも可換なので，

$$
\begin{aligned}
PA - AP &= P\left[\epsilon I + t\left(P + P^{-1}\right)\right] - \left[\epsilon I + t\left(P + P^{-1}\right)\right] P \\
&= O
\end{aligned}
$$

となります。

$$
\finalanswer{PA - AP = O}
$$

### (1)(iii)
固有値方程式 $P\boldsymbol{u} = \omega \boldsymbol{u}$ を成分で書きます。

$$
u_2 = \omega u_1, \quad u_3 = \omega u_2, \quad \dots, \quad u_n = \omega u_{n-1}, \quad u_1 = \omega u_n
$$

これらを順次代入すると $u_j = \omega^{j-1} u_1$（$j = 1, \dots, n$）および $u_1 = \omega^n u_1$ が得られます。$\boldsymbol{u} \neq \boldsymbol{0}$ より $u_1 \neq 0$ なので，$\omega^n = 1$ が成り立ちます。したがって $P$ の $n$ 個の固有値は

$$
\omega_k = \exp\!\left(i\frac{2\pi k}{n}\right) \qquad (k = 1, 2, \dots, n)
$$

です。これらは互いにすべて異なるため，ノルムを $1$ に規格化した対応する固有ベクトル

$$
\boldsymbol{u}_k = \frac{1}{\sqrt{n}}\begin{pmatrix} 1 \\ \omega_k \\ \omega_k^2 \\ \vdots \\ \omega_k^{n-1} \end{pmatrix} \qquad (k = 1, 2, \dots, n)
$$

は互いに線形独立であり，正規直交系をなします。

$$
\finalanswer{\omega_k = e^{i\frac{2\pi k}{n}}, \qquad \boldsymbol{u}_k = \frac{1}{\sqrt{n}}\begin{pmatrix} 1 \\ \omega_k \\ \omega_k^2 \\ \vdots \\ \omega_k^{n-1} \end{pmatrix} \quad (k = 1, 2, \dots, n)}
$$

### (1)(iv)
$P\boldsymbol{x} = \mu \boldsymbol{x}$，$P\boldsymbol{y} = \nu \boldsymbol{y}$（$\mu \neq \nu$）とします。$P$ はユニタリ行列（$P^{\dagger} = P^{-1}$）なので，固有値 $\mu$ は $|\mu| = 1$ を満たし，$P^{\dagger}\boldsymbol{x} = P^{-1}\boldsymbol{x} = \mu^{-1}\boldsymbol{x} = \mu^* \boldsymbol{x}$ が成り立ちます。両辺のエルミート共役をとると $\boldsymbol{x}^{\dagger} P = \mu \boldsymbol{x}^{\dagger}$ です。

(ii) で示した $PA - AP = O$ の左から $\boldsymbol{x}^{\dagger}$，右から $\boldsymbol{y}$ を掛けると，

$$
\begin{aligned}
0 &= \boldsymbol{x}^{\dagger}(PA - AP)\boldsymbol{y} \\
&= (\boldsymbol{x}^{\dagger} P) A \boldsymbol{y} - \boldsymbol{x}^{\dagger} A (P\boldsymbol{y}) \\
&= (\mu - \nu)\boldsymbol{x}^{\dagger} A \boldsymbol{y}
\end{aligned}
$$

となります。仮定より $\mu \neq \nu$ なので，$\boldsymbol{x}^{\dagger} A \boldsymbol{y} = 0$ が成り立ちます。

### (1)(v)
(iii) で求めた正規直交固有ベクトルを列に並べた $n$ 次元正方行列

$$
U = \left(\boldsymbol{u}_1,\; \boldsymbol{u}_2,\; \dots,\; \boldsymbol{u}_n\right), \qquad U_{j,k} = \frac{1}{\sqrt{n}}\omega_k^{j-1} = \frac{1}{\sqrt{n}}\exp\!\left(i\frac{2\pi (j - 1) k}{n}\right)
$$

を定義します。$\boldsymbol{u}_k^{\dagger}\boldsymbol{u}_l = \dfrac{1}{n}\displaystyle\sum_{j=1}^n \left(\omega_k^* \omega_l\right)^{j-1} = \delta_{kl}$ なので，$U^{\dagger} U = I$ すなわち $U$ はユニタリ行列です。

(iv) の結果より，$k \neq l$ のとき $(U^{\dagger} A U)_{k, l} = \boldsymbol{u}_k^{\dagger} A \boldsymbol{u}_l = 0$ です。また，対角成分については $A = \epsilon I + t(P + P^{-1})$ より

$$
\begin{aligned}
A\boldsymbol{u}_k &= \left[\epsilon + t\left(\omega_k + \omega_k^{-1}\right)\right]\boldsymbol{u}_k \\
&= \left(\epsilon + 2t\cos\frac{2\pi k}{n}\right)\boldsymbol{u}_k
\end{aligned}
$$

なので，$(U^{\dagger} A U)_{k,k} = \boldsymbol{u}_k^{\dagger} A \boldsymbol{u}_k = \epsilon + 2t\cos\dfrac{2\pi k}{n}$ となります。したがって，

$$
\finalanswer{U_{j,k} = \frac{1}{\sqrt{n}}e^{i\frac{2\pi (j - 1) k}{n}}, \qquad D = \operatorname{diag}\!\left(d_1, d_2, \dots, d_n\right), \quad d_k = \epsilon + 2t\cos\frac{2\pi k}{n} \quad (j, k = 1, \dots, n)}
$$

### (2)(i)
(1)(v) で構成したユニタリ行列 $U$ は $\epsilon$ や $t$ に依存しないため，$A(0, t)$ と $A(0, 2t)$ を同時に対角化します。$2n$ 次元ユニタリ行列 $\widetilde{U} = \begin{pmatrix} U & O \\ O & U \end{pmatrix}$ を用いて $B$ をユニタリ変換します。

$$
\widetilde{U}^{\dagger} B \widetilde{U}
= \begin{pmatrix} U^{\dagger} A(0, t) U & \lambda U^{\dagger} I U \\ \lambda U^{\dagger} I U & U^{\dagger} A(0, 2t) U \end{pmatrix}
= \begin{pmatrix} D_1 & \lambda I \\ \lambda I & D_2 \end{pmatrix}
$$

ここで $D_1 = \operatorname{diag}(2t\cos\theta_1, \dots, 2t\cos\theta_n)$，$D_2 = \operatorname{diag}(4t\cos\theta_1, \dots, 4t\cos\theta_n)$，$\theta_k = \dfrac{2\pi k}{n}$（$k = 1, 2, \dots, n$）です。

行と列を適切に並べ替えると，$\widetilde{U}^{\dagger} B \widetilde{U}$ は $n$ 個の独立な $2 \times 2$ 対角ブロック

$$
B_k = \begin{pmatrix} 2t\cos\theta_k & \lambda \\ \lambda & 4t\cos\theta_k \end{pmatrix} \qquad (k = 1, 2, \dots, n)
$$

の直和となります。各 $B_k$ の固有方程式を解きます。

$$
\begin{aligned}
(\mu - 2t\cos\theta_k)(\mu - 4t\cos\theta_k) - \lambda^2 &= 0 \\
\mu^2 - 6t\cos\theta_k\,\mu + 8t^2\cos^2\theta_k - \lambda^2 &= 0
\end{aligned}
$$

これにより，$B$ の $2n$ 個の固有値が次のように求まります。

$$
\finalanswer{\mu_{k, \pm} = 3t\cos\frac{2\pi k}{n} \pm \sqrt{t^2\cos^2\frac{2\pi k}{n} + \lambda^2} \qquad (k = 1, 2, \dots, n)}
$$

### (2)(ii)
$\lambda = 0$ のとき，各 $k$ に対する 2 つの固有値は $\mu_{k, \pm}(0) = 3t\cos\theta_k \pm t|\cos\theta_k|$，すなわち $2t\cos\theta_k$ と $4t\cos\theta_k$ です。$\lambda > 0$ になると $\sqrt{t^2\cos^2\theta_k + \lambda^2} > t|\cos\theta_k|$ となるため，各 $k$ について大きい方の固有値 $\mu_{k,+}$ は増加し，小さい方の固有値 $\mu_{k,-}$ は同じ大きさだけ減少します。この変化を**準位反発**といいます。

$0<\lambda\ll t$ のときの変化量 $\Delta\mu_{k,\pm}\equiv\mu_{k,\pm}(\lambda)-\mu_{k,\pm}(0)$ を調べます。同じ波数 $k$ の2準位が一致するかどうか，すなわち $\cos\theta_k=0$ かどうかで，変化の最低次数が異なります。

まず，$\cos\theta_k\neq0$ の場合を考えます。$\lambda \ll t|\cos\theta_k|$ のもとで，平方根をテイラー展開します。

$$
\begin{aligned}
\mu_{k, \pm}(\lambda)
&= 3t\cos\theta_k \pm t|\cos\theta_k|\sqrt{1 + \frac{\lambda^2}{t^2\cos^2\theta_k}} \\
&\simeq 3t\cos\theta_k \pm t|\cos\theta_k| \pm \frac{\lambda^2}{2t|\cos\theta_k|}
\end{aligned}
$$

よって，変化量 $\Delta\mu_{k, \pm} \simeq \pm \dfrac{\lambda^2}{2t|\cos\theta_k|}$ は $\lambda^2$ に比例します。

次に，$\cos\theta_k = 0$ の場合を考えます。これは $n$ が4の倍数のときだけ起こり，$k = \dfrac{n}{4}$ と $k = \dfrac{3n}{4}$ が当てはまります。このとき $\lambda = 0$ の2つの固有値は，ともに $0$ に縮退しています。$\lambda>0$ では

$$
\mu_{k, \pm}(\lambda) = \pm \lambda
$$

となるため，変化量 $\Delta\mu_{k, \pm} = \pm \lambda$ は $\lambda$ に比例します。

$$
\finalanswer{\Delta\mu_{k, \pm} \propto \lambda^2 \quad \left(\cos\frac{2\pi k}{n} \neq 0\right), \qquad \Delta\mu_{k, \pm} \propto \lambda \quad \left(4 \mid n,\; \cos\frac{2\pi k}{n} = 0\right)}
$$

<aside class="rigor-note" markdown>
摂動項 $V=\begin{pmatrix}O&\lambda I\\\lambda I&O\end{pmatrix}$ は，同じ波数 $k$ の上下のバンドだけを結びます。$\cos\theta_k\neq0$ では同じ $k$ の2準位に差があるため，最低次の変化は $O(\lambda^2)$ です。異なる波数間に縮退があっても，摂動が異なる波数を結ばないので，この結論は変わりません。

$n$ が4の倍数なら $k=n/4,3n/4$ の2つの波数で上下の準位がともに $0$ です。各波数で $\pm\lambda$ へ分裂し，4重の $0$ 固有値が2重の $+\lambda$ と2重の $-\lambda$ に分かれます。縮退は一部残ります。
</aside>
