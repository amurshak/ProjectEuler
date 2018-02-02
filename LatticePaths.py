#Lattice Paths
#Project Euler Problem 15
#
#Starting in the top left corner of a 2×2 grid, and only being able to
#move to the right and down, there are exactly 6 routes to the bottom
#right corner.
#
#How many such routes are there through a 20x20 grid?
#
#Solution by Alex Murshak

import math

def lattice_paths(n):
    n_fact = math.factorial(n)

    return math.factorial(2*n)/n_fact/n_fact

print(lattice_paths(20))
