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
