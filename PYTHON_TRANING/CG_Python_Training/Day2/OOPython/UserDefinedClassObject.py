# Object Oriented in Python
# Class
#object is the super class of all class in Python
'''
class Capgemini(object): #inherting the super class 'object'
    pass

obj=Capgemini()
print obj
print dir(obj)
print help(obj)
'''

from Cg import Capgemini
#creating 
obj=Capgemini('Bangalore','Karnataka','India')
#print obj
obj.Info()
obj1=Capgemini('Pune','Maharastra','India')
#print obj
obj1.Info()
obj2=Capgemini('Mumbai','Maharastra','India')
#print obj
obj2.Info()
obj3=Capgemini('Chennai','Tamilnadu','India')
#print obj
obj3.Info()
obj4=Capgemini('Hayderabad','Andhra Pradesh','India')
#print obj
obj4.Info()
obj5=Capgemini('Bangalore','Karnataka','India')
#print obj
obj5.Info()



