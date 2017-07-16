'''
accessing_values_in_list_string.py - show how to access particular elements
and a string
'''

list_1 = ['Chemistry', 'Biochemestry', 1999, 2007]

print 'print the list \n'
print list_1

print '\nprint the first element or index\n'
print list_1[0]

print '\nprint the last element\n'
print list_1[3]

print '\nanother way to print last element\n'
print list_1[-1]

print '\nprint range of elements\n'
print list_1[0:3]

string_1 = 'Chemistry'

print string_1

print '\nprint first element in string'
print string_1[0]

print '\nprint last element in string'
print string_1[-1]

print '\nprint range in string'
print string_1[0:01]

print '\nstepping out of bounds on string'
print string_1[9]