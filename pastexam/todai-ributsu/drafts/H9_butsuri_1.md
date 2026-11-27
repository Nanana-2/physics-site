---
title: 東大理物 平成9年度 物理学 第1問：励起子の束縛エネルギー・デルタ関数摂動と重ね合わせ状態の測定統計
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
  - 物性物理学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成9年度 物理学 第1問：励起子の束縛エネルギー・デルタ関数摂動と重ね合わせ状態の測定統計

## 問題

水素原子の中の陽子と電子の相対運動のシュレディンガー方程式は，相対座標を $\mathbf{r}$，換算質量を $m$ とすると，cgs ガウス系を単位系に用いた場合，通常次の形に書かれる。

$$
\left[-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right]\psi(\mathbf{r}) = E\psi(\mathbf{r}), \qquad \text{(1)}
$$

$$
V = -e^2/r. \qquad \text{(2)}
$$

この固有エネルギー $E_n$ と固有関数 $\psi_{n\ell m}(\mathbf{r})$ は次のように求まる：

$$
E_n = -\frac{R_y}{n^2} \quad (n = 1, 2, \dots), \quad \text{ただし } R_y \equiv \frac{me^4}{2\hbar^2} \text{ は Rydberg 定数}, \qquad \text{(3)}
$$

$$
\psi_{n\ell m}(\mathbf{r}) = R_{n\ell}(r)Y_{\ell m}(\theta, \phi) \quad (\ell = 0, 1, \dots, n - 1;\ m = 0, \pm 1, \dots, \pm\ell). \qquad \text{(4)}
$$

ここで，$(r, \theta, \phi)$ は極座標，$Y_{\ell m}(\theta, \phi)$ は規格化された球面調和関数であり，たとえば，$Y_{00} = 1/\sqrt{4\pi}$ である。波動関数の動径部分 $R_{n\ell}(r)$ は，$1s$ 状態（$n = 1, \ell = 0$），$2s$ 状態（$n = 2, \ell = 0$）および $2p$ 状態（$n = 2, \ell = 1$）についてはそれぞれ，

$$
R_{10}(r) = \frac{2}{\sqrt{a^3}}\exp\left(-\frac{r}{a}\right), \qquad \text{(5)}
$$

$$
R_{20}(r) = \frac{1}{\sqrt{8a^3}}\left(2 - \frac{r}{a}\right)\exp\left(-\frac{r}{2a}\right), \qquad \text{(6)}
$$

$$
R_{21}(r) = \frac{1}{\sqrt{24a^5}}\,r\exp\left(-\frac{r}{2a}\right), \qquad \text{(7)}
$$

で与えられる。ただし $a \equiv \hbar^2/me^2$ は Bohr 半径である。

以上の知識を手がかりにして，以下の問いに答えよ。
{: .problem-lead }

(1) 絶縁体に弱い光を当てると，電子と正孔のペアができる。絶縁体の中では，電子は電荷 $-e$ で質量が $m_e$ の粒子のように，正孔は電荷 $+e$ で質量が $m_h$ の粒子のようにふるまい，両者の間にはたらくポテンシャルは，絶縁体の（比）誘電率を $\varepsilon$（定数とする）として，

$$
V = -\frac{e^2}{\varepsilon r} \qquad \text{(8)}
$$

で与えられると仮定する。電子と正孔の束縛状態について，以下の問いに答えよ。

(i) 最も低いエネルギーをもつ束縛状態の束縛エネルギーを求めよ。

(ii) この束縛状態の空間的広がりの目安として，$r$ の期待値 $\langle r \rangle$ を求めよ。

(2) 電子が実際に感じるポテンシャルは，式 (2) や式 (8) から少しずれていることが分かっている。たとえば水素原子の場合，陽子のごく近くでは，電子・陽電子対が仮想的に生成・消滅している「雲」の内側に入るためにポテンシャルが修正される。それが何をもたらすかを大ざっぱにみるために，式 (2) のポテンシャルを次のように修正してみよう。

$$
V(\mathbf{r}) = -\frac{e^2}{r} - \lambda\delta^3(\mathbf{r}). \qquad \text{(9)}
$$

ただし，$\lambda$ はある正の定数であり，$\delta^3(\mathbf{r})$ は3次元のデルタ関数である。

