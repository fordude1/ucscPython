# Hauns Froehlingsdorf
# Python Programming for Beginners
# Lab 2, question 4
#
# Write a program that asks the user for two integers.
# Then apply all the operators we have learned or head about thus far:
# addition, subtraction, multiplication, division, aand modulo.  Make
# sure to error check when performing modulo.  You need to consider a
# situation where the second number (n in notes) is zero.

# Ask for first Integer
int1 = raw_input("Please enter an integer: ")

# Test for exception
try:
    try_int1 = int(int1)
except ValueError:
    print "The Value entered was not an integer."
    print "Program is exiting!"
else:
    # Ask for second Integer
    int2 = raw_input("Please enter another integer: ")
    # Test for exception
    try:
        try_int2 = int(int2)
    except ValueError:
        print "The Value entered was not an integer."
        print "Program is exiting!"
    else:
        print "Integer 1 = ", try_int1
        print "Integer 2 = ", try_int2
        print try_int1, "+", try_int2, "=", try_int1 + try_int2
        print try_int1, "-", try_int2, "=", try_int1 - try_int2
        print try_int1, "*", try_int2, "=", try_int1 * try_int2
        if try_int2 != 0:
            print try_int1, "/", try_int2, "=", try_int1 / try_int2
            print try_int1, "%", try_int2, "=", try_int1 % try_int2
