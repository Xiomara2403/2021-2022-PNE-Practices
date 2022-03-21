import socket
import termcolor  # pip install termcolor, or colorama

# SERVER IP, PORT
PORT = 8080
IP = "127.0.0.1"  # url of the computer, or ip 127.0.0.1

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
termcolor.cprint(msg.decode("utf-8"), "magenta")  # colorama.init()  print(colorama. Fore.RED + msg.decode("utf-8"))

# Closing the socket
s.close()

# If we use termcolor, we see it using run bottom. Colorama shows the colour in the terminal
