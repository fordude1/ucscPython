# Testing function 1 for homework2

while True:
    letter_request = raw_input('Please type a single letter; type "quit" to end.\n')

    if letter_request == 'quit':
        break
    try:
        letter_test = str(letter_request)
        print 'You typed', letter_test
    except:
        ValueError
        print 'You must type a letter'
