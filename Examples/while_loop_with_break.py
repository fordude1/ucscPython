'''
while_loop_with_true_false_break.py:

This is a script containing a while loop
and it also uses the keywords:

1. True and False
2. break

'''

while True:
    age = raw_input('Give me your age; type "quit" to end.\n')

    if age == 'quit':
        break
    try:
        int_age = int(age)
        print 'Your age is', int_age
    except:
        ValueError
        print 'Your age must be an integer value'