(i) $V$ の右辺第2項を摂動とみなし，摂動を受けた $1s$ 状態，$2s$ 状態，$2p$ 状態のエネルギーを，それぞれ $\lambda$ の一乗の精度で求めよ。

(ii) 摂動を受けた $1s$ 状態の電子について，電子を見いだす確率密度の $r = 0$ における値が，$\lambda = 0$ の場合の何倍になっているかを求めよ。ただし，摂動計算に用いる非摂動状態としては，$1s, 2s, 2p$ 状態だけを考慮すれば良く，また，$\lambda$ の一乗の精度までで良い。

(iii) この確率密度が $\lambda = 0$ の場合に比べて増加しているか減少しているかを述べ，式 (9) の形のポテンシャルがそのような確率密度の増加（あるいは減少）をもたらした理由を直感的に説明せよ。

(3) 通常のクーロンポテンシャルで記述される系，式 (1)〜(7)，に戻って，量子力学における確率の意味を考えよう。

時刻 $t = t_0$ に，電子を，$1s$ 状態と $2s$ 状態の次のような重ね合わせ状態に置く：

$$
\psi(\mathbf{r}, t = t_0) = [\psi_{100}(\mathbf{r}) + \psi_{200}(\mathbf{r})]/\sqrt{2} \qquad \text{(10)}
$$

(i) この状態では確率密度 $|\psi(\mathbf{r}, t)|^2$ が $t$ の周期関数になることを示し，その周期を求めよ。

(ii) 電子のエネルギーの期待値 $\langle E \rangle$ はいくらか？また，実際に電子のエネルギー $E$ を一度だけ測定した場合に，測定値として得られる可能性がある $E$ の値をすべて挙げ，その値が得られる確率を書け。

(iii) 一度目の測定を終了してから，もういちど式 (10) の状態の電子を用意し，その $E$ を測定する。さらにもう一度式 (10) の状態の電子を用意し，その $E$ を測定する，…，ということを繰り返し，全部で $N$ 回の測定を行うとする。$i$ 番目（$i = 1, 2, \dots, N$）の測定で得た $E$ の測定値を $\varepsilon_i$ と記すと，通常，その平均値

$$
\bar{\varepsilon}_N = \frac{1}{N}\sum_{i=1}^{N} \varepsilon_i \qquad \text{(11)}
$$

を「$E$ の実験値」として，理論値と比較することになる。しかしながら，測定の回数 $N$ が有限である以上，$\bar{\varepsilon}_N$ は一般には上で計算した $\langle E \rangle$ とは異なる。この，実験値 $\bar{\varepsilon}_N$ と理論値 $\langle E \rangle$ のずれを $\delta$ と記すことにする。その自乗期待値

$$
\langle \delta^2 \rangle \equiv \langle (\bar{\varepsilon}_N - \langle E \rangle)^2 \rangle \qquad \text{(12)}
$$

を求めよ。そして，無限回の測定を繰り返せば $\bar{\varepsilon}_N$ が $\langle E \rangle$ に一致すると期待できること，即ち，$N \to \infty$ で $\langle \delta^2 \rangle \to 0$ となることを確かめよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
電子と正孔の相対運動は，水素原子の換算質量 $m$ を電子・正孔の換算質量 $\mu$ に，結合定数 $e^2$ を $e^2/\varepsilon$ に置き換えた同じシュレーディンガー方程式に従います。そのため，固有エネルギーとボーア半径の公式をそのまま読み替えることができます。

原点に局在したデルタ関数摂動 $-\lambda\delta^3(\mathbf{r})$ の行列要素は原点での波動関数の積だけで決まるため，$r = 0$ で $0$ になる $2p$ 状態とは一切結合せず，$s$ 状態どうしの計算だけで1次のエネルギー変化と波動関数の補正が求まります。最後の測定統計は，互いに独立な $N$ 回の試行の標本平均の分散が1回の分散の $1/N$ になる性質から計算します。
</div>

### (1)(i)

質量 $m_e$ の電子と質量 $m_h$ の正孔の相対運動に対する換算質量 $\mu$ は次式で与えられます。

$$
\mu = \frac{m_e m_h}{m_e + m_h}
$$

