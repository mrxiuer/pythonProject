# 暂停一秒输出。
# 原题是暂停一秒，这里我为了更加直观，选择暂停10秒

import time
str_in = input("请输入你的字符串:")
time1 = time.time()
time2 = time.time()
while (time2 - time1) <10:
    time2 = time.time()
print(str_in)

# 或者选择另一种方法：
# import time
# str_in = input("请输入你的字符串：")
# time.sleep(10)
# print(str_in)