import socket
import threading 

HEADER = 64
PORT = 5050
#SERVER = "192.168.1.5"
#another way to start a server locally is to use this for different devices
#gethostbyname gets the ip address of the hostname
#gethostname gets the hostname
SERVER = socket.gethostbyname(socket.gethostname())

#to connect to the localhost
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"

#making a new socket, arguments are the type of address and idk
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        #how long the message is 
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            #convert it into integer
            msg_length = int(msg_length)

            #actual message
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting....")
start()