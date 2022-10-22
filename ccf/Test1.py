from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection>>>")
    tcpClisock, addr = tcpSerSock.accept()
    print("connected success!")

    while True:
        data = tcpClisock.recv(BUFSIZ).decode(encoding='utf-8')
        if not data:
            break
        data = "[%s] %s" % (ctime(), data)
        print(data)
        data = input("请输入你要发送的讯息:").encode(encoding='utf-8')
        print("waiting for message>>>")
        tcpClisock.send(data)

    tcpClisock.close()
