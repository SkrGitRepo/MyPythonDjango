import glob
#dir(glob)

L=glob.glob("*.txt") #for current directory search, dir_path can be given
print L
L1=glob.iglob("C:\Python_Training\Day2\File*.py") #with ignore case of file name
print list(L1)
print len(L)

#import filecmp
#import zipfile,import tarfile
#import pickle , cPickle
#import #shelve
#import json # in the jason : javascript object data 
