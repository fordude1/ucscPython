'''
sum_1_to_100_while_loop.py

The following small script calculates the sum of
the numbers from 1 to 100

'''

number_to_count_to = 100

sum_of_numbers = 0
initial_value = 1

while initial_value <= number_to_count_to:

    # Print current count and value
    print "Count:", initial_value, "Sum:", sum_of_numbers
    sum_of_numbers = sum_of_numbers + initial_value
    initial_value = initial_value + 1

print "\nSum of 1 until", number_to_count_to, "is", sum_of_numbers
