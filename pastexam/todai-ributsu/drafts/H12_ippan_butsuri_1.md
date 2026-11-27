---
title: 東大理物 平成12年度 一般教育科目 物理学 第1問：ロケットの垂直打ち上げと脱出速度
tags:
  - 院試過去問
  - 東大理物
  - 力学
  - 熱力学
exam_university: 東京大学大学院理学系研究科物理学専攻
exam_year: 平成12年度
exam_subject: 一般教育科目 物理学
exam_number: 第1問
exam_source_url: https://www.phys.s.u-tokyo.ac.jp/
exam_modified: Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。
---

# 東大理物 平成12年度 一般教育科目 物理学 第1問：ロケットの垂直打ち上げと脱出速度

## 問題

ロケットを垂直上方に打ち上げて，地球の重力圏を脱したい。時刻 $t$ におけるロケットの高さ，速度および質量をそれぞれ $h(t)$，$v(t) = \dfrac{\mathrm{d}h}{\mathrm{d}t}$，$M(t)$，ロケットから噴射されるガスの，ロケットに対する相対速度を $u$ とする。重力加速度を $g = 9.8\,\mathrm{m/s^2}$，地球の半径を $R = 6370\,\mathrm{km}$ として，以下に答えよ。なお，相対速度 $u$ は一定であるとし，空気抵抗は無視せよ。
{: .problem-lead }

(1) 地球の重力圏を脱出するためには噴射が終わったときの速度がある値（脱出速度：$v_{\mathrm{esc}}$）を越えている必要がある。噴射終了時の高度は $R$ に比べて十分小さいとして $v_{\mathrm{esc}}$ を求めよ。

(2) ロケットの運動方程式は，

$$
M\frac{\mathrm{d}v}{\mathrm{d}t} = -u\frac{\mathrm{d}M}{\mathrm{d}t} - Mg
$$

で与えられる。この式を導け。

(3) 燃料の噴射時間を $\Delta t$ とし，噴射開始時および噴射終了時の全質量をそれぞれ，$M_i = M(t_0)$，$M_f = M(t_0 + \Delta t)$ とおくとき，この間の速度変化 $\Delta v = v(t_0 + \Delta t) - v(t_0)$ を求めよ。また，噴射時間内の速度変化 $\Delta v$ を増やすにはどうしたらよいかを述べよ。

(4) 簡単のため，ロケットの加速度は一定であるとし，$\dfrac{\mathrm{d}v}{\mathrm{d}t} = ng$ とおく。ここに，加速度係数 $n$ は，乗組員や機内の装置に支障が生じないように選ばれた定数である。噴射開始時の質量 $M_i$ と噴射終了時の質量 $M_f$ の差がすべて燃料であるとして，燃料噴射時間 $\Delta t$，噴射による速度変化 $\Delta v$，および高度変化 $\Delta h$ を求めよ。

(5) 燃料の燃焼温度を $T\,\mathrm{K}$ とするとき，燃料ガスの噴射速度 $u$ は，燃料の分子がこの温度の下でもつ平均の運動エネルギーから決まる平均速度を超えられない。燃料分子の質量を $m$，ボルツマン定数を $k$ として，燃料分子の平均速度 $u_0$ をあらわせ。また，$u = u_0$ が実現できたとして，燃料ガスの噴射速度を大きくするには，どうしたらよいかを述べ，最良の燃料として何を選んだらよいかを言え。

(6) 燃焼温度を $T = 2000\,\mathrm{K}$，$k = 1.4 \times 10^{-23}\,\mathrm{J/K}$，陽子の質量 $m_p$ を $1.7 \times 10^{-27}\,\mathrm{kg}$ で与えるとき，設問 (5) で選んだ燃料から期待される最高噴射速度を求めよ。

(7) 実際のロケットでは，構造上，噴射開始時および噴射終了時の全質量の比 $\dfrac{M_i}{M_f}$ は，高々 $4$ ていどにしかできない。燃料ガスの噴射速度を $u = 3\,\mathrm{km/s}$，加速度係数を $n = 4$ として，期待される最終速度を求め，脱出速度と比較せよ。この結果と設問 (5) と (6) の結果から，脱出速度を得るためにどういう工夫をしたらよいかを論ぜよ。ただし，$\ln 2 = \log_e 2 = 0.7$ とおけ。

