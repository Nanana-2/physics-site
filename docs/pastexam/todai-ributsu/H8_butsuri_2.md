---
title: 東大理物 平成8年度 物理学 第2問：軸対称磁場中の導体リング振り子の電磁誘導減衰と自己インダクタンス効果
tags:
  - 院試過去問
  - 東大理物
  - 電磁気学
  - 力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成8年度
exam_subject: 物理学
exam_number: 第2問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。
---

# 東大理物 平成8年度 物理学 第2問：軸対称磁場中の導体リング振り子の電磁誘導減衰と自己インダクタンス効果

## 問題

磁場中におかれた単振り子の一次元振動について考える。図に示すように，振り子は導線を円形にしたリングと，それを吊るす絶縁体のワイヤーからできている。導線の太さはリングの半径 $R$ に比べて十分細い。静止状態でのリングの中心軸を $x$ 軸にとり，リングの $x$ 座標の平衡位置からのずれを $x(t)$ とする。振り子の振幅は十分小さく，リングの中心軸は常に $x$ 軸に一致しているとみなせるとする。磁場がないときのリングの運動方程式は

$$
m\left(\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + \omega_0^2 x\right) = f(t) \qquad \text{(1)}
$$

とあらわすことができる。ここで $m$ は振り子の質量，$\omega_0$ は固有角振動数，$f(t)$ は外力である。図のように $x$ 軸に沿って細長い棒磁石が置かれており，$x$ 軸に関して軸対称な磁場をつくっている。磁束密度のリングの中心から半径方向の成分を $B_r$，$x$ 方向の成分を $B_x$ とする。リングの導線の位置での磁場に関して，$B_r$ は振動の範囲以内では一様とみなせるとする。このような磁場中におかれたリングの振動について，以下の問題に答えよ。ただし，(1) から (3) の問題においては，リングのインダクタンスは無視できるものとする。
{: .problem-lead }

