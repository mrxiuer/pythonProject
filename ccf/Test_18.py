# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
import re
str = input("请输入数字和个数：(空格隔开)")
num = re.split(' ',str)
s=0

for i in range(0,int(num[1])):
    s+=int(num[0])*(int(num[1])-i)*pow(10,i)
print(s,"=",num[0],end="")
for q in range(2,int(num[1])+1):
    print("+",num[0]*q,end="")