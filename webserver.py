# Import socket module
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('port:', serverPort)
#Fill in end

while True:
	#Establish the connection

	print ('Ready to serve...')

	connectionSocket, addr =serverSocket.accept() #Fill in start   #Fill in end

	try:

		message = connectionSocket.recv(1024)  #Fill in start #Fill in end

		filename = message.split()[1]
		
		f = open(filename[1:])

		outputdata =f.read() #Fill in start #Fill in end
		print (outputdata)
		#Send one HTTP header line into socket
		#Fill in start#
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
		#Fill in end

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except IOError:
	#Send response message for file not found
		#Fill in start
		mes = "HTTP/1.1 404 Not Found\r\n\r\n"
		connectionSocket.send(mes.encode())

		mes = "<html><body><h1>404 Not Found!</h1></body></html>\r\n"
		connectionSocket.send(mes.encode())
		#Fill in end

		#Close client socket
		#Fill in start
		connectionSocket.close()
		#Fill in end

serverSocket.close()