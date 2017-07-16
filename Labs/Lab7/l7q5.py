'''
Write a python script that will compute 10!.. This is 10 factorial.
Remember: 10 factorial is 10 * 9 * 8 * 7 *.....N
'''

# initialize the variable
factorial = 1

# start the range loop
for number in range(10, 0, -1):
    factorial = factorial * number

# print the result of 10!
print "10! =", factorial

