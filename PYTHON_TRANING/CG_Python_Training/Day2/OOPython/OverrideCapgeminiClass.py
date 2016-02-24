#Rules of 
from Cg import Capgemini

class Employee(Capgemini): #inhariting Capgemini class
    #this must have same as from inherited class    
    def __init__(self,city,state,country,ename):
        self.emp_name=ename
        #this has to be done to say variables are initialized in Super Class 'capgemini'
        Capgemini.__init__(self,city,state,country)
    def Info(self):
        Capgemini.Info(self)
        print "Employee name is  %s :"%self.emp_name

        
    

#creating object of Capgemini class imported from module Cg
obj=Employee('Bangalore','Karnataka','India','sumit')
#print obj
obj.Info()
obj1=Employee('Pune','Maharastra','India','Zaheer')
#print obj
obj1.Info()
obj2=Employee('Mumbai','Maharastra','India','Anil')
#print obj
obj2.Info()
obj3=Employee('Chennai','Tamilnadu','India','Veera')
#print obj
obj3.Info()
obj4=Employee('Hayderabad','Andhra Pradesh','India','Anjee')
#print obj
obj4.Info()


class Account(Employee): #inhariting Employee class
    #this must have same as from inherited class    
    def __init__(self,city,state,country,ename,emp_acnt):
        self.e_account=emp_acnt
        #this has to be done to say variables are initialized in Super Class 'capgemini'
        Employee.__init__(self,city,state,country,ename)
    def Info(self):
        Capgemini.Info(self)
        print "Employee account :: %s "%self.e_account

        
    

#creating object of Capgemini class imported from module Cg
obj=Account('Bangalore','Karnataka','India','sumit','developemt')
obj.Info()
obj1=Account('Pune','Maharastra','India','Zaheer','finance')
obj.Info()





