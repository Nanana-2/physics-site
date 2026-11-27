---
title: 東大理物 平成8年度 物理学 第5問：円筒面上の自由電子の状態密度と環状原子鎖のタイトバインディング模型
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
  - 物性物理学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 物理学
exam_number: 第5問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成8年度 物理学 第5問：円筒面上の自由電子の状態密度と環状原子鎖のタイトバインディング模型

## 問題

最近，炭素原子からなる，原子スケールの半径をもつ円筒状の物質（図1，各六角形の頂点が炭素原子を表す）が合成されている。この系での電子状態を調べてみよう。（電子のスピンは無視する。）

先ず，原子構造を無視して，図2のように電子が円筒の面を自由に運動するという模型を考える。これに対して以下の問に答えよ。
{: .problem-lead }

<figure class="problem-figure" markdown>
![円筒面模型および3原子環・N原子環の模式図](../../../docs/assets/figures/pastexam-todai-ributsu/H8_butsuri_5-p-light.svg#only-light){ loading=lazy }
![円筒面模型および3原子環・N原子環の模式図](../../../docs/assets/figures/pastexam-todai-ributsu/H8_butsuri_5-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) 電子に対する Schrödinger 方程式を書き，その固有値および固有関数を求めよ。電子の質量を $m$ とし，円筒（半径 $r$）の軸方向には長さ $L$ の周期的境界条件があるとせよ。

(2) 円筒の代わりに，直線の上を電子が自由運動するとしたときに，状態密度 $D(E)$ を，導き方を示しながら求めよ。（$D(E)$ は $E$ と $E + \mathrm{d}E$ とのエネルギー間隔（$\mathrm{d}E$ は微小）中の状態数が $D(E)\mathrm{d}E$ で与えられるような量である。）長さ $L$ の周期的境界条件があるとしてよい（$L$ は十分大きいとする）。

これを参考にして，円筒上の問題での状態密度を求め，$L \gg r$ のときにその概形を描け。

次に，円筒は原子の連なりであることを取り入れよう。ここでは簡単のために，円筒の円周方向だけについてこの効果を考えよう。即ち，円筒の円周に沿って原子の鎖を切り出し，原子からなる輪を孤立したものとして考える。

(3) この輪が，図3のように3原子から成るとする。各原子に局在した基底波動関数を $\phi_n$（$n$ は原子の番号）として，隣合う原子 $(n, \ell)$ 間を電子が飛び移る過程をハミルトニアン $\mathcal{H}$ の行列要素 $\langle\phi_n|\mathcal{H}|\phi_\ell\rangle = t$ で表すと，基底 $(\phi_1, \phi_2, \phi_3)$ で張られる $\mathcal{H}$ の行列は

$$
\begin{pmatrix}
\varepsilon & t & t \\
t & \varepsilon & t \\
t & t & \varepsilon
\end{pmatrix}
$$

となる。ここで $\varepsilon$ は原子のエネルギー準位，$t < 0$ とする。この固有エネルギーを全て（縮退度も含めて）求めよ。

(4) このような輪が，一般に $N$ 個の原子から成り（図4），$\mathcal{H}$ の行列は同様に最近接の原子間を電子が飛び移るための $t$ を非対角要素にもつ $N \times N$ の行列とする。これを対角化するために，固有関数が

$$
\psi = \sum_{n=1}^{N} c_n \phi_n
$$

という線形結合で表されるとして，その係数が

$$
c_n \propto \exp(i n k a)
$$

という形を解にもつことを示し（$a$ は格子定数），固有エネルギーを求めよ。ここで波数 $k$ のとり得る値を与えよ。

(5) $N$ が大きいときには，長波長つまり小さな $k$ をもつ固有関数が存在する。このとき，エネルギーの $k$ への依存性は，小さな $k$ に対しては（定数項は別として）自由電子のように振る舞うことを示せ。そこでは電子の質量に対応する量はどのように与えられるか。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 物理学 第5問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
カーボンナノチューブの電子構造の出発点となる2つの基本模型を扱う問題です。前半では円筒面上の自由電子を軸方向と円周方向に変数分離することで，円周方向の量子化による1次元サブバンドの重ね合わせとして状態密度にファン・ホーベ特異点が現れることを導きます。後半では周期的境界条件をもつ環状原子鎖のタイトバインディング模型をブロッホ波で対角化し，バンド底付近の2次分散から有効質量を読み取ります。
</div>

### (1)

円筒の軸方向座標を $0 \le z < L$ の $z$，円周方向の角度を $0 \le \theta < 2\pi$ の $\theta$ とします。半径 $r$ の円筒面上の弧長要素は $\mathrm{d}s^2 = \mathrm{d}z^2 + r^2\,\mathrm{d}\theta^2$ なので，2次元ラプラシアンは $\dfrac{\partial^2}{\partial z^2} + \dfrac{1}{r^2}\dfrac{\partial^2}{\partial\theta^2}$ となります。したがって電子に対する定常状態のシュレーディンガー方程式は次式です。

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial z^2} + \frac{1}{r^2}\frac{\partial^2}{\partial\theta^2}\right)\psi(z, \theta) = E\,\psi(z, \theta)
$$

