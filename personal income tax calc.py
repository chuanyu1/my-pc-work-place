#-*- coding:utf-8 -*-
import sys
#参数处理
try:
    argv_int =int(sys.argv[1])
except:
    print("输入金额错误，请输入整数金额")
#定义应纳税所得额
salary_gl = argv_int-3500
def calc_tax(tax_rate,tax_kc):
    fax_gl = salary_gl*tax_rate - tax_kc
    return print(format(fax_gl,".2f"))
if int(salary_gl<=0):
    print("0")
elif salary_gl <= 1500 and salary_gl>0:
    calc_tax(0.03,0)
elif salary_gl <= 4500 and salary_gl>1500:
    calc_tax(0.1,105)
elif salary_gl <= 9000 and salary_gl>4500:
    calc_tax(0.2,555)
elif salary_gl <= 35000 and salary_gl>9000:
    calc_tax(0.25,1005)
elif salary_gl <= 55000 and salary_gl>35000:
    calc_tax(0.3,2755)
elif salary_gl <= 80000 and salary_gl>55000:
    calc_tax(0.35,5505)
elif salary_gl > 80000:
    calc_tax(0.45,13505)
