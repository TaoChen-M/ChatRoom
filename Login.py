# 创建聊天室的登陆界面
import tkinter.messagebox

from ClientGui import cliGUI
from Resgister import Register
from tkinter import *
from database.Database import seaUser


class Login:
    def __init__(self):
        self.app = Tk()
        self.app.title("欢迎使用c-chat")

        # 创建Frame控件
        # logo、账号密码、登录注册
        self.frameT = Frame(width=300, height=100, bg='white')
        self.frameT.grid(row=0, column=0, padx=1, pady=3)

        self.frameC = Frame(width=300, height=200, bg='white')
        self.frameC.grid(row=1, column=0, padx=1, pady=3)

        self.frameB = Frame(width=300, height=200, bg='white')
        self.frameB.grid(row=2, column=0, padx=1, pady=3)

        # 固定布局
        self.frameT.grid_propagate(0)
        # frameC.grid_propagate(0)

        # 输入：标签控件，显示文本 、输入控件
        Label(self.frameC, text="账号").grid(row=0, column=0)
        Label(self.frameC, text="密码").grid(row=1, column=0)

        self.user = Entry(self.frameC)
        self.user.grid(row=0, column=1)
        self.psd = Entry(self.frameC, show='*')
        self.psd.grid(row=1, column=1)

        # Button
        loginbtn = Button(self.frameB, text="登录", width=8, command=self.logincmd).grid(row=0, column=0)
        registerbtn = Button(self.frameB, text='注册', width=8, command=self.register).grid(row=0, column=1)

        self.app.mainloop()

    def register(self):
        self.app.destroy()
        Register()

    def logincmd(self):
        if (seaUser(self.user.get())):
            self.app.destroy()
            cliGUI()
        else:
            tkinter.messagebox.showinfo(title="警告", message="该用户不存在，请注册")
        # serGUI()


if __name__ == '__main__':
    login = Login()
