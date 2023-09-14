import SocketDef
###
host='0.0.0.0'#Nhap connect tu moi Interface
hostname=SocketDef.socket.gethostname()
print("Server:",SocketDef.socket.gethostbyname(hostname))
Server = SocketDef.CreateServer(host,80)
###
while True:
    try:
        Client,request=SocketDef.readHTTPRequest(Server)#Tao Socket Ao cho client va doc. Request
        #print(request)
        if(request):#Phan tich Request
            headers = request.split('\n')#mang? cac dong``
            method=headers[0].split()[0]
            filename=headers[0].split()[1]
            print("Method:",method,"Location:",filename)
            if(method=='GET'):#Tra Loi theo yeu cau
                if(filename=='/'):
                    print("Send Root")
                    SocketDef.SendFileIndex(Client)
                elif(filename=='/404.html'):
                    print("Sent 404!")
                    SocketDef.SendFile404(Client)
                elif(filename=='/home.html'):
                    print("Sent HomePage!")
                    SocketDef.SendHome(Client)
                elif('/download/'in filename):
                    print("Sent File!")
                    SocketDef.SendDownload(Client,filename)
            if(method=='POST'):
                if(SocketDef.CheckPass(request)):
                    print("LOGIN OK!")
                    SocketDef.MoveHome(Client)
                else:
                    print("Refuse LOGIN!!!")    
                    SocketDef.Move404(Client)
        else:
                    print("No Input!!!")
                    SocketDef.Move404(Client)
    ###Close Server
    except KeyboardInterrupt:#Ctrl+C
        break
### 
Server.close()
print("Server Close!!!")