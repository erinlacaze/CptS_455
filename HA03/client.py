import socket
import threading

H_SIZE = 1024
SERVER = "127.0.0.1"
PORT = 11111

def message(cSocket, msg):
    cSocket.send(msg.encode())

def file(cSocket, file):
    with open(file, 'rb') as file1:
        file2 = file1.read(H_SIZE)
        while file2: # there is still stuff in the file to read
            cSocket.send(file2)
            file2 = file1.read(H_SIZE) # read 1024 bytes at a time

userInput = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print(f"** Found connection to server **")

messageThread = threading.Thread(target=message, args=(client, userInput))
messageThread.start()

while True:
    userInput = input()
    if userInput.startswith("exit"): # close client
        break
    elif userInput.startswith("/"): # read file and send output in packets of 1024 bytes
        find = userInput[1:]
        file(client, find)
    else: # send message
        message(client, userInput) 

client.close()
