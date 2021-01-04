import tkinter
import pymssql
import tkinter.font as tkFont
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *

import pandas as pd


# 录入学生
class LuruFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.E6 = Entry(self)
        self.E7 = Entry(self)
        self.createPage()

    def Isspace(self, text):
        temp = 0
        for i in text:
            if not i.isspace():
                temp = 1
                break

        if temp == 1:
            return 0
        else:
            return 1

    def showxsb(self, res):
        # print(len(res), res[0])
        i = 0
        root = tkinter.Tk(className=" 学生表 ")
        textPad = ScrolledText(root, width=125, height=50)

        while i < len(res):
            textPad.insert(tkinter.constants.END, chars=str("学号："+str(res[i][0]) + " 姓名: " + str(res[i][1]) + " 性别: "+str(res[i][2]) +
                    " 出生时间: "+str(res[i][3])+" 专业: "+str(res[i][4])+" 总学分: "+str(res[i][5])+" 备注: "+str(res[i][6])+"\n"))
            i = i+1
        textPad.pack()
        root.mainloop()

    def luru(self, num1, name1, sex1, birth1, sdept1, score1, remark1):
        # print(num1, name1, sex1, birth1, sdept1, score1, remark1)
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database,)

        cursor = conn.cursor()  # 获取光标

        temp = 0
        sqlfindstu = "select 学号 from xsb where 姓名= %s"
        cursor.execute(sqlfindstu, name1)
        res = cursor.fetchone()
        # print(res)

        if(res != None):
            temp = 1

        if(temp == 0):
            sqlinsertstu = "insert into xsb(学号,姓名, 性别, 出生时间, 专业, 总学分, 备注) " \
                           "values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                num1, name1, sex1, birth1, sdept1, score1, remark1)
            cursor.execute(sqlinsertstu)
            conn.commit()
            messagebox.showinfo(title='提示', message="录入成功")
            sqlshowstu = "select * from xsb"
            cursor.execute(sqlshowstu)
            res = cursor.fetchall()
            self.showxsb(res)
        else:
            messagebox.showinfo(title='提示', message="已经有该学生信息")

    def click(self):
        num = self.E1.get()
        name = self.E2.get()
        sex = self.E3.get()
        birth = self.E4.get()
        sdept = self.E5.get()
        score = self.E6.get()
        remark = self.E7.get()

        if self.Isspace(name) or self.Isspace(num):
            messagebox.showinfo(title='提示', message="输入项为空")
        else:
            self.luru(num, name, sex, birth, sdept, score, remark)

    def createPage(self):
        a = '#E0FFFF'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        Label(self).grid(row=0, stick=W, pady=0)
        Label(self, text='学号: ', font=ft, bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text='姓名: ', font=ft, bg=a).grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self, text='性别: ', font=ft, bg=a).grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E)
        Label(self, text='出生时间: ', font=ft, bg=a).grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self, text='专业: ', font=ft, bg=a).grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)
        Label(self, text='总学分: ', font=ft, bg=a).grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Label(self, text='备注: ', font=ft, bg=a).grid(row=7, stick=W, pady=10)
        self.E7.grid(row=7, column=1, stick=E)

        Button(self, text='录入学生', font=ft, bg='#FF6600', fg='#FFFFFF', command=self.click).grid(row=8, column=1, stick=E, pady=10)


