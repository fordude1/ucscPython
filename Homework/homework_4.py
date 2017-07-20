# Hauns Froehlingsdorf
# Python Programming for Beginners
# Week 4 Homework

'''
 pos 0:45:00 - 0:57:36
1. Ask user how many cities they would like to visit (function - AskForNumberCities)
2. Ask user to input names of cities (limited to number from 1) (function - AskForCityName)
    NOTE: Only allow city names to be entered once
4. Print a sentence about the city (function - PrintFirstCitySentence)
    Sentence: "You would like to visit Tel Aviv as city 1 and Haifa as City 2 and Negev as city 3
                on your trip."
5. Take this sentence string and add 1 to each city number and output the string with the changes
    (function - PrintAddOneCityNumSentence)
    Sentence: "You would like to visit Tel Aviv as city 2 and Haifa as city 3 and Negev as city 4 on
                your trip."
    NOTE: split sentence into a list, use isdigit() to determine if element of list is digit, add one to these elements
            and join the new list elements together using join() (for loop enumerate)
'''

def AskForNumberCities():
    '''
    Ask user how many cities they would like to visit
    :return:number_of_cities
    '''

    # Start a while loop to test input
    while True:
        city_number = raw_input('How many cities would you like to visit?.\n')

        # Check for no input
        if len(city_number) == 0:
            print "You didn't enter anything"

        else:
            # Check for non integers
            try:
                test_city_number = int(city_number)
            except ValueError:
                print "The Value,", city_number, "is not a number, please type a number."
            else:

                # make sure the input isn't 0
                if int(city_number) == 0:
                    print "You entered 0, you need to enter a number greater than 0."
                else:
                    print "The number of cities you want to visit is:", city_number
                    break

def AskForCityName():
    pass

def PrintFirstCitySentence():
    pass

def PrintAddOneCityNumSentence():
    pass


AskForNumberCities()