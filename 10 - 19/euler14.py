# PROBLEM DESCRIPTION
# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


# NOTES:
# Go through the chain backwards, and find the longest distance under one million
# numbers will always end at 1, so we can just walk backwards
# collatz number, will keep track of the length of the chain and the number itself


# After thoughts:
# This is a brute force algorithm that will solve the problem, but it will do it in polynomial time
# This algorithm lacks any semblence of finesse. Like at all. 

# this is simply pair of numbers
class collatzNumber:
	def __init__(self, num, length):
		self.n = num
		self.l = length

def longestCollatzChainBetween(minimum, maximum):
	computed=[]
	longest=collatzNumber(0, 1)
	for x in range(minimum, maximum):
		i = x
		j = 0
		while i > 1:
			if not i in computed:
				computed.append(i)
			if i%2 == 0:
				i = i / 2
			else:
				i = 3 * i + 1
			j += 1

		# lastly we need to check if we have a new longest sequence
		if longest.l <= j:
			longest = collatzNumber(x, j)
			print "NEW LONGEST: Our longest term is " + str(longest.n) + " with " + str(longest.l) + " terms."
	print "Our longest term is " + str(longest.n) + " with " + str(longest.l) + " terms."
	return longest.n

# longestCollatzChainBetween(1, 100000)
# longestCollatzChainBetween(100001, 200000)
# longestCollatzChainBetween(200001, 300000)
# longestCollatzChainBetween(300001, 400000)
# longestCollatzChainBetween(400001, 500000)
# longestCollatzChainBetween(500001, 600000)
# longestCollatzChainBetween(600000, 650000)
# longestCollatzChainBetween(650001, 700000)
# longestCollatzChainBetween(700001, 750000)
# longestCollatzChainBetween(750001, 800000)
# longestCollatzChainBetween(800001, 850000)
# longestCollatzChainBetween(850001, 900000)
# longestCollatzChainBetween(900001, 950000)
# longestCollatzChainBetween(950001, 10000000)