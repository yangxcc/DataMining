import sqlite3
import tkinter
from tkinter.messagebox import showinfo
import random

'''
生成试题库
'''
con=sqlite3.connect("shitiku.db")
cur=con.cursor()
cur.execute("create table if not exists exam (question varchar(80) null,Answer_A varchar(1) null,Answer_B varchar(1) null,Answer_C varchar(1) null,"
            "Answer_D varchar(1) null,Answer varchar(1) null)")
cur.execute("insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,Answer) values('哈雷彗星的平均周期为','54','56'"
            ",'73','83','C')")
cur.execute("insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,Answer) values('夜郎自大中夜郎指的是现在的那个地方','贵州','云南',"
            "'广西','福建','A')")
cur.execute("insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,Answer) values('中国历史上谁发明了麻药','孙思邈','华佗',"
            "'张仲景','扁鹊','B')")
cur.execute("insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,Answer) values('篮球比赛每队多少人',"
            "'4','5','6','7','B')")
cur.execute("insert into exam (question,Answer_A,Answer_B,Answer_C,Answer_D,Answer) values('1+1=','1','2','3','4','B')")
'''cur.close()
con.commit()
con.close()
'''

'''
读取试题信息
'''
cur.execute("select * from exam")
values=cur.fetchall()
cur.close()
con.close()

'''
界面 逻辑设计
'''
def callNext():
    global k
    global score
    useranswer=r.get()
    if useranswer==values[k][5]:
        score+=10
        showinfo("恭喜，答对了")
    else:
        showinfo("遗憾，打错了")
    k=random.randint(0,len(values))
    if k>=len(values):
        showinfo("题做完啦,请结束答题")
        return
    timu['text']=values[k][0]
    radio1['text']=values[k][1]
    radio2['text']=values[k][2]
    radio3['text']=values[k][3]
    radio4['text']=values[k][4]
    r.set("E")

def callResult():
    showinfo("你的得分：",str(score))

root=tkinter.Tk()
root.title("Python智力问答游戏")
root.geometry("500x200")
r=tkinter.StringVar()
r.set("E")
k=random.randint(0,len(values))
score=0
timu=tkinter.Label(root,text=values[k][0])
timu.pack()
f1=tkinter.Frame(root)
f1.pack()
radio1=tkinter.Radiobutton(root,variable=r,value='A',text=values[k][1])
radio1.pack()
radio2=tkinter.Radiobutton(root,variable=r,value='B',text=values[k][2])
radio2.pack()
radio3=tkinter.Radiobutton(root,variable=r,value='C',text=values[k][3])
radio3.pack()
radio4=tkinter.Radiobutton(root,variable=r,value='D',text=values[k][4])
radio4.pack()
f2=tkinter.Frame(root)
f2.pack()
button1=tkinter.Button(root,text="下一题",command=callNext)
button1.pack(side='left')
button2=tkinter.Button(root,text="结束答题",command=callResult)
button2.pack(side='left')
root.mainloop()


'''
有bug,但改成随机数的时候不知道如何跳出，而且还有产生重复的题
'''