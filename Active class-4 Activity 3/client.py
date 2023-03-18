from socket import *
serverName = "127.0.0.1"
serverPort = 11500
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input the message --> ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
serverReply, serverAddress = clientSocket.recvfrom(2048)
clientSocket.close()