from tkinter import *
from tkinter.messagebox import *
from MainPage import *
import tkinter.font as tkFont
import pymssql



class LoginPage(Frame):
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (450, 450))  # 设置窗口大小
        self.num = StringVar()
        self.username = StringVar()
        self.pwd = StringVar()
        self.createPage()

    def createPage(self):
        a = '#FEEEEE'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        self.page = Frame(self.root, bg='#FFFFFF')  # 创建Frame
        self.page.pack(expand=YES, fill=BOTH)
        Label(self.page).grid(row=0, stick=W)

        Label(self.page, text='学号: ', font=ft, bg=a).grid(row=1, column=0, stick=N, pady=5)
        Entry(self.page, textvariable=self.num, width=25, ).grid(row=1, column=1, stick=E)
        Label(self.page, text='姓名: ', font=ft, bg=a).grid(row=2, column=0, stick=N, pady=5)
        Entry(self.page, textvariable=self.username, width=25,).grid(row=2, column=1, stick=E)
        Label(self.page, text='密码: ', font=ft, bg=a).grid(row=3, column=0, stick=N, pady=5)
        Entry(self.page, textvariable=self.pwd, show='*', width=25).grid(row=3, column=1, stick=E)

        Button(self.page, text='登陆', command=self.loginCheck, font=ft, bg='#FF6600', fg='#FFFFFF').grid(row=4, column=1, pady=5)
        Button(self.page, text='退出', command=self.page.quit, font=ft, bg='#FF6600', fg='#FFFFFF').grid(row=4, column=2, pady=5)

    def loginCheck(self):
        num = self.num.get()
        name = self.username.get()
        pwd = self.pwd.get()

        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database, )

        cursor = conn.cursor()  # 获取光标

        sqlfindname = "select username from jsb where username=%s"
        cursor.execute(sqlfindname, name)
        res = cursor.fetchone()
        # print(res)
        if res != None:  # 判断是教师还是学生,不为空是教师
            if self.isLegalUser(name, pwd):
                self.page.destroy()
                MainPage(self.root)
            else:
                showinfo(title='错误', message='密码错误！')
        else:  # 学生登录
            sqlfindstu = "select 姓名 from xsb where 学号=%s"
            cursor.execute(sqlfindstu, num)
            res = cursor.fetchone()
            res = res[0]
            res = res.replace(" ", '')
            if(res == name):
                # self.page.destroy()
                self.isStu()
            else:
                showinfo(title='错误', message='学生姓名或学号错误！')

    #  教师登录
    def isLegalUser(self, name, pwd):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database, )

        cursor = conn.cursor()  # 获取光标

        sqlcheckpwd = "select pwd from jsb where username=%s"
        cursor.execute(sqlcheckpwd, name)
        res = cursor.fetchone()
        res = str(res[0])
        res = res.replace(" ", "")
        # print(res, pwd)
        # print(res == pwd)
        if(res == pwd):
            return True
        else:
            return False

    def isStu(self):
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        Button(self.page, text='查询学生信息', font=ft, bg='#FF6600', fg='#FFFFFF', command=self.click1).grid(row=4, column=0, pady=5)
        Button(self.page, text='查询学生成绩', font=ft, bg='#FF6600', fg='#FFFFFF', command=self.click2).grid(row=4, column=1, pady=5)
        Button(self.page, text='返回', font=ft, bg='#FF6600', fg='#FFFFFF', command=self.back).grid(row=4, column=2,pady=5)

    def click1(self):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database, )

        cursor = conn.cursor()  # 获取光标
        sqlshowstu = "select * from xsb where 学号=%s"
        num = self.num.get()
        num = num.replace(" ", '')
        print(num)
        cursor.execute(sqlshowstu, num)
        res = cursor.fetchone()
        # print(res)

        root = tkinter.Tk(className=" 学生信息表 ")
        textPad = ScrolledText(root, width=100, height=10)
        textPad.insert(tkinter.constants.END, chars=str("学号：" + str(res[0]) + " 姓名: " + str(res[1])
                                                            + " 性别: " + str(res[2]) + " 出生时间: " + str(res[3])
                                                            + " 专业: " + str(res[4]) + " 总学分: " + str(res[5])
                                                            + " 备注: " + str(res[6]) + "\n"))
        textPad.pack()
        root.mainloop()

    def click2(self):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database, )

        cursor = conn.cursor()  # 获取光标

        sqlshowstucj = "select * from cjb where 学号=%s"
        num = self.num.get()
        num = num.replace(" ", '')
        cursor.execute(sqlshowstucj, num)
        res = cursor.fetchall()

        i = 0
        root = tkinter.Tk(className=" 学生成绩表 ")
        textPad = ScrolledText(root, width=100, height=10)
        while i < len(res):
            textPad.insert(tkinter.constants.END, chars=str("学号： " + str(res[i][0]) + "课程号: " + str(res[i][1]) + "成绩: " + str(res[i][2]) + "\n"))
            i = i+1
        textPad.pack()
        root.mainloop()

    def back(self):
        self.page.destroy()
        LoginPage(self.root)


