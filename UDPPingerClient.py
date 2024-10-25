from socket import *
from time import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddr = ('localhost', 12000)
clientSocket.settimeout(1)
ping = 0
while (ping < 10):

	try:
		start = time()
		message = "PING " + str(ping+1)
		clientSocket.sendto(message.encode(), serverAddr)
		print("Ping Message: " + message)
		data, server = clientSocket.recvfrom(1024)
		print("Response Message: " + data.decode())
		end = time()
		elapsed = end - start
		print("RTT: "+ str(elapsed) + " seconds\n")

	except timeout:
		print("Request Time Out\n")

	ping += 1
clientSocket.close()