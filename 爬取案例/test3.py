# -*- coding: utf-8 -*-




dic_test = {'name':'小帅','age':18}

print(dic_test["name"])
for k,v in dic_test.items():

    print(k+":"+str(v))
for k in dic_test.keys():
    print(k)


dic_txl = {"zhangsan":"13806659465","xiaoshuai":"18660653953","xiaoming":"13306464505"}

while(True):
    str_name = input("输入要查找人姓名(可模糊查询)：")
    for k,v in dic_txl.items():
        if k.startswith(str_name):
            print(k+':'+v)
    i = input("是否继续查找(y/n?):")
    if i =='n':
        break

