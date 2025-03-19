# UDP Server

from socket import *
serverPort = 13000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve on port: ", serverPort)

expected_sequence_number = 10001

while True:
    # read client's message and remember client's address (IP and port)
    message, clientAddress = serverSocket.recvfrom(1465)
    decoded_message = message.decode()
    sequence_str, payload = decoded_message.split(';')
    sequence_number = int(sequence_str)

    if sequence_number != expected_sequence_number:
        print(f"Out of order packet received: {sequence_number} (expected: {expected_sequence_number})")

    expected_sequence_number = sequence_number + 1

    # Print message and client address
    print(f"From: {clientAddress}")

    # send back modified sentence to client using remembered address
    serverSocket.sendto(message, clientAddress)
