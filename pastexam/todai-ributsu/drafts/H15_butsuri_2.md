---
title: 東大理物 平成15年度 物理学 第2問：2元合金の平均場近似と相分離
tags:
  - 院試過去問
  - 東大理物
  - 統計力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成15年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成15年度 物理学 第2問：2元合金の平均場近似と相分離

## 問題

イオン半径のほぼ等しい2種の元素 A，B を高温で溶かして均一に混ぜ合わせ，その後急冷して，温度 $T$ で合金（固溶体）を作る。元素 A，B は濃度比によらず格子定数が一定の単純立方格子を作ると仮定する。また，原子 A と A，B と B が最近接で隣り合うときの相互作用エネルギーは等しくその大きさを $a$，A と B が最近接で隣り合うときの相互作用エネルギーの大きさを $b$ であるとし，これ以外には相互作用は働かないとする。A どうし，B どうしが隣り合う方が，A，B が隣り合うよりもエネルギーが低く，$a < b$ が満たされているとする。ただし，合金中の A，B の原子数濃度は等しいとする。
{: .problem-lead }

(1) 格子点 $i$ が A 原子で占められているときを $\sigma_i = 1$，B 原子で占められているときを $\sigma_i = -1$ とする変数 $\sigma_i$ を使うと，この合金のモデルのハミルトニアンは

$$
H = \sum_{\langle i, j \rangle} (P\sigma_i\sigma_j + Q)
$$

という形に書けることを示し，$P$ と $Q$ を $a, b$ を用いてあらわせ。ただし，$\langle i, j \rangle$ は最近接格子点の組である。ここで今の場合，A，B が50%ずつなので，対称性から化学ポテンシャルの項 $-\mu\sum_i \sigma_i$ は必要ないことを注意しておく。

(2) この系の場合，$\sigma_i$ の平均値 $p = \langle\sigma_i\rangle$ の値はいくつか。

(3) ハミルトニアンの中の相互作用を表す項 $\sigma_i\sigma_j$ を定数 $m$ を用いて，$(\sigma_i + \sigma_j)m - m^2$ と置き換える近似を行ない

$$
H = \sum_{\langle i, j \rangle} \bigl[P\{(\sigma_i + \sigma_j)m - m^2\} + Q\bigr]
$$

と表わす。$m$ を設問 (2) で決まっている $\sigma_i$ の一様な平均値 $m = p = \langle\sigma_i\rangle = \langle\sigma_j\rangle$ で与えるならば，この近似は相互作用の相手を平均値で置き換えることになり，「平均場近似」と呼ばれる。しかし，ここではより一般に $m$ をパラメタと考える。すなわち，上記の近似での平均値 $m$ が設問 (2) で与えられる系全体の平均値 $p$ と関係なく与えられるとしたときに，上記のハミルトニアンで与えられる系の分配関数 $Z$ と自由エネルギー $F$ を $m, N, a, b$ および温度 $T$ の関数として表わせ。ただし系の全格子点数は $N$ であり，周期的境界条件下にあるとしてよい。以下，ボルツマン定数を $k_B$ とする。

(4) 設問 (3) で求めた自由エネルギー $F$ を $m$ が小さいと考えて $m$ の4次まで展開した表式は $F = u + vm^2 + wm^4$ と書ける。$u, v, w$ を $N, T, a, b$ を用いて表わせ。

(5) もしも $m$ が自由に選べて，設問 (4) で展開して4次まで求めた自由エネルギーが最小になる $m$ が実現されるとすると，$m$ は温度の関数としてどのようにふるまうか。$k_B T > 2(b - a)$ の範囲でおおざっぱに $m$ と $T$ の関係を表わすグラフも書け。

