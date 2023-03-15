f=open("message.txt",'r+')
f.write('123\n')
for line in f.readlines():
    print(line)