<!--
@Author: shumez
@Date:   2018-06-02 13:36:08
@Project: NLDC/docs
@Filename: DOCS.md
@Last modified by:   shumez
@Last modified time: 2018-06-02 13:37:77
-->


# Docs


## Overview

- Part 0
    - [1 Overview](../c01)
        - [1.0 Chaos, Fractals, and Dynamics](#1.0-Chaos,-Fractals,-and-Dynamics)
        - [1.1 Capsule History of Dynamics](#1.1-Capsule-History-of-Dynamics)
        - [1.2 The Importance of Being Nonlinear](#1.2-The-Importance-of-Being-Nonlinear)
            - [Nonautonomous Systems](#Nonautonomous-Systems)
            - [Why Are Nonlinear Problems So Hard?](#Why-Are-Nonlinear-Problems-So-Hard?)
        - [1.3 A Dynamical View of the World](#1.3-A-Dynamical-View-of-the-World)

- Part I One-Dimensional Flows
    - [2 Flows on the line](../c02)
        - [2.0 Introduction](#2.0-Introduction)
        - [2.1 A Geometric way of Thinking](#2.1-A-Geometric-way-of-Thinking)
        - [2.2 Fixed Points and Stability](#2.2-Fixed-Points-and-Stability)
            - [Example 2.2.1](#Example-2.2.1)
            - [Example 2.2.2](#Example-2.2.2)
            - [Example 2.2.3](#Example-2.2.3)
        - [2.3 Population Growth](#2.3-Population-Growth)
            - [Critique of the Logistic Model](#Critique-of-the-Logistic-Model)
        - [2.4 Linear Stability Analysis](#2.4-Linear-Stability-Analysis)
            - [Example 2.4.1](#Example-2.4.1)
        - [2.5 Existence and Uniquness](#2.5-Existence-and-Uniquness)
            - [Example 2.5.1](#Example-2.5.1)
            - [Example 2.5.2](#Example-2.5.2)
        - [2.6 Impossibility of Oscillations](#2.6-Impossibility-of-Oscillations)
            - [Mechanical Analog: Overdamped Systems](#Mechanical-Analog:-Overdamped-Systems)
        - [2.7 Potentials](#2.7-Potentials)

    - [3 Bifurcations](../c03)
        - [3.0 Introduction](#3.0-Introduction)
        - [3.1 Saddle-Node Bifurcation](#3.1-Saddle-Node-Bifurcation)
            - [Graphical Conventions](#Graphical-Conventions)
            - [Terminology](#Terminology)
            - [Exmaple 3.1.1](#Exmaple-3.1.1)
            - [Normal Forms](#Normal-Forms)
        - [3.2 Transcritical Bifurcation](#3.2-Transcritical-Bifurcation)
            - [Example 3.2.1](#Example-3.2.1)
            - [Example 3.2.2](#Example-3.2.2)
        - [3.3 Laser Threshold](#3.3-Laser-Threshold)
            - [Physical Background](#Physical-Background)
            - [Model](#Model)
        - [3.4 Pitchfolk Bifurcation](#3.4-Pitchfolk-Bifurcation)
            - [Supercritical Pitchfork Bifurcation](#Supercritical-Pitchfork-Bifurcation)
            - [Exmaple 3.4.1](#Exmaple-3.4.1)
            - [Example 3.4.2](#Example-3.4.2)
            - [Subcritical Pitchfork Bifurcation](#Subcritical-Pitchfork-Bifurcation)
            - [Terminology](#Terminology)
        - [3.5 Overdamped Bead on a Rotating Hoop](#3.5-Overdamped-Bead-on-a-Rotating-Hoop)
            - [Analysis of the First-Order System](#Analysis-of-the-First-Order-System)
            - [Dimensional Analysis and Scaling](#Dimensional-Analysis-and-Scaling)
            - [A Paradox](#A-Paradox)
            - [Phase Plane Analysis](#Phase-Plane-Analysis)
            - [A Singular Limit](#A-Singular-Limit)
        - [3.6 Imperfect Bifurcation and Catastrophes](#3.6-Imperfect-Bifurcation-and-Catastrophes)
            - [Bead on a Tilted Wire](#Bead-on-a-Tilted-Wire)
        - [3.7 Insect Outbreak](#3.7-Insect-Outbreak)
            - [Model](#Model)
            - [Dimentionless Formulation](#Dimentionless-Formulation)
            - [Analysis of Fixed Points](#Analysis-of-Fixed-Points)
            - [Calculating the Bifurcation Curves](#Calculating-the-Bifurcation-Curves)
            - [Comparison with Observation](#Comparison-with-Observation)

    - [4 Flows on the Circle](../c04)
        - [4.0 Introduction](#4.0-Introduction)
        - [4.1 Examples and Definitions](#4.1-Examples-and-Definitions)
            - [Example 4.1.1](#Example-4.1.1)
            - [Example 4.1.2](#Example-4.1.2)
        - [4.2 Uniform Oscillator](#4.2-Uniform-Oscillator)
            - [Example 4.2.1](#Example-4.2.1)
        - [4.3 Nonuniform Oscillator](#4.3-Nonuniform-Oscillator)
            - [Example 4.3.1](#Example-4.3.1)
            - [Oscillation Period](#Oscillation-Period)
            - [Ghosts and Bottlenecks](#Ghosts-and-Bottlenecks)
            - [Example 4.3.2](#Example-4.3.2)
        - [4.4 Overdamped Pendulum](#4.4-Overdamped-Pendulum)
        - [4.5 Fireflies](#4.5-Fireflies)
            - [Model](#Model)
        - [4.6 Superconducting Josephson Junctions](#4.6-Superconducting-Josephson-Junctions)
            - [Physical Background](#Physical-Background)
            - [The Josephson Relations](#The-Josephson-Relations)
            - [Equivalent Circuit and Pendulum Analog](#Equivalent-Circuit-and-Pendulum-Analog)
            - [Typical Parameter Values](#Typical-Parameter-Values)
            - [Dimensionless Formulation](#Dimensionless-Formulation)
            - [Example 4.6.1](#Example-4.6.1)

    - [5 Linear Systems](../c05)
        - [5.0 Introduction](#5.0-Introduction)
        - [5.1 Definitions and Exmaples](#5.1-Definitions-and-Exmaples)
            - [Example 5.1.1](#Example-5.1.1)
            - [Stability Language](#Stability-Language)
        - [5.2 Classification of Linear Systems](#5.2-Classification-of-Linear-Systems)
            - [Example 5.2.1](#Example-5.2.1)
            - [Example 5.2.2](#Example-5.2.2)
            - [Classification of Fixed Points](#Classification-of-Fixed-Points)
            - [Example 5.2.6](#Example-5.2.6)
            - [Example 5.2.7](#Example-5.2.7)
        - [5.3 Love Affairs](#5.3-Love-Affairs)
            - [Example 5.3.1](#Example-5.3.1)

    - [6 Phase Plane](../c06)
        - [6.0 Introduction](#6.0-Introduction)
        - [6.1 Phase Portraits](#6.1-Phase-Portraits)
             - [Numerical Computaion of Phase Portraits](#Numerical-Computaion-of-Phase-Portraits)
             - [Example 6.1.1](#Example-6.1.1)
        - [6.2 Exsitence, Uniquness, and Topological Consequences](#6.2-Exsitence,-Uniquness,-and-Topological-Consequences)
            - [Existence and Uniquness Theorem](#Existence-and-Uniquness-Theorem)
        - [6.3 Fixed Points and Linearization](#6.3-Fixed-Points-and-Linearization)
            - [Linearized System](#Linearized-System)
            - [The Effect of Small Nonlinear Terms](#The-Effect-of-Small-Nonlinear-Terms)
            - [Example 6.3.1](#Example-6.3.1)
            - [Example 6.3.2](#Example-6.3.2)
            - [Robust cases](#Robust-cases)
            - [Hyperbolic Fixed Points, Topological Equivalence, and Structural Stability](#Hyperbolic-Fixed-Points,-Topological-Equivalence,-and-Structural-Stability)
        - [6.4 Rabbits versus Sheep](#6.4-Rabbits-versus-Sheep)
        - [6.5 Conservative Systems](#6.5-Conservative-Systems)
            - [Example 6.5.1](#Example-6.5.1)
            - [Example 6.5.2](#Example-6.5.2)
            - [Example 6.5.3](#Example-6.5.3)
            - [Nonlinear Centers](#Nonlinear-Centers)


```
NLDC
├── CHANGELOG.md
├── LICENSE.md
├── README.md
├── c01
│   └── note.ipynb
├── c02
│   ├── README.md
│   ├── img
│   └── note.ipynb
├── c03
│   ├── README.md
│   ├── code
│   ├── img
│   └── note.ipynb
├── c04
│   ├── README.md
│   ├── code
│   ├── img
│   └── note.ipynb
├── c05
│   ├── README.md
│   ├── code
│   ├── img
│   └── note.ipynb
├── c06
│   ├── README.md
│   ├── code
│   ├── img
│   └── note.ipynb
├── c07
│   ├── README.md
│   ├── code
│   ├── img
│   └── note.ipynb
└── docs
    ├── DOCS.md
    └── book.bibtex
```
