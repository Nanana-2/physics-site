---
title: 東大理物 平成20年度 数学 第1問：3次元回転行列と実交代行列の指数関数
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成20年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成20年度 数学 第1問：3次元回転行列と実交代行列の指数関数

## 問題

**(i)** 3次元空間回転を表す3次元実正方行列すべての集合を $R$ とする。$R$ は単位行列 $I$ も含むものとする。これに関して，以下の各命題の真偽を○（真）か×（偽）かで答えよ。
{: .problem-lead }

(a) $X \in R$ かつ $Y \in R$ ならば $XY \in R$ である。

(b) $X \in R$ かつ $Y \in R$ ならば $XY = YX$ である。

(c) $X \in R$ ならば ${}^t X X = X {}^t X = I$ である。ただし，${}^t X$ は $X$ の転置行列を表す。

(d) ${}^t X X = X {}^t X = I$ であるならば $X \in R$ である。

(e) $X \in R$ ならば $U^\dagger X U$ が対角行列であるようなユニタリ行列 $U$ が存在する。ただし，$U^\dagger$ は $U$ のエルミート共役行列（転置行列の複素共役）を表す。

**(ii)** $\Omega(\boldsymbol{n}, \theta)$ を，単位ベクトル $\boldsymbol{n}$ の方向を回転軸とした角度 $\theta$ の回転を表す3次元実正方行列とする。ここで，$\boldsymbol{n}$ 方向に右ねじを進める時右ねじを回す向きを正とする回転角を $\theta$ とする。また，任意の3次元実ベクトル $\boldsymbol{v}_0$ に対して，$\boldsymbol{v}(\theta)$ を $\boldsymbol{v}(\theta) = \Omega(\boldsymbol{n}, \theta)\boldsymbol{v}_0$ で定義する。以下の設問に答えよ。
{: .problem-lead }

(1) $\boldsymbol{n} = (0, 0, 1)$ のとき，$\Omega(\boldsymbol{n}, \theta)$ の3つの固有値を答えよ。

(2) 任意の $\boldsymbol{n}$ に対して，$\Omega(\boldsymbol{n}, \theta)$ の3つの固有値を答えよ。

(3) 原点を始点としたとき $\boldsymbol{v}(\theta)$ の終点がどれだけ移動するかを考えて，

$$
\boldsymbol{v}(\theta + \Delta\theta) - \boldsymbol{v}(\theta) = \boldsymbol{n}\times\boldsymbol{v}(\theta)\,\Delta\theta
$$

となることを説明せよ。ただし，$\Delta\theta$ は $\theta$ に比べて十分小さいものとする。また，$\times$ はベクトル積（外積）である。必要なら図を用いて説明してもよい。

(4) 設問 (3) の結果から得られる $\boldsymbol{v}(\theta)$ に関する微分方程式を解くことによって，

$$
\Omega(\boldsymbol{n}, \theta) = e^{\theta A(\boldsymbol{n})}
$$

であることを示せ。ここで，$A(\boldsymbol{a})$ は，ある3次元実ベクトル $\boldsymbol{a}$ に対して決まる3次元実正方行列であり，任意のベクトル $\boldsymbol{u}$ に対して $A(\boldsymbol{a})\boldsymbol{u} = \boldsymbol{a}\times\boldsymbol{u}$ を満たすものとする。

(5) 3次元実交代行列

$$
X = \begin{pmatrix} 0 & x_{12} & x_{13} \\ x_{21} & 0 & x_{23} \\ x_{31} & x_{32} & 0 \end{pmatrix} \qquad (\text{ただし，} x_{ij} = -x_{ji},\quad i, j = 1 \sim 3)
$$

に対して，$X = A(\boldsymbol{a}_0)$ となるような3次元実ベクトル $\boldsymbol{a}_0$ を求めよ。ここで，$A$ は設問 (4) で定義されたものと同じである。

(6) $Y = e^X$ となるような3次元実交代行列 $X$ が存在するならば $Y$ は3次元回転を表す行列であることを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成20年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
3次元空間の回転はベクトルの長さと向きを保つ線形変換であり，行列式が $+1$ の実直交行列と1対1に対応します。任意の軸の周りの回転は座標軸の回転による相似変換で $z$ 軸周りの回転へ移すことができるため，固有値は回転軸の向きによりません。

また，回転角を微小量 $\Delta\theta$ だけ増やしたときのベクトルの変化は回転軸ベクトルとの外積で表され，線形常微分方程式になります。外積の作用を行列で書くと3次元実交代行列と1対1に対応するため，回転行列を行列指数関数で表すことができます。
</div>

