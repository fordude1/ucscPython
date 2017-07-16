'''
Using the built-in range function generate the following output:

a. 5 10 15 20
b. 5 105 205
c. -1 -21 -41 -61 -81
'''

print 'Range [5, 10, 15, 20]'
for i in range(5, 25, 5):
    print i
print"\n"

print 'Range [5, 105, 205]'
for i in range(5, 305, 100):
    print i
print"\n"

print 'Range [-1, -21, -41, -61, -81]'
for i in range(-1, -101, -20):
    print i
print "\n"

