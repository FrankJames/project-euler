# PROBLEM DESCRIPTION
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?


# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.



# NOTE: I enumerated the possibilities for numbers 1 - 19 because those numbers do not follow a set pattern
# 		they serve as a base case for the rest of the function. Although 14, 16, 17, and 19 DO follow a pattern
# 		(ex: 14 is number_of_letters(4) + 4 letters in 'teen'), 15 bucks the trend. So for a consistency, I enumerated
#		all numbers 1 - 19

# determine how many letters for the digit in the tens place.
def letters_in_tens(x):
	a = x % 10
	b = x - a
	if b in [20, 30, 80, 90]:
		return 6
	elif b in [40, 50, 60]:
		return 5
	else:
		return 7 


def number_of_letters(n):
	letters = 0

	# check if n is 1000. If it is, we can stop here.
	# For this problem, we only care about 1000 as our top number
	if n == 1000:
		return 11

	# the following block will give the correct number of letters for numbers 1 - 19
	if n in [1, 2, 6, 10]:
		letters = 3
	elif n in [4, 5, 9]:
		letters = 4
	elif n in [3, 7, 8]:
		letters = 5
	elif n in [11, 12]:
		letters = 6
	elif n in [15, 16]:
		letters = 7
	elif n in [13, 14, 18, 19]:
		letters = 8
	elif n in [17]:
		letters = 9

	# now we need to start decomposing our input for n < 100
	if 20 <= n < 100:
		letters = letters_in_tens(n) + number_of_letters(n % 10)

	# lastly we need to decompose the input for 100 <= n < 1000
	# do we need to count the letters in "and" or not?
	if (100 <= n < 1000) and ((n % 100) == 0):
		a = n % 100
		b = n - a
		letters = number_of_letters(b / 100) + len("hundred")


	elif (100 <= n < 1000) and ((n % 100) != 0):
		a = n % 100
		b = n - a
		letters = number_of_letters(b / 100) + number_of_letters(a) + len("hundred") + len("and")

	# we have our answer
	return letters

# this function will apply number_of_letters to every number between 1 and top
# and return the sum
def sum_number_of_letters(top):
	answer = 0
	for x in range(top):
		answer += number_of_letters(x+1)
	return answer

# finally we can print out our answer
print "our answer is: " + str(sum_number_of_letters(1000))