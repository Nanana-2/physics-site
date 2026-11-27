---
title: 東大理物 平成11年度 物理学 第3問：マクスウェル方程式・静電遮蔽・電磁波と電磁ポテンシャル
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成11年度
exam_subject: 物理学
exam_number: 第3問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成11年度 物理学 第3問：マクスウェル方程式・静電遮蔽・電磁波と電磁ポテンシャル

## 問題

Maxwell は，いくつかの実験事実から4つの方程式（Maxwell 方程式）

$$
\begin{aligned}
\nabla\cdot\vec{E} &= \frac{\rho}{\varepsilon_0} \qquad \text{(1)} & \nabla\cdot\vec{B} &= 0 \qquad \text{(2)} \\
\nabla\times\vec{E} &= -\frac{\partial\vec{B}}{\partial t} \qquad \text{(3)} & \frac{1}{\varepsilon_0\mu_0}\nabla\times\vec{B} &= \frac{\vec{j}}{\varepsilon_0} + \frac{\partial\vec{E}}{\partial t} \qquad \text{(4)}
\end{aligned}
$$

を与え，電磁気学を完成させた。ただし，$\vec{E}$ は電場，$\vec{B}$ は磁束密度，$\rho$ は電荷密度，$\vec{j}$ は電流密度，$\varepsilon_0$ は真空の誘電率，$\mu_0$ は真空の透磁率で，以下では真空中の電磁場のみを考える。
{: .problem-lead }

(1) 式 (1) は Gauss の法則を表す。

(a) 閉じた中空の導体があると，導体の外部にある電荷が作る電場は，導体に囲まれた中空の空間には侵入できない。このことを，式 (1) を用いて証明せよ。ただし中空の空間には，もともと電荷は存在しなかったものとする。

(b) $R_1$ および $R_2$（$R_1 > R_2$）の半径をもつ2個の同心の中空導体球を用いて，Gauss の法則を実験的に検証したい。原理的にどのような手順で何を測定すれば良いか，答えよ。

(2) Maxwell 方程式から電磁波の存在が予言される。

(a) 電荷の保存則を用いて，Ampère の法則，すなわち，「ある閉曲線が囲む定常電流 $I$ によって生じる磁場 $\vec{B}/\mu_0$ をその閉曲線に沿って線積分すると，$I$ に等しい」を非定常電流の場合に一般化し，式 (4) を導け。

(b) ある瞬間に電流密度 $\vec{j}$ が局所的に発生し，短時間で消滅したとする。その後の $\vec{B}$ と $\vec{E}$ はどのように変動するか。式 (3) と (4) を用いて，直観的に説明せよ。

(c) 電荷や電流の分布が無い場合，真空中を伝播する電磁波が存在することを導け。またその速度を，設問に与えられた量を用いて示せ。

(3) 適当なスカラー場（スカラーポテンシャル）$\phi$ とベクトル場（ベクトルポテンシャル）$\vec{A}$ を導入することにより，

$$
\vec{B} = \nabla\times\vec{A},\qquad \vec{E} = -\nabla\phi - \frac{\partial\vec{A}}{\partial t}
$$

と表わせることを示せ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成11年度 物理学 第3問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
マクスウェル方程式の基礎構造を3つの側面から検証します。設問 (1) では静電場におけるガウスの法則と導体の等電位性から静電遮蔽を証明し，キャベンディッシュの同心球実験による逆2乗則の検証法を整理します。

設問 (2) では電荷保存則とガウスの法則から変位電流項を導入してアンペール・マクスウェルの法則を導き，真空中の波動方程式から光速を導出します。設問 (3) ではベクトル解析の基本恒等式を用いてスカラーポテンシャルとベクトルポテンシャルの存在を示します。
</div>

### (1)(a)

