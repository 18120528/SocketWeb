import socket
import time

client = socket.socket()
server=input("Nhap Dia Chi Server: ")
client.connect((server, 81))
client.send("I am CLIENT\n".encode())
response = client.recv(1024)
client.close()
print (response.decode())

