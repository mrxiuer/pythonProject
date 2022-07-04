# 斐波那契数列。
#
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#
# 在数学上，费波那契数列是以递归的方法来定义：
#
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

def test(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>=2:
        return test(n-1)+test(n-2)
n = int(input("请输入n的值："))
print(test(n))