<figure class="problem-figure" markdown>
![絶縁体ワイヤーで吊るされた導体リング振り子とx軸沿いの棒磁石の配置](../../assets/figures/pastexam-todai-ributsu/H8_butsuri_2-p-light.svg#only-light){ loading=lazy }
![絶縁体ワイヤーで吊るされた導体リング振り子とx軸沿いの棒磁石の配置](../../assets/figures/pastexam-todai-ributsu/H8_butsuri_2-p-dark.svg#only-dark){ loading=lazy }
</figure>

(1) まずリングの一周の抵抗値が $r$ の場合を考える。リングを磁場中で振動させると，その運動は電磁誘導の作用により減衰する。このとき，最初にリングがもっていた運動エネルギーはどこに失われたかを述べよ。また，このエネルギー損失の割合を大きくするためには，抵抗値 $r$ が大きい方がよいか，小さい方がよいか，理由をつけて答えよ。

(2) (a) 運動にともない，リングに発生する誘導起電力 $e$ が

$$
e = -2\pi R B_r \frac{\mathrm{d}x}{\mathrm{d}t} \qquad \text{(2)}
$$

となることを示せ。

(b) 磁場の中でのリングの運動方程式を求めよ。

(3) 次に，リングを静止させた状態で，$f(t) = p_0 \delta(t)$（$\delta(t)$ は Dirac の $\delta$ 関数，$p_0$ は定数）の外力を与えたときの $t \ge 0$ における振動を時間の関数として求め，その概略を図示せよ。

(4) (a) 抵抗値 $r$ がある程度小さくなると，リングの自己インダクタンス $L$ が運動に効き始める。抵抗とインダクタンスの間にどのような関係があるとき，インダクタンスによる効果が支配的になるか答えよ。

(b) この条件が成立する場合について，磁場中でのリングの運動方程式を求め，(1) 式であらわされるような振動がどのような影響を受けるか述べよ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成8年度 物理学 第2問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整え，図を描き直しています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
軸対称磁場中を動くリングには磁束密度の動径成分 $B_r$ に比例した誘導起電力 $e = -2\pi R B_r \dot{x}$ が生じます。自己インダクタンスを無視する領域では誘導電流が速度 $\dot{x}$ に比例するため，ローレンツ力が速度に比例する抵抗力としてはたらき，減衰振動となります。一方，抵抗 $r$ が十分小さくインダクタンス $L$ の寄与が主になると誘導電流は変位 $x$ に比例するようになり，エネルギー散逸が消えて復元力のみが増強される磁気ばね効果が現れます。
</div>

### (1)

磁場中でリングが運動すると，リングを貫く磁束が時間変化して誘導起電力が生じ，抵抗 $r$ をもつリングに誘導電流が流れます。最初にリングがもっていた運動エネルギーは，この誘導電流によってリングの電気抵抗 $r$ で発生するジュール熱として散逸します。

自己インダクタンスを無視すると，リングの速度が $v$ のとき誘導起電力 $e$ は抵抗 $r$ によらず速度のみに比例し，誘導電流は $I = e/r$ となります。したがって単位時間あたりのエネルギー損失すなわちジュール発熱の仕事率 $P$ は

$$
P = r I^2 = \frac{e^2}{r}
$$

で表されます。このように $P$ は $r$ に反比例するため，エネルギー損失の割合を大きくするためには抵抗値 $r$ は小さい方がよいことになります。

### (2)(a)

誘導起電力 $e$ は，磁場のガウスの法則 $\nabla \cdot \mathbf{B} = 0$ とファラデーの電磁誘導の法則から導く方法と，導線内の自由電子にはたらくローレンツ力から直接求める方法のいずれでも示せます。

まずファラデーの法則を用いて示します。リングが位置 $x$ から $x + \mathrm{d}x$ へ微小変位したとき，半径 $R$ で厚さ $\mathrm{d}x$ の円柱領域を考えます。この円柱の表面は位置 $x$ の円板，位置 $x + \mathrm{d}x$ の円板，および半径 $R$・幅 $\mathrm{d}x$ の側面からなります。磁場の発散が $0$ であることから，この閉曲面を貫く全磁束は $0$ です。$x$ 軸正方向を向いて円板を貫く磁束を $\Phi(x)$ とすると，円柱表面から外向きに出る全磁束について次式が成り立ちます。

$$
-\Phi(x) + \Phi(x + \mathrm{d}x) + 2\pi R B_r\,\mathrm{d}x = 0
$$

すなわち磁束の空間変化は

$$
\frac{\mathrm{d}\Phi}{\mathrm{d}x} = -2\pi R B_r
$$

です。ファラデーの電磁誘導の法則より，$x$ 軸正方向に対して右ねじの向きを正とした誘導起電力 $e$ は次のように求まります。

$$
\begin{aligned}
e &= -\frac{\mathrm{d}\Phi}{\mathrm{d}t} \\
&= -\frac{\mathrm{d}\Phi}{\mathrm{d}x}\frac{\mathrm{d}x}{\mathrm{d}t} \\
&= 2\pi R B_r \frac{\mathrm{d}x}{\mathrm{d}t}
\end{aligned}
$$

右ねじと逆向きすなわち $x$ 軸正方向から見て反時計回りの向きを正にとれば，

$$
e = -2\pi R B_r \frac{\mathrm{d}x}{\mathrm{d}t}
$$

となります。ローレンツ力から見る場合も，速度 $\mathbf{v} = (\dot{x}, 0, 0)$ と磁束密度の動径成分 $\mathbf{B}_r = B_r \hat{\mathbf{e}}_r$ の外積は円周方向の単位ベクトル $\hat{\mathbf{e}}_\phi$ を用いて $\mathbf{v} \times \mathbf{B}_r = \dot{x} B_r \hat{\mathbf{e}}_\phi$ となるため，一周積分すると同じ大きさ $2\pi R B_r \dot{x}$ が得られ，向きを左ねじ方向に選べば式 (2) に一致します。

### (2)(b)

自己インダクタンスを無視すると，リングに流れる誘導電流 $I$ はオームの法則より

$$
I = \frac{e}{r} = -\frac{2\pi R B_r}{r}\frac{\mathrm{d}x}{\mathrm{d}t}
$$

です。円周上の微小線素 $\mathrm{d}\mathbf{l}$ に磁場が及ぼすアンペール力は $I\,\mathrm{d}\mathbf{l} \times \mathbf{B}$ です。$B_x$ 成分による力は半径方向を向き円周全体で積分すると軸対称性から打ち消し合って $0$ になります。一方，動径成分 $B_r$ による力は $x$ 方向を向き，レンツの法則より常に運動を妨げる向きにはたらきます。その $x$ 成分の合力 $F_{\mathrm{em}}$ は

$$
\begin{aligned}
F_{\mathrm{em}} &= 2\pi R I B_r \\
&= -\frac{(2\pi R B_r)^2}{r}\frac{\mathrm{d}x}{\mathrm{d}t}
\end{aligned}
$$

となります。なお，単位時間あたりに電磁力がリングにする仕事 $F_{\mathrm{em}}\dot{x}$ は $-\dfrac{e^2}{r}$ となり， (1) のジュール発熱率と符号を除いて厳密に一致します。

これを磁場がないときの運動方程式 (1) に加えることで，磁場中でのリングの運動方程式が得られます。

$$
\finalanswer{m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + \frac{(2\pi R B_r)^2}{r}\frac{\mathrm{d}x}{\mathrm{d}t} + m\omega_0^2 x = f(t)}
$$

### (3)

減衰定数 $\gamma$ を

$$
\gamma = \frac{(2\pi R B_r)^2}{2 m r} = \frac{2\pi^2 R^2 B_r^2}{m r} > 0
$$

と定義すると，運動方程式は次式になります。

$$
\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + 2\gamma\frac{\mathrm{d}x}{\mathrm{d}t} + \omega_0^2 x = \frac{p_0}{m}\delta(t)
$$

$t < 0$ でリングは平衡位置に静止しているため $x(0^-) = 0$，$\dot{x}(0^-) = 0$ です。運動方程式を $t = 0$ を挟む微小な区間 $[-\epsilon, +\epsilon]$ で積分して $\epsilon \to 0^+$ の極限をとると，変位 $x(t)$ は連続で速度 $\dot{x}(t)$ が不連続に跳躍します。

$$
\begin{aligned}
x(0^+) &= 0 \\
\dot{x}(0^+) &= \frac{p_0}{m}
\end{aligned}
$$

$t > 0$ では右辺が $0$ の同次方程式 $\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0$ となります。特性方程式 $\lambda^2 + 2\gamma\lambda + \omega_0^2 = 0$ の解は $\lambda = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$ なので，$\gamma$ と $\omega_0$ の大小関係により次の3つの場合に分けられます。

第1に，$\gamma < \omega_0$ の減衰振動の場合を考えます。$\Omega = \sqrt{\omega_0^2 - \gamma^2}$ とおくと，一般解は $x(t) = e^{-\gamma t}(C_1 \cos\Omega t + C_2 \sin\Omega t)$ です。初期条件 $x(0^+) = 0$ より $C_1 = 0$，$\dot{x}(0^+) = \dfrac{p_0}{m}$ より $\Omega C_2 = \dfrac{p_0}{m}$ すなわち $C_2 = \dfrac{p_0}{m\Omega}$ となります。

$$
x(t) = \frac{p_0}{m\Omega} e^{-\gamma t}\sin(\Omega t)
$$

第2に，$\gamma = \omega_0$ の臨界減衰の場合を考えます。一般解は $x(t) = (C_1 + C_2 t)e^{-\gamma t}$ であり，初期条件 $x(0^+) = 0$ より $C_1 = 0$，$\dot{x}(0^+) = \dfrac{p_0}{m}$ より $C_2 = \dfrac{p_0}{m}$ となります。

$$
x(t) = \frac{p_0}{m} t e^{-\gamma t}
$$

第3に，$\gamma > \omega_0$ の過減衰の場合を考えます。$\Gamma = \sqrt{\gamma^2 - \omega_0^2}$ とおくと，一般解は $x(t) = e^{-\gamma t}(C_1 \cosh\Gamma t + C_2 \sinh\Gamma t)$ であり，初期条件 $x(0^+) = 0$ より $C_1 = 0$，$\dot{x}(0^+) = \dfrac{p_0}{m}$ より $\Gamma C_2 = \dfrac{p_0}{m}$ すなわち $C_2 = \dfrac{p_0}{m\Gamma}$ となります。

$$
x(t) = \frac{p_0}{m\Gamma} e^{-\gamma t}\sinh(\Gamma t)
$$

いずれの場合も $t = 0$ で傾き $\dot{x}(0^+) = p_0/m$ をもって立ち上がり，$t \to \infty$ で $0$ へ収束します。$\gamma < \omega_0$ では符号を反転させながら振幅が減衰して振動し，$\gamma \ge \omega_0$ では一度極大を迎えたあと振動せずに単調に $0$ へ近づきます。これらの概略を図示すると次のようになります。

![衝撃外力に対する導体リング振り子の応答x(t)の3つの減衰領域](../../assets/figures/pastexam-todai-ributsu/H8_butsuri_2-s-light.svg#only-light){ loading=lazy }
![衝撃外力に対する導体リング振り子の応答x(t)の3つの減衰領域](../../assets/figures/pastexam-todai-ributsu/H8_butsuri_2-s-dark.svg#only-dark){ loading=lazy }

$$
\finalanswer{x(t) = \begin{cases} \dfrac{p_0}{m\sqrt{\omega_0^2 - \gamma^2}} e^{-\gamma t}\sin\left(\sqrt{\omega_0^2 - \gamma^2}\,t\right) & (\gamma < \omega_0) \\[10pt] \dfrac{p_0}{m} t e^{-\gamma t} & (\gamma = \omega_0) \\[10pt] \dfrac{p_0}{m\sqrt{\gamma^2 - \omega_0^2}} e^{-\gamma t}\sinh\left(\sqrt{\gamma^2 - \omega_0^2}\,t\right) & (\gamma > \omega_0) \end{cases}}
$$

### (4)(a)

リングの自己インダクタンス $L$ を考慮すると，回路方程式は次のようになります。

$$
L\frac{\mathrm{d}I}{\mathrm{d}t} + r I = e = -2\pi R B_r \frac{\mathrm{d}x}{\mathrm{d}t}
$$

角振動数 $\omega$ の振動を考えると，時間微分は $\omega$ 倍の大きさとなるため，インダクタンスによる逆起電力 $L\dot{I}$ の大きさは $\omega L |I|$，抵抗による電圧降下 $r I$ の大きさは $r |I|$ です。したがってインダクタンスによる効果が主となる条件は，抵抗が誘導リアクタンスに比べて十分小さいこと，すなわち磁場がないときの固有角振動数 $\omega_0$ を用いて次式が成り立つときです。

$$
\finalanswer{r \ll \omega_0 L}
$$

### (4)(b)

$r \ll \omega_0 L$ として抵抗項 $r I$ を無視すると，回路方程式は次式になります。

$$
L\frac{\mathrm{d}I}{\mathrm{d}t} = -2\pi R B_r \frac{\mathrm{d}x}{\mathrm{d}t}
$$

平衡位置 $x = 0$ で電流が流れていない初期状態からこれを時間で積分すると，誘導電流 $I$ はリングの変位 $x$ に比例することがわかります。

$$
I = -\frac{2\pi R B_r}{L} x
$$

これはリングを貫く全磁束 $L I + \Phi(x)$ が保存されることに他なりません。この誘導電流が磁場 $B_r$ から受ける $x$ 方向のローレンツ力 $F_{\mathrm{em}}$ は

$$
\begin{aligned}
F_{\mathrm{em}} &= 2\pi R I B_r \\
&= -\frac{(2\pi R B_r)^2}{L} x
\end{aligned}
$$

となり，変位 $x$ に比例する復元力としてはたらきます。したがって磁場中でのリングの運動方程式は次式となります。

$$
m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + \left(m\omega_0^2 + \frac{(2\pi R B_r)^2}{L}\right) x = f(t)
$$

この結果から，式 (1) で表される振動は次のような影響を受けます。第1に，抵抗によるジュール発熱がなくなるため速度に比例する減衰項が消滅し，振り子は減衰せずに振動を続けます。第2に，電磁誘導による復元力が元の復元力に加わるため，固有角振動数が $\omega_0$ から

$$
\omega' = \sqrt{\omega_0^2 + \frac{(2\pi R B_r)^2}{m L}}
$$

へと増加します。

$$
\finalanswer{m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + \left(m\omega_0^2 + \frac{(2\pi R B_r)^2}{L}\right) x = f(t)}
$$
