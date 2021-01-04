from tkinter import *  
from view import *   # 菜单栏对应的各个子页面

class MainPage(object):

    def __init__(self, master=None):  
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (500, 590))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.luruPage = LuruFrame(self.root)  # 创建不同Frame
        self.deletestuPage = DeletestuFrame(self.root)
        self.inputPage = InputFrame(self.root)
        self.deletePage = DeleteFrame(self.root)
        self.modifyPage = ModifyFrame(self.root)
        self.queryPage = QueryFrame(self.root)
        self.checkPage = CheckFrame(self.root)
        self.luruPage.pack()  # 默认显示数据录入界面,将小部件放置到主窗口中
        menubar = Menu(self.root)
        menubar.add_command(label='录入学生', command=self.lurustu)
        menubar.add_command(label='删除学生', command=self.deletestu)
        menubar.add_command(label='更改信息', command=self.modifyData)
        menubar.add_command(label='查询学生', command=self.checkData)
        menubar.add_command(label='录入成绩', command=self.inputData)
        menubar.add_command(label='删除成绩', command=self.deleteData)
        menubar.add_command(label='查询成绩', command=self.queryData)
        self.root['menu'] = menubar  # 设置菜单栏

    def lurustu(self):
        self.luruPage.pack()
        self.deletestuPage.pack_forget()
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.checkPage.pack_forget()

    def deletestu(self):
        self.luruPage.pack_forget()
        self.deletestuPage.pack()
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.checkPage.pack_forget()

    def inputData(self):
        self.luruPage.pack_forget()
        self.deletestuPage.pack_forget()
        self.inputPage.pack()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.checkPage.pack_forget()

    def deleteData(self):
        self.luruPage.pack_forget()
        self.deletestuPage.pack_forget()
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack()  
        self.modifyPage.pack_forget()
        self.checkPage.pack_forget()

    def modifyData(self):
        self.luruPage.pack_forget()
        self.deletestuPage.pack_forget()
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack()
        self.checkPage.pack_forget()

    def queryData(self):
        self.luruPage.pack_forget()
        self.inputPage.pack_forget()  
        self.queryPage.pack()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()
        self.checkPage.pack_forget()

    def checkData(self):
        self.luruPage.pack_forget()
        self.deletestuPage.pack_forget()
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()
        self.checkPage.pack()