> 出典：東京大学大学院理学系研究科物理学専攻 平成12年度 一般教育科目 物理学 第1問（引用元：<https://www.phys.s.u-tokyo.ac.jp/>）。Web掲載にあたり数式をテキスト化し，小問番号の表記を整えています。解答・解説は当サイトが独自に作成したもので，東京大学が公表したものではありません。

---

## 解答・解説

<div class="approach" markdown>
噴射終了後のロケットは重力だけを受けて運動するため，地表付近と無限遠での力学的エネルギー保存則から脱出速度が求まります。

噴射中の運動方程式は，微小時間 $\mathrm{d}t$ にロケット本体と噴射ガス全体が受ける重力の力積と運動量変化を比べることで導出します。さらに得られた速度変化の式に定加速度の条件と気体分子運動論による噴射速度の上限を組み合わせることで，単段ロケットの限界と多段化の必要性を定量的に導きます。
</div>

### (1)

地球の質量を $M_{\mathrm{E}}$，万有引力定数を $G$，噴射終了時のロケットの質量を $M_f$ とします。噴射終了時の高度は $R$ に比べて十分小さいため，地表 $r = R$ での万有引力によるポテンシャルエネルギーは $-\dfrac{G M_{\mathrm{E}} M_f}{R}$ です。重力圏を脱出する最小速度 $v_{\mathrm{esc}}$ は，無限遠で速度が $0$ になる力学的エネルギー保存の条件から定まります。

$$
\frac{1}{2}M_f v_{\mathrm{esc}}^2 - \frac{G M_{\mathrm{E}} M_f}{R} = 0
$$

地表での重力加速度は $g = \dfrac{G M_{\mathrm{E}}}{R^2}$ なので $G M_{\mathrm{E}} = g R^2$ です。これを代入して $v_{\mathrm{esc}}$ を求めます。

$$
\begin{aligned}
v_{\mathrm{esc}}^2 &= \frac{2 G M_{\mathrm{E}}}{R} \\
&= 2gR
\end{aligned}
$$

数値 $g = 9.8\,\mathrm{m/s^2}$，$R = 6370\,\mathrm{km} = 6.37 \times 10^6\,\mathrm{m}$ を代入します。

$$
\begin{aligned}
v_{\mathrm{esc}} &= \sqrt{2 \times 9.8 \times 6.37 \times 10^6} \\
&= \sqrt{1.24852 \times 10^8} \\
&\approx 1.117 \times 10^4\,\mathrm{m/s}
\end{aligned}
$$

有効数字2〜3桁で表すと次の通りです。

$$
\finalanswer{v_{\mathrm{esc}} = \sqrt{2gR} \approx 1.12 \times 10^4\,\mathrm{m/s} = 11.2\,\mathrm{km/s}}
$$

### (2)

鉛直上向きを正とします。時刻 $t$ に質量 $M$，速度 $v$ のロケットが，微小時間 $\mathrm{d}t$ の間に質量 $-\mathrm{d}M > 0$ のガスをロケットに対して下向きに速さ $u$ で噴射し，時刻 $t + \mathrm{d}t$ にロケットの質量が $M + \mathrm{d}M$，速度が $v + \mathrm{d}v$ になったとします。

噴射されたガスの地上に対する速度は $v - u$ です。時刻 $t$ の系全体の運動量は $P(t) = Mv$ であり，時刻 $t + \mathrm{d}t$ の系全体の運動量 $P(t + \mathrm{d}t)$ を展開します。

$$
\begin{aligned}
P(t + \mathrm{d}t) &= (M + \mathrm{d}M)(v + \mathrm{d}v) + (-\mathrm{d}M)(v - u) \\
&= Mv + M\,\mathrm{d}v + v\,\mathrm{d}M + \mathrm{d}M\,\mathrm{d}v - v\,\mathrm{d}M + u\,\mathrm{d}M \\
&= Mv + M\,\mathrm{d}v + u\,\mathrm{d}M + \mathrm{d}M\,\mathrm{d}v
\end{aligned}
$$

この微小時間 $\mathrm{d}t$ に系全体が受ける外力は下向きの重力 $-Mg$ であり，その力積は $-Mg\,\mathrm{d}t$ です。運動量変化と力積の関係 $P(t + \mathrm{d}t) - P(t) = -Mg\,\mathrm{d}t$ を書き，2次の微小量 $\mathrm{d}M\,\mathrm{d}v$ を落とします。

$$
M\,\mathrm{d}v + u\,\mathrm{d}M = -Mg\,\mathrm{d}t
$$

