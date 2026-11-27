---
title: 東大理物 平成9年度 物理学 第2問：1次元結晶とデルタ関数型不純物ポテンシャルによる電子の束縛
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
  - 物性物理学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成9年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成9年度 物理学 第2問：1次元結晶とデルタ関数型不純物ポテンシャルによる電子の束縛

## 問題

不純物による固体中の電子の束縛問題を考える。簡単のために，格子定数が $a$ の一次元結晶とし，格子点は $x = na;\ n = 0, \pm 1, \pm 2, \dots$ で，不純物は $x = 0$ にあるとする。

完全結晶の場合に，格子点にあるイオンからのポテンシャルを $V_{\mathrm{ion}}(x)$ とし，$x = 0$ にある不純物によるポテンシャル $V_{\mathrm{impurity}}(x)$ は $V_{\mathrm{ion}}(x)$ に $\Delta V(x)$ が加わったものとする。$V_{\mathrm{ion}}(x)$ や $V_{\mathrm{impurity}}(x)$ の概略は下図のようであるが，本問では共にデルタ関数型に簡略化する。
{: .problem-lead }

<figure class="problem-figure" markdown>
![1次元結晶の格子点配置とイオンポテンシャル・不純物ポテンシャルの概略](../../../docs/assets/figures/pastexam-todai-ributsu/H9_butsuri_2-p-light.svg#only-light){ loading=lazy }
![1次元結晶の格子点配置とイオンポテンシャル・不純物ポテンシャルの概略](../../../docs/assets/figures/pastexam-todai-ributsu/H9_butsuri_2-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) まず，$V_{\mathrm{ion}}(x) \equiv 0$，すなわち，1次元の自由運動をする質量 $m$ の電子が $\Delta V(x) = -\dfrac{\hbar^2}{m\lambda_0}\delta(x)$ によって束縛される問題を考える。ここで，$\lambda_0 > 0$ とする。

(i) 束縛エネルギー $E_0$ の電子の波動関数 $\phi_0(x)$ に対するシュレディンガー方程式を書き下せ。

(ii) この方程式にフーリエ変換

$$
\phi_0(x) = \int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi} e^{-ikx}\phi_0(k), \qquad \text{(1)}
$$

を施し，$k$ 空間でのシュレディンガー方程式が次のように書けることを示せ。

$$
\frac{\hbar^2 k^2}{2m}\phi_0(k) - \frac{\hbar^2}{m\lambda_0}\int_{-\infty}^{\infty}\frac{\mathrm{d}k'}{2\pi}\phi_0(k') = E_0\phi_0(k). \qquad \text{(2)}
$$

(iii) $E_0$ を $-\dfrac{\hbar^2\kappa^2}{2m}$ と書くと，$\phi_0(k)$ は

$$
\phi_0(k) = \frac{C_0}{k^2 + \kappa^2}, \qquad \text{(3)}
$$

と書ける。ここで，定数 $C_0$ は

$$
C_0 = \frac{2}{\lambda_0}\int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi}\phi_0(k), \qquad \text{(4)}
$$

である。式 (3) と式 (4) とを組み合わせて $\kappa$ を求めよ。また，$E_0$ を $\lambda_0$ の関数として与えよ。

(iv) $\phi_0(k)$ のフーリエ逆変換 $\phi_0(x)$ を $\lambda_0$ をパラメータとして求めよ。そして，$\phi_0(x)$ の概要を図示し，$\lambda_0$ の物理的な意味を述べよ。なお，波動関数を規格化する必要はない。

(2) 次に，$\Delta V(x) \equiv 0$ の完全一次元結晶を考える。すなわち，$\lambda > 0$ として，

$$
V_{\mathrm{ion}}(x) = -\frac{\hbar^2}{m\lambda}\sum_{n=-\infty}^{\infty}\delta(x - na), \qquad \text{(5)}
$$

の場合に，(1) に倣い，$k$ 空間での電子の波動関数 $\phi(k)$ を使って固有値問題を解こう。

(i) エネルギー $\varepsilon$ の電子の $\phi(k)$ を決めるシュレディンガー方程式は次のようになることを示せ。

