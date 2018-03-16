#-*- coding:utf-8 -*-f
import sys

def calc_tax(Epy_id,tax_rate,tax_kc):
    fax_gl = salary_gl*tax_rate - tax_kc
    return print(Epy_id+':'+format(fax_gl,".2f"))

#参数处理
#遍历所有参数组格式为tim:3333 william:6666
for arg in sys.argv[1:]:
    #获取工号和工资
    Employee_ID = arg.split(':')[0]
    Salary = arg.split(':')[1]
    try:
        #Employee_ID_int =int(Employee_ID)
        Salary_int =int(Salary)
    except:
        print("输入金额错误，请输入整数金额")
#定义应纳税所得额
    salary_gl = Salary_int*0.835-3500

    if int(salary_gl<=0):
        print(Employee_ID+":"+"0")
    elif salary_gl <= 1500 and salary_gl>0:
        calc_tax(Employee_ID,0.03,0)
    elif salary_gl <= 4500 and salary_gl>1500:
        calc_tax(Employee_ID,0.1,105)
    elif salary_gl <= 9000 and salary_gl>4500:
        calc_tax(Employee_ID,0.2,555)
    elif salary_gl <= 35000 and salary_gl>9000:
        calc_tax(Employee_ID,0.25,1005)
    elif salary_gl <= 55000 and salary_gl>35000:
        calc_tax(Employee_ID,0.3,2755)
    elif salary_gl <= 80000 and salary_gl>55000:
        calc_tax(Employee_ID,0.35,5505)
    elif salary_gl > 80000:
        calc_tax(Employee_ID,0.45,13505)