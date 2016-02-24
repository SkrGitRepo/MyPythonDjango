#Assignemt2
# Using the list comrehansion display character (Char,Upchar) from a given word list => e.g:(a,A)
words=['abc','def','gh1','jkl']

#getting words and then char from single word
print [(ch,ch.upper()) for word in words for ch in word ]

#------------OUTPUT-----------------------
'''
[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G'), ('h', 'H'), ('1', '1'), ('j', 'J'), ('k', 'K'), ('l', 'L')]
'''


#getting words and then char from single word
print [(ch,ch.upper()) for word in words for ch in word
        if ch!='a'
       ],
