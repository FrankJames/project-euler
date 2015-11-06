# PROBLEM DESCRIPTION
# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# NOTES:
# The lexicographic permutations of 0, 1, 2, 3 are:

# 0123  0132  0213  0231  0312  0321  
# 1023  1032  1203  1230  1302  1320  
# 2013  2031  2103  2130  2301  2310
# 3012  3021  3102  3120  3201  3210

# number of permutations is len(numbers)! <-- factorial, not emphasis
# 10! == 3628800
# for one row of permutations, it has (len(numbers) - 1)! members
#  9! == 362880
# so the millionth permutation will be near the end of the 2 row

# remove 2 from the list, know how far to million
# and then do the function again


# write function that will take in a list of consecutive numbers and and int
# this function will take the factorial of the len(list)
# and then use this to find the iteration that is the largest and <= the int
# return that number

import math

# this will find which row in the permutation list that x is in
def find_permutation_row(list_numbers, x):
	# find out the length of each permutation row
	row_length = math.factorial(len(list_numbers) - 1)
	# start off at row 1
	row = row_length
	which_row = 0
	# while we still have not found the correct row yet
	while(row < x):
		# proceed to the next row
		row += row_length
		which_row += 1
	return which_row

# this will build the correct permutation by calling find_permutation_row multiple times
def find_permutation(list_numbers, x):
	permutation = ""
	goal = x
	# while we still have numbers in the list to iterate through
	while(1 < len(list_numbers)):
		# the permutation row is different from the number we need to add to the string
		r = find_permutation_row(list_numbers, goal)
		permutation_number = list_numbers[r]
		# move the goal post over so we can feed find_permutation_row the correct maximum
		# need to move the goal by the offset
		row_offset = math.factorial(len(list_numbers) - 1)
		goal -= r * row_offset
		# next remove the found permutation so we don't find it again
		list_numbers.remove(permutation_number)
		permutation+=str(permutation_number)

	# only one item left in the list
	permutation+=str(list_numbers[0])
	return permutation


print("our answer is: " + find_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))