#Assignment

#Reverse the (key,value) to vice versa (value,key) dictionary
Que=['name','loc','age','email','mobile']
Ans=['Sumit','Bangalore','30','sumit@gmail.com','9844816548']
z1=zip(Que,Ans)
phone=dict(z1)
print phone

K = phone.keys()
V = phone.values()
z2= zip(V,K)
phone2= dict(z2)
print phone2






     