(6) 設問 (4) で求めた自由エネルギーの表式を用いて，この系の温度を下げてくるときに，この合金系の熱平衡状態でどのような相転移が生ずるか，説明せよ。ただし A，B の組成比が決まっているときに，物体全体では $\sigma_i$ の平均値 $m$ の値は設問 (2) の値で決まっていて固定されていることに注意せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成15年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
2種の原子の配置をイジング変数 $\sigma_i = \pm 1$ に写像することで，2元合金の相互作用エネルギーを最近接イジング模型のハミルトニアンとして表します。単純立方格子の配位数 $z = 6$ を用いて平均場ハミルトニアンの分配関数と自由エネルギーを計算します。

自由エネルギーを秩序変数 $m$ の4次まで展開すると，2次の係数の符号が変わる転移温度が現れます。さらに，合金全体の組成比が固定されているという拘束条件を加えることで，低温での熱平衡状態がどのような相構造をとるかを導きます。
</div>

### (1)

最近接格子点の組 $\langle i, j \rangle$ において，積 $\sigma_i\sigma_j$ は A-A または B-B の同種原子対のとき $+1$，A-B の異種原子対のとき $-1$ となります。したがって，1つの最近接対の相互作用エネルギー $E_{ij}$ は $\sigma_i\sigma_j$ の1次式 $P\sigma_i\sigma_j + Q$ で表すことができます。

同種対のエネルギーが $a$，異種対のエネルギーが $b$ なので，$P, Q$ は次の連立方程式を満たします。

$$
P + Q = a, \qquad -P + Q = b
$$

2式の差と和をとって $P, Q$ を求めます。

$$
\finalanswer{P = \frac{a - b}{2}, \qquad Q = \frac{a + b}{2}}
$$

全最近接対について和をとることで，ハミルトニアンは $H = \sum_{\langle i, j \rangle}(P\sigma_i\sigma_j + Q)$ となります。

### (2)

合金中の A 原子と B 原子の個数は等しく，それぞれ $\dfrac{N}{2}$ 個です。したがって，$\sigma_i$ の平均値 $p$ は次式となります。

$$
\begin{aligned}
p &= \frac{1}{N}\sum_{i=1}^{N} \sigma_i \\
&= \frac{1}{N}\left(\frac{N}{2}\cdot 1 + \frac{N}{2}\cdot(-1)\right) \\
&= 0
\end{aligned}
$$

$$
\finalanswer{p = 0}
$$

### (3)

単純立方格子では各格子点が $z = 6$ 個の最近接格子点をもつため，周期的境界条件下での最近接対の総数は $\dfrac{zN}{2} = 3N$ です。また，和 $\sum_{\langle i, j \rangle}(\sigma_i + \sigma_j)$ では各 $\sigma_i$ が $6$ 回ずつ現れます。これを用いてハミルトニアンを書き換えます。

$$
\begin{aligned}
H &= \sum_{\langle i, j \rangle} \bigl[P(\sigma_i + \sigma_j)m - Pm^2 + Q\bigr] \\
&= 3N(Q - Pm^2) + 6Pm\sum_{i=1}^{N} \sigma_i
\end{aligned}
$$

設問 (1) の $P = -\dfrac{b - a}{2}$，$Q = \dfrac{a + b}{2}$ を代入します。

$$
H = \frac{3}{2}N(a + b) + \frac{3}{2}N(b - a)m^2 - 3(b - a)m\sum_{i=1}^{N} \sigma_i
$$

$\beta = \dfrac{1}{k_{\mathrm{B}}T}$ とおき，各サイトの $\sigma_i = \pm 1$ が独立であることを用いて分配関数 $Z$ を計算します。

$$
\begin{aligned}
Z &= \sum_{\sigma_1 = \pm 1} \cdots \sum_{\sigma_N = \pm 1} e^{-\beta H} \\
&= \exp\!\left\{-\frac{3N}{2k_{\mathrm{B}}T}\bigl((a + b) + (b - a)m^2\bigr)\right\} \prod_{i=1}^{N}\left(\sum_{\sigma_i = \pm 1} \exp\!\left\{\frac{3(b - a)m}{k_{\mathrm{B}}T}\sigma_i\right\}\right) \\
&= \exp\!\left\{-\frac{3N}{2k_{\mathrm{B}}T}\bigl((a + b) + (b - a)m^2\bigr)\right\} \left\{2\cosh\!\left(\frac{3(b - a)m}{k_{\mathrm{B}}T}\right)\right\}^N
\end{aligned}
$$

