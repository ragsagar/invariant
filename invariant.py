#! /usr/bin/python

import sys

count_dict = {}

def difference_of_numbers(number):
	""" Finds the difference between the given number in asceding form and
	descending form and returns the difference as int """
	number = str(number).zfill(4)
	list_of_digits = list(number)
	list_of_digits.sort(reverse=True)
	descending_number = int(''.join(list_of_digits))
	list_of_digits.sort(reverse=False)
	ascending_number = int(''.join(list_of_digits))
	return descending_number - ascending_number


def is_valid(number):
	""" Checks if the given number is valid and returns a Boolean expression """
	number = str(number)
	status = False
	
	# No need of checking if the number of digits is equal to 4 in this context
	#if len(number) != 4:
		#return status
		
	# Checking if there is atleast 2 different digits	
	if any(number[0] != digit for digit in number[1:]):
		status = True
	return status
	
	
def get_count(number):
	""" Returns the number of iterations needed to reach down to 6174 as int """
	count = 0
	if is_valid(number):
		while number != 6174:
			number = difference_of_numbers(number)
			count += 1	
		return count
		
def display_as_table(out=sys.stdout):
	""" Function to print the output as a pretty table.
		Any file like object can be given as argument """
	header = ["Iterations", "Total Count of Numbers"]
	data = [ [str(key), str(len(value))] for key,value in count_dict.items()]
	data.insert(0, header)
	column_padding = []
	for i in (0,1):
		# max_width = max( [ len(row[i]) for row in data ] )
		# Here we know that the header will be having the maximum  width
		max_width = len(header[i])
		column_padding.append(max_width)
	for row in data:
		print >> out, row[0].center(column_padding[0] + 1),
		print >> out, row[1].center(column_padding[1] + 1)	


def main():
	""" The main function """
	for i in xrange(1000,9999):
		count = get_count(i)
		if count:
			if count in count_dict:
				count_dict[count].append(i)
			else:
				count_dict[count] = [i]	
	display_as_table()
	
if __name__ == '__main__':
	sys.exit(main())
