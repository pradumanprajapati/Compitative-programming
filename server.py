import time,socket,sys

print("\nWelcome to Chat Room\n")
print("initiallsing_______\n")
time.sleep(1)

s=socket.socket()
host=socket.gethostname()
ip=socket.gethostbyname(host)
port=12345
s.bind((host,port))
print(host,'(',ip,')\n')
name=input(str('Enter th your Name:'))

s.listen(1)
print("\nWaiting for incoming connections______\n")
conn,addr=s.accept()
print('Received connection from',addr[0],'(',addr[1],')\n')
s_name=conn.recv(1024)
s_name=s_name.decode()
print(s_name,"has connection to the chat room\n Enter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    massage=input(str("me: "))
    if massage=='[e]':
        massage= "left chat room!"
        conn.send(massage.encode())
        print("\n")
        break
    conn.send(massage.encode())
    massage=conn.recv(1024)
    massage=massage.decode()
    print(s_name,":",massage)