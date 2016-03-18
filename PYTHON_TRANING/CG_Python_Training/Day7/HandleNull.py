'''
Created on Oct 29, 2015

@author: sumkuma2
'''
''' Example to handle variable null value in Python'''

try:
    #x   -> when x have not assigned any value , it throw a NameError
    x=5
except NameError:
    x=None
    
if x == None:
    print "X has no value"
else:
    print x