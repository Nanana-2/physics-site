---
title: 東大理物 平成14年度 数学 第1問：2次実対称行列の対角化と円周上の線形変形
tags:
  - 院試過去問
  - 東大理物
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成14年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。
---

# 東大理物 平成14年度 数学 第1問：2次実対称行列の対角化と円周上の線形変形

## 問題

$2\times 2$ の実行列：$A = \begin{pmatrix} 1 - \gamma\cos 2\phi & -\gamma\sin 2\phi \\ -\gamma\sin 2\phi & 1 + \gamma\cos 2\phi \end{pmatrix}$ に関する以下の設問に答えよ。ただし，$0 < \gamma < 1$ であるものとする。
{: .problem-lead }

(1) 行列 $A$ の固有値 $\lambda_+, \lambda_-$ を求めよ（$\lambda_+ > \lambda_-$ とする）。

(2) $\lambda_+$ と $\lambda_-$ に対応する規格化された固有ベクトル $\vec{w}_+, \vec{w}_-$ を求めよ。

(3) $U A U^{-1} = \begin{pmatrix} \lambda_- & 0 \\ 0 & \lambda_+ \end{pmatrix}$ のように $A$ を対角化する行列 $U$ を求めよ。また，この行列 $U$ が表す変換はどのような操作に対応しているか簡単に述べよ。

(4) 下図のように，単位円 C 上の点 P（$\cos\phi, \sin\phi$）において上述の行列 $A$ が定義されているものとし，この点 P を原点とした任意のベクトル $\vec{w}$ を点 P を原点としたベクトル $A\vec{w}$ へ変換する。この写像によって，図に点線で示された8つの円はどのように変形するか。答案用紙に簡単に図示して説明せよ。

