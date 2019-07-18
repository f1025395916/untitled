import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='cssmoban')

cursor =db.cursor()




#新增
insert_sql = 'insert into tags(tagName) values (%s)'
result  = cursor.executemany(insert_sql,)

db.commit()
print(result)



# 查询
sql = 'select * from tags'
cursor.execute(sql)
print(cursor.fetchall())


cursor.close()
db.close()






