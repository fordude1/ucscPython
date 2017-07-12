# Hauns Froehlingsdorf
# Python Programming for Beginners
# Week 3 Homework

'''
Write a program that takes a 3 word phrase and then converts the words to Pig Latin.
start if list is 3 words - if not, have them re-enter
'''

# define the constant named VOWELS
VOWELS = ["a","e","i","o","u"]

# if letter in vowels

def AskUserForSentence ():
    '''
    obtain 3 word phrase from user
    :return:
    '''
    # initialize our list
    user_input = []
    # a while loop seams logical to get user input and watch for quit to exit
    while True:
        user_input = raw_input("Please type a 3 word phrase to conver to pig latin.  type 'QUIT' to exit program.")
        if user_input == "QUIT":
            break
        # convert input to string
        phrase = user_input.split(" ")
        if len(phrase) == 3:
            LowercaseSentence(phrase)

def LowercaseSentence (phrase):
    '''
    convert the sentence to lower case
    :return:
    '''
    print "Your phrase is:",phrase

def SplitSentenceIntoList ():
    '''
    split the sentence into a list
    :return:
    '''

def ConvertWordToPigLatin ():
    '''
    convert each word to pig latin
    :return:
    '''

def PrintThreeWordPhrase ():
    '''
    print the phrase in pig latin
    :return:
    '''

# Run the program
AskUserForSentence()