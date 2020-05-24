'''
创建组件对象的时绑定
'''
from tkinter import *
from tkinter.messagebox import showinfo


'''def callback():
    showinfo("Pyhton command","人生苦短，我用python")
root=Tk()
bt1=Button(root,text='设置command事件调用命令',command=callback())

'''

'''
第二种方法：示例绑定
调用组件对象实例方法bind()可以为指定组件示例绑定事件，这是最常用的方式
如：canvas.bind("<Button-1>",drawline)
bind函数的第一个参数是事件描述符，指定无论什么时候在canvas上只要点击鼠标左键就调用
事件处理函数drawline进行画线任务，注意：drawline后面是没有括号的，这里只需要声明一下就好
'''
'''
root=Tk()
def printRect(event):
    print('rectangle左键事件')
def printRect2(event):
    print('rectangle右键事件')
def drawline(event):
    print('Line事件')

cv=Canvas(root,bg='white')
rt1=cv.create_rectangle(10,10,110,110,width=8,tags='r1')
cv.tag_bind('r1','<Button-1>',printRect)
cv.tag_bind('r1','<Button-3>',printRect2)  #Button1为鼠标左键，Button3为鼠标右键
#创建一个Line,并将其tags设置为r2
cv.create_line(180,70,280,70,width=10,tags='r2')
cv.tag_bind('r2','<Button-3>',drawline)
cv.pack()
root.mainloop()
'''
#KeyPress键盘事件的例子
def printkey(event):
    print("你按下了："+event.char)
root=Tk()
entry=Entry(root)
entry.bind('<KeyPress>',printkey)
entry.pack()
root.mainloop()
