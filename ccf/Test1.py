from socket import *
from time import ctime
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    tcpClisock,addr = tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data = tcpClisock.recv(BUFSIZ).decode(encoding='utf-8')
        if not data:
            break
        data = '[%s] %s'%(ctime(),data)
        print(data)
        tcpClisock.send(data.encode(encoding='utf-8'))
    tcpClisock.close()