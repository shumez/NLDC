<!--
Filename: 	note.md
Project: 	/Users/shume/Developer/NLDC/02
Author: 	shumez <https://github.com/shumez>
Created: 	2019-04-29 19:27:2
Modified: 	2019-05-02 20:50:48
-----
Copyright (c) 2019 shumez
-->

# 02. Flows on the line

## ToC

* [02.00. Introduction](#0200_introduction)
* [02.01. A Geometric way of Thinking](#0201_a_geometric_way_of_thinking)
* [02.02. Fixed Points and Stability](#0202_fixed_points_and_stability)
    * [02.02.01. Example 2.2.1](#020201_example_221)
    * [02.02.02. Example 2.2.2](#020202_example_222)
    * [02.02.03. Example 2.2.3](#020203_example_223)
* [02.03. Population Growth](#0203_population_growth)
    * [02.03.01. Critique of the Logistic Model](#020301_critique_of_the_logistic_model)
* [02.04. Linear Stability Analysis](#0204_linear_stability_analysis)
    * [02.04.01. Example 2.4.1](#020401_example_241)
    * [02.04.02. Example 2.4.2](#020402_example_242)
    * [02.04.03. Example 2.4.3](#020403_example_243)
* [02.05. Existence and Uniquness](#0205_existence_and_uniquness)
    * [02.05.01. Example 2.5.1](#020501_example_251)
    * [02.05.02. Example 2.5.2](#020502_example_252)
* [02.06. Impossibility of Oscillations](#0206_impossibility_of_oscillations)
    * [02.06.01. Mechanical Analog: Overdamped Systems](#020601_mechanical_analog_overdamped_systems)
* [02.07. Potentials](#0207_potentials)
    * [02.07.01. Example 2.7.1](#020701_example_271)
    * [02.07.02. Example 2.7.2](#020702_example_272)
* [02.08. Solving Equations on the Computer](#0208_solving_equations_on_the_computer)
    * [02.08.01. Euler's Method](#020801_eulers_method)
    * [02.08.02. Example 2.8.1](#020802_example_281)



## 02.00. Introduction

$$
    \begin{align*}
        \dot{x}_1 &= f_1(x_1, \cdots, x_n) \\
        & \vdots \\
        \dot{x}_n &= f_n(x_1, \cdots, x_n)
    \end{align*}
$$

$n = 1$

$$ \dot{x} = f(x) $$

**one-dimensinal** / **first-order system**


## 02.01. A Geometric way of Thinking

$$ \dot{x} = \sin x \tag{1} $$

$$ dt = \frac{dx}{\sin x} $$

implies: 
$$
    \begin{align*}
        t &= \int \csc x \, \mathrm{d}x \\
        &= - \ln |\csc x + \cot x | + C
    \end{align*}
$$

$$ t = \ln \Big|\frac{\csc x_0 + \cot x_0}{\csc x + \cot x}\Big| \tag{2} $$

[![fig.2.1.1][fig_02_01_01]][fig_02_01_01]

**fixed point**
- **stable**
- **unstable**


## 02.02. Fixed Points and Stability

- **phase point**: imaginary point
- **phase portrait**: qualitatively different trajectories


### 02.02.01. Example 2.2.1

$$ \dot{x} = x^2 - 1 $$

[![Fig.2.2.2][fig_02_02_02]][fig_02_02_02]


### 02.02.02. Example 2.2.2

$$ -V_0 + RI + \frac{Q}{C} = 0 $$
$$ \dot{Q} = I $$

$$ - V_0 + R\dot{Q} + \frac{Q}{C} = 0 $$
$$ \dot{Q} = f(Q) = \frac{V_0}{R} - \frac{Q}{RC} $$


### 02.02.03. Example 2.2.3

$$ \dot{x} = x - \cos{x} $$


## 02.03. Population Growth

$$ \dot{N} = rN $$

$$ N(t) = N_0e^rt $$

**Carrying capacity**: $K$

**Logistic eq**
$$ \dot{N} = rN \Big(1 - \frac{N}{K} \Big) $$


### 02.03.01. Critique of the Logistic Model

## 02.04. Linear Stability Analysis

Let 
- $ x\ast $: fixed point

$$ \eta(t) = x(t) - x\ast $$

$$ \dot{\eta} = \frac{d}{dt} (x - x\ast) = \dot{x} $$

- $ x\ast $: constant

$$ \dot{\eta} = \dot{x} = f(x) = f(x\ast + \eta) $$

Taylor's expansion:
$$ f(x\ast + \eta) = f(x\ast) + \eta f'(x\ast) + O(\eta^2) $$

- $ O(\eta^2) $: quadratically small term in $ \eta $

$$ \dot{\eta} = \eta f'(x\ast) + O(\eta^2) $$

$$ \dot{\eta} \approx \eta f'(x\ast) $$


### 02.04.01. Example 2.4.1

using linear stability analysis:
$$ \dot{x} = \sin{x} $$

*Solution:*

$$
    \begin{align*}
        f'(x*) 
        &= \cos k\pi \\
        &=
        \begin{cases}
            1, &\quad k \, \text{even} \\
            -1, &\quad k \, \text{odd}
        \end{cases}
    \end{align*}
$$


### 02.04.02. Example 2.4.2

using linear stability analysis 

*Solution:*

$$ f(N) = rN(1 - \frac{N}{K}) $$

$ N* = 0 $, $ N* = K $

$$ f'(N) = r - \frac{2rN}{K} $$

$ f'(0)=r $, $ f'(K)=-r $


### 02.04.03. Example 2.4.3

1. $ \dot{x} = - x^3 $
2. $ \dot{x} = x^3 $
3. $ \dot{x} = x^2 $
4. $ \dot{x} = 0 $


## 02.05. Existence and Uniquness

$ \dot{x} = f(x) $

### 02.05.01. Example 2.5.1

$$ \dot{x} = x^{\frac{1}{3}} $$

*Solution:*

$$ \int x^{-\frac{1}{3}} dx = \int dt $$

$$ \frac{3}{2} x^{\frac{2}{3}} = t + C $$


### 02.05.02. Example 2.5.2

$$
    \begin{align*}
        \dot{x} &= 1 + x^2 \\
        x(0) &= x_0
    \end{align*}
$$


## 02.06. Impossibility of Oscillations

### 02.06.01. Mechanical Analog: Overdamped Systems

$ \dot{x} = f(x) $ can't oscillate
limiting case of Newton's law

intertia term $ m\ddot{x} $ is negligible

$$ m\ddot{x} + b\dot{x} = F(x) $$

$ b\dot{x} \gg m\ddot{x} $


## 02.07. Potentials

another way to visualize 1st-order system $ \dot{x} = f(x) $

$$ \dot{x} = f(x) = - \frac{dV}{dx} $$

$$ \frac{dV}{dt} = \frac{dV}{dx} \frac{dx}{dt} $$

$$ \frac{dx}{dt} = - \frac{dV}{dx} $$

$$ \frac{dV}{dt} = - \Big( \frac{dV}{dx} \Big)^2 ≤ 0 $$


### 02.07.01. Example 2.7.1

Graph the potential fot the system: $ \dot{x} = - x $

*Solution:*

$ - \frac{dV}{dx} = -x $
general solution: $ V(x) = \frac{1}{2} x^2 + C $


### 02.07.02. Example 2.7.2

Graph the potential for the system: $ \dot{x} = x - x^3 $

*Solution:*

$ -\frac{dV}{dx} = x-x^3 $
$$ V = -\frac{1}{2} x^2 + \frac{1}{4} x^4 + C $$


## 02.08. Solving Equations on the Computer

- graphical
- analytical 
- **numerical method**


**numerical intergration**


### 02.08.01. Euler's Method

$$ \dot{x} = f(x) $$

$$
    \begin{align*}
        x(t_0 + \Delta t) &\approx x_1 \\
        &= x_0 + f(x_0) \Delta t
    \end{align*}
$$

$$ x_{n+1} = x_n + f(x_n) \Delta t $$


**fourth-order Runge-Kutta method**

$$
    \begin{cases}
        k_1 = f(x_n) \Delta t \\
        k_2 = f(x_n + \frac{1}{2} k_1) \Delta t \\
        k_3 = f(x_n + \frac{1}{2} k_2) \Delta t \\
        k_4 = f(x_n + k_3) \Delta t \\
    \end{cases} \\
    x_{n+1} = x_n + \frac{1}{6} (k_1 + 2 k_2 + 2 k_3 + k_4)
$$


### 02.08.02. Example 2.8.1


Solve the system $\dot{x} = x (1 - x)$ numerically

*Solution:*







##

<!-- ref -->

<!-- fig -->
[fig_02_01_01]: img/fig_02_01_01.png
[fig_02_02_02]: img/fig_02_02_02.png

<style type="text/css">
	img{width: 51%; float: right;}
</style>