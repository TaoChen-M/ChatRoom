### 项目介绍

使用python中Socket编程方法和多线程，并结合Mysql数据库，实现聊天室的注册、登录，以及单对单聊天。

### 环境配置

Python=3.6.10

Mysql=8.0.22.0

### 相关知识点

- Socket编程：https://gist.github.com/kevinkindom/108ffd675cb9253f8f71
- 多线程和多进程：https://muyuuuu.github.io/2020/03/16/multi-process-thread/

### 数据库设计

![mysql](photo/mysql.png)

### Release-2021/1/18

1、已经实现用户登录校验，去数据库中匹配相关主键，如果昵称存在则直接转到聊天界面，如果不存在则提示注册
2、注册界面正在开发，函数调用有一定问题
3、可以单线程进行聊天，监听的IP地址为‘127.0.0.1’

### Release-2021/1/19

1、单对单聊天时使用多线程技术，不必在发送消息后一直阻塞等待对方发来消息。

2、已经成功实现各个界面之间的跳转。

3、结果展示![result](photo/chat.png)

