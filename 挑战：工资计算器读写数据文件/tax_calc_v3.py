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


getshebao = config('test.cfg')
sb_table = getshebao.get_shebao_cs()
print(sb_table,type(sb_table))
getshebao = config('user.csv')
employe_table = getshebao.get_shebao_cs()
print(employe_table)

for key,value in employe_table.items():
    need_sb=employee(value).calculate_shebao()
    print(key+"需缴纳社保："+str(need_sb))
