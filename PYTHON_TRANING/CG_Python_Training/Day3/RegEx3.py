import re

s=''' Mobile 9844816548 \n\t email:sumit@gmail.com 8861733377
email:skr@gmail.com\n\t,email :sumit_skr@gmail.com'''

#using sting method #limited use for specific no f replacement
print s.replace('email','EMAIL')

#using regex sub
print re.sub('email','EMAIL',s)

#using regex sub for specific no of match
print re.sub('email','EMAIL',s,2)

#using regex sub for specific no of match and hide with specific chars
print re.sub(r'\b[\w.]+@\w+.\w{2,3}\b','EMAILADDRESS',s,2)