ポテンシャル $V = -\dfrac{e^2}{\varepsilon r}$ は，水素原子のポテンシャル $V = -\dfrac{e^2}{r}$ において $e^2$ を $\dfrac{e^2}{\varepsilon}$ に置き換えた形です。したがって式 (3) の $R_y = \dfrac{me^4}{2\hbar^2}$ において $m \to \mu$，$e^2 \to \dfrac{e^2}{\varepsilon}$ と置き換えると，電子と正孔の束縛状態の固有エネルギー $E_n^*$ が得られます。

$$
\begin{aligned}
E_n^* &= -\frac{\mu (e^2/\varepsilon)^2}{2\hbar^2 n^2} \\
&= -\frac{m_e m_h e^4}{2(m_e + m_h)\varepsilon^2 \hbar^2 n^2}
\end{aligned}
$$

最も低いエネルギーをもつ束縛状態は $n = 1$ の基底状態です。その束縛エネルギー $E_{\mathrm{b}} = |E_1^*|$ は次の通りです。

$$
\finalanswer{E_{\mathrm{b}} = \frac{m_e m_h e^4}{2(m_e + m_h)\varepsilon^2 \hbar^2}}
$$

### (1)(ii)

同様にボーア半径 $a = \dfrac{\hbar^2}{me^2}$ において $m \to \mu$，$e^2 \to \dfrac{e^2}{\varepsilon}$ と置き換えると，電子と正孔の束縛状態に対する有効ボーア半径 $a^*$ は次のようになります。

$$
\begin{aligned}
a^* &= \frac{\hbar^2 \varepsilon}{\mu e^2} \\
&= \frac{(m_e + m_h)\varepsilon\hbar^2}{m_e m_h e^2}
\end{aligned}
$$

基底状態の波動関数は式 (5) で $a \to a^*$ とした $\psi_{100}^*(\mathbf{r}) = R_{10}^*(r)Y_{00}$ です。球面調和関数の規格化 $\int |Y_{00}|^2\,\mathrm{d}\Omega = 1$ を用いて，$r$ の期待値 $\langle r \rangle$ を計算します。

$$
\begin{aligned}
\langle r \rangle &= \int_0^\infty r |R_{10}^*(r)|^2 r^2\,\mathrm{d}r \\
&= \frac{4}{(a^*)^3}\int_0^\infty r^3 \exp\left(-\frac{2r}{a^*}\right)\mathrm{d}r
\end{aligned}
$$

ここで変数変換 $u = \dfrac{2r}{a^*}$ を行うと，$r = \dfrac{a^*}{2}u$，$\mathrm{d}r = \dfrac{a^*}{2}\,\mathrm{d}u$ となります。ガンマ関数の公式 $\int_0^\infty u^3 e^{-u}\,\mathrm{d}u = 6$ を用います。

$$
\begin{aligned}
\langle r \rangle &= \frac{4}{(a^*)^3}\left(\frac{a^*}{2}\right)^4 \int_0^\infty u^3 e^{-u}\,\mathrm{d}u \\
&= \frac{4 a^*}{16}\cdot 6 \\
&= \frac{3}{2}a^* \\
&= \frac{3(m_e + m_h)\varepsilon\hbar^2}{2 m_e m_h e^2}
\end{aligned}
$$

$$
\finalanswer{\langle r \rangle = \frac{3(m_e + m_h)\varepsilon\hbar^2}{2 m_e m_h e^2}}
$$

### (2)(i)

摂動ハミルトニアンを $H' = -\lambda\delta^3(\mathbf{r})$ とおきます。非摂動固有関数 $\psi_{n\ell m}(\mathbf{r})$ に対する行列要素は次の通りです。

