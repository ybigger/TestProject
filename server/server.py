import socket
import json

def handleFileRequest(path):
    fileHandler = open(config_data['root_dir'] + path, 'r' )
    return fileHandler.read()

#Get the server configuration
with open("config.json") as json_data:
    config_data = json.load(json_data)
    

#Create the socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = int(config_data['port'])
serverSocket.bind((host, port))

#Listen to incoming connection requests
serverSocket.listen(5)

while True:
    #Establish a connection 
    clientSocket, addr = serverSocket.accept()

    print ("Got a connection from %s" % str(addr))
    requestMessage = clientSocket.recv(1024)
    responseMessage = handleFileRequest(str(requestMessage.decode('ascii')))
    clientSocket.send(responseMessage.encode('ascii'))
    clientSocket.close()