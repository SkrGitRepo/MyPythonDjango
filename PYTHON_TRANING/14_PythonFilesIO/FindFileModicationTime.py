'''
Created on Mar 28, 2016

@author: sumkuma2
'''
import os
import time

file="readme.txt"
print "last modified: %s" % time.ctime(os.path.getmtime(file))
print "created: %s" % time.ctime(os.path.getctime(file))