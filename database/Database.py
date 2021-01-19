''':key
数据可连接：
将所有对数据库的操作封装成类

数据库操作三步曲：
1、创建连接
2、获取光标
3、执行语句
'''

import mysql.connector as connect

''':param
Host:服务器地址
user:用户名
pass:密码
database:数据库
'''
Host = 'localhost'
User = 'root'
Password = '123456'
Database = 'chatroom'
Table = 'user'
con = connect.connect(host=Host, user=User, password=Password, database=Database)
cursor = con.cursor()


def insertUser(name, psd):
    insert = "insert into " + Table + "(name,psd) values(%s,%s)"
    values = [name, psd]
    cursor.execute(insert, values)
    print(cursor)
    con.commit()

def seaUser(name):
    search = "select 1 from " + Table + " where name=" + "'" + name + "'" + " limit 1"
    cursor.execute(search)
    res = cursor.fetchall()
    return res
