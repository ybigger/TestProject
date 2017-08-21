import socket
import json

#Read the requested file or return an error in case the file is a directory
#or if the path does  not exist
def handleFileRequest(configData, path):
    try:
        fileHandler = open(configData['root_dir'] + path, 'r' )
        return str(fileHandler.read())
    except IOError:
        errorMsg = "Failed to read " + path
        print ("Failed to read " + configData['root_dir'] + path)
        return errorMsg

#Handle the client request
def handleClientConnection(configData, clientSocket, addr):
    print ("Got a connection from %s" % str(addr))
    requestMessage = clientSocket.recv(1024)
    responseMessage = handleFileRequest(configData, requestMessage.decode('ascii'))
    clientSocket.send(responseMessage.encode('ascii'))

#Get the server configuration - config.json - the file is expected in the same
#path as the server.py file and in a JSON format. The file should contain the 
#port number to be used by the server and the root path for the server files.
def getServerConfiguration():
    with open("config.json") as jsonData:
        configData = json.load(jsonData)
    
    return configData

def startTheServerLoop(configData):
    #Create the socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = int(configData['port'])
    serverSocket.bind((host, port))

    #Listen to incoming connection requests
    serverSocket.listen(5)

    while True:
        #Establish a connection 
        clientSocket, addr = serverSocket.accept()

        #Handle the connection
        handleClientConnection(configData, clientSocket, str(addr))

        #Close the connection
        clientSocket.close()

###############################################################################
# Main
###############################################################################

#Read the configuration file
configData = getServerConfiguration()

#Create the server socket and handle requests
startTheServerLoop(configData)
