import socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
print("Sever is Ready")
port=9999
serversocket.bind((host,port))
serversocket.listen(5)
while True:
    clientsocket,addr=serversocket.accept()
    name=clientsocket.recv(1024).decode()
    print(name)
    print("Got a Connection from %s"%str(addr))
    msg='Thank'+'\r\n'
    clientsocket.send(msg.encode("ascii"))

    clientsocket.close()