#import exceptions #its a module under which All Exceptions class are defined
#print dir(exceptions)
#print help(exceptions)

# User defined Exceptions class

class ShortInput(Exception):
    '''Short input exception class '''
    def __init__(self,length,atleast):
        '''Initializing ShortInput Calss'''
        self.length=length #object variable
        self.atleast=atleast
        print "Short Input Exception:, Input Should be minimum 6byte"

#obj = ShortInput(3,9)


try:
    s=raw_input("Enter some data:")
    if len(s) <6:
        raise ShortInput(len(s),6)
except ShortInput,sie:
    print "You entered %s bytes expected  %s bytes"%(sie.length,sie.atleast)
else:
    print "Your data is %s"%s    



