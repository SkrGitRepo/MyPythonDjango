import NetApp as NA

print dir(NA)
print help(NA)
#print NA.version()
print NA.socket1()
print NA.bind()
print NA.listen()
print NA.send()
print NA.recieve()
print NA.end()

#'accept', 'bind', 'end', 'listen', 'recieve', 'send', 'socket1', 'version'
import NetApp
print NetApp.socket1()
print NetApp.send()


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
