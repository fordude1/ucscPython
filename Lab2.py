# Lab 2 from Week 1

# Question 1 Find the modulo for the following
print "Lab 2, Question 1:"
print "0 modulo 5 = ",(0%5)
print "1 modulo 5 = ",(1%5)
print "2 modulo 5 = ",(2%5)
print "3 modulo 5 = ",(3%5)
print "4 modulo 5 = ",(4%5)
print "5 modulo 5 = ",(5%5)
print "6 modulo 5 = ",(6%5)
print "7 modulo 5 = ",(7%5)
print "8 modulo 5 = ",(8%5)
print
# Question 2 Write a program that asks the user for an integer
# Determine if the integer is odd or even

print "Lab 2, Question 2:"
misc_int = raw_input("Please enter an integer: ")

# test for exception
try:
    answer = int(misc_int)
except ValueError:
    print "The Value entered was not an integer."
    print "Program is exiting!"
else:
    test = answer%2
    if test == 0:
        print "Number is even."
    else:
        print "Number is odd."
print
# Question 3 Write a small program that asks the user for their height.  First ask the user
# for the height portion in feet, and then ask for the inches portion.  Convert
# this height to meters.  There are 39.3701 inces in 1 meter.

print "Lab 2, Question 3:"
# Conversion from inches to meters
inches_to_meters = float(39.3701)

# Get users height in feet
height_feet = raw_input(''' I am going to ask for your height in feet
 and then inches.  First, please enter your height in feet: ''')

#test for exception
try:
    test_feet = int(height_feet)
except ValueError:
    print "The Value for feet was not an integer"
    print "Program is now exiting!"
else:
    height_inches = raw_input("Please enter the remainder of your height in inches: ")
    try:
        test_inches = int(height_inches)
    except ValueError:
        print "The Value for inches was not an integer"
        print "Program is now exiting!"
    else:
        height_inches = int(test_feet*12)+int(test_inches)
        height_meters = float(height_inches)/inches_to_meters
        print "Your height in inches is: ", height_inches
        print "Your height in meters is: ", height_meters
print

# Lab 2 question 4 - Write a program that asks the user for two integers.
# Then apply all the operators we have learned or head about thus far:
# addition, subtraction, multiplication, division, aand modulo.  Make
# sure to error check when performing modulo.  You need to consider a
# situation where the second number (n in notes) is zero.