$$
\frac{\hbar^2 k^2}{2m}\phi(k) - \frac{\hbar^2}{m\lambda a}\sum_{n=-\infty}^{\infty}\phi\left(k - \frac{2\pi}{a}n\right) = \varepsilon\phi(k). \qquad \text{(6)}
$$

なお，次のポアソンの和公式に注意せよ。

$$
\sum_{n=-\infty}^{\infty} e^{inx} = 2\pi\sum_{n=-\infty}^{\infty}\delta(x - 2\pi n). \qquad \text{(7)}
$$

(ii) $\varepsilon = -\dfrac{\hbar^2\kappa^2}{2m}$ と書くと，$-\dfrac{\pi}{a} < k < \dfrac{\pi}{a}$ を満たす任意の $k$ や整数 $n$ に対して，

$$
\phi\left(k - \frac{2\pi}{a}n\right) = \frac{C_k}{\left(k - \dfrac{2\pi}{a}n\right)^2 + \kappa^2}, \qquad \text{(8)}
$$

と書ける。ここで，$k$ にはよるが，$n$ にはよらない数 $C_k$ は

$$
C_k = \frac{2}{\lambda a}\sum_{n=-\infty}^{\infty}\phi\left(k - \frac{2\pi}{a}n\right), \qquad \text{(9)}
$$

である。これから，$\kappa$ と $k$ とは次の関係で結びつくことを示せ。

$$
\cos(ak) = \cosh(a\kappa) - \frac{1}{\kappa\lambda}\sinh(a\kappa). \qquad \text{(10)}
$$

なお，$u, v > 0$ として，次の公式を使ってもよい。

$$
\sum_{n=-\infty}^{\infty}\frac{v}{(n - u)^2 + v^2} = \pi\frac{\sinh(2\pi v)}{\cosh(2\pi v) - \cos(2\pi u)}. \qquad \text{(11)}
$$

(iii) 式 (10) から，$\lambda \ll a$ の場合，$-\dfrac{\pi}{a} < k < \dfrac{\pi}{a}$ の範囲の任意の $k$ に対して，$\kappa$ は近似的に

$$
\kappa = \frac{1}{\lambda}\left[1 + 2e^{-a/\lambda}\cos(ak)\right], \qquad \text{(12)}
$$

のように与えられることを示せ。

(iv) 式 (12) から，$k$ の関数としてのエネルギーの固有値 $\varepsilon_k$（分散関係）が決められる。$|k| \ll \dfrac{\pi}{a}$ の場合には，それは次の式に示すような自由電子の分散関係に類似した形を持つことを示せ。

$$
\varepsilon_k = \varepsilon_0 + \frac{\hbar^2 k^2}{2m^*}. \qquad \text{(13)}
$$

このとき，$\varepsilon_0$ や電子の有効質量 $m^*$ はどのように与えられるか。

(3) 最後に，$\Delta V(x) \neq 0$ で $V_{\mathrm{ion}}(x) \neq 0$ の場合を考える。これまでのように，$k$ 空間でのシュレディンガー方程式から出発すると，$x = 0$ にある不純物に捕らえられた電子の束縛エネルギー $\bar{E}_0$ が一般的に求められる。しかし，これまでの結果をよく考察すれば，次の2つの極限的な場合には $\bar{E}_0$ の値は予測できる。その予想値を記し，そのように予測した理由を書け。

(i) $\lambda \ll a$，且つ，$\lambda_0 \ll a$ の場合。

(ii) $\lambda \ll a \ll \lambda_0$ の場合。

> 出典：東京大学大学院理学系研究科物理学専攻 平成9年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
デルタ関数ポテンシャルはフーリエ変換すると波数 $k$ に依存しない定数積分に変わるため，$k$ 空間では波動関数が単純な分数式で表され，自己無撞着な代数方程式から固有エネルギーを直接求めることができます。周期配列したデルタ関数列でもポアソンの和公式により逆格子ベクトル $\dfrac{2\pi}{a}n$ だけ離れた波数成分どうしだけが結合し，同じ手続きでエネルギーバンドの分散関係が導かれます。

$\lambda \ll a$ の強束縛極限では隣り合うイオン間の波動関数の重なりが $e^{-a/\lambda}$ に比例して小さくなるため，バンド底付近で有効質量 $m^*$ が定義できます。不純物を加えたときは，束縛状態の広がりと格子定数 $a$ の大小関係に応じて，孤立イオン極限と有効質量近似の2つの描像を使い分けます。
</div>