<figure class="problem-figure" markdown>
![単位円C上の8つの点線の円と点Pにおけるベクトルw](../../assets/figures/pastexam-todai-ributsu/H14_sugaku_1-p-light.svg#only-light)
![単位円C上の8つの点線の円と点Pにおけるベクトルw](../../assets/figures/pastexam-todai-ributsu/H14_sugaku_1-p-dark.svg#only-dark)
<figcaption markdown="span">図1：単位円 C 上の8つの点線の円と，点 $\mathrm{P}(\cos\phi, \sin\phi)$ を原点とするベクトル $\vec{w}$。</figcaption>
</figure>

> 出典：東京大学大学院理学系研究科物理学専攻 平成14年度 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，図を描き直して小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
実対称行列 $A$ の固有多項式を解いて2つの実固有値を求め，倍角の公式を使って各固有ベクトルを偏角 $\phi$ で表します。

固有ベクトルを並べた直交行列の逆行列として対角化行列 $U$ を構成すると，$U$ が角度 $-\phi$ の回転行列であることがわかります。各点 $\mathrm{P}(\cos\phi, \sin\phi)$ における固有ベクトルの向きが単位円の動径方向と接線方向に対応することから，8つの円が楕円へ変形する向きと軸比が定まります。
</div>

### (1)

固有方程式 $\det(A - \lambda I) = 0$ を計算します。

$$
\begin{aligned}
\det(A - \lambda I) &= (1 - \lambda - \gamma\cos 2\phi)(1 - \lambda + \gamma\cos 2\phi) - (-\gamma\sin 2\phi)^2 \\
&= (1 - \lambda)^2 - \gamma^2\cos^2 2\phi - \gamma^2\sin^2 2\phi \\
&= (1 - \lambda)^2 - \gamma^2
\end{aligned}
$$

$\det(A - \lambda I) = 0$ より $(1 - \lambda)^2 = \gamma^2$ すなわち $\lambda = 1 \pm \gamma$ です。$0 < \gamma < 1$ および $\lambda_+ > \lambda_-$ より，固有値は次式となります。

$$
\finalanswer{\lambda_+ = 1 + \gamma, \qquad \lambda_- = 1 - \gamma}
$$

### (2)

まず固有値 $\lambda_+ = 1 + \gamma$ に対する固有ベクトル $\vec{w}_+ = \begin{pmatrix} x \\ y \end{pmatrix}$ を求めます。$A - (1 + \gamma)I$ を倍角の公式 $1 + \cos 2\phi = 2\cos^2\phi$，$1 - \cos 2\phi = 2\sin^2\phi$，$\sin 2\phi = 2\sin\phi\cos\phi$ で整理します。

$$
\begin{aligned}
A - (1 + \gamma)I &= -\gamma\begin{pmatrix} 1 + \cos 2\phi & \sin 2\phi \\ \sin 2\phi & 1 - \cos 2\phi \end{pmatrix} \\
&= -2\gamma\begin{pmatrix} \cos^2\phi & \sin\phi\cos\phi \\ \sin\phi\cos\phi & \sin^2\phi \end{pmatrix}
\end{aligned}
$$

$\bigl(A - (1 + \gamma)I\bigr)\vec{w}_+ = \vec{0}$ より $\cos\phi\,x + \sin\phi\,y = 0$ です。$|\vec{w}_+| = 1$ となるように規格化すると，符号の自由度を除いて次式が得られます。

$$
\vec{w}_+ = \begin{pmatrix} -\sin\phi \\ \cos\phi \end{pmatrix}
$$

次に固有値 $\lambda_- = 1 - \gamma$ に対する固有ベクトル $\vec{w}_- = \begin{pmatrix} x \\ y \end{pmatrix}$ を求めます。

$$
\begin{aligned}
A - (1 - \gamma)I &= \gamma\begin{pmatrix} 1 - \cos 2\phi & -\sin 2\phi \\ -\sin 2\phi & 1 + \cos 2\phi \end{pmatrix} \\
&= 2\gamma\begin{pmatrix} \sin^2\phi & -\sin\phi\cos\phi \\ -\sin\phi\cos\phi & \cos^2\phi \end{pmatrix}
\end{aligned}
$$

$\bigl(A - (1 - \gamma)I\bigr)\vec{w}_- = \vec{0}$ より $\sin\phi\,x - \cos\phi\,y = 0$ です。規格化すると，符号の自由度を除いて次式が得られます。

$$
\vec{w}_- = \begin{pmatrix} \cos\phi \\ \sin\phi \end{pmatrix}
$$

したがって，符号の自由度を除いて，規格化された固有ベクトルは次式となります。

$$
\finalanswer{\vec{w}_+ = \begin{pmatrix} -\sin\phi \\ \cos\phi \end{pmatrix}, \qquad \vec{w}_- = \begin{pmatrix} \cos\phi \\ \sin\phi \end{pmatrix}}
$$

### (3)

固有ベクトル $\vec{w}_-, \vec{w}_+$ をこの順に列に並べた直交行列を $P = (\vec{w}_-, \vec{w}_+)$ とおきます。

$$
P = \begin{pmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{pmatrix}
$$

$A\vec{w}_- = \lambda_-\vec{w}_-$ および $A\vec{w}_+ = \lambda_+\vec{w}_+$ より次式が成り立ちます。

$$
AP = P\begin{pmatrix} \lambda_- & 0 \\ 0 & \lambda_+ \end{pmatrix}
$$

$P$ は直交行列なので $P^{-1} = P^T$ です。両辺の左から $P^{-1}$ を掛けます。

$$
P^{-1} A P = \begin{pmatrix} \lambda_- & 0 \\ 0 & \lambda_+ \end{pmatrix}
$$

したがって $U = P^T$ とおくと，$U A U^{-1} = \begin{pmatrix} \lambda_- & 0 \\ 0 & \lambda_+ \end{pmatrix}$ を満たします。

$$
\finalanswer{U = \begin{pmatrix} \cos\phi & \sin\phi \\ -\sin\phi & \cos\phi \end{pmatrix}}
$$

行列 $U$ は角度 $-\phi$ の回転行列なので，2次元平面上のベクトルを原点まわりに時計回りに角度 $\phi$ だけ回転させる操作に対応します。すなわち，座標系を反時計回りに $\phi$ 回転させて動径方向を $x$ 軸，接線方向を $y$ 軸に合わせる操作です。

### (4)

点 $\mathrm{P}(\cos\phi, \sin\phi)$ において，固有値 $\lambda_- = 1 - \gamma$（$0 < \lambda_- < 1$）に対応する固有ベクトル $\vec{w}_- = (\cos\phi, \sin\phi)^T$ は単位円 C の動径方向を向いており，固有値 $\lambda_+ = 1 + \gamma$（$\lambda_+ > 1$）に対応する固有ベクトル $\vec{w}_+ = (-\sin\phi, \cos\phi)^T$ は単位円 C の接線方向を向いています。

点 P を原点とする任意のベクトル $\vec{w}$ を $\vec{w} = c_-\vec{w}_- + c_+\vec{w}_+$ と分解すると，変換後のベクトルは次式になります。

$$
A\vec{w} = (1 - \gamma)c_-\vec{w}_- + (1 + \gamma)c_+\vec{w}_+
$$

すなわち写像 $A$ は，各点 P を中心として動径方向に $1 - \gamma$ 倍に縮小し，接線方向に $1 + \gamma$ 倍に伸長する変形です。したがって，図に点線で示された半径 $r$ の8つの円は，それぞれ同じ中心 P をもち，単位円 C の接線方向に長半径 $(1 + \gamma)r$，動径方向に短半径 $(1 - \gamma)r$ をもつ8つの楕円へ変形します。変形前後の様子を次の図に示します。

<figure class="problem-figure" markdown>
![写像Aによる8つの円の楕円への変形](../../assets/figures/pastexam-todai-ributsu/H14_sugaku_1-s-light.svg#only-light)
![写像Aによる8つの円の楕円への変形](../../assets/figures/pastexam-todai-ributsu/H14_sugaku_1-s-dark.svg#only-dark)
<figcaption markdown="span">写像 $A$ による8つの点線の円（破線）から楕円（実線）への変形。各円は単位円 C の接線方向に $1 + \gamma$ 倍に伸び，動径方向に $1 - \gamma$ 倍に縮みます。</figcaption>
</figure>
