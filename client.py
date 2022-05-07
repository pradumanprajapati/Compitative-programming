import time ,socket,sys

print("\nWelcome to Chat Room\n")
print("Initialising........\n")
time.sleep(1)
s=socket.socket()
shost=socket.gethostname()
ip=socket.gethostbyname(shost)
print(shost,"(",ip,")\n")
host=input(str("Enter the server Address: "))
name=input(str("\nEnter your name: "))
port=12345
print("\nTrying to connect to ", host,"(",port,")\n")
time.sleep(1)
s.connect((host,port))
print("connected.....\n")

s.send(name.encode())
s_name=s.recv(1024)
s_name=s_name.decode()
print(s_name,'has joined the chat room \nEnter the [e] to exit chat room\n')

while True:
    massage=s.recv(1024)
    massage=massage.decode()
    print(s_name,":",massage)
    massage=input(str("me: "))
    if massage=='[e]':
       massage="left chat room!"
       s.send(massage.encode())
       print("\n")
       break
    s.send(massage.encode())