'''
Write a Python program that asks the user to enter an integer that is greater
than 0. The
program
will keep on asking the user for the number until it is
valid.
'''

#while True:
#    age = raw_input('Give me your age; type "quit" to end.\n')

#    if age == 'quit':
#        break
#    try:

#        int_age = int(age)
#        print 'Your age is', int_age
#    except:
#        ValueError
#        print 'Your age must be an integer value'

while True:
    # Request user input
    positive_integer_request = raw_input('Please provide a number that is greater than 0:\n')

    try:
            int_number = int(positive_integer_request)
            print 'The number you provided was:', int_number
            if int_number > 0:
                print 'This is greater than 0'
                break
    except:
            ValueError
            print 'Your input must be an integer.  You entered' , positive_integer_request



