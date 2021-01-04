# 摘要

 ​	随着在校大学生的人数不断增多，学生的成绩管理也成了一件很繁琐的事情，利用计算机技术高效的、系统的处理学生成绩，已经成为了提高学校教务系统管理效率，改善学生服务的关键。因此，开发一套适和大众的、兼容性好的学生成绩管理系统是很有必要的。本课程设计使用Python语言来实现“学生成绩管理系统”的基本功能，通过Python来操作SQL Server数据库。采用的开发工具为PyCharm，为简便起见，使用了Python自带的Tkinter来制作“学生成绩管理系统”界面，用pymsSQL模块访问SQL Server数据库。完成了一个具有学生信息管理和学生成绩管理功能的系统，其中涵括了对学生的信息进行录入、删除、更新、查询的功能和对成绩进行录入、删除、查询的功能。较为良好地实现了“学生成绩管理系统”的基本功能。

 学生成绩管理系统；数据库操作；可视化编程

​	 As the number of college students continues to increase, student performance management has become a very cumbersome task. Using computer technology to efficiently and systematically process student performance has become a way to improve the management efficiency of the school’s educational administration system and improve student services. The essential. Therefore, it is necessary to develop a student performance management system that is suitable for the general public and has good compatibility. This course is designed to use the Python language to implement the basic functions of the "student score management system", and to operate the SQL Server database through Python. The development tool used is PyCharm. For the sake of simplicity, Tkinter that comes with Python is used to make the interface of "Student Achievement Management System", and the pymsSQL module is used to access the SQL Server database. A system with student information management and student performance management functions is completed, which includes the functions of inputting, deleting, updating, and querying student information and the functions of inputting, deleting, and querying grades. The basic functions of the "student performance management system" are relatively well realized.

 Student performance management system; database operation; visual programming

# 一、课题背景

## 1.1 背景：

​    随着在校大学生的人数不断增多，学生的成绩管理也成了一件很繁琐的事情，利用计算机技术高效的、系统的处理学生成绩，已经成为了提高学校教务系统管理效率，改善学生服务的关键。因此，开发一套适和大众的、兼容性好的学生成绩管理系统是很有必要的。大学的课程按专业划分，不同的专业可能有相同的必修课和选修课。 必修一般指学校或院系规定学生必须修习某课程， 学校对必修课程一般有统一的要求和安排。 选修是指根据学生个人兴趣或专业需要自由选择修习某课程。 一般来说， 基础性的知识都作为必修课程。 有些知识不是基础性的， 与兴趣和研究方向有关， 这部分知识可以选择。 这是大学与中学最大的不同之处，凸显了学生成绩管理的复杂性和多样性，使得开发一款更加简洁方便的成绩管理系统的需求显得尤为急切和重要。90 年代中期，由于 Internet 的迅普及，Internet技术在企业管理信息系统中的应用和延伸， 形成了集计算机， 计算机网络、 数据库、 分布式计算等于一体的信息技术综合体， 它打破了时间和地域的界限， 使信息交流变得快捷、 准确， 为建立现代高校管理信息系统提供了充足的条件， 用计算机数据库系统的形式来管理选课成为了既方便又快捷的一种方式。 因此开发学生成绩管理系统是十分有前景的工作。

## 1.2 目的：

​	利用计算机支持学校高效率完成学生成绩管理， 是适应现代管理要求、 推动企业劳动型治理走向科学化、 规范化的必要条件； 而成绩管理是一项琐碎、 复杂而又十分细致的工作， 学生的基本资料， 所开设的课程条目， 选课资料的保存， 选课条件的约束，成绩的录入和查询， 一般不允许出错， 假如实行手工操作， 须手工填制大量的表格， 这就会耗费工作人员大量的时间和精力， 而计算机选课操作， 不仅能够保证各项信息准确无误、 快速输出， 同时计算机具有手工治理所无法比拟的优点.例如： 检索迅速、 查找方便、 可靠性高、 存储量大、 保密性好、 寿命长、 成本低等。 这些优点能够极大地提高学校成绩管理的效率， 也是学校的科学化、 正规化管理， 与时代接轨的重要条件。开发本系统就是为了解决高校在选课操作管理中的一些不规范，使学生信息，课程信息，成绩信息的治理向着规范化、 简单化、 有效化的方向发展。


# 二、设计简介及设计方案论述

## 2.1系统需求分析

### 2.1.1信息需求

​	学生成绩管理系统涉及的实体有：

（1）学生：学号，姓名，性别，出生时间，专业，总学分，备注；

（2）教师：用户名，密码

（3）课程：课程号，课程名，开课学期，学时，学分

（4）成绩：学号，课程号，分数

### 2.1.2功能需求

（1）能够对学生信息进行管理。

（2）能够对学生成绩进行管理。