### (i)

3次元空間回転を表す行列の集合 $R$ は，${}^t X X = X {}^t X = I$ かつ $\det X = 1$ を満たす3次元実正方行列の集合です。各命題の真偽を確かめます。

- (a) **○**：$X, Y \in R$ のとき，${}^t(XY)(XY) = {}^t Y ({}^t X X) Y = {}^t Y Y = I$，かつ $\det(XY) = (\det X)(\det Y) = 1\cdot 1 = 1$ なので，$XY \in R$ です。
- (b) **×**：3次元空間の回転は一般に非可換です。たとえば $x$ 軸周りの $\dfrac{\pi}{2}$ 回転 $R_x$ と $y$ 軸周りの $\dfrac{\pi}{2}$ 回転 $R_y$ の積を計算します。

$$
R_x = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad R_y = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{pmatrix}
$$

$$
R_x R_y = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}, \qquad R_y R_x = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{pmatrix}
$$

$R_x R_y \neq R_y R_x$ なので偽です。

- (c) **○**：回転は任意の2つのベクトルの内積を保つ変換なので，$X \in R$ は直交行列であり ${}^t X X = X {}^t X = I$ を満たします。
- (d) **×**：${}^t X X = I$ の両辺の行列式をとると $(\det X)^2 = 1$ より $\det X = \pm 1$ となります。たとえば反転 $X = -I$ は ${}^t X X = X {}^t X = I$ を満たしますが，$\det(-I) = -1$ なので回転ではなく $X \notin R$ です。
- (e) **○**：$X$ は実行列かつ直交行列なので，$X^\dagger = {}^t X = X^{-1}$ です。よって $X^\dagger X = X X^\dagger = I$ となり $X$ は正規行列です。正規行列はユニタリ行列 $U$ によって対角化することができるため，$U^\dagger X U$ が対角行列となるユニタリ行列 $U$ が存在します。

したがって，各命題の真偽は (a) ○，(b) ×，(c) ○，(d) ×，(e) ○ となります。

### (ii) (1)

$\boldsymbol{n} = (0, 0, 1)$，すなわち $z$ 軸周りの角度 $\theta$ の回転行列は次式です。

