'''
Write a Python program that asks the user to enter an integer that is greater
than 0. The
program
will keep on asking the user for the number until it is
valid.
'''

while True:
    # Request user input
    num_request = raw_input('Please provide a number that is greater than 0:')

    if int(num_request) > 0:
        print 'The number you entered was', num_request
        break
    try:
            num_request = int(num_request)
            print num_request, 'is not greater than 0.'
    except:
            ValueError
            print 'Your input must be an integer.'


