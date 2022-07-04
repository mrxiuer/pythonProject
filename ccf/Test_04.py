# 输入某年某月某日，判断这一天是这一年的第几天？
import re
ymd = input("请输入年月日:")
ymd_list = re.split(r'[/|年|月|日]',ymd)
day = int(ymd_list[2])
flag = int(ymd_list[1])
month = [31,28,31,30,31,30,31,31,30,31,30,31]
if int(ymd_list[0]) % 4 == 0:
    month[1]=29
    if flag!=1:
        for m in range(0,flag - 1):
            day += month[m]
else:
    month[1] = 28
    if flag != 1:
        for m in range(0, flag - 1):
            day+=month[m]
print("这是今年的第", day, "天")
