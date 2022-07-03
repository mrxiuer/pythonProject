import re

mail = input("请输入你的邮箱地址：")
temp = r'@|\.'
spil = re.split(temp,mail)
print("收件人的用户名:",spil[0],end=" "+"邮件服务器名:"+spil[1])