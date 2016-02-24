'''
Created on Feb 16, 2016

@author: sumkuma2
'''
# Sample for loop using a List
 
## define a list 
shuttles = ['columbia', 'endeavour', 'challenger', 'discovery', 'atlantis', 'enterprise', 'pathfinder' ]
 
## Read shuttles list and store the value of each element into var shuttle and display on screen
for shuttle in shuttles:
        print shuttle

print "------------------------------------------------------------------------------------"         
'''
To print index and its value, try enumerate(). It simplify a commonly used looping methods. It provides all iterable collections with the
 same advantage that iteritems() affords to dictionaries -- a compact, readable, reliable index notation:
'''
# A list of shuttles , to print index and value using enumerate function 
#shuttles = ['columbia', 'endeavour', 'challenger', 'discovery', 'atlantis', 'enterprise', 'pathfinder' ]
 
## Read shuttles list and enumerate into index and value 
for index, value in enumerate(shuttles):
        print index, value
    