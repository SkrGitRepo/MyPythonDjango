#Python Control Structure
#Indentation is very important in Python
'''
x,y = input("Enter x,y")
if x>y:
    print "x is greater y",x
else:
    print "y is greater",y
'''


'''
x,y,z = input("Enter x,y,z")

if x>y and x>z:
    print "x %d is greatest than y:%d and z:%d "%(x,y,z)
elif y>x and y>z:
    print "y is greatest",y
elif z>x and z>y:
    print "z is greatest",z
elif x==y and y==z and z==x:
    print "x:%d ,y:%d, and z:%d are equals."%(x,y,z)
'''
# making the code indented. (Same level of structure is scope the sturcuter ) 
while True:
    x,y,z = input("Enter x,y,z:")
    if x>y and x>z:
        print "x %d is greatest than y:%d and z:%d "%(x,y,z)
    elif y>x and y>z:
        print "y is greatest",y
    elif z>x and z>y:
        print "z is greatest",z
        break;
    elif x==y and y==z and z==x:
        print "x:%d ,y:%d, and z:%d are equals."%(x,y,z)

print "Outside the loop"
    


