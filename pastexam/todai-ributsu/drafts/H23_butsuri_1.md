---
title: 東大理物 平成23年度 物理学 第1問：3次元分離型ポテンシャルの束縛状態
tags:
  - 院試過去問
  - 東大理物
  - 量子力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成23年度
exam_subject: 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。
---

# 東大理物 平成23年度 物理学 第1問：3次元分離型ポテンシャルの束縛状態

## 問題

質量 $m$ の粒子に対する三次元のシュレーディンガー方程式

$$
\left(\frac{\hat{\boldsymbol{p}}^2}{2m} + \hat{V}\right)|\psi\rangle = E|\psi\rangle
$$

について，以下の設問に答えよ。この問題では，自然単位系を用いて $\hbar = 1$ とし，積分領域は三次元空間の全領域とする。

(1) 状態 $|\psi\rangle$ および演算子 $\hat{O}$ について，それらの座標表示と運動量表示の間に，次の関係が成り立つことを示せ。ただし，$\langle\boldsymbol{x}|\boldsymbol{p}\rangle = \dfrac{1}{(2\pi)^{3/2}} e^{i\boldsymbol{p}\cdot\boldsymbol{x}}$ を用いてよい。

$$
\begin{aligned}
\langle\boldsymbol{p}|\psi\rangle &= \frac{1}{(2\pi)^{3/2}}\int \mathrm{d}^3 x\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x}}\langle\boldsymbol{x}|\psi\rangle \\
\langle\boldsymbol{p}|\hat{O}|\boldsymbol{p}'\rangle &= \frac{1}{(2\pi)^3}\iint \mathrm{d}^3 x\,\mathrm{d}^3 x'\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x} + i\boldsymbol{p}'\cdot\boldsymbol{x}'}\langle\boldsymbol{x}|\hat{O}|\boldsymbol{x}'\rangle
\end{aligned}
$$

座標表示でのポテンシャル $\hat{V}$ が，ある実関数 $g(\boldsymbol{x})$ を用いて，$\langle\boldsymbol{x}|\hat{V}|\boldsymbol{x}'\rangle = -\dfrac{\lambda}{2m} g(\boldsymbol{x}) g(\boldsymbol{x}')$（$\lambda > 0$）と表されるとき，$\hat{V}$ は分離型ポテンシャルと呼ばれる。以下では，分離型ポテンシャルを持つシュレーディンガー方程式を，運動量表示で解くことを考える。
{: .problem-lead }

(2) 運動量表示でのシュレーディンガー方程式

$$
\frac{\boldsymbol{p}^2}{2m}\langle\boldsymbol{p}|\psi\rangle + \int \mathrm{d}^3 p'\,\langle\boldsymbol{p}|\hat{V}|\boldsymbol{p}'\rangle\langle\boldsymbol{p}'|\psi\rangle = E\langle\boldsymbol{p}|\psi\rangle
$$

においても，ポテンシャルが運動量の関数 $h(\boldsymbol{p})$ を用いて分離型

$$
\langle\boldsymbol{p}|\hat{V}|\boldsymbol{p}'\rangle = -\frac{1}{(2\pi)^3}\frac{\lambda}{2m} h(\boldsymbol{p}) h(-\boldsymbol{p}')
$$

となることを示せ。

(3) $E = -\dfrac{\nu^2}{2m}$ の束縛状態が存在するとき，運動量表示での束縛状態の波動関数が

$$
\langle\boldsymbol{p}|\psi\rangle = C\frac{h(\boldsymbol{p})}{\boldsymbol{p}^2 + \nu^2} \qquad (C\text{ は定数})
$$

となることを示せ。

(4) 関数 $g(\boldsymbol{x})$ が次の式で与えられるとする。

$$
g(\boldsymbol{x}) = \frac{\exp(-\mu|\boldsymbol{x}|)}{4\pi|\boldsymbol{x}|} \qquad (\mu > 0)
$$

このとき，設問2の $h(\boldsymbol{p})$ は

