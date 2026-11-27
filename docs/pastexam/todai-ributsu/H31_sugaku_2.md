---
title: 東大理物 平成31年度 数学 第2問：微分演算子の固有値積とゼータ関数正則化
tags:
  - 院試過去問
  - 東大理物
  - 複素関数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成31年度
exam_subject: 数学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直しています。
---

# 東大理物 平成31年度 数学 第2問：微分演算子の固有値積とゼータ関数正則化

## 問題

$x$ 軸上の区間 $[0, \pi]$ で定義された関数に作用する以下の演算子を考える。

$$
H_\alpha = -\frac{d^2}{dx^2} - m_\alpha^2
$$

ここで，$m_\alpha$ は正の実数定数，$\alpha = 1, 2$ である。$H_\alpha$ の $n$ 番目に小さい固有値を $\lambda_\alpha^{(n)}$，対応する固有関数を $f_\alpha^{(n)}(x)$ とする（$n = 1, 2, 3, \dots$）。

$$
H_\alpha f_\alpha^{(n)}(x) = \lambda_\alpha^{(n)} f_\alpha^{(n)}(x)
$$

固有関数 $f_\alpha^{(n)}(x)$ は $x = 0$ と $x = \pi$ で，それぞれ以下の境界条件を満たすものとする。

$$
\left.\frac{d f_\alpha^{(n)}(x)}{dx}\right|_{x=0} = 0,\qquad f_\alpha^{(n)}(\pi) = 0
$$

ただし，$f_\alpha^{(n)}(x) = 0$ という自明な解は考えない。

(1) $\lambda_\alpha^{(n)}$ と $f_\alpha^{(n)}(x)$ を求めよ。固有関数は規格化しなくてよい。

(2) $m_\alpha < \dfrac{1}{2}$ として，次の量 $D$ を計算することを考える。

$$
D = \prod_{n=1}^{\infty} \frac{\lambda_2^{(n)}}{\lambda_1^{(n)}}
$$

そのため，$s$ に関して解析的な関数 $Z(s)$ を導入する。

$$
Z(s) = \sum_{n=1}^{\infty} \left[\left(\lambda_2^{(n)}\right)^{-s} - \left(\lambda_1^{(n)}\right)^{-s}\right]
$$

（$s$ の実部が小さく上の無限和が収束しない領域では，$Z(s)$ は解析接続により与える。）以下，$s$ に関する微分を

$$
Z'(s) = \frac{d}{ds} Z(s)
$$

と表す。また，必要であれば以下の式を用いてもよい。

$$
\int_{C_0} \frac{dz}{z} = 2\pi i
$$

ただし，$C_0$ は $z$ の複素平面上で原点を反時計回りに1周する閉曲線，$i$ は虚数単位である。

(i) $\lambda$ を定数として，次の微分を実行せよ。

$$
\frac{d}{ds}\lambda^{-s}
$$

(ii) $D$ を $Z'(0)$ を用いて表せ。

(iii) $\lambda$ を $-m_\alpha^2$ より大きい実数定数として，以下の微分方程式と境界条件を満たす関数 $g_\alpha(x; \lambda)$ を求めよ。

$$
H_\alpha g_\alpha(x; \lambda) = \lambda g_\alpha(x; \lambda),\qquad g_\alpha(0; \lambda) = 1,\qquad \left.\frac{\partial g_\alpha(x; \lambda)}{\partial x}\right|_{x=0} = 0
$$

(iv) 前問で与えられた関数 $g_\alpha(x; \lambda)$ の $x = \pi$ における値を用いて

$$
\tilde{g}_\alpha(\lambda) = g_\alpha(x = \pi; \lambda)
$$

とする。$\lambda$ が複素数である場合，$\tilde{g}_\alpha(\lambda)$ は解析接続により与える。$\tilde{g}_\alpha(\lambda)$ のゼロ点は $\lambda = \lambda_\alpha^{(n)}\ (n = 1, 2, 3, \dots)$ であり，その近傍で $\tilde{g}_\alpha(\lambda) = k_\alpha^{(n)}\left(\lambda - \lambda_\alpha^{(n)}\right) + \mathcal{O}\!\left[\left(\lambda - \lambda_\alpha^{(n)}\right)^2\right]$（$k_\alpha^{(n)}$ はゼロでない定数）となることに注意し，以下の関係式が成り立つことを示すとともに定数 $A$ を求めよ。

