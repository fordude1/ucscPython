'''
Conditional Statements combined with operators (comparison or relational,
assignment, arithmetic, and logical).  For each sentence, translate the
sentence to Python code using your operators:

if i is from 2 to 78, subtract 2 from i

if j is not between 10 and 15 but is the
number 11, then k equals j times 2

if k is not equal to 7 and i equals 5 or j
is greater than 8, set x equal to 200
divided by k

if i is the sum of j and k, and j is not
equal to sum of i and k, then x equals j
times k divided by i
'''

# First problem
if i > 2 and i < 78:
    i - 2


# Second problem
if j !> 10 and j !< 15 and == 11:
    k = j * 2

# Third problem
if k != 7 and i == 5 or j > 8:
    x = 200/k

# Fourth problem
if i == j + k and j != i + k:
    x = j * k / i


