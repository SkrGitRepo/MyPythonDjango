'''
Created on Feb 20, 2016

@author: sumkuma2
'''

import urllib2


response = urllib2.urlopen('http://mailer-api.cisco.com/itsm/mailer/rest/text/noauth/members/cpo-dev-superuser')
datas = response.read()

mydatadict = {'datadict':datas}
#for value in (mydatadict.values()) :
#    users = value.split('\n')
users = datas.split('\n')
users = filter(None,users) #to remove any empty list item
print users;

if 'alchu' in users:
    print "match found"

else:
    print "Not found"
#for user in users:
#    print user

#print data

if __name__ == '__main__':
    pass