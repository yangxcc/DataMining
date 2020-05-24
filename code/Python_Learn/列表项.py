import tkinter
def callbutton1():
    for i in listb1.curselection():
        listb2.insert(0,listb1.get(i))

def callbutton2():
    for i in listb2.curselection():
        listb2.delete(i)

root=tkinter.Tk()
listb1=tkinter.Listbox(root)
listb2=tkinter.Listbox(root)
b1=tkinter.Button(root,text='添加>>',command=callbutton1)
b2=tkinter.Button(root,text='删除<<',command=callbutton2)
li=['php','python','java','c#','c++','sql']
for item in li:
    listb1.insert(0,item)

listb1.grid(row=0,column=0,rowspan=2)
b1.grid(row=0,column=1,rowspan=2)
b2.grid(row=1,column=1,rowspan=2)
listb2.grid(row=0,column=2,rowspan=2)
root.mainloop()