自由エネルギー $F = -k_{\mathrm{B}}T\log Z$ を計算します。

$$
\begin{aligned}
F &= -k_{\mathrm{B}}T\log Z \\
&= \frac{3}{2}N(a + b) + \frac{3}{2}N(b - a)m^2 - N k_{\mathrm{B}}T\log\!\left\{2\cosh\!\left(\frac{3(b - a)m}{k_{\mathrm{B}}T}\right)\right\}
\end{aligned}
$$

したがって，$Z$ と $F$ は次式となります。

$$
\finalanswer{
\begin{aligned}
Z &= \exp\!\left\{-\frac{3N}{2k_{\mathrm{B}}T}\bigl((a + b) + (b - a)m^2\bigr)\right\} \left\{2\cosh\!\left(\frac{3(b - a)m}{k_{\mathrm{B}}T}\right)\right\}^N \\
F &= \frac{3}{2}N(a + b) + \frac{3}{2}N(b - a)m^2 - N k_{\mathrm{B}}T\log\!\left\{2\cosh\!\left(\frac{3(b - a)m}{k_{\mathrm{B}}T}\right)\right\}
\end{aligned}
}
$$

### (4)

$|x| \ll 1$ に対するテイラー展開 $\cosh x = 1 + \dfrac{1}{2}x^2 + \dfrac{1}{24}x^4 + O(x^6)$ および $\log(1 + \delta) = \delta - \dfrac{1}{2}\delta^2 + O(\delta^3)$ を用いて，$\log(\cosh x)$ を4次まで展開します。

$$
\begin{aligned}
\log(\cosh x) &= \left(\frac{1}{2}x^2 + \frac{1}{24}x^4\right) - \frac{1}{2}\left(\frac{1}{2}x^2\right)^2 + O(x^6) \\
&= \frac{1}{2}x^2 - \frac{1}{12}x^4 + O(x^6)
\end{aligned}
$$

ここに $x = \dfrac{3(b - a)m}{k_{\mathrm{B}}T}$ を代入して $F$ を展開します。

$$
\begin{aligned}
F &= \frac{3}{2}N(a + b) + \frac{3}{2}N(b - a)m^2 - N k_{\mathrm{B}}T\left\{\log 2 + \frac{1}{2}\left(\frac{3(b - a)m}{k_{\mathrm{B}}T}\right)^2 - \frac{1}{12}\left(\frac{3(b - a)m}{k_{\mathrm{B}}T}\right)^4\right\} \\
&= \left\{\frac{3}{2}N(a + b) - N k_{\mathrm{B}}T\log 2\right\} + \frac{3}{2}N(b - a)\left\{1 - \frac{3(b - a)}{k_{\mathrm{B}}T}\right\}m^2 + \frac{27N(b - a)^4}{4(k_{\mathrm{B}}T)^3}m^4
\end{aligned}
$$

したがって，係数 $u, v, w$ は次式となります。

$$
\finalanswer{u = \frac{3}{2}N(a + b) - N k_{\mathrm{B}}T\log 2, \quad v = \frac{3}{2}N(b - a)\left(1 - \frac{3(b - a)}{k_{\mathrm{B}}T}\right), \quad w = \frac{27N(b - a)^4}{4(k_{\mathrm{B}}T)^3}}
$$

### (5)

$a < b$ より常に $w > 0$ です。$F(m) = u + vm^2 + wm^4$ を $m$ で微分して停留条件を求めます。

$$
\begin{aligned}
\frac{\partial F}{\partial m} &= 2vm + 4wm^3 \\
&= 2m(v + 2wm^2)
\end{aligned}
$$

