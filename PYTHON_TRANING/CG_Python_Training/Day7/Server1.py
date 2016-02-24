import socket
s = socket.socket() #create a socket object
host = socket.gethostname()  #get local machine name
port = 60667 #reserve the port for client service
s.bind((host,port)) #bind to the port

s.listen(5) #Now wait for client connection
while True:
    c,addrs = s.accept() #Establish connection with client
    print "Got connection request from",addrs
    c.send('This is server communication with client')
    c.send('Thank you for connecting')
    c.close() #closed the connection
