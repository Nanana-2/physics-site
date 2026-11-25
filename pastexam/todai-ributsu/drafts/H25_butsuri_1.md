---
title: 東大理物 平成25年度 物理学 第1問：一次元調和振動子とコヒーレント状態
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成25年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成25年度 物理学 第1問：一次元調和振動子とコヒーレント状態

## 問題

ハミルトニアンが

$$
\mathcal{H} = \frac{\hat{p}^2}{2m} + \frac{m\omega^2 \hat{x}^2}{2} \tag{1}
$$

で与えられる角振動数 $\omega$ の一次元調和振動子の量子力学を考える。ただし，調和振動子の質点の質量を $m$，位置演算子を $\hat{x}$，運動量演算子を $\hat{p}$ で表し，プランク定数$/2\pi$ を $\hbar$ とする。次の各設問に答えよ。

(1) 以下の文章を読んで，$\boxed{\text{ア}}$〜$\boxed{\text{ク}}$ に当てはまる数式を書け。

一次元調和振動子の消滅演算子 $\hat{a}$ は，

$$
\hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\,\hat{x} + \frac{i}{\sqrt{2m\hbar\omega}}\,\hat{p} \tag{2}
$$

で与えられる。このとき，$\hat{a}$ に共役な生成演算子 $\hat{a}^{\dagger}$ は，$\hat{x}$ と $\hat{p}$ を用いて $\hat{a}^{\dagger} = \boxed{\text{ア}}$ と表される。この $\hat{a}$ と $\hat{a}^{\dagger}$ の交換関係は $[\hat{a}, \hat{a}^{\dagger}] = \boxed{\text{イ}}$ をみたす。$\hat{x}$ と $\hat{p}$ を $\hat{a}$ と $\hat{a}^{\dagger}$ を用いて表すと，$\hat{x} = \boxed{\text{ウ}}$ と $\hat{p} = \boxed{\text{エ}}$ となるので，ハミルトニアン $\mathcal{H}$ も $\hat{x}$ と $\hat{p}$ ではなく $\hat{a}$ と $\hat{a}^{\dagger}$ を用いて $\mathcal{H} = \boxed{\text{オ}}$ と書くことができる。これより，$\mathcal{H}$ の規格化された基底状態 $|\phi_0\rangle$ に対応する $\mathcal{H}$ のエネルギー固有値 $E_0$ は，$E_0 = \boxed{\text{カ}}$ で与えられる。$n$ 番目の規格化された励起状態を $|\phi_n\rangle$，対応するエネルギー固有値を $E_n$ と表すと，$|\phi_n\rangle$ と $|\phi_{n+1}\rangle$ は $|\phi_{n+1}\rangle = \boxed{\text{キ}}\,\hat{a}^{\dagger}|\phi_n\rangle$（$n = 0, 1, 2, \cdots$）で与えられる関係式を満たし，$E_n = \boxed{\text{ク}}$ となる。ただし，$\boxed{\text{キ}}$ は正の実数となるように位相を選ぶものとする。

(2) ハミルトニアン $\mathcal{H}$ による一次元調和振動子の時間発展を考える。時刻 $t = 0$ における規格化された初期状態 $|\psi(0)\rangle$ が，設問 1 で定義された $|\phi_n\rangle$ と複素係数 $c_n(0)$ を用いて

$$
|\psi(0)\rangle = \sum_{n=0}^{\infty} c_n(0)\,|\phi_n\rangle \tag{3}
$$

で与えられているとき，時刻 $t$ における状態 $|\psi(t)\rangle = \sum_{n=0}^{\infty} c_n(t)\,|\phi_n\rangle$ の複素係数 $c_n(t)$ を $c_n(0)$ を用いて表せ。

