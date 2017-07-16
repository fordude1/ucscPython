'''
usage_of_lists_compute_average.py - This program will demonstrate how
to use lists to calculate the average of homework grades.

Also introduces the built-in sum() function.
'''

def CalculateAverage(grade_list):

    sum_grades = sum(grade_list)
    ave = (sum_grades) / len(grade_list)

    return ave

def GetGrades(grade_list):

    average = CalculateAverage(grade_list)

    print "Your homework average is", average

GetGrades([100, 90, 85, 99, 82])

