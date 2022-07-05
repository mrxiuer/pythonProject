# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 在python2中， '整数 / 整数 = 整数'，以上面的 100 / 2 就会等于 50， 并且是整数。
# 而在python3中， ‘整数/整数 = 浮点数’， 也就是100 / 2 = 50.0， 不过，使用 '//'就可以达到原python2中'/'的效果。

num = int(input("请输入数字："))
n = num
list1 = list()

while n !=1:
    for x in range(2,n+1):
        if n%x==0:
            n//=x
            list1.append(x)
            break
print(num,"=",end="")
for l in range(0, len(list1)-1):
    print(list1[l],end="*")
print(list1[len(list1)-1])