(3) 設問 1 で定義された $|\phi_n\rangle$ における $\hat{x}$ の分散を $(\Delta x)^2 = \langle\phi_n|\hat{x}^2|\phi_n\rangle - (\langle\phi_n|\hat{x}|\phi_n\rangle)^2$，$\hat{p}$ の分散を $(\Delta p)^2 = \langle\phi_n|\hat{p}^2|\phi_n\rangle - (\langle\phi_n|\hat{p}|\phi_n\rangle)^2$ とする。このとき，これらの平方根の積 $\Delta x \cdot \Delta p$ を求めよ。

(4) 一次元調和振動子が，ある複素数パラメータ $\alpha = r e^{i\theta}$（$r \ge 0,\ 0 \le \theta < 2\pi$）を用いて表される次の重ね合わせ状態

$$
|\alpha\rangle = e^{-\frac{|\alpha|^2}{2}} \sum_{n=0}^{\infty} \frac{\alpha^n}{\sqrt{n!}}\,|\phi_n\rangle = e^{-\frac{r^2}{2}} \sum_{n=0}^{\infty} \frac{(r e^{i\theta})^n}{\sqrt{n!}}\,|\phi_n\rangle \tag{4}
$$

で与えられているとき，$|\alpha\rangle$ が $\hat{a}$ の固有状態であることを確かめよ。また，$|\alpha\rangle$ における $\hat{x}$ の期待値 $\langle\alpha|\hat{x}|\alpha\rangle$ と $\hat{p}$ の期待値 $\langle\alpha|\hat{p}|\alpha\rangle$ を求め，$r$ と $\theta$ の関数として表せ。

(5) 一次元調和振動子の初期状態が，式 (4) で定義された重ね合わせ状態 $|\alpha\rangle$ と実数 $r_0 \ge 0$ を用いて $|\psi(0)\rangle = |\alpha = r_0\rangle$ で与えられているとき，$|\psi(t)\rangle$ を求めよ。また，$\hat{x}$ と $\hat{p}$ を $\hat{X} = \sqrt{\dfrac{m\omega}{\hbar}}\,\hat{x}$ と $\hat{P} = \dfrac{1}{\sqrt{m\hbar\omega}}\,\hat{p}$ に従って変数変換し，$|\psi(t)\rangle$ における $\hat{X}$ の期待値 $\langle\psi(t)|\hat{X}|\psi(t)\rangle$ と $\hat{P}$ の期待値 $\langle\psi(t)|\hat{P}|\psi(t)\rangle$ の時間発展の特徴を述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成25年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
位置 $\hat{x}$ と運動量 $\hat{p}$ から消滅演算子 $\hat{a}$ と生成演算子 $\hat{a}^{\dagger}$ を作ると，ハミルトニアンは個数演算子 $\hat{a}^{\dagger}\hat{a}$ の1次式になります。そのため，エネルギー固有値や $\hat{x}^2$，$\hat{p}^2$ の期待値は，微分方程式を解かずに交換関係だけで計算することができます。

エネルギー固有値は等間隔に並んでいます。そのため，$\hat{a}$ の固有状態 $|\alpha\rangle$ を時間発展させると，各成分の位相がそろって回り，状態は全体の位相を除いて $\hat{a}$ の固有状態のままになります。
</div>

### (1)
$\hat{x}$ と $\hat{p}$ はエルミート演算子なので，式 (2) のエルミート共役をとると $\hat{a}^{\dagger}$ が得られます。

$$
\hat{a}^{\dagger} = \sqrt{\frac{m\omega}{2\hbar}}\,\hat{x} - \frac{i}{\sqrt{2m\hbar\omega}}\,\hat{p}
$$

正準交換関係 $[\hat{x}, \hat{p}] = i\hbar$ を用いて $[\hat{a}, \hat{a}^{\dagger}]$ を計算します。

