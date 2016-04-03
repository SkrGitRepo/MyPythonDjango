'''
Created on Feb 20, 2016

@author: sumkuma2
'''

import urllib2
import re

#response = urllib2.urlopen('http://mailer-api.cisco.com/itsm/mailer/rest/text/noauth/members/cpo-dev-superuser')
response = urllib2.urlopen('http://127.0.0.1:8090/prime/optical/onramp/api/usertype/cpo-dev-superuser')
datas = response.read()

mydatadict = {'datadict':datas}
#for value in (mydatadict.values()) :
#    users = value.split('\n')
users = datas.split('\n')
users = filter(None,users) #to remove any empty list item
print users;

user_list = []
for user in users:
    user = re.sub('\t|<br/>','', user.strip())
    #user = re.sub('<br/>','', user.strip())
    #user = re.sub('\n','', user.strip())
    user_list.append(user)
user_list = filter(None,user_list) #to remove any empty list item    
print(user_list)

if 'alchu' in users:
    print "match found"

else:
    print "Not found"
#for user in users:
#    print user

#print data

if __name__ == '__main__':
    pass