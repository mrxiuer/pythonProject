# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

num1 = 1
num2 = 1
for i in range(1,22):
    print('%12ld %12ld' % (num1, num2), end=" ")
    if (i % 3) == 0:
        print('')
    num1 = num1 + num2
    num2 = num1 + num2