$$
\begin{aligned}
[\hat{a}, \hat{a}^{\dagger}] &= \left[\sqrt{\frac{m\omega}{2\hbar}}\,\hat{x} + \frac{i}{\sqrt{2m\hbar\omega}}\,\hat{p},\; \sqrt{\frac{m\omega}{2\hbar}}\,\hat{x} - \frac{i}{\sqrt{2m\hbar\omega}}\,\hat{p}\right] \\
&= -\frac{i}{2\hbar}[\hat{x}, \hat{p}] + \frac{i}{2\hbar}[\hat{p}, \hat{x}] \\
&= -\frac{i}{2\hbar}(i\hbar) + \frac{i}{2\hbar}(-i\hbar) \\
&= 1
\end{aligned}
$$

$\hat{a}$ と $\hat{a}^{\dagger}$ の和と差をとって $\hat{x}$ と $\hat{p}$ について解きます。

$$
\begin{aligned}
\hat{a} + \hat{a}^{\dagger} &= 2\sqrt{\frac{m\omega}{2\hbar}}\,\hat{x} \\
\hat{x} &= \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a} + \hat{a}^{\dagger}\right)
\end{aligned}
$$

$$
\begin{aligned}
\hat{a} - \hat{a}^{\dagger} &= \frac{2i}{\sqrt{2m\hbar\omega}}\,\hat{p} \\
\hat{p} &= -i\sqrt{\frac{m\hbar\omega}{2}}\left(\hat{a} - \hat{a}^{\dagger}\right)
\end{aligned}
$$

これらを式 (1) に代入し，$\hat{a}\hat{a}^{\dagger} = \hat{a}^{\dagger}\hat{a} + 1$ を用いて整理します。

$$
\begin{aligned}
\mathcal{H} &= \frac{1}{2m}\left(-\frac{m\hbar\omega}{2}\right)\left(\hat{a} - \hat{a}^{\dagger}\right)^2 + \frac{m\omega^2}{2}\left(\frac{\hbar}{2m\omega}\right)\left(\hat{a} + \hat{a}^{\dagger}\right)^2 \\
&= \frac{\hbar\omega}{4}\left[-\left(\hat{a}^2 - \hat{a}\hat{a}^{\dagger} - \hat{a}^{\dagger}\hat{a} + (\hat{a}^{\dagger})^2\right) + \left(\hat{a}^2 + \hat{a}\hat{a}^{\dagger} + \hat{a}^{\dagger}\hat{a} + (\hat{a}^{\dagger})^2\right)\right] \\
&= \frac{\hbar\omega}{2}\left(\hat{a}\hat{a}^{\dagger} + \hat{a}^{\dagger}\hat{a}\right) \\
&= \hbar\omega\left(\hat{a}^{\dagger}\hat{a} + \frac{1}{2}\right)
\end{aligned}
$$

基底状態 $|\phi_0\rangle$ は $\hat{a}|\phi_0\rangle = 0$ を満たすので，$\mathcal{H}|\phi_0\rangle = \dfrac{1}{2}\hbar\omega|\phi_0\rangle$ より $E_0 = \dfrac{1}{2}\hbar\omega$ です。

次に $|\phi_n\rangle$ が $\hat{a}^{\dagger}\hat{a}|\phi_n\rangle = n|\phi_n\rangle$ を満たす規格化状態であるとします。$\hat{a}^{\dagger}|\phi_n\rangle$ のノルムの2乗を計算します。

$$
\begin{aligned}
\langle\phi_n|\hat{a}\hat{a}^{\dagger}|\phi_n\rangle &= \langle\phi_n|(\hat{a}^{\dagger}\hat{a} + 1)|\phi_n\rangle \\
&= (n + 1)\langle\phi_n|\phi_n\rangle \\
&= n + 1
\end{aligned}
$$

位相を正の実数に選ぶと $|\phi_{n+1}\rangle = \dfrac{1}{\sqrt{n+1}}\hat{a}^{\dagger}|\phi_n\rangle$ です。また $[\hat{a}^{\dagger}\hat{a}, \hat{a}^{\dagger}] = \hat{a}^{\dagger}$ より $\hat{a}^{\dagger}\hat{a}|\phi_n\rangle = n|\phi_n\rangle$ が帰納的に成り立つので，$E_n = \hbar\omega\left(n + \dfrac{1}{2}\right)$ となります。

