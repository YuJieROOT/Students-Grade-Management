#  创建人:  1805120626_实验1班_喻洁

import pymssql  # pymssql是python用来连接Microsoft SQL Server的一个工具库
import tkinter as tk
from LoginPage import *

server = "DESKTOP-86UQ1HA"
user = "sa"
password = "xhn147852"
database = "YU"
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()   # 获取光标

'''
录入学生测试(python 语法测试)
sqlfindstu = "select 姓名 from xsb where 学号='20626'"
cursor.execute(sqlfindstu)
res = cursor.fetchone()

if(res != None):
        temp = 1

num1='1010'
name1='yujie'
sex1='False'
birth1='2001-01-02'
sdept1='cs'
score1='99'
remark1='sdljfh'

# 'num1', 'name1', '0', 'birth1', 'sdept1', 'score1', 'remark1'
# 学号,姓名, 性别, 出生时间, 专业, 总学分, 备注

sqlinsertstu = "insert into xsb(学号,姓名, 性别, 出生时间, 专业, 总学分, 备注) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(num1, name1, sex1, birth1, sdept1, score1, remark1)
cursor.execute(sqlinsertstu)

cursor.execute("select 姓名 from xsb where 学号='1010'")
res = cursor.fetchone()
print(res[0])

'''

root = tk.Tk()
root.title('wit学生管理系统-喻洁')

photo = tk.PhotoImage(file="wit.png")
label_img = tk.Label(root, width=300, height=210, image=photo, bg='#FFFFFF')
label_img.pack(expand=YES, fill=BOTH)


LoginPage(root)
# MainPage(root)
root.mainloop()


