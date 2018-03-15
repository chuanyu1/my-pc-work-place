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
    return print(fax_gl)
if int(salary_gl<=0):
    print("0")
elif salary_gl <= 1500 and salary_gl>0:
    calc_tax(0.03,0)
else:
    print("need more work show answer")