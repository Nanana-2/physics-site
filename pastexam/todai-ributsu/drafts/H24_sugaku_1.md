---
title: 東大理物 平成24年度 数学 第1問：パウリ行列の指数関数と2次正方行列の性質
tags:
  - 院試過去問
  - 東大理物
  - 物理数学
  - 線形代数
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成24年度
exam_subject: 数学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成24年度 数学 第1問：パウリ行列の指数関数と2次正方行列の性質

## 問題

(1) 以下の設問に答えよ。ただし単位行列 $I$ およびパウリ行列 $\sigma_j$（$j = 1, 2, 3$）を

$$
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

で定義する。$i$ は虚数単位である。

(i) パウリ行列の積 $\sigma_j \sigma_k$（$j, k = 1, 2, 3$）を求めよ。

(ii) 実 3 元ベクトル $\boldsymbol{v}$ に対して行列 $S(\boldsymbol{v})$ を $S(\boldsymbol{v}) = \boldsymbol{v} \cdot \boldsymbol{\sigma} = v_1 \sigma_1 + v_2 \sigma_2 + v_3 \sigma_3$ で定義する。$S$ の積 $S(\boldsymbol{a}) S(\boldsymbol{b})$ を単位行列 $I$ とパウリ行列 $\sigma_j$ の線形結合で表せ。

(iii) 実 3 元単位ベクトル $\boldsymbol{n}$ および実数 $\theta$ に対して，行列 $X(\boldsymbol{n}, \theta)$ を

$$
X(\boldsymbol{n}, \theta) = e^{-i\theta S(\boldsymbol{n})}
$$

で定義する。ただし行列 $A$ に対して

$$
e^A = \sum_{k=0}^{\infty} \frac{A^k}{k!}
$$

である。$X(\boldsymbol{n}, \theta)$ を単位行列 $I$ とパウリ行列 $\sigma_j$ の線形結合で表せ。

(iv) $X(\boldsymbol{n}, \theta) S(\boldsymbol{v}) X(\boldsymbol{n}, -\theta)$ が $S(\boldsymbol{v}')$ の形に表せることを示し，$\boldsymbol{v}'$ を $\boldsymbol{n}$，$\boldsymbol{v}$，$\boldsymbol{n} \times \boldsymbol{v}$ の線形結合で表せ。ただし $\times$ はベクトル積（外積）を表す。

(v) $\boldsymbol{n}$ と $\boldsymbol{v}$ が直交しているとき，$0 \le \theta \le 2\pi$ において設問 (iv) の $\boldsymbol{v}'$ がどのように変化するか説明せよ。

(2) 2 行 2 列の複素行列すべての集合を $G$ とする。また，$H$ を 2 行 2 列のエルミート行列の集合（$X \in G$ かつ $X^{\dagger} = X$ を満たす $X$ の集合）とし，$U$ を 2 行 2 列のユニタリー行列の集合（$X \in G$ かつ $X^{\dagger} X = X X^{\dagger} = I$ を満たす $X$ の集合）とする。ただし $X^{\dagger}$ は $X$ のエルミート共役（転置の複素共役）を表す。以下の各命題について真偽を答え，「真」の場合は命題を証明し，「偽」の場合には具体的な反例を 1 つ示せ。

(a) $A \in U$ かつ $B \in U$ ならば，$AB \in U$ である。

(b) $A \in H$ かつ $B \in H$ ならば，$AB \in H$ である。

(c) $A \in H$ ならば $A \in U$ である。

(d) $A \in H$ かつ $A \in U$ ならば，$A = I$ である。

(e) $X \in G$ かつ $X^2 = O$ ならば，$X = O$ である（ただし $O$ は全ての成分が 0 の行列）。

(f) $X \in G$ かつ $X^3 = O$ ならば，$X^2 = O$ である。

> 出典：東京大学大学院理学系研究科物理学専攻 平成24年度修士課程入学試験 数学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
単位ベクトル $\boldsymbol{n}$ に対して $S(\boldsymbol{n})^2 = I$ が成り立つため，行列の指数関数 $e^{-i\theta S(\boldsymbol{n})}$ のべき級数は偶数次と奇数次に分かれて $\cos\theta\,I - i\sin\theta\,S(\boldsymbol{n})$ と有限の和にまとまります。これを用いると $X(\boldsymbol{n}, \theta) S(\boldsymbol{v}) X(\boldsymbol{n}, -\theta)$ が 3 次元空間の回転を表すことが積の公式だけから計算することができます。

後半の真偽判定では，エルミート共役の性質 $(AB)^{\dagger} = B^{\dagger} A^{\dagger}$ や 2 次正方行列のケーリー・ハミルトンの定理を用いると証明と反例の構成が短くまとまります。
</div>

### (1)(i)
定義に従って各積を直接計算します。

$$
\begin{aligned}
\sigma_1^2 &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \\
\sigma_2^2 &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \\
\sigma_3^2 &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
\end{aligned}
$$

$$
\begin{aligned}
\sigma_1 \sigma_2 &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = i\sigma_3, \qquad \sigma_2 \sigma_1 = -i\sigma_3 \\
\sigma_2 \sigma_3 &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} = i\sigma_1, \qquad \sigma_3 \sigma_2 = -i\sigma_1 \\
\sigma_3 \sigma_1 &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = i\sigma_2, \qquad \sigma_1 \sigma_3 = -i\sigma_2
\end{aligned}
$$

