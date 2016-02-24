'''
Created on Feb 16, 2016

@author: sumkuma2
'''

"""
nested if statements ::
Syntax ::
    if expression1:
        statement(s)
        if expression2:
            statement(s)
        elif expression3:
            statement(s)
        else
            statement(s)
    elif expression4:
        statement(s)
    else:
        statement(s)
"""

var = 100

if var < 200:
    print "Expression value is less than 200"
    if var == 150:
        print "Which is 150"
    elif var == 100:
        print "Which is 100"
    elif var == 50:
        print "Which is 50"
elif var < 50:
    print "Expression value is less than 50"
else:
    print "Could not find true expression"