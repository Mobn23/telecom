# HTTP Client

from socket import *
# serverName = 'hostname'
serverName = "www.ingonline.nu"
serverPort = 80

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

request_line = "GET /tictactoe/index.php?board=xoxoeoeex HTTP/1.1\r\n"
headers = (
    "Host: www.ingonline.nu\r\n"
    "Connection: close\r\n"
    "\r\n"
)
# If we didn't format it this way with each component on its own line (\r\n), the server would return an error because it couldn't understand your request.
http_request = request_line + headers
# print("HTTP request: ", http_request)
clientSocket.send(http_request.encode())

response = b"" #display the response from the server in bytes
while True:
    chunk = clientSocket.recv(1024)
    if not chunk:
        break
    response += chunk
print("From server", response.decode())

clientSocket.close() #close the connection after receiving the response cause it's already open in TCP protocol so we need to close it after receiving the response.
