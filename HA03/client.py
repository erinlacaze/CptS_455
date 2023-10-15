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
        while file2:
            cSocket.send(file2)
            file2 = file1.read(H_SIZE)

def main():
    userInput = ""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print(f"** Found connection to server **")

    messageThread = threading.Thread(target=message, args=(client, userInput))
    messageThread.start()

    while True:
        userInput = input()
        if userInput.startswith("/"):
            find = userInput[1:]
            file(client, find)
        elif userInput.startswith("exit"):
            break
        else:
            message(client, userInput)

if __name__ == '__main__':
    main()