静電場を考えているため，式 (3) は $\nabla\times\vec{E} = \vec{0}$ となり，静電ポテンシャル $\phi$ を導入して $\vec{E} = -\nabla\phi$ と表すことができます。また静電平衡状態にある導体内部では $\vec{E} = \vec{0}$ なので，中空の空間 $V$ を囲む導体の内壁面 $\partial V$ 上では $\phi$ は一定値 $\phi_0$ をとります。

中空の空間 $V$ 内には電荷が存在しないため，$\rho = 0$ であり，式 (1) より $V$ 内で $\nabla\cdot\vec{E} = 0$ が成り立ちます。ここでベクトル場 $\phi\vec{E}$ の発散を計算します。

$$
\begin{aligned}
\nabla\cdot(\phi\vec{E}) &= (\nabla\phi)\cdot\vec{E} + \phi(\nabla\cdot\vec{E}) \\
&= -|\vec{E}|^2 + \phi(\nabla\cdot\vec{E})
\end{aligned}
$$

$V$ 内で $\nabla\cdot\vec{E} = 0$ なので，$|\vec{E}|^2 = -\nabla\cdot(\phi\vec{E})$ となります。これを中空領域 $V$ 全体で体積積分し，ガウスの発散定理を用いて面積分に書き換えます。

$$
\begin{aligned}
\int_V |\vec{E}|^2\,\mathrm{d}V &= -\int_V \nabla\cdot(\phi\vec{E})\,\mathrm{d}V \\
&= -\oint_{\partial V} \phi\vec{E}\cdot\mathrm{d}\vec{S}
\end{aligned}
$$

境界 $\partial V$ 上では $\phi = \phi_0$ で一定であるため，$\phi_0$ を積分の外に出すことができます。さらに再びガウスの発散定理を用いると次のようになります。

$$
\begin{aligned}
\int_V |\vec{E}|^2\,\mathrm{d}V &= -\phi_0 \oint_{\partial V} \vec{E}\cdot\mathrm{d}\vec{S} \\
&= -\phi_0 \int_V (\nabla\cdot\vec{E})\,\mathrm{d}V \\
&= 0
\end{aligned}
$$

被積分関数 $|\vec{E}|^2$ は至るところ非負であるため，中空の空間 $V$ のすべての点で $|\vec{E}|^2 = 0$，すなわち $\vec{E} = \vec{0}$ が成り立ちます。したがって，導体の外部にある電荷が作る電場は中空の空間に侵入できません。

<div class="rigor-note" markdown>
静電ポテンシャルが $V$ 内で調和関数 $\nabla^2\phi = 0$ であることと最大値原理から，$\partial V$ 上で定数 $\phi_0$ をとる $\phi$ は $V$ 内部でも恒等的に $\phi = \phi_0$ となり，$\vec{E} = \vec{0}$ を導くこともできます。上のエネルギー積分法は同じ内容を初等的な発散定理だけで完結に証明したものです。
</div>

### (1)(b)

ガウスの法則は静電力の逆2乗則と等価であり，(1)(a) の結果から，帯電した閉じた導体球殻の内部には電場が生じず，静電平衡時には内壁および内部の導体に電荷が存在しないことが導かれます。逆に逆2乗則からわずかでもずれていれば，外球を帯電させたときに内部の導体球にも電位差や電荷が現れます。これを利用したキャベンディッシュの同心球実験の手順は次の通りです。

1. 半径 $R_1$ の外球と半径 $R_2$（$R_1 > R_2$）の内球を同心に配置し，両者を細い導線または開閉可能なスイッチで電気的に接続します。
2. 外球に十分高い電圧 $V_0$ を印加して帯電させ，静電平衡に達するまで待ちます。
3. 外球と内球の間の電気的接続を絶縁棒などで切り離します。
4. 外球を接地して放電させるか，あるいは外球を2つに分割して取り除きます。
5. 高感度の電位計や検電器を用いて，内球に残留した電荷や，内球と外球の間の電位差を測定します。

