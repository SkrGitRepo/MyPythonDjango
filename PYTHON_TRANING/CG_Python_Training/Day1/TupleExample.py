# Tuple is sequence od any type of data element
# Tuple example : Immutable data structure : We can't modify tuple
# Tuple is for read only purpose
# List(mutable) for read and write access


t =1,3,5,'hello','python'
print t
'''print type(t)
for i in t:
    print i

t1=()
print type(t1)
'''
print t[1]
#t[1]=8 # gives error since immutable

#print dir(t)

#swapping data 
(a,b,c,d,e) = (4,5,6,7,'hello')
print "Before Swapping :",a,b,c,d,e
(a,b,c,d,e) = (e,d,c,b,a)
print "After Swapping :",a,b,c,d,e

t2 = (1,2,3,4,5,6,7)
print t2[1]
print t2[5]
print t2[1:5]



