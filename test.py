def test(string):
    print("调用前：",string)
    string +=string
    print("调用后：",string)
str1 = ['123','jds']
str2 = ('232,','323')
str3 = "323wsw"
test(str1)
test(str2)
test(str3)
# 为什么字符串最终也增加了？