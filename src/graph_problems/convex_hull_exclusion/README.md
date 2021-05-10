# Convex hull exclusion problem

## Description

Write a program that, given positive integers $n, k$:

    * Generates a set of vectors ![eq1](https://latex.codecogs.com/gif.download?S%20%3D%20%5C%7B%20x%5E1%2C%20%5Cldots%2C%20x%5Ek%20%5C%7D%20%5Csubseteq%20%5Cmathbb%7BR%7D%5En), according to a multivariate normal distribution ![eq2](https://latex.codecogs.com/gif.download?%5Cmathcal%7BN%7D%280%2C%201%29).

    * For any ![eq3](https://latex.codecogs.com/gif.download?i%20%3D%201%2C%20%5Cldots%2C%20k), verify if ![eq4](https://latex.codecogs.com/gif.download?x%5Ei) belongs to ![eq5](https://latex.codecogs.com/gif.download?P%5Ei%20%3A%3D%20%5Ctext%7Bconv%7D%28S%20%5Csetminus%20%5C%7Bx%5Ei%5C%7D%29). If it does not, return a plane that separates it. \texttt{Hint:} Use Farkas Lemma properly.

    * For ![eq6](https://latex.codecogs.com/gif.latex?n=2), also return a graphical representation of the solution.
