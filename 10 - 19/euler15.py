# PROBLEM DESCRIPTION
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?
# the number of lattice paths from (0,0) to (n,k) is given by the binomial coefficient (n+k, n)

# combinations are resolved as (x,y):
# 								(x! / y!(x-y)!)

# substituting for our problem:
# 								(n+k)! / n!(n+k - n)
#				   since n = k:
#								(2n)! / n!(n!)

from math import factorial

def square_grid_lattice_paths(grid_size):
	numerator = factorial(2*grid_size)
	denominator = factorial(grid_size) ** 2
	return numerator / denominator

print "our answer is: " + str(square_grid_lattice_paths(20))