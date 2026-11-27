---
title: 東大理物 平成8年度 一般教育科目 物理学 第1問：同軸導体円筒の電場・静電容量と逆向き電流による磁場・磁気圧
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 一般教育科目 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成8年度 一般教育科目 物理学 第1問：同軸導体円筒の電場・静電容量と逆向き電流による磁場・磁気圧

## 問題

真空中に二つの無限に長い導体の円筒 $\mathrm{A}$（半径 $a$），および $\mathrm{B}$（半径 $b$）が同軸に配置されている。ただし，$a < b$ であり，円筒の厚さは無視できる。
{: .problem-lead }

(1) 円筒 $\mathrm{A}$ に単位長さあたり正電荷 $Q$ を与え，円筒 $\mathrm{B}$ を接地するとき，

(イ) 円筒 $\mathrm{A}$ と $\mathrm{B}$ の間および $\mathrm{B}$ の外側の電場を求めよ。また，そのおおよその様子を図示せよ。

(ロ) 二つの円筒間の単位長さあたりの静電容量を求めよ。

(2) 円筒の軸方向に一様に電流 $I$ を流す。電流の向きが円筒 $\mathrm{A}$ と $\mathrm{B}$ で逆向きの場合に，

(イ) 電流が円筒 $\mathrm{A}$ と $\mathrm{B}$ の間に作る磁束密度を求めよ。また，そのおおよその様子を図示せよ。

(ロ) 円筒 $\mathrm{A}$ の表面にはたらく圧力は，$\dfrac{\mu_0 I^2}{8\pi^2 a^2}$ であることを示せ。ただし，$\mu_0$ は真空の透磁率である。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 一般教育科目 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
無限に長い同軸導体円筒は円筒対称性をもつため，ガウスの法則から径方向の電場が，アンペールの法則から円周方向の磁束密度が求まります。外側の円筒が接地されていることで外側領域の電場は遮蔽されて $0$ になり，逆向き電流によって外側領域の磁場も打ち消されて $0$ になります。内円筒表面にはたらく磁気圧は，電流層を挟んだ磁場の平均値を用いる方法，あるいは磁気エネルギーに対する仮想仕事の原理のいずれからも導出します。
</div>

### (1)(イ)

円筒の共通中心軸を $z$ 軸とし，軸からの距離を $r$ とする円筒座標系 $(r, \phi, z)$ をとります。系の軸対称性と $z$ 方向の並進対称性から，電場 $\mathbf{E}$ は動径方向のみを向き，その大きさ $E(r)$ は $r$ のみに依存します。

半径 $r$，長さ $L$ の同軸円筒面をガウス面としてガウスの法則を用います。

まず円筒 $\mathrm{A}$ と $\mathrm{B}$ の間 $a < r < b$ では，ガウス面内部に含まれる電荷は円筒 $\mathrm{A}$ の電荷 $Q L$ です。

$$
2\pi r L \cdot E(r) = \frac{Q L}{\varepsilon_0}
$$

したがって $a < r < b$ における電場は外向き動径方向で，その大きさは次式となります。

$$
E(r) = \frac{Q}{2\pi\varepsilon_0 r} \qquad (a < r < b)
$$

次に円筒 $\mathrm{B}$ の外側 $r > b$ を考えます。円筒 $\mathrm{B}$ は接地されており，無限遠と円筒 $\mathrm{B}$ の電位はいずれも $0$ です。もし $r > b$ のガウス面内部に $0$ でない電荷が囲まれていれば $E(r) \propto 1/r$ となり，無限遠までの電位差 $\int_b^\infty E(r)\,\mathrm{d}r$ が発散してしまうため，円筒 $\mathrm{B}$ 上には静電誘導により単位長さあたり $-Q$ の電荷が誘起されます。よって $r > b$ のガウス面内部の総電荷は $Q L + (-Q L) = 0$ となり，円筒 $\mathrm{B}$ の外側では電場は $0$ です。なお円筒 $\mathrm{A}$ の内側 $r < a$ も総電荷が $0$ なので電場は $0$ です。