変数分離形 $\psi(z, \theta) = Z(z)\Theta(\theta)$ を代入すると，$z$ と $\theta$ それぞれの平面波解が得られます。

- 軸方向の周期的境界条件 $\psi(z + L, \theta) = \psi(z, \theta)$ より，$Z(z) \propto e^{ikz}$ の波数 $k$ は整数 $n_z \in \mathbb{Z}$ を用いて $k = \dfrac{2\pi n_z}{L}$ と量子化されます。
- 円周方向の一価性 $\psi(z, \theta + 2\pi) = \psi(z, \theta)$ より，$\Theta(\theta) \propto e^{i\ell\theta}$ の角運動量量子数 $\ell$ は整数 $\ell \in \mathbb{Z}$ に限られます。

円筒面の面積は $2\pi r L$ なので，規格化された固有関数 $\psi_{k, \ell}(z, \theta)$ と固有エネルギー $E_{k, \ell}$ は次のようになります。

$$
\finalanswer{\psi_{k, \ell}(z, \theta) = \frac{1}{\sqrt{2\pi r L}} e^{i(kz + \ell\theta)},\qquad E_{k, \ell} = \frac{\hbar^2}{2m}\left(k^2 + \frac{\ell^2}{r^2}\right)}
$$

ここで $n_z = 0, \pm 1, \pm 2, \dots$ に対して $k = \dfrac{2\pi n_z}{L}$ であり，$\ell = 0, \pm 1, \pm 2, \dots$ です。

### (2)

まず直線上の1次元自由電子の状態密度 $D_{1\mathrm{D}}(E)$ を求めます。長さ $L$ の周期的境界条件より波数 $k = \dfrac{2\pi n_z}{L}$ は間隔 $\dfrac{2\pi}{L}$ で均等に分布します。エネルギーは $E = \dfrac{\hbar^2 k^2}{2m}$ であり，スピンを無視すると正負の波数 $\pm |k|$ が同じエネルギーを与えるため，エネルギーが $E$ 以下となる総状態数 $N_{1\mathrm{D}}(E)$ は $E > 0$ に対して次式で与えられます。

$$
\begin{aligned}
N_{1\mathrm{D}}(E) &= \frac{L}{2\pi}\cdot 2\sqrt{\frac{2m E}{\hbar^2}} \\
&= \frac{L}{\pi\hbar}\sqrt{2m E}
\end{aligned}
$$

状態密度 $D_{1\mathrm{D}}(E) = \dfrac{\mathrm{d}N_{1\mathrm{D}}(E)}{\mathrm{d}E}$ を計算すると次式が得られます。

$$
D_{1\mathrm{D}}(E) = \begin{cases} \dfrac{L}{\pi\hbar}\sqrt{\dfrac{m}{2E}} & (E > 0) \\[10pt] 0 & (E \le 0) \end{cases}
$$

次に円筒面上の状態密度 $D_{\mathrm{cyl}}(E)$ を求めます。(1) より固有エネルギーは各整数 $\ell$ でラベルされた1次元サブバンド

$$
E_{k, \ell} = \frac{\hbar^2 k^2}{2m} + E_\ell, \qquad E_\ell = \frac{\hbar^2 \ell^2}{2 m r^2}
$$

