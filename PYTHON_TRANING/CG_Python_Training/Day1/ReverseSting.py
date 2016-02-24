#reverse the given string
s="GKTCS Innovations Pvt Ltd"
print "Before reverse :",s
print "After reverse :"
print s[len(s):0:-1] #it will not print last char G

print s[len(s)::-1] #this will reverse the whole string
print s[::-1]
print s[::-2]
print s[::2]

#----------------------------------------------------
#converting string to list
StingList = s.split()
print StingList

st ="sumit:kumar:zaheer:abbas"
StingList1 = st.split(':')
print StingList1

#----------------------------------------------------
#converting list to string
listToString = ' '.join(StingList)
print listToString

listToString1 = ':'.join(StingList1)
print listToString1