$$
Z(s) = A \int_C \lambda^{-s} \left[\frac{1}{\tilde{g}_2(\lambda)}\frac{d\tilde{g}_2(\lambda)}{d\lambda} - \frac{1}{\tilde{g}_1(\lambda)}\frac{d\tilde{g}_1(\lambda)}{d\lambda}\right] d\lambda
$$

ただし，積分経路 $C$ は $\lambda$ の複素平面上で全ての固有値 $\lambda_1^{(n)}, \lambda_2^{(n)}\ (n = 1, 2, 3, \dots)$ を囲む実軸に沿った経路，$\lambda^{-s}$ のブランチカット（切断線）は原点 $O$ から実軸との角度 $\theta\ (\theta \neq 0)$ の方向に伸びる半直線とする（図1参照）。また $s$ の実部は上の積分が収束する程度に大きいとしてよい。

(v) $Z'(0)$ を $\tilde{g}_1(0)$ と $\tilde{g}_2(0)$ を用いて表せ。前問に与えられた積分において，経路を $C$ から $C_{\mathrm{in}}$ と $C_{\mathrm{out}}$ を合成した経路（図1参照）に変形できることを用いてよい。

(vi) $\tilde{g}_\alpha(0)$ を具体的に計算し，$D$ を $m_1$ と $m_2$ を用いて表せ。

<figure class="problem-figure" markdown>
![積分経路 C と変形経路 C_in, C_out およびブランチカット](../../assets/figures/pastexam-todai-ributsu/H31_sugaku_2-p-light.svg#only-light)
![積分経路 C と変形経路 C_in, C_out およびブランチカット](../../assets/figures/pastexam-todai-ributsu/H31_sugaku_2-p-dark.svg#only-dark)
<figcaption markdown="span">図1：積分経路 $C$（実線），$C_{\mathrm{in}}$（破線），および $C_{\mathrm{out}}$（点線）。図中の黒丸は $\lambda_1^{(n)},\ \lambda_2^{(n)}\ (n = 1, 2, 3, \dots)$，太い実線はブランチカット（切断線）を表す。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成31年度修士課程入学試験 数学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
$x=0$ の条件だけを満たす解 $g_\alpha(x;\lambda)$ を作ると，固有値は $g_\alpha(\pi;\lambda)=0$ となる $\lambda$ です。そのため，固有値についての和は，$\ln g_\alpha(\pi;\lambda)$ を $\lambda$ で微分した関数の極での留数の和として，複素積分で書くことができます。

固有値の積 $D$ は，対数をとると固有値の対数の和になり，ゼータ関数 $Z(s)$ の $s=0$ での微分で表されます。複素積分の経路を $\lambda^{-s}$ の切断線に沿って変形すると，$s=0$ の近くでも収束する積分になるので，$Z'(0)$ を求めることができます。
</div>

### (1)
固有値方程式は次のように書き換えられます。

$$
\frac{\mathrm{d}^2 f_\alpha}{\mathrm{d}x^2} + \left(\lambda + m_\alpha^2\right) f_\alpha = 0
$$

$\lambda + m_\alpha^2$ の符号で場合分けして調べます。

- $\lambda + m_\alpha^2 = 0$ のとき：一般解は $f_\alpha(x) = c_1 + c_2 x$。$f_\alpha'(0) = 0$ より $c_2 = 0$，$f_\alpha(\pi) = 0$ より $c_1 = 0$ となり，$f_\alpha(x) \equiv 0$ 以外の解はありません。
- $\lambda + m_\alpha^2 = -\mu^2 < 0\ (\mu > 0)$ のとき：一般解は $f_\alpha(x) = c_1\cosh(\mu x) + c_2\sinh(\mu x)$。$f_\alpha'(0) = 0$ より $c_2 = 0$， $f_\alpha(\pi) = c_1\cosh(\mu\pi) = 0$ より $c_1 = 0$ となり，$f_\alpha(x) \equiv 0$ 以外の解はありません。
- $\lambda + m_\alpha^2 = \kappa^2 > 0\ (\kappa > 0)$ のとき：一般解は $f_\alpha(x) = c_1\cos(\kappa x) + c_2\sin(\kappa x)$。 $f_\alpha'(0) = \kappa c_2 = 0$ より $c_2 = 0$， $f_\alpha(\pi) = c_1\cos(\kappa\pi) = 0$ より $c_1 \neq 0$ となる条件は $\cos(\kappa\pi) = 0$，すなわち $\kappa = n - \dfrac{1}{2}\ (n = 1, 2, 3, \dots)$ です。

よって

$$
\begin{aligned}
\lambda_\alpha^{(n)} &= \kappa^2 - m_\alpha^2 \\
&= \left(n - \dfrac{1}{2}\right)^2 - m_\alpha^2
\end{aligned}
$$

となります。対応する固有関数は $f_\alpha^{(n)}(x) = \cos\left[\left(n - \dfrac{1}{2}\right)x\right]$ です。固有関数には，$0$ でない定数倍の任意性があります。したがって，

$$
\finalanswer{\lambda_\alpha^{(n)} = \left(n - \frac{1}{2}\right)^2 - m_\alpha^2,\qquad f_\alpha^{(n)}(x) = \cos\left[\left(n - \frac{1}{2}\right)x\right] \qquad (n = 1, 2, 3, \dots)}
$$

### (2)
(i) $\lambda^{-s} = e^{-s\ln\lambda}$ を $s$ で微分します。

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}s}\lambda^{-s} &= \frac{\mathrm{d}}{\mathrm{d}s}e^{-s\ln\lambda} \\
&= -\lambda^{-s}\ln\lambda
\end{aligned}
$$