もしガウスの法則が厳密に成り立つならば，手順 2 の時点で電荷はすべて外球の外表面に分布し，内球の電荷は厳密に $0$ となります。したがって手順 5 で内球の電荷，あるいは接地した外球に対する内球の電位差が測定限界内で $0$ であることを確認することにより，ガウスの法則を高精度に検証することができます。

### (2)(a)

定常電流に対するアンペールの法則は，任意の閉曲線 $C$ とそれを縁にもつ曲面 $S$ について次式で与えられます。

$$
\oint_C \frac{\vec{B}}{\mu_0}\cdot\mathrm{d}\vec{l} = \int_S \vec{j}\cdot\mathrm{d}\vec{S}
$$

ストークスの定理を左辺に用いると，微分形のアンペールの法則が得られます。

$$
\nabla\times\vec{B} = \mu_0\vec{j}
$$

しかし非定常電流では電荷密度 $\rho$ が時間変化するため，連続の方程式で表される電荷の保存則

$$
\frac{\partial\rho}{\partial t} + \nabla\cdot\vec{j} = 0
$$

より $\nabla\cdot\vec{j} = -\dfrac{\partial\rho}{\partial t} \neq 0$ となります。一方で任意のベクトル場に対して $\nabla\cdot(\nabla\times\vec{B}) = 0$ が恒等的に成り立つため，$\nabla\times\vec{B} = \mu_0\vec{j}$ の両辺の発散をとると矛盾が生じます。

そこで式 (1) のガウスの法則 $\rho = \varepsilon_0\nabla\cdot\vec{E}$ を電荷の保存則に代入します。

$$
\nabla\cdot\left(\vec{j} + \varepsilon_0\frac{\partial\vec{E}}{\partial t}\right) = 0
$$

この式は，伝導電流密度 $\vec{j}$ に変位電流密度 $\vec{j}_{\mathrm{d}} = \varepsilon_0\dfrac{\partial\vec{E}}{\partial t}$ を加えた全電流密度の発散が常に $0$ であることを示しています。したがってアンペールの法則の右辺の $\vec{j}$ を $\vec{j} + \varepsilon_0\dfrac{\partial\vec{E}}{\partial t}$ に置き換えることで，非定常電流の場合へ矛盾なく一般化することができます。

$$
\nabla\times\vec{B} = \mu_0\left(\vec{j} + \varepsilon_0\frac{\partial\vec{E}}{\partial t}\right)
$$

両辺を $\varepsilon_0\mu_0$ で割ると，式 (4) が導かれます。

$$
\frac{1}{\varepsilon_0\mu_0}\nabla\times\vec{B} = \frac{\vec{j}}{\varepsilon_0} + \frac{\partial\vec{E}}{\partial t}
$$

### (2)(b)

ある瞬間に局所的な電流密度 $\vec{j}$ が発生すると，式 (4) の右辺第1項 $\dfrac{\vec{j}}{\varepsilon_0}$ によってその周囲に渦状の磁場 $\vec{B}$ が生じます。電流が短時間で発生・消滅するため，この磁場 $\vec{B}$ は時間的に変化します。

次に，磁場の時間変化 $\dfrac{\partial\vec{B}}{\partial t}$ が生じると，式 (3) のファラデーの電磁誘導の法則 $\nabla\times\vec{E} = -\dfrac{\partial\vec{B}}{\partial t}$ により，その周囲に渦状の電場 $\vec{E}$ が誘導され，この電場もまた時間的に変化します。

すると電流 $\vec{j}$ がすでに消滅した後でも，電場の時間変化 $\dfrac{\partial\vec{E}}{\partial t}$ が式 (4) の右辺第2項の変位電流として働き，さらにその外側に新たな渦状の磁場 $\vec{B}$ を生み出します。

このように，式 (3) と式 (4) の相互作用によって，磁場の時間変化が電場の渦を生み，電場の時間変化が磁場の渦を生むという連鎖が次々と引き起こされます。その結果，$\vec{E}$ と $\vec{B}$ は互いに直交しながら振動する電磁波として，発生源から遠方へ向かって真空中を自律的に伝播していきます。

