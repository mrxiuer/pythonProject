# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
h = 100
s=0
for i in range(1,11):
    s+=h*1.5
    h*=0.5
H = 100*pow(0.5,10)
print("第十次下落时，跳起高度为：",H)
print("总路程为：",s-H)