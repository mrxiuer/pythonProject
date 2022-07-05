# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

list = list()
print("完数：")
for n in range(1,1001):
    s=0
    if n== 1:
        print('1')
    else:
        for y in range(1,n):
            if n%y==0:
                s+=y
    if s==n:
        print(s)