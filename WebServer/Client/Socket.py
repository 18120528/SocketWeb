import socket
import time

client = socket.socket()
server=input("Nhap Dia Chi Server: ")
client.connect((server, 80))
client.send("GET / http/1.1\n\n".encode())
response = client.recv(1024)
client.close()
print (response.decode())
input()

