#Filter the item logically
# It is a funtion which allows the data to be filtered of a sequence
# A filter return true value from given sequence passed


print "Filtering the prime num in given range using filter and lambda method"
seq=range(2,25)
print seq
fun1 = lambda n:n % 2!=0 and n % 3 !=0
print filter(fun1,seq)

print "\npassing seqence explicitly"
print filter(fun1,(1,2,3,4,5,6,7))

print "\nWithout using lambda funtion"
def fun2(x):
    return x % 2!=0 and x % 3 !=0
print filter(fun2,(1,2,3,4,5,6,7,9,8,11,67))


print "using *arg"
Varg=lambda *arg:arg
print Varg(1,2,3,4)

print "Use of lambda using variable argument *arg **kw"
Varg1=lambda *arg,**kw:(arg,kw)
print Varg1(1,2,3,4,a=42,b=93)


#print "Use of lambda using variable argument *arg and loop"
#Varg2=lambda *arg:[arg, for i in arg]
#print Varg2(1,2,3,4)

