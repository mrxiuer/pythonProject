# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import re
str = input("请输入字符串：")
str_list = list(str)
temp1 = r'[a-zA-Z]'
temp2 = r'[0-9]'
temp3 = r' '
e=0
s=0
k=0
o=0
for n in range(0,len(str_list)):
    if re.match(temp1,str_list[n])!=None:
        e+=1
    elif re.match(temp2,str_list[n])!=None:
        s+=1
    elif re.match(temp3,str_list[n])!=None:
        k+=1
    else:
        o+=1
print("英文字符个数为：",e)
print("数字个数为：",s)
print("空格个数为：",k)
print("其他字符的个数为：",o)