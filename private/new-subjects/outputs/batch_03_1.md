===== FILE: 06solid_state/05/05_045.md =====
---
tags:
  - 標準
---

# 非調和性とグリュナイゼン定数

## 問題
質量 $M$ の原子 $N$ 個が一直線に並んだ鎖を考え，周期境界条件を課す。隣り合う原子の間だけに対ポテンシャル $\varphi(r)$ がはたらく。$r$ は原子間の距離で，$\varphi$ は $r=a$ で極小をもつ。鎖を一様に伸ばして原子の間隔を $r$ にしたとき，そのまわりの微小振動の角振動数は

$$
\omega_k=2\sqrt{\frac{\varphi''(r)}{M}}\,\left|\sin\frac{kr}{2}\right|
$$

である。波数は $k=2\pi j/(Nr)$ で，$j$ は整数である。鎖の長さを $L=Nr$ とし，各モードのグリュナイゼン定数を

$$
\gamma_k=-\frac{\mathrm{d}\ln\omega_k}{\mathrm{d}\ln L}
$$

で定義する。温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$ とする。以下の問いに答えよ。

(1) $r=a$ での $\gamma_k$ を，$a$，$\varphi''(a)$，$\varphi'''(a)$ で表せ。

(2) 対ポテンシャルが次の形のとき，$\gamma_k$ の値を求めよ。$\epsilon>0$，$\sigma>0$ は定数である。

$$
\varphi(r)=4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right]
$$

(3) 1つの結合を独立な振動子とみなし，結合の長さを $a+x$ とする。ポテンシャルエネルギー $V(x)=\varphi(a+x)-\varphi(a)$ を $x$ の3次まで展開し，古典統計で $x$ の平均 $\langle x\rangle$ を $\varphi'''(a)$ の1次まで求めよ。必要なら，$\lambda>0$ に対する次の積分を用いてよい。

$$
\begin{aligned}
\int_{-\infty}^{\infty}e^{-\lambda x^2}\,\mathrm{d}x&=\sqrt{\frac{\pi}{\lambda}}\\
\int_{-\infty}^{\infty}x^4e^{-\lambda x^2}\,\mathrm{d}x&=\frac{3}{4\lambda^2}\sqrt{\frac{\pi}{\lambda}}
\end{aligned}
$$

---

## 解答・解説

### (1)
周期境界条件のもとで鎖を伸ばしても，各モードの整数 $j$ は変わりません。そのため $kr=2\pi j/N$ は一定で，$\sin$ の因子は $r$ によりません。$\omega_k$ の $r$ 依存性は $\sqrt{\varphi''(r)}$ だけから生じます。また $L=Nr$ なので $\mathrm{d}\ln L=\mathrm{d}\ln r$ です。対数をとって $\ln r$ で微分すると，

$$
\begin{aligned}
\ln\omega_k&=\frac{1}{2}\ln\varphi''(r)+C_k\\
\frac{\mathrm{d}\ln\omega_k}{\mathrm{d}\ln r}&=\frac{r}{2}\cdot\frac{\varphi'''(r)}{\varphi''(r)}
\end{aligned}
$$

となります。$C_k$ は $r$ によらない定数です。$r=a$ とおいて符号を変えると，

$$
\finalanswer{\gamma_k=-\frac{a\,\varphi'''(a)}{2\varphi''(a)}}
$$

となります。この $\gamma_k$ は $k$ によらず，すべてのモードで同じ値です。調和近似では $\varphi'''=0$ なので $\gamma_k=0$ となり，振動数は長さによりません。グリュナイゼン定数は3次の非調和性の大きさを表しています。ふつうは $\varphi'''(a)<0$ なので $\gamma_k>0$ で，鎖が伸びるとばねが弱くなり，振動数が下がります。

### (2)
はじめに平衡の間隔を求めます。1階の導関数は次のとおりです。

$$
\varphi'(r)=4\epsilon\left(-\frac{12\sigma^{12}}{r^{13}}+\frac{6\sigma^{6}}{r^{7}}\right)
$$

$\varphi'(a)=0$ とおくと，$(\sigma/a)^6=1/2$ が得られます。続いて2階と3階の導関数を計算します。

$$
\begin{aligned}
\varphi''(r)&=4\epsilon\left(\frac{156\sigma^{12}}{r^{14}}-\frac{42\sigma^{6}}{r^{8}}\right)\\
\varphi'''(r)&=4\epsilon\left(-\frac{2184\sigma^{12}}{r^{15}}+\frac{336\sigma^{6}}{r^{9}}\right)
\end{aligned}
$$

$r=a$ とおき，$(\sigma/a)^6=1/2$ と $(\sigma/a)^{12}=1/4$ を代入すると，

$$
\begin{aligned}
a^2\varphi''(a)&=4\epsilon\left(39-21\right)=72\epsilon\\
a^3\varphi'''(a)&=4\epsilon\left(-546+168\right)=-1512\epsilon
\end{aligned}
$$

となります。これらを (1) の結果に代入します。

