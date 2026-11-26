---
title: 東大理物 平成14年度 数学 第2問：球座標3次元ラプラス方程式と球面調和関数展開
tags:
  - 院試過去問
  - 東大理物
  - 微分方程式
  - 特殊関数・変分法
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成14年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成14年度 数学 第2問：球座標3次元ラプラス方程式と球面調和関数展開

## 問題

三次元ラプラス方程式は，極座標を用いて

$$
\left(\frac{1}{r}\frac{\partial^2}{\partial r^2}r - \frac{\hat{L}^2}{r^2}\right)U(r, \theta, \varphi) = 0, \tag{1}
$$

$$
\hat{L}^2 \equiv -\left(\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\sin\theta\frac{\partial}{\partial\theta} + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}\right) \tag{2}
$$

と表せる。また，球面調和関数 $Y_{\ell m}(\theta, \varphi)$ は，

$$
\hat{L}^2 Y_{\ell m}(\theta, \varphi) = \ell(\ell + 1)Y_{\ell m}(\theta, \varphi) \tag{3}
$$

を満たす（$\ell = 0, 1, 2, \dots$；$m = -\ell, -\ell + 1, \dots, \ell$）。
{: .problem-lead }

(1) ラプラス方程式の解 $U(r, \theta, \varphi)$ を $R_\ell(r)Y_{\ell m}(\theta, \varphi)$ と変数分離したとき，$R_\ell(r)$ の満たす微分方程式を求めよ。

(2) 設問 (1) で得られた微分方程式から $R_\ell(r)$ の独立な二つの基本解 $A_\ell(r), B_\ell(r)$ を求めよ。

$U(r, \theta, \varphi)$ に対する境界条件が球面上で与えられれば，設問 (2) で得られた $A_\ell(r)$ と $B_\ell(r)$ を用いて，

$$
U(r, \theta, \varphi) = \sum_{\ell=0}^{\infty}\sum_{m=-\ell}^{\ell} \bigl[\alpha_{\ell m} A_\ell(r) + \beta_{\ell m} B_\ell(r)\bigr]Y_{\ell m}(\theta, \varphi) \tag{4}
$$

と展開し，境界条件に合うような係数 $\alpha_{\ell m}, \beta_{\ell m}$ を持つ解を求めることができる。具体的に，$r = a$ 及び $b$（ただし $b > a > 0$ とする）での境界条件が

$$
U(a, \theta, \varphi) = 0, \qquad U(b, \theta, \varphi) = \sin\theta\cos\varphi \tag{5}
$$

と与えられているとき，以下の問いに答えよ。

(3) $\sin\theta\cos\varphi$ を $Y_{\ell m}(\theta, \varphi)$ を用いて表せ。ただし，$Y_{00}(\theta, \varphi) = \sqrt{\dfrac{1}{4\pi}}$，$Y_{1\pm 1}(\theta, \varphi) = \mp\sqrt{\dfrac{3}{8\pi}}\sin\theta e^{\pm i\varphi}$（複号同順），$Y_{10}(\theta, \varphi) = \sqrt{\dfrac{3}{4\pi}}\cos\theta$ を用いてよい。

(4) 境界条件 (5) と $Y_{\ell m}(\theta, \varphi)$ の直交条件

$$
\int \mathrm{d}\Omega\,Y_{\ell' m'}^*(\theta, \varphi)Y_{\ell m}(\theta, \varphi) = \delta_{\ell'\ell}\delta_{m'm} \tag{6}
$$

から係数 $\alpha_{\ell m}, \beta_{\ell m}$ を決定せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成14年度 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
球座標の3次元ラプラス方程式に変数分離形 $R_\ell(r)Y_{\ell m}(\theta, \varphi)$ を代入すると，角度部分が固有値 $\ell(\ell + 1)$ で置き換わり，動径関数 $R_\ell(r)$ に対するオイラー型常微分方程式が得られます。

べき乗形の試行解から2つの基本解 $r^\ell$ と $r^{-\ell-1}$ を求め，境界条件 $\sin\theta\cos\varphi$ を球面調和関数で展開して直交関係を用いることで，各 $(\ell, m)$ 成分ごとに独立な連立1次方程式として展開係数を求めます。
</div>

### (1)

$U(r, \theta, \varphi) = R_\ell(r)Y_{\ell m}(\theta, \varphi)$ を式 (1) に代入し，式 (3) の固有値方程式 $\hat{L}^2 Y_{\ell m} = \ell(\ell + 1)Y_{\ell m}$ を用います。

$$
\left\{\frac{1}{r}\frac{\mathrm{d}^2}{\mathrm{d}r^2}\bigl(r R_\ell(r)\bigr) - \frac{\ell(\ell + 1)}{r^2}R_\ell(r)\right\}Y_{\ell m}(\theta, \varphi) = 0
$$

これがすべての $(\theta, \varphi)$ で成り立つため，波括弧の中が $0$ になります。さらに $\dfrac{1}{r}\dfrac{\mathrm{d}^2}{\mathrm{d}r^2}(r R_\ell) = \dfrac{\mathrm{d}^2 R_\ell}{\mathrm{d}r^2} + \dfrac{2}{r}\dfrac{\mathrm{d}R_\ell}{\mathrm{d}r}$ と展開すると，求める微分方程式は次式となります。

$$
\finalanswer{\frac{\mathrm{d}^2 R_\ell}{\mathrm{d}r^2} + \frac{2}{r}\frac{\mathrm{d}R_\ell}{\mathrm{d}r} - \frac{\ell(\ell + 1)}{r^2}R_\ell = 0}
$$

### (2)

設問 (1) の微分方程式はオイラー型なので，$R_\ell(r) = r^s$ の形の解を代入します。

