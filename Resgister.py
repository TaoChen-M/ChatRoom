from database.Database import *
from tkinter import *

class Register:
    def __init__(self):
        self.app=Tk()
        self.app.title("注册界面")

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

        Label(self.frameC, text='昵称').grid(row=0,column=0)
        Label(self.frameC, text='密码').grid(row=1, column=0)

        self.user=Entry(self.frameC)
        self.user.grid(row=0, column=1)
        self.psd=Entry(self.frameC, show='*')
        self.psd.grid(row=1, column=1)

        registerbtn = Button(self.frameB, text='注册', width=8, command=self.reg).grid(row=0, column=1)

        self.app.mainloop()

    # 向数据库中保存用户信息
    def reg(self):
        insertUser(self.user.get(),self.psd.get())

if __name__ == '__main__':
    Register()
