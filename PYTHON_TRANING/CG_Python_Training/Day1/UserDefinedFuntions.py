#User Defined Functions in python
def fun():
    ''' Functiona example documentation '''
    print "Function example fun"


#calling the function
'''    
fun()
s=fun
print s.func_name
print s.__doc__
help(0)

(num1)=input("Enter Num1")
(num2)=input("Enter Num2")

#addition(num1,num2)
#funtion definition
def addition(num1,num2):
    add = num1+num2
    print "Addition of Num1:%d and Num2:%d is:%d"%(num1,num2,add)

#Calling the function
addition(num1,num2)
'''

#---------------------------------------------------------
#local and global scope of a funtion

def func(x):
    print "Value of x before assignment",x
    x=5 #local assignment
    print "Value of x after assignement",x


x=50 #Global assignment
func(20)
print "Value after function ",x


#-----------------------------------------------------------
def func():
    global x
    print "Value of x before assignment",x
    x=5 #making this value global assignment
    print "Value of x after assignement",x


x=50 #Global assignment
func()
print "Value after function ",x
#-------------------------------------------------------------







