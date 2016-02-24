import re
#---------------------------------------
#Spliting in regex
s=''' Mobile 9844816548 \n\t email:sumit@gmail.com 8861733377
email:skr@gmail.com\n\t,email :sumit_skr@gmail.com'''

print re.split(r'\b[\w.]+@\w+.\w{2,3}\b',s)

print re.split(r'\b[\w.]+@\w+.\w{2,3}\b',s,1)

