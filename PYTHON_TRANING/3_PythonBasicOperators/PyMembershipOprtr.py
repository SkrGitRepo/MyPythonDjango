'''
Created on Feb 16, 2016

@author: sumkuma2
'''
"""
Python Membership Operators:
Python has membership operators, which test for membership in a sequence, such as strings, lists or tuples. There are two membership operators 
explained below:
1) In -Evaluates to true if it finds a variable in the specified sequence and false otherwise.
Example:
 x in y, here in results in a 1 if x is a m
 
2) not in - Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
Example:
x not in y, here not in results in a 1 if x is not a member of sequence y. 
"""


a = 10
b = 20
my_list = [1, 2, 3, 4, 5 ];

if ( a in my_list ):
    print "Line 1 - a is available in the given list"
else:
    print "Line 1 - a is not available in the given list"
    

if ( b not in my_list ):
    print "Line 2 - b is not available in the given list"
else:
    print "Line 2 - b is available in the given list"

a = 2

if ( a in my_list ):
    print "Line 3 - a is available in the given list"
else:
    print "Line 3 - a is not available in the given list"