# 删除学生
class DeletestuFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()

    def showxsb(self, res):
        print(len(res), res[0])
        i = 0
        root = tkinter.Tk(className=" 学生表 ")
        textPad = ScrolledText(root, width=125, height=50)

        while i < len(res):
            textPad.insert(tkinter.constants.END, chars=str("学号："+str(res[i][0]) + " 姓名: " + str(res[i][1]) + " 性别: "+str(res[i][2]) +
                    " 出生时间: "+str(res[i][3])+" 专业: "+str(res[i][4])+" 总学分: "+str(res[i][5])+" 备注: "+str(res[i][6])+"\n"))
            i = i+1
        textPad.pack()
        root.mainloop()

    def Isspace(self, text):
        temp = 0
        for i in text:
            if not i.isspace():
                temp = 1
                break

        if temp == 1:
            return 0
        else:
            return 1

    def deletestu(self, name1, num1):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database)

        cursor = conn.cursor()  # 获取光标

        temp = 0

        sqlfindstu = "select 学号 from xsb where 姓名= %s"
        cursor.execute(sqlfindstu, name1)
        res = cursor.fetchone()
        # print(res)

        if (res != None):
            temp = 1

            sqldelet1 = "delete from cjb where 学号=%s"
            cursor.execute(sqldelet1, num1)

            sqldelet2 = "delete from xsb where 学号=%s"
            cursor.execute(sqldelet2, num1)
            conn.commit()


        if temp == 0:
            messagebox.showinfo(title='提示', message="没有该信息")
        else:
            messagebox.showinfo(title='提示', message="删除成功")
            sqlshowstu = "select * from xsb"
            cursor.execute(sqlshowstu)
            res = cursor.fetchall()
            self.showxsb(res)

    def click(self):
        name = self.E1.get()
        num = self.E2.get()
        if self.Isspace(num) or self.Isspace(name):
            messagebox.showinfo(title='提示', message="输入项为空")
        else:
            self.deletestu(name, num)

    def createPage(self):
        a = '#E0FFFF'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        self.page = Frame(self.root, bg='#E0FFFF')

        Label(self).grid(row=0, stick=W, pady=0)
        Label(self, text='姓名: ', font=ft, bg=a).grid(row=1, stick=W, pady=65)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text='学号: ', font=ft, bg=a).grid(row=2, stick=W, pady=60)
        self.E2.grid(row=2, column=1, stick=E)
        Button(self, text='删除', command=self.click, font=ft, bg='#FF6600', fg='#FFFFFF').grid(row=6, column=1, stick=E, pady=10)


# 更新学生信息
class ModifyFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.E6 = Entry(self)
        self.E7 = Entry(self)
        self.createPage()

    def showxsb(self, res):
        print(len(res), res[0])
        i = 0
        root = tkinter.Tk(className=" 学生表 ")
        textPad = ScrolledText(root, width=125, height=50)

        while i < len(res):
            textPad.insert(tkinter.constants.END, chars=str("学号："+str(res[i][0]) + " 姓名: " + str(res[i][1]) + " 性别: "+str(res[i][2]) +
                    " 出生时间: "+str(res[i][3])+" 专业: "+str(res[i][4])+" 总学分: "+str(res[i][5])+" 备注: "+str(res[i][6])+"\n"))
            i = i+1
        textPad.pack()
        root.mainloop()

    def Isspace(self, text):
        temp = 0
        for i in text:
            if not i.isspace():
                temp = 1
                break

        if temp == 1:
            return 0
        else:
            return 1

    def modify(self, num1, name1, sex1, birth1, sdept1, score1, remark1):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database)

        cursor = conn.cursor()  # 获取光标

        temp = 0

        sqlfindstu = "select 学号 from xsb where 姓名= %s"
        cursor.execute(sqlfindstu, name1)
        res = cursor.fetchone()

        if(res != None):
            temp = 1

        sqlmodify = "update xsb set 性别='{}', 出生时间='{}', 专业='{}', 总学分='{}', 备注='{}' where 学号='{}'"\
            .format(sex1, birth1, sdept1, score1, remark1, num1)
        cursor.execute(sqlmodify)
        conn.commit()

        if temp == 0:
            messagebox.showinfo(title='提示', message="没有该信息")
        else:
            messagebox.showinfo(title='提示', message="修改成功")
            sqlshowstu = "select * from xsb "
            cursor.execute(sqlshowstu)
            res = cursor.fetchall()
            self.showxsb(res)

    def click(self):
        num = self.E1.get()
        name = self.E2.get()
        sex = self.E3.get()
        birth = self.E4.get()
        sdept = self.E5.get()
        score = self.E6.get()
        remark = self.E7.get()
        if self.Isspace(name) and self.Isspace(num):
            messagebox.showinfo(title='提示', message="输入项为空")
        else:
            self.modify(num, name, sex, birth, sdept, score, remark)

    def createPage(self):
        a = '#E0FFFF'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        Label(self).grid(row=0, stick=W, pady=0)
        Label(self, text='学号: ', font=ft, bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text='姓名: ', font=ft, bg=a).grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self, text='性别: ', font=ft, bg=a).grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E)
        Label(self, text='出生时间: ', font=ft, bg=a).grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self, text='专业: ', font=ft, bg=a).grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)
        Label(self, text='总学分: ', font=ft, bg=a).grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Label(self, text='备注: ', font=ft, bg=a).grid(row=7, stick=W, pady=10)
        self.E7.grid(row=7, column=1, stick=E)

        Button(self, text='修改学生信息', font=ft, bg='#FF6600', fg='#FFFFFF', command=self.click).grid(row=8, column=1, stick=E, pady=10)


