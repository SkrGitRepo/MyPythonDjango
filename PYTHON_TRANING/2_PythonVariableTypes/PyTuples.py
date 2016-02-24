'''
Created on Feb 16, 2016

@author: sumkuma2
'''
"""
Python Tuples:
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated
by commas. Unlike lists, however, tuples are enclosed within parentheses.
The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and
size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.

For example:
"""

my_movie_tuple = ('DDLZ','RHTDM','Blood Diamond',123,'Khiladi420')
my_movie_new_tuple = ('Deadpool','Break Point','Fitoor')

print my_movie_tuple
print my_movie_tuple[0]
print my_movie_tuple[2:4]
print my_movie_tuple[3:]
print my_movie_tuple * 2
print my_movie_tuple + my_movie_new_tuple

### We can not modify(insert,update element of a tuple)
#my_movie_tuple[3] = 'Titanic' #this is not allowed with tuple
#print "Tuple after update :",my_movie_tuple 

### We can modify(insert,update element of a Lists)
my_movie_list =['DDLZ','RHTDM','Blood Diamond',123,'Khiladi420']
my_movie_list[3] ='Titanic'
print "List after update:",my_movie_list

