#What is Dictionary in python(Key:Value storage).
#its an un-ordered collection
#Key should be unique.
#Key should always be of immutable type
#int value


personalData={}
personalData['name'] = 'Sumit'
personalData['email_id'] = 'sumit@gmail.com'
personalData['contact_no'] = 9844816548

print personalData
print "My Mobile no is ",personalData['contact_no']
print "My email is is ",personalData.get('email_id')
print "Keys of my personalData Dictionary :",personalData.keys()
print "Values of my personalData Dictionary :",personalData.values()
personalData['city']= 'Bangalore'
print personalData
personalData['email_id']='sumit_skr@hotmail.com'
print "Modified dictionary :",personalData

#--------------------------------------------------------------
def funct(*arg,**kwarg):
    '''This is a special function in Python'''
    print arg
    print kwarg

f=funct
f(3,4,'apple',a=5,b=9,c='cat')
#print f
#this solves the overloading functilnality in Python

#--------------------------------------------------------------
#passing default value
def dfv(a=6,b=8):
    print a+b
dfv()


