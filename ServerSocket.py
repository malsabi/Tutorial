import socket  # Predefined libraries


class ServerSocket:
    def __init__(self):  # Constructor (Initialization).
        self.__InnerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IsListening = False
        print("__init__ Executed")

    def listen(self, port):
        if not self.IsListening:
            self.__InnerSocket.bind(("0.0.0.0", port))  # 127.0.0.1 (Loop back address)
            self.__InnerSocket.listen()  # Starts the TCP server listener
            self.IsListening = True  # Sets IsListening to true
        else:
            print("Server is already listening on port: " + port)

    def acceptor(self):
        print("Starting server acceptor")
        while self.IsListening:
            clientSock, clientAddress = self.__InnerSocket.accept()
            print("Client [" + str(clientAddress) + "] Accepted successfully")
        print("Finished server acceptor")

    def shutdown(self):
        if self.IsListening:
            self.IsListening = False
            self.__InnerSocket.shutdown(socket.SHUT_RDWR)
            self.__InnerSocket.close()
