''':key
数据可连接：
将所有对数据库的操作封装成类

数据库操作三步曲：
1、创建连接
2、获取光标
3、执行语句
'''

import mysql.connector as connect
import hashlib
from config import Config

''':param
Host:服务器地址
user:用户名
pass:密码
database:数据库
'''

con = connect.connect(host=Config.host, user=Config.user, password=Config.password, database=Config.database)
cursor = con.cursor()

md5 = hashlib.md5()


def insertUser(name, psd):
    psd = psd + "mysalt"
    md5.update(psd.encode(encoding="utf-8"))
    insert = "insert into " + Config.table + "(name,psd) values(%s,%s)"
    values = [name, md5.hexdigest()]
    cursor.execute(insert, values)
    print(cursor)
    con.commit()


def seaUser(name):
    search = "select 1 from " + Config.table + " where name=" + "'" + name + "'" + " limit 1"
    cursor.execute(search)
    res = cursor.fetchall()
    return res
