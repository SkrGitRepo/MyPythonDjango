# In python, a python is a module
# Modules can have data and fucntions together
#%%writefile NetApp.py

'''This is a NetApp Module'''
version=1.0
def socket1():
    ''' Create a socket by providing IP address and Port No'''
    print 'Connect to server'
def bind():
    '''Bind Address'''
    print 'Bind IP address and Port No'
def listen():
    '''Listen number of clients'''
    print "Listen to toatal number pof client"
def accept():
    '''Listen client one by one'''
    print 'Accept client'
def send():
    '''send data'''
    print 'Welcome to NetApp module'
def recieve():
    print 'You are connected to NetApp'
def end();
    print 'Connection end'
