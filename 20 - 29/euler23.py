# PROBLEM DESCRIPTION: 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called 
# abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
# as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers 
# greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be 
# reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
# as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


# could find all abundant numbers under 28123
# and then sum all possible pairs, remove them from list of integers [1... 28123]
# and then find the sum of remaining ints

# 28123 is our upper bound
# we can immediately remove all primes when finding all of the abundant numbers, 
# because primes are-- by definition-- deficient

import math

# create the list of numbers
def create_list(x):
	l = []
	for i in xrange(1,x):
		l.append(i)
	return l

# from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
# this will return a list of primes < n
def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def remove_elements_from_list(a, b):
	l = []
	for e in a:
		if not e in b:
			l.append(e)
	return l

def find_all_composites_under(x):
	a = create_list(x)
	b = primes(x)
	c = remove_elements_from_list(a, b)
	return c

def find_list_of_proper_divisors(x):
	divisors = []
	prop = int(math.floor(x / 2))

	# need to loop through all the numbers less than half of x to find its divisors
	while 1 < prop:
		if x % prop == 0:
			divisors.append(prop)
		prop -= 1

	# because 1 divides everything and at this point prop = 1
	divisors.append(prop) 
	return divisors

# sum all of the elements of a list
def sum_list(a):
	answer = 0
	for e in a:
		answer += e
	return answer

# returns True if a number is abundant, False otherwise
def is_abundant(x):
	divisors = find_list_of_proper_divisors(x)
	prop = sum_list(divisors)
	return True if x < prop else False

def find_all_abundant_numbers_under(x):
	a = []
	c = find_all_composites_under(x)
	for e in c:
		if is_abundant(e):
			a.append(e)
	return a

# n^2 solution to find all the possible pairs of abundant numbers
# but we know there is an upper limit x (28123 for this problem)
# so we don't need to find any pairs that are above the limit
def find_all_pairs_of_abundants_under(a, x):
	answer = []
	for i in range(len(a)):
		for j in range(len(a)):
			prop = a[i] + a[j]
			if prop < x:
				answer.append(prop)
	return answer



prop = find_all_abundant_numbers_under(28123)
all_pairs = find_all_pairs_of_abundants_under(prop, 28123)
possibilities = create_list(28123)
answer = remove_elements_from_list(possibilities, all_pairs)
print "our answer is " + str(sum_list(answer))