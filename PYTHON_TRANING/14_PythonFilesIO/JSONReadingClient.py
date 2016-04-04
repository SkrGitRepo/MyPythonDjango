'''
Created on Apr 3, 2016

@author: sumkuma2
'''
import urllib2
import json
from pprint import pprint



response = urllib2.urlopen('http://127.0.0.1:8090/prime/optical/user/api')
#response = urllib2.urlopen('https://api.instagram.com/v1/tags/pizza/media/XXXXXX')
data = json.load(response) 
print data  
pprint (data)

print "Printing JOSN key 'results'-> data Key-Value"
print "USERID:",data['results'][0]['userid']
print "USERNAME:",data['results'][0]['username']

print "Displaying each userid,username from JOSON 'results'"
for i in xrange(len(data['results'])):
    print "USERID:",data['results'][i]['userid']
    print "USERNAME:",data['results'][i]['username']



#print response

