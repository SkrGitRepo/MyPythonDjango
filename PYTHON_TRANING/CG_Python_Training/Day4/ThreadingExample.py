import threading

'''
def fun():
    print "This is a fun function"

def smile():
    print "Have a smile :-)"

thread = []
threadFun=threading.Thread(target=fun)
threadSmile=threading.Thread(target=smile)

threadFun.run()
threadSmile.run()


thread.append(threadFun)
thread.append(threadSmile)

print thread
'''


#with argument
def fun(*i):
    print "This is a fun function",i

def smile(j):
    print "Have a smile :-)",j

thread = []
threadFun=threading.Thread(target=fun,args=(2,4,6))
threadSmile=threading.Thread(target=smile,args=(3,))

#threadFun.run()
threadFun.start() 
threadSmile.run()


thread.append(threadFun)
thread.append(threadSmile)

print thread

