#zip
Que=['name','loc','age','email','mobile']
Ans=['Sumit','Bangalore','30','sumit@gmail.com','9844816548']
for q,a in zip(Que,Ans):
    print "What's your %s, it is %s"%(q,a)
print zip(Que,Ans)

z1=zip(Que,Ans)
phone=dict(z1)
print phone,

