# 判断101-200之间有多少个素数，并输出所有素数

count = 0
for num in range(101,201):
    flag = True
    for n in range(2,num):
        if num % n == 0:
            flag = False
    if flag:
        count+=1
        print(num)
print("个数为：",count)