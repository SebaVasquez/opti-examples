# Convex hull exclusion problem

## Description

Write a program that, given positive integers $n, k$:

    * Generates a set of vectors $S = \{ x^1, \ldots, x^k \} \subseteq \mathbb{R}^n$, according to a multivariate normal distribution $\mathcal{N}(0, 1)$.

    * For any $i = 1, \ldots, k$, verify if $x^i$ belongs to $P^i := \text{conv}(S \setminus \{x^i\}). If it does not, return a plane that separates it. \texttt{Hint:} Use Farkas Lemma properly.

    * For $n = 2$, also return a graphical representation of the solution.
