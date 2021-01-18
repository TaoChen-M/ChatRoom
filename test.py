import mysql.connector

# 超参数
Host='localhost'
User='root'
Pass='123456'
Data='chatroom'
# 创建连接
con=mysql.connector.connect(host=Host,user=User,password=Pass,database=Data)
# 获取光标
cursor=con.cursor()

# 执行语句
# language="create database chatroom"
language='select * from user'
cursor.execute(language)
res=cursor.fetchall()
print(cursor)
print(res)




