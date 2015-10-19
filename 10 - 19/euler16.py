# PROBLEM DESCRIPTION
# 2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2 ** 1000

# NOTES: 
# We can do this by calculating 2 ** 1000, and using that as an input string
# to a function that will loop through the string and sum the digits


def sum_number_digits(n):
	s = str(n)
	answer = 0
	for digit in s:
		answer += int(digit)
	return answer

print sum_number_digits(2 ** 1000)