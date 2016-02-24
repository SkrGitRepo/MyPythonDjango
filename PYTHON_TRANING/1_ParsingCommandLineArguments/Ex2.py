'''
Created on Feb 14, 2016

@author: sumkuma2
'''
'''
Accessing Command Line Arguments:
  The Python sys module provides access to any command-line arguments via the sys.argv. This serves two
purpose:
sys.argv is the list of command-line arguments.
len(sys.argv) is the number of command-line arguments.
Here sys.argv[0] is the program ie. script name.

'''
import sys;

print "\n Number of command line arguments passed",len(sys.argv);
print "\n Argument List :",str(sys.argv)

for arg_position in range (len(sys.argv)):
    print "\n arg:",sys.argv[arg_position]