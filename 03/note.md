<!--
Filename: 	note.md
Project: 	/Users/shume/Developer/NLDC/03
Author: 	shumez <https://github.com/shumez>
Created: 	2019-04-29 19:27:0
Modified: 	2019-07-02 17:42:31
-----
Copyright (c) 2019 shumez
-->

# 03. Bifurcations

## Contents

* [03.00. Introduction][0300]
* [03.01. Saddle-Node Bifurcation][0301]
    * [03.01.01. Graphical Conventions][030101]
        * [03.01.01.01 Terminology][03010101]
    * [Example 03.01.01.][ex030101]
    * [Example 03.01.02.][ex030102]
    * [03.01.02. Normal Forms][030102]
* [03.02. Transcritical Bifurcation][0302]
    * [Example 03.02.01.][ex030201]
    * [Example 03.02.02.][ex030202]
* [03.03. Laser Threshold][0303]
    * [03.03.01. Physical Background][030301]
    * [03.03.02. Model][030302]
* [03.04. Pitchfork Bifurcation][0304]
    * [03.04.01. Supercritical Pitchfork Bifurcation][030401]
    * [Example 03.04.01.][ex030401]
    * [Example 03.04.02.][ex030402]
    * [03.04.02. Subcritical Pitchfork Bifurcation][030402]
    * [03.04.03. Terminology][030403]
* [03.05. Overdamped Bead on a Rotating Hoop][0305]
    * [03.05.01. Analysis of the First-Order System][030501]
    - [03.05.02. Dimensional Analysis and Scaling][030502]


## 03.00. Introduciton

**birfurcation**

## 03.01. Saddle-Node Bifurcation

\[ \dot{x} = r + x^2 \tag{1} \]

[![Fig.3.1.1][fig030101]][fig030101]


### 03.01.01. Graphical Conventions

bifurcation diagram

[![Fig.3.1.3][fig030103]][fig030103]


#### 03.01.01.01. Terminology

**fold bifurcation** (aka, **tuning-point bifurcation**, **blue sky bifurcation**)

[Abraham, Shaw (1988)][1988_Shaw_Abraham]

\[ \dot{x} = r - x^2 \tag{2} \]

### Example 03.01.01.

linear stability analysis of fixed point: \( \dot{x} = f(x) = r - x^2 \)

*Solution*

\(x^\ast = \pm \sqrt{r}\)


### Example 03.01.02.

\[ \dot{x} = r - x - e^{-x} \]

**Solution:**

[![Fig.3.1.6][fig030106]][fig030106]

[![Fig.3.1.6-1][fig030106-1]][fig030106-1]

derivative:

\[ e^{-x} = r - x \]

and

\[ \frac{d}{dx} e^{-x} = \frac{d}{dx} (r - x) \]

\(-e^{-x}=-1\), \(x=0\)

\(r_c=1\)


### 03.01.02. Normal Forms

Taylor expansion

\[
    \begin{align*}
        \dot{x} 
        &= r - x - e^{-x} \\
        &= r - x - \bigg[ 1 - x + \frac{x^2}{2!} + \cdots \bigg] \\
        &= (r - 1) - \frac{x^2}{2} + \cdots
    \end{align*}
\]

[![Fig.3.1.7][fig030107]][fig030107]

bifurcation at \(x=x^\ast\), \(r=r_c\)
Taylor's expansion

\[
    \begin{align*}
        \dot{x} 
        &= f(x, r) \\
        &= f(x^\ast, r_c) + (x - x^\ast) \frac{\partial f}{\partial x} \Bigg|_{(x^\ast, r_c)} \\
        &+ (r - r_c) \frac{\partial f}{\partial r} \Bigg|_{(x^\ast, r_c)} \\
        &+ \frac{1}{2} (x - x^\ast)^2 \frac{\partial^2 f}{\partial x^2} \Bigg|_{(x^\ast, r_c)} + \cdots
    \end{align*}
\]

\(f(x^\ast, r_c) = 0\) (&lArr; \(x^\ast\) is fixed point), \(\frac{\partial f}{\partial x}|_{(x^\ast, r_c)} = 0\) 

\[ \dot{x} = a(r - r_c) + b(x - x^\ast) + \cdots \tag{3} \]

