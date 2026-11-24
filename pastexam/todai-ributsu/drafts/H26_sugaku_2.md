---
title: 東大理物 平成26年度 数学第2問：巡回行列の対角化と結合2バンド行列の固有値
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成26年度
exam_subject: 専門科目（数学）
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成26年度 数学第2問：巡回行列の対角化と結合2バンド行列の固有値

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

> 出典：[東京大学大学院理学系研究科物理学専攻](https://www.phys.s.u-tokyo.ac.jp/) 平成26年度修士課程入学試験問題 数学 第2問（Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。）

---

## 解答・解説

※ 本解答・解説は非公式であり，大学当局とは無関係です。

### 考え方

巡回シフト行列 $P$ が $A(\epsilon, t)$ と可換であり，しかも $P$ の固有値がすべて縮退していないことを利用すると，$P$ の固有ベクトル系がそのまま $A(\epsilon, t)$ を対角化する離散フーリエ変換ユニタリ行列 $U$ を与える。これは周期境界条件を課した 1 次元強束縛模型のブロッホの定理そのものである。

後半のブロック行列 $B$ では，$U$ が $\epsilon, t$ に依存しないため上下ブロックを同時に対角化でき，問題が $n$ 個の $2 \times 2$ 行列に分解される。微弱な結合 $\lambda \ll t$ に対する固有値のシフトは，非縮退準位では 2 次摂動（$\propto \lambda^2$）となるが，$n$ が 4 の倍数のときに現れる $\cos(2\pi k / n) = 0$ の縮退点では 1 次摂動（$\propto \lambda$）に切り替わる点が要点である。

### 解答

#### (1)(i) シフト行列 $P$

任意の縦ベクトル $\boldsymbol{x} = {}^t(x_1, \dots, x_n)$ に対して $(P\boldsymbol{x})_i = x_{i+1}$（$i = 1, \dots, n - 1$），$(P\boldsymbol{x})_n = x_1$ となる行列 $P$ の成分は，$P_{i, i+1} = 1$（$i = 1, 2, \dots, n - 1$），$P_{n, 1} = 1$，およびそれ以外の成分はすべて $0$ である。行列の形で書き表すと，

$$
\finalanswer{P = \begin{pmatrix}
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & \cdots & 0 & 1 \\
1 & 0 & \cdots & 0 & 0
\end{pmatrix}}
$$

となる。

#### (1)(ii) 交換子 $PA - AP$

$P$ は直交行列（実ユニタリ行列）であり，その逆行列 $P^{-1} = {}^t P$ は $(P^{-1})_{i+1, i} = 1$（$i = 1, \dots, n - 1$），$(P^{-1})_{1, n} = 1$，その他は $0$ である。よって行列 $A(\epsilon, t)$ は

$$
A(\epsilon, t) = \epsilon I + t\left(P + P^{-1}\right)
$$

と表される。$P$ は単位行列 $I$，$P$，および $P^{-1}$ のいずれとも可換であるから，

$$
PA - AP = P\left[\epsilon I + t\left(P + P^{-1}\right)\right] - \left[\epsilon I + t\left(P + P^{-1}\right)\right] P = O
$$

となる。

$$
\finalanswer{PA - AP = O}
$$

#### (1)(iii) $P$ の固有値と固有ベクトル

固有値方程式 $P\boldsymbol{u} = \omega \boldsymbol{u}$ を成分で書くと，

$$
u_2 = \omega u_1, \quad u_3 = \omega u_2, \quad \dots, \quad u_n = \omega u_{n-1}, \quad u_1 = \omega u_n
$$

となる。これらを順次代入すると $u_j = \omega^{j-1} u_1$（$j = 1, \dots, n$）および $u_1 = \omega^n u_1$ を得る。$\boldsymbol{u} \neq \boldsymbol{0}$ より $u_1 \neq 0$ であるから，$\omega^n = 1$ が成り立つ。したがって $P$ の $n$ 個の固有値は

$$
\omega_k = \exp\!\left(i\frac{2\pi k}{n}\right) \qquad (k = 1, 2, \dots, n)
$$

である。これらは互いにすべて異なるため，対応する固有ベクトル（ノルムを $1$ に規格化したもの）

$$
\boldsymbol{u}_k = \frac{1}{\sqrt{n}}\begin{pmatrix} 1 \\ \omega_k \\ \omega_k^2 \\ \vdots \\ \omega_k^{n-1} \end{pmatrix} \qquad (k = 1, 2, \dots, n)
$$

は互いに線形独立である（さらに直交する）。

$$
\finalanswer{\omega_k = e^{i\frac{2\pi k}{n}}, \qquad \boldsymbol{u}_k = \frac{1}{\sqrt{n}}\begin{pmatrix} 1 \\ \omega_k \\ \omega_k^2 \\ \vdots \\ \omega_k^{n-1} \end{pmatrix} \quad (k = 1, 2, \dots, n)}
$$

#### (1)(iv) 異なる固有値に属する固有ベクトル間の行列要素

$P\boldsymbol{x} = \mu \boldsymbol{x}$，$P\boldsymbol{y} = \nu \boldsymbol{y}$（$\mu \neq \nu$）とする。$P$ はユニタリ行列（$P^{\dagger} = P^{-1}$）であるから，固有値 $\mu$ は $|\mu| = 1$ を満たし，$P^{\dagger}\boldsymbol{x} = P^{-1}\boldsymbol{x} = \mu^{-1}\boldsymbol{x} = \mu^* \boldsymbol{x}$ が成り立つ。両辺のエルミート共役をとると $\boldsymbol{x}^{\dagger} P = \mu \boldsymbol{x}^{\dagger}$ である。

(ii) で示した $PA - AP = O$ の左から $\boldsymbol{x}^{\dagger}$，右から $\boldsymbol{y}$ を掛けると，

$$
\begin{aligned}
0 &= \boldsymbol{x}^{\dagger}(PA - AP)\boldsymbol{y} \\
&= (\boldsymbol{x}^{\dagger} P) A \boldsymbol{y} - \boldsymbol{x}^{\dagger} A (P\boldsymbol{y}) \\
&= (\mu - \nu)\boldsymbol{x}^{\dagger} A \boldsymbol{y}
\end{aligned}
$$

となる。仮定より $\mu \neq \nu$ であるから，$\boldsymbol{x}^{\dagger} A \boldsymbol{y} = 0$ が成り立つ。

#### (1)(v) ユニタリ行列 $U$ と対角行列 $D$

(iii) で求めた正規直交固有ベクトルを列に並べた $n$ 次元正方行列

$$
U = \left(\boldsymbol{u}_1,\; \boldsymbol{u}_2,\; \dots,\; \boldsymbol{u}_n\right), \qquad U_{j,k} = \frac{1}{\sqrt{n}}\omega_k^{j-1} = \frac{1}{\sqrt{n}}\exp\!\left(i\frac{2\pi (j - 1) k}{n}\right)
$$

を定義する。$\boldsymbol{u}_k^{\dagger}\boldsymbol{u}_l = \dfrac{1}{n}\sum_{j=1}^n \left(\omega_k^* \omega_l\right)^{j-1} = \delta_{kl}$ であるから，$U^{\dagger} U = I$ すなわち $U$ はユニタリ行列である。

(iv) の結果より，$k \neq l$ のとき $(U^{\dagger} A U)_{k, l} = \boldsymbol{u}_k^{\dagger} A \boldsymbol{u}_l = 0$ である。また，対角成分については $A = \epsilon I + t(P + P^{-1})$ より

$$
A\boldsymbol{u}_k = \left[\epsilon + t\left(\omega_k + \omega_k^{-1}\right)\right]\boldsymbol{u}_k = \left(\epsilon + 2t\cos\frac{2\pi k}{n}\right)\boldsymbol{u}_k
$$

であるから，$(U^{\dagger} A U)_{k,k} = \boldsymbol{u}_k^{\dagger} A \boldsymbol{u}_k = \epsilon + 2t\cos\dfrac{2\pi k}{n}$ となる。したがって，

$$
\finalanswer{U_{j,k} = \frac{1}{\sqrt{n}}e^{i\frac{2\pi (j - 1) k}{n}}, \qquad D = \operatorname{diag}\!\left(d_1, d_2, \dots, d_n\right), \quad d_k = \epsilon + 2t\cos\frac{2\pi k}{n} \quad (j, k = 1, \dots, n)}
$$

である。

#### (2)(i) $2n$ 次元正方行列 $B$ の固有値

(1)(v) で構成したユニタリ行列 $U$ は $\epsilon$ や $t$ に依存しないため，$A(0, t)$ と $A(0, 2t)$ を同時に対角化する。$2n$ 次元ユニタリ行列 $\widetilde{U} = \begin{pmatrix} U & O \\ O & U \end{pmatrix}$ を用いて $B$ をユニタリ変換すると，

$$
\widetilde{U}^{\dagger} B \widetilde{U}
= \begin{pmatrix} U^{\dagger} A(0, t) U & \lambda U^{\dagger} I U \\ \lambda U^{\dagger} I U & U^{\dagger} A(0, 2t) U \end{pmatrix}
= \begin{pmatrix} D_1 & \lambda I \\ \lambda I & D_2 \end{pmatrix}
$$

となる。ここで $D_1 = \operatorname{diag}(2t\cos\theta_1, \dots, 2t\cos\theta_n)$，$D_2 = \operatorname{diag}(4t\cos\theta_1, \dots, 4t\cos\theta_n)$，$\theta_k = \dfrac{2\pi k}{n}$（$k = 1, 2, \dots, n$）である。

行と列を適切に並べ替えると，$\widetilde{U}^{\dagger} B \widetilde{U}$ は $n$ 個の独立な $2 \times 2$ 対角ブロック

$$
B_k = \begin{pmatrix} 2t\cos\theta_k & \lambda \\ \lambda & 4t\cos\theta_k \end{pmatrix} \qquad (k = 1, 2, \dots, n)
$$

の直和となる。各 $B_k$ の固有方程式は

$$
\begin{aligned}
(\mu - 2t\cos\theta_k)(\mu - 4t\cos\theta_k) - \lambda^2 &= 0 \\
\mu^2 - 6t\cos\theta_k\,\mu + 8t^2\cos^2\theta_k - \lambda^2 &= 0
\end{aligned}
$$

であり，これを解くと $B$ の $2n$ 個の固有値が次のように求まる。

$$
\finalanswer{\mu_{k, \pm} = 3t\cos\frac{2\pi k}{n} \pm \sqrt{t^2\cos^2\frac{2\pi k}{n} + \lambda^2} \qquad (k = 1, 2, \dots, n)}
$$

#### (2)(ii) $\lambda = 0$ の場合との比較と微小 $\lambda$ でのスケーリング

$\lambda = 0$ のとき，各 $k$ に対する 2 つの固有値は $\mu_{k, \pm}(0) = 3t\cos\theta_k \pm t|\cos\theta_k|$，すなわち $2t\cos\theta_k$ と $4t\cos\theta_k$ である。$\lambda > 0$ になると $\sqrt{t^2\cos^2\theta_k + \lambda^2} > t|\cos\theta_k|$ となるため，各 $k$ について大きい方の固有値 $\mu_{k,+}$ は増加し，小さい方の固有値 $\mu_{k,-}$ は同じ大きさだけ減少する（準位反発）。

$0 < \lambda \ll t$ のときの微小な変化 $\Delta\mu_{k, \pm} \equiv \mu_{k, \pm}(\lambda) - \mu_{k, \pm}(0)$ は，$\cos\theta_k$ が $0$ であるか否か（すなわち $\lambda = 0$ で縮退しているか否か）によって振る舞いが異なる。

- **$\cos\theta_k \neq 0$ のとき（非縮退）**：$\lambda \ll t|\cos\theta_k|$ のもとで平方根をテイラー展開すると，
  $$
  \begin{aligned}
  \mu_{k, \pm}(\lambda)
  &= 3t\cos\theta_k \pm t|\cos\theta_k|\sqrt{1 + \frac{\lambda^2}{t^2\cos^2\theta_k}} \\
  &\simeq 3t\cos\theta_k \pm t|\cos\theta_k| \pm \frac{\lambda^2}{2t|\cos\theta_k|}
  \end{aligned}
  $$
  となる。よって変化量 $\Delta\mu_{k, \pm} \simeq \pm \dfrac{\lambda^2}{2t|\cos\theta_k|}$ は $\lambda$ の **2 乗**に比例する。

- **$\cos\theta_k = 0$ のとき（縮退）**：$n$ が 4 の倍数のときに限り，$k = \dfrac{n}{4}, \dfrac{3n}{4}$（$\theta_k = \dfrac{\pi}{2}, \dfrac{3\pi}{2}$）で $\cos\theta_k = 0$ となり，$\lambda = 0$ の固有値はともに $0$ に縮退している。このとき
  $$
  \mu_{k, \pm}(\lambda) = \pm \lambda
  $$
  となるため，変化量 $\Delta\mu_{k, \pm} = \pm \lambda$ は $\lambda$ の **1 乗**に比例する。

$$
\finalanswer{\Delta\mu_{k, \pm} \propto \lambda^2 \quad \left(\cos\frac{2\pi k}{n} \neq 0\right), \qquad \Delta\mu_{k, \pm} \propto \lambda \quad \left(4 \mid n,\; \cos\frac{2\pi k}{n} = 0\right)}
$$

<aside class="rigor-note" markdown>
**補足**：(2)(ii) の結果は，量子力学における摂動論の一般構造をそのまま反映している。摂動項 $V = \begin{pmatrix} O & \lambda I \\ \lambda I & O \end{pmatrix}$ は非対角ブロックのみに現れるため，非縮退固有状態に対する 1 次摂動エネルギーは $0$ となり，最低次のシフトは 2 次摂動の $O(\lambda^2)$ から現れる。一方，$n$ が 4 の倍数のときに生じる $\cos(2\pi k/n) = 0$ の縮退部分空間では，摂動行列の対角化によって 1 次摂動の $O(\lambda)$ で縮退が解消される。
</aside>
