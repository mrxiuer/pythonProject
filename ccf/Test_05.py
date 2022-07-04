# 输入三个整数x,y,z，请把这三个数由小到大输出。
import re

num = input("请输入三个数：（空格隔开）")
num_list = re.split(' ',num)
x=float(num_list[0])
y=float(num_list[1])
z=float(num_list[2])
max = x if x>(y if y>z else z) else (y if y>z else z)
min = x if x<(y if y<z else z) else (y if y<z else z)
print("从小到大排序:",min,x+y+z-max-min,max)