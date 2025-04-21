# TCP Receiver

from socket import *
serverPort = 12000 

# create TCP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_STREAM )
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # Enable the server to accept connections (1 queued connection)

print ("The TCP server is ready to receive on port: ", serverPort)

while True:
    # Accept a new connection
    connectionSocket, clientAddress = serverSocket.accept()
    print(f"Connection established with {clientAddress}")

    try:
        while True:
            message = connectionSocket.recv(1465)
            if not message:  # Client closed connection
                break

            # print(f"From {clientAddress}: {message.decode()}")

            # Send back the same message to client
            connectionSocket.send(message)

    except ConnectionResetError:
        print(f"Client {clientAddress} disconnected abruptly")
    finally:
        connectionSocket.close()
        print(f"Connection with {clientAddress} closed")
