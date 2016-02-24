
#Find the fibonacci series.
print "\nFibonacci till 100"
class fibnum:
    def __init__(self):
        self.fn2=1
        self.fn1=1
        
    def next(self): #this is the default method of any object
        (self.fn1,self.fn2,oldfn2)=(self.fn1+self.fn1,self.fn1,self.fn2)
        #if oldfn2 >20:raise StopIteration
        return oldfn2
    
    def __iter__(self): #Iteration of object :this is the default method of any object
        return self

#from fib import fibnum
obj = fibnum()

for i in obj:
    print i,
    if i>100:break
#------------------------------------------
print "\nFibonacci till 20"    
class fibnum20:
    def __init__(self):
        self.fn2=1
        self.fn1=1

    def next(self): #this is the default method of any object
        (self.fn1,self.fn2,oldfn2)=(self.fn1+self.fn1,self.fn1,self.fn2)
        if oldfn2 >20:raise StopIteration
        return oldfn2

    def __iter__(self): #Iteration of object :this is the default method of any object
        return self



#from fib import
obj = fibnum20()

for i in obj:
    print i,
    #if i>100:break
