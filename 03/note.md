<!--
Filename: 	note.md
Project: 	/Users/shume/Developer/NLDC/03
Author: 	shumez <https://github.com/shumez>
Created: 	2019-04-29 19:27:0
Modified: 	2019-05-21 17:01:39
-----
Copyright (c) 2019 shumez
-->

# 03. Bifurcations

## ToC

* [03.00. Introduction][0300]
* [03.01. Saddle-Node Bifurcation][0301]
    * [03.01.01. Graphical Conventions][030101]
    * [03.01.02. Terminology][030102]
    * [Example 3.1.1][example311]
    * [Example 3.1.2][example312]


## 03.00. Introduciton

**birfurcation**

## 03.01. Saddle-Node Bifurcation

\[ \dot{x} = r + x^2 \tag{1} \]

[![Fig.3.1.1][fig030101]][fig030101]


### 03.01.01. Graphical Conventions

bifurcation diagram

[![Fig.3.1.3][fig030103]][fig030103]


### 03.01.02. Terminology

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


##
[0300]: #0300_introduction
[0301]: #0301_saddle-node_bifurcation
[030101]: #030101_graphical_conventions
[030102]: #030102_terminology
[example311]: #example_311
[example312]: #example_312

<!-- ref -->

<!-- fig -->
[fig030101]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030101.png
[fig030103]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030103.png
[fig030106]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030106.png
[fig030106-1]: https://raw.githubusercontent.com/shumez/NLDC/master/03/fig/fig030106-1.png

<style type="text/css">
	img{width: 51%; float: right;}
</style>