$$
h(\boldsymbol{p}) = \frac{1}{\boldsymbol{p}^2 + \mu^2}
$$

となることを計算の詳細も記して示せ。

(5) 設問4で与えられた $h(\boldsymbol{p})$ の場合に，$|\nu|$ を $\lambda$ と $\mu$ を用いて表し，束縛状態が存在するために $\lambda$ が満たすべき条件を求めよ。必要なら，次の公式を用いてもよい。

$$
\int \mathrm{d}^3 p\,\frac{1}{(\boldsymbol{p}^2 + \nu^2)(\boldsymbol{p}^2 + \mu^2)^2} = \frac{\pi^2}{|\mu|(|\mu| + |\nu|)^2}
$$

(6) 設問4で与えられた $h(\boldsymbol{p})$ の場合に，座標表示での束縛状態の波動関数 $\langle\boldsymbol{x}|\psi\rangle$ を求めよ。ただし，規格化はしなくてもよい。また，その概略を図示せよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成23年度修士課程入学試験 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，解答に図を追加して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
分離型ポテンシャルでは，$\langle\boldsymbol{x}|\hat{V}|\boldsymbol{x}'\rangle$ が $\boldsymbol{x}$ だけの因子と $\boldsymbol{x}'$ だけの因子の積になっています。運動量表示でもこの積の形が保たれるので，シュレーディンガー方程式の積分項は，$h(\boldsymbol{p})$ と $\boldsymbol{p}$ によらない積分との積になります。そのため，積分方程式を解かずに，波動関数の $\boldsymbol{p}$ 依存性を求めることができます。

$\boldsymbol{p}$ によらない積分は定数 $C$ を含みます。求めた波動関数をこの積分にもう一度代入すると，$C$ を $C$ 自身で表す式ができます。束縛状態では $C\neq0$ なので，この式から $\nu$ と $\lambda$，$\mu$ の関係式を作ります。

座標表示の波動関数は，運動量表示の波動関数を逆フーリエ変換して求めます。$\dfrac{1}{(\boldsymbol{p}^2+\nu^2)(\boldsymbol{p}^2+\mu^2)}$ を部分分数に分けると，(4) と同じ形のフーリエ変換を逆向きに使うことができます。
</div>

### (1)
座標固有状態の完全性関係は次のとおりです。

$$
\int\mathrm{d}^3x\,|\boldsymbol{x}\rangle\langle\boldsymbol{x}|=1
$$

座標状態と運動量状態の内積は，問題文の関係の複素共役をとります。

$$
\begin{aligned}
\langle\boldsymbol{p}|\boldsymbol{x}\rangle
&=\langle\boldsymbol{x}|\boldsymbol{p}\rangle^*\\
&=\frac{1}{(2\pi)^{3/2}}e^{-i\boldsymbol{p}\cdot\boldsymbol{x}}
\end{aligned}
$$

まず $\langle\boldsymbol{p}|\psi\rangle$ に完全性関係を挿入します。

$$
\begin{aligned}
\langle\boldsymbol{p}|\psi\rangle &= \int \mathrm{d}^3 x\,\langle\boldsymbol{p}|\boldsymbol{x}\rangle\langle\boldsymbol{x}|\psi\rangle \\
&= \frac{1}{(2\pi)^{3/2}}\int \mathrm{d}^3 x\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x}}\langle\boldsymbol{x}|\psi\rangle
\end{aligned}
$$

次に $\langle\boldsymbol{p}|\hat{O}|\boldsymbol{p}'\rangle$ に座標固有状態の完全性関係を $\hat{O}$ の両側から挿入します。

