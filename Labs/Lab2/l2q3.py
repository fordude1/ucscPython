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