以上より，空欄に当てはまる数式は次のとおりです。

- ア：$\sqrt{\dfrac{m\omega}{2\hbar}}\,\hat{x} - \dfrac{i}{\sqrt{2m\hbar\omega}}\,\hat{p}$
- イ：$1$
- ウ：$\sqrt{\dfrac{\hbar}{2m\omega}}\left(\hat{a} + \hat{a}^{\dagger}\right)$
- エ：$-i\sqrt{\dfrac{m\hbar\omega}{2}}\left(\hat{a} - \hat{a}^{\dagger}\right)$
- オ：$\hbar\omega\left(\hat{a}^{\dagger}\hat{a} + \dfrac{1}{2}\right)$
- カ：$\dfrac{1}{2}\hbar\omega$
- キ：$\dfrac{1}{\sqrt{n+1}}$
- ク：$\hbar\omega\left(n + \dfrac{1}{2}\right)$

### (2)
ハミルトニアン $\mathcal{H}$ は時間に依存しないので，時刻 $t$ の状態は時間発展演算子 $e^{-i\mathcal{H}t/\hbar}$ を初期状態 $|\psi(0)\rangle$ に作用させて得られます。

$$
\begin{aligned}
|\psi(t)\rangle &= e^{-i\mathcal{H}t/\hbar}|\psi(0)\rangle \\
&= \sum_{n=0}^{\infty} c_n(0)\,e^{-i\mathcal{H}t/\hbar}|\phi_n\rangle \\
&= \sum_{n=0}^{\infty} c_n(0)\,e^{-i E_n t/\hbar}|\phi_n\rangle \\
&= \sum_{n=0}^{\infty} c_n(0)\,e^{-i\left(n + \frac{1}{2}\right)\omega t}|\phi_n\rangle
\end{aligned}
$$

これと $|\psi(t)\rangle = \sum_{n=0}^{\infty} c_n(t)\,|\phi_n\rangle$ の係数を比較して，$c_n(t)$ が求まります。

$$
\finalanswer{c_n(t) = c_n(0)\,e^{-i\left(n + \frac{1}{2}\right)\omega t}}
$$

### (3)
$\hat{a}|\phi_n\rangle = \sqrt{n}|\phi_{n-1}\rangle$，$\hat{a}^{\dagger}|\phi_n\rangle = \sqrt{n+1}|\phi_{n+1}\rangle$ と状態の直交性 $\langle\phi_m|\phi_n\rangle = \delta_{mn}$ より，$\langle\phi_n|\hat{a}|\phi_n\rangle = 0$，$\langle\phi_n|\hat{a}^{\dagger}|\phi_n\rangle = 0$ です。したがって，$\langle\phi_n|\hat{x}|\phi_n\rangle = 0$，$\langle\phi_n|\hat{p}|\phi_n\rangle = 0$ となります。

同様に，$\langle\phi_n|\hat{a}^2|\phi_n\rangle = 0$，$\langle\phi_n|(\hat{a}^{\dagger})^2|\phi_n\rangle = 0$ なので，$\hat{x}^2$ と $\hat{p}^2$ の期待値は次のように計算されます。

