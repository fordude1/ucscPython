'''
This is a compilation of my most commonly used Functions.

It is by no means an exhaustive list.
'''

misc_int = 10

def catch_intvalex(misc_int):
    # test for Value Error exception
    try:
        test_int = int(misc_int)
    except ValueError:
        print misc_int, "is not an integer."
        print "Program is exiting!"
    else:
        print misc_int, "is an acceptable integer."
        return misc_int

catch_intvalex(misc_int)