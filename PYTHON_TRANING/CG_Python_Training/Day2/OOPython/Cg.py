# Object Oriented in Python
# Class
#Creating a user defined class 'Capgemini'
#First param of a object is "self"(Its a refeerence to the current instance of a class)
# Here "self" is similar as this of java

class Capgemini:
    '''This is a capgemini class'''
    brnchcode =111 #class variable
    
    def __init__(self,city,state,country):
        '''Initializing it'''
        print "Constructor : to initialize class 'Capgemini'"
        self.c=city #object variable
        self.s=state
        self.cn=country
        Capgemini.brnchcode+=1 #calling the class variable directly using class name
        print "Bracnch code is:",Capgemini.brnchcode
        
    def Info(self): 
        print "This is capgemini Information"
        print "City is %s and state is %s"%(self.c,self.s)
        print "Country is %s"%self.cn