where \(a = \frac{\partial f}{\partial x}|_{(x^\ast, r_c)}\), \(b = \frac{1}{2} \frac{\partial^2 f}{\partial x^2}|_{(x^\ast, r_c)}\)

**normal forms**

[Guckenheimier, Holmes (1983)][1983_Holmes_Guckenheimier], [Wiggins (1990)][1990_Wiggins]


## 03.02. Transcritical Bifurcation

**transcritical bifurcation**

\[ \dot{x} = rx - x^2 \tag{1} \]

[![Fig.3.2.1][fig030201]][fig030201]

[![Fig.3.2.2][fig030202]][fig030202]

### Example 03.02.01.

show the first-order system
\[ \dot{x} = x(1 - x^2) - a(1 - e^{-hx}) \]

*Solution*:

\[ 
    \begin{align*}
        1 - e^{-hx} 
        &= 1 - \Big[ 1 - bx + \frac{1}{2} b^2 x^2 + O(x^3) \Big] \\
        &= bx - \frac{1}{2} b^2 x^2 + O(x^3)
    \end{align*}
\]

\[
    \begin{align*}
        \dot{x}
        &= x - a (bx - \frac{1}{2} b^2 x^2) + O(x^3) \\
        &= (1 - ab) x + (\frac{1}{2} ab^2) x^2 + O(x^3)
    \end{align*}
\]

\[ x^\ast \approx \frac{2 (ab - 1)}{ab^2} \]


### Example 03.02.02.

analyze

\[ \dot{x} = r\ln{x} + x - 1 \]

near \(x = 1\)

*Solution*:

\(u := x-1\)

\[
    \begin{align*}
        \dot{u} 
        &= \dot{x} \\
        &= r\ln{(1 + u)} + u \\
        &= r \Big[ u - \frac{1}{2} u^2 + O(u^3) \Big] + u \\
        &\approx (r + 1) u - \frac{1}{2} ru^2 + O(u^3)
    \end{align*}
\]

\[ \dot{v} = (r + 1) v - (\frac{1}{2}ra) v^2 + O(v^3) \]

\(a=\frac{2}{r}\)

\[ \dot{v} = (r + 1)v - v^2 + O(v^3) \]

\(R := r + 1\) and \(X := v\)

\[ \dot{X} \approx RX - X^2 \]

\[ X = v = \frac{u}{a} = \frac{1}{2} r(x-1) \]

([Guckenheimer and Holmes (1983)][1983_Holmes_Guckenheimier], [Wiggins (1990)][1990_Wiggins], [Manneville (1990)][1990_Manneville])


## 03.03. Laser Threshold

[Hanken (1983)][1983_Hanken]

### 03.03.01. Physical Background

**solid-state laser**

### 03.03.02. Model

[Milonmi and Eberly (1988)][1988_Eberly_Milonmi]

[Hanken (1983)][1983_Hanken]

[![Fig.3.3.2][fig030302]][fig030302]

[![Fig.3.3.3][fig030303]][fig030303]

\(n(t)\): num of photons 

\[
    \begin{align*}
        \dot{n} 
        &= \text{gain} - \text{loss} \\
        &= GnN - kn
    \end{align*}
\]

**simulated emission**



* \(N(t)\): num of excited atoms
* \(G (>0)\): gain coef
* \(k (>0)\): rate constant; 
* \(\tau = \frac{1}{k}\): lifetime of photon in laser

\[ N(t) = N_0 - \alpha n \]

* \(\alpha\): rate at which atoms drop back to graund state

Substitute: 
\[
    \begin{align*}
        \dot{n} 
        &= Gn(N_0 - \alpha n) - kn \\
        &= (GN_0 - k) n - \alpha G n^2
    \end{align*}
\]


## 03.04. Pitchfork Bifurcation

**Pitchfork bifurcation**

**symmetry**


### 03.04.01. Supercritical Pitchfork Bifurcation

\[ \dot{x} = rx - x^3 \tag{1} \]

[![Fig.3.4.1][fig030401]][fig030401]

[![Fig.3.4.2][fig030402]][fig030402]


### Example 03.04.01.

\[ \dot{x} = - x + \beta \tanh{x} \]

[![Fig.3.4.3][fig030403]][fig030403]


[![Fig.3.4.4][fig030404]][fig030404]

### Example 03.04.02.

[![Fig.3.4.5][fig030405]][fig030405]