の集まりとみなせます。$L \gg r$ のとき軸方向の波数 $k$ は連続変数とみなせる一方，円周方向のサブバンド端 $E_\ell$ は離散的に現れます。各サブバンド $\ell$ はエネルギー原点を $E_\ell$ だけシフトした1次元自由電子系と同じ状態密度 $D_{1\mathrm{D}}(E - E_\ell)$ を与えるため，全体の状態密度はすべての $\ell \in \mathbb{Z}$ にわたる和になります。

$$
D_{\mathrm{cyl}}(E) = \sum_{\ell = -\infty}^{\infty} \frac{L}{\pi\hbar}\sqrt{\frac{m}{2(E - E_\ell)}}\,\Theta(E - E_\ell)
$$

ここで $\Theta(x)$ はヘビサイドの階段関数であり，$\ell = 0$ は非縮退，$\ell = \pm 1, \pm 2, \dots$ は2重に縮退しているため，次のように書き直すこともできます。

$$
D_{\mathrm{cyl}}(E) = \frac{L}{\pi\hbar}\sqrt{\frac{m}{2E}}\,\Theta(E) + 2\sum_{\ell = 1}^{\infty}\frac{L}{\pi\hbar}\sqrt{\frac{m}{2(E - E_\ell)}}\,\Theta(E - E_\ell)
$$

$E_1 = \dfrac{\hbar^2}{2mr^2}$ とおくと，エネルギーが各サブバンド底 $E_\ell = \ell^2 E_1$ へ上から近づくたびに $(E - E_\ell)^{-1/2}$ の発散ピークすなわち1次元のファン・ホーベ特異点が現れます。また高エネルギー極限 $E \gg E_1$ では和を $\ell$ に関する積分で置き換えると，

$$
\begin{aligned}
D_{\mathrm{cyl}}(E) &\approx \int_{-\sqrt{2mE}r/\hbar}^{\sqrt{2mE}r/\hbar} \frac{L}{\pi\hbar}\sqrt{\frac{m}{2(E - \hbar^2\ell^2/2mr^2)}}\,\mathrm{d}\ell \\
&= \frac{m r L}{\hbar^2}
\end{aligned}
$$

となって面積 $S = 2\pi r L$ の2次元自由電子系の一定な状態密度 $\dfrac{m S}{2\pi\hbar^2} = \dfrac{m r L}{\hbar^2}$ のまわりを振動しながら漸近します。$D_{\mathrm{cyl}}(E)$ の概形を図示すると次のようになります。

