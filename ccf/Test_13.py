# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            if pow(x,3)+pow(y,3)+pow(z,3) == 100*x+10*y+z:
                print(x,y,z)