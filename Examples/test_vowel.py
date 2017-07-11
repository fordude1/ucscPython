original = raw_input('Enter a word:')
#word = original.lower()
first = word[0]

if len(original) > 1: #and original.lower():
    if first == "a" or "e" or "i" or "o" or "u":
        print "vowel"
    else:
        print "consonant"
else:
    print "empty"