$$
\begin{aligned}
\langle\boldsymbol{p}|\hat{O}|\boldsymbol{p}'\rangle &= \iint \mathrm{d}^3 x\,\mathrm{d}^3 x'\,\langle\boldsymbol{p}|\boldsymbol{x}\rangle\langle\boldsymbol{x}|\hat{O}|\boldsymbol{x}'\rangle\langle\boldsymbol{x}'|\boldsymbol{p}'\rangle \\
&= \frac{1}{(2\pi)^3}\iint \mathrm{d}^3 x\,\mathrm{d}^3 x'\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x} + i\boldsymbol{p}'\cdot\boldsymbol{x}'}\langle\boldsymbol{x}|\hat{O}|\boldsymbol{x}'\rangle
\end{aligned}
$$



### (2)
設問1の第2式に $\langle\boldsymbol{x}|\hat{V}|\boldsymbol{x}'\rangle = -\dfrac{\lambda}{2m} g(\boldsymbol{x}) g(\boldsymbol{x}')$ を代入します。

$$
\begin{aligned}
\langle\boldsymbol{p}|\hat{V}|\boldsymbol{p}'\rangle &= \frac{1}{(2\pi)^3}\iint \mathrm{d}^3 x\,\mathrm{d}^3 x'\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x} + i\boldsymbol{p}'\cdot\boldsymbol{x}'}\left(-\frac{\lambda}{2m} g(\boldsymbol{x}) g(\boldsymbol{x}')\right) \\
&= -\frac{1}{(2\pi)^3}\frac{\lambda}{2m}\left(\int \mathrm{d}^3 x\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x}} g(\boldsymbol{x})\right)\left(\int \mathrm{d}^3 x'\, e^{-i(-\boldsymbol{p}')\cdot\boldsymbol{x}'} g(\boldsymbol{x}')\right)
\end{aligned}
$$

ここで 

$$
h(\boldsymbol{p}) \equiv \int \mathrm{d}^3 x\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x}} g(\boldsymbol{x})
$$

 と定義すれば，次式が得られます。

$$
\langle\boldsymbol{p}|\hat{V}|\boldsymbol{p}'\rangle = -\frac{1}{(2\pi)^3}\frac{\lambda}{2m} h(\boldsymbol{p}) h(-\boldsymbol{p}')
$$

### (3)
運動量表示のシュレーディンガー方程式に $E = -\dfrac{\nu^2}{2m}$ と設問2の結果を代入します。

$$
\frac{\boldsymbol{p}^2}{2m}\langle\boldsymbol{p}|\psi\rangle - \frac{1}{(2\pi)^3}\frac{\lambda}{2m} h(\boldsymbol{p})\int \mathrm{d}^3 p'\, h(-\boldsymbol{p}')\langle\boldsymbol{p}'|\psi\rangle = -\frac{\nu^2}{2m}\langle\boldsymbol{p}|\psi\rangle
$$

$\nu^2$ の項を左辺に，積分の項を右辺に移します。

$$
\frac{\boldsymbol{p}^2 + \nu^2}{2m}\langle\boldsymbol{p}|\psi\rangle = \frac{1}{(2\pi)^3}\frac{\lambda}{2m} h(\boldsymbol{p})\int \mathrm{d}^3 p'\, h(-\boldsymbol{p}')\langle\boldsymbol{p}'|\psi\rangle
$$

右辺の積分は $\boldsymbol{p}$ によらない定数なので，

$$
C \equiv \frac{\lambda}{(2\pi)^3}\int \mathrm{d}^3 p'\, h(-\boldsymbol{p}')\langle\boldsymbol{p}'|\psi\rangle
$$

 とおきます。両辺に $2m$ を掛けて $\boldsymbol{p}^2 + \nu^2 > 0$ で割ると，次式が得られます。

$$
\langle\boldsymbol{p}|\psi\rangle = C\frac{h(\boldsymbol{p})}{\boldsymbol{p}^2 + \nu^2}
$$

### (4)
$p = |\boldsymbol{p}|$，$r = |\boldsymbol{x}|$ とおき，$\boldsymbol{p}$ の向きを極軸とする球座標 $(r, \theta, \phi)$ を用いて $h(\boldsymbol{p})$ を計算します。

