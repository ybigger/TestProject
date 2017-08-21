import socket
import json

with open("config.json") as json_data:
    config_data = json.load(json_data)
    print(config_data['port'])

#Create the socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999 # TODO: read the port number from the config.json file
serverSocket.bind((host, port))

#Listen to incoming connection requests
serverSocket.listen(5)

while True:
    #Establish a connection 
    clientSocket, addr = serverSocket.accept()

    print ("Got a connection from %s" % str(addr))
    message = "Hello from the server"
    clientSocket.send(message.encode('ascii'))
    clientSocket.close()