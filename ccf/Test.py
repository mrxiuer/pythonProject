import bmi1,bmi2
l=float(input("请输入矩形的长："))
w=float(input("请输入矩形的宽："))
r=float(input("请输入圆的半径："))
print("矩形的周长：",bmi1.grith(l,w))
print("矩形的面积：",bmi1.area(l,w))
print("圆的周长：",bmi2.grith(r))
print("圆的面积：",bmi2.area(r))