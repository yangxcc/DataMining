import sqlite3
#打开数据库，或者创建表
def opendb():
    con=sqlite3.connect("mydb.db")
    cur=con.execute("create table if not exists tongxunlu(usernum interger primary key,username varchar(128),password varchar(128)"
                    ",address varchar(128),telnum varchar(128) )")
    return cur,con
#查询全部信息
def showalldb():
    print("----------处理后的数据----------")
    hel=opendb()
    cur=hel[1].cursor()
    cur.execute("select * from tongxunlu")
    for row in cur:
        print(row)
    cur.close()
#向数据库中输入信息
def into():
    usernum=input("请输入学号：\n")
    username=input("请输入姓名：\n")
    password=input("请输入密码：\n")
    address=input("请输入地址：\n")
    telnum=input("请输入联系电话\n")
    return usernum,username,password,address,telnum
#往数据库里添加记录
def adddb():
    welcome="""----------欢迎使用添加数据功能----------"""
    print(welcome)
    person=into()
    hel=opendb()
    cur=hel[1].cursor()
    cur.execute("insert into tongxunlu(usernum,username,password,address,telnum) values(?,?,?,?,?)",(
        person[0],person[1],person[2],person[3],person[4]
    ))
    hel[1].commit()   #事务提交
    print("----------恭喜你，数据添加成功----------")
    showalldb()
    hel[1].close()
#删除数据库中的内容
def deldb():
    welcome = """----------欢迎使用删除数据功能----------"""
    print(welcome)
    hel=opendb()
    cur=hel[1].cursor()
    delchoice=input("请输入想要删除的学号:")
    cur.execute("delete from tongxunlu where usernum="+delchoice)
    hel[1].commit()
    print("----------恭喜你，数据删除成功----------")
    showalldb()
    hel[1].close()
#修改数据库中的内容
def alter():
    welcome = """----------欢迎使用修改数据功能----------"""
    print(welcome)
    hel=opendb()
    cur=hel[1].cursor()
    changechoice=input("请输入将要修改的学生的学号：")
    person=into()
    cur.execute("update tongxunlu set usernum=?,username=?,password=?,address=?,telnum=? where usernum="+changechoice,(person[0],
                person[1],person[2],person[3],person[4]))
    hel[1].commit()
    print("----------恭喜你，数据库更新成功----------")
    showalldb()
#查询数据
def searchdb():
    welcome = """----------欢迎使用查询数据功能----------"""
    print(welcome)
    hel=opendb()
    cur=hel[1].cursor()
    choice=input("请输入将要查询学生的学号：")
    cur.execute("select * from tongxunlu where usernum="+choice)
    hel[1].commit()
    print("----------恭喜你，你要查找的数据如下----------")
    for row in cur:
        print(row[0],row[1],row[2],row[3],row[4])
    hel[1].close()
#是否继续
def conti(a):
    choice=input("是否继续Y/N")
    if choice=='y' or choice=='Y':
        a=1
    else:
        a=0
    return a

if __name__ == '__main__':
    flag=1
    while flag:
        welcome="----------欢迎使用通讯录----------"
        print(welcome)
        choiceshow="""
        请选择你的下一步操作：
        （添加）往数据库里添加内容
        （删除）删除数据库中的内容
        （修改）修改数据库中的内容
        （查询）查询数据库中的内容
        选择你要进行的操作：
        """
        choice=input(choiceshow)   #####这种用法！！！！
        if choice=='添加':
            adddb()
            conti(flag)
        elif choice=='删除':
            deldb()
            conti(flag)
        elif choice=='修改':
            alter()
            conti(flag)
        elif choice=='查询':
            searchdb()
            conti(flag)
        else:
            print("输入不合法，请重新输入：")
            #input("输入不合法，请重新输入：")