$$
\begin{aligned}
\langle n'\ell' m' | H' | n\ell m \rangle &= -\lambda \int \psi_{n'\ell' m'}^*(\mathbf{r})\,\delta^3(\mathbf{r})\,\psi_{n\ell m}(\mathbf{r})\,\mathrm{d}^3r \\
&= -\lambda\,\psi_{n'\ell' m'}^*(\mathbf{0})\psi_{n\ell m}(\mathbf{0})
\end{aligned}
$$

式 (5)〜(7) および $Y_{00} = \dfrac{1}{\sqrt{4\pi}}$ より，原点 $\mathbf{r} = \mathbf{0}$ における各波動関数の値を計算します。

$$
\begin{aligned}
\psi_{100}(\mathbf{0}) &= \frac{2}{\sqrt{a^3}}\cdot\frac{1}{\sqrt{4\pi}} \\
&= \frac{1}{\sqrt{\pi a^3}}
\end{aligned}
$$

$$
\begin{aligned}
\psi_{200}(\mathbf{0}) &= \frac{2}{\sqrt{8a^3}}\cdot\frac{1}{\sqrt{4\pi}} \\
&= \frac{1}{\sqrt{8\pi a^3}}
\end{aligned}
$$

$$
\psi_{21m}(\mathbf{0}) = 0 \qquad (m = -1, 0, +1)
$$

$1s$ 状態は非縮退なので，1次のエネルギー変化 $\Delta E_{1s}^{(1)}$ は対角行列要素で与えられます。

$$
\begin{aligned}
\Delta E_{1s}^{(1)} &= -\lambda |\psi_{100}(\mathbf{0})|^2 \\
&= -\frac{\lambda}{\pi a^3}
\end{aligned}
$$

次に $n = 2$ の $2s$ 状態と $2p$ の3状態を合わせた4状態は非摂動エネルギー $E_2 = -\dfrac{R_y}{4}$ に4重縮退しているため，この4次元部分空間内で $H'$ の行列を対角化する必要があります。しかし $\psi_{21m}(\mathbf{0}) = 0$ であるため，$2p$ 状態を含む行列要素は対角成分も非対角成分もすべて $0$ になります。したがって $H'$ は基底 $\{2s, 2p\}$ においてすでに完全に対角化されており，各状態の1次エネルギー変化は次の通りです。

$$
\begin{aligned}
\Delta E_{2s}^{(1)} &= -\lambda |\psi_{200}(\mathbf{0})|^2 \\
&= -\frac{\lambda}{8\pi a^3} \\
\Delta E_{2p}^{(1)} &= 0
\end{aligned}
$$

よって $\lambda$ の1次の精度での各エネルギー固有値は次のようになります。

$$
\finalanswer{E_{1s} = -R_y - \frac{\lambda}{\pi a^3},\qquad E_{2s} = -\frac{R_y}{4} - \frac{\lambda}{8\pi a^3},\qquad E_{2p} = -\frac{R_y}{4}}
$$

### (2)(ii)

非縮退の1次摂動論により，$1s, 2s, 2p$ 状態のみを考慮した摂動後の $1s$ 状態の波動関数 $\tilde{\psi}_{1s}(\mathbf{r})$ は，$\lambda$ の1次まで次の式で与えられます。

$$
\tilde{\psi}_{1s}(\mathbf{r}) = \psi_{100}(\mathbf{r}) + \frac{\langle 200 | H' | 100 \rangle}{E_1 - E_2}\psi_{200}(\mathbf{r}) + \sum_{m=-1}^{1}\frac{\langle 21m | H' | 100 \rangle}{E_1 - E_2}\psi_{21m}(\mathbf{r})
$$

なお，規格化定数の補正は $O(\lambda^2)$ から現れるため，$\lambda$ の1次の精度では考慮する必要はありません。

ここで $\psi_{21m}(\mathbf{0}) = 0$ より $\langle 21m | H' | 100 \rangle = 0$ であり，$2p$ 状態は $1s$ 状態と混ざりません。$2s$ 状態との行列要素およびエネルギー差を計算します。

$$
\begin{aligned}
\langle 200 | H' | 100 \rangle &= -\lambda\,\psi_{200}^*(\mathbf{0})\psi_{100}(\mathbf{0}) \\
&= -\lambda\cdot\frac{1}{\sqrt{8\pi a^3}}\cdot\frac{1}{\sqrt{\pi a^3}} \\
&= -\frac{\lambda}{2\sqrt{2}\pi a^3}
\end{aligned}
$$

$$
\begin{aligned}
E_1 - E_2 &= -R_y - \left(-\frac{R_y}{4}\right) \\
&= -\frac{3}{4}R_y
\end{aligned}
$$

したがって $2s$ 状態の混合係数 $c_{2s}$ は次のようになります。

$$
\begin{aligned}
c_{2s} &= \frac{-\lambda/(2\sqrt{2}\pi a^3)}{-3R_y/4} \\
&= \frac{\sqrt{2}\lambda}{3\pi a^3 R_y}
\end{aligned}
$$

これより原点 $\mathbf{r} = \mathbf{0}$ における波動関数の値 $\tilde{\psi}_{1s}(\mathbf{0})$ を求めます。

$$
\begin{aligned}
\tilde{\psi}_{1s}(\mathbf{0}) &= \psi_{100}(\mathbf{0}) + c_{2s}\psi_{200}(\mathbf{0}) \\
&= \psi_{100}(\mathbf{0})\left(1 + c_{2s}\frac{\psi_{200}(\mathbf{0})}{\psi_{100}(\mathbf{0})}\right) \\
&= \psi_{100}(\mathbf{0})\left(1 + \frac{\sqrt{2}\lambda}{3\pi a^3 R_y}\cdot\frac{1}{2\sqrt{2}}\right) \\
&= \psi_{100}(\mathbf{0})\left(1 + \frac{\lambda}{6\pi a^3 R_y}\right)
\end{aligned}
$$

両辺の絶対値の2乗をとり，$\lambda$ の1次まで展開します。

$$
\begin{aligned}
\frac{|\tilde{\psi}_{1s}(\mathbf{0})|^2}{|\psi_{100}(\mathbf{0})|^2} &= \left(1 + \frac{\lambda}{6\pi a^3 R_y}\right)^2 \\
&= 1 + \frac{\lambda}{3\pi a^3 R_y} + O(\lambda^2)
\end{aligned}
$$

なお $R_y = \dfrac{e^2}{2a}$ を用いると，$1 + \dfrac{2\lambda}{3\pi a^2 e^2}$ と書くこともできます。

$$
\finalanswer{1 + \frac{\lambda}{3\pi a^3 R_y}}
$$

### (2)(iii)

$\lambda > 0$ より $\dfrac{\lambda}{3\pi a^3 R_y} > 0$ であるため，$r = 0$ における確率密度は $\lambda = 0$ の場合に比べて増加しています。

式 (9) の追加項 $-\lambda\delta^3(\mathbf{r})$ は，$\lambda > 0$ のため原点 $r = 0$ に局在した強い引力ポテンシャルです。電子はポテンシャルエネルギーが低い領域へ引き寄せられるため，原点付近に存在するときのエネルギー得が大きくなり，波動関数が原点側へ引き込まれて $r = 0$ での存在確率密度が増加します。

### (3)(i)

時刻 $t = t_0$ で式 (10) の状態にあるとき，定常状態 $\psi_{100}$ と $\psi_{200}$ はそれぞれ時間因子 $e^{-iE_1(t - t_0)/\hbar}$，$e^{-iE_2(t - t_0)/\hbar}$ を伴って時間発展します。したがって時刻 $t$ における波動関数は次の通りです。

$$
\psi(\mathbf{r}, t) = \frac{1}{\sqrt{2}}\left[\psi_{100}(\mathbf{r})e^{-iE_1(t - t_0)/\hbar} + \psi_{200}(\mathbf{r})e^{-iE_2(t - t_0)/\hbar}\right]
$$

$\psi_{100}(\mathbf{r})$ と $\psi_{200}(\mathbf{r})$ は実関数なので，確率密度 $|\psi(\mathbf{r}, t)|^2$ を展開すると次のようになります。

$$
\begin{aligned}
|\psi(\mathbf{r}, t)|^2 &= \frac{1}{2}|\psi_{100}(\mathbf{r})|^2 + \frac{1}{2}|\psi_{200}(\mathbf{r})|^2 + \frac{1}{2}\psi_{100}(\mathbf{r})\psi_{200}(\mathbf{r})\left[e^{i(E_2 - E_1)(t - t_0)/\hbar} + e^{-i(E_2 - E_1)(t - t_0)/\hbar}\right] \\
&= \frac{1}{2}|\psi_{100}(\mathbf{r})|^2 + \frac{1}{2}|\psi_{200}(\mathbf{r})|^2 + \psi_{100}(\mathbf{r})\psi_{200}(\mathbf{r})\cos\left(\frac{E_2 - E_1}{\hbar}(t - t_0)\right)
\end{aligned}
$$

第3項の干渉項が余弦関数として時間振動するため，$|\psi(\mathbf{r}, t)|^2$ は $t$ の周期関数になります。$E_2 - E_1 = \dfrac{3}{4}R_y$ より，その周期 $T$ は次のように求まります。

$$
\begin{aligned}
T &= \frac{2\pi\hbar}{E_2 - E_1} \\
&= \frac{2\pi\hbar}{3R_y/4} \\
&= \frac{8\pi\hbar}{3R_y}
\end{aligned}
$$

$$
\finalanswer{T = \frac{8\pi\hbar}{3R_y}}
$$

### (3)(ii)

式 (10) の状態は規格直交化された固有状態 $\psi_{100}$ と $\psi_{200}$ をそれぞれ係数 $\dfrac{1}{\sqrt{2}}$ で重ね合わせた状態です。したがって1回の測定で得られるエネルギーの値は $E_1 = -R_y$ と $E_2 = -\dfrac{R_y}{4}$ の2通りであり，それぞれの測定値が得られる確率は係数の絶対値の2乗で与えられます。

- $E_1 = -R_y$ が得られる確率：$\left|\dfrac{1}{\sqrt{2}}\right|^2 = \dfrac{1}{2}$
- $E_2 = -\dfrac{R_y}{4}$ が得られる確率：$\left|\dfrac{1}{\sqrt{2}}\right|^2 = \dfrac{1}{2}$

エネルギーの期待値 $\langle E \rangle$ を計算します。

$$
\begin{aligned}
\langle E \rangle &= \frac{1}{2}E_1 + \frac{1}{2}E_2 \\
&= \frac{1}{2}\left(-R_y - \frac{R_y}{4}\right) \\
&= -\frac{5}{8}R_y
\end{aligned}
$$

$$
\finalanswer{\langle E \rangle = -\frac{5}{8}R_y,\qquad E = -R_y\ \left(P = \frac{1}{2}\right),\quad E = -\frac{R_y}{4}\ \left(P = \frac{1}{2}\right)}
$$

### (3)(iii)

まず1回の測定におけるエネルギーの分散 $\sigma_E^2 = \langle (\varepsilon_i - \langle E \rangle)^2 \rangle$ を計算します。$\varepsilon_i$ は確率 $\dfrac{1}{2}$ ずつで $E_1 = -R_y$ または $E_2 = -\dfrac{R_y}{4}$ をとり，$\langle E \rangle = -\dfrac{5}{8}R_y$ からのずれはそれぞれ $-\dfrac{3}{8}R_y$，$+\dfrac{3}{8}R_y$ です。

$$
\begin{aligned}
\sigma_E^2 &= \frac{1}{2}\left(-\frac{3}{8}R_y\right)^2 + \frac{1}{2}\left(+\frac{3}{8}R_y\right)^2 \\
&= \frac{9}{64}R_y^2
\end{aligned}
$$

各測定は毎回新たに式 (10) の状態を用意して独立に行われるため，$i \neq j$ のとき $\varepsilon_i - \langle E \rangle$ と $\varepsilon_j - \langle E \rangle$ は互いに独立であり，次の関係が成り立ちます。

$$
\langle (\varepsilon_i - \langle E \rangle)(\varepsilon_j - \langle E \rangle) \rangle = \sigma_E^2 \delta_{ij}
$$

これを用いて $\langle \delta^2 \rangle = \langle (\bar{\varepsilon}_N - \langle E \rangle)^2 \rangle$ を展開して計算します。

$$
\begin{aligned}
\langle \delta^2 \rangle &= \left\langle \left(\frac{1}{N}\sum_{i=1}^{N}(\varepsilon_i - \langle E \rangle)\right)^2 \right\rangle \\
&= \frac{1}{N^2}\sum_{i=1}^{N}\sum_{j=1}^{N} \langle (\varepsilon_i - \langle E \rangle)(\varepsilon_j - \langle E \rangle) \rangle \\
&= \frac{1}{N^2}\sum_{i=1}^{N} \sigma_E^2 \\
&= \frac{\sigma_E^2}{N} \\
&= \frac{9R_y^2}{64N}
\end{aligned}
$$

この結果から，$\langle \delta^2 \rangle$ は測定回数 $N$ に反比例するため，測定回数を増やす極限 $N \to \infty$ において

$$
\lim_{N \to \infty}\langle \delta^2 \rangle = \lim_{N \to \infty}\frac{9R_y^2}{64N} = 0
$$

となります。したがって，無限回の測定を繰り返せば実験平均値 $\bar{\varepsilon}_N$ が理論期待値 $\langle E \rangle$ に一致することが確かめられます。

$$
\finalanswer{\langle \delta^2 \rangle = \frac{9R_y^2}{64N}}
$$
