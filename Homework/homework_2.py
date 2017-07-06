# Hauns Froehlingsdorf
# Python Programming for Beginners
# Week 2 Homework

'''
Write a program that asks the user for a letter. The program should then determine if the letter is a vowel or not.
'''

# This function will repeatly as the user for a single letter until
# the user types "quit" to exit the program or they have entered a vowel.
def AskForLetter():
    '''
    This function will use the built-in python function called len.
    If the len of the user input is 1, then this function should call the second function below.
    :return:
    '''


def IsVowel(letter):
    '''
    This function will take as input a variable called letter and
    will determine if this letter is a vowel or not.
    If it is a vowel it will return True and is not it will return To determine
    if letter is vowel or not, this function will call a third and a fourth function below.
    :param letter:
    :return:
    '''


def IsLowercaseVowel(letter):
    '''
    this function will take a single variable as input called letter and will
    return True if the letter is a lowercase vowel and will return False if not.
    :param letter:
    :return:
    '''


def IsUppercaseVowel(letter):
    '''
    this function will take a single variable as input called letter
    and will return True if the letter is a uppercase vowel and will return False if not.
    :param letter:
    :return:
    '''

def PrintIsVowel():
    '''
    this function will print a sentence to the user (standard out) indicating if the input is a vowel or not.
    It will be called inside AskForLetter(letter).
    This function will take as input the original letter input by the user
    so that it can be included in the output sentence.
    :return:
    '''