両辺を $\mathrm{d}t$ で割り，移項すると求める運動方程式が得られます。

$$
M\frac{\mathrm{d}v}{\mathrm{d}t} = -u\frac{\mathrm{d}M}{\mathrm{d}t} - Mg
$$

### (3)

(2) の運動方程式の両辺を $M$ で割ります。

$$
\frac{\mathrm{d}v}{\mathrm{d}t} = -\frac{u}{M}\frac{\mathrm{d}M}{\mathrm{d}t} - g
$$

両辺を時刻 $t_0$ から $t_0 + \Delta t$ まで積分します。

$$
\begin{aligned}
\int_{t_0}^{t_0 + \Delta t} \frac{\mathrm{d}v}{\mathrm{d}t}\,\mathrm{d}t &= -u\int_{M_i}^{M_f} \frac{\mathrm{d}M}{M} - g\int_{t_0}^{t_0 + \Delta t} \mathrm{d}t \\
v(t_0 + \Delta t) - v(t_0) &= -u\ln\frac{M_f}{M_i} - g\Delta t \\
&= u\ln\frac{M_i}{M_f} - g\Delta t
\end{aligned}
$$

したがって，速度変化 $\Delta v$ は次の通りです。

$$
\finalanswer{\Delta v = u\ln\frac{M_i}{M_f} - g\Delta t}
$$

この式から，$\Delta v$ を増やすには次の3点が有効です。第1に，ガスの相対噴射速度 $u$ を大きくすることです。第2に，初期質量と最終質量の比 $\dfrac{M_i}{M_f}$ を大きくすること，すなわちロケット全体の質量に占める燃料の割合を高め，構造体の質量を軽くすることです。第3に，噴射時間 $\Delta t$ を短くして，重力による速度損失 $g\Delta t$ を小さくすることです。

### (4)

一定の加速度 $\dfrac{\mathrm{d}v}{\mathrm{d}t} = ng$ より，噴射時間 $\Delta t$ の間の速度変化は $\Delta v = ng\Delta t$ です。これを (3) の結果と等しくおきます。

$$
\begin{aligned}
ng\Delta t &= u\ln\frac{M_i}{M_f} - g\Delta t \\
(n + 1)g\Delta t &= u\ln\frac{M_i}{M_f}
\end{aligned}
$$

これを $\Delta t$ について解きます。

$$
\Delta t = \frac{u}{(n + 1)g}\ln\frac{M_i}{M_f}
$$

次に速度変化 $\Delta v = ng\Delta t$ を求めます。

$$
\begin{aligned}
\Delta v &= ng\cdot\frac{u}{(n + 1)g}\ln\frac{M_i}{M_f} \\
&= \frac{n}{n + 1}u\ln\frac{M_i}{M_f}
\end{aligned}
$$

静止状態 $v(t_0) = 0$ から打ち上げる場合，等加速度運動なので高度変化は $\Delta h = \dfrac{1}{2}(ng)(\Delta t)^2$ です。上で求めた $\Delta t$ を代入します。

$$
\begin{aligned}
\Delta h &= \frac{1}{2}ng\left[\frac{u}{(n + 1)g}\ln\frac{M_i}{M_f}\right]^2 \\
&= \frac{n u^2}{2(n + 1)^2 g}\left(\ln\frac{M_i}{M_f}\right)^2
\end{aligned}
$$

なお，噴射開始時の初速度 $v_0 = v(t_0)$ が $0$ でない場合は，これに $v_0\Delta t = \dfrac{v_0 u}{(n + 1)g}\ln\dfrac{M_i}{M_f}$ が加わります。静止からの打ち上げに対する答えは次の通りです。

$$
\finalanswer{\Delta t = \frac{u}{(n + 1)g}\ln\frac{M_i}{M_f}, \qquad \Delta v = \frac{n}{n + 1}u\ln\frac{M_i}{M_f}, \qquad \Delta h = \frac{n u^2}{2(n + 1)^2 g}\left(\ln\frac{M_i}{M_f}\right)^2}
$$

### (5)

絶対温度 $T$ における気体分子1個当たりの平均の並進運動エネルギーは $\dfrac{3}{2}kT$ です。これと $\dfrac{1}{2}m u_0^2$ を等しくおきます。

$$
\frac{1}{2}m u_0^2 = \frac{3}{2}kT
$$

両辺に $\dfrac{2}{m}$ を掛けると $u_0^2 = \dfrac{3kT}{m}$ となり，平均速度 $u_0$ は次になります。

