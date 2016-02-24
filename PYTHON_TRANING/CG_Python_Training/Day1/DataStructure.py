DataStructure = '''
Moutable Data Strcture and Immutable Data structure
Mutable  = List, Dictionary, set
Immutable = String,Tuple,Numbers
'''
L=[]
print (type(L))
Books=[]
Books.append('CBook')
Books.append('CPPBook')

Books.append('JAVABook')
Books.append('DotNetBook')
print (Books)
#print (Books.pop()) # Stack opertation
#print (Books)
#print (Books.pop(0)) # Queue operation
#print (Books)

print (Books.insert(3,'PythonBook'))# LinkedList operation
print (Books.insert(2,'JythonBook'))
print (Books)

Books.remove('CPPBook')
print (Books)

Books.sort()
print ("Sorted Books ::",Books)
Books.reverse()
print ("Reversed Books ::",Books)

print ("Where is JAVABook in index position [",Books.index('JAVABook'),"]" )


BookList = ['Hadoop','DataScince','Bigdata']
Books.extend(BookList);
print ("Extended the Books list:",Books)
Books[0] ='NewBook' # Ovewriting 0th index data - Allowed since mutable
print Books


#swapping a list
[w,x,y,z] = [1,2,3,4]
print "Before Swapping :",w,x,y,z
[w,x,y,z] = [z,y,x,w]
print "After Swapping :",w,x,y,z



