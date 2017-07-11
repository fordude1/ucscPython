'''
Write a program that will ask the user for a sentence.
Have functions in the program that will do the following:

a.Create an uppercase version of the sentence and return it

b.Create a lowercase version of the sentence and return it

c.split the sentence up and place comma between each element and return it

d.Take the sentence and turn it into a question
by adding a question mark to the end and then return it
'''

converted = []

def UpperCase():
    '''
    convert sentence to uppercase
    '''
    upper=sentence.upper()
    print upper

def LowerCase():
    '''
    convert sentence to lowercase
    '''
    lower=sentence.lower()
    print lower

def SplitComma():
    """
    split sentence up and place comma between each element
    """
    splits=sentence.split()
    print splits

sentence = raw_input("Please type a sentence for me.")


print "Your sentence is: ",sentence

print "Upper Case: "
UpperCase()
print

print "Lower Case: "
LowerCase()
print

print "Split with commas: "
SplitComma()

