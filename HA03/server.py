import socket
import threading

H_SIZE = 1024
SERVER = '127.0.0.1'
PORT = 11111

def message(cSocket):
    while True:
        try:
            msg = cSocket.recv(H_SIZE)
            if not msg:
                break
            print(msg.decode())
        except Exception as x:
            print(f"Exception error: {x}")
            break

def file(cSocket, file):
    with open(file, 'wb') as file1:
        while True:
            file2 = cSocket.recv(H_SIZE)
            if not file2:
                break
            file1.write(file2)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))
server.listen()

print(f"** Listening on {SERVER}:{PORT} **")

while True:
    client, addr = server.accept()
    print(f"** Found connection from {addr[0]}:{addr[1]} **")
    clientThread = threading.Thread(target=message, args=(client,))
    clientThread.start()
    
