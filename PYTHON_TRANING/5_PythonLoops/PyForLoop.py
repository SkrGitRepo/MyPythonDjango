'''
Created on Feb 16, 2016

@author: sumkuma2
'''
#
# for-loop.py: Sample for loop to print welcome message 3 times
#
for i in '123':
        print "Welcome",i,"times"
        

print "------------------------------------------------------------------------------------"
"""
Nested for loop example
The following code shows classic nested for loop using python:
"""
### Outer for loop ###
for x in xrange(1,6 ):
    ### Inner for loop     ###
    for y in xrange(1, 6):
        print '%d ' % (x),
    print ""
    
    
print "------------------------------------------------------------------------------------"   
"""
Iterating python for loop using range() function
Instead of using a string called '123', try range() to iterate over a sequence of numbers:

It is recommended that you use the xrange() function to save memory:
"""
print "*** Generates a list of 3 values starting from 0 using range(3)***"
for i in range(3):
        print "Welcome",i,"times."
 
print "*** Generates a list of 3 values starting from 1 using range(1,3)***"
for i in range(1,4):
        print "Welcome",i,"times."