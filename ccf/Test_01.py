# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

count = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if x != y and x!=z and y!=z:
                count+=1
                print(x,y,z)
print("个数为：",count)