（3）界面设计，简单的显示“教师学生成绩管理”和“学生信息查询”视图界面。

（4）教师学生成绩管理模块能对学生信息进行录入、删除、更新、查询操作并能对成绩进行录入、删除、查询操作。

（5）学生信息查询模块能对自己的信息和成绩进行查询操作。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130105439051.png" alt="image-20201130105439051" style="zoom:67%;" />

![image-20201126214339921](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201126214339921.png)

 

图二 数据流图

## 2.2概念结构设计

### 2.2.1 E-R 图

学生信息表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130111459475.png" alt="image-20201130111459475" style="zoom:67%;" />

教师表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130111514019.png" alt="image-20201130111514019" style="zoom:67%;" />

课程表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130111538130.png" alt="image-20201130111538130" style="zoom:67%;" />

成绩表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130111550458.png" alt="image-20201130111550458" style="zoom:67%;" />

全局E-R图：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201129172232594.png" alt="image-20201129172232594" style="zoom:67%;" />

## 2.3逻辑结构设计

设计学生成绩管理数据库，包括教师、学生、课程、成绩四个关系。

**关系模型：**

教师（<u>用户名</u>，密码）

学生（<u>学号</u>,姓名, 性别, 出生时间, 专业, 总学分, 备注）

课程（<u>课程号</u>，课程名， 学分，学时，开课学期）

成绩（<u>学号</u>，<u>课程号</u>， 分数）

## 2.4 物理设计

### 2.4.1创建数据库

打开SQL工具“查询分析器”，在查询窗口中键入下列SQL语句

```sql
create database YU 
```

执行上述SQL语句即可新建一名为YU的数据库。

### 2.4.2创建数据表

​	一个完整的数据库不可缺少的就是数据表，若干个数据表的集合成一个数据库。数据表主要用来存放一定格式的记录，数据表中的行被称为记录，列被称为字段。创建数据表的过程其实就是定义字段的过程。

​	在此学生成绩管理系统中需要创建四个表，即教师信息表、学生信息表、课程信息表和成绩表。

教师信息表：

![image-20201126225824850](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201126225824850.png)

学生信息表：

![image-20201126225751135](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201126225751135.png)

课程信息表：

![image-20201126225805002](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201126225805002.png)

成绩信息表：

![image-20201126225728969](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201126225728969.png)

### 2.4.3数据关系图

![image-20201130113838582](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130113838582.png)

## 2.5数据库的实施和维护

数据库运行与维护的主要任务包括：
（1）维护数据库的安全性与完整性
（2）监测并改善数据库性能
（3）重新组织和构造数据库
只要数据库系统在运行，就需要不断地进行修改、调整和维护。在运行数据库时，发现了以下问题并进行了维护：

（1）学生对信息有增删查改的权限，不符合实况，于是增加了教师用户，使得成绩管理系统更加的合理。

（2）学生能查询所有的学生信息，不符合常理。于是修改了SQL查询语句。也可以选择创建视图：

```sql
//创建学生的视图，每个学生只能查询自己的成绩
creat view Stu_info as select 学号, 姓名, 性别, 出生时间, 专业, 总学分, 备注
from xsb
where 学号=%s

creat view Stu_cj as select 学号, 课程号, 成绩
form cjb
where 学号=%s
```

# 三、详细设计

## 3.1程序的运行环境、开发环境

```python
前台是用anaconda配置的python环境写的。

anaconda        2020.02
python			3.6
Package         Version
--------------- ---------
certifi         2020.11.8
chardet         3.0.4
idna            2.10
numpy           1.19.3
pandas          1.1.4
pip             20.2.4
pymssql         2.1.5
python-dateutil 2.8.1
pytz            2020.4
setuptools      36.4.0
six             1.15.0
urllib3         1.26.2
wheel           0.29.0
wincertstore    0.2

后台数据库选用SQL SERVER
```

## 3.2模块说明

### 3.2.1 数据库的连接

选用Python中的pymssql库来连接SQL SERVER：

```python
#  创建人:  1805120626_实验1班_喻洁

import pymssql  # pymssql是python用来连接Microsoft SQL Server的一个工具库

server = "DESKTOP-86UQ1HA"
user = "sa"
password = "xhn147852"
database = "YU"
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()   # 获取光标
```

### 3.2.2部分功能的实现及分析

##### 登录：

由于学生不能对数据库中的表进行增删改的操作，也不能查询其他人的信息，故设置了一个登录界面。当输入学号和姓名时是学生登录，进入学生查询信息的界面。当输入为姓名和密码时是教师登录，进入可以对全体学生信息和成绩进行增删查改操作的界面。

