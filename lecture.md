# Fall 2018 275 Lecture notes 

**[Book]** L. Lin and J. Lu, Mathematical introduction to electronic
structure theory (preliminary draft, available on bCourses)

**[Sak]** J. J. Sakurai, Modern quantum Mechanics, Addison-Wesley, 1994

**[Gus]** S. Gustafson and I. Sigal, Mathematical concepts of quantum
mechanics, second edition, 2011

## Lecture 1 (8/22)

Introduction. Stern-Gerlach experiment.

Introducing Julia. 

[Handout slides](https://github.com/lin-lin/2018Fall_228A/blob/master/others/228A_Note_general.pdf)


**Note**: v0.7 and v1.0 released on 8/8/2018 introduces many breaking
changes. So there is a bit learning curve if you are somewhat familiar
with previous versions of Julia before. I compiled a few things below I
noticed when migrating my old code snippets and notebooks used in the
lecture in this [pdf file](https://github.com/lin-lin/2018Fall_228A/blob/master/others/JuliaChange_v0.7.pdf).

Here is a notebook introducing some basic features of Julia.

[Notebook: Julia tutorial](http://nbviewer.jupyter.org/github/lin-lin/2018Fall_228A/blob/master/notebooks/Basics.ipynb), v0.7 compatible

Here are a few other online documents (some information may be
out-of-date).

[Learn X in Y minutes](https://learnxinyminutes.com/docs/julia/)

[The Julia Express](http://bogumilkaminski.pl/files/julia_express.pdf)

[Steven Johnson's Julia-intro](https://github.com/lin-lin/2018Fall_228A/blob/master/others/Julia-intro.pdf) 

[MATLAB–Python–Julia cheatsheet](https://cheatsheets.quantecon.org/)

[Julia manual](https://docs.julialang.org/en/stable/)

## Lecture 2 (8/24)

State space. Operator. Measurement. Spin-1/2 operator.

**Reading**: [Book] 1.1, [Sak] 1.1-1.5

## Lecture 3 (8/27)

Uncertainty principle; Schr\"odinger equation; Tensor product of Hilbert
spaces.

**Reading**: [Book] 1.5, [Sak] 1.3-1.5, [Gus] 1.2-1.4


## Lecture 4 (8/29)

Spin singlet / tripets; Quantum mechnaics in the real space 

**Reading**: [Book] 1.2, [Sak] 1.6-1.7, [Gus] 2.1-2.2


## Lecture 5 (8/31)

Momentum; Canonical relation; Angular momentum; Hydrogen atom

**Reading**: [Book] 1.3, [Sak] 2.1-2.4, 3.1-3.2, 3.5, [Gus] 23.1-23.5 


## Lecture 6 (9/5)

H2+ molecule; Identical particles

[Notebook: One dimensional H2+ molecule](http://nbviewer.jupyter.org/github/lin-lin/2018Fall_275/blob/master/notebooks/OneDimension_H2plus.ipynb)

**Reading**: [Book] 1.6

Some of Kieron Burke et al's work on 

Hubbard dimer 

[CFS15](others/CFS15.pdf)

and one dimensional model problems for electronic structure theory.

[MB04](others/MB04.pdf), [SWW12](others/SWW12.pdf), [BSW15](others/BSW15.pdf)

## Lecture 7 (9/7)

Helium atom. Configuration interaction. Hartree-Fock.

[Notebook: One dimensional Helium atom](http://nbviewer.jupyter.org/github/lin-lin/2018Fall_275/blob/master/notebooks/OneDimension_Helium.ipynb)

**Reading**: [Book] 2.1

## Lecture 8 (9/10)

Hartree-Fock.

**Reading**: [Book] 2.1

## Lecture 9 (9/12)

Hartree-Fock equation.


**Reading**: [Book] 2.3

Numerical optimization on the Grassmann manifold:

A. Edelman, T. Arias, S.T. Smith, The geometry of algorithms with orthogonality constraints, SIAM J. Matrix Anal. 20 (1998)



## Lecture 10 (9/14)

Kohn-Sham Density functional theory. Constrained minimization.

**Reading**: [Book] 2.2


## Lecture 11 (9/17)

Kohn-Sham Density functional theory. Exchange-correlation functional.

**Reading**: [Book] 2.2


## Lecture 12 (9/19)

Kohn-Sham Density functional theory. Euler-Lagrange equation

**Reading**: [Book] 2.3


## Lecture 13 (9/21)

Self consistent field iteration.

**Reading**: [Book] 2.4


## Lecture 14 (9/24)

Density matrix method. Variational formulation

**Reading**: [Book] 2.5


## Lecture 15 (9/26)

Localization algorithms.

**Reading**: [Book] 2.9

N. Marzari, D. Vanderbilt, Maximally localized generalized Wannier functions for composite energy bands, Phys. Rev. B. 56 (1997) 12847–12865.

A. Damle, L. Lin and L. Ying, Compressed representation of Kohn-Sham orbitals via selected columns of the density matrix, J. Chem. Theory Comput. 11, 1463, 2015 

A. Damle and L. Lin, Disentanglement via entanglement: A unified method for Wannier localization, SIAM Multiscale Model. Simul., 16, 1392, 2018



## Lecture 16 (9/28)

Localization algorithms. Periodic systems

**Reading**: [Book] 1.4, 2.8

[Notebook: One dimensional localization (via selected columns of density matrix)](http://nbviewer.jupyter.org/github/lin-lin/2018Fall_275/blob/master/notebooks/OneDimension_Localization.ipynb)


## Lecture 17 (10/1)

Density matrix method. Zero temperature.

**Reading**: [Book] 2.7


## Lecture 18 (10/3)

Density matrix method. Zero temperature.
 
**Reading**: [Book] 2.6, 2.7


## Lecture 19 (10/5)

Density matrix method. Finite temperature.

**Reading**: [Book] 2.6, 2.7

L.N. Trefethen, Is Gauss quadrature better than Clenshaw-Curtis?, SIAM Rev. 50 (2008) 67–87. 

## Lecture 20 (10/8)

Density matrix method. Finite temperature.

**Reading**: [Book] 2.6, 2.7, 2.8

L. Lin, J. Lu, L. Ying and W. E, Pole-based approximation of the Fermi-Dirac function, Chin. Ann. Math. 30B 729, 2009

L. Lin, C. Yang, J. Meza, J. Lu, L. Ying and W. E, SelInv -- An algorithm for selected inversion of a sparse symmetric matrix, ACM Trans. Math. Software 37, 40, 2011 

More information on PEXSI: http://www.pexsi.org

## Lecture 21 (10/10)

Perturbation of Green's functions

**Reading**: [Book] 3.1, 3.2


## Lecture 22 (10/12)

Perturbation of Green's functions

**Reading**: [Book] 3.1, 3.2


## Lecture 23 (10/15)

Density functional perturbation theory

**Reading**: [Book] 3.3, 3.4


## Lecture 24 (10/17)

Density functional perturbation theory

**Reading**: [Book] 3.3, 3.4


## Lecture 25 (10/19)

Density functional perturbation theory

**Reading**: [Book] 3.3, 3.4

## Boom! Boom! Lecture notes online (files of large sizes)!

**These are notes I used to prepare the lectures and are prone to
errors. Please read critically!**

[Lecture Note 1 (pdf)](lectures/275_Lec1.pdf)

[Lecture Note 2 (pdf)](lectures/275_Lec2.pdf)

[Lecture Note 3 (pdf)](lectures/275_Lec3.pdf)

[Lecture Note 4 (pdf)](lectures/275_Lec4.pdf)

[Lecture Note 5 (pdf)](lectures/275_Lec5.pdf)

[Lecture Note 6 (pdf)](lectures/275_Lec6.pdf)

[Lecture Note 7 (pdf)](lectures/275_Lec7.pdf)

[Lecture Note 8 (pdf)](lectures/275_Lec8.pdf)

[Lecture Note 9 (pdf)](lectures/275_Lec9.pdf)

[Lecture Note 10 (pdf)](lectures/275_Lec10.pdf)

[Lecture Note 11 (pdf)](lectures/275_Lec11.pdf)



## Lecture 26 (10/22)

Second quantization

**Reading**: 

[Trond Saue's lecture note on second quantization. Part I (pdf)](others/Saue_secQ_partI.pdf)

## Lecture 27 (10/24)

Second quantization

**Reading**: 

S. Szalay, M. Pfeffer, V. Murg, G. Barcza, F. Verstraete, R. Schneider,
O. Legeza, Tensor product methods and entanglement optimization for ab
initio quantum chemistry, Int. J. Quantum Chem. 115 (2015) 1342–1391. 

## Lecture 28 (10/26)

Perturbation theory in second quantization

**Reading**: 

[Trond Saue's lecture note on second quantization. Part II (pdf)](others/Saue_secQ_partII.pdf)

This uses the Wick theorem and particle hole formalism.

## Lecture 29 (10/29)

Perturbation theory in second quantization


## Lecture 30 (10/31)

Perturbation theory in second quantization

**Reading**: 

[Jurgen Gauss's lecture note on coupled cluster (pdf)](others/Gauss_coupledcluster_slides.pdf)


## Lecture 31 (11/2)

Matrix product states

**Reading**: 

[Eric Jeckelmann, Density-Matrix Renormalization Group Algorithms, 2008](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.218.530&rep=rep1&type=pdf)


## Lecture 32 (11/5)

Matrix product states


**Reading**: 


## Lecture 33 (11/7)

Matrix product states

**Reading**: 

[Notebook: DMRG for Heisenberg model](http://nbviewer.jupyter.org/github/lin-lin/2018Fall_275/blob/master/notebooks/Simple_DMRG_Spin.ipynb)


## Lecture 34 (11/9)

Time-dependent perturbation theory

**Reading**: 

[Book] 3.6


## Lecture 35 (11/14)

Time-dependent perturbation theory

**Reading**: 

[Book] 3.8

## Lecture 36 (11/16)

Time-dependent perturbation theory

**Reading**: 

[Book] 3.9

## Lecture 37 (11/19)

Green's function formalism

**Reading**: 


## Lecture 38 (11/26)

Green's function formalism

**Reading**: 


## Lecture 39 (11/28)

Green's function formalism

**Reading**: 
