import socket
import time

#Tao Socket
def CreateServer(host,port):
    Server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if(not Server):
        print("Create Server Fail!!!")
    Server.bind((host,port))
    Server.listen(5)
    return Server
#Tao Socket ao + luu request
def readHTTPRequest(Server):
    Client, address = Server.accept()
    print("Client: ", address," da ket noi toi Server")
    request=Client.recv(1024).decode()
    return Client, request
#Gui Index
def SendFileIndex(Client):
    f = open ('index.html')
    Index = f.read()
    f.close()
    response_head="HTTP/1.1 200 OK\n\n"
    response_head+=Index
    Client.send(response_head.encode())
    Client.close()
#Move 404
def Move404(Client):
    response = '''HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.66.148/404.html\n\n'''
    Client.sendall(response.encode())
    Client.close()
 #Gui 404
def SendFile404(Client):
    f = open ('404.html')
    F404 = f.read()
    f.close()
    response_head="HTTP/1.1 404 Not Found\n\n"
    response_head+=F404
    Client.send(response_head.encode())
    Client.close()   
#MoveHome
def MoveHome(Client):
    response = '''HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.66.148/home.html\n\n'''
    Client.sendall(response.encode())
    Client.close()
#SendHome
def SendHome(Client):
    f = open ('home.html')
    home = f.read()
    f.close()
    response_head="HTTP/1.1 200 OK\n\n"
    response_head+=home
    Client.send(response_head.encode())
    Client.close()
#SendMedia
def SendMedia(Client,MediaName):
    f=open(MediaName,'rb')
    IMG=f.read()
    response_head="HTTP/1.1 200 OK\n\n"
    response_head=bytes(response_head,'utf-8')+IMG
    Client.send(response_head)
    Client.close()
#SendDownload
def SendDownload(Client,type):
    if('ginyu.jpg'in type):
        SendMedia(Client,'download/ginyu.jpg')
    if('ginyu.mp4'in type):
        SendMedia(Client,'download/ginyu.mp4')
    if('ginyu.mp3'in type):
        SendMedia(Client,'download/ginyu.mp3')
#CheckPassWord
def CheckPass(request):
    USER='quang'#Chua link SQL!!!
    PASS='123123'#Query SQL
    form=request.split('\n')
    len_form=len(form)
    username=form[len_form-1].split('&')[0]
    password=form[len_form-1].split('&')[1]
    print(username,password)
    if(username=='Username='+USER and password=='Password='+PASS):
        return True
    else:
        return False