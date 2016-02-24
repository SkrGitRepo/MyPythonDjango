'''
Created on Feb 16, 2016

@author: sumkuma2
'''
"""
Data Type Conversion:
Sometimes, you may need to perform conversions between the built-in types. To convert between types, you
simply use the type name as a function.
There are several built-in functions to perform conversion from one data type to another.

"""
print "------------------------------------------------------------------------------------------"
my_int_var =239

print "INT var before conversion to FLOAT: ",my_int_var
print "INT var after conversion to FLOAT: ",float(my_int_var)
print "INT var after conversion to LONG: ",long(my_int_var)
print "------------------------------------------------------------------------------------------"
my_string = "Hello Python"
print " String \'%s\' converted to TUPLE :"%(my_string),tuple(my_string)
print " String \'%s\' converted to LIST :"%(my_string),list(my_string)
print " String \'%s\' converted to SET :"%(my_string),set(my_string)
print " String \'%s\' converted to FROZEN SET :"%(my_string),frozenset(my_string)

print "------------------------------------------------------------------------------------------"
my_seq ="sumit is a programmer since 2000"
print "*** Before converting to a TUPLE:\n",my_seq
print "*** After converting to a TUPLE:\n",tuple(my_seq)

print "------------------------------------------------------------------------------------------"
converted_str_tuple = ((1,'mango'),(2,'apple'))
print "Tuple :",converted_str_tuple
print " Tuple converted to DICTIONARY :\n",dict(converted_str_tuple)


print "------------------------------------------------------------------------------------------"
my_char = 's'
print " Char '%s' converted to ord(my_char) its integer (ASCII) value :"%(my_char),ord(my_char);
my_int = 115
print " Int '%d' converted to chr(my_int) its character (ASCII) value:"%(my_int),chr(my_int);
print " Int '%d' converted to chr(my_int) its UNICHR (ASCII) value:"%(my_int),unichr(my_int);
