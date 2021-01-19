import mysql.connector

# # 超参数
# Host='localhost'
# User='root'
# Pass='123456'
# Data='chatroom'
# # 创建连接
# con=mysql.connector.connect(host=Host,user=User,password=Pass,database=Data)
# # 获取光标
# cursor=con.cursor()
#
# # 执行语句
# # language="create database chatroom"
# language='select * from user'
# cursor.execute(language)
# res=cursor.fetchall()
# print(cursor)
# print(res)

import time
import threading

def loop():
    print("当前thread名称%s:" % threading.current_thread().name)
    n=0
    while n<=5:
        n+=1
        print('thread %s>>%s' % (threading.current_thread().name,n))
        time.sleep(1)

    print("thread %s is ended" % threading.current_thread().name)

print('thread %s is running' % threading.current_thread().name)

#创建多线程
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s is ended' % threading.current_thread().name)





