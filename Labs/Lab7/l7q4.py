'''
Write a Python script that will print out the lyrics to "99 Bottles of Beer
on the Wall"

Song goes like this:
99 bottles of beer on the wall, 99 bottles of beer!
So take it down, pass it around, 98 more bottles of beer on the wall!
'''

for beer in range(99, 0, -1):
    print beer, "bottles of beer on the wall,", beer, "bottles of beer!"
    print "So take it down, pass it around, ", beer - 1, "more bottles of beer on the wall!"
    print