円筒の断面における電場の様子を図示すると次のようになります。電気力線は円筒 $\mathrm{A}$ の表面から放射状に外向きに出て円筒 $\mathrm{B}$ の内面で終端し，$r < a$ および $r > b$ では電場は存在しません。

![同軸導体円筒A・B間の放射状電場と外側遮蔽の断面図](../../../docs/assets/figures/pastexam-todai-ributsu/H8_ippan_butsuri_1-s1-light.svg#only-light){ loading=lazy }
![同軸導体円筒A・B間の放射状電場と外側遮蔽の断面図](../../../docs/assets/figures/pastexam-todai-ributsu/H8_ippan_butsuri_1-s1-dark.svg#only-dark){ loading=lazy }

$$
\finalanswer{E(r) = \begin{cases} \dfrac{Q}{2\pi\varepsilon_0 r} & (a < r < b) \\[10pt] 0 & (r > b) \end{cases}}
$$

### (1)(ロ)

円筒 $\mathrm{B}$ を基準とした円筒 $\mathrm{A}$ の電位差 $V$ を求めます。(1)(イ) で得た電場を $r = a$ から $r = b$ まで積分します。

$$
\begin{aligned}
V &= \int_a^b E(r)\,\mathrm{d}r \\
&= \int_a^b \frac{Q}{2\pi\varepsilon_0 r}\,\mathrm{d}r \\
&= \frac{Q}{2\pi\varepsilon_0}\ln\frac{b}{a}
\end{aligned}
$$

したがって二つの円筒間の単位長さあたりの静電容量 $C = \dfrac{Q}{V}$ は次式となります。

$$
\finalanswer{C = \frac{2\pi\varepsilon_0}{\ln(b/a)}}
$$

### (2)(イ)

円筒 $\mathrm{A}$ に紙面裏から表へ向かう $+z$ 方向，円筒 $\mathrm{B}$ に紙面表から裏へ向かう $-z$ 方向へ大きさ $I$ の電流が一様に流れているとします。系の円筒対称性より，磁束密度 $\mathbf{B}$ は中心軸を囲む円周方向 $\hat{\mathbf{e}}_\phi$ のみを向き，大きさ $B(r)$ は $r$ のみに依存します。

中心軸を中心とする半径 $r$ の円を積分経路としてアンペールの法則を用います。円筒 $\mathrm{A}$ と $\mathrm{B}$ の間 $a < r < b$ では，円周が囲む電流は円筒 $\mathrm{A}$ を流れる電流 $I$ のみなので，次式が成り立ちます。

$$
2\pi r B(r) = \mu_0 I
$$

したがって $a < r < b$ における磁束密度の大きさは

$$
B(r) = \frac{\mu_0 I}{2\pi r} \qquad (a < r < b)
$$

であり，向きは円筒 $\mathrm{A}$ の電流方向に対して右ねじの向きすなわち $+z$ 方向から見て反時計回りです。なお円筒 $\mathrm{A}$ の内側 $r < a$ では囲む電流が $0$，円筒 $\mathrm{B}$ の外側 $r > b$ では囲む正味電流が $I - I = 0$ であるため，いずれの領域でも磁束密度は $0$ です。

断面における磁束密度の様子を図示すると次のようになります。磁力線は円筒 $\mathrm{A}$ と $\mathrm{B}$ の間の領域に同心円状に分布し，外側へ向かうにつれて $1/r$ で弱くなります。

![同軸導体円筒A・Bに逆向き電流を流したときの同心円状磁束密度の断面図](../../../docs/assets/figures/pastexam-todai-ributsu/H8_ippan_butsuri_1-s2-light.svg#only-light){ loading=lazy }
![同軸導体円筒A・Bに逆向き電流を流したときの同心円状磁束密度の断面図](../../../docs/assets/figures/pastexam-todai-ributsu/H8_ippan_butsuri_1-s2-dark.svg#only-dark){ loading=lazy }

$$
\finalanswer{B(r) = \frac{\mu_0 I}{2\pi r} \qquad (a < r < b)}
$$

### (2)(ロ)

円筒 $\mathrm{A}$ の表面にはたらく圧力を，電流層にはたらくローレンツ力と仮想仕事の原理の2通りの方法で導出します。

まず，電流層にはたらくローレンツ力から直接求めます。円筒 $\mathrm{A}$ の表面を流れる面電流密度は $K = \dfrac{I}{2\pi a}$ で $+z$ 方向を向きます。磁束密度は円筒 $\mathrm{A}$ のすぐ内側で $B(a^-) = 0$，すぐ外側で $B(a^+) = \dfrac{\mu_0 I}{2\pi a}$ であり，導体層の厚さにわたって線形に変化するため，表面の面電流自身にはたらく有効な磁束密度はその平均値

$$
B_{\mathrm{avg}} = \frac{B(a^-) + B(a^+)}{2} = \frac{\mu_0 I}{4\pi a}
$$

になります。面電流密度 $\mathbf{K} = K\hat{\mathbf{e}}_z$ がこの磁束密度 $\mathbf{B}_{\mathrm{avg}} = B_{\mathrm{avg}}\hat{\mathbf{e}}_\phi$ から受ける単位面積あたりの力すなわち圧力ベクトルは $\mathbf{f} = \mathbf{K} \times \mathbf{B}_{\mathrm{avg}}$ です。ここで $\hat{\mathbf{e}}_z \times \hat{\mathbf{e}}_\phi = -\hat{\mathbf{e}}_r$ なので，力は円筒 $\mathrm{A}$ を径方向内向きに圧縮する向きにはたらき，その大きさ $p$ は次式となります。

$$
\begin{aligned}
p &= K B_{\mathrm{avg}} \\
&= \frac{I}{2\pi a}\cdot\frac{\mu_0 I}{4\pi a} \\
&= \frac{\mu_0 I^2}{8\pi^2 a^2}
\end{aligned}
$$

次に，仮想仕事の原理からも同じ結果を確認します。電流 $I$ を一定に保った状態で，単位長さあたりの磁場エネルギー $U_m$ を計算します。

$$
\begin{aligned}
U_m &= \int_a^b \frac{B(r)^2}{2\mu_0}\cdot 2\pi r\,\mathrm{d}r \\
&= \frac{\mu_0 I^2}{4\pi}\int_a^b \frac{\mathrm{d}r}{r} \\
&= \frac{\mu_0 I^2}{4\pi}\ln\frac{b}{a}
\end{aligned}
$$

電流 $I$ を一定に保ちながら内円筒半径 $a$ を微小量 $\mathrm{d}a$ だけ変化させると，磁束変化に伴う電源からの供給エネルギーを含めた力学的仮想仕事により，半径増加方向すなわち外向きにはたらく単位長さあたりの合力 $F_r$ は $F_r = +\left(\dfrac{\partial U_m}{\partial a}\right)_I$ で与えられます。

$$
F_r = \frac{\partial}{\partial a}\left(\frac{\mu_0 I^2}{4\pi}\ln\frac{b}{a}\right) = -\frac{\mu_0 I^2}{4\pi a}
$$

負号は力が中心軸向きの内向きであることを表します。単位長さあたりの表面積 $2\pi a$ で割ると，円筒 $\mathrm{A}$ の表面にはたらく内向きの圧力の大きさは

$$
p = \frac{|F_r|}{2\pi a} = \frac{\mu_0 I^2}{8\pi^2 a^2}
$$

となり，題意の表式が証明されました。これは磁場のエネルギー密度 $\dfrac{B(a^+)^2}{2\mu_0}$ すなわち磁気圧に一致しています。