クロネッカーのデルタ $\delta_{jk}$ とレビ・チビタ記号 $\epsilon_{jk\ell}$ を用いると，次のように 1 つの式にまとめられます。

$$
\finalanswer{\sigma_j \sigma_k = \delta_{jk} I + i\sum_{\ell=1}^3 \epsilon_{jk\ell}\sigma_\ell \qquad (j, k = 1, 2, 3)}
$$

### (1)(ii)
設問 (1)(i) の結果を用いて $S(\boldsymbol{a}) S(\boldsymbol{b})$ を展開します。

$$
\begin{aligned}
S(\boldsymbol{a}) S(\boldsymbol{b}) &= \sum_{j=1}^3 \sum_{k=1}^3 a_j b_k \sigma_j \sigma_k \\
&= \sum_{j=1}^3 \sum_{k=1}^3 a_j b_k \left(\delta_{jk} I + i\sum_{\ell=1}^3 \epsilon_{jk\ell}\sigma_\ell\right) \\
&= \left(\sum_{j=1}^3 a_j b_j\right) I + i\sum_{\ell=1}^3 \left(\sum_{j=1}^3 \sum_{k=1}^3 \epsilon_{\ell jk} a_j b_k\right)\sigma_\ell \\
&= (\boldsymbol{a} \cdot \boldsymbol{b}) I + i(\boldsymbol{a} \times \boldsymbol{b}) \cdot \boldsymbol{\sigma}
\end{aligned}
$$

$$
\finalanswer{S(\boldsymbol{a}) S(\boldsymbol{b}) = (\boldsymbol{a} \cdot \boldsymbol{b}) I + i\sum_{j=1}^3 (\boldsymbol{a} \times \boldsymbol{b})_j \sigma_j}
$$

### (1)(iii)
$\boldsymbol{n}$ は単位ベクトルなので $\boldsymbol{n} \cdot \boldsymbol{n} = 1$，$\boldsymbol{n} \times \boldsymbol{n} = \boldsymbol{0}$ です。設問 (1)(ii) より $S(\boldsymbol{n})^2 = I$ が成り立ちます。よって非負整数 $m$ に対して $S(\boldsymbol{n})^{2m} = I$，$S(\boldsymbol{n})^{2m+1} = S(\boldsymbol{n})$ です。

指数関数の定義の級数を偶数次と奇数次に分けます。

$$
\begin{aligned}
X(\boldsymbol{n}, \theta) &= \sum_{k=0}^{\infty} \frac{(-i\theta)^k}{k!} S(\boldsymbol{n})^k \\
&= \sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m}}{(2m)!} I - i\sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m+1}}{(2m+1)!} S(\boldsymbol{n}) \\
&= \cos\theta\,I - i\sin\theta\,S(\boldsymbol{n}) \\
&= \cos\theta\,I - i\sin\theta\left(n_1 \sigma_1 + n_2 \sigma_2 + n_3 \sigma_3\right)
\end{aligned}
$$

$$
\finalanswer{X(\boldsymbol{n}, \theta) = \cos\theta\,I - i\sin\theta\left(n_1 \sigma_1 + n_2 \sigma_2 + n_3 \sigma_3\right)}
$$

