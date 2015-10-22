# PROBLEM DESCRIPTION
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# we need to alphabetize our input so that we can get the proper position value for each name
def alphabetize_list(file_name):
	names = []
	with open(file_name, "r") as txt:
		for line in txt:
	 		names = line.split('"')
	 	txt.close()
	# we have some oddly formatted output from the split function, so we need to put it in the correct format
	names[:] = (name for name in names if name != ",")
	names[:] = (name for name in names if name != "")
	names.sort()
	return names

# find the name value, given the name and its position in the list
def name_value(name, position):
	coefficient = 0
	for letter in name:
		coefficient += alphabet.index(letter) + 1
	return coefficient * position


# sum the name values, given a list of alphabetized names
def sum_name_values(list):
	answer = 0
	for x in range(len(list)):
		answer += name_value(list[x], x+1)
	return answer

# combines previous functions to get the answer
def alphabetize_and_sum(file_name):
	a = alphabetize_list(file_name)
	v = sum_name_values(a)
	return v

print "our answer is " + str(alphabetize_and_sum("p022_names.txt"))