$$
\begin{aligned}
(\Delta x)^2 &= \langle\phi_n|\hat{x}^2|\phi_n\rangle \\
&= \frac{\hbar}{2m\omega}\langle\phi_n|\left(\hat{a}^2 + \hat{a}\hat{a}^{\dagger} + \hat{a}^{\dagger}\hat{a} + (\hat{a}^{\dagger})^2\right)|\phi_n\rangle \\
&= \frac{\hbar}{2m\omega}\langle\phi_n|(2\hat{a}^{\dagger}\hat{a} + 1)|\phi_n\rangle \\
&= \frac{\hbar}{m\omega}\left(n + \frac{1}{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
(\Delta p)^2 &= \langle\phi_n|\hat{p}^2|\phi_n\rangle \\
&= -\frac{m\hbar\omega}{2}\langle\phi_n|\left(\hat{a}^2 - \hat{a}\hat{a}^{\dagger} - \hat{a}^{\dagger}\hat{a} + (\hat{a}^{\dagger})^2\right)|\phi_n\rangle \\
&= \frac{m\hbar\omega}{2}\langle\phi_n|(2\hat{a}^{\dagger}\hat{a} + 1)|\phi_n\rangle \\
&= m\hbar\omega\left(n + \frac{1}{2}\right)
\end{aligned}
$$

両者の積の平方根をとると，$\Delta x \cdot \Delta p$ が得られます。

$$
\begin{aligned}
\Delta x \cdot \Delta p &= \sqrt{\frac{\hbar}{m\omega}\left(n + \frac{1}{2}\right) \cdot m\hbar\omega\left(n + \frac{1}{2}\right)} \\
&= \hbar\left(n + \frac{1}{2}\right)
\end{aligned}
$$

$$
\finalanswer{\Delta x \cdot \Delta p = \hbar\left(n + \frac{1}{2}\right)}
$$

### (4)
式 (4) の $|\alpha\rangle$ に $\hat{a}$ を作用させます。$\hat{a}|\phi_0\rangle = 0$ なので $n = 0$ の項は消え，$n \ge 1$ の項に $\hat{a}|\phi_n\rangle = \sqrt{n}|\phi_{n-1}\rangle$ を用います。

$$
\begin{aligned}
\hat{a}|\alpha\rangle &= e^{-\frac{|\alpha|^2}{2}} \sum_{n=1}^{\infty} \frac{\alpha^n}{\sqrt{n!}}\sqrt{n}\,|\phi_{n-1}\rangle \\
&= \alpha e^{-\frac{|\alpha|^2}{2}} \sum_{n=1}^{\infty} \frac{\alpha^{n-1}}{\sqrt{(n-1)!}}\,|\phi_{n-1}\rangle \\
&= \alpha e^{-\frac{|\alpha|^2}{2}} \sum_{m=0}^{\infty} \frac{\alpha^m}{\sqrt{m!}}\,|\phi_m\rangle \\
&= \alpha|\alpha\rangle
\end{aligned}
$$

ここで $m = n - 1$ とおきました。したがって，$|\alpha\rangle$ は固有値 $\alpha$ に属する $\hat{a}$ の固有状態です。

また，$|\alpha\rangle$ のノルムの2乗は次のように $1$ になります。

$$
\begin{aligned}
\langle\alpha|\alpha\rangle &= e^{-|\alpha|^2}\sum_{n=0}^{\infty} \frac{|\alpha|^{2n}}{n!} \\
&= e^{-|\alpha|^2} e^{|\alpha|^2} \\
&= 1
\end{aligned}
$$

$\hat{a}|\alpha\rangle = \alpha|\alpha\rangle$ とそのエルミート共役 $\langle\alpha|\hat{a}^{\dagger} = \alpha^*\langle\alpha|$ を用いて，$\hat{x}$ と $\hat{p}$ の期待値を計算します。

$$
\begin{aligned}
\langle\alpha|\hat{x}|\alpha\rangle &= \sqrt{\frac{\hbar}{2m\omega}}\langle\alpha|(\hat{a} + \hat{a}^{\dagger})|\alpha\rangle \\
&= \sqrt{\frac{\hbar}{2m\omega}}\left(\alpha + \alpha^*\right) \\
&= \sqrt{\frac{\hbar}{2m\omega}}\,2r\cos\theta \\
&= \sqrt{\frac{2\hbar}{m\omega}}\,r\cos\theta
\end{aligned}
$$

$$
\begin{aligned}
\langle\alpha|\hat{p}|\alpha\rangle &= -i\sqrt{\frac{m\hbar\omega}{2}}\langle\alpha|(\hat{a} - \hat{a}^{\dagger})|\alpha\rangle \\
&= -i\sqrt{\frac{m\hbar\omega}{2}}\left(\alpha - \alpha^*\right) \\
&= -i\sqrt{\frac{m\hbar\omega}{2}}\,2ir\sin\theta \\
&= \sqrt{2m\hbar\omega}\,r\sin\theta
\end{aligned}
$$

$$
\finalanswer{\langle\alpha|\hat{x}|\alpha\rangle = \sqrt{\frac{2\hbar}{m\omega}}\,r\cos\theta, \qquad \langle\alpha|\hat{p}|\alpha\rangle = \sqrt{2m\hbar\omega}\,r\sin\theta}
$$

### (5)
初期状態 $|\psi(0)\rangle = |\alpha = r_0\rangle$ の展開係数は $c_n(0) = e^{-r_0^2/2}\dfrac{r_0^n}{\sqrt{n!}}$ です。設問2の結果を用いると，時刻 $t$ における状態 $|\psi(t)\rangle$ は次のようになります。

$$
\begin{aligned}
|\psi(t)\rangle &= e^{-\frac{r_0^2}{2}} \sum_{n=0}^{\infty} \frac{r_0^n}{\sqrt{n!}} e^{-i\left(n + \frac{1}{2}\right)\omega t}\,|\phi_n\rangle \\
&= e^{-\frac{i\omega t}{2}}\,e^{-\frac{r_0^2}{2}} \sum_{n=0}^{\infty} \frac{\left(r_0 e^{-i\omega t}\right)^n}{\sqrt{n!}}\,|\phi_n\rangle \\
&= e^{-\frac{i\omega t}{2}}\,\left|r_0 e^{-i\omega t}\right\rangle
\end{aligned}
$$

状態 $|\psi(t)\rangle$ は全体の位相因子 $e^{-i\omega t/2}$ を除いて，$r = r_0$，$\theta = -\omega t$ とした固有状態 $|\alpha\rangle$ に一致します。設問4の結果を用いて $\hat{X}$ と $\hat{P}$ の期待値を求めます。

$$
\begin{aligned}
\langle\psi(t)|\hat{X}|\psi(t)\rangle &= \sqrt{\frac{m\omega}{\hbar}}\langle\psi(t)|\hat{x}|\psi(t)\rangle \\
&= \sqrt{2}\,r_0 \cos(-\omega t) \\
&= \sqrt{2}\,r_0 \cos\omega t
\end{aligned}
$$

$$
\begin{aligned}
\langle\psi(t)|\hat{P}|\psi(t)\rangle &= \frac{1}{\sqrt{m\hbar\omega}}\langle\psi(t)|\hat{p}|\psi(t)\rangle \\
&= \sqrt{2}\,r_0 \sin(-\omega t) \\
&= -\sqrt{2}\,r_0 \sin\omega t
\end{aligned}
$$

これらより，$\langle\psi(t)|\hat{X}|\psi(t)\rangle^2 + \langle\psi(t)|\hat{P}|\psi(t)\rangle^2 = 2r_0^2$ が成り立ちます。したがって，期待値の組 $\bigl(\langle\hat{X}\rangle, \langle\hat{P}\rangle\bigr)$ は，時刻 $t = 0$ に点 $(\sqrt{2}\,r_0, 0)$ から出発し，原点を中心とする半径 $\sqrt{2}\,r_0$ の円周上を角速度 $\omega$ で時計回りに等速円運動します。これは古典的な一次元調和振動子の位相空間上の軌道と同じ振る舞いです。

$$
\finalanswer{|\psi(t)\rangle = e^{-\frac{i\omega t}{2}}\left|r_0 e^{-i\omega t}\right\rangle, \qquad \langle\psi(t)|\hat{X}|\psi(t)\rangle = \sqrt{2}\,r_0 \cos\omega t, \qquad \langle\psi(t)|\hat{P}|\psi(t)\rangle = -\sqrt{2}\,r_0 \sin\omega t}
$$
