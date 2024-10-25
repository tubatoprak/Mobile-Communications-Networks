from socket import *
msg = "\r\n I love computer networks!" 
endmsg = "\r\n. \r\n" 
mailServer = "localhost"
mailPort = 50
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
#Fill in end
recv = clientSocket.recv(1024)
print (recv) 
if recv[:3] != "220":
    print ("220 reply not received from server.") 

heloCommand = "HELO Alice\r\n" 
clientSocket.send(heloCommand) 
recv1 = clientSocket.recv(1024) 
print (recv1) 
if recv1[:3] != "250": 
    print ("250 reply not received from server.")

clientSocket.send("Mail FROM: <ttoprak@gtu.edu.tr>\r\n")
recv1 = clientSocket.recv(1024)
print (recv1) 
if recv1[:3] != "250": 
    print ("250 reply not received from server.")                       

clientSocket.send("RCPT TO: <tbtoprakk@gmail.com> \r\n")
recv1 = clientSocket.recv(1024)
print (recv1) 
if recv1[:3] != "250": 
    print ("250 reply not received from server.")

clientSocket.send("DATA\r\n") 
recv1 = clientSocket.recv(1024)
print (recv1) 
if recv1[:3] != "354":
    print ("250 reply not received from server.")
clientSocket.send("\r\n")
clientSocket.send("deneme\r\n")

clientSocket.send(".\r\n")
recv1 = clientSocket.recv(1024) 
print (recv1) 
if recv1[:3] != "250": 
    print ("250 reply not received from server.") 

clientSocket.send("QUIT\r\n") 
clientSocket.close() 
pass
