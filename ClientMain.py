import socket

if __name__ == '__main__':  # EntryPoint
    InnerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    InnerSock.connect(("127.0.0.1", 1669))
    input("Client connected")
