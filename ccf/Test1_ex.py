from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpClisock = socket(AF_INET,SOCK_STREAM)
tcpClisock.connect(ADDR)
while True:
    data = input("请输入讯息：").encode(encoding="utf-8")
    if not data:
        break
    tcpClisock.send(data)
    print("waiting for message...")
    data = tcpClisock.recv(BUFSIZ).decode(encoding='utf-8')
    if not data:
        break
    print("message has got!")
    print("[%s] %s"%(ctime(),data))