ここで転移温度 $T_c$ を $v = 0$ の条件から定めます。

$$
k_{\mathrm{B}}T_c = 3(b - a)
$$

$T \ge T_c$ すなわち $k_{\mathrm{B}}T \ge 3(b - a)$ のとき，$v \ge 0$ かつ $w > 0$ なので，$F(m)$ は $m = 0$ のみで最小値をとります。

$T < T_c$ すなわち $k_{\mathrm{B}}T < 3(b - a)$ のとき，$v < 0$ となるため，$m = 0$ は極大となり，$v + 2wm^2 = 0$ の解で最小値をとります。$m^2$ を計算します。

$$
\begin{aligned}
m^2 &= -\frac{v}{2w} \\
&= \frac{\dfrac{3}{2}N(b - a)\left(\dfrac{3(b - a)}{k_{\mathrm{B}}T} - 1\right)}{\dfrac{27N(b - a)^4}{2(k_{\mathrm{B}}T)^3}} \\
&= \frac{(k_{\mathrm{B}}T)^2}{9(b - a)^3}\bigl(3(b - a) - k_{\mathrm{B}}T\bigr) \\
&= 3\left(\frac{T}{T_c}\right)^2\left(1 - \frac{T}{T_c}\right)
\end{aligned}
$$

したがって，最小値を与える $m$ は次式となります。

$$
\finalanswer{m = \begin{cases} 0 & \bigl(k_{\mathrm{B}}T \ge 3(b - a)\bigr) \\[6pt] \pm\dfrac{k_{\mathrm{B}}T}{3(b - a)}\sqrt{3 - \dfrac{k_{\mathrm{B}}T}{b - a}} & \bigl(k_{\mathrm{B}}T < 3(b - a)\bigr) \end{cases}}
$$

$k_{\mathrm{B}}T > 2(b - a)$ の範囲では，$T$ が $T_c$ より下がると $m$ は $0$ から $\pm\sqrt{3(1 - T/T_c)}$ のように連続的に立ち上がって2つの枝に分岐し，$k_{\mathrm{B}}T = 2(b - a)$ で $|m| = \dfrac{2}{3}$ に達します。$m$ と $k_{\mathrm{B}}T$ の関係のグラフは次のようになります。

<figure class="problem-figure" markdown>
![4次展開自由エネルギーを最小にするmの温度依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H15_butsuri_2-s-light.svg#only-light)
![4次展開自由エネルギーを最小にするmの温度依存性](../../../docs/assets/figures/pastexam-todai-ributsu/H15_butsuri_2-s-dark.svg#only-dark)
<figcaption markdown="span">$k_{\mathrm{B}}T > 2(b - a)$ の範囲における，4次展開の自由エネルギー $F$ を最小にする $m$ の温度依存性。</figcaption>
</figure>

### (6)

高温の $T \ge T_c = \dfrac{3(b - a)}{k_{\mathrm{B}}}$ では，自由エネルギー $F(m)$ が $m = 0$ で最小になるため，A 原子と B 原子が格子上に均一に混ざり合った一様な固溶体相が安定な熱平衡状態になります。

温度を下げて $T < T_c$ になると，設問 (5) より自由エネルギーは $m = +m_0$ と $m = -m_0$（$m_0 > 0$）の2点で最小をとり，一様な混合状態 $m = 0$ は極大となって不安定になります。しかし，合金全体では A と B の組成比が50%ずつに固定されているため，系全体での平均値 $\langle\sigma_i\rangle = 0$ を保つ必要があり，系全体が一様に $+m_0$ または $-m_0$ の状態になることはできません。

その結果，系は局所的な秩序変数が $+m_0$ となる A 原子の多い相と，$-m_0$ となる B 原子の多い相に半分ずつの体積比で分かれます。この現象を**相分離**といいます。このように2相が共存することで，系全体の平均値 $p = 0$ を保ったまま全体の自由エネルギーを $F(\pm m_0)$ まで下げることができます。
