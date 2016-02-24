'''
Created on Oct 14, 2015

@author: sumkuma2
'''
import httplib
#conn= httplib.HTTPSConnection("www.python.org")
conn= httplib.HTTPConnection("http://mailer-api.cisco.com/itsm/mailer/rest/text/noauth/members/cpo-dev-superuser")
conn.request("GET","/")
r1 = conn.getresponse()
print r1.status,r1.reason
#200 OK
data1 = r1.read()
print data1

conn.request("GET","/")
r2 = conn.getresponse()
print r2.status,r2.reason
#404 No found
data2 = r2.read()
print data2
conn.close()

