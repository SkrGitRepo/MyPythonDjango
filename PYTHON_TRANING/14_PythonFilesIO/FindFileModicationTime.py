'''
Created on Mar 28, 2016

@author: sumkuma2
'''
import os
import time

file="readme.txt"
print "last modified: %s" % time.ctime(os.path.getmtime(file))
print "created: %s" % time.ctime(os.path.getctime(file))
print "-----------------------------------------------------------------------------"
print os.__all__
print "-----------------------------------------------------------------------------"
print os.path.__all__
print os.path.__doc__
print "-----------------------------------------------------------------------------"
print time.__doc__
print "-----------------------------------------------------------------------------"