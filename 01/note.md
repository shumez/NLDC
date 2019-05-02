<!--
Filename: 	note.md
Project: 	/Users/shume/Developer/NLDC/01
Author: 	shumez <https://github.com/shumez>
Created: 	2019-04-29 19:27:6
Modified: 	2019-05-02 20:39:24
-----
Copyright (c) 2019 shumez
-->

# 01. Overview

## ToC

* [01.00. Chaos, Fractals, and Dynamics](#1.0-Chaos,-Fractals,-and-Dynamics)
* [01.01. Capsule History of Dynamics](#1.1-Capsule-History-of-Dynamics)
* [01.02. The Importance of Being Nonlinear](#1.2-The-Importance-of-Being-Nonlinear)
    * [Nonautonomous Systems](#Nonautonomous-Systems)
    * [Why Are Nonlinear Problems So Hard?](#Why-Are-Nonlinear-Problems-So-Hard?)
* [01.03. A Dynamical View of the World](#0103-A-Dynamical-View-of-the-World)


## 01.00. Chaos, Fractals, and Dynamics


## 01.01. Capsule History of Dynamics


## 01.02. The Importance of Being Nonlinear

\[ m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + kx = 0 \tag{1} \]

\[ \frac{\partial u}{\partial t} = \frac{\partial ^2 u}{\partial x^2} \]

\[
    \begin{align*}
        \dot{x}_1 &= f_1(x_1, \cdots , x_n) \\
        & \vdots \\
        \dot{x}_n &= f_n(x_1, \cdots , x_n)
    \end{align*}
    \tag{2}
\]

\[ \dot{x}_1 \equiv \frac{dx_i}{dt} \]

\[
    \begin{align*}
        \dot{x}_2 
        &= \ddot{x} = - \frac{b}{m} \dot{x} - \frac{k}{m} x \\
        &= - \frac{b}{m} x_2 - \frac{k}{m} x_1
    \end{align*}
\]


\[
    \begin{cases}
        \dot{x}_1 &= x_2 \\
        \dot{x}_2 &= - \frac{b}{m} x_2 - \frac{k}{m} x_1
    \end{cases}
\]

**nonlinear**

e.g., pendulum

\[
    \begin{cases}
        \dot{x}_1 = x_2 \\
        \dot{x}_2 = - \frac{g}{L} \sin(x_1)
    \end{cases}
\]

- \( x \)
- \( g \): gravity acceleration
- \( L \): length


### 01.02.01. Nonautonomous Systems

**forced harmonic oscillator**

\[ m\ddot{x} + b\dot{x} + kx = F \cos t \]

let:
- \(x_1 = x\)
- \(x_2 = \dot{x}\)
- \(x_3 = t\), then \(\dot{x}_3 = 1\)

\[
    \begin{cases}
        \dot{x}_1 = x_2 \\
        \dot{x}_2 = \frac{1}{m} (-kx_1 - bx_2 + F\cos x_3) \\
        \dot{x}_3 = 1
    \end{cases}
    \tag{3}
\]


### 01.02.02. Why Are Nonlinear Problems So Hard?


## 01.03. A Dynamical View of the World

growth of population

\[ \dot{x} = r x \]

swinging of pendulum 

\[ \ddot{x} + \frac{g}{L} \sin{x} = 0 \]

|           | \(n=1\) | \(n=2\) | \(n\ge3\) | \(n\gg1\) | Continuum |
|----------:|:-----:|:-----:|:-------:|:-------:|:---------:|
| Linear    | **Growth, decay, equilibrilium** Exponential growth, RC circuit, Radioactive decay | **Oscillation** Linear oscillator, Mass and spring, RLC circuit, 2-body problem | | **Collective phenomenon** | **Waves & pattern** |
| Nonlinear | Fixed points, Bifurcation, Overdampled system, Logistic equation | Pendlum, Anharmonic oscillator, Limit cycle, Biological oscillator,  | **Chaos** | | **Spatio-temporal complexity** |


##

<!-- ref -->

<!-- fig -->

<!-- <style type="text/css">
	img{width: 51%; float: right;}
</style> -->