### (1)(i)

質量 $m$ の1次元電子がポテンシャル $\Delta V(x) = -\dfrac{\hbar^2}{m\lambda_0}\delta(x)$ の中にあるときの時間に依存しないシュレーディンガー方程式は次の通りです。

$$
\finalanswer{-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\phi_0(x)}{\mathrm{d}x^2} - \frac{\hbar^2}{m\lambda_0}\delta(x)\phi_0(x) = E_0\phi_0(x)}
$$

### (1)(ii)

式 (1) の逆変換は $\phi_0(k) = \int_{-\infty}^{\infty} e^{ikx}\phi_0(x)\,\mathrm{d}x$ です。(1)(i) の方程式の両辺に $e^{ikx}$ を掛けて $x$ について $-\infty$ から $+\infty$ まで積分します。

左辺第1項では，束縛状態が $|x| \to \infty$ で $\phi_0(x) \to 0$，$\phi_0'(x) \to 0$ を満たすことを用いて部分積分を2回行います。

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{ikx}\left(-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\phi_0(x)}{\mathrm{d}x^2}\right)\mathrm{d}x &= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty} (ik)^2 e^{ikx}\phi_0(x)\,\mathrm{d}x \\
&= \frac{\hbar^2 k^2}{2m}\phi_0(k)
\end{aligned}
$$

左辺第2項はデルタ関数の性質より $\phi_0(0)$ を取り出し，式 (1) を代入します。

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{ikx}\left(-\frac{\hbar^2}{m\lambda_0}\delta(x)\phi_0(x)\right)\mathrm{d}x &= -\frac{\hbar^2}{m\lambda_0}\phi_0(0) \\
&= -\frac{\hbar^2}{m\lambda_0}\int_{-\infty}^{\infty}\frac{\mathrm{d}k'}{2\pi}\phi_0(k')
\end{aligned}
$$

右辺は $E_0\phi_0(k)$ となるため，以上をまとめると式 (2) が得られます。

$$
\frac{\hbar^2 k^2}{2m}\phi_0(k) - \frac{\hbar^2}{m\lambda_0}\int_{-\infty}^{\infty}\frac{\mathrm{d}k'}{2\pi}\phi_0(k') = E_0\phi_0(k)
$$

### (1)(iii)

$\kappa > 0$ とします。式 (3) を式 (4) に代入して積分を計算します。

$$
\begin{aligned}
C_0 &= \frac{2}{\lambda_0}\int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi}\frac{C_0}{k^2 + \kappa^2} \\
&= \frac{C_0}{\pi\lambda_0}\left[\frac{1}{\kappa}\arctan\left(\frac{k}{\kappa}\right)\right]_{-\infty}^{\infty} \\
&= \frac{C_0}{\pi\lambda_0}\cdot\frac{\pi}{\kappa} \\
&= \frac{C_0}{\kappa\lambda_0}
\end{aligned}
$$

恒等的に $0$ でない波動関数では $C_0 \neq 0$ なので，両辺を $C_0$ で割って $\kappa$ を求めます。

$$
\kappa = \frac{1}{\lambda_0}
$$

これを $E_0 = -\dfrac{\hbar^2\kappa^2}{2m}$ に代入します。

$$
E_0 = -\frac{\hbar^2}{2m\lambda_0^2}
$$

$$
\finalanswer{\kappa = \frac{1}{\lambda_0},\qquad E_0 = -\frac{\hbar^2}{2m\lambda_0^2}}
$$

### (1)(iv)

式 (3) に $\kappa = \dfrac{1}{\lambda_0}$ を代入し，式 (1) によってフーリエ逆変換します。

$$
\phi_0(x) = C_0\int_{-\infty}^{\infty}\frac{\mathrm{d}k}{2\pi}\frac{e^{-ikx}}{k^2 + \kappa^2}
$$

被積分関数は複素 $k$ 平面において $k = \pm i\kappa$ に1位の極をもちます。$x \ge 0$ のときは下半面の半円弧で閉経路を閉じ，$k = -i\kappa$ の留数に $-2\pi i$ を掛けて計算します。