![円筒面上自由電子の状態密度D(E)の概形と2次元状態密度への漸近](../../../docs/assets/figures/pastexam-todai-ributsu/H8_butsuri_5-s-light.svg#only-light){ loading=lazy }
![円筒面上自由電子の状態密度D(E)の概形と2次元状態密度への漸近](../../../docs/assets/figures/pastexam-todai-ributsu/H8_butsuri_5-s-dark.svg#only-dark){ loading=lazy }

$$
\finalanswer{D_{1\mathrm{D}}(E) = \frac{L}{\pi\hbar}\sqrt{\frac{m}{2E}}\,\Theta(E),\qquad D_{\mathrm{cyl}}(E) = \sum_{\ell = -\infty}^{\infty} \frac{L}{\pi\hbar}\sqrt{\frac{m}{2(E - E_\ell)}}\,\Theta(E - E_\ell)}
$$

### (3)

与えられた $3 \times 3$ 行列 $\mathcal{H}$ の固有方程式 $\det(\mathcal{H} - E I) = 0$ を解きます。

$$
\det(\mathcal{H} - E I) = \begin{vmatrix}
\varepsilon - E & t & t \\
t & \varepsilon - E & t \\
t & t & \varepsilon - E
\end{vmatrix} = 0
$$

第2列と第3列を第1列に加えると，第1列の成分がすべて $\varepsilon + 2t - E$ となります。これをくくり出したのち，第1行を第2行と第3行から引きます。

$$
\begin{aligned}
\det(\mathcal{H} - E I) &= (\varepsilon + 2t - E)\begin{vmatrix}
1 & t & t \\
1 & \varepsilon - E & t \\
1 & t & \varepsilon - E
\end{vmatrix} \\
&= (\varepsilon + 2t - E)\begin{vmatrix}
1 & t & t \\
0 & \varepsilon - t - E & 0 \\
0 & 0 & \varepsilon - t - E
\end{vmatrix} \\
&= (\varepsilon + 2t - E)(\varepsilon - t - E)^2
\end{aligned}
$$

したがって固有エネルギーは $E = \varepsilon + 2t$ が非縮退の縮退度 $1$，$E = \varepsilon - t$ が2重縮退の縮退度 $2$ となります。$t < 0$ なので基底状態のエネルギーは $\varepsilon + 2t$ です。

$$
\finalanswer{E = \varepsilon + 2t,\qquad E = \varepsilon - t}
$$

ここで $E = \varepsilon + 2t$ は非縮退，$E = \varepsilon - t$ は2重縮退です。

### (4)

$N$ 個の原子からなる輪では，周期的境界条件により原子番号 $n$ は法 $N$ で同一視され，$c_0 = c_N$，$c_{N+1} = c_1$ となります。基底 $\{\phi_n\}$ を正規直交基底とみなすと，固有値方程式 $\mathcal{H}\psi = E\psi$ の第 $n$ 成分は次の漸化式になります。

$$
\varepsilon c_n + t(c_{n-1} + c_{n+1}) = E c_n \qquad (n = 1, 2, \dots, N)
$$

ここに $C \neq 0$ の試行解 $c_n = C e^{i n k a}$ を代入します。

$$
\left[\varepsilon + t\left(e^{-ika} + e^{ika}\right)\right] C e^{i n k a} = E C e^{i n k a}
$$

両辺の $C e^{i n k a}$ がすべての $n$ について共通に約分されるため，$c_n \propto \exp(i n k a)$ は固有値方程式の解となり，そのときの固有エネルギー $E(k)$ はオイラーの公式より次式で与えられます。

$$
E(k) = \varepsilon + 2t\cos(ka)
$$

次に波数 $k$ のとり得る値を求めます。輪が一周して元に戻る周期的境界条件 $c_{n + N} = c_n$ を課すと

$$
e^{i N k a} = 1
$$

となるため，整数 $m \in \mathbb{Z}$ を用いて $N k a = 2\pi m$ が必要です。$k$ を $\dfrac{2\pi}{a}$ だけずらしても $e^{i n k a}$ は同じ状態を表すため，独立な $N$ 個の固有状態を与える波数 $k$ はたとえば次のようにとれます。

$$
k = \frac{2\pi m}{N a} \qquad (m = 0, 1, 2, \dots, N - 1)
$$

第1ブリルアンゾーン $-\dfrac{\pi}{a} < k \le \dfrac{\pi}{a}$ にとる場合は $m$ を $-\dfrac{N}{2} < m \le \dfrac{N}{2}$ の範囲の整数とします。なお $N = 3$ のとき $k a = 0, \pm\dfrac{2\pi}{3}$ となり，$E = \varepsilon + 2t$ と2重縮退した $E = \varepsilon - t$ が得られて (3) の結果と一致します。

$$
\finalanswer{E(k) = \varepsilon + 2t\cos(ka),\qquad k = \frac{2\pi m}{N a}\quad (m = 0, 1, \dots, N - 1)}
$$

### (5)

$N$ が十分大きく $|ka| \ll 1$ の長波長極限を考えると，$\cos(ka) = 1 - \dfrac{(ka)^2}{2} + O\bigl((ka)^4\bigr)$ とテイラー展開します。これを (4) の固有エネルギーに代入します。

$$
\begin{aligned}
E(k) &= \varepsilon + 2t\left(1 - \frac{k^2 a^2}{2} + \cdots\right) \\
&\approx (\varepsilon + 2t) + (-t) a^2 k^2
\end{aligned}
$$

ここで $t < 0$ より $-t = |t| > 0$ です。この表式を自由電子の分散関係 $E_{\mathrm{free}}(k) = E_0 + \dfrac{\hbar^2 k^2}{2 m^*}$ と比較すると，定数項 $\varepsilon + 2t$ を除いてエネルギーは波数 $k$ の2乗に比例しており，自由電子と同様に振る舞うことがわかります。

係数を比較すると $\dfrac{\hbar^2}{2 m^*} = -t a^2$ となるため，電子の質量に対応する量すなわち有効質量 $m^*$ は次のように与えられます。

$$
\finalanswer{m^* = -\frac{\hbar^2}{2 t a^2} = \frac{\hbar^2}{2 |t| a^2}}
$$
