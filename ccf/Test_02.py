# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

def get_salary(salary):
    if salary<=10:
        return salary*0.1
    if salary>10 and salary<=20:
        return (salary-10)*0.075+1
    if salary>20 and salary<=40:
        return (salary-20)*0.05+1+0.75
    if salary>40 and salary<=60:
        return (salary-40)*0.03+1+0.75+1
    if salary>60 and salary<=100:
        return (salary-60)*0.015+1+0.75+1+0.6
    if salary>100:
        return (salary-100)*0.01+1+0.75+1+0.6+0.6
salary = float(input("请输入你的工资：(万元)"))
print("你的奖金为：",get_salary(salary))