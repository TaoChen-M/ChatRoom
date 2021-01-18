from tkinter import *
import time
import socket
import tkinter.messagebox

# 定义套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class cliGUI:
    def __init__(self):
        #创建窗口
        self.app=Tk()
        self.app.title("python聊天客户端窗口")

        #创建frame容器
        self.frameLT=Frame(width=500,height=320,bg='white')
        self.frameLC=Frame(width=500,height=150,bg='white')
        self.frameLB=Frame(width=500,height=30)
        self.frameR=Frame(width=200,height=500)

        #窗口布局
        self.frameLT.grid(row=0,column=0,columnspan=2,padx=1,pady=3)
        self.frameLC.grid(row=1,column=0,columnspan=2,padx=1,pady=3)
        self.frameLB.grid(row=2,column=0,columnspan=2)
        self.frameR.grid(row=0,column=2,rowspan=3,padx=2,pady=3)

        #固定大小 grid_propagate表示不会根据内部容件的大小而改变
        self.frameLT.grid_propagate(0)
        self.frameLC.grid_propagate(0)
        self.frameLB.grid_propagate(0)
        self.frameR.grid_propagate(0)

        self.txtMsgList=Text(self.frameLT)
        #创建tag
        self.txtMsgList.tag_config('greencolor',foreground='#008C00')
        self.txtMsgList.grid()

        self.txtMsg = Text(self.frameLC)
        self.txtMsg.bind("<KeyPress-Up>", self.sendMsgEvent)
        self.txtMsg.grid()

        # 创建button
        btnsend = Button(self.frameLB, text='发送', width=8, command=self.sendMsg)
        btnCancel = Button(self.frameLB, text='取消', width=8, command=self.cancelMsg)
        btncon = Button(self.frameLB, text='连接', width=8, command=self.con)

        btnsend.grid(row=2, column=0)
        btnCancel.grid(row=2, column=1)
        btncon.grid(row=2, column=2)

        # 主事件循环
        self.app.mainloop()

    #python中按键触发事件属于回调函数，需要写在函数内部
    # 连接服务器
    def con(self):
        s.connect(('127.0.0.1',9999))
        return

    # 发送消息

    def sendMsg(self):
        # 显示已经发送的内容
        strMsg = "客户端：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        self.txtMsgList.insert(END, strMsg, 'greencolor')
        msg = self.txtMsg.get('0.0', END)
        self.txtMsgList.insert(END, msg)
        self.txtMsg.delete('0.0', END)

        # 发送消息
        s.send(msg.encode())
        #接收服务器消息
        data=s.recv(1024)
        if len(data)!=0:
            strMsg = "服务端：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
            recmsg = data.decode()
            self.txtMsgList.insert(END, strMsg)
            self.txtMsgList.insert(END,recmsg)

    #绑定事件发送消息
    def sendMsgEvent(self,event):
        if event.keysym=='Up':
            self.sendMsg()

    #取消发送
    def cancelMsg(self):
        self.txtMsg.delete('0.0',END)


if __name__ == '__main__':
    cligui=cliGUI()