$$
\begin{aligned}
\gamma_k&=-\frac{a^3\varphi'''(a)}{2a^2\varphi''(a)}\\
&=\frac{1512}{144}
\end{aligned}
$$

したがって，

$$
\finalanswer{\gamma_k=\frac{21}{2}}
$$

となります。この値は $\epsilon$ にも $\sigma$ にもよりません。反発の項のべきが大きいほど，つまり反発が急に立ち上がるほど，ポテンシャルの左右の非対称性が強くなり，$\gamma_k$ は大きくなります。

### (3)
$K=\varphi''(a)$，$c=\varphi'''(a)$ とおいて $V(x)$ を展開します。$\varphi'(a)=0$ なので1次の項はありません。

$$
V(x)=\frac{K}{2}x^2+\frac{c}{6}x^3
$$

ポテンシャルの形を図に示します。

<!-- FIGURE solution (3): 横軸 x，縦軸 V，原点 O。調和近似 V = Kx²/2 を，左右対称な放物線として破線で描く。3次の項を含む V(x) = Kx²/2 + cx³/6（c < 0）を実線で描く。実線は x > 0 の側で破線より低くゆるやかに，x < 0 の側で破線より高く急になるようにする。原点より少し上に水平な線を1本引き，「k_B T 程度のエネルギー」と注記する。その線と実線の2つの交点の中点に黒丸を置き，中点が x > 0 の側にずれていることを縦の点線で示す。 -->

平均は，ボルツマン因子で重みをつけた積分の比で求めます。$\beta=1/k_{\mathrm{B}}T$ とおき，3次の項が小さいとして $e^{-\beta cx^3/6}\approx1-\beta cx^3/6$ と展開します。奇関数の積分は0になるので，分母には3次の項が残りません。

$$
\begin{aligned}
\langle x\rangle&=\frac{\int x\,e^{-\beta V}\,\mathrm{d}x}{\int e^{-\beta V}\,\mathrm{d}x}\\
&\approx\frac{\int x\left(1-\beta cx^3/6\right)e^{-\beta Kx^2/2}\,\mathrm{d}x}{\int e^{-\beta Kx^2/2}\,\mathrm{d}x}\\
&=-\frac{\beta c}{6}\cdot\frac{\int x^4e^{-\beta Kx^2/2}\,\mathrm{d}x}{\int e^{-\beta Kx^2/2}\,\mathrm{d}x}
\end{aligned}
$$

与えられた積分で $\lambda=\beta K/2$ とおくと，積分の比は $3/(4\lambda^2)=3/(\beta K)^2$ です。これを代入すると，

$$
\begin{aligned}
\langle x\rangle&=-\frac{\beta c}{6}\cdot\frac{3}{\beta^2K^2}\\
&=-\frac{c\,k_{\mathrm{B}}T}{2K^2}
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{\langle x\rangle=-\frac{\varphi'''(a)}{2\varphi''(a)^2}\,k_{\mathrm{B}}T}
$$

となります。調和の項だけなら $V$ は左右対称なので $\langle x\rangle=0$ で，熱膨張は起こりません。$\varphi'''(a)<0$ のときは伸びる側でポテンシャルがゆるやかになるので，原子間の平均距離は温度に比例して伸びます。(1) の結果を使うと，線膨張率は次のように書けます。

$$
\frac{1}{a}\cdot\frac{\mathrm{d}\langle x\rangle}{\mathrm{d}T}=\frac{\gamma_kk_{\mathrm{B}}}{a^2\varphi''(a)}
$$

膨張率はグリュナイゼン定数に比例します。熱膨張と，振動数が長さに依存することは，どちらも同じ3次の非調和性から生じています。

===== FILE: 06solid_state/05/05_055.md =====
---
tags:
  - 発展
---

# 低温の熱伝導とウムクラップ過程

## 問題
格子定数 $a$ の一次元の結晶で，フォノンの波数 $k$ を第1ブリルアンゾーン $-\pi/a<k\le\pi/a$ にとる。分散関係を $\omega=v|k|$ で近似し，デバイ温度 $\Theta_{\mathrm{D}}$ を $k_{\mathrm{B}}\Theta_{\mathrm{D}}=\hbar v\pi/a$ で定義する。$v>0$ は音速，$k_{\mathrm{B}}$ はボルツマン定数である。波数 $k_1,k_2$ の2つのフォノンが合体して波数 $k_3$ のフォノンになる過程では，

$$
k_1+k_2=k_3+G
$$

が成り立つ。$k_3$ もゾーンの中にとり，$G$ は逆格子ベクトル $2\pi n/a$ で，$n$ は整数である。$G=0$ の過程を正常過程，$G\ne0$ の過程をウムクラップ過程とよぶ。ここではエネルギーの保存は考えず，波数の条件だけを扱う。以下の問いに答えよ。

(1) $0<k_1\le\pi/a$，$0<k_2\le\pi/a$ のとき，ウムクラップ過程になる $k_1,k_2$ の条件を求めよ。

(2) (1) の条件のもとで，$k_1,k_2$ のうち大きいほうのフォノンのエネルギーの下限 $\varepsilon_{\min}$ を $\Theta_{\mathrm{D}}$ で表せ。

(3) 温度 $T\ll\Theta_{\mathrm{D}}$ で，ウムクラップ過程の起こる頻度が，エネルギー $\varepsilon_{\min}$ のフォノンの平均占有数に比例するとする。ウムクラップ過程で決まるフォノンの平均自由行程 $\ell_{\mathrm{U}}$ の温度依存性を求めよ。

---

## 解答・解説

### (1)
$k_1,k_2>0$ なので，和は $0<k_1+k_2\le2\pi/a$ の範囲にあります。$k_1+k_2\le\pi/a$ なら $k_3=k_1+k_2$ がゾーンの中にあるので，$G=0$ の正常過程になります。$k_1+k_2>\pi/a$ のときは和がゾーンの外に出るため，$G=2\pi/a$ を引いてゾーンの中に戻す必要があります。

$$
k_3=k_1+k_2-\frac{2\pi}{a}
$$

この $k_3$ は $-\pi/a<k_3\le0$ の範囲にあります。したがって，ウムクラップ過程になる条件は

$$
\finalanswer{k_1+k_2>\frac{\pi}{a}}
$$

となります。2つのフォノンの合体を図に示します。

<!-- FIGURE solution (1): 横軸 k，縦軸 ω，原点 O。−π/a から π/a まで V 字形の分散 ω = v|k| を実線で描き，k = ±π/a に縦の破線を引いてゾーンの境界を示す。k 軸の上に，O から k1（約 0.6π/a）までの矢印と，その先から k1 + k2（約 1.3π/a，ゾーンの外）までの矢印をつないで描く。ゾーンの外の点から左向きに長さ 2π/a の矢印を描いて「−G」とラベルし，その先の点（約 −0.7π/a）に黒丸を置いて k3 とラベルする。 -->

$k_1,k_2$ は正の向きに進むフォノンですが，できたフォノンは $k_3\le0$ なので負の向きに進みます。正常過程では波数の総和が保たれるので，熱の流れを運ぶフォノンの分布は崩れません。熱の流れの向きを変えて熱抵抗を生むのは，ウムクラップ過程です。

### (2)
$k_1$ と $k_2$ の大きいほうは，2つの平均以上です。(1) の条件を使うと，

$$
\begin{aligned}
\max(k_1,k_2)&\ge\frac{k_1+k_2}{2}\\
&>\frac{\pi}{2a}
\end{aligned}
$$

となります。このフォノンのエネルギーは $\hbar v\max(k_1,k_2)$ です。下限は $\hbar v\pi/(2a)$ で，これを $\Theta_{\mathrm{D}}$ の定義で書き直すと，

$$
\finalanswer{\varepsilon_{\min}=\frac{k_{\mathrm{B}}\Theta_{\mathrm{D}}}{2}}
$$

となります。この下限には，$k_1$ と $k_2$ がどちらも $\pi/(2a)$ に近い場合に近づきます。ウムクラップ過程が起こるには，ゾーンの中ほどより外側の，エネルギーの高いフォノンが必要です。

### (3)
フォノンは化学ポテンシャル0のボース分布に従います。$T\ll\Theta_{\mathrm{D}}$ では指数関数が1より十分大きいので，平均占有数は次のように近似できます。

$$
\begin{aligned}
\bar{n}(\varepsilon_{\min})&=\frac{1}{e^{\varepsilon_{\min}/k_{\mathrm{B}}T}-1}\\
&=\frac{1}{e^{\Theta_{\mathrm{D}}/2T}-1}\\
&\approx e^{-\Theta_{\mathrm{D}}/2T}
\end{aligned}
$$

ウムクラップ過程の頻度を $1/\tau_{\mathrm{U}}$ とすると，$1/\tau_{\mathrm{U}}\propto\bar{n}$ です。熱を運ぶフォノンは速さ $v$ で進むので，平均自由行程は $\ell_{\mathrm{U}}=v\tau_{\mathrm{U}}$ です。したがって，

$$
\finalanswer{\ell_{\mathrm{U}}\propto e^{\Theta_{\mathrm{D}}/2T}}
$$

となります。温度を下げると $\ell_{\mathrm{U}}$ は指数関数的に伸び，熱伝導率も急に大きくなります。$\ell_{\mathrm{U}}$ が試料の大きさに達すると，それより先は試料の境界での散乱で平均自由行程が決まります。そのため熱伝導率は，境界散乱による $T^3$ の増加とウムクラップ過程による指数関数的な減少の間で極大をとります。

===== FILE: 06solid_state/06/06_015.md =====
---
tags:
  - 基本
---

# 自由電子気体の圧力と体積弾性率

## 問題
体積 $V$ の箱の中にある $N$ 個の自由電子の気体を，絶対零度で考える。電子の質量を $m$，数密度を $n=N/V$ とし，周期境界条件を課す。スピンを含めると，波数の大きさが $k$ と $k+\mathrm{d}k$ の間にある状態の数は $Vk^2\,\mathrm{d}k/\pi^2$ である。フェルミ波数を $k_{\mathrm{F}}$，フェルミエネルギーを $E_{\mathrm{F}}=\hbar^2k_{\mathrm{F}}^{\,2}/2m$ とする。以下の問いに答えよ。

(1) 基底状態の全エネルギー $E_0$ を $N$ と $E_{\mathrm{F}}$ で表せ。

(2) $N$ を一定に保ったときの圧力 $p=-(\partial E_0/\partial V)_N$ を $n$ と $E_{\mathrm{F}}$ で表せ。

(3) $N$ を一定に保ったときの体積弾性率 $B=-V(\partial p/\partial V)_N$ を $n$ と $E_{\mathrm{F}}$ で表せ。

---

## 解答・解説

### (1)
基底状態では，電子は $k\le k_{\mathrm{F}}$ の状態をすべて占めます。まず，状態の数を $k_{\mathrm{F}}$ まで積分して $N$ と $k_{\mathrm{F}}$ を結びつけます。

$$
\begin{aligned}
N&=\int_0^{k_{\mathrm{F}}}\frac{Vk^2}{\pi^2}\,\mathrm{d}k\\
&=\frac{Vk_{\mathrm{F}}^{\,3}}{3\pi^2}
\end{aligned}
$$

全エネルギーは，各状態のエネルギー $\hbar^2k^2/2m$ に状態の数をかけて積分したものです。

$$
\begin{aligned}
E_0&=\int_0^{k_{\mathrm{F}}}\frac{\hbar^2k^2}{2m}\cdot\frac{Vk^2}{\pi^2}\,\mathrm{d}k\\
&=\frac{V\hbar^2k_{\mathrm{F}}^{\,5}}{10\pi^2m}
\end{aligned}
$$

2つの式の比をとり，$E_{\mathrm{F}}$ で書き直します。

$$
\begin{aligned}
\frac{E_0}{N}&=\frac{3}{10}\cdot\frac{\hbar^2k_{\mathrm{F}}^{\,2}}{m}\\
&=\frac{3}{5}E_{\mathrm{F}}
\end{aligned}
$$

したがって，

$$
\finalanswer{E_0=\frac{3}{5}NE_{\mathrm{F}}}
$$

となります。$k$ が大きいほど状態が多いので，電子1個あたりの平均エネルギーは $E_{\mathrm{F}}/2$ より大きく，$3E_{\mathrm{F}}/5$ になります。

### (2)
$N$ を一定にして体積を変えると，フェルミ波数が変わります。(1) の $N$ の式から $k_{\mathrm{F}}=(3\pi^2N/V)^{1/3}$ なので，$E_{\mathrm{F}}$ は $V^{-2/3}$ に比例します。

$$
\begin{aligned}
E_{\mathrm{F}}&=\frac{\hbar^2}{2m}\left(\frac{3\pi^2N}{V}\right)^{2/3}\\
\left(\frac{\partial E_{\mathrm{F}}}{\partial V}\right)_N&=-\frac{2}{3}\cdot\frac{E_{\mathrm{F}}}{V}
\end{aligned}
$$

(1) の $E_0$ を $V$ で微分し，この結果を代入します。

$$
\begin{aligned}
p&=-\frac{3}{5}N\left(\frac{\partial E_{\mathrm{F}}}{\partial V}\right)_N\\
&=\frac{2}{5}\cdot\frac{NE_{\mathrm{F}}}{V}
\end{aligned}
$$

したがって，

$$
\finalanswer{p=\frac{2}{5}nE_{\mathrm{F}}}
$$

となります。これは $p=2E_0/(3V)$ とも書け，理想気体の圧力と運動エネルギーの関係と同じ形です。絶対零度でも圧力が0にならないのは，パウリの排他原理のために電子が大きな運動量の状態まで詰まっているからです。金属では，この圧力とイオンからの引力が釣り合っています。

### (3)
(2) の結果は $p=2NE_{\mathrm{F}}/(5V)$ で，$E_{\mathrm{F}}\propto V^{-2/3}$ なので $p$ は $V^{-5/3}$ に比例します。これを $V$ で微分します。

$$
\begin{aligned}
\left(\frac{\partial p}{\partial V}\right)_N&=-\frac{5}{3}\cdot\frac{p}{V}\\
B&=\frac{5}{3}p
\end{aligned}
$$

(2) の $p$ を代入すると，

$$
\finalanswer{B=\frac{2}{3}nE_{\mathrm{F}}}
$$

となります。体積弾性率は電子密度とフェルミエネルギーだけで決まり，$n^{5/3}$ に比例します。電子密度の小さいアルカリ金属では，この値が実測の体積弾性率と同じ程度の大きさになります。

===== FILE: 06solid_state/08/08_035.md =====
---
tags:
  - 標準
---

# n 型半導体の化学ポテンシャルの温度変化

## 問題
密度 $N_{\mathrm{D}}$ のドナーを含み，アクセプターを含まない n 型半導体を考える。伝導帯の底を $E_{\mathrm{c}}$，ドナー準位を $E_{\mathrm{D}}=E_{\mathrm{c}}-E_{\mathrm{d}}$ とし，$E_{\mathrm{d}}>0$ である。化学ポテンシャルを $\mu$，温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$ とすると，伝導帯の電子密度は $n=N_{\mathrm{c}}e^{-(E_{\mathrm{c}}-\mu)/k_{\mathrm{B}}T}$ と書ける。$N_{\mathrm{c}}$ は $T^{3/2}$ に比例する。正孔を無視すると，電気的中性の条件から

$$
\begin{aligned}
n&=\frac{n_1}{2}\left(\sqrt{1+\frac{4N_{\mathrm{D}}}{n_1}}-1\right)\\
n_1&=\frac{N_{\mathrm{c}}}{2}e^{-E_{\mathrm{d}}/k_{\mathrm{B}}T}
\end{aligned}
$$

となる。以下の問いに答えよ。

(1) $n_1\ll N_{\mathrm{D}}$ となる低温での $\mu$ を求めよ。

(2) $n_1\gg N_{\mathrm{D}}$ となる温度での $\mu$ を求めよ。

(3) さらに高温で，ドナーはすべて電離しており，価電子帯の正孔の密度 $p$ も考える必要があるとする。$np=n_{\mathrm{i}}^{\,2}$ と $n=p+N_{\mathrm{D}}$ が成り立つ。$n_{\mathrm{i}}$ は真性キャリア密度で，真性の化学ポテンシャル $\mu_{\mathrm{i}}$ を $n_{\mathrm{i}}=N_{\mathrm{c}}e^{-(E_{\mathrm{c}}-\mu_{\mathrm{i}})/k_{\mathrm{B}}T}$ で定義する。$\mu-\mu_{\mathrm{i}}$ を $N_{\mathrm{D}}$，$n_{\mathrm{i}}$，$k_{\mathrm{B}}T$ で表せ。

---

##解答・解説

### (1)
電子密度の式を $\mu$ について解いておくと，どの温度でも使えます。

$$
\mu=E_{\mathrm{c}}-k_{\mathrm{B}}T\ln\frac{N_{\mathrm{c}}}{n}
$$

$n_1\ll N_{\mathrm{D}}$ では根号の中の1を無視できます。

$$
\begin{aligned}
n&\approx\frac{n_1}{2}\sqrt{\frac{4N_{\mathrm{D}}}{n_1}}\\
&=\sqrt{n_1N_{\mathrm{D}}}\\
&=\sqrt{\frac{N_{\mathrm{c}}N_{\mathrm{D}}}{2}}\,e^{-E_{\mathrm{d}}/2k_{\mathrm{B}}T}
\end{aligned}
$$

これを使って対数の部分を計算します。

$$
\ln\frac{N_{\mathrm{c}}}{n}=\frac{1}{2}\ln\frac{2N_{\mathrm{c}}}{N_{\mathrm{D}}}+\frac{E_{\mathrm{d}}}{2k_{\mathrm{B}}T}
$$

$\mu$ の式に代入し，$E_{\mathrm{c}}-E_{\mathrm{d}}/2=(E_{\mathrm{c}}+E_{\mathrm{D}})/2$ を使うと，

$$
\finalanswer{\mu=\frac{E_{\mathrm{c}}+E_{\mathrm{D}}}{2}-\frac{k_{\mathrm{B}}T}{2}\ln\frac{2N_{\mathrm{c}}}{N_{\mathrm{D}}}}
$$

となります。$N_{\mathrm{c}}\propto T^{3/2}$ なので，$T\to0$ で $T\ln N_{\mathrm{c}}\to0$ となります。

$$
\lim_{T\to0}\mu=\frac{E_{\mathrm{c}}+E_{\mathrm{D}}}{2}
$$

低温では，ドナー準位はほぼ電子で埋まり，伝導帯はほぼ空です。化学ポテンシャルはその間の中央に近づきます。ごく低温では $2N_{\mathrm{c}}<N_{\mathrm{D}}$ で対数が負になるので，$\mu$ は温度とともにいったん上がります。

### (2)
$n_1\gg N_{\mathrm{D}}$ では，根号を $u=4N_{\mathrm{D}}/n_1$ について $\sqrt{1+u}\approx1+u/2-u^2/8$ と展開します。

$$
\begin{aligned}
n&\approx\frac{n_1}{2}\left(\frac{2N_{\mathrm{D}}}{n_1}-\frac{2N_{\mathrm{D}}^{\,2}}{n_1^{\,2}}\right)\\
&=N_{\mathrm{D}}\left(1-\frac{N_{\mathrm{D}}}{n_1}\right)
\end{aligned}
$$

主要な項は $n\approx N_{\mathrm{D}}$ です。これを (1) の最初の $\mu$ の式に代入すると，

$$
\finalanswer{\mu=E_{\mathrm{c}}-k_{\mathrm{B}}T\ln\frac{N_{\mathrm{c}}}{N_{\mathrm{D}}}}
$$

となります。ドナーの電子がほぼすべて伝導帯に出た出払い領域です。電子密度は一定ですが，$N_{\mathrm{c}}$ が温度とともに増えるので，$\mu$ は伝導帯の底から離れて下がっていきます。

### (3)
$p=n_{\mathrm{i}}^{\,2}/n$ を中性の条件に代入すると，2次方程式 $n^2-N_{\mathrm{D}}n-n_{\mathrm{i}}^{\,2}=0$ が得られます。その正の解は次のとおりです。

$$
n=\frac{N_{\mathrm{D}}}{2}+\sqrt{\frac{N_{\mathrm{D}}^{\,2}}{4}+n_{\mathrm{i}}^{\,2}}
$$

一方，$n$ と $n_{\mathrm{i}}$ の式の比をとると，$N_{\mathrm{c}}$ と $E_{\mathrm{c}}$ が消えます。

$$
\begin{aligned}
\frac{n}{n_{\mathrm{i}}}&=\frac{N_{\mathrm{c}}e^{-(E_{\mathrm{c}}-\mu)/k_{\mathrm{B}}T}}{N_{\mathrm{c}}e^{-(E_{\mathrm{c}}-\mu_{\mathrm{i}})/k_{\mathrm{B}}T}}\\
&=e^{(\mu-\mu_{\mathrm{i}})/k_{\mathrm{B}}T}
\end{aligned}
$$

この式の対数をとり，上の $n$ を代入すると，

$$
\finalanswer{\mu-\mu_{\mathrm{i}}=k_{\mathrm{B}}T\ln\left(\frac{N_{\mathrm{D}}}{2n_{\mathrm{i}}}+\sqrt{1+\frac{N_{\mathrm{D}}^{\,2}}{4n_{\mathrm{i}}^{\,2}}}\right)}
$$

となります。$n_{\mathrm{i}}\ll N_{\mathrm{D}}$ では対数の中は $N_{\mathrm{D}}/n_{\mathrm{i}}$ になり，$\mu$ は次のように計算できます。

$$
\begin{aligned}
\mu&\approx\mu_{\mathrm{i}}+k_{\mathrm{B}}T\ln\frac{N_{\mathrm{D}}}{n_{\mathrm{i}}}\\
&=E_{\mathrm{c}}-k_{\mathrm{B}}T\ln\frac{N_{\mathrm{c}}}{n_{\mathrm{i}}}+k_{\mathrm{B}}T\ln\frac{N_{\mathrm{D}}}{n_{\mathrm{i}}}\\
&=E_{\mathrm{c}}-k_{\mathrm{B}}T\ln\frac{N_{\mathrm{c}}}{N_{\mathrm{D}}}
\end{aligned}
$$

これは (2) の結果と一致します。温度が上がって $n_{\mathrm{i}}\gg N_{\mathrm{D}}$ になると，$\mu-\mu_{\mathrm{i}}\approx k_{\mathrm{B}}TN_{\mathrm{D}}/(2n_{\mathrm{i}})$ は小さくなり，$\mu$ はギャップの中央付近の $\mu_{\mathrm{i}}$ に近づきます。化学ポテンシャルの温度変化を図に示します。

<!-- FIGURE solution (3): 横軸 温度 T，縦軸 エネルギー，原点 O（T = 0）。上から順に，伝導帯の底 E_c の水平な実線，そのすぐ下にドナー準位 E_D の水平な破線，ギャップの中ほどに μ_i の水平な点線，下に価電子帯の頂上 E_v の水平な実線を引く。μ の曲線を太い実線で描く：T = 0 で E_c と E_D の中点から始まり，わずかに上がってから下がり，E_D の線を横切ってさらに下がり，高温で μ_i の点線に近づく。横軸の下に，左から「低温領域」「出払い領域」「真性領域」と3つの範囲を示す。 -->

===== FILE: 06solid_state/08/08_055.md =====
---
tags:
  - 発展
---

# pn 接合の逆バイアスと接合容量

## 問題
$x<0$ にアクセプター密度 $N_{\mathrm{A}}$ の p 型半導体，$x>0$ にドナー密度 $N_{\mathrm{D}}$ の n 型半導体が接した階段型の pn 接合を考える。不純物はすべて電離しており，半導体の誘電率を $\varepsilon$，素電荷を $e>0$ とする。空乏層の両端の電位差が $U$ のとき，空乏層の幅 $W$ と，そのうち n 側の幅 $x_{\mathrm{n}}$ は

$$
\begin{aligned}
W&=\sqrt{\frac{2\varepsilon U}{e}\cdot\frac{N_{\mathrm{A}}+N_{\mathrm{D}}}{N_{\mathrm{A}}N_{\mathrm{D}}}}\\
x_{\mathrm{n}}&=\frac{N_{\mathrm{A}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}W
\end{aligned}
$$

で与えられる。熱平衡での n 側の p 側に対する電位を内蔵電位 $V_{\mathrm{bi}}>0$ とする。この接合に，p 側に対して n 側の電位を $V>0$ だけ高くする逆方向電圧をかける（図）。かけた電圧はすべて空乏層にかかるとする。以下の問いに答えよ。

<!-- FIGURE problem: 横長の長方形を描き，中央の縦の線 x = 0 で左右に分けて，左に「p 型」，右に「n 型」と書く。x = 0 をはさんだ帯状の領域（−x_p から x_n）を薄く塗って「空乏層」と注記し，帯の幅に W の寸法線を付ける。長方形の左端と右端から導線を出して電池につなぎ，電池の + 側が n 型の側，− 側が p 型の側になるように描き，電池に V とラベルする。下に x 軸の矢印を描き，原点を x = 0 に置く。 -->

(1) 空乏層の幅 $W(V)$ を求めよ。

(2) n 側の空乏層にある単位面積あたりの電荷を $Q$ とする。単位面積あたりの接合容量 $C=\mathrm{d}Q/\mathrm{d}V$ が $C=\varepsilon/W(V)$ となることを示せ。

(3) $N_{\mathrm{A}}\gg N_{\mathrm{D}}$ とする。$1/C^2$ を $V$ に対してプロットした直線の傾きを $s$，横軸との交点を $V=-V_0$ とする。$V_{\mathrm{bi}}$ と $N_{\mathrm{D}}$ を求めよ。

---

##解答・解説

### (1)
熱平衡では，n 側は p 側より $V_{\mathrm{bi}}$ だけ電位が高くなっています。逆方向電圧はこの電位差と同じ向きにかかります。空乏層にはキャリアがほとんどなく抵抗が大きいので，電圧はすべて空乏層にかかり，両端の電位差は $U=V_{\mathrm{bi}}+V$ になります。これを与えられた $W$ の式に代入すると，

$$
\finalanswer{W(V)=\sqrt{\frac{2\varepsilon(V_{\mathrm{bi}}+V)}{e}\cdot\frac{N_{\mathrm{A}}+N_{\mathrm{D}}}{N_{\mathrm{A}}N_{\mathrm{D}}}}}
$$

となります。逆方向電圧をかけるほど，空乏層は $\sqrt{V_{\mathrm{bi}}+V}$ に比例して広がります。

### (2)
n 側の空乏層は電離したドナーの正電荷をもつので，$Q=eN_{\mathrm{D}}x_{\mathrm{n}}$ です。与えられた $x_{\mathrm{n}}$ の式を使うと，次のように書けます。

$$
Q=\frac{eN_{\mathrm{A}}N_{\mathrm{D}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}W
$$

$\mathrm{d}W/\mathrm{d}V$ は，(1) の式を2乗してから $V$ で微分すると求まります。

$$
\begin{aligned}
W^2&=\frac{2\varepsilon(N_{\mathrm{A}}+N_{\mathrm{D}})}{eN_{\mathrm{A}}N_{\mathrm{D}}}(V_{\mathrm{bi}}+V)\\
2W\frac{\mathrm{d}W}{\mathrm{d}V}&=\frac{2\varepsilon(N_{\mathrm{A}}+N_{\mathrm{D}})}{eN_{\mathrm{A}}N_{\mathrm{D}}}
\end{aligned}
$$

$Q$ の式を $V$ で微分し，この結果を代入します。

$$
\begin{aligned}
C&=\frac{eN_{\mathrm{A}}N_{\mathrm{D}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}\cdot\frac{\mathrm{d}W}{\mathrm{d}V}\\
&=\frac{eN_{\mathrm{A}}N_{\mathrm{D}}}{N_{\mathrm{A}}+N_{\mathrm{D}}}\cdot\frac{\varepsilon(N_{\mathrm{A}}+N_{\mathrm{D}})}{eN_{\mathrm{A}}N_{\mathrm{D}}W}
\end{aligned}
$$

係数が打ち消し合うので，

$$
\finalanswer{C=\frac{\varepsilon}{W(V)}}
$$

となります。電圧を少し増やすと，空乏層の両端に逆符号の電荷が加わります。そのため接合は，極板の間隔が $W$ の平行板コンデンサーと同じ容量をもちます。

### (3)
(2) の結果を2乗して逆数をとり，(1) の $W^2$ を代入します。$N_{\mathrm{A}}\gg N_{\mathrm{D}}$ では $(N_{\mathrm{A}}+N_{\mathrm{D}})/(N_{\mathrm{A}}N_{\mathrm{D}})\approx1/N_{\mathrm{D}}$ です。

$$
\begin{aligned}
\frac{1}{C^2}&=\frac{W^2}{\varepsilon^2}\\
&=\frac{2(N_{\mathrm{A}}+N_{\mathrm{D}})}{e\varepsilon N_{\mathrm{A}}N_{\mathrm{D}}}(V_{\mathrm{bi}}+V)\\
&\approx\frac{2}{e\varepsilon N_{\mathrm{D}}}(V_{\mathrm{bi}}+V)
\end{aligned}
$$

これは $V$ の1次式で，傾きは $2/(e\varepsilon N_{\mathrm{D}})$，横軸との交点は $V=-V_{\mathrm{bi}}$ です。これらを $s$ と $V_0$ に等しいとおくと，

$$
\begin{aligned}
&\finalanswer{V_{\mathrm{bi}}=V_0}\\
&\finalanswer{N_{\mathrm{D}}=\frac{2}{e\varepsilon s}}
\end{aligned}
$$

となります。グラフを図に示します。

<!-- FIGURE solution (3): 横軸 V，縦軸 1/C²，原点 O。右上がりの直線を描き，V > 0 の部分を実線，横軸と交わる V = −V_0 までの V < 0 の部分を破線にする。横軸との交点に黒丸を置いて「−V_0 = −V_bi」と注記する。直線上に直角三角形を描いて傾き s を示す。 -->

片側の不純物密度が十分大きい接合では，空乏層はほぼすべて密度の小さい側に広がります。そのため容量の測定からわかるのは $N_{\mathrm{D}}$ で，$N_{\mathrm{A}}$ は決まりません。

===== FILE: 06solid_state/09/09_045.md =====
---
tags:
  - 発展
---

# ソフトモードと強誘電転移

## 問題
イオン結晶の長波長の光学フォノンについて，横波の角振動数を $\omega_{\mathrm{T}}$，縦波の角振動数を $\omega_{\mathrm{L}}$，静的な比誘電率を $\varepsilon_{\mathrm{r}}(0)$，電子の分極だけによる高振動数の比誘電率を $\varepsilon_\infty$ とする。これらの間にはリデイン・ザックス・テラーの関係

$$
\frac{\omega_{\mathrm{L}}^{\,2}}{\omega_{\mathrm{T}}^{\,2}}=\frac{\varepsilon_{\mathrm{r}}(0)}{\varepsilon_\infty}
$$

が成り立つ。また，分極率 $\alpha$ の粒子が数密度 $N$ で並んだ物質の比誘電率 $\varepsilon_{\mathrm{r}}$ は，局所電場を考えるとクラウジウス・モソッティの式

$$
\frac{\varepsilon_{\mathrm{r}}-1}{\varepsilon_{\mathrm{r}}+2}=\frac{N\alpha}{3\varepsilon_0}
$$

を満たす。$\varepsilon_0$ は真空の誘電率である。以下の問いに答えよ。

(1) 温度 $T$ を下げると横波の振動数が $\omega_{\mathrm{T}}^{\,2}=A(T-T_0)$ のように下がる結晶を考える。$A>0$ と $T_0$ は定数で，$T>T_0$ とする。$\omega_{\mathrm{L}}$ と $\varepsilon_\infty$ が温度によらないとき，$\varepsilon_{\mathrm{r}}(0)$ を $T$ の関数として求めよ。

(2) クラウジウス・モソッティの式で $N\alpha/3\varepsilon_0=1-\eta$ とし，$0<\eta\ll1$ とする。$\varepsilon_{\mathrm{r}}$ を $\eta$ の最低次まで求めよ。

(3) 電荷 $\pm q$ のイオンの対が数密度 $N$ で並び，対の双極子モーメントは相対変位 $w$ を用いて $qw$ と書けるとする。$w$ は局所電場 $\mathcal{E}_{\mathrm{loc}}$ のもとで

$$
M_{\mathrm{r}}\ddot{w}=-M_{\mathrm{r}}\omega_0^{\,2}w+q\mathcal{E}_{\mathrm{loc}}
$$

に従う。$M_{\mathrm{r}}$ は換算質量，$\omega_0>0$ は近距離力による定数である。電子の分極を無視し，角振動数 $\omega$ の電場に対する分極率 $\alpha(\omega)$ を用いてクラウジウス・モソッティの式が成り立つとする。$\varepsilon_{\mathrm{r}}(\omega)$ が発散する角振動数 $\omega_{\mathrm{T}}$ を，$\omega_0$ と $y_0=N\alpha(0)/3\varepsilon_0$ で表せ。

---

## 解答・解説

### (1)
リデイン・ザックス・テラーの関係を $\varepsilon_{\mathrm{r}}(0)$ について解きます。

$$
\varepsilon_{\mathrm{r}}(0)=\varepsilon_\infty\frac{\omega_{\mathrm{L}}^{\,2}}{\omega_{\mathrm{T}}^{\,2}}
$$

この式に $\omega_{\mathrm{T}}^{\,2}=A(T-T_0)$ を代入すると，

$$
\finalanswer{\varepsilon_{\mathrm{r}}(0)=\frac{\varepsilon_\infty\omega_{\mathrm{L}}^{\,2}}{A(T-T_0)}}
$$

となります。静的な誘電率は $1/(T-T_0)$ に比例して $T_0$ で発散します。これは強誘電体の転移点の上で観測されるキュリー・ワイス則です。振動数が0に向かう横波の光学モードをソフトモードとよびます。誘電率の逆数の温度変化を図に示します。

<!-- FIGURE solution (1): 横軸 温度 T，縦軸 1/ε_r(0)，原点 O。横軸上の T = T_0 の点から右上がりの直線を実線で描き，T_0 に目盛りを付ける。T < T_0 の側には何も描かない。直線のそばに「∝ ω_T² ∝ T − T_0」と注記する。 -->

### (2)
$y=N\alpha/3\varepsilon_0$ とおき，クラウジウス・モソッティの式を $\varepsilon_{\mathrm{r}}$ について解きます。

$$
\begin{aligned}
\varepsilon_{\mathrm{r}}-1&=y(\varepsilon_{\mathrm{r}}+2)\\
\varepsilon_{\mathrm{r}}&=\frac{1+2y}{1-y}
\end{aligned}
$$

この式に $y=1-\eta$ を代入します。

$$
\varepsilon_{\mathrm{r}}=\frac{3-2\eta}{\eta}
$$

$\eta\ll1$ では分子の $2\eta$ を無視できるので，

$$
\finalanswer{\varepsilon_{\mathrm{r}}\approx\frac{3}{\eta}}
$$

となります。$y\to1$ では，周りの双極子がつくる局所電場が分極をさらに強めます。$y=1$ になると，外部の電場がなくても分極が自分自身を保つ状態になります。これを分極破局とよびます。$\eta$ が $T-T_0$ に比例して小さくなるなら，この式からもキュリー・ワイス則が得られます。

### (3)
$w\propto e^{-i\omega t}$ として運動方程式を解くと，$w=q\mathcal{E}_{\mathrm{loc}}/\{M_{\mathrm{r}}(\omega_0^{\,2}-\omega^2)\}$ です。双極子モーメント $qw$ を $\mathcal{E}_{\mathrm{loc}}$ で割ると，分極率が得られます。

$$
\alpha(\omega)=\frac{q^2}{M_{\mathrm{r}}(\omega_0^{\,2}-\omega^2)}
$$

$y(\omega)=N\alpha(\omega)/3\varepsilon_0$ とおき，$y_0=y(0)$ を使って書き直します。

$$
y(\omega)=y_0\frac{\omega_0^{\,2}}{\omega_0^{\,2}-\omega^2}
$$

(2) の解答の式 $\varepsilon_{\mathrm{r}}=(1+2y)/(1-y)$ は $y=1$ で発散します。この条件を $\omega$ について解くと，

$$
\begin{aligned}
y_0\frac{\omega_0^{\,2}}{\omega_0^{\,2}-\omega_{\mathrm{T}}^{\,2}}&=1\\
\omega_{\mathrm{T}}^{\,2}&=\omega_0^{\,2}(1-y_0)
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{\omega_{\mathrm{T}}=\omega_0\sqrt{1-y_0}}
$$

となります。$y_0=1-\eta$ とおくと $\omega_{\mathrm{T}}^{\,2}=\omega_0^{\,2}\eta$ です。横波の振動数が0に近づくことと，静的な分極破局は同じ現象です。一方，$\varepsilon_{\mathrm{r}}=0$ となるのは $y=-1/2$ のときで，そこから $\omega_{\mathrm{L}}^{\,2}=\omega_0^{\,2}(1+2y_0)$ が得られます。2つの振動数の比は次のとおりです。

$$
\begin{aligned}
\frac{\omega_{\mathrm{L}}^{\,2}}{\omega_{\mathrm{T}}^{\,2}}&=\frac{1+2y_0}{1-y_0}\\
&=\varepsilon_{\mathrm{r}}(0)
\end{aligned}
$$

この模型では $\varepsilon_\infty=1$ なので，この結果はリデイン・ザックス・テラーの関係と一致します。

===== FILE: 06solid_state/10/10_025.md =====
---
tags:
  - 標準
---

# 断熱消磁

## 問題
互いに独立な $N$ 個のスピン $1/2$ の磁気モーメントを考える。$z$ 方向に磁束密度 $B>0$ をかけると，各モーメントの $z$ 成分は $+\mu_{\mathrm{B}}$ または $-\mu_{\mathrm{B}}$ で，エネルギーはそれぞれ $-\mu_{\mathrm{B}}B$，$+\mu_{\mathrm{B}}B$ である。$\mu_{\mathrm{B}}$ はボーア磁子である。温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$ とし，$x=\mu_{\mathrm{B}}B/k_{\mathrm{B}}T$ とおく。モーメントと格子振動など他の自由度との間の熱のやりとりは無視する。以下の問いに答えよ。

(1) $N$ 個のモーメント全体のエントロピー $S$ を $x$ の関数として求めよ。

(2) $x\ll1$ と $x\gg1$ のそれぞれについて，$S$ を $x$ に依存する最低次の項まで求めよ。

(3) 温度 $T_{\mathrm{i}}$，磁束密度 $B_{\mathrm{i}}$ の状態から，断熱的に磁束密度を $B_{\mathrm{f}}$ まで下げた。$0<B_{\mathrm{f}}<B_{\mathrm{i}}$ とする。到達する温度 $T_{\mathrm{f}}$ を求めよ。

---

## 解答・解説

### (1)
1つのモーメントの分配関数は，2つの状態のボルツマン因子の和 $Z_1=e^{x}+e^{-x}=2\cosh x$ です。モーメントは独立なので，全体の自由エネルギーは次のようになります。

$$
F=-Nk_{\mathrm{B}}T\ln(2\cosh x)
$$

エントロピーは $S=-\partial F/\partial T$ です。$x$ は $T$ に反比例するので，$\partial x/\partial T=-x/T$ に注意して微分します。

$$
\begin{aligned}
S&=Nk_{\mathrm{B}}\ln(2\cosh x)+Nk_{\mathrm{B}}T\tanh x\cdot\frac{\partial x}{\partial T}\\
&=Nk_{\mathrm{B}}\ln(2\cosh x)-Nk_{\mathrm{B}}x\tanh x
\end{aligned}
$$

したがって，

$$
\finalanswer{S=Nk_{\mathrm{B}}\left[\ln(2\cosh x)-x\tanh x\right]}
$$

となります。

### (2)
$x\ll1$ では，$\ln\cosh x\approx x^2/2$ と $\tanh x\approx x$ を使います。

$$
\begin{aligned}
\ln(2\cosh x)&\approx\ln2+\frac{x^2}{2}\\
x\tanh x&\approx x^2
\end{aligned}
$$

これらを (1) に代入すると，

$$
\finalanswer{S\approx Nk_{\mathrm{B}}\left(\ln2-\frac{x^2}{2}\right)}
$$

となります。$x\gg1$ では，$e^{-2x}$ について1次まで展開します。

$$
\begin{aligned}
\ln(2\cosh x)&=x+\ln\left(1+e^{-2x}\right)\\
&\approx x+e^{-2x}\\
x\tanh x&\approx x\left(1-2e^{-2x}\right)
\end{aligned}
$$

差をとると $(1+2x)e^{-2x}$ となり，$x\gg1$ ではそのうち $2xe^{-2x}$ が主要な項です。したがって，

$$
\finalanswer{S\approx2Nk_{\mathrm{B}}\,x\,e^{-2x}}
$$

となります。高温や弱い磁場では2つの状態がほぼ同じ確率で現れ，エントロピーは $Nk_{\mathrm{B}}\ln2$ に近づきます。低温や強い磁場では，ほぼすべてのモーメントが磁場の向きにそろい，エントロピーは0に近づきます。

### (3)
(1) の $S$ は $x$ だけの関数です。$S$ を $x$ で微分すると，

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}x}\frac{S}{Nk_{\mathrm{B}}}&=\tanh x-\left(\tanh x+\frac{x}{\cosh^2x}\right)\\
&=-\frac{x}{\cosh^2x}
\end{aligned}
$$

となり，$x>0$ で $S$ は単調に減ります。そのため，断熱過程で $S$ が一定に保たれると，$x$ も一定に保たれます。つまり $B/T$ が一定なので，

$$
\finalanswer{T_{\mathrm{f}}=\frac{B_{\mathrm{f}}}{B_{\mathrm{i}}}T_{\mathrm{i}}}
$$

となります。過程の様子を図に示します。

<!-- FIGURE solution (3): 横軸 温度 T，縦軸 S/(Nk_B)，原点 O。エントロピーの曲線を2本描く：磁束密度 B_f の曲線（左寄り，低温で立ち上がる）と，B_i の曲線（右寄り）。どちらも T → 0 で 0，高温で ln 2 に近づくようにし，ln 2 の高さに水平な点線を引く。温度 T_i で B_f の曲線から B_i の曲線へ下向きの矢印（等温で磁場を上げる）を描き，そこから左向きの水平な矢印を B_f の曲線まで引いて（断熱消磁）到達点の温度を T_f とラベルする。横軸に T_f と T_i の目盛りを付ける。 -->

磁場を下げると，スピンのエントロピーを保つために温度が下がります。実際には，スピンの系は冷えたあと格子から熱を受け取って格子を冷やします。モーメントどうしの弱い相互作用が内部磁場としてはたらくため，$B_{\mathrm{f}}\to0$ でも温度は0にはなりません。

===== FILE: 06solid_state/10/10_035.md =====
---
tags:
  - 発展
---

# ストーナー条件

## 問題
数密度 $n$ の伝導電子を絶対零度で考える。スピンを含めた単位体積あたりの状態密度を $D(E)$ とし，$E$ は運動エネルギーである。片方のスピンの状態密度は $D(E)/2$ である。$z$ 方向の磁束密度 $B$ と平行な磁気モーメントをもつ電子の密度を $n_+$，反平行な電子の密度を $n_-$ とし，$m=n_+-n_-$ とおく。平行な電子のエネルギーは運動エネルギーより $\mu_{\mathrm{B}}B+Im/2$ だけ低く，反平行な電子のエネルギーは同じだけ高い。$\mu_{\mathrm{B}}$ はボーア磁子，$I>0$ は交換相互作用の定数である。電子間の相互作用のエネルギー密度のうち $m$ に依存する部分は $-Im^2/4$ である。

$B=0$，$m=0$ でのフェルミエネルギーを $E_{\mathrm{F}}$，化学ポテンシャルを $\mu$ とする。磁化を $M=\mu_{\mathrm{B}}m$，磁化率を $\chi=\mu_0M/B$ とし，パウリ常磁性の磁化率を $\chi_{\mathrm{P}}=\mu_0\mu_{\mathrm{B}}^{\,2}D(E_{\mathrm{F}})$ とする。$\mu_0$ は真空の透磁率である。以下の問いに答えよ。

(1) $B$ の1次までで $\chi$ を求めよ。$\mu$ は $B$ の1次では変化しないとしてよい。

(2) $B=0$ で，全エネルギー密度の $m=0$ からの変化を $m$ の2次まで考える。$m=0$ の状態が不安定になる条件を求めよ。

(3) $ID(E_{\mathrm{F}})/2$ が1をわずかに超えるとき，$B=0$ での自発磁化 $M$ を求めよ。$D(E)$ を $E_{\mathrm{F}}$ のまわりで2次まで展開し，化学ポテンシャルの変化も考えよ。$D(E_{\mathrm{F}})$，$D'(E_{\mathrm{F}})$，$D''(E_{\mathrm{F}})$ をそれぞれ $D$，$D'$，$D''$ と書いてよい。

---

## 解答・解説

### (1)
$\Delta=\mu_{\mathrm{B}}B+Im/2$ とおきます。平行な電子は，エネルギー $E-\Delta$ が $\mu$ 以下の状態を占めるので，運動エネルギーは $\mu+\Delta$ まで詰まります。反平行な電子は $\mu-\Delta$ までです。

$$
n_\pm=\frac{1}{2}\int_0^{\mu\pm\Delta}D(E)\,\mathrm{d}E
$$

差をとり，$\Delta$ の1次まで残します。

$$
\begin{aligned}
m&=\frac{1}{2}\int_{\mu-\Delta}^{\mu+\Delta}D(E)\,\mathrm{d}E\\
&\approx D(E_{\mathrm{F}})\Delta
\end{aligned}
$$

$\Delta$ には $m$ 自身が含まれるので，$m$ を決める式は次のようになります。

$$
m=D(E_{\mathrm{F}})\left(\mu_{\mathrm{B}}B+\frac{I}{2}m\right)
$$

これを $m$ について解くと $m=D(E_{\mathrm{F}})\mu_{\mathrm{B}}B/\{1-ID(E_{\mathrm{F}})/2\}$ です。$\chi=\mu_0\mu_{\mathrm{B}}m/B$ に代入すると，

$$
\finalanswer{\chi=\frac{\chi_{\mathrm{P}}}{1-ID(E_{\mathrm{F}})/2}}
$$

となります。交換相互作用はスピンをさらにそろえるはたらきをもつので，磁化率はパウリ常磁性の値より大きくなり，$ID(E_{\mathrm{F}})/2\to1$ で発散します。

### (2)
$B=0$ で小さな $m$ をつくるには，平行な電子のフェルミ準位を $E_{\mathrm{F}}+\delta$ に上げ，反平行な電子のフェルミ準位を $E_{\mathrm{F}}-\delta$ に下げます。$E_{\mathrm{F}}$ の近くで状態密度を $D$ で一定とみなすと，電子数は保たれ，$m=D\delta$ です。運動エネルギーの増加は次のとおりです。

$$
\begin{aligned}
\Delta E_{\mathrm{kin}}&=\frac{D}{2}\int_{E_{\mathrm{F}}}^{E_{\mathrm{F}}+\delta}E\,\mathrm{d}E-\frac{D}{2}\int_{E_{\mathrm{F}}-\delta}^{E_{\mathrm{F}}}E\,\mathrm{d}E\\
&=\frac{D}{2}\left(E_{\mathrm{F}}\delta+\frac{\delta^2}{2}\right)-\frac{D}{2}\left(E_{\mathrm{F}}\delta-\frac{\delta^2}{2}\right)\\
&=\frac{D\delta^2}{2}
\end{aligned}
$$

$\delta=m/D$ を代入し，相互作用のエネルギー $-Im^2/4$ を加えます。

$$
\begin{aligned}
\Delta E&=\frac{m^2}{2D}-\frac{Im^2}{4}\\
&=\frac{m^2}{4}\left(\frac{2}{D}-I\right)
\end{aligned}
$$

$m^2$ の係数が負になると，$m\ne0$ の状態のほうがエネルギーが低くなります。したがって，不安定になる条件は

$$
\finalanswer{\frac{ID(E_{\mathrm{F}})}{2}>1}
$$

となります。これをストーナーの条件とよびます。等号が成り立つ点は，(1) で $\chi$ が発散する点と一致します。フェルミ準位での状態密度が大きい鉄，コバルト，ニッケルでこの条件が満たされます。

### (3)
$B=0$ では $\Delta=Im/2$ です。$G(E)=\int_0^ED(E')\,\mathrm{d}E'$ とおくと $n_\pm=G(\mu\pm\Delta)/2$ です。これを $\Delta$ について3次まで展開します。

$$
\begin{aligned}
n_++n_-&=G(\mu)+\frac{D'}{2}\Delta^2\\
n_+-n_-&=D(\mu)\Delta+\frac{D''}{6}\Delta^3
\end{aligned}
$$

電子数は $n=G(E_{\mathrm{F}})$ に保たれます。$\mu=E_{\mathrm{F}}+\delta\mu$ として $G(\mu)\approx G(E_{\mathrm{F}})+D\,\delta\mu$ とおくと，1つ目の式から化学ポテンシャルのずれが求まります。

$$
\delta\mu=-\frac{D'}{2D}\Delta^2
$$

これを $D(\mu)\approx D+D'\delta\mu$ に使い，2つ目の式に代入します。

$$
\begin{aligned}
m&=\left(D+D'\delta\mu\right)\Delta+\frac{D''}{6}\Delta^3\\
&=D\Delta-\frac{3D'^2-DD''}{6D}\Delta^3
\end{aligned}
$$

$m=2\Delta/I$ を代入して両辺を $\Delta$ で割り，$\Delta^2$ について解きます。

$$
\begin{aligned}
\frac{2}{I}&=D-\frac{3D'^2-DD''}{6D}\Delta^2\\
\Delta^2&=\frac{6D}{3D'^2-DD''}\left(D-\frac{2}{I}\right)
\end{aligned}
$$

$D-2/I=(2/I)(ID/2-1)$ で，最低次では $2/I\approx D$ です。$M=\mu_{\mathrm{B}}m=2\mu_{\mathrm{B}}\Delta/I\approx\mu_{\mathrm{B}}D\Delta$ を使うと，

$$
\finalanswer{M=\mu_{\mathrm{B}}D^2\sqrt{\frac{6}{3D'^2-DD''}\left(\frac{ID}{2}-1\right)}}
$$

となります。この解は $3D'^2>DD''$ のときに存在します。自発磁化は $(ID/2-1)^{1/2}$ に比例し，10-4 の平均場近似と同じ指数で現れます。たとえば $D\propto\sqrt{E}$ の自由電子では $3D'^2-DD''=D^2/E_{\mathrm{F}}^{\,2}$ となり，$M=\sqrt{6}\,\mu_{\mathrm{B}}DE_{\mathrm{F}}(ID/2-1)^{1/2}$ です。

===== FILE: 06solid_state/10/10_065.md =====
---
tags:
  - 発展
---

# マグノンとブロッホの T^{3/2} 則

## 問題
格子定数 $a$ の単純立方格子の各点に大きさ $S$ のスピンがある強磁性体を考える。最近接の交換相互作用を $J>0$ とすると，波数 $\boldsymbol{k}$ の小さいマグノンのエネルギーは

$$
\begin{aligned}
\hbar\omega&=Dk^2\\
D&=JSa^2
\end{aligned}
$$

である。$k=|\boldsymbol{k}|$ である。マグノンは化学ポテンシャル0のボース分布に従い，1個あたり全スピンの $z$ 成分を1だけ減らす。磁化は全スピンの $z$ 成分に比例する。温度を $T$，ボルツマン定数を $k_{\mathrm{B}}$ とし，$k_{\mathrm{B}}T\ll JS$ とする。$k$ についての積分は上限を $\infty$ にしてよい。必要なら次の積分を用いてよい。$\zeta$ はリーマンのゼータ関数である。

$$
\begin{aligned}
\int_0^\infty\frac{x^{1/2}}{e^x-1}\,\mathrm{d}x&=\frac{\sqrt{\pi}}{2}\zeta\!\left(\frac{3}{2}\right)\\
\int_0^\infty\frac{x^{3/2}}{e^x-1}\,\mathrm{d}x&=\frac{3\sqrt{\pi}}{4}\zeta\!\left(\frac{5}{2}\right)
\end{aligned}
$$

以下の問いに答えよ。

(1) 単位体積あたりのマグノンの数 $n_{\mathrm{mag}}$ を $k_{\mathrm{B}}T$ と $D$ で表せ。

(2) 絶対零度の磁化 $M(0)$ からの減少の割合 $[M(0)-M(T)]/M(0)$ を $S$，$J$，$k_{\mathrm{B}}T$ で表せ。

(3) マグノンによる単位体積あたりの熱容量 $C_{\mathrm{mag}}$ を求めよ。

---

##解答・解説

### (1)
単位体積あたりのモードの数は $\mathrm{d}^3k/(2\pi)^3$ です。各モードの平均のマグノン数をかけて積分し，球座標で角度の積分を先に行います。

$$
\begin{aligned}
n_{\mathrm{mag}}&=\int\frac{\mathrm{d}^3k}{(2\pi)^3}\cdot\frac{1}{e^{Dk^2/k_{\mathrm{B}}T}-1}\\
&=\frac{1}{2\pi^2}\int_0^\infty\frac{k^2}{e^{Dk^2/k_{\mathrm{B}}T}-1}\,\mathrm{d}k
\end{aligned}
$$

与えられた積分の形にするため，$x=Dk^2/k_{\mathrm{B}}T$ と置き換えます。

$$
\begin{aligned}
k&=\left(\frac{k_{\mathrm{B}}T}{D}\right)^{1/2}x^{1/2}\\
k^2\,\mathrm{d}k&=\frac{1}{2}\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}x^{1/2}\,\mathrm{d}x
\end{aligned}
$$

これを代入して，与えられた積分を使います。

$$
\begin{aligned}
n_{\mathrm{mag}}&=\frac{1}{4\pi^2}\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}\int_0^\infty\frac{x^{1/2}}{e^x-1}\,\mathrm{d}x\\
&=\frac{1}{4\pi^2}\cdot\frac{\sqrt{\pi}}{2}\zeta\!\left(\frac{3}{2}\right)\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}
\end{aligned}
$$

したがって，

$$
\finalanswer{n_{\mathrm{mag}}=\frac{\zeta(3/2)}{8\pi^{3/2}}\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}}
$$

となります。$k_{\mathrm{B}}T\ll JS$ ではゾーンの境界付近のマグノンはほとんど励起されないので，積分の上限を $\infty$ にしても結果はほとんど変わりません。

### (2)
単位体積あたりのスピンの数は $1/a^3$ なので，絶対零度での全スピンの $z$ 成分は単位体積あたり $S/a^3$ です。マグノン1個がこれを1だけ減らすので，減少の割合は次のようになります。

$$
\begin{aligned}
\frac{M(0)-M(T)}{M(0)}&=\frac{n_{\mathrm{mag}}a^3}{S}\\
&=\frac{\zeta(3/2)}{8\pi^{3/2}S}\cdot a^3\left(\frac{k_{\mathrm{B}}T}{JSa^2}\right)^{3/2}
\end{aligned}
$$

$a$ は打ち消し合うので，

$$
\finalanswer{\frac{M(0)-M(T)}{M(0)}=\frac{\zeta(3/2)}{8\pi^{3/2}S}\left(\frac{k_{\mathrm{B}}T}{JS}\right)^{3/2}}
$$

となります。これをブロッホの $T^{3/2}$ 則とよびます。平均場近似では，低温での磁化の減少は指数関数的に小さくなります。実際には，エネルギーの低いスピン波が励起されるため，磁化はべき乗でゆっくり減ります。

### (3)
エネルギー密度 $u$ は，(1) の被積分関数にマグノンのエネルギー $Dk^2$ をかけたものです。(1) と同じ置き換えを使うと，$Dk^2=k_{\mathrm{B}}Tx$ です。

$$
\begin{aligned}
u&=\frac{1}{2\pi^2}\int_0^\infty\frac{Dk^2\cdot k^2}{e^{Dk^2/k_{\mathrm{B}}T}-1}\,\mathrm{d}k\\
&=\frac{k_{\mathrm{B}}T}{4\pi^2}\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}\int_0^\infty\frac{x^{3/2}}{e^x-1}\,\mathrm{d}x\\
&=\frac{3\zeta(5/2)}{16\pi^{3/2}}k_{\mathrm{B}}T\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}
\end{aligned}
$$

$u$ は $T^{5/2}$ に比例するので，熱容量は $C_{\mathrm{mag}}=\mathrm{d}u/\mathrm{d}T=5u/(2T)$ です。したがって，

$$
\finalanswer{C_{\mathrm{mag}}=\frac{15\zeta(5/2)}{32\pi^{3/2}}k_{\mathrm{B}}\left(\frac{k_{\mathrm{B}}T}{D}\right)^{3/2}}
$$

となります。格子比熱は $T^3$ に比例するので，十分低温ではマグノンの寄与のほうが大きくなります。絶縁性の強磁性体では，比熱を $C=c_1T^{3/2}+c_2T^3$ と書き，$C/T^{3/2}$ を $T^{3/2}$ に対してプロットすると，2つの寄与を分けられます。

===== FILE: 06solid_state/10/10_075.md =====
---
tags:
  - 発展
---

# ランダウ反磁性

## 問題
$xy$ 平面内を運動する質量 $m$，電荷 $-e$（$e>0$）の2次元電子気体を考え，面積を $A$ とする。$z$ 方向に磁束密度 $B>0$ をかけると，エネルギー準位は

$$
E_n=\hbar\omega_{\mathrm{c}}\left(n+\frac{1}{2}\right)
$$

となる。$n=0,1,2,\ldots$ で，$\omega_{\mathrm{c}}=eB/m$ はサイクロトロン角振動数である。各準位に属する単位面積あたりの状態の数は，スピンを含めて $N_L=2eB/h$ である。$h=2\pi\hbar$ はプランク定数である。ゼーマンエネルギーは無視する。化学ポテンシャル $\mu$ と温度 $T$ は $\hbar\omega_{\mathrm{c}}\ll k_{\mathrm{B}}T\ll\mu$ を満たし，$k_{\mathrm{B}}$ はボルツマン定数である。単位面積あたりのグランドポテンシャルは

$$
\begin{aligned}
\frac{\Omega}{A}&=N_L\sum_{n=0}^{\infty}\phi(E_n)\\
\phi(E)&=-k_{\mathrm{B}}T\ln\left(1+e^{(\mu-E)/k_{\mathrm{B}}T}\right)
\end{aligned}
$$

である。ゆっくり変化して無限遠で0になる関数 $F$ に対して成り立つ近似式

$$
\sum_{n=0}^{\infty}F\!\left(n+\frac{1}{2}\right)\approx\int_0^\infty F(x)\,\mathrm{d}x+\frac{F'(0)}{24}
$$

を用いてよい。単位面積あたりの磁化を $M=-\partial(\Omega/A)/\partial B$，磁化率を $\chi_{\mathrm{L}}=\mu_0M/B$ とする。$\mu_0$ は真空の透磁率で，微分は $\mu$ と $T$ を一定にしてとる。以下の問いに答えよ。

(1) $\Omega/A$ のうち $B$ に依存する部分 $\Delta\Omega/A$ を求めよ。

(2) $\chi_{\mathrm{L}}$ を求めよ。

(3) ボーア磁子を $\mu_{\mathrm{B}}=e\hbar/2m$，スピンを含めた単位面積あたりの状態密度を $D=m/(\pi\hbar^2)$ とすると，2次元のパウリ常磁性の磁化率は $\chi_{\mathrm{P}}=\mu_0\mu_{\mathrm{B}}^{\,2}D$ である。$\chi_{\mathrm{L}}/\chi_{\mathrm{P}}$ を求めよ。

---

##解答・解説

### (1)
$F(x)=\phi(\hbar\omega_{\mathrm{c}}x)$ とおくと，$\phi(E_n)=F(n+1/2)$ です。$\phi$ は $k_{\mathrm{B}}T$ 程度のエネルギーの幅で変化し，$\hbar\omega_{\mathrm{c}}\ll k_{\mathrm{B}}T$ なので，$F$ は $x$ についてゆっくり変化します。そこで近似式を使います。

$$
\begin{aligned}
\frac{\Omega}{A}&=N_L\sum_{n=0}^{\infty}F\!\left(n+\frac{1}{2}\right)\\
&\approx N_L\int_0^\infty\phi(\hbar\omega_{\mathrm{c}}x)\,\mathrm{d}x+\frac{N_L}{24}F'(0)
\end{aligned}
$$

第1項は $E=\hbar\omega_{\mathrm{c}}x$ と置き換えて計算します。$N_L/(\hbar\omega_{\mathrm{c}})=m/(\pi\hbar^2)$ なので，

$$
\begin{aligned}
N_L\int_0^\infty\phi(\hbar\omega_{\mathrm{c}}x)\,\mathrm{d}x&=\frac{N_L}{\hbar\omega_{\mathrm{c}}}\int_0^\infty\phi(E)\,\mathrm{d}E\\
&=\frac{m}{\pi\hbar^2}\int_0^\infty\phi(E)\,\mathrm{d}E
\end{aligned}
$$

となります。これは $B$ を含まず，磁場がないときのグランドポテンシャルに等しくなります。第2項では $F'(0)=\hbar\omega_{\mathrm{c}}\phi'(0)$ です。$\phi$ の導関数はフェルミ分布になります。

$$
\begin{aligned}
\phi'(E)&=\frac{e^{(\mu-E)/k_{\mathrm{B}}T}}{1+e^{(\mu-E)/k_{\mathrm{B}}T}}\\
&=\frac{1}{e^{(E-\mu)/k_{\mathrm{B}}T}+1}
\end{aligned}
$$

$\mu\gg k_{\mathrm{B}}T$ なので $\phi'(0)\approx1$ です。$N_L=eB/(\pi\hbar)$ と $\omega_{\mathrm{c}}=eB/m$ を代入すると，

$$
\begin{aligned}
\frac{\Delta\Omega}{A}&=\frac{N_L\hbar\omega_{\mathrm{c}}}{24}\\
&=\frac{1}{24}\cdot\frac{eB}{\pi\hbar}\cdot\frac{\hbar eB}{m}
\end{aligned}
$$

となります。したがって，

$$
\finalanswer{\frac{\Delta\Omega}{A}=\frac{e^2B^2}{24\pi m}}
$$

となります。磁場をかけるとグランドポテンシャルが $B^2$ に比例して増えるので，この系は反磁性を示します。

### (2)
(1) の結果を $B$ で微分して符号を変えると，磁化が求まります。

$$
M=-\frac{e^2B}{12\pi m}
$$

これを $\mu_0/B$ 倍すると，

$$
\finalanswer{\chi_{\mathrm{L}}=-\frac{\mu_0e^2}{12\pi m}}
$$

となります。2次元系では磁化が単位面積あたりの量なので，$\chi_{\mathrm{L}}$ は長さの次元をもちます。古典力学では磁場は電子に仕事をしないので，熱平衡での軌道運動による磁化は0になります。この反磁性は，軌道運動がランダウ準位に量子化されたことから生じる量子力学的な効果です。

### (3)
はじめに $\chi_{\mathrm{P}}$ を $e$ と $m$ で表します。

$$
\begin{aligned}
\chi_{\mathrm{P}}&=\mu_0\frac{e^2\hbar^2}{4m^2}\cdot\frac{m}{\pi\hbar^2}\\
&=\frac{\mu_0e^2}{4\pi m}
\end{aligned}
$$

これで (2) の結果を割ると，

$$
\frac{\chi_{\mathrm{L}}}{\chi_{\mathrm{P}}}=-\frac{\mu_0e^2}{12\pi m}\cdot\frac{4\pi m}{\mu_0e^2}
$$

となります。したがって，

$$
\finalanswer{\frac{\chi_{\mathrm{L}}}{\chi_{\mathrm{P}}}=-\frac{1}{3}}
$$

となります。自由電子では，軌道の反磁性はスピンの常磁性の3分の1の大きさで，全体の磁化率は $2\chi_{\mathrm{P}}/3$ の常磁性になります。結晶中で有効質量が $m^*$ の電子では，この比は $-(m/m^*)^2/3$ に変わります。そのため，有効質量の小さい半導体では軌道の反磁性が大きくなります。

===== FILE: 06solid_state/11/11_055.md =====
---
tags:
  - 発展
---

# ギンツブルグ・ランダウ方程式とコヒーレンス長

## 問題
超伝導状態を複素数の秩序変数 $\psi(\boldsymbol{r})$ で表し，転移温度 $T_{\mathrm{c}}$ の近くで単位体積あたりの自由エネルギーを

$$
f_{\mathrm{s}}=f_{\mathrm{n}}+\alpha|\psi|^2+\frac{\beta}{2}|\psi|^4+\frac{1}{2m^*}\left|(-i\hbar\nabla-q\boldsymbol{A})\psi\right|^2
$$

とする。$f_{\mathrm{n}}$ は常伝導状態の自由エネルギー密度，$q$ と $m^*$ は超伝導電流を運ぶ粒子の電荷と質量，$\boldsymbol{A}$ はベクトルポテンシャルである。$\alpha=a(T-T_{\mathrm{c}})$，$\beta>0$ で，$a>0$ と $\beta$ は温度によらない。温度は $T<T_{\mathrm{c}}$ とし，コヒーレンス長を $\xi=\hbar/\sqrt{2m^*|\alpha|}$ で定義する。電流密度は

$$
\boldsymbol{j}=\frac{q\hbar}{2m^*i}\left(\psi^*\nabla\psi-\psi\nabla\psi^*\right)-\frac{q^2}{m^*}|\psi|^2\boldsymbol{A}
$$

で与えられ，磁束密度 $\boldsymbol{B}=\nabla\times\boldsymbol{A}$ は $\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$ を満たす。$\mu_0$ は真空の透磁率である。以下の問いに答えよ。

(1) $\boldsymbol{A}=\boldsymbol{0}$ で，$\psi$ が実数で $x$ だけに依存するとする。$\int f_{\mathrm{s}}\,\mathrm{d}x$ を極小にする $\psi(x)$ が満たす微分方程式を求めよ。

(2) 常伝導体と接する境界 $x=0$ で $\psi(0)=0$ とし，$x\to\infty$ で $\psi$ は一様な平衡値 $\psi_0>0$ に，$\psi'$ は0に近づくとする。(1) の方程式の両辺に $\psi'$ を掛けて積分する方法を用いて，$x>0$ での $\psi(x)$ を $\psi_0$ と $\xi$ で表せ。

(3) $\psi=\psi_0$ が一様なとき，磁場は表面から侵入長 $\lambda$ 程度の深さまでしか入らない。比 $\kappa=\lambda/\xi$ を $m^*$，$q$，$\hbar$，$\beta$，$\mu_0$ で表せ。

---

## 解答・解説

### (1)
$\psi$ が実数で $\boldsymbol{A}=\boldsymbol{0}$ なら，勾配の項は $\hbar^2\psi'^2/(2m^*)$ になります。

$$
\int f_{\mathrm{s}}\,\mathrm{d}x=\int\left[f_{\mathrm{n}}+\alpha\psi^2+\frac{\beta}{2}\psi^4+\frac{\hbar^2}{2m^*}\psi'^2\right]\mathrm{d}x
$$

$\psi$ を $\psi+\delta\psi$ に変えたときの1次の変化を求めます。$\psi'\delta\psi'$ の項は部分積分して $\delta\psi$ の形にします。両端で $\delta\psi=0$ とするので，境界の項は残りません。

$$
\begin{aligned}
\delta\int f_{\mathrm{s}}\,\mathrm{d}x&=\int\left[\left(2\alpha\psi+2\beta\psi^3\right)\delta\psi+\frac{\hbar^2}{m^*}\psi'\,\delta\psi'\right]\mathrm{d}x\\
&=\int\left[2\alpha\psi+2\beta\psi^3-\frac{\hbar^2}{m^*}\psi''\right]\delta\psi\,\mathrm{d}x
\end{aligned}
$$

任意の $\delta\psi$ でこれが0になるには，括弧の中が0でなければなりません。両辺を2で割ると，

$$
\finalanswer{-\frac{\hbar^2}{2m^*}\psi''+\alpha\psi+\beta\psi^3=0}
$$

となります。これが1次元のギンツブルグ・ランダウ方程式です。

### (2)
まず平衡値を求めます。一様な解では $\psi''=0$ なので $\alpha+\beta\psi_0^{\,2}=0$ となり，$\psi_0^{\,2}=|\alpha|/\beta$ です。次に，(1) の方程式に $\psi'$ を掛けます。各項は完全微分になります。

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left[-\frac{\hbar^2}{4m^*}\psi'^2+\frac{\alpha}{2}\psi^2+\frac{\beta}{4}\psi^4\right]=0
$$

括弧の中は一定で，その値は $x\to\infty$ での値 $-\beta\psi_0^{\,4}/4$ です。$\alpha=-\beta\psi_0^{\,2}$ を使って整理します。

$$
\begin{aligned}
\frac{\hbar^2}{4m^*}\psi'^2&=\frac{\alpha}{2}\psi^2+\frac{\beta}{4}\psi^4+\frac{\beta}{4}\psi_0^{\,4}\\
&=\frac{\beta}{4}\left(\psi_0^{\,4}-2\psi_0^{\,2}\psi^2+\psi^4\right)\\
&=\frac{\beta}{4}\left(\psi_0^{\,2}-\psi^2\right)^2
\end{aligned}
$$

$m^*\beta/\hbar^2=1/(2\xi^2\psi_0^{\,2})$ であり，$\psi$ は0から増えるので $\psi'>0$ の側をとります。$u=\psi/\psi_0$ とおくと，次の方程式が得られます。

$$
\frac{\mathrm{d}u}{\mathrm{d}x}=\frac{1-u^2}{\sqrt{2}\,\xi}
$$

変数を分けて，$x=0$ で $u=0$ から積分します。

$$
\begin{aligned}
\int_0^{u}\frac{\mathrm{d}s}{1-s^2}&=\int_0^{x}\frac{\mathrm{d}t}{\sqrt{2}\,\xi}\\
\operatorname{artanh}u&=\frac{x}{\sqrt{2}\,\xi}
\end{aligned}
$$

したがって，

$$
\finalanswer{\psi(x)=\psi_0\tanh\frac{x}{\sqrt{2}\,\xi}}
$$

となります。秩序変数の様子を図に示します。

<!-- FIGURE solution (2): 横軸 x/ξ（0〜5），縦軸 ψ/ψ0（0〜1.1），原点 O。曲線 tanh(x/(√2 ξ)) を実線で描く。原点から立ち上がり，x/ξ ≈ 3 でほぼ 1 になる。縦軸 1 の高さに水平な破線を引く。原点より左の x < 0 の領域を薄く塗って「常伝導体」と注記する。x/ξ = √2 に縦の点線を引き，そこで ψ/ψ0 = tanh 1 ≈ 0.76 となる点に黒丸を置く。 -->

秩序変数は，境界から $\xi$ 程度の距離で一様な値に回復します。$\xi$ は $|\alpha|^{-1/2}$ に比例するので，$T_{\mathrm{c}}$ に近づくと $(T_{\mathrm{c}}-T)^{-1/2}$ に比例して発散します。

### (3)
$\psi=\psi_0$ が実数の定数なら，電流密度の第1項は0です。残りの項の回転をとると，ロンドン方程式の形になります。

$$
\nabla\times\boldsymbol{j}=-\frac{q^2\psi_0^{\,2}}{m^*}\boldsymbol{B}
$$

$\nabla\times\boldsymbol{B}=\mu_0\boldsymbol{j}$ の回転をとり，$\nabla\cdot\boldsymbol{B}=0$ を使います。

$$
\begin{aligned}
-\nabla^2\boldsymbol{B}&=\mu_0\nabla\times\boldsymbol{j}\\
\nabla^2\boldsymbol{B}&=\frac{\mu_0q^2\psi_0^{\,2}}{m^*}\boldsymbol{B}
\end{aligned}
$$

この方程式の解は，表面から $\lambda$ の距離で $e^{-x/\lambda}$ のように減衰します。右辺の係数が $1/\lambda^2$ にあたるので，$\psi_0^{\,2}=|\alpha|/\beta$ を代入すると，

$$
\begin{aligned}
\lambda^2&=\frac{m^*}{\mu_0q^2\psi_0^{\,2}}\\
&=\frac{m^*\beta}{\mu_0q^2|\alpha|}
\end{aligned}
$$

となります。これを $\xi^2=\hbar^2/(2m^*|\alpha|)$ で割ると，$|\alpha|$ が消えます。

$$
\begin{aligned}
\kappa^2&=\frac{m^*\beta}{\mu_0q^2|\alpha|}\cdot\frac{2m^*|\alpha|}{\hbar^2}\\
&=\frac{2m^{*2}\beta}{\mu_0q^2\hbar^2}
\end{aligned}
$$

したがって，

$$
\finalanswer{\kappa=\frac{m^*}{\hbar|q|}\sqrt{\frac{2\beta}{\mu_0}}}
$$

となります。$\lambda$ と $\xi$ はどちらも $(T_{\mathrm{c}}-T)^{-1/2}$ に比例するので，比 $\kappa$ は温度によりません。これをギンツブルグ・ランダウ・パラメータとよびます。$\kappa<1/\sqrt{2}$ の物質は第1種超伝導体に，$\kappa>1/\sqrt{2}$ の物質は磁束が侵入した状態をとる第2種超伝導体になります。

===== FILE: 06solid_state/11/11_065.md =====
---
tags:
  - 発展
---

# 直流 SQUID

## 問題
超伝導体のリングに，同じ臨界電流 $I_{\mathrm{c}}>0$ をもつ2つのジョセフソン接合 a，b を入れる。リングは2つの接合によって左の電極 L と右の電極 R に分かれ，電流 $I$ を L から入れて R から取り出す（図）。超伝導体の中の状態を $\psi=\sqrt{n_{\mathrm{s}}}\,e^{i\theta}$ で表すと，電流密度は

$$
\boldsymbol{j}=\frac{qn_{\mathrm{s}}}{m^*}\left(\hbar\nabla\theta-q\boldsymbol{A}\right)
$$

である。$q=-2e$ は電子対の電荷で $e>0$，$m^*$ は電子対の質量，$\boldsymbol{A}$ はベクトルポテンシャルである。接合 a の位相差を

$$
\delta_{\mathrm{a}}=\theta_{\mathrm{R}}-\theta_{\mathrm{L}}-\frac{q}{\hbar}\int_{\mathrm{L}}^{\mathrm{R}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}
$$

で定義する。$\theta_{\mathrm{L}},\theta_{\mathrm{R}}$ は接合 a の両側の位相で，積分は接合 a を L から R へ横切る短い経路に沿ってとる。接合 b の位相差 $\delta_{\mathrm{b}}$ も同じように定義する。電圧0では，接合 a を L から R へ流れる電流は $I_{\mathrm{c}}\sin\delta_{\mathrm{a}}$，接合 b では $I_{\mathrm{c}}\sin\delta_{\mathrm{b}}$ である。リングの太さは磁場侵入長より十分大きい。リングの穴を貫く磁束を $\Phi$ とし，その向きは $\mathrm{L}\to\mathrm{a}\to\mathrm{R}\to\mathrm{b}\to\mathrm{L}$ と回る向きと右ねじの関係にとる。リングを流れる電流がつくる磁束は無視し，$\Phi_0=h/2e$，$h=2\pi\hbar$ とする。以下の問いに答えよ。

<!-- FIGURE problem: 超伝導体のリングを上から見た図。リングを横長の長円の帯として描き，上側の中央と下側の中央にそれぞれ短い隙間（接合）を入れて，上を a，下を b とラベルする。隙間で分けられた左半分を L，右半分を R とラベルする。L の左端から導線を出して電流 I が入る矢印を，R の右端から導線を出して I が出る矢印を描く。リングの穴の中央に，L → a → R → b → L と回る時計回りの細い円弧の矢印を描き，その中心に紙面の裏向きの記号 ⊗ を置いて Φ とラベルする。 -->

(1) $N$ を整数として，$\delta_{\mathrm{a}}-\delta_{\mathrm{b}}=2\pi\Phi/\Phi_0+2\pi N$ となることを示せ。

(2) 電圧0で素子に流せる電流の最大値 $I_{\max}$ を $\Phi$ の関数として求めよ。

(3) 面積 $S$ のリングに垂直に一様な磁束密度 $B$ をかける。$I_{\max}$ が極大になる $B$ の間隔 $\Delta B$ を求めよ。

---

##解答・解説

### (1)
リングの表面から十分深いところを通り，接合 a，b を横切って $\mathrm{L}\to\mathrm{a}\to\mathrm{R}\to\mathrm{b}\to\mathrm{L}$ と一周する閉じた経路 $C$ を考えます。$C$ のうち超伝導体の中にある部分では $\boldsymbol{j}=\boldsymbol{0}$ なので，$\hbar\nabla\theta=q\boldsymbol{A}$ が成り立ちます。経路の4つの部分での位相の変化を書き出します。接合 b は R から L へ逆向きに横切るので，$\delta_{\mathrm{b}}$ の符号が変わります。

$$
\begin{aligned}
\Delta\theta_{\mathrm{a}}&=\delta_{\mathrm{a}}+\frac{q}{\hbar}\int_{\mathrm{a}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}\\
\Delta\theta_{\mathrm{R}}&=\frac{q}{\hbar}\int_{\mathrm{R}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}\\
\Delta\theta_{\mathrm{b}}&=-\delta_{\mathrm{b}}+\frac{q}{\hbar}\int_{\mathrm{b}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}\\
\Delta\theta_{\mathrm{L}}&=\frac{q}{\hbar}\int_{\mathrm{L}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}
\end{aligned}
$$

各積分は，$C$ のそれぞれの部分に沿って一周の向きにとります。$\psi$ は1つの値をとるので，一周したときの位相の変化の合計は $2\pi N$ です。$\boldsymbol{A}$ の積分を合計すると $\oint_C\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}=\Phi$ になるので，

$$
\delta_{\mathrm{a}}-\delta_{\mathrm{b}}+\frac{q}{\hbar}\Phi=2\pi N
$$

が得られます。$q=-2e$ と $\Phi_0=h/2e$ から $-q\Phi/\hbar=2\pi\Phi/\Phi_0$ です。したがって，

$$
\finalanswer{\delta_{\mathrm{a}}-\delta_{\mathrm{b}}=\frac{2\pi\Phi}{\Phi_0}+2\pi N}
$$

となります。接合がなく $\delta_{\mathrm{a}}=\delta_{\mathrm{b}}=0$ の場合には，この式から磁束が $\Phi_0$ の整数倍に限られ，11-4 の磁束の量子化と一致します。

### (2)
平均の位相差を $\bar{\delta}=(\delta_{\mathrm{a}}+\delta_{\mathrm{b}})/2$ とおきます。(1) から $(\delta_{\mathrm{a}}-\delta_{\mathrm{b}})/2=\pi\Phi/\Phi_0+\pi N$ です。2つの正弦の和を積に直すと，

$$
\begin{aligned}
I&=I_{\mathrm{c}}\left(\sin\delta_{\mathrm{a}}+\sin\delta_{\mathrm{b}}\right)\\
&=2I_{\mathrm{c}}\sin\frac{\delta_{\mathrm{a}}+\delta_{\mathrm{b}}}{2}\cos\frac{\delta_{\mathrm{a}}-\delta_{\mathrm{b}}}{2}\\
&=2I_{\mathrm{c}}\sin\bar{\delta}\,\cos\left(\frac{\pi\Phi}{\Phi_0}+\pi N\right)
\end{aligned}
$$

となります。磁束が決まっても $\bar{\delta}$ は自由に変われるので，流す電流に応じて $\bar{\delta}$ が決まります。電流が最大になるのは $|\sin\bar{\delta}|=1$ のときです。$|\cos(\pi\Phi/\Phi_0+\pi N)|=|\cos(\pi\Phi/\Phi_0)|$ なので，

$$
\finalanswer{I_{\max}=2I_{\mathrm{c}}\left|\cos\frac{\pi\Phi}{\Phi_0}\right|}
$$

となります。最大電流の磁束依存性を図に示します。

<!-- FIGURE solution (2): 横軸 Φ/Φ0（−2〜2），縦軸 I_max/I_c（0〜2.2），原点 O。曲線 2|cos(πΦ/Φ0)| を実線で描く。Φ/Φ0 が整数のとき値 2 の極大，半整数のとき 0 になり，周期 1 で繰り返す形にする。縦軸 2 の高さに水平な点線を引き，隣り合う極大の間に両矢印を描いて「周期 Φ0」と注記する。 -->

2つの接合を流れる超伝導電流は，光の二重スリットのように干渉します。磁束が $\Phi_0$ の整数倍のとき強め合い，半整数倍のとき打ち消し合います。

### (3)
一様な磁束密度のもとでは，リングを貫く磁束は $\Phi=BS$ です。(2) から，$I_{\max}$ は $\Phi$ が $\Phi_0$ の整数倍のとき極大になります。隣り合う極大の間で $\Phi$ は $\Phi_0$ だけ変わるので，$\Delta B=\Phi_0/S$ です。$\Phi_0=h/2e$ を代入すると，

$$
\finalanswer{\Delta B=\frac{h}{2eS}}
$$

となります。たとえば $S=1\ \mathrm{mm^2}$ では，$\Delta B$ は約 $2\times10^{-9}\ \mathrm{T}$ です。さらに1周期の中での $I_{\max}$ の変化を読み取れば，これよりはるかに小さい磁場の変化も測定できます。これが直流 SQUID による高感度の磁場測定の原理です。

===== END =====