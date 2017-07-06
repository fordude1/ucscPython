'''
Convert_dollars_to_euros.py

use of docstrings:  A docstring is a string
literal that occurs as the first statement in
a module, function, class, or method definition.

Program using functions that repeatedly asks user
for valid US dollars amount (float) and once valid
amount given will convert that to euros using the
current exchange rate at time of writing

7/1/2017 - $1.00 = 0.88 Euro

'''

# Define the constant for the exchange rate
EURO_CONVERSION_RATE = 1.88

def GetDollars():
    '''Asks user for dollar amount as float
    and returns a verified float
    '''
    # while loop to check for exceptions
    while True:
        us_dollars = raw_input('Enter dollar and cents value to convert.\n')
        try:
            float_us_dollars = float(us_dollars)
        except:
            ValueError
            print us_dollars, "is not a valid dollar amount.  Try again."
            continue
        # return the value of float_us_dollars
        return float_us_dollars

def ConvertDollarsEuros(us_dollars):
    """Converts the parameter us_dollars to euros
    """
    euros = us_dollars / EURO_CONVERSION_RATE

    return euros

def Run():
    """ Run function that will run GetDollars and ConvertDollarsEuros
    functions and print out the result
    """
    verified_us_dollars = GetDollars()
    print '''You will be converting''', verified_us_dollars, '''dollars to euros.\n'''
    print '''The current exchange rate is ''', EURO_CONVERSION_RATE, ''', Euros to $1.00 US Dollar.'''
    print "$", verified_us_dollars, '''converted to euros is''', ConvertDollarsEuros(verified_us_dollars)

# Execute Program Here
Run()