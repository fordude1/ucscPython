# Hauns Froehlingsdorf
# Python Programming for Beginners
# Week 2 Homework

'''
Write a program that asks the user for a letter.
The program should then determine if the letter is a vowel or not.
Make sure you account for user input error. Test your code by trying to cause errors in input.
'''

def AskForLetter():
    '''
    This function will use the built-in python function called len.
    If the len of the user input is 1, then this function should call the second function below.
    '''
    # This function will repeatly ask the user for a single letter until
    # the user types "quit" to exit the program or they have entered a vowel.

    while True:
        letter = raw_input('Please input a single letter.\n')
        if letter == 'quit':
            break
        if len(letter) == 0 or len(letter) > 1:
            print "you didn't enter anything or more than 1 letter"

        else:
            print "you entered a number."
            # return the value of the letter
            return IsVowel(letter)

def IsVowel(letter):
    '''
    This function will take as input a variable called letter and
    will determine if this letter is a vowel or not.
    If it is a vowel it will return True and is not it will return To determine
    if letter is vowel or not, this function will call a third and a fourth function below.
    '''

    if letter == "a" or "A" or "e" or "E" or "i" or "I" or "o" or "O" or "u" or "U":
        return IsLowercaseVowel(letter)
    else:
        print "letter is consonant"

def IsLowercaseVowel(letter):
    '''
    this function will take a single variable as input called letter and will
    return True if the letter is a lowercase vowel and will return False if not.
    '''

    if letter.islower():
        return PrintIsVowel(letter)


def IsUppercaseVowel(letter):
    '''
    this function will take a single variable as input called letter
    and will return True if the letter is a uppercase vowel and will return False if not.
    '''

    if letter.isupper():
        print letter, "is lower case vowel"
        return False

def PrintIsVowel(letter):
    '''
    this function will print a sentence to the user (standard out) indicating if the input is a vowel or not.
    It will be called inside AskForLetter(letter).
    This function will take as input the original letter input by the user
    so that it can be included in the output sentence.
    '''

    print "The letter you typed", "'",letter,"'" "is a vowell."


# Start the program
AskForLetter()