$$
\begin{aligned}
h(\boldsymbol{p}) &= \int \mathrm{d}^3 x\, e^{-i\boldsymbol{p}\cdot\boldsymbol{x}}\frac{e^{-\mu r}}{4\pi r} \\
&= \int_0^{\infty} r^2\,\mathrm{d}r \int_0^{\pi}\sin\theta\,\mathrm{d}\theta \int_0^{2\pi}\mathrm{d}\phi\, e^{-ipr\cos\theta}\frac{e^{-\mu r}}{4\pi r} \\
&= \frac{1}{2}\int_0^{\infty} r e^{-\mu r}\left(\int_{-1}^{1} e^{-ipr t}\,\mathrm{d}t\right)\mathrm{d}r \\
&= \frac{1}{2}\int_0^{\infty} r e^{-\mu r}\left[\frac{e^{-ipr t}}{-ipr}\right]_{-1}^{1}\mathrm{d}r \\
&= \frac{1}{2ip}\int_0^{\infty} \left(e^{-(\mu - ip) r} - e^{-(\mu + ip) r}\right)\mathrm{d}r \\
&= \frac{1}{2ip}\left(\frac{1}{\mu - ip} - \frac{1}{\mu + ip}\right) \\
&= \frac{1}{2ip}\cdot\frac{2ip}{\mu^2 + p^2} \\
&= \frac{1}{\boldsymbol{p}^2 + \mu^2}
\end{aligned}
$$

ここで $t=\cos\theta$ と置換しました。$p=0$ では角度積分を先に行うと，次の式になります。

$$
\begin{aligned}
h(\boldsymbol{0})&=\int_0^\infty re^{-\mu r}\,\mathrm{d}r\\
&=\frac1{\mu^2}
\end{aligned}
$$

したがって $p=0$ でも同じ式に一致します。

### (5)
設問4より 

