#this display 2 steps forwrd between 1 to 10
#what is the difference between range and xrange ???

print list(xrange(1,10,2))
print tuple(xrange(1,10,2))

for i in xrange(1,10,2):
    print i,
