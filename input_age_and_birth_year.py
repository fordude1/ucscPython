# Testing user input
# and catching exceptions
# NOTE: indenting is very important in python
# Ask the user to input their agea nd birth year,
# Read this from stdin, and output their input values

# Inquire age from user
age_input = raw_input("What is your age? ")
# catch exceptions
try:
    age = int(age_input)
except ValueError:
    print "The number input", age_input, "is not a valid integer"
else:
        print "The number input", age_input, "is a valid integer."

# Inquire year born from user
        year_born_input = raw_input("What year were you born? ")
        try:
            year = int(year_born_input)
        except:
            print "The number input ",year_born_input, "is not a valid integer."
            print "Program will now exit."
        else:
            print "The number input",year_born_input, "is a valid integer."
            print "You are", age, "and you were born in", year, "."