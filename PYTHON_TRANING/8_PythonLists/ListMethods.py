'''
Created on Oct 29, 2015

@author: sumkuma2
'''

if __name__ == '__main__':
    pass


aList = [123, 'xyz', 'zara', 'abc'];
print "List before Append: ", aList
aList.append( 2009 );
print "Updated List after Append: ", aList

atuple = ('sumit','kuamr')
aList.append( atuple )
print "Updated List after Appending a tuple: ", aList

adict = {'name':'sumit','address':'Bangalore'}
aList.append( adict )
print "Updated List after Appending a dictionary: ", aList


'''Iterating through the various type of list element'''
for x in aList:
    #print "Each elemnt in alist :",x
    if (type(x) == tuple):
        #print "Tuble found in alist at index %d => %d"%(list.index(tuple),x)
        for t in x:
            print "Element of Tuple :",t
    elif (type(x) == dict):
        print "Distionary found in alist:",x
    elif (type(x) == str):
        print "String found in alist:",x
        
        
    
print ":: Inserting a tuple in specific position of the aList ::"
atuple2 =('Aparna','Kumari')
print ":: aTuple2::",atuple2
aList.insert(2, atuple2)
print ":: Updated aList after inserting new atuple2 in the list at index position 2:\n",aList

print ":: Count of 'zara' in the given aList ::",aList.count('zara')

#aList2 = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print ":: Reversed element of aList :: \n",aList

aList.sort(cmp=None, key=None, reverse=False)
print ":: Sorted element of aList :: \n",aList




aList2 = [123, 'xyz', 'zara', 'abc'];
print ":: aList2 before POP :\n",aList2
print "A List : ", aList2.pop()
print "B List : ", aList2.pop(2)
print "aList2 after POP :\n",aList2