$$
\finalanswer{u_0 = \sqrt{\frac{3kT}{m}}}
$$

$u = u_0$ のとき噴射速度を大きくするには，燃焼温度 $T$ をできるだけ高くし，同時に噴射ガスの分子質量 $m$ ができるだけ小さい物質を選ぶ必要があります。したがって，分子質量が最小である水素分子 $\mathrm{H}_2$ が最良の燃料です。

### (6)

設問 (5) で選んだ水素分子 $\mathrm{H}_2$ の質量は $m = 2m_p$ であり，$m = 3.4 \times 10^{-27}\,\mathrm{kg}$ です。これに $T = 2000\,\mathrm{K}$，$k = 1.4 \times 10^{-23}\,\mathrm{J/K}$ を代入します。

$$
\begin{aligned}
u_0 &= \sqrt{\frac{3 \times 1.4 \times 10^{-23} \times 2000}{2 \times 1.7 \times 10^{-27}}} \\
&= \sqrt{\frac{8.4 \times 10^{-20}}{3.4 \times 10^{-27}}} \\
&= \sqrt{2.47 \times 10^7} \\
&\approx 4.97 \times 10^3\,\mathrm{m/s}
\end{aligned}
$$

有効数字2桁で表すと次の通りです。

$$
\finalanswer{u_0 \approx 5.0 \times 10^3\,\mathrm{m/s} = 5.0\,\mathrm{km/s}}
$$

### (7)

$\dfrac{M_i}{M_f} = 4$ なので，対数は次の値になります。

$$
\begin{aligned}
\ln\frac{M_i}{M_f} &= \ln 4 \\
&= 2\ln 2 \\
&= 2 \times 0.7 \\
&= 1.4
\end{aligned}
$$

静止から打ち上げるとして，(4) の式に $u = 3\,\mathrm{km/s}$，$n = 4$ を代入します。

$$
\begin{aligned}
\Delta v &= \frac{4}{4 + 1} \times 3\,\mathrm{km/s} \times 1.4 \\
&= 0.8 \times 4.2\,\mathrm{km/s} \\
&= 3.36\,\mathrm{km/s}
\end{aligned}
$$

$$
\finalanswer{\Delta v = 3.36\,\mathrm{km/s} \approx 3.4\,\mathrm{km/s}}
$$

これは (1) で求めた脱出速度 $v_{\mathrm{esc}} \approx 11.2\,\mathrm{km/s}$ の約30%にすぎず，単段のロケットではまったく脱出速度に届きません。また (5) と (6) の結果から，最軽量の水素分子を用いても $T = 2000\,\mathrm{K}$ での熱速度の上限は $u_0 \approx 5.0\,\mathrm{km/s}$ 程度であり，仮に $u = 5.0\,\mathrm{km/s}$ を実現しても $\Delta v$ は $5.6\,\mathrm{km/s}$ にとどまります。燃焼温度 $T$ もエンジン材料の耐熱限界から大幅に上げることは困難です。

したがって，1段当たりの質量比 $\dfrac{M_i}{M_f}$ の構造的限界と噴射速度 $u$ の物理的上限のもとで脱出速度を得るには，多段式ロケットにする必要があります。各段の燃料を使い切った時点で空になった燃料タンクやエンジンを切り離して質量を軽くし，次の段を点火して加速を積み重ねれば，1段当たり $\Delta v \approx 3.4\,\mathrm{km/s}$ の4段式ロケットで最終速度が $4 \times 3.36 \approx 13.4\,\mathrm{km/s} > 11.2\,\mathrm{km/s}$ となり，地球の重力圏を脱出できます。なお，赤道付近から地球の自転と同じ東向きに打ち上げて約 $0.46\,\mathrm{km/s}$ の自転速度を上乗せする工夫も補助的に有効です。

<aside class="rigor-note" markdown>
(6) で水素分子 $\mathrm{H}_2$ が高温で完全に原子状水素 $\mathrm{H}$（$m = m_p$）に解離したと仮定しても，$u_0 = \sqrt{2} \times 4.97 \approx 7.0\,\mathrm{km/s}$ となり，(7) の条件で得られる速度変化は $\dfrac{4}{5} \times 7.0 \times 1.4 \approx 7.8\,\mathrm{km/s}$ で依然として脱出速度 $11.2\,\mathrm{km/s}$ に届きません。したがって多段式ロケットが必要であるという結論は変わりません。
</aside>
