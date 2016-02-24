# Map fuction works only on sequence: tuple,list
# in map No of seq and no. of parammeter to the function should be same

cube=lambda a:a**3
print cube(2)

print "After applyin map function"
print map(cube,(2,4,6,5,7,9))

seq1= range(1,5)
seq2=range(6,10)
seq3=range(11,15)

print seq1,"\n",seq2,"\n",seq3

print "add first three value of sequence"
add=lambda x,y,z:x+y+z
print map(add,seq1,seq2,seq3)


mul=lambda x,y,z:x*y*z
print map(mul,seq1,seq2,seq3)


#lambda _:fibo_series.append( fibo_series[-1] + fibo_series[-2]), xrange(8)
#print "FIBo ",fibo_series

fibo_series =[0,1]
fib = lambda n: map(lambda _: fibo_series.append(fibo_series[-1] + fibo_series[-2]), xrange(n-2))
print fib(4) ## Ignore its output ##
print fibo_series
