# PROBLEM DESCRIPTION
# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


# NOTE: the problem with brute forcing this answer is that python will not be able to calculate the whole number
# 		and instead 

# easy_for_sum_factorial will give the factorial of x without any 0's,
# it will remove all ending 0's from the factorial.
def easy_for_sum_factorial(x):
	answer = 1
	while 0 < x:
		if x % 10 == 0:
			a = x / 10
			answer = answer * a
		else:
			answer = answer * x
		x -= 1
	return answer

# now that we've stripped off all of the easy-to-find trailing zeroes, we can 
# add up each individual digit easier.

def sum_digits_of_large_factorial(x):
	s = str(easy_for_sum_factorial(x))
	answer = 0
	for digit in s:
		answer += int(digit)
	return answer

print "our answer is: " + str(sum_digits_of_large_factorial(100))