'''
Created on Feb 16, 2016

@author: sumkuma2
'''


"""
Python Identity Operators:
Identity operators compare the memory locations of two objects. There are two Identity operators explained below:

Operator | Description
------------------------------------------------------
1) Is | Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
Example : x is y, here is results
in 1 if id(x) equals id(y).

2) is not | Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
Example:
x is not y, here is not results in 1 if id(x)
is not equal to id(y).

"""


a = 20
b = 20

if ( a is b ):
    print "Line 1 - a and b have same identity"
else:
    print "Line 1 - a and b do not have same identity"
    

if ( id(a) == id(b) ):
    print "Line 2 - a and b have same identity"
else:
    print "Line 2 - a and b do not have same identity"
    
b = 30
if ( a is b ):
    print "Line 3 - a and b have same identity"
else:
    print "Line 3 - a and b do not have same identity"

if ( a is not b ):
    print "Line 4 - a and b do not have same identity"
else:
    print "Line 4 - a and b have same identity"