#Import socket library
from socket import *

#Assign host and port
host = "94.142.241.111"
port = 23

#Initialize socket and connect to host
test_socket = socket(AF_INET, SOCK_STREAM, 0)
test_socket.connect((host,port))

#Store the received data and print
while True:
    data = test_socket.recv(1024)
    print(data)

test_socket.close()
