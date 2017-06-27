# Hauns Froehlingsdorf
# Python Programming for Beginners
# Week 1, Homework 1
#
# Write a program that asks the user for their dream job title.  Then ask them for the
# hourly wage they want to earn.  This number should account for dollars and cents.
# Calculate the annual wage they will earn over a year.  Assume they work 48 weeks a
# year (4 weeks vacation) but are paid over 52 weeks.  Then ask them how much
# money they feel they will need at retirement time.  Determine the number of years
# they will have to work to save up their retirement dollar value assuming their only
# source of income was their paycheck?  Finally, determine if the number of years
# they need to save is an even or odd numbers.  For this part, use the modulus operator
# to determine if the number you calculated is and even or odd.  Once you have calculated
# it, use print to print out the value.  You should also print out something like this.  "If
# the value is --- then the number is odd, however, if the value is ---- then the number
# is even."
# Make sure you account for user input error.  Test your code by trying to cause errors
# in input.  It is not important to error check on their dream job title.  Just assume it
# will be a reasonable string.

# Ask user for their dream job title
dream_job_title = raw_input("Please tell me your dream job title: ")

# Ask them the hourly wage they want to earn
print '''For the next question, assume you work 48 weeks a year, with 4 weeks of vacation.
You will be paid over a period of 52 weeks.'''
hourly_wage_request = raw_input("Please enter the hourly wage you want to earn (ie. 10.50): ")

# Test for exception
try:
    test_hourly_wage_request = float(hourly_wage_request)
except ValueError:
    print "The Value,", hourly_wage_request, "is not an integer or floating number."
    print "Program is exiting!"
else:

    # Ask them how much they feel they will need at retirement
    retirement_amount = raw_input("How much money will you need at retirement time?: ")

    # Test for exception
    try:
        test_retirement_amount = float(retirement_amount)
    except ValueError:
        print "The Value,", retirement_amount, "is not an integer or floating number."
        print "Program is exiting!"
    else:

        # Annual income
        annual_income = float(hourly_wage_request) * 40 * 52

        # Years until retirement
        years_to_retirement = float(retirement_amount) / annual_income

        # Print results from above
        print "Your dream job is: ", dream_job_title
        print "You want to make: $", float(hourly_wage_request), "an hour."
        print "You want to have: $", float(retirement_amount), "at retirement time."
        print "With this income, you will make $", float(annual_income), "per year."
        print "With this annual income, you will need to work", int(years_to_retirement), "years to attain this."

        # Determine if the years required are odd or even using modulo
        odd_or_even_years = years_to_retirement % 2
        if int(odd_or_even_years) == 0:
            years_result = "even"
        else:
            years_result = "odd"

        print "The number of years to save this is an", years_result, "number of years."

