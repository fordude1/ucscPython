# Homework 3:
# Write a program that takes a 3 word phrase and then converts the wors to Pig Latin.
#
# To review, Pig Latin takes the first letter of a word, puts it at the end, and appends
# "ay". The only exception is if the first letter is a vowel, in which case we keep
# it as it is and append "hay" to the end.
#
# E.g. "boot" --> "ootbay", and "image" --> "imagehay".
#
# There are many more Pig Latin rules, but for this homework this is sufficient.
#
# Define a GLOBAL list at the top of your code file called VOWELS. This way, you can
# check if a letter x is a vowel with the expression x in VOWELS. Remember to get a
# word except for the first letter, you can use word[1:].
#
# It's tricky for us to deal with punctuation and numbers with what we know so far, so
# instead, ask the user to enter only 3 words and spaces. You need to convert their input
# from a string to a list. Also convert the 3 word phrase to all lower when doing
# comparisons against the vowels list.
#
# Use a list of words, you can go through each word and convert it to Pig Latin by
# calling the function ConvertWordToPigLatin. Make sure you have a check in your code
# that it only converts lists that are of length 3 to Pig Latin.
#
# Break all the tasks into functions. Should have functions that: reads user input
# with name AskUserForSentence, lowercases the sentence called LowercaseSentence,
# splits the phrase called SplitSentenceIntoList, convert the word to pig latin called
# ConvertWordToPigLatin and prints out the 3 word phrase in pig latin called
# PrintThreeWordPhrase. Remember, using functions makes your code much more re-useable,
# readable and clean.
#
# Once you have your program working, make it interactive such that it keeps translating
# 3 word phrases into pig latin until the user enters in the phrase QUIT.


VOWELS = ('a, e, i, o, u, A, E, I, O, U')


def AskUserForSentence():
    ask = True

    while ask == True:

        sentence = raw_input('''Please enter 3 word phrase:
Type 'quit' to end.\n''')
        if sentence == 'quit':
            ask = False

            if sentence == True:
                PrintThreeWordPhrase(sentence)


def LowercaseSentence(sentence):
    lowercasesentence = sentence.lower()


def SplitSsentenceIntoList(sentence):
    split_sentence = sentence.split()


def ConvertWordToPigLatin(word):
    for word in split_sentence:
        if letter in VOWELS == word[0]:
            print word + "hay"
        else:
            print word[1:] + word[0] + "ay"


def PrintThreeWordPhrase(sentence):
    print "The 3 word phrase in Pig Latin is " + ConvertWordToPigLatin(word)


AskUserForSentence()
