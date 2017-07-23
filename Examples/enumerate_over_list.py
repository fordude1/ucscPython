'''
enumerate_over_list.py - shows how you can enumerate over a list
'''

def EnumerateList(list_1):

    for i, item in enumerate(list_1):
        print 'index is', i
        print 'item in list is', item

EnumerateList( ['Aaron Rodgers single season passer rating', 122.5, \
              2011, [' Rodgers', 'Manning', 'Foles', 'Brady'] ])