$$
\Omega(\boldsymbol{e}_3, \theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

固有値を $\lambda$ として固有方程式を解きます。

$$
\begin{aligned}
\det\bigl(\Omega(\boldsymbol{e}_3, \theta) - \lambda I\bigr) &= 0 \\
(1 - \lambda)\bigl((\cos\theta - \lambda)^2 + \sin^2\theta\bigr) &= 0 \\
(1 - \lambda)\bigl(\lambda^2 - 2\lambda\cos\theta + 1\bigr) &= 0 \\
(1 - \lambda)(\lambda - e^{i\theta})(\lambda - e^{-i\theta}) &= 0
\end{aligned}
$$

したがって，3つの固有値は次式となります。

$$
\finalanswer{1, \quad e^{i\theta}, \quad e^{-i\theta}}
$$

### (ii) (2)

任意の単位ベクトル $\boldsymbol{n}$ に対し，$\boldsymbol{e}_3 = (0, 0, 1)$ を $\boldsymbol{n}$ に移すような3次元回転行列 $P \in R$ を選ぶことができます。すなわち $P\boldsymbol{e}_3 = \boldsymbol{n}$ です。このとき，回転軸 $\boldsymbol{n}$ 周りの角度 $\theta$ の回転は，まず $P^{-1}$ で $\boldsymbol{n}$ を $\boldsymbol{e}_3$ に移し，次に $\boldsymbol{e}_3$ 周りに $\theta$ だけ回転してから，$P$ で元に戻す操作に等しいため，次式が成り立ちます。

$$
\Omega(\boldsymbol{n}, \theta) = P\Omega(\boldsymbol{e}_3, \theta)P^{-1}
$$

相似変換によって固有多項式は不変です。

$$
\begin{aligned}
\det\bigl(\Omega(\boldsymbol{n}, \theta) - \lambda I\bigr) &= \det\Bigl(P\bigl(\Omega(\boldsymbol{e}_3, \theta) - \lambda I\bigr)P^{-1}\Bigr) \\
&= \det P \cdot \det\bigl(\Omega(\boldsymbol{e}_3, \theta) - \lambda I\bigr) \cdot \det(P^{-1}) \\
&= \det\bigl(\Omega(\boldsymbol{e}_3, \theta) - \lambda I\bigr)
\end{aligned}
$$

よって固有値は (1) と同じです。

$$
\finalanswer{1, \quad e^{i\theta}, \quad e^{-i\theta}}
$$

### (ii) (3)

回転軸 $\boldsymbol{n}$ とベクトル $\boldsymbol{v}(\theta)$ のなす角を $\alpha$（$0 \le \alpha \le \pi$）とします。回転によって $\boldsymbol{v}(\theta)$ の大きさと $\boldsymbol{n}$ とのなす角 $\alpha$ は変わらないため，$\boldsymbol{v}(\theta)$ の終点は $\boldsymbol{n}$ に垂直な平面上で半径 $|\boldsymbol{v}(\theta)|\sin\alpha$ の円周上を動きます。

<figure class="problem-figure" markdown>
![微小回転によるベクトルの終点の移動](../../assets/figures/pastexam-todai-ributsu/H20_sugaku_1-s-light.svg#only-light)
![微小回転によるベクトルの終点の移動](../../assets/figures/pastexam-todai-ributsu/H20_sugaku_1-s-dark.svg#only-dark)
<figcaption markdown="span">回転軸 $\boldsymbol{n}$ 周りの微小角 $\Delta\theta$ の回転による終点の移動 $\Delta\boldsymbol{v} = \boldsymbol{v}(\theta + \Delta\theta) - \boldsymbol{v}(\theta)$。</figcaption>
</figure>

回転角を $\theta$ から $\theta + \Delta\theta$ へ微小量 $\Delta\theta$ だけ増やすと，終点の移動ベクトル $\Delta\boldsymbol{v} = \boldsymbol{v}(\theta + \Delta\theta) - \boldsymbol{v}(\theta)$ の大きさは，円弧の長さで近似することができます。

$$
\begin{aligned}
|\Delta\boldsymbol{v}| &= |\boldsymbol{v}(\theta)|\sin\alpha \cdot |\Delta\theta| \\
&= |\boldsymbol{n}||\boldsymbol{v}(\theta)|\sin\alpha \cdot |\Delta\theta| \\
&= |\boldsymbol{n}\times\boldsymbol{v}(\theta)|\,|\Delta\theta|
\end{aligned}
$$

ここで $|\boldsymbol{n}| = 1$ を用いました。また，$\Delta\theta > 0$ のとき，終点は $\boldsymbol{n}$ 方向に右ねじを進める向きに回転するため，$\Delta\boldsymbol{v}$ は $\boldsymbol{n}$ と $\boldsymbol{v}(\theta)$ の両方に垂直で，右ねじの向きすなわち外積 $\boldsymbol{n}\times\boldsymbol{v}(\theta)$ の向きに一致します。$\Delta\theta < 0$ のときは逆向きになり，$\Delta\theta$ の符号を含めて一致します。

以上より，$\Delta\theta$ が十分小さいとき次式が成り立ちます。

$$
\boldsymbol{v}(\theta + \Delta\theta) - \boldsymbol{v}(\theta) = \boldsymbol{n}\times\boldsymbol{v}(\theta)\,\Delta\theta
$$

### (ii) (4)

設問 (3) の両辺を $\Delta\theta$ で割り，$\Delta\theta \to 0$ の極限をとります。$A(\boldsymbol{n})\boldsymbol{v}(\theta) = \boldsymbol{n}\times\boldsymbol{v}(\theta)$ を用いると，次の常微分方程式が得られます。

$$
\begin{aligned}
\frac{\mathrm{d}\boldsymbol{v}(\theta)}{\mathrm{d}\theta} &= \boldsymbol{n}\times\boldsymbol{v}(\theta) \\
&= A(\boldsymbol{n})\boldsymbol{v}(\theta)
\end{aligned}
$$

また，回転角 $\theta = 0$ のとき $\Omega(\boldsymbol{n}, 0) = I$ なので，初期条件は $\boldsymbol{v}(0) = \boldsymbol{v}_0$ です。ここで行列指数関数をべき級数で定義します。

$$
e^{\theta A(\boldsymbol{n})} = \sum_{k=0}^{\infty} \frac{\theta^k}{k!} A(\boldsymbol{n})^k
$$

$\tilde{\boldsymbol{v}}(\theta) = e^{\theta A(\boldsymbol{n})}\boldsymbol{v}_0$ とおくと，$\tilde{\boldsymbol{v}}(0) = I\boldsymbol{v}_0 = \boldsymbol{v}_0$ であり，項別微分を行うと次式を満たします。

$$
\begin{aligned}
\frac{\mathrm{d}\tilde{\boldsymbol{v}}(\theta)}{\mathrm{d}\theta} &= \sum_{k=1}^{\infty} \frac{\theta^{k-1}}{(k - 1)!} A(\boldsymbol{n})^k \boldsymbol{v}_0 \\
&= A(\boldsymbol{n})\left(\sum_{m=0}^{\infty} \frac{\theta^m}{m!} A(\boldsymbol{n})^m\right)\boldsymbol{v}_0 \\
&= A(\boldsymbol{n})\tilde{\boldsymbol{v}}(\theta)
\end{aligned}
$$

線形常微分方程式の初期値問題の解の一意性より，$\boldsymbol{v}(\theta) = e^{\theta A(\boldsymbol{n})}\boldsymbol{v}_0$ です。定義から $\boldsymbol{v}(\theta) = \Omega(\boldsymbol{n}, \theta)\boldsymbol{v}_0$ なので，任意の3次元実ベクトル $\boldsymbol{v}_0$ に対して

$$
\Omega(\boldsymbol{n}, \theta)\boldsymbol{v}_0 = e^{\theta A(\boldsymbol{n})}\boldsymbol{v}_0
$$

が成り立ちます。したがって，$\Omega(\boldsymbol{n}, \theta) = e^{\theta A(\boldsymbol{n})}$ です。

### (ii) (5)

$\boldsymbol{a}_0 = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$，$\boldsymbol{u} = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}$ とおき，外積 $\boldsymbol{a}_0\times\boldsymbol{u}$ を成分で計算します。

$$
\begin{aligned}
\boldsymbol{a}_0 \times \boldsymbol{u} &= \begin{pmatrix} a_2 u_3 - a_3 u_2 \\ a_3 u_1 - a_1 u_3 \\ a_1 u_2 - a_2 u_1 \end{pmatrix} \\
&= \begin{pmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{pmatrix}\begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}
\end{aligned}
$$

したがって，行列 $A(\boldsymbol{a}_0)$ は次式になります。

$$
A(\boldsymbol{a}_0) = \begin{pmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{pmatrix}
$$

これを与えられた実交代行列 $X$ の各成分と比べます。

$$
\begin{aligned}
-a_3 &= x_{12}, & a_2 &= x_{13}, & -a_1 &= x_{23} \\
a_3 &= x_{21}, & -a_2 &= x_{31}, & a_1 &= x_{32}
\end{aligned}
$$

$x_{ij} = -x_{ji}$ なので上下の式は矛盾なく一致し，$a_1 = -x_{23} = x_{32}$，$a_2 = x_{13} = -x_{31}$，$a_3 = -x_{12} = x_{21}$ が得られます。したがって，求めるベクトル $\boldsymbol{a}_0$ は次式となります。

$$
\finalanswer{\boldsymbol{a}_0 = \begin{pmatrix} -x_{23} \\ x_{13} \\ -x_{12} \end{pmatrix} = \begin{pmatrix} x_{32} \\ x_{13} \\ x_{21} \end{pmatrix}}
$$

### (ii) (6)

$X$ は3次元実交代行列なので，設問 (5) より $X = A(\boldsymbol{a}_0)$ を満たす3次元実ベクトル $\boldsymbol{a}_0$ が存在します。

まず $\boldsymbol{a}_0 = \boldsymbol{0}$，すなわち $X = O$ のときは $Y = e^O = I$ です。単位行列 $I$ は回転角 $0$ の回転を表すので $Y \in R$ です。

次に $\boldsymbol{a}_0 \neq \boldsymbol{0}$ のときは，$\theta = |\boldsymbol{a}_0| > 0$，単位ベクトル $\boldsymbol{n} = \dfrac{\boldsymbol{a}_0}{|\boldsymbol{a}_0|}$ とおきます。任意のベクトル $\boldsymbol{u}$ に対して

$$
\begin{aligned}
A(\boldsymbol{a}_0)\boldsymbol{u} &= (\theta\boldsymbol{n})\times\boldsymbol{u} \\
&= \theta(\boldsymbol{n}\times\boldsymbol{u}) \\
&= \theta A(\boldsymbol{n})\boldsymbol{u}
\end{aligned}
$$

が成り立つので，$X = A(\boldsymbol{a}_0) = \theta A(\boldsymbol{n})$ です。したがって，設問 (4) の結果から次式が得られます。

$$
\begin{aligned}
Y &= e^X \\
&= e^{\theta A(\boldsymbol{n})} \\
&= \Omega(\boldsymbol{n}, \theta)
\end{aligned}
$$

よって $Y$ は単位ベクトル $\boldsymbol{n}$ を軸とする角度 $\theta$ の3次元回転を表す行列です。
