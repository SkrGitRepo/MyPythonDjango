'''
Created on Feb 14, 2016

@author: sumkuma2
'''
'''
Python has five standard data types:
Numbers
String
List
Tuple
Dictionary
'''

'''
PYTHON NUMBERS
Number data types store numeric values. They are immutable data types which means that changing the value of
a number data type results in a newly allocated object.
Number objects are created when you assign a value to them. For example:
'''
var1 = 1
var2 = 10
var= 20000
var_a= 400000
var_b= 300000
''' You can delete a single object or multiple objects by using the del statement. For example: '''
print "Numbers before REFRENCE del: %d,%d,%d"%(var,var_a,var_b)
#del var
#del var_a, var_b
#print "Numbers after REFRENCE del: %d,%d,%d"%(var,var_a,var_b)

'''
Python supports four different numerical types:
int (signed integers)
long (long integers [can also be represented in octal and hexadecimal])
float (floating point real values)
complex (complex numbers)
'''
long_int = 4678432999L
float_int = 1000.543
print "LONG INT :",long_int
print "FLOAT INT :",float_int