'''f=open("E:\python的workspace\hello.txt")
#f.close()
print(f.read())
f.close()
'''

'''f=open("E:\python的workspace\hello.txt","w")

用写模式打开已有文件时文件的原有内容被清空，所以在此读取时长度为0

#print(f.read())
f.write("Frist Line.\nSecond Line\n")
f.close()
f=open("E:\python的workspace\hello.txt","a")  #a是追加模式
f.write("Third Line")
f.close()
f=open("E:\python的workspace\hello.txt")
print(f.read())
'''

#文件复制功能
def copy_file(oldfile,newfile):
    oldfile=open(oldfile,"r")
    newfile=open(newfile,"w")
    while True:
        filecontext=oldfile.readline()
        if filecontext=="":
            break
        newfile.write(filecontext)
    oldfile.close()
    newfile.close()
    return

copy_file("E:\python的workspace\hello.txt","E:\python的workspace\hello2.txt")

f=open("E:\python的workspace\hello.txt")
print(f.read(2))
print(f.read(4))
print(f.tell())   #当前位置与起始位置的字节偏移量


#文件的关闭
'''
确保文件的关闭，可以在try...finally模块中写
f=open("xxxx")
try: 
    对文件的操作
finally:
      f.close()
      
第二种方式  with open("xxxx") as f:

必须在文件使用后关闭文件保证文件内容不会丢失

'''