#-*- coding:utf-8 -*-f
import sys

class config:
    def __init__(self,shebao_file):
        self.shebao_file = shebao_file
    def get_shebao_cs(self):
        with open(self.shebao_file) as f:
            shebao_cs={}
            i=0
            for x in f:
                #获取社保相关系数配置信息
                if "=" in x:
                    dic_key = x.split('=')[0].strip().strip('\n')
                    try:
                        dic_value =float(x.split('=')[1].strip().strip('\n'))
                    except:
                        #print("请检查社保基数配置文件格式是否正确")
                        raise ValueError("请输入正确的社保参数值")
                    shebao_cs[dic_key] = dic_value
                #获取员工配置信息用
                if "," in x:
                    dic_key = x.split(',')[0].strip().strip('\n')
                    try:
                        dic_value =int(x.split(',')[1].strip().strip('\n'))
                    except:
                        #print("请检查社保基数配置文件格式是否正确")
                        raise ValueError("请输入正确的社保参数值")
                    shebao_cs[dic_key] = dic_value
        return shebao_cs

class employee:
    def __init__(self,employee_1):
        self.employee = employee_1

    def calculate_shebao(self):
        JiShuL = sb_table.get('JiShuL')
        JiShuH = sb_table.get('JiShuH')
        YangLao = sb_table.get('YangLao')
        YiLiao = sb_table.get('YiLiao')
        ShiYe = sb_table.get('ShiYe')
        GongShang = sb_table.get('GongShang')
        ShengYu = sb_table.get('ShengYu')
        GongJiJin = sb_table.get('GongJiJin')
        if self.employee <JiShuL:
            sb = JiShuL*(YangLao+YiLiao+ShiYe+GongShang+ShengYu+GongJiJin)
        elif self.employee >JiShuH:
            sb = JiShuH*(YangLao+YiLiao+ShiYe+GongShang+ShengYu+GongJiJin)
        elif self.employee>=JiShuL and self.employee<=JiShuH:
            sb = self.employee*(YangLao+YiLiao+ShiYe+GongShang+ShengYu+GongJiJin)
        return sb
    def calculate_geshui(self):
        ylssde = self.employee-need_sb-3500
        if ylssde < 0:
            ylssde =0
            tax_rate = 0
            tax_kouchu = 0
          #  print(ylssde,self.employee)
        if ylssde <= 1500 and ylssde>=0:
            tax_rate = 0.03
            tax_kouchu = 0
        elif ylssde >1500 and ylssde<=4500:
            tax_rate = 0.1
            tax_kouchu = 105
        elif ylssde >4500 and ylssde<=9000:
            tax_rate = 0.2
            tax_kouchu = 555
        elif ylssde >9000 and ylssde<=35000:
            tax_rate = 0.25
            tax_kouchu = 1005
        elif ylssde >35000 and ylssde<=55000:
            tax_rate = 0.3
            tax_kouchu = 2755
        elif ylssde >55000 and ylssde<=80000:
            tax_rate = 0.35
            tax_kouchu = 5505
        elif ylssde >80000:
            tax_rate = 0.45
            tax_kouchu = 13505
        tx =ylssde*tax_rate-tax_kouchu
        return tx

args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userfile = args[index+1]
index = args.index('-o')
outfile = args[index+1]


getshebao = config(configfile)
sb_table = getshebao.get_shebao_cs()
print(sb_table,type(sb_table))
getshebao = config(userfile)
employe_table = getshebao.get_shebao_cs()
print(employe_table)

for key,value in employe_table.items():
    need_sb=employee(value).calculate_shebao()
    need_tx=employee(value).calculate_geshui()
    little_salary = value- need_sb - need_tx
    out = key+','+str(value)+','+str(format(need_sb,".2f"))+','+str(format(need_tx,".2f"))+','+str(format(little_salary,".2f"))+'\n'
    print(key+','+str(value)+','+str(format(need_sb,".2f"))+','+str(format(need_tx,".2f"))+','+str(format(little_salary,".2f")))
    with open(outfile,'a') as f:
        f.write(out)


  #  print(key+"需缴纳个人所得税："+str(need_tx))