$$
\begin{aligned}
h(-\boldsymbol{p}') &= h(\boldsymbol{p}') \\
&= \dfrac{1}{(\boldsymbol{p}')^2 + \mu^2}
\end{aligned}
$$

 です。設問3の波動関数を定数 $C$ の定義式に代入します。

$$
\begin{aligned}
C &= \frac{\lambda}{(2\pi)^3}\int \mathrm{d}^3 p'\, h(-\boldsymbol{p}')\cdot C\frac{h(\boldsymbol{p}')}{(\boldsymbol{p}')^2 + \nu^2} \\
&= \frac{\lambda C}{(2\pi)^3}\int \mathrm{d}^3 p'\,\frac{1}{\bigl((\boldsymbol{p}')^2 + \nu^2\bigr)\bigl((\boldsymbol{p}')^2 + \mu^2\bigr)^2}
\end{aligned}
$$

束縛状態が存在するには $C \neq 0$ である必要があるため，両辺を $C$ で割り，与えられた積分公式と $\mu > 0$ を用います。

$$
1=\frac{\lambda}{8\pi\mu(\mu+|\nu|)^2}
$$

$\mu+|\nu|>0$ なので，正の平方根をとります。

$$
(\mu+|\nu|)^2=\frac{\lambda}{8\pi\mu},
$$

$$
\mu+|\nu|=\sqrt{\frac{\lambda}{8\pi\mu}}
$$

$|\nu|$ について解くと，次の式になります。

$$
|\nu|=\sqrt{\frac{\lambda}{8\pi\mu}}-\mu
$$

束縛状態が存在するためには $E = -\dfrac{\nu^2}{2m} < 0$ すなわち $|\nu| > 0$ が必要です。

$$
\sqrt{\frac{\lambda}{8\pi\mu}}>\mu
$$

$\lambda$ に対する条件は次のとおりです。

$$
\lambda>8\pi\mu^3
$$

$$
\finalanswer{|\nu| = \sqrt{\frac{\lambda}{8\pi\mu}} - \mu, \qquad \lambda > 8\pi\mu^3}
$$

### (6)
運動量固有状態の完全性関係 $\displaystyle\int \mathrm{d}^3 p\,|\boldsymbol{p}\rangle\langle\boldsymbol{p}| = 1$ を用いて，座標表示の波動関数を求めます。

$$
\begin{aligned}
\langle\boldsymbol{x}|\psi\rangle &= \int \mathrm{d}^3 p\,\langle\boldsymbol{x}|\boldsymbol{p}\rangle\langle\boldsymbol{p}|\psi\rangle \\
&= \frac{C}{(2\pi)^{3/2}}\int \mathrm{d}^3 p\,\frac{e^{i\boldsymbol{p}\cdot\boldsymbol{x}}}{(\boldsymbol{p}^2 + \nu^2)(\boldsymbol{p}^2 + \mu^2)}
\end{aligned}
$$

設問4の結果を逆フーリエ変換すると，任意の正定数 $\alpha > 0$ に対して

$$
\int \frac{\mathrm{d}^3 p}{(2\pi)^3}\frac{e^{i\boldsymbol{p}\cdot\boldsymbol{x}}}{\boldsymbol{p}^2 + \alpha^2} = \frac{e^{-\alpha r}}{4\pi r}
$$

が成り立ちます。$|\nu| \neq \mu$ のとき被積分関数を部分分数に分解してこの公式を用います。

$$
\begin{aligned}
\langle\boldsymbol{x}|\psi\rangle &= \frac{(2\pi)^{3/2} C}{\mu^2 - \nu^2}\int \frac{\mathrm{d}^3 p}{(2\pi)^3} e^{i\boldsymbol{p}\cdot\boldsymbol{x}}\left(\frac{1}{\boldsymbol{p}^2 + \nu^2} - \frac{1}{\boldsymbol{p}^2 + \mu^2}\right) \\
&= \frac{(2\pi)^{3/2} C}{4\pi(\mu^2 - \nu^2)}\,\frac{e^{-|\nu| r} - e^{-\mu r}}{r}
\end{aligned}
$$

$|\nu| = \mu$ のときは $|\nu| \to \mu$ の極限をとることで $\langle\boldsymbol{x}|\psi\rangle = \dfrac{(2\pi)^{3/2} C}{8\pi\mu} e^{-\mu r}$ となります。

波動関数の全体の定数を選び，$a=|\nu|$ とおいて，形を表す関数を次のように定めます。

$$
f(r)=\begin{cases}
\dfrac{e^{-ar}-e^{-\mu r}}{(\mu-a)r} & (a\ne\mu),\\
e^{-\mu r} & (a=\mu)
\end{cases}
$$

どちらの場合も $f(0)=1$ です。次の積分表示から，$r>0$ で正の値をとり，単調に減少して $0$ に近づくことが分かります。

$$
\begin{aligned}
f(r)&=\int_0^1 e^{-[a+(\mu-a)s]r}\,\mathrm{d}s,\\
f'(r)&=-\int_0^1 [a+(\mu-a)s]e^{-[a+(\mu-a)s]r}\,\mathrm{d}s<0
\end{aligned}
$$

この符号と定数の選択での概略を次の図に示します。

<figure class="problem-figure" markdown>
![座標表示での束縛状態の波動関数psi(r)の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H23_butsuri_1-s-light.svg#only-light)
![座標表示での束縛状態の波動関数psi(r)の概略](../../../docs/assets/figures/pastexam-todai-ributsu/H23_butsuri_1-s-dark.svg#only-dark)
<figcaption markdown="span">座標表示での束縛状態の波動関数 $\psi(r)$ の動径依存性。原点 $r = 0$ で有限値をとり，単調に減衰する。</figcaption>
</figure>

$$
\finalanswer{\langle\boldsymbol{x}|\psi\rangle \propto \frac{e^{-|\nu| r} - e^{-\mu r}}{r} \quad (|\nu| \neq \mu), \qquad \langle\boldsymbol{x}|\psi\rangle \propto e^{-\mu r} \quad (|\nu| = \mu)}
$$
