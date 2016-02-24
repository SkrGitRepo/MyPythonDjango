#When to write Decorator: functionas which need to be called regulary ,can be made as decorator
#To reduce line of code
# To write stylish code



def trace ( aFunc ):
    """Trace entry,exit and exceptions. """
    def loggedFunc(*args,**kwargs):
        print "Enter ",aFunc.__name__
        print "Document of function", aFunc.__doc__
        try:
            result=aFunc(*args,**kwargs)
        except Exception,e:
            print "Exception",aFunc.__name__,e
            raise
        print "Exit",aFunc.__name__
        return result

    return loggedFunc


@trace
def add(x,y):
    '''This is addition of two variables'''
    print "Addition of %d and %d is:"%(x,y)
    return x+y

@trace
def mul(x,y):
    '''This is multiplication of two variables'''
    print "Multiplication of %d and %d is:"%(x,y)
    return x*y


print "Addition :",add(3,4)
print "Multiplication :",mul(5,6)
    
            
        
