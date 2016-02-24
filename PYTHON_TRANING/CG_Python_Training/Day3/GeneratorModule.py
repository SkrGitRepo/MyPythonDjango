#creating the genrator to iterator
def gy():
    x=5
    y=3
    yield x,y
    z=x/y
    yield z
    yield x+y
    return

g=gy()
print g
for i in g:#internally next() is getting called here ,"for" has "next" defined for it default
    print i,
    
#print g.next()
#print g.next()
#print g.next()
#print g.next()