```python
    def loginCheck(self):
        num = self.num.get()
        name = self.username.get()
        pwd = self.pwd.get()

        sqlfindname = "select username from jsb where username=%s"
        cursor.execute(sqlfindname, name)
        res = cursor.fetchone()
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
        sqlcheckpwd = "select pwd from jsb where username=%s"
        cursor.execute(sqlcheckpwd, name)
        res = cursor.fetchone()
        res = str(res[0])
        res = res.replace(" ", "")
        if(res == pwd):
            return True
        else:
            return False
        
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

        root = tkinter.Tk(className=" 学生信息表 ")
        textPad = ScrolledText(root, width=100, height=10)
        textPad.insert(tkinter.constants.END, chars=str("学号：" + str(res[0]) + " 姓名: " + str(res[1])
                                                            + " 性别: " + str(res[2]) + " 出生时间: " + str(res[3])
                                                            + " 专业: " + str(res[4]) + " 总学分: " + str(res[5])
                                                            + " 备注: " + str(res[6]) + "\n"))
        textPad.pack()
        root.mainloop()

    def click2(self):        
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
```

学生登录：

输入学号和姓名进入自己的信息查询界面：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130093845882.png" alt="image-20201130093845882" style="zoom:67%;" />

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130093857761.png" alt="image-20201130093857761" style="zoom:67%;" />

教师登录：

输入姓名和密码，进入信息和成绩管理界面

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094251896.png" alt="image-20201130094251896" style="zoom:67%;" />



<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094314039.png" alt="image-20201130094314039" style="zoom:67%;" />

##### 录入学生：

教师登录后，点击录入学生按钮，键入学号,姓名, 性别, 出生时间, 专业, 总学分, 备注，再点击录入学生的按钮即可将学生信息录入数据库中的学生表，并会弹出录入新学生信息后的学生表信息总览。

```python
    def luru(self, num1, name1, sex1, birth1, sdept1, score1, remark1):        
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
```

进行录入：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094631203.png" alt="image-20201130094631203" style="zoom:67%;" />

原学生表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094510987.png" alt="image-20201130094510987" style="zoom:67%;" />

录入后学生表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094835761.png" alt="image-20201130094835761" style="zoom:67%;" />



##### 删除学生：

教师登录后，点击删除学生按钮，键入学生学号，姓名。若此学生在成绩表中有信息，则先删除数据库中成绩表该学生的成绩信息，再在学生表中删除改学生的信息。

```python
    def deletestu(self, name1, num1):
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
```

删除学生界面：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130095803932.png" alt="image-20201130095803932" style="zoom:67%;" />

删除前学生表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130095711863.png" alt="image-20201130095711863" style="zoom:67%;" />

删除后学生表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130095904593.png" alt="image-20201130095904593" style="zoom:67%;" />



##### 更新学生：

教师登录后，点击更新学生按钮，先键入学生学号和姓名在数据库中定位条目，再键入要更新的信息：性别, 出生时间, 专业, 总学分, 备注等信息。

```python
    def modify(self, num1, name1, sex1, birth1, sdept1, score1, remark1):        
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
```

更新学生信息界面：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100215795.png" alt="image-20201130100215795" style="zoom:67%;" />

更新前学生信息：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100158845.png" alt="image-20201130100158845" style="zoom:67%;" />

更新后学生信息：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100317477.png" alt="image-20201130100317477" style="zoom:67%;" />

##### 查询学生：

学生端登录，点击查询学生信息，将登录的学号和姓名信息传入SQL查询语句，实现只查询登录学生的学生信息。教师登录，点击查询学生按钮，键入学号即可查询该学生信息。

```python
    def check(self, num1):
        temp = 0
        sqlfindstu = "select 学号 from xsb where 学号= %s"
        cursor.execute(sqlfindstu, num1)
        res = cursor.fetchone()

        if (res != None):
            temp = 1
            sqlcheck = "select * from xsb where 学号='{}'".format(num1)
            cursor.execute(sqlcheck)
            conn.commit()

        if temp == 1:
            messagebox.showinfo(title='提示', message="查询成功")
            sqlshowstu = "select * from xsb where 学号=%s"
            cursor.execute(sqlshowstu, num1)
            res = cursor.fetchall()
            self.showxsb(res)
        else:
            messagebox.showinfo(title='提示', message="没有该学生信息")
```

学生查询学生信息：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094006569.png" alt="image-20201130094006569" style="zoom:67%;" />

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130093959424.png" alt="image-20201130093959424" style="zoom:67%;" />

教师查询学生信息：

查询界面：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100420979.png" alt="image-20201130100420979" style="zoom:67%;" />

查询所得学生信息：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100530261.png" alt="image-20201130100530261" style="zoom:67%;" />

##### 录入成绩：

教师登录，点击录入成绩按钮，键入学号、课程名、分数即可录入该学生成绩信息，若该学生该课程已有成绩，则弹出提示信息。