### (1)(iv)
設問 (1)(iii) より $X(\boldsymbol{n}, -\theta) = \cos\theta\,I + i\sin\theta\,S(\boldsymbol{n})$ です。積 $X(\boldsymbol{n}, \theta) S(\boldsymbol{v}) X(\boldsymbol{n}, -\theta)$ を展開します。

$$
\begin{aligned}
X(\boldsymbol{n}, \theta) S(\boldsymbol{v}) X(\boldsymbol{n}, -\theta) &= \bigl(\cos\theta\,I - i\sin\theta\,S(\boldsymbol{n})\bigr) S(\boldsymbol{v}) \bigl(\cos\theta\,I + i\sin\theta\,S(\boldsymbol{n})\bigr) \\
&= \cos^2\theta\,S(\boldsymbol{v}) + i\sin\theta\cos\theta\bigl(S(\boldsymbol{v}) S(\boldsymbol{n}) - S(\boldsymbol{n}) S(\boldsymbol{v})\bigr) + \sin^2\theta\,S(\boldsymbol{n}) S(\boldsymbol{v}) S(\boldsymbol{n})
\end{aligned}
$$

右辺第 2 項の交換子と第 3 項を，設問 (1)(ii) の公式 $S(\boldsymbol{a}) S(\boldsymbol{b}) = (\boldsymbol{a}\cdot\boldsymbol{b})I + i S(\boldsymbol{a}\times\boldsymbol{b})$ を用いて計算します。

$$
\begin{aligned}
S(\boldsymbol{v}) S(\boldsymbol{n}) - S(\boldsymbol{n}) S(\boldsymbol{v}) &= 2i S(\boldsymbol{v} \times \boldsymbol{n}) \\
&= -2i S(\boldsymbol{n} \times \boldsymbol{v})
\end{aligned}
$$

$$
\begin{aligned}
S(\boldsymbol{n}) S(\boldsymbol{v}) S(\boldsymbol{n}) &= \bigl((\boldsymbol{n}\cdot\boldsymbol{v})I + i S(\boldsymbol{n}\times\boldsymbol{v})\bigr) S(\boldsymbol{n}) \\
&= (\boldsymbol{n}\cdot\boldsymbol{v}) S(\boldsymbol{n}) + i\bigl((\boldsymbol{n}\times\boldsymbol{v})\cdot\boldsymbol{n}\,I + i S((\boldsymbol{n}\times\boldsymbol{v})\times\boldsymbol{n})\bigr) \\
&= (\boldsymbol{n}\cdot\boldsymbol{v}) S(\boldsymbol{n}) - S\bigl(\boldsymbol{v} - (\boldsymbol{n}\cdot\boldsymbol{v})\boldsymbol{n}\bigr) \\
&= 2(\boldsymbol{n}\cdot\boldsymbol{v}) S(\boldsymbol{n}) - S(\boldsymbol{v})
\end{aligned}
$$

ここでベクトル三重積の公式 $(\boldsymbol{n}\times\boldsymbol{v})\times\boldsymbol{n} = (\boldsymbol{n}\cdot\boldsymbol{n})\boldsymbol{v} - (\boldsymbol{n}\cdot\boldsymbol{v})\boldsymbol{n} = \boldsymbol{v} - (\boldsymbol{n}\cdot\boldsymbol{v})\boldsymbol{n}$ を用いました。これらを元の式に代入してまとめます。

$$
\begin{aligned}
X(\boldsymbol{n}, \theta) S(\boldsymbol{v}) X(\boldsymbol{n}, -\theta) &= (\cos^2\theta - \sin^2\theta) S(\boldsymbol{v}) + 2\sin^2\theta\,(\boldsymbol{n}\cdot\boldsymbol{v}) S(\boldsymbol{n}) + 2\sin\theta\cos\theta\,S(\boldsymbol{n}\times\boldsymbol{v}) \\
&= S\bigl(\cos(2\theta)\,\boldsymbol{v} + (1 - \cos(2\theta))(\boldsymbol{n}\cdot\boldsymbol{v})\boldsymbol{n} + \sin(2\theta)\,(\boldsymbol{n}\times\boldsymbol{v})\bigr)
\end{aligned}
$$

