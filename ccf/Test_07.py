# 将一个列表的数据复制到另一个列表中。

import re
str = input("请输入字符串：(空格隔开)")
str_list = re.split(" ",str)
list = str_list[:]
print(list)