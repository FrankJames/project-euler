# PROBLEM DESCRIPTION
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# NOTES:

# 1/11  =   0.(09)
# 1/12  =   0.08(3)
# 1/13  =   0.(076923)
# 1/14  =   0.0(714285)
# 1/15  =   0.0(6)
# 1/16  =   0.0625
# 1/17  =   0.(0588235294117647)
# 1/18  =   0.0(5)
# 1/19  =   0.(052631578947368421)
# 1/20  =   0.05

# the number of digits in the repetend of (1/p)
# is equal to the smallest integer m which satisfies
# 10^m = 1 mod p, for some prime p.

# additionally, the number of digits in the repetend will be less than or equal to (p-1)


# Steps: 
# 	get all primes 1 - 1000
# 	be able to find the repetend of one prime
# 	put that in a loop for all primes
# 	return the longest repetend

# from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
# this will return a list of primes < n
def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

# the number of digits in the repetend of (1/p)
# is equal to the smallest integer m which satisfies
# 10^m = 1 mod p, for some prime p.
def repetend_length(p):
	# we are uninterested in 2 and 5 specificially because they are 
	# the only primes which divide 10 evenly
	if p == 2 or p == 5:
		return 0

	m = 1
	while( (10 ** m) % p != 1 ): # while we still haven't found the repetend yet
		m += 1
	return m

# if longest_repentend_length returns -1, an error has occurred
def prime_with_longest_repetend(n):
	primes_list = primes(n)
	longest = -1
	prime = -1
	for p in primes_list:
		prop = repetend_length(p)

		# if we found a new longest prime
		if longest < prop:
			longest = prop
			prime = p

	return prime

print "our answer is: " + str(prime_with_longest_repetend(1000))