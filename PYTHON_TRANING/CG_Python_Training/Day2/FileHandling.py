data='''Ericsson OSS product will have around 350 applications and all the applications will be packaged
under a single build and provided to the customer for the upgrade. This upgrade module will have set
of defined procedures how to upgrade the software between various tracks and also clear steps to
upgrade various features based on licenses. Once the upgrade is successful, the customers can attach various LTE/GSM nodes to the severs.
All the servers provided to the customer will be clustered environment where if one node fails other node can take up to cater HA (High Availability) Environment'''

f=open('test.txt','w+')
#print f
f.write(data)
f.close()
f1=open('test.txt')
print "Printing content from file 'text.txt':::"
'''print f1.readline()

print f1.tell()

print f1.read()
print f1.tell()
print f1.readline()

print f1.tell()
f1.seek(0)
print f1.readline()
print f1.tell()'''

#print f1.readlines()
filedata = f1.readlines()
filedata.insert(2,'I am newly inserted line.');
print filedata
f1.close()

ftowrite=open('test.txt','w+')
ftowrite.writelines(filedata)
ftowrite.close()

fread=open('test.txt')
print fread.read()
fread.close()


with open ('test.txt') as f:
    print f.read()

print f