# 查询学生
class CheckFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()

    def showxsb(self, res):
        i = 0
        root = tkinter.Tk(className=" 学生表 ")
        textPad = ScrolledText(root, width=125, height=50)

        while i < len(res):
            textPad.insert(tkinter.constants.END, chars=str("学号："+str(res[i][0]) + " 姓名: " + str(res[i][1]) + " 性别: "+str(res[i][2]) +
                    " 出生时间: "+str(res[i][3])+" 专业: "+str(res[i][4])+" 总学分: "+str(res[i][5])+" 备注: "+str(res[i][6])+"\n"))
            i = i+1
        textPad.pack()
        root.mainloop()

    def Isspace(self, text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break

        if temp==1:
            return 0
        else:
            return 1

    def check(self, num1):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database)

        cursor = conn.cursor()  # 获取光标

        temp = 0
        sqlfindstu = "select 学号 from xsb where 学号= %s"
        cursor.execute(sqlfindstu, num1)
        res = cursor.fetchone()
        # print(res)

        if (res != None):
            temp = 1
            sqlcheck = "select * from xsb where 学号='{}'".format(num1)
            cursor.execute(sqlcheck)
            # res = cursor.fetchone()
            # i = 0
            # while i<len(res):
            #     print(res[i])
            #     i=i+1
            conn.commit()

        if temp == 1:
            messagebox.showinfo(title='提示', message="查询成功")
            sqlshowstu = "select * from xsb where 学号=%s"
            cursor.execute(sqlshowstu, num1)
            res = cursor.fetchall()
            self.showxsb(res)
        else:
            messagebox.showinfo(title='提示', message="没有该学生信息")

    def click(self):
        num = self.E1.get()
        if self.Isspace(num):
            messagebox.showinfo(title='提示', message="输入项为空")
        else:
            self.check(num)

    def createPage(self):
        a = '#E0FFFF'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        Label(self).grid(row=0, stick=W, pady=30)
        Label(self, text = '学号: ', font=ft,bg=a).grid(row=1, stick=W, pady=105)
        self.E1.grid(row=1, column=1, stick=E)
        Button(self, text='查找', command=self.click, font=ft, bg='#FF6600', fg='#FFFFFF').grid(row=6, column=1, stick=E, pady=10)


# 查询学生成绩
class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()

    def showxscj(self, res):
        root = tkinter.Tk(className=" 学生成绩表 ")
        textPad = ScrolledText(root, width=50, height=20)
        textPad.insert(tkinter.constants.END, chars=str("学号："+str(res[0]) + " 课程号： " + str(res[1]) + " 成绩: " + str(res[2]) + "\n"))
        textPad.pack()
        root.mainloop()

    def Isspace(self, text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break

        if temp == 1:
            return 0
        else:
            return 1

    def query(self, num1, course1):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database)

        cursor = conn.cursor()  # 获取光标

        temp = 0
        sqlfindstu = "select 学号 from xsb where 学号= %s"
        cursor.execute(sqlfindstu, num1)
        res = cursor.fetchone()


        if(res == None):
            temp = 1
        else:
            messagebox.showinfo(title='提示', message="查询成功")
            sqlfindkch = "select 课程号 from kcb where 课程名=%s"
            cursor.execute(sqlfindkch, course1)
            kch = cursor.fetchone()
            kch = kch[0]

            sqlfindcj = "select * from cjb where 学号='{}' and 课程号='{}'".format(num1, kch)
            cursor.execute(sqlfindcj)
            res = cursor.fetchone()
            self.showxscj(res)


        if(temp == 1):
            messagebox.showinfo(title='提示', message="没有该信息")


    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        if self.Isspace(num) or self.Isspace(course):
            messagebox.showinfo(title='提示', message="输入项为空")
        else:
            self.query(num, course)

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        a = '#E0FFFF'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        Label(self).grid(row=0, stick=W, pady=0)
        Label(self, text = '学号: ', font=ft, bg=a).grid(row=1, stick=W, pady=60)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text='科目: ', font=ft, bg=a).grid(row=2, stick=W, pady=55)
        self.E2.grid(row=2, column=1, stick=E)

        Button(self, text='查找', command=self.click, font=ft, bg='#FF6600', fg='#FFFFFF').grid(row=6, column=1, stick=E, pady=10)


