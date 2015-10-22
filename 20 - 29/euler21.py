# PROBLEM DESCRIPTION
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


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
	for e in b:
		if e in a:
			a.remove(e)
	return a

def find_all_composites_under(x):
	a = create_list(x)
	b = primes(x)
	c = remove_elements_from_list(a, b)
	return c

# so we need to find all the proper divisors of a number and then sum them to find a potential amicable pair
def find_list_of_divisors(x):
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

# after we find all the proper divisors, we sum them
def sum_list(a):
	answer = 0
	for e in a:
		answer += e
	return answer

# so now that we have a potential amicable number, we need to find its potential amicable number:
#	case 1: we have a pair of amicable numbers, as it satisfies the requirements.
#			-> add both to amicable_numbers, and remove them from our list
#	case 2: the potential amicable number is not in our list
#			-> remove it from our list, and get the next one

def find_amicable_numbers(x):
	amicable_numbers = []
	a = find_all_composites_under(x)
	while a:
		# prop_x is the result of d(n), which is the sum of the divisors of n
		n = a[0]
		prop_x = sum_list(find_list_of_divisors(n))
		if prop_x in a:
			m = prop_x
			prop_y = sum_list(find_list_of_divisors(m))

			# if we have found an amicable pair d(n) == m and d(m) == n, where n != m
			# don't need to check if prop_x == m here, because we already checked if prop_x was in list a
			if prop_y == n and n != m:
				amicable_numbers.append(n)
				amicable_numbers.append(m)
				a.remove(n)
				a.remove(m)

			# if we did not find an amicable pair
			else:
				a.remove(n)

		# if prop_x is not in list a, we don't have a possible amicable pair for n
		else:
			a.remove(n)
	return amicable_numbers


print "our answer is: " + str(sum_list(find_amicable_numbers(10000)))