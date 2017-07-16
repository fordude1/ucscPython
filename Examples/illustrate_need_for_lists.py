'''
illustrate_need_for_lists.py - This program will demonstrate how
we would handle a list of values currently given the knowledge we have
up to this point.

This program will require what is referred to in the industry as
"hard coding values"  Which could cause errors and relies heavily on
knowing what needs to be changed.
'''

def CalculateAveratge(homework_1, homework_2, homework_3, homework_4, homework_5):

    ave = (homework_1 + homework_2 + homework_3 + homework_4 + homework_5) / 5

    return ave

def GetGrades ():

    homework_1 = 100
    homework_2 = 90
    homework_3 = 85
    homework_4 = 99
    homework_5 = 82

    average = CalculateAveratge(homework_1, homework_2, homework_3, homework_4, homework_5)

    print 'Your homework average is', average

GetGrades()