# 录入成绩
class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.createPage()  

    # 判断输入是否为空

    def Isspace(self, text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break

        if temp == 1:
            return 0
        else:
            return 1

    def showxscj(self, res):
        root = tkinter.Tk(className=" 学生成绩表 ")
        textPad = ScrolledText(root, width=50, height=20)
        textPad.insert(tkinter.constants.END, chars=str("学号："+str(res[0]) + " 课程号： " + str(res[1]) + " 成绩: " + str(res[2]) + "\n"))
        textPad.pack()
        root.mainloop()

    def write(self, num1, course1, score1):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database)

        cursor = conn.cursor()  # 获取光标

        temp = 0
        sqlfindstu = "select 学号 from xsb where 学号= %s"
        cursor.execute(sqlfindstu, num1)
        res = cursor.fetchone()

        if(res == None):
            messagebox.showinfo(title='提示', message="没有该学生")
        else:
            sqlfindkch = "select 课程号 from kcb where 课程名=%s"
            cursor.execute(sqlfindkch, course1)
            kch = cursor.fetchone()
            kch = kch[0]

            sqlfindcj = "select 成绩 from cjb where 课程号='{}' and 学号='{}'".format(kch, num1)
            cursor.execute(sqlfindcj)
            cj = cursor.fetchone()


            if(cj != None ):
                messagebox.showinfo(title='结果', message="已存在该学生科目信息！")
            else:
                sqlwritecj = "insert into cjb(学号, 课程号, 成绩) values('{}', '{}', '{}')".format(num1, kch, score1)
                cursor.execute(sqlwritecj)
                conn.commit()
                messagebox.showinfo(title='提示', message="写入成功")
                sqlfindcj = "select * from cjb where 学号='{}' and 课程号='{}'".format(num1, kch)
                cursor.execute(sqlfindcj)
                res = cursor.fetchone()
                self.showxscj(res)





    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        score = self.E3.get()
        if self.Isspace(num) or self.Isspace(course) or self.Isspace(score):
            messagebox.showinfo(title='提示', message="输入项为空")
        else:
            self.write(num, course, score)

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        a = '#E0FFFF'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)

        self.page = Frame(self.root, bg='#E0FFFF')
        self.page.pack(expand=YES, fill=BOTH)

        Label(self, text='学号: ', font=ft, bg=a).grid(row=1, stick=W, pady=35)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text='科目: ', font=ft, bg=a).grid(row=2, stick=W, pady=40)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text='成绩: ', font=ft, bg=a).grid(row=3, stick=W, pady=30)
        self.E3.grid(row=3, column=1, stick=E)
        
        Button(self, text='录入成绩', command=self.click, font=ft, bg='#FF6600', fg='#FFFFFF').grid(row=6, column=1, stick=E, pady=10)


# 删除成绩
class DeleteFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()
        
    def Isspace(self, text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break

        if temp == 1:
            return 0
        else:
            return 1

    def delete(self, num1, course1):
        server = "DESKTOP-86UQ1HA"
        user = "sa"
        password = "xhn147852"
        database = "YU"
        conn = pymssql.connect(server, user, password, database)

        cursor = conn.cursor()  # 获取光标

        temp = 0
        sqlfindstu = "select 学号 from xsb where 学号= %s"
        cursor.execute(sqlfindstu, num1)
        res = cursor.fetchone()

        if(res == None):
            temp = 1
        else:
            sqlfindkch = "select 课程号 from kcb where 课程名=%s"
            cursor.execute(sqlfindkch, course1)
            kch = cursor.fetchone()
            kch = kch[0]

            sqldeletecj = "delete from cjb where 课程号='{}' and 学号='{}'".format(kch, num1)
            cursor.execute(sqldeletecj)
            conn.commit()

        if temp == 1:
            messagebox.showinfo(title='提示', message="没有该信息")
        else:
            messagebox.showinfo(title='提示', message="删除成功")
        
    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        if self.Isspace(num) or self.Isspace(course):
            messagebox.showinfo(title='提示', message="输入项为空")
        else:
            self.delete(num, course)
            
    def createPage(self):
        a = '#E0FFFF'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD) 
        self.page = Frame(self.root, bg='#E0FFFF')

        Label(self).grid(row=0, stick=W, pady=10)     
        Label(self, text = '学号: ', font=ft, bg=a).grid(row=1, stick=W, pady=55)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text='科目: ', font=ft, bg=a).grid(row=2, stick=W, pady=60)
        self.E2.grid(row=2, column=1, stick=E)
        Button(self, text='删除', command=self.click, font=ft, bg='#FF6600', fg='#FFFFFF').grid(row=6, column=1, stick=E, pady=10)