したがって $X(\boldsymbol{n}, \theta) S(\boldsymbol{v}) X(\boldsymbol{n}, -\theta) = S(\boldsymbol{v}')$ の形に表され，$\boldsymbol{v}'$ は次のとおりです。

$$
\finalanswer{\boldsymbol{v}' = \cos(2\theta)\,\boldsymbol{v} + \bigl(1 - \cos(2\theta)\bigr)(\boldsymbol{n}\cdot\boldsymbol{v})\boldsymbol{n} + \sin(2\theta)\,(\boldsymbol{n}\times\boldsymbol{v})}
$$

### (1)(v)
$\boldsymbol{n}$ と $\boldsymbol{v}$ が直交するとき $\boldsymbol{n}\cdot\boldsymbol{v} = 0$ なので，設問 (1)(iv) の式は次のようになります。

$$
\boldsymbol{v}' = \cos(2\theta)\,\boldsymbol{v} + \sin(2\theta)\,(\boldsymbol{n}\times\boldsymbol{v})
$$

$\boldsymbol{v}$ と $\boldsymbol{n}\times\boldsymbol{v}$ は互いに直交し，同じ大きさ $|\boldsymbol{v}|$ をもちます。したがって $\boldsymbol{v}'$ は，$\boldsymbol{n}$ に垂直な平面内で長さを $|\boldsymbol{v}|$ に保ったまま，$\boldsymbol{n}$ を回転軸として右ねじの向きに角 $2\theta$ だけ回転したベクトルです。$\theta$ が $0$ から $2\pi$ まで変化すると回転角 $2\theta$ は $0$ から $4\pi$ まで変化するため，$\boldsymbol{v}'$ は $\boldsymbol{n}$ の周りを右ねじの向きにちょうど 2 周します。

### (2)(a)
**真**です。$A, B \in U$ より $A^{\dagger} A = A A^{\dagger} = I$，$B^{\dagger} B = B B^{\dagger} = I$ が成り立ちます。積 $AB$ について $(AB)^{\dagger} = B^{\dagger} A^{\dagger}$ を用いて計算します。

$$
\begin{aligned}
(AB)^{\dagger}(AB) &= B^{\dagger} A^{\dagger} A B \\
&= B^{\dagger} I B \\
&= B^{\dagger} B \\
&= I
\end{aligned}
$$

$$
\begin{aligned}
(AB)(AB)^{\dagger} &= A B B^{\dagger} A^{\dagger} \\
&= A I A^{\dagger} \\
&= A A^{\dagger} \\
&= I
\end{aligned}
$$

よって $AB \in U$ です。

### (2)(b)
**偽**です。反例として $A = \sigma_1$，$B = \sigma_2$ をとります。$A^{\dagger} = A$，$B^{\dagger} = B$ なので $A, B \in H$ です。しかし $AB = \sigma_1 \sigma_2 = i\sigma_3$ であり，

$$
(AB)^{\dagger} = -i\sigma_3 \neq i\sigma_3 = AB
$$

なので $AB \notin H$ です。

### (2)(c)
**偽**です。反例として零行列 $A = O$ をとります。$O^{\dagger} = O$ より $O \in H$ ですが，$O^{\dagger} O = O \neq I$ なので $O \notin U$ です。

### (2)(d)
**偽**です。反例として $A = -I$ をとります。$(-I)^{\dagger} = -I$ かつ $(-I)^{\dagger}(-I) = (-I)(-I)^{\dagger} = I$ より $A \in H$ かつ $A \in U$ ですが，$A \neq I$ です。

### (2)(e)
**偽**です。反例として $X = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ をとります。$X \neq O$ ですが，

$$
X^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O
$$

となります。

### (2)(f)
**真**です。$X$ の 2 つの固有値を $\lambda_1, \lambda_2$ とします。固有値 $\lambda_j$ に対する固有ベクトル $\boldsymbol{v} \neq \boldsymbol{0}$ に $X^3 = O$ を作用させると $\lambda_j^3 \boldsymbol{v} = \boldsymbol{0}$ より $\lambda_j^3 = 0$，すなわち $\lambda_1 = \lambda_2 = 0$ です。

よって $\operatorname{tr} X = \lambda_1 + \lambda_2 = 0$ かつ $\det X = \lambda_1 \lambda_2 = 0$ です。2 次正方行列 $X$ に対するケーリー・ハミルトンの定理より，

$$
\begin{aligned}
X^2 - (\operatorname{tr} X) X + (\det X) I &= O \\
X^2 &= O
\end{aligned}
$$

が成り立ちます。
