'''
Write a program that will take anything the user inputs into a list.
Have the program stop taking input when the user types quit.
Write a function in the program that will determine the length of
the list(hint use built in function len.)
Write another function that will select a random number between 1 and the length of the list.
Write another function that will use the built in function for list that will remove the
randomly chosen element from the list and print out the list.
'''

import random

def list_length():
    '''
    Determine the length of the list
    '''
    input_length = len(user_input)
    #print "length of your list is:", input_length
    return random_number(input_length)

def random_number(length):
    '''
    selects a random number between 1 and list length
    '''
    ran_number = random.randrange(1,length)
    print "The random number from your list is:", ran_number
    return random_remove(ran_number)

def random_remove(word):
    '''
    remove random number from list and print out list
    '''
    print "Your list is:",user_input
    print "A random variable from your list is:", user_input[word]
    print "Your list without this variable is:", user_input[0:word]+user_input[word+1:]

user_input = []
# Get input from user
while user_input != "quit":
    user_input = raw_input("Please type something for our list.  type quit to exit program.")
    if user_input == "quit":
        break

    #print "Your list is:", user_input
    list_length()