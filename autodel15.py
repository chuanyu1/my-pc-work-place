#-*- coding:utf-8 -*-
import os
import time
import datetime

try:
    ff = open("autodel15.ini","r")
    lj1 = ff.readline().replace("\n","\\")      #读取第1行，即为第一个需要处理文件夹的路径
    lj2 = ff.readline().replace("\n","\\")
    gDay1 = int(ff.readline().replace("\n","")) #读取第3行，作为第一个需要处理文件夹删除文件天数
    gDay2 = int(ff.readline().replace("\n",""))
finally:
    ff.close()

class clean:
    def __init__(self, file_url,cDay):
        self.file_url = file_url
        self.cDay = cDay
    def rename1(self):
        f = list(os.listdir(self.file_url))
        print("%s\n 开始修改文件名添加后缀...." % self.file_url)
        for i in range(len(f)):
          #  filedate = os.path.getmtime(self.file_url + f[i])  getmtime 是获取最后修改时间，ctime在win下是creating time,
            if not ".bak" in f[i]:
                oldname = self.file_url + f[i]
                #newfile = f[i].replace('.txt','.txt.bak')
                add1 = time.strftime("%m-%d")
                newfile = f[i] + "_" + add1+ ".bak"
                newname = self.file_url + newfile
                os.rename(oldname,newname,)
                print(u"已修改文件： %s ====> %s" %  (f[i],newfile))
    def delfile(self):
        f =  list(os.listdir(self.file_url))
        print("%s\n  开始清理过期文件...." % self.file_url)
        for i in range(len(f)):
            filedate = os.path.getmtime(self.file_url + f[i])
            time1 = datetime.datetime.fromtimestamp(filedate).strftime('%Y-%m-%d')
            date1 = time.time()
            num1 =(date1 - filedate)/60/60/24
            if num1 >= self.cDay:
                try:
                    os.remove(self.file_url + f[i])
                    print(u"已删除%s天前文件：%s ： %s" %  (self.cDay,time1, f[i]))
                except Exception as e:
                        print(e)
        else:
            print("......")


file1 = clean(lj1,gDay1)
file1.delfile()
file1.rename1()
print(u'过期文件已清理完毕：%s\n' % file1.file_url)

file2 = clean(lj2,gDay2)
file2.delfile()
file2.rename1()
print(u'过期文件已清理完毕：%s\n' % file1.file_url)