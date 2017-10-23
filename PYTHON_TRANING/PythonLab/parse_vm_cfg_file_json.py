#!/usr/local/bin/python2.7
# encoding: utf-8
'''
PythonLab.parse_vm_cfg_file_json -- shortdesc

PythonLab.parse_vm_cfg_file_json is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2017 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os

def main():
    print "This is a main method"
    
    vm_cfg_file = "/opt/brms/shared/scripts/brms_vm_cfg_NPRD2_STG.txt"
    
    is_file_exist = check_file_exists(vm_cfg_file)
    
    if is_file_exist == 1: 
        VM_FH = open(vm_cfg_file,'r')
        filelines =  VM_FH.readlines()
        VM_FH.close()
        
        for line in filelines:
            print line,
    
def check_file_exists (filename):
    is_exist = os.path.isfile(filename)
    is_redable = os.access(filename, os.R_OK)
    if is_exist and is_redable:
        return 1
    else:
        return 0
    
     
    
if __name__ == "__main__":
    sys.exit(main())