```python
    def write(self, num1, course1, score1):        
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
```

录入成绩界面：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100834931.png" alt="image-20201130100834931" style="zoom:67%;" />

录入学生成绩前：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100744354.png" alt="image-20201130100744354" style="zoom:67%;" />

录入学生成绩后：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130100911354.png" alt="image-20201130100911354" style="zoom:67%;" />

##### 删除成绩：

教师登录，点击删除成绩按钮，键入学号、课程名，判断该学生选修了此课程并有成绩，即可删除该学生成绩信息。

```python
    def delete(self, num1, course1):
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
```

删除成绩界面：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130101031836.png" alt="image-20201130101031836" style="zoom:67%;" />

删除前成绩表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130101213816.png" alt="image-20201130101213816" style="zoom:67%;" />

删除后成绩表：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130101308553.png" alt="image-20201130101308553" style="zoom:67%;" />

##### 查询成绩：

学生端登录，点击查询学生成绩，将登录的学号和姓名信息传入SQL查询语句，实现只查询登录学生的学生成绩信息。教师登录，点击查询成绩，键入学号和课程名即可查询该学生某一门课程的成绩信息。

```python
    def query(self, num1, course1):
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
```

学生查询自己成绩：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094056187.png" alt="image-20201130094056187" style="zoom:67%;" />

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130094147298.png" alt="image-20201130094147298" style="zoom:67%;" />

教师查询学生成绩：

查询界面：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130101459112.png" alt="image-20201130101459112" style="zoom:67%;" />

查询结果：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130101527963.png" alt="image-20201130101527963" style="zoom:67%;" />

# 四、总结

在平时的学习中， 只学习了一些基本的 SQL 语句特点及操作方法， 但这次课
程设计是要求作出一个独立的系统， 不仅要用到 SQL 知识， 还有用到其他的软件，这些软件大部分对我来说都是陌生的， 这让我在设计的过程中遇到了很大的困难， 课设后我稍加总结，我在课程设计中遇到了以下方面的问题：
1、 本次课设我采用了 SQL severs 2019 作为建立数据库的工具，pycharm 作为开发界面的工具。 这两个软件对我来说都是不熟悉的， 在这里我遇到了第一个难题，pycharm软件不会运用， 对 pycharm给出的各控件一无所知， 一度设计进度为零， 但后来经过在网上查阅资料和自己摸索， 慢慢的我能作出一些界面了。 这一个麻烦算是解决了。
2、 在做好界面之后， 又遇到了另一个问题， 不知道怎么把设计好的界面和 SQL
建立的数据库连接在一起， 如果不能连接在一起的话， 那这次课设将是不成功的，后经去图书馆查阅资料， 上网搜索资料， 和同学讨论， 在了解到想要把 pycharm做的界面的 SQL 建立的数据库连接在一起必须要用到 pycharm中提供的库pymssql， 设置好后就能连接到数据库实现一些基本的功能了。
3、 在建立好连接和做好界面后， 后面的是建立表， 把需求和 SQL 语句联系到
一起， 这里同样存在很多问题， 包括建立的表格是否合理， 一些功能是否服符合实际和要求等， 这里的主要解决方法是反复阅读任务要求， 综合考虑各方面的因素， 在设计的过程中不断和同学探讨， 最后才能给出一个较为合理和实际的学生成绩管理系统。

这次的课程设计对我的意义很大。 不仅巩固了就知识， 还学会了新知识。 更是激起了我对数据库的兴趣。在课程设计时， 遇到了很多在书本中和课堂上没有机会遇到的问题， 在课堂上只能学习到数据库中有一些最为基本的知识， 但在课程设计中这些基本知识只是一个基础， 在拿到设计任务书时， 我甚至不能理解什么是 C/S 模式和 B/S 模式，对做出界面毫无概念， 更不要说是把数据库和直观的界面联系在一起， 去完成一个系统了 。 这体现在课程设计中的是我花费近一半的时间去学习怎么用python语言连接数据库， 怎么能实现一个界面到另一个界面的跳转， 怎么通过直观上界面的操作改变个显示数据库中的信息。 这个过程是很痛苦的， 一方面是对设计出一个系统的兴趣驱使我不断的去学习新知识和改正错误； 另一方面是对设计出一个系统没有任何经验。但是看到运用所学知识做出的成果时， 还是选择继续做下去， 哪怕不能实现太多的功能， 但最起码要凭借自己去做出一个系统。在课设中遇到了 诸多苦难和千奇百怪的错误， 一度灰心过。 但当改正错误时， 不由兴起一股成就感， 这些改正后的错误一直激励我坚持到最后， 从这的课程设计中我巩固了以前所学， 新学习到了 python知识， 遇到了很多错误， 但是最终也完成了一个系统， 这次课程设计对我来说是使我受益匪浅！    