Plot potential \(V(x)\) for the system \(\dot{x} = rx = x^3\)

*Solution*

\(f(x) = \frac{-dV}{dx}\) 

\(V(x) = -\frac{1}{2}rx^2 + \frac{1}{4} x^4\)


### 03.04.02. Subcritical Pitchfork Bifurcation

[![Fig.3.4.6][fig030406]][fig030406]

\[ \dot{x} = rx + x^3 \tag{2} \]

[![Fig.3.4.7][fig030407]][fig030407]

\[ \dot{x} = rx + x^3 - x^5 \tag{3} \]


### 03.04.03. Terminology

* Supercritial pitchfork
    * aka, **Forward** bifurcation
    * soft/safe
* Subcritical pitchfork
    * aka, **Backward** bifurcation
    * hard/dangerous


## 03.05. Overdamped Bead on a Rotating Hoop

Let 

* \(\phi\): angle (\(-\pi < \phi ≤ \pi\))
* \(\rho := r \sin{\phi}\)

[![Fig.3.5.2][fig030502]][fig030502]

\[ 
    \begin{align*}
        mr\ddot{\phi} = - b\dot{\phi} - mg\sin \phi + mr\omega^2 \sin \phi \cos \phi
        \tag{3.5.1}
    \end{align*}
\]

### 03.05.01. Analysis of the First-Order System

\[
    \begin{align*}
        b \dot{\phi} 
        &= - mg \sin \phi + mr\omega^2 \sin \phi \cos \phi \\
        &= mg \sin \phi \Big( \frac{r\omega^2}{g} \cos \phi - 1 \Big)
    \end{align*}
    \tag{3.5.2}
\]

where \(\sin\phi = 0\), \(\phi^* = 0, \pi\)

additional fixed points, if \(\frac{r\omega^2}{g} > 1\)

\[ \phi^* = ± \cos^{-1} \bigg( \frac{g}{r\omega^2} \bigg) \]

introduce param \(\gamma\),  
\(\gamma = \frac{r\omega^2}{g} \)

solve \( \cos{\phi^*} = \frac{1}{\gamma} \)

[![Fig.3.5.6][fig030506]][fig030506]


### 03.05.02. Dimensional Analysis and Scaling

##
<!-- toc -->
[0300]: #0300_introduction
[0301]: #0301_saddle-node_bifurcation
[030101]: #030101_graphical_conventions
[03010101]: #03010101_terminology
[ex030101]: #example_030101
[ex030102]: #example_030102
[030102]: #030102_normal_forms
[0302]: #0302_transcritical_bifurcation
[ex030201]: #example_030201
[ex030202]: #example_030202
[0303]: #0303_laser_threshold
[030301]: #030301_physical_background
[030302]: #030302_model
[0304]: #0304_pitchfork_bifurcation
[030401]: #030401_supercritical_pitchfork_bifurcation
[ex030401]: #example_030401
[ex030402]: #example_030402
[030402]: #030402_subcritical_pitchfork_bifurcation
[030403]: #030403_terminology
[0305]: #0305_overdamped_bead_on_a_rotating_hoop
[030501]: #030501_analysis_of_the_first-order_system
[030502]: #030502_dimensional_analysis_and_scaling

<!-- ref -->
[1983_Holmes_Guckenheimier]: #030102 "Guckenheimer and Holmes (1983)"
[1990_Wiggins]: #030102 "Wiggins (1990)"
[1990_Manneville]: #example_030202 "Manneville (1990)"
[1983_Hanken]: #0303 "Hanken (1983)"
[1988_Eberly_Milonmi]: #030302 "Milonmi and Eberly (1988)"

<!-- fig -->
[fig030101]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030101.png
[fig030103]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030103.png
[fig030106]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030106.png
[fig030106-1]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030106-1.png
[fig030107]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030107.png
[fig030201]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030201.png
[fig030202]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030202.png
[fig030302]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030302.png
[fig030303]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030303.png
[fig030401]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030401.png
[fig030402]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030402.png
[fig030403]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030403.png
[fig030404]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030404.png
[fig030405]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030405.png
[fig030406]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030406.png
[fig030407]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030407.png
[fig030502]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030502.png
[fig030506]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/030506.png

<style type="text/css">
	img{width: 51%; float: right;}
</style>