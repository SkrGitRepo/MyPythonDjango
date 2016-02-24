import socket
s = socket.socket() #create a socket object
host = socket.gethostname()  #get local machine name
port = 60667 #reserve the port for client service
s.connect((host,port)) #bind to the port

s.listen(5) #Now wait for client connection
print s.recv(786)
s.send("Hi This is a client program\n")
s.close()
