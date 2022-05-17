from ServerSocket import ServerSocket

if __name__ == '__main__':  # EntryPoint
    sock = ServerSocket()  # It will call directly the Constructor (Initialization)
    print("IsListening: " + str(sock.IsListening))
    sock.listen(1669)
    print("IsListening: " + str(sock.IsListening))
    sock.acceptor()
