#set is a unordered sequence with unique item
basket=['apple','banana','orange','apple','mango','banana','papaya']
fruits=set(basket)
print "As unordered set"
print "Un-Ordered",fruits
print "As Ordered set"
print "Ordered",sorted(fruits)

print "Is orange in basket set ::",'orange' in fruits
#-----------------------------------------------------------
a=set('absdkelpfafgg')
print a
b=set('kdfgrelm')
print b

#combination of both a and b set
c= a|b
print "union1",c
c1=a.union(b)
print "union2",c1

#found in both a and b set
d=a&b
print "Intersection1",d
d1=a.intersection(b)
print "Intersection2",d1

#unique in a and b
print "Uncommon on a and b",a^b

#c is superset of a and b
print "IS Superset of a and b :",c.issuperset(a)
print "IS a is subset of c :",a.issubset(c)



