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
    :return:phrase
    '''

    # initialize our list
    user_input = []

    # a while loop seams logical to get user input and watch for QUIT to exit
    while True:
        user_input = raw_input("Please type a 3 word phrase to convert to pig latin.  type 'QUIT' to exit program.")
        if user_input == "QUIT":
            break

        # convert input to string seperated by space
        phrase = user_input.split(" ")

        # check if phrase has 3 words
        if len(phrase) == 3:

            # send the proper input to LowercaseSentence for case change
            LowercaseSentence(phrase)

def LowercaseSentence (phrase):
    '''
    convert the sentence to lower case
    :return:lowercase_phrase
    '''

    # initialize new list lowercase_phrase
    lowercase_phrase = []

    # use a for loop to convert each word to lowercase
    for word in phrase:
        case_word = word.lower()

        # add the lower case word to the list
        lowercase_phrase.append(case_word)

    # Send this off to be split into a list
    SplitSentenceIntoList(lowercase_phrase)


def SplitSentenceIntoList (lowercase_phrase):
    '''
    split the sentence into a list
    :return:split_list
    '''
    split_list = lowercase_phrase

    # Send the split list to be conversion function
    ConvertWordToPigLatin(split_list)

def ConvertWordToPigLatin (split_list):
    '''
    convert each word to pig latin
    :return:pig_latin
    '''

    # initialize pig_latin list
    pig_latin = []

    # for loop to work on each word
    for word in split_list:

        # check to see if first letter is vowel
        if word[0] in VOWELS:
            pig_latin.append(word+"hay") # print word,"in pig latin is:",word+"hay"

        # word does not start with vowel, apply non vowel change
        else:
            pig_latin.append(word[1:]+word[0]+"ay") # print word,"in pig latin is:",word[1:]+word[0]+"ay"

    # send converted phrase to be printed
    PrintThreeWordPhrase(pig_latin)

def PrintThreeWordPhrase (pig_latin):
    '''
    print the phrase in pig latin
    '''

    # convert list to string for nice display
    print "Your phrase in pig latin is:", ' '.join(pig_latin)

# Run the program
AskUserForSentence()