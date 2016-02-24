'''
Created on Feb 16, 2016

@author: sumkuma2
'''
"""
Python Lists:
Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]).
list can be of different data type.
The values stored in a list can be accessed using the slice operator ( [ ] and [ : ] ) with indexes starting at 0 in the
beginning of the list and working their way to end -1. The plus ( + ) sign is the list concatenation operator, and the
asterisk ( * ) is the repetition operator. For example:
"""

my_movie_list =['DDLZ','RHTDM','Blood Diamond',123,'Khiladi420']
new_movie_list = ['Deadpool','Break Point','Fitoor']


print my_movie_list
print my_movie_list[0]
print my_movie_list[2:4]
print my_movie_list[3:]
print my_movie_list * 2
print my_movie_list + new_movie_list

### We can modify(insert,update element of a Lists)
#my_movie_list =['DDLZ','RHTDM','Blood Diamond',123,'Khiladi420']
my_movie_list[3] ='Titanic'
print "List after update:",my_movie_list