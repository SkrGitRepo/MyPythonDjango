list1= ['phusics','mathemetics',2341,9876]
list2= [1,2,3,4,5,6,7]

print "\n Before modification",list1
print "Value at index position 2 before insertion: ",list1[2]
list1[2]='chemestry'
print "Value at index position 2 after insertion: ",list1[2]
print "\n After modification",list1

print "lenght of list2",len(list2)
list3 = list1 + list2

print "Element of list3 after concatenation of list1 and list2 :",list3

'''Negative count of list from right'''
print "8th value of list3 from right :",list3[-8]

print "Compares elements of both lists : list1 and list2:: ",cmp(list1,list3)

print "Max value in the list3 :",max(list2)

#print list2[4] 





