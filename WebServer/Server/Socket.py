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
    response = '''HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.66.148:8080/404.html\n\n'''
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
#MoveInfo
def MoveInfo(Client):
    response = '''HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.66.148:8080/info.html\n\n'''
    Client.sendall(response.encode())
    Client.close()
#SendInfo
def SendInfo(Client):
    f = open ('info.html')
    F404 = f.read()
    f.close()
    response_head="HTTP/1.1 404 Not Found\n\n"
    response_head+=F404
    Client.send(response_head.encode())
    Client.close()
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
###
host='0.0.0.0'#Nhap connect tu moi Interface
hostname=socket.gethostname()
print(socket.gethostbyname(hostname))
Server = CreateServer(host,8080)
while True:
    try:
        Client,request=readHTTPRequest(Server)
        #print(request)
        if(request):#Phan tich Request
            headers = request.split('\n')
            method=headers[0].split()[0]
            filename=headers[0].split()[1]
            print("Method:",method,"Location:",filename)
            if(method=='GET'):#Tra Loi theo yeu cau
                if(filename=='/'):
                    print("Send Root")
                    SendFileIndex(Client)
                elif(filename=='/404.html'):
                    print("Sent 404!")
                    SendFile404(Client)               
            if(method=='POST'):
                if(CheckPass(request)):
                    print("LOGIN OK!")
                    #Client.sendall(response.encode())
                else:
                    print("Refuse LOGIN!!!")    
                    Move404(Client)      
    except KeyboardInterrupt:#Ctrl+C
        break
    
Server.close()
print("Server Close!!!")