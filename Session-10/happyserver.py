import socket
PORT = 8000
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")
# -- Close the socket
ls.close()

# We are not accepting any connection
# Then it finishes, and is not waiting for connections
