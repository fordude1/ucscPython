'''
Ask the user for a list of numbers and then take this list of numbers and sort them.
'''

# Initialize the list
number_list = []

# Specify the length of this list
maxLengthList = 5

# Use a while loop to insert values into this list
while len(number_list) < maxLengthList:
    numbers = raw_input("Please type in 5 numbers")
    # use the append function to insert number
    number_list.append(numbers)



print "The numbers you typed are:", number_list

# Sort this list
number_list.sort();

# Print results
print "The list sorted is:",number_list




