import re
#use of (r) raw string and boudary character 

s=''' Mobile 9844816548 email sumit@gmail.com 8861733377
skr@gmail.com,sumit_skr@gmail.com'''

print re.findall('\\b\d{10}\\b',s) #
print re.findall(r'\b\d{10}\b',s) # r is to escape all special symbol in the string

s=''' Mobile 9844816548 \n\t email sumit@gmail.com 8861733377
skr@gmail.com\n\t,sumit_skr@gmail.com'''
print s

#used r(raw string) to escape special symbol from string
s=r''' Mobile 9844816548 \n\t email sumit@gmail.com 8861733377
skr@gmail.com\n\t,sumit_skr@gmail.com'''
print s


#extract email address from given string
s=''' Mobile 9844816548 \n\t email sumit@gmail.com 8861733377
skr@gmail.com\n\t,sumit_skr@gmail.com'''
print re.findall(r'\b[\w.]+@\w+.\w{2,3}\b',s)
print re.findall(r'\b[\w.]+@\w+.\w{2,3}\b',s).__len__()


