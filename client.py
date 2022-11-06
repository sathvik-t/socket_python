import socket 

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    #format the code to utf-8
    message = msg.encode(FORMAT)

    #get the length of the message
    msg_length = len(message)

    #converts the the length of the file into byte format
    send_length = str(msg_length).encode(FORMAT)

    #makes the string length size of the header with blank spaces 
    send_length += b' ' * (HEADER - len(send_length))

    #sends the length
    client.send(send_length)

    #sends the message
    client.send(message)

send("Hello World!")
send("Hello Everyone!")
send("Hello Tim!")

send(DISCONNECT_MESSAGE)