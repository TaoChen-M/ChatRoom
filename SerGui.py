from tkinter import *
import socket
import tkinter.messagebox
import threading
import time

# 定义套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999


class serGUI:
    def __init__(self):
        # 创建窗口
        self.app = Tk()
        self.app.title("python聊天服务端窗口")

        # 创建frame容器
        self.frameLT = Frame(width=500, height=320, bg='white')
        self.frameLC = Frame(width=500, height=150, bg='white')
        self.frameLB = Frame(width=500, height=30)
        self.frameR = Frame(width=200, height=500)

        # 窗口布局
        self.frameLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
        self.frameLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
        self.frameLB.grid(row=2, column=0, columnspan=2)
        self.frameR.grid(row=0, column=2, rowspan=3, padx=2, pady=3)

        # 固定大小 grid_propagate表示不会根据内部容件的大小而改变
        self.frameLT.grid_propagate(0)
        self.frameLC.grid_propagate(0)
        self.frameLB.grid_propagate(0)
        self.frameR.grid_propagate(0)

        self.txtMsgList = Text(self.frameLT)
        # 创建tag
        self.txtMsgList.tag_config('greencolor', foreground='#008C00')
        self.txtMsgList.grid()

        self.txtMsg = Text(self.frameLC)
        self.txtMsg.bind("<KeyPress-Up>", self.sendMsgEvent)
        self.txtMsg.grid()

        # 创建button
        btnsend = Button(self.frameLB, text='发送', width=8, command=self.sendMsg)
        btnCancel = Button(self.frameLB, text='取消', width=8, command=self.cancelMsg)
        btnstart = Button(self.frameLB, text='开启服务器', width=17, command=self.start)

        btnsend.grid(row=2, column=0)
        btnCancel.grid(row=2, column=1)
        btnstart.grid(row=2, column=2)

        # 主事件循环
        self.app.mainloop()

    # python中按键触发事件属于回调函数，需要写在函数内部
    # 开启服务器   使用多线程方法
    def start(self):
        # 绑定IP和端口
        s.bind((host, port))
        s.listen(5)
        print('Servr start at Host:%s,port:%s' % (host, port))
        print("waiting connection...")
        # print("服务器启动")
        # 返回一个元组，新的socket和客户端地址
        self.con, self.addres = s.accept()
        if True:
            tkinter.messagebox.showinfo(title='连接', message='服务器成功开启')

        threadServer = threading.Thread(target=self.threadBody, name='Server')
        threadServer.start()

    def threadBody(self):
        while True:
            data = self.con.recv(1024)
            if len(data) != 0:
                strMsg = "客户端：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
                recmsg = data.decode()
                self.txtMsgList.insert(END, strMsg, 'greencolor')
                self.txtMsgList.insert(END, recmsg)
                time.sleep(1)

    # 发送消息
    def sendMsg(self):
        # 显示已经发送的内容
        strMsg = "服务端：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        self.txtMsgList.insert(END, strMsg, 'greencolor')
        msg = self.txtMsg.get('0.0', END)
        self.txtMsgList.insert(END, msg)
        self.txtMsg.delete('0.0', END)
        # 发送消息
        self.con.send(msg.encode())

    # 绑定事件发送消息
    def sendMsgEvent(self, event):
        if event.keysym == 'Up':
            self.sendMsg()

    # 取消发送
    def cancelMsg(self):
        self.txtMsg.delete('0.0', END)


if __name__ == '__main__':
    sergui = serGUI()
