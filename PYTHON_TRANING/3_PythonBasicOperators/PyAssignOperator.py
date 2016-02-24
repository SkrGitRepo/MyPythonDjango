'''
Created on Feb 16, 2016

@author: sumkuma2
'''
a = 21
b = 10
c = 0
c = a + b
print "Line 1 - Value of c is ", c
c += a
print "Line 2 - Value of c is ", c


c *= a
print "Line 3 - Value of c is ", c
c /= a
print "Line 4 - Value of c is ", c

c = 2
c %= a
print "Line 5 - Value of c is ",c


"""
**= :Exponent AND assignment operator, Performs exponential (power)
calculation on operators and assigns value to the left operand
"""
c **= a
print "Line 6 - Value of c is ", c


"""
//= :Floor Dividion and assigns a value, Performs floor division on operators and
assigns value to the left operand
"""
c //= a
print "Line 7 - Value of c is ", c