$$
\begin{aligned}
\phi_0(x) &= \frac{C_0}{2\pi}(-2\pi i)\operatorname{Res}_{k = -i\kappa}\frac{e^{-ikx}}{(k - i\kappa)(k + i\kappa)} \\
&= -i C_0 \frac{e^{-\kappa x}}{-2i\kappa} \\
&= \frac{C_0}{2\kappa}e^{-\kappa x}
\end{aligned}
$$

$x < 0$ のときは上半面の半円弧で閉じ，$k = +i\kappa$ の留数に $+2\pi i$ を掛けて同様に $\dfrac{C_0}{2\kappa}e^{\kappa x}$ を得ます。$\kappa = \dfrac{1}{\lambda_0}$ を代入してまとめると次の通りです。

$$
\phi_0(x) = \frac{C_0\lambda_0}{2}\exp\left(-\frac{|x|}{\lambda_0}\right)
$$

$\phi_0(x)$ の概略は次の図のようになります。$x = 0$ で最大値 $\dfrac{C_0\lambda_0}{2}$ と尖った極大をもち，$|x|$ の増加とともに指数関数的に減衰します。

![デルタ関数ポテンシャルによる束縛状態の波動関数phi_0(x)](../../../docs/assets/figures/pastexam-todai-ributsu/H9_butsuri_2-s-light.svg#only-light){ loading=lazy }
![デルタ関数ポテンシャルによる束縛状態の波動関数phi_0(x)](../../../docs/assets/figures/pastexam-todai-ributsu/H9_butsuri_2-s-dark.svg#only-dark){ loading=lazy }

$|x| = \lambda_0$ で波動関数の振幅が原点での値の $\dfrac{1}{e}$ に減少するため，$\lambda_0$ は不純物ポテンシャルに束縛された電子の波動関数の空間的な広がりの尺度，すなわち局在長を表しています。

$$
\finalanswer{\phi_0(x) = \frac{C_0\lambda_0}{2}\exp\left(-\frac{|x|}{\lambda_0}\right)}
$$

### (2)(i)

ポテンシャル $V_{\mathrm{ion}}(x) = -\dfrac{\hbar^2}{m\lambda}\sum_{n=-\infty}^{\infty}\delta(x - na)$ を含むシュレーディンガー方程式の両辺に $e^{ikx}$ を掛けて全実軸で積分します。運動エネルギー項は (1)(ii) と同じく $\dfrac{\hbar^2 k^2}{2m}\phi(k)$ になります。ポテンシャル項に式 (1) と同様のフーリエ表示 $\phi(na) = \int_{-\infty}^{\infty}\dfrac{\mathrm{d}k'}{2\pi} e^{-ik' na}\phi(k')$ を代入して変形します。

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{ikx} V_{\mathrm{ion}}(x)\phi(x)\,\mathrm{d}x &= -\frac{\hbar^2}{m\lambda}\sum_{n=-\infty}^{\infty} e^{ikna}\phi(na) \\
&= -\frac{\hbar^2}{m\lambda}\int_{-\infty}^{\infty}\frac{\mathrm{d}k'}{2\pi}\phi(k')\sum_{n=-\infty}^{\infty} e^{in(k - k')a}
\end{aligned}
$$

ここで式 (7) のポアソンの和公式を $x = (k - k')a$ に用います。$\delta(\alpha u) = \dfrac{1}{|\alpha|}\delta(u)$ を使うと次のようになります。

$$
\begin{aligned}
\sum_{n=-\infty}^{\infty} e^{in(k - k')a} &= 2\pi\sum_{n=-\infty}^{\infty}\delta\bigl((k - k')a - 2\pi n\bigr) \\
&= \frac{2\pi}{a}\sum_{n=-\infty}^{\infty}\delta\left(k' - \left(k - \frac{2\pi}{a}n\right)\right)
\end{aligned}
$$

これを $k'$ 積分に代入すると，$k' = k - \dfrac{2\pi}{a}n$ の値が取り出されます。

$$
\begin{aligned}
\int_{-\infty}^{\infty} e^{ikx} V_{\mathrm{ion}}(x)\phi(x)\,\mathrm{d}x &= -\frac{\hbar^2}{m\lambda a}\sum_{n=-\infty}^{\infty}\phi\left(k - \frac{2\pi}{a}n\right)
\end{aligned}
$$

以上より，式 (6) が導かれます。

$$
\frac{\hbar^2 k^2}{2m}\phi(k) - \frac{\hbar^2}{m\lambda a}\sum_{n=-\infty}^{\infty}\phi\left(k - \frac{2\pi}{a}n\right) = \varepsilon\phi(k)
$$

### (2)(ii)

式 (8) を式 (9) に代入します。

$$
\begin{aligned}
C_k &= \frac{2}{\lambda a}\sum_{n=-\infty}^{\infty}\frac{C_k}{\left(k - \dfrac{2\pi}{a}n\right)^2 + \kappa^2} \\
&= \frac{2 C_k}{\lambda a}\left(\frac{a}{2\pi}\right)^2\sum_{n=-\infty}^{\infty}\frac{1}{\left(n - \dfrac{ak}{2\pi}\right)^2 + \left(\dfrac{a\kappa}{2\pi}\right)^2}
\end{aligned}
$$

$C_k \neq 0$ で両辺を割り，$u = \dfrac{ak}{2\pi}$，$v = \dfrac{a\kappa}{2\pi} > 0$ とおきます。式 (11) は $u \mapsto -u$ と $n \mapsto -n$ の置き換えに対して両辺とも不変なので，すべての実数 $u$ について成り立ちます。式 (11) の両辺を $v$ で割った結果を代入します。

$$
\begin{aligned}
1 &= \frac{a}{2\pi^2\lambda}\cdot\frac{\pi}{v}\frac{\sinh(2\pi v)}{\cosh(2\pi v) - \cos(2\pi u)} \\
&= \frac{a}{2\pi^2\lambda}\cdot\frac{2\pi^2}{a\kappa}\frac{\sinh(a\kappa)}{\cosh(a\kappa) - \cos(ak)} \\
&= \frac{1}{\kappa\lambda}\frac{\sinh(a\kappa)}{\cosh(a\kappa) - \cos(ak)}
\end{aligned}
$$

分母を払って整理すると，式 (10) が得られます。

$$
\cos(ak) = \cosh(a\kappa) - \frac{1}{\kappa\lambda}\sinh(a\kappa)
$$

### (2)(iii)

式 (10) の右辺の双曲線関数を指数関数で書き換えます。

$$
\begin{aligned}
\cos(ak) &= \frac{e^{a\kappa} + e^{-a\kappa}}{2} - \frac{1}{\kappa\lambda}\frac{e^{a\kappa} - e^{-a\kappa}}{2} \\
&= \frac{1}{2}e^{a\kappa}\left(1 - \frac{1}{\kappa\lambda}\right) + \frac{1}{2}e^{-a\kappa}\left(1 + \frac{1}{\kappa\lambda}\right)
\end{aligned}
$$

両辺に $2e^{-a\kappa}$ を掛けて整理します。

$$
1 - \frac{1}{\kappa\lambda} = 2e^{-a\kappa}\cos(ak) - e^{-2a\kappa}\left(1 + \frac{1}{\kappa\lambda}\right)
$$

$\lambda \ll a$ のとき $\kappa \sim \dfrac{1}{\lambda}$ より $a\kappa \gg 1$ であるため，右辺は $O(e^{-a/\lambda})$ の微小量になります。そこで微小量 $|\delta| \ll 1$ を用いて $\kappa = \dfrac{1}{\lambda}(1 + \delta)$ とおくと，左辺は

$$
\begin{aligned}
1 - \frac{1}{1 + \delta} &= \frac{\delta}{1 + \delta} \\
&= \delta + O(\delta^2)
\end{aligned}
$$

となり，右辺は $e^{-a\kappa} = e^{-a/\lambda} + O(e^{-2a/\lambda})$ かつ $e^{-2a\kappa} = O(e^{-2a/\lambda})$ です。したがって $e^{-a/\lambda}$ の1次までを比較すると

$$
\delta \approx 2e^{-a/\lambda}\cos(ak)
$$

となり，式 (12) が得られます。

$$
\kappa = \frac{1}{\lambda}\left[1 + 2e^{-a/\lambda}\cos(ak)\right]
$$

### (2)(iv)

式 (12) を $\varepsilon_k = -\dfrac{\hbar^2\kappa^2}{2m}$ に代入し，$e^{-a/\lambda}$ の1次まで展開します。

$$
\begin{aligned}
\varepsilon_k &= -\frac{\hbar^2}{2m\lambda^2}\left[1 + 2e^{-a/\lambda}\cos(ak)\right]^2 \\
&\approx -\frac{\hbar^2}{2m\lambda^2}\left[1 + 4e^{-a/\lambda}\cos(ak)\right]
\end{aligned}
$$

$|k| \ll \dfrac{\pi}{a}$ より $|ak| \ll 1$ なので，$\cos(ak) \approx 1 - \dfrac{1}{2}a^2 k^2$ を代入します。

$$
\begin{aligned}
\varepsilon_k &\approx -\frac{\hbar^2}{2m\lambda^2}\left[1 + 4e^{-a/\lambda}\left(1 - \frac{1}{2}a^2 k^2\right)\right] \\
&= -\frac{\hbar^2}{2m\lambda^2}\left(1 + 4e^{-a/\lambda}\right) + \frac{\hbar^2 a^2 e^{-a/\lambda}}{m\lambda^2}k^2
\end{aligned}
$$

式 (13) の $\varepsilon_k = \varepsilon_0 + \dfrac{\hbar^2 k^2}{2m^*}$ と比較すると，$\varepsilon_0$ と有効質量 $m^*$ が次のように定まります。

$$
\begin{aligned}
\varepsilon_0 &= -\frac{\hbar^2}{2m\lambda^2}\left(1 + 4e^{-a/\lambda}\right) \\
\frac{1}{2m^*} &= \frac{a^2 e^{-a/\lambda}}{m\lambda^2}
\end{aligned}
$$

第2式を $m^*$ について解きます。

$$
m^* = \frac{m\lambda^2}{2a^2}e^{a/\lambda}
$$

$$
\finalanswer{\varepsilon_0 = -\frac{\hbar^2}{2m\lambda^2}\left(1 + 4e^{-a/\lambda}\right),\qquad m^* = \frac{m\lambda^2}{2a^2}e^{a/\lambda}}
$$

### (3)(i)

$x = 0$ における全ポテンシャルはイオンポテンシャルと不純物ポテンシャルの和

$$
\begin{aligned}
V_{\mathrm{impurity}}(x) &= -\frac{\hbar^2}{m\lambda}\delta(x) - \frac{\hbar^2}{m\lambda_0}\delta(x) \\
&= -\frac{\hbar^2}{m}\left(\frac{1}{\lambda} + \frac{1}{\lambda_0}\right)\delta(x)
\end{aligned}
$$

です。ここで有効な長さパラメータ $\lambda_{\mathrm{eff}}$ を $\dfrac{1}{\lambda_{\mathrm{eff}}} = \dfrac{1}{\lambda} + \dfrac{1}{\lambda_0}$ とおくと，$\lambda \ll a$ かつ $\lambda_0 \ll a$ より $\lambda_{\mathrm{eff}} < \min(\lambda, \lambda_0) \ll a$ が成り立ちます。

したがって (1)(iv) より，$x = 0$ に束縛された電子の波動関数の広がり $\lambda_{\mathrm{eff}}$ は格子定数 $a$ に比べて十分に小さく，隣り合う格子点 $x = \pm a, \pm 2a, \dots$ にあるイオンポテンシャルの影響は指数関数的に小さく無視することができます。よって電子は $x = 0$ の孤立した単一のデルタ関数ポテンシャルに束縛されているとみなすことができ，(1)(iii) の結果で $\dfrac{1}{\lambda_0}$ を $\dfrac{1}{\lambda} + \dfrac{1}{\lambda_0}$ に置き換えることで $\bar{E}_0$ が予測されます。

$$
\finalanswer{\bar{E}_0 = -\frac{\hbar^2}{2m}\left(\frac{1}{\lambda} + \frac{1}{\lambda_0}\right)^2}
$$

### (3)(ii)

$\lambda \ll a$ のもとでは，完全結晶中の電子の最低エネルギーバンドの底付近の運動は (2)(iv) の分散関係 $\varepsilon_k = \varepsilon_0 + \dfrac{\hbar^2 k^2}{2m^*}$ に従い，底のエネルギーを基準にすれば質量 $m^*$ の自由電子のように振る舞います。

一方 $a \ll \lambda_0$ のときは不純物ポテンシャル $\Delta V(x) = -\dfrac{\hbar^2}{m\lambda_0}\delta(x)$ が弱いため，不純物に束縛された電子の波動関数は多くの格子定数 $a$ にわたって広がります。そこで有効質量近似を用い，(1) の自由電子の運動エネルギーの質量 $m$ を結晶中の有効質量 $m^*$ に置き換えた有効シュレーディンガー方程式を考えます。

$$
-\frac{\hbar^2}{2m^*}\frac{\mathrm{d}^2 F(x)}{\mathrm{d}x^2} - \frac{\hbar^2}{m\lambda_0}\delta(x) F(x) = (\bar{E}_0 - \varepsilon_0)F(x)
$$

ここで $-\dfrac{\hbar^2}{m\lambda_0} = -\dfrac{\hbar^2}{m^*\lambda_0^*}$ と書き直すと，有効な長さパラメータは $\lambda_0^* = \dfrac{m}{m^*}\lambda_0$ となります。(1)(iii) の結果を用いると，バンド底 $\varepsilon_0$ からの束縛エネルギーは $-\dfrac{\hbar^2}{2m^*(\lambda_0^*)^2}$ となるため，エネルギー固有値 $\bar{E}_0$ は次のように予測されます。

$$
\begin{aligned}
\bar{E}_0 &= \varepsilon_0 - \frac{\hbar^2}{2m^*(\lambda_0^*)^2} \\
&= \varepsilon_0 - \frac{m^*}{m}\cdot\frac{\hbar^2}{2m\lambda_0^2} \\
&= -\frac{\hbar^2}{2m\lambda^2}\left(1 + 4e^{-a/\lambda}\right) - \frac{\hbar^2\lambda^2 e^{a/\lambda}}{4m a^2 \lambda_0^2}
\end{aligned}
$$

$$
\finalanswer{\bar{E}_0 = \varepsilon_0 - \frac{m^*}{m}\cdot\frac{\hbar^2}{2m\lambda_0^2} = -\frac{\hbar^2}{2m\lambda^2}\left(1 + 4e^{-a/\lambda}\right) - \frac{\hbar^2\lambda^2 e^{a/\lambda}}{4m a^2 \lambda_0^2}}
$$

<aside class="rigor-note" markdown>
(3)(ii) で用いた有効質量近似は本来，格子定数 $a$ に比べて緩やかに変化する不純物ポテンシャルに対する近似であり，かつ不純物準位の束縛エネルギーがバンド幅 $\dfrac{4\hbar^2}{m\lambda^2}e^{-a/\lambda}$ に比べて小さい条件 $\lambda_0 \gg \lambda e^{a/\lambda}$ を必要とします。デルタ関数 $\Delta V(x) = -\dfrac{\hbar^2}{m\lambda_0}\delta(x)$ を $x = 0$ の格子点上で厳密に解くと，$\cosh(qa) = \cosh(\kappa a) - \dfrac{\sinh(\kappa a)}{\kappa\lambda}$ のもとで束縛条件は $\kappa\dfrac{\sinh(qa)}{\sinh(\kappa a)} = \dfrac{1}{\lambda_0}$ となります。$\lambda_0 \gg \lambda e^{a/\lambda}$ の極限ではブロッホ関数が $x = 0$ のイオン位置に集中している効果で行列要素が $\dfrac{a}{\lambda}$ 倍になるため，厳密解のバンド底からのずれは $-\dfrac{\hbar^2 e^{a/\lambda}}{4m\lambda_0^2}$ と上の有効質量近似より $\left(\dfrac{a}{\lambda}\right)^2$ 倍大きくなります。逆に $a \ll \lambda_0 \ll \lambda e^{a/\lambda}$ では不純物ポテンシャルがバンド幅より大きくなるため，(3)(i) と同じく $\bar{E}_0 \simeq -\dfrac{\hbar^2}{2m}\left(\dfrac{1}{\lambda} + \dfrac{1}{\lambda_0}\right)^2$ に近づきます。
</aside>
