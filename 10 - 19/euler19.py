# PROBLEM DESCRIPTION
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



# advance to the next first day of the month when given a day and a month, and if the year is a leap year
def first_of_next_month(day, month, leap):
	# if the month has 31 days
	if month in [1, 3, 5, 7, 8, 10, 12]:
		return day + 3
	# if the month has 30 days
	elif month in [4, 6, 9, 11]:
		return day + 2
	# if the month is february on a leap year
	elif (month == 2) and leap:
		return day + 1
	# if the month is february
	else:
		return day


# need to write a function that will count the sundays in a 100 year period
def count_sundays():
	# Jan 1, 1900 was a monday, so we initialize day with 1
	sundays = 0
	day = 1
	for i in range(101):
		# calculate if we are in a leap year
		b = True if (i % 4 == 0) else False
		for j in range(12):
			# we started on Jan 1 1900, but we only want to count sundays during and after 1901
			if day == 0 and 0 < i:
				sundays += 1
			# find the first day of next month, if it is a sunday, we keep track of it
			day = first_of_next_month(day, j+1, b)
			day = day % 7
			
	return sundays

print "our answer is: " + str(count_sundays())