$$
s(s - 1)r^{s-2} + 2s r^{s-2} - \ell(\ell + 1)r^{s-2} = 0
$$

$r^{s-2}$ でくくって整理します。

$$
\bigl\{s(s + 1) - \ell(\ell + 1)\bigr\}r^{s-2} = 0
$$

$r > 0$ より括弧内が $0$ となり，次のように因数分解することができます。

$$
(s - \ell)(s + \ell + 1) = 0
$$

よって $s = \ell$ または $s = -(\ell + 1)$ です。$\ell \ge 0$ の整数に対して $\ell \neq -(\ell + 1)$ なので，独立な2つの基本解 $A_\ell(r), B_\ell(r)$ は次式となります。

$$
\finalanswer{A_\ell(r) = r^\ell, \qquad B_\ell(r) = r^{-\ell - 1}}
$$

### (3)

与えられた $Y_{11}(\theta, \varphi) = -\sqrt{\dfrac{3}{8\pi}}\sin\theta\,e^{i\varphi}$ と $Y_{1,-1}(\theta, \varphi) = +\sqrt{\dfrac{3}{8\pi}}\sin\theta\,e^{-i\varphi}$ の差をとります。

$$
\begin{aligned}
Y_{1,-1}(\theta, \varphi) - Y_{11}(\theta, \varphi) &= \sqrt{\frac{3}{8\pi}}\sin\theta\bigl(e^{-i\varphi} + e^{i\varphi}\bigr) \\
&= \sqrt{\frac{3}{8\pi}}\sin\theta\cdot 2\cos\varphi \\
&= \sqrt{\frac{3}{2\pi}}\sin\theta\cos\varphi
\end{aligned}
$$

両辺に $\sqrt{\dfrac{2\pi}{3}}$ を掛けると，$\sin\theta\cos\varphi$ は次式となります。

$$
\finalanswer{\sin\theta\cos\varphi = \sqrt{\frac{2\pi}{3}}\bigl(Y_{1,-1}(\theta, \varphi) - Y_{11}(\theta, \varphi)\bigr)}
$$

### (4)

式 (4) に $r = a$ および $r = b$ を代入し，両辺に $Y_{\ell' m'}^*(\theta, \varphi)$ を掛けて全立体角で積分します。直交条件 (6) と境界条件 (5) および設問 (3) の結果を用いると，すべての $(\ell, m)$ に対して次の連立方程式が得られます。

まず $(\ell, m) \neq (1, 1), (1, -1)$ のとき，境界 $r = a, b$ での条件は次式になります。

$$
\alpha_{\ell m} a^\ell + \beta_{\ell m} a^{-\ell - 1} = 0, \qquad \alpha_{\ell m} b^\ell + \beta_{\ell m} b^{-\ell - 1} = 0
$$

係数行列の行列式を計算します。

$$
a^\ell b^{-\ell - 1} - b^\ell a^{-\ell - 1} = \frac{a^{2\ell + 1} - b^{2\ell + 1}}{(ab)^{\ell + 1}}
$$

$b > a > 0$ より $a^{2\ell + 1} - b^{2\ell + 1} \neq 0$ なので，解は $\alpha_{\ell m} = 0$ かつ $\beta_{\ell m} = 0$ のみとなります。

次に $\ell = 1$，$m = \pm 1$ のとき，$A_1(r) = r$，$B_1(r) = r^{-2}$ であり，設問 (3) より $r = b$ での係数は $m = 1$ で $-\sqrt{\dfrac{2\pi}{3}}$，$m = -1$ で $+\sqrt{\dfrac{2\pi}{3}}$ です。複号同順で連立方程式を立てます。

$$
\alpha_{1,\pm 1} a + \frac{\beta_{1,\pm 1}}{a^2} = 0, \qquad \alpha_{1,\pm 1} b + \frac{\beta_{1,\pm 1}}{b^2} = \mp\sqrt{\frac{2\pi}{3}}
$$

第1式より $\beta_{1,\pm 1} = -a^3\alpha_{1,\pm 1}$ を得ます。これを第2式に代入します。

$$
\alpha_{1,\pm 1}\left(b - \frac{a^3}{b^2}\right) = \mp\sqrt{\frac{2\pi}{3}}
$$

左辺を通分します。

$$
\alpha_{1,\pm 1}\frac{b^3 - a^3}{b^2} = \mp\sqrt{\frac{2\pi}{3}}
$$

$b > a > 0$ より $b^3 - a^3 \neq 0$ なので，これを解くと $\alpha_{1,\pm 1}$ と $\beta_{1,\pm 1} = -a^3\alpha_{1,\pm 1}$ が得られます。

$$
\alpha_{1,\pm 1} = \mp\sqrt{\frac{2\pi}{3}}\frac{b^2}{b^3 - a^3}, \qquad \beta_{1,\pm 1} = \pm\sqrt{\frac{2\pi}{3}}\frac{a^3 b^2}{b^3 - a^3}
$$

以上より，複号同順で $(\ell, m) = (1, \pm 1)$ 以外のすべての係数は $0$ であり，求める係数は次式となります。

$$
\finalanswer{
\begin{aligned}
\alpha_{1,\pm 1} &= \mp\sqrt{\frac{2\pi}{3}}\frac{b^2}{b^3 - a^3}, \qquad \beta_{1,\pm 1} = \pm\sqrt{\frac{2\pi}{3}}\frac{a^3 b^2}{b^3 - a^3} \\
\alpha_{\ell m} &= 0, \qquad \beta_{\ell m} = 0 \qquad \bigl((\ell, m) \neq (1, \pm 1)\bigr)
\end{aligned}
}
$$
