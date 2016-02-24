def Var(*arg):
    print arg
Var(4,6,'hello')


#-------------------------
#Mult(1,2,3,4) = (1*2*3*4)

def Mult(*arg):
    mul =1
    for num in arg:
        mul = mul*num
    print mul 
    
Mult(5,2,3,4)
