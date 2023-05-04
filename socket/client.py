import socket

host = "127.0.0.1"
port = 50001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input(">>")

while message.lower().strip != "quit":
    if(message != ""):
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Response from server : "+str(data))
    message = input(">> ")
client_socket.close()