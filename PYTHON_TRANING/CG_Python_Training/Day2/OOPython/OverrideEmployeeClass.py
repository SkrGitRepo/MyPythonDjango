#Rules of 
from Cg import Capgemini

class Account(Employee): #inhariting Employee class
    #this must have same as from inherited class    
    def __init__(self,city,state,country,ename,emp_acnt):
        self.e_account=emp_acnt
        #this has to be done to say variables are initialized in Super Class 'capgemini'
        Employee.__init__(self,city,state,country,ename)
    def Info(self):
        Capgemini.Info(self)
        print "Employee account is  %s :"%self.e_account

        
    

#creating object of Capgemini class imported from module Cg
obj=Account('Bangalore','Karnataka','India','sumit','developemt')
obj.Info()
obj1=Account('Pune','Maharastra','India','Zaheer','finance')
obj.Info()





