
Que=['name','loc','age','email','mobile']
Ans=['Sumit','Bangalore','30','sumit@gmail.com','9844816548']
z1=zip(Que,Ans)
phone=dict(z1)
print phone
#Dictinary Comprehension
comp = {v:k for k,v in phone.items()}
print comp

#print phone{k.upper():v for k,v in phone.items()}


#list Comrehension
print "List of tuple :(n,n*n*n)\n",[(x,x**3) for x in range(1,10)]
print "Filter :\n", [x for x in range (2,25) if x%2 !=0 and x%3!=0]
print "Filter and cube:\n", [(x,x**3) for x in range (2,25) if x%2 !=0 and x%3!=0]
