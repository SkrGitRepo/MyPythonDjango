'''
Created on Feb 16, 2016

@author: sumkuma2
'''
print "------------------------------------------------------------------------------------"   
"""
It is recommended that you use the xrange() function to save memory:
"""
# Python for loop using xrange()
 
print "*** Generates a list of 3 values starting from 0 using xrange() ***"
for i in xrange(3):
        print "Welcome",i,"times."
 
print "*** Generates a list of 3 values starting from 1 using xrange() ***"
for i in xrange(1,4):
        print "Welcome",i,"times." 
        
print "*** range() vs xrange() ***"
print "It is recommended that you use the xrange() function to save memory."
print "range() creates a list containing numbers all at once."
print "xrange() creates a list containing numbers as needed."