### (2)(c)

電荷や電流の分布がない真空中では $\rho = 0$，$\vec{j} = \vec{0}$ であり，マクスウェル方程式 (1)〜(4) は次の形になります。

$$
\begin{aligned}
\nabla\cdot\vec{E} &= 0 & \nabla\cdot\vec{B} &= 0 \\
\nabla\times\vec{E} &= -\frac{\partial\vec{B}}{\partial t} & \nabla\times\vec{B} &= \varepsilon_0\mu_0\frac{\partial\vec{E}}{\partial t}
\end{aligned}
$$

式 (3) の両辺の回転をとり，ベクトル恒等式 $\nabla\times(\nabla\times\vec{E}) = \nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E}$ を用います。

$$
\begin{aligned}
\nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E} &= -\frac{\partial}{\partial t}(\nabla\times\vec{B}) \\
-\nabla^2\vec{E} &= -\varepsilon_0\mu_0\frac{\partial^2\vec{E}}{\partial t^2}
\end{aligned}
$$

ここで $\nabla\cdot\vec{E} = 0$ および式 (4) を代入しました。整理すると $\vec{E}$ に対する波動方程式が得られます。

$$
\left(\nabla^2 - \varepsilon_0\mu_0\frac{\partial^2}{\partial t^2}\right)\vec{E} = \vec{0}
$$

同様に式 (4) の両辺の回転をとり，$\nabla\cdot\vec{B} = 0$ と式 (3) を用いると，$\vec{B}$ もまったく同じ波動方程式を満たします。

$$
\left(\nabla^2 - \varepsilon_0\mu_0\frac{\partial^2}{\partial t^2}\right)\vec{B} = \vec{0}
$$

一般の波動方程式 $\nabla^2 u = \dfrac{1}{c^2}\dfrac{\partial^2 u}{\partial t^2}$ と比較することにより，真空中を伝播する電磁波の存在と，その伝播速度 $c$ が次のように導かれます。

$$
\finalanswer{c = \frac{1}{\sqrt{\varepsilon_0\mu_0}}}
$$

### (3)

まず式 (2) より $\nabla\cdot\vec{B} = 0$ が全空間で成り立っています。ポアンカレの補題より，単連結な3次元空間において発散が恒等的に $0$ である滑らかなベクトル場 $\vec{B}$ に対しては，

$$
\vec{B} = \nabla\times\vec{A}
$$

を満たすベクトルポテンシャル $\vec{A}$ が存在します。

実際に $\vec{A}$ の具体構成を確認すると，例えば $A_z = 0$ として

$$
\begin{aligned}
A_x(x, y, z, t) &= \int_{z_0}^{z} B_y(x, y, z', t)\,\mathrm{d}z' - \int_{y_0}^{y} B_z(x, y', z_0, t)\,\mathrm{d}y' \\
A_y(x, y, z, t) &= -\int_{z_0}^{z} B_x(x, y, z', t)\,\mathrm{d}z'
\end{aligned}
$$

と定義すれば，$\nabla\cdot\vec{B} = 0$ を用いて $\nabla\times\vec{A} = \vec{B}$ が直接確かめられます。

次にこの $\vec{B} = \nabla\times\vec{A}$ を式 (3) のファラデーの法則に代入して整理します。

$$
\nabla\times\left(\vec{E} + \frac{\partial\vec{A}}{\partial t}\right) = \vec{0}
$$

単連結な領域において回転が恒等的に $0$ であるベクトル場は，適当なスカラーポテンシャル $\phi$ の勾配として表すことができます。

$$
\vec{E} + \frac{\partial\vec{A}}{\partial t} = -\nabla\phi
$$

これを移項すると，求める表示が得られます。

$$
\vec{B} = \nabla\times\vec{A},\qquad \vec{E} = -\nabla\phi - \frac{\partial\vec{A}}{\partial t}
$$
