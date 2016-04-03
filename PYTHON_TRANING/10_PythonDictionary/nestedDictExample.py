'''
Created on Mar 30, 2016

@author: sumkuma2
'''

#This require Python external module to be insalled
# pip install nested_dict==1.0.9
#from nested_dict import *
from nested_dict import nested_dict

subtypeofuser=1
username=('sumkuma2')
username1=('anil','zaheer')
nd=nested_dict()
nd["eon-rtp3-1-l"][subtypeofuser]=username
nd["eon-rtp3-1-l"][4]=username
nd["eon-rtp3-1-l"][5]=username1

nd["eon-rtp3-2-l"][subtypeofuser]=username
nd["eon-rtp3-2-l"][4]=username
nd["eon-rtp3-2-l"][5]=username1


print nd

#nested way of dictionary iteration
for k, v in nd.iteritems_flat():
    #print "%-30s = %20s" % (k,v)
    if k[0] == 'eon-rtp3-1-l' and k[1] ==1:
        print "eon-rtp3-1-l :: SuperUser :: ",v
    elif k[0] == 'eon-rtp3-1-l' and k[1] ==2:
        print "eon-rtp3-1-l :: Sysadmin :: ",v
    elif k[0] == 'eon-rtp3-1-l' and k[1] ==3:
        print "eon-rtp3-1-l :: Network Admin :: "
    elif k[0] == 'eon-rtp3-1-l' and k[1] ==4:
        print "eon-rtp3-1-l :: Operator :: ",v
    elif k[0] == 'eon-rtp3-1-l' and k[1] ==5:
        print "eon-rtp3-1-l :: Provisioner :: ",v

#simple dictionary iteration
for k, v in nd.items():
    print "%s = %s" % (k,v)
    for k1,v1 in v.items():
        print "%-s = %s" % (k1,v1)
        #print k1,v1
         
