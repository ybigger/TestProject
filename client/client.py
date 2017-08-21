import socket
import tkinter
import re

class clientBrowser(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        #Setup the browser address area
        self.addressVariable = tkinter.StringVar()
        self.addressBar = tkinter.Entry(self, textvariable=self.addressVariable)
        self.addressBar.grid(column=0,row=0,sticky='EW')
        self.addressBar.bind("<Return>", self.goToAddressThroughEnter)
        self.addressVariable.set(u"<server ip>:<port>/<path to file>")

        #Setup the go button
        self.goButton = tkinter.Button(self,text=u"GO", command=self.goToAddress)
        self.goButton.grid(column=1,row=0)

        #Setup the display area
        self.labelVariable = tkinter.StringVar()
        self.displayArea = tkinter.Label(self, textvariable=self.labelVariable,
         anchor="w",fg="black",bg="gray")
        self.displayArea.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.update()
        self.geometry(self.geometry())  
        

    def goToAddress(self):
        self.theSocketPart()

    def goToAddressThroughEnter(self, event):
        self.theSocketPart()

    def theSocketPart(self):
        #Create the client socket
        address = self.addressVariable.get()
        host = re.split(r':', address)[0]
        #host = socket.gethostname()
        address = re.split(r':', address)[1]
        arr = re.split(r'/', address)
        port = arr[0]
        path = ""
        for i in range(1, len(arr)):
            path += "/"
            path += arr[i]

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
        clientSocket.connect((host, int(port)))
        clientSocket.send(path.encode('ascii')) # TODO: read the file name from the UI

        serverMessage = ""
        while True:
            data = clientSocket.recv(1024)    
            if not data:
                break
            else:
                serverMessage += data.decode('ascii')

        self.labelVariable.set(serverMessage)
        clientSocket.close()

if __name__ == "__main__":
    browser = clientBrowser(None)
    browser.title('Browser')
    browser.mainloop()





