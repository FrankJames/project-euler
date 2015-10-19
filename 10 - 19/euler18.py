# PROBLEM DESCRIPTION: 
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 	  3
#    7 4
#   2 4 6
#  8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 							   	  75
# 							    95 64
# 							  17 47 82
# 						    18 35 87 10
# 						  20 04 82 47 65
# 					    19 01 23 75 03 34
# 					  88 02 77 73 07 63 67
# 				    99 65 04 28 06 16 70 92
# 				  41 41 26 56 83 40 80 70 33
# 			    41 48 72 33 47 32 37 16 94 29
# 			  53 71 44 65 25 43 91 52 97 51 14
# 		    70 11 33 28 77 73 17 78 39 68 17 57
# 		  91 71 52 38 17 14 91 43 58 50 27 29 48
# 		63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 	  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, 
# it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing 
# one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


# combine two lists into a new one that contains the sums of the first list with the second list,
# but only the greater sums
def combine_layers(layer1, layer2):
	end_list = []
	# we need to iterate over the smaller list-- layer 2. 
	# Layer 2 is guaranteed to be one element shorter than Layer 1
	for x in range(len(layer2)):
		a = layer1[x] + layer2[x]
		b = layer1[x+1] + layer2[x]

		# we take the maximum of the two possible values and discard the lower value path
		end_list.append(max(a, b))
	return end_list

# triangle needs to be a 2-d array
def walk_through_triangle(triangle):
	# we need to start with the bottom layer, and continue overwriting it with every call to combine_layers
	paths = triangle[0]
	for x in range(len(triangle) - 1):
		paths = combine_layers(paths, triangle[x+1])

	# after we combine all of our layers, we should only have one element left in paths,
	# which is the sum of the longest path
	return paths[0]

t = [
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[99, 65, 4, 28, 6, 16, 70, 92],
[88, 2, 77, 73, 7, 63, 67,],
[19, 1, 23, 75, 3, 34],
[20, 4, 82, 47, 65],
[18, 35, 87, 10],
[17, 47, 82],
[95, 64],
[75]
]
 
print "our answer is " + str(walk_through_triangle(t))