# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
grade = float(input("请输入分数："))

if grade >= 90:
    print("该学生成绩为：A")
elif grade >=60 and grade <89:
    print("该学生成绩为：B")
elif grade < 60:
    print("该学生成绩为：C")