したがって，

$$
\finalanswer{\frac{\mathrm{d}}{\mathrm{d}s}\lambda^{-s}=-\lambda^{-s}\ln\lambda}
$$

(ii) (i) の結果を用いて $Z(s)$ を $s$ で微分します。

$$
Z'(s) = -\sum_{n=1}^{\infty} \left[\left(\lambda_2^{(n)}\right)^{-s}\ln\lambda_2^{(n)} - \left(\lambda_1^{(n)}\right)^{-s}\ln\lambda_1^{(n)}\right]
$$

解析接続された $Z(s)$ の $s=0$ での微分は，次のように $D$ の対数と結び付きます。

$$
\begin{aligned}
Z'(0) &= -\sum_{n=1}^{\infty} \left(\ln\lambda_2^{(n)} - \ln\lambda_1^{(n)}\right) \\
&= -\ln\left(\prod_{n=1}^{\infty}\frac{\lambda_2^{(n)}}{\lambda_1^{(n)}}\right) \\
&= -\ln D
\end{aligned}
$$

よって $D = e^{-Z'(0)}$ です。したがって，

$$
\finalanswer{D = e^{-Z'(0)}}
$$

(iii) $\lambda > -m_\alpha^2$ より $\kappa = \sqrt{\lambda + m_\alpha^2} > 0$ とおくと，微分方程式は $\dfrac{\partial^2 g_\alpha}{\partial x^2} + \kappa^2 g_\alpha = 0$ です。一般解は $g_\alpha(x; \lambda) = c_1\cos(\kappa x) + c_2\sin(\kappa x)$ となります。

境界条件 $\left.\dfrac{\partial g_\alpha}{\partial x}\right|_{x=0} = \kappa c_2 = 0$ より $c_2 = 0$， $g_\alpha(0; \lambda) = c_1 = 1$ です。したがって，

$$
\finalanswer{g_\alpha(x; \lambda) = \cos\left(\sqrt{\lambda + m_\alpha^2}\,x\right)}
$$

(iv) $\tilde{g}_\alpha(\lambda) = \cos\left(\pi\sqrt{\lambda + m_\alpha^2}\right)$ は $\lambda$ の整関数です。$\cos(\pi\sqrt z)$ のべき級数は $z$ の整数乗のみを含むため，分岐点はありません。

零点 $\lambda = \lambda_\alpha^{(n)}$ の近傍で $\tilde{g}_\alpha(\lambda) = k_\alpha^{(n)}\left(\lambda - \lambda_\alpha^{(n)}\right) + \mathcal{O}\!\left[\left(\lambda - \lambda_\alpha^{(n)}\right)^2\right]$ なので，その対数微分は $\lambda = \lambda_\alpha^{(n)}$ に留数 $1$ の1位の極をもちます。

$$
\begin{aligned}
\frac{1}{\tilde{g}_\alpha(\lambda)}\frac{\mathrm{d}\tilde{g}_\alpha(\lambda)}{\mathrm{d}\lambda} &= \frac{k_\alpha^{(n)} + \mathcal{O}\!\left(\lambda - \lambda_\alpha^{(n)}\right)}{k_\alpha^{(n)}\left(\lambda - \lambda_\alpha^{(n)}\right) + \mathcal{O}\!\left[\left(\lambda - \lambda_\alpha^{(n)}\right)^2\right]} \\
&= \frac{1}{\lambda - \lambda_\alpha^{(n)}} + \mathcal{O}(1)
\end{aligned}
$$

ここで $0 < m_\alpha < \dfrac{1}{2}$ よりすべての固有値 $\lambda_\alpha^{(n)}$ は正の実数であり，経路 $C$ はこれらを反時計回りに囲み，ブランチカットとは交わりません。$\lambda^{-s}$ は正の実軸上で正則なので，各極での留数は $\left(\lambda_2^{(n)}\right)^{-s}$ および $-\left(\lambda_1^{(n)}\right)^{-s}$ です。留数定理より，

$$
\begin{aligned}
\int_C \lambda^{-s} \left[\frac{1}{\tilde{g}_2(\lambda)}\frac{\mathrm{d}\tilde{g}_2(\lambda)}{\mathrm{d}\lambda} - \frac{1}{\tilde{g}_1(\lambda)}\frac{\mathrm{d}\tilde{g}_1(\lambda)}{\mathrm{d}\lambda}\right]\mathrm{d}\lambda &= 2\pi i \sum_{n=1}^{\infty} \left[\left(\lambda_2^{(n)}\right)^{-s} - \left(\lambda_1^{(n)}\right)^{-s}\right] \\
&= 2\pi i\,Z(s)
\end{aligned}
$$

が成り立ちます。よって $A = \dfrac{1}{2\pi i}$ です。したがって，

$$
\finalanswer{A = \frac{1}{2\pi i}}
$$

(v) $\lambda$ が正の実軸上で $\arg\lambda = 0$ となるように1価の分枝をとると，ブランチカットが $\arg\lambda = \theta\ (0 < \theta < \pi)$ にあるため，偏角の範囲は $\theta - 2\pi < \arg\lambda < \theta$ です。

- 経路 $C_{\mathrm{in}}$ はブランチカットの下側です。$r = \infty \to 0$ で積分します。$\lambda = r e^{i\theta}$ より $\lambda^{-s} = r^{-s} e^{-i\theta s}$。
- 経路 $C_{\mathrm{out}}$ はブランチカットの上側です。$r = 0 \to \infty$ で積分します。$\lambda = r e^{i(\theta - 2\pi)}$ より $\lambda^{-s} = r^{-s} e^{-i\theta s} e^{2\pi i s}$。

被積分関数の大括弧内は $\dfrac{\mathrm{d}}{\mathrm{d}\lambda}\ln\dfrac{\tilde{g}_2(\lambda)}{\tilde{g}_1(\lambda)}$ であり，ブランチカットをまたいでも1価正則なので，経路を $C_{\mathrm{in}} + C_{\mathrm{out}}$ に変形すると次のようになります。原点周りの微小円の寄与は $\operatorname{Re}s<1$ の範囲で $0$ になります。

$$
\begin{aligned}
Z(s)
&= \frac{1}{2\pi i}\left[\int_\infty^0 r^{-s} e^{-i\theta s}\,\frac{\mathrm{d}}{\mathrm{d}r}\ln\frac{\tilde{g}_2(re^{i\theta})}{\tilde{g}_1(re^{i\theta})}\,\mathrm{d}r
 + \int_0^\infty r^{-s} e^{-i\theta s} e^{2\pi i s}\,\frac{\mathrm{d}}{\mathrm{d}r}\ln\frac{\tilde{g}_2(re^{i\theta})}{\tilde{g}_1(re^{i\theta})}\,\mathrm{d}r\right] \\
&= \frac{e^{-i\theta s}\left(e^{2\pi i s} - 1\right)}{2\pi i}\int_0^\infty r^{-s}\,\frac{\mathrm{d}}{\mathrm{d}r}\ln\frac{\tilde{g}_2(re^{i\theta})}{\tilde{g}_1(re^{i\theta})}\,\mathrm{d}r
\end{aligned}
$$

ここで $r \to \infty$ の漸近挙動を確認します。$\theta \in (0, \pi)$ に対し $\operatorname{Im}\left(e^{i\theta/2}\right) > 0$ なので，$\sqrt{re^{i\theta} + m_\alpha^2} = \sqrt{r}\,e^{i\theta/2} + \dfrac{m_\alpha^2}{2\sqrt{r}}e^{-i\theta/2} + \mathcal{O}(r^{-3/2})$ より

$$
\frac{\tilde{g}_2(re^{i\theta})}{\tilde{g}_1(re^{i\theta})}
= \frac{\cos\left(\pi\sqrt{re^{i\theta} + m_2^2}\right)}{\cos\left(\pi\sqrt{re^{i\theta} + m_1^2}\right)}
\sim \exp\left[-i\pi\frac{m_2^2 - m_1^2}{2\sqrt{r}}e^{-i\theta/2}\right] \xrightarrow{r\to\infty} 1
$$

となり，$\ln\dfrac{\tilde{g}_2(re^{i\theta})}{\tilde{g}_1(re^{i\theta})} = \mathcal{O}(r^{-1/2}) \to 0$ です。したがって上の積分は $s = 0$ の近傍（$-1/2 < \operatorname{Re} s < 1$）で絶対収束し，$Z(s)$ の解析接続を与えます。

係数 $F(s) = \dfrac{e^{-i\theta s}(e^{2\pi i s} - 1)}{2\pi i}$ は $F(0) = 0$ かつ $F'(0) = \dfrac{2\pi i}{2\pi i} = 1$ を満たすため，$Z(s)$ を $s$ で微分して $s = 0$ を代入すると次式が得られます。

$$
\begin{aligned}
Z'(0) &= F'(0)\int_0^\infty \frac{\mathrm{d}}{\mathrm{d}r}\ln\frac{\tilde{g}_2(re^{i\theta})}{\tilde{g}_1(re^{i\theta})}\,\mathrm{d}r \\
&= \left[\ln\frac{\tilde{g}_2(re^{i\theta})}{\tilde{g}_1(re^{i\theta})}\right]_0^\infty \\
&= 0 - \ln\frac{\tilde{g}_2(0)}{\tilde{g}_1(0)} \\
&= \ln\frac{\tilde{g}_1(0)}{\tilde{g}_2(0)}
\end{aligned}
$$

したがって，

$$
\finalanswer{Z'(0) = \ln\frac{\tilde{g}_1(0)}{\tilde{g}_2(0)} = -\ln\frac{\tilde{g}_2(0)}{\tilde{g}_1(0)}}
$$

(vi) (iii), (iv) より $\tilde{g}_\alpha(\lambda) = \cos\left(\pi\sqrt{\lambda + m_\alpha^2}\right)$ なので，$\lambda = 0$ を代入すると

$$
\tilde{g}_\alpha(0) = \cos(\pi m_\alpha)
$$

となります。$0<m_\alpha<1/2$ より $\cos(\pi m_\alpha)>0$ です。これを (ii) と (v) の結果に代入します。

$$
\begin{aligned}
D &= e^{-Z'(0)} \\
&= \frac{\tilde{g}_2(0)}{\tilde{g}_1(0)} \\
&= \frac{\cos(\pi m_2)}{\cos(\pi m_1)}
\end{aligned}
$$

したがって，

$$
\finalanswer{\tilde{g}_\alpha(0) = \cos(\pi m_\alpha),\qquad D = \frac{\cos(\pi m_2)}{\cos(\pi m_1)}}
$$

<aside class="rigor-note" markdown>
余弦関数の無限積公式から結果を検算することができます。

$$
\begin{aligned}
\cos(\pi m)&=\prod_{n=1}^\infty\left(1-\frac{m^2}{(n-1/2)^2}\right)\\
\frac{\cos(\pi m_2)}{\cos(\pi m_1)}&=\prod_{n=1}^\infty\frac{(n-1/2)^2-m_2^2}{(n-1/2)^2-m_1^2}\\
&=D
\end{aligned}
$$

$0 < m_\alpha < 1/2$ では各因子が正で，因子の対数は $n\to\infty$ で $\mathcal O(n^{-2})$ です。この比の積自体は絶対収束します。
</aside>
