import tkinter as tk
import random

number=random.randint(0,1024)    #玩家要猜的数字
running=True
num=0  #猜的次数
nmaxn=1024
nminn=0

def labelqval(vText):
    label_val_q.config(label_val_q,text=vText)
def eBtnClose(event):
    root.destroy()

def eBtnGuess(event):
    global nmaxn
    global nminn
    global num
    global running
    if running:
        val_a=int(entry_a.get())
        if val_a>1024 or val_a<0:
            labelqval("输入的数字超出范围，请重新输入")
        else:
            if val_a==number:
                labelqval("恭喜答对了")
                num+=1
                running=False
                numGuess()
            elif val_a<number:
                 num+=1
                 nminn=val_a
                 labelqval("猜小了，请输入"+str(nminn)+"到"+str(nmaxn)+"之间的数")
            else:
                 num+=1
                 nmaxn=val_a
                 labelqval("猜大了，请输入"+str(nminn)+"到"+str(nmaxn)+"之间的数")

    else:
         labelqval("你已经答对了")

def numGuess():
    if num==1:
        labelqval("一次答对")
    elif num<10:
        labelqval("10次以内答对了，不错哟")
    else:
        labelqval("超过10次了，嘤嘤嘤")

root=tk.Tk(className='猜数字游戏')
root.geometry("400x90+200+200")
label_val_q=tk.Label(root,width=80)
label_val_q.pack(side='top')
entry_a=tk.Entry(root,width='40')
entry_a.pack(side='left')
bt1=tk.Button(root,text='猜')
bt1.bind('<Button-1>',eBtnGuess)
bt1.pack(side='left')
bt2=tk.Button(root,text='关闭')
bt2.bind('<Button-1>',eBtnClose)
bt2.pack(side='left')
labelqval("请输入0-1024之间的任意整数")
root.mainloop()


