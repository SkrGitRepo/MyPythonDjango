'''
Created on Feb 16, 2016

@author: sumkuma2
'''


"""
Dictionary data type example using for loop
Dictionaries are indexed by keys. You can use key and value pair using a Python for loop. The following example illustrates this concept:
"""

 
# define a dict data type for our dns server as geoLocation : DNS server name
dnsservers = {"us":"ns1.cyberciti.com", "uk":"ns2.cyberciti.biz", "asia":"ns3.cyberciti.org"  }
 
# Python for loop for key,value using dict data type
for location, server in dnsservers.iteritems():
    print server, "dns server is located in" , location
    
    
print "------------------------------------------------------------------------------------"
## Dict data type
#dnsservers = {"us":"ns1.cyberciti.com", "uk":"ns2.cyberciti.biz", "asia":"ns3.cyberciti.org"  }
 
## Is location found ? 
found = False
 
## INPUT: Search for a geo location 
search_ns_location = raw_input("Provide geo location :")
 
## Use for loop to search geo location for ns
for location, server in dnsservers.iteritems():
    if location == search_ns_location:
        print server, "dns server is located in :" , search_ns_location
        found = True
 
## Display an error 
if found == False :
    print search_ns_location ,"not a valid geo location."