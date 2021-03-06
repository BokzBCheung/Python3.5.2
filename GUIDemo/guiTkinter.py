#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-04-12 09:11
# @Author  : BokzBCheung
# @Site    : www.github.com/BokzBCheung
# @File    : guiTkinter.py
# @Software: PyCharm
# @license : Copyright(C),BokzBCheung
# @Contact : BokzBCheung@gmail.com

# 导入gui程序包
from tkinter import *
from tkinter import messagebox
import sys
sys.path.append('E:\\BokzBCheung\\Python\\PycharmProjects\\PythonLearning\\MysqlDemo')
from MysqlDemo.mysqlConnector import getUserName

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 添加label
        self.helloLabel = Label(self,text='Please enter your name：',bg='#34b4f4')
        self.helloLabel.pack(pady=10)

        # 添加姓名输入框
        self.nameInput = Entry(self)
        self.nameInput.pack()

        # 添加密码输入框
        self.pwdInput = Entry(self)
        self.pwdInput.pack()

        # 添加确认按钮
        self.confirmButton = Button(self,text='Confirm',command=self.confirm)
        self.confirmButton.pack(padx=18,pady=10,side=LEFT)

        # 添加退出按钮
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack(padx=18,pady=10,side=LEFT)

    def confirm(self):
        name = self.nameInput.get()
        pwd = self.pwdInput.get()

        if getUserName(name) == 1:
            messagebox.showinfo(title='Succ',message='Hello，'+name+'登录成功!')
        else:
            messagebox.showinfo(title="Fail",message='Sorry，登录失败!')


# 实例化派生类Application
app = Application()

# 设置窗口标题
app.master.title('Welcom to use this testdemo!')

# 设置窗口大小
app.master.geometry('600x400')

# 设置窗体是否可以拉伸
app.master.resizable(width=True,height=True)

# 主消息循环
app.mainloop()
