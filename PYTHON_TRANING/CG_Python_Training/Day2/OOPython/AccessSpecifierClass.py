class Acc:
    __ano=624001053989 #private data
    ifsc='citi001748' #publicdata

    def __Accinfo(self): #this private method
        print "My account information is :%d"%Acc.__ano
    def branchinfo(self):
        print "My Bracnch IFSC code is %s"%Acc.ifsc


obj = Acc()
print obj.ifsc
#print obj.__ano
obj.branchinfo()
dir(obj)
print obj._Acc__Accinfo() #to print private method we have to follow this

class Bcc(Acc):
    __ano=7865430899 #Private data
    ifsc='citi7800' #public data

    def __Accinfo(self): #this private method
        print "My BCC account information is :%d"%Bcc.__ano
    def branchinfo(self):
        print "My Bracnch IFSC code is %s"%Bcc.ifsc
    
b_obj = Bcc()
print b_obj.ifsc
print b_obj.branchinfo()
dir(b_obj)


print Acc._Acc__ano
b_obj._Acc__Accinfo
b_obj._Bcc__Accinfo
print b_obj._Bcc__ano

