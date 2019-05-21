<!--
Filename: 	note.md
Project: 	/Users/shume/Developer/NLDC/03
Author: 	shumez <https://github.com/shumez>
Created: 	2019-04-29 19:27:0
Modified: 	2019-05-21 20:42:16
-----
Copyright (c) 2019 shumez
-->

# 03. Bifurcations

## ToC

* [03.00. Introduction][0300]
* [03.01. Saddle-Node Bifurcation][0301]
    * [03.01.01. Graphical Conventions][030101]
        * [03.01.01.01 Terminology][03010101]
    * [Example 3.1.1][example311]
    * [Example 3.1.2][example312]
    * [03.01.02. Normal Forms][030102]
* [03.02. Transcritical Bifurcation][0302]


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

### Example 3.1.1

linear stability analysis of fixed point: \( \dot{x} = f(x) = r - x^2 \)

*Solution*

\(x^\ast = \pm \sqrt{r}\)


### Example 3.1.2

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
        &= f(x^\ast, r_c) + (x - x^\ast) \frac{\partial f}{\partial x} \Bigg|_{(x^\ast, r_c)} + (r - r_c) \frac{\partial f}{\partial r} \Bigg|_{(x^\ast, r_c)} + \frac{1}{2} (x - x^\ast)^2 \frac{\partial^2 f}{\partial x^2} \Bigg|_{(x^\ast, r_c)} + \cdots
    \end{align*}
\]

\(f(x^\ast, r_c) = 0\) (&lArr; \(x^\ast\) is fixed point), \(\frac{\partial f}{\partial x}|_{(x^\ast, r_c)} = 0\) 

\[ \dot{x} = a(r - r_c) + b(x - x^\ast) + \cdots \tag{3} \]

where \(a = \frac{\partial f}{\partial x}|_{(x^\ast, r_c)}\), \(b = \frac{1}{2} \frac{\partial^2 f}{\partial x^2}|_{(x^\ast, r_c)}\)

**normal forms**

[Guckenheimier, Holmes (1983)][1983_Holmes_Guckenhemier], [Wiggins (1990)][1990_Wiggins]


## 03.02. Transcritical Bifurcation

**transcritical bifurcation**

\[ \dot{x} = rx - x^2 \tag{1} \]

[![Fig.3.2.1][fig030201]][fig030201]

[![Fig.3.2.2][fig030201]][fig030201]

##
[0300]: #0300_introduction
[0301]: #0301_saddle-node_bifurcation
[030101]: #030101_graphical_conventions
[03010101]: #03010101_terminology
[example311]: #example_311
[example312]: #example_312
[030102]: #030102_normal_forms
[0302]: #0302_transcritical_bifurcation

<!-- ref -->

<!-- fig -->
[fig030101]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030101.png
[fig030103]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030103.png
[fig030106]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030106.png
[fig030106-1]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030106-1.png
[fig030107]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030107.png
[fig030201]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030201.png
[fig030202]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030202.png

<style type="text/css">
	img{width: 51%; float: right;}
</style>