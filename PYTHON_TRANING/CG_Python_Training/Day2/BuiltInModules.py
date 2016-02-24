#--------------------------
import sys
print "Where Python looks for modules::"
print sys.path
'''
OUTPUT:
-----------------------------
['C:/Python_Training/Day2', 'C:\\Python27\\Lib\\idlelib',
'C:\\Windows\\system32\\python27.zip', 'C:\\Python27\\DLLs',
'C:\\Python27\\lib', 'C:\\Python27\\lib\\plat-win', 'C:\\Python27\\lib\\lib-tk',
'C:\\Python27', 'C:\\Python27\\lib\\site-packages']
'''

#to add extra path:
#better to give absolute path
#sys.path.append("/mypath/../..")

#-----------------------------
import os
print os.getcwd() #current workinf dir
print dir(os)
#print help(os.mkdir)
print os.system('ls -l')
#os.mkdir('capg') # to create a dir
#help(os.rename) # to know how OS module rename functions systax 
